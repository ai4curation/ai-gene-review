# SOD1 (human) — research notes

UniProt: P00441 (SODC_HUMAN). HGNC:11179. 154 aa. EC=1.15.1.1 (Cu-Zn superoxide dismutase).
Chromosome 21. Erythrocyte/cytosolic enzyme; one of the most abundant cytosolic proteins.

## Core enzymatic function
- Cu/Zn superoxide dismutase: catalyzes 2 superoxide + 2 H+ = H2O2 + O2 (RHEA:20696, EC 1.15.1.1)
  [UniProt P00441 CATALYTIC ACTIVITY; ECO:0000269|PubMed:24140062].
- "Destroys radicals which are normally produced within the cells and which are toxic to biological
  systems" [UniProt FUNCTION, PubMed:24140062].
- Binds 1 copper ion + 1 zinc ion per subunit; copper is catalytic, zinc structural
  [UniProt COFACTOR, PubMed:17888947 "Binds 1 copper ion per subunit"; "Binds 1 zinc ion per subunit"].
- Homodimer, non-disulfide-linked; unusually stable quaternary structure controlled by metal occupancy
  and disulfide status [UniProt SUBUNIT; PubMed:15326189].
- Newer (2023) activity: also oxidizes hydrogen sulfide (H2S) to sulfate, EC 1.8.-.-, a H2S/RSS
  detoxifying role [UniProt; PubMed:36630448 — abstract not cached but UniProt-curated].

