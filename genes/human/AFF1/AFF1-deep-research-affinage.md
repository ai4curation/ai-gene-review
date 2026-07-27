---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/AFF1
affinage_run_date: 2026-06-09T22:02:42
uniprot_accession: P51825
self_evaluation_pairwise: 
faith_pct: 100.0
n_discoveries: 23
citation_count: 23
gates_passed: True
note: >-
  Machine-fetched from the Affinage API (Cheeseman Lab). This is external
  precomputed research to be treated as a preliminary source, NOT a curated
  annotation. Affinage is human-only and LLM-generated; verify claims against
  the cited PMIDs before use.
---

# Affinage mechanistic annotation for AFF1 (human)

## Current model (mechanistic narrative)

AFF1 (AF4) is a nuclear scaffolding subunit of the super elongation complex (SEC) that drives RNA polymerase II transcriptional elongation [PMID:21030982, PMID:24367103]. Originally identified as the serine/proline-rich, glutamine-rich putative transcription factor fused to MLL by the t(4;11) translocation [PMID:1423625, PMID:7689231], AFF1 was established as a bona fide transcriptional activator through its autonomous transactivation domain [PMID:8555498] and localizes to discrete subnuclear foci ('AF4 bodies') where it co-localizes with the chromatin reader AF9 [PMID:9808577, PMID:14603337]. AFF1 constitutively binds the P-TEFb kinase (CDK9-CycT) and is a ubiquitous component of the P-TEFb network, partitioning among the 7SK snRNP, SECs, and Brd4-P-TEFb complexes; the tripartite CDK9-CycT-AFF1 module is transferred as a unit, and AFF1 stimulates P-TEFb kinase activity to phosphorylate the Pol II CTD and release promoter-arrested polymerase [PMID:21030982, PMID:24367103]. Within an AF4/AF9/ENL/AF10 assembly it recruits the H3K79 methyltransferase DOT1L to elongating Pol II, coupling elongation to chromatin modification [PMID:17135274, PMID:18977325, PMID:21030982]. AFF1 activates specific target promoters by direct binding, including Igf-1 in cerebellar Purkinje cells [PMID:20007461], CD133/PROM1 [PMID:22337994], and DKK1 in mesenchymal stem cells where it restrains osteogenic differentiation [PMID:28955517]. Its dosage and activity are tightly controlled: SIAH1/SIAH2 E3 ubiquitin ligases bind the AFF1 N-terminus to direct proteasomal turnover [PMID:15221006, PMID:15459319], and p300-mediated acetylation transiently disrupts SEC assembly and dampens Pol II CTD phosphorylation during genotoxic stress [PMID:31611376]. A missense mutation reducing SIAH-mediated degradation stabilizes Af4, elevates its transcriptional output, and causes autosomal dominant cerebellar ataxia with Purkinje cell loss in mice [PMID:12629167, PMID:15459319]. In t(4;11) leukemia, the MLL-AF4 fusion redirects these elongation and H3K79-methylation activities to hematopoietic loci, and disruption of the AF4-AF9 interaction selectively kills MLL-AF4 leukemic cells [PMID:15269783, PMID:18977325, PMID:34431785].

## Affinage mechanism profile (its own GO/Reactome grounding)

_Recorded for reference. The AIGR evaluation found this grounding is coarse (collapses to general parents) and can contradict the narrative — do not import these GO ids directly; re-ground from the narrative + PMIDs._

