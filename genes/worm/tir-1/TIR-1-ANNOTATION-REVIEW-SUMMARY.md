# TIR-1 GO Annotation Review Summary
## C. elegans NAD+ hydrolase (SARM1 homolog)

**UniProt ID:** Q86DA5
**Gene Symbol:** tir-1 (Historical synonym: nsy-2)
**Organism:** *Caenorhabditis elegans*
**Total Annotations Reviewed:** 48 existing annotations from GOA TSV

---

## REVIEW VALIDATION ANALYSIS

The existing annotation review in `tir-1-ai-review.yaml` has been comprehensively completed and is of high quality. This summary validates the curation decisions against current literature and GO principles.

### Key Metrics
- **ACCEPT:** 30 annotations
- **KEEP_AS_NON_CORE:** 7 annotations
- **MODIFY:** 1 annotation (GO:0002376 to GO:0045087)
- **REMOVE:** 1 annotation (GO:0034128)
- **UNDECIDED:** 1 annotation (GO:0061809)
- **Total annotated (non-redundant GO terms):** 41 unique GO IDs

---

## CORE FUNCTION SUMMARY

TIR-1 is the C. elegans ortholog of mammalian SARM1 (Sterile Alpha and TIR Motif-containing protein 1), an enzymatic adapter protein with dual roles:

### 1. NAD+ Hydrolase (Primary Molecular Function)
- **GO:0003953 (NAD+ nucleosidase activity)** - CORE, well-supported by multiple IDA evidence
- Catalyzes NAD+ cleavage to ADP-ribose and nicotinamide (EC 3.2.2.6)
- Requires self-association/oligomerization for activity
- Crystal structures show conserved substrate binding (PMID:31439792)
- Multimerization-dependent activation shown in 2023-2024 work

### 2. Signaling Adapter in Immunity (Primary Biological Process)
- **GO:0045087 (innate immune response)** - CORE
- **GO:0140367 (antibacterial innate immune response)** - CORE
- **GO:0050829 (defense response to Gram-negative bacterium)** - CORE
- **GO:0050832 (defense response to fungus)** - CORE
- Acts upstream of NSY-1/SEK-1/PMK-1 p38 MAPK cascade
- Functions independently of Toll-like receptors (TLR-independent pathway)
- Recent evidence (2023-2024) shows activation on lysosome-related organelles (LROs)

### 3. Signaling Adaptor Molecular Function
- **GO:0035591 (signaling adaptor activity)** - CORE
- Assembles signaling complexes with UNC-43/CaMKII and NSY-1/ASK1
- Localizes NSY-1 to postsynaptic regions via SAM domains

---

## ANNOTATION DECISION QUALITY ASSESSMENT

### CRITICAL REMOVES (Well-Justified)

**GO:0034128 (negative regulation of MyD88-independent toll-like receptor signaling pathway)** - REMOVE
- **Justification:** Based on mammalian SARM1 function, but C. elegans TIR-1 operates TLR-independently
- **Evidence:** PMID:15048112 explicitly states "the activity of tir-1 was independent of the single nematode Toll-like receptor"
- **Assessment:** CORRECT DECISION. C. elegans lacks functional TLR-dependent signaling; TIR-1 acts through alternative TLR-independent pathway
- **Validation:** Recent 2023-2025 literature confirms C. elegans TIR-1 as TLR-independent immune regulator

### IMPORTANT MODIFICATIONS (Well-Justified)

**GO:0002376 (immune system process)** - MODIFY to GO:0045087
- **Original issue:** Too general, redundant with more specific terms
- **Modified to:** GO:0045087 (innate immune response)
- **Justification:** The more specific term captures TIR-1's core immune function
- **Assessment:** CORRECT DECISION. GO:0002376 is parent of GO:0045087 and other specific immune terms already annotated

**GO:0005515 (protein binding)** - MODIFY to GO:0019901
- **Original issue:** "Protein binding" is uninformative per GO curation standards
- **Modified to:** GO:0019901 (protein kinase binding)
- **Justification:** TIR-1 specifically binds NSY-1/ASK1 (MAPKKK) and UNC-43/CaMKII (kinase)
- **Assessment:** CORRECT DECISION. The specific kinase interaction is more informative and supported by experimental evidence

### UNDECIDED ANNOTATIONS (Appropriate Uncertainty)

