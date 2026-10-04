# CACNA2D4 evidence notes

## Scope and source identity

Manual review of the seven existing human CACNA2D4 annotations, using the annotation-reviewer and core-function-synthesizer skills. UniProt Q7Z3S7 is the 1137-residue human alpha2delta-4 precursor (sequence version 2; CRC64 BF7FD169E1AF34F7). All source annotation fields and six alternative products (1, 2, 4, 5, 6, 7) remain unchanged. The current product list must not be replaced with the four historical splice variants described in the original cloning article. UniProt records an alternative-initiation caution for an earlier sequence; its current sequence is retained.

Normal source fetching, authenticated artifact recovery and ROOT's exclusive import supplied the UniProt/GOA/review seed and PMID:17033974. The existing exact PMID:12181424 cache was preserved. Raw source caches are not edited. The family cache provides PTHR10166 metadata and entries, but no positive PAINT IBD/tree/alignment was recovered for PTN000018330. No matching CACNA2D4/Q7Z3S7 entry was found in the current local GO-CAM index. These observations are limits on this review, not evidence that curated family or GO-CAM assertions are absent globally.

## Direct human channel evidence

PMID:12181424, Molecular cloning and characterization of the human voltage-gated calcium channel alpha(2)delta-4 subunit was read in full at the cached abstract level and checked against official PubMed. The paper distinguishes alpha1 pore formation from auxiliary regulation, and reports functional association of human alpha2delta-4 with CaV1.2/beta3 in HEK293 cells. Increased calcium entry supports regulatory activity and participation in the functional channel complex. The same abstract reports a negative gabapentin-binding assay. Endocrine tissue expression does not establish a separate endocrine function. Full text was not accessed; no unreported surface-trafficking assay, native human retinal electrophysiology or absolute channel stoichiometry is inferred.

This is the basis for refining both existing voltage-gated calcium-channel molecular-function rows to GO:0005246 calcium channel regulator activity. It preserves the positive experimental result and locates the molecular action in the auxiliary subunit. The original transport-process annotation is retained: alpha2delta-4 does active regulatory work in the transport complex, although alpha1 provides the pore. No new transport or regulation-process annotation is added.

The IBA is a considered ancestral assertion, and the presence of Q7Z3S7 in its descendant evidence is expected. Donor count and self-inclusion are not defects. The direct target-level distinction between auxiliary regulation and pore conductance motivates the proposed activity refinement; without the positive PAINT reconstruction, the upstream cause is left unresolved rather than assigned to an invented evolutionary loss or faulty node placement.

## Human retinal disease and the light-detection annotation

PMID:17033974, Mutation in the auxiliary calcium-channel subunit CACNA2D4 causes autosomal recessive cone dystrophy was read as a complete cached abstract. It identifies a homozygous truncating variant in two siblings and places the protein in retinal ribbon-synapse signaling. The official PubMed figure caption distinguishes the photoreceptor a-wave from the secondary neuronal b-wave. It does not by itself provide a complete mechanistic adjudication of the source GO:0050908 annotation.

