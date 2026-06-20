---
title: "IBA Annotation Quality — History, Methodology & Lessons"
---

# IBA Annotation Quality — History, Methodology & Lessons

[← back to the findings page](../IBA_REVIEW.md)

This is the working log for the IBA quality project. The main page holds the
**findings**; this page holds the **process**: the dated log, how each candidate
was verified, what got retracted, and — most importantly — the lessons I want my
future self to apply before ever flagging an IBA as wrong.

---

## Lessons learned (read this before flagging any IBA)

These are written to myself. The recurring failure mode is **acting on one line of
evidence**. Flagging a curated IBA as wrong is a strong claim; treat it like one.

1. **No single source is sufficient — synthesize.** A review YAML assertion, a
   UniProt keyword, and a PANTHER node label are each individually weak. Before
   REMOVE, I should have at least two independent lines pointing the same way
   (e.g. UniProt CAUTION *and* direct enzymology; a curated NOT *and* the term
   definition).

2. **Read the GO term *definition*, not the label.** My worst miss: I called
   ATP7B's `GO:0015677` "copper ion import" a direction inversion because ATP7B is
   a copper *exporter*. But the definition is "movement into a cell **or
   organelle**," and ATP7B pumps Cu into the Golgi lumen — so the term is
   defensible. The label looked opposite; the definition was not. **Always fetch
   the definition (QuickGO/OLS) for any "directionally wrong" claim.**

