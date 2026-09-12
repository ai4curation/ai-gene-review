---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-24T04:14:40.328149'
end_time: '2026-06-24T04:30:04.231025'
duration_seconds: 923.9
template_file: templates/treegrafter_family_function.md
template_variables:
  family_id: PTHR11632
  family_name: SUCCINATE DEHYDROGENASE 2 FLAVOPROTEIN SUBUNIT
  subfamily: PTHR11632:SF51 SUCCINATE DEHYDROGENASE [UBIQUINONE] FLAVOPROTEIN SUBUNIT,
    MITOCHONDRIAL
  gene_symbol: Q72DT2
  uniprot: Q72DT2
  organism: DESVH
  taxon_label: DESVH
  propagated_term: succinate dehydrogenase activity (GO:0000104)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 38
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: PTHR11632-function-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PTHR11632-function-falcon_artifacts/artifact-01.md
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

- **PANTHER family:** PTHR11632 — SUCCINATE DEHYDROGENASE 2 FLAVOPROTEIN SUBUNIT
- **Subfamily of interest:** PTHR11632:SF51 SUCCINATE DEHYDROGENASE [UBIQUINONE] FLAVOPROTEIN SUBUNIT, MITOCHONDRIAL
- **Representative member:** Q72DT2 (Q72DT2), DESVH / DESVH
- **GO term currently propagated at/near this node:** succinate dehydrogenase activity (GO:0000104)

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
3. **Subfamily of interest.** Where does PTHR11632:SF51 SUCCINATE DEHYDROGENASE [UBIQUINONE] FLAVOPROTEIN SUBUNIT, MITOCHONDRIAL sit — does it carry the
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

- **PANTHER family:** PTHR11632 — SUCCINATE DEHYDROGENASE 2 FLAVOPROTEIN SUBUNIT
- **Subfamily of interest:** PTHR11632:SF51 SUCCINATE DEHYDROGENASE [UBIQUINONE] FLAVOPROTEIN SUBUNIT, MITOCHONDRIAL
- **Representative member:** Q72DT2 (Q72DT2), DESVH / DESVH
- **GO term currently propagated at/near this node:** succinate dehydrogenase activity (GO:0000104)

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
3. **Subfamily of interest.** Where does PTHR11632:SF51 SUCCINATE DEHYDROGENASE [UBIQUINONE] FLAVOPROTEIN SUBUNIT, MITOCHONDRIAL sit — does it carry the
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


# PTHR11632 — SUCCINATE DEHYDROGENASE FLAVOPROTEIN SUBUNIT FAMILY: TreeGrafter Granularity Audit

## Family Function Summary

The PTHR11632 family encompasses the flavoprotein subunits of succinate:quinone oxidoreductases (Complex II superfamily), which share a conserved ~70 kDa Rossmann-fold architecture with a covalently attached flavin adenine dinucleotide (FAD) cofactor linked through an 8α-N3-histidyl bond (kim2013emergingconceptsin pages 2-3, cheng2015redoxstateof pages 1-2, sharma2019maturationofthe pages 4-6). The covalent FAD attachment increases the cofactor's redox potential by approximately 60–100 mV, which is essential for succinate oxidation catalysis (kim2013emergingconceptsin pages 2-3, cheng2015redoxstateof pages 6-7, kim2012flavinylationandassembly pages 1-1). The core catalytic machinery includes the FAD-binding histidine residue, an arginine (R286 in *E. coli* SdhA) that acts as a proton donor/acceptor during substrate interconversion, and a histidine (H242 in *E. coli* SdhA) that hydrogen-bonds to the dicarboxylate substrate (cheng2015redoxstateof pages 6-7). All characterized family members catalyze the reversible interconversion of succinate and fumarate, but critically differ in their preferred catalytic directionality: succinate dehydrogenase (SQR) members preferentially oxidize succinate (EC 1.3.5.1), while fumarate reductase (QFR/FRD) members preferentially reduce fumarate (EC 1.3.5.4) (cheng2015redoxstateof pages 1-2, tran2011thefunctionof pages 34-39, maklashina2006fumaratereductaseand pages 1-2). A single diagnostic residue near the FAD—Gln in SdhA versus Glu in FrdA—substantially governs this directionality through coulombic effects on FAD electronic state and substrate binding (maklashina2006fumaratereductaseand pages 1-2, maklashina2006fumaratereductaseand pages 7-8, maklashina2006fumaratereductaseand pages 4-5). The Complex II superfamily is further classified into Types A–E based on membrane anchor subunit composition and heme content, though the catalytic SdhA/FrdA flavoprotein core is conserved across all types (tran2011thefunctionof pages 34-39).

## Subfamily Divergence Table

The following table summarizes the major functional subgroups within the PTHR11632 family and their divergent properties:

