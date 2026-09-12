---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-24T04:14:40.897533'
end_time: '2026-06-24T04:36:57.308099'
duration_seconds: 1336.41
template_file: templates/treegrafter_family_function.md
template_variables:
  family_id: PTHR11571
  family_name: GLUTATHIONE S-TRANSFERASE
  subfamily: PTHR11571:SF150 GLUTATHIONE S-TRANSFERASE
  gene_symbol: OCTS1
  uniprot: P27013
  organism: OCTVU
  taxon_label: OCTVU
  propagated_term: glutathione transferase activity (GO:0004364)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 39
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: PTHR11571-function-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PTHR11571-function-falcon_artifacts/artifact-01.md
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

- **PANTHER family:** PTHR11571 — GLUTATHIONE S-TRANSFERASE
- **Subfamily of interest:** PTHR11571:SF150 GLUTATHIONE S-TRANSFERASE
- **Representative member:** OCTS1 (P27013), OCTVU / OCTVU
- **GO term currently propagated at/near this node:** glutathione transferase activity (GO:0004364)

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
3. **Subfamily of interest.** Where does PTHR11571:SF150 GLUTATHIONE S-TRANSFERASE sit — does it carry the
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

- **PANTHER family:** PTHR11571 — GLUTATHIONE S-TRANSFERASE
- **Subfamily of interest:** PTHR11571:SF150 GLUTATHIONE S-TRANSFERASE
- **Representative member:** OCTS1 (P27013), OCTVU / OCTVU
- **GO term currently propagated at/near this node:** glutathione transferase activity (GO:0004364)

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
3. **Subfamily of interest.** Where does PTHR11571:SF150 GLUTATHIONE S-TRANSFERASE sit — does it carry the
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


# PANTHER Family PTHR11571 — Glutathione S-Transferase: TreeGrafter Granularity Audit

## Family Function Summary

The glutathione S-transferase (GST) superfamily (PTHR11571) is defined by a conserved two-domain fold architecture: an N-terminal domain adopting a thioredoxin-like topology (β1α1β2α2β3β4α3) that provides the glutathione (GSH) binding site (G-site), and an α-helical C-terminal domain that contributes the hydrophobic substrate-binding pocket (H-site) (sheehan2001structurefunctionand pages 4-6, vaish2020glutathionestransferasea pages 10-12, sheehan2001structurefunctionand pages 2-3). The most broadly conserved feature across the family is glutathione binding and activation — all characterized GST-fold proteins interact with GSH through the G-site, lowering the pKa of the GSH thiol from ~9.0 to ~6–7 (sheehan2001structurefunctionand pages 2-3). However, the catalytic residue mediating this activation varies by class: Alpha, Mu, Pi, and Sigma classes employ a conserved tyrosine; Theta, Zeta, Phi, and Tau classes use a serine; and Omega, Lambda, DHAR, CLIC, and other Cys-GST classes use a cysteine residue (vaish2020glutathionestransferasea pages 10-12, vaish2020glutathionestransferasea pages 1-2, micic2024overlookedandmisunderstood pages 3-4, perez2024sigmaclassglutathionetransferases pages 2-4). This mechanistic heterogeneity is accompanied by profound functional divergence — not all members of this fold superfamily catalyze glutathione conjugation reactions, and several branches have been neofunctionalized into oxidoreductases, isomerases, structural proteins, and ion channel-associated proteins (pearson2005phylogeniesofglutathione pages 6-9, sheehan2001structurefunctionand pages 7-9, sheehan2001structurefunctionand pages 9-10). The canonical "glutathione transferase activity" (EC 2.5.1.18; GO:0004364), defined as the nucleophilic conjugation of GSH to electrophilic substrates, is therefore not a safe term to propagate across the entire family.

## Subfamily Divergence Table

The following table enumerates the major functional subgroups within PTHR11571 and how they differ in molecular function, catalytic mechanism, and GO annotation fitness:

