# ced-9 notes

## 2026-09-30 APOPTOSIS manual review

CED-9 is the C. elegans BCL2-family brake on canonical apoptosis. The supported
core is not Bax/Bak-like pore formation or cytochrome c release; it is physical
sequestration of CED-4 followed by EGL-1-dependent release. Early two-hybrid
and localization papers showed that CED-9 binds CED-4 [PMID:9024666, "Here we
show that CED-9 interacts physically with CED-4"] and retargets CED-4 to
intracellular membranes [PMID:9027313, "targeted CED-4 from the cytosol to
intracellular membranes"]. The structural and reconstitution work then made the
mechanism explicit: one CED-9 molecule binds the asymmetric CED-4 dimer,
prevents CED-4 from activating CED-3, and releases the dimer after EGL-1 binding
[PMID:16208361, "This specific interaction prevents CED-4 from activating
CED-3"; PMID:16208361, "EGL-1 binding induces pronounced conformational changes
in CED-9"].

- Generic `GO:0005515 protein binding` rows to EGL-1 were narrowed to
  `GO:0051434 BH3 domain binding`. EGL-1 binds CED-9 directly and that
  interaction is essential for CED-4 release in vivo [PMID:11027303, "direct
  physical interaction between EGL-1 and CED-9 is essential"], while the
  EGL-1/CED-9 structure explains this as BH3-helix recognition
  [PMID:15383288, "EGL-1 adopts an extended alpha-helical conformation"].
- Generic CED-4-binding rows were narrowed to
  `GO:0140311 protein sequestering activity`. The important CED-9 activity is
  holding CED-4 inactive before apoptosis, not binding a partner in the
  abstract.
- Mammalian BCL2-family transfers to `release of cytochrome c from
  mitochondria`, `channel activity`, `transmembrane transport`, and
  `extrinsic apoptotic signaling pathway in absence of ligand` were removed.
  Worm CED-9 sits at the mitochondrial outer membrane, but the CED-4/CED-3
  apoptosome is regulated by CED-4 sequestration and EGL-1 release, not by a
  receptor or cytochrome-c-to-APAF1 module.
- Broad apoptosis rows from MAC-1 and Salmonella experiments were modified to
  `negative regulation of apoptotic process`. MAC-1 may form a CED-4/CED-9
  complex [PMID:10101135, "also includes CED-3 or CED-9"], and ced-9(n1950)
  changes Salmonella-induced germline death [PMID:11226309, "Salmonella
  -induced apoptosis is substantially reduced in the ced-9(n1950) mutant"], but
  in both cases CED-9's direct role is CED-4/CED-3 restraint.
- The CSP-3 and CSP-2 protein-processing rows were removed. Those papers
  characterize CED-3 zymogen inhibitors, not CED-9 as a protein-processing
  regulator [PMID:18776901, "CSP-3 associates with the large subunit of the
  CED-3 zymogen"; PMID:19575016, "CSP-2 associates with the CED-3 zymogen"].
- Synapse-pruning annotations from Meng et al. were kept as non-core or
  tightened to `GO:1905808 positive regulation of synapse pruning`. The local
  axonal pathway really reuses EGL-1/CED-9/CED-4/CED-3 to eliminate
  presynaptic material through CED-3 cleavage of GSNL-1 [PMID:26074078, "four
  core components of the C. elegans apoptosis pathway are all required for
  elimination of transient presynaptic components"], but that is distinct from
  whole-cell death.
- Mitochondrial fission/fusion rows were kept as non-core. Tan et al. reported
  CED-9-dependent regulation of DRP-1 GTPase activity [PMID:18827010, "CED-9
  activates the GTPase activity of human DRP1"], and Lu et al. reported
  CED-9 interaction with DRP-1 [PMID:21949250, "CED-9 also physically interacts
  with the mitochondrial fission protein DRP-1"]. Breckenridge et al. argued
  from embryo morphology that `egl-1` and `ced-9` are not required for
  mitochondrial fission or fusion [PMID:19327994, "ced-9 is not required for
  either the mitochondrial fission or fusion process in C. elegans"], so this
  branch should stay separate from core apoptosis.
- The `apoptotic process involved in development` row from the PIG-1 cell
  extrusion paper is over-annotation for CED-9. `ced-9(gf)` is one of several
  blocked-canonical-apoptosis backgrounds that reveal PIG-1/PAR-4-dependent
  cell shedding [PMID:22801495, "a gain-of-function mutation of the bcl-2
  homolog ced-9 also produced shed cells"], while PIG-1 and the PAR-4 complex
  perform the extrusion/adhesion work.

