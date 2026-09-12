# MTHFR (human, P42898) — review notes

## Deep research status
`just deep-research-falcon human MTHFR` failed immediately with a Python
environment error in `scripts/deep_research_wrapper.py`
(`TypeError: unsupported operand type(s) for |: 'type' and 'NoneType'` — PEP 604
`dict | None` annotation under an older interpreter). No `-deep-research-falcon.md`
was produced. Per instructions I did NOT fabricate one. The review is grounded in:
- `MTHFR-uniprot.txt` (SwissProt P42898, entry v223)
- `MTHFR-goa.tsv` (seeded GOA)
- cached primary literature in `publications/PMID_*.md` (all 11 cited PMIDs are cached)

## Core biology (verified)
MTHFR (EC 1.5.1.53) is the cytosolic, FAD-dependent, NAD(P)H-linked
methylenetetrahydrofolate reductase. It catalyses the physiologically
irreversible reduction of 5,10-methylene-THF (CH2-THF) to 5-methyl-THF (CH3-THF),
the committed step channelling folate one-carbon units into the methionine cycle.
CH3-THF is the methyl donor used by methionine synthase (MTR) to remethylate
homocysteine to methionine. [PMID:29891918 "MTHFR catalyzes the physiologically
irreversible reduction of 5,10-methylene-tetrahydrofolate (CH2-THF) to
5-methyl-tetrahydrofolate (CH3-THF), a reaction requiring FAD as a cofactor and
NADPH as an electron donor. Since the product CH3-THF is exclusively used by
methionine synthase ... MTHFR commits THF-bound one-carbon units to the methionine
cycle."]

- Homodimer; asymmetric dimerization juxtaposes N-terminal Ser-rich
  phosphoregion with C-terminal eukaryote-only SAM-binding domain. Allosterically
  inhibited by S-adenosylmethionine (SAM); N-terminal phosphorylation increases
  sensitivity to SAM inhibition. [PMID:29891918]
- FAD cofactor confirmed structurally and biochemically. [PMID:29891918; PMID:20236116 (UniProt COFACTOR)]
- Kinetics: KM 22.4 uM CH2-THF, 35.5 uM NADPH, 3760 uM NADH (strong NADPH
  preference); kcat 40.7 /s. [PMID:29891918, file:uniprot]
- Deficiency: severe MTHFR deficiency (MIM 236250 / gene 607093) — autosomal
  recessive homocystinuria/hyperhomocysteinaemia; common c.677C>T (p.Ala222Val)
  thermolabile variant is a folate-sensitive risk factor for NTDs, vascular
  disease, etc. [PMID:12673793, PMID:25736335, PMID:10551815]
- Cytosolic. [UniProt IBA/IEA; Reactome R-HSA-200676]

## Annotation-level notes
- Two `protein binding` IPIs (PMID:28514442 BioPlex2.0, PMID:33961781 BioPlex3.0)
  are the same high-throughput AP-MS interaction (both with SMPD2/O60906). Bare
  `protein binding` -> MARK_AS_OVER_ANNOTATED (not REMOVE per policy).
- GO:0044877 protein-containing complex binding (IPI, PMID:24769206,
  ComplexPortal:CPX-2007) — MTHFR homodimer complex; keep as non-core.
- Heterochromatin maintenance (GO:0070828, PMID:24769206) and neural tube closure
  (GO:0001843, several PMIDs) are downstream/indirect (acts_upstream_of) —
  KEEP_AS_NON_CORE.
- Ensembl-projected "response to X" IEAs (GO_REF:0000107) are generic
  ortholog-transfer terms, not core; several are weakly supported -> mostly
  KEEP_AS_NON_CORE, with the least specific ones marked over-annotated.
- GO:0072341 modified amino acid binding (IDA, PMID:20031578) — that paper is a
  GWAS of plasma homocysteine; it provides NO IDA binding evidence for MTHFR.
  Likely mis-attributed evidence code/reference; the abstract+full text contain no
  MTHFR binding assay. Mark over-annotated (cannot verify the binding claim).
- GO:0050667 homocysteine metabolic process (IDA, PMID:20031578) — same GWAS
  paper; genetic association, not IDA. MTHFR does act upstream of homocysteine
  levels but the IDA/reference pairing is weak -> KEEP_AS_NON_CORE.
</content>
