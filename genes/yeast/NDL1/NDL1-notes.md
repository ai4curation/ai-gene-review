# NDL1 (S. cerevisiae, Q06568) review notes

## 2026-09-27 initial review (claude-code)

Context: yeast NudE-family member, comparative for `modules/nucleokinesis.yaml` (human NDE1/NDEL1 reviewed).

Key evidence
- Discovery, genetics, localization [PMID:15965467 "Taken together, the growth and nuclear segregation assays show that NDL1 has an important but not essential role in the dynein pathway."; "No foci of Ndl1–3GFP were found at microtubule plus ends in pac1 Δ cells"; Pac1 co-IP; Pac1 overexpression suppresses ndl1].
- Ndl1 binds dynein intermediate chain N-terminus (ICN), only contact on dynein; increases dynein-Pac1 association [PMID:37730751 "These data also indicate that the ICN is the only contact point on the yeast dynein complex for Ndl1."].
- Falcon deep research (NDL1-deep-research-falcon.md): sequential Pac1 hand-off model (Ndl1 and dynein motor compete for Pac1 surface); consistent with primary papers. Used as supporting text.

Decisions
- NEW MF GO:0045505 dynein intermediate chain binding and GO:0140659 cytoskeletal motor regulator activity (IDA PMID:37730751); NEW CC GO:0035371.
- Nuclear migration along microtubule IMP/IPI accepted (core).
- MT plus-end binding IDA marked over-annotated: same paper shows plus-end foci require Pac1; in vitro Ndl1 not on MTs without dynein.
- Nucleus (HDA/IDA/IEA) kept non-core; peroxisome IDA (proteome screen, Ndl1 absent from cached text) UNDECIDED.
