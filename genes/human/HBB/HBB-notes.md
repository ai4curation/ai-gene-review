# HBB research notes

## Identity and research status

Human HBB is HGNC:4827, UniProt P68871, NCBI Gene 3043. The native fetch
produced 93 annotation contexts, including seven IBA rows and two
`contributes_to` qualifiers. Their machine-sourced fields are retained. This
research checkpoint precedes completion of the annotation review; it is not a
merged delivery or a project-tracker increment.

The retained ClinGen project catalog lists six Definitive HBB associations:
recessive and dominant beta-thalassemia, familial erythrocytosis 6, hemoglobin M
disease, sickling disease and unstable hemoglobin disease. These are the
catalog's existing assertion snapshots, not a fresh reclassification of its
MONDO labels or evidence. Disease consequences do not automatically define
normal HBB molecular functions.

## Respiratory function and assembly

The main function is oxygen carriage in adult HbA, alpha2-beta2. The beta chain
is not the beta-like chain in HbA2 (delta) or HbF (gamma). Disease-associated
beta4/HbH and zeta2-beta2/Portland-2 contexts must be distinguished from normal
adult HbA. PMID:11159543 characterizes human embryonic hemoglobins and
Portland-2; PMID:24100324 examines a zeta2-betaS2 structural context.

Human oxyhemoglobin directly resolves an "oxygen ligand of both the alpha and
beta-subunits" [PMID:16765986]. PMID:8114096 states that adult hemoglobin
"assembles via a stable alpha 1 beta 1 dimer intermediate". Its experimental
structure is isolated human beta4 carbonmonoxy hemoglobin; this is not a direct
measurement of normal alpha2-beta2 cooperativity or CO2 carriage. Carbon
monoxide is not carbon dioxide. The retained Reactome N-terminal carbamation
and protonation events supply the separate CO2/proton context.

PMID:1512262 identifies the "critical alpha 1 beta 2 interface", supporting a
specific hemoglobin-alpha-binding refinement. Native GO:0031721 is already
present in HBB's IBA contexts. HBZ/zeta interactions are a different specific
assembly context: zeta is not the HBA1/HBA2 alpha product.

Several original sources study engineered or mutant hemoglobins:
PMID:1301199 (Hb Brescia beta114 Leu-to-Pro), PMID:1540659 (Hb La Roche),
PMID:10930828 (engineered alpha-chain fusion), PMID:9830011 (beta6-mutant fiber
packing), and PMID:9894000 (N-terminally engineered globin reassembly).
Their altered stability, affinity or polymerization must not be assigned to
wild-type HBB. PMID:11747442 includes mouse-beta/human-embryonic chimeras;
independent human HbA evidence supports established normal functions.
PMIDs:10588683 and 28066926 are bibliographic-only locally; no full-paper
inspection is claimed for them.

## Phylogenetic inference and interaction scope

The retained PANTHER data identify PTHR11442:SF42, HEMOGLOBIN SUBUNIT BETA.
Six native HBB IBA contexts use PTN000154218. Hemoglobin-alpha binding uses
PTN000154350; the separate PTN000154377 assertion in this family is not a
replacement for that native node. Positive IBD assertions in the retained
family slice support these placements. Target P68871 among descendant
experimental sources is legitimate, and donor count is not an evidence-quality
proxy. No unsupported finer phylogeny or target-specific loss is asserted.

Read-only IntAct checks confirmed the HBZ contexts for PMID:25502805
(EBI-22086955 / IM-26175-3) and PMID:31515488 (EBI-22144391 /
IM-27438-3672); GRID1 contexts for PMID:28514442 (EBI-21878389 /
IM-25778-199) and PMID:33961781 (EBI-54780658 / IM-29278-14557); and all four
seeded PMID:32296183 partners (HBZ, HBQ1, P69905 and HBM). Supported screening
associations remain bounded interactions under the project's user-directed
non-core policy. They do not establish neuronal HBB function or physiological
respiratory complexes with every globin partner. UniProt's interaction summary
and IntAct are the same curation lineage, not independent replication.
PMIDs:6683087 and 9441940 require additional source-specific evidence; a paper
foregrounding another organism or experimental system is not proof of a
curator's gene-attribution error.

## Beta-chain NO transfer and competing physiological models

