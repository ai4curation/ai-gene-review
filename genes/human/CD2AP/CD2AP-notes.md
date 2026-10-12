# CD2AP curation notes

## 2026-06-19

- Deep-research attempt with `just deep-research-falcon human CD2AP --fallback perplexity-lite` timed out after 180 seconds with no generated research artifact, so this manual review uses cached UniProt, GOA, PANTHER family, and publication evidence.
- CD2AP is best treated as an SH3-domain scaffolding/adaptor protein that links membrane and junctional proteins to actin-rich cortical structures. The original CMS/CD2AP paper reports that the protein is cytoplasmic, colocalizes with F-actin and p130(Cas) in membrane ruffles and leading edges, and that ectopic expression changes actin cytoskeleton organization [PMID:10339567 "functions as a scaffolding molecule with a specialized role in regulation of the actin cytoskeleton"].
- Core localization annotations are cytoplasm, actin cytoskeleton/filamentous actin, ruffle, leading edge, plasma membrane/cell periphery, vesicle/endosomal compartments, and junctional structures. UniProt summarizes CD2AP as acting between membrane proteins and actin cytoskeleton, anchoring the podocyte slit diaphragm to actin, and participating in epithelial junction formation.
- Homodimerization and multimeric SH3-mediated complexes are supported. The structural paper states that CD2AP/CMS family endocytic adaptors engage multiple effectors and can couple cargo trafficking to the cytoskeleton [PMID:17020880 "couple cargo trafficking with the cytoskeleton"], and reports that CD2 and Cbl-b peptides mediate multimerization of CMS SH3 domains [PMID:17020880 "can mediate multimerization of N-terminal CMS SH3 domains"].
- The broad `protein binding` annotations should not be accepted as core terms. Several are real interaction observations, but CD2AP's informative molecular role is adaptor/scaffold activity, SH3/proline-rich partner recognition, actin association, or specific complex context rather than generic protein binding.
- Epithelial junction evidence is strong. A full-text JCB paper reports that SH3BP1 formed a complex with JACOP/paracingulin and CD2AP, and that both scaffold proteins were required for normal Cdc42 signaling and junction formation [PMID:22891260 "CD2AP, a scaffolding protein; both were required for normal Cdc42 signaling and junction formation"]. This supports anchoring junction, actin filament organization, and negative regulation of small GTPase signaling annotations.
- CD2AP is also part of the submembrane actin/junction module through CapZ. The same paper states that CD2AP is part of the submembrane actin cytoskeleton and binds/regulates CapZ [PMID:22891260 "CD2AP, a protein that is part of the submembrane actin cytoskeleton and binds and regulates CapZ"].
- Podocyte slit diaphragm localization is biologically central for CD2AP in vivo, even though several slit-diaphragm details in the current GOA set are electronically transferred. I accepted slit diaphragm/anchoring junction context because it is consistent with UniProt and the established renal disease association.
- Neuronal axon/dendrite and synapse annotations are plausible Alzheimer/endosomal context but are not the primary evolved function of CD2AP. The RIN3 Alzheimer paper shows that RIN3 recruited BIN1 and CD2AP to early endosomes and that RIN3/CD2AP expression affected APP cleavage/trafficking in neuronal models [PMID:32552912 "RIN3 recruited BIN1(bridging integrator 1) and CD2AP (CD2 associated protein), two other AD risk factors, to early endosomes"]. I kept axon/dendrite/synapse context non-core rather than making it the defining function.
- The tau secretion annotation from PMID:27044754 is experimental but the cached record is abstract-only and the abstract names FRMD4A rather than CD2AP. Following the project rule not to overrule curators from incomplete evidence, I marked this annotation UNDECIDED rather than removing it [PMID:27044754 "Individual silencing of ten common late-onset Alzheimer's disease risk genes"].
- High-throughput cadhesome, exosome, AD network, and interactome annotations are useful context but not core molecular function evidence. Cadherin binding from E-cadherin proximity proteomics is over-specific for CD2AP because the paper describes a large cadhesome proximity/interactome resource rather than direct CD2AP cadherin binding [PMID:25468996 "isolate and identify 612 proteins in the vicinity of E-cadherin's cytoplasmic tail"].

## 2026-06-20 Second-Pass Review Notes

Second-pass audit confirmed the existing action calls and reference-review
coverage. No YAML changes were needed in this pass.

