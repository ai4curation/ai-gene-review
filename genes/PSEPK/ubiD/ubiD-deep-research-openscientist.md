---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-18T17:53:47.581800'
end_time: '2026-07-18T18:59:11.032947'
duration_seconds: 3923.45
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: ubiD
  gene_symbol: ubiD
  uniprot_accession: Q88CG8
  protein_description: 'RecName: Full=3-octaprenyl-4-hydroxybenzoate carboxy-lyase
    {ECO:0000255|HAMAP-Rule:MF_01636}; EC=4.1.1.98 {ECO:0000255|HAMAP-Rule:MF_01636};
    AltName: Full=Polyprenyl p-hydroxybenzoate decarboxylase {ECO:0000255|HAMAP-Rule:MF_01636};'
  gene_info: Name=ubiD {ECO:0000255|HAMAP-Rule:MF_01636}; OrderedLocusNames=PP_5213;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the UbiD family. {ECO:0000255|HAMAP-
  protein_domains: UbiD. (IPR002830); UbiD-like_C. (IPR049381); UbiD-like_N. (IPR049383);
    UbiD_bacteria. (IPR023677); UbiD_Rift_dom. (IPR048304)
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
citation_count: 14
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: ubiD-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: ubiD-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88CG8
- **Protein Description:** RecName: Full=3-octaprenyl-4-hydroxybenzoate carboxy-lyase {ECO:0000255|HAMAP-Rule:MF_01636}; EC=4.1.1.98 {ECO:0000255|HAMAP-Rule:MF_01636}; AltName: Full=Polyprenyl p-hydroxybenzoate decarboxylase {ECO:0000255|HAMAP-Rule:MF_01636};
- **Gene Information:** Name=ubiD {ECO:0000255|HAMAP-Rule:MF_01636}; OrderedLocusNames=PP_5213;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the UbiD family. {ECO:0000255|HAMAP-
- **Key Domains:** UbiD. (IPR002830); UbiD-like_C. (IPR049381); UbiD-like_N. (IPR049383); UbiD_bacteria. (IPR023677); UbiD_Rift_dom. (IPR048304)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ubiD" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ubiD' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ubiD** (gene ID: ubiD, UniProt: Q88CG8) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *ubiD* (Q88CG8, PP_5213) in *Pseudomonas putida* KT2440

## Summary

The gene **ubiD** (UniProt **Q88CG8**; ordered locus **PP_5213**) of *Pseudomonas putida* strain KT2440 encodes **3-octaprenyl-4-hydroxybenzoate carboxy-lyase** (**EC 4.1.1.98**), also called polyprenyl *p*-hydroxybenzoate decarboxylase. This is a **prenylated-FMN (prFMN)-dependent, UbiD-family enzyme** that catalyzes the **non-oxidative decarboxylation of 3-polyprenyl-4-hydroxybenzoate to 2-polyprenylphenol plus CO₂** (RHEA:41680), a committed step in the biosynthesis of **ubiquinone (coenzyme Q)**. The gene symbol, protein description, UbiD-family domain architecture, and single-copy status in the KT2440 genome are all fully consistent with the UniProt-provided identity; there is no ambiguity in the assignment. This report describes the enzyme's function with high confidence, drawing on direct biochemical characterization of orthologs in *Escherichia coli* and *Pseudomonas aeruginosa* together with UniProt curation of Q88CG8 itself.

The enzyme is catalytically inert as a bare apoprotein. Its activity strictly depends on a remarkable modified flavin cofactor, **prenylated FMN (prFMN)**, which bears a fourth non-aromatic ring formed by linking a dimethylallyl moiety to the FMN N5 and C6 atoms. prFMN is synthesized by the partner flavin prenyltransferase **UbiX**; *P. putida* KT2440 encodes a cognate UbiX (**Q88QE6**), so the genome contains a complete, functional UbiX–UbiD prFMN-dependent decarboxylation module. Catalysis proceeds through a chemically unusual, **reversible 1,3-dipolar cycloaddition** between the substrate and the azomethine-ylide form of oxidized prFMN — the first known enzymatic example of this cycloaddition chemistry. UbiD is a **homohexamer**, binding **one prFMN per subunit**, with an active-site proton donor and a conserved divalent metal (annotated as Mn/Mg) adjacent to the catalytic cleft.

Functionally, UbiD acts on the **cytoplasmic side of the inner (cell) membrane** as a **peripheral membrane protein**, and more precisely operates as a component of a **soluble cytoplasmic "Ubi metabolon"** — a ~1-MDa multienzyme complex that carries out the terminal reactions of ubiquinone biosynthesis in the cytosol. Because *Pseudomonas* uses **ubiquinone-9 (Q-9)** as its respiratory quinone, the physiological substrate in *P. putida* carries a **C45 nonaprenyl (9-isoprene) tail** rather than the octaprenyl chain in the *E. coli*-derived enzyme name; that is, the reaction in this organism is the decarboxylation of 3-nonaprenyl-4-hydroxybenzoate to 2-nonaprenylphenol.

---

## Key Findings

### Finding 1 — UbiD is 3-octaprenyl-4-hydroxybenzoate carboxy-lyase in ubiquinone biosynthesis

UbiD (Q88CG8 / PP_5213) catalyzes the **non-oxidative decarboxylation of 3-polyprenyl-4-hydroxybenzoate to 2-polyprenylphenol**, a committed and essential step in the bacterial ubiquinone (coenzyme Q) biosynthetic pathway. This assignment is codified by HAMAP-Rule MF_01636 (which defines the UbiD family) and by the enzyme classification **EC 4.1.1.98**. The reaction was directly characterized in orthologs from *E. coli* and *P. aeruginosa*, and PP_5213 is the canonical single-copy *ubiD* ortholog in *P. putida* KT2440.

The mechanistic role is stated explicitly in the literature: "The 3-polyprenyl-4-hydroxybenzoate decarboxylase (UbiD) catalyzes the conversion of 3-polyprenyl-4-hydroxybenzoate to 2-polyprenylphenol in the biosynthesis of ubiquinone" [PMID: 23671667](https://pubmed.ncbi.nlm.nih.gov/23671667/). A second study confirms the specific ubiquinone context: "ubiX and ubiD, which are responsible for decarboxylation of the 3-octaprenyl-4-hydroxybenzoate precursor" [PMID: 26083743](https://pubmed.ncbi.nlm.nih.gov/26083743/). Loss-of-function studies of the pathway reinforce this: an *E. coli* strain defective in the UbiX/UbiD decarboxylation step "accumulates 4-hydroxy-3-octaprenyl-benzoate" and produces very low levels of Q [PMID: 17889824](https://pubmed.ncbi.nlm.nih.gov/17889824/), pinpointing the decarboxylation step catalyzed by UbiD as the metabolic bottleneck.

### Finding 2 — Activity requires the prenylated-FMN (prFMN) cofactor produced by UbiX

UbiD is catalytically inactive as an apoprotein. It requires **prenylated FMN (prFMN)**, a modified flavin bearing a **fourth non-aromatic ring** formed by covalently linking a dimethylallyl moiety to the FMN N5 and C6 atoms. This cofactor is synthesized by the partner enzyme **UbiX**, a flavin prenyltransferase that transfers the dimethylallyl group from dimethylallyl-monophosphate (DMAP) or dimethylallyl-pyrophosphate (DMAPP) to FMN.

The discovery paper establishes both the enzymatic source and chemical structure of the cofactor: "UbiX produces a novel flavin-derived cofactor required for the decarboxylase activity of UbiD. UbiX acts as a flavin prenyltransferase, linking a dimethylallyl moiety to the flavin N5 and C6 atoms. This adds a fourth non-aromatic ring to the flavin isoalloxazine group" [PMID: 26083743](https://pubmed.ncbi.nlm.nih.gov/26083743/). After prenylation, the cofactor must undergo an activation step: "Following prenylation, prFMN undergoes oxidative maturation to form the iminium species required for UbiD activity" [PMID: 32951834](https://pubmed.ncbi.nlm.nih.gov/32951834/). The same modified cofactor was shown to be shared between the ubiquinone pathway (UbiX/UbiD) and the aromatic-acid decarboxylases (PAD1/FDC), and endogenous UbiX can activate FDC — implying "the same cofactor is required for decarboxylation of 4-hydroxy-3-polyprenylbenzoic acid by UbiD" [PMID: 25647642](https://pubmed.ncbi.nlm.nih.gov/25647642/).

### Finding 3 — Catalysis proceeds via a reversible 1,3-dipolar cycloaddition on prFMN

Atomic-resolution crystal structures of the UbiD-family model enzyme **Fdc1** show that oxidized prFMN adopts **azomethine ylide (1,3-dipole)** character. Substrate binding positions the reactive (dipolarophile) group directly above this ylide, enabling a **1,3-dipolar cycloaddition** that underpins the reversible (de)carboxylation chemistry. This was proposed as the first known enzymatic example of such a reaction: "we propose that this presents the first example, to our knowledge, of an enzymatic 1,3-dipolar cycloaddition reaction" [PMID: 26083754](https://pubmed.ncbi.nlm.nih.gov/26083754/). The structural basis is described directly: "Substrate binding positions the dipolarophile enoic acid group directly above the azomethine ylide group" [PMID: 26083754](https://pubmed.ncbi.nlm.nih.gov/26083754/).

It is worth noting that the precise mechanism may vary across the family — for example, quantum-chemical work on the UbiD-family enzyme HmfF (furandicarboxylic acid decarboxylase) proposes a nucleophilic attack rather than a concerted cycloaddition [PMID: 40343387](https://pubmed.ncbi.nlm.nih.gov/40343387/) — but the cycloaddition model is the canonical mechanism for prFMN-dependent (de)carboxylation.

### Finding 4 — Ubiquinone synthesis, including the UbiD step, occurs in a soluble cytoplasmic Ubi metabolon

Rather than being a strictly membrane-embedded process, the terminal reactions of ubiquinone biosynthesis are carried out by a **soluble, cytoplasmic multienzyme complex**. In *E. coli*, "seven Ubi proteins form the Ubi complex, a stable metabolon that catalyzes the last six reactions of the UQ biosynthetic pathway" [PMID: 30686758](https://pubmed.ncbi.nlm.nih.gov/30686758/). Critically, the complex was purified from the cytosol and shown to be functional there: "We purify the Ubi complex from cytoplasmic extracts and demonstrate that UQ biosynthesis occurs in this fraction, challenging the current thinking of a membrane-associated biosynthetic process" [PMID: 30686758](https://pubmed.ncbi.nlm.nih.gov/30686758/). The hydrophobic polyprenyl-tailed intermediates are chaperoned within the complex by the SCP2 lipid-binding domain of UbiJ, allowing water-soluble handling of otherwise membrane-partitioning substrates [PMID: 36142227](https://pubmed.ncbi.nlm.nih.gov/36142227/). This locates the UbiD reaction on the cytoplasmic side of the cell, within a soluble metabolon, even though the final product (ubiquinone) resides in the membrane.

### Finding 5 — Three-domain UbiD architecture and family diversity

Crystal structures of UbiD-family members — including *P. aeruginosa* **PA0254** and *E. coli* UbiD — reveal a conserved **three-domain subunit**: "an N-terminal α/β domain, a split β-barrel with a similar fold of a family of flavin reductases and a C-terminal α/β domain with a topology characteristic for the UbiD protein family" [PMID: 23671667](https://pubmed.ncbi.nlm.nih.gov/23671667/). The central split β-barrel is the flavin/prFMN-binding module (a flavin-reductase-like fold), and the C-terminal domain is diagnostic of the family. The family is functionally diverse: "considerable variation exists in the many branches of the UbiD family tree" [PMID: 28754323](https://pubmed.ncbi.nlm.nih.gov/28754323/). The canonical ubiquinone-pathway UbiD (to which Q88CG8 belongs) is distinct from other branches catalyzing (de)carboxylation of ferulate, phenazine-1-carboxylate, furandicarboxylate, and other aromatic/unsaturated acids used in lignin and aromatic-compound biotransformation.

### Finding 6 — Curated structural/catalytic specifics of Q88CG8

UniProt curation of Q88CG8 provides the following organism-specific annotations, consistent with the family: **Function** — "Catalyzes the decarboxylation of 3-octaprenyl-4-hydroxy benzoate to 2-octaprenylphenol, an intermediate step in ubiquinone biosynthesis"; **Cofactor** — "Binds 1 prenylated FMN per subunit"; **Subunit** — "Homohexamer"; an annotated **Active Site** functioning as a "Proton donor"; and family assignment to **UbiD**. The catalyzed reaction is mapped to **RHEA:41680** (3-octaprenyl-4-hydroxybenzoate = 2-octaprenylphenol + CO₂), **EC 4.1.1.98**.

### Finding 7 — UbiD (de)carboxylation is reversible with broad substrate scope

UbiD-family enzymes catalyze **reversible** (de)carboxylation of aromatic and aliphatic/acrylic substrates via prFMN. The reverse (carboxylation) direction is physiologically relevant: "It has been proposed that the first step in anaerobic microbial degradation of recalcitrant aromatic compounds is a UbiD-mediated carboxylation" [PMID: 32719558](https://pubmed.ncbi.nlm.nih.gov/32719558/), and these enzymes are exploited for enzymatic C–H carboxylation. The family is enormous — "There are now ∼35 000 protein sequences annotated as hypothetical UbiD-like enzymes" [PMID: 38837123](https://pubmed.ncbi.nlm.nih.gov/38837123/) — spanning dozens of decarboxylase subfamilies. Substrate handling differs by chemistry: turnover of bulky aromatic substrates requires **prFMN-binding-domain motion**, since "during aromatic acid decarboxylation, substantial rearrangement of the substrate aromatic moiety associated with covalent catalysis presents a molecular dynamic challenge" [PMID: 34417452](https://pubmed.ncbi.nlm.nih.gov/34417452/), whereas smaller acrylic substrates react within a closed active site. This domain dynamics is directly relevant to UbiD, whose physiological substrate carries a very bulky polyprenyl-hydroxybenzoate moiety.

### Finding 8 — Q88CG8 localizes to the cytoplasmic face of the cell membrane and binds a metal ion

UniProt curated keywords for Q88CG8 place its subcellular location at the **Cell membrane** — specifically, HAMAP-Rule MF_01636 annotates UbiD as a **peripheral membrane protein on the cytoplasmic side**. Additional keywords include **Manganese**, **Metal-binding**, **FMN**, **Decarboxylase**, and **Ubiquinone biosynthesis**. Structurally, the *P. aeruginosa* PA0254 UbiD structure shows a conserved **divalent-metal site** (Mg²⁺, ligated by invariant His and Glu residues) adjacent to the active-site cleft [PMID: 23671667](https://pubmed.ncbi.nlm.nih.gov/23671667/). This peripheral, cytoplasmic-side localization is fully consistent with the finding that UQ biosynthesis (including UbiD) is executed by a soluble cytoplasmic Ubi metabolon [PMID: 30686758](https://pubmed.ncbi.nlm.nih.gov/30686758/).

### Finding 9 — *P. putida* KT2440 encodes a cognate UbiX (Q88QE6) that supplies prFMN

A UniProt query of *P. putida* KT2440 (taxon 160488) returns **Q88QE6 "Flavin prenyltransferase UbiX"**, the partner enzyme that synthesizes prFMN. Because UbiD (Q88CG8) is catalytically inert without prFMN, the presence of a cognate UbiX in the same genome establishes a **complete, functional UbiX–UbiD prFMN-dependent decarboxylation module** in *P. putida*. This mirrors the tightly linked UbiX/UbiD systems characterized in *E. coli* and yeast [PMID: 25647642](https://pubmed.ncbi.nlm.nih.gov/25647642/); [PMID: 26083743](https://pubmed.ncbi.nlm.nih.gov/26083743/).

### Finding 10 — *Pseudomonas* uses ubiquinone-9, so the physiological substrate carries a nonaprenyl chain

Chemotaxonomic data show that **ubiquinone-9 (Q-9)** is the characteristic respiratory quinone of *Pseudomonas* and its close relatives. For a Pseudomonadales isolate whose closest cultivated neighbor is *Pseudomonas putida* R43, "The only respiratory quinone detected was ubiquinone-9 (Q-9)" [PMID: 27054961](https://pubmed.ncbi.nlm.nih.gov/27054961/). Therefore, although the enzyme name and annotation use "octaprenyl" (inherited from *E. coli*, which makes Q-8), the physiological substrate and product in *P. putida* bear a **C45 nonaprenyl (9-isoprene) tail**. The reaction in this organism is precisely: **decarboxylation of 3-nonaprenyl-4-hydroxybenzoate → 2-nonaprenylphenol + CO₂**. The enzyme's catalytic chemistry is identical; only the chain length of the isoprenoid tail differs.

---

## Mechanistic Model / Interpretation

UbiD occupies a single, well-defined position in the bacterial ubiquinone (coenzyme Q) biosynthetic pathway: it removes the carboxyl group from the aromatic ring of the polyprenylated 4-hydroxybenzoate intermediate. The following diagram places UbiD in its pathway context (chain length shown for *P. putida*, which makes Q-9):

```
   4-hydroxybenzoate (4-HB)
            |
            |  UbiA (polyprenyltransferase; attaches C45 nonaprenyl tail)
            v
   3-nonaprenyl-4-hydroxybenzoate  ────────────────┐
            |                                        │  prFMN cofactor
            |  UbiD  (Q88CG8, PP_5213)               │  supplied by
            |  EC 4.1.1.98                           │  UbiX (Q88QE6)
            |  requires prFMN (1 per subunit)        │  via FMN + DMAP/DMAPP
            v                                        │
   2-nonaprenylphenol  +  CO2  <────────────────────┘
            |
            |  UbiG, UbiH, UbiE, UbiF ... (ring hydroxylations/methylations)
            v
   Ubiquinone-9 (Coenzyme Q9)  →  inserted into inner membrane
                                   → respiratory electron transport
```

**Cofactor logic.** The unusual chemistry of a non-oxidative decarboxylation on an aromatic ring is made possible by prFMN. UbiX first builds prFMN by prenylating FMN (adding a fourth ring across N5–C6); oxidative maturation then generates the iminium/azomethine-ylide species. In the mature cofactor, the ylide behaves as a 1,3-dipole. The substrate's reactive group docks over the ylide, and a reversible 1,3-dipolar cycloaddition forms a covalent substrate–cofactor adduct; CO₂ is then eliminated and the product released. Because the cycloaddition is reversible, UbiD-family enzymes can run in either the decarboxylation or carboxylation direction depending on conditions — the basis for both their physiological reverse-direction roles in anaerobic aromatic degradation and their biocatalytic exploitation.

**Spatial logic.** Although the end product ubiquinone is a membrane lipid and UbiD is annotated as a peripheral membrane protein on the cytoplasmic side, the enzyme physically works within a **soluble cytoplasmic metabolon**. This resolves an apparent paradox: the substrate is extremely hydrophobic (a C45 isoprenoid tail), yet the reaction runs in the aqueous cytosol. The metabolon's UbiJ SCP2 lipid-binding domain sequesters the hydrophobic tail, presenting the reactive aromatic head group to the successive Ubi enzymes — including UbiD — in an assembly-line fashion. UbiD's own bulky substrate additionally demands prFMN-domain motion, consistent with the "molecular dynamic challenge" observed for aromatic decarboxylation across the family.

The table below summarizes the enzyme's key properties as they apply to Q88CG8:

| Property | Value | Basis |
|---|---|---|
| Gene / locus | *ubiD* / PP_5213 | UniProt Q88CG8 |
| Enzyme name | 3-octaprenyl-4-hydroxybenzoate carboxy-lyase | UniProt / HAMAP MF_01636 |
| EC number | 4.1.1.98 | UniProt / HAMAP |
| Reaction (RHEA) | 3-octaprenyl-4-hydroxybenzoate → 2-octaprenylphenol + CO₂ (RHEA:41680) | UniProt |
| Physiological substrate in *P. putida* | 3-**nonaprenyl**-4-hydroxybenzoate (Q-9 organism) | [PMID: 27054961](https://pubmed.ncbi.nlm.nih.gov/27054961/) |
| Cofactor | 1 prenylated FMN (prFMN) per subunit | UniProt; [PMID: 26083743](https://pubmed.ncbi.nlm.nih.gov/26083743/) |
| Cofactor supplier | UbiX (Q88QE6 in KT2440) | UniProt; [PMID: 26083743](https://pubmed.ncbi.nlm.nih.gov/26083743/) |
| Mechanism | Reversible 1,3-dipolar cycloaddition | [PMID: 26083754](https://pubmed.ncbi.nlm.nih.gov/26083754/) |
| Metal | Divalent metal (Mn/Mg), His/Glu-ligated | UniProt; [PMID: 23671667](https://pubmed.ncbi.nlm.nih.gov/23671667/) |
| Oligomeric state | Homohexamer | UniProt |
| Domain architecture | N-terminal α/β + central split β-barrel + C-terminal α/β | [PMID: 23671667](https://pubmed.ncbi.nlm.nih.gov/23671667/) |
| Localization | Peripheral membrane protein, cytoplasmic side; functions in soluble Ubi metabolon | UniProt; [PMID: 30686758](https://pubmed.ncbi.nlm.nih.gov/30686758/) |
| Pathway | Ubiquinone (coenzyme Q) biosynthesis | Multiple |

---

## Evidence Base

| PMID | Title (abbreviated) | How it supports the annotation |
|---|---|---|
| [23671667](https://pubmed.ncbi.nlm.nih.gov/23671667/) | *Structural insights into the UbiD family from PA0254 (P. aeruginosa)* | Direct structure of a *Pseudomonas* UbiD ortholog; defines the three-domain fold, the reaction (3-polyprenyl-4-HB → 2-polyprenylphenol), and the conserved divalent-metal site. Strongest structural evidence for the family in the target genus. |
| [26083743](https://pubmed.ncbi.nlm.nih.gov/26083743/) | *UbiX is a flavin prenyltransferase required for bacterial ubiquinone biosynthesis* | Establishes prFMN as the UbiX-made cofactor required for UbiD activity, its chemical structure, and the UbiX/UbiD role in decarboxylating the octaprenyl-4-hydroxybenzoate precursor. |
| [26083754](https://pubmed.ncbi.nlm.nih.gov/26083754/) | *New cofactor supports unsaturated acid decarboxylation via 1,3-dipolar cycloaddition* | Provides the catalytic mechanism (azomethine ylide / 1,3-dipolar cycloaddition) and the structural basis for reversible (de)carboxylation. |
| [32951834](https://pubmed.ncbi.nlm.nih.gov/32951834/) | *Biochemistry of prenylated-FMN enzymes* | Confirms oxidative maturation of prFMN to the active iminium species required by UbiD. |
| [25647642](https://pubmed.ncbi.nlm.nih.gov/25647642/) | *Isofunctional PAD1 and UbiX catalyze formation of a novel cofactor* | Shows the same modified-FMN cofactor is shared by UbiD (ubiquinone) and FDC (aromatic acids); links UbiX activity to 4-hydroxy-3-polyprenylbenzoate decarboxylation. |
| [17889824](https://pubmed.ncbi.nlm.nih.gov/17889824/) | *Role of UbiX in E. coli coenzyme Q biosynthesis* | Genetic loss-of-function: disrupting the UbiX/UbiD decarboxylation step causes accumulation of 4-hydroxy-3-octaprenyl-benzoate and low Q, localizing UbiD's step in the pathway. |
| [30686758](https://pubmed.ncbi.nlm.nih.gov/30686758/) | *A Soluble Metabolon Synthesizes the Isoprenoid Lipid Ubiquinone* | Demonstrates that UQ biosynthesis (including UbiD) occurs in a soluble cytoplasmic ~1-MDa metabolon, defining the enzyme's operational localization. |
| [36142227](https://pubmed.ncbi.nlm.nih.gov/36142227/) | *Functional role of UbiJ-UbiK* | Explains how the SCP2 domain of UbiJ solubilizes hydrophobic UQ intermediates within the cytosolic complex. |
| [28754323](https://pubmed.ncbi.nlm.nih.gov/28754323/) | *The UbiX-UbiD system* | Reviews family diversity; distinguishes the ubiquinone branch from aromatic-acid decarboxylase branches. |
| [34417452](https://pubmed.ncbi.nlm.nih.gov/34417452/) | *UbiD domain dynamics underpins aromatic decarboxylation* | Shows bulky aromatic substrates require prFMN-domain motion — relevant to UbiD's large polyprenyl substrate. |
| [32719558](https://pubmed.ncbi.nlm.nih.gov/32719558/) | *Enzymatic C-H activation through CO2 fixation* | Documents reversibility and the physiologically relevant carboxylation direction. |
| [38837123](https://pubmed.ncbi.nlm.nih.gov/38837123/) | *Surveying aromatic decarboxylations by prFMN enzymes* | Quantifies the ~35,000-sequence breadth of the UbiD family and its substrate diversity. |
| [27054961](https://pubmed.ncbi.nlm.nih.gov/27054961/) | *Ventosimonas gracilis (Pseudomonadales)* | Chemotaxonomic evidence that Q-9 is the respiratory quinone of Pseudomonas relatives, fixing the isoprenoid chain length of the UbiD substrate in *P. putida*. |
| [40343387](https://pubmed.ncbi.nlm.nih.gov/40343387/) | *QM study of furandicarboxylic acid decarboxylase (HmfF)* | Cautionary note: some UbiD-family members may use nucleophilic-attack rather than concerted cycloaddition mechanisms. |

**Identity verification.** All mandatory verification checks pass. The gene symbol *ubiD* matches the protein description (3-octaprenyl-4-hydroxybenzoate carboxy-lyase); the organism is *P. putida* KT2440; the UbiD-family domains (IPR002830, IPR023677, etc.) align with the three-domain architecture reported in structural literature; and no conflicting literature for a different gene with the same symbol was encountered. The assignment is unambiguous.

---

## Limitations and Knowledge Gaps

1. **No enzyme-specific biochemistry for Q88CG8 itself.** The functional assignment for *P. putida* PP_5213 rests on (a) UniProt/HAMAP curation and (b) direct characterization of orthologs (*E. coli* UbiD, *P. aeruginosa* PA0254, and the model enzyme Fdc1). No purified-enzyme kinetics (kcat, Km), crystal structure, or gene-knockout phenotype has been reported specifically for the KT2440 protein. The inference is strong by homology but not directly demonstrated.

2. **Substrate chain length inferred, not measured.** The conclusion that the physiological substrate carries a nonaprenyl (Q-9) tail is inferred from *Pseudomonas* chemotaxonomy rather than from a direct assay of the KT2440 enzyme with defined-chain substrates. UbiD is known to be relatively permissive about tail length, so this is a well-supported inference but remains indirect.

3. **Mechanistic universality.** The 1,3-dipolar cycloaddition model derives chiefly from Fdc1 and related aromatic-acid decarboxylases. At least one computational study (HmfF) argues for an alternative nucleophilic mechanism, so the exact microscopic mechanism for the polyprenyl-hydroxybenzoate substrate has not been experimentally resolved for UbiD.

4. **Metal identity.** UniProt keywords list both Manganese and generic metal-binding, while the PA0254 structure modeled Mg²⁺. The physiologically relevant divalent metal for the *P. putida* enzyme is not firmly established.

5. **Metabolon composition in Pseudomonas.** The soluble Ubi metabolon was characterized in *E. coli*. Whether *P. putida* assembles an identical complex (including UbiJ/UbiK orthologs and the same stoichiometry) has not been directly shown, though the pathway is conserved.

---

## Proposed Follow-up Experiments / Actions

1. **Direct biochemical characterization of PP_5213.** Heterologously express and purify Q88CG8 (co-expressing UbiX Q88QE6 to load prFMN, or reconstituting with purified prFMN), then measure decarboxylation of synthetic 3-prenyl-4-hydroxybenzoate analogs of varying chain length to confirm activity and probe chain-length preference (nonaprenyl vs. octaprenyl vs. short-chain surrogates).

2. **Genetic complementation / knockout.** Delete *ubiD* (PP_5213) in KT2440 and test for (a) loss of Q-9, (b) accumulation of 3-nonaprenyl-4-hydroxybenzoate, and (c) a respiratory/succinate growth defect; complement with the wild-type gene to confirm causality — mirroring the *E. coli* UbiX study [PMID: 17889824](https://pubmed.ncbi.nlm.nih.gov/17889824/).

3. **Structure determination.** Solve the crystal or cryo-EM structure of the KT2440 UbiD homohexamer with bound prFMN (and, ideally, a substrate/inhibitor) to confirm the divalent-metal identity, the proton-donor active-site residue, and the domain-dynamics required for the bulky polyprenyl substrate.

4. **Metabolon reconstitution.** Test whether *P. putida* forms a soluble Ubi metabolon by co-purification/pull-down of UbiD with UbiJ/UbiK/UbiH/UbiG orthologs from cytoplasmic extracts, quantifying UQ synthesis in the soluble fraction as done for *E. coli* [PMID: 30686758](https://pubmed.ncbi.nlm.nih.gov/30686758/).

5. **Reverse-reaction / biocatalysis assessment.** Given the family's reversible chemistry and biotechnological interest, test whether the KT2440 enzyme can catalyze carboxylation of 2-prenylphenol analogs under CO₂-rich conditions, informing potential use in enzymatic C–H carboxylation [PMID: 32719558](https://pubmed.ncbi.nlm.nih.gov/32719558/).

---

*Report compiled from 5 iterations of autonomous investigation; 10 confirmed findings; 27 papers reviewed. All functional claims are anchored to UniProt curation of Q88CG8 and to primary/structural literature on directly characterized UbiD-family orthologs.*


## Artifacts

- [OpenScientist final report](ubiD-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](ubiD-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:23671667
2. PMID:26083743
3. PMID:17889824
4. PMID:32951834
5. PMID:25647642
6. PMID:26083754
7. PMID:40343387
8. PMID:30686758
9. PMID:36142227
10. PMID:28754323
11. PMID:32719558
12. PMID:38837123
13. PMID:34417452
14. PMID:27054961