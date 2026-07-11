# DHCR7 (Q9UBM7) review notes

## Identity and core function
DHCR7 = 7-dehydrocholesterol reductase (7-DHC reductase; Delta7-sterol reductase; EC 1.3.1.21),
the ER-membrane enzyme catalysing the FINAL step of the Kandutsch-Russell arm of cholesterol
biosynthesis: NADPH-dependent reduction of the C7-C8 double bond of 7-dehydrocholesterol (7-DHC)
to cholesterol.

- Cloning/expression + catalytic activity: [PMID:9465114 "The Delta7-sterol reductase is the
  ultimate enzyme of cholesterol biosynthesis in vertebrates and is absent from yeast."] and
  [PMID:9465114 "Microsomes from Saccharomyces cerevisiae strains heterologously expressing the
  human cDNA remove the C7-8 double bond in 7-dehydrocholesterol."]; "The conversion to
  cholesterol depends on NADPH".
- UniProt FUNCTION: "Oxidoreductase that catalyzes the last step of the cholesterol synthesis
  pathway, which transforms cholesta-5,7-dien-3beta-ol (7-dehydrocholesterol,7-DHC) into
  cholesterol by reducing the C7-C8 double bond of its sterol core".
- CATALYTIC ACTIVITY (Rhea:RHEA:23984): cholesterol + NADP(+) = 7-dehydrocholesterol + NADPH +
  H(+); EC=1.3.1.21. Physiological direction right-to-left (i.e., 7-DHC -> cholesterol).
- Correct MF term = GO:0047598 7-dehydrocholesterol reductase activity (NOT GO:0047750; GOA uses
  0047598 throughout). QuickGO confirms GO:0047598 label + non-obsolete.

7-DHC is also the precursor of vitamin D3, so DHCR7 partitions 7-DHC between cholesterol and
vitamin D synthesis [PMID:25637936 "DHCR7 is important for both cholesterol and vitamin D
synthesis"; "as 7DHC can be converted into cholesterol or vitamin D, DHCR7 represents a switch
between these vital molecules in skin cells exposed to UVB"].

## Localization
ER membrane, multi-pass. [PMID:9878250 "these two related proteins are in the endoplasmic
reticulum"]. UniProt SUBCELLULAR LOCATION: Endoplasmic reticulum membrane; Multi-pass membrane
protein. HPA IDA -> ER. IDA PMID:9878250 also assigns nuclear outer membrane (contiguous with
ER/nuclear envelope) and ER. 7 predicted TM helices. Note GO:0005640 nuclear outer membrane is
part of ER envelope continuum — plausible but non-core.

## DHCR24 / TMEM147 interactions
- Interacts physically+functionally with DHCR24 (Q15392), the other terminal reductase; DHCR24
  knockdown ablates DHCR7 activity [PMID:25637936 "24-Dehydrocholesterol reductase (DHCR24) and
  7-dehydrocholesterol reductase (DHCR7) coimmunoprecipitate, and when the DHCR24 gene is knocked
  down by siRNA, DHCR7 activity is also ablated."]. IPI to Q15392 is DHCR24 -> keep as
  interaction, but bare 'protein binding' is uninformative; MARK_AS_OVER_ANNOTATED.
- Interacts with TMEM147 (Q9BVK8) [PMID:32694168 "TMEM147 also physically interacts with the key
  sterol reductase DHCR7"]. IPI 'protein binding' -> MARK_AS_OVER_ANNOTATED.

## Cholesterol-5,6-oxide hydrolase (ChEH) / AEBS — GO:0033963
IMP PMID:20615952: DHCR7 + EBP (D8D7I) together reconstitute cholesterol-5,6-epoxide hydrolase
(ChEH) activity of the microsomal antiestrogen binding site (AEBS). This is a genuine, curated,
experimentally-supported second activity of DHCR7 as part of a heterodimeric AEBS complex — NOT
a spurious wrong-branch IEA. UniProt records it (AltName "Cholesterol-5,6-epoxide hydrolase
subunit DHCR7", EC 3.3.2.11) with IMP-level evidence. It is a moonlighting/complex activity, not
the core reductase function; KEEP_AS_NON_CORE (do not REMOVE an experimental annotation). The
task framing warned of an "incorrect ChEH IEA" but this specific annotation is IMP/experimental
and its full text supports it — treat accordingly.

## Ferroptosis — GO:0160020 positive regulation of ferroptosis
Two 2024 Nature papers (IMP): DHCR7 is pro-ferroptotic because it consumes the anti-ferroptotic
metabolite 7-DHC. [PMID:38297129 "we identify proferroptotic activity of 7-dehydrocholesterol
reductase (DHCR7) and an unexpected prosurvival function of its substrate, 7-dehydrocholesterol
(7-DHC)"]. [PMID:38297130 "DHCR7 functions as a pro-ferroptotic gene"]. Real, experimentally
supported regulatory role (via depleting a radical-trapping sterol); non-core relative to the
biosynthetic function. KEEP_AS_NON_CORE.

## Disease
SLOS (Smith-Lemli-Opitz syndrome) — autosomal recessive; elevated 7-DHC, low cholesterol;
microcephaly/2-3 toe syndactyly/developmental delay. Many SLOS missense variants in UniProt;
loss of 7-DHC reductase activity (e.g., T93M, N274K, L306R mutagenesis). Confirms enzyme is the
cause. Background for the enzymatic core function.

## Annotation dispositions (summary)
- GO:0047598 7-DHC reductase activity (IBA/IEA/EXP/IMP x2/IDA): ACCEPT — CORE MF.
- GO:0006695 cholesterol biosynthetic process (IBA/TAS x2/IEA/IMP x3): ACCEPT — CORE BP.
- GO:0005789 ER membrane (IBA is_active_in / IEA / TAS x3): ACCEPT — CORE CC.
- GO:0005783 endoplasmic reticulum (IDA HPA, IDA PMID:9878250): ACCEPT (parent of ER membrane).
- GO:0016126 sterol biosynthetic process (IEA InterPro): ACCEPT (broader parent, correct).
- GO:0016628 oxidoreductase activity CH-CH NAD/NADP (IEA InterPro): MARK_AS_OVER_ANNOTATED —
  correct-branch but too general vs GO:0047598 (MODIFY toward GO:0047598).
- GO:0016020 membrane (IEA InterPro / HDA NK-cell proteome PMID:19946888): too general; ER
  membrane already captured. MARK_AS_OVER_ANNOTATED.
- GO:0050661 NADP binding (ISS): ACCEPT — supported by NADP(+) binding-site features + NADPH-
  dependent catalysis.
- GO:0033963 cholesterol-5,6-oxide hydrolase activity (IMP PMID:20615952): KEEP_AS_NON_CORE.
- GO:0160020 positive regulation of ferroptosis (IMP x2): KEEP_AS_NON_CORE.
- GO:0005515 protein binding (IPI DHCR24, IPI TMEM147): MARK_AS_OVER_ANNOTATED (bare protein
  binding uninformative; real interactions documented in reason).
- GO:0005640 nuclear outer membrane (IDA PMID:9878250): KEEP_AS_NON_CORE (ER/NE continuum).
