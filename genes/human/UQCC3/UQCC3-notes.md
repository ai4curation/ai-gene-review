# UQCC3 (C11orf83) review notes

UniProtKB:Q6UW78 · HGNC:34399 · human, chromosome 11. 93 aa, single-pass inner
mitochondrial membrane protein. No falcon deep-research file (falcon out of credits,
HTTP 402); grounded review in UniProt record, seeded GOA, and cached abstracts for
PMID:25008109 and PMID:25605331 (both `full_text_available: false`).

## Function (verified)
UQCC3 is the human functional equivalent of yeast Cbp4p, a **respiratory Complex III
(cytochrome bc1 / ubiquinol-cytochrome c reductase) assembly factor** in the
mitochondrial inner membrane. It is **non-catalytic** (no EC, no enzymatic MF).

- Complex III assembly factor, acts downstream of UQCC1/UQCC2; stabilises the
  cytochrome-b-containing early assembly intermediate ("bc1 core complex")
  [PMID:25008109 abstract "UQCC3 functions in the complex III assembly pathway
  downstream of UQCC1 and UQCC2"; PMID:25605331 abstract "involved in the early stages
  of its assembly by stabilizing the bc1 core complex"].
- Required for cytochrome b (MT-CYB) stability; in patient cells lacking UQCC3,
  cytochrome b levels are lower and it is absent from the high-MW complex III
  [PMID:25008109].
- Cardiolipin-binding (via α-helices 2 and 3), influences cardiolipin composition and
  cristae/crista morphology; stabilises bc1-containing supercomplexes, especially
  III2/IV [PMID:25605331]. UniProt CHAIN region 23–80 "Mediates lipid-binding".
- OMA1 cleaves UQCC3 upon mitochondrial depolarization (stress) [PMID:25605331].
- Topology: matrix N-terminus (1–7), TM helix (8–28), IMS-facing C-terminus (29–93).
  N-terminal RK (res 5–6) needed for mitochondrial targeting [PMID:25605331 mutagenesis].

## Disease
Mitochondrial complex III deficiency, nuclear type 9 (MC3DN9; MIM:616111):
lactic acidosis, hypoglycemia, hypotonia, delayed development. Causal homozygous
c.59T>A (V20E) variant [PMID:25008109].

## GOA review decisions (13 annotations)
- GO:0005743 mito inner membrane — IBA(is_active_in), IEA(SubCell), IDA×2 → ACCEPT (core CC). Strong IDA support.
- GO:0006122 mito electron transport ubiquinol→cyt c — IBA, IMP(25008109) → KEEP_AS_NON_CORE.
  UQCC3 is a non-catalytic assembly factor; it enables electron transport indirectly
  (via building complex III), it is not itself part of the electron-transfer machinery.
  Keep (IMP is defensible: loss abolishes CIII activity) but non-core; core is assembly.
- GO:0034551 CIII assembly — IBA, IEA(InterPro), IMP(25605331) → ACCEPT (CORE BP).
- GO:0005739 mitochondrion — IDA(HPA), HTP(34800366) → ACCEPT (correct, less specific than IMM).
- GO:0042407 cristae formation — IMP(25605331) → KEEP_AS_NON_CORE. Real phenotype
  (abnormal crista morphology on depletion) but a downstream/pleiotropic consequence of
  CIII/supercomplex/cardiolipin roles, not the core molecular activity.
- GO:0070300 phosphatidic acid binding — IDA(25605331) → KEEP_AS_NON_CORE. From full
  text (abstract only mentions cardiolipin); can't quote from cache & can't REMOVE an
  experimental IDA per policy. Lipid-binding region 23–80 in UniProt supports lipid
  binding generally. Cardiolipin is the physiologically salient ligand; PA binding kept non-core.
- GO:1901612 cardiolipin binding — IDA(25605331) → ACCEPT (core MF; the one informative
  molecular function). Abstract: "C11orf83 binds to cardiolipin by its α-helices 2 and 3".

## core_functions
- MF: cardiolipin binding (GO:1901612) — the sole informative, verified MF.
- BP: mitochondrial respiratory chain complex III assembly (GO:0034551).
- CC: mitochondrial inner membrane (GO:0005743).
No catalytic MF (non-enzymatic assembly factor). Do NOT invent one.
