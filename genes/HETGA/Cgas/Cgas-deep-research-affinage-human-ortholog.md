---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/CGAS
affinage_run_date: 2026-06-09T22:57:18
uniprot_accession: Q8N884
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 27
citation_count: 27
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for CGAS (human)

## Current model (mechanistic narrative)

cGAS is a cytosolic and nuclear nucleic-acid sensor that initiates innate immune and cell-fate responses by detecting aberrant DNA and synthesizing the second messenger 2'3'-cGAMP, which activates downstream STING signaling [PMID:23722159]. A DNA-induced structural switch converts cGAS into an active nucleotidyl transferase that forms cGAMP, and beyond B-form dsDNA it also recognizes cytosolic RNA:DNA hybrids [PMID:23722159, PMID:25425575]. Activation requires assembly of a 2:2 cGAS-dsDNA complex, and cGAS is held inactive when bound to the nucleosome acidic patch via two conserved arginines that occlude its dsDNA-binding surface and lock it as a monomer [PMID:32911482, PMID:32913000]. This sets up cGAS as a sensor of genome instability: it accumulates at micronuclei following nuclear envelope rupture and is activated by exposed chromatin in a cell-cycle-dependent manner to drive interferon-stimulated gene expression, cellular senescence, and the senescence-associated secretory phenotype [PMID:28738408, PMID:28533362]. During mitosis, when cGAS contacts chromatin, it is restrained by nucleosome competition, Aurora kinase B-mediated N-terminal hyperphosphorylation, and blockade of oligomerization, while in arrested cells cGAS-dependent IRF3 phosphorylation can instead promote apoptosis [PMID:31299200, PMID:33542149]. cGAS activity is set by an extensive layer of regulators and modifications: G3BP1 promotes large activating cGAS complexes and DNA binding, MRE11-RAD50-NBN displaces cGAS from nucleosome sequestration to enable activation by oncogenic stress and ionizing radiation, and ZBP1 nucleates a cGAS-RIPK1-RIPK3 complex to sense mitochondrial genome instability [PMID:30510222, PMID:38200309, PMID:37352855]. Inhibitory modifications include DNA-PK phosphorylation, ZDHHC18-mediated C474 palmitoylation, PRMT1-mediated Arg133 methylation, PARP1-mediated PARylation at Asp191, and AARS2-mediated lactylation, while HERC5-mediated ISGylation enhances oligomerization and activity [PMID:33273464, PMID:35438208, PMID:37193698, PMID:35460603, PMID:39322678, PMID:38421872]. Nuclear cGAS is degraded by the CRL5-SPSB3 ubiquitin ligase via a C-terminal NN degron, and in the nucleus cGAS suppresses homologous recombination by interacting with PARP1 through poly(ADP-ribose) to impede the PARP1-Timeless complex [PMID:38418882, PMID:30356214]. cGAS also acts as a selective autophagy receptor for micronuclei through an LC3B-interacting region, and its DNA sensing is tuned by RNA-promoted phase separation [PMID:33752561, PMID:36382803]. The activated pathway has broad physiological consequences, including STING-dependent autophagy, antitumor immunity through cGAMP transfer to myeloid cells, and age-associated microglial dysfunction and neurodegeneration [PMID:30842662, PMID:31665636, PMID:37532932].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0003677 DNA binding, GO:0016740 transferase activity, GO:0140098 catalytic activity, acting on RNA, GO:0003723 RNA binding, GO:0140299 molecular sensor activity, GO:0140096 catalytic activity, acting on a protein
- **localization:** GO:0005829 cytosol, GO:0005634 nucleus, GO:0005694 chromosome, GO:0005739 mitochondrion
- **pathway (Reactome):** R-HSA-168256 Immune System, R-HSA-8953897 Cellular responses to stimuli, R-HSA-73894 DNA Repair, R-HSA-9612973 Autophagy, R-HSA-5357801 Programmed Cell Death
- **partners:** STING1, G3BP1, PARP1, ZBP1, DRP1, MAP1LC3B, MRE11, SPSB3
- **complexes:** cGAS-PARP1 (poly(ADP-ribose)-mediated), ZBP1-cGAS-RIPK1-RIPK3 complex, CRL5-SPSB3 ubiquitin ligase (substrate)

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2013 | High | Crystal structure of cGAS alone and in complex with DNA, ATP, and GTP revealed that cGAS catalyzes dinucleotide (cGAMP) formation via a DNA-induced structural switch; cGAS possesses structural similarity to OAS1 and contains a unique zinc thumb that recognizes B-form dsDNA. | PMID:23722159 | Nature |
| 2014 | High | cGAS recognizes cytosolic RNA:DNA hybrids in addition to dsDNA; recombinant cGAS produced cGAMP upon RNA:DNA hybrid recognition in vitro, and THP-1 knockout cells confirmed this response is mediated entirely through the cGAS-STING pathway. | PMID:25425575 | The EMBO journal |
| 2017 | High | cGAS localizes to micronuclei arising from genome instability; breakdown of the micronuclear envelope leads to rapid cGAS accumulation at chromatin, and cGAS is activated by chromatin in a cell-cycle-dependent manner, triggering interferon-stimulated gene expression in micronucleated cells. | PMID:28738408 | Nature |
| 2017 | High | cGAS is essential for cellular senescence and the senescence-associated secretory phenotype (SASP); deletion of cGAS accelerated immortalization of MEFs and abrogated SASP induced by DNA-damaging agents. cGAS localizes in the cytoplasm of non-dividing cells but enters the nucleus and associates with chromatin DNA during mitosis. | PMID:28533362 | Proceedings of the National Academy of Sciences of the United States of America |
| 2018 | High | Nuclear cGAS suppresses homologous recombination (HR) DNA repair. DNA damage induces nuclear translocation of cGAS dependent on importin-α; phosphorylation of cGAS at Tyr215 by B-lymphoid tyrosine kinase (BLK) facilitates cytosolic retention. In the nucleus, cGAS is recruited to DSBs, interacts with PARP1 via poly(ADP-ribose), and the cGAS-PARP1 interaction impedes formation of the PARP1-Timeless complex, suppressing HR. | PMID:30356214 | Nature |
| 2018 | High | G3BP1 physically interacts with cGAS and promotes formation of large cGAS complexes, enhancing DNA binding of cGAS and its activation; G3BP1 deficiency leads to inefficient DNA binding by cGAS and inhibited cGAS-dependent IFN production. | PMID:30510222 | Nature immunology |
| 2019 | High | cGAS-dependent IRF3 phosphorylation during mitotic arrest promotes apoptosis through transcription-independent alleviation of Bcl-xL-dependent suppression of mitochondrial outer membrane permeabilization; nucleosomes competitively inhibit DNA-dependent cGAS activation so cGAS-STING is not effectively activated during normal mitosis. | PMID:31299200 | Cell |
| 2019 | High | STING activates autophagy through a TBK1- and interferon-independent mechanism upon cGAMP binding; STING translocates to the ERGIC and Golgi in a COP-II- and ARF GTPase-dependent manner, and STING-containing ERGIC serves as a membrane source for LC3 lipidation (autophagosome biogenesis) dependent on WIPI2 and ATG5. | PMID:30842662 | Nature |
| 2020 | High | Cryo-EM structure of human cGAS bound to nucleosomes revealed that cGAS makes extensive contacts with the acidic patch of H2A-H2B and nucleosomal DNA; nucleosome binding locks cGAS into an inactive monomeric state through steric hindrance. Mutations to the cGAS-acidic patch interface abolished nucleosome-mediated inhibition in vitro and unleashed cGAS activity on genomic DNA in living cells. | PMID:32911482 | Nature |
| 2020 | High | Cryo-EM structure (3.3 Å) of cGAS bound to nucleosome core particle showed cGAS uses two conserved arginines to anchor to the nucleosome acidic patch; this nucleosome-binding interface exclusively occupies the strong dsDNA-binding surface on cGAS and sterically prevents cGAS from oligomerizing into the active 2:2 cGAS-dsDNA state. | PMID:32913000 | Science |
| 2020 | Medium | DNA-PK (DNA-PKcs) phosphorylates cGAS and suppresses its enzymatic activity; DNA-PK deficiency reduces cGAS phosphorylation and promotes antiviral innate immune responses. | PMID:33273464 | Nature communications |
| 2021 | High | cGAS activity is selectively suppressed during mitosis by two parallel mechanisms: (1) hyperphosphorylation of the N-terminus by mitotic kinases including Aurora kinase B, which blocks chromatin sensing; and (2) prevention of oligomerization of chromatin-bound cGAS. Together these prevent autoimmune activation when cGAS contacts chromatin during mitosis. | PMID:33542149 | Science |
| 2021 | High | TREX1 (ER-associated nuclease) inhibits cGAS activation at micronuclei by degrading micronuclear DNA upon micronuclear envelope rupture; the ER accesses ruptured micronuclei and enables TREX1 nucleolytic attack. TREX1 mutations that untether it from the ER disrupt localization to micronuclei and enhance cGAS activation. | PMID:33476576 | Molecular cell |
| 2021 | Medium | cGAS functions as a micronucleophagy receptor: it accumulates in autophagic machinery and directly interacts with MAP1LC3B via a MAP1LC3-interacting region (LIR). This interaction is essential for LC3 recruitment to micronuclei and their clearance via selective autophagy, which dampens cGAMP production induced by genotoxic stress. | PMID:33752561 | Autophagy |
| 2022 | High | Palmitoylation of cGAS at C474, catalyzed mainly by the palmitoyltransferase ZDHHC18, restricts cGAS enzymatic activity by reducing the interaction between cGAS and dsDNA and inhibiting cGAS dimerization; dsDNA promotes this palmitoylation modification. | PMID:35438208 | The EMBO journal |
| 2022 | Medium | PRMT1 methylates cGAS at conserved Arg133, preventing cGAS dimerization and suppressing cGAS/STING signaling in cancer cells; PRMT1 ablation activates cGAS/STING-dependent DNA sensing and elevates type I and II interferon response genes. | PMID:37193698 | Nature communications |
| 2022 | High | Cytoplasmic PARP1 (translocated via DNA-PK-mediated Thr594 phosphorylation) directly PARylates cGAS at Asp191, inhibiting its DNA-binding ability and antiviral immunity. | PMID:35460603 | Molecular cell |
| 2022 | Medium | Cytoplasmic RNAs promote phase separation of cGAS in vitro and colocalize with phase-separated cGAS-dsDNA condensates in cells; RNAs enhance cGAS enzymatic activity when dsDNA concentration is low by promoting condensate formation. | PMID:36382803 | EMBO reports |
| 2023 | Medium | cGAS is localized to the outer mitochondrial membrane in hepatocellular carcinoma cells, where it associates with DRP1 to facilitate DRP1 oligomerization; loss of cGAS or DRP1 oligomerization increases mitochondrial ROS and ferroptosis, inhibiting tumor growth. | PMID:36864172 | Cell research |
| 2023 | High | ZBP1 stabilizes Z-form mtDNA and nucleates a cytosolic complex containing cGAS, RIPK1, and RIPK3 to sustain STAT1 phosphorylation and type I IFN signaling; cGAS cooperates with ZBP1 in detecting mitochondrial genome instability. | PMID:37352855 | Cell |
| 2023 | High | Cytosolic DNA released from perturbed mitochondria elicits cGAS activity in old microglia; cGAS gain-of-function in microglia is sufficient to drive ageing-associated transcriptional states, neurodegeneration, and cognitive decline via STING. | PMID:37532932 | Nature |
| 2023 | Medium | SIRT2 deacetylates G3BP1 at K257, K276, and K376, causing disassembly of the cGAS-G3BP1 complex, thereby inhibiting cGAS DNA binding and droplet formation and suppressing IFN production; SIRT2 deficiency or inhibition enhances cGAS-STING signaling. | PMID:37870259 | EMBO reports |
| 2024 | High | The MRE11-RAD50-NBN complex displaces cGAS from nucleosome acidic-patch-mediated sequestration by binding to nucleosome fragments, enabling cGAS mobilization and activation by dsDNA; MRE11 is essential for cGAS activation in response to oncogenic stress, cytosolic dsDNA, and ionizing radiation, and MRE11-dependent cGAS activation promotes ZBP1-RIPK3-MLKL-mediated necroptosis. | PMID:38200309 | Nature |
| 2024 | High | The CRL5-SPSB3 ubiquitin ligase complex degrades nuclear cGAS in cycling cells; SPSB3 is the substrate receptor that ligates ubiquitin onto nuclear cGAS via a conserved C-terminal Asn-Asn (NN) degron motif. Cryo-EM structure of nucleosome-bound cGAS in complex with SPSB3 revealed the structural basis. Interference with SPSB3-mediated nuclear cGAS degradation primes cells for type I IFN signaling. | PMID:38418882 | Nature |
| 2024 | High | AARS2 associates with cGAS and mediates its lactylation (via AARS1/2 acting as lactyltransferases) at an N-terminal site, abolishing cGAS liquid-like phase separation and DNA sensing; a lactyl-resistant cGAS knock-in protects mice against innate immune evasion induced by high L-lactate. | PMID:39322678 | Nature |
| 2024 | Medium | HERC5 catalyzes ISGylation of cGAS at K21, K187, K219, and K458; ISGylation promotes DNA-induced cGAS oligomerization and enhances cGAS enzymatic activity. USP18 removes ISGylation from cGAS. ISGylation deficiency attenuates IFN expression and antiviral defense. | PMID:38421872 | Cell reports |
| 2020 | Medium | Cancer cells produce cGAMP that is transferred via gap junctions to tumor-associated dendritic cells and macrophages, which respond by producing type I IFN in situ; cancer-cell-intrinsic cGAS (but not STING) expression promotes CD8+ T cell infiltration and tumor immunogenicity. | PMID:31665636 | Cell reports |

## Citations

- PMID:23722159
- PMID:25425575
- PMID:28533362
- PMID:28738408
- PMID:30356214
- PMID:30510222
- PMID:30842662
- PMID:31299200
- PMID:31665636
- PMID:32911482
- PMID:32913000
- PMID:33273464
- PMID:33476576
- PMID:33542149
- PMID:33752561
- PMID:35438208
- PMID:35460603
- PMID:36382803
- PMID:36864172
- PMID:37193698
- PMID:37352855
- PMID:37532932
- PMID:37870259
- PMID:38200309
- PMID:38418882
- PMID:38421872
- PMID:39322678
