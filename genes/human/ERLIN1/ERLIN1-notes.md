# ERLIN1 (SPFH1 / ER lipid raft-associated protein 1) review notes

UniProt: O75477 (ERLN1_HUMAN), 348 aa. Synonyms SPFH1, KE04, C10orf69. HGNC:16947.
Single-pass type II ER membrane protein with an SPFH/prohibitin (band 7) domain in the ER lumen.
Belongs to the band 7/mec-2 (prohibitin/stomatin/flotillin) family. Associates with lipid-raft-like
ER membrane domains. Disease: autosomal recessive spastic paraplegia SPG62 (variant G50V).

## Core biology
1. **ERLIN1/ERLIN2 complex mediating ERAD of IP3 receptors.** ERLIN1 (SPFH1) and ERLIN2 (SPFH2) form a
   heteromeric ~2 MDa ring-shaped complex that binds IP3R tetramers and mediates their ERAD with the E3
   ligase RNF170.
   [PMID:19240031 "the ER membrane protein SPFH1 and its homolog SPFH2 form a heteromeric approximately 2 MDa complex that binds to IP(3)R tetramers"]
   [PMID:19240031 "RNA interference-mediated depletion of SPFH1 and SPFH2 blocks IP(3)R"]
   ComplexPortal CPX-7121 "ERLIN1-ERLIN2 complex". In complex with ERLIN2, interacts with RNF170.
2. **Cholesterol binding / SREBP regulation.** Erlins bind cholesterol cooperatively and restrict SREBP
   activation, promoting ER retention of the SCAP-SREBP-Insig complex; they regulate cellular cholesterol
   homeostasis and cholesterol/fatty-acid biosynthesis.
   [PMID:24217618 "Erlins bound cholesterol with specificity and strong cooperativity"]
   [PMID:24217618 "define erlins as novel cholesterol-binding proteins that are directly involved in regulating the SREBP machinery"]
   [PMID:24217618 "promote stability of the SREBP-Scap-Insig complex"]
3. **Sterol-accelerated HMGCR ERAD (gp78/AMFR module).** ERLIN1 interacts with the gp78/AMFR and
   SYVN1/HRD1 ER ubiquitin ligases; SPFH2/TMUB1 link gp78 to sterol-accelerated ERAD of HMG-CoA reductase.
   [PMID:21343306 "we identify two ER membrane proteins, SPFH2 and TMUB1, as associated proteins of mammalian gp78"]
4. **Lipid-raft ER domains.** Erlin-1/2 are prohibitin-family proteins that define lipid-raft-like domains
   of the ER.
   [PMID:16835267 "Erlin-1 and erlin-2 are novel members of the prohibitin family of proteins that define lipid-raft-like domains of the ER"]
5. **USP25/cholesterol/virus.** USP25 deubiquitinates and stabilizes ERLIN1; Usp25-Erlin1/2 activity
   limits cholesterol flux to restrict virus infection (PMID:37683630, not cached — referenced via UniProt).

## Annotation assessment summary
- ER membrane (GO:0005789) / ER (GO:0005783): core compartment → ACCEPT (many redundant Reactome TAS CFTR/CD274
  ERAD-machinery annotations → ACCEPT as correct compartment but non-core specifics).
- ERLIN1/2 complex / ERAD of IP3R (GO:0036503 ERAD pathway IDA): core → ACCEPT.
- cholesterol binding (GO:0015485 IDA): core MF → ACCEPT.
- SREBP signaling (GO:0032933), regulation/negative regulation of cholesterol biosynthesis (GO:0045540/45541),
  negative regulation of fatty acid biosynthesis (GO:0045717): SREBP/sterol role → ACCEPT.
- membrane raft (GO:0045121 NAS): lipid-raft ER domains → ACCEPT (non-core).
- ubiquitin protein ligase binding (GO:0031625 IEA InterPro): consistent with AMFR/SYVN1/RNF170 E3 interactions → ACCEPT (informative).
- protein-containing complex (GO:0032991): generic → KEEP_AS_NON_CORE.
- protein binding (GO:0005515) IPI: uninformative → KEEP_AS_NON_CORE.
- Do NOT over-claim catalytic MF: ERLIN1 is a scaffold/lipid-binding SPFH protein, not an enzyme.

## Falcon deep-research findings (incorporated 2026-06)

Falcon corroborates the existing review (ERLIN1/2 ring complex, IP3R ERAD with RNF170, cholesterol
binding, SREBP restriction, lipid-raft ER domains) and adds three verifiable, mostly newer references:

- ERLIN1/2 scaffolds bridge the full-length isoform of TMUB1 with the E3 ligase RNF170 (conserved
  luminal N-terminal motif binding adjacent ERLIN SPFH domains), and restrict cholesterol
  esterification, thereby favouring ER-to-Golgi cholesterol transport and regulating Golgi morphology
  and the secretory pathway. [PMID:38782601 "we demonstrate a role of ERLIN scaffolds in limiting
  cholesterol esterification, thereby favouring cholesterol transport from the ER to the Golgi
  apparatus and regulating Golgi morphology and the secretory pathway"] (PubMed-verified;
  doi:10.26508/lsa.202402620; Veronese et al. 2024). NEW mechanism (TMUB1-L/RNF170 bridging +
  cholesterol esterification/SOAT1 + secretory pathway) beyond the prior single-client IP3R-ERAD
  model. Added as a top-level reference (relevance HIGH). Loss of ERLINs abolished the TMUB1-RNF170
  interaction; reported SOAT1 tendency to increase in DKO (log2FC 0.40, q=0.07), ER tubule collapse,
  Golgi fragmentation, lipid-droplet accumulation, avasimibe (SOAT1 inhibitor) rescue.
- Largest SPG62 case series to date: 13 individuals from six families with biallelic ERLIN1 variants,
  childhood-onset slowly progressive predominantly pure spastic paraparesis (possible cerebellar /
  peripheral-nerve involvement); three new variants predicted to disrupt the bell-shaped ERLIN1/ERLIN2
  ring. [PMID:39367212 "Biallelic pathogenic ERLIN1 variants induce a rare, predominantly pure,
  spastic paraparesis, with possible cerebellar and peripheral nerve involvement"] (PubMed-verified;
  doi:10.1007/s00439-024-02702-0; Cogan et al. 2024). Expands disease genetics beyond the G50V variant
  noted in the prior review. Added as a top-level reference (relevance HIGH).
- ERLIN1 is a host factor required for efficient hepatitis C virus infection; it is a cholesterol-
  binding ER detergent-resistant-membrane protein, and its knockdown reduces HCV RNA replication
  initiation, viral protein expression, and infectious virus production downstream of entry/primary
  translation. [PMID:31810281 "erlin-1 protein is required early in the infection, downstream of cell
  entry and primary translation, specifically to initiate RNA replication, and later in the infection
  to support infectious virus production"] (PubMed-verified; doi:10.3390/cells8121555; Whitten-Bauer
  et al. 2019). Corroborates the cholesterol-homeostasis/ER-raft role already in the review (which
  also has the USP25-Erlin1/2 antiviral angle via PMID:37683630). Added as a top-level reference
  (relevance MEDIUM).
- Manganelli 2021 (PMID:34572057, already a review reference) plus its companion paper
  (doi:10.1080/15548627.2020.1834207) describe ERLIN1 at MAM raft-like microdomains interacting with
  AMBRA1 to support starvation-induced autophagy initiation. Not added as a new annotation/reference;
  noted here as additional context for a potential MAM/autophagy role.
- Note: none of the three new references were cached in publications/, so no paraphrased
  supporting_text was added to existing annotations (reference validator requires verbatim cached
  substrings). They were added as top-level references with reference_review only.


## 2026-10-24 — current annotation integration checkpoint

All 53 current imported contexts have proposed decisions: 27 ACCEPT, eight MODIFY and 18 KEEP_AS_NON_CORE. Thirty-four contexts are matched one-to-one to existing rows and enriched with their current machine-supplied provenance. Five older aggregate binding contexts lack current partner identities; they remain in their original positions as retired historical records, with all 18 current partner-specific contexts appended independently. The additional ERAD IBA is also appended. The record therefore contains 58 rows, of which 53 are active and five retired. All 43 inherited supporting-text paths and values are preserved; none is assigned to an arbitrary partner, moved or duplicated. No new publication quotation or NEW annotation is introduced. The original core, description and historical findings remain unchanged at this annotation checkpoint and are pending the separate synthesis phase. The source guide records actual original reading limits and the genuine new human ERAD reference PMID:19751772.


## 2026-10-24: core synthesis and modern original-source reassessment

The two inherited core slots now distinguish the integral structural activity of the ERLIN complex from ERLIN1 cholesterol binding. Current GO:0140378 describes a protein-complex scaffold; GO:0030674 explicitly directs integral complex scaffolds to that term. This identifies an organizing component of the assembly, without assigning RNF170's ubiquitin-transfer chemistry to ERLIN1 or adding a duplicate adaptor core. Complex membership is separate from ER-membrane location.

