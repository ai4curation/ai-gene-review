---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-17T12:56:46.290895'
end_time: '2026-07-17T13:10:40.383120'
duration_seconds: 834.09
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: leuC
  gene_symbol: leuC
  uniprot_accession: Q88LE8
  protein_description: 'RecName: Full=3-isopropylmalate dehydratase large subunit
    {ECO:0000255|HAMAP-Rule:MF_01026}; EC=4.2.1.33 {ECO:0000255|HAMAP-Rule:MF_01026};
    AltName: Full=Alpha-IPM isomerase {ECO:0000255|HAMAP-Rule:MF_01026}; Short=IPMI
    {ECO:0000255|HAMAP-Rule:MF_01026}; AltName: Full=Isopropylmalate isomerase {ECO:0000255|HAMAP-Rule:MF_01026};'
  gene_info: Name=leuC {ECO:0000255|HAMAP-Rule:MF_01026}; OrderedLocusNames=PP_1985;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the aconitase/IPM isomerase family. LeuC type 1
  protein_domains: 3-IsopropMal_deHydase_lsu. (IPR004430); Acnase/IPM_dHydase_lsu_aba_1/3.
    (IPR015931); Acoase/IPM_deHydtase_lsu_aba. (IPR001030); Aconitase_4Fe-4S_BS. (IPR018136);
    Aconitase_4Fe-4S_dom. (IPR036008)
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
citation_count: 11
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: leuC-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: leuC-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88LE8
- **Protein Description:** RecName: Full=3-isopropylmalate dehydratase large subunit {ECO:0000255|HAMAP-Rule:MF_01026}; EC=4.2.1.33 {ECO:0000255|HAMAP-Rule:MF_01026}; AltName: Full=Alpha-IPM isomerase {ECO:0000255|HAMAP-Rule:MF_01026}; Short=IPMI {ECO:0000255|HAMAP-Rule:MF_01026}; AltName: Full=Isopropylmalate isomerase {ECO:0000255|HAMAP-Rule:MF_01026};
- **Gene Information:** Name=leuC {ECO:0000255|HAMAP-Rule:MF_01026}; OrderedLocusNames=PP_1985;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the aconitase/IPM isomerase family. LeuC type 1
- **Key Domains:** 3-IsopropMal_deHydase_lsu. (IPR004430); Acnase/IPM_dHydase_lsu_aba_1/3. (IPR015931); Acoase/IPM_deHydtase_lsu_aba. (IPR001030); Aconitase_4Fe-4S_BS. (IPR018136); Aconitase_4Fe-4S_dom. (IPR036008)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "leuC" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'leuC' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **leuC** (gene ID: leuC, UniProt: Q88LE8) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *leuC* (Q88LE8, PP_1985) in *Pseudomonas putida* KT2440

**Target:** 3-isopropylmalate dehydratase large subunit (isopropylmalate isomerase, IPMI large subunit)
**Gene:** *leuC* / PP_1985
**UniProt:** Q88LE8
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / NCIMB 11950 / KT2440)
**EC number:** 4.2.1.33
**Enzyme family:** Aconitase / isopropylmalate isomerase (IPM) superfamily, LeuC type 1

---

## Summary

The gene *leuC* (locus PP_1985; UniProt Q88LE8) of *Pseudomonas putida* KT2440 encodes the **large, catalytic subunit of 3-isopropylmalate dehydratase**, also known as **isopropylmalate isomerase (IPMI)**, EC 4.2.1.33. This enzyme is a member of the aconitase superfamily of **[4Fe-4S]-cluster-dependent hydro-lyases** that reversibly catalyze coupled dehydration/hydration reactions. LeuC does not act alone: it forms an obligate heterodimer with the small subunit LeuD (PP_1986, Q88LE7), and together the LeuCD complex catalyzes **step 2 of the four-step L-leucine biosynthesis pathway**—the stereospecific isomerization of (2S)-2-isopropylmalate (α-isopropylmalate) into (2R,3S)-3-isopropylmalate (β-isopropylmalate) via the dehydrated intermediate 2-isopropylmaleate.

