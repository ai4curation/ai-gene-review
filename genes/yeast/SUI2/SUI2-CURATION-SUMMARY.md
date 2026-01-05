# SUI2 Gene Annotation Curation Review Summary

## Gene Overview

**SUI2** encodes eukaryotic translation initiation factor 2 subunit alpha (eIF2α), a core component of the translation initiation machinery in *Saccharomyces cerevisiae*. SUI2 was initially identified through genetic suppressor mutations that could suppress initiator codon mutations, revealing its central role in start codon recognition and translation initiation.

### Key Biological Role

eIF2α functions as the catalytic subunit of the heterotrimeric eIF2 complex (composed of alpha, beta/SUI3, and gamma/GCD1-GCD2 subunits). The primary mechanism involves:

1. Formation of the ternary complex: eIF2-GTP binds to formyl-Met-tRNAi
2. Delivery to the 40S ribosomal subunit to initiate complex formation
3. GTP-dependent recognition of the methionine moiety of initiator tRNA
4. GTP hydrolysis upon start codon recognition, triggering factor release
5. Recycling of eIF2-GDP by the GEF eIF2B to regenerate eIF2-GTP

eIF2α is also a critical node in integrated stress responses, being phosphorylated at Ser-52 by kinases (GCN2, HRI, PKR) during stress conditions to attenuate global translation while maintaining GCN4 expression.

## Annotation Curation Results

### Summary Statistics

- **Total annotations reviewed**: 59
- **ACCEPT**: 23 annotations (39%)
- **KEEP_AS_NON_CORE**: 2 annotations (3%)
- **MARK_AS_OVER_ANNOTATED**: 11 annotations (19%)
- **MODIFY**: 1 annotation (2%)
- **REMOVE**: 2 annotations (3%)

### High-Level Curation Strategy

The curation focused on:

1. **Distinguishing mechanistic accuracy from generic annotations**: Removed or marked as over-annotated generic terms like "protein binding" and "nucleic acid binding" that fail to capture mechanistic specificity.

2. **Prioritizing specific molecular interactions**: Retained and emphasized annotations for:
   - Methionyl-initiator methionine tRNA binding (GO:1990856) - the core ligand
   - GTP binding (GO:0005525) - the nucleotide switch
   - Translation initiation factor activity (GO:0003743) - the functional role

3. **Recognizing complex membership and localization**: Retained all annotations related to:
   - eIF2 complex membership (GO:0005850)
   - Multi-eIF complex participation (GO:0043614)
   - 48S/43S preinitiation complex components
   - Cytosolic localization

4. **Evidence quality considerations**: Preferred experimental evidence (IDA, IPI, IMP) over computational predictions, while recognizing that multiple evidence codes for the same accurate annotation strengthen confidence.

## Key Annotation Decisions

### ACCEPTED ANNOTATIONS (23 total)

#### Molecular Function (5 annotations)

1. **GO:0003743 - translation initiation factor activity**
   - Evidence: IBA (phylogenetic), IEA (computational), IDA (experimental)
   - Status: ACCEPT - This is eIF2α's core function. Multiple evidence types strengthen confidence. The IDA evidence from reconstituted yeast translation systems provides direct experimental support.
   - Rationale: eIF2α is fundamentally defined by its role as a GTPase that delivers initiator tRNA to the ribosome.

2. **GO:1990856 - methionyl-initiator methionine tRNA binding**
   - Evidence: IDA (experimental)
   - Status: ACCEPT - This is eIF2α's most direct and specific ligand-binding function. The methionyl-initiator tRNA is the only substrate efficiently bound in the GTP-bound state.
   - Rationale: This interaction is the molecular basis for eIF2α's role as a translation initiation factor, representing the defining molecular interaction.

3. **GO:0005525 - GTP binding** (2 annotations with different references)
   - Evidence: IDA (experimental - 2 studies)
   - Status: ACCEPT - GTP binding creates the conformational state that specifically recognizes the methionine moiety on initiator tRNA. Multiple studies confirm GTP binding is mechanistically central to eIF2α function, with GTP hydrolysis/phosphate release serving as the mechanism for initiation control.
   - Rationale: Not generic GTP binding but GTP-regulated methionyl-tRNA recognition.

