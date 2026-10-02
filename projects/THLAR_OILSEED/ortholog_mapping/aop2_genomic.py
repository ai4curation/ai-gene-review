"""Search the genomic region of the pennycress AOP2 candidate for coding sequence its gene model omits.

The AOP2-type candidate A0AAU9SS97 / TAV2_LOCUS22152 (CDS CAH2071852 on OU466862.2, chromosome 6)
is flagged by UniProt as a fragment and aligns only to residues ~3-179 and ~318-430 of Brassica rapa
AOP2 (GSL-ALK, B5KJ58). This script:

1. fetches the annotated CDS exon coordinates from ENA,
2. fetches the genomic region around the locus from ENA,
3. translates all six frames into stop-free open segments (>= MIN_AA residues),
4. aligns B. rapa AOP2 and Arabidopsis AOP2 (Cvi-0, Q945B5) against those segments with phmmer,
5. reports, for every aligned segment, its genomic span, strand and frame, which comparator
   residues it covers, and whether it lies inside an annotated exon or inside an annotated intron.

Comparator residues matched only by segments outside the annotated exons indicate coding sequence
that the gene model misses. Nothing is hard-coded except the accession of the CDS to inspect.

Usage: uv run python aop2_genomic.py
"""

from __future__ import annotations

import csv
import re

import pyhmmer
import requests

from find_orthologs import ALPHABET, DATA, HERE, RESULTS, UNIPROT, acc, fetch, read_fasta

CDS_PROTEIN_ID = "CAH2071852"
# neighbouring AOP-like model (TAV2_LOCUS20419, A0AAU9SRQ3) whose position is reported for context
NEIGHBOUR_PROTEIN_IDS = ["CAH2071850"]
FLANK = 3000
MIN_AA = 20
COMPARATORS = ["B5KJ58", "Q945B5"]
ENA = "https://www.ebi.ac.uk/ena/browser/api"

CODON = {}
_bases = "TCAG"
_aas = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
for i, a in enumerate(_bases):
    for j, b in enumerate(_bases):
        for k, c in enumerate(_bases):
            CODON[a + b + c] = _aas[16 * i + 4 * j + k]


def revcomp(s: str) -> str:
    return s.translate(str.maketrans("ACGTN", "TGCAN"))[::-1]


def cds_exons(protein_id: str) -> tuple[str, str, list[tuple[int, int]]]:
    txt = requests.get(f"{ENA}/embl/{protein_id}", timeout=120).text
    block = re.search(r"^FT   CDS\s+(.*?)(?=^FT   \s+/)", txt, re.S | re.M).group(1)
    loc = re.sub(r"\s|FT", "", block)
    strand = "-" if loc.startswith("complement") else "+"
    seqid = re.search(r"([A-Z]{2}\d+\.\d+):", loc).group(1)
    exons = [(int(a), int(b)) for a, b in re.findall(r":<?(\d+)\.\.>?(\d+)", loc)]
    return seqid, strand, sorted(exons)


def open_segments(dna: str, offset: int):
    """Yield (strand, frame, genomic_start, genomic_end, peptide) for stop-free stretches."""
    n = len(dna)
    for strand, seq in (("+", dna), ("-", revcomp(dna))):
        for frame in range(3):
            pep = "".join(CODON.get(seq[i:i + 3], "X") for i in range(frame, n - 2, 3))
            for m in re.finditer(r"[^*]+", pep):
                if len(m.group()) < MIN_AA:
                    continue
                s_nt = frame + 3 * m.start()
                e_nt = frame + 3 * m.end() - 1
                if strand == "+":
                    g1, g2 = offset + s_nt, offset + e_nt
                else:
                    g1, g2 = offset + (n - 1 - e_nt), offset + (n - 1 - s_nt)
                yield strand, frame, g1, g2, m.group()


def overlap_class(g1: int, g2: int, exons, strand: str, gene_strand: str) -> str:
    if strand != gene_strand:
        return "opposite strand"
    lo, hi = exons[0][0], exons[-1][1]
    if g2 < lo or g1 > hi:
        return "outside gene span"
    if any(g1 <= b and g2 >= a for a, b in exons):
        return "overlaps annotated exon"
    return "within annotated intron"


def intron_bp_inside(g1: int, g2: int, exons) -> int:
    """Base pairs of annotated introns (gaps between consecutive exons) lying inside [g1, g2]."""
    total = 0
    for (a1, b1), (a2, b2) in zip(exons, exons[1:]):
        lo, hi = max(g1, b1 + 1), min(g2, a2 - 1)
        total += max(0, hi - lo + 1)
    return total


