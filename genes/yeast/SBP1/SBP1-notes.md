# SBP1 review notes

## Identity correction

The canonical *S. cerevisiae* gene symbol for UniProt P10080 / YHL034C is **SBP1**.
Older literature used **SSB1** or **SSB-1** for this single-stranded RNA-binding
protein. That historical synonym caused this review to be stored under `SSB1`,
colliding with the unrelated ribosome-associated Hsp70 gene **SSB1** (P11484).
This review and its source files were therefore moved to the canonical `SBP1`
path; fetched and provider-generated content was retained unchanged.

## Evidence re-audit

- The historical nucleolar annotations remain credible but non-core. The original
  study reports that SSB-1/Sbp1 colocalized with fibrillarin in the yeast nucleolus
  and co-immunoprecipitated snR10 and snR11 [PMID:2121740, "SSB-1 colocalized with
  fibrillarin in a double-label immunofluorescence mapping experiment to the yeast
  nucleolus"].
- Cytoplasmic translation control is the best-established core role. Sbp1 directly
  binds eIF4G and represses translation through its RGG motif [PMID:22284680,
  "Npl3 and Sbp1, also directly bind eIF4G and repress translation in a manner
  dependent on their RGG motifs"]. Full-text experiments further show cooperative
  binding of the two RRMs to the A-rich region in the PAB1 5' UTR and inhibition of
  both cap-dependent and cap-independent initiation [PMID:28986506, "a decreased
  translation activity in the presence of an increasing amount of Sbp1 indicated an
  inhibitory function of this protein in both cap-dependent and cap-independent
  initiation of the Pab1 mRNA"].
- The PMID:35440550 evidence is specifically for **P-body** disassembly, not stress
  granule disassembly: the abstract identifies Sbp1 as a P-body disassembly factor,
  reports defective disassembly in `sbp1`-null cells, and shows that Sbp1 competes
  with Edc3 self-interaction [PMID:35440550, "Sbp1-Edc3 interaction competes with
  Edc3-Edc3 interaction"]. The existing `MODIFY` decision to replace stress granule
  disassembly with protein-containing complex disassembly is retained. The related
  core function is localized only to the P-body; stress-granule localization remains
  a valid, condition-dependent non-core annotation.

## Review outcome

The existing annotation decisions remain evidence-consistent after re-audit: RNA
and mRNA binding, translation repression, eIF4G binding, and cytoplasmic localization
are core; P-body/stress-granule and historical nucleolar localizations are retained as
non-core; generic protein-binding annotations remain over-annotated. No experimental
annotation was removed on the basis of incomplete full text.
