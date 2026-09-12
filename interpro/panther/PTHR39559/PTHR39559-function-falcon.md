---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-24T04:45:40.989123'
end_time: '2026-06-24T05:14:25.308972'
duration_seconds: 1724.32
template_file: templates/treegrafter_family_function.md
template_variables:
  family_id: PTHR39559
  family_name: ISOCITRATE DEHYDROGENASE KINASE/PHOSPHATASE (family)
  subfamily: PTHR39559:SF1 ISOCITRATE DEHYDROGENASE KINASE/PHOSPHATASE
  gene_symbol: aceK
  uniprot: Q88EA1
  organism: PSEPK
  taxon_label: PSEPK
  propagated_term: phosphoprotein phosphatase activity (GO:0004721)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 24
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: PTHR39559-function-falcon_artifacts/artifact-00.md
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

- **PANTHER family:** PTHR39559 — ISOCITRATE DEHYDROGENASE KINASE/PHOSPHATASE (family)
- **Subfamily of interest:** PTHR39559:SF1 ISOCITRATE DEHYDROGENASE KINASE/PHOSPHATASE
- **Representative member:** aceK (Q88EA1), PSEPK / PSEPK
- **GO term currently propagated at/near this node:** phosphoprotein phosphatase activity (GO:0004721)

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
3. **Subfamily of interest.** Where does PTHR39559:SF1 ISOCITRATE DEHYDROGENASE KINASE/PHOSPHATASE sit — does it carry the
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

- **PANTHER family:** PTHR39559 — ISOCITRATE DEHYDROGENASE KINASE/PHOSPHATASE (family)
- **Subfamily of interest:** PTHR39559:SF1 ISOCITRATE DEHYDROGENASE KINASE/PHOSPHATASE
- **Representative member:** aceK (Q88EA1), PSEPK / PSEPK
- **GO term currently propagated at/near this node:** phosphoprotein phosphatase activity (GO:0004721)

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
3. **Subfamily of interest.** Where does PTHR39559:SF1 ISOCITRATE DEHYDROGENASE KINASE/PHOSPHATASE sit — does it carry the
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


# PANTHER Family PTHR39559 — Isocitrate Dehydrogenase Kinase/Phosphatase: Function Characterization and TreeGrafter Granularity Audit

## Family Function Summary

Isocitrate dehydrogenase kinase/phosphatase (AceK, also known as IDHK/P) is a bifunctional enzyme that catalyzes both the phosphorylation and dephosphorylation of isocitrate dehydrogenase (IDH/ICD) from a single active site within its C-terminal kinase domain (KD) (zheng2012structuralandmechanistic pages 1-3). The enzyme was the first identified example of prokaryotic protein phosphorylation and serves as the metabolic switch between the tricarboxylic acid (TCA) cycle and the glyoxylate bypass pathway in Gram-negative bacteria (zheng2012structuralandmechanistic pages 1-3, rangwala2022kinasesondouble pages 14-15). Structurally, AceK comprises two domains: (1) a C-terminal kinase domain (~residues 307–574 in *E. coli*) that adopts an atypical protein kinase fold resembling eukaryotic Ser/Thr and Tyr protein kinases (ePKs), containing a bilobal architecture with ATP bound at the interface (zheng2012structuralandmechanistic pages 3-4), and (2) an N-terminal regulatory domain (RD) with a unique protein fold that has no structural homologues and contains allosteric binding pockets for metabolite regulators such as AMP (zheng2012structuralandmechanistic pages 1-3, zheng2012structuralandmechanistic pages 4-6). The conserved catalytic machinery includes the catalytic triad (Asp457, Asn462, Asp475), a P-loop motif (315-APGIRG-320), an invariant ATP-binding Lys336, and the phosphatase-critical DXDX(T/V) motif residues Asp475 (nucleophile) and Asp477 (general acid), which show sequence similarity to the haloacid dehalogenase (HAD) phosphatase superfamily (zheng2012structuralandmechanistic pages 4-6, zheng2012structuralandmechanistic pages 6-7). Kinase, phosphatase, and ATPase activities all share the same active site, with switching between kinase and phosphatase modes controlled by the conformational state of Loop β3αC and allosteric regulation by AMP and other metabolites (zheng2012structuralandmechanistic pages 7-9, zheng2012structuralandmechanistic pages 10-11). The enzyme phosphorylates IDH at Ser113 (Ser115 in *Pseudomonas*), completely inactivating it by electrostatically repulsing the isocitrate substrate (crousilles2018threeenzymesand pages 1-3). AceK is found exclusively in Gram-negative bacteria (zheng2012structuralandmechanistic pages 11-13, rangwala2022kinasesondouble pages 14-15). The relevant EC numbers are EC 2.7.11.5 ([Isocitrate dehydrogenase (NADP+)] kinase) and EC 3.1.3.— (protein phosphatase activity on phospho-IDH).

