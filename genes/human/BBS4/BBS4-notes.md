# BBS4 (Q96RK4) curation notes

## Identity / structure
- Human BBS4, 519 aa, UniProt Q96RK4; HGNC:969; gene on chr 15.
- TPR (tetratricopeptide-repeat) superhelical protein: UniProt annotates 10 TPR repeats (positions ~67–408); InterPro IPR011990/IPR019734; PANTHER PTHR44186:SF1 (BBS4). Belongs to the BBS4 family.
- Resolved in cryo-EM structure of the BBSome (PDB 6XT9, chain D). TCDB 3.A.33.1.1 "BBSome complex family"; ComplexPortal CPX-1908 BBSome.
- Disordered N-term (1–25) and C-term (440–519). REGION 1..66 and 338..519 "required for localization to centrosomes"; REGION 101..337 "Interaction with PCM1" [UniProt FT, ECO:0000269|PubMed:15107855].
- 3 isoforms; isoform 3 lacks aa 1–172 (loses N-terminal half incl. several TPRs).

## Core biology
BBS4 is a core subunit of the **BBSome** (8-subunit complex: BBS1, BBS2, BBS4, BBS5, BBS7, BBS8/TTC8, BBS9, BBIP1/BBIP10). The BBSome is a coat-like cargo adaptor that sorts membrane proteins into/out of the primary cilium via IFT, working with the small GTPase ARL6/BBS3 and Rabin8/Rab8.

- BBSome composition + function + ciliary membrane localization: [PMID:17574030 "Here we identify a complex composed of seven highly conserved BBS proteins. This complex, the BBSome, localizes to nonmembranous centriolar satellites in the cytoplasm but also to the membrane of the cilium... required for ciliogenesis but is dispensable for centriolar satellite function... mediated in part by the Rab8 GDP/GTP exchange factor"]. This paper IDed BBSome by MS and assigned subcellular location (centriolar satellites + ciliary membrane). It is the source for alpha-/beta-tubulin binding IDA annotations and BBSome part_of IDA.
- BBSome assembly order — BBS4 is added LAST onto the BBS7-BBS2-BBS9 core, after BBS1/BBS5/BBS8: [PMID:22500027 "BBS1, BBS5, BBS8, and finally BBS4 are added to the BBSome core to form the complete BBSome"]. Chaperonin BBS6/10/12 + CCT/TRiC required for assembly [PMID:20080638].

## BBS4-specific functions (the adaptor/PCM1 role)
- BBS4 as dynein/p150glued adaptor recruiting PCM1 to centriolar satellites: [PMID:15107855 "BBS4 localizes to the centriolar satellites of centrosomes and basal bodies of primary cilia, where it functions as an adaptor of the p150(glued) subunit of the dynein transport machinery to recruit PCM1 (pericentriolar material 1 protein) and its associated cargo to the satellites. Silencing of BBS4 induces PCM1 mislocalization and concomitant deanchoring of centrosomal microtubules, arrest in cell division and apoptotic cell death"]. Source of: protein-macromolecule adaptor activity (IMP), dynactin binding (IDA), microtubule anchoring at centrosome (IMP), PCM1/DCTN1 interaction, centriolar satellite/PCM/centriole/basal body localization, cell-cycle/cytokinesis phenotypes (centrosome cycle IMP, mitotic cytokinesis IMP, regulation of cytokinesis IMP, protein localization to centrosome IMP).
  - NOTE: the cytokinesis/cell-division-arrest/apoptosis effects are downstream secondary consequences of PCM1 mislocalization and MT de-anchoring on RNAi; these are over-annotations of the molecular role rather than direct BBS4 functions.
