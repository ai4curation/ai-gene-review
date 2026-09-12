---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-24T04:14:38.193249'
end_time: '2026-06-24T04:36:47.789351'
duration_seconds: 1329.6
template_file: templates/treegrafter_family_function.md
template_variables:
  family_id: PTHR43201
  family_name: ACYL-COA SYNTHETASE
  subfamily: PTHR43201:SF32 2-SUCCINYLBENZOATE--COA LIGASE
  gene_symbol: fcs
  uniprot: Q88HK0
  organism: PSEPK
  taxon_label: PSEPK
  propagated_term: medium-chain fatty acid-CoA ligase activity (GO:0031956)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 41
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: PTHR43201-function-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PTHR43201-function-falcon_artifacts/artifact-01.md
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

- **PANTHER family:** PTHR43201 — ACYL-COA SYNTHETASE
- **Subfamily of interest:** PTHR43201:SF32 2-SUCCINYLBENZOATE--COA LIGASE
- **Representative member:** fcs (Q88HK0), PSEPK / PSEPK
- **GO term currently propagated at/near this node:** medium-chain fatty acid-CoA ligase activity (GO:0031956)

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
3. **Subfamily of interest.** Where does PTHR43201:SF32 2-SUCCINYLBENZOATE--COA LIGASE sit — does it carry the
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

- **PANTHER family:** PTHR43201 — ACYL-COA SYNTHETASE
- **Subfamily of interest:** PTHR43201:SF32 2-SUCCINYLBENZOATE--COA LIGASE
- **Representative member:** fcs (Q88HK0), PSEPK / PSEPK
- **GO term currently propagated at/near this node:** medium-chain fatty acid-CoA ligase activity (GO:0031956)

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
3. **Subfamily of interest.** Where does PTHR43201:SF32 2-SUCCINYLBENZOATE--COA LIGASE sit — does it carry the
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


# PANTHER Family PTHR43201 (ACYL-COA SYNTHETASE) — TreeGrafter Granularity Audit

## Family Function Summary

PANTHER family PTHR43201 corresponds to the **ANL superfamily of adenylating enzymes**, named after its three historically recognized subfamilies: **Acyl-CoA synthetases**, **NRPS adenylation domains**, and **Luciferases** (gulick2009conformationaldynamicsin pages 2-4, gulick2009conformationaldynamicsin pages 1-2). All members share a conserved two-domain architecture consisting of a large N-terminal domain (αβαβα fold with two eight-stranded β-sheets) and a smaller C-terminal domain that undergoes a ~140° rotation between two catalytic half-reactions (gulick2009conformationaldynamicsin pages 4-5, gulick2009conformationaldynamicsin pages 5-7). The conserved core mechanism is a two-step reaction: (i) ATP-dependent adenylation of a carboxylate substrate to form a tightly bound acyl-AMP intermediate with release of pyrophosphate, followed by (ii) thioesterification in which a pantetheine thiol (from CoA or carrier protein) attacks the acyl-adenylate to form a thioester product and release AMP (gulick2009conformationaldynamicsin pages 2-4, lux2019targetingadenylateformingenzymes pages 2-4). Catalysis depends on a universally conserved lysine in the A10 motif region that coordinates the ribose and bridging phosphate oxygens, along with conserved aspartate and arginine residues that position ATP (gulick2009conformationaldynamicsin pages 4-5, gulick2009conformationaldynamicsin pages 7-8). However, substrate specificity varies enormously across the family, from short-chain fatty acids (C2–C4) to long-chain fatty acids (C10–C22), aromatic acids (coumarate, ferulate, succinylbenzoate), amino acids, and even luciferin (khurana2010genomescaleprediction pages 1-3, gulick2009conformationaldynamicsin pages 4-5, khurana2010genomescaleprediction pages 3-4). This extreme substrate diversity is governed by 15 specificity-determining residues (SDRs) lining the binding pocket, whose identities differ systematically among subfamilies (khurana2010genomescaleprediction pages 4-6, khurana2010genomescaleprediction pages 6-8). The family is therefore defined by its **adenylation-thioesterification fold and mechanism**, not by any single substrate class.

## Subfamily Divergence Table

The following table summarizes the major functional subgroups within the PTHR43201 family and how they differ in substrate specificity, molecular function, and appropriate GO annotation:

| Subgroup/Subfamily | Representative Member(s) (with PMID/reference) | Molecular Function | Substrate or Specialization | Catalytic Residues Intact? | GO MF Term That Fits | Notes |
|---|---|---|---|---|---|---|
| Acetyl-CoA synthetase (AcCS) | Acs from *Salmonella enterica* / fungal ACS structures summarized by Jezewski et al. 2021, DOI:10.1021/acschembio.1c00484 (not PMID in retrieved context) (khurana2010genomescaleprediction pages 1-3, khurana2010genomescaleprediction pages 6-8) | ATP-dependent acetate/short-chain acid activation followed by CoA thioesterification | Short-chain fatty acids, typically C2-C4 | Yes; canonical ANL catalytic machinery conserved, including C-terminal Lys and domain alternation | acetyl-CoA synthetase activity / short-chain fatty acid-CoA ligase activity | Conserved ANL fold; AcCS pocket uses restrictive residues such as Trp associated with small-substrate selectivity (khurana2010genomescaleprediction pages 6-8, khurana2010genomescaleprediction pages 10-13) |
| Medium-chain acyl-CoA synthetase (MCS/ACSM) | MCS class defined in Khurana et al. 2010; human ACSM family summarized by Watkins et al. 2007 (khurana2010genomescaleprediction pages 1-3, watkins2007evidencefor26 pages 12-13, watkins2007evidencefor26 pages 5-7) | ATP-dependent medium-chain fatty acid activation to acyl-CoA | Medium-chain fatty acids, ~C4-C12 | Yes in characterized ACSMs; ANL catalytic lysine/domain alternation retained | medium-chain fatty acid-CoA ligase activity | One bona fide ACS subgroup, but only one among several chemically distinct branches in PTHR43201; unsafe as a family-wide propagation term (khurana2010genomescaleprediction pages 1-3, khurana2010genomescaleprediction pages 3-4) |
| Long-chain acyl-CoA synthetase (LCS/ACSL) | LCS class in Khurana et al. 2010; ACSL family in Watkins et al. 2007 (khurana2010genomescaleprediction pages 1-3, watkins2007evidencefor26 pages 12-13, watkins2007evidencefor26 pages 5-7) | ATP-dependent long-chain fatty acid activation to acyl-CoA | Long-chain fatty acids, ~C10-C22 | Yes; canonical ANL catalytic residues retained | long-chain fatty acid-CoA ligase activity | Distinct from MCS by binding-pocket SDRs and substrate chain-length preference; same fold/mechanism but different MF granularity (khurana2010genomescaleprediction pages 6-8, khurana2010genomescaleprediction pages 10-13) |
| 4-Coumarate:CoA ligase (4CL) | Nt4CL2 (*Nicotiana tabacum*), Li & Nair 2015, DOI:10.1016/j.str.2015.08.012 (not PMID in retrieved context) (li2015structuralbasisfor pages 3-4, li2015structuralbasisfor pages 1-3, li2015structuralbasisfor pages 5-6) | ATP-dependent hydroxycinnamate activation followed by CoA ligation | 4-coumarate, caffeate, ferulate; some isoforms broaden to sinapate | Yes; ANL motifs A1-A10 and C-terminal Lys526 retained | 4-coumarate-CoA ligase activity | Strong example of aromatic-acid specialization within ANL enzymes; same domain alternation but not a fatty-acid ligase (li2015structuralbasisfor pages 3-4, li2015structuralbasisfor pages 7-8, li2015structuralbasisfor pages 5-6) |
| *o*-Succinylbenzoate-CoA ligase (MenE) | MenE from *Escherichia coli*, *Bacillus subtilis*, *Staphylococcus aureus*; pathway/enzyme summaries in Meganathan & Kwon 2009 and Evans et al. 2019 (meganathan2009biosynthesisofmenaquinone pages 8-9, boersch2018menaquinonebiosynthesisinhibition pages 2-3, evans2019structurebaseddesignsynthesis pages 8-10, evans2019structurebaseddesignsynthesis pages 1-3) | ATP-dependent ligation of CoA to *o*-succinylbenzoate via OSB-AMP intermediate | Aromatic acid *o*-succinylbenzoate in menaquinone biosynthesis | Yes; conserved ANL linchpin Lys (E. coli MenE K437), Arg/Asp network, domain alternation retained | *o*-succinylbenzoate-CoA ligase activity | Specialized biosynthetic enzyme in vitamin K2/menaquinone pathway; clearly not a medium-chain fatty acid enzyme (meganathan2009biosynthesisofmenaquinone pages 8-9, boersch2018menaquinonebiosynthesisinhibition pages 2-3) |
| Feruloyl-CoA synthetase (Fcs) | Q88HK0 Fcs from *Pseudomonas*; pathway evidence from *Pseudomonas putida* F1 and related hydroxycinnamate degraders (hughes2017pseudomonasputidaf1 pages 3-4, mohan2025biotransformationofferulic pages 5-10, mohan2025biotransformationofferulic pages 10-12) | ATP-dependent ligation of CoA to hydroxycinnamic acids | Ferulic acid, *p*-coumaric acid, caffeic acid; entry step in CoA-dependent ferulate catabolism | Yes; inferred intact ANL catalytic machinery because enzyme performs canonical adenylation/thioesterification chemistry | ferulate-CoA ligase activity / hydroxycinnamate-CoA ligase activity | Important audit point: representative Q88HK0 is Fcs-like, not MenE-like; if placed in SF32 labeled “2-succinylbenzoate--CoA ligase,” that suggests a likely subfamily labeling problem (hughes2017pseudomonasputidaf1 pages 3-4, hughes2017pseudomonasputidaf1 pages 1-2) |
| NRPS adenylation domains | DhbE/other NRPS A-domains summarized in Gulick 2009 and Khurana et al. 2010 (gulick2009conformationaldynamicsin pages 2-4, gulick2009conformationaldynamicsin pages 1-2, khurana2010genomescaleprediction pages 3-4) | ATP-dependent adenylation of amino acids or related carboxylates, usually transferred to phosphopantetheine on carrier proteins rather than free CoA | Proteinogenic/non-proteinogenic amino acids in nonribosomal peptide biosynthesis | Yes for catalytic adenylation residues; CoA-binding features differ because product is PCP-loaded thioester | amino acid adenylation activity | Shares ANL fold and first-half adenylation chemistry, but second-half nucleophile/acceptor differs; family-level “CoA ligase” already over-annotates this branch if included in a broader ANL grouping (gulick2009conformationaldynamicsin pages 2-4, priyadarshan2018fattyacylampligases pages 1-2) |
| Luciferase | Firefly luciferase; ANL relationship summarized in Gulick 2009 and Lux et al. 2019 (gulick2009conformationaldynamicsin pages 2-4, lux2019targetingadenylateformingenzymes pages 2-4, gulick2009conformationaldynamicsin pages 4-5) | ATP-dependent luciferin adenylation followed by oxidative chemistry producing light, not CoA thioester | D-luciferin | Catalytic ANL core retained, but reaction outcome diverges from CoA ligation | luciferase activity | Extreme functional divergence: same adenylate-forming ancestry and conserved fold, but neofunctionalized output; any acyl-CoA ligase GO term would mis-annotate this branch (gulick2009conformationaldynamicsin pages 2-4, lux2019targetingadenylateformingenzymes pages 2-4) |


