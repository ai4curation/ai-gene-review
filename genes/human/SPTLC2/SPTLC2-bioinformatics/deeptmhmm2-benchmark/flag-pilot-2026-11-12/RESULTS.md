# Expanded human topology-flag pilot

The pilot supports using topology constraints as a **bidirectional review queue**:
they can challenge an annotation, a prediction, or the assumption that both refer
to the same protein form and membrane context. They do not provide an automatic
GO NOT generator.

We ran **205 additional human proteins**, excluding the earlier 31, and obtained
**45 flags on 32 proteins**. The remaining 173 triggered no checks; that does not
validate their annotations. Every flagged protein has a manual triage entry in
[adjudication.yaml](adjudication.yaml). These entries draw on existing reviews and
selected primary evidence, not a new full literature review for each gene. No
gene review or GO assertion was changed in this expanded pilot.

## Design and measured cost

Selection preceded inspection of predictions: all additional locally available
positive canonical GOA claims in FRR:0004 scope (176 proteins), all exact
lipid-droplet GOA candidates (26), and three controls. See [README.md](README.md)
and [selection.json](selection.json) for the exact scope. The 14 reviews missing
required files were noncoding targets, not protein-inference failures. This is an
enriched curation sample, not a proteome-wide accuracy estimate. Overlap with model
training data is unknown.

| Measurement | Result |
|---|---:|
| Sequences / residues | 205 / 126,912 |
| Length range | 55–4,563 aa |
| CPU inference, one pass | 726.87 s |
| Whole API process | 739.61 s (12.33 min) |
| Peak resident RAM | 5,596,381,184 bytes (5.21 GiB) |
| Separate upstream CLI diagnostic | 5 proteins; 102.70 s overall |

The run used the pinned model on the M1 Max CPU, eight threads, default API
precision, no marginals, and the previously validated unbatching workaround.
Full sequences were supplied; ESM uses upstream chunking for long inputs.
Sequence-length mix and local system conditions limit whole-proteome runtime
extrapolation.

## What fired

| Check | Flags |
|---|---:|
| FRR:0004 companion: no predicted span on an in-scope transporter assertion | 27 |
| DTM2:0002: retained lipid-droplet claim plus source or predicted span | 10 |
| DTM2:0004: predicted span overlaps UniProt INTRAMEM residues | 7 |
| DTM2:0003: human protein assigned a chloroplast membrane | 1 |
| DTM2:0001: source TRANSMEM versus IF/RE-only prediction | 0 |

DTM2:0003 and DTM2:0004 were added **during this pilot** after examining APOB and
AUP1/CAV1. The original checks produced 37 flags on 26 proteins; expanded counts
are exploratory, not a prespecified validation result. The regional check records
all overlaps, so small boundary overlaps deserve less weight than substantial
geometry disagreements. The original S20-enriched DTM2:0001 pattern did not recur.

## Biological interpretation

**Seven genes recover existing annotation distinctions:** AKR1C4, AP4M1, AZGP1,
BLOC1S3 and HPX already have removals distinguishing soluble carriage or vesicular
delivery from trans-bilayer transport. CACNB2 and CACNB3 already have refinements
distinguishing channel regulation from pore activity. These are not new errors.

**Eight genes require complex-role interpretation:** ATP5PF, ATP6V1B1, ATP6V1B2,
ATP6V1C1, ATP6V1C2, ATP6V1F, CACNA2D1 and CACNA2D4. Absence of a span does not
negate participation in transport. The rule exempts primary-active-transporter
terms, but broad proton-transporter parent terms can still fire. CACNA2D1 also
illustrates precursor processing and GPI anchoring. Existing reviews differ in
how they resolve the relation semantics; the flag does not adjudicate that debate.

**Four genes expose model counterexamples:**

