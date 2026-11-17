# SLC6A3 (DAT) curation notes

UniProt: Q01959 (SC6A3_HUMAN). HGNC:11049. Gene SLC6A3 (synonym DAT1).
620 aa, 12-TM integral membrane protein. NCBI taxon 9606.
Batch 10 canonical-surfaceome backfill. 102 GOA rows (101 seeded stub rows).

## Core biology (verified)

SLC6A3 encodes the **dopamine transporter (DAT)**, the presynaptic plasma-membrane
transporter that clears released dopamine from the synaptic cleft and recycles it into
dopaminergic neurons, terminating dopaminergic signalling. It is a **Na+- and
Cl--dependent (secondary-active) symporter** of the SLC6 / neurotransmitter:sodium
symporter (NSS, SNF) family (TC 2.A.22.1.3), driven by the inwardly-directed Na+
electrochemical gradient — a symporter, not an antiporter or uniporter.

- UniProt FUNCTION: "Mediates sodium- and chloride-dependent transport of dopamine"
  [Q01959 CC:FUNCTION, ECO:0000269|PubMed:1406597, 10375632, 11093780, 15505207,
  19478460, 39112701/3/5, 8302271].
- UniProt CATALYTIC ACTIVITY (RHEA:70919): "dopamine(out) + chloride(out) + Na(+)(out) =
  dopamine(in) + chloride(in) + Na(+)(in)"; a second Rhea (RHEA:70931) with 2 Na+ is the
  structurally-resolved 2 Na+ : 1 Cl- : 1 DA stoichiometry [PubMed:39112701].
  ChEBI: dopamine(1+) CHEBI:59905, Na+ CHEBI:29101, chloride CHEBI:17996.
