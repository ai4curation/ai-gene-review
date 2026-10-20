# SLAC1 (At1g12480, Q9LD83) curation notes

## Deep research status

`just deep-research ARATH SLAC1 --provider falcon` failed on 2026-10-20 with
"Failed to authenticate"; the perplexity provider is not configured and the
openai provider returned `invalid_api_key`. No deep-research file was written.
These notes come from my own reading of the cached publications in
`publications/` and the UniProt record (`SLAC1-uniprot.txt`).

## Identity

- UniProtKB Q9LD83 (SLAC1_ARATH), gene SLAC1 (synonyms CDI3, OZS1, RCD3),
  locus At1g12480. 556 aa; cytosolic N-terminal tail (about 1-189), ten
  transmembrane helices, short cytosolic C-terminal tail.
- Family: SLAC1 S-type anion channel family (SLAC/SLAH, IPR030183;
  SLAC1/Mae1/Ssu1/TehA, IPR004695). PANTHER PTHR31269 per `just fetch-gene`.
- Four Arabidopsis paralogues (SLAH1-3) [PMID:18305482 "It belongs to a protein
  family that in Arabidopsis consists of four structurally related members"].

## Molecular function: S-type anion channel

- Cloned twice from guard-cell screens. Negi et al. (CO2 screen):
  [PMID:18305482 "is localized specifically to the plasma membrane of guard cells"];
  mutants over-accumulate anions
  [PMID:18305482 "The loss-of-function mutation in SLAC1 was accompanied by an over-accumulation of the osmoregulatory anions in guard cell protoplasts."].
- Vahisalu et al. (ozone screen):
  [PMID:18305484 "Mutations in SLAC1 impair slow (S-type) anion channel currents that are activated by cytosolic Ca2+ and abscisic acid, but do not affect rapid (R-type) anion channel currents or Ca2+ channel function."]
- Heterologous reconstitution in Xenopus oocytes. SLAC1 alone is silent and
  needs an activating kinase:
  [PMID:20385816 "When expressed heterologously SLAC1 remained electrically silent."]
  [PMID:19955405 "Upon coexpression of SLAC1 with OST1 in Xenopus oocytes, SLAC1-related anion currents appeared similar to those observed in guard cells."]
  Biophysics: slow, deactivating, weakly voltage-dependent; permeability
  I- > NO3- > Br- > Cl- >> HCO3-, malate, SO4 2- (PMID:19955405 full text).
  [PMID:19955405 "Our studies demonstrate that SLAC1 represents the slow, deactivating, weak voltage-dependent anion channel of guard cells controlled by phosphorylation/dephosphorylation."]
- Structure from the bacterial homologue HiTehA, plus SLAC1 mutagenesis in
  oocytes: trimer, each protomer a five-helix pore gated by Phe450
  [PMID:20981093 "SLAC1 is a symmetrical trimer composed from quasi-symmetrical subunits, each having ten transmembrane helices arranged from helical hairpin pairs to form a central five-helix transmembrane pore that is gated by an extremely conserved phenylalanine residue."].
  The DOI-cited GOA rows (DOI:10.1038/nature09487) are this paper (PMID:20981093).
  I confirmed the match by Crossref title and PubMed DOI search.

## Regulation by kinases and phosphatases (input side)

- OST1/SnRK2.6 (Q940H6) binds the SLAC1 N-terminus and phosphorylates it; Ser120
  is required [PMID:19955405 "we identified residue Ser-120 as an important OST1 target."];
  [PMID:19955427 "Here we show that the OST1 kinase interacts with the SLAC1 anion channel, leading to its activation via phosphorylation."]
- PP2CA (P49598) binds SLAC1 directly and inhibits it (PMID:19955427). ABI1/ABI2 block
  OST1-dependent activation (PMID:19955405); ABI1 can also dephosphorylate the SLAC1
  N-terminus after CPK6 phosphorylation (PMID:22689970).
- CPK21 and CPK23 (PMID:20385816) and CPK6 (PMID:22689970, S59) activate SLAC1.
- GHR1 receptor-like kinase (PMID:22730405) and SIF2 (PMID:32327536, Ser65) also
  phosphorylate and activate SLAC1.
- CO2 relay: RHC1 -> HT1 -| OST1 -> SLAC1 (PMID:25599916).

## Output side and physiology

- SLAC1-dependent anion efflux depolarises guard cells and drives stomatal closure
  in response to ABA, CO2, ozone, darkness, low humidity, Ca2+, H2O2 and NO
  [PMID:18305484 "The plasma membrane protein SLAC1 is essential for stomatal closure in response to CO2, abscisic acid, ozone, light/dark transitions, humidity change, calcium ions, hydrogen peroxide and nitric oxide."].
- SLAC1 binds and inhibits the inward K+ channel KAT1 (not KAT2), coupling closure
  to inhibition of opening
  [PMID:27002025 "Voltage-clamp results demonstrated that SLAC1 inhibited KAT1 dramatically, but did not inhibit KAT2."].
- Systemic light-stress stomatal closure requires SLAC1 (PMID:29463779). The
  8-nitro-cGMP closure pathway acts upstream of SLAC1 (PMID:23396828).

## Curation decisions (summary)

- Core MF is voltage-gated monoatomic anion channel activity (GO:0008308). The broader
  "monoatomic anion transmembrane transporter activity" rows are MODIFY to it.
- Bare protein-binding rows are MODIFY to protein kinase binding (OST1, CPKs, GHR1,
  SIF2) or potassium channel inhibitor activity (KAT1, AKT2). Rows with KAT2 (not
  inhibited) and KC1 are REMOVE.
- The AtSubP "nucleus" ISM row is REMOVE. SLAC1 is a polytopic plasma-membrane
  channel with no nuclear evidence.
- The CPK6 protein kinase binding row (PMID:20385816) cannot be checked from the
  abstract-only cache. The abstract names only CPK21/23. CPK6 binding and activation
  of SLAC1 is independently established (PMID:22689970), so the row is kept.
