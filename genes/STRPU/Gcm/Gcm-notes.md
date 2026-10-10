# Gcm (Strongylocentrotus purpuratus, UniProt Q8MMJ4) - curation notes

## Identity

- UniProt Q8MMJ4 (`Q8MMJ4_STRPU`, unreviewed/TrEMBL, 794 aa) is the S. purpuratus
  Glial cells missing-like protein deposited by the Davidson lab from the 12 h
  endomesoderm cDNA library (EMBL AAM53250.1, RefSeq NP_999826.1, GeneID 378470).
  Its single RX line is PMID:12027439 (Ransick et al. 2002), the differential
  macroarray screen that discovered `Spgcm`. Community symbol: `gcm` / `Gcm`
  (older papers `Spgcm`, `SpGcm`). No identity doubt: this is the single sea
  urchin gcm gene used in all Davidson-lab GRN work.
- Domain architecture (UniProt FT): GCM DNA-binding domain at residues 50-208
  (PROSITE PS50807, Pfam PF03615); three MobiDB-lite disordered regions; the
  more 3' exons encode the trans-activation domains
  [PMID:22509525 "However, this fusion protein does not contain the more 3’ Gcm exons encoding the trans-activation domains."].
  PANTHER PTHR12414 / PTHR12414:SF8 (labels not written from memory here).
- The GCM consensus binding site ATGCGGRY is used in cis-regulatory work on this
  gene [PMID:22509525 "This candidate Gcm site matched the published consensus ATGCGGRY"].

## Place in the endomesoderm GRN

Gcm is the immediate transcriptional target of Delta/Notch signalling from the
skeletogenic micromeres and the top-level regulator of the aboral
non-skeletogenic mesoderm (NSM) / pigment cell regulatory state.

- Discovery and expression: found among transcripts sharply reduced by
  cadherin-mRNA blockade of nuclear beta-catenin
  [PMID:12027439 "Spgcm, an orthologue of the fruit fly gene glial cells missing, which is first expressed specifically and exclusively in part of the prospective secondary mesenchyme (mesodermal) domain at late-cleavage blastula stage"].
  Also recovered independently in a pigment-cell-specific differential screen
  and shown by WMISH to be pigment-cell specific
  [PMID:12925586 "This group of clones contained sequences highly similar to: the transcription factor glial cells missing (gcm); the polyketide synthase gene cluster (pks-gc)"; "it was shown that these genes are specifically expressed in pigment cells"].
- Input (Delta/Notch via Su(H)): three cis-regulatory modules identified; a
  conserved paired Su(H) site plus a lone site in the middle module both drive
  expression in Delta-receiving SMC precursors and repress it elsewhere
  [PMID:16925988 "confirming that spgcm is a direct target of canonical N signaling mediated through Su(H) inputs"].
  gcm is the first gene switched on by Delta signalling in veg2
  [PMID:22306924 "gcm was previously shown to be a direct cis-regulatory target of the Nic/Su(H) complex (Ransick and Davidson, 2006), and is the first gene to become activated by D/N signaling."; "Only these cells are contiguous to the Delta source on which gcm expression is dependent."].
- Spatial repression: Alx1 keeps gcm out of the skeletogenic micromere lineage
  [PMID:18413610 "a role of the micromere lineage regulator alx1 is to repress gcm in that lineage"],
  and FoxA keeps it out of the veg2 endoderm
  [PMID:17038513 "a crucial role of Foxa is to repress gcm expression in response to a Notch signal, and hence to repress mesodermal fate"].
  Later, Not clears gcm from the oral NSM so that gcm becomes strictly aboral
  [PMID:23261933 "Most strikingly, gcm expression persists throughout the entire circular NSM at 24 hpf in embryos treated with Not MASO while in controls, expression of gcm is extinguished in the oral segment by about 19 hpf."].