| Subgroup/Class | Representative member(s) (citation) | Molecular function | Substrate or specialization | Catalytic residue type and intact? | GO MF term that fits | Notes (pseudo-enzyme, neofunctionalization, etc.) |
|---|---|---|---|---|---|---|
| Alpha class | Mammalian Alpha GSTs; human GSTA1-1 discussed as class exemplar (sheehan2001structurefunctionand pages 4-6, sheehan2001structurefunctionand pages 3-4, sheehan2001structurefunctionand pages 7-9) | Canonical glutathione conjugation; some members also catalyze steroid isomerization | Broad xenobiotic/electrophile detoxification; steroid isomerase side activity | **Tyr-type** G-site residue intact | glutathione transferase activity (GO:0004364) | Canonical cytosolic GST architecture; good fit for family name but not for all GST-like branches |
| Mu class | Mammalian Mu GSTs; Fasciola gigantica FgGST1 as characterized Mu-class example (sheehan2001structurefunctionand pages 4-6, sheehan2001structurefunctionand pages 7-9) | Canonical glutathione conjugation | Broad detoxification of electrophiles; also peroxidase activity on lipid peroxidation products | **Tyr-type** intact | glutathione transferase activity (GO:0004364) | Typical dimeric cytosolic GST with broad substrate promiscuity |
| Pi class | Mammalian Pi GSTs / placental Pi GST referenced structurally (sheehan2001structurefunctionand pages 4-6, sheehan2001structurefunctionand pages 3-4, sheehan2001structurefunctionand pages 7-9) | Canonical glutathione conjugation; some members catalyze isomerization reactions | Electrophilic xenobiotics; retinoic-acid-related isomerization reported for GSTP1-1 | **Tyr-type** intact | glutathione transferase activity (GO:0004364) | Canonical GST branch; often used as archetypal cytosolic GST |
| Sigma class (enzymatic) | Hematopoietic prostaglandin D synthase / mammalian Sigma GSTs; helminth GSTσ; squid GSTσ (sheehan2001structurefunctionand pages 9-10, perez2024sigmaclassglutathionetransferases pages 4-5, perez2024sigmaclassglutathionetransferases pages 10-11) | Glutathione-dependent transferase and prostaglandin synthase/isomerase activities | PGH2 to PGD2/PGE2/PGF2α in some taxa; detoxification and ligand binding also reported | **Tyr-type** generally intact | glutathione transferase activity (GO:0004364); prostaglandin-D synthase activity where demonstrated | Clear functional expansion beyond generic conjugation; still enzymatic GSTs |
| Sigma class / S-crystallin (cephalopod) | Octopus S-crystallins OctS1/OctS2/OctS3; P27013/OCTS1 (chuang1999homologymodelingof pages 1-2, tan2016structureofa pages 2-4) | Primarily structural lens/refractive protein; residual vestigial GST activity in some forms | Lens transparency/stability; strong GSH binding; collapsed H-site disfavors classic substrates | **Tyr-type ancestry but catalytic architecture disrupted/mutated** | structural constituent of eye lens (GO:0005212) | Neofunctionalized GST-fold protein derived from sigma-class GST; family-level GO:0004364 would over-annotate this branch |
| Theta class | Theta GSTs as conserved Ser-GST branch (sheehan2001structurefunctionand pages 2-3, sheehan2001structurefunctionand pages 10-10, perez2024sigmaclassglutathionetransferases pages 2-4) | Glutathione conjugation | Distinct substrate spectrum from Alpha/Mu/Pi; older GST lineage | **Ser-type** intact | glutathione transferase activity (GO:0004364) | Structurally divergent from Alpha/Mu/Pi; still bona fide GST enzymes |
| Zeta class | Zeta GST / maleylacetoacetate isomerase (sheehan2001structurefunctionand pages 9-10, vaish2020glutathionestransferasea pages 10-12, perez2024sigmaclassglutathionetransferases pages 2-4) | Isomerase in tyrosine catabolism; low activity on standard GST substrates | Maleylacetoacetate/maleylacetone pathway intermediates | **Ser-type** intact | maleylacetoacetate isomerase activity | Specialized metabolic enzyme; classic GST term is too coarse if specific activity is known |
| Phi/Tau class (plant-specific) | Plant GSTF/GSTU classes; broad plant exemplars summarized in recent review (vaish2020glutathionestransferasea pages 10-12, micic2024overlookedandmisunderstood pages 3-4) | Glutathione conjugation | Plant stress metabolites, xenobiotics, herbicides; also transport-associated roles in specialized metabolism | **Ser-type** intact | glutathione transferase activity (GO:0004364) | Large plant expansions with high substrate promiscuity; many remain bona fide transferases |
| Omega class | Human GSTO1-1 / Omega GSTs (sheehan2001structurefunctionand pages 7-9, menon2015thebiologicalroles pages 55-58) | GSH-dependent thiol transferase / glutaredoxin-like redox chemistry | Deglutathionylation and thiol-disulfide exchange rather than classic electrophile conjugation | **Cys-type** intact | thiol transferase activity | Atypical GSTs with minimal resemblance to classical detoxifying GST catalysis; family-level GO:0004364 can over-annotate |
| DHAR/Lambda (plant) | Arabidopsis DHAR2; plant Lambda/Cys-GST class summaries (vaish2020glutathionestransferasea pages 10-12, micic2024overlookedandmisunderstood pages 3-4) | Dehydroascorbate reductase / deglutathionylation-type chemistry | Reduction of dehydroascorbate; glutathione-dependent antioxidant recycling | **Cys-type** intact and essential | dehydroascorbate reductase activity | Cys-GSTs mechanistically distinct from conjugating GSTs; poor fit to GO:0004364 |
| CLIC proteins | CLIC1/3/4 (khoury2025aninvitro pages 1-2, khoury2025aninvitro pages 15-15, khoury2025aninvitro pages 13-15, khoury2025aninvitro pages 9-12) | Oxidoreductase / glutaredoxin-like glutathionylation chemistry; membrane-associated ion-channel-like role | Redox-regulated protein glutathionylation/deglutathionylation; trafficking/channel-associated functions | **Cys-type** intact in active-site thioredoxin-like motif | oxidoreductase activity, acting on sulfhydryl groups | GST-superfamily fold but not classical GST conjugases; strong over-annotation risk for GO:0004364 |
| Kappa class | Mitochondrial/peroxisomal Kappa GSTs (sheehan2001structurefunctionand pages 9-10) | Glutathione-dependent enzymatic activity in organelles | Organellar detoxification/redox metabolism | Catalytic residue type not resolved in retrieved context; GST-active branch retained | glutathione transferase activity (GO:0004364) | Distinct class lacking some canonical cytosolic motifs; still generally treated as enzymatic GST |