| Subgroup | Representative Member(s) (PMID) | Molecular Function | Substrate/Specialization | Catalytic Residues Intact? | GO MF Term | Notes |
|---|---|---|---|---|---|---|
| Succinate dehydrogenase (SQR/SDH) | *E. coli* SdhCDAB; human SDHA/P31040; *Chloroflexus aurantiacus* SdhA (PMID via DOI: 10.1021/bi501350j; 10.1074/jbc.m512544200) (cheng2015redoxstateof pages 1-2, maklashina2006fumaratereductaseand pages 1-2) | Succinate:quinone oxidoreductase; preferential succinate oxidation with reversible fumarate/succinate chemistry | Aerobic or respiratory-chain-linked succinate oxidation; covalent FAD, quinone reduction | Yes: catalytic His for covalent FAD linkage and Arg proton shuttle conserved; diagnostic Gln at ~position 50 near FAD favors SDH directionality (cheng2015redoxstateof pages 6-7, maklashina2006fumaratereductaseand pages 1-2) | GO:0000104 succinate dehydrogenase activity | Canonical SDH branch of Complex II; same Rossmann-fold flavoprotein core as FRD but tuned for succinate oxidation (kim2013emergingconceptsin pages 2-3, sharma2019maturationofthe pages 4-6) |
| Fumarate reductase (QFR/FRD) | *E. coli* FrdABCD; *Wolinella succinogenes* FrdA (PMID via DOI: 10.1074/jbc.m512544200) (maklashina2006fumaratereductaseand pages 1-2, maklashina2006fumaratereductaseand pages 7-8, maklashina2006fumaratereductaseand pages 3-4) | Quinol:fumarate oxidoreductase; preferential fumarate reduction with reversible chemistry | Anaerobic respiration using fumarate as terminal electron acceptor | Mostly yes for catalytic architecture, but directionality shifted; diagnostic Glu at ~position 49 near FAD favors FRD directionality rather than SDH (maklashina2006fumaratereductaseand pages 1-2, maklashina2006fumaratereductaseand pages 7-8, maklashina2006fumaratereductaseand pages 4-5) | GO:0008177 fumarate reductase activity | Structurally homologous to SDH, so family-level propagation of GO:0000104 would over-annotate this branch (kim2013emergingconceptsin pages 2-3, tran2011thefunctionof pages 34-39) |
| Menaquinone-dependent SDH (reverse redox loop) | *Desulfovibrio vulgaris* SdhA/Q72DT2; *Bacillus subtilis* SdhA (PMID via DOI: 10.1099/mic.0.28849-0) (zaunmuller2006succinatedehydrogenasefunctioning pages 1-2, zaunmuller2006succinatedehydrogenasefunctioning pages 2-3, zaunmuller2006succinatedehydrogenasefunctioning pages 7-8) | Succinate dehydrogenase coupled to menaquinone reduction; proton-potential-dependent SDH | SDH function in anaerobic/microaerophilic physiology via reverse redox loop; not fumarate respiration in *D. vulgaris* | Yes for SDH function; retains SDH-like catalytic core, but bioenergetic context differs from classical aerobic SQR (zaunmuller2006succinatedehydrogenasefunctioning pages 1-2, zaunmuller2006succinatedehydrogenasefunctioning pages 6-7, zaunmuller2006succinatedehydrogenasefunctioning pages 7-8) | GO:0000104 succinate dehydrogenase activity | Relevant to PTHR11632:SF51: *D. vulgaris* Q72DT2 is experimentally supported as SDH, not FRD (zaunmuller2006succinatedehydrogenasefunctioning pages 6-7, zaunmuller2006succinatedehydrogenasefunctioning pages 3-4, zaunmuller2006succinatedehydrogenasefunctioning pages 4-6) |
| Extracellular flavinylated reductases (Gram-positive) | *Listeria monocytogenes* FrdA and related extracellular reductases (PMID via DOI: 10.1073/pnas.1915678116) (light2019extracellularelectrontransfer pages 2-3, light2019extracellularelectrontransfer pages 3-4, light2019extracellularelectrontransfer pages 4-5) | Extracellular flavinylated reductase activities; clade-dependent fumarate, urocanate, or other acceptor reduction | Extracytoplasmic electron transfer; FMN attached at Ser, not canonical His-linked covalent FAD; some clades retain fumarate reductase activity, others are neofunctionalized | Divergent: canonical SdhA/FrdA His-FAD architecture not retained; N-terminal flavinylation at Ser48 is key, and active-site substitutions predict altered specificity in some clades (light2019extracellularelectrontransfer pages 2-3, light2019extracellularelectrontransfer pages 3-4, light2019extracellularelectrontransfer pages 5-5) | Clade-dependent; not safely assignable as GO:0000104 across the group | Strongest evidence that the broader homolog space is functionally heterogeneous; includes fumarate reductases, urocanate reductases, and unassigned reductases (light2019extracellularelectrontransfer pages 3-4, light2019extracellularelectrontransfer pages 4-5, light2019extracellularelectrontransfer pages 1-1) |
| Structural-similarity caution: L-aspartate oxidase (NadB) | NadB/L-aspartate oxidase mentioned as structurally similar reference, but inclusion in PTHR11632 uncertain (maklashina2016bindingofthe pages 9-10) | L-aspartate oxidase, not Complex II dicarboxylate oxidoreduction | NAD biosynthesis, not SDH/FRD respiration | Not applicable for this family-level audit | Not recommended for PTHR11632 without direct family evidence | Shares fold similarity with SdhA/FrdA in available structural comparison, but current evidence is insufficient to place it confidently inside PTHR11632; treat as out-of-scope/uncertain for curation (maklashina2016bindingofthe pages 9-10) |