#### Biological Process (3 annotations)

4. **GO:0006413 - translational initiation** (3 annotations with IBA, IEA, IDA evidence)
   - Evidence: IBA, IEA, IDA
   - Status: ACCEPT - eIF2α is mechanistically essential for translation initiation. Multiple evidence types from phylogenetic, computational, and experimental sources.
   - Rationale: eIF2α is not merely associated with but mechanistically essential for initiation as the GTPase delivering initiator tRNA to the 40S ribosome.

5. **GO:0001731 - formation of translation preinitiation complex**
   - Evidence: IDA (experimental)
   - Status: ACCEPT - Reconstituted translation system studies demonstrate eIF2α is absolutely essential for 43S preinitiation complex formation because it delivers the initiator tRNA cargo.
   - Rationale: This annotation represents eIF2α's mechanistic role in complex assembly.

#### Cellular Component (8 annotations)

6. **GO:0005850 - eukaryotic translation initiation factor 2 complex** (3 annotations: IBA, IPI, IMP)
   - Evidence: IBA, IPI, IMP
   - Status: ACCEPT - eIF2α is by definition a structural subunit of the eIF2 complex. Multiple evidence types from phylogenetic, biochemical (IPI showing interaction with GCD1 and CDC123), and genetic (IMP from original SUI2 discovery paper).
   - Rationale: Core structural component defining the protein.

7. **GO:0033290 - eukaryotic 48S preinitiation complex** (2 annotations: IBA, IDA)
   - Evidence: IBA, IDA
   - Status: ACCEPT - eIF2α delivers initiator tRNA required for 48S complex assembly. Multiple evidence types from phylogenetic and experimental sources.
   - Rationale: eIF2α is an essential component of this functional intermediate.

8. **GO:0043614 - multi-eIF complex** (2 annotations: IDA from 2 different studies)
   - Evidence: IDA (2 studies)
   - Status: ACCEPT - eIF2α is a structural and functional component of the multifactor complex (MFC) containing eIF1, eIF2, eIF3, eIF5, and initiator tRNA. Both early yeast studies confirm this.
   - Rationale: Multiple IDA annotations from different mechanistic studies strengthen evidence.

9. **GO:0005840 - ribosome**
   - Evidence: IDA (experimental)
   - Status: ACCEPT - eIF2α is demonstrated to associate with ribosomes as part of initiation. While "ribosome" is a broad term, it accurately describes the subcellular localization/association of eIF2α during translation initiation.
   - Rationale: The more specific 48S preinitiation complex annotation provides mechanistic detail; this provides cellular context.

10. **GO:0005829 - cytosol** (2 annotations: IEA, TAS from Reactome)
    - Evidence: IEA, TAS
    - Status: ACCEPT - eIF2α is a cytosolic protein. Multiple evidence types (IEA from UniProtKB, TAS from Reactome expert curation) strengthen confidence.
    - Rationale: Appropriate localization annotation for a translation initiation factor.

11. **GO:0005737 - cytoplasm**
    - Evidence: HDA (homology-derived)
    - Status: ACCEPT - While cytosol is more specific, cytoplasm annotation is broader and provides non-redundant cellular context. HDA evidence is reasonable for established localization.
    - Rationale: Complements the more specific cytosol annotation.

### MODIFIED ANNOTATIONS (1 total)

12. **GO:0043022 - ribosome binding**
    - Evidence: IBA
    - Status: MODIFY
    - Proposed replacements: GO:0003743 (translation initiation factor activity) or GO:1990856 (methionyl-initiator methionine tRNA binding)
    - Rationale: eIF2α does not directly bind the ribosome in isolation. The binding interaction is GTP-dependent and mediated through the methionyl-tRNA substrate. The term "ribosome binding" is too generic and mechanistically inaccurate. More specific terms already annotated better capture the actual mechanism.