*Table: This table summarizes the major functional subgroups within the GST superfamily and highlights where classical glutathione transferase activity is retained versus where it has specialized or been lost. It is useful for judging whether family-level propagation of GO:0004364 would mis-annotate divergent branches such as S-crystallins, Omega GSTs, DHAR/Lambda proteins, and CLICs.*

## Subfamily of Interest: PTHR11571:SF150 (S-Crystallin / OCTS1, P27013)

The representative member of PTHR11571:SF150, designated OCTS1 (UniProt P27013, Octopus vulgaris S-crystallin 1), is a cephalopod lens structural protein that has been extensively characterized as a neofunctionalized sigma-class GST derivative. Homology modeling and crystallographic studies demonstrate that S-crystallin shares 41% amino acid sequence identity with cephalopod sigma-class GST (GST-σ) and retains the canonical two-domain GST fold with a functional GSH-binding site (chuang1999homologymodelingof pages 1-2, tan2016structureofa pages 2-4). However, its GST enzymatic activity is vestigial: the specific activity of purified S-crystallin is approximately 0.10 μmol/min/μg, compared with 100–200 μmol/min/μg for mammalian GSTs (chiou1995octopusscrystallinswith pages 4-5), and its catalytic rate constant (k_cat = 0.24 s⁻¹) is approximately 1/700th that of octopus GST-σ (k_cat = 173.6 s⁻¹) (tan2016structureofa pages 2-4).

This dramatic reduction in catalytic activity is explained by specific structural changes: key mutations at residues 100, 104, and 108 (Leu100, Met104, Gln108 in S-crystallin vs. Phe98, Val102, Phe106 in GST-σ), plus an 11-amino acid insertion between α4 and α5 helices, collapse the substrate-binding pocket and disfavor binding of electrophilic substrates such as CDNB (tan2016structureofa pages 2-4, chuang1999homologymodelingof pages 1-2). Of the 26 invariant residues considered essential for preserving the GST structural fold and function, five have been mutated or deleted in octopus S-crystallins (chiou1995octopusscrystallinswith pages 7-8). Conversely, S-crystallin shows 43-fold tighter GSH binding than GST-σ, and this GSH binding serves a structural role — preventing protein aggregation and protecting against cataract formation in the lens (tan2016structureofa pages 2-4, tan2016structureofa pages 5-6).

Phylogenetically, OctS1 diverged early from the S-crystallin lineage, showing only 67–68% amino acid identity with OctS2 and OctS3 (chiou1995octopusscrystallinswith pages 5-5, chiou1995octopusscrystallinswith pages 4-5). The S-crystallin multigene family arose through gene duplication from an ancestral sigma-class GST, with subsequent mutational substitutions driving the transition from enzymatic function to structural lens protein (chiou1995octopusscrystallinswith pages 1-2, tan2016structureofa pages 6-7). Recent single-cell transcriptomic work in cephalopods confirms S-crystallins as cephalopod-specific GST-σ-derived lens proteins (gavriouchkina2025asinglecellatlas pages 5-6).

**Characterized exemplars:** OctS1 (P27013, *O. vulgaris*), OctS2, OctS3, OL1, OL2 (*O. dofleini*), SL11, SL20 (squid *Loligo*) (chiou1995octopusscrystallinswith pages 4-5, chiou1995octopusscrystallinswith pages 5-5).

**Conclusion for SF150:** The GO term glutathione transferase activity (GO:0004364) is an over-annotation for this subfamily. The appropriate term is **structural constituent of eye lens (GO:0005212)**.

## Homogeneous vs. Heterogeneous Verdict

**The GST superfamily (PTHR11571) is HETEROGENEOUS.** A single family-level GO molecular function term of glutathione transferase activity (GO:0004364) is **not safe to propagate** across all descendants of this family. Propagation of GO:0004364 would mis-annotate at least the following branches:

