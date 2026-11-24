# WDR76 (human, Q9H967) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: WDR76 is being reviewed as the closest experimentally characterised
relative of Arabidopsis DRS1 (Q9SAI7). No ProtNLM2 files or prediction-evidence
folders were opened; this review is built only from literature, UniProt, GOA and
PANTHER/PAINT data.

### Deep research status

`just deep-research-falcon human WDR76 --fallback perplexity-lite` failed:
falcon returned `403 Forbidden` at the Edison auth endpoint
(`https://api.platform.edisonscientific.com/auth/login`), and the
perplexity-lite fallback timed out after 600 s. No deep-research file exists.
The review was built from a direct PubMed search (`WDR76[tiab]`, 30 hits;
`Cmr1[tiab] AND yeast`) and the cached papers listed below.

### Evolutionary grounding

- PANTHER: Q9H967 is in PTHR14773:SF0 "WD REPEAT-CONTAINING PROTEIN 76"
  (`interpro/panther/PTHR14773/PTHR14773-entries.csv`), the same subfamily as
  yeast CMR1 (Q12510) and Arabidopsis DRS1 (Q9SAI7). InterPro IPR050853
  (WD_repeat_DNA-damage-binding). UniProt: "Belongs to the WD repeat
  DDB2/WDR76 family."
- Gallina et al. 2015 call WDR76 the Cmr1 orthologue
  [PMID:25817432 "WDR76 is the closest orthologue of Cmr1 in higher eukaryotes"].
- PAINT node PTN000381277 propagates four terms to WDR76: nucleus
  (donors CMR1 + WDR76), heterochromatin (donor WDR76 only), DNA binding
  (donor CMR1), regulation of DNA damage checkpoint (donor CMR1).
- Yeast Cmr1 experimental terms NOT propagated by PAINT (QuickGO, 2026-10-21):
  chromatin (IDA, PMID:22367945), cytoplasm (IDA/HDA), nuclear periphery
  (IDA, PMID:25817432; the INQ compartment). These are treated as deliberate
  omissions; I do not transfer INQ / nuclear periphery to human.

### Human experimental evidence (what is established in this species)

- Nucleus / chromatin: GFP-WDR76 in human cells "associated with chromatin in
  untreated cells and relocalized into nuclear foci under replication stress
  conditions" [PMID:25817432]. Human foci are not at 53BP1 DSB foci and mostly
  not at PCNA replication foci [PMID:25817432].
- Heterochromatin: Halo-WDR76 co-localises with CLIP-CBX1/CBX5 puncta, which
  the authors identify as heterochromatic regions [PMID:27248496]. This is an
  overexpression/co-localisation result.
- Site of DNA damage: Halo-WDR76 is recruited to UV-laser microirradiation
  stripes immediately, with higher maximal recruitment than PARP1, XRCC5 or RPA1
  [PMID:27248496].
- Interactions (co-IP/AP-MS): CBX1, CBX3, CBX5, PARP1, XRCC5 [PMID:27248496];
  CCT/TRiC, HELLS, SUGT1 [PMID:25817432]; CCT complex via the WD40 domain and
  DNA-PK-KU, PARP1, GAN, SIRT1, histones outside it [PMID:31353912]; CUL4A/B
  (UniProt SUBUNIT, ECO:0000269, PMID:17041588); SPIN1 with H3K4me3 nucleosomes
  [PMID:39116123].
- Protein turnover: WDR76 binds HRAS, promotes RAS polyubiquitination and
  proteasome-dependent degradation in liver cancer cells; Wdr76-/- mice have
  raised Ras [PMID:30655611; PMID:31362761; PMID:31873167]. The cullin partner
  is contested: Jeong 2019 used CUL4A co-expression, Wang 2025 reports "WDR76
  couples with CUL1 E3 ligase, rather than CUL4" [PMID:40889735]. Huang 2020
  shows WDR76 instead antagonises CRL4-DCAF8-mediated LSH (HELLS) degradation
  [PMID:33288900]. So the robust process-level claim is participation in
  ubiquitin-dependent proteasomal protein degradation of RAS; whether WDR76 is a
  bona fide substrate receptor (DCAF) of a specific cullin is unresolved.

### Inferred only (not tested in human)

- DNA binding: yeast Cmr1 recombinant protein binds DNA and prefers UV-damaged
  DNA [PMID:22367945]. The mouse/Xenopus 5hmC-reader statement in UniProt is
  ECO:0000250 (by similarity) from the Spruijt 2013 mESC reader screen
  [PMID:23434322, abstract only, WDR76 not named in abstract]. No direct human
  DNA-binding assay found.
- Regulation of DNA damage checkpoint: from yeast cmr1Δ checkpoint-adaptation
  defect [PMID:25817432]; Gallina explicitly leave open whether WDR76
  participates in the human replication stress response.

### Decisions

- Generic protein binding (CBX1/3/5 IPI): REMOVE per GO:0005515 policy.
- Enzyme binding (PARP1, XRCC5 IPI): KEEP_AS_NON_CORE; validated co-IPs,
  functional meaning unknown.
- DNA damage response (IMP): KEEP_AS_NON_CORE; human evidence is relocalisation.
- Regulation of DNA damage checkpoint (IBA): KEEP_AS_NON_CORE; inherited
  yeast claim, untested in human.
- NEW: GO:0043161 proteasome-mediated ubiquitin-dependent protein catabolic
  process (RAS degradation, two independent labs). Comparator check: CRL
  substrate-receptor WD40 proteins DTL (Q9NZJ0, GO:0043161 IBA) and DCAF1
  (Q9Y4B6, GO:0043161 IDA) carry it, so this matches convention for an
  adaptor that recruits the substrate. Not adding GO:0080008 Cul4-RING complex
  because the cullin partner is contested.
- Organismal phenotypes (obesity/steatosis, tumour susceptibility in Wdr76-/-
  mice, ferroptosis) are not annotated as process participation.
