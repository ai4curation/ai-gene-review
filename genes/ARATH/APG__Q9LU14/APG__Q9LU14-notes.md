# APG / AT3G16370 (UniProtKB:Q9LU14) notes

## Accession and name check (do this first — the symbol "APG" is ambiguous)

UniProt has **two** Arabidopsis entries whose gene name is `APG`:

- **P40602** (`APG_ARATH`, AT1G20130, 534 aa) — "Anther-specific proline-rich
  protein APG", the gene named by Roberts et al. 1993 (PMID:8401599). It has a
  long Pro-rich N-terminal extension (UniProt `COMPBIAS 59..196 Pro residues`).
- **Q9LU14** (`APG2_ARATH`, AT3G16370, 353 aa) — "GDSL esterase/lipase APG",
  AltName "Extracellular lipase APG". **This is the gene reviewed here.**

`just fetch-gene ARATH APG` resolves to P40602, so this review was fetched by
accession (`just fetch-gene ARATH Q9LU14 --alias APG__Q9LU14`) and the folder
uses the `SYMBOL__ACCESSION` convention (precedent: `genes/ARATH/AT4G38370__F4JTN4`,
`genes/PSEPK/aroE__Q88K85`). Q9LU14's "APG" name appears to be a family-based
carry-over from P40602 rather than a TAIR symbol; TAIR/Lai et al. call AT3G16370
**GGL19 / AtGELP67** [PMID:34621289, "GGL19"; table row "GGL19" / "AT3G16370" /
"AtGELP67"]. Recorded as a UniProt source defect (WRONG_NAME, POSSIBLE) rather
than corrected here.

## What is actually known about AT3G16370

Nothing about its biochemistry. The record is:

- **Family/architecture only.** 353 aa precursor, predicted signal peptide
  1..25, GDSL/SGNH fold: Pfam PF00657 `Lipase_GDSL`, CDD `cd01837
  SGNH_plant_lipase_like`, InterPro IPR001087/IPR035669/IPR036514, PANTHER
  `PTHR45642:SF35`. Catalytic triad positions Ser37 (nucleophile), Asp328,
  His331 are `ACT_SITE ... /evidence="ECO:0000250"` — by similarity, not
  measured. `EC=3.1.1.-` and the names "GDSL esterase/lipase APG" /
  "Extracellular lipase APG" are family-derived predictions, as are the
  keywords `Hydrolase`, `Lipid degradation`, `Lipid metabolism`.
  `PE 2: Evidence at transcript level`.
- **Secreted / apoplastic.** UniProt `CC SUBCELLULAR LOCATION: Secreted
  {ECO:0000305}`. TAIR has an HDA apoplast row (GO:0048046) from PMID:18538804
  (HILEP quantitative proteomics; abstract-only in our cache, so the protein
  identification cannot be quoted from it). Independently, Q9LU14/AT3G16370 is
  reported in three further apoplast proteomes: PMID:37876907 (apoplast washing
  fluid, SAR; table row "GGL19GDSL-motif lipase0.49"), PMID:25852701 and
  PMID:26862584 (Europe PMC `"Q9LU14"` → 5 hits, 2026-11-06). So the
  extracellular location is well supported by direct evidence; the enzymology
  is not.
