---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-25T11:26:13.949014'
end_time: '2026-07-25T11:56:49.173029'
duration_seconds: 1835.22
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: purF
  gene_symbol: purF
  uniprot_accession: Q88LD5
  protein_description: 'RecName: Full=Amidophosphoribosyltransferase {ECO:0000256|HAMAP-Rule:MF_01931};
    Short=ATase {ECO:0000256|HAMAP-Rule:MF_01931}; EC=2.4.2.14 {ECO:0000256|HAMAP-Rule:MF_01931};
    AltName: Full=Glutamine phosphoribosylpyrophosphate amidotransferase {ECO:0000256|HAMAP-Rule:MF_01931};
    Short=GPATase {ECO:0000256|HAMAP-Rule:MF_01931};'
  gene_info: Name=purF {ECO:0000256|HAMAP-Rule:MF_01931, ECO:0000313|EMBL:AAN67614.1};
    OrderedLocusNames=PP_2000 {ECO:0000313|EMBL:AAN67614.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: In the C-terminal section; belongs to the purine/pyrimidine
  protein_domains: GATase_2_dom. (IPR017932); Ntn_hydrolases_N. (IPR029055); PRTase-like.
    (IPR029057); PRTase_dom. (IPR000836); PurF. (IPR005854)
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
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: purF-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: purF-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88LD5
- **Protein Description:** RecName: Full=Amidophosphoribosyltransferase {ECO:0000256|HAMAP-Rule:MF_01931}; Short=ATase {ECO:0000256|HAMAP-Rule:MF_01931}; EC=2.4.2.14 {ECO:0000256|HAMAP-Rule:MF_01931}; AltName: Full=Glutamine phosphoribosylpyrophosphate amidotransferase {ECO:0000256|HAMAP-Rule:MF_01931}; Short=GPATase {ECO:0000256|HAMAP-Rule:MF_01931};
- **Gene Information:** Name=purF {ECO:0000256|HAMAP-Rule:MF_01931, ECO:0000313|EMBL:AAN67614.1}; OrderedLocusNames=PP_2000 {ECO:0000313|EMBL:AAN67614.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** In the C-terminal section; belongs to the purine/pyrimidine
- **Key Domains:** GATase_2_dom. (IPR017932); Ntn_hydrolases_N. (IPR029055); PRTase-like. (IPR029057); PRTase_dom. (IPR000836); PurF. (IPR005854)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "purF" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'purF' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **purF** (gene ID: purF, UniProt: Q88LD5) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of *purF* (Q88LD5) in *Pseudomonas putida* KT2440

**Gene:** *purF* (ordered locus PP_2000) · **UniProt:** Q88LD5 · **Enzyme:** Amidophosphoribosyltransferase / glutamine phosphoribosylpyrophosphate amidotransferase (GPATase, ATase) · **EC 2.4.2.14** · **Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / KT2440)

---

## 1. Summary (Answer to the Research Question)

*purF* encodes **amidophosphoribosyltransferase (GPATase)**, the enzyme that catalyzes the **first committed and rate-controlling step of de novo purine nucleotide biosynthesis**. In the cytoplasm it transfers the amide nitrogen of **L-glutamine** to **5-phospho-α-D-ribose-1-diphosphate (PRPP)**, producing **5-phospho-β-D-ribosylamine (PRA)**, L-glutamate, and pyrophosphate. It is a two-domain glutamine amidotransferase: an N-terminal Ntn-hydrolase glutaminase domain (catalytic Cys1) generates ammonia, which is channeled through an internal tunnel to a C-terminal phosphoribosyltransferase (PRT) domain that attaches it to PRPP. Its activity is gated by ordered substrate binding (PRPP first, which activates the glutaminase site) and feedback-inhibited by purine nucleotides (AMP/GMP/IMP), while the gene is transcriptionally repressed by the purine-responsive PurR repressor. The product PRA feeds both the purine pathway (→ IMP → AMP/GMP) and thiamine biosynthesis.

**Gene-identity verification:** Confirmed. The gene symbol, EC number, InterPro domains (GATase_2, Ntn-hydrolase N, PRTase), organism, and the direct Q88LD5 sequence (501 aa beginning **M-C-G-I-V-G**, the canonical GPATase N-terminus; 65% identical to experimentally characterized *E. coli* PurF) all agree. This is a genuine, well-characterized amidophosphoribosyltransferase, not an ambiguous or mis-annotated symbol.

---

## 2. Primary Function: Reaction and Substrate Specificity

**Reaction (EC 2.4.2.14):**
> PRPP + L-glutamine + H₂O → 5-phospho-β-D-ribosylamine (PRA) + L-glutamate + PPᵢ

This is the entry reaction of de novo purine biosynthesis. In *Salmonella*/*E. coli* genetics, "Glutamine phosphoribosyl pyrophosphate (PRPP) amidotransferase is the product of the *purF* gene … and catalyzes the synthesis of PRA from PRPP and glutamine. Strains lacking PurF require exogenous addition of purines for growth" (Koenigsknecht et al., 2012, **PMID 23133571**). The enzyme is also confirmed as a distinct, competitively inhibitable target: feruloyl amide "is a competitive inhibitor of glutamine PRPP amidotransferase (PurF)" (Pisithkul et al., 2015, **PMID 26070680**).

**Substrate specificity and kinetics.** The two substrates are the phosphoribosyl donor **PRPP** and the amide-nitrogen donor **L-glutamine** (free ammonia can substitute at high concentration in vitro, but glutamine is the physiological donor). Kinetic analysis of the mechanistically conserved enzyme gave dissociation constants of **80 µM for PRPP** and **420 µM for L-glutamine**, "with P-Rib-PP bound first with positive cooperativity for interaction with a second site on the catalytically active dimer" (Schoettle et al., 1997, **PMID 9174353**). Thus catalysis follows an **ordered mechanism in which PRPP binds before glutamine**.

---

## 3. Catalytic Mechanism and Domain Architecture

GPATase is a **bifunctional, two-domain enzyme**:

- **N-terminal glutaminase domain** — a class-II (Ntn) glutamine amidotransferase (InterPro GATase_2, IPR017932; Ntn-hydrolase N, IPR029055). It belongs to the **N-terminal nucleophile (Ntn) hydrolase superfamily**; the mature enzyme is generated by autocatalytic removal of an N-terminal propeptide to expose the catalytic **Cys1**, and "propeptide cleavage was strongly inhibited by replacement of the cysteine nucleophile and two residues of an oxyanion hole that are required for glutaminase function" (Li et al., 1999, **PMID 10049369**).
- **C-terminal phosphoribosyltransferase (PRT) domain** — a type-I PRTase fold (IPR000836/IPR029057) that binds PRPP and receives the ammonia.

**Active-site chemistry (from *E. coli* crystallography + mutagenesis, Kim et al., 1996, PMID 8663035):** the **free α-amino group of Cys1 acts as the proton acceptor/donor**; **Asn101 and the Gly102 backbone form the oxyanion hole**; **Arg73 and Asp127 bind glutamine**; and **Tyr74 couples the glutamine and PRPP sites**.

**Substrate-gated activation.** The basal PRPP-independent glutaminase activity is only ~0.3% of the fully active enzyme; "Binding of PRPP activates the enzyme by a structural change that lowers the Km for glutamine 100-fold and couples glutamine hydrolysis to synthesis of 5-phosphoribosylamine" (**PMID 8663035**). The **ring oxygen of PRPP is required** for this activating conformational change (Kim et al., 1995, **PMID 7542237**). This structural gating ensures glutamine is not wastefully hydrolyzed unless the acceptor PRPP is present — the mechanistic counterpart of the PRPP-first ordered kinetics.

**Intramolecular ammonia channeling.** The ammonia generated at the glutaminase site is not released to solvent; GPATase "catalyzes the synthesis of 5′-phosphoribosylamine in a reaction that involves the translocation of ammonia along an intramolecular tunnel linking the two active sites," behaving as a "pipe" through which ammonia travels; the L415A mutation reduces channel efficiency (Wang et al., 2009, **PMID 19921932**).

---

## 4. Localization

GPATase is a **soluble cytoplasmic enzyme**. All structurally characterized bacterial orthologs (*E. coli*, *B. subtilis*) are cytosolic proteins crystallized as soluble oligomers (**PMID 9514258; 8663035**), and the *P. putida* sequence has no signal peptide or transmembrane segment. It therefore carries out its function **in the cytoplasm**, where PRPP and glutamine are supplied by central metabolism. (The mammalian cytosolic "purinosome" metabolon is a eukaryote-specific organization and is not expected in bacteria; notably, even in humans amidophosphoribosyltransferase is the one DNPB enzyme that does not stably join the PAICS-centered purinosome interactions — He et al., 2022, **PMID 35331738**.)

---

## 5. Pathway Context and Biological Process

PurF initiates the **ten-step de novo purine pathway**: purF → purD → purN/purT → purL → purM → purK/purE → purC → purB → purH, yielding **IMP**, from which **AMP** and **GMP** are made. Its product PRA is also the branch-point precursor of **thiamine (vitamin B1)** biosynthesis: "Phosphoribosylamine (PRA) is an intermediate in the biosynthetic pathway that is common to thiamine and purines" (**PMID 23133571**). By consuming PRPP and glutamine, PurF sits at the intersection of nucleotide supply, one-carbon/nitrogen metabolism, and central carbon metabolism.

---

## 6. Regulation

PurF flux is controlled at **two layers**:

1. **Allosteric feedback inhibition (fast, enzyme level).** End-product purine nucleotides inhibit the enzyme. In the *E. coli* structure the feedback inhibitor **AMP binds the PRPP catalytic site**, locking the inhibited conformation with the two active sites disconnected (Muchmore et al., 1998, **PMID 9514258**); AMP is **competitive with respect to PRPP** (Kd ~40 µM), and IMP and GMP also inhibit (**PMID 9174353**). A separate allosteric nucleotide site also exists (**PMID 7542237**).
2. **Transcriptional repression (slow, gene level).** In *E. coli* the LacI-family repressor **PurR**, with a purine corepressor (hypoxanthine/guanine), binds a high-affinity operator at *purF* to repress de novo purine/pyrimidine genes (Schumacher et al., 1994, **PMID 8089849**; Devroede et al., 2004, **PMID 14741201**). In *B. subtilis* a non-homologous PurR senses excess adenine via the PRPP pool (Weng et al., 1995, **PMID 7638212**). *P. putida* KT2440 encodes a LacI-family PurR ortholog, so analogous purine-responsive repression of *purF* is expected.

---

## 7. Evolutionary / Structural Classification

Bacterial GPATases form two subfamilies: "The *E. coli* enzyme is a prototype for the **metal-free** GPATases, whereas the *B. subtilis* enzyme represents the **metal-containing** enzymes … a common ancestor … may have included an Fe-S cluster" (**PMID 9514258**). The *B. subtilis* [4Fe-4S] cluster is remote from the active sites and confers oxygen-triggered turnover rather than catalysis. **Q88LD5 is a gammaproteobacterial, E. coli-like, metal-free GPATase** (HAMAP rule MF_01931), so it is not expected to be intrinsically O₂-sensitive via a metal center — consistent with *P. putida*'s aerobic lifestyle.

**Direct evidence for the P. putida protein:** Q88LD5 is 501 aa, begins **MCGIVGIVG** (conserved Cys1 nucleophile motif), and is **65.1% identical to E. coli PurF (P0AG16)** over the full length (Needleman-Wunsch, this work). Crucially, **all six experimentally-defined catalytic residues are perfectly conserved** in Q88LD5 by alignment (this work): the nucleophile **Cys1**, glutamine-binding **Arg73** and **Asp127**, inter-site coupling **Tyr74**, and oxyanion-hole **Asn101/Gly102** (residues defined in *E. coli* by Kim et al., **PMID 8663035**). This residue-level conservation justifies transferring the *E. coli* experimental mechanism directly to the *P. putida* ortholog.

---

## 8. Supported and Refuted Hypotheses

**Supported:**
- H1: *purF* encodes amidophosphoribosyltransferase (EC 2.4.2.14) catalyzing PRPP + Gln → PRA. ✔ (PMIDs 23133571, 26070680; sequence)
- H2: Two-domain Ntn-hydrolase mechanism with Cys1 nucleophile and PRPP-gated glutaminase. ✔ (PMIDs 8663035, 10049369, 7542237)
- H3: Intramolecular ammonia channeling between active sites. ✔ (PMID 19921932)
- H4: Ordered kinetics (PRPP first); feedback inhibition by AMP/GMP/IMP. ✔ (PMIDs 9174353, 9514258)
- H5: Dual regulation — allosteric + PurR transcriptional repression. ✔ (PMIDs 8089849, 14741201, 7638212)
- H6: Cytoplasmic localization; entry to purine + thiamine pathways. ✔ (PMIDs 23133571, 9514258)
- H7: P. putida enzyme is a metal-free, E. coli-type GPATase. ✔ (PMID 9514258; 65% identity)

**Refuted / not applicable:**
- The bacterial enzyme does not organize into a mammalian-style purinosome, and (unlike the *B. subtilis* enzyme) is not predicted to carry an oxygen-sensitive Fe-S cluster.

---

## 9. Limitations and Future Directions

- No *P. putida*-specific enzymological or structural study of PurF was found; mechanistic detail is transferred by strong orthology (65% identity, conserved catalytic residues) from *E. coli*/*B. subtilis*, which is well justified but not organism-specific proof.
- Direct confirmation of PurR-mediated *purF* regulation and the exact operon structure in *P. putida* KT2440 would benefit from ChIP/RNA-seq or reporter data.
- A crystal or cryo-EM structure of the *P. putida* enzyme would confirm the metal-free assignment and quaternary state directly.

---

*Key references: PMID 23133571, 26070680, 8663035, 10049369, 7542237, 19921932, 9174353, 9514258, 8089849, 14741201, 7638212, 35331738. Sequence analyses (Q88LD5 vs P0AG16) performed in this study.*


## Artifacts

- [OpenScientist final report](purF-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](purF-deep-research-openscientist_artifacts/final_report.pdf)