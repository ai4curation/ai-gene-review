# CDC14A — evidence and review notes

## Biological synthesis — 2026-10-09

CDC14A is a protein phosphatase whose defining activity is removal of phosphate from protein substrates, preferentially at proline-directed phosphoserine sites. Purified human catalytic-domain measurements establish this preference; low threonine efficiency does not negate the broader serine/threonine class. The available evidence does not settle the exact human protein-phosphotyrosine assay behind the older dual-specificity characterization. pNPP hydrolysis and membership in the PTP structural family cannot substitute for that assay. [PMID:22117071](https://pubmed.ncbi.nlm.nih.gov/22117071/), [PMID:9367992](https://pubmed.ncbi.nlm.nih.gov/9367992/).

The human ciliary mechanism includes direct DBN1 dephosphorylation and altered growth after CDC14A perturbation. This is catalytic participation in regulation, beyond a requirement inferred solely from a phenotype. The existing cilium-assembly assertion is refined to regulation of cilium assembly, GO:1902017. The experiments do not resolve every downstream actin or vesicle effect. [PMID:30467237](https://pubmed.ncbi.nlm.nih.gov/30467237/).

CDC14A has several demonstrated cell-cycle substrates. The primary APC study reports that human CDC14A “dephosphorylates hCdh1 and activates APC(Cdh1).” This supports a regulatory contribution to mitotic exit. It does not establish an indispensable yeast-like exit mechanism in human cells. In RPE1, single and double CDC14A/CDC14B knockouts retain mitotic timing and cytokinesis, while ciliary behavior changes. The older cytokinesis RNAi result is preserved as an unresolved context-dependent discrepancy. [PMID:11598127](https://pubmed.ncbi.nlm.nih.gov/11598127/), [PMID:33328327](https://pubmed.ncbi.nlm.nih.gov/33328327/), [PMID:11901424](https://pubmed.ncbi.nlm.nih.gov/11901424/).

Human CDC14A also dephosphorylates CDC25B in biochemical assays; inhibition of CDC25A in cells has a distinct mechanistic boundary. Direct MAPK6/ERK3 binding and dephosphorylation support the two Reactome events. The SIRT2 abstract provides another protein-substrate example. These findings support phosphatase catalysis without transferring the substrates' kinase, deacetylase or other activities to CDC14A. [PMID:20956543](https://pubmed.ncbi.nlm.nih.gov/20956543/), [PMID:18235225](https://pubmed.ncbi.nlm.nih.gov/18235225/), [PMID:20236090](https://pubmed.ncbi.nlm.nih.gov/20236090/), [PMID:17488717](https://pubmed.ncbi.nlm.nih.gov/17488717/).

## Compartments, species and products

Human centrosomal localization is established independently of the original high-throughput centrosome annotation. The exact CDC14A supplement entry in PMID:21399614 was not inspected, so the source review remains UNVERIFIED while the location is accepted using direct human evidence. Selected experiments distinguish centrosomal CDC14A from nucleolar CDC14B. An export-defective CDC14A mutant's nucleolar accumulation cannot establish physiological wild-type nucleolar activity. [PMID:11901424](https://pubmed.ncbi.nlm.nih.gov/11901424/), [PMID:12134069](https://pubmed.ncbi.nlm.nih.gov/12134069/), [PMID:21399614](https://pubmed.ncbi.nlm.nih.gov/21399614/).

Human CDC14A was observed at spindle poles and the central spindle during anaphase, with MKlp2-dependent recruitment and in-vitro INCENP dephosphorylation. The retained spindle is_active_in assertion is a PAINT inference with these experiments as corroboration; no direct spatial catalytic-turnover assay was inspected. Later human experiments support regulated cellular distribution but do not show that CDK1 phosphorylation alone controls catalytic activity or centrosomal release. [PMID:15263015](https://pubmed.ncbi.nlm.nih.gov/15263015/), [PMID:30089874](https://pubmed.ncbi.nlm.nih.gov/30089874/).

The current [Human Protein Atlas CDC14A record](https://www.proteinatlas.org/ENSG00000079335/subcellular) reports supported nucleoplasmic staining with HPA023783. The uncertain ER and cytosol observations are not new annotations. Both [Reactome binding](https://reactome.org/content/detail/R-HSA-5692749) and [dephosphorylation](https://reactome.org/content/detail/R-HSA-5692754) diagrams depict a nuclear compartment, but the binding-event summary explicitly acknowledges that the reaction location has not been established. Nucleoplasm is retained through the independent staining evidence, not inferred from the diagram.

Hair-cell compartments are mouse-derived transfers, not direct human localization assays. Human genetics and mouse perturbations support hearing dependence; the hair-cell substrates remain unknown, and germline mutant kinocilia need not reproduce morpholino shortening. [PMID:29293958](https://pubmed.ncbi.nlm.nih.gov/29293958/), [PMID:27259055](https://pubmed.ncbi.nlm.nih.gov/27259055/).

The newer truncation study separates human transcript stability from mouse enzyme/targeting experiments. Mouse residues 1–345 retain activity, while truncation alters intracellular localization; purified full-length and truncated specific activities were not successfully compared. Its human RefSeq sequence is 623 residues and its mouse sequence 603 residues, whereas the normal seed displays a 594-residue canonical human product. Neither construct numbering nor functional equivalence is silently assigned across those sequences. All five source products are preserved, without inventing product-specific functions. [PMID:41308992](https://pubmed.ncbi.nlm.nih.gov/41308992/).

## Binding evidence and annotation decisions

The UXT interaction has human-library two-hybrid and reciprocal tagged-protein co-immunoprecipitation support. The original authors could not perform endogenous co-IP with their antibodies. This does not establish UXT as a CDC14A substrate. [PMID:16221885](https://pubmed.ncbi.nlm.nih.gov/16221885/).

The two HuRI partner accessions, Q8N5M1 and Q9NWQ9, were matched exactly to human-human IntAct records IM-25472-156817 and IM-25472-161486, respectively, linked to the publication's Supplementary Table 9. These are target-specific curated assay records; the raw supplement was not independently reread. Array, pooled and validated records describe related assay observations, not independent physiological replications. [PMID:32296183](https://pubmed.ncbi.nlm.nih.gov/32296183/), [IntAct CDC14A](https://www.ebi.ac.uk/intact/search?query=Q9UNH5).

The standing [project curation instruction](https://github.com/ai4curation/ai-gene-review/blob/fe9d0eec86d1f5b949960c82e206f1a330bba618/projects/CLINGEN_MENDELIAN.md#curation-instructions) says to “retain a supported, biologically correct `GO:0005515` (protein binding) annotation as `KEEP_AS_NON_CORE`” when a narrower MF is unsupported. All three binding rows meet that evidence boundary. No protein-binding term is used as a core function, and no partner activity is transferred.

There are 34 decisions: seven ACCEPT, 22 KEEP_AS_NON_CORE, two MODIFY and three UNDECIDED. The refinements are organizing center to centrosome, and cilium assembly to regulation of cilium assembly. The unresolved assertions concern exact human protein-tyrosine catalysis, physiological nucleolar activity and the positive cytokinesis role across differing human perturbations. All original references, evidence codes, qualifiers, partner identifiers and other source fields remain unchanged. PAINT nodes are treated as ancestral inferences: donor counts and target self-evidence are not used to reject them. The full PAINT reconstruction was not recovered, so no erroneous ancestral-node placement is asserted.

## Access and follow-up

Normal fetch-gene and publication caching ran in an isolated workspace. Genuine Falcon research and the explicit perplexity-lite fallback each reached the bounded timeout; neither produced a report. These notes record manual primary research and are not a fabricated provider output. Source caches were preserved exactly; selected externally accessible primary text is distinguished from abstract-only cached records in each reference review.

The original 1997 biochemical Methods, several older cell-cycle Methods, and the exact centrosome supplement entry remain uninspected. An HTTP200 anti-bot page is recorded as a failed full-text retrieval, not article access. Selected primary text for the ciliary and localization studies was accessible through the article index. The independent annotation consultation addressed substrate specificity, nucleolar activity and conflicting mitotic evidence. No coordinate, raw image or proteomic reanalysis was performed.

A focused next step is to identify endogenous hair-cell substrates while separately testing catalytic competence and targeting of the human products. Matched acute-depletion and knockout experiments could resolve the cytokinesis discrepancy. A direct human protein-phosphotyrosine assay and substrate identification would resolve the specificity boundary without inferring absence from phosphoserine preference.


## Follow-up: microtubule core scope and biochemical specificity

Microtubule cytoskeleton organization (GO:0000226) is retained as a non-core
PAINT inference and is removed from the core process list. The inspected human
microtubule-regrowth experiment used transient GFP-hCDC14A expression in U2OS
cells: high expression abolished centrosomal nucleation after nocodazole washout,
whereas low expression did not. Deregulation can disrupt an organelle without
establishing that its organization is the protein's principal physiological
function. The older RNAi/cell-division observations remain acknowledged; they are
not reclassified as solely overexpression evidence. Human RPE1 knockout results
limit an indispensable cell-cycle claim without proving absence of all regulatory
roles. [PMID:12134069](https://pubmed.ncbi.nlm.nih.gov/12134069/),
[PMID:11901424](https://pubmed.ncbi.nlm.nih.gov/11901424/),
[PMID:33328327](https://pubmed.ncbi.nlm.nih.gov/33328327/).

The proposed colocalization alternative does not establish a core organization
mechanism either. The primary COS-7 transfection Methods specify GFP-tagged WT
and mutant mouse Cdc14a constructs. This is neither endogenous human expression
nor a demonstrated microtubule-assembly step. Those Methods were inspected through
the official PMC article's indexed text; the current direct HTML response was a
challenge page and the XML request failed. The preserved publication cache remains
abstract-only. Separate endogenous human spindle localization and in-vitro INCENP
dephosphorylation support the existing location/activity-inference rows, with their
assay distinction retained. [PMID:29293958](https://pubmed.ncbi.nlm.nih.gov/29293958/),
[PMID:15263015](https://pubmed.ncbi.nlm.nih.gov/15263015/).

The drebrin/Arp2 result is an actin-mediated cilium-growth mechanism, not direct
microtubule organization. Regulation of cilium assembly (GO:1902017) remains the
single core process. GO:1902018 negative regulation of cilium assembly was
considered because loss of CDC14A activity lengthens RPE1 cilia. The parent term
is retained for the broader synthesis: zebrafish morphants have shortened kinocilia,
whereas germline mouse and zebrafish mutants can have normal kinocilium lengths.
This does not deny the negative direction in the tested human RPE1 context.
[PMID:30467237](https://pubmed.ncbi.nlm.nih.gov/30467237/),
[PMID:27259055](https://pubmed.ncbi.nlm.nih.gov/27259055/),
[PMID:29293958](https://pubmed.ncbi.nlm.nih.gov/29293958/).

Selected structural and kinetic Results of the newer truncation study sharpen
the unresolved protein-Tyr question. Its phosphatase-dead mouse 1–345 construct
binds the proline following phosphoserine in a hydrophobic pocket. Active
truncation kinetics use pNPP and the ApSPRRR phosphopeptide. This supports pSer-Pro
recognition in that construct, without testing human protein-phosphotyrosine
catalysis. Neither substrate preference nor pNPP hydrolysis resolves the older
human dual-specificity claim. No residue numbering or catalytic property is
silently transferred to the seeded 594-residue human product.
[PMID:41308992](https://pubmed.ncbi.nlm.nih.gov/41308992/),
[PMID:9367992](https://pubmed.ncbi.nlm.nih.gov/9367992/).

The nucleolar is_active_in assertion remains UNDECIDED for a biological reason:
the observed centrosomal WT protein and nucleolar export mutant do not establish
a normal nucleolar molecular role, while a state-specific role is not excluded.
Not reconstructing the PAINT tree does not prevent a biological challenge; no
unsupported node-placement error is claimed. Short verbatim anchors were added
at selected annotation decisions, without duplicating them in these notes. All
34 original source assertions, five products and 28 reference identities remain
unchanged; the only action change is the microtubule process moving to non-core.