- **Expression only.** The one paper that studies this gene specifically is
  PMID:34621289 (Xiao et al. 2021, guard-cell-enriched GDSL lipases). It is a
  promoter-GUS / localisation / mutant survey of 19 GGLs. For GGL19 it reports
  expression and nothing else: ["Ten members (GGL6, GGL8, GGL9, GGL13, GGL16,
  GGL19, GGL22, GGL23, GGL26, and GGL29) were highly expressed in cotyledons"],
  ["five GGLs (GGL5, GGL14, GGL17, GGL19, and GGL23) were also expressed in
  trichomes"], ["GGL19 was expressed in filaments and sepals"], and
  dehydration-repressed: ["the expression levels of GGL5, GGL6, GGL16, GGL19,
  GGL22, GGL23, and GGL29 were downregulated"]. GGL19 was **not** among the 13
  GGLs whose subcellular localisation was tested, and **not** among the mutants
  phenotyped (those were GGL7, GGL14, GGL22, GGL26).

Literature searches run 2026-11-06, none of which turned up any biochemical or
genetic characterisation: PubMed `At3g16370 OR "AT3G16370"` (0 hits); Europe PMC
full-text `"AT3G16370"` (17 hits — PMID:34621289 plus transcriptome/proteome
surveys: 40033544, 37752834, 37876907, 35567144, 25852701, 26862584, 19000166,
23031452, 32184371, 24682084, 31555307, 28250106, 20519339, 22291129, 36294998);
Europe PMC `"Q9LU14"` (5 hits, all proteomics). No enzyme assay, no substrate, no
mutant phenotype, no structure.

## Verdict on the GO:0008610 lipid biosynthetic process IBA

**The IBA does not hold for this gene. Action: MARK_AS_OVER_ANNOTATED.**

Evidence gathered specifically to test it (and *not* to confirm the prior
conclusion of `genes/PSEAE/estA`):

1. **Nothing on this gene supports it.** As above, the gene has no experimental
   function annotation of any kind and no primary literature beyond expression
   and apoplast proteomics. The EC number and the "lipase" in its name are
   predictions from the GDSL signature, so they cannot support a *biosynthetic*
   process either — ester hydrolysis is the opposite direction.
2. **The IBD sits at a LUCA node and its only seed is bacterial.** Topology
   re-checked with `projects/PSEUDOCAP/panther_tree.py node PTN005219546`
   (2026-11-06): PTN005219546 is `SPECIATION LUCA`, 960 leaves, splitting into
   PTN005219547 Eukaryota (952 leaves; PTN005219553 Viridiplantae 940,
   PTN008144646 Dikarya 12) and PTN005220548 Eubacteria (8 leaves). The
   GO:0008610 IBD has a single seed, *P. aeruginosa* EstA (UniProtKB:O33407);
   the GO:0052689 IBD at the same node has two (O33407, Q9HUP2). QuickGO
   (2026-11-06, GO:0008610 + ECO:0000318) returns 885 leaf IBAs from this node
   across 48 taxa, of which the large majority are plant GELPs (90 wheat, 57
   *B. napus*, 48 soybean, 40 *B. rapa*, 39 Arabidopsis, …) and only a handful
   bacterial/fungal. One indirect bacterial phenotype is being projected across
   a kingdom boundary.
3. **The seed is a necessity phenotype, not participation.** EstA's GO:0008610
   IMP (PMID:17631636) rests on an *estA* deletion making little rhamnolipid;
   rhamnolipid is assembled by RhlA/RhlB/RhlC, and UniProt itself says EstA's
   role is unclear. See `genes/PSEAE/estA/estA-notes.md`.
4. **But the clade is not empty of biosynthetic evidence — a correction to the
   estA review.** The estA review asserts that "the clade offers no positive
   evidence for a biosynthetic process" and that "No other member of the GDSL
   autotransporter esterase clade has evidence for lipid biosynthesis". That is
   **wrong**. `OSP1 / AT2G04570 / GELP47 / GGL14` (UniProtKB:Q9SJB4,
   PTHR45642:SF32) is a leaf of PTN005219546 — it carries the same two IBAs
   (GO:0008610 and GO:0052689, WITH `PANTHER:PTN005219546|UniProtKB:O33407`) —
   and it *is* characterised: [PMID:32542680 "significant reduction in leaf wax
   synthesis and occlusion of stomata, leading to"] in the mutant, and
   [PMID:32542680 "demonstrated that OSP1 possesses thioesterase activity,
   particularly on C22:0"] and C26:0 acyl-CoAs, with the authors placing OSP1
   upstream of CER3 in wax biosynthesis. TAIR curated that paper as MF
   GO:0016297 IDA and added **no** BP term, so GOA currently hides this.
5. **It still does not rescue the IBD, for three reasons.** (a) OSP1's role is
   lineage-specific angiosperm cuticular-wax metabolism, not a LUCA-level
   property; the seed asserts something else entirely (bacterial glycolipid).
   (b) The MRCA of OSP1 with this gene is PTN008693276, a 892-leaf DUPLICATION
   node — essentially the base of the plant clade — so even a plant-restricted
   IBD seeded from OSP1 would not be placed where this one is, and transfer to
   AT3G16370 would be the shallowest possible inference. (c) A survey of all 39
   Arabidopsis leaves of PTN005219546 (QuickGO, 2026-11-06) finds **no**
   experimental BP annotation anywhere in the clade; the only experimental rows
   are OSP1's GO:0016297 IDA, EXL1–6 extracellular/pollen-coat locations
   (PMID:11431566, PMID:32374882) and EXL3's ER IDA (PMID:34621289).

So: the honest reading is that the term is not demonstrably false for a secreted
plant GDSL enzyme (one clade member really does feed wax synthesis), but on this
gene it is an unsupported projection of a single indirect bacterial phenotype.
`MARK_AS_OVER_ANNOTATED` rather than `REMOVE`, with the node-level defect
recorded against GO_CENTRAL and the estA review's over-broad "no evidence in the
clade" claim flagged for correction.

Other GDSL enzymes with demonstrated *biosynthetic* roles are in **different**
PANTHER families, so they are irrelevant to this node (PANTHER cross-references
checked at UniProt, 2026-11-06): the five suberin-polymerising GELPs of
[PMID:33686223 "One is required for suberin synthesis, while the other can drive
suberin degradation"] are GELP22/AT1G54000 (Q1H583, PTHR45966), GELP38/AT1G74460
(Q9CA68, PTHR45648), GELP49/AT2G19050 (O64468, PTHR45650), GELP51/AT2G23540
(O80470, PTHR45648) and GELP96/AT5G37690 (Q9FHQ1, PTHR45650) — none of them in
PTHR45642, and none of them carrying a GO:0008610 IBA.

## Other annotation calls

- GO:0052689 carboxylic ester hydrolase activity IBA — **ACCEPT**, core. The
  second IBD at the same node has an experimentally grounded seed pair
  (EstA's esterase activity; ChoE/PA4921 cholinesterase IDA), and the SGNH
  triad is intact in this sequence. The term is as precise as the evidence
  allows: no substrate has been measured, so no descendant is warranted.
- GO:0048046 apoplast HDA — **ACCEPT**. Direct proteomic evidence, corroborated
  by three further apoplast proteomes.
- GO:0005576 extracellular region IEA — **ACCEPT**. Apoplast is not an `is_a`
  descendant of extracellular region in GO (checked via OLS: GO:0048046's
  ancestors are `cellular anatomical structure` / `cellular_component` only),
  so this row is not entailed by the apoplast row and is not `TOO_GENERAL`.
- GO:0003824 catalytic activity IEA(ARBA) and GO:0016788 hydrolase activity,
  acting on ester bonds IEA(InterPro) — **TOO_GENERAL**, both entailed by
  GO:0052689.
- GO:0009507 chloroplast ISM (AtSubP, GO_REF:0000122) — **REMOVE**. A
  sequence-model prediction that contradicts a cleavable signal peptide, a
  curated `Secreted` location and four apoplast proteomes. (The same predictor
  put the paralog P40602 in the nucleus; it is unreliable for this family.)

## Open questions / experiments

- Which ester does AT3G16370 hydrolyse in the apoplast? A purified-enzyme panel
  (p-nitrophenyl esters C2–C16, Tweens, monoacylglycerol, acyl-CoA, cutin/suberin
  oligomers, pectin acetyl esters) would turn the family-level MF into a
  substrate-level one.
- Does it, like OSP1, act on very-long-chain acyl thioesters? Its expression in
  trichomes, guard-cell-containing epidermis and sepals is cuticle-adjacent, so
  a wax/cutin phenotype in a higher-order mutant with its 171-leaf-clade
  relatives (PTN008145211, which also contains AT5G03810) is worth testing.
