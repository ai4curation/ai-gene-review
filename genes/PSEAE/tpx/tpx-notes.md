# tpx (PA2532, P57668) notes

## Literature (own research, 2026-11-05)

Full text of PMID:22609922 cached and read.
- [PMID:22609922 "The enzyme catalyzes thioredoxin-dependent peroxidation and can utilize organic hydroperoxides and H(2)O(2) as substrates."]; coupled TrxA/TrxB/NADPH assay with no activity when either is omitted; Km(app) for H2O2, CHP and BHP measured.
- [PMID:22609922 "The Δ tpx mutant was more than 10-fold more sensitive to 0.5 mM H 2 O 2 than the PAO1 wild type"], complemented in trans; not sensitive at 20 mM.
- PhoA/LacZ fusions: probably cytoplasmic, unlike E. coli Tpx [PMID:22609922 "we conclude that the protein is not secreted to the periplasm via a typical signal sequence"].
- IscR represses tpx; induced by redox-cycling agents and diamide.
- GO:0008379 thioredoxin peroxidase activity is labelled obsolete in current GOA; replaced here by GO:0140824 thioredoxin-dependent peroxiredoxin activity (substrate breadth shown), following the precedent in genes/XANCP/Q8P365.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002454730 | GO:0008379 thioredoxin peroxidase activity | 2 | 32 (30 taxa) | GO:0008379, IDA, PMID:22609922 | SOUND | Purified enzyme assayed with Trx/TrxR/NADPH and three peroxides. | E. coli Tpx P0A862 (GO:0008379 IDA PMID:7499381; GO:0140824 EXP PMID:12514184) | Yes |
| PTN002454730 | GO:0034599 cellular response to oxidative stress | 2 | 32 (30 taxa) | GO:0070301 cellular response to hydrogen peroxide, IMP, PMID:22609922 | SOUND | Deletion mutant H2O2 hypersensitivity with complementation, explained by the gene's own peroxidase activity. | E. coli Tpx P0A862 (GO:0034599 IMP PMID:8824604) | Yes |

No PseudoCAP defects. One GO_CENTRAL defect (OUTDATED_STATEMENT, CONFIRMED): the PTN002454730 IBD uses the now-obsolete GO:0008379; repoint to GO:0140824. The IBD is otherwise sound.

## Action counts

ACCEPT 3, MODIFY 3, TOO_GENERAL 5.
