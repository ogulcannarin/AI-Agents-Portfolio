import os

def scan_repository(path):
    files = []

    for file in os.listdir(path):
        full_path = os.path.join(path, file)

        if os.path.isfile(full_path):
            size = os.path.getsize(full_path) / 1024

            ext = file.split(".")[-1] if "." in file else "none"

            files.append({
                "name": file,
                "size_kb": round(size,2),
                "extension": ext
            })

    return files