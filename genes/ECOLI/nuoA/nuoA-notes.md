# nuoA (E. coli K-12, P0AFC3) notes

## 2026-10-23 review session

- Deep-research providers are unavailable in this environment (no API keys), so
  no `-deep-research-*.md` file exists. Literature was reviewed manually from
  cached `publications/PMID_*.md` files (most abstract-only) and the UniProt
  record.
- NuoA is a three-TMH membrane subunit of NDH-1; C terminus cytoplasmic
  [PMID:21925501 "the c-terminal end of the polypeptide is localized in the bacterial cytoplasm"].
- Membrane-domain structure: NuoA is one of six resolved membrane subunits and
  the fourth proton channel lies at the N/K/J/A interface
  [PMID:21822288 "The fourth probable proton-translocation channel is at the interface of subunits N, K, J and A."].
- E. coli cryo-EM (newly cached, full text): [PMID:34308841 "The conserved region of the NuoA TMH1-TMH2 loop forms a plug, which fills a crevice between the subunits NuoD, NuoB, and NuoH."].
- Thermus orthologue Nqo7: [PMID:23417064 "The first cytoplasmic loop from Nqo7/NuoA wraps around Nqo8"].
- Every nuo gene is needed for a functional complex [PMID:22063474 "Thus, all nuo-genes are required either for the assembly or the stability of a functional E. coli complex I."].
- Decisions: GO:0050136 (non-electrogenic) REMOVED - NDH-1 pumps protons, NDH-2
  does not [PMID:3122832 "whose turnover does not lead to generation of a H+ electrochemical gradient"].
  General terms (GO:0003954, GO:0016651, GO:0016020, GO:0030964) MODIFIED to
  GO:0008137 / GO:0005886 / GO:0045271. IMP row from PMID:8366049 accepted
  deferring to curator (abstract does not name the gene; possible polarity noted).
- Core function: contributes_to GO:0008137, in complex I, plasma membrane.
