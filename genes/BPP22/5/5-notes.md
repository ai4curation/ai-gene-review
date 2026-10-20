# Gene 5 (CAPSD_BPP22, P26747) Notes

## Overview
- **Gene symbol:** `5`
- **UniProt ID:** `P26747` (`CAPSD_BPP22`)
- **Protein name:** Major capsid protein (gp5; Coat protein; Major head protein; Gene product 5)
- **Length:** 430 AA

## Function & Structural Insights
- **T=7 laevo Icosahedral Capsid Shell (415 copies):** Polymerizes as monomers around the scaffolding protein (gp8) core and a single portal dodecamer (gp1) to form a 415-subunit procapsid (60 hexons + 11 pentons, as one 5-fold vertex is occupied by the 12-fold portal ring) [PMID:20223221, PMID:21220301, PMID:28270620, PMID:36851569].
- **HK97-like Core Fold + Inserted Telokin-like I-Domain (ED Domain):** Possesses the canonical bacteriophage HK97 coat protein core (N-arm, E-loop, P-domain, A-domain) plus a nonconserved 124-residue telokin-like immunoglobulin insertion domain (I-domain, residues 223–345, NMR PDB: `2M5S`) that acts as a folding nucleus for the monomer and mediates intercapsomer "molecular staple" contacts across the icosahedral 2-fold axis via its D-loop [PMID:20223221, PMID:24600011, PMID:26269173].
- **Procapsid Maturation & Expansion Without Crosslinks or Cementing Proteins:** Upon DNA packaging and scaffolding protein (gp8) release, the procapsid expands (~10% in radius) into a thinner, angular, highly stable mature T=7 capsid. Maturation involves straightening of the spine helix, reordering of the N-arm and P-loop, closure of the skewed hexon local 6-fold opening into symmetric hexons, and formation of extensive intersubunit salt bridges and hydrogen bonds that stabilize the capsid without chemical crosslinks (unlike HK97) or auxiliary cementing proteins (unlike phage L Dec) [PMID:15784254, PMID:20223221, PMID:21220301, PMID:28270620, PMID:36851569].

## Domains & Orthology
- **InterPro:** `IPR024659` (`Phage_coat_Gp5`)
- **Pfam:** `PF11651` (`P22_CoatProtein`, 1 hit)
- **Gene3D:** `G3DSA:2.40.30.240` (immunoglobulin/telokin-like I-domain, 1 hit)

## Curation Decisions
- `GO:0019028` (viral capsid, IDA PMID:15784254 & IEA GO_REF:0000043): **MODIFY** to `GO:0039620` (`T=7 icosahedral viral capsid`) — `GO:0039620` is a more specific `is_a` child of `GO:0019028` already annotated on `5`.
- `GO:0039620` (T=7 icosahedral viral capsid, IDA PMID:21220301, IDA PMID:28270620, IEA GO_REF:0000043): **ACCEPT** — gp5 forms the T=7 laevo icosahedral viral capsid shell [PMID:21220301, PMID:28270620].
- `GO:0042802` (identical protein binding, IDA PMID:15784254, IPI PMID:16698545, IPI PMID:20223221): **KEEP_AS_NON_CORE** — coat protein subunits self-associate into hexamers and pentamers via intersubunit contacts (and C-terminal domain dimers in solution) [PMID:15784254, PMID:20223221]; note that PMID:16698545 primarily studies phage L Dec protein binding to capsids, while P22 gp5 self-associates into capsomers.
- `GO:0046729` (viral procapsid, IDA PMID:15784254 & IDA PMID:26269173): **ACCEPT** — gp5 forms the outer shell of the precursor viral procapsid prior to expansion [PMID:15784254, PMID:26269173].
- `GO:0046797` (viral procapsid maturation, IDA PMID:15784254 & IMP PMID:26269173): **ACCEPT** — conformational rearrangements of gp5 drive procapsid expansion and maturation into the stable virion shell [PMID:15784254, PMID:26269173].