- **AUP1:** predicted spans at 32–56 and 61–70 conflict with experimentally
  supported monotopic hairpin insertion. Experimentally changing the hairpin
  motif converts topology and abolishes LD targeting—a direct example of the
  geometric constraint ([PMID:23197321](https://pmc.ncbi.nlm.nih.gov/articles/PMC3588876/)).
- **CAV1:** predicted spans overlap its intramembrane region. Human assembly and
  reconstitution evidence supports monotopic membrane interaction. Its pending
  LD annotations alone would not trigger the retained-LD rule
  ([PMID:40359049](https://pubmed.ncbi.nlm.nih.gov/40359049/)).
- **LPCAT2:** two short predicted spans conflict with the human LPCAT1/2 study's
  monotopic interpretation. The earlier LPCAT1 success does not establish that
  the model resolves every family member
  ([PMID:21498505](https://pmc.ncbi.nlm.nih.gov/articles/PMC3122193/)).
- **APOB:** 114 predicted beta strands and a chloroplast outer-membrane label.
  Human apoB100 structural work shows a beta belt around LDL. This does not
  support a bilayer-spanning barrel, and the chloroplast label is incompatible
  with human cell biology. The structural argument addresses the LDL-associated
  form, not every biosynthetic intermediate
  ([PMID:39662503](https://www.nature.com/articles/s41586-024-08467-w)).

All four counterexamples, plus GSDMD, reproduced **exactly** with the unmodified
upstream CLI for topology strings, segment boundaries, classes and selected
membrane labels ([cli-comparison.json](cli-comparison.json)). They are not artifacts
of the API adapter. Rounded probability scores were not compared.

**Context explains BSCL2:** seipin remains ER-embedded at ER–LD contacts. Broad LD
association does not assert that its spanning helices occupy the droplet monolayer.
Five other LD flags—BCAP31, C19orf12, DGAT2, HSD3B7 and NSDHL—remain context or
topology questions. Neither contamination nor direct monolayer insertion follows
from the flag. Original relations, including `colocalizes_with`, are preserved.

**Five regional conflicts need structural mapping:** CLCN4, CLCN5, CLCN7, CNNM2
and CNNM4 have overlapping INTRAMEM/predicted-TM intervals. They remain membrane
proteins in both sources. Suitable structural mapping is a follow-up, not
completed here; none of these flags justifies NOT transport.

**Two source/processing questions remain:** AIFM2 has a cached N-terminal span,
a wholly globular prediction, and literature on lipid-mediated recruitment.
Myristoylation alone cannot rule out a span. TOMM70 is predicted to have a transit
peptide at 1–71 instead of its annotated 39–59 anchor. Its receptor/adaptor role
is separate from anchor geometry; the cached cited abstracts do not resolve that
geometry directly. Both warrant a targeted topology check before any change.

## Evidence can weaken negative rules too

The original UniProt-feature rule would flag 15 proteins. DeepTMHMM2 finds spans
in **APOL1 and ATP5ME**, weakening the absence argument for those two. Independent
bilayer electrophysiology supports APOL1 channel formation, but the model does not
settle chloride-versus-cation selectivity
([PMID:25730870](https://pubmed.ncbi.nlm.nih.gov/25730870/)). Finding an anchor in
ATP5ME does not establish that this accessory ATP-synthase subunit independently
conducts protons; its existing role-specific concern remains.

Likewise, **ABCC8** has 17 predicted spans and passes the topology requirement,
yet its reviewed role is regulation of the Kir6.2 pore. A structural requirement
is insufficient to assign function. **GSDMD** recovers four beta strands and a
plasma-membrane label, consistent with its active pore; cleavage and assembly
still matter ([PMID:33883744](https://pubmed.ncbi.nlm.nih.gov/33883744/)).

All three explicit controls—ATP5F1B, ATP6V1A and HSPA5—were unflagged. Exempt terms
and `contributes_to` relations prevent indiscriminate negative calls on soluble
pump components. These are scope checks, not a population specificity estimate.

## Recommended use and remaining leads

Show the disputed claim, exact residues, provenance, protein form/context and
independent evidence during review. Prioritize impossible taxon labels and
literature-resolved topology disagreements. Keep regional geometry and contact
questions advisory. Before inferring GO NOT, ask whether evidence excludes the
precise asserted function/location or only one proposed mechanism.

Follow-ups are recorded for AIFM2/TOMM70 topology, five LD-context cases, five
regional structural mappings, and complex-subunit relation handling. These are
explicit research leads, not incomplete inference jobs. This pilot is sufficient
to demonstrate value; scaling should preserve this review layer.

## Reproducibility and validation

- [x] Scripts take explicit inputs/outputs; cohort choices are recorded separately.
- [x] All 205 sequences completed; identity and complete coverage were checked.
- [x] Raw outputs, all-protein summary and manual triage are present.
- [x] Every flagged protein occurs exactly once in the triage table.
- [x] Five selected diagnostic outputs match the upstream CLI exactly.
- [x] The earlier 31-protein panel retains exactly its original 21 flags.
- [x] Literature support, prior review judgments and unresolved questions are distinguished.

Weight verification and script provenance are recorded in `provenance.json`.
The offline test suite and project-history checks are recorded in `validation.txt`.
An initial concurrent test run passed its assertions but the filesystem guard
detected the predictor's new files. Tests were rerun after inference/export ended;
only the final clean run counts as validation. No global rule configuration was
changed and no automatic GO NOT assertion was emitted.
