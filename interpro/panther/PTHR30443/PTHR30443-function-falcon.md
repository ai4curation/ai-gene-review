---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-24T04:30:09.086182'
end_time: '2026-06-24T04:45:36.414706'
duration_seconds: 927.33
template_file: templates/treegrafter_family_function.md
template_variables:
  family_id: PTHR30443
  family_name: INNER MEMBRANE PROTEIN
  subfamily: PTHR30443:SF0 PHOSPHOETHANOLAMINE TRANSFERASE EPTA
  gene_symbol: mcr-1
  uniprot: A0A0R6L508
  organism: ECOLX
  taxon_label: ECOLX
  propagated_term: phosphotransferase activity, phosphate group as acceptor (GO:0016776)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 33
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: PTHR30443-function-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PTHR30443-function-falcon_artifacts/artifact-01.md
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

- **PANTHER family:** PTHR30443 — INNER MEMBRANE PROTEIN
- **Subfamily of interest:** PTHR30443:SF0 PHOSPHOETHANOLAMINE TRANSFERASE EPTA
- **Representative member:** mcr-1 (A0A0R6L508), ECOLX / ECOLX
- **GO term currently propagated at/near this node:** phosphotransferase activity, phosphate group as acceptor (GO:0016776)

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
3. **Subfamily of interest.** Where does PTHR30443:SF0 PHOSPHOETHANOLAMINE TRANSFERASE EPTA sit — does it carry the
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

- **PANTHER family:** PTHR30443 — INNER MEMBRANE PROTEIN
- **Subfamily of interest:** PTHR30443:SF0 PHOSPHOETHANOLAMINE TRANSFERASE EPTA
- **Representative member:** mcr-1 (A0A0R6L508), ECOLX / ECOLX
- **GO term currently propagated at/near this node:** phosphotransferase activity, phosphate group as acceptor (GO:0016776)

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
3. **Subfamily of interest.** Where does PTHR30443:SF0 PHOSPHOETHANOLAMINE TRANSFERASE EPTA sit — does it carry the
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


# PTHR30443 — INNER MEMBRANE PROTEIN / Phosphoethanolamine Transferase Family: TreeGrafter Granularity Audit

## Family Function Summary

PANTHER family PTHR30443, annotated as "INNER MEMBRANE PROTEIN," comprises the bacterial phosphoethanolamine transferase (PET) superfamily. These are integral inner-membrane metalloenzymes belonging to the alkaline phosphatase superfamily that share a conserved two-domain architecture: an N-terminal transmembrane domain containing five transmembrane helices, connected via a bridging helix to a C-terminal periplasmic catalytic domain adopting a hydrolase/sulfatase-type fold (samantha2020lipidaphosphoethanolamine pages 8-12, anandan2020structureandfunction pages 14-17, anandan2017structureofa pages 2-3). The catalytic domain harbors a Zn²⁺ ion tetrahedrally coordinated by conserved residues (His, Asp, Glu, and a catalytic Thr in Class I enzymes; His453, Asp452, Glu240, and Thr280 in *Neisseria meningitidis* EptA numbering) (anandan2017structureofa pages 2-3, thai2023phosphoethanolaminetransferasesas pages 14-16). These enzymes operate via a ping-pong mechanism: the catalytic threonine (or serine in Class VI) nucleophile attacks the phosphoethanolamine (pEtN) moiety of phosphatidylethanolamine (PE), forming a pEtN-enzyme intermediate and releasing diacylglycerol, then the pEtN is transferred to the acceptor substrate (schumann2024themultifacetedroles pages 2-4, thai2023phosphoethanolaminetransferasesas pages 16-18, anandan2020structureandfunction pages 17-20). The conserved core molecular function across the family is **phosphoethanolamine transferase activity** — the transfer of a pEtN moiety from PE to a diverse array of acceptor substrates. However, the acceptor substrates diverge radically across subfamilies (lipid A, Kdo sugars, heptose residues, O-antigen, cellulose, periplasmic glucans, and even pilin proteins), making this family functionally **heterogeneous** with respect to substrate specificity (thai2023phosphoethanolaminetransferasesas pages 9-10, thai2023phosphoethanolaminetransferasesas pages 2-5, thai2023phosphoethanolaminetransferasesas pages 6-7).

## Subfamily Divergence Table

The following table enumerates the major functional subgroups, their substrate specificities, catalytic residue status, and appropriate GO molecular function terms.