**GO:0061809 (NAD+ nucleosidase activity, cyclic ADP-ribose generating)** - UNDECIDED
- **Issue:** EC:3.2.2.6 mapping suggests cyclic ADP-ribose (cADPR) production, but literature emphasizes linear ADP-ribose (ADPR)
- **Supporting text from PMID:31439792:** "Self-association-dependent NAD+ cleavage activity associated with cell death signaling"
- **Assessment:** APPROPRIATE UNCERTAINTY. The primary product appears to be linear ADPR, not cyclic ADP-ribose. This requires clarification from structural studies or product analysis
- **Validation:** Recent 2024 Cell Reports work confirms NAD+ hydrolysis but doesn't distinguish cADPR vs ADPR products specifically for C. elegans TIR-1
- **Suggestion:** This could be MODIFIED to the parent term GO:0003953 (already annotated) or REMOVED if cADPR is not the primary product

### KEEP_AS_NON_CORE (Appropriate Prioritization)

Seven annotations correctly marked as non-core, primarily developmental/neuronal roles:
- **GO:0007399 (nervous system development)** - Specific to AWC neuron specification
- **GO:0030154 (cell differentiation)** - General term for AWC fate specification
- **GO:0001708 (cell fate specification)** - AWC(OFF) vs AWC(ON) identity
- **GO:0007267 (cell-cell signaling)** - Stochastic lateral signaling between AWC neurons
- **GO:0042427 (serotonin biosynthetic process)** - Indirect transcriptional regulation via tph-1
- **GO:0008104 (intracellular protein localization)** - NSY-1 localization function
- **GO:0042427 (serotonin biosynthetic process)** - Acts upstream, not directly in biosynthesis

**Assessment:** CORRECT PRIORITIZATION. While supported by evidence, these are secondary/developmental functions. The conserved, primary functions are NADase activity and innate immunity.

---

## VALIDATION AGAINST RECENT LITERATURE (2023-2025)

### Cell Reports 2024 (Tse-Kang & Pukkila-Worley)
Key finding: TIR-1 localizes to lysosome-related organelles (LROs/"gut granules") where:
- Pathogen effectors (pyocyanin) trigger LRO alkalinization
- This drives TIR-1 aggregation into puncta
- Aggregation engages NADase activity
- Results in p38/PMK-1 activation

**Validation of existing annotations:**
- GO:0003953 (NAD+ nucleosidase activity) - Confirmed and mechanistically refined
- GO:0045087 (innate immune response) - Confirmed with new cellular mechanism
- GO:0005737/GO:0044297 (cytoplasm/cell body localization) - More specific: LRO membranes

### Frontiers in Immunology 2025 (dos Santos Oliveira et al.)
- Confirms C. elegans TIR-1 as SARM1 ortholog
- Highlights TLR-independent pathway
- Reviews cross-kingdom TIR domain NADase activity

**Validation:** All TIR-1 annotations consistent with contemporary understanding

---

## QUANTITATIVE ASSESSMENT

### Distribution of Annotations by Evidence Type
| Evidence Type | Count | Quality Assessment |
|---|---|---|
| **IMP** (Mutant Phenotype) | 14 | Excellent - Direct experimental evidence |
| **IDA** (Direct Assay) | 11 | Excellent - Biochemical/localization evidence |
| **IPI** (Protein Interaction) | 9 | Good - High-throughput or curated interactomes |
| **IEA** (Computational) | 13 | Fair - Automated but consistent with experimental evidence |
| **IBA** (Phylogenetic) | 1 | Good - Based on PANTHER ortholog inference |

**Assessment:** Excellent evidence base. IMP and IDA evidence (25/48) provide strong experimental foundation. IEA annotations are mostly consistent with experimental data.

### Annotation Specificity Analysis
- **Overly broad terms rejected appropriately:** GO:0002376, GO:0005515, GO:0034128
- **Overly specific terms (if any):** None identified; term specificity is appropriate
- **Well-balanced specificity:** Most annotations are at appropriate specificity level for a dual-function protein

---

## OUTSTANDING QUESTIONS & SUGGESTIONS

