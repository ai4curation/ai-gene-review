# DPYD (Q12882) review notes

Human dihydropyrimidine dehydrogenase [NADP(+)], EC 1.3.1.2. Deep research (falcon) was
NOT run — the falcon provider is out of credits (HTTP 402). This review is grounded in the
UniProt record (`DPYD-uniprot.txt`), the seeded GOA (`DPYD-goa.tsv`), cached publications,
and the two cached Reactome entries.

## Core biology (from UniProt Q12882 + primary literature)

- Initial and rate-limiting enzyme of pyrimidine (uracil/thymine) catabolism. Reduces
  uracil to 5,6-dihydrouracil and thymine to 5,6-dihydrothymine, using NADPH.
  UniProt FUNCTION: "Catalyzes the reduction of uracil and thymine (PubMed:1512248)."
  Catalytic activity: "5,6-dihydrouracil + NADP(+) = uracil + NADPH + H(+)" (RHEA:18093,
  physiological direction right-to-left) and "5,6-dihydrothymine + NADP(+) = thymine +
  NADPH + H(+)" (RHEA:58284). [file:human/DPYD/DPYD-uniprot.txt]
- Large homodimeric flavoprotein. Each subunit binds 2 FAD, 2 FMN and 4 [4Fe-4S]
  clusters (~16 Fe/subunit). UniProt COFACTOR notes: "Binds 2 FAD", "Binds 2 FMN",
  "Binds 4 [4Fe-4S] clusters. Contains approximately 16 iron atoms per subunit." SUBUNIT:
  Homodimer. [file:human/DPYD/DPYD-uniprot.txt]
- PMID:1512248 (Lu, Zhang, Diasio 1992): purified human liver DPD to homogeneity,
  ~210 kDa, two subunits, "four flavin nucleotide molecules (two each of FAD and FMN)
  and 33 iron atoms per molecule of enzyme." Kinetics on uracil, thymine, 5-FU, NADPH.
  KM 4.9 uM uracil, 4.8 uM thymine, 3.3 uM 5-FU (UniProt).
- PMID:8083224 (Yokota et al. 1994): cloned human + pig DPD cDNA; pig enzyme expressed in
  E. coli "catalyzed the reduction of uracil, thymine, and 5-fluorouracil"; identified
  NADPH/FAD binding domains at N-terminus and two [4Fe-4S] motifs near the C-terminus;
  uracil-binding site between them; DPYD mapped to chromosome 1 (1p22-q21). Title links
  the enzyme to "5-fluorouracil toxicity and congenital thymine uraciluria."
- Cytosolic. UniProt SUBCELLULAR LOCATION: Cytoplasm; Reactome R-HSA-73585/73616 describe
  "Cytosolic dihydropyrimidine dehydrogenase." GO cytosol is the standard, well-supported
  location.
- Product of the pathway feeds into beta-alanine biosynthesis (UniProt PATHWAY:
  "Amino-acid biosynthesis; beta-alanine biosynthesis"). This is a downstream, pathway-
  membership annotation (DPD makes dihydrouracil; DPYS then opens the ring; UPB1 releases
  beta-alanine), so it is non-core for DPYD's molecular function.

## Pharmacogenetics / disease

- Principal catabolic enzyme for the fluoropyrimidine chemotherapeutic 5-fluorouracil
  (5-FU). UniProt FUNCTION: "Also involved the degradation of the chemotherapeutic drug
  5-fluorouracil (PubMed:1512248)." >80% of administered 5-FU is inactivated by DPD.
- DPD deficiency (DPYDD, MIM:274270): autosomal recessive; partial deficiency → severe/
  life-threatening 5-FU/capecitabine toxicity; complete deficiency → thymine-uraciluria
  with variable neurology. PMID:11988088 (van Kuilenburg et al. 2002): "Dihydropyrimidine
  dehydrogenase (DPD) deficiency is an autosomal recessive disease characterized by
  thymine-uraciluria in homozygous deficient patients. Cancer patients with a partial
  deficiency of DPD are at risk of developing severe life-threatening toxicities after
  the administration of 5-fluorouracil." Disease-causing missense variants mapped onto the
  pig DPD 3D structure interfere with cofactor binding/electron transport. Major
  pharmacogenetic gene; DPYD genotyping guides fluoropyrimidine dosing.

## Annotation-specific notes / flags

- GO:0006145 purine nucleobase catabolic process (IMP, PMID:11988088): DPD is a
  PYRIMIDINE enzyme; the cited paper concerns DPD deficiency and pyrimidine
  (uracil/thymine) catabolism, not purine catabolism. This looks like a term-selection /
  data-entry error (purine vs pyrimidine). Per the reviewer policy for experimental
  annotations whose full text I cannot fully verify, I do NOT REMOVE it; flagged
  MARK_AS_OVER_ANNOTATED with a note that GO:0006208 (pyrimidine) is the intended term.
- GO:0006212 uracil catabolic process (IDA, PMID:18075467) and GO:0017113 (IDA,
  PMID:18075467): the cached abstract of PMID:18075467 (Thomas et al. 2007) is about
  DIHYDROPYRIMIDINASE (DHP, gene DPYS) — the SECOND enzyme in pyrimidine catabolism — and
  about the [2-13C]-uracil breath test measuring overall uracil catabolism, not about DPD
  activity per se. DHP does not have DPD (GO:0017113) activity. I keep the uracil catabolic
  process annotation (correct process, and the paper's breath-test work concerns overall
  uracil catabolism in which DPD is the first step) as KEEP-worthy but the GO:0017113 IDA
  on this reference is a mis-fit; marked MARK_AS_OVER_ANNOTATED rather than REMOVE
  (experimental, full text not read). The core GO:0017113 support comes from PMID:1512248,
  PMID:8083224 and IBA.
- GO:0046045 TMP catabolic process and GO:0046050 UMP catabolic process (IDA,
  PMID:8083224): DPD acts on the free pyrimidine BASES (uracil, thymine), not on the
  nucleotides UMP/TMP. These monophosphate-catabolism terms are over-specific/upstream of
  DPD's actual reaction; marked MARK_AS_OVER_ANNOTATED. UniProt itself lists these only as
  MGI IEA/IDA transfers.
- GO:0042178 xenobiotic catabolic process (IDA, PMID:8083224): this captures DPD's role in
  catabolising 5-FU (a drug/xenobiotic). Real and well-supported, but a downstream/context
  role rather than DPD's endogenous core function; KEEP_AS_NON_CORE.
- GO:0005515 protein binding (IPI, PMID:25416956; partners LXN Q9BS40 and GOPC Q9HD26):
  bare "protein binding" is uninformative and these Y2H interactome hits have no
  established functional role for DPD; MARK_AS_OVER_ANNOTATED.
- GO:0016491 oxidoreductase activity (IEA InterPro): correct but far too general given the
  specific GO:0017113; MODIFY → GO:0017113.
- GO:0016627 oxidoreductase activity, acting on the CH-CH group of donors (IEA InterPro):
  a true ancestor of GO:0017113 (DPD reduces the C5-C6 double bond); accurate but general;
  MODIFY → GO:0017113.

## Core functions (for core_functions block)

1. MF GO:0017113 dihydropyrimidine dehydrogenase (NADP+) activity — with FAD, FMN,
   [4Fe-4S] cofactors and NADP binding; substrate uracil binding. Located in cytosol.
   Directly involved in thymine and uracil catabolic processes (GO:0006210, GO:0006212;
   parent GO:0006208 pyrimidine nucleobase catabolic process).
