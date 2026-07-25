---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-17T16:15:20.929145'
end_time: '2026-07-17T16:43:11.531099'
duration_seconds: 1670.6
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: argD
  gene_symbol: argD
  uniprot_accession: P59319
  protein_description: 'RecName: Full=Acetylornithine aminotransferase {ECO:0000255|HAMAP-Rule:MF_01107};
    Short=ACOAT {ECO:0000255|HAMAP-Rule:MF_01107}; EC=2.6.1.11 {ECO:0000255|HAMAP-Rule:MF_01107};'
  gene_info: Name=argD {ECO:0000255|HAMAP-Rule:MF_01107}; OrderedLocusNames=PP_4481;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the class-III pyridoxal-phosphate-dependent
  protein_domains: Ac/SucOrn_transaminase_bac. (IPR017652); AcOrn/SuccOrn_fam. (IPR004636);
    Aminotrans_3. (IPR005814); Aminotrans_3_PPA_site. (IPR049704); Class-III_PLP-dep_AT.
    (IPR050103)
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
  path: argD-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: argD-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** P59319
- **Protein Description:** RecName: Full=Acetylornithine aminotransferase {ECO:0000255|HAMAP-Rule:MF_01107}; Short=ACOAT {ECO:0000255|HAMAP-Rule:MF_01107}; EC=2.6.1.11 {ECO:0000255|HAMAP-Rule:MF_01107};
- **Gene Information:** Name=argD {ECO:0000255|HAMAP-Rule:MF_01107}; OrderedLocusNames=PP_4481;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the class-III pyridoxal-phosphate-dependent
- **Key Domains:** Ac/SucOrn_transaminase_bac. (IPR017652); AcOrn/SuccOrn_fam. (IPR004636); Aminotrans_3. (IPR005814); Aminotrans_3_PPA_site. (IPR049704); Class-III_PLP-dep_AT. (IPR050103)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "argD" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'argD' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **argD** (gene ID: argD, UniProt: P59319) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *argD* / PP_4481 (UniProt P59319) in *Pseudomonas putida* KT2440

## Summary

The gene annotated **argD** (locus **PP_4481**, UniProt **P59319**) in *Pseudomonas putida* KT2440 encodes a **cytoplasmic, homodimeric, pyridoxal-5′-phosphate (PLP)-dependent class-III aminotransferase** of the acyl-ornithine aminotransferase family. Its molecular function is that of an **acyl-ornithine:2-oxoglutarate aminotransferase** — it removes the amino group from the side-chain (δ) carbon of an N-acylated ornithine and transfers it to 2-oxoglutarate, generating an N-acylglutamate-5-semialdehyde and L-glutamate. This is a reversible, PLP-Schiff-base–dependent transamination characteristic of the class-III PLP-dependent aminotransferase fold.

There is an important **annotation conflict** that this investigation resolved. UniProt, via the automated HAMAP rule MF_01107, names P59319 the **biosynthetic acetylornithine aminotransferase (ArgD/ACOAT, EC 2.6.1.11)**, the enzyme that catalyzes the fourth (transamination) step of L-arginine biosynthesis. However, three independent lines of evidence — (i) genomic synteny placing PP_4481 inside the **arginine succinyltransferase (AST) catabolic operon** (PP_4478–PP_4481), (ii) KEGG orthology assignment (K00840, EC 2.6.1.81, *astC*), and (iii) **~80 % pairwise sequence identity to the experimentally characterized *P. aeruginosa* AruC** — converge on the conclusion that the **primary physiological role of PP_4481 is catabolic**: it is the **N²-succinyl-L-ornithine 5-aminotransferase (AstC/AruC, EC 2.6.1.81)**, catalyzing the third step of the aerobic pathway that degrades arginine and ornithine to glutamate for use as carbon and nitrogen sources. The dedicated **biosynthetic** ACOAT step in *P. putida* is instead attributable to a distinct paralog, **PP_0372** (UniProt Q88QW2), and the pathway operates through the *argJ* (PP_1346) acetyl-recycling route.

