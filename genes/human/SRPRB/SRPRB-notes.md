# SRPRB (Q9Y5M8) review notes

## Identity / overview
SRPRB is the beta subunit of the signal recognition particle receptor (SR), a heterodimeric ER-membrane
complex (SRalpha = SRPRA + SRbeta = SRPRB). SRbeta is a small Ras-superfamily GTPase (closely related to
Arf/Sar1) that is membrane-anchored via a single N-terminal transmembrane helix and tethers the
soluble SRalpha to the ER membrane. The SR docks the SRP-ribosome-nascent chain complex at the ER so
that cotranslational translocation through the Sec61 channel can proceed. Also known as APMCF1.

- UniProt FUNCTION: "Component of the signal recognition particle (SRP) complex receptor (SR)";
  "Ensures, in conjunction with the SRP complex, the correct targeting of the nascent secretory proteins
  to the endoplasmic reticulum membrane system"; "May mediate the membrane association of SR"
  [file:human/SRPRB/SRPRB-uniprot.txt].
- SUBUNIT: "Heterodimer with SRPRA" [file:human/SRPRB/SRPRB-uniprot.txt].
- SUBCELLULAR LOCATION: "Endoplasmic reticulum membrane ... Single-pass membrane protein"
  [file:human/SRPRB/SRPRB-uniprot.txt].
- GTPase: TRANSMEM 37-57; GTP BINDING sites at 71-79, 92-95, 120, 248; KW GTP-binding, Nucleotide-binding.
  BRENDA 3.6.5.4. Belongs to the SRP receptor beta subunit family.

## Key functional evidence
- Structure of mammalian SR: PMID:16439358 "The structure of the mammalian signal recognition particle
  (SRP) receptor as prototype for the interaction of small GTPases with Longin domains" — "The SR is a
  heterodimeric complex assembled by the two GTPases SRalpha and SRbeta, which is membrane-anchored";
  "2.45-A structure of mammalian SRbeta in its Mg2+ GTP-bound state in complex with the minimal binding
  domain of SRalpha"; "SRbeta is a member of the Ras-GTPase superfamily closely related to Arf and Sar1"
  [PMID:16439358].
- Cryo-EM of SRP-RNC-SR: PMID:34020957 (PDB 7NFX) "Receptor compaction and GTPase rearrangement drive
  SRP-mediated cotranslational protein translocation into the ER" (in uniprot reference list; not cached).

## Annotation review decisions
- Core MF: GTP binding (GO:0005525) — SRbeta is a GTPase; this is its core molecular activity.
- Core CC: signal recognition particle receptor complex (GO:0005785); endoplasmic reticulum membrane
  (GO:0005789).
- Core BP: protein targeting to ER (GO:0045047) / SRP-dependent cotranslational targeting, signal sequence
  recognition (GO:0006617).
- GO:0016020 membrane (NAS/IDA): SRPRB is an ER-membrane protein; "membrane" is a correct but generic
  parent of ER membrane. KEEP_AS_NON_CORE (generic).
- GO:0005881 cytoplasmic microtubule (IDA, PMID:23264731): the cited paper is about MTR120/KIAA1383, a
  microtubule-associated protein, and characterizes microtubule biology; it does not establish SRPRB as a
  microtubule component. SRPRB is an ER-membrane GTPase, not a microtubule protein. This appears to be a
  mis-attributed/over-extended localization. Cannot verify SRPRB involvement from the cached abstract.
  -> UNDECIDED (per guidelines: do not REMOVE an experimental annotation on incomplete evidence; flag
  inconsistency). Biologically implausible as a core function.
- GO:0005737 cytoplasm (IDA, PMID:19664239): APMCF1 = SRPRB alias; GFP-APMCF1 subcellular localization
  study. A diffuse cytoplasmic signal is plausible for an ER-membrane protein (ER is cytoplasmic). KEEP
  as non-core (the ER membrane is the informative location).
- protein binding (GO:0005515) IPI rows: high-throughput interactome captures (PMID:16169070,
  PMID:33961781, PMID:40205054); the informative SRPRA interaction is captured by the SR-complex term.
  KEEP_AS_NON_CORE per guidelines.

## Disease
No clearly established Mendelian disease for SRPRB (gene MIM 616883; phenotype not assigned in UniProt).

## Falcon deep-research findings (incorporated 2026-06)
- Cryo-EM of the prehandover mammalian ribosome-SRP-SR complex shows GTP-bound SRbeta (SRPRB) and eukaryote-specific SRP/SR proteins forming a large assembly at the distal SRP RNA site, with SRP/SR GTP hydrolysis delayed at this stage to permit signal-sequence handover [PMID:29567807 "GTP hydrolysis of SRP-SR is delayed at this stage, possibly to provide a time window for signal sequence handover to the translocon"]. Added to GTP binding (GO:0005525) and SR-complex core_function supported_by.
- Eukaryotic SRP-mediated targeting requires sequential GTPase-driven compaction of the SR (SRalpha/SRbeta) and conformational rearrangements coupling the SRP/SR GTPase cycle to translocation; SRP54 SCN mutations uncouple the cycle from translocation [PMID:34020957 "this transition requires multiple sequential conformational rearrangements ... initiated by GTPase-driven compaction of the SRP receptor"]. Added to GTP binding supported_by.
- Human SRPRB CRISPR knockout profoundly destabilizes SRalpha (proteasome-sensitive) and redistributes residual SRalpha to the cytosol, while steady-state ER mRNA localization is largely unaltered (uncoupling ER mRNA localization from SR expression) [PMID:37643813 "CRISPR/Cas9-mediated KO resulted in profound destabilization of SRA"]. Added to SR-complex core_function supported_by; direct human loss-of-function evidence for the SRbeta anchoring role.
- New SRbeta function beyond anchoring: SRbeta is required to assemble an N-glycosylation-competent translocon; perturbing its GTP-binding site causes hypoglycosylation and reduces SRbeta-OST association without disrupting SRalpha-SRbeta binding [PMID:36921042 "SR-beta has a previously unrecognized function coordinating endoplasmic reticulum translation with N-glycosylation"]. Candidate for a future MF/BP annotation (cotranslational N-glycosylation coordination); reference added (relevance HIGH).
- Foundational Miller et al. 1995 (J Cell Biol) characterizing SRbeta as a transmembrane GTPase anchoring SRalpha is consistent with the review but predates the 2020-2025 scope; not added (PMID not separately resolved here).