## Subfamily Divergence Table

| Subgroup | Representative Member(s) with citations | Molecular Function | Substrate/Specialization | Catalytic Residues Intact? | GO MF Term that Fits | Notes |
|---|---|---|---|---|---|---|
| Canonical AceK / family-wide Gram-negative bacterial orthologs | *Escherichia coli* AceK; family overview also lists AceK in *Klebsiella*, *Pseudomonas*, *Yersinia*, *Shigella*, *Salmonella* (rangwala2022kinasesondouble pages 14-15, zheng2012structuralandmechanistic pages 1-3) | Bifunctional protein kinase/phosphatase acting on isocitrate dehydrogenase (IDH/ICD) from a single active site | Reversible phosphorylation cycle of bacterial IDH at the conserved phosphoserine site (Ser113 in *E. coli* ICD); metabolic switch between TCA cycle and glyoxylate shunt (zheng2012structuralandmechanistic pages 1-3, miller2000locationsofthe pages 1-2) | Yes in characterized AceK enzymes: ATP-site Lys336; kinase catalytic residues including Asp457/Asn462; phosphatase-active DXDX(T/V)-related residues Asp475/Asp477 (zheng2012structuralandmechanistic pages 3-4, zheng2012structuralandmechanistic pages 6-7, zheng2012structuralandmechanistic pages 4-6) | More appropriate combined family description: **isocitrate dehydrogenase kinase/phosphatase activity**; if forced to choose a single existing propagated term, **phosphoprotein phosphatase activity (GO:0004721)** is incomplete because it omits the equally conserved kinase function (rangwala2022kinasesondouble pages 14-15, zheng2012structuralandmechanistic pages 1-3) | Core family is functionally homogeneous in current evidence: all characterized natural members are bifunctional, not phosphatase-only or kinase-only. Restriction to Gram-negative bacteria reflects substrate-recognition constraints, not divergence of core chemistry (zheng2012structuralandmechanistic pages 11-13, dolan2018theglyoxylateshunt pages 4-6) |
| *Pseudomonas* AceK branch | *Pseudomonas aeruginosa* PaIDH K/P; *P. putida* AceK represented in family/subfamily and supported by genus-level AceK distribution (rangwala2022kinasesondouble pages 14-15, chen2023twodifferentisocitrate pages 1-2) | Same bifunctional IDH kinase/phosphatase activity | In *P. aeruginosa*, PaIDH K/P phosphorylates PaIDH1 at Ser115 and reduces activity by ~80%; phosphatase activity is stimulated by multiple metabolites including fumarate, succinate, pyruvate, oxaloacetate, AMP/ADP (chen2023twodifferentisocitrate pages 9-10, crousilles2018threeenzymesand pages 5-7, crousilles2018threeenzymesand pages 3-5) | Presumed intact in natural *Pseudomonas* AceK orthologs; no evidence of loss of catalytic residues or natural separation of activities (rangwala2022kinasesondouble pages 14-15, dolan2018theglyoxylateshunt pages 4-6) | Same as family: **isocitrate dehydrogenase kinase/phosphatase activity** | Species-specific regulatory tuning exists: *P. aeruginosa* AceK does not fully inactivate its ICD as completely as *E. coli* AceK, but this is regulatory divergence, not a change in core enzymatic function (crousilles2018threeenzymesand pages 3-5, dolan2018theglyoxylateshunt pages 11-12) |
| PTHR39559:SF1 (named the same as family) | PTHR39559:SF1 representative Q88EA1 / AceK from *Pseudomonas putida*; mechanistic inference anchored by characterized AceK orthologs and *Pseudomonas* exemplars (zheng2012structuralandmechanistic pages 1-3, rangwala2022kinasesondouble pages 14-15) | Conserved AceK bifunctional kinase/phosphatase activity | Expected reversible control of isocitrate dehydrogenase at the TCA/glyoxylate branch point in Gram-negative metabolism (zheng2012structuralandmechanistic pages 1-3, rangwala2022kinasesondouble pages 14-15) | Expected yes; no evidence that SF1 is catalytically diverged from characterized AceK orthologs (zheng2012structuralandmechanistic pages 1-3, rangwala2022kinasesondouble pages 14-15) | Same as family: **isocitrate dehydrogenase kinase/phosphatase activity** | SF1 shares the same name as the family and no distinct neofunctionalized branch was identified. Current propagated **GO:0004721 phosphoprotein phosphatase activity** is an under-granular partial annotation, not a wrong-direction branch-specific annotation (rangwala2022kinasesondouble pages 14-15, zheng2012structuralandmechanistic pages 1-3) |
| Engineered or mutationally separated activity states (not natural subfamilies) | AceK Asp477 mutants (e.g., D477N, D477A) retain kinase but lose phosphatase activity (zheng2012structuralandmechanistic pages 6-7) | Experimentally separable kinase-only state | Demonstrates mechanistic partitioning within one active site rather than natural subfamily divergence (zheng2012structuralandmechanistic pages 6-7, zheng2012structuralandmechanistic pages 7-9) | No: phosphatase catalytic machinery disrupted at Asp477 while kinase activity persists (zheng2012structuralandmechanistic pages 6-7) | No natural-family GO assignment should be based on these mutants | Important curation note: these data show why propagating only phosphatase activity underspecifies the family, but they do **not** support existence of natural phosphatase-dead subfamilies within PTHR39559 (zheng2012structuralandmechanistic pages 6-7) |