## Metal binding details
- [PMID:17381088 "The apparent thermodynamics of zinc binding to the apoproteins were favorable
  (Ka > 10^8 M-1)"] — zinc binding to apo-SOD1; structural/stability role; IDA zinc ion binding.
- [PMID:17008312 "the likely source of copper for assembly of cytochrome c oxidase (CcO) and
  superoxide dismutase 1 (Sod1) within the intermembrane space (IMS)"] — copper supply; supports
  copper ion binding (IDA). Note: this paper localizes Sod1 metallation to IMS, NOT matrix; the
  GOA "mitochondrial matrix" NAS annotation from this PMID is a misread (the CuL complex is in matrix,
  but SOD1 itself is in IMS/cytosol).

## Copper chaperone (CCS) / maturation
- [PMID:9726962 "CCS and SOD1 directly interact in vitro and in vivo and that this interaction is
  mediated via the homologous domains"] — SOD1 binds its copper chaperone CCS (chaperone binding).
- [PMID:30735496] hCCS catalyses SOD1 folding, copper insertion, disulfide formation; structures of
  reaction precursors/intermediates/products. Supports "superoxide dismutase copper chaperone complex"
  (GO:1902694, part_of).
- [PMID:31292775 "Ccs stably interacts with the cytosolic C-terminal tail of Ctr1 ... This interaction
  becomes tripartite ... the activation of the target (Sod1) regulates the Ccs·Ctr1 interaction"] —
  SOD1:CCS:Ctr1 heterotrimer; SOD1 activation terminates the interaction. Protein binding (CCS).
- [PMID:24026195 "both localize to the cytosol and the mitochondrial intermembrane space where they
  specifically counteract mitochondria-derived superoxide ... CCS1 import parallels SOD1 import"] —
  CCS-dependent oxidation-coupled import of SOD1 into mitochondrial IMS. Supports IMS localization (IDA).
- [PMID:24567322] DJ-1 (PARK7) is a copper chaperone activating SOD1 — supports SOD activity (IDA) and
  removal of superoxide radicals (IDA), and copper delivery.

## Subcellular localization
- Primary: cytosol/cytoplasm. [PMID:1332049 "Cu,Zn-SOD was found widely distributed in the cell cytosol
  and in the cell nucleus ... Mitochondria and secretory compartments did not label for this protein.
  ... peroxisomes showed a labeling density slightly less than that of cytoplasm"] — strongly supports
  cytosol + nucleus; argues AGAINST mitochondrion/secretory; peroxisome labeling near background.
- Also nucleus [PMID:22496122 palmitoylation Cys-7 helps nuclear targeting; UniProt SUBCELLULAR LOCATION
  "Nucleus {PubMed:22496122}"].
- A minor pool in mitochondrial intermembrane space (IMS), delivered via CCS [PMID:24026195;
  PMID:17008312]. Reactome R-HSA-3777112 SOD1 dismutation in IMS.
- Secreted/extracellular pool: SOD1 detected extracellularly/in exosomes [PMID:9453566 blood;
  PMID:23533145, PMID:19056867 urinary/prostatic exosomes — HDA proteomics]. Minor, non-core.
- Plasma membrane colocalization on endocytosis into endothelial cells [PMID:17077646 "Rapid endocytosis
  of copper-zinc superoxide dismutase into human endothelial cells"].

## Oxidative-stress defense / downstream processes
- [PMID:16790527 "Superoxide dismutases (SODs) represent the first line of defense against oxidative
  stress ... SOD1 down-regulation ... superoxide increase ... mitochondria were significantly affected
  with impairment of the mitochondrial transmembrane potential"] — supports removal of superoxide
  radicals (IDA), response to superoxide (IDA), regulation of mitochondrial membrane potential (IMP),
  redundancy of SOD1 in redox homeostasis.
- [PMID:12551919] CuZn-SOD overexpression modulates hydroperoxide-induced apoptosis in PC-12 — supports
  superoxide metabolic process (IDA); apoptosis effects are downstream/context-specific.
- [PMID:24140062 "SOD1 is succinylated and that succinylation decreases its activity. SIRT5 binds to,
  desuccinylates and activates SOD1 ... SOD1-mediated ROS reduction is increased"] — SOD activity (IDA),
  reactive oxygen species metabolic process (IDA), hydrogen peroxide biosynthesis (product of SOD).

## Moonlighting / interactions (mostly non-core)
- [PMID:18219391 "SOD1 is not just a catabolic enzyme, but can also directly regulate NADPH oxidase ...
  by binding Rac1 and inhibiting its GTPase activity"] — small GTPase binding (Rac1), regulation of
  GTPase activity, positive regulation of superoxide anion generation (via Nox). Real but specialized.
- [PMID:17324120 "native ... human ... SOD1 ... activated Cn (calcineurin) ... depends on direct
  SOD1-Cn protein interactions"] — protein phosphatase 2B (calcineurin) binding. Direct, specialized.
- [PMID:26643113 "α-synuclein and SOD1 physically interact ... promotes its oligomerization"] —
  protein binding (disease context).
- [PMID:12968035] Murr1/COMMD1–Wilson disease protein paper; SOD1 IPI listed in GOA but this paper is
  about copper toxicosis, peripheral. Generic protein binding.

## ALS / disease (gain-of-function; downstream of core enzyme)
- [PMID:17504823 "ALS ... linked to mutations of superoxide dismutase type-1 (SOD1), an antioxidant
  enzyme whose activity is preserved in most mutant forms ... gain of a loss of function"] — ALS is a
  toxic gain-of-function (misfolding/aggregation), NOT loss of dismutase activity. Localization: wtSOD1
  cytoplasm + nuclei; mutant mainly cytoplasmic.
- [PMID:24023695] HSJ1/DNAJB2 chaperone reduces mutant SOD1 aggregation in SOD1(G93A) mice — chaperone
  interaction; nucleus/cytoplasm localization (IDA in mouse model).
- Many interactome/aggregation papers (PMID:16369483, 16595634, 19171884, 21252941, 23831581, 19022905,
  19369197, 19828437, 21257910, 31999698, 32814053, 29128334, 33961781, 28514442, 20195357, 24981860,
  24234043) — generic "protein binding" IPI, largely high-throughput or aggregation-context; non-core.

## Bioinformatic-only / orthology-transfer (ISS GO_REF:0000024, IEA GO_REF:0000107) processes
- Large set of organismal/physiological process terms transferred from orthologs (mouse Sod1 KO
  phenotypes): ovarian follicle development, placenta development, retina homeostasis, myeloid cell
  homeostasis, spermatogenesis, embryo implantation, sensory perception of sound, locomotory behavior,
  regulation of blood pressure, response to heat/ethanol/H2O2/copper/cadmium/ATP/K+/CO/amphetamine/
  antipsychotic, thymus development, T-cell differentiation, neurofilament organization, PNS myelin
  maintenance, vascular smooth-muscle relaxation, stereocilium organization, heart contraction, etc.
  These reflect pleiotropic phenotypes of Sod1-null mice / overexpression and are downstream of the
  core antioxidant function. Keep as NON_CORE (or REMOVE if unsupported/over-specific).
- Mouse Sod1-/- phenotypes (hepatocellular carcinoma, reduced fertility, hearing loss, accelerated
  aging) are well documented and underlie many of these transfers; they are genuine consequences of
  lost antioxidant protection but are not the molecular "core function."

## Key conclusions for review
- CORE: superoxide dismutase activity (GO:0004784); copper ion binding (GO:0005507); zinc ion binding
  (GO:0008270); removal of superoxide radicals (GO:0019430) / superoxide metabolic process (GO:0006801);
  cytosol (GO:0005829); homodimerization (GO:0042803). Nucleus is a genuine secondary localization.
- IMS (GO:0005758) is a real minor catalytic location (IDA, Reactome).
- Avoid endorsing bare GO:0005515 protein binding; KEEP_AS_NON_CORE at most, note more informative
  partners where direct (CCS chaperone binding, Rac1, calcineurin).
- Mitochondrion (whole) and peroxisome are largely IBA/IEA over-annotations; PMID:1332049 explicitly
  found mitochondria/secretory compartments did NOT label and peroxisome ~background. Mark accordingly.
