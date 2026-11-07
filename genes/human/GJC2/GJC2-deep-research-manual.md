# GJC2 manual evidence and source boundaries

## Human channel experiments

[PMID:17344063](https://pmc.ncbi.nlm.nih.gov/articles/PMC1937038/) reports human Cx47 dye transfer and paired-cell currents. Selected original sections were read. Tissue evidence is rhesus; mutant ER retention is separate.

[PMID:19056803](https://doi.org/10.1093/brain/awn328) separates surface plaques from channel function: I33M has defective homotypic coupling and altered heterotypic gating. The published Methods cite AF014643, whose sequence differs from AY285161 at historical residues 80 and 249; the actual plasmid sequence is unavailable. Historical I33 maps to current I36. Figure 7 includes a reused WT curve; contemporary WT controls are also reported. Opposing-cell pairing is not heteromeric coassembly. Selected original text and Figure 7 were inspected.

## Mouse donor and myelin context

[PMID:11160382](https://pmc.ncbi.nlm.nih.gov/articles/PMC3671913/) tests mouse Cx47 in HeLa cells and Xenopus oocytes, untagged or C-terminally EGFP-tagged. Historical 437-residue construct equivalence to current Q8BQU6 remains unresolved. Selected Methods/Results/captions were read. Its neuronal-localization interpretation is not used to override later glial evidence.

[PMID:20578039](https://doi.org/10.1002/glia.21032) supplies mouse myelin evidence: antibodies label WT but not knockout tissue, and immunoprecipitation distinguishes specific Cx47 from nonspecific crude Western bands. Cuprizone-associated redistribution does not demonstrate that Cx47 synthesizes myelin. Selected original IHC, immunoprecipitation and discussion passages were read; no figure pixels or supplement were inspected here.

The actual [mouse Q8BQU6](https://www.uniprot.org/uniprotkb/Q8BQU6/entry) experimental records include GO:0005243 and GO:0005921 IDA from PMID:11160382 and GO:0043209 IDA from PMID:20578039. The latter retains a mouse anatomical extension, without copying it into the human row. Official Ensembl maps ENSG00000198835 to ENSMUSG00000043448 as one-to-one orthologs; ENSMUSP00000104421 is the incoming mouse protein. Human-return inferred mouse rows are not used as experimental donor evidence.

## Human immunofluorescence

The [HPA GJC2 record](https://www.proteinatlas.org/ENSG00000198835-GJC2/subcellular) reports HPA069619 plasma membrane and cytosol staining in EFO-21 and SH-SY5Y, and cytosolic staining in U2OS. Overall reliability is supported, while the antibody subassay carries uncertainty. These cell-line observations are not direct human myelin imaging. The retained XML and image descriptions were read, without inspecting image pixels.

## Ancestry and ontology

The actual PTHR11984 tree has 948 nodes and 497 leaves. Human Q5T442 is AN478/PTN002485539 below AN0/PTN008334405. The three IBDs for GO:0005243, GO:0007267 and GO:0005922 are at AN0, with their original donor groups retained. The target alignment recovers all 439 residues; the four transmembrane intervals are 26–46, 79–99, 217–237 and 266–286. No relevant ancestral negative record was found on this target path. Neither donor count nor experimental target self-inclusion is treated as a failure.

GO:0007267 and GO:0010644 are direct is_a children of GO:0007154. The broad existing communication row is therefore TOO_GENERAL. GO:0005243 describes a pore through each adjacent membrane, supporting direct transport without assuming unapposed hemichannel function. GO:0005922 describes the connexin complex; this does not establish a particular native heteromeric composition.

## Clinical and background references

[PMID:15192806](https://pmc.ncbi.nlm.nih.gov/articles/PMC1216059/) supports disease linkage and human tissue transcripts, rather than direct channel or myelin-protein localization assays. [PMID:20537300](https://pmc.ncbi.nlm.nih.gov/articles/PMC3032064/) supports a lymphedema association; its channel and lymph-flow mechanisms remain hypotheses. Selected original sections were read for both. PMID:15489334 and PMID:16710414 were assessed from authentic abstracts as sequence-resource background. The Reactome assembly pathway is background; its Cx43-specific trafficking text is not transferred to GJC2.

## Product boundary

The current canonical record is Q5T442, 439 residues. Historical constructs and uncertain initiation do not establish a second natural isoform. The sequence and its hash are retained in the source archive; a canonical-only product slot is not added to the review.

## Reproducible deposited-sequence comparisons

The [local comparison](GJC2-bioinformatics/README.md) parses the two original GenBank CDS translations and the cached UniProt sequence. It reproduces the human accession comparisons and residue-number mapping above. The mouse 437-residue construct remains a reported experimental length, with equivalence unresolved; no mouse sequence reconstruction is claimed.
