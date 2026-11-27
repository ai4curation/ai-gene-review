# HRH2 notes

Deep research providers unavailable; research from UniProt (P25021), cached publications, Reactome.

## Identity / function
- Histamine H2 receptor: class A, 7-transmembrane G-protein-coupled receptor. [UniProt "G
  protein-coupled receptor for histamine, primarily mediating gastric acid secretion"].
- Couples to Gs, activating adenylate cyclase and raising cAMP [UniProt "couples to G(s) G alpha
  proteins upon histamine binding, leading to activation of adenylate cyclase and increased
  intracellular cyclic AMP"]; stimulates parietal-cell HCl secretion.
- Additional roles: immune modulation (suppresses IL-12, stimulates IL-10 via H2 [PMID:9725260]),
  CNS histaminergic neurotransmission, cardiac stimulation.
- Interacts with RAMP2/RAMP3 (receptor activity-modifying proteins) in a GPCR-RAMP interactome
  screen [PMID:39083597].

## Localization (cell-surface benchmark)
- CELL-SURFACE plasma-membrane GPCR; multi-pass (7TM). Ligand (histamine) binds the
  transmembrane pocket accessible from the extracellular side. [UniProt "Cell membrane; Multi-pass
  membrane protein"]. In neurons also dendrite/synapse.
- Conclusion: plasma membrane, cell-surface accessible (extracellular ligand-binding pocket).

## Curation
- GPCR activity / GPCR signaling / cyclic-nucleotide signaling: MODIFY or TOO_GENERAL toward the
  specific histamine receptor activity and adenylate cyclase-activating GPCR signaling.
- Bare protein binding (RAMP2/3 IPI): REMOVE under policy (no specific RAMP-binding MF term).
- positive regulation of vasoconstriction (IEA InterPro2GO): over-annotation; H2 vascular effects
  are predominantly vasodilatory (cAMP), and the call derives from a generic histamine-receptor
  domain mapping -> MARK_AS_OVER_ANNOTATED.
