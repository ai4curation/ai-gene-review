# mnxG (B0KQT1, PputGB1_2447) — Pseudomonas putida GB-1

## Identity
- TrEMBL B0KQT1, 1,944 aa, locus PputGB1_2447. UniProt has no gene name; the RecName
  "Manganese-oxidizing multicopper oxidase MnxG" is a ProtNLM machine name (ECO:0008006),
  which happens to agree with the literature name. Folder `mnxG` follows the literature
  symbol (fetched by accession with `--alias mnxG`).
- Domains: SignalP signal peptide 1-26; PROSITE MULTICOPPER_OXIDASE2 (PS00080),
  IPR002355 Cu_oxidase_Cu_BS, NCBIfam NF041487 copper_ox_MnxG, IPR048215 MnxG-like.
  No PANTHER family assigned.

## Function (genetic, not biochemical)
- Identified by genome comparison and MnxR regulation; deletion of each MCO alone leaves
  oxidation, the double deletion abolishes it [PMID:23124227 "loss of oxidation was attained only upon deletion of
both genes"; "PputGB1_2447 and PputGB1_2665 encode two
MCOs that are independently capable of oxidizing both Mn(II) and Mn(III)"].
- Strains retaining only MnxG oxidize Mn(III)-citrate and Mn(III)-DFOB
  [PMID:29706936 "Evidence of Mn(III)-L oxidation by MnxG and McoA, but not MopA suggests that this step may be predominately MCO driven, at least in the absence of light."].
- MnxG drives initial oxide precipitation, mnxG is induced at low Mn(II)
  [PMID:40122939 "we find that MnxG is responsible for the initial precipitation of Mn oxides"];
  [PMID:40470839 "with an increasing proportion of cells expressing
mnxG (<10 μM) and then mcoA (>10 to 500 μM)"].
- No biochemistry on the GB-1 enzyme [PMID:42757987 "While the biochemical characteristics of MnxG and McoA from P. putida GB-1 have not been investigated"].
- Localization not determined [PMID:27084014 "the cellular localization of MnxG and McoA is unknown, although the proteins are likely exported"];
  review infers Sec export from the signal peptide [PMID:42757987 "Both MnxG and McoA possess amino-terminal Sec system signal peptides, indicating that they are transported across the cell membrane by the Sec system"].
  No CC term added (single line of evidence, no assay).

## Relationship to McoA and MopA (paralogy)
- MnxG and McoA are both MCOs but not recent paralogs: different copper-domain
  arrangement [PMID:42757987 "The arrangement of these Cu-binding domains also differs between the two proteins, suggesting they did not arise by gene duplication"].
- MopA (PputGB1_3353) is an animal heme peroxidase with RTX Ca-binding domains,
  unrelated in fold to the MCOs: functional redundancy, not paralogy
  [PMID:27084014 "Mass spectrometry and directed mutagenesis identified this protein as MopA, an animal heme peroxidase"].

## GO
- Only GOA row: copper ion binding (IEA InterPro) -> ACCEPT.
- NEW: GO:0016724 (IMP, PMID:23124227). No GO term exists for EC 1.16.3.3 manganese
  oxidase (checked ec2go and QuickGO search, 2026-10-28); proposed as new term.
- No BP added: there is no GO process for Mn(II) oxidation/biomineralization.

## CMMMech record notes (data/records/manganese.yaml; not edited)
- Protein example evidence says "genetic deletion and complementation in Wright et al.
  (2018)". Wright 2018 used existing mutants (the deletions were made in Geszvain et al.
  2013, PMID:23124227, and Geszvain et al. 2016, PMID:27084014, plus two strains built in
  Wright 2018); I found no complementation of mnxG in Wright 2018. The edge
  "Deletion and complementation of mnxG ... confirm its dominant role" is stronger than
  the cited source: no complementation is reported there, and "dominant" is supported
  by Gehin et al. 2025 (initial precipitation) rather than by Wright 2018.
- functional_role says MnxG catalyzes "two-electron oxidation"; MCOs transfer electrons
  one at a time, Mn(II)->Mn(III)->Mn(IV) [PMID:42757987 "Both MnxG and McoA can oxidize Mn(II) to Mn(III) and Mn(III) to Mn(IV), resulting in a Mn(IV) oxide product."].
  "Catalyzing" should be qualified as genetically inferred: the enzyme has not been
  purified (quote above).
- "Primary multicopper oxidase" is reasonable only at low Mn(II); McoA dominates at higher
  Mn(II) (PMID:40470839).
