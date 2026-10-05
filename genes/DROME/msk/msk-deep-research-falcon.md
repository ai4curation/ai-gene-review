---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-08T18:12:55.934459'
end_time: '2026-09-08T18:20:32.614741'
duration_seconds: 456.68
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: DROME
  gene_id: msk
  gene_symbol: msk
  uniprot_accession: Q9VSD6
  protein_description: 'SubName: Full=Moleskin {ECO:0000313|EMBL:AAF50487.1};'
  gene_info: Name=msk {ECO:0000313|EMBL:AAF50487.1, ECO:0000313|FlyBase:FBgn0026252};
    Synonyms=61 {ECO:0000313|EMBL:AAF50487.1}, CIP-61 {ECO:0000313|EMBL:AAF50487.1},
    DIM-7 {ECO:0000313|EMBL:AAF50487.1}, Dim-7 {ECO:0000313|EMBL:AAF50487.1}, dim-7
    {ECO:0000313|EMBL:AAF50487.1}, Dim7 {ECO:0000313|EMBL:AAF50487.1}, dim7 {ECO:0000313|EMBL:AAF50487.1},
    Dmel\CG7935 {ECO:0000313|EMBL:AAF50487.1}, DmRanBP7 {ECO:0000313|EMBL:AAF50487.1},
    Imp 7 {ECO:0000313|EMBL:AAF50487.1}, Imp7 {ECO:0000313|EMBL:AAF50487.1}, Imp7/8
    {ECO:0000313|EMBL:AAF50487.1}, Msk {ECO:0000313|EMBL:AAF50487.1}, S(ls)2 {ECO:0000313|EMBL:AAF50487.1};
    ORFNames=CG7935 {ECO:0000313|EMBL:AAF50487.1, ECO:0000313|FlyBase:FBgn0026252},
    Dmel_CG7935 {ECO:0000313|EMBL:AAF50487.1};
  organism_full: Drosophila melanogaster (Fruit fly).
  protein_family: Belongs to the importin beta family.
  protein_domains: ARM-like. (IPR011989); ARM-type_fold. (IPR016024); Importin-beta_N.
    (IPR001494); TPR_IPO7/11-like. (IPR058669); XPO2_central. (IPR013713)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 41
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: msk-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q9VSD6
- **Protein Description:** SubName: Full=Moleskin {ECO:0000313|EMBL:AAF50487.1};
- **Gene Information:** Name=msk {ECO:0000313|EMBL:AAF50487.1, ECO:0000313|FlyBase:FBgn0026252}; Synonyms=61 {ECO:0000313|EMBL:AAF50487.1}, CIP-61 {ECO:0000313|EMBL:AAF50487.1}, DIM-7 {ECO:0000313|EMBL:AAF50487.1}, Dim-7 {ECO:0000313|EMBL:AAF50487.1}, dim-7 {ECO:0000313|EMBL:AAF50487.1}, Dim7 {ECO:0000313|EMBL:AAF50487.1}, dim7 {ECO:0000313|EMBL:AAF50487.1}, Dmel\CG7935 {ECO:0000313|EMBL:AAF50487.1}, DmRanBP7 {ECO:0000313|EMBL:AAF50487.1}, Imp 7 {ECO:0000313|EMBL:AAF50487.1}, Imp7 {ECO:0000313|EMBL:AAF50487.1}, Imp7/8 {ECO:0000313|EMBL:AAF50487.1}, Msk {ECO:0000313|EMBL:AAF50487.1}, S(ls)2 {ECO:0000313|EMBL:AAF50487.1}; ORFNames=CG7935 {ECO:0000313|EMBL:AAF50487.1, ECO:0000313|FlyBase:FBgn0026252}, Dmel_CG7935 {ECO:0000313|EMBL:AAF50487.1};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Belongs to the importin beta family.
- **Key Domains:** ARM-like. (IPR011989); ARM-type_fold. (IPR016024); Importin-beta_N. (IPR001494); TPR_IPO7/11-like. (IPR058669); XPO2_central. (IPR013713)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "msk" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'msk' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **msk** (gene ID: msk, UniProt: Q9VSD6) in DROME.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

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

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q9VSD6
- **Protein Description:** SubName: Full=Moleskin {ECO:0000313|EMBL:AAF50487.1};
- **Gene Information:** Name=msk {ECO:0000313|EMBL:AAF50487.1, ECO:0000313|FlyBase:FBgn0026252}; Synonyms=61 {ECO:0000313|EMBL:AAF50487.1}, CIP-61 {ECO:0000313|EMBL:AAF50487.1}, DIM-7 {ECO:0000313|EMBL:AAF50487.1}, Dim-7 {ECO:0000313|EMBL:AAF50487.1}, dim-7 {ECO:0000313|EMBL:AAF50487.1}, Dim7 {ECO:0000313|EMBL:AAF50487.1}, dim7 {ECO:0000313|EMBL:AAF50487.1}, Dmel\CG7935 {ECO:0000313|EMBL:AAF50487.1}, DmRanBP7 {ECO:0000313|EMBL:AAF50487.1}, Imp 7 {ECO:0000313|EMBL:AAF50487.1}, Imp7 {ECO:0000313|EMBL:AAF50487.1}, Imp7/8 {ECO:0000313|EMBL:AAF50487.1}, Msk {ECO:0000313|EMBL:AAF50487.1}, S(ls)2 {ECO:0000313|EMBL:AAF50487.1}; ORFNames=CG7935 {ECO:0000313|EMBL:AAF50487.1, ECO:0000313|FlyBase:FBgn0026252}, Dmel_CG7935 {ECO:0000313|EMBL:AAF50487.1};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Belongs to the importin beta family.
- **Key Domains:** ARM-like. (IPR011989); ARM-type_fold. (IPR016024); Importin-beta_N. (IPR001494); TPR_IPO7/11-like. (IPR058669); XPO2_central. (IPR013713)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "msk" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'msk' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **msk** (gene ID: msk, UniProt: Q9VSD6) in DROME.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Functional annotation report: *Drosophila melanogaster moleskin* (*msk*), UniProt Q9VSD6

