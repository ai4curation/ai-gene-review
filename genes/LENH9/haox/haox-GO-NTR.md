# GO New Term Request: L-lactate oxidase activity

## Requested Term Details

**Preferred term label:** L-lactate oxidase activity

**Synonyms:**
- lactate oxidase activity
- LOX activity
- L-lactate:oxygen oxidoreductase activity

**Definition:** Catalysis of the reaction: (S)-lactate + O2 = pyruvate + H2O2.

**Parent term:** GO:0003973 ((S)-2-hydroxy-acid oxidase activity)
- This parent relationship is consistent with RHEA's hierarchy, where RHEA:55868 is a child of RHEA:16789 (a (2S)-2-hydroxycarboxylate + O2 = a 2-oxocarboxylate + H2O2), which corresponds to the general (S)-2-hydroxy-acid oxidase activity

**Ontology branch:** molecular_function

## Mappings

- **EC Number:** EC:1.1.3.2 (skos:exactMatch)
- **RHEA:** RHEA:55868 (skos:exactMatch)
- **MetaCyc:** LACTATE-2-MONOOXYGENASE-RXN (skos:exactMatch - note the misleading name)
- **KEGG Reaction:** R00319 (skos:exactMatch)

**Note on mapping consistency:** The MetaCyc entry LACTATE-2-MONOOXYGENASE-RXN lists KEGG R00319 as its corresponding reaction, confirming the mapping consistency across databases despite the confusing MetaCyc identifier name.

**Note to RHEA curators:** The RHEA:55868 entry currently lacks a KEGG cross-reference. Consider adding R00319 as the corresponding KEGG reaction to improve database interoperability.

## Justification

### Gap in Current GO Annotation

The Gene Ontology currently lacks a specific term for L-lactate oxidase activity (EC 1.1.3.2), despite this being a well-characterized enzyme class that is biochemically and functionally distinct from related activities. This creates an annotation gap where curators must use the overly general term GO:0003973 ((S)-2-hydroxy-acid oxidase activity) to describe this specific enzymatic function.

### Biochemical Distinctiveness

L-lactate oxidase represents a specific enzymatic activity with unique characteristics:

1. **Substrate specificity:** Strict specificity for (S)-lactate (L-lactate)
2. **Electron acceptor:** Uses molecular oxygen (O2) as the terminal electron acceptor, producing H2O2
3. **Cofactor requirement:** FMN-dependent oxidation mechanism
4. **Reaction mechanism:** Operates via flavin-mediated α-hydroxyacid oxidation with carbanion intermediate formation

This is fundamentally different from:
- **L-lactate dehydrogenase (GO:0140171):** Uses NAD+ as electron acceptor, not O2
- **Lactate 2-monooxygenase (GO:0050040):** Produces acetate + CO2 + H2O, not pyruvate + H2O2

### Historical Classification Confusion

The classification of L-lactate oxidase has a complex history that highlights the need for clear ontological terms:

**Timeline of EC number changes:**
- **1961:** EC 1.1.3.2 created for L-lactate oxidase
- **1972:** EC 1.1.3.2 transferred to EC 1.13.12.4, conflating two distinct activities
- **2018:** EC 1.1.3.2 reinstated as a separate enzyme class

**Current status (as of 2025):**
- **ExplorEnz (IUBMB):** Correctly shows EC 1.1.3.2 as active for L-lactate oxidase (reaction: (S)-lactate + O2 = pyruvate + H2O2)
- **ExPASy ENZYME:** Still shows EC 1.1.3.2 as "Transferred to EC 1.13.12.4" (appears to be at least 7 years out of date)
- **MetaCyc:** Uses the confusing identifier "LACTATE-2-MONOOXYGENASE-RXN" for the oxidase reaction, likely a remnant from the 1972-2018 period when these were considered the same enzyme

This historical confusion arose because both enzymes:
1. Use L-lactate as substrate
2. Use O2 as electron acceptor
3. Are found in similar organisms

However, they are biochemically distinct:
- **L-lactate oxidase (EC 1.1.3.2):** L-lactate + O2 → pyruvate + H2O2 (simple oxidation)
- **Lactate 2-monooxygenase (EC 1.13.12.4):** L-lactate + O2 → acetate + CO2 + H2O (oxidative decarboxylation)

The persistence of outdated classifications in major databases (ExPASy) and confusing nomenclature (MetaCyc) demonstrates the urgent need for clear, distinct GO terms to prevent continued misannotation.

### Precedent in GO

GO already contains specific terms for many other L-amino acid and L-hydroxy acid oxidases:
- GO:0008734 (L-aspartate oxidase activity)
- GO:0050025 (L-glutamate oxidase activity)
- GO:0050029 (L-lysine oxidase activity)
- GO:0050024 (L-galactonolactone oxidase activity)
- GO:0050035 (L-sorbose oxidase activity)

The absence of L-lactate oxidase activity is inconsistent with this established pattern.

## Supporting Evidence

### Published Literature

