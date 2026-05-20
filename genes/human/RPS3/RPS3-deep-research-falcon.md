---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-12T19:13:15.803990'
end_time: '2026-05-12T19:38:03.653005'
duration_seconds: 1487.85
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 30
---

## Question

Concise GO annotation research for human RPS3 / UniProt P23396 (40S ribosomal protein S3, uS3). Focus only on GO-relevant evidence: core role as structural constituent of the small ribosomal subunit/cytosolic ribosome and cytoplasmic translation; cellular locations cytosolic small ribosomal subunit, ribosome, cytosol/cytoplasm, nucleus/nucleolus, synapse/postsynaptic density, mitochondrial inner membrane or ER if supported; non-ribosomal activities including damaged DNA binding, class I DNA-(apurinic/apyrimidinic site) endonuclease/AP lyase activity, base-excision repair/DNA damage response, interactions with APEX1/OGG1, wide-range base-damage endonuclease claims; regulation of NF-kB or transcription by RNA polymerase II, DNA-binding transcription factor binding/coactivator caveats; apoptosis regulation; RNA binding. Include caveats for generic protein binding, high-throughput interactome rows, over-broad cell division/apoptosis/development terms, and whether DNA repair enzymatic activity is direct and physiologically core or secondary. Include PMID/DOI citations and keep under 1500 words.

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

Concise GO annotation research for human RPS3 / UniProt P23396 (40S ribosomal protein S3, uS3). Focus only on GO-relevant evidence: core role as structural constituent of the small ribosomal subunit/cytosolic ribosome and cytoplasmic translation; cellular locations cytosolic small ribosomal subunit, ribosome, cytosol/cytoplasm, nucleus/nucleolus, synapse/postsynaptic density, mitochondrial inner membrane or ER if supported; non-ribosomal activities including damaged DNA binding, class I DNA-(apurinic/apyrimidinic site) endonuclease/AP lyase activity, base-excision repair/DNA damage response, interactions with APEX1/OGG1, wide-range base-damage endonuclease claims; regulation of NF-kB or transcription by RNA polymerase II, DNA-binding transcription factor binding/coactivator caveats; apoptosis regulation; RNA binding. Include caveats for generic protein binding, high-throughput interactome rows, over-broad cell division/apoptosis/development terms, and whether DNA repair enzymatic activity is direct and physiologically core or secondary. Include PMID/DOI citations and keep under 1500 words.

## Concise GO annotation research report: Human **RPS3** (UniProt **P23396**, 40S ribosomal protein S3 / uS3)

### Scope and key GO concepts
RPS3 is a core protein of the **cytosolic small ribosomal subunit (40S)** and therefore supports GO annotations centered on (i) **structural constituent of ribosome**, (ii) **cytoplasmic translation**, and (iii) localization to **cytosolic ribosome / small ribosomal subunit / cytosol (cytoplasm)**. Evidence also supports **nuclear** (and more cautiously **nucleolar**) presence tied to **ribosome biogenesis** and to stimulus-dependent “moonlighting” signaling roles. (dionne2018characterizationofzinc pages 26-29, dionne2018characterizationofzinc pages 10-15)

A second tier of GO-relevant “extra-ribosomal” evidence (DNA lesion binding/BER cofactor activity, NF-κB transcriptional specificity, apoptosis) exists, but requires careful caveats about direct catalytic activity vs **cofactor/interaction** roles, species extrapolations, and the frequent reliance on **review synthesis** rather than modern physiological genetics. (gao2011ribosomalproteins3 pages 2-3, wan2011ikkβphosphorylationregulates pages 1-3)

