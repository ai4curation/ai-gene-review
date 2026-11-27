---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-26T20:24:31.964410'
end_time: '2026-09-26T20:31:00.224055'
duration_seconds: 388.26
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: yeast
  gene_id: RLF2
  gene_symbol: RLF2
  uniprot_accession: Q12495
  protein_description: 'RecName: Full=Chromatin assembly factor 1 subunit A {ECO:0000250|UniProtKB:Q13111};
    Short=CAF-1 subunit A {ECO:0000250|UniProtKB:Q13111}; AltName: Full=CAF-1 90 kDa
    subunit; AltName: Full=Chromatin assembly factor 1 subunit p90 {ECO:0000305};
    AltName: Full=RAP1 localization factor 2;'
  gene_info: Name=RLF2; Synonyms=CAC1; OrderedLocusNames=YPR018W; ORFNames=YP9531.12;
  organism_full: Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
  protein_family: Belongs to the RLF2 family. .
  protein_domains: Cac1-like_C. (IPR048800); CAF-1_p150_acidic. (IPR021644); CAF1A_DD.
    (IPR022043); Cac1_C (PF21796); CAF1A_acidic (PF11600)
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
  path: RLF2-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** Q12495
- **Protein Description:** RecName: Full=Chromatin assembly factor 1 subunit A {ECO:0000250|UniProtKB:Q13111}; Short=CAF-1 subunit A {ECO:0000250|UniProtKB:Q13111}; AltName: Full=CAF-1 90 kDa subunit; AltName: Full=Chromatin assembly factor 1 subunit p90 {ECO:0000305}; AltName: Full=RAP1 localization factor 2;
- **Gene Information:** Name=RLF2; Synonyms=CAC1; OrderedLocusNames=YPR018W; ORFNames=YP9531.12;
- **Organism (full):** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
- **Protein Family:** Belongs to the RLF2 family. .
- **Key Domains:** Cac1-like_C. (IPR048800); CAF-1_p150_acidic. (IPR021644); CAF1A_DD. (IPR022043); Cac1_C (PF21796); CAF1A_acidic (PF11600)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "RLF2" matches the protein description above**
2. **Verify the organism is correct:** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'RLF2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **RLF2** (gene ID: RLF2, UniProt: Q12495) in yeast.

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
- **UniProt Accession:** Q12495
- **Protein Description:** RecName: Full=Chromatin assembly factor 1 subunit A {ECO:0000250|UniProtKB:Q13111}; Short=CAF-1 subunit A {ECO:0000250|UniProtKB:Q13111}; AltName: Full=CAF-1 90 kDa subunit; AltName: Full=Chromatin assembly factor 1 subunit p90 {ECO:0000305}; AltName: Full=RAP1 localization factor 2;
- **Gene Information:** Name=RLF2; Synonyms=CAC1; OrderedLocusNames=YPR018W; ORFNames=YP9531.12;
- **Organism (full):** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
- **Protein Family:** Belongs to the RLF2 family. .
- **Key Domains:** Cac1-like_C. (IPR048800); CAF-1_p150_acidic. (IPR021644); CAF1A_DD. (IPR022043); Cac1_C (PF21796); CAF1A_acidic (PF11600)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "RLF2" matches the protein description above**
2. **Verify the organism is correct:** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'RLF2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **RLF2** (gene ID: RLF2, UniProt: Q12495) in yeast.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Research report: *Saccharomyces cerevisiae* RLF2/CAC1 (UniProt Q12495)

## Executive conclusion

RLF2 is unambiguously the same budding-yeast gene as **CAC1** (ordered locus **YPR018W**) and encodes the large, approximately 90-kDa subunit of chromatin assembly factor 1 (CAF-1). It is the yeast counterpart of metazoan CHAF1A/p150. The literature examined concerns *Saccharomyces cerevisiae* and is consistent with the supplied S288c/Q12495 record; no similarly named gene from another organism was substituted. Independent primary studies explicitly identify RLF2 with CAC1 and connect it to the large CAF-1 subunit. (kaufman1997ultravioletradiationsensitivity pages 1-2, enomoto1998chromatinassemblyfactor pages 1-2, enomoto1997rlf2asubunit pages 1-2)

Cac1/Rlf2 is **not an enzyme** and has no catalytic reaction or small-molecule substrate specificity. It is a nuclear histone-chaperone scaffold. In the heterotrimeric CAF-1 complex, it coordinates Cac2, Cac3/Msi1, histones H3–H4, DNA, and the sliding clamp PCNA. Its primary molecular function is to couple DNA synthesis to deposition of newly synthesized H3–H4, generating the tetrasome precursor of a nucleosome. This restores chromatin behind replication forks and at synthesis-dependent DNA-repair sites. (zhang2016adnabinding pages 1-2, mattiroli2017dnamediatedassociationof pages 1-2, mattiroli2017dnamediatedassociationof pages 4-6)