1. **S-crystallins** (including SF150): neofunctionalized structural lens proteins with vestigial/negligible GST activity (chuang1999homologymodelingof pages 1-2, tan2016structureofa pages 2-4).
2. **Omega-class GSTs**: described as "atypical GSTs with minimal functional resemblance" to classical GSTs; they function primarily as GSH-dependent thiol transferases / glutaredoxin-like enzymes (menon2015thebiologicalroles pages 55-58, sheehan2001structurefunctionand pages 7-9).
3. **CLIC proteins**: GST-superfamily members that function as oxidoreductases and membrane-associated ion channels, not as glutathione conjugases (khoury2025aninvitro pages 1-2, khoury2025aninvitro pages 15-15, khoury2025aninvitro pages 9-12).
4. **DHAR/Lambda/Cys-GSTs**: catalyze deglutathionylation (removing GSH from conjugates) and dehydroascorbate reduction, mechanistically distinct from GSH conjugation (vaish2020glutathionestransferasea pages 10-12, micic2024overlookedandmisunderstood pages 3-4).
5. **Zeta-class GSTs**: primary activity is maleylacetoacetate isomerase in tyrosine catabolism, with low activity on standard GST substrates (pearson2005phylogeniesofglutathione pages 6-9, sheehan2001structurefunctionand pages 9-10).

## Granularity Leads for Curation

> PTHR11571 (glutathione S-transferase family) is **functionally heterogeneous**: a single family-level molecular function annotation of **glutathione transferase activity (GO:0004364)** is **not safe to propagate** across the full family, because the conserved feature across GST-like proteins is better described as a shared GST fold with **glutathione binding/activation**, while multiple branches have diverged away from classical GSH-conjugating transferase chemistry (sheehan2001structurefunctionand pages 4-6, sheehan2001structurefunctionand pages 2-3, pearson2005phylogeniesofglutathione pages 6-9, sheehan2001structurefunctionand pages 7-9, perez2024sigmaclassglutathionetransferases pages 2-4).
>
> Family-wide propagation of GO:0004364 would mis-annotate at least these branches: **S-crystallins** including **PTHR11571:SF150 / OCTS1 (P27013)**, which are primarily structural lens proteins derived from sigma-class GSTs; **Omega-class GSTs**, which are glutaredoxin-like/thiol-transfer enzymes rather than canonical conjugating GSTs; **CLIC proteins**, which are GST-superfamily oxidoreductases with channel-associated moonlighting roles; **DHAR/Lambda Cys-GSTs**, which function in dehydroascorbate reduction/deglutathionylation; and **Zeta-class GSTs**, whose defining activity is **maleylacetoacetate isomerase** in tyrosine catabolism (tan2016structureofa pages 2-4, sheehan2001structurefunctionand pages 9-10, vaish2020glutathionestransferasea pages 10-12, khoury2025aninvitro pages 1-2, khoury2025aninvitro pages 15-15, menon2015thebiologicalroles pages 55-58, chuang1999homologymodelingof pages 1-2).
>
> For curation, the best **family-level** lead is **glutathione binding (GO:0043295)** as the most broadly conserved property supported by the shared G-site architecture, whereas **subfamily-level** MF terms should remain specific: **GO:0004364** for canonical conjugating branches such as **Alpha/Mu/Pi/Theta/Sigma(enzymatic)/Phi/Tau**; **structural constituent of eye lens (GO:0005212)** for **S-crystallins**; **thiol transferase activity** for **Omega**; **dehydroascorbate reductase activity** for **DHAR**; an **oxidoreductase, acting on sulfhydryl groups** term for **CLICs**; and an **isomerase** term for **Zeta** (micic2024overlookedandmisunderstood pages 3-4, sheehan2001structurefunctionand pages 7-9, sheehan2001structurefunctionand pages 9-10, vaish2020glutathionestransferasea pages 10-12, perez2024sigmaclassglutathionetransferases pages 4-5, tan2016structureofa pages 5-6, khoury2025aninvitro pages 1-2, khoury2025aninvitro pages 9-12).
>
> The subfamily of interest, **PTHR11571:SF150**, is a **clear over-annotation case**: **OctS1/OCTS1** is a cephalopod **S-crystallin** with only vestigial GST activity, a remodeled/collapsed substrate-binding pocket, and a primary role as a **lens-refractive structural protein**, so assigning **GO:0004364** at this node would overstate the conserved function of that branch (chuang1999homologymodelingof pages 1-2, tan2016structureofa pages 2-4, tan2016structureofa pages 5-6).


*Blockquote: This blockquote summarizes the annotation granularity audit for PTHR11571, showing why GO:0004364 is too specific at the family level and which divergent branches require narrower, subfamily-specific molecular function terms.*

**Summary of recommendations:**

