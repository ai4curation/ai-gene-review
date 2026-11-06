# LIG4 (human, P49917) review notes

## Literature search (manual; no deep-research provider available)

Sources checked:
- All 38 GOA-cited PMIDs, cached with `just fetch-gene-pmids human LIG4`.
- PubMed E-utilities searches (2026-11-04): "Frank KM[au] late embryonic lethality DNA ligase
  IV 1998" -> PMID:9823897; "Barnes DE[au] targeted disruption ligase IV 1998" ->
  PMID:9889105; "Lieber MR[au] mechanism double-strand break repair nonhomologous
  end-joining 2010" -> PMID:20192759. Fetched into `publications/`.
- Reactome cached entries for the NHEJ ligation reactions and HIV 2-LTR circle formation.
- UniProt P49917 record.
- Context: telomere end-joining pathway choice (module and GO-CAM review proposed in ai4curation/ai-gene-review#5904; not on this branch and not used as evidence): LIG4 as the ligase of the
  classical-NHEJ route that fuses telomeres lacking TRF2 [PMID:28216226 "Classical-NHEJ-mediated repair of
  telomeres lacking TRF2 requires phosphorylated NBS1S432 to activate ATM"].

## Key findings

- ATP-dependent nick sealing; purified from HeLa nuclei [PMID:8798671 "The purified protein
  effectively joins single-strand breaks in a double-stranded polydeoxynucleotide in an
  ATP-dependent reaction."]. Crystal structures of catalytic core on nicked DNA
  [PMID:29980672 "a dynamic LigIV DNA encirclement mechanism"]. Mg2+ cofactor (PMID:29980672
  metal screen).
- Obligate partner XRCC4 (BRCT-linker interface, PMID:19332554), stimulates ligation
  [PMID:9242410 "Ligation of DNA double-strand breaks in a cell-free system by DNA ligase IV
  is increased fivefold by purified XRCC4"]. XRCC4 imports and stabilizes LIG4
  (PMID:21982441) and LIG4 reciprocally controls XRCC4 nuclear localization (PMID:24984242).
- Ligase of classical NHEJ and V(D)J recombination [PMID:9809069 "DNA ligase IV is the
  activity responsible for the ligation step in NHEJ and in V(D)J recombination."]. Flexible
  ligase that ligates incompatible ends and across gaps (PMID:17290226). Component of NHEJ
  supercomplexes with Ku, DNA-PKcs, XRCC4, XLF (PMID:34352203, PMID:25941166).
- LIG4 is dispensable for viability in human HCT116 cells; needed for TRF2-dominant-negative
  telomere fusions [PMID:23275564]; most end joining in human cells is LIG4-dependent, LIG3
  only for Ku-suppressed A-NHEJ [PMID:24837021].
- Mouse: Lig4 knockout is late-embryonic lethal with neuronal apoptosis and blocked
  lymphopoiesis [PMID:9823897; PMID:9889105]. These underlie the many ISS rows (development,
  proliferation, neuron apoptosis), which are downstream consequences of unrepaired DSBs.

## Curation decisions of note
- GO:0003909 and GO:0016874 rows MODIFY -> GO:0003910.
- GO:0006297 "nucleotide-excision repair, DNA gap filling" rows: the cited papers
  (PMID:12517771, PMID:17290226) describe gap filling/ligation during NHEJ of DSBs, not NER.
  The IDA rows are repointed to GO:0006303; the IBA (seeded only by these LIG4 rows) is
  removed. Recorded as source defects.
- GO:0071479 IGI PMID:29463814: the paper is entirely on C. elegans (LEM-3 with lig-4
  alleles); the annotation belongs to worm lig-4, not human LIG4. REMOVE + source defect.
- Base-excision repair IDA (PMID:19589734) and single strand break repair IDA (PMID:8798671)
  are in vitro nick-ligation results; LIG4 has no in vivo role in BER/SSBR -> over-annotated.
- Mouse phenotype ISS rows: developmental ones kept as non-core; proliferation/apoptosis/
  neurogenesis/stem-cell/chromosome-organization rows marked over-annotated.
- 25 bare protein-binding rows REMOVE; partner relationships are captured by the DNA ligase
  IV complex, DNA-PK-LIG4 complex and NHEJ complex CC terms.

## PR #5944 review follow-up

- Rule applied across the NBN and LIG4 reviews: a developmental or tissue-level process term whose only basis is the knockout phenotype of a housekeeping DNA repair factor (lethality, apoptosis, progenitor loss) records necessity, not participation, and is MARK_AS_OVER_ANNOTATED; it is kept as non-core only where the gene performs a step inside the process itself (as LIG4 does in V(D)J joining during lymphocyte differentiation). Applied to GO:0001701 and GO:0007417 (changed from KEEP_AS_NON_CORE); GO:0002328 pro-B cell differentiation, GO:0033077 T cell differentiation in thymus and GO:0045190 isotype switching stay non-core because LIG4 performs the joining step inside them.