The original PMID:8292032 is a heme-NO spectroscopic study, so it alone does
not demonstrate directed transport. HBB has separate beta-chain-specific
transfer evidence. PMID:9843411 reports: "The specific reaction of NO with
Cys93beta is confirmed in this structure". PMID:8637569 states that "the NO
group is released during arterial-venous transit". PMID:11214321 describes
human erythrocyte Hb-to-AE1 transfer, "which subserves NO group transfer to the
membrane", with deoxygenation-associated release of membrane vasodilatory
activity. The publisher's figure identifies beta Cys93; conventional mature
Cys93 corresponds to UniProt precursor residue 94.

These findings support a possible NO-group/bioactivity-transfer role. They do
not establish free-NO diffusion or an obligatory universal mechanism of
hypoxic vasodilation. Positive mouse physiology in PMID:25810253 is disputed
by the models in PMID:18516054 and PMID:30905171 (Circulation, 2019), which
find beta-Cys93 nonessential for the tested export/vasodilation outcomes.
The two negative studies have cached full text. The positive SNO studies are
abstract-only in the native cache, supplemented by bounded primary-publisher
inspection. Differences between models should be recorded as conflict rather
than mechanically declaring one paper superseded.

PMID:39633569 studies human arterial hemoglobin/eNOS complexes and restriction
of NO signaling, a mechanism distinct from erythrocyte NO export. Purified
alpha-globin nitrite reduction is not automatically an isolated-beta-chain
activity. The planned core remains gas carriage; the NO-transfer contexts
remain non-core.

## Peroxide chemistry, inflammatory context and extracellular clearance

PMID:19740759 reports that "Hb peroxidase activity is retained upon binding
with Hp". The primary full article at
https://pmc.ncbi.nlm.nih.gov/articles/PMC2781594/ examines human Hb, human
THP-1-derived macrophages, peroxide-dependent chemistry and septic plasma.
It supports complex-level chemistry, not isolated-beta catalytic attribution.
The native `contributes_to` qualifier must remain intact.

Covalent Hb-Hp aggregates "activate superoxide production and induce
intracellular oxidative stress" [PMID:19740759]. Unaggregated Hb and noncovalent
Hb-Hp did not produce the same cellular effects. This bounds the inflammatory
and peroxide-response contexts to pathological extracellular chemistry.
Peroxide consumption does not by itself show reduced cellular oxidant toxicity.
The live GO:0042744 is_a/part_of closure checked during HBA2 review on
2026-11-15 excludes GO:0098869, so peroxide breakdown need not entail
protective detoxification.

The retained Reactome records locate Hb-containing complexes during
haptoglobin/CD163 clearance, extracellular redox chemistry, heme transfer and
bacterial proteolysis. These locations are contextual cargo observations.
The bacterial EspC and Hbp proteases execute the cleavage; HBB does not thereby
become proteolysis or bacterial heme-acquisition machinery. The uptake event
R-HSA-2230938 has an extracellular starting compartment and an endosomal
luminal destination. Human P68871 entities R-HSA-6800191 and R-HSA-6801015
also support tertiary-granule and ficolin-1-rich-granule lumen cargo assignments,
without an exocytosis-machinery role.

PMID:7965120 adds purified human Hb to rat aortic smooth-muscle cells and
reports: "Hb can modify cytokine-induced production of NO in RA-SMC's by
increasing the inducible form of NOS." This is a contextual effect on cytokine
signaling, not nitric-oxide synthase activity by HBB.

## Proteomics and disease-phenotype boundaries