| Annotation aspect | Best-supported conclusion | Evidence type / strength | Key quantitative or mechanistic detail | Principal source / year |
|---|---|---|---|---|
| Identity | **RLF2 is identical to CAC1** in *Saccharomyces cerevisiae* and encodes the large CAF-1 subunit; this matches the supplied Q12495/YPR018W identity. | Direct genetic and biochemical evidence; strong | Independently identified as the yeast counterpart of the human p150 CAF-1 subunit. | Kaufman et al., 1997; Enomoto et al., 1997; Enomoto & Berman, 1998 (kaufman1997ultravioletradiationsensitivity pages 1-2, enomoto1998chromatinassemblyfactor pages 1-2, enomoto1997rlf2asubunit pages 1-2) |
| Molecular class | Cac1/Rlf2 is a **nonenzymatic histone chaperone and scaffold**, not an enzyme; no catalytic reaction or conventional substrate specificity is known. | Biochemical reconstitution and structural studies; strong | It coordinates histone, DNA, PCNA, and CAF-1-subunit interactions to promote chromatin assembly. | Zhang et al., 2016; Mattiroli et al., 2017 (zhang2016adnabinding pages 1-2, mattiroli2017dnamediatedassociationof pages 1-2) |
| CAF-1 composition | Yeast CAF-1 is a heterotrimer of **Cac1, Cac2, and Cac3/Msi1**; Cac1 is the large structural and functional subunit. | Purification, sequence comparison, and reconstitution; strong | Cac1, Cac2, and Cac3 correspond broadly to human p150, p60, and p48-family subunits, respectively. | Kaufman et al., 1997; Mattiroli et al., 2017 (kaufman1997ultravioletradiationsensitivity pages 1-2, kaufman1997ultravioletradiationsensitivity pages 5-6, mattiroli2017dnamediatedassociationof pages 1-2) |
| Cargo and biological substrate | CAF-1 carries newly synthesized **H3–H4 dimers** and deposits an **(H3–H4)₂ tetramer** onto newly synthesized or repaired DNA. | Stoichiometric biochemistry; strong | One CAF-1 binds one H3–H4 dimer; a cross-linked tetramer binds two CAF-1 complexes, yielding an approximately 300-kDa species. | Mattiroli et al., 2017 (mattiroli2017dnamediatedassociationof pages 4-6) |
| Deposition mechanism | Histone binding activates Cac1 DNA engagement; two CAF-1·H3–H4 complexes meet on DNA, form the H3–H4 tetramer, and discharge it as a tetrasome. | EMSA, SEC-MALS, cross-linking, FRET, HX-MS, and assembly assays; strong | An 18-bp DNA bridges two WHDs; 33-bp DNA makes assembly tetramerization-dependent; 79-bp DNA supports complete histone discharge. Activity peaked at a twofold CAF-1 excess per H3–H4 tetramer. | Mattiroli et al., 2017 (mattiroli2017dnamediatedassociationof pages 10-12, mattiroli2017dnamediatedassociationof pages 2-4) |
| Domains and motifs | The supplied acidic CAF1A region and C-terminal Cac1-like domains agree with experimentally defined histone- and subunit-interaction regions and a C-terminal **winged-helix DNA-binding domain**. | Crystallography, mutagenesis, and biochemical binding; strong | Cac1 residues 520–606 form a WHD solved at 2.75 Å; DNA binding is sequence-independent. K564E/K568E disrupts the histone-activated DNA-bound intermediate without abolishing H3–H4 binding. | Zhang et al., 2016; Mattiroli et al., 2017 (zhang2016adnabinding pages 2-3, mattiroli2017dnamediatedassociationof pages 6-8) |
| Localization | Cac1 acts in the **nucleus**, particularly on nascent DNA at replication forks and at synthesis-dependent repair sites; its PCNA and DNA interactions stabilize fork association. | Functional interaction and fork-association evidence; strong | DNA-binding-defective and PCNA-binding-defective mutations show synergistic silencing and DNA-damage phenotypes. | Zhang et al., 2016 (zhang2016adnabinding pages 1-2) |
| Telomeric chromatin | Cac1 supports telomeric heterochromatin and normal Rap1 organization rather than serving only as a Rap1-specific localization factor. | Deletion genetics, reporter silencing, microscopy, and FISH; strong | Loss of RLF2/CAC1 causes reduced telomeric silencing, more numerous and diffuse Rap1 foci, and approximately **50% greater nuclear volume**, while subtelomeric DNA positioning remains broadly normal. | Enomoto et al., 1997 (enomoto1997rlf2asubunit pages 1-2) |
| HM-locus silencing | CAF-1 primarily promotes **maintenance**, rather than de novo re-establishment, of silent mating-type chromatin. | Targeted genetic epistasis and silencing assays; strong | Reintroduced SIR3 restored HML silencing in *cac1 sir3* cells but not in *sir1 sir3* cells; *sir1Δ cac1Δ* abolished residual silencing maintained in most *sir1Δ* cells. | Enomoto & Berman, 1998 (enomoto1998chromatinassemblyfactor pages 11-12, enomoto1998chromatinassemblyfactor pages 1-2) |
| DNA-damage response | CAF-1 is dispensable for ordinary vegetative viability but contributes to chromatin restoration after DNA damage. | Null-mutant survival assays and domain mutagenesis; strong | Deleting any CAF-1 subunit increases UV sensitivity without a comparable increase in γ-ray sensitivity; WHD mutations also increase damage sensitivity. | Kaufman et al., 1997; Zhang et al., 2016 (kaufman1997ultravioletradiationsensitivity pages 6-7, zhang2016adnabinding pages 1-2) |
| Genome-stability pathway | Emerging evidence links Cac1/CAF-1 to suppression of replication-associated rDNA recombination and extrachromosomal rDNA-circle formation. | Direct budding-yeast genetics and molecular assays, initially reported as a 2024-posted preprint; moderate/emerging | *cac1Δ* produced approximately fourfold higher E-pro transcription; instability depended on Fob1 and Rad52 and was associated with increased DSB-end resection and altered nucleosome-coupled lagging-strand synthesis. | Futami et al., preprint posted 2024 and updated 2025 (futami2025thehistonechaperone pages 28-31) |
| Recent mechanistic update | **Species warning: the 2024 experiments were performed in *Schizosaccharomyces pombe*, not Q12495-bearing *S. cerevisiae*.** They support, but do not directly prove, a conserved dynamic CAF-1 model. | NMR, SAXS, modeling, in-vitro biochemistry, and in-vivo mutagenesis; strong for *S. pombe*, indirect for Cac1 | *S. pombe* CAF-1 is a 1:1:1 complex measured at 179 kDa; one H3–H4 dimer gives a 193-kDa complex. DNA binding to 40-bp duplexes had EC₅₀ = 0.7 ± 0.1 µM and Hill coefficient 2.7 ± 0.2. Pcf1 shares only 16% sequence identity with ScCac1. | Ouasti et al., 20 February 2024 (ouasti2024disorderedregionsand pages 7-9, ouasti2024disorderedregionsand pages 2-4, ouasti2024disorderedregionsand pages 4-5, ouasti2024disorderedregionsand pages 1-2) |
| Current application | RLF2/CAC1 is principally a **research model** for replication-coupled nucleosome assembly, epigenetic inheritance, heterochromatin maintenance, and repair-coupled genome stability; no established clinical or industrial application was identified. | Assessment of the gathered literature; well supported as a research use | Experimental applications include silencing reporters, CAF-1 reconstitution, histone-deposition assays, replication-fork studies, and DNA-damage genetics. | Zhang et al., 2016; Mattiroli et al., 2017; Ouasti et al., 2024 (zhang2016adnabinding pages 1-2, mattiroli2017dnamediatedassociationof pages 1-2, ouasti2024disorderedregionsand pages 1-2) |


