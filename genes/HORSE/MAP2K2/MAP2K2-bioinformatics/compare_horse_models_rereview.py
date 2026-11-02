"""Compare every horse MAP2K2 gene-model product with human MEK2 (P36507) (re-review).

Fetches (live) all horse UniProt entries placed in PANTHER PTHR47448:SF3
(MITOGEN-ACTIVATED PROTEIN KINASE KINASE 2), the Ensembl transcript set of horse
gene ENSECAG00000009157, and human P36507, then for each horse product:

* aligns it globally to human P36507;
* reports identity, coverage, and where it diverges from the human C-terminus;
* checks presence of human landmark residues/segments: ATP Lys101, catalytic
  Asp194 (HRD), activating Ser222/Ser226, the end of the kinase domain (human
  362-369, containing the subdomain XI 'HTF' motif), and the C-terminal tail
  370-400 (DVD docking region and Thr394/Thr396 phosphosites).

Writes RESULTS-rereview.md and results-rereview.json next to this script.
Run from the repository root:
    uv run python genes/HORSE/MAP2K2/MAP2K2-bioinformatics/compare_horse_models_rereview.py
"""

import json
from pathlib import Path
from urllib.request import Request, urlopen

from Bio import Align

HERE = Path(__file__).resolve().parent
HUMAN = "P36507"
TARGET = "A0A9L0SHX8"
HORSE_GENE = "ENSECAG00000009157"
SITES = {101: "K", 194: "D", 222: "S", 226: "S", 394: "T", 396: "T"}
PAINT_TSV = HERE.parents[3] / "interpro/panther/PTHR48013/PTHR48013-paint.tsv"
PAINT_NODE = "PTN000684494"
SEGMENTS = {"kinase_domain_end_362_369": (362, 369), "c_terminal_tail_370_400": (370, 400)}


def get(url: str, accept: str = "text/plain") -> str:
    with urlopen(Request(url, headers={"Accept": accept})) as r:
        return r.read().decode()


def fasta_seq(acc: str) -> str:
    return "".join(get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta").splitlines()[1:])


def horse_entries() -> list[dict]:
    url = (
        "https://rest.uniprot.org/uniprotkb/search?query=xref:panther-PTHR47448"
        "+AND+organism_id:9796&fields=accession,length,gene_names,xref_ensembl,xref_panther&format=tsv"
    )
    out = []
    for row in get(url).strip().splitlines()[1:]:
        acc, length, gene, ens, panther = (row.split("\t") + ["", "", "", "", ""])[:5]
        if "PTHR47448:SF3" not in panther:
            continue
        out.append({"accession": acc, "length": int(length), "gene_name": gene,
                    "ensembl_transcript": ens.strip(";").split(".")[0]})
    return out


def ensembl_transcripts() -> dict:
    d = json.loads(get(f"https://rest.ensembl.org/lookup/id/{HORSE_GENE}?expand=1",
                       accept="application/json"))
    return {t["id"]: {"is_canonical": bool(t.get("is_canonical")),
                      "n_exons": len(t.get("Exon", [])),
                      "translation_length": t.get("Translation", {}).get("length")}
            for t in d["Transcript"]}


def compare(human: str, horse: str) -> dict:
    aligner = Align.PairwiseAligner(mode="global", match_score=2, mismatch_score=-1,
                                    open_gap_score=-10, extend_gap_score=-0.5)
    al = aligner.align(human, horse)[0]
    hmap = {}
    for (s, e), (t, u) in zip(*al.aligned):
        for i, j in zip(range(s, e), range(t, u)):
            hmap[i] = j
    ident = sum(human[i] == horse[j] for i, j in hmap.items())
    # last human position (1-based) such that the preceding 10 aligned positions are all identical
    last_conserved = 0
    for p in range(10, len(human) + 1):
        if all((i in hmap and human[i] == horse[hmap[i]]) for i in range(p - 10, p)):
            last_conserved = p
    sites = {str(p): (horse[hmap[p - 1]] if (p - 1) in hmap else "-") for p in SITES}
    segs = {}
    for name, (a, b) in SEGMENTS.items():
        idx = range(a - 1, b)
        segs[name] = {"identical": sum(1 for i in idx if i in hmap and human[i] == horse[hmap[i]]),
                      "length": b - a + 1}
    return {"paired": len(hmap), "identical": ident,
            "identity_percent": round(100 * ident / len(hmap), 2),
            "human_coverage_percent": round(100 * len(hmap) / len(human), 2),
            "last_human_position_in_conserved_10mer": last_conserved,
            "sites": sites, "segments": segs, "horse_c_terminal_20": horse[-20:]}


def main() -> None:
    human = fasta_seq(HUMAN)
    tx = ensembl_transcripts()
    rows = []
    for e in horse_entries():
        seq = fasta_seq(e["accession"])
        r = {**e, **compare(human, seq), **tx.get(e["ensembl_transcript"], {})}
        rows.append(r)
    rows.sort(key=lambda r: -r["length"])
    (HERE / "results-rereview.json").write_text(json.dumps(
        {"human": HUMAN, "human_length": len(human), "human_c_terminal_20": human[-20:],
         "horse_gene": HORSE_GENE, "target": TARGET, "models": rows}, indent=2) + "\n")
    lines = ["# MAP2K2 (horse): all gene-model products vs human MEK2 P36507 (re-review)", "",
             f"Human P36507 length {len(human)}; C-terminal 20 residues `{human[-20:]}`. "
             f"All horse products below are transcripts of Ensembl gene {HORSE_GENE}.", "",
             "Human landmark residues checked: K101 (ATP), D194 (HRD catalytic base), "
             "S222/S226 (RAF-activated sites), T394/T396 (C-terminal phosphosites).", "",
             "| accession | len | Ensembl transcript | canonical | exons | id% | human cov% | "
             "last conserved human pos | K101 D194 S222 S226 T394 T396 | 362-369 ident | 370-400 ident |",
             "|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        s = " ".join(r["sites"][str(p)] for p in SITES)
        k = r["segments"]["kinase_domain_end_362_369"]
        c = r["segments"]["c_terminal_tail_370_400"]
        mark = " (target)" if r["accession"] == TARGET else ""
        lines.append(f"| {r['accession']}{mark} | {r['length']} | {r['ensembl_transcript']} | "
                     f"{r.get('is_canonical')} | {r.get('n_exons')} | {r['identity_percent']} | "
                     f"{r['human_coverage_percent']} | {r['last_human_position_in_conserved_10mer']} | "
                     f"{s} | {k['identical']}/{k['length']} | {c['identical']}/{c['length']} |")
    lines += ["", f"## PAINT node {PAINT_NODE} (local {PAINT_TSV.name})", ""]
    for row in PAINT_TSV.read_text().splitlines()[1:]:
        c = row.split("\t")
        if c[1] == PAINT_NODE:
            seeds = c[6].split("|")
            lines.append(f"- node {c[1]} asserts {c[2]} ({c[3]}, {c[4]}, negated={c[5]}), "
                         f"taxon {c[7]}; {len(seeds)} seeds; human P36507 among seeds: "
                         f"{'UniProtKB:P36507' in seeds}")
    lines += ["", "Interpretation is in MAP2K2-notes.md; this file reports computed values only."]
    (HERE / "RESULTS-rereview.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