- Output, early phase (specification): gcm morpholino gives larvae with no pigment cells
  [PMID:16925988 "Here, we show that microinjection of a spgcm antisense morpholino oligonucleotide results in larvae without pigment cells."; "These results confirm that this gene is required for pigment cell specification."].
  gcm is the pioneer of the aboral NSM regulatory state
  [PMID:23261933 "First the gcm gene acts as the primary, novel, regulatory state pioneer activated by the D/N signal"].
- Output, direct targets: gataE is a direct Gcm target and Gcm is the
  Notch-dependent feed-forward input into gataE
  [PMID:23261933 "A linchpin of this network is gataE which as we show is a direct Gcm target and part of a feedback loop locking down the aboral regulatory state."]
  [PMID:22306924 "Gcm itself is an activator required, in a feed forward relationship with respect to the D/N input, for gataE expression to occur in the NSM."].
  pks (echinochrome polyketide synthase) is a direct target via Gcm sites in
  its -1.5 kb cis-regulatory region
  [PMID:20122918 "Predicted DNA-binding sites for SpGcm, SpGataE and SpKrl are located within this region. The mutagenesis of these DNA-binding sites indicated that SpGcm, SpGataE and SpKrl are direct positive regulators of SpPks."].
  Gcm MASO knocks down the whole pigment differentiation battery
  [PMID:23261933 "As expected, Gcm MASO causes severe decreases in transcript levels of the differentiation genes bpnt, dopt, fmo, papss, pks, and sult."; "Gcm provides a direct input into pigment cell differentiation genes, which begin to be expressed even before gastrulation"].
- Output, late phase (self-sustaining loop): a late cis-regulatory module takes
  over from mesenchyme blastula; its two critical elements are Gcm and Six1 sites
  (autoregulation plus gcm-gataE-six1 feedback)
  [PMID:22509525 "Cis-perturbation analyses reveal that the two critical elements within this late module are consensus matches to Gcm and Six1 binding sites."; "The self-sustaining expression of gcm that the late module promotes effectively locks down the pigment cell fate."; "Gcm is required in veg2 progeny during late cleavages for the early phase of pigment cell precursor specification."].
- Sufficiency (synthetic rewiring): forcing gcm under tbr control in
  skeletogenic cells converts them to pigment cells and up-regulates pks while
  repressing alx1/ets1/tbr
  [PMID:22238426 "The result of reengineering the regulatory circuitry in this way was to divert the developmental program of these cells from skeletogenesis to pigment cell formation, confirming a direct prediction of the GRN."; "Both Delta/Notch signaling and Gcm translation are absolutely required for pigment cell specification"].
  The repression of skeletogenic genes is indirect (probably via ets1) and is
  not annotated here. Cross-species confirmation in other euechinoids:
  [PMID:27046223 "We confirmed previous results by demonstrating that gcm is involved in pigment cell differentiation."; "gcm functions in skeletogenic fate repression"].

## Annotation decisions (journal)

- Electronic MF/CC rows (GO:0000981, GO:0000978, GO:0001228, GO:0003677, nucleus)
  are consistent with the cis-regulatory evidence (Gcm sites required in pks and
  in the gcm late module; direct activation of gataE) and are accepted.
- GO:0042063 gliogenesis (IBA, from Drosophila gcm/gcm2 and mouse Gcm1): removed.
  The Drosophila glial function is lineage-specific; vertebrate Gcm1/Gcm2 act in
  placenta/parathyroid, and sea urchin gcm is expressed exclusively in mesodermal
  pigment cell precursors and never in neural tissue, so the target lies outside
  any clade for which gliogenesis can be inferred.
- NEW: GO:0001228 (IDA, pks and gcm late-module site mutagenesis), GO:0000978
  (IDA), GO:0045944 (IDA/IMP), GO:0007501 mesodermal cell fate specification (IMP:
  MASO loss, synthetic gain), GO:0050942 positive regulation of pigment cell
  differentiation (IMP/IDA). Indirect skeletogenic repression and oral-NSM
  repression (via GataE) are not annotated.
- gocams/index.tsv contains no entry for this gene.
