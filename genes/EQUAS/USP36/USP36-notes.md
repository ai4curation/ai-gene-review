# USP36 (donkey, Equus asinus) - A0A9L0JCH5

DONKEY40 cohort review. Unreviewed TrEMBL entry, 1156 aa, "Ubiquitin carboxyl-terminal hydrolase" (EC 3.4.19.12); PANTHER PTHR24006:SF653 (USP36); peptidase C19.

## Sources
- Donkey UniProt `USP36-uniprot.txt` (USP domain 122-456; ACT_SITE 131 and 415).
- Donkey GOA `USP36-goa.tsv`: 18 IEA rows (3 TreeGrafter GO_REF:0000118: nucleus, cytosol, regulation of apoptotic process; combined GO_REF:0000120; Ensembl Compara GO_REF:0000107 from human/mouse experimental; UniRule GO_REF:0000104; GO_REF:0000108 inter-ontology).
- Human ortholog Q9P275 UniProt fetched to `USP36-bioinformatics/human-Q9P275-uniprot.txt`. No human/mouse USP36 review in repo.
- Cached publications: PMID:19208757 (nucleolar DUB; NPM1/FBL), PMID:22622177 (selective autophagy), PMID:35989368 (CEP63 K48 deubiquitination), PMID:12429849 (nucleolar proteome).

## Sequence
- 78.10% identity to human over 1114 aligned residues; 33-residue insertion inside USP domain (donkey 253-285); catalytic Cys131 and His415 (=human His382) conserved [file:EQUAS/USP36/USP36-bioinformatics/RESULTS.md].

## Biology
- Nucleolar deubiquitinase that deubiquitinates and stabilizes nucleophosmin/B23 and fibrillarin; depletion reduces rRNA transcription and processing [PMID:19208757 "USP36 deubiquitylated the nucleolar proteins nucleophosmin/B23 and fibrillarin, and stabilized them by counteracting ubiquitylation-mediated proteasomal degradation"].
- Localizes to nucleoli via C-terminal basic stretches [PMID:19208757 "USP36 localized to nucleoli via the C-terminal region"].
- Controls selective autophagy activation [PMID:22622177 "USP36 function in p62-dependent selective autophagy is conserved in human cells"].
- K48-linked deubiquitination of CEP63 [PMID:35989368 "USP36 is identified for stabilizing CEP63 by enhancing its K48-dependent deubiquitination"].
- H2B deubiquitination at promoters (PMID:29274341, not cached; via human UniProt).

## Decisions
- ACCEPT: DUB activity, protein deubiquitination, nucleolus, nucleus, protein stabilization, regulation of protein stability, regulation of rRNA processing, K48-linked DUB.
- KEEP_AS_NON_CORE: cytosol, cytoplasm, nuclear speck, chromatin remodeling, chromatin organization, H2B DUB, nucleolus organization, negative regulation of macroautophagy.
- MARK_AS_OVER_ANNOTATED: ubiquitin-dependent protein catabolic process (UniRule; USP36 opposes degradation of its substrates), regulation of apoptotic process (TreeGrafter; no USP36-specific evidence).
