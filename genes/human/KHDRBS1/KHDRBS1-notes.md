# KHDRBS1 (Sam68) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: KHDRBS1 is the closest experimentally characterised relative of fly qkr58E-1 (Q9W255).
They are clade-level co-orthologs under PAINT node PTN000879731, the KHDRBS/Sam68-SLM clade and the IBA source for
GO:0000381. KHDRBS1 is PANTHER PTHR11208:SF30. ProtNLM2 outputs were not consulted.

Deep research: `just deep-research-falcon human KHDRBS1 --fallback perplexity-lite` failed. Falcon returned
"Failed to authenticate" and perplexity returned 401 insufficient_quota, so no deep-research file exists. This
review is built from the cached publications (several have full text), the UniProt record and the PAINT/IBA rows.

### Experimentally established in human (usable as a transfer reference)
- mRNA/pre-mRNA binding: Bcl-x mRNA [PMID:17371836 "We demonstrate that Sam68 binds the mRNA for Bcl-x and affects its alternative splicing."];
  SMN2 exon 7 [PMID:20186123 "RNA pull-down assays and UV-crosslink experiments showed that Sam68 binds to this sequence."].
- Regulation of alternative splicing: Bcl-xS, CD44 v5, SMN2 exon 7 [PMID:24514149, PMID:36537190, PMID:26080397].
- SH3 binding via proline-rich motifs and SH2 binding when tyrosine-phosphorylated [PMID:7537265, PMID:9045636, PMID:10913193].
- Nuclear, with Sam68/SLM nuclear bodies [PMID:10913193 "endogenous BRK and Sam68 colocalize in Sam68-SLM nuclear bodies (SNBs)"].
  Added as a NEW annotation, GO:0016604 nuclear body.

### PAINT propagation decisions (for transfer)
- PTN000879731 (KHDRBS/SLM clade): GO:0000381 is propagated.
- PTN000129548 (deeper STAR/BBP-like node): mRNA binding and nucleus are propagated.
- PTN002598463: poly(A) binding, with KHDRBS1 as the only donor.
- PAINT does NOT propagate SH3/SH2 domain binding, signaling adaptor activity, TCR signalling or cell-cycle terms.
  I read this as a deliberate choice: do not transfer the signalling and phosphorylation-dependent functions to the fly SF140 paralogs.
  Those functions depend on vertebrate proline-rich and tyrosine-rich C-terminal motifs (Sam68-YY domain, PF16568),
  and conservation of those motifs in the fly paralogs has not been checked.

### Notable decisions
- GO:0046833 positive regulation of RNA export from nucleus (IDA, PMID:21613532): REMOVE. The full text says
  "However, Sam68 does not increase export, either alone ( Coyle et al. 2003 ) or in combination with shRNA targeting Tpr."
- GO:0140678 molecular function inhibitor activity (DisProt EXP, PMID:36537190): REMOVE. The paper describes
  phosphorylation inhibiting KHDRBS1's own RNA binding, not KHDRBS1 inhibiting another molecule.
- GO:0046831 regulation of RNA export (ISS): UNDECIDED, because the Rev-homologue literature and the CTE literature conflict.
- Cell-cycle, apoptosis and TCR terms: non-core or over-annotated. These are phenotypes or substrate relationships, not process participation.
- Protein binding (GO:0005515): removed per policy. Where the paper shows SH3- or SH2-mediated binding, the row is
  MODIFY to SH3 or SH2 domain binding.
