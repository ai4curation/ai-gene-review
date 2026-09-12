# ATP5MD / ATP5MK (DAPIT / USMG5) review notes

UniProtKB: **Q96IX5** (ATPMK_HUMAN). 58 aa protein; single-pass transmembrane
(TRANSMEM 23-45). HGNC:30889, gene symbol now **ATP5MK** (prior ATP5MD; synonyms
DAPIT, HCVFTP2, USMG5). "ATP synthase F(0) complex subunit k, mitochondrial".

Deep research: falcon provider OUT OF CREDITS (402) at time of review — no
`-deep-research-falcon.md` generated. This review is grounded in the UniProt record,
the seeded GOA, and cached publications.

## Core biology (from UniProt Q96IX5 + cached PMIDs)

- **Subunit k of mitochondrial F1Fo ATP synthase (Complex V)**, part of the membrane
  F(0) domain [UniProt FUNCTION: "Subunit k, of the mitochondrial membrane ATP synthase
  complex (F(1)F(0) ATP synthase or Complex V)"; "Part of the complex F(0) domain"].
- **Non-catalytic / structural**: the complex (not this subunit) has the catalytic /
  rotary activity. UniProt: "In vivo, can only synthesize ATP although its ATP hydrolase
  activity can be activated artificially in vitro" — this refers to the whole complex.
  Subunit k itself is a small membrane accessory subunit; no independent catalytic MF
  should be invented. Use GO:0005198 structural molecule activity (subunit-specific) +
  contributes_to GO:0046933 (complex rotational ATP synthase activity).
- **Required for dimerization/oligomerisation and stability of Complex V**:
  UniProt: "Required for dimerization of the ATP synthase complex and as such regulates
  ATP synthesis in the mitochondria (PubMed:21345788, PubMed:29917077)". The complex
  "exists as a monomeric and a dimeric supercomplex that helps shape mitochondrial
  cristae to optimize proton flow (PubMed:29917077)".
- **Localisation**: Mitochondrion inner membrane / membrane; single-pass membrane protein.

## Key papers

- **PMID:21345788** (Ohsakaya 2011, JBC) — DAPIT knockdown in HeLa causes loss of ATP
  synthase population in mitochondria; reduced mitochondrial ATP synthesis activity;
  slower growth; α/β mRNA unchanged. Supports FUNCTION (complex stability, ATP synthesis)
  and mitochondrial membrane localization (EXP). Abstract-only cache (full_text_available:
  false).
- **PMID:29917077** (Barca 2018, HMG) — USMG5 (=ATP5MK) Ashkenazi founder splice mutation
  causes Leigh syndrome (MC5DN6). Mutation reduced CV **dimer** expression and ATP
  synthesis rate without altering monomeric CV; WT cDNA rescue restored dimerization and
  ATP production. Supports complex membership (IMP), dimerization role, ATP synthesis,
  inner-membrane localization. Abstract-only cache.
- **PMID:26297831** (Fujikawa 2015, FEBS Lett) — human ATP synthase assembly via two
  intermediates (F1-c-ring, b-e-g). Used by ComplexPortal as NAS reference for complex
  membership + PMF-driven ATP synthesis + inner-membrane localization. Abstract foregrounds
  d-subunit knockdown; ComplexPortal curator used full text / complex context. Abstract-only.
- **PMID:34800366** (Morgenstern 2021, Cell Metab) — high-confidence human mitochondrial
  proteome; HTP evidence for mitochondrion localization. Full text available but gene named
  only in supplementary tables (not in extracted body text). Cite verbatim framing phrase.

## GOA (17 annotations, lines 2-18)

All CC/BP terms consistent with a mitochondrial Complex V Fo subunit:
- GO:0045259 proton-transporting ATP synthase complex (IBA, NAS, ISS, IMP) — ACCEPT (core)
- GO:0005743 mitochondrial inner membrane (NAS, TAS x4) — ACCEPT (core location)
- GO:0031966 mitochondrial membrane (IEA, EXP x2) — ACCEPT (correct but less specific than 0005743)
- GO:0005739 mitochondrion (IEA, IDA, HTP, IMP) — ACCEPT (correct but least specific)
- GO:0015986 proton motive force-driven ATP synthesis (NAS) — ACCEPT (core BP)

No annotations warrant REMOVE. No bare `protein binding` IPIs present. No IEAs are wrong.

## core_functions term IDs (verified via OLS)

- GO:0005198 structural molecule activity (MF, subunit-specific)
- GO:0046933 proton-transporting ATP synthase activity, rotational mechanism (contributes_to)
- GO:0042776 proton motive force-driven mitochondrial ATP synthesis (BP)
- GO:0033615 mitochondrial proton-transporting ATP synthase complex assembly (BP)
- GO:0005743 mitochondrial inner membrane (location)
- GO:0045259 proton-transporting ATP synthase complex (in_complex)
