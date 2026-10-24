# BAS1 (G5EHI7, MGG_04795) - Magnaporthe oryzae Biotrophy-associated secreted protein 1 - curation notes

## 2026-10-02 initial review

Sources: UniProt G5EHI7 (Swiss-Prot), BAS1-deep-research-falcon.md, cached PMID:19357089 (full text),
PMID:20435900 (abstract only), and newly cached (PMIDs verified by PubMed search "BAS1 Magnaporthe oryzae"
and citation lookup) PMID:23774898 (full text), PMID:38722963 (full text), PMID:29551940 (full text),
PMID:29931642.

### Identity
- 115 aa secreted protein, no Cys, no paralogs or orthologs
  [PMID:19357089 "encodes a secreted protein with 115 amino acids, but no Cys residues"];
  [PMID:19357089 "no orthologs occur in other organisms"]. No InterPro domain/family in UniProt.
- Not related to yeast BAS1 (Myb transcription factor; its M. oryzae homolog is MoMyb1, PMID:25885817 -
  name collision only, not used).

### Expression and localization
- Strongly induced in invasive hyphae [PMID:19357089 "BAS1 was 100-fold upregulated in IH"].
- Secreted into BICs; colocalizes with AVR-Pita1 [PMID:19357089 "Therefore, BAS1 encodes a small unique protein that is secreted into BICs."].
- BIC lies outside fungal plasma membrane and is plant-derived
  [PMID:23774898 "confirming that the BIC lies outside the fungal plasma membrane"].
- NB: in Mosquera 2009, host-cytoplasm entry of BAS1 is hypothesised, not shown
  [PMID:19357089 "BAS1 and BAS2 might represent structural BIC components, or they might represent candidate effectors that are translocated across the EIHM into the rice cell"].
  The abstract does say BAS proteins were "secreted into rice cells", which is likely what the curator used.
- Translocation into rice cytoplasm and movement into neighbouring cells shown by Khang 2010
  [PMID:20435900 "were translocated into the rice cytoplasm"]; [PMID:20435900 "and BAS1 proteins that reached the rice cytoplasm moved into uninvaded"].
- Secretion is BFA-insensitive and requires exocyst Exo70/Sec5 and t-SNARE Sso1 (BAS1 is the cargo)
  [PMID:23774898 "Similar impaired secretion was observed for independent transformants expressing a different cytoplasmic effector, Bas1:mRFP"].
- Uptake into host blocked by clathrin inhibitors ES9/ES9-17 (host CME does the work, BAS1 is cargo)
  [PMID:38722963 "fluorescently labeled effectors Bas1 and Pwl2 in rice cells, leading to swollen"].

### Function / phenotype
- Knockouts: no major pathogenicity phenotype; slight lesion decreases in 3/6 whole-plant assays
  [PMID:19357089 "There was not a major pathogenicity phenotype"].
- Yang et al. (Saudi J Biol Sci 2017; ESPR 2019): purified recombinant BAS1 sprayed on leaves triggers
  callose/ROS; overexpression strain more virulent [PMID:29551940 "showed in vitro the purified expression product caused rapid callose deposition"].
  Overexpression and exogenous recombinant protein; no knockout/complementation; modest journals. Not used
  to support any GO term. UniProt FUNCTION line derives from these.
- Molecular activity and host target unknown (deep research concurs).

### Annotation decisions
- GO:0005576 extracellular region EXP (PMID:19357089) + IEA: ACCEPT (secreted, BIC outside fungal PM).
- GO:0030430 host cell cytoplasm EXP (PMID:20435900): ACCEPT - core location.
- GO:0030430 host cell cytoplasm EXP (PMID:19357089): ACCEPT, but note the direct evidence is in PMID:20435900;
  2009 paper only shows BIC accumulation (do not overrule curator; term is correct for the gene).
- GO:0030430 IEA: ACCEPT.
- No NEW terms. Rejected: GO:0044053 translocation of peptides or proteins into host cell cytoplasm
  (BAS1 is the cargo; no translocation motif; host clathrin-mediated endocytosis performs uptake ->
  fails participation test). No effector-mediated suppression/induction terms: no mechanistic evidence;
  overexpression data are weak and partly contradictory (induces defense vs increases virulence).
- No MF assigned (unknown).

### Project question notes
- Q1: GOA has no process terms at all for BAS1 - only CC. Appropriate: there is no experimental basis for a
  symbiont-side process term; UniProt free-text FUNCTION ("induces basal defense") is from weak
  overexpression/recombinant-protein studies and should not be converted to plant-side defense terms.
- Contrast with slp1: slp1 is apoplastic (EIHM, BFA-sensitive) with a defined MF; BAS1 is a BIC/cytoplasmic
  effector marker with no MF. GO lacks a BIC CC term; host cell cytoplasm + extracellular region is the best
  available pair.
