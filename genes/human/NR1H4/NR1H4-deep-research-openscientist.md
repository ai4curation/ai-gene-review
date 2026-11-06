---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-31T18:22:51.301043'
end_time: '2026-10-31T18:33:35.516938'
duration_seconds: 644.22
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: NR1H4
  gene_symbol: NR1H4
  uniprot_accession: Q96RI1
  protein_description: 'RecName: Full=Bile acid receptor; AltName: Full=Farnesoid
    X-activated receptor; AltName: Full=Farnesol receptor HRR-1; AltName: Full=Nuclear
    receptor subfamily 1 group H member 4; AltName: Full=Retinoid X receptor-interacting
    protein 14; Short=RXR-interacting protein 14;'
  gene_info: Name=NR1H4; Synonyms=BAR, FXR, HRR1, RIP14;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the nuclear hormone receptor family. NR1
  protein_domains: NHR-like_dom_sf. (IPR035500); NR_LBD_NR1H4. (IPR044114); Nucl_hrmn_rcpt_lig-bd.
    (IPR000536); Nuclear_hormone_rcpt_NR1. (IPR050234); Nuclear_hrmn_rcpt. (IPR001723)
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
citation_count: 16
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: NR1H4-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: NR1H4-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q96RI1
- **Protein Description:** RecName: Full=Bile acid receptor; AltName: Full=Farnesoid X-activated receptor; AltName: Full=Farnesol receptor HRR-1; AltName: Full=Nuclear receptor subfamily 1 group H member 4; AltName: Full=Retinoid X receptor-interacting protein 14; Short=RXR-interacting protein 14;
- **Gene Information:** Name=NR1H4; Synonyms=BAR, FXR, HRR1, RIP14;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the nuclear hormone receptor family. NR1
- **Key Domains:** NHR-like_dom_sf. (IPR035500); NR_LBD_NR1H4. (IPR044114); Nucl_hrmn_rcpt_lig-bd. (IPR000536); Nuclear_hormone_rcpt_NR1. (IPR050234); Nuclear_hrmn_rcpt. (IPR001723)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "NR1H4" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'NR1H4' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **NR1H4** (gene ID: NR1H4, UniProt: Q96RI1) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# NR1H4 (FXR, Farnesoid X Receptor): Functional Annotation Report

**UniProt:** Q96RI1 | **Gene:** NR1H4 (synonyms: BAR, FXR, HRR1, RIP14) | **Organism:** *Homo sapiens* | **Family:** Nuclear hormone receptor, subfamily NR1

---

## Summary

**NR1H4 encodes the Farnesoid X Receptor (FXR), the principal intracellular (nuclear) receptor for bile acids and the master transcriptional regulator of bile-acid homeostasis in humans.** Identity is firmly established: the gene symbol, organism, protein family (nuclear hormone receptor, NR1 subfamily), and ligand-binding/DNA-binding domain architecture all match the extensive primary literature on the bile-acid receptor FXR. There is no ambiguity — the literature for NR1H4/FXR in *Homo sapiens* is deep and internally consistent.

Mechanistically, FXR is a **ligand-activated transcription factor**. Its endogenous agonists are bile acids, with chenodeoxycholic acid (CDCA) being the most potent natural human ligand. Upon bile-acid binding within its ligand-binding domain (LBD), FXR forms an **obligate heterodimer with retinoid X receptor alpha (RXRα)**, binds **inverted-repeat-1 (IR-1)** DNA response elements in the promoters of target genes, recruits coactivators via its activation-function-2 (AF-2) surface (helix 12), and switches target genes on or off. Through this single biochemical activity, FXR governs the complete enterohepatic bile-acid cycle — synthesis, conjugation/detoxification, canalicular export, intestinal reabsorption, and feedback repression — and secondarily tunes hepatic lipid and glucose metabolism and intestinal antibacterial barrier defense.

FXR carries out its function **in the nucleus of hepatocytes and enterocytes**, with lower expression in kidney and adrenal glands. It is spatially and mechanistically distinct from the separate *membrane* bile-acid receptor TGR5/GPBAR1. The two defining effector arms of FXR signaling are: (1) hepatic induction of **Small Heterodimer Partner (SHP/NR0B2)**, which represses CYP7A1 (the rate-limiting bile-acid synthetic enzyme), and (2) intestinal induction of **FGF15/FGF19**, an enterokine that signals back to the liver via FGFR4/β-Klotho to suppress synthesis and refill the gallbladder. FXR's clinical importance is validated by human genetics (loss-of-function causes progressive familial intrahepatic cholestasis) and pharmacology (the synthetic agonist obeticholic acid, a CDCA derivative, developed for cholestatic and metabolic liver disease).

