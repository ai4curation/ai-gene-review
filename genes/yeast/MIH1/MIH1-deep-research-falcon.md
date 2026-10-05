---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-25T01:59:49.857768'
end_time: '2026-09-25T02:09:40.653509'
duration_seconds: 590.8
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: yeast
  gene_id: MIH1
  gene_symbol: MIH1
  uniprot_accession: P23748
  protein_description: 'RecName: Full=M-phase inducer phosphatase; EC=3.1.3.48 {ECO:0000250|UniProtKB:P30303};
    AltName: Full=Mitosis initiation protein MIH1; AltName: Full=Mitotic inducer homolog;'
  gene_info: Name=MIH1; OrderedLocusNames=YMR036C {ECO:0000312|SGD:S000004639}; ORFNames=YM9532.01C,
    YM9973.10C;
  organism_full: Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
  protein_family: Belongs to the MPI phosphatase family. .
  protein_domains: MPI_Phosphatase. (IPR000751); Rhodanese-like_dom. (IPR001763);
    Rhodanese-like_dom_sf. (IPR036873); Rhodanese (PF00581)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 31
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: MIH1-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** P23748
- **Protein Description:** RecName: Full=M-phase inducer phosphatase; EC=3.1.3.48 {ECO:0000250|UniProtKB:P30303}; AltName: Full=Mitosis initiation protein MIH1; AltName: Full=Mitotic inducer homolog;
- **Gene Information:** Name=MIH1; OrderedLocusNames=YMR036C {ECO:0000312|SGD:S000004639}; ORFNames=YM9532.01C, YM9973.10C;
- **Organism (full):** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
- **Protein Family:** Belongs to the MPI phosphatase family. .
- **Key Domains:** MPI_Phosphatase. (IPR000751); Rhodanese-like_dom. (IPR001763); Rhodanese-like_dom_sf. (IPR036873); Rhodanese (PF00581)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "MIH1" matches the protein description above**
2. **Verify the organism is correct:** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'MIH1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **MIH1** (gene ID: MIH1, UniProt: P23748) in yeast.

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
- **UniProt Accession:** P23748
- **Protein Description:** RecName: Full=M-phase inducer phosphatase; EC=3.1.3.48 {ECO:0000250|UniProtKB:P30303}; AltName: Full=Mitosis initiation protein MIH1; AltName: Full=Mitotic inducer homolog;
- **Gene Information:** Name=MIH1; OrderedLocusNames=YMR036C {ECO:0000312|SGD:S000004639}; ORFNames=YM9532.01C, YM9973.10C;
- **Organism (full):** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
- **Protein Family:** Belongs to the MPI phosphatase family. .
- **Key Domains:** MPI_Phosphatase. (IPR000751); Rhodanese-like_dom. (IPR001763); Rhodanese-like_dom_sf. (IPR036873); Rhodanese (PF00581)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "MIH1" matches the protein description above**
2. **Verify the organism is correct:** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'MIH1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **MIH1** (gene ID: MIH1, UniProt: P23748) in yeast.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# MIH1 (P23748/YMR036C) functional-annotation report

## Executive conclusion

**Identity is verified.** The requested protein is Mih1 from *Saccharomyces cerevisiae* S288c, encoded by **MIH1/YMR036C**, not a similarly named protein from another organism. The literature consistently identifies it as the sole budding-yeast homolog of **Cdc25**, the M-phase-inducing phosphatase. This agrees with the supplied UniProt accession P23748, MPI/Cdc25 phosphatase-family assignment, and rhodanese-like phosphatase domain. No conflicting MIH1 identity was used in this report. (kennedy2016redundantregulationof pages 1-2, keaton2008nucleocytoplasmictraffickingof pages 1-2)

The primary molecular function of Mih1 is to **activate Cdc28/Cdk1–mitotic cyclin complexes by removing the inhibitory phosphate from Cdc28 Tyr19**. The best-supported reaction is:

**Cdc28-pTyr19 + H₂O → Cdc28-Tyr19 + inorganic phosphate.**

This assignment is supported not merely by homology or genetics: purified Mih1 directly dephosphorylated Swe1-phosphorylated Cdc28/Cdk1–Clb2 complexes in vitro. Mih1 therefore constitutes the phosphatase arm of a reversible switch in which Swe1 phosphorylates and inhibits Cdc28 at Tyr19, whereas Mih1 removes that phosphate to promote mitotic activity. (sia1996cdc28tyrosinephosphorylation pages 1-2, kennedy2016redundantregulationof pages 1-2, kennedy2016redundantregulationof pages 4-6)

