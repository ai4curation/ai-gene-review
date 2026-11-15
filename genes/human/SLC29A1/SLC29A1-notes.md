# SLC29A1 (ENT1, hENT1) curation notes

UniProt: Q99808 (S29A1_HUMAN), 456 aa. HGNC:11003. PANTHER PTHR10332:SF9. TCDB 2.A.57.1.1.

## Core identity
SLC29A1/ENT1 is the prototypic **es-type** (equilibrative, NBMPR-**sensitive**)
nucleoside transporter: a **uniporter** mediating **facilitated, Na+-INDEPENDENT,
bidirectional (equilibrative)** transport of nucleosides and (lower-affinity)
nucleobases down their concentration gradient. 11 TM helices, MFS-like fold
(PDB 6OB6/6OB7/8TZI).

- UniProt CC:FUNCTION: "Uniporter involved in the facilitative transport of
  nucleosides and nucleobases... Functions as a Na(+)-independent transporter
  (PubMed:8986748)." [file:human/SLC29A1/SLC29A1-uniprot.txt CC:FUNCTION]
- Na+-independent / equilibrative mechanism is the defining feature ⇒ the Na+
  **symporter** term GO:0015389 is factually wrong for ENT1 (see defect below).

## Substrates (from UniProt CATALYTIC ACTIVITY + literature)
Nucleosides (core, high affinity, Km ~11–580 µM): adenosine, guanosine, inosine,
uridine, thymidine, cytidine [PMID:10722669, PMID:8986748, PMID:9396714,
PMID:12527552]. Also purine/pyrimidine **nucleobases** (lower affinity, Km mM
range: adenine 3200, thymine 6300, hypoxanthine 6000 µM) — adenine, guanine,
hypoxanthine, thymine, uracil [PMID:21795683 (full text), "hENT1 additionally
transports thymine and adenine and, to a lesser extent, uracil and guanine.
Fluxes of hypoxanthine, thymine, and adenine by hENT1 were saturable and
inhibited by NBMPR"]. Nicotinamide is a newer substrate [PMID:39885119, UniProt
CATALYTIC ACTIVITY nicotinamide] — not in GOA; candidate addition.

## Pharmacology / inhibitors
Potently inhibited by NBMPR (Ki ~2 nM; es-type), dipyridamole, dilazep,
draflazine. Transports nucleoside-analog drugs (gemcitabine, cytarabine,
cladribine, fludarabine, ribavirin, 6-mercaptopurine, AZT/ddC/ddI) — basis of
Reactome drug-ADME annotations and the gemcitabine-response biomarker role
[PMID:15501974, UniProt MISCELLANEOUS]. Drug transport is pharmacological ⇒
non-core (xenobiotic transport) / over-annotation (xenobiotic metabolism).

## Physiology
- Regulates extracellular **adenosine** (and thus purinergic P1 signalling):
  cardiovascular, CNS. Adenosine is a neuromodulator, not a classical
  neurotransmitter ⇒ "neurotransmitter transporter/uptake/transport" terms are
  over-annotations of the equilibrative nucleoside activity.
- Regulates extracellular **inosine** in brown adipose tissue → BAT-dependent
  energy expenditure [PMID:35790189].
- Plasma-membrane protein; polarized epithelia show basolateral (renal, Sertoli)
  and apical (renal) localization [PMID:12527552 "both transporters are expressed
  on the basolateral membrane. hENT1 is also present on the apical membrane";
  PMID:23639800 "ENT1 to be located on the basolateral membrane of human and rat
  Sertoli cells"]. Erythrocyte membrane; complex with stomatin (STOM)
  [PMID:23219802]. Detected at the blood-brain barrier by quantitative proteomics
  [PMID:23137377].

## Key review decisions
- Core MF = **GO:0015395** nucleoside transmembrane transporter activity, down a
  concentration gradient (equilibrative) — more precise than GO:0005337 and
  matches Na+-independent evidence. Added as NEW (IC). GO:0005337 rows ACCEPT
  (correct general level; IBA at PTHR node legitimately general — family includes
  H+-coupled plant ENTs).
- Nucleoside/adenosine/inosine/uridine/cytidine transport (MF + BP): ACCEPT
  (core, strong IDA).
- Nucleobase transport (adenine/guanine/uracil/thymine/hypoxanthine; MF + BP):
  KEEP_AS_NON_CORE (genuine but low-affinity secondary activity, IDA
  PMID:21795683).
- GO:0015389 pyrimidine- and adenosine-specific:sodium symporter activity (IDA
  PMID:21795683): **REMOVE** + source_defect (WRONG_TERM, UNIPROT). ENT1 is
  Na+-independent/equilibrative; the paper itself shows NBMPR-sensitive
  equilibrative transport. Correct term = GO:0005337/GO:0015395.
- GO:0016020 membrane: TOO_GENERAL (plasma membrane asserted).
- Neurotransmitter terms (GO:0005326/0006836/0001504): MARK_AS_OVER_ANNOTATED.
- Xenobiotic transport GO:0006855: KEEP_AS_NON_CORE (drug transport, real but
  pharmacological); xenobiotic/nucleobase metabolic process GO:0006805/GO:0006139:
  MARK_AS_OVER_ANNOTATED (ENT1 is a transporter, not a metabolic enzyme).
- Electronic rodent-ortholog process transfers (lactation, response to
  antibiotic, EPSP, response to glucose, response to hypoxia):
  MARK_AS_OVER_ANNOTATED (indirect/pleiotropic, no human evidence).
- Synapse CC (presynapse/postsynapse, IEA): KEEP_AS_NON_CORE (plausible CNS
  location, rodent-ortholog electronic).
- Blood-brain barrier transport GO:0150104 (NAS): KEEP_AS_NON_CORE.
