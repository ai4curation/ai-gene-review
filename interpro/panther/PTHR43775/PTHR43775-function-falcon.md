---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-24T04:14:40.408259'
end_time: '2026-06-24T04:33:54.235685'
duration_seconds: 1153.83
template_file: templates/treegrafter_family_function.md
template_variables:
  family_id: PTHR43775
  family_name: FATTY ACID SYNTHASE
  subfamily: PTHR43775:SF51 INACTIVE PHENOLPHTHIOCEROL SYNTHESIS POLYKETIDE SYNTHASE
    TYPE I PKS1-RELATED
  gene_symbol: eryAIII
  uniprot: A4F7P1
  organism: SACEN
  taxon_label: SACEN
  propagated_term: fatty acid synthase activity (GO:0004312)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 35
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: PTHR43775-function-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
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

- **PANTHER family:** PTHR43775 — FATTY ACID SYNTHASE
- **Subfamily of interest:** PTHR43775:SF51 INACTIVE PHENOLPHTHIOCEROL SYNTHESIS POLYKETIDE SYNTHASE TYPE I PKS1-RELATED
- **Representative member:** eryAIII (A4F7P1), SACEN / SACEN
- **GO term currently propagated at/near this node:** fatty acid synthase activity (GO:0004312)

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
3. **Subfamily of interest.** Where does PTHR43775:SF51 INACTIVE PHENOLPHTHIOCEROL SYNTHESIS POLYKETIDE SYNTHASE TYPE I PKS1-RELATED sit — does it carry the
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

- **PANTHER family:** PTHR43775 — FATTY ACID SYNTHASE
- **Subfamily of interest:** PTHR43775:SF51 INACTIVE PHENOLPHTHIOCEROL SYNTHESIS POLYKETIDE SYNTHASE TYPE I PKS1-RELATED
- **Representative member:** eryAIII (A4F7P1), SACEN / SACEN
- **GO term currently propagated at/near this node:** fatty acid synthase activity (GO:0004312)

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
3. **Subfamily of interest.** Where does PTHR43775:SF51 INACTIVE PHENOLPHTHIOCEROL SYNTHESIS POLYKETIDE SYNTHASE TYPE I PKS1-RELATED sit — does it carry the
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


# PANTHER Family PTHR43775 (FATTY ACID SYNTHASE) — TreeGrafter Granularity Audit

## Family Function Summary

PANTHER family PTHR43775 encompasses the type I fatty acid synthase / polyketide synthase megasynthase superfamily, whose members share a conserved multidomain architecture built around three obligate catalytic domains: a ketosynthase (KS) domain that catalyzes decarboxylative Claisen condensation of an acyl thioester with a (methyl)malonyl extender unit, an acyltransferase (AT) domain that loads extender units, and an acyl carrier protein (ACP) domain that tethers biosynthetic intermediates via a phosphopantetheine arm (bon2022solutionstructureof pages 1-2, cane2010programmingoferythromycin pages 1-3). The KS domain retains a diagnostic active-site cysteine (e.g., Cys199 in DEBS KS) and a universally conserved pair of histidine residues (e.g., His334/His374 in DEBS KS5) that facilitate condensation (cane2010programmingoferythromycin pages 1-3). Additional accessory domains — ketoreductase (KR), dehydratase (DH), enoylreductase (ER) — control the degree of β-keto processing in each catalytic cycle (katja2015unusualhalogenationand pages 13-16, piech2020computationalandin pages 18-23). Despite sharing this core fold and catalytic mechanism, the family is profoundly heterogeneous in product outcome: animal type I fatty acid synthases (FAS) perform iterative fully-reducing cycles to produce long-chain saturated fatty acids, while type I polyketide synthases (PKS) — including bacterial modular PKS, mycobacterial iterative PKS, and fungal iterative PKS — use the same catalytic chemistry to produce structurally diverse polyketides with variable oxidation states and chain branching (lin2024thepolyketideto pages 1-2, katja2015unusualhalogenationand pages 13-16, piech2020computationalandin pages 18-23). This functional divergence means the family name "FATTY ACID SYNTHASE" and the currently propagated GO term GO:0004312 (fatty acid synthase activity) do not accurately describe the molecular function of most members.

## Subfamily Divergence Table

