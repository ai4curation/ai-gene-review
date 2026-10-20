---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-27T15:49:11.388660'
end_time: '2026-09-27T15:55:53.736233'
duration_seconds: 402.35
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: worm
  gene_id: unc-18
  gene_symbol: unc-18
  uniprot_accession: P34815
  protein_description: 'RecName: Full=Acetylcholine regulator unc-18 {ECO:0000305};
    AltName: Full=Uncoordinated protein 18;'
  gene_info: Name=unc-18 {ECO:0000312|WormBase:F27D9.1a}; Synonyms=lan-2 {ECO:0000312|WormBase:F27D9.1a};
    ORFNames=F27D9.1 {ECO:0000312|WormBase:F27D9.1a};
  organism_full: Caenorhabditis elegans.
  protein_family: Belongs to the STXBP/unc-18/SEC1 family. .
  protein_domains: Sec-1-like_dom1. (IPR043154); Sec-1-like_dom3a. (IPR043127); Sec1-like.
    (IPR001619); Sec1-like_dom2. (IPR027482); Sec1-like_sf. (IPR036045)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 32
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: unc-18-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** P34815
- **Protein Description:** RecName: Full=Acetylcholine regulator unc-18 {ECO:0000305}; AltName: Full=Uncoordinated protein 18;
- **Gene Information:** Name=unc-18 {ECO:0000312|WormBase:F27D9.1a}; Synonyms=lan-2 {ECO:0000312|WormBase:F27D9.1a}; ORFNames=F27D9.1 {ECO:0000312|WormBase:F27D9.1a};
- **Organism (full):** Caenorhabditis elegans.
- **Protein Family:** Belongs to the STXBP/unc-18/SEC1 family. .
- **Key Domains:** Sec-1-like_dom1. (IPR043154); Sec-1-like_dom3a. (IPR043127); Sec1-like. (IPR001619); Sec1-like_dom2. (IPR027482); Sec1-like_sf. (IPR036045)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "unc-18" matches the protein description above**
2. **Verify the organism is correct:** Caenorhabditis elegans.
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'unc-18' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **unc-18** (gene ID: unc-18, UniProt: P34815) in worm.

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
- **UniProt Accession:** P34815
- **Protein Description:** RecName: Full=Acetylcholine regulator unc-18 {ECO:0000305}; AltName: Full=Uncoordinated protein 18;
- **Gene Information:** Name=unc-18 {ECO:0000312|WormBase:F27D9.1a}; Synonyms=lan-2 {ECO:0000312|WormBase:F27D9.1a}; ORFNames=F27D9.1 {ECO:0000312|WormBase:F27D9.1a};
- **Organism (full):** Caenorhabditis elegans.
- **Protein Family:** Belongs to the STXBP/unc-18/SEC1 family. .
- **Key Domains:** Sec-1-like_dom1. (IPR043154); Sec-1-like_dom3a. (IPR043127); Sec1-like. (IPR001619); Sec1-like_dom2. (IPR027482); Sec1-like_sf. (IPR036045)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "unc-18" matches the protein description above**
2. **Verify the organism is correct:** Caenorhabditis elegans.
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'unc-18' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **unc-18** (gene ID: unc-18, UniProt: P34815) in worm.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Functional annotation report: *C. elegans unc-18* (UniProt P34815)

## Executive summary

The requested target is correctly identified as ***Caenorhabditis elegans unc-18***, locus **F27D9.1**, encoding the acetylcholine regulator/uncoordinated protein UNC-18 (UniProt **P34815**). It is a **Sec1/Munc18 (SM)-family protein**, not an enzyme or transporter. Its primary function is to organize the presynaptic membrane-fusion machinery: UNC-18 binds the plasma-membrane syntaxin **UNC-64**, supports syntaxin trafficking and availability, promotes synaptic-vesicle tethering and docking, and enables productive SNARE-complex assembly and vesicle priming. It therefore acts as a molecular chaperone, scaffold, and SNARE-assembly template in regulated exocytosis. Direct worm evidence places this activity at neuronal presynaptic plasma membranes. (weimer2003defectsinsynaptic pages 1-2, gracheva2010differentialregulationof pages 1-2, park2017unc18andtomosyn pages 1-2)