## Executive conclusion

The identity is internally consistent and verified at the literature level: *D. melanogaster moleskin* (*msk*) encodes Moleskin/DIM-7, the fly ortholog of Importin-7/RanBP7. Published comparisons report approximately 50–53% amino-acid identity to vertebrate or human Importin-7 and 72% similarity in one comparison. This agrees with the supplied identifiers CG7935/FBgn0026252/Q9VSD6 and with the supplied importin-β-family, Importin-beta_N, ARM/ARM-type-fold, and TPR_IPO7/11-like annotations. The retrieved papers do not themselves print accession Q9VSD6, so accession-to-gene mapping rests on the supplied UniProt record, whereas the *msk*–DIM-7–Importin-7 equivalence is independently supported by multiple studies. No literature concerning a different “MSK” protein was used. (liu2012“importin”signalingroles pages 4-4, james2007nuclearlocalizationof pages 2-3, baker2002geneticinteractionbetween pages 1-2)

The most defensible primary annotation is:

> **Msk is a non-enzymatic, Ran-associated importin-β-family nuclear-transport receptor that mediates context-dependent nuclear accumulation of activated signaling proteins—notably doubly phosphorylated ERK, phosphorylated Mad, and Yorkie—and also performs a localized cytoplasmic/scaffolding-signaling function at muscle–tendon attachment sites.**

Msk therefore has no catalytic reaction or small-molecule substrate. Its “substrates” are protein cargoes. Its best-supported fly cargoes are activated D-ERK, Dpp/BMP-activated phospho-Mad, and tension-competent Yorkie. At myotendinous junctions, Msk also participates in integrin-dependent organization of an Elmo–Mbc–Rac module and in muscle-to-tendon Vein–EGFR–MAPK signaling. (xu2007mskisrequired pages 2-3, james2007nuclearlocalizationof pages 2-3, liu2013drosophilaimportin7functions pages 1-4, liu2011moleskinisessential pages 1-2, garciagarcia2022mechanicalcontrolof pages 9-10)

## Evidence overview

