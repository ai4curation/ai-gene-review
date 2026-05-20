---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-12T15:17:01.677740'
end_time: '2026-05-12T15:33:42.177158'
duration_seconds: 1000.5
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 28
---

## Question

Concise GO annotation research for human ANKS6 / UniProt Q68DC2. Focus only on GO-relevant evidence: ANKS6/SamCystin as a ciliary inversin-compartment scaffold or molecular adaptor; interactions with NEK8, INVS, NPHP3, ANKS3, BICC1; protein kinase binding versus generic protein binding; SAM-domain-mediated complex assembly; localization to ciliary inversin compartment, cilium and cytoplasm; role in nephronophthisis/cystic kidney disease, renal tubule/nephron development; regulation of canonical Wnt/beta-catenin signaling, Hippo/YAP signaling, cAMP pathways, and ciliopathy phenotypes. Include caveats for over-broad developmental/disease terms and high-throughput interactome protein binding annotations. Include PMID/DOI citations and keep under 1500 words.

## Output

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

Concise GO annotation research for human ANKS6 / UniProt Q68DC2. Focus only on GO-relevant evidence: ANKS6/SamCystin as a ciliary inversin-compartment scaffold or molecular adaptor; interactions with NEK8, INVS, NPHP3, ANKS3, BICC1; protein kinase binding versus generic protein binding; SAM-domain-mediated complex assembly; localization to ciliary inversin compartment, cilium and cytoplasm; role in nephronophthisis/cystic kidney disease, renal tubule/nephron development; regulation of canonical Wnt/beta-catenin signaling, Hippo/YAP signaling, cAMP pathways, and ciliopathy phenotypes. Include caveats for over-broad developmental/disease terms and high-throughput interactome protein binding annotations. Include PMID/DOI citations and keep under 1500 words.

## Concise GO-annotation research report: Human **ANKS6 / SamCystin (UniProt Q68DC2; NPHP16)**

### Scope and framing (GO-relevant concepts)
ANKS6 is an ankyrin-repeat + SAM-domain protein best supported as a **ciliary inversin-compartment (INVc/InvsC) scaffold/adaptor** that (i) forms a **specific functional subcomplex with the ciliary kinase NEK8**, and (ii) participates in a **SAM-domain multivalent assembly network** with ANKS3 and BICC1 that tunes higher-order complex formation (and, indirectly, RNA/cAMP-related outputs). Mechanistically, ANKS6 sits within a hierarchical module: **INVS** is upstream/core for INVc assembly, **ANKS6–NEK8** are downstream to recruit/concentrate **NPHP3**. (bennett2020novelfibrillarstructure pages 1-4, bennett2020novelfibrillarstructure pages 11-13, hoff2013anks6isa pages 1-2)

---

### 1) Key GO concepts and definitions (current understanding)

**Inversin compartment (INVc/InvsC):** A proximal-cilium (periaxonemal) subcompartment containing **INVS, ANKS6, NEK8, and NPHP3**. Superresolution and genetic dissection support that **INVS is the structural determinant**, while **NEK8 and ANKS6 depend on INVS for localization** and together act to localize/concentrate **NPHP3**. (bennett2020novelfibrillarstructure pages 1-4, bennett2020novelfibrillarstructure pages 11-13)

**ANKS6 as kinase-binding adaptor vs generic ‘protein binding’:** Several datasets place ANKS6 in interactome-like networks, but high-confidence GO MF annotation should emphasize **specific, domain-mapped binding to a protein kinase (NEK8)** and its functional consequence (NEK8 activation/phosphorylation), rather than broad “protein binding.” (czarnecki2015anks6isthe pages 1-2, smith2019themechanisticfunctiona pages 56-59, hoff2013anks6isa pages 1-2)

**SAM-domain complex assembly:** ANKS6 SAM-domain integrity is required for selective interactions (notably with ANKS3 and/or indirectly with BICC1 via ANKS3), and cystic mutations in the SAM region disrupt these assemblies. (bakey2015thesamdomain pages 1-2, clark2020invivocharacterisationa pages 34-38, rothe2018crystalstructureof pages 10-11)

---

### 2) Most recent developments (prioritizing 2023–2024)