A key recent qualification is that *C. elegans* also has a separate SM-protein paralog, ***uncp-18/T07A9.10***. UNCP-18 can partially compensate for UNC-18, so viable *unc-18* null animals do not represent complete loss of all SM-family activity. This distinction resolves an important ambiguity without changing the identity of P34815. (boeglin2023expressionandfunction pages 1-2, boeglin2023expressionandfunction pages 5-6, boeglin2023expressionandfunction pages 2-3)

## 1. Identity verification

The gene symbol matches the supplied protein. The 2023 *Genetics* study explicitly labels ***unc-18* as F27D9.1** and engineered a reporter at that locus. This is distinct from ***uncp-18/T07A9.10***, a separately encoded paralog. Vertebrate **STXBP1/Munc18-1** is an ortholog used to infer conserved structural mechanisms, but it is not the research target. (boeglin2023expressionandfunction pages 1-2, boeglin2023expressionandfunction pages 2-3)

The supplied InterPro assignments—Sec-1-like domains 1, 2, and 3a within a Sec1-like superfamily fold—are consistent with the literature classification of UNC-18 as an arched, multidomain SM protein. Structure–function work additionally identifies domain 3b as an important regulatory surface for exocytosis. Because UNC-18 has no demonstrated catalytic activity, terms such as “substrate specificity” or “catalyzed reaction” do not apply; its relevant specificity is for cognate neuronal fusion proteins, particularly UNC-64/syntaxin and SNARE assemblies. (graham2011structurefunctionstudyof pages 12-12)

## 2. Primary molecular function

### 2.1 Syntaxin chaperone and trafficking factor

UNC-18 binds UNC-64/syntaxin, including its closed conformation and N-terminal region. This interaction protects or chaperones syntaxin and promotes its anterograde delivery and functional availability at synapses. Closed syntaxin masks its SNARE motif; conversion toward an open state permits association with SNAP-25 and vesicular synaptobrevin. UNC-18 nevertheless does substantially more than simply open syntaxin. Open UNC-64 failed to rescue *unc-18* null animals and slightly worsened physiological defects, demonstrating that UNC-18 remains necessary after syntaxin opening. (weimer2003defectsinsynaptic pages 5-6, weimer2003defectsinsynaptic pages 1-2, graham2011structurefunctionstudyof pages 12-12)

In the decisive experiment, evoked responses were **485 ± 55 pA** in *unc-18(md299)* animals and **333 ± 105 pA** after introduction of open syntaxin. Spontaneous fusion rates were **8.58 ± 1.81 versus 7.0 ± 1.5 events per second**, respectively. Thus, constitutively open syntaxin cannot replace UNC-18’s docking/priming functions. (weimer2003defectsinsynaptic pages 5-6)

### 2.2 Vesicle tethering and docking

Electron microscopy provides strong direct evidence that UNC-18 promotes vesicle targeting to the presynaptic membrane. In *unc-18* mutants, vesicles were still generated and accumulated at synapses, but the membrane-associated fraction fell from **5.8 ± 0.5% in wild type** to **1.5 ± 0.2%, 2.1 ± 0.2%, and 2.4 ± 0.2%** in three mutant alleles—approximately **36% of wild type**, with *P* < 0.0001. The deficit therefore reflects impaired docking rather than vesicle biogenesis. (weimer2003defectsinsynaptic pages 5-6, weimer2003defectsinsynaptic pages 7-8)

Subsequent ultrastructural analysis separated two UNC-18-dependent stages: tethering within approximately **25 nm** of the plasma membrane and direct membrane-contact docking. *unc-64* syntaxin mutants phenocopied loss of both pools, whereas excess/open syntaxin preferentially increased docking. These results support a model in which UNC-18–closed-syntaxin complexes promote early tethering, followed by syntaxin opening and SNARE-dependent docking/priming. (gracheva2010differentialregulationof pages 1-2)

The studies establish that UNC-18 is required for docking but do not prove that it physically bridges vesicles and plasma membrane by itself. Direct tethering, recruitment of another tether, regulation of SNARE organization, and post-fusion maintenance of fusion-competent syntaxin remain mechanistically compatible possibilities. (weimer2003defectsinsynaptic pages 7-8)

### 2.3 SNARE assembly, priming, and fusion competence

