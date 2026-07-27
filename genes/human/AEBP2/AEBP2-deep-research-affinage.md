---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/AEBP2
affinage_run_date: 2026-06-09T22:02:42
uniprot_accession: Q6ZN18
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 24
citation_count: 24
gates_passed: True
note: >-
  Machine-fetched from the Affinage API (Cheeseman Lab). This is external
  precomputed research to be treated as a preliminary source, NOT a curated
  annotation. Affinage is human-only and LLM-generated; verify claims against
  the cited PMIDs before use.
---

# Affinage mechanistic annotation for AEBP2 (human)

## Current model (mechanistic narrative)

AEBP2 is a zinc-finger accessory subunit of Polycomb Repressive Complex 2 (PRC2) that modulates the deposition and genomic targeting of repressive H3K27 methylation [PMID:15225548, PMID:27317809, PMID:29628311]. First characterized as a zinc-finger DNA-binding transcriptional repressor acting at the aP2 promoter [PMID:10329662], AEBP2 was subsequently shown to enhance the histone methyltransferase activity of the EED-EZH2-SUZ12 core above its minimal baseline through a mechanism independent of and additive to H3K27me3-driven allosteric activation [PMID:15225548, PMID:29681498]. Together with JARID2, AEBP2 defines the PRC2.2 subcomplex, which is mutually exclusive and antagonistic to the PCL/PALI1-containing PRC2.1 assembly [PMID:29628311]. Structural studies place AEBP2 in contact with the RBBP4 subunit, where it mimics an unmodified H3 tail and progressively blocks H3K4 binding, and show that AEBP2 and JARID2 each engage a ubiquitin moiety and the H2A-H2B surface of H2AK119ub1 nucleosomes to stimulate methylation and partly override the inhibitory effect of active marks H3K4me3 and H3K36me3 [PMID:29348366, PMID:29499137, PMID:33479123]. This nucleosomal engagement is the structural basis of a positive feedback loop in which PRC1-deposited H2Aub recruits JARID2-AEBP2-PRC2 to establish H3K27me3 domains, a relationship demonstrated in vitro and through in vivo epistasis at zebrafish zygotic genome activation [PMID:24837194, PMID:34982026, PMID:36610636]. AEBP2 controls PRC2 genomic localization by binding the non-canonical SUZ12 C2 domain, where it competes with PHF19, disrupts the intrinsic PRC2 dimer, blocks C2-DNA contacts, and thereby regulates cooperative DNA looping and chromatin residence [PMID:29499137, PMID:29891558, PMID:31959557, PMID:32043141]. AEBP2 exists as two developmentally regulated isoforms with opposing effects on PRC2: the embryo-specific short isoform stimulates DNA binding and de novo repression, while the broadly expressed long isoform inhibits PRC2 DNA binding and methyltransferase activity through a recently evolved, negatively charged N-terminal region [PMID:41168462]. In vivo, Aebp2 is essential for embryogenesis and neural crest development, with knockouts co-occupying and regulating neural crest migration genes alongside PRC2 [PMID:21949878, PMID:27317809]. AEBP2 is itself a substrate of SCF-β-TrCP-mediated ubiquitin-proteasomal degradation, and its abundance influences cisplatin sensitivity in cancer cells [PMID:31864706].

## Affinage mechanism profile (its own GO/Reactome grounding)

_Recorded for reference. The AIGR evaluation found this grounding is coarse (collapses to general parents) and can contradict the narrative — do not import these GO ids directly; re-ground from the narrative + PMIDs._

