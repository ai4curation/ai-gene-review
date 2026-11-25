# WWC2 notes

## 2026-11-25 gpt-rosalind-5.5

### Scope

WWC2 was reviewed for GO-CAM `65a1f4f800003542`, Cell contact inhibition by Hippo signaling (Human). No provider deep-research artifact was generated for this gene; Perplexity/Falcon were unavailable for this campaign and the review used the cached UniProt, GOA, publication and PAINT artifacts directly.

### Evidence synthesis

The core role is cytosolic Hippo-pathway scaffolding. The GO-CAM activity models WWC2 with `GO:0035591` signaling adaptor activity in cytoplasm/Hippo signaling, and this agrees with the literature-supported WWC role: the SAV/LATS study reports that "WWC proteins (WWC1/2/3) directly interact with LATS1/2 and SAV1" and that "WWC1/2/3 play an organizer role in a signaling module" for MST-dependent LATS activation [PMID:35429439].

The earlier WWC-family study supports shared WWC2/KIBRA/WWC3 behavior, including that WWC proteins can "form homo- and heterodimers" and that "all WWC proteins negatively regulate cell proliferation and organ growth" by repressing YAP transcriptional activity [PMID:24682284]. That justifies keeping the antiproliferative, organ-growth and YAP-transcription rows as downstream non-core consequences rather than elevating them to WWC2's molecular core function.

UniProt records WWC2 in the cytosol and records direct kinase interactions: "Interacts with DLC1 and PRKCZ. Interacts (via WW domains) with LATS1 and LATS2" [file:genes/human/WWC2/WWC2-uniprot.txt]. The PRKCZ binding row is therefore not Hippo core, but kinase binding is correct for both the Hippo LATS interaction and that peripheral PRKCZ interaction.

### Annotation decisions

- Bare `GO:0005515` protein binding rows were removed under the project protein-binding policy. The review does not assert that the reported YWHAZ interactions are false.
- `GO:0035331` negative regulation of Hippo signaling has the regulatory sign inverted for WWC2. WWC2 promotes the LATS/YAP-inhibitory Hippo kinase cascade, so the direct and ARBA negative-regulation rows were changed to `MODIFY` with `GO:0035332` positive regulation of Hippo signaling as the replacement.
- `GO:0035330` regulation of Hippo signaling and `GO:0060090` molecular adaptor activity were marked `TOO_GENERAL` because the more specific signed Hippo and signaling-adaptor claims are asserted in the review.
- The PAINT `GO:0016477` cell migration row was marked `MARK_AS_OVER_ANNOTATED`. The PANTHER row for node `PTN002308339` shows the IBD cell-migration transfer, but the accessible human WWC2 evidence supports SAV/LATS Hippo scaffolding rather than a WWC2-specific migration role [file:interpro/panther/PTHR14791/PTHR14791-paint.tsv].

### GO-CAM consistency

No GO-CAM conflict was found for WWC2. The model already uses the supported `GO:0035591` signaling adaptor activity in `GO:0035329` Hippo signaling and cites PMID:35429439 for the WWC2 activity.
