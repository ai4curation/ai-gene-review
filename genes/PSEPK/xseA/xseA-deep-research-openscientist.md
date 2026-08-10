---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-25T16:42:45.006083'
end_time: '2026-07-25T18:19:43.787569'
duration_seconds: 5818.78
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: xseA
  gene_symbol: xseA
  uniprot_accession: Q88P26
  protein_description: 'RecName: Full=Exodeoxyribonuclease 7 large subunit {ECO:0000255|HAMAP-Rule:MF_00378};
    EC=3.1.11.6 {ECO:0000255|HAMAP-Rule:MF_00378}; AltName: Full=Exodeoxyribonuclease
    VII large subunit {ECO:0000255|HAMAP-Rule:MF_00378}; Short=Exonuclease VII large
    subunit {ECO:0000255|HAMAP-Rule:MF_00378};'
  gene_info: Name=xseA {ECO:0000255|HAMAP-Rule:MF_00378}; OrderedLocusNames=PP_1027;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the XseA family. {ECO:0000255|HAMAP-
  protein_domains: Exonuc_VII_L. (IPR003753); Exonuc_VII_lsu_C. (IPR020579); OB-fold_nuc-bd_dom.
    (IPR025824); Exonuc_VII_L (PF02601); tRNA_anti_2 (PF13742)
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
citation_count: 12
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: xseA-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: xseA-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88P26
- **Protein Description:** RecName: Full=Exodeoxyribonuclease 7 large subunit {ECO:0000255|HAMAP-Rule:MF_00378}; EC=3.1.11.6 {ECO:0000255|HAMAP-Rule:MF_00378}; AltName: Full=Exodeoxyribonuclease VII large subunit {ECO:0000255|HAMAP-Rule:MF_00378}; Short=Exonuclease VII large subunit {ECO:0000255|HAMAP-Rule:MF_00378};
- **Gene Information:** Name=xseA {ECO:0000255|HAMAP-Rule:MF_00378}; OrderedLocusNames=PP_1027;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the XseA family. {ECO:0000255|HAMAP-
- **Key Domains:** Exonuc_VII_L. (IPR003753); Exonuc_VII_lsu_C. (IPR020579); OB-fold_nuc-bd_dom. (IPR025824); Exonuc_VII_L (PF02601); tRNA_anti_2 (PF13742)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "xseA" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'xseA' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **xseA** (gene ID: xseA, UniProt: Q88P26) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *xseA* (Q88P26) — Exodeoxyribonuclease VII Large Subunit in *Pseudomonas putida* KT2440

## Summary

The gene **xseA** (ordered locus **PP_1027**; UniProt **Q88P26**) of *Pseudomonas putida* KT2440 encodes the **large, catalytic subunit of Exodeoxyribonuclease VII (Exonuclease VII, ExoVII; EC 3.1.11.6)**, a single-strand-specific DNA exonuclease that participates in bacterial genome maintenance. The 459-amino-acid protein belongs to the **XseA family** (HAMAP rule MF_00378) and carries the diagnostic Exonuc_VII_L (PF02601) catalytic domain together with an N-terminal OB-fold nucleic-acid-binding domain. All family and domain assignments are consistent with the UniProt identity provided, and bioinformatic analysis confirms that the four catalytic residues defined experimentally in the *Escherichia coli* enzyme are strictly conserved in the *P. putida* ortholog. The gene symbol is unambiguous: "xseA" universally denotes the exonuclease VII large subunit across bacteria, and no conflicting gene of the same symbol was encountered.

Functionally, ExoVII is an obligate heterooligomer of the large subunit **XseA** (encoded here) and a small subunit **XseB** (xseB). The holoenzyme processively degrades **single-stranded DNA from both the 5′ and 3′ termini**, releasing short oligonucleotide products (predominantly 4–12 nucleotides), and — unusually among nucleases — requires **no divalent metal cofactor**. A 2024 cryo-EM structure of the *E. coli* enzyme revealed a strikingly large, elongated **XseA₄·XseB₂₄ holo-complex** whose catalytic sites are buried in the interior and accessible only through narrow pores, providing an elegant structural explanation for the enzyme's strict single-strand specificity: only flexible ssDNA can thread into the active sites. XseA itself contributes the OB-fold DNA-binding module, the metal-independent catalytic center (a fold related to 3-dehydroquinate dehydratase), and the extended α-helical/coiled-coil segment that scaffolds multiple XseB copies and drives oligomerization.

Biologically, ExoVII acts in the **cytoplasm** on chromosomal DNA as one of several redundant single-strand exonucleases (alongside RecJ, ExoI, and ExoX). It contributes to **methyl-directed mismatch-repair excision**, **UV and recombinational DNA repair**, **mutation avoidance** (suppressing frameshifts and quasipalindrome-associated mutagenesis), **processing of multicopy single-stranded DNA (msDNA)**, **removal of 3′ single-stranded flaps** to prevent aberrant re-replication, and — as newly established — **repair of covalent DNA–protein crosslinks (DPCs)**. It is important to note that **no direct experimental study of the *P. putida* protein exists**; the functional annotation is inferred with high confidence from well-characterized orthologs in *E. coli* and *Thermotoga maritima* combined with strong sequence and structural conservation.

---

## Gene/Protein Identity Verification

Before presenting the functional findings, the mandatory identity checks were completed:

| Verification step | Result |
|---|---|
| Gene symbol matches protein description | ✅ "xseA" is the universal symbol for the exonuclease VII **large subunit**; matches "Exodeoxyribonuclease VII large subunit" |
| Organism correct | ✅ *Pseudomonas putida* KT2440 (ATCC 47054 / DSM 6125), locus PP_1027 |
| Protein family/domains align with literature | ✅ XseA family (MF_00378); Exonuc_VII_L (PF02601), OB-fold — all consistent with characterized ExoVII large subunits |
| Symbol ambiguity / conflicting literature | ✅ None. "xseA" is not shared with an unrelated gene; literature is unambiguous |

**Conclusion:** The gene symbol is unambiguous and the domain architecture matches the exonuclease VII large-subunit family precisely. Research proceeded with confidence, drawing mechanistic detail from *E. coli* and *T. maritima* orthologs and mapping it to Q88P26 by sequence/structure conservation.

---

## Key Findings

### Finding 1 — XseA is the catalytic large subunit of a single-strand-specific DNA exonuclease (EC 3.1.11.6)

*Pseudomonas putida* XseA (Q88P26, PP_1027) belongs to the XseA family (HAMAP MF_00378) and contains the Exonuc_VII_L (PF02601) catalytic domain and an OB-fold nucleic-acid-binding domain. The catalytic activity of the enzyme it forms — Exodeoxyribonuclease VII — was defined biochemically in the classic *E. coli* studies of Chase and Richardson. The canonical enzyme is **"specific for single-stranded DNA and can initiate hydrolysis at both 5′ and 3′ termini... The limit products of the reaction are oligonucleotides, predominantly in the range of tetramers to dodecamers. DNA is hydrolyzed by the enzyme in a processive fashion"** ([PMID: 1103829](https://pubmed.ncbi.nlm.nih.gov/1103829/)). This establishes the enzyme's four defining biochemical properties: **(i)** single-stranded DNA substrate specificity, **(ii)** bidirectional (5′→3′ *and* 3′→5′) initiation, **(iii)** processivity, and **(iv)** oligonucleotide (≈4–12 nt) end products. ExoVII additionally requires no divalent cations, distinguishing it from most nucleases.

Bioinformatic mapping strongly supports transfer of this activity to the *P. putida* protein. The four *E. coli* catalytic residues (D155, R205, H238, D241) are **strictly conserved** in Q88P26 as **D161, R210, H243, D246** (≈46% global identity by Needleman–Wunsch alignment), including the diagnostic **GGGSLEDLW** and **GHETDV** signature motifs. The two-subunit composition is likewise conserved: ExoVII "is comprised of two subunits (XseA and XseB) that are highly conserved and present in most sequenced prokaryotic genomes" ([PMID: 18812402](https://pubmed.ncbi.nlm.nih.gov/18812402/)), confirming that the *P. putida* XseA is a canonical member of a broadly distributed family.

### Finding 2 — ExoVII is an obligate heterooligomer with a defined domain-function architecture

ExoVII activity requires **both** subunits. Genetic work in *E. coli* showed that xseB is a structural gene, because "Exonuclease VII purified from KLC835 (xseA⁺ xseB3) is more heat labile than enzyme purified from the parent strain... showing that xseB is a structural gene for exonuclease VII" ([PMID: 6350262](https://pubmed.ncbi.nlm.nih.gov/6350262/)). Independent reconstitution work confirmed that "both subunits were required for enzyme activity" ([PMID: 26626352](https://pubmed.ncbi.nlm.nih.gov/26626352/)).

Domain dissection of XseA established a clear division of labor within the large subunit: **"the OB-fold domain is responsible for DNA binding, the coiled-coil domain is involved in binding multiple copies of the XseB subunit and residues D155, R205, H238 and D241 of the middle domain are important for the catalytic activity but not for DNA binding"** ([PMID: 22718974](https://pubmed.ncbi.nlm.nih.gov/22718974/)). The 459-residue *P. putida* XseA reproduces this three-part architecture:

| Domain | Location in XseA | Function |
|---|---|---|
| N-terminal OB-fold | N-terminus | Single-stranded DNA binding |
| Middle catalytic domain | Central | Phosphodiester hydrolysis (conserved D161/R210/H243/D246) |
| C-terminal coiled-coil / α-helical segment | C-terminus | Scaffolds multiple XseB copies; drives oligomerization |

The catalytic residues are essential for nuclease chemistry but not for substrate binding, mirroring the conserved residues identified in the *P. putida* sequence.

### Finding 3 — ExoVII functions in the cytoplasm in DNA repair, mismatch-repair excision, and mutation avoidance

ExoVII is one of a set of **redundant single-strand-specific exonucleases** — with RecJ, ExoI, and ExoX — that carry out the excision step of methyl-directed mismatch repair: mismatch correction depends on "three redundant single-strand DNA-specific exonucleases (RecJ, ExoI, and ExoVII)" ([PMID: 11418610](https://pubmed.ncbi.nlm.nih.gov/11418610/)). This redundancy extends to general DNA repair: while no single exonuclease mutant is markedly UV-sensitive, "the RecJ⁻ ExoVII⁻ double mutant was extremely sensitive. The addition of an ExoI⁻ mutation augmented this sensitivity, suggesting that all three exonucleases play partially redundant roles in DNA repair" ([PMID: 9584082](https://pubmed.ncbi.nlm.nih.gov/9584082/)).

ExoVII also protects the genome by removing 3′ single-stranded DNA that would otherwise trigger aberrant replication restart: "cells must have either RecG or a 3′ single-stranded DNA (ssDNA) exonuclease, which can be exonuclease I, exonuclease VII, or SbcCD" ([PMID: 20647503](https://pubmed.ncbi.nlm.nih.gov/20647503/)). Its excision activity is regulated by mismatch-repair machinery — MutS and UvrD stimulate ExoVII action on duplex substrates in an ATP-dependent manner while paradoxically protecting ssDNA targets, implying a "destabilized duplex" intermediate in exonuclease-mediated strand repair ([PMID: 19618961](https://pubmed.ncbi.nlm.nih.gov/19618961/)). Loss of ExoI/ExoVII also elevates frameshift mutation and stimulates quasipalindrome-associated mutagenesis ([PMID: 16547019](https://pubmed.ncbi.nlm.nih.gov/16547019/); [PMID: 10986118](https://pubmed.ncbi.nlm.nih.gov/10986118/)), underscoring a **mutation-avoidance** role. The enzyme acts on **cytoplasmic chromosomal DNA**; it possesses no signal or localization sequence and is a soluble, cation-independent protein.

### Finding 4 — ExoVII is a large XseA₄·XseB₂₄ holo-complex with buried catalytic sites gated by steric access (cryo-EM, 2024)

A 2024 cryo-EM structure (Liu, Hauk, Yan & Berger, *PNAS*) provided the first high-resolution architecture of ExoVII and transformed understanding of its specificity. The *E. coli* enzyme is **"a highly elongated XseA₄·XseB₂₄ holo-complex. Each XseA subunit dimerizes through a central extended α-helical segment decorated by six XseB subunits and a C-terminal, domain-swapped β-barrel element; two XseA₂·XseB₁₂ subcomplexes further associate using N-terminal OB folds and catalytic domains to form a spindle-shaped, catenated octaicosamer"** ([PMID: 38271335](https://pubmed.ncbi.nlm.nih.gov/38271335/)).

Two mechanistic insights follow. First, the catalytic domain "adopt[s] a nuclease fold related to 3-dehydroquinate dehydratases," and the active sites "are sequestered in the center of the complex and accessible only through large pores formed between XseA tetramers." Second, **"substrate selectivity is controlled by steric access to its nuclease elements and... tetramer dissociation results from substrate DNA binding"** ([PMID: 38271335](https://pubmed.ncbi.nlm.nih.gov/38271335/)). In other words, the enzyme's single-strand specificity is not chemically imposed at the active site but **sterically imposed by the architecture**: only thin, flexible ssDNA can reach the buried catalytic centers, while rigid duplex DNA is excluded. Substrate binding triggers a conformational change (tetramer dissociation) that couples recognition to catalysis. The 459-aa *P. putida* XseA preserves all elements required for this assembly — the OB-fold, the DHQase-like catalytic domain (D161/R210/H243/D246), and the long central α-helical/coiled-coil segment.

### Finding 5 — ExoVII participates in DNA–protein crosslink (DPC) repair, paralleling Mre11-Rad50/SbcCD by convergent evolution

The same 2024 study extended ExoVII's functional repertoire beyond classical ssDNA trimming. It reported that **"ExoVII participates in multiple nucleic acid-dependent pathways including the processing of multicopy single-stranded DNA and the repair of covalent DNA-protein crosslinks (DPCs)"** ([PMID: 38271335](https://pubmed.ncbi.nlm.nih.gov/38271335/)). The role in msDNA processing is corroborated by in vivo work showing that multicopy single-stranded DNAs Ec83 and Ec78 are natural ExoVII substrates, cleaved between the fourth and fifth nucleotide from the 5′ end ([PMID: 26626352](https://pubmed.ncbi.nlm.nih.gov/26626352/)).

Structurally, ExoVII shows a remarkable case of convergent evolution: "Despite a lack of sequence and fold homology, the physical organization of ExoVII is reminiscent of Mre11·Rad50/SbcCD ATP-dependent nucleases used in the repair of double-stranded DNA breaks, including those formed by DPCs through aberrant topoisomerase activity, suggesting that there may have been convergent evolutionary pressure to contend with such damage events" ([PMID: 38271335](https://pubmed.ncbi.nlm.nih.gov/38271335/)). This positions ExoVII within the cell's toolkit for resolving protein-blocked DNA ends — a role of potential relevance to *P. putida*, an organism prized for its metabolic robustness and stress tolerance.

---

## Mechanistic Model / Interpretation

Integrating the five findings yields a coherent picture of XseA's role in *P. putida*:

```
                 Exodeoxyribonuclease VII (ExoVII) — EC 3.1.11.6
                 =================================================
   Composition:  XseA (large, catalytic; PP_1027 / Q88P26)  x4
                 XseB (small, structural; xseB)              x24
                 --> XseA4 . XseB24 elongated holo-complex

   XseA domain map (459 aa):
   +-------------+----------------------+---------------------------+
   |  OB-fold    |  Catalytic (middle)  |  a-helical / coiled-coil  |
   |  ssDNA bind |  D161 R210 H243 D246 |  binds XseB, oligomerizes |
   +-------------+----------------------+---------------------------+
                 DHQase-like nuclease fold; metal-INDEPENDENT

   Reaction:     ssDNA  --(processive, from BOTH 5' and 3' ends)-->
                 oligonucleotides (~4-12 nt), no Mg2+/Mn2+ required

   Specificity:  Active sites BURIED inside complex; reachable only
                 through narrow pores => only flexible ssDNA fits.
                 Substrate binding -> tetramer dissociation (gating).

   Localization: CYTOPLASM, acting on chromosomal DNA
```

**Primary function.** XseA is the catalytic engine of a single-strand-specific DNA exonuclease. It hydrolyzes phosphodiester bonds in ssDNA, initiating at either terminus and moving processively to yield short oligonucleotides. The metal-independent chemistry (a DHQase-like fold) and steric gating together produce the enzyme's defining substrate preference for single-stranded over double-stranded DNA.

**Substrate specificity.** The substrate is single-stranded DNA — including displaced/nascent strands at replication forks, excision intermediates in mismatch repair, 3′ ssDNA flaps, and multicopy single-stranded DNA (msDNA). Duplex DNA is excluded by architecture, not by chemistry.

**Cellular location.** The enzyme operates in the **cytoplasm** on the bacterial chromosome. It carries no export/localization signal and is a soluble, cation-independent complex.

**Pathways.** ExoVII is embedded in a redundant network of ssDNA exonucleases (RecJ, ExoI, ExoX) supporting:
- Methyl-directed **mismatch-repair excision** (stimulated by MutS/UvrD);
- **UV / recombinational DNA repair** (redundant with RecJ, ExoI);
- **Mutation avoidance** (suppressing frameshifts and hairpin/quasipalindrome-templated mutagenesis, and preventing SOS-driven, DinB/PolIV-dependent mutagenesis);
- **3′ ssDNA flap removal** to avert PriA-mediated aberrant re-replication (redundant with RecG, SbcCD);
- **msDNA processing**; and
- **DNA–protein crosslink (DPC) repair**, echoing the Mre11-Rad50/SbcCD machinery through convergent evolution.

For *P. putida* specifically, this predicts that XseA contributes to genome stability and stress resilience, though redundancy with RecJ/ExoI likely renders a single xseA deletion phenotypically mild under standard conditions — consistent with the redundancy observed in *E. coli*.

---

## Evidence Base

| PMID | Study focus | Contribution to this annotation |
|---|---|---|
| [1103829](https://pubmed.ncbi.nlm.nih.gov/1103829/) | *Exonuclease VII of E. coli* (Chase & Richardson) | Defines ssDNA specificity, bidirectional initiation, processivity, and 4–12 nt oligonucleotide products (Finding 1) |
| [18812402](https://pubmed.ncbi.nlm.nih.gov/18812402/) | Thermophilic ExoVII in *T. maritima* | Confirms two-subunit (XseA/XseB) composition and broad conservation; identifies conserved catalytic aspartates (Findings 1, 2) |
| [22718974](https://pubmed.ncbi.nlm.nih.gov/22718974/) | Structural domains of ExoVII (Poleszak et al.) | Maps OB-fold→DNA binding, coiled-coil→XseB binding, and D155/R205/H238/D241→catalysis (Finding 2) |
| [6350262](https://pubmed.ncbi.nlm.nih.gov/6350262/) | E. coli ExoVII mutants | Establishes XseB as a structural subunit; holoenzyme requires both subunits (Finding 2) |
| [26626352](https://pubmed.ncbi.nlm.nih.gov/26626352/) | Cell death mediated by XseA | Identifies msDNA (Ec83, Ec78) as in vivo substrates; both subunits required for activity (Findings 2, 5) |
| [11418610](https://pubmed.ncbi.nlm.nih.gov/11418610/) | Redundant exonucleases in MMR | Places ExoVII among three redundant ssDNA exonucleases in mismatch-repair excision (Finding 3) |
| [9584082](https://pubmed.ncbi.nlm.nih.gov/9584082/) | ssDNA exonucleases in repair/mutation avoidance | Demonstrates redundant UV-repair role with RecJ and ExoI (Finding 3) |
| [20647503](https://pubmed.ncbi.nlm.nih.gov/20647503/) | RecG and ssDNA exonucleases vs PriA lethality | Shows ExoVII removes 3′ ssDNA to prevent aberrant re-replication (Finding 3) |
| [19618961](https://pubmed.ncbi.nlm.nih.gov/19618961/) | MutS/UvrD stimulate exonuclease action | Links ExoVII to regulated MMR excision via a "destabilized duplex" intermediate (Finding 3) |
| [16547019](https://pubmed.ncbi.nlm.nih.gov/16547019/) | ExoI/ExoVII and frameshift mutagenesis | Supports mutation-avoidance role; loss elevates SOS/PolIV-dependent frameshifts (Finding 3) |
| [10986118](https://pubmed.ncbi.nlm.nih.gov/10986118/) | Quasipalindrome mutational hotspot | ExoI/ExoVII loss stimulates hairpin-templated mutagenesis; ExoVII aborts replicative misalignment (Finding 3) |
| [38271335](https://pubmed.ncbi.nlm.nih.gov/38271335/) | Cryo-EM structure of ExoVII (2024) | Defines XseA₄·XseB₂₄ architecture, steric-gated specificity, DPC/msDNA roles, convergence with Mre11-Rad50/SbcCD (Findings 4, 5) |
| [10080932](https://pubmed.ncbi.nlm.nih.gov/10080932/) | ssDNA backbone recognition by nucleases | Suggests ExoVII recognizes sequence-dependent ssDNA backbone conformation (supporting context) |
| [10049912](https://pubmed.ncbi.nlm.nih.gov/10049912/) | RNase T suppresses exonuclease-deficiency UV sensitivity | Reinforces redundant ssDNA-exonuclease network in UV repair (supporting context) |

**How the evidence converges.** The biochemical foundation (Chase & Richardson, [PMID: 1103829](https://pubmed.ncbi.nlm.nih.gov/1103829/)) defines the reaction; the genetic and domain studies ([PMID: 6350262](https://pubmed.ncbi.nlm.nih.gov/6350262/), [PMID: 22718974](https://pubmed.ncbi.nlm.nih.gov/22718974/), [PMID: 18812402](https://pubmed.ncbi.nlm.nih.gov/18812402/)) define the subunit and domain architecture; the pathway studies ([PMID: 11418610](https://pubmed.ncbi.nlm.nih.gov/11418610/), [PMID: 9584082](https://pubmed.ncbi.nlm.nih.gov/9584082/), [PMID: 20647503](https://pubmed.ncbi.nlm.nih.gov/20647503/), [PMID: 19618961](https://pubmed.ncbi.nlm.nih.gov/19618961/), [PMID: 16547019](https://pubmed.ncbi.nlm.nih.gov/16547019/), [PMID: 10986118](https://pubmed.ncbi.nlm.nih.gov/10986118/)) place the enzyme in mismatch repair, UV repair, and mutation avoidance; and the 2024 cryo-EM study ([PMID: 38271335](https://pubmed.ncbi.nlm.nih.gov/38271335/)) unifies these into a mechanistic model and adds DPC repair. Strict conservation of the catalytic residues (D161/R210/H243/D246) and domain architecture in Q88P26 licenses transfer of this knowledge to *P. putida*.

---

## Limitations and Knowledge Gaps

1. **No direct study of the *P. putida* protein.** Every mechanistic and functional claim is inferred from orthologs — chiefly *E. coli*, with structural fold information from *T. maritima*. There is no published biochemical, genetic, or structural characterization of Q88P26/PP_1027 itself. The annotation is a high-confidence *inference* by homology, not a direct measurement.

2. **Homology-based residue mapping.** The identification of catalytic residues D161/R210/H243/D246 rests on pairwise alignment (~46% global identity) to *E. coli* XseA. While alignment quality is strong and the signature motifs (GGGSLEDLW, GHETDV) are present, the catalytic assignment has not been experimentally verified in *P. putida*.

3. **Stoichiometry generalization.** The XseA₄·XseB₂₄ architecture was determined for the *E. coli* enzyme. Although the assembly elements are conserved in Q88P26, the precise oligomeric state of the *P. putida* enzyme has not been measured and could differ.

4. **Physiological role in *P. putida* is uncharacterized.** The contributions of xseA to mismatch repair, UV resistance, mutation rate, msDNA metabolism (if *P. putida* produces msDNA), and DPC repair have not been tested in this organism. Redundancy with RecJ/ExoI likely masks single-mutant phenotypes, complicating functional assignment.

5. **Metal independence assumed.** The cation-independence of ExoVII was established in *E. coli*; it is presumed but not verified for the *P. putida* enzyme.

6. **The XseA-mediated cell-death phenomenon** ([PMID: 26626352](https://pubmed.ncbi.nlm.nih.gov/26626352/)) — in which overexpressed XseA without XseB triggers an apoptosis-like death via a putative caspase cleavage — is an *E. coli* observation of uncertain physiological significance and unknown relevance to *P. putida*; it is noted but not incorporated as a core function.

---

## Proposed Follow-up Experiments / Actions

1. **Experimental confirmation of enzymatic activity.** Recombinantly express *P. putida* XseA (PP_1027) together with its cognate XseB and assay nuclease activity on defined ssDNA substrates. Confirm bidirectional initiation, processivity, oligonucleotide product size, and metal independence to validate the EC 3.1.11.6 assignment directly.

2. **Site-directed mutagenesis of predicted catalytic residues.** Mutate D161, R210, H243, and D246 individually to alanine and test loss of nuclease activity while retaining ssDNA binding — directly testing the homology-based catalytic assignment.

3. **Determine the oligomeric state.** Use size-exclusion chromatography with multi-angle light scattering (SEC-MALS), native mass spectrometry, or cryo-EM to test whether the *P. putida* enzyme forms the XseA₄·XseB₂₄ assembly seen in *E. coli*.

4. **Genetic phenotyping in *P. putida*.** Construct a clean ΔxseA deletion (and ΔxseA ΔrecJ / ΔxseA Δsbccd double mutants) and measure UV/MMS sensitivity, spontaneous mutation and frameshift rates, and mismatch-repair proficiency to reveal the in vivo, redundancy-masked role.

5. **Test the DPC-repair role.** Challenge wild-type and ΔxseA *P. putida* with topoisomerase poisons or formaldehyde (DPC-inducing agents) and assess survival and DPC-clearance kinetics to evaluate the newly proposed crosslink-repair function in this organism.

6. **Structural modeling and validation.** Generate an AlphaFold model of *P. putida* XseA(+XseB), verify the OB-fold, DHQase-like catalytic domain, and coiled-coil scaffold, and superpose against the *E. coli* cryo-EM structure to confirm conservation of the steric-gating architecture.

---

## Conclusion

The gene **xseA** (Q88P26; PP_1027) of *Pseudomonas putida* KT2440 encodes the **large, catalytic subunit of Exodeoxyribonuclease VII (EC 3.1.11.6)**, a metal-independent, single-strand-specific DNA exonuclease. Together with the small subunit XseB, it forms a large, elongated XseA₄·XseB₂₄ holo-complex that processively degrades single-stranded DNA from both ends into short oligonucleotides, with specificity enforced by steric gating of buried active sites. XseA supplies the OB-fold DNA-binding module, the DHQase-like catalytic center (conserved D161/R210/H243/D246), and the oligomerization scaffold. Operating in the **cytoplasm** on chromosomal DNA within a redundant network of ssDNA exonucleases, the enzyme supports mismatch-repair excision, UV/recombinational repair, mutation avoidance, msDNA processing, 3′-flap removal, and DNA–protein-crosslink repair. All mechanistic detail is inferred from well-characterized *E. coli* and *T. maritima* orthologs plus strong sequence/structure conservation, as no direct study of the *P. putida* protein currently exists.


## Artifacts

- [OpenScientist final report](xseA-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](xseA-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:1103829
2. PMID:18812402
3. PMID:6350262
4. PMID:26626352
5. PMID:22718974
6. PMID:11418610
7. PMID:9584082
8. PMID:20647503
9. PMID:19618961
10. PMID:16547019
11. PMID:10986118
12. PMID:38271335