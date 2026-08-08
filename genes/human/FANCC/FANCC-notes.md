# FANCC (Q00597) — gene review notes

## Identity
- Human Fanconi anemia group C protein (FACC / FAC). UniProt Q00597, HGNC:3584, GeneID 2176, chr 9q22.32. 558 aa, ~63 kDa.
- One of the FA "core complex" subunits. First FA gene cloned by functional complementation
  [PMID:1574115 "Cloning of cDNAs for Fanconi's anaemia by functional complementation."].

## Core biology — FA core complex subunit required for FANCD2-FANCI monoubiquitination / ICL repair
- The FA core complex is a multisubunit E3 ubiquitin ligase; FANCC is a non-catalytic subunit of it.
  [PMID:22266823 "Eight of the FA proteins comprise the FA core complex, a multisubunit complex required for DNA damage recognition at a stalled replication fork. In response to DNA damage, the complex, an E3 ligase, monoubiquitinates the FANCD2/FANCI heterodimer"].
- FANCC is co-immunoprecipitated as an integral member of the core complex
  [PMID:22266823 "Flag-tagged FAAP20 co-immunoprecipitated with FANCA, FANCE, and FANCC, indicating that FAAP20 associates with the FA core complex"].
- The five-subunit nuclear complex (FANCA/C/E/F/G) is required for FANCD2 monoubiquitination
  [PMID:12649160 "The FANCA, FANCC, FANCE, FANCF, and FANCG proteins form a nuclear complex required for the monoubiquination of the FANCD2 protein."].
- FANCC binds FANCE directly; the disease mutation L554P abolishes this
  [PMID:12649160 "A central region of FANCE was sufficient for FANCC binding. A Leu554Pro mutant of FANCC failed to interact with FANCE."].
- Structural placement (cryo-EM, not in GOA): FANCC-FANCE-FANCF constitute the substrate-recognition
  module of the FA core E3 ligase, present in a single copy, that positions the FANCD2-FANCI substrate
  for monoubiquitination by the FANCL RING/UBE2T module (Shakeel et al. 2019 Nature, PMID:31666700;
  deep-learning atomic model PMID:32939280; PDB 7KZP chain C = FANCC 1-558). This supports a
  molecular-adaptor / substrate-scaffold role and contribution to the complex's ubiquitin-ligase activity.
- Downstream: monoubiquitinated FANCI-FANCD2 drives replication-coupled ICL repair in S phase
  [PMID:19965384 "A central event in the activation of the Fanconi anemia pathway is the mono-ubiquitylation of the FANCI-FANCD2 complex" ; "FANCI-FANCD2 is required for replication-coupled ICL repair in S phase."].

## FANCC and translesion synthesis (TLS) — branch of the pathway
- Genetic (DT40) epistasis links FANCC to REV1-mediated error-prone TLS; the FA core (not FANCD2) is
  needed for REV1 focus formation and point mutagenesis
  [PMID:22266823 "Studies by Niedzwiedz et al. in chicken DT40 cells demonstrated an epistatic relationship between FANCC of the FA core complex and the error-prone TLS polymerase, Rev1, suggesting that the FA pathway regulates TLS through this mechanism."]
  [PMID:22266823 "FANCC-deficient DT40 cells display a reduced frequency of spontaneous point mutations, suggesting that the FA pathway is required for Rev1-mediated TLS of abasic sites or other spontaneously generated DNA lesions"].

## FA core complex assembly / integrity — FANCA-FANCC interaction
- FANCA (FAA) and FANCC (FAC) bind each other; binding correlates with function and is lost in L554P
  [PMID:9398857 "we demonstrate the FAA and FAC bind each other and form a complex. Protein binding correlates with the functional activity of FAA and FAC, as patient-derived mutant FAC (L554P) fails to bind FAA."].
- Unbound FAA/FAC are largely cytoplasmic; the assembled complex is both cytoplasmic and nuclear
  [PMID:9398857 "Although unbound FAA and FAC localize predominantly to the cytoplasm, the FAA-FAC complex is found in similar abundance in both cytoplasm and nucleus."].
