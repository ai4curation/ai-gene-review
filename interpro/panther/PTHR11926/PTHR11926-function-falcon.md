---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-24T05:17:48.246684'
end_time: '2026-06-24T05:45:07.839998'
duration_seconds: 1639.59
template_file: templates/treegrafter_family_function.md
template_variables:
  family_id: PTHR11926
  family_name: GLUCOSYL/GLUCURONOSYL TRANSFERASES
  subfamily: PTHR11926:SF1392 GLYCOSYLTRANSFERASE
  gene_symbol: NaUGT1_candidate_UGT85A2_0
  uniprot: A0A2H4GSI3
  organism: NICAT
  taxon_label: NICAT
  propagated_term: quercetin 3-O-glucosyltransferase activity (GO:0080043)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 34
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: PTHR11926-function-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PTHR11926-function-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# PANTHER Family Function Characterization (TreeGrafter granularity audit)

You are characterizing the function of a **protein family** for AI Gene Review.
This is the companion to a set of blinded gene-level function checks: the point
here is to establish, from primary literature and sequence/structure evidence,
**what function is actually conserved across the family** and **where function
diverges between subfamilies** — because automated phylogenetic annotation
(TreeGrafter/PANTHER) propagates a GO term from an ancestral node to every
descendant, and that is only safe when the family is functionally homogeneous.

## Family Under Review

- **PANTHER family:** PTHR11926 — GLUCOSYL/GLUCURONOSYL TRANSFERASES
- **Subfamily of interest:** PTHR11926:SF1392 GLYCOSYLTRANSFERASE
- **Representative member:** NaUGT1_candidate_UGT85A2_0 (A0A2H4GSI3), NICAT / NICAT
- **GO term currently propagated at/near this node:** quercetin 3-O-glucosyltransferase activity (GO:0080043)

Note: do **not** assume the propagated term is the family's true conserved
function — that is exactly what you are testing.

## Research Objective

1. **Conserved core function.** What molecular function (and reaction/EC where
   relevant) is shared by *characterized* members across the whole family? Anchor
   this to the diagnostic fold, catalytic/binding residues, and obligate
   cofactors/partners — not to the family name.
2. **Functional divergence across subfamilies.** Enumerate the major
   functional subgroups within the family and how they differ (substrate
   specificity, lost catalysis / pseudo-enzymes, neofunctionalization, structural
   co-option). Is the family **homogeneous** (one MF safe to propagate) or
   **heterogeneous** (propagation will mis-annotate some branches)?
3. **Subfamily of interest.** Where does PTHR11926:SF1392 GLYCOSYLTRANSFERASE sit — does it carry the
   conserved family function, a more specific specialized activity, or a diverged
   / non-enzymatic role? Name characterized exemplars of that subfamily.
4. **GO granularity verdict.** State the GO MF term appropriate at the **family**
   level versus at the **subfamily** level, and identify any subfamilies for
   which a family-level term would be an over-annotation. This is a lead for
   curators, not a final call.

Where decidable by computation, actually run it (domain/Pfam/InterPro
architecture, catalytic-residue conservation, orthology/paralogy splits) and keep
the result as provenance. Use resources you can access programmatically
(UniProt, InterPro, AlphaFold, sequence computation, public APIs). Prefer PMID
citations to primary literature; treat reviews/databases as orientation. If a
check is web-only or cannot be run, say so — an inconclusive result is acceptable;
never fabricate one.

## Required Output

### Family Function Summary

One paragraph: the conserved core molecular function and the fold/residues that
define it.

### Subfamily Divergence Table

One row per major functional subgroup: subgroup / representative member(s) (PMID)
· molecular function · substrate or specialization · catalytic residues intact?
· GO MF term that fits · notes (pseudo-enzyme, neofunctionalization, etc.).

### Homogeneous vs Heterogeneous Verdict

State plainly whether a single family-level GO MF term is safe to propagate
across this family, and if not, which branches it would mis-annotate.

### Granularity Leads for Curation

Family-level vs subfamily-level GO MF term recommendation, and the subfamilies
(if any) where the currently-propagated term is an over-annotation. Avoid
"protein binding" as a final recommendation.

### Evidence and Gaps

Key citations (PMID preferred), and explicit uncertainties that matter for
deciding the family-vs-subfamily granularity.


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

# PANTHER Family Function Characterization (TreeGrafter granularity audit)

You are characterizing the function of a **protein family** for AI Gene Review.
This is the companion to a set of blinded gene-level function checks: the point
here is to establish, from primary literature and sequence/structure evidence,
**what function is actually conserved across the family** and **where function
diverges between subfamilies** — because automated phylogenetic annotation
(TreeGrafter/PANTHER) propagates a GO term from an ancestral node to every
descendant, and that is only safe when the family is functionally homogeneous.

## Family Under Review

- **PANTHER family:** PTHR11926 — GLUCOSYL/GLUCURONOSYL TRANSFERASES
- **Subfamily of interest:** PTHR11926:SF1392 GLYCOSYLTRANSFERASE
- **Representative member:** NaUGT1_candidate_UGT85A2_0 (A0A2H4GSI3), NICAT / NICAT
- **GO term currently propagated at/near this node:** quercetin 3-O-glucosyltransferase activity (GO:0080043)