The best-supported current model is that UNC-18 binds closed UNC-64, then—together with UNC-13—supports a transition to a productive trans-SNARE complex containing syntaxin, SNAP-25, and synaptobrevin. UNC-18 can subsequently engage the assembling SNARE bundle and stabilize or template correct zippering. UNC-13 therefore does not simply displace UNC-18; the two cooperate during priming. (park2017unc18andtomosyn pages 1-2, calahorro2018thepresynapticmachinery pages 4-6)

Worm genetics places UNC-18-mediated priming at least partly downstream of UNC-13. The gain-of-function **UNC-18(P334A)** substitution increased locomotion and acetylcholine release, partially bypassed UNC-13 deficiency, and synergized with loss of TOM-1/tomosyn to suppress *unc-13* phenotypes. Experiments with the corresponding mammalian Munc18-1(P335A) found enhanced binding to preassembled SNARE complexes and partial bypass of Munc13 in liposome-fusion assays. The latter is conserved-mechanism inference, not direct biochemical proof using purified worm UNC-18. (park2017unc18andtomosyn pages 1-2)

## 3. Cellular and anatomical localization

UNC-18 is predominantly associated with the **nervous system**, where its physiologically established site of action is the **presynaptic cytoplasm/plasma-membrane interface** at chemical synapses, including neuromuscular junctions. Its membrane enrichment is mediated through interactions with syntaxin and other release machinery rather than through a transmembrane segment. TOM-1 loss increases UNC-18 plasma-membrane localization, directly connecting localization with the size of tethered and docked vesicle pools. (gracheva2010differentialregulationof pages 1-2, calahorro2018thepresynapticmachinery pages 4-6)

Recent reporter analysis also detected *unc-18* expression in the **intestine and male gonad**, and figure annotations included neuronal, intestinal, head-muscle, and hypodermal signals. However, the most precisely demonstrated molecular role remains presynaptic exocytosis; reporter expression alone should not be interpreted as proof of the same release mechanism in every tissue. (boeglin2023expressionandfunction pages 1-2, boeglin2023expressionandfunction pages 2-3)

## 4. Pathway placement and principal interaction network

The core pathway is regulated neuronal exocytosis:

1. UNC-18 associates with closed UNC-64/syntaxin and supports its trafficking and availability.
2. Synaptic vesicles are brought into UNC-18-dependent proximity with the presynaptic membrane.
3. UNC-13 promotes syntaxin opening while cooperating with UNC-18.
4. UNC-18 helps template productive assembly of UNC-64, SNAP-25, and synaptobrevin into a trans-SNARE complex.
5. The vesicle becomes primed and fusion competent; Ca²⁺ entry and synaptotagmin then trigger rapid fusion.
6. TOM-1/tomosyn opposes productive syntaxin/SNARE engagement and thereby antagonizes UNC-18-dependent targeting and priming. (park2017unc18andtomosyn pages 1-2, gracheva2010differentialregulationof pages 1-2)

In *tom-1* mutants, UNC-18 membrane localization and both tethered and docked vesicle pools increase. In *tom-1;unc-18* double mutants, the docked/primed pool is preferentially restored relative to *unc-18* alone. This places TOM-1 and UNC-18 in an antagonistic regulatory module centered on syntaxin. (gracheva2010differentialregulationof pages 1-2)

Although the historical name “acetylcholine regulator” reflects strong phenotypes at cholinergic neuromuscular junctions, UNC-18 is not an acetylcholine-synthesis enzyme or acetylcholine transporter. It is part of the general neuronal vesicle-release apparatus and can affect both excitatory and inhibitory transmission. (huang2023doublemutationof pages 4-7, huang2023doublemutationof pages 13-17)

## 5. Biological processes and phenotypes

Loss of UNC-18 severely reduces spontaneous and evoked neurotransmitter release and produces profound paralysis/uncoordinated locomotion. Adult neuronal architecture is sufficiently preserved that the phenotype is interpreted principally as failed synaptic transmission, not wholesale failure of neuronal development or maintenance. (weimer2003defectsinsynaptic pages 5-6, weimer2003defectsinsynaptic pages 1-2)

UNC-18 acts during multiple successive release stages rather than at one isolated endpoint: syntaxin trafficking, vesicle tethering, docking, priming, and fusion competence. Domain-3b mutagenesis can reduce exocytosis while preserving binding to closed syntaxin and assembled SNARE complexes, indicating that regulatory surfaces outside the canonical syntaxin-binding cavity contribute to secretion. (graham2011structurefunctionstudyof pages 12-12)