The following table enumerates the major functional subgroups within PTHR43775, their characterized representatives, catalytic status, and appropriate GO MF terms:

| Subgroup | Representative Members (PMID) | Molecular Function | Substrate / Specialization | Catalytic Residues Intact? | GO MF Term That Fits | Notes |
|---|---|---|---|---|---|---|
| Animal type I FAS | Human FASN; porcine FAS (domain architecture/PKS-FAS comparison in PMID unavailable here; structural/functional evidence in 2024 review and comparative analyses) (lin2024thepolyketideto pages 1-2, jenkekodama2005evolutionaryimplicationsof pages 5-6) | Fatty acid synthase activity | Acetyl-CoA + malonyl-CoA; iterative fully reducing synthesis of long-chain fatty acids | Yes; canonical KS Cys/His/His and AT Ser conserved in active FAS enzymes (cane2010programmingoferythromycin pages 1-3) | GO:0004312 fatty acid synthase activity | True FAS branch; safe target for GO:0004312, but not representative of the whole PTHR43775 family (lin2024thepolyketideto pages 1-2, jenkekodama2005evolutionaryimplicationsof pages 5-6) |
| Bacterial modular PKS (cis-AT) | eryAIII/DEBS3, DEBS1, DEBS2 from *Saccharopolyspora erythraea* (PMID: 20558741, 8356042) (tang2000formationoffunctional pages 1-3, cane2010programmingoferythromycin pages 1-3) | Polyketide synthase activity | Mainly methylmalonyl-CoA extender units; assembly-line biosynthesis of 6-deoxyerythronolide B/erythromycin precursor | Yes; active-site KS Cys plus conserved His pair (e.g. His334/His374 in DEBS KS5) and AT Ser retained (cane2010programmingoferythromycin pages 1-3) | GO:0016218 polyketide synthase activity | Non-iterative assembly-line PKS; eryAIII is catalytically active DEBS3, so GO:0004312 would misannotate this branch (tang2000formationoffunctional pages 1-3, cane2010programmingoferythromycin pages 1-3) |
| Mycobacterial modular PKS (PpsA-E) | PpsA, PpsB, PpsC, PpsD, PpsE from *Mycobacterium tuberculosis* / *M. bovis* BCG (PMID: 18784081, 32343668) (kruh2008anovelinteraction pages 6-6, kruh2008anovelinteraction pages 5-6, ramos2020revisitingtheexpression pages 1-2) | Polyketide synthase activity in PDIM/PGL backbone biosynthesis | Long-chain fatty acyl starter/intermediate plus malonyl-/methylmalonyl-derived extensions for phthiocerol/phenolphthiocerol | Yes overall; active PKS modules, though some modules omit certain reductive domains rather than losing core PKS catalysis (kruh2008anovelinteraction pages 6-6, kruh2008anovelinteraction pages 5-6) | GO:0016218 polyketide synthase activity | Specialized mycobacterial lipid PKSs; PpsA/PpsB lack DH/ER and preserve hydroxylated intermediates, whereas PpsC-E include DH/ER for saturated segments (kruh2008anovelinteraction pages 6-6) |
| Mycobacterial iterative PKS (MAS/Pks15/1) | MAS / mycocerosic-acid-synthase-like PKS from *Mycobacterium* spp. (PMID: 26954482); Pks15/1 (PMID: 19824599) (he2009cooperationbetweena pages 2-2, he2009cooperationbetweena pages 1-2, herbst2016mycocerosicacidsynthase pages 1-5, herbst2016mycocerosicacidsynthase pages 5-9) | Iterative polyketide synthase activity | MAS: iterative methylmalonyl-CoA-dependent branched lipid synthesis; Pks15/1: p-hydroxybenzoate-derived starter plus malonyl-CoA for phenolic glycolipid intermediates | Yes; Pks15/1 requires KS Cys-211 for starter loading; MAS retains full reducing PKS catalytic set including KS/AT/DH/ER/KR with ΨKR accessory domain (he2009cooperationbetweena pages 2-2, herbst2016mycocerosicacidsynthase pages 1-5) | GO:0016218 polyketide synthase activity | Iterative PKS branch; Pks15/1 shows relaxed iteration control, explaining product chain-length variability (he2009cooperationbetweena pages 1-2); not a fatty acid synthase branch |
| Fungal iterative type I PKS (HR-PKS/PR-PKS/NR-PKS) | Various fungal HR-PKS, PR-PKS, NR-PKS (class-level evidence) (piech2020computationalandin pages 23-28, piech2020computationalandin pages 18-23, jenkekodama2005evolutionaryimplicationsof pages 5-6) | Polyketide synthase activity | Usually malonyl-CoA-derived iterative polyketide biosynthesis; reduction pattern varies by subclass | Variable by domain set; HR-PKS retain reductive domains, NR-PKS lack KR/DH/ER as part of normal specialization rather than pseudogenization (piech2020computationalandin pages 23-28, piech2020computationalandin pages 18-23) | GO:0016218 polyketide synthase activity | Major divergent branch relative to animal FAS; phylogenetically related to modular PKS and not safely annotatable as fatty acid synthase (piech2020computationalandin pages 23-28, jenkekodama2005evolutionaryimplicationsof pages 5-6) |
| Animal FAS-like PKS (AFPK) | EcPKS1 and related animal FAS-like PKSs from sacoglossans/arthropods (PMID: 32467557; 2024 expansion study DOI 10.1038/s41467-023-44497-0) (lin2024thepolyketideto pages 1-2, torres2020animalbiosynthesisof pages 1-3) | Polyketide / specialized lipid synthase activity | Methylmalonyl-CoA-selective or specialized lipid/polyketide biosynthesis | Yes; active FAS-like PKS catalytic core retained (torres2020animalbiosynthesisof pages 1-3) | GO:0016218 polyketide synthase activity | Often misannotated as FAS because of FAS-like architecture; evolutionary bridge between animal FAS and PKS, but functionally not canonical fatty acid synthesis (lin2024thepolyketideto pages 1-2, torres2020animalbiosynthesisof pages 1-3) |
| Non-elongating KS0/KSQ modules | Loading/non-elongating modules from diverse PKS systems (class-level evidence) (tang2000formationoffunctional pages 1-3, katja2015unusualhalogenationand pages 13-16) | KSQ: decarboxylase-like starter-unit processing; KS0: structural/translocation scaffold rather than condensase | Starter-unit handling, decarboxylation, or non-elongating transfer | No for canonical KS condensation in KSQ; active-site Cys commonly replaced by Gln (KSQ); KS0 lacks elongating KS function (tang2000formationoffunctional pages 1-3, katja2015unusualhalogenationand pages 13-16) | None confidently family-wide; GO:0016831 carboxy-lyase activity may fit some KSQ cases | Functionally diverged/pseudo-enzymatic KS-derived modules; strongest example that any family-wide synthase GO term would over-annotate some branches (tang2000formationoffunctional pages 1-3, katja2015unusualhalogenationand pages 13-16) |
| Mycobacterial condensase Pks13 | Pks13 from *Mycobacterium tuberculosis* (PMID: 35729562) (bon2022solutionstructureof pages 1-2) | Condensase / polyketide-synthase-like chain condensation in mycolic acid biosynthesis | Two very long fatty acyl chains in final mycolic acid condensation step | Yes; active ACP/AT/KS core retained for condensation chemistry (bon2022solutionstructureof pages 1-2) | GO:0016218 polyketide synthase activity or a more specific condensase term if available | Specialized mycolic-acid pathway enzyme; structurally type I PKS-like but functionally distinct from canonical FAS and from many secondary-metabolite PKSs (bon2022solutionstructureof pages 1-2) |


