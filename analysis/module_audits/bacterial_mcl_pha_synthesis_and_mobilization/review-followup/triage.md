# PR6194 independent scientific triage

Reviewed published HEAD `abf55243f2d7d6099ffb186a923f36d73ffb2ef9` on 2026-11-07. This is a read-only consultation, not implementation or approval. The full comment is preserved in `comment.json`; exact reviewed-file hashes are in `before.yaml`. No gene, family, module, source cache or older receipt was changed.

## 1. Family verdicts: partly agree; do not restore wholesale

The reviewer correctly distinguishes an ancestral **gain placed too deeply** (TOO_DEEP) from a subsequent loss (NEEDS_PRUNING/LOSS_SUPPORTED). Current PTHR43194 reasons incorrectly use the absence of a demonstrated loss to justify withdrawing a TOO_DEEP assessment. Rewrite that reasoning even if the resulting verdict remains UNRESOLVED. A negative purified assay is not mandatory for a defensible phylogenetic restriction; independent biochemical specialization, pathway architecture and a resolved tree can jointly support one.

However, the original assertions do not provide that complete argument. The old PTHR43194 PTN002455972 GO0090499/0009102 reasons assert that RsbQ/PhaG/RhlA have no biotin function because their characterized functions differ. The original PTHR43798 PTN008685307 GO0047372/0046464 reasons explicitly rely on missing evidence and putative fungal hydrolase labels. Those premises do not establish when the function arose. Restore neither TOO_DEEP nor a safe whole-subfamily grant merely to satisfy a cross-check. Preserve positive BioH and ABHD6 anchors and explain the precise unresolved branch/substrate question, rather than suggesting their established activities are doubtful.

`node-payload-comparison.json` verifies all five PTHR43194 and ten PTHR43798 ordered node assertion payloads (IDs, terms, evidence, seeds and snapshot/taxon fields) against the pre-PR baseline. These assertions were not erased; their review verdicts changed. PTHR43194 lost three structured exceptions; PTHR43798 retains its one original Q59695 exception. Archived judgments must remain visible, with their evidentiary reassessment.

**Exact correction:** in both family files, replace “no loss/no target-negative assay, therefore UNRESOLVED” with the actual missing argument: whether the documented heterogeneous branches inherited the specific substrate reaction or native process at the asserted ancestor. Do not invent a later gain node. Investigate RsbQ's native pathway boundary before restoring an SF3-specific TOO_DEEP; PMID15632289 establishes a specialized stress regulator, not a direct negative BioH assay. PAO1 now has a stronger native comparator (section 5).

Schema nuance: `member_exceptions` means the term **does not hold**, not merely that a gene row is MAOA. The validator requires a positive FAMILY_WIDE/SUBFAMILY_ONLY scope. `pruned_node_id` is optional; only an explicitly named node must have a negative matching assessment. Thus an exception does not invariably require restoring a negative node verdict. Conversely, exceptions cannot justify manufacturing a positive scope. Keep archived AcoC/PhaG judgments available, and restore a structured exception only with a supported positive scope and a justified member-negative claim. P26495's MAOA is not itself proof of a catalytic absence or of its exact graft position.

## 2. PSEPK PhaZ tributyrin: agree with MAOA, disagree with the chemistry objection

`genes/PSEPK/phaZ/phaZ-ai-review.yaml` GO0004806 should be reconsidered as MARK_AS_OVER_ANNOTATED under `projects/ENZYME_SPECIFICITY.md`: the overnight weak KT2442 reaction has no established physiological role and does not meet that policy's genuine-secondary-function bar. Preserve the positive measurement and strain inference; do not call the reaction nonexistent. A dedicated competing enzyme and quantitative specificity comparison have not been established here, so REMOVE is not compelled.

The current official GO0004806 definition includes triacylglycerol hydrolysis without a chain-length minimum (`GO0004806.json`). Tributyrin is therefore not excluded simply because it is C4. The reviewer's proposed categorical chemistry objection is incorrect. Likewise the glycerolipid BP and lipase MF need not have identical verdicts: measured chemistry and native pathway participation are different claims. No new row is needed solely to make COMPLETE or core coverage green.

## 3. PhaZ molecular-function granularity: important counterevidence

The claim that both PhaZ panels lack product-size information is false. Full PMID17170116 Fig.6 and Results resolve HO monomer and HO–HO dimer by LC-MS; a mixed Hx–HO dimer is also reported. Dimers dominate early and monomer remains after extended hydrolysis. These products satisfy the size-1-or-2 portion of GO0050527's size-1–5 definition. The evidence is KT2442 recombinant enzyme, not a sequence-verified KT2440 assay; the substrate is HO-rich copolymer, not demonstrated pure-HO homopolymer.