- **molecular_activity:** GO:0140110 transcription regulator activity, GO:0003677 DNA binding, GO:0098772 molecular function regulator activity, GO:0060090 molecular adaptor activity
- **localization:** GO:0005634 nucleus, GO:0005654 nucleoplasm
- **pathway (Reactome):** R-HSA-74160 Gene expression (Transcription), R-HSA-4839726 Chromatin organization, R-HSA-1643685 Disease
- **partners:** CDK9, CCNT1, AF9, DOT1L, SIAH1, SIAH2, EP300, DDX6
- **complexes:** super elongation complex (SEC), P-TEFb (CDK9-CycT), AF4/ENL/P-TEFb (AEP) complex, MLL-AF4 fusion complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 1992 | High | The t(4;11) chromosomal translocation fuses the ALL-1 (MLL) gene to the AF-4 (AFF1) gene on chromosome 4, generating a chimeric protein. AF-4 was identified as a serine- and proline-rich putative transcription factor with a glutamine-rich carboxyl terminus. | PMID:1423625 | Cell |
| 1993 | High | The MLL-AF4 fusion protein (der(11) product) retains the AF4 transactivation domain. AF4 was characterized as a serine-proline-rich putative transcription factor with nuclear localization and GTP-binding motifs in the portion retained in the fusion. | PMID:7689231 | Proceedings of the National Academy of Sciences of the United States of America |
| 1996 | Medium | AF4 protein has a domain that activates transcription when fused to the GAL4 DNA-binding domain, establishing AF4 as a transcriptional activator. The AF4 transactivation domain is retained in the MLL/AF4 fusion protein. | PMID:8555498 | Blood |
| 1997 | Medium | The AF-4 protein (116 kDa) is localized predominantly to the nucleus in mitogen-stimulated human peripheral blood mononuclear cells, consistent with its role as a nuclear transcription factor. The gene contains five highly conserved domains shared with LAF-4 and FMR-2 family members. | PMID:9233580 | British journal of haematology |
| 1997 | Medium | The murine Af4 protein localizes to the nucleus and encodes a region in its 5' half with transcriptional transactivation activity, which is disrupted by the t(4;11) translocation in human leukemias. | PMID:9365243 | Oncogene |
| 1998 | Medium | AF4 protein (125 kDa and 145 kDa isoforms) localizes to discrete subnuclear punctate compartments by confocal immunofluorescence in both t(4;11) and non-t(4;11) leukemic cells. A 45-kDa protein co-precipitates with AF4. The MLL-AF4 fusion protein (240 kDa) shows a similar subnuclear distribution as wild-type AF4. | PMID:9808577 | Blood |
| 2001 | Medium | Drosophila Lilliputian (lilli), the AF4/FMR2 family ortholog, functions in the Ras/MAPK pathway for cell identity determination and is essential for normal cellular growth. Loss of Lilli autonomously reduces cell size and partially suppresses growth increases from PTEN loss, placing AF4-family proteins in parallel with Ras/MAPK and PI3K/PKB pathways. | PMID:11171403 | Development (Cambridge, England) |
| 2003 | High | A missense mutation in the highly conserved region of mouse Af4 causes autosomal dominant cerebellar ataxia with region-specific Purkinje cell loss. Af4 is specifically expressed in Purkinje cells, establishing a direct role for Af4 in cerebellar neuronal maintenance. | PMID:12629167 | The Journal of neuroscience |
| 2004 | Medium | AF4 and AF9 interact at discrete subnuclear foci termed 'AF4 bodies'. This interaction is maintained by the MLL-AF4 fusion protein, and MLL-AF4 expression alters the subnuclear localization of AF9. | PMID:14603337 | Leukemia |
| 2004 | Medium | AF4 wild-type protein and the AF4.MLL fusion protein interact with E3 ubiquitin ligases SIAH1 and SIAH2 via the N-terminal portion of AF4, and this interaction protects AF4.MLL from proteasomal degradation, contributing to growth transformation. | PMID:15221006 | Oncogene |
| 2004 | Medium | A synthetic peptide (PFWT) based on the AF9-binding domain of AF4 disrupts the AF4-AF9 protein interaction in vitro and in vivo, and inhibits proliferation/induces apoptosis specifically in t(4;11) leukemia cells expressing MLL-AF4. | PMID:15269783 | Leukemia |
| 2004 | High | Af4 binds E3 ubiquitin ligases Siah-1a and Siah-2 in the brain (identified by yeast two-hybrid). The robotic mutant Af4 shows significantly reduced affinity for Siah-1a, leading to near-complete abolition of mutant Af4 proteasomal degradation and accumulation of Af4 in Purkinje cells. Mutant Af4 has increased transcriptional activity relative to wild-type, indicating that Siah-mediated degradation controls Af4 transcriptional activity levels. | PMID:15459319 | Proceedings of the National Academy of Sciences of the United States of America |
| 2006 | High | Mouse Af4 functions as a positive regulator of P-TEFb kinase activity and, in complex with MLL fusion partners Af9, Enl, and Af10, mediates histone H3-K79 methylation by recruiting Dot1 to elongating RNA Pol II. P-TEFb-dependent phosphorylation of Af4, Af9, and Enl controls their transactivation activity and/or protein stability. Increased phosphorylated Pol II and methylated H3-K79 are observed in the ataxic robotic mouse (Af4 overexpression model). | PMID:17135274 | Human molecular genetics |
| 2008 | High | MLL-AF4 fusion promotes H3K79 methylation at target gene loci. Suppression of the H3K79 methyltransferase DOT1L inhibits expression of critical MLL-AF4 target genes, establishing a mechanistic link between MLL-AF4, DOT1L recruitment, and H3K79 methylation-dependent gene activation. | PMID:18977325 | Cancer cell |
| 2009 | High | Af4 directly regulates transcription of the Igf-1 gene in Purkinje cells, as confirmed by chromatin immunoprecipitation. Loss/reduction of Igf-1 leads to decreased downstream IGF-1R and ERK1/2 activation, and IGF-1 treatment delayed Purkinje cell death in robotic mice. | PMID:20007461 | The Journal of neuroscience |
| 2010 | High | Affinity purification of the AF4 protein complex identified 11 binding partners including P-TEFb kinase and demonstrated P-TEFb-mediated activation of promoter-arrested RNA Pol II, together with chromatin-modifying activities. The AF4-MLL fusion complex contains at least 16 constituents, additionally including H3K4(me3) and H3K79(me3) histone methyltransferases, a protein arginine N-methyltransferase, and a histone acetyltransferase, causing disturbed RNA Pol II activation and altered histone methylation signatures. | PMID:21030982 | Leukemia |
| 2012 | Medium | AF4 directly promotes CD133 (PROM1) transcription. Knockdown of AF4 causes a dramatic reduction in CD133 transcript levels across multiple cancer cell lines, and CD133 is required for leukemia cell survival in MLL-AF4+ ALL cells. | PMID:22337994 | Cancer research |
| 2013 | High | AFF1 is a ubiquitous component of the P-TEFb network: it is bound to CDK9-CycT and present in all major P-TEFb complexes (7SK snRNP, SECs, and Brd4-P-TEFb complex). The tripartite CDK9-CycT-AFF1 complex is transferred as a unit within the network. AFF1 increases Tat's affinity for CycT1, facilitating Tat's extraction of P-TEFb from 7SK snRNP and formation of Tat-SECs for HIV transcription. | PMID:24367103 | Proceedings of the National Academy of Sciences of the United States of America |
| 2016 | Medium | DDX6, a DEAD-box RNA helicase, binds to 7SK snRNA and transfers P-TEFb to the AF4/AF4N (AFF1) super elongation complex. DDX6 also stably binds AF4 and AF4N. Co-overexpression of AF4/AF4N with DDX6 causes an 11-fold increase in mRNA production, while DDX6 knockdown decreases mRNA production by 70%. | PMID:27679741 | American journal of blood research |
| 2017 | High | AFF1 regulates expression of DKK1 by directly binding to its promoter region. Depletion of AFF1 in human MSCs increases osteogenic differentiation (ALP activity, mineralization, osteogenic gene expression), and knockdown of DKK1 in AFF1-overexpressing MSCs abrogates the impairment of osteogenic differentiation, placing AFF1 upstream of DKK1 in MSC osteogenesis. | PMID:28955517 | Bone research |
| 2019 | High | p300 acetylates AFF1 at a specific site, reducing its interaction with other super elongation complex (SEC) components and impairing P-TEFb-mediated CTD phosphorylation of RNA Pol II both in vitro and in vivo. Upon genotoxic stress, p300-mediated AFF1 acetylation is dynamically induced and correlates with global transcriptional downregulation. Re-expression of wild-type AFF1, but not an acetylation-mimic mutant, restores SEC recruitment and target gene expression. | PMID:31611376 | Proceedings of the National Academy of Sciences of the United States of America |
| 2021 | Medium | MLL-ELL recruits an AF4/ENL/P-TEFb (AEP) complex—containing AFF1 (AF4)—to target promoters to activate transcription in murine hematopoietic progenitors. The C-terminal portion of ELL provides a binding platform for AF4 (as well as EAF1 and p53). The HBO1 complex promotes AEP (AFF1-containing SEC) association over EAF1. | PMID:34431785 | eLife |
| 2022 | Medium | Disruption of 7SK snRNP causes complete dissociation of the Cdk9/CycT1 heterodimer into monomers under stress conditions. AFF1-containing SEC (along with Brd4) then recruits monomerized Cdk9 and CycT1 on chromatin, reassembling active P-TEFb and inducing autophosphorylation of Cdk9 T186. | PMID:34935961 | Nucleic acids research |

## Citations

- PMID:11171403
- PMID:12629167
- PMID:1423625
- PMID:14603337
- PMID:15221006
- PMID:15269783
- PMID:15459319
- PMID:17135274
- PMID:18977325
- PMID:20007461
- PMID:21030982
- PMID:22337994
- PMID:24367103
- PMID:27679741
- PMID:28955517
- PMID:31611376
- PMID:34431785
- PMID:34935961
- PMID:7689231
- PMID:8555498
- PMID:9233580
- PMID:9365243
- PMID:9808577