*Table: This table summarizes the major functional branches relevant to the PTHR11632 flavoprotein family and highlights where succinate dehydrogenase activity is conserved versus where annotation should split to fumarate reductase or other extracellular reductase functions.*

## Homogeneous vs. Heterogeneous Verdict

> HOMOGENEOUS vs HETEROGENEOUS VERDICT:
>
> - The PTHR11632 family is **HETEROGENEOUS**. It includes both succinate dehydrogenase (SQR/SDH) and fumarate reductase (QFR/FRD) flavoprotein subunits. These enzymes share the same Rossmann-fold flavoprotein core and covalent FAD chemistry, but differ in preferred catalytic directionality; SDH branches are tuned for succinate oxidation, whereas FRD branches are tuned for fumarate reduction. Therefore, propagating **GO:0000104 succinate dehydrogenase activity** from the family root would over-annotate fumarate reductase branches. (kim2013emergingconceptsin pages 2-3, cheng2015redoxstateof pages 1-2, maklashina2006fumaratereductaseand pages 1-2, maklashina2006fumaratereductaseand pages 7-8)
>
> GRANULARITY LEADS FOR CURATION:
>
> - **Family-level safe term:** a broader parent term such as **oxidoreductase activity, acting on the CH-CH group of donors (GO:0016627)**, or an equivalent higher-level succinate/fumarate oxidoreductase concept, is safer than GO:0000104 at the PTHR11632 family level. (kim2013emergingconceptsin pages 2-3, tran2011thefunctionof pages 34-39)
> - **SDH/SQR subfamilies:** **GO:0000104 succinate dehydrogenase activity** is appropriate for bona fide SDH branches, including **PTHR11632:SF51**. Experimental evidence in *Desulfovibrio vulgaris* shows the representative Q72DT2 branch functions as SDH rather than FRD. (zaunmuller2006succinatedehydrogenasefunctioning pages 1-2, zaunmuller2006succinatedehydrogenasefunctioning pages 6-7, zaunmuller2006succinatedehydrogenasefunctioning pages 3-4, zaunmuller2006succinatedehydrogenasefunctioning pages 2-3, zaunmuller2006succinatedehydrogenasefunctioning pages 7-8)
> - **FRD/QFR subfamilies:** these should instead receive **GO:0008177 fumarate reductase activity**, because their preferred physiological role is fumarate reduction despite the shared fold and partially reversible chemistry. (maklashina2006fumaratereductaseand pages 1-2, maklashina2006fumaratereductaseand pages 7-8, maklashina2006fumaratereductaseand pages 4-5, maklashina2006fumaratereductaseand pages 3-4)
> - **Extracellular flavinylated reductases** (if they fall within this PANTHER family boundary) require **clade-specific annotation**. Some retain fumarate reductase activity, whereas others are neofunctionalized extracellular reductases, including urocanate-reducing branches and additional unresolved specificities. (light2019extracellularelectrontransfer pages 2-3, light2019extracellularelectrontransfer pages 3-4, light2019extracellularelectrontransfer pages 4-5, light2019extracellularelectrontransfer pages 5-5)
> - **Bottom line:** the currently propagated **GO:0000104** is supported for **SF51 specifically**, but it is **not safe at the family level**. (zaunmuller2006succinatedehydrogenasefunctioning pages 1-2, zaunmuller2006succinatedehydrogenasefunctioning pages 6-7, maklashina2006fumaratereductaseand pages 1-2, maklashina2006fumaratereductaseand pages 7-8)


*Blockquote: This blockquote gives the curator-facing verdict on whether PTHR11632 is functionally homogeneous enough for GO:0000104 propagation. It highlights the SDH versus FRD split and specifies where the current annotation is appropriate versus over-broad.*