Thus the current qualified PSEPK GO0050527 inference has substantially stronger reaction evidence than GPo1 native genetics. Do not force identical precision merely because both act on C8/C6-containing PHA. Clarify that reaction and strain boundary in PSEPK core support. If pure-polymer substrate specificity is considered indispensable, narrow both claims conservatively, but do not justify it by claiming product sizes were unmeasured.

ECTOL PhaZ's GO0016788 genus plus specific proposed activity remains scientifically faithful to its evidence. The reviewer's proposed switch to an NTR core is an optional representation choice, not proof that the valid genus is wrong. Do not change the proposed definition to promise an experimentally resolved GPo1 oligomer distribution. PSEPK's proposed term should use GO0016788 rather than GO0016787 as its supported immediate hydrolase genus.

## 4. ECTOL PhaZ membrane: retain uncertainty unless stronger placement evidence is found

GO0016020 includes proteins attached to a bilayer, not only transmembrane proteins (`GO0016020.json`). No TM helix therefore cannot establish absence of membrane association. A PHA granule monolayer alone also does not establish bilayer localization. Current UNDECIDED is defensible for this unresolved propagated claim. Family-wide TOO_DEEP at PTN001661081 does not establish that every descendant lacks membrane association; exact target placement and evidence remain relevant. Correct any family reason that treats absence of a TM segment alone as sufficient negative evidence.

## 5. PAO1 PhaG: new native BioH comparator, bounded inference

New primary **PMID36689471**, DOI10.1371/journal.ppat.1011110, directly characterizes PA0502 BioH. Its PAO1 ΔbioH mutant is biotin auxotrophic in defined biotin-free M9, with genetic/biotin rescue; purified PA0502 demethylates pimeloyl-ACP methyl ester. This is stronger than inferring biotin prototrophy from the older phaG mutant's PHA-growth experiment.

The result shows that endogenous PhaG does not provide sufficient compensation in that tested context. It does not directly assay purified PhaG against the BioH substrate or establish zero secondary activity. **Recommended decision:** strengthen the native-process overpropagation assessment for PAO1 GO0009102 (MAOA is defensible); retain explicit uncertainty for GO0090499 unless additional target reaction/specificity evidence warrants MAOA. Do not automatically REMOVE either term or turn this single-strain result into a universal SF5 negative. Keep the exact PhaG tree placement and BioH positives.

## 6. PTHR36837: agree that the current rationale conflates broad and specific scope

Variable chain length and partner requirements do not negate generic PHA biosynthesis or generic non-amino-acyl transfer. HETEROGENEOUS is poorly supported when the only proposed non-synthase branch is an unverified submitter label. Reassess coherence as MOSTLY_COHERENT at the common polymerization role (or UNKNOWN if the enum is being applied strictly to unresolved branches), explicitly distinguishing uncertainty from a proven exception. Do not declare Q8PAX3 a hydrolase exception from its name.

Reassess positive SF5 scope for GO0016747 and GO0042621 using its actual reviewed/classified members and sequence architecture; “polymer composition/partners differ” is not a valid reason to withhold these broad terms. A qualified SUBFAMILY_ONLY grant is preferable if that inspection supports SF5; the present triage does not independently prove every SF5 branch. Keep PHB-specific GO0042619 and universal granule-location scope separate and conservative. No existing PAINT assertion exists here to restore: this family has no node assessments.

## 7. Nearby suggestions

- **PAO1 PhaG authored NEW IC:** review its provenance rather than mechanically substituting IMP. IC is not a generic synonym for curator inference; direct PAO1 genetic evidence and cross-species chemistry must be distinguished. Any evidence-code change requires explicit old-row archival and root authorization because the proposal is historical in the published PR.
- **PSEPK PhaG core support:** move the “no forward in-vitro data” quotation to limitations; retain direct reverse-reaction and positive product-sink evidence as support. This is evidence presentation, not reversal of chemistry.
- **PAO1 raw EC2.4.1.-:** preserve the raw file. A scoped source-defect note is appropriate if the current DE line still classifies the established acyltransfer chemistry as glycosyl transfer; do not invent a precise four-digit replacement EC.
- **ECTOL record sections:** normal deterministic backfill is appropriate; no biological claim changes.
- **CUPNH cytoplasm/granule:** current refinement follows repository general-term policy. No additional NEW is justified solely to accommodate the suggested duplication.

## Source access and limits

Full PMID17170116 was independently read through the author-uploaded ResearchGate text, including Fig.6/Results, not inferred from its abstract. Full PMID36689471 was read on the official PLOS/PMC sites. Only scoped excerpts and URLs are retained here; no protected publication was refreshed. Exact current GO responses are saved. Existing source artifacts and family raw snapshots were inspected; no MSA-based new evolutionary reconstruction was performed. Therefore this report identifies supported corrections and remaining work, not a blanket family approval or an assertion that every requested negative verdict is disproven.
