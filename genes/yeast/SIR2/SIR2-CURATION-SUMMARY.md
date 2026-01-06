# SIR2 GO Annotation Curation Review

## Gene Summary
Yeast SIR2 (NAD-dependent histone deacetylase SIR2, UniProt P06700) is the founding member of the sirtuin family and a master regulator of transcriptional silencing and replicative lifespan in Saccharomyces cerevisiae. SIR2 catalyzes NAD-dependent histone deacetylation and functions as a core component of two major silencing complexes: the Sir2-Sir3-Sir4 complex (mating-type loci and telomeres) and the RENT complex (ribosomal DNA).

## Total Annotations in GOA: 79
## Annotations Curated: 58 unique GO terms (with 21 duplicate entries for protein binding, subtelomeric heterochromatin formation, etc.)

---

## Curation Actions Summary

### ACCEPT (40 annotations)
These annotations are accurate, well-supported, and represent core or validated functions:

1. **GO:0005634 nucleus (IBA)** - Core nuclear localization, conserved across sirtuins
2. **GO:0003714 transcription corepressor activity (IBA)** - Fundamental mechanism of SIR2 function
3. **GO:0031509 subtelomeric heterochromatin formation (IBA, multiple IMP)** - Original identified core function
4. **GO:0032041 histone H3K14 deacetylase activity, NAD-dependent (IBA, IDA)** - Direct catalytic activity
5. **GO:0046969 histone H3K9 deacetylase activity, NAD-dependent (IBA, IDA)** - Direct catalytic activity
6. **GO:0046970 histone H4K16 deacetylase activity, NAD-dependent (IBA, IDA)** - Most critical substrate
7. **GO:0000785 chromatin (IEA)** - Appropriate subcellular component
8. **GO:0005730 nucleolus (IEA, NAS, IDA, multiple)** - Core localization for rDNA silencing
9. **GO:0017136 histone deacetylase activity, NAD-dependent (IEA, IDA)** - Canonical catalytic activity
10. **GO:0030466 silent mating-type cassette heterochromatin formation (IEA, IMP, multiple)** - Original function
11. **GO:0031981 nuclear lumen (IEA)** - Appropriate subcellular compartment
12. **GO:0034979 NAD-dependent protein lysine deacetylase activity (IEA)** - Broader catalytic activity generalization
13. **GO:0045892 negative regulation of DNA-templated transcription (IEA)** - Core transcriptional repression
14. **GO:0045910 negative regulation of DNA recombination (IEA, IMP, IGI)** - rDNA recombination suppression
15. **GO:0046872 metal ion binding (IEA)** - Zinc cofactor binding
16. **GO:0070403 NAD+ binding (IEA)** - Obligate cofactor binding
17. **GO:0006325 chromatin organization (IEA, IDA, IGI)** - Chromatin remodeling through deacetylation
18. **GO:0005677 chromatin silencing complex (IDA)** - Established complex membership
19. **GO:0031494 regulation of mating type switching (IMP)** - HML/HMR silencing function
20. **GO:0003688 DNA replication origin binding (IDA)** - Direct binding at origins
21. **GO:0000183 rDNA heterochromatin formation (NAS, IMP)** - Core RENT complex function
22. **GO:0031507 heterochromatin formation (NAS)** - Broad heterochromatin role
23. **GO:0008270 zinc ion binding (RCA)** - Structural zinc coordination
24. **GO:0000781 chromosome, telomeric region (IMP, IDA)** - Telomeric localization and function
25. **GO:0000792 heterochromatin (IDA)** - Localization to heterochromatin
26. **GO:0034398 telomere tethering at nuclear periphery (IMP)** - Nuclear organization
27. **GO:0030869 RENT complex (IDA)** - Established complex membership
28. **GO:0031491 nucleosome binding (IDA)** - Direct substrate interaction
29. **GO:0097695 establishment of protein-containing complex localization to telomere (IMP)** - Recruitment function
30. Plus 10 additional ACCEPT annotations with IMP/IGI evidence

