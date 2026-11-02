"""Extract published DOCX tables and match terminal primer translations to proteins.
No reference sequences or expected matches are embedded in this script.
"""

import argparse
import hashlib
import re
import zipfile
from pathlib import Path
import xml.etree.ElementTree as ET
from Bio.Seq import Seq
import yaml

p = argparse.ArgumentParser()
p.add_argument("--docx", type=Path, required=True)
p.add_argument("--proteins", type=Path, nargs="+", required=True)
p.add_argument("--output", type=Path, required=True)
p.add_argument("--text-output", type=Path, required=True)
a = p.parse_args()
ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
with zipfile.ZipFile(a.docx) as z:
    root = ET.fromstring(z.read("word/document.xml"))
paragraphs = ["".join(t.itertext()) for t in root.findall(".//w:p", ns)]
a.text_output.write_text("\n".join(paragraphs) + "\n")
proteins = []
for path in a.proteins:
    text = path.read_text()
    seq = "".join(
        re.findall(
            "[A-Z]+", text.split("SQ   SEQUENCE", 1)[1].split("\n", 1)[1].split("//")[0]
        )
    )
    proteins.append(
        {
            "path": str(path),
            "accession": re.search(r"^AC   (\w+);", text, re.M)[1],
            "length": len(seq),
            "sequence": seq,
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        }
    )
primers = []
for tr in root.findall(".//w:tr", ns):
    cells = ["".join(n.itertext()).strip() for n in tr.findall("w:tc", ns)]
    if len(cells) < 2:
        continue
    name, nt = cells[:2]
    nt = re.sub(r"\s+", "", nt)
    if len(nt) < 15 or re.fullmatch("[ACGTacgt]+", nt) is None:
        continue
    matches = []
    for direction, dna in [
        ("forward", nt.upper()),
        ("reverse_complement", str(Seq(nt).reverse_complement()).upper()),
    ]:
        for frame in range(3):
            aa = str(Seq(dna[frame : len(dna) - (len(dna) - frame) % 3]).translate())
            for protein in proteins:
                seq = protein["sequence"]
                # Find the longest terminal exact match, at least 6 aa. Ignore the
                # noncoding restriction/adaptor sequence and allow a terminal stop.
                for n in range(min(len(aa), len(seq)), 5, -1):
                    for end, part in [("N", seq[:n]), ("C", seq[-n:])]:
                        if part in aa:
                            matches.append(
                                {
                                    "accession": protein["accession"],
                                    "end": end,
                                    "amino_acids": part,
                                    "length": n,
                                    "orientation": direction,
                                    "frame": frame,
                                    "primer_translation": aa,
                                }
                            )
                    if any(
                        m["accession"] == protein["accession"]
                        and m["orientation"] == direction
                        and m["frame"] == frame
                        for m in matches
                    ):
                        break
    primers.append({"name": name, "sequence": nt, "matches": matches})
report = {
    "source": {
        "file": str(a.docx),
        "sha256": hashlib.sha256(a.docx.read_bytes()).hexdigest(),
        "md5": hashlib.md5(a.docx.read_bytes()).hexdigest(),
    },
    "method": {
        "minimum_terminal_match_aa": 6,
        "frames": "all three, both orientations",
    },
    "proteins": [{k: v for k, v in r.items() if k != "sequence"} for r in proteins],
    "primers": primers,
}
a.output.write_text(yaml.safe_dump(report, sort_keys=False, width=100))
print(f"Extracted {len(primers)} primers against {len(proteins)} proteins")