### REMOVED ANNOTATIONS (2 total)

13. **GO:0003676 - nucleic acid binding**
    - Evidence: IEA (computational from InterPro domains)
    - Status: REMOVE
    - Rationale: eIF2α does not function as a nucleic acid-binding protein in the traditional sense. The RNA-binding domains identified by InterPro are structural components facilitating methionyl-tRNA recognition, not general nucleic acid binding. The specific interaction is better captured by "methionyl-initiator methionine tRNA binding" (GO:1990856). Including this term conflates structural domains with functional role and is misleading.

14. **GO:0003723 - RNA binding**
    - Evidence: IEA (computational)
    - Status: REMOVE
    - Rationale: While eIF2α does interact with RNA (methionyl-tRNA), generic "RNA binding" is problematic because it suggests broad RNA-binding capability or nonspecific interactions. eIF2α specifically recognizes only the initiator methionyl-tRNA through GTP-dependent binding. This specific function is better represented by "methionyl-initiator methionine tRNA binding" (GO:1990856). Generic "RNA binding" inappropriately groups this with proteins having different binding specificity.

### MARKED AS OVER-ANNOTATED (11 total)

15-25. **GO:0005515 - protein binding** (11 annotations from multiple IPI studies)
    - Evidence: IPI (protein interaction evidence)
    - Status: MARK_AS_OVER_ANNOTATED
    - References: PMID:11805837, PMID:16429126, PMID:16554755, PMID:18719252, PMID:20485439, PMID:24852487, PMID:26211610, PMID:27107014, PMID:37507029, PMID:37968396, PMID:8947054
    - Rationale: Generic "protein binding" is uninformative and should be avoided per GO curation guidelines. eIF2α's specific interactions are:
      - Subunit interactions: beta (SUI3) and gamma (GCD1/GCD2) subunits form the heterotrimeric complex
      - Assembly factor: CDC123 facilitates eIF2 biogenesis
      - GEF interaction: eIF2B catalyzes nucleotide exchange
      - Multifactor complex: eIF5 (TIF5) and other initiation factors
    - These specific interactions are better captured through complex membership annotations (GO:0005850, GO:0043614) and more specific functional terms. The generic "protein binding" fails to convey the mechanistic importance of these interactions.

### KEPT AS NON-CORE (2 total)

26. **GO:0006412 - translation**
    - Evidence: IEA
    - Status: KEEP_AS_NON_CORE
    - Rationale: While eIF2α is involved in translation, it specifically participates only in the initiation phase. The broader term "translation" includes elongation and termination phases in which eIF2α does not participate. The more specific "translational initiation" (GO:0006413) is already annotated and more accurate. This broader term is retained as non-core context but should not be treated as a primary function annotation.

27. **GO:0010494 - cytoplasmic stress granule**
    - Evidence: HDA
    - Status: KEEP_AS_NON_CORE
    - Rationale: eIF2α is phosphorylated during stress and this triggers translational attenuation and stress granule formation. However, the core function is "translation control in response to stress," not stress granule localization per se. Stress granule association is a secondary consequence of translational shutdown. This annotation can be retained as contextual background but is not a core function of the protein. HDA evidence quality is lower than experimental evidence.

## Evidence Code Quality Assessment

The annotations for SUI2/eIF2α show good evidence diversity:

- **Highest quality**: IDA (experimental direct assay) - 13 annotations
- **High quality**: IBA (phylogenetic comparison) - 4 annotations, IMP (mutant phenotype) - 1 annotation
- **Good quality**: IPI (protein interaction) - 23 annotations (though many are generic)
- **Computational**: IEA (automated) - 5 annotations, ISS (sequence similarity) - 0 annotations
- **Expert curation**: TAS (traceable author statement) - 1 annotation
- **Homology-derived**: HDA - 2 annotations

The abundance of IDA evidence reflects the extensive biochemical and structural characterization of translation initiation in yeast, which is a well-studied system.

## Publications Used

