"""Which zebrafish gad1 paralog does the classic 'GAD67' cDNA (GenBank AF017266) represent?

Mueller & Guo 2009 (PMID:19673006) state that their GAD67 riboprobe covers nucleotides
151-1964 of AF017266 ("zfin: gad1"). Lueffe et al. 2021/2022 (PMID:34650032, PMID:35769333)
describe their 'gad1a (previously gad67a)' probe as coming from the Martin et al. plasmid.
This script fetches AF017266 from NCBI (E-utilities), takes its CDS translation and the
nucleotide sequence, and compares them with gad1a and gad1b (cached UniProt proteins and
Ensembl canonical cDNAs) so the paralog identity of the classic GAD67 clone is settled from
sequence rather than from names.

Run from the repo root:
    uv run python genes/DANRE/gad1a/gad1a-bioinformatics/probe_identity.py \
        > genes/DANRE/gad1a/gad1a-bioinformatics/probe_identity_output.txt
"""

import json
import re
import time
import urllib.request
from pathlib import Path

from Bio import Align
from Bio.Align import substitution_matrices

ROOT = Path(__file__).resolve().parents[4]
UA = {"User-Agent": "ai-gene-review-probe-identity/1.0"}
ACCESSION = "AF017266"
GENES = {"gad1a": "genes/DANRE/gad1a/gad1a-uniprot.txt", "gad1b": "genes/DANRE/gad1b/gad1b-uniprot.txt"}


def get(url: str, retries: int = 8, headers: dict | None = None) -> bytes:
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers={**UA, **(headers or {})})
            return urllib.request.urlopen(req, timeout=120).read()
        except Exception:  # noqa: BLE001
            if i == retries - 1:
                raise
            time.sleep(3 + 4 * i)
    raise RuntimeError(url)


def fasta_seq(text: str) -> str:
    return "".join(line.strip() for line in text.splitlines() if not line.startswith(">"))


def uniprot_txt_seq(path: Path) -> str:
    m = re.search(r"^SQ .*?\n(.*?)^//", path.read_text(), re.S | re.M)
    return re.sub(r"[\s\d]", "", m.group(1))


def ens(path: str):
    time.sleep(0.2)
    return json.loads(get("https://rest.ensembl.org" + path + ("&" if "?" in path else "?")
                          + "content-type=application/json", headers={"Content-Type": "application/json"}))


def identity(a: str, b: str, protein: bool) -> tuple[float, int, int]:
    al = Align.PairwiseAligner(mode="local")
    if protein:
        al.substitution_matrix = substitution_matrices.load("BLOSUM62")
        al.open_gap_score, al.extend_gap_score = -10, -0.5
    else:
        al.match_score, al.mismatch_score, al.open_gap_score, al.extend_gap_score = 2, -3, -5, -2
    x = al.align(a, b)[0]
    cols = [(p, q) for p, q in zip(x[0], x[1])]
    same = sum(1 for p, q in cols if p == q and p != "-")
    return 100.0 * same / len(cols), same, len(cols)


def main():
    base = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=" + ACCESSION
    nt = fasta_seq(get(base + "&rettype=fasta&retmode=text").decode())
    aa = fasta_seq(get(base + "&rettype=fasta_cds_aa&retmode=text").decode())
    title = get(base + "&rettype=fasta&retmode=text").decode().splitlines()[0]
    print(f"# {ACCESSION}: {title}")
    print(f"nucleotide length {len(nt)}; CDS translation length {len(aa)}\n")
    for g, p in GENES.items():
        prot = uniprot_txt_seq(ROOT / p)
        pid, same, cols = identity(aa, prot, protein=True)
        d = ens(f"/lookup/symbol/danio_rerio/{g}?expand=1")
        tr = [t for t in d["Transcript"] if t.get("is_canonical")][0]
        cdna = ens(f"/sequence/id/{tr['id']}?type=cdna")["seq"]
        nid, nsame, ncols = identity(nt, cdna, protein=False)
        print(f"{g}: protein identity {pid:.1f}% ({same}/{cols} local-alignment columns); "
              f"cDNA identity to Ensembl {tr['id']} {nid:.1f}% ({nsame}/{ncols} columns)")


if __name__ == "__main__":
    main()
