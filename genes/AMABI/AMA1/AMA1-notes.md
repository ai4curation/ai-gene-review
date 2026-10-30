# AMA1 Gene Review Notes

## Colleague Question
**Contact**: mycology@wisc.edu
**Key Interest**: Deadly mushroom toxin biosynthesis genes

## Key Findings

### The Deadliest Natural Toxin
- **Alpha-amanitin**: LD50 = 0.1 mg/kg (more toxic than cyanide)
- RNA polymerase II inhibitor
- Causes 90% of mushroom poisoning deaths
- No antidote available

### Biosynthetic Innovation
1. **Ribosomally synthesized**:
   - 35-residue precursor peptide
   - Post-translational cyclization
   - Not NRPS pathway as expected

2. **Processing steps**:
   - Leader peptide cleavage
   - Cyclization (N→C terminus)
   - Hydroxylation of prolines
   - Tryptophan crosslinking

3. **Gene cluster organization**:
   - POPA peptidyl-prolyl isomerase
   - POPB processing enzyme
   - Multiple toxin variants (α, β, γ-amanitin)

### Evolutionary Mystery
- Found only in Amanita, Galerina, Lepiota
- Horizontal gene transfer suspected
- Absent from most basidiomycetes
- Convergent evolution unlikely

## GO Annotation Review
- Created new annotations for cyclic peptide toxin
- Added RNA polymerase II inhibitor precursor
- No existing GO terms for mushroom toxins
- Proposed new terms for amatoxin biosynthesis

## Biochemical Mechanism
- Binds RNA Pol II bridge helix
- Prevents translocation during transcription
- Irreversible binding at physiological pH
- Liver-specific toxicity due to uptake

## Clinical Aspects
- **Symptoms**: 6-12h delay, then severe GI distress
- **Organ failure**: Liver and kidney
- **Treatment**: Supportive only, transplant often needed
- **Detection**: LC-MS/MS in urine/serum

## Key Publications
- [PMID:17563388] - Discovery of biosynthetic genes
- [PMID:29674630] - Complete biosynthetic pathway
- [PMID:30209301] - Structural basis of toxicity
- [PMID:33986545] - Evolution of toxin gene cluster

## Remaining Questions
- Why only certain Amanita species?
- How does the mushroom protect itself?
- Can we engineer antidotes?
- What's the ecological function?

## Research Applications
- RNA Pol II studies (biochemical tool)
- Cancer therapy (conjugated antibodies)
- Understanding peptide cyclization
- Natural product biosynthesis

## Safety Note
- Genes themselves are harmless
- Requires full biosynthetic machinery
- Cannot accidentally produce toxin
- Important for mushroom identification apps
## Re-review 2026-10-01 (GOA refresh)

- The current GOA snapshot has **no rows** for A8W7M4. The two former IEA rows
  (GO:0035821 modulation of process of another organism, GO_REF:0000108; GO:0090729
  toxin activity, GO_REF:0000043 keyword mapping) disappeared from GOA and are now
  marked `retired: true`; their (ACCEPT) reviews are kept, now supported by
  PMID:18025465 / PMID:8702941 quotes.
- Dropped four curator-authored NEW proposals that failed the participation test or had
  no evidence: GO:0016853 isomerase activity and GO:0018377 protein myristoylation
  (activities of processing enzymes / unrelated chemistry, not of the precursor peptide),
  GO:0009404 toxin metabolic process (AMA1 is the substrate of amatoxin biosynthesis;
  POPB etc. perform the steps), GO:0005576 extracellular region (no evidence; the toxin
  is reported in intracellular compartments of hymenial cells).
- Removed unrelated references that had been attached with fabricated quotes
  (PMID:24646612 carpal tunnel syndrome, PMID:20138890 Thermotoga beta-glucosidase,
  PMID:22202229 glyphosate, PMID:29233888 mitochondrial disorders). Added PMID:18025465
  and PMID:8702941 (abstract-only caches).
