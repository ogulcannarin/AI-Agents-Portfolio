from transport import serve


def handle(method: str, params: dict) -> dict:
    if method != "finalize":
        raise ValueError(f"bilinmeyen method: {method}")
    ranked = params["ranked"]
    return {"top_3": ranked[:3]}


if __name__ == "__main__":
    serve(8903, handle)