Note: do **not** assume the propagated term is the family's true conserved
function — that is exactly what you are testing.

## Research Objective

1. **Conserved core function.** What molecular function (and reaction/EC where
   relevant) is shared by *characterized* members across the whole family? Anchor
   this to the diagnostic fold, catalytic/binding residues, and obligate
   cofactors/partners — not to the family name.
2. **Functional divergence across subfamilies.** Enumerate the major
   functional subgroups within the family and how they differ (substrate
   specificity, lost catalysis / pseudo-enzymes, neofunctionalization, structural
   co-option). Is the family **homogeneous** (one MF safe to propagate) or
   **heterogeneous** (propagation will mis-annotate some branches)?
3. **Subfamily of interest.** Where does PTHR11926:SF1392 GLYCOSYLTRANSFERASE sit — does it carry the
   conserved family function, a more specific specialized activity, or a diverged
   / non-enzymatic role? Name characterized exemplars of that subfamily.
4. **GO granularity verdict.** State the GO MF term appropriate at the **family**
   level versus at the **subfamily** level, and identify any subfamilies for
   which a family-level term would be an over-annotation. This is a lead for
   curators, not a final call.

Where decidable by computation, actually run it (domain/Pfam/InterPro
architecture, catalytic-residue conservation, orthology/paralogy splits) and keep
the result as provenance. Use resources you can access programmatically
(UniProt, InterPro, AlphaFold, sequence computation, public APIs). Prefer PMID
citations to primary literature; treat reviews/databases as orientation. If a
check is web-only or cannot be run, say so — an inconclusive result is acceptable;
never fabricate one.

## Required Output

### Family Function Summary

One paragraph: the conserved core molecular function and the fold/residues that
define it.

### Subfamily Divergence Table

One row per major functional subgroup: subgroup / representative member(s) (PMID)
· molecular function · substrate or specialization · catalytic residues intact?
· GO MF term that fits · notes (pseudo-enzyme, neofunctionalization, etc.).

### Homogeneous vs Heterogeneous Verdict

State plainly whether a single family-level GO MF term is safe to propagate
across this family, and if not, which branches it would mis-annotate.

### Granularity Leads for Curation

Family-level vs subfamily-level GO MF term recommendation, and the subfamilies
(if any) where the currently-propagated term is an over-annotation. Avoid
"protein binding" as a final recommendation.

### Evidence and Gaps

Key citations (PMID preferred), and explicit uncertainties that matter for
deciding the family-vs-subfamily granularity.


## PANTHER Family PTHR11926 — GLUCOSYL/GLUCURONOSYL TRANSFERASES: TreeGrafter Granularity Audit

---

### Family Function Summary

PTHR11926 corresponds to the glycosyltransferase family 1 (GT1) superfamily, encompassing plant UDP-glycosyltransferases (UGTs) and related mammalian UDP-glucuronosyltransferases. All characterized members share a conserved GT-B fold consisting of two Rossmann-type domains connected by a linker region that forms a substrate-binding cleft (gharabli2024thesugardonor pages 3-4, speeckaert2022ugt72amajor pages 2-5). The C-terminal domain contains the family-defining Plant Secondary Product Glycosyltransferase (PSPG) motif, a 44-amino-acid consensus sequence under strong purifying selection (Ka/Ks ≪ 1), which is essential for UDP-sugar donor binding and recognition (gharabli2024thesugardonor pages 3-4, gachon2005plantsecondarymetabolism pages 3-4). The catalytic mechanism employs a conserved His-Asp dyad: the histidine residue (e.g., His-19/His-22) acts as a Brønsted base to deprotonate the sugar acceptor's functional group, enabling nucleophilic attack on the C1′ carbon of the UDP-sugar donor, while the aspartate (e.g., Asp-121) stabilizes the active site (gharabli2024thesugardonor pages 1-3, lethe2024similaritiesinstructure pages 4-5). The conserved core molecular function is the regio- and stereoselective transfer of a sugar moiety from a UDP-activated donor (predominantly UDP-glucose in plants, UDP-glucuronic acid in mammals) to a diverse array of acceptor substrates. Critically, while the catalytic mechanism and fold are conserved, the N-terminal acceptor-binding domain is highly variable, leading to extreme substrate diversity across the family — encompassing flavonoids, monolignols, plant hormones (auxins, cytokinins, abscisic acid, brassinosteroids, salicylic acid), terpenoids, cyanogenic glucoside precursors, glucosinolate intermediates, and xenobiotics (rehman2018comparativegenomicand pages 13-13, lethe2024similaritiesinstructure pages 5-7, bowles2006glycosyltransferasesoflipophilic pages 6-7, lim2004aclassof pages 4-5).

---

### Subfamily Divergence Table

The following table enumerates the major functional subgroups within PTHR11926 and their characterized substrate specificities:

| Subgroup/Phylogenetic Group | Representative Member(s) | Molecular Function | Substrate/Specialization | Catalytic Residues Intact? | GO MF Term that Fits | Notes |
|---|---|---|---|---|---|---|
| Group A (UGT74/UGT84) | UGT74B1, UGT74F1/F2, UGT84B1 | UDP-glycosyltransferase activities in glucosinolate precursor, salicylic acid, and auxin conjugation pathways | Thiohydroximates/glucosinolate biosynthesis; salicylic acid glucoside/glucose ester; indole-3-acetic acid glucose ester | Yes | glucosyltransferase activity; indole-3-acetate beta-glucosyltransferase activity; salicylic acid glucosyltransferase activity | Hormone and defense-metabolite conjugation branch; not flavonoid-specific (rehman2018comparativegenomicand pages 13-13, bowles2006glycosyltransferasesoflipophilic pages 9-10, gachon2005plantsecondarymetabolism pages 4-5, bowles2006glycosyltransferasesoflipophilic pages 16-17, lim2004aclassof pages 4-5) |
| Group D (UGT73) | UGT73C5, UGT73K1, UGT73A5 | Broad-spectrum UDP-glycosyltransferase activities | Brassinosteroids, triterpene aglycones/saponins, flavonoids, betanidin, xenobiotics | Yes | glucosyltransferase activity | Explicitly heterogeneous even within one phylogenetic group; sequence does not predict a single acceptor class safely here (gachon2005plantsecondarymetabolism pages 3-4, gachon2005plantsecondarymetabolism pages 5-7, gachon2005plantsecondarymetabolism pages 4-5, lim2004aclassof pages 4-5) |
| Group E (UGT72) | UGT72E1-E3, UGT72B1, UGT72B3 | O-glycosyltransferase activities for phenylpropanoids and related small molecules | Monolignols, monolignol aldehydes/acids, flavonoids, coumarins, some xenobiotics | Yes | monolignol 4-O-glucosyltransferase activity; flavonoid glucosyltransferase activity; glucosyltransferase activity | Conserved GT-B fold and catalytic His/Asp chemistry, but acceptor range spans lignin precursors to flavonoids/coumarins (speeckaert2022ugt72amajor pages 2-5, speeckaert2022ugt72amajor pages 5-8, bowles2006glycosyltransferasesoflipophilic pages 7-9, lim2004aclassof pages 5-7) |
| Group F (UGT78) | UGT78D1, UGT78D2 | Flavonoid 3-O-glycosyltransferase activities | Flavonols including quercetin/kaempferol; anthocyanin-related flavonoids | Yes | quercetin 3-O-glucosyltransferase activity; flavonol 3-O-glucosyltransferase activity | This is the branch that contains bona fide quercetin/flavonol 3-O-glucosyltransferases; a much better home for GO:0080043 than UGT85 (gachon2005plantsecondarymetabolism pages 4-5, lim2004aclassof pages 4-5) |
| Group G (UGT85) | UGT85B1, UGT85C2, UGT85A1, UGT85K4/K5 | UDP-glycosyltransferase activities acting on cyanohydrins, diterpenes, and cytokinins | p-Hydroxymandelonitrile to dhurrin; steviol C13 glucosylation; trans-zeatin O-glucosylation; cyanogenic glucoside biosynthesis | Yes | glucosyltransferase activity; cytokinin glucosyltransferase activity; cyanohydrin glucosyltransferase activity | **Subfamily of interest (SF1392) sits here. Group G members do NOT glycosylate quercetin and should not receive quercetin 3-O-glucosyltransferase annotations by propagation** (zhou2021metabolicengineeringfor pages 7-8, gachon2005plantsecondarymetabolism pages 4-5, bowles2006glycosyltransferasesoflipophilic pages 16-17, nielsen2008metabolonformationin pages 1-2, nielsen2008metabolonformationin pages 2-3, selmar2010biosynthesisofcyanogenic pages 22-25, zhou2021metabolicengineeringfor pages 8-10) |
| Group H (UGT76) | UGT76C1, UGT76C2, UGT76G1 | Cytokinin N-glucosyltransferase and steviol glycoside-modifying glucosyltransferase activities | trans-Zeatin N-glucosides; downstream steviol glycoside elaboration | Yes | cytokinin N-glucosyltransferase activity; glucosyltransferase activity | Distinct from UGT85: related to cytokinin N-glucosylation and steviol glycoside modification rather than quercetin 3-O-glucosylation (bowles2006glycosyltransferasesoflipophilic pages 9-10, gachon2005plantsecondarymetabolism pages 4-5) |
| Group L (flavonoid GTs) | Bz1, Ph1, Pgt8, RhGT1 | Flavonoid/anthocyanin glycosyltransferase activities | Anthocyanidins, anthocyanins, flavonoids in pigment biosynthesis | Yes | anthocyanidin 3-O-glucosyltransferase activity; flavonoid glucosyltransferase activity | Pigment-specialized branch with conserved flavonoid context; still distinct from UGT85 Group G chemistry (gachon2005plantsecondarymetabolism pages 4-5, lim2004aclassof pages 4-5) |
| Mammalian UGTs (UGT1A/UGT2B) | UGT1A1, UGT1A9, UGT2B family | UDP-glucuronosyltransferase activities in phase II detoxification | Xenobiotics, drugs, bilirubin, steroids, bile acids, dietary flavonoids | Yes | glucuronosyltransferase activity | Same broad superfamily logic but membrane-bound ER enzymes in animals; donor preference and physiology differ markedly from soluble plant UGT85 enzymes (lethe2024similaritiesinstructure pages 5-7, lim2004aclassof pages 3-4, lethe2024similaritiesinstructure pages 1-4, lethe2024similaritiesinstructure pages 4-5) |