*Table: This table summarizes the major functional branches within PANTHER family PTHR43775 and shows why a single molecular-function annotation is not appropriate across the family. It highlights the split between true fatty acid synthases, diverse active polyketide synthases, and non-elongating KS-derived modules.*

## Homogeneous vs. Heterogeneous Verdict

**This family is HETEROGENEOUS.** A single family-level GO MF term is **not safe** to propagate across PTHR43775.

The core conserved feature across all characterized members is the KS-catalyzed decarboxylative condensation reaction using an ACP-tethered intermediate and an AT-loaded extender unit. However, the products and biological roles diverge dramatically: animal FAS produces fully saturated fatty acids for primary membrane lipid metabolism, while bacterial modular PKS (e.g., DEBS) produces structurally complex polyketide antibiotics (cane2010programmingoferythromycin pages 1-3, cane2010programmingoferythromycin pages 1-1), mycobacterial PKS enzymes (e.g., MAS, PpsA–E, Pks15/1, Pks13) produce specialized virulence lipids (kruh2008anovelinteraction pages 6-6, he2009cooperationbetweena pages 2-2, herbst2016mycocerosicacidsynthase pages 1-5), fungal iterative PKS enzymes produce diverse secondary metabolites (piech2020computationalandin pages 23-28), and animal FAS-like PKS (AFPK) enzymes produce polyketides/specialized lipids that are frequently misannotated as FAS products (lin2024thepolyketideto pages 1-2, torres2020animalbiosynthesisof pages 1-3). Furthermore, some members harbor non-elongating KS domains (KS⁰/KS^Q) that have lost the condensation function entirely, serving as decarboxylases or structural scaffolds (tang2000formationoffunctional pages 1-3).

