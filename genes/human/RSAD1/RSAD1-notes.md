# RSAD1 (human, Q9HA92) — curation notes

Part of the RADICAL_SAM project (`projects/RADICAL_SAM.md`). Literature retrieval was
run with the `asta` provider (`RSAD1-deep-research-asta.md`) because the `falcon`
provider failed with an authentication error; the asta output turned out to be
retrieval noise (database/annotation-methodology papers, none about RSAD1), so the
evidence below was assembled from the cached publications plus targeted PubMed
searches.

## Identity and architecture

- UniProt: "Radical S-adenosyl methionine domain-containing protein 1, mitochondrial",
  with `AltName: Full=Putative heme chaperone {ECO:0000303|PubMed:29282292}`
  [file:human/RSAD1/RSAD1-uniprot.txt].
- Radical SAM core domain 34–270, N-terminal mitochondrial transit peptide 1–17,
  mature chain 18–442; signatures: `PF04055 Radical_SAM`, `PF06969 HemN_C`,
  `IPR004559 HemW-like`, `TIGR00539 hemN_rel`, `PANTHER PTHR13932:SF5`
  [file:human/RSAD1/RSAD1-uniprot.txt].
- Family placement: "Belongs to the anaerobic coproporphyrinogen-III oxidase" family,
  **HemW subfamily** [file:human/RSAD1/RSAD1-uniprot.txt]. This is the key point: HemW
  is a sister subfamily to the catalytic HemN (coproporphyrinogen III dehydrogenase,
  EC 1.3.98.3) proteins, not a HemN itself.
- UniProt function text: "May be a heme chaperone, appears to bind heme." and
  "Binds 1 [4Fe-4S] cluster." [file:human/RSAD1/RSAD1-uniprot.txt]. UniProt explicitly
  records that homologous bacterial proteins lack oxygen-independent
  coproporphyrinogen-III oxidase activity.

## HemW is not a coproporphyrinogen oxidase/dehydrogenase

- *Lactococcus lactis* HemW: "showed that it is devoid of CPDH activity in vivo and in
  vitro" and HemW-like proteins "are usually annotated as CPDHs
  (coproporphyrinogen III dehydrogenases). However, such a function has never been
  demonstrated for a HemW-like protein." The protein instead "covalently bound haem b
  in vitro, with a stoichiometry of one haem per monomer", existed as "a haem-free
  cytosolic form, as well as a haem-containing membrane-associated form", and released
  heme on addition of membranes, leading the authors to "propose a role of HemW in
  haem trafficking" [PMID:22142238].
- HemW-like proteins "form a distinct phylogenetic clade that has not previously been
  recognized" [PMID:22142238] — i.e. the catalytic HemN activity is a property of the
  sister clade, and the HemW clade is defined partly by its loss (the fourth cysteine
  of the HemN CX3CX2CXC motif is not conserved; see also [PMID:34311096], which argues
  mycobacterial "HemN" sequences are mis-annotated HemW proteins).

## HemW/RSAD1 as a heme chaperone

- *E. coli* HemW: "we observed one heme per subunit of HemW", "intact iron-sulfur
  cluster was required for HemW dimerization and HemW-catalyzed" "heme transfer but not
  for stable heme binding"; "Of note, heme that was covalently bound to HemW was
  actively transferred to a" heme-depleted, inactive nitrate reductase, restoring
  activity; interaction partners found were bacterioferritins and the heme-containing
  NarI subunit of nitrate reductase [PMID:29282292].
- Human protein: "domain-containing 1 (RSAD1) stably bound heme. In conclusion, our
  findings" "indicate that the radical SAM protein family HemW/RSAD1 is a heme
  chaperone" [PMID:29282292]. Note the human experiment establishes **binding**; the
  transfer/insertion experiments were done on the bacterial protein. GOA records only
  `GO:0020037 heme binding` (IDA) from this paper, which is the right scope.
- Independent biochemistry on the human protein: hRSAD1 "was reconstituted with"
  "a [4Fe-4S]2+ cluster that could be reduced to the [4Fe-4S]+ state", binds PPIX and
  its metal analogues (K_A for Fe(III)-PPIX ≈ 1.6 × 10^6 M⁻¹), and the
  "hRSAD1-[4Fe-4S]-heme complex binds" "oxygen, carbon monoxide, and cyanide"; the
  authors conclude only that hRSAD1 "may" "play a significant role in heme-related
  metabolic processes" [PMID:41747499]. So: cluster + heme binding confirmed on the
  human protein; no reaction demonstrated.
