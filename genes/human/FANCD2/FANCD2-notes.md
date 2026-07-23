# FANCD2 (Q9BXW9) review notes

## Summary of biology
FANCD2 (Fanconi anemia group D2 protein; 1451 aa) is the central effector of the Fanconi
anemia (FA)/BRCA DNA interstrand crosslink (ICL) repair pathway. With its paralog FANCI it
forms the ID2 heterodimer. Upon replication stress/ICLs, FANCD2 is monoubiquitinated at
Lys561 by the FA core complex (E3 = FANCL, E2 = UBE2T), which converts the open ID2 trough
into a closed sliding DNA clamp that encircles duplex DNA, loading ID2 onto chromatin to
coordinate nucleolytic incision (unhooking), translesion synthesis (POLN) and homologous
recombination. It is deubiquitinated by the USP1–UAF1(WDR48) complex. FANCD2 also protects
stalled replication forks, restrains nucleases, and localizes to common fragile sites /
ultrafine anaphase bridges (with BLM). Loss causes Fanconi anemia complementation group D2:
bone marrow failure, congenital malformations, chromosomal instability, MMC/DEB
hypersensitivity, cancer predisposition.

## Key provenance (verbatim)

- ID2 clamp / monoubiquitination function:
  [PMID:32269332 "monoubiquitination triggers a complete rearrangement of the open, trough-like ID structure through the ubiquitin of one protomer binding to the other protomer in a reciprocal fashion"]
  [PMID:32269332 "the monoubiquitinated ID complex loses its preference for ICL and related branched DNA structures, and becomes a sliding DNA clamp that can coordinate the subsequent repair reactions"]
  [PMID:32269332 "a closed ring that encircles the DNA"]

- Replication-coupled ICL repair, incision + TLS:
  [PMID:19965384 "FANCI-FANCD2 is required for replication-coupled ICL repair in S phase. Removal of FANCD2 from extracts inhibits both nucleolytic incisions near the ICL and translesion DNA synthesis past the lesion. Reversal of these defects requires ubiquitylated FANCI-FANCD2"]

- ssDNA binding / ring-like particle:
  [PMID:19609304 "Purified FANCD2, a ring-like particle by electron microscopy, preferentially bound ssDNA over various DNA substrates"]
  [PMID:19609304 "We propose that FANCD2 binds to ssDNA arising from MRE11-processed DNA double-strand breaks"]

- FANCI as monoubiquitinated paralog / partner:
  [PMID:17460694 "A FANCD2 protein sequence-based homology search facilitated the discovery of FANCI, a second monoubiquitinated component of the FA pathway"]

- BRCA2 direct interaction (HR):
  [PMID:15115758 "it bound to a highly conserved C-terminal site in BRCA2 that also binds FANCG/XRCC9. FANCD2 and BRCA2 can be coimmunoprecipitated from cell extracts"]
  [PMID:18212739 "phosphorylation of FANCG serine 7 is required for its co-precipitation with BRCA2, XRCC3 and FANCD2, as well as the direct interaction of BRCA2-FANCD2"]

- FAN1 nuclease recruitment by monoubiquitinated FANCD2:
  [PMID:20603015 "KIAA1018/MTMR15/FAN1, that interacts with, and is recruited to sites of DNA damage by, the monoubiquitinated form of FANCD2"]

- POLN interaction (crosslink repair / HR):
  [PMID:19995904 "we obtained evidence for physical and functional interaction of POLN with factors belonging to the Fanconi anemia pathway, a master regulator of cross-link repair"]

- UHRF1/UHRF2 promote FANCD2 recruitment/monoubiquitination (nucleus/chromatin):
  [PMID:30335751 "UHRF2 cooperates with UHRF1, to ensure recruitment of FANCD2 to ICLs"]
  [PMID:30335751 "the essential monoubiquitination of FANCD2 is stimulated by UHRF1/UHRF2 ... by a retention of FANCD2 on chromatin"]

- MEN1/menin interaction; enhanced by gamma-irradiation:
  [PMID:12874027 "menin specifically interacts with FANCD2 ... The interaction between menin and FANCD2 is enhanced by gamma-irradiation"]

- CEBPD/IPO4 nuclear import:
  [PMID:20805509 "C/EBPδ interacts with FANCD2 and importin 4 (IPO4 ...) via separate domains, mediating FANCD2-IPO4 association and augmenting nuclear import of FANCD2, a prerequisite for its monoubiquitination"]

- Monoubiquitination at Lys561 by FANCL/UBE2T; DUB USP1; chromatin binding requirement
  (UniProt Q9BXW9 PTM/SUBUNIT sections).

## Curation decisions (high level)
- Core: interstrand cross-link repair (GO:0036297); ssDNA/damaged DNA binding (clamp);
  DNA-repair (ID2) complex; nuclear/chromatin localization; HR-mediated DSB repair.
- protein binding (GO:0005515, 11 IPI rows): REMOVE — uninformative MF; the underlying
  interactions (FANCI, BRCA2, MEN1, MRE11/NBS1, FAN1, CEBPD, EGFR) are recorded here/in
  more specific terms.
- DNA polymerase binding (GO:0070182, IBA + POLN IPI): KEEP_AS_NON_CORE — real but peripheral.
- Meiotic terms (GO:0007129, GO:1990918): KEEP_AS_NON_CORE (germline-restricted, IBA).
- nucleolus (GO:0005730), response to gamma radiation (GO:0010332): KEEP_AS_NON_CORE.
- Added NEW GO:0003697 single-stranded DNA binding (IDA, PMID:19609304).
</content>
