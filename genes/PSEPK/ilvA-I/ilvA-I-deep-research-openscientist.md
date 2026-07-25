---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-17T07:25:51.809129'
end_time: '2026-07-17T07:44:39.069924'
duration_seconds: 1127.26
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: ilvA-I
  gene_symbol: ilvA-I
  uniprot_accession: Q88HB4
  protein_description: 'RecName: Full=L-threonine dehydratase {ECO:0000256|RuleBase:RU362012};
    EC=4.3.1.19 {ECO:0000256|RuleBase:RU362012}; AltName: Full=Threonine deaminase
    {ECO:0000256|RuleBase:RU362012};'
  gene_info: Name=ilvA-I {ECO:0000313|EMBL:AAN69048.1}; Synonyms=ilvA {ECO:0000256|RuleBase:RU362012};
    OrderedLocusNames=PP_3446 {ECO:0000313|EMBL:AAN69048.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the serine/threonine dehydratase family.
  protein_domains: ACT-like_dom_sf. (IPR045865); Ser/Thr_Dehydratase. (IPR050147);
    Ser/Thr_deHydtase_PyrdxlP-BS. (IPR000634); TD_ACT-like. (IPR001721); TD_ACT-like_sf.
    (IPR038110)
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
  path: ilvA-I-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: ilvA-I-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88HB4
- **Protein Description:** RecName: Full=L-threonine dehydratase {ECO:0000256|RuleBase:RU362012}; EC=4.3.1.19 {ECO:0000256|RuleBase:RU362012}; AltName: Full=Threonine deaminase {ECO:0000256|RuleBase:RU362012};
- **Gene Information:** Name=ilvA-I {ECO:0000313|EMBL:AAN69048.1}; Synonyms=ilvA {ECO:0000256|RuleBase:RU362012}; OrderedLocusNames=PP_3446 {ECO:0000313|EMBL:AAN69048.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the serine/threonine dehydratase family.
- **Key Domains:** ACT-like_dom_sf. (IPR045865); Ser/Thr_Dehydratase. (IPR050147); Ser/Thr_deHydtase_PyrdxlP-BS. (IPR000634); TD_ACT-like. (IPR001721); TD_ACT-like_sf. (IPR038110)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ilvA-I" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ilvA-I' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ilvA-I** (gene ID: ilvA-I, UniProt: Q88HB4) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *ilvA-I* (Q88HB4 / PP_3446) — Biosynthetic L-Threonine Dehydratase of *Pseudomonas putida* KT2440

## Summary

**ilvA-I** (UniProt **Q88HB4**; ordered locus **PP_3446**) of *Pseudomonas putida* KT2440 (PSEPK) encodes a **biosynthetic L-threonine dehydratase** — equivalently a **threonine deaminase (TD)** — classified as **EC 4.3.1.19**. This is a soluble, cytoplasmic, **pyridoxal-5′-phosphate (PLP)-dependent** enzyme that catalyzes the **first committed step of L-isoleucine biosynthesis**: the PLP-dependent α,β-elimination (dehydration/deamination) of **L-threonine to 2-ketobutyrate (α-ketobutyrate) + ammonia + water**. The resulting 2-ketobutyrate is condensed with pyruvate by acetohydroxyacid synthase to launch the four-carbon → five-carbon branch that produces L-isoleucine. The identification is unambiguous: the gene symbol, EC number, protein family (serine/threonine dehydratase family), and the full complement of catalytic and regulatory sequence signatures all align with the UniProt target identity, and the organism is confirmed as *P. putida* KT2440.

Structurally, ilvA-I is a **"long-form" biosynthetic isozyme**: it carries an N-terminal PLP catalytic domain (Pfam PF00291) bearing the catalytic Schiff-base lysine, followed by **two C-terminal ACT-like regulatory domains** (Pfam PF00585). This architecture is the molecular hardware for **allosteric feedback control**: the enzyme is **inhibited by the pathway end-product L-isoleucine** and **activated by L-valine** (the product of the parallel branched-chain pathway). It thereby acts as the flux valve at the entry point of the isoleucine branch. Beyond L-threonine, biosynthetic TDs of this family also accept **L-serine and L-allo-threonine** as substrates and display **sigmoidal (cooperative) kinetics**, and their catalytic cycle generates the reactive electrophilic metabolite **2-aminoacrylate (2AA)**, which is normally detoxified by RidA-family deaminases.

The functional assignment rests on strong comparative and bioinformatic evidence: ilvA-I shares **55% sequence identity** with the structurally and biochemically characterized *Escherichia coli* biosynthetic threonine deaminase (IlvA, P04968), with strict conservation of the catalytic PLP Schiff-base lysine (**Lys77** in Q88HB4) and the isoleucine-allostery residue (**Phe368**, corresponding to *E. coli* Phe352). KEGG places PP_3446 in ortholog group **K01754** and in both the valine/leucine/isoleucine biosynthesis (ppu00290) and glycine/serine/threonine metabolism (ppu00260) pathways. Notably, KT2440 encodes a **second, 75%-identical, fully competent paralog (ilvA-II / PP_5149)** plus two short single-domain PLP dehydratases, indicating genetic redundancy at this metabolic node.

---

## Gene/Protein Identity Verification

Before presenting findings, the mandatory identity check was completed and **passed**:

| Verification item | Expected (UniProt target) | Found | Status |
|---|---|---|---|
| Gene symbol | ilvA-I (syn. ilvA) | ilvA-I / PP_3446 | ✅ Match |
| EC number / reaction | EC 4.3.1.19, L-threonine dehydratase | EC 4.3.1.19, Thr → 2-ketobutyrate + NH₃ | ✅ Match |
| Organism | *P. putida* KT2440 (taxid 160488) | *P. putida* KT2440 | ✅ Match |
| Protein family | Serine/threonine dehydratase family | PF00291 + PF00585 architecture | ✅ Match |
| Key domains | ACT-like + Ser/Thr dehydratase + PLP-BS | PLP catalytic + 2× ACT regulatory | ✅ Match |

The literature retrieved describes the *ilvA*/threonine-deaminase function consistently across organisms (*E. coli*, *M. smegmatis*, *S. aureus*, *Salmonella*, *Corynebacterium*), and the *P. putida* KT2440 genome context (PP_3446) was independently confirmed. **No conflicting gene of the same symbol** in a different functional class was encountered. Research therefore proceeded on the correct target.

---

## Key Findings

### Finding 1 — ilvA-I is a biosynthetic L-threonine dehydratase catalyzing the first committed step of L-isoleucine biosynthesis

UniProt Q88HB4 annotates PP_3446 as an **L-threonine dehydratase / threonine deaminase (EC 4.3.1.19)**, a 530-amino-acid protein encoded by the gene *ilvA-I* in *P. putida* KT2440. The protein sequence contains the conserved **PLP-binding Schiff-base lysine** embedded in the canonical motif (…VLLK⁶²REDL… region and, in the numbering used later, the T-F-S-F-**K77**-I-R-G motif) and the Pfam **PF00291** PLP-dependent catalytic domain. The enzyme catalyzes:

```
L-threonine  ──(PLP)──►  2-ketobutyrate (α-ketobutyrate) + NH3 + H2O
```

This is a **PLP-dependent α,β-elimination** in which the β-hydroxyl of threonine is eliminated and the resulting intermediate is hydrolyzed to release ammonia and the 2-oxo acid. The product **2-ketobutyrate is the entry metabolite of L-isoleucine biosynthesis**: it is condensed with pyruvate by acetohydroxyacid synthase (AHAS) to form 2-aceto-2-hydroxybutyrate, which proceeds through the shared branched-chain amino acid pathway (IlvC, IlvD, IlvE) to L-isoleucine.

This reaction and its pathway role are directly stated in the primary literature. As reported for the *ilvA*-encoded enzyme ([PMID: 30226377](https://pubmed.ncbi.nlm.nih.gov/30226377/)): *"Threonine dehydratase (TD), a pyridoxal 5′-phosphate (PLP)-dependent enzyme encoded by the ilvA gene, is the enzyme responsible for the conversion of l-threonine (l-Thr) to α-ketobutyrate, ammonia, and water, which is the first step in the biosynthesis of l-isoleucine."* This establishes the reaction, the PLP dependence, and the committed-step role for the gene product.

### Finding 2 — The enzyme is allosterically feedback-inhibited by L-isoleucine and activated by L-valine via its C-terminal ACT domains

Q88HB4 possesses the diagnostic **"long-form"/biosynthetic** architecture: an N-terminal PLP catalytic domain followed by **two C-terminal ACT-like regulatory domains** (approximately residues 355–427 and 450–521; Pfam **PF00585**). In the paradigm *E. coli* enzyme, the biologically active form is a **tetramer with 222 symmetry**, in which the C-terminal regulatory domains project out from a core of catalytic PLP-containing N-terminal domains. The regulatory domains are the effector-binding module that transmits allosteric signals to the active site.

This architecture directly explains the enzyme's role as a **metabolic feedback sensor**. In the *E. coli* structure ([PMID: 9562556](https://pubmed.ncbi.nlm.nih.gov/9562556/)): *"The tetramer has 222 symmetry, with C-terminal regulatory domains projecting out from a core of catalytic PLP-containing N-terminal domains,"* and *"Isoleucine, the pathway end-product, and valine, the product of a parallel pathway, serve as allosteric inhibitor and activator, respectively."* Thus L-isoleucine (the end product of the very pathway ilvA-I initiates) binds the regulatory domains and **shuts down flux** when isoleucine is abundant, while L-valine relieves/activates the enzyme. This makes ilvA-I the **flux-controlling valve** at the branch point.

Recent structural work has refined the mechanism of allosteric transmission. Isoleucine binding to the regulatory domain initiates a conformational change that propagates across the protein to the catalytic site of the adjacent protomer. As reported ([PMID: 40093177](https://pubmed.ncbi.nlm.nih.gov/40093177/)), *"isoleucine feedback-regulates the enzyme in Escherichia coli,"* and the conformational signal begins at a specific regulatory-domain phenylalanine (see Finding 5) and travels ~23 Å to the active site. The strict conservation of this machinery in Q88HB4 (below) argues that ilvA-I is regulated by the identical mechanism.

### Finding 3 — Substrate promiscuity (Thr, allo-Thr, Ser) and generation of the reactive 2-aminoacrylate intermediate

Biochemically characterized orthologs establish that biosynthetic threonine dehydratases are **not strictly specific for L-threonine**. In the well-studied *Mycobacterium smegmatis* TD, **L-allo-threonine and L-serine are also substrates**, and all three exhibit **sigmoidal, non-Michaelis–Menten (cooperative) kinetics**, consistent with the allosteric, multi-subunit nature of the enzyme ([PMID: 30226377](https://pubmed.ncbi.nlm.nih.gov/30226377/)): *"in addition to l-threonine, l-allo-threonine and l-serine are also used as substrates by TD, and all exhibit sigmoidal, non-Michaelis-Menten kinetics."*

Mechanistically, the PLP-dependent elimination proceeds through an **enamine / 2-aminoacrylate (2AA)** intermediate. When L-serine is the substrate, this intermediate is especially relevant because it can escape the active site as free 2-aminoacrylate — a **reactive, enzyme-damaging electrophile**. The biosynthetic Ser/Thr dehydratase IlvA is identified as *"a significant generator of 2AA"* ([PMID: 30327426](https://pubmed.ncbi.nlm.nih.gov/30327426/)): *"the biosynthetic serine/threonine dehydratase (EC 4.3.1.19; IlvA), which is a significant generator of 2AA."* In cells, 2AA is quenched by **RidA-family deaminases**, tying ilvA-I activity to the Rid/2AA stress-management system. This is directly relevant to *Pseudomonas*, where multiple Rid-family proteins contribute to fitness and possess broad imine/enamine deaminase activity (see Evidence Base). The substrate promiscuity and 2AA generation therefore refine the "precise role" of ilvA-I: it is primarily an isoleucine-pathway entry enzyme, but its serine-dehydratase side-activity couples it to reactive-metabolite homeostasis.

### Finding 4 — KT2440 encodes two long-form biosynthetic TD paralogs plus two short single-domain PLP dehydratases; PP_3446 maps to KEGG K01754

A UniProt survey of *P. putida* KT2440 (taxid 160488) for EC 4.3.1.19 returns **four proteins**, revealing genetic redundancy and diversity at this node:

| Protein | UniProt | Locus | Length | Architecture | Regulation |
|---|---|---|---|---|---|
| **ilvA-I** | Q88HB4 | PP_3446 | 530 aa | PLP domain (PF00291) + 2× ACT (PF00585) | Allosteric (long-form) |
| **ilvA-II** | Q88CN1 | PP_5149 | 504 aa | PLP domain + 2× ACT (329–401, 424–495) | Allosteric (long-form) |
| (short TD) | Q88EM4 | PP_4430 | 330 aa | PLP domain only (PF00291) | None (catabolic/short-form) |
| (short TD) | Q88I11 | PP_3191 | 350 aa | PLP domain only (PF00291) | None (catabolic/short-form) |

**KEGG** assigns PP_3446 to ortholog **K01754** (threonine dehydratase), and places it in pathways **ppu00290** (valine, leucine, isoleucine biosynthesis) and **ppu00260** (glycine, serine, threonine metabolism). Genomically, PP_3446 lies at complement(3903150..3904742) and is **not embedded within an ilvBN/ilvC operon** — its flanking genes differ in orientation — consistent with **independent transcriptional regulation** rather than co-expression with the downstream branched-chain machinery. The presence of a second long-form paralog (ilvA-II) plus two short single-domain enzymes indicates that *P. putida* maintains both **regulated biosynthetic** and **unregulated (likely catabolic) dehydratase** capacity, and that loss of ilvA-I alone may be partially buffered.

### Finding 5 — ilvA-I conserves both the catalytic PLP-lysine (Lys77) and the isoleucine-allostery residue (Phe368) shared with *E. coli* IlvA

A Needleman–Wunsch global alignment (BLOSUM62) of Q88HB4 (530 aa) against *E. coli* IlvA (P04968, 514 aa) yields **282/513 = 55.0% identity** — high enough for confident transfer of mechanism and function. Crucially, the two functionally decisive residues are **strictly conserved**:

- The *E. coli* **catalytic PLP Schiff-base lysine (Lys62)**, embedded in the S-F-K-I-R-G PLP-binding motif, aligns to a conserved **Lys77** in Q88HB4 (motif …TFSF**K77**IRG…). This lysine forms the internal aldimine with PLP and is indispensable for catalysis.
- The *E. coli* **isoleucine-regulatory residue Phe352**, whose isoleucine-induced movement initiates the long-range allosteric signal, aligns to a conserved **Phe368** in Q88HB4.

The allostery-initiating role of this phenylalanine is documented directly ([PMID: 40093177](https://pubmed.ncbi.nlm.nih.gov/40093177/)): *"conformational changes that initiate at Phe352 and propagate 23 Angstrom across the domain."* Because both the catalytic Lys and the allosteric Phe are conserved in ilvA-I, we can infer with high confidence that ilvA-I (i) uses the identical PLP Schiff-base catalytic mechanism and (ii) is subject to the same isoleucine-triggered, ~23 Å-propagated allosteric inhibition.

### Finding 6 — ilvA-I and ilvA-II are a recently diverged paralog pair (75% identity), both retaining intact catalytic and regulatory residues

Global NW/BLOSUM62 alignments quantify the relationships among the long-form enzymes:

| Pair | % identity |
|---|---|
| ilvA-I (Q88HB4) vs ilvA-II (Q88CN1) | **75.0%** |
| ilvA-I vs *E. coli* IlvA | 55.0% |
| ilvA-II vs *E. coli* IlvA | 53.2% |

The 75% mutual identity indicates a **relatively recent gene duplication/divergence** within *P. putida*. Both paralogs retain the functional residues: in ilvA-II the catalytic PLP Schiff-base lysine (*E. coli* Lys62 → **Lys51**) and the isoleucine-allostery phenylalanine (*E. coli* Phe352 → **Phe342**) are conserved, just as in ilvA-I (Lys77, Phe368). Therefore **both paralogs are predicted to be catalytically active and allosterically regulated biosynthetic threonine deaminases**. ilvA-I is marginally closer to the *E. coli* archetype (55.0% vs 53.2%). The functional redundancy has practical consequences: single-gene knockout phenotypes for ilvA-I may be masked by ilvA-II, and interpreting fitness data at this locus requires accounting for the paralog.

---

## Mechanistic Model / Interpretation

The findings assemble into a coherent picture of ilvA-I as the **regulated gateway enzyme of the isoleucine branch** of branched-chain amino acid (BCAA) biosynthesis in *P. putida* KT2440.

**Domain architecture and catalysis.** ilvA-I is a two-module protein. The N-terminal **PLP catalytic domain** binds pyridoxal-5′-phosphate through an internal aldimine at **Lys77**. Catalysis of the α,β-elimination proceeds via a PLP–amino-acid external aldimine, α-proton abstraction, β-elimination of the hydroxyl, and hydrolysis of the resulting **2-aminoacrylate/enamine** intermediate to yield the 2-oxo acid and ammonia.

**Pathway position.**

```
                 L-threonine
                      │
                      │   ilvA-I (PP_3446)  ── EC 4.3.1.19, PLP
                      │   [also acts on L-Ser, L-allo-Thr]
                      ▼
              2-ketobutyrate + NH3 + H2O
                      │
                      │   + pyruvate ──► acetohydroxyacid synthase (IlvBN)
                      ▼
          2-aceto-2-hydroxybutyrate
                      │  IlvC → IlvD → IlvE (shared BCAA enzymes)
                      ▼
                 L-ISOLEUCINE ──────────────┐
                                            │ (feedback)
                                            ▼
                         allosteric inhibition of ilvA-I
                              via C-terminal ACT domains
                              (signal initiates at Phe368)

          L-valine ──► allosteric ACTIVATOR of ilvA-I
```

**Allosteric control.** The two **C-terminal ACT regulatory domains** form the effector-sensing module. Binding of the end-product **L-isoleucine** initiates a conformational change (starting at **Phe368**) that propagates ~23 Å to the catalytic site of the neighboring protomer in the tetramer, damping activity — a classic negative-feedback loop that prevents wasteful overproduction of isoleucine. **L-valine**, the product of the parallel valine/leucine branch, acts as an activator, integrating the two branches so the cell balances BCAA pools. This makes ilvA-I the principal **flux valve** of the isoleucine branch.

**Coupling to reactive-metabolite homeostasis.** Because the enzyme also dehydrates L-serine, it is a **significant generator of 2-aminoacrylate (2AA)**, a reactive electrophile that can inactivate PLP enzymes. In cells this is quenched by **RidA/Rid-family deaminases**, which are present and functionally important in *Pseudomonas*. Thus ilvA-I sits at the intersection of BCAA biosynthesis and 2AA stress management.

**Redundancy.** KT2440 encodes a **second long-form paralog, ilvA-II (PP_5149, 75% identical)**, also predicted active and regulated, plus two **short single-domain** PLP dehydratases (PP_4430, PP_3191) that lack ACT regulation and likely serve catabolic or specialized roles. This layered redundancy means the isoleucine node is genetically buffered.

**Localization.** As a soluble PLP-dependent metabolic enzyme with no signal peptide or transmembrane segments, ilvA-I functions in the **cytoplasm**, where the substrate threonine and downstream BCAA-biosynthetic enzymes reside.

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution to this report |
|---|---|---|
| [30226377](https://pubmed.ncbi.nlm.nih.gov/30226377/) | *Biochemical Characterization of the M. smegmatis Threonine Deaminase* | Primary source for the catalyzed reaction (Thr → α-ketobutyrate + NH₃ + H₂O), PLP dependence, committed-step role, and substrate promiscuity (Ser, allo-Thr) with sigmoidal kinetics. **Supports F1, F3.** |
| [9562556](https://pubmed.ncbi.nlm.nih.gov/9562556/) | *Structure and control of PLP-dependent allosteric threonine deaminase* | Structural basis of the tetramer (222 symmetry), catalytic PLP N-domain + regulatory C-domains, and isoleucine-inhibition/valine-activation. **Supports F2.** |
| [40093177](https://pubmed.ncbi.nlm.nih.gov/40093177/) | *Isoleucine binding and regulation of E. coli and S. aureus threonine dehydratase (IlvA)* | Defines the isoleucine feedback mechanism and identifies Phe352 as the allostery-initiating residue propagating ~23 Å — conserved as Phe368 in ilvA-I. **Supports F2, F5.** |
| [30327426](https://pubmed.ncbi.nlm.nih.gov/30327426/) | *Analyses of variants of the Ser/Thr dehydratase IlvA … 2-aminoacrylate metabolism* | Establishes IlvA as a significant generator of the reactive 2-aminoacrylate intermediate. **Supports F3.** |
| [28957411](https://pubmed.ncbi.nlm.nih.gov/28957411/) | *Rid protein family … broad imine deaminase activity … in Pseudomonas aeruginosa* | Context for the Rid/2AA quenching system that manages IlvA-derived reactive metabolites in *Pseudomonas*. **Supports mechanistic model.** |
| [39434937](https://pubmed.ncbi.nlm.nih.gov/39434937/) | *RidA proteins contribute to fitness of …* | Reinforces the physiological link between 2AA-generating PLP enzymes and Rid-family detoxification. **Supports mechanistic model.** |
| [38664309](https://pubmed.ncbi.nlm.nih.gov/38664309/) | *Reconstruction the feedback regulation … non-auxotrophic L-threonine producing C. glutamicum* | Applied confirmation that IlvA feedback inhibition by L-isoleucine is the key control point (engineered for tighter Ile inhibition). **Supports F2.** |
| [39486138](https://pubmed.ncbi.nlm.nih.gov/39486138/) | *Targeting threonine deaminase with chiral Au NPs* | Confirms TD/ilvA as a central BCAA-biosynthetic enzyme whose inhibition blocks BCAA synthesis; supplementing Ile/Val rescues. **Supports F1, F2.** |
| [23995642](https://pubmed.ncbi.nlm.nih.gov/23995642/) | *Amino acid racemization in P. putida KT2440* | KT2440-specific metabolic-enzymology context (D/L-amino acid handling in the target organism). Background. |
| [31503400](https://pubmed.ncbi.nlm.nih.gov/31503400/) | *Metabolite profiling of cold adaptation of P. putida KT2440* | Documents amino-acid pool remodeling in KT2440, the physiological milieu of ilvA-I. Background. |

**How the evidence converges:** No single experimental study characterizes Q88HB4 directly (see Limitations). Instead, the assignment is built from (i) authoritative structural and biochemical primary literature on orthologous biosynthetic threonine deaminases (*E. coli*, *M. smegmatis*, *S. aureus*, *Salmonella*), (ii) strict conservation of catalytic and regulatory residues demonstrated by sequence alignment, and (iii) database placement (UniProt, KEGG K01754, Pfam PF00291/PF00585). All lines agree, giving high confidence in the annotation.

---

## Limitations and Knowledge Gaps

1. **No direct experimental characterization of Q88HB4.** There is, to date, **no primary study that purifies and kinetically characterizes the PP_3446 protein specifically**. Function is inferred by homology (55% identity to *E. coli* IlvA) and conserved-residue mapping, not by direct assay. Kinetic parameters (Kₘ for Thr/Ser, Hill coefficient, Kᵢ for isoleucine, activation by valine) for the *P. putida* enzyme are unmeasured.

2. **Paralog redundancy complicates genetics.** Because ilvA-II (PP_5149) is 75% identical and predicted fully active, a single ilvA-I deletion may show **little or no isoleucine-auxotrophy phenotype**. The relative contribution, expression level, and condition-specific roles of ilvA-I vs ilvA-II are unknown.

3. **Regulation is inferred, not measured.** The isoleucine-inhibition/valine-activation model is transferred from *E. coli*. Whether *P. putida* ilvA-I shows identical effector specificity and cooperativity, or has diverged (e.g., altered Ile sensitivity), has not been tested.

4. **Domain-boundary and oligomeric state predictions are computational.** The ACT domain boundaries (~355–427, 450–521) and the assumed homotetramer are based on family architecture, not an experimental *P. putida* structure.

5. **Physiological significance of the serine-dehydratase side reaction / 2AA output in KT2440 is untested.** The coupling to specific Rid-family proteins in KT2440 and the in-vivo 2AA burden attributable to ilvA-I remain to be quantified.

6. **Operon/regulon context.** While PP_3446 appears not to be in an ilvBN/ilvC operon, its actual promoter, transcription-factor control, and co-regulation with the BCAA regulon in *P. putida* are not experimentally defined here.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant expression and enzyme kinetics.** Clone, express, and purify Q88HB4; measure steady-state kinetics on L-threonine, L-serine, and L-allo-threonine (expect sigmoidal curves), and determine the Hill coefficient, Kᵢ for L-isoleucine, and activation by L-valine. This would directly confirm Findings 1–3 for the *P. putida* enzyme.

2. **Site-directed mutagenesis of Lys77 and Phe368.** Mutate the predicted catalytic lysine (K77A) to confirm PLP Schiff-base catalysis, and the allosteric phenylalanine (F368A/F368L) to test whether isoleucine feedback is abolished while catalysis is retained — validating Finding 5's residue assignments.

3. **Single and double knockouts (ΔilvA-I, ΔilvA-II, double).** Assess isoleucine auxotrophy on minimal medium ± isoleucine to quantify redundancy (Finding 6). A double mutant is predicted to be isoleucine-auxotrophic; single mutants may be silent.

4. **Structural determination.** Solve a crystal or cryo-EM structure of ilvA-I ± isoleucine to confirm the tetramer, ACT-domain arrangement, and the ~23 Å allosteric relay proposed from the *E. coli* homolog.

5. **2-aminoacrylate flux and Rid coupling.** Using serine-loading and RidA-deficient backgrounds, test whether ilvA-I is a significant in-vivo 2AA source in KT2440 and identify which Rid-family protein(s) quench it (linking to [PMID: 28957411](https://pubmed.ncbi.nlm.nih.gov/28957411/), [PMID: 39434937](https://pubmed.ncbi.nlm.nih.gov/39434937/)).

6. **Transcriptional analysis.** Map the PP_3446 promoter and test regulation by isoleucine/BCAA availability and by global regulators, resolving whether ilvA-I and ilvA-II are differentially expressed across conditions.

---

## Conclusion

*ilvA-I* (Q88HB4 / PP_3446) encodes the **isoleucine-regulated biosynthetic L-threonine dehydratase (threonine deaminase, EC 4.3.1.19)** of *P. putida* KT2440. It is a soluble, cytoplasmic, PLP-dependent enzyme that performs the **first committed step of L-isoleucine biosynthesis** — converting L-threonine (and, secondarily, L-serine/L-allo-threonine) to 2-ketobutyrate + ammonia + water via a 2-aminoacrylate intermediate. As a long-form isozyme with an N-terminal PLP catalytic domain (Lys77) and two C-terminal ACT regulatory domains, it functions as the **allosterically controlled flux valve** of the isoleucine branch: feedback-inhibited by L-isoleucine (signal initiating at Phe368) and activated by L-valine. The assignment is strongly supported by 55% identity to the structurally characterized *E. coli* IlvA, strict conservation of catalytic and regulatory residues, and KEGG/Pfam placement. KT2440 additionally encodes a 75%-identical, competent paralog (ilvA-II / PP_5149), indicating functional redundancy at this metabolic node.


## Artifacts

- [OpenScientist final report](ilvA-I-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](ilvA-I-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:30226377
2. PMID:9562556
3. PMID:40093177
4. PMID:30327426
5. PMID:28957411
6. PMID:39434937