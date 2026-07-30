---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ABR
affinage_run_date: 2026-06-09T22:02:37
uniprot_accession: Q12979
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 15
citation_count: 15
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ABR (human)

## Current model (mechanistic narrative)

ABR is a dual-function regulator of Rho-family GTPase signaling that carries both a Dbl-homology guanine-nucleotide exchange factor (GEF) domain and a C-terminal GTPase-activating protein (GAP) domain within a single polypeptide [PMID:8349582, PMID:7479768]. Biochemical reconstitution established that its GEF domain stimulates GTP loading of CDC42, RhoA, Rac1, and Rac2 (rank order CDC42 > RhoA > Rac1 = Rac2) while its GAP domain selectively inactivates Rac1, Rac2, and CDC42 but not RhoA or Ras, with each domain binding substrate non-competitively [PMID:7479768]. In vivo, ABR acts predominantly as a negative regulator of Rac: it is redundant with its paralog BCR, and combined loss in mice elevates active Rac1 and downstream p38 MAPK signaling, producing cerebellar developmental defects in glia [PMID:11684658], dysregulated macrophage morphology, motility, and phagocytosis with sustained Rac activation [PMID:17116687], excessive neutrophil ROS and protease output [PMID:19703997], and pulmonary vascular remodeling under hypoxia [PMID:23152932]. ABR enforces spatial control of GTPase activity: in single-cell wound repair it is recruited to the active-Rho zone through binding GTP-bound Rho, where it locally amplifies Rho via its GEF domain and restricts Cdc42 via its GAP domain to keep the two activity zones segregated [PMID:21295482], and it transiently translocates to the plasma membrane and phagosomes upon CSF-1 stimulation [PMID:17116687]. At excitatory synapses ABR binds the scaffold PSD-95 and constrains basal Rac1 activity to support long-term potentiation maintenance and memory [PMID:20962234], and in CD4+ T cells it deactivates Rac to limit chemotaxis and allergic airway responses [PMID:24058174]. ABR additionally supports phagocytosis in trabecular meshwork cells via an integrin/RAC1 pathway [PMID:31516309], osteoclast differentiation and bone resorption through interaction with PARG and Rho GTPases [PMID:37507586], mitotic fidelity and centrosome dynamics in human embryonic stem cells [PMID:28579391], and hyperglycaemia-driven RhoA activation and actin organization in feto-placental endothelium [PMID:38776074]. ABR is also the host target of the bacterial effector EspH, which binds the ABR GAP domain to hijack Rac1 and Cdc42 signaling [PMID:36219160].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0140096 catalytic activity, acting on a protein, GO:0098772 molecular function regulator activity, GO:0060089 molecular transducer activity
- **localization:** GO:0005886 plasma membrane, GO:0031410 cytoplasmic vesicle, GO:0005815 microtubule organizing center
- **pathway (Reactome):** R-HSA-162582 Signal Transduction, R-HSA-168256 Immune System, R-HSA-1640170 Cell Cycle
- **partners:** BCR, PSD-95, RHOA, RAC1, CDC42, PARG, ESPH
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 1989 | Medium | ABR (Active BCR-Related) was identified as a functionally active gene on chromosome 17p, distinct from BCR on chromosome 22, encoding a protein with exons similar to those in the BCR major breakpoint cluster region. | PMID:2587217 | Nucleic acids research |
| 1993 | High | ABR encodes a protein with a DBL-homology (GEF) domain and a GAP domain; the GAP domain expressed as a recombinant fusion protein in E. coli demonstrated in vitro GTPase-activating protein (GAP) activity specifically toward Rac (not Rho, Rap1A, or Ha-Ras). | PMID:8349582 | The Journal of biological chemistry |
| 1995 | High | Purified recombinant Abr Dbl-homology (GEF) domain stimulated GTP binding to CDC42Hs, RhoA, Rac1, and Rac2 (rank order CDC42Hs > RhoA > Rac1 = Rac2) but was inactive toward Rap1A and Ha-Ras. The GAP domain was active toward Rac1, Rac2, and CDC42Hs but inactive toward RhoA, Rap1A, and Ha-Ras. Each domain bound non-competitively to GTP-binding protein substrates, suggesting simultaneous or sequential interactions. | PMID:7479768 | Proceedings of the National Academy of Sciences of the United States of America |
| 2001 | High | Simultaneous genetic disruption of Abr and Bcr in mice causes postnatal cerebellar development defects including granule cell ectopia and foliation defects, linked to structural and functional abnormalities of Bergmann glia and astroglia. Double-null astroglia showed constitutively increased p38 MAPK phosphorylation (a Rac-regulated pathway), hyper-responsiveness to EGF and LPS stimulation, and abnormal morphology, establishing Abr and Bcr as negative regulators of Rac in glial cells in vivo. | PMID:11684658 | Development (Cambridge, England) |
| 2006 | High | Genetic ablation of both Abr and Bcr in murine macrophages causes multiple Rac-dependent phenotypes: atypical elongated morphology, increased CSF-1-directed motility, and increased phagocytosis of opsonized particles with sustained Rac activation. In response to CSF-1 stimulation, Abr and Bcr transiently translocate to the plasma membrane. GAP-domain mutant Abr and Bcr reproduced the morphology phenotype and localized around phagosomes, inducing distinct phagocytic cup formation. | PMID:17116687 | Molecular and cellular biology |
| 2009 | High | Abr and Bcr cooperate as negative regulators of Rac in innate immune cells; mice lacking both proteins show excessive neutrophil ROS, myeloperoxidase (MPO), and elastase production, and increased monocyte MMP9 secretion during experimental endotoxemia, demonstrating that Abr normally curbs specific effector functions of mature tissue innate immune cells. | PMID:19703997 | Molecular and cellular biology |
| 2010 | High | ABR and BCR localize at excitatory synapses and directly interact with PSD-95, a postsynaptic scaffolding protein, as shown by co-immunoprecipitation. Mice deficient for ABR or BCR show enhanced basal Rac1 activity, decreased maintenance (but not induction) of long-term potentiation, and impaired spatial and object recognition memory. | PMID:20962234 | The Journal of neuroscience : the official journal of the Society for Neuroscience |
| 2011 | High | In Xenopus single-cell wound repair, Abr is targeted to the Rho activity zone via interaction with active (GTP-bound) Rho. Within this zone, Abr promotes local Rho activation via its GEF domain and limits Cdc42 activity via its GAP domain, enforcing sharp segregation of Rho and Cdc42 activity zones. Depletion of Abr attenuates Rho activity and impairs wound repair. | PMID:21295482 | Current biology : CB |
| 2012 | High | Abr and Bcr function as negative regulators of Rac1 in pulmonary arterial smooth muscle cells and macrophages; mice lacking Abr or Bcr develop increased right ventricular pressure, pulmonary vascular remodeling, and perivascular leukocyte infiltration under hypoxia. Loss of Abr/Bcr leads to elevated activated Rac1, phosphorylated p38, and IL-6 in smooth muscle cells under hypoxia, and Rac1 inhibition rescued proliferation and signaling. | PMID:23152932 | PloS one |
| 2013 | High | Abr deactivates Rac in CD4+ T cells; abr-null mice exposed to cockroach allergen develop fatal asthma with increased Th2 cytokines (IL-4, IL-5), elevated IgE, and eosinophil infiltration. Adoptive transfer of abr-null CD4+ T cells into wild-type hosts recapitulated increased airway resistance, and abr-null CD4+ T cells showed elevated GTP-bound Rac and enhanced chemotaxis toward CCL21. | PMID:24058174 | Journal of immunology (Baltimore, Md. : 1950) |
| 2017 | Medium | ABR is required for mitotic fidelity in human embryonic stem cells (hESCs); ABR depletion compromises centrosome dynamics, predisposes cells to chromosome misalignment and missegregation, and raises aneuploidy frequency. This function is independent of direct effects on cell survival when cell-cell contact is intact. | PMID:28579391 | Stem cell reports |
| 2019 | Medium | ABR knockdown using siRNA in human trabecular meshwork cells decreased phagocytosis by ~40%, placing ABR in an αvβ5 integrin/RAC1-mediated engulfment pathway. DEX treatment downregulated ABR mRNA, suggesting glucocorticoid-induced inhibition of phagocytosis is partly mediated through reduced ABR expression. | PMID:31516309 | Molecular vision |
| 2022 | High | The bacterial effector EspH interacts with ABR via ABR's GAP domain (targeted by EspH's C-terminal 38 amino acid segment), suppressing Rac1 and Cdc42 activity, host cell cytotoxicity, bacterial invasion, and filopodium formation. ABR knockdown abolished EspH's ability to suppress Rac1 and Cdc42, establishing ABR as the host target through which EspH hijacks RhoGTPase signaling. | PMID:36219160 | Gut microbes |
| 2023 | Medium | Abr protein interacts with poly(ADP-ribose) glycohydrolase (PARG) and with RhoA, Rac1/2/3, and Cdc42 in osteoclasts. Abr knockdown suppressed osteoclast differentiation, bone resorption, and lamellipodia formation; Abr overexpression enhanced multinucleated osteoclast formation, bone resorption, actin ring formation, and upregulated osteoclast marker genes (Nfatc1, c-fos, Src, Ctsk). A variant of the Abr gene was identified in osteoclasts. | PMID:37507586 | Molecular biology reports |
| 2024 | Medium | ABR functions as a RhoA activator (GEF activity toward RhoA) in feto-placental arterial endothelial cells; ABR is epigenetically programmed by gestational diabetes mellitus (GDM) via altered DNA methylation and is upregulated by in vitro hyperglycaemia. ABR silencing in GDM-exposed cells reduced RhoA activity by ~34% and restored normal cell morphology, identifying ABR as a glucose-sensitive regulator of actin organization and cell shape. | PMID:38776074 | The Journal of physiology |

## Citations

- PMID:11684658
- PMID:17116687
- PMID:19703997
- PMID:20962234
- PMID:21295482
- PMID:23152932
- PMID:24058174
- PMID:2587217
- PMID:28579391
- PMID:31516309
- PMID:36219160
- PMID:37507586
- PMID:38776074
- PMID:7479768
- PMID:8349582
