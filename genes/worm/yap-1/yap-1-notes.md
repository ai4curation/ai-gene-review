# yap-1 (C. elegans) research notes

UniProt: Q19404 (YAP1_CAEEL, Swiss-Prot, PE 1), 442 aa. ORF F13E6.4, WormBase
WBGene00008748. One WW domain (203-236, PROSITE PRU00224); N-terminal region with
similarity to the YAP TEAD-binding domain; LATS-site Ser104 phosphorylated. UniProt calls
the family membership "Highly divergent". PANTHER PTHR17616:SF8 (TRANSCRIPTIONAL
COACTIVATOR YORKIE). Related reviews: `genes/worm/wts-1` (LATS) and `genes/worm/ftt-2`
(14-3-3).

## Provenance of this research

- Automated deep research was **not available** (no FutureHouse, Perplexity or OpenAI keys);
  no `-deep-research-<provider>.md` file exists. Literature work is manual.
- WormBase hand-written description fetched with
  `just mod-description-deep-research worm yap-1`, used as a recall checklist.
- Queries run (2026-11-16): PubMed esearch `(yap-1[tiab] OR "YAP-1"[tiab] OR F13E6.4) AND
  elegans` (19 hits, all titles scanned); QuickGO by reference for PMID:32857822, 41746831,
  31358532, 40178516, 37985670, 38177158, 40898783 (no annotations from any of them) and
  29853655 (the yap-1 rows only); comparator query for GO:0050829 in C. elegans (128 genes,
  including the transcription factors atf-7, cebp-1, daf-16, elt-2, hlh-30, skn-1, xbp-1 and
  zip-2).
- Cached with `just fetch-pmid`: 40898783 (abstract only), 37985670, 38177158, 32857822
  (full text). Already cached: 23396260 (abstract only), 27930654, 29853655, 31358532,
  41746831, 40178516 (full text). The founding paper (Iwasa et al. 2013) is abstract-only,
  so its interaction, reporter and S104 mutagenesis data were not read.

## Identity and regulation

- [PMID:23396260 "we found that F13E6.4 gene encodes a protein that shows sequence
  similarities to YAP in the N-terminal TEAD-binding domain and in the WW domain"].
- Localisation: [PMID:23396260 "YAP-1 is distributed in cytoplasm and nuclei."];
  [PMID:23396260 "wts-1 (LATS ortholog) and ftt-2 (14-3-3 ortholog) knockdowns cause nuclear
  accumulation of YAP-1"]; endogenous tagged YAP-1 [PMID:41746831 "Upon WTS-1 loss,
  endogenous YAP-1 translocated from cytosol to nucleus in the epithelium and intestine."].
- Direct WTS-1 binding: [PMID:31358532 "WTS-1 bound directly to YAP-1 and inhibited its
  nuclear accumulation in intestinal cells."].
- Upstream kinases: [PMID:41746831 "The duplicated Hippo-related kinases CST-1 and CST-2
  repressed YAP-1 nuclear localization in the epithelium but not the intestine"]; NFM-1/Merlin
  acts with WTS-1 in the intestine (PMID:31358532). Hippo-independent activation by PP2A
  after barrier loss (PMID:32857822).
- Heat: [PMID:23396260 "Heat shock also causes the nuclear accumulation of YAP-1 but after
  heat shock, YAP-1 translocates to cytoplasm."]; DAF-21/HSP90 and HSF-1 needed for the
  re-export.
- Cilia: an overexpressed YAP-1::GFP driven by the ciliated-neuron bbs-8 promoter appears in
  the ciliary axoneme [PMID:27930654 "Ciliary axoneme localisations are also observed for
  the GFP-tagged RPI-1, MAPH-9, YAP-1 and CCDC-104 translational reporters"]. No ciliary
  function is known.
- Hemidesmosome-containing structures in the hypodermis on daf-2(RNAi) (PMID:38177158).

## Roles

1. **WTS-1/YAP-1/EGL-44 module in larval development and intestinal polarity.**
   [PMID:41746831 "WTS-1, YAP-1, and the TEAD-like transcription factor EGL-44 form a
   conserved core module required for larval development past the L2 stage."]; yap-1 and
   egl-44 alleles suppress wts-1 (PMID:31358532), so hyperactive nuclear YAP-1 is what
   disrupts apicobasal polarity in wts-1 mutants; target candidates include tat-2.
   [PMID:41746831 "YAP-1/EGL-44 outputs are repurposed from the conventional association
   with growth control to nonproliferative developmental functions."]
2. **Thermotolerance and ageing.** [PMID:23396260 "YAP-1 overexpression is beneficial for
   thermotolerance, whereas YAP-1 hyperactivity induced by wts-1 and ftt-2 knockdowns is
   deleterious on thermal response and yap-1 deficiency promotes health aging."]. The ECM
   mechanotransduction study instead finds YAP-1 needed for longevity interventions
   [PMID:38177158 "coupling mechanical forces to adjust ECM gene expression and longevity via
   the transcriptional co-activator YAP-1 across tissues"]. The two lifespan results point
   in different directions and depend on context.
3. **Intestinal immunity after barrier loss.** [PMID:32857822 "Genetic inactivation of
   yap-1 and egl-44 significantly reduced the survival rate and promoted bacterial
   accumulation in worms after bacterial infections."]; [PMID:32857822 "These results
   demonstrate that the EGL-44/TEAD-YAP-1/YAP complex specifically controls a set of immune
   response-related genes in C."] (sentence continues "elegans"). Activation is
   Hippo-independent and needs PP2A.
4. **Neurons.** ALM dendrite polarity, cell-autonomous, downstream of CWN-1/CWN-2 Wnts
   [PMID:29853655 "Cell-specific rescue experiments showed that yap-1 acts in the cell
   autonomous manner to polarize ALM dendrites."]; touch-neuron deformation in wts-1 mutants
   is yap-1-dependent (PMID:40178516).
5. **Pharynx size scaling** via mechanotransduction (PMID:37985670); **phagosome closure**
   during compartmentalized cell elimination of the tail-spike cell, downstream of CDH-3,
   with EGL-44, through SYX-2 and EFF-1 (PMID:40898783).

## GO annotation thoughts

- MF: transcription coactivator activity (IBA, ISS) = core; binding to EGL-44 (IPI, Pol
  II-specific DNA-binding TF binding) and membership of the YAP-1/EGL-44 regulator complex
  are informative and accepted.
- protein kinase binding (IPI with WTS-1): YAP-1 is the substrate; kept non-core.
- BP: hippo signaling, positive regulation of transcription by Pol II (IBA, IGI with
  egl-44) = core. establishment of cell polarity (IMP, ALM) = non-core.
- CC: nucleus = core; cytoplasm = where it is held inactive (non-core); cilium/axoneme/
  ciliary base from one overexpression screen (non-core). cell-cell junction ISS from mouse
  Yap1: no worm study reports junctional YAP-1; marked over-annotated.
- NEW: defense response to Gram-negative bacterium (GO:0050829), IMP, PMID:32857822.
  Participation test: YAP-1 is the coactivator of the EGL-44 transcriptional program that
  induces the immune genes. Comparator: worm transcription factors that drive defense
  programs (atf-7, zip-2, skn-1, elt-2, hlh-30, daf-16, cebp-1) carry the term.
- UniProt MUTAGEN note for S104A reads "Cytoplasmic localization. No significant effect on
  nucleocytoplasmic localization." The two clauses contradict each other; the paper's full
  text could not be read to resolve it (recorded as a SUSPECTED defect).
- No PAINT losses on the lineage (`just paint-losses worm yap-1`).
