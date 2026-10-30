# SIRT5: ProtNLM function-description review

**NPI (score 0): the deacylase activities are true of horse SIRT5 but not of this frameshifted F6S899 model, which lacks half of the zinc site and the C-terminal NAD-binding segments.**

Target: [F6S899](https://www.uniprot.org/uniprotkb/F6S899/entry), Equus caballus. The exact source is the frozen [ProtNLM API](https://rest.uniprot.org/uniprotkb/F6S899?annotation=protnlm) response dated 2026-09-08, retained in `projects/PROTNLM_EVALUATION/mammal-benchmark/predictions.jsonl.gz`.

## Original prediction

> NAD-dependent lysine demalonylase, desuccinylase and deglutarylase that specifically removes malonyl, succinyl and glutaryl groups on target proteins. Has weak NAD-dependent protein deacetylase activity; however this activity may not be physiologically relevant in vivo

## Atomic claims

### NAD-dependent lysine demalonylase

**NPI (0), DOMAIN_ARCHITECTURE_MISMATCH.** Human SIRT5 has this activity (PMID:22076378), and the full-length horse product of the same gene, A0A9L0T9B1, carries protein-malonyllysine demalonylase activity (GO:0036054) in GOA, so the claim is not novel at gene level. F6S899 is a defective model of that gene: its transcript skips a 124-nt coding exon, so the C-terminal third is translated out of frame. Of the four human zinc-ligand cysteines, Cys166 and Cys169 are retained but Cys207 and Cys212 map to tryptophans, and the human NAD(+)-binding segments at 249-251, 275-277 and 293 are altered or absent. The catalytic fold the activity depends on is therefore incomplete in the exact sequence scored.

### Lysine desuccinylase

**NPI (0), DOMAIN_ARCHITECTURE_MISMATCH.** A0A9L0T9B1 carries protein-succinyllysine desuccinylase activity (GO:0036055) in GOA. The substrate-selectivity residues Tyr102 and Arg105 and catalytic His158 are retained in F6S899 and place it in the SIRT5 family, but they do not compensate for the missing zinc-ribbon cysteines and C-terminal NAD-contact segments.

### Lysine deglutarylase

**NPI (0), DOMAIN_ARCHITECTURE_MISMATCH.** A0A9L0T9B1 carries protein-glutaryllysine deglutarylase activity (GO:0061697) in GOA. Human biochemical evidence establishes deglutarylation, but the activity requires the intact catalytic fold and cofactor site that F6S899 lacks.

### Weak NAD-dependent protein deacetylase activity

**NPI (0), DOMAIN_ARCHITECTURE_MISMATCH.** The statement is appropriate for characterized human SIRT5, and A0A9L0T9B1 carries NAD-dependent protein lysine deacetylase activity (GO:0034979) in GOA. The same NAD- and zinc-dependent fold is required, and F6S899 lacks it.

### Deacetylation may lack physiological relevance

**UNC (1).** This is a qualification of human enzymology rather than a claim about equine physiology. No horse experiment available here resolves the physiological significance of SIRT5 deacetylation.

## Evidence and limits

The defect is a gene-model problem, not a demonstrated equine pseudoenzyme: the same Ensembl gene also encodes A0A9L0T9B1 (88.1% identity to human SIRT5 across 310 residues) and A0A9L0T6A9, both of which retain all four zinc-ligand cysteines. F6S899 is 67.5% identical overall, and its identity to human falls to 10/30 and 7/40 residues in the 201-250 and 251-300 windows. The [gene-model comparison](SIRT5-bioinformatics/RESULTS-rereview.md) records the exon differences and the feature mapping for all three models. These scores apply to F6S899 only; the same paragraph would be CNN for A0A9L0T9B1. Horse-specific research is justified by equine SIRT5-expression literature (PMID:36361948), but expression alone would not validate enzyme activity.

The reproducible [paired sequence comparison](SIRT5-bioinformatics/RESULTS.md) records residue-level findings and sequence hashes. The [human UniProt source](../../human/SIRT5/SIRT5-uniprot.txt) distinguishes experimental supporting papers from inferred statements. ARBA assertions and generated review prose are not used as validating evidence.
