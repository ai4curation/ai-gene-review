"""Compare the T. pseudonana SIT1/SIT2 reference-proteome entries with the cDNA-derived entries.

Fetches sequences live from the UniProt REST API and reports, for each pair:
- whether the reference-proteome (gene-model) sequence is an exact suffix of the cDNA-derived one,
- the length of the N-terminal segment missing from the gene model,
- the position of the anti-TpEL4 antigen peptide (Thamatrakoln & Hildebrand 2007, residues 318-332
  of TpSIT1) in each sequence, and the N- and C-terminal residues encoded by the published cloning
  primers (translated by hand from the primer sequences given in that paper's Methods).

Usage: python compare_models.py > RESULTS-output.txt
"""
import urllib.request

PAIRS = [
    ("SIT1", "B8C2V9", "Q0QVM8"),
    ("SIT2", "B5YNJ0", "Q0QVM7"),
]
ANTIGEN = "PANERGTSFFGRKTC"  # TpSIT1 residues 318-332 (anti-TpEL4 antigen)
# Translated starts/ends of the published TpSIT cloning primers (PMID:17172435 Methods)
PRIMER_N = {"SIT1": "MSTAEIQ", "SIT2": "MSSAEV"}
PRIMER_C = {"SIT1": "DALAEDA", "SIT2": "EAVDAQA"}


def fetch(acc):
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"
    with urllib.request.urlopen(url, timeout=60) as r:
        lines = r.read().decode().splitlines()
    return lines[0], "".join(lines[1:])


def hydrophobic_windows(seq, w=19, thresh=1.6):
    kd = dict(A=1.8, R=-4.5, N=-3.5, D=-3.5, C=2.5, Q=-3.5, E=-3.5, G=-0.4, H=-3.2, I=4.5,
              L=3.8, K=-3.9, M=1.9, F=2.8, P=-1.6, S=-0.8, T=-0.7, W=-0.9, Y=-1.3, V=4.2)
    hits = []
    for i in range(len(seq) - w + 1):
        s = sum(kd.get(a, 0) for a in seq[i:i + w]) / w
        if s >= thresh:
            hits.append((i + 1, round(s, 2)))
    return hits


for name, model, cdna in PAIRS:
    hm, sm = fetch(model)
    hc, sc = fetch(cdna)
    print(f"## {name}: gene model {model} ({len(sm)} aa) vs cDNA entry {cdna} ({len(sc)} aa)")
    print(f"header {model}: {hm}")
    print(f"header {cdna}: {hc}")
    suffix = sc.endswith(sm)
    print(f"{model} is exact C-terminal suffix of {cdna}: {suffix}")
    if suffix:
        missing = sc[: len(sc) - len(sm)]
        print(f"N-terminal residues absent from {model}: {len(missing)}")
        print(f"absent segment: {missing}")
        hw = hydrophobic_windows(missing)
        if hw:
            best = max(hw, key=lambda x: x[1])
            print(f"Kyte-Doolittle 19-residue windows >=1.6 in absent segment: {len(hw)}; "
                  f"max {best[1]} starting at residue {best[0]}")
        else:
            print("no Kyte-Doolittle 19-residue window >=1.6 in absent segment")
    for label, s in ((model, sm), (cdna, sc)):
        pos = s.find(ANTIGEN)
        print(f"antigen {ANTIGEN} in {label}: {'absent' if pos < 0 else f'residues {pos + 1}-{pos + len(ANTIGEN)}'}")
        print(f"primer N-terminus {PRIMER_N[name]} at start of {label}: {s.startswith(PRIMER_N[name])}")
        print(f"primer C-terminus {PRIMER_C[name]} at end of {label}: {s.endswith(PRIMER_C[name])}")
    print()
