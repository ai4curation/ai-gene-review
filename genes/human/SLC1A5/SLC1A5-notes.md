# SLC1A5 (ASCT2 / ATB0) — curation notes

UniProt: Q15758 (AAAT_HUMAN). HGNC:10943. 541 aa, chr 19q13.3. Family:
dicarboxylate/amino acid:cation symporter (DAACS, TC 2.A.23) family, SLC1A5
subfamily; SLC1 solute carrier family. PANTHER PTHR11958:SF19.

## Core identity

SLC1A5 is a **sodium-coupled, obligate antiporter (exchanger) of small neutral
amino acids** in the plasma membrane. Its physiologically preferred substrate is
**L-glutamine**, which it exchanges bidirectionally with other neutral amino
acids (L-serine, L-threonine, L-asparagine, L-alanine, L-valine, L-methionine).
It is mechanistically distinct from the glutamate-transporting EAATs (SLC1A1-3)
in the same SLC1 family, which are Na+/H+/K+-coupled **symporters** that
concentratively accumulate glutamate; ASCT2 instead runs a 1:1 amino-acid
**exchange** and cannot concentrate its substrates [UniProt CC FUNCTION
ECO:0000269; PMID:23756778].

- Obligate exchange: "ASCT2 is a neutral amino acid transporter, which catalyzes
  a sodium-dependent obligatory antiport among glutamine and other neutral amino
  acids" [PMID:32733894, abstract].
- Cloning / substrate scope: a Na+-dependent system with "preference for
  zwitterionic amino acids. Anionic amino acids, cationic amino acids, imino
  acids, and N-methylated amino acids are excluded by this system" [PMID:8702519,
  abstract]. This directly excludes aspartate/glutamate as canonical substrates
  of the wild-type transporter.
- Antiporter mechanism shown directly in proteoliposomes: "Time dependent
  [(3)H]glutamine/glutamine antiport was measured in proteoliposomes which was
  active only in the presence of external Na(+)"; kinetic asymmetry Km 0.097 mM
  (external) vs 1.8 mM (internal) for glutamine, Km(Na+) 32 mM [PMID:23756778,
  abstract; GOA IDA GO:0015297 antiporter activity].
- Cryo-EM: homotrimer, elevator-type transport; "ASCT2 forms a homotrimeric
  complex in which each subunit contains a transport and a scaffold domain"
  [PMID:29872227, abstract]. Obligatory exchange mode confirmed structurally
  [PMID:39095408, UniProt].

## Substrate specificity details (UniProt CATALYTIC ACTIVITY, ECO:0000269)

RHEA reactions document Na+-coupled exchange of L-glutamine(out) with L-serine,
L-threonine, L-asparagine, L-alanine, L-valine, L-methionine, D-serine. Aspartate
is NOT a wild-type substrate: the C467R mutant "Changes the substrate specificity
toward negatively charged amino acids. Impairs L-glutamine transport and enables
L-aspartate transport instead" [UniProt FT MUTAGEN 467; PMID:31366933]. Thus
L-aspartate transporter/import annotations describe the mutant or family-level
behaviour, not WT ASCT2.

Glutamate is a conditional/secondary substrate: ASCT2 "also catalyzes a
sodium-dependent antiport of glutamate with glutamine ... the glutamate/glutamine
antiport is pH-dependent with optimal activity at acidic pH on the external
(extracellular) side" with a coupled proton (1:1 H+:glutamate) [PMID:32733894,
abstract]. So glutamate transmembrane transporter activity is real but minor and
pH-gated, not the core function.

Cysteine is a modulator, not a transported substrate [UniProt ACTIVITY REGULATION
ECO:0000269|PubMed:26492990]. The family also shows a substrate-/Na+-gated,
thermodynamically uncoupled anion (SCN- > NO3- > I- > Cl-) conductance
(channel-like) [UniProt CC FUNCTION By similarity].

## Localization

Plasma membrane / cell membrane, multi-pass (8 TM + two reentrant hairpins HP1,
HP2) [UniProt; PMID:29872227]. In polarized epithelia it is restricted to the
**apical** (brush-border) membrane of proximal tubule and intestine
[UniProt SUBCELLULAR LOCATION ECO:0000250|P51912; TISSUE SPECIFICITY placenta,
lung, skeletal muscle, kidney, pancreas, intestine, PMID:8702519]. HPA IF: plasma
membrane [GO_REF:0000052 IDA]. Detected in melanosome fractions (MS proteomics,
PMID:17081065) and in B-cell extracellular exosomes (MS, PMID:20458337) — these
are large-scale detections of a surface membrane protein, not functional
organellar locations. A "basal plasma membrane" ISS contradicts the documented
apical restriction.

