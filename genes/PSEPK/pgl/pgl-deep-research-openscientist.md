---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-15T08:23:48.169517'
end_time: '2026-07-15T08:51:11.296853'
duration_seconds: 1643.13
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: pgl
  gene_symbol: pgl
  uniprot_accession: Q88P30
  protein_description: 'RecName: Full=6-phosphogluconolactonase {ECO:0000256|ARBA:ARBA00020337,
    ECO:0000256|RuleBase:RU365095}; Short=6PGL {ECO:0000256|RuleBase:RU365095}; EC=3.1.1.31
    {ECO:0000256|ARBA:ARBA00013198, ECO:0000256|RuleBase:RU365095};'
  gene_info: Name=pgl {ECO:0000256|RuleBase:RU365095, ECO:0000313|EMBL:AAN66648.1};
    OrderedLocusNames=PP_1023 {ECO:0000313|EMBL:AAN66648.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the glucosamine/galactosamine-6-phosphate
  protein_domains: 6-phosphogluconolactonase_DevB. (IPR005900); 6PGL. (IPR039104);
    Glc/Gal-6P_isomerase. (IPR006148); NagB/RpiA_transferase-like. (IPR037171); Glucosamine_iso
    (PF01182)
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
citation_count: 8
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: pgl-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: pgl-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88P30
- **Protein Description:** RecName: Full=6-phosphogluconolactonase {ECO:0000256|ARBA:ARBA00020337, ECO:0000256|RuleBase:RU365095}; Short=6PGL {ECO:0000256|RuleBase:RU365095}; EC=3.1.1.31 {ECO:0000256|ARBA:ARBA00013198, ECO:0000256|RuleBase:RU365095};
- **Gene Information:** Name=pgl {ECO:0000256|RuleBase:RU365095, ECO:0000313|EMBL:AAN66648.1}; OrderedLocusNames=PP_1023 {ECO:0000313|EMBL:AAN66648.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the glucosamine/galactosamine-6-phosphate
- **Key Domains:** 6-phosphogluconolactonase_DevB. (IPR005900); 6PGL. (IPR039104); Glc/Gal-6P_isomerase. (IPR006148); NagB/RpiA_transferase-like. (IPR037171); Glucosamine_iso (PF01182)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "pgl" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'pgl' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **pgl** (gene ID: pgl, UniProt: Q88P30) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of *pgl* (PP_1023, UniProt Q88P30): 6-Phosphogluconolactonase of *Pseudomonas putida* KT2440

## Summary

The gene **pgl** (ordered locus **PP_1023**; UniProt **Q88P30**) of *Pseudomonas putida* strain KT2440 encodes **6-phosphogluconolactonase (6PGL, EC 3.1.1.31)**, a cytoplasmic hydrolase that catalyzes the second reaction of the oxidative branch of the pentose-phosphate pathway. Specifically, Pgl hydrolyzes **6-phospho-D-glucono-1,5-lactone** — the product released by glucose-6-phosphate dehydrogenase (Zwf) — to **6-phospho-D-gluconate**, with the net reaction 6-phospho-D-glucono-1,5-lactone + H₂O → 6-phospho-D-gluconate + H⁺ (Rhea:12556). The enzyme is a 242-residue, cofactor-independent lactonohydrolase belonging to the glucosamine/galactosamine-6-phosphate isomerase (NagB/RpiA) superfamily, specifically the DevB-type 6PGL subfamily, and adopts an α/β-hydrolase-like fold (Pfam PF01182; InterPro IPR005900, IPR039104, IPR006148, IPR037171).

The functional assignment of PP_1023 rests on a coherent, mutually reinforcing body of evidence: (1) concordant orthology and domain annotation across UniProt, KEGG, COG (COG0363), and BioCyc; (2) genomic context — *pgl* is embedded in the canonical, experimentally confirmed **zwf-pgl-eda operon** whose transcription is repressed by the sugar-isomerase-domain regulator HexR and derepressed specifically by the Entner-Doudoroff intermediate 2-keto-3-deoxy-6-phosphogluconate (KDPG); (3) systems-level ¹³C-flux physiology showing that ~90 % of glucose in *P. putida* transits through 6-phosphogluconate (Pgl's product) into the Entner-Doudoroff pathway; and (4) structural bioinformatics — a very high-confidence AlphaFold model (mean pLDDT 95.5) that superposes onto the experimentally solved *Trypanosoma brucei* 6PGL and conserves the family's catalytic signature motif (G-D-x-G-H-T-A-S) including a putative catalytic His152.

Biologically, Pgl sits at a metabolic hub. *P. putida* KT2440 lacks 6-phosphofructokinase and cannot run classical (EMP) glycolysis in the catabolic direction; it catabolizes glucose exclusively via the Entner-Doudoroff pathway, where three convergent peripheral routes meet at 6-phosphogluconate. As the single-copy 6PGL (in contrast to the triplicated *zwf*), PP_1023 provides the obligatory lactone-hydrolysis step in the cytoplasmic phosphorylative branch and, through the NADPH-generating **EDEMP cycle**, contributes to the redox economy that underpins this bacterium's hallmark tolerance to oxidative stress. The one important caveat is that the *P. putida* Pgl protein has not itself been enzymatically assayed; the annotation, though very strong, is an inference from orthology, operon structure, flux physiology, and structural homology rather than direct biochemical characterization of Q88P30.

---

## Gene/Protein Identity Verification

Before presenting findings, the gene identity was verified against the UniProt reference. The gene symbol *pgl* corresponds precisely to the protein description (6-phosphogluconolactonase, 6PGL, EC 3.1.1.31); the organism is confirmed as *Pseudomonas putida* KT2440 (ordered locus PP_1023, KEGG ppu:PP_1023); and the protein family and domains found in the literature (DevB-type 6PGL, Pfam PF01182 Glucosamine_iso, NagB/RpiA fold) align exactly with the UniProt annotation. The literature reviewed for this report — both the *P. putida*-specific metabolic studies and the structural studies of orthologous 6PGL enzymes — is consistent with this identity. **No ambiguity or misassignment was found.** *pgl* is unambiguously the single-copy 6-phosphogluconolactonase gene of the ED/oxidative-pentose-phosphate route in this genome.

---

## Key Findings

### 1. Pgl catalyzes step 2 of the oxidative pentose-phosphate branch: hydrolysis of 6-phosphogluconolactone

The primary function of PP_1023 is enzymatic. UniProt Q88P30, annotated through the curated rule systems RuleBase RU365095 and ARBA, assigns the FUNCTION "Hydrolysis of 6-phosphogluconolactone to 6-phosphogluconate" and the CATALYTIC ACTIVITY reaction **6-phospho-D-glucono-1,5-lactone + H₂O = 6-phospho-D-gluconate + H⁺** (Rhea:12556; ChEBI substrate 57955 → product 58759), with enzyme classification **EC 3.1.1.31**. The pathway annotation places the reaction precisely: "pentose phosphate pathway; D-ribulose 5-phosphate from D-glucose 6-phosphate (oxidative stage): step 2/3." The protein is 242 amino acids, gene symbol *pgl*, ordered locus name PP_1023, catalogued as KEGG ppu:PP_1023, orthology group COG0363, with a defined BioCyc monomer entry.

Mechanistically, this is a lactonohydrolase reaction. The oxidative pentose-phosphate branch proceeds in three steps: (step 1) glucose-6-phosphate dehydrogenase (Zwf) oxidizes glucose-6-phosphate to 6-phospho-D-glucono-1,5-lactone, generating NAD(P)H; (step 2) Pgl accelerates the hydrolysis of the strained δ-lactone ring to 6-phospho-D-gluconate; (step 3) 6-phosphogluconate is further metabolized — either dehydrated by Edd (to KDPG, entering the ED pathway) or oxidatively decarboxylated by 6-phosphogluconate dehydrogenase (to ribulose-5-phosphate, the pentose-phosphate branch). Although the lactone can hydrolyze spontaneously, the enzymatic step matters because the reactive 1,5-lactone can otherwise isomerize to a stable, metabolically dead-end 1,4-lactone; Pgl channels the intermediate cleanly to 6-phosphogluconate. This function is cofactor-independent (no NAD(P) and no metal is required for the hydrolysis).

### 2. Pgl belongs to the DevB-type 6PGL / NagB-fold superfamily with an α/β-hydrolase-like active site

The family assignment is consistent across all annotation systems. UniProt records the SIMILARITY "Belongs to the glucosamine/galactosamine-6-phosphate isomerase family. 6-phosphogluconolactonase subfamily," with the domain spanning residues 24–237 annotated as "Glucosamine/galactosamine-6-phosphate isomerase." Supporting signatures include Pfam **PF01182 (Glucosamine_iso)**, InterPro **IPR005900** (6-phosphogluconolactonase DevB), **IPR039104** (6PGL), **IPR006148** (Glc/Gal-6P isomerase), **IPR037171** (NagB/RpiA transferase-like), SUPFAM SSF100950, and COG0363.

The structural and mechanistic basis for this family was established in the crystallographic study of *T. brucei* 6PGL, [PMID: 17196981](https://pubmed.ncbi.nlm.nih.gov/17196981/), which states: *"Comparison of its sequence and structure to other related proteins in the 6PGL family with a known structure (Thermotoga maritima Tm6GPL 1PBT and Vibrio cholerae Vc6PGL (1Y89), which have not been discussed in print), or in the glucosamine-6-phosphate-deaminase family (hexameric Escherichia coli 1DEA and monomeric Bacillus subtilis 2BKV), allowed the identification of the 6PGL active site."* This confirms that DevB-type 6PGL enzymes share the glucosamine-6-phosphate deaminase (NagB) fold and that their active sites are defined by homology within this superfamily — exactly the family to which Q88P30 is assigned. A follow-up study combining structural data and molecular dynamics, [PMID: 19345229](https://pubmed.ncbi.nlm.nih.gov/19345229/), further reports that *"Analysis of the structural data and MD simulations allowed us to propose a detailed enzymatic mechanism for 6PGL enzymes,"* establishing that the catalytic mechanism of this family — hydrolysis of the δ-6-phosphogluconolactone — has been characterized both structurally and by simulation.

### 3. The AlphaFold model of Q88P30 is high-confidence, supporting a single well-folded catalytic domain

To assess the structural plausibility of the annotation, the AlphaFold DB model **AF-Q88P30-F1 (v6)** was examined. Across all 242 residues, the model has a **mean pLDDT of 95.5** and median of 97.9; **92.1 % of residues score pLDDT > 90 (very high confidence)** and 97.9 % score > 70 (confident), with only 1.2 % below 50. Restricting to the annotated catalytic domain (residues 24–237, the glucosamine/galactosamine-6-phosphate isomerase domain), the mean pLDDT is **97.0**; only the short, flexible N-terminus is slightly less ordered.

This level of confidence indicates that AlphaFold recognizes Q88P30 as a single, well-defined, compact NagB/6PGL-fold domain with no disordered or ambiguous regions in the catalytically relevant core — consistent with a stably folded soluble metabolic enzyme rather than a multidomain or intrinsically disordered protein.

### 4. Q88P30 conserves the 6PGL fold and catalytic motif (His152) of the experimentally solved *T. brucei* 6PGL

A direct structural superposition (via `phenix.superpose_pdbs`) of the Q88P30 AlphaFold model against the experimental *T. brucei* 6PGL crystal structure (PDB **2J0E**) yielded **21.7 % sequence identity** over the aligned length — squarely within the expected range for distant, cross-kingdom orthologs of the same enzyme family. The alignment conserves the family signature block: the *T. brucei* segment `VLLGLGSDGHTASIFP` aligns to Q88P30 `VLVLGMGDDGHTASLFP` (Q88P30 residues 141–157). This block contains the conserved **G-D-x-G-H-T-A-S motif** (Q88P30 positions 148–155) and a **putative catalytic histidine, His152**. An N-terminal G-G motif (Q88P30 residues 55–56, within the sequence `LSGG`) is also conserved. Critically, AlphaFold confidence at these functionally important positions is very high (domain mean pLDDT 97.0), meaning the conserved catalytic residues are modeled with high reliability.

The relevance of this comparison is that the *T. brucei* 6PGL structure (2J0E) is the very reference from which the 6PGL active site was originally defined, per [PMID: 17196981](https://pubmed.ncbi.nlm.nih.gov/17196981/). Using its conserved motif to locate the active site of the *P. putida* ortholog is therefore methodologically sound, and the conservation of both the fold and the catalytic His validates the EC 3.1.1.31 assignment structurally.

### 5. *pgl* is the single-copy 6PGL gene in the *P. putida* KT2440 genome

Mapping KEGG KO identifiers to genes in *P. putida* KT2440 shows that **K01057 (6-phosphogluconolactonase) maps to a single locus, ppu:PP_1023 (*pgl*)** — the enzyme is non-redundant in this genome. This contrasts sharply with the neighboring oxidative-branch enzyme: glucose-6-phosphate dehydrogenase (**K00036, *zwf*) is triplicated** (PP_1022/zwf-1, PP_4042/zwf-2, PP_5351/zwf-3), a redundancy that has been the subject of dedicated study on isozyme cofactor specificity ([PMID: 33727391](https://pubmed.ncbi.nlm.nih.gov/33727391/)). KDPG aldolase (K01625, *eda*, PP_1024) is likewise single-copy.

The single-copy status of *pgl* has functional implications: while the cell hedges its NADPH-generating dehydrogenase step across three *zwf* isozymes (with different cofactor preferences), the lactone-hydrolysis step depends on a single gene product. This makes PP_1023 a potentially non-redundant node in the oxidative branch, and it simplifies the interpretation of any loss-of-function phenotype since there is no paralog to buffer its loss.

### 6. *pgl* is encoded in the zwf-pgl-eda operon feeding the Entner-Doudoroff / EDEMP cycle

The genomic neighborhood of PP_1023 defines its regulatory and metabolic logic. In KEGG, the locus organization is: **PP_1022 *zwf*** = glucose-6-phosphate 1-dehydrogenase (K00036), **PP_1023 *pgl*** = 6-phosphogluconolactonase (K01057), **PP_1024 *eda*** = KDPG aldolase (K01625), with an upstream **PP_1021** RpiR/HexR-family carbohydrate-utilization regulator (K19337). This is the canonical **zwf-pgl-eda operon**.

The physiological importance of this arrangement is that *P. putida* KT2440 lacks 6-phosphofructokinase and therefore catabolizes glucose **exclusively via the Entner-Doudoroff pathway**. Metabolic flux analysis, [PMID: 26350459](https://pubmed.ncbi.nlm.nih.gov/26350459/), showed that *"90% of the consumed sugar was converted into gluconate, entering central carbon metabolism as 6-phosphogluconate and further channeled into the ED pathway"* — that is, Pgl's product (6-phosphogluconate) is the central metabolite of glucose catabolism. The same study defined the **EDEMP cycle**: *"This set of reactions merges activities belonging to the ED, the EMP (operating in a gluconeogenic fashion), and the pentose phosphate pathways to form an unforeseen metabolic architecture (EDEMP cycle)."* In this cycle, a fraction of triose phosphates is recycled to hexose phosphates, and glucose-6-phosphate re-enters the oxidative branch (Zwf → Pgl → 6PG) to overproduce NADPH. The link between this route and physiology is direct: [PMID: 23301697](https://pubmed.ncbi.nlm.nih.gov/23301697/) reports that *"these results expose the role of the ED pathway for generating the redox currency (NADPH) that is required for counteracting oxidative stress"* in *P. putida*.

### 7. Pgl operates in the cytoplasmic phosphorylative branch, one of three convergent peripheral glucose pathways

The precise metabolic placement of Pgl was established by the integrated genomic, ¹³C-flux, and microarray study of del Castillo et al., [PMID: 17483213](https://pubmed.ncbi.nlm.nih.gov/17483213/). This work showed that *"glucose catabolism in Pseudomonas putida occurs through the simultaneous operation of three pathways that converge at the level of 6-phosphogluconate, which is metabolized by the Edd and Eda Entner/Doudoroff enzymes to central metabolites."* Pgl is a member of the **cytoplasmic phosphorylative branch**: cytoplasmic glucose is *"phosphorylated by glucokinase (encoded by the glk gene) and converted by glucose-6-phosphate dehydrogenase (encoded by the zwf genes) to 6-phosphogluconate."* In this two-enzyme (Zwf-then-Pgl) segment, PP_1023 catalyzes the intervening lactone-hydrolysis step. The other two convergent branches — direct gluconate phosphorylation via gluconokinase, and the 2-ketogluconate route — bypass Pgl entirely, reaching 6-phosphogluconate without a lactone intermediate. This clarifies that Pgl is specifically required only for the fraction of carbon that enters as intracellular glucose-6-phosphate.

### 8. The operon is experimentally confirmed and regulated by HexR, derepressed specifically by KDPG

The regulation of *pgl* was characterized experimentally by Daddaoua, Krell & Ramos, [PMID: 19506074](https://pubmed.ncbi.nlm.nih.gov/19506074/). This study established that in *P. putida* *"genes for the glucose phosphorylative pathway and the Entner-Doudoroff pathway are organized in two operons; one made up of the zwf, pgl, and eda genes."* The *P(zwf)* promoter is modulated by the repressor **HexR** in response to glucose availability. Purified HexR (a monomer) binds the *P(zwf)*, *P(edd)*, and *P(gap-1)* operators with nanomolar affinity at a pseudopalindromic site 5′-TTGTN₇₋₈ACAA-3′. Crucially, the derepression signal is specific: *"Binding of the Entner-Doudoroff pathway intermediate 2-keto-3-deoxy-6-phosphogluconate to HexR released the repressor from its target operators, whereas other chemicals such as glucose, glucose 6-phosphate, and 6-phosphogluconate did not induce complex dissociation."* The phosphorylated effector KDPG is recognized by HexR's C-terminal sugar-isomerase (RpiR) domain; PP_1021 is the adjacent *hexR* gene. This defines the regulatory logic controlling *pgl* expression: the operon is switched on when flux through the ED pathway builds up the downstream intermediate KDPG, coupling *pgl* transcription to actual ED-pathway demand.

---

## Mechanistic Model / Interpretation

### The reaction and its place in the pathway

```
        Glucose-6-phosphate (G6P)
                 │
                 │  Zwf (G6P dehydrogenase, PP_1022/4042/5351)
                 │  + NADP+ / NAD+  →  + NAD(P)H          [OPPP step 1]
                 ▼
   6-Phospho-D-glucono-1,5-lactone
                 │
                 │  ★ Pgl (6PGL, PP_1023)  ★               [OPPP step 2]
                 │  + H2O  →  + H+     (EC 3.1.1.31)
                 ▼
        6-Phospho-D-gluconate  ◄────────── central branch-point metabolite
                 │
        ┌────────┴───────────────┐
        │                        │
        │ Edd (6PG dehydratase)  │ Gnd (6PG dehydrogenase)  [OPPP step 3]
        ▼                        ▼
      KDPG ──► Eda ──► pyruvate + G3P      Ribulose-5-P (PPP)
      (Entner–Doudoroff)
```

Pgl performs a single, well-defined chemical step: the water-mediated ring opening of the reactive δ-lactone to the open-chain acid. Although this hydrolysis proceeds spontaneously at a low rate, the enzyme both accelerates it and prevents the metabolically inconvenient isomerization of the 1,5-lactone to the stable 1,4-lactone. The reaction is cofactor- and metal-independent, distinguishing Pgl mechanistically from its NADP-dependent upstream partner Zwf.

### Convergent glucose catabolism and the branch point

*P. putida* KT2440 is metabolically distinctive: it has no 6-phosphofructokinase and therefore cannot run Embden-Meyerhof-Parnas glycolysis in the catabolic direction. Instead, glucose is funneled to **6-phosphogluconate** via three convergent peripheral routes, and only then split by the Entner-Doudoroff enzymes. Pgl participates in exactly one of these three routes — the intracellular phosphorylative branch (Glk → Zwf → **Pgl**) — as summarized below.

| Peripheral branch | Enzymes | Does it use Pgl? |
|---|---|---|
| Phosphorylative (intracellular glucose) | Glk → Zwf → **Pgl** → 6PG | **Yes** — Pgl performs the lactone hydrolysis |
| Direct gluconate phosphorylation | Gluconate → gluconokinase → 6PG | No |
| 2-Ketogluconate route | Gluconate → 2-ketogluconate → … → 6PG | No |

Because roughly 90 % of glucose in *P. putida* is first oxidized in the periplasm to gluconate and enters as 6-phosphogluconate through the gluconate branches, the majority carbon flux actually bypasses Pgl under glucose growth. Pgl is essential specifically for the portion of glucose that is phosphorylated intracellularly and oxidized by Zwf, and — importantly — for the **EDEMP recycling cycle**, in which recycled glucose-6-phosphate is re-routed through the oxidative branch (Zwf → Pgl) to boost NADPH output. In this recycling role, Pgl contributes directly to the redox economy that gives *P. putida* its notable oxidative-stress robustness.

### Regulatory logic

```
   ED-pathway flux ↑  ──►  KDPG accumulates
                               │
                               ▼   (binds HexR RpiR domain)
     HexR ─────────────────►  HexR released from P(zwf)
   (represses P(zwf))                    │
                                         ▼
                       zwf ─ pgl ─ eda  transcription ON
```

The zwf-pgl-eda operon is under negative control by HexR and is derepressed **specifically by KDPG**, a downstream ED intermediate — not by glucose, G6P, or 6-phosphogluconate. This feed-forward-like logic ensures that *pgl* (and its operon partners) are expressed in proportion to genuine flux demand through the ED pathway, rather than simply in the presence of the initial substrate. The single-copy status of *pgl* (versus triplicated *zwf*) means this one regulated gene must satisfy the lactone-hydrolysis demand of the whole oxidative branch.

### Localization

All evidence points to a **cytoplasmic** location. The reaction operates on phosphorylated intracellular intermediates (G6P-derived lactone → 6-phosphogluconate); the pathway partners Zwf and Eda are cytoplasmic; there is no signal peptide, transmembrane segment, or periplasmic-targeting feature in the annotation; and the AlphaFold model is a single soluble globular domain. Pgl carries out its function in the cytoplasm, at the interface of the oxidative pentose-phosphate branch and the Entner-Doudoroff/EDEMP network.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [17483213](https://pubmed.ncbi.nlm.nih.gov/17483213/) | *Convergent peripheral pathways catalyze initial glucose catabolism in P. putida* | Places Pgl in the cytoplasmic phosphorylative branch; establishes 6-phosphogluconate as the convergence point feeding the ED enzymes (¹³C-flux + genomics + microarray) |
| [19506074](https://pubmed.ncbi.nlm.nih.gov/19506074/) | *Regulation of glucose metabolism in Pseudomonas… repressor with sugar isomerase domain* | Experimentally confirms the zwf-pgl-eda operon and HexR/KDPG regulatory logic |
| [26350459](https://pubmed.ncbi.nlm.nih.gov/26350459/) | *P. putida KT2440 metabolizes glucose through the EDEMP cycle* | Defines the EDEMP cycle; shows ~90 % of glucose transits as 6-phosphogluconate (Pgl's product) |
| [23301697](https://pubmed.ncbi.nlm.nih.gov/23301697/) | *The ED pathway empowers P. putida with high oxidative-stress tolerance* | Links the ED/oxidative branch (Pgl's route) to NADPH supply and stress tolerance |
| [17196981](https://pubmed.ncbi.nlm.nih.gov/17196981/) | *3D structure and catalytic mechanism of 6PGL from T. brucei* | Reference structure (2J0E) defining the 6PGL family active site; basis for structural validation of Q88P30 |
| [19345229](https://pubmed.ncbi.nlm.nih.gov/19345229/) | *Enzymatic mechanism of 6PGL from T. brucei (structure + MD)* | Establishes the detailed catalytic mechanism of the 6PGL family |
| [33727391](https://pubmed.ncbi.nlm.nih.gov/33727391/) | *Cofactor specificity of G6PDH isozymes in P. putida* | Context for the triplicated *zwf* (Pgl's operon/pathway partner) and redox-balance role of the oxidative branch |

**How the evidence fits together.** The literature does not include a direct biochemical assay of the *P. putida* Pgl protein. Instead, the annotation is supported by convergent lines: primary ¹³C-flux physiology (17483213, 26350459) establishes that 6-phosphogluconate is the central hub of glucose catabolism and that the oxidative branch feeds the NADPH-generating EDEMP cycle; experimental genetics/biochemistry of the regulator HexR (19506074) confirms that *pgl* is physically co-transcribed with *zwf* and *eda* and is controlled by a mechanism keyed to ED-pathway flux; and structural biology of the well-characterized *T. brucei* orthologue (17196981, 19345229) defines the family fold, active site, and mechanism that the high-confidence AlphaFold model of Q88P30 recapitulates (21.7 % identity, conserved GDxGHTAS motif, His152). No paper contradicts the 6PGL assignment; the *P. putida*-specific studies uniformly treat *pgl* as the operonic 6PGL of the ED/oxidative route. Orthologous 6PGL enzymes from other organisms (e.g., *Leishmania donovani*, [PMID: 36037881](https://pubmed.ncbi.nlm.nih.gov/36037881/)) have been shown to adopt the same α/β-hydrolase 6PGL fold and to be enzymatically active, reinforcing the family-level functional assignment.

---

## Limitations and Knowledge Gaps

1. **No direct enzymology on the *P. putida* protein.** Q88P30 itself has not been purified and assayed. Kinetic parameters (kcat, Km for 6-phospho-D-glucono-1,5-lactone), oligomeric state, and metal/cofactor independence are inferred from family membership and orthologs, not measured for PP_1023.

2. **Catalytic residue is predicted, not proven.** His152 is identified as the putative catalytic histidine by conservation of the GDxGHTAS motif and structural superposition onto *T. brucei* 6PGL. No site-directed mutagenesis of PP_1023 has confirmed it.

3. **No loss-of-function phenotype reported.** Because *pgl* is single-copy and the majority of glucose flux bypasses it via the periplasmic gluconate branches, a *pgl* deletion might have a modest or conditional phenotype. This has not been experimentally tested; the metabolic consequences (e.g., lactone accumulation, altered NADPH balance, EDEMP-cycle impairment) remain predictions.

4. **Structural inference from a model.** The structural conservation argument relies on an AlphaFold model (albeit very high-confidence) rather than an experimental *P. putida* structure. There is no crystal or cryo-EM structure of Q88P30.

5. **Substrate specificity untested.** Members of the broader glucosamine/galactosamine-6-phosphate isomerase superfamily can act on related sugar-phosphates. While the DevB-type subfamily assignment strongly implies 6-phosphogluconolactone specificity, alternative or promiscuous activities of PP_1023 have not been ruled out experimentally.

6. **Quantitative flux through Pgl specifically is unresolved.** The ¹³C-flux studies quantify flux through 6-phosphogluconate as a node but do not resolve the exact fraction that passes through the Zwf→Pgl lactone step versus the direct gluconate/2-ketogluconate branches under different conditions.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant enzyme assay.** Overexpress and purify PP_1023 (as done for the *Leishmania* and *T. brucei* orthologs) and measure lactonohydrolase activity on 6-phospho-D-glucono-1,5-lactone, determining kcat, Km, cofactor/metal dependence, and pH optimum. This would convert the annotation from inference to direct evidence.

2. **Site-directed mutagenesis of His152.** Substitute the predicted catalytic His152 (and test the conserved Asp of the GDxGHTAS motif) and assay activity to confirm the catalytic role predicted by structural homology.

3. **Δ*pgl* knockout phenotyping.** Construct a clean deletion in KT2440 and characterize growth on glucose vs. gluconate vs. non-sugar carbon sources, intracellular 6-phosphogluconolactone/1,4-lactone accumulation, NADPH/NADP⁺ ratio, and sensitivity to oxidative stressors (e.g., H₂O₂, paraquat) — testing the predicted link between Pgl, EDEMP-cycle NADPH, and stress tolerance.

4. **¹³C-flux comparison of WT vs. Δ*pgl*.** Quantify how deletion re-routes carbon among the three convergent peripheral branches and whether the periplasmic gluconate route compensates, resolving the quantitative importance of the Pgl step.

5. **Experimental structure determination.** Solve a crystal or cryo-EM structure of Q88P30 (ideally with a substrate/product analog bound) to validate the AlphaFold model and active-site geometry.

6. **Promoter/regulation validation.** Use a *P(zwf)*-reporter fusion in WT vs. Δ*hexR* backgrounds and with defined effectors to confirm that *pgl* expression tracks KDPG-mediated HexR derepression as predicted, tying transcriptional control directly to the *pgl* gene product level.

---

## Conclusion

The gene *pgl* / PP_1023 (UniProt Q88P30) of *Pseudomonas putida* KT2440 encodes **6-phosphogluconolactonase (6PGL, EC 3.1.1.31)**, a single-copy, cytoplasmic, cofactor-independent hydrolase that converts 6-phospho-D-glucono-1,5-lactone to 6-phospho-D-gluconate as the second step of the oxidative pentose-phosphate branch. It is a DevB/NagB-fold enzyme (Pfam PF01182) encoded in the experimentally confirmed, HexR/KDPG-regulated zwf-pgl-eda operon, and its product 6-phosphogluconate is the branch-point metabolite feeding the Entner-Doudoroff pathway and the NADPH-generating EDEMP cycle that underlies this bacterium's oxidative-stress tolerance. The assignment is a high-confidence, multi-line inference — from concordant orthology/domain annotation, canonical operon structure with experimentally validated regulation, primary ¹³C-flux physiology, and structural homology (21.7 % identity, conserved GDxGHTAS motif, catalytic His152) to the experimentally solved *T. brucei* 6PGL — with the sole caveat that the *P. putida* protein itself has not yet been directly assayed.


## Artifacts

- [OpenScientist final report](pgl-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](pgl-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:17196981
2. PMID:19345229
3. PMID:33727391
4. PMID:26350459
5. PMID:23301697
6. PMID:17483213
7. PMID:19506074
8. PMID:36037881