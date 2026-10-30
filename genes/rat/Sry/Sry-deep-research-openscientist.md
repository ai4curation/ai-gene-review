---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-24T04:14:57.235382'
end_time: '2026-10-24T06:01:41.565265'
duration_seconds: 6404.33
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: rat
  gene_id: Sry
  gene_symbol: Sry
  uniprot_accession: P36394
  protein_description: 'RecName: Full=Sex-determining region Y protein; AltName: Full=Testis-determining
    factor;'
  gene_info: Name=Sry; Synonyms=Tdf;
  organism_full: Rattus norvegicus (Rat).
  protein_family: Belongs to the SRY family. .
  protein_domains: HMG_box_dom. (IPR009071); HMG_box_dom_sf. (IPR036910); SRY-related_HMG-box_TF-like.
    (IPR050140); HMG_box (PF00505)
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
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Sry-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Sry-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** P36394
- **Protein Description:** RecName: Full=Sex-determining region Y protein; AltName: Full=Testis-determining factor;
- **Gene Information:** Name=Sry; Synonyms=Tdf;
- **Organism (full):** Rattus norvegicus (Rat).
- **Protein Family:** Belongs to the SRY family. .
- **Key Domains:** HMG_box_dom. (IPR009071); HMG_box_dom_sf. (IPR036910); SRY-related_HMG-box_TF-like. (IPR050140); HMG_box (PF00505)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Sry" matches the protein description above**
2. **Verify the organism is correct:** Rattus norvegicus (Rat).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Sry' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Sry** (gene ID: Sry, UniProt: P36394) in rat.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: Sry (Sex-determining region Y protein / Testis-determining factor) — *Rattus norvegicus*

**UniProt:** P36394 | **Gene:** Sry (synonym Tdf) | **Organism:** *Rattus norvegicus* (rat)
**Family:** SRY family | **Domain:** HMG box (PF00505; IPR009071, IPR036910; SRY-related HMG-box TF-like IPR050140)
**Report date:** 2026-10-24

---

## 1. Identity verification

The target is correctly identified. The gene symbol **Sry**, the description "Sex-determining region Y protein / Testis-determining factor", the organism (rat), and the HMG-box domain architecture are mutually consistent and match the canonical mammalian **SRY** sex-determining transcription factor. SRY is the founding member of the SOX ("SRY-related HMG box") family and is encoded on the Y chromosome. There is **no symbol ambiguity**: "Sry" unambiguously denotes this gene across mammals.

One rat-specific caveat is important for interpreting the literature. Unlike mouse and human, the laboratory rat carries **multiple Sry gene copies** on the Y chromosome (e.g., Sry1, Sry2, Sry3C, Sry4A…), encoding slightly different protein variants [PMID 32398044]. P36394 corresponds to one rat SRY protein; some functional experiments in rat use a specific copy (commonly "Sry1"). Claims below are drawn from rat primary studies where available, supplemented by closely related mouse/human SRY mechanism where the rat protein has not been assayed directly (clearly flagged).

---

## 2. Summary (answer to the research question)

Rat Sry is a **Y-chromosome–encoded, nuclear, sequence-specific DNA-binding transcription factor** of the HMG-box class. Its single defining biochemical activity is to **bind the minor groove of specific DNA target sites and sharply bend the DNA** (an "architectural" transcription factor); it has no enzymatic or transporter activity. Its **primary biological function** is to act as the master trigger of male sex determination: a transient embryonic pulse of Sry in pre-Sertoli cells of the bipotential gonad, acting together with the nuclear receptor **SF1/NR5A1**, activates the testis-specific enhancer of **Sox9**, switching on the SOX9 gene-regulatory network that commits the gonad to testis (Sertoli-cell) fate. In the rat, Sry additionally has well-documented **extragonadal functions** in catecholaminergic and renal tissue: it up-regulates transcription of **tyrosine hydroxylase** (the rate-limiting catecholamine-biosynthetic enzyme) and shifts the **renin–angiotensin system** toward its pressor (ACE/ANG II) axis, thereby raising catecholamine output, sympathetic tone, and blood pressure. Different rat Sry paralogs are **not functionally equivalent** (graded potency Sry3 > Sry1 > Sry2). Sry carries out all of these functions in the **nucleus**, to which it is targeted by two nuclear localization signals within its HMG box.