| GO aspect | Suggested GO term name | Evidence summary | Evidence type | Key citations | Caveats |
|---|---|---|---|---|---|
| MF | structural constituent of ribosome | RPS3/uS3 is a canonical 40S small-subunit protein; assembly literature supports incorporation into pre-40S particles and mature cytosolic ribosomes (dionne2018characterizationofzinc pages 26-29, dionne2018characterizationofzinc pages 10-15) | low-throughput + background/review | Wan et al., Nat Immunol. 2011, doi:10.1038/ni.2007, Mar 2011, https://doi.org/10.1038/ni.2007 (wan2011ikkβphosphorylationregulates pages 1-3); Dionne 2018 thesis excerpts (dionne2018characterizationofzinc pages 26-29, dionne2018characterizationofzinc pages 10-15) | Core/physiologic role; strongest GO support. Some assembly details derive from yeast-conserved pathways rather than direct human perturbation. |
| BP | cytoplasmic translation | Proteomics and ribosome-biology sources place RPS3 in the cytosolic 40S machinery supporting translation; 2024 tumor proteomics enriched DEPs in cytoplasmic translation/cytosolic ribosome/structural constituent of ribosome (tan2019theinteractomeof pages 13-15, tong2024proteomicsshowsthat pages 3-5) | high-throughput + background | Tong et al., Sci Rep 2024-07, doi:10.1038/s41598-024-58967-y, https://doi.org/10.1038/s41598-024-58967-y (tong2024proteomicsshowsthat pages 3-5) | Enrichment/proteomics is indirect for RPS3-specific function, but aligns with canonical biology. |
| CC | cytosolic small ribosomal subunit / cytosolic ribosome / cytosol | RPS3 detected with multiple ribosomal proteins in AP-MS/proteomics datasets; consistent with 40S/cytosolic ribosome localization (tan2019theinteractomeof pages 13-15, zeng2023spatiallyresolvedsinglecell pages 3-5) | high-throughput + orthogonal method use | Zeng et al., Science 2023-06, doi:10.1126/science.add3067, https://doi.org/10.1126/science.add3067 (zeng2023spatiallyresolvedsinglecell pages 3-5); Tong et al. 2024 (tong2024proteomicsshowsthat pages 3-5) | AP-MS and antibody-based ribosome targeting support localization/association, not independent proof of all subcellular contexts. |
| CC | nucleus | uS3/RPS3 is imported to the nucleus for pre-40S incorporation; multiple studies show stimulus-dependent nuclear translocation in extra-ribosomal contexts (NF-κB, apoptosis, DNA damage) (dionne2018characterizationofzinc pages 26-29, gao2011ribosomalproteins3 pages 2-3, jang2004rps3adna pages 3-4, wan2011ikkβphosphorylationregulates pages 1-3) | low-throughput | Wan et al., Nat Immunol. 2011, doi:10.1038/ni.2007, https://doi.org/10.1038/ni.2007 (wan2011ikkβphosphorylationregulates pages 1-3); Jang et al., FEBS Lett. 2004-02, doi:10.1016/S0014-5793(04)00074-2, https://doi.org/10.1016/S0014-5793(04)00074-2 (jang2004rps3adna pages 3-4) | Nuclear localization is well supported, but occurs in both ribosome biogenesis and moonlighting pathways; annotation should avoid overgeneralizing to transcription regulation per se. |
| CC | nucleolus | Ribosome-biogenesis context and intronic snoRNA biology of human RPS3 support nucleolar relevance during ribosome assembly/processing (lim2002completegenomicstructure pages 7-7) | low-throughput + background | Lim et al., Gene 2002-03, doi:10.1016/S0378-1119(02)00502-4, https://doi.org/10.1016/S0378-1119(02)00502-4 (lim2002completegenomicstructure pages 7-7) | Evidence is more about RPS3 gene-associated snoRNA/biogenesis context than direct imaging of RPS3 protein in nucleoli. Use cautiously. |
| CC | synapse / postsynaptic density | Recent data support ribosome/translation machinery near synaptic compartments; RPS3 was used as a ribosome marker in spatial translatomics, and synaptosome proteomics supports synaptic local translation context (gorski2025insightsintosynaptic pages 71-74, zeng2023spatiallyresolvedsinglecell pages 3-5) | high-throughput | Zeng et al., Science 2023-06, doi:10.1126/science.add3067, https://doi.org/10.1126/science.add3067 (zeng2023spatiallyresolvedsinglecell pages 3-5) | Evidence is indirect for human RPS3-specific PSD residency; better treated as synaptic ribosome/local translation association, not a definitive stable PSD component. |
| MF | RNA binding | RPS3 contains a KH domain; review/primary NF-κB literature notes KH-domain-mediated ssRNA/ssDNA binding and association with p65 (wan2010thenuclearsignaling pages 1-2, gao2011ribosomalproteins3 pages 1-2) | review + low-throughput | Wan & Lenardo, Cell Res. 2010-12, doi:10.1038/cr.2009.137, https://doi.org/10.1038/cr.2009.137 (wan2010thenuclearsignaling pages 1-2) | RNA binding is credible, but much evidence is domain-based or in NF-κB context; avoid broad annotations to sequence-specific RNA regulation without direct assays. |
| MF | damaged DNA binding | Human RPS3 binds tightly to abasic (AP) and 8-oxoG lesions; cited as damaged-DNA recognition in BER-related studies (gao2011ribosomalproteins3 pages 2-3, wan2011ikkβphosphorylationregulates pages 11-13) | review summarizing primary low-throughput | Gao & Hardwidge, Front Microbiol. 2011-06, doi:10.3389/fmicb.2011.00137, https://doi.org/10.3389/fmicb.2011.00137 (gao2011ribosomalproteins3 pages 2-3); Wan et al. 2011 cites Hegde 2004 PMID:14706345 (wan2011ikkβphosphorylationregulates pages 11-13) | Stronger for lesion binding than for direct catalytic repair in vivo. Much wording comes through reviews citing older primary papers. |
| MF | AP lyase / DNA-(apurinic or apyrimidinic site) endonuclease activity | Historical literature reports human RPS3 as a DNA repair endonuclease and phosphorylation-enhanced endonuclease activity; C-terminus implicated in repair function (gao2011ribosomalproteins3 pages 3-4, jang2004rps3adna pages 3-4, jang2004rps3adna pages 1-2) | low-throughput + review | Jang et al., FEBS Lett. 2004-02, doi:10.1016/S0014-5793(04)00074-2, https://doi.org/10.1016/S0014-5793(04)00074-2 (jang2004rps3adna pages 3-4); Lim et al. 2002, https://doi.org/10.1016/S0378-1119(02)00502-4 (lim2002completegenomicstructure pages 7-7) | Major caveat: direct intrinsic human AP-lyase/endonuclease activity remains debated/secondary; some strongest catalytic evidence is from Drosophila/yeast or engineered variants, not clear core human physiology. |
| BP / MF | base-excision repair; BER enzyme activator/cofactor | Human RPS3 reportedly stimulates uracil-DNA glycosylase, hOGG1, and APE1/Ref-1 while lacking its own glycosylase activity; supports BER participation via cofactor-like action (gao2011ribosomalproteins3 pages 2-3) | review summarizing primary low-throughput | Gao & Hardwidge, Front Microbiol. 2011-06, doi:10.3389/fmicb.2011.00137, https://doi.org/10.3389/fmicb.2011.00137 (gao2011ribosomalproteins3 pages 2-3) | Best framed as interaction/stimulation within BER, not core BER enzyme. Direct physical interaction details with OGG1/APEX1 should be annotated cautiously unless curators verify original primary assays. |
| BP / MF | NF-κB complex cofactor; transcription coactivator activity caveat | RPS3 is a non-Rel NF-κB subunit/specifier that binds p65, enhances selective κB-site occupancy, and requires IKKβ-dependent S209 phosphorylation for nuclear import (wan2010thenuclearsignaling pages 1-2, wan2011ikkβphosphorylationregulates pages 1-3, wan2011ikkβphosphorylationregulates media cf840cd8) | low-throughput + review | Wan et al., Nat Immunol. 2011-03, doi:10.1038/ni.2007, https://doi.org/10.1038/ni.2007 (wan2011ikkβphosphorylationregulates pages 1-3); Wan & Lenardo, Cell Res. 2010-12, doi:10.1038/cr.2009.137, https://doi.org/10.1038/cr.2009.137 (wan2010thenuclearsignaling pages 1-2); Sen et al., Mol Cell 2012-01, doi:10.1016/j.molcel.2011.10.021, https://doi.org/10.1016/j.molcel.2011.10.021 (gao2011ribosomalproteins3 pages 5-6) | Strong for NF-κB cofactor/specifier in selected promoters; weaker for generic “RNA polymerase II transcription” or “DNA-binding transcription factor binding/coactivator” across all contexts. |
| CC / BP | nuclear translocation in NF-κB signaling | Co-IP, phospho-specific blots, microscopy, and fractionation show TNF/PMA-induced S209 phosphorylation, importin-α association, and reduced nuclear entry of S209A mutant (wan2011ikkβphosphorylationregulates pages 1-3, wan2011ikkβphosphorylationregulates media cf840cd8) | low-throughput | Wan et al., Nat Immunol. 2011-03, doi:10.1038/ni.2007, https://doi.org/10.1038/ni.2007 (wan2011ikkβphosphorylationregulates pages 1-3) | Supports regulated nuclear trafficking, not broad chromatin residency. |
| BP | regulation of apoptotic process | RPS3 overexpression/transfection induces apoptosis with caspase-8/caspase-3 dependence; endogenous rpS3 accumulates in nuclei during cytokine-treated apoptosis (jang2004rps3adna pages 3-4, gao2011ribosomalproteins3 pages 3-4) | low-throughput | Jang et al., FEBS Lett. 2004-02, doi:10.1016/S0014-5793(04)00074-2, https://doi.org/10.1016/S0014-5793(04)00074-2 (jang2004rps3adna pages 3-4) | Likely context-dependent moonlighting effect; do not overextend to generic apoptosis/development terms without genetic/physiologic evidence. |
| CC / misc. caution | mitochondrial inner membrane / ER | No convincing direct evidence in gathered RPS3-specific sources for stable mitochondrial inner membrane localization; ER-related translation appears generic/translatome-level, not RPS3-specific (zeng2023spatiallyresolvedsinglecell pages 13-18, zeng2023spatiallyresolvedsinglecell pages 3-5) | negative / insufficient | Zeng et al., Science 2023-06, https://doi.org/10.1126/science.add3067 (zeng2023spatiallyresolvedsinglecell pages 13-18, zeng2023spatiallyresolvedsinglecell pages 3-5) | Avoid GO annotation to mitochondrial inner membrane or ER unless supported by direct targeted localization evidence for human RPS3. |
| misc. caution | generic protein binding / cell division / development terms | Interactome/AP-MS rows detect RPS3 in many complexes but are insufficient for specific GO molecular functions or broad processes without orthogonal validation (rahim2018globalinteractomicsconnect pages 11-12, tan2019theinteractomeof pages 13-15) | high-throughput | Rahim et al., Viruses 2018-12, doi:10.3390/v10120731, https://doi.org/10.3390/v10120731 (rahim2018globalinteractomicsconnect pages 11-12); Tan et al., 2019 preprint, doi:10.21203/rs.2.12355/v1, https://doi.org/10.21203/rs.2.12355/v1 (tan2019theinteractomeof pages 13-15) | Curate generic binding/over-broad process terms conservatively; HTP co-purification does not establish direct function, physiological relevance, or stable localization. |