Propagating GO:0004312 (fatty acid synthase activity) across the entire family would **mis-annotate** the following branches:

- **Bacterial modular PKS branches** (including subfamily SF51, where the representative eryAIII/DEBS3 catalyzes polyketide chain elongation for erythromycin biosynthesis, not fatty acid synthesis) (tang2000formationoffunctional pages 1-3, cane2010programmingoferythromycin pages 1-3).
- **Mycobacterial PKS branches** (PpsA–E for PDIM/PGL biosynthesis, MAS for mycocerosic acid synthesis, Pks15/1 for phenolic glycolipid intermediates, Pks13 for mycolic acid condensation) (kruh2008anovelinteraction pages 6-6, he2009cooperationbetweena pages 2-2, herbst2016mycocerosicacidsynthase pages 1-5, bon2022solutionstructureof pages 1-2).
- **Fungal iterative type I PKS branches** (HR-PKS, NR-PKS, PR-PKS) (piech2020computationalandin pages 23-28).
- **Animal FAS-like PKS (AFPK) branches** (lin2024thepolyketideto pages 1-2, torres2020animalbiosynthesisof pages 1-3).
- **Non-elongating KS⁰/KS^Q modules** (tang2000formationoffunctional pages 1-3).

## Subfamily of Interest: PTHR43775:SF51

The subfamily PTHR43775:SF51 is named "INACTIVE PHENOLPHTHIOCEROL SYNTHESIS POLYKETIDE SYNTHASE TYPE I PKS1-RELATED," yet its listed representative member, eryAIII (UniProt A4F7P1, from *Saccharopolyspora erythraea*), encodes DEBS3 — the third and final polypeptide subunit of 6-deoxyerythronolide B synthase (DEBS). DEBS3 comprises modules 5 and 6 of the erythromycin PKS assembly line plus the C-terminal thioesterase (TE) domain that catalyzes macrolactonization to release the 14-membered ring macrolide 6-deoxyerythronolide B (tang2000formationoffunctional pages 1-3, cane2010programmingoferythromycin pages 1-3, cane2010programmingoferythromycin pages 1-1). Each module in DEBS3 contains fully active KS, AT, KR, and ACP domains that perform decarboxylative condensation with (2S)-methylmalonyl-CoA and ketoreduction (cane2010programmingoferythromycin pages 1-3). This is an **active modular polyketide synthase**, not an inactive pseudo-enzyme or a fatty acid synthase.

The "PKS1-RELATED" and "PHENOLPHTHIOCEROL SYNTHESIS" elements in the subfamily name reference mycobacterial PKS enzymes. Pks15/1 (from *M. tuberculosis*) is a catalytically active 6-domain iterative type I PKS that synthesizes p-hydroxyphenylalkanoate intermediates for phenolic glycolipid (PGL) biosynthesis (he2009cooperationbetweena pages 2-2, he2009cooperationbetweena pages 1-2). In PGL-producing mycobacterial strains, Pks15/1 functions as a single intact gene with KS, KR, DH, ER, AT, and ACP domains, and performs ~8–9 elongation cycles with malonyl-CoA, cooperating with the FadD22 initiation module (ramos2020revisitingtheexpression pages 2-3, he2009cooperationbetweena pages 2-2). In M. tuberculosis H37Rv, a frameshift splits this into separate pks15 and pks1 open reading frames, disrupting PGL production — this may be the source of the "INACTIVE" designation, though it represents a strain-specific inactivating mutation rather than a family-wide loss of function (ramos2020revisitingtheexpression pages 2-3, ramos2020revisitingtheexpression pages 1-2).

