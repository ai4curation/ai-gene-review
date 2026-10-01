"""Characterize pennycress AOP (2-oxoglutarate-dependent dioxygenase) gene models.

Question: does the pennycress reference proteome (UP000836841) contain a complete AOP2, as expected
for a species whose seed glucosinolate is dominated by allylglucosinolate (sinigrin)?

Steps (all computed, nothing hard-coded):
1. Collect pennycress candidates: every proteome entry hit by phmmer with Arabidopsis AOP2 (Cvi-0,
   Q945B5) whose best Arabidopsis match is an AOP gene (AOP1/AOP2/AOP3).
2. For each candidate, align to each comparator (Arabidopsis AOP1, AOP2 Cvi-0, AOP2 Col-0, AOP3 and
   Brassica rapa GSL-ALK) and report identity and the comparator span covered.
3. Run the Pfam HMMs of the two halves of the 2-ODD fold (PF14226 DIOX_N, PF03171 2OG-FeII_Oxy)
   over every candidate and comparator, reporting each domain's envelope. A fused gene model shows
   up as repeated domain pairs; a truncated one as a missing domain or partial envelope.

Requires find_orthologs.py to have been run once (reuses data/THLAR_*.fasta.gz and data/ARATH_*).
Writes results/aop2_check.tsv, results/aop2_domains.tsv and AOP2_RESULTS.md.

Usage: uv run python aop2_check.py
"""

from __future__ import annotations

import csv
import gzip
from pathlib import Path

import pyhmmer
import requests

from find_orthologs import (
    ALPHABET, DATA, HERE, RESULTS, UNIPROT, acc, fetch, gene_name, identity_and_coverage,
    proteome_fasta, read_fasta,
)

COMPARATORS = {
    "Q9ZTA3": "AOP1 (Arabidopsis Col-0)",
    "Q945B5": "AOP2 (Arabidopsis Cvi-0, functional)",
    "Q9ZTA2": "AOP2 (Arabidopsis Col-0, non-functional)",
    "Q9ZTA1": "AOP3 (Arabidopsis Col-0)",
    "B5KJ58": "GSL-ALK/AOP2 (Brassica rapa)",
}
PFAM = {"PF14226": "DIOX_N", "PF03171": "2OG-FeII_Oxy"}
AOP_GENES = {"AOP1", "AOP1.1", "AOP2", "AOP3"}


def pfam_hmm(pfam_id: str) -> pyhmmer.plan7.HMM:
    path = fetch(f"https://www.ebi.ac.uk/interpro/api/entry/pfam/{pfam_id}?annotation=hmm",
                 DATA / f"{pfam_id}.hmm.gz")
    with pyhmmer.plan7.HMMFile(gzip.open(path, "rb")) as fh:
        return fh.read()


