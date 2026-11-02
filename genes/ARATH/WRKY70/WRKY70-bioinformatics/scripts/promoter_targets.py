#!/usr/bin/env python
"""Map DAP-seq peaks of one TF to promoters of query genes, scan W-box motifs, and test
enrichment of DAP-seq promoter targets in curated GO gene sets.

Nothing biological is hardcoded: every number in the outputs is computed from the input
files. Query loci and GO sets come from a YAML config.

Inputs
  --peaks        narrowPeak of the focal TF (GEM events; summit = col2 + col10)
  --ns-targets   O'Malley et al. 2016 gene-target list for the focal TF (tf.at_id, target.at_id)
  --other-peaks  directory of narrowPeak files for comparison TFs (file stem = dataset name)
  --gtf          Ensembl Plants TAIR10 GTF (gene features, gene_biotype)
  --genome       TAIR10 toplevel FASTA (.gz ok)
  --gaf          TAIR GAF (AGI locus codes in column 2)
  --obo          go-basic.obo
  --config       YAML with tf_locus, genes[{agi,label,category}], go_sets[{id,label}]
  --upstream / --downstream   promoter window relative to TSS (default 2000 / 0)
  --outdir       output directory

Outputs (outdir)
  query_gene_promoters.tsv    per query gene: peaks in window, scores, ranks, motif counts,
                              official-target membership, other-WRKY datasets with a peak
  go_set_enrichment.tsv       Fisher exact test of promoter-target genes vs GO sets
  wbox_background.tsv         genome-wide distribution of motif counts per promoter window
  dataset_peak_counts.tsv     number of peaks in each comparison dataset
  run_summary.txt             parameters and global counts
"""
import argparse
import gzip
import re
import sys
from collections import defaultdict
from pathlib import Path

import yaml
from scipy.stats import fisher_exact

MOTIFS = {
    # W-box core as usually written (TTGACY); counted on both strands
    "Wbox_TTGACY": "TTGAC[CT]",
    # WT-box reported for WRKY70 (Machens et al. 2014): YGACTTTT
    "WTbox_YGACTTTT": "[CT]GACTTTT",
}
COMP = str.maketrans("ACGTN[]", "TGCAN][")


def revcomp_regex(rx: str) -> str:
    # reverse-complement a simple regex made of bases and [..] classes
    tokens = re.findall(r"\[[^\]]+\]|[ACGTN]", rx)
    out = []
    for t in reversed(tokens):
        if t.startswith("["):
            out.append("[" + "".join(sorted(t[1:-1].translate(COMP))) + "]")
        else:
            out.append(t.translate(COMP))
    return "".join(out)


def norm_chrom(c: str) -> str:
    return c[3:] if c.lower().startswith("chr") else c


def open_any(p):
    p = str(p)
    return gzip.open(p, "rt") if p.endswith(".gz") else open(p)


def read_peaks(path):
    peaks = []
    with open_any(path) as fh:
        for line in fh:
            f = line.rstrip("\n").split("\t")
            if len(f) < 10:
                continue
            start = int(f[1])
            summit = start + int(f[9])
            peaks.append(
                dict(chrom=norm_chrom(f[0]), start=start, end=int(f[2]), summit=summit,
                     name=f[3], score=int(f[4]), signal=float(f[6]))
            )
    # rank by signalValue (1 = strongest)
    for r, p in enumerate(sorted(peaks, key=lambda x: -x["signal"]), start=1):
        p["rank"] = r
    return peaks


def index_peaks(peaks):
    idx = defaultdict(list)
    for p in peaks:
        idx[p["chrom"]].append(p)
    for c in idx:
        idx[c].sort(key=lambda x: x["summit"])
    return idx


def read_genes(gtf):
    genes = {}
    with open_any(gtf) as fh:
        for line in fh:
            if line.startswith("#"):
                continue
            f = line.rstrip("\n").split("\t")
            if f[2] != "gene":
                continue
            attrs = dict(re.findall(r'(\S+) "([^"]*)"', f[8]))
            genes[attrs["gene_id"].upper()] = dict(
                chrom=norm_chrom(f[0]), start=int(f[3]), end=int(f[4]), strand=f[6],
                biotype=attrs.get("gene_biotype", ""))
    return genes


def promoter(g, up, down, chrom_len=None):
    """1-based inclusive window; TSS = gene 5' end."""
    if g["strand"] == "+":
        tss = g["start"]
        lo, hi = tss - up, tss + down - (1 if down > 0 else 0)
        if down == 0:
            hi = tss - 1
    else:
        tss = g["end"]
        lo, hi = tss - down + (1 if down > 0 else 0), tss + up
        if down == 0:
            lo = tss + 1
    lo = max(1, lo)
    if chrom_len:
        hi = min(chrom_len, hi)
    return tss, lo, hi