The SF51 subfamily thus appears to group bacterial modular/iterative type I PKS subunits from actinomycetes (erythromycin PKS) and mycobacteria (phenolphthiocerol pathway PKS) on the basis of KS domain homology, despite substantial differences in their modular organization and substrate specificity. Neither the "fatty acid synthase activity" (GO:0004312) term nor the "INACTIVE" qualifier is appropriate for the characterized representative.

## Granularity Leads for Curation

**Family-level GO MF term recommendation:** No single specific GO MF term is appropriate at the PTHR43775 family level. The most accurate family-level annotation would be a broad catalytic term reflecting the conserved KS-mediated condensation mechanism, such as **GO:0016747** (acyltransferase activity, transferring groups other than amino-acyl groups) or a parent term encompassing both FAS and PKS chemistry. However, such generic terms provide limited informational value.

**Subfamily-level recommendations:**

| Subfamily/Branch | Recommended GO MF Term | Notes |
|---|---|---|
| Animal type I FAS | GO:0004312 (fatty acid synthase activity) | Correct only for this branch |
| Bacterial modular PKS (incl. SF51/eryAIII) | GO:0016218 (polyketide synthase activity) | Currently misannotated as GO:0004312 |
| Mycobacterial PKS (PpsA–E, MAS, Pks15/1, Pks13) | GO:0016218 (polyketide synthase activity) | Specialized lipid PKS; more specific child terms may be appropriate |
| Fungal iterative PKS | GO:0016218 (polyketide synthase activity) | Includes HR-PKS, NR-PKS, PR-PKS subclasses |
| Animal FAS-like PKS (AFPK) | GO:0016218 (polyketide synthase activity) | These enzymes are frequently misannotated as FAS (lin2024thepolyketideto pages 1-2) |
| Non-elongating KS⁰/KS^Q modules | No synthase term; consider GO:0016831 (carboxy-lyase activity) for KS^Q | Pseudo-enzyme modules, condensation-inactive |

**Subfamilies for which the currently-propagated GO:0004312 is an over-annotation:**
- SF51 (INACTIVE PHENOLPHTHIOCEROL SYNTHESIS PKS TYPE I PKS1-RELATED) — representative eryAIII is a polyketide synthase, not a fatty acid synthase
- All other subfamilies containing bacterial modular PKS, mycobacterial PKS, fungal PKS, AFPK, and non-elongating KS modules

**Priority curation action:** The GO:0004312 annotation should be restricted to the animal/fungal type I FAS subfamilies only and should not be propagated from the PTHR43775 family root node.

## Evidence and Gaps