Because catabolic AstC-type and anabolic ArgD-type enzymes are only ~58–60 % identical yet have been shown to be **functionally interchangeable** and mutually promiscuous toward both N-acetyl- and N-succinyl-ornithine, PP_4481 most likely retains measurable activity on acetylornithine as well. Nonetheless, the weight of genomic, phylogenetic, and structural evidence assigns its **primary cellular function to arginine/ornithine catabolism via the AST pathway**, not to arginine biosynthesis. The enzyme acts in the **cytoplasm** and prefers **N-acylated ornithine over free ornithine**, a specificity that arises from steric and desolvation effects at the active site.

---

## Key Findings

### Finding 1 — Molecular identity: a class-III PLP-dependent acyl-ornithine aminotransferase

UniProt P59319 describes a 406-residue class-III PLP-dependent aminotransferase of the ArgD/acetylornithine-aminotransferase subfamily. The canonical annotated reaction (EC 2.6.1.11) is the reversible transamination:

> N²-acetyl-L-ornithine + 2-oxoglutarate ⇌ N-acetyl-L-glutamate 5-semialdehyde + L-glutamate

with **pyridoxal 5′-phosphate (PLP)** as the essential cofactor, covalently bound as an internal aldimine (Schiff base) to the active-site lysine (mapped to **Lys255** in P59319). Substrate- and cofactor-binding residues are annotated at positions 108, 141, 144, 226, 283 and 284, all consistent with the conserved class-III active site. The core aminotransferase chemistry — abstraction of the substrate α/δ-amino group via a PLP ketimine/quinonoid intermediate and its transfer to 2-oxoglutarate — is deeply conserved across bacteria including *E. coli*, *M. tuberculosis*, *Erwinia*, *Corynebacterium* and cyanobacteria.

