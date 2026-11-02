# GAA (Lysosomal acid alpha-glucosidase / acid maltase) — review notes

UniProtKB:P10253 (LYAG_HUMAN), gene GAA, HGNC:4065, human (NCBITaxon:9606). 952 aa precursor.

## Core biology (from UniProt P10253 + literature)

- **Enzyme:** Lysosomal alpha-glucosidase, EC 3.2.1.20 ("acid maltase"). Glycoside hydrolase family 31 (GH31; CAZy GH31). Same family as intestinal maltase-glucoamylase (MGAM) and sucrase-isomaltase (SI).
- **Function (UniProt CC):** "Essential for the degradation of glycogen in lysosomes ... Has highest activity on alpha-1,4-linked glycosidic linkages, but can also hydrolyze alpha-1,6-linked glucans." [file:human/GAA/GAA-uniprot.txt]
- **Catalytic activity (UniProt CC):** "Hydrolysis of terminal, non-reducing (1->4)-linked alpha-D-glucose residues with release of alpha-D-glucose.; EC=3.2.1.20" [file:human/GAA/GAA-uniprot.txt]
- **Mechanism (PMID:29061980, full text):** GH31 Koshland double displacement, retaining. Catalytic nucleophile D518, acid/base D616. Within the lysosome no debranching enzyme is present, so GAA must hydrolyze both alpha-1,4 and alpha-1,6 linkages; clear preference for alpha-1,4 (32-fold higher specificity constant on maltose vs isomaltose). This is DISTINCT from cytosolic glycogenolysis (phosphorylase + debranching enzyme). [PMID:29061980]
- **Catalytic site (PMID:1856189, abstract):** Asp-518 predicted essential carboxylate; Trp-516 and Asp-518 critical for catalytic function; competitive inhibition with glycogen as natural substrate and 4-MU-alpha-D-glucopyranoside as artificial substrate. [PMID:1856189]
- **Biogenesis / targeting (PMID:29061980 full text):** "GAA is synthesized as a 110 kDa glycoprotein, which is targeted to the lysosome via the mannose-6-phosphate receptor and undergoes in the late endosomal/lysosomal compartment a series of proteolytic and N-glycan processing events to yield a mature active form composed of four tightly associated peptides." UniProt PTM: phosphorylation of mannose residues ensures transport via M6P receptor; proteolytic processing yields 76 kDa/70 kDa forms.
- **Localization:** Lysosome / lysosome lumen (UniProt SUBCELLULAR LOCATION: Lysosome, Lysosome membrane, ECO PubMed:17897319). Structure (PMID:29061980) is the mature lumenal enzyme.

## Disease
- **Pompe disease (GSD II, acid maltase deficiency):** autosomal recessive lysosomal storage disease from GAA deficiency; lysosomal glycogen accumulation, cardiac + skeletal muscle damage. IOPD (infantile, MIM:232300): cardiomyopathy + muscular hypotonia. LOPD (late-onset, MIM:621314): limb-girdle myopathy, respiratory muscle failure. Hundreds of GAA mutations. [PMID:29061980; UniProt DISEASE]
- **Therapy:** rhGAA (alglucosidase alfa / Myozyme) approved 2006 for ERT; M6P-receptor-mediated uptake into muscle. Pharmacological chaperones (DNJ, NAC) also studied. [PMID:29061980; PMID:9505277]
- **ERT uptake (PMID:9505277, abstract):** recombinant hGAA (110 kD precursor -> 76 kD mature within 24 h) corrects intracellular GAA + glycogen in deficient fibroblasts/myoblasts; endocytosed enzyme localizes to lysosomes; endocytosis inhibited by M6P; M6P-receptor-mediated. [PMID:9505277]

## Annotation review reasoning

