# Datp (CG31713, formerly Apf; Q4V6M1) review notes

## Identity / accession choice (2026-10-08)

- Current FlyBase symbol is **Datp** (Diadenosine tetraphosphatase), FBgn0287788, CG31713.
  The older symbol **Apf** (FBgn0051713, the name used in PMID:17344088) is no longer a live
  FlyBase gene ID (Alliance API: "No gene found with ID: FB:FBgn0051713"); Apf, Ap4A and
  CG31713 are synonyms. The folder therefore uses the current symbol `Datp`.
- UniProt has two unreviewed entries with the identical 142 aa sequence (CRC64 26C2AD6374C12308):
  - **Q4V6M1** - carries the `FlyBase; FBgn0287788; Datp` cross-reference, the
    PMID:17344088 citation (EMBL AAX68972) and the IBA rows in GOA. Used as `id`.
  - A0ACM8PZ70 - new TrEMBL entry (integrated 10-JUN-2026) from the genome record
    (AAN10714.2), no FlyBase DR line. In QuickGO (2026-10-08) it holds FlyBase's
    `GO:0004081 ISS GO_REF:0000024` row and a `GO:0005575 ND` row, which therefore are not in
    `Datp-goa.tsv`. This looks like a transitional mapping of FlyBase annotations to the new
    accession; the ISS would be accepted (same activity as the accepted IBA) and the ND CC
    row would be superseded by the proposed nucleus IDA.
- **PANTHER uses Q4V6M1.** The PANTHER 19.0 fruit fly classification file lists
  `DROME|FlyBase=FBgn0287788|UniProtKB=Q4V6M1  Q4V6M1  Datp  PTHR21340:SF0`, and the
  PTHR21340 reference tree leaf PTN000482053 is FlyBase:FBgn0287788 (resolved to Q4V6M1).
  A0ACM8PZ70 does not appear in PANTHER. Q4V6M1 is therefore the accession used here, in the
  PTHR21340 family review and in the Ap4A turnover module.
- Fetched with `just fetch-gene DROME Q4V6M1 --alias Datp`.

## Summary of evidence

- Recombinant Apf/Datp is a heat-stable 16.6 kDa Nudix hydrolase specific for diadenosine
  polyphosphates [PMID:17344088 "we have expressed and characterized a heat stable, 16.6kDa Nudix hydrolase (Apf) that specifically metabolizes these nucleotides from a Drosophila melanogaster cDNA"].
- Ap4A -> ATP + AMP; Km 9 uM, kcat 43 s-1 (pH 6.5, Zn2+); Km 12 uM, kcat 13 s-1 (pH 7.5, Mg2+)
  [PMID:17344088 "diadenosine tetraphosphate is hydrolysed to ATP and AMP with K(m), k(cat) and k(cat)/K(m) values 9microM, 43s(-1) and 4.8microM(-1)s(-1)"].
- Always produces an NTP; substrate preference depends on pH and metal
  [PMID:17344088 "Apf always produces an NTP product, with substrate preference depending on pH and divalent ion (Zn(2+) or Mg(2+))"].
- Ap6A -> ATP efficiently only at pH 7.5 with Mg2+ [PMID:17344088 "diadenosine hexaphosphate is efficiently hydrolysed to ATP only at pH 7.5 with 20mMMg(2+)"].
- Fluoride inhibition with Mg2+ only (MgF3- transition-state analogue)
  [PMID:17344088 "supporting the view that inhibition involves a specific, MgF(3)(-)-containing transition state analogue complex"].
- Expression highest in embryos and adult females [PMID:17344088 "Apf mRNA levels to be highest in embryos and adult females"].
- Apf-EGFP predominantly nuclear, apparent euchromatin/facultative heterochromatin association
  [PMID:17344088 "Subcellular localization with Apf-EGFP fusion constructs reveals Apf to be predominantly nuclear, having an apparent preferential association with euchromatin and facultative heterochromatin."].
