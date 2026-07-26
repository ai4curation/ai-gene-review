---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/BRCA1
affinage_run_date: 2026-06-09T22:02:45
uniprot_accession: P38398
self_evaluation_pairwise: tie
faith_pct: 100.0
n_discoveries: 22
citation_count: 22
gates_passed: False
note: >-
  Machine-fetched from the Affinage API (Cheeseman Lab). This is external
  precomputed research to be treated as a preliminary source, NOT a curated
  annotation. Affinage is human-only and LLM-generated; verify claims against
  the cited PMIDs before use.
---

# Affinage mechanistic annotation for BRCA1 (human)

> ⚠️ **CAUTION — trust gate(s) tripped; review before using:**
>
> - Affinage's own head-to-head self-evaluation scored this record `pairwise = tie` (not `win`) vs the curated UniProt reference — treat the narrative with extra scepticism.

## Current model (mechanistic narrative)

BRCA1 is a multifunctional nuclear tumor suppressor that safeguards genome integrity by promoting error-free homologous recombination (HR) repair of DNA double-strand breaks and limiting mutagenic nonhomologous repair [PMID:10549283]. It executes HR through two genetically separable activities: a coiled-coil-dependent function that counteracts the 53BP1-RIF1-Shieldin axis to license DNA end resection, and a Δ11-region/PALB2-dependent function that loads RAD51 onto resected DNA, with RNF168 acting redundantly with BRCA1 in the PALB2-loading step [PMID:30704900, PMID:32359443]. BRCA1 functions as a RING-domain heterodimer with BARD1; cryo-EM of the BRCA1-BARD1–nucleosome complex shows BARD1 ankyrin and BRCT domains reading nucleosomal histones, DNA, and the DSB-specific H2A K13/K15 monoubiquitin mark while the RING domains position an E2 enzyme for C-terminal H2A ubiquitylation that opposes 53BP1 [PMID:34321665]. Recruitment to ionizing-radiation-induced foci requires cooperation of the BRCA1 RING and BRCT domains and co-localization with MDC1, with cancer mutations abolishing targeting [PMID:15569676], and BRCA1 retention at breaks is organized by the RAP80/Abraxas(CCDC98)/MERIT40-containing BRCA1-A complex, which controls foci formation and the G2/M checkpoint [PMID:17643121, PMID:19261748]. Heterodimer assembly and DNA-damage localization are tuned by SIRT2-mediated deacetylation of the BARD1 RING interface, while BAP1 antagonizes the BRCA1/BARD1 ligase through both catalytic and non-catalytic mechanisms [PMID:33789098, PMID:19117993]. As an E3 ubiquitin ligase BRCA1/BARD1 modifies substrates including topoisomerase IIα, regulating DNA decatenation and chromosome segregation [PMID:15965487], and estrogen receptor-α, repressing its transcriptional activity [PMID:19887647]. BRCA1 activity is integrated into genotoxic stress signaling through ATR phosphorylation of multiple residues including Ser1423 at stalled replication forks [PMID:11114888] and through p53/CRM1-dependent nuclear export after DNA damage [PMID:15087457]. Beyond repair, BRCA1 maintains centromere stability by resolving R-loops at α-satellite repeats to preserve CENP-A loading [PMID:34599155], supports XIST RNA concentration and chromatin structure on the inactive X chromosome [PMID:12419249], and acts as a transcriptional regulator—autorepressing its own promoter via a BRCA1/E2F1/Rb complex dissolved by genotoxic stress [PMID:20068145] and controlling target genes such as SIRT1 and the ferroptosis regulators VDAC3 and GPX4 [PMID:18851829, PMID:38552003].

## Affinage mechanism profile (its own GO/Reactome grounding)

_Recorded for reference. The AIGR evaluation found this grounding is coarse (collapses to general parents) and can contradict the narrative — do not import these GO ids directly; re-ground from the narrative + PMIDs._

