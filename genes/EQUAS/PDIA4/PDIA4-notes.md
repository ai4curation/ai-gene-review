# PDIA4 (donkey, A0A8C4LTV9) - review notes

DONKEY40 cohort. 11 IEA GOA rows.

## Chimeric gene model (key finding)
- The entry is 1197 aa; human PDIA4 (P13667) is 645 aa. Donkey record: [file:EQUAS/PDIA4/PDIA4-uniprot.txt "SIMILARITY: Belongs to the krueppel C2H2-type zinc-finger protein family."] and ["SIMILARITY: Belongs to the protein disulfide isomerase family."]; domains: KRAB (9-80), ten C2H2 zinc fingers, then thioredoxin domains.
- [file:EQUAS/PDIA4/PDIA4-bioinformatics/ALT_ENTRY.md "A0A8C4LTV9 (1197 aa) residues 571-1197 align locally to P13667 (645 aa) residues 17-645"]. The human signal peptide (1-20) has no contiguous counterpart: [file:EQUAS/PDIA4/PDIA4-bioinformatics/RESULTS.md "SIGNAL : human [1, 20] MA -> donkey [1, 541] MS"] (residues scattered over 541 donkey positions by the global aligner).
- Second donkey entry from the same Ensembl gene, A0A8C4PKQ4 (664 aa), also begins with a KRAB A-box-like sequence: [ALT_ENTRY.md "First 30 residues of A0A8C4PKQ4: MAEPARLPLTFEDVAIYFSEQEWQKLEAWQ"], and is 100% identical to A0A8C4LTV9 over the PDI region.
- Interpretation: Ensembl gene-model fusion of a neighbouring KRAB-ZNF gene to PDIA4 (signal-peptide exon missed). Horse also has a 1248-aa PDIA4 entry (F6WGL8) besides 645-aa entries (UniProt search, 2026-10-14), consistent with an annotation issue in equid assemblies. Not experimentally verified.
- PDI catalytic sites conserved: ["DISULFID Redox-active: human [91, 94] CC -> donkey [643, 646] CC"], ["DISULFID Redox-active: human [555, 558] CC -> donkey [1107, 1110] CC"]; C-terminal REEL vs human KEEL.

## Function
- [PMID:16677074 "An examination of the pH-dependence and nature of the rate limiting step for the peptide thiol-disulfide oxidase activity of these enzymes reveals that, with the exception of PDIr, they are all remarkably similar."] (ERp72 = PDIA4 among the six).
- Human UniProt: [file:EQUAS/PDIA4/PDIA4-bioinformatics/human-P13667-uniprot.txt "SUBCELLULAR LOCATION: Endoplasmic reticulum lumen"]; chaperone complex with HSPA5/HSP90B1/PDIA6.

## Decisions
- Accept PDI activity, ER lumen, protein folding. REMOVE nucleus and regulation of DNA-templated transcription (both from the fused KRAB-ZNF part). Melanosome and cell redox homeostasis over-annotated.
- ProtNLM2 GO:0003690 double-stranded DNA binding: driven by the zinc-finger segment (evidence phmmer hit to mouse ZNF148, Q61624); not PDIA4 biology -> NPI, WRONG_INPUT_SEQUENCE.

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not consulted for this re-review.

### Deep research
- `just deep-research-falcon EQUAS PDIA4 --fallback perplexity-lite` failed: falcon "Exception: Failed to authenticate"; perplexity-lite "HTTP error: 401 ... insufficient_quota". No deep-research file was produced. The review relies on cached publications that name ERp72 and on new sequence/locus analysis.

### Identity of A0A8C4LTV9 (merged gene model)
- New analysis: `PDIA4-bioinformatics/locus_context_rereview.py` -> `RESULTS-rereview.md` (Ensembl REST + UniProt sequences; existing RESULTS.md/ALT_ENTRY.md left untouched).
- [file:EQUAS/PDIA4/PDIA4-bioinformatics/RESULTS-rereview.md "N-terminal segment vs human ZNF786 (Q8N393, 782 aa): 64.2% identity over 565 paired residues; donkey 1-580, human 1-649"]; vs ZNF425 only 45.2%.
- [file:EQUAS/PDIA4/PDIA4-bioinformatics/RESULTS-rereview.md "C-terminal segment vs human PDIA4 (P13667, 645 aa): 90.1% identity over 615 paired residues; donkey 583-1197, human 31-645"].
- Synteny: human ZNF425, ZNF786 and PDIA4 lie in that order on the minus strand of 7q36.1 (ZNF786 immediately 5' of PDIA4). Donkey chr1 (+ strand) has ZNF425 (1004371-1014880) then PDIA4 (1023772-1078943, 55 kb vs 25 kb in human), and no separate ZNF786 gene. So the KRAB-ZNF segment is donkey ZNF786, merged into the PDIA4 gene model, and the PDIA4 signal-peptide exon was missed. The PDIA4 portion (~581-1197) lacks residues 1-30 of human PDIA4 (signal peptide + start of the acidic region) but has all three CGHC sites and the C-terminal REEL retrieval signal.
- Benchmark accession = alternative (merged) gene model of donkey PDIA4. No reviewed/canonical donkey PDIA4 entry exists; the other donkey entry A0A8C4PKQ4 also has an aberrant KRAB-like N-terminus. Recorded as source_defects (resource OTHER, Ensembl build) on the nucleus and transcription rows.

### Evolutionary grounding
- UniProt: PANTHER PTHR18929:SF210 (PROTEIN DISULFIDE-ISOMERASE A4), the same subfamily as human P13667, mouse P08003, rat P38659, bovine Q29RV1 (interpro/panther/PTHR18929/PTHR18929-entries.csv). The task header said "PANTHER: (none listed)" but the UniProt record does list it.
- PAINT (PTHR18929-paint.tsv): root node PTN000432607 IBD for ER, PDI activity, protein folding, response to ER stress; PTN001448731 IBD cell surface with donors MGI:104864 and P13667 (i.e. the PDIA4 clade). NOT nodes (PTN000750846 ER stress, Amniota; PTN002553919/PTN002706902 PDI activity; PTN008566470) are on other clades: human PDIA4 retains its IBA for GO:0034976, so the donkey TreeGrafter row (PTN008566466) is consistent.
- No interpro/panther PTHR18929 family review file (only entries/metadata/paint), so no subfamily-placement disagreement to report. No module under modules/ mentions PDIA4/P13667.

### Changes vs previous review
- Actions unchanged (all still hold). Supports improved: cell surface now cites PMID:19995400 ["ERp72, ERp57, ERp44 and ERp29 are released by platelets and relocate to the cell surface following platelet activation."] instead of a listing of human annotations; ER stress now cites PMID:7916014; protein folding adds PMID:22665516 ["ERp72-cyclophilin B complex that enhances the rate of folding of immunoglobulin G"] and PMID:12475965; melanosome adds PMID:17081065. ARBA-only "krueppel" SIMILARITY quotes replaced by the InterPro KRAB signature line. Description rewritten with ZNF786 identification.

### Relative
- Human PDIA4 (P13667), ortholog in PTHR18929:SF210; no review exists in genes/human/. Needs review.