The strongest direct evidence concerns synaptic vesicles. Reports that UNC-18 regulates dense-core secretion are biologically plausible and consistent with the broad SM-protein role, but the retrieved evidence does not provide equally precise worm-specific quantitative measurements for dense-core vesicle docking or peptide release. That aspect should therefore receive lower confidence than the synaptic-vesicle annotation.

## 6. Recent developments, 2023–2024

### Paralog compensation revises null-mutant interpretation

Boeglin, Leyva-Díaz, and Hobert, published online **5 October 2023**, showed that UNCP-18 is ubiquitously expressed and overlaps functionally with UNC-18. UNCP-18 overexpression partially rescued *unc-18*-null locomotion. Conversely, *unc-18;uncp-18* double-null larvae or adults were not recovered; crosses expected to generate double-null progeny produced approximately **25% inviable embryos**, consistent with fully penetrant double-null embryonic lethality. Thus, viable *unc-18* null worms retain paralogous SM activity, and their synaptic phenotype should not be equated with complete removal of SM-dependent secretion. DOI: https://doi.org/10.1093/genetics/iyad180. (boeglin2023expressionandfunction pages 1-2, boeglin2023expressionandfunction pages 5-6)

### Gain-of-function interactions reveal excitation/inhibition constraints

A **2023 bioRxiv preprint** examined open UNC-64 together with UNC-18(P334A). Each mutation can enhance exocytosis separately, but the combination was nonadditive: excitatory evoked charge transfer increased while spontaneous and evoked inhibitory transmission declined, producing excitation/inhibition imbalance. Increased acetylcholine release and aldicarb sensitivity did not translate into better locomotion, growth, body size, or brood size. This demonstrates that globally accelerating SNARE assembly is not necessarily beneficial and that excitatory and inhibitory terminals respond differently to the same exocytosis-enhancing mutations. Posted August 2023; DOI: https://doi.org/10.1101/2023.08.18.553709. Because it is a preprint, these findings warrant less evidentiary weight than the peer-reviewed studies. (huang2023doublemutationof pages 4-7, huang2023doublemutationof pages 13-17)

No 2024 paper retrieved here provided a new UNC-18-specific molecular mechanism. The major 2024 *C. elegans* neurogenesis review supplies broader nervous-system context rather than revising the UNC-18 annotation.

## 7. Research applications and translational relevance

*C. elegans unc-18* is used as an in vivo platform to dissect conserved SM/SNARE mechanisms by combining null and gain-of-function alleles with electron microscopy, electrophysiology, locomotion, thrashing, and aldicarb assays. Open-syntaxin and UNC-18(P334A) alleles are especially useful for ordering release factors genetically and testing whether deficits in UNC-13, UNC-31/CAPS, synaptotagmin, or TOM-1 can be bypassed. (park2017unc18andtomosyn pages 1-2, huang2023doublemutationof pages 4-7)

The system also has relevance to human **STXBP1/Munc18-1** disorders. A human STXBP1 variant has been functionally tested by rescue of *unc-18*-null worm locomotion and aldicarb phenotypes, illustrating how the worm can evaluate conserved neurosecretory defects. Such experiments are translational models, not evidence that worm UNC-18 itself causes human disease.

## 8. Evidence summary

