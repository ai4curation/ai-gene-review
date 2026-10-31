# SMIM3 (NID67, C5orf62) notes

## 2026-10-08: initial review (MICROPROTEINS Tier 2)

**Identity.** UniProt Q9BZL3, 60 aa, Swiss-Prot reviewed, MANE-select canonical gene product on
5q33.1 (not an alternative ORF, so the standard `genes/human/SMIM3/` folder applies). One
predicted TM helix (residues 20-40); a "Cleavage" site 19-20 is propagated by similarity from
the mouse entry (Q99PE6) and is not experimentally shown for human.

**Literature.** PubMed `SMIM3[tiab] OR NID67[tiab]` returns 10 papers. Only two say anything
about the protein:

- Cloning in rat PC12 cells [PMID:11288140 "We now report the cloning of a previously unknown
  primary response gene, NID67."]. Induced by NGF and FGF, also forskolin, A23187 and ATP. mRNA
  highest in heart, ovary and adrenal. ORF confirmed by in vitro translation [PMID:11288140 "In
  vitro transcription and translation reactions confirmed that the ORF we identified produces a
  6000 Da protein product."]. The ion-channel role is speculation by analogy [PMID:11288140
  "NID67 may play a similar role in cellular physiology."]. Abstract-only in cache.
- AML study [PMID:36550462 "Knockdown of SMIM3 inhibited cell proliferation and cell cycle
  progression, and induced cell apoptosis in AML cells."]; reduced p-PI3K/p-AKT after knockdown.
  Correlative, single shRNA approach, no rescue, no mechanism. Not used for any GO term.
- Mouse 5q- model [PMID:19966810 "Haploinsufficiency of the Cd74-Nid67 interval (containing
  Rps14, encoding the ribosomal protein S14) caused macrocytic anemia"]. Nid67 is only a deletion
  boundary; phenotype attributed to Rps14/p53.
- The rest are expression-signature papers (IVDD, OSCC, radiation dose) and 5q- reviews; not
  cached, not informative about function.

**GOA (60 rows).**
- 58 x GO:0005515 protein binding IPI from four binary-interactome screens (HuRI 47, HI-II-14 9,
  Sahni 2015 2, CCSB-HI1 1). Partners are ~55 mostly unrelated membrane proteins (PMP22, MAL,
  BSCL2, CNIH1/3, EMP1/3, claudins, tetraspanins, ATP6V0C, SLC22A1, CLEC7A...): the typical
  sticky single-TM-helix Y2H signature also seen for STRIT1. All REMOVE per project policy.
- 1 x GO:0042802 identical protein binding (HuRI self-pair): MARK_AS_OVER_ANNOTATED.
- 1 x GO:0016020 membrane IEA (SubCell): ACCEPT; the only supportable statement.

**Outcome.** No MF or BP term is supported. Core function records membrane location only. No
NEW proposals: the AML proliferation phenotype is a knockdown necessity result with no
mechanism, and fails the participation test.