3. **"By similarity" is weak; direct experiment in the target species beats it.**
   My second miss (in the *other* direction): I retracted the AGK ceramide/sphingosine
   flags because UniProt "curates" them — but the ceramide claim was only a
   propagated "By similarity" tag, UniProt *also* says "Does not phosphorylate
   sphingosine," and two papers (PMID:15939762, PMID:16269826) report no
   ceramide/sphingosine activity. Deferring to the keyword was exactly backwards.
   **Check the evidence code behind the UniProt statement (ECO:0000250 "by
   similarity" vs ECO:0000269 experimental) and read the cited paper.**

4. **Don't misread fragmented tool output.** I mis-paraphrased UniProt's "Does not
   phosphorylate sphingosine" as "phosphorylates sphingosine" from a line-wrapped
   `grep`. **Read the full FUNCTION block (`sed -n '/FUNCTION/,/-!-/p'`), not a
   keyword grep, before quoting it.**

5. **Use phylogeny / the PANTHER family composition.** Over-propagation almost
   always traces to a family node that lumps members of different
   function/specificity. Inspecting the family pays off: PTHR12358 mixes
   acylglycerol *and* sphingosine kinases (explains AGK); PTN000135648 mixes pro-
   and anti-apoptotic BCL2 members (explains the BCL2 sign error); PTN000222418
   lumps HMGCS paralogs (explains HMGCS2). **Always look at the IBA WITH/FROM and
   what the node contains.**

6. **Distinguish "absent" from "over-annotated/non-core".** HMGCS2 really does
   catalyze the HMG-CoA-synthase step (the mevalonate-pathway entry reaction); what's
   wrong is assigning it the *downstream FPP/isoprenoid* flux that belongs to the
   cytosolic paralog. That's a paralog over-annotation, not a fabricated activity —
   so the framing must be precise (over-annotation), not "it can't do this."

7. **Respect the curator (CLAUDE.md).** REMOVE is for IBA/IEA inferences I can argue
   against on biological grounds — not for second-guessing experimental annotations
   whose full text I haven't read. When I genuinely can't adjudicate, UNDECIDED.

8. **A label that "looks" like a name collision needs the WITH/FROM to confirm the
   cause.** PEX2 is biologically not in the Cdc73/Paf1 complex (solid), but the
   "old synonym PAF1" *mechanism* is unverified — the WITH/FROM is a PANTHER node,
   not a PAF1 gene. Separate "this is wrong" (provable) from "this is *why* it's
   wrong" (often a hypothesis).

9. **Read the WITH/FROM column before anything else.** It names the exact source
   proteins the IBA was transferred from. If they are the wrong family (NTN1's TF
   terms came from POU2F1/POU1F1/POU4F1; NOTCH1's axon guidance from SLIT1/2/3) or
   a single wrong paralog (ABRAXAS1's spindle terms from ABRAXAS2/Q15018; HINT2's
   cytoplasm from HINT1), that is near-mechanical evidence of error. If they are a
   broad, coherent set of true orthologs, the transfer is probably fine. I should
   pull WITH/FROM on *every* candidate, not just the puzzling ones.

10. **Uncertain ≠ wrong — leave the borderline ones (UQCRC1).** I nearly added
    UQCRC1 as a "pseudo-peptidase," but UniProt says the bc1 core subunits *"seem to
    have preserved their MPP processing properties (By similarity)"* and *"may be
    involved in"* processing UQCRFS1. That is genuinely unresolved, so the right call
    is UNDECIDED, not a confident REMOVE. Excluding it was the disciplined choice.

11. **For localization, place both compartments in the GO hierarchy first.**
    `GO:0005737` cytoplasm is defined as "the contents of a cell excluding the plasma
    membrane and nucleus, but including other subcellular structures" — and
    mitochondrion, ER, Golgi, and lysosome are all `part_of` cytoplasm. So "cytoplasm"
    is *not wrong* for a mitochondrial/ER/lysosomal protein (just imprecise); flagging
    it REMOVE is an over-reach. Valid localization REMOVEs need **mutually-exclusive**
    compartments: nucleus vs cytoplasm, plasma membrane vs internal, one organelle vs
    another. This is the same "read the definition" trap as ATP7B's copper import.

12. **Check taxon/lineage appropriateness for process terms.** The single biggest BP
    error class is processes transferred across kingdoms to organisms where they don't
    exist: inflammatory response on a mosquito Toll (from human TLR4), JAK-STAT on a
    worm (no JAK), aerobic respiration on chloroplast NDH subunits, smell perception
    on mosquito salivary OBP-fold proteins. The WITH/FROM naming a vertebrate/Drosophila
    source is the tell; GO taxon constraints catch some. Always ask "does this process
    occur in this lineage / this organelle system?"

---

## 2026-06-20 (d) — Fifth pass: biological-process cluster

Triaged the 53 BP REMOVE candidates (44 genes). Verified each flagship against UniProt
+ WITH/FROM + (where cited) cached papers. Two new patterns, two reinforced.

**New Pattern 14 — lineage-inappropriate / cross-kingdom process transfer** (largest BP
class): TOLL9 inflammatory response ← human TLR4 (O00206); ndhA/D/K aerobic respiration
(UniProt: chloroplastic NDH, plastid); che-3 cilium motility (dynein-2 IFT; worm cilia
non-motile); D7r2/r4/r5/L1 smell perception (UniProt: blood-feeding salivary proteins);
sta-2 JAK-STAT (no JAK in worms; from fly/mouse STATs); fshr-1 hormone signaling (no
gonadotropins); HEN1 piRNA processing (plant; metazoan over-transfer); DpuGr29 male
courtship (Drosophila-specific term).

**New Pattern 15 — regulator/effector & direct/downstream conflation**: lys-7 (AMP
effector, not a signal transducer); SIR3 (represses origins ≠ replication initiation);
UBP3 (regulation of protein stability is downstream of its DUB activity).

**Reinforced Pattern 8 (sub-activity)**: worm pseudo-sHSPs — hsp-12.3/hsp-12.6 have *no*
chaperone activity (PMID:9744800 title verbatim), stronger than CRYAA. **Reinforced
Pattern 12 (mis-grouping)**: opa1/eat-3 peroxisome fission on mitochondrial-fusion OPA1
(DRP1-branch transfer); YAR1 transcription term on an RPS3-binding 40S-biogenesis factor;
ACL4 mito-import by TOM70-family over-transfer; plus BP versions of the PIWI/germ-granule
cluster (pgl-1 mRNA splicing/export, glh-4 SSU-rRNA maturation).

**Noted but not separately featured (paralog conflation, already a known pattern):**
mid1←mid2 (septin ring), Ang2←angiogenin/AMP paralogs, csr-1 (cell-differentiation IBA
traceable to a nuclear-receptor node, not the Argonaute — a wrong-grouping case I left
out pending tighter confirmation of the source).

---

## 2026-06-20 (c) — Fourth pass: the generic-localization cluster (two-sided)

Triaged the 32 generic-localization REMOVE candidates (cytoplasm 10, nucleus 7,
plasma membrane 6, mitochondrion 2, membrane 2, cytosol 2, peroxisome/Golgi/nucleoplasm
1 each). First fetched the **GO:0005737 definition** — it subsumes membrane-bounded
organelles — which split the cluster cleanly:

**Valid REMOVEs (mutually-exclusive compartment) → added as Pattern 13 Tier A:**
nucleus on cytoplasmic PIWI/Argonaute (PIWIL1, prg-1, wago-1, glh-1; WITH/FROM
includes nuclear-acting Piwi orthologs), nucleus on ER-kinase EIF2AK3 and on BIRC6,
plasma membrane on ribosome-associated chaperones SSB2/SSZ1, nucleoplasm on BAIAP2L2,
peroxisome on PIK3C3, cytoplasm on strictly-nuclear rqh1/HDA1, cytoplasm on secreted
SCGB1A1.

**Reviewer over-reaches (cytoplasm subsumes the organelle) → Pattern 13 Tier B, NOT
flagged:** "cytoplasm" REMOVE on Aga/GLA (lysosome), DHCR24 (ER), ISCA1/ATP5IF1/gtpbp3
(mito); "membrane" REMOVE on flvcr2a (a multi-pass membrane transporter). These
should be UNDECIDED/KEEP.

**Self-correction:** HINT2 (added in pass (b) as a wrong-paralog "cytoplasm" case) is
itself a Tier-B over-reach — mitochondrion ⊂ cytoplasm, so "cytoplasm" isn't strictly
wrong. Removed HINT2 from the findings table.

Net lesson: localization is where reviewers (me included) most often over-flag, because
"cytoplasm"/"membrane" are broad subsuming terms. Roughly a third of this cluster were
reviewer over-reaches rather than bad IBAs.

---

## 2026-06-20 (b) — Third pass: WITH/FROM-driven triage of the backlog

Worked through more of the ~167 un-triaged REMOVE candidates, this time leading
with the WITH/FROM column and confirming each against UniProt + family. Added 11
verified examples and **two new patterns** (mis-grouping revealed by WITH/FROM;
extended pseudo-enzyme + substrate/neofunctionalization sets).

**Added (verified):**
- **Pseudo-enzyme** — **AKTIP** (UniProt CAUTION: *"Lacks the conserved Cys residue
  necessary for ubiquitin-[conjugation]"*; UEV pseudo-E2) and **DPYSL4** (fourth
  CRMP-family member on the same non-catalytic basis as DPYSL2/3/CRMP1).
- **Substrate / neofunctionalization** — **SAMD8/SMSr** (UniProt: makes ceramide
  phosphoethanolamine from PE, not sphingomyelin from PC — *"The larger PC prevents
  an efficient fit in the enzyme's catalytic pocket"*) and **CPT1C** (UniProt RecName
  *"Palmitoyl thioesterase CPT1C"*; lost the ancestral carnitine-transferase activity).
- **Mis-grouping (WITH/FROM-confirmed)** — Tier A wrong-family: **NTN1/NTN3** (secreted
  Netrins carrying POU-domain TF terms; WITH/FROM = POU2F1 P14859, POU1F1 P28069,
  POU4F1 Q12837, POU4F3 Q15319), **NOTCH1** (axon guidance from SLIT1/2/3
  O75093/O94813/O75094), **IL23R** (prolactin-receptor activity from PRLR P16471).
  Tier B wrong-paralog: **ABRAXAS1** (spindle/MT from ABRAXAS2 Q15018), **HINT2**
  (cytoplasm reflects HINT1).

**Examined and deliberately NOT added (insufficiently certain):**
- **UQCRC1 / `GO:0017087` (MPP complex)** — UniProt: core subunits *"seem to have
  preserved their MPP processing properties (By similarity)"* and *"may be involved
  in"* UQCRFS1 processing. Residual activity is unresolved → UNDECIDED, not REMOVE.

**Still in the backlog (not yet adjudicated):** many generic localization
over-propagations (`GO:0005737` cytoplasm / `GO:0005634` nucleus on DHCR24, PIWIL1,
BIRC6, EIF2AK3, GLA, GK5, SCGB1A1, …) — these look like a high-frequency "default
compartment" category worth a dedicated future pass; CRY1/CRY2 photo-entrainment
(contested); ankzf1 ERAD-vs-RQC; CALCOCO2 PML-body; BAIAP2L2 nucleoplasm.

---

## 2026-06-20 — Second corpus pass (+ verification)

**Method.** Mined all 2,732 `genes/*/*/*-ai-review.yaml` for IBA-evidence
annotations and their review action. Distribution:
`ACCEPT 4651 · KEEP_AS_NON_CORE 943 · MODIFY 321 · MARK_AS_OVER_ANNOTATED 189 ·
REMOVE 190 · UNDECIDED 39 · NEW 33 · PENDING 11`. Shortlisted ~12 REMOVE candidates
and verified each against: UniProt `*-uniprot.txt` (FUNCTION block + evidence codes),
the GO term definition (QuickGO), GOA `*-goa.tsv` WITH/FROM provenance and PANTHER
family composition, cached `publications/`, and the gene `-notes.md`.

**Verification first pass — over-retracted three, then corrected on review:**

| Gene | First call | Why first call was wrong | Final |
|------|-----------|--------------------------|-------|
| ATP7B `GO:0015677` | flag → then retract | n/a — retraction was correct | **Stays out.** Term covers organelle import; ATP7B loads Cu into Golgi. Not a direction error. |
| AGK ceramide/sphingosine | flag → retract | I deferred to a UniProt "By similarity" keyword and **misread** "Does not phosphorylate sphingosine" | **Reinstated.** Two papers (PMID:15939762, PMID:16269826) + UniProt's own "does not phosphorylate sphingosine" refute the activity; ceramide is only "By similarity". |
| HMGCS2 `GO:0010142` | flag → retract | I deferred to UniProt's UniPathway "mevalonate biosynthesis" tag (shared reaction chemistry) | **Reinstated as paralog over-annotation.** FPP/isoprenoid flux belongs to cytosolic HMGCS1; mito HMGCS2 → ketogenesis. |

**Final verified additions (on the findings page):** pseudo-enzyme cluster
(DPYSL2/CRMP1/DPYSL3, AGO4, UBAC2), partial sub-activity loss (CAPG, CRYAA),
regulatory-sign inversion (BCL2, with caveat), complex/compartment/pathway
over-transfer (EIF4E2, ALDH1L1, HMGCS2, PEX2), substrate over-propagation (AGK).

**Evidence anchors per gene:**
- **DPYSL2/CRMP1/DPYSL3** — UniProt CAUTION: *"Lacks most of the conserved residues … essential for binding the metal cofactor"*.
- **AGO4** — UniProt FUNCTION: *"Lacks endonuclease activity and does not appear to cleave target mRNAs"*.
- **UBAC2** — rhomboid-*like* fold (inactive-rhomboid clan) + no curated protease activity (no explicit CAUTION → kept MEDIUM/cautious).
- **CAPG** — cached PMID:1322908 verbatim *"blocks the barbed ends … but does not sever preformed actin"*.
- **CRYAA** — GOA already contains a curated `NOT|involved_in` (ISS) to `GO:0042026` (refolding) that the IBA contradicts.
- **BCL2** — WITH/FROM node PTN000135648 mixes pro-apoptotic BAX (Q07812)/BAK1 (Q16611) with anti-apoptotic members; caveat: a separate NAS annotation to the same term exists + context-dependent pro-apoptotic roles → "IBA sign unreliable," not "impossible".
- **EIF4E2** — UniProt: *"is unable to bind eIF4G"*, *"Does not interact with eIF4G"*.
- **ALDH1L1** — UniProt *Cytosolic 10-formyltetrahydrofolate dehydrogenase*, `Cytoplasm, cytosol`, cytosol IDA; mito work is ALDH1L2.
- **HMGCS2** — IBA from PANTHER node PTN000222418 lumping HMGCS paralogs; notes reason out ketogenesis vs cytosolic mevalonate.
- **PEX2** — UniProt: peroxisomal RING E3 for PEX5 retrotranslocation; WITH/FROM is a PANTHER node (name-collision cause unverified).
- **AGK** — PTHR12358 mixes acylglycerol + sphingosine kinases; direct human enzymology (PMID:15939762, PMID:16269826) shows MAG/DAG only.

**Backlog (~175 un-triaged REMOVE-flagged IBAs)** — verify each the same way before
adding: e.g. PIWIL1 piRNA cross-aspect, human/CRY1 & human/CRY2 photo-entrainment,
ankzf1 ERAD vs RQC.

---

## 2026-03-04 — Added ECOLI/arnF (mechanism divergence within SMR superfamily)

PTHR30561 groups the whole SMR/DMT superfamily — EmrE (drug efflux), MdtI/J
(spermidine export), Gdx (guanidinium export), Mmr (multidrug resistance), and
ArnE/ArnF (lipid flipping). Same 4-TM fold, but ArnE/ArnF do intramembrane lipid
translocation rather than transmembrane solute export. The IBA WITH/FROM for
`GO:0022857` (transmembrane transporter activity) lists EmrE (P23895), MdtI
(P69210), MdtJ (P69212), Gdx (P69937), Mmr (P9WGF1), ArnE (Q47377) + ArnF — all
genuine exporters, correct for them but misleading for the flippase. Correct term:
`GO:0140303` (intramembrane lipid transporter activity). Severity MEDIUM: the IBA
isn't wrong in kind (it *is* a transporter), just wrong in mechanism. EcoCyc also
contributed two "response to iron(III) ion" over-annotations (IGI PMID:12139617,
IEP PMID:15322361) that conflate BasS-BasR transcriptional regulation of the arn
operon with direct function.

## 2026-01-26 — Added cds1 (neo-functionalization, opposite reaction) + RIMBP2

**cds1 (PTHR10314 SF135)** — the most severe error type: `GO:0019344` (cysteine
*biosynthesis*) propagated from the family root (PTN000034104) to a subfamily that
catalyzes cysteine *catabolism* (EC 4.4.1.1: L-Cys → H2S + pyruvate). Evidence of
neo-functionalization in SF135: longest branch length (0.528), different EC class,
~24% identity with synthases (synthases share 43%), distinct active-site motif
(ASSGST vs PTSGNTG). Experimental: PMID:34439535 (M. tuberculosis), PMID:34283874
(V. cholerae). Detail: `interpro/panther/PTHR10314/PTHR10314-notes.md`.

**RIMBP2** — organism/tissue context transfer: `GO:0007274` (neuromuscular synaptic
transmission) transferred from the Drosophila ortholog (FB:FBgn0262483, NMJ is the
fly model), but human RIMBP2 acts at central synapses (hippocampal mossy fiber,
CA3-CA1, auditory ribbon). Family PTHR14234 also contains non-synaptic RIMBP3 (SF21,
testis/spermiogenesis); the family research warns against propagating
"regulation of neurotransmitter release" to RIMBP3 paralogs.

## 2026-01-22 — Project creation (Epe1)

Documented IBA quality issues found through AI review. First key finding:
**pseudo-enzyme propagation** — Epe1 has a JmjC fold but an HVD (not HXD) motif and
lacks Fe(II) coordination; mass-spec assays show no demethylation; the H297A
catalytic mutant retains anti-silencing function. So the demethylase IBA
(`GO:0032452`) should be REMOVE. Recommendation that seeded the project: build a
pipeline to flag IBA enzymatic annotations on proteins with degenerate active-site
motifs.
