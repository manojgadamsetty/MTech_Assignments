from pathlib import Path


BASE = Path("reports")


def read_report(name):
    try:
        return (BASE / name).read_text()
    except Exception as error:
        return str(error)


print("2025MT12100")
for name in ["summary.txt", "missing.txt", "../secret.txt"]:
    print(name, "->", read_report(name))
