---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-13T04:17:30.708267'
end_time: '2026-05-13T04:32:34.906757'
duration_seconds: 904.2
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 24
---

## Question

GO annotation research for Saccharomyces cerevisiae HSC82 (UniProt P15108), the constitutive Hsp90 isoform. Focus on GO evidence for core functions: ATP-dependent protein folding chaperone activity, ATP binding and ATP hydrolysis linked to the Hsp90 conformational cycle, Hsp90 homodimer/heterodimer and co-chaperone/client complexes, cytosolic localization, protein folding, protein stabilization, heat stress/elevated-temperature growth, and client maturation/regulation including calcineurin/CNA2 and signaling/cell-cycle clients. Evaluate non-core or questionable annotations: plasma membrane, perinuclear region, mitochondrion, generic protein-containing complex, generic nucleotide binding, unfolded protein binding versus ATP-dependent protein folding chaperone, box C/D snoRNP assembly/R2TP, kinetochore assembly/SGT1, and broad stress-response terms. Distinguish HSC82 from inducible HSP82 where relevant. Include PMID/DOI citations and keep under 1200 words.

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

GO annotation research for Saccharomyces cerevisiae HSC82 (UniProt P15108), the constitutive Hsp90 isoform. Focus on GO evidence for core functions: ATP-dependent protein folding chaperone activity, ATP binding and ATP hydrolysis linked to the Hsp90 conformational cycle, Hsp90 homodimer/heterodimer and co-chaperone/client complexes, cytosolic localization, protein folding, protein stabilization, heat stress/elevated-temperature growth, and client maturation/regulation including calcineurin/CNA2 and signaling/cell-cycle clients. Evaluate non-core or questionable annotations: plasma membrane, perinuclear region, mitochondrion, generic protein-containing complex, generic nucleotide binding, unfolded protein binding versus ATP-dependent protein folding chaperone, box C/D snoRNP assembly/R2TP, kinetochore assembly/SGT1, and broad stress-response terms. Distinguish HSC82 from inducible HSP82 where relevant. Include PMID/DOI citations and keep under 1200 words.

## Research report: GO annotation evidence for *S. cerevisiae* HSC82 (UniProt P15108)