*Table: This table summarizes the major functional groupings relevant to PTHR39559 and shows that characterized natural members are consistently bifunctional AceK enzymes. It is useful for GO granularity review because it indicates that phosphatase-only propagation under-annotates a functionally homogeneous family.*

## Homogeneous vs. Heterogeneous Verdict

**The PTHR39559 family is functionally homogeneous.** All characterized natural members of this family—spanning *Escherichia coli*, *Pseudomonas aeruginosa*, *Pseudomonas putida*, *Klebsiella*, *Salmonella*, *Shigella*, *Yersinia*, and *Burkholderia* species—are bifunctional isocitrate dehydrogenase kinase/phosphatases that operate through the same single active site with conserved catalytic residues (zheng2012structuralandmechanistic pages 11-13, rangwala2022kinasesondouble pages 14-15). No natural subfamily members have been documented to have lost either kinase or phosphatase activity; no pseudo-enzymes have been identified within this family (dolan2018theglyoxylateshunt pages 4-6). While species-specific differences exist in regulatory sensitivity (e.g., *P. aeruginosa* AceK achieves ~75% maximal IDH inhibition compared to near-complete inactivation by *E. coli* AceK), these represent tuning of allosteric regulatory responses rather than divergence in core catalytic function (crousilles2018threeenzymesand pages 3-5). Mutagenesis studies demonstrate that the two activities *can* be experimentally separated (e.g., D477N/D477A mutations retain kinase but abolish phosphatase), but this does not reflect natural functional divergence within the family (zheng2012structuralandmechanistic pages 6-7).

A single family-level GO MF term capturing the bifunctional activity is safe to propagate across this family. The currently propagated term **phosphoprotein phosphatase activity (GO:0004721)** is not incorrect per se, but it is **incomplete and under-annotating**: it captures only one of the two inseparable enzymatic activities that define this family. Propagating GO:0004721 alone would not mis-annotate any branch (no branch lacks phosphatase activity), but it would omit the equally conserved and functionally essential kinase activity from all members.

## Granularity Leads for Curation

### Family-level GO MF term recommendation
The most accurate family-level annotation would be a combined term reflecting the bifunctional nature:
- **[Isocitrate dehydrogenase (NADP+)] kinase activity (GO:0004427)** — capturing the kinase function
- **Phosphoprotein phosphatase activity (GO:0004721)** — capturing the phosphatase function
- Both should be propagated at the family level, as all characterized members possess both activities from the same active site (rangwala2022kinasesondouble pages 14-15, miller2000locationsofthe pages 1-2).

Ideally, a composite or more specific term such as **"isocitrate dehydrogenase kinase/phosphatase activity"** would best represent the conserved molecular function, if such a term exists or could be created in GO.

