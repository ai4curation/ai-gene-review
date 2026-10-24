---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T14:45:05.772511'
end_time: '2026-09-01T15:09:27.204354'
duration_seconds: 1461.43
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: glgB
  gene_symbol: glgB
  uniprot_accession: Q88FN1
  protein_description: 'RecName: Full=1,4-alpha-glucan branching enzyme GlgB {ECO:0000255|HAMAP-Rule:MF_00685};
    EC=2.4.1.18 {ECO:0000255|HAMAP-Rule:MF_00685}; AltName: Full=1,4-alpha-D-glucan:1,4-alpha-D-glucan
    6-glucosyl-transferase {ECO:0000255|HAMAP-Rule:MF_00685}; AltName: Full=Alpha-(1->4)-glucan
    branching enzyme {ECO:0000255|HAMAP-Rule:MF_00685}; AltName: Full=Glycogen branching
    enzyme {ECO:0000255|HAMAP-Rule:MF_00685}; Short=BE {ECO:0000255|HAMAP-Rule:MF_00685};'
  gene_info: Name=glgB {ECO:0000255|HAMAP-Rule:MF_00685}; OrderedLocusNames=PP_4058;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the glycosyl hydrolase 13 family. GlgB
  protein_domains: A-amylase/branching_C. (IPR006048); Branching_enzy. (IPR037439);
    GH. (IPR017853); GH13_cat_dom. (IPR006047); GlgB. (IPR006407)
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
citation_count: 15
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: glgB-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: glgB-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88FN1
- **Protein Description:** RecName: Full=1,4-alpha-glucan branching enzyme GlgB {ECO:0000255|HAMAP-Rule:MF_00685}; EC=2.4.1.18 {ECO:0000255|HAMAP-Rule:MF_00685}; AltName: Full=1,4-alpha-D-glucan:1,4-alpha-D-glucan 6-glucosyl-transferase {ECO:0000255|HAMAP-Rule:MF_00685}; AltName: Full=Alpha-(1->4)-glucan branching enzyme {ECO:0000255|HAMAP-Rule:MF_00685}; AltName: Full=Glycogen branching enzyme {ECO:0000255|HAMAP-Rule:MF_00685}; Short=BE {ECO:0000255|HAMAP-Rule:MF_00685};
- **Gene Information:** Name=glgB {ECO:0000255|HAMAP-Rule:MF_00685}; OrderedLocusNames=PP_4058;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the glycosyl hydrolase 13 family. GlgB
- **Key Domains:** A-amylase/branching_C. (IPR006048); Branching_enzy. (IPR037439); GH. (IPR017853); GH13_cat_dom. (IPR006047); GlgB. (IPR006407)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "glgB" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'glgB' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **glgB** (gene ID: glgB, UniProt: Q88FN1) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *glgB* (Q88FN1) — 1,4-α-Glucan Branching Enzyme of *Pseudomonas putida* KT2440

**Gene:** *glgB* (Ordered locus PP_4058) · **UniProt:** Q88FN1 · **EC 2.4.1.18**
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440)
**Protein:** 1,4-α-glucan branching enzyme GlgB · 736 aa · 82.9 kDa · GH13 family

---

## Summary

The gene **glgB** (UniProt **Q88FN1**; ordered locus **PP_4058**) of *Pseudomonas putida* KT2440 encodes the **1,4-α-glucan branching enzyme GlgB** (EC 2.4.1.18), a 736-residue (~82.9 kDa) soluble cytoplasmic enzyme of **glycoside hydrolase family 13 (GH13)**. Its primary function is unambiguous and well supported both by direct UniProt annotation of the protein and by an extensive body of structural and biochemical work on orthologs: GlgB introduces **α-1,6 branch points** into linear α-1,4-glucan chains. It does so through an unusual **dual catalytic activity** for a single active site — it first cleaves an internal α-1,4-glucosidic bond (α-amylase-like activity), then transfers the released oligosaccharide segment to an α-1,6 position on the same chain (transglycosylase activity). The enzyme is chain-length selective: it does not act on short glucans and requires long linear donor chains (in mycobacterial orthologs, a degree of polymerization of ~16) before it will introduce a branch.

