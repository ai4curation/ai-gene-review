# ESA1 curation notes

## Update 2026-09-02

Batch audit of the existing `ESA1-ai-review.yaml`. The review is otherwise thorough
(63 GOA lines all reviewed, sound REMOVE/KEEP_AS_NON_CORE calls), but one citation in
`core_functions[0].supported_by` was wrong:

- The entry cited `PMID:11742990` ("The Saccharomyces cerevisiae Set1 complex includes
  an Ash2 homologue and methylates histone 3 lysine 4", Roguev et al. 2001 EMBO J) with
  `supporting_text` equal to that paper's own title, offered as support for ESA1's core
  histone-acetyltransferase molecular function (GO:0004402) plus its involvement in
  transcription regulation (GO:0006357) and DNA repair (GO:0006281).
- `publications/PMID_11742990.md` (cached abstract) is about the **Set1/COMPASS**
  H3K4-methyltransferase complex and does not mention ESA1/Esa1 anywhere
  [PMID:11742990 "The Saccharomyces cerevisiae Set1 complex includes an Ash2 homologue
  and methylates histone 3 lysine 4"] — an unrelated methyltransferase complex, not the
  NuA4/Esa1 acetyltransferase this review is about. This is a genuine miscitation (right
  format, wrong paper), not merely a weak citation.
- Fixed by replacing it with `PMID:9520405` ("ESA1 is a histone acetyltransferase that
  is essential for growth in yeast", Smith et al. 1998 PNAS), which is already used
  elsewhere in this review's `existing_annotations` (GO:0004402 IMP evidence line) and
  directly supports the claim: [PMID:9520405 "we express a yeast ORF with homology to
  MYST family members and show it possesses histone acetyltransferase activity"].
- No other content, actions, or GO terms were changed. `PMID:31699900` (crotonylation)
  remains as the second `supported_by` entry, unchanged.

Everything else reviewed (all `existing_annotations`, the `description`, and the rest of
`core_functions`) was judged sound and evidence-backed; no further changes made in this
pass. Note: this gene directory also carries several non-standard files
(`ESA1-CURATION-ANALYSIS.md`, `ESA1-CURATION-SUMMARY.md`, `ESA1-ai-review-CURATED.yaml`,
`ESA1-ANNOTATION-TRIAGE.tsv`, `README-CURATION.md`, `FILES-INDEX.md`,
`ESA1-DECISIONS-OVERVIEW.txt`, `ESA1-CURATION-COMPLETE.md`) left over from an earlier
curation pass; left untouched here since removing/consolidating them is outside the
scope of this citation fix.

## 2026-10-01 current-GOA / IBA review

- Refreshed ESA1 from current UniProt/GOA before editing. Current GOA has 76
  live rows after the header; the refresh expanded the YAML from 63 to 86 rows
  by adding 23 current assertions that were absent from the older review.
- Preserved 10 historical source assertions as `retired: true`: the old generic
  `GO:0004402` IBA, four old UniProt keyword rows under `GO_REF:0000043`, one
  broad ARBA stress row, and three old consolidated IntAct `GO:0005515` rows
  whose exact source signatures are absent from the current GOA export.
- Checked `interpro/panther/PTHR10615/PTHR10615-paint.tsv`. Six live IBA rows
  still trace to the broad MYST/KAT ancestor `PANTHER:PTN004172926`; the newly
  materialized `GO:0010485 histone H4 acetyltransferase activity` IBA row traces
  to the fungal Esa1/NuA4 node `PANTHER:PTN000834946`. Both placements match
  yeast Esa1 biology, and the ESA1 self-donors are direct experimental seeds,
  not circularity.
- Resolved the new rows conservatively. New direct `GO:0004402` HAT rows, NuA4
  and Piccolo complex rows, the broad DNA-damage response row, the
  protein-lysine-acetyltransferase row, the histone H4 IBA, and the
  crotonyltransferase row were accepted. The ComplexPortal nucleosome `part_of`
  row was removed because NuA4/Piccolo bind nucleosome substrates but Esa1 is
  not part of a nucleosome. The fission-yeast ISS
  `GO:0106226 peptide 2-hydroxyisobutyryltransferase activity` row remains
  `UNDECIDED` pending source-side review.
- Converted all generic `GO:0005515 protein binding` rows to `REMOVE`. The
  IntAct interactions may be real, but the bare binding rows add no functional
  information beyond Esa1's NuA4/Piccolo complex membership and catalytic
  annotations.
- Searched 2024-2026 literature for exact yeast ESA1/NuA4/Tip60 updates. The
  2024 NuA4/Pah1/nuclear-shape paper (PMID:38961766) extends the existing
  lipid-metabolism/Pah1 context, and the 2025 Gcn5/Esa1/RSC-occupancy paper
  (PMID:40958614) fits the existing chromatin/transcription-regulation calls.
  The 2025 Piccolo NuA4 cryo-EM study (PMID:40100634) and the 2026
  NuA4/Sfp1/ribosome-biogenesis paper (PMID:42103225) are additional context.
  None justify new ESA1 GO rows beyond the accepted acetyltransferase,
  complex, chromatin, and Pol II transcription-regulation assertions.
