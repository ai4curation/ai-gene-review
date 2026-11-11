"""Reproducible checks for glo (Q9VGH5).

1. PANTHER 19.0 subfamily of Q9VGH5 and of the PAINT IBA donor proteins
   (read from the release-pinned PANTHER classification files in .cache/panther/).
2. PAINT IBD rows for the nodes cited in the GOA IBA rows (interpro/panther/PTHR13976).
3. Identity of Q9VGH5 (586 aa) with Q8INJ6 (glo isoform C) and which
   RRM domains fall inside the shared region.

Run from the repository root:
    python genes/DROME/glo__Q9VGH5/glo__Q9VGH5-bioinformatics/panther_and_isoform_check.py
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
ACCS = ["Q9VGH5", "Q8INJ6", "Q9BJZ5", "P31943", "P52597", "P55795", "P31942",
        "Q12849", "Q6NXG1", "Q9H6T0"]


def panther_subfamilies():
    out = {}
    for fn in ["PTHR19.0_fruit_fly", "PTHR19.0_human"]:
        for line in (ROOT / ".cache/panther" / fn).read_text().splitlines():
            cols = line.split("\t")
            if len(cols) > 3 and cols[1] in ACCS:
                out[cols[1]] = (cols[2], cols[3])
    return out


def paint_rows():
    path = ROOT / "interpro/panther/PTHR13976/PTHR13976-paint.tsv"
    lines = path.read_text().splitlines()
    return [ln for ln in lines[1:] if "PTN000360053" in ln or "PTN000359854" in ln]


def uniprot_seq(path):
    text = path.read_text()
    m = re.search(r"^SQ .*?\n(.*?)^//", text, re.S | re.M)
    return re.sub(r"[^A-Z]", "", m.group(1))


def domains(path):
    text = path.read_text()
    return re.findall(r"^FT   DOMAIN\s+(\d+)\.\.(\d+)", text, re.M)


def main():
    print("## PANTHER 19.0 subfamilies")
    sub = panther_subfamilies()
    for acc in ACCS:
        print(acc, *sub.get(acc, ("not in PANTHER fly/human files", "")))
    print("\n## PAINT IBD rows for PTN000360053 / PTN000359854")
    for row in sorted(set(paint_rows())):
        print(row)
    full = uniprot_seq(ROOT / "genes/DROME/glo__Q9VGH5/glo__Q9VGH5-uniprot.txt")
    iso_c = uniprot_seq(ROOT / "genes/DROME/glo/glo-uniprot.txt")
    n = 0
    while n < min(len(full), len(iso_c)) and full[n] == iso_c[n]:
        n += 1
    print("\n## Isoform comparison")
    print(f"Q9VGH5 length {len(full)}; Q8INJ6 length {len(iso_c)}; "
          f"identical N-terminal prefix: residues 1-{n}")
    print("Q9VGH5 RRM DOMAIN features (UniProt):",
          domains(ROOT / "genes/DROME/glo__Q9VGH5/glo__Q9VGH5-uniprot.txt"))
    for s, e in domains(ROOT / "genes/DROME/glo__Q9VGH5/glo__Q9VGH5-uniprot.txt"):
        inside = int(e) <= n
        print(f"  domain {s}-{e}: {'within' if inside else 'NOT within'} shared region")


if __name__ == "__main__":
    main()