**PMID:34555022** - Rembeza E, Engqvist MKM. (2021) "Experimental and computational investigation of enzyme functional annotations uncovers misannotation in the EC 1.1.3.15 enzyme class." PLoS Comput Biol.
- Experimentally validated L-lactate oxidase activity (EC 1.1.3.2) as a distinct enzyme class
- Demonstrated that at least 78% of sequences in related enzyme classes are misannotated
- Highlights the need for precise functional annotation terms

**PMID:8589073** - Lederer F. (1996) "L-lactate oxidase and L-lactate monooxygenase: mechanistic variations on a common structural theme." Biochimie.
- Detailed mechanistic studies showing the unique catalytic mechanism of L-lactate oxidase
- Demonstrates the flavin-mediated oxidation with H2O2 production

**PMC:5648907** - Zaunmüller T, et al. (2017) "Oxygen-Inducible Conversion of Lactate to Acetate in Heterofermentative Lactobacillus brevis"
- Shows the metabolic role of L-lactate oxidase in bacterial lactate catabolism
- Demonstrates the enzyme's role in aerobic energy metabolism

### Organisms with Characterized L-lactate Oxidases

L-lactate oxidases have been characterized in numerous organisms:
- *Lentilactobacillus hilgardii* (UniProt: C0XIJ3)
- *Aerococcus viridans* (UniProt: Q44467)
- *Mycobacterium smegmatis* (UniProt: O33655)
- *Lactobacillus plantarum*
- *Pediococcus* species

The enzyme is found across 161+ bacterial genera, indicating widespread distribution and functional importance.

## Proposed Annotation Guidelines

### When to use this term:
- Enzymes that specifically oxidize L-lactate to pyruvate using O2 as electron acceptor
- FMN-dependent lactate oxidases producing H2O2
- Proteins with demonstrated EC 1.1.3.2 activity

### When NOT to use this term:
- NAD+-dependent lactate dehydrogenases (use GO:0140171)
- Lactate monooxygenases producing acetate (use GO:0050040)
- D-lactate oxidases (would need a separate term)

## Quality Control

This new term would improve annotation quality by:
1. Reducing over-annotation with the general (S)-2-hydroxy-acid oxidase term
2. Enabling precise functional annotation consistent with biochemical evidence
3. Facilitating accurate metabolic pathway reconstruction
4. Supporting comparative genomics studies of lactate metabolism

## Annotation Strategy

### Automated Annotation Propagation

The proposed term includes an exact mapping (skos:exactMatch) to RHEA:55868, which will enable automatic propagation of annotations to existing proteins:

- **Current RHEA annotations:** 2,065 UniProtKB entries are currently annotated with RHEA:55868
- **Immediate impact:** Upon creation of this GO term, these 2,065 proteins would be eligible for GO annotation with "L-lactate oxidase activity"
- **Annotation evidence:** These would receive IEA (Inferred from Electronic Annotation) evidence codes based on the RHEA-to-GO mapping

### Annotation Pipeline

1. **Automatic propagation via RHEA mapping:**
   - All proteins with RHEA:55868 annotation → GO:XXXXXXX (L-lactate oxidase activity) with IEA evidence
   - This ensures immediate broad coverage across bacterial species

2. **EC number mapping:**
   - Proteins annotated with EC 1.1.3.2 can be mapped to this term
   - Care must be taken to verify these are the oxidase (not transferred to monooxygenase)

3. **Manual curation priorities:**
   - Well-characterized enzymes (e.g., Aerococcus viridans, Mycobacterium smegmatis)
   - Enzymes with experimental validation (IDA, IMP evidence)
   - Industrially relevant species (dairy, fermentation organisms)

4. **Quality control:**
   - Review existing annotations using GO:0003973 to identify candidates for more specific annotation
   - Check for proteins incorrectly annotated with GO:0050040 (lactate 2-monooxygenase) that should be re-annotated

### Expected Annotation Coverage

Based on the RHEA mapping alone, this new term would immediately provide precise functional annotation for over 2,000 bacterial proteins across diverse species including:
- Lactic acid bacteria (Lactobacillus, Pediococcus, Leuconostoc)
- Pathogenic bacteria (Streptococcus, Mycobacterium)
- Industrial fermentation organisms
- Human microbiome species

This represents a significant improvement in annotation specificity for a metabolically important enzyme class.

## Term Submitter

This term request was created by an AI agent operated by @cmungall (ORCID 0000-0002-6601-2165).
It was checked for correctness and completeness by @cmungall

## Additional Notes

This term request is based on comprehensive curation of the haox gene (UniProt: C0XIJ3) in *Lentilactobacillus hilgardii* as part of the AI-assisted gene curation project. The mechanistic details and metabolic context have been thoroughly reviewed using both literature analysis and bioinformatic investigation.

For further details, see https://github.com/ai4curation/ai-gene-review/tree/main/genes/LENH9/haox

The proposed term fills a clear gap in GO's coverage of oxidoreductase activities and would benefit the annotation of bacterial metabolic enzymes across numerous species involved in fermentation, dairy production, and the human microbiome.

---

*This new term request was generated as part of the [ai-gene-review project](https://github.com/ai4curation/ai-gene-review/) for systematic improvement of GO annotations.*