---

## 3. Primary molecular function

### 3.1 Architectural, sequence-specific DNA-binding transcription factor (HMG box)
SRY's only structured, conserved module is the ~79-residue **HMG box**, which is the sole region conserved among mammalian orthologs and the site of almost all clinically observed sex-reversal mutations [PMID 25258310]. The HMG box "mediates sequence-specific DNA binding with sharp DNA bending" [PMID 36568077] and is "essential for DNA binding and activity" [PMID 39788310]. SRY therefore acts not as an enzyme but as an **architectural transcription factor**: it recognizes an A/T-rich consensus (WAACAAT-type) in the **minor groove**, intercalates hydrophobic residues, and sharply bends the duplex (measured values ~54–85° depending on the method and construct; see §3.1b), remodeling enhancer geometry so that other factors can assemble a productive transcription complex [PMID 25258310, PMID 11563911].

- **Substrate/target specificity:** double-stranded DNA bearing SOX/SRY HMG-box recognition elements (A/T-rich WAACAAT-type motif); the functional readout is the degree of specific occupancy and induced bend angle. Mutations that preserve DNA affinity/bend but destabilize the domain still cause disease, underscoring that correct folding and stability (not just contact chemistry) govern activity [PMID 27576690, PMID 25258310].
- **No catalytic activity:** SRY is not an enzyme and not a transporter; "function" here means transcriptional regulation through DNA binding/bending.

### 3.1b Quantitative DNA-bending mechanism (structural evidence)
High-resolution NMR of the human SRY HMG-box–DNA complex shows the box binds within an **expanded minor groove** and bends the duplex by **54 ± 2°**, with bulky "cantilever" side chains (Met/Ile) partially intercalating between base pairs [PMID 11563911, PMID 16813837]. This bend is **functionally critical**: the clinical sex-reversal mutation M9I reduces bending to **41 ± 2°**, causing 46,XY sex reversal despite retained binding [PMID 11563911]. The C-terminal **basic tail** flanking the box is bifunctional — it serves as a **nuclear localization signal and accessory DNA-binding element**, and acts as a **"kinetic clamp"** that slows dissociation of the bent complex ~20-fold [PMID 16504207]. Transgenic XX mice are masculinized by either human or mouse Sry despite different bend geometries, indicating male gene regulation requires **DNA bending above a critical threshold** for enhanceosome assembly rather than a precise angle [PMID 15170344]. Thus the mechanistic model is: minor-groove binding → side-chain intercalation → threshold DNA bend → nucleation of an enhanceosome at target enhancers (e.g., Sox9 TESCO).

### 3.2 Position in the sex-determination pathway: Sry → (SF1) → Sox9
In the embryonic XY gonadal ridge, **SRY + SF1 (NR5A1) co-bind the testis-specific enhancer of Sox9** (TESCO / enhancer Enh13) to activate **Sox9** transcription; SRY also up-regulates **ER71**, which independently activates Sox9 [PMID 27611740, PMID 40467489, PMID 38246151]. Once Sox9 crosses a threshold it sustains its own expression and drives Sertoli-cell differentiation and downstream genes such as **AMH** (with SF1). Thus Sry sits at the **apex of the testis-determining transcriptional cascade**, acting transiently and upstream; the durable phenotype is executed by SOX9. This is the core "signaling/regulatory" role requested: Sry is the switch, SF1 the obligatory partner, Sox9 the primary direct target, and Sertoli-cell specification the pathway output.