- An earlier embryonic Ap4A hydrolase activity (26 kDa, Co2+-stimulated, Zn2+-inhibited) peaked
  1.5 h after fertilization and was speculatively linked to nuclear division
  [PMID:2558922 "The profile of activity is compatible with its involvement in the regulation of nuclear division."];
  Winward et al. say Apf is distinguishable from it [PMID:17344088 "with features that distinguish it from a previously reported bis (5'-nucleosyl)-tetraphosphatase hydrolase activity from Drosophila embryos"].
  The FlyBase/Alliance comment "Datp is involved in the activation of nuclear division" probably
  derives from this; it is not used as evidence here.
- Ap4A levels in Drosophila cells: sub-micromolar, rising under heat shock and high cadmium
  [PMID:4066685 "Upon heat-shock from 19 to 37 degrees C, Ap4A, Ap3A, and Ap3G increase up to 2.2, 3, and 3.3 times their initial levels, respectively."].
- FlyBase auto-summary (FB2026_03): 8 alleles; phenotypic classes "fertile; partially lethal;
  viable; abnormal pain response" (the nociception class presumably from a large-scale screen;
  not followed up here).

## Curation decisions (consistent with genes/worm/ndx-4)

- GO:0004081 IBA: ACCEPT (confirmed by recombinant enzyme).
- GO:0006167 AMP / GO:0006754 ATP biosynthetic process IBA: MARK_AS_OVER_ANNOTATED -
  product-based inference propagated from PTN000482012 whose only seed is ndx-4's own IDA.
- GO:0008796 IEA: ACCEPT (broader parent).
- GO:0016787 hydrolase activity IEA: MODIFY -> GO:0004081.
- GO:0046872 metal ion binding IEA: KEEP_AS_NON_CORE (Mg2+/Zn2+ dependence; cofactor feature).
  This row has no counterpart in the ndx-4 review.
- NEW GO:0015967 diadenosine tetraphosphate catabolic process (IDA, PMID:17344088): Datp
  catalyses the step; comparator ndx-4 has it by IDA.
- NEW GO:0005634 nucleus (IDA, PMID:17344088): tagged-protein localization; euchromatin not
  proposed (the abstract calls the association "apparent").
- No PRPP pyrophosphatase or apoptosis rows exist for the fly gene; the PMID:12370170 PRPP
  screen abstract names no Drosophila enzyme, so no PRPP activity is proposed.

## Caveats

All cached publications are abstract-only (`full_text_available: false`).

## Deep research status

OpenScientist run started 2026-10-08 (`just deep-research-openscientist DROME Datp`).
Completed 2026-10-08 (~26 min): `Datp-deep-research-openscientist.md`. It confirmed the
gene identity (Datp = Apf = CG31713 = Q4V6M1) and found no fly literature beyond
PMID:17344088. Additions, none of which change a curation decision:

- 48.6% full-length identity to human NUDT2 (P50583) with a conserved Nudix box
  [file:DROME/Datp/Datp-deep-research-openscientist.md "gives **68 of 140 aligned positions identical = 48.6% identity**"];
  Nudix box R50-E51-T52-K53-E54-E55-A56-G57 (consistent with the UniProt sequence; MOTIF 36..57).
- AlphaFold AF-Q4V6M1-F1 high-confidence single Nudix domain (pLDDT 94.9), predicted
  three-glutamate metal site (model-based, not experimental).
- States no loss-of-function phenotypes are published
  [file:DROME/Datp/Datp-deep-research-openscientist.md "There are no published loss-of-function (mutant/RNAi/CRISPR) phenotypes establishing what Datp does for the organism"];
  note FlyBase nonetheless lists 8 alleles with "viable/fertile/partially lethal/abnormal
  pain response" classes (likely large-scale screens), so this should be checked.
- Ap4A signaling context (LysRS synthesis, Hint1-MITF, STING) is mammalian; not used as
  evidence for fly process annotations.
