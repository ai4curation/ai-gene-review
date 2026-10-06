# MLKL (human, Q8NB16) — curation notes

**Provenance note:** Provider deep research for this gene FAILED (Falcon returned
HTTP 402 Payment Required; Perplexity was not configured). No
`MLKL-deep-research-<provider>.md` exists. The synthesis below replaces it and was
written manually from the UniProt record (Q8NB16) and the cached publications in
`publications/` (abstracts and, where available, PMC full text).

## Identity and architecture

- Mixed lineage kinase domain-like protein, 471 aa. N-terminal four-helix bundle
  (4HB) "killer" domain plus brace helices, C-terminal pseudokinase domain
  (UniProt DOMAIN 194..469). Belongs to the protein kinase superfamily but is a
  catalytically inactive pseudokinase.
- [PMID:24012422 "Structurally, MLKL comprises a four-helical bundle tethered to the
  pseudokinase domain, which contains an unusual pseudoactive site. Although the
  pseudokinase domain binds ATP, it is catalytically inactive"]
- [PMID:24703947 "binds to RIP3 through its kinase-like domain but lacks kinase
  activity of its own"]
- Human pseudokinase domain crystal structure, nucleotide binding probed by
  mutagenesis [PMID:24219132 "we report the crystal structure of the human MLKL
  pseudokinase domain at 1.7 Å"]. Note: Zhao et al. 2012 [PMID:22421439] reported
  apparent kinase activity of MLKL in vitro, but later structural and biochemical
  work established it is a pseudokinase; GOA carries NOT annotations for kinase
  activity, which are correct.

## Activation by RIPK3

- Identified as the target of necrosulfonamide and a RIP3 interactor; RIP3
  phosphorylates T357/S358 [PMID:22265413 "MLKL was phosphorylated by RIP3 at the
  threonine 357 and serine 358 residues, and these phosphorylation events were
  critical for necrosis"].
- Phosphorylation acts as a molecular switch [PMID:24012422 "its essential
  nonenzymatic role in necroptotic signaling is induced by receptor-interacting
  serine-threonine kinase 3 (RIPK3)-mediated phosphorylation"].
- Pseudokinase domain restrains the 4HB [PMID:25288762 "the MLKL pseudokinase domain
  acts as a latch to restrain the N-terminal four-helix bundle (4HB) domain"].
- Necrosome association with RIP1/RIP3/PGAM5 [PMID:22265414 "The programmed necrosis
  induced by TNF-α requires the activities of the receptor-interacting
  serine-threonine kinases RIP1 and RIP3 and their interaction with the mixed
  lineage kinase domain-like protein MLKL"].
- Highly phosphorylated soluble inositol phosphates (IP6 etc.) are required
  co-activators [PMID:29883610 "purified MLKL specifically bound the IP6 affinity
  reagent but not a phosphate control reagent (Figure 6C), suggesting that MLKL
  directly binds IP6"; "genetic disruption of IP kinases to abolish production of
  higher order inositol phosphates blocked necroptosis downstream of MLKL
  phosphorylation by RIPK3"].

## Oligomerization, membrane translocation, membrane disruption (executioner role)

- Oligomerization: trimer [PMID:24316671 "MLKL forms a homotrimer through its
  amino-terminal coiled-coil domain"]; tetramer [PMID:24366341 "Both the
  HBD*-mediated and TNF-induced complexes of MLKL(ND) or MLKL are tetramers"];
  high-molecular-weight complexes [PMID:25288762]. Exact stoichiometry is
  context-dependent; homo-oligomerization per se is well established.
- Translocation to plasma membrane is required [PMID:24316671 "the plasma membrane
  localization of trimerized MLKL is critical for mediating necroptosis"];
  [PMID:24366341 "translocation of these complexes to lipid rafts of the plasma
  membrane precedes cell death"].
- Phosphoinositide binding and direct membrane permeabilization: [PMID:24813885 "a
  patch of positively charged amino acids on the surface of the 4HBD binds to
  phosphatidylinositol phosphates (PIPs) and allows recruitment of MLKL to the
  plasma membrane"; "recombinant MLKL, but not a mutant lacking these positive
  charges, induces leakage of PIP-containing liposomes as potently as BAX"];
  [PMID:24703947 "The phosphorylated MLKL forms an oligomer that binds to
  phosphatidylinositol lipids and cardiolipin. This property allows MLKL to move
  from the cytosol to the plasma and intracellular membranes, where it directly
  disrupts membrane integrity, resulting in necrotic death."].
- Downstream ion flux: Ca2+ influx (TRPM7 implicated) [PMID:24316671]; Na+ influx
  [PMID:24366341]. Membrane localization is necessary but not sufficient
  [PMID:25288762 "membrane localization is necessary, but insufficient, to induce
  cell death"].
- ESCRT-III counteracts MLKL-induced PM damage [PMID:28388412 "The activation of
  mixed lineage kinase-like (MLKL) by receptor-interacting protein kinase-3 (RIPK3)
  results in plasma membrane (PM) disruption and a form of regulated necrosis,
  called necroptosis."].

## Genetics / physiology

- Mlkl-null mice are viable and resistant to necroptosis [PMID:23835476 "found Mlkl
  to be dispensable for normal mouse development as well as immune cell
  development"]; [PMID:24012422 "cells derived from these animals were resistant to
  TNF-induced necroptosis unless MLKL expression was restored"].
- Antiviral role and nuclear necroptosis during influenza infection are inferred
  from mouse (UniProt "By similarity"; ZBP1-RIPK3-MLKL axis). Human-specific
  evidence not reviewed here.
- Species specificity: human MLKL interacts with human but not mouse RIPK3 (UniProt).

## Curation conclusions

- Core: executioner of necroptosis (GO:0097528 execution phase of necroptosis);
  disrupts the plasma membrane (GO:0140912 membrane destabilizing activity) after
  binding phosphatidylinositol phosphates (GO:1901981) to target it; binds IP6 (GO:0000822) as an obligate activation cofactor.
- Kinase NOT annotations: accept.
- protein binding (RIPK3, IPI x3): MODIFY to protein kinase binding (GO:0019901).
- GO:0140911 pore-forming activity is restricted to the membrane of another cell and
  does not fit, but GO:0140912 membrane destabilizing activity ("binding to a membrane
  and increasing its permeability") does, and is the core activity used for NINJ1. It is
  now MLKL's core molecular function (NEW, IDA, PMID:24813885 liposome leakage), with
  phosphatidylinositol phosphate binding kept as the membrane-targeting activity.
