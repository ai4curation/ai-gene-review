# EIF2S1 (eIF2alpha) review notes

## Literature search (no deep-research provider available)
Sources checked: UniProt P05198 (curated FUNCTION, ACTIVITY REGULATION, SUBUNIT, PTM,
SUBCELLULAR LOCATION); all 32 GOA-cited PMIDs cached via `just fetch-gene-pmids`; additionally
fetched PMID:10613902 (Kedersha 1999, stress granules). Context only: the integrated stress response module and GO-CAM review proposed in
ai4curation/ai-gene-review#5904. The EIF2S1 GO-CAM mistyping is cited directly from
gocams/66b5638000001589/66b5638000001589-src.yaml and gocams/66b5638000000624/66b5638000000624-src.yaml.

## Key findings
- eIF2 is a general initiation factor: [PMID:16289705 "eIF2 (eukaryotic translation initiation factor 2) and eIF2B augmented translation of capped, uncapped and encephalomyocarditis virus-internal ribosome entry site-promoted mRNAs."] whereas [PMID:16289705 "eIF4E specifically stimulated capped mRNA translation"].
- Ternary complex: [PMID:23063529 "Together with GTP and initiator methionyl-tRNA, translation initiation factor eIF2 forms a ternary complex that binds the 40S ribosome and then scans an mRNA to select the AUG start codon for protein synthesis."]
- Phospho-eIF2 inhibits eIF2B: [PMID:10613902 "Phosphorylation of eIF-2α increases the affinity of eIF-2 for eIF-2B, and prevents the exchange of GDP for GTP, thereby inhibiting the formation of preinitiation complexes."]
- Stress granules: [PMID:10613902 "A phosphomimetic eIF-2alpha mutant (S51D) induces the assembly of SGs, whereas a nonphosphorylatable eIF-2alpha mutant (S51A) prevents the assembly of SGs."]
- HRI/mitophagy: [PMID:38340717 "Activation of the HRI branch results in mitochondrial localization of phosphorylated eukaryotic initiation factor 2, which we show is sufficient to induce mitophagy."]; ER-marker check: [PMID:38340717 "Analysis of the subcellular fractions with an ER marker showed no evidence of ER enrichment of p-EIF2α upon DFP treatment (Figure S4C)."]

## GO-CAM term check (task question)
Yes: GOA carries GO:0160296 cap-dependent translation initiation factor activity (IDA, PMID:16289705,
assigned by UniProt, dated 2022-01-19 and 2024-08-19, deduplicated to one review row) and GO:0160297
IRES-mediated translation initiation factor activity (IDA, PMID:16289705, UniProt, 2024-08-19).
These mirror the GO-CAM typing. Both MODIFY to GO:0003743, with WRONG_TERM source_defects (resource UNIPROT).

## Decisions
- GO:0010998 (regulation of translational initiation by eIF2 alpha phosphorylation) not proposed:
  it is_a GO:0006468 protein phosphorylation, i.e. the kinases' process; GOA carries it only on EIF2AK4 in this repo.
- Protein-binding rows (25) removed per protein-binding policy.
- translational initiation rows MODIFY to cytoplasmic translational initiation (GO:0002183).
