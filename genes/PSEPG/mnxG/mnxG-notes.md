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

## EC 1.16.3.3 (ExplorEnz, looked up 2026-10-28)
The load-bearing claim behind the proposed term, recorded here verbatim-ish so it need
not be re-checked:
- Accepted name: **manganese oxidase**
- Reaction: 4 Mn2+ + 2 O2 + 4 H2O = 4 Mn(IV)O2 + 8 H+ (overall reaction)
  - (1a) 4 Mn2+ + O2 + 4 H+ = 4 Mn3+ + 2 H2O
  - (1b) 4 Mn3+ + O2 + 6 H2O = 4 Mn(IV)O2 + 12 H+
- Other name(s): mnxG (gene name); mofA (gene name); moxA (gene name); cotA (gene name)
- Systematic name: manganese(II):oxygen oxidoreductase
- Comments: "The enzyme, which belongs to the multicopper oxidase family, is found in many
  bacterial strains. It oxidizes soluble manganese(II) to insoluble manganese(IV) oxides."

Two consequences. (i) The EC entry lists **mnxG itself as a gene name** for this activity,
which is independent corroboration of this gene's identity on top of the GB-1 genetics.
(ii) The product of the overall reaction is Mn(IV)O2; Mn(III) is an **intermediate**
(step 1a), not the product. The proposed term's definition therefore states MnO2 as the
product and the one-electron steps are kept in `justification` as mechanism, matching
[PMID:42757987 "Sequential one-electron oxidation reactions occur along the tunnel, with Mn(IV) ultimately condensing into MnO2 nanoparticles"].

## GO
- Only GOA row: copper ion binding (IEA InterPro) -> ACCEPT.
- NEW: GO:0016724 (IMP, PMID:23124227). No GO term exists for EC 1.16.3.3 manganese
  oxidase (checked ec2go and QuickGO search, 2026-10-28); proposed as new term.
- No BP added: there is no GO process for Mn(II) oxidation/biomineralization. A sibling
  review (SIL1, ai4curation/ai-gene-review#5636) ran the OLS search for a lineage-neutral
  biomineralization process term and found none: every hit is GO:0031214 biomineral tissue
  development or a descendant, all of which presuppose an animal tissue. The decline here
  is consistent with that finding.
- `interpro/panther/PTHR48267/` was fetched by `just fetch-gene` for mcoA, not for mnxG:
  UniProt assigns mnxG no PANTHER family. Those files are cited from the mcoA review.

## CMMMech record notes (CMMMech repository, data/records/manganese.yaml; not edited here)
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
