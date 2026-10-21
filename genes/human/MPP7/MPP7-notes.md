# MPP7 (human, Q5T2T1) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: MPP7 is reviewed as the closest experimentally characterised vertebrate relative
of DROME/metro (A1Z8G0). This review is of MPP7 in its own right. No ProtNLM2 output was
consulted.

### Deep research

`just deep-research-falcon human MPP7 --fallback perplexity-lite` failed: falcon returned
"Failed to authenticate", and the perplexity-lite fallback returned HTTP 401 (insufficient
quota). No deep-research file exists. The review is built from the cached publications
(18 GOA-cited PMIDs plus PMID:29091764, fetched for this review) and the UniProt record.

### Evolutionary placement (PANTHER 19.0, local classification files)

- Human MPP7 Q5T2T1 and mouse Mpp7 Q8BVD5 are in PTHR23122:SF39 ("MAGUK P55 SUBFAMILY MEMBER 7").
- Drosophila metro A1Z8G0 and C. elegans magu-1 Q95XW5 are in PTHR23122:SF42.
- MPP3 is in SF33 and MPP4 in SF34. PALS1/sdt are in SF14, and CASK is in SF40 (fly CASK and worm lin-2 are in SF7).
- The two clade-level IBA rows (plasma membrane, cell-cell junction) come from
  PTN001137125, the MPP/PALS clade node, which includes MPP7. The only donor for the
  "protein localization to adherens junction" IBA (PTN002750930) is MPP7 itself.
  That node therefore appears to be an MPP7-lineage node: PAINT did not place this
  process at the clade level.
- For transfer to Metro: MPP7 and Metro are in different subfamilies. Only the
  clade-level terms (plasma membrane / cell-cell junction) have PAINT support for
  inheritance. The MPP7-specific experimental functions (LIN7-dependent DLG1
  recruitment, adherens-junction targeting, TJ function) are not phylogenetically
  placed at the clade level.

### Experimentally established in human (with species and system)

- MPP7 C-terminal L27 heterodimerizes with LIN7A/B/C. The N-terminal L27 then binds DLG1, but only in the
  MPP7-LIN7 context, giving a 1:1:1 tripartite complex that localizes to adherens junctions in an
  MPP7-dependent manner [PMID:17237226 "The tripartite complex forms in a ratio of 1:1:1 and localizes to epithelial adherens junctions in a manner dependent upon MPP7."]
  (abstract only in cache).
- Crystal structure of the 4-L27-domain core of the Dlg1-MPP7-Mals3 complex
  [PMID:20702775 "the loop αA-αB and helix αB of the C-terminal L27 domain of MPP7 play a critical role in assembling the entire tripartite complex"].
- Endogenous DLG1-MPP7 interaction, and lateral membrane targeting via L27N and DLG1. MPP7 binds PALS1 via its SH3-HOOK region,
  and the CRB3 association is indirect. shRNA in Caco-2 delays TER recovery after calcium switch
  [PMID:17332497 "Loss of either hDlg1 or MPP7 from epithelial Caco-2 cells results in a significant defect in the assembly and maintenance of functional tight junctions."].
  Caveat in the same paper: occludin/ZO-1 localization was unaffected
  [PMID:17332497 "This may suggest that MPP7 and the Dlg/Scrib group of polarity proteins are not required for cell junction assembly, but rather for some functional activity perhaps related to its dynamic stability."].
- PRBH (basic-hydrophobic) motif fragment is cortical in Drosophila S2 cells and is released
  by aPKC [PMID:26481050 "The candidate MPP7 PRBH was highly enriched at the cell cortex and aPKC expression inhibited cortical localization"].
  This is a fragment assay in a heterologous system.

### Mouse-only

- Mpp7 is a CREB target. With AMOT, it is needed for YAP1 nuclear accumulation and
  satellite-cell expansion [PMID:29091764 "MPP7 and AMOT are required for YAP1 nuclear accumulation, and the three are individually required for a proliferative state in myoblasts."].
  This is used in the description only and is not proposed as a human annotation.
  A later paper on the L27 domain and TAZ-YY1 (PMC11624273) was found by web search but not cached
  or used.

### Decisions summary

- 36 bare protein-binding rows. The three LIN7 rows from PMID:17237226 are MODIFIED to L27 domain binding (GO:0097016).
  All high-throughput rows are REMOVED under the GO:0005515 policy.
- Adaptor terms are MODIFIED to protein complex scaffold activity (GO:0140378): two molecular adaptor activity IDA rows and two
  signaling adaptor activity NAS/TAS rows. MPP7 holds the complex together. No signalling pathway role is shown.
- General location terms (membrane, plasma membrane IBA, cell junction, cell-cell junction IBA)
  are MODIFIED to the specific supported descendants that the gene already carries.
- Cadherin binding (proximity-labelling HDA) and CRB3 domain-specific binding (indirect via PALS1)
  are marked over-annotated.
- No NEW annotations proposed.
- The remaining validation warning is for the three GO:0019904 rows. They are judged on different partners, so their
  actions differ on purpose.
