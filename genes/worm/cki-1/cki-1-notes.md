# cki-1 (C. elegans) research notes

UniProt: Q22197 (CKI1_CAEEL, Swiss-Prot), 184 aa. ORF T05A6.1, WormBase WBGene00000516.
CIP/KIP family cyclin-dependent kinase inhibitor (Pfam PF02234 CDI; InterPro IPR003175;
PANTHER PTHR10265:SF46). Human ortholog per the Alliance: CDKN1B (p27/KIP1). The adjacent
gene cki-2 (T05A6.2) is the second worm CIP/KIP member.

## Provenance of this research

- Automated deep research was **not available** (no FutureHouse, Perplexity or OpenAI keys
  in this environment); no `-deep-research-<provider>.md` file exists. Literature work is
  manual.
- WormBase hand-written description fetched with
  `just mod-description-deep-research worm cki-1` and used as a recall checklist.
- Queries run (2026-11-16): PubMed esearch `(cki-1[tiab] OR CKI-1[tiab]) AND elegans`
  (31 hits, all titles scanned); web search for Tilmann & Kimble 2005 (cki-1 content of
  PMID:16198291; full text not retrievable).
- Cached with `just fetch-pmid` (beyond the GOA papers): 21074724 (full text), 16631585,
  12885569, 14597199, 19597327 (full text), 18050422, 12062054. Already cached: 17509881
  (full text), 18082681. Full text not retrievable for 16198291, 9716524, 10587644,
  11684669, 15247923.

## Identity and activity

