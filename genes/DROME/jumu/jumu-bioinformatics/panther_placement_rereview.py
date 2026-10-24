"""Report PANTHER 19.0 subfamily placement of jumu and FOXN-related proteins.

Reads the release-pinned PANTHER HMM classification files that
`just validate-families` downloads into .cache/panther/ (PTHR19.0_<organism>)
and prints, for each accession of interest, the family/subfamily PANTHER
assigns. Run from the repository root:

    uv run python genes/DROME/jumu/jumu-bioinformatics/panther_placement_rereview.py
"""

from pathlib import Path

ACCESSIONS = {
    "Q9XTP7": "fly jumu",
    "Q96NZ1": "human FOXN4",
    "Q8K3Q3": "mouse Foxn4",
    "A2BGM5": "zebrafish foxn4",
    "Q3BJS1": "Xenopus foxn4",
    "O15353": "human FOXN1",
    "Q61575": "mouse Foxn1",
    "O00409": "human FOXN3",
    "P32314": "human FOXN2",
}

cache = Path(".cache/panther")
found = {}
for f in sorted(cache.glob("PTHR19.0_*")):
    for line in f.read_text().splitlines():
        cols = line.split("\t")
        if len(cols) > 3 and cols[1] in ACCESSIONS:
            found[cols[1]] = (cols[3], f.name)

print("accession\tprotein\tPANTHER_19.0_subfamily\tsource_file")
for acc, name in ACCESSIONS.items():
    sub, src = found.get(acc, ("NOT_FOUND", "-"))
    print(f"{acc}\t{name}\t{sub}\t{src}")