def summits_in(idx, chrom, lo, hi):
    # peak summits are 0-based offsets from a 0-based start: convert to 1-based
    return [p for p in idx.get(chrom, []) if lo <= p["summit"] + 1 <= hi]


def read_genome(fa):
    seqs, name, buf = {}, None, []
    with open_any(fa) as fh:
        for line in fh:
            if line.startswith(">"):
                if name:
                    seqs[name] = "".join(buf)
                name, buf = norm_chrom(line[1:].split()[0]), []
            else:
                buf.append(line.strip().upper())
    if name:
        seqs[name] = "".join(buf)
    return seqs


def count_motifs(seq):
    out = {}
    for k, rx in MOTIFS.items():
        rc = revcomp_regex(rx)
        pos = {m.start() for m in re.finditer(f"(?={rx})", seq)}
        if rc != rx:
            pos |= {m.start() for m in re.finditer(f"(?={rc})", seq)}
        out[k] = len(pos)
    return out


def read_obo(path):
    parents, names, ns = defaultdict(set), {}, {}
    cur = None
    with open(path) as fh:
        for line in fh:
            line = line.rstrip("\n")
            if line == "[Term]":
                cur = None
            elif line.startswith("id: GO:"):
                cur = line[4:]
            elif cur and line.startswith("name: "):
                names[cur] = line[6:]
            elif cur and line.startswith("namespace: "):
                ns[cur] = line[11:]
            elif cur and line.startswith("is_a: "):
                parents[cur].add(line[6:16])
            elif cur and line.startswith("relationship: part_of "):
                parents[cur].add(line[22:32])
            elif line.startswith("[Typedef]"):
                cur = None
    children = defaultdict(set)
    for c, ps in parents.items():
        for p in ps:
            children[p].add(c)
    return names, children


def descendants(term, children):
    seen, stack = {term}, [term]
    while stack:
        for c in children.get(stack.pop(), ()):
            if c not in seen:
                seen.add(c)
                stack.append(c)
    return seen


