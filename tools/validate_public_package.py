"""Public teaser integrity checks only: not scientific, legal or security certification."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
ALLOWED = {
    ".gitignore",
    ".github/workflows/validate.yml",
    "README.md",
    "README_RU.md",
    "LEGAL.md",
    "SECURITY.md",
    "assets/kilu-logo.svg",
    "assets/kilu-symbol.svg",
    "docs/PUBLIC_REVIEW.md",
    "docs/ACCESS_POLICY.md",
    "tools/validate_public_package.py",
}
actual = {
    str(p.relative_to(ROOT))
    for p in ROOT.rglob("*")
    if p.is_file() and ".git" not in p.parts and "__pycache__" not in p.parts
}
assert actual == ALLOWED, f"Unexpected public files: {sorted(actual ^ ALLOWED)}"
for p in ROOT.rglob("*.md"):
    data = p.read_text(encoding="utf-8")
    for pattern, label in [
        (r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----", "key"),
        (r"\b(?:ghp_|gho_|github_pat_)\S+", "GitHub token"),
        (r"\b[a-f0-9]{40}\b", "full git SHA"),
        (r"https?://github\.com/IkaRiche/(?:KiLu-Network|DRC_Core|ashby-cells)(?:/|\\b)", "private repository URL"),
        (r"\b(?:Nebius|offer price|acquisition price)\b", "buyer-specific terms"),
        (r"\b\d+(?:\.\d+)?\s*(?:µs|us|KiB|MHz|cycles|bytes)\b", "exact benchmark specification"),
    ]:
        assert not re.search(pattern, data, re.I), f"Possible {label}: {p.relative_to(ROOT)}"
    for link in re.findall(r"!?\[[^\]]+\]\(([^)]+)\)", data):
        target = link.split("#", 1)[0]
        if not target or target.startswith(("https://", "http://", "mailto:", "#")):
            continue
        real = (p.parent / target).resolve()
        assert real.is_relative_to(ROOT) and real.is_file(), f"Broken link: {p}: {link}"
print("PUBLIC_TEASER_STRUCTURE_OK", len(actual), "files")
print("NOT technical, scientific or IP-leak clearance")