### 3.2b Sry as a "master switch": upstream regulation and downstream network
Authoritative reviews establish Sry as **"the Y-linked master switch that is both required and sufficient to drive the testis-determining pathway,"** acting immediately upstream of Sox9 [PMID 25246082]. Its action is **transient and initiating, not maintenance**: a pulse of Sry in pre-Sertoli cells tips a bistable switch. 
- **Upstream of Sry:** WT1(+KTS), SF1/NR5A1 and GATA4 promote Sry expression. In Wt1(+KTS)-null XY gonads, SRY protein per cell and the number of SRY⁺ cells fall, SOX9 and Fgf9 are lost, and Sertoli differentiation fails (rescued by FGF9) [PMID 19549635].
- **Downstream of Sry:** the core **testis SRY–SOX9–FGF9** network forms a feed-forward loop that commits Sertoli cells, while simultaneously **antagonizing the ovarian RSPO1–WNT4–CTNNB1–FOXL2** network [PMID 24643063, PMID 25246082]. SOX9 then drives AMH and sustains itself after Sry switches off.

This defines Sry's precise role as the **initiating transcriptional input** of the male gene-regulatory network, exerting its effect through a single key target (Sox9) at a narrow developmental window.

### 3.3 Rat-specific gene multiplicity
RNA-seq across rat gonad development (E11–E14) shows **multiple Sry copies expressed at E12–E13**, with Sry4A, Sry1, and Sry3C conserved across sequenced *R. norvegicus* strains [PMID 32398044]. Different copies "encode amino acid variations that influence the resulting protein function" [PMID 32398044]. This means rat testis determination is driven by a **family of Sry paralogs**, a distinctive feature relevant to any functional study of P36394.

---

### 3.4 Evolutionary origin (inference from evolution)
Sry is a young, rapidly evolving mammalian gene that **originated from the ancestral SOX3 gene** and retained only the HMG-box DNA-binding domain as its conserved functional core [PMID 41138755]. As a master sex-determining gene it evolves under **unusually relaxed selective constraint** outside the HMG box [PMID 41138755], which explains (i) why the HMG box is the sole strongly conserved, function-defining module; (ii) the rat lineage's tolerance for Sry copy amplification and sequence divergence; and (iii) the overlapping target repertoire of Sry and its X-linked homolog SOX3 (e.g., on RAS promoters) [PMID 25759379]. Cross-species transgenic rescue (human or mouse Sry masculinizes XX mice) despite extensive non-HMG divergence is consistent with this evolutionary plasticity [PMID 15170344].

## 4. Subcellular localization

SRY functions in the **cell nucleus**. Its HMG box contains **two nuclear localization signals (NLSs)**, one at each terminus, which operate independently and by distinct import routes: the **N-terminal NLS binds calmodulin (CaM)**, while the **C-terminal NLS binds importin-β** [PMID 11990798, PMID 15746192]. Pharmacological CaM antagonism reduces SRY nuclear entry, and NLS mutations found in XY sex-reversal patients impair nuclear import — demonstrating that correct nuclear targeting is a functional prerequisite [PMID 15746192]. The HMG box is therefore a **bifunctional module** combining DNA binding and nuclear targeting. Functionally, Sry acts in the nuclei of (i) **pre-Sertoli cells** of the embryonic gonad (sex determination) and (ii) **catecholaminergic cells** (adrenal medulla; midbrain dopamine neurons) in its extragonadal role.

---

## 5. Extragonadal / biochemical-pathway function in the rat (catecholamine biosynthesis & blood pressure)

A substantial rat literature establishes a second, pathway-specific role for Sry outside the gonad:

- **Male-specific expression in catecholaminergic tissue:** "Sry was found to be expressed in catecholaminergic regions, in male but not female rats" [PMID 15464265].
- **Direct transcriptional regulation of tyrosine hydroxylase (TH):** Co-transfection of Sry with a TH-promoter luciferase reporter in PC12 cells raises reporter activity; **mutating the AP1 site in the TH promoter greatly reduces induction by Sry**, mapping the principal regulatory motif [PMID 15464265]. TH is the rate-limiting enzyme of catecholamine (dopamine/norepinephrine/epinephrine) biosynthesis.
- **In vivo physiological consequence:** Delivering a Sry1 expression construct into the adrenal medulla of normotensive WKY rats increased **adrenal TH content (+49%)**, **resting plasma norepinephrine (+57%)**, and **blood pressure (~+30 mmHg)** over 2–3 weeks [PMID 17324261]. Sry is a leading candidate for the **SHR Y-chromosome hypertension locus** [PMID 17324261].
- **Conservation:** In humans, SRY localizes to substantia nigra/VTA dopamine neurons and positively regulates TH, DDC, DBH, and MAO-A, increasing extracellular dopamine [PMID 22568433], indicating the catecholamine-regulatory role is evolutionarily conserved and not a rat artefact.

