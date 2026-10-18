# ECHS1 evidence guide

ECHS1 is a mitochondrial enoyl-CoA hydratase. The principal evidence supports one catalytic function operating in fatty acid beta-oxidation and valine catabolism. Its other substrate reactions and protein associations have different evidential scopes and are not interchangeable.

## Human substrate chemistry and disease

[PMID:26251176](https://pubmed.ncbi.nlm.nih.gov/26251176/) is the key human biochemical study. The operative Methods, Results, Table 2 and Figure 4 were examined in an [archived original PDF](https://web.archive.org/web/20240413153104if_/https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=5923b113057f4548be71733a93d326c1eec3aeb1). Its SHA-256 is `0b1c96c82e0b44dea4118463eed88d0387466147a7a4fbb9879cdff1588c1d2b`. The unchanged publication cache contains an abstract; the separate original provides the additional assay detail.

The preparation expressed human ECHS1 in HEK293 cells and was partially purified 51-fold. It was not homogeneous enzyme. Crotonyl-CoA, acryloyl-CoA, 3-methylcrotonyl-CoA and tiglyl-CoA were assessed by direct hydration measurements. Methacrylyl-CoA activity was measured using a coupled assay with rat HIBCH. ECHS1 performs the hydration step; HIBCH performs the subsequent hydrolysis. Weak but nonzero tiglyl turnover does not establish a major human isoleucine-catabolic role.

The exact GO:0043956 reaction is acryloyl-CoA/3-hydroxypropionyl-CoA. The valine reaction instead uses methacrylyl-CoA/3-hydroxyisobutyryl-CoA. The earlier two-core presentation conflated these substrates. The revised core uses GO:0004300 and retains both supported fatty acid and valine process contexts. The specific acryloyl and crotonyl annotations remain positive substrate-level evidence within that enzyme function.

[PMID:25125611](https://pubmed.ncbi.nlm.nih.gov/25125611/) was available at abstract scope: patient-cell loss of ECHS1 protein/activity and wild-type rescue support disease attribution. Its unseen Methods are not reconstructed. [PMID:40056416](https://pubmed.ncbi.nlm.nih.gov/40056416/) was also available only as an abstract. It reports methacrylation and mitochondrial phenotypes in ECHS1/HIBCH-deficient cells and fly tissues. The imported matrix IDA and valine IMP assertions are retained with curator deference and independently established ECHS1 biology, without claiming to have inspected that paper's target-specific localization assay.

The official product is a 290-residue precursor with a cleaved targeting segment at residues 1–27 and a mature chain at 28–290. These are processed forms of one product, not alternative splice isoforms. No artificial isoform identifier is introduced.

## Minor isomerase and lysine-derived metabolite context

The human isomerase annotation is explicitly inferred from rat ECHS1/P14604. The complete abstract of [PMID:10074351](https://pubmed.ncbi.nlm.nih.gov/10074351/) reports rat wild-type isomerization and active-site mutant effects, with isomerization much weaker than hydration. This is positive evidence for the accessory activity; a human isomerase rate and its physiological flux remain unresolved. The original human cloning paper [PMID:9073515](https://pubmed.ncbi.nlm.nih.gov/9073515/) attributes hydratase activity and beta-oxidation but does not provide the specific rat isomerase assay.

[PMID:37198486](https://pubmed.ncbi.nlm.nih.gov/37198486/) connects lysine-derived crotonyl-CoA metabolism with ECHS1 expression in human glioma cells. Selected operative Results and Methods cover lysine tracing, ECHS1 perturbations and GCDH/CBP dependencies. ECHS1 depletion or overexpression changes histone crotonylation and growth in this metabolic context. The positive lysine-catabolism assertion is retained as non-core. ECHS1 is not assigned the histone-modifying activity of CBP/P300 or other crotonylation enzymes.

## Binding records and construct scope

The [reproducible evidence extracts](ECHS1-evidence/README.md) retain complete selected interaction records, including species, experimental features, host context and stable interaction identifiers. A feature describing a sufficient binding region is not evidence that the reference-sequence checksum authenticates the exact experimental insert.

| Source | Positive evidence and limits | Interpretation |
| --- | --- | --- |
| [23416296](https://doi.org/10.1016/j.febslet.2013.02.005) | Publisher Results 3.1, Figure 1 caption and Discussion excerpt were available; complete Methods were not. MINT records distinguish human STAT3 yeast two-hybrid/endogenous HepG2 assays from mouse Stat3 used in tagged HEK293T experiments. | DNA-binding transcription factor binding. Human host cells do not make a mouse construct human; no ECHS1 DNA-binding or phosphatase activity is inferred. |
| [24510904](https://pubmed.ncbi.nlm.nih.gov/24510904/) | Main Methods describe GST-LRRK2 and full-length Flag-LRRK2 protein-array screens and controls. The literal curated pair is ECHS1–LRRK2; the target supplementary table was not recovered. | Protein kinase binding, with screen-level scope. Follow-up on other partners is not ECHS1 validation. |
| [24947832](https://pubmed.ncbi.nlm.nih.gov/24947832/) | The main original distinguishes LRRK1/LRRK2 protein arrays from cell-based AP-MS. Literal records identify both kinase partners, while the imported assertion retains its LRRK2 context. The target supplement was unavailable. | Protein kinase binding. No ECHS1 phosphorylation or kinase activity is claimed. |
| [31046837](https://pubmed.ncbi.nlm.nih.gov/31046837/) | Human-cell Myc-LRRK2 AP-MS records include wild-type and G2019S contexts. The supplementary Table S1 lists 232 enriched proteins, a subset of 2,831 identified proteins; it has no literal ECHS1 accession. | The subset absence does not refute the wider curated association. The SERCA functional follow-up is not an ECHS1 experiment. |
| [14557246](https://pubmed.ncbi.nlm.nih.gov/14557246/) | Figure 1 and Methods describe human ECHS1 precursor recognition by TOMM20 and TOMM22 fragments, including translated precursor/GST receptor assays with GST controls. | Positive generic binding retained as non-core. TOMM20/Q15388 and TOMM22/Q9NS69 are mitochondrial import receptors, not signaling receptors under GO:0005102. ECHS1 is the imported precursor, not an import receptor or chaperone. |

GO:0140297 requires binding to a DNA-binding transcription factor; verified STAT3 class and the interaction evidence satisfy this definition. GO:0019901 requires binding to a protein kinase; verified LRRK2 class and its curated associations support that refinement without a requirement to demonstrate catalytic-site recognition. These classifications describe what ECHS1 binds, not what activity it acquires from the partner. Supported generic binding without an informative demonstrated refinement follows the explicit exception in [the project instructions](../../../projects/CLINGEN_MENDELIAN.md).

## Localization and reaction models

The [HPA target record](https://www.proteinatlas.org/ENSG00000127884-ECHS1/subcellular) labels the individual mitochondrial location as enhanced. The XML includes A-431, U-251 MG and U2OS staining contexts. This supports mitochondria, not a matrix-specific imaging claim or universal exclusion from other pools.

The MitoCoP study [PMID:34800366](https://pubmed.ncbi.nlm.nih.gov/34800366/) supplies an exact P30084/ECHS1 entry in supplementary Table S1, sheet A physical row 337, and in its gene inventory, sheet B row 305. The relevant Methods describe subtractive and spatial proteomics and importomics in human cells. Selected fields can be regenerated from the original workbook using the linked extraction script. No isoform-specific interpretation is made from the target protein group.

The endothelial-proteomics source [PMID:16130169](https://pubmed.ncbi.nlm.nih.gov/16130169/) was verified at abstract scope. Its target-specific table was unavailable. The historical mitochondrial TAS assertion remains consistent with independently established ECHS1 localization; abstract absence is not used to allege a curation error.

The normal Reactome hydration events resolve through catalyst 71049, ECHS1 hexamer 71048 and human mature-chain entity 54125, residues 28–290. The beta-oxidation pathways contain the corresponding hydration events rather than merely mentioning ECHS1 in a narrative. R-HSA-70895 contains the valine reaction R-HSA-70870; this supports the broader branched-chain pathway through valine without requiring equal participation in every branch.

[R-HSA-9916717](https://reactome.org/content/detail/R-HSA-9916717) is a FailedReaction. Its `normalReaction` is R-HSA-70870; its mutant catalyst has loss-of-function status and separates characterized members from uncharacterized candidates. The imported activity annotation refers to the normal ECHS1 activity being deficient, not successful catalysis by the mutant set. Its matrix compartment is curated model evidence, not variant-by-variant microscopy.

## Phylogeny and source lifecycle

The current PAINT tree and alignment contain an exact 290-residue human target. Its 25-node path includes the mitochondrial IBD at PTN000235143 and beta-oxidation IBD at PTN000941828, without a target-lineage loss event. The latter's ECI1 donors support a shared beta-oxidation process, not transfer of their specific enzyme activity. Legitimate target self-grounding and small donor counts are not treated as circularity or weakness.

The historical 49 source assertions remain intact. Historical index 10 is retired solely because its exact electronic source context is absent from the new snapshot; GO:0170035 is also currently obsolete, and the biological review proposes valine catabolism. Four current partner assertions are appended as genuine imports, not NEW annotations. The [source provenance](ECHS1-source-provenance.yaml) identifies the unchanged archived historical GOA bytes and the current normal snapshot. The earlier notes remain preserved as a historical prefix; the appended dated assessment supersedes their mistaken partner identities, reaction conflation and access statements.