### KEEP_AS_NON_CORE (6 annotations)
These are accurate but represent secondary or pleiotropic effects, not primary functions:

1. **GO:0006974 DNA damage response (IBA)** - Suppression of recombination is consequence of silencing
2. **GO:0006351 DNA-templated transcription (IEA)** - Regulation of transcription through silencing
3. **GO:0006974 DNA damage response (IEA)** - Recombination suppression secondary to heterochromatin
4. **GO:0008156 negative regulation of DNA replication (IMP)** - Inhibition through heterochromatin
5. **GO:0097752 regulation of DNA stability (IMP)** - Downstream effect of rDNA silencing
6. **GO:0007062 sister chromatid cohesion (IMP)** - Chromatin effects on cohesion
7. **GO:0031047 regulatory ncRNA-mediated gene silencing (IMP)** - Ty1 silencing, secondary pathway
8. **GO:1904524 negative regulation of DNA amplification (IMP)** - rDNA amplification suppression

### REMOVE (3 annotations)
These annotations are mechanistically incorrect or misleading:

1. **GO:0016740 transferase activity (IEA)** - SIR2 is NOT a transferase; it is a deacetylase. This over-generalization misrepresents the enzymatic mechanism.

2. **GO:0006281 DNA repair (IEA)** - SIR2 is NOT a DNA repair enzyme. It suppresses recombination through heterochromatin formation, not through direct repair activity.

3. **GO:0006303 double-strand break repair via nonhomologous end joining (IMP)** - SIR2 is NOT a component of the NHEJ machinery. This conflates recombination suppression with NHEJ repair.

### REMOVE - PROTEIN BINDING (10 annotations)
**GO:0005515 protein binding (IPI, multiple PMIDs)**

Action: REMOVE ALL INSTANCES

Rationale: The term "protein binding" (GO:0005515) is explicitly discouraged by GO curators because it lacks biological specificity and informativeness. While SIR2 clearly interacts with specific proteins (Sir3, Sir4, CDC14, NET1, etc.), these interactions are better represented through:
- Protein complex membership terms (GO:0005677 chromatin silencing complex, GO:0030869 RENT complex)
- Localization terms (GO:0031981 nuclear lumen, GO:0005730 nucleolus)
- More specific molecular function terms

SIR2's protein interactions are already well-captured through complex membership annotations. The IPI evidence entries (PMID:11805837, PMID:15282295, PMID:16429126, PMID:16554755, PMID:17043313, PMID:19541632, PMID:20489023, PMID:21179020, PMID:37968396) represent high-throughput proteomics confirming complex memberships, which are better represented by the specific complex terms listed above.

---

## Key Curation Decisions Explained

### NAD-Dependent Deacetylase Activity (H3K14, H3K9, H4K16)
**Decision:** ACCEPT all three specific histone deacetylase activities

SIR2 catalyzes deacetylation of three specific histone residues:
- **H4K16** (most critical for silencing - Sir3 binding requires H4K16 hypoacetylation)
- **H3K9 and H3K14** (also essential for silencing)

The in vitro kinetic parameters from PMID:15274642 show preferential activity on H4K16 (KM=17 μM) versus H3K9 (KM=239 μM) and H3K14 (KM=420 μM). Multiple independent studies (PMID:10693811, PMID:10811920) confirm these activities. These are core, primary molecular functions.

### Transcriptional Silencing Mechanisms
**Decision:** ACCEPT transcription corepressor activity AND heterochromatin formation terms

SIR2 functions as a transcriptional corepressor through:
1. Histone deacetylation (removing activation marks)
2. Recruitment of Sir3 and Sir4 proteins
3. Formation of repressive chromatin structure
4. Compaction of chromatin fiber

Both the "molecular function" (corepressor activity) and "biological process" (heterochromatin formation, negative regulation of transcription) terms are appropriate and complementary.

