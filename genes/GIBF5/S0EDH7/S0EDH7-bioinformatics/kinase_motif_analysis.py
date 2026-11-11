"""Kinase-like domain and catalytic-motif analysis for S0EDH7 (FFUJ_06423).

Reproduce (from this folder):
    # one-time: download Pfam HMMs from InterPro into hmms/ and press them
    #   for pf in PF00069 PF07714 PF01636 PF17667 PF06293 PF01633 PF02958 PF12260 \
    #             PF06176 PF14531 PF10707 PF01163 PF03109 PF05445; do
    #     curl -s "https://www.ebi.ac.uk/interpro/api/entry/pfam/$pf?annotation=hmm" | gunzip > hmms/$pf.hmm
    #   done; cat hmms/PF*.hmm > hmms/kinase_like_panel.hmm; hmmpress -f hmms/kinase_like_panel.hmm
    python3 kinase_motif_analysis.py

Fetches S0EDH7 plus a few BLAST-selected Pezizomycotina homologs from UniProt REST,
runs hmmscan (HMMER3, local) against the kinase-like Pfam panel, and prints, for the
Pkinase (PF00069) alignment of each sequence, the residues aligned to the catalytic
loop HRD..N and the DFG motif, plus whether the N-lobe region (HMM positions 1-42,
containing the glycine-rich loop and the beta3 lysine) is covered by the alignment.
Results are printed, not hardcoded.
"""

import os
import subprocess
import urllib.request
from pathlib import Path

HERE = Path(__file__).parent
PANEL = Path(os.environ.get("HMM_PANEL", HERE / "hmms" / "kinase_like_panel.hmm"))
# S0EDH7 plus homologs chosen from the EBI BLAST (UniProtKB) hit list
ACCESSIONS = ["S0EDH7", "A0A1L7VSC9", "G2WYF2", "A7ERU3", "A0A162MTB1"]


def fetch(acc: str) -> str:
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"
    with urllib.request.urlopen(url) as r:
        return r.read().decode()


def parse_domtbl_and_ali(out: str):
    """Yield (model, score, hmm_from, hmm_to, ali_from, hmm_line, seq_line) for top domain."""
    blocks = out.split(">> ")[1:]
    for b in blocks:
        model = b.split()[0]
        b = b.split("== domain 2")[0]  # alignment of the first reported domain only
        lines = b.splitlines()
        rows = [ln for ln in lines if ln.strip()[:1].isdigit()]
        if not rows:  # model listed but no domain passed reporting threshold
            continue
        row = rows[0]
        f = row.split()
        score, hmm_from, hmm_to, ali_from = float(f[2]), int(f[6]), int(f[7]), int(f[9])
        hmm_seq, tgt_seq = "", ""
        idx = [i for i, ln in enumerate(lines) if ln.split()[:1] == [model] and ln.split()[1].isdigit()]
        for i in idx:
            hmm_seq += lines[i].split()[2]
            tgt_seq += lines[i + 2].split()[2]
        yield model, score, hmm_from, hmm_to, ali_from, hmm_seq, tgt_seq


def map_hmm_to_seq(hmm_from, ali_from, hmm_seq, tgt_seq):
    """Return dict hmm_position -> (residue, seq_position)."""
    m, s, out = hmm_from, ali_from, {}
    for h, t in zip(hmm_seq, tgt_seq):
        if h != ".":
            out[m] = (t, s if t != "-" else None)
            m += 1
        if t != "-":
            s += 1
    return out


def main():
    for acc in ACCESSIONS:
        fa = HERE / f"{acc}.fa"
        fa.write_text(fetch(acc).replace(">", ">q ", 1))
        res = subprocess.run(
            ["hmmscan", "--max", "-E", "10", "--domE", "10", str(PANEL), str(fa)],
            capture_output=True, text=True, check=True,
        ).stdout
        seqlen = sum(len(x) for x in fa.read_text().splitlines()[1:])
        print(f"== {acc} (length {seqlen})")
        for model, score, hf, ht, af, hs, ts in parse_domtbl_and_ali(res):
            if model != "Pkinase":
                continue
            mp = map_hmm_to_seq(hf, af, hs, ts)
            # PF00069 consensus: ...HrDlKpeNiLid...kitDFG ; positions located from HMM consensus
            cons = dict(zip(range(hf, ht + 1), [c for c in hs if c != "."]))
            hrd = [p for p in cons if cons[p] == "H" and cons.get(p + 1) == "r" and cons.get(p + 2) == "D"]
            dfg = [p for p in cons if cons[p] == "D" and cons.get(p + 1) == "F" and cons.get(p + 2) == "G"]
            print(f"  Pkinase score {score} bits, HMM {hf}-{ht}, N-lobe (HMM 1-42) covered: {hf <= 20}")
            for p in hrd:
                motif = "".join(mp[q][0] for q in range(p, p + 8) if q in mp)
                print(f"  catalytic loop (HMM HrDlKpeN @{p}): {motif} starting seq pos {mp[p][1]}")
            for p in dfg:
                motif = "".join(mp[q][0] for q in range(p, p + 3) if q in mp)
                print(f"  DFG (HMM @{p}): {motif} at seq pos {mp[p][1]}")


if __name__ == "__main__":
    main()
