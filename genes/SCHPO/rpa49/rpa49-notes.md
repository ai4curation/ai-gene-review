# rpa49: functional evidence

Rpa49, also characterized as RPA51, is a Pol I-specific accessory subunit in the nucleolus. It supports efficient ribosomal DNA transcription and transcription elongation by RNA polymerase I. It is functionally conserved with budding-yeast A49 and acts within the polymerase complex rather than providing an independent RNA-polymerase catalytic center.

- [PMID:12893961] "Transcripts analysis in vivo and in vitro shows that RPA51 plays a
general role for maximizing transcription of rDNA whereas it is dispensable for
non-specific transcription."

Evidence interpretation: sequence/domain records are used for family placement; AI descriptions and ARBA labels are not independent validation. Family transfer is limited to conserved properties and is identified as inference. Genome-scale localization annotations are retained where consistent with the biology; an abstract does not expose every individual observation. All original annotation rows are preserved.

ProtNLM provenance: pre-release `post-processed-2026_02_28k.xml`, exact entry and all evidence keys preserved in the source XML/JSON. These current Swiss-Prot entries are absent from the public TrEMBL pilot. Known-function overlap does not establish model training membership. See the function sidecar for atom-by-atom paragraph assessments.

Research provenance: the gene-focused Falcon report was generated concurrently with publication caching. The report was inspected for source leads; the biological decisions above rely on the cited primary records and specified family evidence.

The completed Falcon search has retrieval gaps: its inability to locate target-level localization is not used to override PomBase’s HDA records. Curated genomic-screen observations and the directly inspected papers take precedence over an empty literature-search result.

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Scope: full re-review of all 10 GOA rows, the description and the core functions. ProtNLM2 files were not opened or used.

Identity: O14086 is the canonical reviewed Swiss-Prot entry (425 aa, single chain PRO_0000073954, A49 family signatures IPR009668 / PF06870 / PTHR14440 across the protein). It is not a fragment, isoform or alternative gene model. The original paper reports 415 aa for RPA51 [PMID:12893961 "a protein of 415 amino acids exhibiting 30% and 19% identities to A49 and PAF53"]; the 10-residue difference is an annotated start-site difference, and the C-terminal two-thirds that carry function are intact.

Evolutionary grounding: PTHR14440 has a single subfamily. The S. pombe target, S. cerevisiae RPA49 (Q01080, SGD:S000005192), mouse Polr1e (MGI:1929022) and human POLR1E (Q9GZS1) all descend from PAINT node PTN000374345, which donates the IBA rows. Cross-species complementation of S. cerevisiae rpa49Delta by rpa51+ [PMID:12893961] independently places the target in the functional clade. So transferring the budding-yeast A49 mechanism (tWH DNA binding, TFIIF-like dimerization module with A34.5, Rrn3 recruitment and release) is justified as family-level inference.

New evidence: S. pombe Pol I cryo-EM [PMID:33536435 "The presence of the A49/A34.5 subunit-complex in Pol I preparations was confirmed by Coomassie−stained SDS-PAGE (Supplementary Fig. 1a) and mass-spectrometry analysis."]. The heterodimer is not resolved in the density ("Both, EC and monomeric Pol I, lack cryo-EM density for the A49/A34.5 heterodimer"). Review comparing yeast and mammalian heterodimers: PMID:33921963.

Changes:
- nucleus (HDA): ACCEPT -> MODIFY to nucleolus (GO:0005730), which the same screen and the gene already carry.
- DNA-templated transcription (IEA): MODIFY now proposes both supported descendants, GO:0006362 and GO:0001188 (ancestry checked in OLS).
- Localization rows no longer quote UniProt `DR GO` lines, which restate annotations; they now cite the curated subcellular-location CC line and the screen abstract.
- The other rows are unchanged in action (ACCEPT); the reasons were rewritten with PAINT-node and ortholog grounding.
- Core functions: added preinitiation complex assembly to the Pol I core function and added a DNA-binding core function (family inference).
- PANTHER family review interpro/panther/PTHR14440/PTHR14440-review.yaml: no disagreement; single subfamily, with rpa49 as reference protein.
- Module: modules/dmel_nuclear_rna_polymerases.yaml (Drosophila nuclear RNA polymerases; Pol I includes Polr1E, the fly ortholog). No S. pombe Pol I module exists.
- Next relative: S. cerevisiae RPA49 (Q01080). It is the best-characterised member of the same PAINT clade, and genes/yeast/RPA49 has no review.