*Table: This table consolidates the strongest evidence for the identity, molecular function, mechanism, localization, pathways, and research uses of budding-yeast RLF2/CAC1. It also distinguishes direct Saccharomyces cerevisiae findings from the relevant but nonidentical 2024 Schizosaccharomyces pombe study.*

## 1. Identity verification and nomenclature

The mandatory identity checks are satisfied:

1. **Gene-symbol match:** Kaufman and colleagues explicitly reported that **CAC1 is identical to RLF2**. Enomoto and colleagues independently identified RLF2 as the large CAF-1 subunit and linked its loss to telomeric chromatin defects. (kaufman1997ultravioletradiationsensitivity pages 1-2, enomoto1997rlf2asubunit pages 1-2)
2. **Organism:** The relevant primary literature is in budding yeast, *Saccharomyces cerevisiae*, consistent with the supplied strain lineage S288c/ATCC 204508 and locus YPR018W. The report does not transfer findings from an unrelated RLF2 symbol.
3. **Protein family and complex:** Yeast CAF-1 is a heterotrimer of Cac1, Cac2, and Cac3/Msi1, corresponding broadly to the large p150, middle p60, and small p48-family subunits of metazoan CAF-1. Cac1 is therefore appropriately assigned to the RLF2/CAF1A-like family. (kaufman1997ultravioletradiationsensitivity pages 1-2, kaufman1997ultravioletradiationsensitivity pages 5-6, mattiroli2017dnamediatedassociationof pages 1-2)
4. **Domain correspondence:** The supplied CAF1A acidic, CAF1A_DD, Cac1-like_C, and Cac1_C annotations agree with experimentally demonstrated acidic histone-binding/subunit-assembly regions and the folded C-terminal Cac1 DNA-binding module. The crystallized Cac1 C terminus, residues 520–606, is a winged-helix domain (WHD), providing direct structural support for the C-terminal domain annotation. (zhang2016adnabinding pages 2-3, mattiroli2017dnamediatedassociationof pages 6-8)

The historical name “Rap1 localization factor 2” reflects the mutant phenotype through which RLF2 was identified; it should not be interpreted as making Cac1 a dedicated Rap1-transport or anchoring protein. Its primary function is CAF-1-mediated chromatin assembly.

## 2. Molecular function and substrate/cargo specificity

### 2.1 Functional class

CAF-1 is a histone chaperone rather than a catalyst. Cac1 supplies much of the complex’s interaction framework, while the assembled heterotrimer shields histone surfaces, engages nascent DNA, and promotes ordered histone transfer. No ATPase, transferase, nuclease, or other intrinsic catalytic activity has been demonstrated for Cac1. Its biologically relevant cargo is newly synthesized **H3–H4**, and its acceptor substrate is newly synthesized DNA or DNA undergoing repair-associated synthesis. (zhang2016adnabinding pages 1-2, mattiroli2017dnamediatedassociationof pages 1-2)

### 2.2 Mechanism of H3–H4 deposition

Detailed budding-yeast reconstitution established the following mechanism:

1. One CAF-1 heterotrimer binds **one H3–H4 dimer**, not a complete tetramer. FRET-based Job plots supported 1:1 CAF-1:dimer stoichiometry. A cross-linked H3–H4 tetramer recruited two CAF-1 complexes and produced an approximately 300-kDa species by SEC-MALS. (mattiroli2017dnamediatedassociationof pages 4-6)
2. H3–H4 binding rearranges CAF-1 and activates Cac1’s WHD for DNA engagement. In the histone-free state, an acidic Cac1 segment at residues 397–431 helps restrain the WHD through an intramolecular interaction with the histone-binding module. (mattiroli2017dnamediatedassociationof pages 6-8)
3. DNA brings together two CAF-1·H3–H4 complexes. On an 18-bp duplex, two Cac1 WHDs form a bridged intermediate; the DNA is too short to wrap a tetramer, allowing this intermediate to be trapped. (mattiroli2017dnamediatedassociationof pages 10-12)
4. The exposed H3–H3′ interface permits the two CAF-1-bound dimers to form an **(H3–H4)₂ tetramer**. Assembly on 33-bp DNA becomes dependent on this tetramerization step. (mattiroli2017dnamediatedassociationof pages 10-12, mattiroli2017dnamediatedassociationof pages 4-6)
5. DNA long enough to accept the histones drives discharge from CAF-1. A 79-bp duplex generated the final tetramer–DNA product, whereas complete assembly assays produced protected fragments of approximately 125–160 bp and detected tetrasomes, hexasomes, and nucleosomes. Activity peaked around a twofold CAF-1 excess per H3–H4 tetramer. (mattiroli2017dnamediatedassociationof pages 10-12, mattiroli2017dnamediatedassociationof pages 2-4)

