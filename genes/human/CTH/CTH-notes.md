# CTH (Cystathionine gamma-lyase / CSE / CGL) — review notes

UniProtKB:P32929 (CGL_HUMAN), HGNC:2501, human. EC 4.4.1.1 (and 4.4.1.2 as homocysteine desulfhydrase).

## Deep research status

Attempted `just deep-research-falcon human CTH`. The wrapper
(`scripts/deep_research_wrapper.py`) fails immediately at import/annotation time with:
`TypeError: unsupported operand type(s) for |: 'type' and 'NoneType'` (a `dict | None`
annotation evaluated under an interpreter that does not support PEP 604 union syntax).
This is a deterministic environment/runtime error unrelated to CTH, so it aborts before
doing any research; retrying does not help. Per project policy I did NOT fabricate a
`-deep-research-*.md` file. The review is grounded in the UniProt record
(`CTH-uniprot.txt`), the seeded GOA (`CTH-goa.tsv`), and the cached
`publications/PMID_*.md` entries, which are rich for this well-characterized enzyme.

## Core biology (from UniProt CC + cached primary literature)

- **Cystathionine gamma-lyase**: catalyses the LAST/second step of the transsulfuration
  pathway (methionine -> cysteine), cleaving L,L-cystathionine into L-cysteine, NH4+ and
  2-oxobutanoate. PLP (pyridoxal-5'-phosphate)-dependent. [UniProt FUNCTION;
  PMID:10212249 abstract "high gamma-lyase activity toward L-cystathionine (Km = 0.5 mM,
  Vmax = 2.5 units/mg) with an optimum pH of 8.2"; PMID:19428278 "the enzyme that
  catalyzes the conversion of cystathionine to cysteine, ammonia, and 2-oxobutyrate"].
- **H2S biosynthesis (second physiological function)**: uses L-cysteine and
  L-homocysteine (at lower rates) to generate the gasotransmitter hydrogen sulfide.
  [PMID:19019829 title "an enzyme responsible for the production of H(2)S";
  PMID:22169477 "cystathionine-γ-lyase (CSE) ... largely responsible for the production
  of H(2)S in mammals"]. UniProt lists CATALYTIC ACTIVITY reactions for L-cysteine ->
  H2S + pyruvate + NH4+ and L-homocysteine -> 2-oxobutanoate + H2S + NH4+.
- **Cysteine-protein sulfhydrase**: converts protein -SH to -SSH (persulfidation) on
  target Cys residues (GAPDH, PTPN1/PTP1B, NF-kB RELA). [PMID:22169477 IMP:
  "Sulfhydration of PTP1B in cells required the presence of cystathionine γ-lyase (CSE)"].
- **Structure**: homotetramer; PLP bound covalently at Lys212 (N6-(pyridoxal
  phosphate)lysine). [PMID:19019829 X-ray structures apo/PLP/PLP-PAG; UniProt MOD_RES 212].
- **Localization**: Cytoplasm (UniProt SUBCELLULAR LOCATION); cytosol (Reactome TAS).
- **Tissue**: highly expressed in liver; also muscle. Estrogen receptor alpha (ESR1)
  induces expression in osteoblasts (PMID:29254196, from UniProt).
- **Disease**: Cystathioninuria (CSTNU, MIM:219500), autosomal recessive, largely benign
  ("provides no evidence that severe loss of CTH activity is accompanied by adverse
  clinical effects", PMID:19428278). Caused by loss-of-function variants (T67I, Q240E, etc.).

## Annotation decisions summary

- Core MF: **GO:0004123 cystathionine gamma-lyase activity** (multiple IDA + IBA + IEA) — ACCEPT core.
- **GO:0030170 pyridoxal phosphate binding** (IDA/IBA/IEA) — ACCEPT (cofactor).
- **GO:0019346 transsulfuration** and **GO:0019344 L-cysteine biosynthetic process**
  (IBA/IEA/IDA) — ACCEPT core process.
- **GO:0070814 hydrogen sulfide biosynthetic process** (IDA + TAS) — ACCEPT (second core role).
- **GO:0044524 protein sulfhydration** (IMP) — ACCEPT (moonlighting/persulfidation function).
- Cytosol/cytoplasm CC (IBA/IEA/TAS) — ACCEPT (one representative), others accept as duplicates.
- H2S-related lyase activities on Cys/homocysteine (GO:0047982 homocysteine desulfhydrase,
  GO:0080146 L-cysteine desulfhydrase, GO:0044540 L-cystine L-cysteine-lyase) — real
  side/promiscuous activities; ACCEPT/KEEP_AS_NON_CORE. GO:0044540 IMP from PMID:22169477
  is the cysteine-desulfhydrase measurement underlying sulfhydration; ACCEPT.
- **GO:0098606 selenocystathionine gamma-lyase activity** (IEA) & **GO:0001887 selenium
  compound metabolic process** (IEA) — By-similarity Se-substrate activity; KEEP_AS_NON_CORE.
- **GO:0018272 protein-pyridoxal-5-phosphate linkage** (IDA, Lys212) — ACCEPT (covalent PLP linkage).
- **GO:0051289 protein homotetramerization** (IPI self) — ACCEPT (documented quaternary structure).
- **GO:0042802 identical protein binding** (IPI, CTH:CTH) — reflects homotetramer; KEEP_AS_NON_CORE.
- **GO:0005515 protein binding** (bare IPI, HT interactome/Y2H) — uninformative; MARK_AS_OVER_ANNOTATED (policy: not REMOVE).
- **GO:0043066 negative regulation of apoptotic process** & **GO:0043123 positive
  regulation of canonical NF-kappaB signal transduction** (IEA from mouse ortholog) —
  downstream H2S-signaling effects; KEEP_AS_NON_CORE.
- **GO:1904831 positive regulation of aortic smooth muscle cell differentiation** (IMP,
  PMID:21659522) — CSE/H2S promotes SMC differentiation; KEEP_AS_NON_CORE.
- **GO:0030968 ER unfolded protein response** (TAS, PMID:22169477) — via sulfhydration of
  PTP1B/PERK axis; KEEP_AS_NON_CORE.
- **GO:0070062 extracellular exosome** (HDA urinary exosome proteomics) — mass-spec
  localization, not a functional site; MARK_AS_OVER_ANNOTATED.
</content>
