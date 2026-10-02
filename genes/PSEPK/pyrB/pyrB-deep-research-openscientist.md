---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T19:58:27.967633'
end_time: '2026-08-31T21:00:06.397593'
duration_seconds: 3698.43
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: pyrB
  gene_symbol: pyrB
  uniprot_accession: Q88D30
  protein_description: 'RecName: Full=Aspartate carbamoyltransferase catalytic subunit
    {ECO:0000255|HAMAP-Rule:MF_00001}; EC=2.1.3.2 {ECO:0000255|HAMAP-Rule:MF_00001};
    AltName: Full=Aspartate transcarbamylase {ECO:0000255|HAMAP-Rule:MF_00001}; Short=ATCase
    {ECO:0000255|HAMAP-Rule:MF_00001};'
  gene_info: Name=pyrB {ECO:0000255|HAMAP-Rule:MF_00001}; OrderedLocusNames=PP_4998;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the aspartate/ornithine carbamoyltransferase
  protein_domains: Asp/Orn_carbamoyltranf_P-bd. (IPR006132); Asp/Orn_carbamoylTrfase.
    (IPR006130); Asp/Orn_carbamoylTrfase_sf. (IPR036901); Asp_carbamoyltransf. (IPR002082);
    Asp_carbamoyltransf_Asp/Orn-bd. (IPR006131)
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
citation_count: 10
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: pyrB-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: pyrB-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88D30
- **Protein Description:** RecName: Full=Aspartate carbamoyltransferase catalytic subunit {ECO:0000255|HAMAP-Rule:MF_00001}; EC=2.1.3.2 {ECO:0000255|HAMAP-Rule:MF_00001}; AltName: Full=Aspartate transcarbamylase {ECO:0000255|HAMAP-Rule:MF_00001}; Short=ATCase {ECO:0000255|HAMAP-Rule:MF_00001};
- **Gene Information:** Name=pyrB {ECO:0000255|HAMAP-Rule:MF_00001}; OrderedLocusNames=PP_4998;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the aspartate/ornithine carbamoyltransferase
- **Key Domains:** Asp/Orn_carbamoyltranf_P-bd. (IPR006132); Asp/Orn_carbamoylTrfase. (IPR006130); Asp/Orn_carbamoylTrfase_sf. (IPR036901); Asp_carbamoyltransf. (IPR002082); Asp_carbamoyltransf_Asp/Orn-bd. (IPR006131)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "pyrB" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'pyrB' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **pyrB** (gene ID: pyrB, UniProt: Q88D30) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *pyrB* (PP_4998, UniProt Q88D30) — Aspartate Carbamoyltransferase Catalytic Subunit of *Pseudomonas putida* KT2440

**Target:** UniProt **Q88D30** | Gene **pyrB** / OrderedLocusName **PP_4998** | EC **2.1.3.2**
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440)
**Date:** 2026-09-01

## Summary

The gene **pyrB** (ordered locus name **PP_4998**; UniProt accession **Q88D30**) of *Pseudomonas putida* strain KT2440 encodes the **catalytic subunit of aspartate carbamoyltransferase** (aspartate transcarbamoylase; **ATCase**; EC 2.1.3.2). ATCase catalyzes the **first committed and rate-limiting step of the de novo pyrimidine biosynthetic pathway**: the transfer of a carbamoyl group from **carbamoyl phosphate** to the α-amino group of **L-aspartate**, producing **N-carbamoyl-L-aspartate** and **inorganic phosphate**. This reaction commits the cell's metabolic flux toward uridine-5′-monophosphate (UMP), the precursor from which all other pyrimidine nucleotides are derived. The enzyme functions in the **cytoplasm** as a soluble protein.

The identity of Q88D30 as a *pyrB*/ATCase catalytic subunit is strongly supported by convergent lines of evidence: (1) UniProt's HAMAP rule-based family and domain annotation places it firmly in the aspartate/ornithine carbamoyltransferase family with all five diagnostic InterPro domains; (2) direct sequence analysis of the 334-residue Q88D30 protein reveals intact, positionally conserved catalytic motifs (the carbamoyl-phosphate-binding "STRTR" loop and the aspartate-binding "HPTQ" motif); (3) global alignment against the extensively characterized *Escherichia coli* catalytic subunit shows ~39% identity with exact conservation of the catalytic carbamoyl-phosphate-binding arginine; and (4) the KT2440 genome confirms the experimentally described *pyrB–pyrC′* gene arrangement.

