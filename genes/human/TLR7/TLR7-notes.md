# TLR7 (human, Q9NYK1) — curation notes

Batch 1 of the INNATE_IMMUNITY project (Toll/TLR axis). Reviewed alongside TLR8
(Q9NR97), with which TLR7 shares most of its annotation set and its PAINT node.

**Deep research:** `TLR7-deep-research-falcon.md` (Falcon) arrived after the
review was written; see the cross-check section at the end. The notes below are
built from the UniProt record, cached publications, QuickGO and, where noted, open
PMC full text.

## What TLR7 is

Endolysosomal single-pass type I membrane pattern-recognition receptor: a
leucine-rich-repeat ectodomain, one transmembrane helix, and a cytoplasmic TIR
domain. UniProt Q9NYK1: signal 1–26, chain 27–1049, extracellular 27–839,
transmembrane 840–860.

**Dual ligand-binding architecture.** TLR7 is not a simple "ssRNA receptor". The
crystal structures resolve two spatially distinct sites:

- [PMID:27742543 "The first site conserved in TLR7 and TLR8 was used for small
  ligand-binding essential for its activation. The second site spatially distinct
  from that of TLR8 was used for a ssRNA-binding that enhanced the affinity of the
  first-site ligands. The first site preferentially recognized guanosine and the
  second site specifically bound to uridine moieties in ssRNA."]
- [PMID:27742543 "Our structural, biochemical, and mutagenesis studies indicated
  that TLR7 is a dual receptor for guanosine and uridine-containing ssRNA."]

**The endogenous site-1 ligand is 2',3'-cGMP, not 3',5'-cGMP.** This matters for
the `GO:0070305 response to cGMP` row (see below).

- [PMID:38697119 "TLR7 contains two ligand-binding pockets that recognize
  different RNA degradation products: pocket 1 recognizes guanosine, while pocket
  2 coordinates pyrimidine-rich RNA fragments."]
- [PMID:38697119 "PLD exonuclease activity further released the terminal
  2',3'-cyclic guanosine monophosphate (2',3'-cGMP) to engage pocket 1 and was
  also needed to generate RNA fragments for pocket 2."]
- [PMID:35477763 "The TLR7Y264H variant selectively increased sensing of guanosine
  and 2',3'-cGMP10-12, and was sufficient to cause lupus when introduced into
  mice."]

Guanosine analogues and deoxyguanosine are RNA-independent agonists acting at the
same site:

- [PMID:12738885 "Here, we report that several guanosine analogs activate
  Toll-like receptor 7 (TLR7)."]
- [PMID:31608988 "We conclude that dG induces an inflammatory response through
  TLR7 and propose that dG is an RNA-independent TLR7 agonist."]

**ssRNA sensing and antiviral function.**
- [PMID:14976261 "Here, we show that this requires endosomal recognition of
  influenza genomic RNA and signaling by means of Toll-like receptor 7 (TLR7) and
  MyD88."]
- [PMID:16188996 "ectopic expression of TLR7 and TLR8 (but not TLR2, -3, -4, or
  -9) in HEK293 cells elevated SeV-induced activation of NF-κB and expression of
  IL-8 and IP-10"]

**Localisation.** ER at rest, relocating to endosomes/lysosomes; UNC93B1 is the
trafficking chaperone.
- [PMID:22164301 "Thus, the localization site of TLR8 differed from TLR7 and
  TLR9, both of which reside in the endolysosome and the ER."]
- [PMID:12738885 "The stimulation of TLR7 by the guanosine analogs in human cells
  appears to require endosomal maturation because inhibition of this process with
  chloroquine significantly reduced the downstream activation of NF-kappaB."]
- [PMID:33432245 "Both TLRs interact with the UNC93B1 amino-terminal six-helix
  bundle through their transmembrane and luminal juxtamembrane regions"]

**Outputs and disease.** MyD88 myddosome → NF-κB (proinflammatory cytokines) and
IRF7 (type I IFN). Loss of function causes IMD74 (severe COVID-19); gain of
function causes SLEB17 (lupus).
- [PMID:32706371 "In addition, both index patients were completely deficient for
  IFN-γ production in response to TLR7 stimulation ( Figure 2 C)."]
- [PMID:32706371 "Additionally, an abrogated production of the type II IFN, IFN-γ,
  was observed in the patients’ PBMCs stimulated with imiquimod"]

## Annotation-level findings

1. **`GO:0070305 response to cGMP` (IMP, PMID:35477763) is chemically wrong.**
   `GO:0070305` is defined as a response to "cGMP (cyclic GMP, guanosine
   3',5'-cyclophosphate)" (QuickGO). The TLR7 site-1 ligand released by
   RNase T2/PLD3/PLD4 is guanosine **2',3'**-cyclic monophosphate
   [PMID:38697119], and the cited lupus paper says exactly that
   ("guanosine and 2',3'-cGMP"). MODIFY to `GO:1905108 guanosine binding`, which
   is what the structures and the deoxyguanosine work establish directly. GO has
   no term for 2',3'-cGMP binding or for a response to it — raised as a question.

2. **`GO:0071260 cellular response to mechanical stimulus` (IEP, PMID:19593445)
   cites an unrelated paper.** PMID:19593445 is "Expression of the Bcl-2 protein
   BAD promotes prostate cancer growth" (PLoS ONE 2009); the cached record has
   full text and contains **zero** occurrences of "TLR" or "toll". The same row
   exists on TLR8 and on TLR3 (where it was also left UNDECIDED). Marked
   UNDECIDED, with `reference_review.correctness: WRONG_IDENTIFIER`.

3. **`GO:0034158 toll-like receptor 8 signaling pathway` on TLR7.** An Ensembl
   Compara transfer from mouse Tlr7 (UniProtKB:P58681). `GO:0034158` is defined as
   "The series of molecular signals initiated by a ligand binding to the
   endolysosomal toll-like receptor 8" (QuickGO) — by definition it cannot be a
   process TLR7 carries out. TLR7 already has `GO:0034154` four times over.
   REMOVE.

4. **`GO:0043235 signaling receptor complex` (IDA, PMID:23382219) cites the SNX17
   PX-FERM structure paper.** I retrieved the open PMC copy (PMC3581954, 244 kB of
   text) and it contains no mention of TLR7 or of Toll-like receptors. The claim
   itself is true — TLR7 forms an activated m-shaped homodimer [PMID:27742543] and
   associates with UNC93B1 [PMID:33432245] — so the row is kept (ACCEPT) with the
   real support attached and the reference flagged as a wrong identifier.

5. **`GO:0003725 double-stranded RNA binding` (IDA, PMID:16111635).** The cached
   record is abstract-only and says "RNA signals through human TLR3, TLR7, and
   TLR8"; dsRNA is TLR3's ligand, while TLR7's second site binds single-stranded
   uridine-containing RNA [PMID:27742543]. MODIFY to `GO:0003727`.

6. **`GO:0035197 siRNA binding` (IEA from mouse Tlr7 + ISS).** siRNA is a duplex;
   the structurally defined TLR7 sites bind guanosine and single-stranded
   uridine-containing RNA. Immunostimulatory siRNA plausibly acts through
   single-stranded regions or degradation products rather than duplex binding.
   MARK_AS_OVER_ANNOTATED.

7. **Type II interferon.** Two rows. The `IDA PMID:16286015` row rests on a paper
   that measured IFN-α/β and IFN-λ only — "Human TLR-7-, -8-, and -9-mediated
   induction of IFN-alpha/beta and -lambda Is IRAK-4 dependent" — so it is
   MODIFY→`GO:0034346 positive regulation of type III interferon production`
   (matching the decision already taken in the TLR9 review). The ARBA `IEA` row is
   independently supported for TLR7 by PMID:32706371 (IFN-γ abolished in TLR7
   loss-of-function patients' PBMCs), but that is a 7-day PBMC readout and the
   IFN-γ producers are not the TLR7-expressing cells, so it is kept as non-core.

8. **Plasma membrane.** The `is_active_in GO:0005886` IBA sits at the TLR7/8/9
   PAINT node and there is a melanocyte surface IDA [PMID:19740627]. TLR7's
   intracellular confinement is functionally essential, and the endolysosome is
   where it signals, so both rows are kept as non-core rather than accepted —
   consistent with the TLR9 review. Whether `is_active_in plasma membrane` should
   stand at that node is raised as a question.

9. **`GO:0005515 protein binding` (IPI, PMID:33432245, UNC93B1).** Uninformative;
   TLR7 is the *client* of UNC93B1 and the biology is trafficking, not an activity
   of TLR7. REMOVE (mirrors the TLR3 review's handling of the same paper).
   Removal does not dispute the interaction.

10. **Reactome bulk rows.** 19 `GO:0010008 endosome membrane` and 19
    `GO:0036020 endolysosome membrane` TAS rows, plus Golgi and ER membrane rows,
    all from the Reactome TLR7/8/9 cascade models. Endosome/endolysosome membrane
    are accepted as core; ER membrane is accepted (resting location); the two Golgi
    membrane rows are kept as non-core because Golgi transit is a modelling
    assumption of the UNC93B1 route with no direct evidence for human TLR7 (and
    Golgi markers explicitly failed to colocalise with the paralogue TLR8,
    [PMID:22164301]).

## Deep-research cross-check (2026-09-30)

Compared the Falcon report (review-level sources: Zheng 2023, Hamerman & Barton
2024, von Hofsten 2024, Lind 2022; citation keys are not PMIDs) against every
review decision, the description and core functions.

- **Agrees:** dual-site recognition (guanosine at site 1, uridine-containing ssRNA
  at site 2; matches PMID:27742543/PMID:38697119); RNase T2-generated ligands; Z-loop
  cleavage; UNC93B1-dependent ER-to-endolysosome trafficking; MyD88-IRAK4/IRAK1-TRAF6
  to NF-kappaB and IRF7/type I IFN; *not* a plasma-membrane receptor (consistent with
  keeping the PAINT/melanocyte plasma membrane rows only as non-core); pDC/B-cell
  expression; TLR7 Y264H gain-of-function lupus (PMID:35477763).
- **Adds (not used for decisions):** possible TIRAP/TRAM contribution to TLR7-IRF7
  signalling; Cys98-Cys475 disulfide linking cleaved ectodomain fragments; B-cell
  differentiation/autoantibody roles; therapeutic antagonists. None was verified in a
  cached primary paper and none supports a NEW term under the participation test.
- **Conflicts:** none. The report does not mention the reference problems found here
  (PMID:19593445, PMID:23382219) or the 2',3'- vs 3',5'-cGMP issue.
- **Changes:** no annotation decisions changed. Added the report to `references`
  (relevance LOW, UNVERIFIED) and cited it as corroborating context on the
  `GO:0038187` IMP row.