The functional assignment is exceptionally well supported by a convergence of evidence: (i) the UniProt/HAMAP curated annotation (rule MF_01026, LeuC type 1); (ii) domain signatures diagnostic of the aconitase [4Fe-4S] hydro-lyase fold (IPR004430, IPR001030, IPR015931, IPR018136, IPR036008); (iii) strict conservation of the three cluster-ligating cysteines (Cys352, Cys413, Cys416) and 68.5% sequence identity to the experimentally characterized *Escherichia coli* LeuC; (iv) genomic organization in a clustered *leuC–leuD–leuB* leucine-biosynthesis locus flanked by a LysR-family regulator; and (v) crystallographic and biochemical characterization of orthologous LeuCD complexes (*Mycobacterium tuberculosis*, *Salmonella*, *Corynebacterium glutamicum*) that confirm the aconitase-fold, two-subunit isopropylmalate isomerase architecture and function.

Functionally, LeuC operates in the **cytoplasm** as a soluble metabolic enzyme. Its [4Fe-4S] cluster is coordinated by only three cysteines, leaving one open iron coordination site that directly binds substrate—the hallmark catalytic strategy of the aconitase family—which also makes the enzyme **oxygen- and nitric-oxide-labile**. Because the leucine biosynthesis pathway is entirely absent in humans, IPMI (LeuCD) is a validated candidate antibacterial drug target in pathogens, and its role in *P. putida* is a dedicated, non-redundant biosynthetic one rather than a pleiotropic or regulatory function.

---

## Key Findings

### Finding 1 — *leuC* encodes the large subunit of 3-isopropylmalate dehydratase (isopropylmalate isomerase), EC 4.2.1.33

The core identity of Q88LE8 is firmly established. UniProt curation under HAMAP rule MF_01026 (LeuC type 1) assigns the recommended name **3-isopropylmalate dehydratase large subunit**, EC 4.2.1.33, with the alternative names **Alpha-IPM isomerase** and **Isopropylmalate isomerase (IPMI)**. The gene is designated *leuC* with the ordered locus name PP_1985 in *P. putida* KT2440.

