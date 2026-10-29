---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ANKRD28
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: O15084
self_evaluation_pairwise: tie
faith_pct: 100.0
n_discoveries: 8
citation_count: 8
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ANKRD28 (human)

## Current model (mechanistic narrative)

ANKRD28 is an ankyrin-repeat regulatory/scaffold subunit that couples protein Ser/Thr phosphatases to specific substrates, thereby shaping signaling outputs in the NF-κB pathway, nuclear transcriptional control, and cell migration [PMID:18186651, PMID:16564677, PMID:19118547]. As part of the PP6 holoenzyme, it forms a heterotrimer with the PP6 catalytic subunit and SAPS-domain scaffolds (PP6R1 or PP6R3), with PP6R1 providing separable binding surfaces for PP6c and ANKRD28; loss of ANKRD28 or PP6R1 accelerates IκBε degradation upon TNFα, defining ANKRD28 as a positive PP6 co-regulator restraining NF-κB activation [PMID:18186651]. Independently, ANKRD28 (PITK) acts as a PP1-targeting subunit that directs PP1 to nuclear foci to dephosphorylate hnRNP K at S284 and reprogram transcription, with its PP1 binding switched off by sequential CaMKIIδ-mediated phosphorylation of S1017 followed by GSK3 phosphorylation of S1013 flanking its PP1C-binding motif, which also governs its speckled-nuclear versus diffuse localization [PMID:16564677, PMID:17023142]. Through its ankyrin repeats it binds the SH3 domain of DOCK180 in competition with ELMO, controlling focal adhesion organization, p130Cas phosphorylation, and Rac1-dependent migration [PMID:19118547], a function further tuned by Rab40c/CRL5-mediated ubiquitylation and lysosomal turnover of ANKRD28 that modulates PP6 activity in migrating cells [PMID:35512830]. BRCA1 binds ANKRD28 in the cytoplasm and stabilizes IκBε through this interaction, linking BRCA1 to suppression of NF-κB signaling via the ANKRD28–PP6 axis [PMID:27026398]. An ANKRD28–NUP98 fusion arising from a cryptic translocation in MDS/AML mislocalizes the protein to the nucleolus and drives oncogenic focus formation in a manner requiring the ANKRD28 C-terminus [PMID:17988990].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0098772 molecular function regulator activity, GO:0060090 molecular adaptor activity
- **localization:** GO:0005634 nucleus, GO:0005829 cytosol, GO:0005730 nucleolus
- **pathway (Reactome):** R-HSA-162582 Signal Transduction, R-HSA-392499 Metabolism of proteins
- **partners:** PPP6C, PP6R1, PP6R3, PP1C, HNRNP K, DOCK180, BRCA1, RAB40C
- **complexes:** PP6 phosphatase holoenzyme, PP1 phosphatase complex (PITK targeting), Rab40c/CRL5 E3 ubiquitin ligase complex (substrate)

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2008 | High | ANKRD28 is a regulatory subunit of the PP6 holoenzyme, forming a heterotrimer with the PP6 catalytic subunit and SAPS-domain scaffold subunits (PP6R1 or PP6R3). Tagged ANKRD28 co-precipitated with PP6 but not PP2A or PP4. The C-terminal region of PP6R1 was sufficient to co-precipitate ANKRD28 but not PP6, demonstrating that PP6R1 acts as a scaffold with separate binding regions for PP6 and ANKRD28. Knockdown of PP6R1 or ANKRD28 equivalently enhanced IκBε degradation in response to TNFα, placing ANKRD28 as a functional PP6 co-regulator in the NF-κB pathway. | PMID:18186651 | Biochemistry |
| 2006 | High | ANKRD28 (PITK) functions as a PP1 targeting subunit that directs PP1 to nuclear foci to dephosphorylate hnRNP K at S284. PITK is phosphorylated in vivo at S1013 and S1017 flanking its PP1C-binding motif, and this phosphorylation negatively regulates PP1 binding. The phosphomimetic mutant S1013,1017D-PITK showed reduced PP1 binding, whereas constitutively dephosphorylated S1013,1017A-PITK showed increased PP1 binding and more profound hnRNP K dephosphorylation at S284. PITK expression altered transcription of 47 genes, including >14-fold induction of MEK5, in a manner modulated by hnRNP K co-expression. | PMID:16564677 | Cellular signalling |
| 2006 | High | ANKRD28 (PITK) phosphorylation at S1017 is catalyzed by CaMKIIδ, which promotes subsequent phosphorylation of S1013 by GSK3 in vitro. Phosphorylation state at S1013/S1017 dictates subcellular localization: wildtype and S1013,1017D-PITK show speckled nuclear localization, whereas constitutively dephosphorylated S1013,1017A-PITK displays diffuse cytoplasmic/nuclear localization. | PMID:17023142 | Cellular signalling |
| 2008 | High | ANKRD28 binds the SH3 domain of DOCK180 and competes with ELMO for this interaction. ANKRD28 knockdown reduced HeLa cell migration velocity and altered focal adhesion distribution (Crk, paxillin, p130Cas). Co-expression of ANKRD28 with p130Cas, Crk, and DOCK180 induced hyper-phosphorylation of p130Cas and formation of multiple long cellular processes, distinct from ELMO co-expression which induced lamellipodial protrusion. | PMID:19118547 | Experimental cell research |
| 2016 | High | BRCA1 interacts with ANKRD28 in the cytoplasm, identified by yeast two-hybrid screen and confirmed by reciprocal co-immunoprecipitation of overexpressed proteins and endogenous co-IP. The interaction is located in the cytoplasm by proximity ligation assay. The main ANKRD28-binding site on BRCA1 is in its intrinsically disordered scaffold central region. BRCA1 overexpression stabilizes IκBε upon TNFα stimulation, an effect lost with a BRCA1 truncation that cannot interact with ANKRD28, indicating BRCA1 modulates PP6 signaling via ANKRD28. | PMID:27026398 | The Biochemical journal |
| 2007 | Medium | In a patient with MDS/AML, ANKRD28 is fused to NUP98 via a cryptic translocation t(3;5;11)(p25;q35;p15), producing in-frame ANKRD28-NUP98 fusion transcripts. Transient overexpression of ANKRD28-NUP98 in NIH/3T3 cells caused significantly increased focus formation (oncogenic transformation), whereas a C-terminal deletion mutant (ΔC-ANKRD28) did not. ANKRD28-NUP98 localized to the nucleolus and cytoplasm, whereas wildtype ANKRD28 and ΔC-ANKRD28 were exclusively cytoplasmic, indicating the NUP98 fusion alters ANKRD28 subcellular localization. | PMID:17988990 | International journal of hematology |
| 2022 | High | Rab40c, as part of a Cullin5-based E3 ubiquitin ligase complex (Rab40c/CRL5), binds the PP6 complex and ubiquitylates ANKRD28, targeting it for lysosomal degradation. Rab40c knockout reduces PP6 activity (measured via decreased FAK and MOB1 phosphorylation) and alters focal adhesion number, size, and distribution in migrating MDA-MB-231 cells. | PMID:35512830 | Life science alliance |
| 2024 | Medium | PP6 functions as a heterotrimer composed of PP6c, PP6R (PP6R1/R2/R3), and scaffold subunits including ANKRD28. The PP6c-PP6R3 complex specifically regulates cancer stem cell (CSC) markers in colorectal cancer cells; PP6c knockdown reduced colony-forming ability, in vivo proliferation, and altered expression of stemness-associated genes. | PMID:39014521 | Cancer science |

## Citations

- PMID:16564677
- PMID:17023142
- PMID:17988990
- PMID:18186651
- PMID:19118547
- PMID:27026398
- PMID:35512830
- PMID:39014521