| Level | Recommended GO MF term | Applicable branches |
|-------|----------------------|---------------------|
| **Family-level (PTHR11571)** | glutathione binding (GO:0043295) | All branches sharing the conserved G-site |
| **Subfamily: Alpha/Mu/Pi/Theta/Sigma(enzymatic)/Phi/Tau** | glutathione transferase activity (GO:0004364) | Canonical conjugating GSTs |
| **Subfamily: Sigma/S-crystallin (SF150)** | structural constituent of eye lens (GO:0005212) | Neofunctionalized cephalopod lens proteins |
| **Subfamily: Omega** | thiol transferase activity | Glutaredoxin-like thiol-disulfide exchange |
| **Subfamily: Zeta** | maleylacetoacetate isomerase activity | Specialized metabolic isomerase |
| **Subfamily: DHAR** | dehydroascorbate reductase activity | Ascorbate recycling enzymes |
| **Subfamily: CLIC** | oxidoreductase activity, acting on sulfhydryl groups | Ion channel-associated oxidoreductases |

The currently propagated term GO:0004364 is appropriate for the canonical conjugating GST branches (Alpha, Mu, Pi, Theta, Sigma-enzymatic, Phi, Tau, Kappa) but should not be inherited by S-crystallin, Omega, CLIC, DHAR, or Zeta branches.

## Evidence and Gaps

### Key citations
- Sheehan et al., *Biochem J* 360:1–16 (2001) — comprehensive GST superfamily classification and structure-function review (sheehan2001structurefunctionand pages 4-6, sheehan2001structurefunctionand pages 2-3, sheehan2001structurefunctionand pages 7-9).
- Vaish et al., *3 Biotech* 10:1–19 (2020) — GST class diversity including Ser-GST and Cys-GST division (vaish2020glutathionestransferasea pages 10-12, vaish2020glutathionestransferasea pages 1-2).
- Pearson, *Methods Enzymol* 401:186–204 (2005) — phylogenies of GST families noting non-conjugating homologs including CLICs and crystallins (pearson2005phylogeniesofglutathione pages 6-9).
- Chiou et al., *Biochem J* 309:793–800 (1995) — characterization of octopus S-crystallins OctS1/S2/S3, sequence comparison with GSTs (chiou1995octopusscrystallinswith pages 1-2, chiou1995octopusscrystallinswith pages 4-5, chiou1995octopusscrystallinswith pages 7-8).
- Chuang et al., *Biophys J* 76:679–690 (1999) — homology model establishing S-crystallin as sigma-class GST natural mutant (chuang1999homologymodelingof pages 1-2).
- Tan et al., *Sci Rep* 6:31176 (2016) — crystal structure of S-crystallin mutant demonstrating evolutionary transition from enzyme to lens protein (tan2016structureofa pages 2-4, tan2016structureofa pages 5-6).
- Sánchez Pérez et al., *Trop Med Infect Dis* 9:85 (2024) — sigma-class GST prostaglandin synthase function and immunomodulation (perez2024sigmaclassglutathionetransferases pages 2-4, perez2024sigmaclassglutathionetransferases pages 4-5, perez2024sigmaclassglutathionetransferases pages 5-7).
- Micic et al., *Phil Trans R Soc B* 379 (2024) — plant GST functional divergence and Ser-GST vs Cys-GST classification (micic2024overlookedandmisunderstood pages 3-4).
- El Khoury et al., *Biomolecules* 15:1213 (2025) — CLIC protein glutathionylation/deglutathionylation activity (khoury2025aninvitro pages 1-2, khoury2025aninvitro pages 9-12).
- Menon, PhD thesis, ANU (2015) — GSTO1-1 as atypical GST with glutaredoxin-like properties (menon2015thebiologicalroles pages 55-58).
- Lallement et al., *Front Pharmacol* 5:192 (2014) — Cys-GST classes and their mechanistic distinction from conjugating GSTs.

### Explicit uncertainties
1. **PANTHER tree topology vs. literature classes.** This analysis maps literature-defined GST classes onto the PTHR11571 family. The exact PANTHER subfamily boundaries (e.g., how many subfamilies cover the sigma-class + S-crystallin split) could not be verified computationally; the PANTHER web interface was not programmatically accessible.
2. **Kappa-class catalytic residue.** The catalytic residue identity for Kappa-class GSTs was not resolved from retrieved literature; the Kappa class lacks the canonical SNAIL/TRAIL motifs of other cytosolic classes (sheehan2001structurefunctionand pages 7-9).
3. **Residual GST activity in S-crystallins.** While S-crystallins have drastically reduced GST activity, some residual catalytic capacity remains. Whether this vestigial activity is biologically meaningful at the high protein concentrations found in the lens is debated (chiou1995octopusscrystallinswith pages 4-5).
4. **Additional divergent branches.** The GST superfamily may contain 24–44 additional classes in non-mammalian organisms (sheehan2001structurefunctionand pages 7-9), and the full breadth of PTHR11571 subfamilies was not exhaustively audited.
5. **InterPro/Pfam domain architecture verification.** Computational verification of domain architecture consistency across PTHR11571 subfamilies was not performed (web-only resource); this would strengthen the evidence for functional heterogeneity if domain composition varies across subfamilies.

