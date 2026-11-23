# SLC34A1 (NaPi-IIa / NaPi-2a) curation notes

## Identity
UniProt Q06495, "Sodium-dependent phosphate transport protein 2A"; HGNC SLC34A1. SLC34 (type II NaPi) family, PANTHER PTHR10010; multi-pass apical membrane protein.

## Core transport function
Renal apical Na-coupled inorganic-phosphate cotransporter: [file:human/SLC34A1/SLC34A1-uniprot.txt CC:FUNCTION "Involved in actively transporting phosphate into cells via" Na+ cotransport in the renal brush border; "a Na(+):Pi stoichiometry of 3:1 and is electrogenic"; ECO:0000269 PubMed:12324554/20335586/26047794/8327470; KM=0.17 mM]. Catalytic reaction 3 Na+(out) + phosphate(out) = 3 Na+(in) + phosphate(in). Core MF GO:0005436; core BP GO:0035435 / GO:0044341 (Na-dependent) and GO:0055062 phosphate ion homeostasis (IDA x3; NaPi-IIa sets systemic phosphate via renal reabsorption).

## Location and regulated trafficking
Apical brush-border membrane of proximal-tubule cells [CC:SUBCELLULAR LOCATION "Apical cell membrane"; "Localized at the brush border" membranes of the proximal tubules]. Core locations GO:0005886 + GO:0016324 apical (apical IS where NaPi-IIa acts, unlike the non-polarized sites of PiT2). Hormonally regulated: PTH and FGF23 trigger internalization/degradation (-> GO:0005768 endosome, GO:0031982 vesicle KEEP_AS_NON_CORE); dietary phosphate restriction increases it. Apical retention depends on the C-terminal PDZ motif binding NHERF1/PDZK1/MPDZ [CC:SUBUNIT "Interacts with NHERF1"] -> GO:0030165 PDZ domain binding ACCEPT.

## Disease
Loss-of-function: hypophosphatemic nephrolithiasis/osteoporosis, infantile hypercalcemia, Fanconi renotubular syndrome.

## The IEA response-to-X cluster (all Ensembl-Compara ortholog projections, GO_REF:0000107)
Kept as non-core regulatory responses where NaPi-IIa regulation is established (rodent ortholog + conserved physiology): parathyroid hormone (GO:0071374/GO:0071107; PTH-induced internalization is curated), dietary phosphate (GO:0016036 phosphate starvation, GO:0007584 nutrient), estradiol, growth hormone, thyroid hormone, peptide hormone/peptide (PTH/FGF23), cellular response to metal ion, plus the IDA heavy-metal responses (cadmium/lead/mercury, PMID:8898024, inhibit renal NaPi transport). Marked over-annotated where no NaPi-IIa-specific mechanism exists or the aspect is wrong: staurosporine, potassium, magnesium, vitamin A (vitamin D - not A - regulates NaPi-IIa), xenobiotic stimulus, dentinogenesis, kidney development (mature-function transporter, not a developmental role), tricarboxylic acid metabolic process (wrong aspect), ossification (distal systemic consequence; participation-test fail). Self-referential GO:2000120/GO:2000187 (a transporter regulating its own transport) MARK_AS_OVER_ANNOTATED. Bare GO:0005515 protein binding (IPI x2) REMOVE per policy (informative binding captured by the PDZ row). GO:0016020 membrane MODIFY->plasma membrane; GO:0006817 broad phosphate transport KEEP_AS_NON_CORE; arsenate transport (Pi mimic) KEEP_AS_NON_CORE. Batch 27.
