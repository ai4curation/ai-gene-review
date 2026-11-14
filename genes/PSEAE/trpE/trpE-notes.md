# trpE (PA0609, P20580) review notes

## Literature summary

- P. aeruginosa has two anthranilate synthases; trpE/trpG make the tryptophan enzyme [PMID:2153661 "its genes are designated trpE and trpG"], and chromosomal trpE deletion gives [PMID:2153661 "This resulted in\ntryptophan auxotrophy"].
- TrpEG is the tryptophan anthranilate synthase, PhnAB the pyocyanin one [PMID:23449919 "P. aeruginosa\npossesses two functional anthranilate synthases, TrpEG and PhnAB"]; [PMID:23449919 "trpEG mutants are tryptophan\nauxotrophs but produce PQS"].
- Anthranilate synthase catalyses the first step shared by tryptophan and PQS synthesis [PMID:23449919 "PQS biosynthesis requires conversion of the\ncentral metabolite chorismate to anthranilate by anthranilate synthase"; "This reaction is also the first step in tryptophan biosynthesis"].
- UniProt: reaction chorismate + L-glutamine = anthranilate + pyruvate + L-glutamate (RHEA:21732, EC 4.1.3.27); heterotetramer of TrpE and TrpG; anthranilate synthase component I family.

Literature search (2026-11-05): PubMed MCP and NCBI E-utilities failed all session; Europe PMC search was
intermittent. Based on PMID:2153661 (abstract) and PMID:23449919 (full text, cached), the UniProt record, and
QuickGO for the seeds.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002599563 | GO:0000162 L-tryptophan biosynthetic process | 8 | 182 (95 taxa) | GO:0000162, IMP, PMID:2153661 | SOUND | Chromosomal trpE knockout is a tryptophan auxotroph; trpE is explicitly the tryptophan (not pyocyanin) anthranilate synthase. | B. subtilis TrpE P00895 (IDA PMID:4886289, IMP PMID:5331787), S. cerevisiae TRP2 (SGD S000000892), S. pombe SPCC1442.09, Arabidopsis AT5G05730, M. tuberculosis P9WFX3, and plant/other UniProt Q94GF1, Q9XJ29 | Yes; a deeply conserved node with multiple experimental seeds (e.g. B. subtilis TrpE IDA, QuickGO 2026-11-05) |

No `source_defects`: the PseudoCAP row is sound and the IBD is sound for this broad, well-characterised enzyme
family. Only two trpE rows are PseudoCAP (both from PMID:2153661); the GO:0004049 IMP row is genetic rather than a
direct enzyme assay but the activity assignment is correct, so it is accepted (not flagged).

## Action summary

5 rows, all ACCEPT (GO:0000162 IBA/IEA/IMP; GO:0004049 IEA/IMP).
