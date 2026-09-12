# NDUFA2 (Complex I-B8, CI-B8) — Gene Review Notes

UniProt: O43678 (NDUA2_HUMAN). HGNC:7685. Gene ID 4695. Chromosome 5. 99 aa,
~10.9 kDa. Two isoforms (O43678-1 displayed; O43678-2 differs at C-terminus,
VSP_045479). Evidence at protein level (PE 1).

## Identity and family

NDUFA2 is the "NADH dehydrogenase [ubiquinone] 1 alpha subcomplex subunit 2",
also called Complex I-B8 / CI-B8 and the NADH-ubiquinone oxidoreductase B8 subunit
[file:human/NDUFA2/NDUFA2-uniprot.txt, "RecName: Full=NADH dehydrogenase [ubiquinone] 1 alpha subcomplex subunit 2"; "AltName: Full=Complex I-B8"].
It belongs to the "complex I NDUFA2 subunit family"
[file:human/NDUFA2/NDUFA2-uniprot.txt, "Belongs to the complex I NDUFA2 subunit family"].

## Function: accessory (supernumerary), non-catalytic

UniProt states it is an accessory subunit believed NOT to be involved in catalysis:
[file:human/NDUFA2/NDUFA2-uniprot.txt, "Accessory subunit of the mitochondrial membrane respiratory chain NADH dehydrogenase (Complex I), that is believed not to be involved in catalysis. Complex I functions in the transfer of electrons from NADH to the respiratory chain. The immediate electron acceptor for the enzyme is believed to be ubiquinone."].
This FUNCTION statement carries an experimental evidence attribution to
PubMed:27626371 (ECO:0000269).

