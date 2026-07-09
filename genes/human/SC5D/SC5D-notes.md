# SC5D (Lathosterol oxidase / sterol-C5-desaturase) — review notes

UniProtKB: O75845 (SC5D_HUMAN), 299 aa. HGNC:10547. EC 1.14.19.20.

## Function (verified)

SC5D is **lathosterol oxidase / sterol-C5(6)-desaturase**, a non-heme-iron,
multi-pass endoplasmic-reticulum-membrane oxidoreductase that introduces the
C5–6 double bond into lathosterol, producing 7-dehydrocholesterol (7-DHC). This
is the **penultimate step** of cholesterol biosynthesis (Kandutsch–Russell arm),
immediately upstream of DHCR7 which reduces 7-DHC to cholesterol.

- UniProt FUNCTION: "Catalyzes the penultimate step of the biosynthesis of
  cholesterol, the dehydrogenation of lathosterol into 7-dehydrocholesterol
  (7-DHC)" [file:human/SC5D/SC5D-uniprot.txt]. EC=1.14.19.20; belongs to the
  sterol desaturase family.
- Catalytic activity uses Fe(II)/Fe(III)-[cytochrome b5] and O2 (two-electron
  desaturation). Cofactor: Fe cation. Three histidine-box motifs (138–143,
  151–155, 228–233) form the di-iron active site.
- Topology: multi-pass membrane protein (4 predicted TM helices), ER membrane.

## Reaction (RHEA / ChEBI)
lathosterol + 2 Fe(II)-[cyt b5] + O2 + 2 H+ = 7-dehydrocholesterol + 2 Fe(III)-[cyt b5] + 2 H2O (RHEA:46556; EC 1.14.19.20).
Also acts on 5α-cholesta-7,24-dien-3β-ol → 7-dehydrodesmosterol (RHEA:47184; Bloch-arm intermediate).

## Key references (all cached, abstract-only unless noted)
- [PMID:10786622] Nishi et al. 2000 — cloned human+mouse SC5D cDNA; yeast-mutant
  functional complementation; "an enzyme that catalyzes the dehydrogenation to
  introduce C5-6 double bond into lathosterol in cholesterol biosynthesis ...
  Mammalian SC5D was presumed as an integral membrane protein". Source of
  RecName, EC, and ER subcellular location; UniProt IDA basis.
- [PMID:12189593] Brunetti-Pierri et al. 2002 — first human lathosterolosis
  patient; block in conversion of lathosterol → 7-DHC; SC5D activity deficient;
  R29Q + G211D. "novel defect of cholesterol biosynthesis."
- [PMID:12812989] Krakowiak et al. 2003 — Sc5d−/− mouse (stillborn, elevated
  lathosterol, decreased cholesterol, cleft palate/micrognathia/limb defects,
  hedgehog-signalling phenotype) + human Y46S patient. "Lathosterol 5-desaturase
  catalyzes the conversion of lathosterol to 7-dehydrocholesterol in the next to
  last step of cholesterol synthesis."
- [PMID:38297129] Freitas et al. 2024 (Nature) — 7-DHC is an endogenous
  suppressor of ferroptosis (via DHCR7 axis); confirms SC5D FUNCTION/CATALYTIC
  ACTIVITY/PATHWAY in UniProt. Abstract-only in cache.
- [PMID:38297130] Li et al. 2024 (Nature) — FULL TEXT cached. Genome-wide CRISPR
  screen: SC5D (with MSMO1/CYP51A1/EBP) is an anti-ferroptotic distal-CB gene;
  SC5D KO increases ferroptosis susceptibility, rescued by SC5D re-expression;
  SC5D deletion lowers 7-DHC. Supports GO:0110076 negative regulation of
  ferroptosis (IMP) and the "7-DHC synthesized by SC5D" statement.

## Disease
Lathosterolosis (LATHOS, MIM:607330): autosomal recessive; elevated lathosterol;
SLOS-like multiple-malformation / dysmorphism syndrome with liver disease and
lysosomal storage. Caused by SC5D variants.

## Annotation strategy
- Core MF: GO:0000248 C-5 sterol desaturase activity + GO:0050046 delta7-sterol
  5(6)-desaturase activity (both accurate; 0050046 is the precise reaction).
- Core BP: cholesterol biosynthesis. GOA carries generic GO:0006695. UniProt DR
  also carries the more specific GO:0033490 (cholesterol biosynthetic process via
  lathosterol) IDA — a legitimate MODIFY target for the PMID:10786622 IDA, but
  I keep GOA ids and note this; core_functions uses GO:0006695.
- Core CC: GO:0005789 endoplasmic reticulum membrane.
- GO:0005506 iron ion binding (IEA/InterPro): ACCEPT — di-iron/His-box enzyme,
  cofactor Fe confirmed by UniProt.
- GO:0008610 lipid biosynthetic process (IEA): broad parent of cholesterol
  biosynthesis; ACCEPT as correct-but-general.
- GO:0110076 negative regulation of ferroptosis (IMP x2): ACCEPT but non-core —
  indirect, via 7-DHC product; secondary/moonlighting-adjacent role.