References

1. (sheehan2001structurefunctionand pages 4-6): David SHEEHAN, Gerardene MEADE, Vivienne M. FOLEY, and Catriona A. DOWD. Structure, function and evolution of glutathione transferases: implications for classification of non-mammalian members of an ancient enzyme superfamily. The Biochemical journal, 360 Pt 1:1-16, Nov 2001. URL: https://doi.org/10.1042/0264-6021:3600001, doi:10.1042/0264-6021:3600001. This article has 2581 citations.

2. (vaish2020glutathionestransferasea pages 10-12): Swati Vaish, Divya Gupta, Rajesh Mehrotra, Sandhya Mehrotra, and Mahesh Kumar Basantani. Glutathione s-transferase: a versatile protein family. 3 Biotech, 10:1-19, Jun 2020. URL: https://doi.org/10.1007/s13205-020-02312-3, doi:10.1007/s13205-020-02312-3. This article has 185 citations and is from a peer-reviewed journal.

3. (sheehan2001structurefunctionand pages 2-3): David SHEEHAN, Gerardene MEADE, Vivienne M. FOLEY, and Catriona A. DOWD. Structure, function and evolution of glutathione transferases: implications for classification of non-mammalian members of an ancient enzyme superfamily. The Biochemical journal, 360 Pt 1:1-16, Nov 2001. URL: https://doi.org/10.1042/0264-6021:3600001, doi:10.1042/0264-6021:3600001. This article has 2581 citations.

4. (vaish2020glutathionestransferasea pages 1-2): Swati Vaish, Divya Gupta, Rajesh Mehrotra, Sandhya Mehrotra, and Mahesh Kumar Basantani. Glutathione s-transferase: a versatile protein family. 3 Biotech, 10:1-19, Jun 2020. URL: https://doi.org/10.1007/s13205-020-02312-3, doi:10.1007/s13205-020-02312-3. This article has 185 citations and is from a peer-reviewed journal.

5. (micic2024overlookedandmisunderstood pages 3-4): Nikola Micic, Asta Holmelund Rønager, Mette Sørensen, and Nanna Bjarnholt. Overlooked and misunderstood: can glutathione conjugates be clues to understanding plant glutathione transferases? Philosophical Transactions of the Royal Society B: Biological Sciences, Sep 2024. URL: https://doi.org/10.1098/rstb.2023.0365, doi:10.1098/rstb.2023.0365. This article has 21 citations and is from a domain leading peer-reviewed journal.

6. (perez2024sigmaclassglutathionetransferases pages 2-4): Lluvia de Carolina Sánchez Pérez, Rafael A. Zubillaga, Ponciano García-Gutiérrez, and Abraham Landa. Sigma-class glutathione transferases (gstσ): a new target with potential for helminth control. Tropical Medicine and Infectious Disease, 9:85, Apr 2024. URL: https://doi.org/10.3390/tropicalmed9040085, doi:10.3390/tropicalmed9040085. This article has 11 citations.

7. (pearson2005phylogeniesofglutathione pages 6-9): William R. Pearson. Phylogenies of glutathione transferase families. Methods in enzymology, 401:186-204, Jan 2005. URL: https://doi.org/10.1016/s0076-6879(05)01012-8, doi:10.1016/s0076-6879(05)01012-8. This article has 135 citations and is from a peer-reviewed journal.

8. (sheehan2001structurefunctionand pages 7-9): David SHEEHAN, Gerardene MEADE, Vivienne M. FOLEY, and Catriona A. DOWD. Structure, function and evolution of glutathione transferases: implications for classification of non-mammalian members of an ancient enzyme superfamily. The Biochemical journal, 360 Pt 1:1-16, Nov 2001. URL: https://doi.org/10.1042/0264-6021:3600001, doi:10.1042/0264-6021:3600001. This article has 2581 citations.

9. (sheehan2001structurefunctionand pages 9-10): David SHEEHAN, Gerardene MEADE, Vivienne M. FOLEY, and Catriona A. DOWD. Structure, function and evolution of glutathione transferases: implications for classification of non-mammalian members of an ancient enzyme superfamily. The Biochemical journal, 360 Pt 1:1-16, Nov 2001. URL: https://doi.org/10.1042/0264-6021:3600001, doi:10.1042/0264-6021:3600001. This article has 2581 citations.

