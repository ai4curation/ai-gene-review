# FBN2 database source guide

The 30 database contexts are recorded with complete original source objects in [FBN2-database-decisions.yaml](FBN2-database-decisions.yaml). They remain distinct from the 30 direct-paper contexts. The source objects, order, 32 seed references and two curated splice products are preserved. No supporting quotations or new annotations were added.

## Product scope

The displayed precursor is 2,912 residues. Official metadata describes mature fibrillin-2 at 78–2779 and placensin at 2780–2912; those chain boundaries are separate from the two curated splice products. The reconstructed 1,473-residue splice isoform 2 lacks the canonical C-terminal placensin region. The hormone/glucose assessments concern the C-terminal product of the displayed precursor and do not establish the same processing or activity for isoform 2.

The actual placensin study (PMID:32329225) specifies human residues 2780–2912 in Methods, while its Figure 2 caption says 2779–2912. Endogenous secretion and IP-MS support a C-terminal product, but the inspected experiments do not map its exact endogenous N terminus or demonstrate that furin is necessary. The official coordinates are retained as metadata-supported boundaries. Human recombinant ligand was tested in mouse hepatocytes, liver and mice, and in human trophoblast cells; no human glucose intervention is inferred. Recipient-cell metabolism executes glucose conversion. The narrower replacement is positive regulation of gluconeogenesis (GO:0045722), supported by the original glucose-free lactate/pyruvate hepatocyte assay and PEPCK/G6Pase induction. This remains a lateral role correction from glucose metabolism, not a claim of hormone catalysis, tracer-resolved flux or a human metabolic intervention.

## PAINT and family releases

[FBN2-phylogeny-evidence.yaml](FBN2-phylogeny-evidence.yaml) supplies the actual target path, sequence checksum, literal IBD rows, current GOA joins, public source links and acquisition provenance. Current membership is PTHR47333, named “von Willebrand factor C/EGF & Fibrillin”, with the literal SF5 label “FIBRILLIN-3”. The live PANTHER service explicitly returns release 19 and identifies P35556 as PTHR24039:SF26, “FIBRILLIN-2”. These are distinct release records, not a guessed family correction.

The actual legacy leaf PTN002513885 names human FBN2/P35556. Its ungapped 2,912-residue alignment matches the official sequence exactly. Both asserted ancestral nodes, PTN000620536 and PTN002778720, occur on its target-to-root path. The current selected IBD file has five relevant positive assertions and no NOT row. Some current GOA extant-source lists differ from the selected IBD lists; both originals remain visible. The first tree request timed out, and a successful current-family-name query to release 19 returned a family without the target. Identity-guided recovery of the actual release-19 family resolved target placement. This does not claim a complete current-release tree or renewed review of every descendant. Target self-WITH and short donor lists are not defects.

## Orthology, domain and rule evidence

The four paired ISS/Ensembl inferences cite mouse Fbn2 Q61555. Its official UniProt record identifies the Ensembl protein model ENSMUSP00000025497.6, and current QuickGO connects all four IMP donor assertions to PMID:20855508. The actual mouse study measures bone architecture, osteoblast maturation and matrix-dependent TGF-beta sequestration/signaling. Fbn2-null cells have reduced matrix LTBP1/TGF-beta, increased active TGF-beta and impaired maturation that improves when TGF-beta signaling is blocked. The study separates this regulation from a necessary mineralizing substrate. Elevated BMP signaling/calibration was shown for Fbn1-null cultures and is not transferred to FBN2. The direct Ensembl lookup failed with HTTP 503; no fresh Ensembl gene-tree replay is claimed.

Actual target-specific InterPro responses place 44 IPR001881 domain intervals and 17 IPR018097 conserved-site intervals on displayed P35556 and map both entries to calcium binding. They do not establish affinity at every repeat or calcium signaling.

The five genuine ARBA rule payloads were read. Their conditions and consequences are recorded, but a complete rerun of all FunFam matches and training examples was not performed. Independent target evidence informs the contextual elasticity, developing-eye and basement-membrane judgments. The method records describe how predictions are generated; they are not primary assays. Original rule and normal-cache bytes are unchanged.

## Reactome target routes

All nine event records genuinely contain P35556 through inspected input/output and nested entity routes. The table below lists the event-level scope. Every target leaf uses reference entity 54678 and extracellular-region compartment GO:0005576. No FBN1-only event title was used to discard FBN2 membership.

