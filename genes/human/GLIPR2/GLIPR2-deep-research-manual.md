# Manual literature synthesis for human GLIPR2 (Q9H4G4)

## Research provenance and limitations

Automated deep research was attempted on 2026-07-18 using the required Falcon
provider with Perplexity-lite fallback. Falcon/Edison returned HTTP 402 and the
fallback returned HTTP 401 because the configured accounts lacked quota. This
manual synthesis is based on PubMed/PMC-cached primary literature, UniProt
Q9H4G4, QuickGO definitions, and the local PANTHER PAINT table. It is not a
provider-generated report.

## Evidence synthesis

GLIPR2, also known as GAPR-1, is a 154-residue CAP-domain protein that is
N-myristoylated at Gly2 and associates with lipid-enriched microdomains on the
cytosolic leaflet of the Golgi. It is unusual among CAP-family proteins because
it is not cotranslationally delivered to the ER lumen or secreted
[PMID:11865038]. Direct microscopy, Golgi fractionation, mass spectrometry, and
caveolin-1 co-immunoprecipitation support this topology and membrane association.

GAPR-1 forms homodimers, and its dimer state is sensitive to protein sequence,
inositol hexakisphosphate, membrane charge, and metal/redox conditions
[PMID:15123429; PMID:22560898; PMID:30700571; PMID:31636315]. Negatively charged
lipids support membrane binding and liposome tethering. Acidic lipids and metal
ions can also promote amyloid-like assemblies in vitro, but no physiological
function for those assemblies has been established [PMID:24471790;
PMID:30700571; PMID:31636315].

Overexpressed human GLIPR2 also forms dynamic, reversible inclusions in yeast,
and suppresses co-expressed human BECN1 condensates through the previously
mapped interaction surfaces [PMID:34298062; PMID:36586462]. These heterologous
experiments strengthen the case that assembly state can regulate BECN1 binding,
but do not demonstrate endogenous condensates in mammalian cells.

The best-established function is inhibition of basal macroautophagy. GLIPR2
binds the BARA region of BECN1 and the ATG14-containing class III
phosphatidylinositol 3-kinase complex I (PtdIns3K-C1). In vitro, wild-type GLIPR2,
but not a BECN1-binding-defective pentad mutant, binds PtdIns3K-C1, lowers its
membrane association, and reduces PtdIns3P production. In human HeLa cells,
CRISPR knockout increases autophagic flux, PtdIns3P, WIPI2 puncta,
autophagosomes, autolysosomes, and long-lived-protein degradation; wild-type
rescue reverses these phenotypes. Glipr2-null mouse tissues likewise show
increased basal autophagic flux and WIPI2 recruitment [PMID:23364696;
PMID:28876241; PMID:33222586]. This directly supports phosphatidylinositol
3-kinase inhibitor activity (GO:0141039) and negative regulation of
macroautophagy (GO:0016242).

Other experimentally supported roles are context dependent. Overexpression in
human HK-2 renal epithelial cells and hepatocellular-carcinoma lines activates
ERK1/2, EMT-like marker changes, migration, and invasion; GLIPR2 knockdown
attenuates these responses during hypoxia in HCC cells [PMID:23516513;
PMID:24204846]. An abstract-only monocyte/TLR4 study reports that IRAK1
phosphorylates GAPR-1 at Ser58, enabling TMED7 interaction and enhancing
IFN-beta/IL10 output [PMID:26678074]. It is unknown whether either phenotype is a
direct consequence of PtdIns3K-C1/autophagy inhibition.

Three high-throughput proteomic studies identify GLIPR2 in extracellular-exosome
preparations [PMID:18570454; PMID:19056867; PMID:23533145]. These observations
are retained as non-core vesicle-cargo localizations; they do not support the
extracellular-region activity inferred from the broadly secreted CAP family.

## PAINT conclusion

CAP-family membership does not establish extracellular localization for GLIPR2,
which is a directly demonstrated nonsecreted cytosolic Golgi protein. The broad
PTN000036124 extracellular-region propagation should be removed. The same node's
molecular-adaptor inference is seeded solely from mouse Glipr1l1, a divergent
sperm/acrosomal paralog, and does not provide valid transfer evidence for
GLIPR2. Direct GLIPR2 data instead support the specific replacement molecular
function GO:0141039, phosphatidylinositol 3-kinase inhibitor activity.

## Key unresolved questions

- Where does endogenous GLIPR2 encounter and inhibit PtdIns3K-C1, and is Golgi
  tethering required?
- Does GLIPR2 also inhibit the UVRAG-containing PtdIns3K-C2 complex?
- Are dimerization and myristoylation required for BECN1/PtdIns3K-C1 inhibition
  independently of their role in membrane localization?
- Do ERK/EMT and TLR4/interferon effects require autophagy inhibition?
- Do reversible amyloid-like assemblies occur in vivo or represent only an in
  vitro property of concentrated membrane-bound CAP domains?
