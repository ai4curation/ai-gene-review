"""Gene-model and paralog comparison for A0A804UIX9 (Zm00001eb381380_T001).

Fetches sequences from UniProt and transcript structures from Ensembl REST,
aligns the target with its alternative transcript product (A0A804R394,
Zm00001eb381380_T002), the tandem paralog A0A804R017 (Zm00001eb380900) and
other PTHR24177:SF432 members using MAFFT, and reports per-segment identity.

Run: python3 gene_model_rereview.py  (requires mafft on PATH)
"""
import json
import subprocess
import tempfile
import urllib.request

ACCS = ["A0A804UIX9", "A0A804R394", "A0A804R017", "A0A804QG70", "B4FV28",
        "B8B0U1", "A0A0P0WVA6", "Q8LPS2"]
TARGET = "A0A804UIX9"
SEGMENTS = [(1, 44), (45, 200), (201, 297), (298, 375)]


def fetch(url: str) -> str:
    with urllib.request.urlopen(url, timeout=60) as r:
        return r.read().decode()


def parse_fasta(text: str) -> dict:
    seqs, name = {}, None
    for line in text.splitlines():
        line = line.strip()
        if line.startswith(">"):
            name = line.split("|")[1]
            seqs[name] = ""
        elif name:
            seqs[name] += line
    return seqs


def main() -> None:
    fasta = "".join(fetch(f"https://rest.uniprot.org/uniprotkb/{a}.fasta") for a in ACCS)
    with tempfile.NamedTemporaryFile("w", suffix=".fa", delete=False) as fh:
        fh.write(fasta)
    aln = parse_fasta(subprocess.run(["mafft", "--quiet", "--auto", fh.name],
                                     capture_output=True, text=True, check=True).stdout)
    t = aln[TARGET]
    print("## Identity of target segments to each sequence (aligned, ungapped columns)")
    print("cells = identical/aligned target residues")
    print("acc\tlength\t" + "\t".join(f"{a}-{b}" for a, b in SEGMENTS))
    for acc in ACCS:
        if acc == TARGET:
            continue
        o = aln[acc]
        stats = {s: [0, 0] for s in SEGMENTS}
        pos = 0
        for x, y in zip(t, o):
            if x == "-":
                continue
            pos += 1
            seg = next(s for s in SEGMENTS if s[0] <= pos <= s[1])
            if y != "-":
                stats[seg][0] += 1
                stats[seg][1] += x == y
        cells = [f"{stats[s][1]}/{stats[s][0]}" for s in SEGMENTS]
        print(f"{acc}\t{len(o.replace('-', ''))}\t" + "\t".join(cells))
    print("\n## Ensembl transcript structures for Zm00001eb381380")
    d = json.loads(fetch("https://rest.ensembl.org/lookup/id/Zm00001eb381380"
                         "?expand=1;content-type=application/json"))
    for tr in d.get("Transcript", []):
        exons = [(e["start"], e["end"]) for e in tr.get("Exon", [])]
        tl = tr.get("Translation", {})
        print(tr["id"], "canonical" if tr.get("is_canonical") else "",
              "protein_len", tl.get("length"), "CDS", tl.get("start"), tl.get("end"),
              "exons", exons)


if __name__ == "__main__":
    main()
