---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-13T02:19:54.393011'
end_time: '2026-05-13T02:36:08.790916'
duration_seconds: 974.4
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 29
---

## Question

GO annotation research for Saccharomyces cerevisiae GCN5/ADA4/SWI9 (UniProt Q03330). Focus on GO evidence for histone acetyltransferase activity, histone H3/H2B lysine acetylation, histone crotonyltransferase/crotonylation if supported, SAGA/ADA/SLIK histone acetyltransferase complexes, chromatin organization/remodeling, positive regulation of RNA polymerase II transcription through chromatin modification, bromodomain/acetyl-lysine binding if directly supported, and nuclear localization. Identify over-broad or non-core terms such as generic protein binding, DNA-templated transcription, cytoplasm, stress or unrelated phenotypes. Include PMID/DOI citations. Under 1200 words.

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

GO annotation research for Saccharomyces cerevisiae GCN5/ADA4/SWI9 (UniProt Q03330). Focus on GO evidence for histone acetyltransferase activity, histone H3/H2B lysine acetylation, histone crotonyltransferase/crotonylation if supported, SAGA/ADA/SLIK histone acetyltransferase complexes, chromatin organization/remodeling, positive regulation of RNA polymerase II transcription through chromatin modification, bromodomain/acetyl-lysine binding if directly supported, and nuclear localization. Identify over-broad or non-core terms such as generic protein binding, DNA-templated transcription, cytoplasm, stress or unrelated phenotypes. Include PMID/DOI citations. Under 1200 words.

## GO annotation research report: *Saccharomyces cerevisiae* Gcn5/Ada4/Swi9 (UniProt Q03330)

### 1) Key concepts and definitions (current understanding)
**GCN5/Ada4 is a lysine acetyltransferase (KAT/HAT).** In yeast, Gcn5 is the catalytic histone acetyltransferase subunit in the SAGA coactivator and in the related ADA subcomplex; incorporation into multisubunit complexes potentiates nucleosomal acetylation versus recombinant Gcn5 alone. This underpins GO **molecular function** terms such as *histone acetyltransferase activity* and **cellular component** terms for SAGA/ADA membership. Primary biochemical evidence shows that native Ada and SAGA complexes acetylate nucleosomal histones in an acetyl‑CoA-dependent manner and that this activity is Gcn5-dependent (lost in gcn5Δ or HAT-dead mutants). (grant1999expandedlysineacetylation pages 2-4)

**Histone tail lysines as substrates (H3-centric).** Gcn5-containing complexes show a strong preference for histone H3 lysines, with H3K14 a dominant site and broader site usage (e.g., H3K9/K18/K23) when in complexes. (grant1999expandedlysineacetylation pages 1-2, cieniewicz2014thebromodomainof pages 3-6)

**SAGA/ADA/SLIK as transcriptional chromatin-modifying coactivators.** Gcn5 is described as the HAT subunit of SAGA, acting in promoter nucleosome eviction/PIC assembly and transcriptional activation, supporting GO biological process terms like *positive regulation of transcription by RNA polymerase II through chromatin modification* and *chromatin organization*. (zheng2023differentialrequirementsfor pages 1-2)

**Bromodomain as an acetyl-lysine “reader” module.** Yeast Gcn5 contains an acetyl-lysine binding bromodomain that modulates enzymatic site specificity and likely promoter chromatin engagement, supporting GO MF terms related to acetyl-lysine binding where directly supported. (cieniewicz2014thebromodomainof pages 1-2)

### 2) GO-relevant evidence for requested functions/complexes