*Table: This table summarizes the major functional branches relevant to the PTHR43201 acyl-CoA synthetase/ANL family audit. It shows that the conserved fold and adenylation mechanism are shared, but substrate specificity and even overall reaction outcome diverge strongly across subfamilies.*

## Homogeneous vs. Heterogeneous Verdict

**PTHR43201 is functionally HETEROGENEOUS.** Propagation of a single substrate-specific GO molecular function term across this entire family is not safe. The family encompasses enzymes that activate chemically distinct carboxylate substrates — including aliphatic fatty acids of different chain lengths, aromatic hydroxycinnamic acids, *o*-succinylbenzoate, amino acids, and luciferin — through the same adenylation-thioesterification fold (gulick2009conformationaldynamicsin pages 2-4, khurana2010genomescaleprediction pages 1-3, khurana2010genomescaleprediction pages 3-4). Khurana et al. (2010) formally demonstrated that the acyl-adenylate superfamily partitions into at least six functionally distinct subfamilies (AcCS, MCS, LCS, 4CL, luciferase, and NRPS), each with characteristic active-site residue profiles and non-overlapping substrate preferences (khurana2010genomescaleprediction pages 3-4, khurana2010genomescaleprediction pages 1-3). Watkins et al. (2007) independently catalogued 26 human ACS genes across six subfamilies (ACSS, ACSM, ACSL, ACSVL, ACSBG, ACSF), further demonstrating extensive functional partitioning even within the fatty acid–activating branch alone (watkins2007evidencefor26 pages 12-13, watkins2007evidencefor26 pages 5-7). Applying a substrate-specific term such as "medium-chain fatty acid-CoA ligase activity" (GO:0031956) to the entire family would mis-annotate every non-medium-chain branch, including all aromatic-substrate branches (MenE, Fcs, 4CL) and any luciferase/NRPS descendants.

## Granularity Leads for Curation

The following blockquote encapsulates the key verdict and recommendations:

> PTHR43201 is functionally **heterogeneous**: characterized members share the ANL adenylate-forming fold and ATP-dependent acyl-adenylate/thioesterification mechanism, but they diverge strongly in substrate specificity and even overall chemistry, so a single **substrate-specific** GO molecular function is not safe to propagate across the family (gulick2009conformationaldynamicsin pages 2-4, lux2019targetingadenylateformingenzymes pages 2-4, khurana2010genomescaleprediction pages 3-4, khurana2010genomescaleprediction pages 1-3).
>
> The currently propagated term **medium-chain fatty acid-CoA ligase activity (GO:0031956)** is therefore an **over-annotation**. It would mis-annotate aromatic/acrylate branches such as **MenE** (*o*-succinylbenzoate-CoA ligase in menaquinone biosynthesis), **Fcs** (feruloyl-/hydroxycinnamoyl-CoA synthetase), and **4CL** (4-coumarate:CoA ligase), and it would also be incompatible with any luciferase or NRPS-related descendants if those are present within the broader phylogenetic scope (meganathan2009biosynthesisofmenaquinone pages 8-9, boersch2018menaquinonebiosynthesisinhibition pages 2-3, li2015structuralbasisfor pages 3-4, khurana2010genomescaleprediction pages 1-3, hughes2017pseudomonasputidaf1 pages 3-4, mohan2025biotransformationofferulic pages 5-10).
>
> A safer family-level MF is a **broad ligase term**, e.g. **CoA-ligase activity (GO:0016405)** or **acid-thiol ligase activity (GO:0016878)**, with substrate-specific terms reserved for narrower, experimentally supported subfamilies (supported by the breadth of substrate classes documented for ANL/acyl-CoA synthetase branches: short-, medium-, long-chain fatty acids; hydroxycinnamates; and aromatic acids) (khurana2010genomescaleprediction pages 1-3, watkins2007evidencefor26 pages 12-13, li2015structuralbasisfor pages 3-4, gulick2009conformationaldynamicsin pages 4-5, khurana2010genomescaleprediction pages 3-4).
>
> **SF32 needs curator review independently of GO granularity:** its label says **“2-SUCCINYLBENZOATE--COA LIGASE”**, but the named representative **Q88HK0 / fcs** is reported as a **feruloyl-CoA synthetase** used in hydroxycinnamate catabolism, not as **MenE** (*o*-succinylbenzoate-CoA ligase). That discrepancy suggests possible subfamily mislabeling or mixed membership and makes direct propagation of a MenE-specific term unsafe without re-checking the clade composition (meganathan2009biosynthesisofmenaquinone pages 8-9, hughes2017pseudomonasputidaf1 pages 3-4, mohan2025biotransformationofferulic pages 5-10, hughes2017pseudomonasputidaf1 pages 1-2).


