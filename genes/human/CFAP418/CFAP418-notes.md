# CFAP418 (C8orf37) Gene Review Notes

## Gene Overview
- **Gene Symbol**: CFAP418 (also known as C8orf37, smalltalk)
- **UniProt ID**: Q96NL8
- **Protein**: Cilia- and flagella-associated protein 418
- **Size**: 207 amino acids
- **Domain**: Contains RMP (Retinal Maintenance Protein) domain (pfam14996, aa 63-175)

## Disease Associations
1. **Cone-rod dystrophy 16 (CORD16)** [MIM:614500]
   - Autosomal recessive
   - Early macular involvement
   - Cone loss precedes rod degeneration
   
2. **Retinitis pigmentosa 64 (RP64)** [MIM:614500]
   - Autosomal recessive
   - Rod loss precedes cone degeneration
   - Progressive peripheral vision loss

3. **Bardet-Biedl syndrome 21 (BBS21)** [MIM:617406]
   - Syndromic ciliopathy
   - Features: retinal degeneration, obesity, polydactyly, renal malformations, intellectual disability
   - First functional evidence from zebrafish studies [PMID:27008867 "C8orf37 knockdown reproduced cardinal BBS phenotypes"]

## Key Pathogenic Variants
- **R177W**: Associated with CORD16 and BBS21 [PMID:22177090 "c.529C>T [p.Arg177Trp]"; PMID:36233334 "does not affect interaction with FAM161A"]
- **Q182R**: Associated with RP64 [PMID:22177090 "c.545A>G [p.Gln182Arg]"; PMID:36233334 "does not affect interaction with FAM161A"]
- **L166***: Nonsense mutation in RP patient [PMID:22177090 "c.497T>A [p.Leu166(∗)]"]
- **c.156-2A>G**: Splice site mutation, associated with postaxial polydactyly [PMID:22177090 "two CRD siblings with the c.156−2A>G mutation also showed unilateral postaxial polydactyly"]

## Protein Localization
- **Primary cilium base**: Localized at basal body/transition zone in RPE1 cells [PMID:22177090 "C8orf37 localization at the base of the primary cilium of human retinal pigment epithelium cells"]
- **Photoreceptor connecting cilium**: Enriched at junction between inner and outer segments [PMID:22177090 "at the base of connecting cilia of mouse photoreceptors"]
- **Photoreceptor inner segment**: Present throughout inner segment [PMID:36233334 "C8orf37 immunoreactivity was enriched at the inner segment, including the ciliary base"]
- **Cytoplasm**: Diffuse cytoplasmic localization also observed
- **NOT in outer segment**: Absent from photoreceptor outer segment itself

## Protein Interactions
### FAM161A Interaction
- **Direct interaction confirmed**: Y2H, co-IP, proximity ligation assays [PMID:36233334 "C8orf37 interacted with FAM161A"]
- **Interaction domains**:
  - CFAP418 N-terminus (aa 1-75) required for binding [PMID:36233334 "N-terminal aa 1–75 region on C8orf37 was sufficient and required for its interaction with FAM161A"]
  - FAM161A UPF0564 domain (aa 341-517) [PMID:36233334 "aa 341–517 of FAM161A were sufficient for interaction with C8orf37"]
- **Pathogenic mutations do not disrupt interaction**: R177W and Q182R maintain FAM161A binding [PMID:36233334 "these mutations did not affect interactions between C8orf37 and FAM161A"]

### Other Interactions
- **CAPNS1**: Calpain small subunit 1 (IntAct database)

## Functional Evidence

### Mouse Knockout Studies
- Progressive photoreceptor degeneration (rods and cones) [Deep research: "C8orf37 knockout mouse, the absence of CFAP418 caused disorganized photoreceptor outer segment discs"]
- **Disorganized outer segment discs**: Key phenotype, suggests role in disc morphogenesis [Deep research: "severely disorganized outer segment discs in photoreceptors lacking CFAP418"]
- Normal connecting cilium structure
- No systemic BBS features in mice (species difference)

### Zebrafish Knockdown
- Visual impairment
- Kupffer's vesicle defects (ciliary organ)
- Delayed retrograde intraflagellar transport [PMID:27008867 "defects in retrograde melanosome transport"]
- Left-right asymmetry defects

## Molecular Function
- No enzymatic domains identified
- Likely scaffolding/adaptor protein at ciliary base
- May regulate:
  - Photoreceptor outer segment disc morphogenesis
  - Protein trafficking through connecting cilium
  - Intraflagellar transport (IFT)

## Expression Pattern
- **Ubiquitous expression** with enrichment in:
  - Retina (photoreceptors)
  - Brain
  - Heart
- Consistent with ciliary protein expression pattern

## Evolutionary Conservation
- Highly conserved across ciliated eukaryotes
- Absent in non-ciliated organisms (plants, fungi)
- C-terminal two-thirds most conserved
- Mouse ortholog 82% identical to human

