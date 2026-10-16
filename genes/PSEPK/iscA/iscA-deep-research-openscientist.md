---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-12T22:54:46.932316'
end_time: '2026-08-12T23:15:06.587469'
duration_seconds: 1219.66
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: iscA
  gene_symbol: iscA
  uniprot_accession: Q88PK6
  protein_description: 'RecName: Full=Iron-binding protein IscA {ECO:0000256|ARBA:ARBA00014591};
    AltName: Full=Iron-sulfur cluster assembly protein {ECO:0000256|ARBA:ARBA00032050};'
  gene_info: Name=iscA {ECO:0000313|EMBL:AAN66469.1}; OrderedLocusNames=PP_0844 {ECO:0000313|EMBL:AAN66469.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the HesB/IscA family.
  protein_domains: ATAP. (IPR016092); ATAP_core_dom. (IPR000361); Fe-S_cluster_asmbl/transfer.
    (IPR050322); FeS_cluster_insertion_CS. (IPR017870); HesB-like_dom_sf. (IPR035903)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 3
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: iscA-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: iscA-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q88PK6
- **Protein Description:** RecName: Full=Iron-binding protein IscA {ECO:0000256|ARBA:ARBA00014591}; AltName: Full=Iron-sulfur cluster assembly protein {ECO:0000256|ARBA:ARBA00032050};
- **Gene Information:** Name=iscA {ECO:0000313|EMBL:AAN66469.1}; OrderedLocusNames=PP_0844 {ECO:0000313|EMBL:AAN66469.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the HesB/IscA family.
- **Key Domains:** ATAP. (IPR016092); ATAP_core_dom. (IPR000361); Fe-S_cluster_asmbl/transfer. (IPR050322); FeS_cluster_insertion_CS. (IPR017870); HesB-like_dom_sf. (IPR035903)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "iscA" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'iscA' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **iscA** (gene ID: iscA, UniProt: Q88PK6) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: IscA (Q88PK6, PP_0844) in *Pseudomonas putida* KT2440

## 1. Summary / Answer to the Research Question

**IscA (gene *iscA*, locus PP_0844; UniProt Q88PK6) is an A-type carrier (ATC) protein of the ISC (Iron–Sulfur Cluster) biogenesis machinery.** Its primary function is **not** enzymatic catalysis but **molecular carriage**: it is a soluble cytoplasmic Fe–S cluster / iron chaperone that binds a pre-assembled iron–sulfur cluster (a labile, solvent-exposed [2Fe–2S], which it can convert/deliver as [4Fe–4S]) and **transfers it from the de novo assembly scaffold (IscU) to specific apo-target proteins**, thereby maturing them into active Fe–S enzymes. It belongs to the HesB/IscA family and carries the family-defining triad of conserved cysteines that ligate the cluster.

The gene identity is **confirmed and unambiguous**: the symbol *iscA*, the "Iron-binding protein IscA / Iron-sulfur cluster assembly protein" description, the HesB/IscA family, and the ATAP/FeS-cluster-insertion domains all coincide with a large, directly applicable body of literature on bacterial (chiefly *E. coli*) IscA. The 107-aa Q88PK6 sequence retains all three functional cysteines.

---

## 2. Molecular Function (Primary Role)

IscA is one of a small set of **A-type carrier proteins (ATCs)**. In the well-studied *E. coli* paradigm there are four ATCs — IscA, SufA, ErpA and the degenerate ATC* domain of NfuA — which "were shown to partially replace each other in their roles in [4Fe-4S] cluster insertion into specific target proteins" (Hasnat et al. 2021, PMID 33782054).

- **What it does:** receives an Fe–S cluster from the biosynthetic scaffold and hands it off to acceptor apoproteins. It does **not** synthesize sulfide or perform de novo cluster assembly; that is the job of the upstream cysteine desulfurase IscS and scaffold IscU. The ISC system assembles a "transient formation of a 2Fe2S cluster on a scaffold protein from sulfide and iron salts" which is then transferred via carriers to acceptor apoproteins (Bonomi et al. 2022, PMID 35611886).
- **Substrate / ligand specificity:** the "substrate" is the iron–sulfur cluster itself (and/or ferrous/ferric iron). UniProt annotates Q88PK6 as an **iron-binding protein**, and IscA family members are documented to bind iron as well as Fe–S clusters, supporting a dual role as an **iron chaperone/donor** that recruits iron for cluster assembly and as a **cluster carrier** for downstream delivery.

### Iron-chaperone role and the "scaffold vs. carrier" resolution
Direct biochemical/genetic work (the Ding laboratory) clarified IscA's precise role. In vivo, "IscA binds iron" whereas the scaffold IscU and the frataxin homolog CyaY do not, and IscA "may act as an iron chaperone for the biogenesis of iron-sulfur clusters in *E. coli* cells under aerobic conditions" (Wang et al. 2010, PMID 20942799). Critically this activity is **oxygen-regulated**: "the strong iron-binding activity of IscA is greatly diminished in *E. coli* cells under anaerobic growth conditions," and IscA + its paralogue SufA are essential for Fe–S assembly aerobically but not anaerobically (PMID 20942799). In vitro, with IscS/L-cysteine present, "iron-sulfur clusters are assembled in IscU, but not in IscA, suggesting that IscU is a preferred iron-sulfur cluster assembly scaffold protein," while in the absence of cysteine "nearly all iron is bound to IscA," which prevents precipitation of biologically inaccessible ferric hydroxide (Yang, Bitoun & Ding 2006, PMID 16877383). **Interpretation for the target:** IscA is best described as an **iron chaperone / cluster carrier acting downstream of the IscU scaffold**, keeping iron soluble and bioavailable under oxidizing conditions. Because *P. putida* KT2440 is an **obligate aerobe**, this aerobic iron-chaperone function is expected to be particularly relevant for PP_0844.
- **Clients:** IscA/ATCs deliver clusters to numerous [4Fe–4S] enzymes, including respiratory-chain and metabolic proteins. Concrete examples of IscA-dependent maturation include subunits of the membrane-associated formate hydrogenlyase (FHL) complex — "The A-type carrier (ATC) proteins IscA and ErpA probably deliver [Fe-S] to specific apoprotein components of the FHL complex because mutants lacking either protein exhibited strongly reduced hydrogen production. Neither ATC protein could compensate for the lack of the other" (Pinske et al. 2013, PMID 23558265) — and radical-SAM / molybdenum-cofactor and nitrate-reductase pathway proteins (Hasnat et al. 2021, PMID 33782054).

### Structural basis of function
The first Fe–S-cluster-bound structure of an IscA (from *Thermosynechococcus elongatus*) showed that "one partially exposed [2Fe-2S] cluster is coordinated by two conformationally distinct IscA protomers … with asymmetric cysteinyl ligation by **Cys37, Cys101, Cys103**" and that the protein "carries three strictly conserved cysteine residues" (Morimoto et al. 2006, PMID 16730357). The **solvent-exposed** cluster and asymmetric, labile ligation are precisely what enable cluster handoff to acceptor proteins.

**Bioinformatic confirmation for the target:** Direct analysis of Q88PK6 (107 aa) identifies exactly three cysteines — **C35** within the conserved `...RTTG**C**SGL...` motif (the InterPro IPR017870 FeS-cluster-insertion conserved site) and **C99/C101** in the C-terminal `...RGE**C**G**C**GES...` motif. These are positionally homologous to the cluster-ligating Cys37/Cys101/Cys103 of *T. elongatus* IscA. Retention of this triad distinguishes a functional carrier from the "degenerate' A-type carrier domain (ATC*) lacking Fe-S cluster co-ordinating Cys ligands" found in NfuA subfamily II (Py et al. 2012, PMID 22966982) — i.e., P. putida IscA is a **bona fide, cluster-competent** ATC.

---

## 3. Biological Process / Pathway

IscA operates within the **ISC iron–sulfur cluster biogenesis pathway**, encoded by the *isc* operon (`iscR-iscS-iscU-iscA-hscB-hscA-fdx-iscX`).

**Organism-specific genomic context (this study).** A UniProt/KEGG query for *P. putida* KT2440 confirms the ISC cluster is present and canonically ordered around the target: **PP_0841 *iscR*** (2Fe–2S IscR transcriptional dual regulator) → **PP_0842 *iscS*** (cysteine desulfurase, EC 2.8.1.7) → **PP_0843 *iscU*** (scaffold) → **PP_0844 *iscA*** (target, Q88PK6) → **PP_0845 *hscB*** (co-chaperone) → **PP_0846 *hscA*** (Hsp70 chaperone) → **PP_0847 *fdx*** (2Fe–2S ferredoxin). A second cysteine desulfurase, *iscS-II* (PP_2435), lies elsewhere. This exact synteny with the *E. coli* `iscR-iscSUA-hscBA-fdx` operon is strong organism-specific evidence that PP_0844 functions as the A-type carrier/iron chaperone of a fully intact ISC machinery, co-regulated with the desulfurase, scaffold, chaperones, ferredoxin, and the IscR master regulator.
 Genetic dissection of this operon in *E. coli* placed IscA in the **assembler/delivery** stage: "the assembly of Fe-S clusters [is executed] by assembler machinery comprising of the iscUA-hscBA-fdx gene products," with IscS providing sulfur via cysteine desulfurase activity (Tokumoto & Takahashi 2001, PMID 11432781). Coexpression of the whole `iscS-iscU-iscA-hscB-hscA-fdx` cluster dramatically increases holo-ferredoxin production, confirming these products "are involved in the assembly of the Fe-S clusters in a wide variety of Fe-S proteins" (Nakamura et al. 1999, PMID 10393315).

**Pathway position (order of events):**
`IscS (Cys → sulfur) → IscU scaffold (+ Fe, + Fdx electrons, HscA/HscB chaperones) builds [2Fe–2S] → IscA/other ATCs receive & traffic the cluster (and supply iron) → apo-target proteins matured to holo-enzymes.`

**Redundancy and regulation.** The cell maintains an interconnected **carrier network** ("ErpA, IscA, SufA, and NfuA," plus the glutaredoxin GrxD) that bridges the housekeeping **ISC** and stress-responsive **SUF** systems (Fisher et al. 2024, PMID 38944118). Among ATCs, "ErpA is the only ATC essential under aerobiosis," while IscA and SufA are partially redundant (Mandin et al. 2016, PMID 27651365). This redundancy explains why *iscA* single mutants show only a "small but appreciable" defect in Fe-S enzyme activity (Tokumoto & Takahashi 2001, PMID 11432781), even though IscA has non-redundant roles for specific clients (e.g., FHL; Pinske et al. 2013, PMID 23558265). IscA is also reported dispensable under anaerobic conditions in an ISC-only background (Tanaka et al. 2016, PMID 26560204), consistent with condition-dependent redundancy.

**Reduced redundancy in *P. putida* (this study).** Database searches of KT2440 reveal a Fe-S biogenesis complement that is notably simpler than *E. coli*'s: the organism has the complete **ISC** operon plus the ATC carriers **ErpA (PP_0433)** and **NfuA (PP_2378)**, but **no canonical SUF operon and, critically, no SufA paralogue** (searches for *sufA/sufB/sufD/sufS/sufE* return no cognate SUF genes). Consequently IscA is the **sole IscA/SufA-type A-type carrier** in *P. putida*, so its aerobic iron-chaperone/cluster-carrier role is **less buffered** than in *E. coli* (where SufA can partially substitute). This suggests a comparatively more prominent, less redundant role for PP_0844 in this obligate aerobe — an inference from annotation searches that merits direct experimental verification.

The end products of the pathway — mature Fe–S proteins — are essential for respiration, the TCA cycle (aconitase), isoprenoid biosynthesis (IspG/IspH), DNA repair, and gene regulation, so IscA contributes indirectly but importantly to central metabolism.

---

## 4. Subcellular Localization

IscA functions in the **bacterial cytoplasm**. It is a soluble protein with no signal peptide or transmembrane segment (107 aa, consistent with the compact soluble ATC fold), and it acts on cytoplasmic scaffolds (IscU) and cytoplasmic/inner-membrane-associated apoprotein clients. Its membership in the cytoplasmic Fe-S trafficking network (Fisher et al. 2024, PMID 38944118) situates its activity in the cytosol, where it can also deliver clusters to membrane-embedded complexes (e.g., FHL) from the cytoplasmic face. In *P. putida* this network comprises the ISC system plus the carriers IscA, ErpA and NfuA (no SUF pathway; see §3).

---

## 5. Evidence Summary

| Claim | Evidence type | Source |
|---|---|---|
| IscA is an A-type carrier delivering [4Fe-4S] to targets | Experimental (genetics, *E. coli*) | PMID 33782054 |
| Three conserved Cys ligate an exposed [2Fe-2S] across an asymmetric dimer | Experimental (X-ray structure, *T. elongatus*) | PMID 16730357 |
| Q88PK6 retains the three functional cysteines (C35, C99, C101) | Bioinformatic (sequence analysis, this study) | UniProt Q88PK6 + PMID 16730357 |
| IscA acts downstream of IscS/IscU in the *isc* operon | Experimental (operon mutagenesis) | PMID 11432781; 10393315 |
| Non-redundant delivery to specific clients (FHL) | Experimental (deletion phenotypes) | PMID 23558265 |
| Partial redundancy with SufA/ErpA; ErpA essential aerobically | Experimental / review | PMID 27651365; 26560204 |
| Part of cytoplasmic ISC↔SUF carrier network incl. GrxD | Experimental (chemoproteomics) | PMID 38944118 |
| Distinct from degenerate ATC* (lacking Cys) of NfuA | Experimental / phylogenomic | PMID 22966982 |
| IscA is an iron chaperone; iron binding is oxygen-dependent (aerobic) | Experimental (in vivo + in vitro, *E. coli*) | PMID 20942799; 16877383 |
| IscU (not IscA) is the preferred de novo cluster scaffold | Experimental (in vitro reconstitution) | PMID 16877383 |
| PP_0844 sits in a complete, canonically ordered *P. putida* isc operon (PP_0841–0847) | Bioinformatic (genomic synteny, this study) | UniProt/KEGG; PMID 11432781 |
| *P. putida* has ISC + ErpA/NfuA but no SUF operon or SufA paralogue → IscA less redundant | Bioinformatic (annotation search, this study) | UniProt/KEGG; PMID 38944118 |

---

## 6. Supported and Refuted Hypotheses

**Supported**
- H1: IscA is an Fe–S cluster carrier/chaperone in the ISC pathway (not a catalytic enzyme). ✔
- H2: P. putida IscA retains the functional cluster-ligating cysteine triad. ✔ (sequence analysis)
- H3: IscA acts in the cytoplasm and delivers clusters to specific apoproteins with partial redundancy among ATCs. ✔

**Refuted / not supported**
- That IscA performs de novo cluster synthesis or sulfur mobilization — those are IscS/IscU functions; IscA is downstream. ✗
- That IscA is individually essential — single *iscA* deletion has only a modest phenotype due to ATC redundancy. ✗

---

## 7. Limitations and Future Directions

- Nearly all direct functional/structural data derive from *E. coli* and cyanobacterial orthologs; there is little *P. putida*-specific experimental characterization of PP_0844. Functional assignment for Q88PK6 is by strong homology and conserved-motif inference rather than direct in-organism assay.
- The long-debated "scaffold vs. iron-chaperone vs. cluster-carrier" emphasis of IscA is condition- and organism-dependent; the precise balance in *P. putida* (an obligate aerobe with active oxidative metabolism) is untested.
- **Future work:** (i) *P. putida* Δ*iscA* / Δ*sufA* / Δ*erpA* phenotyping under aerobic vs. iron-limited stress; (ii) in vitro reconstitution to confirm Fe/[2Fe–2S] binding by recombinant Q88PK6; (iii) identify P. putida-specific client apoproteins (e.g., ferredoxins, aconitase, IspG/IspH) that depend on IscA.

---

### Gene identity verification (as required)
- Symbol **iscA** ✔ matches "Iron-binding protein IscA / Iron-sulfur cluster assembly protein."
- Organism ✔ *Pseudomonas putida* KT2440 (OX=160488), locus PP_0844.
- Family/domains ✔ HesB/IscA family; ATAP core (IPR000361), FeS-cluster-insertion conserved site (IPR017870), HesB-like sf (IPR035903) — all consistent with the literature above.
- No conflicting "same-symbol, different-gene" ambiguity was encountered; the eukaryotic "ISCA/MagR" magnetoreception literature (e.g., PMID 36183809) refers to homologous ISCA proteins and does not contradict the bacterial IscA carrier function assigned here.


## Artifacts

- [OpenScientist final report](iscA-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](iscA-deep-research-openscientist_artifacts/final_report.pdf)