Thus, Cac1 does not merely bind histones. It implements a regulated handoff in which histone loading licenses DNA binding, two chaperone complexes cooperate, and DNA itself promotes histone release.

## 3. Domain architecture and interaction logic

The C-terminal WHD is the best structurally resolved Cac1 element. Its 2.75-Å structure comprises four helices, two antiparallel β-strands, and a long wing loop. A basic surface containing Lys553, Lys560, Lys564, Lys568, Arg573, Lys577, Arg582, and Lys583 supports sequence-independent DNA binding. (zhang2016adnabinding pages 2-3)

Functional mutagenesis reinforces this assignment. The K564E/K568E WHD mutant retains H3–H4 binding but fails to form the histone-activated DNA-bound intermediate, separating histone recognition from productive deposition. More generally, DNA-binding-defective WHD mutations impair transcriptional silencing and increase DNA-damage sensitivity; combining them with PCNA-binding-defective Cac1 mutations worsens the phenotypes. DNA binding and PCNA engagement therefore cooperate to retain CAF-1 at active DNA-synthesis sites. (zhang2016adnabinding pages 1-2, mattiroli2017dnamediatedassociationof pages 6-8)

The supplied acidic CAF1A region is also mechanistically credible: budding-yeast experiments place an acidic regulatory segment within the histone-responsive interaction network, and the assembled histone-binding module includes Cac1 and Cac2. The exact boundaries used by InterPro/Pfam need not coincide perfectly with experimental truncations, but the functional assignments are concordant. (mattiroli2017dnamediatedassociationof pages 6-8)

## 4. Cellular localization

Cac1 functions in the **nucleus**, on chromosomal DNA. Its most precise functional localization is transient rather than a fixed organelle compartment:

- **Replication forks and newly replicated DNA:** Cac1 binds PCNA and DNA, positioning CAF-1 behind the replisome for replication-coupled nucleosome assembly. Direct disruption of WHD-mediated DNA binding destabilizes fork association, especially when PCNA binding is also impaired. (zhang2016adnabinding pages 1-2, mattiroli2017dnamediatedassociationof pages 1-2)
- **DNA-repair synthesis sites:** CAF-1 is recruited in the context of PCNA-dependent repair synthesis and restores H3–H4 chromatin after DNA damage. The ultraviolet sensitivity of CAF-1-null mutants supports a repair-associated role. (kaufman1997ultravioletradiationsensitivity pages 6-7, kaufman1997ultravioletradiationsensitivity pages 1-2)
- **Silent chromatin:** Cac1-dependent assembly contributes to telomeric and HM-locus chromatin. This is a functional chromosomal localization rather than evidence that Cac1 is a permanent structural component of telomeres. (enomoto1998chromatinassemblyfactor pages 1-2, enomoto1997rlf2asubunit pages 1-2)

## 5. Biological pathways

### 5.1 Replication-coupled nucleosome assembly

This is the primary pathway. PCNA encircles newly synthesized DNA and provides a platform for CAF-1 recruitment; Cac1’s DNA- and PCNA-binding activities cooperate with histone-triggered conformational switching. CAF-1 deposits H3–H4 tetramers, after which H2A–H2B addition can complete nucleosomes. (zhang2016adnabinding pages 1-2, mattiroli2017dnamediatedassociationof pages 16-17, mattiroli2017dnamediatedassociationof pages 1-2)

### 5.2 Repair-coupled chromatin restoration

Deletion of CAC1, CAC2, or CAC3 does not prevent ordinary vegetative growth, showing that CAF-1 is nonessential under standard conditions. Nevertheless, each deletion increases UV sensitivity, and combining CAF-1-subunit mutations does not yield additive sensitivity, consistent with the three proteins acting in one complex. Comparable hypersensitivity to γ radiation was not observed in the original study. This pattern supports an important role in restoring chromatin during or after repair of UV lesions, while not implying exclusive action in nucleotide-excision repair. (kaufman1997ultravioletradiationsensitivity pages 6-7, kaufman1997ultravioletradiationsensitivity pages 1-2)

### 5.3 Telomeric chromatin and Rap1 organization

Loss of RLF2/CAC1 reduces repression of telomere-proximal reporters and alters the distribution of Rap1. Mutant nuclei contain more numerous and diffuse Rap1 foci and are approximately **50% larger**. FISH showed that subtelomeric DNA distribution remained broadly similar to wild type, arguing that the Rap1 phenotype was not simply caused by wholesale telomere repositioning. Cac1 therefore supports a chromatin environment needed for normal telomeric protein organization and transcriptional silencing. (kaufman1997ultravioletradiationsensitivity pages 6-7, enomoto1997rlf2asubunit pages 1-2)

### 5.4 Silent mating-type loci

CAF-1 contributes mainly to **maintenance** of silencing at HML/HMR. In genetic re-establishment experiments, reintroducing SIR3 restored HML repression in *cac1 sir3* cells but not in *sir1 sir3* cells. Moreover, most *sir1Δ* cells retained residual repression, whereas *sir1Δ cac1Δ* cells lost it. These results support a model in which CAF-1-built nucleosomes stabilize inheritance of silent chromatin but are not absolutely required to nucleate silencing anew. (enomoto1998chromatinassemblyfactor pages 11-12, enomoto1998chromatinassemblyfactor pages 1-2)

