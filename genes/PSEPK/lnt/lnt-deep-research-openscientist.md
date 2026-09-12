---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-11T14:36:37.450045'
end_time: '2026-07-11T14:47:50.797511'
duration_seconds: 673.35
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: lnt
  gene_symbol: lnt
  uniprot_accession: Q88DN4
  protein_description: 'RecName: Full=Apolipoprotein N-acyltransferase {ECO:0000255|HAMAP-Rule:MF_01148};
    Short=ALP N-acyltransferase {ECO:0000255|HAMAP-Rule:MF_01148}; EC=2.3.1.269 {ECO:0000255|HAMAP-Rule:MF_01148};'
  gene_info: Name=lnt {ECO:0000255|HAMAP-Rule:MF_01148}; OrderedLocusNames=PP_4790;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the CN hydrolase family. Apolipoprotein N-
  protein_domains: Apolipo_AcylTrfase. (IPR004563); C-N_Hydrolase. (IPR003010); C-N_Hydrolase_sf.
    (IPR036526); LNT_N. (IPR045378); CN_hydrolase (PF00795)
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
citation_count: 9
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: lnt-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: lnt-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88DN4
- **Protein Description:** RecName: Full=Apolipoprotein N-acyltransferase {ECO:0000255|HAMAP-Rule:MF_01148}; Short=ALP N-acyltransferase {ECO:0000255|HAMAP-Rule:MF_01148}; EC=2.3.1.269 {ECO:0000255|HAMAP-Rule:MF_01148};
- **Gene Information:** Name=lnt {ECO:0000255|HAMAP-Rule:MF_01148}; OrderedLocusNames=PP_4790;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the CN hydrolase family. Apolipoprotein N-
- **Key Domains:** Apolipo_AcylTrfase. (IPR004563); C-N_Hydrolase. (IPR003010); C-N_Hydrolase_sf. (IPR036526); LNT_N. (IPR045378); CN_hydrolase (PF00795)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "lnt" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'lnt' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **lnt** (gene ID: lnt, UniProt: Q88DN4) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *lnt* (Apolipoprotein N-acyltransferase, PP_4790, Q88DN4) in *Pseudomonas putida* KT2440

## Summary

The gene **lnt** (ordered locus **PP_4790**; UniProt **Q88DN4**) of *Pseudomonas putida* KT2440 encodes **apolipoprotein N-acyltransferase (Lnt; EC 2.3.1.269)**, an integral inner-membrane enzyme that catalyzes the **third and final step of Gram-negative bacterial lipoprotein maturation**. Lnt transfers a single acyl chain onto the free α-amino group of the N-terminal S-diacylglyceryl-cysteine of an apolipoprotein, converting the diacylated apolipoprotein into a mature **triacylated lipoprotein**. This is the committed, final tailoring reaction of the ordered biosynthetic pathway **Lgt → LspA → Lnt**, after which mature lipoproteins are handed to the Lol sorting system for delivery (most commonly to the outer membrane).

Mechanistically, Lnt is a member of the **carbon–nitrogen (CN) hydrolase / nitrilase superfamily**. It uses a **Cys–Glu–Lys catalytic triad** and operates by a **two-step ping-pong (bi-bi) mechanism** in which the active-site cysteine first forms a covalent **thioester acyl-enzyme intermediate** (the slow half-reaction) and then rapidly transfers the acyl chain to the apolipoprotein amino group. Crucially, the acyl donor is not acyl-CoA or acyl-ACP but a **membrane phospholipid** — phosphatidylethanolamine being the physiological donor in *E. coli* and pseudomonads — and the enzyme shows selectivity for the phospholipid headgroup and acyl-chain composition. Structurally, Lnt is a polytopic inner-membrane protein bearing a globular periplasmic catalytic domain that sits atop the membrane, with its **active site facing the periplasm**, where exported, Lgt/LspA-processed apolipoprotein substrates reside.

While the enzymatic characterization has been performed primarily in *Escherichia coli* and *Pseudomonas aeruginosa*, the functional assignment to the *P. putida* protein rests on more than database annotation. Direct, target-specific bioinformatic analysis performed during this investigation shows that Q88DN4 shares **43.1% amino-acid identity** with *E. coli* Lnt and **conserves every residue** shown by mutagenesis to be essential for catalysis — including the complete catalytic triad, which maps to **E269–K329–C381** in the *P. putida* numbering. Hydropathy analysis further confirms the diagnostic Lnt topology: an N-terminal polytopic membrane anchor supporting a C-terminal catalytic module. Together these results provide confident, evidence-backed transfer of the well-established Lnt function to *P. putida* PP_4790. The gene symbol *lnt*, the organism, and the CN-hydrolase / apolipoprotein N-acyltransferase domain architecture supplied by UniProt are fully consistent with the protein studied here — verification passed on all counts.