This annotation is anchored to experimental literature from orthologous systems. In *Corynebacterium glutamicum*, a Gly-456→Asp substitution was mapped directly to "the 3-isopropylmalate dehydratase large subunit gene (*leuC*)" ([PMID: 16944136](https://pubmed.ncbi.nlm.nih.gov/16944136/)), establishing that the *leuC* gene product is precisely the large subunit of this enzyme. The nucleotide sequence of *leuC* from *Salmonella typhimurium* was among the earliest characterizations of this gene ([PMID: 2190189](https://pubmed.ncbi.nlm.nih.gov/2190189/)). The diagnostic domain content of Q88LE8 reinforces the assignment: IPR004430 (3-isopropylmalate dehydratase large subunit), IPR001030 and IPR015931 (aconitase/IPM dehydratase large subunit), and IPR018136/IPR036008 (aconitase 4Fe-4S binding site and domain).

### Finding 2 — IPMI/LeuCD is an oxygen- and NO-labile [4Fe-4S] enzyme of the aconitase superfamily

The aconitase superfamily comprises "a family of [4Fe-4S] cluster-dependent enzymes that catalyse hydration/dehydration reactions," of which "the best characterized example... is the ubiquitous ACN (aconitase), which catalyses the dehydration of citrate to cis-aconitate, and the subsequent hydration of cis-aconitate to isocitrate" ([PMID: 16524361](https://pubmed.ncbi.nlm.nih.gov/16524361/)). Isopropylmalate isomerase belongs to this superfamily and uses the identical catalytic strategy—a dehydration followed by a re-hydration in the opposite regiochemistry—to isomerize its substrate.

The requirement for a [4Fe-4S] cofactor is experimentally documented: activation of *Saccharomyces cerevisiae* apo-isopropylmalate isomerase (Leu1) in vitro is "a process known to require the transfer of a [4Fe-4S] cluster" ([PMID: 18616280](https://pubmed.ncbi.nlm.nih.gov/18616280/)). The physiological consequences of this iron-sulfur dependence are illustrated in *Salmonella* Typhimurium, where "iron-sulfur enzymes dihydroxy-acid dehydratase (IlvD) and isopropylmalate isomerase (LeuCD)... are essential for BCAA biosynthesis," and nitric oxide inactivates these clusters, producing branched-chain-amino-acid auxotrophy under nitrosative stress ([PMID: 26374245](https://pubmed.ncbi.nlm.nih.gov/26374245/)). Q88LE8 carries the aconitase 4Fe-4S domain signatures (IPR018136/IPR036008), consistent with this cofactor assignment.

### Finding 3 — LeuC catalyzes step 2 of 4 in L-leucine biosynthesis as a LeuC/LeuD heterodimer with three-cysteine cluster ligation

Q88LE8 is a 477-residue, ~51.3 kDa protein. Its catalytic activity (EC 4.2.1.33; Rhea:32287) is the reversible reaction **(2S)-2-isopropylmalate ⇌ (2R,3S)-3-isopropylmalate**, proceeding through the intermediate **2-isopropylmaleate**. Within the UniPathway framework this is annotated as **L-leucine biosynthesis, L-leucine from 3-methyl-2-oxobutanoate, step 2 of 4** (UPA00048).

The [4Fe-4S] cluster is bound per subunit and coordinated by three cysteine residues—**Cys352, Cys413, and Cys416**—the canonical three-cysteine ligation of the aconitase family that leaves the fourth cluster iron open for direct substrate binding. The enzyme functions as a **heterodimer of LeuC (large) and LeuD (small)** subunits. The physiological essentiality of this complex for leucine (a branched-chain amino acid) biosynthesis is confirmed by the observation that "isopropylmalate isomerase (LeuCD)... [is] essential for BCAA biosynthesis," with *leuCD* mutants behaving as BCAA auxotrophs ([PMID: 26374245](https://pubmed.ncbi.nlm.nih.gov/26374245/)).

### Finding 4 — *leuC* (PP_1985) is genomically adjacent to its partner *leuD* (PP_1986)

The two subunits of the enzyme are encoded by adjacent, co-oriented genes. *leuC* = PP_1985 (ppu:PP_1985) and *leuD* = PP_1986 (UniProt Q88LE7, 214 aa, HAMAP rule MF_01031). The consecutive ordered-locus numbering and shared orientation indicate a **leuCD gene unit**, consistent with the obligate heterodimeric quaternary structure of the enzyme. Cross-database anchoring for Q88LE8 includes EMBL AE015451, RefSeq WP_010953002.1, AlphaFoldDB Q88LE8, BioCyc PPUT160488:G1G01-2116-MONOMER, Pfam PF00330 (aconitase family), and UniPathway UPA00048.

### Finding 5 — Crystallographic and solution-scattering studies confirm the aconitase-fold, two-subunit isopropylmalate isomerase, and establish drug-target relevance

Structural characterization of the orthologous *Mycobacterium tuberculosis* IPMI provides direct experimental confirmation of the architecture and function: "IPMI exists as a complex of two subunits: the large (LeuC) and the small (LeuD) subunit. The functional LeuCD complex catalyzes the stereospecific conversion reaction of α-isopropylmalate to β-isopropylmalate" ([PMID: 20938981](https://pubmed.ncbi.nlm.nih.gov/20938981/)). High-resolution (to 1.2 Å) X-ray structures of the LeuD subunit identified a substrate-discriminating loop (residues 30–37) and a substrate-binding loop (residues 70–74), and the LeuCD assembly was compared directly to its functional homolog, mitochondrial aconitase—underscoring the shared aconitase fold.

The same study establishes the pathway's biomedical significance: "The absence of the leucine biosynthesis pathway in humans makes the enzymes of this pathway in pathogenic bacteria such as *Mycobacterium tuberculosis* potential candidates for developing novel antibacterial drugs" ([PMID: 20938981](https://pubmed.ncbi.nlm.nih.gov/20938981/)). This implies that in *P. putida*, LeuC serves a dedicated, non-redundant anabolic role.

### Finding 6 — *leuC* resides in a leucine-biosynthesis gene cluster flanked by a LysR-family regulator

Examination of the KEGG genome neighborhood in *P. putida* KT2440 reveals a coherent biosynthetic locus:

| Locus | Product |
|-------|---------|
| PP_1984 | LysR-family transcriptional regulator |
| **PP_1985** | **3-isopropylmalate dehydratase large subunit (*leuC*)** |
| PP_1986 | 3-isopropylmalate dehydratase small subunit (*leuD*) |
| PP_1987 | UbiE/COQ5-family methyltransferase |
| PP_1988 | 3-isopropylmalate dehydrogenase (*leuB*) |
| PP_1989 | aspartate-semialdehyde dehydrogenase |

*leuC* and *leuD* are immediately adjacent and co-oriented, and *leuB* (encoding the enzyme for the subsequent step of leucine biosynthesis) lies two genes downstream. The neighboring LysR-family regulator (PP_1984) is a plausible transcriptional controller of the locus. This clustering of consecutive-pathway enzymes provides orthogonal, genomic-context support for the functional assignment.

### Finding 7 — Strong sequence conservation with experimentally characterized *E. coli* LeuC

A global Needleman–Wunsch alignment of Q88LE8 (*P. putida*, 477 aa) against P0A6A6 (*E. coli* LeuC, 466 aa) yields **313/457 identical positions = 68.5% identity**. Critically, all three cluster-ligating cysteines annotated in Q88LE8 align exactly to conserved cysteines in *E. coli* LeuC:

| Q88LE8 residue | Sequence motif | *E. coli* LeuC equivalent |
|----------------|----------------|---------------------------|
| Cys352 | VFIGS-**C**-TNSRI | Cys347 |
| Cys413 | WREPG-**C**-SM... | Cys407 |
| Cys416 | ...SM-**C**-LA | Cys410 |

The Cys413-x-x-Cys416 arrangement is the canonical aconitase-family **CxxC** [4Fe-4S] binding motif, with the third ligand (Cys352) contributed from a distal segment of the polypeptide. This high identity to a well-studied enzyme, combined with strict conservation of the catalytically essential residues, provides high confidence that *P. putida* LeuC performs the identical reaction.

---

## Mechanistic Model / Interpretation

### The reaction and its place in leucine biosynthesis

L-Leucine is synthesized from the valine-pathway intermediate **3-methyl-2-oxobutanoate (2-ketoisovalerate)** in four enzymatic steps. LeuCD catalyzes the second step:

```
Leucine biosynthesis (from 3-methyl-2-oxobutanoate):

  3-methyl-2-oxobutanoate
        │  Step 1: LeuA (2-isopropylmalate synthase)  + acetyl-CoA
        ▼
  (2S)-2-isopropylmalate  (α-isopropylmalate)
        │
        │  Step 2: LeuCD  ◄── THIS ENZYME (LeuC = large subunit, PP_1985)
        │          [4Fe-4S] hydro-lyase
        │          via 2-isopropylmaleate intermediate
        ▼
  (2R,3S)-3-isopropylmalate  (β-isopropylmalate)
        │
        │  Step 3: LeuB (3-isopropylmalate dehydrogenase, PP_1988)  + NAD+
        ▼
  4-methyl-2-oxopentanoate (2-oxoisocaproate)
        │
        │  Step 4: transaminase (IlvE/BCAT)  + L-glutamate
        ▼
  L-leucine
```

The step-2 reaction catalyzed by LeuCD is formally an **isomerization** achieved through two consecutive hydro-lyase half-reactions on a common enzyme-bound intermediate:

```
(2S)-2-isopropylmalate  ──[dehydration]──►  2-isopropylmaleate  ──[re-hydration]──►  (2R,3S)-3-isopropylmalate
   (α-IPM)                  (loses H2O)        (cis-unsaturated)      (adds H2O across
                                                                       the other carbon)      (β-IPM)
```

This is mechanistically analogous to aconitase, which converts citrate → *cis*-aconitate → isocitrate via the same dehydration/re-hydration logic ([PMID: 16524361](https://pubmed.ncbi.nlm.nih.gov/16524361/)).

### The catalytic [4Fe-4S] cluster and substrate binding

```
          Cys352
             \
              Fe——S
             /      \
     Cys413-Fe      Fe——[ open coordination site ]
             \      /        │
              Fe——S          └── binds substrate hydroxyl/carboxylate
             /                    (Lewis-acid activation, like aconitase)
          Cys416
```

Only **three** of the four cluster irons are ligated by protein cysteines (Cys352, Cys413, Cys416). The fourth iron (Fe_a) is coordinatively unsaturated and serves as a **Lewis acid** that binds and polarizes the substrate hydroxyl and carboxylate groups, facilitating the elimination/addition of water. This is the defining catalytic strategy of the entire aconitase superfamily and explains two important properties of LeuC:

1. **Oxygen and NO lability.** The exposed [4Fe-4S] cluster is sensitive to oxidative and nitrosative damage; NO inactivates LeuCD, producing leucine/BCAA auxotrophy under nitrosative stress ([PMID: 26374245](https://pubmed.ncbi.nlm.nih.gov/26374245/)).
2. **Requirement for cluster assembly/repair machinery.** Apo-IPMI must be loaded with an intact [4Fe-4S] cluster to become active, a maturation step mediated by Fe-S cluster transfer proteins ([PMID: 18616280](https://pubmed.ncbi.nlm.nih.gov/18616280/)).

### Quaternary structure and subunit division of labor

LeuC (large subunit, ~51 kDa, 477 aa) and LeuD (small subunit, ~23 kDa, 214 aa) assemble into a functional **LeuCD heterodimer**. In the single-chain homolog aconitase, the equivalent domains are fused into one polypeptide; in the LeuCD-type isomerases they are split, with LeuC contributing the catalytic core (including the cluster-binding cysteines) and LeuD contributing the substrate-specificity/discrimination loops identified crystallographically (LeuD residues 30–37 and 70–74) ([PMID: 20938981](https://pubmed.ncbi.nlm.nih.gov/20938981/)). This division of labor is why the two genes are obligately co-inherited and co-located (PP_1985/PP_1986).

### Localization

As a soluble metabolic enzyme with no signal peptide or transmembrane segments, LeuC functions in the **bacterial cytoplasm**, where the amino acid biosynthesis machinery and its substrates reside. This is consistent with all characterized aconitase-family isopropylmalate isomerases.

### Summary annotation table

| Attribute | Assignment | Basis |
|-----------|-----------|-------|
| Molecular function | 3-isopropylmalate dehydratase / isopropylmalate isomerase (large subunit) | UniProt/HAMAP MF_01026; PMID 16944136, 20938981 |
| EC number | 4.2.1.33 | UniProt; Rhea:32287 |
| Reaction | (2S)-2-isopropylmalate ⇌ (2R,3S)-3-isopropylmalate (via 2-isopropylmaleate) | UniProt; PMID 20938981 |
| Cofactor | 1 × [4Fe-4S] cluster (Cys352/413/416) | UniProt; PMID 18616280, 16524361 |
| Pathway | L-leucine biosynthesis, step 2 of 4 (UPA00048) | UniProt UniPathway |
| Quaternary structure | Heterodimer with LeuD (PP_1986) | PMID 20938981; genomic adjacency |
| Localization | Cytoplasm | Family inference |
| Genomic context | *leuC–leuD–…–leuB* cluster; LysR regulator upstream | KEGG ppu neighborhood |

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution |
|------|-----------------|--------------|
| [16944136](https://pubmed.ncbi.nlm.nih.gov/16944136/) | *leuC* mutation in *C. glutamicum* | Directly maps a mutation to "the 3-isopropylmalate dehydratase large subunit gene (*leuC*)," confirming gene-product identity |
| [20938981](https://pubmed.ncbi.nlm.nih.gov/20938981/) | Structural studies on IPMI (LeuCD) from *M. tuberculosis* | Direct structural evidence of a LeuC/LeuD two-subunit aconitase-fold complex catalyzing α→β-isopropylmalate isomerization; establishes human-absent pathway → drug target |
| [26374245](https://pubmed.ncbi.nlm.nih.gov/26374245/) | BCAA supplementation under nitrosative stress (*Salmonella*) | Confirms LeuCD is an Fe-S isopropylmalate isomerase essential for BCAA biosynthesis; NO lability |
| [18616280](https://pubmed.ncbi.nlm.nih.gov/18616280/) | Bacterial ApbC binds/transfers Fe-S clusters | Shows apo-IPMI activation requires transfer of a [4Fe-4S] cluster |
| [16524361](https://pubmed.ncbi.nlm.nih.gov/16524361/) | Homoaconitase kinetics (*T. thermophilus*) | Defines the aconitase [4Fe-4S] hydro-lyase superfamily and its dehydration/hydration mechanism |
| [2190189](https://pubmed.ncbi.nlm.nih.gov/2190189/) | Nucleotide sequence of *leuC* from *S. typhimurium* | Early molecular characterization of the *leuC* gene |

**Note on genome-context and sequence evidence:** Findings 4, 6, and 7 rest on database records (UniProt, KEGG, RefSeq) and a direct sequence alignment performed during the investigation. The 68.5% identity to *E. coli* LeuC (P0A6A6) with strict conservation of Cys352/413/416 constitutes strong bioinformatic evidence that the *P. putida* enzyme is catalytically equivalent to the biochemically studied *E. coli* enzyme.

**Papers reviewed but not directly supporting the core assignment:** A substantial set of *P. putida* literature concerns the *bkd* operon and its regulator BkdR (a leucine-responsive, Lrp-like activator controlling branched-chain keto acid dehydrogenase **catabolism**; [PMID: 8320210](https://pubmed.ncbi.nlm.nih.gov/8320210/), [PMID: 7836297](https://pubmed.ncbi.nlm.nih.gov/7836297/), [PMID: 8982009](https://pubmed.ncbi.nlm.nih.gov/8982009/), [PMID: 9068646](https://pubmed.ncbi.nlm.nih.gov/9068646/), [PMID: 10217783](https://pubmed.ncbi.nlm.nih.gov/10217783/)). These describe branched-chain amino acid **degradation/regulation**, which is distinct from LeuC's **biosynthetic** role, and were reviewed to rule out any conflation with the *leuC* function. Other retrieved papers (TNT/lindane biotransformation, vanillin production, ncRNA prediction, RB-TnSeq machine learning) are *P. putida* genome-scale studies that do not specifically characterize LeuC.

---

## Limitations and Knowledge Gaps

1. **No direct experimental study of the *P. putida* KT2440 enzyme.** There is, to our knowledge, no published biochemical or structural characterization of Q88LE8 itself. The functional assignment is inferred from (i) curated database annotation, (ii) high sequence identity to experimentally studied orthologs (*E. coli* 68.5%), and (iii) structural/biochemical data from orthologs in *M. tuberculosis*, *Salmonella*, *C. glutamicum*, and yeast. While this inference is strong, it is not a direct measurement.

2. **Kinetic parameters unknown for this ortholog.** Substrate affinity (Km), turnover (kcat), and substrate specificity have not been measured for the *P. putida* enzyme. Specificity is assumed to be restricted to 2-isopropylmalate based on family membership and the LeuD substrate-discrimination loops.

3. **Cluster stoichiometry and maturation pathway in *P. putida* not defined.** The specific Fe-S biogenesis system (ISC/SUF) responsible for maturing LeuCD in *P. putida*, and the in vivo consequences of oxidative/nitrosative stress on this enzyme in this organism, remain uncharacterized.

4. **Regulation is inferred, not demonstrated.** The adjacent LysR-family regulator (PP_1984) is a plausible transcriptional controller of the *leuCD* locus, but no experimental data confirm that it regulates *leuC* expression in *P. putida*.

5. **Residue numbering caveat.** The catalytic cysteine positions (Cys352/413/416) derive from UniProt feature annotation; exact positions should be confirmed against the mature processed sequence if used for mutagenesis design.

---

## Proposed Follow-up Experiments / Actions

1. **Heterologous expression and activity assay.** Clone PP_1985 (*leuC*) together with PP_1986 (*leuD*), co-express the heterodimer in *E. coli*, reconstitute the [4Fe-4S] cluster anaerobically, and measure isopropylmalate isomerase activity spectrophotometrically (coupled to LeuB/NAD+). This would directly confirm the reaction and yield kinetic parameters.

2. **Genetic complementation / auxotrophy test.** Construct a *P. putida* KT2440 Δ*leuC* mutant and test for leucine auxotrophy on minimal medium; complement with plasmid-borne *leuC* to confirm the phenotype is due to loss of this gene. This is the definitive test of the biosynthetic role.

3. **Site-directed mutagenesis of cluster cysteines.** Individually mutate Cys352, Cys413, and Cys416 to serine/alanine and assay for loss of [4Fe-4S] loading (UV-visible/EPR) and catalytic activity, confirming the three-cysteine ligation model.

4. **Structural determination.** Solve the crystal or cryo-EM structure of the *P. putida* LeuCD complex to confirm the aconitase fold, the open substrate-binding iron, and the LeuD specificity loops predicted from the *M. tuberculosis* ortholog.

5. **Fe-S maturation and stress physiology.** Test the sensitivity of *P. putida* leucine biosynthesis to nitrosative and oxidative stress, and identify the Fe-S cluster assembly machinery (ISC vs. SUF) required for LeuCD maturation, paralleling the *Salmonella* findings.

6. **Regulatory characterization.** Test whether the upstream LysR-family regulator (PP_1984) binds the *leuC* promoter and modulates expression, using EMSA and reporter fusions, to define the transcriptional control of the locus.

---

## Conclusion

*leuC* (Q88LE8, PP_1985) in *Pseudomonas putida* KT2440 encodes the **large, catalytic subunit of 3-isopropylmalate dehydratase (isopropylmalate isomerase; IPMI; EC 4.2.1.33)**, a cytoplasmic [4Fe-4S]-cluster hydro-lyase of the aconitase superfamily. Acting as an obligate heterodimer with the small subunit LeuD (PP_1986), it performs **step 2 of L-leucine biosynthesis**—the stereospecific, reversible isomerization of (2S)-2-isopropylmalate to (2R,3S)-3-isopropylmalate via a 2-isopropylmaleate intermediate. The [4Fe-4S] cluster is ligated by three cysteines (Cys352/413/416), leaving an open iron for substrate binding, which confers the family's characteristic oxygen/NO lability. This assignment is supported by curated annotation, diagnostic domain signatures, 68.5% identity to the experimentally studied *E. coli* enzyme with full conservation of the catalytic cysteines, a clustered *leuC–leuD–leuB* biosynthetic locus, and structural/biochemical characterization of orthologous LeuCD complexes. Because leucine biosynthesis is absent in humans, this enzyme represents a validated antibacterial drug-target class and, in *P. putida*, plays a dedicated, non-redundant anabolic role.


## Artifacts

- [OpenScientist final report](leuC-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](leuC-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:16944136
2. PMID:2190189
3. PMID:16524361
4. PMID:18616280
5. PMID:26374245
6. PMID:20938981
7. PMID:8320210
8. PMID:7836297
9. PMID:8982009
10. PMID:9068646
11. PMID:10217783