*Blockquote: This blockquote summarizes the annotation verdict for PTHR43201. It explains why the family is too functionally diverse for a substrate-specific GO term and highlights the SF32 naming/representative inconsistency that warrants curator review.*

### Specific Recommendations

**Family-level (PTHR43201):** The only GO MF term safe to propagate at the family level is a broad ligase term such as **CoA-ligase activity (GO:0016405)** or **acid-thiol ligase activity (GO:0016878)**, which captures the conserved adenylation + CoA thioesterification chemistry without specifying substrate. Even these may be too narrow if luciferase or NRPS branches are included, since those branches do not produce CoA thioesters (gulick2009conformationaldynamicsin pages 2-4, priyadarshan2018fattyacylampligases pages 1-2, lux2019targetingadenylateformingenzymes pages 2-4).

**Subfamily PTHR43201:SF32:** The currently propagated term **medium-chain fatty acid-CoA ligase activity (GO:0031956)** is an **incorrect annotation** for this subfamily. This subfamily is labeled "2-SUCCINYLBENZOATE--COA LIGASE," yet its named representative member Q88HK0 (fcs from *Pseudomonas* sp. PSEPK) is biochemically characterized as a **feruloyl-CoA synthetase (EC 6.2.1.34)** that activates hydroxycinnamic acids — specifically ferulic acid, *p*-coumaric acid, and caffeic acid — as the first step in CoA-dependent hydroxycinnamic acid catabolism (hughes2017pseudomonasputidaf1 pages 3-4, mohan2025biotransformationofferulic pages 5-10). This is functionally distinct from both *o*-succinylbenzoate-CoA ligase (MenE, EC 6.2.1.26) and medium-chain fatty acid-CoA ligase. Two possible issues exist:

1. **If the subfamily truly contains Fcs orthologs**, the appropriate term is **ferulate-CoA ligase activity** (or 4-coumarate-CoA ligase activity, GO:0016207, depending on substrate breadth), and the subfamily name should be corrected.
2. **If the subfamily contains both MenE and Fcs orthologs**, it may need splitting, as these enzymes act on chemically distinct aromatic substrates in different metabolic pathways (menaquinone biosynthesis vs. hydroxycinnamic acid catabolism) (meganathan2009biosynthesisofmenaquinone pages 8-9, boersch2018menaquinonebiosynthesisinhibition pages 2-3, hughes2017pseudomonasputidaf1 pages 3-4).

