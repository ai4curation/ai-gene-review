# PDSS1 (Q5T2R2) review notes

Human PDSS1 = decaprenyl-diphosphate synthase subunit 1 (UniProt entry name DPS1_HUMAN;
"All trans-polyprenyl-diphosphate synthase PDSS1"). HGNC:17759, gene id 23590, chromosome 10.

## Core biology (from UniProt Q5T2R2 = file:human/PDSS1/PDSS1-uniprot.txt)

- FUNCTION: "Heterotetrameric enzyme that catalyzes the condensation of farnesyl diphosphate
  (FPP), which acts as a primer, and isopentenyl diphosphate (IPP) to produce prenyl diphosphates
  of varying chain lengths and participates in the determination of the side chain of ubiquinone."
  "Supplies nona and decaprenyl diphosphate, the precursors for the side chain of the isoprenoid
  quinones ubiquinone-9 (Q9) and ubiquinone-10 (Q10) respectively." "The enzyme adds isopentenyl
  diphosphate molecules sequentially to farnesyl diphosphate with trans stereochemistry."
  [ECO:0000269|PubMed:16262699]
- CATALYTIC ACTIVITY (EC 2.5.1.91): "7 isopentenyl diphosphate + (2E,6E)-farnesyl diphosphate =
  all-trans-decaprenyl diphosphate + 7 diphosphate" (RHEA:27802). A second reaction produces
  all-trans-nonaprenyl diphosphate (6 IPP; RHEA:55364, by similarity to Q33DR2).
- COFACTOR: Mg(2+); "Binds 2 Mg(2+) ions per subunit." (by similarity to P14324). Explains the
  IEA metal-ion-binding keyword annotation (GO:0046872, not in GOA TSV but in UniProt DR).
- PATHWAY: "Cofactor biosynthesis; ubiquinone biosynthesis." [ECO:0000269|PubMed:16262699];
  UniPathway UPA00232.
- SUBUNIT: "Heterotetramer composed of 2 PDSS1/DPS1 and 2 PDSS2/DLP1 subunits."
  [ECO:0000269|PubMed:16262699]. PDSS2 = UniProtKB Q86YH6 (the with/from id on the IPI in GOA).
- SUBCELLULAR LOCATION: "Mitochondrion" [ECO:0000269|PubMed:34800366].
- SIMILARITY: "Belongs to the FPP/GGPP synthase family." Trans-IPPS head-to-tail
  (CDD cd00685 Trans_IPPS_HT); Pfam PF00348 polyprenyl_synt.
- DISEASE: "Coenzyme Q10 deficiency, primary, 2 (COQ10D2) [MIM:614651]" — autosomal recessive;
  variant D308E (VAR_034879, rs119463988) [ECO:0000269|PubMed:17332895]. Orphanet 254898
  (deafness-encephaloneuropathy-obesity-valvulopathy syndrome).

## Key primary reference: PMID:16262699 (Saiki et al. 2005, FEBS J) — ABSTRACT ONLY

`full_text_available: false` in publications/PMID_16262699.md, so only the abstract can be quoted.
Establishes the human enzyme experimentally:
- "murine and human solanesyl and decaprenyl diphosphate synthases are heterotetramers composed
  of newly characterized hDPS1 (mSPS1) and hDLP1 (mDLP1)" — hDPS1 = PDSS1, hDLP1 = PDSS2.
- E. coli reconstitution: "double transformants expressing mSPS1 and mDLP1 or hDPS1 and hDLP1
  produced Q9 or Q10, respectively, and an in vitro activity of solanesyl or decaprenyl
  diphosphate synthase was verified." — direct assay of the decaprenyl-diphosphate synthase
  (GO:0097269) activity of the human hDPS1/hDLP1 pair.
- "The complex size ... indicates that they consist of heterotetramers." — supports the
  heterotetrameric complex CC (GO:0032478).
- "both components are involved in determining the ubiquinone side chain." — supports ubiquinone
  biosynthetic process (GO:0006744).
This paper is the source of the experimental GOA annotations 14-16, 18-19 (IDA/IPI). The IPI
(GO:0005515, with UniProtKB:Q86YH6 = PDSS2) records the PDSS1-PDSS2 interaction; bare "protein
binding" is uninformative and the biology is better captured by the heterotetramer CC + subunit
role, so it is marked over-annotated rather than removed.

## Localization: PMID:34800366 (Morgenstern et al. 2021, Cell Metab) — full text cached

High-confidence quantitative human mitochondrial proteome; source of the UniProt SUBCELLULAR
LOCATION "Mitochondrion" and the HTP GO:0005739 annotation. PDSS1 is not named in the abstract
prose (it appears in the proteome dataset), consistent with an HTP localization annotation.

## Term-by-term reasoning

- Core MF = GO:0097269 all-trans-decaprenyl-diphosphate synthase activity (EC 2.5.1.91). Verified
  current & non-obsolete via OLS. This is the specific trans-prenyltransferase activity; the
  IBA/IEA generic GO:0004659 "prenyltransferase activity" is a true parent → MODIFY to GO:0097269.
- Core CC = GO:0032478 heterotetrameric polyprenyl diphosphate synthase complex (verified current).
  IBA GO:0032476 (parent "polyprenyl diphosphate synthase complex") → MODIFY to the specific
  heterotetrameric term, which is directly supported experimentally (IDA, PMID:16262699).
- Core BP = GO:0006744 ubiquinone biosynthetic process (verified current). GO:0008299 isoprenoid
  biosynthetic process is a broad parent BP — kept as non-core.
- Location: mitochondrion (GO:0005739) experimentally supported; matrix (GO:0005759) from ARBA/
  Reactome is a plausible more-specific location (matrix/inner-membrane face) but not directly
  demonstrated in the cached sources → kept as non-core.
- Metal ion binding (GO:0046872) is in the UniProt DR block (IEA KW) but absent from the GOA TSV,
  so it is not among the 19 seeded annotations; the Mg2+ cofactor is noted here for completeness.
</content>
