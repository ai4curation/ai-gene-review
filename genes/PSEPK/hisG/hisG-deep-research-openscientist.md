---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-17T04:40:47.248445'
end_time: '2026-07-17T05:32:06.516986'
duration_seconds: 3079.27
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: hisG
  gene_symbol: hisG
  uniprot_accession: Q88P87
  protein_description: 'RecName: Full=ATP phosphoribosyltransferase {ECO:0000255|HAMAP-Rule:MF_01018};
    Short=ATP-PRT {ECO:0000255|HAMAP-Rule:MF_01018}; Short=ATP-PRTase {ECO:0000255|HAMAP-Rule:MF_01018};
    EC=2.4.2.17 {ECO:0000255|HAMAP-Rule:MF_01018};'
  gene_info: Name=hisG {ECO:0000255|HAMAP-Rule:MF_01018}; OrderedLocusNames=PP_0965;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the ATP phosphoribosyltransferase family. Short
  protein_domains: ATP_PRibTrfase_cat. (IPR013820); ATP_PRibTrfase_CS. (IPR018198);
    ATP_PRibTrfase_HisG. (IPR001348); ATP_PRibTrfase_HisG_short. (IPR024893); HisG
    (PF01634)
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
citation_count: 9
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: hisG-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: hisG-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88P87
- **Protein Description:** RecName: Full=ATP phosphoribosyltransferase {ECO:0000255|HAMAP-Rule:MF_01018}; Short=ATP-PRT {ECO:0000255|HAMAP-Rule:MF_01018}; Short=ATP-PRTase {ECO:0000255|HAMAP-Rule:MF_01018}; EC=2.4.2.17 {ECO:0000255|HAMAP-Rule:MF_01018};
- **Gene Information:** Name=hisG {ECO:0000255|HAMAP-Rule:MF_01018}; OrderedLocusNames=PP_0965;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the ATP phosphoribosyltransferase family. Short
- **Key Domains:** ATP_PRibTrfase_cat. (IPR013820); ATP_PRibTrfase_CS. (IPR018198); ATP_PRibTrfase_HisG. (IPR001348); ATP_PRibTrfase_HisG_short. (IPR024893); HisG (PF01634)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "hisG" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'hisG' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **hisG** (gene ID: hisG, UniProt: Q88P87) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *hisG* (ATP Phosphoribosyltransferase, Q88P87) in *Pseudomonas putida* KT2440

## Summary

**hisG** (UniProt **Q88P87**; ordered locus **PP_0965**) of *Pseudomonas putida* KT2440 encodes the catalytic subunit of **ATP phosphoribosyltransferase (ATP-PRT, EC 2.4.2.17)**, the enzyme that carries out the **first and committed step of de novo L-histidine biosynthesis**. The reaction is a Mg²⁺-dependent, phosphoribosyltransferase-class condensation of **ATP** with **5-phospho-α-D-ribose-1-diphosphate (PRPP)** to yield **N′-(5′-phosphoribosyl)-ATP (PR-ATP)** and inorganic **pyrophosphate**, forming a new N1-glycosidic bond between the adenine ring of ATP and the C1′ of the phosphoribosyl moiety (Rhea 18473). This is step 1 of the 9-step histidine pathway, and because it consumes both ATP and PRPP — high-value metabolic currency shared with nucleotide biosynthesis — it is the principal flux-control point of the pathway.

Q88P87 is a **short-form HisG**: it comprises only the catalytic core (211 amino acids) and **lacks the C-terminal regulatory domain** found in long-form ATP-PRTs. That missing regulatory function is supplied *in trans* by a separate protein, **HisZ** — a catalytically dead histidyl-tRNA synthetase paralogue encoded at a distant locus (PP_4890, Q88DD7). Together HisG and HisZ assemble into a **hetero-octamer of four HisG catalytic chains plus four HisZ regulatory chains**. HisZ binding allosterically **enhances catalysis** and confers **feedback inhibition by L-histidine**, the pathway end-product, so that histidine supply is matched to demand. Quantitatively, characterized orthologs show HisZ provides only a **modest ~2–4-fold boost in *k*cat**, and the isolated HisG catalytic subunit is intrinsically active — establishing that HisG carries the catalytic machinery while HisZ acts as a remote allosteric tuner and histidine sensor.

