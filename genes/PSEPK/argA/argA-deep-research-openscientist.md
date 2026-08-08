---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-17T16:42:43.607404'
end_time: '2026-07-17T16:55:27.566060'
duration_seconds: 763.96
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: argA
  gene_symbol: argA
  uniprot_accession: P0A0Z9
  protein_description: 'RecName: Full=Amino-acid acetyltransferase; EC=2.3.1.1; AltName:
    Full=N-acetylglutamate synthase; Short=AGS; Short=NAGS;'
  gene_info: Name=argA; OrderedLocusNames=PP_5185;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the acetyltransferase family. ArgA subfamily.
  protein_domains: AceGlu_kinase-like_sf. (IPR036393); Acyl_CoA_acyltransferase. (IPR016181);
    Asp/Glu/Uridylate_kinase. (IPR001048); GNAT_dom. (IPR000182); NAGS_kin. (IPR033719)
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
citation_count: 6
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: argA-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: argA-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** P0A0Z9
- **Protein Description:** RecName: Full=Amino-acid acetyltransferase; EC=2.3.1.1; AltName: Full=N-acetylglutamate synthase; Short=AGS; Short=NAGS;
- **Gene Information:** Name=argA; OrderedLocusNames=PP_5185;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the acetyltransferase family. ArgA subfamily.
- **Key Domains:** AceGlu_kinase-like_sf. (IPR036393); Acyl_CoA_acyltransferase. (IPR016181); Asp/Glu/Uridylate_kinase. (IPR001048); GNAT_dom. (IPR000182); NAGS_kin. (IPR033719)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "argA" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'argA' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **argA** (gene ID: argA, UniProt: P0A0Z9) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *argA* (P0A0Z9) — N-Acetylglutamate Synthase of *Pseudomonas putida* KT2440

## Summary

The gene **argA** (ordered locus **PP_5185**; UniProt **P0A0Z9**) of *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / KT2440) encodes **N-acetylglutamate synthase (NAGS; also called amino-acid acetyltransferase or AGS; EC 2.3.1.1)**. This enzyme catalyzes the transfer of an acetyl group from acetyl-CoA to the α-amino group of L-glutamate, producing **N-acetyl-L-glutamate (NAG) + coenzyme A + H⁺** (Rhea:24292). This is the **first, committed, and rate-controlling step of L-arginine biosynthesis** (step 1 of 4 leading to N²-acetyl-L-ornithine). The gene symbol, organism, protein family (acetyltransferase family, ArgA subfamily), and characteristic bidomain architecture all align unambiguously — there is no evidence of gene-symbol misassignment, and the identification is made with **high confidence**.

Structurally, P. putida ArgA is a **432-amino-acid, cytoplasmic, bidomain protein** consisting of an N-terminal **amino-acid kinase (AAK) domain** (~residues 1–285) that binds the allosteric feedback inhibitor L-arginine, and a C-terminal **GNAT (GCN5-related N-acetyltransferase) domain** (~residues 286–432) that carries the acetyltransferase active site. This "classical" NAGS architecture — biochemically and structurally dissected in the close relative *P. aeruginosa* and in *Neisseria gonorrhoeae* — assembles into a **hexameric ring** (three AAK dimers) and is catalytically active through a **one-step nucleophilic addition–elimination mechanism**. The enzyme is switched off by end-product **L-arginine**, which binds the AAK domain and triggers a large conformational change that disorders the acetyltransferase active site.

Physiologically, ArgA functions in the **cytoplasm** as the anaplerotic enzyme that **replenishes the pool of acetylated intermediates** in the cyclic ornithine-biosynthetic pathway that operates in *Pseudomonas*. Because the acetyl group is normally recycled internally by ornithine acetyltransferase (ArgJ), ArgA supplies only the net acetyl input needed to sustain the cycle. In *Pseudomonas*, flux through this committed step is governed **chiefly by allosteric feedback inhibition of the enzyme by L-arginine**, rather than by transcriptional repression (in contrast to the ArgR-repressed *arg* regulon of *Escherichia coli*). Deletion of *argA* renders *Pseudomonas* an **arginine auxotroph**, confirming the enzyme's essential, non-redundant role in de novo arginine synthesis.

---

## Key Findings

### 1. argA encodes N-acetylglutamate synthase — the first committed step of arginine biosynthesis

