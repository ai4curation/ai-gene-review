# SIRT5: ProtNLM function-description review

**Finding: Unresolved for this exact horse sequence despite a well-supported human SIRT5 mechanism.**

Target: [F6S899](https://www.uniprot.org/uniprotkb/F6S899/entry), Equus caballus. The exact source is the frozen [ProtNLM API](https://rest.uniprot.org/uniprotkb/F6S899?annotation=protnlm) response dated 2026-09-08, retained in `projects/PROTNLM_EVALUATION/mammal-benchmark/predictions.jsonl.gz`.

## Original prediction

> NAD-dependent lysine demalonylase, desuccinylase and deglutarylase that specifically removes malonyl, succinyl and glutaryl groups on target proteins. Has weak NAD-dependent protein deacetylase activity; however this activity may not be physiologically relevant in vivo

## Atomic claims

### NAD-dependent lysine demalonylase

**Uncertain.** Human SIRT5 has this activity, but the selected horse sequence diverges sharply after roughly residue 200 and lacks multiple human NAD-contact segments. Two conserved zinc-coordinating cysteines map to tryptophans.

### Lysine desuccinylase

**Uncertain.** The retained substrate-selectivity residues Tyr102 and Arg105 and catalytic His158 support SIRT5-family identity. They do not compensate for the unresolved zinc-binding and C-terminal-fold defects.

### Lysine deglutarylase

**Uncertain.** Human biochemical evidence establishes deglutarylation, but functional transfer requires an intact catalytic fold and cofactor site; this exact horse sequence fails a straightforward conservation check.

### Weak NAD-dependent protein deacetylase activity

**Uncertain.** The statement is appropriate for characterized human SIRT5, but activity measurements cannot be assigned to this divergent horse protein model.

### Deacetylation may lack physiological relevance

**Not established for horse.** This is a qualification of human enzymology rather than direct evidence about equine physiology. No horse experiment available here resolves the catalytic activity or its physiological significance.

## Evidence and limits

The comparison points to a possible protein-model problem, not a demonstrated equine pseudoenzyme. The current accession sequence may not be identical to the sequence originally supplied to ProtNLM. Establishing a corrected transcript/protein model and testing its zinc/NAD-binding fold are necessary before deciding whether this is a prediction failure. Horse-specific research is justified by equine SIRT5-expression literature (PMID:36361948), but expression alone would not validate enzyme activity.

The reproducible [paired sequence comparison](SIRT5-bioinformatics/RESULTS.md) records residue-level findings and sequence hashes. The [human UniProt source](../../human/SIRT5/SIRT5-uniprot.txt) distinguishes experimental supporting papers from inferred statements. ARBA assertions and generated review prose are not used as validating evidence.