The family is **heterogeneous**. A single family-level GO MF term of GO:0000104 (succinate dehydrogenase activity) is **not safe** to propagate across the entire PTHR11632 family. This term would mis-annotate the fumarate reductase (QFR/FRD) branch, whose members preferentially catalyze fumarate reduction and are physiologically specialized for anaerobic respiration using fumarate as a terminal electron acceptor (tran2011thefunctionof pages 34-39, maklashina2006fumaratereductaseand pages 1-2, maklashina2006fumaratereductaseand pages 7-8). Although SDH and FRD enzymes share the same fold, the same covalent FAD linkage, and can cross-complement each other when overexpressed, they are functionally optimized for opposite directions of the same reaction (cheng2015redoxstateof pages 1-2). The SdhA Q50E mutation causes a 500-fold loss in succinate oxidase activity, while FrdA E49Q impairs fumarate reduction, demonstrating that the directionality preference is biochemically meaningful and not merely nominal (maklashina2006fumaratereductaseand pages 7-8, maklashina2006fumaratereductaseand pages 4-5). Additional functional heterogeneity exists in the form of extracellular flavinylated reductases in Gram-positive bacteria, which include neofunctionalized urocanate reductases and other uncharacterized reductases alongside fumarate reductases (light2019extracellularelectrontransfer pages 3-4, light2019extracellularelectrontransfer pages 4-5).

## Granularity Leads for Curation

**Family-level GO MF term recommendation:** The safest family-level GO MF term is a broader parent term such as **oxidoreductase activity, acting on the CH-CH group of donors (GO:0016627)**, which encompasses both the succinate dehydrogenase and fumarate reductase activities without implying a specific directionality. The currently propagated GO:0000104 is too specific for the family root.

**Subfamily-level GO MF term recommendations:**
- **SDH/SQR subfamilies** (including PTHR11632:SF51): **GO:0000104 (succinate dehydrogenase activity)** is appropriate. For SF51 specifically, the representative member Q72DT2 from *Desulfovibrio vulgaris* Hildenborough has been experimentally characterized as functioning as succinate dehydrogenase via a reverse redox loop mechanism, with a low fumarate reductase-to-SDH activity ratio of 4:1 and the absence of the FRD-specific uncoupling Glu180 residue (zaunmuller2006succinatedehydrogenasefunctioning pages 1-2, zaunmuller2006succinatedehydrogenasefunctioning pages 6-7, zaunmuller2006succinatedehydrogenasefunctioning pages 4-6, zaunmuller2006succinatedehydrogenasefunctioning pages 7-8).
- **FRD/QFR subfamilies**: **GO:0008177 (fumarate reductase activity)** should replace GO:0000104, as these members preferentially reduce fumarate under anaerobic conditions and are bioenergetically specialized for this direction (tran2011thefunctionof pages 34-39, maklashina2006fumaratereductaseand pages 1-2, maklashina2006fumaratereductaseand pages 3-4).
- **Extracellular flavinylated reductase subfamilies** (if included in PTHR11632): These require clade-specific annotation. Clade I members retain fumarate reductase activity; Clade II members are urocanate reductases; Clade III members have unidentified specificities (light2019extracellularelectrontransfer pages 3-4, light2019extracellularelectrontransfer pages 4-5).

**Subfamilies where the currently propagated term is an over-annotation:** Any FRD/QFR-containing subfamilies within PTHR11632 that receive GO:0000104 by inheritance from the family node are over-annotated. The Glu-at-position-49 diagnostic can be used computationally to identify these branches.

## Evidence and Gaps

**Key citations (by DOI, with PMID where available):**
- Cheng et al. (2015), *Biochemistry* 54:1043–52, DOI: 10.1021/bi501350j — Redox state of FAD drives substrate binding in *E. coli* SDH, key residue characterization (cheng2015redoxstateof pages 1-2, cheng2015redoxstateof pages 6-7, cheng2015redoxstateof pages 7-9).
- Kim & Winge (2013), *BBA-Bioenergetics* 1827:627–36, DOI: 10.1016/j.bbabio.2013.01.012 — Covalent flavinylation mechanisms and SDH/FRD comparison (kim2013emergingconceptsin pages 2-3).
- Maklashina et al. (2006), *J Biol Chem* 281:11357–65, DOI: 10.1074/jbc.m512544200 — Glu49/Gln50 swaps between FRD and SDH demonstrate directionality determinants (maklashina2006fumaratereductaseand pages 1-2, maklashina2006fumaratereductaseand pages 7-8, maklashina2006fumaratereductaseand pages 4-5, maklashina2006fumaratereductaseand pages 3-4, maklashina2006fumaratereductaseand pages 6-7).
- Zaunmüller et al. (2006), *Microbiology* 152:2443–53, DOI: 10.1099/mic.0.28849-0 — *D. vulgaris* enzyme characterized as SDH, not FRD (zaunmuller2006succinatedehydrogenasefunctioning pages 1-2, zaunmuller2006succinatedehydrogenasefunctioning pages 6-7, zaunmuller2006succinatedehydrogenasefunctioning pages 3-4, zaunmuller2006succinatedehydrogenasefunctioning pages 4-6, zaunmuller2006succinatedehydrogenasefunctioning pages 2-3, zaunmuller2006succinatedehydrogenasefunctioning pages 7-8).
- Zhang et al. (2025), *Nature Communications* 16, DOI: 10.1038/s41467-025-65828-3 — Cryo-EM structure of *C. aurantiacus* SDH with menaquinone (zhang2025structuralbasisof pages 3-5).
- Light et al. (2019), *PNAS* 116:26892–99, DOI: 10.1073/pnas.1915678116 — Extracellular flavinylated reductases in Gram-positive bacteria, neofunctionalization (light2019extracellularelectrontransfer pages 2-3, light2019extracellularelectrontransfer pages 3-4, light2019extracellularelectrontransfer pages 1-2, light2019extracellularelectrontransfer pages 4-5, light2019extracellularelectrontransfer pages 6-6, light2019extracellularelectrontransfer pages 5-5).
- Sharma et al. (2019), *Curr Opin Struct Biol* 59:38–46, DOI: 10.1016/j.sbi.2019.01.027 — Complex II flavoprotein maturation (sharma2019maturationofthe pages 4-6).
- Tran (2011), University of Alberta thesis, DOI: 10.7939/r3jd33 — Classification of Complex II types A–E (tran2011thefunctionof pages 34-39).
- OpenTargets: human SDHA associated with Leigh syndrome, pheochromocytoma/paraganglioma, cardiomyopathy, mitochondrial complex II deficiency (OpenTargets Search: -SDHA,SDHB).