| Subgroup/Class | Representative Member(s) | Molecular Function | Substrate/Specialization | Catalytic Residues Intact? | GO MF Term That Fits | Notes |
|---|---|---|---|---|---|---|
| Class I | EptA/PmrC/LptA; MCR-1 through MCR-10 | Lipid A phosphoethanolamine transferase | Transfers pEtN from phosphatidylethanolamine (PE) to lipid A phosphates | Yes; canonical Zn2+-dependent active site with catalytic Thr nucleophile and conserved His/Asp/Glu ligands | lipid A phosphoethanolamine transferase activity | Best-characterized branch for colistin resistance. MCR-1 preferentially modifies the 4′-phosphate, whereas chromosomal EptA preferentially modifies the 1-phosphate; mcr genes likely evolved from chromosomal eptA after mobilization/diversification (thai2023phosphoethanolaminetransferasesas pages 9-10, schumann2024themultifacetedroles pages 4-6, gaballa2023morethanmcr pages 2-3, schumann2024siteselectivemodificationsby pages 7-10, schumann2024siteselectivemodificationsby pages 1-2) |
| Class II | EptB | Kdo-specific phosphoethanolamine transferase | Modifies KdoII in the LPS inner core | Yes; catalytic PET machinery retained | phosphoethanolamine transferase activity | Core-oligosaccharide rather than lipid A modifier; distinct acceptor specificity from Class I (thai2023phosphoethanolaminetransferasesas pages 9-10, schumann2024themultifacetedroles pages 2-4, thai2023phosphoethanolaminetransferasesas pages 6-7) |
| Class III | EptC/CptA | Heptose-core phosphoethanolamine transferase | Modifies HepI in the LPS/LOS inner core | Yes, but diverged; Zn2+-coordinating residues present, with only two essential in tested Class III enzyme | phosphoethanolamine transferase activity | Functionally broader in some taxa; Campylobacter jejuni EptC can also modify lipid A, flagellar rod protein FlgG, and N-glycan-linked structures (thai2023phosphoethanolaminetransferasesas pages 9-10, anandan2020structureandfunction pages 14-17, thai2023phosphoethanolaminetransferasesas pages 14-16) |
| Class IV | Lpt-O | O-antigen phosphoethanolamine transferase | Modifies O-antigen sugars | Presumed intact in functional members; no divergent catalytic exception highlighted in retrieved sources | phosphoethanolamine transferase activity | Accepts O-antigen rather than lipid A or inner-core sugars, demonstrating family substrate divergence (thai2023phosphoethanolaminetransferasesas pages 2-5, thai2023phosphoethanolaminetransferasesas pages 6-7, thai2023phosphoethanolaminetransferasesas pages 9-10) |
| Class V | PetK | KdoI-specific phosphoethanolamine transferase | Modifies KdoI in LPS core | Presumed intact in functional members; no catalytic anomaly noted in retrieved sources | phosphoethanolamine transferase activity | Distinct from EptB by Kdo position specificity (thai2023phosphoethanolaminetransferasesas pages 6-7) |
| Class VI | BcsG | Cellulose phosphoethanolamine transferase | Modifies cellulose | Diverged catalytic architecture; uses Ser nucleophile instead of Thr and different Zn2+ ligands (Cys243, Glu442, His443) | phosphoethanolamine transferase activity | Strong evidence that not all family members share the canonical Class I active-site chemistry; also lacks the second Zn2+ site described for Class I enzymes (thai2023phosphoethanolaminetransferasesas pages 2-5, thai2023phosphoethanolaminetransferasesas pages 6-7, thai2023phosphoethanolaminetransferasesas pages 22-24, thai2023phosphoethanolaminetransferasesas pages 14-16, thai2023phosphoethanolaminetransferasesas pages 16-18) |
| Class VII | Lpt6 / EptC-type | HepII O-6 phosphoethanolamine transferase | Modifies O-6 of HepII in LOS/LPS | Presumed intact in functional members | phosphoethanolamine transferase activity | LOS/LPS inner-core branch distinct from HepI and Kdo-modifying enzymes (thai2023phosphoethanolaminetransferasesas pages 6-7) |
| Class VIII | Lpt3 | HepII O-3 phosphoethanolamine transferase | Modifies O-3 of HepII in LOS | Presumed intact in functional members | phosphoethanolamine transferase activity | Position-specific core glycan modifier; distinct from Lpt6 despite related chemistry (thai2023phosphoethanolaminetransferasesas pages 6-7) |
| Class IX | OpgE | Periplasmic glucan phosphoethanolamine transferase | Modifies osmoregulated periplasmic glucans | Not directly resolved in retrieved sources for residue-level conservation | phosphoethanolamine transferase activity | Non-LPS carbohydrate substrate; demonstrates that family function extends beyond envelope lipid/core decoration (thai2023phosphoethanolaminetransferasesas pages 2-5, thai2023phosphoethanolaminetransferasesas pages 6-7, thai2023phosphoethanolaminetransferasesas pages 22-24) |
| Class X | PetG | Galactose-residue phosphoethanolamine transferase | Modifies galactose residues of LPS | Not directly resolved in retrieved sources for residue-level conservation | phosphoethanolamine transferase activity | Another acceptor-specific branch outside lipid A/Kdo/Hep categories (thai2023phosphoethanolaminetransferasesas pages 6-7) |
| Class XI | PptA | Pilin phosphoethanolamine transferase | Modifies pilin subunit PilE | Not directly resolved in retrieved sources for residue-level conservation | phosphoethanolamine transferase activity | Protein substrate rather than lipid or sugar acceptor; important evidence against using a lipid A-specific family-level GO term (thai2023phosphoethanolaminetransferasesas pages 2-5, thai2023phosphoethanolaminetransferasesas pages 6-7, thai2023phosphoethanolaminetransferasesas pages 22-24) |
| Divergent PET-like branch | PET-B; PET-C | Putative lipid A phosphoethanolamine transferase-like proteins | Lipid A-related/unknown; PET-C can modify lipid A in E. coli assays but neither PET-B nor PET-C conferred detectable colistin resistance phenotype in E. coli | Unclear/branch-specific; not safely inferable as bona fide catalytic activity for all homologs | phosphoethanolamine transferase activity, if and only if experimentally supported; otherwise avoid specific MF propagation | PET-B showed no detectable pEtN modification activity in E. coli; PET-C modified the 4′-phosphate yet still lacked measurable colistin-resistance phenotype. Could reflect host-specific activity, altered substrate preference, reduced efficiency, or partial/pseudoenzymatic divergence (schumann2024siteselectivemodificationsby pages 7-10, schumann2024siteselectivemodificationsby pages 5-7, schumann2024siteselectivemodificationsby pages 10-12, schumann2024siteselectivemodificationsby pages 1-2, schumann2024siteselectivemodificationsby pages 12-14) |