The single UNDECIDED annotation remains GO:0050714 positive regulation of
protein secretion from PMID:27044754. The cached record is abstract-only and
foregrounds FRMD4A rather than exposing the CD2AP-specific experimental result.
Because the annotation is experimental, it should remain UNDECIDED rather than
be removed without full-text or supplementary-data review.

The core function remains SH3-domain scaffold/adaptor activity linking membrane,
endocytic, junctional, and slit-diaphragm partner complexes to actin-rich
cortical structures. Alzheimer relevance should be represented through
endosomal trafficking modules involving RIN3/BIN1/CD2AP and APP/tau-related
cellular phenotypes, not as generic protein-binding function.

## Falcon deep research integration (2026-06-21)

A freshly-grounded Falcon/Edison deep-research report (CD2AP-deep-research-falcon.md, ~22 cited
sources) is now available; it corroborates the existing review's core picture well — CD2AP as a
multi-SH3 scaffold/adaptor linking nephrin/podocin slit-diaphragm and junctional complexes to actin,
plus endocytic/vesicle trafficking and Alzheimer relevance — and adds no contradictions, only
context. The following Falcon-sourced citations are NOT yet independently verified against full text.

Genuinely new or refined findings beyond the current notes/review:

- Explicit nephrin–podocin–CD2AP–actin axis: CD2AP scaffolds the slit-diaphragm receptor nephrin and
  binds the podocin C-terminus, coupling slit-diaphragm signaling to F-actin via cortactin and
  synaptopodin [Blaine & Dylewski, Cells 2020, doi:10.3390/cells9071700; Ha, World J Nephrol 2013,
  doi:10.5527/wjn.v2.i1.1]. This refines the existing review, which treats slit diaphragm largely as
  electronically-transferred localization rather than a named nephrin/podocin partner module.
- Insulin-responsive Glut4 trafficking: CD2AP forms a complex with the clathrin adaptor GGA2 and
  co-fractionates with Glut4/IRAP/sortilin; loss of CD2AP disrupts GSV/clathrin recycling and
  attenuates insulin-stimulated glucose uptake in podocytes [Tolvanen et al., J Cell Sci 2015,
  doi:10.1242/jcs.175075]. This is a NEW functional module not represented in the existing review.
- Neuronal NGF/TrkA trophic-signaling scaffold: CD2AP is enriched in TrkA+ basal-forebrain
  cholinergic neurons, co-localizes with Rab5 endosomes, and couples TrkA to PI3K-p85/Akt to support
  NGF-dependent axon growth and retrograde signaling [Fitzsimons et al., bioRxiv 2024,
  doi:10.1101/2024.07.24.604961 — preprint, treat cautiously]. Refines the currently generic
  neuron-projection/synapse non-core annotations toward a specific NGF/Rab5 retrograde-trafficking role.
- MYO1F/CASS podosome and phagocytic-cup module: proximity-labeling (BioID) in myeloid cells places
  CD2AP with ASAP1, SH3BP2 and SH3KBP1/CIN85 in an SH3-dependent "CASS" adaptor group recruited to
  podosomes and phagocytic cups in macrophages/microglia [Arden et al., J Cell Sci 2024,
  doi:10.1242/jcs.264357]. This adds molecular partners and a phagocytosis context to the existing
  KEEP_AS_NON_CORE podosome annotation (GO:0002102).
- Dose-sensitive synaptic role: heterozygous Cd2ap mice show altered dendritic branching/spine
  density, impaired ubiquitin-proteasome activity, increased paired-pulse facilitation, and mild
  learning deficits, supporting a haploinsufficient presynaptic requirement [SH3-superfamily/synaptic
  work cited as Mehrabipour et al., Cells 2023, doi:10.3390/cells12162054 — NOTE: this token is cited
  by Falcon for synaptic-plasticity claims that read like a separate mouse study, so the citation
  mapping should be checked against full text before reuse].
- Glioblastoma CD2AP–TRIM5–NF-κB axis: CD2AP stabilizes TRIM5 and promotes NF-κB activity and GBM
  progression [Zhang et al., Cell Death Dis 2024, doi:10.1038/s41419-024-07094-7]. New disease context
  (oncogenic), absent from the existing review; would be non-core if curated.
