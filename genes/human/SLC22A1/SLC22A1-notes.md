# SLC22A1 (OCT1 / hOCT1) — curation notes

UniProt: O15245 (S22A1_HUMAN), 554 aa, HGNC:10963. Gene synonym OCT1.

## Summary of function (provenance)

SLC22A1 encodes Organic Cation Transporter 1 (OCT1), a 12-transmembrane-helix
polyspecific plasma-membrane transporter of the SLC22 family within the Major
Facilitator Superfamily (MFS).

- Mechanism: electrogenic, voltage-dependent, Na(+)- and pH-independent, bidirectional
  **facilitated uniporter** — NOT a Na(+)-coupled symporter.
  [UniProtKB:O15245 CC:FUNCTION, "Electrogenic voltage-dependent uniporter that mediates the transport of a variety of organic cations such as endogenous bioactive amines, cationic drugs and xenobiotics"]
  [UniProtKB:O15245 CC:FUNCTION, "Functions as a pH- and Na(+)-independent, bidirectional transporter"]
  [UniProtKB:O15245 CC:FUNCTION, "cellular uptake or release is driven by the electrochemical potential"]
- Family: [UniProtKB:O15245 CC:SIMILARITY, "Belongs to the major facilitator (TC 2.A.1) superfamily. Organic cation transporter (TC 2.A.1.19) family."]
- Topology: 12 TM helices (FT TRANSMEM 22-42, 150-170, ... 493-513), large extracellular loop (43-149, glycosylated at Asn71).

## Core location

- Primarily basolateral (sinusoidal) membrane of hepatocytes — the core physiological site.
  [UniProtKB:O15245 CC:SUBCELLULAR LOCATION, "Note=Localized to the sinusoidal/basolateral membrane of"] (hepatocytes)
  [UniProtKB:O15245 CC:FUNCTION, "Primarily expressed at the basolateral membrane of hepatocytes and proximal tubules"]
- Basolateral confirmed by IDA in liver [PMID:12719534].
- Polarity is tissue-dependent and partly contested (apical in airway ciliated epithelium [PMID:15817714]; apical vs basolateral in enterocytes and proximal tubule debated — see UniProt CAUTION). Apical/lateral/basal rows are genuine but peripheral to the hepatic core.

## Substrate profile (provenance)

Endogenous substrates (UniProt curated, with Rhea catalytic-activity entries and kinetics):
- Monoamines / neurotransmitters: dopamine (CHEBI:59905), serotonin (CHEBI:350546),
  (R)-adrenaline (CHEBI:71406), histamine (CHEBI:58432), N-1-methylnicotinamide, guanidine.
  [UniProtKB:O15245 CC:FUNCTION, "Transports endogenous"] "monoamines such as N-1-methylnicotinamide (NMN), guanidine, histamine, neurotransmitters dopamine, serotonin and adrenaline".
- Thiamine / vitamin B1 (CHEBI:18385): high-capacity hepatic uptake; regulates hepatic lipid/energy metabolism; metformin competitively inhibits this uptake.
  [UniProtKB:O15245 CC:FUNCTION, "the hepatic uptake of vitamin B1/thiamine, hence regulating hepatic"] (lipid and energy metabolism) [PMID:24961373 "OCT1 is a high-capacity thiamine transporter that regulates hepatic steatosis and is a target of metformin"].
- Acetylcholine: bidirectional transport at apical membrane of airway ciliated cells (luminal ACh release).
  [UniProtKB:O15245 CC:FUNCTION, "Mediates the bidirectional"] "transport of acetylcholine (ACh) at the apical membrane of ciliated cell in airway epithelium" [PMID:15817714].
- Choline (CHEBI:15354): low affinity (Km ~3445 uM) [PMID:40972734].
- Natural polyamines: spermidine, agmatine, putrescine — low affinity, relatively high turnover.
  [UniProtKB:O15245 CC:FUNCTION, "natural polyamines such as spermidine, agmatine and putrescine at low"] (affinity, but relatively high turnover) [PMID:21128598].
- Prostaglandins E2/F2alpha (non-amine; high affinity, nM Km): genuine secondary activity, physiological relevance uncertain.
  [UniProtKB:O15245 CC:FUNCTION, "Also capable of transporting non-amine"] "endogenous compounds such as prostaglandin E2 (PGE2) and prostaglandin F2-alpha (PGF2-alpha)" [PMID:11907186].
- Quaternary ammonium cations (TEA, prototypical substrate) [PMID:23567998].

