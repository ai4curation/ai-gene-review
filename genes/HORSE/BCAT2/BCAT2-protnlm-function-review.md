# BCAT2: ProtNLM function-description review

**Finding: Supported conserved catalytic function; mitochondrial targeting is not assessed by this claim.**

Target: [A0A9L0TSN4](https://www.uniprot.org/uniprotkb/A0A9L0TSN4/entry), Equus caballus. The exact source is the frozen [ProtNLM API](https://rest.uniprot.org/uniprotkb/A0A9L0TSN4?annotation=protnlm) response dated 2026-09-08, retained in `projects/PROTNLM_EVALUATION/mammal-benchmark/predictions.jsonl.gz`.

## Original prediction

> Catalyzes the first reaction in the catabolism of the essential branched chain amino acids leucine, isoleucine, and valine

## Atomic claims

### First step in branched-chain amino acid catabolism

**Supported.** Human mitochondrial BCAT2 structural and kinetic work establishes transamination of branched-chain substrates (PMID:17050531). The horse protein aligns across the full human enzyme and preserves the mapped substrate-contact residues. The extra 60-residue N-terminal segment does not remove that catalytic domain.

### Leucine, isoleucine and valine are substrates

**Supported.** The experimentally characterized human enzyme has the substrate spectrum given in the prediction. Its human UniProt functional statement is grounded in biochemical papers, including PMID:17050531 and PMID:25653144; mapped contacts and broad sequence conservation support transfer to this horse enzyme.

## Evidence and limits

The statement is a plausible conserved mammalian enzyme function, not an equine-specific experimental observation. The selected model has a long N-terminal extension; this analysis does not certify mitochondrial targeting. The narrative adds a substrate-level description to target GOA branched-chain amino acid catabolism; training membership is unknown.

The reproducible [paired sequence comparison](BCAT2-bioinformatics/RESULTS.md) records residue-level findings and sequence hashes. The [human UniProt source](../../human/BCAT2/BCAT2-uniprot.txt) distinguishes experimental supporting papers from inferred statements. ARBA assertions and generated review prose are not used as validating evidence.