10. (sheehan2001structurefunctionand pages 3-4): David SHEEHAN, Gerardene MEADE, Vivienne M. FOLEY, and Catriona A. DOWD. Structure, function and evolution of glutathione transferases: implications for classification of non-mammalian members of an ancient enzyme superfamily. The Biochemical journal, 360 Pt 1:1-16, Nov 2001. URL: https://doi.org/10.1042/0264-6021:3600001, doi:10.1042/0264-6021:3600001. This article has 2581 citations.

11. (perez2024sigmaclassglutathionetransferases pages 4-5): Lluvia de Carolina Sánchez Pérez, Rafael A. Zubillaga, Ponciano García-Gutiérrez, and Abraham Landa. Sigma-class glutathione transferases (gstσ): a new target with potential for helminth control. Tropical Medicine and Infectious Disease, 9:85, Apr 2024. URL: https://doi.org/10.3390/tropicalmed9040085, doi:10.3390/tropicalmed9040085. This article has 11 citations.

12. (perez2024sigmaclassglutathionetransferases pages 10-11): Lluvia de Carolina Sánchez Pérez, Rafael A. Zubillaga, Ponciano García-Gutiérrez, and Abraham Landa. Sigma-class glutathione transferases (gstσ): a new target with potential for helminth control. Tropical Medicine and Infectious Disease, 9:85, Apr 2024. URL: https://doi.org/10.3390/tropicalmed9040085, doi:10.3390/tropicalmed9040085. This article has 11 citations.

13. (chuang1999homologymodelingof pages 1-2): Chyh-Chong Chuang, Shih-Hsiung Wu, Shyh-Horng Chiou, and Gu-Gang Chang. Homology modeling of cephalopod lens s-crystallin: a natural mutant of sigma-class glutathione transferase with diminished endogenous activity. Biophysical journal, 76 2:679-90, Feb 1999. URL: https://doi.org/10.1016/s0006-3495(99)77235-8, doi:10.1016/s0006-3495(99)77235-8. This article has 27 citations and is from a domain leading peer-reviewed journal.

14. (tan2016structureofa pages 2-4): Wei-Hung Tan, Shu-Chun Cheng, Yu-Tung Liu, Cheng-Guo Wu, Min-Han Lin, Chiao-Che Chen, Chao-Hsiung Lin, and Chi-Yuan Chou. Structure of a highly active cephalopod s-crystallin mutant: new molecular evidence for evolution from an active enzyme into lens-refractive protein. Scientific Reports, Aug 2016. URL: https://doi.org/10.1038/srep31176, doi:10.1038/srep31176. This article has 17 citations and is from a peer-reviewed journal.

15. (sheehan2001structurefunctionand pages 10-10): David SHEEHAN, Gerardene MEADE, Vivienne M. FOLEY, and Catriona A. DOWD. Structure, function and evolution of glutathione transferases: implications for classification of non-mammalian members of an ancient enzyme superfamily. The Biochemical journal, 360 Pt 1:1-16, Nov 2001. URL: https://doi.org/10.1042/0264-6021:3600001, doi:10.1042/0264-6021:3600001. This article has 2581 citations.

16. (menon2015thebiologicalroles pages 55-58): Deepthi Menon. The biological roles of glutathione transferase omega 1. ArXiv, Mar 2015. URL: https://doi.org/10.25911/5d70ef0bed810, doi:10.25911/5d70ef0bed810. This article has 1 citations.

17. (khoury2025aninvitro pages 1-2): Wendy El Khoury, Khondker Rufaka Hossain, Amani Alghalayini, Hala M. Ali, and Stella M. Valenzuela. An in vitro study of protein s-glutathionylation by members of the clic protein family. Biomolecules, 15:1213, Aug 2025. URL: https://doi.org/10.3390/biom15091213, doi:10.3390/biom15091213. This article has 0 citations.

18. (khoury2025aninvitro pages 15-15): Wendy El Khoury, Khondker Rufaka Hossain, Amani Alghalayini, Hala M. Ali, and Stella M. Valenzuela. An in vitro study of protein s-glutathionylation by members of the clic protein family. Biomolecules, 15:1213, Aug 2025. URL: https://doi.org/10.3390/biom15091213, doi:10.3390/biom15091213. This article has 0 citations.

19. (khoury2025aninvitro pages 13-15): Wendy El Khoury, Khondker Rufaka Hossain, Amani Alghalayini, Hala M. Ali, and Stella M. Valenzuela. An in vitro study of protein s-glutathionylation by members of the clic protein family. Biomolecules, 15:1213, Aug 2025. URL: https://doi.org/10.3390/biom15091213, doi:10.3390/biom15091213. This article has 0 citations.

20. (khoury2025aninvitro pages 9-12): Wendy El Khoury, Khondker Rufaka Hossain, Amani Alghalayini, Hala M. Ali, and Stella M. Valenzuela. An in vitro study of protein s-glutathionylation by members of the clic protein family. Biomolecules, 15:1213, Aug 2025. URL: https://doi.org/10.3390/biom15091213, doi:10.3390/biom15091213. This article has 0 citations.

