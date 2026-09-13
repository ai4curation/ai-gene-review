---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-25T15:29:06.316922'
end_time: '2026-07-25T15:37:14.527528'
duration_seconds: 488.21
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: davT
  gene_symbol: davT
  uniprot_accession: Q88RB9
  protein_description: 'RecName: Full=5-aminovalerate aminotransferase DavT; EC=2.6.1.48;
    AltName: Full=5-aminovalerate transaminase; AltName: Full=Delta-aminovalerate
    aminotransferase;'
  gene_info: Name=davT; OrderedLocusNames=PP_0214;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the class-III pyridoxal-phosphate-dependent
  protein_domains: 4NH2But_aminotransferase_bac. (IPR004632); Aminotrans_3. (IPR005814);
    Aminotrans_3_PPA_site. (IPR049704); Class-III_PLP-dep_AT. (IPR050103); PyrdxlP-dep_Trfase.
    (IPR015424)
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
citation_count: 4
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: davT-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: davT-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88RB9
- **Protein Description:** RecName: Full=5-aminovalerate aminotransferase DavT; EC=2.6.1.48; AltName: Full=5-aminovalerate transaminase; AltName: Full=Delta-aminovalerate aminotransferase;
- **Gene Information:** Name=davT; OrderedLocusNames=PP_0214;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the class-III pyridoxal-phosphate-dependent
- **Key Domains:** 4NH2But_aminotransferase_bac. (IPR004632); Aminotrans_3. (IPR005814); Aminotrans_3_PPA_site. (IPR049704); Class-III_PLP-dep_AT. (IPR050103); PyrdxlP-dep_Trfase. (IPR015424)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "davT" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'davT' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **davT** (gene ID: davT, UniProt: Q88RB9) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# DavT (PP_0214, Q88RB9): 5-Aminovalerate Aminotransferase in *Pseudomonas putida* KT2440

## Summary

**DavT (gene *davT*, ordered locus PP_0214, UniProt Q88RB9) is a pyridoxal-5′-phosphate (PLP)-dependent, class-III aminotransferase (EC 2.6.1.48) that catalyzes the penultimate step of the aminovalerate branch of L-lysine catabolism in *Pseudomonas putida* KT2440.** The enzyme transfers the ω-amino group of 5-aminovalerate (δ-aminovalerate) onto the 2-oxo acid acceptor 2-oxoglutarate, producing glutarate-5-semialdehyde (glutarate semialdehyde) and L-glutamate. This transamination reaction converts a linear C5 ω-amino acid into a C5 semialdehyde that is subsequently oxidized by the neighboring enzyme DavD (glutarate semialdehyde dehydrogenase) to glutarate — the key metabolic node at which lysine-derived carbon and nitrogen enter central (TCA) metabolism.

The gene is organized in the **davDT operon**, transcribed from a single σ⁷⁰-dependent promoter and induced specifically by the pathway intermediate 5-aminovalerate rather than by lysine itself. Two upstream enzymes generate DavT's substrate: DavB (lysine 2-monooxygenase) oxidizes L-lysine to 5-aminovaleramide, and DavA (δ-aminovaleramidase) hydrolyzes that amide to 5-aminovalerate. The DavT step therefore sits at the heart of a well-defined four-enzyme route (DavB → DavA → DavT → DavD) that enables *P. putida* to use L-lysine as a sole carbon and nitrogen source. Because this pathway produces the industrially valuable C5 platform chemicals 5-aminovalerate and glutarate, DavT has been widely transplanted into engineered *Escherichia coli* and *Corynebacterium glutamicum* production strains.

The identity of the target is unambiguous: the gene symbol *davT*, the organism (*P. putida* KT2440), the EC number (2.6.1.48), and the class-III PLP aminotransferase domain architecture all align consistently across UniProt annotation and multiple primary studies. The enzyme's subcellular localization is cytoplasmic, consistent with its role in a soluble catabolic pathway and the absence of signal/transmembrane features. The chief remaining knowledge gap is the lack of a dedicated in-vitro kinetic and structural characterization of the *P. putida* DavT enzyme itself; its homodimeric fold, ping-pong bi-bi mechanism, and ω-amino-acid active-site specificity are inferred from robust family membership rather than from a solved structure or purified-enzyme assay.

