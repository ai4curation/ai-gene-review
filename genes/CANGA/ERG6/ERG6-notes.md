# ERG6 notes

## PubMed and PAINT re-review, 2026-11-21

PTHR44068 places the conserved sterol-SMT activity on `PTN002226525`, the
fungal ergosterol-biosynthesis process on `PTN000802684`, broad sterol
biosynthesis and ER localization on `PTN002226525`, and generic
methyltransferase activity at the family root. `CANGA/ERG6` is not currently in
the GO-Central PANTHER IBA rows, but Q6FRZ7 is a `PTHR44068:SF1` fungal
Erg6/SMT member in the PANTHER member file.

The seed C. glabrata paper is Vandeputte et al. 2008. It found a clinical
isolate whose reduced ergosterol and reduced polyene susceptibility tracked to a
nonsense mutation in `ERG6`, then complemented the isolate with wild-type
`ERG6`, restoring wild-type amphotericin B susceptibility, cell-wall stress
resistance, growth, viability, and fitness [PMID:18694952, "The nonsense
mutation detected in the ERG6 gene of this isolate led to a decrease in
ergosterol content."].

I searched PubMed for `(ERG6 OR CgERG6) AND (Candida glabrata OR Nakaseomyces
glabratus)` and found 15 hits. Direct ERG6 hits after the GOA's 2008 paper
include 2019 clinical ERG2/ERG6 amphotericin-resistance profiling
[PMID:30455247], a 2022 abstract-only deletion study reporting altered
ergosterol, antifungal susceptibility, membrane fluidity, and cell-wall
integrity [PMID:36047961, "reduced content of ergosterol in the Cgerg6 deletion
mutant"], the 2023 oxidative-stress/iron-homeostasis deletion paper
[PMID:37233290, "Here, we show that the Cgerg6Δ mutant displays increased
susceptibility to oxidative stress inducing agents"], two September 2024
deletion papers on weak-acid and catechin/azole phenotypes [PMID:39452621,
"loss of the CgERG6 gene resulted in increased sensitivity to cycloheximide and
4-nitroquinoline-N-oxide (4-NQO)"; PMID:39452706], and the 2025 GOA-cited
membrane-composition paper [PMID:39477913, "Our findings revealed a depletion
of ergosterol, increased zymosterol and eburicol content"]. The 2025 Osh2 paper
mentions ERG6 only as a contextual sterol step and did not change this review.

The CGD GOA table still has a cellular_component ND placeholder; ER and
lipid-droplet locations are currently inferred from fungal Erg6 orthology, and
the 2022-2025 C. glabrata ERG6 papers checked here did not test CgErg6
subcellular localization directly.

The CGD `PMID:39477913` rows to plasma membrane raft polarization and cellular
response to xenobiotic stimulus are useful phenotypic signposts but not the
core pathway work of Erg6. The 2025 paper measured sterol/phospholipid
composition, transmembrane potential, and myriocin/aureobasidin sensitivity
after ERG6 deletion; the 2024 cycloheximide/4-NQO/weak-acid paper makes the
downstream membrane-efflux interpretation explicit. Erg6 supplies the C-24
methylated sterol pool and does not itself execute plasma-membrane raft
polarization or xenobiotic response.
