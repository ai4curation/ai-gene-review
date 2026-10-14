"""Fetch OpenCell (PMID:35271311) and Human Protein Atlas subcellular localization for AVL9.

OpenCell endogenously tags proteins in HEK293T cells and assigns each localization category a
grade; the grade legend is read from the OpenCell web bundle rather than hard-coded. The HPA
search API returns the antibody-based subcellular location calls.
    uv run python opencell_localization.py
"""
import json
import re
import urllib.request

BASE = "https://opencell.czbiohub.org"
TARGETS = ("AVL9",)
HPA = "https://www.proteinatlas.org/api/search_download.php?search={g}&format=json&columns=g,scl,scml,scal&compress=no"


def get(url: str) -> str:
    with urllib.request.urlopen(url) as r:
        return r.read().decode()


def main() -> None:
    lines = json.loads(get(f"{BASE}/api/lines"))
    print(f"OpenCell lines: {len(lines)}")
    found = {x["metadata"]["target_name"]: x for x in lines if x["metadata"]["target_name"] in TARGETS}
    for t in TARGETS:
        if t in found:
            m = found[t]["metadata"]
            print(f"{t}\tcell_line_id={m['cell_line_id']}\tterminus={m['target_terminus']}\tcategories={found[t]['annotation']['categories']}")
        else:
            print(f"{t}\tnot in OpenCell")
    html = get(BASE + "/")
    bundle = re.search(r'src="(/[^"]+-bundle\.js)"', html).group(1)
    js = get(BASE + bundle)
    for name, grade in re.findall(r'name:"([^"]+)",grade:"([123])"', js):
        print(f"grade {grade} = {name}")
    for t in TARGETS:
        for row in json.loads(get(HPA.format(g=t))):
            if row["Gene"] == t:
                print(f"HPA\t{t}\tmain={row['Subcellular main location']}\tadditional={row['Subcellular additional location']}")


if __name__ == "__main__":
    main()
