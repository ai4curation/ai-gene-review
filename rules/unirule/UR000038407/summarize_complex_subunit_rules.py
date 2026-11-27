#!/usr/bin/env python3
"""Summarise how HAMAP annotates subunits of multi-subunit enzymes.

Parses a HAMAP rule flat file (hamap_rules.dat) and, for each rule in a set of
subunit families, reports what the rule writes:

- the EC number(s) in the DE lines (the protein name),
- the Rhea id(s) in CC CATALYTIC ACTIVITY,
- the CC SUBCELLULAR LOCATION text,
- whether a transmembrane-prediction trigger (DR General; Transmembrane) is set,
- whether CC FUNCTION states a subunit-level role or only "Part of a complex".

The Mtr (tetrahydromethanopterin S-methyltransferase) group is the subject of
the UR000038407 / MF_01501 review; the other groups (bacterial F-type ATP
synthase, NDH-1, Na+-NQR, Rnf) are comparators showing the HAMAP convention for
subunits of other multi-subunit membrane enzymes.

Nothing is hardcoded except which rule names to look at; all values are read
from the flat file. Lines inside ``case ... end case`` blocks are included and
flagged with ``[cond]``.

Usage:
    python summarize_complex_subunit_rules.py /path/to/hamap_rules.dat
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

GROUPS: dict[str, re.Pattern[str]] = {
    "Mtr (EC 7.2.1.4 complex)": re.compile(r"^Mtr[A-H]$"),
    "F-type ATP synthase (bacterial)": re.compile(r"^ATP_synth_.*_(bact|bprime)$|^ATP_synth_bprime$|^ATP_synth_epsil_bac$"),
    "NDH-1 (Nuo)": re.compile(r"^NDH1_Nuo"),
    "Na+-NQR": re.compile(r"^Nqr[A-F]$"),
    "Rnf": re.compile(r"^Rsx[A-G]_Rnf[A-G]$"),
}


def parse_blocks(text: str) -> list[list[str]]:
    blocks, cur = [], []
    for line in text.splitlines():
        if line.startswith("//"):
            if cur:
                blocks.append(cur)
            cur = []
        else:
            cur.append(line)
    if cur:
        blocks.append(cur)
    return blocks


def cc_topics(lines: list[str]) -> list[tuple[str, str, bool]]:
    """Return (topic, text, conditional) for every CC -!- topic."""
    out: list[tuple[str, str, bool]] = []
    depth = 0
    topic = None
    buf: list[str] = []
    cond = False

    def flush():
        if topic is not None:
            text = ""
            for piece in buf:
                if text.endswith("-") or not text:
                    text += piece
                else:
                    text += " " + piece
            out.append((topic, text.strip(), cond))

    for line in lines:
        if line.startswith("case ") or line.startswith("else"):
            depth = 1
            continue
        if line.startswith("end case"):
            depth = 0
            continue
        if not line.startswith("CC   "):
            continue
        body = line[5:]
        m = re.match(r"-!- ([A-Z ]+):\s*(.*)", body)
        if m:
            flush()
            topic, buf, cond = m.group(1), [m.group(2)], depth > 0
        else:
            buf.append(body.strip())
    flush()
    return out


def summarise(block: list[str]) -> dict[str, str] | None:
    ac = name = None
    for line in block:
        if line.startswith("AC   "):
            ac = line[5:].strip().rstrip(";")
        elif line.startswith("Names: "):
            name = line[7:].strip()
    if not ac or not name:
        return None
    de_ec = sorted({m for line in block if line.startswith("DE   ")
                    for m in re.findall(r"EC=([\d.\-n]+)", line)})
    topics = cc_topics(block)
    rhea = sorted({r for t, txt, _ in topics if t == "CATALYTIC ACTIVITY"
                   for r in re.findall(r"RHEA:(\d+)", txt)})
    loc = "; ".join((txt + (" [cond]" if c else "")) for t, txt, c in topics
                    if t == "SUBCELLULAR LOCATION") or "-"
    func = " ".join(txt for t, txt, _ in topics if t == "FUNCTION")
    tm = [line.split(";")[3].strip() for line in block
          if line.startswith("DR   General; Transmembrane")]
    go_c = [line[5:].split(";")[0] for line in block
            if line.startswith("GO   ") and "; C:" in line]
    full_name = next((line.split("Full=")[1].rstrip(";") for line in block
                      if line.startswith("DE   RecName: Full=")), "-")
    return {
        "rule": ac,
        "name": name,
        "recname": full_name,
        "de_ec": ",".join(de_ec) or "-",
        "rhea": ",".join("RHEA:" + r for r in rhea) or "-",
        "location": loc,
        "tm_trigger": ",".join(tm) or "-",
        "go_cc": ",".join(go_c) or "-",
        "function_start": (func[:70] + "...") if len(func) > 70 else (func or "-"),
    }


def main(path: str) -> None:
    rows = [r for r in (summarise(b) for b in parse_blocks(Path(path).read_text()))
            if r]
    cols = ["rule", "name", "de_ec", "rhea", "tm_trigger", "go_cc", "location",
            "recname"]
    for group, pat in GROUPS.items():
        sel = sorted((r for r in rows if pat.search(r["name"])),
                     key=lambda r: r["name"])
        print(f"## {group}: {len(sel)} rules")
        print("\t".join(cols))
        for r in sel:
            print("\t".join(r[c] for c in cols))
        with_ec = sum(r["de_ec"] != "-" for r in sel)
        with_rhea = sum(r["rhea"] != "-" for r in sel)
        print(f"# {with_ec}/{len(sel)} carry an EC in DE; "
              f"{with_rhea}/{len(sel)} carry a CATALYTIC ACTIVITY Rhea id")
        print()
    mtr = sorted((r for r in rows if GROUPS["Mtr (EC 7.2.1.4 complex)"].search(r["name"])),
                 key=lambda r: r["name"])
    print("## Mtr FUNCTION text (first 70 characters)")
    for r in mtr:
        print(f"{r['name']}\t{r['function_start']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
