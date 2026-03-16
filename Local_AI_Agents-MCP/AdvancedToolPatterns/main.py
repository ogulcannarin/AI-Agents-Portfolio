from tools import scan_repository
from analyzer import analyze_project
from llm_analyzer import llm_project_analysis

path = "./test_repo"

files = scan_repository(path)

report = analyze_project(files)

analysis = llm_project_analysis(report)

print("PROJECT REPORT")
print(report)

print("\nLLM ANALYSIS")
print(analysis)