| Annotation dimension | Best-supported conclusion | Evidence type / key quantitative result | Confidence | Key source |
|---|---|---|---|---|
| Identity and family | **Verified target:** Mih1 is the *Saccharomyces cerevisiae* MIH1/YMR036C product and sole budding-yeast Cdc25 homolog—an M-phase-inducer, dual-specificity protein phosphatase. Its MPI/Cdc25-family classification agrees with the UniProt-supplied rhodanese-like phosphatase domain and catalytic HCX₅R motif; the fold assignment is inferred rather than based on a Mih1 structure. | Organism-specific literature identifies MIH1 as the budding-yeast CDC25 homolog; sequence/domain annotation supports a rhodanese-like PTPase catalytic fold. | **High** for identity/family; **moderate** for inferred structure | Kennedy et al., 2016, [DOI](https://doi.org/10.1534/genetics.115.182469) (kennedy2016redundantregulationof pages 1-2, david2021exploringtheregulation pages 45-59) |
| Catalytic reaction and substrate specificity | **Direct evidence:** Mih1 hydrolyzes the inhibitory phosphate from Cdc28/Cdk1 phospho-Tyr19: Cdc28-pY19 + H₂O → Cdc28-Y19 + inorganic phosphate, activating mitotic Cdk1–cyclin complexes. Cdc28/Clb2 is the best-established physiological substrate; a broad Mih1 substrate repertoire has not been demonstrated. | Purified Mih1 directly dephosphorylated Swe1-phosphorylated Cdk1/Clb2 in vitro. It did not dephosphorylate a fortuitous background phosphoprotein in the same assay, supporting substrate selectivity. | **Very high** | Kennedy et al., 2016, [DOI](https://doi.org/10.1534/genetics.115.182469) (kennedy2016redundantregulationof pages 4-6) |
| Mitotic role and redundancy | Mih1 promotes mitotic entry and anaphase progression by opposing Swe1-mediated Cdc28-Y19 phosphorylation, but it is **nonessential** because Ptp1 and a PP2A-Rts1-dependent activity provide redundancy. | **Direct genetics/biochemistry:** *mih1Δ* cells are viable, display elevated mitotic Cdc28-pY19, and have mild mitotic-entry and anaphase delays. Mitotic Cdk1 activity in *mih1Δ* and *mih1Δ ptp1Δ* was about **65% of wild type**, versus **50%** during LatA- or GAL-SWE1-induced arrest. *mih1Δ ptp1Δ rts1Δ* blocked detectable Cdk1-Y19 dephosphorylation and was lethal unless *SWE1* was deleted. | **Very high** | Kennedy et al., 2016, [DOI](https://doi.org/10.1534/genetics.115.182469) (kennedy2016redundantregulationof pages 1-2, kennedy2016redundantregulationof pages 2-4, kennedy2016redundantregulationof pages 4-6) |
| Morphogenesis checkpoint | Mih1 is the phosphatase arm of the budding-yeast morphogenesis checkpoint. When budding or polarization fails, reduced Mih1 output together with Swe1 activity sustains inhibitory Cdc28-pY19 and delays nuclear division; removing MIH1 strengthens or prolongs this delay. | **Direct genetics:** in *cdc24* cells unable to polarize, deleting *SWE1* abolished the mitotic delay, whereas homozygous *MIH1* deletion made it effectively permanent; even a twofold gene-dosage change altered timing. Later work found **40% binucleate** *cdc24-1 alk1Δ* cells by 2 h, while additional *MIH1* deletion restored normal anaphase kinetics, implicating premature Mih1 activation. | **High** | Sia et al., 1996, [DOI](https://doi.org/10.1091/mbc.7.11.1657); Galli et al., 2021, [DOI](https://doi.org/10.3389/fcell.2020.625717) (sia1996cdc28tyrosinephosphorylation pages 1-2, sia1996cdc28tyrosinephosphorylation pages 4-5, galli2021haspinmodulatesthe pages 4-6, galli2021haspinmodulatesthe pages 6-7) |
| Cellular localization | Mih1 acts in both cytoplasm and nucleus and undergoes cell-cycle-regulated nucleocytoplasmic shuttling. It is predominantly cytoplasmic through most of the cycle but transiently accumulates in nuclei during late mitosis/telophase. | **Direct immunofluorescence:** approximately **75% of post-anaphase cells** showed nuclear Mih1, whereas nuclear signal was rare in G1. Substitution of Lys31–Lys33 with alanines prevented telophase nuclear accumulation; the cytoplasm-restricted protein remained functional but was less effective, producing larger, elongated cells and delayed nuclear division. | **High** | Keaton et al., 2008, [DOI](https://doi.org/10.1091/mbc.e08-03-0286) (keaton2008nucleocytoplasmictraffickingof pages 9-11, keaton2008nucleocytoplasmictraffickingof pages 1-2) |
| Regulation | Mih1 abundance is comparatively constitutive, while activity is regulated chiefly through phosphorylation, localization, and checkpoint context. PP2A-Cdc55/Zds promotes Mih1 dephosphorylation at mitotic entry; casein kinases Yck1/Yck2 and Mck1 contribute to Mih1 phosphorylation. The physiological effects of individual Mih1 phosphosites remain unresolved. | **Mixed direct and pathway-level evidence:** *cdc55Δ* causes persistent Mih1 hyperphosphorylation, consistent with Mih1 being a PP2A-Cdc55 substrate; Mih1-myc abundance remained constitutive across the cell cycle. Yck1/Yck2 and Mck1 involvement is supported by phosphorylation-state studies but not a complete site-resolved mechanism. | **Moderate–high** | Pal et al., 2008, [DOI](https://doi.org/10.1083/jcb.200711014); Keaton et al., 2008, [DOI](https://doi.org/10.1091/mbc.e08-03-0286); Yasutis and Kozminski, 2013, [DOI](https://doi.org/10.4161/cc.24637) (david2021exploringtheregulation pages 75-77, mcqueen2013explorationofthe pages 24-28, keaton2008nucleocytoplasmictraffickingof pages 9-11, yasutis2013cellcyclecheckpoint pages 4-5, yasutis2013cellcyclecheckpoint pages 5-6) |
| 2023–2024 evidence status | No substantive 2023–2024 MIH1-specific mechanistic primary study was found in the targeted search. Current annotation therefore rests on foundational studies, the 2016 direct biochemical analysis, and a 2021 checkpoint extension; a 2023 yeast phosphoproteome resource does not by itself revise Mih1’s established mechanism. | Targeted literature-search result; this is an evidence-gap statement, not proof that no publication exists. | **Moderate** | Leutert et al., 2023, [DOI](https://doi.org/10.6084/m9.figshare.23546118.v1); latest target-specific mechanistic evidence assessed here: Galli et al., 2021, [DOI](https://doi.org/10.3389/fcell.2020.625717) (galli2021haspinmodulatesthe pages 4-6, galli2021haspinmodulatesthe pages 6-7) |


*Table: Compact evidence assessment for *S. cerevisiae* MIH1/P23748, distinguishing direct experiments from structural or pathway inference. It summarizes identity, catalytic specificity, pathway function, localization, regulation, quantitative findings, and the 2023–2024 evidence gap.*

## 1. Identity, nomenclature, family, and domains

The organism-specific identification is:

- **Gene:** *MIH1*
- **Ordered locus:** **YMR036C**
- **Protein:** Mih1/M-phase inducer phosphatase/mitotic inducer homolog
- **Organism:** *Saccharomyces cerevisiae*, including the S288c reference background specified by UniProt
- **UniProt:** **P23748**
- **Functional orthology:** Cdc25-family phosphatase

Primary yeast literature describes Mih1 as the budding-yeast—and in this context sole—Cdc25 homolog. The target is therefore distinct from Cdc25 proteins in fission yeast, animals, or other fungi, although those proteins provide evolutionary context. (keaton2008nucleocytoplasmictraffickingof pages 1-2, kennedy2016redundantregulationof pages 1-2)

The supplied InterPro/Pfam assignments—MPI phosphatase, rhodanese-like domain, and Rhodanese/PF00581—are coherent with the Cdc25 phosphatase family. A secondary source describes Mih1 as containing a rhodanese-like protein-tyrosine-phosphatase domain with the characteristic **HCX₅R** catalytic-loop motif. This domain conclusion is sequence/family inference; the evidence retrieved here did not include an experimentally solved Mih1 structure. A crystallographic study of another yeast rhodanese-like protein, Ygr203w, must not be treated as a Mih1 structure. (david2021exploringtheregulation pages 45-59, david2021exploringtheregulation pages 75-77)

## 2. Catalytic function and substrate specificity

### Directly demonstrated reaction

The strongest biochemical experiment was reported by Kennedy et al. in *Genetics* (published online December 29, 2015; print March 2016; DOI: https://doi.org/10.1534/genetics.115.182469). Cdc28/Cdk1–Clb2 complexes were first phosphorylated by Swe1 and then incubated with purified phosphatases. Purified Mih1 removed Cdc28 Tyr19 phosphorylation directly. A fortuitous background phosphoprotein in the same preparation was not dephosphorylated by Mih1, providing evidence that the result was not indiscriminate bulk phosphatase activity. (kennedy2016redundantregulationof pages 1-2, kennedy2016redundantregulationof pages 4-6)

Accordingly, the best-established physiological substrate is **Cdc28/Cdk1 phosphorylated at Tyr19**, particularly mitotic cyclin complexes such as Cdc28–Clb2. The current evidence does **not** establish a large, broad Mih1 substrate repertoire. Annotation should therefore remain specific rather than labeling Mih1 as a general cellular tyrosine phosphatase. Its classification as a “dual-specificity phosphatase” reflects Cdc25-family catalytic chemistry and potential residue-class capability; the decisive *S. cerevisiae* physiological reaction documented here is Tyr19 dephosphorylation. (kennedy2016redundantregulationof pages 1-2, kennedy2016redundantregulationof pages 4-6)

### Functional consequence

Tyr19 phosphorylation inhibits Cdc28–Clb activity. Removing this phosphate increases mitotic Cdk1 activity and thereby facilitates mitotic entry and progression. In synchronized cells, *mih1Δ* and *mih1Δ ptp1Δ* Cdk1 complexes retained approximately **65% of wild-type mitotic kinase activity**, whereas latrunculin-A treatment or GAL-driven Swe1 overexpression reduced activity to approximately **50%**. Conversely, Cdk1 isolated from mitotic *swe1Δ* cells had about **threefold greater activity** than synchronized mitotic wild type, illustrating how strongly the Swe1–Mih1 axis can tune the active Cdk1 pool. (kennedy2016redundantregulationof pages 2-4)

## 3. Biological pathway and physiological role

### Core G2/M control

Mih1 and Swe1 form an antagonistic control module:

1. **Swe1/Wee1** phosphorylates Cdc28 Tyr19 and suppresses mitotic Cdk1 activity.
2. **Mih1/Cdc25** removes Tyr19 phosphate and promotes Cdk1 activation.
3. Active Cdc28–Clb complexes drive nuclear division and other mitotic events.

Unlike fission-yeast Cdc25, Mih1 is not essential under standard budding-yeast growth conditions. *mih1Δ* cells are viable and display elevated mitotic Cdc28-pTyr19, but only mild delays in mitotic entry and anaphase onset; they eventually dephosphorylate Cdc28 as they enter G1. This led to the discovery of redundant control by Ptp1 and a PP2A-Rts1-dependent activity. (kennedy2016redundantregulationof pages 1-2)

Direct biochemical evidence shows that Ptp1, like Mih1, can dephosphorylate Cdc28-pTyr19. Genetic/in-vivo assays further indicate that PP2A-Rts1 either acts on Cdc28-pTyr19 or controls another unidentified phosphatase. In *mih1Δ ptp1Δ rts1Δ* cells, detectable Cdc28-Y19 dephosphorylation was blocked; this triple-mutant state was lethal, and lethality was rescued by deleting *SWE1*. Thus, Mih1 is the canonical Cdc25-like enzyme but participates in a robust, partially redundant network rather than acting alone. (kennedy2016redundantregulationof pages 2-4, kennedy2016redundantregulationof pages 4-6)

### Morphogenesis checkpoint

Mih1 has a particularly important role when budding or cell polarization is defective. The morphogenesis checkpoint delays nuclear division until bud formation and polarity are adequate. Foundational experiments using temperature-sensitive *cdc24* cells showed that the timing of nuclear division was highly sensitive to both *SWE1* and *MIH1* dosage. Deleting *SWE1* abolished the checkpoint delay, whereas loss of *MIH1* greatly strengthened it; in diploids, even a twofold gene-dosage difference produced intermediate timing. These findings established the Cdc28-Tyr19 switch as the checkpoint’s central output. (sia1996cdc28tyrosinephosphorylation pages 1-2, sia1996cdc28tyrosinephosphorylation pages 4-5)

This delay is physiologically consequential rather than a dispensable laboratory phenotype. In polarization-defective cells at 37°C, wild-type checkpoint cells began losing viability at approximately 6 h, whereas *swe1* and *mih1* mutants began doing so at about 4 h and 5 h, respectively. Both premature and excessively delayed mitosis were therefore detrimental. (sia1996cdc28tyrosinephosphorylation pages 4-5)

A 2021 extension implicated the yeast haspin paralogs Alk1 and Alk2 in maintaining this checkpoint. Loss of Alk1 allowed premature nuclear division after polarity disruption: approximately **40%** of *cdc24-1 alk1Δ* cells were binucleate 2 h after release. Additional deletion of *MIH1* restored normal anaphase kinetics, supporting the interpretation that checkpoint failure involved inappropriate Mih1 activity. Loss of Alk1 permitted initial Cdc28-Y19 phosphorylation but prevented its sustained accumulation after roughly 1 h. No Alk1–Mih1 physical interaction was detected by two-hybrid analysis, and obvious Mih1 abundance or mobility changes were not observed, so this regulatory connection is likely indirect. Galli et al., January 2021, DOI: https://doi.org/10.3389/fcell.2020.625717. (galli2021haspinmodulatesthe pages 4-6, galli2021haspinmodulatesthe pages 6-7)

## 4. Cellular localization: where Mih1 acts

Mih1 is a **nucleocytoplasmic protein**, not a membrane, secreted, or organelle-resident enzyme. Immunofluorescence of a functional Mih1–12Myc fusion showed signal throughout the cell, with predominantly cytoplasmic localization during most of the vegetative cell cycle. Approximately **75% of post-anaphase cells** displayed nuclear Mih1, whereas nuclear Mih1 was rare in G1, indicating transient nuclear accumulation around telophase/mitotic exit. Mih1 protein abundance itself remained relatively constant through the cell cycle. Keaton et al., September 2008, DOI: https://doi.org/10.1091/mbc.e08-03-0286. (keaton2008nucleocytoplasmictraffickingof pages 9-11, keaton2008nucleocytoplasmictraffickingof pages 1-2)

A basic sequence near the N terminus functions as a nuclear-import determinant. Changing **Lys31–Lys33 to alanines** prevented telophase nuclear accumulation. This cytoplasm-restricted variant remained capable of promoting nuclear division, but it was less effective than wild-type Mih1 in sensitized *hsl1* cells, producing larger, more elongated cells and delaying nuclear division. Appending an exogenous SV40 nuclear-localization signal rescued these defects. These experiments show that Mih1 can act from either compartment because Cdc28–Clb2 itself shuttles, but the nuclear Mih1 pool is functionally more efficient. (keaton2008nucleocytoplasmictraffickingof pages 9-11, keaton2008nucleocytoplasmictraffickingof pages 1-2)

The appropriate localization annotation is therefore **cytoplasm and nucleus, with cell-cycle-regulated shuttling and transient late-mitotic nuclear enrichment**. Mih1 likely encounters mobile Cdc28–cyclin complexes in both compartments rather than acting at one fixed structure. (keaton2008nucleocytoplasmictraffickingof pages 9-11)

## 5. Regulation of Mih1

### Phosphoregulation

Mih1 is extensively regulated at the post-translational level. PP2A containing the Cdc55 regulatory subunit promotes Mih1 dephosphorylation as cells approach mitosis: loss of Cdc55 causes persistent Mih1 hyperphosphorylation. Zds1/Zds2 proteins are required for PP2A-Cdc55-dependent Mih1 dephosphorylation. However, an important unresolved point is whether Mih1 hyperphosphorylation changes its intrinsic catalytic rate, substrate access, or localization; authoritative reviews explicitly note that these alternatives were not resolved. Pal, Paraz and Kellogg, March 2008, DOI: https://doi.org/10.1083/jcb.200711014. (david2021exploringtheregulation pages 75-77, yasutis2013cellcyclecheckpoint pages 4-5, yasutis2013cellcyclecheckpoint pages 5-6)

Casein kinases Yck1/Yck2 and the kinase Mck1 have also been implicated in generating the Mih1 phosphorylation pattern under unstressed conditions. The evidence retrieved supports their contribution to Mih1 mobility/phosphorylation state, but it does not provide a complete site-resolved regulatory mechanism. Claims that a particular Mih1 phosphosite directly activates or inhibits catalysis should therefore be treated cautiously. (mcqueen2013explorationofthe pages 24-28)

### Upstream signaling context

The broader regulatory architecture links growth and membrane trafficking to mitotic entry. Exocytosis and Rho1/Pkc1/Zds signaling feed into PP2A-Cdc55 and Mih1, coupling successful polarized growth and cell-wall-related processes to Cdc28 activation. Yet PP2A-Cdc55 has complex effects on both Mih1 and Swe1, and some genetic results have supported apparently opposing roles. Expert reviews consequently describe this branch as spatially and mechanistically more complicated than a simple linear activation pathway. (yasutis2013cellcyclecheckpoint pages 4-5, yasutis2013cellcyclecheckpoint pages 5-6)

### Expression versus activity

Available microscopy and immunoblotting indicate that Mih1 abundance is comparatively constitutive. Regulation is therefore dominated by phosphorylation state, access to Cdc28 complexes, subcellular trafficking, and the balance with Swe1 and redundant phosphatases rather than large periodic changes in protein concentration. (keaton2008nucleocytoplasmictraffickingof pages 9-11)

## 6. Recent developments and present state of the field

A targeted search of 2023–2024 literature did **not** identify a substantive new Mih1-specific mechanistic primary study. A 2023 yeast phosphoproteome resource is relevant to the general phosphorylation landscape but did not, in the retrieved evidence, revise the established Mih1 mechanism. Consequently, the most reliable annotation still rests on the foundational morphogenesis-checkpoint study from 1996, localization and phosphoregulation work from 2008, direct biochemical/redundancy analysis from 2016, and the Alk1/Alk2 checkpoint extension from 2021. This is a literature-gap statement rather than proof that no relevant report exists.

The current consensus is therefore stable: Mih1 is the canonical Cdc25-like Cdc28-pTyr19 phosphatase, but its biological output is embedded in a redundant and spatially regulated network. The major conceptual advance after the early checkpoint model was recognition that Mih1 is **not the only route** to Cdc28-Y19 dephosphorylation. (kennedy2016redundantregulationof pages 1-2, kennedy2016redundantregulationof pages 4-6)

## 7. Current applications and real-world implementation

Mih1 is principally a **basic-research model**, not a clinical or industrially deployed target. Its practical applications are:

- dissecting the conserved Wee1–Cdc25–Cdk1 mitotic switch;
- studying how cell polarity, cytoskeletal stress, exocytosis, and cell-wall integrity are coupled to nuclear division;
- testing robustness and redundancy in cell-cycle networks;
- analyzing how nucleocytoplasmic trafficking affects enzyme–substrate encounters; and
- providing a genetically tractable model for phosphatase regulation relevant to the mammalian G2/M checkpoint.

The translational relevance is architectural rather than target-specific. Human Cdc25 phosphatases and Wee1 are oncology targets, but Mih1 itself is a yeast protein and there is no evidence in the retrieved literature for a Mih1-directed therapy or commercial bioprocess. Reviews emphasize that conserved pathway organization can be informative even where individual upstream components differ between yeast and vertebrates. (yasutis2013cellcyclecheckpoint pages 1-2, yasutis2013cellcyclecheckpoint pages 5-6)

## 8. Evidence-weighted functional annotation

A defensible concise annotation is:

> **Mih1 is the nucleocytoplasmic Cdc25-family M-phase-inducer phosphatase of budding yeast. It directly hydrolyzes the inhibitory Tyr19 phosphate on Cdc28/Cdk1–mitotic cyclin complexes, opposing Swe1 to promote mitotic Cdk activity. Mih1 contributes to normal mitotic timing and is a central effector of the morphogenesis checkpoint, particularly when bud formation or polarity is defective. Its activity is controlled by phosphorylation and nucleocytoplasmic trafficking, including PP2A-Cdc55/Zds-dependent dephosphorylation, while Ptp1 and a PP2A-Rts1-dependent mechanism provide functional redundancy.**

Confidence is **very high** for the Cdc28-pTyr19 reaction and Swe1-opposing pathway, **high** for nucleocytoplasmic localization and morphogenesis-checkpoint function, and **moderate** for the detailed causal effects of individual Mih1 phosphorylation states.

## 9. Important unresolved questions

1. **Full substrate repertoire:** Cdc28-pTyr19 is directly established, but other physiological Mih1 substrates remain poorly defined.
2. **Phosphosite mechanism:** Mih1 phosphorylation is well documented, but the contribution of individual sites to catalytic activity, localization, or substrate binding remains incomplete.
3. **PP2A-Rts1 branch:** genetic evidence supports a third Cdc28-Y19-dephosphorylation route, but direct PP2A-Rts1 activity against Cdc28 was not demonstrated in the reported purified assay. (kennedy2016redundantregulationof pages 4-6)
4. **Structure:** the family/fold assignment is strong, but no Mih1-specific experimental structure was identified in the retrieved evidence.
5. **Checkpoint integration:** Alk1/Alk2, Pkc1, Zds proteins, PP2A complexes, and trafficking clearly influence the network, but several connections remain indirect or context dependent. (galli2021haspinmodulatesthe pages 6-7, yasutis2013cellcyclecheckpoint pages 4-5, yasutis2013cellcyclecheckpoint pages 5-6)

References

1. (kennedy2016redundantregulationof pages 1-2): Erin K Kennedy, Michael Dysart, Noel Lianga, Elizabeth C Williams, Sophie Pilon, Carole Doré, Jean-Sebastien Deneault, and Adam D Rudner. Redundant regulation of cdk1 tyrosine dephosphorylation in saccharomyces cerevisiae. Genetics, 202:903-910, Dec 2016. URL: https://doi.org/10.1534/genetics.115.182469, doi:10.1534/genetics.115.182469. This article has 20 citations and is from a domain leading peer-reviewed journal.

2. (keaton2008nucleocytoplasmictraffickingof pages 1-2): Mignon A. Keaton, Lee Szkotnicki, Aron R. Marquitz, Jake Harrison, Trevin R. Zyla, and Daniel J. Lew. Nucleocytoplasmic trafficking of g2/m regulators in yeast. Molecular biology of the cell, 19 9:4006-18, Sep 2008. URL: https://doi.org/10.1091/mbc.e08-03-0286, doi:10.1091/mbc.e08-03-0286. This article has 43 citations and is from a domain leading peer-reviewed journal.

3. (sia1996cdc28tyrosinephosphorylation pages 1-2): R. A. Sia, Heather A. Herald, and D. Lew. Cdc28 tyrosine phosphorylation and the morphogenesis checkpoint in budding yeast. Molecular biology of the cell, 7 11:1657-66, Nov 1996. URL: https://doi.org/10.1091/mbc.7.11.1657, doi:10.1091/mbc.7.11.1657. This article has 236 citations and is from a domain leading peer-reviewed journal.

4. (kennedy2016redundantregulationof pages 4-6): Erin K Kennedy, Michael Dysart, Noel Lianga, Elizabeth C Williams, Sophie Pilon, Carole Doré, Jean-Sebastien Deneault, and Adam D Rudner. Redundant regulation of cdk1 tyrosine dephosphorylation in saccharomyces cerevisiae. Genetics, 202:903-910, Dec 2016. URL: https://doi.org/10.1534/genetics.115.182469, doi:10.1534/genetics.115.182469. This article has 20 citations and is from a domain leading peer-reviewed journal.

5. (david2021exploringtheregulation pages 45-59): Alain David. Exploring the regulation of mitotic pp2a-rts1 activity in saccharomyces cerevisiae. ArXiv, Jul 2021. URL: https://doi.org/10.20381/ruor-26657, doi:10.20381/ruor-26657. This article has 0 citations.

6. (kennedy2016redundantregulationof pages 2-4): Erin K Kennedy, Michael Dysart, Noel Lianga, Elizabeth C Williams, Sophie Pilon, Carole Doré, Jean-Sebastien Deneault, and Adam D Rudner. Redundant regulation of cdk1 tyrosine dephosphorylation in saccharomyces cerevisiae. Genetics, 202:903-910, Dec 2016. URL: https://doi.org/10.1534/genetics.115.182469, doi:10.1534/genetics.115.182469. This article has 20 citations and is from a domain leading peer-reviewed journal.

7. (sia1996cdc28tyrosinephosphorylation pages 4-5): R. A. Sia, Heather A. Herald, and D. Lew. Cdc28 tyrosine phosphorylation and the morphogenesis checkpoint in budding yeast. Molecular biology of the cell, 7 11:1657-66, Nov 1996. URL: https://doi.org/10.1091/mbc.7.11.1657, doi:10.1091/mbc.7.11.1657. This article has 236 citations and is from a domain leading peer-reviewed journal.

8. (galli2021haspinmodulatesthe pages 4-6): Martina Galli, Laura Diani, Roberto Quadri, Alessandro Nespoli, Elena Galati, Davide Panigada, Paolo Plevani, and Marco Muzi-Falconi. Haspin modulates the g2/m transition delay in response to polarization failures in budding yeast. Frontiers in Cell and Developmental Biology, Jan 2021. URL: https://doi.org/10.3389/fcell.2020.625717, doi:10.3389/fcell.2020.625717. This article has 6 citations.

9. (galli2021haspinmodulatesthe pages 6-7): Martina Galli, Laura Diani, Roberto Quadri, Alessandro Nespoli, Elena Galati, Davide Panigada, Paolo Plevani, and Marco Muzi-Falconi. Haspin modulates the g2/m transition delay in response to polarization failures in budding yeast. Frontiers in Cell and Developmental Biology, Jan 2021. URL: https://doi.org/10.3389/fcell.2020.625717, doi:10.3389/fcell.2020.625717. This article has 6 citations.

10. (keaton2008nucleocytoplasmictraffickingof pages 9-11): Mignon A. Keaton, Lee Szkotnicki, Aron R. Marquitz, Jake Harrison, Trevin R. Zyla, and Daniel J. Lew. Nucleocytoplasmic trafficking of g2/m regulators in yeast. Molecular biology of the cell, 19 9:4006-18, Sep 2008. URL: https://doi.org/10.1091/mbc.e08-03-0286, doi:10.1091/mbc.e08-03-0286. This article has 43 citations and is from a domain leading peer-reviewed journal.

11. (david2021exploringtheregulation pages 75-77): Alain David. Exploring the regulation of mitotic pp2a-rts1 activity in saccharomyces cerevisiae. ArXiv, Jul 2021. URL: https://doi.org/10.20381/ruor-26657, doi:10.20381/ruor-26657. This article has 0 citations.

12. (mcqueen2013explorationofthe pages 24-28): Jennifer McQueen. Exploration of the budding yeast kinase mck1 in cell cycle regulation. ArXiv, Jan 2013. URL: https://doi.org/10.14288/1.0072986, doi:10.14288/1.0072986. This article has 0 citations.

13. (yasutis2013cellcyclecheckpoint pages 4-5): Kimberly Yasutis and Keith Kozminski. Cell cycle checkpoint regulators reach a zillion. Cell Cycle, 12:1501-1509, May 2013. URL: https://doi.org/10.4161/cc.24637, doi:10.4161/cc.24637. This article has 83 citations and is from a peer-reviewed journal.

14. (yasutis2013cellcyclecheckpoint pages 5-6): Kimberly Yasutis and Keith Kozminski. Cell cycle checkpoint regulators reach a zillion. Cell Cycle, 12:1501-1509, May 2013. URL: https://doi.org/10.4161/cc.24637, doi:10.4161/cc.24637. This article has 83 citations and is from a peer-reviewed journal.

15. (yasutis2013cellcyclecheckpoint pages 1-2): Kimberly Yasutis and Keith Kozminski. Cell cycle checkpoint regulators reach a zillion. Cell Cycle, 12:1501-1509, May 2013. URL: https://doi.org/10.4161/cc.24637, doi:10.4161/cc.24637. This article has 83 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](MIH1-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. kennedy2016redundantregulationof pages 4-6
2. kennedy2016redundantregulationof pages 2-4
3. kennedy2016redundantregulationof pages 1-2
4. keaton2008nucleocytoplasmictraffickingof pages 9-11
5. mcqueen2013explorationofthe pages 24-28
6. keaton2008nucleocytoplasmictraffickingof pages 1-2
7. david2021exploringtheregulation pages 45-59
8. galli2021haspinmodulatesthe pages 4-6
9. galli2021haspinmodulatesthe pages 6-7
10. david2021exploringtheregulation pages 75-77
11. yasutis2013cellcyclecheckpoint pages 4-5
12. yasutis2013cellcyclecheckpoint pages 5-6
13. yasutis2013cellcyclecheckpoint pages 1-2
14. DOI
15. https://doi.org/10.1534/genetics.115.182469
16. https://doi.org/10.1091/mbc.7.11.1657
17. https://doi.org/10.3389/fcell.2020.625717
18. https://doi.org/10.1091/mbc.e08-03-0286
19. https://doi.org/10.1083/jcb.200711014
20. https://doi.org/10.4161/cc.24637
21. https://doi.org/10.6084/m9.figshare.23546118.v1
22. https://doi.org/10.3389/fcell.2020.625717.
23. https://doi.org/10.1091/mbc.e08-03-0286.
24. https://doi.org/10.1083/jcb.200711014.
25. https://doi.org/10.1534/genetics.115.182469,
26. https://doi.org/10.1091/mbc.e08-03-0286,
27. https://doi.org/10.1091/mbc.7.11.1657,
28. https://doi.org/10.20381/ruor-26657,
29. https://doi.org/10.3389/fcell.2020.625717,
30. https://doi.org/10.14288/1.0072986,
31. https://doi.org/10.4161/cc.24637,