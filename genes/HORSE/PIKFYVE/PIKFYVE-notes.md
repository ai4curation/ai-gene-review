# PIKFYVE (horse, A0A3Q2HE51) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: DONKEY40_HORSE_PARTNER target for the donkey PIKFYVE short isoform (A0A9L0JQ61, reviewed separately in genes/EQUAS/PIKFYVE). No horse review existed; created with `just fetch-gene HORSE A0A3Q2HE51 --alias PIKFYVE` (stub id confirmed A0A3Q2HE51). ProtNLM2 output was not opened or used.

Deep research: `just deep-research-falcon HORSE PIKFYVE --fallback perplexity-lite` failed (falcon "Failed to authenticate"; perplexity 401 insufficient quota). Literature was read directly from cached publications instead (PMIDs cached with `just fetch-pmid`).

### Identity
- TrEMBL, PE 4, 2108 aa, Ensembl ENSECAP00000031851.3, VGNC:21455. Full-length gene model, not a fragment or short isoform.
- PANTHER PTHR46715:SF1, the single PIKfyve subfamily, shared with human Q9Y2I7 and mouse Q9Z1T6 (interpro/panther/PTHR46715/PTHR46715-entries.csv). IBA donors: PTN002928511/PTN002928512 with human Q9Y2I7 and mouse MGI:1335106. This, not the similarity score, is the basis for transfer.
- Sequence comparison (PIKFYVE-bioinformatics/RESULTS.md, compare_orthologs.py): 92.89% identity to human over 2095 paired residues (99.86% of human covered); all eight FYVE Zn-ligand Cys conserved (offset +10); catalytic Lys (human K1877, K1877E kinase-dead [PMID:33098764]) = horse K1887; autophosphorylation site human S2053 = horse S2063.
- Caution recorded: the old mouse numbering (K1831E kinase-dead in PMID:14530284; K1999 in PMID:11706043) does not match the current Q9Z1T6 sequence, so those residue numbers were not used.

### Key literature (mammalian orthologs)
- Mouse PIKfyve makes PtdIns5P and PtdIns(3,5)P2 [PMID:10419465 "displays a strong in vitro activity for PtdIns 5-P and PtdIns 3,5-P(2) generation"].
- FYVE finger required for late endocytic membrane targeting [PMID:11706043 "PIKfyve localization to membranes of the late endocytic pathway was found to be absolutely dependent on the presence of an intact FYVE finger."].
- PAS complex with VAC14 and FIG4 [PMID:17556371 "formed a stable ternary complex with ArPIKfyve and PIKfyve"]; 5:1:1 stoichiometry and autophosphorylation repression [PMID:33098764 "PIKfyve autophosphorylation represses its lipid kinase activity and stimulates Fig4 lipid phosphatase activity."].
- Serine kinase on p40/RABEPK; endosome-to-TGN [PMID:14530284].
- Cell-type processes (inhibitor/knockout necessity evidence): neutrophil chemotaxis/ROS/phagosome-lysosome fusion [PMID:28779020]; melanosome biogenesis [PMID:29584722]; MHC-II antigen presentation [PMID:30612035]; STING activation via PtdIns(3,5)P2 [PMID:41639454]; EGFR nuclear transit [PMID:17909029]; coronavirus entry [PMID:32221306].

### Decisions (44 rows)
- ACCEPT: PtdIns3P 5-kinase (IBA, IEA), PtdIns 5-kinase (IBA, IEA), early and late endosome membrane, PAS complex.
- MODIFY: general MF terms (kinase, transferase, PI kinase, nucleotide binding, metal ion binding -> zinc ion binding, ser/thr kinase -> protein serine kinase); general CC (endosome membrane, vesicle membrane, cytoplasmic vesicle -> early/late endosome membrane); PI metabolic process and PI(3,5)P2 metabolic process -> PI(3,5)P2 biosynthetic (GO:1903102) / PI5P biosynthetic (GO:1904563).
- KEEP_AS_NON_CORE: cell-type processes PAINT chose to propagate (neutrophil chemotaxis, ROS regulation, melanosome organization, phagosome-lysosome fusion, phagocytic vesicle membrane), plus Ensembl projections of human experimental terms (MHC-II, phagosome maturation, retrograde transport, STING, autophagosome assembly, membrane raft), ATP binding, cytosol, protein serine kinase.
- MARK_AS_OVER_ANNOTATED: Golgi membrane (ARBA), intracellular protein localization (ARBA), PI4P 5-kinase (ARBA; PAINT did not propagate this from mouse IDA, treated as deliberate), virus endocytosis (host-requirement), protein localization to nucleus (single siRNA tumour-cell study), DEP -> intracellular signal transduction.
- No NEW terms proposed.

### Relative
Human PIKFYVE (Q9Y2I7), same PANTHER subfamily PTHR46715:SF1 and PAINT donor; no review exists in the repo (no genes/human/PIKFYVE, no mouse Pikfyve). The module modules/phosphoinositide_biosynthesis.yaml lists human PIKFYVE as a representative of the PI3P 5-kinase step and places it in PTHR46715, consistent with UniProt.
