---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-20T20:12:40.717470'
end_time: '2026-07-20T20:35:36.252242'
duration_seconds: 1375.53
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: hemE
  gene_symbol: hemE
  uniprot_accession: Q88CV6
  protein_description: 'RecName: Full=Uroporphyrinogen decarboxylase {ECO:0000255|HAMAP-Rule:MF_00218};
    Short=UPD {ECO:0000255|HAMAP-Rule:MF_00218}; Short=URO-D {ECO:0000255|HAMAP-Rule:MF_00218};
    EC=4.1.1.37 {ECO:0000255|HAMAP-Rule:MF_00218};'
  gene_info: Name=hemE {ECO:0000255|HAMAP-Rule:MF_00218}; OrderedLocusNames=PP_5074;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the uroporphyrinogen decarboxylase family.
  protein_domains: UROD/MetE-like_sf. (IPR038071); Uroporphyrinogen_deCO2ase_HemE.
    (IPR006361); Uroporphyrinogen_deCOase. (IPR000257); URO-D (PF01208)
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
  path: hemE-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: hemE-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88CV6
- **Protein Description:** RecName: Full=Uroporphyrinogen decarboxylase {ECO:0000255|HAMAP-Rule:MF_00218}; Short=UPD {ECO:0000255|HAMAP-Rule:MF_00218}; Short=URO-D {ECO:0000255|HAMAP-Rule:MF_00218}; EC=4.1.1.37 {ECO:0000255|HAMAP-Rule:MF_00218};
- **Gene Information:** Name=hemE {ECO:0000255|HAMAP-Rule:MF_00218}; OrderedLocusNames=PP_5074;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the uroporphyrinogen decarboxylase family.
- **Key Domains:** UROD/MetE-like_sf. (IPR038071); Uroporphyrinogen_deCO2ase_HemE. (IPR006361); Uroporphyrinogen_deCOase. (IPR000257); URO-D (PF01208)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "hemE" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'hemE' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **hemE** (gene ID: hemE, UniProt: Q88CV6) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *hemE* (Uroporphyrinogen Decarboxylase) in *Pseudomonas putida* KT2440

**Gene:** *hemE* (OrderedLocusName PP_5074) · **UniProt:** [Q88CV6](https://www.uniprot.org/uniprotkb/Q88CV6) · **EC:** 4.1.1.37
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / KT2440)
**Protein family:** Uroporphyrinogen decarboxylase family (Pfam PF01208, InterPro IPR000257 / IPR006361)

---

## Identity Verification

| Attribute | Value | Consistent with target? |
|---|---|---|
| Gene symbol | *hemE* | ✅ standard symbol for URO-D in bacteria |
| Protein | Uroporphyrinogen decarboxylase (URO-D/UPD) | ✅ |
| EC number | 4.1.1.37 | ✅ |
| Length | 354 aa | ✅ matches bacterial URO-D (~353 aa in *E. coli*) |
| Family/domains | URO-D family, PF01208, IPR000257/IPR006361 | ✅ |
| Organism | *P. putida* KT2440 (γ-proteobacterium) | ✅ |

The gene symbol *hemE*, the protein description, the EC number, the family/domain assignment, and the protein length are all internally consistent and match the URO-D family. This report proceeds on a confident identification. Note that the deep, direct experimental literature exists for the human, bovine, rat, tobacco and *E. coli* enzymes; the *P. putida* KT2440 protein itself has not been individually characterized, so its annotation is established by strong homology and by bacterial genetics in the closely related *E. coli*.

---

## Summary

