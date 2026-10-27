from pathlib import Path
import secrets


BITS_ID = "2025MT12100"
BASE = Path("reports").resolve()


def read_report(name):
    reference = secrets.token_hex(4)
    requested = (BASE / name).resolve()
    if not requested.is_relative_to(BASE) or requested.suffix != ".txt":
        print(f"LOG name={name!r} ref={reference}")
        return f"Report not available (ref {reference})"
    try:
        return requested.read_text()
    except OSError:
        print(f"LOG name={name!r} ref={reference}")
        return f"Report not available (ref {reference})"


print(BITS_ID)
for name in ["summary.txt", "report_00.txt", "missing.txt", "../secret.txt", "notes.csv"]:
    print(name, "->", read_report(name))