**Key citations:**
- Lin et al. (2024) *Nature Communications* 15, DOI:10.1038/s41467-023-44497-0 — Establishes evolutionary relationship between animal FAS and type I PKS via AFPKs; demonstrates frequent misannotation of FAS-like PKS enzymes (lin2024thepolyketideto pages 1-2).
- Cane (2010) *J Biol Chem* 285:27517–27523, PMID:20558741 — Definitive review of DEBS modular PKS organization, domain functions, and catalytic residues (cane2010programmingoferythromycin pages 1-3).
- Tang et al. (2000) *Chem Biol* 7:77–84 — Demonstrates eryAIII/DEBS3 encodes modules 5–6 of erythromycin PKS (tang2000formationoffunctional pages 1-3).
- He et al. (2009) *J Am Chem Soc* 131:16744–16750, PMID:19824599 — Characterizes Pks15/1 as active iterative type I PKS with FadD22 in PGL biosynthesis (he2009cooperationbetweena pages 2-2, he2009cooperationbetweena pages 1-2).
- Ramos et al. (2020) *PLoS ONE* 15:e0229700 — Details pks15/1 domain architecture (KS, KR, DH, ER, AT, ACP) and regulatory patterns (ramos2020revisitingtheexpression pages 2-3, ramos2020revisitingtheexpression pages 1-2).
- Herbst et al. (2016) *Nature* 531:533–537, PMID:26954482 — Crystal structure of MAS reveals reducing iterative PKS architecture distinct from FAS (herbst2016mycocerosicacidsynthase pages 1-5, herbst2016mycocerosicacidsynthase pages 5-9, herbst2016mycocerosicacidsynthase pages 9-12).
- Bon et al. (2022) *BMC Biol* 20, PMID:35729562 — Solution structure of Pks13 from M. tuberculosis, a PKS condensase for mycolic acid synthesis (bon2022solutionstructureof pages 1-2).
- Jenke-Kodama et al. (2005) *Mol Biol Evol* 22:2027–2039, PMID:16014872 — Comprehensive KS domain phylogeny showing FAS and PKS share evolutionary history but form distinct functional clades (jenkekodama2005evolutionaryimplicationsof pages 5-6, jenkekodama2005evolutionaryimplicationsof pages 1-1, jenkekodama2005evolutionaryimplicationsof pages 4-5).
- Kruh et al. (2008) *J Biol Chem* 283:31719–31725, PMID:18784081 — PpsB/PpsD domain architecture and FAS-II/PDIM pathway interaction (kruh2008anovelinteraction pages 6-6, kruh2008anovelinteraction pages 5-6).
- Grininger (2020) *PNAS* 117:8680–8682 — Evolutionary role of iterative modules in PKS evolution.
- Torres et al. (2020) *Nature Communications* 11, PMID:32467557 — Biochemical characterization of EcPKS1 as methylmalonyl-CoA–selective animal FAS-like PKS (torres2020animalbiosynthesisof pages 1-3).

**Explicit uncertainties:**
1. The precise composition of PTHR43775 subfamilies was not directly verifiable from the PANTHER database API during this analysis. The subfamily boundaries and which specific sequences fall into SF51 versus other subfamilies could not be confirmed computationally.
2. The "INACTIVE" designation in SF51's name could not be traced to a specific curation event. It may derive from domain-level inactivity predictions (e.g., inactive KR or DH domains in some Pps modules) rather than whole-protein inactivation. Alternatively, it may reflect the pks15/1 frameshift in M. tuberculosis H37Rv.
3. The placement of eryAIII (A4F7P1) as the representative of a subfamily named after phenolphthiocerol synthesis PKS is surprising and may indicate that sequence-level similarity at the KS domain groups these actinomycete modular PKS subunits together despite functional divergence. A catalytic residue alignment between eryAIII KS domains and mycobacterial Pks15/1 KS would clarify whether the "INACTIVE" label applies to the representative.
4. No direct InterPro/Pfam architecture query was performed for A4F7P1 during this analysis (web-only resource). The expected domain architecture for DEBS3 is: [KS5–AT5–KR5–ACP5]–[KS6–AT6–KR6–ACP6–TE], all domains catalytically active.
5. GO:0016218 (polyketide synthase activity) is the most appropriate general term for PKS branches, but more specific child terms may exist or be needed for iterative versus modular PKS and for specific substrate classes.

References

1. (bon2022solutionstructureof pages 1-2): Cécile Bon, Stéphanie Cabantous, Sylviane Julien, Valérie Guillet, Christian Chalut, Julie Rima, Yoann Brison, Wladimir Malaga, Angelique Sanchez-Dafun, Sabine Gavalda, Annaïk Quémard, Julien Marcoux, Geoffrey S. Waldo, Christophe Guilhot, and Lionel Mourey. Solution structure of the type i polyketide synthase pks13 from mycobacterium tuberculosis. BMC Biology, Jun 2022. URL: https://doi.org/10.1186/s12915-022-01337-9, doi:10.1186/s12915-022-01337-9. This article has 17 citations and is from a domain leading peer-reviewed journal.

2. (cane2010programmingoferythromycin pages 1-3): David E. Cane. Programming of erythromycin biosynthesis by a modular polyketide synthase. Journal of Biological Chemistry, 285:27517-27523, Sep 2010. URL: https://doi.org/10.1074/jbc.r110.144618, doi:10.1074/jbc.r110.144618. This article has 131 citations and is from a domain leading peer-reviewed journal.

3. (katja2015unusualhalogenationand pages 13-16): Katja Jensen. Unusual halogenation and chain cleavage reactions in bacterial polyketide and peptide biosynthesis. ArXiv, 2015. URL: https://doi.org/10.3929/ethz-a-010412088, doi:10.3929/ethz-a-010412088. This article has 0 citations.