21. (chiou1995octopusscrystallinswith pages 4-5): S. Chiou, C. W. Yu, C. W. Lin, F. Pan, S. F. Lu, H. Lee, and G. Chang. Octopus s-crystallins with endogenous glutathione s-transferase (gst) activity: sequence comparison and evolutionary relationships with authentic gst enzymes. The Biochemical journal, 309 ( Pt 3):793-800, Aug 1995. URL: https://doi.org/10.1042/bj3090793, doi:10.1042/bj3090793. This article has 22 citations.

22. (chiou1995octopusscrystallinswith pages 7-8): S. Chiou, C. W. Yu, C. W. Lin, F. Pan, S. F. Lu, H. Lee, and G. Chang. Octopus s-crystallins with endogenous glutathione s-transferase (gst) activity: sequence comparison and evolutionary relationships with authentic gst enzymes. The Biochemical journal, 309 ( Pt 3):793-800, Aug 1995. URL: https://doi.org/10.1042/bj3090793, doi:10.1042/bj3090793. This article has 22 citations.

23. (tan2016structureofa pages 5-6): Wei-Hung Tan, Shu-Chun Cheng, Yu-Tung Liu, Cheng-Guo Wu, Min-Han Lin, Chiao-Che Chen, Chao-Hsiung Lin, and Chi-Yuan Chou. Structure of a highly active cephalopod s-crystallin mutant: new molecular evidence for evolution from an active enzyme into lens-refractive protein. Scientific Reports, Aug 2016. URL: https://doi.org/10.1038/srep31176, doi:10.1038/srep31176. This article has 17 citations and is from a peer-reviewed journal.

24. (chiou1995octopusscrystallinswith pages 5-5): S. Chiou, C. W. Yu, C. W. Lin, F. Pan, S. F. Lu, H. Lee, and G. Chang. Octopus s-crystallins with endogenous glutathione s-transferase (gst) activity: sequence comparison and evolutionary relationships with authentic gst enzymes. The Biochemical journal, 309 ( Pt 3):793-800, Aug 1995. URL: https://doi.org/10.1042/bj3090793, doi:10.1042/bj3090793. This article has 22 citations.

25. (chiou1995octopusscrystallinswith pages 1-2): S. Chiou, C. W. Yu, C. W. Lin, F. Pan, S. F. Lu, H. Lee, and G. Chang. Octopus s-crystallins with endogenous glutathione s-transferase (gst) activity: sequence comparison and evolutionary relationships with authentic gst enzymes. The Biochemical journal, 309 ( Pt 3):793-800, Aug 1995. URL: https://doi.org/10.1042/bj3090793, doi:10.1042/bj3090793. This article has 22 citations.

26. (tan2016structureofa pages 6-7): Wei-Hung Tan, Shu-Chun Cheng, Yu-Tung Liu, Cheng-Guo Wu, Min-Han Lin, Chiao-Che Chen, Chao-Hsiung Lin, and Chi-Yuan Chou. Structure of a highly active cephalopod s-crystallin mutant: new molecular evidence for evolution from an active enzyme into lens-refractive protein. Scientific Reports, Aug 2016. URL: https://doi.org/10.1038/srep31176, doi:10.1038/srep31176. This article has 17 citations and is from a peer-reviewed journal.

27. (gavriouchkina2025asinglecellatlas pages 5-6): Daria Gavriouchkina, Yongkai Tan, Elise Parey, Fabienne Ziadi-Künzli, Yuko Hasegawa, Laura Piovani, Lin Zhang, Chikatoshi Sugimoto, Nicholas Luscombe, Ferdinand Marlétaz, and Daniel S. Rokhsar. A single-cell atlas of the bobtail squid visual and nervous system highlights molecular principles of convergent evolution. Nature Ecology & Evolution, 9:1245-1262, Jun 2025. URL: https://doi.org/10.1038/s41559-025-02720-9, doi:10.1038/s41559-025-02720-9. This article has 44 citations and is from a highest quality peer-reviewed journal.

28. (perez2024sigmaclassglutathionetransferases pages 5-7): Lluvia de Carolina Sánchez Pérez, Rafael A. Zubillaga, Ponciano García-Gutiérrez, and Abraham Landa. Sigma-class glutathione transferases (gstσ): a new target with potential for helminth control. Tropical Medicine and Infectious Disease, 9:85, Apr 2024. URL: https://doi.org/10.3390/tropicalmed9040085, doi:10.3390/tropicalmed9040085. This article has 11 citations.

## Artifacts

- [Edison artifact artifact-00](PTHR11571-function-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PTHR11571-function-falcon_artifacts/artifact-01.md)