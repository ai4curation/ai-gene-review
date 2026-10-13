# CTLA4 curation notes

## 2026-09-04 (PAINT no-IBA project finishing pass)

Reviewed the full `CTLA4-ai-review.yaml` draft (all actions pre-assigned). CTLA4 is
the inhibitory checkpoint counterpart to CD28, competing for CD80/CD86 with higher
avidity. Core MF `receptor decoy activity` (GO:0140319) and the NEW `signaling
receptor inhibitor activity` (GO:0030547) are well grounded in the two crystal
structures [PMID:11279501; PMID:11279502 "Signalling through CD28 augments the T-cell
response, whereas CTLA-4 signalling attenuates it"].

Changes made this pass:
1. `DNA damage response` (GO:0006974, IMP, PMID:17875758): changed action
   REMOVE -> UNDECIDED. This is an experimental annotation and the cached publication
   is abstract-only (full text unavailable). The paper's title foregrounds ATM (a
   DNA-damage gene), so removing on the basis that "DNA damage belongs to ATM" is
   exactly the move the project guidance forbids for experimental annotations whose
   full text we cannot read. Reason text updated to flag it as a likely theme-transfer
   over-annotation while deferring to the curator's unseen full-text evidence.
2. Added structured `propagation_review` to the `B cell receptor signaling pathway`
   IBA (GO:0050853, node PTN000160996, MARK_AS_OVER_ANNOTATED). root_cause
   SOURCE_WEAK_OR_INFERRED; the IBD node is seeded by CTLA4's own weak IMP for the
   same term (the same correlative B-CLL expression study, PMID:17875758), and CTLA4
   acts in the TCR/CD28 axis, so BCR signaling does not transfer confidently
   [PMID:17875758 "the overexpression of CTLA4 and MNDA was associated with good
   outcome"].
3. Added a deep-research supporting citation to the LRBA trafficking annotation
   (PMID:26206937) to satisfy the "no annotations reference deep research" warning
   [file:human/CTLA4/CTLA4-deep-research-falcon.md "recycling to the surface (e.g.,
   after TCR stimulation) is regulated by LRBA and Rab11 pathways"].

Confirmed sound: the whole PMID:17875758 cluster (BCR signaling, neg reg B-cell
proliferation, pos reg apoptosis) as MARK_AS_OVER_ANNOTATED — all from one CLL
differential-expression paper, correlative rather than mechanistic. Trafficking/
localization annotations (Golgi, clathrin-coated vesicle, perinuclear region, external
side of PM) accepted, consistent with CTLA4's constitutive endocytosis biology.

Both warnings cleared; validates clean with no PENDING. Status IN_PROGRESS -> COMPLETE.

Action tally: 31 ACCEPT, 19 MARK_AS_OVER_ANNOTATED, 1 NEW, 1 UNDECIDED.

## 2026-10-13 — substantive annotation and source audit

This entry supersedes the September judgments where they conflict. The prior journal, all historical source assertions, source caches, provider output and history remain intact. The old COMPLETE label did not substitute for a new scientific assessment. The current raw annotation response contains 56 records. The review retains the original 51 machine assertions and the historical authored NEW, then adds two genuine current plasma-membrane EXP assertions separately. Two historical keyword-derived records are absent currently; their supported biology remains accepted. None of these source-reconciliation changes manufactures a NEW annotation.

CTLA4's compact core remains receptor decoy activity at the external plasma-membrane surface, with inhibition of T-cell activation and TCR signaling. The two structural originals directly establish CD86/CD80 binding, not a cellular signaling experiment or obligatory membrane lattice. The first uses refolded human extracellular domains; the second uses CHO-expressed, cleaved human domains including CTLA4 C122S. Its actual publisher correction supplies PDB 1I8L (DOI 10.1038/35079149). Neither engineered soluble domain is automatically one of the official truncated products. The genuine full main of [PMID21474713](https://doi.org/10.1126/science.1202947) directly demonstrates ligand capture/depletion, human T-cell/DC blocking and repurified-DC responder assays, and restoration of CD86 costimulation. CHO construct experiments and mouse in vivo experiments are distinguished from the human experiments. Supplementary Methods, movies and figure pixels were not inspected.

The historical authored signaling-receptor-inhibitor NEW is retired because its definition requires inhibitory binding to a receptor. The measured CTLA4 targets here are CD80/CD86 ligands, limiting their access to CD28; direct CTLA4–CD28 binding is not established. This is a molecular-role correction, not an ancestry claim: receptor decoy activity is not a typed descendant of signaling receptor inhibitor activity. Both actual GO-CAM activities use CD80/CD86 as input and directly negatively regulate the ligand activity, which connects onward to CD28. No redundant NEW is introduced.

The negative-Treg-differentiation annotations are refined to negative regulation of T-cell proliferation. The full indexed original [PMID18641304](https://doi.org/10.4049/jimmunol.181.3.1683) shows acquisition of suppressive function and CTLA4-dependent reduction of responder CFSE division/thymidine uptake, with transfection and antibody reversal. This is not inhibition of Treg differentiation. The actual 98-node tree and 98-entry alignment give the exact 223-aa human target on the relevant ancestral path. The on-path PTN000160996 IBD legitimately uses the human experimental self seed. The correction concerns the shared experimental term scope, not donor count, circularity or a missing ancestral node. The broader TCR-signaling IBD is genuinely grounded in mouse Cd28 evidence and is retained at a regulatory-participation scope, without transferring an activating sign.

The previous T-cell-only treatment of the CLL annotations was unsound. The original [PMID17875758](https://doi.org/10.1158/1078-0432.CCR-07-0283) remains full-text unresolved; its abstract cannot exclude unseen experiments. Independent [PMID23936412](https://doi.org/10.1371/journal.pone.0070352) provides actual antisense/siRNA perturbation in primary human CLL: increased proliferation/Ki-67 after CTLA4 depletion and reduced Annexin-V/CD19 apoptosis in three low-CD38/high-CTLA4 samples after 72 hours. These positive disease-context functions are retained as non-core. The BCR-pathway and DNA-damage-response assertions remain undecided because the accessible experiments do not directly resolve a BCR-crosslink-initiated cascade or a defined DNA-damage response. This does not demand a direct mechanism for every regulation term. The old 17875758 reference is preserved and is not declared miscited from its title or abstract.

Supported generic interactions are individually retained or refined. The current IntAct/MINT queries contain 136 complete 42-field records, with 24 exact source/partner matches for the reviewed rows; all 48 participant backbone ROGIDs match official sequences. Construct features remain separate. Human CTLA4–CD80/CD86 binding supports a decoy refinement through independent functional corroboration; the PLA record is explicitly proximity in HeLa cells. HuRI TMEM218/MALL/CTXN3 interactions remain positive and non-core without invented physiological roles. LRBA associations remain non-core with full-source and direct-contact limits. The three p85 records support the specific PI3K regulatory-subunit binding class, not CTLA4 kinase activity. Historical paper Tyr165 and current precursor Tyr201 numbering are kept distinct; the original numbering convention was not recovered.

The authentic [PMID7544393](https://doi.org/10.1084/jem.182.3.667) original separates CD28-positive/CTLA4-negative Jurkat adhesion from soluble CTLA4-Ig binding to CD80 transfectants. The adhesion-complex annotation is therefore overextended at this experiment's scope. Positive CTLA4–CD80 binding remains valid; this is not a universal assertion that CTLA4 complexes can never contribute to adhesion.

The five official products reconstruct exactly as 223/56/58/79/174 residues and match official FASTAs. The product named ss-CTLA-4 is only 56 residues and lacks an intact ligand-binding Ig domain; its name must not be equated with the engineered soluble ectodomains in structural or therapeutic experiments. Products 2/3 lack the intact IgV/native transmembrane segment, product 4 retains only a partial Ig segment, and product 5 changes/removes canonical transmembrane/cytoplasmic sequence. These are sequence observations, not measured secretion, ligand binding or inhibitory equivalence. The original machine product IDs, names and VSP slots are unchanged.

All 19 current ARBA00043397 branches were evaluated: only zero-based branch 14 matches the actual FunFam and human Euteleostomi lineage, yielding external side of plasma membrane. The exact InterPro family mappings and historical UniProt keyword/subcellular mappings remain distinct sources. Eight donor joins retain complete literal source records and experimentally grounded support, with source accession/species checked. The rat Ctla4 proliferation donor's antibody does not block B7 binding; its specific assay properties are not generalized to every CTLA4 mechanism.

Five current Reactome events were followed through 75 objects and nine exact target paths. CTLA4 is a membrane complex participant, phosphorylation substrate or expression output as appropriate, not a kinase, phosphatase or transcription factor merely because the event contains those activities. The current SHP2 event itself acknowledges uncertain/possibly indirect contact. The two GO-CAM models and their literal relations are separately retained in the public evidence index.

Access remains source-specific. The selected 33961781 cache carries a full-text flag but contains Introduction/Discussion rather than full Methods. The 32822567 target workbook and 40205054 exact CTLA4 network record were not recovered; independent evidence supports the underlying ligand/LRBA interactions without pretending those tables were read. The 35922511 genuine publisher workbook was reused with its original receipt: Table 3 contains literature-grounded CD80/CD86 pairs and Table 2 the primary screen matrix. Its correction concerns CLC4M, an affinity-unit label and Methods citations. The 40205054 correction changes a duplicated loss-function equation, not a CTLA4 interaction. All caches retain their original flags and bytes. Failed PDF/XML/HTML routes remain recorded as failures, and scan notices are not labeled full articles.

The existing genuine Falcon report was read and preserved as contextual research. Its review/clinical/preprint leads and automated quality labels are not substitutes for original experimental evidence. The public source-evidence file records literal assertions, target records, ontology and access boundaries; computational checks authenticate those records but do not replace scientific reading.

## Final source-snapshot representation

The source audit above assessed 54 distinct objects. The final review YAML preserves the original 52 objects; the two additional genuine current EXP plasma-membrane assertions, PMID:18468488 and PMID:18641304, are retained with their complete source objects and assessments in `CTLA4-source-evidence.yaml` under `supplemental_current_annotations`. This supersedes the earlier statement that they were added to the review list. They remain active current source annotations, not NEW proposals or retired records. Plasma-membrane biology is already represented by the retained historical annotations, and the references remain in the review. This representation permits validation against the preserved historical GOA snapshot without inventing a merged source file or discarding current evidence.


## PR #4989 finite follow-up — 2026-10-13

The four supported generic-binding assertions remain non-core under the explicit [ClinGen project curation instruction](https://github.com/ai4curation/ai-gene-review/blob/f2e26020e5367cc0f5a33dad6b89724c5b9e31a1/projects/CLINGEN_MENDELIAN.md#L2976-L2978). This instruction was already present at the reviewed head and deliberately differs from the general annotation-reviewer informational-exclusion default. LRBA co-purification/trafficking and the three HuRI partners retain their separate assay and access limits; no unmeasured adaptor activity is inferred. The four corresponding advisories and derived DRAFT status remain expected. The seven decoy refinements now name the actual CD80/CD86 WITH/FROM accession in each reason. Those fields identify the ligand; functional ligand sequestration is supported by the independent experiments, not by the partner field alone.

The biological description and decoy core again explain canonical type-I topology, Ig-V domain, disulfide-linked dimerization, stronger B7 binding than CD28, ligand depletion and regulated surface trafficking. The official [P16410 record](https://www.uniprot.org/uniprotkb/P16410/entry) grounds the domain/topology, disease and precursor Tyr201 statements. The [PMID:9398332 abstract](https://doi.org/10.1021/bi971762i) distinguishes unphosphorylated AP-2 binding from phosphotyrosine-dependent p85 binding; its Tyr165 is historical paper numbering and is not relabeled as a verified mature-chain coordinate. The [PMID:21474713 original](https://doi.org/10.1126/science.1202947) directly demonstrates ligand depletion and the constitutive Treg context. The clinical examples identify opposite uses of this pathway: ipilimumab blocks CTLA4 (PMID:28484017 abstract), whereas abatacept is a soluble CTLA4-Ig fusion (PMID:26206937 abstract). The IDAIL statement follows the official disease annotation; no new common-variant risk claim or disease-mechanism annotation is proposed.

Canonical receptor biology does not establish equivalent activity for all five official products. Their exact 223/56/58/79/174-aa sequences and the distinctions between physiological products, soluble Ig fusions and structural fragments remain as previously recorded. These evidence boundaries belong here and in the source-specific assessments, rather than replacing the biological summary.

The selected publication caches and their access flags are unchanged. For [PMID:18641304](https://pmc.ncbi.nlm.nih.gov/articles/PMC2758479/), the separately accessed original Materials and methods (suppression, transfection and CFSE) and Results/Figure 6 show inhibition of responder-cell division and PPD responses. For [PMID:7544393](https://doi.org/10.1084/jem.182.3.667), the [authentic original PDF](https://pdfs.semanticscholar.org/a325/d82f81ccb82f2390c42f4d85326966c27719.pdf), Methods pp. 668–669, adhesion Results/Figure 2 on p. 670, and CTLA4-Ig binding Results on pp. 671–672/Figure 4, separates CD28-positive/CTLA4-negative Jurkat adhesion from soluble CTLA4-Ig binding. The public evidence index now records these direct locators and the recovered PDF hash. Indexed text and PDF text access are distinguished from image-pixel or supplementary analysis.

Exact opening-sentence repetition between summaries and reasons was removed, and four repeated electronic-source comments now describe the specific family/rule output. No action, term, evidence code, qualifier, product, core term, reference identity, or supporting quotation changed. The two current EXP membrane assessments remain complete supplemental current assertions; the historical GOA snapshot, existing provider file and prior history remain intact.


## 2026-10-13: source-specific binding uncertainty

Re-review comment 6154075418 identified that independent support for an interaction does not settle every source-specific assertion. Rows 16 (PMID:26206937) and 21 (PMID:40205054) are now UNDECIDED because their original target binding records remain unadjudicated. The positive CTLA4–LRBA record from PMID:33961781 remains KEEP_AS_NON_CORE, as do the recovered HuRI interactions. This applies the project's inaccessible-evidence clause without claiming the interaction is false or changing the generic-binding retention policy. All 52 source objects, five products, core functions, quotations and source caches are preserved.
