# Notes for DANRE spns1

- Core function is lysosomal membrane transmembrane transport; the current UniProt record specifies proton-dependent lysophospholipid efflux [file:DANRE/spns1/spns1-uniprot.txt "efflux of lysophospholipids"].
- A proposed new MF term was added because GO:0022857 is too generic for the now-described proton-dependent lysosomal lysophospholipid efflux activity, while no existing specific GO term was found in the local term cache.
- Autophagy and senescence annotations are retained as non-core because they are process consequences of impaired lysosomal transport [PMID:24967584 "Beclin 1 suppression ameliorates Spns1 loss-mediated senescence"].

## Falcon deep research enrichment (2026-05)

- Integrated `spns1-deep-research-falcon.md` (Edison; He 2022 PNAS, Ha 2024 JCI Insight, Chávez 2024 iScience, Coffey 2021 J Dev Biol).
- Substrate refined from generic "lysophospholipids" to the demonstrated zwitterionic substrates LPC and LPE [file:DANRE/spns1/spns1-deep-research-falcon.md "specificity for **lysophosphatidylcholine (LPC)** and **lysophosphatidylethanolamine (LPE)**"]. The brief's "sphingolipids/sphingosine" framing is a lower-confidence secondary claim (Ha 2024 mammalian genetics); falcon notes "highest-confidence substrate assignment remains LPC/LPE". Core function kept as lysophospholipid efflux.
- Localization corroborated: lysosomal/late-endosomal membrane, LAMP1/Rab7 colocalization.
- Mechanism: pH-dependent (acidic optimum ~5-6), proton-coupled; conserved residues R76, E164, H427 required.
- New zebrafish-specific process: endocardial-autonomous spns1 drives cardiac valve morphogenesis via notch1 signaling (Chávez 2024) — noted in description but not added as a NEW annotation (no curated PMID cached; would require IC/primary-PMID pairing).
- MF term check (OLS): GO:0051978 "lysophospholipid:sodium symporter activity" is the only lysophospholipid transporter MF term but is Na+-coupled (spns1 is H+-coupled efflux), and GO:0005548 is obsolete — so the proposed_new_terms entry for proton-dependent lysophospholipid efflux remains justified; justification updated accordingly.
- No falcon contradictions to existing actions; the PMID:24967584 "H+-carbohydrate transporter" hypothesis is now flagged as superseded by the LPC/LPE transporter demonstration.
