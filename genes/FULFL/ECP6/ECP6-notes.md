# ECP6 (Fulvia fulva / Cladosporium fulvum; UniProt B3VBK9) - curation notes

## Sources
- UniProt B3VBK9 record (ECP6-uniprot.txt); 3 LysM domains, PDB 4B8V/4B9H.
- ECP6-deep-research-falcon.md (Falcon/Edison deep research).
- PMID:18452583 Bolton et al. 2008 (abstract-only cache) - discovery, apoplastic secretion, virulence.
- PMID:20724636 de Jonge et al. 2010 Science (abstract-only cache; PubMed metadata verified) - chitin sequestration, PTI suppression.
- PMID:23840930 Sanchez-Vallet et al. 2013 eLife (full text cached) - crystal structure, intrachain LysM1-LysM3 groove.

## Identity / localization
- Secreted into tomato leaf apoplast during infection [PMID:18452583 "During tomato leaf colonization, the biotrophic fungus Cladosporium fulvum
secretes several effector proteins into the apoplast"]; Ecp6 identified among proteins secreted during C. fulvum-tomato interactions
[PMID:18452583 "Three novel C. fulvum proteins were identified: CfPhiA, Ecp6 and
Ecp7"].
- Virulence factor: RNAi silencing reduces virulence; heterologous expression in Fusarium oxysporum increases virulence
[PMID:18452583 "by RNA interference (RNAi)-mediated gene silencing we demonstrate
that Ecp6 is instrumental for C. fulvum virulence on tomato"].

## Molecular function: chitin binding
- [PMID:20724636 "During infection, Ecp6 sequesters chitin oligosaccharides that are released from the cell walls of invading hyphae to prevent elicitation of host immunity."]
- Structure: intrachain LysM1-LysM3 dimerization forms buried groove; ultra-high affinity
[PMID:23840930 "The composite LysM1–LysM3 binding site shows ultra-high chitin-binding affinity, thus explaining how LysM effectors outcompete plant host receptors for chitin binding."]
[PMID:23840930 "A first binding phase in which one chitin molecule was bound with ultra-high affinity (kd = 280 pM"].
- LysM2 binds chitin with low micromolar affinity yet still suppresses chitin-triggered immunity, proposed via receptor-complex perturbation (hypothesis)
[PMID:23840930 "Consequently, the suppression of chitin-triggered immunity by LysM2 is unlikely to work via chitin oligosaccharide sequestration."].
- Glycan array / chitosan / cellulose specificity and failure to protect hyphae against chitinases (in contrast to Avr4) are reported in de Jonge 2010 full text
(not cached; abstract only); taken from deep research and UniProt FUNCTION text. Not quoted in YAML.

## Biological process
- [PMID:20724636 "Ecp6 of the fungal plant pathogen Cladosporium fulvum mediates virulence through perturbation of chitin-triggered host immunity."]
- GO:0140423 effector-mediated suppression of host pattern-triggered immunity signaling (EXP, PMID:23840930) - correct symbiont-side term; matches
the term used for M. oryzae Slp1 (genes/PYRO7/slp1).

## Decisions
- All 4 GOA rows ACCEPT (2x extracellular region, chitin binding, GO:0140423).
- No NEW terms: no chitinase-protection term (negative evidence); no receptor/perception terms (those belong on CEBiP/CERK1);
  a host-apoplast-specific CC term was considered but not added - extracellular region is adequate and consistent with slp1.
- Project question 2 (LysM effector vs receptor leakage): no InterPro2GO rows on ECP6 at all; effector carries only the activity term
  (chitin binding) and the symbiont-side process term, no "chitin-mediated signaling"/"defense response" leakage.