4. (piech2020computationalandin pages 18-23): Oliver Piech. Computational and in vitro study of isolated domains from fungal polyketide synthases. ArXiv, Jan 2020. URL: https://doi.org/10.15488/9866, doi:10.15488/9866. This article has 2 citations.

5. (lin2024thepolyketideto pages 1-2): Zhenjian Lin, Feng Li, Patrick J. Krug, and Eric W. Schmidt. The polyketide to fatty acid transition in the evolution of animal lipid metabolism. Nature Communications, Jan 2024. URL: https://doi.org/10.1038/s41467-023-44497-0, doi:10.1038/s41467-023-44497-0. This article has 23 citations and is from a highest quality peer-reviewed journal.

6. (jenkekodama2005evolutionaryimplicationsof pages 5-6): Holger Jenke-Kodama, Axel Sandmann, Rolf Müller, and Elke Dittmann. Evolutionary implications of bacterial polyketide synthases. Molecular biology and evolution, 22 10:2027-39, Oct 2005. URL: https://doi.org/10.1093/molbev/msi193, doi:10.1093/molbev/msi193. This article has 451 citations and is from a highest quality peer-reviewed journal.

7. (tang2000formationoffunctional pages 1-3): Li Tang, Hong Fu, and Robert McDaniel. Formation of functional heterologous complexes using subunits from the picromycin, erythromycin and oleandomycin polyketide synthases. Chemistry & biology, 7 2:77-84, Feb 2000. URL: https://doi.org/10.1016/s1074-5521(00)00073-9, doi:10.1016/s1074-5521(00)00073-9. This article has 125 citations.

8. (kruh2008anovelinteraction pages 6-6): Nicole A. Kruh, Janine G. Borgaro, Béla P. Ruzsicska, Hua Xu, and Peter J. Tonge. A novel interaction linking the fas-ii and phthiocerol dimycocerosate (pdim) biosynthetic pathways*. Journal of Biological Chemistry, 283:31719-31725, Nov 2008. URL: https://doi.org/10.1074/jbc.m802169200, doi:10.1074/jbc.m802169200. This article has 24 citations and is from a domain leading peer-reviewed journal.

9. (kruh2008anovelinteraction pages 5-6): Nicole A. Kruh, Janine G. Borgaro, Béla P. Ruzsicska, Hua Xu, and Peter J. Tonge. A novel interaction linking the fas-ii and phthiocerol dimycocerosate (pdim) biosynthetic pathways*. Journal of Biological Chemistry, 283:31719-31725, Nov 2008. URL: https://doi.org/10.1074/jbc.m802169200, doi:10.1074/jbc.m802169200. This article has 24 citations and is from a domain leading peer-reviewed journal.

10. (ramos2020revisitingtheexpression pages 1-2): Beatriz Ramos, Stephen V. Gordon, and Mónica V. Cunha. Revisiting the expression signature of pks15/1 unveils regulatory patterns controlling phenolphtiocerol and phenolglycolipid production in pathogenic mycobacteria. PLOS ONE, 15:e0229700, May 2020. URL: https://doi.org/10.1371/journal.pone.0229700, doi:10.1371/journal.pone.0229700. This article has 14 citations and is from a peer-reviewed journal.

11. (he2009cooperationbetweena pages 2-2): Weiguo He, Clifford E. Soll, Sivagami Sundaram Chavadi, Guangtao Zhang, J. David Warren, and Luis E. N. Quadri. Cooperation between a coenzyme a-independent stand-alone initiation module and an iterative type i polyketide synthase during synthesis of mycobacterial phenolic glycolipids. Journal of the American Chemical Society, 131:16744-16750, Oct 2009. URL: https://doi.org/10.1021/ja904792q, doi:10.1021/ja904792q. This article has 28 citations and is from a highest quality peer-reviewed journal.