The identity of the target is verified with high confidence. The gene symbol *glgB*, the protein description (1,4-α-glucan branching enzyme / glycogen branching enzyme / EC 2.4.1.18), the GH13 family assignment, and the InterPro domain signatures (IPR006407 GlgB, IPR006047 GH13 catalytic domain, IPR006048 α-amylase C-domain, IPR004193 CBM48) all agree internally and match the literature on characterized GlgB orthologs. No conflicting-gene ambiguity was encountered.

The most biologically specific finding of this investigation concerns the **pathway context** in *P. putida* KT2440. Rather than functioning in classical ADP-glucose–dependent glycogen synthesis, GlgB here is the **terminal branching step of the cytoplasmic GlgE pathway**. Genome analysis shows PP_4058 (*glgB*) is immediately adjacent to, co-oriented with, and operonically linked to **PP_4059 (a fused TreS–Mak trehalose synthase/maltokinase)** and **PP_4060 (GlgE, an α-1,4-glucan:maltose-1-phosphate maltosyltransferase)**, with the *glgB*/*treS* stop–start overlap indicating a single transcriptional unit. Critically, *P. putida* KT2440 **lacks glgC** (ADP-glucose pyrophosphorylase). This pathway — TreS → Mak → GlgE → GlgB — converts trehalose to maltose to maltose-1-phosphate to a linear α-1,4-glucan, which GlgB then branches into a glycogen-type α-1,4/α-1,6-glucan. GlgB thus functions in the cytoplasm as the final, architecture-defining enzyme of intracellular α-glucan (glycogen) biosynthesis in this organism.

---

## Key Findings

### Finding 1 — GlgB is a 1,4-α-glucan branching enzyme (EC 2.4.1.18) that creates α-1,6 branch points

The core functional annotation of Q88FN1 is a **1,4-α-glucan branching enzyme** (EC 2.4.1.18), also known as the glycogen branching enzyme (BE) or 1,4-α-D-glucan:1,4-α-D-glucan 6-glucosyl-transferase. The protein is 736 amino acids and approximately 82.9 kDa. The UniProt FUNCTION annotation states that it "catalyzes the formation of the alpha-1,6-glucosidic linkages in glycogen by scission of a 1,4-alpha-linked oligosaccharide from growing alpha-1,4-glucan chains and the subsequent attachment of the oligosaccharide to the alpha-1,6 position," placing it squarely in glycogen biosynthesis and in the GlgB subfamily of GH13.

This annotation is corroborated by primary literature on GlgB orthologs. Work on the *Mycobacterium tuberculosis* GlgB establishes that the enzyme "catalyzes the branching of a linear glucose chain during glycogenesis by cleaving a 1→4 bond and making a new 1→6 bond" and confirms that "this enzyme belongs to glycoside hydrolase (GH) family 13" ([PMID: 20444687](https://pubmed.ncbi.nlm.nih.gov/20444687/)). More broadly, structural work on the *E. coli* branching enzyme underscores that "branching enzyme is responsible for all branching of glycogen and starch" ([PMID: 26280198](https://pubmed.ncbi.nlm.nih.gov/26280198/)) — that is, the branch points that give glycogen its characteristic tree-like, highly branched architecture are introduced exclusively by enzymes of this class. The reaction and family assignment for Q88FN1 are therefore established with high confidence.

### Finding 2 — GlgB uses a GH13 dual-activity mechanism (α-1,4 cleavage / α-1,6 transfer) with catalytic Asp417 and Glu470 and marked substrate-length selectivity

Branching enzymes are unusual members of the α-amylase (GH13) superfamily because a single active site performs two chemically distinct steps. As documented for the *E. coli* enzyme, GlgB "is an unusual member of the α-amylase family because it has both α-1,4-amylase activity and α-1,6-transferase activity" ([PMID: 26280198](https://pubmed.ncbi.nlm.nih.gov/26280198/)). Mechanistically, GlgB is a **retaining glycosyltransferase**: it cleaves an internal α-1,4 bond of a linear donor chain, holds the released oligosaccharide, and then re-attaches it in α-1,6 linkage. For Q88FN1, the two catalytic residues are identifiable from the conserved GH13 sequence regions: **Asp417** is the catalytic nucleophile (in the region-II motif ...RVDAV...) and **Glu470** is the general acid/base proton donor (region-III motif ...IAEE...).

A defining kinetic property of branching enzymes is their **selectivity for long chains**. GlgB "does not react with shorter glucans, though it will bind much longer substrates and substrate mimics" ([PMID: 26280198](https://pubmed.ncbi.nlm.nih.gov/26280198/)). Quantitatively, studies of mycobacterial and streptomycete GlgB show that linear chains must reach a degree of polymerization of ~16 before branching occurs, "yielding a linear oligomer with a degree of polymerization (∼16) sufficient for GlgB to introduce a branch," and that "branching involves strictly intrachain transfer to generate a C chain" ([PMID: 27221142](https://pubmed.ncbi.nlm.nih.gov/27221142/)). This chain-length requirement explains why GlgB acts downstream of chain-elongating enzymes — it can only branch a polymer that has already been extended sufficiently. This is directly relevant to *P. putida*, where GlgE performs the elongation (see Finding 4).

### Finding 3 — GlgB is a soluble cytoplasmic enzyme embedded in a conserved *glg* gene cluster and is evolutionarily ancient

GlgB carries out its function in the **cytoplasm**. Q88FN1 has no signal peptide and no transmembrane segment (a single Chain feature spanning residues 1–736), consistent with a soluble intracellular enzyme acting on the cytoplasmic α-glucan/glycogen pool. In bacteria the branching-enzyme gene is characteristically embedded within the *glg* gene cluster that encodes the complete glycogen synthesis and degradation machinery — for example "glycogen phosphorylase (glgP), glycogen branching enzyme (glgB), ADP glucose pyrophosphorylase (glgC), glycogen synthase (glgA), phosphoglucomutase (pgm), and glycogen debranching enzyme (glgX)" ([PMID: 11208782](https://pubmed.ncbi.nlm.nih.gov/11208782/)).

Branching enzymes are also extraordinarily ancient. A phylogenomic analysis across more than 400 genomes concluded that these enzymes "were likely to have been present in the last universal common ancestor (LUCA)" ([PMID: 25148856](https://pubmed.ncbi.nlm.nih.gov/25148856/)). The same analysis clarified that the bacterial and eukaryotic branching enzymes are paralogous rather than simple orthologs, noting that "human branching enzyme GBE1 and E. coli branching enzyme GlgB, are in fact related by a gene duplication and consequently paralogous" ([PMID: 25148856](https://pubmed.ncbi.nlm.nih.gov/25148856/)). This deep conservation reinforces the reliability of transferring detailed mechanistic knowledge from characterized orthologs to the *P. putida* enzyme.

### Finding 4 — In *P. putida* KT2440, *glgB* is co-transcribed with *glgE* and *treS/mak* and branches α-glucan made by the cytoplasmic GlgE (maltose-1-phosphate) pathway

This is the most organism-specific and biologically informative finding. KEGG and genome analysis of *P. putida* KT2440 shows **PP_4058 glgB** (KEGG K00700, EC 2.4.1.18) lies immediately adjacent to, and co-oriented (minus strand) with, **PP_4059**, a fused trehalose synthase / maltokinase **TreS–Mak** (K05343), and **PP_4060**, **GlgE**, an α-1,4-glucan:maltose-1-phosphate maltosyltransferase (K16147, EC 2.4.99.16). The genome coordinates — complement(4577900..4580110) for *glgB*, complement(4580107..4583427) for *treS-mak*, and complement(4583598..4585583) for *glgE* — show a stop–start overlap between *glgB* and *treS*, strongly indicating an operon.

Crucially, *P. putida* KT2440 **lacks glgC** (ADP-glucose pyrophosphorylase, K00975 — no genomic hit), even though it retains *glgA* (PP_4050, glycogen synthase, K00703), *glgX* (PP_4055, debranching enzyme, K01214) and *glgP* (PP_5041, glycogen phosphorylase, K00688). The absence of GlgC means the classical ADP-glucose route to glycogen is not the (sole) operative pathway; instead the operonic clustering of *glgB* with *treS/mak* and *glgE* points to the **cytoplasmic GlgE pathway** as the route that GlgB serves.

The GlgE pathway is well defined in mycobacteria and is directly transferable here. It "converts trehalose to α(1→4),α(1→6)-linked glucan in 4 steps" ([PMID: 23901909](https://pubmed.ncbi.nlm.nih.gov/23901909/)), "catalyzed by trehalose synthase TreS, maltokinase Pep2, and glycosyltransferases GlgE and GlgB" ([PMID: 23901909](https://pubmed.ncbi.nlm.nih.gov/23901909/)) — exactly the enzymes encoded by PP_4059 (TreS–Mak), PP_4060 (GlgE), and PP_4058 (GlgB). The role of GlgB within this pathway is explicit: the building block is "α-maltose-1-phosphate as the substrate for the maltosyltransferase GlgE, with subsequent branching of the polymer by the branching enzyme GlgB" ([PMID: 27513637](https://pubmed.ncbi.nlm.nih.gov/27513637/)). The four-step architecture was originally described as "a new pathway from trehalose to alpha-glucan in Mycobacterium tuberculosis comprising four enzymatic steps mediated by TreS, Pep2, GlgE (which has been identified as a maltosyltransferase that uses maltose 1-phosphate) and GlgB" ([PMID: 20305657](https://pubmed.ncbi.nlm.nih.gov/20305657/)). In *P. putida*, therefore, GlgB is the terminal, branch-forming enzyme that converts GlgE-elongated linear α-1,4-glucan into a mature, branched glycogen-type α-glucan.

### Finding 5 — Q88FN1 has the canonical four-module branching-enzyme architecture

InterPro/Pfam mapping of the 736-residue Q88FN1 sequence reveals the classic four-module branching-enzyme domain organization:

| Module | Approx. residues | Pfam / InterPro | Fold / role |
|---|---|---|---|
| N-terminal GlgB-specific domain | ~13–103 | PF22019 / IPR054169 | β-sandwich; influences substrate specificity |
| Carbohydrate-Binding Module 48 (CBM48 / GH13 N-terminal) | ~129–211 | PF02922 / IPR004193 | E-set/Ig-like β-sandwich; carbohydrate binding |
| Central α-amylase GH13 catalytic domain | ~273–606 | PF00128 / IPR006047 | (β/α)₈ TIM-barrel; houses Asp417 (nucleophile) and Glu470 (acid/base) |
| C-terminal α-amylase all-β domain | ~638–735 | PF02806 / IPR006048 | β-sandwich |

The HAMAP rule MF_00685 (GlgB) spans residues 105–736. This architecture is congruent with the experimentally solved full-length *M. tuberculosis* GlgB structure, which "contains four domains: N1 beta-sandwich, N2 beta-sandwich, a central (beta/alpha)(8) domain that houses the catalytic site, and a C-terminal beta-sandwich" ([PMID: 20444687](https://pubmed.ncbi.nlm.nih.gov/20444687/)). The N-terminal modules are functionally important, not merely structural: "the N1 beta-sandwich, which is formed by the first 105 amino acids and superimposes well with the N2 beta-sandwich, is shown to have an influence in substrate binding" ([PMID: 20444687](https://pubmed.ncbi.nlm.nih.gov/20444687/)). This modular layout — N-terminal β-sandwich(es) plus CBM48 flanking a central catalytic TIM-barrel and a C-terminal β-domain — is a hallmark shared across GH13 branching enzymes from bacteria, cyanobacteria, and plants (e.g., rice BEI; [PMID: 21493662](https://pubmed.ncbi.nlm.nih.gov/21493662/)).

### Finding 6 — The AlphaFold model of Q88FN1 is very high confidence, corroborating the four-module fold

The AlphaFold DB model for Q88FN1 (v6, 2025) has a global pLDDT of 96.25. Per-residue analysis of all 736 Cα positions gives a mean pLDDT of 96.2, with 97% of residues at very-high confidence (>90), 99% confident (>70), and only 1% low (<50). Domain-wise mean pLDDT values are uniformly excellent: N-terminal GlgB domain (13–103) 95.1; CBM48 (129–211) 97.1; the GH13 (β/α)₈ catalytic domain (273–606) 97.2; and the C-terminal β-sandwich (638–735) 97.1. The very high and even confidence across all four modules provides strong independent structural support that Q88FN1 folds into the canonical GlgB architecture inferred from sequence and homology, and that the catalytic barrel is well ordered around the predicted active-site residues.

---

## Mechanistic Model / Interpretation

The findings integrate into a coherent picture of GlgB as the **branch-installing terminal enzyme of intracellular α-glucan biosynthesis** in *P. putida* KT2440, operating through the GlgE pathway rather than the classical ADP-glucose pathway.

### The GlgE pathway in *P. putida* KT2440

```
   trehalose
      │  TreS  (PP_4059, N-terminal trehalose synthase module)
      ▼
   maltose
      │  Mak/Pep2  (PP_4059, C-terminal maltokinase module) + ATP
      ▼
   maltose-1-phosphate
      │  GlgE  (PP_4060, maltosyltransferase, EC 2.4.99.16)
      ▼   [iterative α-1,4 elongation → linear α-1,4-glucan, DP grows]
   long linear α-1,4-glucan (DP ≳ 16)
      │  GlgB  (PP_4058, branching enzyme, EC 2.4.1.18)   ◄── THIS PROTEIN
      ▼   [cleave internal α-1,4 bond → transfer segment to α-1,6 position]
   branched α-1,4/α-1,6-glucan  (glycogen-type polymer)
```

Genomic organization (all on the minus strand, an apparent operon):

```
  ── PP_4060 (glgE) ──┤ ├── PP_4059 (treS–mak) ──┤├── PP_4058 (glgB) ──
     4583598..4585583      4580107..4583427          4577900..4580110
                                          ▲ stop–start overlap ▲
```

### The GlgB catalytic step in detail

GlgB acts only once its substrate is long enough (DP ≥ ~16). Within its (β/α)₈ TIM-barrel active site, the catalytic nucleophile **Asp417** attacks an internal α-1,4 glucosidic bond of a donor chain, forming a covalent glycosyl–enzyme intermediate while **Glu470** acts as the general acid/base. The excised oligosaccharide segment is then transferred — by strictly intrachain transfer — onto the C6 hydroxyl of a glucose unit, creating a new α-1,6 branch point (a "C chain"). The net result is the conversion of a mostly linear polymer into a branched, glycogen-like α-glucan. The chain-length selectivity ensures branches are only installed on adequately elongated chains, giving glycogen its regular, densely branched architecture and keeping the polymer soluble and osmotically inert as a carbon/energy store.

### Localization and physiological role

All evidence points to a **soluble, cytoplasmic** localization: no signal peptide or transmembrane region, and the substrate (intracellular α-glucan/glycogen) is a cytoplasmic storage polymer. GlgB's role is architectural — it does not synthesize the glucan backbone (that is GlgE, and to some extent GlgA) but determines the branched structure of the final product. In mycobacteria the analogous pathway feeds both intracellular glycogen and extracellular capsular α-glucan; in *P. putida* the operonic *treS-mak/glgE/glgB* cluster and the absence of GlgC most parsimoniously indicate a role in cytoplasmic glycogen/α-glucan carbon storage, with GlgB defining polymer branching.

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports this report |
|---|---|---|
| [20444687](https://pubmed.ncbi.nlm.nih.gov/20444687/) | *Crystal structure of full-length M. tuberculosis GlgB* | Defines the branching reaction (cleave α-1,4, form α-1,6), GH13 family membership, the four-domain architecture, and the central (β/α)₈ catalytic domain — the structural template for Q88FN1. |
| [26280198](https://pubmed.ncbi.nlm.nih.gov/26280198/) | *Crystal structures of E. coli branching enzyme with linear oligosaccharides* | Establishes the dual α-1,4-amylase / α-1,6-transferase activity, substrate-length selectivity (no reaction on short glucans), and that BE is responsible for all glycogen branching. |
| [27221142](https://pubmed.ncbi.nlm.nih.gov/27221142/) | *Assembly of α-glucan by GlgE and GlgB in mycobacteria and streptomycetes* | Quantifies the ~DP16 minimum donor length and the strictly intrachain transfer mechanism; directly links GlgE elongation to GlgB branching. |
| [25148856](https://pubmed.ncbi.nlm.nih.gov/25148856/) | *Phylogenomic analysis of branching/debranching duo* | Places branching enzymes in LUCA; clarifies GlgB and eukaryotic GBE1 are paralogs — validates ortholog-based inference. |
| [11208782](https://pubmed.ncbi.nlm.nih.gov/11208782/) | *Rhizobium tropici glycogen synthase mutants* | Documents the conserved bacterial *glg* operon organization in which *glgB* sits with the other glycogen-metabolism genes. |
| [23901909](https://pubmed.ncbi.nlm.nih.gov/23901909/) | *TreS–Pep2 complex initiating α-glucan synthesis* | Defines the four-step cytoplasmic GlgE pathway (TreS, Pep2/Mak, GlgE, GlgB) that produces branched α-glucan — the pathway whose genes flank *glgB* in *P. putida*. |
| [27513637](https://pubmed.ncbi.nlm.nih.gov/27513637/) | *Metabolic network for intra-/extracellular α-glucans in M. tuberculosis* | States explicitly that GlgB branches the linear α-glucan made by GlgE from maltose-1-phosphate. |
| [20305657](https://pubmed.ncbi.nlm.nih.gov/20305657/) | *Self-poisoning of M. tuberculosis by targeting GlgE* | Confirms the four-step TreS–Pep2–GlgE–GlgB pathway architecture mirrored by the *P. putida glgB-treS-glgE* cluster. |
| [21493662](https://pubmed.ncbi.nlm.nih.gov/21493662/) | *Crystal structure of rice BEI* | Independent confirmation of the modular CBM48 + central α-amylase + C-domain architecture and the nucleophile/acid-base catalytic pair, generalizing the mechanism across kingdoms. |

Supporting/contextual literature reviewed but not directly cited for primary claims includes structural and mechanistic studies of cyanobacterial branching enzymes ([PMID: 28193843](https://pubmed.ncbi.nlm.nih.gov/28193843/), [PMID: 33662318](https://pubmed.ncbi.nlm.nih.gov/33662318/)), GH57-type archaeal branching enzymes ([PMID: 28163025](https://pubmed.ncbi.nlm.nih.gov/28163025/), [PMID: 31190240](https://pubmed.ncbi.nlm.nih.gov/31190240/)), cyanobacterial glycogen-synthesis modelling ([PMID: 41631621](https://pubmed.ncbi.nlm.nih.gov/41631621/)), and the TreS:Pep2 complex structure ([PMID: 30877199](https://pubmed.ncbi.nlm.nih.gov/30877199/)). These reinforce the conserved branching mechanism and pathway context but are less specific to *P. putida* GlgB.

**Consistency of the evidence:** Every line of evidence — UniProt/HAMAP annotation, InterPro domain signatures, ortholog crystal structures, phylogenomics, KEGG pathway assignment, genome-neighborhood analysis, and the AlphaFold model — converges on the same conclusion. No contradictory evidence or gene-identity ambiguity was found.

---

## Limitations and Knowledge Gaps

1. **No *P. putida*–specific biochemistry.** There is, to our knowledge, no direct in vitro enzymological characterization of the Q88FN1 protein itself (no purified-enzyme kinetics, no measured branch-length distribution, no crystal structure). All mechanistic and kinetic parameters (dual activity, catalytic residues, ~DP16 selectivity, intrachain transfer) are **inferred from characterized orthologs** (*E. coli*, *M. tuberculosis*, *Streptomyces*, rice) via strong sequence/structure homology. The catalytic residue positions (Asp417, Glu470) are assigned from conserved GH13 motifs, not from a solved *P. putida* structure.

2. **Pathway operation inferred from genomics.** The assignment of GlgB to the GlgE pathway rests on genome-neighborhood/operon analysis and the absence of *glgC*, combined with mycobacterial pathway biochemistry. Direct transcriptomic (operon confirmation by RT-PCR/RNA-seq) and metabolic-flux evidence in *P. putida* KT2440 has not been established here.

3. **Physiological role and regulation unquantified.** The conditions under which *P. putida* accumulates α-glucan, the relative contributions of the GlgE pathway vs. the residual GlgA (PP_4050) route, and the regulation of the *glgB-treS-glgE* operon remain uncharacterized. Whether the product is purely intracellular storage glycogen or also contributes to extracellular/capsular glucan (as in mycobacteria) is unknown for *P. putida*.

4. **GlgC absence — interpretation caveat.** The lack of a GlgC hit is based on KEGG orthology; a highly divergent or non-canonical ADP-glucose pyrophosphorylase cannot be entirely excluded without experimental confirmation. However, the presence of the full TreS–Mak–GlgE–GlgB set makes the GlgE-pathway interpretation robust regardless.

5. **AlphaFold confidence ≠ functional proof.** The very high pLDDT confirms fold reliability but does not by itself demonstrate catalytic activity, substrate specificity, or active-site geometry under physiological conditions.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant expression and enzymatic assay.** Express Q88FN1 in *E. coli*, purify, and assay branching activity on defined linear α-1,4-glucans. Measure the minimum chain length required for branching and the transferred branch-length distribution (e.g., by isoamylase debranching + HPAEC-PAD) to confirm the ~DP16 selectivity and characterize product architecture specific to *P. putida*.

2. **Active-site mutagenesis.** Generate D417A and E470A (and D417N/E470Q) variants and confirm loss of branching activity, experimentally validating the catalytic nucleophile / acid-base assignments inferred from GH13 motifs.

3. **Operon confirmation.** Use RT-PCR or RNA-seq across the PP_4058–PP_4060 region to confirm co-transcription of *glgB*, *treS-mak*, and *glgE*, and map the transcription start site and any internal promoters.

4. **Gene-deletion phenotyping.** Construct a clean ΔglgB (ΔPP_4058) mutant and compare intracellular α-glucan content and structure (branch frequency, chain-length profile) with wild type. Combine with ΔglgE and ΔtreS deletions to establish pathway epistasis and confirm that GlgB acts downstream of GlgE.

5. **Structural determination.** Solve the crystal or cryo-EM structure of *P. putida* GlgB, ideally in complex with linear oligosaccharide substrates/mimics (as done for the *E. coli* enzyme), to directly visualize the active site, surface binding sites, and the role of the N-terminal β-sandwich and CBM48 modules in substrate engagement.

6. **Physiological triggers of α-glucan accumulation.** Determine under which growth/stress conditions (carbon excess, stationary phase, osmotic or oxidative stress) *P. putida* accumulates branched α-glucan and how *glgB*/GlgE-pathway expression responds, clarifying the storage vs. protective role of the polymer.