UniProt P0A0Z9 annotates the PP_5185/argA product as **Amino-acid acetyltransferase / N-acetylglutamate synthase (NAGS/AGS), EC 2.3.1.1**. The enzyme transfers the acetyl group from acetyl-CoA to L-glutamate, producing N-acetyl-L-glutamate + CoA. Substrate specificity is well defined: **acetyl-CoA serves as the acyl donor and L-glutamate as the acceptor**.

The functional identity is directly supported by classical genetics in the closely related *Pseudomonas aeruginosa*, where argA was biochemically identified as N-acetylglutamate synthase and shown to be **essential**: argA mutants "showed no growth on unsupplemented minimal medium" [(PMID: 408599)](https://pubmed.ncbi.nlm.nih.gov/408599/). The authors state that "N-Acetylglutamate synthase, the enzyme which replenishes the cycle of acetylated intermediates in ornithine synthesis of Pseudomonas, appears to be essential for arginine synthesis since argA mutants showed no growth on unsupplemented minimal medium." This single sentence establishes the reaction catalyzed, the pathway role, and the genetic essentiality of argA in *Pseudomonas* arginine biosynthesis.

### 2. Classical bacterial ArgA is a bidomain AAK+GNAT enzyme forming a hexameric ring, feedback-inhibited by L-arginine

The most directly relevant structural/functional dissection is that of *P. aeruginosa* ArgA [(PMID: 22447897)](https://pubmed.ncbi.nlm.nih.gov/22447897/), which describes "the classical N-acetylglutamate synthase (NAGS), an enzyme composed of N-terminal amino acid kinase (AAK) and C-terminal histone acetyltransferase (GNAT) domains that bind the feedback inhibitor arginine and the substrates, respectively." The quaternary structure is a hexamer: "three AAK domain dimers are interlinked by their N-terminal helices, conforming a hexameric ring, whereas each GNAT domain sits on the AAK domain of an adjacent dimer." Critically, the **isolated GNAT domain retains acetyltransferase activity but loses arginine sensitivity** — meaning the hexameric assembly and the AAK domain are required for allosteric regulation, not for catalysis per se.

The allosteric mechanism is illuminated by the structure of *Neisseria gonorrhoeae* NAGS [(PMID: 19095660)](https://pubmed.ncbi.nlm.nih.gov/19095660/), a hexamer of two stacked trimers in which "Binding of l-arginine to the AAK domain induces a global conformational change." In that transition (a T-to-R–like rearrangement), the acetyltransferase (NAT) domains rotate by roughly 109°, disordering the NAT active site and reducing catalytic activity. A complementary study of the bifunctional NAGS/K from *Maricaulis maris* [(PMID: 23850694)](https://pubmed.ncbi.nlm.nih.gov/23850694/) shows that when L-arginine binds, "the AcCoA binding site in the N-acetyltransferase (NAT) domain is blocked by a loop from the amino acid kinase (AAK) domain, as a result of a domain rotation that occurs when L-arginine binds," providing a second structural rationale for allosteric inhibition. The 432-aa length and bidomain layout of P. putida ArgA place it firmly within this classical, hexameric, arginine-inhibited subfamily rather than among the short (~170-aa) GNAT-only NAGS variants.

### 3. Catalytic mechanism: direct one-step acetyl transfer

The catalytic chemistry of this enzyme family was resolved crystallographically and kinetically using the *N. gonorrhoeae* NAGS–bisubstrate complex [(PMID: 23261468)](https://pubmed.ncbi.nlm.nih.gov/23261468/). The reaction "N-Acetyl-L-glutamate synthase catalyzes the conversion of AcCoA and glutamate to CoA and N-acetyl-L-glutamate (NAG), the first step of the arginine biosynthetic pathway in lower organisms," and proceeds via "a one-step nucleophilic addition-elimination mechanism with **Glu353 as the catalytic base and Ser392 as the catalytic acid**." This is a **direct (sequential/ternary-complex) acetyl transfer** — the α-amino group of glutamate attacks the thioester carbonyl of acetyl-CoA to form a tetrahedral intermediate that collapses to release CoA and NAG — rather than a ping-pong mechanism proceeding through an acetyl-enzyme intermediate.

### 4. P. putida ArgA is a 432-aa cytoplasmic bidomain enzyme catalyzing step 1/4 of the N-acetylornithine branch

Direct retrieval of UniProt P0A0Z9 confirms the organism-specific details for the target protein: gene **argA / PP_5185**; length **432 aa**; catalytic activity "**L-glutamate + acetyl-CoA = N-acetyl-L-glutamate + CoA + H(+)**" (EC 2.3.1.1, Rhea:24292); pathway annotation "**Amino-acid biosynthesis; L-arginine biosynthesis; N(2)-acetyl-L-ornithine from L-glutamate: step 1/4**"; subcellular location **Cytoplasm** (evidence code ECO:0000250, inferred from homology). The feature table lists a C-terminal N-acetyltransferase (GNAT) domain spanning residues **286–432**, implying an N-terminal AAK domain from roughly residue 1 to 285. This bidomain layout and 432-aa length match the classical hexameric, arginine-inhibited NAGS of *P. aeruginosa* (~430 aa).

### 5. Transcriptional layer: the ArgR-controlled arginine regulon (general context)

In enteric bacteria, arginine biosynthetic genes constitute a classic **regulon**. The authoritative review by Charlier & Bervoets [(PMID: 31267155)](https://pubmed.ncbi.nlm.nih.gov/31267155/) recounts that "the term 'regulon' was coined by Maas and Clark (J Mol Biol 8:365-370, 1964) for the ensemble of arginine biosynthetic genes dispersed over the E. coli chromosome but all subjected to regulation by the trans-acting argR gene product." ArgR is the arginine-responsive repressor: when charged with L-arginine, it represses transcription of *arg* genes. This establishes a **two-tier control paradigm** — transcriptional repression by arginine-bound ArgR layered on top of allosteric feedback inhibition of the committed enzyme NAGS.

### 6. In Pseudomonas, control is dominated by allosteric feedback, not transcriptional repression

A key organism-specific nuance is that *Pseudomonas* relies far less on transcriptional control of *arg* genes than *E. coli* does. Voellmy & Leisinger [(PMID: 103997)](https://pubmed.ncbi.nlm.nih.gov/103997/) systematically measured all eight arginine biosynthetic enzymes in *P. aeruginosa* grown on arginine versus its precursor glutamate and found that "In Pseudomonas aeruginosa the synthesis of only two out of eight arginine biosynthetic enzymes tested was regulated" (acetylornithine aminotransferase, induced ~14-fold; anabolic ornithine carbamoyltransferase, repressed ~18-fold). **NAGS/ArgA was not among the transcriptionally regulated enzymes**, indicating its cellular level is largely constitutive. Combined with the strong allosteric arginine inhibition of *Pseudomonas* NAGS [(PMID: 22447897)](https://pubmed.ncbi.nlm.nih.gov/22447897/), the dominant control point for the committed step in *Pseudomonas* is **post-translational feedback inhibition of the enzyme** rather than repression of its gene.

### 7. Genomic context in P. putida KT2440: monofunctional NAGS feeding a complete pathway with both acetyl-handling routes

KEGG genome analysis situates argA within a fully functional arginine biosynthetic gene set. **argA = PP_5185**, a single 1299-bp CDS (432 aa) at complement(5914261..5915559), assigned KEGG Orthology **K14682** (amino-acid N-acetyltransferase, EC 2.3.1.1), pathway **ppu00220 (Arginine biosynthesis)** and module **M00028 (Ornithine biosynthesis, glutamate ⇒ ornithine)**. Pfam motifs **AA_kinase + Acetyltransf** confirm the bidomain AAK+GNAT architecture. Its immediate genomic neighbor, PP_5186, is **argE (acetylornithine deacetylase, EC 3.5.1.16)**. Notably, the KT2440 genome encodes the full downstream pathway (argB at PP_5289; argC at PP_0432/PP_3633) **and both acetyl-recycling systems**: **argJ ornithine acetyltransferase (PP_1346, cyclic route)** and **argE acetylornithine deacetylase (PP_5186/PP_3571, linear route)**. This means the acetyl group introduced by ArgA can be either internally recycled (cyclic pathway, the energetically economical mode) or hydrolytically removed as acetate (linear pathway).

### 8. Consolidated annotation (high confidence)

Integrating all findings: argA/P0A0Z9 is the **cytoplasmic, committed entry enzyme of arginine biosynthesis** in *P. putida* KT2440 — a 432-aa amino-acid N-acetyltransferase / N-acetylglutamate synthase (EC 2.3.1.1, K14682, Rhea:24292) that converts L-glutamate + acetyl-CoA → N-acetyl-L-glutamate + CoA + H⁺ (pathway step 1/4 to N²-acetyl-L-ornithine). It has a bidomain AAK(~1–285)+GNAT(286–432) architecture matching the classical hexameric ArgA subfamily (as documented in *P. aeruginosa* [PMID: 22447897] and *N. gonorrhoeae* [PMID: 19095660]), uses a direct one-step acetyl-transfer catalytic mechanism [PMID: 23261468], and is controlled principally by allosteric L-arginine feedback inhibition in *Pseudomonas* [PMID: 22447897; 103997]. Its essentiality is demonstrated genetically — argA-null mutants are arginine auxotrophs [(PMID: 408599)](https://pubmed.ncbi.nlm.nih.gov/408599/).

---

## Mechanistic Model / Interpretation

### The reaction

```
                              ArgA / N-acetylglutamate synthase (EC 2.3.1.1)
   L-glutamate  +  acetyl-CoA  ─────────────────────────────────────────►  N-acetyl-L-glutamate  +  CoA  +  H⁺
   (acceptor)      (acyl donor)          (Rhea:24292)                        (NAG)
```

The α-amino group of L-glutamate is acetylated. This "masks" the amino group so that the downstream glutamate carbon skeleton can be phosphorylated, reduced, and transaminated without cyclizing prematurely — the acetyl group is the chemical protecting group that channels glutamate specifically toward ornithine (and thence arginine) rather than proline.

### The pathway and the acetyl cycle

*Pseudomonas*, like most bacteria, uses the **cyclic (economical) route** for ornithine biosynthesis, in which the acetyl group is conserved:

```
        ┌───────────────────────────── acetyl group recycled ─────────────────────────────┐
        │                                                                                  │
        ▼                                                                                  │
   L-glutamate ──[ArgA/NAGS]──► N-acetylglutamate ──[ArgB]──► N-acetylglutamyl-P            │
     (+AcCoA, net input)                                          │                         │
                                                                  ▼ [ArgC]                  │
                                                          N-acetylglutamate-5-semialdehyde  │
                                                                  │                         │
                                                                  ▼ [ArgD]                  │
                                                          N-acetyl-L-ornithine ─────────────┘
                                                                  │        [ArgJ: transfers acetyl
                                                                  │         back to glutamate — CYCLIC]
                                                                  ▼
                                                          L-ornithine ──► ... ──► L-arginine
                                                                  ▲
                                                 [ArgE: hydrolyzes acetyl off as acetate — LINEAR]
```

Because ArgJ (ornithine acetyltransferase) transfers the acetyl group from N-acetylornithine back onto a fresh glutamate, the bulk of the acetyl flux is internally recycled. **ArgA therefore acts anaplerotically** — it supplies only the *net* acetyl groups needed to top up the cyclic pool (lost to dilution, growth, or the linear ArgE branch). This is precisely the "replenishes the cycle of acetylated intermediates" role described for *Pseudomonas* [(PMID: 408599)](https://pubmed.ncbi.nlm.nih.gov/408599/). KT2440 encodes **both** ArgJ (PP_1346, cyclic) and ArgE (PP_5186, linear), giving it metabolic flexibility in how the acetyl group is ultimately handled.

### The regulatory switch

```
   Low [arginine]  ──►  ArgA hexamer in ACTIVE (R-like) state  ──►  high NAG synthesis  ──►  arginine made
                                                                                                  │
   High [arginine] ──►  Arg binds AAK domain ──► ~109° domain rotation ──► NAT active site         │
                        disordered / AcCoA site blocked ──► LOW NAG synthesis  ◄────── feedback ───┘
```

Two comparative structural models converge on the same outcome: in *N. gonorrhoeae* NAGS the arginine-induced rotation **disorders the NAT active site** [(PMID: 19095660)](https://pubmed.ncbi.nlm.nih.gov/19095660/), while in *M. maris* NAGS/K a loop from the AAK domain **physically blocks the acetyl-CoA binding site** [(PMID: 23850694)](https://pubmed.ncbi.nlm.nih.gov/23850694/). Either way, high arginine shuts the enzyme off. Because *Pseudomonas* largely does **not** repress the arg genes transcriptionally [(PMID: 103997)](https://pubmed.ncbi.nlm.nih.gov/103997/), this **allosteric feedback inhibition is the primary flux-control mechanism** for the committed step in this organism.

### Comparison of control logic

| Feature | *E. coli* (enteric) | *Pseudomonas* (this target) |
|---|---|---|
| Transcriptional control of *arg* genes | Strong — ArgR-repressed regulon | Weak — only 2/8 enzymes regulated |
| Allosteric feedback on NAGS/ArgA | Present | Present, **dominant** control point |
| Acetyl handling | Linear (ArgE) predominant | Cyclic (ArgJ) + linear (ArgE) both present |
| Net role of ArgA | First committed step | First committed step, **anaplerotic** to acetyl cycle |

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports the annotation |
|---|---|---|
| [408599](https://pubmed.ncbi.nlm.nih.gov/408599/) | *Genetic organization of arginine biosynthesis in P. aeruginosa* | Directly names argA as N-acetylglutamate synthase in *Pseudomonas*; demonstrates essentiality (argA mutants are arginine auxotrophs) and the anaplerotic "replenishes the cycle" role. |
| [22447897](https://pubmed.ncbi.nlm.nih.gov/22447897/) | *Functional dissection of NAGS (ArgA) of P. aeruginosa* | The single most relevant paper: defines the AAK+GNAT bidomain architecture, hexameric ring assembly, and the roles of each domain (arginine binding vs. catalysis) for *Pseudomonas* ArgA. |
| [19095660](https://pubmed.ncbi.nlm.nih.gov/19095660/) | *Mechanism of allosteric inhibition of NAGS by L-arginine* | Structural basis of feedback inhibition: arginine binding to the AAK domain drives a global conformational change (~109° NAT rotation) that disorders the active site. |
| [23261468](https://pubmed.ncbi.nlm.nih.gov/23261468/) | *N. gonorrhoeae NAGS with bisubstrate analog* | Defines the one-step nucleophilic addition–elimination catalytic mechanism (Glu353 base, Ser392 acid) and confirms the reaction as the first step of arginine biosynthesis. |
| [23850694](https://pubmed.ncbi.nlm.nih.gov/23850694/) | *Structure of M. maris NAGS/K with L-arginine bound* | Second structural model of allostery: arginine binding causes an AAK-domain loop to block the AcCoA site, explaining feedback inhibition. |
| [22174908](https://pubmed.ncbi.nlm.nih.gov/22174908/) | *Novel NAGS architecture from M. maris* | Shows domain-rotation control of activity and homology to human NAGS; contextualizes the bidomain family and quaternary-structure diversity (tetramer vs. hexamer). |
| [31267155](https://pubmed.ncbi.nlm.nih.gov/31267155/) | *Regulation of arginine biosynthesis in E. coli* (review) | Establishes the ArgR-repressed arginine regulon paradigm — the transcriptional layer against which *Pseudomonas* is contrasted. |
| [103997](https://pubmed.ncbi.nlm.nih.gov/103997/) | *Regulation of arginine enzymes in P. aeruginosa* | Shows only 2/8 arg enzymes are transcriptionally regulated in *Pseudomonas*; NAGS is not, implying reliance on allosteric feedback. |
| [16409639](https://pubmed.ncbi.nlm.nih.gov/16409639/) | *Bioinformatic analysis of gene-enzyme relationships (marine γ-proteobacteria)* | Important caveat: warns that the name "argA" has been applied to structurally different entities (classical NAGS vs. short GNAT-only NAGS vs. argH-A fusions); confirms P. putida ArgA is the *classical* type. |
| [27037498](https://pubmed.ncbi.nlm.nih.gov/27037498/) | *NAGS deficiency mutational spectrum* | Uses recombinant *P. aeruginosa* NAGS as the experimental model; corroborates the paramount catalytic role of the C-terminal GNAT domain and the modulatory role of the AAK domain. |

**Note on gene-symbol ambiguity:** The literature explicitly flags that "argA" has been used for structurally distinct enzymes [(PMID: 16409639)](https://pubmed.ncbi.nlm.nih.gov/16409639/). We verified that P. putida ArgA (432 aa, AAK+GNAT bidomain, Pfam AA_kinase + Acetyltransf) is the **classical NAGS type** (as in *E. coli* and *P. aeruginosa*), not the short ~170-aa GNAT-only variant (as in *M. tuberculosis*) nor an argH-A fusion (as in *Moritella*). The identification is therefore unambiguous.

---

## Limitations and Knowledge Gaps

1. **No direct biochemistry on the P. putida KT2440 protein itself.** Every functional and structural claim about the *specific* PP_5185 gene product is inferred by strong homology from *P. aeruginosa* ArgA (~430 aa, closely related) and from more distant NAGS structures (*N. gonorrhoeae*, *M. maris*). No purified P. putida ArgA kinetic constants (Kₘ for glutamate/acetyl-CoA, kcat, IC₅₀ for arginine) have been reported here.

2. **Subcellular localization is inferred, not measured.** UniProt assigns cytoplasmic localization with evidence code ECO:0000250 (by similarity). This is highly plausible for a soluble biosynthetic enzyme but has not been experimentally verified in P. putida.

3. **Quaternary structure not directly confirmed for P. putida.** The hexameric ring is documented for *P. aeruginosa*; the P. putida assembly state is assumed from homology. Some family members (e.g., *M. maris* NAGS/K) are tetramers, so the oligomeric state is not universally conserved across the family.

4. **Regulatory details in P. putida specifically.** The conclusion that flux control is dominated by allosteric feedback rather than transcription is drawn from *P. aeruginosa* [(PMID: 103997)](https://pubmed.ncbi.nlm.nih.gov/103997/) and general reasoning; direct measurement of argA/PP_5185 expression under arginine excess in KT2440, and quantitative in vitro arginine inhibition of the KT2440 enzyme, are lacking.

5. **Relative flux through cyclic (ArgJ) vs. linear (ArgE) routes** in KT2440 has not been quantified; both genes are present, but their relative contributions under different growth conditions are unknown.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant enzymology of PP_5185.** Clone, over-express, and purify P. putida ArgA; measure steady-state kinetics (Kₘ for L-glutamate and acetyl-CoA, kcat) and determine the IC₅₀/Kᵢ for L-arginine feedback inhibition. This would replace homology inference with direct data for the target.

2. **Structural determination.** Solve the crystal or cryo-EM structure of P. putida ArgA in apo, substrate-bound, and arginine-bound states to confirm the hexameric ring and the arginine-induced domain rotation directly for this protein.

3. **Genetic complementation/auxotrophy test.** Construct a clean PP_5185 deletion in KT2440 and confirm arginine auxotrophy plus rescue by exogenous arginine or by a complementing plasmid — the definitive test of essentiality and non-redundancy in this strain.

4. **Regulatory profiling.** Use RT-qPCR/RNA-seq to measure argA transcript levels under arginine-replete vs. arginine-limited growth, and metabolomics (NAG pool sizing) to test whether allosteric inhibition is indeed the dominant in vivo control point in KT2440.

5. **Flux partitioning between ArgJ and ArgE.** Use ¹³C-labeled acetyl tracing or single/double knockouts of argJ (PP_1346) and argE (PP_5186) to quantify the relative use of the cyclic vs. linear acetyl-handling routes.

6. **Domain-dissection assay.** Express the isolated GNAT domain (residues ~286–432) of P. putida ArgA to test whether, as in *P. aeruginosa*, it retains acetyltransferase activity but loses arginine sensitivity — directly localizing catalysis vs. regulation in this ortholog.

---

## Conclusion

*argA* (PP_5185; UniProt P0A0Z9) of *Pseudomonas putida* KT2440 encodes **N-acetylglutamate synthase (EC 2.3.1.1)**, a cytoplasmic, 432-aa, bidomain (AAK + GNAT) enzyme that catalyzes the **acetyl-CoA-dependent acetylation of L-glutamate to N-acetyl-L-glutamate**, the first committed and essential step of L-arginine biosynthesis. It operates anaplerotically to replenish the acetyl-intermediate cycle, assembles into the classical hexameric ArgA architecture, uses a direct one-step acetyl-transfer mechanism, and is controlled principally by **allosteric feedback inhibition by L-arginine**. The annotation is supported by direct genetics in *Pseudomonas* and by extensive structural/mechanistic work on close homologs, with high overall confidence and no evidence of gene-symbol misidentification.


## Artifacts

- [OpenScientist final report](argA-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](argA-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:22447897
2. PMID:19095660
3. PMID:23850694
4. PMID:23261468
5. PMID:31267155
6. PMID:16409639