def read_gaf(path):
    ann = defaultdict(set)
    sym = {}
    with open_any(path) as fh:
        for line in fh:
            if line.startswith("!"):
                continue
            f = line.rstrip("\n").split("\t")
            agi = f[1].upper()
            sym.setdefault(agi, f[2])
            if "NOT" in f[3].split("|"):
                continue
            ann[f[4]].add(agi)
    return ann, sym


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    for a in ["peaks", "ns-targets", "other-peaks", "gtf", "genome", "gaf", "obo", "config", "outdir"]:
        ap.add_argument(f"--{a}", required=True)
    ap.add_argument("--focal-dataset", default="",
                    help="stem of the focal dataset inside --other-peaks, excluded from the comparison")
    ap.add_argument("--upstream", type=int, default=2000)
    ap.add_argument("--downstream", type=int, default=0)
    args = ap.parse_args()
    out = Path(args.outdir)
    out.mkdir(parents=True, exist_ok=True)
    cfg = yaml.safe_load(open(args.config))

    print("reading inputs", file=sys.stderr)
    peaks = read_peaks(args.peaks)
    pidx = index_peaks(peaks)
    other = {}
    for f in sorted(Path(args.other_peaks).glob("*.narrowPeak")):
        other[f.stem] = index_peaks(read_peaks(f))
    genes = read_genes(args.gtf)
    genome = read_genome(args.genome)
    gaf, gaf_sym = read_gaf(args.gaf)
    go_names, go_children = read_obo(args.obo)
    ns_targets = set()
    with open(args.ns_targets) as fh:
        next(fh)
        for line in fh:
            f = line.split()
            if len(f) >= 2:
                ns_targets.add(f[1].upper())
    chrom_len = {c: len(s) for c, s in genome.items()}
    nuclear = {str(i) for i in range(1, 6)}
    up, down = args.upstream, args.downstream

    # universe: nuclear protein-coding genes
    universe = {a for a, g in genes.items() if g["biotype"] == "protein_coding" and g["chrom"] in nuclear}
    targets, motif_bg = set(), []
    for a in sorted(universe):
        g = genes[a]
        tss, lo, hi = promoter(g, up, down, chrom_len[g["chrom"]])
        if summits_in(pidx, g["chrom"], lo, hi):
            targets.add(a)
        motif_bg.append((a, count_motifs(genome[g["chrom"]][lo - 1:hi])))

    # background motif distribution
    with open(out / "wbox_background.tsv", "w") as fh:
        fh.write("motif\tcount_per_window\tn_promoters\n")
        for k in MOTIFS:
            dist = defaultdict(int)
            for _, m in motif_bg:
                dist[m[k]] += 1
            for c in sorted(dist):
                fh.write(f"{k}\t{c}\t{dist[c]}\n")
    bg = {k: sorted(m[k] for _, m in motif_bg) for k in MOTIFS}

    def pct_le(k, v):
        arr = bg[k]
        return 100.0 * sum(1 for x in arr if x <= v) / len(arr)

    # per query gene
    cols = ["agi", "label", "category", "gaf_symbol", "chrom", "strand", "tss", "window_start", "window_end",
            "n_focal_peaks_in_window", "max_peak_score", "max_peak_signal", "best_peak_rank_of_total",
            "summit_offsets_from_tss", "nearest_focal_summit_offset_any", "in_focal_nS_targets"]
    cols += [f"{k}_count" for k in MOTIFS] + [f"{k}_genome_percentile" for k in MOTIFS]
    cols += ["n_other_wrky_datasets_with_peak", "other_wrky_datasets_with_peak"]
    with open(out / "query_gene_promoters.tsv", "w") as fh:
        fh.write("\t".join(cols) + "\n")
        for q in cfg["genes"]:
            a = q["agi"].upper()
            g = genes.get(a)
            if g is None:
                fh.write(f"{a}\t{q['label']}\t{q['category']}\tNOT_IN_GTF\n")
                continue
            tss, lo, hi = promoter(g, up, down, chrom_len[g["chrom"]])
            hits = summits_in(pidx, g["chrom"], lo, hi)
            sgn = 1 if g["strand"] == "+" else -1

            def off(p):
                return sgn * (p["summit"] + 1 - tss)

            near = min(pidx.get(g["chrom"], []), key=lambda p: abs(p["summit"] + 1 - tss), default=None)
            mot = count_motifs(genome[g["chrom"]][lo - 1:hi])
            others = [ds for ds, ix in other.items() if summits_in(ix, g["chrom"], lo, hi)
                      and ds != args.focal_dataset]
            row = [a, q["label"], q["category"], gaf_sym.get(a, "NA"), g["chrom"], g["strand"], tss, lo, hi,
                   len(hits),
                   max((p["score"] for p in hits), default="NA"),
                   max((p["signal"] for p in hits), default="NA"),
                   (f"{min(p['rank'] for p in hits)}/{len(peaks)}" if hits else "NA"),
                   ",".join(str(off(p)) for p in sorted(hits, key=off)) or "NA",
                   off(near) if near else "NA",
                   a in ns_targets]
            row += [mot[k] for k in MOTIFS] + [f"{pct_le(k, mot[k]):.1f}" for k in MOTIFS]
            row += [len(others), ",".join(others) or "NA"]
            fh.write("\t".join(map(str, row)) + "\n")

    # enrichment
    with open(out / "go_set_enrichment.tsv", "w") as fh:
        fh.write("go_id\tconfig_label\tobo_name\tn_terms_incl_descendants\tset_size_in_universe\t"
                 "set_and_target\ttarget_size\tuniverse_size\tfrac_set_targeted\tfrac_universe_targeted\t"
                 "odds_ratio\tfisher_p_two_sided\n")
        for s in cfg["go_sets"]:
            terms = descendants(s["id"], go_children)
            members = set().union(*(gaf.get(t, set()) for t in terms)) & universe
            a = len(members & targets)
            b = len(members - targets)
            c = len(targets - members)
            d = len(universe) - a - b - c
            orr, p = fisher_exact([[a, b], [c, d]])
            fh.write(f"{s['id']}\t{s['label']}\t{go_names.get(s['id'], 'NA')}\t{len(terms)}\t{len(members)}\t"
                     f"{a}\t{len(targets)}\t{len(universe)}\t{a / max(1, len(members)):.3f}\t"
                     f"{len(targets) / len(universe):.3f}\t{orr:.3f}\t{p:.3g}\n")

    with open(out / "dataset_peak_counts.tsv", "w") as fh:
        fh.write("dataset\tn_peaks\n")
        for ds, ix in sorted(other.items(), key=lambda kv: -sum(len(v) for v in kv[1].values())):
            fh.write(f"{ds}\t{sum(len(v) for v in ix.values())}\n")

    with open(out / "run_summary.txt", "w") as fh:
        fh.write(f"focal_peaks_file\t{args.peaks}\n")
        fh.write(f"n_focal_peaks\t{len(peaks)}\n")
        fh.write(f"n_focal_peaks_chr1_5\t{sum(len(pidx[c]) for c in nuclear)}\n")
        fh.write(f"n_other_datasets\t{len([d for d in other if d != args.focal_dataset])}\n")
        fh.write(f"promoter_window\t-{up} to +{down} relative to TSS (gene 5' end, Ensembl Plants gene feature)\n")
        fh.write(f"universe_protein_coding_chr1_5\t{len(universe)}\n")
        fh.write(f"promoter_target_genes\t{len(targets)}\n")
        fh.write(f"omalley_nS_targets\t{len(ns_targets)}\n")
        fh.write(f"overlap_promoter_targets_vs_nS_targets\t{len(targets & ns_targets)}\n")
    print("done", file=sys.stderr)


if __name__ == "__main__":
    main()
