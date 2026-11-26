# CFAP65 (Q6ZU64) curation notes

## Deep research status

- `just deep-research human CFAP65 --provider falcon` failed with an Edison client
  `Exception: Failed to authenticate`.
- `just deep-research human CFAP65 --provider perplexity` failed: `Provider 'perplexity'
  not available. Available: falcon, asta, openscientist`.
- No `*-deep-research-*.md` file exists. Literature was gathered manually: PubMed title
  search `CFAP65[Title]` (11 records), the cached GOA publications, and the cached
  Chlamydomonas FAP70 / C2a paper. Abstract-only caches are flagged.

## Identity

- 1,925 aa (alias CCDC108); a series of Ig-like (HYDIN/VesB/CFA65-like) domains, an MSP
  domain and a C-terminal coiled coil; an N-terminal hydrophobic segment is predicted as a
  transmembrane helix (ECO:0000255 only)
  [file:human/CFAP65/CFAP65-uniprot.txt "PANTHER; PTHR46127; CILIA- AND FLAGELLA-ASSOCIATED PROTEIN 65; 1."].

## Central apparatus C2a projection

- Chlamydomonas FAP65 co-precipitates with FAP70 and is lost from fap70 axonemes; inferred
  C2a component [PMID:33988244 "it is likely that FAP65 and FAP147 also are components of C2a"].
- Mouse: CFAP65 anchors at the base of the C2a projection and binds CFAP70 and MYCBPAP;
  loss disintegrates C2a [PMID:39853433 "CFAP65 was found to anchor at the base of the C2a projection of the axoneme, interacting with proteins such as CFAP70 and MYCBPAP"];
  [PMID:39853433 "CFAP65 deficiency led to the disintegration of the C2a projection"].
- CFAP65 fractionates with axonemal (Triton-resistant) proteins in mouse sperm, not with
  membrane proteins [PMID:39853433 "was present in the Triton X-100-resistant fraction containing axonemal proteins"].
- Tissue-specific consequences: severe MMAF and hydrocephalus (ependymal flow reduced),
  little effect on tracheal cilia beating
  [PMID:39853433 "The knockout mice displayed severe sperm flagellar defects (MMAF), high hydrocephalus incidence, but no significant impact on respiratory cilia"];
  [PMID:39853433 "there was no significant difference in tracheal ciliary movement between Cfap65+/+ and Cfap65−/− mice"].
- The authors explicitly note conflicting earlier localizations
  [PMID:39853433 "the localization of CFAP65 across studies has been contradictory, ranging from the acrosome and midpiece to the entire flagellum"].

## Sperm phenotypes (human, mouse)

- Human biallelic null variants cause MMAF (SPGF40)
  [PMID:31501240 "CFAP65 homozygous mutations were identified in four unrelated consanguineous families"] (abstract only);
  [PMID:31571197 "Our experimental observations on human subjects suggested that CFAP65 is involved in sperm flagellum structure and assembly"] (abstract only).
- Wang et al. (full text): acrosome hypoplasia plus flagellar defects; immunostaining in
  acrosome area and midpiece of normal sperm, and cytoplasm of human spermatids
  [PMID:31413122 "CFAP65 staining was detected in the acrosome area and flagellar midpiece of normal spermatozoa"];
  [PMID:31413122 "CFAP65 was specifically localised in the cytoplasm of round spermatid and elongating spermatid"].
- Mouse knockout (abstract only): manchette, acrosome and mitochondrial-sheath defects and
  a proposed cytoplasmic network with MNS1, RSPH1, TPPP2, ZPBP1 and SPACA1
  [PMID:34231842 "CFAP65 may form a cytoplasmic protein network comprising MNS1, RSPH1, TPPP2, ZPBP1 and SPACA1"].
- PMID:33472045 (CFAP47 paper) is the source of the CFAP47 interaction and some
  localization rows; the cached abstract does not mention CFAP65, so those data are unseen.

## Other

- RNA binding (HDA) comes from HeLa mRNA interactome capture
  [PMID:22658674 "to define the mRNA interactome of proliferating human HeLa cells"]; no
  RNA-binding domain or follow-up; abstract only, supplementary list not seen.

## Synthesis

CFAP65 is a structural component at the base of the C2a projection of the axonemal central
apparatus, needed for C2a integrity and therefore for motility of sperm flagella and
ependymal cilia; respiratory cilia are relatively spared. Acrosome, manchette and
mitochondrial-sheath defects are documented in knockouts and patients, but whether CFAP65
acts directly in these (it was reported in acrosome region staining) or they are secondary
to flagellar/manchette disorganization is unresolved.
