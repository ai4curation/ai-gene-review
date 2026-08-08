# FANCA (human) — gene review notes

UniProt: O15360 (FANCA_HUMAN), 1455 aa. Gene on 16q24.3. Synonyms FAA, FACA, FANCH.
Accounts for ~60-65% of Fanconi anemia cases.

## Summary of function
FANCA is one of the eight Fanconi anemia (FA) proteins (FANCA, B, C, E, F, G,
L/PHF9, M) that assemble into the multisubunit **FA core complex** (FA nuclear
complex; GO:0043240; ComplexPortal CPX-6263 "Fanconi anemia ubiquitin ligase
complex"). The core complex is a nuclear E3 ubiquitin-ligase assembly (catalytic
RING subunit = FANCL, E2 = UBE2T/FANCT) that, in response to DNA interstrand
crosslinks (ICLs) encountered during replication, monoubiquitinates the
FANCD2-FANCI (ID2) heterodimer. Monoubiquitinated ID2 is loaded onto chromatin
and coordinates downstream nucleolytic incision, translesion synthesis (TLS), and
homologous-recombination repair. FANCA itself is not the catalytic subunit; it is
a large scaffolding/docking subunit and the principal protein-protein interaction
hub of the core complex.

## Key provenance

### Positional cloning / identity
- [PMID:8896564 "The gene encodes a protein of 1,455 amino acids that has no significant homology to any other known proteins, and may therefore represent a new class of genes associated with the prevention or repair of DNA damage."]

### Nuclear complex membership (GO:0043240)
- [PMID:9398857 "we demonstrate the FAA and FAC bind each other and form a complex"] and
  [PMID:9398857 "the FAA-FAC complex is found in similar abundance in both cytoplasm and nucleus"]
- [PMID:11063725 "FANCF was found predominantly in the nucleus, where it complexes with FANCA, FANCC and FANCG"]
- [PMID:12649160 "The FANCA, FANCC, FANCE, FANCF, and FANCG proteins form a nuclear complex required for the monoubiquination of the FANCD2 protein"]
- [PMID:22343915 "We show that FAAP20 is an integral component of the FA nuclear core complex. We identify a region on FANCA that physically interacts with FAAP20, and show that FANCA regulates stability of this protein."]
- [PMID:22266823 "We identified Fanconi anemia-associated protein (FAAP20), an integral subunit of the multisubunit Fanconi anemia core complex. FAAP20 binds to FANCA subunit and is required for stability of the complex and monoubiquitination of FANCD2."]
- UniProt SUBUNIT: "Belongs to the multisubunit FA complex composed of FANCA, FANCB, FANCC, FANCE, FANCF, FANCG, FANCL/PHF9 and FANCM."

### Interstrand cross-link repair (GO:0036297) / DNA repair (GO:0006281)
- [PMID:19965384 "A central event in the activation of the Fanconi anemia pathway is the mono-ubiquitylation of the FANCI-FANCD2 complex"] — FANCA is a core-complex subunit required for this activation.
- [PMID:22266823 "the FA proteins cooperate in a DNA damage response (DDR) pathway required for DNA interstrand crosslink repair"] and
  [PMID:22266823 "Eight of the FA proteins comprise the FA core complex, a multisubunit complex required for DNA damage recognition at a stalled replication fork"]

### Subcellular location
- Nucleus (major functional form) and cytoplasm (minor form):
  UniProt SUBCELLULAR LOCATION "Nucleus. Cytoplasm. Note=The major form is nuclear. The minor form is cytoplasmic."
- [PMID:9398857 "Although unbound FAA and FAC localize predominantly to the cytoplasm, the FAA-FAC complex is found in similar abundance in both cytoplasm and nucleus"]
- Nuclear localization + phosphorylation required for function (UniProt refs PMID:9742112, PMID:9789045; NLS motif 18-34).
- Chromatin loading is DNA-damage-induced: [PMID:22343915 "the FAAP20-UBZ domain ... is required for DNA-damage-induced chromatin loading of FANCA and the functional integrity of the FA pathway"]

