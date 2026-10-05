# COA4 / CMC3 / YLR218C (Q05809) — research notes

*Saccharomyces cerevisiae* cytochrome oxidase assembly factor 4. 96 aa.
Companion to `genes/human/COA4/`. Most of the mechanistic genetics for this family is in yeast;
the human review depends on it via cross-species complementation.

## Identity and structure

- Twin CX9C protein: CHCH domain 36–77, Cx9C motifs at 39–49 and 59–69, disulfides 39↔69 and
  49↔59 (UniProt Q05809, PROSITE-ProRule inference).
- UniProt `FUNCTION: Involved in cytochrome c oxidase assembly or stability.`
  `SUBCELLULAR LOCATION: Mitochondrion inner membrane.` Abundance ~907 molecules/cell.
- Named Cmc3 on discovery in the twin Cx9C family survey, renamed Coa4 on functional
  characterization.

## Evidence chain

**2009 — family survey, as Cmc3** [PMID:19703468]. Identified among 14 yeast twin Cx9C proteins;
import shown to depend on the Mia40–Erv1 disulfide relay ["which we demonstrated to be dependent
for import"]. Deletion mutants of most family members impair respiratory chain assembly or
stability — the basis of the general `GO:0033108` IMP row.

**2010 — renaming and characterization** [PMID:20624914]. Isolated as an allele-specific
suppressor of the Shy1 G137E Leigh-syndrome mutant.
- "Coa4 is a twin CX 9 C motif mitochondrial protein localized in the intermembrane space and
  associated with the inner membrane"
- "Cells lacking Coa4 are depressed in CcO activity but show no impairment in Cox1 maturation or
  formation of the Shy1-stabilized Cox1 assembly intermediate" — places Coa4 downstream of Cox1
  synthesis and hemylation.
- "Cells lacking Coa4 resemble shy1 Δ cells in exhibiting a reduced mitochondrial copper content"
- CYC1 (cytochrome c) overexpression restores respiratory function.
- Source of both IGI rows: SGD:S000003344 = **SHY1**, SGD:S000003809 = **CYC1**.

**2013 — ROS, not assembly, limits growth** [PMID:23198688]. "Deletion of CMC1 or COA4 leads to
assembly defects of cytochrome c oxidase"; DTT/GSH/ascorbate rescue respiratory growth but
"the presence of the reductants does not suppress these assembly defects and the levels of
cytochrome c oxidase remain reduced". Source of the IGI row with SGD:S000001620 = **CMC1**.
Methodological caveat: respiratory-growth rescue is not evidence of restored assembly.

**2012 — IMS proteome** [PMID:22984289]. Bax-release profiling of isolated mitochondria;
"From the known 31 soluble IMS proteins, 29 proteins" were recovered and "we found 20 novel
intermembrane space proteins". Source of the `EXP GO:0005758` row. Coa4 is not named in the
cached body text (the assignment is in the study's protein tables), so the SGD curator call is
accepted rather than second-guessed.

**2022 — genetic placement in the copper pathway** [PMID:35666203]. Cox11 overexpression restores
Cox1 abundance, CcO assembly and respiration in coa4Δ; the rescue requires Cox11's
copper-coordinating cysteines; Coa4 and Cox11 abundance are reciprocally regulated; coa4Δ has
reduced cellular copper; human COA4 complements coa4Δ. Coa4 is **not** a metallochaperone —
"Importantly, Coa4 lacks the copper-binding cysteine motif that is found in Cox17, further
negating its metallochaperone role". The authors explicitly could not detect a Coa4–Cox11
physical interaction by co-IP/MS.

**2026 — the physical interaction** [DOI:10.1038/s41467-026-77112-z]. Co-IP of yeast Coa4-V5 from
DSSO-crosslinked mitochondria recovered Cox11, closing the gap left in 2022 — plausibly because
crosslinking captures a transient contact. Also enriched: "the IMS-localized Ptc5 phosphatase,
which suggests a role for this protein in regulating copper delivery to CcO through reversible
phosphorylation of Coa4 in yeast" — suggestive only, no follow-up.

## Annotation assessment

**Core.** `GO:0033617 mitochondrial respiratory chain complex IV assembly` carries IMP evidence
from two independent studies plus three IGI rows (SHY1, CYC1, CMC1). `GO:0005758 mitochondrial
intermembrane space` carries EXP, two IDA rows, IBA, IEA and TAS. Both are exceptionally
well-supported here — considerably better than in human, which is why the yeast review is the
anchor for the family.

**`GO:0003674 molecular_function` ND.** SGD's explicit "no data" placeholder. This is *correct
and worth preserving*: no catalytic or binding activity has ever been demonstrated for Coa4, and
metallochaperone activity is positively excluded. It independently corroborates the decision in
the human review not to assert a molecular function term.

**`GO:0033108 mitochondrial respiratory chain complex assembly` (IMP, PMID:19703468).** Faithful
to that paper, which assayed respiratory chain function generally, but superseded by the
complex IV–specific IMP rows from focused studies. MODIFY → `GO:0033617`.

**`GO:0005634 nucleus` (HDA, PMID:14562095) — flagged.** From the genome-wide C-terminal GFP
library. Flagged on conflict grounds, not because the underlying images are unavailable:
- Coa4 is a twin CX9C substrate of the MIA40-ERV1 relay, and there is no described route by which
  such a protein reaches the nucleus — import commits it to the IMS, where its disulfides are
  oxidatively trapped.
- Contradicted by EXP IMS proteomics, two IDA rows, IBA, IEA, TAS and UniProt, with no other
  source of any kind placing Coa4 in the nucleus.
- Most likely a C-terminal GFP fusion that blocked import and was scored outside mitochondria.

Marked `MARK_AS_OVER_ANNOTATED` rather than `REMOVE` so a curator with the original images makes
the final call. `REMOVE` would be defensible.

**`GO:0005737 cytoplasm` (HDA, PMID:14562095) — accepted, non-core.** Deliberately treated
differently from the nucleus row. Mia40 substrates genuinely dwell in the cytosol before import —
"substrates of Mia40 remain in the cytosol for several minutes" [PMID:23676665, human study of the
same pathway] — so a cytosolic signal here is *expected*, not anomalous. The GFP tag may
additionally inflate it, but nothing known about Coa4 contradicts a real cytosolic pool, so the
annotation stands as a correct compartment. Kept non-core because the functional pool is the IMS one.

**`GO:0005743 mitochondrial inner membrane` (IEA).** Consistent with UniProt and with Bestwick's
"associated with the inner membrane", but in slight tension with the Bax-release IMS proteomics
that treats Coa4 as soluble-releasable. Best read as peripheral association; kept non-core.

## Open questions

- Same as human: is Coa4 stabilizing Cox11, loading it with copper, or gating handoff to Cox1?
- Does Ptc5 dephosphorylate Coa4, and does that regulate copper delivery? Only co-IP enrichment.
- Why does high-copy CYC1 suppress coa4Δ? Bestwick called this "a major clue" and it has never
  been followed up.
- Would an **N**-terminally tagged or untagged Coa4 GFP construct abolish the nuclear signal?
  That is the experiment that would settle the contested nucleus row.
