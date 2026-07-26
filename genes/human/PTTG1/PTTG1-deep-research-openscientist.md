---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-19T08:21:13.417562'
end_time: '2026-07-19T08:45:37.794212'
duration_seconds: 1464.38
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: PTTG1
  gene_symbol: PTTG1
  uniprot_accession: O95997
  protein_description: 'RecName: Full=Securin; AltName: Full=Esp1-associated protein;
    AltName: Full=Pituitary tumor-transforming gene 1 protein; Short=Tumor-transforming
    protein 1; Short=hPTTG;'
  gene_info: Name=PTTG1; Synonyms=EAP1, PTTG, TUTR1;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the securin family. .
  protein_domains: Securin_separation_inhibitor. (IPR006940); Securin (PF04856)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 20
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PTTG1-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PTTG1-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** O95997
- **Protein Description:** RecName: Full=Securin; AltName: Full=Esp1-associated protein; AltName: Full=Pituitary tumor-transforming gene 1 protein; Short=Tumor-transforming protein 1; Short=hPTTG;
- **Gene Information:** Name=PTTG1; Synonyms=EAP1, PTTG, TUTR1;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the securin family. .
- **Key Domains:** Securin_separation_inhibitor. (IPR006940); Securin (PF04856)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PTTG1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PTTG1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PTTG1** (gene ID: PTTG1, UniProt: O95997) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# PTTG1 / Securin (UniProt O95997): Functional Annotation Report

**Gene:** PTTG1 (synonyms: EAP1, PTTG, TUTR1)
**Protein:** Securin / Esp1-associated protein / Pituitary tumor-transforming gene 1 protein (hPTTG)
**Organism:** *Homo sapiens* (Human)
**UniProt:** O95997
**Family:** Securin family — domains Securin_separation_inhibitor (IPR006940); Securin (PF04856)

---

## Identity Verification

