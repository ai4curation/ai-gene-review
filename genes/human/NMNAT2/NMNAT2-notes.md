# NMNAT2 (human) — review notes

UniProt: Q9BZQ4 (NMNA2_HUMAN), gene NMNAT2 (HGNC:16789), 307 aa, chromosome 1q25.
Synonyms: C1orf15, KIAA0479. EC 2.7.7.1 and EC 2.7.7.18.

## Core identity

NMNAT2 is one of three human nicotinamide/nicotinate mononucleotide adenylyltransferase
isoforms (NMNAT1 nuclear, NMNAT2 Golgi/cytosolic, NMNAT3 mitochondrial). It catalyzes the
central, rate-committing adenylyl-transfer step of NAD+ biosynthesis, common to both the
salvage and de novo routes:
- NMN + ATP -> NAD+ + PPi (EC 2.7.7.1, GO:0000309)
- NaMN + ATP -> NaAD (deamido-NAD+) + PPi (EC 2.7.7.18, GO:0004515)

The UniProt record names it "Nicotinamide/nicotinic acid mononucleotide adenylyltransferase 2"
with both EC numbers experimentally supported [file:human/NMNAT2/NMNAT2-uniprot.txt "EC=2.7.7.1 {ECO:0000269|PubMed:16118205, ECO:0000269|PubMed:17402747}"].

The functional summary in UniProt:
[file:human/NMNAT2/NMNAT2-uniprot.txt "Nicotinamide/nicotinate-nucleotide adenylyltransferase that acts as an axon maintenance factor"]
and
[file:human/NMNAT2/NMNAT2-uniprot.txt "Catalyzes the formation of NAD(+) from nicotinamide mononucleotide (NMN) and ATP"]
plus lower-efficiency use of the deamidated substrate
[file:human/NMNAT2/NMNAT2-uniprot.txt "Can also use the deamidated form; nicotinic acid mononucleotide (NaMN) as substrate but with a lower efficiency"].

## Catalytic evidence (PMID:16118205, PMID:17402747)

Both are abstract-only in the local cache (`full_text_available: false`), but they are the
ECO:0000269 experimental references cited by UniProt for EC 2.7.7.1/2.7.7.18 and for the
Golgi/cytoplasm localization. UniProt attributes FUNCTION, CATALYTIC ACTIVITY,
BIOPHYSICOCHEMICAL PROPERTIES, SUBSTRATE SPECIFICITY and SUBCELLULAR LOCATION to
PubMed:16118205, and FUNCTION, CATALYTIC ACTIVITY, ACTIVITY REGULATION and COFACTOR to
PubMed:17402747 [file:human/NMNAT2/NMNAT2-uniprot.txt "RP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, SUBSTRATE"].

Berger et al. 2005 (PMID:16118205) abstract: "Nicotinamide mononucleotide adenylyltransferase
(NMNAT) is the central enzyme of the NAD biosynthetic pathway" and localized NMNAT2 "to the
Golgi complex" [PMID:16118205 "NMNAT2 and -3 were localized to the Golgi complex and the mitochondria, respectively"].

Sorci et al. 2007 (PMID:17402747) abstract: gives kinetic mechanism and confirms NMNAT2 as a
Golgi apparatus isozyme of NMNAT (EC 2.7.7.1) [PMID:17402747 "Golgi apparatus NMNAT2"]; NMNH
conversion by NMNAT2 is "much slower" and TrMP is not a substrate for NMNAT2, consistent with
UniProt's "Cannot use triazofurin monophosphate (TrMP) as substrate".

KM values (UniProt, from PMID:16118205/17402747): NMN 32 uM, NaMN 14.5 uM, ATP 204 uM;
Mg2+ is the preferred cofactor; monomeric active form; pH optimum 6.0–9.0.

## Subcellular location

UniProt SUBCELLULAR LOCATION: Golgi apparatus membrane (lipid-anchor), cytoplasmic vesicle
membrane (lipid-anchor), cytoplasm, and cell projection/axon
[file:human/NMNAT2/NMNAT2-uniprot.txt "SUBCELLULAR LOCATION: Golgi apparatus membrane"].
Delivered to axons with Golgi-derived cytoplasmic vesicles
[file:human/NMNAT2/NMNAT2-uniprot.txt "Delivered to axons with Golgi-"].
Palmitoylation (Cys164/Cys165) is required for membrane association
[file:human/NMNAT2/NMNAT2-uniprot.txt "Palmitoylated; palmitoylation is required for membrane"].
Cytosolic localization is also supported by HPA immunofluorescence (GOA IDA, GO_REF:0000052,
GO:0005829). The axon and cytoplasmic-vesicle-membrane C annotations are By-similarity/ISS to
mouse Q8BNJ3, consistent with the axonal-transport biology.

## Axon maintenance / survival factor