*Table: This table summarizes the major functional subgroups within the PTHR30443 phosphoethanolamine transferase family, highlighting conserved transfer chemistry alongside strong divergence in acceptor substrate, catalytic architecture, and phenotype. It is useful for judging whether family-level GO propagation is safe or whether annotation must be constrained to narrower subfamilies.*

## Homogeneous vs. Heterogeneous Verdict

**This family is functionally HETEROGENEOUS.** A single family-level GO MF term is NOT safe to propagate across the entire family if that term specifies a particular acceptor substrate. The family encompasses at least 11 experimentally distinct subclasses with radically different acceptor substrates, ranging from lipid A phosphate groups (Class I EptA/MCR), to Kdo sugars of the LPS inner core (Classes II and V), to heptose residues (Classes III, VII, VIII), O-antigen (Class IV), cellulose (Class VI BcsG), osmoregulated periplasmic glucans (Class IX OpgE), galactose residues of LPS (Class X), and even protein substrates such as the pilin subunit PilE (Class XI PptA) (thai2023phosphoethanolaminetransferasesas pages 9-10, thai2023phosphoethanolaminetransferasesas pages 2-5, thai2023phosphoethanolaminetransferasesas pages 6-7).

Furthermore, catalytic residue architecture itself varies across subclasses: Class VI BcsG uses a Ser nucleophile instead of the canonical Thr and coordinates Zn²⁺ via Cys243, Glu442, and His443 rather than the Class I-typical His/Asp/Glu/Thr constellation, and lacks the second Zn²⁺ binding site present in Class I enzymes (thai2023phosphoethanolaminetransferasesas pages 14-16, thai2023phosphoethanolaminetransferasesas pages 16-18). Additionally, some PET-like proteins (PET-B) show no detectable pEtN modification activity in *E. coli*, raising the possibility of pseudoenzymatic divergence or host-restricted activity (schumann2024siteselectivemodificationsby pages 7-10, schumann2024siteselectivemodificationsby pages 5-7, schumann2024siteselectivemodificationsby pages 10-12).

The only function that can be safely propagated at the family level is the *general* phosphoethanolamine transferase activity — the Zn²⁺-dependent transfer of pEtN from PE to an acceptor substrate — without specifying the nature of the acceptor. Even this family-level term should be applied cautiously to branches like PET-B where catalytic activity has not been confirmed.

## Subfamily of Interest: PTHR30443:SF0 — PHOSPHOETHANOLAMINE TRANSFERASE EPTA

PTHR30443:SF0, represented by MCR-1 (A0A0R6L508), belongs to the Class I lipid A-modifying PET clade. MCR-1 is a plasmid-encoded phosphoethanolamine transferase that catalyzes the addition of pEtN from PE to the phosphate groups of lipid A, the lipid anchor of lipopolysaccharide (LPS) in the outer membrane of Gram-negative bacteria (zinkle2025mechanisticbasisof pages 1-2, anandan2020structureandfunction pages 14-17). This modification reduces the net negative charge of the outer membrane, thereby conferring resistance to the cationic antimicrobial peptide colistin (polymyxin E), a last-resort antibiotic (gaballa2023morethanmcr pages 2-3, gaballa2023morethanmcr pages 1-2).