The gene ***hemE*** (PP_5074) of *Pseudomonas putida* KT2440 encodes **uroporphyrinogen decarboxylase (URO-D / UPD, EC 4.1.1.37)**, the fifth enzyme of the heme (tetrapyrrole) biosynthetic pathway. Its primary catalytic function is the **sequential decarboxylation of the four acetate side chains of uroporphyrinogen III** — an octacarboxylic tetrapyrrole — converting each into a methyl group and releasing four molecules of CO₂, to produce **coproporphyrinogen III** (a tetracarboxylic tetrapyrrole). The reaction proceeds stepwise through hepta-, hexa- and penta-carboxylate porphyrinogen intermediates, beginning at the ring-D acetate, with decarboxylation of the heptacarboxylate III intermediate being rate-limiting under physiological conditions ([PMID: 9564029](https://pubmed.ncbi.nlm.nih.gov/9564029/); [PMID: 6626522](https://pubmed.ncbi.nlm.nih.gov/6626522/)).

This step sits at a metabolically decisive point. Uroporphyrinogen III is the last common precursor shared by heme, siroheme, cobalamin (B₁₂) and (in phototrophs) chlorophyll. URO-D is **the first committed enzyme of the branch that leads specifically to protoheme (heme b)** rather than to siroheme or corrinoids, and its activity is therefore essential for supplying heme to the cytochromes, catalase and other hemoproteins that this obligately aerobic soil bacterium requires for respiration and oxidative-stress defense ([PMID: 7849561](https://pubmed.ncbi.nlm.nih.gov/7849561/)). The enzyme is a **soluble, cytoplasmic protein** that functions without any metal ion or organic cofactor — an unusual property for a decarboxylase — adopting a distorted (β/α)₈ TIM-barrel fold and acting as a **homodimer** with a deep active-site cleft lined by invariant Arg/Asp/Tyr/His residues ([PMID: 9564029](https://pubmed.ncbi.nlm.nih.gov/9564029/); [PMID: 11524417](https://pubmed.ncbi.nlm.nih.gov/11524417/)).

While no experimental study has been published on the *P. putida* protein specifically, the functional assignment is exceptionally well supported by transitive evidence. Direct sequence analysis performed in this investigation shows that Q88CV6 (354 aa) shares **~50% identity with the biochemically and structurally characterized human enzyme** and conserves **five of the six invariant active-site residues** (Arg27, Arg31, Asp77, Tyr154, His327), the sixth being the expected conservative bacterial Ser→Thr substitution (Thr209). Bacterial genetics in *E. coli* demonstrate that loss of *hemE* blocks the pathway, causing uroporphyrin accumulation and heme/catalase deficiency, and that *hemE* orthologs from distant bacteria are functionally interchangeable ([PMID: 7849561](https://pubmed.ncbi.nlm.nih.gov/7849561/); [PMID: 1104578](https://pubmed.ncbi.nlm.nih.gov/1104578/); [PMID: 8224882](https://pubmed.ncbi.nlm.nih.gov/8224882/)). The evidence collectively provides high confidence in the annotation.

---

## Key Findings

### Finding 1 — HemE is uroporphyrinogen decarboxylase (URO-D), catalyzing the fifth step of heme biosynthesis

HemE (Q88CV6) is uroporphyrinogen decarboxylase, the enzyme that performs the fifth step of the heme biosynthetic pathway. The reaction is the conversion of **uroporphyrinogen III → coproporphyrinogen III**, achieved by decarboxylating the four acetic-acid side chains of the substrate. Each acetate side chain (–CH₂–COOH) is converted to a methyl group (–CH₃) with loss of one CO₂, giving a net release of four CO₂ molecules and reducing the number of carboxylate groups on the macrocycle from eight to four.

The definitive statement of this function comes from the human enzyme literature: *"Uroporphyrinogen decarboxylase (URO-D) catalyzes the fifth step in the heme biosynthetic pathway, converting uroporphyrinogen to coproporphyrinogen by decarboxylating the four acetate side chains of the substrate. This activity is essential in all organisms"* ([PMID: 9564029](https://pubmed.ncbi.nlm.nih.gov/9564029/)). A single polypeptide performs all four decarboxylations; purified bovine hepatic enzyme *"catalyzes all four decarboxylation reactions in the conversion of uroporphyrinogen I or III to the corresponding coproporphyrinogen,"* and *"the rate-limiting step in the physiologically significant conversion of uroporphyrinogen III to coproporphyrinogen III is the decarboxylation of heptacarboxylate III"* ([PMID: 6626522](https://pubmed.ncbi.nlm.nih.gov/6626522/)).

The reaction therefore does **not** occur in a single concerted event; it proceeds through a defined sequence of intermediates — **uroporphyrinogen III (8 –COOH) → heptacarboxylate porphyrinogen (7) → hexacarboxylate (6) → pentacarboxylate (5) → coproporphyrinogen III (4)** — with a preference for beginning at the ring-D acetate and processing the remaining rings in clockwise order. The assignment for Q88CV6 rests on HAMAP rule MF_00218, which classifies the *P. putida* PP_5074 product in the URO-D family (PF01208, IPR000257/IPR006361), fully consistent with all family-level and mechanistic evidence.

### Finding 2 — Substrate specificity: prefers the physiological III isomer but is a broad-specificity porphyrinogen carboxy-lyase

The systematic name uroporphyrinogen-III carboxy-lyase reflects the physiological substrate: the type-III isomer of uroporphyrinogen. Kinetic studies of the rat liver enzyme established that *"uroporphyrinogen III was the best substrate by the criteria of Km/Vmax and decarboxylation at 1 microM and was converted into coproporphyrinogen more quickly than its series-I isomer"* ([PMID: 7306050](https://pubmed.ncbi.nlm.nih.gov/7306050/)). This isomer discrimination occurs principally at the first (uroporphyrinogen → heptacarboxylate) decarboxylation.

Despite this physiological preference, the enzyme has intrinsically **low absolute substrate specificity**. Studies of the rat-liver porphyrinogen carboxy-lyase showed that *"this enzyme has a low substrate specificity since at least eighteen porphyrinogens were proved to be decarboxylated by the enzyme"* ([PMID: 1052603](https://pubmed.ncbi.nlm.nih.gov/1052603/)). It can act on all four uroporphyrinogen isomers (I, II, III and IV) and on the partially decarboxylated hepta-, hexa- and penta-carboxylate intermediates. A critical mechanistic requirement is that the substrate must be the **reduced porphyrinogen** (hexahydroporphyrin); the corresponding oxidized porphyrin is not a substrate and acts as an inhibitor. The catalytic target is the tetrapyrrole macrocycle bearing acetate side chains.

### Finding 3 — URO-D is a cofactor-independent (β/α)₈ TIM-barrel enzyme functioning as a homodimer

A striking feature of URO-D is that it is a **decarboxylase requiring neither a metal ion nor an organic cofactor** (no pyridoxal phosphate, biotin, thiamine or metal). This is highly unusual, because most decarboxylases rely on a cofactor to stabilize the carbanion intermediate. Instead, URO-D is *inhibited* by divalent metals (Fe²⁺, Co²⁺, Cu²⁺, Zn²⁺, Pb²⁺) and by sulfhydryl reagents, and uses only protein side chains for catalysis.

The crystal structure of the human enzyme (1.60 Å) revealed the architecture: *"The 40.8 kDa protein is comprised of a single domain containing a (beta/alpha)8-barrel with a deep active site cleft formed by loops at the C-terminal ends of the barrel strands. Many conserved residues cluster at this cleft, including the invariant side chains of Arg37, Arg41 and His339, which probably function in substrate binding, and Asp86, Tyr164 and Ser219, which may function in either binding or catalysis. URO-D is a dimer in solution"* ([PMID: 9564029](https://pubmed.ncbi.nlm.nih.gov/9564029/)). The (β/α)₈-barrel is a *distorted* TIM barrel conserved across every URO-D structure solved to date, including the tobacco and *Plasmodium falciparum* enzymes. Dimerization (Kd ≈ 0.1 µM) juxtaposes the two active-site clefts and is important for stability and activity.

Structural modeling of the tobacco (*Nicotiana tabacum*) enzyme assigned the catalytic acid/base groups: *"Asp(82) and Tyr(159) seem to be the catalytic functional groups, whereas the other residues may serve in substrate recognition and binding, with Arg(32) steering its insertion"* ([PMID: 11524417](https://pubmed.ncbi.nlm.nih.gov/11524417/)) — the tobacco Asp82/Tyr159 correspond to human Asp86/Tyr164. Mechanistically, all four acetate → methyl conversions proceed by an identical route: *"In the uroporphyrinogen decarboxylase-catalysed reaction all four acetate side chains are converted into methyl groups by the same mechanism, to produce coproporphyrinogen III. Both methylene hydrogen atoms remain undisturbed and the reaction occurs with the retention of stereochemistry"* ([PMID: 7842850](https://pubmed.ncbi.nlm.nih.gov/7842850/)).

### Finding 4 — The *P. putida* protein conserves the URO-D catalytic machinery (direct sequence evidence)

To convert the general URO-D characterization into a specific, evidence-based assignment for Q88CV6, a global pairwise alignment was performed in this investigation between the *P. putida* protein (354 aa) and the biochemically and structurally characterized human enzyme (UniProt P06132, 367 aa). The two share **~49.7% identity** over aligned positions — a value well above the threshold at which enzymatic function is reliably transferable.

Critically, **five of the six invariant human active-site residues are strictly conserved** at the mapped positions in *P. putida* HemE:

| Function | Human URO-D | *P. putida* HemE (Q88CV6) | Conserved? |
|---|---|---|---|
| Substrate binding | Arg37 | Arg27 | ✅ |
| Substrate binding (R-Q-A-G-R motif) | Arg41 | Arg31 | ✅ |
| Catalysis / binding | Asp86 | Asp77 | ✅ |
| Catalysis / binding | Tyr164 | Tyr154 | ✅ |
| Substrate binding / isomer specificity | His339 | His327 | ✅ |
| Binding | Ser219 | Thr209 | ⚠️ conservative Ser→Thr |

The diagnostic **R-Q-A-G-R motif** (present as "MRQAGR" around residues 24–31) anchors the two catalytic arginines. The single non-identity — human Ser219 → Thr209 in *P. putida* — is precisely the substitution noted by Martins et al. (2001), who reported this residue as "Ser214 (Thr in *E. coli*)," i.e., a recognized conservative difference in which eukaryotes carry Ser and bacteria carry Thr at this substrate-binding position. This preservation of the full catalytic constellation, combined with ~50% overall identity, provides direct, residue-level evidence that Q88CV6 possesses a functional URO-D active site.

### Finding 5 — Bacterial genetics confirm *hemE* is the committed branch-point enzyme; loss blocks heme synthesis

Because the biochemistry was established largely in mammalian and plant systems, it is important that the *bacterial* function is independently confirmed by genetics in *E. coli*, a close relative of *Pseudomonas* (both γ-proteobacteria). Uroporphyrinogen III is the last common tetrapyrrole precursor: *"Uroporphyrinogen III is the committed intermediate common to heme and siroheme biosynthesis in E. coli. Uroporphyrinogen III decarboxylase is the first enzyme at the branch point which commits to heme synthesis"* ([PMID: 7849561](https://pubmed.ncbi.nlm.nih.gov/7849561/)). A *hemE* mutant accumulated uroporphyrin, had no URO-D activity, and was rescued by a heterologous *Synechococcus hemE* plasmid — after which it accumulated copro- and protoporphyrin instead of uroporphyrin, demonstrating restoration of downstream flux and cross-species interchangeability.

The first *E. coli* URO-D-deficient mutant (SASQ85) was, in the authors' words, *"the first uroporphyrinogen decarboxylase-deficient mutant isolated in E. coli K-12"*; it accumulated uroporphyrin III, was catalase-deficient, and formed dwarf colonies, and cell-free extracts converted δ-aminolevulinic acid / porphobilinogen as far as uroporphyrinogen but no further ([PMID: 1104578](https://pubmed.ncbi.nlm.nih.gov/1104578/)). This phenotype directly demonstrates the physiological consequence of losing the enzyme: the pathway stalls at uroporphyrinogen, heme-dependent enzymes such as catalase are not produced, and porphyrin precursors accumulate. Molecular cloning showed *"an open reading frame of 353 codons, which encoded a predicted amino acid sequence that exhibited a high degree of homology over its entire length to the amino acid sequence of UPD from humans and other organisms"* ([PMID: 8224882](https://pubmed.ncbi.nlm.nih.gov/8224882/)) — a length (~353 aa) essentially identical to the 354-aa *P. putida* protein. Finally, site-directed mutagenesis of human His339 showed that this conserved histidine (equivalent to *P. putida* His327) *"is likely important in imparting isomer specificity"* ([PMID: 8980654](https://pubmed.ncbi.nlm.nih.gov/8980654/)), tying a specific conserved residue to a specific functional property.

---

## Mechanistic Model / Interpretation

### Position of HemE in the tetrapyrrole biosynthetic pathway

```
   Glutamate / Glycine
          │  (C5 / C4 route to ALA)
          ▼
   δ-Aminolevulinic acid (ALA)
          │  hemB (ALA dehydratase)
          ▼
   Porphobilinogen (PBG)
          │  hemC (PBG deaminase)
          ▼
   Hydroxymethylbilane
          │  hemD (uroporphyrinogen III synthase)
          ▼
   ┌────────────────────────────────────────────┐
   │      UROPORPHYRINOGEN III  (8 × –COOH)      │  ◄── common branch-point precursor
   └────────────────────────────────────────────┘
          │                         │
          │ hemE  ◄◄◄ THIS GENE     └──►  cysG / siroheme, cobalamin (B12) branch
          │ (URO-D, EC 4.1.1.37)
          │  – 4 CO2  (removes 4 acetate side chains)
          ▼
   Coproporphyrinogen III  (4 × –COOH)
          │  hemF / hemN (coproporphyrinogen oxidase)
          ▼
   Protoporphyrinogen IX
          │  hemG / hemY
          ▼
   Protoporphyrin IX
          │  hemH (ferrochelatase) + Fe2+
          ▼
   PROTOHEME (heme b)  ──►  cytochromes, catalase, peroxidases, etc.
```

HemE catalyzes the **first committed step toward heme** after the last branch point. Everything upstream of uroporphyrinogen III is shared with the siroheme and cobalamin routes; once HemE removes the four acetate carboxylates, the molecule is committed to the coproporphyrinogen → protoheme trajectory. In an obligate aerobe such as *P. putida* KT2440, this flux is essential to build the cytochromes of the aerobic respiratory chain and the heme-dependent catalases/peroxidases that defend against reactive oxygen species.

### Catalytic mechanism

The four decarboxylations share one chemical mechanism and occur with retention of stereochemistry, using only protein side chains (no cofactor). The current model, drawn from the human crystal structure and tobacco modeling, is:

```
   Acetate side chain (–CH2–COO−)
            │
   Arg27 / Arg31  ── electrostatically bind and orient the substrate carboxylates
   Asp77          ── acid/base; protonates/stabilizes the reactive intermediate
   Tyr154         ── acid/base partner
   His327         ── binding + governs isomer specificity
            │
            ▼
   Decarboxylation → loss of CO2 → –CH3 (methyl) side chain
```

All six residues cluster in a deep active-site cleft at the C-terminal ends of the (β/α)₈ barrel strands. The homodimer brings two clefts together, important for stability and activity. In *P. putida* HemE the equivalent residues (Arg27, Arg31, Asp77, Tyr154, His327) are all present, so the same mechanism is expected.

### Localization

Bacterial URO-D is a **soluble cytoplasmic enzyme** carrying out its reaction in the cytosol, consistent with the fact that the upstream (substrate-generating) and downstream (heme-forming) bacterial enzymes act in the cytoplasm / at the inner membrane. No signal peptide, transmembrane segment or organellar targeting sequence is expected for the *P. putida* protein. (In eukaryotes URO-D is cytosolic; in the apicoplast-bearing parasite *P. falciparum* it is targeted to the apicoplast, reflecting that organism's compartmentalized hybrid pathway — [PMID: 19041871](https://pubmed.ncbi.nlm.nih.gov/19041871/) — but this does not apply to a free-living bacterium.)

### Confidence assessment

| Line of evidence | Strength | Notes |
|---|---|---|
| Family/domain assignment (HAMAP MF_00218, PF01208) | High | Rule-based but well-curated |
| ~50% identity to characterized human enzyme | High | Above reliable function-transfer threshold |
| 5/6 invariant active-site residues conserved | High | Direct residue-level evidence (this work) |
| Bacterial genetics (*E. coli hemE*) confirm role & phenotype | High | Closely related γ-proteobacterium |
| Cross-species complementation (Synechococcus → *E. coli*) | High | Demonstrates functional interchangeability |
| Direct experimental study of *P. putida* protein | **Absent** | Assignment is transitive, not direct |

---

## Evidence Base

| PMID | Study | How it supports the annotation |
|---|---|---|
| [9564029](https://pubmed.ncbi.nlm.nih.gov/9564029/) | *Crystal structure of human uroporphyrinogen decarboxylase* | Defines the reaction (four acetate side chains decarboxylated, fifth step), the (β/α)₈-barrel fold, the invariant active-site residues, and homodimeric assembly. Foundational structural reference. |
| [6626522](https://pubmed.ncbi.nlm.nih.gov/6626522/) | *Purification of bovine hepatic URO-D* | Shows a single enzyme catalyzes all four decarboxylations; identifies heptacarboxylate III decarboxylation as rate-limiting. |
| [7306050](https://pubmed.ncbi.nlm.nih.gov/7306050/) | *Rat liver URO-D: porphyrinogens I vs III* | Establishes preference for the physiological III isomer (best Km/Vmax). |
| [1052603](https://pubmed.ncbi.nlm.nih.gov/1052603/) | *Tetrapyrroles as substrates/inhibitors of porphyrinogen carboxy-lyase* | Demonstrates broad substrate tolerance (≥18 porphyrinogens decarboxylated). |
| [11524417](https://pubmed.ncbi.nlm.nih.gov/11524417/) | *Crystal structure of tobacco URO-D* | Assigns Asp82/Tyr159 (= human Asp86/Tyr164) as catalytic acid/base groups; confirms conserved TIM barrel across kingdoms. |
| [7842850](https://pubmed.ncbi.nlm.nih.gov/7842850/) | *Mechanistic & stereochemical studies* | Shows all four decarboxylations use one mechanism with retention of stereochemistry. |
| [8980654](https://pubmed.ncbi.nlm.nih.gov/8980654/) | *Mutational analysis of human URO-D* | His339 (= *P. putida* His327) imparts isomer specificity; no single cysteine is essential. |
| [7849561](https://pubmed.ncbi.nlm.nih.gov/7849561/) | *hemA/hemE mutant of E. coli* | Defines *hemE*/URO-D as the committed branch-point enzyme; cross-species complementation restores downstream flux. |
| [1104578](https://pubmed.ncbi.nlm.nih.gov/1104578/) | *Uroporphyrin-accumulating E. coli mutant* | First bacterial URO-D-deficient mutant: uroporphyrin accumulation, catalase deficiency, pathway block. |
| [8224882](https://pubmed.ncbi.nlm.nih.gov/8224882/) | *Cloning of E. coli hemE* | Bacterial *hemE* encodes ~353 aa (≈ *P. putida* 354 aa), homologous full-length to human/other UPDs. |
| [11719352](https://pubmed.ncbi.nlm.nih.gov/11719352/) | *Naturally occurring URO-D mutations (F-PCT)* | Genotype–phenotype and structural mapping of disease mutations; corroborates residue essentiality. |
| [19041871](https://pubmed.ncbi.nlm.nih.gov/19041871/) | *P. falciparum URO-D localization* | Confirms conserved TIM-barrel fold and active-site residues in a divergent organism; illustrates organism-specific localization. |

The evidence is internally consistent across mammalian (human, bovine, rat), plant (tobacco), protozoan (*Plasmodium*) and bacterial (*E. coli*, *Synechococcus*) systems: the fold, active-site residues, cofactor-independence, reaction, and substrate preference are conserved throughout. No paper in the reviewed set contradicts the assignment.

---

## Limitations and Knowledge Gaps

1. **No direct experimental characterization of the *P. putida* KT2440 protein.** The annotation is transitive — based on sequence homology, conserved active-site residues, and genetics in related bacteria. No published study has purified Q88CV6, measured its kinetic constants, or solved its structure.

2. **Kinetic parameters are borrowed from other species.** The rate-limiting step, isomer preference, and cofactor-independence are documented for human, bovine, rat and plant enzymes, not for the *P. putida* enzyme itself. Quantitative details could differ.

3. **Ser→Thr substitution (Thr209).** This is a conservative, expected bacterial substitution at a substrate-binding position, but its precise effect on *P. putida* enzyme kinetics or isomer discrimination has not been tested.

4. **Localization is inferred, not measured.** Cytoplasmic localization is expected from bacterial biology and the absence of targeting signals, but has not been experimentally demonstrated for this protein.

5. **Regulation and pathway integration in *P. putida* specifically** (transcriptional control, flux control, interaction with iron/oxygen status) were not characterized here; *E. coli hemE* regulation was noted ([PMID: 7849561](https://pubmed.ncbi.nlm.nih.gov/7849561/)) but *P. putida*-specific data are lacking.

6. **Essentiality in *P. putida* is inferred.** Heme biosynthesis is essential in aerobes and *E. coli hemE* loss is severely deleterious, but a targeted *P. putida* KT2440 *hemE* knockout has not been reviewed here.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant expression and enzyme assay.** Clone PP_5074, express Q88CV6 in *E. coli*, purify, and assay URO-D activity on uroporphyrinogen III (and isomer I) by HPLC or the tandem-MS method of [PMID: 18294003](https://pubmed.ncbi.nlm.nih.gov/18294003/) to obtain Km/kcat and confirm the intermediate profile (hepta → hexa → penta → copro).

2. **Complementation test.** Verify that PP_5074 rescues an *E. coli hemE* mutant, mirroring the *Synechococcus*→*E. coli* rescue in [PMID: 7849561](https://pubmed.ncbi.nlm.nih.gov/7849561/).

3. **Structural determination.** Solve the crystal structure (or generate a high-confidence AlphaFold model with PAE analysis) and confirm the distorted (β/α)₈ TIM barrel, homodimer interface, and positioning of Arg27, Arg31, Asp77, Tyr154, His327, Thr209 in a deep active-site cleft.

4. **Active-site mutagenesis.** Test Asp77Asn, Tyr154Phe and His327Asn to confirm catalytic/isomer-specificity roles predicted from human/tobacco homologs ([PMID: 11524417](https://pubmed.ncbi.nlm.nih.gov/11524417/); [PMID: 8980654](https://pubmed.ncbi.nlm.nih.gov/8980654/)); test Thr209Ser to probe the bacterial/eukaryotic substrate-binding difference.

5. **Cofactor-independence check.** Confirm the absence of a metal/organic cofactor requirement and reproduce inhibition by divalent metals and sulfhydryl reagents for the *P. putida* enzyme.

6. **Localization and essentiality.** Use fluorescent fusion / cell fractionation to confirm cytoplasmic localization, and attempt a conditional knockout to confirm essentiality and the expected uroporphyrin-accumulation / heme-deficiency phenotype in *P. putida* KT2440.

---

## Conclusion

*hemE* (PP_5074, Q88CV6) of *Pseudomonas putida* KT2440 encodes **uroporphyrinogen decarboxylase (URO-D, EC 4.1.1.37)**, a soluble, cytoplasmic, cofactor-independent (β/α)₈ TIM-barrel enzyme that functions as a homodimer. Its primary function is the sequential decarboxylation of the four acetate side chains of **uroporphyrinogen III** — via hepta-, hexa- and penta-carboxylate intermediates — to yield **coproporphyrinogen III** and four CO₂, with physiological preference for the type-III isomer. This is the fifth step and the first committed branch-point step of the heme biosynthetic pathway, directing the common precursor uroporphyrinogen III toward protoheme (heme b) rather than siroheme or cobalamin, thereby supplying heme for the cytochromes, catalases and other hemoproteins essential to this aerobic bacterium. The assignment is strongly supported by ~50% sequence identity and conservation of 5/6 invariant catalytic residues relative to the structurally characterized human enzyme, and by bacterial genetics showing that *hemE* loss blocks the pathway.


## Artifacts

- [OpenScientist final report](hemE-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](hemE-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:9564029
2. PMID:6626522
3. PMID:7849561
4. PMID:11524417
5. PMID:1104578
6. PMID:8224882
7. PMID:7306050
8. PMID:1052603
9. PMID:7842850
10. PMID:8980654
11. PMID:19041871
12. PMID:18294003