Xenobiotics/drugs (major pharmacogene): metformin (signature hepatic-uptake substrate → glucose-lowering action), MPP+, cisplatin/oxaliplatin, tetraethylammonium, quinidine, lamivudine, many cationic drugs. OCT1 polymorphisms affect metformin and other drug responses.

## Substrates the human ortholog does NOT transport (important negatives)

UniProt CAUTION (from PMID:34040533, Jensen 2021): "In contrast with mouse ortholog, not
able to transport carnitine, noradrenaline". Carnitine was initially reported [PMID:28942964]
but a later study could not verify it.
- Consequence: Ensembl/Compara IEA rows projected from the mouse ortholog (O08966) for
  (R)-carnitine transporter activity (GO:1901235) and (R)-carnitine transport (GO:1902270)
  are NOT valid for human OCT1 → REMOVE.
- Norepinephrine uptake (GO:0051620) is contradicted by this CAUTION yet has an IDA
  (PMID:24688079). Genuine conflict → UNDECIDED.
- Acylcarnitine (e.g. isobutyrylcarnitine) transport is distinct from carnitine and is
  documented for human OCT1 [PMID:34040533, PMID:28942964] → O-acyl-L-carnitine transport
  (GO:1902616) KEEP_AS_NON_CORE.

## Annotation-review rationale highlights

- Core MF: no live GO grouping term for "organic cation transmembrane transporter activity"
  (GO:0015101 is OBSOLETE — "unnecessary and confusing grouping term", no replacement;
  verified via QuickGO 2026-11-15). Core function therefore represented by the live,
  experimentally-grounded substrate-class MF terms: GO:0008504 monoamine TTA, GO:0015651
  quaternary ammonium group TTA, GO:0015234 thiamine TTA.
- Wrong-mechanism electronic rows → REMOVE: GO:0005330 dopamine:sodium symporter activity
  and GO:0005334 norepinephrine:sodium symporter activity imply Na(+)-coupled symport; OCT1
  is a Na(+)-independent uniporter (and human does not transport norepinephrine). These are
  Ensembl ortholog projections carrying the wrong mechanistic class.
- GO:0010248 establishment/maintenance of transmembrane electrochemical gradient →
  MARK_AS_OVER_ANNOTATED: OCT1 transport is DRIVEN BY the membrane potential; it does not
  establish/maintain the gradient.
- GO:0098793 presynapse → REMOVE: automated inter-ontology inference from "serotonin uptake";
  OCT1 is a hepatic/epithelial transporter, not a neuronal presynaptic transporter.
- GO:0072237 metanephric proximal tubule development → MARK_AS_OVER_ANNOTATED: OCT1 is
  expressed in and transports cations across proximal tubule, but does not execute tubule
  development (necessity/expression ≠ participation in the developmental process).
- GO:0006805 xenobiotic metabolic process → MARK_AS_OVER_ANNOTATED: OCT1 transports
  xenobiotics (uptake), it does not metabolize them.
- Obsolete term GO:0072530 (purine-containing compound transmembrane transport) → REMOVE.
- General/root terms entailed by asserted specifics → TOO_GENERAL (no replacement):
  GO:0022857 transmembrane transporter activity, GO:0055085 transmembrane transport,
  GO:0016020 membrane, GO:0015837 amine transport.
- GO:0005515 bare protein binding (IntAct IPI with CERS2/SMIM3) → REMOVE per protein-binding
  policy (uninformative). Partners of unclear functional significance.
- IBA rows (plasma membrane, transmembrane transporter activity, transmembrane transport):
  ACCEPT/TOO_GENERAL by term; target's own UniProtKB:O15245 in WITH/FROM is expected
  (experimental grounding on target), not circular.
- Blood-brain-barrier rows (GO:0150104, NAS) KEEP_AS_NON_CORE — OCT1 BBB transport is
  documented for some substrates (pentamidine, PMID:28362799) but peripheral/debated.

## Key references (cached)

- PMID:9260930, PMID:9187257 — cloning/characterization of human OCT1 (polyspecific OC transport).
- PMID:24961373 — high-capacity thiamine transporter; metformin target; hepatic steatosis.
- PMID:15817714 — ACh transport, airway apical localization.
- PMID:12719534 — basolateral localization; variant characterization.
- PMID:35469921 — human vs mouse ortholog substrate differences; adrenaline/serotonin/histamine/thiamine kinetics.
- PMID:34040533 — isobutyrylcarnitine biomarker; human does not transport carnitine/noradrenaline.
- PMID:11907186 — prostaglandin (PGE2/PGF2a) transport.
- PMID:21128598 — polyamine (putrescine/agmatine) transport.
- PMID:23567998 — quaternary ammonium (TEA) transport.