#### A. Histone acetyltransferase activity (core GO MF)
Grant et al. purified Ada and SAGA fractions and demonstrated robust nucleosomal HAT activity requiring Gcn5: activity is present in WT complexes but lost when complexes are purified from gcn5Δ strains or from strains with a catalytically defective Gcn5 allele (KQL), while a catalytically competent allele (LKN) retains activity. (1999-02; J Biol Chem; DOI:10.1074/jbc.274.9.5895; https://doi.org/10.1074/jbc.274.9.5895) (grant1999expandedlysineacetylation pages 2-4)

#### B. Histone H3 lysine acetylation (core GO MF/BP: “histone H3 acetylation”)
**Site specificity and quantitative residue preferences.** Cieniewicz et al. used an in vitro ADA subcomplex (Gcn5-Ada2-Ada3) assay combined with acid-urea gel separation and quantitative MS to show that ADA targets up to six N-terminal H3 lysines (H3K9, H3K14, H3K18, H3K23, H3K27, H3K36), with H3K14 near-saturating early in the reaction and ordered progression to other sites. (2014-11; Mol Cell Proteomics; DOI:10.1074/mcp.M114.038174; https://doi.org/10.1074/mcp.M114.038174) (cieniewicz2014thebromodomainof pages 3-6, cieniewicz2014thebromodomainof media eb2d9a97, cieniewicz2014thebromodomainof media e0c89de4)

Grant et al. similarly reported that recombinant Gcn5 is H3K14-biased, while native Ada/SAGA complexes acetylate additional H3 sites, including H3K9/K18 recognition by site-specific antisera in both free-histone and nucleosomal contexts. (grant1999expandedlysineacetylation pages 2-4)

#### C. Histone H2B acetylation (requested; evidence scope/limits)
Within the retrieved corpus, **direct primary residue-level mapping for yeast H2B acetylation by Gcn5** was not available as a full primary-text snippet. However, an authoritative review (Baker & Grant) states that yeast SAGA preferentially acetylates multiple lysines on the N-terminal tails of histones **H3 and H2B**, consistent with GO BP/MF annotations for nucleosomal histone acetylation beyond H3. (2007-08; Oncogene; DOI:10.1038/sj.onc.1210603; https://doi.org/10.1038/sj.onc.1210603) (baker2007thesagacontinues pages 1-2)

#### D. SAGA / ADA / SLIK complex membership (core GO CC)
- **SAGA and ADA:** Grant et al. experimentally purify and assay Ada and SAGA activities and show Gcn5 dependence, supporting CC annotations for these complexes. (grant1999expandedlysineacetylation pages 2-4)
- **ADA subcomplex organization:** Cieniewicz et al. explicitly frame Gcn5 as associating with Ada2 and Ada3 to form the ADA catalytic module used for mechanistic assays. (cieniewicz2014thebromodomainof pages 1-2, cieniewicz2014thebromodomainof pages 3-6)
- **SLIK:** A recent review emphasizes that yeast Gcn5 functions in SAGA, SLIK, and ADA, supporting curated CC assignment for SLIK, though not providing distinct functional specificity in the excerpt. (2022-09; PLOS Genet; DOI:10.1371/journal.pgen.1010352; https://doi.org/10.1371/journal.pgen.1010352) (ononye2022posttranslationalregulationof pages 1-3)

#### E. Chromatin organization/remodeling and Pol II transcription activation via chromatin modification (core GO BP)
A recent yeast-focused study (Zheng et al., 2023) reports that **Gcn5 (SAGA HAT subunit) stimulates promoter nucleosome eviction**, contributes to TBP recruitment/PIC assembly, and stimulates transcription—particularly in starvation-induced gene programs—supporting GO BP terms including chromatin remodeling/organization coupled to Pol II transcription. (Published online 2023-03-02; Nucleic Acids Res; DOI:10.1093/nar/gkad099; https://doi.org/10.1093/nar/gkad099) (zheng2023differentialrequirementsfor pages 1-2)

#### F. Bromodomain / acetyl-lysine binding (requested; directly supported)
Cieniewicz et al. state that Gcn5 contains an **acetyl-lysine binding bromodomain** and show that bromodomain-defective ADA complexes exhibit altered H3 site specificity (notably diminished H3K18ac), providing direct support for acetyl-lysine reader/binding functionality affecting enzymatic output. (cieniewicz2014thebromodomainof pages 1-2, cieniewicz2014thebromodomainof pages 3-6)

#### G. Histone crotonyltransferase / histone crotonylation (requested; supported)
Kollenstart et al. provide **direct biochemical and in vivo** evidence that yeast Gcn5 (in the ADA complex) functions as a histone crotonyltransferase:
- **In vitro:** purified Gcn5-Ada2-Ada3 crotonylates H3 at K9/K14/K18/K23/K27 (MS-mapped; antibody-supported). (kollenstart2019gcn5andesa1 pages 2-3, kollenstart2019gcn5andesa1 pages 1-2)
- **In vivo:** crotonate supplementation increases histone crotonylation with dependence on Gcn5, and crotonate triggers a Gcn5/Esa1-dependent transcriptional response (RNA-seq reports 880 differentially expressed transcripts after crotonate treatment). (2019-12; J Biol Chem; DOI:10.1074/jbc.RA119.010302; https://doi.org/10.1074/jbc.RA119.010302) (kollenstart2019gcn5andesa1 pages 4-5, kollenstart2019gcn5andesa1 pages 3-4)

### 3) Nuclear localization (requested; direct evidence and caveats)
A yeast GFP-fusion localization study of Gcn5 reports that the fusion signal is **“certainly nuclear”**, while also showing additional speckled cytoplasmic signal compatible with mitochondrial localization; thus **nuclear localization is directly supported**, but localization may be context-dependent. (2019-02; Biology Open; DOI:10.1242/bio.041244; https://doi.org/10.1242/bio.041244) (montanari2019gcn5histoneacetyltransferase pages 2-3)

### 4) Recent developments (prioritizing 2023–2024)
- **Mechanistic transcription/chromatin work in yeast (2023):** Gcn5 vs NuA4 interplay in promoter nucleosome eviction and transcription across starvation-induced vs basal transcriptomes. (Zheng et al., 2023) (zheng2023differentialrequirementsfor pages 1-2)
- **Systems-level physiology/aging (2023):** Gcn5 modulates starvation-induced stress and metabolic regulons and shows antagonistic pleiotropy in chronological aging, which can influence broad GO biological process assignments if not constrained to chromatin-mediated mechanisms. (Li et al., 2023-10; Aging (Albany NY); DOI:10.18632/aging.205109; https://doi.org/10.18632/aging.205109) (li2023thesaccharomycescerevisiae pages 1-2)

For crotonylation specifically, the strongest yeast mechanistic evidence in this corpus remains the 2019 primary study; 2023–2024 sources retrieved here are largely general or non-yeast focused and do not extend yeast-specific site mapping beyond that anchor. (kollenstart2019gcn5andesa1 pages 2-3)

### 5) Applications and real-world implementations
**Experimental implementations in yeast functional genomics and chromatin biology** include: (i) using gcn5Δ/HAT-dead alleles to test causality of promoter nucleosome eviction and transcriptional activation programs (starvation-induced regulons), and (ii) using crotonate supplementation to probe metabolite-to-chromatin signaling via histone crotonylation. (zheng2023differentialrequirementsfor pages 1-2, kollenstart2019gcn5andesa1 pages 4-5)

### 6) Non-core / over-broad GO terms to flag (with rationale)
Certain annotations are often technically true but **non-specific** for interpreting Gcn5’s core function:
- **“Protein binding”**: Gcn5 functions largely via multisubunit complexes (SAGA/ADA/SLIK) and pleiotropic interaction networks; generic binding terms add little mechanistic resolution. (ononye2022posttranslationalregulationof pages 1-3, baker2007thesagacontinues pages 1-2)
- **Over-broad transcription terms** (e.g., “DNA-templated transcription” without chromatin context): the best-supported role is *coactivation via chromatin modification/nucleosome eviction*, not generic basal transcription. (zheng2023differentialrequirementsfor pages 1-2)
- **Cytoplasm/mitochondrion localization**: a study reports mitoplast-associated Gcn5 and mtDNA/respiration phenotypes, but these are less central than the canonical nuclear chromatin role and may be strain/condition dependent; annotate carefully and prefer evidence-coded CC terms (nucleus/chromatin) when summarizing canonical function. (montanari2019gcn5histoneacetyltransferase pages 1-2, montanari2019gcn5histoneacetyltransferase pages 2-3)
- **Stress response phenotypes**: starvation/stress regulon changes and pleiotropic genetic interactions (including SAGA/SLIK-associated factors) can drive broad “response to stress” terms; these should be tied back to transcription via chromatin modification when possible. (li2023thesaccharomycescerevisiae pages 1-2, hoke2008systematicgeneticarray pages 1-2)

### Evidence summary table
| GO aspect (MF/BP/CC) | Term/theme | Key evidence | Primary source (year) | DOI + URL | Context citation id |
|---|---|---|---|---|---|
| MF | Histone acetyltransferase activity | Purified recombinant and native Gcn5-containing complexes catalyze acetyl-CoA-dependent histone acetylation, and loss or catalytic mutation of Gcn5 abolishes nucleosomal HAT activity. | Grant et al. (1999) | 10.1074/jbc.274.9.5895; https://doi.org/10.1074/jbc.274.9.5895 | (grant1999expandedlysineacetylation pages 2-4) |
| MF | Histone H3 lysine acetylation | ADA/Gcn5 acetylates multiple H3 lysines with strong preference for H3K14 and detectable activity on H3K9, K18, K23, K27, and K36, quantified by acid-urea gel/MS. | Cieniewicz et al. (2014) | 10.1074/mcp.M114.038174; https://doi.org/10.1074/mcp.M114.038174 | (cieniewicz2014thebromodomainof pages 3-6, cieniewicz2014thebromodomainof media eb2d9a97, cieniewicz2014thebromodomainof media e0c89de4) |
| MF | Histone H2B acetylation | Review synthesis states that SAGA preferentially acetylates multiple lysines on histones H3 and H2B, supporting H2B-directed HAT function in native complex context, though exact H2B lysines are not specified in the retrieved primary text. | Baker & Grant (2007) | 10.1038/sj.onc.1210603; https://doi.org/10.1038/sj.onc.1210603 | (baker2007thesagacontinues pages 1-2) |
| MF | Histone crotonyltransferase activity | Purified Gcn5-Ada2-Ada3 (ADA) crotonylates histone H3 in vitro at K9, K14, K18, K23, and K27, and crotonate-induced H3 crotonylation/transcriptional responses depend on Gcn5 in vivo. | Kollenstart et al. (2019) | 10.1074/jbc.RA119.010302; https://doi.org/10.1074/jbc.RA119.010302 | (kollenstart2019gcn5andesa1 pages 2-3, kollenstart2019gcn5andesa1 pages 1-2, kollenstart2019gcn5andesa1 pages 4-5, kollenstart2019gcn5andesa1 pages 3-4) |
| MF | Bromodomain / acetyl-lysine binding | Gcn5 contains an acetyl-lysine-binding bromodomain, and bromodomain-defective ADA complexes show altered H3 site specificity, especially reduced H3K18ac. | Cieniewicz et al. (2014) | 10.1074/mcp.M114.038174; https://doi.org/10.1074/mcp.M114.038174 | (cieniewicz2014thebromodomainof pages 1-2, cieniewicz2014thebromodomainof pages 3-6) |
| CC | SAGA complex membership | Gcn5/Ada4 is the catalytic HAT subunit of SAGA, and purified SAGA fractions show Gcn5-dependent nucleosomal acetylation. | Grant et al. (1999) | 10.1074/jbc.274.9.5895; https://doi.org/10.1074/jbc.274.9.5895 | (grant1999expandedlysineacetylation pages 1-2, grant1999expandedlysineacetylation pages 1-1, grant1999expandedlysineacetylation pages 2-4) |
| CC | ADA complex membership | Gcn5 associates with Ada2 and Ada3 in the ADA subcomplex/minimal HAT module required for robust physiological H3 acetylation. | Cieniewicz et al. (2014) | 10.1074/mcp.M114.038174; https://doi.org/10.1074/mcp.M114.038174 | (cieniewicz2014thebromodomainof pages 1-2, cieniewicz2014thebromodomainof pages 3-6) |
| CC | SLIK complex membership | Review evidence places Gcn5 in the related SLIK complex alongside SAGA/ADA, supporting curated complex membership but not a distinct catalytic specificity in the retrieved primary excerpts. | Ononye & Downey (2022) | 10.1371/journal.pgen.1010352; https://doi.org/10.1371/journal.pgen.1010352 | (ononye2022posttranslationalregulationof pages 1-3) |
| BP | Positive regulation of RNA polymerase II transcription through chromatin modification | Gcn5/SAGA stimulates promoter nucleosome eviction, TBP/PIC recruitment, and transcription of starvation-induced genes, indicating direct coactivator function via chromatin acetylation. | Zheng et al. (2023) | 10.1093/nar/gkad099; https://doi.org/10.1093/nar/gkad099 | (zheng2023differentialrequirementsfor pages 1-2) |
| BP | Chromatin organization / remodeling | Gcn5 acts with remodelers to evict and reposition promoter nucleosomes, linking its HAT activity to chromatin organization at active genes. | Zheng et al. (2023) | 10.1093/nar/gkad099; https://doi.org/10.1093/nar/gkad099 | (zheng2023differentialrequirementsfor pages 1-2) |
| CC | Nuclear/chromatin-associated localization | The strongest retrieved evidence places Gcn5 in nuclear chromatin coactivator complexes (ADA/SAGA/SLIK) rather than relying on generic compartment terms. | Baker & Grant (2007) | 10.1038/sj.onc.1210603; https://doi.org/10.1038/sj.onc.1210603 | (baker2007thesagacontinues pages 1-2) |
| Caveat | Mitochondrial/pleiotropy caveat (non-core for GO summary) | A later study reports mitoplast-associated Gcn5 and mtDNA/respiration phenotypes, but these appear pleiotropic and are less central than the well-established nuclear HAT/coactivator role. | Montanari et al. (2019) | 10.1242/bio.041244; https://doi.org/10.1242/bio.041244 | (montanari2019gcn5histoneacetyltransferase pages 1-2, montanari2019gcn5histoneacetyltransferase pages 2-3) |
| Caveat | Over-broad terms to treat cautiously | Broad annotations such as generic protein binding, DNA-templated transcription, stress response, or cytoplasmic/mitochondrial localization can arise from complex membership and pleiotropic phenotypes rather than direct core molecular function. | Li et al. (2023); Ononye & Downey (2022) | 10.18632/aging.205109; https://doi.org/10.18632/aging.205109; 10.1371/journal.pgen.1010352; https://doi.org/10.1371/journal.pgen.1010352 | (li2023thesaccharomycescerevisiae pages 1-2, ononye2022posttranslationalregulationof pages 1-3, ononye2022posttranslationalregulationof pages 4-5) |


*Table: This table maps the main GO-relevant functions and locations requested for S. cerevisiae Gcn5/ADA4 to the strongest supporting evidence found in the retrieved literature. It also flags broader or potentially non-core themes that should be interpreted cautiously during GO curation.*

References

1. (grant1999expandedlysineacetylation pages 2-4): Patrick A. Grant, Anton Eberharter, Sam John, Richard G. Cook, Bryan M. Turner, and Jerry L. Workman. Expanded lysine acetylation specificity of gcn5 in native complexes*. The Journal of Biological Chemistry, 274:5895-5900, Feb 1999. URL: https://doi.org/10.1074/jbc.274.9.5895, doi:10.1074/jbc.274.9.5895. This article has 488 citations.

2. (grant1999expandedlysineacetylation pages 1-2): Patrick A. Grant, Anton Eberharter, Sam John, Richard G. Cook, Bryan M. Turner, and Jerry L. Workman. Expanded lysine acetylation specificity of gcn5 in native complexes*. The Journal of Biological Chemistry, 274:5895-5900, Feb 1999. URL: https://doi.org/10.1074/jbc.274.9.5895, doi:10.1074/jbc.274.9.5895. This article has 488 citations.

3. (cieniewicz2014thebromodomainof pages 3-6): Anne M. Cieniewicz, Linley Moreland, Alison E. Ringel, Samuel G. Mackintosh, Ana Raman, Tonya M. Gilbert, Cynthia Wolberger, Alan J. Tackett, and Sean D. Taverna. The bromodomain of gcn5 regulates site specificity of lysine acetylation on histone h3. Molecular &amp; Cellular Proteomics, 13:2896-2910, Nov 2014. URL: https://doi.org/10.1074/mcp.m114.038174, doi:10.1074/mcp.m114.038174. This article has 108 citations and is from a domain leading peer-reviewed journal.

4. (zheng2023differentialrequirementsfor pages 1-2): Qiaoyun Zheng, Hongfang Qiu, Hongen Zhang, and Alan G Hinnebusch. Differential requirements for gcn5 and nua4 hat activities in the starvation-induced versus basal transcriptomes. Nucleic acids research, 51:3696-3721, Mar 2023. URL: https://doi.org/10.1093/nar/gkad099, doi:10.1093/nar/gkad099. This article has 9 citations and is from a highest quality peer-reviewed journal.

5. (cieniewicz2014thebromodomainof pages 1-2): Anne M. Cieniewicz, Linley Moreland, Alison E. Ringel, Samuel G. Mackintosh, Ana Raman, Tonya M. Gilbert, Cynthia Wolberger, Alan J. Tackett, and Sean D. Taverna. The bromodomain of gcn5 regulates site specificity of lysine acetylation on histone h3. Molecular &amp; Cellular Proteomics, 13:2896-2910, Nov 2014. URL: https://doi.org/10.1074/mcp.m114.038174, doi:10.1074/mcp.m114.038174. This article has 108 citations and is from a domain leading peer-reviewed journal.

6. (cieniewicz2014thebromodomainof media eb2d9a97): Anne M. Cieniewicz, Linley Moreland, Alison E. Ringel, Samuel G. Mackintosh, Ana Raman, Tonya M. Gilbert, Cynthia Wolberger, Alan J. Tackett, and Sean D. Taverna. The bromodomain of gcn5 regulates site specificity of lysine acetylation on histone h3. Molecular &amp; Cellular Proteomics, 13:2896-2910, Nov 2014. URL: https://doi.org/10.1074/mcp.m114.038174, doi:10.1074/mcp.m114.038174. This article has 108 citations and is from a domain leading peer-reviewed journal.

7. (cieniewicz2014thebromodomainof media e0c89de4): Anne M. Cieniewicz, Linley Moreland, Alison E. Ringel, Samuel G. Mackintosh, Ana Raman, Tonya M. Gilbert, Cynthia Wolberger, Alan J. Tackett, and Sean D. Taverna. The bromodomain of gcn5 regulates site specificity of lysine acetylation on histone h3. Molecular &amp; Cellular Proteomics, 13:2896-2910, Nov 2014. URL: https://doi.org/10.1074/mcp.m114.038174, doi:10.1074/mcp.m114.038174. This article has 108 citations and is from a domain leading peer-reviewed journal.

8. (baker2007thesagacontinues pages 1-2): S P Baker and P A Grant. The saga continues: expanding the cellular role of a transcriptional co-activator complex. Oncogene, 26:5329-5340, Aug 2007. URL: https://doi.org/10.1038/sj.onc.1210603, doi:10.1038/sj.onc.1210603. This article has 288 citations and is from a domain leading peer-reviewed journal.

9. (ononye2022posttranslationalregulationof pages 1-3): Onyekachi E. Ononye and Michael Downey. Posttranslational regulation of the gcn5 and pcaf acetyltransferases. PLOS Genetics, 18:e1010352, Sep 2022. URL: https://doi.org/10.1371/journal.pgen.1010352, doi:10.1371/journal.pgen.1010352. This article has 13 citations and is from a domain leading peer-reviewed journal.

10. (kollenstart2019gcn5andesa1 pages 2-3): Leonie Kollenstart, Anton J.L. de Groot, George M.C. Janssen, Xue Cheng, Kees Vreeken, Fabrizio Martino, Jacques Côté, Peter A. van Veelen, and Haico van Attikum. Gcn5 and esa1 function as histone crotonyltransferases to regulate crotonylation-dependent transcription. Journal of Biological Chemistry, 294:20122-20134, Dec 2019. URL: https://doi.org/10.1074/jbc.ra119.010302, doi:10.1074/jbc.ra119.010302. This article has 99 citations and is from a domain leading peer-reviewed journal.

11. (kollenstart2019gcn5andesa1 pages 1-2): Leonie Kollenstart, Anton J.L. de Groot, George M.C. Janssen, Xue Cheng, Kees Vreeken, Fabrizio Martino, Jacques Côté, Peter A. van Veelen, and Haico van Attikum. Gcn5 and esa1 function as histone crotonyltransferases to regulate crotonylation-dependent transcription. Journal of Biological Chemistry, 294:20122-20134, Dec 2019. URL: https://doi.org/10.1074/jbc.ra119.010302, doi:10.1074/jbc.ra119.010302. This article has 99 citations and is from a domain leading peer-reviewed journal.

12. (kollenstart2019gcn5andesa1 pages 4-5): Leonie Kollenstart, Anton J.L. de Groot, George M.C. Janssen, Xue Cheng, Kees Vreeken, Fabrizio Martino, Jacques Côté, Peter A. van Veelen, and Haico van Attikum. Gcn5 and esa1 function as histone crotonyltransferases to regulate crotonylation-dependent transcription. Journal of Biological Chemistry, 294:20122-20134, Dec 2019. URL: https://doi.org/10.1074/jbc.ra119.010302, doi:10.1074/jbc.ra119.010302. This article has 99 citations and is from a domain leading peer-reviewed journal.

13. (kollenstart2019gcn5andesa1 pages 3-4): Leonie Kollenstart, Anton J.L. de Groot, George M.C. Janssen, Xue Cheng, Kees Vreeken, Fabrizio Martino, Jacques Côté, Peter A. van Veelen, and Haico van Attikum. Gcn5 and esa1 function as histone crotonyltransferases to regulate crotonylation-dependent transcription. Journal of Biological Chemistry, 294:20122-20134, Dec 2019. URL: https://doi.org/10.1074/jbc.ra119.010302, doi:10.1074/jbc.ra119.010302. This article has 99 citations and is from a domain leading peer-reviewed journal.

14. (montanari2019gcn5histoneacetyltransferase pages 2-3): Arianna Montanari, Manuela Leo, Veronica De Luca, Patrizia Filetici, and Silvia Francisci. Gcn5 histone acetyltransferase is present in the mitoplasts. Biology Open, Feb 2019. URL: https://doi.org/10.1242/bio.041244, doi:10.1242/bio.041244. This article has 19 citations and is from a peer-reviewed journal.

15. (li2023thesaccharomycescerevisiae pages 1-2): Kaiqiang Li, Gabriele Mocciaro, Jules L. Griffin, and Nianshu Zhang. The saccharomyces cerevisiae acetyltransferase gcn5 exerts antagonistic pleiotropic effects on chronological ageing. Aging (Albany NY), 15:10915-10937, Oct 2023. URL: https://doi.org/10.18632/aging.205109, doi:10.18632/aging.205109. This article has 3 citations.

16. (montanari2019gcn5histoneacetyltransferase pages 1-2): Arianna Montanari, Manuela Leo, Veronica De Luca, Patrizia Filetici, and Silvia Francisci. Gcn5 histone acetyltransferase is present in the mitoplasts. Biology Open, Feb 2019. URL: https://doi.org/10.1242/bio.041244, doi:10.1242/bio.041244. This article has 19 citations and is from a peer-reviewed journal.

17. (hoke2008systematicgeneticarray pages 1-2): Stephen MT Hoke, Julie Guzzo, Brenda Andrews, and Christopher J Brandl. Systematic genetic array analysis links the saccharomyces cerevisiae saga/slik and nua4 component tra1 to multiple cellular processes. BMC Genetics, 9:46-46, Jul 2008. URL: https://doi.org/10.1186/1471-2156-9-46, doi:10.1186/1471-2156-9-46. This article has 34 citations.

18. (grant1999expandedlysineacetylation pages 1-1): Patrick A. Grant, Anton Eberharter, Sam John, Richard G. Cook, Bryan M. Turner, and Jerry L. Workman. Expanded lysine acetylation specificity of gcn5 in native complexes*. The Journal of Biological Chemistry, 274:5895-5900, Feb 1999. URL: https://doi.org/10.1074/jbc.274.9.5895, doi:10.1074/jbc.274.9.5895. This article has 488 citations.

19. (ononye2022posttranslationalregulationof pages 4-5): Onyekachi E. Ononye and Michael Downey. Posttranslational regulation of the gcn5 and pcaf acetyltransferases. PLOS Genetics, 18:e1010352, Sep 2022. URL: https://doi.org/10.1371/journal.pgen.1010352, doi:10.1371/journal.pgen.1010352. This article has 13 citations and is from a domain leading peer-reviewed journal.

## Citations

1. grant1999expandedlysineacetylation pages 2-4
2. zheng2023differentialrequirementsfor pages 1-2
3. cieniewicz2014thebromodomainof pages 1-2
4. baker2007thesagacontinues pages 1-2
5. ononye2022posttranslationalregulationof pages 1-3
6. li2023thesaccharomycescerevisiae pages 1-2
7. grant1999expandedlysineacetylation pages 1-2
8. cieniewicz2014thebromodomainof pages 3-6
9. hoke2008systematicgeneticarray pages 1-2
10. grant1999expandedlysineacetylation pages 1-1
11. ononye2022posttranslationalregulationof pages 4-5
12. https://doi.org/10.1074/jbc.274.9.5895
13. https://doi.org/10.1074/mcp.M114.038174
14. https://doi.org/10.1038/sj.onc.1210603
15. https://doi.org/10.1371/journal.pgen.1010352
16. https://doi.org/10.1093/nar/gkad099
17. https://doi.org/10.1074/jbc.RA119.010302
18. https://doi.org/10.1242/bio.041244
19. https://doi.org/10.18632/aging.205109
20. https://doi.org/10.18632/aging.205109;
21. https://doi.org/10.1074/jbc.274.9.5895,
22. https://doi.org/10.1074/mcp.m114.038174,
23. https://doi.org/10.1093/nar/gkad099,
24. https://doi.org/10.1038/sj.onc.1210603,
25. https://doi.org/10.1371/journal.pgen.1010352,
26. https://doi.org/10.1074/jbc.ra119.010302,
27. https://doi.org/10.1242/bio.041244,
28. https://doi.org/10.18632/aging.205109,
29. https://doi.org/10.1186/1471-2156-9-46,