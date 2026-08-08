---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-16T10:31:06.448944'
end_time: '2026-07-16T10:50:55.901578'
duration_seconds: 1189.45
template_file: templates/module_research.md.j2
template_variables:
  module_title: Bacterial non-homologous end joining
  module_summary: Species-neutral bacterial module for Ku/LigD-mediated repair of
    DNA double-strand breaks by non-homologous end joining. The module covers the
    compact prokaryotic system in which Ku binds broken double-stranded DNA ends,
    protects and aligns them, and recruits the multifunctional LigD enzyme for end
    processing and ATP-dependent ligation. It excludes homologous recombination, mismatch
    repair, nucleotide excision repair, and eukaryotic multi-protein NHEJ factors.
  module_outline: "- Bacterial non-homologous end joining\n  - 1. double-stranded\
    \ DNA end recognition\n  - Ku DNA-end binding and LigD recruitment\n    - ku:\
    \ prokaryotic Ku DNA-end binding factor (molecular player: prokaryotic Ku family;\
    \ activity or role: double-stranded DNA binding)\n  - 2. DNA end processing and\
    \ ligation\n  - LigD end processing and ATP-dependent ligation\n    - ligD: NHEJ\
    \ DNA ligase/polymerase (molecular player: bacterial LigD family; activity or\
    \ role: DNA ligase (ATP) activity)"
  module_connections: '- Ku DNA-end binding and LigD recruitment feeds into LigD end
    processing and ATP-dependent ligation: Ku-bound DNA ends and Ku-LigD recruitment
    provide the substrate context for LigD-mediated end processing and sealing.'
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 31
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: bacterial_nonhomologous_end_joining-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: bacterial_nonhomologous_end_joining-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Review Brief

## Review Topic

Bacterial non-homologous end joining

## Working Scope

Species-neutral bacterial module for Ku/LigD-mediated repair of DNA double-strand breaks by non-homologous end joining. The module covers the compact prokaryotic system in which Ku binds broken double-stranded DNA ends, protects and aligns them, and recruits the multifunctional LigD enzyme for end processing and ATP-dependent ligation. It excludes homologous recombination, mismatch repair, nucleotide excision repair, and eukaryotic multi-protein NHEJ factors.

## Provisional Biological Outline

- Bacterial non-homologous end joining
  - 1. double-stranded DNA end recognition
  - Ku DNA-end binding and LigD recruitment
    - ku: prokaryotic Ku DNA-end binding factor (molecular player: prokaryotic Ku family; activity or role: double-stranded DNA binding)
  - 2. DNA end processing and ligation
  - LigD end processing and ATP-dependent ligation
    - ligD: NHEJ DNA ligase/polymerase (molecular player: bacterial LigD family; activity or role: DNA ligase (ATP) activity)

## Known Relationships Among Steps

- Ku DNA-end binding and LigD recruitment feeds into LigD end processing and ATP-dependent ligation: Ku-bound DNA ends and Ku-LigD recruitment provide the substrate context for LigD-mediated end processing and sealing.

## Assignment

Write a rigorous, review-style synthesis suitable for a molecular biology
audience. Treat the topic as a biological system whose boundaries, core
mechanisms, variants, and unresolved points should be made clear to readers who
know the field but are not specialists in this specific process.

The review should be explanatory rather than encyclopedic. Anchor broad claims
in primary literature or authoritative reviews, but keep the focus on how the
system works and how its parts fit together.

## Questions To Address

1. **Scope and boundaries**
   - What exactly is included in this biological system?
   - Which neighboring pathways, organelle processes, complexes, or regulatory
     events are often confused with it but should be treated separately?
   - Are there competing definitions in the literature?

2. **Core mechanism**
   - What is the best current model for the sequence of events?
   - Which steps are obligatory, which are conditional, and which are accessory?
   - What molecular assemblies, enzymes, receptors, adaptors, transporters, or
     structural units carry out each major step?

3. **Variation**
   - How does the system vary across major evolutionary lineages?
   - Are there well-supported differences between cell types, tissues,
     developmental stages, physiological states, or compartments?
   - Where are there alternative routes that achieve a similar outcome by
     different molecular means?

4. **Conservation and origin**
   - What is the deepest plausible evolutionary origin of the system?
   - Which parts appear ancient and conserved, and which appear to be later
     elaborations, replacements, or lineage-specific losses?
   - When a protein family has expanded, which family members are the best
     representatives for understanding the ancestral role?

5. **Physical and biological constraints**
   - What steps must occur in a particular order?
   - Which events are mutually exclusive, compartment-specific, cell-type
     specific, substrate-specific, or stage-specific?
   - What evidence rules out otherwise plausible paths through the system?

6. **Evidence and controversy**
   - Which mechanistic claims are strongly supported by experiments?
   - Where does the literature disagree, rely on indirect evidence, or mix data
     from organisms that may not be comparable?
   - What are the most important open questions?

## Output Format

Use the style and structure of a concise review article:

1. Executive summary
2. Definition and biological boundaries
3. Mechanistic overview
4. Major molecular players and active assemblies
5. Evolutionary and cell-biological variation
6. Constraints, dependencies, and failure modes
7. Controversies and open questions
8. Key references

Include citations for major claims, preferably PMIDs or DOIs. Be explicit about
uncertainty and avoid overgeneralizing from one organism, cell type, or assay
system to all biology.

