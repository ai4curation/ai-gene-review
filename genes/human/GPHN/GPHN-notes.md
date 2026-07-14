# GPHN (Gephyrin) — review notes

UniProt: Q9NQX3 (GEPH_HUMAN), 736 aa, chromosome 14. HGNC:15465.

## Summary of function

GPHN encodes gephyrin, a **bifunctional (moonlighting) protein** with two independent, well-established core roles:

1. **Enzyme: final two steps of molybdenum cofactor (MoCo) biosynthesis.** The N-terminal G domain has **molybdopterin adenylyltransferase activity** (adenylylates molybdopterin to MPT-AMP; EC 2.7.7.75; GO:0061598) and the C-terminal E domain has **molybdopterin molybdotransferase activity** (inserts molybdenum to form MoCo; EC 2.10.1.1; GO:0061599). MoCo is the prosthetic group of sulfite oxidase, xanthine oxidase/dehydrogenase, aldehyde oxidase and mARC. Loss causes molybdenum cofactor deficiency type C (MOCODC, MIM:615501).
2. **Scaffold: master organizer of inhibitory (glycinergic + GABAergic) postsynapses.** Gephyrin clusters glycine receptors (GlyR) and major subsets of GABA type A receptors at the postsynaptic membrane, anchoring them to the cytoskeleton. Loss/dysfunction causes hyperekplexia and epilepsy phenotypes.

The two functions are physically and functionally separable: the MOCODC variant D580A (E domain) abolishes MoCo synthesis but still forms normal postsynaptic clusters, whereas the Dravet-like G375D variant abolishes both.

## Key provenance

### Enzymatic / MoCo function
- [file:human/GPHN/GPHN-uniprot.txt "Also has a catalytic activity and catalyzes two steps in the"] and next lines: "biosynthesis of the molybdenum cofactor. In the first step, molybdopterin is adenylated. Subsequently, molybdate is inserted into adenylated molybdopterin and AMP is released."
- UniProt CATALYTIC ACTIVITY: EC=2.7.7.75 (MPT + ATP -> adenylyl-MPT + PPi; RHEA:31331) and EC=2.10.1.1 (adenylyl-MPT + molybdate -> Mo-MPT + AMP; RHEA:35047).
- UniProt REGION: 326..736 = "MPT adenylyltransferase" (G domain, C-terminal in this numbering); 14..166 = "MPT Mo-transferase" (E domain). N-terminal MoaB/Mog family; C-terminal MoeA family.
- [PMID:9990024 "gephyrin binds with high"] affinity to molybdopterin (abstract); [PMID:9990024 "gephyrin expression can reconstitute Moco"] biosynthesis in Moco-deficient bacteria, a molybdenum-dependent mouse cell line, and a Moco-deficient plant mutant. This is the original human-gephyrin reconstitution/complementation paper (IMP/IDA basis for GO:0006777, GO:0043546).
- [PMID:23163752 "combining two enzymatic functions within the"] biosynthesis of the Moco; "over 300-fold increase in Moco synthesis for gephyrin compared with the isolated G domain, which synthesizes adenylylated molybdopterin, and E domain, which catalyses the metal insertion". Demonstrates in-vitro two-step MoCo synthesis and product-substrate channelling from domain fusion.
- [PMID:26613940 "catalyzes the synthesis of the molybdenum cofactor"]; the G375D variant is [PMID:26613940 "enzymatically inactive and unable to catalyze MoCo biosynthesis"], matching MOCODC control D580A.

### Synaptic scaffold function
- [file:human/GPHN/GPHN-uniprot.txt "Microtubule-associated protein involved in membrane protein-"] cytoskeleton interactions; "anchor the inhibitory glycine receptor (GLYR) to subsynaptic microtubules"; "Acts as a major instructive molecule at inhibitory synapses, where it also clusters GABA type A receptors".
- [PMID:26613940 "Gephyrin is the major postsynaptic scaffolding protein at inhibitory synapses"]; it directly binds and [PMID:26613940 "organizes GABAA and glycine receptors"] and "regulates clustering and diffusion of these receptors."
- [PMID:25025157 "Gephyrin anchors major subsets of GABAARs in the postsynaptic membrane"]. Palmitoylation at Cys212/Cys284 (by ZDHHC12/DHHC-12) controls membrane association and clustering; [PMID:25025157 "palmitoylation of gephyrin is essential for postsynaptic cluster formation in neurons"]. Cys->Ser mutants reduce GABAAR clustering (IMP basis for GO:0097112, GO:0030674).
- [PMID:26613940 "GFP‐G375D was diffusively distributed in neurons and filled all cellular compartments"]; G375D acts dominant-negatively, decreasing GABAAR surface expression and mIPSC amplitude (IDA basis for GO:0097112 and dendrite/postsynaptic-membrane localization).

### Localization
- [PMID:22270318 "gephyrin localizes to the cytoplasm of both tissue hepatocytes and cultured"] immortalized cells; [PMID:22270318 "gephyrin is indispensible for the biosynthesis of molybdenum cofactor"] in non-neuronal tissues (cytosolic IDA GO:0005829).
- UniProt SUBCELLULAR LOCATION: Postsynaptic cell membrane (lipid-anchor, cytoplasmic side); Cytoplasm, cytosol; Cytoplasm, cytoskeleton; Cell projection, dendrite; Postsynaptic density; forms clusters at synapses.

### Interactions (IPI protein binding)
- DYNLL1 (dynein light chain LC8, P63167) is a validated gephyrin interactor (UniProt INTERACTION: Q9NQX3;P63167 DYNLL1, NbExp=5). The five IntAct IPI annotations (PMID:21094642, 27173435, 33961781, 35271311, 40205054) all record with/from UniProtKB:P63167 (DYNLL1). PMID:21094642 is a structural modelling paper explicitly about DYNLL1 with gephyrin; the others are large-scale interactome/organelle maps (BioPlex/OpenCell/multimodal cell maps) where GPHN is one of many baits/preys.
- GABRA3 (P34903) and GLRB (P48167) interactions are experimentally supported (PMID:26613940 IPI) and underlie the receptor-clustering function.

## Curation reasoning highlights
- Two catalytic MFs (GO:0061598, GO:0061599) and MoCo BP (GO:0006777) are CORE (enzymatic moonlighting function).
- Receptor clustering (GO:0097112 GABAAR, GO:0072579 GlyR) + protein-macromolecule adaptor activity (GO:0030674) are CORE (synaptic scaffold function). Postsynaptic membrane / inhibitory synapse localization is CORE for this role.
- `nitrate reductase activity` (GO:0008940, IMP PMID:9990024, CAFA) is a MoCo-reconstitution *readout* (Nia1 plant nitrate reductase complementation assay), not a gephyrin enzymatic activity — MARK_AS_OVER_ANNOTATED (experimental, do not REMOVE).
- Bare `protein binding` (GO:0005515) IPI annotations → MARK_AS_OVER_ANNOTATED (uninformative; DYNLL1/GABRA3/GLRB partners captured in core functions/notes).
- Generic IEA terms (`catalytic activity`, `molecular adaptor activity`, `signaling receptor binding`, `establishment of protein localization`, `protein localization to membrane`, `synapse organization`) → over-annotated or non-core generalizations; better specific terms exist and are separately annotated.