MCR-1 preferentially modifies the **4′-phosphate** of lipid A, conferring strong colistin resistance (8–16-fold MIC increase) with relatively low fitness costs. In contrast, chromosomal EptA preferentially modifies the **1-phosphate** and confers fitness advantages only at sub-inhibitory colistin concentrations while incurring higher fitness costs in the absence of colistin (schumann2024siteselectivemodificationsby pages 7-10, schumann2024siteselectivemodificationsby pages 1-2). The *mcr* genes likely evolved from chromosomal *eptA* through mobilization onto plasmids via composite transposon structures, with diversification of genomic context and regulatory pathways altering gene expression and enzyme activity (schumann2024themultifacetedroles pages 4-6, gaballa2023morethanmcr pages 1-2). As of July 2024, 10 major MCR families (MCR-1 through MCR-10) with 115 alleles have been identified (schumann2024themultifacetedroles pages 4-6, schumann2024themultifacetedroles pages 2-4).

The structural basis of MCR-1 has been resolved: the PE donor substrate binds near the active site in the periplasmic domain, while lipid A is bound within the transmembrane region over 20 Å away, and a two-state conformational model involves rotation of the periplasmic domain to bring the active site to lipid A (zinkle2025mechanisticbasisof pages 1-2). The conserved catalytic residues include Thr285 (nucleophile), Glu246, His395, His466, Asp465, and His478 (schumann2024themultifacetedroles pages 2-4, thai2023phosphoethanolaminetransferasesas pages 14-16, thai2023phosphoethanolaminetransferasesas pages 16-18).

**Characterized exemplars of PTHR30443:SF0:** MCR-1 (A0A0R6L508, first identified 2015), MCR-3, MCR-9 (all Class I lipid A-modifying PETs); chromosomal EptA/PmrC (*E. coli*, *Salmonella*, *Neisseria*); PetL (*Pasteurella multocida*). The subfamily carries a **more specific specialized activity** (lipid A pEtN transfer) relative to the broader family-level conserved function (general pEtN transfer).

## Granularity Leads for Curation

> PTHR30443 is functionally **heterogeneous**: characterized members share phosphoethanolamine (pEtN) transfer chemistry, but diverge strongly in acceptor substrate, including lipid A, Kdo, heptose, O-antigen, cellulose, periplasmic glucans, and pilin; therefore a single narrow subfamily function is not safe to propagate across the whole family (thai2023phosphoethanolaminetransferasesas pages 9-10, schumann2024themultifacetedroles pages 4-6, thai2023phosphoethanolaminetransferasesas pages 2-5, thai2023phosphoethanolaminetransferasesas pages 6-7).
>
> The currently propagated term **GO:0016776 phosphotransferase activity, phosphate group as acceptor** is chemically defensible but **over-generic** for this family because it misses the defining conserved feature: these are Zn2+-dependent **phosphoethanolamine transferases** that use phosphatidylethanolamine as donor and transfer a pEtN moiety to diverse acceptors (samantha2020lipidaphosphoethanolamine pages 8-12, anandan2020structureandfunction pages 14-17, schumann2024themultifacetedroles pages 2-4).
>
> **Family-level curation lead:** use a term equivalent to **phosphoethanolamine transferase activity** for branches where catalytic function is supported, rather than a lipid A-specific term; this better captures the conserved chemistry while avoiding false restriction to LPS/lipid A substrates (thai2023phosphoethanolaminetransferasesas pages 2-5, thai2023phosphoethanolaminetransferasesas pages 6-7, thai2023phosphoethanolaminetransferasesas pages 22-24).
>
> **Subfamily-level curation lead for PTHR30443:SF0 (EptA/MCR):** annotate as **lipid A phosphoethanolamine transferase activity** (or equivalent) because this branch specifically modifies lipid A and includes the canonical colistin-resistance enzymes EptA/MCR; within this branch, MCR-1 and EptA differ further in preferred lipid A phosphate site (4′ versus 1) (gaballa2023morethanmcr pages 2-3, samantha2020lipidaphosphoethanolamine pages 5-8, schumann2024siteselectivemodificationsby pages 7-10, schumann2024siteselectivemodificationsby pages 1-2).
>
> **Do not automatically propagate even the family-level catalytic term to all PET-like branches**: PET-B/PET-C-like proteins showed absent or weak/noncanonical phenotypes in E. coli, with PET-B lacking detectable pEtN modification and PET-C showing lipid A modification without a colistin-resistance phenotype; these branches may be host-specific, low-activity, or partially diverged and need direct evidence (schumann2024siteselectivemodificationsby pages 7-10, schumann2024siteselectivemodificationsby pages 10-12, schumann2024siteselectivemodificationsby pages 1-2, schumann2024siteselectivemodificationsby pages 12-14).
>
> **Class VI BcsG** remains within the broader pEtN-transferase family, but it uses altered catalytic machinery, including a **Ser** nucleophile instead of the canonical Class I **Thr**, different Zn2+-coordinating residues, and no second Zn2+ site; thus family-level chemistry may still apply, but Class I-specific residue annotations should **not** be propagated to BcsG branches (thai2023phosphoethanolaminetransferasesas pages 14-16, thai2023phosphoethanolaminetransferasesas pages 16-18).
>
> **Class XI PptA** modifies the pilin subunit **PilE** rather than lipid A, LPS core sugars, or other glycans; any LPS-specific or lipid A-specific GO term at the family node would therefore mis-annotate this branch (thai2023phosphoethanolaminetransferasesas pages 2-5, thai2023phosphoethanolaminetransferasesas pages 6-7, thai2023phosphoethanolaminetransferasesas pages 22-24).


