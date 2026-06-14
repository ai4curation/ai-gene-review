# RCA (Rubisco activase) — Arabidopsis thaliana — Review Notes

UniProt: P10896 (RCA_ARATH), gene At2g39730, TAIR: RCA. 474 aa precursor; transit peptide 1-58; mature chain 59-474. Member of the RuBisCO activase family (AAA+ ATPase). PE 1 (evidence at protein level). PDB 4W5W (X-ray 2.90 Å, residues 59-437).

## Core biology

RCA is a nuclear-encoded, chloroplast stroma-localized AAA+ ATPase chaperone that uses ATP
hydrolysis to remodel the active sites of Rubisco, removing tightly bound inhibitory
sugar-phosphates (RuBP, and in some species 2-carboxyarabinitol-1-phosphate / CA1P), thereby
restoring/maintaining Rubisco carbamylation and carboxylation activity. It is a key
determinant of photosynthetic induction kinetics and of the thermal sensitivity of
photosynthesis.

UniProt FUNCTION: "Activation of RuBisCO (ribulose-1,5-bisphosphate carboxylase/oxygenase;
EC 4.1.1.39) involves the ATP-dependent carboxylation of the epsilon-amino group of lysine
leading to a carbamate structure." [UniProt P10896]

UniProt SUBCELLULAR LOCATION: "Plastid, chloroplast stroma. Plastid, chloroplast,
plastoglobule {ECO:0000269|PubMed:16461379}." [UniProt P10896]

ATP-binding Walker A / P-loop: BINDING 165..172 ligand ATP (ECO:0000255). [UniProt P10896]

## Alternative splicing / isoforms (alpha = Long; beta = Short)

