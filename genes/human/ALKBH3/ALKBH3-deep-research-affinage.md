---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ALKBH3
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: Q96Q83
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 22
citation_count: 22
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ALKBH3 (human)

## Current model (mechanistic narrative)

ALKBH3 is a single-stranded nucleic acid demethylase that reverses N1-methyladenine/N1-methyladenosine (m1A) and N3-methylcytosine/N3-methylcytidine (m3C) lesions in both DNA and RNA, functioning both as an alkylation-damage repair enzyme and as an epitranscriptomic eraser that controls mRNA fate [PMID:22055184, PMID:30541109, PMID:26967262]. In its DNA-repair role, ALKBH3 acts within the ASCC complex: the ASCC3 3'-5' helicase generates the single-stranded substrate ALKBH3 prefers, and loss of either protein elevates 3-methylcytosine and triggers DNA-damage signaling and reduced proliferation [PMID:22055184]. The complex is targeted to nuclear alkylation sites through the ASCC2 CUE domain, which reads K63-linked polyubiquitin chains [PMID:34971705], and ALKBH3 repair of methyl adducts on 3'-tailed DNA is further stimulated by direct interaction with the recombination factor RAD51C [PMID:31642493]. Crystal structures of substrate-crosslinked ALKBH3 show that the enzyme grips single-stranded substrate via two beta-hairpins and an alpha2 helix and everts the methylated base, with active-site residue Thr133 dictating m1A/m3C selectivity (its substitution by the corresponding FTO/ALKBH5 residue switches selectivity toward m6A) and Asp194 and Tyr143 contributing to substrate recognition and base eversion [PMID:38158383, PMID:38256217]. As an RNA demethylase, ALKBH3 strips m1A from numerous target mRNAs to govern their stability and translation: by erasing m1A it either prevents reader-driven decay—removing marks recognized by YTHDF2/PAN2-PAN3 or, conversely, by the stabilizing reader YTHDF1—or otherwise alters transcript half-life, thereby controlling targets such as CSF-1, Aurora A, METTL3, ALDOA, HK2, VEGFA, PINK1, ZBED6, and Mmp15 [PMID:30342176, PMID:35277482, PMID:38118002, PMID:40019372, PMID:40654364, PMID:40493193, PMID:41816968, PMID:41816893, PMID:39004750]. Through this mRNA-regulatory activity ALKBH3 influences a broad range of processes including cancer cell invasion and glycolysis, ciliogenesis, hippocampal neurogenesis, mitophagy, neovascularization, and cell-survival decisions [PMID:30342176, PMID:35277482, PMID:39004750, PMID:40493193, PMID:41816968]. ALKBH3 also demethylates tRNA, sensitizing it to angiogenin cleavage and generating tRNA-derived small RNAs that support ribosome assembly and suppress apoptosis [PMID:30541109].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0140098 catalytic activity, acting on RNA, GO:0140097 catalytic activity, acting on DNA, GO:0016491 oxidoreductase activity, GO:0003723 RNA binding, GO:0003677 DNA binding
- **localization:** GO:0005634 nucleus, GO:0005829 cytosol
- **pathway (Reactome):** R-HSA-73894 DNA Repair, R-HSA-8953854 Metabolism of RNA, R-HSA-74160 Gene expression (Transcription), R-HSA-1643685 Disease
- **partners:** ASCC3, ASCC2, RAD51C
- **complexes:** ASCC complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2011 | High | ALKBH3 forms a complex with the Activating Signal Cointegrator Complex (ASCC), and ASCC3 (the largest subunit) encodes a 3'-5' DNA helicase whose activity generates single-stranded DNA upon which ALKBH3 preferentially performs dealkylation. Loss of either ALKBH3 or ASCC3 leads to increased 3-methylcytosine levels, reduced cell proliferation, and pH2A.X/53BP1 foci formation. | PMID:22055184 | Molecular cell |
| 2019 | High | ALKBH3 is a 1-methyladenosine (m1A) and 3-methylcytidine (m3C) demethylase of tRNA. ALKBH3-demethylated tRNA is more sensitive to angiogenin (ANG) cleavage, generating tRNA-derived small RNAs (tDRs) around anticodon regions that strengthen ribosome assembly and prevent cytochrome c-triggered apoptosis. | PMID:30541109 | Nucleic acids research |
| 2018 | Medium | ALKBH3-mediated m1A demethylation of CSF-1 mRNA increases CSF-1 mRNA stability (half-life) in breast and ovarian cancer cells, promoting cancer cell invasiveness. The m1A site is mapped to the 5'UTR near the translation initiation site, and YTHDF2 (an m6A reader) is not the reader of m1A-containing CSF-1 mRNA. | PMID:30342176 | Biochimica et biophysica acta. Gene regulatory mechanisms |
| 2019 | Medium | ALKBH2 and ALKBH3 (and E. coli AlkB) can oxidize 5-methylcytosine (5mC) in DNA to 5-hydroxymethylcytosine, 5-formylcytosine, and 5-carboxylcytosine in vitro, demonstrating capacity to oxidize a methyl group attached to carbon rather than nitrogen. | PMID:31114894 | Nucleic acids research |
| 2022 | High | ALKBH3 removes m1A from Aurora A mRNA, stabilizing it and promoting its translation; depletion of ALKBH3 enhances Aurora A mRNA decay and inhibits its translation, leading to inhibition of ciliogenesis. The catalytically inactive ALKBH3 mutant cannot rescue ciliary defects in alkbh3 morphant zebrafish, confirming the demethylation activity is required. | PMID:35277482 | Cell discovery |
| 2019 | Medium | ALKBH3 directly interacts with human RAD51 paralogue RAD51C via protein-protein interaction, and RAD51C-ALKBH3 interaction stimulates ALKBH3-mediated repair of methyl-adducts within 3'-tailed DNA substrates; disruption of this interaction impairs ALKBH3 function both in vitro and in vivo. | PMID:31642493 | Nucleic acids research |
| 2021 | Medium | ASCC3, the ALKBH3 binding partner, mediates P-body formation and promotes selective removal of chemically induced m1A and m3C from mRNA; ASCC3-deficient cells show delayed clearance of MMS-induced m1A and m3C from mRNA and impaired P-body formation, consistent with a model where ASCC3-mediated ribosome disassembly allows ALKBH3-dependent mRNA demethylation. | PMID:34217309 | Journal of translational medicine |
| 2015 | Medium | ALKBH3 binds to transcription-associated genomic locations including promoter-proximal paused RNA Pol II sites and enhancers in prostate cancer cells; it strongly binds to transcription initiation sites of a small number of highly active promoters characterized by high levels of Mediator, cohesin, and active histone marks. ALKBH3 depletion does not directly alter transcription of its target genes but induces upregulation of ALKBH3-non-bound inflammatory genes. | PMID:26221185 | Genome medicine |
| 2016 | High | A fluorogenic probe (MAQ) exploiting fluorescence quenching of 1-methyladenine enables direct measurement of ALKBH3 repair activity in vitro and in cells; the probe is specific for ALKBH3 over ALKBH2 and shows Km and kcat values equivalent to the native substrate. ALKBH3 activity was imaged and quantified in live cells by microscopy and flow cytometry. | PMID:26967262 | Journal of the American Chemical Society |
| 2024 | High | Crystal structures of ALKBH3 crosslinked to oligonucleotide substrates (obtained with a synthetic antibody chaperone) reveal that ALKBH3 uses two β-hairpins (β4-loop-β5 and β'-loop-β'') and an α2 helix for single-stranded substrate binding. Residue Thr133 in the active pocket is required for specific recognition of m1A and m3C; mutation of Thr133 to the corresponding FTO or ALKBH5 residue converts ALKBH3 substrate selectivity from m1A to m6A. Asp194 forms a bubble-like region also critical for substrate recognition. | PMID:38158383 | Angewandte Chemie (International ed. in English) |
| 2024 | Medium | Biochemical and mutagenesis analysis identifies Tyr143, Leu177, and His191 as key residues for ALKBH3 secondary structure and catalytic activity toward methylated single-stranded DNA. Tyr143 is critical for binding the flipped-out methylated base and stabilizing its everted conformation; Leu177 and His191 are required for secondary structure integrity. Stopped-flow fluorescence spectroscopy revealed a transient kinetic mechanism comprising substrate binding, base eversion, and anchoring steps. | PMID:38256217 | International journal of molecular sciences |
| 2021 | Medium | The ASCC2 CUE domain selectively binds K63-linked polyubiquitin chains (diubiquitin) by contacting both the distal and proximal ubiquitin, thereby localizing the ASCC-ALKBH3 repair complex to alkylation damage sites in the nucleus. Mutation of residues in the N-terminal portion of the ASCC2 α1 helix that contact the proximal ubiquitin decreases ASCC2 nuclear recruitment in response to DNA alkylation. | PMID:34971705 | The Journal of biological chemistry |
| 2016 | Medium | Alkbh3 (and Alkbh2), but not alkyladenine DNA glycosylase (Aag), can repair N3-ethylthymidine (N3-EtdT) in mammalian cells, as shown by transcription-based lesion bypass assays. Purified human Alkbh2 directly reverses N3-EtdT in vitro. N3-CMdT, O2-EtdT, O4-EtdT, and O4-CMdT are not repaired by Alkbh2 or Alkbh3. | PMID:26930515 | ACS chemical biology |
| 2024 | Medium | ALKBH3-mediated m1A demethylation of SP100A mRNA prevents its recognition by YTHDF1 (an m1A reader that promotes RNA stability and translation), thereby reducing SP100A protein levels and attenuating formation of tumor-suppressive PML nuclear condensates. YTHDF1 is identified as a reader of m1A-methylated SP100A mRNA. | PMID:38118002 | Nucleic acids research |
| 2025 | Medium | ALKBH3 demethylates m1A on METTL3 mRNA, preventing YTHDF2-dependent mRNA decay of METTL3 transcript and thereby increasing METTL3 protein levels. Elevated METTL3 then stabilizes COL1A1 and FN1 mRNAs via m6A modification, promoting pathological skin fibrosis (hypertrophic scars). | PMID:40019372 | Advanced science |
| 2024 | Medium | m1A demethylase Alkbh3 promotes neurogenesis by demethylating m1A on Mmp15 mRNA, improving its RNA stability and translational efficacy; depletion of Alkbh3 in neural stem cells decreases neuronal differentiation and proliferation while increasing gliogenesis, and reduces hippocampal neurogenesis and spatial memory in adult mice. | PMID:39004750 | Cell & bioscience |
| 2025 | Medium | ALKBH3 demethylates m1A on HK2 mRNA in retinal pigment epithelial cells, activating glycolysis and excess lactate production. This lactate promotes H3K18 histone lactylation, which binds the ALKBH3 promoter to amplify its transcription, establishing a positive feedback loop. ALKBH3 also directly demethylates VEGFA mRNA to promote choroidal neovascularization. | PMID:40493193 | Proceedings of the National Academy of Sciences of the United States of America |
| 2025 | Medium | ALKBH3-mediated m1A demethylation of ALDOA mRNA at the 3'UTR stabilizes ALDOA mRNA by preventing recruitment of the YTHDF2/PAN2-PAN3 complex that drives mRNA degradation; this stabilization potentiates glycolysis and doxorubicin resistance in triple-negative breast cancer cells. | PMID:40654364 | Acta pharmaceutica Sinica. B |
| 2026 | Medium | ALKBH3 removes m1A from PINK1 mRNA, promoting its stability and translation; elevated ALKBH3 in Alzheimer's disease models impairs PINK1-dependent mitophagy, leading to mitochondrial dysfunction and neuronal damage. Alkbh3 reduction decreases amyloid-β plaques and restores cognition in 5xFAD mice. | PMID:41816968 | Advanced science |
| 2026 | Medium | ALKBH3 demethylates m1A on ZBED6 mRNA, enhancing ZBED6 translation; ZBED6 then physically interacts with STAT1 (confirmed by co-immunoprecipitation and ChIP) and represses STAT1-driven AIM2 transcription, thereby suppressing PANoptosis (pyroptosis/apoptosis/necroptosis) in cardiomyocytes during ischemia/reperfusion injury. | PMID:41816893 | Clinical and translational medicine |
| 2024 | Medium | PUS7-dependent pseudouridylation of ALKBH3 mRNA at position U696 enhances its translation efficiency, thereby increasing ALKBH3 protein levels and suppressing gastric cancer progression. | PMID:39175405 | Clinical and translational medicine |
| 2025 | Low | ALKBH3-mediated m1A demethylation of ATF4 mRNA increases ATF4 expression, which inhibits ferroptosis (by upregulating SLC7A11, GPX4, FTH1) and promotes AML cell survival; ALKBH3 knockdown promotes ferroptosis in KG-1 cells. | PMID:39803678 | Hematology |

## Citations

- PMID:22055184
- PMID:26221185
- PMID:26930515
- PMID:26967262
- PMID:30342176
- PMID:30541109
- PMID:31114894
- PMID:31642493
- PMID:34217309
- PMID:34971705
- PMID:35277482
- PMID:38118002
- PMID:38158383
- PMID:38256217
- PMID:39004750
- PMID:39175405
- PMID:39803678
- PMID:40019372
- PMID:40493193
- PMID:40654364
- PMID:41816893
- PMID:41816968
