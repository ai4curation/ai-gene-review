"""Score KT2440 MoaA-family proteins against the function-level MoaA models
NCBIfam TIGR02666 (HMMER3) and HAMAP MF_01225_B (PROSITE-format generalized
profile), and locate where the paralogs PP_1969 (Q88LG4) and PP_2482 (Q88K11)
lose score relative to canonical MoaA.

Nothing about the results is hardcoded. Model files, the HAMAP rule and the
sequences are downloaded separately by fetch_inputs.sh into a scratch directory
and passed in as arguments. Cutoffs are read from the model headers.

Usage (from repo root):
  uv run --no-project --with pyhmmer python -I \
    genes/PSEPK/PP_1969/PP_1969-bioinformatics/model_scores.py \
    --hmm $D/TIGR02666.1.HMM --hmm $D/TIGR02668.1.HMM \
    --prf $D/MF_01225_B.prf --rule $D/MF_01225.rule.txt \
    --fasta $D/seqs.fasta --ref-uniprot genes/PSEPK/moaA/moaA-uniprot.txt \
    --ref Q88E69 --targets Q88LG4,Q88K11 \
    --canonical Q88E69,P30745,P69848,Q9HXD6,Q9I3K7,Q9NZB8 \
    --outdir genes/PSEPK/PP_1969/PP_1969-bioinformatics/model_scores_out

Requires the hmmsearch (HMMER 3) and pfsearchV3 (pftools 3) executables on PATH;
both are also called directly so that their native outputs are kept.

Per-position contributions: for each aligned match state k and residue a, the
emission log-odds log2(e_k(a) / f(a)) is computed from the HMM match emissions
and the HMMER background frequencies (pyhmmer.plan7.Background). This is an
approximate decomposition: it ignores transition scores and the null2 bias
correction, so the per-position values do not sum to the reported bit score.
It is used only to rank where along the model the paralogs lose score.
"""
import argparse
import importlib.util
import math
import re
import subprocess
from pathlib import Path

import pyhmmer
from pyhmmer.easel import Alphabet, SequenceFile
from pyhmmer.plan7 import Background, HMMFile

HERE = Path(__file__).resolve().parent