*Table: This table compiles GO-relevant evidence for human RPS3/P23396 across canonical ribosomal functions, cellular locations, and reported moonlighting activities. It emphasizes evidence strength and caveats to help distinguish core annotations from context-dependent or indirect claims.*

---

### 1) Core ribosomal function (highest-confidence GO)
**Structural constituent of cytosolic ribosome / small ribosomal subunit (MF/CC)**
- Ribosome assembly/biogenesis literature supports that uS3/RPS3 is a canonical 40S protein that is handled by dedicated chaperone pathways and imported for **pre-40S incorporation**, consistent with core ribosome structure. (dionne2018characterizationofzinc pages 26-29)

**Cytoplasmic translation (BP)**
- A 2024 clinical proteomics study of lung adenocarcinoma (LUAD) brain metastases after **gamma knife radiosurgery (GKRS)** shows differentially expressed proteins enriched in **cytoplasmic translation**, and in CC/MF categories including **cytosolic ribosome** and **structural constituent of ribosome**—consistent with RPS3’s canonical GO placement in translation/ribosome. (Tong et al., 2024-07, Scientific Reports; https://doi.org/10.1038/s41598-024-58967-y) (tong2024proteomicsshowsthat pages 3-5)

**Recent quantitative statistic (2024):** proteomics detected **70 ribosomal proteins**, with **53/70 (75.7%) significantly upregulated** after GKRS; no ribosomal protein was significantly downregulated. RPS3 was among proteins reported to accumulate after GKRS. (Tong et al., 2024-07) (tong2024proteomicsshowsthat pages 5-7)

---

### 2) Cellular component annotations: cytosol/cytosolic ribosome; nucleus/nucleolus; synapse/PSD
**Cytosol / cytoplasm / cytosolic ribosome (CC)**
- High-throughput interactome/proteomics studies consistently recover RPS3 alongside many ribosomal proteins, supporting cytosolic ribosome association (but not fine-grained localization). (tan2019theinteractomeof pages 13-15)

**Nucleus (CC)**
- Primary evidence shows stimulus-dependent nuclear translocation in non-ribosomal contexts.
  - In NF-κB signaling, RPS3 nuclear entry depends on **IKKβ phosphorylation (S209)** and association with the nuclear import machinery (importin-α). (Wan et al., 2011-03, Nature Immunology; https://doi.org/10.1038/ni.2007) (wan2011ikkβphosphorylationregulates pages 1-3)
  - In apoptosis paradigms, endogenous rpS3 translocated into nuclei in cytokine-treated cells, and rpS3 overexpression induced caspase-dependent apoptosis. (Jang et al., 2004-02, FEBS Letters; https://doi.org/10.1016/S0014-5793(04)00074-2) (jang2004rps3adna pages 3-4)

**Image-supported evidence (NF-κB/nuclear translocation):** figure panels from Wan et al. (2011) show phosphorylation, co-IP interactions, and nuclear translocation behavior. (wan2011ikkβphosphorylationregulates media cf840cd8, wan2011ikkβphosphorylationregulates media 7c78b978, wan2011ikkβphosphorylationregulates media b6da7309, wan2011ikkβphosphorylationregulates media de8959ff, wan2011ikkβphosphorylationregulates media 799fbec1)

**Nucleolus (CC; cautious)**
- Human RPS3 gene contains an intronic snoRNA (U15b) relevant to nucleolar rRNA processing/biogenesis programs, supporting a nucleolus-linked **gene architecture/biogenesis context**. (Lim et al., 2002-03, Gene; https://doi.org/10.1016/S0378-1119(02)00502-4) (lim2002completegenomicstructure pages 7-7)
- Caveat: this is not direct imaging of RPS3 protein in nucleoli; nucleolar **protein** localization should be annotated conservatively unless supported by direct localization assays. (lim2002completegenomicstructure pages 7-7)

**Synapse / postsynaptic density (CC; limited RPS3-specific evidence)**
- Synaptic/PSD association is currently best supported as **ribosome/translation machinery near synapses**, not as a definitive stable PSD component of RPS3.
  - A mouse synaptosome proteomics study reports ribosomal proteins including an Rps3-family entry among local translation machinery in synaptosomes, consistent with synaptic ribosomes. (gorski2025insightsintosynaptic pages 71-74)
  - In 2023, RPS3 was used as an antibody target to label ribosomes in a spatial translatomics method (RIBOmap), reinforcing its role as a ribosomal marker but not proving PSD residency. (Zeng et al., 2023-06, Science; https://doi.org/10.1126/science.add3067) (zeng2023spatiallyresolvedsinglecell pages 3-5)

**Mitochondrial inner membrane / ER:** no direct, RPS3-specific evidence in the retrieved corpus supports stable mitochondrial inner membrane or ER localization; avoid those CC annotations without targeted localization data. (zeng2023spatiallyresolvedsinglecell pages 13-18)

---

### 3) Non-ribosomal (moonlighting) functions relevant to GO: DNA damage/BER, NF-κB, apoptosis, RNA binding

#### 3.1 Damaged DNA binding and BER-related roles
**Damaged DNA binding (MF): AP sites and 8-oxoG**
- Review-synthesized evidence states human RPS3 binds tightly to **abasic (AP)** sites and **8-oxoG** lesions. (Gao & Hardwidge, 2011-06; https://doi.org/10.3389/fmicb.2011.00137) (gao2011ribosomalproteins3 pages 2-3)

**Interaction with BER enzymes (MF/BP; cofactor framing)**
- The same review summarizes that human RPS3 lacks its own glycosylase activity but can **stimulate** a uracil-DNA glycosylase and BER enzymes **hOGG1** and **APE/Ref-1 (APE1)**. (gao2011ribosomalproteins3 pages 2-3)
- Caveat: because this statement is mediated through a review excerpt here, GO curators should confirm the original primary interaction/enzymology experiments before asserting “direct physical interaction” annotations; best annotated as **modulates/stimulates BER enzyme activity** if primary evidence is verified. (gao2011ribosomalproteins3 pages 2-3)

**AP lyase / AP endonuclease claims (MF; strong caveats)**
- Multiple sources describe RPS3 as a DNA repair endonuclease/AP lyase and map repair activity to the C-terminus, but the excerpts show that the most definitive catalytic evidence often arises from non-human orthologs (e.g., Drosophila/yeast) or engineered conversions, and human intrinsic catalytic status is not resolved here. (jang2004rps3adna pages 1-2, lim2002completegenomicstructure pages 7-7)
- Annotation guidance: treat **DNA lesion binding** and **BER cofactor roles** as better-supported than broad “wide-range base-damage endonuclease” claims unless primary human biochemistry is directly cited. (gao2011ribosomalproteins3 pages 2-3, lim2002completegenomicstructure pages 7-7)

#### 3.2 NF-κB signaling and transcriptional specificity
**NF-κB complex cofactor/specifier (BP/MF; avoid overly broad transcription terms)**
- RPS3 is described as a non-Rel NF-κB subunit that cooperates with Rel dimers for DNA binding and promoter selectivity; its KH domain is important for association with p65, and RPS3 translocates to the nucleus upon stimulation. (Wan & Lenardo, 2010-12, Cell Research; https://doi.org/10.1038/cr.2009.137) (wan2010thenuclearsignaling pages 1-2)

**Mechanistic primary evidence (2011): IKKβ→RPS3 S209 phosphorylation→importin-α association→nuclear translocation**
- Wan et al. demonstrate RPS3 phosphorylation and nuclear import regulation, supporting GO terms related to **NF-κB signaling** and regulated nuclear localization, and justifying cautionary, context-specific annotations such as “positive regulation of NF-κB transcription factor activity” rather than generic “RNA polymerase II transcription.” (Wan et al., 2011-03; https://doi.org/10.1038/ni.2007) (wan2011ikkβphosphorylationregulates pages 1-3)
- Supporting figure panels are available. (wan2011ikkβphosphorylationregulates media cf840cd8, wan2011ikkβphosphorylationregulates media 7c78b978, wan2011ikkβphosphorylationregulates media b6da7309, wan2011ikkβphosphorylationregulates media de8959ff, wan2011ikkβphosphorylationregulates media 799fbec1)

#### 3.3 Apoptosis regulation
- RPS3/rpS3 overexpression induces apoptosis with caspase-8 and caspase-3 dependence, and endogenous rpS3 accumulates in nuclei during cytokine-induced apoptosis; separable N-terminal death-inducing vs C-terminal repair domains were proposed. (Jang et al., 2004-02; https://doi.org/10.1016/S0014-5793(04)00074-2) (jang2004rps3adna pages 3-4)
- Caveat: these are overexpression/transfection and cytokine-treatment paradigms; avoid over-broad developmental/cell-cycle/apoptosis GO terms without genetic physiological evidence. (jang2004rps3adna pages 3-4)

#### 3.4 RNA binding
- RPS3’s KH domain is described as capable of binding single-stranded RNA/DNA and is required for NF-κB complex association; this supports GO:RNA binding in a mechanistically grounded way. (wan2010thenuclearsignaling pages 1-2)

---

### 4) Expert/authoritative interpretation and caveats for GO curation
1. **Core GO annotations should prioritize ribosome/translation**: structural constituent of ribosome, cytosolic small ribosomal subunit/cytosolic ribosome, cytoplasm/cytosol, and cytoplasmic translation are strongly supported and are the physiological primary function. (dionne2018characterizationofzinc pages 26-29, tong2024proteomicsshowsthat pages 3-5)
2. **Nuclear localization is real but context-dependent**: supported for ribosome biogenesis trafficking and for NF-κB/apoptosis responses; annotate nuclear location but avoid implying constitutive transcription factor behavior. (wan2011ikkβphosphorylationregulates pages 1-3, jang2004rps3adna pages 3-4)
3. **DNA repair enzymatic activity claims require caution**: evidence in the retrieved excerpts supports damaged-DNA binding and cofactor-like stimulation of BER enzymes (OGG1/APE1), while direct intrinsic AP-lyase/endonuclease activity for human RPS3 appears historically claimed and may be secondary or context-dependent; species and engineered-variant literature complicates interpretation. (gao2011ribosomalproteins3 pages 2-3, lim2002completegenomicstructure pages 7-7)
4. **Avoid “generic protein binding” and HTP-only overreach**: AP-MS/interactome detections are useful for association but do not establish direct functions, subcellular compartments (e.g., PSD), or broad biological processes. (rahim2018globalinteractomicsconnect pages 11-12, tan2019theinteractomeof pages 13-15)

---

### 5) Recent applications / real-world implementations (2023–2024)
- **Spatial translatomics (methodological application):** RIBOmap (Science 2023) is an in situ translation profiling platform; RPS3 was trialed as an antibody ribosome target (as a ribosomal marker), illustrating real-world use of RPS3 as a translation machinery handle (though the authors preferred rRNA targeting due to signal-to-noise). (Zeng et al., 2023-06; https://doi.org/10.1126/science.add3067) (zeng2023spatiallyresolvedsinglecell pages 3-5)
- **Clinical proteomics (biomedical application):** In LUAD brain metastasis tissue collected in a clinical setting post-GKRS, ribosomal proteins (including RPS3) were prominently upregulated and used in downstream prognostic modeling. (Tong et al., 2024-07; https://doi.org/10.1038/s41598-024-58967-y) (tong2024proteomicsshowsthat pages 5-7)

---

### References (URLs and dates available in evidence)
- Wan F. et al. **Nature Immunology** (2011-03). *IKKβ phosphorylation regulates RPS3 nuclear translocation and NF-κB function…* https://doi.org/10.1038/ni.2007 (wan2011ikkβphosphorylationregulates pages 1-3)
- Wan F., Lenardo MJ. **Cell Research** (2010-12). *The nuclear signaling of NF-κB…* https://doi.org/10.1038/cr.2009.137 (wan2010thenuclearsignaling pages 1-2)
- Gao X., Hardwidge PR. **Frontiers in Microbiology** (2011-06). *Ribosomal Protein S3: A Multifunctional Target…* https://doi.org/10.3389/fmicb.2011.00137 (gao2011ribosomalproteins3 pages 2-3)
- Jang C-Y. et al. **FEBS Letters** (2004-02). *RpS3… is involved in apoptosis* https://doi.org/10.1016/S0014-5793(04)00074-2 (jang2004rps3adna pages 3-4)
- Lim Y. et al. **Gene** (2002-03). *Complete genomic structure of human rpS3…* https://doi.org/10.1016/S0378-1119(02)00502-4 (lim2002completegenomicstructure pages 7-7)
- Zeng H. et al. **Science** (2023-06). *Spatially resolved single-cell translatomics at molecular resolution* https://doi.org/10.1126/science.add3067 (zeng2023spatiallyresolvedsinglecell pages 3-5)
- Tong L. et al. **Scientific Reports** (2024-07). *Proteomics shows that brain metastases… overexpress ribosomal proteins…* https://doi.org/10.1038/s41598-024-58967-y (tong2024proteomicsshowsthat pages 5-7)


References

1. (dionne2018characterizationofzinc pages 26-29): K Dionne. Characterization of zinc finger protein 277 and its role in the extra-ribosomal us5 complex. Unknown journal, 2018.

2. (dionne2018characterizationofzinc pages 10-15): K Dionne. Characterization of zinc finger protein 277 and its role in the extra-ribosomal us5 complex. Unknown journal, 2018.

3. (gao2011ribosomalproteins3 pages 2-3): Xiaofei Gao and Philip R. Hardwidge. Ribosomal protein s3: a multifunctional target of attaching/effacing bacterial pathogens. Frontiers in Microbiology, Jun 2011. URL: https://doi.org/10.3389/fmicb.2011.00137, doi:10.3389/fmicb.2011.00137. This article has 80 citations and is from a peer-reviewed journal.

4. (wan2011ikkβphosphorylationregulates pages 1-3): Fengyi Wan, Amanda Weaver, Xiaofei Gao, Michael Bern, Philip R Hardwidge, and Michael J Lenardo. Ikkβ phosphorylation regulates rps3 nuclear translocation and nf-κb function during infection with escherichia coli strain o157:h7. Mar 2011. URL: https://doi.org/10.1038/ni.2007, doi:10.1038/ni.2007. This article has 170 citations and is from a highest quality peer-reviewed journal.

5. (tan2019theinteractomeof pages 13-15): Min Tan, Guofei Ding, Xinna Cai, Shengliang Cao, Fangyuan Cong, Jiaqi Liu, Yuzhong Zhao, Sidang Liu, Guangliang Liu, and Yihong Xiao. The interactome of porcine epidemic diarrhea virus nucleocapsid protein. ArXiv, Aug 2019. URL: https://doi.org/10.21203/rs.2.12355/v1, doi:10.21203/rs.2.12355/v1. This article has 0 citations.

6. (tong2024proteomicsshowsthat pages 3-5): Luqing Tong, Ke Ye, Qun Chen, Xiaoxi Wang, Chi Hu, Qingsheng Xu, Lihui Zhou, Renya Zhan, and Ying Tong. Proteomics shows that brain metastases of lung adenocarcinoma overexpress ribosomal proteins in response to gamma knife radiosurgery. Scientific Reports, Jul 2024. URL: https://doi.org/10.1038/s41598-024-58967-y, doi:10.1038/s41598-024-58967-y. This article has 4 citations and is from a peer-reviewed journal.

7. (zeng2023spatiallyresolvedsinglecell pages 3-5): Hu Zeng, Jiahao Huang, Jingyi Ren, Connie Kangni Wang, Zefang Tang, Haowen Zhou, Yiming Zhou, Hailing Shi, Abhishek Aditham, Xin Sui, Hongyu Chen, Jennifer A. Lo, and Xiao Wang. Spatially resolved single-cell translatomics at molecular resolution. Science, Jun 2023. URL: https://doi.org/10.1126/science.add3067, doi:10.1126/science.add3067. This article has 190 citations and is from a highest quality peer-reviewed journal.

8. (jang2004rps3adna pages 3-4): Chang-Young Jang, Jae Yung Lee, and Joonhee Kim. Rps3, a dna repair endonuclease and ribosomal protein, is involved in apoptosis. FEBS Letters, 560:81-85, Feb 2004. URL: https://doi.org/10.1016/s0014-5793(04)00074-2, doi:10.1016/s0014-5793(04)00074-2. This article has 186 citations and is from a peer-reviewed journal.

9. (lim2002completegenomicstructure pages 7-7): Yoon Lim, Seong Min Lee, Mijin Kim, Jae Yung Lee, Eun Pyo Moon, Byeong Jae Lee, and Joon Kim. Complete genomic structure of human rps3: identification of functional u15b snorna in the fifth intron. Gene, 286 2:291-7, Mar 2002. URL: https://doi.org/10.1016/s0378-1119(02)00502-4, doi:10.1016/s0378-1119(02)00502-4. This article has 24 citations and is from a peer-reviewed journal.

10. (gorski2025insightsintosynaptic pages 71-74): K Gorski. Insights into synaptic physiology from omics analyses in the early disease onset of cstb-deficient mice modeling epm1. Unknown journal, 2025.

11. (wan2010thenuclearsignaling pages 1-2): Fengyi Wan and Michael J Lenardo. The nuclear signaling of nf-κb: current knowledge, new insights, and future perspectives. Cell Research, 20:24-33, Dec 2010. URL: https://doi.org/10.1038/cr.2009.137, doi:10.1038/cr.2009.137. This article has 525 citations and is from a domain leading peer-reviewed journal.

12. (gao2011ribosomalproteins3 pages 1-2): Xiaofei Gao and Philip R. Hardwidge. Ribosomal protein s3: a multifunctional target of attaching/effacing bacterial pathogens. Frontiers in Microbiology, Jun 2011. URL: https://doi.org/10.3389/fmicb.2011.00137, doi:10.3389/fmicb.2011.00137. This article has 80 citations and is from a peer-reviewed journal.

13. (wan2011ikkβphosphorylationregulates pages 11-13): Fengyi Wan, Amanda Weaver, Xiaofei Gao, Michael Bern, Philip R Hardwidge, and Michael J Lenardo. Ikkβ phosphorylation regulates rps3 nuclear translocation and nf-κb function during infection with escherichia coli strain o157:h7. Mar 2011. URL: https://doi.org/10.1038/ni.2007, doi:10.1038/ni.2007. This article has 170 citations and is from a highest quality peer-reviewed journal.

14. (gao2011ribosomalproteins3 pages 3-4): Xiaofei Gao and Philip R. Hardwidge. Ribosomal protein s3: a multifunctional target of attaching/effacing bacterial pathogens. Frontiers in Microbiology, Jun 2011. URL: https://doi.org/10.3389/fmicb.2011.00137, doi:10.3389/fmicb.2011.00137. This article has 80 citations and is from a peer-reviewed journal.

15. (jang2004rps3adna pages 1-2): Chang-Young Jang, Jae Yung Lee, and Joonhee Kim. Rps3, a dna repair endonuclease and ribosomal protein, is involved in apoptosis. FEBS Letters, 560:81-85, Feb 2004. URL: https://doi.org/10.1016/s0014-5793(04)00074-2, doi:10.1016/s0014-5793(04)00074-2. This article has 186 citations and is from a peer-reviewed journal.

16. (wan2011ikkβphosphorylationregulates media cf840cd8): Fengyi Wan, Amanda Weaver, Xiaofei Gao, Michael Bern, Philip R Hardwidge, and Michael J Lenardo. Ikkβ phosphorylation regulates rps3 nuclear translocation and nf-κb function during infection with escherichia coli strain o157:h7. Mar 2011. URL: https://doi.org/10.1038/ni.2007, doi:10.1038/ni.2007. This article has 170 citations and is from a highest quality peer-reviewed journal.

17. (gao2011ribosomalproteins3 pages 5-6): Xiaofei Gao and Philip R. Hardwidge. Ribosomal protein s3: a multifunctional target of attaching/effacing bacterial pathogens. Frontiers in Microbiology, Jun 2011. URL: https://doi.org/10.3389/fmicb.2011.00137, doi:10.3389/fmicb.2011.00137. This article has 80 citations and is from a peer-reviewed journal.

18. (zeng2023spatiallyresolvedsinglecell pages 13-18): Hu Zeng, Jiahao Huang, Jingyi Ren, Connie Kangni Wang, Zefang Tang, Haowen Zhou, Yiming Zhou, Hailing Shi, Abhishek Aditham, Xin Sui, Hongyu Chen, Jennifer A. Lo, and Xiao Wang. Spatially resolved single-cell translatomics at molecular resolution. Science, Jun 2023. URL: https://doi.org/10.1126/science.add3067, doi:10.1126/science.add3067. This article has 190 citations and is from a highest quality peer-reviewed journal.

19. (rahim2018globalinteractomicsconnect pages 11-12): Md Niaz Rahim, Ludger Klewes, Ali Zahedi-Amiri, Sabine Mai, and Kevin M. Coombs. Global interactomics connect nuclear mitotic apparatus protein numa1 to influenza virus maturation. Viruses, 10:731, Dec 2018. URL: https://doi.org/10.3390/v10120731, doi:10.3390/v10120731. This article has 12 citations.

20. (tong2024proteomicsshowsthat pages 5-7): Luqing Tong, Ke Ye, Qun Chen, Xiaoxi Wang, Chi Hu, Qingsheng Xu, Lihui Zhou, Renya Zhan, and Ying Tong. Proteomics shows that brain metastases of lung adenocarcinoma overexpress ribosomal proteins in response to gamma knife radiosurgery. Scientific Reports, Jul 2024. URL: https://doi.org/10.1038/s41598-024-58967-y, doi:10.1038/s41598-024-58967-y. This article has 4 citations and is from a peer-reviewed journal.

21. (wan2011ikkβphosphorylationregulates media 7c78b978): Fengyi Wan, Amanda Weaver, Xiaofei Gao, Michael Bern, Philip R Hardwidge, and Michael J Lenardo. Ikkβ phosphorylation regulates rps3 nuclear translocation and nf-κb function during infection with escherichia coli strain o157:h7. Mar 2011. URL: https://doi.org/10.1038/ni.2007, doi:10.1038/ni.2007. This article has 170 citations and is from a highest quality peer-reviewed journal.

22. (wan2011ikkβphosphorylationregulates media b6da7309): Fengyi Wan, Amanda Weaver, Xiaofei Gao, Michael Bern, Philip R Hardwidge, and Michael J Lenardo. Ikkβ phosphorylation regulates rps3 nuclear translocation and nf-κb function during infection with escherichia coli strain o157:h7. Mar 2011. URL: https://doi.org/10.1038/ni.2007, doi:10.1038/ni.2007. This article has 170 citations and is from a highest quality peer-reviewed journal.

23. (wan2011ikkβphosphorylationregulates media de8959ff): Fengyi Wan, Amanda Weaver, Xiaofei Gao, Michael Bern, Philip R Hardwidge, and Michael J Lenardo. Ikkβ phosphorylation regulates rps3 nuclear translocation and nf-κb function during infection with escherichia coli strain o157:h7. Mar 2011. URL: https://doi.org/10.1038/ni.2007, doi:10.1038/ni.2007. This article has 170 citations and is from a highest quality peer-reviewed journal.

24. (wan2011ikkβphosphorylationregulates media 799fbec1): Fengyi Wan, Amanda Weaver, Xiaofei Gao, Michael Bern, Philip R Hardwidge, and Michael J Lenardo. Ikkβ phosphorylation regulates rps3 nuclear translocation and nf-κb function during infection with escherichia coli strain o157:h7. Mar 2011. URL: https://doi.org/10.1038/ni.2007, doi:10.1038/ni.2007. This article has 170 citations and is from a highest quality peer-reviewed journal.

## Citations

1. tong2024proteomicsshowsthat pages 3-5
2. zeng2023spatiallyresolvedsinglecell pages 3-5
3. lim2002completegenomicstructure pages 7-7
4. wan2010thenuclearsignaling pages 1-2
5. rahim2018globalinteractomicsconnect pages 11-12
6. tan2019theinteractomeof pages 13-15
7. dionne2018characterizationofzinc pages 26-29
8. tong2024proteomicsshowsthat pages 5-7
9. gorski2025insightsintosynaptic pages 71-74
10. zeng2023spatiallyresolvedsinglecell pages 13-18
11. dionne2018characterizationofzinc pages 10-15
12. https://doi.org/10.1038/ni.2007
13. https://doi.org/10.1038/s41598-024-58967-y
14. https://doi.org/10.1126/science.add3067
15. https://doi.org/10.1016/S0014-5793(04
16. https://doi.org/10.1016/S0378-1119(02
17. https://doi.org/10.1038/cr.2009.137
18. https://doi.org/10.3389/fmicb.2011.00137
19. https://doi.org/10.1016/j.molcel.2011.10.021
20. https://doi.org/10.3390/v10120731
21. https://doi.org/10.21203/rs.2.12355/v1
22. https://doi.org/10.3389/fmicb.2011.00137,
23. https://doi.org/10.1038/ni.2007,
24. https://doi.org/10.21203/rs.2.12355/v1,
25. https://doi.org/10.1038/s41598-024-58967-y,
26. https://doi.org/10.1126/science.add3067,
27. https://doi.org/10.1016/s0014-5793(04
28. https://doi.org/10.1016/s0378-1119(02
29. https://doi.org/10.1038/cr.2009.137,
30. https://doi.org/10.3390/v10120731,