| Annotation aspect | Best-supported conclusion | Direct evidence / quantitative result | Evidence type | Source |
|---|---|---|---|---|
| Identity versus UNCP-18 | The target is *C. elegans unc-18*, locus **F27D9.1**, encoding UNC-18 (UniProt **P34815**). It is distinct from paralog **uncp-18/T07A9.10** and vertebrate STXBP1/Munc18-1. | A CRISPR reporter was engineered at F27D9.1; T07A9.10 was independently identified as UNCP-18. | Direct worm genomic and reporter evidence | Boeglin et al., 2023, [DOI](https://doi.org/10.1093/genetics/iyad180) (boeglin2023expressionandfunction pages 1-2, boeglin2023expressionandfunction pages 2-3) |
| Molecular class and domains | UNC-18 is a nonenzymatic Sec1/Munc18 (SM) trafficking factor with the characteristic three-domain Sec1-like fold. It regulates neuronal SNARE assembly rather than catalyzing a reaction or transporting a substrate. | Worm studies classify it as an SM protein; domain-3b mutagenesis altered exocytosis without eliminating closed-syntaxin or assembled-SNARE binding. | Direct worm structure-function evidence plus family inference | Graham et al., 2011, [DOI](https://doi.org/10.1371/journal.pone.0017999) (graham2011structurefunctionstudyof pages 12-12) |
| Expression and localization | UNC-18 is expressed mainly in the nervous system, with additional expression in intestine and male gonad. Its synaptic function occurs at presynaptic plasma membranes through association with syntaxin and release machinery. | Reporter analysis detected nervous-system, intestinal, and male-gonadal expression. Loss of *tom-1* increased UNC-18 plasma-membrane localization. | Direct worm reporter, localization, and genetic evidence | Boeglin et al., 2023, [DOI](https://doi.org/10.1093/genetics/iyad180); Gracheva et al., 2010, [DOI](https://doi.org/10.3389/fnsyn.2010.00141) (boeglin2023expressionandfunction pages 1-2, gracheva2010differentialregulationof pages 1-2) |
| UNC-64/syntaxin and SNARE mechanism | UNC-18 binds UNC-64/syntaxin, supports syntaxin stability or trafficking, and enables productive SNARE assembly with SNAP-25 and synaptobrevin. Its role extends beyond opening syntaxin. | Open UNC-64 did not rescue *unc-18* nulls: evoked responses were **485 ± 55 pA** in *unc-18(md299)* versus **333 ± 105 pA** with open syntaxin; spontaneous activity was **8.58 ± 1.81** versus **7.0 ± 1.5 events/s**. | Direct worm genetics and electrophysiology | Weimer et al., 2003, [DOI](https://doi.org/10.1038/nn1118) (weimer2003defectsinsynaptic pages 5-6, weimer2003defectsinsynaptic pages 1-2) |
| Vesicle tethering and docking | UNC-18 promotes synaptic-vesicle tethering within about 25 nm of the presynaptic membrane and membrane-contact docking. The phenotype is not due to failure to generate vesicles. | Membrane-associated vesicles declined from **5.8 ± 0.5%** in wild type to **1.5 ± 0.2%**, **2.1 ± 0.2%**, and **2.4 ± 0.2%** in three *unc-18* alleles, about **36% of wild type**; *P* < 0.0001. | Direct worm electron microscopy, genetics, and physiology | Weimer et al., 2003, [DOI](https://doi.org/10.1038/nn1118); Gracheva et al., 2010, [DOI](https://doi.org/10.3389/fnsyn.2010.00141) (weimer2003defectsinsynaptic pages 5-6, weimer2003defectsinsynaptic pages 7-8, gracheva2010differentialregulationof pages 1-2) |
| Priming with UNC-13 | UNC-18 acts with and partly downstream of UNC-13 to form fusion-competent SNARE complexes. UNC-13-dependent syntaxin opening does not remove the requirement for UNC-18. | Gain-of-function UNC-18(P334A) increased locomotion and acetylcholine release and partly bypassed UNC-13 deficiency; open syntaxin aggravated *unc-18* defects. | Direct worm genetic, behavioral, and secretion evidence | Park et al., 2017, [DOI](https://doi.org/10.1523/JNEUROSCI.0338-17.2017) (park2017unc18andtomosyn pages 1-2) |
| TOM-1/tomosyn antagonism | TOM-1 opposes UNC-18-dependent targeting and priming within the syntaxin/SNARE pathway. | *tom-1* mutants increased UNC-18 membrane localization and tethered and docked vesicles. In *tom-1;unc-18* animals, the docked/primed pool was preferentially restored. | Direct worm localization, ultrastructural, and genetic evidence | Gracheva et al., 2010, [DOI](https://doi.org/10.3389/fnsyn.2010.00141); Park et al., 2017, [DOI](https://doi.org/10.1523/JNEUROSCI.0338-17.2017) (gracheva2010differentialregulationof pages 1-2, park2017unc18andtomosyn pages 1-2) |
| 2023 paralog compensation | UNCP-18 can partly compensate for neuronal UNC-18, and both proteins are redundantly required for embryonic viability. An *unc-18* null therefore does not eliminate all SM-family activity. | *uncp-18* overexpression partly rescued *unc-18*-null locomotion. Double-null larvae or adults were not recovered; relevant crosses produced about **25% inviable progeny**, consistent with fully penetrant double-null embryonic lethality. | Direct worm CRISPR genetics, rescue, and viability analysis | Boeglin et al., October 5, 2023, [DOI](https://doi.org/10.1093/genetics/iyad180) (boeglin2023expressionandfunction pages 1-2, boeglin2023expressionandfunction pages 5-6) |
| 2023 P334A/open-syntaxin interaction | Open UNC-64 and UNC-18(P334A) individually enhance exocytosis, but their combination is nonadditive and can cause excitation/inhibition imbalance and behavioral impairment. | The double mutant increased excitatory evoked charge transfer but reduced spontaneous and evoked inhibitory release. Despite increased aldicarb sensitivity, it did not improve locomotion, growth, body size, or brood size. | Direct worm electrophysiology and behavior; preprint | Huang et al., August 2023, [DOI](https://doi.org/10.1101/2023.08.18.553709) (huang2023doublemutationof pages 4-7, huang2023doublemutationof pages 13-17) |
| Structural and liposome-fusion model | A conserved model proposes that Munc18/UNC-18 templates syntaxin-synaptobrevin assembly and that P334A/P335A favors productive SNARE-complex formation. | Mammalian Munc18-1(P335A) bound preassembled SNARE complexes more strongly and partly bypassed Munc13-1 in liposome-fusion assays. This supports, but does not directly establish, the worm mechanism. | **Conserved-mechanism inference from mammalian proteins**, integrated with worm genetics | Park et al., 2017, [DOI](https://doi.org/10.1523/JNEUROSCI.0338-17.2017) (park2017unc18andtomosyn pages 1-2) |


*Table: Evidence table for *C. elegans* UNC-18 (F27D9.1/P34815), covering identity, localization, molecular mechanism, vesicle-release functions, and recent findings. Direct worm evidence is distinguished from conserved-mechanism inference based on mammalian proteins.*

## 9. Recommended functional annotation

**Molecular function:** neuronal Sec1/Munc18-family syntaxin-binding protein; nonenzymatic chaperone and template for cognate SNARE-complex assembly.

**Primary biological process:** regulated synaptic-vesicle exocytosis, with experimentally supported roles in UNC-64 trafficking/availability, vesicle tethering, docking, priming, and acquisition of fusion competence.

**Principal location:** neuronal presynaptic cytoplasm and presynaptic plasma membrane, recruited or stabilized through syntaxin and associated release machinery.

**Core pathway:** UNC-64/syntaxin–SNAP-25–synaptobrevin SNARE-mediated neurotransmitter release, acting cooperatively with UNC-13 and antagonistically with TOM-1/tomosyn.

**Confidence:** high for the presynaptic syntaxin/SNARE, tethering, docking, and priming annotation; moderate for broader non-neuronal secretion; and lower for detailed dense-core-vesicle roles in the absence of equally direct worm-specific quantitative evidence.

### Key dated sources

- Weimer et al., *Nature Neuroscience*, published online **14 September 2003**: https://doi.org/10.1038/nn1118. (weimer2003defectsinsynaptic pages 5-6, weimer2003defectsinsynaptic pages 1-2)
- Gracheva et al., *Frontiers in Synaptic Neuroscience*, **July 2010**: https://doi.org/10.3389/fnsyn.2010.00141. (gracheva2010differentialregulationof pages 1-2)
- Graham et al., *PLoS ONE*, **March 2011**: https://doi.org/10.1371/journal.pone.0017999. (graham2011structurefunctionstudyof pages 12-12)
- Park et al., *Journal of Neuroscience*, **August 2017**: https://doi.org/10.1523/JNEUROSCI.0338-17.2017. (park2017unc18andtomosyn pages 1-2)
- Calahorro and Izquierdo, *Invertebrate Neuroscience*, **March 2018**: https://doi.org/10.1007/s10158-018-0207-5. (calahorro2018thepresynapticmachinery pages 4-6)
- Boeglin et al., *Genetics*, published online **5 October 2023**: https://doi.org/10.1093/genetics/iyad180. (boeglin2023expressionandfunction pages 1-2)
- Huang et al., bioRxiv preprint, **August 2023**: https://doi.org/10.1101/2023.08.18.553709. (huang2023doublemutationof pages 4-7, huang2023doublemutationof pages 13-17)

References

1. (weimer2003defectsinsynaptic pages 1-2): Robby M Weimer, Janet E Richmond, Warren S Davis, Gayla Hadwiger, Michael L Nonet, and Erik M Jorgensen. Defects in synaptic vesicle docking in unc-18 mutants. Nature Neuroscience, 6:1023-1030, Oct 2003. URL: https://doi.org/10.1038/nn1118, doi:10.1038/nn1118. This article has 323 citations and is from a highest quality peer-reviewed journal.

2. (gracheva2010differentialregulationof pages 1-2): Elena O. Gracheva, Ed B. Maryon, Martine Berthelot-Grosjean, and Janet E. Richmond. Differential regulation of synaptic vesicle tethering and docking by unc-18 and tom-1. Frontiers in Synaptic Neuroscience, Jul 2010. URL: https://doi.org/10.3389/fnsyn.2010.00141, doi:10.3389/fnsyn.2010.00141. This article has 48 citations.

3. (park2017unc18andtomosyn pages 1-2): Seungmee Park, Na-Ryum Bin, Bin Yu, Raymond Wong, Ewa Sitarska, Kyoko Sugita, Ke Ma, Junjie Xu, Chi-Wei Tien, Arash Algouneh, Ekaterina Turlova, Siyan Wang, Pranay Siriya, Waleed Shahid, Lorraine Kalia, Zhong-Ping Feng, Philippe P. Monnier, Hong-Shuo Sun, Mei Zhen, Shangbang Gao, Josep Rizo, and Shuzo Sugita. Unc-18 and tomosyn antagonistically control synaptic vesicle priming downstream of unc-13 in <i>caenorhabditis elegans</i>. The Journal of Neuroscience, 37:8797-8815, Aug 2017. URL: https://doi.org/10.1523/jneurosci.0338-17.2017, doi:10.1523/jneurosci.0338-17.2017. This article has 42 citations.

4. (boeglin2023expressionandfunction pages 1-2): Marion Boeglin, Eduardo Leyva-Díaz, and Oliver Hobert. Expression and function of caenorhabditis elegans uncp-18, a paralog of the sm protein unc-18. Genetics, Oct 2023. URL: https://doi.org/10.1093/genetics/iyad180, doi:10.1093/genetics/iyad180. This article has 6 citations and is from a domain leading peer-reviewed journal.

5. (boeglin2023expressionandfunction pages 5-6): Marion Boeglin, Eduardo Leyva-Díaz, and Oliver Hobert. Expression and function of caenorhabditis elegans uncp-18, a paralog of the sm protein unc-18. Genetics, Oct 2023. URL: https://doi.org/10.1093/genetics/iyad180, doi:10.1093/genetics/iyad180. This article has 6 citations and is from a domain leading peer-reviewed journal.

6. (boeglin2023expressionandfunction pages 2-3): Marion Boeglin, Eduardo Leyva-Díaz, and Oliver Hobert. Expression and function of caenorhabditis elegans uncp-18, a paralog of the sm protein unc-18. Genetics, Oct 2023. URL: https://doi.org/10.1093/genetics/iyad180, doi:10.1093/genetics/iyad180. This article has 6 citations and is from a domain leading peer-reviewed journal.

7. (graham2011structurefunctionstudyof pages 12-12): Margaret E. Graham, Gerald R. Prescott, James R. Johnson, Mathew Jones, Alice Walmesley, Lee P. Haynes, Alan Morgan, Robert D. Burgoyne, and Jeff W. Barclay. Structure-function study of mammalian munc18-1 and c. elegans unc-18 implicates domain 3b in the regulation of exocytosis. PLoS ONE, 6:e17999, Mar 2011. URL: https://doi.org/10.1371/journal.pone.0017999, doi:10.1371/journal.pone.0017999. This article has 26 citations and is from a peer-reviewed journal.

8. (weimer2003defectsinsynaptic pages 5-6): Robby M Weimer, Janet E Richmond, Warren S Davis, Gayla Hadwiger, Michael L Nonet, and Erik M Jorgensen. Defects in synaptic vesicle docking in unc-18 mutants. Nature Neuroscience, 6:1023-1030, Oct 2003. URL: https://doi.org/10.1038/nn1118, doi:10.1038/nn1118. This article has 323 citations and is from a highest quality peer-reviewed journal.

9. (weimer2003defectsinsynaptic pages 7-8): Robby M Weimer, Janet E Richmond, Warren S Davis, Gayla Hadwiger, Michael L Nonet, and Erik M Jorgensen. Defects in synaptic vesicle docking in unc-18 mutants. Nature Neuroscience, 6:1023-1030, Oct 2003. URL: https://doi.org/10.1038/nn1118, doi:10.1038/nn1118. This article has 323 citations and is from a highest quality peer-reviewed journal.

10. (calahorro2018thepresynapticmachinery pages 4-6): Fernando Calahorro and Patricia G. Izquierdo. The presynaptic machinery at the synapse of c. elegans. Invertebrate Neuroscience, Mar 2018. URL: https://doi.org/10.1007/s10158-018-0207-5, doi:10.1007/s10158-018-0207-5. This article has 42 citations and is from a peer-reviewed journal.

11. (huang2023doublemutationof pages 4-7): Mengjia Huang, Ya Wang, Chun Hin Chow, Karolina P. Stepien, Karen Indrawinata, Junjie Xu, Peter Argiropoulos, Xiaoyu Xie, Kyoko Sugita, Chi-Wei Tien, Soomin Lee, Philippe P. Monnier, Josep Rizo, Shangbang Gao, and Shuzo Sugita. Double mutation of open syntaxin and unc-18 p334a leads to excitatory-inhibitory imbalance and impairs multiple aspects of c. elegans behavior. bioRxiv, Aug 2023. URL: https://doi.org/10.1101/2023.08.18.553709, doi:10.1101/2023.08.18.553709. This article has 1 citations.

12. (huang2023doublemutationof pages 13-17): Mengjia Huang, Ya Wang, Chun Hin Chow, Karolina P. Stepien, Karen Indrawinata, Junjie Xu, Peter Argiropoulos, Xiaoyu Xie, Kyoko Sugita, Chi-Wei Tien, Soomin Lee, Philippe P. Monnier, Josep Rizo, Shangbang Gao, and Shuzo Sugita. Double mutation of open syntaxin and unc-18 p334a leads to excitatory-inhibitory imbalance and impairs multiple aspects of c. elegans behavior. bioRxiv, Aug 2023. URL: https://doi.org/10.1101/2023.08.18.553709, doi:10.1101/2023.08.18.553709. This article has 1 citations.

## Artifacts

- [Edison artifact artifact-00](unc-18-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. graham2011structurefunctionstudyof pages 12-12
2. weimer2003defectsinsynaptic pages 5-6
3. gracheva2010differentialregulationof pages 1-2
4. weimer2003defectsinsynaptic pages 7-8
5. calahorro2018thepresynapticmachinery pages 4-6
6. boeglin2023expressionandfunction pages 1-2
7. weimer2003defectsinsynaptic pages 1-2
8. boeglin2023expressionandfunction pages 5-6
9. boeglin2023expressionandfunction pages 2-3
10. huang2023doublemutationof pages 4-7
11. huang2023doublemutationof pages 13-17
12. DOI
13. https://doi.org/10.1093/genetics/iyad180.
14. https://doi.org/10.1101/2023.08.18.553709.
15. https://doi.org/10.1093/genetics/iyad180
16. https://doi.org/10.1371/journal.pone.0017999
17. https://doi.org/10.3389/fnsyn.2010.00141
18. https://doi.org/10.1038/nn1118
19. https://doi.org/10.1523/JNEUROSCI.0338-17.2017
20. https://doi.org/10.1101/2023.08.18.553709
21. https://doi.org/10.1038/nn1118.
22. https://doi.org/10.3389/fnsyn.2010.00141.
23. https://doi.org/10.1371/journal.pone.0017999.
24. https://doi.org/10.1523/JNEUROSCI.0338-17.2017.
25. https://doi.org/10.1007/s10158-018-0207-5.
26. https://doi.org/10.1038/nn1118,
27. https://doi.org/10.3389/fnsyn.2010.00141,
28. https://doi.org/10.1523/jneurosci.0338-17.2017,
29. https://doi.org/10.1093/genetics/iyad180,
30. https://doi.org/10.1371/journal.pone.0017999,
31. https://doi.org/10.1007/s10158-018-0207-5,
32. https://doi.org/10.1101/2023.08.18.553709,