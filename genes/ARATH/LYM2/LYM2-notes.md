# LYM2 (At2g17120, UniProt O23006) curation notes

## Identity
- LysM domain-containing GPI-anchored protein 2; also called AtCEBiP / CEBiP-like1. Closest
  Arabidopsis homologue of rice OsCEBiP. UniProt: signal peptide 1-23, two annotated LysM
  domains (108-155, 172-216), GPI-anchor at D318, C-terminal propeptide removed; no
  transmembrane or intracellular domain.
- Deep research (falcon) available: `LYM2-deep-research-falcon.md`; consistent with primary papers.
- Note that "CEBiP-like1" in Petutschnig 2010 / Wan 2012 is LYM2: [PMID:20610395 "the LysM protein At2g17120 (LYM2), the closest Arabidopsis homolog of the rice chitin-binding protein CEBiP"].

## Molecular function: chitin binding
- [PMID:22891159 "Only one of three CEBiP homologs, AtCEBiP (LYM2), showed a high-affinity binding for chitin oligosaccharides similar to rice CEBiP."] (abstract only in cache)
- [PMID:22891159 "AtCEBiP also represented the major chitin-binding protein in the Arabidopsis membrane."]
- Chitin bead pulldowns: [PMID:22744984 "We repeated this experiment and also found that LYK1, LYK4, LYK5, and CEBiP-like1 were pulled down by chitin magnetic beads and eluted by chitooctaose"] — basis for the TAIR IDA.
- LYM1/LYM3 do not bind chitin (they act in peptidoglycan perception with CERK1).

## Not required for canonical CERK1 chitin signalling
- [PMID:22891159 "indicating that AtCEBiP is biochemically functional as a chitin-binding protein but does not contribute to signaling"]
- [PMID:22744984 "Our data show that mutations in these genes, either singly or in combination, did not compromise the response to chitin treatment."]
- [PMID:23674687 "these results indicate that LYM2 is not necessary for CERK1 activation and CERK1-mediated responses and vice versa"]
- So the rice OsCEBiP-OsCERK1 model does not transfer to Arabidopsis; in Arabidopsis LYK5 is the high-affinity chitin receptor that recruits CERK1 (see genes/ARATH/LYK5).

## Chitin-triggered plasmodesmal closure
- [PMID:23674687 "We show that LYSIN MOTIF DOMAIN-CONTAINING GLYCOSYLPHOSPHATIDYLINOSITOL-ANCHORED PROTEIN 2 (LYM2), the Arabidopsis homolog of a rice chitin receptor-like protein, mediates a reduction in molecular flux via plasmodesmata in the presence of chitin."]
- CERK1 not required: [PMID:23674687 "Surprisingly, the chitin-recognition receptor CHITIN ELCITOR RECEPTOR KINASE 1 (CERK1) is not required for chitin-induced changes to plasmodesmata flux"]
- Localization: [PMID:23674687 "In accordance with a role in the regulation of intercellular flux, LYM2 is resident at the plasma membrane and is enriched at plasmodesmata."]
- Mechanism (Cheval 2020): requires LYK4, LYK5, RBOHD (Ser133), CPK6, CPK11; callose deposition. [PMID:32284410 "Focusing on chitin signaling, we found that responses in the plasmodesmal PM require the LysM receptor kinases LYK4 and LYK5 in addition to LYM2."]
- [PMID:32284410 "LYM2 also exhibits greater homo-FRET in the plasmodesmal PM than in the PM, indicating it oligomerizes or clusters there, possibly to form a signaling platform."]
- [PMID:32284410 "LYM2 can associate with both LYK4 and LYK5, but we detected only LYK4 in plasmodesmata, suggesting that chitin-triggered plasmodesmal signaling is mediated directly by a LYM2-LYK4 complex."]
- LYM2 lacks intracellular domains: [PMID:32284410 "LYM2 has no intracellular domains for signaling"]
- Poplar orthologues do the same (PMID:42516602), suggesting conservation in dicots.

## Defense against fungi
- Botrytis: [PMID:23674687 "Chitin-triggered regulation of molecular flux between cells is required for defense responses against the fungal pathogen Botrytis cinerea"]
- Alternaria brassicicola: [PMID:23803749 "Here we show that LYM2 does contribute to disease resistance against fungal pathogens but the mechanism seems independent of chitin signaling mediated by CERK1."]
- Not required against Pto DC3000: [PMID:23674687 "Indeed, LYM2 is not required for defense against Pto DC3000."]

## GOA observations
- GOA has NO biological process annotation for LYM2 at all (and OsCEBiP also has none),
  despite clear mutant data from Faulkner 2013 and Cheval 2020. LYK5 carries
  `cellular response to chitin` (IBA, IEP) and `innate immune response` (IMP).
- Mitochondrion HDA (PMID:28887381) is a co-fractionation profiling call; contradicted by
  the signal peptide/GPI anchor and imaging. Removed.
- Plasma membrane / plasmodesma rows all consistent with imaging (PMID:23674687).
- GO lacks a term for regulation of plasmodesmata-mediated intercellular transport; proposed.

## Decisions
- NEW: GO:0071323 cellular response to chitin (IMP, PMID:23674687). Participation test: LYM2
  is the chitin-binding receptor component for this response (it performs ligand perception),
  not merely a required downstream component. Comparator: LYK5 and CERK1 (chitin-binding LysM
  receptors) carry chitin-response terms.
- NEW: GO:0050832 defense response to fungus not added — evidence is infection phenotype
  (necessity); recorded as non-asserted context and in questions.
