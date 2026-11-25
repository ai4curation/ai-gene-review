# ABCC4 (MRP4) — curation notes

UniProt: O15439 (MRP4_HUMAN). HGNC symbol ABCC4. ATP-binding cassette sub-family C member 4,
also "multidrug resistance-associated protein 4" / "MOAT-B". 1325 aa, polytopic membrane protein.

## Architecture (UniProt O15439)

- Multi-pass (polytopic) membrane protein with two transmembrane domains and two
  cytoplasmic nucleotide-binding (ABC transporter) domains
  [file:human/ABCC4/ABCC4-uniprot.txt FT DOMAIN 93..377, 410..633, 711..1005, 1041..1274;
  12 predicted transmembrane helices].
- "The two ABC transporter domains, also known as nucleotide-binding domains, are essential
  for ATP binding and hydrolysis" (PMID:38886124, PMID:40138312, cryo-EM; UniProt DOMAIN).
- C-terminal class-I **PDZ-binding motif** [file:human/ABCC4/ABCC4-uniprot.txt FT MOTIF 1322..1325].
  Cryo-EM shows MRP4 is a **monomer** (PMID:38886124, PMID:40138312).
- EC numbers assigned: 7.6.2.2 (xenobiotic), 7.6.2.3 (glutathione S-conjugate), plus 7.6.2.-.

## Core molecular function: ATP-driven organic-anion efflux

MRP4 is a **primary active (ATP-dependent) efflux pump** for a broad spectrum of organic anions.
ATPase activity is direct: [PMID:15364914 "MRP4 hydrolyzes ATP (Km, 0.62 mm)"] and is stimulated by
transported substrates [PMID:15364914 "the prostaglandins E1 and E2, stimulate ATP hydrolysis"].

Substrate classes with experimental support:

- **Cyclic nucleotides (cAMP, cGMP).** Apical renal efflux pump for urinary cAMP/cGMP
  [PMID:11856762 "exhibit ATP-dependent transport of [(3)H]cAMP and [(3)H]cGMP"];
  [PMID:15454390 "MRP4 could transport urate simultaneously with cAMP or cGMP"]. cGMP transport is
  positive-cooperative (Km ~180 µM) and modulated by urate.
- **Prostaglandins (PGE1, PGE2).** [PMID:25173977 "only ABCC4 is known to directly transport PGE2"];
  KM 2.1 µM (PGE1), 3.4 µM (PGE2) (UniProt BIOPHYSICOCHEMICAL PROPERTIES). NSAIDs inhibit transport.