- DISC1 + BBS4 cooperatively recruit PCM1 (and ninein) to the centrosome; relevant to corticogenesis/neuronal migration: [PMID:18762586 "DISC1 and BBS4 are required for targeting PCM1 and other cargo proteins, such as ninein, to the centrosome in a synergistic manner. In the developing cerebral cortex, suppression of PCM1 leads to neuronal migration defects, which are phenocopied by the suppression of either DISC1 or BBS4"]. Source of centrosome IDA (PMID:18762586) and protein binding IPI.
- AZI1/CEP131 (centriolar satellite protein) interacts with BBSome via BBS4 and negatively regulates BBSome ciliary trafficking: [PMID:24550735 "AZI1 (also known as CEP131), interacts with the BBSome and regulates BBSome ciliary trafficking activity... AZI1 interacts with the BBSome through BBS4... accumulation of the BBSome in cilia is enhanced upon AZI1 depletion"]. Source of BBSome part_of IDA, centrosome IDA, cilium IDA, centriolar satellite IDA, protein binding IPI (PMID:24550735).
- BBIP10/BBIP1 is a BBSome subunit; BBSome functions in membrane trafficking to/inside primary cilium; BBIP10 (not BBS4) couples MT acetylation: [PMID:19081074 "seven highly conserved BBS proteins form a stable complex, the BBSome, that functions in membrane trafficking to and inside the primary cilium"]. Source of BBSome IPI, ciliary membrane IDA, cilium assembly NAS (PMID:19081074). The microtubule-stability/acetylation function in the title belongs to BBIP10, not BBS4.
- CEP290 interaction; BBS4 modifies CEP290 ciliopathy expression: [PMID:23943788 full text available]. Source of cilium IDA, centriolar satellite IDA, ciliary transition zone IDA, protein localization to cilium IMP, protein binding IPI.
- NPHP5/CEP290 regulate BBSome integrity & cargo delivery [PMID:25552655] — protein binding IPI.
- BBS1/BBS3 regulate ciliary trafficking of PKD1; BBS4 interacts with PKD1 [PMID:24939912] — protein binding IPI.

## Transcriptional regulation claim
- [PMID:22302990 "BBS7 ... probably has a nuclear role ... interacts physically with the polycomb group (PcG) member RNF2 ... our data supports a similar role for other BBS proteins"]. Primarily a BBS7 study; "RNA polymerase II-specific DNA-binding transcription factor binding" IPI (MGI) for BBS4 rests on weak generalization. The nucleus IEA (GOC inter-ontology) and transcription-factor-binding IPI are poorly supported as a core function. Treat as non-core/uncertain.

## Other annotations
- Many ISS (GO_REF:0000024) developmental/neurological/sensory process terms transferred from mouse ortholog (Q8C1Z7): heart looping, neural tube closure, retina homeostasis, spermatid development, smell, dendrite/striatum/hippocampus/cerebral cortex/brain development, adult behavior, fat cell differentiation, lipid metabolism regulation, photoreceptor maintenance, retinal rod development, melanosome transport, leptin appetite regulation. These reflect BBS mouse-model phenotypes — pleiotropic ciliopathy downstream effects, not direct molecular functions. KEEP_AS_NON_CORE for the credible ciliopathy-related ones.
- Melanosome transport (ISS): zebrafish bbs4 morphants show melanosome transport delay [PMID:24550735]; classic BBS assay. Plausible as non-core developmental/transport readout.
- DLEC1 interaction [PMID:33144677] — mouse spermatogenesis paper; protein binding IPI.
- Numerous high-throughput interactome IPI protein binding annotations (25416956, 26871637, 27173435, 29039417, 32296183, 32814053, 33961781, 40205054, 18000879=ALDOB, 16327777=CCDC28B). All "protein binding" GO:0005515 — uninformative MF; keep but flag.

## Curation strategy summary
- CORE molecular function: protein-macromolecule adaptor activity (GO:0030674) — BBSome cargo adaptor / dynein-PCM1 adaptor. KEEP. Plus the experimentally grounded tubulin/dynactin binding.
- CORE cellular components: BBSome (GO:0034464), centriolar satellite, ciliary membrane, basal body, centrosome, cilium. KEEP experimental ones.
- CORE process: protein localization to cilium / cilium assembly / protein localization to centrosome (PCM1 recruitment), microtubule anchoring at centrosome.
- GO:0005515 protein binding: uninformative per guidelines — mark over-annotated (not core), but do not remove experimental IPIs casually.
- Cell-cycle/cytokinesis terms: secondary RNAi consequences -> MARK_AS_OVER_ANNOTATED.
- nucleus / transcription factor binding: weak; UNDECIDED/non-core.
- ISS pleiotropic developmental terms: KEEP_AS_NON_CORE.
</content>
