# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython>=1.83", "requests"]
# ///
"""Sequence audit of ZNF788P (UniProt Q6ZQV5).

All data are fetched live:
  - Ensembl gene biotype / transcripts for ENSG00000214189;
  - current Q6ZQV5 sequence and every historical sequence version (UniSave);
  - ZNF10/KOX1 (P21506) as a canonical KRAB-A/B + C2H2 reference;
  - the two FLJ cDNAs (AK128282, AK128700) from ENA, translated in 3 frames.
Reports: C2H2 motif counts per sequence version, local alignment of the current
82-aa product to the ZNF10 KRAB domain (with the ZNF10 'DV' and 'MLE' motifs mapped),
and, in each cDNA, which frame encodes the 82-aa KRAB peptide and which encodes the
historical zinc-finger ORF.
Run: uv run --script znf788p_check.py
"""
import re
from datetime import datetime
import requests
from Bio.Seq import Seq
from Bio.Align import PairwiseAligner, substitution_matrices

ACC = "Q6ZQV5"
ENSG = "ENSG00000214189"
REF = "P21506"  # ZNF10 / KOX1
CDNAS = ["AK128282", "AK128700"]
C2H2 = re.compile(r"C..C.{12}H...H|C....C.{12}H...H|C..C.{12}H....H")


def get(url, **kw):
    r = requests.get(url, timeout=60, **kw)
    r.raise_for_status()
    return r


def fasta_seq(text):
    return "".join(l.strip() for l in text.splitlines() if not l.startswith(">"))


def aligner():
    a = PairwiseAligner()
    a.mode = "local"
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -10
    a.extend_gap_score = -0.5
    return a


def main():
    g = get(f"https://rest.ensembl.org/lookup/id/{ENSG}?expand=1",
            headers={"Content-Type": "application/json"}).json()
    print(f"# Ensembl {ENSG}: biotype={g['biotype']} chr{g['seq_region_name']}:{g['start']}-{g['end']}")
    for t in g.get("Transcript", []):
        print(f"  transcript {t['id']} biotype={t['biotype']} translation={t.get('Translation', {}).get('id')}")

    cur = get(f"https://rest.uniprot.org/uniprotkb/{ACC}.json").json()
    cseq = cur["sequence"]["value"]
    print(f"\n# UniProt {ACC} current: length {len(cseq)}, PE={cur.get('proteinExistence')}")
    hist = get(f"https://rest.uniprot.org/unisave/{ACC}?format=json").json()["results"]
    first_entry_for_seqver = {}
    for r in hist:
        first_entry_for_seqver.setdefault(r["sequenceVersion"], r["entryVersion"])
    for r in hist:
        sv = r["sequenceVersion"]
        if first_entry_for_seqver.get(sv) is not None:
            first_entry_for_seqver[sv] = min(first_entry_for_seqver[sv], r["entryVersion"])
    seqs = {}
    for sv, ev in sorted(first_entry_for_seqver.items()):
        s = fasta_seq(get(f"https://rest.uniprot.org/unisave/{ACC}?format=fasta&versions={ev}").text)
        dates = sorted((datetime.strptime(x["firstReleaseDate"], "%d-%b-%Y") for x in hist
                        if x["sequenceVersion"] == sv))
        seqs[sv] = s
        print(f"sequence version {sv} (entry versions from {ev}; first {dates[0].date() if dates else '?'}; last {dates[-1].date() if dates else '?'}): "
              f"length {len(s)}, C2H2 motifs {len(C2H2.findall(s))}, starts {s[:30]}")

    ref = get(f"https://rest.uniprot.org/uniprotkb/{REF}.json").json()
    rseq = ref["sequence"]["value"]
    krab = [f for f in ref["features"] if f["type"] == "Domain" and "KRAB" in f.get("description", "")][0]
    ks, ke = krab["location"]["start"]["value"], krab["location"]["end"]["value"]
    print(f"\n# ZNF10 {REF} KRAB domain {ks}-{ke}; C2H2 motifs in ZNF10: {len(C2H2.findall(rseq))}")
    aln = aligner().align(cseq, rseq[ks - 1:ke])[0]
    m = {}
    ident = 0
    for (a0, a1), (b0, b1) in zip(*aln.aligned):
        for k in range(a1 - a0):
            m[int(b0 + k + ks)] = int(a0 + k + 1)
            ident += cseq[a0 + k] == rseq[b0 + k + ks - 1]
    n = sum(a1 - a0 for a0, a1 in aln.aligned[0])
    print(f"alignment score {aln.score:.1f}; aligned {n}; identical {ident} ({100 * ident / n:.1f}%)")
    print(aln)
    for motif in ("DV", "MLE"):
        for x in re.finditer(motif, rseq[ks - 1:ke]):
            pos = [x.start() + ks + i for i in range(len(motif))]
            tgt = "".join(cseq[m[p] - 1] if p in m else "-" for p in pos)
            print(f"ZNF10 motif {motif} at {pos[0]}-{pos[-1]} -> ZNF788P {tgt} "
                  f"(positions {[m.get(p) for p in pos]})")
    last_aligned_ref = max(m)
    print(f"ZNF788P aligns up to ZNF10 residue {last_aligned_ref} of KRAB {ks}-{ke}; "
          f"ZNF788P ends at residue {len(cseq)} (C-terminal residues after last aligned: "
          f"{len(cseq) - max(m.values())})")

    zf_old = seqs[min(seqs)]
    for acc in CDNAS:
        nt = fasta_seq(get(f"https://www.ebi.ac.uk/ena/browser/api/fasta/{acc}").text)
        print(f"\n# cDNA {acc}: {len(nt)} nt")
        for fr in range(3):
            sub = nt[fr:]
            sub = sub[: len(sub) - len(sub) % 3]
            prot = str(Seq(sub).translate())
            hits = []
            for label, q in (("KRAB peptide (current, aa 22-82)", cseq[21:]), ("historical ZF ORF (aa 1-60)", zf_old[:60])):
                i = prot.find(q[:20])
                if i >= 0:
                    hits.append(f"{label} first 20 aa at nt {fr + 3 * i + 1}")
            if hits:
                print(f"  frame {fr + 1}: " + "; ".join(hits))
                for h in hits:
                    start_aa = (int(h.split('at nt ')[1]) - fr - 1) // 3
                    stop = prot.find("*", start_aa)
                    print(f"    -> next stop in frame {fr + 1} at aa offset {stop - start_aa} "
                          f"(nt {fr + 3 * stop + 1})")
        # zinc fingers in any frame
        for fr in range(3):
            sub = nt[fr:]
            sub = sub[: len(sub) - len(sub) % 3]
            prot = str(Seq(sub).translate())
            print(f"  frame {fr + 1}: C2H2 motifs {len(C2H2.findall(prot))}")


if __name__ == "__main__":
    main()