**ANKS6→ANKS3 remodeling licenses BICC1 assemblies (2023):** In vitro reconstitution and AlphaFold-guided complex models support that ANKS6 binds ANKS3 with higher affinity than BICC1, sequestering ANKS3’s SAM and thereby **freeing BICC1 SAM to self-polymerize**, promoting BICC1 RNP assembly. This provides updated mechanistic evidence for **SAM-domain-mediated complex assembly** and “adaptor/scaffold” roles involving ANKS6–ANKS3–BICC1. (Published 2023-09; DOI:10.1371/journal.pbio.3002302; https://doi.org/10.1371/journal.pbio.3002302) (rothe2023bicc1ribonucleoproteincomplexes pages 1-2)

**ANKS6/InvsC metrics in ciliary assays (2024 preprint):** A 2024 bioRxiv study includes experimental pipelines quantifying the **inversin-compartment size** using **ANKS6/NEK8/INVS staining** relative to total cilium length and uses co-IP/colocalization analysis. In the provided excerpt, these details are methodological (results not shown), so they currently support **that ANKS6 localization/InvsC parameters were directly measured**, but cannot be used as outcome evidence without the results sections. (Posted 2024-04; DOI:10.1101/2024.04.18.588747; https://doi.org/10.1101/2024.04.18.588747) (mahuzier2024theanks3bicc1protein pages 20-24, mahuzier2024theanks3bicc1protein pages 1-5)

**Ciliopathy model synthesis (2024 review):** A 2024 review of the Han:SPRD rat model reiterates ANKS6/SamCystin relevance to cystogenesis and summarizes pathway connections including Hippo/YAP (secondary source). Use for context, not primary GO evidence. (Published 2024-02; DOI:10.3390/biomedicines12020362; https://doi.org/10.3390/biomedicines12020362) (kofotolios2024thehansprdrat pages 7-8)

---

### 3) Core GO evidence by aspect (CC, MF, BP)

#### A. Cellular Component (CC)

**Ciliary inversin compartment / proximal cilium:** 
* High-confidence localization and dependency evidence comes from superresolution imaging plus CRISPR knockouts in human RPE1 cells, supporting that ANKS6 is an INVc component and depends on INVS for localization; ANKS6 and NEK8 are required downstream to properly localize/concentrate NPHP3. (bennett2020novelfibrillarstructure pages 1-4, bennett2020novelfibrillarstructure pages 11-13)
* Additional support that ANKS6 “localizes to the proximal cilium” and is part of the NEK8–INVS–NPHP3 nephronophthisis module comes from human genetics plus functional work. (Published 2013-06; DOI:10.1038/ng.2681; https://doi.org/10.1038/ng.2681) (hoff2013anks6isa pages 1-2)

**Primary cilium (broader):** Renal cilium localization and “Inv compartment” framing supports primary cilium annotation as a parent CC term. (nakajima2018theinvcompartment pages 1-2, bakey2015thesamdomain pages 1-2)

**Cytoplasm (qualified):** There is evidence that INV proteins can exist outside cilia and that ANKS6 participates in cytoplasmic complexes (especially with ANKS3/BICC1 in co-expression assays), but this is weaker and should be annotated cautiously compared with ciliary localization. (nakajima2018theinvcompartment pages 1-2, clark2020invivocharacterisationa pages 34-38)

**Visual evidence:** Bennett et al. provide figure-level support showing co-localization and a hierarchical dependency model for INVc components (INVS, ANKS6, NEK8, NPHP3). (bennett2020novelfibrillarstructure media 833c1b6b, bennett2020novelfibrillarstructure media af0b91fd)

#### B. Molecular Function (MF)

**Protein kinase binding (specific):** ANKS6 binds the **NEK8 kinase domain** (domain-mapped interaction), supporting “protein kinase binding” over generic “protein binding.” (Published 2015-01; DOI:10.1038/ncomms7023; https://doi.org/10.1038/ncomms7023) (czarnecki2015anks6isthe pages 1-2)

**Kinase activation/regulation (NEK8):** Cell-based kinase assays and genetics support that ANKS6 **stimulates NEK8 autophosphorylation/kinase output** and is also phosphorylated in a NEK8-dependent manner; disease-relevant alleles reducing ANKS6–NEK8 interaction impair NEK8 activation. (czarnecki2015anks6isthe pages 1-2)

**SAM-domain-mediated complex assembly / adaptor function:** SAM-domain mutations (e.g., PKD-associated) disrupt specific interactions (e.g., with ANKS3 or BICC1 depending on allele/model), and reconstitution studies show ANKS6 promotes higher-order assemblies that recruit other partners. (bakey2015thesamdomain pages 1-2, rothe2018crystalstructureof pages 10-11, clark2020invivocharacterisationa pages 34-38)

#### C. Biological Process (BP)

**Organization of the inversin compartment / intraciliary signaling center:** The INVc acts as an intraciliary center where INV and NPHP3 cooperate to promote **NEK8-dependent phosphorylation of ANKS6**, tying ANKS6 to intraciliary signal activation rather than only “ciliogenesis.” (Published 2018-05; DOI:10.1016/j.kint.2017.11.016; https://doi.org/10.1016/j.kint.2017.11.016) (nakajima2018theinvcompartment pages 1-2)

**Renal tubule/nephron development (avoid over-broad terms):** Knockdown experiments in zebrafish/Xenopus plus human genetics link ANKS6 dysfunction to renal developmental phenotypes consistent with nephronophthisis-spectrum ciliopathy. Prefer specific developmental process terms (e.g., renal tubule morphogenesis) over broad “kidney development” when curating. (hoff2013anks6isa pages 1-2)

**Ciliopathy phenotypes (context, not GO BP):** Human families with ANKS6 mutations show nephronophthisis and multisystem ciliopathy phenotypes (including laterality defects). These support biological-process annotations around cilium-dependent morphogenesis/signaling, but disease names themselves are not GO processes. (hoff2013anks6isa pages 1-2, bakey2015thesamdomain pages 1-2)

**Pathway links (Wnt/β-catenin, Hippo/YAP, cAMP):**
* **Wnt signaling:** INVc/InvsC is repeatedly stated to control canonical Wnt/Wnt-PCP, but the provided 2024 preprint excerpt is not outcome evidence; treat as indirect unless supported by direct ANKS6 perturbation assays in the cited work. (mahuzier2024theanks3bicc1protein pages 1-5)
* **Hippo/YAP:** A primary pathway study reports ANKS6 affects YAP/TAZ/TEAD activity in a developmental context; however, this is not kidney-specific and should not be generalized to all ANKS6 biology without additional corroboration. (kofotolios2024thehansprdrat pages 7-8)
* **cAMP:** Newer mechanistic work ties ANKS6 to the ANKS3–BICC1 network that controls BICC1 polymerization/RNP behavior and discusses BICC1-mediated control of Adcy6/cAMP; ANKS6 effects appear indirect via ANKS3 remodeling. (rothe2023bicc1ribonucleoproteincomplexes pages 1-2)

---

### 4) Applications and real-world implementations

**Translational use is mainly interpretive/diagnostic rather than therapeutic:** Mechanistic INVc and SAM-network insights are used to interpret **ciliopathy genetics** (e.g., ANKS6/NEK8/INVS/NPHP3 modules) and to select/validate **preclinical models** of cystic kidney disease and laterality defects. (hoff2013anks6isa pages 1-2, bakey2015thesamdomain pages 1-2, czarnecki2015anks6isthe pages 1-2)

---

### 5) Expert caveats for GO curation

1. **Prefer specific MF terms (protein kinase binding; kinase activator/regulator) where domain mapping and functional assays exist**, particularly for ANKS6–NEK8. (czarnecki2015anks6isthe pages 1-2, smith2019themechanisticfunctiona pages 56-59)
2. **De-emphasize generic “protein binding”** when evidence is largely AP-MS/network-based without orthogonal validation. (hoff2013anks6isa pages 1-2)
3. **Use appropriately granular BP terms:** “renal tubule development/morphogenesis” and “cilium-dependent signaling/compartment organization” are better supported than broad “development” terms or disease-name processes. (hoff2013anks6isa pages 1-2, nakajima2018theinvcompartment pages 1-2)
4. **Treat preprints/reviews as provisional/secondary** for direct GO assertions unless primary results are explicitly available in the excerpted evidence. (mahuzier2024theanks3bicc1protein pages 1-5, kofotolios2024thehansprdrat pages 7-8)

---

### GO-evidence mapping table

| GO aspect | Proposed GO term label | Evidence summary (1 sentence) | Key interactors | Strongest evidence type | Key citation with publication date and DOI/URL | Caveats |
|---|---|---|---|---|---|---|
| CC | ciliary inversin compartment | ANKS6 is a core component of the proximal ciliary inversin compartment, with imaging and dependency models placing it in the INVS-centered INVc network that links to NPHP3 via ANKS6-NEK8 assemblies (bennett2020novelfibrillarstructure pages 11-13, bennett2020novelfibrillarstructure pages 1-4, bennett2020novelfibrillarstructure media 833c1b6b) | INVS, NEK8, NPHP3 | superresolution imaging + CRISPR KO | Bennett et al., 2020-03, *Mol Biol Cell*, doi:10.1091/mbc.e19-09-0499, https://doi.org/10.1091/mbc.e19-09-0499 (bennett2020novelfibrillarstructure pages 11-13, bennett2020novelfibrillarstructure pages 1-4) | Strong CC evidence, but one structural model is inferential; dependency diagrams are supportive rather than standalone localization proof (bennett2020novelfibrillarstructure media 833c1b6b, bennett2020novelfibrillarstructure media a7fab014) |
| CC | primary cilium | ANKS6 localizes to the proximal cilium/renal cilium in human and model systems, including tubular and glomerular cilia, consistent with cilium annotation broader than the specific inversin compartment term (hoff2013anks6isa pages 1-2, nakajima2018theinvcompartment pages 1-2, bakey2015thesamdomain pages 1-2) | INVS, NEK8, NPHP3 | immunofluorescence localization + genetics | Hoff et al., 2013-06, *Nat Genet*, doi:10.1038/ng.2681, https://doi.org/10.1038/ng.2681 (hoff2013anks6isa pages 1-2); Nakajima et al., 2018-05, *Kidney Int*, doi:10.1016/j.kint.2017.11.016, https://doi.org/10.1016/j.kint.2017.11.016 (nakajima2018theinvcompartment pages 1-2) | “Primary cilium” is valid but less specific than “ciliary inversin compartment”; some evidence comes from non-human models or kidney epithelia rather than all human cell types (bakey2015thesamdomain pages 1-2) |
| CC | cytoplasm | ANKS6-NEK8 can exist as a cytoplasmic subcomplex before ciliary import, and ANKS6 participates with ANKS3/BICC1 in cytoplasmic bodies in overexpression assays (nakajima2018theinvcompartment pages 1-2, clark2020invivocharacterisationa pages 34-38) | NEK8, ANKS3, BICC1 | cell localization + co-expression assays | Nakajima et al., 2018-05, *Kidney Int*, doi:10.1016/j.kint.2017.11.016, https://doi.org/10.1016/j.kint.2017.11.016 (nakajima2018theinvcompartment pages 1-2) | Cytoplasmic localization is weaker than ciliary localization and partly relies on overexpression/co-expression studies; best treated as supporting rather than primary CC assignment (clark2020invivocharacterisationa pages 34-38) |
| MF | protein kinase binding | ANKS6 specifically binds the NEK8 kinase domain through its ankyrin-repeat region, distinguishing a precise kinase-binding function from generic protein-binding annotations (czarnecki2015anks6isthe pages 1-2, smith2019themechanisticfunctiona pages 56-59, leettola2015asterilealpha pages 113-116) | NEK8 | co-IP + domain mapping + kinase assay | Czarnecki et al., 2015-01, *Nat Commun*, doi:10.1038/ncomms7023, https://doi.org/10.1038/ncomms7023 (czarnecki2015anks6isthe pages 1-2) | Prefer “protein kinase binding” over broad “protein binding”; some assays used co-expression because purified full-length proteins were difficult to reconstitute (czarnecki2015anks6isthe pages 1-2) |
| MF | protein kinase activator activity | ANKS6 not only binds NEK8 but stimulates NEK8 autophosphorylation and kinase activity, with mutant alleles reducing binding and abolishing activation (czarnecki2015anks6isthe pages 1-2) | NEK8 | kinase assay + mutant phenotype | Czarnecki et al., 2015-01, *Nat Commun*, doi:10.1038/ncomms7023, https://doi.org/10.1038/ncomms7023 (czarnecki2015anks6isthe pages 1-2) | This is strong mechanistic evidence, but if a GO curator wants maximal conservatism, annotation may still be routed through kinase binding/regulation wording rather than direct activator activity depending on ontology scope |
| MF | molecular adaptor/scaffold activity | ANKS6 functions as a central adaptor linking NEK8 to INVS and NPHP3 in the nephronophthisis module and helping organize hierarchical INVc assembly (hoff2013anks6isa pages 1-2, bennett2020novelfibrillarstructure pages 1-4, smith2019themechanisticfunctiona pages 56-59) | NEK8, INVS, NPHP3 | affinity proteomics + co-IP + KO dependency | Hoff et al., 2013-06, *Nat Genet*, doi:10.1038/ng.2681, https://doi.org/10.1038/ng.2681 (hoff2013anks6isa pages 1-2); Bennett et al., 2020-03, *Mol Biol Cell*, doi:10.1091/mbc.e19-09-0499, https://doi.org/10.1091/mbc.e19-09-0499 (bennett2020novelfibrillarstructure pages 1-4) | “Scaffold/adaptor” is mechanistically accurate but may map imperfectly to current GO MF vocabulary; AP-MS/network evidence should not be overread as direct pairwise binding without corroboration (hoff2013anks6isa pages 1-2, bennett2020novelfibrillarstructure pages 1-4) |
| MF | SAM-domain-mediated protein complex assembly | ANKS6 SAM-domain integrity is required for selective assembly with ANKS3 and for higher-order BICC1/ANKS3/ANKS6 complexes, and cystic mutations disrupt these interactions (bakey2015thesamdomain pages 1-2, clark2020invivocharacterisationa pages 34-38, rothe2018crystalstructureof pages 10-11) | ANKS3, BICC1 | mutational analysis + pulldown/co-IP + structural reconstitution | Bakey et al., 2015-08, *Kidney Int*, doi:10.1038/ki.2015.122, https://doi.org/10.1038/ki.2015.122 (bakey2015thesamdomain pages 1-2); Rothé et al., 2018-02, *Structure*, doi:10.1016/j.str.2017.12.002, https://doi.org/10.1016/j.str.2017.12.002 (rothe2018crystalstructureof pages 10-11) | Direct BICC1-ANKS6 binding can be weak; some assemblies are inferred from reconstitution or overexpression, so ANKS3 may bridge parts of the network (clark2020invivocharacterisationa pages 34-38, rothe2018crystalstructureof pages 10-11) |
| BP | organization of ciliary inversin compartment | INVS is the core organizer of the inversin compartment, while ANKS6 and NEK8 are required downstream to concentrate NPHP3 and maintain proper compartment architecture (bennett2020novelfibrillarstructure pages 1-4, bennett2020novelfibrillarstructure pages 11-13, bennett2020novelfibrillarstructure media 833c1b6b) | INVS, NEK8, NPHP3 | superresolution imaging + CRISPR KO | Bennett et al., 2020-03, *Mol Biol Cell*, doi:10.1091/mbc.e19-09-0499, https://doi.org/10.1091/mbc.e19-09-0499 (bennett2020novelfibrillarstructure pages 1-4, bennett2020novelfibrillarstructure pages 11-13) | Good BP-level support for compartment organization; avoid overstating ANKS6 as the sole organizer because INVS appears upstream/core (bennett2020novelfibrillarstructure media 833c1b6b, bennett2020novelfibrillarstructure media af0b91fd) |
| BP | intraciliary signaling / cilium-dependent signaling | The Inv compartment acts as a ciliary signaling center where INV and NPHP3 promote NEK8-dependent phosphorylation of ANKS6, supporting a role for ANKS6 in intraciliary signal transduction rather than generic ciliogenesis alone (nakajima2018theinvcompartment pages 1-2, czarnecki2015anks6isthe pages 1-2) | INVS, NPHP3, NEK8 | ciliary phosphoregulation + mutant analysis | Nakajima et al., 2018-05, *Kidney Int*, doi:10.1016/j.kint.2017.11.016, https://doi.org/10.1016/j.kint.2017.11.016 (nakajima2018theinvcompartment pages 1-2) | Strong for ciliary signaling; weaker for broad “ciliogenesis” because the cited work focuses more on compartment signaling and localization than on building the cilium itself |
| BP | regulation of canonical Wnt signaling | ANKS6-containing InvsC/NPHP modules are repeatedly implicated in canonical Wnt regulation, but the evidence in the provided set is largely contextual/review-like or module-level rather than a direct ANKS6-only perturbation assay (bennett2020novelfibrillarstructure pages 1-4, mahuzier2024theanks3bicc1protein pages 1-5) | INVS, NEK8, NPHP3 | module-level mechanistic context | Mahuzier et al., 2024-04, *bioRxiv*, doi:10.1101/2024.04.18.588747, https://doi.org/10.1101/2024.04.18.588747 (mahuzier2024theanks3bicc1protein pages 1-5) | Use cautiously: support is indirect and includes a preprint; avoid overconfident direct ANKS6-to-Wnt annotation unless stronger primary perturbation data are added (bennett2020novelfibrillarstructure pages 1-4, mahuzier2024theanks3bicc1protein pages 1-5) |
| BP | regulation of Hippo signaling / positive regulation of YAP activity | Loss of ANKS6 causes YAP deficiency and liver abnormalities, indicating ANKS6 can promote YAP/TAZ/TEAD output in a developmental ciliopathy context (kofotolios2024thehansprdrat pages 7-8) | none of the five core interactors directly shown in this evidence summary | mutant phenotype + biochemical pathway study | Airik et al., 2020-09, *Hum Mol Genet*, doi:10.1093/hmg/ddaa197, https://doi.org/10.1093/hmg/ddaa197 (kofotolios2024thehansprdrat pages 7-8) | Relevant mechanistically but outside kidney/cilium-focused core evidence here; disease-organ context is liver, so do not overgeneralize to all ANKS6 biology from this single pathway study (kofotolios2024thehansprdrat pages 7-8) |
| BP | regulation of cAMP biosynthetic/signaling pathway | Recent work places ANKS6 in ANKS3-BICC1 regulatory assemblies that influence BICC1-dependent control of Adcy6/cAMP signaling, but ANKS6’s contribution appears indirect through complex remodeling (rothe2023bicc1ribonucleoproteincomplexes pages 1-2, clark2020invivocharacterisationa pages 34-38) | ANKS3, BICC1 | structural reconstitution + co-expression functional assays | Rothé et al., 2023-09, *PLOS Biol*, doi:10.1371/journal.pbio.3002302, https://doi.org/10.1371/journal.pbio.3002302 (rothe2023bicc1ribonucleoproteincomplexes pages 1-2) | Best treated as indirect/qualified evidence for ANKS6 involvement in cAMP-related regulation; direct ANKS6-specific cAMP assays are limited in the provided context (rothe2023bicc1ribonucleoproteincomplexes pages 1-2, clark2020invivocharacterisationa pages 34-38) |
| BP | renal tubule development / nephron development | Knockdown and mutant phenotypes in zebrafish, Xenopus, mouse and rat support a conserved requirement for ANKS6 in renal morphogenesis and tubular integrity, with cystic phenotypes when disrupted (hoff2013anks6isa pages 1-2, czarnecki2015anks6isthe pages 1-2, bakey2015thesamdomain pages 1-2) | NEK8, INVS, NPHP3 | knockdown + mutant phenotype | Hoff et al., 2013-06, *Nat Genet*, doi:10.1038/ng.2681, https://doi.org/10.1038/ng.2681 (hoff2013anks6isa pages 1-2); Czarnecki et al., 2015-01, *Nat Commun*, doi:10.1038/ncomms7023, https://doi.org/10.1038/ncomms7023 (czarnecki2015anks6isthe pages 1-2) | Appropriate as developmental BP with phenotype support, but avoid very broad terms like “kidney development” without specifying that much evidence comes from ciliopathy-associated renal morphogenesis/cyst prevention |
| BP | nephronophthisis-associated / cystic kidney disease-related process | Human genetics and model phenotypes consistently link ANKS6 loss or mutation to nephronophthisis-spectrum ciliopathy, renal cysts, and laterality defects, supporting disease-relevant biological-process context (hoff2013anks6isa pages 1-2, bakey2015thesamdomain pages 1-2, czarnecki2015anks6isthe pages 1-2) | NEK8, INVS, NPHP3, ANKS3, BICC1 | human genetics + mutant phenotype | Hoff et al., 2013-06, *Nat Genet*, doi:10.1038/ng.2681, https://doi.org/10.1038/ng.2681 (hoff2013anks6isa pages 1-2); Bakey et al., 2015-08, *Kidney Int*, doi:10.1038/ki.2015.122, https://doi.org/10.1038/ki.2015.122 (bakey2015thesamdomain pages 1-2) | Disease names are not GO BPs; use these data to support narrower process terms and phenotype context rather than annotating overly broad disease/process hybrids |
| MF | protein binding | ANKS6 has multiple reported partners across ciliary and cytoplasmic modules, but the most reliable GO interpretation is to prioritize experimentally resolved specific interactions rather than generic “protein binding” from network screens (hoff2013anks6isa pages 1-2, smith2019themechanisticfunctiona pages 56-59, bakey2015thesamdomain pages 1-2) | NEK8, INVS, NPHP3, ANKS3, BICC1 | AP-MS + co-IP | Hoff et al., 2013-06, *Nat Genet*, doi:10.1038/ng.2681, https://doi.org/10.1038/ng.2681 (hoff2013anks6isa pages 1-2) | Broad “protein binding” is true but low-value and easily inflated by high-throughput AP-MS; more specific terms such as kinase binding and complex assembly are preferable where evidence permits |


*Table: This table summarizes GO-relevant evidence for human ANKS6/SamCystin across cellular component, molecular function, and biological process categories. It highlights the strongest mechanistic support and flags where annotations should remain cautious because evidence is indirect, overexpression-based, high-throughput, or review/preprint derived.*

### Key primary sources (with dates and URLs)
* Hoff et al., 2013-06 (*Nature Genetics*): https://doi.org/10.1038/ng.2681 (hoff2013anks6isa pages 1-2)
* Czarnecki et al., 2015-01 (*Nature Communications*): https://doi.org/10.1038/ncomms7023 (czarnecki2015anks6isthe pages 1-2)
* Bakey et al., 2015-08 (*Kidney International*): https://doi.org/10.1038/ki.2015.122 (bakey2015thesamdomain pages 1-2)
* Nakajima et al., 2018-05 (*Kidney International*): https://doi.org/10.1016/j.kint.2017.11.016 (nakajima2018theinvcompartment pages 1-2)
* Rothé et al., 2018-02 (*Structure*): https://doi.org/10.1016/j.str.2017.12.002 (rothe2018crystalstructureof pages 10-11)
* Bennett et al., 2020-03 (*Molecular Biology of the Cell*): https://doi.org/10.1091/mbc.e19-09-0499 (bennett2020novelfibrillarstructure pages 1-4, bennett2020novelfibrillarstructure pages 11-13)
* Rothé et al., 2023-09 (*PLOS Biology*): https://doi.org/10.1371/journal.pbio.3002302 (rothe2023bicc1ribonucleoproteincomplexes pages 1-2)
* Mahuzier et al., 2024-04 (bioRxiv preprint): https://doi.org/10.1101/2024.04.18.588747 (mahuzier2024theanks3bicc1protein pages 20-24, mahuzier2024theanks3bicc1protein pages 1-5)


References

1. (bennett2020novelfibrillarstructure pages 1-4): Henrietta W. Bennett, Anna-Karin Gustavsson, Camille A. Bayas, Petar N. Petrov, Nancie Mooney, W. E. Moerner, and Peter K. Jackson. Novel fibrillar structure in the inversin compartment of primary cilia revealed by 3d single-molecule superresolution microscopy. Molecular Biology of the Cell, 31:619-639, Mar 2020. URL: https://doi.org/10.1091/mbc.e19-09-0499, doi:10.1091/mbc.e19-09-0499. This article has 60 citations and is from a domain leading peer-reviewed journal.

2. (bennett2020novelfibrillarstructure pages 11-13): Henrietta W. Bennett, Anna-Karin Gustavsson, Camille A. Bayas, Petar N. Petrov, Nancie Mooney, W. E. Moerner, and Peter K. Jackson. Novel fibrillar structure in the inversin compartment of primary cilia revealed by 3d single-molecule superresolution microscopy. Molecular Biology of the Cell, 31:619-639, Mar 2020. URL: https://doi.org/10.1091/mbc.e19-09-0499, doi:10.1091/mbc.e19-09-0499. This article has 60 citations and is from a domain leading peer-reviewed journal.

3. (hoff2013anks6isa pages 1-2): Sylvia Hoff, Jan Halbritter, Daniel Epting, Valeska Frank, Thanh-Minh T Nguyen, Jeroen van Reeuwijk, Christopher Boehlke, Christoph Schell, Takayuki Yasunaga, Martin Helmstädter, Miriam Mergen, Emilie Filhol, Karsten Boldt, Nicola Horn, Marius Ueffing, Edgar A Otto, Tobias Eisenberger, Mariet W Elting, Joanna A E van Wijk, Detlef Bockenhauer, Neil J Sebire, Søren Rittig, Mogens Vyberg, Troels Ring, Martin Pohl, Lars Pape, Thomas J Neuhaus, Neveen A Soliman Elshakhs, Sarah J Koon, Peter C Harris, Florian Grahammer, Tobias B Huber, E Wolfgang Kuehn, Albrecht Kramer-Zucker, Hanno J Bolz, Ronald Roepman, Sophie Saunier, Gerd Walz, Friedhelm Hildebrandt, Carsten Bergmann, and Soeren S Lienkamp. Anks6 is a central component of a nephronophthisis module linking nek8 to invs and nphp3. Nature genetics, 45:951-956, Jun 2013. URL: https://doi.org/10.1038/ng.2681, doi:10.1038/ng.2681. This article has 237 citations and is from a highest quality peer-reviewed journal.

4. (czarnecki2015anks6isthe pages 1-2): Peter G. Czarnecki, George C. Gabriel, Danielle K. Manning, Mikhail Sergeev, Kristi Lemke, Nikolai T. Klena, Xiaoqin Liu, Yu Chen, You Li, Jovenal T. San Agustin, Maija K. Garnaas, Richard J. Francis, Kimimasa Tobita, Wolfram Goessling, Gregory J. Pazour, Cecilia W. Lo, David R. Beier, and Jagesh V. Shah. Anks6 is the critical activator of nek8 kinase in embryonic situs determination and organ patterning. Nature communications, 6:6023-6023, Jan 2015. URL: https://doi.org/10.1038/ncomms7023, doi:10.1038/ncomms7023. This article has 66 citations and is from a highest quality peer-reviewed journal.

5. (smith2019themechanisticfunctiona pages 56-59): DC Smith. The mechanistic function of bicc1: its role in adpkd pathogenesis. Unknown journal, 2019.

6. (bakey2015thesamdomain pages 1-2): Zeineb Bakey, Marie-Thérèse Bihoreau, Rémi Piedagnel, Laure Delestré, Catherine Arnould, Alexandre d'Hotman de Villiers, Olivier Devuyst, Sigrid Hoffmann, Pierre Ronco, Dominique Gauguier, and Brigitte Lelongt. The sam domain of anks6 has different interacting partners and mutations can induce different cystic phenotypes. Kidney international, 88 2:299-310, Aug 2015. URL: https://doi.org/10.1038/ki.2015.122, doi:10.1038/ki.2015.122. This article has 31 citations and is from a highest quality peer-reviewed journal.

7. (clark2020invivocharacterisationa pages 34-38): E Clark. In vivo characterisation of anks3-a new candidate for ciliopathic disease. Unknown journal, 2020.

8. (rothe2018crystalstructureof pages 10-11): Benjamin Rothé, Catherine N. Leettola, Lucia Leal-Esteban, Duilio Cascio, Simon Fortier, Manuela Isenschmid, James U. Bowie, and Daniel B. Constam. Crystal structure of bicc1 sam polymer and mapping of interactions between the ciliopathy-associated proteins bicc1, anks3, and anks6. Structure, 26:209-224.e6, Feb 2018. URL: https://doi.org/10.1016/j.str.2017.12.002, doi:10.1016/j.str.2017.12.002. This article has 36 citations and is from a domain leading peer-reviewed journal.

9. (rothe2023bicc1ribonucleoproteincomplexes pages 1-2): Benjamin Rothé, Yayoi Ikawa, Zhidian Zhang, Takanobu A. Katoh, Eriko Kajikawa, Katsura Minegishi, Sai Xiaorei, Simon Fortier, Matteo Dal Peraro, Hiroshi Hamada, and Daniel B. Constam. Bicc1 ribonucleoprotein complexes specifying organ laterality are licensed by anks6-induced structural remodeling of associated anks3. PLOS Biology, 21:e3002302, Sep 2023. URL: https://doi.org/10.1371/journal.pbio.3002302, doi:10.1371/journal.pbio.3002302. This article has 8 citations and is from a highest quality peer-reviewed journal.

10. (mahuzier2024theanks3bicc1protein pages 20-24): Alexia Mahuzier, Gweltas Odye, Valentina Grampa, Albane Bizet, Amandine Viau, Rebecca Ryan, Manon Mehraz, Thierry Blisnick, Euan Clark, Charline Henry, Rémi Piedagnel, Flora Silbermann, Gaelle Hayot, Line De grande, Agathe Kahn, Jean-Marc Plaza, Pauline Krug, Bertrand Knebelmann, Florian Muller, Philippe Bastin, Andreas W. Sailer, Pierre Saint-Mezard, Cécile Jeanpierre, Sigrid Hoffmann, Alexandre Benmerah, Brigitte Lelongt, Marion Delous, and Sophie Saunier. The anks3/bicc1 protein complex is a master post-transcriptional regulator of nphp1 ciliopathy-gene transcripts. bioRxiv, Apr 2024. URL: https://doi.org/10.1101/2024.04.18.588747, doi:10.1101/2024.04.18.588747. This article has 4 citations.

11. (mahuzier2024theanks3bicc1protein pages 1-5): Alexia Mahuzier, Gweltas Odye, Valentina Grampa, Albane Bizet, Amandine Viau, Rebecca Ryan, Manon Mehraz, Thierry Blisnick, Euan Clark, Charline Henry, Rémi Piedagnel, Flora Silbermann, Gaelle Hayot, Line De grande, Agathe Kahn, Jean-Marc Plaza, Pauline Krug, Bertrand Knebelmann, Florian Muller, Philippe Bastin, Andreas W. Sailer, Pierre Saint-Mezard, Cécile Jeanpierre, Sigrid Hoffmann, Alexandre Benmerah, Brigitte Lelongt, Marion Delous, and Sophie Saunier. The anks3/bicc1 protein complex is a master post-transcriptional regulator of nphp1 ciliopathy-gene transcripts. bioRxiv, Apr 2024. URL: https://doi.org/10.1101/2024.04.18.588747, doi:10.1101/2024.04.18.588747. This article has 4 citations.

12. (kofotolios2024thehansprdrat pages 7-8): Ioannis Kofotolios, Michael J. Bonios, Markos Adamopoulos, Iordanis Mourouzis, Gerasimos Filippatos, John N. Boletis, Smaragdi Marinaki, and Manolis Mavroidis. The han:sprd rat: a preclinical model of polycystic kidney disease. Biomedicines, 12:362, Feb 2024. URL: https://doi.org/10.3390/biomedicines12020362, doi:10.3390/biomedicines12020362. This article has 7 citations.

13. (nakajima2018theinvcompartment pages 1-2): Yoshiro Nakajima, Hiroshi Kiyonari, Yoshiko Mukumoto, and Takahiko Yokoyama. The inv compartment of renal cilia is an intraciliary signal-activating center to phosphorylate anks6. Kidney international, 93 5:1108-1117, May 2018. URL: https://doi.org/10.1016/j.kint.2017.11.016, doi:10.1016/j.kint.2017.11.016. This article has 26 citations and is from a highest quality peer-reviewed journal.

14. (bennett2020novelfibrillarstructure media 833c1b6b): Henrietta W. Bennett, Anna-Karin Gustavsson, Camille A. Bayas, Petar N. Petrov, Nancie Mooney, W. E. Moerner, and Peter K. Jackson. Novel fibrillar structure in the inversin compartment of primary cilia revealed by 3d single-molecule superresolution microscopy. Molecular Biology of the Cell, 31:619-639, Mar 2020. URL: https://doi.org/10.1091/mbc.e19-09-0499, doi:10.1091/mbc.e19-09-0499. This article has 60 citations and is from a domain leading peer-reviewed journal.

15. (bennett2020novelfibrillarstructure media af0b91fd): Henrietta W. Bennett, Anna-Karin Gustavsson, Camille A. Bayas, Petar N. Petrov, Nancie Mooney, W. E. Moerner, and Peter K. Jackson. Novel fibrillar structure in the inversin compartment of primary cilia revealed by 3d single-molecule superresolution microscopy. Molecular Biology of the Cell, 31:619-639, Mar 2020. URL: https://doi.org/10.1091/mbc.e19-09-0499, doi:10.1091/mbc.e19-09-0499. This article has 60 citations and is from a domain leading peer-reviewed journal.

16. (bennett2020novelfibrillarstructure media a7fab014): Henrietta W. Bennett, Anna-Karin Gustavsson, Camille A. Bayas, Petar N. Petrov, Nancie Mooney, W. E. Moerner, and Peter K. Jackson. Novel fibrillar structure in the inversin compartment of primary cilia revealed by 3d single-molecule superresolution microscopy. Molecular Biology of the Cell, 31:619-639, Mar 2020. URL: https://doi.org/10.1091/mbc.e19-09-0499, doi:10.1091/mbc.e19-09-0499. This article has 60 citations and is from a domain leading peer-reviewed journal.

17. (leettola2015asterilealpha pages 113-116): C Leettola. A sterile alpha motif domain network involved in kidney development. Unknown journal, 2015.

## Citations

1. kofotolios2024thehansprdrat pages 7-8
2. nakajima2018theinvcompartment pages 1-2
3. bakey2015thesamdomain pages 1-2
4. clark2020invivocharacterisationa pages 34-38
5. bennett2020novelfibrillarstructure pages 1-4
6. rothe2018crystalstructureof pages 10-11
7. bennett2020novelfibrillarstructure pages 11-13
8. smith2019themechanisticfunctiona pages 56-59
9. leettola2015asterilealpha pages 113-116
10. https://doi.org/10.1371/journal.pbio.3002302
11. https://doi.org/10.1101/2024.04.18.588747
12. https://doi.org/10.3390/biomedicines12020362
13. https://doi.org/10.1038/ng.2681
14. https://doi.org/10.1038/ncomms7023
15. https://doi.org/10.1016/j.kint.2017.11.016
16. https://doi.org/10.1091/mbc.e19-09-0499
17. https://doi.org/10.1038/ki.2015.122
18. https://doi.org/10.1016/j.str.2017.12.002
19. https://doi.org/10.1093/hmg/ddaa197
20. https://doi.org/10.1091/mbc.e19-09-0499,
21. https://doi.org/10.1038/ng.2681,
22. https://doi.org/10.1038/ncomms7023,
23. https://doi.org/10.1038/ki.2015.122,
24. https://doi.org/10.1016/j.str.2017.12.002,
25. https://doi.org/10.1371/journal.pbio.3002302,
26. https://doi.org/10.1101/2024.04.18.588747,
27. https://doi.org/10.3390/biomedicines12020362,
28. https://doi.org/10.1016/j.kint.2017.11.016,