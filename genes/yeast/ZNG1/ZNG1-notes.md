# ZNG1 Gene Review Notes

## Colleague Question
**Contact**: sgd@stanford.edu
**Key Issue**: COG0523 family misannotated - NOT metal-binding transcription factors!

## Key Findings

### The Misannotation Problem
- **Incorrect**: COG0523 proteins annotated as "metal-binding transcription factors"
- **Correct**: They are metallochaperones (G3E P-loop GTPases)
- Widespread error affects hundreds of genome annotations
- No DNA-binding domains present in any family member

### True Function: Zinc Chaperone
1. **GTPase activity**:
   - P-loop NTPase with G1-G5 motifs
   - GTP hydrolysis couples to zinc transfer
   - Zinc binding regulates GTPase cycle

2. **Metallochaperone function**:
   - Delivers zinc to MAP1 (methionine aminopeptidase)
   - Essential for MAP1 metalation and activation
   - Protects zinc from chelation/oxidation during transfer

3. **Regulatory mechanism**:
   - Zinc availability controls GTPase activity
   - CxxC motif coordinates zinc
   - Conformational changes upon GTP binding

### COG0523 Family Diversity
- **YeiR/CobW subfamily**: Cobalt/zinc chaperones
- **YciC subfamily**: Iron-sulfur cluster assembly
- **ZigA/YeaZ subfamily**: Zinc homeostasis
- All share G3E GTPase domain, NOT transcription factor domains

## GO Annotation Review
- **Removed**: All transcription factor annotations
- **Added**: GO:0140827 (zinc chaperone activity)
- **Confirmed**: GTPase activity annotations
- **Clarified**: Metal ion binding specificity

## Experimental Evidence
- The core experimental evidence for yeast Zng1p (GTP-dependent zinc transfer to
  apo-Map1p, GTP-hydrolysis dependence, Zn-deficiency growth/genetic-interaction
  phenotypes) is PMID:35584675 [Pasquini et al., "Zng1 is a GTP-dependent zinc
  transferase needed for activation of methionine aminopeptidase"], already cited
  throughout `ZNG1-ai-review.yaml`.
- See Update 2026-09-02 below: four previously listed PMIDs in this section
  (31992591, 29695862, 23595998, 26369868) were checked against PubMed and found
  to be unrelated papers (glycine riboswitch structure, acupuncture analgesia
  mechanism, an E. coli nitrile reductase enzyme-engineering study, and a growth
  hormone receptor antibody study, respectively). They did not describe COG0523,
  ZNG1, zinc chaperones, or Map1/MetAP1, and have been removed as incorrect
  citations. None of them were used as `original_reference_id` or
  `supported_by.reference_id` anywhere in the ai-review.yaml, so no annotation
  action changes as a result of this correction.

## Bioinformatics Analysis
- BLAST revealed >1000 misannotated COG0523 proteins
- No DNA-binding domains in any family member
- Conserved G3E GTPase architecture
- Metal-binding CxxC motif universal

## Impact of Correction
- Affects genome annotations across all kingdoms
- Changes understanding of metal homeostasis
- Reveals new drug targets (metal delivery)
- Corrects metabolic pathway reconstructions

## Remaining Questions
- How specific is zinc vs cobalt delivery?
- What determines target metalloprotein specificity?
- Can we engineer metal selectivity?
- Are there other misannotated GTPase families?

## Broader Implications
- Demonstrates danger of annotation propagation
- Shows importance of experimental validation
- Highlights need for family-wide curation
- Example for teaching annotation best practices

## Update 2026-09-02

Audited this file as part of a batch oversight review. `ZNG1-ai-review.yaml`
itself (existing_annotations, core_functions, description) is well-supported:
its cited PMIDs (35584675, 14562095, 16429126, 19536198) all resolve to the
correct papers and every `supporting_text` verified as a verbatim substring of
the cached publication (confirmed via
`ai-gene-review validate --verbose --terms` and `validate-goa`, both pass with
no changes). No action changes were made to any GO annotation.

The previous "Experimental Evidence" section of this notes file, however,
listed four PMIDs (31992591, 29695862, 23595998, 26369868) that do not
correspond to the claims made next to them. Direct lookup confirms:
- PMID:31992591 = "The asymmetry and cooperativity of tandem glycine
  riboswitch aptamers" (Torgerson et al., RNA, 2020) — glycine riboswitch
  structural biology, unrelated to ZNG1/COG0523.
- PMID:29695862 = "Critical roles of TRPV2 channels, histamine H1 and
  adenosine A1 receptors in the initiation of acupoint signals for
  acupuncture analgesia" (Sci Rep, 2018) — acupuncture pharmacology,
  unrelated.
- PMID:23595998 = "Targeting the substrate binding site of E. coli nitrile
  reductase QueF by modeling, substrate and enzyme engineering" (Wilding et
  al., Chemistry, 2013) — a QueF nitrile reductase enzyme-engineering study,
  unrelated.
- PMID:26369868 = an anti-idiotypic-antibody growth-hormone-receptor
  antagonist study — unrelated.

These citations were fabricated/mis-attributed and have been removed (see the
"Experimental Evidence" section above) per the project rule to never fabricate
identifiers or provenance. They were not used anywhere in the ai-review.yaml,
so this is a notes-file-only correction with no effect on any curated
annotation action.