Mechanistically this places Sry as a **male-specific transcriptional input to the catecholamine biosynthetic pathway**, providing a direct molecular link from the Y chromosome to sympathetic nervous system activity and blood-pressure regulation.

### 5.1 Second extragonadal axis: the renin–angiotensin system (RAS)
Rat Sry also regulates the RAS. In promoter–luciferase assays, **Sry1/Sry2/Sry3 up-regulate the angiotensinogen, renin, and ACE promoters and down-regulate the ACE2 promoter** — i.e., they shift the balance toward the vasoconstrictor/pressor ACE→ANG II axis and away from the vasodilator ACE2→ANG-(1-7)→MAS axis [PMID 19809364]. The effect is **copy-specific and graded (Sry3 > Sry1 > Sry2)**; Sry3 raised the ACE promoter 2.6-fold and the angiotensinogen promoter 1.7-fold while lowering ACE2 to ~0.5-fold [PMID 19809364]. Rat **Sry transcripts are present in all male tissues examined, including the kidney** (the primary site of renin production) [PMID 25759379], and **in vivo delivery of Sry1 (but not Sry2) to the kidney** raised renal TH (+41%), plasma norepinephrine (+27%), and blood pressure [PMID 19500370]. The SHR Y chromosome, which raises blood pressure ~20–25 mmHg, carries a divergent/additional Sry locus (Sry3), providing a candidate molecular basis for the Y-linked hypertension effect [PMID 19809364, PMID 10829096].

**Copy-specific functional note:** these data show the rat Sry paralogs are **not functionally equivalent** — they differ in transactivation potency and in which physiological targets they engage, reinforcing that conclusions about "rat Sry" (including P36394) should specify the copy where possible.

---

## 6. Supporting evidence by type

| Evidence type | Finding | Example |
|---|---|---|
| Structure / biophysics | HMG box = specific DNA binding + sharp bending; stability governs activity | NMR/crystallography, FRET [PMID 25258310, PMID 36568077] |
| Evolution / bioinformatics | HMG box uniquely conserved; rat has multiple Sry copies with functional variants | comparative sequence analysis [PMID 41138755, PMID 32398044] |
| Cell-based transactivation | SRY+SF1 activate Sox9 TESCO/Enh13; SRY activates TH promoter | reporter assays [PMID 27611740, PMID 38246151, PMID 15464265] |
| In vivo functional | Adrenal Sry delivery raises TH, catecholamines, BP; HMG knockout causes male→female sex reversal | electroporation in rat [PMID 17324261]; CRISPR in pig [PMID 33443157] |
| Clinical genetics | HMG-box and NLS mutations cause XY gonadal dysgenesis via lost DNA binding, destabilization, or defective nuclear import | human DSD variants [PMID 39788310, PMID 15746192] |

---

## 7. Supported and refuted hypotheses

**Supported:**
- H1 — Sry's primary function is sequence-specific DNA binding/bending (architectural TF), not catalysis. **Supported** (structure, mutation data).
- H2 — Sry initiates testis determination by activating Sox9 with SF1 at a testis-specific enhancer. **Supported** (transactivation, cross-species).
- H3 — Sry is a nuclear protein with HMG-box NLSs (CaM and importin-β dependent). **Supported**.
- H4 — In the rat, Sry additionally regulates catecholamine biosynthesis (TH) and blood pressure. **Supported** (in vitro + in vivo rat data).
- H5 — The rat uses multiple functional Sry copies. **Supported**.