*Blockquote: This blockquote summarizes the curation implications of the PTHR30443 audit. It distinguishes the conserved family-level phosphoethanolamine transfer chemistry from the strongly divergent subfamily-level acceptor specificities that make broad GO propagation unsafe.*

**Summary of recommendations:**

| Level | Recommended GO MF Term | Notes |
|---|---|---|
| **Family level (PTHR30443)** | Phosphoethanolamine transferase activity (or the closest available GO term capturing Zn²⁺-dependent pEtN transfer from PE to acceptor) | Safe for branches with confirmed catalytic residues; not safe for PET-B-like branches without experimental support |
| **Subfamily level (PTHR30443:SF0, EptA/MCR)** | Lipid A phosphoethanolamine transferase activity | Appropriately captures the substrate-specific function of this clade |
| **Currently propagated term (GO:0016776)** | Phosphotransferase activity, phosphate group as acceptor | Over-generic — misses the defining pEtN specificity; technically defensible but uninformative for this family |

**Branches where the current family-level term would be an over-annotation:**
- **PET-B-like sequences:** No confirmed catalytic activity; propagating any enzymatic GO term risks false positive annotation (schumann2024siteselectivemodificationsby pages 10-12).
- **Class XI (PptA):** Any lipid A- or LPS-specific term would mis-annotate this protein-modifying branch (thai2023phosphoethanolaminetransferasesas pages 6-7, thai2023phosphoethanolaminetransferasesas pages 22-24).
- **Class VI (BcsG):** The canonical Class I catalytic Thr residue is replaced by Ser; Class I-specific residue-level annotations should not be propagated (thai2023phosphoethanolaminetransferasesas pages 14-16, thai2023phosphoethanolaminetransferasesas pages 16-18).
- **Class IX (OpgE):** Modifies periplasmic glucans, not LPS; any LPS-specific term would be incorrect (thai2023phosphoethanolaminetransferasesas pages 6-7, thai2023phosphoethanolaminetransferasesas pages 22-24).

## Evidence and Gaps

**Key citations:**
- Anandan et al. (2017) PNAS 114:2218–2223 (PMID: 28193870) — Crystal structure of NmEptA, founding structural work (anandan2017structureofa pages 2-3, anandan2017structureofa pages 3-4).
- Anandan & Vrielink (2020) Ann NY Acad Sci 1459:19–37 (PMID: 31432520) — Comprehensive review of lipid A-modifying enzyme structures (anandan2020structureandfunction pages 14-17, anandan2020structureandfunction pages 17-20).
- Thai et al. (2023) Antibiotics 12:1382 — Systematic 11-class classification of PEA transferases and drug target review (thai2023phosphoethanolaminetransferasesas pages 9-10, thai2023phosphoethanolaminetransferasesas pages 2-5, thai2023phosphoethanolaminetransferasesas pages 6-7, thai2023phosphoethanolaminetransferasesas pages 22-24, thai2023phosphoethanolaminetransferasesas pages 14-16, thai2023phosphoethanolaminetransferasesas pages 16-18).
- Gaballa et al. (2023) Front Cell Infect Microbiol 13:1060519 — Evolutionary relationship between *mcr* and intrinsic *eptA* (gaballa2023morethanmcr pages 2-3, gaballa2023morethanmcr pages 1-2).
- Schumann et al. (2024) Microbiol Mol Biol Rev 88(4) — Comprehensive review of pEtN-modified LPS biology (schumann2024themultifacetedroles pages 2-4, schumann2024themultifacetedroles pages 4-6, schumann2024themultifacetedroles pages 23-25, schumann2024themultifacetedroles pages 17-19).
- Schumann et al. (2024) mSphere 9(12) — Site-selective lipid A modification by different PETs (schumann2024siteselectivemodificationsby pages 7-10, schumann2024siteselectivemodificationsby pages 5-7, schumann2024siteselectivemodificationsby pages 10-12, schumann2024siteselectivemodificationsby pages 1-2, schumann2024siteselectivemodificationsby pages 12-14).
- Zinkle et al. (2025) Nat Commun 16(1) — Cryo-EM structure of MCR-1 with substrates; two-state model (zinkle2025mechanisticbasisof pages 1-2).
- Samantha & Vrielink (2020) J Mol Biol 432:5184–5196 — EptA regulation, structure, immune response (samantha2020lipidaphosphoethanolamine pages 8-12, samantha2020lipidaphosphoethanolamine pages 5-8).
- Purcell et al. (2022) J Bacteriol 204(2) — DgkA requirement for EptA/MCR function (gallardo2020involvementofhpap2 pages 1-3).