def load_site_parser():
    spec = importlib.util.spec_from_file_location("map_moaA_sites", HERE / "map_moaA_sites.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.read_uniprot


def acc_of(name):
    name = name.decode() if isinstance(name, bytes) else name
    parts = name.split("|")
    return parts[1] if len(parts) > 2 else name


def read_fasta(path):
    seqs, cur = {}, None
    for line in Path(path).read_text().splitlines():
        if line.startswith(">"):
            cur = acc_of(line[1:].split()[0])
            seqs[cur] = []
        elif cur:
            seqs[cur].append(line.strip())
    return {k: "".join(v) for k, v in seqs.items()}


# ---------------------------------------------------------------- HMMER part
def run_hmmsearch_cli(hmm, fasta, outdir):
    stem = Path(hmm).name.replace(".HMM", "")
    tbl, dtbl = outdir / f"{stem}.tblout", outdir / f"{stem}.domtblout"
    cmd = ["hmmsearch", "--max", "-E", "1000", "--domE", "1000", "--tblout", str(tbl),
           "--domtblout", str(dtbl), "-o", str(outdir / f"{stem}.hmmsearch.txt"), str(hmm), str(fasta)]
    subprocess.run(cmd, check=True)
    return " ".join(cmd), tbl, dtbl


def parse_tbl(path):
    rows = {}
    for line in Path(path).read_text().splitlines():
        if line.startswith("#"):
            continue
        f = line.split()
        rows[acc_of(f[0])] = dict(full_E=float(f[4]), full_bits=float(f[5]), best_dom_E=float(f[7]),
                                  best_dom_bits=float(f[8]), n_dom=int(f[15]))
    return rows


def parse_domtbl(path):
    best = {}
    for line in Path(path).read_text().splitlines():
        if line.startswith("#"):
            continue
        f = line.split()
        a = acc_of(f[0])
        d = dict(dom_bits=float(f[13]), i_E=float(f[12]), hmm_from=int(f[15]), hmm_to=int(f[16]),
                 ali_from=int(f[17]), ali_to=int(f[18]), tlen=int(f[2]), qlen=int(f[5]))
        if a not in best or d["dom_bits"] > best[a]["dom_bits"]:
            best[a] = d
    return best


def pyhmmer_columns(hmm_path, fasta):
    """Return hmm, background and, per sequence, a dict model_pos -> (seq_pos|None, residue|'-', pp)
    plus insertion counts after each model position, from the best-scoring domain."""
    alpha = Alphabet.amino()
    with HMMFile(hmm_path) as fh:
        hmm = fh.read()
    with SequenceFile(fasta, digital=True, alphabet=alpha) as sf:
        seqs = sf.read_block()
    bg = Background(alpha)
    out = {}
    for hits in pyhmmer.hmmsearch([hmm], seqs, E=1000, domE=1000, bit_cutoffs=None):
        for hit in hits:
            dom = max(hit.domains, key=lambda d: d.score)
            ali = dom.alignment
            k, i = ali.hmm_from - 1, ali.target_from - 1
            cols, ins = {}, {}
            for h, t, pp in zip(ali.hmm_sequence, ali.target_sequence, ali.posterior_probabilities):
                if h == ".":  # insert state in target
                    i += 1
                    ins[k] = ins.get(k, 0) + 1
                    continue
                k += 1
                if t == "-":
                    cols[k] = (None, "-", " ")
                else:
                    i += 1
                    cols[k] = (i, t.upper(), pp)
            out[acc_of(hit.name)] = dict(cols=cols, ins=ins, hmm_from=ali.hmm_from, hmm_to=ali.hmm_to)
    return hmm, bg, alpha, out


def emission_bits(hmm, bg, alpha, k, res):
    if res == "-" or res not in alpha.symbols[:20]:
        return None
    a = alpha.symbols.index(res)
    return math.log2(hmm.match_emissions[k][a] / bg.residue_frequencies[a])


# ---------------------------------------------------------------- HAMAP part
def prf_header(path):
    cut, length = [], None
    for line in Path(path).read_text().splitlines():
        if "/GENERAL_SPEC" in line:
            length = int(re.search(r"LENGTH=(\d+)", line).group(1))
        if "/CUT_OFF" in line:
            cut.append(dict(level=int(re.search(r"LEVEL=(-?\d+)", line).group(1)),
                            raw=int(re.search(r"SCORE=(\d+)", line).group(1)),
                            norm=float(re.search(r"N_SCORE=([\d.]+)", line).group(1))))
    return length, cut


def run_pfsearch(prf, fasta, outdir):
    # -f FASTA, -n no heuristic, -a report optimal alignment for every sequence,
    # -o 1 InterPro-style output with the aligned sequence (match = upper/'-', insert = lower)
    cmd = ["pfsearchV3", "-f", "-n", "-a", "-o", "1", str(prf), str(fasta)]
    res = subprocess.run(cmd, check=True, capture_output=True, text=True)
    (outdir / "MF_01225_B.pfsearchV3.txt").write_text(res.stdout)
    hits, cur = {}, None
    for line in res.stdout.splitlines():
        if line.startswith(">"):
            m = re.match(r">\S+ L=(-?\d+) +([\d.-]+) +(\d+) pos\. +(\d+) - +(\d+) .*?\] (\S+)", line)
            cur = acc_of(m.group(6))
            hits[cur] = dict(level=int(m.group(1)), norm=float(m.group(2)), raw=int(m.group(3)),
                             start=int(m.group(4)), end=int(m.group(5)), ali="")
        elif cur:
            hits[cur]["ali"] += line.strip()
    return " ".join(cmd), hits


def prf_columns(hit):
    """profile match position -> sequence position (None for deletion)."""
    cols, k, i = {}, 0, hit["start"] - 1
    for c in hit["ali"]:
        if c == "-":
            k += 1
            cols[k] = None
        elif c.islower():
            i += 1
        else:
            k += 1
            i += 1
            cols[k] = i
    return cols


def rule_conditions(rule_path, taxon="Bacteria"):
    """FT BINDING positions/conditions for one taxon case of a HAMAP rule (template coordinates)."""
    lines = Path(rule_path).read_text().splitlines()
    out, on, template, last_from, cur = [], False, None, None, None
    for line in lines:
        m = re.match(r"FT   From: \S+ \((\S+)\)", line)
        if m:
            last_from = m.group(1)
        if line.startswith("case <OC:"):
            on = taxon in line
            if on and last_from and template is None:
                template = last_from
        elif line.startswith("end case"):
            on = False
        if not on or not line.startswith("FT"):
            continue
        m = re.match(r"FT   BINDING\s+(\d+)(?:\.\.(\d+))?", line)
        if m:
            cur = dict(span=(int(m.group(1)), int(m.group(2) or m.group(1))), ligand=None)
        elif cur and "/ligand=" in line and cur["ligand"] is None:
            cur["ligand"] = line.split("/ligand=")[1].strip('"')
        elif cur and "Condition:" in line:
            cur["optional"] = "Optional" in line
            cur["condition"] = line.split("Condition:")[1].strip()
            out.append(cur)
            cur = None
    return template, out


def prosite_to_regex(cond):
    return "".join("." if t == "x" else t for t in cond.split("-"))


# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--hmm", action="append", required=True)
    ap.add_argument("--prf", required=True)
    ap.add_argument("--rule", required=True)
    ap.add_argument("--fasta", required=True)
    ap.add_argument("--ref-uniprot", required=True)
    ap.add_argument("--ref", required=True)
    ap.add_argument("--targets", required=True)
    ap.add_argument("--canonical", required=True)
    ap.add_argument("--outdir", required=True)
    args = ap.parse_args()
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    targets = args.targets.split(",")
    canon = args.canonical.split(",")
    seqs = read_fasta(args.fasta)
    order = list(seqs)
    _, ref_seq, sites = load_site_parser()(args.ref_uniprot)
    assert ref_seq == seqs[args.ref], "reference UniProt sequence differs from FASTA"
    print(f"pyhmmer {pyhmmer.__version__}")

    # ---- HMMER models
    main_hmm = args.hmm[0]
    for hmm_path in args.hmm:
        cmd, tbl, dtbl = run_hmmsearch_cli(hmm_path, args.fasta, outdir)
        with HMMFile(hmm_path) as fh:
            h = fh.read()
        tc, nc = h.cutoffs.trusted, h.cutoffs.noise
        print(f"\n## {h.accession} {h.name} (LENG {h.M}; TC {tc[0]} / {tc[1]}; NC {nc[0]} / {nc[1]})")
        print(f"command: {cmd}")
        t, d = parse_tbl(tbl), parse_domtbl(dtbl)
        print("acc\tlen\tfull_bits\tfull_E\tbest_dom_bits\tdom_iE\thmm_from-to\tali_from-to\tn_dom\tvs_TC\tvs_NC")
        for a in order:
            if a not in t:
                print(f"{a}\t{len(seqs[a])}\tno hit")
                continue
            r, x = t[a], d[a]
            print(f"{a}\t{x['tlen']}\t{r['full_bits']:.1f}\t{r['full_E']:.2g}\t{x['dom_bits']:.1f}\t"
                  f"{x['i_E']:.2g}\t{x['hmm_from']}-{x['hmm_to']}\t{x['ali_from']}-{x['ali_to']}\t"
                  f"{r['n_dom']}\t{r['full_bits'] - tc[0]:+.1f}\t{r['full_bits'] - nc[0]:+.1f}")

    hmm, bg, alpha, cols = pyhmmer_columns(main_hmm, args.fasta)
    M = hmm.M
    cons = hmm.consensus
    bits = {a: {k: emission_bits(hmm, bg, alpha, k, cols[a]["cols"].get(k, (None, "-", " "))[1])
                for k in range(1, M + 1)} for a in cols}

    # per-position table
    tsv = outdir / "TIGR02666_positions.tsv"
    with tsv.open("w") as fh:
        fh.write("model_pos\tconsensus\tref_ligand\t" + "\t".join(f"{a}_res\t{a}_pos\t{a}_pp\t{a}_bits" for a in order if a in cols) + "\n")
        ref_cols = cols[args.ref]["cols"]
        ref_lig = {}
        for p, lig in sites:
            for k, (sp, _, _) in ref_cols.items():
                if sp == p:
                    ref_lig.setdefault(k, []).append(lig)
        for k in range(1, M + 1):
            row = [str(k), cons[k - 1], ";".join(ref_lig.get(k, []))]
            for a in order:
                if a not in cols:
                    continue
                sp, res, pp = cols[a]["cols"].get(k, (None, "-", " "))
                b = bits[a][k]
                row += [res, str(sp or ""), pp, "" if b is None else f"{b:.2f}"]
            fh.write("\t".join(row) + "\n")
    print(f"\nper-position table: {tsv}")

    print(f"\n## TIGR02666 coverage and gaps of best domain (model 1..{M})")
    for a in order:
        if a not in cols:
            continue
        c = cols[a]
        dels = [k for k, v in c["cols"].items() if v[1] == "-"]
        ins = sum(c["ins"].values())
        print(f"{a}\thmm {c['hmm_from']}-{c['hmm_to']}\tdeleted_match_states={len(dels)}\tinserted_residues={ins}"
              f"\tdeletion_runs={runs(dels)}")

    print("\n## C-terminal model segment not reached by the targets' best domain")
    last = min(cols[t]["hmm_to"] for t in targets)
    print(f"model consensus {last + 1}-{M}: {cons[last:M]}")
    for a in order:
        if a not in cols:
            continue
        c = cols[a]
        seg = "".join(c["cols"].get(k, (None, "-", " "))[1] if k in c["cols"] else "." for k in range(last + 1, M + 1))
        end = max(v[0] for v in c["cols"].values() if v[0])
        print(f"{a}\taligned_at_model_{last + 1}-{M}={seg}\tlast_aligned_residue={end}/{len(seqs[a])}"
              f"\tunaligned_C_tail={seqs[a][end:] or '-'}")

    # windowed emission sums
    w = 20
    print(f"\n## Emission log-odds (bits) summed over {w}-position model windows; mean of canonical set vs targets")
    print("window\tcanonical_mean\t" + "\t".join(targets) + "\t" + "\t".join(f"{t}-canon" for t in targets)
          + "\tref_ligand_positions_in_window")
    lig_k = {k: v for k, v in ref_lig.items()}
    deficits = []
    for s in range(1, M + 1, w):
        ks = range(s, min(s + w, M + 1))
        def tot(a):
            return sum(bits[a][k] for k in ks if bits[a][k] is not None)
        cm = sum(tot(a) for a in canon) / len(canon)
        tv = [tot(t) for t in targets]
        ligs = [f"{k}({ref_seq[ref_cols[k][0]-1]}{ref_cols[k][0]})" for k in ks if k in lig_k]
        deficits.append((min(v - cm for v in tv), s))
        print(f"{s}-{ks[-1]}\t{cm:.1f}\t" + "\t".join(f"{v:.1f}" for v in tv) + "\t"
              + "\t".join(f"{v - cm:+.1f}" for v in tv) + "\t" + (",".join(ligs) or "-"))
    tot_canon = sum(sum(b for b in bits[a].values() if b is not None) for a in canon) / len(canon)
    print("total emission bits: canonical mean %.1f; " % tot_canon
          + "; ".join(f"{t} {sum(b for b in bits[t].values() if b is not None):.1f}" for t in targets))

    # discriminating positions: canonical all positive and conserved, both targets negative or gapped
    print("\n## Model positions where every canonical MoaA scores >= 1 bit and every target scores < 0 bits or is gapped")
    print("model_pos\tconsensus\tcanonical_residues\t" + "\t".join(targets) + "\tnearest_ref_ligand_model_pos(distance)")
    lig_list = sorted(lig_k)
    n_disc = 0
    for k in range(1, M + 1):
        cb = [bits[a][k] for a in canon]
        tb = [bits[t][k] for t in targets]
        if all(b is not None and b >= 1 for b in cb) and all(b is None or b < 0 for b in tb):
            n_disc += 1
            near = min(lig_list, key=lambda x: abs(x - k))
            cres = "".join(cols[a]["cols"][k][1] for a in canon)
            tr = [f"{cols[t]['cols'].get(k, (None, '-', ' '))[1]}{cols[t]['cols'].get(k, (None,))[0] or ''}"
                  f"({'gap' if tb[i] is None else f'{tb[i]:.1f}'})" for i, t in enumerate(targets)]
            print(f"{k}\t{cons[k-1]}\t{cres}\t" + "\t".join(tr) + f"\t{near}({abs(near - k)})")
    print(f"n_discriminating_positions={n_disc}")

    print("\n## Q88E69 UniProt binding positions at their TIGR02666 match states")
    print("ref_site\tligand\tmodel_pos\tconsensus\t" + "\t".join(f"{a}" for a in [args.ref] + targets)
          + "\t" + "\t".join(f"{a}_bits" for a in [args.ref] + targets))
    for p, lig in sites:
        ks = [k for k, v in ref_cols.items() if v[0] == p]
        if not ks:
            print(f"{ref_seq[p-1]}{p}\t{lig}\tnot in a match state")
            continue
        k = ks[0]
        res = [f"{cols[a]['cols'].get(k, (None, '-', ' '))[1]}{cols[a]['cols'].get(k, (None,))[0] or ''}"
               f"(pp {cols[a]['cols'].get(k, (None, '-', ' '))[2]})" for a in [args.ref] + targets]
        bb = [bits[a][k] for a in [args.ref] + targets]
        print(f"{ref_seq[p-1]}{p}\t{lig}\t{k}\t{cons[k-1]}\t" + "\t".join(res) + "\t"
              + "\t".join("gap" if b is None else f"{b:.2f}" for b in bb))

    # ---- HAMAP
    length, cut = prf_header(args.prf)
    print(f"\n## HAMAP MF_01225_B profile (LENGTH {length}); cutoffs from header:")
    for c in cut:
        print(f"level {c['level']}: raw {c['raw']}, normalized {c['norm']}")
    cmd, hits = run_pfsearch(args.prf, args.fasta, outdir)
    print(f"command: {cmd}")
    lvl0 = [c for c in cut if c["level"] == 0][0]
    print("acc\tlevel_reached\tnorm_score\traw_score\tseq_from-to\tvs_level0_norm\ttrigger(level0)")
    for a in order:
        if a not in hits:
            print(f"{a}\tno alignment reported")
            continue
        h = hits[a]
        print(f"{a}\t{h['level']}\t{h['norm']:.3f}\t{h['raw']}\t{h['start']}-{h['end']}\t"
              f"{h['norm'] - lvl0['norm']:+.3f}\t{'yes' if h['norm'] >= lvl0['norm'] else 'no'}")

    template, conds = rule_conditions(args.rule)
    print(f"\n## MF_01225 Bacteria FT conditions (template {template}) evaluated through the profile alignment")
    tcols = prf_columns(hits[template])
    inv_t = {v: k for k, v in tcols.items() if v}
    print("template_span\tligand\tcondition\t" + "\t".join(order))
    for c in conds:
        a0, a1 = c["span"]
        row = [f"{a0}..{a1}" if a1 != a0 else str(a0), c["ligand"], c["condition"] + (" (optional)" if c.get("optional") else "")]
        rx = re.compile("^" + prosite_to_regex(c["condition"]) + "$")
        for a in order:
            if a not in hits:
                row.append("-")
                continue
            ac = prf_columns(hits[a])
            res = ""
            for tp in range(a0, a1 + 1):
                k = inv_t.get(tp)
                sp = ac.get(k) if k else None
                res += seqs[a][sp - 1] if sp else "-"
            row.append(f"{res}:{'ok' if rx.match(res) else 'FAIL'}")
        print("\t".join(row))


def runs(ks):
    if not ks:
        return "-"
    out, s, p = [], ks[0], ks[0]
    for k in ks[1:]:
        if k != p + 1:
            out.append(f"{s}-{p}" if s != p else str(s))
            s = k
        p = k
    out.append(f"{s}-{p}" if s != p else str(s))
    return ",".join(out)


if __name__ == "__main__":
    main()