The biosynthetic ArgD reaction was confirmed verbatim in the literature: ArgD "*catalyzes the reversible conversion of N-acetylornithine and 2 oxoglutarate into glutamate-5-semialdehyde and L-glutamate*" ([PMID: 34922100](https://pubmed.ncbi.nlm.nih.gov/34922100/)), and N-acetylornithine aminotransferase "*(EC 2.6.1.11, ACOAT) catalyzes the conversion of N-acetylglutamic semialdehyde to N-acetylornithine, the forth step involved in the L-arginine biosynthetic pathways*" ([PMID: 22016985](https://pubmed.ncbi.nlm.nih.gov/22016985/)). These establish the **enzyme class and chemistry**; the subsequent findings establish which *physiological* reaction PP_4481 performs.

### Finding 2 — Subcellular localization and quaternary structure

P59319 is annotated (HAMAP MF_01107) as a **cytoplasmic, homodimeric** enzyme with PLP covalently bound via a Schiff base to Lys255. This is fully consistent with the class-III PLP aminotransferase fold, which functions as an obligate dimer with the active site formed at the subunit interface. The physiological role is therefore carried out **inside the cell**, in the cytoplasm, where the arginine/ornithine catabolic and biosynthetic intermediates reside.

The essentiality of *argD*-type activity for a functional arginine pathway is well demonstrated in related bacteria: in *Erwinia amylovora*, an *argD* transposon-insertion mutant "*was an arginine auxotroph that did not cause fire blight in apple and had reduced virulence in immature pear fruits*," and the *argD* gene "*encodes a predicted N-acetylornithine aminotransferase enzyme, which is involved in the production of the amino acid arginine*" ([PMID: 25172854](https://pubmed.ncbi.nlm.nih.gov/25172854/)). Note that this evidence pertains to the *biosynthetic* role of ArgD in *Erwinia*; for *P. putida* PP_4481 specifically, the localization (cytoplasm) and fold (homodimeric PLP enzyme) hold, but the physiological pathway is catabolic (see Findings 4–8).

### Finding 3 — Dual biosynthetic capability of the ArgD/ACOAT family (substrate promiscuity)

A key feature of this enzyme family, directly relevant to interpreting PP_4481's substrate specificity, is **catalytic promiscuity**. Purified *E. coli* ArgD exhibits both N-acetylornithine aminotransferase and **N-succinyl-L,L-diaminopimelate aminotransferase (DapC/SDAP-AT)** activities with *similar specificity constants*: the enzyme "*exhibits both NAcOATase and DapATase activity, with similar specificity constants for N-acetylornithine and N-succinyl-L,L-DAP, suggesting that it can function in both lysine and arginine biosynthesis*" ([PMID: 10074354](https://pubmed.ncbi.nlm.nih.gov/10074354/)). Genetic dissection in *E. coli* further showed extensive aminotransferase redundancy: "*The enzymes with N-acetylornithine aminotransferase (ACOAT) activity in arginine synthesis were ArgD, AstC, GabT and PuuE; the major anaerobic ACOAT was ArgD*" ([PMID: 25243376](https://pubmed.ncbi.nlm.nih.gov/25243376/)). This demonstrates that members of this family — including the catabolic AstC — routinely accept multiple acylated amino-acid substrates. This promiscuity is the root cause of the cross-annotation between *argD* and *astC*.

### Finding 4 — Genomic synteny places PP_4481 in the AST catabolic operon

The decisive contextual evidence is genomic. PP_4481 sits within a tight, co-oriented **arginine succinyltransferase (AST) catabolic operon** on the *P. putida* KT2440 chromosome:

| Locus | Gene | Enzyme | Role in AST pathway |
|-------|------|--------|---------------------|
| PP_4478 | *astD* | N-succinylglutamate-5-semialdehyde dehydrogenase | Step 4 |
| PP_4479 | *astA-I* (aruAI) | arginine/ornithine N-succinyltransferase subunit | Step 1 |
| PP_4480 | *astA-II* (aruAII) | arginine/ornithine N-succinyltransferase subunit | Step 1 |
| **PP_4481** | **astC (this gene)** | **succinylornithine aminotransferase** | **Step 3** |

KEGG annotates PP_4481 as *astC*, **K00840, EC 2.6.1.81**, within module **M00879 "Arginine succinyltransferase pathway, arginine ⇒ glutamate."** This arrangement mirrors the *P. aeruginosa* PAO1 *aru* cluster, in which "*The arginine succinyltransferase (AST) pathway is the major arginine and ornithine utilization (aru) pathway under aerobic conditions in Pseudomonas aeruginosa*" and the cluster encodes "*N2-succinylornithine 5-aminotransferase, N-succinylglutamate 5-semialdehyde dehydrogenase, N2-succinylarginine dihydrolase, and N-succinylglutamate desuccinylase*" ([PMID: 9393691](https://pubmed.ncbi.nlm.nih.gov/9393691/)). The neighboring genes of PP_4481 correspond precisely to these AST enzymes, strongly indicating that PP_4481 is the operon's **succinylornithine aminotransferase (AruC/AstC)**, a catabolic enzyme.

### Finding 5 — Resolution of the UniProt-vs-KEGG annotation conflict via a distinct biosynthetic paralog

*P. putida* KT2440 encodes at least **two paralogous class-III acyl-ornithine aminotransferases**, and the KEGG orthology cleanly separates their roles:

- **K00821** (biosynthetic acetylornithine aminotransferase, *argD*, EC 2.6.1.11) → **PP_0372** (*aruC*/"Acetylornithine aminotransferase 2", UniProt Q88QW2)
- **K00840** (catabolic succinylornithine aminotransferase, *astC*, EC 2.6.1.81) → **PP_4481** (this gene, UniProt P59319)

UniProt's HAMAP rule MF_01107 applied the biosynthetic ArgD/ACOAT name to P59319 by sequence signature, but the genomic synteny and KEGG orthology assign it the catabolic AstC role. Because AstC also possesses ACOAT activity ("*The enzymes with N-acetylornithine aminotransferase (ACOAT) activity in arginine synthesis were ArgD, AstC, GabT and PuuE*", [PMID: 25243376](https://pubmed.ncbi.nlm.nih.gov/25243376/)), the two *P. putida* paralogs likely overlap partially in substrate specificity (acetyl- vs succinyl-ornithine), explaining why an automated rule could not distinguish them. The physiologically dedicated **biosynthetic** step is carried by PP_0372.

### Finding 6 — Phylogeny: PP_4481 is the ortholog of *P. aeruginosa* AruC

A pairwise sequence analysis (Needleman-Wunsch global alignment of UniProt sequences) quantitatively confirms the orthology:

| Comparison | % Identity | Interpretation |
|------------|-----------|----------------|
| PP_4481 vs *P. aeruginosa* AruC (O30508, catabolic N²-succinylornithine 5-aminotransferase) | **79.8 %** | Highest — direct ortholog |
| PP_4481 vs *E. coli* ArgD (P18335, anabolic ACOAT) | 65.6 % | More distant |
| PP_4481 vs *E. coli* AstC (P77581, catabolic) | 62.6 % | More distant |
| PP_4481 vs *E. coli* GabT (P22256, GABA-AT outgroup) | 35.8 % | Outgroup |
| *E. coli* ArgD vs *E. coli* AstC | 59.2 % | Close paralogs, interchangeable |
| PP_0372 (Q88QW2, biosynthetic-argD paralog) vs all four references | ~38–40 % | Divergent outlier |

The **79.8 % identity to *P. aeruginosa* AruC** — an experimentally characterized AST-pathway succinylornithine aminotransferase — is the single strongest quantitative argument that PP_4481 performs the same catabolic function. AruC is annotated "Succinylornithine transaminase/acetylornithine aminotransferase" and was characterized by Itoh (1997) as the AST-pathway succinylornithine aminotransferase ([PMID: 9393691](https://pubmed.ncbi.nlm.nih.gov/9393691/)). Notably, PP_0372 (the KEGG-designated biosynthetic paralog) is a divergent outlier at only ~38–40 % identity to all references, confirming it is a *separate* functional class.

### Finding 7 — Position and function within the AST catabolic pathway

PP_4481/AruC catalyzes the **third (transamination) step** of the arginine succinyltransferase pathway, which degrades L-arginine to glutamate through N-succinylated intermediates:

```
              AruAI/AII (AST)      AruB              AruC (PP_4481)            AruD              AruE
 L-arginine ───────────────▶ N2-succinyl- ─────▶ N2-succinyl- ──────────▶ N2-succinyl- ─────▶ N2-succinyl- ─────▶ L-glutamate
  + succinyl-CoA              arginine     (dihydrolase) ornithine  (aminotransferase) glutamate     (dehydrog.) glutamate  (desuccinylase) + succinate
                                                                    + 2-oxoglutarate   5-semialdehyde
                                                                    → + L-glutamate
```

This sequence — "*L-arginine→N2-succinylarginine→N2-succinylornithine→N2-succinylglutamate semialdehyde→N2-succinylglutamate→glutamate + succinate*" — was established in *Pseudomonas cepacia* ([PMID: 2865249](https://pubmed.ncbi.nlm.nih.gov/2865249/)). The pathway allows arginine to serve as **sole carbon and nitrogen source**, and its enzymes are regulated: "*The formation of the enzymes responsible for arginine degradation is regulated not only by induction but also by both carbon and nitrogen catabolite repression*" ([PMID: 2865249](https://pubmed.ncbi.nlm.nih.gov/2865249/)). In *P. aeruginosa*, "*The aruCFGDB genes appear to form an operon transcribed from a promoter upstream of aruC*" ([PMID: 9393691](https://pubmed.ncbi.nlm.nih.gov/9393691/)), placing the *aruC* ortholog at the head of an ArgR-controlled catabolic operon. PP_4481 therefore performs the transamination that transfers the amino group from **N²-succinyl-L-ornithine** to **2-oxoglutarate**, yielding **N²-succinylglutamate-5-semialdehyde + L-glutamate**.

### Finding 8 — Structural basis of substrate specificity: preference for acylated ornithine

The catabolic AstC-type enzyme's substrate preference has been defined crystallographically. X-ray structures of *E. coli* AstC were solved in apo, holo-PLP, and **N-succinylornithine-bound** forms ([PMID: 23484010](https://pubmed.ncbi.nlm.nih.gov/23484010/)). That work established the anabolic/catabolic dichotomy directly: "*Escherichia coli possesses two acyl ornithine aminotransferases, one catabolic (AstC) and the other anabolic (ArgD), that participate in L-arginine metabolism. Although only 58% identical, the enzymes have been shown to be functionally interchangeable*" ([PMID: 23484010](https://pubmed.ncbi.nlm.nih.gov/23484010/)). Docking of ornithine, succinylornithine and acetylornithine showed that "*AstC has a strong preference for acylated ornithine species over ornithine itself, and suggest that the increase in specificity associated with acylation is caused by steric and desolvation effects*" ([PMID: 23484010](https://pubmed.ncbi.nlm.nih.gov/23484010/)) — i.e., the enzyme discriminates against free ornithine not through specific acyl-group contacts but through general steric/desolvation penalties.

For PP_4481, UniProt maps the PLP Schiff-base to **Lys255** and cofactor/substrate-binding residues to positions 108, 141, 144, 226, 283 and 284, consistent with this conserved class-III active site. The fold matches the *Salmonella typhimurium* ArgD structure. Thus PP_4481 is expected to bind and turn over **N-acyl-ornithine (succinyl- and, more weakly, acetyl-)** far more efficiently than free ornithine.

### Finding 9 — Separation of biosynthetic machinery confirms PP_4481's catabolic role

The biosynthetic arginine genes of *P. putida* KT2440 map to distinct loci, none coinciding with the AST operon:

| Step | Gene | Locus |
|------|------|-------|
| N-acetylglutamate kinase | *argB* | PP_5289 |
| N-acetyl-γ-glutamyl-phosphate reductase | *argC* | PP_0432 (and PP_3633) |
| Ornithine acetyltransferase / NAGS | *argJ* | PP_1346 |
| **Biosynthetic acetylornithine aminotransferase (K00821)** | *argD* | **PP_0372** |
| Acetylornithine deacetylase candidates | *argE* | PP_3571 / PP_5186 |

The presence of *argJ* (PP_1346) indicates KT2440 uses the **cyclic/acetyl-recycling ornithine biosynthesis route**, in which the biosynthetic acetylornithine aminotransferase (assigned to PP_0372) supplies the transamination step. None of these biosynthetic loci coincide with PP_4481, which is embedded in the catabolic AST operon (PP_4478–4481). This spatial and functional separation reinforces that **biosynthesis and catabolism use different enzymes**, with PP_4481 dedicated to catabolism.

---

## Mechanistic Model / Interpretation

The evidence integrates into a coherent model in which *P. putida* KT2440 maintains **two parallel acyl-ornithine aminotransferase systems** built on the same class-III PLP fold but committed to opposite metabolic directions:

```
                   ARGININE BIOSYNTHESIS (anabolic)
  L-glutamate → N-acetylglutamate → ... → N-acetylglutamate-5-semialdehyde
                                                  │
                                   PP_0372 (ArgD/ACOAT, K00821, EC 2.6.1.11)
                                                  │  ← 2-oxoglutarate / L-glutamate
                                                  ▼
                                        N-acetyl-L-ornithine → (argJ recycle) → L-ornithine → L-arginine


                   ARGININE CATABOLISM (catabolic AST pathway)
  L-arginine → N2-succinylarginine → N2-succinylornithine
                                            │
                         PP_4481 (AstC/AruC, K00840, EC 2.6.1.81)   ← THIS GENE
                                            │  ← 2-oxoglutarate / → L-glutamate
                                            ▼
                                N2-succinylglutamate-5-semialdehyde → ... → L-glutamate + succinate
```

Both enzymes catalyze the same *type* of reaction — transamination between the δ-carbon of an N-acyl-ornithine and 2-oxoglutarate — but on **different acyl groups** (acetyl for biosynthesis, succinyl for catabolism) and in **different physiological directions**. Because the class-III active site tolerates both acyl groups, the enzymes are biochemically promiscuous and, in *E. coli*, functionally interchangeable. The specialization is therefore primarily one of **regulation and metabolic context** (which operon, which inducers, which flux) rather than absolute substrate exclusivity.

For PP_4481 specifically, the primary annotation should be understood as follows:

- **Molecular function:** N²-succinyl-L-ornithine:2-oxoglutarate 5-aminotransferase (EC 2.6.1.81), PLP-dependent, class-III fold; likely retains secondary acetylornithine aminotransferase activity (EC 2.6.1.11).
- **Biological process:** aerobic **arginine and ornithine catabolism** via the arginine succinyltransferase (AST) pathway, yielding glutamate + succinate as carbon/nitrogen sources.
- **Localization:** cytoplasm; homodimeric holoenzyme with PLP bound at Lys255.
- **Pathway position:** step 3 of 5 in the AST pathway; product feeds AstD (PP_4478).
- **Regulation:** inducible by arginine, subject to carbon and nitrogen catabolite repression, and (by orthology to *P. aeruginosa aruCFGDB*) controlled by the ArgR regulator.

The **UniProt/HAMAP "argD/ACOAT biosynthetic" name is a mis-specialization** driven by sequence-signature promiscuity; the primary physiological role indicated by genomic context, orthology, and pathway membership is **catabolic AstC/AruC**.

---

## Evidence Base

| PMID | Title (abbreviated) | How it supports the findings |
|------|--------------------|------------------------------|
| [9393691](https://pubmed.ncbi.nlm.nih.gov/9393691/) | *Cloning of the aru genes of the catabolic AST pathway in P. aeruginosa* | Defines *aruC* (79.8 %-identity ortholog of PP_4481) as the AST-pathway succinylornithine aminotransferase; establishes AST as the major aerobic arginine/ornithine utilization route; *aruCFGDB* operon organization. **Central supporting paper.** |
| [2865249](https://pubmed.ncbi.nlm.nih.gov/2865249/) | *Succinyl derivatives in arginine catabolism in P. cepacia* | Defines the full AST reaction sequence and the exact substrate/product of the AruC step; documents inducible, catabolite-repressed regulation. |
| [23484010](https://pubmed.ncbi.nlm.nih.gov/23484010/) | *Structure of catabolic N-succinylornithine transaminase (AstC) from E. coli* | Crystallographic basis for catabolic-vs-anabolic distinction; AstC/ArgD only 58 % identical yet interchangeable; AstC strongly prefers acylated ornithine (steric/desolvation). |
| [10074354](https://pubmed.ncbi.nlm.nih.gov/10074354/) | *Dual biosynthetic capability of N-acetylornithine aminotransferase* | Direct enzymology: ArgD has both ACOAT and succinyl-DAP-AT activity with similar specificity constants — establishes family promiscuity. |
| [25243376](https://pubmed.ncbi.nlm.nih.gov/25243376/) | *Redundant aminotransferases in lysine/arginine synthesis in E. coli* | Documents that AstC also has ACOAT activity and quantifies aminotransferase redundancy — explains argD/astC cross-annotation. |
| [34922100](https://pubmed.ncbi.nlm.nih.gov/34922100/) | *ArgD of M. tuberculosis is a functional ACOAT* | States the exact reversible ArgD transamination reaction (family chemistry). |
| [22016985](https://pubmed.ncbi.nlm.nih.gov/22016985/) | *N-acetylornithine aminotransferase from C. crenatum* | Confirms EC 2.6.1.11 and the fourth-step biosynthetic role of ACOAT. |
| [25172854](https://pubmed.ncbi.nlm.nih.gov/25172854/) | *argD mutation causes arginine auxotrophy in E. amylovora* | Genetic evidence that ArgD-type activity is required for arginine biosynthesis (biosynthetic-role context). |

Supporting context papers on *P. putida* arginine physiology — including the role of arginine as a metabolic signal ([PMID: 38429473](https://pubmed.ncbi.nlm.nih.gov/38429473/)), arginine biosynthesis modulating pyoverdine and oxidative-stress adaptation ([PMID: 31451546](https://pubmed.ncbi.nlm.nih.gov/31451546/)), and c-di-GMP/biofilm links ([PMID: 27489550](https://pubmed.ncbi.nlm.nih.gov/27489550/)) — confirm that arginine metabolism is physiologically prominent in KT2440 but do not directly assay PP_4481.

---

## Limitations and Knowledge Gaps

1. **No direct enzymatic characterization of PP_4481 itself.** The functional assignment rests on orthology (79.8 % identity to *P. aeruginosa* AruC), genomic synteny, and KEGG orthology — not on a purified-enzyme kinetic study of the *P. putida* KT2440 protein. Kinetic constants (kcat, Km for succinyl- vs acetyl-ornithine) have not been measured for this specific protein.
2. **Annotation conflict remains formally unresolved at the database level.** UniProt (HAMAP MF_01107) still names P59319 the biosynthetic ArgD/ACOAT. This report argues, on strong indirect evidence, that the primary role is catabolic AstC — but the two functions are biochemically overlapping, so the enzyme may contribute to both pathways to differing degrees.
3. **The biosynthetic-paralog assignment (PP_0372) is likewise inferential**, based on KEGG KO mapping and sequence divergence, not on a KT2440 knockout/complementation study.
4. **Regulatory details are extrapolated from *P. aeruginosa*.** ArgR control and catabolite repression of the *P. putida* PP_4478–4481 operon are inferred from orthology and from *P. cepacia*/*P. aeruginosa* studies, not directly demonstrated in KT2440.
5. **No structure of the KT2440 protein exists;** active-site residues (Lys255 etc.) are from UniProt feature mapping and homology to *S. typhimurium* ArgD / *E. coli* AstC.

---

## Proposed Follow-up Experiments / Actions

1. **Direct enzyme kinetics.** Heterologously express and purify PP_4481 (P59319) and measure steady-state kinetics with **N²-succinyl-L-ornithine** vs **N²-acetyl-L-ornithine** (and free ornithine) using 2-oxoglutarate as the amino acceptor. Compare kcat/Km to test the predicted succinyl-preference and quantify promiscuity.
2. **Genetic dissection.** Construct single (ΔPP_4481, ΔPP_0372) and double deletion mutants in KT2440. Test (a) growth on **L-arginine or L-ornithine as sole carbon/nitrogen source** (predicting ΔPP_4481 is impaired) and (b) **arginine auxotrophy** (predicting ΔPP_0372, not ΔPP_4481, causes auxotrophy). Cross-complementation would test functional interchangeability.
3. **Operon/regulation mapping.** Verify the PP_4478–4481 transcript by RT-PCR/RNA-seq, map the promoter, and test **ArgR dependence** and **carbon/nitrogen catabolite repression** by growth-condition-dependent expression assays.
4. **Structural confirmation.** Solve the crystal structure of PP_4481, ideally with N-succinylornithine bound, to confirm the active-site geometry and the steric/desolvation basis of acyl-ornithine preference.
5. **Database curation.** Submit a curation note to UniProt/KEGG reconciling the *argD* (biosynthetic) vs *astC* (catabolic) assignment for PP_4481, flagging PP_0372 as the biosynthetic ACOAT paralog.

---

## Conclusion

PP_4481 (UniProt P59319) in *Pseudomonas putida* KT2440 is a cytoplasmic, homodimeric, PLP-dependent class-III acyl-ornithine aminotransferase whose **primary physiological function is catabolic**: it is the **N²-succinyl-L-ornithine 5-aminotransferase (AstC/AruC, EC 2.6.1.81)** that catalyzes the third step of the aerobic arginine succinyltransferase (AST) pathway, degrading arginine/ornithine to glutamate + succinate for use as carbon and nitrogen sources. Despite the UniProt/HAMAP "biosynthetic argD/ACOAT" name, genomic synteny within the AST operon, KEGG orthology, and ~80 % identity to characterized *P. aeruginosa* AruC establish the catabolic assignment, with the dedicated biosynthetic ACOAT role attributable to the distinct paralog PP_0372. The enzyme prefers N-acylated ornithine over free ornithine and is expected to retain secondary acetylornithine aminotransferase activity, reflecting the well-documented promiscuity of this enzyme family.


## Artifacts

- [OpenScientist final report](argD-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](argD-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:34922100
2. PMID:22016985
3. PMID:25172854
4. PMID:10074354
5. PMID:25243376
6. PMID:9393691
7. PMID:2865249
8. PMID:23484010
9. PMID:38429473
10. PMID:31451546
11. PMID:27489550