---

## Gene/Protein Identity Verification

Before presenting the research, the target identity was verified against the UniProt record and the primary literature. All descriptors are mutually consistent — there is no evidence of gene-symbol ambiguity or cross-organism confusion for this protein.

| Attribute | Value | Verified against |
|-----------|-------|------------------|
| **UniProt accession** | Q88RB9 | UniProt |
| **Gene symbol** | *davT* | PMID 30144560, 15150230 |
| **Locus tag** | PP_0214 | UniProt |
| **Protein** | 5-aminovalerate aminotransferase (δ-aminovalerate transaminase) | PMID 30144560 |
| **EC number** | 2.6.1.48 | UniProt |
| **Organism** | *Pseudomonas putida* KT2440 (ATCC 47054 / DSM 6125) | PMID 15150230, 16237033 |
| **Family** | Class-III PLP-dependent aminotransferase | UniProt domains (IPR004632, IPR005814, IPR049704, IPR050103, IPR015424) |

The gene symbol *davT* matches the protein description (5-aminovalerate transaminase); the organism is confirmed as *P. putida* KT2440 in multiple primary studies; and the protein family/domain content aligns with the class-III PLP aminotransferase mechanism described in the literature. **Verification passed — research proceeds on the correct gene.**

---

## Key Findings

### Finding 1 — DavT is 5-aminovalerate:2-oxoglutarate aminotransferase (EC 2.6.1.48)