7. **Test GlgC absence directly.** Assay for ADP-glucose pyrophosphorylase activity in cell extracts, or perform a sensitive homology/HMM search, to confirm that the classical ADP-glucose route is genuinely absent and that the GlgE pathway is the dominant route to branched α-glucan.

---

## Conclusion

*glgB* (Q88FN1, PP_4058) of *Pseudomonas putida* KT2440 encodes the cytoplasmic **1,4-α-glucan branching enzyme GlgB** (EC 2.4.1.18), a GH13-family enzyme with the canonical four-module architecture (N-terminal GlgB β-sandwich, CBM48, central (β/α)₈ catalytic TIM-barrel with catalytic Asp417/Glu470, and a C-terminal β-sandwich; AlphaFold pLDDT 96). It installs α-1,6 branch points into long linear α-1,4-glucan chains via a dual α-1,4-cleavage / α-1,6-transfer mechanism, acting only on sufficiently elongated chains. In *P. putida* KT2440 it is the terminal branch-forming step of the **cytoplasmic GlgE pathway**, operonically linked to *treS/mak* (PP_4059) and *glgE* (PP_4060), branching the maltose-1-phosphate–derived α-glucan produced by GlgE — the organism lacking the classical ADP-glucose pyrophosphorylase GlgC. The identity, function, localization, and pathway context are all consistent and well supported, with the principal remaining gaps being the absence of direct in vitro and genetic characterization of the *P. putida* enzyme itself.


## Artifacts

- [OpenScientist final report](glgB-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](glgB-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:20444687
2. PMID:26280198
3. PMID:27221142
4. PMID:11208782
5. PMID:25148856
6. PMID:23901909
7. PMID:27513637
8. PMID:20305657
9. PMID:21493662
10. PMID:28193843
11. PMID:33662318
12. PMID:28163025
13. PMID:31190240
14. PMID:41631621
15. PMID:30877199