**Explicit uncertainties that matter for granularity decisions:**
1. **Catalytic residue conservation in Classes IV, V, VII–XI** (Lpt-O, PetK, Lpt6, Lpt3, OpgE, PetG, PptA) has not been resolved at residue-level structural detail. These classes are assigned to the PET family by sequence homology, but structural/mutagenesis data are limited to Classes I, III, and VI. Computational residue-conservation analysis across all classes would strengthen the family-level GO annotation.
2. **PET-B functional status** remains ambiguous: it may be a pseudoenzyme, may require a host-specific lipid A substrate (e.g., *Pseudomonas aeruginosa* rather than *E. coli*), or may have lost catalytic competence. Its placement in the PANTHER tree and whether it should receive any enzymatic GO annotation is uncertain (schumann2024siteselectivemodificationsby pages 10-12).
3. **Whether the PANTHER family PTHR30443 actually encompasses all 11 PET classes or only a subset** cannot be confirmed without direct inspection of the PANTHER HMM and tree topology. The family name "INNER MEMBRANE PROTEIN" is uninformative, and the subfamily name "PHOSPHOETHANOLAMINE TRANSFERASE EPTA" suggests the tree may be limited to the lipid A-modifying clade. If the PANTHER family is narrower than the full 11-class PET superfamily, the heterogeneity issue may be less severe, but this requires direct PANTHER database inspection (a web-only check).
4. **EC number assignment** for these enzymes is not standardized. The reaction is not cleanly captured by existing EC numbers; the most relevant would be EC 2.7.8.— (transferases for other substituted phosphate groups), but a specific EC for pEtN transfer to lipid A has not been widely assigned.
5. **CjEptC multi-substrate activity** (lipid A, HepI, FlgG, N-glycans) challenges simple subfamily classification — it simultaneously belongs to Classes I and III functionally, suggesting that substrate specificity can be broader than the phylogenetic position implies (thai2023phosphoethanolaminetransferasesas pages 9-10, anandan2020structureandfunction pages 14-17).

References

1. (samantha2020lipidaphosphoethanolamine pages 8-12): Ariela Samantha and Alice Vrielink. Lipid a phosphoethanolamine transferase: regulation, structure and immune response. Journal of Molecular Biology, 432:5184-5196, Aug 2020. URL: https://doi.org/10.1016/j.jmb.2020.04.022, doi:10.1016/j.jmb.2020.04.022. This article has 87 citations and is from a domain leading peer-reviewed journal.

2. (anandan2020structureandfunction pages 14-17): Anandhi Anandan and Alice Vrielink. Structure and function of lipid a–modifying enzymes. Annals of the New York Academy of Sciences, 1459:19-37, Jan 2020. URL: https://doi.org/10.1111/nyas.14244, doi:10.1111/nyas.14244. This article has 54 citations and is from a peer-reviewed journal.

3. (anandan2017structureofa pages 2-3): Anandhi Anandan, Genevieve L. Evans, Karmen Condic-Jurkic, Megan L. O’Mara, Constance M. John, Nancy J. Phillips, Gary A. Jarvis, Siobhan S. Wills, Keith A. Stubbs, Isabel Moraes, Charlene M. Kahler, and Alice Vrielink. Structure of a lipid a phosphoethanolamine transferase suggests how conformational changes govern substrate binding. Proceedings of the National Academy of Sciences, 114:2218-2223, Feb 2017. URL: https://doi.org/10.1073/pnas.1612927114, doi:10.1073/pnas.1612927114. This article has 153 citations and is from a highest quality peer-reviewed journal.

4. (thai2023phosphoethanolaminetransferasesas pages 14-16): Van C. Thai, Keith A. Stubbs, Mitali Sarkar-Tyson, and Charlene M. Kahler. Phosphoethanolamine transferases as drug discovery targets for therapeutic treatment of multi-drug resistant pathogenic gram-negative bacteria. Antibiotics, 12:1382, Aug 2023. URL: https://doi.org/10.3390/antibiotics12091382, doi:10.3390/antibiotics12091382. This article has 13 citations.

5. (schumann2024themultifacetedroles pages 2-4): Anna Schumann, Ahmed Gaballa, and Martin Wiedmann. The multifaceted roles of phosphoethanolamine-modified lipopolysaccharides: from stress response and virulence to cationic antimicrobial resistance. Microbiology and Molecular Biology Reviews, Dec 2024. URL: https://doi.org/10.1128/mmbr.00193-23, doi:10.1128/mmbr.00193-23. This article has 13 citations and is from a domain leading peer-reviewed journal.

6. (thai2023phosphoethanolaminetransferasesas pages 16-18): Van C. Thai, Keith A. Stubbs, Mitali Sarkar-Tyson, and Charlene M. Kahler. Phosphoethanolamine transferases as drug discovery targets for therapeutic treatment of multi-drug resistant pathogenic gram-negative bacteria. Antibiotics, 12:1382, Aug 2023. URL: https://doi.org/10.3390/antibiotics12091382, doi:10.3390/antibiotics12091382. This article has 13 citations.

