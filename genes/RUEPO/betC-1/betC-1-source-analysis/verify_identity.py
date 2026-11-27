"""Verify Ruegeria mutant primers and protein identity against frozen sources.

Run from the repository root with uv run python <this file>. The committed
genomic window contains all primer matches. Full-genome uniqueness can also be
rechecked when the original cached CP000031.fasta is present. No network calls.
"""
from pathlib import Path
import hashlib
import json
import re
from zipfile import ZipFile
from Bio import SeqIO
from Bio.Seq import Seq
from lxml import etree

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
with ZipFile(HERE / "EMI-17-5048-s001.docx") as doc:
    xml = etree.fromstring(doc.read("word/document.xml"))
rows = [["".join(c.xpath(".//w:t/text()", namespaces=NS))
         for c in row.xpath("./w:tc", namespaces=NS)]
        for row in xml.xpath("//w:tr", namespaces=NS)]
assert "\n".join("\t".join(row) for row in rows) + "\n" == (
    HERE / "EMI-17-5048-s001-tables.txt").read_text()
window = str(SeqIO.read(HERE / "CP000031.2-1137800-1143500.fasta", "fasta").seq)
genome_path = ROOT / ".cache/module-audit-logs/choline-sulfate-20261106/CP000031.fasta"
genome = str(SeqIO.read(genome_path, "fasta").seq) if genome_path.exists() else None
if genome:
    provenance = json.loads((HERE / "provenance.json").read_text())
    assert hashlib.sha256(genome.encode()).hexdigest() == provenance["genome"]["sequence_sha256"]
    assert genome[1137799:1143500] == window
primers = []
for row in rows:
    if len(row) != 3 or not any(x in row[0] for x in ("Spo1083", "Spo1087")):
        continue
    name, sequence, use = row
    sequence = re.sub("[^ACGT]", "", sequence)
    # Cloning primers carry the documented CAAT clamp plus six-base restriction site.
    annealing = sequence[10:] if sequence.startswith("CAAT") else sequence
    hits = []
    for strand, target in [("+", annealing), ("-", str(Seq(annealing).reverse_complement()))]:
        hits.extend({"start": m.start() + 1137800, "strand": strand}
                    for m in re.finditer(target, window))
    assert len(hits) == 1, (name, hits)
    if genome:
        count = len(list(re.finditer(annealing, genome))) + len(list(re.finditer(str(Seq(annealing).reverse_complement()), genome)))
        assert count == 1, (name, count)
    primers.append({"name": name.strip(), "source_sequence": row[1], "annealing_sequence": annealing,
                    "use": use, "genome_hits": hits, "full_genome_uniqueness_checked": genome is not None})
proteins = []
for gene, accession in [("betC-1", "AAV94383.1"), ("SPO1087", "AAV94387.1")]:
    original = SeqIO.read(HERE / (accession + ".gp"), "genbank")
    uniprot = SeqIO.read(ROOT / "genes/RUEPO" / gene / (gene + "-uniprot.txt"), "swiss")
    assert original.seq == uniprot.seq
    proteins.append({"gene": gene, "uniprot": uniprot.id, "source_protein": accession,
                     "length": len(original.seq), "identical": True,
                     "coded_by": [f.qualifiers["coded_by"][0] for f in original.features if f.type == "CDS"]})
assert len(primers) == 12
(HERE / "identity-proof.json").write_text(json.dumps({"proteins": proteins, "primers": primers}, indent=2) + "\n")
print("Exact protein matches: 2; unique mapped primers: 12; full-genome check:", genome is not None)