*Table: This table summarizes the major functional branches within PTHR11926 and highlights that the UGT85-containing Group G, where SF1392 sits, is functionally distinct from the flavonoid 3-O-glucosyltransferase branches. It is useful for evaluating whether quercetin 3-O-glucosyltransferase activity is safe to propagate at family or subfamily level.*

---

### Homogeneous vs. Heterogeneous Verdict

**PTHR11926 is unambiguously HETEROGENEOUS.** A single substrate-specific GO molecular function term cannot be safely propagated across this family. The conserved core — the GT-B fold, PSPG motif, and His-Asp catalytic dyad — defines only the general capacity for UDP-sugar-dependent glycosyl transfer (EC 2.4.1.-), not the identity of the acceptor substrate, the regioselectivity of sugar attachment, or the sugar donor employed (gharabli2024thesugardonor pages 3-4, speeckaert2022ugt72amajor pages 2-5, gharabli2024thesugardonor pages 1-3).

Within plant UGTs alone, there are 14 recognized phylogenetic groups (A–N), and these groups show extensively divergent substrate specificities (rehman2018comparativegenomicand pages 3-6, gachon2005plantsecondarymetabolism pages 3-4). Even within individual phylogenetic groups, substrate specificity can vary dramatically — Group D (UGT73 family), for example, contains enzymes acting on brassinosteroids, triterpene saponins, flavonoids, and betacyanin (gachon2005plantsecondarymetabolism pages 3-4). Furthermore, it is established that sequence homology does not reliably predict substrate specificity: enzymes with low sequence identity can glycosylate the same substrate, and closely related paralogs can exhibit switched regioselectivity (lethe2024similaritiesinstructure pages 5-7, speeckaert2022ugt72amajor pages 5-8, lim2004aclassof pages 5-7). Mammalian UGTs (UGT1A/UGT2B families) within this same superfamily use UDP-glucuronic acid rather than UDP-glucose and act on entirely different substrates (drugs, bilirubin, steroids) in a membrane-bound ER context (lim2004aclassof pages 3-4, lethe2024similaritiesinstructure pages 1-4).

Propagating any acceptor-specific GO term (such as quercetin 3-O-glucosyltransferase activity) from an ancestral node of this family would mis-annotate the vast majority of descendant branches, including those glycosylating hormones, monolignols, cyanohydrins, terpenoids, glucosinolate precursors, and xenobiotics.

---

### Granularity Leads for Curation

> **Verdict: HETEROGENEOUS.** PTHR11926 is a functionally heterogeneous family of family-1 UDP-glycosyltransferases; what is conserved is the GT-B fold, the C-terminal PSPG donor-binding motif, and the catalytic His-Asp chemistry for UDP-sugar transfer, not a single acceptor or regio-specific activity. Therefore, a substrate-specific MF such as quercetin 3-O-glucosyltransferase activity cannot be safely propagated across the family. Characterized branches act on hormones, flavonoids, monolignols, cyanohydrins, terpenoids, glucosinolate precursors, and xenobiotics (gharabli2024thesugardonor pages 3-4, speeckaert2022ugt72amajor pages 2-5, rehman2018comparativegenomicand pages 13-13, lethe2024similaritiesinstructure pages 5-7, rehman2018comparativegenomicand pages 3-6).
>
> **Family-level GO lead:** use a broad term such as **UDP-glycosyltransferase activity (GO:0008194)** or, more conservatively, **transferase activity, transferring glycosyl groups (GO:0016757)**. These terms match the conserved structural/mechanistic core without overcommitting on acceptor identity or glycosylation position (gharabli2024thesugardonor pages 3-4, speeckaert2022ugt72amajor pages 2-5, gharabli2024thesugardonor pages 1-3, lethe2024similaritiesinstructure pages 4-5).
>
> **Subfamily PTHR11926:SF1392 / UGT85A lead:** the propagated **quercetin 3-O-glucosyltransferase activity (GO:0080043)** is a **mis-annotation** for this branch. Characterized UGT85-family members instead include cytokinin O-glucosylation (UGT85A1; trans-zeatin), cyanohydrin glucosylation in dhurrin biosynthesis (UGT85B1), and steviol C13 glucosylation (UGT85C2); these data support a broader **UDP-glucosyltransferase activity (GO:0035251)** call, or a more specific **cytokinin glucosyltransferase activity** only if direct subfamily-specific experimental evidence is assembled for SF1392 itself (zhou2021metabolicengineeringfor pages 7-8, rehman2018comparativegenomicand pages 13-13, nielsen2008metabolonformationin pages 1-2, nielsen2008metabolonformationin pages 2-3, zhou2021metabolicengineeringfor pages 8-10).
>
> **Placement of the quercetin term:** bona fide quercetin/flavonol 3-O-glucosyltransferase activity maps to flavonoid-specialized branches such as **Group F / UGT78** (and some related flavonoid GT clades), not to **Group G / UGT85** where SF1392 sits. Propagating GO:0080043 onto UGT85 therefore conflates distinct evolutionary branches and would mis-annotate cytokinin-, cyanogenic-, and diterpene-active enzymes (gachon2005plantsecondarymetabolism pages 4-5, lim2004aclassof pages 4-5, gachon2005plantsecondarymetabolism pages 3-4).