DavT (PP_0214) is definitively identified as **5-aminovalerate transaminase** operating within the L-lysine aminovalerate catabolic pathway. Kim et al. (2019), in reconstructing a glutaric-acid biosynthesis pathway in *C. glutamicum*, state explicitly that the "*Pseudomonas putida davT and davD genes encoding 5-aminovalerate transaminase and glutarate semialdehyde dehydrogenase, respectively*" were used, with *davB* (lysine 2-monooxygenase) and *davA* (δ-aminovaleramidase) supplying the upstream steps [PMID: 30144560](https://pubmed.ncbi.nlm.nih.gov/30144560/). This places DavT unambiguously as the third of four enzymes converting L-lysine to glutarate.

The molecular function is corroborated by the UniProt annotation for Q88RB9, which assigns **EC 2.6.1.48** and identifies the protein as a class-III PLP-dependent aminotransferase. The diagnostic domain content — Aminotrans_3 (IPR005814), the bacterial 4-aminobutyrate-aminotransferase-like subfamily signature 4NH2But_aminotransferase_bac (IPR004632), the Aminotrans_3 PLP-attachment site (IPR049704), the class-III PLP-dependent aminotransferase family (IPR050103), and the PLP-dependent transferase fold (IPR015424) — is exactly the architecture expected for an ω-amino-acid:2-oxo-acid aminotransferase. The reaction catalyzed is:

```
5-aminovalerate + 2-oxoglutarate  ⇌  glutarate-5-semialdehyde + L-glutamate
```

The amino group is transferred from the terminal (δ, ω) carbon of the linear C5 amino acid to the α-keto acceptor, regenerating L-glutamate and leaving a reactive C5 semialdehyde for downstream oxidation.

### Finding 2 — *davT* lies in the davDT operon, induced by 5-aminovalerate

Revelles et al. (2004) demonstrated that *davD* and *davT* form a single transcriptional unit — the **davDT operon** — transcribed from one σ⁷⁰-dependent promoter: "*We show that the davDT genes form an operon transcribed from a single sigma70-dependent promoter*" [PMID: 15150230](https://pubmed.ncbi.nlm.nih.gov/15150230/). Basal expression from the PdavD promoter rose roughly four-fold in the presence of exogenous lysine, but the physiologically relevant inducer proved to be the pathway intermediate itself. In a mutant blocked in converting lysine to δ-aminovalerate, δ-aminovalerate — but not lysine — activated the operon: "*the true inducer of this operon seems to be delta-aminovaleric acid because in a mutant unable to metabolize lysine to delta-aminovaleric acid, this compound, but not lysine, acted as an effector*" [PMID: 15150230](https://pubmed.ncbi.nlm.nih.gov/15150230/).

This regulatory logic is elegant: DavT is synthesized precisely when its substrate accumulates, coupling enzyme expression to substrate availability. Efficient induction by lysine additionally required ABC-transporter-mediated lysine uptake, meaning the signal must be internalized and metabolically converted to 5-aminovalerate before the operon responds. The operonic organization also co-regulates DavT with its immediate downstream partner DavD, ensuring the reactive semialdehyde intermediate is efficiently handed off and oxidized.

### Finding 3 — The aminovalerate route is one of two interconnected lysine-catabolic pathways converging on glutarate

Revelles et al. (2005) used L-[U-¹³C,U-¹⁵N]lysine isotopic tracing to show that *P. putida* KT2440 runs the **aminovalerate and aminoadipate pathways simultaneously** as parallel routes of L-lysine catabolism [PMID: 16237033](https://pubmed.ncbi.nlm.nih.gov/16237033/). The aminovalerate branch begins when "*the davB and davA genes that encode the enzymes involved in the oxidation of L-lysine to delta-aminovaleramide and the hydrolysis of the latter to delta-aminovalerate*" generate DavT's substrate. Crucially, the two pathways interconnect at their lower ends: "*there is yet another interconnection at the lower end of the pathways in which aminoadipate is channeled to yield glutarate*" [PMID: 16237033](https://pubmed.ncbi.nlm.nih.gov/16237033/).

Glutarate — the product formed immediately downstream of the DavT/DavD steps — is thus the **metabolic convergence point** of lysine catabolism. Mutants disrupted in either pathway failed to grow on L-lysine as a sole carbon and nitrogen source, confirming both routes are physiologically operative and that the glutarate node is essential for full lysine utilization. This situates DavT not as an isolated enzyme but as a committed step feeding a shared metabolic funnel.

### Finding 4 — DavT connects L-lysine to central metabolism via glutarate; validated by genome-wide fitness profiling

Thompson et al. (2019) applied massively parallel random-barcode transposon sequencing (RB-TnSeq) fitness profiling to resolve the genetic and biochemical links between lysine metabolism and central metabolism in *P. putida*, noting that "*Despite intensive study for 50 years, the biochemical and genetic links between lysine metabolism and central metabolism in*" this organism had remained incompletely resolved [PMID: 31064836](https://pubmed.ncbi.nlm.nih.gov/31064836/). Their high-throughput approach confirmed and extended the aminovalerate route (DavB/DavA/DavT/DavD → glutarate) and mapped the downstream glutarate-catabolic enzymes that feed the TCA cycle.

This complements the isotope-tracing work of Revelles et al. (2005), which showed both lysine pathways converge on glutarate: "*there is yet another interconnection at the lower end of the pathways in which aminoadipate is channeled to yield glutarate*" [PMID: 16237033](https://pubmed.ncbi.nlm.nih.gov/16237033/). Together the two orthogonal methods — targeted isotope tracing and genome-wide fitness profiling — establish that the DavT-generated semialdehyde, once oxidized to glutarate, is the gateway through which lysine-derived carbon and nitrogen enter central metabolism, enabling growth on lysine as a sole C/N source.

### Finding 5 — DavT is inferred to be a homodimeric fold-type-I PLP enzyme using a ping-pong mechanism specific for C5 ω-amino acids

Structurally, DavT (Q88RB9) carries the full diagnostic complement of a **class-III PLP-dependent aminotransferase**: the Aminotrans_3 domain (IPR005814), the Aminotrans_3 PLP-attachment site containing the catalytic PLP-binding lysine (IPR049704), the PLP-dependent transferase fold (IPR015424), and the bacterial 4-aminobutyrate-aminotransferase-like subfamily signature (IPR004632). From this family membership, the enzyme is inferred to (i) assemble as a homodimer with active sites at the subunit interface, (ii) operate by a **ping-pong bi-bi mechanism** in which the PLP cofactor cycles to pyridoxamine-5′-phosphate (PMP) and back as the amino group shuttles between amino-donor and 2-oxo-acid acceptor, and (iii) possess an active site adapted to bind linear C5 ω-amino acids such as 5-aminovalerate.

Importantly, **no experimental crystal structure or in-vitro kinetic study of the *P. putida* DavT enzyme was located in the retrieved literature.** Searches for a solved structure or purified-enzyme kinetic characterization returned nothing specific to this protein. Consequently the oligomeric state, mechanism, and active-site substrate specificity described here are strong bioinformatic inferences from a well-characterized enzyme family (which includes GABA aminotransferases and ornithine aminotransferases), not direct measurements on DavT itself. This is the principal experimental gap in the current annotation.

---

## Mechanistic Model / Interpretation

### The aminovalerate pathway of L-lysine catabolism

DavT catalyzes the third of four sequential reactions that dismantle L-lysine into glutarate. The pathway, and DavT's precise position within it, is summarized below.

```
                  DavB                 DavA                  DavT                    DavD
 L-lysine ──────────────────► 5-amino- ─────────────► 5-amino- ──────────────► glutarate- ───────────► glutarate
   (C6)    lysine 2-mono-      valeramide δ-amino-      valerate  5-aminovalerate  5-semi-   glutarate     (C5
           oxygenase           (amide)    valeramidase  (C5 ω-    aminotransferase aldehyde  semialdehyde  dicarb-
           (+O2, -CO2)                     (hydrolysis, amino     (EC 2.6.1.48)             dehydrogenase  oxylate)
                                           -NH3)        acid)     +2-oxoglutarate           (+NAD(P)+)
                                                                  -L-glutamate
```

The specific chemistry of the DavT step:

| Component | Role in the DavT reaction |
|-----------|---------------------------|
| **Amino donor (substrate)** | 5-aminovalerate (δ-aminovalerate), a linear C5 ω-amino acid |
| **Amino acceptor (co-substrate)** | 2-oxoglutarate (α-ketoglutarate) |
| **Cofactor** | Pyridoxal-5′-phosphate (PLP), covalently tethered via an active-site lysine |
| **Product 1** | Glutarate-5-semialdehyde (glutarate semialdehyde) |
| **Product 2** | L-glutamate (regenerated from 2-oxoglutarate) |
| **Downstream fate of product 1** | Oxidized by DavD to glutarate, then routed into central metabolism |
| **EC class** | 2.6.1.48 (ω-amino-acid:2-oxoglutarate aminotransferase) |

### Why the operon and inducer logic matter

The **davDT operon** links DavT's expression to DavD's expression and to the accumulation of 5-aminovalerate. This achieves two things simultaneously. First, co-transcription of *davT* and *davD* guarantees that the reactive glutarate-5-semialdehyde produced by DavT is immediately handled by DavD, minimizing accumulation of a potentially cytotoxic aldehyde. Second, because 5-aminovalerate itself is the true inducer, the cell only invests in the transaminase/dehydrogenase pair when the substrate is actually present — a just-in-time expression strategy typical of catabolic operons under σ⁷⁰ control.

### The glutarate node and entry into central metabolism

DavT's biological significance derives from what happens two steps downstream. Both the aminovalerate pathway (via DavT/DavD) and the parallel aminoadipate pathway converge on **glutarate**. Glutarate is then further catabolized (as mapped by both isotope tracing and RB-TnSeq fitness profiling) to feed the TCA cycle, allowing lysine-derived carbon and nitrogen to fuel growth. In this framing, DavT is best understood as the **committed transamination step that liberates the lysine ω-nitrogen (onto glutamate) while delivering the carbon skeleton toward the shared glutarate funnel.**

### Localization

All evidence indicates DavT functions in the **cytoplasm**: it is a soluble PLP enzyme of a catabolic pathway whose substrate (5-aminovalerate) is generated intracellularly from imported lysine, its operon partner DavD is a soluble dehydrogenase, and the protein lacks any signal peptide or transmembrane segment characteristic of secreted or membrane-associated proteins. This is fully consistent with the class-III aminotransferase family, whose members are cytosolic enzymes.

---

## Evidence Base

| PMID | Study | How it supports the findings |
|------|-------|------------------------------|
| [30144560](https://pubmed.ncbi.nlm.nih.gov/30144560/) | *Metabolic engineering of C. glutamicum for the production of glutaric acid* (Kim et al., 2019) | Directly names *davT* as "5-aminovalerate transaminase" and *davD* as "glutarate semialdehyde dehydrogenase," situating DavT downstream of DavB/DavA and upstream of DavD. Primary basis for **Finding 1**. |
| [15150230](https://pubmed.ncbi.nlm.nih.gov/15150230/) | *The davDT operon of P. putida is induced by delta-aminovaleric acid* (Revelles et al., 2004) | Establishes operon structure (single σ⁷⁰ promoter) and identifies 5-aminovalerate as the true inducer. Basis for **Finding 2**. |
| [16237033](https://pubmed.ncbi.nlm.nih.gov/16237033/) | *Multiple and interconnected pathways for L-lysine catabolism in P. putida KT2440* (Revelles et al., 2005) | ¹³C/¹⁵N isotope tracing defining the upstream DavB/DavA steps that generate DavT's substrate and demonstrating convergence on glutarate. Basis for **Findings 3 and 4**. |
| [31064836](https://pubmed.ncbi.nlm.nih.gov/31064836/) | *Massively Parallel Fitness Profiling Reveals Multiple Novel Enzymes* (Thompson et al., 2019) | Genome-wide RB-TnSeq fitness profiling confirming and extending the lysine → aminovalerate → glutarate → central-metabolism route. Basis for **Finding 4**. |
| [25012259](https://pubmed.ncbi.nlm.nih.gov/25012259/) | *Enzymatic production of 5-aminovalerate from L-lysine* (2014) | Confirms DavB and DavA convert L-lysine to 5-aminovalerate (DavT's substrate) and describes the aminovalerate pathway of *P. putida*. Context for the upstream steps. |
| [27717386](https://pubmed.ncbi.nlm.nih.gov/27717386/) | *Metabolic engineering of C. glutamicum for enhanced 5-aminovaleric acid production* (2016) | Reinforces the roles of DavB (lysine 2-monooxygenase) and DavA (δ-aminovaleramidase) upstream of DavT, and shows glutarate as a downstream byproduct — consistent with the DavT/DavD → glutarate route. |

The convergence of these independent lines of evidence — a targeted metabolic-engineering reconstitution (30144560), promoter/operon genetics (15150230), stable-isotope tracing (16237033), and genome-scale fitness profiling (31064836) — gives high confidence in DavT's identity and pathway placement. No retrieved study contradicts the annotation. The class-III PLP domain architecture (UniProt Q88RB9) independently supports the enzymatic mechanism.

---

## Limitations and Knowledge Gaps

1. **No direct structural or kinetic characterization of *P. putida* DavT.** Searches returned no crystal structure and no purified-enzyme kinetic study specific to Q88RB9. The homodimeric fold-type-I assembly, the ping-pong bi-bi mechanism, the identity of the catalytic PLP-binding lysine, and the quantitative substrate specificity (Km/kcat for 5-aminovalerate vs. related ω-amino acids) are all **inferred from family membership**, not measured. This is the single largest gap.

2. **Substrate promiscuity is uncharacterized.** Class-III aminotransferases (e.g., GABA-AT, ornithine-AT) often accept multiple ω-amino-acid substrates. Whether DavT can also transaminate GABA, 4-aminobutyrate, putrescine-derived intermediates, or longer/shorter ω-amino acids has not been directly tested for the *P. putida* enzyme. The observed cross-reactivity of a *C. glutamicum* GabT with this chemistry (PMID 27717386) hints at overlap but does not resolve DavT's own specificity spectrum.

3. **Cofactor preference of the downstream step is not pinned down here.** DavD is annotated as a glutarate semialdehyde dehydrogenase, but whether it uses NAD⁺ or NADP⁺ in vivo — which affects the redox accounting of the pathway — was not established in the retrieved literature and is tangential to DavT itself.

4. **Reliance on annotation transfer for EC and localization.** The EC number (2.6.1.48) and cytoplasmic localization rest on sequence-based annotation plus pathway logic rather than a biochemical assay of the isolated protein. This is standard and well-supported here, but remains inference.

5. **Directionality and physiological reversibility** of the transamination in vivo (5-aminovalerate → semialdehyde vs. the reverse) were not experimentally quantified for DavT.

---

## Proposed Follow-up Experiments / Actions

1. **Purify and kinetically characterize recombinant DavT.** Express Q88RB9 with an affinity tag in *E. coli*, purify, and measure steady-state kinetics (Km, kcat, kcat/Km) for 5-aminovalerate with 2-oxoglutarate as acceptor. Confirm PLP dependence spectroscopically (420 nm internal aldimine) and by apoenzyme reconstitution.

2. **Map substrate specificity.** Assay DavT against a panel of ω-amino acids (GABA, 4-aminobutyrate, 6-aminohexanoate, putrescine, ornithine) and alternative amino acceptors (pyruvate, oxaloacetate) to define the specificity profile and test for promiscuity relevant to metabolic engineering.

3. **Solve the structure.** Determine a crystal or cryo-EM structure (or a high-confidence AlphaFold model validated against family templates) to identify the catalytic PLP-binding lysine, the substrate-binding pocket residues conferring C5 ω-amino-acid selectivity, and the dimer interface.

4. **Confirm localization directly.** Use fluorescent-fusion or fractionation/proteomics to verify cytoplasmic localization experimentally rather than by inference.

5. **Test in-vivo reversibility and flux.** Use ¹³C/¹⁵N tracing in *P. putida* under defined nitrogen conditions to quantify net flux through DavT and the fate of the transferred amino group (regenerated glutamate), and to determine how DavT flux partitions between the aminovalerate and aminoadipate routes.

6. **Engineering-oriented mutagenesis.** Rational active-site mutagenesis to improve kcat/Km or broaden/narrow specificity, supporting the use of DavT in bioproduction of glutarate, valerolactam, and 1,5-pentanediol precursors — the applied context in which this enzyme is most exploited (PMIDs 30144560, 25012259, 27717386).

---

## Conclusion

DavT (PP_0214, Q88RB9) is the **5-aminovalerate:2-oxoglutarate aminotransferase (EC 2.6.1.48)** of *Pseudomonas putida* KT2440 — a cytoplasmic, PLP-dependent class-III aminotransferase that transaminates 5-aminovalerate to glutarate-5-semialdehyde (with L-glutamate as co-product) as the penultimate step of the aminovalerate branch of L-lysine catabolism. Encoded in the substrate-inducible davDT operon, it is functionally coupled to DavD, whose oxidation of the semialdehyde yields glutarate, the convergence node channeling lysine-derived carbon and nitrogen into central metabolism. The identification is robust and mutually consistent across metabolic-engineering, genetic, isotope-tracing, and genome-scale fitness studies; the outstanding need is a direct structural and kinetic characterization of the enzyme itself.


## Artifacts

- [OpenScientist final report](davT-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](davT-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:30144560
2. PMID:15150230
3. PMID:16237033
4. PMID:31064836