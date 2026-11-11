"""Compare every horse DYNLT2B UniProt/Ensembl gene model with human Q8WW35.

Run with the repository environment:
  uv run python genes/HORSE/DYNLT2B/DYNLT2B-bioinformatics/compare_gene_models_rereview.py

Fetches (live) the horse UniProtKB entries for gene DYNLT2B, the Ensembl gene
record (canonical transcript flag), and the UniProt reference-proteome
one-protein-per-gene FASTA to identify the gene-centric canonical entry. Each
horse model is globally aligned to the human reference and the mapping of the
human beta-strands (from the cached human UniProt record) is reported.
Writes models-rereview.json and RESULTS-rereview.md next to this script.
"""

import gzip
import io
import json
from pathlib import Path

import requests
from Bio import Align, SeqIO
from Bio.Align import substitution_matrices

here = Path(__file__).resolve().parent
root = next(p for p in here.parents if (p / "pyproject.toml").exists())
HUMAN_FILE = root / "genes/human/DYNLT2B/DYNLT2B-uniprot.txt"
BENCHMARK = "A0A9L0SWY1"
ENSEMBL_GENE = "ENSECAG00000015913"
REFPROT = (
    "https://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/"
    "reference_proteomes/Eukaryota/UP000002281/UP000002281_9796.fasta.gz"
)

human = SeqIO.read(HUMAN_FILE, "swiss")
hseq = str(human.seq)
strands = [
    (int(f.location.start), int(f.location.end))
    for f in human.features
    if f.type == "STRAND"
]

search = requests.get(
    "https://rest.uniprot.org/uniprotkb/search",
    params={
        "query": "gene_exact:DYNLT2B AND organism_id:9796",
        "fields": "accession,length,xref_ensembl,xref_panther",
        "format": "tsv",
    },
    timeout=60,
)
search.raise_for_status()
rows = [line.split("\t") for line in search.text.strip().split("\n")[1:]]

ens = requests.get(
    f"https://rest.ensembl.org/lookup/id/{ENSEMBL_GENE}",
    params={"expand": 1},
    headers={"Content-Type": "application/json"},
    timeout=60,
).json()
canonical_tx = ens["canonical_transcript"].split(".")[0]

refprot_fasta = gzip.decompress(requests.get(REFPROT, timeout=300).content).decode()
gene_centric = [
    line.split("|")[1]
    for line in refprot_fasta.splitlines()
    if line.startswith(">") and "GN=DYNLT2B " in line
]

aligner = Align.PairwiseAligner(
    mode="global",
    substitution_matrix=substitution_matrices.load("BLOSUM62"),
    open_gap_score=-10,
    extend_gap_score=-0.5,
)

models = []
for acc, length, ensembl, panther in rows:
    fasta = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60).text
    seq = str(SeqIO.read(io.StringIO(fasta), "fasta").seq)
    al = aligner.align(hseq, seq)[0]
    hmap = {}
    for (s, e), (t, u) in zip(*al.aligned):
        for i, j in zip(range(s, e), range(t, u)):
            hmap[i] = j
    ident = sum(hseq[i] == seq[j] for i, j in hmap.items())
    strand_cov = [
        {
            "human_strand": f"{s + 1}-{e}",
            "mapped": sum(1 for i in range(s, e) if i in hmap),
            "length": e - s,
        }
        for s, e in strands
    ]
    models.append(
        {
            "accession": acc,
            "length": len(seq),
            "ensembl_transcripts": ensembl.strip(";"),
            "ensembl_canonical": canonical_tx in ensembl,
            "uniprot_gene_centric_canonical": acc in gene_centric,
            "panther": panther.strip(";"),
            "starts_with_met": seq.startswith("M"),
            "paired_with_human": len(hmap),
            "identity_paired_percent": round(100 * ident / len(hmap), 2),
            "human_coverage_percent": round(100 * len(hmap) / len(hseq), 2),
            "c_terminal_25": seq[-25:],
            "human_strands": strand_cov,
            "all_human_strands_complete": all(x["mapped"] == x["length"] for x in strand_cov),
        }
    )

models.sort(key=lambda m: m["accession"])
(here / "models-rereview.json").write_text(json.dumps(
    {"human": human.id, "human_length": len(hseq), "ensembl_canonical_transcript": canonical_tx,
     "uniprot_gene_centric": gene_centric, "models": models}, indent=2) + "\n")

out = [
    "# DYNLT2B horse gene models vs human Q8WW35 (re-review)",
    "",
    f"Human reference {human.id} ({len(hseq)} aa). Ensembl canonical transcript of {ENSEMBL_GENE}: "
    f"{canonical_tx}. UniProt reference-proteome gene-centric entry: {', '.join(gene_centric) or 'none'}.",
    "",
    "| accession | len | Ens canonical | UniProt gene-centric | Met start | identity % | human cov % | all human strands | C-terminus |",
    "|---|---|---|---|---|---|---|---|---|",
]
for m in models:
    flag = " (benchmark)" if m["accession"] == BENCHMARK else ""
    out.append(
        f"| {m['accession']}{flag} | {m['length']} | {m['ensembl_canonical']} | {m['uniprot_gene_centric_canonical']} | "
        f"{m['starts_with_met']} | {m['identity_paired_percent']} | {m['human_coverage_percent']} | "
        f"{m['all_human_strands_complete']} | {m['c_terminal_25']} |"
    )
out += [
    "",
    "Global alignment: Biopython PairwiseAligner, BLOSUM62, gap open -10, extension -0.5. "
    "Strand coverage counts human STRAND residues (from the cached human UniProt record) that pair with a horse residue. "
    "Per-strand details are in `models-rereview.json`. This is a gene-model comparison, not a transcript-support assessment.",
    "",
]
(here / "RESULTS-rereview.md").write_text("\n".join(out))
print("\n".join(out))
