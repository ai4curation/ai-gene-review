# Tes (testin), Rattus norvegicus (UniProtKB:Q2LAP6) - manual literature synthesis

No deep-research provider API keys were available in this session, so this synthesis was written by
the reviewer from cached publications (`publications/PMID_*.md`) and PubMed searches (2026-10-28).
Full text was available for PMID:21278383 and PMID:12695497; the others were read as abstracts only.

## Identity and domain architecture

- Rat Tes (Q2LAP6, 419 aa, RGD:1566346, GeneID 500040) is the orthologue of human TES (Q9UGI8) and
  mouse Tes (P47226). It has an N-terminal PET domain (residues 92-199) and three C-terminal LIM
  zinc-binding domains (232-295, 297-357, 360-419) [UniProtKB:Q2LAP6 FT DOMAIN], and "Belongs to the
  prickle / espinas / testin family" [UniProtKB:Q2LAP6].
- The N- and C-terminal halves bind each other, a closed conformation that masks the zyxin site
  [PMID:12695497 "we demonstrate that the two halves of Tes interact with each other in vitro and in vivo"].

## Localisation

- Human TES localises to focal adhesions, stress fibres and cell-cell contacts
  [PMID:12571287 "the TES protein is localised at focal adhesions, actin stress fibres and areas of cell-cell contact"].
- Recruitment to focal adhesions depends on zyxin, which binds LIM1
  [PMID:12695497 "zyxin is required to recruit Tes, as well as Mena and VASP, but not vinculin or paxillin, to focal adhesions"];
  [PMID:21278383 "Tes is recruited to focal adhesions via a direct interaction between its LIM1 domain and zyxin (27)."].
- In rodent testis, Tes is in the subacrosomal layer (acroplaxome) of round spermatids together with
  Arp7A (ACTL7A) and Mena, but not on the Golgi [PMID:21278383 "all three proteins are actually localized
  in the subacrosomal layer that links the acrosome to the nuclear envelope"]. GO has no acroplaxome term.

## Interactions (binding activity)

- Rat-specific: Tes co-immunoprecipitates with Arp7A and Mena from rat testis
  [PMID:21278383 "Arp7A, Tes, and Mena are complexed to each other in rat testes extracts"].
- LIM2(-3) binds the N-terminal extension of Arp7A directly (crystal structure of
  1-65Arp7A-LIM2-3Tes-EVH1Mena) [PMID:21278383 "the N-terminal extension to the actin-like fold of Arp7A interacts directly with the LIM2 domain of Tes"].
- LIM3 binds the EVH1 domain of Mena, but not VASP or EVL, occluding the FPPPP site
  [PMID:18158903 "the LIM3 domain of Tes, which lacks the FPPPP motif, binds to the EVH1 domain of Mena, but not to those of VASP or Evl"].
- Tes is in complexes with actin, Mena and VASP in cells
  [PMID:12695497 "Coimmunoprecipitations demonstrate that in vivo Tes is complexed with actin, Mena, and vasodilator-stimulated phosphoprotein (VASP)."];
  chicken TES pulls down zyxin and actin [PMID:14743347 "GST-cTES can pull-down zyxin and actin"].
- Zinc: the LIM2-3 crystal structure contains two zinc ions per LIM domain
  [PMID:21278383 "Using a simple metric based on the four common zinc ions in the tandem LIM structures"].

## Cellular roles (phenotypes, human/chicken cells)

- Overexpression increases cell spreading on fibronectin [PMID:12571287]; chicken TES overexpression
  increases spreading and decreases motility [PMID:14743347].
- RNAi loss of TES in HeLa cells causes loss of stress fibres and reduced RhoA activity
  [PMID:15662727 "we demonstrate that loss of TES from focal adhesions results in loss of actin stress fibres"].
- LIM3 regulates Mena-dependent migration [PMID:18158903 "It also regulates cell migration through a Mena-dependent mechanism."].
- Growth suppression / candidate tumour suppressor: forced expression reduces colony formation
  [PMID:11420696 "forced expression of TES in HeLa or OVCAR5 cells, resulted in a profound reduction in growth potential"];
  negatively regulates T47D proliferation [PMID:12695497]. These are overexpression phenotypes in tumour
  lines; a direct mechanism is not established.

## No rat-specific functional studies beyond PMID:21278383 were found.
