# LOC732824 (ZmCCaMK) - manual literature synthesis

No deep-research API was available for this session; this file was compiled manually from
PubMed searches (query "ZmCCaMK maize", 8 hits) and the cached publications under
`publications/`. Every claim carries inline provenance.

## Identity

- UniProt A0A804P0P6 (TrEMBL, Zm00001eb200350_P001, B73 RefGen_v5), 528 aa, GeneID 732824,
  RefSeq NP_001105906.1. The same gene and an identical sequence (same CRC64
  83CA9566392266E9) is also represented by the older TrEMBL entry Q208N4, which is built from
  GenBank DQ403196, the ZmCCaMK cDNA used in every functional paper below
  [PMID:22865912 "ZmCCaMK (GenBank accession no. DQ403196"; PMID:27208250 "ZmCCaMK DQ403196"].
  The literature name is **ZmCCaMK** (maize calcium and calcium/calmodulin-dependent protein
  kinase). It is the maize ortholog of Medicago DMI3 / Lotus CCaMK and rice OsCCaMK/OsDMI3
  [PMID:22865912 "the rice mutant line NF8513 ('Nipponbare') containing the Tos17 insertion in OsDMI3, a homologous gene of ZmCCaMK in rice"].
- Domain architecture (UniProt features, PROSITE/InterPro): Ser/Thr protein kinase domain
  13-307 with ATP-binding Lys45 and catalytic Asp172 (proton acceptor); three EF-hand motifs
  (408-436, 437-472, 479-514) forming a visinin-like Ca2+-binding domain; the region between
  kinase and EF-hands corresponds to the CaM-binding/autoinhibitory region of CCaMKs
  [PMID:22865912 "A CCaMK structure includes a serine/threonine kinase domain, a CaM-binding domain, and three EF-hand motifs, similar to the visinin-like domain"].

## Molecular function: Ca2+/CaM-dependent protein Ser/Thr kinase

- Immunoprecipitated ZmCCaMK from maize leaves phosphorylates histone S-III in an in-gel
  kinase assay; the activity is competed by the antigen peptide, and is reduced by EGTA,
  LaCl3 and CaM antagonists [PMID:22865912 "Proteins that could phosphorylate histone S-III were precipitated from extracts of leaves of maize plants."; "pre-treatments with the Ca2+ chelator EGTA, the Ca2+ channel blocker LaCl3, and the CaM antagonists TFP and W7 significantly reduced the ABA-induced activation of ZmCCaMK"].
- ZmCCaMK phosphorylates the NAC transcription factor ZmNAC84 in vitro at Ser-113 (LC-MS/MS)
  [PMID:27208250 "ZmCCaMK was found to phosphorylate His-ZmNAC84 in vitro ( Fig. 1C )."; "LC-MS/MS analysis confirmed Ser-113 in ZmNAC84 as the phosphorylation site by ZmCCaMK"].
- Recombinant ZmCCaMK phosphorylates myelin basic protein in a reaction containing Ca2+ and CaM,
  but does not phosphorylate its interactor ZmWRKY104 [PMID:41482925 "In vitro kinase assays showed a ³²P-labeled band for MBP (positive control) but no ³²P-labeled band for ZmWRKY104 (Figure 1d), indicating that ZmWRKY104 is not a phosphorylation substrate of ZmCCaMK."].
- Autophosphorylation: seven candidate autophosphorylation sites identified by LC-MS/MS; T420
  and S454 (in the EF-hand region) are needed for autophosphorylation and substrate
  phosphorylation [PMID:32113680, abstract only].
- Upstream regulation: ZmBSK1 (a plasma-membrane BR-signalling kinase) phosphorylates ZmCCaMK at
  Ser-67, which regulates its Ca2+/CaM binding, autophosphorylation and transphosphorylation
  [PMID:33864702, abstract only]. Residue numbers S67, T420 and S454 all fall on Ser/Thr in the
  displayed A0A804P0P6 sequence (checked in this session), so the papers use the canonical
  numbering.

## Location

- YFP-ZmCCaMK (35S promoter, transient expression in maize mesophyll protoplasts) is found in
  the nucleus (DAPI), cytoplasm and plasma membrane (FM4-64) [PMID:22865912 "YFP–ZmCCaMK was localized in the nucleus, the cytoplasm, and the plasma membrane in maize mesophyll protoplasts"].
- BiFC places the ZmCCaMK-ZmNAC84 and ZmCCaMK-ZmWRKY104 complexes in the nucleus
  [PMID:27208250 "the BiFC experiments revealed that ZmCCaMK-ZmNAC84 interacted in nucleus"; PMID:41482925].
- Legume orthologs (DMI3) are nuclear [PMID:22865912 "In Medicago trunculata, CCaMK (DMI3) was localized in the nucleus in epidermal root cells and root hairy cells"].

## Biological roles studied in maize

- **ABA signalling / antioxidant defence:** ABA (via H2O2 then NO) activates ZmCCaMK and
  induces its transcript; transient overexpression raises SOD/APX expression and activity, RNAi
  reduces them [PMID:22865912]. Activated ZmCCaMK phosphorylates ZmNAC84 at Ser-113, and Ser-113
  is required for the ABA-induced stimulation of antioxidant defence by ZmCCaMK [PMID:27208250].
  ZmCCaMK is not required for ABA-induced NO production (acts downstream of NO) [PMID:22865912].
- **Brassinosteroid signalling:** BR raises cytosolic Ca2+ and ZmCCaMK activity; ZmCCaMK is
  required for BR-induced antioxidant defence [PMID:25647327, abstract]; ZmBSK1 phosphorylates
  ZmCCaMK [PMID:33864702; PMID:35738188]; ZmWRKY104 interacts with ZmCCaMK without being
  phosphorylated [PMID:41482925].
- **Drought / salt tolerance:** overexpression phenotypes in tobacco/maize (PMID:32113680,
  PMID:33864702, PMID:41482925). These are phenotype-level and do not themselves establish a
  process annotation.
- **Root endosymbiosis:** CCaMK/DMI3 is a core component of the common symbiosis signalling
  pathway for arbuscular mycorrhiza in plants generally [PMID:41482925 "CCaMK was initially identified as a key factor in root nodule symbiosis of legumes and arbuscular mycorrhizal symbiosis of mycorrhizal plants"],
  but no maize-specific genetic test of ZmCCaMK in AM symbiosis was found in PubMed (search
  "(CCaMK OR DMI3) AND maize AND (mycorrhiza OR symbiosis)" returned 0 hits). The rice ortholog
  is required for AM symbiosis in the literature generally; this is not asserted for maize here.

## Caveats

- All maize functional work comes from one group (Nanjing Agricultural University) and relies
  heavily on transient protoplast assays and antioxidant-enzyme readouts.
- Localization uses 35S-driven YFP fusions; native-promoter localization has not been reported.