*Blockquote: This blockquote summarizes the curation recommendation for PTHR11926 and SF1392, emphasizing that the family is heterogeneous and that GO:0080043 is too specific and misplaced for the UGT85 branch.*

**Specific leads:**

1. **Family-level (PTHR11926) GO MF recommendation:** Use **UDP-glycosyltransferase activity (GO:0008194)** or the more general **transferase activity, transferring glycosyl groups (GO:0016757)**. These terms capture the conserved enzymatic mechanism (UDP-sugar dependent glycosyl transfer) without committing to any particular acceptor substrate or regioselectivity. This is the only safe level of granularity for the whole family.

2. **Subfamily PTHR11926:SF1392 (UGT85A / Group G) GO MF recommendation:** The currently propagated **quercetin 3-O-glucosyltransferase activity (GO:0080043) is a mis-annotation** and should be removed or replaced. Characterized UGT85A-subfamily members include Arabidopsis UGT85A1, a trans-zeatin O-glucosyltransferase involved in cytokinin homeostasis (PMID 23263235) (rehman2018comparativegenomicand pages 13-13), and cucumber CsUGT85A2, which regulates cytokinin content. Within the broader UGT85 clan (phylogenetic group G), UGT85B1 from sorghum glucosylates the cyanohydrin p-hydroxymandelonitrile in dhurrin biosynthesis (PMID 17959211) (nielsen2008metabolonformationin pages 1-2, nielsen2008metabolonformationin pages 2-3, selmar2010biosynthesisofcyanogenic pages 22-25), UGT85C2 from stevia catalyzes β-1,2-glucosylation at the C13 position of steviol in steviol glycoside biosynthesis (PMID 15610349) (zhou2021metabolicengineeringfor pages 8-10, zhou2021metabolicengineeringfor pages 7-8), and UGT85K4/K5 from cassava catalyze cyanogenic glucoside biosynthesis (PMID 21916862). None of these characterized UGT85 members glycosylates quercetin at the 3-O position. An appropriate subfamily-level term would be **UDP-glucosyltransferase activity (GO:0035251)**, pending further experimental characterization of the specific representative (A0A2H4GSI3 from *Nicotiana attenuata*).

3. **Quercetin 3-O-glucosyltransferase activity (GO:0080043) belongs elsewhere:** This term is appropriate for **Group F (UGT78 family)** members such as Arabidopsis UGT78D1 and UGT78D2, which are experimentally characterized flavonol 3-O-glucosyltransferases recognizing quercetin and kaempferol (gachon2005plantsecondarymetabolism pages 4-5, lim2004aclassof pages 4-5). Some Group L anthocyanin/flavonoid GTs may also carry this activity. It should not be propagated onto Group G / UGT85 branches.

4. **Subfamilies where family-level propagation of quercetin 3-O-GT would be an over-annotation:** This includes essentially all branches outside the flavonoid-specific Group F and Group L clades, specifically including Group A (glucosinolate/hormone conjugation), Group D (diverse terpenoid/steroid/phenolic), Group E (monolignol/coumarin), Group G (cyanohydrin/cytokinin/diterpene), Group H (cytokinin N-GT/steviol modification), and all mammalian UGT1A/UGT2B branches.

---

### Evidence and Gaps

**Key citations supporting this analysis:**