The target was verified before and throughout research. The gene symbol **PTTG1** unambiguously corresponds to the protein described in UniProt O95997: human **Securin**, the vertebrate ortholog of the yeast securins **Pds1** (*S. cerevisiae*) and **Cut2** (*S. pombe*). The literature reviewed consistently describes a human protein of ~22 kDa that (i) binds and inhibits the cysteine protease **separase (ESPL1)**, (ii) regulates sister-chromatid separation during mitosis, and (iii) was originally isolated as an oncogene overexpressed in pituitary tumors ("**p**ituitary **t**umor-**t**ransforming **g**ene"). This matches the securin family/domain assignment exactly ([PMID: 12444553](https://pubmed.ncbi.nlm.nih.gov/12444553/)). No conflicting-gene ambiguity was encountered; all cited literature refers to the same human PTTG1/Securin protein. Research proceeded with high confidence in the identity.

---

## Summary

**PTTG1 encodes human Securin, a small (~22 kDa), largely intrinsically disordered regulatory protein whose primary, defining molecular function is to bind and control the giant cysteine endopeptidase separase (ESPL1).** Securin is not itself an enzyme, transporter, or structural protein; it is a **direct enzyme regulator and molecular chaperone** for separase. It performs a striking dual role: it acts as a **pseudosubstrate inhibitor** that occludes separase's catalytic site, and simultaneously as a **chaperone/positive activator** required for the proper folding and full activity of nascent separase. By keeping separase inhibited and helping target it to chromosomes, securin prevents the premature proteolytic cleavage of the cohesin kleisin subunit **RAD21/Scc1** (and **REC8** in meiosis), thereby holding sister chromatids together until the correct moment in the cell cycle.

Securin sits at the terminal, decisive node of the mitotic anaphase-triggering pathway: **Spindle Assembly Checkpoint (SAC) → APC/C^Cdc20^ → securin ubiquitination/destruction → separase activation → RAD21 cleavage → sister-chromatid separation**. While the checkpoint detects unattached kinetochores, securin is stabilized and separase stays silenced; once all kinetochores are correctly attached, the APC/C^Cdc20^ ubiquitin ligase destroys securin, unleashing separase precisely at anaphase onset. A parallel stress pathway, the **SCF–βTrCP** E3 ligase, degrades securin after DNA damage to enforce cell-cycle arrest. Because both loss and overexpression of securin produce chromosomal instability and aneuploidy, PTTG1 is a **dosage-sensitive guardian of genome stability**.

Securin carries out its core function chiefly **in the nucleus and on mitotic chromosomes**, though the protein is also partially cytosolic and its localization is cell-type dependent. Beyond the separase axis, securin has well-documented nuclear **"moonlighting" functions**: it possesses an intrinsic acidic **transactivation domain**, it **binds and inhibits the p53 tumor suppressor**, and it drives **FGF-2/VEGF-mediated angiogenesis**. These activities explain its proto-oncogenic behavior when overexpressed across many human tumors.

---

## Key Findings

### 1. Securin is the vertebrate separase inhibitor that blocks premature sister-chromatid separation

The core, primary function of PTTG1/Securin is to bind and inhibit **separase**, a cysteine protease that dissolves sister-chromatid cohesion. PTTG1 is the human ortholog of the yeast securins Pds1 and Cut2, confirmed as "the vertebrate analog of yeast securins Pds1 and Cut2 with a key role in the regulation of sister chromatid separation during mitosis" ([PMID: 12444553](https://pubmed.ncbi.nlm.nih.gov/12444553/)). Functionally, PTTG1 "encodes Securin, a protein involved in the inhibition of sister chromatid separation binding to Separase until the onset of anaphase. Separase is a cysteine-protease that degrades cohesin to segregate the sister chromatids" ([PMID: 22819078](https://pubmed.ncbi.nlm.nih.gov/22819078/)).

The mechanism of inhibition is now defined at near-atomic resolution. The cryo-EM structure of a metazoan (*C. elegans*) separase–securin complex shows that "**securin engages separase in an extended antiparallel conformation, interacting with both lobes. It inhibits separase by interacting with the catalytic site through a pseudosubstrate mechanism**" ([PMID: 28263324](https://pubmed.ncbi.nlm.nih.gov/28263324/)). In this pseudosubstrate mode, securin threads through the enzyme and places an aliphatic side chain at the P1 position of the catalytic cleft — mimicking a substrate but resisting cleavage — thereby repressing catalysis. When securin is removed, separase becomes free to cleave the kleisin (Scc1/Rad21, or Rec8 in meiosis) subunit of the cohesin ring, triggering chromatid segregation. This is the structural basis of securin's role as the guardian that prevents premature anaphase.

### 2. Securin has a dual role: it both inhibits AND positively promotes (chaperones) separase

Securin is not a simple inhibitor. It also acts as a **molecular chaperone** essential for separase to fold and function. Securin "associates with nascent separase to co-translationally assist proper folding" ([PMID: 25659430](https://pubmed.ncbi.nlm.nih.gov/25659430/)), meaning that fully active separase paradoxically requires securin for its biogenesis even though securin also inhibits it.

The inhibitory and activating activities are structurally separable. Comparison of PTTG1 with its paralog PTTG2 (which cannot bind separase) pinpointed a single residue: "**Mutation of the homologous position in PTTG1 (H134) switched PTTG1 from an inhibitor into an activator of separase**" ([PMID: 23798554](https://pubmed.ncbi.nlm.nih.gov/23798554/)), and this switch triggers premature sister-chromatid separation. Thus securin contains a high-affinity, H134-containing inhibitory domain and a distinct, weaker-affinity activating domain.

This dual/redundant regulation also explains a puzzling genetic observation: "**securin knock-out mice are surprisingly viable and fertile**" ([PMID: 25659430](https://pubmed.ncbi.nlm.nih.gov/25659430/)). The redundancy arises because **Cdk1–cyclin B1** can independently bind and inhibit native separase, providing a backup brake in the absence of securin.

### 3. Securin levels are set by cell-cycle and stress-responsive ubiquitin ligases (APC/C and SCF–βTrCP)

Securin's abundance — and therefore separase activity — is controlled by regulated proteolysis. At the metaphase-to-anaphase transition, "**securin is targeted for proteasomal destruction by the anaphase-promoting complex or cyclosome (APC/C), allowing activation of separase**" ([PMID: 18460583](https://pubmed.ncbi.nlm.nih.gov/18460583/)). This is the canonical cell-cycle trigger for anaphase.

A second, stress-responsive pathway degrades securin after DNA damage. After UV irradiation, the **SKP1–CUL1–βTrCP (SCF–βTrCP)** E3 ligase destroys securin via "a conserved and unconventional **βTrCP recognition motif (DDAYPE)** in the securin primary amino acid sequence" ([PMID: 18460583](https://pubmed.ncbi.nlm.nih.gov/18460583/)). GSK-3β activity is required, and βTrCP knockdown accumulates securin even without stress, implying SCF–βTrCP also sets basal securin turnover. This degradation contributes to cell-cycle arrest after DNA damage.

The dosage matters physiologically. In aging mouse oocytes, "**oocytes from aged mice have less securin than oocytes from young mice and that this reduction is mediated by increased destruction by the anaphase promoting complex/cyclosome (APC/C) during meiosis I**" ([PMID: 28516917](https://pubmed.ncbi.nlm.nih.gov/28516917/)). Reduced securin leads to premature sister-chromatid separation in meiosis II and aneuploidy — a mechanistic link between securin dosage and the maternal-age effect on egg quality.

### 4. Subcellular localization is both cytoplasmic and nuclear, and is cell-type dependent

Securin carries out its chromosome-segregation function in the nucleus/on chromosomes, but the protein is distributed between compartments. Subcellular fractionation showed that "although hPTTG is mainly a cytosolic protein, it is partially localized in the nucleus" ([PMID: 9811450](https://pubmed.ncbi.nlm.nih.gov/9811450/)). Localization varies by cell type: securin is "predominantly in the nucleus in HeLa, Cos-7 and DU145 cells, but showed a diffuse distribution in both the nucleus and cytoplasm in A549, DLD-1 and NIH3T3 cells" ([PMID: 14709851](https://pubmed.ncbi.nlm.nih.gov/14709851/)).

Compartmentalization is itself part of the safety mechanism. Its partner separase is actively kept away from nuclear cohesin during interphase: "**separase is excluded from cohesin by the nuclear envelope, which forms in telophase and disassembles in mitosis**" ([PMID: 17102637](https://pubmed.ncbi.nlm.nih.gov/17102637/)), reinforced by a CRM1-dependent nuclear export signal. This spatial control prevents premature cohesin cleavage independently of securin's biochemical inhibition.

### 5. Securin spatially targets separase to chromosomes; downstream separase cleaves centromeric RAD21/Scc1

Securin does more than inhibit — it **localizes** separase to its site of action. Using a fluorescent separase activity sensor, researchers found that "separase undergoes abrupt activation shortly before anaphase onset in the vicinity of chromosomes," and that "**This activation profile of separase depends on the abilities of two of its binding proteins, securin and cyclin B1, to inhibit its protease activity and target it to chromosomes**" ([PMID: 22814604](https://pubmed.ncbi.nlm.nih.gov/22814604/)). Securin therefore couples timing (inhibition until anaphase) with space (delivery to chromosomes).

Downstream, cohesion is dissolved in two steps. A **prophase pathway** (PLK1 phosphorylation of the cohesin subunit SA2, plus Wapl) removes cohesin from chromosome arms, while at anaphase onset "the protease separase removes centromere-enriched cohesin by **proteolytic cleavage of another cohesin subunit, Scc1 (Rad21, Mcd1)**, which allows the separation of sister chromatids" ([PMID: 18003702](https://pubmed.ncbi.nlm.nih.gov/18003702/)). This substrate identity is confirmed independently: cohesion "is dissolved in anaphase when separase, a giant cysteine endopeptidase, **cleaves the Scc1/Rad21 subunit of cohesin**, thereby triggering chromosome segregation" ([PMID: 25659430](https://pubmed.ncbi.nlm.nih.gov/25659430/)). Non-cleavable Scc1 blocks separation, establishing that separase-dependent RAD21 cleavage is required for anaphase — the ultimate outcome gated by securin.

### 6. The spindle assembly checkpoint (SAC) gates securin destruction

Securin degradation is the terminal, checkpoint-controlled step of anaphase licensing. "**APC/C-Cdc20 is required for polyubiquitination and degradation of securin and cyclin B at anaphase onset. The spindle assembly checkpoint delays APC/C-Cdc20 activation until all kinetochores attach to mitotic spindles**" ([PMID: 18852296](https://pubmed.ncbi.nlm.nih.gov/18852296/)). Thus while unattached kinetochores keep the SAC active, securin is stabilized and separase remains silenced; once attachment is complete, the checkpoint is satisfied and APC/C^Cdc20^ destroys securin.

Checkpoint integrity is essential to hold securin steady during arrest: "**Smurf2 inactivation prevents nocodazole-treated cells from accumulating cyclin B and securin and prometaphase arrest**" ([PMID: 18852296](https://pubmed.ncbi.nlm.nih.gov/18852296/)), and silencing Cdc20 restores securin accumulation. Loss of this control causes premature anaphase, misaligned/lagging chromosomes, and defective cytokinesis — the signature of losing the securin brake.

### 7. Both loss and overexpression of PTTG1 cause chromosomal instability — a dosage-sensitive guardian

Securin's protective function is exquisitely dosage sensitive; deviation in either direction is destabilizing. **Overexpression** drives chromosomal instability (CIN), aneuploidy, and transformation: "**Coexpression of Tax and PTTG enhanced chromosomal instability and neoplastic changes to levels greater than overexpression of either factor singularly**" ([PMID: 17507465](https://pubmed.ncbi.nlm.nih.gov/17507465/)), and hPTTG is overexpressed across many tumors (lymphomas, pituitary adenomas, breast cancer). A single point mutation is enough: "**a single mutation in pttg1 is sufficient to trigger the oncogenic properties of Securin**" ([PMID: 22819078](https://pubmed.ncbi.nlm.nih.gov/22819078/)).

Conversely, **loss** also destabilizes the genome. In Pttg-deficient pituitary, "**DNA damage signaling pathways were activated and aneuploidy was evident in the Pttg-deficient pituitary, triggering senescence-associated genes**" ([PMID: 17975001](https://pubmed.ncbi.nlm.nih.gov/17975001/)), producing ARF/p53/p21-dependent senescence and pituitary hypoplasia. This bidirectional phenotype defines PTTG1 as a balance-point guardian: too little or too much securin both compromise faithful chromosome segregation.

### 8. Moonlighting nuclear functions: transcriptional transactivation and p53 inhibition

Beyond the separase axis, securin has intrinsic gene-regulatory activity. It is a proline-rich protein with an N-terminal basic domain, a C-terminal acidic domain, and SH3-binding motifs; "**the acidic carboxyl-terminal region of hPTTG acts as a transactivation domain when fused to a heterologous DNA binding domain, both in yeast and in mammalian cells**" ([PMID: 9811450](https://pubmed.ncbi.nlm.nih.gov/9811450/)).

Securin also directly antagonizes p53. It physically interacts with p53, and "**This interaction blocks the specific binding of p53 to DNA and inhibits its transcriptional activity. Securin also inhibits the ability of p53 to induce cell death**" ([PMID: 12355087](https://pubmed.ncbi.nlm.nih.gov/12355087/)). The relationship is reciprocal and forms a feedback loop: PTTG1 suppresses p53-driven transcription of tumor-suppressive microRNAs, and "**we found that PTTG1 could inhibit p53 transcriptional activity to the four miRNAs**" (miR-329/300/381/655) ([PMID: 26320179](https://pubmed.ncbi.nlm.nih.gov/26320179/)). These activities mechanistically connect securin overexpression to escape from tumor-suppressive checkpoints.

### 9. Securin promotes angiogenesis via FGF-2, and the securin–separase axis influences membrane traffic

PTTG was originally characterized as tumorigenic partly through growth-factor signaling. "**A pituitary tumor-derived transforming gene (PTTG) has been isolated, which is tumorigenic in vivo, regulates bFGF secretion, and inhibits chromatid separation**" ([PMID: 10546001](https://pubmed.ncbi.nlm.nih.gov/10546001/)). In pituitary tumorigenesis, "**Maximal induction of rat pituitary pttg mRNA in vivo occurred early in pituitary transformation... coincident with bFGF and vascular endothelial growth factor induction and pituitary angiogenesis**" ([PMID: 10546001](https://pubmed.ncbi.nlm.nih.gov/10546001/)), and pttg is itself induced by estrogen and bFGF, forming a pro-angiogenic feed-forward loop. This PTTG→FGF-2 axis has clinical resonance: in differentiated thyroid cancer, PTTG and FGF-2 are co-overexpressed and independently predict aggressive behavior ([PMID: 12727994](https://pubmed.ncbi.nlm.nih.gov/12727994/)).

Separately, the securin–separase axis modulates membrane trafficking. "**cells depleted of securin or separase display defective acidification of early endosomes and increased membrane recruitment of vacuolar (V-) ATPase complexes**" ([PMID: 21272169](https://pubmed.ncbi.nlm.nih.gov/21272169/)), impairing constitutive secretion and receptor recycling. This is a less well-characterized, likely secondary function.

---

## Mechanistic Model / Interpretation

Securin is best understood as the **timer and safety catch on the anaphase trigger**. The core logic is a proteolytic relay in which one protease (separase) is held in reserve by securin until an upstream surveillance system (the SAC) certifies that segregation can proceed safely.

```
              UNATTACHED KINETOCHORE
                       │  (SAC "wait-anaphase" signal: Mad2, Bub1/Mad3)
                       ▼
        SAC ACTIVE ──► APC/C^Cdc20 INHIBITED
                       │
                       ▼
              SECURIN (PTTG1) STABLE
                       │  binds + inhibits (pseudosubstrate, H134)
                       │  + chaperones + targets to chromosomes
                       ▼
              SEPARASE (ESPL1) SILENCED  ◄── backup brake: Cdk1–cyclin B1
                       │
        ══════════════ ALL KINETOCHORES ATTACHED ══════════════
                       │  SAC satisfied
                       ▼
        APC/C^Cdc20 ACTIVE ──► ubiquitinates SECURIN + cyclin B
                       │
                       ▼  proteasomal destruction
              SECURIN DEGRADED
                       │
                       ▼
              SEPARASE ACTIVATED  (abruptly, near chromosomes)
                       │  cleaves kleisin
                       ▼
        RAD21/Scc1 (mitosis) / REC8 (meiosis) CLEAVED
                       │  cohesin ring opens
                       ▼
              SISTER-CHROMATID SEPARATION → ANAPHASE

   Parallel stress branch:  DNA damage ─► GSK-3β ─► SCF–βTrCP
        recognizes DDAYPE motif ─► SECURIN degraded ─► cell-cycle arrest
```

Three features make this model distinctive. First, securin is **bifunctional on the same target**: it is both the inhibitor and the folding chaperone/activator of separase — a "necessary evil" that separase needs to exist but must shed to act. The H134 residue is the molecular fulcrum separating these opposing activities. Second, securin provides **spatial as well as temporal** control, delivering separase to chromosomes so that its abrupt activation is locally concentrated where cohesin must be cut. Third, the system is **dosage-buffered**: the parallel Cdk1–cyclin B1 brake explains why securin-null mice survive, but this redundancy is imperfect — both securin excess and deficiency cause CIN, revealing that the true requirement is *balanced* securin, not merely its presence.

The **moonlighting functions** (transactivation, p53 inhibition, FGF-2/VEGF induction) are largely separable from the segregation role and are concentrated in the nucleus/secretory output. They are most relevant in the overexpression (oncogenic) regime, where securin simultaneously (a) destabilizes the genome through separase dysregulation, (b) disables the p53 checkpoint that would otherwise sense that instability, and (c) promotes angiogenesis to support tumor growth — a coherent three-pronged pro-tumor program.

| Property | Securin / PTTG1 |
|---|---|
| **Molecular class** | Intrinsically disordered enzyme regulator + chaperone (not itself catalytic) |
| **Primary target** | Separase (ESPL1), a cysteine endopeptidase |
| **Inhibition mechanism** | Pseudosubstrate blockade of catalytic site (cryo-EM confirmed) |
| **Dual activity** | Inhibitor (H134, high affinity) + chaperone/activator (weaker affinity) |
| **Downstream substrate (via separase)** | RAD21/Scc1 kleisin (mitosis); REC8 (meiosis) |
| **Primary localization** | Nucleus / mitotic chromosomes (also partly cytosolic; cell-type dependent) |
| **Cell-cycle regulation** | Degraded by APC/C^Cdc20 at anaphase; by SCF–βTrCP after DNA damage |
| **Upstream control** | Spindle assembly checkpoint (SAC) gates APC/C^Cdc20 |
| **Backup regulator of separase** | Cdk1–cyclin B1 |
| **Moonlighting roles** | Transactivation domain; p53 inhibition; FGF-2/VEGF angiogenesis; endosome acidification |
| **Disease relevance** | Dosage-sensitive oncogene; CIN/aneuploidy from both loss and overexpression |

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution |
|---|---|---|
| [28263324](https://pubmed.ncbi.nlm.nih.gov/28263324/) | Cryo-EM of metazoan separase–securin | **Structural proof** of pseudosubstrate inhibition; securin wraps both separase lobes |
| [22819078](https://pubmed.ncbi.nlm.nih.gov/22819078/) | Single mutation in Securin induces CIN | Defines PTTG1 = securin = separase inhibitor; single mutation is oncogenic |
| [12444553](https://pubmed.ncbi.nlm.nih.gov/12444553/) | hPTTG in lymphoid neoplasias | Confirms PTTG1 as vertebrate Pds1/Cut2 ortholog |
| [23798554](https://pubmed.ncbi.nlm.nih.gov/23798554/) | Isoform differences in securin | H134 switches inhibitor↔activator; separable domains |
| [25659430](https://pubmed.ncbi.nlm.nih.gov/25659430/) | Cdk1–cyclin B1 regulation of separase | Securin as co-translational chaperone; explains viable knockout; substrate = Scc1/Rad21 |
| [18460583](https://pubmed.ncbi.nlm.nih.gov/18460583/) | UV-induced securin degradation by SCF–βTrCP | APC/C at anaphase; SCF–βTrCP + DDAYPE motif after DNA damage |
| [28516917](https://pubmed.ncbi.nlm.nih.gov/28516917/) | Maternal-age APC/C decrease in securin | Links securin dosage to meiotic aneuploidy |
| [9811450](https://pubmed.ncbi.nlm.nih.gov/9811450/) | hPTTG overexpression + transactivation | Localization (cytosolic + nuclear); C-terminal transactivation domain |
| [14709851](https://pubmed.ncbi.nlm.nih.gov/14709851/) | hPTTG in A549 lung cancer | Cell-type-dependent nuclear/cytoplasmic distribution |
| [17102637](https://pubmed.ncbi.nlm.nih.gov/17102637/) | Nuclear exclusion of separase | Spatial safety mechanism compartmentalizing the axis |
| [22814604](https://pubmed.ncbi.nlm.nih.gov/22814604/) | Separase sensor / dual roles | Securin + cyclin B1 target separase to chromosomes |
| [18003702](https://pubmed.ncbi.nlm.nih.gov/18003702/) | Complete arm cohesin removal needs separase | Two-step cohesion loss; separase cleaves Scc1/Rad21 |
| [18852296](https://pubmed.ncbi.nlm.nih.gov/18852296/) | Smurf2 required for Mad2-dependent SAC | SAC gates APC/C^Cdc20 control of securin |
| [17507465](https://pubmed.ncbi.nlm.nih.gov/17507465/) | PTTG + HTLV-1 Tax cooperation | Overexpression drives CIN and transformation |
| [17975001](https://pubmed.ncbi.nlm.nih.gov/17975001/) | Senescence in pituitary hypoplasia | Loss of PTTG also causes aneuploidy + senescence |
| [12355087](https://pubmed.ncbi.nlm.nih.gov/12355087/) | Securin interacts with p53 | Securin blocks p53 DNA binding and apoptosis |
| [26320179](https://pubmed.ncbi.nlm.nih.gov/26320179/) | PTTG1-targeting miRNAs | p53/PTTG1 feedback loop via tumor-suppressive miRNAs |
| [10546001](https://pubmed.ncbi.nlm.nih.gov/10546001/) | Estrogen–PTTG–FGF in prolactinoma | PTTG regulates bFGF; angiogenesis loop |
| [12727994](https://pubmed.ncbi.nlm.nih.gov/12727994/) | PTTG + FGF-2 in thyroid cancer | Clinical PTTG→FGF-2 angiogenic/prognostic axis |
| [21272169](https://pubmed.ncbi.nlm.nih.gov/21272169/) | Securin/separase + endosomal acidification | Membrane-trafficking side function |
| [21876002](https://pubmed.ncbi.nlm.nih.gov/21876002/) | Calpain-1 cleaves Rad21 | Alternative (separase-independent) Rad21 protease — context for substrate |
| [25173175](https://pubmed.ncbi.nlm.nih.gov/25173175/) | SA2–Scc1 structure / Sgo1–Wapl | Structural context for centromeric cohesion protection |

The evidence base is unusually strong and internally consistent. The **primary molecular function** (separase inhibition) is supported by orthogonal lines: near-atomic structure ([PMID: 28263324](https://pubmed.ncbi.nlm.nih.gov/28263324/)), genetic/mutagenesis dissection ([PMID: 23798554](https://pubmed.ncbi.nlm.nih.gov/23798554/), [PMID: 22819078](https://pubmed.ncbi.nlm.nih.gov/22819078/)), live-cell activity sensing ([PMID: 22814604](https://pubmed.ncbi.nlm.nih.gov/22814604/)), and biochemistry of the downstream substrate ([PMID: 18003702](https://pubmed.ncbi.nlm.nih.gov/18003702/), [PMID: 25659430](https://pubmed.ncbi.nlm.nih.gov/25659430/)). Evolutionary conservation (Pds1/Cut2 → PTTG1) further anchors the annotation. The moonlighting functions rest on somewhat lower-throughput but direct biochemical evidence (co-IP, transactivation assays, expression correlations).

---

## Limitations and Knowledge Gaps

1. **Structural data are from a non-human ortholog.** The definitive pseudosubstrate mechanism was solved in *C. elegans* separase–securin ([PMID: 28263324](https://pubmed.ncbi.nlm.nih.gov/28263324/)). While conservation is high, a high-resolution *human* PTTG1–ESPL1 complex would confirm residue-level details (e.g., exact P1 contacts of the human protein).

2. **Intrinsic disorder complicates structural interpretation.** Securin is largely disordered when free; its conformation is defined mainly in the bound state. The structure of unbound human securin and the dynamics of the inhibitor↔chaperone transition remain incompletely characterized.

3. **Redundancy blurs genetic phenotypes.** Because Cdk1–cyclin B1 provides a backup brake, securin-null mice are viable/fertile ([PMID: 25659430](https://pubmed.ncbi.nlm.nih.gov/25659430/)), making it difficult to attribute phenotypes cleanly to securin loss alone. The relative contribution of securin vs. Cdk1–cyclin B1 in different human tissues is not fully quantified.

4. **Moonlighting functions may be context/dose dependent.** The p53 inhibition, transactivation, and FGF-2 induction activities are mostly documented in overexpression or tumor contexts; their physiological relevance at normal securin levels is less clear, and direct target genes of the transactivation domain are not comprehensively mapped.

5. **Membrane-trafficking role is mechanistically shallow.** The endosome-acidification/V-ATPase phenotype ([PMID: 21272169](https://pubmed.ncbi.nlm.nih.gov/21272169/)) is intriguing but the direct molecular link (does securin act here via separase, or independently?) is unresolved.

6. **No new primary data were generated.** This report is a literature/annotation synthesis (28 papers). Quantitative claims derive from the cited studies, not from independent re-analysis.

7. **Substrate specificity of separase (not securin) is the "reaction" of record.** Securin itself catalyzes no reaction; the enzymatic substrate (RAD21/Scc1, REC8) belongs to its regulated partner. This distinction should be kept explicit in any enzyme-centric annotation.

---

## Proposed Follow-up Experiments / Actions

1. **Solve the human PTTG1–ESPL1 complex** by cryo-EM to confirm the pseudosubstrate P1 residue and validate H134's role at atomic resolution in the human enzyme.

2. **Separation-of-function alleles in cells.** Introduce the H134 activator-switch and inhibition-only mutants into human cells to dissect, quantitatively, how the inhibitor vs. chaperone activities each contribute to segregation fidelity and to CIN.

3. **Map the transactivation targets.** Perform ChIP-seq / reporter screens with the securin acidic C-terminal domain fused to a defined DBD to define its direct transcriptional program and test whether endogenous securin regulates these genes at physiological levels.

4. **Dissect the p53–securin interface.** Determine the structural basis of the securin–p53 interaction and test whether disrupting it (without affecting separase binding) reverses the anti-apoptotic and pro-tumor phenotypes.

5. **Resolve the membrane-traffic mechanism.** Use separase-cleavage-site substrate profiling and V-ATPase interaction assays to determine whether securin's endosomal role is separase-dependent or a genuinely independent moonlighting function.

6. **Dosage titration in vivo.** Build allelic series (hypomorph → wild type → overexpression) to define the securin "safe window" for genome stability and map the thresholds at which CIN emerges in each direction.

7. **Therapeutic exploration.** Given securin overexpression across tumors and its dual disabling of genome stability and p53, evaluate securin (or the securin–separase interface) as a target — including synthetic-lethal strategies in CIN-high, securin-high cancers.

---

## Conclusion

PTTG1/Securin is the **checkpoint-controlled brake on separase**. Its primary function is to bind the cysteine protease separase and inhibit it by a pseudosubstrate mechanism while also chaperoning its folding and targeting it to chromosomes, thereby preventing premature cleavage of the cohesin kleisin RAD21/Scc1 until the spindle assembly checkpoint is satisfied and APC/C^Cdc20 destroys securin to license anaphase. It acts chiefly in the nucleus and on mitotic chromosomes, is a dosage-sensitive guardian of genome stability, and possesses separable nuclear moonlighting activities (transactivation, p53 inhibition, FGF-2/VEGF angiogenesis) that account for its proto-oncogenic behavior when overexpressed.


## Artifacts

- [OpenScientist final report](PTTG1-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PTTG1-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:12444553
2. PMID:22819078
3. PMID:28263324
4. PMID:25659430
5. PMID:23798554
6. PMID:18460583
7. PMID:28516917
8. PMID:9811450
9. PMID:14709851
10. PMID:17102637
11. PMID:22814604
12. PMID:18003702
13. PMID:18852296
14. PMID:17507465
15. PMID:17975001
16. PMID:12355087
17. PMID:26320179
18. PMID:10546001
19. PMID:12727994
20. PMID:21272169