7. (anandan2020structureandfunction pages 17-20): Anandhi Anandan and Alice Vrielink. Structure and function of lipid a–modifying enzymes. Annals of the New York Academy of Sciences, 1459:19-37, Jan 2020. URL: https://doi.org/10.1111/nyas.14244, doi:10.1111/nyas.14244. This article has 54 citations and is from a peer-reviewed journal.

8. (thai2023phosphoethanolaminetransferasesas pages 9-10): Van C. Thai, Keith A. Stubbs, Mitali Sarkar-Tyson, and Charlene M. Kahler. Phosphoethanolamine transferases as drug discovery targets for therapeutic treatment of multi-drug resistant pathogenic gram-negative bacteria. Antibiotics, 12:1382, Aug 2023. URL: https://doi.org/10.3390/antibiotics12091382, doi:10.3390/antibiotics12091382. This article has 13 citations.

9. (thai2023phosphoethanolaminetransferasesas pages 2-5): Van C. Thai, Keith A. Stubbs, Mitali Sarkar-Tyson, and Charlene M. Kahler. Phosphoethanolamine transferases as drug discovery targets for therapeutic treatment of multi-drug resistant pathogenic gram-negative bacteria. Antibiotics, 12:1382, Aug 2023. URL: https://doi.org/10.3390/antibiotics12091382, doi:10.3390/antibiotics12091382. This article has 13 citations.

10. (thai2023phosphoethanolaminetransferasesas pages 6-7): Van C. Thai, Keith A. Stubbs, Mitali Sarkar-Tyson, and Charlene M. Kahler. Phosphoethanolamine transferases as drug discovery targets for therapeutic treatment of multi-drug resistant pathogenic gram-negative bacteria. Antibiotics, 12:1382, Aug 2023. URL: https://doi.org/10.3390/antibiotics12091382, doi:10.3390/antibiotics12091382. This article has 13 citations.

11. (schumann2024themultifacetedroles pages 4-6): Anna Schumann, Ahmed Gaballa, and Martin Wiedmann. The multifaceted roles of phosphoethanolamine-modified lipopolysaccharides: from stress response and virulence to cationic antimicrobial resistance. Microbiology and Molecular Biology Reviews, Dec 2024. URL: https://doi.org/10.1128/mmbr.00193-23, doi:10.1128/mmbr.00193-23. This article has 13 citations and is from a domain leading peer-reviewed journal.

12. (gaballa2023morethanmcr pages 2-3): Ahmed Gaballa, Martin Wiedmann, and Laura M. Carroll. More than mcr: canonical plasmid- and transposon-encoded mobilized colistin resistance genes represent a subset of phosphoethanolamine transferases. Frontiers in Cellular and Infection Microbiology, Jun 2023. URL: https://doi.org/10.3389/fcimb.2023.1060519, doi:10.3389/fcimb.2023.1060519. This article has 24 citations.

13. (schumann2024siteselectivemodificationsby pages 7-10): Anna Schumann, Ahmed Gaballa, Hyojik Yang, Di Yu, Robert K. Ernst, and Martin Wiedmann. Site-selective modifications by lipid a phosphoethanolamine transferases linked to colistin resistance and bacterial fitness. Dec 2024. URL: https://doi.org/10.1128/msphere.00731-24, doi:10.1128/msphere.00731-24. This article has 9 citations and is from a peer-reviewed journal.

14. (schumann2024siteselectivemodificationsby pages 1-2): Anna Schumann, Ahmed Gaballa, Hyojik Yang, Di Yu, Robert K. Ernst, and Martin Wiedmann. Site-selective modifications by lipid a phosphoethanolamine transferases linked to colistin resistance and bacterial fitness. Dec 2024. URL: https://doi.org/10.1128/msphere.00731-24, doi:10.1128/msphere.00731-24. This article has 9 citations and is from a peer-reviewed journal.

15. (thai2023phosphoethanolaminetransferasesas pages 22-24): Van C. Thai, Keith A. Stubbs, Mitali Sarkar-Tyson, and Charlene M. Kahler. Phosphoethanolamine transferases as drug discovery targets for therapeutic treatment of multi-drug resistant pathogenic gram-negative bacteria. Antibiotics, 12:1382, Aug 2023. URL: https://doi.org/10.3390/antibiotics12091382, doi:10.3390/antibiotics12091382. This article has 13 citations.

16. (schumann2024siteselectivemodificationsby pages 5-7): Anna Schumann, Ahmed Gaballa, Hyojik Yang, Di Yu, Robert K. Ernst, and Martin Wiedmann. Site-selective modifications by lipid a phosphoethanolamine transferases linked to colistin resistance and bacterial fitness. Dec 2024. URL: https://doi.org/10.1128/msphere.00731-24, doi:10.1128/msphere.00731-24. This article has 9 citations and is from a peer-reviewed journal.

