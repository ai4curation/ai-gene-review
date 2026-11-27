---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ARFGEF1
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q9Y6D6
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 26
citation_count: 26
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ARFGEF1 (human)

## Current model (mechanistic narrative)

ARFGEF1/BIG1 is a Golgi-localized guanine nucleotide exchange factor that activates class I ARFs via its Sec7 domain to drive vesicular trafficking, with brefeldin A acting as an uncompetitive inhibitor of the BIG1–ARF complex [PMID:10393931]. It is recruited to the trans-Golgi by the Arf-like GTPase Arl1 binding its N-terminal region [PMID:22291037], downstream of a GEF cascade in which GBF1-activated ARF4/ARF5 promote BIG1/BIG2 TGN recruitment [PMID:23386609], where BIG1 acts redundantly with BIG2 in AP-1-dependent transport between the TGN and endosomes [PMID:18417613] while non-redundantly maintaining Golgi morphology [PMID:20360857]. Through its GEF activity BIG1 controls surface trafficking of multiple cargoes, including integrin β1 glycosylation and RhoA activation [PMID:17227842], ABCA1 recycling and cholesterol efflux [PMID:23220274], and neuronal GABAA receptor surface expression [PMID:24198228]. Its catalytic activity is subject to a cAMP/PKA switch: PKA phosphorylates Ser-883 to reduce GEF activity and is reversed by PP1γ [PMID:17360629], while PDE3A-containing AKAP complexes limit local cAMP to sustain ARF1 activation [PMID:19332778]; the same phosphorylation, together with an NLS and intact microtubules, drives nuclear/nucleolar translocation where BIG1 associates with nucleolin, U3 snoRNA, and fibrillarin [PMID:16467138, PMID:18292223]. Beyond catalysis, BIG1 scaffolds nonmuscle myosin IIA phosphatase complexes (with PP1δ and MYPT1) to regulate actomyosin dynamics and cell migration [PMID:23918382] and binds myosin IXb to inhibit its RhoA-GAP activity [PMID:15644318]. In immune and neural contexts it promotes pro-inflammatory TLR4 signaling via ARF3-dependent PI(4,5)P2 synthesis and TIRAP recruitment [PMID:32415087], supports TNFR1 complex assembly through TRAF2 recruitment [PMID:27834853], and is required for Schwann cell myelination through ARF1/AP-1-dependent trafficking [PMID:29740613]. Loss-of-function studies establish that BIG1 is essential for cortical neuron survival and axon guidance [PMID:28414797], and haploinsufficiency reduces seizure threshold via impaired GABAA receptor trafficking [PMID:31678406].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0140096 catalytic activity, acting on a protein, GO:0098772 molecular function regulator activity, GO:0060090 molecular adaptor activity
- **localization:** GO:0005794 Golgi apparatus, GO:0005730 nucleolus, GO:0005635 nuclear envelope, GO:0005634 nucleus
- **pathway (Reactome):** R-HSA-5653656 Vesicle-mediated transport, R-HSA-168256 Immune System, R-HSA-162582 Signal Transduction, R-HSA-1266738 Developmental Biology
- **partners:** ARF1, ARL1, MYO9B, MYH9, FKBP13, CTNNB1, TRAF2, YWHAZ
- **complexes:** myosin phosphatase complex (myosin IIA / PP1δ / MYPT1), BIG1 homodimer/BIG-GBF1 dimer (DCB-HUS), PDE3A-containing AKAP complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 1999 | High | Human p200 ARF-GEP1 (ARFGEF1) is a Golgi-localized guanine nucleotide exchange factor whose Sec7 domain catalyzes GTP loading onto class I ARFs; brefeldin A acts as an uncompetitive inhibitor targeting the p200-ARF complex (Ki ~7 µM) rather than competing with ARF for p200 binding. Golgi localization signal maps to the N-terminal third of the protein. | PMID:10393931 | Proceedings of the National Academy of Sciences of the United States of America |
| 2003 | Medium | The N-terminal region (aa 1–331) of BIG1 interacts with FK506-binding protein 13 (FKBP13); this association was confirmed by co-immunoprecipitation of endogenous BIG1 and FKBP13 from Jurkat T cells. FK506 treatment increased membrane binding of BIG1, BIG2, and ARF to Golgi and other membranes. | PMID:12606707 | Proceedings of the National Academy of Sciences of the United States of America |
| 2004 | Medium | BIG1 localizes to nuclei (nuclear envelope/nucleoli) in serum-starved HepG2 cells independently of BIG2; nuclear BIG1 co-immunoprecipitates with nucleoporin p62 and nucleolin, but ARF is not detected in nuclear BIG1 immunoprecipitates, indicating independent nuclear functions distinct from Golgi ARF activation. | PMID:14973189 | Proceedings of the National Academy of Sciences of the United States of America |
| 2005 | High | BIG1 directly binds to the zinc finger/GAP domain of myosin IXb and inhibits myosin IXb RhoA-GAP activity (IC50 ~0.06 µM) by competing with RhoA for the same binding region on myosin IXb. | PMID:15644318 | The Journal of biological chemistry |
| 2006 | High | PKA-catalyzed phosphorylation of BIG1 at Ser-883 is required for cAMP-induced nuclear accumulation of BIG1; a functional nuclear localization signal (712KPK714) is also necessary. Microtubule integrity (nocodazole-sensitive) is required for translocation. BIG2 is not similarly regulated. | PMID:16467138 | Proceedings of the National Academy of Sciences of the United States of America |
| 2007 | High | PKA phosphorylates BIG1, significantly decreasing its GEF activity toward ARFs; protein phosphatase 1γ (but not PP1α, PP1β, or PP2A) reverses this phosphorylation and restores GEP activity. Endogenous PP1γ co-immunoprecipitates with BIG1 from microsomal fractions. Elevated cAMP induces PKA-catalyzed phosphorylation and nuclear accumulation of BIG1 but not BIG2. | PMID:17360629 | Proceedings of the National Academy of Sciences of the United States of America |
| 2007 | Medium | BIG1 is required for correct N-glycosylation of integrin β1 in the Golgi; BIG1 siRNA (but not BIG2 siRNA) causes aberrant electrophoretic mobility of β1, decreased active RhoA-GTP, impaired cell spreading, adhesion, and migration. Overexpression of HA-BIG1 restores RhoA-GTP levels. | PMID:17227842 | Proceedings of the National Academy of Sciences of the United States of America |
| 2007 | Medium | BIG1 and BIG2 form homodimers through interactions between their conserved DCB domains; within each homodimer the DCB domain also interacts with the HUS domain via the HUS box. Both DCB and HUS domains are necessary for GBF1 dimerization in mammalian cells; the DCB domain is essential for yeast viability. | PMID:17640864 | The Journal of biological chemistry |
| 2008 | Medium | BIG1 in nuclei of HepG2 cells associates with nucleolin, U3 snoRNA, and fibrillarin, dependent on nucleic acids (RNase A/DNase-sensitive); BIG1 and nucleolin also associate with nucleoporin p62 at the nuclear envelope, suggesting BIG1 participates in dynamic nucleolar complexes. | PMID:18292223 | Proceedings of the National Academy of Sciences of the United States of America |
| 2008 | Medium | BIG1 and BIG2 play redundant roles in membrane trafficking between the TGN and endosomes, including retrograde transport of furin from late endosomes to the TGN and maintenance of localization of TGN/recycling endosome proteins; this overlaps functionally with AP-1 clathrin adaptor activity. | PMID:18417613 | Molecular biology of the cell |
| 2009 | Medium | PDE3A interacts with BIG1 and BIG2 as part of AKAP complexes; depletion or inhibition of PDE3A disperses BIG1/BIG2 from the perinuclear Golgi and decreases membrane-associated ARF1-GTP, suggesting PDE3A limits local cAMP to prevent PKA-mediated inhibition of BIG1/BIG2 GEF activity. | PMID:19332778 | Proceedings of the National Academy of Sciences of the United States of America |
| 2010 | Medium | BIG1 (but not BIG2) depletion causes fragmentation of the Golgi apparatus into mini-stacks that remain polarized and functional for cargo export, demonstrating a non-redundant role for BIG1 in maintaining normal Golgi morphology. | PMID:20360857 | PloS one |
| 2012 | High | The Arf-like GTPase Arl1 directly binds the N-terminal region of BIG1/BIG2 (via their Drosophila ortholog Sec71) and is necessary for Golgi recruitment of BIG1 and BIG2 (but not GBF1) to the trans-Golgi in mammalian cells. | PMID:22291037 | The Journal of cell biology |
| 2012 | Medium | BIG1 associates with ABCA1 in vesicle preparations from rat liver; BIG1 depletion reduces surface ABCA1, inhibits its internalization and recycling, and decreases cholesterol efflux by ~60%. These effects depend on BIG1 GEF activity and ARF1 activation. | PMID:23220274 | Arteriosclerosis, thrombosis, and vascular biology |
| 2013 | Medium | GBF1-activated ARF4 and ARF5 (but not ARF3) facilitate recruitment of BIG1 and BIG2 to the TGN, defining a functional GEF cascade where GBF1 at the TGN acts upstream of BIG1/BIG2 recruitment. GBF1 localizes ultrastructurally to pre-Golgi, Golgi, and TGN. | PMID:23386609 | The Journal of biological chemistry |
| 2013 | High | BIG1 and BIG2 form complexes with nonmuscle myosin IIA independently of their GEF catalytic activity (C-terminal sequences suffice for interaction); selective depletion of BIG1 or BIG2 enhances phosphorylation of myosin regulatory light chain (T18/S19) and F-actin content, impairing cell migration. BIG1/BIG2 scaffold myosin phosphatase complexes (including myosin IIA, PP1δ, and MYPT1) to regulate myosin IIA activity. | PMID:23918382 | Proceedings of the National Academy of Sciences of the United States of America |
| 2013 | Medium | BIG1 directly binds GABAA receptor subunits and is required for their trafficking to the neuronal cell surface via its GEF activity; BIG1 depletion or dominant-negative BIG1-E793K expression reduces surface GABAAR and suppresses GABA-gated chloride influx. | PMID:24198228 | Molecular neurobiology |
| 2013 | Medium | BIG1 GEF activity regulates neurite development via PI3K-AKT signaling (GEF-activity-dependent) and ERK signaling (partially GEF-activity-independent); BIG1 colocalizes with synaptophysin and its expression increases during rat brain development. | PMID:24090963 | Neuroscience |
| 2016 | Medium | BIG1 directly interacts with β-catenin via its N-terminal sequence; depletion of BIG1 and/or BIG2 or GEF-inactive mutant expression causes β-catenin accumulation at perinuclear Golgi and reduces PKA-phosphorylated β-catenin (S675). BIG2 AKAP-C sequence is required for PKA-mediated S675 phosphorylation and β-catenin transcription coactivator function. Effects require phospholipase D activity and vesicular trafficking. | PMID:27162341 | Proceedings of the National Academy of Sciences of the United States of America |
| 2016 | Medium | BIG1 is required for recruitment of TRAF2 to TNFR1 signaling complex (complex I) and to the death-inducing signaling complex (complex II) after TNF-α stimulation; BIG1 knockdown attenuates TNF-α-induced TRAF2 ubiquitination and JNK activation, and increases apoptosis sensitivity. | PMID:27834853 | International journal of molecular sciences |
| 2017 | Medium | BIG1 loss in mice causes apoptosis of Tbr1+/Ctip2+ deep-layer neurons in a spatial-temporal pattern, impairs neuronal polarization in vitro, renders neurons hypersensitive to glutamate-induced apoptosis, and causes ectopic corticothalamic axon projections and failure of thalamocortical axons to cross the DTB. | PMID:28414797 | PloS one |
| 2018 | High | BIG1/Arfgef1 and its effector Arf1 are required for initiation of myelination by Schwann cells; Schwann cell-specific BIG1 conditional KO mice show reduced myelin thickness and decreased myelin protein zero (P0) in the myelin membrane. BIG1 KO specifically reduces Arf1 association with AP-1 clathrin adaptor subunits (but not GGA1 or COPI), indicating AP-1-dependent trafficking is the relevant effector pathway. | PMID:29740613 | Science advances |
| 2019 | Medium | Arfgef1 haploinsufficiency in mice alters neuronal endosome composition (altered ratio of Arf6+:Rab11+:TrfR+ recycling endosomes) and reduces dendritic surface and synaptic GABAA receptor levels (with increased lysosomal targeting), resulting in decreased seizure threshold but no spontaneous seizures. | PMID:31678406 | Neurobiology of disease |
| 2020 | Medium | BIG1 promotes macrophage pro-inflammatory responses in sepsis via ARF3 activation, which stimulates PIP5K-mediated PI(4,5)P2 synthesis and TIRAP recruitment to the plasma membrane, thereby activating TLR4-MyD88 signaling. Myeloid-specific BIG1 cKO reduces sepsis mortality and organ damage. | PMID:32415087 | Cell death & disease |
| 2022 | Medium | 14-3-3ζ interacts with both GABAA receptor β subunit and BIG1 in vitro and in vivo (hippocampal neurons); overexpression of 14-3-3ζ increases BIG1 surface expression and BIG1–GABAAR interaction, while 14-3-3ζ depletion reduces surface expression of both BIG1 and GABAAR and suppresses GABA-gated chloride influx. | PMID:36562883 | Molecular neurobiology |
| 2022 | Medium | KLF4 transcriptionally activates BIG1 (ARFGEF1) by binding its promoter (confirmed by ChIP-qPCR and dual-luciferase reporter assay); BIG1 mediates LPS-induced microglial neuroinflammation and migration via the PI3K/Akt/NF-κB pathway. | PMID:35090882 | Neuroscience |

## Citations

- PMID:10393931
- PMID:12606707
- PMID:14973189
- PMID:15644318
- PMID:16467138
- PMID:17227842
- PMID:17360629
- PMID:17640864
- PMID:18292223
- PMID:18417613
- PMID:19332778
- PMID:20360857
- PMID:22291037
- PMID:23220274
- PMID:23386609
- PMID:23918382
- PMID:24090963
- PMID:24198228
- PMID:27162341
- PMID:27834853
- PMID:28414797
- PMID:29740613
- PMID:31678406
- PMID:32415087
- PMID:35090882
- PMID:36562883
