# SMPD3 (nSMase2 / neutral sphingomyelinase 2) — review notes

UniProt: Q9NY59 (NSMA2_HUMAN). Gene: SMPD3 (HGNC:14240). EC 3.1.4.12. 655 aa. Chromosome 16.

## Core identity and enzymology

SMPD3 is the **Mg2+-dependent neutral sphingomyelinase 2 (nSMase2)**, the major
stress-responsive cellular neutral sphingomyelinase. It hydrolyses sphingomyelin to
ceramide + phosphocholine, generating the second-messenger ceramide.

- "Catalyzes the hydrolysis of sphingomyelin to form ceramide and phosphocholine.
  Ceramide mediates numerous cellular functions, such as apoptosis and growth arrest"
  [file:human/SMPD3/SMPD3-uniprot.txt].
- EC=3.1.4.12; catalytic activity `a sphingomyelin + H2O = phosphocholine + an
  N-acylsphing-4-enine + H(+)` (Rhea:19253), evidence PubMed:15051724
  [file:human/SMPD3/SMPD3-uniprot.txt].
- Cofactor Mg(2+), evidence PubMed:10823942, PubMed:15051724
  [file:human/SMPD3/SMPD3-uniprot.txt]. Neutral pH optimum (7.5).
- Pathway: "Lipid metabolism; sphingolipid metabolism." (PubMed:14741383,
  PubMed:15051724) [file:human/SMPD3/SMPD3-uniprot.txt].

### Cloning / characterisation
Hofmann et al. 2000 (PMID:10823942) identified nSMase2 as a second mammalian nSMase
"with predominant expression in the brain. The sphingomyelinase activity of nSMase2 has
a neutral pH optimum, depends on Mg(2+) ions, and is activated by unsaturated fatty
acids and phosphatidylserine." Immunofluorescence "colocalizes with a Golgi marker in a
number of cell lines" and it is likely identical to rat cca1, "a rat protein involved in
contact inhibition of 3Y1 fibroblasts, suggests a role for this enzyme in cell cycle
arrest" [PMID:10823942]. Inhibited by GW4869 [file:human/SMPD3/SMPD3-uniprot.txt].

### Additional substrates (broader in vitro specificity)
Miura et al. 2004 (PMID:14741383) showed "nSMase1 and nSMase2, human neutral
sphingomyelinases (SMases), are capable of hydrolyzing SPC [sphingosylphosphocholine]
efficiently under detergent-free conditions." Substrate specificity: hydrolyses SM, SPC,
and monoradyl glycerophosphocholine "but not diradyl glycerophosphocholine"
[PMID:14741383]. UniProt captures the corresponding CATALYTIC ACTIVITY entries
(sphingosylphosphocholine, 1-hexadecanoyl-/1-O-octadecyl-sn-glycero-3-phosphocholine) all
with EC 3.1.4.12-type phosphodiester hydrolysis, evidence PubMed:14741383
[file:human/SMPD3/SMPD3-uniprot.txt].

## Subcellular location
- "Golgi apparatus membrane {ECO:0000269|PubMed:10823942}; Lipid-anchor" and "Cell
  membrane {ECO:0000269|PubMed:15051724}; Lipid-anchor" [file:human/SMPD3/SMPD3-uniprot.txt].
- Marchesini et al. 2004 (PMID:15051724): "nSMase2 became nearly exclusively located at
  the plasma membrane in confluent, contact-inhibited cells" [PMID:15051724].
- Membrane topology: two intramembrane (hairpin) helical segments (aa 11–31, 65–85); the
  catalytic domain is cytoplasmic (TOPO_DOM 86..655) [file:human/SMPD3/SMPD3-uniprot.txt];
  Tani & Hannun 2007 (PMID:17349629) analysed topology.
- Palmitoylated (S-palmitoyl Cys at 53/54/59/397/398); "palmitoylation-deficient proteins
  are targeted for lysosomal degradation" [file:human/SMPD3/SMPD3-uniprot.txt]. Lipid-anchor,
  not a classical single-pass transmembrane protein.

## Anionic phospholipid binding (regulatory, not lipid metabolism per se)
"Binds to anionic phospholipids (APLs) such as phosphatidylserine (PS) and phosphatidic
acid (PA) that modulate enzymatic activity and subcellular location" and "Binding of
anionic phospholipids (APLs) such as phosphatidylserine (PS) and phosphatidic acid (PA)
increases enzymatic activity" [file:human/SMPD3/SMPD3-uniprot.txt]. So PS/PA binding
(GO:0001786, GO:0070300) are genuine regulatory functions of the enzyme, transferred by
similarity from mouse Q9JJY3.