- **molecular_activity:** GO:0016874 ligase activity, GO:0140096 catalytic activity, acting on a protein, GO:0140110 transcription regulator activity, GO:0003677 DNA binding, GO:0140098 catalytic activity, acting on RNA
- **localization:** GO:0005634 nucleus, GO:0000228 nuclear chromosome, GO:0005654 nucleoplasm
- **pathway (Reactome):** R-HSA-73894 DNA Repair, R-HSA-1640170 Cell Cycle, R-HSA-74160 Gene expression (Transcription), R-HSA-4839726 Chromatin organization, R-HSA-8953897 Cellular responses to stimuli
- **partners:** BARD1, ATR, RAP80, CCDC98, MERIT40, BAP1, SIRT2, PALB2
- **complexes:** BRCA1-BARD1 heterodimer, BRCA1-A complex (RAP80/Abraxas/MERIT40/BRCC45), BRCA1/E2F1/Rb repressive complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 1999 | High | Brca1-deficient mouse embryonic stem cells have impaired repair of chromosomal DNA double-strand breaks (DSBs) by homologous recombination, with altered relative frequencies of homologous vs. nonhomologous DNA integration and DSB repair, demonstrating a caretaker role for BRCA1 in promoting homologous recombination and limiting mutagenic nonhomologous repair. | PMID:10549283 | Molecular cell |
| 2000 | High | ATR phosphorylates BRCA1 on six Ser/Thr residues including Ser1423 in vitro and in vivo in response to UV light, hydroxyurea, aphidicolin, and partially in response to ionizing radiation. ATR and BRCA1 co-localize in nuclear foci at stalled replication forks, placing them in the same genotoxic stress-responsive pathway. | PMID:11114888 | Genes & development |
| 2002 | High | BRCA1 colocalizes with markers of the inactive X chromosome (Xi) in female somatic cells and physically associates with XIST RNA as detected by chromatin immunoprecipitation. BRCA1-deficient cells show defects in Xi chromatin structure and XIST RNA concentration; reconstitution of BRCA1-deficient cells with wild-type BRCA1 restored focal XIST RNA staining and reduced re-expression of a silenced Xi-located GFP transgene. | PMID:12419249 | Cell |
| 2003 | High | The purified BRCA1/BARD1 complex, together with E1 and UbcH5a, is sufficient to reconstitute monoubiquitination of FANCD2 in vitro. However, siRNA-mediated knockdown of BRCA1 in human cells does not lead to a defect in FANCD2 ubiquitination, and ablation of RING finger domains of BRCA1 or BARD1 in DT40 cells leaves FANCD2 modification intact. BRCA1 affects accumulation of FANCD2 at DNA damage sites but BRCA1/BARD1 E3 ligase activity is not essential for FANCD2 monoubiquitination in vivo. | PMID:12887909 | Molecular cell |
| 2003 | Medium | BRCA1 interacts with processive (hyperphosphorylated, IIO form) RNA polymerase II rather than the hypophosphorylated promoter-associated form (IIA) in undamaged cells. BRCA1-RNA pol II complexes are highly functional in transcriptional run-off assays and the interaction is disrupted by DNA-damaging agents. | PMID:14506230 | The Journal of biological chemistry |
| 2004 | Medium | BRCA1 interacts and colocalizes with topoisomerase IIα in S-phase cells. BRCA1-deficient cells show lagging chromosomes and defective DNA decatenation in vitro, phenocopying topoisomerase IIα inhibition. Topoisomerase IIα is ubiquitinated in a BRCA1-dependent manner, and its ubiquitination correlates with higher DNA decatenation activity. | PMID:15965487 | Nature structural & molecular biology |
| 2004 | Medium | BRCA1 RING and BRCT domains cooperate to target BRCA1 to ionizing radiation-induced nuclear foci. Cancer mutations in the BRCT domain abolish recruitment. A RING-BRCT fusion restores foci targeting, co-localizes with MDC1, and inhibits entry of endogenous BRCA1 into foci. Neither RING nor BRCT domain alone is sufficient for targeting. | PMID:15569676 | The Journal of biological chemistry |
| 2007 | Medium | CCDC98 (Abraxas) is a component of the BRCA1-RAP80 complex that mediates BRCA1's association with RAP80, controls DNA damage-induced formation of BRCA1 foci, and is required for BRCA1-dependent G2/M checkpoint activation. | PMID:17643121 | Nature structural & molecular biology |
| 2008 | Medium | BRCA1 binds the SIRT1 promoter and increases SIRT1 expression, which in turn inhibits Survivin by altering epigenetic modification of histone H3. Absence of SIRT1 blocks BRCA1's regulation of Survivin. | PMID:18851829 | Molecular cell |
| 2009 | High | BRCA1-associated protein 1 (BAP1) interacts with the RING finger domain of BARD1 and interferes with the BRCA1/BARD1 E3 ligase association via surface plasmon resonance. BAP1 inhibits BRCA1 autoubiquitination and NPM1/B23 ubiquitination by BRCA1/BARD1. A catalytically inactive BAP1 mutant (C91S) still inhibits ubiquitination, indicating a second non-catalytic inhibitory mechanism. | PMID:19117993 | Cancer research |
| 2009 | Medium | MERIT40 (a 40 kDa protein) assembles into the RAP80/CCDC98-containing BRCA1-A complex via direct interaction with BRE/BRCC45, and is required for maintaining stability of BRE and the five-subunit complex at DNA damage sites, thereby regulating BRCA1 retention at DNA breaks and checkpoint function. | PMID:19261748 | Genes & development |
| 2009 | Medium | BRCA1 overexpression reduces acetylation of estrogen receptor-α (ER-α) and increases mono-ubiquitination of ER-α; a BRCA1 mutant defective for ubiquitin ligase activity (I26A) failed to ubiquitinate ER-α or repress its transcriptional activity in vivo. Wild-type BRCA1 but not cancer mutant C61G inhibited p300-mediated acetylation of ER-α in vitro. | PMID:19887647 | Molecular endocrinology |
| 2010 | Medium | BRCA1 assembles with complexes containing E2F-1 and RB to form a repressive multicomponent transcriptional complex that inhibits BRCA1 promoter transcription (autoregulatory loop). Genotoxic stress disrupts this complex, displacing BRCA1 from its own promoter and upregulating BRCA1 transcription. Tandem ChIP confirmed the BRCA1/E2F1/Rb complex at the BRCA1 promoter in vivo. | PMID:20068145 | Cancer research |
| 2019 | High | RNF168 acts redundantly with BRCA1 to load PALB2 onto damaged DNA. Loss of RNF168 negates synthetic rescue of BRCA1 deficiency by 53BP1 deletion. Forced targeting of PALB2 to DNA breaks circumvents BRCA1 haploinsufficiency. BRCA1 promotes two distinct steps of homologous recombination: DNA end resection (counteracting 53BP1) and RAD51 loading (via PALB2 recruitment). | PMID:30704900 | Molecular cell |
| 2020 | High | BRCA1 promotes two genetically separable activities in homologous recombination: (1) counteracting 53BP1-RIF1-Shieldin to promote DNA end resection (via the coiled-coil domain) and (2) promoting RAD51 loading (via the Δ11 region). Brca1CC and Brca1Δ11 alleles are separation-of-function mutations that complement each other to provide sufficient HR for normal development. | PMID:32359443 | Molecular cell |
| 2021 | High | Cryo-EM structure of BRCA1-BARD1 bound to nucleosome revealed that ankyrin repeat and tandem BRCT domains in BARD1 bind nucleosomal histones, DNA, and monoubiquitin on H2A K13/K15 (DSB-specific marks). RING domains in BRCA1-BARD1 orient an E2 ubiquitin-conjugating enzyme atop the nucleosome for ubiquitin transfer to flexible C-terminal tails of H2A/H2AX. Recognition of N-terminal H2A monoubiquitin blocks polyubiquitin chain formation and cooperatively promotes C-terminal H2A ubiquitylation, opposing 53BP1. | PMID:34321665 | Nature |
| 2021 | Medium | SIRT2 deacetylase complexes with BRCA1-BARD1 and deacetylates conserved lysines in the BARD1 RING domain at the BRCA1-BARD1 interface, promoting BRCA1-BARD1 heterodimerization, mutual stability, nuclear retention, localization to DNA damage sites, and efficient homologous recombination. | PMID:33789098 | Cell reports |
| 2021 | Medium | BRCA1 associates with centromeric chromatin in an R-loop-dependent manner and counteracts accumulation of R-loops at centromeric α-satellite repeats. BRCA1-deficient cells show impaired CENP-A localization, increased centromeric RNA transcription, increased centromeric breakage, acentric micronuclei, and Rad52-dependent hyper-recombination at centromeric satellites, all R-loop-dependent. | PMID:34599155 | Cell death & disease |
| 1999 | Low | Casein kinase 2 (CK2) β-subunit associates with the carboxy-terminal region of BRCA1 (yeast two-hybrid and Sf9 cell confirmation) and phosphorylates BRCA1 in vitro at Ser1572; the cancer-associated missense mutation M1775R in BRCA1 weakens the CK2β association. | PMID:10403822 | Biochemical and biophysical research communications |
| 2000 | Low | BRCA1 physically associates with ATF1 (a CREB/ATF transcription factor) via the BRCA1 RING finger domain in vitro, in yeast, and in human cells. BRCA1 stimulates transcription from a CRE reporter gene and from the TNF-α promoter in a CRE-dependent manner. | PMID:10945975 | The Journal of biological chemistry |
| 2004 | Medium | DNA damage (ionizing radiation) induces BRCA1 nuclear export in a dose-dependent, CRM1-dependent manner that also requires wild-type p53 function. BRCA1 nuclear export occurs across all cell cycle phases, representing a p53-dependent regulatory mechanism of BRCA1 localization in response to DNA damage. | PMID:15087457 | The Journal of biological chemistry |
| 2024 | Medium | BRCA1 promotes transcription of both VDAC3 and GPX4; BRCA1 deficiency blocks VDAC3-dependent erastin-induced ferroptosis but sensitizes cells to GPX4 inhibitor-induced ferroptosis. NCOA4-mediated ferritinophagy and defective GPX4 induction synergize PARPi and GPX4 inhibition to induce ferroptosis in BRCA1-deficient cancer cells. | PMID:38552003 | Cancer discovery |

## Citations

- PMID:10403822
- PMID:10549283
- PMID:10945975
- PMID:11114888
- PMID:12419249
- PMID:12887909
- PMID:14506230
- PMID:15087457
- PMID:15569676
- PMID:15965487
- PMID:17643121
- PMID:18851829
- PMID:19117993
- PMID:19261748
- PMID:19887647
- PMID:20068145
- PMID:30704900
- PMID:32359443
- PMID:33789098
- PMID:34321665
- PMID:34599155
- PMID:38552003