Complex I is composed of 45 different subunits
[file:human/NDUFA2/NDUFA2-uniprot.txt, "Complex I is composed of 45 different subunits."],
of which 14 core subunits (shared with bacteria) are essential for catalysis; the
remaining 31 are accessory/supernumerary subunits [PMID:27626371 abstract,
"Bacterial and human complex I share 14 core subunits that are essential for
enzymatic function; however, the role and necessity of the remaining 31 human
accessory subunits is unclear."]. Supernumerary subunits "play essential roles in
assembly, regulation and stability" while the core proteins perform catalysis
[PMID:30030361 abstract, "The human enzymes comprise core proteins, performing the
catalytic activities, and a large number of 'supernumerary' subunits that play
essential roles in assembly, regulation and stability."].

Stroud et al. 2016 knocked out each accessory subunit; 25 subunits are strictly
required for assembly of a functional complex [PMID:27626371 abstract, "We show
that 25 subunits are strictly required for assembly of a functional complex and 1
subunit is essential for cell viability."; "loss of each subunit affects the
stability of other subunits residing in the same structural module."]. This is the
experimental basis for the UniProt FUNCTION line and the "part of complex I /
required for assembly and function" framing.

## Structure: thioredoxin-like fold, redox-active disulfide — but no demonstrated redox catalysis

The isolated oxidized B8 subunit adopts a thioredoxin fold (NMR, PDB 1S3A)
[file:human/NDUFA2/NDUFA2-uniprot.txt, "RP   STRUCTURE BY NMR, AND DISULFIDE BOND."
and RT "The oxidized subunit B8 from human complex I adopts a thioredoxin fold."
(Brockmann et al., Structure 2004; PMID:15341729 — abstract not cached locally)].
UniProt records a "Redox-active" disulfide bond between Cys24 and Cys58
[file:human/NDUFA2/NDUFA2-uniprot.txt, "DISULFID        24..58" / "/note=\"Redox-active\""],
and the Gene3D/SUPFAM assignments are Glutaredoxin / Thioredoxin-like
[file:human/NDUFA2/NDUFA2-uniprot.txt, "Gene3D; 3.40.30.10; Glutaredoxin"; "SUPFAM; SSF52833; Thioredoxin-like"].

IMPORTANT: The thioredoxin-like fold and redox-active disulfide are STRUCTURAL /
biophysical observations. UniProt does NOT assert any thioredoxin, oxidoreductase,
disulfide-isomerase, or protein-disulfide redox catalytic activity as the function
of NDUFA2; the FUNCTION line explicitly says it is "believed not to be involved in
catalysis." There is no GO molecular-function annotation in GOA for a redox
activity. Therefore no thioredoxin/oxidoreductase MF should be assigned. The honest
molecular function is structural molecule activity (GO:0005198) as a stable
structural subunit of the holoenzyme, contributing to the complex-level NADH
dehydrogenase (ubiquinone) activity (GO:0008137).

## Localization: peripheral (matrix) arm of Complex I, inner membrane, matrix side

Subcellular location: mitochondrion inner membrane, peripheral membrane protein,
matrix side
[file:human/NDUFA2/NDUFA2-uniprot.txt, "Mitochondrion inner membrane"; "Peripheral membrane protein"; "Matrix side"].
It is part of the peripheral (matrix) arm of Complex I. GOA has experimental
component annotations to respiratory chain complex I (GO:0045271) from
immunopurification/MS (PMID:12611891), assembly-intermediate tracing (PMID:17209039),
knockout proteomics (PMID:27626371), and cryo-EM of the megacomplex (PMID:28844695).

## Assembly-intermediate context (Reactome)

Reactome models NDUFA2 within Complex I biogenesis: peripheral-arm subunits bind
the 815 kDa complex to form a 980 kDa complex; the MCIA complex and NDUFAF2-7
dissociate to yield mature Complex I; and mature Complex I oxidises NADH to NAD+,
reducing CoQ to CoQH2. Reactome also captures LONP1-mediated turnover of
inner-membrane proteins (R-HSA-9837978/9838004) — this is a substrate-of-degradation
relationship, not an NDUFA2 function.

## Disease

Variants cause Mitochondrial complex I deficiency, nuclear type 13 (MC1DN13;
MIM 618235), autosomal recessive, presenting as Leigh disease / leukoencephalopathy
[file:human/NDUFA2/NDUFA2-uniprot.txt, "Mitochondrial complex I deficiency, nuclear type 13 (MC1DN13)"; "INVOLVEMENT IN MC1DN13" from PubMed:18513682, "NDUFA2 complex I mutation leads to Leigh disease."].
This clinically confirms NDUFA2 is required for functional Complex I even though it
is non-catalytic.

## Curation conclusions

- Core MF: structural molecule activity (GO:0005198). Contributes to (does NOT
  directly enable) NADH dehydrogenase (ubiquinone) activity (GO:0008137) at the
  complex level.
- Core CC: part_of respiratory chain complex I (GO:0045271); located_in
  mitochondrial inner membrane (GO:0005743, matrix side).
- Core BP: mitochondrial electron transport, NADH to ubiquinone (GO:0006120) and
  mitochondrial respiratory chain complex I assembly (GO:0032981; required for
  assembly per PMID:27626371).
- GO:0008137 "NADH dehydrogenase (ubiquinone) activity" as a *direct* MF (NAS,
  GO:0006120/enables) is an over-annotation for a non-catalytic accessory subunit:
  the catalytic MF belongs to the core subunits / holoenzyme. Marked over-annotated
  (NAS, not experimental, so not REMOVE-forbidden but MARK_AS_OVER_ANNOTATED is the
  right call and preserves the honest complex-level relationship via
  contributes_to in core_functions).
- IEA proton transmembrane transport (GO:1902600) and proton motive force-driven
  ATP synthesis (GO:0042776, NAS) are complex/pathway-level processes to which this
  non-catalytic subunit contributes only indirectly; kept as non-core rather than
  claimed as NDUFA2's own function.
- LONP1 Reactome mitochondrial-inner-membrane localizations are correct location
  calls (accepted as non-core, since they derive from a degradation model, not an
  NDUFA2-function assay).
