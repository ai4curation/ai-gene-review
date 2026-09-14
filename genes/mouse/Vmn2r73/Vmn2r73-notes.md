# Vmn2r73 (A0A3B2WCZ5): evidence and exact-input prediction review

The domain-containing name is supported, but the glutamate GPCR function paragraph assigns autonomous membrane signaling to a product lacking the required seven-transmembrane module.

## Input identity and functional boundary

A0A3B2WCZ5 is 496 residues, compared with the 851-residue Vmn2r73 reference D3Z7M3 linked to the same MGI gene. The first 429 residues are identical. A later 43-residue segment retains 41 identities, but the complete reference seven-transmembrane region is absent. Sparse matches in a global alignment of the alternative tail do not constitute a transmembrane module. The signal peptide and ligand-binding domain are retained.

## Biological evidence

- [PMID:30675062 — Structural insights into the activation of metabotropic glutamate receptors.](https://pubmed.ncbi.nlm.nih.gov/30675062/): Class C receptor signaling requires a seven-transmembrane module distinct from the extracellular ligand-binding region; the experimental study concerns mGlu5 rather than Vmn2r73.

> the GPCR-defining 7TM domain

- [PMID:9288755 — A novel family of putative pheromone receptors in mammals with a topographically organized and sexually dimorphic distribution.](https://pubmed.ncbi.nlm.nih.gov/9288755/): The founding rat V2R study identifies a receptor family related to, but distinct from, metabotropic glutamate receptors.

> genes encoding seven transmembrane receptors with sequence similarity with
> Ca2+-sensing and metabotropic glutamate receptors

## Exact non-GO claims

The complete emitted record is preserved in [Vmn2r73-protnlm-source.json](Vmn2r73-protnlm-source.json). Assessments below address the selected protein product; evidence on longer products is identified explicitly.

### Protein name

> Receptor ligand binding region domain-containing protein

CNN (CS 2). The wording identifies the retained receptor ligand-binding region without claiming that an intact GPCR or a particular ligand specificity is present. The exact sequence retains this annotated domain in the same-gene reference.

### Function

> G-protein coupled receptor for glutamate. Ligand binding causes a conformation change that triggers signaling via guanine nucleotide-binding proteins (G proteins) and modulates the activity of down-stream effectors. Signaling inhibits adenylate cyclase activity

NPI (CS 0). The compound claim requires an autonomous G-protein-coupled receptor, whereas the exact input lacks the seven-transmembrane signaling module. The extracellular class C fold also does not establish glutamate specificity or inhibition of adenylate cyclase. The emitted donor accession is Q14833; it does not substitute for domain completeness in the target. [Sequence analysis](Vmn2r73-bioinformatics/RESULTS.md); [class C signaling study](https://pubmed.ncbi.nlm.nih.gov/30675062/).

No GO or EC term was emitted in this record; the name, function and location assessments above constitute its prediction review.

## Family integration

V2R family membership and retention of its ligand-binding region are separable from an intact class C receptor architecture. A partial gene product can preserve family identity while losing the domain needed for the ancestral activity. Neither the V2R designation nor similarity to glutamate receptors establishes the ligand of this particular product.

## Evidence limits

No assay or localization study of the exact 496-residue product was found. The genuine Falcon report describes conventional seven-transmembrane receptor biology but does not account for this input sequence boundary; its full-length signaling conclusions cannot be transferred. The 1997 V2R publication is abstract-only in the cache. Stable expression and any accessory role of the shortened product remain unresolved.

Exact sequence mapping: [Vmn2r73-bioinformatics/RESULTS.md](Vmn2r73-bioinformatics/RESULTS.md). Global alignments can place nonhomologous alternative tails opposite gaps or distant residues; only conserved segments and explicitly retained feature intervals support functional transfer.
