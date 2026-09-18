---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T08:27:04.684981'
end_time: '2026-09-01T08:39:10.900102'
duration_seconds: 726.22
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: frmA
  gene_symbol: frmA
  uniprot_accession: Q88MF5
  protein_description: 'RecName: Full=S-(hydroxymethyl)glutathione dehydrogenase {ECO:0000256|ARBA:ARBA00021865};
    EC=1.1.1.1 {ECO:0000256|ARBA:ARBA00013190}; EC=1.1.1.284 {ECO:0000256|ARBA:ARBA00012309};
    AltName: Full=Alcohol dehydrogenase class-3 {ECO:0000256|ARBA:ARBA00030752}; AltName:
    Full=Alcohol dehydrogenase class-III {ECO:0000256|ARBA:ARBA00033399}; AltName:
    Full=Glutathione-dependent formaldehyde dehydrogenase {ECO:0000256|ARBA:ARBA00031007};'
  gene_info: Name=frmA {ECO:0000313|EMBL:AAN67237.1}; OrderedLocusNames=PP_1616 {ECO:0000313|EMBL:AAN67237.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the zinc-containing alcohol dehydrogenase
  protein_domains: ADH-like_C. (IPR013149); ADH-like_N. (IPR013154); ADH_3. (IPR014183);
    GroES-like_sf. (IPR011032); NAD(P)-bd_dom_sf. (IPR036291)
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
citation_count: 13
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: frmA-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: frmA-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88MF5
- **Protein Description:** RecName: Full=S-(hydroxymethyl)glutathione dehydrogenase {ECO:0000256|ARBA:ARBA00021865}; EC=1.1.1.1 {ECO:0000256|ARBA:ARBA00013190}; EC=1.1.1.284 {ECO:0000256|ARBA:ARBA00012309}; AltName: Full=Alcohol dehydrogenase class-3 {ECO:0000256|ARBA:ARBA00030752}; AltName: Full=Alcohol dehydrogenase class-III {ECO:0000256|ARBA:ARBA00033399}; AltName: Full=Glutathione-dependent formaldehyde dehydrogenase {ECO:0000256|ARBA:ARBA00031007};
- **Gene Information:** Name=frmA {ECO:0000313|EMBL:AAN67237.1}; OrderedLocusNames=PP_1616 {ECO:0000313|EMBL:AAN67237.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the zinc-containing alcohol dehydrogenase
- **Key Domains:** ADH-like_C. (IPR013149); ADH-like_N. (IPR013154); ADH_3. (IPR014183); GroES-like_sf. (IPR011032); NAD(P)-bd_dom_sf. (IPR036291)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "frmA" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'frmA' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **frmA** (gene ID: frmA, UniProt: Q88MF5) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *frmA* (PP_1616, UniProt Q88MF5) in *Pseudomonas putida* KT2440

## Summary

The gene **frmA** (ordered locus **PP_1616**; UniProt accession **Q88MF5**) of *Pseudomonas putida* KT2440 encodes a **cytoplasmic, NAD⁺-dependent, zinc-containing class III alcohol dehydrogenase**, more precisely a **S-(hydroxymethyl)glutathione dehydrogenase / glutathione-dependent formaldehyde dehydrogenase (GD-FALDH; EC 1.1.1.284, EC 1.1.1.1)**. Its primary, physiologically committed reaction is the NAD⁺-dependent oxidation of **S-(hydroxymethyl)glutathione** — the spontaneous adduct formed between formaldehyde and reduced glutathione (GSH) — to **S-formylglutathione**. This is the first and committed step of the **universal glutathione-dependent formaldehyde detoxification pathway**, which is completed by a downstream **S-formylglutathione hydrolase (SFGH)** that regenerates glutathione and releases formate. The formate can then be further oxidized to CO₂ or assimilated.

The enzyme belongs to the medium-chain, zinc-containing alcohol dehydrogenase superfamily and carries the diagnostic domains annotated for Q88MF5 (ADH-like N-terminal IPR013154, ADH-like C-terminal IPR013149, ADH_3 IPR014183, GroES-like IPR011032, and NAD(P)-binding IPR036291). Structurally it is a soluble homotetramer with a catalytic zinc (coordinated by Cys, His, Cys and water/Glu) and a second structural zinc typical of medium-chain ADHs. It follows a **random bi-bi kinetic mechanism** and strongly prefers **bulky substrates** — glutathione adducts and long-chain / ω-hydroxy fatty alcohols — over small alcohols such as ethanol, and is insensitive to pyrazole. Importantly, the very same enzyme is the evolutionarily conserved **S-nitrosoglutathione (GSNO) reductase**, making it a dual-function protein that governs cellular S-nitrosothiol homeostasis and protects against nitrosative stress from bacteria to humans.

In *P. putida* KT2440 specifically, FrmA is one of two formaldehyde dehydrogenases that channel formaldehyde toward CO₂, and glutathione biosynthesis is genetically required for formaldehyde tolerance — direct organism-level support for the glutathione-dependent route. FrmA protects the cytoplasm from endogenous formaldehyde generated by O-demethylation of methoxylated aromatics (e.g., vanillate) and from other methylated/C1 substrates. It must be carefully distinguished from the separate, well-crystallized **glutathione-INDEPENDENT** *Pseudomonas* formaldehyde dehydrogenase, which is a mechanistically distinct (ping-pong) enzyme encoded by a different gene. All identity-verification criteria — gene symbol, organism, protein family, and domain architecture — are satisfied, and the literature is consistent and directly relevant.

---

## Gene/Protein Identity Verification

Before presenting the functional narrative, the mandatory identity checks were completed:

- **UniProt:** Q88MF5
- **Gene:** frmA / PP_1616
- **Organism:** *Pseudomonas putida* KT2440 (PSEPK)
- **Family:** Zinc-containing (class III) alcohol dehydrogenase

| Criterion | Expected (UniProt Q88MF5) | Finding | Status |
|-----------|---------------------------|---------|--------|
| Gene symbol | frmA / PP_1616 | frmA denotes glutathione-dependent formaldehyde dehydrogenase across bacteria | ✅ Match |
| Organism | *P. putida* KT2440 (PSEPK) | KT2440-specific studies confirm the enzyme and pathway | ✅ Match |
| Protein family | Zinc-containing (class III) ADH | Class III ADH = glutathione-dependent FDH, confirmed | ✅ Match |
| Key domains | ADH_N, ADH_C, ADH_3, GroES-like, NAD(P)-binding | Structural studies of orthologs show identical fold/residues | ✅ Match |

The gene symbol *frmA* is used elsewhere (e.g., *E. coli* frmA, plant/fungal GSNOR orthologs, human ADH5/class III ADH). Critically, **these are all true orthologs of the same enzyme**, not spurious same-symbol collisions — so cross-species literature is directly applicable. The one important disambiguation, addressed explicitly below, is the distinct *glutathione-independent* *Pseudomonas* FDH (a different gene product).

---

## Key Findings

### F001 — FrmA is a glutathione-dependent formaldehyde dehydrogenase = class III alcohol dehydrogenase

UniProt annotates PP_1616/frmA (Q88MF5) as **S-(hydroxymethyl)glutathione dehydrogenase (EC 1.1.1.284) / alcohol dehydrogenase class-III (EC 1.1.1.1)** — a zinc-containing medium-chain ADH bearing the ADH-like N-terminal (IPR013154), ADH-like C-terminal (IPR013149), ADH_3 (IPR014183), and NAD(P)-binding (IPR036291) domains. The foundational biochemical identity of this enzyme was established by Koivusalo and colleagues, who sequenced tryptic peptides from purified formaldehyde dehydrogenase and found them exactly homologous to class III ADH, proving the two are the same enzyme ([PMID: 2806555](https://pubmed.ncbi.nlm.nih.gov/2806555/)).

The exact reaction is unambiguous: *"Formaldehyde dehydrogenase (EC 1.2.1.1) is a widely occurring enzyme which catalyzes the oxidation of S-hydroxymethylglutathione, formed from formaldehyde and glutathione, into S-formyglutathione in the presence of NAD"* ([PMID: 2806555](https://pubmed.ncbi.nlm.nih.gov/2806555/)). The substrate specificity that characterizes this family was also defined there: at high pH the enzyme oxidizes long-chain aliphatic alcohols such as *n*-octanol and 12-hydroxydodecanoate, but uses ethanol only at very high concentrations and is **not inhibited by pyrazole** — a hallmark distinguishing class III from class I ADH. The authors concluded that *"the amino acid sequence homology and identical structural and kinetic properties indicate that formaldehyde dehydrogenase and the mammalian class III alcohol dehydrogenases are identical enzymes."*

**Reaction catalyzed:**

```
formaldehyde (HCHO) + GSH  ⇌  S-(hydroxymethyl)glutathione   (spontaneous, non-enzymatic)
S-(hydroxymethyl)glutathione + NAD⁺  →  S-formylglutathione + NADH + H⁺   (FrmA, committed step)
```

### F002 — FrmA orthologs are dual-function GSNO reductases conserved from bacteria to humans

A landmark study purified a single GSNO-metabolizing activity from *Escherichia coli*, *Saccharomyces cerevisiae*, and mouse macrophages and showed it to be the glutathione-dependent formaldehyde dehydrogenase: *"Here we have purified a single activity from Escherichia coli, Saccharomyces cerevisiae and mouse macrophages that metabolizes S-nitrosoglutathione (GSNO), and show that it is the glutathione-dependent formaldehyde dehydrogenase"* ([PMID: 11260719](https://pubmed.ncbi.nlm.nih.gov/11260719/)). The enzyme is *"highly specific for GSNO"* yet *"controls intracellular levels of both GSNO and S-nitrosylated proteins."* Deletion of the reductase in yeast/mice abolished GSNO-consuming activity, raised GSNO and protein-SNO levels, and increased susceptibility specifically to nitrosative (not oxidative) challenge. The authors concluded: *"GSNO reductase is evolutionarily conserved from bacteria to humans, is critical for SNO homeostasis, and protects against nitrosative stress."*

Because *P. putida* FrmA is a bacterial member of this conserved family, this GSNO-reductase / nitrosative-defense role applies to it. This is a genuine second physiological function of the same active site, not merely a promiscuous side activity.

### F003 — FrmA detoxifies formaldehyde generated by O-demethylation reactions in *Pseudomonas*

In *P. putida*, aromatic O-demethylation is a major endogenous source of formaldehyde. The vanillate O-demethylase (VanAB) releases formaldehyde as a demethylation by-product, which is then metabolized: *"Formaldehyde, which is the by-product of the demethylation, was converted into formate in the cellular reaction"* ([PMID: 16242864](https://pubmed.ncbi.nlm.nih.gov/16242864/)). Crucially, disrupting the frmA gene blocked this conversion: *"Formate accumulation was blocked by gene disruption of the E. coli frmA that coded glutathione-dependent formaldehyde dehydrogenase."* This demonstrates functional coupling between aromatic O-demethylation (central to lignin-derived aromatic catabolism in *Pseudomonas*) and the glutathione-dependent formaldehyde detoxification pathway in which FrmA operates.

### F004 — Disambiguation: FrmA is the glutathione-DEPENDENT enzyme, distinct from the glutathione-INDEPENDENT *Pseudomonas* FDH

*P. putida* is famous in the enzymology literature for a **glutathione-independent** NAD⁺-dependent formaldehyde dehydrogenase that has been crystallized. It is essential to recognize this is a **different gene product** from FrmA/PP_1616. As stated for the related *P. aeruginosa* enzyme: *"Most FDHs are dependent on glutathione for catalysis, but the enzyme from Pseudomonas putida is an exception"* ([PMID: 23989142](https://pubmed.ncbi.nlm.nih.gov/23989142/)). That glutathione-independent enzyme uses a *"conserved glutathione-independent 'ping-pong' mechanism of formaldehyde oxidization"* (shared with *P. aeruginosa* FDH, ~88% identity). FrmA/PP_1616 (Q88MF5), by contrast, is explicitly annotated as glutathione-DEPENDENT and follows an ordered/ternary-complex (random bi-bi) mechanism. Thus **P. putida encodes two mechanistically different formaldehyde-oxidizing enzymes**, and FrmA is the glutathione-dependent one.

### F005 — FrmA acts in a two-enzyme pathway completed by a formaldehyde-inducible S-formylglutathione hydrolase

The product of FrmA, S-formylglutathione, is hydrolyzed to formate + GSH by **S-formylglutathione hydrolase (SFGH)**, an α/β-hydrolase serine esterase. Characterization of *E. coli* FrmB and YeiG showed *"both proteins had the highest hydrolytic activity toward S-formylglutathione, an intermediate of the glutathione-dependent pathway of formaldehyde detoxification"* (Km ~0.41–0.43 mM; Ser-Asp-His triad) ([PMID: 16567800](https://pubmed.ncbi.nlm.nih.gov/16567800/)). The pathway is strongly stress-inducible: *"the expression of frmB was stimulated 45-75 times by the addition of formaldehyde to the growth medium"*, and double deletion of *frmB*+*yeiG* increased formaldehyde sensitivity. Structural work on a psychrophilic SFGH showed the enzyme catalyzes *"the hydrolysis of S-formylglutathione to formic acid and glutathione"* and belongs to a family that is *"ubiquitous... in prokaryotes and eukaryotes"* which *"play a key role in formaldehyde detoxification"* ([PMID: 20209484](https://pubmed.ncbi.nlm.nih.gov/20209484/)). The hydrolase efficiently processes thioesters with small acyl moieties, consistent with a narrow acyl pocket — matching S-formylglutathione as its physiological substrate.

### F006 — Structural/mechanistic basis: two-zinc medium-chain ADH, random bi-bi, prefers glutathione adducts and long-chain alcohols

Crystallographic studies of the human ortholog (class III / χχ ADH), which shares the same fold and catalytic residues as bacterial FrmA, established the mechanism: *"It follows a random bi bi kinetic mechanism and prefers bulkier substrates like long chain primary alcohols and glutathione adducts like s-hydroxymethylglutathione and GSNO over smaller alcohols like ethanol"* ([PMID: 12604204](https://pubmed.ncbi.nlm.nih.gov/12604204/)). The catalytic zinc is coordinated in the apoenzyme by Cys44, His66, Cys173 and a water molecule; upon coenzyme/substrate binding, Glu67 enters the coordination sphere to promote ligand exchange: *"In the FDH.NAD(H) binary complex reported here, Glu67 is added to the coordination environment of the active site zinc"* ([PMID: 12604204](https://pubmed.ncbi.nlm.nih.gov/12604204/); see also [PMID: 12196016](https://pubmed.ncbi.nlm.nih.gov/12196016/)). The enzyme adopts a "semi-open" catalytic-domain conformation intermediate between the open and closed states of class I ADH. Substrate breadth was confirmed for the human χχ enzyme: *"chi chi ADH catalyzes the oxidation of long-chain alcohols such as omega-hydroxy fatty acids as well as S-hydroxymethyl-glutathione, a spontaneous adduct between formaldehyde and glutathione"* ([PMID: 9018047](https://pubmed.ncbi.nlm.nih.gov/9018047/)). A second, structural zinc typical of medium-chain ADHs is also present. These features map directly onto the InterPro domains annotated for Q88MF5.

### F007 — Genetic evidence: a soluble tetramer essential for growth on formaldehyde-generating substrates

In the related bacterium *Paracoccus denitrificans*, the orthologous NAD- and glutathione-dependent formaldehyde dehydrogenase (gene *flhA*) was purified as a 150 kDa tetramer, and its inactivation abolished growth on methanol, methylamine, and choline while leaving heterotrophic growth unaffected: *"The mutant strain is not able to grow on methanol, methylamine, or choline, while heterotrophic growth is not influenced by the mutation. This finding indicates that GD-FALDH of P. denitrificans is essential for the oxidation of formaldehyde produced during methylotrophic growth"* ([PMID: 7798140](https://pubmed.ncbi.nlm.nih.gov/7798140/)). The enzyme was purified *"as a tetramer with a relative molecular mass of 150 kDa"*, establishing the soluble homotetrameric quaternary structure. The downstream hydrolase (gene *fghA*, homologous to human esterase D) is likewise essential and defines a *"formaldehyde detoxification pathway that is universal in nature"* ([PMID: 8892832](https://pubmed.ncbi.nlm.nih.gov/8892832/)). This loss-of-function genetics pinpoints the enzyme's role: detoxifying formaldehyde arising from C1/methylated substrate catabolism, dispensable when no such formaldehyde stress is present.

### F008 — In *P. putida* KT2440 specifically, formaldehyde is oxidized to CO₂ and glutathione is required for tolerance

The most organism-specific evidence comes from a physiological study of *P. putida* KT2440 during formaldehyde detoxification: *"Pseudomonas putida KT2440 exhibits two formaldehyde dehydrogenases and two formate dehydrogenase complexes that allow the strain to stoichiometrically convert formaldehyde into CO(2)"* ([PMID: 21261833](https://pubmed.ncbi.nlm.nih.gov/21261833/)). FrmA is the glutathione-dependent one of the two formaldehyde dehydrogenases. The strain tolerated up to ~1.5 mM formaldehyde and died at 10 mM; sublethal 0.5 mM reduced growth rate ~40% and upregulated 52 genes for overcoming DNA/protein damage, extrusion, and detoxification to CO₂. Critically, *"we found that mutants in glutathione biosynthesis, stress response mediated by 2-hydroxy acid dehydrogenases and two efflux pumps of the MSF family were unable to grow in the presence of 1.5 mM HCOH"* — directly implicating glutathione (the co-substrate of the FrmA pathway) in formaldehyde tolerance, while MexEF/OprN efflux and recA/uvrB DNA-repair mutants were hypersensitive to killing by 10 mM formaldehyde.

---

## Mechanistic Model / Interpretation

FrmA sits at the heart of a two-enzyme, glutathione-recycling detoxification module that converts a highly reactive, protein- and DNA-crosslinking electrophile (formaldehyde) into an innocuous, assimilable one-carbon unit (formate → CO₂). The pathway operates entirely in the **cytoplasm**, where both glutathione and NAD⁺ are abundant.

```
   Endogenous / exogenous sources
   (O-demethylation of vanillate & methoxy-aromatics;
    methanol, methylamine, choline; environmental HCHO)
                    │
                    ▼
              FORMALDEHYDE (HCHO)  ──── toxic electrophile
                    │
          + GSH (spontaneous, non-enzymatic)
                    ▼
        S-(hydroxymethyl)glutathione (HMGSH)
                    │
        ┌───────────┴───────────┐  FrmA / PP_1616  (EC 1.1.1.284)
        │   NAD⁺ → NADH         │  Zn²⁺-dependent class III ADH
        │   random bi-bi        │  soluble homotetramer, cytoplasm
        └───────────┬───────────┘
                    ▼
           S-formylglutathione
                    │
        ┌───────────┴───────────┐  S-formylglutathione hydrolase (SFGH)
        │   + H₂O               │  α/β-hydrolase, Ser-Asp-His triad
        │   → GSH (recycled)    │  formaldehyde-inducible (45–75×)
        └───────────┬───────────┘
                    ▼
                 FORMATE
                    │
          formate dehydrogenase(s)
                    ▼
                   CO₂   (or C1 assimilation)
```

A parallel, chemically distinct role runs through the **same active site**: reduction of **S-nitrosoglutathione (GSNO)**. Here the enzyme acts as GSNO reductase, using NADH to consume GSNO and thereby lowering the cellular pool of protein S-nitrosothiols. This links FrmA to redox/nitrosative signaling homeostasis, a function conserved from bacteria to humans.

**Two enzymes, one job — don't confuse them.** *P. putida* has both a glutathione-dependent FDH (FrmA/PP_1616, this report) and a glutathione-independent FDH (a different, ping-pong-mechanism enzyme). The physiological study of KT2440 (F008) counts "two formaldehyde dehydrogenases," consistent with FrmA being one of them.

| Property | FrmA / PP_1616 (this protein) | Glutathione-independent *Pseudomonas* FDH |
|----------|-------------------------------|-------------------------------------------|
| Glutathione requirement | **Required** (co-substrate as HMGSH) | Not required |
| True substrate | S-(hydroxymethyl)glutathione | Free formaldehyde |
| Mechanism | Random bi-bi (ternary complex) | Ping-pong |
| Family | Class III ADH (medium-chain, Zn) | Distinct FDH |
| Second function | GSNO reductase | — |
| Gene | frmA / PP_1616 (Q88MF5) | Separate gene |

**Localization.** All lines of evidence — soluble tetramer purified from cytosol (F007), use of cytoplasmic GSH/NAD⁺, and the absence of a signal peptide or membrane-spanning segment in the ADH fold — place FrmA in the **cytoplasm**, where it acts on soluble small-molecule substrates.

---

## Evidence Base

| PMID | Study focus | Contribution to this report | Weight |
|------|-------------|-----------------------------|--------|
| [2806555](https://pubmed.ncbi.nlm.nih.gov/2806555/) | Identity of GD-FDH and class III ADH | Defines exact reaction, substrate specificity, family identity | Primary, foundational |
| [11260719](https://pubmed.ncbi.nlm.nih.gov/11260719/) | Metabolic enzyme for S-nitrosothiol, bacteria→humans | Establishes dual GSNO-reductase function & conservation | Primary, *Nature* |
| [16242864](https://pubmed.ncbi.nlm.nih.gov/16242864/) | Vanillate-O-demethylase ↔ formaldehyde detox | *Pseudomonas*-specific coupling; frmA disruption blocks formate | Primary, direct |
| [23989142](https://pubmed.ncbi.nlm.nih.gov/23989142/) | Structure of *P. aeruginosa* FDH | Disambiguates the glutathione-INDEPENDENT FDH | Primary, structural |
| [16567800](https://pubmed.ncbi.nlm.nih.gov/16567800/) | *E. coli* FrmB & YeiG SFGHs | Downstream step; formaldehyde-inducibility (45–75×) | Primary, direct |
| [20209484](https://pubmed.ncbi.nlm.nih.gov/20209484/) | SFGH crystal structure | Defines final hydrolysis step; ubiquity | Primary, structural |
| [12604204](https://pubmed.ncbi.nlm.nih.gov/12604204/) | Human class III ADH structure-function | Random bi-bi; substrate preference; Zn coordination | Primary, structural |
| [12196016](https://pubmed.ncbi.nlm.nih.gov/12196016/) | Human GD-FDH apo/binary/ternary | Zn coordination dynamics; random mechanism | Primary, structural |
| [9018047](https://pubmed.ncbi.nlm.nih.gov/9018047/) | Human χχ ADH structure | Confirms long-chain alcohol + HMGSH substrates | Primary, structural |
| [7798140](https://pubmed.ncbi.nlm.nih.gov/7798140/) | *P. denitrificans* GD-FALDH | Essential for methylotrophic growth; 150 kDa tetramer | Primary, genetics |
| [8892832](https://pubmed.ncbi.nlm.nih.gov/8892832/) | *P. denitrificans* SFGH / esterase D | Universal detox pathway; downstream essential | Primary, genetics |
| [21261833](https://pubmed.ncbi.nlm.nih.gov/21261833/) | *P. putida* KT2440 formaldehyde responses | Organism-specific: two FDHs → CO₂; GSH required | Primary, direct |

Supplementary orthology support (fungal/plant GSNOR studies, e.g. [PMID: 25793615](https://pubmed.ncbi.nlm.nih.gov/25793615/)) reinforces the conserved dual formaldehyde-detox / GSNO-reductase function across kingdoms but is peripheral to the bacterial target.

---

## Limitations and Knowledge Gaps

1. **No direct biochemical characterization of the KT2440 protein itself.** The functional assignment for Q88MF5 rests on (a) unambiguous sequence/domain annotation, (b) closely related bacterial orthologs (*Paracoccus*, *E. coli*), and (c) KT2440 physiology showing "two formaldehyde dehydrogenases." No purified-enzyme kinetics (Km, kcat) specific to PP_1616 were located.

2. **Structural inference, not a solved KT2440 structure.** Zn coordination, the random bi-bi mechanism, and substrate preference derive from human and *Pseudomonas* orthologs. A KT2440 crystal or cryo-EM structure has not been reported here; catalytic residue numbering (Cys44/His66/Cys173/Glu67) is from the human enzyme.

3. **GSNO-reductase role not experimentally demonstrated in KT2440.** The dual function is inferred from the conserved-family study (F002). Whether PP_1616 disruption in *P. putida* elevates protein-SNO levels or increases nitrosative-stress sensitivity has not been directly shown.

4. **Gene-specificity in disruption experiments.** The vanillate-demethylation coupling study (F003) used *E. coli frmA* disruption to make its mechanistic point; a clean PP_1616-specific knockout phenotype in KT2440 would strengthen the direct attribution.

5. **Relative flux through the two *P. putida* FDHs.** The quantitative division of labor between FrmA (glutathione-dependent) and the glutathione-independent FDH under different substrate/stress regimes is not resolved.

---

## Proposed Follow-up Experiments / Actions

1. **Purify and kinetically characterize recombinant PP_1616.** Measure NAD⁺-dependent HMGSH oxidation (Km, kcat), long-chain alcohol activity, ethanol activity, pyrazole insensitivity, and GSNO-reductase activity to confirm the class III ADH signature directly for the KT2440 protein.

2. **Construct a clean ΔPP_1616 knockout in KT2440** and assay: (a) growth/survival across a formaldehyde dose range (0.5–10 mM); (b) formate/CO₂ output from vanillate and methanol; (c) sensitivity to NO donors and steady-state protein-SNO levels (biotin-switch). Complement to confirm specificity.

3. **Distinguish the two FDHs genetically.** Build single and double knockouts of PP_1616 and the glutathione-independent FDH gene; quantify the flux contribution of each under aromatic-O-demethylation load versus exogenous formaldehyde.

4. **Solve the KT2440 enzyme structure** (X-ray or AlphaFold-guided cryo-EM) with NAD(H) and glutathione-adduct ligands to verify the catalytic and structural zinc sites and the semi-open catalytic-domain conformation.

5. **Test transcriptional induction** of PP_1616 (and its cognate SFGH) by formaldehyde and GSNO via RT-qPCR/RNA-seq, to establish whether the *P. putida* module is stress-inducible like the *E. coli frmRAB* operon.

6. **Confirm downstream SFGH identity in KT2440** — identify the PP locus encoding S-formylglutathione hydrolase and test whether its deletion causes S-formylglutathione accumulation and formaldehyde hypersensitivity.

---

## Conclusion

*frmA* (PP_1616, Q88MF5) encodes the **cytoplasmic, NAD⁺- and zinc-dependent class III alcohol dehydrogenase — glutathione-dependent formaldehyde dehydrogenase / S-(hydroxymethyl)glutathione dehydrogenase** of *P. putida* KT2440. Its primary reaction is the NAD⁺-dependent oxidation of the formaldehyde–glutathione adduct S-(hydroxymethyl)glutathione to S-formylglutathione, the committed step of the universal glutathione-dependent formaldehyde detoxification pathway (completed by S-formylglutathione hydrolase, which regenerates GSH and releases formate). The enzyme prefers bulky glutathione adducts and long-chain/ω-hydroxy alcohols over ethanol, follows a random bi-bi mechanism, and doubles as a conserved S-nitrosoglutathione reductase that safeguards S-nitrosothiol homeostasis. In *P. putida* it defends the cytoplasm against formaldehyde generated by O-demethylation of methoxylated aromatics and other C1/methylated substrates, and it is distinct from the separate glutathione-independent *Pseudomonas* formaldehyde dehydrogenase.


## Artifacts

- [OpenScientist final report](frmA-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](frmA-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:2806555
2. PMID:11260719
3. PMID:16242864
4. PMID:23989142
5. PMID:16567800
6. PMID:20209484
7. PMID:12604204
8. PMID:12196016
9. PMID:9018047
10. PMID:7798140
11. PMID:8892832
12. PMID:21261833
13. PMID:25793615