- **molecular_activity:** GO:0003677 DNA binding, GO:0140110 transcription regulator activity, GO:0098772 molecular function regulator activity, GO:0060090 molecular adaptor activity, GO:0042393 histone binding
- **localization:** GO:0005634 nucleus, GO:0000228 nuclear chromosome
- **pathway (Reactome):** R-HSA-4839726 Chromatin organization, R-HSA-74160 Gene expression (Transcription), R-HSA-1266738 Developmental Biology
- **partners:** SUZ12, RBBP4, JARID2, EZH2, EED, PHF19
- **complexes:** PRC2, PRC2.2

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 1999 | High | AEBP2 is a zinc finger transcriptional repressor that binds to the AE-1 regulatory sequence in the aP2 gene promoter; the zinc finger motif plays a direct role in transcriptional repression (but not DNA binding), as mutation of a conserved histidine and flanking serine in the middle zinc finger abolished repression without affecting nuclear localization or DNA binding. | PMID:10329662 | The Journal of biological chemistry |
| 2004 | High | AEBP2 is required for optimal (but not minimal) histone methyltransferase activity of the EED-EZH2-SUZ12 PRC2 complex; the minimum active complex requires EZH2, EED, and SUZ12, while AEBP2 enhances enzymatic activity above this baseline. | PMID:15225548 | Molecular cell |
| 2009 | Medium | AEBP2 is an evolutionarily conserved zinc finger protein that binds DNA via a bipartite motif (CTT(N)15-23cagGCC), exists as two developmental-stage-specific isoforms (adult 51 kDa and embryo 32 kDa), and co-occupies genomic loci with SUZ12, functioning as a potential targeting factor for mammalian PRC2. | PMID:19293275 | Nucleic acids research |
| 2011 | High | In developing mouse embryos, Aebp2 is expressed mainly in neural crest-derived cells; homozygous Aebp2 knockout is embryonic lethal, and heterozygotes display neural crest defects (enlarged colon, hypopigmentation). ChIP analyses showed that AEBP2 and PRC2 co-occupy promoters of genes involved in neural crest cell migration and development, and expression of these genes is altered in Aebp2 heterozygotes. | PMID:21949878 | PloS one |
| 2012 | High | The first 3D electron microscopy structure of human PRC2 bound to cofactor AEBP2 revealed that AEBP2 stabilizes the complex and occupies a position suggesting an allosteric role in regulating gene silencing; cross-linking mass spectrometry and internal protein tagging localized all PRC2 subunits and mapped AEBP2 interactions within the assembly. | PMID:23110252 | eLife |
| 2014 | High | Monoubiquitination of histone H2A by PRC1 (H2Aub) creates a binding site for Jarid2-Aebp2-containing PRC2, promoting H3K27 trimethylation on H2Aub nucleosomes; Jarid2, Aebp2, and H2Aub constitute a positive feedback loop establishing H3K27me3 chromatin domains. | PMID:24837194 | Nature structural & molecular biology |
| 2014 | High | AEBP2 localizes specifically to PRC2 target loci including the inactive X chromosome; proteomic analysis confirmed AEBP2 associates exclusively with PRC2 complexes. In Aebp2 mutant ESCs, elevated H3K27 methylation at target loci was observed and atypical hybrid PRC2 subcomplexes assembled, suggesting AEBP2 normally defines mutually exclusive PRC2 subcomplex composition. Unexpectedly, homozygous Aebp2 mutant embryos display a Trithorax (anti-Polycomb) phenotype. | PMID:27317809 | Development (Cambridge, England) |
| 2014 | Medium | The somatic (long, 52 kDa) isoform of AEBP2 acts as a transcriptional activator for Jarid2, Aebp2, and Snai2 target genes, whereas the embryonic (short, 32 kDa) isoform acts as a transcriptional repressor for Snai2; the somatic form also enhances cell migration. AEBP2 binds its own promoter and the promoters of Jarid2 and Snai2 as shown by ChIP. | PMID:25451679 | Genomics |
| 2017 | Medium | The AEBP2 subunit of PRC2 regulates preferential binding of PRC2 to methylated DNA (CpG-rich sequences); inclusion of AEBP2 in the PRC2 complex mediates this specificity for methylated DNA. | PMID:29058709 | Nature structural & molecular biology |
| 2018 | High | Cryo-EM structures of human PRC2 with JARID2 and AEBP2 in basal and active states showed that AEBP2 interacts with the RBAP48 (RBBP4) subunit, mimicking an unmodified H3 tail. SUZ12 interacts with all other subunits; together these interactions define the complete architecture of the complex. | PMID:29348366 | Science (New York, N.Y.) |
| 2018 | High | AEBP2 and PHF19 compete for binding to the non-canonical C2 domain of SUZ12; AEBP2 and JARID2 together enable nucleosome binding by the PRC2 complex. Crystal structures show that SUZ12 contains two structural platforms defining distinct PRC2 holo-complex classes. AEBP2 progressively blocks histone H3K4 binding to RBBP4 together with SUZ12. | PMID:29499137 | Molecular cell |
| 2018 | High | AEBP2 stimulates both PRC2-EZH1 and PRC2-EZH2 methyltransferase activity through a mechanism that is independent of and additive to allosteric activation (by H3K27me3), distinguishing AEBP2-mediated stimulation from the allosteric pathway. | PMID:29681498 | Molecular cell |
| 2018 | High | AEBP2 and PCL homolog proteins make a major contribution to PRC2 chromatin binding in living human cells; SUZ12 separation-of-function mutants that cannot bind accessory proteins (including AEBP2) greatly reduce chromatin residence time of PRC2, as measured by single-particle tracking. | PMID:29891558 | Genes & development |
| 2018 | High | AEBP2 and JARID2 define the PRC2.2 subcomplex, which is mutually exclusive and antagonistic relative to the PRC2.1 subcomplex (containing PALI1/PCL proteins); the balance of PRC2.1 and PRC2.2 activities is required for appropriate regulation of polycomb target genes during differentiation. | PMID:29628311 | Molecular cell |
| 2019 | Medium | AEBP2 contains a non-canonical phosphodegron and is targeted for ubiquitylation and proteasomal degradation by the SCF-β-TrCP E3 ubiquitin ligase complex; failure to degrade AEBP2 confers cisplatin resistance in ovarian cancer cells. | PMID:31864706 | Biochemical and biophysical research communications |
| 2020 | High | AEBP2 binding to the C2 domain of SUZ12 disrupts the intrinsic PRC2 dimer (formed by domain swapping involving RBBP4 and the SUZ12 C2 domain), whereas MTF2/PHF19 stabilize the dimer; PRC2 dimerization enhances CpG island DNA binding, and loss of dimerization impairs H3K27me3 at developmental gene loci. | PMID:31959557 | Molecular cell |
| 2020 | Medium | PRC2 (five-subunit complex including AEBP2) bends DNA approximately 3-fold locally and mediates DNA looping via multiple PRC2 molecules binding cooperatively; AEBP2 regulates loop formation, in part by associating with the C2 domain of SUZ12 and blocking its DNA contact. | PMID:32043141 | Nucleic acids research |
| 2021 | High | Cryo-EM structure of PRC2 with JARID2 and AEBP2 bound to an H2AK119ub1-containing nucleosome revealed: JARID2 and AEBP2 each contact one ubiquitin moiety and the H2A-H2B surface; JARID2 stimulates PRC2 via interactions with EED and H2AK119-ubiquitin; AEBP2 has an additional scaffolding role. The presence of both cofactors partially overcomes the inhibitory effect of H3K4me3 and H3K36me3 on PRC2 activity. | PMID:33479123 | Science (New York, N.Y.) |
| 2021 | Medium | AEBP2 regulates cooperative DNA looping by multiple PRC2 complexes; the association of AEBP2 with the C2 domain of SUZ12 blocks C2-DNA contacts, providing a mechanism by which AEBP2 modulates PRC2 genomic localization. | PMID:34057467 | Nucleic acids research |
| 2022 | High | In zebrafish embryos, H2Aub1 deposition by PRC1 (Rnf2) during pre-ZGA stages enables recruitment of Aebp2-containing PRC2 and subsequent H3K27me3 deposition during post-ZGA; inhibition of Rnf2 eliminates both Aebp2-PRC2 recruitment and H3K27me3, demonstrating that H2Aub1 is required upstream of Aebp2-PRC2 for gene silencing at ZGA. | PMID:34982026 | eLife |
| 2023 | High | H2A ubiquitination by PRC1 alters contacts between the H3 tail and DNA on nucleosomes, improving the methyltransferase activity of the PRC2-AEBP2-JARID2 complex; linker DNA is equally important as H2Aub for H3K27 methylation, and these effects synergize. | PMID:36610636 | Journal of molecular biology |
| 2025 | High | The broadly expressed long isoform of AEBP2 (AEBP2L) inhibits PRC2, while the short isoform (AEBP2S) promotes PRC2 activity. AEBP2L inhibits PRC2 DNA binding, histone methyltransferase activity, and binding to target genes; AEBP2S promotes PRC2 DNA-binding and is essential for de novo repression during naïve-to-primed pluripotency transition. Cryo-EM and mutagenesis identified the negatively charged N-terminal region of AEBP2L as the inhibitory element, which is a recently evolved vertebrate feature. | PMID:41168462 | The EMBO journal |
| 2025 | Medium | AEBP2 long isoform N-terminal DE-rich motif inhibits both EZH2 automethylation and H3K27 methylation; AEBP2 short isoform enhances PRC2 catalytic activity and H3K27me3 spreading; re-expression of AEBP2L (but not AEBP2S) in Mtf2/Jarid2/Aebp2 triple-knockout mESCs failed to restore H3K27me3 and caused defective differentiation. | PMID:bio_10.1101_2025.11.09.687442 | bioRxiv |
| 2025 | Medium | In EZH2-mutant DLBCL, AEBP2 functions within a PRC2.2 complex lacking JARID2, using its zinc-finger domains to sample intergenic chromatin and sustain H3K27me2 (not H3K27me3-mediated gene silencing). Loss of AEBP2 reduces intergenic H3K27me2 and sensitizes cells to PRC2 inhibitors. | PMID:bio_10.1101_2025.10.14.682307 | bioRxiv |

## Citations

- PMID:10329662
- PMID:15225548
- PMID:19293275
- PMID:21949878
- PMID:23110252
- PMID:24837194
- PMID:25451679
- PMID:27317809
- PMID:29058709
- PMID:29348366
- PMID:29499137
- PMID:29628311
- PMID:29681498
- PMID:29891558
- PMID:31864706
- PMID:31959557
- PMID:32043141
- PMID:33479123
- PMID:34057467
- PMID:34982026
- PMID:36610636
- PMID:41168462
- PMID:bio_10.1101_2025.10.14.682307
- PMID:bio_10.1101_2025.11.09.687442
