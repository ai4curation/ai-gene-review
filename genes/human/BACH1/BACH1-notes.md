# BACH1 (human, O14867) curation notes

No deep-research provider output was available for this review (no provider API keys).
These notes were compiled manually from the cached UniProt record, the cached
publications under `publications/`, and Europe PMC searches. Every assertion below
carries its provenance.

## Identity and architecture

- BTB-bZIP transcription regulator of the CNC subfamily; BTB/POZ domain (34-100) and
  bZIP domain (557-620) [file:human/BACH1/BACH1-uniprot.txt "Belongs to the bZIP family. CNC subfamily."].
- Heterodimerises with small Maf proteins (MAFK, MAFG, MAFF) and binds MARE/ARE
  elements [PMID:12356737 "Bach1 bound to the multiple Maf recognition elements (MAREs) of ho-1 enhancers with MafK in vitro and repressed their activity in vivo"].
- The BTB domain mediates repression and homodimerisation; the bZIP mediates
  heterodimerisation [PMID:24630724 "Bach1 and the related factor Bach2 contain a BTB protein-protein interaction motif that mediates transcriptional repression and a basic leucine zipper (bZIP) domain that mediates heterodimerization with other bZIP transcription factors"].

## Heme sensing (primary papers verified in Europe PMC)

- Ogawa et al. 2001 EMBO J, PMID:11387216 (Europe PMC search "Ogawa Bach1 heme EMBO";
  title "Heme mediates derepression of Maf recognition element through direct binding to
  transcription repressor Bach1."). Heme binds the C-terminal cysteine-proline (CP) motifs
  and inhibits DNA binding [PMID:11387216 "Mutations in all of the CP motifs of Bach1 abolished its interaction with heme."]
  [PMID:11387216 "The DNA-binding activity of Bach1 as a MafK hetero-oligomer was markedly inhibited by heme in gel mobility shift assays."]
- Sun et al. 2002 EMBO J, PMID:12356737: Bach1 is the physiological repressor of
  Hmox1 in mice; heme inhibits its binding to the enhancers [PMID:12356737 "regulation of ho-1 involves a direct sensing of heme levels by Bach1 (by analogy to lac repressor sensitivity to lactose)"].
- Suzuki et al. 2004 EMBO J, PMID:15175654: heme triggers CRM1-dependent nuclear export
  [PMID:15175654 "Inhibition of heme synthesis enhanced the nuclear accumulation of Bach1, whereas treating cells with hemin resulted in nuclear exclusion of Bach1."]
- Zenke-Kawasaki et al. 2007 Mol Cell Biol, PMID:17682061 (Europe PMC search
  "Zenke-Kawasaki ... Bach1"): heme induces polyubiquitination and degradation
  [PMID:17682061 "These results suggest that heme within a cell regulates the polyubiquitination and degradation of Bach1."]
  HOIL-1 (RBCK1) proposed as an E3 [PMID:17682061 "HOIL-1 stimulated the polyubiquitination of Bach1 in a purified in vitro ubiquitination system depending on the intact heme binding motifs of Bach1."]
- Lignitto et al. 2019 Cell, PMID:31257023: heme promotes FBXO22-mediated degradation
  [PMID:31257023 "heme triggers the degradation of Bach1, a pro-metastatic transcription factor, by promoting its interaction with the ubiquitin ligase Fbxo22."]
- Cao et al. 2024 Cell, PMID:39504958: FBXO22 and FBXL17 recognise quaternary BTB degrons
  after oxidative stress releases BACH1 from chromatin
  [PMID:39504958 "FBXO22 recognizes a degron constructed by the BACH1 BTB domain dimer interface, which is unmasked from transcriptional co-repressors after oxidative stress releases BACH1 from chromatin."]
- Tan et al. 2013 Mol Cell, PMID:24035498: SCF-FBXL17 turnover of BACH1 controls HMOX1
  [PMID:24035498 "FBXL17 controls the transcription of the NRF2 target HMOX1 via turnover of the transcriptional repressor BACH1"].

Most of the heme-binding/export/degradation biochemistry was done with mouse Bach1 or in
mouse cells; human-cell experiments include Suzuki 2004 (293T, GM02063) and Kitamuro 2003
(PMID:12511571, human HMOX1 repression).

## Targets and biology

- Human HMOX1 repression via a MARE [PMID:12511571 "We have identified a Maf recognition element in the human HO-1 gene that is required for repression of a reporter gene by hypoxia and targeted by Bach1."]
- ChIP-seq + knockdown in HEK293: HMOX1, FTL, FTH1, ME1, SLC48A1, GCLC, GCLM, SLC7A11 etc.
  [PMID:21555518 "The 59 BACH1 target genes identified by chromatin immunoprecipitation sequencing were found highly enriched in genes showing expression changes after BACH1 knockdown"].
- Ferroportin (SLC40A1) is co-regulated with HMOX1 by heme via BACH1 at a MARE/ARE
  (PMID:20179090, abstract only, mouse RAW264.7).
- Spic repression in macrophage precursors: heme-induced proteasomal degradation of
  Bach1 de-represses Spic, driving red pulp / bone marrow iron-recycling macrophage
  development (mouse) [PMID:24630724 "These results demonstrate that Bach1 is a transcriptional repressor of Spic that is inhibited by heme."]
  [PMID:24630724 "heme-mediated induction of Spic proceeds via proteasome-dependent degradation of the transcriptional repressor Bach1, and are not dependent on Nrf2."]
- Activator role: pro-metastatic genes in lung cancer [PMID:31257023 "Bach1 promotes invasion and metastasis by activating the transcription of critical metastatic genes"].

## Annotation issues found

- GO:0006281 DNA repair (IMP, PMID:11301010, CACAO): the paper describes the DEAH helicase
  "BACH1" = BRIP1/FANCJ (UniProtKB:Q9BX63, gene names BRIP1 BACH1 FANCJ), not the bZIP
  BACH1. The abstract states "BRCA1 interacts in vivo with a novel protein, BACH1, a member
  of the DEAH helicase family." O14867 has no helicase domain. Recorded as a source defect
  (symbol collision).
- NAS rows from ComplexPortal citing PMID:1655749 (ATF-1 cDNA paper) do not mention BACH1;
  the claims (nucleus; regulation of Pol II transcription) are correct anyway.
- Protein-binding rows: bZIP coiled-coil array data (Reinke 2010, 2013) support
  leucine-zipper heterodimerisation with MAF/ATF/DDIT3 partners -> protein
  heterodimerization activity; AP-MS/Y2H rows removed per policy.
- Comparator/NEW: no NEW process terms proposed. "cellular response to heme" was
  considered; the guessed id turned out to be a different term (checked in QuickGO), and
  the existing ligand-modulated TF activity row already captures heme sensing.