### MF (all converge on the same catalytic activity)
- GO:0004558 alpha-1,4-glucosidase activity — CORE. Supported by EXP/IDA (PMID:18429042, 1856189, 7717400, 29061980, 9505277, 24417) + IBA + IEA(EC 3.2.1.20). ACCEPT the experimental ones; IBA ACCEPT; IEA (EC/InterPro) ACCEPT.
- GO:0090599 alpha-glucosidase activity — parent of 0004558. EXP(PMID:5264799 abstract=title only re alpha-1,4 & alpha-1,6 glucosidase absence in GSD II) + TAS(Reactome). Less specific than 0004558; KEEP_AS_NON_CORE (redundant broader parent). Not wrong.
- GO:0043896 glucan 1,6-alpha-glucosidase activity — IDA (PMID:24417). GAA does hydrolyze alpha-1,6 branches (secondary activity; PMID:29061980 confirms, 32x lower). Real but minor/secondary activity. ACCEPT as a genuine secondary activity (KEEP_AS_NON_CORE — not the core alpha-1,4 activity).
- GO:0004553 hydrolase activity, hydrolyzing O-glycosyl compounds — IEA InterPro. Correct but broad parent. KEEP_AS_NON_CORE.
- GO:0030246 carbohydrate binding — IEA InterPro (IPR011013 = Galactose mutarotase-like / Gal_mutarotase_sf_dom). GAA does bind its carbohydrate substrate; there's a documented secondary carbohydrate-binding site (trefoil domain) in PMID:29061980. However this is a generic domain-based mapping; substrate binding is subsumed under the hydrolase MF. MARK_AS_OVER_ANNOTATED (uninformative; the meaningful MF is the glucosidase activity).