17. (schumann2024siteselectivemodificationsby pages 10-12): Anna Schumann, Ahmed Gaballa, Hyojik Yang, Di Yu, Robert K. Ernst, and Martin Wiedmann. Site-selective modifications by lipid a phosphoethanolamine transferases linked to colistin resistance and bacterial fitness. Dec 2024. URL: https://doi.org/10.1128/msphere.00731-24, doi:10.1128/msphere.00731-24. This article has 9 citations and is from a peer-reviewed journal.

18. (schumann2024siteselectivemodificationsby pages 12-14): Anna Schumann, Ahmed Gaballa, Hyojik Yang, Di Yu, Robert K. Ernst, and Martin Wiedmann. Site-selective modifications by lipid a phosphoethanolamine transferases linked to colistin resistance and bacterial fitness. Dec 2024. URL: https://doi.org/10.1128/msphere.00731-24, doi:10.1128/msphere.00731-24. This article has 9 citations and is from a peer-reviewed journal.

19. (zinkle2025mechanisticbasisof pages 1-2): Allen P. Zinkle, Mariana Bunoro Batista, Carmen M. Herrera, Satchal K. Erramilli, Brian Kloss, Khuram U. Ashraf, Kamil Nosol, Guozhi Zhang, Rosemary J. Cater, Michael T. Marty, Anthony A. Kossiakoff, M. Stephen Trent, Rie Nygaard, Phillip J. Stansfeld, and Filippo Mancia. Mechanistic basis of antimicrobial resistance mediated by the phosphoethanolamine transferase mcr-1. Nature Communications, Nov 2025. URL: https://doi.org/10.1038/s41467-025-65515-3, doi:10.1038/s41467-025-65515-3. This article has 4 citations and is from a highest quality peer-reviewed journal.

20. (gaballa2023morethanmcr pages 1-2): Ahmed Gaballa, Martin Wiedmann, and Laura M. Carroll. More than mcr: canonical plasmid- and transposon-encoded mobilized colistin resistance genes represent a subset of phosphoethanolamine transferases. Frontiers in Cellular and Infection Microbiology, Jun 2023. URL: https://doi.org/10.3389/fcimb.2023.1060519, doi:10.3389/fcimb.2023.1060519. This article has 24 citations.

21. (samantha2020lipidaphosphoethanolamine pages 5-8): Ariela Samantha and Alice Vrielink. Lipid a phosphoethanolamine transferase: regulation, structure and immune response. Journal of Molecular Biology, 432:5184-5196, Aug 2020. URL: https://doi.org/10.1016/j.jmb.2020.04.022, doi:10.1016/j.jmb.2020.04.022. This article has 87 citations and is from a domain leading peer-reviewed journal.

22. (anandan2017structureofa pages 3-4): Anandhi Anandan, Genevieve L. Evans, Karmen Condic-Jurkic, Megan L. O’Mara, Constance M. John, Nancy J. Phillips, Gary A. Jarvis, Siobhan S. Wills, Keith A. Stubbs, Isabel Moraes, Charlene M. Kahler, and Alice Vrielink. Structure of a lipid a phosphoethanolamine transferase suggests how conformational changes govern substrate binding. Proceedings of the National Academy of Sciences, 114:2218-2223, Feb 2017. URL: https://doi.org/10.1073/pnas.1612927114, doi:10.1073/pnas.1612927114. This article has 153 citations and is from a highest quality peer-reviewed journal.

23. (schumann2024themultifacetedroles pages 23-25): Anna Schumann, Ahmed Gaballa, and Martin Wiedmann. The multifaceted roles of phosphoethanolamine-modified lipopolysaccharides: from stress response and virulence to cationic antimicrobial resistance. Microbiology and Molecular Biology Reviews, Dec 2024. URL: https://doi.org/10.1128/mmbr.00193-23, doi:10.1128/mmbr.00193-23. This article has 13 citations and is from a domain leading peer-reviewed journal.

24. (schumann2024themultifacetedroles pages 17-19): Anna Schumann, Ahmed Gaballa, and Martin Wiedmann. The multifaceted roles of phosphoethanolamine-modified lipopolysaccharides: from stress response and virulence to cationic antimicrobial resistance. Microbiology and Molecular Biology Reviews, Dec 2024. URL: https://doi.org/10.1128/mmbr.00193-23, doi:10.1128/mmbr.00193-23. This article has 13 citations and is from a domain leading peer-reviewed journal.

25. (gallardo2020involvementofhpap2 pages 1-3): Alejandro Gallardo, María Ugarte-Ruiz, Marta Hernández, Pedro Miguela-Villoldo, David Rodríguez-Lázaro, Lucas Domínguez, and Alberto Quesada. Involvement of hpap2 and dgka genes in colistin resistance mediated by mcr determinants. Antibiotics, 9:531, Aug 2020. URL: https://doi.org/10.3390/antibiotics9090531, doi:10.3390/antibiotics9090531. This article has 23 citations.

## Artifacts

- [Edison artifact artifact-00](PTHR30443-function-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PTHR30443-function-falcon_artifacts/artifact-01.md)