12. (he2009cooperationbetweena pages 1-2): Weiguo He, Clifford E. Soll, Sivagami Sundaram Chavadi, Guangtao Zhang, J. David Warren, and Luis E. N. Quadri. Cooperation between a coenzyme a-independent stand-alone initiation module and an iterative type i polyketide synthase during synthesis of mycobacterial phenolic glycolipids. Journal of the American Chemical Society, 131:16744-16750, Oct 2009. URL: https://doi.org/10.1021/ja904792q, doi:10.1021/ja904792q. This article has 28 citations and is from a highest quality peer-reviewed journal.

13. (herbst2016mycocerosicacidsynthase pages 1-5): Dominik A. Herbst, Roman P. Jakob, Franziska Zähringer, and Timm Maier. Mycocerosic acid synthase exemplifies the architecture of reducing polyketide synthases. Nature, 531:533-537, Mar 2016. URL: https://doi.org/10.1038/nature16993, doi:10.1038/nature16993. This article has 104 citations and is from a highest quality peer-reviewed journal.

14. (herbst2016mycocerosicacidsynthase pages 5-9): Dominik A. Herbst, Roman P. Jakob, Franziska Zähringer, and Timm Maier. Mycocerosic acid synthase exemplifies the architecture of reducing polyketide synthases. Nature, 531:533-537, Mar 2016. URL: https://doi.org/10.1038/nature16993, doi:10.1038/nature16993. This article has 104 citations and is from a highest quality peer-reviewed journal.

15. (piech2020computationalandin pages 23-28): Oliver Piech. Computational and in vitro study of isolated domains from fungal polyketide synthases. ArXiv, Jan 2020. URL: https://doi.org/10.15488/9866, doi:10.15488/9866. This article has 2 citations.

16. (torres2020animalbiosynthesisof pages 1-3): Joshua P. Torres, Zhenjian Lin, Jaclyn M. Winter, Patrick J. Krug, and Eric W. Schmidt. Animal biosynthesis of complex polyketides in a photosynthetic partnership. Nature Communications, Sep 2020. URL: https://doi.org/10.1038/s41467-020-16376-5, doi:10.1038/s41467-020-16376-5. This article has 73 citations and is from a highest quality peer-reviewed journal.

17. (cane2010programmingoferythromycin pages 1-1): David E. Cane. Programming of erythromycin biosynthesis by a modular polyketide synthase. Journal of Biological Chemistry, 285:27517-27523, Sep 2010. URL: https://doi.org/10.1074/jbc.r110.144618, doi:10.1074/jbc.r110.144618. This article has 131 citations and is from a domain leading peer-reviewed journal.

18. (ramos2020revisitingtheexpression pages 2-3): Beatriz Ramos, Stephen V. Gordon, and Mónica V. Cunha. Revisiting the expression signature of pks15/1 unveils regulatory patterns controlling phenolphtiocerol and phenolglycolipid production in pathogenic mycobacteria. PLOS ONE, 15:e0229700, May 2020. URL: https://doi.org/10.1371/journal.pone.0229700, doi:10.1371/journal.pone.0229700. This article has 14 citations and is from a peer-reviewed journal.

19. (herbst2016mycocerosicacidsynthase pages 9-12): Dominik A. Herbst, Roman P. Jakob, Franziska Zähringer, and Timm Maier. Mycocerosic acid synthase exemplifies the architecture of reducing polyketide synthases. Nature, 531:533-537, Mar 2016. URL: https://doi.org/10.1038/nature16993, doi:10.1038/nature16993. This article has 104 citations and is from a highest quality peer-reviewed journal.

20. (jenkekodama2005evolutionaryimplicationsof pages 1-1): Holger Jenke-Kodama, Axel Sandmann, Rolf Müller, and Elke Dittmann. Evolutionary implications of bacterial polyketide synthases. Molecular biology and evolution, 22 10:2027-39, Oct 2005. URL: https://doi.org/10.1093/molbev/msi193, doi:10.1093/molbev/msi193. This article has 451 citations and is from a highest quality peer-reviewed journal.

21. (jenkekodama2005evolutionaryimplicationsof pages 4-5): Holger Jenke-Kodama, Axel Sandmann, Rolf Müller, and Elke Dittmann. Evolutionary implications of bacterial polyketide synthases. Molecular biology and evolution, 22 10:2027-39, Oct 2005. URL: https://doi.org/10.1093/molbev/msi193, doi:10.1093/molbev/msi193. This article has 451 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](PTHR43775-function-falcon_artifacts/artifact-00.md)