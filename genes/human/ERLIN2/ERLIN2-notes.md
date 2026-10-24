# ERLIN2 (SPFH2 / ER lipid raft-associated protein 2) review notes

UniProt: O94905 (ERLN2_HUMAN), 339 aa. Synonyms SPFH2, C8orf2. HGNC:1356.
Single-pass type II ER membrane protein with a lumenal SPFH/prohibitin (band 7) domain. Band 7/mec-2
family; associates with lipid-raft-like ER domains. Disease: hereditary spastic paraplegia SPG18A/SPG18B
and recessive intellectual disability/joint-contractures syndrome.

## Core biology
1. **ERLIN1/ERLIN2 complex mediating ERAD of IP3 receptors.** SPFH2 (ERLIN2) and SPFH1 (ERLIN1) form a
   ~2 MDa ring-shaped ER membrane complex that binds IP3R tetramers and mediates their ERAD with RNF170.
   [PMID:19240031 "the ER membrane protein SPFH1 and its homolog SPFH2 form a heteromeric approximately 2 MDa complex that binds to IP(3)R tetramers"]
   SPFH2 alone was shown to mediate ERAD of IP3 receptors and other substrates (PubMed:17502376, not cached).
   In complex with ERLIN1, interacts with RNF170. ComplexPortal CPX-7121.
2. **Sterol-accelerated ERAD of HMGCR (gp78/AMFR module).** ERLIN2 promotes sterol-accelerated ERAD of
   HMG-CoA reductase via an AMFR/gp78-containing ubiquitin ligase complex; TMUB1 bridges ERLIN2 to gp78.
   [PMID:21343306 "we identify two ER membrane proteins, SPFH2 and TMUB1, as associated proteins of mammalian gp78"]
   Interacts with AMFR, SYVN1, RNF139, TMUB1, HMGCR.
3. **Cholesterol binding / SREBP regulation.** Like ERLIN1, ERLIN2 restricts SREBP activation and
   regulates cholesterol homeostasis; interacts with SCAP, INSIG1, SREBF1, SREBF2 under sterol sufficiency.
   [PMID:24217618 "Erlins bound cholesterol with specificity and strong cooperativity"]
4. **E3-ligase binding.** ERLIN2 binds the ER ubiquitin ligases RNF170, AMFR/gp78, SYVN1, RNF139, and the
   RNF185/RNF5 module (PubMed:24019521) — informative ubiquitin protein ligase binding.
5. **Lipid-raft ER domains** (PMID:16835267).

## Annotation assessment summary
- ER membrane (GO:0005789) / ER (GO:0005783): core compartment → ACCEPT.
- ERLIN1/2 complex / ERAD of IP3R (GO:0036503 ERAD pathway IDA): core → ACCEPT.
- cholesterol binding (GO:0015485 IBA): core MF → ACCEPT (note: only IBA here, no human IDA, but consistent
  with the erlin family cholesterol-binding evidence in PMID:24217618).
- SREBP signaling / negative regulation cholesterol & fatty acid biosynthesis / regulation cholesterol
  biosynthesis: SREBP/sterol role → ACCEPT.
- ubiquitin protein ligase binding (GO:0031625 IPI PMID:24019521; IEA InterPro): binds RNF185/RNF5 and other
  ER E3 ligases → ACCEPT (informative).
- membrane raft (GO:0045121 IDA/NAS): lipid-raft ER domains → KEEP_AS_NON_CORE.
- **plasma membrane (GO:0005886) TAS Reactome (x13, FGFR1 signaling pathways)**: ERLIN2 is an ER membrane
  protein; plasma-membrane localization is an over-annotation from pathway bulk-membrane curation →
  MARK_AS_OVER_ANNOTATED.
- protein-containing complex (GO:0032991): generic → KEEP_AS_NON_CORE.
- protein binding (GO:0005515) IPI: uninformative → KEEP_AS_NON_CORE (TMEM41B interaction PMID:30352685 etc.).
- Do NOT over-claim catalytic MF: ERLIN2 is a scaffold/lipid-binding SPFH protein.

## Falcon deep-research findings (incorporated 2026-06)

All four cited papers below were PMID-verified via PubMed (DOI-to-PMID); none are in the
publications/ cache, so no verbatim supporting_text was added to the review — references
added with reference_review only, plus the Veronese ref id on the E3-ligase/TMUB1 core_function.

- ERLIN1/2 scaffolds form "large ring-like cup-shaped structures on the ER membrane" that
  "bind cholesterol and E3 ubiquitin ligases, potentially defining functional nanodomains."
  [PMID:38782601 "ERLIN1 and ERLIN2 ... form large ring-like cup-shaped structures on the endoplasmic reticulum (ER) membrane and serve as platforms to bind cholesterol and E3 ubiquitin ligases"]
