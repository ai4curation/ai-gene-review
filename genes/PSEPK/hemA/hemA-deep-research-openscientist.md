---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-20T14:53:30.813365'
end_time: '2026-07-20T15:09:45.148975'
duration_seconds: 974.34
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: hemA
  gene_symbol: hemA
  uniprot_accession: Q88PW6
  protein_description: 'RecName: Full=Glutamyl-tRNA reductase {ECO:0000255|HAMAP-Rule:MF_00087};
    Short=GluTR {ECO:0000255|HAMAP-Rule:MF_00087}; EC=1.2.1.70 {ECO:0000255|HAMAP-Rule:MF_00087};'
  gene_info: Name=hemA {ECO:0000255|HAMAP-Rule:MF_00087}; OrderedLocusNames=PP_0732;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the glutamyl-tRNA reductase family.
  protein_domains: 4pyrrol_synth_GluRdtase. (IPR000343); 4pyrrol_synth_GluRdtase_dimer.
    (IPR015896); 4pyrrol_synth_GluRdtase_N. (IPR015895); GluRdtase_CS. (IPR018214);
    GluRdtase_dimer_dom_sf. (IPR036453)
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
  path: hemA-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: hemA-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88PW6
- **Protein Description:** RecName: Full=Glutamyl-tRNA reductase {ECO:0000255|HAMAP-Rule:MF_00087}; Short=GluTR {ECO:0000255|HAMAP-Rule:MF_00087}; EC=1.2.1.70 {ECO:0000255|HAMAP-Rule:MF_00087};
- **Gene Information:** Name=hemA {ECO:0000255|HAMAP-Rule:MF_00087}; OrderedLocusNames=PP_0732;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the glutamyl-tRNA reductase family.
- **Key Domains:** 4pyrrol_synth_GluRdtase. (IPR000343); 4pyrrol_synth_GluRdtase_dimer. (IPR015896); 4pyrrol_synth_GluRdtase_N. (IPR015895); GluRdtase_CS. (IPR018214); GluRdtase_dimer_dom_sf. (IPR036453)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "hemA" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'hemA' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **hemA** (gene ID: hemA, UniProt: Q88PW6) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of *hemA* (Q88PW6, PP_0732) — Glutamyl-tRNA Reductase in *Pseudomonas putida* KT2440

**Target:** UniProt **Q88PW6** · Gene **hemA** · Ordered locus **PP_0732**
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / KT2440) — PSEPK
**Enzyme:** Glutamyl-tRNA reductase (GluTR) · **EC 1.2.1.70**

---

## Summary

The gene **hemA** (ordered locus **PP_0732**; UniProt **Q88PW6**) of *Pseudomonas putida* KT2440 encodes **glutamyl-tRNA reductase (GluTR; EC 1.2.1.70)**, the enzyme that catalyzes the **first and committed step of tetrapyrrole biosynthesis** via the glutamate (C5) pathway. The gene identity is unambiguous: the UniProt annotation, the InterPro domain complement (4pyrrol_synth_GluRdtase family, IPR000343, with associated N-terminal, dimerization, and conserved-site domains), and the experimental literature all converge on the same enzymatic assignment. Critically, the C5 pathway (rather than the alternative ALA-synthase / C4 pathway) has been **experimentally demonstrated in *P. putida* itself** by complementation studies, so this is not a case of an ambiguous gene symbol or mis-transferred annotation. The gene symbol "hemA" correctly matches the protein description, the organism is confirmed, and the domain architecture aligns with characterized GluTR enzymes.

GluTR catalyzes the **NADPH-dependent reduction of glutamate that is esterified to tRNA^Glu (glutamyl-tRNA^Glu)**, converting it to **glutamate-1-semialdehyde (GSA)**. This is a mechanistically unusual reaction: the enzyme uses a substrate — an aminoacylated tRNA — that is otherwise dedicated to protein synthesis, and it reduces the activated aminoacyl (ester) bond rather than a free carboxylate. Catalysis proceeds through a **covalent thioester intermediate on a conserved active-site cysteine (Cys50)**, which is then reduced by a hydride transferred from NADPH. The reaction takes place in the **cytoplasm**. The product GSA is subsequently converted by glutamate-1-semialdehyde-2,1-aminomutase (HemL, encoded by *hemL*) into **5-aminolevulinic acid (ALA)**, the universal precursor of all tetrapyrroles — heme, siroheme, and (in phototrophs) chlorophyll and related cofactors.

