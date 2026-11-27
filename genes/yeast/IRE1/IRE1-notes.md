# IRE1 review notes

## 2026-09-30 -- apoptosis IBA and broad-MF cleanup for APOPTOSIS

The only death-related yeast IRE1 annotation is the GO_Central IBA to
`GO:0070059 intrinsic apoptotic signaling pathway in response to endoplasmic
reticulum stress`. I left this as `MARK_AS_OVER_ANNOTATED` and tightened the
propagation review: the current local PANTHER cache places conserved ER
localization, RNA endonuclease activity, Ser/Thr kinase activity, and
IRE1-mediated UPR on the pan-eukaryotic IRE1-family node PTN000359335, but the
ER-stress apoptosis term now appears on PTN000359344 with mouse ERN seeds. Yeast
IRE1 is an adaptive IRE1-HAC1 UPR sensor/kinase/RNase, not a mediator of the
metazoan IRE1/ERN apoptosis branch.

Also cleaned the whole review before marking it complete: broad direct molecular
function ancestors such as nucleotide binding, catalytic activity, kinase
activity, transferase activity, RNA nuclease activity, hydrolase activity, and
metal ion binding now `MODIFY` to ATP binding, protein Ser/Thr kinase activity,
RNA endonuclease activity, or magnesium ion binding as appropriate. The generic
IntAct `protein binding` row for DCR2 was changed to `REMOVE`; the DCR2-Ire1
interaction is real [PMID:16990850 "Dcr2 physically interacts in vivo with
Ire1-S840E,S841E, which mimics phosphorylated Ire1, and Dcr2 de-phosphorylates
Ire1 in vitro"], but the specific phosphatase activity belongs to Dcr2 and
`GO:0005515` adds no useful IRE1-side activity.

## 2026-09-02 Update: nuclear-localization annotation (GO:0005634, IDA, PMID:17035634)

Audited the existing review for oversights. The IDA annotation of GO:0005634 (nucleus)
from PMID:17035634 had been marked `UNDECIDED` with the stated reason "Unable to access
PMID:17035634 to verify the nuclear localization claim." This was incorrect: the
publication is cached in this repository (`publications/PMID_17035634.md`) and its
abstract directly and unambiguously supports the annotation.

Goffin et al. 2006 (Mol Biol Cell) show that Ire1p's cytoplasmic linker region contains
an 18-residue nuclear localization sequence (NLS) recognized by both importin alpha
(Kap60p) and multiple importin beta homologues, that this NLS drives Ran-GTPase-dependent
nuclear import of Ire1p (or an NLS-GFP reporter) in vivo, and that NLS-disrupting point
mutations impair ER-stress-induced HAC1 mRNA splicing:

[PMID:17035634 "The Ire1p transmembrane receptor kinase/endonuclease transduces the
unfolded protein response (UPR) from the endoplasmic reticulum (ER) to the nucleus in
Saccharomyces cerevisiae."]

[PMID:17035634 "This 18-residue sequence is capable of targeting green fluorescent
protein to the nucleus of yeast cells in a process requiring proteins involved in the
Ran GTPase cycle that facilitates nuclear import."]

[PMID:17035634 "The NLS-dependent nuclear localization of Ire1p would thus seem to be
central to its role in UPR signaling."]

Changed the annotation's `action` from `UNDECIDED` to `KEEP_AS_NON_CORE`: the nuclear
pool and NLS-dependent import are real and evidence-backed (so UNDECIDED, reserved for
cases where the evidence genuinely cannot be assessed, was not appropriate), but IRE1's
best-established, defining catalytic activities (kinase trans-autophosphorylation and
HAC1 pre-mRNA endoribonuclease splicing) are ER-membrane events, so nuclear import is
kept as a non-core regulatory/trafficking aspect rather than promoted into
`core_functions`.

All other existing annotations, `core_functions`, and the top-level `description` were
reviewed and found sound and well-supported; no other changes made.

## 2026-09-04 — SFT review consistency after the nuclear-localization re-review

The SFT prediction review still classified GO:0005634 (nucleus) as NPI and asserted
that IRE1 is never found in the nucleus after the main gene review retained the IDA
annotation from PMID:17035634 as KEEP_AS_NON_CORE. The benchmark policy treats an
exact term retained with a positive AIGR action as CNN (correct but not novel), even
when the function or location is non-core. The standard SFT audit identified this
single deterministic category conflict across its 95-gene cohort.

The categorical exclusion is also too strong for the cached abstract, which reports
NLS-dependent localization and mutational effects on signaling [PMID:17035634
"ER stress-induced HAC1 mRNA splicing, is inhibited by
point mutations in the Ire1p NLS that inhibit nuclear localization"]. This consistency
repair follows the existing annotation review; it does not infer that nuclear
localization is IRE1's principal location or resolve the mechanism of trafficking of
the intact membrane protein. The reference cache remains abstract-only.

## 2026-09-30 IBA rereview

Rechecked the six IRE1 IBA rows against the current cached PTHR13954 PAINT export:

- `PTN000359335` still carries the four deep eukaryotic IRE1 assertions
  inherited by yeast IRE1: `GO:0005783 endoplasmic reticulum`,
  `GO:0036498 IRE1-mediated unfolded protein response`, `GO:0004521 RNA
  endonuclease activity`, and `GO:0004674 protein serine/threonine kinase
  activity`. Those are core conserved Ire1 activities and localization.
- `GO:0051082 unfolded protein binding` remains in the cached GOA snapshot but
  is absent from the current PTHR13954 PAINT export. The yeast IRE1 seed is real
  target evidence for unfolded-protein detection, not circular support, but the
  GO:0051082 molecular-function term is obsolete and chaperone-scoped; the
  existing replacement with `GO:0002235 detection of unfolded protein` remains
  the better representation of Ire1's sensor role.
- `GO:0070059 intrinsic apoptotic signaling pathway in response to endoplasmic
  reticulum stress` remains confined to `PTN000359344`, the mammalian ERN1/ERN2
  branch, and no longer sits on the broad eukaryotic IRE1 node that generated
  the old yeast GOA row.
- The 2026 public-literature search found current database, review, and yeast
  engineering mentions but no newer direct yeast Ire1 primary study that changes
  these IBA decisions.
