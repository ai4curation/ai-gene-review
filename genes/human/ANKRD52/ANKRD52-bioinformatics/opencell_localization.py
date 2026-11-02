"""Fetch OpenCell (PMID:35271311) localization annotations for ANKRD52.

OpenCell endogenously tags proteins in HEK293T cells and assigns each localization category a
grade. The grade legend is read from the OpenCell web bundle rather than hard-coded:
    uv run python opencell_localization.py
"""
import json
import re
import urllib.request

BASE = "https://opencell.czbiohub.org"
TARGETS = ("ANKRD52",)


def get(url: str) -> str:
    with urllib.request.urlopen(url) as r:
        return r.read().decode()


def main() -> None:
    lines = json.loads(get(f"{BASE}/api/lines"))
    for x in lines:
        if x["metadata"]["target_name"] in TARGETS:
            m = x["metadata"]
            print(f"{m['target_name']}\tcell_line_id={m['cell_line_id']}\tterminus={m['target_terminus']}\tcategories={x['annotation']['categories']}")
    html = get(BASE + "/")
    bundle = re.search(r'src="(/[^"]+-bundle\.js)"', html).group(1)
    js = get(BASE + bundle)
    for name, grade in re.findall(r'name:"([^"]+)",grade:"([123])"', js):
        print(f"grade {grade} = {name}")


if __name__ == "__main__":
    main()
