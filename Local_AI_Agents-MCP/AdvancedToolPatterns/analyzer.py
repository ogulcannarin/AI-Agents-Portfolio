def analyze_project(files):

    total_files = len(files)

    python_files = [f for f in files if f["extension"] == "py"]

    data_files = [f for f in files if f["extension"] in ["csv","xlsx","json"]]

    biggest = max(files, key=lambda x: x["size_kb"])

    report = {
        "total_files": total_files,
        "python_files": len(python_files),
        "data_files": len(data_files),
        "largest_file": biggest["name"]
    }

    return report