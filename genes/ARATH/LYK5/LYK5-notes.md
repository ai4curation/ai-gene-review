# LYK5 (At2g33580, O22808) curation notes

## Sources
- Deep research: `LYK5-deep-research-falcon.md` (present).
- Cached papers: PMID:25340959 (Cao 2014, full text), PMID:22744984 (Wan 2012, partial full text: abstract plus discussion), PMID:34558681 (Giovannoni 2021, full text), PMID:28513921 (Erwig 2017, abstract only), PMID:28195333 (Liao 2017, abstract only), PMID:32595659 (Huang 2020, CPK5).

## Key findings
- LYK5 is the primary high-affinity chitin receptor [PMID:25340959 "the binding affinity of AtLYK5 for chitooctaose was measured (Kd = 1.72 µM), which is roughly 200-fold higher than measured for AtCERK1 under the same conditions (Kd = 455 µM)"].
- It forms a chitin-dependent complex with CERK1 [PMID:25340959 "AtLYK5 interacts with AtCERK1 in a chitin-dependent manner. Chitin binding to AtLYK5 is indispensable for chitin-induced AtCERK1 phosphorylation."].
- It is redundant with LYK4 [PMID:25340959 "Atlyk4/Atlyk5-2 double mutants show a complete loss of chitin response"].
- The kinase domain is a pseudokinase but is required for function [PMID:25340959 "no kinase activity was detected using the AtLYK5 kinase domain"]. The K395E variant still complements, while ΔKD fails and cannot co-IP with CERK1.
- Ligand-independent homodimer [PMID:25340959 "AtLYK5 homodimers were detected even in the absence of chitin and this association was independent of the presence of AtCERK1"].
- No basal bacterial phenotype [PMID:25340959 "Untreated Atcerk1 and Atlyk5-2 mutant plants showed wild-type levels of resistance to the bacterial pathogen Pseudomonas syringae pv. tomato DC3000."]. Giovannoni 2021 says the opposite in passing, citing the same paper; we rely on the primary paper.
- Localization and trafficking [PMID:28513921 "Both CERK1 and LYK5 localized to the plasma membrane and showed constitutive endomembrane trafficking."] After chitin, CERK1 phosphorylates LYK5, which is internalized.
- PUB13 controls basal LYK5 abundance [PMID:28195333 "PUB13 could ubiquitinate the LYK5 kinase domain in vitro"].
- CPK5/CPK6 phosphorylate LYK5 at S323 and S542 [PMID:32595659 "Ser-323 and Ser-542 of AtLYK5 are important phosphorylation residues by AtCPK5"].
- Weak interaction with LYK2 [PMID:34558681 "suggesting that LYK2 and LYK5 can physically interact"].

## Decisions
- protein binding (CERK1, LYK2): REMOVE as uninformative, consistent with the CERK1 review.
- extracellular region (ISM): REMOVE. This is a signal-peptide default; LYK5 is a type I plasma membrane protein.
- ATP binding (IEA): MARK_AS_OVER_ANNOTATED. Pseudokinase; the K395E variant rescues; ATP binding never tested.
- response to molecule of bacterial origin (IBA): MARK_AS_OVER_ANNOTATED, with a propagation_review.
- cellular response to oxygen-containing compound (ARBA): over-annotated ancestor of cellular response to chitin.
- NEW GO:0038187 pattern recognition receptor activity. Comparators carrying the term: RLP23, RLP42 (a non-catalytic ligand-binding PRR), SOBIR1.
- NEW GO:0032491 detection of molecule of fungal origin. Comparators carrying the term: CERK1 (IMP), RLP23, RLP30.
- Considered but not added: GO:0002752 (cell surface PRR signaling pathway). PAINT gives the IBA to CERK1 and LYK3 but not LYK5, so this looks like a deliberate node placement.
- No LYK5 node in gocams/index.tsv.

## Project relevance (PLANT_FUNGAL_INTERACTIONS Q2, Q4)
- No leakage of effector or symbiont terms. The receptor-side annotations are chitin binding and chitin-response terms only.
- LYK5 has no symbiosis annotations, so no defense/symbiosis conflation arises (Arabidopsis is non-mycorrhizal).