## Physiological / disease roles

- **Cancer "glutamine addiction" / mTORC1**: SLC1A5 is the principal glutamine
  importer in many tumours; intracellular Gln feeds TCA anaplerosis and, via
  SLC7A5/SLC3A2 exchange, leucine uptake and mTORC1 activation; it is a drug
  target [PMID:25759021 intro, "SLC1A5 is highly expressed in BCa cells and is
  also implicated in regulation of essential amino acid influx, mammalian target
  of rapamycin (mTOR) activation ... and L-Gln-dependent tumor cell growth"].
  RNF5 ubiquitinates SLC1A5 → proteasomal degradation under ER stress
  [PMID:25759021]. (SLC1A5 is the substrate here; this gives it no new MF.)
- **Hematopoiesis**: glutamine transport via ASCT2 is required for erythroid
  lineage specification of human HSCs; blocking it diverts cells to
  myelomonocytic fates [PMID:24953180, "HSCs require the ASCT2 glutamine
  transporter and active glutamine metabolism for erythroid specification"].
  This is a metabolic-support (necessity) role, not a core transporter function.
- **Retrovirus receptor**: ASCT2 (=RDR) is the cell-surface receptor for the
  RD114/type D retrovirus interference group (feline endogenous RD114, baboon
  endogenous virus, type D simian retroviruses) [PMID:10051606, "Both RDR and
  ATB0 serve as retrovirus receptors"; UniProt CC FUNCTION (Microbial
  infection)]. The docking platform is the TM4 beta-hairpin (aa 204-224)
  [UniProt FT REGION; PMID:29872227, PMID:38671230]. This is virus receptor
  activity (GO:0001618), not generic signaling receptor activity.
- **Placental syncytialization**: ASCT2 is the receptor for the fusogenic HERV
  envelope syncytin-1/ERVW-1; secreted suppressyn/ERVH48-1 binds ASCT2 and
  inhibits syncytin-1-mediated trophoblast fusion [PMID:23492904, "cell-associated
  and secreted suppressyn binds to the syn1 receptor, ASCT2"; UniProt SUBUNIT].

## Interactome (GO:0005515 IPI rows)

C-terminal (…ESV) PDZ ligand binds many PDZ-scaffold proteins (DLG1/2/4, MAGI1/2,
SCRIB, PDZK1, MPDZ, GRIP1/2, PATJ, LNX1/2, NHERF4/PDZD3, WHRN, TJP1, APBA1/2,
FRMPD2) plus PTPN3, IL16, TUSC5, APOL3, PLP1, and the E3 ligase RNF5 and
suppressyn (ERVH48-1, M5A8F1) [UniProt INTERACTION; IntAct]. All are bare
"protein binding" (GO:0005515) with no informative MF for ASCT2 itself →
REMOVE per the project protein-binding policy; the biologically meaningful
interactions (RNF5 regulation, suppressyn/syncytin) are captured in prose/other
rows.

## Action summary rationale

- Core MF: GO:0015175 neutral L-amino acid transmembrane transporter activity;
  GO:0015186 L-glutamine transmembrane transporter activity; GO:0015297
  antiporter activity (the obligate-exchange mechanism). Core BP: GO:1903803
  L-glutamine import across plasma membrane, GO:0015804 neutral amino acid
  transport. Core CC: GO:0005886 plasma membrane.
- GO:0015293 symporter activity (IEA/InterPro): wrong transport mode for this
  subfamily (ASCT2 is an obligate antiporter) → MARK_AS_OVER_ANNOTATED.
- Aspartate terms (GO:0015183, GO:0140009): not WT substrates → MARK_AS_OVER_ANNOTATED.
- Glutamate terms (GO:0005313 MF, GO:0015813 BP): real but conditional/pH-gated
  secondary activity → KEEP_AS_NON_CORE.
- GO:0038023 signaling receptor activity → MODIFY to GO:0001618 virus receptor activity.
- General parents (GO:0006865, GO:0015171, GO:0016020, GO:0098657) → TOO_GENERAL.
