# LCP2 (SLP-76) curation notes

Project: ADAPTIVE_IMMUNITY, T cell receptor trunk.

## Deep research

- `just deep-research-falcon human LCP2 --fallback perplexity-lite` was run. The first
  background run's log was overwritten by a concurrent job, and no
  `LCP2-deep-research-*.md` file was produced. The re-run's wrapper reported failure: falcon timed out
  after 600s, and the perplexity-lite fallback errored with "Provider 'perplexity' not available".
  The falcon client still completed in the background at 13:54, after about 1186 s, and wrote
  `LCP2-deep-research-falcon.md`.
  The review was done from UniProt, GOA and cached publications. The deep-research report was read
  afterwards and cited as corroboration on the collagen-activated signaling NEW row. The report was
  later regenerated; see "Deep research integration (falcon)" below for the current version.

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

## Deep research integration (falcon)

The regenerated `LCP2-deep-research-falcon.md` (Edison, 24 citations) was re-read in full. It rests
almost entirely on secondary reviews (Rudd 2021, Dadwal 2021, Borowicz 2020, Balagopalan 2021, Katzav
2023, Liu 2023, Hakami 2026, an unidentified 2023 Chinese review). The only primary paper is Yamane et al.
2026. The regenerated report no longer contains the sentence the review had quoted on the collagen
NEW row ("SLP-76 contributes to platelet activation and aggregation..."). It also no longer mentions
neutrophils or NK cells, contrary to what the note above originally said.

Claim tally: about 27 substantive claims. 19 confirm the review, 4 add something new, 0 conflict with it,
and 4 are not relevant or unsupported.

**Confirms review (19):** non-catalytic adaptor; ZAP70 phosphorylation; Y113/Y128 bind VAV1 and NCK;
Y145 and ITK; Y173 needed for PLCG1 activation in T and mast cells; GADS C-SH3 binds the central
RxxK/PRR and bridges to pLAT; SH2 binds pADAP; ADAP-SKAP1-Rap1-LFA-1 inside-out signaling; HPK1
association; cytosolic at rest and recruited to LAT microclusters; immunological synapse; PLCG1/Ca2+/NFAT;
PKC-theta/NF-kB; Ras/ERK; actin and cytoskeleton; DN3 block in thymocyte development; GPVI in platelets;
FcERI in mast cells; SAM domain at the N-terminus.

**Adopted (adds new):**
- The weak, conserved PRR185-200 / PLCG1 SH3 interaction in the LAT-GADS-SLP-76-PLCG1 tetramer tunes TCR
  signal strength. Raising its affinity (SLP-76HA) increases PLCG1 activity, perturbs thymocyte
  selection, CD8 central memory and Tfh responses. Verified in PMID:42660881 (full text, mouse). Added
  to the description and to core_functions[0] supported_by, plus a suggested question.
  [PMID:42660881 "the conserved weak SLP-76/PLC-γ1 interaction is important for the controlled activation of PLC-γ1, thus fine-tuning TCR signal strength to optimize T cell-mediated immunity"]
- HPK1 phosphorylates Ser376 as negative feedback. The report cited only a review; the primary source
  is PMID:17353368, which also shows the pS376 site recruits 14-3-3. Added to the description and to
  core_functions[0] supported_by. No annotation was added: SLP-76 is the substrate here, and
  HPK1 performs the step.
  [PMID:17353368 "a novel negative feedback loop involving HPK-1-dependent serine phosphorylation of SLP-76 and 14-3-3 protein recruitment, which tunes T cell activation"]
- SLP-76 binds SUMO-RANGAP1 at NPC cytoplasmic filaments via K56, and this promotes NFATC1 and p65 nuclear
  entry. The primary source is PMID:26321253 (Rudd lab, Jurkat J14 and mouse). Added to the description
  with hedged wording ("has been reported"). No NEW CC or BP annotation was made because the finding comes
  from a single lab and GOA has no such annotation. Raised as a suggested question and a suggested experiment.
- Report quoted in core_functions[0] for the "non-enzymatic scaffold" framing.

**Not acted on / rejected:**
- Clinical claims (checkpoint biomarker, antisense, 145pTyr peptides, CAR-T speculation): not relevant
  to GO function, and the Chinese review is unidentified ("Unknown journal").
- BCR signaling in CLL: rests only on the unidentified Chinese review, so no primary source.
- c-Cbl-dependent microcluster internalization: this is a property of the microcluster, not an
  SLP-76 activity. Not needed.
- Treating the integrin/LFA-1 or NF-kB branches as separate processes: the report itself calls these
  indirect consequences. The review keeps the process at TCR signaling, so no NEW process terms.

**Report errors / embellishments detected:**
- It calls the weak SLP-76/PLCG1 interaction a "kinetic proofreading mechanism". This phrase does not
  appear in PMID:42660881. It also calls the study "landmark"/"paradigm shift", which is overstatement.
- Domain boundaries are approximate. The SH2 is given as about 420-510, but UniProt has 422-530.
  The SAM is given as about 12-78, but UniProt has 15-81.
- HPK1-Ser376 and RanGAP1 are attributed to a review rather than to the primary papers.
- The Tyr145-ITK assignment is self-flagged as unverified in the report. The review already supports
  ITK recruitment via ZAP70-phosphorylated N-terminal tyrosines (PMID:17420479, PMID:21725281).
- No wrong PMIDs were found (the report gives DOIs only). The DOI for Yamane 2026 resolves correctly to
  PMID:42660881.

**Fix for the regenerated report:** the stale falcon quote on the GO:0038065 NEW row was replaced with a
current verbatim sentence ("SLP-76 participates in ITAM-receptor signaling downstream of the collagen
receptor GPVI, ...").

**Annotation actions:** no existing-annotation actions were changed. The report contains no primary
evidence that contradicts any decision.
