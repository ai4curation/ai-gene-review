---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ARPC5
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: O15511
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 14
citation_count: 14
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ARPC5 (human)

## Current model (mechanistic narrative)

ARPC5 (p16-Arc) is the smallest subunit of the Arp2/3 actin-nucleation complex, and within that complex its N-terminal tail functions as an autoinhibitory element whose release upon nucleation-promoting-factor binding to Arp2 is allosterically coupled to complex activation, with closure of the Arp2 ATP-binding cleft and rotation toward the active conformation [PMID:40042350]. Mammalian cells contain two compositionally distinct Arp2/3 complexes built around the ARPC5 and ARPC5L isoforms, both incorporated into native complexes purified from neutrophils [PMID:12451597], and these isoforms carry out divergent cellular functions: ARPC5-containing complexes stabilize ArpC1 at actin branch junctions, position Ena/VASP proteins at the leading edge, and shape protrusion dynamics during migration [PMID:36662867], drive cytoplasmic actin dynamics after TCR stimulation while ARPC5L specifically mediates nuclear actin polymerization through a calcium-calmodulin-N-WASP pathway [PMID:37162507]. ARPC5 activity is set post-translationally by phosphorylation: MAPKAPK2 phosphorylates the A isoform at Ser-77 [PMID:12829704], and PKC phosphorylation is required for rear MTOC polarization and directional migration [PMID:21281821]. Biallelic null mutations in ARPC5 disrupt Arp2/3 complex conformation and selectively impair IL-6 classical signaling, with re-expression rescuing complex function, defining ARPC5 deficiency as a cause of human disease [PMID:37349293]. Beyond its structural role in actin nucleation, ARPC5 has an unconventional function as a translational suppressor in male germ cells, where it blocks 80S ribosome formation and routes mRNAs into chromatoid/P bodies, a microRNA-controlled activity required for normal spermatid differentiation and fertility [PMID:22447776].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0005198 structural molecule activity, GO:0008092 cytoskeletal protein binding, GO:0045182 translation regulator activity
- **localization:** GO:0005856 cytoskeleton, GO:0005829 cytosol, GO:0005634 nucleus
- **pathway (Reactome):** R-HSA-168256 Immune System, R-HSA-162582 Signal Transduction
- **partners:** ARPC1, TAGLN2, CPEB2
- **complexes:** Arp2/3 complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2003 | High | MAPKAPK2 (MK2) directly phosphorylates the A isoform (ARPC5A/p16-Arc) but not the B isoform of ARPC5 at serine-77; mutation of Ser-77 to alanine abolishes phosphorylation. MAPKAPK2 also phosphorylates ARPC5 within intact Arp2/3 complexes precipitated from neutrophil lysates. | PMID:12829704 | The Journal of biological chemistry |
| 2003 | High | ARPC5 exists as two isoforms (ARPC5A and ARPC5B) that are both incorporated into the Arp2/3 complex purified from human neutrophils, demonstrating that mammalian cells contain multiple compositionally distinct Arp2/3 complexes. Both isoforms co-localize with Arp2/3 complex in C2C12 cells when myc-tagged. | PMID:12451597 | Cell motility and the cytoskeleton |
| 2011 | High | PKC phosphorylates ARPC5 in neointimal smooth muscle cells, and this phosphorylation is required for rear polarization of the MTOC. A non-phosphorylatable ARPC5 mutant abolishes rear MTOC polarization and directional migration of neointimal SMCs, linking ARPC5 phosphorylation to cytoskeletal organization underlying cell polarity. | PMID:21281821 | The American journal of pathology |
| 2012 | Medium | ARPC5 is a direct target of miR-133a; luciferase reporter assay confirmed direct binding. Silencing ARPC5 inhibits cell migration and invasion in HNSCC lines and causes reorganization of the actin cytoskeleton to a round, bleb-like morphology. | PMID:22378351 | International journal of oncology |
| 2012 | High | ARPC5 functions as a broadly acting translational suppressor in male germ cells: it inhibits translation initiation by blocking 80S ribosome formation and facilitates transport of mRNAs to chromatoid/P bodies. Loss of microRNA-dependent regulation of Arpc5 disrupts sequestration of germ cell mRNAs into translationally inert ribonucleoprotein particles, resulting in abnormal round spermatid differentiation and impaired fertility. | PMID:22447776 | Proceedings of the National Academy of Sciences of the United States of America |
| 2023 | High | ARPC5 and ARPC5L isoforms differentially regulate Arp2/3 complex-dependent cell migration: both isoforms determine the structural stability of ArpC1 in actin branch junctions and influence protrusion characteristics and actin network ultrastructure. Additionally, ArpC5 isoforms differentially position Ena/VASP family proteins at the leading edge, and Ena/VASP mediates isoform-specific effects on actin assembly levels. | PMID:36662867 | Science advances |
| 2023 | High | ARPC5 and ARPC5L isoforms play distinct roles in CD4 T cells: ARPC5 drives cytoplasmic actin dynamics after TCR stimulation and mediates nuclear actin polymerization triggered by DNA replication stress, while ARPC5L specifically drives nuclear actin polymerization upon TCR stimulation via a calcium-calmodulin-N-WASP signaling pathway. | PMID:37162507 | eLife |
| 2023 | High | Germline biallelic null mutations in ARPC5 disrupt Arp2/3 complex conformation and function; reestablishment of ARPC5 expression in vitro rescues Arp2/3 complex conformation and functions. ARPC5 deficiency also selectively impairs IL-6 classical signaling but not IL-6 trans-signaling. | PMID:37349293 | Nature communications |
| 2025 | High | Cryo-EM structures at 2.9-Å resolution reveal that NPF binding to Arp2 is allosterically linked to the release of ArpC5's N-terminal tail from Arp2 and induces conformational changes in Arp2 including closure of its ATP-binding cleft and partial rotation/translation toward the active-complex position. This defines ArpC5's N-terminal tail as an inhibitory element whose release is part of the allosteric activation mechanism of Arp2/3 complex. | PMID:40042350 | Proceedings of the National Academy of Sciences of the United States of America |
| 2023 | Medium | KLF4 transcriptionally activates ARPC5 by binding to its promoter region, as demonstrated by chromatin immunoprecipitation and luciferase reporter assay. ARPC5 in turn upregulates ADAM17 as a downstream effector to promote prostate cancer cell migration and invasion. | PMID:36881291 | Apoptosis |
| 2023 | Medium | CPEB2 promotes ARPC5 mRNA stability through direct interaction, as shown by RNA immunoprecipitation and co-localization in the cytoplasm, and actinomycin D chase experiments demonstrating increased ARPC5 mRNA half-life when CPEB2 is expressed. | PMID:37231521 | Journal of orthopaedic surgery and research |
| 2024 | Medium | TAGLN2 (transgelin-2) physically interacts with ARPC5 and promotes its expression, activating the MEK/ERK signaling pathway to drive pancreatic cancer cell proliferation, invasion, and metastasis. Silencing ARPC5 reverses TAGLN2 overexpression-induced effects. | PMID:38744388 | Cellular signalling |
| 2024 | Medium | Arp2/3 complexes containing Arpc5 (but not the Arpc5l isoform) are required for macrophage phagocytosis and killing of intracellular bacteria; loss of Arpc5 in the murine hematopoietic system leads to failure of macrophages to restrict microbial invasion, causing intestinal inflammation and demonstrating an isoform-specific role for ARPC5-containing Arp2/3 complexes in innate immune defense. | PMID:bio_10.1101_2024.07.18.604111 | bioRxiv |
| 2024 | Medium | Arpc5-containing Arp2/3 complexes in the actomyosin cortex act as a gatekeeper for membrane availability required for t-tubule growth in muscle cells; disruption of Arpc5 leads to enlarged t-tubules and impaired synchronization between plasma membrane depolarization and calcium release, causing muscle fatigue. | PMID:bio_10.1101_2024.08.13.607563 | bioRxiv |

## Citations

- PMID:12451597
- PMID:12829704
- PMID:21281821
- PMID:22378351
- PMID:22447776
- PMID:36662867
- PMID:36881291
- PMID:37162507
- PMID:37231521
- PMID:37349293
- PMID:38744388
- PMID:40042350
- PMID:bio_10.1101_2024.07.18.604111
- PMID:bio_10.1101_2024.08.13.607563
