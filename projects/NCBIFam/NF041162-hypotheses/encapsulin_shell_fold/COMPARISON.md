# Blinded comparison — encapsulin NF041162 / A0A0D5NHT9

Holdout (before run) vs `openscientist.md`.

## Verdict: CONFIRMED (very high confidence), matches holdout exactly

- **Identity:** Family 2A encapsulin shell protein, **HK97 phage-capsid fold** —
  NOT a membrane protein. "Membrane protein" is a mis-annotation traceable to an
  unreviewed EMBL submission (AJY74493.1).
- **Assembly / CC:** self-assembling icosahedral 25–42 nm nanocompartment →
  **GO:0140737 encapsulin nanocompartment** (intracellular, non-membrane-bound
  proteinaceous organelle). Confirms the seed's CC mapping.
- **Independent structural support:** AlphaFold AF-A0A0D5NHT9-F1 (pLDDT 89.9) is
  an elongated α+β subunit with a large β-sheet + one ~22-aa spine helix and **no
  TM bundle**; hydropathy max KD 1.89 (< ~2.5), net charge −6 → soluble shell.

## Caveat on blindedness (weaker test than DUF1156)

OpenScientist reached the identity largely by looking up the **curated family
signatures** attached to the accession (NF041162 short-name "encap_f2a";
IPR049822 "Encapsulin nanocompartment shell protein 2A"; PF19307), which the
prompt named. So this is more a *corroboration that the CC mapping is right* than
a structure-first rediscovery. The genuinely independent part is the AlphaFold/
hydropathy evidence ruling out a membrane protein. (Contrast DUF1156, where the
DUF name gave nothing away and the mechanism was truly structure-derived.)

## Curation consequence

NF041162 → GO:0140737 CC mapping **stands, corroborated**. gain_rev=0 (reviewed
encapsulins already carry it), gain_all=897 net-new — mostly TrEMBL entries
generically named "membrane protein"/hypothetical (like this representative) that
would gain the correct non-membrane organelle CC. A clean, high-value CC gap-fill.

## Literature note

Cited PMIDs (41481934, 42297566, 41794648, 41309228, 41369466, 41239465) are very
recent and NOT in publications/ cache → treated as leads; the identity rests on
curated signatures + AlphaFold structure, which are solid.
