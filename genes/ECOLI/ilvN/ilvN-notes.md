# ilvN (P0ADF8) — Escherichia coli K-12 — curation notes

Provider deep research was not run for this gene. These notes are drawn from
the cached publications in `publications/` (all relevant ones are
abstract-only) and the UniProt record (`ilvN-uniprot.txt`).

## Three AHAS isozymes in E. coli K-12

- UniProt (P0ADF8, MISCELLANEOUS): "E.coli contains genes for 3 AHAS isozymes:
  ilvBN, ilvGM and ilvIH." IlvBN is AHAS I, IlvGM is AHAS II and IlvIH is
  AHAS III.
- In K-12 only AHAS I and AHAS III are expressed: the curated UniProt entry
  for IlvG (P0DP90, MISCELLANEOUS, ECO:0000269 PubMed:7015336) states "In
  strain K12 only the Val-inhibitable ilvBN and ilvIH are expressed; ilvGM has
  a frameshift that disturbs the ilvG reading frame." (retrieved from the
  UniProt REST API during this review; P0DP89 is the K-12 pseudogene
  fragment). This is why valine inhibits growth of wild-type K-12.
- AHAS I is apparently restricted to enterobacteria and differs from the other
  isozymes [PMID:16326011 "AHAS I is an isozyme of acetohydroxyacid synthase
  which is apparently unique to enterobacteria."]; it lacks the preference for
  forming acetohydroxybutyrate [PMID:16326011 "the absence of a preference for
  forming acetohydroxybutyrate"].

## IlvN is the small, regulatory subunit

- Purified AHAS I contains a 60 kDa and a 9.5 kDa polypeptide in constant 1:1
  proportion with activity, co-immunoprecipitated by anti-large-subunit serum
  [PMID:6360995 "These two polypeptides were present in constant proportion to
  each other and to enzyme activity."].
- IlvN binds the catalytic subunit IlvB near the FAD site and activates the
  enzyme [PMID:18193896 title "Escherichia coli ilvN interacts with the FAD
  binding domain of ilvB and activates the AHAS I enzyme."; "NMR chemical
  shift mapping methods show that ilvN binds close to the FAD binding site in
  ilvBbeta"].
- Holoenzyme reconstituted from purified IlvB and IlvN shows cooperative
  valine feedback inhibition [PMID:16326011 "Unlike other AHASs, AHAS I
  demonstrates cooperative feedback inhibition by valine"].
- IlvN is 96 aa, a single ACT domain (PROSITE PS51671, Pfam PF22629,
  NCBIfam NF006036 ilvN); crystal structures 5YPP etc.

## Decision on catalytic GO:0003984 rows

The catalytic machinery (ThDP, FAD) is in the large subunit IlvB; IlvN has no
active site. Existing comparator reviews differ: P. putida IlvH removes the IEA
GO:0003984 row ("Catalysis resides in IlvI"), whereas yeast ILV6 accepts its
experimental GO:0003984 rows but records the core function as MF
GO:1990610 with contributes_to GO:0003984. The PTHR30239 family review rates
the PAINT node assertion of "enables" GO:0003984 (PTN000767018, seeded by
E. coli IlvH and IlvN) as UNRESOLVED and says a contributes_to qualifier or
GO:1990610 describes the subunit correctly.

Here all three GO:0003984 rows (IBA, IDA, IEA) are MODIFY to GO:1990610: the
essence of each row (IlvN is required for and shapes holoenzyme activity) is
sound, but "enables acetolactate synthase activity" transfers the complex's
catalysis to a non-catalytic subunit. This matches the substance of both the
yeast core function and the PSEPK reasoning, keeps the claim-level actions on
one term consistent, and is applied identically to E. coli ilvH.

## Other decisions

- GO:0005515 with IlvB: the PMID:18193896 row is MODIFY to GO:1990610 (the
  paper shows IlvN binding activates IlvB); the two high-throughput rows and
  the subunit-composition row (PMID:6360995) are REMOVE per the
  protein-binding policy (complex membership is captured by GO:0005948).
- GO:0009082: correct but general; MODIFY to L-valine and L-isoleucine
  biosynthetic process. GO:1901705 added as NEW (UniProt pathway step 1/4).
- GO:0005737 (ARBA): MODIFY to cytosol.