### Protein interactions (all GO:0005515 protein binding — uninformative MF; scaffold/hub role)
FANCA is the central interaction hub of the core complex. Verified partners in cached lit:
- FANCG (O15287): [PMID:10627486 "found a strong interaction between FANCA and FANCG proteins"];
  [PMID:10652215 "a high level of activation was found when FANCA was co-expressed with FANCG, indicating strong, direct interaction between these proteins"];
  [PMID:12649160 "FANCG was shown to interact with both the amino-terminus of FANCA"]
- FANCF (Q9NPI8): [PMID:11063725 "complexes with FANCA, FANCC and FANCG"]
- FAAP24 (via FANCM), FAAP100 (Q0VG06): [PMID:17396147 "FAAP100 is essential for activation of the Fanconi anemia-associated DNA damage response pathway"]; [PMID:17289582] FAAP24 targets FANCM.
- FAAP20/C1orf86 (Q6NZ36): [PMID:22343915], [PMID:22705371 "FAAP20, a component of the FA core complex"], [PMID:22266823 "FAAP20 binds to FANCA subunit"]
- SMARCA4/BRG1 (P51532), SWI/SNF: [PMID:11726552 "We identified an interaction between the FA protein, FANCA and brm-related gene 1 (BRG1) product"]; [PMID:11726552 "we demonstrated co-localization in the nucleus between transfected FANCA and BRG1"]
- ERCC4/XPF (Q92889) + nonerythroid αII-spectrin: [PMID:12571280 "alphaSpIISigma*, FANCA and XPF co-immunoprecipitate with each other from normal human nuclear proteins"]
- GRB2 (P62993): SH3 peptide-array screen [PMID:17474147] — high-throughput, peripheral.
- Large-scale interactome / proteomics screens (FANCG or FAAP100 baits): PMID:16189514, PMID:28514442, PMID:32814053, PMID:33961781, PMID:35271311, PMID:37398436, PMID:40205054 — high-throughput, uninformative.

### regulation of regulatory T cell differentiation (GO:0045589, IBA)
Phylogenetic (PANTHER/GO_Central) inference seeded from mouse Fanca (MGI:1341823).
Peripheral/pleiotropic; not a core molecular function of the DNA-repair scaffold.
Treat as non-core.

### protein-containing complex assembly (GO:0065003, TAS PMID:9398857)
FANCA is required for formation/stability of the FA core complex (binds FANCG/FANCF/FAAP20;
regulates FAAP20 stability). Genuine but essentially a restatement of complex membership.

## Structure
Cryo-EM structures of the human FA core complex: PDB 7KZP/7KZQ/7KZR/7KZS/7KZT/7KZV
(1-1455). FANCA is largely α-helical (Pfam FANCA_arcN, FANCA_helical, FANCA_CTD, Fanconi_A_N).

## Action plan for annotations
- GO:0043240 FA nuclear complex (IBA/IEA/NAS/IDA x7): ACCEPT (core; must be consistent).
- GO:0005515 protein binding (all IPI): MARK_AS_OVER_ANNOTATED (uninformative; hub role captured in core_functions/notes).
- GO:0036297 ICL repair (IEA/NAS): ACCEPT (core BP).
- GO:0006281 DNA repair (TAS): ACCEPT (correct broader BP).
- GO:0005634 nucleus (IEA/IDA/TAS): ACCEPT (functional location).
- GO:0005654 nucleoplasm (IDA/TAS x10): ACCEPT.
- GO:0000785 chromatin (IDA): ACCEPT (DNA-damage-induced loading).
- GO:0005737 cytoplasm (IEA/TAS): KEEP_AS_NON_CORE (minor/inactive form).
- GO:0005829 cytosol (TAS): KEEP_AS_NON_CORE.
- GO:0065003 complex assembly (TAS): ACCEPT.
- GO:0045589 Treg differentiation (IBA): KEEP_AS_NON_CORE (pleiotropic, mouse-ortholog-derived).