**Explicit uncertainties:**
1. **PANTHER family boundary verification.** Whether PTHR11632 as currently defined includes FRD flavoprotein subunits (FrdA) as well as SDH flavoprotein subunits (SdhA) could not be verified computationally here, as the PANTHER family tree was not directly accessible. The assessment above assumes the family spans the full SQR/QFR superfamily based on the family name and the known close homology between SdhA and FrdA. If PTHR11632 is narrowly scoped to exclude FrdA paralogs, the heterogeneity concern is reduced.
2. **Extracellular flavinylated reductases.** Whether the *Listeria* FrdA and related extracellular reductases are classified within PTHR11632 versus a separate PANTHER family is uncertain. These use FMN rather than FAD and flavinylation at Ser rather than His, suggesting they may fall outside PTHR11632.
3. **L-aspartate oxidase (NadB).** NadB shares structural similarity with SdhA/FrdA but catalyzes a different reaction (L-aspartate oxidation in NAD biosynthesis). Its placement relative to PTHR11632 is uncertain (maklashina2016bindingofthe pages 9-10).
4. **Residue-level conservation across PTHR11632 subfamilies.** A systematic alignment of the Glu/Gln diagnostic position across all PTHR11632 subfamilies was not performed computationally; this would strengthen the curation lead.
5. **Whether "succinate dehydrogenase activity" (GO:0000104) encompasses the full Complex II reaction (succinate + quinone → fumarate + quinol) or only the dicarboxylate half-reaction** is a GO ontology question beyond the scope of this audit but relevant to precision of annotation.

References

1. (kim2013emergingconceptsin pages 2-3): Hyung J. Kim and Dennis R. Winge. Emerging concepts in the flavinylation of succinate dehydrogenase. Biochimica et biophysica acta, 1827 5:627-36, May 2013. URL: https://doi.org/10.1016/j.bbabio.2013.01.012, doi:10.1016/j.bbabio.2013.01.012. This article has 97 citations.

2. (cheng2015redoxstateof pages 1-2): Victor W. T. Cheng, Ramanaguru Siva Piragasam, Richard A. Rothery, Elena Maklashina, Gary Cecchini, and Joel H. Weiner. Redox state of flavin adenine dinucleotide drives substrate binding and product release in escherichia coli succinate dehydrogenase. Biochemistry, 54 4:1043-52, Jan 2015. URL: https://doi.org/10.1021/bi501350j, doi:10.1021/bi501350j. This article has 33 citations and is from a peer-reviewed journal.

3. (sharma2019maturationofthe pages 4-6): Pankaj Sharma, Elena Maklashina, Gary Cecchini, and TM Iverson. Maturation of the respiratory complex ii flavoprotein. Current opinion in structural biology, 59:38-46, Dec 2019. URL: https://doi.org/10.1016/j.sbi.2019.01.027, doi:10.1016/j.sbi.2019.01.027. This article has 35 citations and is from a peer-reviewed journal.

4. (cheng2015redoxstateof pages 6-7): Victor W. T. Cheng, Ramanaguru Siva Piragasam, Richard A. Rothery, Elena Maklashina, Gary Cecchini, and Joel H. Weiner. Redox state of flavin adenine dinucleotide drives substrate binding and product release in escherichia coli succinate dehydrogenase. Biochemistry, 54 4:1043-52, Jan 2015. URL: https://doi.org/10.1021/bi501350j, doi:10.1021/bi501350j. This article has 33 citations and is from a peer-reviewed journal.

