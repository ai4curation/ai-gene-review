# SepJ (FraG, alr2338) — research notes

UniProt: **A0ACD7RSI0** (unreviewed), 751 aa. Gene *sepJ* = *fraG* = locus **alr2338**,
Nostoc/Anabaena sp. PCC 7120 (NCBITaxon:103690). SepJ is one of the best-studied septal
proteins of filamentous, heterocyst-forming cyanobacteria.

## Discovery and naming
- The gene was identified independently and near-simultaneously by two groups. Flores et al.
  named it *sepJ* for its **sep**tal localization [PMID:17369306 "the sepJ gene (open reading
  frame alr2338 of the Anabaena sp. genome)"], while Nayar et al. named it *fraG* from a
  filament-fragmentation screen [PMID:17259632 "The gene alr2338 (designated fraG herein),
  located immediately upstream of the master regulator of differentiation hetR"]. The two
  names refer to the same locus; *sepJ* is the more widely used designation.
- Both groups reported the same core mutant phenotype: filament fragmentation, failure to
  synthesize heterocyst-specific glycolipids, and inability to grow diazotrophically
  [PMID:17369306 "SepJ is a novel composite protein needed for filament integrity, proper
  heterocyst development, and diazotrophic growth."] [PMID:17259632 "fraG appears to play a
  role in filament integrity and differentiation of proheterocysts into mature heterocysts."].

## Protein family / domain architecture (EamA / DMT superfamily)
SepJ is a **three-domain (multidomain) protein** [PMID:21299655 "SepJ is a protein
conspicuously located at the cell poles in the intercellular septa of the filaments that has
three well-defined domains: an N-terminal coiled-coil domain, a central linker and a
C-terminal permease domain."]:
- **N-terminal coiled-coil domain** (~aa 28–207): strongly conserved; mediates
  cell-cell anchoring and peptidoglycan interaction.
- **Central linker** (~aa 208–401): not conserved in sequence but Pro/Ser/Thr-rich;
  dispensable for function in the domain-swap experiments.
- **C-terminal integral-membrane permease domain** (~aa 412–751): resembles an export
  permease [PMID:17369306 "SepJ is a multidomain protein whose N-terminal region is
  predicted to be periplasmic and whose C-terminal domain resembles an export permease."].

The C-terminal permease domain is annotated by InterPro as an **EamA domain (IPR000620)**,
Pfam **PF00892 (EamA-like transporter)**, PANTHER **PTHR22911 ("Diverse Metabolite
Transporter Superfamily")** — i.e. the **DMT / drug-metabolite transporter (EmrE/EamA)
superfamily** of small-molecule permeases. This is the InterPro/PANTHER signature that drives
the single existing GOA IEA annotation (GO:0016020 membrane).

Domain-dissection experiments show the two functional modules are separable
[PMID:21299655 "the coiled-coil domain is required for polar localization of SepJ, filament
integrity, normal intercellular transfer of small fluorescent tracers and diazotrophy."] and
that they carry distinct functions [PMID:21299655 "SepJ provides filamentous cyanobacteria
with a cell-cell anchoring function, but the permease domain has evolved in heterocyst formers
to provide intercellular molecular exchange functions required for diazotrophy."].

## Subcellular localization
SepJ localizes as a focused spot at the **intercellular septa (cell poles)** and forms a ring
at the division site during cytokinesis [PMID:17369306 "the protein is localized at the
intercellular septa, and when cell division starts, it is localized in a ring whose position
is similar to that of a Z ring."]. GFP-fusion topology work indicates the C terminus is
cytoplasmic (SepJ is an integral cytoplasmic/inner-membrane protein), with the long
N-terminal extramembrane section extending toward the periplasm/septum. SepJ, FraC and FraD
are described together as cytoplasmic-membrane proteins located at the cell poles in the
septa [PMID:28979840 "SepJ (also known as FraG 13), FraC, and FraD are cytoplasmic membrane
proteins that are located at the cell poles in the intercellular septa of the filament"].

## Multimerization and peptidoglycan interaction
Native (blue-native) PAGE of Anabaena membranes shows SepJ in high-molecular-weight complexes
[PMID:28979840 "SepJ (predicted MW, 81.3 kDa) solubilized from Anabaena membranes was found
in complexes of about 296-334 kDa, suggesting that SepJ forms multimeric complexes."]. His-tag
pull-downs show that SepJ and its isolated coiled-coil domain bind peptidoglycan
[PMID:28979840 "pull-down experiments showed that His6-tagged versions of SepJ and of the SepJ
coiled-coil domain interact with Anabaena peptidoglycan (PG)."]. Together this supports SepJ
being a structural component of the septal junctions [PMID:28979840 "These observations
support the idea that SepJ is a component of the septal junctions that join the cells in the
Anabaena filament."].

## Role in intercellular communication and diazotrophy
SepJ is needed for the normal number of septal **nanopores** and for the intercellular
transfer of fluorescent tracers (calcein/FRAP). fraC/fraD mutants mislocalize SepJ and impair
tracer transfer [PMID:20487302 "The fraC and fraD mutants showed an impaired localization of
SepJ at the intercellular septa and were hampered in the intercellular transfer of the
fluorescent probe calcein."]. The permease domain's similarity to transporters, together with
its septal position, led to the hypothesis that SepJ participates in intercellular movement of
metabolites or regulators [PMID:17369306 "The similarity of the C-terminal domain of SepJ to
transporters, and the localization of this protein at the junction between cells, raises the
possibility that it is involved in the movement of metabolites or regulatory compounds between
neighboring cells."]. Note: **no specific transport substrate for the SepJ permease domain has
been established**, so a catalytic/transporter MF is not asserted as a core function here (the
structural/anchoring role dominates the evidence).

## The SepJ-vs-FraCD junction question
There is evidence for **at least two types of septal junctions** in Anabaena — those related
to SepJ and those related to FraCD [PMID:28979840 "Although both SepJ and the FraCD proteins
are required in Anabaena to produce a normal number of nanopores 16, there is evidence for the
existence of at least two types of septal junctions, those related to SepJ and those related
to FraCD 17."]. The recently resolved cryoET SJ structural core is built from **SepN (plug) +
FraD (anchor)** (PMID:36470860, PMID:42424141), and SepJ is not (yet) placed as a subunit of
that core complex. Whether SepJ forms the same channel as the FraCD/SepN complex or a distinct
but related junction remains unresolved; SepJ is best described as a **septal-junction-
associated / architectural** protein required for SJ formation, nanopore number and filament
integrity (consistent with `modules/septal_junction.yaml`, which groups SepJ/FraG among
associated septal proteins rather than as an asserted core subunit).

## Annotation summary (for the review)
- Existing GOA: **GO:0016020 membrane (IEA, GO_REF:0000120)** — correct but very general;
  MODIFY → **GO:0005886 plasma membrane** (SepJ is an integral cytoplasmic-membrane protein).
- NEW core annotations: **GO:0005198 structural molecule activity** (structural component of
  the septal junction; forms multimers; PG-binding coiled-coil), **GO:0007267 cell-cell
  signaling** (gated intercellular molecular transfer / cell-cell communication), and
  **GO:0030428 cell septum** (focused septal/cell-pole localization).
- Core function: structural molecule activity, involved_in cell-cell signaling, located_in
  plasma membrane + cell septum.

## Key references
- PMID:17369306 — Flores et al. 2007, J Bacteriol. Original *sepJ*; septal localization, Z-ring,
  filament integrity + diazotrophy; multidomain (permease-like C-terminus). Full text cached.
- PMID:17259632 — Nayar et al. 2007, Microbiology. Independent *fraG*; filament integrity +
  heterocyst maturation. Abstract only.
- PMID:21299655 — Mariscal et al. 2011, Mol Microbiol. Three-domain functional dissection;
  coiled-coil = anchoring, permease = intercellular exchange. Abstract only.
- PMID:20487302 — Merino-Puerto et al. 2010, Mol Microbiol. FraC/FraD required for SepJ
  localization, calcein transfer, filament integrity, diazotrophy. Abstract only.
- PMID:28979840 — Ramos-León et al. 2017, FEBS Open Bio. SepJ multimers + PG interaction;
  two-junction-types statement. Full text cached. PRIMARY for this review.
- PMID:36470860 / PMID:42424141 — SepN/FraD cryoET SJ core (context for SepJ-vs-FraCD).