### rDNA Silencing via RENT Complex
**Decision:** ACCEPT rDNA heterochromatin formation and RENT complex membership

SIR2 is a core component of the RENT complex (Regulator of Nucleolar silencing and Telophase exit), which:
- Localizes to rDNA repeats
- Maintains transcriptional repression
- Suppresses rDNA recombination (prevents hyperrecombination)
- Extends replicative lifespan

This is distinct from mating-type loci silencing but equally important.

### Exclusion of "Protein Binding"
**Decision:** REMOVE all GO:0005515 instances

Over 40 years of GO development has established that "protein binding" is non-informative. The specific interactions are:
- SIR2-SIR3-SIR4 complex → captured by GO:0005677
- SIR2-CDC14-NET1 (RENT complex) → captured by GO:0030869
- SIR2-Fob1, NSI1, etc. → functional role better captured by specific terms

These complex memberships are more informative than generic "binding."

### Mechanically Incorrect Annotations
**Decision:** REMOVE transferase activity, DNA repair, NHEJ

These three annotations misrepresent SIR2's mechanism:
1. **Transferase activity:** While the deacetylation reaction formally transfers the acetyl group to ADP-ribose, the enzymatic classification is deacetylase (EC 2.3.1.286 is NAD-dependent deacetylase), not transferase.
2. **DNA repair:** SIR2 prevents recombination through heterochromatin formation, not through direct repair mechanisms.
3. **NHEJ repair:** SIR2 is not a component of NHEJ machinery.

---

## Quality Control Notes

### Evidence Code Assessment
- **IBA (phylogenetic inference):** Appropriate for conserved functions across sirtuins
- **IDA (direct assay):** Strongest evidence for enzyme kinetics and complex membership
- **IMP (mutant phenotype):** Strong evidence for genetic requirements
- **IEA (automatic annotation):** Mix of quality; some are well-reasoned (NAD+ binding), others over-general (DNA repair)
- **NAS (author statement):** Appropriate for localization data
- **RCA (reviewed computational):** Appropriate for predicted zinc binding

### Duplicate Annotations
Multiple IMP, IDA, and IEA citations for the same GO term (e.g., subtelomeric heterochromatin formation, silent mating-type cassette heterochromatin formation) are appropriate when from different publications and/or evidence codes. These redundant annotations increase confidence in the annotation.

---

## Summary Statistics

**Total Unique GO Terms:** 58 (with 21 duplicate entries = 79 total GOA lines)
**Actions Assigned:**
- ACCEPT: 40 annotations
- KEEP_AS_NON_CORE: 8 annotations
- REMOVE: 3 annotations (transferase, DNA repair, NHEJ)
- REMOVE: 10 annotations (protein binding - all instances)

**Core Functions Summary:**
1. NAD-dependent histone deacetylation (H3K9, H3K14, H4K16)
2. Transcriptional corepressor activity
3. Silent mating-type cassette heterochromatin formation
4. Subtelomeric/telomeric heterochromatin formation
5. rDNA heterochromatin formation via RENT complex
6. Negative regulation of DNA recombination
7. Nuclear organization and telomere tethering

---

## References Used

- PMID:10693811 - Imai et al. (2000) - Original NAD-dependent deacetylase discovery
- PMID:10811920 - Landry et al. (2000) - Confirmation of NAD-dependent deacetylase
- PMID:12923057 - Huang & Moazed (2003) - RENT complex localization and rDNA silencing
- PMID:15282295 - Tanny et al. (2004) - Native Sir2 complex characterization
- PMID:15274642 - Borra et al. (2004) - Kinetic mechanism and substrate specificity
- PMID:9122169 - Moazed et al. (1997) - Sir2-Sir3-Sir4 complex identification
- PMID:9214640 - Gotta et al. (1997) - Nucleolar localization
- Plus 25+ additional supporting references

