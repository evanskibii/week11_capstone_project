from pathlib import Path
import re, sys

PATTERNS = [re.compile(r"sk-[A-Za-z0-9_-]{12,}"), re.compile(r"(?i)(api[_-]?key|password|secret)\s*[:=]\s*[^\s]{8,}")]
SKIP = {".git", ".venv", "__pycache__", ".pytest_cache"}
findings=[]
for path in Path(".").rglob("*"):
    if not path.is_file() or any(part in SKIP for part in path.parts) or path.name == Path(__file__).name:
        continue
    try: text=path.read_text(encoding="utf-8")
    except UnicodeDecodeError: continue
    for n,line in enumerate(text.splitlines(),1):
        if "allow-secret-test" in line:
            continue
        if any(p.search(line) for p in PATTERNS): findings.append(f"{path}:{n}")
if findings:
    print("Potential secrets:", *findings, sep="\n")
    sys.exit(1)
print("No configured secret patterns found.")
