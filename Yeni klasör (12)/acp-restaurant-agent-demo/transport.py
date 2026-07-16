import json
import socket
import time


def send_request(host: str, port: int, method: str, params: dict, request_id: int = 1) -> dict:
    request = {"jsonrpc": "2.0", "method": method, "params": params, "id": request_id}
    print(f"\n>>> istek  {method} -> 127.0.0.1:{port}")
    print(json.dumps(request, ensure_ascii=False, indent=2))

    with socket.create_connection((host, port), timeout=60) as sock:
        sock.sendall((json.dumps(request) + "\n").encode("utf-8"))
        sock.shutdown(socket.SHUT_WR)
        chunks = []
        while True:
            chunk = sock.recv(4096)
            if not chunk:
                break
            chunks.append(chunk)

    response = json.loads(b"".join(chunks).decode("utf-8"))
    print(f"<<< cevap  {method}")
    print(json.dumps(response, ensure_ascii=False, indent=2))

    if "error" in response:
        raise RuntimeError(response["error"])
    return response["result"]


def serve(port: int, handler) -> None:
    """handler(method: str, params: dict) -> dict; her bağlantıda tek istek/cevap işler."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind(("127.0.0.1", port))
        server.listen(5)
        print(f"[agent] 127.0.0.1:{port} dinleniyor...", flush=True)
        while True:
            conn, _ = server.accept()
            with conn:
                data = b""
                while not data.endswith(b"\n"):
                    chunk = conn.recv(4096)
                    if not chunk:
                        break
                    data += chunk

                if not data.strip():
                    # wait_for_port gibi salt bağlantı yoklamalarını yok say
                    continue

                try:
                    request = json.loads(data.decode("utf-8"))
                    method = request["method"]
                    params = request.get("params", {})
                    request_id = request.get("id")
                    try:
                        result = handler(method, params)
                        response = {"jsonrpc": "2.0", "result": result, "id": request_id}
                    except Exception as exc:
                        response = {"jsonrpc": "2.0", "error": str(exc), "id": request_id}
                    conn.sendall(json.dumps(response).encode("utf-8"))
                except Exception as exc:
                    print(f"[agent] geçersiz istek yok sayıldı: {exc}")


def wait_for_port(host: str, port: int, timeout: float = 10.0) -> None:
    deadline = time.time() + timeout
    while time.time() < deadline:
        try:
            with socket.create_connection((host, port), timeout=0.5):
                return
        except OSError:
            time.sleep(0.2)
    raise TimeoutError(f"{host}:{port} zaman aşımına uğradı")