- Reviews of the human radical SAM set still list RSAD1 among enzymes "of unknown
  function" [PMID:27145839]; the tetrapyrrole-focused review states that "In bacteria,
  heme is inserted into enzymes by the cytoplasmic heme chaperone HemW, a radical SAM
  enzyme structurally highly related to CgdH" [PMID:37101575].

## Localization

- UniProt: "SUBCELLULAR LOCATION: Mitochondrion" (ECO:0000305), with a predicted
  N-terminal transit peptide [file:human/RSAD1/RSAD1-uniprot.txt].
- MitoCoP high-confidence mitochondrial proteome ("We defined a human mitochondrial
  high-confidence proteome (MitoCoP) of 1,134 protein-coding genes") includes RSAD1
  (GOA HTP row) [PMID:34800366].
- The bacterial orthologues are cytoplasmic/membrane-associated [PMID:22142238;
  PMID:37101575]; the eukaryotic protein has relocated to the mitochondrion, so
  `GO:0005737 cytoplasm` (the IBA transfer from bacterial donors, plus an InterPro
  mapping) is true only in the trivial sense that the mitochondrion is part of the
  cytoplasm, and `GO:0005739` is the supported term.

## A candidate catalytic activity (2026, not yet in GOA)

- A porcine/mouse picornavirus study reports that RSAD1 "catalyzes methionine
  oxidation of FMDV 3D polymerase and promotes its aggregation and subsequent
  degradation through the autophagy-lysosome pathway", with an in vitro oxidation assay
  using purified GST-RSAD1 vs a cluster-binding mutant (RSAD1-C3A) in SAM/dithionite
  buffer, SAM-domain dependence of the cellular effect, and Rsad1−/− mice being "more
  susceptible to FMDV-, EV71-, or EMCV-triggered death" [PMID:42736308].
- This is a single study, mostly in pig cells and mice, on a viral substrate, and the
  "oxidation" chemistry (net two-electron oxidation of a methionine thioether) is
  unusual for a radical SAM enzyme. Treated here as a lead and recorded in
  `suggested_questions`/`suggested_experiments`, **not** asserted as a new molecular
  function or as a defence-response process annotation for the human gene.

## Other associations (not annotation-grade)

- Rare-variant burden association of RSAD1 with chronic central serous
  chorioretinopathy in females only, explicitly needing replication [PMID:31036833].
- Differential neuronal expression in Alzheimer brain samples [PMID:34121475].
- Neither speaks to molecular function; not used in the review.

## Decisions taken in the review

- `GO:0004109 coproporphyrinogen oxidase activity` (IEA, InterPro IPR004559 →
  HemW-like): **REMOVE**. The mapping is from the HemW-like signature, and HemW is
  precisely the subfamily shown *not* to have this activity [PMID:22142238;
  PMID:29282292]; UniProt agrees.
- `GO:0006779 porphyrin-containing compound biosynthetic process` (IBA + IEA):
  **REMOVE**. The IBD node was placed where coproporphyrinogen dehydrogenase chemistry
  sits (donors are HemN-type bacterial/cyanobacterial proteins); the HemW/RSAD1 clade
  is a sister subfamily that does not perform that step. Heme *binding and delivery*
  is downstream of tetrapyrrole biosynthesis, so even the chaperone role does not place
  RSAD1 in porphyrin biosynthesis.
- `GO:0003824 catalytic activity`: **KEEP_AS_NON_CORE** per the project's treatment
  rule for generic rows — no reaction is established for RSAD1, so the root term is as
  precise as the evidence allows.
- `GO:0051536` → **MODIFY** to `GO:0051539`; the two `GO:0051539` rows →
  **KEEP_AS_NON_CORE**, since catalysis is not established (project rule), even though
  the cluster is required for heme transfer in the bacterial protein.
- `GO:0005737 cytoplasm` rows → **MODIFY** to `GO:0005739 mitochondrion`.
- No `NEW` rows. A heme-insertion/chaperone process term would require that the human
  protein itself be shown to perform the insertion; only binding has been shown for
  RSAD1, and the transfer assays are bacterial. The methionine-oxidation activity is a
  single non-human-cell study.
