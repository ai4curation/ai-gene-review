# PTPRC (CD45) review notes

Review created 2026-10-03 for the ADAPTIVE_IMMUNITY project (T cell receptor area).

## Biology summary

- CD45 is a type I transmembrane receptor-type PTP on all nucleated hematopoietic cells; intrinsic PTPase activity shown biochemically [PMID:2853967 "The present study confirms that CD45 possesses intrinsic protein tyrosine phosphatase (PTPase) activity."].
- Positive role: dephosphorylates the inhibitory C-terminal tyrosine of SFKs in T and B cells [PMID:9197241 "activates Src family kinases associated with B-cell and T-cell antigen receptor signaling by constitutive dephosphorylation of the inhibitory carboxy-terminal tyrosine phosphorylation site"].
- Negative role: dephosphorylates activating tyrosines (HCK/LYN in macrophages; LCK Y394) [PMID:9197241 "CD45 decreases Src family kinase activity by dephosphorylating the tyrosine residue located within the kinase domain."]; [PMID:17719247 "a rheostat mechanism whereby CD45 differentially regulates the negatively acting pTyr-505 and positively acting pTyr-394 p56(lck) tyrosine kinase phosphorylation sites"].
- Substrate recognition: D1 binds LCK kinase, SH2 and unique domains; D2 binds kinase subdomain X [PMID:14625311].
- Beyond T cells: CD45 with CD148 required for BCR and macrophage Fc receptor signaling [PMID:18249142]; JAK phosphatase dampening cytokine signaling [PMID:11201744 "In vitro, CD45 directly dephosphorylates and binds to JAKs."]; human anti-CD45 suppresses IL-4/JAK/STAT6 [PMID:12574355].
- Human CD45 deficiency causes SCID [PMID:10700239 "Thus, CD45 deficiency in humans results in T- and B-lymphocyte dysfunction."].

## Curation decisions

- Core MF kept general: GO:0004725 protein tyrosine phosphatase activity. GO:0005001 (transmembrane receptor PTP) rows accepted as the standard RPTP classification, but not used as core because its definition requires signal binding and no physiological ligand regulating CD45 activity is established (question raised).
- 17 `protein binding` rows: 3 LCK rows (PMID:7507203, PMID:8576115 x2) changed to protein kinase binding; ITGAL row changed to integrin binding; the rest removed (enzyme-substrate peptide assays from PMID:19167335, CSK phosphorylating CD45, galectin-1 lectin binding, CD2 crosslinking, SKAP1 substrate, EGFR screen, beta-catenin).
- Beta-catenin IPI (PMID:12370829): the abstract says CD45's catalytic domain did NOT detectably bind catenins. Flagged as a suggested question for curators.
- `synapse` (GO:0045202, EXP PMID:35767951 and the UniProt SubCell mapping) changed to immunological synapse (GO:0001772): the UniProt "Synapse" location refers to the T cell contact, not a neuronal synapse.
- `protein tyrosine kinase inhibitor activity` (IDA PMID:12100025) removed: the paper measured LCK protein expression after antibody crosslinking; CD45 is not an enzyme inhibitor of kinases.
- Knockout, antibody-blockade and cytokine-output process rows kept as non-core; cell cycle, bone marrow development, stem cell development/proliferation, calcium release, defense response to virus, DN2 thymocyte differentiation marked over-annotated; response to gamma radiation and response to aldosterone removed; heparin and HSPG binding left undecided (no accessible source).
- No NEW rows: immunological synapse arrives via MODIFY; peptidyl-tyrosine dephosphorylation is implied by the MF.

## Additional publications cached

- PMID:17719247 (McNeill 2007, LCK rheostat), PMID:11201744 (Irie-Sasaki 2001, JAK phosphatase), PMID:10700239 (Kung 2000, human SCID).