### Subfamily-level (PTHR39559:SF1) GO MF term recommendation
SF1 shares the same name as the family ("ISOCITRATE DEHYDROGENASE KINASE/PHOSPHATASE") and the representative member Q88EA1 (AceK from *Pseudomonas putida* KT2440) is expected to carry the full conserved bifunctional activity based on genus-level evidence from *P. aeruginosa* (chen2023twodifferentisocitrate pages 9-10, chen2023twodifferentisocitrate pages 1-2) and metabolic/transcriptomic studies in *P. putida* (dolan2018theglyoxylateshunt pages 11-12, dolan2018theglyoxylateshunt pages 10-11). The same dual GO MF annotation (GO:0004427 + GO:0004721) is appropriate at the subfamily level.

### Over-annotation assessment
The currently propagated term **GO:0004721 (phosphoprotein phosphatase activity)** is:
- **Not an over-annotation** — it is not false for any known member
- **An under-annotation** — it omits the kinase activity (GO:0004427) that is equally conserved and mechanistically inseparable
- **No subfamilies are mis-annotated** by this term; rather, all subfamilies are *incompletely* annotated

No subfamily within PTHR39559 requires a narrower or different term than the family-level annotation. The family is sufficiently narrow and homogeneous that family-level propagation of both GO:0004427 and GO:0004721 is safe across all branches.

## Evidence and Gaps

### Key Citations
- **Zheng, Yates & Jia (2012)** Phil. Trans. R. Soc. B 367:2656–2668. PMID: 22889910. Comprehensive structural and mechanistic review of AceK, including crystal structure, catalytic residues, and switching mechanism (zheng2012structuralandmechanistic pages 7-9, zheng2012structuralandmechanistic pages 6-7, zheng2012structuralandmechanistic pages 3-4, zheng2012structuralandmechanistic pages 4-6, zheng2012structuralandmechanistic pages 10-11, zheng2012structuralandmechanistic pages 1-3, zheng2012structuralandmechanistic pages 11-13).
- **Zheng & Jia (2010)** Nature 465:961–965. PMID: 20505668. First crystal structure of AceK (unobtainable but cited in evidence).
- **Rangwala et al. (2022)** Biomolecules 12:685. PMID: 35625104. Review of bifunctional kinases including IDHK/P (rangwala2022kinasesondouble pages 14-15).
- **Chen et al. (2023)** Int. J. Mol. Sci. 24:14985. PMID: 37834426. Characterization of *P. aeruginosa* IDH K/P showing phosphorylation of PaIDH1 at Ser115 (chen2023twodifferentisocitrate pages 9-10, chen2023twodifferentisocitrate pages 1-2).
- **Crousilles et al. (2018)** bioRxiv 10.1101/318345. *P. aeruginosa* AceK regulatory characterization (crousilles2018threeenzymesand pages 5-7, crousilles2018threeenzymesand pages 1-3, crousilles2018threeenzymesand pages 3-5).
- **Dolan & Welch (2018)** Annu. Rev. Microbiol. 72:309–330. PMID: 30200851. Review of glyoxylate shunt regulation including AceK distribution (dolan2018theglyoxylateshunt pages 11-12, dolan2018theglyoxylateshunt pages 10-11, dolan2018theglyoxylateshunt pages 4-6).
- **Ikeda & LaPorte (1991)** J. Bacteriol. 173:1801–1806. PMID: 1999392. Identification of aceK alleles with kinase but not phosphatase activity (zheng2012structuralandmechanistic pages 6-7).
- **Miller et al. (2000)** J. Biol. Chem. 275:833–839. PMID: 10625615. Regulatory site locations on IDHK/P (miller2000locationsofthe pages 1-2).

### Explicit Uncertainties
1. **Direct biochemical characterization of Q88EA1 (*P. putida* AceK):** No primary literature was found that directly assays the kinase and phosphatase activities of the *P. putida* KT2440 AceK protein. Function is inferred from orthology with well-characterized *E. coli* and *P. aeruginosa* AceK enzymes and from transcriptomic/metabolic studies showing aceK upregulation in *P. putida* under glyoxylate shunt-activating conditions.
2. **PANTHER subfamily composition:** The PANTHER database could not be programmatically queried to enumerate all subfamilies within PTHR39559. The family and SF1 share the same name, suggesting a narrow family, but additional subfamilies may exist that were not evaluated.
3. **Catalytic residue conservation across all family members:** Sequence alignment of catalytic residues (Asp457, Asp475, Asp477, Lys336) across all PTHR39559 members was not computationally performed. This check would strengthen the homogeneity verdict.
4. **InterPro/Pfam domain architecture:** The specific InterPro/Pfam identifiers for AceK domains were not retrieved programmatically. The kinase domain is structurally classified as an atypical protein kinase; the regulatory domain has no Pfam homologue.
5. **HAD phosphatase superfamily relationship:** The phosphatase active site shows sequence-level similarity to the HAD superfamily DXDX(T/V) motif, but AceK is structurally a protein kinase fold enzyme. This dual evolutionary heritage is unusual and may warrant careful consideration in automated classification pipelines.


