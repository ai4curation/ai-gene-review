# Bunyamwera virus NSs (UniProt P16494) — curation notes

## Scope and identity caveat

This folder reviews **P16494 = NSs**, the 101-aa non-structural protein of
Bunyamwera virus (BUNV). UniProt files the entry under gene name `N` because NSs is
translated by alternative initiation from the S-segment mRNA in a reading frame that
overlaps the nucleocapsid (N) ORF: "Produced by alternative initiation in the N gene,
but encoded on another frame" (`N__P16494-uniprot.txt`, `CC ALTERNATIVE PRODUCTS` /
`CC MISCELLANEOUS`). The nucleocapsid protein N itself is a different entry
(P16495). Per CLAUDE.md's alternative-ORF rule the folder is
`genes/BUNYW/N__P16494/` with `gene_symbol: N` and `id: P16494`.
Everything below is about NSs, not about N.

Confusion risk is real in the literature: PMID:19193790 (poly(A)-independent
translation / PABP1 nuclear retention) attributes PABP1 binding to the
**nucleocapsid protein N**, not to NSs ("the viral nucleocapsid protein binds to,
and colocalizes with, PABP in the cytoplasm early in infection, followed by nuclear
retention of PABP"), even though UniProt's P16494 FUNCTION block cites that paper for
"NSs also seems to be involved in the nuclear relocalization of host PABP1". That
UniProt sentence looks like a gene-attribution slip and is not used as support for any
NSs annotation here.

## Deep research availability

No deep-research provider keys are available in this container, so
`just deep-research` was not run and no `-deep-research-<provider>.md` file exists.
Literature below was assembled by hand from the cached publications, PubMed search
(PubMed MCP) and UniProt. The GONUTS/CACAO wiki was checked for the student evidence
behind the CACAO rows: `https://gowiki.tamu.edu/wiki/index.php/PMID:15150262` returns
only "This site is temporarily offline while we perform upgrades", so no CACAO
annotation worksheet could be consulted (2026-10-29).

## What NSs does

**Accessory, non-essential virulence factor.** Reverse genetics gave BUNdelNSs, a
virus that makes no NSs: "The generation of viruses lacking the NSs gene shows
conclusively that the product is not essential for replication in either cultured
cells or in mice, and thus NSs can be designated as an accessory protein"
[PMID:11209062 "shows conclusively that the product is not essential for replication in either cultured
 cells or in mice, and thus NSs can be designated as an accessory protein"].
Attenuation in mice: "Eleven of the 12
 mice inoculated i.c. with wt BUN were dead or moribund and had to be
 killed by 4 days after infection, whereas most of the mice inoculated
 with BUNdelNSs survived for at least 3 days longer." [PMID:11209062]

**Host-cell gene-expression (protein synthesis) shutoff.** "At 48 h after
 infection, host cell protein synthesis was almost completely shut
 off in wt BUN-infected BHK cells. In contrast, in BUNdelNSs-infected
 cells, host cell protein synthesis was reduced compared with
 mock-infected cells but not inhibited to the same extent as in
 wt-infected cells." [PMID:11209062, Fig. 4B, 35S-methionine labelling].
Shutoff is reduced but not abolished without NSs, so more than one pathway
contributes: "The reduction, but not the abrogation, of host cell protein shutoff by
 BUNdelNSs suggests also that more than one pathway may be involved." [PMID:11209062].
Shutoff is mammalian-cell specific: "This process is clearly highly cell specific, because neither wt BUN
 ( 36 ) nor BUNdelNSs (data not shown) shuts off host cell protein
 synthesis in mosquito cells." [PMID:11209062]

**Mechanism: block of RNA polymerase II CTD Ser2 phosphorylation.** "In BUNV-infected mammalian cells, serine 5 phosphorylation occurred normally. Furthermore, RNAP
II was able to bind to the IFN-beta gene promoter as revealed by chromatin
immunoprecipitation analysis, indicating that the initiation of transcription
was not disturbed by NSs. However, NSs prevented CTD phosphorylation at serine
2, suggesting a block in transition from initiation to elongation."
[PMID:15150262 (abstract only in cache)]. The same paper notes the block is
mammalian-specific: "Surprisingly,
no interference with CTD phosphorylation was observed in insect cells."
[PMID:15150262]. Recapped in the MED8 paper: "NSs, independently of other viral proteins, inhibited phosphorylation at serine 2 in the heptapeptide repeat (YSPTSPS) of the CTD of RNA polymerase II, suggesting that the elongation step of transcription and/or 3′-end processing was prevented."
[PMID:16973571]

**Mechanism: NSs binds the Mediator subunit MED8.** Yeast two-hybrid plus
co-immunoprecipitation; interaction domain mapped to NSs aa 81–93; a recombinant
virus truncated there (BUNNSs-T83) behaves like BUNdelNSs:
"The region encompassing amino acids 81 to 93 of NSs was shown to be essential for the interaction."
and "Wild-type BUNV efficiently inhibited transcription from the CMV promoter, whereas BUNdelNSs2 and BUNNSs-T83 had no major effect on RNA polymerase II activity compared to mock infection"
and "an RT-PCR signal specific for IFN-β mRNA was detected only in cells infected with BUNdelNSs or BUNNSsT83 virus, and no signal was detected in cells infected with wt BUNV or in mock-infected cells"
[PMID:16973571]. Also RNAP II is destabilised late in wt infection: "RNA polymerase II levels decreased over time in wt BUNV-infected cells, while the protein appeared considerably more stable in BUNdelNSs2-infected cells."
[PMID:16973571]. The NSs N-terminus matters too, independently of MED8 binding:
"Strikingly, despite encoding an NSs protein that contains the Med8 interaction domain, mBUNNSs22 fails to block RNA polymerase II activity during infection."
[PMID:20427562]

**Interferon: NSs blocks IFN *induction*, not IFN *signalling*.** The 2001 paper used
an IFN-β promoter–luciferase reporter: "there was approximately 20-fold
 increase in luciferase activity in cells infected with BUNdelNSs,
 indicating strong activation of the IFN-β promoter" and "the loss of NSs changed BUN from a
 noninducer to an inducer of IFN." [PMID:11209062, Fig. 7A]. Direct IFN/IFN-mRNA
measurement: "we demonstrate that BUNdelNSs is a strong inducer of IFN-alpha/beta, whereas in cells infected with the wild-type counterpart expressing NSs (wild-type BUN), neither IFN nor IFN mRNA could be detected"
and "These results suggest that BUN NSs is an IFN induction antagonist that blocks the transcriptional activation of IFN-alpha/beta in order to increase the virulence of Bunyamwera virus."
[PMID:12133999]. Upstream sensing is *not* blocked — IRF-3 and NF-κB activation still
occur, and NSs does not inhibit the dsRNA-activated effectors: "NSs is different from other IFN antagonists, since it inhibits dsRNA-dependent IFN induction but has no effect on the dsRNA-activated PKR and RNase L systems."
[PMID:12692253]. This matters for GO term choice: nothing in this literature tests the
**type I interferon-mediated signalling pathway** (IFNAR → JAK–STAT), which is what
GO:0039502 is defined as ("A process in which a symbiont interferes with, inhibits or
disrupts a type I interferon-mediated signaling in the host organism"; it sits under
GO:0052029 *symbiont-mediated suppression of host signal transduction pathway*).
The claim that is actually supported is suppression of IFN-β **gene transcription**,
i.e. GO:0039523 for the mechanism plus GO:0052170 *symbiont-mediated suppression of
host innate immune response* for the outcome.

**Effect on viral N protein levels.** "Quantification of
 this gel by using a PhosphorImager indicated that approximately 10
 times more N protein was produced in cells infected with BUNdelNSs
 compared with wt BUN." [PMID:11209062, Fig. 4A]. So NSs *lowers* the level of a
viral protein in the infected cell (GO:0046725), most plausibly as a side-effect of
the general transcription/translation block; it does not promote viral gene
expression. This is why the CACAO row `GO:0019080 viral gene expression` (IMP,
PMID:11209062) points the wrong way.

**Localisation.** Mostly cytoplasmic with some nuclear signal:
"NSs has a predominantly cytoplasmic distribution, though a proportion can also be detected in the nuclei of cells transfected with an NSs-expressing plasmid"
[PMID:16973571]; ambisense-segment viruses expressing tagged NSs confirm "NSs was shown to localize to both the nucleus and the cytoplasm during infection"
[PMID:25740985, abstract; not cited in the review]. No GOA CC row exists and no CC
`NEW` row is proposed: a nucleus/cytoplasm claim from tagged/transfected NSs is one
line of evidence and the review stays silent rather than asserting it.

## CACAO row-by-row reading (ASSIGNED BY = CACAO, from `N__P16494-goa.tsv`)

| Term | Ev | PMID | What the paper shows | Verdict |
|---|---|---|---|---|
| GO:0039523 RNAP II inhibition | IMP | 15150262 | NSs blocks CTD Ser2 phosphorylation; Ser5-P and promoter binding intact | matches exactly; ACCEPT |
| GO:0039502 type I IFN-mediated signalling | IDA | 15150262 | IFN-β *transcription* block via RNAP II; no IFNAR/JAK-STAT assay | wrong branch (induction vs signalling); MODIFY → GO:0052170 |
| GO:0039502 type I IFN-mediated signalling | IMP | 11209062 | IFN-β promoter-luciferase induced 20-fold in BUNdelNSs (Fig. 7A) | same wrong branch; MODIFY → GO:0052170 |
| GO:0039657 suppression of host gene expression | IMP | 11209062 | host protein synthesis shutoff impaired in BUNdelNSs (Fig. 4B) | matches; ACCEPT |
| GO:0019080 viral gene expression | IMP | 11209062 | BUNdelNSs makes ~10× *more* N protein (Fig. 4A) | sign inverted; MODIFY → GO:0046725 |
| GO:0046725 negative reg. of viral protein levels | IMP | 11209062 | same 10× N increase | holds, but a consequence of global shutoff; KEEP_AS_NON_CORE |

CACAO failure-taxonomy notes for `projects/CACAO.md`:

- **New pattern — inverted sign / phenotype read as the forward process.** `GO:0019080
  viral gene expression` (IMP, PMID:11209062) was written from the observation that
  deleting NSs *raises* viral N protein. The knockout-phenotype logic ("NSs affects
  viral gene expression") lost the direction; GO's own `involved_in` reading makes
  this a positive contribution to viral gene expression, which is the opposite of the
  data. The same student team also entered GO:0046725 from the same figure, which is
  the correct-signed term, so the two rows contradict one another.
- **Adjacent-branch substitution (wrong granularity of a different kind).** Both
  `GO:0039502` rows read "blocks interferon" as "blocks interferon *signalling*". The
  two sit in different GO branches (suppression of host signal transduction vs
  suppression of host transcription / innate immune response), and no paper on BUNV
  NSs assays IFNAR-driven signalling. This is a plausible-label trap rather than a
  phenotype-as-process error.
- The remaining CACAO rows (GO:0039523, GO:0039657, GO:0046725) are sound, and
  GO:0039523 is an unusually good student annotation: a deep, mechanism-specific term
  that matches the paper's central result.
- For this gene product the CACAO rows are the **only** experimental GO annotations;
  the other three rows are IEA from InterPro and UniProt keywords.
