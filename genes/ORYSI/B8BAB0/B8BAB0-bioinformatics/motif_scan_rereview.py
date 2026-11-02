"""Scan B8BAB0 and SF2 comparators for the PG1beta repeat (FxxY, after
Park et al. 2015 / Zheng et al. 1992 FTNYGxxGNGGxxx) and BURP-domain CH motifs.
Run: uv run python motif_scan_rereview.py
"""
import re
import urllib.request

ACCS = ["B8BAB0", "Q6ZA27", "Q7XES5", "Q40161", "O80760"]
# Strict tomato-type core: F-T-x-Y-G ; looser FxxY as described for AtPGLs
STRICT = re.compile(r"F[TS].YG")
LOOSE = re.compile(r"(?=(F..Y))")
CH = re.compile(r"CH")


def fetch(acc: str) -> str:
    text = urllib.request.urlopen(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta").read().decode()
    return "".join(text.splitlines()[1:])


def main() -> None:
    print("acc\tlength\tF[TS]xYG_count\tFxxY_count\tCH_positions(1-based)")
    for acc in ACCS:
        s = fetch(acc)
        strict = [m.start() + 1 for m in STRICT.finditer(s)]
        loose = len(LOOSE.findall(s))
        ch = [m.start() + 1 for m in CH.finditer(s)]
        print(f"{acc}\t{len(s)}\t{len(strict)}\t{loose}\t{ch}")
        print(f"\t\tF[TS]xYG starts: {strict}")


if __name__ == "__main__":
    main()