- [PMID:9716524 "C. elegans cki-1 encodes a member of the CIP/KIP family of
  cyclin-dependent kinase inhibitors"].
- CDK target in vivo: genetic epistasis shows CKI-1 keeps cells quiescent by inhibiting
  CYE-1/CDK-2 [PMID:17476329 "Therefore, in wild-type animals, CKI-1/CKI in these cells
  maintained quiescence by inhibiting CYE-1/CDK-2, while sufficient CYE-1/CDK-2 remained
  to repress the terminal differentiation."]. UniProt records a direct interaction with
  CYD-1 (PMID:11684669, "Probable"). No in vitro kinase-inhibition assay on worm CKI-1 was
  found; the CDK inhibitor activity rests on family membership plus this genetics.
- Location: nucleus (UniProt SUBCELLULAR LOCATION, ECO:0000269 from PMID:10587644 and
  PMID:15247923). CDC-14 promotes nuclear accumulation [PMID:15247923 "cdc-14 functions
  upstream of the cki-1 Cip/Kip inhibitor to promote accumulation of CKI-1 in the
  nucleus"]. CRL2-LRR-1 controls nuclear CKI-1 in germ cells, in contrast to cytoplasmic
  p21 in human cells [PMID:21074724 "elegans LRR-1 is nuclear localized in germ cells and
  regulates the abundance of nuclear CKI-1 to control the cell cycle, while human LRR1 is
  cytoplasmic localized and regulates the abundance of cytoplasmic p21"]. No worm evidence
  for a cytoplasmic CKI-1 function was found.

## Roles

1. **G1/S control and developmental quiescence (postembryonic).**
   [PMID:9716524 "Ectopic expression of CKI-1 can prematurely arrest cells in G1, while
   reducing cki-1 activity by RNA-mediated interference (RNAi) causes extra larval cell
   divisions, suggesting a role for cki-1 in the developmental control of G1/S."];
   [PMID:11684669 "Surprisingly, loss of cki-1, but not lin-35, results in precocious entry
   into S phase."]; cki-1 and lin-35 Rb are partly independent
   [PMID:11684669 "We demonstrate that lin-35 Rb and cki-1 Cip/Kip contribute
   non-overlapping levels of G1/S inhibition in C. elegans."]; cki-2 acts in a distinct
   parallel pathway [PMID:19597327 "both cki-1 and cki-2 mediate cell cycle quiescence"].
2. **Arrest in dauer and starved L1.** [PMID:9716524 "cki-1 activity is required for the
   suspension of cell cycling that occurs in dauer larvae and starved L1 larvae in response
   to environmental signals."]; DAF-16/FOXO drives cki-1 transcription in L1 arrest
   [PMID:16631585 "We show that DAF-16 is required for transcription of the
   cyclin-dependent kinase inhibitor cki-1 in stem cells in response to starvation"].
3. **VPC quiescence.** Heterochronic genes act via cki-1 [PMID:9716524]; LIN-1/LIN-31
   promote cki-1 transcription before induction [PMID:18082681 "LIN-1 and LIN-31 promote
   cki-1/Kip-1 transcription prior to their inhibition through RTK/Ras/MAPK activation."].
4. **Embryonic cell-cycle exit, essential.** [PMID:12885569 "Our findings demonstrate that
   cki-1 activity plays an essential role in embryonic cell cycle arrest, differentiation
   and morphogenesis"]; [PMID:12885569 "RNA interference of cki-1 leads to embryonic
   lethality with phenotypes similar to, or more severe than, the deletion mutants."]. Not
   in the WormBase text, which is written about postembryonic lineages only.
5. **Cell fate in the somatic gonad.** Extra DTCs arise from aberrant SGP divisions
   [PMID:14597199 "cki-1(RNAi) animals also possess extra anchor cells and ectopic gonad
   arms with variable sheath cell numbers and positioning."]; Emo phenotype
   [PMID:14597199 "In addition, cki-1(RNAi) animals display an endomitotic oocyte (Emo)
   phenotype."]; quiescent uncommitted cells after asymmetric division (Z1.ap/Z4.pa)
   [PMID:17476329 "In contrast, in cki-1(RNAi) animals, these cells underwent extra
   divisions"].
6. **Anchor cell invasion needs G1 arrest.** [PMID:26506306 "We show that the nuclear
   receptor nhr-67/tlx directs the AC into G1 arrest in part through regulation of the
   cyclin-dependent kinase inhibitor cki-1."]; [PMID:26506306 "Strikingly, CKI-1 expression
   completely rescued AC invasion in nhr-67(pf88) hypomorphs"]. Uterine-specific cki-1 RNAi
   only rarely gave dividing ACs (full text).

## Regulators of CKI-1 protein

- CUL-2: [PMID:10587644 "cul-2 mutant germ cells undergo a G1-phase arrest that correlates
  with accumulation of CKI-1"]. Substrate receptor identified later:
  [PMID:21074724 "The nematode CRL2(LRR-1) complex negatively regulates nuclear CKI-1
  levels to ensure G1-phase cell cycle progression in germ cells."]. The UniProt FUNCTION
  still has the 1999 hedge "Cul-2 may function in ubiquitin-mediated degradation".
- CUL-4: [PMID:17509881 "CUL-4 promotes the phosphorylation and subsequent translocation
  of CDC-6 via negative regulation of the CDK-inhibitor CKI-1."].
- CDC-14 stabilises a hypophosphorylated nuclear CKI-1 [PMID:15247923].

## GO annotation thoughts

- MF: CDK serine/threonine kinase inhibitor activity (IBA, IEA) = core. Accept.
- BP core: negative regulation of G1/S transition (IBA, 2 IMP); positive regulation of G1
  to G0 transition (2 IMP, 2 IGI) - quiescence in VPCs, AC, dauer/L1.
- GO:1902806 regulation of cell cycle G1/S phase transition (IGI, PMID:11684669): the
  paper's evidence is G1/S inhibition, so MODIFY to GO:2000134 (already carried).
- GO:0051726 regulation of cell cycle (IEA): entailed by GO:2000134; TOO_GENERAL.
- regulation of cell differentiation (IMP, PMID:26506306), gonad development and
  regulation of DNA endoreduplication (IGI): real but downstream of G1 control; non-core.
- regulation of cell division (IGI x2, PMID:16198291): paper not readable here; consistent
  with CKI-1's role; GO:2000134 is not a descendant of GO:0051302, so not TOO_GENERAL.
- cytoplasm (IBA): donors are mammalian p27/p57 only; worm CKI-1 evidence is nuclear, and
  the cytoplasmic p21/p27 motility function is explicitly contrasted with worm CKI-1
  (PMID:21074724). Mark as over-annotated.
- No PAINT losses on the lineage (`just paint-losses worm cki-1`).