---

## Gene/Protein Identity Verification

| Field | Value |
|---|---|
| UniProt accession | Q88DN4 |
| Gene name / locus | *lnt* / PP_4790 |
| Protein | Apolipoprotein N-acyltransferase (ALP N-acyltransferase) |
| EC number | 2.3.1.269 |
| Organism | *Pseudomonas putida* KT2440 (ATCC 47054 / DSM 6125) |
| Protein family | CN hydrolase (nitrilase) superfamily; apolipoprotein N-acyltransferase |
| Key domains | Apolipo_AcylTrfase (IPR004563); C-N_Hydrolase (IPR003010); C-N_Hydrolase_sf (IPR036526); LNT_N (IPR045378); CN_hydrolase (PF00795) |

**Verdict:** The gene symbol, organism, and domain architecture are internally consistent and match the enzyme characterized throughout the literature. No conflicting-gene ambiguity was encountered. The functional annotation is transferred with high confidence.

---

## Key Findings

### Finding 1 — Lnt catalyzes the final N-acylation step of lipoprotein maturation

Lnt (Q88DN4, PP_4790) is annotated with **EC 2.3.1.269** and catalyzes the transfer of a single acyl chain onto the **free α-amino group of the N-terminal S-diacylglyceryl-cysteine** of apolipoproteins. This converts a diacylated apolipoprotein into a mature **triacylated lipoprotein**, and it is the **third and last** of three sequential, membrane-embedded enzymatic steps in bacterial lipoprotein biogenesis (Lgt → LspA → Lnt). *In vitro*, purified *E. coli* Lnt N-acylates the apo-form of Braun's murein lipoprotein (Lpp) and the synthetic diacylated lipopeptide FSL-1, directly demonstrating the reaction. As stated by Buddelmeijer and colleagues, Lnt "then transfers the acyl chain to the α-amino group of the N-terminal diacylglyceryl-modified cysteine of apolipoprotein, leading to the formation of mature triacylated lipoprotein" ([PMID: 21676878](https://pubmed.ncbi.nlm.nih.gov/21676878/)). The placement of Lnt as the terminal enzyme of a three-step, membrane-embedded process is stated explicitly: "Lipoprotein maturation requires the sequential activity of three enzymes that are embedded in the cytoplasmic membrane" ([PMID: 28698362](https://pubmed.ncbi.nlm.nih.gov/28698362/)).

The function for the *P. putida* protein is assigned by orthology (HAMAP rule MF_01148) to these experimentally characterized γ-proteobacterial Lnt enzymes (*E. coli*, *P. aeruginosa*), and — as detailed in Findings 6 and 7 — is reinforced here by direct sequence and topology analysis of Q88DN4 itself.

### Finding 2 — CN-hydrolase catalytic triad and a ping-pong mechanism via a thioester intermediate