### 1) Key concepts and definitions (current understanding)
HSC82 encodes the constitutive cytosolic Hsp90 isoform (Hsc82), whereas HSP82 encodes a strongly heat‑inducible isoform (Hsp82); both are ~97% identical but differ measurably in ATPase/conformational properties and stress robustness. (Girstmair et al., 2019‑08, Nat Commun, https://doi.org/10.1038/s41467-019-11518-w) (girstmair2019thehsp90isoforms pages 1-2)

Gene Ontology (GO) annotations are evidence-backed statements linking a gene product to a specific molecular function (MF), biological process (BP), or cellular component (CC); complete functional descriptions require multiple GO annotations, and annotations are updated as ontology terms/gene sets/guidelines change. (Aleksander et al., 2025‑12, NAR “GO knowledgebase in 2026”, https://doi.org/10.1093/nar/gkaf1292) (g2026thegeneontology pages 1-2)

SGD is a primary yeast annotation source and (i) manually curates yeast literature and pathways, and (ii) exports curated pathway knowledge through Noctua/GO‑CAM workflows to generate GO annotations. (Engel et al., posted 2024‑09‑20; bioRxiv 2025 listing; https://doi.org/10.1101/2024.09.16.613348) (engel2025saccharomycesgenomedatabase pages 5-7)

### 2) Core GO-relevant functions for Hsc82 (supported annotations)
**ATP binding and ATPase-driven conformational cycle (MF).** Yeast Hsp90 undergoes nucleotide-dependent conformational changes: ATP binding drives lid closure and N‑terminal association (“molecular clamp”) and ATP hydrolysis is coupled to cycle progression; cochaperones tune these steps. (Johnson et al., 2007‑01, Mol Cell Biol, https://doi.org/10.1128/mcb.01034-06) (johnson2007nucleotidedependentinteractionof pages 1-2). Isoform comparison shows Hsc82 ATPase activity is higher than Hsp82 (~1.3× at 30 °C; ~1.6× at 37 °C), with only slight ATP-binding affinity differences. (Girstmair et al., 2019‑08) (girstmair2019thehsp90isoforms pages 2-4, girstmair2019thehsp90isoforms media 03f98d7e)

**ATP-dependent protein folding chaperone activity and client maturation (MF/BP).** Hsp90/Hsc82 functions as an ATP-dependent folding chaperone for late intermediates/clients, and specific Hsp90 mutants that disrupt client loading/closing/reopening cause client-specific maturation defects and temperature-sensitive growth. (Hohrman et al., 2021‑01, Genetics, https://doi.org/10.1093/genetics/iyab009) (hohrman2021disruptingprogressionof pages 1-2); (Mercier et al., 2023‑05, PLOS Genet, https://doi.org/10.1371/journal.pgen.1010772) (mercier2023hsp90mutantswith pages 2-4). Single-molecule refolding assays indicate Hsc82 supports client refolding (reported as ~14% full refolding events) but less efficiently than Hsp82, consistent with Hsp82’s stress-optimized role. (Girstmair et al., 2019‑08) (girstmair2019thehsp90isoforms pages 2-4)

**Hsp90 homodimer and cochaperone/client complexes (CC).** Mechanistically, Hsp90 is a homodimer (C‑terminal dimerization) and forms nucleotide-state-specific cochaperone complexes: Sba1 (p23) and Cpr6 preferentially bind the ATP-closed state; Sti1 binds in a nucleotide-independent, loading-competent state and inhibits ATPase/N‑terminal dimerization. (Johnson et al., 2007‑01) (johnson2007nucleotidedependentinteractionof pages 1-2). In isoform comparisons, Aha1 and Cpr6 stimulate ATPase activity of both isoforms, while Cdc37, Sba1/p23, and Sti1 inhibit with only minor isoform-specific differences. (Girstmair et al., 2019‑08) (girstmair2019thehsp90isoforms pages 2-4, girstmair2019thehsp90isoforms media 03f98d7e)

**Cytosolic localization (CC).** Hsc82 is described as the constitutive cytosolic Hsp90 isoform; many experimental Hsc82 interactome/purification studies use cytosolic lysates, consistent with CC:cytosol annotations for both isoforms, with expression-level differences for HSC82 vs HSP82. (Hohrman et al., 2021‑01) (hohrman2021disruptingprogressionof pages 1-2); (Girstmair et al., 2019‑08) (girstmair2019thehsp90isoforms pages 1-2)

**Heat/elevated-temperature growth (BP; phenotype-linked).** Hsp90 mutant collections include alleles (including in Hsc82 backgrounds) with growth at 30 °C but not 37 °C, supporting a role in elevated-temperature fitness. (Hohrman et al., 2021‑01) (hohrman2021disruptingprogressionof pages 1-2). Isoform tuning supports that Hsp82 is more thermally stable/refolds better under stress, whereas Hsc82 is more processive and favors closed states—important for interpreting which “heat response” GO terms should map to HSC82 vs HSP82. (Girstmair et al., 2019‑08) (girstmair2019thehsp90isoforms pages 1-2)

**Client maturation/regulation: calcineurin (Cna2/Cnb1) (BP/MF: client chaperoning).** Recent in vitro work shows direct physical association of Hsc82 with calcineurin components: surface plasmon resonance and crosslinking detect binding between Hsc82 and CNB1 (regulatory subunit). (Heim, 2024) (heim2024characterizationandchaperone pages 99-100). Functional assays show Hsc82 can modulate calcineurin activity in a temperature- and CaM-dependent manner; under heat-stress assay conditions (42 °C), Hsc82 with Ydj1/Ssa1/Sti1 increases calcineurin activity, and preincubation of CNB1 with Hsc82 enhances activity, consistent with chaperone-facilitated subunit assembly under stress. (Heim, 2024) (heim2024characterizationandchaperone pages 104-106). Reviews of Hsp90–calcineurin in fungi summarize physical interaction and that Hsp90 inhibition blocks calcineurin activation, supporting calcineurin as an Hsp90 client (but often without isoform separation in older work). (Singh, 2012) (singh2012therolesof pages 67-72)

**Signaling/cell-cycle clients (BP).** Hsp90 client maturation defects are shown for diverse regulatory clients (e.g., v‑Src and other regulatory proteins assayed across distinct Hsp90 cycle mutants), and kinase client handling is mechanistically supported by Cdc37-dependent loading steps. (Hohrman et al., 2021‑01) (hohrman2021disruptingprogressionof pages 1-2); (Mercier et al., 2023‑05) (mercier2023hsp90mutantswith pages 2-4)

### 3) Recent developments and latest research (prioritizing 2023–2024)
**Cycle-step-resolved client specificity.** 2023 genetics/biochemistry dissected Hsp90 cycle mutants into “loading/closing/reopening” classes with distinct cochaperone dependencies and client phenotypes, refining which mechanistic subfunctions are captured by GO terms that reference ATPase-cycle steps or cochaperone complexes. (Mercier et al., 2023‑05) (mercier2023hsp90mutantswith pages 2-4)

**Calcineurin–Hsc82 biochemistry.** 2024 work provides direct Hsc82 binding to CNB1 and stress-dependent modulation of calcineurin activity/assembly, strengthening a yeast-isoform-specific evidence base (Hsc82 explicitly tested) for calcineurin-client related GO annotations. (Heim, 2024) (heim2024characterizationandchaperone pages 99-100, heim2024characterizationandchaperone pages 104-106)

### 4) Applications and real-world implementations
The Hsp90/Hsc82 cycle is routinely exploited in yeast genetics and chemical biology as a tunable proteostasis node: Hsp90 inhibitors or cycle mutants are used to perturb client maturation and to map which cellular pathways (e.g., calcineurin-mediated stress circuits) depend on chaperoning. This is a practical basis for using yeast HSC82 alleles as tools to interrogate signaling and stress physiology. (Hohrman et al., 2021‑01) (hohrman2021disruptingprogressionof pages 1-2); (Singh, 2012) (singh2012therolesof pages 67-72)

### 5) Statistics/data points useful for GO evidence summaries
* Hsc82 ATPase activity is higher than Hsp82 (~1.3× at 30 °C; ~1.6× at 37 °C). (Girstmair et al., 2019‑08) (girstmair2019thehsp90isoforms pages 2-4, girstmair2019thehsp90isoforms media 03f98d7e)
* Single-molecule folding assay: Hsc82 supports full refolding in ~14% of events (lower than Hsp82). (Girstmair et al., 2019‑08) (girstmair2019thehsp90isoforms pages 2-4)

### 6) Non-core/questionable GO annotations (critical evaluation)
* **Plasma membrane / perinuclear region (CC):** No direct localization evidence was found in the retrieved Hsc82 primary sources; such CC terms should be treated as questionable unless supported by dedicated localization experiments for Hsc82 (not just indirect stress phenotypes). (hohrman2021disruptingprogressionof pages 1-2, girstmair2019thehsp90isoforms pages 1-2)
* **Mitochondrion (CC):** Reviews discuss broader Hsp90 network connections to organelles and mitochondrial-related processes, but this is not equivalent to demonstrating stable mitochondrial localization of Hsc82; annotate only if supported by direct localization/targeting data. (rizzolo2014theinteractionnetwork pages 1-4)
* **Unfolded protein binding (MF) vs ATP-dependent folding chaperone (MF):** Hsp90/Hsc82 is better captured by ATP-dependent chaperone cycle terms; mechanistic descriptions emphasize action on partially folded/late intermediates and cochaperone-regulated cycle steps rather than generic unfolded-substrate binding. (girstmair2019thehsp90isoforms pages 1-2, rizzolo2014theinteractionnetwork pages 1-4)
* **Generic nucleotide binding (MF):** Technically true but far less specific than ATP binding/ATPase cycle terms; GO should prefer ATP-focused terms with mechanistic support. (johnson2007nucleotidedependentinteractionof pages 1-2, girstmair2019thehsp90isoforms pages 2-4)
* **Generic protein-containing complex (CC):** Hsc82 participates in many complexes; GO is more informative when annotating specific complexes (e.g., Hsp90–Sti1, Hsp90–Sba1, Hsp90–Cdc37) supported by nucleotide-state-specific binding evidence. (johnson2007nucleotidedependentinteractionof pages 1-2, girstmair2019thehsp90isoforms pages 2-4)
* **R2TP/box C/D snoRNP assembly (BP):** Mentioned in network reviews as part of broader Hsp90 interactomes, but direct Hsc82-specific experimental evidence was not identified in the retrieved set; treat as tentative unless backed by primary yeast experiments tied to Hsc82. (rizzolo2014theinteractionnetwork pages 1-4)
* **Kinetochore assembly/SGT1 (BP/CC):** Sgt1 is cataloged as an Hsp90 adaptor/cochaperone in yeast-focused reviews, supporting a plausible link; however, in this evidence set it is primarily review-level rather than direct Hsc82-focused experimental excerpts, so annotation should be constrained to evidence-supported statements (and ideally cite yeast primary work explicitly). (verghese2012biologyofthe pages 13-13, dodt2020characterizationofthe pages 24-27)
* **Broad stress-response terms (BP):** Because HSC82 is constitutive and HSP82 is heat-inducible, broad “response to stress” annotations risk conflating isoforms; prefer phenotype-anchored terms (e.g., growth at elevated temperature) and client-pathway terms (e.g., calcineurin regulation) where evidence is clear. (girstmair2019thehsp90isoforms pages 1-2, hohrman2021disruptingprogressionof pages 1-2)

### Summary table (core vs questionable)
| GO aspect | Proposed GO term label | Core/questionable | Evidence type | Isoform specificity | Key mechanistic note | Citations |
|---|---|---|---|---|---|---|
| MF | ATP binding / Hsp90 ATPase activity | Core | biochemical, structural | Hsc82 (compared with Hsp82) | N-terminal ATP-binding domain; ATP binding drives lid closure and N-terminal association; Hsc82 shows higher ATPase activity than Hsp82 at 30–37°C | (johnson2007nucleotidedependentinteractionof pages 1-2, girstmair2019thehsp90isoforms pages 1-2, girstmair2019thehsp90isoforms pages 2-4, girstmair2019thehsp90isoforms media 03f98d7e) |
| MF | ATP hydrolysis linked to Hsp90 conformational cycle | Core | biochemical, genetic | Hsc82 and both isoforms | Closed/open transitions and reopening steps mapped with Hsc82 mutants; cochaperones tune cycle timing; ATP exchange may suffice for essential in vivo function but hydrolysis remains a regulatory control point | (mercier2023hsp90mutantswith pages 2-4, johnson2007nucleotidedependentinteractionof pages 1-2) |
| MF | ATP-dependent protein folding chaperone activity | Core | biochemical, genetic, review | Hsc82 and both isoforms | Hsp90 acts in an ATP-dependent folding pathway on late folding intermediates/clients; optical-trap assays show Hsc82 supports refolding, though less efficiently than stress-inducible Hsp82 | (hohrman2021disruptingprogressionof pages 1-2, girstmair2019thehsp90isoforms pages 1-2, girstmair2019thehsp90isoforms pages 2-4) |
| BP | Protein folding / protein stabilization / client maturation | Core | genetic, biochemical, review | Hsc82 and both isoforms | Supports stability and activation of diverse clients; proteome analyses and mutant studies show client-specific maturation defects and reduced abundance of client subsets when cycle steps are disrupted | (hohrman2021disruptingprogressionof pages 1-2, mercier2023hsp90mutantswith pages 2-4, verghese2012biologyofthe pages 13-13) |
| CC | Hsp90 homodimer | Core | structural, biochemical | Hsc82 and both isoforms | Constitutive C-terminal dimerization is central to Hsp90 architecture; nucleotide binding promotes transient N-terminal dimerization during the cycle | (dodt2020characterizationofthe pages 24-27, johnson2007nucleotidedependentinteractionof pages 1-2, girstmair2019thehsp90isoforms pages 1-2) |
| CC | Hsp90–Sti1 co-chaperone complex | Core | biochemical, genetic | Hsc82 and both isoforms | Sti1 binds Hsp90 in a nucleotide-independent/client-loading state, inhibits ATPase, and helps transfer clients from Hsp70 to Hsp90 | (hohrman2021disruptingprogressionof pages 1-2, johnson2007nucleotidedependentinteractionof pages 1-2) |
| CC | Hsp90–Sba1/p23 closed-state complex | Core | biochemical | Hsc82 and both isoforms | Sba1 preferentially binds ATP-closed Hsp90 and stabilizes the closed conformation | (mercier2023hsp90mutantswith pages 2-4, johnson2007nucleotidedependentinteractionof pages 1-2, girstmair2019thehsp90isoforms pages 2-4, girstmair2019thehsp90isoforms media 03f98d7e) |
| CC | Hsp90–Cpr6/Cpr7 complex | Core | biochemical, genetic, review | Hsc82 and both isoforms | Cpr6/Cpr7 are TPR immunophilin co-chaperones; Cpr6 stimulates ATPase and favors closed-state progression; Cpr7 has stronger in vivo phenotypic impact | (mercier2023hsp90mutantswith pages 2-4, dodt2020characterizationofthe pages 24-27, johnson2007nucleotidedependentinteractionof pages 1-2, girstmair2019thehsp90isoforms media 03f98d7e) |
| CC | Hsp90–Cdc37 kinase-loading complex | Core | genetic, review | Both / not Hsc82-specific | Cdc37 recruits kinase clients and interfaces with Hsp90 N/M domains; supports signaling and cell-cycle client maturation | (hohrman2021disruptingprogressionof pages 1-2, dodt2020characterizationofthe pages 24-27, verghese2012biologyofthe pages 13-13) |
| CC | Hsp90–Sgt1 complex | Supported but narrower than generic complex | biochemical, genetic, review | Hsc82 emphasized in yeast | Sgt1 is an essential co-chaperone/adaptor; binds Hsc82 and participates in maturation of selected clients and kinetochore-related assemblies | (dodt2020characterizationofthe pages 24-27, verghese2012biologyofthe pages 13-13) |
| CC | Cytosol / cytoplasmic localization | Core | review, experimental context | Hsc82 vs Hsp82 both cytosolic; Hsc82 constitutive | Yeast Hsc82 is the constitutive cytosolic Hsp90 isoform; many assays isolate Hsc82 complexes from cytosolic lysates | (hohrman2021disruptingprogressionof pages 1-2, dodt2020characterizationofthe pages 24-27, girstmair2019thehsp90isoforms pages 1-2) |
| BP | Response to heat / elevated-temperature growth | Core but should be phenotype-linked, not overbroad | genetic, biochemical | Hsc82 vs Hsp82 distinguished | Hsc82 is constitutive, Hsp82 heat-inducible; Hsc82 mutants show 37°C growth defects, while Hsp82 is more thermally stable/refolds better under stress | (hohrman2021disruptingprogressionof pages 1-2, girstmair2019thehsp90isoforms pages 1-2, girstmair2019thehsp90isoforms pages 2-4) |
| BP | Calcineurin/Cna2/Cnb1 maturation or regulation | Core client-related | biochemical, review | Hsc82 supported; often not separated from total Hsp90 in older literature | Direct Hsc82 binding to CNB1 and effects on CNA2/CNB1 complex state/activity support calcineurin as an Hsp90 client/regulatory target | (heim2024characterizationandchaperone pages 99-100, heim2024characterizationandchaperone pages 104-106, singh2012therolesof pages 67-72) |
| BP | Signaling/cell-cycle client maturation | Core | genetic, biochemical, review | Both / often not isoform-specific | Strong support from kinase and regulatory clients such as v-Src, Ssl2, Utp21 and kinase-loading via Cdc37; justified as client maturation rather than broad pathway control | (hohrman2021disruptingprogressionof pages 1-2, mercier2023hsp90mutantswith pages 2-4, verghese2012biologyofthe pages 13-13) |
| CC | Mitochondrion | Questionable/non-core for Hsc82 itself | review only / indirect | Not Hsc82-specific | Some literature discusses cytosolic Hsp90/co-chaperones affecting mitochondrial biogenesis or preprotein handling, but that does not establish stable mitochondrial localization of Hsc82 | (rizzolo2014theinteractionnetwork pages 1-4) |
| CC | Plasma membrane | Questionable | lacking direct support | None | No direct Hsc82 localization evidence in the retrieved sources | (hohrman2021disruptingprogressionof pages 1-2, girstmair2019thehsp90isoforms pages 1-2) |
| CC | Perinuclear region | Questionable | lacking direct support | None | No direct support in retrieved Hsc82 literature | (hohrman2021disruptingprogressionof pages 1-2, girstmair2019thehsp90isoforms pages 1-2) |
| MF | Unfolded protein binding | Questionable / likely too generic | review, mechanistic inference | Both | Hsp90 generally acts on partially folded, late-stage intermediates or near-native clients rather than canonical unfolded substrates; ATP-dependent chaperone term is more precise | (rizzolo2014theinteractionnetwork pages 1-4, girstmair2019thehsp90isoforms pages 1-2) |
| MF | Generic nucleotide binding | Non-core, overly broad | biochemical | Hsc82 | True but much less informative than ATP binding/ATPase activity; GO should prefer the specific ATP-related terms | (johnson2007nucleotidedependentinteractionof pages 1-2, girstmair2019thehsp90isoforms pages 2-4) |
| CC | Generic protein-containing complex | Non-core, overly broad | biochemical, review | Both | Hsc82 forms many complexes, but specific complexes (homodimer; Sti1/Cpr6/Sba1/Cdc37/Sgt1 complexes) are more biologically useful than a generic complex term | (dodt2020characterizationofthe pages 24-27, johnson2007nucleotidedependentinteractionof pages 1-2, verghese2012biologyofthe pages 13-13) |
| BP | Box C/D snoRNP assembly / R2TP | Questionable for Hsc82-specific annotation | review only / indirect | Both, not Hsc82-specific | Hsp90 network reviews mention Tah1/Pih1 (R2TP-like) functions, but direct Hsc82-specific experimental support in the retrieved set is weak | (rizzolo2014theinteractionnetwork pages 1-4) |
| BP | Kinetochore assembly via Sgt1 | Supported but should be qualified | biochemical, genetic | Hsc82 implicated, likely not isoform-exclusive | Yeast studies support Hsc82–Sgt1 involvement in assembly of core kinetochore complexes; suitable only if annotation is tied to specific evidence and not generalized to all Hsp90 functions | (verghese2012biologyofthe pages 13-13) |
| BP | Broad stress-response terms | Questionable if unspecific | genetic, review | Hsc82 vs Hsp82 must be separated | Hsc82 contributes to heat/elevated-temperature fitness and some stress-linked client pathways, but very broad stress-response annotations risk conflating constitutive Hsc82 with inducible Hsp82 | (verghese2012biologyofthe pages 13-13, girstmair2019thehsp90isoforms pages 1-2, girstmair2019thehsp90isoforms pages 2-4) |


*Table: This table summarizes GO-relevant assertions for Saccharomyces cerevisiae HSC82/Hsc82, separating well-supported core annotations from broader or weaker terms. It is useful for deciding which GO labels are mechanistically justified for the constitutive Hsp90 isoform and which should be treated cautiously.*

References

1. (girstmair2019thehsp90isoforms pages 1-2): Hannah Girstmair, Franziska Tippel, Abraham Lopez, Katarzyna Tych, Frank Stein, Per Haberkant, Philipp Werner Norbert Schmid, Dominic Helm, Matthias Rief, Michael Sattler, and Johannes Buchner. The hsp90 isoforms from s. cerevisiae differ in structure, function and client range. Nature Communications, Aug 2019. URL: https://doi.org/10.1038/s41467-019-11518-w, doi:10.1038/s41467-019-11518-w. This article has 82 citations and is from a highest quality peer-reviewed journal.

2. (g2026thegeneontology pages 1-2): Suzi A Aleksander, James P Balhoff, Seth Carbon, J Michael Cherry, Dustin Ebert, Marc Feuermann, Pascale Gaudet, Nomi L Harris, David P Hill, Patrick Kalita, Raymond Lee, Huaiyu Mi, Sierra Moxon, Christopher J Mungall, Anushya Muruganujan, Tremayne Mushayahama, Paul W Sternberg, Paul D Thomas, Kimberly Van Auken, Edith D Wong, Valerie Wood, Jolene Ramsey, Deborah A Siegele, Rex L Chisholm, Robert Dodson, Petra Fey, Maria Cristina Aspromonte, Maria Victoria Nugnes, Ximena Aixa Castro Naser, Silvio C E Tosatto, Michelle Giglio, Suvarna Nadendla, Giulia Antonazzo, Helen Attrill, Nicholas H Brown, Gil dos Santos, Steven Marygold, Katja Röper, Victor Strelets, Christopher J Tabone, Jim Thurmond, Pinglei Zhou, Rossana Zaru, Ruth C Lovering, Colin Logie, Daqing Chen, Alexandra Naba, Karen Christie, Lori Corbani, Li Ni, Dmitry Sitnikov, Cynthia Smith, James Seager, Laurel Cooper, Justin Elser, Pankaj Jaiswal, Parul Gupta, Sushma Naithani, Pascal Carme, Kim Rutherford, Jeffrey L De Pons, Melinda R Dwinell, G Thomas Hayman, Mary L Kaldunski, Anne E Kwitek, Stanley J F Laulederkind, Marek A Tutaj, Mahima Vedi, Shur-Jen Wang, Peter D’Eustachio, Lucila Aimo, Kristian Axelsen, Alan Bridge, Nevila Hyka-Nouspikel, Anne Morgat, Gene Goldbold, Stacia R Engel, Stuart R Miyasato, Robert S Nash, Gavin Sherlock, Shuai Weng, Erika Bakker, Tanya Z Berardini, Leonore Reiser, Andrea Auchincloss, Ghislaine Argoud-Puy, Marie-Claude Blatter, Emmanuel Boutet, Lionel Breuza, Cristina Casals-Casas, Elisabeth Coudert, Anne Estreicher, Maria Livia Famiglietti, Arnaud Gos, Nadine Gruaz-Gumowski, Chantal Hulo, Florence Jungo, Philippe Le Mercier, Damien Lieberherr, Patrick Masson, Ivo Pedruzzi, Lucille Pourcel, Sylvain Poux, Catherine Rivoire, Shyamala Sundaram, Alex Bateman, Aduragbemi Adesina, Emily Bowler-Barnett, David Carpentier, Paul Denny, Alexandr Ignatchenko, Rizwan Ishtiaq, Antonia Lock, Yvonne Lussi, Michele Magrane, Maria J Martin, Sandra Orchard, Pedro Raposo, Elena Speretta, Nidhi Tyagi, Nadya Urakova, Kate Warner, Conny Wing-Hen Yu, Juancarlos Chan, Stavros Diamantakis, Mark Quinton-Tulloch, Daniela Raciti, Malcolm Fisher, Christina James-Zorn, Virgilio Ponferrada, Aaron Zorn, Doug Howe, Sridhar Ramachandran, Leyla Ruzicka, and Monte Westerfield. The gene ontology knowledgebase in 2026. Nucleic Acids Research, 54(D1):D1779-D1792, Dec 2025. URL: https://doi.org/10.1093/nar/gkaf1292, doi:10.1093/nar/gkaf1292. This article has 63 citations and is from a highest quality peer-reviewed journal.

3. (engel2025saccharomycesgenomedatabase pages 5-7): Stacia R. Engel, Suzi Aleksander, Robert S. Nash, Edith D. Wong, Shuai Weng, Stuart R. Miyasato, Gavin Sherlock, and J. Michael Cherry. Saccharomyces genome database: advances in genome annotation, expanded biochemical pathways, and other key enhancements. bioRxiv, Sep 2025. URL: https://doi.org/10.1101/2024.09.16.613348, doi:10.1101/2024.09.16.613348. This article has 82 citations.

4. (johnson2007nucleotidedependentinteractionof pages 1-2): Jill L. Johnson, Agnieszka Halas, and Gary Flom. Nucleotide-dependent interaction of <i>saccharomyces cerevisiae</i> hsp90 with the cochaperone proteins sti1, cpr6, and sba1. Molecular and Cellular Biology, 27:768-776, Jan 2007. URL: https://doi.org/10.1128/mcb.01034-06, doi:10.1128/mcb.01034-06. This article has 87 citations and is from a domain leading peer-reviewed journal.

5. (girstmair2019thehsp90isoforms pages 2-4): Hannah Girstmair, Franziska Tippel, Abraham Lopez, Katarzyna Tych, Frank Stein, Per Haberkant, Philipp Werner Norbert Schmid, Dominic Helm, Matthias Rief, Michael Sattler, and Johannes Buchner. The hsp90 isoforms from s. cerevisiae differ in structure, function and client range. Nature Communications, Aug 2019. URL: https://doi.org/10.1038/s41467-019-11518-w, doi:10.1038/s41467-019-11518-w. This article has 82 citations and is from a highest quality peer-reviewed journal.

6. (girstmair2019thehsp90isoforms media 03f98d7e): Hannah Girstmair, Franziska Tippel, Abraham Lopez, Katarzyna Tych, Frank Stein, Per Haberkant, Philipp Werner Norbert Schmid, Dominic Helm, Matthias Rief, Michael Sattler, and Johannes Buchner. The hsp90 isoforms from s. cerevisiae differ in structure, function and client range. Nature Communications, Aug 2019. URL: https://doi.org/10.1038/s41467-019-11518-w, doi:10.1038/s41467-019-11518-w. This article has 82 citations and is from a highest quality peer-reviewed journal.

7. (hohrman2021disruptingprogressionof pages 1-2): Kaitlyn Hohrman, Davi Gonçalves, Kevin A Morano, and Jill L Johnson. Disrupting progression of the yeast hsp90 folding pathway at different transition points results in client-specific maturation defects. Genetics, Jan 2021. URL: https://doi.org/10.1093/genetics/iyab009, doi:10.1093/genetics/iyab009. This article has 13 citations and is from a domain leading peer-reviewed journal.

8. (mercier2023hsp90mutantswith pages 2-4): Rebecca Mercier, Danielle Yama, Paul LaPointe, and Jill L. Johnson. Hsp90 mutants with distinct defects provide novel insights into cochaperone regulation of the folding cycle. PLOS Genetics, 19:e1010772, May 2023. URL: https://doi.org/10.1371/journal.pgen.1010772, doi:10.1371/journal.pgen.1010772. This article has 13 citations and is from a domain leading peer-reviewed journal.

9. (heim2024characterizationandchaperone pages 99-100): B Heim. Characterization and chaperone interactions of calcineurin from s. cerevisiae. Unknown journal, 2024.

10. (heim2024characterizationandchaperone pages 104-106): B Heim. Characterization and chaperone interactions of calcineurin from s. cerevisiae. Unknown journal, 2024.

11. (singh2012therolesof pages 67-72): SD Singh. The roles of hsp90 and calcineurin in antifungal drug resistance. Unknown journal, 2012.

12. (rizzolo2014theinteractionnetwork pages 1-4): Kamran Rizzolo, Philip Wong, Elisabeth R. M. Tillier, and Walid A. Houry. The interaction network of the hsp90 molecular chaperone. ArXiv, pages 111-131, Jan 2014. URL: https://doi.org/10.1007/978-1-4939-1130-1\_5, doi:10.1007/978-1-4939-1130-1\_5. This article has 5 citations.

13. (verghese2012biologyofthe pages 13-13): Jacob Verghese, Jennifer Abrams, Yanyu Wang, and Kevin A. Morano. Biology of the heat shock response and protein chaperones: budding yeast (saccharomyces cerevisiae) as a model system. Microbiology and Molecular Biology Reviews, 76:115-158, Jun 2012. URL: https://doi.org/10.1128/mmbr.05018-11, doi:10.1128/mmbr.05018-11. This article has 767 citations and is from a domain leading peer-reviewed journal.

14. (dodt2020characterizationofthe pages 24-27): CM Dodt. Characterization of the essential hsp90 co-chaperone sgt1 in s. cerevisiae. Unknown journal, 2020.

## Citations

1. g2026thegeneontology pages 1-2
2. engel2025saccharomycesgenomedatabase pages 5-7
3. johnson2007nucleotidedependentinteractionof pages 1-2
4. hohrman2021disruptingprogressionof pages 1-2
5. heim2024characterizationandchaperone pages 99-100
6. heim2024characterizationandchaperone pages 104-106
7. singh2012therolesof pages 67-72
8. rizzolo2014theinteractionnetwork pages 1-4
9. verghese2012biologyofthe pages 13-13
10. dodt2020characterizationofthe pages 24-27
11. https://doi.org/10.1038/s41467-019-11518-w
12. https://doi.org/10.1093/nar/gkaf1292
13. https://doi.org/10.1101/2024.09.16.613348
14. https://doi.org/10.1128/mcb.01034-06
15. https://doi.org/10.1093/genetics/iyab009
16. https://doi.org/10.1371/journal.pgen.1010772
17. https://doi.org/10.1038/s41467-019-11518-w,
18. https://doi.org/10.1093/nar/gkaf1292,
19. https://doi.org/10.1101/2024.09.16.613348,
20. https://doi.org/10.1128/mcb.01034-06,
21. https://doi.org/10.1093/genetics/iyab009,
22. https://doi.org/10.1371/journal.pgen.1010772,
23. https://doi.org/10.1007/978-1-4939-1130-1\_5,
24. https://doi.org/10.1128/mmbr.05018-11,