# ALPI (human) — review notes

UniProt: P09923 (PPBI_HUMAN) · intestinal-type alkaline phosphatase (IAP) · EC 3.1.3.1 ·
528 aa precursor, chromosome 2q37 cluster with ALPP and ALPG.

Reviewed alongside the other three human alkaline phosphatases; the cross-isozyme
reasoning is recorded in `genes/human/ALPL/ALPL-notes.md` and the shared decisions are
summarised there.

## What the record looked like before review

17 GOA rows, of which the substantive content was: alkaline phosphatase activity (four
times), plasma membrane (six times), zinc/magnesium binding by ISS, generic
`dephosphorylation`, `protein binding` twice, and `protease binding` once. Nothing about
lipopolysaccharide, TLR4, the brush border, or the disease. For a gene with a published
Mendelian disease mechanism that is a striking gap.

## The paper GOA is missing

Parlato et al. 2018 (PMID:29567797, EMBO Mol Med, full text cached) is not cited anywhere
in ALPI's GOA. It reports biallelic loss-of-function ALPI variants in two unrelated
patients as a Mendelian cause of IBD [PMID:29567797, "Herein, we report the first
identification of biallelic-inherited mutations in ALPI as a Mendelian cause of
inflammatory bowel disease in two unrelated patients."] and works out the mechanism
[same, "ALPI encodes for intestinal phosphatase alkaline, a brush border metalloenzyme
that hydrolyses phosphate from the lipid A moiety of lipopolysaccharides and thereby
drastically reduces Toll-like receptor 4 agonist activity."].

Every variant was reconstituted in HEK293T cells; LPS dephosphorylating activity was
measured directly; ALPI staining was reduced in patient biopsies; faecal ALPI activity was
undetectable in the deficient patient. Four of the five NEW annotations rest on it:

- `GO:0008653 lipopolysaccharide metabolic process` (IMP). Precedent checked: AOAH, the
  other host enzyme that chemically modifies LPS to detoxify it, carries this term with
  IDA in human. I checked GO:0046493 lipid A metabolic process first and rejected it —
  QuickGO returns zero human or mouse annotations for it, so it appears to be used only
  for bacterial biosynthesis and asserting it here would be a taxon gamble.
- `GO:0034144 negative regulation of toll-like receptor 4 signaling pathway` (IMP).
  Acting on the ligand rather than the receptor is well precedented for this term in
  human — BPIFB1, a secreted LPS-binding protein, carries it with IDA — and ALPI's case is
  stronger since it covalently alters the agonist.
- `GO:0031526 brush border membrane` (TAS). Deliberately TAS, not IDA: the paper states
  the localisation as established background rather than demonstrating it with a new
  experiment.
- `GO:0009897 external side of plasma membrane` (IDA) [PMID:29567797, "As expected, given
  the lack of a GPI anchoring site at the CT domain, the Q439X truncated protein was
  undetectable at the cell surface by flow cytometry (Fig 3B)."]
- `GO:0042803 protein homodimerization activity` (IMP) [same, "Active ALPI consists of two
  identically processed subunits (each lacking the first 19 and last 24 aa) bound to the
  cell surface via a post-translationally added GPI anchor (Fig 2D)."]

## Judgement calls

- **`GO:0016311 dephosphorylation` (ISS)** → KEEP_AS_NON_CORE. It is the only BP term GOA
  gives this gene, and it is nearly contentless: it restates the MF as a process and would
  be true of any phosphatase. Kept rather than removed only because removing it would leave
  the gene with no process annotation at all; the real fix is the two proposed BP terms.
- **`GO:0002020 protease binding` (IPI, PMID:18307834)** → KEEP_AS_NON_CORE, not
  over-annotated. This is a directed IP/MS experiment in Caco-2 cells, a physiologically
  appropriate human cell type, and it is the one protein-interaction row for this gene
  worth keeping. Non-core because ALPI is the *target*: the cathepsin C propeptide
  accelerates ALPI degradation [PMID:18307834, "Pulse-chase analysis confirmed that the
  reduction in IAP activity was due to an increase in IAP degradation, but not a decrease
  in IAP expression."]. The biology belongs on cathepsin C, not here.
- **The two `GO:0005515 protein binding` rows** → MARK_AS_OVER_ANNOTATED. Both are binary
  Y2H interactome maps (PMID:25416956 = Rolland/Vidal HI-II-14; PMID:31515488 =
  Fragoza/Yu variant screen). Partners are KRTAP10-8, KRTAP10-9 and NOTCH2NLA. KRTAPs are
  the classic sticky-partner class; nothing here suggests an enterocyte-surface complex.
  PMID:31515488 only re-detects NOTCH2NLA in the same assay format, which is assay
  reproducibility rather than biological support.
- **`GO:0005576 extracellular region` (TAS)** → ACCEPT, unusually. For the other three
  isozymes the released soluble pool is a by-product; for ALPI it is the main site of
  action, since the enzyme is shed into the lumen and faecal ALPI activity is the clinical
  assay [PMID:29567797, "ALPI is produced in the intestinal brush border and released in an
  active form into the intestinal lumen where it can dephosphorylate microbiota-derived LPS
  and thereby considerably reduces its TLR4 agonist activity."].
- **`GO:0016791 phosphatase activity`** (InterPro2GO) → MODIFY to GO:0004035, same as in
  all four reviews.
- Zinc and magnesium ISS rows → ACCEPT. The metal ligands are the most conserved positions
  in the family and the human paralogues have crystallographically resolved sites, so the
  transfer from mouse Akp3 is safe.

## Isozyme non-equivalence

Worth recording because it constrains how much can be transferred between these genes: the
deep research reports that upregulated TNAP in ALPI-deficient intestine did not restore
luminal function [file:human/ALPI/ALPI-deep-research-falcon.md, "Upregulation of TNAP in
ALPI-deficient intestine did not restore luminal ALPI function, supporting functional
non-equivalence in this compartment."]. Two GPI-anchored alkaline phosphatases with the
same catalytic machinery are not interchangeable in the same compartment, which is a
caution against family-level BP transfer in either direction.
