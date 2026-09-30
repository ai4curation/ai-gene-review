# LCP2 (SLP-76) curation notes

Project: ADAPTIVE_IMMUNITY, T cell receptor trunk.

## Deep research

- `just deep-research-falcon human LCP2 --fallback perplexity-lite` was run. The first
  background run's log was overwritten by a concurrent job, and no
  `LCP2-deep-research-*.md` file was produced. It was re-run; see the status at the end of this file.
  The review was done from UniProt, GOA and cached publications, not from deep research.

## Biology summary (with provenance)

- Cloned as a 76 kDa substrate of the TCR-activated tyrosine kinase pathway that associates with GRB2. It has no catalytic domain and carries SH2/SH3 recognition motifs
  [PMID:7706237 "Although no recognizable motifs related to tyrosine, serine/threonine, or lipid kinase domains are present in the predicted amino acid sequence, it contains several potential motifs recognized by SH2 and SH3 domains"].
- ZAP70 phosphorylates SLP-76 N-terminal Y113/Y128, creating binding sites for the VAV1 SH2 domain
  [PMID:9047237 "only ZAP-70 phosphorylates SLP-76 at specific sites that allow Vav SH2 domain binding"]. NCK binds the same pY sites
  [PMID:10229072 "Y113 and Y128 phosphopeptides could compete binding of SLP-76 to the SH2 domain of Nck"].
- The GADS C-SH3 binds the SLP-76 RxxK motif with nanomolar affinity, which links SLP-76 to LAT
  [PMID:17235283 "the Gads C-terminal SH3 domain binds a core RxxK sequence motif in the SLP-76 scaffold"]; crystal structure of the motif 233-PSIDRSTKP-241 [PMID:17010654].
- The C-terminal SH2 domain binds phospho-ADAP/FYB1 [PMID:10570256, PMID:22074159], ARAP/FYB2 [PMID:27335501] and CD6 [PMID:24584089].
- SLP-76-deficient Jurkat (J14): TCR is uncoupled from PLCG1 and Ras
  [PMID:9665884 "coupling of TCR-regulated PTKs to downstream signaling pathways requires SLP-76"].
- ITK activation requires SLP-76 and ongoing binding to it [PMID:17420479]. Y173, phosphorylated by ITK, is needed for PLCG1 phosphorylation in T and mast cells [PMID:21725281].
- Mast cells: SLP-76-/- BMMCs fail to degranulate or secrete IL-6 after FcERI crosslinking [PMID:10377180].
- Platelets: SLP-76 and LAT are needed for PLCG2 activation downstream of GPVI/FcR-gamma and CLEC-2 [PMID:18826392].
- NF-kB/PKC-theta: needs ZAP70/SLP-76 [PMID:11313406]; GLK/MAP4K3 is activated by binding SLP-76 [PMID:21983831].
- Human disease: biallelic LCP2 variants cause combined immunodeficiency with neutrophil and platelet defects [PMID:33231617] (UniProt IMD81).

## Curation decisions

- **MF:** signaling adaptor activity (GO:0035591), the child of the IBA term protein-macromolecule adaptor activity (GO:0030674), which is accepted.
- **Protein binding (62 IPI rows):**
  - MODIFY when the paper states the mechanism:
    - SH2 domain binding for the pY motifs bound by VAV1 or NCK SH2.
    - SH3 domain binding for the RxxK/proline-rich motifs bound by GADS, GRB2 or PLCG1 SH3.
    - Phosphotyrosine residue binding for the SLP-76 SH2 binding pY of ADAP, ARAP or CD6.
    - Signaling adaptor activity for the complex-assembly papers (ITK, PLCG1, NCK/VAV1, GLK).
  - REMOVE for the high-throughput Y2H and AP-MS screens, and for the STAM/STAM2 SH3-array cross-reactivity, which the authors say has no physiological correlate.
- **GO:0007169** (RTK signaling, IBA and TAS): MODIFY to the TCR signaling pathway. The TCR, FcERI and GPVI have no intrinsic kinase activity, and GO does not place the TCR pathway under GO:0007169.
- **Cell-cell junction** (Ensembl IEA): MODIFY to immunological synapse. In GO, immunological synapse is not under cell-cell junction.
- **Plasma membrane raft** (IDA PMID:20551903): UNDECIDED. The cached full text has no mention of rafts.
- **Positive regulation of protein kinase activity** (IEP PMID:14624253): MARK_AS_OVER_ANNOTATED. This is expression-pattern evidence, and SLP-76 is used there only as a mutant background.
- **Mast cell activation** (IBA): KEEP_AS_NON_CORE.
- **NEW terms:**
  - Fc-epsilon receptor signaling pathway (GO:0038095), IMP PMID:10377180.
  - Collagen-activated signaling pathway (GO:0038065), TAS PMID:18826392.
  - Both pass the participation test: SLP-76 does the adaptor work in these pathways, as in TCR signaling.

## Open issues

- Should a kinase activator MF be added for ITK (PMID:17420479)?
- Is there direct evidence for raft localization?