---

## Key Findings

### 1. FXR is the nuclear receptor for bile acids that transcriptionally controls bile-acid homeostasis

The foundational discovery establishing FXR's primary function came from Makishima et al. (1999, *Science*), who demonstrated that **bile acids are the physiological ligands of FXR**. In the same work, ligand-bound FXR was shown to **repress transcription of CYP7A1** — the gene encoding cholesterol 7α-hydroxylase, the rate-limiting enzyme of bile-acid synthesis — and to **activate the gene encoding intestinal bile-acid-binding protein**. This established, in a single study, the core transcriptional feedback loop: bile acids activate their own nuclear receptor, which then shuts down further bile-acid production and promotes enterohepatic transport ([PMID: 10334992](https://pubmed.ncbi.nlm.nih.gov/10334992/)).

This is the central fact of FXR biology: FXR is a *bile-acid sensor* that converts intracellular bile-acid concentration into a transcriptional program protecting the cell and organism from bile-acid overload while maintaining sufficient bile for digestion.

### 2. FXR functions as an obligate heterodimer with RXRα

FXR does not act alone. It partners with **retinoid X receptor alpha (RXRα)** to form the DNA-binding, transcriptionally active unit. Crystal structures of the human FXR/RXRα ligand-binding-domain heterodimer (Wang et al., 2018) show that "FXR and nuclear receptor retinoid X receptor α (RXRα) form a heterodimer that controls the expression of numerous downstream genes." Critically, the heterodimer is not merely a scaffolding convenience — it enhances function: "both FXR and RXR bind to the transcriptional coregulator steroid receptor coactivator 1 with higher affinity when they are part of the heterodimer complex than when they are in their respective monomeric states." Ligand binding plus heterodimerization induce conformational changes at helix 11/12 (the AF-2 surface) that stabilize the coactivator-binding surface ([PMID: 30275017](https://pubmed.ncbi.nlm.nih.gov/30275017/)).

### 3. The ligand-binding domain accommodates bile acids via an arginine anchor and a histidine/AF-2 activation trigger

High-resolution X-ray crystallography (Soisson et al., 2008; 1.9 Å) defined how bile acids are recognized. Naturally occurring bile acids bind in a specific pose, with their carboxylate neutralized by an **arginine in the binding pocket**. Receptor activation involves a **protonated histidine** that forms part of the activation trigger engaging helix 12 (AF-2). Interestingly, synthetic agonists can bind in the *reverse* orientation: "The steroid ring system of MFA-1 binds with its D ring-facing helix 12 (AF-2) in a manner reminiscent of hormone binding to classical steroid hormone receptors and the reverse of the pose adopted by naturally occurring bile acids when bound to FXR" ([PMID: 18391212](https://pubmed.ncbi.nlm.nih.gov/18391212/)). This structural work explains both endogenous ligand recognition and the rational design of synthetic FXR drugs.

### 4. FXR binds IR-1 response elements in target-gene promoters

The DNA "grammar" of FXR signaling is the **inverted-repeat-1 (IR-1)** element — two copies of the nuclear-receptor half-site (AGGTCA) arranged as an inverted repeat separated by a single nucleotide. Matsukuma et al. (2006) showed that "an IR-1 is present in promoters of several genes of bile acid and lipid homeostasis and binds farnesoid X receptor/retinoid X receptor (FXR/RXR) heterodimers to mediate bile acid-dependent transcription" ([PMID: 16957179](https://pubmed.ncbi.nlm.nih.gov/16957179/)). Direct, specific FXR/RXRα binding to IR-1 elements was independently confirmed in the human kininogen promoter — "FXR/RXRalpha heterodimers specifically bind to this IR-1" ([PMID: 12761213](https://pubmed.ncbi.nlm.nih.gov/12761213/)) — and in the fetuin-B promoter, where mutations in the IR-1 sites abolished both binding and transactivation ([PMID: 17655523](https://pubmed.ncbi.nlm.nih.gov/17655523/)).

### 5. FXR enforces bile-acid feedback through two effector arms: hepatic SHP and intestinal FGF15/19

FXR controls bile-acid synthesis through two complementary, tissue-specific circuits (reviewed in Keitel et al., 2019; Di Ciaula et al., 2022):

- **Hepatic arm:** FXR induces **Small Heterodimer Partner (SHP, NR0B2)**, an atypical repressor nuclear receptor that inhibits LRH-1 and thereby represses CYP7A1.
- **Intestinal arm:** FXR induces **FGF15 (mouse) / FGF19 (human)**, an enterokine secreted into portal blood that signals through hepatic **FGFR4/β-Klotho** to suppress bile-acid synthesis and promote gallbladder refilling.

As stated in the review: "FXR and its hepatic and intestinal target genes, small heterodimer partner (SHP, NR0B2) and fibroblast growth factor 15/19 (Fgf15 in mice, FGF19 in humans), transcriptionally regulate BA synthesis, detoxification, secretion, and absorption in the enterohepatic circulation" ([PMID: 31201556](https://pubmed.ncbi.nlm.nih.gov/31201556/)). The physiological necessity of this circuit is proven by human genetics: "two pairs of siblings with homozygous FXR truncation or deletion variants were identified. All four children suffered from severe, early-onset PFIC [progressive familial intrahepatic cholestasis] and liver failure" ([PMID: 31201556](https://pubmed.ncbi.nlm.nih.gov/31201556/)). Loss of FXR is therefore not compensated — it causes catastrophic cholestatic liver failure. The complementary FGF19 arm is further detailed in Di Ciaula et al. (2022), who describe how circulating FGF19 binding FGFR4/β-Klotho "causes smooth muscle relaxation and refilling of the gallbladder" and activates the hepatic FXR–SHP pathway ([PMID: 36500979](https://pubmed.ncbi.nlm.nih.gov/36500979/)).

### 6. FXR directly activates the bile salt export pump (BSEP/ABCB11)

Beyond feedback repression of synthesis, FXR directly drives bile-acid *efflux*. Ananthanarayanan et al. (2004) established BSEP — "the bile salt export pump (BSEP), a well established FXR target gene that functions as an ATP-dependent canalicular bile acid transporter" — as a direct FXR target. Ligand (CDCA)-dependent FXR activation increases FXR and CARM1 occupancy at the human BSEP locus, depositing activating histone marks (H3R17 methylation, H3K9 acetylation) at the FXR DNA-binding element. Crucially, the coactivator CARM1 "led to increased BSEP promoter activity with an intact FXR regulatory element, whereas CARM1 failed to transactivate the BSEP promoter with a mutated FXRE" ([PMID: 15471871](https://pubmed.ncbi.nlm.nih.gov/15471871/)). This confirms FXR acts through an authentic FXRE and recruits coactivators to switch on the pump that exports bile acids into the canaliculus — the committed step of hepatic bile secretion.

### 7. FXR extends bile-acid signaling to lipid and glucose metabolism

Through its SHP effector arm, FXR couples bile-acid status to intermediary metabolism. Bile-acid-activated FXR induces SHP, which represses the lipogenic master regulator **SREBP-1c** (and its downstream targets FAS, ACC1, SCD1), suppresses **microsomal triglyceride transfer protein (MTP)** to lower VLDL/triglyceride output, and represses the gluconeogenic genes **PEPCK and G6Pase** (reviewed in Smelt, 2010). The review states that "SHP (small heterodimer partner) and FXR are the link between BAs and TG metabolism" and that "FXR activation by BAs suppresses the expression of MTP" ([PMID: 20699090](https://pubmed.ncbi.nlm.nih.gov/20699090/)). FXR can also act *directly* on lipogenesis — it binds an IR-1 in the fatty acid synthase (FAS) promoter ([PMID: 16957179](https://pubmed.ncbi.nlm.nih.gov/16957179/)), showing both indirect (SHP) and direct routes to lipid control. These metabolic effects are a mechanistic extension of FXR's bile-acid-sensing function rather than an independent role.

### 8. FXR is a nuclear transcription factor, distinct from the membrane receptor TGR5

FXR's site of action is intracellular. It "is a member of the nuclear hormone receptor superfamily of ligand-activated transcription factors" and acts in the nucleus on target-gene promoters. It is explicitly distinguished from the membrane bile-acid receptor: "TGR5 is a membrane-bound BA receptor" ([PMID: 24878541](https://pubmed.ncbi.nlm.nih.gov/24878541/)). Lysine-mutation studies confirmed that disrupting FXR activity does not abolish its nuclear localization — FXR resides in the nucleus regardless ([PMID: 23462506](https://pubmed.ncbi.nlm.nih.gov/23462506/)). In human intestine, FXR mRNA is expressed along the small intestine following the pattern of its target OSTα/β, with highest expression distally ([PMID: 38636096](https://pubmed.ncbi.nlm.nih.gov/38636096/)).

### 9. FXR is expressed as four isoforms with differential tissue distribution

Zhang, Kast-Woelbern & Edwards (2003) identified **four FXR transcripts from a single gene** (FXRα1, α2, β1, β2), differing at the amino terminus and by a four-amino-acid insert in the hinge region adjacent to the DNA-binding domain. "These four transcripts are expressed differentially in liver, intestine, kidney, adrenals, stomach, fat, and heart." The hinge insert functionally tunes DNA binding: "FXRalpha2 and FXRbeta2 bind to FXR response elements with a higher affinity as compared with FXRalpha1 and FXRbeta1, suggesting that the four-amino acid insert may affect FXR function," producing up to 20-fold promoter-specific differences in transactivation ([PMID: 12393883](https://pubmed.ncbi.nlm.nih.gov/12393883/)).

### 10. Chenodeoxycholic acid is the principal endogenous human agonist

Among bile acids, **chenodeoxycholic acid (CDCA)** is the most potent endogenous human FXR agonist. "Bile acids (BAs) are the natural ligands of the FXRs." The first-in-class selective synthetic agonist, **obeticholic acid (OCA)**, is "a 6α-ethyl derivative of the natural human BA chenodeoxycholic acid (CDCA)… ~100-fold more potent than CDCA" ([PMID: 25705637](https://pubmed.ncbi.nlm.nih.gov/25705637/)). OCA validated FXR as a druggable target in clinical trials for primary biliary cholangitis and NAFLD/NASH.

### 11. Intestinal FXR drives an enteroprotective antibacterial program

In the ileum, FXR maintains the gut barrier. Inagaki et al. (2006, *PNAS*) showed that "the farnesoid X receptor (FXR), a nuclear receptor for bile acids, induces genes involved in enteroprotection and inhibits bacterial overgrowth and mucosal injury in ileum caused by bile duct ligation." Loss-of-function evidence confirms causation: "Mice lacking FXR have increased ileal levels of bacteria and a compromised epithelial barrier" ([PMID: 16473946](https://pubmed.ncbi.nlm.nih.gov/16473946/)). FXR agonists prevent epithelial deterioration and bacterial translocation under impaired bile flow.

---

## Mechanistic Model / Interpretation

FXR is best understood as a **single-input, multi-output transcriptional switch** that reads intracellular bile-acid concentration and writes a coordinated program maintaining bile-acid homeostasis. The unifying biochemical activity is ligand-dependent, RXRα-partnered, IR-1-directed transcription.

```
            Bile acids (CDCA most potent)
                        │ bind LBD (Arg anchor, His/AF-2 trigger)
                        ▼
         ┌──────────────────────────────┐
         │   FXR ──heterodimer── RXRα    │  ← nuclear; coactivators (SRC-1,
         │        (binds IR-1 DNA)       │     CARM1) recruited at helix-12/AF-2
         └──────────────────────────────┘
                │                     │
        HEPATOCYTE nucleus      ENTEROCYTE nucleus (ileum)
                │                     │
   ┌────────────┼───────────┐        ├── FGF19 (enterokine) ──► portal blood
   │            │           │        │        │
 ↑SHP        ↑BSEP       ↑detox      │   FGFR4/β-Klotho on hepatocyte
   │         (ABCB11)    transport   │        │
 ⊣CYP7A1   export BA    OSTα/β etc.  │   ⊣ CYP7A1 (synthesis)
 (⊣synthesis) to bile                │   + gallbladder refilling
   │                                 ├── antibacterial/enteroprotective genes
 ⊣SREBP-1c, ⊣MTP, ⊣PEPCK/G6Pase      │   (barrier defense; ⊣bacterial overgrowth)
 (lipid & glucose control)           └── FGF19 feedback
```

**Output summary table:**

| Target / effector | Direction | Physiological consequence | Evidence (PMID) |
|---|---|---|---|
| CYP7A1 (via SHP) | ↓ repress | Reduce bile-acid synthesis (feedback) | 10334992, 31201556 |
| SHP (NR0B2) | ↑ induce | Hepatic repressor arm | 31201556 |
| FGF15/19 | ↑ induce | Gut→liver endocrine feedback; gallbladder refill | 31201556, 36500979 |
| BSEP (ABCB11) | ↑ induce | Canalicular bile-acid export | 15471871 |
| SREBP-1c, FAS, MTP | ↓ repress | Lower lipogenesis / VLDL output | 20699090, 16957179 |
| PEPCK, G6Pase | ↓ repress | Lower gluconeogenesis | 20699090 |
| Enteroprotective/antibacterial genes | ↑ induce | Gut barrier defense | 16473946 |

**Localization:** The functional site is the **nucleus** of hepatocytes and enterocytes (highest), with lower expression in kidney and adrenal gland. This is categorically distinct from TGR5/GPBAR1, the membrane-bound bile-acid GPCR.

**Primary function statement:** FXR is **not an enzyme or transporter** — it is a **signaling molecule (ligand-activated transcription factor)**. Its "substrate" is its ligand (bile acids/CDCA), and its "product" is a transcriptional output. Its role in the pathway is to be the apex **sensor-regulator** of the enterohepatic bile-acid circuit.

---

## Evidence Base

| PMID | Study | Contribution | Strength |
|---|---|---|---|
| [10334992](https://pubmed.ncbi.nlm.nih.gov/10334992/) | Makishima et al. 1999, *Science* | Bile acids = FXR ligands; FXR represses CYP7A1, activates IBABP | Foundational, direct experimental |
| [18391212](https://pubmed.ncbi.nlm.nih.gov/18391212/) | Soisson et al. 2008 | 1.9 Å crystal structure of LBD; Arg anchor, His/AF-2 trigger, binding poses | High (structural) |
| [30275017](https://pubmed.ncbi.nlm.nih.gov/30275017/) | Wang et al. 2018 | FXR/RXRα heterodimer structure; enhanced SRC-1 binding | High (structural) |
| [16957179](https://pubmed.ncbi.nlm.nih.gov/16957179/) | Matsukuma et al. 2006 | IR-1 is the FXR/RXR response element; direct FAS promoter binding | High |
| [12761213](https://pubmed.ncbi.nlm.nih.gov/12761213/) | Human kininogen 2003 | Direct, specific FXR/RXRα binding to IR-1 | High |
| [17655523](https://pubmed.ncbi.nlm.nih.gov/17655523/) | Fetuin-B 2007 | IR-1 mutation abolishes binding & transactivation | High |
| [31201556](https://pubmed.ncbi.nlm.nih.gov/31201556/) | Keitel et al. 2019 review | SHP + FGF15/19 arms; human PFIC loss-of-function | High (review + human genetics) |
| [15471871](https://pubmed.ncbi.nlm.nih.gov/15471871/) | Ananthanarayanan et al. 2004 | BSEP is direct FXR target via FXRE + CARM1 | High |
| [20699090](https://pubmed.ncbi.nlm.nih.gov/20699090/) | Smelt 2010 review | FXR-SHP link to triglyceride/lipid metabolism; MTP suppression | Medium (review) |
| [24878541](https://pubmed.ncbi.nlm.nih.gov/24878541/) | Fan et al. 2015 | FXR = nuclear TF, distinct from membrane TGR5 | High |
| [23462506](https://pubmed.ncbi.nlm.nih.gov/23462506/) | Sun et al. 2013 | Nuclear localization retained despite activity mutations | Medium |
| [12393883](https://pubmed.ncbi.nlm.nih.gov/12393883/) | Zhang et al. 2003 | Four isoforms, tissue distribution, hinge insert tunes DNA binding | High |
| [25705637](https://pubmed.ncbi.nlm.nih.gov/25705637/) | Ali et al. 2015 review | CDCA = natural human ligand; OCA ~100× more potent | High |
| [16473946](https://pubmed.ncbi.nlm.nih.gov/16473946/) | Inagaki et al. 2006, *PNAS* | Intestinal FXR antibacterial/barrier program; FXR-null phenotype | High |
| [38636096](https://pubmed.ncbi.nlm.nih.gov/38636096/) | Nerild et al. 2025 | Human intestinal FXR expression gradient | Medium (expression) |
| [36500979](https://pubmed.ncbi.nlm.nih.gov/36500979/) | Di Ciaula et al. 2022 review | FXR-FGF19 axis; gallbladder refilling | Medium (review) |

The evidence base is unusually strong and convergent: direct ligand-binding/activation experiments, multiple independent crystal structures, promoter-level ChIP and mutagenesis defining the IR-1 element, coactivator-recruitment assays, genetic loss-of-function in both mouse and human, and pharmacological validation with a clinically advanced agonist. No major conflicting evidence was encountered regarding FXR's core identity or function.

---

## Limitations and Knowledge Gaps

1. **Isoform-specific physiology.** Four FXR isoforms exist with differential DNA-binding and tissue distribution ([PMID: 12393883](https://pubmed.ncbi.nlm.nih.gov/12393883/)), but the distinct *in vivo* physiological roles of each isoform remain incompletely mapped.
2. **Species differences.** Some target genes (e.g., human fetuin-B) are FXR-responsive in human but not mouse hepatocytes ([PMID: 17655523](https://pubmed.ncbi.nlm.nih.gov/17655523/)), and FGF15 (mouse)/FGF19 (human) are orthologs with potential functional differences — caution is needed when extrapolating rodent data to humans.
3. **Non-canonical DNA binding.** Evidence indicates FXR can bind DNA independently of RXRα and regulate SHP through a non-IR-1 (LRH-1-binding) site; the physiological weight of these non-canonical modes versus the dominant RXRα/IR-1 mechanism is not fully resolved.
4. **Post-translational regulation.** FXR is modulated by SUMOylation and lysine methylation (Set7/9), which tune target-gene selection, but the integrated regulatory logic under physiological and disease states is still being defined.
5. **This report is literature-derived.** No primary experimental dataset was analyzed; conclusions rest on published studies and database annotations, prioritizing primary and structural evidence.

---

## Proposed Follow-up Experiments / Actions

1. **Genome-wide human FXR cistrome mapping.** Perform ChIP-seq / CUT&RUN for FXR and RXRα in primary human hepatocytes and enterocytes ± CDCA/OCA to define the full set of direct IR-1 targets and quantify the contribution of non-canonical (RXR-independent) sites.
2. **Isoform knock-in models.** Generate isoform-selective human hepatocyte/organoid lines (α1/α2/β1/β2) to dissect isoform-specific target-gene programs predicted by the hinge-insert DNA-binding differences.
3. **Structure-guided ligand panel.** Use the LBD crystallographic framework (Arg anchor, His/AF-2 trigger) to screen endogenous bile-acid species for agonist/antagonist potency, refining the human ligand-specificity hierarchy beyond CDCA.
4. **Spatial validation of localization.** Quantitative imaging / single-nucleus RNA-seq across human liver and intestinal segments to confirm the nuclear site of action and the enterocyte expression gradient relative to OSTα/β.
5. **Therapeutic translation.** Continue evaluating FXR agonists (and non-canonical binding modes) in cholestatic (PBC, PFIC) and metabolic (NASH) disease, correlating target-gene induction (SHP, BSEP, FGF19) with clinical response.

---

*Report generated from a 5-iteration autonomous investigation; 11 confirmed findings, 53 papers reviewed. Gene identity (NR1H4 = FXR, Q96RI1, Homo sapiens) verified against UniProt and primary literature with no ambiguity.*


## Artifacts

- [OpenScientist final report](NR1H4-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](NR1H4-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:10334992
2. PMID:30275017
3. PMID:18391212
4. PMID:16957179
5. PMID:12761213
6. PMID:17655523
7. PMID:31201556
8. PMID:36500979
9. PMID:15471871
10. PMID:20699090
11. PMID:24878541
12. PMID:23462506
13. PMID:38636096
14. PMID:12393883
15. PMID:25705637
16. PMID:16473946