| Functional facet | Direct evidence | Cellular location/context | Confidence / interpretation | Key publication (date; DOI URL) |
|---|---|---|---|---|
| Identity and family | *D. melanogaster* **msk** encodes DIM-7/Moleskin, the fly homolog of vertebrate Importin-7/RanBP7; DIM-7 reportedly shares ~50–53% amino-acid identity with vertebrate/human Imp7. This agrees with Q9VSD6/CG7935 being an importin-β-superfamily protein with ARM/HEAT-like solenoid architecture. The accession/domain mapping itself derives from the supplied UniProt record rather than the cited papers. | Nucleocytoplasmic transport system; additional enrichment at cell cortex and muscle attachments | **High** for msk–DIM-7–Importin-7 identity; domain architecture is database-supported and family-concordant. | Baker et al. (September 2002), [10.1093/genetics/162.1.285](https://doi.org/10.1093/genetics/162.1.285); Liu & Geisbrecht (January 2012), [10.4161/cam.19774](https://doi.org/10.4161/cam.19774) (liu2012“importin”signalingroles pages 4-4, baker2002geneticinteractionbetween pages 1-2) |
| Activated ERK nuclear import | Two non-overlapping **msk/Dim7** dsRNAs produced a **4–5-fold decrease in nuclear doubly phosphorylated ERK (dpERK)** in spreading or insulin-stimulated integrin-expressing S2 cells. Xenopus Importin-7 rescued the defect; DIM-7 also co-immunoprecipitated with activated ERK. | Nuclear accumulation downstream of insulin/RTK and αPS2βPS-integrin signaling in S2 cells; nuclear dpERK in embryos | **High** for requirement in activated ERK nuclear accumulation and conserved transport activity. Lack of reciprocal cytoplasmic dpERK accumulation means effects on stability or signaling may accompany transport. | James et al. (October 2007), [10.1091/mbc.e06-07-0659](https://doi.org/10.1091/mbc.e06-07-0659) (james2007nuclearlocalizationof pages 2-3) |
| Phosphorylated Mad/Smad import | Genome-wide RNAi followed by a second non-overlapping dsRNA showed that Msk depletion blocked nuclear concentration of activated Mad without reducing C-terminal phosphorylation. After Dpp stimulation, the phospho-Mad nuclear:cytoplasmic ratio fell from **2.9 to 1.1**. | Dpp/BMP-responsive S2/S2R+ cells and developing eye imaginal disc nuclei | **High** for a post-phosphorylation role in phospho-Mad nuclear accumulation. Mammalian Imp7/Imp8–Smad transport supports conservation but is not itself fly evidence. | Xu et al. (17 September 2007), [10.1083/jcb.200703106](https://doi.org/10.1083/jcb.200703106) (xu2007mskisrequired pages 2-3) |
| Myotendinous-junction function and Vein–EGFR–MAPK signaling | Msk accumulates at embryonic muscle ends; **msk** mutants form unstable attachments despite retention of major integrin/ECM components, lose junctional phospho-FAK, and show reduced tendon Stripe and activated MAPK. Muscle-specific Msk, activated MAPK, or secreted Vein rescues attachment defects, supporting a muscle-to-tendon signal. | Cytoplasmic/cortical muscle attachment sites; non-autonomous maturation or maintenance of adjacent tendon cells | **High** for muscle-autonomous Msk requirement and junctional localization; **moderate–high** for the inferred sequence Msk→Vein→tendon EGFR–MAPK because rescue establishes pathway sufficiency/order more strongly than direct regulation of Vein secretion. | Liu & Geisbrecht (15 November 2011), [10.1016/j.ydbio.2011.08.028](https://doi.org/10.1016/j.ydbio.2011.08.028) (liu2011moleskinisessential pages 1-2, liu2011moleskinisessential pages 12-13) |
| Integrin–Dim7–Elmo–Mbc–Rac attachment pathway | Dim7 associates with Elmo/Mbc by proteomics, pulldown, immunoisolation, and in-situ proximity ligation. Elmo–Mbc, activated Elmo, or RacV12 rescues **msk** attachment defects; genetic interactions place Dim7 upstream of Elmo–Mbc–Rac. Integrin depletion attenuates Dim7 and activated-Elmo enrichment at attachment sites. | Embryonic and larval muscle ends/myotendinous junctions; also muscle Z-discs | **High** for local association, integrin-dependent enrichment, and pathway epistasis; **moderate** for direct binding and mechanistic activation of Rac because association and genetic ordering do not alone define a biochemical reaction. This is an important noncanonical, junctional role distinct from demonstrated nuclear cargo import. | Liu et al. (15 November 2013), [10.1242/jcs.132241](https://doi.org/10.1242/jcs.132241) (liu2013drosophilaimportin7functions pages 4-7, liu2013drosophilaimportin7functions pages 1-4, liu2013drosophilaimportin7functions pages 10-13) |
| Adult muscle-precursor proliferation and Wg signaling | Myoblast-specific Msk loss reduces the adult muscle precursor pool by impaired proliferation rather than increased death and eliminates indirect flight-muscle formation. Msk reduction removes Vestigial, nuclear Armadillo/β-catenin, and the Wg target Ladybird; the normal precursor population expands to about **2,500 myoblasts within 120 h**. | Wing-disc-associated larval adult muscle precursors; indirect flight-muscle lineage | **High** for developmental requirement and reduced Wg readouts; **moderate/uncertain** for direct Armadillo transport because altered stability, signaling, or indirect transcriptional effects were not excluded. | Vishal et al. (May 2017), [10.1534/genetics.116.193813](https://doi.org/10.1534/genetics.116.193813) (vishal2017adultmuscleformation pages 1-2, vishal2017adultmuscleformation pages 2-3) |
| Mechanosensitive Yorkie cargo (fly evidence) | In flies, Msk depletion reduced nuclear Yorkie (Yki) and Yki-driven tissue growth; Msk bound Yki under high-tension conditions, whereas deleting Yki’s terminal seven residues prevented binding. Constitutively active Yki-S168A retained Msk binding under semi-detached/low-tension conditions, and Msk localization itself changed with tension. | *Drosophila* wing epithelium and fly-cell tension paradigms; nuclear Yki accumulation | **High** that Msk regulates tension-dependent Yki binding/nuclear accumulation and Yki-driven growth; this 2022 work expands Msk’s experimentally supported fly cargo repertoire and connects nuclear import to mechanotransduction. | García-García et al. (1 March 2022), [10.1038/s41467-022-28693-y](https://doi.org/10.1038/s41467-022-28693-y) (garciagarcia2022mechanicalcontrolof pages 9-10) |
| YAP-dominant cargo competition (comparative mammalian evidence) | Mammalian Imp7 imports YAP; under high tension, YAP–Imp7 association favors YAP nuclear entry while restricting Imp7 association and nuclear translocation of Smad3 and ERK2. Under low tension, Hippo-pathway phosphorylation of YAP S127 prevents Imp7 binding, freeing Imp7 for other cargos. | Primarily mammalian RPE-1 and other cultured cells; actomyosin-, density-, and Hippo-dependent nuclear transport | **High for mammalian Imp7**, but **comparative/inferential for fly Msk**. Fly Msk–Yki transport is direct evidence; YAP-driven competition among Yki/Mad/ERK cargos has not been established in *Drosophila* and should not be assigned to Q9VSD6 as proven substrate competition. | García-García et al. (1 March 2022), [10.1038/s41467-022-28693-y](https://doi.org/10.1038/s41467-022-28693-y) (garciagarcia2022mechanicalcontrolof pages 1-2, garciagarcia2022mechanicalcontrolof pages 14-16) |


*Table: Compact evidence map for Drosophila Moleskin/Importin-7, separating direct fly experiments from conserved mammalian inference and reporting the strongest quantitative transport results.*

## 1. Molecular function and mechanism

### 1.1 Importin-7-type nuclear transport receptor

Importin-β-family receptors bind protein cargo in the cytoplasm, traverse nuclear-pore FG-repeat barriers, and release cargo in the RanGTP-rich nucleus. A 2022 mechanistic study describes every nuclear-transport receptor as possessing a RanGTP-binding motif and explains transport directionality through the nuclear RanGTP/GDP gradient. That study explicitly classifies Importin-7 as an importin-β-superfamily receptor capable of acting autonomously or with Importin-β1. Applying the detailed Ran cycle to fly Msk is strongly supported by homology and family architecture, although the retrieved fly experiments did not directly reconstitute a complete Msk–Ran transport cycle. (garciagarcia2022mechanicalcontrolof pages 1-2)

The supplied ARM-like and ARM-type-fold annotations are compatible with the extended α-solenoid architecture characteristic of importin-β-family proteins. These repeats provide a large, conformationally adaptable surface for binding Ran, cargoes, and nuclear-pore components. This is a structural/evolutionary inference, not evidence that each InterPro-labelled segment has been functionally dissected in Msk.

### 1.2 Activated ERK is a high-confidence cargo

DIM-7/Msk is required for nuclear accumulation of activated, doubly phosphorylated D-ERK downstream of receptor-tyrosine-kinase and integrin-associated signaling. In insulin-stimulated or spreading αPS2βPS-integrin-expressing S2 cells, two independent *msk* dsRNAs caused a **four- to fivefold reduction in nuclear dpERK**. DIM-7 co-immunoprecipitated with activated ERK, and Xenopus Importin-7 rescued the RNAi phenotype, supporting both cargo association and conserved transport activity. The absence of a matching increase in cytoplasmic dpERK leaves open additional effects on ERK stability or signaling, but the combined localization, association, RNAi, and cross-species rescue evidence strongly supports nuclear-import function. Published 17 October 2007; DOI: https://doi.org/10.1091/mbc.e06-07-0659. (james2007nuclearlocalizationof pages 2-3)

Msk also binds the Drosophila SHP-2 ortholog Corkscrew, and genetic interactions connect *msk* with integrins. However, suppression of integrin-induced wing blistering was not simply explained by loss of nuclear ERK import, suggesting that Msk can influence cytoplasmic or junctional signaling independently of its canonical transport activity. Published September 2002; DOI: https://doi.org/10.1093/genetics/162.1.285. (baker2002geneticinteractionbetween pages 1-2)

### 1.3 Phosphorylated Mad is a high-confidence cargo

A genome-wide RNAi screen identified *msk* as necessary for nuclear accumulation of phosphorylated Mad, the Drosophila BMP/Dpp-pathway R-Smad. A second non-overlapping dsRNA reproduced the result. Crucially, Msk depletion did **not** reduce receptor-mediated C-terminal Mad phosphorylation, locating Msk’s action downstream of activation. Following Dpp stimulation, depletion changed the endogenous phospho-Mad nuclear:cytoplasmic ratio from **2.9 to 1.1**. Thus, Msk controls nuclear concentration of activated Mad rather than its phosphorylation. Published 17 September 2007; DOI: https://doi.org/10.1083/jcb.200703106. (xu2007mskisrequired pages 2-3)

Mammalian Importin-7 and Importin-8 similarly support BMP-activated Smad1 and TGF-β-activated Smad2/3 import, reinforcing evolutionary conservation. Nevertheless, mammalian Smad results should not be used to assign every mammalian cargo automatically to fly Msk. (xu2007mskisrequired pages 2-3)

### 1.4 Yorkie: the latest substantial fly cargo assignment

The newest direct mechanistic advance recovered was published on **1 March 2022**, not in 2023–2024. Msk bound the Hippo effector Yorkie (Yki) under conditions favoring high cellular tension, was required for Yki nuclear accumulation, and supported Yki-driven organ growth in vivo. Deleting Yki’s terminal seven residues prevented Msk binding. Constitutively active Yki-S168A retained Msk association under semi-detached/low-tension conditions, and Msk localization itself responded to tension. DOI: https://doi.org/10.1038/s41467-022-28693-y. (garciagarcia2022mechanicalcontrolof pages 9-10)

In mammalian cells, the same study found that Importin-7 imports YAP and that YAP acts as a dominant, mechanically regulated cargo. Under high tension, YAP–Importin-7 formation favors YAP nuclear entry while restricting Smad3 and ERK2 access; under low tension, Hippo-pathway phosphorylation of YAP S127 inhibits Importin-7 binding. This establishes a cargo-competition mechanism for mammalian Importin-7. The fly Msk–Yki interaction is directly demonstrated, but Yki-mediated competition against Mad or ERK has **not** been demonstrated in flies and should remain a testable hypothesis rather than a Q9VSD6 annotation. (garciagarcia2022mechanicalcontrolof pages 1-2, garciagarcia2022mechanicalcontrolof pages 14-16)

## 2. Subcellular localization

Msk is best regarded as a **dynamic nucleocytoplasmic and cortical/junctional protein**, rather than as constitutively nuclear.

* During its canonical function, it operates between cytoplasm, nuclear pore, and nucleus to promote nuclear accumulation of activated ERK, phospho-Mad, and Yki. The measured endpoint in most fly assays is cargo localization rather than stable nuclear accumulation of Msk itself. (xu2007mskisrequired pages 2-3, james2007nuclearlocalizationof pages 2-3, garciagarcia2022mechanicalcontrolof pages 9-10)
* In embryos, DIM-7 is broadly expressed through approximately stage 12 and becomes strongly enriched at muscle ends after stage 15, overlapping βPS-integrin at muscle–tendon attachment sites. YFP-DIM-7 can also enrich along lateral muscle edges. Loss of staining in *msk* mutants supports antibody specificity. (liu2012“importin”signalingroles pages 4-4)
* In larval muscles, Msk persists at myotendinous junctions and is also enriched at Z-discs. In-situ proximity ligation places Msk–Elmo complexes at embryonic attachment sites and actively contracting larval junctions. (liu2013drosophilaimportin7functions pages 10-13)
* Endogenous nuclear Msk was not clearly detected in embryonic muscle, and overexpressed YFP-Msk nuclear localization was judged inconclusive. Consequently, Msk’s muscle-attachment role should not be reduced to nuclear ERK transport; substantial evidence supports a local cytoplasmic/junctional function. (liu2011moleskinisessential pages 12-13)

## 3. Pathway functions

### 3.1 Integrin–Msk–Elmo–Mbc–Rac signaling at muscle attachments

Msk and Elmo accumulate at myofiber ends during late myogenesis. Proteomic and biochemical evidence detected Dim7 in Elmo and Mbc preparations, while pulldown, immunoisolation, and proximity-ligation assays support a local complex. Genetic epistasis is particularly informative: Elmo–Mbc, activated Elmo, or constitutively active Rac rescued *msk* detachment phenotypes, placing Msk upstream of the Elmo–Mbc–Rac module. Conversely, reducing pathway components modified Msk/Elmo gain- and loss-of-function phenotypes. (liu2013drosophilaimportin7functions pages 1-4, liu2013drosophilaimportin7functions pages 10-13, liu2013drosophilaimportin7functions pages 26-29)

Integrin-complex depletion attenuated junctional Msk and activated-Elmo enrichment. The resulting model is **integrin-dependent recruitment or regulation of Msk → local Elmo–Mbc/Rac activation → actin remodeling and attachment stability**. Association and epistasis do not yet reveal whether Msk directly activates Elmo biochemically; “scaffold/regulator” is therefore more accurate than “enzyme.” Published 15 November 2013; DOI: https://doi.org/10.1242/jcs.132241. (liu2013drosophilaimportin7functions pages 4-7, liu2013drosophilaimportin7functions pages 1-4)

### 3.2 Muscle-to-tendon Vein–EGFR–MAPK signaling

In *msk* mutants, major integrin-complex and extracellular-matrix components can remain localized, but junctional phospho-FAK is disrupted and tendon-cell Stripe and activated MAPK decline. Muscle-specific Msk rescue, together with rescue by activated MAPK or secreted Vein, supports a muscle-autonomous Msk requirement that non-autonomously promotes adjacent tendon maturation through **Vein–EGFR–MAPK** signaling. Msk is thus needed more for maturation and maintenance of a mechanically stable junction than for the initial positioning of the attachment. Published 15 November 2011; DOI: https://doi.org/10.1016/j.ydbio.2011.08.028. (liu2011moleskinisessential pages 1-2, liu2011moleskinisessential pages 12-13)

### 3.3 Wg/β-catenin-associated adult muscle precursor proliferation

Msk is required during larval amplification of wing-disc-associated adult muscle precursors. Loss reduces precursor proliferation rather than increasing cell death and can eliminate indirect flight-muscle formation. Msk depletion also removes Vestigial, nuclear Armadillo/β-catenin, and the Wg target Ladybird. The normal population expands to approximately **2,500 myoblasts within 120 hours**. These findings establish a role in Wg-pathway output, but do not yet prove Armadillo is a direct Msk cargo; altered Arm stability or an indirect signaling effect remains possible. Published May 2017; DOI: https://doi.org/10.1534/genetics.116.193813. (vishal2017adultmuscleformation pages 1-2)

## 4. Biological processes and phenotypes

Loss-of-function evidence implicates *msk* in embryonic muscle–tendon adhesion, junctional maintenance under contraction, eye and wing growth, neuronal/photoreceptor development, adult muscle-precursor proliferation, and indirect flight-muscle formation. Mutant embryos exhibit missing muscles, guidance abnormalities, and widespread muscle detachment; larval muscle RNAi against *msk*, *elmo*, or *mbc* causes pupal lethality, missing or thinned fibers, and occasional detachment. These phenotypes are biologically important, but the strongest mechanistic annotation remains protein nuclear import plus localized junctional signaling—not a generic designation as a muscle-development gene. (baker2002geneticinteractionbetween pages 1-2, liu2013drosophilaimportin7functions pages 4-7, liu2012“importin”signalingroles pages 4-4, vishal2017adultmuscleformation pages 1-2)

## 5. Current applications and real-world implementation

There is no clinical or industrial implementation specific to fly Msk/Q9VSD6. Its present applications are experimental:

1. **Nuclear-transport model:** S2/S2R+ RNAi and cargo-localization assays provide tractable systems for dissecting non-classical nuclear import of activated ERK and Smads. (xu2007mskisrequired pages 2-3, james2007nuclearlocalizationof pages 2-3)
2. **Mechanotransduction model:** Fly wing and cell-tension paradigms connect integrin/cytoskeletal tension to Msk-dependent Yki import and organ growth. (garciagarcia2022mechanicalcontrolof pages 9-10)
3. **Myotendinous-junction model:** Tissue-specific RNAi, rescue, proximity ligation, and epistasis allow separation of nuclear-transport activity from local adhesion/scaffolding roles. (liu2013drosophilaimportin7functions pages 10-13, liu2011moleskinisessential pages 1-2)
4. **Conservation studies:** Rescue by Xenopus Importin-7 and parallel mammalian Importin-7 cargo biology make Msk useful for testing evolutionarily conserved transport mechanisms. (james2007nuclearlocalizationof pages 2-3, garciagarcia2022mechanicalcontrolof pages 1-2)

## 6. Recent-literature assessment and expert interpretation

Targeted searches found **no 2023–2024 primary study that materially revised the molecular annotation of Q9VSD6**. A 2023 review of Drosophila tendon diversity places muscle–tendon signaling in a modern developmental context, but the latest substantive direct Msk mechanism found remains the 2022 Msk–Yki/Importin-7–YAP mechanotransduction study. Accordingly, foundational 2007–2017 primary papers remain the authoritative evidence for ERK, Mad, junctional, and precursor-proliferation functions.

The evidence supports two connected but separable functional modes:

* **Canonical transport mode:** Msk recognizes selected activated protein cargoes and promotes their nuclear accumulation through an importin/Ran pathway.
* **Noncanonical junctional mode:** Msk concentrates at integrin-rich muscle attachments, associates with Elmo/Mbc, and organizes signaling needed for Rac-dependent cytoskeletal stability and Vein-dependent tendon maturation.

The major unresolved questions are whether Msk directly transports additional proposed cargos such as Armadillo, how Ran dependence is implemented for each fly cargo, whether junctional Msk undergoes regulated release into a nuclear-import pool, and whether the mammalian YAP-driven cargo hierarchy among YAP, Smad3, and ERK2 also exists among fly Yki, Mad, and D-ERK. These distinctions prevent overannotation while preserving the strong mechanistic conclusions supported by current evidence.

References

1. (liu2012“importin”signalingroles pages 4-4): Ze (Cindy) Liu and Erika R. Geisbrecht. “importin” signaling roles for import proteins. Cell Adhesion & Migration, 6:12-4-89, Jan 2012. URL: https://doi.org/10.4161/cam.19774, doi:10.4161/cam.19774. This article has 8 citations and is from a peer-reviewed journal.

2. (james2007nuclearlocalizationof pages 2-3): Brian P. James, Thomas A. Bunch, Srinivasan Krishnamoorthy, Lizabeth A. Perkins, and Danny L. Brower. Nuclear localization of the erk map kinase mediated by<i>drosophila</i>αps2βps integrin and importin-7. Oct 2007. URL: https://doi.org/10.1091/mbc.e06-07-0659, doi:10.1091/mbc.e06-07-0659. This article has 44 citations and is from a domain leading peer-reviewed journal.

3. (baker2002geneticinteractionbetween pages 1-2): Scott E Baker, James A Lorenzen, Steven W Miller, Thomas A Bunch, Alison L Jannuzi, Mark H Ginsberg, Lizabeth A Perkins, and Danny L Brower. Genetic interaction between integrins and <i>moleskin</i>, a gene encoding a drosophila homolog of importin-7. Sep 2002. URL: https://doi.org/10.1093/genetics/162.1.285, doi:10.1093/genetics/162.1.285. This article has 39 citations and is from a domain leading peer-reviewed journal.

4. (xu2007mskisrequired pages 2-3): Lan Xu, Xiaohao Yao, Xiaochu Chen, Peiyuan Lu, Biliang Zhang, and Y. Tony Ip. Msk is required for nuclear import of tgf-β/bmp-activated smads. The Journal of Cell Biology, 178:981-994, Sep 2007. URL: https://doi.org/10.1083/jcb.200703106, doi:10.1083/jcb.200703106. This article has 105 citations.

5. (liu2013drosophilaimportin7functions pages 1-4): Ze Cindy Liu, Nadia Odell, and Erika R. Geisbrecht. Drosophila importin-7 functions upstream of the elmo signaling module to mediate the formation and stability of muscle attachments. Journal of Cell Science, 126:5210-5223, Nov 2013. URL: https://doi.org/10.1242/jcs.132241, doi:10.1242/jcs.132241. This article has 13 citations and is from a domain leading peer-reviewed journal.

6. (liu2011moleskinisessential pages 1-2): Ze (Cindy) Liu and Erika R. Geisbrecht. Moleskin is essential for the formation of the myotendinous junction in drosophila. Developmental biology, 359 2:176-89, Nov 2011. URL: https://doi.org/10.1016/j.ydbio.2011.08.028, doi:10.1016/j.ydbio.2011.08.028. This article has 21 citations and is from a peer-reviewed journal.

7. (garciagarcia2022mechanicalcontrolof pages 9-10): María García-García, Sara Sánchez-Perales, Patricia Jarabo, Enrique Calvo, Trevor Huyton, Liran Fu, Sheung Chun Ng, Laura Sotodosos-Alonso, Jesús Vázquez, Sergio Casas-Tintó, Dirk Görlich, Asier Echarri, and Miguel A. Del Pozo. Mechanical control of nuclear import by importin-7 is regulated by its dominant cargo yap. Nature Communications, Mar 2022. URL: https://doi.org/10.1038/s41467-022-28693-y, doi:10.1038/s41467-022-28693-y. This article has 83 citations and is from a highest quality peer-reviewed journal.

8. (liu2011moleskinisessential pages 12-13): Ze (Cindy) Liu and Erika R. Geisbrecht. Moleskin is essential for the formation of the myotendinous junction in drosophila. Developmental biology, 359 2:176-89, Nov 2011. URL: https://doi.org/10.1016/j.ydbio.2011.08.028, doi:10.1016/j.ydbio.2011.08.028. This article has 21 citations and is from a peer-reviewed journal.

9. (liu2013drosophilaimportin7functions pages 4-7): Ze Cindy Liu, Nadia Odell, and Erika R. Geisbrecht. Drosophila importin-7 functions upstream of the elmo signaling module to mediate the formation and stability of muscle attachments. Journal of Cell Science, 126:5210-5223, Nov 2013. URL: https://doi.org/10.1242/jcs.132241, doi:10.1242/jcs.132241. This article has 13 citations and is from a domain leading peer-reviewed journal.

10. (liu2013drosophilaimportin7functions pages 10-13): Ze Cindy Liu, Nadia Odell, and Erika R. Geisbrecht. Drosophila importin-7 functions upstream of the elmo signaling module to mediate the formation and stability of muscle attachments. Journal of Cell Science, 126:5210-5223, Nov 2013. URL: https://doi.org/10.1242/jcs.132241, doi:10.1242/jcs.132241. This article has 13 citations and is from a domain leading peer-reviewed journal.

11. (vishal2017adultmuscleformation pages 1-2): Kumar Vishal, David S Brooks, Simranjot Bawa, Samantha Gameros, Marta Stetsiv, and Erika R Geisbrecht. Adult muscle formation requires <i>drosophila</i> moleskin for proliferation of wing disc-associated muscle precursors. May 2017. URL: https://doi.org/10.1534/genetics.116.193813, doi:10.1534/genetics.116.193813. This article has 10 citations and is from a domain leading peer-reviewed journal.

12. (vishal2017adultmuscleformation pages 2-3): Kumar Vishal, David S Brooks, Simranjot Bawa, Samantha Gameros, Marta Stetsiv, and Erika R Geisbrecht. Adult muscle formation requires <i>drosophila</i> moleskin for proliferation of wing disc-associated muscle precursors. May 2017. URL: https://doi.org/10.1534/genetics.116.193813, doi:10.1534/genetics.116.193813. This article has 10 citations and is from a domain leading peer-reviewed journal.

13. (garciagarcia2022mechanicalcontrolof pages 1-2): María García-García, Sara Sánchez-Perales, Patricia Jarabo, Enrique Calvo, Trevor Huyton, Liran Fu, Sheung Chun Ng, Laura Sotodosos-Alonso, Jesús Vázquez, Sergio Casas-Tintó, Dirk Görlich, Asier Echarri, and Miguel A. Del Pozo. Mechanical control of nuclear import by importin-7 is regulated by its dominant cargo yap. Nature Communications, Mar 2022. URL: https://doi.org/10.1038/s41467-022-28693-y, doi:10.1038/s41467-022-28693-y. This article has 83 citations and is from a highest quality peer-reviewed journal.

14. (garciagarcia2022mechanicalcontrolof pages 14-16): María García-García, Sara Sánchez-Perales, Patricia Jarabo, Enrique Calvo, Trevor Huyton, Liran Fu, Sheung Chun Ng, Laura Sotodosos-Alonso, Jesús Vázquez, Sergio Casas-Tintó, Dirk Görlich, Asier Echarri, and Miguel A. Del Pozo. Mechanical control of nuclear import by importin-7 is regulated by its dominant cargo yap. Nature Communications, Mar 2022. URL: https://doi.org/10.1038/s41467-022-28693-y, doi:10.1038/s41467-022-28693-y. This article has 83 citations and is from a highest quality peer-reviewed journal.

15. (liu2013drosophilaimportin7functions pages 26-29): Ze Cindy Liu, Nadia Odell, and Erika R. Geisbrecht. Drosophila importin-7 functions upstream of the elmo signaling module to mediate the formation and stability of muscle attachments. Journal of Cell Science, 126:5210-5223, Nov 2013. URL: https://doi.org/10.1242/jcs.132241, doi:10.1242/jcs.132241. This article has 13 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](msk-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. james2007nuclearlocalizationof pages 2-3
2. xu2007mskisrequired pages 2-3
3. garciagarcia2022mechanicalcontrolof pages 9-10
4. garciagarcia2022mechanicalcontrolof pages 1-2
5. baker2002geneticinteractionbetween pages 1-2
6. liu2011moleskinisessential pages 12-13
7. vishal2017adultmuscleformation pages 1-2
8. liu2011moleskinisessential pages 1-2
9. vishal2017adultmuscleformation pages 2-3
10. garciagarcia2022mechanicalcontrolof pages 14-16
11. 10.1093/genetics/162.1.285
12. 10.4161/cam.19774
13. 10.1091/mbc.e06-07-0659
14. 10.1083/jcb.200703106
15. 10.1016/j.ydbio.2011.08.028
16. 10.1242/jcs.132241
17. 10.1534/genetics.116.193813
18. 10.1038/s41467-022-28693-y
19. https://doi.org/10.1093/genetics/162.1.285
20. https://doi.org/10.4161/cam.19774
21. https://doi.org/10.1091/mbc.e06-07-0659
22. https://doi.org/10.1083/jcb.200703106
23. https://doi.org/10.1016/j.ydbio.2011.08.028
24. https://doi.org/10.1242/jcs.132241
25. https://doi.org/10.1534/genetics.116.193813
26. https://doi.org/10.1038/s41467-022-28693-y
27. https://doi.org/10.1091/mbc.e06-07-0659.
28. https://doi.org/10.1093/genetics/162.1.285.
29. https://doi.org/10.1083/jcb.200703106.
30. https://doi.org/10.1038/s41467-022-28693-y.
31. https://doi.org/10.1242/jcs.132241.
32. https://doi.org/10.1016/j.ydbio.2011.08.028.
33. https://doi.org/10.1534/genetics.116.193813.
34. https://doi.org/10.4161/cam.19774,
35. https://doi.org/10.1091/mbc.e06-07-0659,
36. https://doi.org/10.1093/genetics/162.1.285,
37. https://doi.org/10.1083/jcb.200703106,
38. https://doi.org/10.1242/jcs.132241,
39. https://doi.org/10.1016/j.ydbio.2011.08.028,
40. https://doi.org/10.1038/s41467-022-28693-y,
41. https://doi.org/10.1534/genetics.116.193813,