- Gharabli & Welner (2024), *Front. Bioeng. Biotechnol.* — PSPG motif structure, sugar donor specificity, GT-B fold architecture in plant UGTs (gharabli2024thesugardonor pages 3-4, gharabli2024thesugardonor pages 1-3).
- Speeckaert et al. (2022), *Biology* — UGT72 family functional characterization, catalytic residues (His-19, Asp/Glu), monolignol and flavonoid substrates (speeckaert2022ugt72amajor pages 2-5, speeckaert2022ugt72amajor pages 5-8).
- Bowles et al. (2006), *Annu. Rev. Plant Biol.* — Comprehensive review of GT1 family acceptor substrates including hormones, secondary metabolites, cyanogenic glucosides; UGT85B1 in dhurrin biosynthesis; UGT85C2 in steviol glycoside biosynthesis (bowles2006glycosyltransferasesoflipophilic pages 6-7, bowles2006glycosyltransferasesoflipophilic pages 7-9, bowles2006glycosyltransferasesoflipophilic pages 9-10, bowles2006glycosyltransferasesoflipophilic pages 14-16, bowles2006glycosyltransferasesoflipophilic pages 16-17). PMID: 16669764.
- Gachon et al. (2005), *Trends Plant Sci.* — Phylogenetic group classification of plant UGTs (A–N), PSPG motif conservation, UGT85B1 in dhurrin metabolon (gachon2005plantsecondarymetabolism pages 3-4). PMID: 16213164.
- Lim & Bowles (2004), *EMBO J.* — Substrate diversity table, regioselectivity studies, multiple UGTs recognizing same substrates (lim2004aclassof pages 5-7, lim2004aclassof pages 3-4, lim2004aclassof pages 4-5). PMID: 15282543.
- Nielsen et al. (2008), *Phytochemistry* — UGT85B1 metabolon formation, cyanohydrin stabilization by glucosylation (nielsen2008metabolonformationin pages 1-2, nielsen2008metabolonformationin pages 2-3). PMID: 17959211.
- Zhou et al. (2021), *Appl. Microbiol. Biotechnol.* — UGT85C2 as rate-limiting enzyme in steviol glycoside biosynthesis, C13 glucosylation (zhou2021metabolicengineeringfor pages 8-10, zhou2021metabolicengineeringfor pages 7-8). PMID: 34245335.
- Rehman et al. (2018), *Sci. Rep.* — Brassica/Arabidopsis UGT classification into 14 groups, UGT85A1 in zeatin biosynthesis, KEGG pathway mapping (rehman2018comparativegenomicand pages 13-13, rehman2018comparativegenomicand pages 3-6). PMID: 29382866.
- Lethe et al. (2024), *Int. J. Mol. Sci.* — Cross-kingdom UGT structural comparison, human UGT1A1 vs. plant UGT71G1, catalytic His-22/Asp-121 dyad (lethe2024similaritiesinstructure pages 1-4, lethe2024similaritiesinstructure pages 4-5). PMID: 38474012.
- Mi et al. (2021), *Nucleic Acids Res.* — PANTHER v16, TreeGrafter propagation mechanism for GO annotations (mi2020pantherversion16 pages 9-10). PMID: 33290554.

**Explicit uncertainties and gaps:**

1. **No direct biochemical characterization of A0A2H4GSI3 (the specific representative member) was found.** The protein is annotated as UGT85A2 from *Nicotiana attenuata*, but no published in vitro substrate assays or in planta functional studies for this specific gene were located. Its function is inferred from phylogenetic placement within the UGT85A subfamily.

2. **UGT85A subfamily functional breadth remains incompletely characterized.** While UGT85A1 is linked to cytokinin (trans-zeatin) O-glucosylation and CsUGT85A2 from cucumber to cytokinin regulation, the *Nicotiana* UGT85A2 could potentially have diverged toward a different substrate class (e.g., defense-related terpenoid glycosylation). This requires experimental testing.

3. **The PANTHER family PTHR11926 boundary relative to the CAZy GT1 family was not computationally verified.** Whether PTHR11926 includes mammalian UGT1A/UGT2B members alongside plant UGTs, or is restricted to the plant clade, could not be confirmed from available sources. The family name "GLUCOSYL/GLUCURONOSYL TRANSFERASES" implies it spans both clades.

4. **Catalytic-residue conservation check (His-Asp dyad, PSPG motif) was not computationally run** on the specific SF1392 sequences due to tool limitations. However, there is no published evidence for pseudo-enzyme or catalytically dead members within the UGT85 clade.

5. **The source of the GO:0080043 annotation at this PANTHER node was not traced.** It is unclear whether this term was propagated from a mis-placed experimental annotation on a distant relative or was assigned computationally. Determining the provenance would help curators decide whether to remove or relocate it.

References

1. (gharabli2024thesugardonor pages 3-4): Hani Gharabli and Ditte Hededam Welner. The sugar donor specificity of plant family 1 glycosyltransferases. Frontiers in Bioengineering and Biotechnology, May 2024. URL: https://doi.org/10.3389/fbioe.2024.1396268, doi:10.3389/fbioe.2024.1396268. This article has 22 citations.

2. (speeckaert2022ugt72amajor pages 2-5): Nathanaël Speeckaert, Mondher El Jaziri, Marie Baucher, and Marc Behr. Ugt72, a major glycosyltransferase family for flavonoid and monolignol homeostasis in plants. Biology, 11:441, Mar 2022. URL: https://doi.org/10.3390/biology11030441, doi:10.3390/biology11030441. This article has 44 citations.

3. (gachon2005plantsecondarymetabolism pages 3-4): Claire M.M. Gachon, Mathilde Langlois-Meurinne, and Patrick Saindrenan. Plant secondary metabolism glycosyltransferases: the emerging functional analysis. Trends in plant science, 10 11:542-9, Nov 2005. URL: https://doi.org/10.1016/j.tplants.2005.09.007, doi:10.1016/j.tplants.2005.09.007. This article has 671 citations and is from a domain leading peer-reviewed journal.

4. (gharabli2024thesugardonor pages 1-3): Hani Gharabli and Ditte Hededam Welner. The sugar donor specificity of plant family 1 glycosyltransferases. Frontiers in Bioengineering and Biotechnology, May 2024. URL: https://doi.org/10.3389/fbioe.2024.1396268, doi:10.3389/fbioe.2024.1396268. This article has 22 citations.

