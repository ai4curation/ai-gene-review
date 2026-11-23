# ADAT3 notes

## 2026-11-21

Deep research provider execution was unavailable in this sparse ADAT worktree, so this review was
completed from cached UniProt/GOA/PANTHER/Reactome data plus the fetched primary papers.

ADAT3 is the non-catalytic partner of human hetADAT. Torres et al. identify the enzyme as
"hetADAT, composed of two subunits: ADAT2 and ADAT3" and localize the complex to the nucleus
[PMID:25916855]. The 2025 structural/disease analysis assigns substrate recognition to the ADAT3
N-terminal domain and places patient ADAT3 variants in a mechanism that reduces the A34-to-I34
editing activity of the ADAT2:ADAT3 heterodimer [PMID:40120092].

The zinc-binding row is retained because the human UniProt record retains Zn(2+) ligand features
in ADAT3 by mouse inference. ADAT3 is catalytically inactive, but this is a structural
specialization of a deaminase-like partner rather than loss of the metal-binding pocket.

`PANTHER:PTN001668995` carries the SF156 ADAT3/TAD3 location rows in PAINT, but PAINT correctly
keeps `GO:0052717` on the catalytic SF149 ADAT2/TAD2 node. `just paint-losses human ADAT3`
reported no IRD or IKR on the human ADAT3 lineage.
