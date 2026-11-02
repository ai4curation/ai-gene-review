# HOXA2 (horse, Equus caballus; UniProt F7DP63) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

No ProtNLM2 output was opened or used.

### Deep research
`just deep-research-falcon HORSE HOXA2 --fallback perplexity-lite` failed: falcon returned
"Edison API request failed: Failed to authenticate" and the perplexity-lite fallback also
failed (HTTP 403 Forbidden). No deep-research file exists; the review uses cached publications
read directly.

### Identity / gene model
- F7DP63 is unreviewed (PE 3), 404 aa, Ensembl model ENSECAT00000000353.4. It is the only horse
  HOXA2 entry in UniProt.
- Horse RefSeq XP_001499478.2 is 373 aa and has the canonical HOXA2 N-terminus (MNYEFEREIG...).
- F7DP63 residues 1-85 are a non-homologous N-terminal segment; the conserved 54-residue
  N-terminus is missing. From residue 86 onward F7DP63 matches RefSeq at 318/319 positions,
  with intact YPWM hexapeptide (126) and a homeodomain identical to human 143-202 (F7DP63
  171-230). [file:HORSE/HOXA2/HOXA2-bioinformatics/RESULTS.md]
- UniProt SignalP signal peptide 1-32 lies in the spurious segment: a gene-model artefact. HOXA2
  is a nuclear TF; no secretion is expected.
- Conclusion: F7DP63 is an alternative (likely erroneous 5' exon) gene model of horse HOXA2; DNA
  binding and PBX-interaction determinants are intact, so the TF-level annotations still apply.

### Evolutionary placement
- PANTHER PTHR45664:SF3 (HOMEOBOX PROTEIN HOX-A2), same subfamily as human O43364, mouse
  P31245, rat P31246, chicken Q08727 (interpro/panther/PTHR45664/PTHR45664-entries.csv). No
  PANTHER family review exists for PTHR45664; no subfamily disagreement.
- IBA rows come from PTN005228379, a deep node whose donors include Drosophila FBgn0000166 and
  FBgn0004053 and mammalian Hox2/Hox3 paralogs: TF activity, cis-regulatory DNA binding,
  nucleus and regulation of Pol II transcription are ancestral and appropriate.
- Ensembl Compara IEA rows (GO_REF:0000107) project mouse Hoxa2 (P31245) experimental
  annotations: GO:0001227/GO:0000978/GO:0043565 from PMID:15634706 (Six2 promoter binding and
  repression), GO:0048706/GO:0060037/GO:0061061 from PMID:25889273 (Hoxa2 overexpression in
  CNCC). GO:1990837 projects human O43364 IDA from HT-SELEX (PMID:28473536).

### Literature (mouse ortholog; same PANTHER subfamily)
- Hoxa2 represses Six2 directly in second-arch mesenchyme [PMID:15634706 "Hoxa2 binds to this
  promoter region"].
- ChIP-seq: Hoxa2 binds Hox and Pbx-Hox motifs genome-wide [PMID:22223247]; acts as a
  tissue-specific cofactor enhancing Meis binding at second-arch enhancers [PMID:25640223].
- Knockout: second-arch skeletal elements transformed into first-arch-like elements; cleft
  palate [PMID:7903600]; r2-r3 hindbrain identity and motor-axon pathfinding defects
  [PMID:9367425].
- Ectopic Hoxa2 transforms first-arch CNCC derivatives into second-arch-like structures
  [PMID:25889273]. The abstract says nothing about muscle; the muscle structure development
  row is weakly supported and likely non-cell-autonomous.
- Human HOXA2 homeodomain variant p.Q186K causes recessive microtia with hearing impairment
  and partial cleft palate [PMID:18394579].

### Relative
- Mouse Hoxa2 (P31245, MGI:96174), same PANTHER subfamily SF3, carries the bulk of the
  experimental annotation; no repo review (genes/mouse/Hoxa2 absent). Human HOXA2 (O43364) is
  also unreviewed. Donkey HOXA2 (genes/EQUAS/HOXA2, A0A9L0JBM7) is the paired cohort target.
- Side observation: MGI cites PMID:7508007 for Hoxa2 GO:0021568/GO:0021569, but the cached
  record is an SV40 T-antigen PNET paper. This looks like a mis-keyed reference on the mouse
  side; check it when mouse Hoxa2 is reviewed.

### Modules
- modules/neural_crest_gene_regulatory_network.yaml covers cranial neural crest; its deep-research
  file mentions Hoxa2 regulation, but the module does not list HOXA2 as a part.