- OCRL/IPIP27A link: CD2AP associates with the inositol-5-phosphatase OCRL via IPIP27A in podocytes,
  tying it to endosomal trafficking and actin polymerization [Preston et al., Pediatr Nephrol 2020,
  doi:10.1007/s00467-019-04317-4]. Corroborates the endocytic-adaptor theme.

Discrepancies / annotations to revisit:
- No direct contradictions with the existing review or its action calls.
- The Glut4/GGA2/insulin-trafficking and NGF/TrkA/Rab5 modules suggest the existing endocytic-adaptor
  core could be strengthened with a clathrin/endocytic-vesicle process term (e.g. consider whether
  GO:0072583 clathrin-dependent endocytosis or GO:0006897 endocytosis better captures the
  Tolvanen/Arden evidence than relying on GO:0030276 clathrin binding alone). Defer pending full-text
  verification.
- The MYO1F/CASS data (Arden 2024) provide a concrete molecular basis for the GO:0002102 podosome
  KEEP_AS_NON_CORE call and could be cited there if verified.
- Per project guidelines, do not promote any of these to "protein binding"; route new partner
  evidence through specific adaptor/SH3/actin or process terms instead.


## Whole reassessment after source-provenance restoration — 2026-10-05

The preceding journal is preserved verbatim as historical work. This reassessment supersedes its biological judgments where they differ. The historical review compressed 79 distinct raw assertions into 72 decisions by collapsing seven partner distinctions across five binding groups. The restored review retains all 79 complete source objects, in raw order, and judges each separately. The immutable human Q9Y5K6 record contains the 639-residue reviewed protein and no alternative-products block; no predicted transcript product is invented. All source caches, the existing Falcon report and its nested artifacts remain unchanged.

The project’s explicit binding override controls this review: supported generic protein binding is retained as KEEP_AS_NON_CORE unless actual evidence justifies a more informative function. It is not removed or marked over-annotated merely for being generic. The historical blanket binding decisions and provider-supported core synthesis were reconsidered rather than inherited. The existing Falcon report was read as background; it includes source associations that remain unverified, including a general SH3 compilation attached to a claimed later mouse dosage experiment. No provider prose supplies a primary evidence anchor. The final proposal contains 19 ACCEPT, 40 KEEP_AS_NON_CORE, 8 MODIFY and 12 UNDECIDED decisions, no REMOVE/OVER and no NEW annotation. Its two cores describe physical partner organization and direct filament binding/stabilization.

### Target identity, interaction direction and molecular organization