The current name and definition of GO:0036503 specify ERAD quality control. The positive quality-control evidence is the modest stabilization of misfolded A1AT-NHK and TTR-D18G after combined erlin depletion in human cells ([PMID:19751772](https://doi.org/10.1016/j.bbamcr.2009.09.004), Figure 6/Results). Activated IP3-receptor turnover is a distinct regulatory substrate example; it is not described as misfolded-protein disposal. The RNF170 recruitment ordering is supported at complex level by human mHeLa depletion experiments monitored through ERLIN2 ([PMID:21610068](https://doi.org/10.1074/jbc.M111.251983), Priority of Binding to Activated IP3 Receptors/Figure 5). Mouse RNF170 constructs and rodent native-cell experiments remain separately identified.

Actual modern originals replace the earlier availability statements for PMID:38782601, PMID:39367212 and PMID:31810281. The normal PMID:37683630 cache is still abstract-only; its actual original was recovered independently and read. Manual access assessments reflect those reads without changing normal cache bytes. Cholesterol-binding, lipid-abundance and gene-expression evidence supports sterol regulation, but does not uniquely establish an Insig/SREBP scaffold mechanism or direct ERLIN1 cholesterol transport. The 2023 efflux assay and T65I construct are ERLIN2-specific. The 2024 interaction surfaces and clinical assembly defects remain models, distinct from the positive cellular interaction and RNA-splicing experiments.

The displayed natural product is the source-described 348-aa O75477 sequence. No additional isoform is invented. All 58 accepted annotation rows, their source/review objects, and all 43 inherited quotation paths, values and reference associations remain unchanged. The two existing core citation prefixes remain in order. PMID:21610068 is added to the review references from its already acquired genuine normal record; no new normal source was generated. This synthesis preserves the inherited status pending final whole-gene validation. Focused questions concern sterol coupling, assembly/cargo recruitment and RNA-versus-protein effects of disease variants.

The first strict core validation found one ontology-version label mismatch: live QuickGO prefers ERAD quality control pathway for GO:0036503, while the frozen validator uses the inherited ERAD pathway label. The latter remains an explicit live broad synonym and is retained for compatibility. The current quality-control definition governs the biological interpretation above; the ID and scope are unchanged. The failed receipt is preserved, and no ontology/configuration/cache was edited.

## 2026-10-24: final validation

The integrated review passes canonical GOA/schema validation, strict term validation, ontology-component checks, computed-status checks and rendering. All 125 review narratives appear in the rendered output. The derived HTML was inspected privately; the previously committed HTML and other legacy generated artifacts remain unchanged. The 43 selected normal sources retain their acquired bytes, including the genuinely refreshed GOA/UniProt records and newly acquired PMID:11118313 and PMID:19751772 caches.

The computed status is DRAFT with 25 advisories: 22 supported generic-binding rows retained as non-core under the campaign policy, one deliberately different assessment of a generic experimental complex versus the independently refined electronic complex assertion, an unused historical provider report, and a core scaffold activity without a duplicate NEW annotation. The first status command reported the inherited COMPLETE label as a mismatch; that command only fills missing statuses. The status alone was explicitly corrected to DRAFT, and the repeated status check passed. No biological field was changed to suppress an advisory.

Final counts are 58 rows (53 active plus five retained historical aggregates): 27 ACCEPT, eight MODIFY and 23 KEEP_AS_NON_CORE overall; the active rows contain 27 ACCEPT, eight MODIFY and 18 KEEP_AS_NON_CORE. There are 33 references, two core functions, and one displayed 348-residue natural product. All 43 inherited quotation paths, literal texts and reference associations remain fixed. No NEW annotation or new publication quotation is introduced.


## 2026-10-24 — Exact-head review follow-up

The first core now records structural molecule activity (GO:0005198) for ERLIN1's physical contribution to the oligomeric assembly, and `contributes_to_molecular_function: GO:0140378` for scaffold activity of the ERLIN1/ERLIN2 complex. This follows the schema distinction between a subunit's activity and its contribution to a complex activity. Physical oligomer composition/assembly and complex-dependent partner association support the synthesis (PMID:19240031; PMID:38782601). It does not assert an isolated ERLIN1 bridging assay, equal or interchangeable subunits, or an experimentally resolved interface. GO:0005198 describes contribution to structural integrity, while GO:0140378 describes integral complex scaffolding; the two slots express different relationships.

No NEW scaffold annotation is proposed: the synthesis records a bounded structural contribution while the experiments do not isolate an independently enabled ERLIN1 scaffold activity. Existing source annotations, inherited quotations and all reference identities remain fixed. The membrane-raft NAS context is now KEEP_AS_NON_CORE, resolving the earlier notes' ambiguous “ACCEPT (non-core)” wording. The fractionation evidence stays positive; ER membrane remains the primary core location. Current counts are 26 ACCEPT, eight MODIFY and 19 KEEP_AS_NON_CORE across 53 active contexts; five retained historical contexts give 58 total rows with 24 non-core decisions.

The current GO:0036503 quality-control definition continues to govern the biology; its inherited broad-synonym label remains necessary for the frozen validator. The ADRA1D-associated preparation and the erlin ER complex retain deliberately different GO:0032991 decisions. PMID:11118313 is a genuine normal dependency cited by the UniProt source record, not a newly adjudicated direct annotation reference. No quotation backfill or reassociation was needed for this revision.

The broad structural-molecule term is also retained only in core synthesis, without a NEW source-level assertion. Validation passes with 25 advisories, including that deliberate synthesis-versus-annotation distinction; computed status remains DRAFT.
