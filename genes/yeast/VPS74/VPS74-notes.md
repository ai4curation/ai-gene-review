# VPS74 (Q06385, YDR372C) — curation notes

**Provenance note:** no deep-research provider API key was available in this
container, so `just deep-research` could not be run and there is no
`VPS74-deep-research-*.md` file. The literature below was read directly from the
cached `publications/PMID_*.md` records (most have `full_text_available: true`),
plus the UniProt flat file and SGD locus records. The GONUTS/CACAO wiki
(`gowiki.tamu.edu`) was queried on 2026-10-29 for `PMID:24019977` and
`PMID:18410729` and redirects to `maintenance.html` ("temporarily offline"),
matching the status recorded in `projects/CACAO.md`; both CACAO papers are
full-text cached here, so the wiki was not needed.

## Identity

- UniProt Q06385 `VPS74_YEAST`, 345 aa, *S. cerevisiae* S288C. Synonyms: MNN3,
  YDR372C. Orthologue of human GOLPH3/GPP34/GMx33/MIDAS and GOLPH3L.
- Pfam PF05719 GPP34; InterPro IPR008628 (GPP34-like); PANTHER PTHR12704.
  Crystal structures 2ZIH, 2ZII, 4TU3.
- Peripheral membrane protein on the **cytosolic** face of Golgi membranes
  [file:yeast/VPS74/VPS74-uniprot.txt "SUBCELLULAR LOCATION: Golgi apparatus, Golgi stack membrane"].
  Note PMID:24019977 calls it a "346-residue Vps74p polypeptide" while UniProt
  gives 345 aa; this is a trivial off-by-one in the paper, not a gene-model issue.

## Core mechanism: a cytosolic sorting receptor for Golgi glycosyltransferases

Schmitz et al. 2008 established the mechanism. Vps74p binds the short N-terminal
cytosolic tails of cis/medial Golgi mannosyltransferases
[PMID:18410729 "Vps74p binds strongly to the Kre2p fusion protein and significantly to a number of the other fusion proteins."],
assayed as GST fusions carrying the first 15 residues of KRE2, MNN2, MNN5 and
OCH1 (Fig. 3). Loss of VPS74 mislocalizes those enzymes to the vacuole
[PMID:18410729 "These results implicate Vps74p in specific retention of mannosyltransferases that reside in cis and medial Golgi compartments."],
while multi-TM Golgi proteins, TGN proteins and the ER glycosyltransferase Alg5p
are unaffected. The protein tetramerizes through a β-hairpin (197–208); deleting
it abolishes both tetramer formation and function.

Tu et al. 2008 independently defined a pentameric tail motif and showed Vps74p
also binds COPI
[PMID:18635803 "Here, we found that Vps74p bound to a pentameric motif present in the cytoplasmic tails of the majority of yeast Golgi-localized glycosyltransferases, as well as to COPI."],
proposing retention by promoting incorporation into COPI vesicles
[PMID:18635803 "We propose that Vps74p maintains the steady-state localization of Golgi glycosyltransferases dynamically, by promoting their incorporation into COPI-coated vesicles."].
The coatomer-binding determinant is an N-terminal arginine cluster
[PMID:22889169 "We identify a cluster of arginine residues at the N-terminal end of GOLPH3 proteins that are necessary and sufficient to mediate coatomer binding."],
and losing it inactivates retention without much affecting membrane binding
[PMID:22889169 "While loss of coatomer binding renders Vps74p non-functional for glycosyltransferase retention, the Golgi membrane-binding capabilities of the mutant protein are not significantly reduced."].

So the molecular function is a **cargo adaptor / sorting receptor** (GO:0140312):
one face reads glycosyltransferase cytosolic tails, another reads COPI, and the
GPP34 fold reads PtdIns4P.

## PtdIns4P binding and Golgi recruitment

Vps74p is a PI4K (Pik1) effector. Direct lipid binding was shown by dot blot
[PMID:20026658 "In a dot blot assay (Kavran et al., 1998; Stevenson et al., 1998), in vitro–translated radiolabeled Vps74 and GOLPH3 bind to immobilized PtdIns4P."]
and independently by Dippold et al.
[PMID:19837035 "Our data demonstrate that Vps74p binds PtdIns(4)P in vitro and is downstream of PIK1 in vivo."].
Golgi association requires ongoing PtdIns4P synthesis — in a `pik1-83ts` strain
[PMID:19837035 "EGFP-Vps74p dissociates from the Golgi within five minutes after shift to the non-permissive temperature"]
— and mutating the basic pocket (W88/R97, K178/R181) abolishes both binding and
function in vivo
[PMID:20026658 "Golgi mannosyltransferases that depend on Vps74 for Golgi localization are not retained in the Golgi in mutant cells that express a form of Vps74 that does not bind PtdIns4P."].

## Second, lipid-regulatory function: Vps74–Sac1

Wood et al. 2012 showed Vps74 binds the Sac1 phosphatase directly
[PMID:22553352 "Surface plasmon resonance (SPR) experiments employing untagged recombinant proteins indicated that Vps74 binds Sac1 (amino acids 2–521) with a KD value of 3.8 ± 0.4 μM (Figure 2B)."]
and that both are needed to keep medial-Golgi PtdIns4P low
[PMID:22553352 "These results indicate that both Vps74 and Sac1 function to maintain a low level of PtdIns4P on medial Golgi compartments."].
This is the evidence behind GO:0060304 (regulation of phosphatidylinositol
dephosphorylation, IMP with SAC1).