| Event | FBN2 route and scope | Review |
|---|---|---|
| [1592387](https://reactome.org/content/detail/R-HSA-1592387) | Elastic fibre → fibrillin/MFAP complex → fibrillin set → FBN2 polymer → 29–2779 entity | ACCEPT |
| [2129353](https://reactome.org/content/detail/R-HSA-2129353) | Fibrillin/MFAP input → fibrillin set → FBN2 polymer → 29–2779 entity | ACCEPT |
| [2129357](https://reactome.org/content/detail/R-HSA-2129357) | Precursor 29–2912; matrix-side 29–2779 and C-terminal 2780–2912 outputs | ACCEPT |
| [2129362](https://reactome.org/content/detail/R-HSA-2129362) | Fibrillin-peptide input includes FBN2 29–2779; output is fibrillar assembly | ACCEPT |
| [2129375](https://reactome.org/content/detail/R-HSA-2129375) | FBN2 is a nested matrix component in the tropoelastin aggregate input | ACCEPT |
| [2129385](https://reactome.org/content/detail/R-HSA-2129385) | Fibrillin set → FBN2 polymer → 29–2779 entity | ACCEPT |
| [2161282](https://reactome.org/content/detail/R-HSA-2161282) | Elastic-fibre/Fibulin/Emilin complex → fibrillin/MFAP complex → FBN2 polymer | ACCEPT |
| [2396399](https://reactome.org/content/detail/R-HSA-2396399) | Fibrillin set contains FBN2 polymer in the BMP-binding event | ACCEPT |
| [2485148](https://reactome.org/content/detail/R-HSA-2485148) | Microfibrillar FBN2 input plus modeled degradation products, including 29–? | ACCEPT |

All nine Reactome extracellular rows are ACCEPTed consistently with the other extracellular-region records. The broad term remains informative for FBN2; the mature-matrix, precursor and released-fragment distinctions remain properties of each source assessment. Positive ECM IBA row 44 is KEEP_AS_NON_CORE, aligned with verified matrix detections. The separate HDA row 42 retains source-specific UNDECIDED because the exact target join remains inaccessible. Modeled starts at residue 29 differ from the official mature-chain start 78; they remain database entity coordinates, not revised natural products. FBN2 is not assigned the protease or cross-linking activity of other event participants. These are target-route assessments, not exhaustive audits of unrelated event branches or every Reactome citation.

## Primary reading boundaries and ontology

Shared PMID assessments are whole-reference unions with the direct-paper lane. Actual main text, relevant Methods and captions were read for PMID:20855508, 32329225, 24899048, 25406291 and 15277214. The genuine original text of PMID:8120105 distinguishes bovine microfibril immunogold from human fetal tissue staining. This database lane did not independently inspect original figure pixels or supplements. Full originals recovered separately remain distinct from any abstract-only normal caches.

PMID:25406291 documents structural deposition in developing human ocular matrices. A vascular ECM precursor to the future zonule is a hypothesis, and human developmental perturbation is not claimed. PMID:15277214 directly includes human FBN2 GBM/mesangial staining despite its FBN1-focused title. PMID:24899048 places FBN2 in the central elastin layer of fetal Bruch membrane; this is not generalized to all RPE basal laminae. Descemet/anterior lens capsule and kidney evidence support bounded non-core basement-membrane location.

Official typed paths confirm microfibril → extracellular matrix/extracellular region, elasticity → structural constituent, and hormone activity → receptor agonist activity → signal transduction. Broad structural MF remains useful beyond elastic matrices. The eye terms GO:0048048 and GO:0043010 have no demonstrated strict path in the tested direction and are not collapsed by their labels. GO:0045722 is a verified direct is_a child of GO:0010907, but the replacement from imported GO:0006006 is still a lateral regulatory-role correction. It is not an ancestor or descendant of retained glucose homeostasis (GO:0042593). The current reviewed FBN1/asprosin record also corrects its raw GO:0006006 assertions to regulation; placensin's more specific assay scope supports the narrower gluconeogenesis term. FBN1's GO:0007189 pharmacological pathway support is not transferred to placensin, whose cAMP/PKA response alone does not determine receptor class. Signal-transduction row 34 remains TOO_GENERAL relative to retained hormone activity.