def main() -> None:
    seqid, gene_strand, exons = cds_exons(CDS_PROTEIN_ID)
    start, end = exons[0][0] - FLANK, exons[-1][1] + FLANK
    region = fetch(f"{ENA}/fasta/{seqid}", DATA / f"{seqid}_{start}-{end}.fasta",
                   {"range": f"{start}-{end}"})
    dna = "".join(l.strip() for l in open(region) if not l.startswith(">")).upper()

    segs = list(open_segments(dna, start))
    targets = pyhmmer.easel.DigitalSequenceBlock(ALPHABET, [
        pyhmmer.easel.TextSequence(name=f"seg{i}", sequence=s[4]).digitize(ALPHABET) for i, s in enumerate(segs)])
    comp_fasta = fetch(f"{UNIPROT}/stream", DATA / "aop_comparators_genomic.fasta",
                       {"query": " OR ".join(f"accession:{a}" for a in COMPARATORS), "format": "fasta"})
    comps = read_fasta(comp_fasta)
    q = pyhmmer.easel.DigitalSequenceBlock(ALPHABET, [c.digitize(ALPHABET) for c in comps])

    rows = []
    for c, hits in zip(comps, pyhmmer.hmmer.phmmer(q, targets, cpus=0, E=1)):
        for h in hits:
            if h.evalue > 1e-3:
                continue
            strand, frame, g1, g2, pep = segs[int(h.name[3:])]
            for d in h.domains.included:
                aln = d.alignment
                cols = [(x, y) for x, y in zip(aln.hmm_sequence, aln.target_sequence) if x not in ".-" and y not in ".-"]
                ident = round(100 * sum(x.upper() == y.upper() for x, y in cols) / max(len(cols), 1), 1)
                rows.append(dict(comparator=acc(c.name), comparator_from=aln.hmm_from, comparator_to=aln.hmm_to,
                                 identity_pct=ident,
                                 strand=strand, frame=frame, segment_genomic=f"{g1}-{g2}",
                                 segment_aa=len(pep), evalue=f"{h.evalue:.1e}",
                                 location=overlap_class(g1, g2, exons, strand, gene_strand),
                                 annotated_intron_bp_inside=intron_bp_inside(g1, g2, exons) if strand == gene_strand else 0))
    rows.sort(key=lambda r: (r["comparator"], r["comparator_from"]))

    RESULTS.mkdir(exist_ok=True)
    with open(RESULTS / "aop2_genomic.tsv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()), delimiter="\t")
        w.writeheader()
        w.writerows(rows)

    L = ["---", 'title: "Pennycress AOP2 genomic check"', "species: [THLAR, ARATH]", "---", "",
         "# Genomic check of the pennycress AOP2 candidate", "",
         "Generated by `aop2_genomic.py`; do not edit by hand. Interpretation is in CALLS.md.", "",
         f"CDS {CDS_PROTEIN_ID} on {seqid}, strand {gene_strand}; annotated exons: " +
         ", ".join(f"{a}-{b}" for a, b in exons) + ".",
         f"Region searched: {seqid}:{start}-{end}; six-frame stop-free segments of at least {MIN_AA} aa.", "",
         "| Comparator | Comparator residues | %id | Genomic segment | Strand/frame | Segment aa | E-value | Location | Annotated intron bp inside open segment |",
         "|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        L.append(f"| {r['comparator']} | {r['comparator_from']}-{r['comparator_to']} | {r['identity_pct']} | {r['segment_genomic']} | "
                 f"{r['strand']}/{r['frame']} | {r['segment_aa']} | {r['evalue']} | {r['location']} | {r['annotated_intron_bp_inside']} |")
    # annotated exons with no aligned same-strand segment over them
    aligned = [tuple(map(int, r["segment_genomic"].split("-"))) for r in rows
               if r["strand"] == gene_strand and r["comparator"] == COMPARATORS[0]]
    unsupported = [(a, b) for a, b in exons if not any(a <= g2 and b >= g1 for g1, g2 in aligned)]
    L += ["", f"Annotated exons not covered by any {COMPARATORS[0]}-aligned segment: " +
          (", ".join(f"{a}-{b}" for a, b in unsupported) if unsupported else "none") + "."]
    # neighbouring AOP-like model(s): genomic position relative to this locus
    L += ["", "## Neighbouring model(s)", "",
          "| CDS | Sequence | Strand | Span | Gap to this locus (bp) |", "|---|---|---|---|---|"]
    for pid in NEIGHBOUR_PROTEIN_IDS:
        nseq, nstrand, nex = cds_exons(pid)
        n1, n2 = nex[0][0], nex[-1][1]
        gap = exons[0][0] - n2 - 1 if n2 < exons[0][0] else n1 - exons[-1][1] - 1
        same = "same sequence" if nseq == seqid else "different sequence"
        L.append(f"| {pid} | {nseq} ({same}) | {nstrand} | {n1}-{n2} | {gap} |")
    (HERE / "AOP2_GENOMIC_RESULTS.md").write_text("\n".join(L) + "\n")
    print(f"{len(rows)} aligned segments; wrote results/aop2_genomic.tsv")


if __name__ == "__main__":
    main()