A distinctive and important feature of the *P. putida* enzyme, established by direct biochemical and genetic characterization, is that its **quaternary structure differs fundamentally from the textbook *E. coli* ATCase**. Rather than the *E. coli* class-C architecture of six catalytic (PyrB) plus six regulatory (PyrI) chains, the *Pseudomonas*-type enzyme is a **dodecamer of six catalytic PyrB subunits and six catalytically inactive dihydroorotase-homolog PyrC′ subunits** (encoded by the adjacent PP_4999). *P. putida* possesses **no separate PyrI regulatory subunit**; instead, the regulatory nucleotide-binding site resides in a **unique N-terminal extension of PyrB itself**, and the inactive PyrC′ serves a purely structural role, maintaining the dodecameric assembly required for activity. Consequently, UniProt's rule-propagated "2C₃:3R₂ heterododecamer with six PyrI chains" subunit annotation is **inaccurate for this organism**, while its FUNCTION, CATALYTIC ACTIVITY, and PATHWAY annotations remain correct.

---

## Key Findings

### Finding 1 — *pyrB* (Q88D30) encodes the catalytic subunit of aspartate carbamoyltransferase (ATCase, EC 2.1.3.2)

UniProt Q88D30 annotates PP_4998/*pyrB* as the ATCase catalytic subunit (EC 2.1.3.2), a member of the aspartate/ornithine carbamoyltransferase family, carrying the diagnostic **Asp/Orn carbamoyltransferase P-binding domain (IPR006132)** and **Asp/Orn-binding domain (IPR006131)**, along with IPR006130, IPR036901, and IPR002082. The enzyme catalyzes:

> **carbamoyl phosphate + L-aspartate → N-carbamoyl-L-aspartate + phosphate + H⁺**

The chemical mechanism has been established rigorously in the *E. coli* ortholog using ¹³C and ¹⁵N kinetic isotope effect studies. The reaction proceeds by an **ordered nucleophilic attack of the aspartate α-amino group on the carbonyl carbon of carbamoyl phosphate**, forming a **tetrahedral intermediate** that collapses, following an intramolecular proton transfer, into the products N-carbamoyl-L-aspartate and inorganic phosphate. As reported by Waldrop and colleagues: *"Nucleophilic attack on the carbonyl carbon of carbamyl phosphate by the alpha-amino group of L-aspartate results in the formation of a tetrahedral intermediate. An intramolecular proton transfer leads to formation of products N-carbamyl-L-aspartate and inorganic phosphate"* ([PMID: 1633169](https://pubmed.ncbi.nlm.nih.gov/1633169/)).

The pathway role of this reaction is definitive: ATCase catalyzes **the committed step of de novo pyrimidine biosynthesis**. As stated in a study of the plant enzyme: *"Aspartate transcarbamoylase (ATCase, EC 2.1.3.2) catalyzes the committed step in the de novo synthesis of uridine-5'-monophosphate (UMP), from which all other pyrimidine nucleotides are made"* ([PMID: 18053734](https://pubmed.ncbi.nlm.nih.gov/18053734/)). Because this step commits metabolic resources irreversibly toward pyrimidines, it is a natural and universal locus of metabolic regulation.

### Finding 2 — The *P. putida* ATCase is a dodecameric PyrB₆/PyrC′₆ complex with an internal regulatory site, not the *E. coli* c₆r₆ architecture

The most mechanistically distinctive feature of this enzyme comes from direct sequencing and biochemical characterization of the *P. putida pyrBC′* locus by Schurr and colleagues. The *pyrB* gene is **1,005 bp long and encodes the 334-amino-acid, 36.4-kDa catalytic subunit**. Immediately downstream, an overlapping and co-translated gene encodes a **424-residue, 44.2-kDa polypeptide homologous to dihydroorotase (DHOase)** but which is **catalytically inactive** — it lacks the conserved catalytic histidyl residues and does not complement *E. coli pyrC* auxotrophs.

Crucially, the native *P. putida* ATCase *"does not possess dissociable regulatory and catalytic functions but instead apparently contains the regulatory nucleotide binding site within a unique N-terminal extension of the pyrB-encoded subunit. The first gene, pyrB, is 1,005 bp long and encodes the 334-amino-acid, 36.4-kDa catalytic subunit of the enzyme"* ([PMID: 7896697](https://pubmed.ncbi.nlm.nih.gov/7896697/)). This means that, unlike *E. coli* ATCase (which separates into distinct catalytic and regulatory subunits), the *Pseudomonas* enzyme integrates its allosteric regulatory site into the catalytic polypeptide itself.

The inactive DHOase homolog (designated **PyrC′**) is not a functional dihydroorotase but a **structural partner**: *"The proposed function for the vestigial DHOase is to maintain ATCase activity by conserving the dodecameric assembly of the native enzyme"* ([PMID: 7896697](https://pubmed.ncbi.nlm.nih.gov/7896697/)). The holoenzyme is therefore a **dodecamer of six active PyrB and six inactive PyrC′ chains**, and PyrC′ is required to hold the assembly together and thereby maintain catalytic activity.

This *Pseudomonas*-type ("class A") architecture is consistent with the known structural diversity of the transcarbamoylase family. For example, the related catabolic ornithine transcarbamoylase of *Pseudomonas aeruginosa* is *"a dodecamer composed of four trimers organized in a tetrahedral manner"* with 23 point-group symmetry, in contrast to the pseudo-32 symmetry of *E. coli* ATCase ([PMID: 7479879](https://pubmed.ncbi.nlm.nih.gov/7479879/)).

### Finding 3 — ATCase uses an ordered kinetic mechanism (carbamoyl phosphate binds first) and is a cytoplasmic pyrimidine-pathway enzyme

The catalytic cycle proceeds through an **ordered-binding kinetic mechanism** in which **carbamoyl phosphate (CP) binds first**, forming an enzyme–CP complex before L-aspartate binds. As described for the transcarbamoylase family: *"Both of these transcarbamoylases use an ordered-binding mechanism in which CP binds first, allowing the formation of an enzyme"* complex ([PMID: 18971327](https://pubmed.ncbi.nlm.nih.gov/18971327/)). This ordered binding has a physiological benefit beyond kinetics: CP binding **stabilizes the otherwise thermally labile intermediate**, protecting it from decomposition.

The active site is formed at the interface between adjacent subunits of the catalytic trimer, and its key residues are conserved across the family. In the *E. coli* catalytic chain, **Arg54 interacts with both the anhydride oxygen and a phosphate oxygen of carbamoyl phosphate** ([PMID: 1303763](https://pubmed.ncbi.nlm.nih.gov/1303763/)), positioning the substrate for catalysis; **Arg105 and Leu267** help orient the aspartate and CP substrates ([PMID: 17603076](https://pubmed.ncbi.nlm.nih.gov/17603076/)); and **Lys84 from an adjacent chain** (part of the "80s loop") is critical for catalysis and cooperativity ([PMID: 10386880](https://pubmed.ncbi.nlm.nih.gov/10386880/)). The reaction occurs in the **cytoplasm**, consistent with the soluble, non-membrane character of the pyrimidine biosynthetic enzymes.

### Finding 4 — Sequence analysis of Q88D30 confirms intact ATCase catalytic signatures and the *Pseudomonas* N-terminal extension

Direct examination of the Q88D30 primary sequence independently corroborates the annotation. The protein is **exactly 334 residues long**, matching the catalytic subunit size reported experimentally: *"The first gene, pyrB, is 1,005 bp long and encodes the 334-amino-acid, 36.4-kDa catalytic subunit of the enzyme"* ([PMID: 7896697](https://pubmed.ncbi.nlm.nih.gov/7896697/)). The correspondence of the retrieved sequence length with the experimentally determined subunit confirms correct gene-product identity.

The sequence contains the **diagnostic carbamoyl-phosphate-binding loop motif "STRTR"** at positions 69–73 (in the context …FFEN**STRTR**TTF…), whose central arginine corresponds to the catalytic **Arg54** of *E. coli* ATCase that contacts carbamoyl phosphate ([PMID: 1303763](https://pubmed.ncbi.nlm.nih.gov/1303763/)). It also carries the conserved second-domain **"HPTQ" motif** at positions 151–154 (…NGGDGRHA**HPTQ**GML…), characteristic of the aspartate-binding domain. Notably, the catalytic P-loop motif appears **~15–17 residues later** than in the shorter *E. coli* PyrB (where the equivalent arginine is near residue 52–54), consistent with the **unique N-terminal extension** that in *Pseudomonas* houses the regulatory nucleotide-binding site.

### Finding 5 — Q88D30 is a bona fide ortholog of the *E. coli* ATCase catalytic subunit (~39% identity, catalytic motif exactly conserved)

A global Needleman–Wunsch alignment of *P. putida* PyrB (Q88D30, 334 aa) against the extensively characterized *E. coli* K-12 PyrB catalytic subunit (P0A786, 311 aa) yields **117/303 = 38.6% identity** over the aligned core. The carbamoyl-phosphate-binding catalytic loop aligns **exactly** (*P. putida* FEN-**STRTR**-TTF vs. *E. coli* FEA-**STRTR**-LSF), confirming positional conservation of the catalytic arginine (*E. coli* Arg54). The ~23-residue length difference is fully accounted for by the *Pseudomonas* N-terminal regulatory extension.

This orthology assignment is reinforced by the recognized sequence grouping of *Pseudomonas* ATCases. In a study of the *Thermus* strain ZO5 enzyme: *"The deduced amino acid sequence of Thermus strain ZO5 aspartate carbamoyltransferase (ATCase; encoded by pyrB) exhibits the highest similarities (about 50% identical amino acids) with ATCases from Pseudomonas sp."* ([PMID: 9171389](https://pubmed.ncbi.nlm.nih.gov/9171389/)). This confirms that *Pseudomonas* ATCases form a recognizable, distinct sequence group within the family.

The same study documents **pyrimidine end-product transcriptional control**: *"In Thermus strain ZO5, pyrB and pyrC gene expression is repressed three- to fourfold by uracil and increased twofold by arginine"* ([PMID: 9171389](https://pubmed.ncbi.nlm.nih.gov/9171389/)). This indicates that, in addition to allosteric control at the protein level, *pyr* genes including *pyrB* are subject to gene-expression-level regulation by pyrimidine availability — a layer of control expected to operate on the *P. putida pyr* regulon as well.

### Finding 6 — KT2440 genome confirms the *pyrB*(PP_4998)–*pyrC′*(PP_4999) locus and lacks *pyrI*; UniProt's *E. coli*-style subunit annotation is an inaccurate rule propagation

In the *P. putida* KT2440 reference genome, *pyrB* (PP_4998, Q88D30, 334 aa, 36.3 kDa) is immediately adjacent to **PP_4999 (Q88D29, 423 aa, 44.1 kDa)**, a dihydroorotase-like protein. This matches the 424-aa/44.2-kDa inactive DHOase homolog (PyrC′) described biochemically by Schurr et al. ([PMID: 7896697](https://pubmed.ncbi.nlm.nih.gov/7896697/)). A **separate, genuine dihydroorotase, *pyrC* (PP_1086, Q88NW7, 348 aa, EC 3.5.2.3)**, is located elsewhere in the genome and provides the actual dihydroorotase step (step 3) of the pyrimidine pathway. This genomic arrangement — an inactive DHOase homolog fused into the ATCase operon plus a genuine DHOase elsewhere — is exactly what the *Pseudomonas*-type ATCase model predicts.

A UniProt query for a *pyrI* (ATCase regulatory subunit) gene in *P. putida* KT2440 (taxid 160488) returns **no hits** — the genome encodes no PyrI. This directly supports the biochemical conclusion that *"The P. putida ATCase does not possess dissociable regulatory and catalytic functions but instead apparently contains the regulatory nucleotide binding site within a unique N-terminal extension of the pyrB-encoded subunit"* ([PMID: 7896697](https://pubmed.ncbi.nlm.nih.gov/7896697/)).

Nonetheless, UniProt's **SUBUNIT** field for Q88D30 (a rule-based annotation, ECO:0000255, HAMAP-Rule MF_00001) states: *"Heterododecamer (2C3:3R2) of six catalytic PyrB chains … and six regulatory PyrI chains"* — the *E. coli* class-C architecture. **This is an inaccurate propagation of a general rule to an organism whose enzyme has a genuinely different quaternary structure.** By contrast, UniProt's curated **FUNCTION**, **CATALYTIC ACTIVITY** (carbamoyl phosphate + L-aspartate = N-carbamoyl-L-aspartate + phosphate + H⁺), and **PATHWAY** (UMP biosynthesis de novo, step 2 of 3) annotations are accurate.

---

## Mechanistic Model and Interpretation

### The catalyzed reaction and its pathway context

ATCase performs the **second enzymatic step and the first committed step** of de novo pyrimidine biosynthesis. The pathway from central metabolism to UMP proceeds as follows:

```
   Glutamine + 2 ATP + HCO3-
            │  (CPSase, PyrA)
            ▼
   Carbamoyl phosphate  ──────┐
                               │  + L-aspartate
                               ▼
        ╔══════════════════════════════╗
        ║  ATCase  (pyrB / PP_4998)     ║  ← COMMITTED STEP
        ║  EC 2.1.3.2                   ║
        ╚══════════════════════════════╝
                               │
                               ▼
              N-carbamoyl-L-aspartate + Pi
                               │  (DHOase, genuine pyrC / PP_1086)
                               ▼
                    Dihydroorotate
                               │  (DHODH, pyrD)
                               ▼
                        Orotate
                               │  (OPRTase, pyrE)
                               ▼
                        Orotidine-5'-P
                               │  (OMP decarboxylase, pyrF)
                               ▼
                          U M P  ──►  all other pyrimidine nucleotides
```

The enzyme carries out its reaction in the **cytoplasm**. Its high specificity is for **L-aspartate** as the amino-group acceptor (the related family member ornithine transcarbamoylase uses L-ornithine instead; the two enzymes share the CP-binding domain but diverge in the second, substrate-binding domain). ATCase can weakly carbamoylate L-asparagine at ~10-fold lower maximal velocity, underscoring the strict optimization of the active site for L-aspartate ([PMID: 18004787](https://pubmed.ncbi.nlm.nih.gov/18004787/)).

### The catalytic mechanism

The reaction follows an **ordered bi-bi kinetic mechanism**:

| Step | Event |
|------|-------|
| 1 | Carbamoyl phosphate (CP) binds first to the CP-binding domain; Arg54 (E. coli numbering) contacts the anhydride and phosphate oxygens |
| 2 | CP binding organizes the active site and protects the labile intermediate from thermal decomposition |
| 3 | L-aspartate binds to the adjacent aspartate-binding domain; domain closure creates the high-activity active site |
| 4 | The α-amino group of aspartate performs nucleophilic attack on the CP carbonyl carbon → tetrahedral intermediate |
| 5 | Intramolecular proton transfer; collapse of intermediate → N-carbamoyl-L-aspartate + Pi |
| 6 | Products released |

The active site is **shared between two adjacent catalytic chains** — residues from one chain (e.g., Arg54, Arg105, Leu267) and from the neighboring chain (e.g., Lys84) both contribute — which is why the trimeric organization of catalytic subunits is essential for activity.

### The distinctive *Pseudomonas*-type quaternary structure

The single most important organism-specific insight is the enzyme's **architecture**:

| Feature | *E. coli* ATCase (class C) | *P. putida* ATCase (class A / *Pseudomonas*-type) |
|---|---|---|
| Catalytic subunit | PyrB (~34 kDa), 6 copies | PyrB (36.4 kDa, 334 aa), 6 copies |
| Regulatory subunit | PyrI (~17 kDa), 6 copies | **None** — no *pyrI* gene in genome |
| Second subunit type | — | Inactive DHOase homolog **PyrC′** (44.2 kDa), 6 copies |
| Holoenzyme | Heterododecamer 2C₃:3R₂ | **Dodecamer PyrB₆/PyrC′₆** |
| Regulatory nucleotide site | On separate PyrI chains | In **N-terminal extension of PyrB itself** |
| Role of second subunit | Allosteric regulation | **Structural — maintains dodecameric assembly** |

In *P. putida*, the regulatory function has been internalized into an N-terminal extension of PyrB (explaining the ~23-residue length increase over *E. coli* PyrB and the C-terminal shift of the catalytic motifs in the sequence). The PyrC′ protein — a "vestigial" dihydroorotase that has lost its catalytic residues — has been co-opted as an obligatory structural scaffold. This is an elegant example of **enzyme recruitment / moonlighting**, in which an ancestral catalytic protein is retained for a purely architectural purpose. The genome-level confirmation that a *separate*, genuine *pyrC* dihydroorotase (PP_1086) exists elsewhere resolves any ambiguity: the pathway's DHOase chemistry is provided by PP_1086, while PP_4999 (PyrC′) exists only to build the ATCase holoenzyme.

### Regulation

The enzyme is controlled at two levels:
1. **Allosteric (post-translational):** via the nucleotide-binding regulatory site in the PyrB N-terminal extension, tuning activity in response to the nucleotide pool.
2. **Transcriptional (gene expression):** pyrimidine end-product (uracil/UMP-derived) repression of the *pyr* regulon, as demonstrated for the closely grouped *Thermus* and *Pseudomonas* systems ([PMID: 9171389](https://pubmed.ncbi.nlm.nih.gov/9171389/)).

---

## Evidence Base

| PMID | Title (abbreviated) | Role in this report |
|------|---------------------|---------------------|
| [7896697](https://pubmed.ncbi.nlm.nih.gov/7896697/) | *Aspartate transcarbamoylase genes of Pseudomonas putida: requirement for an inactive dihydroorotase for assembly into the dodecameric holoenzyme* | **Primary, organism-specific evidence.** Defines the 334-aa/36.4-kDa PyrB catalytic subunit, the inactive PyrC′ DHOase homolog, the dodecameric PyrB₆/PyrC′₆ assembly, the internal N-terminal regulatory site, and the absence of dissociable regulatory subunits. |
| [1633169](https://pubmed.ncbi.nlm.nih.gov/1633169/) | *13C and 15N isotope effects as a probe of the chemical mechanism of E. coli aspartate transcarbamylase* | Defines the chemical mechanism: nucleophilic attack, tetrahedral intermediate, product formation. |
| [18053734](https://pubmed.ncbi.nlm.nih.gov/18053734/) | *Expression and functional analysis of ATCase … in Arabidopsis* | Establishes ATCase as the committed step of de novo UMP biosynthesis. |
| [18971327](https://pubmed.ncbi.nlm.nih.gov/18971327/) | *Mechanism of thermal decomposition of carbamoyl phosphate and its stabilization by aspartate and ornithine transcarbamoylases* | Establishes the ordered mechanism (CP binds first) and intermediate stabilization. |
| [1303763](https://pubmed.ncbi.nlm.nih.gov/1303763/) | *Arginine 54 in the active site of E. coli aspartate transcarbamoylase is critical for catalysis* | Identifies the conserved catalytic CP-binding arginine (Arg54), used to anchor the sequence-motif conservation in Q88D30. |
| [17603076](https://pubmed.ncbi.nlm.nih.gov/17603076/) | *Structural model of the R state of E. coli ATCase with substrates bound* | Documents active-site residues (Arg105, Leu267) and pre-catalytic geometry. |
| [10386880](https://pubmed.ncbi.nlm.nih.gov/10386880/) | *The 80s loop … is critical for catalysis and homotropic cooperativity* | Documents the cross-subunit Lys84 contribution to the shared active site. |
| [9171389](https://pubmed.ncbi.nlm.nih.gov/9171389/) | *Structure and expression of a pyrimidine gene cluster from Thermus strain ZO5* | Confirms *Pseudomonas* ATCase sequence grouping (~50% identity) and pyrimidine transcriptional repression of *pyrB*. |
| [7479879](https://pubmed.ncbi.nlm.nih.gov/7479879/) | *Crystal structure of P. aeruginosa catabolic OTCase … different oligomeric organization* | Illustrates the structural diversity of *Pseudomonas* transcarbamoylases (dodecameric assemblies). |
| [18004787](https://pubmed.ncbi.nlm.nih.gov/18004787/) | *Use of L-asparagine … to investigate catalysis and cooperativity in E. coli ATCase* | Demonstrates strict substrate specificity for L-aspartate (asparagine carbamoylated ~10× slower). |

The strongest and most directly relevant paper is **Schurr et al. 1995 ([PMID: 7896697](https://pubmed.ncbi.nlm.nih.gov/7896697/))**, which characterized the *P. putida* enzyme itself and provides organism-specific experimental grounding for essentially all of the structural conclusions. The mechanistic and active-site details are transferred from the exhaustively studied *E. coli* ortholog, which is justified by the ~39% sequence identity and exact conservation of the catalytic motifs.

---

## Limitations and Knowledge Gaps

1. **No direct structural or kinetic study of Q88D30 itself.** The mechanistic and quaternary-structure conclusions rest on (a) the *P. putida* enzyme characterized by Schurr et al. and (b) the *E. coli* ortholog. No crystal structure, cryo-EM structure, or steady-state kinetic characterization of the specific KT2440 gene product (PP_4998) has been identified. Confirmation that KT2440's enzyme behaves identically to the strain studied by Schurr et al. is by inference from genome conservation, not direct measurement.

2. **Regulatory ligand specificity is not resolved for KT2440.** While the regulatory site is placed in the PyrB N-terminal extension, the identity of the physiological allosteric effector(s) (e.g., ATP, CTP, UTP) and their quantitative effects on the KT2440 enzyme have not been experimentally determined here.

3. **The exact residues of the N-terminal regulatory site are not mapped.** Sequence analysis localizes the extension but does not define which residues bind nucleotides.

4. **Transcriptional regulation of the *P. putida pyr* regulon is inferred by analogy.** Pyrimidine end-product repression of *pyrB* is documented in *Thermus* (and is a general feature of *pyr* regulons); direct promoter/operator mapping for PP_4998 in KT2440 was not performed.

5. **The UniProt SUBUNIT annotation conflict** (rule-based "PyrI heterododecamer") is a documented database inaccuracy for this organism rather than a genuine biological uncertainty, but downstream users relying solely on automated annotation may be misled.

---

## Proposed Follow-up Experiments and Actions

1. **Recombinant expression and enzymology of PP_4998.** Clone and overexpress KT2440 *pyrB* (with and without co-expressed PP_4999/PyrC′), purify, and determine steady-state kinetic parameters (kcat, Km for CP and L-aspartate) and substrate specificity. Confirm that co-expression of PyrC′ is required for a stable, active dodecamer.

2. **Structural determination.** Solve the cryo-EM or crystal structure of the KT2440 PyrB₆/PyrC′₆ holoenzyme to directly visualize the dodecameric assembly, the PyrB–PyrC′ interfaces, and the N-terminal regulatory extension.

3. **Map the allosteric site.** Perform nucleotide-binding assays (ITC/fluorescence) with ATP, CTP, and UTP against the holoenzyme, and use mutagenesis of the PyrB N-terminal extension to identify effector-binding residues.

4. **Genetic validation in KT2440.** Construct *pyrB* (PP_4998) and *pyrC′* (PP_4999) deletion mutants and test for pyrimidine auxotrophy and loss of ATCase activity, confirming the essential structural role of PyrC′ in vivo.

5. **Transcriptional analysis.** Measure *pyrBC′* transcript levels under pyrimidine-rich versus pyrimidine-limited conditions (qRT-PCR/RNA-seq) to confirm end-product repression of the *P. putida pyr* operon.

6. **Correct the annotation.** Submit a curation note to UniProt flagging that the rule-based SUBUNIT field (PyrI-containing heterododecamer) is inaccurate for *P. putida*, which uses the *Pseudomonas*-type PyrB₆/PyrC′₆ architecture with no PyrI.

---

## Conclusion

**pyrB (PP_4998, Q88D30) is unambiguously the catalytic subunit of aspartate carbamoyltransferase (EC 2.1.3.2)** in *Pseudomonas putida* KT2440. It catalyzes the first committed, cytoplasmic step of de novo pyrimidine biosynthesis — carbamoylation of L-aspartate by carbamoyl phosphate to form N-carbamoyl-L-aspartate — via an ordered mechanism with high specificity for L-aspartate. The physiological enzyme is a *Pseudomonas*-type dodecamer of six catalytic PyrB subunits and six catalytically inactive dihydroorotase-homolog PyrC′ subunits, with the allosteric regulatory site integrated into an N-terminal extension of PyrB; there is no separate PyrI regulatory subunit, making the widely propagated *E. coli*-style subunit annotation incorrect for this organism.


## Artifacts

- [OpenScientist final report](pyrB-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](pyrB-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:1633169
2. PMID:18053734
3. PMID:7896697
4. PMID:7479879
5. PMID:18971327
6. PMID:1303763
7. PMID:17603076
8. PMID:10386880
9. PMID:9171389
10. PMID:18004787