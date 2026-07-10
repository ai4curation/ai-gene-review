# ALAD (P13716) review notes

Human delta-aminolevulinic acid dehydratase / porphobilinogen synthase (PBGS), EC 4.2.1.24.
Deep research: falcon provider is out of credits (HTTP 402); no `-deep-research-falcon.md`
was generated. This review is grounded in the UniProt record (`ALAD-uniprot.txt`), the seeded
GOA (`ALAD-goa.tsv`), and cached `publications/PMID_*.md` + `reactome/*.md`.

## Core biology

- **Molecular function**: porphobilinogen synthase (PBGS) / 5-aminolevulinate dehydratase.
  Catalyses the **second step of heme biosynthesis**: the asymmetric condensation of two
  molecules of 5-aminolevulinate (ALA) to form the monopyrrole porphobilinogen (PBG), with
  release of 2 H2O. RHEA:24064, EC 4.2.1.24.
  - UniProt FUNCTION: "Catalyzes an early step in the biosynthesis of tetrapyrroles. Binds two
    molecules of 5-aminolevulinate per subunit, each at a distinct site, and catalyzes their
    condensation to form porphobilinogen." [file:human/ALAD/ALAD-uniprot.txt]
  - Reactome R-HSA-189439: "catalyzes the asymmetric condensation of two molecules of ALA to
    form porphobilinogen (PBG)." "PBG is the first pyrrole formed, the precursor to all
    tetrapyrrole pigments such as heme and chlorophyll."
  - PMID:19812033 / PMID:12897770: "catalyzes the first common step in tetrapyrrole" biosynthesis.
- **Cofactor / metal ion**: Zn2+-dependent metalloenzyme. Binds 8 zinc ions per homo-octamer;
  4 are required for catalysis (catalytic ZnB site, Cys122/Cys124/Cys132).
  [PMID:11032836 "purifies with eight Zn(II) per homo-octamer"; "Only four ... are required for
  activity"]. Zinc binding is a supporting/secondary MF underpinning the catalytic activity.
- **Quaternary structure / allostery**: equilibrium of high-activity homooctamer and
  low-activity homohexamer; a bound Mg2+ promotes octamer assembly. Morpheein/allosteric enzyme.
  [PMID:12897770; PMID:19812033]
- **Localisation**: cytosol (GO:0005829). Second (and following three) steps of heme synthesis
  occur in the cytosol (Reactome R-HSA-189451: "The next four steps take place in the cytosol").
- **Disease**: ALAD-deficiency porphyria (Doss porphyria / acute hepatic porphyria AHEPP,
  MIM:612740); loss-of-function variants (G133R, V275M, R240W, A274T, V153M, F12L) shift the
  quaternary equilibrium toward the low-activity hexamer. [PMID:2063868; PMID:17236137]
- **Lead poisoning**: ALAD is the classic biomarker/target of lead poisoning; Pb2+ inhibits by
  partially displacing the catalytic zinc. [PMID:11032836 "is a main target in lead poisoning";
  Reactome R-HSA-190141 "Lead binds to ALAD enzyme displacing half the zinc ions essential for
  its catalytic activity and inactivating it"]. Supports GO:0032791 lead ion binding (EXP).

## Moonlighting / non-catalytic

- ALAD = CF-2, a 240-kDa endogenous proteasome inhibitor (ATP-stabilized component of the 26S
  proteasome). [PMID:8175643 "inhibitory factor is indistinguishable from delta-aminolevulinic
  acid dehydratase (ALAD), the second enzyme in the pathway of heme"]. This is a bona fide
  moonlighting function (MoonProt/MoonDB list ALAD), supporting GO:0004655 IDA (CAFA),
  GO:1904854 proteasome core complex binding, and GO:1901799 negative regulation of proteasomal
  protein catabolic process. Kept as non-core relative to the heme-synthesis catalytic role.

## Annotation review strategy

- Core MF: GO:0004655 porphobilinogen synthase activity (EXP/IDA/IBA/TAS/IEA) — ACCEPT.
- Core BP: GO:0006783 heme biosynthetic process (IBA/IDA/TAS/IEA) — ACCEPT; GO:0006785 heme B
  biosynthetic process (IDA) is a valid specific child — ACCEPT; GO:0033014 tetrapyrrole
  biosynthetic process (IEA) is a correct broader parent — ACCEPT.
- Core CC: GO:0005829 cytosol (IBA/IEA/ISS/TAS) — ACCEPT.
- Secondary MF: GO:0008270 zinc ion binding (IDA), GO:0046872 metal ion binding (IEA),
  GO:0032791 lead ion binding (EXP) — ACCEPT/KEEP_AS_NON_CORE (underpin catalysis / lead
  toxicology).
- GO:0003824 catalytic activity (TAS) — MODIFY to GO:0004655 (too general).
- GO:0042802 identical protein binding (IPI) + GO:0051260 protein homooligomerization (IPI):
  ALAD is a genuine homo-octamer; homooligomerization is functionally meaningful (octamer =
  active form). Keep homooligomerization as non-core; identical protein binding is the bare
  "protein binding"-style term — MARK_AS_OVER_ANNOTATED per policy (not REMOVE for an IPI).
- Moonlighting proteasome terms (GO:1904854, GO:1901799) — KEEP_AS_NON_CORE.
- Localisation noise: nucleus (HDA, sperm-nucleus proteomics), extracellular exosome (HDA),
  extracellular region + secretory/ficolin granule lumen (Reactome neutrophil degranulation) —
  KEEP_AS_NON_CORE (high-throughput / bystander localisations for an abundant cytosolic enzyme;
  not core). Cannot REMOVE experimental HDA/TAS per policy.
- Large GO_REF:0000107 Ensembl-projected "response to X" block (~30 terms) + response to
  hypoxia/oxidative stress: these are electronic (IEA, ECO:0000265) transfers from rat ortholog
  P06214 of a huge, largely non-specific stimulus-response profile. Most are over-propagated and
  not informative of ALAD's molecular role; MARK_AS_OVER_ANNOTATED. The lead/metal-response ones
  (response to lead ion, cellular response to lead ion, response to metal ion) are biologically
  defensible given ALAD's role as the lead target — KEEP_AS_NON_CORE.
- GO:1904854 proteasome core complex binding (IEA, Ensembl) duplicates the moonlighting role
  captured experimentally by PMID:8175643 — KEEP_AS_NON_CORE.
</content>