**Refuted / not supported:**
- "The HMG box is the only functional domain" is **refuted** for rodents: the rodent-specific C-terminal glutamine-rich (CAG-microsatellite) tract is essential in mouse for protein stability and transactivation and acts as a "genetic capacitor" [PMID 25074915, PMID 23901118]. (Note: this is best characterized in mouse; the rat P36394 variant's non-HMG regions warrant direct study.)
- "Sry acts as an enzyme/transporter" — **refuted**; no catalytic or transport activity.

---

## 8. Limitations and future directions

- **Copy-specific attribution:** Because the rat has multiple Sry paralogs, assigning every reported activity specifically to P36394 is imperfect; copy-resolved functional assays are needed.
- **Direct rat structural data:** Most HMG-box structural/biophysical work is on human/mouse/SOX orthologs; a rat-specific structure (e.g., AlphaFold model of P36394) could confirm DNA-contact and NLS residues.
- **Non-HMG regions in rat:** The role of rat-specific C-terminal regions (analogous to the mouse polyQ capacitor) in stability/transactivation is not fully characterized.
- **Extragonadal scope:** The breadth of adult rat tissues where Sry is transcriptionally active (brain, heart, kidney, adrenal) and its complete target-gene set remain incompletely mapped.

---

## 9. Key references
- PMID 32398044 — Multiple rat Sry genes expressed at onset of testis differentiation (Rattus norvegicus).
- PMID 27611740 — SRY+SF1 activate Sox9 via TESCO; SRY→ER71→Sox9.
- PMID 40467489 / 38246151 — SRY/NR5A1 regulation of Sox9 via testis-specific enhancer.
- PMID 15464265 — Sry regulates tyrosine hydroxylase transcription (AP1 site) in rat catecholaminergic cells.
- PMID 17324261 — Adrenal Sry delivery raises TH, catecholamines, and blood pressure in rats.
- PMID 22568433 — SRY regulates catecholamine synthesis/metabolism in human midbrain dopamine neurons.
- PMID 11990798 / 15746192 — SRY HMG-box dual NLS; calmodulin- and importin-β-dependent nuclear import.
- PMID 25258310 / 36568077 / 39788310 — HMG box as architectural, sequence-specific DNA-binding/bending domain.
- PMID 25074915 / 23901118 — Rodent-specific C-terminal glutamine tract: stability and "genetic capacitor" function.
- PMID 33443157 — HMG-box knockout causes XY→female sex reversal (pig), confirming the HMG box's central role.
- PMID 11563911 — NMR structure: SRY bends DNA ~54°; sex-reversal mutation M9I reduces the bend to 41°.
- PMID 16504207 — SRY basic tail is a dual NLS/accessory-DNA element and "kinetic clamp".
- PMID 15170344 — Sry-directed sex reversal is robust to bend angle above a threshold (transgenic mice).
- PMID 25246082 — Review: Sry is the required-and-sufficient master switch acting immediately upstream of Sox9.
- PMID 24643063 — Review: antagonistic SRY–SOX9–FGF9 (testis) vs RSPO1–WNT4–CTNNB1–FOXL2 (ovary) networks.
- PMID 19549635 — WT1(+KTS) cell-autonomously regulates Sry; links Sry to Sertoli differentiation via FGF9.
- PMID 19809364 — Rat Sry1/2/3 differentially regulate renin–angiotensin system promoters (Sry3 strongest).
- PMID 25759379 — SRY (and SOX3) regulate RAS promoters; Sry expressed in kidney and all male rat tissues.
- PMID 19500370 — Kidney delivery of Sry1 (not Sry2) raises renal TH, norepinephrine, and blood pressure.
- PMID 10829096 — Review: SHR Y-chromosome locus raises blood pressure ~20–25 mmHg; Sry a candidate.
- PMID 41138755 — Sry originated from Sox3 and evolves under relaxed constraint (HMG box conserved).


## Artifacts

- [OpenScientist final report](Sry-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Sry-deep-research-openscientist_artifacts/final_report.pdf)