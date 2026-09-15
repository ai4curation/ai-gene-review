---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/AP3D1
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: O14617
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 11
citation_count: 11
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for AP3D1 (human)

## Current model (mechanistic narrative)

AP3D1 encodes the δ subunit of the AP-3 adaptor protein complex and is essential for assembly and stability of both the ubiquitous and neuronal forms of AP-3, which direct vesicle-mediated trafficking of cargo to late endosomal and lysosomal compartments [PMID:26744459]. Through its δ subunit, AP3D1 selects specific cargo for lysosomal delivery: it binds S-palmitoylated IFNGR1 (Cys122) to route the receptor for lysosomal degradation [PMID:33627378], and it captures DRAM2 in a phosphorylation-dependent manner, requiring RSK2-mediated phosphorylation at Ser263, such that the non-phosphorylatable DRAM2(S263A) loses AP3D1 binding and is instead diverted to the plasma membrane to enhance exosome secretion [PMID:42059423]. AP3D1 also participates in TGFβ2 secretion via an AP-3-dependent late endosomal/exosomal route [PMID:34166600] and governs the endolysosomal trafficking and lysosomal localization of cargo such as RNF13 [PMID:34831286]. Consistent with its role in lysosome-related organelle biogenesis, loss-of-function mutations in AP3D1 destabilize the complex and cause a Hermansky-Pudlak-type disorder featuring immunodeficiency with defective T-cell degranulation [PMID:26744459] and abnormal platelet dense granule storage [PMID:30472485]. In the nervous system, AP3D1 loss perturbs neurotransmitter vesicle turnover and synaptic transmission and is required for proper retinal progenitor differentiation [PMID:19032734, PMID:19631730].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0060090 molecular adaptor activity, GO:0038024 cargo receptor activity
- **localization:** GO:0005768 endosome, GO:0005764 lysosome, GO:0031410 cytoplasmic vesicle
- **pathway (Reactome):** R-HSA-5653656 Vesicle-mediated transport, R-HSA-9609507 Protein localization, R-HSA-1852241 Organelle biogenesis and maintenance
- **partners:** IFNGR1, OPTN, FAM13A, TGFB2, DRAM2, RNF13
- **complexes:** AP-3 adaptor complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2016 | High | AP3D1 encodes the AP3δ subunit essential for both the ubiquitous and neuronal forms of the AP-3 complex; homozygous loss-of-function mutation in AP3D1 destabilizes the entire AP-3 complex, and retroviral reconstitution with wild-type AP3D1 restores AP-3 complex formation and rescues the T-cell degranulation defect in patient cells. | PMID:26744459 | Blood |
| 2018 | Medium | Homozygous frameshift mutation in AP3D1 (c.1978delG, p.Ala660Argfs*54) causes loss of AP-3 complex function, leading to abnormal platelet storage pathway, confirming AP3D1/AP3δ is required for lysosome-related organelle biogenesis including platelet dense granules. | PMID:30472485 | European journal of medical genetics |
| 2021 | High | AP3D1 binds palmitoylated IFNGR1 (S-palmitoylated on Cys122) and sorts it to the lysosome for degradation; optineurin interacts with AP3D1 to prevent this palmitoylation-dependent lysosomal sorting, thereby maintaining IFNGR1 surface expression and IFNγ/MHC-I signaling. | PMID:33627378 | Cancer discovery |
| 2021 | Medium | AP3D1 forms a cellular protein complex with FAM13A and TGFβ2; this complex mediates secretion of TGFβ2 through an AP-3-dependent pathway involving delivery to late endosomal compartments for exosomal secretion, with FAM13A acting as a negative regulator targeting a late stage of coat-cargo dissociation. | PMID:34166600 | American journal of respiratory cell and molecular biology |
| 2021 | Medium | Knockdown of AP3D1 (AP-3 complex subunit) alters the lysosomal localization of wild-type RNF13 and causes abnormal enlargement of endosomal vesicles, placing AP3D1 upstream of RNF13 endolysosomal trafficking. | PMID:34831286 | Cells |
| 2009 | Medium | Loss of Ap3d1 in mocha mice (10,639 bp deletion covering exons 2–6) results in deficiency in vesicle transport and storage, affecting neurotransmitter vesicle turnover; Ap3d1-null hippocampal neurons show higher input resistance and faster, stronger depression of glutamatergic autaptic EPSCs compared to controls. | PMID:19032734 | BMC research notes |
| 2009 | Medium | Ap3d1 loss in mocha mice causes complete absence of cholinergic amacrine cells and reduction of parvalbumin-expressing and other amacrine cell subtypes in the retina without affecting overall retinal layering, cell number, proliferation, or apoptosis, indicating AP3D1 regulates retinal progenitor cell competence and differentiation. | PMID:19631730 | International journal of developmental neuroscience |
| 2009 | Medium | The Nxf1(CAST) allele suppresses the Ap3d1(mh2J) IAP retrovirus insertion mutation by approximately 2-fold increase in correctly-spliced Ap3d1 mRNA and decrease in mutant-specific alternatively-processed RNA, demonstrating that Ap3d1 expression can be rescued at a functional threshold through modulation of pre-mRNA splicing. | PMID:19436707 | PLoS genetics |
| 2022 | Medium | Loss of ap3d1 in zebrafish (crasher mutant and ap3d1 knockout) causes reduced expression of melanogenesis genes dct and tyrp1b (but not tyr), and autophagy pathway genes are upregulated; treatment with autophagy inhibitor bafilomycin A1 significantly decreases melanophore number in ap3d1 mutants, indicating ap3d1 promotes melanophore survival by limiting excessive autophagy. | PMID:35816398 | Pigment cell & melanoma research |
| 2026 | High | AP3D1/AP-3 is required for RPS6KA3/RSK2-phosphorylation-dependent trafficking of DRAM2 to the late endosomal-lysosomal pathway; phosphorylation of DRAM2 at Ser263 enables its binding to AP3D1, and the non-phosphorylatable DRAM2(S263A) mutant fails to bind AP3D1, exhibits defective lysosomal trafficking, and is instead redirected toward the plasma membrane where it enhances exosome secretion. | PMID:42059423 | Autophagy |
| 2018 | Low | Bovine AP3D1 (boAP3D1) interacts in vitro with the N-terminal domain of BLV envelope glycoprotein gp51; key amino acids on AP3D1 (Lys925, Asp807, Asp695, Arg800) and gp51 were identified as probable interaction residues, and recombinant N-terminal gp51 binding to MDBK cells was sensitive to trypsin and chymotrypsin treatment. | PMID:29928016 | PloS one |

## Citations

- PMID:19032734
- PMID:19436707
- PMID:19631730
- PMID:26744459
- PMID:29928016
- PMID:30472485
- PMID:33627378
- PMID:34166600
- PMID:34831286
- PMID:35816398
- PMID:42059423