5. (kim2012flavinylationandassembly pages 1-1): Hyung J. Kim, Mi-Young Jeong, Un Na, and Dennis R. Winge. Flavinylation and assembly of succinate dehydrogenase are dependent on the c-terminal tail of the flavoprotein subunit. Nov 2012. URL: https://doi.org/10.1074/jbc.m112.405704, doi:10.1074/jbc.m112.405704. This article has 54 citations and is from a domain leading peer-reviewed journal.

6. (tran2011thefunctionof pages 34-39): Quang Tran. The function of the electron transfer chain in escherichia coli succinate dehydrogenase. Text, Nov 2011. URL: https://doi.org/10.7939/r3jd33, doi:10.7939/r3jd33. This article has 0 citations and is from a peer-reviewed journal.

7. (maklashina2006fumaratereductaseand pages 1-2): Elena Maklashina, Tina M. Iverson, Yelizaveta Sher, Violetta Kotlyar, Juni Andréll, Osman Mirza, Janette M. Hudson, Fraser A. Armstrong, Richard A. Rothery, Joel H. Weiner, and Gary Cecchini. Fumarate reductase and succinate oxidase activity of escherichia coli complex ii homologs are perturbed differently by mutation of the flavin binding domain*. Journal of Biological Chemistry, 281:11357-11365, Apr 2006. URL: https://doi.org/10.1074/jbc.m512544200, doi:10.1074/jbc.m512544200. This article has 62 citations and is from a domain leading peer-reviewed journal.

8. (maklashina2006fumaratereductaseand pages 7-8): Elena Maklashina, Tina M. Iverson, Yelizaveta Sher, Violetta Kotlyar, Juni Andréll, Osman Mirza, Janette M. Hudson, Fraser A. Armstrong, Richard A. Rothery, Joel H. Weiner, and Gary Cecchini. Fumarate reductase and succinate oxidase activity of escherichia coli complex ii homologs are perturbed differently by mutation of the flavin binding domain*. Journal of Biological Chemistry, 281:11357-11365, Apr 2006. URL: https://doi.org/10.1074/jbc.m512544200, doi:10.1074/jbc.m512544200. This article has 62 citations and is from a domain leading peer-reviewed journal.

9. (maklashina2006fumaratereductaseand pages 4-5): Elena Maklashina, Tina M. Iverson, Yelizaveta Sher, Violetta Kotlyar, Juni Andréll, Osman Mirza, Janette M. Hudson, Fraser A. Armstrong, Richard A. Rothery, Joel H. Weiner, and Gary Cecchini. Fumarate reductase and succinate oxidase activity of escherichia coli complex ii homologs are perturbed differently by mutation of the flavin binding domain*. Journal of Biological Chemistry, 281:11357-11365, Apr 2006. URL: https://doi.org/10.1074/jbc.m512544200, doi:10.1074/jbc.m512544200. This article has 62 citations and is from a domain leading peer-reviewed journal.

10. (maklashina2006fumaratereductaseand pages 3-4): Elena Maklashina, Tina M. Iverson, Yelizaveta Sher, Violetta Kotlyar, Juni Andréll, Osman Mirza, Janette M. Hudson, Fraser A. Armstrong, Richard A. Rothery, Joel H. Weiner, and Gary Cecchini. Fumarate reductase and succinate oxidase activity of escherichia coli complex ii homologs are perturbed differently by mutation of the flavin binding domain*. Journal of Biological Chemistry, 281:11357-11365, Apr 2006. URL: https://doi.org/10.1074/jbc.m512544200, doi:10.1074/jbc.m512544200. This article has 62 citations and is from a domain leading peer-reviewed journal.

11. (zaunmuller2006succinatedehydrogenasefunctioning pages 1-2): Tanja Zaunmüller, David J. Kelly, Frank O. Glöckner, and Gottfried Unden. Succinate dehydrogenase functioning by a reverse redox loop mechanism and fumarate reductase in sulphate-reducing bacteria. Microbiology, 152 Pt 8:2443-53, Aug 2006. URL: https://doi.org/10.1099/mic.0.28849-0, doi:10.1099/mic.0.28849-0. This article has 55 citations and is from a peer-reviewed journal.

12. (zaunmuller2006succinatedehydrogenasefunctioning pages 2-3): Tanja Zaunmüller, David J. Kelly, Frank O. Glöckner, and Gottfried Unden. Succinate dehydrogenase functioning by a reverse redox loop mechanism and fumarate reductase in sulphate-reducing bacteria. Microbiology, 152 Pt 8:2443-53, Aug 2006. URL: https://doi.org/10.1099/mic.0.28849-0, doi:10.1099/mic.0.28849-0. This article has 55 citations and is from a peer-reviewed journal.