The functional assignment is supported convergently by four independent lines of evidence: (1) UniProt/HAMAP rule-based annotation of the reaction, pathway, and subunit architecture; (2) primary biochemical and structural literature on multiple characterized short- and long-form orthologs; (3) direct sequence analysis showing Q88P87 is **62.7% identical** to the crystallized *Psychrobacter arcticus* HisGS and strictly conserves both catalytic arginines (mapping to **Arg10** and **Arg34**) that stabilize the pyrophosphate leaving group; and (4) a **very high-confidence AlphaFold model (mean pLDDT 96)** confirming a well-ordered single catalytic-domain fold with confidently placed active-site residues. The gene product functions in the **cytoplasm** and sits in a histidine-biosynthesis gene cluster adjacent to *hisD* (PP_0966).

---

## Identity Verification

| Field | Value | Status |
|---|---|---|
| UniProt accession | Q88P87 | ✓ |
| Gene symbol | *hisG* | ✓ matches ATP-PRT annotation |
| Ordered locus | PP_0965 | ✓ |
| Organism | *Pseudomonas putida* KT2440 (ATCC 47054 / DSM 6125 / NCIMB 11950) | ✓ |
| Protein | ATP phosphoribosyltransferase, EC 2.4.2.17 | ✓ |
| Family | ATP-PRT family, Short subfamily (IPR024893) | ✓ |
| Domains | PF01634 (HisG); IPR001348, IPR013820, IPR018198 | ✓ |
| Length | 211 aa (catalytic core only) | ✓ consistent with short-form |

The gene symbol *hisG*, the organism, the protein family, and the diagnostic domains all align consistently. No conflicting literature for a differently-functioning gene of the same symbol was encountered. **The identity is confidently verified**, and this report proceeds with research on the correct target.

---

## Key Findings

### F001 — Q88P87 is the catalytic subunit of ATP phosphoribosyltransferase, catalyzing step 1 of histidine biosynthesis

Q88P87 is annotated with **EC 2.4.2.17** and the reaction (Rhea 18473): 1-(5-phospho-β-D-ribosyl)-ATP + diphosphate ⇌ PRPP + ATP. In the biosynthetic (forward) direction, the enzyme condenses **ATP + PRPP → N′-(5′-phosphoribosyl)-ATP (PR-ATP)**. The pathway annotation places this as **step 1 of 9** in L-histidine biosynthesis. The protein is 211 amino acids and belongs to the ATP phosphoribosyltransferase family, **Short subfamily** (InterPro IPR024893). Functional keywords include Glycosyltransferase, Transferase, ATP-binding, and Nucleotide-binding.