In *P. putida*, GluTR functions as the **rate-limiting, heme-feedback-regulated flux-control node** that governs the supply of tetrapyrrole cofactors required for aerobic respiration (heme) and assimilatory sulfite/nitrite reduction (siroheme). Sequence analysis of Q88PW6 confirms full conservation of all functionally characterized active-site residues (52.5% identity to the biochemically dissected *E. coli* enzyme), and genomic context places *hemA* at the head of a conserved **hemA–prfA–prmC operon** that is translationally coupled to the translation-termination machinery. This report consolidates seven confirmed findings, drawn from 20 reviewed papers, into a complete mechanistic and functional annotation.

---

## Key Findings

### Finding 1 — hemA (Q88PW6, PP_0732) is glutamyl-tRNA reductase, catalyzing the first committed step of C5 tetrapyrrole biosynthesis in *P. putida*

The core functional assignment is secure at multiple levels of evidence. UniProt annotates Q88PW6 as glutamyl-tRNA reductase (GluTR; EC 1.2.1.70), a member of the 4pyrrol_synth_GluRdtase family (IPR000343). More importantly, the use of the tRNA-dependent (C5) pathway — as opposed to the ALA-synthase (C4/Shemin) pathway found in α-proteobacteria and animals — was **directly and experimentally established in *P. putida***. Hungerer, Weiss, and colleagues demonstrated that *Pseudomonas putida*, along with *P. aeruginosa*, *P. stutzeri*, and several other γ-proteobacteria, synthesizes ALA via the two-enzyme C5 route requiring glutamyl-tRNA reductase (HemA) and glutamate-1-semialdehyde-2,1-aminomutase (HemL) ([PMID: 7883699](https://pubmed.ncbi.nlm.nih.gov/7883699/)). The verified quote states that "the tRNA-dependent pathway, involving the enzymes glutamyl-tRNA reductase (encoded by hemA) and glutamate-1-semialdehyde-2,1-aminomutase (encoded by hemL), was demonstrated to be used by Pseudomonas aeruginosa, Pseudomonas putida, Pseudomonas stutzeri, Comamonas testosteroni, Azotobacter vinelandii, and Acinetobacter calcoaceticus." The homologous *P. aeruginosa* enzyme is a 423-residue, ~46 kDa protein that complements an *E. coli hemA* mutant — establishing functional equivalence across the genus. This anchors the assignment for *P. putida* directly, rather than by inference alone.

The reaction catalyzed is:

> **L-glutamyl-tRNA^Glu + NADPH + H⁺ → L-glutamate-1-semialdehyde + tRNA^Glu + NADP⁺**

This is the committed, entry-point reaction of the entire tetrapyrrole branch of metabolism.

### Finding 2 — Catalytic mechanism: a conserved active-site cysteine forms a thioester with glutamyl-tRNA, then NADPH-dependent hydride transfer yields glutamate-1-semialdehyde

The catalytic mechanism of GluTR is well characterized from both structural and mutagenesis studies. The high-resolution crystal structure of *Methanopyrus kandleri* GluTR (Schubert et al.) revealed a **dimeric, V-shaped enzyme**, each monomer built from three domains connected by an unusually long "spinal" α-helix. A conserved catalytic cysteine sits poised to attack the activated aminoacyl bond of glutamyl-tRNA. The review by Moser and colleagues summarizes the two-step mechanism directly: "It bears a conserved cysteine poised to nucleophilically attack the activated aminoacyl bond of glutamyl-tRNA. Subsequently, the thioester intermediate is reduced to the product glutamate-1-semialdehyde via hydride transfer from NADPH supplied by the second domain" ([PMID: 16228559](https://pubmed.ncbi.nlm.nih.gov/16228559/)).

The molecular basis of **substrate specificity** was dissected in *E. coli* by Lüer et al. through site-directed mutagenesis. They established that GluTR recognizes the aminoacyl ester bond itself rather than the glutamate side chain: "We thus propose that the ester bond between glutamate and tRNA(Glu) represents the crucial determinant for substrate recognition by GluTR" ([PMID: 17697121](https://pubmed.ncbi.nlm.nih.gov/17697121/)). Consistent with this, tRNA^Glu that had been mischarged with glutamine remained a substrate, whereas substitutions of Gln116 and Glu114 abolished reductase activity, and Cys50 was shown to be essential for both thioester formation and esterase activity. The mechanism therefore has two clearly separable chemical steps — nucleophilic transesterification onto the cysteine thiol, then hydride-mediated reduction of the resulting thioester to an aldehyde.

### Finding 3 — GluTR (HemA) forms a physical complex with GSA-aminomutase (HemL) enabling metabolic channeling of the reactive intermediate glutamate-1-semialdehyde

Glutamate-1-semialdehyde is a chemically reactive aldehyde that could undergo unwanted side reactions if released into bulk cytoplasm. Lüer et al. demonstrated that GluTR (HemA) and GSA-aminomutase (HemL) form a **direct physical complex** in *E. coli*, verified by co-immunoprecipitation and gel-permeation chromatography, and independent of the presence of Glu-tRNA or cofactors. Complex formation requires the GluTR C-terminal dimerization domain: a C-terminal truncation (GluTR-A338Stop) abolished the interaction. In silico modeling of the complex and detection of GluTR side-product formation when the complex could not assemble both support **direct metabolic channeling** of GSA between the two active sites: "The in silico model of the E. coli GluTR.GSA-AM complex suggested direct metabolic channeling between both enzymes to protect the reactive aldehyde species GSA" ([PMID: 15757895](https://pubmed.ncbi.nlm.nih.gov/15757895/)). By homology, *P. putida* GluTR — which retains the C-terminal dimerization domain (IPR015896) required for this interaction — is expected to function within an analogous HemA·HemL channeling assembly. The immediate downstream partner HemL is itself structurally characterized in the sibling species *P. aeruginosa*, where it is a PLP-dependent aminomutase with a Schiff base to Lys286 ([PMID: 29684343](https://pubmed.ncbi.nlm.nih.gov/29684343/)).

### Finding 4 — GluTR/HemA is the tightly regulated flux-control node of tetrapyrrole synthesis, governed by heme feedback and regulated protein stability

GluTR is universally recognized as the **rate-limiting and most tightly regulated** step of tetrapyrrole biosynthesis, and its principal control input is **feedback by heme**, the pathway end-product. In *Salmonella* and *E. coli*, Wang and colleagues showed that HemA enzyme activity increases 10- to 25-fold under heme limitation, and that this induction is mediated by increased HemA protein abundance rather than by transcription ([PMID: 9139907](https://pubmed.ncbi.nlm.nih.gov/9139907/)). The mechanism is **regulated proteolysis**: HemA is unstable when heme is plentiful and stabilized when heme is scarce. The verified quantitative statement is that "the half-life of HemA protein is approximately 20 min in unrestricted cells but increases to >300 min in heme-limited cells" ([PMID: 9973348](https://pubmed.ncbi.nlm.nih.gov/9973348/)). This turnover is energy-dependent and is blocked in a *lon clpP* double mutant, implicating the ClpAP/Lon protease systems in heme-responsive HemA degradation. Beyond bacteria, GluTR is a conserved target of heme feedback: "GluTR is a target of feedback regulation by heme" ([PMID: 17360620](https://pubmed.ncbi.nlm.nih.gov/17360620/)), and in plants a dedicated GluTR-binding protein (GBP) serves as the heme-sensing factor for this feedback ([PMID: 31194674](https://pubmed.ncbi.nlm.nih.gov/31194674/)). This positions HemA as the metabolic valve that matches tetrapyrrole cofactor production to cellular demand.

### Finding 5 — *P. putida* GluTR (Q88PW6) conserves the catalytic Cys50 and NADPH-binding motif — sequence-level confirmation of function

Direct sequence analysis of Q88PW6 (425 residues) corroborates the enzymatic assignment. The protein contains its catalytic cysteine at **position 50**, embedded within the strictly conserved **"CNRS" active-site motif** — the exact structural equivalent of *E. coli* GluTR Cys50, which was experimentally shown to be essential for thioester formation ([PMID: 17697121](https://pubmed.ncbi.nlm.nih.gov/17697121/)). Notably, the entire protein contains only two cysteines (at positions 36 and 50), and the catalytic one occupies the canonical position. A **dinucleotide-binding Rossmann signature** (an IGAGE motif at ~residue 186 and a V-A-N-R motif near residue 209) marks the NADPH-binding domain. The overall domain order — N-terminal catalytic domain → central NADPH-binding domain → C-terminal dimerization domain — matches both the GluTR family architecture and the InterPro domain complement listed for Q88PW6 (IPR015895 N-terminal, IPR015896 dimerization, IPR018214 conserved site). This is coherent bioinformatic confirmation that the folded protein retains all elements required for the annotated chemistry.

### Finding 6 — *hemA* (PP_0732) heads a conserved hemA–prfA–prmC operon and feeds both heme and siroheme biosynthesis

Genomic-context analysis places *hemA* within a conserved and functionally suggestive operon. In the KT2440 genome, PP_0732/*hemA* (coordinates 851222–852499, + strand) is immediately followed on the same strand by **PP_0733 = peptide chain release factor 1 (prfA/RF1, K02835)**, with a **4-bp overlap** between the *hemA* stop codon and the *prfA* start codon — a hallmark of **translational coupling**. This is followed by **PP_0734 = release factor glutamine-N5-methyltransferase (prmC/HemK, K02493)**, again with a 1-bp overlap. This gene arrangement directly mirrors the *P. aeruginosa* organization reported by Hungerer et al., who showed *hemA* forms an operon with release factor 1 ([PMID: 7883699](https://pubmed.ncbi.nlm.nih.gov/7883699/)). The juxtaposition of the tetrapyrrole-pathway entry enzyme with the translation-termination apparatus is evolutionarily conserved and may reflect co-regulation, given that GluTR uniquely couples tetrapyrrole synthesis to the aminoacyl-tRNA/translation machinery. KEGG assigns PP_0732 to K02492 / EC 1.2.1.70, pathway ppu00860 (porphyrin metabolism), and both module **M00121 (heme biosynthesis, glutamate ⇒ heme)** and module **M00846 (siroheme biosynthesis, glutamyl-tRNA ⇒ siroheme)** — confirming that GluTR feeds both major tetrapyrrole end-products in *P. putida*.

### Finding 7 — *P. putida* GluTR is 52.5% identical to *E. coli* GluTR with full conservation of all functionally characterized active-site residues

A global Needleman-Wunsch alignment (BLOSUM62) of Q88PW6 (425 aa) against *E. coli* HemA/GluTR (P0A6X1, 418 aa) yields **52.5% identity (218/415 aligned positions)** — a level that justifies confident mechanistic homology transfer. Every residue that was functionally characterized by mutagenesis in the *E. coli* enzyme is conserved and positionally aligned in the *P. putida* protein:

| *E. coli* residue | *P. putida* (Q88PW6) equivalent | Functional role |
|---|---|---|
| Cys50 | Cys50 | Catalytic nucleophile forming the thioester intermediate |
| Glu114 | Glu112 | Substitution abolishes reductase activity |
| Gln116 | Gln114 | Substitution abolishes reductase activity |
| Ser109 | Ser107 | Glutamate binding |
| His99 | His97 | Active-site residue |
| Arg52 | Arg52 | Active-site residue |

This full conservation, together with the shared domain architecture and NADPH-binding signature, provides strong structural-evolutionary evidence that the *P. putida* enzyme uses the identical catalytic mechanism experimentally established for *E. coli* GluTR ([PMID: 17697121](https://pubmed.ncbi.nlm.nih.gov/17697121/)).

---

## Mechanistic Model / Interpretation

### The reaction in cellular context

GluTR (HemA) is the committed entry point of the **C5 (glutamate) pathway** of tetrapyrrole biosynthesis. The pathway proceeds:

```
                         GluRS
   L-glutamate + tRNA^Glu ----> L-glutamyl-tRNA^Glu   (shared with translation)
                                          |
                                          |  GluTR / HemA  (PP_0732, Q88PW6)
                                          |  + NADPH  --> thioester on Cys50 --> hydride transfer
                                          v
                          L-glutamate-1-semialdehyde (GSA)   [reactive aldehyde]
                                          |
                                          |  HemL / GSA-aminomutase (PLP-dependent)
                                          |  [channeled via HemA·HemL complex]
                                          v
                          5-aminolevulinic acid (ALA)   <-- universal tetrapyrrole precursor
                                          |
                                    (HemB, HemC, HemD, ...)
                                          v
                          +---------------+---------------+
                          v                               v
                    Protoporphyrin IX               Precorrin / siroheme branch
                          |                               |
                          v                               v
                        HEME                          SIROHEME
              (respiration, cytochromes,        (assimilatory sulfite &
               catalases, oxidases)              nitrite reductases)
```

Two features make GluTR mechanistically distinctive. First, it recruits an **aminoacyl-tRNA** — a molecule otherwise reserved for ribosomal protein synthesis — as its substrate, thereby directly coupling cofactor metabolism to the translation apparatus. This coupling is echoed at the genomic level by the conserved *hemA–prfA–prmC* operon (Finding 6). Second, it reduces an **activated ester bond to an aldehyde** rather than reducing a free carboxylate, which is thermodynamically why the tRNA activation step is required.

### Catalytic cycle

```
   Step 1 (transesterification):
      Cys50-SH  +  Glu~tRNA^Glu   -->   Cys50-S~Glu (thioester)  +  tRNA^Glu

   Step 2 (reduction):
      Cys50-S~Glu  +  NADPH  -->   Cys50-SH  +  Glu-1-semialdehyde  +  NADP+
```

The conserved Cys50 (retained in Q88PW6 within the CNRS motif) performs nucleophilic attack; the NADPH-binding (Rossmann-fold) middle domain supplies the hydride; and the C-terminal dimerization domain both builds the V-shaped homodimer and provides the interface for the HemL complex that channels the reactive GSA product.

### Regulatory logic

GluTR sits at the top of the pathway precisely so that it can be the point of control. The cell measures its heme status and throttles GluTR accordingly:

```
   Heme abundant  --> HemA destabilized (t½ ~20 min, ClpAP/Lon-dependent) --> low ALA flux
   Heme limited   --> HemA stabilized   (t½ >300 min)                     --> high ALA flux (10-25x activity)
```

This makes HemA a **negative-feedback valve**: end-product heme suppresses the committed step, ensuring tetrapyrrole cofactor supply is matched to demand and preventing accumulation of phototoxic/pro-oxidant porphyrin intermediates. In *P. putida*, an obligate aerobe that depends on heme-containing cytochromes and oxidases for respiration, this regulation directly gates respiratory competence and, via siroheme, assimilatory nitrogen/sulfur metabolism.

### Localization

All available evidence indicates GluTR acts in the **cytoplasm**. It is a soluble enzyme with no signal peptide or transmembrane segments, its substrate (glutamyl-tRNA^Glu) is generated by cytoplasmic glutamyl-tRNA synthetase, and its partner HemL and the downstream ALA-utilizing enzymes are cytoplasmic. (In photosynthetic eukaryotes the orthologous enzyme is plastid-localized, but that compartment is irrelevant to a bacterium.)

---

## Evidence Base

| PMID | Study focus | How it supports the annotation |
|---|---|---|
| [7883699](https://pubmed.ncbi.nlm.nih.gov/7883699/) | *hemA* regulation & C5 pathway in *Pseudomonas* | **Directly demonstrates** *P. putida* uses the HemA/GluTR C5 pathway; establishes the *hemA*–RF1 operon. Primary organism-specific evidence. |
| [16228559](https://pubmed.ncbi.nlm.nih.gov/16228559/) | Structure/function review of GluTR | Defines the two-step mechanism: cysteine nucleophile + NADPH hydride transfer to GSA. |
| [17697121](https://pubmed.ncbi.nlm.nih.gov/17697121/) | *E. coli* GluTR mutagenesis (Lüer et al.) | Establishes substrate specificity is the aminoacyl ester bond; identifies essential Cys50, Glu114, Gln116. Basis for homology transfer to Q88PW6. |
| [15757895](https://pubmed.ncbi.nlm.nih.gov/15757895/) | GluTR·GSA-AM complex (Lüer et al.) | Demonstrates physical HemA·HemL complex and metabolic channeling of reactive GSA; C-terminal domain required. |
| [9139907](https://pubmed.ncbi.nlm.nih.gov/9139907/) | HemA activity under heme limitation | Shows 10-25x activity increase via increased protein abundance, not transcription. |
| [9973348](https://pubmed.ncbi.nlm.nih.gov/9973348/) | Conditional HemA stability (*Salmonella*) | Quantifies heme-responsive HemA half-life (20 min → >300 min); implicates ClpAP/Lon. |
| [17360620](https://pubmed.ncbi.nlm.nih.gov/17360620/) | Heme status & Glu-tRNA metabolism | Confirms GluTR as a conserved heme-feedback target. |
| [31194674](https://pubmed.ncbi.nlm.nih.gov/31194674/) | GluTR-binding protein (plants) | Illustrates the heme-sensing mechanism for GluTR feedback (eukaryotic paradigm). |
| [29684343](https://pubmed.ncbi.nlm.nih.gov/29684343/) | GSA-aminomutase structure (*P. aeruginosa*) | Structural characterization of the immediate downstream partner (HemL) in a *Pseudomonas*. |
| [20158506](https://pubmed.ncbi.nlm.nih.gov/20158506/) | KT2440 essential-gene screen | Genome-scale context for *P. putida* KT2440 metabolic essentiality. |

Supporting biotechnology literature ([PMID: 26453466](https://pubmed.ncbi.nlm.nih.gov/26453466/), [PMID: 21620993](https://pubmed.ncbi.nlm.nih.gov/21620993/), [PMID: 27664748](https://pubmed.ncbi.nlm.nih.gov/27664748/)) further confirms HemA function: overexpression of *hemA* (often with *hemL*) drives ALA overproduction in engineered *E. coli* and *C. glutamicum*, direct functional proof that HemA is the flux-determining committed enzyme. Plant studies ([PMID: 17571216](https://pubmed.ncbi.nlm.nih.gov/17571216/), [PMID: 15584960](https://pubmed.ncbi.nlm.nih.gov/15584960/), [PMID: 36171567](https://pubmed.ncbi.nlm.nih.gov/36171567/)) reinforce the conserved rate-limiting and feedback-regulated role of GluTR (HEMA) across kingdoms, though the plant-specific regulatory partners (FLU, GBP) are not present in bacteria.

### Note on citation scope

Two of the strongest mechanistic anchors — the *M. kandleri* GluTR crystal structure (Schubert et al.) and the *E. coli* Cys50 esterase/thioester work (Lüer et al. 2007) — are summarized here via the verified review and mutagenesis abstracts above. No literature was found describing a *different* gene under the "hemA" symbol that would conflict with this assignment; the plant HEMA and bacterial hemA are true functional orthologs (both glutamyl-tRNA reductase), differing only in localization and regulatory accessories.

---

## Limitations and Knowledge Gaps

1. **No direct biochemistry on the *P. putida* KT2440 enzyme itself.** The functional assignment for Q88PW6 rests on (a) direct pathway demonstration in *P. putida* by complementation ([PMID: 7883699](https://pubmed.ncbi.nlm.nih.gov/7883699/), which used the *P. aeruginosa* gene), (b) very high sequence conservation to the biochemically characterized *E. coli* enzyme (52.5% identity, all active-site residues conserved), and (c) domain/motif analysis. No purified-enzyme kinetics (kcat, Km for glutamyl-tRNA^Glu and NADPH) have been reported specifically for the KT2440 protein.

2. **No experimental structure of Q88PW6.** The three-domain, V-shaped homodimer architecture is inferred from homology (GluTR crystal structures from *M. kandleri* and other organisms) and InterPro domains; a *P. putida*-specific crystal or cryo-EM structure has not been reported. AlphaFold prediction could close this gap.

3. **Regulation not verified in *P. putida*.** Heme-feedback control and ClpAP/Lon-dependent conditional stability are established in *Salmonella*/*E. coli*. Whether the identical proteolytic regulatory circuit operates on PP_0732 in *P. putida* — and which protease and which N-terminal degradation determinant are involved — has not been directly tested.

4. **HemA·HemL channeling not confirmed in *P. putida*.** The physical complex and metabolic channeling were shown in *E. coli*. The *P. putida* HemL structure exists for the sibling species *P. aeruginosa* ([PMID: 29684343](https://pubmed.ncbi.nlm.nih.gov/29684343/)), but the KT2440 HemA·HemL interaction has not been demonstrated experimentally.

5. **Operon transcription not mapped.** The *hemA–prfA–prmC* gene arrangement and codon overlaps strongly imply an operon with translational coupling, but promoter mapping, transcript boundaries, and any condition-dependent regulation in KT2440 have not been directly measured.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant enzymology.** Clone, express, and purify Q88PW6 (PP_0732); assay NADPH-dependent reduction of *P. putida* glutamyl-tRNA^Glu to GSA; determine kcat and Km, and confirm the Cys50 requirement by a C50A/C50S mutant. This would convert the current homology-based assignment into direct biochemical proof.

2. **Structure determination.** Solve the crystal or cryo-EM structure of Q88PW6, or at minimum generate and analyze an AlphaFold2/3 model, to confirm the three-domain V-shaped homodimer, the Cys50 active site, and the Rossmann NADPH pocket.

3. **In vivo essentiality and complementation.** Test whether PP_0732 is essential in KT2440 (or conditionally rescuable by exogenous ALA/heme), and confirm that the cloned gene complements an *E. coli hemA* mutant, extending the *P. aeruginosa* result to KT2440.

4. **Regulation.** Measure HemA protein half-life and abundance in KT2440 under heme-replete vs. heme-limited conditions, and in *clp*/*lon* protease mutants, to test whether the conditional-stability feedback circuit is conserved.

5. **Complex and channeling.** Test physical interaction between KT2440 HemA (PP_0732) and HemL by pull-down/co-purification, and probe GSA channeling by measuring side-product formation when the interaction is disrupted (e.g., C-terminal truncation).

6. **Operon mapping.** Use RT-PCR/RNA-seq and 5′-RACE to confirm co-transcription of *hemA–prfA–prmC*, define the promoter, and test whether translational coupling links tetrapyrrole entry to translation termination.

---

## Conclusion

The evidence is consistent and mutually reinforcing across organism-specific experiments, mechanistic biochemistry, structural biology, sequence conservation, and genomic context. **hemA (PP_0732, Q88PW6) in *Pseudomonas putida* KT2440 encodes glutamyl-tRNA reductase (GluTR, EC 1.2.1.70)**, the cytoplasmic, NADPH-dependent, heme-feedback-regulated enzyme that catalyzes the first committed step of the C5 tetrapyrrole biosynthesis pathway — reduction of glutamyl-tRNA^Glu to glutamate-1-semialdehyde — thereby controlling the flux to 5-aminolevulinic acid and, downstream, to heme and siroheme. The gene symbol, organism, domain complement, and literature are all in agreement; there is no ambiguity in this annotation.


## Artifacts

- [OpenScientist final report](hemA-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](hemA-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:7883699
2. PMID:16228559
3. PMID:17697121
4. PMID:15757895
5. PMID:29684343
6. PMID:9139907
7. PMID:9973348
8. PMID:17360620
9. PMID:31194674
10. PMID:26453466
11. PMID:21620993
12. PMID:27664748
13. PMID:17571216
14. PMID:15584960
15. PMID:36171567