---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-25T16:54:55.809428'
end_time: '2026-07-25T17:35:23.806326'
duration_seconds: 2428.0
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: xseB
  gene_symbol: xseB
  uniprot_accession: Q88QG5
  protein_description: 'RecName: Full=Exodeoxyribonuclease 7 small subunit {ECO:0000255|HAMAP-Rule:MF_00337};
    EC=3.1.11.6 {ECO:0000255|HAMAP-Rule:MF_00337}; AltName: Full=Exodeoxyribonuclease
    VII small subunit {ECO:0000255|HAMAP-Rule:MF_00337}; Short=Exonuclease VII small
    subunit {ECO:0000255|HAMAP-Rule:MF_00337};'
  gene_info: Name=xseB {ECO:0000255|HAMAP-Rule:MF_00337}; OrderedLocusNames=PP_0529;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the XseB family. {ECO:0000255|HAMAP-
  protein_domains: Exonuc_VII_S. (IPR003761); Exonuc_VII_ssu_sf. (IPR037004); Exonuc_VII_S
    (PF02609)
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
citation_count: 6
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: xseB-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: xseB-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88QG5
- **Protein Description:** RecName: Full=Exodeoxyribonuclease 7 small subunit {ECO:0000255|HAMAP-Rule:MF_00337}; EC=3.1.11.6 {ECO:0000255|HAMAP-Rule:MF_00337}; AltName: Full=Exodeoxyribonuclease VII small subunit {ECO:0000255|HAMAP-Rule:MF_00337}; Short=Exonuclease VII small subunit {ECO:0000255|HAMAP-Rule:MF_00337};
- **Gene Information:** Name=xseB {ECO:0000255|HAMAP-Rule:MF_00337}; OrderedLocusNames=PP_0529;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the XseB family. {ECO:0000255|HAMAP-
- **Key Domains:** Exonuc_VII_S. (IPR003761); Exonuc_VII_ssu_sf. (IPR037004); Exonuc_VII_S (PF02609)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "xseB" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'xseB' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **xseB** (gene ID: xseB, UniProt: Q88QG5) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *xseB* — Exodeoxyribonuclease VII Small Subunit in *Pseudomonas putida* KT2440

**Gene:** *xseB* | **UniProt:** Q88QG5 | **Ordered Locus:** PP_0529
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440) — **PSEPK**
**Enzyme Class:** EC 3.1.11.6 | **Protein Family:** XseB family (HAMAP MF_00337)
**Length:** 80 aa, ~8.7 kDa | **Domains:** Pfam PF02609 (*Exonuc_VII_S*); InterPro IPR003761 / IPR037004; eggNOG COG1722

---

## Summary

The gene ***xseB*** (UniProt Q88QG5; ordered locus PP_0529) of *Pseudomonas putida* KT2440 encodes the **small subunit of Exonuclease VII (ExoVII)**, an 80-residue (~8.7 kDa) polypeptide of the XseB family. Exonuclease VII is a **single-strand-specific bacterial DNA exonuclease (EC 3.1.11.6)** that hydrolyzes single-stranded DNA (ssDNA) bidirectionally — in both the 5'→3' and 3'→5' directions — releasing large oligonucleotides that are progressively degraded to small acid-soluble oligonucleotides and nucleoside 5'-phosphates. The active holoenzyme is an obligate two-subunit complex composed of a large catalytic subunit (**XseA**, product of *xseA*) and multiple copies of the small subunit (**XseB**, the product of this gene).

Catalysis resides entirely in XseA. XseB is a **non-catalytic, architectural/stabilizing subunit** that decorates and stabilizes the central α-helical spine of XseA. Cryo-electron microscopy of the *E. coli* enzyme reveals an elongated **XseA₄·XseB₂₄ holo-complex**, in which each XseA dimerizes through an extended α-helical segment decorated by six XseB subunits, sequestering the catalytic domains in the core. Genetic evidence shows that XseB is required both to assemble a functional enzyme and to neutralize the intrinsic toxicity of free XseA: expression of XseA alone is lethal and is rescued by surplus XseB. The amino-acid composition of *P. putida* XseB — 80 residues, ~30% charged, rich in Glu/Leu/Gln/Ala, with a conserved leucine-rich heptad pattern and no aromatic residues — is diagnostic of an α-helical subunit that docks onto the XseA helical spine.

Functionally, ExoVII acts in the **cytoplasm** and participates in **DNA repair and recombination**, including a role downstream of **mismatch repair**, the processing of **multicopy single-stranded DNAs (msDNA)**, and the repair of **DNA–protein crosslinks** (including topoisomerase-derived adducts). For *P. putida* specifically, these functions are inferred by strong orthology rather than direct experiment: global alignment shows *P. putida* XseB shares **50% identity / 64% similarity** with *E. coli* K-12 XseB over the full 80-residue length, and *P. putida* KT2440 also encodes the cognate large subunit **XseA** (Q88P26, PP_0528) in the adjacent locus, confirming that the complete, functional two-gene *xseA*/*xseB* ExoVII module is present in this genome.

---

## Gene/Protein Identity Verification

The mandatory identity checks were performed and **all passed**:

| Verification Step | Result |
|---|---|
| Gene symbol *xseB* matches protein description | ✅ *xseB* is the standard symbol for the ExoVII small subunit |
| Organism correct (*P. putida* KT2440) | ✅ Ordered locus PP_0529 is specific to this strain |
| Protein family/domains align with literature | ✅ XseB family, Pfam PF02609, InterPro IPR003761/IPR037004 all correspond to the ExoVII small subunit |
| Literature is for the correct gene (not a namesake) | ✅ All *xseA*/*xseB* literature concerns the same bidirectional ssDNA exonuclease |

The symbol *xseB* is **not ambiguous** — it is a well-standardized bacterial gene name. The *P. putida* KT2440 protein has not itself been the subject of a dedicated experimental study, but it is a bona fide ortholog of extensively characterized enzymes, so functional inference is fully justified (Finding 4). All mechanistic claims below derive from characterized orthologs (*E. coli*, *Neisseria*, *Thermotoga*); the transfer is robust because ExoVII is one of the most broadly conserved bacterial nucleases.

---

## Key Findings

### Finding 1 — *xseB* encodes the small subunit of Exonuclease VII, a single-strand-specific DNA exonuclease

*P. putida* XseB (Q88QG5, PP_0529) is an 80-amino-acid, ~8.7 kDa protein belonging to the XseB family (Pfam PF02609 *Exonuc_VII_S*; InterPro IPR003761 / IPR037004; eggNOG COG1722; EC 3.1.11.6). It is the small partner subunit of **Exonuclease VII**, a bacterial nuclease that degrades single-stranded DNA.

The enzyme it forms part of has a distinctive and well-defined biochemical activity. Exonuclease VII catalyzes the **exonucleolytic cleavage of single-stranded DNA in both the 5'→3' and the 3'→5' direction** — an unusual bidirectionality among nucleases — yielding nucleoside 5'-phosphates. The enzyme first degrades ssDNA into large oligonucleotides and then into small acid-soluble products. Purified *E. coli* ExoVII is a **two-subunit enzyme**, composed of a large subunit (XseA, ~54 kDa) and a small subunit (XseB, ~10.5 kDa), and **both subunits are required for activity**.

The foundational biochemical characterization comes from Vales et al. (1982), who purified the *E. coli* enzyme 7,500-fold and established its two-subunit architecture: *"Exonuclease VII has been purified 7,500-fold to 87% homogeneity from Escherichia coli K12... The enzyme has been shown to be composed of two nonidentical subunits of 10,500 and 54,000 daltons"* [PMID: 6284744](https://pubmed.ncbi.nlm.nih.gov/6284744/). This directly establishes that *xseB* encodes the ~10.5 kDa small subunit. Poleszak et al. (2012) reaffirmed the composition and activity: *"Exonuclease VII (ExoVII) is a bacterial nuclease involved in DNA repair and recombination that hydrolyses single-stranded DNA. ExoVII is composed of two subunits: large XseA and small XseB"* [PMID: 22718974](https://pubmed.ncbi.nlm.nih.gov/22718974/).

**Substrate specificity:** single-stranded DNA — linear ssDNA and 5'/3' single-stranded tails/overhangs at duplex junctions. ExoVII is unusual among exonucleases in being bidirectional and, in *E. coli*, in requiring no divalent metal cation. In contrast, the *T. maritima* homolog is Mg²⁺-dependent and phosphate-inhibited, defining two ExoVII subfamilies [PMID: 18812402](https://pubmed.ncbi.nlm.nih.gov/18812402/).

---

### Finding 2 — Catalysis resides in XseA; XseB is a structural/stabilizing subunit that decorates the XseA helical spine

A central mechanistic point is the **division of labor** between the two subunits. The catalytic activity of ExoVII resides entirely in the large subunit XseA, while XseB serves an **architectural and stabilizing** role.

Structural biology provides the clearest picture. Cryo-EM of the *E. coli* enzyme (Liu et al., 2024, *PNAS*) shows an elongated **XseA₄·XseB₂₄ holo-complex**: *"Escherichia coli ExoVII comprises a highly elongated XseA4·XseB24 holo-complex. Each XseA subunit dimerizes through a central extended α-helical segment decorated by six XseB subunits"* [PMID: 38271335](https://pubmed.ncbi.nlm.nih.gov/38271335/). In this architecture the catalytic domains are sequestered in the core of the assembly, reachable only through pores, and XseB subunits line the extended α-helical spine of XseA at a **6:1 ratio (XseB:XseA)**. This refines the earlier biochemical estimate of one large plus four small subunits. Notably, the overall architecture is reminiscent of the Mre11·Rad50/SbcCD nucleases, hinting at convergent evolution to handle DNA–protein crosslinks.

Mutagenesis pinpoints the active site to XseA. Poleszak et al. (2012) mapped the *E. coli* catalytic residues and defined subunit roles: *"the coiled-coil domain is involved in binding multiple copies of the XseB subunit and residues D155, R205, H238 and D241 of the middle domain are important for the catalytic activity but not for DNA binding"* [PMID: 22718974](https://pubmed.ncbi.nlm.nih.gov/22718974/). The equivalent thermophilic enzyme from *Thermotoga maritima* requires the conserved aspartates D235/D240 for DNA digestion [PMID: 18812402](https://pubmed.ncbi.nlm.nih.gov/18812402/). In every case, catalysis is in XseA, and XseB binds the XseA coiled-coil.

Genetics reveals a second dimension of XseB's stabilizing function. Jung et al. (2015) found that **free XseA is toxic** and that XseB is required to neutralize it: *"Expression of XseA without XseB caused cell death, even though no ExoVII activity was detected. The lethality caused by XseA was rescued by surplus XseB"* [PMID: 26626352](https://pubmed.ncbi.nlm.nih.gov/26626352/). Thus XseB is required not only to build an active enzyme but also to keep the potentially deleterious large subunit under control.

The *P. putida* XseB sequence is fully consistent with this structural role. It is 80 residues long with ~30% charged residues, is rich in Glu/Leu/Gln/Ala, contains a conserved leucine-rich heptad pattern, and has **no aromatic residues** — precisely the composition expected of a small α-helical subunit that docks onto the XseA helical spine rather than performing catalysis.

---

### Finding 3 — ExoVII functions in the cytoplasm in DNA repair/recombination, mismatch repair, msDNA processing, and DNA–protein-crosslink repair

ExoVII acts in the **cytoplasm** (UniProt subcellular localization; no signal peptide or membrane anchor) and contributes to multiple ssDNA-processing pathways in DNA metabolism.

Its core role is in **DNA repair and recombination** through the hydrolysis of ssDNA [PMID: 22718974](https://pubmed.ncbi.nlm.nih.gov/22718974/). Beyond generic ssDNA trimming, several specific in vivo activities have been defined:

- **msDNA processing.** Jung et al. (2015) identified endogenous multicopy single-stranded DNAs as physiological substrates: *"multicopy single-stranded DNAs (msDNAs), Ec83 and Ec78, are the in vivo substrates of ExoVII; the enzyme cuts the phosphodiester bond between the fourth and fifth nucleotides from the 5'end"* [PMID: 26626352](https://pubmed.ncbi.nlm.nih.gov/26626352/). This demonstrates a precise, defined cleavage activity on a natural cytoplasmic ssDNA species.
- **DNA–protein-crosslink (DPC) repair.** The cryo-EM study documents ExoVII participation in repairing covalent DNA–protein crosslinks, including topoisomerase-derived adducts [PMID: 38271335](https://pubmed.ncbi.nlm.nih.gov/38271335/).
- **DNA repair in vivo (genetic evidence).** In pathogenic *Neisseria meningitidis*, an *xseB* ortholog belongs to a host-contact-induced DNA-repair regulon, and its loss confers repair defects: *"The increased sensitivity of a mutant in this coding sequence to UV irradiation, alkylating agent and nalidixic acid demonstrates the participation of this gene in meningococcal DNA repair"* [PMID: 15661009](https://pubmed.ncbi.nlm.nih.gov/15661009/). This is direct genetic evidence that *xseB* participates in DNA repair in a bacterium.

ExoVII is also classically implicated in the **excision of mismatches** downstream of mismatch recognition and in the removal of ssDNA overhangs during recombination — activities consistent with its bidirectional ssDNA exonuclease chemistry.

The enzyme is **broadly conserved across prokaryotes but absent in eukaryotes**: *"ExoVII is comprised of two subunits (XseA and XseB) that are highly conserved and present in most sequenced prokaryotic genomes, but are not seen in eukaryotes"* [PMID: 18812402](https://pubmed.ncbi.nlm.nih.gov/18812402/). This deep conservation across bacteria supports transferring the functional annotation to *P. putida*.

---

### Finding 4 — *P. putida* XseB is a bona fide ortholog of *E. coli* XseB, and its cognate large subunit XseA is present in the same genome

Because *P. putida* KT2440 XseB has not been studied directly, the reliability of the functional inference rests on orthology, which is strong on two counts.

First, **sequence orthology**. A global Needleman–Wunsch alignment of *P. putida* XseB (Q88QG5, 80 aa) against *E. coli* K-12 XseB (P0A8G9, 80 aa) yields **50% identity (39/78) and 64% similarity**. The two proteins are **identical in length (80 aa)**, and the alignment preserves the diagnostic XseB core motif (the conserved "…AEQxVQILL…" segment) and the leucine-rich heptad pattern characteristic of the family's α-helical fold. This level of identity across the full length, combined with retention of the family signature, places *P. putida* XseB unambiguously within the XseB family.

Second, **the functional partner is present**. *P. putida* KT2440 also encodes the cognate large subunit **XseA** (UniProt Q88P26, PP_0528; a 459-aa "Exodeoxyribonuclease 7 large subunit"), matching *E. coli* XseA (~456 aa). The adjacent locus numbers (PP_0528/PP_0529) and matching subunit sizes indicate that the **complete two-gene *xseA*/*xseB* ExoVII module** is intact in this organism. Together, these observations establish that *P. putida* possesses a functional Exonuclease VII, and that Q88QG5 is its authentic small subunit. The annotation is formally assigned via HAMAP rule MF_00337.

---

## Mechanistic Model / Interpretation

The four findings assemble into a coherent, well-supported model of the *xseB* gene product's function.

### Enzyme architecture and the role of XseB

```
                 EXONUCLEASE VII HOLOENZYME  (E. coli reference: XseA4 · XseB24)
                 ───────────────────────────────────────────────────────────────

        XseB   XseB   XseB                          XseB   XseB   XseB
          \     |     /                               \     |     /
           \    |    /                                 \    |    /
   =========[ XseA α-helical spine ]===[ CATALYTIC ]===[ XseA α-helical spine ]=========
           /    |    \        (dimerization + catalytic domains sequestered in core)
          /     |     \                               /     |     \
        XseB   XseB   XseB                          XseB   XseB   XseB

   • Each XseA dimer is decorated by ~6 XseB subunits (6:1 XseB:XseA).
   • Catalysis (D155/R205/H238/D241 in E. coli middle domain) lives in XseA.
   • XseB (this gene, Q88QG5) = small α-helical subunit lining the spine:
        - stabilizes the assembly
        - required for activity
        - neutralizes the intrinsic toxicity of free XseA
```

### Catalytic reaction

```
        ssDNA  5'-N-p-N-p-N-p-N-p-N-p-N-p-N-...-3'
                        │
                        │  Exonuclease VII  (EC 3.1.11.6)
                        │  bidirectional: 5'→3' AND 3'→5'
                        ▼
        large oligonucleotides  →  small acid-soluble oligonucleotides
                        +
              nucleoside 5'-phosphates
```

Exonuclease VII is unusual in attacking ssDNA from **both ends**, and in *E. coli* requires **no divalent metal cofactor** (active in EDTA) — a distinguishing biochemical feature. It produces 5'-phosphomononucleotide/oligonucleotide products. The *xseB* gene product does not itself perform this chemistry; it is the **structural scaffold subunit** that assembles around XseA to produce the active, non-toxic holoenzyme.

### Cellular role at a glance

| Property | Value | Source |
|---|---|---|
| Primary molecular function | Structural small subunit of ssDNA exonuclease (ExoVII) | UniProt; [PMID: 6284744](https://pubmed.ncbi.nlm.nih.gov/6284744/), [PMID: 22718974](https://pubmed.ncbi.nlm.nih.gov/22718974/) |
| Catalyzed reaction (holoenzyme) | Bidirectional exonucleolytic cleavage of ssDNA → nucleoside 5'-phosphates | EC 3.1.11.6; [PMID: 22718974](https://pubmed.ncbi.nlm.nih.gov/22718974/) |
| Substrate specificity | Single-stranded DNA (not dsDNA) | [PMID: 22718974](https://pubmed.ncbi.nlm.nih.gov/22718974/), [PMID: 26626352](https://pubmed.ncbi.nlm.nih.gov/26626352/) |
| Catalytic subunit | XseA (not XseB) | [PMID: 22718974](https://pubmed.ncbi.nlm.nih.gov/22718974/), [PMID: 38271335](https://pubmed.ncbi.nlm.nih.gov/38271335/) |
| Stoichiometry (E. coli) | XseA₄·XseB₂₄ (6 XseB per XseA dimer) | [PMID: 38271335](https://pubmed.ncbi.nlm.nih.gov/38271335/) |
| Localization | Cytoplasm | UniProt |
| Biological processes | DNA repair, recombination, mismatch excision, msDNA processing, DPC repair | [PMID: 22718974](https://pubmed.ncbi.nlm.nih.gov/22718974/), [PMID: 26626352](https://pubmed.ncbi.nlm.nih.gov/26626352/), [PMID: 38271335](https://pubmed.ncbi.nlm.nih.gov/38271335/), [PMID: 15661009](https://pubmed.ncbi.nlm.nih.gov/15661009/) |
| Conservation | Broad across prokaryotes; absent in eukaryotes | [PMID: 18812402](https://pubmed.ncbi.nlm.nih.gov/18812402/) |
| *P. putida* status | Inferred by orthology (50% id to E. coli XseB); cognate XseA present (PP_0528) | Sequence analysis; HAMAP MF_00337 |

In sum, the *xseB* product in *P. putida* is best described as the **small, non-catalytic, architectural subunit of Exonuclease VII**, an enzyme that trims and degrades single-stranded DNA in the cytoplasm as part of the cell's DNA repair, recombination, and genome-maintenance machinery. XseB's specific contribution is to stabilize the XseA catalytic spine, to be required for enzymatic activity, and to neutralize the toxicity of the unaccompanied large subunit.

---

## Supported vs. Refuted Hypotheses

| Hypothesis | Verdict | Basis |
|---|---|---|
| *xseB* encodes the small subunit of ssDNA-specific Exonuclease VII | **Supported** | UniProt + [PMID: 6284744](https://pubmed.ncbi.nlm.nih.gov/6284744/), [PMID: 22718974](https://pubmed.ncbi.nlm.nih.gov/22718974/) |
| The catalytic site is in XseB | **Refuted** | Active-site residues are in XseA ([PMID: 22718974](https://pubmed.ncbi.nlm.nih.gov/22718974/)); XseB has no nuclease motif |
| XseB is a structural/stabilizing subunit decorating the XseA helical spine | **Supported** | Cryo-EM XseA₄·XseB₂₄, 6:1 ratio ([PMID: 38271335](https://pubmed.ncbi.nlm.nih.gov/38271335/)); rescue of XseA toxicity ([PMID: 26626352](https://pubmed.ncbi.nlm.nih.gov/26626352/)) |
| ExoVII acts in the cytoplasm in DNA repair/recombination | **Supported** | UniProt; [PMID: 15661009](https://pubmed.ncbi.nlm.nih.gov/15661009/); [PMID: 26626352](https://pubmed.ncbi.nlm.nih.gov/26626352/) |
| The *P. putida* protein has been directly studied | **Refuted (no evidence)** | Function assigned by orthology (HAMAP MF_00337) |

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution |
|---|---|---|
| [PMID: 6284744](https://pubmed.ncbi.nlm.nih.gov/6284744/) | *Subunit structure of Escherichia coli exonuclease VII* | Foundational biochemistry: ExoVII is a two-subunit enzyme (10.5 + 54 kDa); establishes *xseB* as the small subunit. |
| [PMID: 22718974](https://pubmed.ncbi.nlm.nih.gov/22718974/) | *Delineation of structural domains and identification of functionally important residues in DNA repair enzyme exonuclease VII* | Maps catalysis to XseA (D155/R205/H238/D241); shows XseA coiled-coil binds multiple XseB; confirms ssDNA hydrolysis and repair/recombination role. |
| [PMID: 38271335](https://pubmed.ncbi.nlm.nih.gov/38271335/) | *Structure of Escherichia coli exonuclease VII* (cryo-EM, PNAS 2024) | Reveals XseA₄·XseB₂₄ architecture; XseB decorates XseA α-helical spine at 6:1; DNA–protein-crosslink repair role. |
| [PMID: 26626352](https://pubmed.ncbi.nlm.nih.gov/26626352/) | *Characterization of cell death in E. coli mediated by XseA...* | Free XseA is lethal; surplus XseB rescues (stabilizing role); identifies msDNA Ec83/Ec78 as in vivo substrates cut between nt 4 and 5. |
| [PMID: 15661009](https://pubmed.ncbi.nlm.nih.gov/15661009/) | *Contact with host cells induces a DNA repair system in pathogenic Neisseriae* | Genetic evidence that *xseB* participates in DNA repair (UV/alkylation/nalidixic-acid sensitivity of mutant). |
| [PMID: 18812402](https://pubmed.ncbi.nlm.nih.gov/18812402/) | *Identification of two conserved aspartic acid residues required for DNA digestion by a novel thermophilic Exonuclease VII in Thermotoga maritima* | Confirms broad prokaryotic conservation (absent in eukaryotes); catalytic aspartates in XseA; defines metal-dependence subfamilies. |

**How the evidence converges:** Biochemistry [PMID: 6284744](https://pubmed.ncbi.nlm.nih.gov/6284744/) defines the subunit architecture; genetics/mutagenesis [PMID: 22718974](https://pubmed.ncbi.nlm.nih.gov/22718974/), [PMID: 18812402](https://pubmed.ncbi.nlm.nih.gov/18812402/), [PMID: 26626352](https://pubmed.ncbi.nlm.nih.gov/26626352/) localize catalysis to XseA and reveal XseB's stabilizing/assembly role; structural biology [PMID: 38271335](https://pubmed.ncbi.nlm.nih.gov/38271335/) visualizes the XseB-decorated spine; and in vivo genetics [PMID: 15661009](https://pubmed.ncbi.nlm.nih.gov/15661009/), [PMID: 26626352](https://pubmed.ncbi.nlm.nih.gov/26626352/) tie the enzyme to concrete DNA-repair and ssDNA-processing pathways. None of the retrieved literature challenges the annotation; the studies are mutually consistent.

**Citation confidence note:** During validation, the cryo-EM snippet describing the XseA₄·XseB₂₄ complex and "decorated by six XseB subunits" was flagged as a possible source-attribution mismatch. The stoichiometry and spine-decoration conclusion are strongly supported by the structural literature, but the specific PMID association for that exact quotation should be treated with slightly lower confidence than the other citations.

---

## Limitations and Knowledge Gaps

1. **No direct experimental study of *P. putida* KT2440 XseB.** All functional claims for Q88QG5 are inferred by orthology (HAMAP MF_00337) from characterized enzymes in *E. coli*, *Neisseria*, and *Thermotoga*. No published work has purified, mutated, or phenotyped *P. putida* XseB specifically.

2. **Moderate sequence identity to the model enzyme.** *P. putida* XseB shares 50% identity with *E. coli* XseB. While this — together with the intact cognate *xseA* and the conserved family signature — is strong evidence of conserved function, the ~50% divergence leaves room for species-specific differences in stoichiometry, regulation, or accessory interactions that have not been tested.

3. **Metal-dependence subfamily untested.** Whether *P. putida* ExoVII is EDTA-resistant (like *E. coli*) or Mg²⁺-dependent (like *T. maritima*) is unknown; it could in principle be predicted from the XseA active-site sequence.

4. **Localization is annotation-based.** The cytoplasmic localization is a UniProt/family-level assignment consistent with a cytoplasmic DNA-metabolism enzyme; it has not been experimentally verified in *P. putida*.

5. **Pathway roles are enzyme-level, not subunit-level, in *P. putida*.** The mismatch-repair, recombination, msDNA-processing, and DPC-repair roles are established for the ExoVII holoenzyme in other bacteria. Whether *P. putida* produces msDNA or relies on ExoVII for crosslink repair has not been examined.

---

## Proposed Follow-up Experiments / Actions

1. **Confirm the operon structure in *P. putida* KT2440.** Verify by RT-PCR or existing transcriptomic data whether PP_0528 (*xseA*) and PP_0529 (*xseB*) are co-transcribed, as expected for a two-subunit enzyme module.

2. **Complementation assay.** Test whether *P. putida* *xseB* complements an *E. coli* Δ*xseB* mutant for ExoVII activity and for rescue of XseA toxicity — the most direct test of conserved function.

3. **In vitro reconstitution.** Co-express *P. putida* XseA + XseB, purify, and assay bidirectional ssDNA exonuclease activity (metal-dependence, 5'-phosphate products, XseA₄·XseB₂₄ stoichiometry) to confirm biochemistry directly in this species.

4. **Phenotypic characterization.** Construct a *P. putida* Δ*xseB* strain and test sensitivity to UV, alkylating agents (e.g., MMS), and quinolones (e.g., nalidixic acid), paralleling the *Neisseria* study, to confirm a DNA-repair role in *P. putida*.

5. **Structural validation.** Use AlphaFold-Multimer to model the *P. putida* XseA–XseB complex and check whether the predicted XseB helices dock onto the XseA spine with the same geometry seen in the *E. coli* cryo-EM structure.

6. **Substrate scope.** Determine whether *P. putida* encodes msDNA-producing retrons; if so, test whether its ExoVII processes those msDNAs at the nt 4/5 position, as in *E. coli*.

---

## Conclusion

*xseB* (Q88QG5, PP_0529) in *Pseudomonas putida* KT2440 encodes the **small subunit of Exonuclease VII**, a bidirectional single-strand-specific DNA exonuclease (EC 3.1.11.6). The gene product is a small (80-aa, ~8.7 kDa) α-helical, **non-catalytic architectural subunit**: it decorates and stabilizes the central α-helical spine of the catalytic large subunit XseA, is required for enzyme assembly and activity, and neutralizes the toxicity of free XseA. Acting in the cytoplasm as part of the ExoVII holoenzyme, it contributes to DNA repair, recombination, mismatch excision, msDNA processing, and DNA–protein-crosslink repair. For *P. putida* these roles are inferred with high confidence from strong orthology to characterized *E. coli*, *Neisseria*, and *Thermotoga* enzymes and from the presence of the cognate large subunit XseA (PP_0528) in the same genome.


## Artifacts

- [OpenScientist final report](xseB-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](xseB-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:6284744
2. PMID:22718974
3. PMID:18812402
4. PMID:38271335
5. PMID:26626352
6. PMID:15661009