## GO Annotation Assessment

### Cellular Component Annotations
1. **GO:0001917 (photoreceptor inner segment)**: Well-supported by experimental evidence
2. **GO:0005737 (cytoplasm)**: Supported, though broad term
3. **GO:0097546 (ciliary base)**: Strong experimental support from PMID:22177090

### Molecular Function Annotations
1. **GO:0005515 (protein binding)**: Too general, should specify FAM161A interaction

### Biological Process Annotations
1. **GO:0008594 (photoreceptor cell morphogenesis)**: Supported by mouse knockout data

## Core Functions Summary
Based on the evidence, CFAP418 functions as:
1. **Ciliary base scaffold protein** essential for photoreceptor survival
2. **Regulator of photoreceptor outer segment disc morphogenesis**
3. **Component of ciliary protein trafficking machinery** (via FAM161A interaction)
4. **Contributor to ciliary transport processes** (retrograde IFT)

## Key Supporting Literature
- PMID:22177090 - Initial disease gene identification, localization studies
- PMID:27008867 - BBS link, zebrafish functional studies
- PMID:36233334 - FAM161A interaction, domain mapping
- PMC5884456 - Mouse knockout, outer segment disc phenotype

## 2026-10-10 — ClinGen campaign audit and correction

This entry supersedes the functional interpretation above while preserving that journal text and the entire original source/provider/bioinformatics tree. The eight original machine annotation objects and eight original reference identifier/title pairs remain unchanged. The normal intake now yields 13 machine rows; that distinct current projection is retained as audit context, not substituted for the original source family. The four old authored NEW process proposals are adjudicated separately below. No alternative product record existed in the original review or the new seed.

The current standalone biological synthesis is phospholipid binding, inferred for human CFAP418 from direct mouse ortholog experiments. The 2024 study (PMID:37971880) uses full-length mouse NM_026005-derived His- and GST-tagged proteins, with constructs traced to PMID:29440555. The publisher supplement specifies bacterial expression, purification and immobilized lipid/PIP-strip overlays. Both tags recognize phosphatidic acid and cardiolipin; weaker His-only lysophosphatidic-acid signal is not added as a third function. No human protein assay, tag removal, affinity constant or liposome experiment is implied. Two specific human ISS proposals cite mouse Q3UJP5 and feed one broader phospholipid-binding core. The primary full text and independent supplemental/figure peer support the precise species and assay limits.

Mouse loss-of-function changes retinal lipid composition, membrane-protein association and outer-segment disc organization. These effects and the PRKCA phosphorylation readout do not show CFAP418 catalysing lipid metabolism, inhibiting a kinase, transferring or sequestering lipids, or operating an IFT motor. Its performed membrane mechanism is unresolved. Consequently, the core has no direct process link inferred only from these downstream outcomes.

The historical bioinformatics RESULTS.md names Q6ZT21 and 453 amino acids; the official record identifies that sequence as TMPPE, not human CFAP418 Q96NL8 (207 amino acids). Its long coiled-coil/motif claims cannot support this protein. A separate historical mouse FASTA uses Q8BXQ0, now resolving to Etnk1, rather than Cfap418 Q3UJP5. Another output counted the literal sequence terminator as two residues. The valid 207-residue human data FASTA is distinguished from these other artifacts. All original artifact bytes are retained; no new predictive analysis is claimed. The authored pathway page now starts with a dated correction, and its preserved historical diagram and linked old SVG are explicitly superseded. The exact identity records, hashes and parsing observations are in [the source audit](CFAP418-source-evidence.json).

Both original protein-binding assertions are retained as non-core. The PMID:27173435 human CFAP418–CAPNS1 pair has two source-linked tandem-affinity IntAct records (EBI-12449215 and EBI-12449224), representing opposite tag orientations in one study rather than separate replication. Actual HEK293T affinity-purification Methods and the source records support association without a binary interface or calpain-regulatory claim. PMID:36233334 tests human CFAP418–FAM161A by yeast two-hybrid and tagged HEK293 proximity ligation, with separate marmoset retinal proximity evidence. It does not report the previously claimed co-IP. N-terminal fragment self-activation and the partner-dependent growth controls are kept in scope. Neither paper establishes scaffold-protein binding or transfers FAM161A microtubule activity to CFAP418.