### BP
- GO:0005980 glycogen catabolic process — CORE. IBA + IEA(ARBA) + TAS(Reactome R-HSA-70221) + IDA(PMID:29061980, 9505277). ACCEPT experimental/IBA; the lysosomal glycogen degradation IS the core BP.
- GO:0061723 glycophagy — autophagy-mediated delivery + lysosomal degradation of glycogen; this is precisely the pathway GAA acts in. IEA(Ensembl, from mouse P70699) + IMP(PMID:5264799). The IMP via GAA-deficiency phenotype (absence of activity in GSD II) supports involvement. ACCEPT / KEEP_AS_NON_CORE (glycophagy is the physiological process; glycogen catabolic process is the direct MF-linked BP).
- GO:0007040 lysosome organization — IBA + IMP(PMID:7717400). GAA deficiency causes lysosomal glycogen storage -> enlarged/disrupted lysosomes; the IMP is inferred from a leaky-splicing patient phenotype paper (delayed-onset GSD II). This is a secondary/downstream consequence, not GAA's molecular role. Reactome/IBA also carry it. KEEP_AS_NON_CORE (downstream/consequence of loss, not a direct organizing function).
- GO:0005975 carbohydrate metabolic process — IEA InterPro. Broad parent of glycogen catabolism. KEEP_AS_NON_CORE.
- GO:0005984 disaccharide metabolic process — IEA ARBA. GAA hydrolyzes maltose (a disaccharide) in vitro (acid maltase). Plausible but reflects in-vitro substrate scope, not physiological role. MARK_AS_OVER_ANNOTATED.
- GO:0000023 maltose metabolic process — IC (from GO:0004558), PMID:9505277. Maltose is an in-vitro substrate (4-MU-glucoside / maltose assays); no evidence GAA physiologically metabolizes dietary maltose (that's intestinal MGAM/SI). IC-inferred from the MF. MARK_AS_OVER_ANNOTATED.
- GO:0005985 sucrose metabolic process — IC (from GO:0004558), PMID:9505277. GAA is not a sucrase; sucrose metabolism is SI. Over-broad IC inference. MARK_AS_OVER_ANNOTATED (borderline REMOVE, but IC anchored on a real MF; not demonstrably an EC-mapping error, keep conservative).
- GO:0006006 glucose metabolic process — IC (from GO:0004558). GAA releases glucose from glycogen; broad parent. KEEP_AS_NON_CORE.
- GO:0002086 diaphragm contraction — IMP(PMID:16917947, LOPD mutation profile). This is a disease-consequence phenotype (respiratory/diaphragm failure in LOPD), not a GAA molecular role in muscle contraction. Highly indirect. MARK_AS_OVER_ANNOTATED / KEEP_AS_NON_CORE (physiological consequence of deficiency).

### CC
- GO:0005764 lysosome — CORE. IEA(UniProt) + IDA(PMID:9505277). ACCEPT.
- GO:0043202 lysosomal lumen — CORE (mature soluble lumenal enzyme). TAS(Reactome x2). ACCEPT.
- GO:0005765 lysosomal membrane — IEA(SubCell) + HDA(PMID:17897319 lysosomal membrane proteome). GAA is a soluble lumenal enzyme but is membrane-associated / co-purifies with lysosomal membrane (UniProt SUBCELLULAR LOCATION lists "Lysosome membrane" ECO PubMed:17897319). KEEP_AS_NON_CORE (peripheral association; not integral membrane).
- GO:0016020 membrane — IEA(Ensembl) + HDA(PMID:19946888 NK cell membrane proteome). Generic; MARK_AS_OVER_ANNOTATED.
- GO:0005886 plasma membrane — TAS(Reactome neutrophil degranulation exocytosis, x3). GAA appears in neutrophil granule/degranulation Reactome pathways (granule membrane proteins exocytosed to PM). Reflects proteomic detection in neutrophil granules, not the primary lysosomal function. KEEP_AS_NON_CORE / MARK_AS_OVER_ANNOTATED.
- GO:0035577 azurophil granule membrane; GO:0070821 tertiary granule membrane; GO:0101003 ficolin-1-rich granule membrane — TAS(Reactome neutrophil degranulation). Neutrophil granules are lysosome-related organelles; GAA detected there by proteomics. KEEP_AS_NON_CORE (secretory-lysosome/granule localization, not core).
- GO:0120282 autolysosome lumen — IEA(Ensembl, from mouse). Autolysosome = fusion of autophagosome + lysosome; where autophagy-delivered glycogen is degraded. Consistent with glycophagy role. KEEP_AS_NON_CORE.
- GO:0070062 extracellular exosome — HDA(PMID:23533145 prostatic-secretion exosomes; PMID:19056867 urinary exosomes). Generic high-throughput exosome proteomics detection. MARK_AS_OVER_ANNOTATED.

## Core functions summary
1. MF GO:0004558 alpha-1,4-glucosidase activity; directly involved in BP GO:0005980 glycogen catabolic process; located_in GO:0043202 lysosomal lumen (and GO:0005764 lysosome). This is the well-established core: lysosomal degradation of glycogen to glucose at acidic pH.

## 2026-10-09 completion pass (alignment with dismech Pompe entries)

- Re-checked all 45 GOA rows against the review; actions and core function (GO:0004558 alpha-1,4-glucosidase activity, directly involved in GO:0005980 glycogen catabolic process, lysosomal lumen/lysosome) stand. Status set to COMPLETE.
- dismech Pompe_Disease, Infantile-Onset_Pompe_Disease and Late-Onset_Pompe_Disease now all bind GO:0004558 (DECREASED) on their molecular GAA node, consistent with this core function and with modules/lysosomal_glycogen_degradation.yaml.


## Manual reassessment and native reconciliation — 2026-11-01

All 45 current GOA contexts have individual source-based judgments: 18 ACCEPT, 17 KEEP_AS_NON_CORE, five MODIFY, four UNDECIDED and one MARK_AS_OVER_ANNOTATED. Two catalytic cores retain alpha-1,4 hydrolysis and complementary alpha-1,6 branch cleavage in lysosomal glycogen degradation. The five correct parent-term contexts use already-asserted descendants verified through official typed is_a paths; no NEW annotation is added. The four unresolved source contexts remain explicit, and sucrose metabolism is over-annotated without inventing a negative assay. The source guide records all 25 manual reference assessments and their access limits.

The October 10 manual exosome decisions are preserved in full. Positive original GAA peptide observations in the 23533145 and 19056867 preparations support their explicit non-core reassessment; a cognate EV-surface receptor is not a prerequisite for observed fraction membership. Purity, topology and an EV function remain unresolved. The separate YTS membrane source stays UNDECIDED. All six Reactome membrane contexts have literal human GAA target membership, without an exocytosis catalyst or topology assertion. The failed mutant reaction is distinguished from normal wild-type catalysis.

Genuine native fetch used --force --no-seed and left the inherited 45-row review untouched. Its actual 45-context export, all 16 columns, literal donor order and 952-residue sequence match the retained official inputs. Raw41/native38 carries exactly one urine part_of atom; the parser omits this field, so the original atom is restored as BFO:0000050/UBERON:0001088. This is lossless metadata restoration, not a new scientific assertion. Processing features and historical proteomic accessions are not turned into natural isoforms.

The source union is 78: 28 existing immutable objects and 50 missing-only native acquisitions (48 publications and two Reactome records). The original review, old journal and three histories remain fully archived. All 55 original quotation associations remain intact: two existing exact snippets support the current cores, and 53 stay historical-only, including the one whitespace-only old quote. No new quotation, provider output or source rewrite was introduced. Native acquisition outputs were read; failed full-text fallback attempts do not confer full-text access.

The accepted science is transferred. Native EDIT history, target validation, strict GOA conservation, status, scoped whitespace and private rendering passed.

## Executed target checks — 2026-11-01

The native EDIT session is `2026-11-01T154634Z-codex-730a35`. Default validation passed with three advisories, all concerning intentionally different source-specific judgments for the same term: lysosome organization (phylogenetic non-core evidence versus the unresolved human IMP source), membrane (specificity refinement of the electronic parent versus the unresolved YTS assay), and glycophagy (supported ortholog-derived context versus the inaccessible classic human experiment). These differences do not rest on evidence-code ranking and do not claim the unresolved experiments are false. Strict GOA conservation matches all 45 contexts; the restored urine atom remains literal. Status is DRAFT. History, scoped whitespace, source conservation and private HTML rendering passed. All prior journal/history/provider artifacts and the owned family review remain preserved. No broad test suite or provider was run.


## 2026-11-01: scientific review follow-up

The initial draft preserved the old COMPLETE sign-off and all 55 inherited quote associations, while native status computation returned DRAFT with three mixed-action advisories. This was an actual computed outcome, not a manual erasure of prior curation. The original automated reviewer could not execute just/uv; the subsequently completed ordinary CI independently validated GAA with exactly those three warnings. Its full test-suite step was skipped by path routing.

The follow-up judges shared biological claims consistently: both lysosome-organization and glycophagy rows are non-core, while both general membrane rows propose the established lysosomal-membrane descendant. The unread 7717400,5264799 and YTS19946888 source details remain explicitly unverified. The diaphragm-contraction annotation remains unresolved because the available evidence does not settle participation in force generation. No new assay is inferred.

The two extracellular-exosome annotations retain the positive original fraction-identification evidence; the complete October 10 soluble-protein/receptor rationale remains unchanged in the historical journal and archive. A receptor requirement is not inherent in a fraction-membership observation. Purity, topology and physiological EV function remain separate unresolved questions. Four selected source-table extracts with public URLs, hashes and locators are now in GAA-bioinformatics/RESULTS.md. They do not change immutable caches or turn imported database GO columns into experiments.

Carbohydrate binding remains non-core on the directly observed secondary acarbose site, spatially separate from the catalytic pocket. The broad term does not require lectin activity, while the site’s contribution to endogenous glycogen processivity remains hypothetical. Both linkage-specific catalytic cores, all 45 original contexts and the exact urine atom remain unchanged. The current follow-up contains 18 ACCEPT, 19 KEEP_AS_NON_CORE, six MODIFY, one UNDECIDED and one MARK_AS_OVER_ANNOTATED; no NEW. Application, native EDIT and scoped checks passed; the computed current status is COMPLETE with zero advisories.

Independent PMID:27805059 evidence now strengthens the EV decision: three tetraspanin-specific immunocaptures, reported vesicle morphology and detergent-free on-bead digestion identified GAA/P10253 with 23–39% coverage. The source uses extraexosomal for the outer vesicle surface, not a nonvesicular fraction. Its native full-text cache was acquired once after bounded qualification; all 78 prior sources remain exact. The new observation is kept within its preparation, control and unresolved physiological-function limits.

## Follow-up executed checks — 2026-11-01

Native EDIT `2026-11-01T162336Z-codex-6dfcdf` records this amendment. Target default validation passed with zero advisories; strict GOA matches all 45 contexts, including the single urine atom. Harmonizing the three shared claims removed the initial mixed-action warnings. Native status computation returned COMPLETE. The status command reported a mismatch without writing the existing DRAFT field, so that exact computed scalar was recorded and the final native status audit passed. The initial diagnostic remains retained privately. All prior history and journal text remain intact.

History validation, scoped whitespace, source conservation and private rendering passed. The 79 normal sources comprise all 78 prior immutable source objects plus the single qualified missing publication. Four selected data-row quotations now support the portable evidence, alongside the two unchanged core snippets; all 55 historical associations remain archived. No broad test suite or provider was run for this local amendment.