## Where in the Golgi?

Quantitatively, the steady-state pool is **cis/medial**, the opposite polarity to
PtdIns4P itself
[PMID:22553352 "Vps74 is enriched on cis and medial compartments of the Golgi."],
consistent with Schmitz et al.
[PMID:18410729 "N-terminally GFP-tagged Vps74p (GFP-Vps74p) localizes to the Golgi apparatus as judged by its co-localization with Arf1p-mCherry, Cop1p-mCherry, and Sec7p-mCherry"].
There is also a substantial soluble pool
[PMID:18410729 "A substantial amount of GFP-Vps74p is also seen in the cytosol"].
TGN co-localization is nonetheless real but partial
[PMID:19837035 "In yeast, EGFP-Vps74p colocalizes with the late Golgi marker Sec7p-dsRed (Figure S2B)."]
[PMID:24019977 "Wild-type Vps74p partially co-localized with Arf1p and Arl1p (Figures 2 and S1), indicating that Vps74p localizes to both the cis- and trans-Golgi networks."].

## Redundancy and partner pathways

Wang et al. 2020 found a parallel Bre5p/Ubp3p deubiquitinase retention pathway;
Ktr3p and Mnn4p need both, and the Vps74p requirement is nutrient-dependent
[PMID:32673164 "Moreover, Ktr3p and Mnn4p employ a dual retention mechanism that requires both Bre5p/Ubp3p as well as Vps74p for their robust Golgi retention."]
[PMID:32673164 "while Bre5p/Ubp3p was required for Mnn11p’s Golgi retention irrespective of the nutrient conditions under which the cells were grown"].

## CACAO rows (ASSIGNED BY = CACAO in VPS74-goa.tsv)

Four rows, two papers.

1. **GO:0005794 Golgi apparatus, IDA, PMID:24019977.** Figure 2 images
   GFP-Vps74p against Arf1p-mRFP and Arl1p-mRFP. Term matches the assay
   exactly. → ACCEPT.
2. **GO:0005802 trans-Golgi network, IDA, PMID:19837035.** Figure S2B,
   EGFP-Vps74p vs Sec7p-dsRed in yeast. Supported, but the quantitative
   cisternal profiling in PMID:22553352 puts the steady-state peak on cis/medial,
   so the TGN is a real but peripheral location. → KEEP_AS_NON_CORE.
3. **GO:0006487 protein N-linked glycosylation, IMP, PMID:18410729.** Figs 1A–1C
   (pulse-chase of secreted proteins, invertase mobility ± PNGase F, mCPY).
   Real data, but the paper itself says the role is indirect
   [PMID:18410729 "Since Vps74p exists on the cytosolic side, and protein glycosylation occurs on the luminal side of secretory organelles, the role that Vps74p plays in glycosylation must be indirect."].
   Classic phenotype-read-as-process: the mechanism is GO:0045053, annotated by
   SGD from the same paper. → MARK_AS_OVER_ANNOTATED.
4. **GO:0035269 protein O-linked glycosylation via mannose, IMP, PMID:18410729.**
   Fig. 1D, Hsp150p-HA mobility. Same shape as (3). → MARK_AS_OVER_ANNOTATED.

So two of four CACAO rows are sound localizations read off real images, and two
are the same downstream phenotype term pair. No wrong-gene, wrong-organism or
sign-inversion problems here; the student picked the right papers and the right
evidence codes.

## Other rows worth flagging

- **GO:0005634 nucleus, HDA, PMID:14562095** — from the genome-wide GFP
  localization screen. No subsequent study reports nuclear Vps74p; the soluble
  pool is cytosolic. Over-annotation, not removable from an abstract.
- **GO:0030968 ER unfolded protein response, IMP, PMID:16582425** — a
  genome-wide Opi⁻ screen; the authors' own reading is indirect
  [PMID:16582425 "This suggests that VPS74 is required for the function/expression of either HAC1 or IRE1 ( Figure 9 )."].
- **GO:0006890 retrograde vesicle-mediated transport, Golgi to ER, IMP,
  PMID:18635803** — the abstract describes intra-Golgi COPI recycling, not
  Golgi→ER traffic; GO:0000301 is the better fit. Abstract-only, so a lateral
  MODIFY rather than REMOVE.
- **GO:0043001 Golgi to plasma membrane protein transport, IBA** — driven by
  mammalian GOLPH3/MYO18A, and yeast has no MYO18A orthologue
  [PMID:19837035 "In mammals, we observe that GOLPH3 functions through its interaction with MYO18A, but the S. cerevisiae genome does not encode an ortholog of MYO18A, having only type I, II, and V myosins (Berg et al., 2001)."].
  Bulk secretion is not grossly impaired in vps74Δ
  [PMID:18410729 "although the number of proteins and their relative abundances are similar"].
- **GO:0019899 enzyme binding, IPI ×4 (MNN2 S000000219, KRE2 S000002891,
  OCH1 S000003006, MNN5 S000003722)** — the Fig. 3 GST pull-downs. True but
  uninformative; the informative MF is GO:0140312 cargo adaptor activity.
