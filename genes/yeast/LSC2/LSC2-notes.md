# LSC2 (YGR244C, P53312) notes

- Beta subunit of succinyl-CoA ligase; ATP-specific enzyme [PMID:9874242 "The yeast succinyl-CoA ligase was shown to utilize ATP but not GTP for succinyl-CoA synthesis"].
- Beta provides nucleotide specificity and succinate binding, Mg2+ cofactor (By similarity) [UniProt:P53312].
- Mitochondrial [PMID:9874242; UniProt:P53312 HTP mito proteome PMID:14576278].
- ARBA "cytoplasm" IEA marked over-annotated (bacterial default; protein is mitochondrial).

## 2026-11-11 re-review from an evolutionary perspective

Scope and method as in the LSC1 notes; the shared analysis is in LSC2-bioinformatics/ (script, results.yaml, RESULTS.md).

- Lsc2 groups with animal SUCLA2 in the PANTHER tree, a bootstrapped neighbor-joining tree and a maximum-likelihood tree [file:yeast/LSC2/LSC2-bioinformatics/RESULTS.md "The fungal subunits and animal SUCLA2 form one clade in the PANTHER tree, the neighbor-joining tree and the maximum-likelihood tree."]. Lsc2 is the SUCLA2 ortholog and a paralog of SUCLG2.
- The duplication is older than proposed in 1998 [PMID:9765291 "suggests that the A-beta and G-beta genes arose by duplication early in the evolution of multicellular eucaryotes"]; Dictyostelium and the choanoflagellate Monosiga each have one gene in each clade.
- GDP specificity marker: Gln at position 20 of the mature beta subunit [PMID:16481318 "interactions of the guanine base with a glutamine residue (Gln-20beta) and with backbone atoms provide the specificity"]. Lsc2 has Pro at the aligned position (Pro50 of the precursor). The residue is a marker only [PMID:22751660 "This contrasts with Escherichia coli SCS, which uses GDP/GTP but prefers ADP/ATP"]. Recorded as a residue site (strength CONTRIBUTES) in the PTHR11815 family review.
- Action changes: GO:0042709 succinate-CoA ligase complex IBA, ACCEPT to TOO_GENERAL (the ADP-forming child GO:0009361 is asserted; the root node correctly carries the parent because it has ADP- and GDP-forming descendants). GO:0005737 cytoplasm ARBA row, MARK_AS_OVER_ANNOTATED to TOO_GENERAL (true, entailed by mitochondrion). Both now match the S. pombe ortholog SPCC1620.08.
- PAINT handles the beta tree correctly: ADP-forming at the root, with a loss (IKR) and a GDP-forming gain at PTN000929335, which is exactly the clade that carries Gln20. Lsc2 is outside that node. The alpha tree has no equivalent, which is the cause of the wrong GDP-forming IBA on Lsc1.
- Unresolved by the trees: which copy plants, stramenopiles and excavates descend from, and the position of a second, divergent Ustilago maydis protein (A0A0D1E3R8). Neither affects an annotation on Lsc2.
- OpenScientist run (LSC2-hypotheses/beta-nucleotide-specificity-phylogeny): supports ADP-forming by assay, residue and phylogeny; could not resolve whether Lsc2 is sister to SUCLA2 with a k-mer distance tree of 18 sequences and recommended a maximum-likelihood tree with broader sampling, which was then run locally (clade of fungal subunits and animal SUCLA2, ultrafast bootstrap 90).
- Family-level observations recorded in interpro/panther/PTHR11815/PTHR11815-review.yaml: coherence changed to MOSTLY_COHERENT (ATP-citrate synthase, malate-CoA ligase and sulfoacetate-CoA ligase subunits are InterPro members of SF10); the mitochondrion IBD at the eukaryotic root needs pruning for the hydrogenosomal Trichomonas vaginalis subunits.
- Mitochondrial matrix was not added as a NEW row: no sub-mitochondrial assay of Lsc2 was found, and the transit peptide is rule-based.
