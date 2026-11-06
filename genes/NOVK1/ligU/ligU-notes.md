# ligU (Q0KJL4, Novosphingobium sp. KA1) - curator notes

Deep research could not be run for this session; these notes were written by hand from the
cached publications and the UniProt record. No `-deep-research-*.md` file exists.

## Identity
- LigU, 357 aa, PrpF family (Pfam PF04303; NCBIfam NF033377 OMA_tautomer; PANTHER
  PTHR43709:SF3). Encoded on the carbazole-degradation plasmid pCAR3 of strain KA1 (ORF100).
- Gene context: ORF100 lies within the pCAR3 protocatechuate (lig) cluster, between ligI (ORF99)
  and ligK (ORF102) [PMID:17172338 "These genes were designated ligI (ORF99), ligK (ORF102), ligR (ORF103), ligBII (ORF103a), ligAII (ORF103b), ligJ (ORF105), ligAI (ORF106), ligBI (ORF107), and ligC (ORF109)"];
  [PMID:17172338 "Nine ORFs around ORF106 whose products were predicted to catalyze protocatechuate degradation were identified."]
- In Sphingobium sp. SYK-6 the equivalent position (ligK-orf1-ligI) holds orf1, a YbhH-like gene
  originally guessed to be a transporter and essential for growth on vanillate/syringate
  [PMID:12486039 is the SYK-6 paper; not cited in the review]. PrpF-family LigU homologues are annotated
  "ISOMERASE YBHH-RELATED" in PANTHER, so SYK-6 orf1 is probably the SYK-6 ligU (inference, not verified).

## Function (PMID:29658701; abstract-only in cache)
- [PMID:29658701 "LigU catalyzes the isomerization of the double bond between C4 and C5 in (4 E)-OMA to (3 Z)-2-keto-4-carboxy-3-hexenedioate (KCH), where the double bond has migrated to be between C3 and C4 via a 1,3-allylic isomerization."]
- Kinetics: kcat 1300 s-1, kcat/Km 7.7 x 10^6 M-1 s-1 at pH 8.
- Homology: [PMID:29658701 "LigU is most closely related in amino acid sequence to methylaconitate isomerase (PrpF) from Shewanella oneidensis and methylitaconate-Δ-isomerase (Mii) from Eubacterium barkeri."]
- Downstream coupling: [PMID:29658701 "We have also shown that the product of the LigU-catalyzed reaction is the preferred substrate for the LigJ hydratase."]
- UniProt places this experimental characterization (ECO:0000269) on the KA1 entry; the paper title names
  Sphingobium sp. SYK-6 as the pathway organism. UniProt reaction RHEA:58504, EC 5.3.3.-.
- Structures PDB 6P3H/6P3J/6P3K on this entry (secondary-structure features only in the cached record).

## GO term availability
- No GO term for OMA delta-isomerase / RHEA:58504 (OLS/QuickGO searches "oxalomesaconate",
  "hexenedioate", "allylic isomerase" returned nothing relevant). Closest existing parent:
  GO:0016863 intramolecular oxidoreductase activity, transposing C=C bonds (EC 5.3.3 class), which the
  P. putida GalD tautomerase review also uses. Proposed: "(4E)-oxalomesaconate delta-isomerase activity".
- Functional analogy: in Pseudomonas gallate catabolism, OMA -> CHA is GalD (tautomerase) + GalB
  (OMA hydratase); in sphingomonads it is LigU (1,3-allylic isomerase) + LigJ (KCH hydratase).

## Curation decisions
- lignin catabolic process (UniPathway IEA): KEEP_AS_NON_CORE (lignin-derived monoaromatic context).
- NEW GO:0016863 (MF, existing parent term) and NEW GO:0019617 protocatechuate catabolic process, meta-cleavage
  (BP; LigU catalyses a step of the PCA 4,5-cleavage pathway per PMID:29658701).
- Gallate catabolic process not asserted for KA1: no gallate data for this strain.


## 2026-11-06 comparative source and annotation audit

PMID:31339729 explicitly identifies KA1 LigU and supplies independent target-grounded structural/mechanistic evidence; normal fetch initially returned429, then succeeded with abstract-only cache. PDB6P3J entity1 maps Q0KJL4 and contains the complete unchanged 357-aa target within its 365-aa expression construct. This supports the curated KA1 attribution of PMID:29658701 despite its SYK-6 title; that older protected cache remains abstract-only and no purported full-methods reading is claimed. Both historical IDA NEW rows are retained. The core now uses the existing substrate-specific NTR. Polymer-defined lignin BP is laterally replaced with the demonstrated lower PCA pathway. A complete native KA1 gallate route is not established by this single enzyme.

Research: the normal default Falcon attempt failed with HTTP403 authentication; manual evidence assessment is recorded here, without a fabricated provider report. All original non-review annotation payloads, order and inherited NEW actions are retained; no new annotation row was added. Sources were not refreshed. Current ontology responses and pre-edit proofs are in the ignored gallate-20261106/gene-review audit cache.