## Cell-cycle / growth-arrest role
Marchesini et al. 2004 (PMID:15051724): endogenous nSMase2 mRNA up-regulated ~5-fold at
confluence; siRNA knockdown "increased the cell population of cells in S phase" and
prevented Rb dephosphorylation / p21 induction; "nSMase2 functions as a growth suppressor
in MCF7 cells, linking confluence to the G(0)/G(1) cell cycle check point" [PMID:15051724].
UniProt: "Regulates the cell cycle by acting as a growth suppressor in confluent cells"
and DEVELOPMENTAL STAGE "Up-regulated during G0/G1 phases" [file:human/SMPD3/SMPD3-uniprot.txt].

## TNF-R1 signalling / EED interaction (the GO:0005515 IPI)
Philipp et al. 2010 (PMID:20080539) identified the Polycomb protein EED (UniProt O75530)
as an interaction partner: "the N terminus of EED binds to the catalytic domain of
nSMase2"; TNF recruits EED and nSMase2 to the TNF-R1.FAN.RACK1 complex; EED knockdown
abrogates TNF-dependent activation of nSMase2, so EED "physically and functionally
couples TNF-R1 to nSMase2" [PMID:20080539]. This is the O75530 IntAct IPI in GOA. Reactome
R-HSA-5626981 "TNF-α:TNFR1:NSMAF:GNB2L1 associates with SMPD2,3" captures the same complex.

## Development / skeletal role
UniProt: "Probably acts as a regulator of postnatal development and participates in bone
and dentin mineralization (PubMed:10823942, PubMed:14741383, PubMed:15051724)"
[file:human/SMPD3/SMPD3-uniprot.txt]. KW "Developmental protein". This underlies the
fro/fro (fragilitas ossium) mouse phenotype and SMPD3-related skeletal dysplasia; the
mouse ortholog (O35049) is the source of transferred developmental/exosome annotations.

## Exosome / extracellular-vesicle secretion
GOA has GO:1903543 positive regulation of exosomal secretion (ISS from mouse O35049).
nSMase2-generated ceramide drives inward budding of intraluminal vesicles / exosome
release; the mouse ortholog experimentally supports this. No direct human experimental
statement in the cached UniProt text, so treated as a supported-by-orthology non-core
process.

## Notes on specific GOA annotations
- Cytoplasm (IBA, GO:0005737): the catalytic domain is cytosol-facing but the protein is
  membrane-anchored at Golgi/plasma membrane; "cytoplasm" is a low-information IBA that is
  compatible with a cytoplasmic-facing membrane enzyme but is not the informative location.
- Endoplasmic reticulum (IDA, GO:0005783, from HPA GO_REF:0000052): HPA immunofluorescence.
  Not the canonical location (Golgi + plasma membrane); kept as non-core, likely partly
  reflecting the biosynthetic/secretory route. Overexpression IF can show ER staining.
- Extracellular region (IEA, GO:0005576, InterPro IPR017766): the InterPro
  Sphingomyelinase/PLipase_C signature is shared with secreted bacterial SMases; SMPD3 is a
  membrane-anchored intracellular enzyme, so this is an InterPro over-propagation.
- catalytic activity (GO:0003824) and phosphoric diester hydrolase activity (GO:0008081)
  are correct but generic parents of the specific GO:0004767.
- metal ion binding: UniProt DR lists GO:0046872 (metal ion binding, IEA UniProtKB-KW) and
  a Mg(2+) BINDING site at residue 364 (ECO:0000250) — supports magnesium ion binding
  (GO:0000287) as a core supporting MF (cofactor Mg2+).

## Key GO term ids used in core_functions (verified via OLS 2026-07)
- GO:0004767 sphingomyelin phosphodiesterase activity (MF; hydrolysis SM -> ceramide + choline phosphate)
- GO:0000287 magnesium ion binding (MF; Mg2+ cofactor)
- GO:0006685 sphingomyelin catabolic process (BP)
- GO:0046513 ceramide biosynthetic process (BP)
- GO:0000139 Golgi membrane (CC)
- GO:0005886 plasma membrane (CC)
