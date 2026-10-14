# SLC27A5 (donkey, Equus asinus) - A0A9L0JNL2

DONKEY40 cohort review. Unreviewed TrEMBL entry, 700 aa, "long-chain-fatty-acid--CoA ligase" (ARBA name); PANTHER PTHR43107:SF25 (LONG-CHAIN FATTY ACID TRANSPORT PROTEIN 5).

## Sources
- Donkey UniProt `SLC27A5-uniprot.txt` (ARBA catalytic activities; AMP-binding domain; PROSITE AMP_BINDING).
- Donkey GOA `SLC27A5-goa.tsv`: 14 IEA rows (3 TreeGrafter GO_REF:0000118, combined GO_REF:0000120, Ensembl Compara GO_REF:0000107).
- Human ortholog review exists: `genes/human/SLC27A5/` (used for consistency; human UniProt file:human/SLC27A5/SLC27A5-uniprot.txt).
- Cached: PMID:10479480, PMID:10749848, PMID:11980911 (human enzyme characterization; abstract-only).

## Sequence
- 81.30% identity to human over 690 aligned residues, full human coverage; 10-residue N-terminal extension [file:EQUAS/SLC27A5/SLC27A5-bioinformatics/RESULTS.md].

## Biology
- Cholate:CoA ligase [PMID:10749848 "exhibited cholate:CoA ligase (choloyl-CoA synthetase) activity with both"].
- Activates chenodeoxycholate, deoxycholate, lithocholate and THCA; main role in recycling C24 bile acids [PMID:11980911 "We hypothesize that the primary function of homolog 2 is in the reactivation and recycling of C24 bile acids"].
- LC/VLC acyl-CoA synthetase; ER-associated [PMID:10479480 "For all substrates tested (C18:0, C20:0, C24:0, C26:0)"; "the protein was associated with the endoplasmic reticulum but not with"].
- Hepatic fatty acid uptake, by similarity to mouse [human UniProt].

## Decisions
- ACCEPT: LC-CoA ligase, VLC-CoA ligase, cholate-CoA ligase, LCFA and VLCFA metabolic process, bile acid metabolic process, ER, ER membrane.
- KEEP_AS_NON_CORE: plasma membrane, basal plasma membrane, LCFA import into cell, LCFA transmembrane transporter activity, bile acid biosynthetic process (main role is recycling; human review ACCEPTs this term - a deliberate difference in emphasis, not a contradiction).
- TOO_GENERAL: fatty acid transmembrane transporter activity (parent of the LCFA transporter term).