13. (zaunmuller2006succinatedehydrogenasefunctioning pages 7-8): Tanja Zaunmüller, David J. Kelly, Frank O. Glöckner, and Gottfried Unden. Succinate dehydrogenase functioning by a reverse redox loop mechanism and fumarate reductase in sulphate-reducing bacteria. Microbiology, 152 Pt 8:2443-53, Aug 2006. URL: https://doi.org/10.1099/mic.0.28849-0, doi:10.1099/mic.0.28849-0. This article has 55 citations and is from a peer-reviewed journal.

14. (zaunmuller2006succinatedehydrogenasefunctioning pages 6-7): Tanja Zaunmüller, David J. Kelly, Frank O. Glöckner, and Gottfried Unden. Succinate dehydrogenase functioning by a reverse redox loop mechanism and fumarate reductase in sulphate-reducing bacteria. Microbiology, 152 Pt 8:2443-53, Aug 2006. URL: https://doi.org/10.1099/mic.0.28849-0, doi:10.1099/mic.0.28849-0. This article has 55 citations and is from a peer-reviewed journal.

15. (zaunmuller2006succinatedehydrogenasefunctioning pages 3-4): Tanja Zaunmüller, David J. Kelly, Frank O. Glöckner, and Gottfried Unden. Succinate dehydrogenase functioning by a reverse redox loop mechanism and fumarate reductase in sulphate-reducing bacteria. Microbiology, 152 Pt 8:2443-53, Aug 2006. URL: https://doi.org/10.1099/mic.0.28849-0, doi:10.1099/mic.0.28849-0. This article has 55 citations and is from a peer-reviewed journal.

16. (zaunmuller2006succinatedehydrogenasefunctioning pages 4-6): Tanja Zaunmüller, David J. Kelly, Frank O. Glöckner, and Gottfried Unden. Succinate dehydrogenase functioning by a reverse redox loop mechanism and fumarate reductase in sulphate-reducing bacteria. Microbiology, 152 Pt 8:2443-53, Aug 2006. URL: https://doi.org/10.1099/mic.0.28849-0, doi:10.1099/mic.0.28849-0. This article has 55 citations and is from a peer-reviewed journal.

17. (light2019extracellularelectrontransfer pages 2-3): Samuel H. Light, Raphaël Méheust, Jessica L. Ferrell, Jooyoung Cho, David Deng, Marco Agostoni, Anthony T. Iavarone, Jillian F. Banfield, Sarah E. F. D’Orazio, and Daniel A. Portnoy. Extracellular electron transfer powers flavinylated extracellular reductases in gram-positive bacteria. Proceedings of the National Academy of Sciences, 116:26892-26899, Dec 2019. URL: https://doi.org/10.1073/pnas.1915678116, doi:10.1073/pnas.1915678116. This article has 98 citations and is from a highest quality peer-reviewed journal.

18. (light2019extracellularelectrontransfer pages 3-4): Samuel H. Light, Raphaël Méheust, Jessica L. Ferrell, Jooyoung Cho, David Deng, Marco Agostoni, Anthony T. Iavarone, Jillian F. Banfield, Sarah E. F. D’Orazio, and Daniel A. Portnoy. Extracellular electron transfer powers flavinylated extracellular reductases in gram-positive bacteria. Proceedings of the National Academy of Sciences, 116:26892-26899, Dec 2019. URL: https://doi.org/10.1073/pnas.1915678116, doi:10.1073/pnas.1915678116. This article has 98 citations and is from a highest quality peer-reviewed journal.

19. (light2019extracellularelectrontransfer pages 4-5): Samuel H. Light, Raphaël Méheust, Jessica L. Ferrell, Jooyoung Cho, David Deng, Marco Agostoni, Anthony T. Iavarone, Jillian F. Banfield, Sarah E. F. D’Orazio, and Daniel A. Portnoy. Extracellular electron transfer powers flavinylated extracellular reductases in gram-positive bacteria. Proceedings of the National Academy of Sciences, 116:26892-26899, Dec 2019. URL: https://doi.org/10.1073/pnas.1915678116, doi:10.1073/pnas.1915678116. This article has 98 citations and is from a highest quality peer-reviewed journal.

20. (light2019extracellularelectrontransfer pages 5-5): Samuel H. Light, Raphaël Méheust, Jessica L. Ferrell, Jooyoung Cho, David Deng, Marco Agostoni, Anthony T. Iavarone, Jillian F. Banfield, Sarah E. F. D’Orazio, and Daniel A. Portnoy. Extracellular electron transfer powers flavinylated extracellular reductases in gram-positive bacteria. Proceedings of the National Academy of Sciences, 116:26892-26899, Dec 2019. URL: https://doi.org/10.1073/pnas.1915678116, doi:10.1073/pnas.1915678116. This article has 98 citations and is from a highest quality peer-reviewed journal.

