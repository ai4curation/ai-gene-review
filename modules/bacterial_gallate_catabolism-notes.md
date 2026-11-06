# Gallate catabolism audit — 2026-11-06

The audit covers gallate ring cleavage, the two chemically distinct OMA-to-CHA routes, terminal CHA cleavage and optional GalP entry. It does not equate growth on gallate with a particular enzyme set, or a shared lower-pathway enzyme with an entire native pathway.

## Comparative literature and scope

Three reviews were searched and read: Masai et al. 2007 ([PMID:17213657](https://pubmed.ncbi.nlm.nih.gov/17213657/)), Kamimura et al. 2017 ([PMID:29052962](https://pubmed.ncbi.nlm.nih.gov/29052962/)), and Lubbers et al. 2019 ([PMID:31075306](https://pubmed.ncbi.nlm.nih.gov/31075306/)). The first publisher PDF and the third author manuscript have independently retrieved text and provenance in the module source-analysis directory. The second was read on the publisher website; its cached PMID remains abstract-only. Module references record individual findings and the limits of each source.

The 2007 synthesis connects the sphingomonad lower pathway to protocatechuate catabolism and describes analogous downstream machinery in Arthrobacter. That comparison supports component homology, not gallate-specific entry outside Pseudomonadota. The model now uses Pseudomonadota as its evidence-backed taxon scope, without making a biological absence claim for other bacteria.

The 2019 comparison is useful for locating fungal alternatives, but two descriptions are unsuitable as mechanistic specifications: it calls GalA/DesB cleavage intradiol and groups LigU with keto-enol tautomerases. The primary studies distinguish extradiol cleavage and the LigU allylic reaction. The 2024 Aspergillus study ([PMID:38064205](https://pubmed.ncbi.nlm.nih.gov/38064205/)) supports a distinct tetrahydroxybenzene route; fungal gallate use alone therefore does not justify adding fungal exemplars here.

## Reactions and family boundaries

Every catalytic leaf carries primary evidence. GalD/GalB and LigU/LigJ remain paired alternatives because their immediate intermediates differ. Broad fold or enzyme-class matches cannot substitute for substrate-specific evidence. GalD and LigU share the PrpF-related family; GalB and LigJ use unrelated folds. The current GO:0047443 definition already covers CHA cleavage, so the archived GalC term proposal is redundant. Its short HMG-based label does not change that definition.

GalB's retained GO:0047584 has keto-OMA wording, whereas its measured immediate substrate is OMA-enol. The curated Rhea reaction and explicit chemical descriptors preserve the distinction. No gene source annotation was rewritten to conceal that ontology mismatch.

The KA1 LigU exemplar is supported directly by [PMID:31339729](https://pubmed.ncbi.nlm.nih.gov/31339729/), whose abstract identifies the organism. A SYK-6-focused paper title was insufficient reason to reject the target assignment. A collection of enzyme exemplars across strains is not proof that one strain expresses the whole modeled route.

## Sampling and evidence limits

Nine inherited reviews span Pseudomonas, Sphingobium and Novosphingobium. Three seeded Burkholderia lata 383 reviews extend the audit to a beta-proteobacterial strain with reported native gallate utilization. The ring-cleavage and terminal-aldolase representatives have the declared family signatures independently of submitter/ARBA function names. The hydratase remains a reviewed boundary candidate because its precise KCH versus OMA-enol activity is unresolved. These partial assignments do not establish a complete molecular route in BURL3.

Transport interpretation distinguishes the adapted KTGAL strain from parental KT2440. The known GalT transporter is adjacent to the chemical module boundary, not an unidentified candidate. GalP contributes to native uptake, but isolated-channel selectivity remains an experimental question. The 2017 transporter review supports this separation.

## Verification in progress

The nine existing reviews preserve 50 annotation payloads, including nine inherited NEW rows. No annotation was added or retired in that panel. The new BURL3 panel has ten seeded rows. Exact source and provider preservation, focused validations and generated histories are recorded in the consultation manifests. The rebuilt family index confirms the declared representatives. All 24 production coverage and boundary cases pass; the chemical oracle and its limits are explicit. Three module conformance advisories concern specific proposed core terms, not missing chemistry. Whole-repository validation and a dedicated PR remain pending.