### 5.5 rDNA stability: emerging evidence

A study first posted in 2024 and updated as a 2025 preprint directly links budding-yeast CAF-1 to ribosomal-DNA stability. CAF-1 deficiency increased chromosomal rDNA variation and extrachromosomal rDNA circles in pathways requiring the fork-block protein Fob1 and homologous-recombination factor Rad52. The work reported approximately **fourfold greater E-pro transcription** in *cac1Δ*, increased DSB-end resection, and reduced nucleosome-scale Okazaki-fragment signatures behind arrested forks. The proposed mechanism is that CAF-1-dependent H3–H4 deposition restricts excessive resection and misaligned Rad52-mediated repair among repetitive rDNA copies. Because the evidence was initially a preprint and postdates the requested 2023–2024 priority window in its analyzed form, it should be regarded as strong emerging evidence rather than part of the older consensus. (futami2025thehistonechaperone pages 49-50, futami2025thehistonechaperone pages 28-31)

## 6. Recent developments, especially 2023–2024

Direct 2023–2024 mechanistic literature specifically centered on *S. cerevisiae* Cac1 is limited. The most relevant major 2024 structural study examined **Schizosaccharomyces pombe** CAF-1, not Q12495 and not *S. cerevisiae*. This distinction is essential.

Ouasti et al., version of record published **20 February 2024**, reconstituted the fission-yeast Pcf1/Pcf2/Pcf3 complex and used NMR, SAXS, modeling, biochemistry, and in-vivo mutants. The measured complex was 179 kDa, close to the calculated 167-kDa 1:1:1 assembly; binding one H3–H4 dimer produced a 193-kDa complex. Up to approximately one-quarter of Pcf1 remained disordered in the assembled state. An acidic region folded upon histone binding, while the KER helix mediated DNA binding and enhanced association with PCNA. For 40-bp DNA, the reported EC₅₀ was 0.7 ± 0.1 µM with a Hill coefficient of 2.7 ± 0.2. [DOI URL](https://doi.org/10.7554/eLife.91461). (ouasti2024disorderedregionsand pages 7-9, ouasti2024disorderedregionsand pages 4-5, ouasti2024disorderedregionsand pages 1-2)

These results support a conserved model in which CAF-1 uses flexible/disordered regions and folded modules to integrate histone, DNA, and PCNA binding. They do **not** establish every detail for budding-yeast Cac1: Pcf1 shares only 16% sequence identity with ScCac1, and the fission-yeast WHD did not behave identically to the budding-yeast DNA-binding WHD. The 2024 work should therefore be treated as evolutionary and mechanistic support, not direct annotation evidence for individual Q12495 residues. (ouasti2024disorderedregionsand pages 7-9, ouasti2024disorderedregionsand pages 2-4)

## 7. Current applications and expert assessment

RLF2/CAC1 currently has no established clinical, diagnostic, or industrial application. Its real-world use is as an experimental model for:

- replication-coupled nucleosome assembly and chromatin maturation;
- PCNA-mediated coordination of DNA synthesis with epigenome restoration;
- inheritance and maintenance of transcriptionally silent chromatin;
- chromatin restoration after DNA damage;
- genome stability at repetitive loci;
- biochemical reconstitution of histone deposition and structure–function analysis of histone chaperones.

The strongest expert-level interpretation is that Cac1 is the central organizing subunit of a regulated deposition machine. Its phenotypes in silencing and DNA-damage resistance are downstream consequences of this primary chromatin-assembly role, not evidence for separate catalytic or signaling activities. The convergence of genetics, crystallography, quantitative stoichiometry, and reconstituted deposition makes this interpretation substantially stronger than annotations derived only from high-throughput screens. (zhang2016adnabinding pages 1-2, mattiroli2017dnamediatedassociationof pages 16-17, mattiroli2017dnamediatedassociationof pages 4-6)

## 8. Evidence limitations

Several boundaries should be retained in functional annotation:

- “Nuclear/replication-fork localization” is best understood as recruitment to chromosomal sites of DNA synthesis through PCNA and DNA, not as residence in a membrane-bounded nuclear subcompartment.
- Telomeric, HM, and rDNA phenotypes demonstrate where defective chromatin assembly matters; they do not change the primary function from H3–H4 deposition to locus-specific signaling.
- The 2024 fission-yeast architecture is highly relevant but indirect for Q12495.
- Recent rDNA results were first disseminated as a preprint, whereas the foundational identity, silencing, structural, and deposition conclusions are supported by peer-reviewed primary studies.

## Selected authoritative sources

- Kaufman P, Kobayashi R, Stillman B. “Ultraviolet radiation sensitivity and reduction of telomeric silencing in *Saccharomyces cerevisiae* cells lacking chromatin assembly factor-I.” *Genes & Development* 11:345–357. **February 1997.** [https://doi.org/10.1101/gad.11.3.345](https://doi.org/10.1101/gad.11.3.345). (kaufman1997ultravioletradiationsensitivity pages 1-2)
- Enomoto S et al. “RLF2, a subunit of yeast chromatin assembly factor-I, is required for telomeric chromatin function in vivo.” *Genes & Development* 11:358–370. **February 1997.** [https://doi.org/10.1101/gad.11.3.358](https://doi.org/10.1101/gad.11.3.358). (enomoto1997rlf2asubunit pages 1-2)
- Enomoto S, Berman J. “Chromatin assembly factor I contributes to the maintenance, but not the re-establishment, of silencing at the yeast silent mating loci.” *Genes & Development* 12:219–232. **January 1998.** [https://doi.org/10.1101/gad.12.2.219](https://doi.org/10.1101/gad.12.2.219). (enomoto1998chromatinassemblyfactor pages 1-2)
- Zhang K et al. “A DNA binding winged helix domain in CAF-1 functions with PCNA to stabilize CAF-1 at replication forks.” *Nucleic Acids Research* 44:5083–5094. **22 February 2016 online.** [https://doi.org/10.1093/nar/gkw106](https://doi.org/10.1093/nar/gkw106). (zhang2016adnabinding pages 2-3, zhang2016adnabinding pages 1-2)
- Mattiroli F et al. “DNA-mediated association of two histone-bound complexes of yeast CAF-1 drives tetrasome assembly in the wake of DNA replication.” *eLife* 6:e22799. **18 March 2017.** [https://doi.org/10.7554/eLife.22799](https://doi.org/10.7554/eLife.22799). (mattiroli2017dnamediatedassociationof pages 1-2, mattiroli2017dnamediatedassociationof pages 4-6)
- Ouasti F et al. “Disordered regions and folded modules in CAF-1 promote histone deposition in *Schizosaccharomyces pombe*.” *eLife*. **20 February 2024.** [https://doi.org/10.7554/eLife.91461](https://doi.org/10.7554/eLife.91461). This is cross-species supporting evidence, not direct Q12495 experimentation. (ouasti2024disorderedregionsand pages 7-9, ouasti2024disorderedregionsand pages 1-2)
- Futami H et al. “The histone chaperone CAF-1 prevents Rad52-mediated instability of the budding yeast ribosomal DNA during replication-coupled DNA double-strand break repair.” Preprint initially posted in 2024 and updated **February 2025**. [https://doi.org/10.1101/2024.03.12.584701](https://doi.org/10.1101/2024.03.12.584701). (futami2025thehistonechaperone pages 28-31)

References

1. (kaufman1997ultravioletradiationsensitivity pages 1-2): P. Kaufman, R. Kobayashi, and B. Stillman. Ultraviolet radiation sensitivity and reduction of telomeric silencing in saccharomyces cerevisiae cells lacking chromatin assembly factor-i. Genes & development, 11 3:345-57, Feb 1997. URL: https://doi.org/10.1101/gad.11.3.345, doi:10.1101/gad.11.3.345. This article has 473 citations and is from a highest quality peer-reviewed journal.

2. (enomoto1998chromatinassemblyfactor pages 1-2): Shinichiro Enomoto and Judith Berman. Chromatin assembly factor i contributes to the maintenance, but not the re-establishment, of silencing at the yeast silent mating loci. Genes & development, 12 2:219-32, Jan 1998. URL: https://doi.org/10.1101/gad.12.2.219, doi:10.1101/gad.12.2.219. This article has 258 citations and is from a highest quality peer-reviewed journal.

3. (enomoto1997rlf2asubunit pages 1-2): S. Enomoto, P. McCune-Zierath, M. Gerami‐Nejad, M. Sanders, and J. Berman. Rlf2, a subunit of yeast chromatin assembly factor-i, is required for telomeric chromatin function in vivo. Genes & development, 11 3:358-70, Feb 1997. URL: https://doi.org/10.1101/gad.11.3.358, doi:10.1101/gad.11.3.358. This article has 197 citations and is from a highest quality peer-reviewed journal.

4. (zhang2016adnabinding pages 1-2): Kuo Zhang, Yuan Gao, Jingjing Li, Rebecca Burgess, Junhong Han, Huanhuan Liang, Zhiguo Zhang, and Yingfang Liu. A dna binding winged helix domain in caf-1 functions with pcna to stabilize caf-1 at replication forks. Nucleic Acids Research, 44:5083-5094, Feb 2016. URL: https://doi.org/10.1093/nar/gkw106, doi:10.1093/nar/gkw106. This article has 71 citations and is from a highest quality peer-reviewed journal.

5. (mattiroli2017dnamediatedassociationof pages 1-2): Francesca Mattiroli, Yajie Gu, Tejas Yadav, Jeremy L Balsbaugh, Michael R Harris, Eileen S Findlay, Yang Liu, Catherine A Radebaugh, Laurie A Stargell, Natalie G Ahn, Iestyn Whitehouse, and Karolin Luger. Dna-mediated association of two histone-bound complexes of yeast chromatin assembly factor-1 (caf-1) drives tetrasome assembly in the wake of dna replication. eLife, Mar 2017. URL: https://doi.org/10.7554/elife.22799, doi:10.7554/elife.22799. This article has 111 citations and is from a domain leading peer-reviewed journal.

6. (mattiroli2017dnamediatedassociationof pages 4-6): Francesca Mattiroli, Yajie Gu, Tejas Yadav, Jeremy L Balsbaugh, Michael R Harris, Eileen S Findlay, Yang Liu, Catherine A Radebaugh, Laurie A Stargell, Natalie G Ahn, Iestyn Whitehouse, and Karolin Luger. Dna-mediated association of two histone-bound complexes of yeast chromatin assembly factor-1 (caf-1) drives tetrasome assembly in the wake of dna replication. eLife, Mar 2017. URL: https://doi.org/10.7554/elife.22799, doi:10.7554/elife.22799. This article has 111 citations and is from a domain leading peer-reviewed journal.

7. (kaufman1997ultravioletradiationsensitivity pages 5-6): P. Kaufman, R. Kobayashi, and B. Stillman. Ultraviolet radiation sensitivity and reduction of telomeric silencing in saccharomyces cerevisiae cells lacking chromatin assembly factor-i. Genes & development, 11 3:345-57, Feb 1997. URL: https://doi.org/10.1101/gad.11.3.345, doi:10.1101/gad.11.3.345. This article has 473 citations and is from a highest quality peer-reviewed journal.

8. (mattiroli2017dnamediatedassociationof pages 10-12): Francesca Mattiroli, Yajie Gu, Tejas Yadav, Jeremy L Balsbaugh, Michael R Harris, Eileen S Findlay, Yang Liu, Catherine A Radebaugh, Laurie A Stargell, Natalie G Ahn, Iestyn Whitehouse, and Karolin Luger. Dna-mediated association of two histone-bound complexes of yeast chromatin assembly factor-1 (caf-1) drives tetrasome assembly in the wake of dna replication. eLife, Mar 2017. URL: https://doi.org/10.7554/elife.22799, doi:10.7554/elife.22799. This article has 111 citations and is from a domain leading peer-reviewed journal.

9. (mattiroli2017dnamediatedassociationof pages 2-4): Francesca Mattiroli, Yajie Gu, Tejas Yadav, Jeremy L Balsbaugh, Michael R Harris, Eileen S Findlay, Yang Liu, Catherine A Radebaugh, Laurie A Stargell, Natalie G Ahn, Iestyn Whitehouse, and Karolin Luger. Dna-mediated association of two histone-bound complexes of yeast chromatin assembly factor-1 (caf-1) drives tetrasome assembly in the wake of dna replication. eLife, Mar 2017. URL: https://doi.org/10.7554/elife.22799, doi:10.7554/elife.22799. This article has 111 citations and is from a domain leading peer-reviewed journal.

10. (zhang2016adnabinding pages 2-3): Kuo Zhang, Yuan Gao, Jingjing Li, Rebecca Burgess, Junhong Han, Huanhuan Liang, Zhiguo Zhang, and Yingfang Liu. A dna binding winged helix domain in caf-1 functions with pcna to stabilize caf-1 at replication forks. Nucleic Acids Research, 44:5083-5094, Feb 2016. URL: https://doi.org/10.1093/nar/gkw106, doi:10.1093/nar/gkw106. This article has 71 citations and is from a highest quality peer-reviewed journal.

11. (mattiroli2017dnamediatedassociationof pages 6-8): Francesca Mattiroli, Yajie Gu, Tejas Yadav, Jeremy L Balsbaugh, Michael R Harris, Eileen S Findlay, Yang Liu, Catherine A Radebaugh, Laurie A Stargell, Natalie G Ahn, Iestyn Whitehouse, and Karolin Luger. Dna-mediated association of two histone-bound complexes of yeast chromatin assembly factor-1 (caf-1) drives tetrasome assembly in the wake of dna replication. eLife, Mar 2017. URL: https://doi.org/10.7554/elife.22799, doi:10.7554/elife.22799. This article has 111 citations and is from a domain leading peer-reviewed journal.

12. (enomoto1998chromatinassemblyfactor pages 11-12): Shinichiro Enomoto and Judith Berman. Chromatin assembly factor i contributes to the maintenance, but not the re-establishment, of silencing at the yeast silent mating loci. Genes & development, 12 2:219-32, Jan 1998. URL: https://doi.org/10.1101/gad.12.2.219, doi:10.1101/gad.12.2.219. This article has 258 citations and is from a highest quality peer-reviewed journal.

13. (kaufman1997ultravioletradiationsensitivity pages 6-7): P. Kaufman, R. Kobayashi, and B. Stillman. Ultraviolet radiation sensitivity and reduction of telomeric silencing in saccharomyces cerevisiae cells lacking chromatin assembly factor-i. Genes & development, 11 3:345-57, Feb 1997. URL: https://doi.org/10.1101/gad.11.3.345, doi:10.1101/gad.11.3.345. This article has 473 citations and is from a highest quality peer-reviewed journal.

14. (futami2025thehistonechaperone pages 28-31): Hajime Futami, Tsugumi Yamaji, Yuko Katayama, Nanase Arata, Takehiko Kobayashi, and Mariko Sasaki. The histone chaperone caf-1 prevents rad52-mediated instability of the budding yeast ribosomal dna during replication-coupled dna double-strand break repair. bioRxiv, Feb 2025. URL: https://doi.org/10.1101/2024.03.12.584701, doi:10.1101/2024.03.12.584701. This article has 0 citations.

15. (ouasti2024disorderedregionsand pages 7-9): Fouad Ouasti, Maxime Audin, Karine Fréon, Jean-Pierre Quivy, Mehdi Tachekort, Elizabeth Cesard, Aurélien Thureau, Virginie Ropars, Paloma Fernández Varela, Gwenaelle Moal, Ibrahim Soumana Adamou, Aleksandra Uryga, Pierre Legrand, Jessica Andreani, Raphaël Guerois, Geneviève Almouzni, Sarah Lambert, and Francoise Ochsenbein. Disordered regions and folded modules in caf-1 promote histone deposition in schizosaccharomyces pombe. eLife, Feb 2024. URL: https://doi.org/10.7554/elife.91461, doi:10.7554/elife.91461. This article has 6 citations and is from a domain leading peer-reviewed journal.

16. (ouasti2024disorderedregionsand pages 2-4): Fouad Ouasti, Maxime Audin, Karine Fréon, Jean-Pierre Quivy, Mehdi Tachekort, Elizabeth Cesard, Aurélien Thureau, Virginie Ropars, Paloma Fernández Varela, Gwenaelle Moal, Ibrahim Soumana Adamou, Aleksandra Uryga, Pierre Legrand, Jessica Andreani, Raphaël Guerois, Geneviève Almouzni, Sarah Lambert, and Francoise Ochsenbein. Disordered regions and folded modules in caf-1 promote histone deposition in schizosaccharomyces pombe. eLife, Feb 2024. URL: https://doi.org/10.7554/elife.91461, doi:10.7554/elife.91461. This article has 6 citations and is from a domain leading peer-reviewed journal.

17. (ouasti2024disorderedregionsand pages 4-5): Fouad Ouasti, Maxime Audin, Karine Fréon, Jean-Pierre Quivy, Mehdi Tachekort, Elizabeth Cesard, Aurélien Thureau, Virginie Ropars, Paloma Fernández Varela, Gwenaelle Moal, Ibrahim Soumana Adamou, Aleksandra Uryga, Pierre Legrand, Jessica Andreani, Raphaël Guerois, Geneviève Almouzni, Sarah Lambert, and Francoise Ochsenbein. Disordered regions and folded modules in caf-1 promote histone deposition in schizosaccharomyces pombe. eLife, Feb 2024. URL: https://doi.org/10.7554/elife.91461, doi:10.7554/elife.91461. This article has 6 citations and is from a domain leading peer-reviewed journal.

18. (ouasti2024disorderedregionsand pages 1-2): Fouad Ouasti, Maxime Audin, Karine Fréon, Jean-Pierre Quivy, Mehdi Tachekort, Elizabeth Cesard, Aurélien Thureau, Virginie Ropars, Paloma Fernández Varela, Gwenaelle Moal, Ibrahim Soumana Adamou, Aleksandra Uryga, Pierre Legrand, Jessica Andreani, Raphaël Guerois, Geneviève Almouzni, Sarah Lambert, and Francoise Ochsenbein. Disordered regions and folded modules in caf-1 promote histone deposition in schizosaccharomyces pombe. eLife, Feb 2024. URL: https://doi.org/10.7554/elife.91461, doi:10.7554/elife.91461. This article has 6 citations and is from a domain leading peer-reviewed journal.

19. (mattiroli2017dnamediatedassociationof pages 16-17): Francesca Mattiroli, Yajie Gu, Tejas Yadav, Jeremy L Balsbaugh, Michael R Harris, Eileen S Findlay, Yang Liu, Catherine A Radebaugh, Laurie A Stargell, Natalie G Ahn, Iestyn Whitehouse, and Karolin Luger. Dna-mediated association of two histone-bound complexes of yeast chromatin assembly factor-1 (caf-1) drives tetrasome assembly in the wake of dna replication. eLife, Mar 2017. URL: https://doi.org/10.7554/elife.22799, doi:10.7554/elife.22799. This article has 111 citations and is from a domain leading peer-reviewed journal.

20. (futami2025thehistonechaperone pages 49-50): Hajime Futami, Tsugumi Yamaji, Yuko Katayama, Nanase Arata, Takehiko Kobayashi, and Mariko Sasaki. The histone chaperone caf-1 prevents rad52-mediated instability of the budding yeast ribosomal dna during replication-coupled dna double-strand break repair. bioRxiv, Feb 2025. URL: https://doi.org/10.1101/2024.03.12.584701, doi:10.1101/2024.03.12.584701. This article has 0 citations.

## Artifacts

- [Edison artifact artifact-00](RLF2-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. mattiroli2017dnamediatedassociationof pages 4-6
2. zhang2016adnabinding pages 1-2
3. futami2025thehistonechaperone pages 28-31
4. mattiroli2017dnamediatedassociationof pages 6-8
5. mattiroli2017dnamediatedassociationof pages 10-12
6. zhang2016adnabinding pages 2-3
7. kaufman1997ultravioletradiationsensitivity pages 1-2
8. enomoto1998chromatinassemblyfactor pages 1-2
9. mattiroli2017dnamediatedassociationof pages 1-2
10. kaufman1997ultravioletradiationsensitivity pages 5-6
11. mattiroli2017dnamediatedassociationof pages 2-4
12. enomoto1998chromatinassemblyfactor pages 11-12
13. kaufman1997ultravioletradiationsensitivity pages 6-7
14. ouasti2024disorderedregionsand pages 7-9
15. ouasti2024disorderedregionsand pages 2-4
16. ouasti2024disorderedregionsand pages 4-5
17. ouasti2024disorderedregionsand pages 1-2
18. mattiroli2017dnamediatedassociationof pages 16-17
19. futami2025thehistonechaperone pages 49-50
20. DOI URL
21. https://doi.org/10.1101/gad.11.3.345
22. https://doi.org/10.1101/gad.11.3.358
23. https://doi.org/10.1101/gad.12.2.219
24. https://doi.org/10.1093/nar/gkw106
25. https://doi.org/10.7554/eLife.22799
26. https://doi.org/10.7554/eLife.91461
27. https://doi.org/10.1101/2024.03.12.584701
28. https://doi.org/10.1101/gad.11.3.345](https://doi.org/10.1101/gad.11.3.345
29. https://doi.org/10.1101/gad.11.3.358](https://doi.org/10.1101/gad.11.3.358
30. https://doi.org/10.1101/gad.12.2.219](https://doi.org/10.1101/gad.12.2.219
31. https://doi.org/10.1093/nar/gkw106](https://doi.org/10.1093/nar/gkw106
32. https://doi.org/10.7554/eLife.22799](https://doi.org/10.7554/eLife.22799
33. https://doi.org/10.7554/eLife.91461](https://doi.org/10.7554/eLife.91461
34. https://doi.org/10.1101/2024.03.12.584701](https://doi.org/10.1101/2024.03.12.584701
35. https://doi.org/10.1101/gad.11.3.345,
36. https://doi.org/10.1101/gad.12.2.219,
37. https://doi.org/10.1101/gad.11.3.358,
38. https://doi.org/10.1093/nar/gkw106,
39. https://doi.org/10.7554/elife.22799,
40. https://doi.org/10.1101/2024.03.12.584701,
41. https://doi.org/10.7554/elife.91461,