21. (light2019extracellularelectrontransfer pages 1-1): Samuel H. Light, Raphaël Méheust, Jessica L. Ferrell, Jooyoung Cho, David Deng, Marco Agostoni, Anthony T. Iavarone, Jillian F. Banfield, Sarah E. F. D’Orazio, and Daniel A. Portnoy. Extracellular electron transfer powers flavinylated extracellular reductases in gram-positive bacteria. Proceedings of the National Academy of Sciences, 116:26892-26899, Dec 2019. URL: https://doi.org/10.1073/pnas.1915678116, doi:10.1073/pnas.1915678116. This article has 98 citations and is from a highest quality peer-reviewed journal.

22. (maklashina2016bindingofthe pages 9-10): Elena Maklashina, Sany Rajagukguk, Chrystal A. Starbird, W. Hayes McDonald, Anna Koganitsky, Michael Eisenbach, Tina M. Iverson, and Gary Cecchini. Binding of the covalent flavin assembly factor to the flavoprotein subunit of complex ii. Journal of Biological Chemistry, 291:2904-2916, Feb 2016. URL: https://doi.org/10.1074/jbc.m115.690396, doi:10.1074/jbc.m115.690396. This article has 20 citations and is from a domain leading peer-reviewed journal.

23. (cheng2015redoxstateof pages 7-9): Victor W. T. Cheng, Ramanaguru Siva Piragasam, Richard A. Rothery, Elena Maklashina, Gary Cecchini, and Joel H. Weiner. Redox state of flavin adenine dinucleotide drives substrate binding and product release in escherichia coli succinate dehydrogenase. Biochemistry, 54 4:1043-52, Jan 2015. URL: https://doi.org/10.1021/bi501350j, doi:10.1021/bi501350j. This article has 33 citations and is from a peer-reviewed journal.

24. (maklashina2006fumaratereductaseand pages 6-7): Elena Maklashina, Tina M. Iverson, Yelizaveta Sher, Violetta Kotlyar, Juni Andréll, Osman Mirza, Janette M. Hudson, Fraser A. Armstrong, Richard A. Rothery, Joel H. Weiner, and Gary Cecchini. Fumarate reductase and succinate oxidase activity of escherichia coli complex ii homologs are perturbed differently by mutation of the flavin binding domain*. Journal of Biological Chemistry, 281:11357-11365, Apr 2006. URL: https://doi.org/10.1074/jbc.m512544200, doi:10.1074/jbc.m512544200. This article has 62 citations and is from a domain leading peer-reviewed journal.

25. (zhang2025structuralbasisof pages 3-5): Xin Zhang, Jingyi Wu, Jiamao Wang, Huimin He, Aokun Liu, Xin Hong, Yuanyi Yu, Xinkai Pei, Xianjie Fang, Yueyong Xin, Lu Yu, Changlin Tian, and Xiaoling Xu. Structural basis of menaquinone reduction by succinate dehydrogenase from chloroflexus aurantiacus. Nature Communications, Nov 2025. URL: https://doi.org/10.1038/s41467-025-65828-3, doi:10.1038/s41467-025-65828-3. This article has 2 citations and is from a highest quality peer-reviewed journal.

26. (light2019extracellularelectrontransfer pages 1-2): Samuel H. Light, Raphaël Méheust, Jessica L. Ferrell, Jooyoung Cho, David Deng, Marco Agostoni, Anthony T. Iavarone, Jillian F. Banfield, Sarah E. F. D’Orazio, and Daniel A. Portnoy. Extracellular electron transfer powers flavinylated extracellular reductases in gram-positive bacteria. Proceedings of the National Academy of Sciences, 116:26892-26899, Dec 2019. URL: https://doi.org/10.1073/pnas.1915678116, doi:10.1073/pnas.1915678116. This article has 98 citations and is from a highest quality peer-reviewed journal.

27. (light2019extracellularelectrontransfer pages 6-6): Samuel H. Light, Raphaël Méheust, Jessica L. Ferrell, Jooyoung Cho, David Deng, Marco Agostoni, Anthony T. Iavarone, Jillian F. Banfield, Sarah E. F. D’Orazio, and Daniel A. Portnoy. Extracellular electron transfer powers flavinylated extracellular reductases in gram-positive bacteria. Proceedings of the National Academy of Sciences, 116:26892-26899, Dec 2019. URL: https://doi.org/10.1073/pnas.1915678116, doi:10.1073/pnas.1915678116. This article has 98 citations and is from a highest quality peer-reviewed journal.

28. (OpenTargets Search: -SDHA,SDHB): Open Targets Query (-SDHA,SDHB, 11 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

## Artifacts

- [Edison artifact artifact-00](PTHR11632-function-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PTHR11632-function-falcon_artifacts/artifact-01.md)