The authors' retained NIH urinary-exosome database
(https://esbl.nhlbi.nih.gov/Databases/UrinaryExosomes/) identifies beta globin,
HBB, two peptides, NP_000509, with reference 2 resolving to PMID:19056867.
A read-only retrieval was 468601 bytes with SHA256
`e62dbbf0a132cea7b6650ba618f4f257370a56cfbaf42b1949ed02cd28d1cb8c`.
This supports occurrence in the preparation, not a secretion mechanism.
The imported GO-process columns are not independent functional evidence.
The PMID:23533145 supplementary spreadsheet did not return a readable XLSX,
and the PMID:22516433 plasma-microvesicle protein table remained inaccessible.
Those specific identifications remain unresolved; neither soluble extracellular
Hb nor a study's general proteomics scope confirms a vesicle-specific hit.

The complete PMID:18465053 primary PDF
(https://smj.sma.org.sg/4905/4905a9.pdf) describes renal abnormalities in 166
beta-thalassemia-major patients. The cached abstract states:
"Beta-thalassaemia patients present multiple renal abnormalities which may be
due to iron overload." Clinical secondary injury is not evidence that HBB
performs renal absorption. PMID:18974585 remains abstract-only and reports
"reduced tubular reabsorption of phosphorus" in a thalassemia-minor case;
its experimental annotation should remain UNDECIDED without a verified full
source, rather than alleging a curator error.

Full PMID:23382103 (https://pmc.ncbi.nlm.nih.gov/articles/PMC3650338/) lists
HBB_HUMAN in Table I as 2.59-fold higher in MDS platelet preparations
(p=0.011719). Functional experiments concern patient platelets and
talin/integrin signaling. No HBB-specific perturbation, rescue or aggregation
effector assay was identified. Differential abundance does not establish HBB
executing platelet-to-platelet adhesion.

## Processed peptides

The native 147-residue precursor has mature beta chain 2-147
(PRO_0000052976), LVV-hemorphin-7 at 33-42 (PRO_0000296641, LVVYPWTQRF), and
spinorphin at 33-39 (PRO_0000424226, LVVYPWT). These are processing products,
not splice isoforms or activities of the intact oxygen carrier.

PMID:1575724 reports LVV-hemorphin-7 "isolated from human ventricular
cerebrospinal fluid (CSF)" after cerebrovascular bleeding. The authors also report that it "was not
detectable in control CSF". The sequence is shared among beta-, delta-, gamma-
and epsilon-globins; peptide identification alone does not uniquely identify
HBB as its source. Historical residues 32-41 omit the initiator methionine.
PMID:17676725 assays spinorphin-related peptides "with recombinant human P2X3
receptors expressed in Xenopus oocytes"; it does not establish endogenous
HBB-dependent human pain regulation. PMID:16904236 concerns dog/sheep isolates
and rat pharmacology. PMID:12470213 is a review describing bovine, monkey and
mouse evidence. No NEW peptide-maturation process is proposed: supplying a
cleaved substrate is not executing its proteolysis.

## Provenance and next step

Native fetch and publication caching are complete. The fetch-generated
versions of three existing publications are retained in Git commit
62183e72c705b3a777c6fbf8dbd397a0a6c3ae25. Two had lost richer cached text and
the third changed metadata/whitespace without new body content; canonical
versions were restored without hand-editing at checkpoint
9928ee877f3b7996ae6cd856aae77f29910dab4c. No unique source version was discarded.

Research used native sources, primary full text where accessible and bounded
read-only helper audits. The known Falcon authentication and Perplexity quota
failures were not retried without changed conditions. No provider-generated
report is claimed. Work uses one registered sparse checkout and a retained
runtime; no nested repository, per-gene environment or bulk source snapshot
was created.

The next step is to adjudicate all 93 seeded contexts, retain source-access
uncertainty, synthesize the core and processing records, and run the schema,
reference, quote, history and rendering checks before publishing the HBB PR.

## 2026-11-15 completed curation

All 93 native contexts have now been adjudicated: 33 ACCEPT, 40
KEEP_AS_NON_CORE, 11 MODIFY, 6 UNDECIDED and 3 MARK_AS_OVER_ANNOTATED.
No NEW annotation was added. Native annotation fields, including both
contributes_to qualifiers, were preserved. The review remains DRAFT because
six source-specific questions are unresolved.

The respiratory core identifies oxygen-carrier activity, oxygen and carbon
dioxide transport, cytosol and the hemoglobin complex. Structured records
separate the mature chain, LVV-hemorphin-7 and spinorphin. The nitric-oxide
findings preserve both positive and conflicting beta-Cys93 physiological
studies. Experimental peroxidase chemistry is not treated as sufficient
evidence for protective cellular oxidant detoxification.

The compact [source-evidence report](HBB-source-evidence/RESULTS.md) records
the HBB-specific urinary-exosome and platelet table rows and the two human
P68871 Reactome granule entities. Its script parses primary responses in
memory and retains selected records, URLs, retrieval times and hashes; it
does not archive entire responses or infer a biological role from imported
GO columns. A second urinary-exosome row serves as a parser control.

Schema, ontology and best-practice validation passed. Thirteen advisory
warnings are intentional: eleven supported generic-binding contexts remain
non-core under the standing user policy; the urinary/prostatic exosome and
renal-absorption pairs differ because one source in each pair can be
adjudicated and the other retains a full-text access limitation. The
reference validator checked 118 snippets and 51 titles with zero issues;
the direct quotation check verified all 210 quotations with none unchecked.
The repository helper derived 40 UniProt record-section fields. Canonical
rendering succeeded in memory. Independent scientific review found no
blocking concern with the evidence boundaries, refinements, core or forms.
