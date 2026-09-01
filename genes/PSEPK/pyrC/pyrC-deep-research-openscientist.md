---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T19:58:27.950573'
end_time: '2026-08-31T20:32:25.626943'
duration_seconds: 2037.68
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: pyrC
  gene_symbol: pyrC
  uniprot_accession: Q88NW7
  protein_description: 'RecName: Full=Dihydroorotase {ECO:0000255|HAMAP-Rule:MF_00219};
    Short=DHOase {ECO:0000255|HAMAP-Rule:MF_00219}; EC=3.5.2.3 {ECO:0000255|HAMAP-Rule:MF_00219};'
  gene_info: Name=pyrC {ECO:0000255|HAMAP-Rule:MF_00219}; OrderedLocusNames=PP_1086;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the metallo-dependent hydrolases superfamily.
  protein_domains: Amidohydro-rel. (IPR006680); DHOdimr. (IPR004721); Dihydroorotase_CS.
    (IPR002195); Metal_Hydrolase. (IPR032466); Amidohydro_1 (PF01979)
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
citation_count: 11
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: pyrC-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: pyrC-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88NW7
- **Protein Description:** RecName: Full=Dihydroorotase {ECO:0000255|HAMAP-Rule:MF_00219}; Short=DHOase {ECO:0000255|HAMAP-Rule:MF_00219}; EC=3.5.2.3 {ECO:0000255|HAMAP-Rule:MF_00219};
- **Gene Information:** Name=pyrC {ECO:0000255|HAMAP-Rule:MF_00219}; OrderedLocusNames=PP_1086;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the metallo-dependent hydrolases superfamily.
- **Key Domains:** Amidohydro-rel. (IPR006680); DHOdimr. (IPR004721); Dihydroorotase_CS. (IPR002195); Metal_Hydrolase. (IPR032466); Amidohydro_1 (PF01979)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "pyrC" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'pyrC' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **pyrC** (gene ID: pyrC, UniProt: Q88NW7) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# pyrC (PP_1086, UniProt Q88NW7) in *Pseudomonas putida* KT2440: Functional Annotation Report

## Summary

The gene **pyrC** (ordered locus **PP_1086**; UniProt **Q88NW7**; *PYRC_PSEPK*) of *Pseudomonas putida* KT2440 encodes **dihydroorotase (DHOase; EC 3.5.2.3)**, a cytoplasmic, zinc-dependent metallohydrolase of the amidohydrolase (metallo-dependent hydrolase) superfamily. Its primary and well-defined function is to catalyze the **reversible cyclization of N-carbamoyl-L-aspartate (carbamoyl aspartate) to (S)-4,5-dihydro-L-orotate**, the **third step of the de novo pyrimidine (UMP) biosynthetic pathway**. The enzyme is strictly specific: the natively purified *P. putida* protein hydrolyzed only dihydro-L-orotate and its methyl ester, and the reaction is fully reversible, with a Km for dihydroorotate of ~0.081 mM.

Structurally and mechanistically, this DHOase is a monofunctional (**"Class II"/standalone**) enzyme that functions as a **soluble homodimer** with ~41 kDa subunits (native mass ~82 kDa). Each subunit adopts a **TIM-barrel ((β/α)₈) fold** housing a **binuclear zinc active center** in which the two Zn²⁺ ions (~3.6 Å apart) are bridged by a **post-translationally carbamylated lysine**, a catalytic architecture established at atomic resolution for the orthologous *Escherichia coli* enzyme and conserved across bacterial DHOases. Sequence analysis confirms that Q88NW7 retains the complete catalytic-residue set — His14, His16, the carbamylated Lys100, His137, His175, and Asp248 — mapping one-to-one onto the *E. coli* scaffold. As a soluble metabolic enzyme with no signal peptide or transmembrane segments, it acts in the **cytoplasm**.

A crucial disambiguation underlies this report: *P. putida* carries **two** DHOase-homologous genes. PP_1086/pyrC (Q88NW7) is the **genuinely catalytically active** dihydroorotase. It is distinct from a separate **vestigial "pyrC'"** gene, physically linked to pyrB, which encodes a catalytically **dead** DHOase homolog that lacks critical histidyl residues and instead serves a purely **structural role** — stabilizing the dodecameric assembly of the *P. putida* aspartate transcarbamoylase (ATCase) holoenzyme. This report establishes, on the basis of direct enzymology, structural homology, sequence-level residue conservation, and genome annotation, that Q88NW7 is the active pyrimidine-biosynthetic DHOase and is monocistronic and physically unlinked to the pyr/ATCase locus.

