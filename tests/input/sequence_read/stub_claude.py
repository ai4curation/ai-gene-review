#!/usr/bin/env python3
"""Stand-in for the `claude` CLI in sequence-read tests (no model is called).

It answers the FEAT and PSEUDO prompts deterministically from the sequence in the
prompt: a Pfam domain only for the real sequence (passed in SEQREAD_STUB_REAL),
and "active" only while residue 124 is Cys (PTEN's catalytic Cys124).
"""

import json
import os
import sys

if "--version" in sys.argv:
    print("0.0.0 (stub)")
    sys.exit(0)
prompt = sys.stdin.read()
seq = prompt.split(">sequence\n", 1)[1].replace("\n", "")
if '"pfam_domains"' in prompt:
    real = seq == os.environ.get("SEQREAD_STUB_REAL")
    ans = {
        "pfam_domains": [{"accession": "PF10409", "name": "PTEN_C2", "start": 186, "end": 350}] if real else [],
        "transmembrane_helices": [],
        "signal_peptide": False,
        "protein_name": "PTEN" if real else "unknown",
        "ec_number": None,
        "function": "Lipid phosphatase.",
    }
else:
    active = seq[123] == "C"
    ans = {
        "protein_name": "PTEN",
        "enzyme_family": "protein tyrosine phosphatase",
        "catalytic_residues": [{"role": "nucleophile", "residue": "C", "position": 124}] if active else [],
        "substituted_or_missing": [] if active else [{"role": "nucleophile", "expected": "C", "found": seq[123], "position": 124}],
        "catalytically_active": "yes" if active else "no",
        "ec_number": "3.1.3.67",
        "reason": "stub",
    }
print(json.dumps({
    "result": "Here it is:\n" + json.dumps(ans),
    "is_error": False,
    "total_cost_usd": 0.0,
    "num_turns": 1,
    "usage": {"input_tokens": 900, "output_tokens": 50},
    "modelUsage": {"stub-model": {}},
}))