5. (lethe2024similaritiesinstructure pages 4-5): Mary Caroline L. Lethe, Vincent Paris, Xiaoqiang Wang, and Clement T. Y. Chan. Similarities in structure and function of udp-glycosyltransferase homologs from human and plants. International Journal of Molecular Sciences, 25:2782, Feb 2024. URL: https://doi.org/10.3390/ijms25052782, doi:10.3390/ijms25052782. This article has 9 citations.

6. (rehman2018comparativegenomicand pages 13-13): Hafiz Mamoon Rehman, Muhammad Amjad Nawaz, Zahid Hussain Shah, Jutta Ludwig-Müller, Gyuhwa Chung, Muhammad Qadir Ahmad, Seung Hwan Yang, and Soo In Lee. Comparative genomic and transcriptomic analyses of family-1 udp glycosyltransferase in three brassica species and arabidopsis indicates stress-responsive regulation. Scientific Reports, Jan 2018. URL: https://doi.org/10.1038/s41598-018-19535-3, doi:10.1038/s41598-018-19535-3. This article has 158 citations and is from a peer-reviewed journal.

7. (lethe2024similaritiesinstructure pages 5-7): Mary Caroline L. Lethe, Vincent Paris, Xiaoqiang Wang, and Clement T. Y. Chan. Similarities in structure and function of udp-glycosyltransferase homologs from human and plants. International Journal of Molecular Sciences, 25:2782, Feb 2024. URL: https://doi.org/10.3390/ijms25052782, doi:10.3390/ijms25052782. This article has 9 citations.

8. (bowles2006glycosyltransferasesoflipophilic pages 6-7): Dianna Bowles, Eng-Kiat Lim, Brigitte Poppenberger, and Fabián E. Vaistij. Glycosyltransferases of lipophilic small molecules. Jun 2006. URL: https://doi.org/10.1146/annurev.arplant.57.032905.105429, doi:10.1146/annurev.arplant.57.032905.105429. This article has 655 citations and is from a domain leading peer-reviewed journal.

9. (lim2004aclassof pages 4-5): Eng-Kiat Lim and Dianna J Bowles. A class of plant glycosyltransferases involved in cellular homeostasis. The EMBO Journal, 23:2915-2922, Aug 2004. URL: https://doi.org/10.1038/sj.emboj.7600295, doi:10.1038/sj.emboj.7600295. This article has 353 citations.

10. (bowles2006glycosyltransferasesoflipophilic pages 9-10): Dianna Bowles, Eng-Kiat Lim, Brigitte Poppenberger, and Fabián E. Vaistij. Glycosyltransferases of lipophilic small molecules. Jun 2006. URL: https://doi.org/10.1146/annurev.arplant.57.032905.105429, doi:10.1146/annurev.arplant.57.032905.105429. This article has 655 citations and is from a domain leading peer-reviewed journal.

11. (gachon2005plantsecondarymetabolism pages 4-5): Claire M.M. Gachon, Mathilde Langlois-Meurinne, and Patrick Saindrenan. Plant secondary metabolism glycosyltransferases: the emerging functional analysis. Trends in plant science, 10 11:542-9, Nov 2005. URL: https://doi.org/10.1016/j.tplants.2005.09.007, doi:10.1016/j.tplants.2005.09.007. This article has 671 citations and is from a domain leading peer-reviewed journal.

12. (bowles2006glycosyltransferasesoflipophilic pages 16-17): Dianna Bowles, Eng-Kiat Lim, Brigitte Poppenberger, and Fabián E. Vaistij. Glycosyltransferases of lipophilic small molecules. Jun 2006. URL: https://doi.org/10.1146/annurev.arplant.57.032905.105429, doi:10.1146/annurev.arplant.57.032905.105429. This article has 655 citations and is from a domain leading peer-reviewed journal.

13. (gachon2005plantsecondarymetabolism pages 5-7): Claire M.M. Gachon, Mathilde Langlois-Meurinne, and Patrick Saindrenan. Plant secondary metabolism glycosyltransferases: the emerging functional analysis. Trends in plant science, 10 11:542-9, Nov 2005. URL: https://doi.org/10.1016/j.tplants.2005.09.007, doi:10.1016/j.tplants.2005.09.007. This article has 671 citations and is from a domain leading peer-reviewed journal.

14. (speeckaert2022ugt72amajor pages 5-8): Nathanaël Speeckaert, Mondher El Jaziri, Marie Baucher, and Marc Behr. Ugt72, a major glycosyltransferase family for flavonoid and monolignol homeostasis in plants. Biology, 11:441, Mar 2022. URL: https://doi.org/10.3390/biology11030441, doi:10.3390/biology11030441. This article has 44 citations.

15. (bowles2006glycosyltransferasesoflipophilic pages 7-9): Dianna Bowles, Eng-Kiat Lim, Brigitte Poppenberger, and Fabián E. Vaistij. Glycosyltransferases of lipophilic small molecules. Jun 2006. URL: https://doi.org/10.1146/annurev.arplant.57.032905.105429, doi:10.1146/annurev.arplant.57.032905.105429. This article has 655 citations and is from a domain leading peer-reviewed journal.