The [official GO:0050908 definition](https://amigo.geneontology.org/amigo/term/GO%3A0050908) describes receiving light and converting it into a molecular signal. Disrupted transmission from a photoreceptor can impair visual responses downstream of light detection. PMC access returned a browser challenge and Europe PMC was inaccessible through the browsing tool. Accordingly the IMP light-detection row remains UNDECIDED; the annotation is not removed or confidently reclassified from an abstract or isolated figure caption. GO:0007601 visual perception is broader, but a specific replacement is withheld pending evidence sufficient to review the curator's original claim.

## Rod and cone mechanism from recovered normal full-text caches

Two additional normal references were recovered from the successful exact-head fetch and authenticated transport. Both cached abstracts were read completely. The 2017 XML extraction repeats aggregate sections and individual paragraphs; the targeted individual Methods, Results and Discussion were read. For the 2018 HTML fallback cache, targeted Methods, Results and Discussion were read. Images and supplementary material were not independently inspected. These are mouse experiments, not native human retinal assays.

PMID:28262416 uses an exon8-disrupted mouse line. Native retinal recordings show a substantial reduction in rod calcium-current density and altered voltage sensitivity. Photoreceptor photocurrents and light sensitivity remain intact, while rod-to-ON-bipolar transmission fails. Cone transmission persists with reduced efficiency; its relatively intact ribbon/synapse findings do not mean cone calcium regulation is normal. Cellular ELFN1 coassociation and rescue support a coordinated synaptic complex, but purified ELFN1 ectodomain pull-down was negative. Thus binary direct binding and an independent ELFN1-binding activity are not established here.

PMID:29875267 uses an independent exon2-disrupted mouse line. Rod-terminal calcium imaging corroborates reduced functional channel activity. Serial electron-microscopy Results identify fewer normal cone postsynaptic triads despite relatively preserved ribbons. This resolves a difference in the structural endpoint emphasized in the earlier study; it should not be reduced to either universal cone sparing or identical rod and cone phenotypes. Residual native channels persist, so an absolute requirement for forward channel trafficking is unwarranted. The small a-wave loss in older mutants is discussed alongside degeneration and does not alone establish participation in primary light detection.

These studies strengthen the existing auxiliary-regulator/complex/transport interpretation. The human light-detection IMP remains unresolved because the original complete article was inaccessible and its precise curator evidence was not reconstructed. No NEW synaptogenesis, binary-binding, trafficking or phototransduction annotation is introduced.

## Protein architecture and core-function choice

The human UniProt record supports a large extracellular region, signal peptide and C-terminal membrane anchor. The broad existing membrane annotation is accepted. Domain/MIDAS information assigned by similarity is not converted into a new experimentally demonstrated metal-binding function. UniProt's proposed alpha2/delta cleavage is explicitly uncertain in vivo; neither proteolysis nor an alternative anchoring mechanism is asserted as established. Its subunit prose also includes alpha2-2/delta-2 nomenclature in this alpha2delta-4 record; the raw record is preserved, and the inconsistent names are not propagated into this biological summary.

One core function captures GO:0005246 calcium channel regulator activity, in the GO:0005891 voltage-gated calcium-channel complex at a membrane, directly supporting GO:0070588 calcium-ion transmembrane transport. The [official regulator-activity definition](https://amigo.geneontology.org/amigo/term/GO%3A0005246) matches the experimentally demonstrated modulation. The core does not assign pore-forming activity to the auxiliary subunit, add a drug-binding function, or imply that retinal disease alone proves participation in the initial phototransduction step.

## Decisions and evidence limits

The final seven-row candidate has four ACCEPT decisions (two independent complex-membership rows, membrane, and calcium transport), two MODIFY decisions (the two channel-activity rows to regulator activity), and one UNDECIDED decision (specific light detection). There are no NEW or PENDING rows. All source assertions and products remain exact. The two normal mouse references refine the mechanistic explanation without changing those decisions or expanding the annotation inventory. Independent ROOT peer review is required before canonical application.

## Normal research-provider attempt

The ordinary isolated Falcon research command was attempted on 2026-10-04 at 04:00:23 UTC. Falcon and its perplexity-lite fallback failed, returning exit code 1 after approximately 4.9 seconds; no provider report or artifact was produced. The preserved failure log is 107226 bytes, SHA256 47160e853eaca5b4d7e580c694969b29511d08302ff9ef6a4fa98a8c491dd24c. The assessment and receipt reside under `tmp/CACNA2D4-deep-research-attempt/`. These manually authored notes are not a provider-generated research report. This failure did not prevent reviewing the primary sources available above.

## Review validation and provenance

The initial seven-row candidate passed normal validation including authored GO-term checks without curation warnings, and its rendered page contains the exact candidate YAML. An exploratory filename first triggered the expected GOA-path naming guard; validation passed when the standard CACNA2D4-ai-review.yaml basename was used. Final integration preserves the seven source records, six alternative products and single core function. The additional source caches retain their exact fetched titles and content, with source-access limits recorded manually. The artifact/source assessment preserves all original five canonical source preimages and identifies exactly two new normal publication caches. No provider report, family annotation, GO-CAM assertion or protein isoform was manufactured.
