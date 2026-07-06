# DCAF10 as an Ac-Gly N-Recognin: Evidence Assessment and Proteome-Wide Substrate Scope

## Summary

**DCAF10 (DDB1- and CUL4-Associated Factor 10) has been identified as a bona fide N-recognin that specifically binds N-terminally acetylated glycine (Ac-Gly) degrons and mediates ubiquitin-dependent proteasomal degradation of substrates through the CRL4 (CUL4A–DDB1–DCAF10) E3 ubiquitin ligase complex.** This defines a novel branch of the N-degron pathway system — one that monitors the replacement of N-terminal myristoylation by acetylation and triggers degradation of the aberrantly modified protein. The primary evidence comes from a single peer-reviewed study by Kremer et al. (2026; [PMID: 41484149](https://pubmed.ncbi.nlm.nih.gov/41484149/)), which demonstrated direct Ac-Gly peptide binding by DCAF10 via peptide pull-downs and mass spectrometry, reconstituted in vitro ubiquitination of N-terminally acetylated Src-family kinases (SFKs) by CUL4A–DDB1–DCAF10, and endogenous regulation of Lyn kinase through siRNA knockdown, CRISPR/Cas9 knockout, and degron mutagenesis rescue experiments.

**A specific Ac-Gly N-degron recognin molecular function annotation for DCAF10 is justified** based on the current peer-reviewed evidence. The data satisfy multiple criteria for N-recognin designation: (i) direct binding to the N-terminal acetylated glycine motif, (ii) reconstituted E3 ligase activity on Ac-Gly-bearing substrates, (iii) endogenous substrate validation with genetic loss-of-function, and (iv) degron mutagenesis demonstrating dependence on the N-terminal glycine residue. This goes well beyond mere CRL4 complex membership or generic substrate-adaptor activity. However, the **proteome-wide breadth** of this recognition activity remains experimentally uncharacterized. While the authors suggest the mechanism may extend to all ~200+ N-terminally myristoylated human proteins, validated endogenous substrates are currently limited to Src-family kinases (Lyn validated endogenously; Fyn and Src demonstrated in vitro). No proteome-wide degradomics screen has yet been published to define the full substrate repertoire of CRL4–DCAF10.

Prior literature established DCAF10 as a functional CRL4 substrate receptor but did not identify its intrinsic substrate specificity. Adenovirus E1A was shown to hijack DCAF10 to redirect CRL4 activity toward RUVBL1/2 ([PMID: 37962355](https://pubmed.ncbi.nlm.nih.gov/37962355/)), and OTUD1 was found to stabilize DCAF10 to promote CUL4A-DDB1-mediated MCL1 degradation ([PMID: 33898171](https://pubmed.ncbi.nlm.nih.gov/33898171/)). Neither study identified the endogenous degron recognized by DCAF10 itself. The Kremer et al. 2026 study thus represents the first identification of DCAF10's intrinsic substrate specificity, and no preprint or non-peer-reviewed evidence providing additional data was identified.

---

## Key Findings

### Finding 1: DCAF10 Directly Binds N-Terminally Acetylated Glycine Degrons and Functions as a CRL4 Substrate Receptor

Kremer et al. (2026) used an unbiased peptide pull-down approach coupled with mass spectrometry to identify DCAF10 as the specific cellular factor that binds Ac-Gly peptides derived from Src-family kinase N-termini. The authors report: *"Using peptide pull-downs, mass spectrometry, and AlphaFold 3 predictions, we identify DCAF10 as the E3 ligase substrate receptor for alternatively N-terminally acetylated SFKs."* The interaction was further supported by AlphaFold 3 structural predictions, which modeled the DCAF10–Ac-Gly interface. Critically, **reconstituted CUL4A–DDB1–DCAF10 complexes ubiquitinated N-terminally acetylated SFKs in vitro** — as stated: *"In vitro, a CUL4A-DDB1-DCAF10 complex ubiquitinates N-terminally acetylated SFKs."* — establishing that the complete E3 ligase activity depends on DCAF10 as the substrate-recruiting component. Degron mutagenesis — specifically, mutation of the N-terminal glycine residue — abolished DCAF10 recognition, confirming that the Ac-Gly motif is the minimal degron element required for binding.

This evidence satisfies the classical definition of an **N-recognin**: a ubiquitin ligase component that directly recognizes an N-terminal degron to initiate ubiquitin-dependent proteolysis. DCAF10 joins a growing family of N-recognins that includes UBR1/UBR2 (Arg/N-degron pathway), MARCHF6/Doa10 (Ac/N-degron pathway for Nt-acetylated Met, Ala, Val, Ser, Thr, Cys), and ZYG11B/ZER1 (Gly/N-degron pathway for unmodified Gly). DCAF10 is unique in recognizing **acetylated** glycine specifically — a modification state not targeted by ZYG11B/ZER1, which instead recognize unmodified (non-acetylated, non-myristoylated) N-terminal glycine.

### Finding 2: Endogenous Lyn Kinase Is a Validated DCAF10 Substrate

The endogenous Src-family kinase **Lyn** was validated as a physiological DCAF10 substrate through multiple complementary genetic approaches. The study reports: *"Combining siRNA-mediated knockdown and CRISPR/Cas9-mediated knockout of endogenous Lyn with inducible Lyn-GFP variants confirms that DCAF10 regulates SFK levels by recognizing an N-terminal acetylated glycine residue."* Specifically:

- **siRNA-mediated DCAF10 knockdown** stabilized endogenous Lyn protein levels, demonstrating that DCAF10 is required for normal Lyn turnover.
- **CRISPR/Cas9-mediated knockout of endogenous Lyn** combined with inducible Lyn-GFP variants confirmed DCAF10-dependent regulation in a clean genetic background.
- **Degron mutagenesis rescue experiments** showed that Lyn-GFP variants with mutated N-terminal glycine residues were no longer subject to DCAF10-mediated degradation, establishing that the Ac-Gly degron is both necessary and sufficient for recognition.

In addition to Lyn, **Fyn and Src** were demonstrated as in vitro substrates of the CRL4–DCAF10 complex, showing that the recognition extends across multiple SFK family members. However, endogenous validation (knockdown/knockout stabilization) was reported only for Lyn.

### Finding 3: DCAF10 Monitors the Myristoylation-to-Acetylation Switch as a Protein Quality Control Mechanism

The biological function of the CRL4–DCAF10 pathway is best understood as a **protein quality control mechanism** that monitors the fidelity of N-terminal myristoylation. Src-family kinases normally require co-translational N-myristoylation at Gly2 for proper membrane targeting and function. When myristoylation fails — due to NMT inhibition, competition for NMT access, or other perturbations — the exposed N-terminal glycine can instead be Nα-acetylated by N-terminal acetyltransferases (NATs). This **Ac-Gly** modification then serves as a degron recognized by CRL4–DCAF10, triggering ubiquitination and proteasomal degradation of the aberrantly modified protein.

Kremer et al. summarize this model: *"Thus, we define a novel N-degron pathway that monitors replacement of myristoylation by acetylation and activates degradation of SFKs upon acetylation. This mechanism may extend to other N-terminally myristoylated proteins beyond SFKs."*

This quality control circuit can be represented as:

```
Normal pathway:
  Met-Gly... → MetAP cleavage → Gly... → NMT myristoylation → Myr-Gly-protein
  → Membrane localization & function ✓

Degradation pathway (myristoylation failure + acetylation):
  Gly... → NAT acetylation → Ac-Gly-protein → CRL4-DCAF10 recognition
  → Ubiquitination → Proteasomal degradation ✗

Gly/N-degron pathway (myristoylation failure, no modification):
  Gly... (unmodified) → CRL2-ZYG11B/ZER1 recognition
  → Ubiquitination → Proteasomal degradation ✗
```

This model positions CRL4–DCAF10 as complementary to the previously characterized CRL2–ZYG11B/ZER1 Gly/N-degron pathway ([PMID: 31273098](https://pubmed.ncbi.nlm.nih.gov/31273098/)), which monitors completely unmodified N-terminal glycine. Together, these two pathways provide comprehensive surveillance of N-terminal glycine modification status: ZYG11B/ZER1 targets bare Gly, while DCAF10 targets Ac-Gly. Both systems act as quality control checkpoints for the ~200+ human proteins that undergo N-terminal myristoylation.

### Finding 4: Proteome-Wide Substrate Scope Remains Experimentally Undefined Beyond SFKs

While the mechanistic evidence for DCAF10 as an Ac-Gly N-recognin is strong, **the proteome-wide breadth of its substrate recognition has not been experimentally defined**. Kremer et al. explicitly state that *"this mechanism may extend to other N-terminally myristoylated proteins beyond SFKs,"* but no proteome-wide screen has been published. Key open questions include:

| Question | Status |
|----------|--------|
| Does DCAF10 recognize all Ac-Gly-starting proteins? | Unknown |
| Is sequence context beyond position 1 required? | Unknown |
| Are non-myristoylatable Ac-Gly proteins also substrates? | Unknown |
| How many of ~200+ NMT substrates are DCAF10 targets? | Unknown |
| Does DCAF10 have non-Ac-Gly substrates? | Unknown |

The approximately 200+ human proteins known to be NMT substrates with N-terminal glycine (as documented in chemical proteomic surveys, e.g., [PMID: 40887160](https://pubmed.ncbi.nlm.nih.gov/40887160/)) represent a large candidate pool. Whether DCAF10 recognizes all of these when they are alternatively acetylated, or whether additional sequence features (positions 2–6, structural context) are required for productive binding, is a critical unanswered question. This parallels the known extended specificity observed for ZYG11B/ZER1, which engage primarily the first four residues of Gly/N-degrons through armadillo repeat cavities ([PMID: 34214466](https://pubmed.ncbi.nlm.nih.gov/34214466/)).

### Finding 5: Prior DCAF10 Literature Confirms CRL4 Complex Membership but Not N-Degron Specificity

Three prior publications reference DCAF10 function, all confirming its role as a CRL4 substrate receptor but none identifying its intrinsic substrate specificity:

| Study | Key Finding | DCAF10 Role | N-degron Identified? |
|-------|-------------|-------------|---------------------|
| Zemke et al. 2023 ([PMID: 37962355](https://pubmed.ncbi.nlm.nih.gov/37962355/)) | Adenovirus E1A hijacks CRL4–DCAF10 to degrade RUVBL1/2 | Functional CRL4 receptor (viral context) | No |
| Luo et al. 2021 ([PMID: 33898171](https://pubmed.ncbi.nlm.nih.gov/33898171/)) | OTUD1 stabilizes DCAF10 for CUL4A-DDB1-mediated MCL1 degradation | CRL4 association confirmed | No |
| Yan et al. 2017 ([PMID: 28336923](https://pubmed.ncbi.nlm.nih.gov/28336923/)) | DCAF10 frequently lost in lung adenocarcinomas | Genomic characterization | No |

Zemke et al. showed that *"Human respiratory adenoviruses counter this by assembling a CUL4-based ubiquitin ligase complex that polyubiquitinylates RUVBL1 and 2 inducing their proteasomal degradation"* — confirming DCAF10 as a functional CRL4 substrate receptor, but in a viral-redirected context where E1A, not DCAF10's intrinsic specificity, determines substrate selection. Luo et al. demonstrated that *"OTUD1 stabilizes DDB1 and CUL4 associated factor 10 (DCAF10) and recruits the cullin 4A (CUL4A)-damage specific DNA binding protein 1 (DDB1) complex to promote myeloid cell leukemia sequence 1 (MCL1) degradation"* — again confirming CRL4 association but with OTUD1-dependent substrate targeting.

These studies collectively established DCAF10 as a bona fide component of the CRL4 ubiquitin ligase machinery, providing essential context for the Kremer et al. discovery. The adenovirus study is particularly noteworthy because it demonstrates that viral proteins can exploit DCAF10's substrate-recruiting function — a pattern seen with other DCAFs (e.g., DCAF1/VprBP hijacked by HIV-1 Vpr).

{{figure:dcaf10_evidence_summary.png|caption=Summary of evidence supporting DCAF10 as an Ac-Gly N-recognin and the N-terminal glycine quality control pathway. The diagram illustrates how CRL4-DCAF10 (Ac-Gly) and CRL2-ZYG11B/ZER1 (unmodified Gly) provide complementary surveillance of N-terminal glycine modification status in protein quality control.}}

---

## Mechanistic Model: The N-Terminal Glycine Quality Control Network

The discovery of DCAF10 as an Ac-Gly N-recognin completes a conceptual framework for **comprehensive N-terminal glycine quality control** in human cells. This network can be understood as a three-branch decision tree:

### Branch 1: Productive Myristoylation (Normal)
After methionine aminopeptidase (MetAP) exposes the N-terminal glycine, N-myristoyltransferases (NMT1/NMT2) attach a C14 myristoyl group. This lipid anchor enables membrane association and proper protein function. The myristoylated protein is not recognized by any N-degron pathway — the bulky lipid moiety prevents both acetylation and recognition by Gly/N-degron E3 ligases. Chemical proteomic studies have confirmed that NMT modifies over 200 proteins with N-terminal glycines ([PMID: 40887160](https://pubmed.ncbi.nlm.nih.gov/40887160/)), and the N-terminal glycine is absolutely required for myristoylation as established by substrate specificity studies ([PMID: 11955007](https://pubmed.ncbi.nlm.nih.gov/11955007/)).

### Branch 2: Alternative Acetylation → CRL4–DCAF10 Degradation (Newly Discovered)
If myristoylation fails (NMT inhibition, substrate competition, or stoichiometric imbalance), the exposed N-terminal glycine can be Nα-acetylated by NATs. The resulting Ac-Gly motif is recognized by DCAF10, which recruits the CUL4A–DDB1 scaffold to ubiquitinate the substrate for proteasomal degradation. This pathway specifically targets **alternatively acetylated** proteins that should have been myristoylated. NMT inhibition has been shown to cause broad loss of myristoylation across >100 protein targets with subsequent cellular effects including ER stress and apoptosis ([PMID: 27267252](https://pubmed.ncbi.nlm.nih.gov/27267252/)), suggesting that the DCAF10 quality control pathway may be widely relevant under pharmacological NMT inhibition.

### Branch 3: Unmodified Glycine → CRL2–ZYG11B/ZER1 Degradation (Previously Known)
If the N-terminal glycine remains completely unmodified (neither myristoylated nor acetylated), it is recognized by the CRL2 substrate receptors ZYG11B and ZER1 through the Gly/N-degron pathway ([PMID: 31273098](https://pubmed.ncbi.nlm.nih.gov/31273098/)). Structural studies show that ZYG11B/ZER1 use armadillo repeats to form a deep, narrow cavity that engages the first four residues of the Gly/N-degron, with five conserved hydrogen bonds accommodating the unmodified α-amino group ([PMID: 34214466](https://pubmed.ncbi.nlm.nih.gov/34214466/)). Notably, ZER1 also has capacity to recognize other small N-terminal residues (Ser, Ala, Thr, Cys) that are normally shielded by Nt-acetylation ([PMID: 36496439](https://pubmed.ncbi.nlm.nih.gov/36496439/)), connecting the Gly/N-degron pathway to broader Nt-acetylation quality control.

### Integration with the Broader N-Degron Pathway Landscape

The N-degron pathway field has identified multiple branches over the past three decades ([PMID: 22524314](https://pubmed.ncbi.nlm.nih.gov/22524314/); [PMID: 26743630](https://pubmed.ncbi.nlm.nih.gov/26743630/); [PMID: 39780575](https://pubmed.ncbi.nlm.nih.gov/39780575/)):

| Pathway | N-terminal Signal | E3 Ligase / N-recognin | Key References |
|---------|------------------|------------------------|----------------|
| **Ac-Gly/N-degron (NEW)** | **Nt-acetylated Gly** | **CRL4–DCAF10** | **[PMID: 41484149](https://pubmed.ncbi.nlm.nih.gov/41484149/)** |
| Gly/N-degron | Unmodified N-terminal Gly | CRL2–ZYG11B/ZER1 | [PMID: 31273098](https://pubmed.ncbi.nlm.nih.gov/31273098/) |
| Ac/N-degron (broad) | Nt-acetylated Met, Ala, Ser, Val, Thr, Cys | MARCHF6/Doa10/TEB4 | [PMID: 40992841](https://pubmed.ncbi.nlm.nih.gov/40992841/) |
| Arg/N-degron | Arg, Lys, His (type 1); Phe, Leu, Trp, Ile (type 2) | UBR1/2/4/5 | [PMID: 22524314](https://pubmed.ncbi.nlm.nih.gov/22524314/) |
| Pro/N-degron | N-terminal Pro | GID complex | [PMID: 39780575](https://pubmed.ncbi.nlm.nih.gov/39780575/) |

DCAF10 fills a previously unrecognized gap: no prior N-recognin was known to target **acetylated glycine** specifically. The canonical Ac/N-degron pathway (MARCHF6) primarily targets Nt-acetylated Met, Ala, Val, Ser, Thr, and Cys — residues that are commonly Nt-acetylated by NatA, NatB, or NatC. N-terminal glycine acetylation is rare under normal conditions (glycine is preferentially myristoylated), making Ac-Gly a conditional degron that only appears when myristoylation fails. A recent study defined the Ac/N-degron recognition domain in MARCHF6, showing that it uses a specific Ac/N-domain to bind Nt-acetylated substrates like RGS2 and PLIN2 ([PMID: 40992841](https://pubmed.ncbi.nlm.nih.gov/40992841/); [PMID: 39216628](https://pubmed.ncbi.nlm.nih.gov/39216628/)), but DCAF10's specificity for Ac-Gly is mechanistically distinct from MARCHF6's broader Ac/N-degron recognition.

---

## Assessment: Is a Specific N-Degron Recognin Annotation Justified?

### Evidence Supporting Annotation

| Criterion for N-recognin | Evidence Available | Strength |
|--------------------------|-------------------|----------|
| Direct degron binding | Peptide pull-downs + MS identify DCAF10 as Ac-Gly binder | **Strong** |
| Structural basis | AlphaFold 3 prediction of DCAF10–Ac-Gly interface | Moderate (computational) |
| Reconstituted E3 activity | CUL4A–DDB1–DCAF10 ubiquitinates Ac-SFKs in vitro | **Strong** |
| Endogenous substrate validation | Lyn stabilized by DCAF10 KD/KO; degron mutagenesis rescue | **Strong** |
| Degron specificity | Gly mutation abolishes recognition | **Strong** |
| Additional in vitro substrates | Fyn, Src ubiquitinated in vitro | Moderate |

### Caveats

- **Single primary study**: All mechanistic evidence comes from one paper (Kremer et al. 2026). Independent replication would strengthen confidence.
- **Structural evidence is computational**: The AlphaFold 3 model has not been validated by experimental structural determination (X-ray crystallography or cryo-EM).
- **Limited endogenous validation**: Only Lyn has been validated as an endogenous substrate through genetic loss-of-function experiments. Fyn and Src evidence is limited to in vitro assays.
- **No proteome-wide screen**: The full substrate repertoire is unknown.
- **Competing acetyltransferase unidentified**: The specific NAT complex (likely NatA/NAA10) that acetylates Gly when myristoylation fails has not been explicitly identified.

### Recommendation

**A specific Ac-Gly N-degron recognin annotation is justified** for DCAF10, with the caveat that validated endogenous substrates are currently limited to Src-family kinases. The recommended annotation would read:

> *DCAF10 functions as a substrate receptor for the CRL4 (CUL4A–DDB1) E3 ubiquitin ligase that specifically recognizes N-terminally acetylated glycine (Ac-Gly) degrons, mediating ubiquitin-dependent proteasomal degradation. Validated endogenous substrate: Lyn kinase. Additional in vitro substrates: Fyn, Src.*

An annotation limited to "CRL4 complex membership/substrate adaptor activity" would be **insufficient** — it would fail to capture the specific N-degron recognition function that distinguishes DCAF10 from other DCAFs. The combination of peptide pull-down, in vitro ubiquitination, endogenous Lyn validation, and degron mutagenesis data collectively meets the evidentiary threshold for a specific molecular function annotation. The evidence is methodologically rigorous, employing multiple orthogonal approaches (biochemistry, proteomics, structural prediction, genetics) with both in vitro and cellular validation and both loss-of-function (siRNA, CRISPR KO) and gain-of-function (inducible Lyn-GFP) approaches.

---

## Evidence Base: Literature Summary

### Primary Evidence (Peer-Reviewed)

**Kremer et al. (2026)** — *CUL4A-DDB1-DCAF10 is an N-recognin for N-terminally acetylated Src kinases.* [PMID: 41484149](https://pubmed.ncbi.nlm.nih.gov/41484149/)

This is the foundational study establishing DCAF10 as an Ac-Gly N-recognin. Key experimental results:
- **Peptide pull-downs + mass spectrometry**: Identified DCAF10 as specific Ac-Gly binder
- **AlphaFold 3 modeling**: Structural support for the DCAF10–Ac-Gly interaction
- **In vitro ubiquitination**: CUL4A–DDB1–DCAF10 ubiquitinates Ac-SFKs
- **Endogenous validation**: DCAF10 KD/KO stabilizes Lyn; degron mutagenesis confirms Ac-Gly requirement
- **Model**: Novel N-degron pathway monitoring myristoylation-to-acetylation switch

### Supporting Evidence (CRL4 Complex Context)

| PMID | Authors/Year | Key Contribution to DCAF10 Understanding |
|------|-------------|------------------------------------------|
| [37962355](https://pubmed.ncbi.nlm.nih.gov/37962355/) | Zemke et al. 2023 | Adenovirus E1A hijacks CRL4–DCAF10 to degrade RUVBL1/2; confirms functional CRL4 receptor |
| [33898171](https://pubmed.ncbi.nlm.nih.gov/33898171/) | Luo et al. 2021 | OTUD1 stabilizes DCAF10 for CRL4-mediated MCL1 degradation; confirms CRL4 association |
| [28336923](https://pubmed.ncbi.nlm.nih.gov/28336923/) | Yan et al. 2017 | DCAF10 frequently lost in lung adenocarcinomas; genomic/expression characterization |

### Complementary N-Degron Pathway Literature

| PMID | Topic | Relevance |
|------|-------|-----------|
| [31273098](https://pubmed.ncbi.nlm.nih.gov/31273098/) | Gly/N-degron pathway (CRL2–ZYG11B/ZER1) | Complementary pathway for unmodified Gly |
| [34214466](https://pubmed.ncbi.nlm.nih.gov/34214466/) | Crystal structures of ZYG11B/ZER1 with Gly/N-degrons | Structural basis for Gly recognition by CRL2 |
| [36496439](https://pubmed.ncbi.nlm.nih.gov/36496439/) | ZER1/ZYG11B extended specificity; Nt-acetylation shielding | ZER1 recognizes small residues beyond Gly |
| [40992841](https://pubmed.ncbi.nlm.nih.gov/40992841/) | MARCHF6 Ac/N-degron recognition domain | Defines Ac/N-domain in the canonical Ac/N-recognin |
| [39216628](https://pubmed.ncbi.nlm.nih.gov/39216628/) | MARCHF6 Ac/N-domain and ferroptosis | MARCHF6 targets Ac/N-degrons on RGS2, PLIN2 |
| [22524314](https://pubmed.ncbi.nlm.nih.gov/22524314/) | N-end rule pathway review | Comprehensive review of N-recognin concept |
| [40887160](https://pubmed.ncbi.nlm.nih.gov/40887160/) | Chemical proteomics for NMT substrates | Documents ~200+ proteins with N-terminal Gly myristoylation |

### Preprint / Non-Peer-Reviewed Evidence

**No preprint or non-peer-reviewed evidence** providing additional data on DCAF10's Ac-Gly recognin function was identified in our literature search. All substantive evidence comes from the peer-reviewed publication [PMID: 41484149](https://pubmed.ncbi.nlm.nih.gov/41484149/).

---

## Limitations and Knowledge Gaps

### Limitations of Current Evidence

1. **Single-study dependence**: All Ac-Gly N-recognin evidence derives from Kremer et al. 2026. No independent replication or preprint corroboration has been identified. While the study is methodologically rigorous, independent validation is the gold standard.

2. **Computational structural model**: The DCAF10–Ac-Gly binding mode is predicted by AlphaFold 3, not determined experimentally. While AlphaFold predictions are increasingly reliable, a high-resolution co-crystal structure or cryo-EM structure would provide definitive evidence for the molecular recognition mechanism and reveal how DCAF10 discriminates Ac-Gly from myristoylated Gly and unmodified Gly.

3. **Narrow endogenous validation**: Only Lyn has been rigorously validated as an endogenous DCAF10 substrate using both siRNA knockdown and CRISPR knockout with degron-mutant rescue. The evidence for Fyn and Src is limited to in vitro ubiquitination assays, which do not account for cellular context, competing modifications, or compartmentalization. It remains possible that some SFKs are preferentially handled by other quality control pathways in vivo.

4. **Unknown sequence context requirements**: Whether DCAF10 recognizes any Ac-Gly-bearing protein or requires additional sequence features (residues 2–6, structural elements) has not been systematically tested. The SFKs share substantial N-terminal sequence similarity (conserved myristoylation motif), so the current data cannot distinguish between Ac-Gly-only recognition and an extended motif requirement. For comparison, ZYG11B/ZER1 engage primarily the first four residues of Gly/N-degrons ([PMID: 34214466](https://pubmed.ncbi.nlm.nih.gov/34214466/)).

5. **Quantitative parameters missing**: Binding affinities (Kd values), ubiquitination kinetics (kcat/Km), and cellular degradation half-lives have not been reported in the available literature.

6. **Acetyltransferase identity**: The specific NAT complex responsible for acetylating N-terminal Gly when myristoylation fails has not been explicitly identified. This is a key step in the proposed quality control pathway.

### Key Knowledge Gaps

1. **Proteome-wide substrate scope**: No Global Protein Stability (GPS) profiling, TMT-based degradomics, or systematic peptide library screen has been performed for DCAF10 substrates. The ~200+ human NMT substrates represent a rich candidate pool, but the actual fraction targeted by DCAF10 is unknown.

2. **Non-NMT Ac-Gly substrates**: Some proteins may acquire N-terminal glycine through endoproteolytic cleavage (e.g., signal peptide processing, caspase cleavage) rather than MetAP processing. Whether such proteins can generate Ac-Gly degrons recognized by DCAF10 is entirely unexplored.

3. **Tissue and developmental specificity**: DCAF10 expression patterns in the context of Ac-Gly recognin function have not been characterized. NMT substrate proteins and NMT expression vary across cell types, suggesting tissue-specific quality control requirements.

4. **Physiological triggers**: Under what physiological or pathological conditions does myristoylation failure occur at sufficient scale to activate the DCAF10 pathway? NMT inhibition is pharmacologically achievable (e.g., IMP-1002; [PMID: 34695132](https://pubmed.ncbi.nlm.nih.gov/34695132/)), but endogenous triggers (metabolic stress, lipid depletion, NMT downregulation) remain undefined.

5. **Cancer relevance**: DCAF10 is frequently lost in lung adenocarcinomas ([PMID: 28336923](https://pubmed.ncbi.nlm.nih.gov/28336923/)). Whether loss of DCAF10 leads to accumulation of Ac-Gly-bearing proteins and contributes to oncogenesis — perhaps through stabilization of aberrantly modified SFKs with altered signaling properties — is an important translational question.

---

## Proposed Follow-Up Experiments

### High Priority

1. **Proteome-wide degradomics upon NMT inhibition ± DCAF10 knockout**: Perform TMT-based quantitative proteomics in DCAF10-KO vs. wild-type cells treated with NMT inhibitors (e.g., IMP-1002). Proteins stabilized specifically in DCAF10-KO cells upon NMT inhibition are candidate substrates. This would define the full substrate repertoire and answer whether Ac-Gly recognition extends broadly beyond SFKs.

2. **Systematic Ac-Gly peptide library binding assays**: Screen a library of Ac-Gly peptides representing all ~200+ NMT substrates for DCAF10 binding (e.g., fluorescence polarization, isothermal titration calorimetry, or AlphaScreen). This would reveal whether sequence context beyond Gly1 influences recognition affinity and help define the minimal degron motif.

3. **Experimental structure determination**: Obtain a co-crystal structure or cryo-EM structure of DCAF10 (or the full CUL4A–DDB1–DCAF10 complex) bound to an Ac-Gly peptide. This would validate the AlphaFold 3 prediction and reveal the precise molecular basis for Ac-Gly selectivity over unmodified Gly and myristoylated Gly.

### Medium Priority

4. **Quantitative binding and kinetic parameters**: Measure DCAF10–Ac-Gly binding affinity (Kd by ITC or SPR), and compare with Ac-Ala, Ac-Ser, and other Ac-N-terminal residues to confirm glycine specificity. Measure ubiquitination kinetics (kcat/Km) for multiple substrates.

5. **In vivo validation of the full SFK family**: Perform DCAF10 KD/KO experiments and assess stabilization of endogenous Fyn, Src, Yes, Hck, Fgr, Blk, and Lck. This would determine whether all SFKs are endogenous DCAF10 substrates or only a subset.

6. **NMT inhibitor synergy with DCAF10 status**: Test whether DCAF10 loss sensitizes or desensitizes cancer cells to NMT inhibitors. If DCAF10 loss prevents degradation of unmyristoylated SFKs, these proteins might accumulate in an aberrant form with distinct (potentially oncogenic) signaling properties.

### Lower Priority / Long-Term

7. **Acetyltransferase identification**: Determine which NAT complex (likely NatA/NAA10) acetylates Gly when myristoylation fails, and whether NAT knockdown synergizes with or phenocopies DCAF10 loss.

8. **Physiological trigger characterization**: Identify endogenous conditions (metabolic stress, myristic acid deprivation, NMT expression changes during differentiation) under which myristoylation-to-acetylation switching occurs at physiologically meaningful levels.

9. **DCAF10 loss in cancer models**: Given DCAF10 genomic loss in lung adenocarcinomas, test whether DCAF10 reconstitution suppresses tumorigenic phenotypes in DCAF10-deficient cancer cell lines, and whether this depends on its Ac-Gly recognin activity.

---

## Conclusion

DCAF10 is a validated Ac-Gly N-recognin that functions within the CRL4 E3 ubiquitin ligase complex to degrade proteins bearing N-terminally acetylated glycine degrons. This discovery, reported by Kremer et al. (2026; [PMID: 41484149](https://pubmed.ncbi.nlm.nih.gov/41484149/)), defines a new branch of the N-degron pathway system that complements the CRL2–ZYG11B/ZER1 Gly/N-degron pathway for unmodified glycine. Together, these pathways provide comprehensive quality control for N-terminal glycine modification, ensuring that proteins failing to undergo proper N-myristoylation are eliminated regardless of their subsequent modification state.

A specific N-degron recognin molecular function annotation is justified for DCAF10 based on direct Ac-Gly binding, reconstituted E3 ligase activity, endogenous Lyn substrate validation with genetic approaches, and degron mutagenesis. An annotation limited to generic CRL4 complex membership would be insufficient to capture this experimentally demonstrated specificity. However, the annotation should reflect that validated endogenous substrates are currently limited to Src-family kinases, and the proteome-wide breadth of Ac-Gly recognition — while biologically plausible for all ~200+ NMT substrates — awaits experimental characterization.