16. (lim2004aclassof pages 5-7): Eng-Kiat Lim and Dianna J Bowles. A class of plant glycosyltransferases involved in cellular homeostasis. The EMBO Journal, 23:2915-2922, Aug 2004. URL: https://doi.org/10.1038/sj.emboj.7600295, doi:10.1038/sj.emboj.7600295. This article has 353 citations.

17. (zhou2021metabolicengineeringfor pages 7-8): Xuan Zhou, Mengyue Gong, Xueqin Lv, Yanfeng Liu, Jianghua Li, Guocheng Du, and Long Liu. Metabolic engineering for the synthesis of steviol glycosides: current status and future prospects. Applied Microbiology and Biotechnology, 105:5367-5381, Jul 2021. URL: https://doi.org/10.1007/s00253-021-11419-3, doi:10.1007/s00253-021-11419-3. This article has 43 citations and is from a domain leading peer-reviewed journal.

18. (nielsen2008metabolonformationin pages 1-2): Kirsten Annette Nielsen, David B. Tattersall, Patrik Raymond Jones, and Birger Lindberg Møller. Metabolon formation in dhurrin biosynthesis. Phytochemistry, 69 1:88-98, Jan 2008. URL: https://doi.org/10.1016/j.phytochem.2007.06.033, doi:10.1016/j.phytochem.2007.06.033. This article has 181 citations and is from a peer-reviewed journal.

19. (nielsen2008metabolonformationin pages 2-3): Kirsten Annette Nielsen, David B. Tattersall, Patrik Raymond Jones, and Birger Lindberg Møller. Metabolon formation in dhurrin biosynthesis. Phytochemistry, 69 1:88-98, Jan 2008. URL: https://doi.org/10.1016/j.phytochem.2007.06.033, doi:10.1016/j.phytochem.2007.06.033. This article has 181 citations and is from a peer-reviewed journal.

20. (selmar2010biosynthesisofcyanogenic pages 22-25): Dirk Selmar. Biosynthesis of cyanogenic glycosides, glucosinolates and non‐protein amino acids. ArXiv, pages 92-181, Mar 2010. URL: https://doi.org/10.1002/9781444320503.ch3, doi:10.1002/9781444320503.ch3. This article has 51 citations.

21. (zhou2021metabolicengineeringfor pages 8-10): Xuan Zhou, Mengyue Gong, Xueqin Lv, Yanfeng Liu, Jianghua Li, Guocheng Du, and Long Liu. Metabolic engineering for the synthesis of steviol glycosides: current status and future prospects. Applied Microbiology and Biotechnology, 105:5367-5381, Jul 2021. URL: https://doi.org/10.1007/s00253-021-11419-3, doi:10.1007/s00253-021-11419-3. This article has 43 citations and is from a domain leading peer-reviewed journal.

22. (lim2004aclassof pages 3-4): Eng-Kiat Lim and Dianna J Bowles. A class of plant glycosyltransferases involved in cellular homeostasis. The EMBO Journal, 23:2915-2922, Aug 2004. URL: https://doi.org/10.1038/sj.emboj.7600295, doi:10.1038/sj.emboj.7600295. This article has 353 citations.

23. (lethe2024similaritiesinstructure pages 1-4): Mary Caroline L. Lethe, Vincent Paris, Xiaoqiang Wang, and Clement T. Y. Chan. Similarities in structure and function of udp-glycosyltransferase homologs from human and plants. International Journal of Molecular Sciences, 25:2782, Feb 2024. URL: https://doi.org/10.3390/ijms25052782, doi:10.3390/ijms25052782. This article has 9 citations.

24. (rehman2018comparativegenomicand pages 3-6): Hafiz Mamoon Rehman, Muhammad Amjad Nawaz, Zahid Hussain Shah, Jutta Ludwig-Müller, Gyuhwa Chung, Muhammad Qadir Ahmad, Seung Hwan Yang, and Soo In Lee. Comparative genomic and transcriptomic analyses of family-1 udp glycosyltransferase in three brassica species and arabidopsis indicates stress-responsive regulation. Scientific Reports, Jan 2018. URL: https://doi.org/10.1038/s41598-018-19535-3, doi:10.1038/s41598-018-19535-3. This article has 158 citations and is from a peer-reviewed journal.

25. (bowles2006glycosyltransferasesoflipophilic pages 14-16): Dianna Bowles, Eng-Kiat Lim, Brigitte Poppenberger, and Fabián E. Vaistij. Glycosyltransferases of lipophilic small molecules. Jun 2006. URL: https://doi.org/10.1146/annurev.arplant.57.032905.105429, doi:10.1146/annurev.arplant.57.032905.105429. This article has 655 citations and is from a domain leading peer-reviewed journal.

26. (mi2020pantherversion16 pages 9-10): Huaiyu Mi, Dustin Ebert, Anushya Muruganujan, Caitlin Mills, Laurent-Philippe Albou, Tremayne Mushayamaha, and Paul D Thomas. Panther version 16: a revised family classification, tree-based classification tool, enhancer regions and extensive api. Nucleic Acids Research, 49:D394-D403, Dec 2021. URL: https://doi.org/10.1093/nar/gkaa1106, doi:10.1093/nar/gkaa1106. This article has 1510 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](PTHR11926-function-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PTHR11926-function-falcon_artifacts/artifact-01.md)