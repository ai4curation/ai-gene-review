# DAM manual review notes

## 2026-05-21 deeper SPKW-BPT4 review

Reviewed the AIGR review skill, `DAM-ai-review.yaml`, `DAM-goa.tsv`, `DAM-uniprot.txt`, `DAM-deep-research-falcon.md`, and cached publications `PMID_2510127.md`, `PMID_7782299.md`, `PMID_12937411.md`, and `PMID_15882618.md`.

Core function is DNA adenine methyltransferase activity at `GATC` sites. The direct biochemical support is strong: [PMID:7782299 Phage T4 DNA [N6-adenine]methyltransferase. Overexpression, purification, and characterization., "T4 Dam methylates the palindromic tetranucleotide, GATC"] and [PMID:2510127 Single amino acid changes that alter the DNA sequence specificity of the DNA-[N6-adenine] methyltransferase (Dam) of bacteriophage T4., "recognizes primarily the sequence GATC in both cytosine- and hydroxymethylcytosine-containing DNA"].

The SPKW immune/defense rows are better treated as replacement cases rather than as a blanket claim that bacteria lack all defense biology. The supported mechanism is phage restriction-modification evasion by DNA methylation, not generic suppression of host innate immune response. The specific replacement target is already in GOA: `GO:0099018 symbiont-mediated evasion of host restriction-modification system`.

The UniProt flatfile also contains `GO:1904047 S-adenosyl-L-methionine binding` and `GO:0006298 mismatch repair`, but these are absent from the fetched `DAM-goa.tsv`, so they were not added to `existing_annotations` in this YAML pass. If those enter GOA later, SAM binding would be non-core at most; mismatch repair would need careful review because T4 Dam is a DNA modification/antirestriction enzyme, not a canonical mismatch-repair factor in this review.
