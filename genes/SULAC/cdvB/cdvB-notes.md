# cdvB (Saci_1373, Q4J924, CDVB_SULAC) notes

## Provenance note

Automated deep research providers (falcon, openai) were unavailable for this review
(API authentication failures). No `-deep-research-*.md` file was generated. The
literature below was gathered manually via NCBI E-utilities (PubMed esearch/esummary)
and read from the cached `publications/PMID_*.md` files. QuickGO API queries were used
for the comparator and archaeal-annotation checks (2026-10-15).

## Identity and paralog caution

- S. acidocaldarius DSM 639 encodes four ESCRT-III homologs: CdvB (Saci_1373, this
  entry, in the cdvA-cdvB-cdvC operon), CdvB1 (Saci_0451), CdvB2 (Saci_1416) and CdvB3
  (Saci_1601). Only CdvB carries the MIT-binding motif and the C-terminal winged-helix
  (wH/"broken winged helix") that binds CdvA.
  [PMID:19008417 "Among the four Saci ESCRT-III-like subunits, only Saci1373 has this MIT-binding motif"]
- Papers on *Saccharolobus islandicus* (PMID:39699168, "ESCRT-III", "-III-1", "-III-2")
  and *S. solfataricus* overexpression assays (PMID:19008417, PMID:21255729) are related
  organisms; claims below are tagged by organism where it matters.

## Discovery and localization

- The cdv operon (cdvA-cdvB-cdvC) is induced at genome segregation/division and the Cdv
  proteins form a mid-cell structure between segregating nucleoids that shrinks during
  constriction.
  [PMID:18987308 "the Cdv proteins then polymerize between segregating nucleoids and persist throughout cell division, forming a successively smaller structure during constriction"]
  (abstract only in cache)
- Immunostaining of Saci1373: band between the two separated nucleoids at the site of
  membrane ingression; protein levels peak in dividing populations.
  [PMID:19008417 "a band or belt of Saci1373 (ESCRT-III) was detected between the two nucleoids, correlating with the site of membrane ingression"]
  [PMID:19008417 "levels of Saci1373 (ESCRT-III) protein were highest in dividing cell populations"]
- Super-resolution: CdvB forms a single narrow ring at the cell centre, flanked by
  CdvB2 (proximal) and CdvB1 (distal) rings.
  [PMID:36921039 "CdvB was found to localize into a single narrow ring positioned at the center of control cells"]

**Implication for GOA:** the UniProt SubCell line "Cytoplasm, nucleoid" (mapped to
GO:0009295 nucleoid by GO_REF:0000044) is a mis-encoding of "between segregating
nucleoids". The protein is at the mid-cell division plane, not in the nucleoid.

## Interactions

- C-terminal MIT-interacting motif (183-193) binds the MIT domain of Vps4/CdvC
  (crystal structure 2W2U). [PMID:19008417 "The minimal interaction sites comprised residues 183 to 193 of Saci1373 (ESCRT-III)"]
- C-terminal wH domain binds CdvA; CdvA recruits CdvB to archaeal-lipid liposomes;
  CdvA + CdvB together tubulate liposomes in vitro (CdvB alone does not deform them).
  [PMID:21255729 "although the archaeal ESCRT-III does not bind to liposomes on its own, in the presence of CdvA, it is recruited to liposomes"]
  [PMID:21255729 "the combination of CdvA and ESCRT-III had the dramatic effect of inducing the formation of an extensive network of inter-connected tubular structures"]
- Conflicting in vitro data on intrinsic membrane binding: the 2026 structural study
  finds CdvB pellets with archaeal liposomes via a short N-terminal amphipathic helix.
  [PMID:41543908 "CdvB and CdvB2 efficiently pelleted with archaeal liposomes, while CdvB1 remained mainly in the soluble fraction"]
  [PMID:41543908 "Short N-terminal amphipathic helices in all CdvB paralogues, B, B1, and B2, mediate membrane binding and are required for liposome recruitment in vitro"]
- Structure: bona fide ESCRT-III fold, closed and "semiopen" conformations.
  [PMID:41543908 "Monomeric CdvB adopts the canonical ESCRT-III fold in both a closed and a distinct"]

## Role in division: template ring, removed to trigger constriction

- CdvB is essential in S. acidocaldarius and is a key proteasome target at division.
  [PMID:32764038 "Previous studies have suggested that CdvB, an essential gene in S. acidocaldarius, is actively required for division"]
  [PMID:32764038 "Proteomics analyses identified a single archaeal ESCRT-III homolog, CdvB (Saci_1373), as a key target for proteasome-mediated degradation during the final stages of the cell division cycle."]