- Cloning + sodium-dependent DA uptake: [PMID:1406597 "the human clone is able to induce
  a saturable, time- and sodium-dependent, dopamine uptake"].
- Na+/Cl- coupling mapped to transporter domains: [PMID:11093780 "the Na(+)- and
  Cl(-)-dependence of dopamine transport"].
- Recent cryo-EM: DAT is a **monomer** in detergent/nanodisc structures
  [PubMed:39112701, 39112703, 39112705] (earlier work reported a disulphide-linked
  homodimer, Ref.16). Cocaine, amphetamine, benztropine, GBR12909 etc. occupy/overlap the
  dopamine site [UniProt CC:ACTIVITY REGULATION].

**Core MF** = GO:0005330 dopamine:sodium symporter activity (OLS-verified, not obsolete).
Confirmed is_a ancestors of GO:0005330 (OLS getAncestors): GO:0008504 monoamine
transmembrane transporter activity and GO:0015370 solute:sodium symporter activity (both
TOO_GENERAL once GO:0005330 is asserted). GO:0005326 neurotransmitter transmembrane
transporter activity is NOT an ancestor of GO:0005330 (parallel branch) — so those rows
cannot be TOO_GENERAL; kept as broad-but-correct (ACCEPT). GO:0005334
norepinephrine:sodium symporter activity is a sibling, not an ancestor; DAT does transport
noradrenaline as a genuine secondary substrate (UniProt catalytic activity RHEA:70923, By
similarity; well established that DAT clears NE, especially in prefrontal cortex) →
KEEP_AS_NON_CORE.

**Location** (verified): presynaptic/axonal plasma membrane of dopaminergic neurons;
substantia nigra, striatum, axonal varicosities (at protein level) [UniProt TISSUE
SPECIFICITY, PubMed:17296554]. DAT is definitively **presynaptic** — the postsynaptic
membrane IEA (ortholog-transferred) is not supported and conflicts with its role, so
REMOVE. Internalized/trafficking pools explain the old "cytoplasm" TAS row
(MARK_AS_OVER_ANNOTATED — DAT is an integral membrane protein).

**Disease**: biallelic loss-of-function → infantile parkinsonism-dystonia 1 (PKDYS1,
MIM:613135) [PMID:19478460 "loss-of-function SLC6A3 mutations that impair DAT-mediated
dopamine transport activity are associated with an early-onset complex movement disorder"].

## Process-term strategy (participation test)

DAT **performs** dopamine reuptake, so it executes the step of:
- GO:0090494 dopamine uptake → ACCEPT (IDA/IEA/ISS)
- GO:0051583 dopamine uptake involved in synaptic transmission → ACCEPT (it does the
  reuptake step of the dopaminergic synaptic cycle)
- GO:0001504 neurotransmitter uptake, GO:0006836 neurotransmitter transport → ACCEPT
  (broad-but-correct; OLS shows GO:0090494 is NOT is_a either of these — parallel branches
  under organic-hydroxy/nitrogen-compound transport — so not TOO_GENERAL).
- GO:0035725 sodium ion transmembrane transport (IBA) → KEEP_AS_NON_CORE (Na+ is the
  co-transported driving ion, part of the mechanism, not the biological point).

DAT does **not** execute steps of the many downstream behavioural / pharmacological /
physiological processes it accumulates by ortholog IEA. It is upstream (via setting
dopamine tone) or is merely the drug target. Applying the participation test:
- Direct pharmacological/regulatory target (drug binds DAT, or signalling directly tunes
  DAT trafficking): response to xenobiotic stimulus, nicotine, ethanol, cAMP →
  KEEP_AS_NON_CORE.
- Indirect physiology: response to iron ion, response to leptin,
  protein-containing complex binding, protease binding, heterocyclic compound binding →
  MARK_AS_OVER_ANNOTATED.
- hyaloid vascular plexus regression (mouse, downstream of OPN5/dopamine, By similarity) →
  KEEP_AS_NON_CORE.
- GO:0006865 amino acid transport (IBA, node PANTHER:PTN000907004) → REMOVE. DAT is a
  monoamine (dopamine) transporter; dopamine is a decarboxylated catecholamine, not an
  amino acid. This is over-propagation across the SLC6 family, which contains both amino-
  acid transporters and monoamine/GABA neurotransmitter transporters. See propagation_review.

## Interactors (bare GO:0005515 protein binding IPI rows → all REMOVE per policy)

34 bare `protein binding` rows. Removing them does not deny the interactions; the generic
term is uninformative, and specific interactions are captured elsewhere (signaling receptor
binding = DRD2; PP2A binding; flotillin complex). Meaningful, literature-backed partners:
- PICK1/PRKCABP (Q9NRD5/Q9EP80): PDZ interaction, DAT clustering [PMID:11343649].
- DRD2 (P14416): D2 receptor promotes DAT surface localization [PMID:17380124] → underlies
  signaling receptor binding (GO:0005102).
- GPR37 (O15354): modulates DA uptake and drug responses [PMID:17519329].
- TOR1A/torsinA (O14656): regulates DAT trafficking [PMID:15505207].
- alpha-synuclein/SNCA (P37840): modulates DAT activity/surface levels [PMID:12958153,
  22163275, 26442590].
- Flotillin-1 (FLOT1): required for PKC-triggered DAT endocytosis + microdomain
  localization [PMID:21399631] → flotillin complex (GO:0016600), membrane raft.
- RIT2/Rin (Q99578/Q5BJQ5): required for PKC-regulated DAT trafficking, in lipid rafts
  [PMID:21957239].
- Many PDZ-scaffold interactors (DLG1-4, MPP/MAGI, SCRIB, LIN7C, PATJ, MPDZ, GRIP1/2) from
  interactome/fragmentomics screens [PMID:36115835, 40355756] — scaffolding, no single
  informative MF.

## IBA rows (phylogenetic reading)

- GO:0005886 plasma membrane (IBA, node PTN000177662) — correct; the WITH/FROM includes
  the target Q01959 itself (experimental grounding on target; expected, not circular).
  ACCEPT.
- GO:0035725 sodium ion transmembrane transport (IBA, PTN000177662) — co-transported ion;
  KEEP_AS_NON_CORE.
- GO:0006865 amino acid transport (IBA, PTN000907004) — cross-branch over-propagation
  (amino-acid-transporter clade of SLC6); REMOVE with propagation_review. DAT/NET/SERT are
  monoamine, not amino-acid, transporters.

No PAINT IRD/IKR loss review run (coordinator-scoped edit-only task); IBA rows kept here
are independently well grounded on the target.

## No NEW terms, no proposed_new_terms, no source_defects

Annotation coverage of DAT's real functions is comprehensive (specific MF + uptake process
+ presynaptic locations present). The reuptake term GO:0098810 neurotransmitter reuptake is
not in GOA but would be broader/redundant with the accepted dopamine-uptake-in-synaptic-
transmission row, so not proposed. No gene-model or isoform defects found.