def main() -> None:
    comp_fasta = fetch(f"{UNIPROT}/stream", DATA / "aop_comparators.fasta",
                       {"query": " OR ".join(f"accession:{a}" for a in COMPARATORS), "format": "fasta"})
    comps = {acc(s.name): s for s in read_fasta(comp_fasta)}
    thlar = {s.name: s for s in read_fasta(proteome_fasta("THLAR"))}
    arath = read_fasta(next(DATA.glob("ARATH_*.fasta.gz")))
    arath_db = arath + [s for a, s in comps.items() if "OX=3702" in s.description and a not in {acc(x.name) for x in arath}]
    thlar_d = pyhmmer.easel.DigitalSequenceBlock(ALPHABET, [s.digitize(ALPHABET) for s in thlar.values()])
    arath_d = pyhmmer.easel.DigitalSequenceBlock(ALPHABET, [s.digitize(ALPHABET) for s in arath_db])
    arath_desc = {s.name: s.description for s in arath_db}

    # 1. candidates: pennycress hits of AOP2 whose reverse best hit is an AOP gene
    q = pyhmmer.easel.DigitalSequenceBlock(ALPHABET, [comps["Q945B5"].digitize(ALPHABET)])
    fwd = [h for h in next(iter(pyhmmer.hmmer.phmmer(q, thlar_d, cpus=0))) if h.included][:15]
    rq = pyhmmer.easel.DigitalSequenceBlock(ALPHABET, [thlar[h.name].digitize(ALPHABET) for h in fwd])
    cands = []
    for h, rhits in zip(fwd, pyhmmer.hmmer.phmmer(rq, arath_d, cpus=0)):
        rb = next((x for x in rhits if x.included), None)
        rgene = gene_name(arath_desc.get(rb.name, "")) if rb else ""
        if rgene.upper() in AOP_GENES:
            cands.append((h.name, rgene))

    # 2. pairwise identity / comparator coverage
    rows = []
    cand_block = pyhmmer.easel.DigitalSequenceBlock(ALPHABET, [thlar[n].digitize(ALPHABET) for n, _ in cands])
    comp_list = list(comps.values())
    comp_q = pyhmmer.easel.DigitalSequenceBlock(ALPHABET, [s.digitize(ALPHABET) for s in comp_list])
    for cs, hits in zip(comp_list, pyhmmer.hmmer.phmmer(comp_q, cand_block, cpus=0, E=10)):
        by_name = {h.name: h for h in hits}
        for name, rgene in cands:
            h = by_name.get(name)
            ident, cov = identity_and_coverage(h, len(cs.sequence)) if h is not None else ("", "")
            spans = ";".join(f"{d.alignment.hmm_from}-{d.alignment.hmm_to}" for d in h.domains.included) if h is not None else ""
            rows.append(dict(candidate=acc(name), locus=gene_name(thlar[name].description),
                             candidate_len=len(thlar[name].sequence), reverse_best_aop=rgene,
                             comparator=acc(cs.name), comparator_desc=COMPARATORS[acc(cs.name)],
                             comparator_len=len(cs.sequence), identity_pct=ident,
                             comparator_cov_pct=cov, comparator_spans=spans,
                             bitscore=round(h.score, 1) if h is not None else ""))

    # 3. Pfam domain architecture
    seqs = [thlar[n] for n, _ in cands] + comp_list
    block = pyhmmer.easel.DigitalSequenceBlock(ALPHABET, [s.digitize(ALPHABET) for s in seqs])
    dom_rows = []
    for pid, label in PFAM.items():
        hmm = pfam_hmm(pid)
        for hits in pyhmmer.hmmer.hmmsearch([hmm], block, cpus=0, E=10, domE=1):
            for h in hits:
                for d in h.domains:
                    if d.i_evalue > 0.01:
                        continue
                    dom_rows.append(dict(sequence=acc(h.name), domain=f"{pid} {label}",
                                         env_from=d.env_from, env_to=d.env_to,
                                         hmm_from=d.alignment.hmm_from, hmm_to=d.alignment.hmm_to,
                                         hmm_len=hmm.M, i_evalue=f"{d.i_evalue:.1e}"))
    dom_rows.sort(key=lambda r: (r["sequence"], r["env_from"]))

    RESULTS.mkdir(exist_ok=True)
    for path, data in ((RESULTS / "aop2_check.tsv", rows), (RESULTS / "aop2_domains.tsv", dom_rows)):
        with open(path, "w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=list(data[0].keys()), delimiter="\t")
            w.writeheader()
            w.writerows(data)
    write_md(cands, rows, dom_rows, thlar, comps)
    print(f"{len(cands)} pennycress AOP candidates; wrote results/aop2_check.tsv, results/aop2_domains.tsv")


def write_md(cands, rows, dom_rows, thlar, comps):
    L = ["---", 'title: "Pennycress AOP2 gene-model check"', "species: [THLAR, ARATH]", "---", "",
         "# Pennycress AOP gene models", "",
         "Generated by `aop2_check.py`; do not edit by hand. Interpretation is in CALLS.md.", "",
         "## Candidates (pennycress proteins whose best Arabidopsis match is an AOP gene)", "",
         "| Pennycress | Locus | Length | Reverse best |", "|---|---|---|---|"]
    for n, g in cands:
        L.append(f"| {acc(n)} | {gene_name(thlar[n].description)} | {len(thlar[n].sequence)} | {g} |")
    L += ["", "## Alignment to comparators", "",
          "| Pennycress | Comparator | %id | %cov of comparator | Comparator spans | Bits |",
          "|---|---|---|---|---|---|"]
    for r in rows:
        L.append(f"| {r['candidate']} ({r['candidate_len']} aa) | {r['comparator_desc']} ({r['comparator_len']} aa) | "
                 f"{r['identity_pct']} | {r['comparator_cov_pct']} | {r['comparator_spans']} | {r['bitscore']} |")
    L += ["", "## Pfam domains (i-Evalue <= 0.01)", "",
          "| Sequence | Domain | Envelope | HMM coords (of length) | i-Evalue |", "|---|---|---|---|---|"]
    for d in dom_rows:
        L.append(f"| {d['sequence']} | {d['domain']} | {d['env_from']}-{d['env_to']} | "
                 f"{d['hmm_from']}-{d['hmm_to']} ({d['hmm_len']}) | {d['i_evalue']} |")
    (HERE / "AOP2_RESULTS.md").write_text("\n".join(L) + "\n")


if __name__ == "__main__":
    main()