- CdvB ring forms first (CdvA-dependent), templates the CdvB1:CdvB2 contractile ring,
  and holds it unconstricted; its removal (Vps4-dependent disassembly, then proteasomal
  degradation) triggers constriction.
  [PMID:32764038 "CdvB both templates the assembly of a contractile ESCRT-III copolymer, composed of the paralogs CdvB1 (Saci_0451) and CdvB2 (Saci_1416), and prevents their constriction"]
  [PMID:32764038 "The absence of large polymeric CdvB1:CdvB2 structures in these early G1 cells implies that CdvB1 and CdvB2 do not form de novo ESCRT-III filaments without a CdvB template."]
  [PMID:36921039 "beginning with the removal of CdvB, followed by the disassembly of CdvB1, and then CdvB2"]
  [PMID:36921039 "This is consistent with the notion that MIM2-dependent removal of CdvB from the ESCRT-III copolymer ring by Vps4 is a prerequisite for its subsequent proteasomal degradation"]
- Degradation mechanism: the C-terminal broken-winged helix is a cell-cycle-regulated
  instability determinant; PAN levels (repressed by CCTF1) rise in division.
  [PMID:41514146 "the C-terminal broken-winged helix of CdvB, previously shown to bind CdvA, is sufficient to render a fusion protein unstable as cells progress through division"]
  [PMID:41514146 "The loss of CdvB from the division ring frees CdvB1/B2 polymers to constrict and drive cytokinesis"]
- Paralog roles for comparison: CdvB1 and CdvB2 are the constricting polymers
  (PMID:32502411); CdvB3 has an accessory role (PMID:24399085, abstract only).

## GO term choices

- **GO:0061639 Cdv-dependent cytokinesis** — exists precisely for this machinery
  (definition names the Cdv proteins). Parent GO:0000910 cytokinesis carries the note
  that it should not be used for direct annotation and that prokaryotes should use
  FtsZ-dependent (GO:0043093) or Cdv-dependent (GO:0061639) cytokinesis. QuickGO
  (2026-10-15): **zero** annotations to GO:0061639 for any organism. That is a curation
  gap (no archaeal Cdv protein has experimental GO curation), not a convention: the
  term was coined for exactly these proteins. Participation test: CdvB does work in the
  process as the structural template/scaffold of the division ring (scaffold case), not
  merely as a substrate of the proteasome.
- **GO:0032153 cell division site** — replaces nucleoid.
- **GO:0000815 ESCRT III complex** — definition is not endosome-specific (it explicitly
  includes cytokinetic abscission); CdvB co-assembles with CdvB1/CdvB2 into a composite
  ESCRT-III polymer. Added as NEW.
- MF: no specific GO MF captures "template for a contractile polymer". Used
  GO:0005198 structural molecule activity in core_functions. Not proposing
  GO:0180020 membrane bending activity because CdvB alone did not deform liposomes
  (PMID:21255729) and constriction in vivo is performed by CdvB1/CdvB2.

## Archaea error-pattern check (ESCRT/endosome leakage)

- Q4J924 itself has no endosome/MVB/vacuole rows. Its InterPro family is IPR053654
  (CdvB), not IPR005024 (Snf7 family), so it escapes the Snf7 InterPro2GO mapping.
- QuickGO (taxon Archaea, 2026-10-15): **GO:0007034 vacuolar transport** is applied by
  InterPro2GO (GO_REF:0000002, via IPR005024 Snf7) to ~41 archaeal ESCRT-III/CdvB
  homologs, including Sulfolobales proteins (e.g. Q972B4 ST1214 *Sulfurisphaera
  tokodaii*, A4YHE8 Msed_1695 *Metallosphaera sedula*, A0A557ST16 cdvB2,
  A0AAT9GTS0 cdvB). Archaea have no vacuole. TreeGrafter (GO_REF:0000118) also places
  GO:0032511 late endosome to vacuole transport via multivesicular body sorting pathway
  and GO:0043328 protein transport to vacuole involved in ubiquitin-dependent protein
  catabolic process via the multivesicular body sorting pathway on Asgard archaeal
  ESCRT proteins (DSAG12_*, NEF87_*). No archaeal rows were found for GO:0000815,
  GO:0005768 endosome, GO:0036258 MVB assembly or GO:0031902.
- Pattern: eukaryotic-compartment process terms transferred to archaeal ESCRT-III
  homologs by InterPro2GO (Snf7 family) and PANTHER/TreeGrafter; correct archaeal
  process is cell division (GO:0061639).