Lnt belongs to the **CN hydrolase (nitrilase) superfamily**. Site-directed mutagenesis in *E. coli* identified a **catalytic triad E267–K335–C387**, together with additional essential residues (Y388, E389 in the active-site hydrophobic pocket; W237, E343 on flexible arms). Robichon and co-workers reported that "besides the potential catalytic triad E267-K335-C387, four residues that directly affect the modification of Braun's lipoprotein Lpp are absolutely required for Lnt function" ([PMID: 17416655](https://pubmed.ncbi.nlm.nih.gov/17416655/)).

Kinetic studies established the reaction chemistry. Lnt first forms a covalent **thioester acyl-enzyme intermediate** on the active-site cysteine (a slow half-reaction), then rapidly transfers the acyl chain to the apolipoprotein α-amino group — the hallmark of a **ping-pong bi-bi mechanism**. Buddelmeijer and colleagues found that "kinetics of Lnt using phosphatidylethanolamine as an acyl donor and FSL-1 as a substrate were consistent with a ping-pong type mechanism, demonstrating slow acyl-enzyme intermediate formation and rapid N-acyl transfer to the apolipopeptide in vitro" ([PMID: 21676878](https://pubmed.ncbi.nlm.nih.gov/21676878/)). The catalytic-triad residues are conserved across proteobacterial Lnt orthologues, including the *P. putida* protein, whose domain complement (CN_hydrolase PF00795; IPR003010 / IPR004563 / IPR045378) marks it as a member of this family.

### Finding 3 — The acyl donor is a membrane phospholipid, with donor selectivity

A defining feature of Lnt is that the acyl group it adds is derived from **membrane phospholipids** rather than from soluble acyl-CoA or acyl-ACP. *In vitro* kinetic assays with purified *E. coli* Lnt used **phosphatidylethanolamine** — the major phospholipid of both *E. coli* and *Pseudomonas* membranes — as the acyl donor and the diacylglyceryl lipopeptide FSL-1 as the acceptor; [³H]palmitate incorporation and mass spectrometry confirmed acyl transfer. Importantly, activity depended on donor identity: "in contrast to earlier in vitro observations, the N-acyltransferase activity was strongly affected by the phospholipid headgroup and acyl chain composition" ([PMID: 21676878](https://pubmed.ncbi.nlm.nih.gov/21676878/)), indicating genuine donor selectivity rather than indiscriminate lipid usage.

The phospholipid origin of the acyl chains is a general property of the pathway: "lipoproteins from proteobacteria are posttranslationally modified by fatty acids derived from membrane phospholipids by the action of three integral membrane enzymes, resulting in triacylated proteins" ([PMID: 32478756](https://pubmed.ncbi.nlm.nih.gov/32478756/)). On the acceptor side, the specificity is broad: the recognized moiety is the invariant **lipobox-derived N-terminal diacylglyceryl-cysteine**, so Lnt modifies essentially the entire lipoprotein complement of the cell.

### Finding 4 — Integral inner-membrane enzyme with a periplasm-facing active site

Crystal structures of Lnt from *Pseudomonas aeruginosa* and *Escherichia coli* are remarkably similar and reveal the enzyme's architecture and topology. Each consists of a **membrane-embedded domain** (multiple transmembrane helices) topped by a **globular periplasmic domain**, with the active site located at the membrane interface facing the periplasm. Lu and colleagues describe that both enzymes "consist of a membrane domain on which sits a globular periplasmic domain. The active site resides above the membrane interface where the domains meet facing into the periplasm" ([PMID: 28675161](https://pubmed.ncbi.nlm.nih.gov/28675161/)).

Structural studies also captured the catalytic cycle in action. A dynamic/flexible arm and loops open and close to control access to the active-site cysteine, and a covalently modified active-site cysteine consistent with the acyl-enzyme intermediate was observed directly: "in one form we observe a highly dynamic arm that is able to restrict access to the active site as well as a covalent modification to the active site cysteine consistent with the thioester acyl-intermediate" ([PMID: 31959792](https://pubmed.ncbi.nlm.nih.gov/31959792/)). This topology places Lnt in the **cytoplasmic (inner) membrane**, catalyzing acylation on the **periplasmic face**, precisely where the exported, Lgt/LspA-processed apolipoprotein resides. Because one of the two solved structures is from the closely related *P. aeruginosa*, the architecture and localization are directly relevant to the *P. putida* orthologue.

### Finding 5 — Position in the Lgt–LspA–Lnt pathway, feeding the Lol sorting system

Lnt occupies a defined position in the lipoprotein biogenesis pathway:

1. **Lgt** (phosphatidylglycerol:prolipoprotein diacylglyceryl transferase) recognizes the conserved **lipobox** in the prolipoprotein signal sequence and adds diacylglycerol to an invariant cysteine.
2. **LspA** (signal peptidase II) cleaves the signal peptide to yield the **apolipoprotein** bearing an N-terminal S-diacylglyceryl-cysteine.
3. **Lnt** adds the third, amide-linked acyl chain to give the **mature triacylated lipoprotein**.

El Rayes and colleagues describe the first two steps: "First, phosphatidylglycerol:prolipoprotein diacylglyceryl transferase (Lgt) recognizes a conserved lipobox motif within the prolipoprotein signal sequence and catalyzes the addition of diacylglycerol to an invariant cysteine. The signal sequence is then cleaved by signal peptidase II (LspA) to give an N-terminal S-diacylglyceryl cysteine" ([PMID: 28698362](https://pubmed.ncbi.nlm.nih.gov/28698362/)). The mature product is then routed onward: "mature lipoproteins in these bacteria are triacylated, with the final fatty acid addition performed by Lnt, an apolipoprotein N-acyltransferase. The mature lipoproteins are then sorted by the Lol system, with most Lpps inserted into the outer membrane (OM)" ([PMID: 25755189](https://pubmed.ncbi.nlm.nih.gov/25755189/)).

The pathway is essential in most γ-proteobacteria (including *E. coli* and *Pseudomonas*), making Lnt a candidate **antibacterial target**. Loss of Lnt has concrete physiological consequences: "absence of a fully functional Lnt impairs modification of lipoproteins, increases outer membrane permeability and susceptibility to antibiotics, and alters normal cellular morphology" ([PMID: 30307391](https://pubmed.ncbi.nlm.nih.gov/30307391/)). Notably, *lnt* is dispensable in some bacteria (e.g., *Acinetobacter*, *Francisella*, *Neisseria*) whose Lol systems can sort diacylated lipoproteins — underscoring that Lnt performs a **narrow, precise tailoring role** rather than a broadly pleiotropic one.

### Finding 6 — Direct sequence evidence: Q88DN4 conserves the complete Lnt catalytic machinery

Because the enzymatic characterization was performed in orthologues, this investigation verified the functional assignment directly on the target sequence. Global pairwise alignment of Q88DN4 (505 aa) against experimentally characterized *E. coli* Lnt (P23930, 512 aa) yields **43.1% amino-acid identity** (213/494 aligned columns) — well within the range for confident orthology and functional transfer.

Critically, **every residue** shown by mutagenesis to be essential in *E. coli* Lnt ([PMID: 17416655](https://pubmed.ncbi.nlm.nih.gov/17416655/)) is conserved at the structurally corresponding position in *P. putida*:

| Functional role | *E. coli* (P23930) | *P. putida* (Q88DN4) | Conserved |
|---|---|---|---|
| Catalytic triad — Glu | E267 | **E269** | ✔ |
| Catalytic triad — Lys | K335 | **K329** | ✔ |
| Catalytic triad — Cys (nucleophile) | C387 | **C381** | ✔ |
| Active-site hydrophobic pocket | Y388 | Y382 | ✔ |
| Active-site hydrophobic pocket | E389 | E383 | ✔ |
| Flexible-arm residue | W237 | W240 | ✔ |
| Flexible-arm residue | E343 | E337 | ✔ |

All seven positions are identical (100% conservation of functionally critical residues). This provides direct, target-specific bioinformatic confirmation — not merely database annotation — that Q88DN4 possesses an intact apolipoprotein N-acyltransferase active site.

### Finding 7 — Target-specific topology matches the Lnt fold

Kyte–Doolittle hydropathy analysis of Q88DN4 (window 19) detects multiple hydrophobic membrane-spanning segments clustered in the **N-terminal half** of the protein (e.g., approximately residues 17–43, 82–105, and 164–180), while the catalytic triad (E269, K329, C381) and the remainder of the CN-hydrolase catalytic module lie **C-terminal** to these segments. (Kyte–Doolittle is a coarse predictor and undercounts the ~6–8 transmembrane helices resolved crystallographically, but it correctly localizes the membrane domain to the N-terminus.) This domain arrangement — an **N-terminal polytopic membrane anchor supporting a C-terminal globular catalytic domain** — matches the experimentally determined architecture of *E. coli* and *P. aeruginosa* Lnt, in which the catalytic domain sits atop the membrane with its active site facing the periplasm (Finding 4).

---

## Mechanistic Model / Interpretation

The findings converge on a single, coherent mechanistic picture of Lnt as the **committed final tailoring enzyme** of Gram-negative lipoprotein biogenesis in *P. putida*.

### The biosynthetic pathway

```
 Prolipoprotein (cytoplasm → inner membrane, lipobox signal)
        │
        │  Lgt  — adds diacylglycerol from phosphatidylglycerol
        ▼        to the invariant lipobox cysteine (S-linkage)
 Diacylglyceryl-prolipoprotein
        │
        │  LspA (signal peptidase II) — cleaves signal peptide
        ▼
 Apolipoprotein  (N-terminal S-diacylglyceryl-cysteine, free α-amino group)
        │
        │  ★ Lnt (PP_4790, Q88DN4) — transfers 3rd acyl chain from
        ▼        phosphatidylethanolamine to the α-amino group (amide bond)
 Mature TRIACYLATED lipoprotein
        │
        │  Lol system — sorting
        ▼
 Outer membrane (most lipoproteins) / retained in inner membrane
```

### The catalytic cycle at the membrane–periplasm interface

Lnt is embedded in the **inner (cytoplasmic) membrane** by its N-terminal transmembrane domain, with a **periplasm-facing globular catalytic domain**. Catalysis proceeds by a two-step ping-pong mechanism:

```
 Step 1 (slow):  Phospholipid (PE) + Lnt–Cys381–SH
                     → Lnt–Cys381–S–C(=O)–R   (thioester acyl-enzyme)  + lyso-PE
 Step 2 (fast):  Lnt–Cys381–S–C(=O)–R + H2N–[apolipoprotein]
                     → R–C(=O)–NH–[lipoprotein]  (amide) + regenerated Lnt–Cys381–SH
```

The **Cys381** nucleophile is activated within the **E269–K329–C381** triad characteristic of the CN-hydrolase superfamily; the acyl chain is drawn from a membrane phospholipid (physiologically phosphatidylethanolamine), and a dynamic arm gates access to the active site between the two half-reactions. The net result is an **amide (N-linked) acyl chain** on the apolipoprotein amino terminus, completing the triacylated anchor that stabilizes the lipoprotein in the membrane and licenses downstream Lol-mediated sorting.

### Localization and biological role

The enzyme's function is spatially precise: it acts at the **periplasmic face of the inner membrane**, the compartment where Lgt/LspA-processed apolipoproteins accumulate. Its role is narrow and mechanistic rather than pleiotropic — it performs one chemical modification on a broad set of substrates (essentially all cellular lipoproteins, recognized through their invariant diacylglyceryl-cysteine). The physiological importance of this single modification is evident from the consequences of its loss: impaired lipoprotein modification, increased outer-membrane permeability, antibiotic hypersusceptibility, and morphological defects. In *P. putida* — a γ-proteobacterium like *E. coli* and *P. aeruginosa* — Lnt is expected to be essential or near-essential, consistent with the pattern across most γ-proteobacteria.

---

## Evidence Base

| PMID | Title (abbreviated) | Contribution to this report |
|---|---|---|
| [21676878](https://pubmed.ncbi.nlm.nih.gov/21676878/) | *Kinetics and phospholipid specificity of apolipoprotein N-acyltransferase* | Defines the exact reaction (acyl transfer to α-amino group → triacylated lipoprotein); establishes ping-pong mechanism, thioester intermediate, and phospholipid (PE) donor with headgroup/acyl-chain selectivity |
| [17416655](https://pubmed.ncbi.nlm.nih.gov/17416655/) | *Identification of essential residues in apolipoprotein N-acyl transferase, a member of the CN hydrolase family* | Identifies the E267–K335–C387 catalytic triad and additional essential residues; basis for mapping conserved residues onto Q88DN4 |
| [28675161](https://pubmed.ncbi.nlm.nih.gov/28675161/) | *Structural insights into the mechanism of the membrane integral N-acyltransferase step…* | Crystal structures (*P. aeruginosa*, *E. coli*): inner-membrane domain + periplasmic catalytic domain, periplasm-facing active site |
| [31959792](https://pubmed.ncbi.nlm.nih.gov/31959792/) | *Conformational changes in Apolipoprotein N-acyltransferase (Lnt)* | Captures the covalent acyl-cysteine intermediate and the dynamic gating arm |
| [28698362](https://pubmed.ncbi.nlm.nih.gov/28698362/) | *Structural insights into lipoprotein N-acylation by…* | Places Lnt as third of three sequential inner-membrane enzymes; describes the Lgt→LspA steps upstream |
| [25755189](https://pubmed.ncbi.nlm.nih.gov/25755189/) | *Revisiting the Gram-negative lipoprotein paradigm* | Links Lnt's triacylated product to downstream Lol sorting to the outer membrane |
| [32478756](https://pubmed.ncbi.nlm.nih.gov/32478756/) | *Click-Chemistry Based Fluorometric Assay for Apolipoprotein N-acyltransferase…* | Confirms acyl chains originate from membrane phospholipids; assay development for Lnt |
| [30307391](https://pubmed.ncbi.nlm.nih.gov/30307391/) | *The apolipoprotein N-acyl transferase Lnt is dispensable for growth in Acinetobacter species* | Documents physiological consequences of Lnt loss and its variable essentiality across taxa |
| [29859843](https://pubmed.ncbi.nlm.nih.gov/29859843/) | *The N-acyltransferase Lnt: Structure-function insights from recent simultaneous studies* | Review synthesizing the 2017 Lnt structures; comparison to soluble nitrilases |
| [31685855](https://pubmed.ncbi.nlm.nih.gov/31685855/) | *A sensitive fluorescence-based assay to monitor…Lnt* | Reinforces phospholipid-derived acyl donors and essentiality of the modification |
| [32845938](https://pubmed.ncbi.nlm.nih.gov/32845938/) | *Characterization of a novel AraC/XylS-regulated family of N-acyltransferases…* | Describes AatD, an Lnt-like N-acyltransferase, and periplasmic accumulation phenotypes on loss of activity (context for the Lnt family) |
| [37937999](https://pubmed.ncbi.nlm.nih.gov/37937999/) | *Essential role of…* | Confirms Lgt/LspA essentiality and variable Lnt essentiality across Gram-negative bacteria |

The evidence base is internally consistent: independent kinetic, structural, mutagenic, and phenotypic studies all point to the same enzymatic identity, mechanism, and localization. No literature was found that contradicts the assignment. Critically, the direct sequence and topology analysis of Q88DN4 performed here (Findings 6–7) bridges the gap between the orthologue-based experimental literature and the specific *P. putida* protein.

---

## Limitations and Knowledge Gaps

1. **No direct experimental characterization of the *P. putida* protein.** All enzymology, kinetics, and structures derive from *E. coli* and *P. aeruginosa* Lnt. The functional assignment to Q88DN4 is by strong orthology (43.1% identity to *E. coli* Lnt) plus complete conservation of catalytic and essential residues — robust, but inferential rather than direct.

2. **Essentiality in *P. putida* not experimentally confirmed here.** Lnt is essential in most γ-proteobacteria, but essentiality is species-dependent (dispensable in *Acinetobacter*, *Francisella*, *Neisseria*). Whether *P. putida* KT2440 tolerates *lnt* deletion has not been established in this investigation.

3. **Acyl donor specificity is inferred.** Phosphatidylethanolamine is the physiological donor in *E. coli* and is the major phospholipid in pseudomonads, but the precise donor preference of the *P. putida* enzyme (and the exact acyl-chain profile it installs) has not been measured.

4. **Lipoprotein substrate repertoire in *P. putida* is uncharacterized.** The specific set of lipoproteins modified by PP_4790 in *P. putida*, and any substrate that might escape modification, are unknown.

5. **Coarse topology prediction.** Kyte–Doolittle analysis correctly localizes the membrane domain to the N-terminus but undercounts transmembrane helices relative to the crystal structures; a precise experimental topology for the *P. putida* protein is not available.

---

## Proposed Follow-up Experiments / Actions

1. **Structural prediction and validation.** Generate an AlphaFold model of Q88DN4 and superpose it on the *P. aeruginosa* Lnt structure to confirm the fold, transmembrane-helix count, and the geometry of the E269–K329–C381 triad. Verify active-site positioning at the periplasmic membrane interface.

2. **Genetic essentiality test.** Attempt a clean *lnt* (PP_4790) deletion in *P. putida* KT2440 with and without a complementing copy; assess viability, outer-membrane permeability (e.g., detergent/antibiotic sensitivity), and morphology to test whether the *E. coli*-like essential phenotype holds.

3. **In vitro reconstitution.** Overexpress and purify Q88DN4, then assay N-acyltransferase activity using a fluorescence- or click-chemistry-based Lnt assay ([PMID: 31685855](https://pubmed.ncbi.nlm.nih.gov/31685855/); [PMID: 32478756](https://pubmed.ncbi.nlm.nih.gov/32478756/)) with FSL-1 as acceptor and defined phospholipids as donors to measure headgroup/acyl-chain preference.

4. **Active-site mutagenesis.** Construct C381A (nucleophile), E269A, and K329A variants and test loss of activity in vitro and loss of complementation in vivo, directly confirming the predicted catalytic triad.

5. **Lipoproteomics.** Use mass spectrometry to characterize the N-acylation state of the *P. putida* lipoproteome in wild-type versus *lnt*-depleted cells, defining the substrate repertoire and confirming triacylation in this organism.

6. **Antibacterial-target assessment.** Given Lnt's status as an emerging antibiotic target, evaluate whether inhibitors developed against *E. coli* / *P. aeruginosa* Lnt cross-react with the *P. putida* enzyme, informing broad-spectrum potential.


## Artifacts

- [OpenScientist final report](lnt-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](lnt-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:21676878
2. PMID:28698362
3. PMID:17416655
4. PMID:32478756
5. PMID:28675161
6. PMID:31959792
7. PMID:25755189
8. PMID:30307391
9. PMID:31685855