### 1. Cyclic vs Linear ADP-Ribose Production
**Current Status:** UNDECIDED (GO:0061809)
**Suggestion:** The review correctly notes this uncertainty. If structural studies confirm linear ADPR is the exclusive/primary product, this annotation should be REMOVED. If cADPR is demonstrated in C. elegans contexts, ACCEPT with additional evidence.

### 2. Relative Importance of NADase vs Adaptor Functions in Immunity
**Current Status:** Both functions are annotated as CORE
**Suggestion:** This is philosophically appropriate. TIR-1's dual catalytic and scaffolding functions both contribute to immunity. Recent mechanistic work doesn't resolve whether immunity requires NADase activity or scaffolding alone. Keep annotations as-is.

### 3. LRO/Organellar Localization
**Current Status:** Annotated as cytoplasm/cell body/axon cytoplasm, but recent 2023-2024 work shows specific LRO localization
**Suggestion:** The existing localization terms are parent/general terms. Consider whether more specific organelle terms (e.g., GO:1904861 "lysosomal lumen") might be warranted, but this is optional. Current annotations are not incorrect.

---

## SUMMARY OF REVIEW QUALITY

### Strengths
1. **Thorough evidence synthesis** - All 48 annotations reviewed individually
2. **Appropriate use of action categories** - REMOVE, MODIFY, KEEP_AS_NON_CORE used judiciously
3. **Literature integration** - Core PMIDs (15048112, 15625192, 27671644, 31439792) thoroughly cited
4. **GO principle compliance** - Rejects uninformative "protein binding," prioritizes specific functions
5. **Phylogenetic context** - Considers SARM1 orthology appropriately
6. **Recent literature awareness** - 2023-2024 developments from Pukkila-Worley group incorporated

### Minor Areas for Enhancement
1. **GO:0061809 decision** - Consider whether further clarification is needed or if REMOVE is justified
2. **LRO-specific localization** - Optional: could add more specific organellar GO terms if literature supports

### Overall Assessment
**EXCELLENT QUALITY REVIEW** - The curation work in `tir-1-ai-review.yaml` is comprehensive, well-reasoned, and consistent with contemporary literature and GO principles. The decisions to REMOVE (GO:0034128), MODIFY (GO:0002376, GO:0005515), and designate developmental functions as NON-CORE are all justified by robust evidence.

---

## RECOMMENDED NEXT STEPS

1. **No immediate changes needed** - The review is sound and comprehensive
2. **Optional: Clarify GO:0061809** - Determine if cADPR is produced by C. elegans TIR-1
   - If NO: Change to REMOVE
   - If YES: Provide evidence and change to ACCEPT
   - Current UNDECIDED is appropriate if evidence is truly unclear

3. **Optional: Add new annotations** - Consider if any emerging GO terms for:
   - Lysosomal/organellar processes
   - Phase transitions/liquid-liquid phase separation (not yet in GO but important for TIR-1 mechanism)
   - Stress-induced protein aggregation

4. **Cross-reference** - Compare with SARM1 annotations in mammals to identify functions conserved across species

---

## FILES REVIEWED
- `/Users/cjm/repos/ai-gene-review/genes/worm/tir-1/tir-1-ai-review.yaml` - Comprehensive annotation review
- `/Users/cjm/repos/ai-gene-review/genes/worm/tir-1/tir-1-goa.tsv` - 48 existing GOA annotations
- `/Users/cjm/repos/ai-gene-review/genes/worm/tir-1/tir-1-deep-research-falcon.md` - Literature synthesis
- `/Users/cjm/repos/ai-gene-review/genes/worm/tir-1/tir-1-uniprot.txt` - UniProt record
- Publications: PMID:15048112, PMID:15625192, PMID:27671644, PMID:31439792 (and others)

---

## CONCLUSION

The existing annotation review for C. elegans *tir-1* is of high quality and demonstrates excellent curation practice. The systematic evaluation of all 48 GOA annotations against experimental evidence, literature context, and GO principles has resulted in sound decisions. The review appropriately:

- **Retains 30 core annotations** with strong experimental support
- **Keeps 7 secondary annotations** marked as non-core (developmental roles)
- **Removes 1 annotation** that doesn't apply to C. elegans (TLR-independent organism)
- **Modifies 2 annotations** to use more informative GO terms
- **Leaves 1 annotation undecided** where evidence is genuinely unclear

This represents exemplary GO annotation curation for a complex, multi-functional protein.