- New mechanistic link: ERLIN scaffolds bridge full-length TMUB1 and RNF170 through a conserved
  luminal N-terminal motif that binds the SPFH/prohibitin domain of two adjacent ERLIN subunits;
  HSP-linked variants map to these interfaces.
  [PMID:38782601 "ERLIN scaffolds mediate the interaction between the full-length isoform of TMUB1 ... and RNF170 ... binds the stomatin/prohibitin/flotillin/HflKC domain of two adjacent ERLIN subunits at different interfaces. Protein variants that preclude these interactions have been previously linked to hereditary spastic paraplegia"]
- New cell-biology role beyond classical ERAD: ERLINs limit cholesterol esterification, favouring
  ER-to-Golgi cholesterol transport and regulating Golgi morphology and the secretory pathway
  (HeLa double-KO phenotype).
  [PMID:38782601 "a role of ERLIN scaffolds in limiting cholesterol esterification, thereby favouring cholesterol transport from the ER to the Golgi apparatus and regulating Golgi morphology and the secretory pathway"]
- Falcon also notes SOAT1 inhibition (avasimibe) rescues lipid-droplet/Golgi phenotypes in
  ERLIN-deficient cells (from figures); treat as a translational/pharmacology lead, not a GO
  annotation. (Veronese 2024, PMID:38782601)
- Proposed dominant disease mechanism: a heterozygous ERLIN2 p.Val71Ala recruits the E3 ligase
  RNF213 (NOT RNF170) to degrade IP3R1, lowering free Ca2+, triggering ER-stress apoptosis and
  suppressing MAPK/proliferation in patient-derived iPSC models.
  [PMID:40225166 "the ERLIN2 heterozygous missense variant protein recruited the ubiquitin E3 ligase RNF213 to degrade IP3R1 ... reduction of intracellular free calcium, which triggered endoplasmic reticulum (ER) stress-mediated apoptosis"]
- SPG18 inheritance is broader than classic recessive: monoallelic/autosomal-dominant ERLIN2
  variants (often pure, late-onset) occur, with HSP-to-ALS phenoconversion (2/5 cases) and a
  recurrent monoallelic c.502G>A hotspot for an ALS-like phenotype.
  [PMID:38427163 "Recent cases of late-onset, pure HSP with monoallelic ERLIN2 variants ... two cases out of five exhibiting HSP-ALS phenoconversion ... relatively high incidence of the c.502G>A variant in monoallelic SPG18 cases"]
- An AD ERLIN2 p.V168M family showed variable expressivity (ALS phenoconversion, pure HSP, and a
  complicated form with psychomotor delay/epilepsy) but NORMAL erlin2 oligomerization, arguing
  against a dominant-negative oligomerization defect for this variant.
  [PMID:38607533 "a phenoconversion to amyotrophic lateral sclerosis (ALS) ... pure HSP ... a complicated form with psychomotor delay and epilepsy ... Erlin2 oligomerization was found to be normal ... we ruled out a dominant negative effect of V168M on erlin2 oligomerization"]
- Caveat: the Falcon report's "cryo-EM of the ERLIN complex" framing is not directly supported by
  a retrieved structural paper; Veronese 2024 uses 3D modelling, not cryo-EM. The existing
  suggested_question about a cryo-EM-resolved architecture remains a forward-looking question.


## 2026-10-24 — current annotation integration checkpoint

All 59 current imported contexts have reviewed decisions: {'ACCEPT': 21, 'MODIFY': 12, 'KEEP_AS_NON_CORE': 26}. Forty-six old contexts match one-to-one. Four historical binding contexts lack explicit partner identities and remain as replaced historical records while all 12 current partner-specific contexts are appended independently. The additional ERAD IBA is also appended. The absent historical cholesterol-binding IBA remains separately preserved: its retired status records the current source boundary, while its biological assessment is UNDECIDED. Current PAINT places cholesterol binding on an ERLIN1 clade outside the ERLIN2 ancestry; this is not a claim of biological loss. The record contains 64 rows, 59 current and five historical. All 57 inherited quotation paths, texts and reference associations remain fixed. No new quotation or NEW annotation is introduced. Three source-described natural products (339, 152 and 206 residues) remain distinct. The ERLIN2–FGFR1 fusion context is retained in its 12 Reactome location records without assigning fusion kinase function to natural ERLIN2. The inherited description, three cores and historical findings are unchanged here and await separate synthesis.


## 2026-10-24 — Core-function synthesis and mechanistic limits

The three ordered summaries now distinguish the integral erlin scaffold, sterol-pathway restraint, and measured ubiquitin-ligase associations. The 64 annotation/source/review objects, three product records and all 57 inherited quotation paths and associated references remain unchanged. No annotation or publication quotation was added. PMID:19751772 and PMID:21610068 were appended using genuine normal records; the preceding 47 reference identities and order remain intact.

