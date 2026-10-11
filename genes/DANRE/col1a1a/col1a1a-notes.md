# col1a1a notes

## 2026-09-28 (claude-opus-5-5, DANRE_DUPLICATION pair review col1a1a/col1a1b)

- **Deep research failed.** Edison returned 402 Payment Required and the OpenAI key is invalid. It was not retried. The literature research below was done by hand (Europe PMC REST search plus cached publications).
- Accession Q6U1J5 (1447 aa, TrEMBL, EMBL AAR24536 "Chihuahua", RefSeq NP_954684). It holds all GOA rows (27).
- Identity: [PMID:26876635 "In zebrafish the existence of three genes, col1a1a, col1a1b and col1a2 coding for collagen type I α1, α3 and α2 chains was reported"].
- TGD origin: PANTHER TGD_tree (Neopterygii|Teleostei, 1 gar co-ortholog, 2 medaka). Literature: [PMID:26876635 "The similarity between α1(I) and α3(I) suggested that the genes for both proteins probably originated from the duplication of an ancestor α(I) coding gene during the whole genome duplication event that occurred ~320 mya at the basis of teleost evolution"].
- Expression: co-expressed with col1a1b and col1a2 [PMID:26876635 "The expression profiles of all three type I collagen genes were highly similar, with a peak in relative expression between 3 and 4 dpf"], except in the fin fold [PMID:26876635 "Interestingly, only col1a1a was shown to be expressed in the median fin fold and in the apical ectodermal ridge of the pectoral fin at 48, 72 and 96 hpf"].
- Loss of function (PMID:30082390, full text): the col1a1a sa1748 null is lethal [PMID:30082390 "Eventually, all genotypes containing a homozygous knockout of col1a1a [loss of α1(I)] were found to be lethal by the age of 3 mo."]. It lacks actinotrichia [PMID:30082390 "Upon detailed examination of the finfold, these actinotrichia were found to be absent in col1a1a−/− mutant larvae (Fig. 5D)."]. The heterozygote is normal; the double heterozygote with col1a1b is fragile.
- Dominant alleles: chihuahua dc124 [PMID:14623232 "Heterozygous chihuahua fish have phenotypic similarities to human osteogenesis imperfecta"]; dmh13 and dmh14 [PMID:28835471 "Both the dmh13 and dmh14 mutants carry mutations in the col1a1a gene (G1093R; G1144E)"].
- **ZFIN genotype check** (zfin.org pages fetched 2026-09-28):
  - 180503-6 = col1a1a^dmh13/+
  - 180504-3 = col1a1a^dmh14/+
  - 110630-21 = col1a1a^dc124/+
  - **180503-7 = col1a1b^dmh29/+**
  - **180503-8 = col1a2^dmh15/+**
  - 190402-1 = col1a1a^sa1748/+; col1a1b^sa12931/+
  - 221115-1 = col1a1a^dc124/+
  - 011017-1 = col1a1a^dc124
  - 111013-8 = col1a1a^tt281/tt281
  - MRPHLNO-110630-1 = MO2-col1a1a

  Two col1a1a skeletal system development IMP rows (PMID:30082390) therefore rest on genotypes with no col1a1a lesion. Those two rows are marked REMOVE; the term is kept through the other rows.
- **Cytoplasm IDA (PMID:19757382).** The full text was read. col1a1 is only an mRNA FISH marker [PMID:19757382 "double fluorescent in situ hybridizations for grhl1 and the keratinocyte markers collagen 1a1"]. The IDA row is MARK_AS_OVER_ANNOTATED. The IBA cytoplasm row (PTN002771199, sole source col1a1a) is REMOVE, and the same is done on col1a1b.
- Decisions:
  - skeletal system development: IMP ACCEPT (col1a1a alleles); 2 mis-attached rows REMOVE.
  - regulation of ossification: MODIFY to ossification (GO:0001503). Structural, not regulatory.
  - fin development and fin morphogenesis: ACCEPT (copy-specific actinotrichia role). Pectoral fin development (morphant) and fin regeneration: non-core.
  - bone mineralization, bone mineralization involved in bone maturation, and bone remodeling: non-core (downstream or indirect).
  - collagen fibril organization (IBA and IMP), ECM structural constituent conferring tensile strength, ECM, extracellular region, ECM structural constituent: ACCEPT.
  - skin development and skeletal system morphogenesis (IBA): non-core.
  - NEW GO:0005584 collagen type I trimer (IDA, PMID:26876635). Comparator: human COL1A1 carries it by IDA/IPI/IMP (QuickGO, 2026-09-28).
- Pair page: projects/DANRE_DUPLICATION/pairs/col1a1a_col1a1b/col1a1a_col1a1b.md