This retention follows the standing explicit project instruction: [published ClinGen curation policy](https://github.com/ai4curation/ai-gene-review/blob/8a69f3d2b551d632a37bfeb6217a7d667db8d51b/projects/CLINGEN_MENDELIAN.md#curation-instructions). Supported generic binding is retained as non-core unless a more informative activity is supported; a partner name or unreliable structural prediction does not justify a narrower assignment.

The original human hTERT-RPE1 cytoplasmic and serum-starvation-associated ciliary-base observations in PMID:22177090 are both retained. The later mouse knockout controls in PMID:29440555 question antibody specificity and find broad tagged-protein distribution without exclusive basal-body enrichment; they do not erase the earlier human IDA. Endogenous rat retinal fractionation and marmoset staining provide additional compartment context. Broad cytoplasm and inner segment are core locations; ciliary-base localization remains non-core with its nonexclusive, assay-dependent scope.

The original morphogenesis ISS assertion is refined to outer-segment organization based on actual mouse Q3UJP5 IMP evidence in PMID:29440555, whose knockout disc-stack phenotypes were previously misattributed to PMID:22177090. This is a semantic specificity recommendation, not a claim that GO:0035845 is formally a descendant of GO:0008594 or that broad morphogenesis is false.

All four prior authored NEW processes are withdrawn: differentiation was inferred from disease/developmental phenotypes without a performed differentiation step; broad cell-projection organization relied on the unsupported scaffold interpretation; intraciliary transport was inferred from a zebrafish melanophore melanosome-retrieval assay in PMID:27008867; and the separate outer-segment-organization proposal is now redundant with the existing source-preserving refinement. The actual zebrafish ciliary-vesicle phenotype and later retinal trafficking effects remain biological observations, but no direct CFAP418 IFT action is invented. Current typed term definitions/parents and the authenticated GO-CAM index were checked; no target hit was found, which is not evidence for adding a process. No new process is proposed.

Source access: selected main caches remain byte-for-byte unchanged. PMID:22177090 is abstract-only in main, but its genuine fresh normal full variant and authentic PMC body were read. The selected PMID:27008867 cache is flagged full but lacks key sections; authentic PMC full Methods/Results supplied the construct and transport scope. PMID:27173435 and PMID:36233334 selected full caches were read for the relevant assays. PMID:29440555 and PMID:37971880 were absent at the pinned main and were added through genuine normal fetching. For the latter, the independent peer recovered the original publisher supplement and visually checked the lipid panels and species alignment. Reference assessments describe actual access depth rather than treating a cache-availability flag as the whole access record.

The genuine historical provider reports remain unchanged. The new default Falcon attempt timed out after the bounded allowance, and the genuine perplexity-lite fallback returned insufficient quota; no new provider report was fabricated. Manual primary reading and independent peer consultation supplied this audit. Short supporting quotations are counted across newly authored YAML and this append, including repetitions: PMID:22177090 19 words, PMID:36233334 10 words, PMID:29440555 5 words, PMID:37971880 15 words. There are no new primary quotations in this append or the pathway correction. The inherited journal and retained historical pathway body are identified as historical, not newly authored quotations; source downloads and literal machine records remain evidence artifacts.


## 2026-10-10 — PR #4553 source-artifact correction

The current review conclusions remain unchanged. The prior audit correctly rejected the wrong-protein analysis, but its author-generated report and FASTA label still needed in-file correction. Dated supersession notices now precede the complete historical RESULTS.md and previously empty README.md. Q6ZT21 is TMPPE (453 aa), whereas human CFAP418 is Q96NL8 (207 aa). Fresh official UniProt retrieval also resolves historical Q8BXQ0 to current primary Q9D4V0/Etnk1. The historical mouse FASTA has a 363-aa sequence exactly matching that entry, not mouse Cfap418 Q3UJP5 (209 aa). Its header now states that identity and the correction date; every byte after the header newline remains unchanged. Analysis scripts, results, plots and other sequence files remain historical artifacts; no replacement analysis or new functional inference was run. The durable source artifact records the source URLs, identity hashes and sequence comparison.

PMID:37971880 Figure 4 Results provide mitochondrial context for the independent in-vitro cardiolipin-binding assay: PGS1 abundance falls in young knockout retinas and photoreceptor mitochondrial shape becomes irregular. The same text reports relatively normal mitochondrial position/cristae and unchanged retinal oxygen consumption under the tested conditions. These phenotypes support a lipid-homeostasis question; they do not demonstrate endogenous CFAP418 mitochondrial localization, establish access to inner-membrane cardiolipin, or independently validate direct lipid binding in vivo. The added question targets that unresolved link. No mitochondrial-location annotation is proposed.

The existing GO:0008594 MODIFY recommendation still retains GO:0035845 outer-segment organization as a source-supported non-core developmental consequence; it is not promoted to an experimentally resolved disc-building activity of the lipid-binding core. The localization finding now uses a short action-bearing exact anchor in place of a bare cell-type phrase. All original assertions, actions, source-reference identities, products and source caches remain intact; the old notes are preserved as the exact prefix. This follow-up adds no primary quotation in notes or banners. The current YAML quote totals, including repeated inherited-in-YAML anchors, remain below 25 words per primary source; preserved historical notes/artifacts are accounted for separately.