This is the best-known physiological role of NMNAT2 and is central, not incidental. UniProt:
"Axon survival factor required for the maintenance of healthy axons: acts by delaying Wallerian
axon degeneration" [file:human/NMNAT2/NMNAT2-uniprot.txt "Axon survival"]. NMNAT2 is a labile
protein whose continuous replenishment from the soma maintains axonal NAD+ and keeps the
pro-degenerative NADase SARM1 inactive; when NMNAT2 is depleted, NMN accumulates, SARM1 is
activated, and Wallerian-type axon degeneration ensues.

Gilley, Mayer, Yu & Coleman 2019 (PMID:30304512), abstract-only in cache, is the ISS source
reference for GO:0061564 (axon development). Abstract: "Nicotinamide mononucleotide
adenylyltransferase 2 (NMNAT2) is an endogenous axon maintenance factor that preserves axon
health by blocking Wallerian-like axon degeneration" [PMID:30304512 "an endogenous axon
maintenance factor that preserves axon health by blocking Wallerian-like axon degeneration"];
"Mice lacking NMNAT2 die at birth with severe axon defects" [PMID:30304512 "Mice lacking NMNAT2
die at birth with severe axon defects"]; reduced levels "compromises the development of
peripheral axons and increases their vulnerability to stresses" [PMID:30304512 "compromises the
development of peripheral axons"].

Turnover: NMNAT2 is degraded after neurite injury via polyubiquitination by the MYCBP2 (PHR/PAM)
E3 ligase after recognition by FBXO45 [file:human/NMNAT2/NMNAT2-uniprot.txt "Degradation is
caused by polyubiquitination by MYCBP2 after recognition"] (PMID:29643511, PMID:29997255).

Disease: biallelic loss-of-function NMNAT2 variants cause a childhood-onset polyneuropathy with
erythromelalgia / skeletal abnormalities (not in cached publications; consistent with the axon-
maintenance role). Recorded as a suggested-question / disease context, not annotated here.

## PARP16 adaptor / translation role (PMID:34314702, full text available)

Challa et al. 2021 (Cell) is the IDA source for two annotations:
- GO:0140768 protein ADP-ribosyltransferase-substrate adaptor activity
- GO:2000766 negative regulation of cytoplasmic translation

Full text supports both. NMNAT2 supplies cytosolic NAD+ that "supports the catalytic activity of
the mono(ADP-ribosyl) transferase (MART) PARP-16, which mono(ADP-ribosyl)ates (MARylates)
ribosomal proteins" [PMID:34314702 "NMNAT-2 supports the catalytic activity of the mono(ADP-ribosyl)
transferase (MART) PARP-16, which mono(ADP-ribosyl)ates (MARylates) ribosomal proteins"]. NMNAT2
and PARP-16 physically interact and "only wild-type and not catalytically dead mutant NMNAT-2
(W92G) enhances PARP-16 auto-MARylation" [PMID:34314702 "only wild-type and not catalytically
dead mutant NMNAT-2 (W92G) enhances PARP-16 auto-MARylation"]. Functionally, "NMNAT-2, which
supports ribosomal protein MARylation, acts to inhibit protein synthesis in a manner that
depends on its catalytic activity" [PMID:34314702 "acts to inhibit protein synthesis in a manner
that depends on its catalytic activity"].

Note on GO:0140768: the effect is mediated through NAD+ production feeding PARP16 (catalytic-
activity dependent, W92G-sensitive), plus a direct NMNAT2–PARP16 interaction. This is a
context-specific (ovarian cancer / high-PARP16) moonlighting activity, not the core evolved
function; the primary MF remains the NMN/NaMN adenylyltransferase. Both annotations are
experimental IDA and are KEPT (non-core). Retained per policy (do not REMOVE experimental
annotations); marked KEEP_AS_NON_CORE.

## Annotation-by-annotation disposition (summary)

Core MF (adenylyltransferase): GO:0000309 and GO:0004515.
Core BP: GO:0009435 NAD+ biosynthetic process (and salvage-route child GO:0034355).
Core location: Golgi apparatus / Golgi membrane / cytosol.
Non-core but genuine: axon development (GO:0061564), axon/cytoplasmic-vesicle-membrane location,
PARP16 adaptor (GO:0140768), negative regulation of cytoplasmic translation (GO:2000766),
nucleotide biosynthetic process (GO:0009165, general parent).
Over-annotated / too-general: GO:0003824 catalytic activity (IEA, root-level MF).

## Term label verifications (OLS, 2026-07)

- GO:0000309 nicotinamide-nucleotide adenylyltransferase activity — current, matches.
- GO:0004515 nicotinate-nucleotide adenylyltransferase activity — current, matches.
- GO:0009435 NAD+ biosynthetic process — current.
- GO:0034355 NAD+ biosynthetic process via the salvage pathway — current.
- GO:0061564 axon development — current (covers axonogenesis + axon regeneration).
- GO:2000766 negative regulation of cytoplasmic translation — current.
- GO:0140768 protein ADP-ribosyltransferase-substrate adaptor activity — current.
- GO:0005794 Golgi apparatus / GO:0000139 Golgi membrane — current.