UniProt ALTERNATIVE PRODUCTS: two isoforms by alternative splicing — Long (P10896-1,
displayed, ~46 kDa "alpha") and Short (P10896-2, VSP_005539, ~43 kDa "beta"), differing only
at the C-terminus. [UniProt P10896; PMID:2535524 "Alternative mRNA splicing generates the two
ribulosebisphosphate carboxylase/oxygenase activase polypeptides in spinach and Arabidopsis"]

## Redox regulation via the alpha (Long) C-terminal extension

[PMID:10430961 Zhang & Portis 1999, full text] "Rubisco activase is a nuclear-encoded
chloroplast protein that is required for the light activation of ribulose 1,5-bisphosphate
carboxylase/oxygenase (Rubisco) in vivo." "in Arabidopsis the larger isoform has a unique
role in the regulation of Rubisco activity. At physiological ratios of ADP/ATP, the 46-kDa
isoform has minimal ATP hydrolysis and Rubisco activation activity in comparison with the
43-kDa isoform." "incubation of the 46-kDa isoform with DTT and thioredoxin-f increased both
activities, whereas incubations with DTT alone or with thioredoxin-m were ineffective.
Thioredoxin-f and DTT had no effect on the 43-kDa isoform." Cys-411 and Cys-392 form the
critical disulfide bond. Conclusion: "Rubisco activase regulates the activity of Rubisco in
response to light-induced changes in both the ADP/ATP ratio and the redox potential via
thioredoxin-f." This supports MF (Rubisco activator activity, ATP hydrolysis) and process
(regulation of photosynthesis / light activation).

[PMID:16822862 Wang & Portis 2006, abstract only] "oxidation of the large (46-kDa) isoform
activase to form a disulfide bond in the C-terminal extension (C-extension) significantly
increases its ADP sensitivity for both ATP hydrolysis and ribulose-1,5-bisphosphate
carboxylase/oxygenase (Rubisco) activation". Demonstrates the C-extension cross-links to the
nucleotide-binding pocket; "the C-extension selectively interferes with the proper binding of
ATP". This is the experimental basis for the TAIR IDA annotations to ATP binding
(GO:0005524), ADP binding (GO:0043531), and Rubisco activator activity (GO:0046863).

## Light / circadian regulation of expression

[PMID:8819320 Liu, Taub & McClung 1996, abstract only] "Transcription of the Arabidopsis
thaliana gene encoding ribulose-1,5-bisphosphate carboxylase/oxygenase (Rubisco) activase
(RCA) is organ-specific, light-responsive, and regulated by the circadian clock." "the light
response is mediated, at least in part, by phytochrome." This is the IEP basis for
response to light stimulus (GO:0009416) — note this is regulation of RCA *gene expression* by
light, i.e. RCA responds to light at the transcript level (acts_upstream_of_or_within is the
GOA qualifier).

## Jasmonate / leaf senescence

[PMID:21173027 Shan et al. 2011, abstract+discussion] RCA identified as a COI1-dependent
JA-repressed protein. "RCA was down-regulated at the levels of transcript and protein
abundance by JA in a COI1-dependent manner. We further found that loss of RCA led to typical
senescence-associated features and that the COI1-dependent JA repression of RCA played an
important role in JA-induced leaf senescence." Supports IEP response to jasmonic acid
(GO:0009753) and IMP leaf senescence (GO:0010150). These are downstream physiological roles
tied to RCA's effect on photosynthetic capacity, not RCA's core molecular function — keep as
non-core.

## Cold

[PMID:16923014 Goulas et al. 2006, abstract only] Proteomic (DIGE) study of chloroplast
stroma/lumen proteome changes during cold acclimation at 5 °C; RCA among differentially
displayed photosynthesis-related stromal proteins. Supports response to cold (GO:0009409, IEP)
as a non-core abundance-change observation. NOTE: this same PMID is also cited in GOA as the
source for the stromule (GO:0010319) IDA annotation — the abstract describes a stromal/lumen
proteomics study and does not mention stromules, so the stromule provenance is questionable;
treated as UNDECIDED (cannot verify supporting evidence; do not REMOVE an experimental-coded
annotation).

## mRNA binding (moonlighting?)

[PMID:32344669 Bach-Pages et al. 2020, full text] Improved plant RNA interactome capture
(ptRIC) in Arabidopsis leaves identified 717 RBPs; "a large number of proteins related to
photosynthesis associate with RNA in vivo". RCA is among metabolic/photosynthetic enzymes
captured as RNA-binding without a canonical RNA-binding domain. This is a proteome-wide
moonlighting/unconventional observation; not a core function. Keep as non-core (IDA on a
single specific moonlighting assay), do not elevate.

## Localization annotations (proteomics)

Numerous HDA localization annotations from large-scale chloroplast/organelle proteomics:
chloroplast stroma (GO:0009570, multiple), chloroplast (GO:0009507), thylakoid /
thylakoid membrane (GO:0009579, GO:0009535), chloroplast envelope (GO:0009941), plastoglobule
(GO:0010287, UniProt-validated ECO:0000269|PubMed:16461379). These are all consistent with an
abundant stromal protein that co-fractionates with multiple chloroplast sub-compartments.
Chloroplast stroma is the authentic primary location (ACCEPT as core location).

Several HDA annotations place RCA outside the chloroplast: plant-type cell wall (GO:0009505,
PMID:16287169), apoplast (GO:0048046, PMID:18538804), nucleus (GO:0005634, PMID:14617066),
Golgi apparatus (GO:0005794, PMID:28887381). RCA is one of the most abundant soluble leaf
proteins and is a near-ubiquitous contaminant of subcellular proteomics fractions; these
extra-plastidial localizations are best interpreted as abundant-protein contamination /
over-annotation rather than bona fide localizations. Marked MARK_AS_OVER_ANNOTATED (kept,
flagged) rather than REMOVE because they are experimentally coded HDA annotations whose full
data we have not inspected.

## EC / family

UniProt SIMILARITY: "Belongs to the RuBisCO activase family." InterPro: IPR044960 RCA-like,
IPR048571 RuBisCO_activase_AAA_helical, AAA core (PF00004), P-loop NTPase. Gene3D
3.40.50.300 (P-loop NTPase) + 1.10.8.1070. BRENDA 6.3.4.B4. Confirms AAA+ ATPase architecture.

## Decisions summary

Core MF: ATP binding (GO:0005524), ATP hydrolysis activity (GO:0016887), Rubisco activator
activity (GO:0046863). Core CC: chloroplast stroma (GO:0009570). Core/relevant process: the
Rubisco activator activity term itself captures the photosynthetic role; no curated specific
"regulation of photosynthesis" BP annotation exists in GOA, so suggested as a proposed term
consideration only.

enzyme regulator activity (GO:0030234) is a generic parent of the specific Rubisco activator
activity term — MODIFY to the specific child GO:0046863.

ADP binding (GO:0043531): experimentally supported (PMID:16822862), reflects nucleotide
exchange / inhibition; KEEP_AS_NON_CORE (real but a facet of the ATPase cycle, not the
headline function).