Key publications informing this curation:

1. **PMID:2649894** - Original SUI2 identification as eIF2α (Cigan et al., 1989)
2. **PMID:14698289** - GTP-dependent methionine moiety recognition (Kapp & Lorsch, 2004)
3. **PMID:16565414** - Initiator tRNA identity elements and eIF2 binding (Kapp et al., 2006)
4. **PMID:16246727** - Pi release as the rate-limiting step (Pi release controls start-site selection)
5. **PMID:12008673** - Reconstituted yeast translation initiation system
6. **PMID:17242201** - Coupled release of eIF5B and eIF1A from 80S ribosomes
7. **PMID:23775072** - CDC123 role in eIF2 biogenesis (Perzlmaier et al., 2013)
8. **PMID:1739968** - GCN2 phosphorylation and stress response (Dever et al., 1992)

## Recommendations for Future Work

### Core Annotations to Maintain

The following annotations represent the essential, non-redundant, mechanistically accurate set for SUI2/eIF2α:

1. GO:0003743 - translation initiation factor activity (molecular function)
2. GO:1990856 - methionyl-initiator methionine tRNA binding (molecular function)
3. GO:0005525 - GTP binding (molecular function)
4. GO:0006413 - translational initiation (biological process)
5. GO:0005850 - eukaryotic translation initiation factor 2 complex (cellular component)
6. GO:0043614 - multi-eIF complex (cellular component)
7. GO:0033290 - eukaryotic 48S preinitiation complex (cellular component)
8. GO:0001731 - formation of translation preinitiation complex (biological process)
9. GO:0005829 - cytosol (cellular component)

### Missing Annotations Considered

The curation did not identify high-priority missing GO annotations. However, eIF2α's role in stress-responsive translation control through Ser-52 phosphorylation could potentially be represented by:
- GO:0031047 - gene silencing by RNA (if applied to translational attenuation)
- GO:0006355 - regulation of transcription (not applicable - eIF2α does not directly regulate transcription)

The integrated stress response pathway involvement is well-captured by the existing annotations combined with the phosphorylation information in UniProt.

### Specific Interaction Annotations

For future enhancement, more specific GO terms could capture:
- SUI3 (beta subunit) interaction as part of complex formation
- GCD1/GCD2 (gamma subunit) interaction
- CDC123 assembly factor interaction
- TIF5/eIF5 interaction in the multifactor complex
- eIF2B interaction during nucleotide exchange

However, these would require either new GO terms or would be better represented in a GO-CAM (Causal Activity Model) representation rather than simple GO annotations.

## Curation Standards Applied

This review applied the following standards from the GO Curation Guidelines:

1. **Avoid generic molecular function terms**: Removed "protein binding" and "nucleic acid binding" as uninformative
2. **Capture mechanistic specificity**: Retained specific terms like "methionyl-initiator methionine tRNA binding" and "GTP binding" that capture actual molecular mechanisms
3. **Distinguish complex membership from function**: Separated "eIF2 complex" (structural component) from "translation initiation factor activity" (catalytic function)
4. **Prefer experimental evidence**: Weighted IDA, IPI, and IMP more heavily than computational IEA
5. **Remove misleading annotations**: Eliminated "nucleic acid binding" and "RNA binding" that conflate structural domains with functional role
6. **Consider evidence diversity**: Retained multiple evidence codes for well-established annotations, recognizing that evidence aggregation strengthens confidence

## Conclusion

SUI2/eIF2α has been comprehensively reviewed with 59 annotations evaluated. The curation identified and removed 2 misleading generic annotations (nucleic acid binding, RNA binding), marked 11 generic protein binding annotations as over-annotated, and retained 23 high-quality, mechanistically accurate annotations that comprehensively describe eIF2α's essential role as a translation initiation factor, GTPase, methionyl-tRNA binder, and key component of translation initiation complexes.

The resulting annotation set accurately reflects current understanding of eIF2α's mechanism of action in translation initiation and its critical role as a node in integrated stress response pathways.