- FA core also present in a larger BLM-containing "BRAFT" super-complex
  [PMID:12724401 "one of the complexes, termed BRAFT, also contains five of the Fanconi anemia (FA) complementation group proteins"].
- FAAP20 is an integral core-complex protein needed for DNA-damage-induced chromatin loading of the core
  [PMID:22343915 "We show that FAAP20 is an integral component of the FA nuclear core complex." ; "The FAAP20-UBZ domain is not required for interaction with FANCA, but is required for DNA-damage-induced chromatin loading of FANCA and the functional integrity of the FA pathway."].

## Non-core / additional proposed roles (context-specific, separable from ICL-repair function)
- Cytoplasmic chaperone GRP94/HSP90B1 binds FANCC and regulates its steady-state level; interaction is
  cytosolic, not nuclear
  [PMID:9596688 "Binding was confirmed by coimmunoprecipitation of FAC and GRP94 from cytosolic, but not nuclear, lysates" ; "Ribozyme-mediated inactivation of GRP94 ... led to significantly reduced levels of immunoreactive FAC and concomitant hypersensitivity to mitomycin C"]. This is a stability/localization interaction, not a distinct MF.
- Cytokine signaling / apoptosis: FANCC promotes IFN-gamma-induced STAT1 activation and suppresses
  cytokine-induced apoptosis via modulation of PKR (EIF2AK2). These functions are STRUCTURALLY SEPARABLE
  from the cross-linker-resistance/FANCD2 function
  [PMID:11520787 "FANCC is also required for optimal activation of STAT1 in response to cytokine and growth factors and for suppressing cytokine-induced apoptosis by modulating the activity of double-stranded RNA-dependent protein kinase."]
  [PMID:11520787 "All mutants complemented mitomycin C (MMC) hypersensitive phenotype of FA-C cells and corrected aberrant posttranslational activation of FANCD2 in FA-C mutant cells. However, 2 of the mutants, S249A and E251A, failed to correct defective STAT1 activation."].
  => Treat oxidative-stress/redox and cytokine/apoptosis roles as NON-CORE.

## Localization summary
- UniProt: Nucleus + Cytoplasm; "The major form is nuclear. The minor form is cytoplasmic." Assembled
  FA core acts in the nucleoplasm/on chromatin; cytosolic pool associates with chaperones (GRP94) and a
  PKR/HSP70 complex (Reactome R-HSA-9835411). Nucleoplasm (HPA IDA) and chromatin (ComplexPortal IDA)
  are well supported.

## Annotation-review decisions (summary)
- GO:0043240 Fanconi anaemia nuclear complex (part_of; IBA/IEA/NAS/IDA x5): ACCEPT — CORE.
- GO:0036297 interstrand cross-link repair (IEA, NAS): ACCEPT — CORE.
- GO:0006281 DNA repair (TAS): ACCEPT (general parent, correct).
- GO:0065003 protein-containing complex assembly (TAS): ACCEPT (FANCC needed for FA core assembly/integrity).
- GO:0034599 cellular response to oxidative stress (IBA): KEEP_AS_NON_CORE (mouse-driven phylogenetic;
  redox role real but peripheral, separable from ICL repair).
- GO:0006289 nucleotide-excision repair (IBA): MARK_AS_OVER_ANNOTATED — FANCC is not a canonical NER
  factor; its process is ICL repair / TLS regulation. Over-propagated IBA.
- GO:0005515 protein binding (IPI x6): MARK_AS_OVER_ANNOTATED — uninformative MF; specific partners
  (FANCE, GRP94, SMAD4, FBXW7, MEOX2, AKT1) are largely HT/network or captured better by complex terms.
- Locations nucleus/cytoplasm/nucleoplasm/cytosol/chromatin: ACCEPT (all supported).

## References not in GOA but used for context (notes only; not cited as supporting_text)
- PMID:31666700 Shakeel et al., Structure of the FA monoubiquitin ligase complex, Nature 2019.
- PMID:32939280 Deep-learning atomic structure of FA core complex (PDB 7KZP), 2020.