References

1. (zheng2012structuralandmechanistic pages 1-3): Jimin Zheng, Susan P. Yates, and Zongchao Jia. Structural and mechanistic insights into the bifunctional enzyme isocitrate dehydrogenase kinase/phosphatase acek. Philosophical Transactions of the Royal Society B: Biological Sciences, 367:2656-2668, Sep 2012. URL: https://doi.org/10.1098/rstb.2011.0426, doi:10.1098/rstb.2011.0426. This article has 36 citations and is from a domain leading peer-reviewed journal.

2. (rangwala2022kinasesondouble pages 14-15): Aziz M. Rangwala, Victoria R. Mingione, George Georghiou, and Markus A. Seeliger. Kinases on double duty: a review of uniprotkb annotated bifunctionality within the kinome. Biomolecules, 12:685, May 2022. URL: https://doi.org/10.3390/biom12050685, doi:10.3390/biom12050685. This article has 3 citations.

3. (zheng2012structuralandmechanistic pages 3-4): Jimin Zheng, Susan P. Yates, and Zongchao Jia. Structural and mechanistic insights into the bifunctional enzyme isocitrate dehydrogenase kinase/phosphatase acek. Philosophical Transactions of the Royal Society B: Biological Sciences, 367:2656-2668, Sep 2012. URL: https://doi.org/10.1098/rstb.2011.0426, doi:10.1098/rstb.2011.0426. This article has 36 citations and is from a domain leading peer-reviewed journal.

4. (zheng2012structuralandmechanistic pages 4-6): Jimin Zheng, Susan P. Yates, and Zongchao Jia. Structural and mechanistic insights into the bifunctional enzyme isocitrate dehydrogenase kinase/phosphatase acek. Philosophical Transactions of the Royal Society B: Biological Sciences, 367:2656-2668, Sep 2012. URL: https://doi.org/10.1098/rstb.2011.0426, doi:10.1098/rstb.2011.0426. This article has 36 citations and is from a domain leading peer-reviewed journal.

5. (zheng2012structuralandmechanistic pages 6-7): Jimin Zheng, Susan P. Yates, and Zongchao Jia. Structural and mechanistic insights into the bifunctional enzyme isocitrate dehydrogenase kinase/phosphatase acek. Philosophical Transactions of the Royal Society B: Biological Sciences, 367:2656-2668, Sep 2012. URL: https://doi.org/10.1098/rstb.2011.0426, doi:10.1098/rstb.2011.0426. This article has 36 citations and is from a domain leading peer-reviewed journal.

6. (zheng2012structuralandmechanistic pages 7-9): Jimin Zheng, Susan P. Yates, and Zongchao Jia. Structural and mechanistic insights into the bifunctional enzyme isocitrate dehydrogenase kinase/phosphatase acek. Philosophical Transactions of the Royal Society B: Biological Sciences, 367:2656-2668, Sep 2012. URL: https://doi.org/10.1098/rstb.2011.0426, doi:10.1098/rstb.2011.0426. This article has 36 citations and is from a domain leading peer-reviewed journal.

7. (zheng2012structuralandmechanistic pages 10-11): Jimin Zheng, Susan P. Yates, and Zongchao Jia. Structural and mechanistic insights into the bifunctional enzyme isocitrate dehydrogenase kinase/phosphatase acek. Philosophical Transactions of the Royal Society B: Biological Sciences, 367:2656-2668, Sep 2012. URL: https://doi.org/10.1098/rstb.2011.0426, doi:10.1098/rstb.2011.0426. This article has 36 citations and is from a domain leading peer-reviewed journal.

