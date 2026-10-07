---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ARHGEF28
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q8N1W1
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 20
citation_count: 20
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ARHGEF28 (human)

## Current model (mechanistic narrative)

ARHGEF28 (RGNEF/p190RhoGEF) is a bifunctional 190 kDa protein that couples RhoA-specific guanine nucleotide exchange to RNA binding, integrating cytoskeletal signaling at focal adhesions with post-transcriptional control in neurons [PMID:11058585, PMID:11435431]. Its tandem DH/PH module catalyzes RhoA-specific GDP release in vitro while sparing Rac1 and Cdc42, and the full-length protein is autoinhibited until binding partners unmask activity [PMID:11058585]; crystallography shows that activated RhoA·GTP and Rac1·GTP dock onto the same hydrophobic surface of its PH domain to recruit the enzyme to substrate RhoA·GDP, generating both positive feedback and Rac→Rho cross-talk [PMID:29196061]. Downstream of integrins and GPCRs, ARHGEF28 forms a scaffold with FAK through its C-terminal coiled-coil binding the FAK FAT domain [PMID:12702722, PMID:21224360], and genetic knockout establishes it as essential for RhoA activation, focal adhesion formation, and migration after fibronectin stimulation [PMID:22649559]; this scaffolding role promotes FAK-Y397 autophosphorylation and peripheral adhesion assembly in a PH-domain-dependent but GEF-activity-independent manner, whereas its GEF activity separately drives paxillin-Y118 phosphorylation [PMID:24006257]. It is an effector of Gα13 downstream of gastrin/CCK2 receptor signaling [PMID:25922072] and supports NF-κB-dependent transcriptional programs in tumor and bone contexts [PMID:31308489, PMID:41571890]. As an RNA-binding protein, its C-terminal domain binds the destabilizing element of NF-L mRNA to extend its half-life, a site also engaged by BC1 RNA [PMID:11435431, PMID:12215442]. The protein additionally engages TDP-43 RNA-recognition motifs through an N-terminal IPT/TIG-containing fragment, and ARHGEF28 and TDP-43 act antagonistically to regulate splicing of long introns in axon-guidance genes [PMID:38739752, PMID:39360635].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0003723 RNA binding, GO:0060090 molecular adaptor activity, GO:0098772 molecular function regulator activity, GO:0008092 cytoskeletal protein binding
- **localization:** GO:0005829 cytosol, GO:0005634 nucleus, GO:0005856 cytoskeleton
- **pathway (Reactome):** R-HSA-162582 Signal Transduction, R-HSA-1474244 Extracellular matrix organization, R-HSA-8953854 Metabolism of RNA, R-HSA-1643685 Disease
- **partners:** PTK2/FAK, GNA13, YWHAH, YWHAE, CTNND2, TARDBP, RHOA, RAC1
- **complexes:** Rgnef-FAK scaffold complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2000 | High | The isolated tandem DH/PH domain of p190RhoGEF activates RhoA in vitro (GDP release and protein binding assays), but not Rac1 or Cdc42, establishing RhoA-specific GEF activity. Full-length p190RhoGEF fails to activate RhoA in vitro, suggesting autoinhibition requiring unknown binding partners to unmask exchange activity in vivo. p190RhoGEF directly interacts with microtubules via its C-terminal region adjacent to the DH/PH domain, shown by in vitro and in vivo binding experiments. | PMID:11058585 | The Journal of biological chemistry |
| 2003 | High | FAK directly interacts with p190RhoGEF in neuronal cells and brain tissue extracts. The FAK C-terminal focal adhesion targeting (FAT) domain binds the C-terminal coiled-coil domain of p190RhoGEF, identified by two-hybrid assay and deletion mutagenesis. A FAK FAT domain mutation (Leu-1034 to Ser) disrupts this interaction. FAK activity promotes p190RhoGEF tyrosine phosphorylation and RhoA GTP loading downstream of laminin/integrin and IGF-1 receptor stimulation. | PMID:12702722 | The Journal of biological chemistry |
| 2001 | High | 14-3-3η and 14-3-3ε are binding partners of p190RhoGEF, identified by yeast two-hybrid screen and confirmed biochemically by co-immunoprecipitation and co-localization. A phosphorylation-independent binding site (I1370QAIQNL) in p190RhoGEF was mapped; deletion of this site abolishes 14-3-3η interaction in vitro and prevents 14-3-3η-mediated alteration of p190RhoGEF cytoplasmic aggregation in cells. | PMID:11533041 | The Journal of biological chemistry |
| 2001 | High | p190RhoGEF binds directly and specifically to the 68-nucleotide destabilizing element in the 3' UTR of NF-L (neurofilament light) mRNA via its C-terminal domain (clone 39), demonstrated by Northwestern blot, gel-shift, and cross-linkage assays. Expression of p190RhoGEF in stably transfected neuronal cells increased the half-life of wild-type NF-L mRNA but not of a mutant lacking the destabilizing element, establishing a functional role in NF-L mRNA stability. | PMID:11435431 | The Journal of biological chemistry |
| 2002 | Medium | BC1 RNA (a neuronally expressed non-coding RNA) binds to the same C-terminal site of p190RhoGEF as NF-L mRNA and competes with NF-L mRNA for p190RhoGEF binding, identified by affinity chromatography and cross-competition experiments using a GST-p190RhoGEF C-terminal fusion protein. | PMID:12215442 | The Journal of biological chemistry |
| 2003 | Medium | Anti-apoptotic activity of p190RhoGEF is localized to two cytoplasmic retention sequences (CRS-1 and CRS-2) in its C-terminal region that overlap with the JIP-1 and 14-3-3 binding sites. Deleting both CRS sequences abolishes cytoplasmic retention and anti-apoptotic activity of EGFP-tagged p190RhoGEF in Neuro 2a cells; restoring either CRS-1 or CRS-2 rescues both properties. | PMID:14499478 | Brain research. Molecular brain research |
| 2003 | Medium | p190RhoGEF expression is induced by CD40 stimulation in WEHI 231 B cells. Overexpression of p190RhoGEF mimics CD40-stimulated cellular structure changes and NF-κB activation through RhoA; these effects are blocked by dominant-negative RhoA (T19N) or dominant-negative p190RhoGEF (Y1003A). | PMID:12496377 | Journal of immunology |
| 2008 | Medium | delta-Catenin interacts with p190RhoGEF in the cytoplasm at low cell density, reducing RhoA activity. At high cell density, E-cadherin outcompetes p190RhoGEF for delta-catenin binding, shifting delta-catenin to the plasma membrane and restoring RhoA activity. Ectopic E-cadherin expression in mouse embryonic fibroblasts decreased delta-catenin's effect on RhoA activity reduction. | PMID:18930028 | Biochemical and biophysical research communications |
| 2010 | Medium | Human RGNEF (the human homologue of p190RhoGEF) directly interacts with human NFL mRNA in vitro by gel-shift assay. In tissue lysates, RGNEF-NFL mRNA interaction was detected by IP-RT-PCR only in ALS patient samples, not in neuropathologically normal controls. | PMID:19488899 | Amyotrophic lateral sclerosis |
| 2011 | High | Rgnef forms a complex with FAK in human colon carcinoma cells. Upon gastrin stimulation, Rgnef-FAK interaction is required for FAK translocation to focal adhesions, paxillin tyrosine phosphorylation, cell motility, and invadopodia formation. Overexpression of the Rgnef C-terminal region (aa 1279–1582) disrupts endogenous Rgnef-FAK interaction and blocks these events; a version lacking the FAK binding site (aa 1302–1582) does not. Rgnef-C-expressing cells form smaller, less invasive tumors in vivo. | PMID:21224360 | Cancer research |
| 2012 | High | Genetic knockout of Rgnef in mouse embryo fibroblasts (Rgnef-/- MEFs) significantly inhibits haptotaxis migration, wound closure motility, focal adhesion number, and RhoA GTPase activation after fibronectin-integrin stimulation. These phenotypes are rescued by epitope-tagged Rgnef re-expression, establishing Rgnef as essential for RhoA regulation downstream of integrins. | PMID:22649559 | PloS one |
| 2013 | High | Rgnef plays a non-canonical, upstream scaffolding role in promoting FAK localization to peripheral adhesions and FAK-Y397 activation upon fibronectin binding, independent of its GEF catalytic activity. A PH domain mutation in Rgnef blocks adhesion formation, FAK localization, and FAK/paxillin phosphorylation without disrupting the Rgnef-FAK interaction. A GEF-inactive Rgnef mutant rescues FAK-Y397 phosphorylation and adhesion localization but not paxillin-Y118 phosphorylation, indicating paxillin-pY118 requires Rgnef GEF activity through a distinct mechanism. | PMID:24006257 | Journal of cell science |
| 2015 | High | Rgnef is a new effector for Gα13 downstream of gastrin and the CCK2 receptor in DLD-1 colon carcinoma cells. Rgnef co-immunoprecipitates with activated Gα13Q226L but not Gα12Q229L; the Rgnef C-terminal region (aa 1279–1582) is sufficient for this interaction and its exogenous expression blocks Gα13-stimulated SRE activity. Point mutations in the Rgnef C-terminal region disrupt Gα13 association but not Gαq association. Gα13 depletion reduces gastrin-induced FAK-pY397 and paxillin-pY31. | PMID:25922072 | The Journal of biological chemistry |
| 2017 | High | Crystal structures reveal that activated Rac1·GTP and RhoA·GTP use their effector-binding surfaces to associate with the same hydrophobic surface on the p190RhoGEF PH domain. Both activated RhoA and Rac1 stimulate nucleotide exchange on RhoA·GDP by p190RhoGEF in vitro, localizing it to its substrate. This demonstrates a positive feedback (activated RhoA) and a cross-talk mechanism (activated Rac1 directly stimulates RhoA activation through p190RhoGEF). | PMID:29196061 | Journal of structural biology |
| 2017 | Medium | RGNEF expression is upregulated in murine spinal motor neurons following distal sciatic nerve injury. Under cellular stress (sodium arsenite or sorbitol), RGNEF expression confers a survival benefit in HEK293T cells; the NH2-terminus domain is essential for this protective effect. Under stress, RGNEF associates with Staufen1-positive granules but not TIA-1-positive stress granules. | PMID:28495450 | Molecular and cellular neurosciences |
| 2018 | Medium | A 23-amino acid bipartite nuclear localization signal (NLS) within the Pleckstrin Homology (PH) domain of RGNEF controls its nuclear localization; deletion or mutation of this region abolishes nuclear localization. Within this NLS, an overlapping nuclear export signal (NES) promotes nuclear export in an exportin-1-dependent manner (confirmed by Leptomycin B treatment). The PH domain alone is sufficient to translocate a 160 kDa fusion protein to the nucleus. | PMID:30482479 | European journal of cell biology |
| 2019 | Medium | Rgnef is essential for ovarian tumor spheroid formation in vitro and tumor growth in vivo using transgenic and transplantable Rgnef knockout mouse models. Rgnef supports an NF-κB-mediated antioxidant gene signature (including Gpx4, Nqo1, Gsta4); antioxidant treatment rescues growth of Rgnef-knockout spheroids, and Rgnef re-expression facilitates NF-κB-dependent tumorsphere survival. | PMID:31308489 | Oncogene |
| 2024 | High | An N-terminal fragment of RGNEF (NF242) directly interacts with the RNA recognition motifs (RRMs) of TDP-43, competing with RNA binding. The IPT/TIG domain of NF242 is essential for this interaction. In a Drosophila ALS model overexpressing TDP-43, genetic expression of NF242 suppressed neuropathological phenotypes (increased lifespan, abolished motor defects, prevented neurodegeneration). Intracerebroventricular injection of AAV9/NF242 in a murine TDP-43 model (rNLS8) improved lifespan and motor phenotype and decreased neuroinflammation markers. | PMID:38739752 | Brain : a journal of neurology |
| 2024 | Medium | RGNEF and TDP-43 act predominantly in an antagonistic manner to regulate expression of axon guidance genes in neuronal cells. Mechanistically, both factors affect the processivity of long intron removal (splicing), explaining their mode of transcriptomic action upon depletion. | PMID:39360635 | FASEB journal |
| 2026 | Medium | Rgnef promotes osteoclastogenesis and attenuates osteoblastogenesis through activation of RhoA and Rac1, leading to enhanced NF-κB, MAPK, and AKT signaling. Rgnef-deficient mice show increased bone mass due to reduced osteolysis and increased osteogenesis, while Rgnef-overexpressing mice show the opposite. Rgnef-deficient mice are protected from bone loss in LPS-induced inflammation and ovariectomy models. | PMID:41571890 | Experimental & molecular medicine |

## Citations

- PMID:11058585
- PMID:11435431
- PMID:11533041
- PMID:12215442
- PMID:12496377
- PMID:12702722
- PMID:14499478
- PMID:18930028
- PMID:19488899
- PMID:21224360
- PMID:22649559
- PMID:24006257
- PMID:25922072
- PMID:28495450
- PMID:29196061
- PMID:30482479
- PMID:31308489
- PMID:38739752
- PMID:39360635
- PMID:41571890