The scaffold assignment describes an integral structural component that supports erlin assembly and partner organization. The ERAD quality-control process has separate positive support from misfolded luminal A1AT-NHK and TTR-D18G turnover after combined erlin depletion in human HEK/HeLa cells (PMID:19751772, model-substrate Methods and Figure 6). This modest, selective effect is not a claim that ERLIN2 is universally required for ERAD. Activated IP3R turnover is a regulatory substrate context, not by itself evidence that the receptor is misfolded. Human mHeLa reciprocal-depletion experiments place ERLIN2-dependent complex recruitment before RNF170 recruitment (PMID:21610068, Figure 5C/D and Priority of binding to activated IP3 receptors); the cloned RNF170 reagent is mouse, and separate rodent experiments retain their species boundaries.

The sterol unit retains negative SREBP regulation and regulation of cholesterol biosynthesis without assigning cholesterol-binding molecular function to ERLIN2. The available binding assays do not resolve ERLIN2-specific binding to native cholesterol: PMID:24217618 uses purified human ERLIN1 and a native mouse mixed complex, while the ERLIN2 probe evidence in PMID:23396283 has the recorded ligand-specificity limits. This is a target/ligand-attribution limit, not a rule that GO binding annotations require purified proteins. SREBP processing, transcripts and lipid pools do not themselves measure isotope-resolved biosynthetic flux. Positive gp78-associated HMGCR results in PMID:21343306 coexist with the negative mHeLa/Rat1 conditions in PMID:19751772, Figure 7.

The ligase-association summary does not duplicate an ERAD process or imply that every association recruits a ligase to every cargo. TMUB1 bridging constrains direct-binary interpretations. PMID:24019521, Figure 4A, recovers endogenous human ERLIN2 with RNF185 and RNF5, whereas the principal CFTR functional perturbations concern the ligases.

Modern findings supersede stronger earlier authored interpretations in these notes. In PMID:38782601, erlin double knockout **increases** cholesterol esterification and lipid storage; re-expression and SOAT1 inhibition support the cellular phenotype. Adjacent-subunit interfaces are AlphaFold predictions, and simultaneous TMUB1/RNF170 occupancy is unproven. In PMID:38607533, comparable gross high-molecular-weight assemblies in one heterozygous V168M fibroblast line do not exclude cargo, partner-selection or all dominant-negative defects. In PMID:40225166, patient-cell IP3R1 abundance, calcium measurements and RNF213-associated co-immunoprecipitation support a proposed mechanism, not demonstrated RNF213-dependent ubiquitination or degradation. Isogenic correction, RNF213 rescue and substrate half-life tests remain useful experiments. The questions no longer assume an experimentally resolved human structure, a proven ERLIN2 cholesterol-binding site, or unverified variant examples.

Inherited quotations are retained as historical evidence with their original references. The core 0 PMID:19240031 snippets support complex assembly and activated-receptor turnover; the new quality-control support is the separate unquoted PMID:19751772 citation. The core 1 cholesterol-binding snippet refers to the reagent/complex scope above, not resolved ERLIN2-specific binding. The core 2 RNF185/RNF5 snippet concerns the ligase module; the actual ERLIN2 association is supported by Figure 4A. These quotations were not reassigned to different claims or references.

Current GO:0036503 is named “ERAD quality control pathway”; the inherited label “ERAD pathway” is retained for compatibility with the frozen ontology used by validation and is a current broad synonym. Its current definition governs the biological interpretation. GO:0140378 is an unrestricted molecular-function term for an integral complex scaffold; the ER complex term is placed in `in_complex`, with ER membrane retained as the location. The two sterol processes are not ancestors or descendants of one another in the inspected current ontology. The three product records and the shorter-product boundaries remain unchanged; no canonical-product function was transferred to the 152- or 206-amino-acid products.

Whole-candidate and component schema checks, and strict typed-term/label checks for all three core objects, passed in the private frozen runtime. Final gene-wide status, best-practice validation and rendering remain separate publication checks.


## 2026-10-24 — Structural-subunit attribution

The structural core now records GO:0005198 structural molecule activity for ERLIN2's integral contribution to oligomer integrity, and `contributes_to_molecular_function: GO:0140378` for the assembly's scaffold activity. Physical assembly evidence (PMID:19240031) and human complex-dependent partner association (PMID:38782601) support this synthesis without independently resolved ERLIN2 bridging or equal/interchangeable subunits. The two slots express distinct attribution levels within one core. No NEW scaffold annotation is proposed because the synthesis is bounded to structural participation in the complex; an independently enabled ERLIN2 scaffold activity is not established. All 64 annotation/review objects, three products, 49 reference identities and 57 inherited quotation paths remain exact. No new original-access or figure-inspection claim is made by this refinement.

Final canonical validation records DRAFT with 17 advisories. All 59 current source contexts, five retained historical contexts, three product records and 57 inherited quotation paths were checked; all 139 authored narratives appear in the private HTML rendering. The structural-molecule core and complex scaffold contribution remain bounded synthesis without a duplicate NEW assertion.