The complete original CMS paper establishes human 639-residue CD2AP constructs, biochemical experiments in human 293T cells and imaging of the human construct in monkey COS-7 cells. Its proline-rich regions bind partner SH3 domains, including BCAR1/p130Cas, Fyn, GRB2 and p85; CD2AP’s own SH3 domains recognize other proline-rich partners. These directions must not be reversed. The BCAR1 accession Q6P5Z4 is preserved: official NCBI gene-level mapping resolves it as BCAR1, without proving the exact historical isoform/construct. The original coiled-coil experiments support homotypic association but do not establish a universal native oligomeric stoichiometry. [PMID:10339567](https://pubmed.ncbi.nlm.nih.gov/10339567/); [official BCAR1 record](https://www.ncbi.nlm.nih.gov/gene/9564)

The CBL/CBLB rows are refined to ubiquitin protein ligase binding and FYN rows to protein tyrosine kinase binding. These terms name the binding partner class and do not transfer its catalysis to CD2AP. Exact reviewed UniProt edge corroboration is disclosed where an original network table was not inspected. The direct CD2AP SH3A/CD2 and Cbl-b studies are domain/peptide experiments: CD2AP dimers and CIN85 trimers in the same abstract must not be conflated. GRB2 network rows remain generic binding because independent evidence for a particular SH3 interface does not establish that every original network context used that interface. AP-SRM profiling of GRB2 complexes is not APS-regulated recruitment. [PMID:17020880](https://pubmed.ncbi.nlm.nih.gov/17020880/); [PMID:23663663](https://pubmed.ncbi.nlm.nih.gov/23663663/); [PMID:21706016](https://pubmed.ncbi.nlm.nih.gov/21706016/)

Selected actual SLP65/BLNK Results and Methods distinguish human/mouse CD2AP coassociation and motif controls from the purified CIN85 example and chicken DT40 redundancy experiments. Selected human podocyte IQGAP1 experiments include target co-IP and proximity ligation; IQGAP1 is the perturbation target, and those phenotypes are not silently reassigned to CD2AP. [PMID:21822214](https://pmc.ncbi.nlm.nih.gov/articles/PMC3181483/); [PMID:22662192](https://pmc.ncbi.nlm.nih.gov/articles/PMC3360763/)

### Own filament activity versus regulation of another capping protein

The 1999 CMS imaging demonstrates colocalization and cytoskeletal remodeling, not purified direct F-actin binding. The later cosedimentation abstract explicitly reports “CD2AP directly associates with filamentous actin”; its complete Methods and construct species were not recovered in the normal abstract-only cache. Independent 2013 Methods establish full-length human CD2AP and its 351–639 truncation produced in Rosetta bacteria. Full-length protein caps barbed ends and limits both addition and loss of subunits. The truncation still binds filaments but fails the capping readout. Single-filament washout and oriented Limulus bundles distinguish end capping from actin-monomer sequestration. [PMID:12217865](https://pubmed.ncbi.nlm.nih.gov/12217865/); [PMID:24322428](https://pmc.ncbi.nlm.nih.gov/articles/PMC3857477/); [publisher DOI](https://doi.org/10.1083/jcb.201304143)

The 2013 cellular experiments use MDCK cells, while the membrane reconstitution uses rat liver junctional fractions. Depletion decreases junctional F-actin and resistance to imposed mechanical stress; it does not simply abolish basal epithelial barrier function. These distinct experiments support a contribution to cytoskeletal structural integrity under GO:0005200, without demanding that CD2AP be the sole load-bearing polymer. Its migration effect is context-dependent: stabilized junctions can restrain migration. The core summarizes this structural mechanism through the more informative filament-binding activity and actin-filament-organization process. It does not duplicate migration ancestors or add an annotation merely to silence a coverage advisory.

CPI-region regulation of heterodimeric capping protein is a separate mechanism. The 2006 work uses CD2AP fragments, including a CPI segment, with chicken CP; the inspected Methods do not explicitly resolve the species of the 636-residue source construct. The 2010 structure uses a human CD2AP peptide with chicken CP, with human CD2AP GST fragments derived from a whole-brain cDNA library; related mouse CARMIL constructs are separate controls. Neither fragment inhibition nor an isolated peptide structure replaces the full-length human capping evidence. Selected external 2012 primary Methods/Results use mouse wild-type/knockout podocytes and 293T coassociation to study recruitment of CP to cortactin; the normal cache for that paper remains abstract-only. [PMID:16707503](https://pmc.ncbi.nlm.nih.gov/articles/PMC2581424/); [PMID:20625546](https://pubmed.ncbi.nlm.nih.gov/20625546/); [PMID:23090967](https://pmc.ncbi.nlm.nih.gov/articles/PMC3536300/)

No NEW capping process is proposed. The source set already includes actin filament organization, and barbed-end capping is a more specific part of that organization. Official term ancestry and positive dated ADD1/Twf1/Capg comparator examples were inspected; historical comparator displays are not treated as a systematic current absence proof. The local GO-CAM index search found no CD2AP/Q9Y5K6 hit, which is only a local result. [GO:0051016](https://amigo.geneontology.org/amigo/term/GO:0051016); [GO:0005200](https://amigo.geneontology.org/amigo/term/GO:0005200)

### Junctional signaling and localization boundaries

The human epithelial SH3BP1 paper provides CD2AP coassociation, recruitment and depletion evidence. SH3BP1 performs GTPase-activating catalysis; CD2AP organizes the complex. Critically, CD2AP depletion lowers bulk active Cdc42 while partially disrupting junctional SH3BP1 recruitment. The authors’ spatial-termination model is partly interpretive, and the selected passages do not demonstrate CD2AP-specific spatial Cdc42 activity imaging. The existing negative-regulation IMP is retained as non-core with this precise organizing contribution, not a claim that CD2AP globally suppresses Cdc42 or that its loss increases Cdc42. T’s bounded independent consultation agrees that this qualified retention is defensible; T did not author the annotation. [PMID:22891260](https://pmc.ncbi.nlm.nih.gov/articles/PMC3514035/); [GO:0051058](https://amigo.geneontology.org/amigo/term/GO:0051058)

The RIN3 study distinguishes transfected HEK293T interaction/recruitment from endogenous mouse neuronal and rat PC12 localization. RIN3 recruits CD2AP to Rab5 early endosomes under the tested conditions; selected Rab7/Rab11 negatives do not rule out other compartments in other systems. RIN3 supplies Rab exchange activity. Axon, dendrite and broad neuronal-projection transfers are retained as contextual ortholog-based locations. More specific growth-cone, late-endosome and trans-Golgi donor claims remain unresolved where their exact assay was not read. [PMID:32552912](https://pmc.ncbi.nlm.nih.gov/articles/PMC7301499/)

GO:0005641 names the intermembrane nuclear-envelope lumen, not perinuclear cytoplasm. Selected external podocyte confocal descriptions do not resolve that narrow space, and the original mouse donor mapping remains uncertain. The dated March 2023 MGI comparative graph links neuromuscular-junction and synapse-organization donor contexts to PMID31412248. Actual inspected passages distinguish fly Cindr NMJ experiments from mouse brain protein/proteasome measurements; complete donor mapping and supplements remain unresolved. Neither a fly-focused title nor partial cross-species evidence is a basis for a wrong-gene removal. Podosome, growth-cone and direct clathrin-binding donor evidence also need resolution. [GO:0005641](https://amigo.geneontology.org/amigo/term/GO:0005641); [nuclear-envelope lead](https://pmc.ncbi.nlm.nih.gov/articles/PMC3655450/); [PMID:31412248 external primary](https://pmc.ncbi.nlm.nih.gov/articles/PMC6703184/); [dated MGI graph](https://www.informatics.jax.org/homology/GOGraph/Cd2ap)

The HPA immunofluorescence row is retained with explicit curator deference and independent target evidence; its original image/antibody panel was not re-inspected. UniProt controlled-vocabulary mappings, Ensembl Compara mouse transfers, ARBA rules and PAINT inherited-node assertions are different methods and were not treated as one generic electronic source. The original PAINT tree/MSA was not reconstructed; donor count and target self-reference were never used as defects. Broad cytoplasm, vesicle, protein complex and cell-periphery assertions remain valid but non-core.

### Source access, corrections and unresolved target tables

All 23 original PMID complete available abstracts and all six supplemental complete headers/abstracts were read. The normal caches for 24322428 and 20625546 contain XML, and 16707503 contains a fuller HTML body; selected load-bearing passages or complete scientific narrative were read as specified in each reference assessment. Supplemental 23090967, 12217865 and 17713465 remain normal abstract-only records. External primary access is separately linked above and recorded in the source ledger; it does not change cache bytes or access flags. The source pipeline imported the six authenticated normal caches once, after separate integrity and factual-access review.

True full-text flags on 25036637, 25468996 and 33961781 accompany partial HTML extractions. The cadherin/proximity source also contains mixed-version material; the exact CD2AP table and controls were not inspected. Its HDA remains UNDECIDED, not automatically over-annotated because of proximity methodology. The FRMD4A tau-secretion paper describes a broader gene screen, but its CD2AP panel/direction was unavailable; the CD2AP IMP remains UNDECIDED rather than removed from a title inference. The two exosome identifications likewise await target tables and fraction controls. An intracellular dominant function does not preclude extracellular-vesicle detection. HENA is explicitly an integrated heterogeneous resource, not a newly inspected pairwise experiment.

The actual 2012 correction to PMID17853893 states that the ROCK1 yeast-two-hybrid construct was residues 1–123 rather than full length; it does not state a CD2AP/ALIX correction, and the co-IP remains unaffected. The actual 2017 correction to PMID21988832 changes Juncheng Wei’s name only. These notices were read through the separately recorded primary notice access, not guessed from their existence. [2012 correction](https://pmc.ncbi.nlm.nih.gov/articles/PMC3400022/); [2017 correction](https://pmc.ncbi.nlm.nih.gov/articles/PMC5740501/)

### Human disease context and remaining audit work

The frozen ClinGen associations remain exactly AR Definitive for focal segmental glomerulosclerosis 3 susceptibility (2024-04-08) and AD Moderate for inherited focal segmental glomerulosclerosis (2024-06-28). The normal PMID17713465 abstract reports a homozygous truncation, low residual lymphocyte expression and reduced F-actin binding, with clinically unaffected heterozygous parents in that family. This is bounded support for loss-of-function biology, not proof against all heterozygous susceptibility and not a new clinical classification. [PMID:17713465](https://pubmed.ncbi.nlm.nih.gov/17713465/)

The remaining 12 UNDECIDED source assertions are podosome, nuclear-envelope lumen, late endosome, clathrin binding, growth cone, neuromuscular junction, trans-Golgi-network membrane, synapse organization, positive protein secretion, cadherin binding and two exosome identifications. Each is retained with its exact source object and a source-specific access question. No NEW annotation, source cache edit, provider rewrite or history mutation was made in this TMP authoring stage.


## Capping mechanisms and annotation specificity — 2026-10-05

This entry supersedes the earlier rationale for retaining only broad actin organization. Full-length human CD2AP itself performs barbed-end capping: the original single-filament washout and oriented Limulus-seed experiments discriminate end protection from soluble monomer sequestration, and polymerization/depolymerization measurements agree. The human 351–639 fragment retains filament binding without the full-length capping result. Both broad GO:0007015 review rows now propose GO:0051016 using this independent human biochemical experiment; the original IMP and IBA source fields remain intact. The epithelial knockdown experiment is not relabeled as a direct capping assay, and the narrower function is not retroactively attributed to an uninspected ancestral PAINT node. [PMID:24322428](https://pubmed.ncbi.nlm.nih.gov/24322428/).

CD2AP also regulates a different capper, the CP heterodimer. In the 2010 study, human CD23 (485–507) is both a crystallographic ligand and a partial CP inhibitor in Figure 9D; extended CD30 is more inhibitory. The CP used there is chicken CP. The predominantly beta-subunit peptide interface does not establish isolated human CAPZA1 inhibition, although the original human epithelial co-IP supports the CAPZA1-containing complex association. The generic binding row therefore refines to molecular function inhibitor activity with explicit assay scope, and a separate core distinguishes this mechanism from direct full-length CD2AP capping. Earlier CPI-region constructs show partial inhibition and uncapping; those construct effects are not a universal claim about the intact protein in cells. [PMID:20625546](https://pubmed.ncbi.nlm.nih.gov/20625546/); [PMID:16707503](https://pubmed.ncbi.nlm.nih.gov/16707503/).

The proposed CP-specific inhibitor term follows the existing [CARMIL2 proposal](../CARMIL2/CARMIL2-ai-review.yaml). The official [GO:0140678 definition and descendants](https://amigo.geneontology.org/amigo/term/GO:0140678) cover direct noncovalent inhibition of target activities, including nonenzymatic ligand/transporter examples; the page's enzyme-only comment does not justify assigning enzyme activity to CP. [GO:0051016](https://amigo.geneontology.org/amigo/term/GO:0051016) names the act of capping, while [GO:2000813](https://amigo.geneontology.org/amigo/term/GO:2000813) negatively regulates that process. Their regulation relation is not an is-a equivalence. No redundant NEW capping row is added: the existing broad process rows are refined, and the inhibitor specificity gap is recorded as a proposed term. The earlier same-role comparator observations (ADD1, TWF1 and CAPG) support a specific capping annotation; they were not a reason to leave the mechanism unrepresented.

The nuclear-envelope lumen electronic row is now over-annotated at its compartmental precision. A cytoplasmic adaptor with no annotated signal peptide or transmembrane feature and perinuclear staining lacks demonstrated luminal topology; this does not establish absolute biological impossibility or invalidate the underlying microscopy. SH3-domain recognition and the broad structural-constituent assertion remain supported non-core annotations. The structural term is not restricted to polymer subunits, but junctional knockdown necessity alone does not establish its molecular mechanism. The core now records direct filament binding/capping, partner assembly and CPI-mediated CP inhibition separately. The human mutation abstract supplies an additional limited F-actin-binding anchor, and GO:0003779 to GO:0051015 is explicitly a collapse/refinement, not a new assertion. [PMID:17713465](https://pubmed.ncbi.nlm.nih.gov/17713465/).

The earlier journal's unexplained “T” denotes the computational reviewer assigned the bounded source consultation, not a biological source or an experimenter. Its historical sentence remains in the unchanged prefix; the biological judgments above are grounded in the named papers. New prose here avoids repeating source-access bookkeeping for every unchanged partner.
