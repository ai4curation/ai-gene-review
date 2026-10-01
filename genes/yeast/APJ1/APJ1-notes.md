# APJ1 re-review notes

Re-reviewed 2026-08-22. APJ1/YNL077W encodes the 528-aa class A J-domain protein
Apj1 (UniProt P53940), a low-abundance Hsp70 cochaperone found mainly in the
nucleus and cytoplasm. The original review correctly identified a proteostasis
role but over-centered generic protein folding/refolding and did not incorporate
the strongest target-specific nuclear-degradation or Hsf1 evidence.

## Mechanistic anchor

- Apj1 contains an N-terminal HPD-bearing J domain, a class A cysteine-rich
  zinc-binding region (four CXXCXGXG motifs; UniProt residues 193-274), and
  client-binding beta-sandwich regions. Its core molecular activity is stimulation
  of the Ssa Hsp70 ATPase cycle.
- PMID:17892321 experimentally recovered Apj1 with Ssa1 and Ssa2. This makes
  `Hsp70 protein binding` the informative replacement for the two generic
  `protein binding` IPI rows.
- PMID:23329686 identifies APJ1 as a YDJ1 duplicate specialized for degradation
  of sumoylated proteins. The apj1/slx5 genetic relationship supports a SUMO-pathway
  association, but Apj1 is not a SUMO-conjugating enzyme.

## Nuclear protein quality control, not generic refolding

PMID:32492414 is the decisive APJ1-specific study. Apj1 is recruited to heat- or
proteasome-stress-induced intranuclear quality-control inclusions and promotes
turnover of insoluble nuclear clients. Loss of APJ1 delayed degradation of
nuclear-targeted misfolded proteins but *accelerated* recovery of luciferase
activity after heat aggregation. Thus the inherited `protein refolding` IBA is
removed as a family-level specialization error; the direct target outcome is
nuclear ubiquitin-proteasome quality control (new GO:0071630 IMP annotation).

The existing `protein unfolding` IMP is accepted as core because the same study
reconstitutes Hsp104-independent aggregate solubilization by Apj1 with Ssa Hsp70
and Sse1/Hsp110 in vivo and in vitro. The term captures the demonstrated
disaggregation step; Apj1 should not be described as an autonomous unfoldase.

## Heat-shock response attenuation

PMID:41025326 (2025, full text) shows that Apj1 arrives at Hsf1-regulated loci
after Hsf1 activation and promotes Hsf1 displacement from heat-shock elements.
In `apj1Δ`, Hsf1 occupancy and target expression remain elevated during the
attenuation phase. This directly supports the broad `cellular response to heat`
IBA and motivates a new `negative regulation of cellular response to heat`
annotation (GO:1900035, `involved_in`; child relationship confirmed through the
[QuickGO ontology service](https://www.ebi.ac.uk/QuickGO/term/GO:1900035) on
2026-08-27).

## Prion-curing specialization

PMID:11923285 first identified APJ1 overexpression as a suppressor of [PSI+]
propagation. PMID:38721277 resolves this activity: under Hsp104 overexpression,
the first 90 residues (J domain plus adjacent Q/A segment) are sufficient for
curing the tested strong [PSI+] variant, while neighboring segments support
distinct Sis1-like functions. This is a real specialized activity, but the
overexpression/prion-variant context is not generalized into the core function.

## Localization boundaries

- Nuclear and cytoplasmic localization are supported by the genome-wide GFP
  screen and subsequent target-specific nuclear studies.
- INQ and nuclear-periphery terms are direct but stress-specific active locations,
  so they remain non-core.
- Two mitochondrial proteomics studies detected Apj1. Those HDA rows are retained
  as non-core because independent detections may reflect a small or precursor-
  associated pool, but there is no targeting sequence or demonstrated mitochondrial
  APJ1 mechanism and they do not override the nuclear/cytoplasmic evidence.

## Project/module check

APJ1 is already in `projects/UNFOLDED_PROTEIN_BINDING.md` and its `genes.csv`.
The project row is updated to specify the interim GO:0044183 replacement and the
nuclear aggregate-to-proteasome specialization. No module currently names APJ1.

## OpenScientist refolding-hypothesis audit

The focused OpenScientist report independently rated “APJ1 has protein refolding
(GO:0042026)” as **weakly supported / partially over-annotated as a direct
function**. It correctly centered PMID:32492414 and distinguished Apj1's Hsp70
cochaperone activity from the fate of the client. Its suggested curation option
was to retain the IBA as non-core. Because the cached full text directly shows
that APJ1 deletion accelerates reporter reactivation while Apj1 promotes
proteasomal turnover, the final curator decision is the stronger REMOVE: this is
target-specific evidence that the refolding output placed at the PAINT node was
not retained as APJ1's specialization. The report remains marked UNVERIFIED as
an LLM-generated evidence synthesis; its conclusions were checked against the
primary paper, and its ancillary literature leads are not used without
independent verification.

## 2026-10-01 IBA alignment and current-GOA refresh

Forced a fresh QuickGO/UniProt fetch. The live APJ1 feed now has 22 GOA rows:
all three `GO:0051082` unfolded-protein-binding rows have disappeared after the
GO:0051082 obsoletion cleanup, and the UniProt keyword-derived `GO:0008270`
and `GO:0046872` rows are gone. The SGD RCA `GO:0008270` zinc ion binding row
remains live and continues to capture the class A zinc-binding region.

The upstream `GO:0051082` retirement deliberately retires APJ1 from the old
`UNFOLDED_PROTEIN_BINDING.md` interim `MODIFY -> GO:0044183` queue rather than
turning that historical decision into a fresh `NEW` assertion. The 2026 YAR1
refresh shows that both `GO:0140309` unfolded protein holdase activity and
`GO:0044183` protein folding chaperone now exist in live upstream GOA when SGD
chooses to assert them. For APJ1, the APJ1-specific output in PMID:32492414 is
proteasomal turnover of insoluble nuclear clients rather than generic
refolding, so there is no current APJ1 live row to modify and no strong basis
for manufacturing a new `GO:0044183` annotation.

The four remaining IBA rows were checked against
`interpro/panther/PTHR43888/PTHR43888-paint.tsv`. Added explicit
`propagation_review` source nodes for the three accepted rows:
`GO:0001671` ATPase activator activity at PTN002376157, `GO:0034605` cellular
response to heat at PTN001531327, and `GO:0005634` nucleus at PTN001180221.
The `GO:0042026` protein refolding row already carried the same PTN001531327
review and remains removed because PMID:32492414 supports APJ1-dependent
nuclear aggregate turnover rather than refolding.

PubMed/web freshness checks did not find a 2026 APJ1-specific mechanistic study
that supersedes the already-incorporated 2025 Hsf1 attenuation paper
(PMID:41025326).