**Subfamilies that would be mis-annotated by GO:0031956 at any node above them:**
- MenE/*o*-succinylbenzoate-CoA ligase branches (should be GO:0008756)
- Fcs/feruloyl-CoA synthetase branches (should be ferulate-CoA ligase or related)
- 4CL/4-coumarate:CoA ligase branches (should be GO:0016207)
- Acetyl-CoA synthetase branches (should be GO:0003987)
- Long-chain acyl-CoA synthetase branches (should be GO:0004467)
- Any luciferase branches (should be GO:0008218)
- Any NRPS adenylation domain branches (should not receive a CoA-ligase term at all)

## Evidence and Gaps

### Key Citations

- **Gulick 2009** (ACS Chem Biol, PMID: 19610673): Definitive review of ANL superfamily domain alternation mechanism. Establishes the three-subfamily framework and conserved catalytic strategy (gulick2009conformationaldynamicsin pages 2-4, gulick2009conformationaldynamicsin pages 1-2, gulick2009conformationaldynamicsin pages 4-5, gulick2009conformationaldynamicsin pages 7-8, gulick2009conformationaldynamicsin pages 5-7, gulick2009conformationaldynamicsin pages 12-14).
- **Khurana et al. 2010** (BMC Bioinformatics, PMID: 20105318): Computational prediction of substrate specificity across six subfamilies using 15 SDRs; demonstrated subfamily-level active-site conservation patterns (khurana2010genomescaleprediction pages 1-3, khurana2010genomescaleprediction pages 3-4, khurana2010genomescaleprediction pages 4-6, khurana2010genomescaleprediction pages 13-14, khurana2010genomescaleprediction pages 6-8, khurana2010genomescaleprediction pages 10-13).
- **Watkins et al. 2007** (J Lipid Res, PMID: 17908991): Identified 26 human ACS genes across ACSS/ACSM/ACSL/ACSVL/ACSBG/ACSF subfamilies with distinct chain-length preferences (watkins2007evidencefor26 pages 12-13, watkins2007evidencefor26 pages 4-5, watkins2007evidencefor26 pages 7-8, watkins2007evidencefor26 pages 5-7, watkins2007evidencefor26 pages 8-9, watkins2007evidencefor26 pages 2-3).
- **Lux et al. 2019** (J Antibiotics, PMID: 30850720): Overview of nine structural classes of adenylate-forming enzymes and their inhibitors (lux2019targetingadenylateformingenzymes pages 2-4).
- **Evans et al. 2019** (Biochemistry, PMID: 30835445): Crystal structure of MenE with OSB-AMS; identifies catalytic residues K437, R195, D336 (evans2019structurebaseddesignsynthesis pages 8-10, evans2019structurebaseddesignsynthesis pages 17-22, evans2019structurebaseddesignsynthesis pages 1-3, evans2019structurebaseddesignsynthesis pages 3-5).
- **Meganathan & Kwon 2009** (EcoSal Plus, PMID: 26443769): MenE characterization as homotetramer with Km for OSB = 16 µM; essential His341 in ATP-binding region (meganathan2009biosynthesisofmenaquinone pages 8-9).
- **Boersch et al. 2018** (RSC Advances): MenE Bi Uni Uni Bi ping-pong mechanism via OSB-AMP intermediate; antibiotic target review (boersch2018menaquinonebiosynthesisinhibition pages 2-3, boersch2018menaquinonebiosynthesisinhibition pages 1-2).
- **Li & Nair 2015** (Structure, PMID: 26439767): 4CL2 crystal structures in adenylation and thioester-forming conformations; Val341 deletion expands substrate scope (li2015structuralbasisfor pages 3-4, li2015structuralbasisfor pages 1-3, li2015structuralbasisfor pages 7-8, li2015structuralbasisfor pages 5-6, li2015structuralbasisfor pages 10-11).
- **Hughes et al. 2017** (Microbiology, PMID: 28956771): Fcs gene essential for hydroxycinnamic acid catabolism in *P. putida* F1 (hughes2017pseudomonasputidaf1 pages 3-4, hughes2017pseudomonasputidaf1 pages 1-2).
- **Mohan et al. 2025** (Biomass Conv Bioref): Fcs (EC 6.2.1.34) in ferulic acid-to-vanillin biotransformation; requires ATP, Mg²⁺, CoASH (mohan2025biotransformationofferulic pages 5-10, mohan2025biotransformationofferulic pages 10-12, mohan2025biotransformationofferulic pages 1-2).

### Explicit Uncertainties

1. **PTHR43201 subfamily composition is not fully verified here.** The exact membership of PTHR43201 — whether it includes luciferase and NRPS branches or only acyl/aryl-CoA synthetases — was not computationally checked against the PANTHER database in this audit. The scope of the family-level term recommendation depends on this.

2. **SF32 clade composition is uncertain.** The discrepancy between the subfamily label ("2-succinylbenzoate--CoA ligase") and the representative member's biochemical characterization (feruloyl-CoA synthetase) could reflect: (a) mixed membership in the clade, (b) mislabeling of the subfamily name, (c) closer phylogenetic relationship between fcs and MenE orthologs than expected, or (d) dual functionality that has not been tested. Curator review of the SF32 clade composition using sequence alignment and SDR analysis is needed.

3. **Chen et al. 2016 and Chen et al. 2017** crystal structures of *B. subtilis* MenE (PMID: 27882793 and PMID: 28634234) were identified but not obtainable for this analysis. These would provide key catalytic residue information for the MenE subfamily specifically.

4. **Kim et al. 2008** (PMID: 18363783) characterizing Arabidopsis AAE14 as *o*-succinylbenzoyl-CoA ligase essential for phylloquinone synthesis was not obtainable; this would clarify plant MenE ortholog function.

5. **No direct PTHR43201 subfamily enumeration was performed.** A programmatic query of the PANTHER database to list all SF nodes under PTHR43201 and their associated GO terms was not executed and would strengthen the audit.

References

1. (gulick2009conformationaldynamicsin pages 2-4): Andrew M. Gulick. Conformational dynamics in the acyl-coa synthetases, adenylation domains of non-ribosomal peptide synthetases, and firefly luciferase. ACS chemical biology, 4 10:811-27, Oct 2009. URL: https://doi.org/10.1021/cb900156h, doi:10.1021/cb900156h. This article has 548 citations and is from a domain leading peer-reviewed journal.

2. (gulick2009conformationaldynamicsin pages 1-2): Andrew M. Gulick. Conformational dynamics in the acyl-coa synthetases, adenylation domains of non-ribosomal peptide synthetases, and firefly luciferase. ACS chemical biology, 4 10:811-27, Oct 2009. URL: https://doi.org/10.1021/cb900156h, doi:10.1021/cb900156h. This article has 548 citations and is from a domain leading peer-reviewed journal.

3. (gulick2009conformationaldynamicsin pages 4-5): Andrew M. Gulick. Conformational dynamics in the acyl-coa synthetases, adenylation domains of non-ribosomal peptide synthetases, and firefly luciferase. ACS chemical biology, 4 10:811-27, Oct 2009. URL: https://doi.org/10.1021/cb900156h, doi:10.1021/cb900156h. This article has 548 citations and is from a domain leading peer-reviewed journal.

4. (gulick2009conformationaldynamicsin pages 5-7): Andrew M. Gulick. Conformational dynamics in the acyl-coa synthetases, adenylation domains of non-ribosomal peptide synthetases, and firefly luciferase. ACS chemical biology, 4 10:811-27, Oct 2009. URL: https://doi.org/10.1021/cb900156h, doi:10.1021/cb900156h. This article has 548 citations and is from a domain leading peer-reviewed journal.

5. (lux2019targetingadenylateformingenzymes pages 2-4): Michaelyn C. Lux, Lisa C. Standke, and Derek S. Tan. Targeting adenylate-forming enzymes with designed sulfonyladenosine inhibitors. The Journal of Antibiotics, 72:325-349, Apr 2019. URL: https://doi.org/10.1038/s41429-019-0171-2, doi:10.1038/s41429-019-0171-2. This article has 55 citations.

6. (gulick2009conformationaldynamicsin pages 7-8): Andrew M. Gulick. Conformational dynamics in the acyl-coa synthetases, adenylation domains of non-ribosomal peptide synthetases, and firefly luciferase. ACS chemical biology, 4 10:811-27, Oct 2009. URL: https://doi.org/10.1021/cb900156h, doi:10.1021/cb900156h. This article has 548 citations and is from a domain leading peer-reviewed journal.

7. (khurana2010genomescaleprediction pages 1-3): Pankaj Khurana, Rajesh S Gokhale, and Debasisa Mohanty. Genome scale prediction of substrate specificity for acyl adenylate superfamily of enzymes based on active site residue profiles. BMC Bioinformatics, 11:57-57, Jan 2010. URL: https://doi.org/10.1186/1471-2105-11-57, doi:10.1186/1471-2105-11-57. This article has 45 citations and is from a peer-reviewed journal.

8. (khurana2010genomescaleprediction pages 3-4): Pankaj Khurana, Rajesh S Gokhale, and Debasisa Mohanty. Genome scale prediction of substrate specificity for acyl adenylate superfamily of enzymes based on active site residue profiles. BMC Bioinformatics, 11:57-57, Jan 2010. URL: https://doi.org/10.1186/1471-2105-11-57, doi:10.1186/1471-2105-11-57. This article has 45 citations and is from a peer-reviewed journal.

9. (khurana2010genomescaleprediction pages 4-6): Pankaj Khurana, Rajesh S Gokhale, and Debasisa Mohanty. Genome scale prediction of substrate specificity for acyl adenylate superfamily of enzymes based on active site residue profiles. BMC Bioinformatics, 11:57-57, Jan 2010. URL: https://doi.org/10.1186/1471-2105-11-57, doi:10.1186/1471-2105-11-57. This article has 45 citations and is from a peer-reviewed journal.

10. (khurana2010genomescaleprediction pages 6-8): Pankaj Khurana, Rajesh S Gokhale, and Debasisa Mohanty. Genome scale prediction of substrate specificity for acyl adenylate superfamily of enzymes based on active site residue profiles. BMC Bioinformatics, 11:57-57, Jan 2010. URL: https://doi.org/10.1186/1471-2105-11-57, doi:10.1186/1471-2105-11-57. This article has 45 citations and is from a peer-reviewed journal.

11. (khurana2010genomescaleprediction pages 10-13): Pankaj Khurana, Rajesh S Gokhale, and Debasisa Mohanty. Genome scale prediction of substrate specificity for acyl adenylate superfamily of enzymes based on active site residue profiles. BMC Bioinformatics, 11:57-57, Jan 2010. URL: https://doi.org/10.1186/1471-2105-11-57, doi:10.1186/1471-2105-11-57. This article has 45 citations and is from a peer-reviewed journal.

12. (watkins2007evidencefor26 pages 12-13): Paul A. Watkins, Dony Maiguel, Zhenzhen Jia, and Jonathan Pevsner. Evidence for 26 distinct acyl-coenzyme a synthetase genes in the human genomes⃞s⃞ the online version of this article (available at http://www.jlr.org) contains supplementary data in the form of 3 tables. published, jlr papers in press, august 30, 2007. Journal of Lipid Research, 48:2736-2750, Dec 2007. URL: https://doi.org/10.1194/jlr.m700378-jlr200, doi:10.1194/jlr.m700378-jlr200. This article has 464 citations and is from a peer-reviewed journal.

13. (watkins2007evidencefor26 pages 5-7): Paul A. Watkins, Dony Maiguel, Zhenzhen Jia, and Jonathan Pevsner. Evidence for 26 distinct acyl-coenzyme a synthetase genes in the human genomes⃞s⃞ the online version of this article (available at http://www.jlr.org) contains supplementary data in the form of 3 tables. published, jlr papers in press, august 30, 2007. Journal of Lipid Research, 48:2736-2750, Dec 2007. URL: https://doi.org/10.1194/jlr.m700378-jlr200, doi:10.1194/jlr.m700378-jlr200. This article has 464 citations and is from a peer-reviewed journal.

14. (li2015structuralbasisfor pages 3-4): Zhi Li and Satish K. Nair. Structural basis for specificity and flexibility in a plant 4-coumarate:coa ligase. Structure, 23:2032-2042, Nov 2015. URL: https://doi.org/10.1016/j.str.2015.08.012, doi:10.1016/j.str.2015.08.012. This article has 93 citations and is from a domain leading peer-reviewed journal.

15. (li2015structuralbasisfor pages 1-3): Zhi Li and Satish K. Nair. Structural basis for specificity and flexibility in a plant 4-coumarate:coa ligase. Structure, 23:2032-2042, Nov 2015. URL: https://doi.org/10.1016/j.str.2015.08.012, doi:10.1016/j.str.2015.08.012. This article has 93 citations and is from a domain leading peer-reviewed journal.

16. (li2015structuralbasisfor pages 5-6): Zhi Li and Satish K. Nair. Structural basis for specificity and flexibility in a plant 4-coumarate:coa ligase. Structure, 23:2032-2042, Nov 2015. URL: https://doi.org/10.1016/j.str.2015.08.012, doi:10.1016/j.str.2015.08.012. This article has 93 citations and is from a domain leading peer-reviewed journal.

17. (li2015structuralbasisfor pages 7-8): Zhi Li and Satish K. Nair. Structural basis for specificity and flexibility in a plant 4-coumarate:coa ligase. Structure, 23:2032-2042, Nov 2015. URL: https://doi.org/10.1016/j.str.2015.08.012, doi:10.1016/j.str.2015.08.012. This article has 93 citations and is from a domain leading peer-reviewed journal.

18. (meganathan2009biosynthesisofmenaquinone pages 8-9): R. Meganathan and Ohsuk Kwon. Biosynthesis of menaquinone (vitamin k <sub>2</sub> ) and ubiquinone (coenzyme q). EcoSal Plus, Dec 2009. URL: https://doi.org/10.1128/ecosalplus.3.6.3.3, doi:10.1128/ecosalplus.3.6.3.3. This article has 113 citations.

19. (boersch2018menaquinonebiosynthesisinhibition pages 2-3): M. Boersch, Santosh Rudrawar, Gary D. Grant, and M. Zunk. Menaquinone biosynthesis inhibition: a review of advancements toward a new antibiotic mechanism. RSC Advances, 8:5099-5105, Jan 2018. URL: https://doi.org/10.1039/c7ra12950e, doi:10.1039/c7ra12950e. This article has 71 citations and is from a peer-reviewed journal.

20. (evans2019structurebaseddesignsynthesis pages 8-10): Christopher E. Evans, Yuanyuan Si, Joe S. Matarlo, Yue Yin, Jarrod B. French, Peter J. Tonge, and Derek S. Tan. Structure-based design, synthesis, and biological evaluation of non-acyl sulfamate inhibitors of the adenylate-forming enzyme mene. Biochemistry, 58:1918-1930, Mar 2019. URL: https://doi.org/10.1021/acs.biochem.9b00003, doi:10.1021/acs.biochem.9b00003. This article has 9 citations and is from a peer-reviewed journal.

21. (evans2019structurebaseddesignsynthesis pages 1-3): Christopher E. Evans, Yuanyuan Si, Joe S. Matarlo, Yue Yin, Jarrod B. French, Peter J. Tonge, and Derek S. Tan. Structure-based design, synthesis, and biological evaluation of non-acyl sulfamate inhibitors of the adenylate-forming enzyme mene. Biochemistry, 58:1918-1930, Mar 2019. URL: https://doi.org/10.1021/acs.biochem.9b00003, doi:10.1021/acs.biochem.9b00003. This article has 9 citations and is from a peer-reviewed journal.

22. (hughes2017pseudomonasputidaf1 pages 3-4): Jonathan G. Hughes, Xiangsheng Zhang, Juanito V. Parales, Jayna L. Ditty, and Rebecca E. Parales. Pseudomonas putida f1 uses energy taxis to sense hydroxycinnamic acids. Oct 2017. URL: https://doi.org/10.1099/mic.0.000533, doi:10.1099/mic.0.000533. This article has 13 citations and is from a peer-reviewed journal.

23. (mohan2025biotransformationofferulic pages 5-10): Harsha Mohan, Febiya Anna Fedin, and Jayachandran Kochupurackal. Biotransformation of ferulic acid to vanillin via vanillic acid by a single isolate burkholderia cenocepacia vw2. Biomass Conversion and Biorefinery, Feb 2025. URL: https://doi.org/10.1007/s13399-025-06646-x, doi:10.1007/s13399-025-06646-x. This article has 1 citations and is from a peer-reviewed journal.

24. (mohan2025biotransformationofferulic pages 10-12): Harsha Mohan, Febiya Anna Fedin, and Jayachandran Kochupurackal. Biotransformation of ferulic acid to vanillin via vanillic acid by a single isolate burkholderia cenocepacia vw2. Biomass Conversion and Biorefinery, Feb 2025. URL: https://doi.org/10.1007/s13399-025-06646-x, doi:10.1007/s13399-025-06646-x. This article has 1 citations and is from a peer-reviewed journal.

25. (hughes2017pseudomonasputidaf1 pages 1-2): Jonathan G. Hughes, Xiangsheng Zhang, Juanito V. Parales, Jayna L. Ditty, and Rebecca E. Parales. Pseudomonas putida f1 uses energy taxis to sense hydroxycinnamic acids. Oct 2017. URL: https://doi.org/10.1099/mic.0.000533, doi:10.1099/mic.0.000533. This article has 13 citations and is from a peer-reviewed journal.

26. (priyadarshan2018fattyacylampligases pages 1-2): Kinatukara Priyadarshan and Rajan Sankaranarayanan. Fatty acyl-amp ligases as mechanistic variants of anl superfamily and molecular determinants dictating substrate specificities. Journal of the Indian Institute of Science, 98:261-272, Jul 2018. URL: https://doi.org/10.1007/s41745-018-0084-2, doi:10.1007/s41745-018-0084-2. This article has 13 citations.

27. (gulick2009conformationaldynamicsin pages 12-14): Andrew M. Gulick. Conformational dynamics in the acyl-coa synthetases, adenylation domains of non-ribosomal peptide synthetases, and firefly luciferase. ACS chemical biology, 4 10:811-27, Oct 2009. URL: https://doi.org/10.1021/cb900156h, doi:10.1021/cb900156h. This article has 548 citations and is from a domain leading peer-reviewed journal.

28. (khurana2010genomescaleprediction pages 13-14): Pankaj Khurana, Rajesh S Gokhale, and Debasisa Mohanty. Genome scale prediction of substrate specificity for acyl adenylate superfamily of enzymes based on active site residue profiles. BMC Bioinformatics, 11:57-57, Jan 2010. URL: https://doi.org/10.1186/1471-2105-11-57, doi:10.1186/1471-2105-11-57. This article has 45 citations and is from a peer-reviewed journal.

29. (watkins2007evidencefor26 pages 4-5): Paul A. Watkins, Dony Maiguel, Zhenzhen Jia, and Jonathan Pevsner. Evidence for 26 distinct acyl-coenzyme a synthetase genes in the human genomes⃞s⃞ the online version of this article (available at http://www.jlr.org) contains supplementary data in the form of 3 tables. published, jlr papers in press, august 30, 2007. Journal of Lipid Research, 48:2736-2750, Dec 2007. URL: https://doi.org/10.1194/jlr.m700378-jlr200, doi:10.1194/jlr.m700378-jlr200. This article has 464 citations and is from a peer-reviewed journal.

30. (watkins2007evidencefor26 pages 7-8): Paul A. Watkins, Dony Maiguel, Zhenzhen Jia, and Jonathan Pevsner. Evidence for 26 distinct acyl-coenzyme a synthetase genes in the human genomes⃞s⃞ the online version of this article (available at http://www.jlr.org) contains supplementary data in the form of 3 tables. published, jlr papers in press, august 30, 2007. Journal of Lipid Research, 48:2736-2750, Dec 2007. URL: https://doi.org/10.1194/jlr.m700378-jlr200, doi:10.1194/jlr.m700378-jlr200. This article has 464 citations and is from a peer-reviewed journal.

31. (watkins2007evidencefor26 pages 8-9): Paul A. Watkins, Dony Maiguel, Zhenzhen Jia, and Jonathan Pevsner. Evidence for 26 distinct acyl-coenzyme a synthetase genes in the human genomes⃞s⃞ the online version of this article (available at http://www.jlr.org) contains supplementary data in the form of 3 tables. published, jlr papers in press, august 30, 2007. Journal of Lipid Research, 48:2736-2750, Dec 2007. URL: https://doi.org/10.1194/jlr.m700378-jlr200, doi:10.1194/jlr.m700378-jlr200. This article has 464 citations and is from a peer-reviewed journal.

32. (watkins2007evidencefor26 pages 2-3): Paul A. Watkins, Dony Maiguel, Zhenzhen Jia, and Jonathan Pevsner. Evidence for 26 distinct acyl-coenzyme a synthetase genes in the human genomes⃞s⃞ the online version of this article (available at http://www.jlr.org) contains supplementary data in the form of 3 tables. published, jlr papers in press, august 30, 2007. Journal of Lipid Research, 48:2736-2750, Dec 2007. URL: https://doi.org/10.1194/jlr.m700378-jlr200, doi:10.1194/jlr.m700378-jlr200. This article has 464 citations and is from a peer-reviewed journal.

33. (evans2019structurebaseddesignsynthesis pages 17-22): Christopher E. Evans, Yuanyuan Si, Joe S. Matarlo, Yue Yin, Jarrod B. French, Peter J. Tonge, and Derek S. Tan. Structure-based design, synthesis, and biological evaluation of non-acyl sulfamate inhibitors of the adenylate-forming enzyme mene. Biochemistry, 58:1918-1930, Mar 2019. URL: https://doi.org/10.1021/acs.biochem.9b00003, doi:10.1021/acs.biochem.9b00003. This article has 9 citations and is from a peer-reviewed journal.

34. (evans2019structurebaseddesignsynthesis pages 3-5): Christopher E. Evans, Yuanyuan Si, Joe S. Matarlo, Yue Yin, Jarrod B. French, Peter J. Tonge, and Derek S. Tan. Structure-based design, synthesis, and biological evaluation of non-acyl sulfamate inhibitors of the adenylate-forming enzyme mene. Biochemistry, 58:1918-1930, Mar 2019. URL: https://doi.org/10.1021/acs.biochem.9b00003, doi:10.1021/acs.biochem.9b00003. This article has 9 citations and is from a peer-reviewed journal.

35. (boersch2018menaquinonebiosynthesisinhibition pages 1-2): M. Boersch, Santosh Rudrawar, Gary D. Grant, and M. Zunk. Menaquinone biosynthesis inhibition: a review of advancements toward a new antibiotic mechanism. RSC Advances, 8:5099-5105, Jan 2018. URL: https://doi.org/10.1039/c7ra12950e, doi:10.1039/c7ra12950e. This article has 71 citations and is from a peer-reviewed journal.

36. (li2015structuralbasisfor pages 10-11): Zhi Li and Satish K. Nair. Structural basis for specificity and flexibility in a plant 4-coumarate:coa ligase. Structure, 23:2032-2042, Nov 2015. URL: https://doi.org/10.1016/j.str.2015.08.012, doi:10.1016/j.str.2015.08.012. This article has 93 citations and is from a domain leading peer-reviewed journal.

37. (mohan2025biotransformationofferulic pages 1-2): Harsha Mohan, Febiya Anna Fedin, and Jayachandran Kochupurackal. Biotransformation of ferulic acid to vanillin via vanillic acid by a single isolate burkholderia cenocepacia vw2. Biomass Conversion and Biorefinery, Feb 2025. URL: https://doi.org/10.1007/s13399-025-06646-x, doi:10.1007/s13399-025-06646-x. This article has 1 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](PTHR43201-function-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PTHR43201-function-falcon_artifacts/artifact-01.md)