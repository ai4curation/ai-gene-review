# PON1 manual review notes

Automated deep research was not available in this lane without starting an extra
`claude_code` worker, so this review uses the seeded GOA references, UniProt, and
the PTHR11799 PAINT export directly.

## Evidence notes

- PTHR11799 PAINT puts lactonase, arylesterase, acyl-homoserine-lactone
  hydrolase, and broad lactone/carboxylic-acid catabolic process terms at the
  vertebrate paraoxonase node (`PTN008526997`). These activities are supported
  for PON1, PON2, and PON3 by the Draganov 2005 recombinant-enzyme substrate
  survey, which found that the human family members are
  `lactonases/lactonizing enzymes` with overlapping aromatic lactone substrates
  and distinct preferences for organophosphates, N-acyl-homoserine lactones,
  and bulky drug lactones (PMID:15772423).
- PON1 has the strongest organophosphate evidence in the human family. The 1991
  purification work concluded that human serum arylesterase and paraoxonase
  activities are catalyzed by one enzyme, and Draganov 2005 reported that
  organophosphates are hydrolyzed almost exclusively by PON1 (PMID:1673382;
  PMID:15772423). Organophosphate hydrolysis is therefore real but secondary to
  the lactonase/arylesterase chemistry that appears shared across the family.
- The PON1 crystal structure used a directed-evolution variant and resolved the
  six-bladed beta-propeller and HDL-binding active-site lid, supporting calcium
  binding and the catalytic fold rather than a distinct process term
  (PMID:15098021).
- PON1 is a secreted HDL-associated serum enzyme. Its unusual retained
  hydrophobic N-terminus binds HDL phospholipids rather than apoA-I directly,
  while apoA-I stabilizes arylesterase activity (PMID:10479665). HDL particle
  rows are therefore direct PON1 biology; ER membrane Reactome rows are
  secretory transit rather than a site of residence or activity.
- PON1-associated HDL can stimulate ABCA1-dependent macrophage cholesterol
  efflux by acting on macrophage phospholipids to increase LPC (PMID:15721011).
  This supports a non-core HDL-linked effect, not a replacement for the core
  hydrolase activities.
- Proteomic rows for blood microparticles and extracellular exosomes report PON1
  in extracellular vesicle fractions (PMID:22516433; PMID:23533145). They are
  compartment detections in extracellular samples, not evidence for a vesicle
  resident function.
- The literature is mixed on purified PON1 antioxidant activity. Teiber 2004
  failed to detect PON1-mediated antioxidant activity in copper- or
  AAPH-initiated in vitro LDL assays (PMID:15342686), while apoM-containing HDL
  contained PON1 and was more protective in LDL-oxidation and cholesterol-efflux
  assays (PMID:16682745). Treat the antioxidant and efflux terms as contextual
  HDL particle phenotypes.