---

## Key Findings

### Finding 1 — pyrC (Q88NW7) is a dihydroorotase catalyzing the reversible interconversion of N-carbamoyl-L-aspartate and L-dihydroorotate (step 3 of de novo pyrimidine biosynthesis)

The primary function of the pyrC gene product is enzymatic. It is classified as **EC 3.5.2.3** and catalyzes the third reaction of the de novo pyrimidine biosynthetic pathway: the intramolecular cyclization/dehydration of **N-carbamoyl-L-aspartate** to form **(S)-4,5-dihydro-L-orotate** plus water, a reaction that operates in both directions.

The most authoritative evidence for the *P. putida* enzyme comes from direct enzymology on DHOase purified from *Pseudomonas putida* by Ogawa & Shimizu (1995). They demonstrated strict substrate specificity — "*The enzyme only hydrolyzed dihydro-L-orotate and its methyl ester, and the reactions were reversible*" ([PMID: 8572888](https://pubmed.ncbi.nlm.nih.gov/8572888/)) — thereby establishing both the substrate preference and reversibility that define this step in the exact ortholog context. The kinetic parameters were quantified: "*The apparent Km and Vmax values for dihydro-L-orotate hydrolysis (at pH 7.4) were 0.081 mM and 18 mumol min-1 mg-1*" ([PMID: 8572888](https://pubmed.ncbi.nlm.nih.gov/8572888/)). For the reverse (cyclization) direction, the Km for N-carbamoyl-DL-aspartate was 2.2 mM with a Vmax of 68 µmol min⁻¹ mg⁻¹ at pH 6.0. The pH optima differing between the two directions (7.4 for hydrolysis, 6.0 for cyclization) are characteristic of this reversible amidohydrolase.

The identity of the reaction is corroborated across bacterial and structural studies. Thoden et al. (2001) state that "*Dihydroorotase plays a key role in pyrimidine biosynthesis by catalyzing the reversible interconversion of carbamoyl aspartate to dihydroorotate*" ([PMID: 11401542](https://pubmed.ncbi.nlm.nih.gov/11401542/)), and Lipowska et al. (2019), analyzing pathogen DHOases, confirm that "*dihydroorotase (DHO), catalyzes the reversible interconversion of N-carbamoyl-l-aspartate to 4,5-dihydroorotate*" ([PMID: 31207330](https://pubmed.ncbi.nlm.nih.gov/31207330/)). The reaction is thus conserved and well-characterized across the bacterial lineage, with the *P. putida* enzyme directly measured.

| Parameter | Value | Condition | Source |
|---|---|---|---|
| Km (dihydro-L-orotate) | 0.081 mM | pH 7.4 (hydrolysis) | [PMID: 8572888](https://pubmed.ncbi.nlm.nih.gov/8572888/) |
| Vmax (dihydro-L-orotate) | 18 µmol min⁻¹ mg⁻¹ | pH 7.4 | [PMID: 8572888](https://pubmed.ncbi.nlm.nih.gov/8572888/) |
| Km (N-carbamoyl-DL-aspartate) | 2.2 mM | pH 6.0 (cyclization) | [PMID: 8572888](https://pubmed.ncbi.nlm.nih.gov/8572888/) |
| Vmax (N-carbamoyl-DL-aspartate) | 68 µmol min⁻¹ mg⁻¹ | pH 6.0 | [PMID: 8572888](https://pubmed.ncbi.nlm.nih.gov/8572888/) |
| Substrate specificity | Only dihydro-L-orotate + methyl ester | — | [PMID: 8572888](https://pubmed.ncbi.nlm.nih.gov/8572888/) |

### Finding 2 — DHOase is a Zn-dependent metallohydrolase with a binuclear metal center and a carboxylated-lysine bridge in a TIM-barrel fold

The mechanism of catalysis is built on a **binuclear zinc center**. The gold-standard structural reference is the 1.7 Å crystal structure of *E. coli* DHOase (Thoden et al. 2001), where "*each subunit contains a binuclear zinc center with the metal ions separated by approximately 3.6 A. Lys 102, which is carboxylated, serves as a bridging ligand between the two cations*" ([PMID: 11401542](https://pubmed.ncbi.nlm.nih.gov/11401542/)). In this arrangement, the α-metal is coordinated by His16, His18, the carboxylated Lys102, and Asp250 plus a hydroxide; the β-metal by Lys102, His139, His177, and the bridging hydroxide. The overall subunit is a "*'TIM' barrel motif*" ([PMID: 11401542](https://pubmed.ncbi.nlm.nih.gov/11401542/)) — the classic (β/α)₈ scaffold on which amidohydrolase-superfamily active sites are constructed.

The metal dependence is experimentally confirmed for the *P. putida* enzyme itself: Ogawa & Shimizu found that "*The enzyme was inhibited by metal ion chelators and activated by Zn2+*" ([PMID: 8572888](https://pubmed.ncbi.nlm.nih.gov/8572888/)), directly demonstrating that a zinc cofactor is required for activity in the native protein. Independent confirmation of the architecture comes from the human CAD DHOase domain, which likewise contains "*two Zn²⁺ ions bridged by a carboxylated lysine*" ([PMID: 24332717](https://pubmed.ncbi.nlm.nih.gov/24332717/)), showing the binuclear-Zn/carbamylated-lysine motif is conserved from bacteria to humans.

This mechanistic picture matches the InterPro/Pfam annotation of Q88NW7: the Amidohydro_1 domain (**PF01979**), Metal_Hydrolase (IPR032466), and the Dihydroorotase_CS conserved-site signature (IPR002195) — all hallmarks of a metal-dependent hydrolase acting through a bridged bimetal center. The flexibility of a catalytic surface loop is also important mechanistically: kinetic and structural analysis of *E. coli* mutants showed that residues Thr109 and Thr110 in a flexible loop provide productive substrate binding and stabilize the transition-state intermediate, with loop deletion causing near-complete activity loss despite an intact binuclear zinc center ([PMID: 17711307](https://pubmed.ncbi.nlm.nih.gov/17711307/)).

### Finding 3 — The *P. putida* enzyme is a cytoplasmic, homodimeric (~41 kDa subunit), monofunctional (Class II) DHOase regulated by pyrimidine-pathway intermediates

Ogawa & Shimizu determined that the native *P. putida* enzyme is 82 kDa, composed of "*two identical subunits with a relative molecular mass of 41 kDa*" ([PMID: 8572888](https://pubmed.ncbi.nlm.nih.gov/8572888/)). This homodimeric organization is the defining feature of the **standalone, "Class II" DHOase** typified by *E. coli* (a homodimer; [PMID: 11401542](https://pubmed.ncbi.nlm.nih.gov/11401542/)), as opposed to the DHOase activity embedded within the large multifunctional eukaryotic CAD protein ([PMID: 24332717](https://pubmed.ncbi.nlm.nih.gov/24332717/)). Thus, pyrC in *P. putida* encodes an independent metabolic enzyme, not a fused domain.

The active site's specificity is further illuminated by product- and analog-based inhibition of the *P. putida* enzyme. It is "*competitively inhibited by N-carbamoylamino acids such as N-carbamoylglycine, with a Ki value of 2.7 mM*" ([PMID: 8572888](https://pubmed.ncbi.nlm.nih.gov/8572888/)), and is non-competitively inhibited by dihydrouracil (Ki 3.4 mM) and orotate (Ki 0.75 mM). These inhibition profiles — by structural analogs of the substrate and by downstream pyrimidine-metabolism intermediates — are consistent with a tightly shaped active site and with metabolic feedback sensitivity.

At the pathway/regulatory level, de novo pyrimidine enzymes in *P. putida* (including DHOase) are regulated by pyrimidine availability and carbon source. Santiago & West-type studies documented that "*Regulation at the transcriptional level of de novo pyrimidine biosynthetic enzyme synthesis in P. putida ATCC 17536 was observed*" ([PMID: 12619820](https://pubmed.ncbi.nlm.nih.gov/12619820/)). Consistent with earlier work, repression of these enzymes by pyrimidines in *P. putida* is comparatively weak — only 1.5-to-2-fold derepression following pyrimidine starvation was detected ([PMID: 176312](https://pubmed.ncbi.nlm.nih.gov/176312/)) — indicating modest but real transcriptional control. As a soluble cytoplasmic enzyme lacking any signal peptide or transmembrane feature, the protein performs its catalysis in the **cytoplasm**.

### Finding 4 — PP_1086/pyrC is the ACTIVE standalone DHOase, distinct from the vestigial pyrC' that is a structural subunit of the *P. putida* ATCase holoenzyme

This is the central identity-verification finding. *P. putida* encodes **two** DHOase-homologous genes with fundamentally different roles, and it is essential not to conflate them.

The first is a **pyrB-overlapping "pyrC'"** gene encoding a 424-residue/44.2 kDa polypeptide that is a catalytically **inactive ("vestigial") DHOase**. Schurr et al. (1995) showed that "*the 44.2-kDa polypeptide lacks specific histidyl residues thought to be critical for DHOase enzymatic function*" ([PMID: 7896697](https://pubmed.ncbi.nlm.nih.gov/7896697/)), and it does not complement *E. coli* pyrC auxotrophs. Its role is purely **structural**: "*The proposed function for the vestigial DHOase is to maintain ATCase activity by conserving the dodecameric assembly of the native enzyme*" ([PMID: 7896697](https://pubmed.ncbi.nlm.nih.gov/7896697/)). Critically, the authors state that "*this 44.2-kDa polypeptide is not considered to be the functional product of the pyrC gene in P. putida, as DHOase activity is distinct from the ATCase complex*" ([PMID: 7896697](https://pubmed.ncbi.nlm.nih.gov/7896697/)).

The second — and the subject of this report — is the **functional, catalytically active DHOase**, PP_1086/pyrC (Q88NW7): a separate, standalone monofunctional homodimer (82 kDa native; 41 kDa subunits; [PMID: 8572888](https://pubmed.ncbi.nlm.nih.gov/8572888/)) whose activity is "distinct from the ATCase complex" and which retains the binuclear-Zn His/Lys/Asp active-site ligands defined by the *E. coli* structure ([PMID: 11401542](https://pubmed.ncbi.nlm.nih.gov/11401542/)). The evolutionary logic of these two paralogs is captured by the ATCase quaternary-structure classification, in which prokaryotic ATCases fall into classes depending on whether the associated DHOase (PyrC) is active (subclass A1) or inactive (PyrC', subclass A2) ([PMID: 14660694](https://pubmed.ncbi.nlm.nih.gov/14660694/)).

This finding satisfies the mandatory verification requirement: Q88NW7 is unambiguously the **active pyrimidine-biosynthetic DHOase (PyrC)**, not the vestigial ATCase-scaffolding PyrC'.

### Finding 5 — Q88NW7 retains the complete binuclear-Zn catalytic residue set, one-to-one homologous to *E. coli* DHOase

Direct sequence analysis provides residue-level proof that Q88NW7 is catalytically competent. The 348-amino-acid PYRC_PSEPK sequence was mapped onto the *E. coli* DHOase scaffold ([PMID: 11401542](https://pubmed.ncbi.nlm.nih.gov/11401542/)). All six catalytic ligands are present and correctly positioned:

| Q88NW7 residue | Role | *E. coli* equivalent |
|---|---|---|
| His14 | α-Zn ligand (N-terminal H-I-H motif) | His16 |
| His16 | α-Zn ligand | His18 |
| Lys100 (carbamylated) | Bridges both Zn ions | Lys102 |
| His137 | β-Zn ligand | His139 |
| His175 | β-Zn ligand | His177 |
| Asp248 | α-Zn ligand / active-site base | Asp250 |

Substrate-contact residues (e.g., the His16-Leu-Arg18 element, Asn42, His137, Leu220, His252, Ala264) are likewise conserved. The retention of the full catalytic set stands in explicit contrast to the vestigial pyrC', which "*lacks specific histidyl residues thought to be critical for DHOase enzymatic function*" ([PMID: 7896697](https://pubmed.ncbi.nlm.nih.gov/7896697/)) — reinforcing that PP_1086 is the active enzyme. UniProt curation independently lists the catalytic reaction ((S)-dihydroorotate + H₂O = N-carbamoyl-L-aspartate + H⁺; RHEA:24296), the Zn²⁺ cofactor, the pathway assignment ("UMP biosynthesis via de novo pathway, step 3/3"), and the homodimeric assembly.

### Finding 6 — pyrC/PP_1086 is a monocistronic, isolated gene, physically unlinked to other pyr genes

Genome annotation (KEGG, organism ppu) independently confirms PP_1086 = pyrC / dihydroorotase, KO **K01465**, EC 3.5.2.3, mapped to Pyrimidine metabolism (ppu00240), Metabolic pathways (ppu01100), and Biosynthesis of cofactors (ppu01240); cross-referenced to UniProt Q88NW7 and NCBI protein AAN66711 (348 aa), at genome position complement(1244481..1245527), Pfam Amidohydro_1.

The genomic neighborhood shows the gene is **not part of a pyr operon**: PP_1084 = tsaA (peroxiredoxin), PP_1085 = rnt (RNase T), **PP_1086 = pyrC**, PP_1087 = an OmpA-family outer-membrane protein, and PP_1088 = argG (argininosuccinate synthase) — all functionally unrelated to pyrimidine biosynthesis. pyrC is therefore monocistronic and separated from the pyrB/pyrC' (ATCase) locus. This organization is consistent with independent transcriptional regulation of pyrimidine genes in *P. putida*, as documented by the observation that "*Regulation at the transcriptional level of de novo pyrimidine biosynthetic enzyme synthesis in P. putida ATCC 17536 was observed*" ([PMID: 12619820](https://pubmed.ncbi.nlm.nih.gov/12619820/)).

---

## Mechanistic Model / Interpretation

### Position in the pathway

pyrC/PP_1086 executes the **third of six enzymatic steps** in the de novo synthesis of UMP, the precursor of all pyrimidine nucleotides:

```
Glutamine + HCO3- + 2ATP
        │  (carbamoyl-phosphate synthetase, carAB)
        ▼
   Carbamoyl-phosphate
        │  + L-aspartate  (aspartate transcarbamoylase, ATCase, pyrB)
        ▼
  N-carbamoyl-L-aspartate  ────────────┐
        │                              │  ← STEP 3: DIHYDROOROTASE (pyrC / PP_1086 / Q88NW7)
        │   reversible cyclization/dehydration (–H2O)
        ▼                              │
   (S)-4,5-dihydro-L-orotate  ◄────────┘  reversible (hydrolysis adds H2O)
        │  (dihydroorotate dehydrogenase, pyrD)
        ▼
      Orotate
        │  (orotate phosphoribosyltransferase, pyrE)
        ▼
      OMP
        │  (OMP decarboxylase, pyrF)
        ▼
       UMP  →  UDP, UTP, CTP, dTTP, ...
```

### The catalytic machine

Each of the two identical subunits folds into a **(β/α)₈ TIM barrel**, at the C-terminal end of which sits the active site. Two Zn²⁺ ions (~3.6 Å apart) are held by a constellation of histidines and an aspartate and bridged by a **carbamylated lysine** (Lys100 in Q88NW7). A metal-bridging hydroxide serves as the nucleophile/leaving group. In the **cyclization** direction, the bimetal center polarizes the carbamoyl group of N-carbamoyl-L-aspartate and the hydroxide-mediated chemistry closes the six-membered dihydroorotate ring while expelling water; in the **hydrolysis** direction the same machinery adds water across the ring amide bond. The differing pH optima (7.4 vs 6.0) for the two directions reflect the protonation requirements of the forward vs reverse chemistry.

```
        His14   His16                 His137  His175
           \    /                        \    /
            [Zn_α] ---- OH(bridge) ---- [Zn_β]
            /   \        |                 /
        Asp248  (Lys100-CO2- bridges both Zn)
                          |
              substrate: N-carbamoyl-L-aspartate  ⇌  dihydro-L-orotate + H2O
```

### Two paralogs, two fates

The most important interpretive point for correct annotation is the **paralog split** in *P. putida*:

| Feature | **pyrC / PP_1086 (Q88NW7)** — this report | **pyrC' (pyrB-linked)** |
|---|---|---|
| Catalytic activity | **Active DHOase** (EC 3.5.2.3) | **Inactive** (vestigial) |
| Catalytic His ligands | **Retained** (His14/16/137/175, Asp248, Lys100) | **Missing** critical histidines |
| Quaternary role | Standalone homodimer, ~82 kDa | Structural subunit of ATCase dodecamer |
| Complements *E. coli* pyrC⁻ | Expected yes (functional) | **No** |
| Genomic location | Isolated / monocistronic (complement 1244481..1245527) | Overlaps/linked to pyrB (ATCase locus) |
| Function | Metabolic catalysis (pyrimidine biosynthesis) | Scaffolding — maintains ATCase dodecamer assembly |

This division of labor is an elegant example of **subfunctionalization after gene duplication**: one copy retained catalysis, the other lost catalysis but was co-opted for a structural role in the ATCase holoenzyme, a scenario recognized in the broader ATCase quaternary-structure/evolution framework ([PMID: 14660694](https://pubmed.ncbi.nlm.nih.gov/14660694/)).

### Localization and regulation

The enzyme is **cytoplasmic** — it is a soluble metabolic protein with no signal peptide or membrane anchor and it operates on soluble small-molecule substrates in the cytosol. Its expression is under **modest transcriptional control** by pyrimidine availability and carbon source, and its activity is **product/analog-inhibited** by pyrimidine-metabolism intermediates (orotate, dihydrouracil, N-carbamoylglycine), providing local feedback tuning.

---

## Evidence Base

| PMID | Study (short) | How it supports the findings |
|---|---|---|
| [8572888](https://pubmed.ncbi.nlm.nih.gov/8572888/) | *Purification and characterization of dihydroorotase from Pseudomonas putida* (Ogawa & Shimizu 1995) | **Primary, direct evidence** on the exact ortholog: strict substrate specificity, reversibility, kinetics (Km/Vmax), Zn dependence, homodimer 41 kDa×2, analog/product inhibition. Underpins Findings 1, 2, 3, 4. |
| [11401542](https://pubmed.ncbi.nlm.nih.gov/11401542/) | *Molecular structure of dihydroorotase: a paradigm for catalysis through a binuclear metal center* (Thoden et al. 2001) | High-resolution *E. coli* structure defining the TIM-barrel fold, binuclear Zn center, carboxylated Lys102, and the catalytic ligand set to which Q88NW7 maps. Underpins Findings 1, 2, 5. |
| [7896697](https://pubmed.ncbi.nlm.nih.gov/7896697/) | *ATCase genes of P. putida: requirement for an inactive dihydroorotase* (Schurr et al. 1995) | Defines the **vestigial pyrC'** — inactive, lacks histidyl residues, structural role in ATCase dodecamer — establishing that PP_1086 is the distinct **active** DHOase. Central to Findings 4, 5. |
| [31207330](https://pubmed.ncbi.nlm.nih.gov/31207330/) | *Pyrimidine biosynthesis in pathogens — DHOases from Yersinia and Vibrio* (Lipowska et al. 2019) | Confirms the substrates/products and reversibility of bacterial DHOases broadly. Supports Finding 1. |
| [24332717](https://pubmed.ncbi.nlm.nih.gov/24332717/) | *Structure/function/evolution of the DHOase domain of human CAD* | Independent confirmation of the binuclear-Zn / carbamylated-lysine architecture across kingdoms; contrasts standalone vs CAD-fused DHOase. Supports Findings 2, 3. |
| [12619820](https://pubmed.ncbi.nlm.nih.gov/12619820/) | *Control of pyrimidine formation in P. putida ATCC 17536* | Documents transcriptional regulation of de novo pyrimidine enzymes in *P. putida*. Supports Findings 3, 6. |
| [176312](https://pubmed.ncbi.nlm.nih.gov/176312/) | *Regulation of arginine and pyrimidine biosynthesis in P. putida* | Shows only weak (1.5–2×) derepression of pyrimidine enzymes on starvation, plus ATCase feedback inhibition. Supports Finding 3. |
| [14660694](https://pubmed.ncbi.nlm.nih.gov/14660694/) | *Using quaternary structures to assess ATCase evolution* | Frames the active-PyrC (A1) vs inactive-PyrC' (A2) paralog classification and its evolutionary logic. Supports Finding 4. |
| [17711307](https://pubmed.ncbi.nlm.nih.gov/17711307/) | *Kinetic/structural analysis of mutant E. coli DHOases* | Details the flexible surface loop (Thr109/Thr110) that stabilizes the transition state — mechanistic depth for the catalytic model. Supports Finding 2. |
| [26446564](https://pubmed.ncbi.nlm.nih.gov/26446564/) | *Creation of a putative third metal site in type II DHOases* | Confirms type II (Class II) DHOases use a binuclear center; a third site can be engineered. Context for Findings 2/3. |
| [24418229](https://pubmed.ncbi.nlm.nih.gov/24418229/) | *Allantoinase/DHOase inhibition by flavonols/amidohydrolase substrates* | Places DHOase in the cyclic amidohydrolase family with shared binuclear active sites and defines substrate-specificity boundaries. Context for Finding 2. |

Supporting/contextual papers on pathway regulation in related pseudomonads include *P. fluorescens* ([PMID: 16255137](https://pubmed.ncbi.nlm.nih.gov/16255137/)) and *P. fragi* ([PMID: 12390485](https://pubmed.ncbi.nlm.nih.gov/12390485/)), and the L-hydantoinase structure ([PMID: 12093275](https://pubmed.ncbi.nlm.nih.gov/12093275/)) illustrating the shared TIM-barrel/binuclear-Zn fold across the amidohydrolase superfamily.

---

## Limitations and Knowledge Gaps

1. **No crystal structure of Q88NW7 itself.** The atomic mechanism is inferred from the highly homologous *E. coli* enzyme ([PMID: 11401542](https://pubmed.ncbi.nlm.nih.gov/11401542/)) and residue mapping. While the conservation is unambiguous (all six catalytic ligands present), a direct *P. putida* KT2440 DHOase structure has not been reported.

2. **Enzymology strain provenance.** The definitive kinetic/biochemical characterization ([PMID: 8572888](https://pubmed.ncbi.nlm.nih.gov/8572888/)) was performed on DHOase purified from *P. putida* (species-level); it is reasonably but not formally proven that the purified protein corresponds precisely to the KT2440 PP_1086 gene product rather than a very close ortholog. Given the sequence identity and functional match, this is a minor caveat.

3. **Regulatory detail is coarse.** Transcriptional regulation of pyrimidine genes in *P. putida* is documented at the pathway level ([PMID: 12619820](https://pubmed.ncbi.nlm.nih.gov/12619820/); [PMID: 176312](https://pubmed.ncbi.nlm.nih.gov/176312/)), but the specific promoter, regulator(s), and any operon/regulon context for PP_1086 have not been experimentally mapped. Genome context indicates it is monocistronic, but the transcription start site and regulatory elements remain uncharacterized.

4. **Metal stoichiometry not directly measured for Q88NW7.** Zn dependence is established biochemically for the *P. putida* enzyme ([PMID: 8572888](https://pubmed.ncbi.nlm.nih.gov/8572888/)) and structurally for homologs, but the exact in vivo metal occupancy (mono- vs binuclear under physiological conditions) has not been quantified for this specific protein.

5. **Physiological flux and essentiality.** Whether PP_1086 is strictly essential in KT2440 under standard conditions (versus salvage-pathway rescue) has not been directly tested here.

---

## Proposed Follow-up Experiments / Actions

1. **Genetic complementation.** Clone PP_1086 and test complementation of an *E. coli* pyrC auxotroph to formally confirm in vivo catalytic function — the clean, decisive test that distinguishes it from vestigial pyrC'.

2. **Recombinant expression + kinetics.** Express His-tagged Q88NW7, purify, and re-measure kinetics (Km, kcat, pH profile) and metal content (ICP-MS) to tie the classic *P. putida* enzymology definitively to the PP_1086 gene product.

3. **Structure determination.** Solve the KT2440 DHOase crystal or cryo-EM structure (± bound substrate/product/analog) to confirm the binuclear-Zn center, carbamylated Lys100, and the flexible catalytic loop analogous to *E. coli* Thr109/Thr110 ([PMID: 17711307](https://pubmed.ncbi.nlm.nih.gov/17711307/)).

4. **Active-site mutagenesis.** Mutate the mapped ligands (His14, His16, Lys100, His137, His175, Asp248) individually and assay activity loss to experimentally validate the residue assignments made from homology.

5. **Transcriptional mapping.** Use RNA-seq/5′-RACE and reporter fusions under pyrimidine-replete vs -starved and different carbon sources to define the PP_1086 promoter, transcription start, and regulator(s).

6. **Knockout phenotyping.** Construct a ΔPP_1086 deletion and test pyrimidine auxotrophy and growth rescue by uracil/uridine to establish essentiality and pathway position in KT2440.

---

*Report prepared for functional annotation of pyrC (PP_1086, UniProt Q88NW7) in* Pseudomonas putida *KT2440. All claims are attributed to the cited primary literature and database annotations above.*


## Artifacts

- [OpenScientist final report](pyrC-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](pyrC-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:8572888
2. PMID:11401542
3. PMID:31207330
4. PMID:24332717
5. PMID:17711307
6. PMID:12619820
7. PMID:7896697
8. PMID:14660694
9. PMID:16255137
10. PMID:12390485
11. PMID:12093275