- **Glutathione and GSH S-conjugates / leukotrienes.** [PMID:17959747 "human ABCC4 mediates the
  ATP-dependent efflux of LTB(4) in the presence of reduced glutathione (GSH)"] and
  [PMID:17959747 "also functioned as an ATP-dependent efflux pump for LTC(4)"] (LTC4 KM 0.13 µM;
  GSH not required for LTC4). Interacts with GSH conjugates such as
  [PMID:11856762 "S-(2,4-dinitrophenyl)-glutathione"].
- **Bile acids (cotransport with GSH).** [PMID:16282361 "has a high affinity for the taurine and
  glycine conjugates of the common natural bile acids as well as the unconjugated bile acid cholate"];
  [PMID:12883481 "localized the multidrug resistance protein 4 (MRP4; ABCC4) to the basolateral
  membrane of human, rat, and mouse hepatocytes"]. Proposed basolateral/sinusoidal overflow pathway
  for bile acids and a source of plasma GSH.
- **Urate.** [PMID:15454390 "mediates ATP-dependent urate transport via a positive cooperative
  mechanism"]; candidate apical pump for urinary urate excretion.
- **Steroid conjugates.** DHEA-3-sulfate, testosterone-17-sulfate, estradiol-17/estriol-16-glucuronide
  (UniProt CATALYTIC ACTIVITY; PMID:29175180, PMID:39993711); no transport of estrone 3-sulfate.
- **Xenobiotics / drugs.** Ganciclovir [PMID:12105214 "confers resistance to purine-based
  antiretroviral agents"], 6-MP and PMEA [PMID:18300232 "participates in the transport of diverse
  antiviral and chemotherapeutic agents such as 6-mercaptopurine (6-MP) and 9-(2-phosphonyl
  methoxyethyl) adenine (PMEA)"], cephalosporins [PMID:17344354 "Significant ATP-dependent transport
  of ceftizoxime (K(m), 18 microM), cefazolin ..."], methotrexate/folate (PMID:11856762, low
  affinity). This underlies its multidrug-resistance phenotype.

## Localization

Tissue-dependent polarity: **apical** in kidney proximal tubule
[PMID:11856762 "MRP4 is localized to the proximal tubule apical membrane of human kidney"], **basolateral**
in hepatocytes (PMID:12883481). Present at blood-tissue barriers (blood-brain, blood-CSF, blood-testis;
PMID:18619525, PMID:23137377, PMID:24130369, PMID:25986174, PMID:26590417, PMID:30280653) and in
**platelet dense-granule membranes** [PMID:15297306 "largely colocalized with the accumulation of
mepacrine as marker for delta-granules"], where it loads cyclic nucleotides/nucleotides for mediator
storage. UniProt: "Its localization to the basolateral or apical membranes is tissue-dependent."

## PDZ interactome (protein-binding annotations)

The ~37 `GO:0005515 protein binding` GOA rows all report interactions with **PDZ-domain-containing
proteins** (SNX27, PDZK1, NHERF2/4, DLG1/2/4/5, MAGI1-3, SCRIB, TJP1-3, PARD3/3B, PATJ, MPP1, GRIP1/2,
syntenin, whirlin, harmonin/USH1C, etc.) via MRP4's C-terminal PDZ-binding motif. These were reviewed
as **MODIFY → GO:0030165 PDZ domain binding** rather than bare "protein binding".
[PMID:22411990 "MRP4 has a PDZ-binding motif, which is a potential sequence that modulates the membrane
expression of MRP4 via interaction with PDZ adaptor proteins"] — SNX27 accelerates MRP4 internalization;
[PMID:29146910 "PDZ motifs mediate interactions with their cognate PDZ-binding domain proteins"] — MPP1
enhances MRP4 surface expression/drug resistance in AML;
[PMID:36115835 "we measured with unprecedented coverage and sensitivity ~65,000 PDZ-PBM affinities"] —
large-scale PDZ-PBM affinity map; [PMID:24550280] — Scribble PDZ phage-display screen. These PDZ
interactions govern MRP4 trafficking, turnover and polarized membrane targeting.

## Downstream / context roles (non-core)

- **Platelet degranulation / mediator storage** (PMID:15297306; Reactome R-HSA-114608).
- **Prostaglandin-dependent ciliogenesis**: ABCC4 exports the PGE2 signal that promotes ciliogenesis
  via intraflagellar transport [PMID:25173977 "These data reveal the molecular bases of Lkt/ABCC4
  function, linking PGE2 export to ciliogenesis."]. ABCC4 acts upstream (transport), not as a cilium
  component.
- **Efflux at the blood-brain barrier** (PMID:26590417, PMID:30280653; NAS reviews).

## Removed / corrected annotation

- `GO:0016404 15-hydroxyprostaglandin dehydrogenase (NAD+) activity` (NAS, PMID:7557451) — **REMOVE**.
  PMID:7557451 is about the **HPGD / 15-PGDH enzyme**, not ABCC4. ABCC4 is an ABC membrane transporter
  with no NAD(+)-dependent dehydrogenase domain; this enzymatic MF is biologically impossible for it and
  is a gene/term mis-attribution (recorded as a `source_defects` entry, WRONG_TERM/GOA_EBI, DELETE_ROW).
- `GO:0098591 external side of apical plasma membrane` (ISS, PMID:18619525) — **MARK_AS_OVER_ANNOTATED**.
  MRP4 is a polytopic integral membrane transporter, not a protein peripherally attached to the external
  face; apical plasma membrane (GO:0016324) captures the surface-biotinylation result correctly.
- Generic `GO:0016020 membrane` rows — **TOO_GENERAL** (plasma membrane / apical / basolateral asserted
  and accepted elsewhere).

## Provenance notes

All quoted `supporting_text` was verified as a verbatim (whitespace-collapsed) substring of the cited
cached publication. Many primary transport papers are abstract-only in the cache
(`full_text_available: false`); experimental (EXP/IDA/IMP) annotations were accepted/deferred to the
curator per project policy rather than overruled on abstract-only evidence.


## Generic CC/MF term convention (batch-2 review, 2026-11-11)
Applied consistently across ABCA8/ABCC1/ABCC3/ABCC4: GO:0016020 membrane -> MODIFY to GO:0005886 plasma membrane (paradigm MODIFY case); GO:0022857 transmembrane transporter activity -> TOO_GENERAL (entailed by the specific accepted transporter activities); GO:0005886 plasma membrane -> ACCEPT (the generic PM term is informative, and apical/basolateral sidedness is carried by the gene's own GO:0016324/GO:0016323 rows, not by blanket-MODIFYing the PM parent to a sub-domain).
This gene: changed its 3 GO:0016020 rows from TOO_GENERAL to MODIFY->GO:0005886, and GO:0022857 from ACCEPT to TOO_GENERAL; GO:0005886 rows already ACCEPT.