## Output

# Bacterial Non-Homologous End Joining: The Ku/LigD Module

*A review-style synthesis of the compact prokaryotic system for Ku/LigD-mediated repair of DNA double-strand breaks*

---

## 1. Executive Summary

Bacterial non-homologous end joining (NHEJ) is the minimal, self-contained pathway by which many prokaryotes reseal DNA double-strand breaks (DSBs) without a homologous template. In stark contrast to the multi-protein eukaryotic apparatus (Ku70/Ku80, DNA-PKcs, Artemis, XRCC4/Ligase IV, XLF, PAXX, and others), the bacterial system is built from just **two dedicated proteins**: a homodimeric **Ku** DNA-end-binding factor and a multifunctional DNA ligase, **LigD**. Together these two players carry out every activity the reaction requires — end recognition, end protection, end bridging (synapsis), end processing (fill-in, resection, and nucleotide "healing"), and ATP-dependent sealing ([PMID: 17506672](https://pubmed.ncbi.nlm.nih.gov/17506672/); [PMID: 12215643](https://pubmed.ncbi.nlm.nih.gov/12215643/)).

The best-supported mechanistic model is straightforward and sequential: Ku homodimers thread onto and slide along broken duplex ends, protect them from nucleolytic degradation, bridge the two ends into a synaptic complex, and recruit LigD via a species-variable Ku C-terminus. LigD then uses three autonomous catalytic domains — an archaeo-eukaryotic-primase (AEP)-like **polymerase (POL)**, a manganese-dependent **3'-phosphoesterase (PE)**, and an **ATP-dependent ligase (LIG)** — to remodel incompatible ends into a ligatable configuration and seal the backbone ([PMID: 16023671](https://pubmed.ncbi.nlm.nih.gov/16023671/); [PMID: 16446439](https://pubmed.ncbi.nlm.nih.gov/16446439/)). The pathway is template-free and intrinsically **error-prone**, leaving molecular scars — single-nucleotide (frequently ribonucleotide) insertions, templated fill-ins, and short deletions — at the junctions ([PMID: 15778718](https://pubmed.ncbi.nlm.nih.gov/15778718/)).

Three broad conclusions emerge from this investigation. First, bacterial NHEJ is **physiologically specialized for the non-replicating state** — stationary phase, dormancy, and spores — precisely the conditions where a sister chromatid is unavailable and homologous recombination (HR) cannot operate ([PMID: 17360246](https://pubmed.ncbi.nlm.nih.gov/17360246/); [PMID: 17496093](https://pubmed.ncbi.nlm.nih.gov/17496093/)). Second, the module is assembled from **ancient, redeployed protein folds** — a Ku core shared with eukaryotes and a polymerase from the AEP primase clan — and is distributed patchily across bacteria through gene loss and horizontal transfer, even being pirated by mycobacteriophages ([PMID: 11483577](https://pubmed.ncbi.nlm.nih.gov/11483577/); [PMID: 16949369](https://pubmed.ncbi.nlm.nih.gov/16949369/)). Third, the "minimal" two-component system is flanked by **backup and alternative routes** — LigC/LigC1 ligases, the PrimC primase, and a faithful, Ku/LigD-independent joining of cohesive 3'-overhangs — so that end structure and physiological context, not a single fixed enzyme set, dictate outcome ([PMID: 18281464](https://pubmed.ncbi.nlm.nih.gov/18281464/); [PMID: 24957619](https://pubmed.ncbi.nlm.nih.gov/24957619/)).

---

## 2. Definition and Biological Boundaries

### 2.1 What is included

The system reviewed here is the **species-neutral Ku/LigD module** for DSB repair by NHEJ in bacteria. Its defining features are:

- **Ku** — a prokaryotic, homodimeric DNA-end-binding protein that recognizes broken double-stranded DNA ends in a sequence-independent manner, protects and aligns them, and recruits the ligase.
- **LigD** — a dedicated, modular NHEJ enzyme that provides end-processing (polymerase and nuclease/phosphoesterase) and ATP-dependent ligation activities within a single polypeptide.
- The **functional coupling** between them: Ku-bound, synapsed ends provide the substrate context for LigD-mediated processing and sealing ([PMID: 16023671](https://pubmed.ncbi.nlm.nih.gov/16023671/); [PMID: 20018881](https://pubmed.ncbi.nlm.nih.gov/20018881/)).

### 2.2 What is excluded and what is commonly confused

Several neighboring processes are frequently discussed alongside bacterial NHEJ but are mechanistically distinct and lie outside this scope:

| Process | Why it is separate |
|---|---|
| **Homologous recombination (HR)** — RecA/RecBCD/AdnAB | Template-dependent, error-free, requires a homologous donor; dominant in replicating cells. HR and NHEJ are parallel, partly redundant DSB routes; loss of one is compensated by the other ([PMID: 21219454](https://pubmed.ncbi.nlm.nih.gov/21219454/); [PMID: 24658131](https://pubmed.ncbi.nlm.nih.gov/24658131/)). |
| **Single-strand annealing (SSA)** | A third, RecA-independent DSB route in mycobacteria that uses RecBCD; distinct machinery and logic ([PMID: 21219454](https://pubmed.ncbi.nlm.nih.gov/21219454/)). |
| **Mismatch repair, nucleotide excision repair, base excision repair** | Repair single-strand lesions, not DSBs. Note that some NHEJ proteins *moonlight* in BER (Ku AP-lyase activity; LigD/LigC/PrimC in BER), which can blur assays but does not change the DSB-repair definition ([PMID: 25355514](https://pubmed.ncbi.nlm.nih.gov/25355514/); [PMID: 33918798](https://pubmed.ncbi.nlm.nih.gov/33918798/)). |
| **Eukaryotic NHEJ** | Shares a Ku core and functional logic but requires many additional factors (DNA-PKcs, XRCC4-LigIV, XLF, Artemis). The bacterial system is a two-protein reduction, not a scaled-down copy ([PMID: 17506672](https://pubmed.ncbi.nlm.nih.gov/17506672/)). |

### 2.3 Competing definitions

The literature is largely consistent in defining bacterial NHEJ as the Ku + LigD two-component system ([PMID: 17938628](https://pubmed.ncbi.nlm.nih.gov/17938628/)). The main definitional ambiguity concerns **how expansive "the pathway" is**. A strict definition limits it to Ku + LigD. A broader, more accurate definition recognizes that in organisms such as *Mycobacterium smegmatis*, NHEJ is a **network** in which the LigD POL domain can partner with backup ligases (LigC1) or stand-alone POL-domain paralogs (PolD1/PolD2), and in which accessory factors (a Sir2-like deacetylase) modulate efficiency ([PMID: 24957619](https://pubmed.ncbi.nlm.nih.gov/24957619/); [PMID: 23198659](https://pubmed.ncbi.nlm.nih.gov/23198659/); [PMID: 21637345](https://pubmed.ncbi.nlm.nih.gov/21637345/)). This review adopts the two-protein core as the boundary while explicitly cataloguing the accessory and backup layer.

---

## 3. Mechanistic Overview

### 3.1 The canonical sequence of events

The best current model runs as follows:

```
   DSB created (IR, desiccation, ROS/RNS, replication collapse, endonuclease)
                                │
                                ▼
   [1] END RECOGNITION      Ku homodimer threads onto each broken dsDNA end
                            (sequence-independent), protects ends from exonucleases
                                │
                                ▼
   [2] SYNAPSIS             Ku oligomerizes into proteo-filaments; bridges the two
                            ends into a synaptic complex (Ku-driven and, in vitro,
                            LigD-POL-driven end bridging both observed)
                                │
                                ▼
   [3] LigD RECRUITMENT     Ku C-terminus (minimal region) + Ku core recruit LigD
                            via the POL and LIG domains
                                │
                                ▼
   [4] END PROCESSING       LigD PE domain heals 3' ends (Mn-dependent 3'-ribonuclease/
                            3'-phosphatase); LigD POL fills gaps / adds (ribo)nucleotides,
                            can realign mispaired ends → makes ends compatible
                                │
                                ▼
   [5] LIGATION             LigD LIG domain (ATP-dependent) seals the nicked backbone
                                │
                                ▼
   Repaired junction — often carrying insertions/deletions (mutagenic scar)
```

### 3.2 Obligatory, conditional, and accessory steps

- **Obligatory:** DNA-end recognition/protection by Ku and phosphodiester sealing by an ATP-dependent ligase (normally LigD LIG) are required for repair of blunt and 5'-overhang breaks in vivo; deleting *ku* or *ligD* abolishes NHEJ and sensitizes non-replicating cells to ionizing radiation ([PMID: 21219454](https://pubmed.ncbi.nlm.nih.gov/21219454/); [PMID: 12215643](https://pubmed.ncbi.nlm.nih.gov/12215643/)).
- **Conditional:** End processing (POL fill-in, PE healing) is invoked only when ends are not directly ligatable. Blunt and 5'-overhang breaks depend stringently on the POL domain; cohesive 3'-overhangs can bypass Ku/LigD entirely ([PMID: 18281464](https://pubmed.ncbi.nlm.nih.gov/18281464/)).
- **Accessory:** Backup ligases (LigC1), stand-alone POL paralogs (PolD1/PolD2), and modulators (Sir2-like deacetylase) contribute redundancy and regulation but are individually dispensable under standard conditions ([PMID: 24957619](https://pubmed.ncbi.nlm.nih.gov/24957619/); [PMID: 23198659](https://pubmed.ncbi.nlm.nih.gov/23198659/); [PMID: 21637345](https://pubmed.ncbi.nlm.nih.gov/21637345/)).

---

## 4. Major Molecular Players and Active Assemblies

### 4.1 Key Finding 1 — Bacterial NHEJ is a minimal, autonomous two-component system (Ku + LigD)

Bacterial NHEJ collapses the eukaryotic multi-factor apparatus into just two proteins that between them possess all the break-recognition, end-processing, and ligation activities required. This was first predicted bioinformatically by Aravind & Koonin (2001), who noted that prokaryotic Ku homologs form predicted operons with genes for an ATP-dependent DNA ligase and/or an archaeo-eukaryotic-type primase — the signature of a self-contained DSB-repair cassette ([PMID: 11483577](https://pubmed.ncbi.nlm.nih.gov/11483577/)). The authoritative microbial review of Pitcher, Brissett & Doherty (2007) states the point directly: *"the bacterial NHEJ complex is a two-component system that, despite its relative simplicity, possesses all of the break-recognition, end-processing, and ligation activities required to facilitate the complex task of DSB repair"* ([PMID: 17506672](https://pubmed.ncbi.nlm.nih.gov/17506672/)). Genetics confirm the functional minimalism: ablating *ku* or *ligD* abolishes NHEJ and renders non-replicating mycobacteria hypersensitive to ionizing radiation ([PMID: 21219454](https://pubmed.ncbi.nlm.nih.gov/21219454/); [PMID: 24957619](https://pubmed.ncbi.nlm.nih.gov/24957619/)).

### 4.2 Key Finding 2 — LigD is a modular enzyme with three autonomous catalytic domains

LigD is the "Swiss-army knife" of the system. Domain dissection of *M. tuberculosis* LigD demonstrated that its polymerase (primase), nuclease/phosphoesterase, and ligase functions reside in physically separable, individually active domains ([PMID: 16023671](https://pubmed.ncbi.nlm.nih.gov/16023671/)). Weller et al.'s and later structural work established the modular architecture directly: *"LigD consists of an ATP-dependent ligase domain fused to a polymerase domain (Pol) and a phosphoesterase module"* ([PMID: 16446439](https://pubmed.ncbi.nlm.nih.gov/16446439/)). The three modules are:

| Domain | Fold / family | Activity | Notes |
|---|---|---|---|
| **POL** (polymerase) | AEP / archaeal-primase-like | Templated & non-templated (ribo)nucleotide addition; gap fill; end bridging | Two-metal mechanism, Mn-dependent, prefers rNTPs; **the direct catalyst of mutagenic NHEJ in vivo** |
| **PE** (3'-phosphoesterase) | Novel bifunctional phosphoesterase family | Mn-dependent 3'-ribonuclease + 3'-phosphatase ("end healing") | Resects 3'-ribonucleotide tracts; requires penultimate 2'-OH for the ribonuclease step |
| **LIG** (ligase) | ATP-dependent DNA ligase | Nick sealing | Requires active-site lysine for adenylation |

The crystal structure of the *Pseudomonas*/*Mycobacterium* LigD POL domain revealed the archaeal-primase-like fold and two-metal chemistry, and — importantly — showed that *"a mutation of Mycobacterium LigD that uniquely ablates the polymerase activity results in increased fidelity of blunt-end double-strand break repair in vivo by virtue of eliminating nucleotide insertions at the recombination junctions,"* pinning the source of NHEJ mutagenesis on the POL domain ([PMID: 16446439](https://pubmed.ncbi.nlm.nih.gov/16446439/)). The PE domain's Mn-dependent 3'-ribonuclease/3'-phosphatase resection chemistry was mapped in a series of *Pseudomonas* studies ([PMID: 15897197](https://pubmed.ncbi.nlm.nih.gov/15897197/); [PMID: 16540477](https://pubmed.ncbi.nlm.nih.gov/16540477/); [PMID: 16046407](https://pubmed.ncbi.nlm.nih.gov/16046407/)).

### 4.3 Key Finding 3 — Bacterial Ku shares a conserved core with eukaryotic Ku but has a unique, multipurpose C-terminus

Aravind & Koonin dissected Ku into a **eukaryote/prokaryote-conserved core ring** plus lineage-specific extensions — *"the Ku core that is conserved in eukaryotes and prokaryotes"* ([PMID: 11483577](https://pubmed.ncbi.nlm.nih.gov/11483577/)). Bacterial Ku lacks the eukaryotic von Willebrand A (vWA) domain and functions as a **homodimer** (versus the Ku70/Ku80 heterodimer of eukaryotes). The bacterial-specific **C-terminus** is the functional hotspot: dissection in *Bacillus subtilis* showed that *"the minimal C-terminus is required for the Ku-LigD interaction, whereas the basic extension controls the threading and DNA bridging abilities of Ku"* ([PMID: 26961308](https://pubmed.ncbi.nlm.nih.gov/26961308/)). In *M. tuberculosis*, the Ku C-terminus is a "multipurpose arm" that binds DNA and LigD and stimulates ligation, with the extended C-terminus limiting DNA binding and the Ku core also contributing to ligase stimulation and direct LigD binding ([PMID: 36250639](https://pubmed.ncbi.nlm.nih.gov/36250639/)). Recent cryo-EM work resolved apo and DNA-bound mycobacterial Ku homodimers and showed that **Ku forms extended proteo-filaments upon binding DNA**, driving DNA synapsis; the C-terminus regulates DNA loading and subsequent LigD recruitment ([PMID: 41298423](https://pubmed.ncbi.nlm.nih.gov/41298423/); [PMID: 41521670](https://pubmed.ncbi.nlm.nih.gov/41521670/)).

### 4.4 Key Finding 7 — The Ku-recruits-ligase core mechanism is strongly supported experimentally

The founding experimental demonstration is Weller et al. (2002, *Science*), which established that bacterial Ku homologs retain the end-binding biochemistry of eukaryotic Ku, that *"bacterial Ku specifically recruits DNA ligase to DNA ends and stimulates DNA ligation. Loss of these proteins leads to hypersensitivity to ionizing radiation in Bacillus subtilis"* ([PMID: 12215643](https://pubmed.ncbi.nlm.nih.gov/12215643/)). This Ku-recruits-and-stimulates-ligase mechanism has since been reproduced across *Mycobacterium*, *Pseudomonas*, and *Bacillus* by genetics, in-vitro reconstitution, and structural biology ([PMID: 15778718](https://pubmed.ncbi.nlm.nih.gov/15778718/); [PMID: 20018881](https://pubmed.ncbi.nlm.nih.gov/20018881/); [PMID: 23691176](https://pubmed.ncbi.nlm.nih.gov/23691176/); [PMID: 36250639](https://pubmed.ncbi.nlm.nih.gov/36250639/)), and is synthesized in the definitive Shuman & Glickman review, which confirms that *"mycobacteria and other genera have an NHEJ system that depends on a dedicated DNA ligase, LigD, and the DNA-end-binding protein Ku"* ([PMID: 17938628](https://pubmed.ncbi.nlm.nih.gov/17938628/)).

---

## 5. Evolutionary and Cell-Biological Variation

### 5.1 Key Finding 4 — Dedicated to non-replicating/dormant states, and intrinsically mutagenic

Bacterial NHEJ is not a general-purpose DSB pathway; it is the **repair option of last resort in cells that cannot use HR**. In *M. smegmatis*, deletion of *ku*/*ligD* sensitizes cells to ionizing radiation and desiccation **specifically in stationary phase, not in log phase** — because in replicating cells a sister chromatid supports error-free HR: *"NHEJ-mutant strains (Deltaku, DeltaligD, Deltaku/ligD) were significantly more sensitive to ionizing radiation (IR) during stationary phase than wild-type M. smegmatis. However, there was little difference in IR sensitivity between NHEJ-mutant and wild-type strains in logarithmic phase"* ([PMID: 17360246](https://pubmed.ncbi.nlm.nih.gov/17360246/); [PMID: 17496093](https://pubmed.ncbi.nlm.nih.gov/17496093/)). NHEJ is the **sole** DSB pathway operating during *M. tuberculosis* dormancy ([PMID: 41521670](https://pubmed.ncbi.nlm.nih.gov/41521670/)).

The price of template-free joining is **fidelity**. Repair of blunt and 5'-overhang DSBs is roughly 50% mutagenic, with molecular signatures of templated fill-in, non-templated single-nucleotide additions (often ribonucleotides), and nucleolytic resection: *"NHEJ of blunt-end and complementary 5'-overhang DSBs is highly mutagenic"* ([PMID: 15778718](https://pubmed.ncbi.nlm.nih.gov/15778718/)). At chromosomal I-SceI breaks, NHEJ produces predominantly single-nucleotide insertions and rapidly mutates the break site in the absence of HR ([PMID: 17496093](https://pubmed.ncbi.nlm.nih.gov/17496093/)).

### 5.2 Key Finding 5 — End structure dictates pathway choice; backup ligases and a faithful alternative route exist

The system is best understood as **end-structure-tuned**. Aniukwu et al. (2008) showed that repair of blunt and 5'-overhang breaks depends stringently on Ku and the LigD POL domain, whereas 3'-overhang breaks are handled by *"a novel end-joining pathway specific to breaks with 3' overhangs that is Ku- and LigD-independent and perfectly faithful"* — most plausibly relying on the essential NAD⁺-dependent replicative ligase LigA ([PMID: 18281464](https://pubmed.ncbi.nlm.nih.gov/18281464/)). Redundancy extends to ligases: LigC1 supports a **LigD-ligase-independent backup route that still requires the LigD POL domain** — *"we define a LigD ligase-independent NHEJ pathway in Mycobacterium smegmatis that requires the ATP-dependent DNA ligase LigC1 and the POL domain of LigD"* ([PMID: 24957619](https://pubmed.ncbi.nlm.nih.gov/24957619/)); LigC also provides backup for blunt-end repair ([PMID: 15778718](https://pubmed.ncbi.nlm.nih.gov/15778718/)); and LigC plus the AEP-primase PrimC contribute additional backup activities under oxidative stress ([PMID: 33918798](https://pubmed.ncbi.nlm.nih.gov/33918798/)).

**Pathway-choice summary:**

| End structure | Primary route | Ku required? | LigD required? | Fidelity |
|---|---|---|---|---|
| Blunt | Ku + LigD (POL-dependent) | Yes | Yes (POL critical) | Mutagenic |
| 5'-overhang | Ku + LigD (POL fill-in) | Yes | Yes | Mutagenic |
| Cohesive 3'-overhang | LigA-dependent, Ku/LigD-independent | No | No | Faithful |
| Blunt (backup) | LigC / LigC1 + LigD POL | Yes | POL only | Variable |

### 5.3 Key Finding 6 — Ancient, redeployed folds; patchy distribution via loss and horizontal transfer

The Ku/LigD module is a mosaic of old parts. The **prokaryotic Ku core is homologous to the eukaryotic Ku core**, placing the fold before the eukaryote/prokaryote divergence; eukaryotic Ku later acquired a vWA domain and heterodimerized ([PMID: 11483577](https://pubmed.ncbi.nlm.nih.gov/11483577/)). The **LigD polymerase belongs to the archaeo-eukaryotic primase (AEP) superfamily**, adopting *"a fold similar to that of archaeal DNA primase"* ([PMID: 16446439](https://pubmed.ncbi.nlm.nih.gov/16446439/); [PMID: 17174332](https://pubmed.ncbi.nlm.nih.gov/17174332/)). The two genes frequently sit together in predicted operons — *"genes for prokaryotic Ku homologs form predicted operons with genes coding for an ATP-dependent DNA ligase and/or archeal-eukaryotic-type DNA primase"* ([PMID: 11483577](https://pubmed.ncbi.nlm.nih.gov/11483577/)). The module is **absent from many bacteria** (e.g., *E. coli*), giving a patchy phyletic distribution consistent with gene loss and horizontal transfer ([PMID: 17506672](https://pubmed.ncbi.nlm.nih.gov/17506672/)). Strikingly, mycobacteriophages Corndog and Omega carry their **own Ku** and hijack the host LigD to circularize their genomes via short 4-base cos ends, demonstrating the module's mobility and modularity ([PMID: 16949369](https://pubmed.ncbi.nlm.nih.gov/16949369/)).

Because the LigD polymerase is the representative bacterial member of the AEP clan and Ku's core is the representative shared fold, these two domains — rather than the lineage-specific C-terminal extensions or accessory paralogs — are the best proxies for understanding the ancestral NHEJ role.

---

## 6. Constraints, Dependencies, and Failure Modes

**Ordering constraints.** The reaction is strongly ordered: Ku must load and protect ends *before* recruiting LigD (Ku is upstream and rate-limiting), and end **processing precedes ligation** — the PE domain heals 3' termini and the POL domain fills/realigns before the LIG domain can seal ([PMID: 16023671](https://pubmed.ncbi.nlm.nih.gov/16023671/); [PMID: 17947582](https://pubmed.ncbi.nlm.nih.gov/17947582/)). In *M. tuberculosis*, Ku is the rate-limiting factor for the whole pathway ([PMID: 41521670](https://pubmed.ncbi.nlm.nih.gov/41521670/)).

**Physiological / compartment constraints.** NHEJ is functionally confined to the **non-replicating state**. In log phase, HR outcompetes and largely replaces it; the two pathways are partly redundant so that inactivating NHEJ is compensated by elevated HR, and vice versa ([PMID: 21219454](https://pubmed.ncbi.nlm.nih.gov/21219454/); [PMID: 24658131](https://pubmed.ncbi.nlm.nih.gov/24658131/)). This physiological gating is why NHEJ mutants show phenotypes only in stationary phase, spores, and dormancy ([PMID: 17360246](https://pubmed.ncbi.nlm.nih.gov/17360246/); [PMID: 31948638](https://pubmed.ncbi.nlm.nih.gov/31948638/)).

**Substrate constraints.** End chemistry governs which route is used and whether processing is needed. Faithful, direct joining is possible for compatible cohesive ends; blunt/5'-overhang ends require mutagenic POL activity; the PE 3'-ribonuclease step even requires a specific 2'-OH configuration on the penultimate ribose ([PMID: 18281464](https://pubmed.ncbi.nlm.nih.gov/18281464/); [PMID: 16540477](https://pubmed.ncbi.nlm.nih.gov/16540477/)).

**Evidence ruling out otherwise-plausible paths.** The Ku/LigD-independent, perfectly faithful 3'-overhang route ([PMID: 18281464](https://pubmed.ncbi.nlm.nih.gov/18281464/)) rules out the assumption that *all* bacterial end joining flows through Ku/LigD. The POL-ablation experiment ([PMID: 16446439](https://pubmed.ncbi.nlm.nih.gov/16446439/)) rules out the LIG or PE domains as the principal source of insertional mutagenesis. Stand-alone POL paralogs PolD1/PolD2, although biochemically LigD-POL-like, were shown *not* to substitute for LigD POL in fill-in during NHEJ under the conditions tested, ruling them out as the primary NHEJ polymerases ([PMID: 23198659](https://pubmed.ncbi.nlm.nih.gov/23198659/)).

**Failure modes.** Loss of Ku or LigD → radiation/desiccation hypersensitivity of dormant cells; loss of both HR and NHEJ (Δ*ku* Δ*ligD* Δ*recA*) cripples intracellular survival of *M. tuberculosis*, an effect rescuable by neutralizing host ROS/RNS ([PMID: 24658131](https://pubmed.ncbi.nlm.nih.gov/24658131/)). Because NHEJ is mutagenic, its "success" can itself be a failure mode at the sequence level, fixing insertions/deletions at the repaired locus ([PMID: 17496093](https://pubmed.ncbi.nlm.nih.gov/17496093/)).

---

## 7. Controversies and Open Questions

1. **What drives synapsis in vivo — Ku filaments or the LigD polymerase?** Recent cryo-EM shows Ku itself oligomerizes into proteo-filaments that bridge ends ([PMID: 41298423](https://pubmed.ncbi.nlm.nih.gov/41298423/); [PMID: 41521670](https://pubmed.ncbi.nlm.nih.gov/41521670/)), whereas an earlier crystal structure captured the **LigD POL domain mediating end synapsis** as a proposed bridging intermediate ([PMID: 17947582](https://pubmed.ncbi.nlm.nih.gov/17947582/)). Whether these are sequential stages, redundant mechanisms, or context-dependent alternatives is unresolved.

2. **What is the source of repair-associated deletions?** The POL domain explains insertions, and the PE/nuclease activity can generate deletions in reconstituted *E. coli* systems ([PMID: 20530153](https://pubmed.ncbi.nlm.nih.gov/20530153/)), but the in-vivo origin of terminal deletions at junctions is not fully assigned.

3. **How general is the mycobacterial/Pseudomonas paradigm?** Nearly all mechanistic detail comes from *Mycobacterium*, *Pseudomonas*, and *Bacillus*. Given the module's patchy distribution and species-variable Ku C-termini and LigD domain arrangements (some organisms split LigD activities across separate proteins), extrapolating a single model across all NHEJ-competent bacteria risks overgeneralization ([PMID: 17506672](https://pubmed.ncbi.nlm.nih.gov/17506672/)).

4. **Are second Ku–LigD contact sites functionally important?** Beyond the primary POL–Ku interaction, evidence for a second Ku-dependent LIG-domain interaction has been reported ([PMID: 20530153](https://pubmed.ncbi.nlm.nih.gov/20530153/); [PMID: 36250639](https://pubmed.ncbi.nlm.nih.gov/36250639/)); their relative in-vivo weight is unclear.

5. **Role of accessory modulators.** A Sir2-like NAD⁺-dependent deacetylase interacts with Ku and LigD and modestly promotes NHEJ ([PMID: 21637345](https://pubmed.ncbi.nlm.nih.gov/21637345/)); the regulatory logic (e.g., acetylation control of end binding) is not established.

**Well-supported vs. indirect.** Strongly supported: the two-component composition, LigD's three-domain modular chemistry, Ku's end-binding/recruitment role, POL as the mutagenesis catalyst, and the stationary-phase specialization — all backed by convergent genetics, biochemistry, and structures. More indirect / model-dependent: the exact in-vivo synaptic architecture, the LigA identity of the faithful 3'-overhang route (inferred), and the physiological importance of backup ligases outside stress conditions.

---

## 8. Limitations and Knowledge Gaps

- **Organism bias.** The evidence base is dominated by a handful of Actinobacteria and *Bacillus*/*Pseudomonas*; broad phyla with Ku/LigD homologs remain experimentally unexplored.
- **In-vitro vs. in-vivo gap.** Much end-processing chemistry (PE ribonuclease specificity, POL ribonucleotide preference) is characterized on defined primer-templates that may not reflect chromosomal DSB contexts.
- **Reconstitution artifacts.** Heterologous reconstitution in *E. coli* (which lacks native NHEJ) is powerful but can over- or under-represent activities (e.g., nuclease-driven deletions) relative to the native host.
- **Structural snapshots.** The new cryo-EM Ku-filament and older POL-synapsis structures are static; the temporal choreography of loading → synapsis → processing → ligation is inferred, not directly observed as a trajectory.

---

## 9. Proposed Follow-up Experiments / Actions

1. **Time-resolved / single-molecule synapsis assays** (e.g., smFRET or live-cell imaging as in [PMID: 41521670](https://pubmed.ncbi.nlm.nih.gov/41521670/)) comparing Ku-only, LigD-only, and Ku+LigD conditions to determine whether Ku filaments and LigD-POL bridging are sequential or alternative synaptic mechanisms.
2. **Cross-phylum functional survey.** Reconstitute Ku/LigD pairs from underexplored phyla in a common heterologous host to test how far the mycobacterial paradigm generalizes and to catalogue split-LigD architectures.
3. **Deletion-source mapping.** Use domain-specific catalytic mutants (PE-dead, POL-dead, nuclease-dead) at a defined chromosomal I-SceI break to assign the enzymatic origin of junction deletions in vivo.
4. **Genetic test of the faithful 3'-overhang route.** Directly test LigA (and other candidate ligases) dependence for Ku/LigD-independent cohesive-end joining to confirm the inferred LigA route ([PMID: 18281464](https://pubmed.ncbi.nlm.nih.gov/18281464/)).
5. **Regulatory dissection of accessory factors.** Define whether the Sir2-like deacetylase regulates Ku/LigD by acetylation, and whether backup ligases (LigC/LigC1) and PrimC are induced under specific stresses ([PMID: 21637345](https://pubmed.ncbi.nlm.nih.gov/21637345/); [PMID: 33918798](https://pubmed.ncbi.nlm.nih.gov/33918798/)).
6. **Therapeutic targeting.** Given NHEJ's essentiality in *M. tuberculosis* dormancy, pursue Ku-synapsis or LigD-domain inhibitors as adjuncts that block persistence-phase DSB repair ([PMID: 41298423](https://pubmed.ncbi.nlm.nih.gov/41298423/)).

---

## 10. Key References

| PMID | Contribution |
|---|---|
| [12215643](https://pubmed.ncbi.nlm.nih.gov/12215643/) | Weller et al. 2002, *Science* — founding identification of the bacterial NHEJ complex; Ku recruits and stimulates ligase; IR sensitivity in *B. subtilis*. |
| [11483577](https://pubmed.ncbi.nlm.nih.gov/11483577/) | Aravind & Koonin 2001 — bioinformatic prediction of the prokaryotic DSB-repair system; conserved Ku core; Ku–ligase/AEP-primase operons. |
| [17506672](https://pubmed.ncbi.nlm.nih.gov/17506672/) | Pitcher, Brissett & Doherty 2007 — microbial-perspective review defining the two-component system. |
| [17938628](https://pubmed.ncbi.nlm.nih.gov/17938628/) | Shuman & Glickman 2007 — authoritative review of bacterial NHEJ (Ku + LigD). |
| [16023671](https://pubmed.ncbi.nlm.nih.gov/16023671/) | Pitcher et al. 2005 — LigD domain dissection (POL, PE, LIG). |
| [16446439](https://pubmed.ncbi.nlm.nih.gov/16446439/) | Zhu et al. 2006 — POL crystal structure; AEP-primase fold; POL as in-vivo mutagenesis catalyst. |
| [17174332](https://pubmed.ncbi.nlm.nih.gov/17174332/) | Brissett et al. 2007 — Mt-LigD PolDom structure; AEP superfamily; 5'-phosphate recognition. |
| [15897197](https://pubmed.ncbi.nlm.nih.gov/15897197/), [16540477](https://pubmed.ncbi.nlm.nih.gov/16540477/), [16046407](https://pubmed.ncbi.nlm.nih.gov/16046407/) | Zhu & Shuman — PE domain 3'-ribonuclease/3'-phosphatase chemistry. |
| [26961308](https://pubmed.ncbi.nlm.nih.gov/26961308/) | McGovern et al. 2016 — *B. subtilis* Ku C-terminus: LigD recruitment vs bridging/threading. |
| [36250639](https://pubmed.ncbi.nlm.nih.gov/36250639/) | Sowa et al. 2022 — Mt-Ku C-terminus as multipurpose arm. |
| [41298423](https://pubmed.ncbi.nlm.nih.gov/41298423/), [41521670](https://pubmed.ncbi.nlm.nih.gov/41521670/) | Cryo-EM of mycobacterial Ku; proteo-filament synapsis model. |
| [15778718](https://pubmed.ncbi.nlm.nih.gov/15778718/) | Gong et al. 2005 — low-fidelity NHEJ; LigC backup. |
| [17360246](https://pubmed.ncbi.nlm.nih.gov/17360246/), [17496093](https://pubmed.ncbi.nlm.nih.gov/17496093/) | Stationary-phase specificity; mutagenic chromosomal repair. |
| [18281464](https://pubmed.ncbi.nlm.nih.gov/18281464/) | Aniukwu et al. 2008 — end-structure-dependent pathway choice; faithful Ku/LigD-independent 3'-overhang route. |
| [24957619](https://pubmed.ncbi.nlm.nih.gov/24957619/) | Bhattarai et al. 2014 — LigC1 backup NHEJ requiring LigD POL. |
| [21219454](https://pubmed.ncbi.nlm.nih.gov/21219454/) | Gupta et al. 2011 — three genetically distinct DSB pathways (HR, NHEJ, SSA). |
| [16949369](https://pubmed.ncbi.nlm.nih.gov/16949369/) | Mycobacteriophage-encoded Ku; module mobility. |
| [17947582](https://pubmed.ncbi.nlm.nih.gov/17947582/) | POL-mediated DNA synaptic complex structure. |
| [20018881](https://pubmed.ncbi.nlm.nih.gov/20018881/) | *Pseudomonas* LigD gap-filling; Ku stimulation and end protection. |
| [23691176](https://pubmed.ncbi.nlm.nih.gov/23691176/) | *B. subtilis* minimal NHEJ reconstituted in vitro. |
| [20530153](https://pubmed.ncbi.nlm.nih.gov/20530153/) | Mt-Ku/Mt-LigD reconstitution in *E. coli*; nuclease-driven deletions; second Ku–LIG contact. |
| [23198659](https://pubmed.ncbi.nlm.nih.gov/23198659/) | PolD1/PolD2 stand-alone POL paralogs. |
| [21637345](https://pubmed.ncbi.nlm.nih.gov/21637345/) | Sir2-like deacetylase in mycobacterial NHEJ. |
| [33918798](https://pubmed.ncbi.nlm.nih.gov/33918798/) | LigC/PrimC backup under oxidative stress. |
| [24658131](https://pubmed.ncbi.nlm.nih.gov/24658131/) | HR or NHEJ sufficient for intracellular *M. tuberculosis* survival. |
| [25355514](https://pubmed.ncbi.nlm.nih.gov/25355514/) | Ku AP-lyase (BER moonlighting) activity. |
| [31948638](https://pubmed.ncbi.nlm.nih.gov/31948638/) | Ku/LigD in *B. subtilis* spore resistance to electron-beam treatment. |

---

*Prepared as a commissioned review synthesis of the Ku/LigD bacterial NHEJ module. Mechanistic detail is drawn predominantly from* Mycobacterium, Pseudomonas, *and* Bacillus; *claims should not be assumed to generalize uniformly to all NHEJ-competent bacteria.*


## Artifacts

- [OpenScientist final report](bacterial_nonhomologous_end_joining-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](bacterial_nonhomologous_end_joining-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:17506672
2. PMID:12215643
3. PMID:16023671
4. PMID:16446439
5. PMID:15778718
6. PMID:17360246
7. PMID:17496093
8. PMID:11483577
9. PMID:16949369
10. PMID:18281464
11. PMID:24957619
12. PMID:20018881
13. PMID:21219454
14. PMID:24658131
15. PMID:25355514
16. PMID:33918798
17. PMID:17938628
18. PMID:23198659
19. PMID:21637345
20. PMID:15897197
21. PMID:16540477
22. PMID:16046407
23. PMID:26961308
24. PMID:36250639
25. PMID:41298423
26. PMID:41521670
27. PMID:23691176
28. PMID:17174332
29. PMID:17947582
30. PMID:31948638
31. PMID:20530153