8. (crousilles2018threeenzymesand pages 1-3): Audrey Crousilles, Stephen K. Dolan, Paul Brear, Dimitri Y. Chirgadze, and Martin Welch. Three enzymes and one substrate; regulation of flux through the glyoxylate shunt in the opportunistic pathogen, pseudomonas aeruginosa. bioRxiv, May 2018. URL: https://doi.org/10.1101/318345, doi:10.1101/318345. This article has 1 citations.

9. (zheng2012structuralandmechanistic pages 11-13): Jimin Zheng, Susan P. Yates, and Zongchao Jia. Structural and mechanistic insights into the bifunctional enzyme isocitrate dehydrogenase kinase/phosphatase acek. Philosophical Transactions of the Royal Society B: Biological Sciences, 367:2656-2668, Sep 2012. URL: https://doi.org/10.1098/rstb.2011.0426, doi:10.1098/rstb.2011.0426. This article has 36 citations and is from a domain leading peer-reviewed journal.

10. (miller2000locationsofthe pages 1-2): Stephen P. Miller, Ridong Chen, Elizabeth J. Karschnia, Charles Romfo, Antony Dean, and David C. LaPorte. Locations of the regulatory sites for isocitrate dehydrogenase kinase/phosphatase*. The Journal of Biological Chemistry, 275:833-839, Jan 2000. URL: https://doi.org/10.1074/jbc.275.2.833, doi:10.1074/jbc.275.2.833. This article has 36 citations.

11. (dolan2018theglyoxylateshunt pages 4-6): Stephen K. Dolan and Martin Welch. The glyoxylate shunt, 60 years on. Annual review of microbiology, 72:309-330, Sep 2018. URL: https://doi.org/10.1146/annurev-micro-090817-062257, doi:10.1146/annurev-micro-090817-062257. This article has 213 citations and is from a peer-reviewed journal.

12. (chen2023twodifferentisocitrate pages 1-2): Xuefei Chen, Wei Wei, Wei Xiong, Shen Wu, Quanchao Wu, Peng Wang, and Guoping Zhu. Two different isocitrate dehydrogenases from pseudomonas aeruginosa: enzymology and coenzyme-evolutionary implications. International Journal of Molecular Sciences, 24:14985, Oct 2023. URL: https://doi.org/10.3390/ijms241914985, doi:10.3390/ijms241914985. This article has 3 citations.

13. (chen2023twodifferentisocitrate pages 9-10): Xuefei Chen, Wei Wei, Wei Xiong, Shen Wu, Quanchao Wu, Peng Wang, and Guoping Zhu. Two different isocitrate dehydrogenases from pseudomonas aeruginosa: enzymology and coenzyme-evolutionary implications. International Journal of Molecular Sciences, 24:14985, Oct 2023. URL: https://doi.org/10.3390/ijms241914985, doi:10.3390/ijms241914985. This article has 3 citations.

14. (crousilles2018threeenzymesand pages 5-7): Audrey Crousilles, Stephen K. Dolan, Paul Brear, Dimitri Y. Chirgadze, and Martin Welch. Three enzymes and one substrate; regulation of flux through the glyoxylate shunt in the opportunistic pathogen, pseudomonas aeruginosa. bioRxiv, May 2018. URL: https://doi.org/10.1101/318345, doi:10.1101/318345. This article has 1 citations.

15. (crousilles2018threeenzymesand pages 3-5): Audrey Crousilles, Stephen K. Dolan, Paul Brear, Dimitri Y. Chirgadze, and Martin Welch. Three enzymes and one substrate; regulation of flux through the glyoxylate shunt in the opportunistic pathogen, pseudomonas aeruginosa. bioRxiv, May 2018. URL: https://doi.org/10.1101/318345, doi:10.1101/318345. This article has 1 citations.

16. (dolan2018theglyoxylateshunt pages 11-12): Stephen K. Dolan and Martin Welch. The glyoxylate shunt, 60 years on. Annual review of microbiology, 72:309-330, Sep 2018. URL: https://doi.org/10.1146/annurev-micro-090817-062257, doi:10.1146/annurev-micro-090817-062257. This article has 213 citations and is from a peer-reviewed journal.

17. (dolan2018theglyoxylateshunt pages 10-11): Stephen K. Dolan and Martin Welch. The glyoxylate shunt, 60 years on. Annual review of microbiology, 72:309-330, Sep 2018. URL: https://doi.org/10.1146/annurev-micro-090817-062257, doi:10.1146/annurev-micro-090817-062257. This article has 213 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](PTHR39559-function-falcon_artifacts/artifact-00.md)