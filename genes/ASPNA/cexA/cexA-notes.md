# cexA (CexA, citrate exporter A) — Aspergillus niger ATCC 1015 — review notes

UniProtKB:G3Y4N5 (CEXA_ASPNA; strain ATCC 1015, NCBITaxon:380704; ORF names
ASPNIDRAFT2_1165828, ASPNIDRAFT_57285; synonym citT). The sequence is identical
(524 aa, zero differences) to UniProtKB:A0A254TZW7 (CEXA_ASPNG, N402/ATCC 64974
genome entry). The full literature notes, including the CMMMech grounding assessment,
are in `genes/ASPNG/cexA/cexA-notes.md`; the points below are specific to this entry.

## Evidence specific to the ATCC 1015 entry

- GOA rows here come from Steiger et al. 2019 (Metab Eng, PMID:30553933; IMP, IC) and
  Erian et al. 2020 (FEMS Yeast Res, PMID:32990722; IGI with Y. lipolytica Cex1,
  UniProtKB:Q6C8F0), plus the EXP plasma-membrane row from Alves et al. 2023
  (PMID:37216016), which used the AlphaFold model of this accession.
  [PMID:37216016 "The Alphafold AF-G3Y4N5-F1-model_v4 structure was used in this work."]
- Disruption abolishes citrate secretion and re-routes metabolism to oxalate.
  [PMID:30553933 "The disruption of this gene completely abolishes citric acid secretion, which indicates that this protein is the main citric acid transporter in A. niger."]
  [PMID:30553933 "In the disruption strain, the metabolism is re-routed mainly to oxalic acid, which is a known by-product during citric acid production."]
- Cex1 complements an A. niger export-deficient strain (abstract only; full text not cached).
  [PMID:32990722 "Likewise, expression of YALI0D20196p complemented the ability to secrete citrate in an export-deficient strain of Aspergillus niger, confirming a citrate export function of YALI0D20196p."]
- Both cached abstracts for PMID:30553933 and PMID:32990722 are abstract-only; the
  IMP/IGI rows are accepted because the function they assert is established
  independently by full-text papers (PMID:31062025, PMID:34071072, PMID:37216016).
- Steiger et al. describe CexA as DHA1 ("drug-H+ antiporter") family, but Alves et al.
  found transport independent of the proton motive force:
  [PMID:37216016 "Citrate uptake was independent of the proton motive force and compatible with a facilitated diffusion mechanism."]

## UniProt free-text issue

Same INDUCTION comment as in A0A254TZW7: "repressed by Mg(2+) ions" where the cited
papers (PMID:38076415, PMID:39377610) report manganese(II). Probably "Mn(2+)".

## CMMMech note

CMMMech annotation_notes ground ATCC 1015 records to G3Y4N5 with "locus
ASPNIDRAFT_56962"; that locus is not among the entry's ORF names (ASPNIDRAFT2_1165828,
ASPNIDRAFT_57285). See the ASPNG notes for the functional_role assessment (oxalate and
manganese caveats).
