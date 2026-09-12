---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-11T16:19:41.818416'
end_time: '2026-07-11T16:50:48.459125'
duration_seconds: 1866.64
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_2528
  gene_symbol: PP_2528
  uniprot_accession: Q88JW9
  protein_description: 'SubName: Full=O-acetylhomoserine (Thiol)-lyase {ECO:0000313|EMBL:AAN68137.1};
    EC=2.5.1.49 {ECO:0000313|EMBL:AAN68137.1};'
  gene_info: OrderedLocusNames=PP_2528 {ECO:0000313|EMBL:AAN68137.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the trans-sulfuration enzymes family.
  protein_domains: Cys/Met-Metab_PyrdxlP-dep_enz. (IPR000277); Cys_met_metab_PP. (IPR054542);
    OAc-hSer/O-AcSer_sulfhydrylase. (IPR006235); PyrdxlP-dep_Trfase. (IPR015424);
    PyrdxlP-dep_Trfase_major. (IPR015421)
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
citation_count: 8
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PP_2528-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PP_2528-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88JW9
- **Protein Description:** SubName: Full=O-acetylhomoserine (Thiol)-lyase {ECO:0000313|EMBL:AAN68137.1}; EC=2.5.1.49 {ECO:0000313|EMBL:AAN68137.1};
- **Gene Information:** OrderedLocusNames=PP_2528 {ECO:0000313|EMBL:AAN68137.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the trans-sulfuration enzymes family.
- **Key Domains:** Cys/Met-Metab_PyrdxlP-dep_enz. (IPR000277); Cys_met_metab_PP. (IPR054542); OAc-hSer/O-AcSer_sulfhydrylase. (IPR006235); PyrdxlP-dep_Trfase. (IPR015424); PyrdxlP-dep_Trfase_major. (IPR015421)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_2528" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_2528' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_2528** (gene ID: PP_2528, UniProt: Q88JW9) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: PP_2528 (Q88JW9) — O-Acetylhomoserine Sulfhydrylase (MetY) of *Pseudomonas putida* KT2440

**Gene:** PP_2528 (ordered locus name) · **Organism:** *Pseudomonas putida* strain ATCC 47054 / DSM 6125 / KT2440 (PSEPK)
**UniProt:** Q88JW9 · **Length:** 425 aa · **NCBI Protein:** AAN68137 · **KEGG:** ppu:PP_2528 · **KEGG Orthology:** K01740
**EC:** 2.5.1.49 · **Enzyme name:** O-acetylhomoserine (thiol)-lyase / O-acetylhomoserine sulfhydrylase (MetY / OAHS)

---

## Summary

**PP_2528 (UniProt Q88JW9) of *Pseudomonas putida* KT2440 encodes an O-acetylhomoserine sulfhydrylase (OAHS; also called MetY; EC 2.5.1.49), a pyridoxal-5′-phosphate (PLP)-dependent enzyme of the trans-sulfuration / Cys-Met-metabolism enzyme family.** Its primary and defining function is to catalyze the sulfur-incorporation step of *de novo* L-methionine biosynthesis via the **"direct sulfhydrylation"** route. The enzyme condenses the activated amino acid **O-acetyl-L-homoserine** with an inorganic sulfur nucleophile (hydrogen sulfide / sulfide) to produce **L-homocysteine + acetate**. When methanethiol (CH₃SH) serves as the nucleophile, the enzyme can produce **L-methionine directly**, demonstrating the sulfur-donor flexibility characteristic of the family. Mechanistically this is a **γ-replacement (γ-substitution)** on the O-acyl-homoserine side chain, proceeding through a PLP internal aldimine at an active-site lysine.

The gene product is a **soluble, cytoplasmic enzyme** that assembles into a **homotetramer** and adopts the classic γ-family fold shared with cystathionine γ-lyase and methionine γ-lyase. Catalysis depends on a covalently bound PLP cofactor anchored via a Schiff base to a conserved active-site lysine (**Lys204** in PP_2528), assisted by two conserved active-site tyrosines (**Tyr52** and **Tyr107**) that were experimentally validated by site-directed mutagenesis in the closely related *Clostridioides difficile* orthologue and are conserved at identical positions in PP_2528.

Within *P. putida* KT2440 the enzyme sits at the **sulfhydrylation branchpoint** of the aspartate-derived methionine pathway (KEGG map ppu00270). Its substrate is supplied by homoserine O-acetyltransferase (MetXA, PP_5097); its L-homocysteine product is methylated to L-methionine by MetH (PP_2375) or MetE (PP_2698/PP_4637), and methionine is then adenylated to S-adenosylmethionine by MetK (PP_4967). A parallel transsulfuration route (MetB, PP_0659) coexists, so PP_2528 represents one of two convergent means of introducing reduced sulfur into the methionine backbone. **No PP_2528-specific experimental study exists; the assignment rests on strong orthology to biochemically and structurally characterized OAHS enzymes, exact conservation of the catalytic apparatus, and an intact pathway context — giving high confidence in the primary function while leaving quantitative parameters (kinetics, sulfur-donor preference) to be measured.**

---

## Identity Verification (this is the correct gene)

All independent lines of evidence converge on the same assignment, confirming PP_2528/Q88JW9 is an O-acetylhomoserine sulfhydrylase and not an ambiguous or mis-matched symbol:

| Evidence source | Annotation | Reference |
|---|---|---|
| UniProt Q88JW9 | "O-acetylhomoserine (Thiol)-lyase", EC 2.5.1.49; trans-sulfuration family; PLP cofactor (ChEBI:597326) | UniProtKB |
| InterPro / Pfam | **IPR006235 OAc-hSer/O-AcSer sulfhydrylase**; IPR000277 Cys/Met-Metab PLP-dep enzyme; **PF01053** | InterPro/Pfam |
| KEGG | Orthology **K01740** "O-acetylhomoserine (thiol)-lyase [EC:2.5.1.49]"; pathway **ppu00270** | KEGG |
| GO (electronic) | O-acetylhomoserine aminocarboxypropyltransferase activity (GO:0003961); L-homocysteine biosynthetic process (GO:0071269); transsulfuration (GO:0019346); cytoplasm (GO:0005737) | UniProtKB |

Gene symbol, EC number, protein family, and conserved domains are mutually consistent, and the organism is confirmed as *P. putida* KT2440. **No ambiguity was found.** One important caveat: much *P. putida* literature concerns the unrelated *catabolic* enzyme **methionine γ-lyase (PpMGL / methioninase)**; PP_2528 is a *biosynthetic* enzyme with the opposite role and must not be conflated with it (see *Limitations*).

---

## Key Findings

### Finding 1 — PP_2528 is an O-acetylhomoserine sulfhydrylase (MetY, EC 2.5.1.49) catalyzing direct sulfhydrylation in methionine biosynthesis

The UniProt record for Q88JW9 describes a 425-amino-acid protein encoded by PP_2528 in *P. putida* KT2440, annotated with EC 2.5.1.49 and assigned to the trans-sulfuration enzyme family. It carries a PLP cofactor (ChEBI:597326) and the GO terms **O-acetylhomoserine aminocarboxypropyltransferase activity (GO:0003961)**, **L-homocysteine biosynthetic process (GO:0071269)**, and **transsulfuration (GO:0019346)**. Its InterPro signature includes IPR006235 (OAc-hSer/O-AcSer sulfhydrylase), IPR000277 (Cys/Met-metabolism PLP-dependent enzyme), and Pfam PF01053; the sequence contains the catalytic PLP-binding lysine within a conserved "LTKY" motif near residue 200.

The reaction defines the enzyme's role. O-acetylhomoserine sulfhydrylase converts O-acetylhomoserine to homocysteine using sulfide in the process known as **direct sulfhydrylation** — the biochemical alternative to the enterobacterial transsulfuration route, introducing reduced sulfur into the C4 amino-acid backbone in a single γ-substitution step. Literature on the enzyme family confirms OAHS is a member of the Cys/Met-metabolism PLP-dependent enzyme family, matching PP_2528's annotated cofactor and domains.

**Annotation/statistical evidence:** UniProt Q88JW9 — 425 aa; EC 2.5.1.49; trans-sulfuration family; PLP cofactor; GO:0003961 / GO:0071269 / GO:0019346; InterPro IPR006235, IPR000277; Pfam PF01053; catalytic Lys in "LTKY" motif (~res 200).

- *"OAHS catalyzes the conversion of O-acetylhomoserine to homocysteine using sulfide in a process known as direct sulfhydrylation"* — [PMID: 21931214](https://pubmed.ncbi.nlm.nih.gov/21931214/). Defines the reaction catalyzed by the OAHS/MetY family to which PP_2528 belongs.
- *"a member of the Cys/Met metabolism pyridoxal 5′-phosphate-dependent enzyme family"* — [PMID: 39736317](https://pubmed.ncbi.nlm.nih.gov/39736317/). Confirms OAHS is a PLP-dependent Cys/Met metabolism enzyme, matching PP_2528's cofactor and InterPro family.

### Finding 2 — OAHS is a PLP-dependent γ-fold enzyme that assembles as a homotetramer and uses sulfide or methanethiol as the sulfur nucleophile

Structural and biochemical characterization of OAHS orthologues establishes the quaternary structure, fold, and mechanism confidently extended to PP_2528. The crystal structure of *Wolinella succinogenes* OAHS (MetY), solved at 2.2 Å, shows the biological unit is a **tetramer in solution**, sharing the same fold as cystathionine γ-lyase and methionine γ-lyase and placing MetY in the **γ-elimination subclass** of the Cys/Met-metabolism PLP-dependent family; that study also proposed a novel sulfur transfer proceeding through a protein thiocarboxylate intermediate.

Multiple bacterial OAHS enzymes reinforce this picture. The *Clostridium tetani* enzyme has a ~50 kDa (462-aa) subunit forming a ~200 kDa native homotetramer, has a pH optimum near 7.5, and is capable of forming L-methionine directly using methanethiol as the sulfur source — evidencing sulfur-donor flexibility. The *Clostridium novyi* OAHS is a ~184 kDa native protein built from ~46 kDa subunits, catalyzes γ-substitution of O-acetylhomoserine, and also has a pH optimum of 7.5. The *Clostridioides difficile* enzyme provides mutagenetic evidence that active-site Tyr52 and Tyr107 are essential, with Tyr107 acting as the general acid in acetate elimination.

**Structural/statistical evidence:** *W. succinogenes* OAHS 2.2 Å, tetramer, γ-elimination subclass, thiocarboxylate intermediate (PMID 21931214); *C. tetani* OAHS 462 aa / ~50 kDa subunit, ~200 kDa native tetramer, pH optimum 7.5, methionine from methanethiol (PMID 39736317); *C. novyi* OAHS ~184 kDa / ~46 kDa subunit, γ-substitution, pH optimum 7.5 (PMID 33338587).

- *"the biological unit is a tetramer in solution"* — [PMID: 21931214](https://pubmed.ncbi.nlm.nih.gov/21931214/). Establishes the homotetrameric quaternary structure of OAHS enzymes.
- *"MetY belongs to the γ-elimination subclass of the Cys/Met metabolism PLP-dependent family of enzymes"* — [PMID: 21931214](https://pubmed.ncbi.nlm.nih.gov/21931214/). Defines the catalytic fold/mechanistic subclass of the family PP_2528 belongs to.
- *"capable of l-methionine formation using methanethiol as a sulfur source"* — [PMID: 39736317](https://pubmed.ncbi.nlm.nih.gov/39736317/). Shows OAHS can directly form methionine using methanethiol, evidencing sulfur-donor flexibility.

### Finding 3 — PP_2528 (MetY) sits at the sulfhydrylation branchpoint of an intact aspartate-derived methionine pathway in *P. putida* KT2440

Mapping the *P. putida* KT2440 (KEGG code **ppu**) methionine-pathway KEGG Orthology groups to their genome loci places PP_2528 in a complete, intact route. Homoserine O-acetyltransferase (MetXA, K00641) is **PP_5097**, producing the substrate O-acetyl-L-homoserine. PP_2528 is the O-acetylhomoserine (thiol)-lyase (MetY, K01740) that consumes it. A parallel transsulfuration route is also encoded: cystathionine γ-synthase (MetB, K01739) is **PP_0659**. Downstream, the methionine synthases MetH (K00548, **PP_2375**) and MetE (K00549, **PP_2698/PP_4637**) methylate homocysteine to methionine, and SAM synthetase MetK (K00789, **PP_4967**) forms S-adenosylmethionine.

PP_2528 lies in KEGG pathway **ppu00270 (Cysteine and methionine metabolism)** at genomic position complement(2874605..2875882). Its immediate neighbors (PP_2526, PP_2527, PP_2530) are unrelated unknown-function proteins, indicating PP_2528 is **not** part of a clustered *met* operon (unlike *Leptospira*, where *metYX(W)* are co-localized). This cements the branchpoint interpretation: PP_2528 provides one of two convergent sulfur-incorporation routes feeding a shared downstream methylation and SAM-synthesis machinery. Comparative genetics supports this: in *Leptospira*, a *metY* knockout retains methionine prototrophy because the transsulfuration route bypasses direct sulfhydrylation ([PMID: 12951250](https://pubmed.ncbi.nlm.nih.gov/12951250/)) — mirroring the redundant MetY(PP_2528)/MetB(PP_0659) architecture in *P. putida*.

**Genomic/statistical evidence:** KEGG ppu KO-to-locus mapping — MetXA/K00641=PP_5097; MetY/K01740=PP_2528; MetB/K01739=PP_0659; MetH/K00548=PP_2375; MetE/K00549=PP_2698 & PP_4637; MetK/K00789=PP_4967. Pathway ppu00270; locus complement(2874605..2875882); flanking genes PP_2526/2527/2530 unrelated (no *met* operon).

### Finding 4 — PP_2528 conserves the complete OAHS catalytic apparatus, including Tyr52/Tyr107 at positions identical to the mutagenetically-validated *C. difficile* enzyme

Direct sequence analysis of Q88JW9 (425 aa) shows PP_2528 preserves every element of the OAHS catalytic machinery. The catalytic PLP-Schiff-base lysine is **Lys204**, within the canonical [ST]-x-[ST]-K-[YF] motif "SLTKY" (residues 201–205). Critically, the two active-site tyrosines shown essential by site-directed mutagenesis in the *C. difficile* orthologue — **Tyr52**, which positions the catalytic lysine, and **Tyr107**, which acts as the general acid during acetate elimination — are present at the **identical sequence positions 52 and 107** in PP_2528. Additional PLP-anchoring and phosphate-binding motifs are conserved: the glycine-rich loop "GNPAG" (res 153–157), "GGHGTS" (res 207–212), and the substrate/PLP-binding "DNTVA" motif (res 179).

Because these are exactly the functionally decisive positions validated experimentally in a close relative, and because they are conserved with matching spacing in PP_2528, the assignment can be made with high confidence by orthology. A targeted PubMed search returned no PP_2528-specific experimental study, so the assignment is inferential — but it rests on identity at mechanistically critical positions, the strongest available structural/evolutionary evidence.

**Sequence/statistical evidence:** Q88JW9 425 aa; catalytic Lys204 in "SLTKY" (201–205); Tyr52 and Tyr107 at identical positions to *C. difficile*; conserved "GNPAG" (153–157), "GGHGTS" (207–212), "DNTVA" (179).

- *"Tyr107 could act as a general acid catalyst at the stage of acetate elimination"* — [PMID: 37331706](https://pubmed.ncbi.nlm.nih.gov/37331706/). Identifies Tyr107 as the mechanistically critical general-acid residue; PP_2528 conserves Tyr at the identical position 107.
- *"Tyr52 is involved in ensuring optimal position of the catalytic coenzyme-binding lysine residue"* — [PMID: 37331706](https://pubmed.ncbi.nlm.nih.gov/37331706/). Identifies Tyr52's role in positioning the PLP-binding lysine; PP_2528 conserves Tyr at position 52 and the catalytic Lys204.

---

## Mechanistic Model / Interpretation

### The catalyzed reaction

PP_2528 catalyzes a PLP-dependent **γ-substitution** (direct sulfhydrylation):

```
   O-acetyl-L-homoserine  +  HS⁻ (sulfide)   ─────►  L-homocysteine  +  acetate
                                    │
                                    │ (alternative nucleophile)
                                    ▼
   O-acetyl-L-homoserine  +  CH₃SH (methanethiol) ─► L-methionine  +  acetate
```

The PLP cofactor forms an internal aldimine (Schiff base) with **Lys204**. The amino-acid substrate displaces the lysine to form an external aldimine; α-proton abstraction and γ-elimination of the acetate leaving group (assisted by **Tyr107** as a general acid) generate a PLP-bound α,β-unsaturated intermediate. The sulfur nucleophile then attacks at Cγ, and re-protonation releases the thiol product. **Tyr52** maintains the productive geometry of the catalytic lysine. In the *W. succinogenes* enzyme, sulfur transfer proceeds through a novel protein thiocarboxylate intermediate, enabling capture of inorganic sulfide.

### Placement in the methionine biosynthetic pathway

```
     aspartate
        │  (aspartokinase, ASA-DH, homoserine DH …)
        ▼
   L-homoserine
        │  MetXA (homoserine O-acetyltransferase, PP_5097)
        ▼
   O-acetyl-L-homoserine ─────────────────────────────┐
        │                                              │
        │  ►► DIRECT SULFHYDRYLATION ◄◄                │  ►► TRANSSULFURATION ◄◄
        │  MetY = PP_2528  (this gene)                 │  MetB (PP_0659) + cysteine
        │  + HS⁻ / CH₃SH                               │  → cystathionine → (β-lyase)
        ▼                                              ▼
   L-homocysteine  ◄───────────────────────────────────┘
        │  MetH (PP_2375, B12-dependent)  /  MetE (PP_2698, PP_4637)
        ▼
   L-methionine
        │  MetK (PP_4967)
        ▼
   S-adenosyl-L-methionine (SAM)
```

The two routes into homocysteine are convergent: PP_2528 introduces sulfur directly from inorganic sulfide (or methanethiol), whereas the MetB route routes sulfur through cysteine and a cystathionine intermediate. *P. putida* retains both, offering metabolic flexibility depending on available sulfur. Genetic studies in *Leptospira* show that disrupting *metY* still permits methionine prototrophy because transsulfuration can bypass it — implying PP_2528 is likely dispensable when the parallel route is functional. PP_2528's product feeds the cell's entire methionine and **SAM (methyl-donor)** economy.

### Localization

All biochemically characterized OAHS enzymes are soluble cytoplasmic proteins with no signal peptide or transmembrane segments. PP_2528 (425 aa, ~46 kDa subunit) is annotated to the cytoplasm (GO:0005737) and carries out its function in the **bacterial cytosol**, where sulfide and precursors are generated.

### Comparative summary of characterized OAHS orthologues

| Organism | Locus / name | Native mass | Subunit | Oligomer | pH opt. | Sulfur donor | Reference |
|---|---|---|---|---|---|---|---|
| *P. putida* KT2440 | PP_2528 / Q88JW9 | — | 425 aa (~46 kDa) | tetramer (by orthology) | — | sulfide (inferred) | this report |
| *Wolinella succinogenes* | MetY | tetramer | — | tetramer | — | sulfide | [PMID: 21931214](https://pubmed.ncbi.nlm.nih.gov/21931214/) |
| *Clostridium tetani* | — | ~200 kDa | ~50 kDa / 462 aa | homotetramer | 7.5 | methanethiol / sulfide | [PMID: 39736317](https://pubmed.ncbi.nlm.nih.gov/39736317/) |
| *Clostridium novyi* | NT01CX_1210 | ~184 kDa | ~46 kDa | tetramer | 7.5 | sulfide | [PMID: 33338587](https://pubmed.ncbi.nlm.nih.gov/33338587/) |
| *Clostridioides difficile* | — | — | — | — | — | Tyr52/Tyr107 catalytic | [PMID: 37331706](https://pubmed.ncbi.nlm.nih.gov/37331706/) |

---

## Evidence Base

| PMID | Title (abbrev.) | Relevance to PP_2528 |
|---|---|---|
| [21931214](https://pubmed.ncbi.nlm.nih.gov/21931214/) | Novel sulfur-transfer mechanism of OAHS in *Wolinella succinogenes* | Defines the direct-sulfhydrylation reaction, homotetrameric structure, and γ-elimination fold/subclass; primary structural anchor. |
| [39736317](https://pubmed.ncbi.nlm.nih.gov/39736317/) | OAHS in the direct sulfhydrylation pathway of *Clostridium tetani* | Confirms Cys/Met PLP-dependent family membership; homotetramer ~200 kDa; L-methionine from methanethiol (sulfur-donor flexibility). |
| [37331706](https://pubmed.ncbi.nlm.nih.gov/37331706/) | Role of tyrosine residues in *Clostridioides difficile* OAHS active site | Mutagenetic validation of Tyr52 (positions catalytic Lys) and Tyr107 (general acid) — both conserved at identical positions in PP_2528. |
| [33338587](https://pubmed.ncbi.nlm.nih.gov/33338587/) | OAHS from *Clostridium novyi*: cloning, expression, characterization | Independent biochemical confirmation of γ-substitution, ~184 kDa native mass, pH 7.5 optimum; single route to methionine in that organism. |
| [12951250](https://pubmed.ncbi.nlm.nih.gov/12951250/) | Two methionine-biosynthesis pathways in *Leptospira* | Genetic evidence that *metY* (sulfhydrylation) can be bypassed by transsulfuration — informs the non-essentiality/branchpoint interpretation. |
| [41240142](https://pubmed.ncbi.nlm.nih.gov/41240142/) | *Thermotoga maritima* MetY has five enzyme activities | Shows OAHS produces L-homocysteine from O-acetyl-L-homoserine + H₂S; documents catalytic promiscuity of the family. |
| [38568076](https://pubmed.ncbi.nlm.nih.gov/38568076/) | pH-dependent regulation of an acidophilic OAHS | Describes open/closed conformational interconversion regulating substrate/PLP access; relevant to mechanism and inhibitor design. |

The evidence base is entirely orthologue-based: no study reports PP_2528 directly. However, concordance across a Gram-negative epsilonproteobacterium, three Clostridia, and a hyperthermophile on reaction, fold, oligomeric state, and catalytic residues, combined with PP_2528's exact conservation of the decisive Lys204/Tyr52/Tyr107 apparatus, makes the assignment robust. Note that several reviewed *P. putida* papers concern methionine **γ-lyase (methioninase)** — e.g. [PMID: 34953671](https://pubmed.ncbi.nlm.nih.gov/34953671/), [PMID: 41005402](https://pubmed.ncbi.nlm.nih.gov/41005402/), [PMID: 31479672](https://pubmed.ncbi.nlm.nih.gov/31479672/). These share the PLP γ-family fold but catalyze the opposite, degradative reaction and are a different gene; they were correctly excluded and are flagged to prevent conflation.

---

## Supported vs. Refuted Hypotheses

**Supported:**
- PP_2528 is an O-acetylhomoserine sulfhydrylase (MetY/OAHS, EC 2.5.1.49).
- It catalyzes direct sulfhydrylation of O-acetyl-L-homoserine to L-homocysteine (or methionine with methanethiol).
- It is a cytoplasmic, PLP-dependent homotetramer.
- It functions in the aspartate-derived methionine-biosynthesis pathway upstream of MetH/MetE.

**Refuted / ruled out:**
- PP_2528 is **not** the O-succinyl enzyme (KT2440 uses the *O-acetyl* transferase MetXA, K00641).
- PP_2528 is **not** a catabolic methionine γ-lyase (a different *P. putida* gene).
- PP_2528 is not membrane-associated or secreted.

---

## Limitations and Knowledge Gaps

1. **No direct experimental characterization of PP_2528.** The assignment is inferential (orthology + sequence conservation + pathway context). No purified-protein kinetics, crystal structure, or knockout phenotype exists specifically for the *P. putida* KT2440 gene product. Confidence in the primary function is nonetheless **high**; residual gaps are quantitative.
2. **Substrate/sulfur-donor specificity is inferred, not measured.** Whether PP_2528 prefers sulfide vs. methanethiol, and its kinetic parameters (kcat, Km, pH optimum), are unknown. Family members vary.
3. **Essentiality and in vivo flux are unresolved.** Because *P. putida* also encodes MetB (PP_0659), PP_2528 may be dispensable under some conditions, as seen for *metY* in *Leptospira*. The relative flux through direct sulfhydrylation vs. transsulfuration is unquantified.
4. **Regulation is unknown.** Transcriptional/metabolic control (e.g., by MetR, methionine, or sulfur availability) in KT2440 has not been examined.
5. **Potential catalytic promiscuity untested.** The *Thermotoga* orthologue shows five activities; whether PP_2528 has secondary activities is unknown.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant expression and enzyme assay.** Clone PP_2528, purify the protein, and confirm OAHS activity by measuring L-homocysteine (or L-methionine) production from O-acetyl-L-homoserine with sulfide and with methanethiol. Determine kcat/Km for each sulfur donor and the pH optimum.
2. **Structural determination.** Solve the crystal or cryo-EM structure of PP_2528 (or produce a high-confidence AlphaFold model) to confirm the homotetramer, the PLP-Lys204 internal aldimine, and the spatial arrangement of Tyr52/Tyr107; compare against the *W. succinogenes* structure (PMID 21931214).
3. **Site-directed mutagenesis.** Mutate Lys204, Tyr52, and Tyr107 to test predicted catalytic roles, mirroring the *C. difficile* study (PMID 37331706).
4. **Gene-knockout phenotyping.** Delete PP_2528 in KT2440 and assess methionine auxotrophy under varying sulfur sources (sulfide, sulfate, methanethiol, cysteine); combine with a *metB* (PP_0659) deletion to test mutual redundancy, as in *Leptospira* (PMID 12951250).
5. **Regulation studies.** Measure PP_2528 transcription/protein levels under sulfur limitation and methionine supplementation to place the gene within the sulfur-assimilation regulon.
6. **Biotechnology/therapeutic context.** Given *P. putida*'s role as a biotechnology chassis, evaluate PP_2528 as a lever for methionine/sulfur-amino-acid overproduction, and as a potential antibacterial target (per inhibitor-design rationale in PMID 38568076).

---

### Key References
- Tran, Krishnamoorthy, Begley, Ealick (2011). *A novel mechanism of sulfur transfer catalyzed by O-acetylhomoserine sulfhydrylase in the methionine-biosynthetic pathway of Wolinella succinogenes.* PMID **21931214**.
- Kulikova et al. (2025). *Revealing O-acetylhomoserine sulfhydrylase involved in direct sulfhydrylation pathway in Clostridium tetani.* PMID **39736317**.
- Kulikova et al. (2023). *O-Acetylhomoserine Sulfhydrylase from Clostridioides difficile: Role of Tyrosine Residues in the Active Site.* PMID **37331706**.
- Kulikova et al. (2021). *O-acetylhomoserine sulfhydrylase from Clostridium novyi.* PMID **33338587**.
- Matoba et al. (2024). *pH-dependent regulation of an acidophilic O-acetylhomoserine sulfhydrylase.* PMID **38568076**.
- Miyamoto & Sakai-Kato (2025). *O-Acetyl-L-homoserine sulfhydrylase from Thermotoga maritima has five enzyme activities.* PMID **41240142**.
- Picardeau, Bauby, Saint Girons (2003). *Genetic evidence for the existence of two pathways for the biosynthesis of methionine in the Leptospira spp.* PMID **12951250**.
- Database records: UniProtKB Q88JW9; KEGG ppu:PP_2528 (K01740); InterPro IPR006235; Pfam PF01053.

---

*Prepared from 3 investigation iterations, 4 confirmed findings, and 17 reviewed papers. Functional assignment is by strong orthology to biochemically and structurally characterized O-acetylhomoserine sulfhydrylases; no PP_2528-specific primary study currently exists.*


## Artifacts

- [OpenScientist final report](PP_2528-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PP_2528-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:21931214
2. PMID:39736317
3. PMID:12951250
4. PMID:37331706
5. PMID:33338587
6. PMID:34953671
7. PMID:41005402
8. PMID:31479672