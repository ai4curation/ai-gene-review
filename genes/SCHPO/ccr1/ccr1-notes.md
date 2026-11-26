# ccr1 (SPBC29A10.01; UniProt P36587) notes

Fetched accession verified: `AC   P36587` (NCPR_SCHPO, 678 aa) [UniProt:P36587].

## Identity and domain architecture
- NADPH--cytochrome P450 reductase, EC 1.6.2.4; HAMAP MF_03212 family rule [UniProt:P36587 "This enzyme is required for electron transfer from NADP to cytochrome P450 in microsomes"].
- Flavodoxin (FMN) N-terminal module + FNR-like FAD/NADPH C-terminal module; PANTHER PTHR19384:SF17 (NADPH--CYTOCHROME P450 REDUCTASE) [UniProt:P36587].
- Location by rule: ER membrane, single-pass, cytoplasmic side; HAMAP also lists mitochondrial outer membrane and cell membrane (these derive from the S. cerevisiae Ncp1 template, not from S. pombe data) [UniProt:P36587].
- Genome-wide YFP localisation (Matsuyama 2006, HDA) places Ccr1 at the ER (PomBase GOA row GO:0005783 HDA PMID:16823372). Abstract-only in cache.

## S. pombe experimental evidence
- Liu et al. 2020 (PMID:32571823, full text): ccr1/cls1 isolated in a clotrimazole-hypersensitivity screen; deletion hypersensitive to azoles, terbinafine and fenpropimorph [PMID:32571823 "the Δ ccr1 cells exhibited hypersensitivity to all these drugs"]. Clotrimazole acts on erg11 (CYP51) [PMID:32571823 "which functions by disrupting ergosterol biosynthesis through inhibition of the cytochrome P450-dependent enzyme lanosterol 14-α-demethylase"].
- Same paper measures microsomal NADPH-cytochrome c reductase activity attributed to Ccr1 and its inhibition by tamoxifen [PMID:32571823 "the results showed that TAM inhibited NADPH-cytochrome P450 reductase activities in a dose-dependent manner"].
- Pleiotropic phenotypes (cell wall integrity, vacuole fusion, Ca2+/calcineurin) are downstream consequences, not separate activities [PMID:32571823 "Ccr1 and calcineurin are required in parallel for the regulation of cell wall integrity"].
- Neunzig et al. 2013 (PMID:23737303, abstract only): coexpressed ccr1 supports human microsomal CYPs in S. pombe [PMID:23737303 "CYP2D6 displayed its highest activity when coexpressed with ccr1"]. Basis of PomBase IMP for GO:0003958 and of the GO-CAM edge ccr1 -> erg11.
- PomBase: deletion viable; phenotypes include sensitivity to clotrimazole, fluconazole, terbinafine (PomBase gene page API, accessed 2026-10-06).

## Ortholog consistency
- S. cerevisiae NCP1 review core function: GO:0003958 / GO:0006696 / ER membrane. Same here; no S. pombe-specific difference.
- NCP1 review REMOVEd the IBA cytosol row (soluble diflavin-reductase subfamilies); same reasoning applies to Ccr1, which has a TM anchor.

## GO-CAM (gomodel:66c7d41500002088)
- Activity 66c7d41500002387: ccr1 enables GO:0003958, occurs_in ER membrane, part_of ergosterol biosynthesis, RO:0002629 (directly positively regulates) erg11 only.
- Module (ergosterol_biosynthesis) gives ncp1_activity PROVIDES_INPUT_FOR erg1, erg11 and erg5; the PomBase model only links to erg11. Not a contradiction, just less complete; electron supply to erg5 (CYP61) and erg1 is homology-inferred.
