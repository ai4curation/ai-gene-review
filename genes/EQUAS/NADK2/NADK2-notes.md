# NADK2 (donkey, A0A9L0K2P4) notes

## Sources
- Donkey UniProt A0A9L0K2P4 (unreviewed, TrEMBL; Ensembl ENSEASP00005059781.1). All names, EC, subunit and location statements in this record are ARBA-derived (ECO:0000256), i.e. automated predictions, not evidence.
- Human ortholog NADK2 Q4G0N4 (Swiss-Prot), genes/human/NADK2/NADK2-uniprot.txt, and the human review genes/human/NADK2/NADK2-ai-review.yaml.
- Sequence comparison: NADK2-bioinformatics/RESULTS.md (Biopython global alignment).

## Biology (human ortholog, transferred by orthology)
- Human NADK2 is the mitochondrial NAD kinase: [file:human/NADK2/NADK2-uniprot.txt "Mitochondrial NAD(+) kinase that phosphorylates NAD(+) to yield NADP(+)"].
- Activity with ATP and polyphosphate shown on purified protein: [PMID:23212377 "showing that C5orf33 protein has NADK activity using ATP and poly(P) as phosphoryl donors"].
- Mitochondrial localization with a functional N-terminal targeting sequence: [PMID:23212377 "confirming that C5orf33 protein is a mitochondrial NADK, and that its N-terminal 62 residues contain a functional mitochondrial-targeting sequence"].
- NAD kinase is the sole NADP+ biosynthetic enzyme: [PMID:23212377 "NAD kinase is the sole NADP(+) biosynthetic enzyme"].
- Homodimer statement in human UniProt is a curator inference (ECO:0000305) from PMID:23212377; the cached text does not contain a dimerization result.

## Donkey sequence
- 96.59% identity over 410 aligned residues to human; but the donkey model has a 96-aa N-terminal extension and lacks the human 288-319 segment (= human isoform 2 deletion VSP_027193) [file:EQUAS/NADK2/NADK2-bioinformatics/RESULTS.md]. GGDG motif retained.
- Consequence: the gene-level function (mitochondrial NAD kinase) transfers by orthology; the activity of this exact isoform-2-like model, and the use of its internal transit peptide, are unverified.

## Annotation decisions
- NAD+ kinase activity (GO_REF:0000120): ACCEPT (core).
- mitochondrion (GO_REF:0000120), mitochondrial matrix (ARBA GO_REF:0000117): ACCEPT.
- NAD+ metabolic process (TreeGrafter GO_REF:0000118): ACCEPT; added NEW NADP+ biosynthetic process (GO:0006741), the direct product of the catalysed step (the enzyme performs the step; passes the participation test).

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not consulted. Deep research could not be generated: `just deep-research EQUAS NADK2 --provider falcon` failed with "Failed to authenticate", and the perplexity-lite fallback also failed; the review uses the cached literature (PMID:23212377 full text, PMID:24847004 abstract) and new sequence analysis.

### Identity of the benchmark accession (gene-model problem)
- UniProt lists three donkey NADK2 entries, all from Ensembl gene ENSEASG00005014681.2: A0A9L0K2P4 (506 aa, benchmark), A0A8C4M4D0 (538 aa) and A0A8C4M5G3 (560 aa). [file:EQUAS/NADK2/NADK2-bioinformatics/RESULTS-rereview.md]
- A0A8C4M4D0 aligns gap-free to the whole human canonical NADK2 (Q4G0N4, 442 aa; 96.83% identity), as does the horse model F7DCV0. It is the donkey canonical-equivalent product.
- A0A9L0K2P4 is an alternative-splice model equivalent to human isoform 2 (VSP_027193): it lacks the segment equivalent to human 288-319, which holds human Ser306, Lys317 and Trp319, the positions mapped to the NAD+-binding Asp/Thr/Tyr of M. tuberculosis Ppnk [PMID:23212377 "although the GGDG motif and NE/D short motif were completely conserved, the Asp, Thr and Tyr residues were not, corresponding instead to Ser-306, Lys-317 and Trp-319"]; [PMID:23212377 "taking part in the creation of NAD+-binding site"]. The GGDG motif is retained. The earlier review recorded the deletion but not that it removes these positions.
- All equid models carry a 96-residue N-terminal extension before the Met (donkey Met97) that aligns to human Met1; the transit-peptide-equivalent region is internal (97-158). Start site unresolved.

### Evolutionary grounding
- Donkey NADK2 is in PANTHER PTHR13158:SF5 (NAD kinase 2, mitochondrial), the same subfamily as human Q4G0N4, mouse Q8C5H8 and rat Q1HCL7 (interpro/panther/PTHR13158/PTHR13158-entries.csv). PAINT IBDs in this family: NAD+ kinase activity and NAD+ metabolic process at PTN004406956; mitochondrion at PTN000994636 (taxon Eukaryota); seeds human NADK2 and mouse Nadk2. No FamilyReview exists for PTHR13158, so there is no subfamily-placement disagreement to report. The donkey GOA rows cite TreeGrafter node PTN001407776, which is not in the cached PAINT table.

### Annotation decisions (changes from the earlier version)
- NAD+ kinase activity: ACCEPT (gene-level; isoform caveat in reason and suggested_questions).
- mitochondrion, mitochondrial matrix: ACCEPT; added PMID:24847004 support (NADK2 loss lowers mitochondrial NADP(H); DECR and lysine-degradation steps depend on it).
- NAD+ metabolic process: changed ACCEPT -> MODIFY to NADP+ biosynthetic process (GO:0006741; is_a descendant of GO:0019674, verified via OLS hierarchicalAncestors), which the enzyme itself performs. The separate NEW row for GO:0006741 was dropped as redundant with the MODIFY replacement.
- Description rewritten to drop the transit-peptide claim for this model and to state the missing NAD+-binding positions.

### Relative
- Canonical product of the same gene, A0A8C4M4D0, has no review in the repo (would go in genes/EQUAS/NADK2__A0A8C4M4D0). The human ortholog review genes/human/NADK2 has every row reviewed but status INITIALIZED; it carries the same ACCEPT(NAD+ metabolic process)+NEW(NADP+ biosynthetic process) pattern that was changed here.
- Module: modules/nadp_synthesis_and_nr_salvage.yaml (NADK2 is the mitochondrial NAD+ -> NADP+ step).