This assignment rests on an authoritative body of literature establishing ATP-PRT/HisG as the pathway-entry enzyme. As stated in [PMID: 29208762](https://pubmed.ncbi.nlm.nih.gov/29208762/): *"Adenosine triphosphate (ATP) phosphoribosyltransferase (ATP-PRT) catalyses the first committed step of histidine biosynthesis in plants and microorganisms."* This is independently confirmed by [PMID: 22989207](https://pubmed.ncbi.nlm.nih.gov/22989207/), which describes the enzyme as one that *"catalyzes the first and committed step in l-histidine biosynthesis."* The convergence of UniProt/HAMAP annotation with primary literature on characterized orthologs makes this the most robustly supported claim of the report.

### F002 — Q88P87 is a SHORT-form HisG lacking the C-terminal regulatory domain; it functions as a HisG/HisZ heteromultimer

The UniProt subunit annotation for Q88P87 states it is a *"Heteromultimer composed of HisG and HisZ subunits,"* and the domain annotation notes it *"Lacks the C-terminal regulatory region which is replaced by HisZ."* The sequence length (211 aa) reflects only the catalytic core, versus ~280–310 aa for long-form HisG that carries a covalently fused regulatory domain. In *P. putida* KT2440 the regulatory partner **HisZ is encoded separately at PP_4890** (Q88DD7, 395 aa, annotated "ATP phosphoribosyltransferase regulatory subunit"), physically distant from *hisG* (PP_0965), which lies adjacent to *hisD* (PP_0966).

This architecture is well established for the short-form enzyme class. [PMID: 29208762](https://pubmed.ncbi.nlm.nih.gov/29208762/) defines it precisely: *"The short-form ATP-PRT is a hetero-octamer, with four HisG chains that comprise only the catalytic domains and four separate chains of HisZ required for allosteric regulation by histidine."* This is corroborated by [PMID: 29940105](https://pubmed.ncbi.nlm.nih.gov/29940105/): *"Short-form ATP phosphoribosyltransferase (ATPPRT) is a hetero-octameric allosteric enzyme comprising four catalytic subunits (HisG…)."* The separation of catalytic and regulatory functions onto two polypeptides is the defining feature distinguishing Q88P87 from long-form enzymes such as those of *Mycobacterium tuberculosis* or *Campylobacter jejuni*.

### F003 — HisG activity is allosterically activated by HisZ and feedback-inhibited by L-histidine

In short-form systems, the isolated HisG catalytic subunit has activity that is markedly enhanced upon complex formation with HisZ, which also confers histidine sensitivity. **L-histidine, the final product of the pathway, binds the HisZ regulatory subunit and allosterically inhibits the HisG:HisZ complex** — classic end-product feedback inhibition. The UniProt function note for Q88P87 states that *"the rate of histidine biosynthesis seems to be controlled primarily by regulation of HisG enzymatic activity."*

The activating role of HisZ is documented in [PMID: 36494361](https://pubmed.ncbi.nlm.nih.gov/36494361/): histidine biosynthesis is *"controlled via a complex allosteric mechanism where the regulatory protein HisZ enhances catalysis by the catalytic protein HisG."* The feedback-inhibition arm is confirmed by [PMID: 31251578](https://pubmed.ncbi.nlm.nih.gov/31251578/): *"ATP phosphoribosyltransferase (ATPPRT) catalyzes the first step of histidine biosynthesis, being allosterically inhibited by the final product of the pathway."* Together, activation and feedback inhibition make HisG the principal rate-controlling valve of histidine flux, poised to throttle back consumption of ATP and PRPP when histidine is abundant.

### F004 — HisG (Q88P87) acts in the cytoplasm as the entry enzyme of the histidine pathway

The UniProt subcellular location for Q88P87 is **Cytoplasm (SL-0086)**. In *P. putida* KT2440, *hisG* (PP_0965) is co-localized in a histidine-biosynthesis gene cluster with *hisD* (histidinol dehydrogenase, PP_0966, P59400), while the regulatory partner *hisZ* is at a separate locus (PP_4890). The histidine biosynthetic pathway is entirely cytosolic and proceeds in nine steps from PRPP, with HisG catalyzing step 1.

The genomic organization is consistent with the classic operon structure. [PMID: 1104579](https://pubmed.ncbi.nlm.nih.gov/1104579/) establishes hisG as *"The first enzyme for histidine biosynthesis, encoded in the hisG gene,"* consistent with its position as the pathway-entry enzyme and its clustering with downstream *his* genes.

### F005 — HisZ is a catalytically repurposed histidyl-tRNA synthetase paralogue; isolated dimeric HisGS retains intrinsic activity

The regulatory partner HisZ (in *P. putida*, PP_4890 / Q88DD7, 395 aa) is structurally a **paralogue of histidyl-tRNA synthetase (HisRS)** that has lost aminoacylation activity and been recruited to regulate HisG — an example of enzyme "moonlighting"/evolutionary repurposing. Importantly, direct biochemical study of the homologous *Lactococcus lactis* short-form enzyme showed the catalytic subunit HisGS is a **dimer** and, contrary to earlier assumptions of strict HisZ dependence, retains **measurable ATP-PRT activity even without HisZ**.

[PMID: 27393206](https://pubmed.ncbi.nlm.nih.gov/27393206/) identifies the partnership: *"Lactococcus lactis possesses the short form ATP-PRT comprising four subunits of HisGS, the catalytic subunit, and four subunits of HisZ, a histidyl-tRNA synthetase paralogue."* The same study demonstrates catalytic autonomy: *"the dimeric HisGS does display ATP-PRT activity in the absence of HisZ."* This informs the interpretation of Q88P87 as an intrinsically catalytic enzyme whose partner HisZ modulates — rather than creates — activity.

### F006 — HisG catalyzes a Mg²⁺-dependent N1-glycosidic condensation of ATP and PRPP, releasing pyrophosphate

Mechanistically, the reaction (Rhea 18473, EC 2.4.2.17) forms an **N-glycosidic bond between N1 of the adenine ring of ATP and C1′ of the 5-phosphoribosyl moiety of PRPP**, with displacement of the pyrophosphate leaving group of PRPP. UniProt classifies HisG with the keyword "Glycosyltransferase," reflecting the phosphoribosyltransferase chemistry. The enzyme is ATP/nucleotide-binding.

[PMID: 28092443](https://pubmed.ncbi.nlm.nih.gov/28092443/) describes the reaction directly: the enzyme *"catalyzes the first step in histidine biosynthesis, the condensation of ATP and 5-phospho-α-d-ribosyl-1-pyrophosphate."* Kinetic dissection in [PMID: 22989207](https://pubmed.ncbi.nlm.nih.gov/22989207/) reveals that *"Pre-steady-state kinetic experiments indicate that chemistry is not rate-limiting for the overall reaction"* — an important mechanistic insight indicating that product release or conformational steps, rather than bond formation itself, govern turnover.

### F007 — Quantitative mechanism: HisZ provides a modest 2–4× *k*cat boost and remotely tunes catalytic arginines that stabilize the pyrophosphate leaving group

The most thoroughly characterized short-form ortholog structurally and kinetically is the cold-adapted ***Psychrobacter arcticus* ATPPRT** — a Gammaproteobacterium, like *P. putida*. Its crystal structure reveals an equimolar **HisGS–HisZ hetero-octamer**, and steady-state kinetics show that **both the holoenzyme and the isolated HisGS are catalytically active**, with HisZ conferring only a **modest 2–4-fold increase in *k*cat** ([PMID: 28092443](https://pubmed.ncbi.nlm.nih.gov/28092443/)). ³¹P-NMR confirmed the same reaction proceeds with or without HisZ.

Mechanistically, HisZ activation was proposed to **position HisGS Arg56 (with Arg32) to stabilize departure of the pyrophosphate leaving group**, even though the HisZ:HisGS interface lies ~20 Å from the active site; molecular dynamics show that HisZ binding constrains HisGS dynamics to preorganize the active-site electrostatics ([PMID: 36494361](https://pubmed.ncbi.nlm.nih.gov/36494361/)). Independently, the *Acinetobacter baumannii* enzyme follows a **rapid-equilibrium random kinetic mechanism with noncompetitive histidine inhibition** ([PMID: 34928596](https://pubmed.ncbi.nlm.nih.gov/34928596/)). Direct quotes: HisZ *"confers only a modest 2-4-fold increase in kcat"* and *"both the ATPPRT holoenzyme and HisGS are catalytically active"* ([PMID: 28092443](https://pubmed.ncbi.nlm.nih.gov/28092443/)); *"Activation by HisZ was proposed to position HisGS Arg56 to stabilise departure of the pyrophosphate leaving group"* ([PMID: 36494361](https://pubmed.ncbi.nlm.nih.gov/36494361/)).

### F008 — Direct sequence evidence: Q88P87 is 62.7% identical to crystallized *P. arcticus* HisGS and conserves both catalytic arginines

A Needleman-Wunsch pairwise alignment (BLOSUM62, gap −8) of *P. putida* HisG Q88P87 (211 aa) against the experimentally crystallized short-form HisGS of *Psychrobacter arcticus* (Q4FQF7, 231 aa — the enzyme of Stroek et al. 2017 and Fisher et al. 2022) gives **131/209 = 62.7% identity** over aligned positions. Critically, the **two catalytic arginines** shown in *P. arcticus* to stabilize departure of the pyrophosphate leaving group (**Arg32 and Arg56**) are **strictly conserved** in Q88P87, mapping to **Arg10 and Arg34** respectively (a consistent ~22-residue N-terminal offset). *P. arcticus* HisZ (Q4FTX3, 387 aa) is the cognate regulatory partner, mirroring *P. putida* HisZ (Q88DD7, PP_4890, 395 aa).

This is the strongest direct, target-specific evidence in the report. The crystallization of the reference is established in [PMID: 28092443](https://pubmed.ncbi.nlm.nih.gov/28092443/): *"The crystal structure of P. arcticus ATPPRT was determined at 2.34…"* The catalytic arginine identity is established in [PMID: 36494361](https://pubmed.ncbi.nlm.nih.gov/36494361/). At 62.7% identity — well above the ~40% threshold for confident functional transfer — and with strict conservation of the two active-site arginines, the homology transfer to Q88P87 is unusually secure.

### F009 — AlphaFold model of Q88P87 is very high confidence (mean pLDDT 96)

The AlphaFold DB model AF-Q88P87-F1 (v6, 211 residues) has a **mean per-residue pLDDT = 96.0** (median 97.2); **94.8% of residues exceed pLDDT 90** (very high confidence), 99.1% exceed 70 (confident), and **0% fall below 50** (no disordered/low-confidence regions). The two inferred catalytic arginines (Arg10, Arg34) are modeled at pLDDT 94.3 and 94.5. Excluding five terminal residues at each end, the core mean pLDDT is 96.3.

This confirms a **well-ordered single catalytic-domain fold** with confidently placed active-site residues — exactly the compact catalytic core expected for a short-form HisG that lacks the C-terminal regulatory domain. The absence of any low-confidence stretch is consistent with the protein being a single, cohesively folded domain rather than a multidomain protein with disordered linkers.

---

## Mechanistic Model / Interpretation

### The reaction and its place in metabolism

```
        de novo L-HISTIDINE BIOSYNTHESIS (9 steps, cytoplasm)

   ATP  +  PRPP
     \     /
      \   /   ┌───────────────────────────┐
       \ /    │  HisG (Q88P87, PP_0965)   │  ← STEP 1, committed step
   ─────X─────│  ATP-PRT, EC 2.4.2.17     │     (this gene product)
       / \    │  short-form catalytic     │
      /   \   │  subunit, Mg²⁺-dependent  │
     /     \  └───────────────────────────┘
   PR-ATP  +  PPi
     │
     ▼  (HisE, HisI, HisA, HisF/HisH, HisB, HisC, HisD ...)
     │
     ▼
  L-HISTIDINE ───────────┐  feedback inhibition
                         │  (binds HisZ)
                         ▼
              ┌──────────────────────┐
              │ regulation loops     │
              │ back onto HisG:HisZ  │
              └──────────────────────┘
```

### The two-subunit short-form architecture

Q88P87 belongs to the **short-form** branch of the ATP-PRT family. Unlike long-form HisG (e.g., *M. tuberculosis*, *C. jejuni*), which fuses the catalytic and regulatory functions into a single ~280–310 aa polypeptide, the short-form separates them:

| Feature | Long-form HisG | Short-form HisG (Q88P87) |
|---|---|---|
| Length | ~280–310 aa | 211 aa (catalytic core only) |
| Regulatory domain | C-terminal, covalently fused | Absent — supplied by separate HisZ |
| Active oligomer | Homo-hexamer | Hetero-octamer (4×HisG + 4×HisZ) |
| Histidine sensing | Between own regulatory domains | On HisZ subunit |
| *P. putida* loci | — | PP_0965 (HisG) + PP_4890 (HisZ) |

The functional assembly is a **hetero-octamer**:

```
      ┌──────┐   ┌──────┐   ┌──────┐   ┌──────┐
      │ HisG │   │ HisG │   │ HisG │   │ HisG │   catalytic subunits
      └──┬───┘   └──┬───┘   └──┬───┘   └──┬───┘   (Q88P87 ×4)
         │          │          │          │
      ~20 Å      ~20 Å      ~20 Å      ~20 Å   (regulatory interface distant
         │          │          │          │        from active site)
      ┌──┴───┐   ┌──┴───┐   ┌──┴───┐   ┌──┴───┐
      │ HisZ │   │ HisZ │   │ HisZ │   │ HisZ │   regulatory subunits
      └──────┘   └──────┘   └──────┘   └──────┘   (Q88DD7 ×4; HisRS paralogue,
                                                    histidine sensor)
```

### The allosteric logic

HisZ, a catalytically dead histidyl-tRNA synthetase paralogue, performs two jobs. (1) It **modestly activates** HisG (~2–4× *k*cat) by constraining the catalytic subunit's dynamics to **preorganize the active-site electrostatics**, positioning the conserved arginines (Arg10/Arg34 in Q88P87) to stabilize the developing negative charge of the pyrophosphate leaving group during catalysis. (2) It serves as the **histidine sensor**: when cytoplasmic histidine accumulates, it binds HisZ and allosterically inhibits the complex, shutting down the pathway's committed step. This design elegantly couples the cell's histidine status (read out through a tRNA-synthetase-like domain that "recognizes" histidine) to the flux valve of histidine biosynthesis. Because chemistry is not rate-limiting, the allosteric mechanism operates on conformational/product-release steps rather than the bond-forming event itself.

The key nuance emerging across iterations is that HisG is **not** an obligately inactive subunit rescued by HisZ. Isolated HisGS is intrinsically catalytic (dimeric in *L. lactis*; active in *P. arcticus*), so Q88P87 carries the full catalytic machinery, and HisZ is best understood as a **remote allosteric tuner and histidine-responsive brake** rather than the source of catalysis.

---

## Evidence Base

| PMID | Title (abbrev.) | Form | How it supports the findings |
|---|---|---|---|
| [29208762](https://pubmed.ncbi.nlm.nih.gov/29208762/) | *A dimeric catalytic core relates the short and long forms of ATP-PRT* | Both | Defines the first-committed-step function and the hetero-octameric short-form architecture (F001, F002) |
| [22989207](https://pubmed.ncbi.nlm.nih.gov/22989207/) | *Mechanism of feedback allosteric inhibition of ATP-PRT* | — | Confirms first/committed step; chemistry not rate-limiting (F001, F006) |
| [29940105](https://pubmed.ncbi.nlm.nih.gov/29940105/) | *Allosteric Activation Shifts the Rate-Limiting Step in a Short-Form ATP-PRT* | Short | Confirms hetero-octameric short-form; HisZ shifts rate-limiting step (F002, F003) |
| [36494361](https://pubmed.ncbi.nlm.nih.gov/36494361/) | *Allosteric rescue links protein dynamics to active-site electrostatic preorganisation* | Short | HisZ enhances catalysis; catalytic Arg positioning of pyrophosphate leaving group (F003, F007, F008) |
| [31251578](https://pubmed.ncbi.nlm.nih.gov/31251578/) | *Mapping the Structural Path for Allosteric Inhibition … by Histidine* | Short | Feedback inhibition by end-product histidine (F003) |
| [1104579](https://pubmed.ncbi.nlm.nih.gov/1104579/) | *trans-Recessive mutation in the first structural gene of the his operon* | — | hisG is the first structural gene/enzyme of the his operon (F004) |
| [27393206](https://pubmed.ncbi.nlm.nih.gov/27393206/) | *Independent catalysis of the short form HisG from L. lactis* | Short | HisZ is a HisRS paralogue; isolated dimeric HisGS is catalytically active (F005) |
| [28092443](https://pubmed.ncbi.nlm.nih.gov/28092443/) | *Kinetics and Structure of a Cold-Adapted Hetero-Octameric ATP-PRT* | Short | Crystal structure & kinetics of *P. arcticus* HisGS; modest 2–4× HisZ boost; homology reference for Q88P87 (F006, F007, F008) |
| [34928596](https://pubmed.ncbi.nlm.nih.gov/34928596/) | *Allosteric Inhibition of [A. baumannii ATPPRT]* | Short | Rapid-equilibrium random mechanism; noncompetitive His inhibition (F007) |
| [25892668](https://pubmed.ncbi.nlm.nih.gov/25892668/) | *C. glutamicum ATP-PRT for L-histidine production* | Long | Feedback via C-terminal regulatory domain (contrast with short-form) |
| [22172596](https://pubmed.ncbi.nlm.nih.gov/22172596/) | *Genetic/biochemical characterization of C. glutamicum HisG mutants* | Long | HisG essential for histidine biosynthesis; His-binding site in C-terminal domain |
| [27191057](https://pubmed.ncbi.nlm.nih.gov/27191057/) | *C. jejuni ATP-PRT is an active hexamer …* | Long | Long-form hexamer contrast; remote His regulation |
| [12511575](https://pubmed.ncbi.nlm.nih.gov/12511575/) | *Crystal structure of ATP-PRT from M. tuberculosis* | Long | Long-form fold; dimer↔hexamer allostery contrast |
| [30072492](https://pubmed.ncbi.nlm.nih.gov/30072492/) | *Guarding the gateway to histidine biosynthesis in plants* | Long | Plant/long-form gateway role; drug-target rationale |
| [42399476](https://pubmed.ncbi.nlm.nih.gov/42399476/) | *Repurposing bleomycin against A. baumannii HisG* | Short | HisG as antibacterial drug target; active-site druggability |

**How the evidence converges on Q88P87 specifically.** The strongest target-specific evidence is F008: the 62.7% sequence identity to the crystallized *P. arcticus* HisGS with strict conservation of both catalytic arginines (Arg10/Arg34). This links Q88P87 directly to an experimentally characterized ortholog in the same bacterial class (Gammaproteobacteria). The AlphaFold model (F009, mean pLDDT 96) provides orthogonal structural confirmation of a single, well-ordered catalytic domain. The remaining findings generalize the well-established short-form ATP-PRT paradigm — validated across *P. arcticus*, *L. lactis*, and *A. baumannii* — to the *P. putida* enzyme, whose UniProt/HAMAP annotation (short subfamily, HisG/HisZ heteromultimer, cytoplasmic, EC 2.4.2.17) is fully consistent with that paradigm.

The literature includes both **short-form** studies (directly relevant to Q88P87) and **long-form** studies (*C. glutamicum*, *C. jejuni*, *M. tuberculosis*, plants). The long-form papers serve as informative contrasts: they show the alternative solution in which the regulatory domain is covalently fused and histidine binds between regulatory domains rather than on a separate HisZ subunit. This distinction is essential for correctly classifying Q88P87 and avoiding misattribution of long-form regulatory mechanisms.

---

## Limitations and Knowledge Gaps

1. **No direct biochemical study of the *P. putida* KT2440 enzyme itself.** All kinetic and structural data cited are from orthologs (*P. arcticus*, *L. lactis*, *A. baumannii*). The functional assignment for Q88P87 is by high-confidence homology transfer and rule-based annotation, not direct experiment. No purified-enzyme *k*cat, *K*m, or crystal structure exists specifically for PP_0965.

2. **HisZ partnership inferred, not demonstrated in *P. putida*.** The pairing of PP_0965 (HisG) with PP_4890 (HisZ) is based on genomic annotation and analogy to characterized short-form systems; direct co-purification or reconstitution of the *P. putida* hetero-octamer has not been reported here.

3. **Catalytic arginine assignment is computational.** Arg10/Arg34 are proposed by sequence alignment to *P. arcticus* Arg32/Arg56 and AlphaFold modeling; their catalytic roles in Q88P87 have not been tested by mutagenesis.

4. **Quantitative regulation parameters unknown for *P. putida*.** The magnitude of HisZ activation and the histidine inhibition constant (*K*i) may differ from the *P. arcticus*/*A. baumannii* values; the exact flux-control coefficient of HisG in *P. putida* central metabolism is not established.

5. **Physiological context in *P. putida* is unexplored here.** *P. putida* is a metabolically versatile soil bacterium of biotechnological interest; how histidine biosynthetic flux is integrated with its broader nitrogen/carbon metabolism and whether HisG activity is transcriptionally co-regulated with the adjacent *hisD* was not investigated.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant expression and kinetic characterization.** Clone and purify *P. putida* HisG (PP_0965) alone and co-expressed with HisZ (PP_4890). Measure steady-state kinetics (*k*cat, *K*m for ATP and PRPP) for the isolated catalytic subunit vs. the reconstituted hetero-octamer to test whether the ~2–4× HisZ activation observed in *P. arcticus* holds. Confirm Mg²⁺ dependence and PPi release (e.g., coupled pyrophosphatase assay or ³¹P-NMR).

2. **Feedback-inhibition assay.** Titrate L-histidine against the reconstituted complex to determine the *K*i and inhibition mode (expected noncompetitive, per *A. baumannii*), verifying that inhibition requires HisZ.

3. **Site-directed mutagenesis of the inferred catalytic arginines.** Mutate Arg10 and Arg34 (individually and together) to Ala/Gln and assay activity loss, experimentally validating their role in stabilizing the pyrophosphate leaving group.

4. **Hetero-octamer reconstitution and structure.** Confirm the 4:4 HisG:HisZ stoichiometry by size-exclusion chromatography/SEC-MALS and, ideally, solve a cryo-EM or crystal structure of the *P. putida* complex to compare with the *P. arcticus* template.

5. **Genetic essentiality and complementation.** Construct a *hisG* deletion in *P. putida* KT2440 and confirm histidine auxotrophy rescued by plasmid-borne *hisG*, establishing in vivo essentiality for histidine prototrophy.

6. **Antibacterial target validation (translational).** Given interest in HisG as an antibacterial target (bleomycin vs. *A. baumannii* HisG; plant/microbial gateway enzyme absent in humans), evaluate whether known ATP-PRT inhibitors bind the *P. putida* active site — useful both for probing the enzyme and for understanding *P. putida* robustness in engineered strains.

---

## Conclusion

*hisG* (Q88P87, PP_0965) in *Pseudomonas putida* KT2440 encodes the **cytoplasmic catalytic subunit of ATP phosphoribosyltransferase (EC 2.4.2.17)**, which catalyzes the **first and committed step of de novo L-histidine biosynthesis** — the Mg²⁺-dependent condensation of ATP with PRPP to give N′-(5′-phosphoribosyl)-ATP plus pyrophosphate. It is a **short-form HisG** that lacks the C-terminal regulatory domain and works as an obligate **HisG₄/HisZ₄ hetero-octamer**, being modestly activated (~2–4× *k*cat) by the histidyl-tRNA-synthetase paralogue **HisZ (PP_4890)** and feedback-inhibited by end-product **L-histidine**, making it the pathway's principal rate-controlling enzyme. The assignment is supported convergently by UniProt/HAMAP annotation, primary literature on characterized orthologs, 62.7% sequence identity to the crystallized *P. arcticus* HisGS with strict conservation of the catalytic arginines (Arg10/Arg34), and a very high-confidence AlphaFold model (mean pLDDT 96).


## Artifacts

- [OpenScientist final report](hisG-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](hisG-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:29208762
2. PMID:22989207
3. PMID:29940105
4. PMID:36494361
5. PMID:31251578
6. PMID:1104579
7. PMID:27393206
8. PMID:28092443
9. PMID:34928596