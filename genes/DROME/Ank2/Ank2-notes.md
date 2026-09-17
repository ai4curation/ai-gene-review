# Ank2 / Q3KN55: short-isoform review

## Finding

**Q3KN55 is the genuine annotated short Ank2-PE polypeptide (697 aa), not the giant neuronal Ank2 proteins investigated in the classic synaptic-stability papers.** The ProtNLM toxin prediction is a particularly informative error: its own evidence metadata point to a black-widow latrotoxin. Ankyrin-repeat similarity does not establish the membrane-insertion mechanism or evolved toxic activity of that donor. Exocytosis and extracellular localization remain uncertain for the exact short fly product.

This distinction also matters for GOA. The experimental Ank2 annotations are biologically well grounded at the gene/giant-isoform level. They must not all be treated as direct measurements of the 697-residue protein, nor should uncertainty about the short product be presented as evidence that FlyBase curators chose the wrong gene.

## Identity and source provenance

- [UniProt Q3KN55](https://www.uniprot.org/uniprotkb/Q3KN55/entry): unreviewed RE55168p; 697 aa; sequence version 1 since 2005. Sequence and feature evidence come from the submitted cDNA and PROSITE repeat calls, respectively. ARBA keywords are not used to validate a function.
- [FlyBase Ank2-PE, FBpp0292239](https://flybase.org/reports/FBpp0292239.html): explicitly assigns the same 697-aa product to `CG42734-PE`, transcript `Ank2-RE` / `FBtr0303120`, and links Q3KN55.
- [RefSeq NP_001097534.1](https://www.ncbi.nlm.nih.gov/protein/NP_001097534.1): identifies ankyrin 2 isoform E. This is the same accession cross-referenced by UniProt and FlyBase.
- [FlyBase Ank2 gene](https://flybase.org/reports/FBgn0261788.html) encodes many different products. The short PE product must not be silently replaced with Ank2-PF, Ank2-PU or other giant isoforms.

The downloaded FlyBase HTML and its plain-text extraction are stored as `Ank2-PE-flybase-source.html` and `Ank2-PE-flybase-source.txt`. The sequence in the HTML `<pre>` element, after whitespace removal, is identical to the frozen UniProt sequence: both are 697 aa, SHA-256 `14c9804138cf7636dd66509229d4921bf19b0adc81c88d72706f81fba388ea7f`. This is a source identity check, not a claim of experimental characterization of every annotated isoform. The current sequence is not independently proven to be the exact sequence supplied to ProtNLM at prediction time.

UniProt records a low-complexity/disordered N terminus and PROSITE ankyrin-repeat features between residues 193 and 650. It records neither a spectrin-binding region nor the extensive microtubule-organizing tail of giant Ank2. The broad PANTHER family name includes “protein kinase”; that label is not evidence that this protein has a kinase domain or activity.

## Experimental evidence and the scope of GO annotations

### Giant Ank2 and the membrane/microtubule scaffold

[PMID:18439405](https://pubmed.ncbi.nlm.nih.gov/18439405/), Pielage et al., *Neuron* (2008), [DOI:10.1016/j.neuron.2008.02.017](https://doi.org/10.1016/j.neuron.2008.02.017), directly identifies Ank2-L and states: “The stabilizing functions of Ank2-L can be mapped to the extended C-terminal domain”. Its microtubule-binding and synapse-stabilizing results therefore require an architecture that PE does not contain. The cached record is abstract-only. PMC HTML was additionally attempted but returned a browser-check page; no full-text access is claimed.

[PMID:18439406](https://pubmed.ncbi.nlm.nih.gov/18439406/), Koch et al., *Neuron* (2008), [DOI:10.1016/j.neuron.2008.03.019](https://doi.org/10.1016/j.neuron.2008.03.019), reports “two giant Ank2 isoforms” and their association with the presynaptic membrane cytoskeleton. The paper supports synaptic stability and microtubule organization at the Ank2 locus, but the accessible abstract does not establish localization or activity of PE. Its cache is also abstract-only. No assertion is made that the full paper never assays a shorter product.

The corresponding microtubule, NMJ-development and fine presynaptic-location GOA rows are individually assessed with these scope limitations. Their UNDECIDED actions concern transfer to Q3KN55, not a claim that the primary experiments or gene-level annotations are false.

### Degeneration and neurotransmission

[PMID:22153373](https://pubmed.ncbi.nlm.nih.gov/22153373/), *Glial-derived prodegenerative signaling in the Drosophila neuromuscular system*, is available in the publication cache with full text. The study actually tests ank2 mutants, including the `ank2^2001` background from the giant-Ank2 work. It demonstrates severe synaptic degeneration, genetic suppression by eiger loss, and improved evoked responses in double mutants. These results support an Ank2 gene-level neuronal-homeostasis role, while leaving the PE contribution unresolved.

The negative-regulation GO annotation deserves a separate directionality check. The paper states “loss of ank2 results in impaired average EPSP amplitudes”; that observation supports maintaining transmission, not by itself an evolved inhibitory role. The present action is UNDECIDED, since the whole genetic interpretation should be reconciled with the GOA assertion before removal or a replacement. This is distinct from claiming that intracellular Ank2 cannot participate in exocytosis: a structural or regulatory protein can participate without catalyzing membrane fusion.

### Other experiments

- [PMID:16920632](https://pubmed.ncbi.nlm.nih.gov/16920632/), [DOI:10.1016/j.cub.2006.06.061](https://doi.org/10.1016/j.cub.2006.06.061): the accessible abstract describes an intracellular Nrg–Ank adaptor mechanism and axonal sprouting. It does not resolve the experimental construct and short-isoform contribution. Do not infer wrong-paralog attribution from the abbreviated name.
- [PMID:19317464](https://pubmed.ncbi.nlm.nih.gov/19317464/), [DOI:10.1021/pr800866n](https://doi.org/10.1021/pr800866n): LOPIT proteomics in Drosophila embryos underlies the plasma-membrane HDA annotation. Isoform-discriminating peptides and protein-group assignments are not available in the cached abstract. The HDA assertion itself is a legitimate experimental localization claim.
- [PMID:22939627](https://pubmed.ncbi.nlm.nih.gov/22939627/), [DOI:10.1016/j.cell.2012.06.043](https://doi.org/10.1016/j.cell.2012.06.043): auditory-organ functional screen. Its abstract does not expose the Ank2 allele or isoform details; no negative inference follows from this omission.
- [PMID:23390136](https://pubmed.ncbi.nlm.nih.gov/23390136/), [DOI:10.1093/hmg/ddt043](https://doi.org/10.1093/hmg/ddt043): despite the human ANK3 title, the abstract explicitly reports a Drosophila knockdown model with memory defects. This is not grounds for a human/fly name-conflation allegation. The short-product contribution and synapse-assembly assay remain unverified from the abstract.
- [PMID:37061542](https://pubmed.ncbi.nlm.nih.gov/37061542/), *Next-generation large-scale binary protein interaction network for Drosophila melanogaster*: full-text cache available. The GOA IPI row and the exact Q3KN55 IntAct record identify Tramtrack/P17789 binding (four experiments). Retain that measured interaction as non-core. The main article does not identify the exact Ank2 ORF; an interaction alone does not establish a transcriptional, synaptic or toxic function.

No specific core molecular function is assigned to PE from these incomplete data. This does not erase the well-established structural functions of giant Ank2 proteins.

## ProtNLM claim tracing

The complete original API object is preserved in `Ank2-protnlm-source.json`, including the original predicted name, subcellular-location comment, model scores, phmmer donors and scores. The sidecar reviews all three GO claims. This record carries no prediction timestamp that can be used reliably; the placeholder `1111-11-10` date is preserved as source metadata rather than interpreted as real chronology.

| GO claim | Model score | phmmer donor | phmmer score | Assessment |
|---|---:|---|---:|---|
| toxin activity (GO:0090729) | 0.49 | Q9XZC0 | 293.2 | NPI |
| exocytosis (GO:0006887) | 0.53 | P16157 | 889.4 | UNC |
| extracellular region (GO:0005576) | 0.54 | Q9XZC0 | 293.2 | UNC |

[Q9XZC0](https://www.uniprot.org/uniprotkb/Q9XZC0/entry) is alpha-latrocrustotoxin-Lt1a from a black widow spider. Its experimentally investigated mechanism is documented in [PMID:34845192](https://pubmed.ncbi.nlm.nih.gov/34845192/), Chen et al., *Molecular architecture of black widow spider neurotoxins*, [DOI:10.1038/s41467-021-26562-8](https://doi.org/10.1038/s41467-021-26562-8). Full text is cached. The structural study resolves a central membrane-insertion domain in addition to ankyrin-like repeats. Sharing repeat motifs with a cellular ankyrin is not sufficient to transfer this evolved toxic activity. The metadata implicate an inappropriate donor, but do not prove the model's internal causal reasoning or a recent paralog relationship.

[P16157](https://www.uniprot.org/uniprotkb/P16157/entry) is human ankyrin-1, a different donor used for the exocytosis claim. Its record has an NAS exocytosis annotation. That annotation is comparison provenance, not independent biological proof for PE. The toxin, exocytosis and extracellular claims must not be described as a single identical-donor event.

Extracellular localization is biologically disfavored by cellular Ank2 context, but remains UNC because the short product has unresolved direct localization. Missing signal-peptide annotation is not alone a complete secretion prediction. This is a deliberately different evidential threshold from the positive mismatch between the toxin-specific multidomain mechanism and the target's cellular ankyrin identity.

GO definitions were fetched from [QuickGO](https://www.ebi.ac.uk/QuickGO/) on 2026-09-08 and saved as three `GO_*-quickgo.json` records. Toxin activity is an evolved activity against another organism; exocytosis is the vesicular secretion process; extracellular region is outside the cell boundary, distinct from the cytoplasmic face of a presynaptic membrane.

## Additional domain evidence and research synthesis

[PMID:31475145](https://pubmed.ncbi.nlm.nih.gov/31475145/), Weber et al. (2019), [DOI:10.3389/fcell.2019.00148](https://doi.org/10.3389/fcell.2019.00148), is cached with full text. Its deletion/rescue experiments show that particular ankyrin-repeat subdomains determine synaptic targeting of the giant proteins. Thus, the retained repeat module supports an intracellular interaction/scaffold context, but does not make every fine presynaptic location transferable automatically. The broad plasma-membrane HDA observation is retained as compatible with this context; the detailed giant-isoform localization claims remain unresolved for PE.

The Falcon literature research completed on 2026-09-08 and is stored unedited as `Ank2-deep-research-falcon.md`, with its evidence-summary artifact. It appropriately distinguishes locus-level evidence from accession-specific function and highlights the 2019 domain-targeting work. Its canonical 24-repeat/spectrin-binding architecture is a description of the large proteins, not of the 697-residue input; the FlyBase sequence reconciliation above supplies that distinction. The synthesis is useful for evaluating domain dependence and locating sources, while the per-annotation excerpts point to the primary papers or exact source records.
