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

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 files were not opened or used.

### Deep research
- `just deep-research-falcon EQUAS USP36 --fallback perplexity-lite` failed: Edison API "Failed to authenticate", and the perplexity-lite fallback timed out (600 s). No deep-research file exists; the re-review uses cached primary papers instead.
- Newly cached: PMID:25775507 (c-Myc), PMID:29274341 (H2Bub1, full text), PMID:27445338 (NEDD4L, cytoplasm, full text), PMID:29273634 (mouse KO, DHX33), PMID:22902402 (yeast Ubp10 / RNA Pol I; human USP36 complements), PMID:36912080 (EXOSC10 SUMOylation), PMID:14715245 (cloning).

### Identity of A0A9L0JCH5 (gene model)
- Ensembl gene ENSEASG00005005026 (USP36) has four long products: A0A9L0JCH5 1156 aa (Ensembl canonical, ENSEAST00005074877), A0A9L0I9H9 1123 aa, A0A8C4LEG8 1124 aa, A0A9L0K514 1064 aa [file:EQUAS/USP36/USP36-bioinformatics/RESULTS-rereview.md].
- A0A9L0I9H9 is identical to the benchmark except for lacking residues 253-285 (33 aa, AGERRGASWFQGLETRAGALGPGSLPAPLPSVA); both transcripts have 20 exons, so the segment is an exon extension (alternative splice site).
- The segment has no counterpart in horse (F6W2H6), human Q9P275, mouse B1AQJ2 or cattle A0A3Q1M0E6. So the benchmark is the Ensembl-canonical but atypical splice form; catalytic Cys131/His415 retained. No donkey USP36 entry is reviewed, so there is no separate canonical UniProt product to review.

### Evolutionary grounding
- Donkey, human and mouse USP36 are all in PANTHER PTHR24006:SF653 (UBIQUITIN CARBOXYL-TERMINAL HYDROLASE 36) [interpro/panther/PTHR24006/PTHR24006-entries.csv; donkey UniProt DR PANTHER]. Transfers from human/mouse USP36 are within the subfamily.
- Human GOA (QuickGO, 2026-10-21): IBA for cysteine-type deubiquitinase activity, regulation of protein stability, regulation of apoptotic process (seeded by FBgn0260936, Q0WX57 — not USP36), nucleus and cytosol (is_active_in). The apoptosis node is deep and USP36-independent.
- Yeast Ubp10 is the functional ortholog named in PMID:22902402 ("USP36, the human ortholog of Ubp10, complements the ubp10Δ allele for RNAPI stability, pre-rRNA processing, and cell growth in yeast"). Not used for direct transfer.
- No PANTHER family review exists under interpro/panther/PTHR24006/ (only entries/metadata/partial PAINT tsv), so no subfamily disagreement to report. No module in modules/ mentions USP36.

### Changes
- nucleus: ACCEPT -> MODIFY to nucleolus (general term; gene carries nucleolus).
- chromatin organization: KEEP_AS_NON_CORE -> MODIFY to chromatin remodeling (is_a child, verified OLS; gene carries it).
- regulation of protein stability: ACCEPT -> MODIFY to protein stabilization (all evidence is stabilization).
- H2B deubiquitinase / chromatin remodeling now quoted from PMID:29274341 [PMID:29274341 "We show that USP36 interacts with H2B and deubiquitinates H2Bub1 in cells and in vitro"]; note the p21 effect is "primarily within its gene body", not just promoters as UniProt says.
- cytoplasm/cytosol: quoted from PMID:27445338 (rat PC12) instead of UniProt.
- regulation of apoptotic process: kept MARK_AS_OVER_ANNOTATED; apoptosis after knockdown is downstream of DHX33/ribosome biogenesis loss [PMID:29273634 "USP36 down-regulation alters cell proliferation in human cancer cells by inducing both apoptosis and cell cycle arrest"].
- Description rewritten (adds DHX33, RNA Pol I, c-Myc, SUMOylation, NEDD4L; corrects "promoters"; states splice-form identity).
- SUMO ligase activity (PMID:36912080) not added as NEW: single-laboratory report, not curated for human; raised as a suggested question.

### Relative
- Human USP36 (Q9P275), ortholog, same PANTHER subfamily SF653. No review in genes/human/ (none for mouse Usp36 or yeast UBP10 either).
