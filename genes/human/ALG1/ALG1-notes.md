# ALG1 (Q9BT22) review notes

Human ALG1 = chitobiosyldiphosphodolichol beta-mannosyltransferase (EC 2.4.1.142; RHEA:13865),
a.k.a. beta-1,4-mannosyltransferase / GDP-Man:GlcNAc2-PP-dolichol mannosyltransferase / MT-1.
HGNC:18294. CAZy GT33 (glycosyltransferase group 1 family, GT33 subfamily). 464 aa, chromosome 16.

## Core biology (verified)

- Catalyzes the FIRST mannose-addition step of dolichol-linked oligosaccharide (LLO / DLO) assembly:
  transfer of the first mannose from GDP-mannose onto the chitobiose core (GlcNAc2-PP-dolichol),
  forming Man1GlcNAc2-PP-dolichol, on the cytoplasmic (cytosolic) face of the ER membrane.
  [file UniProt Q9BT22 FUNCTION: "Catalyzes, on the cytoplasmic face of the endoplasmic reticulum,
  the addition of the first mannose residues to the dolichol-linked oligosaccharide chain, to produce
  Man1GlcNAc(2)-PP-dolichol core oligosaccharide."]
  [PMID:26931382 "encodes an ER localized β1,4 mannosyltransferase that catalyzes the transfer of the
  first of nine Man moieties onto the growing DLO"]
- Man1GlcNAc2-PP-dolichol is the substrate for ALG2, the next enzyme (UniProt FUNCTION).
- CATALYTIC ACTIVITY (UniProt / RHEA:13865): an N,N'-diacetylchitobiosyl-diphospho-dolichol +
  GDP-alpha-D-mannose = beta-D-Man-(1->4)-beta-D-GlcNAc-(1->4)-alpha-D-GlcNAc-diphospho-dolichol +
  GDP + H+. EC 2.4.1.142. Direct enzymatic evidence from PMID:14973778 (patient fibroblast extracts,
  [14C]GlcNAc2-PP-dolichol + GDP-mannose assay).
- Subcellular location: ER membrane, single-pass membrane protein. Topology (PMID:35136180): short
  lumenal N-terminus (1-2), one TM helix (3-23), then a large cytoplasmic catalytic region — consistent
  with acting on the cytoplasmic face. GOA also carries "cytoplasmic side of ER membrane" (GO:0098554, ISS).

## Disease

- Deficiency causes ALG1-CDG (congenital disorder of glycosylation type Ik / CDG-Ik; MIM:608540),
  a severe autosomal-recessive multisystem disorder: developmental delay, hypotonia, epilepsy,
  microcephaly, dysmorphism, coagulation/hematologic and immune involvement; high early mortality.
  [PMID:14973778, PMID:26931382]
- Diagnostic biomarker: xeno-tetrasaccharide NeuAc-Gal-GlcNAc2 (PMID:26931382).
- Originally described by 3 groups in 2004 (Schwarz PMID:14973778; Kranz PMID:14973782;
  Grubenmann PMID:14709599). PMID:26931382 tripled the case count (39 new patients, 26 new mutations).

## Annotation review reasoning

- MF GO:0004578 (chitobiosyldiphosphodolichol beta-mannosyltransferase activity) is the exact,
  correct MF — supported by IDA (PMID:14973778), TAS (Reactome), IEA (RHEA/EC). ACCEPT all.
- GO:0000030 (mannosyltransferase activity) IBA + IEA is the correct-branch parent; less specific
  than GO:0004578. MODIFY -> GO:0004578 (too general).
- GO:0016757 (glycosyltransferase activity) IEA (InterPro Glyco_trans_1) is a very general
  grandparent — over-annotation given the specific term is available. MARK_AS_OVER_ANNOTATED.
- BP: GO:0006488 (dolichol-linked oligosaccharide biosynthetic process) IDA + TAS — core, ACCEPT.
  GO:0006487 (protein N-linked glycosylation) IDA x2 (acts_upstream_of_positive_effect) — core,
  ACCEPT. GO:0009101 (glycoprotein biosynthetic process) IBA — correct but more general parent of
  N-linked glycosylation; KEEP (accept as broader).
- CC: GO:0005789 (ER membrane) TAS/IEA/ISS — core location, ACCEPT. GO:0005783 (ER) IBA — broader
  correct location, ACCEPT. GO:0098554 (cytoplasmic side of ER membrane) ISS — correct catalytic
  face, ACCEPT. GO:0016020 (membrane) HDA (PMID:19946888 NK-cell membrane proteome) — correct but
  uninformatively general; MARK_AS_OVER_ANNOTATED.

## Refs used
- PMID:14973778 (Schwarz 2004) — CDG-Ik discovery, enzymatic + complementation; abstract-only cache.
- PMID:26931382 (Ng 2016) — 39-patient clinical/molecular series; full text cached.
- PMID:19946888 (Ghosh 2010) — NK-cell membrane proteome (basis of the HDA membrane annotation).
- Reactome R-HSA-446218 / R-HSA-446193 / R-HSA-4549382 — pathway TAS annotations.
- file:human/ALG1/ALG1-uniprot.txt — UniProt Q9BT22 FUNCTION / SUBCELLULAR LOCATION / CATALYTIC ACTIVITY.

## Provenance notes
- No falcon deep research (provider out of credits, HTTP 402). Grounded in UniProt, GOA, cached PMIDs
  and Reactome only.

## 2026-09-27: full ClinGen campaign re-review

This dated section supersedes the action guidance and unbounded source claims above while preserving the earlier record. The full audit covers all 19 seeded assertions, both alternative products, every existing reference, and the integrated catalytic core. The verified approved human symbol is ALG1 (HGNC:18294; UniProt Q9BT22); the archived HGNC subset and live NCBI Gene 56052 agree. Historical aliases HMT-1, HMAT1, CDG1K and Mat-1 have no separate gene directory or open PR in the coordinator's separate searches. The five canonical files matched current main `ba3ff58d7d2de76dbe3c24b16e05e12369f463fc` before authoring. No machine source objects, original reference identities, GOA or UniProt bytes were changed.

### Research access and source boundaries

A genuine Falcon research attempt with a 1,200-second timeout and `--fallback perplexity-lite` ran concurrently with `just fetch-gene-pmids human ALG1`. Both research paths failed before contacting a provider because the required package could not be retrieved from PyPI (DNS resolution failure). Neither produced a research report. The publication step reused all three seeded PMID caches successfully. This is a new attempt, distinct from the earlier HTTP 402 note. Logs are `/tmp/ALG1-provider.log` and `/tmp/ALG1-fetch.log`; their hashes are recorded in the final local audit receipt.

The local source census includes the historical notes, not only YAML references. PMID:14709599 and PMID:14973782 are pre-existing notes-only discovery citations whose caches were absent; a normal fetch was attempted in `/tmp/ALG1-extra-fetch.log`. Primary Reactome R-HSA-446218 and the immutable UniProt bibliography identify both discovery sources consistently. This review does not manufacture their full text or use unread details as evidence against a curated annotation.

The canonical cache for PMID:14973778 is abstract-only. Its identifier, DOI 10.1086/382492 and primary figure captions were independently read at <https://pubmed.ncbi.nlm.nih.gov/14973778/>. Indexed original PMC1182261 Results additionally describe the paired substrates in Figure 4: deficient elongation from GlcNAc2-PP-dolichol versus retained downstream elongation when the first mannose is already present. Figures 5 and 6 describe human fibroblast retroviral rescue and human-transgene complementation in yeast. Direct PMC opens later returned a browser challenge, so this is an abstract, figure-caption and indexed-Results read, not a claim to have inspected every Methods paragraph. The reviewed enzyme assignment rests on the accessible positive assay and rescue evidence, with curator deference. It is not presented as a purified human enzyme kinetic measurement.

PMID:26931382 has an extracted full-text cache, which was read for Methods, Results and Discussion. The experiment expresses human reference cDNA and individual variants in a temperature-sensitive yeast alg1 strain. Wild-type human ALG1 restores growth and carboxypeptidase Y glycosylation. The authors explicitly caution that residual mutant growth could include remaining endogenous yeast activity, and that their glycosylation assay does not rank patient clinical severity. Accordingly, neither partial activity percentages nor universal genotype-to-severity predictions are inferred. The clinical phenotype is variable; severe early mortality in the studied cohort does not describe every ALG1-CDG presentation. The paper's discussion places ALG1/ALG2/ALG11 complex evidence in yeast, so no human complex membership is newly asserted.

PMID:19946888 remains abstract-only. The primary PubMed abstract and identifier were independently verified through indexed search. It describes enriched YTS-cell membrane fractions and mass spectrometry; the ALG1-specific target/peptide row was not recovered. The HDA membrane assertion is ACCEPT with explicit curator deference and independent human ER evidence. Broadness alone does not make the compartment false or excessive, and the survey-wide percentage of predicted membrane proteins is not an ALG1-specific result. This source establishes neither plasma-membrane residence nor a new molecular function.

PMID:35136180 is fully cached and was read for the relevant Results, Figure 2 and Methods. Although its title foregrounds human ALG2, Figure 2 directly tests an N-terminal FLAG-Suc2A-human ALG1 fusion in HEK293 cells. PNGase-sensitive reporter glycosylation supports access of that N-terminal reporter to the ER lumen. The study's ALG2 C-terminal reporters, protease-protection, fractionation and catalytic assays must not be reassigned to ALG1. The exact native ALG1 transmembrane residue boundaries in the earlier notes are curated feature assignments, not positions mapped by this reporter assay. The cytoplasmic ALG1 catalytic face is independently supported by the established reaction context and curated localization inference. A second reviewer independently read and agreed with these construct-specific limits.

### New primary research checked without expanding the core

PMID:40328714 (2025; DOI 10.13345/j.cjb.240834) was independently identified through its primary PubMed record at <https://pubmed.ncbi.nlm.nih.gov/40328714/>. Its English abstract reports recombinant full-length human ALG1 and a construct comprising residues 23–464 expressed in E. coli, with LC-MS activity assays using DPGn2. Full-length activity declined after purification and was partly restored by adding membrane components; the truncated construct lacked detectable glycosylation activity under the tested conditions. These are positive biochemical findings supporting membrane-dependent catalytic function, not a map of native human ER orientation or proof that all possible soluble constructs are inactive. The official Chinese article's indexed introduction/conclusion were visible, but its complete Methods/Results were not reliably retrieved. A normal cache fetch was attempted; no synthetic cache or provider file was written.

PMID:40980150 (2025; DOI 10.3892/ol.2025.15263) was checked against primary PubMed and the publisher's indexed full Methods/Results/Discussion at <https://www.spandidos-publications.com/10.3892/ol.2025.15263>. The reported human carcinoma-cell perturbations affect proliferation, migration, apoptosis and EMT markers; co-immunoprecipitation and colocalization support an association with THBS1. These experiments do not identify which ALG1-catalyzed or scaffold step performs EMT regulation, or isolate a mechanism from altered glycosylation and cell health. Docking is not a direct affinity measurement. No new EMT, proliferation, apoptosis or generic protein-binding assertion is proposed. This is a bounded research assessment, not a rejection of the measured phenotypes. Its normal fetch shares `/tmp/ALG1-recent-fetch.log` with the preceding source.

These two recent sources are research notes rather than necessary supporting quotations for the existing GO decisions. Their typed citations remain in the notes-inclusive cache gate. All four missing citation candidates are separate from the already frozen source6 recovery design.

### Ontology, inference and complete action audit

Live AmiGO GO:0004578 was read on 2026-09-27: its formal reaction matches GDP-mannose plus GlcNAc2-PP-dolichol forming the beta-1,4-linked first mannose product (RHEA:13865). Its displayed ancestry includes GO:0000030 mannosyltransferase activity and GO:0016757 glycosyltransferase activity. The broad IBA/InterPro molecular-function assignments therefore receive MODIFY to the measured subtype. This corrects the earlier use of OVER for a true but overly general molecular function; no substrate specificity is inferred merely from the domain label.

The three IBA rows trace PTN000315506. Only that ancestral node is listed in their source_entities, and its exact original tree/MSA placement remains UNRESOLVED rather than invented. Human target evidence supports the retained judgments. Q9BT22 appearing in the descendant evidence is valid grounding, not circularity. The proposed catalytic refinement is for this human target, not an assertion about every member of the ancestral clade. InterPro IPR026051 and IPR001296, RHEA:13865, EC:2.4.1.142 and the SL-0097 mapping were checked against the human source record, with separate source-specific comments.

Both ISS location rows trace P16661, verified as S. cerevisiae ALG1 through primary UniProt/SGD records. Human rescue of yeast deficiency and the compatible human reporter/reaction evidence support transfer; no human-specific localization divergence was established. The exact historical donor localization assay was not independently recovered. The cached model `gocams/65c57c3400000687/65c57c3400000687-src.yaml` explicitly models Q9BT22 enabling GO:0004578, part of GO:0006488, occurring at GO:0098554. Its cytoplasmic-face edge uses the same yeast source inference, not a new experiment. The live GO:0098554 definition includes proteins embedded in or associated with the cytoplasmic ER leaflet. The integrated core uses this precise location without also listing its ER-membrane parent.

The normal Reactome reaction R-HSA-446218 supports first mannose transfer; R-HSA-4549382 instead describes defective variants. The latter's gene-level activity is accepted using its explicit normal-function contrast plus independent human enzymology, without asserting that inactive mutants perform the blocked reaction. No individual mutant trafficking claim is inferred from its disease summary. R-HSA-446193 correctly covers precursor biosynthesis but has a literal sugar-list error: it lists the three terminal residues as GlcNAcs rather than glucoses. The immutable cache is preserved; the reference assessment identifies the error and uses independent correct reaction context. This does not invalidate ALG1 pathway participation.

All 19 rows are adjudicated: 16 ACCEPT and 3 MODIFY. The membrane HDA row changes from OVER to ACCEPT; GO:0016757 changes from OVER to MODIFY. All broad source-level ER/membrane and glycoprotein-process assertions are retained. The exact biochemical reaction is catalytic work in precursor synthesis, so these process judgments are not based on necessity evidence alone. The N-linked glycosylation rows retain their machine-sourced qualifiers without interpreting or changing them.

No NEW assertion is added. The established catalytic step, its processes and its location are already represented in seeded GO and the cached GO-CAM; duplicating an ancestor or descendant would add no coverage. The unresolved human assembly and genotype-severity issues remain questions and proposed experiments. No speculative human complex or additional tumor-process core is introduced.

### Final verification and independent review

The coordinator independently read all 19 annotation decisions, all 13 reference assessments, the core, questions and recent-source notes. The coordinator also checked the live catalytic term and the primary 2025 human ALG1 abstract and requested no biological changes. The separate topology consultation agreed on the N-terminal reporter boundary.

`just validate human ALG1` passed with no reported warnings; `just render human ALG1` succeeded. All 41 supporting quotations were independently checked as exact whitespace-normalized substrings of their cited canonical files. All 19 seeded source objects, both alternative products, the original 12 reference ID/title pairs and immutable UniProt/GOA bytes were preserved. The four YAML PMID references have canonical caches and cache-consistent full-text flags. History is scaffolded with actor `codex`, tool `codex`, model `gpt-6` and checked separately.

Both additional normal retrieval processes terminated with exit code 1: the historical-source request cached 0/2, and the recent-source request cached 0/2. The notes-inclusive census therefore still has exactly four absent records: PMID:14709599, PMID:14973782, PMID:40328714 and PMID:40980150. The targeted validator did not report these historical/research-notes gaps; the independent notes-inclusive census did. Status remains DRAFT and publication readiness is contingent on their recovery. No new canonical cache or provider artifact was created, and no Git or remote mutation was performed by this reviewer.


## 2026-09-27 — source7 cache closure

The four previously missing, notes-cited publications are now present as exact
normal-fetch outputs from [recovery run36299519155](https://github.com/ai4curation/ai-gene-review/actions/runs/36299519155),
source commit `583c2ac3b65ce1f7f9808c7b10c53e25f322129a`, artifact10927941174
(235,928 bytes; SHA256 `a07af3765c6f8fa1aea780c1a6a4a6f71a561a75d1a29b6c9d334018618fa4b3`).
The verified import preserved the original record bytes. The earlier failed local
retrievals remain historical facts; their missing-cache gate is now closed.

- [PMID:14709599] is abstract-only locally.
  The patient lipid-linked precursor profile and human-allele complementation in
  yeast support the original discovery context. This is not a purified human
  enzyme assay or native human topology experiment.
- [PMID:14973782] is also abstract-only
  locally. It reports affected human patients, reduced enzyme activity, and
  human wild-type versus patient-allele rescue in yeast. Its severe infantile
  presentation is source-specific, consistent with the broader phenotypic
  variability already described above. Both discovery-paper identities and
  abstracts were checked against the official PubMed records.
- [PMID:40328714] remains abstract-only
  locally. The recovered English abstract and independently indexed primary
  record confirm the previously described human constructs expressed in E. coli,
  substrate-dependent LC-MS assay and partial membrane-component restoration.
  The [original publisher page](https://cjb.ijournals.cn/html/cjbcn/2025/4/24240834.htm)
  additionally exposes indexed Methods section1.2.7: DPGn2 acceptor and GDP-Man
  donor are incubated with recombinant protein before LC-MS product analysis.
  This further supports the construct-specific assay scope; it does not turn the
  local cache into a full-text record or establish native ER topology.
- [PMID:40980150](https://www.spandidos-publications.com/10.3892/ol.2025.15263)
  now has an extracted full-text cache. The recovered Methods, Results and
  Discussion were read, including the human primary carcinoma-cell cultures,
  ALG1 knockdown/overexpression, antibody-based co-immunoprecipitation, and
  migration, viability, apoptosis and EMT-marker assays. These results agree
  with the bounded research assessment above. Co-immunoprecipitation from cell
  lysate establishes association but does not isolate a purified binary binding
  mechanism; docking is computational. The discussion explicitly identifies
  downstream signaling mechanisms as future work. No new tumor-process or
  binding annotation is justified merely by closing this source-access gap.

The recursive authored-file citation census contains eight PMIDs and three
Reactome records, all cached. The three explicit DOI links and two PMC identifiers
resolve to publications already in that census. No provider report or raw provider
attachment exists for this gene, and unasserted UniProt bibliography is not added
as a new citation requirement. All 19 annotation/source objects, their decisions,
the integrated core, both alternative products, all 13 reference assessments and
all supporting quotations are unchanged. Status becomes COMPLETE after source
closure and targeted validation; no new biological assertion is introduced.


## 2026-09-27 — recovered enzymology and propagation evidence

This follow-up addresses review 5330000832 at exact PR #3280 head `189f9f47bba8c89e22d83df4987a97217b2d43c4`. All 19 original annotation source objects, actions, two alternative products and the integrated core remain unchanged. The earlier undated MARK_AS_OVER_ANNOTATED guidance for GO:0016757 and GO:0016020 is superseded by the dated full review and this entry: the molecular function is refined to the measured enzyme activity, while the established membrane location remains accepted as core.

Three recovered sources now have explicit reference assessments and support the corresponding annotation claims. [PMID:14709599] provides the independent short-LLO discovery and yeast complementation evidence; [PMID:14973782] provides human-allele rescue in PRY56 yeast; [PMID:40328714] measures recombinant human protein expressed in E. coli and membrane-dependent activity. Their local records are abstract-only. The first two primary PubMed identities were independently rechecked; the third indexed PubMed identity and [official publisher record](https://cjb.ijournals.cn/cjbcn/article/abstract/24240834) match DOI 10.13345/j.cjb.240834. Full article Methods are not claimed. The proposed membrane-reconstitution experiment now explicitly extends the existing study. The already recorded carcinoma study remains contextual and does not generate a new annotation.

The GDP-mannose-dependent sugar transfer and ER membrane location are biological work and location of ALG1's core function. A correct broad process/location does not become non-core because the compact core block uses a narrower term; the corpus frequency of an action is not biological evidence. The membrane proteomics reference is now UNVERIFIED for its individual ALG1 identification, while its bibliographic identity and abstract are verified. The independent human ER reporter supplies positive location evidence; no individual HDA assay is claimed recovered.

The original WITH/FROM sources are explicitly inventoried in all three IBA rows. [NCBI Gene 852407](https://www.ncbi.nlm.nih.gov/gene/852407) identifies SGD:S000000314 as yeast ALG1/YBR110W with the expected ER, enzyme and LLO functions, consistent with the existing P16661 ISS assessment. [Ensembl Plants AT1G16570](https://plants.ensembl.org/Arabidopsis_thaliana/Gene/Summary?g=AT1G16570) verifies the plant locus; its exact PAINT descendant assay remains unreviewed. Q388S6 primary retrieval failed, so no organism or assay identity is invented. Human Q9BT22 self-evidence is legitimate experimental grounding. The PTN assessment remains UNRESOLVED specifically for the uninspected ancestral placement; that is distinct from the positively assessed donor/target function and is not evidence of weak support or loss. The review does not promote a donor identity check into a completed tree/MSA audit.

The original human catalytic activity and both core process terms are unchanged, with no NEW assertion. The existing EC anchor is now quoted directly from the immutable human record. Four existing PubMed links use the renderer's native syntax to avoid doubled URLs. Source caches, raw gene files and prior history remain unchanged. Validation and independent delta review are recorded with this session.

The expanded WITH/FROM inventory in this follow-up supersedes the earlier PTN-only `source_entities` note. Explicit extant-source assessments are retained alongside the PTN assessment: verified source identity or function is distinguished from unresolved descendant assays and unresolved ancestral placement. Independent delta review confirmed the three recovered source scopes and retained biological judgments; the final wording correction specifies GDP-mannose-dependent transfer.
