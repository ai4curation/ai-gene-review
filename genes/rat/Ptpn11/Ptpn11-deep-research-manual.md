# Ptpn11 (rat, P41499) - manual literature synthesis

No deep-research API was available; this synthesis was compiled by hand from the cached
publications in `publications/` and the UniProt record `Ptpn11-uniprot.txt`. Most cached
papers are abstract-only; PMID:17662049 was read in full.

## Identity and structure
- SHP2 / PTP1D / SH-PTP2 / Syp; 593 aa; two SH2 domains (6-102, 112-216), PTP domain (247-517),
  catalytic Cys459 (UniProt FT ACT_SITE, PROSITE-ProRule).
- UniProt: "Belongs to the protein-tyrosine phosphatase family." Non-receptor class 2 subfamily.
- UniProt DOMAIN: "The SH2 domains repress phosphatase activity. Binding of these domains to
  phosphotyrosine-containing proteins relieves this auto-inhibition" (By similarity to human Q06124).

## Catalytic activity (rat-specific)
- [PMID:7512964 "Whereas both PTP1D and PTP1Di had catalytic activity"] - rat brain cDNA; the PTP1Di
  splice isoform (Ala-Leu-Leu-Gln insert in the catalytic domain) has 8-20-fold lower Vmax but lower Km.
- [PMID:7711057 "Immunodepletion studies demonstrated that LAR, SH-PTP2 and PTPase1B were quantitatively
  major PTPase activities in the initial muscle homogenate"]; SH-PTP2 present in cytosol and particulate fractions.
- [PMID:15378208 "Using a combination of approaches, we identified the tyrosine phosphatase Shp-2 in mitochondria."]
  (rat brain; activity mainly in intermembrane space and outer membrane).

## Substrates and dephosphorylation
- [PMID:15272025 "The activated SHP-2 then dephosphorylated IRS-1 Tyr(P)-895, resulting in blockade of the
  pathways from IRS-1/Grb2/Sos to the ERK and p38 MAPK."] (differentiated rat VSMCs; negative role).
- [PMID:7545675 "the most efficiently dephosphorylated sites were phosphotyrosines (Tyr(P)-771 and -751, followed by Tyr(P)740"] (PDGFRB).
- [PMID:18757826 "Recombinant Shp2 C-terminal protein tyrosine phosphatase domain (Shp2-PTP) interacted with
  nonphosphorylated recombinant FAK and dephosphorylated FAK immunoprecipitated from NRVMs."]
- [PMID:16690621 "Cat.G induces SHP2 activation that leads to FAK tyrosine dephosphorylation and promotes cardiomyocyte anoikis"]
- [PMID:19348936] H2O2 drives SHP-2 phosphorylation and raft translocation in astrocytes; complex with STAT-3.

## Phosphotyrosine recruitment / partners
- BIT/SIRPA TAMs: [PMID:8810330 "Bisphosphotyrosyl peptides corresponding to BIT-TAMs stimulated SH-PTP2 activity 33-35-fold in vitro"]
- PECAM-1: [PMID:9388260 "A fusion protein containing the two SH2 domains of SHP-2 precipitated PECAM-1 from
  cell lysates and also directly bound to phosphorylated PECAM-1."]
- TLT1 ITIM Y281 [PMID:15128762]; Gab2 in EGF-treated hepatocytes [PMID:10973965]; JAK2 [PMID:8912646
  "Thus, SHPTP2 might serve as an adapter protein linking between JAK2 and IRS."]; D1 dopamine receptor
  [PMID:23328768]; PLCgamma1 [PMID:16814162]; Ret-containing complexes, not direct [PMID:15115663].

## Signalling roles
- Positive: ERK1/2 activation downstream of D1R in striatum [PMID:23328768]; Ang II/IGF-I activation in
  VSMCs [PMID:9139682 "In addition, IGF I stimulated PTP-1D phosphatase activity."]; SMC proliferation
  [PMID:12117720]; ICAM-1-Src-cortactin signalling in brain endothelium [PMID:17662049 "SHP-2 is positively
  involved in ICAM-1 signaling, upstream of the tyrosine phosphorylation of cortactin by Src and of
  RhoA-mediated actin cytoskeleton rearrangements."].
- Negative / restraining: IRS-1 Tyr895 in differentiated VSMCs [PMID:15272025]; FAK/Src-mTOR control of
  cardiomyocyte size [PMID:18757826].
- Focal adhesion/ER coupling in IL-1 Ca2+ signalling [PMID:16905534].
