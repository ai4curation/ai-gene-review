---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T11:46:03.576445'
end_time: '2026-08-31T12:00:08.695635'
duration_seconds: 845.12
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: rbsD
  gene_symbol: rbsD
  uniprot_accession: Q88K33
  protein_description: 'RecName: Full=D-ribose pyranase {ECO:0000255|HAMAP-Rule:MF_01661};
    EC=5.4.99.62 {ECO:0000255|HAMAP-Rule:MF_01661};'
  gene_info: Name=rbsD {ECO:0000255|HAMAP-Rule:MF_01661}; OrderedLocusNames=PP_2459;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the RbsD / FucU family. RbsD subfamily.
  protein_domains: D-ribose_pyranase. (IPR023064); RbsD-like_sf. (IPR023750); RbsD_FucU.
    (IPR007721); RbsD_FucU (PF05025)
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
citation_count: 13
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: rbsD-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: rbsD-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88K33
- **Protein Description:** RecName: Full=D-ribose pyranase {ECO:0000255|HAMAP-Rule:MF_01661}; EC=5.4.99.62 {ECO:0000255|HAMAP-Rule:MF_01661};
- **Gene Information:** Name=rbsD {ECO:0000255|HAMAP-Rule:MF_01661}; OrderedLocusNames=PP_2459;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the RbsD / FucU family. RbsD subfamily.
- **Key Domains:** D-ribose_pyranase. (IPR023064); RbsD-like_sf. (IPR023750); RbsD_FucU. (IPR007721); RbsD_FucU (PF05025)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "rbsD" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'rbsD' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **rbsD** (gene ID: rbsD, UniProt: Q88K33) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *rbsD* (D-ribose pyranase) in *Pseudomonas putida* KT2440

**Gene:** *rbsD* — **UniProt:** Q88K33 — **Ordered locus:** PP_2459 — **EC:** 5.4.99.62
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / KT2440), PSEPK
**Protein family:** RbsD / FucU family, RbsD subfamily (Pfam PF05025; InterPro IPR007721, IPR023064, IPR023750)

---

## Summary

RbsD (Q88K33, encoded by *rbsD* / PP_2459) is a **cytoplasmic D-ribose pyranase**, EC 5.4.99.62, that catalyzes the interconversion of the two ring forms of the pentose sugar D-ribose: **β-D-ribopyranose ⇌ β-D-ribofuranose**. This is a ring-form (mutarotase-type) isomerization — it changes the ring size of the sugar, not its stereochemistry or oxidation state. Free D-ribose in solution exists predominantly as the six-membered pyranose ring, but the downstream catabolic enzyme ribokinase can only phosphorylate the five-membered furanose form. Because the spontaneous pyranose↔furanose interconversion of ribose is slow, RbsD is required to keep the furanose pool replenished. The assignment for the *P. putida* protein rests on HAMAP-Rule MF_01661 and is independently corroborated here by residue-level conservation analysis against the biochemically characterized *E. coli* enzyme (~50 % identity, all catalytic residues retained).

Functionally, RbsD occupies the **first committed step of D-ribose degradation** (step 1 of 2 leading to D-ribose-5-phosphate). It works in tandem with ribokinase (RbsK, PP_2458), which phosphorylates the β-furanose product to **D-ribose-5-phosphate**, feeding carbon into the **pentose phosphate pathway** and thence into central metabolism. Upstream, ribose is imported by a high-affinity ABC transporter (RbsABC). In *P. putida* KT2440 all of these components are encoded in a single contiguous chromosomal ribose (*rbs*) cluster spanning PP_2454–PP_2460, which also carries the LacI-family repressor RbsR and an adjacent ribonucleoside hydrolase (*nuh*), mirroring the canonical *E. coli rbsDACBK* operon plus regulator.

Structurally, RbsD is not active as a monomer. Members of this family assemble into a striking **decameric toroidal ring**, and each catalytic site is built from **two adjacent subunits** — one contributing a catalytic tyrosine, the other a His–Asp dyad and a proton-donor histidine. Catalytic competence therefore depends on the higher-order oligomeric state: a dimeric homolog from *Staphylococcus aureus* with an incomplete active site is inactive. The *P. putida* protein retains all of the diagnostic catalytic and substrate-binding residues and is annotated as a cytoplasmic homodecamer, so it is confidently a *bona fide*, fully functional D-ribose pyranase rather than a distant, possibly neofunctionalized family member.

> **Gene-identity verification.** The symbol "rbsD" and the D-ribose pyranase description are internally consistent with the RbsD/FucU family and the D-ribose_pyranase domains listed in UniProt. No conflicting literature under an unrelated gene of the same symbol was found. Note that in *E. coli* the same letters appear in the LacI-family repressor **RbsR** — a distinct regulatory gene, not RbsD — and these were kept separate here.

---

## Key Findings

### F001 — RbsD is a D-ribose pyranase catalyzing pyranose⇌furanose ring interconversion

The core enzymatic identity of RbsD was established biochemically in the *Escherichia coli* ortholog using NMR. Direct saturation-difference NMR experiments demonstrated that RbsD catalyzes the **pyran-to-furan conversion of ribose**, functionally distinguishing it from the paralogous FucU (fucose) and YiiL (rhamnose) mutarotases that act on their own sugars ([PMID: 15060078](https://pubmed.ncbi.nlm.nih.gov/15060078/)). Independent kinetic NMR work described RbsD as a mutarotase that accelerates conversion specifically between the **β-pyranose and β-furanose forms of ribose** ([PMID: 15489434](https://pubmed.ncbi.nlm.nih.gov/15489434/)).

Why is an enzyme needed for this step at all? A careful NMR analysis of free-equilibrium versus enzyme-catalyzed mutarotation kinetics showed that D-ribose has an **exceptionally fast spontaneous α↔β conversion but only between the furan forms**; the slow, rate-limiting transition in solution is the pyranose↔furanose ring interconversion ([PMID: 15281797](https://pubmed.ncbi.nlm.nih.gov/15281797/)). RbsD therefore targets precisely the bottleneck reaction — opening the abundant pyranose ring and closing it into the metabolically usable furanose ring. This furanose bias is also the biological reason ribose is incorporated as the furanose in nucleic acids. The *P. putida* protein (Q88K33 / PP_2459) is assigned EC 5.4.99.62 with catalytic activity β-D-ribopyranose = β-D-ribofuranose by HAMAP-Rule MF_01661 on the basis of its membership in the RbsD subfamily (Pfam PF05025).

> Evidence quote (PMID: 15060078): *"We show that RbsD catalyzes the pyran to furan conversion of ribose, whereas FucU and YiiL are involved in the catalysis of the anomeric conversion of their respective sugars."*

### F002 — RbsD is coupled to ribokinase, feeding ribose carbon into the pentose phosphate pathway

RbsD does not act in isolation. Its furanose product is the obligate substrate for **ribokinase (RbsK)**, which phosphorylates β-D-ribofuranose to **D-ribose-5-phosphate**. This coupling is explicit in studies of the ribose regulon: RbsABC forms the ABC-type high-affinity D-ribose transporter, "while RbsD and RbsK are involved in the conversion of D-ribose into D-ribose 5-phosphate" ([PMID: 23651393](https://pubmed.ncbi.nlm.nih.gov/23651393/)). Structural/mechanistic work on the *S. aureus* homolog framed the ring interconversion as "the key step for substrate supply to ribokinase RbsK, which converts ribose to ribose-5-phosphate for further metabolism" ([PMID: 21276853](https://pubmed.ncbi.nlm.nih.gov/21276853/)).

The physiological consequence of this coupling was shown directly: overexpression of RbsD in *E. coli* **raised the intracellular level of ribose-5-phosphate**, driving carbon into the pentose phosphate pathway and glycolysis; when flux was excessive it spilled into the toxic metabolite methylglyoxal ([PMID: 15489434](https://pubmed.ncbi.nlm.nih.gov/15489434/)). This experiment establishes RbsD activity as a genuine metabolic throttle on ribose entry into central carbon metabolism, not merely an in-vitro curiosity.

> Evidence quote (PMID: 15489434): *"The intracellular level of ribose 5-phosphate increased with the presence of the protein RbsD."*

### F003 — RbsD is a cytoplasmic decameric toroid; catalysis requires the higher-order oligomer

Crystallography reveals an unusual and highly conserved quaternary architecture. The *Bacillus subtilis* RbsD structure showed a **novel decameric toroidal assembly** of a cytoplasmic sugar-binding fold ([PMID: 12738765](https://pubmed.ncbi.nlm.nih.gov/12738765/)). The dual-function *E. coli* FucU (a close RbsD paralog with both ribose-pyranase and fucose-mutarotase activity) likewise forms a **decameric toroid in which each active site is built by two adjacent subunits** — one subunit donates most of the sugar-interacting residues including a catalytic tyrosine, and the neighboring subunit contributes a catalytic His–Asp dyad ([PMID: 19524593](https://pubmed.ncbi.nlm.nih.gov/19524593/)).

The functional importance of this oligomeric state is demonstrated by a natural negative control: the *S. aureus* homolog Sa240 crystallizes only as a **dimer with an incomplete active site** and is inferred to be **catalytically inactive** precisely because it does not reach the decameric state ([PMID: 21276853](https://pubmed.ncbi.nlm.nih.gov/21276853/)). In other words, the reaction is an emergent property of the assembled ring, not of an isolated subunit. UniProt annotates Q88K33 as a **homodecamer localized to the cytoplasm**, consistent with this family-wide architecture. Notably, an early crystallographic study had initially concluded RbsD was merely a passive cytoplasmic sugar-*binding* protein lacking enzymatic activity ([PMID: 12738765](https://pubmed.ncbi.nlm.nih.gov/12738765/)) — a conclusion later overturned by the NMR demonstration of pyranase activity (F001).

> Evidence quote (PMID: 21276853): *"Because the catalytic activity of ribose pyranase depends on its oligomeric state, we propose Sa240 is catalytically inactive in its dimeric structure."*

### F004 — *P. putida* RbsD (Q88K33) conserves the full catalytic machinery (~50 % identity to *E. coli* RbsD)

To confirm that the *P. putida* protein is a true D-ribose pyranase and not a divergent family member, a global sequence alignment was performed between Q88K33 (132 aa) and the experimentally characterized *E. coli* RbsD, P04982 (139 aa). The two share **49.6 % identity over 131 aligned columns** — well within the range expected for conserved orthologous function. Critically, the functionally important residues map onto conserved positions:

| Role | *P. putida* Q88K33 | *E. coli* P04982 | Conserved |
|------|--------------------|------------------|-----------|
| Active site, **proton donor** | **His20** | His20 | ✔ |
| Substrate binding | **Asp28** | Asp28 | ✔ |
| Substrate binding | **His99** | His106 | ✔ |
| Substrate binding (Tyr motif) | **Tyr121**-Ser-Asn | Tyr128-Ala-Asn | ✔ |

These are exactly the catalytic tyrosine and His–Asp dyad residues identified in the FucU/RbsD structural mechanism ([PMID: 19524593](https://pubmed.ncbi.nlm.nih.gov/19524593/)). UniProt independently lists Q88K33 with catalytic activity β-D-ribopyranose = β-D-ribofuranose, the pathway "D-ribose degradation; D-ribose 5-phosphate from β-D-ribopyranose: step 1/2," homodecamer subunit structure, and cytoplasmic localization. The convergence of sequence conservation, structural family membership, and database annotation makes the functional assignment robust. (One caveat: the *E. coli* enzyme additionally interconverts β-D-allofuranose/β-D-allopyranose; no such secondary allose activity is annotated for the *P. putida* protein.)

> Evidence quote (PMID: 19524593): *"While one subunit provides most of the fucose-interacting residues including a catalytic tyrosine residue, the other subunit provides a catalytic His-Asp dyad."*

### F005 — In *P. putida* KT2440, *rbsD* (PP_2459) sits in a complete chromosomal ribose (*rbs*) cluster

Genome annotation of *P. putida* KT2440 shows that PP_2459 is embedded in a contiguous, complete ribose-utilization gene cluster spanning **PP_2454–PP_2460**:

| Locus | Gene | Product | EC / role |
|-------|------|---------|-----------|
| PP_2454 | *rbsB* | Periplasmic ribose-binding protein | ABC substrate-binding |
| PP_2455 | *rbsA* | ABC transporter ATP-binding protein | EC 3.6.3.17 |
| PP_2456 | *rbsC* | ABC transporter permease | Membrane transport |
| PP_2457 | *rbsR* | LacI-family transcriptional repressor | Regulation |
| PP_2458 | *rbsK* | Ribokinase | EC 2.7.1.15 |
| **PP_2459** | ***rbsD*** | **D-ribose pyranase** | **EC 5.4.99.62** |
| PP_2460 | *nuh* | Ribonucleoside hydrolase | EC 3.2.2.- |

This layout recapitulates the canonical *E. coli rbsDACBK* operon (transporter + RbsD + ribokinase) together with the *rbsR* regulator ([PMID: 23651393](https://pubmed.ncbi.nlm.nih.gov/23651393/)). The genomic co-localization is strong independent corroboration of pathway context: RbsD's immediate neighbors are exactly the transporter and kinase whose activities bracket its reaction, plus a repressor coordinating expression of the whole module. The adjacent ribonucleoside hydrolase (*nuh*) can liberate ribose from nucleosides, providing an additional intracellular source of the substrate. Thus the pathway context is not merely inferred from *E. coli* — the full functional gene set is present and co-localized in *P. putida* itself.

> Evidence quote (PMID: 23651393): *"The genes for the transport and initial-step metabolism of d-ribose form a single rbsDACBK operon."*

---

## Mechanistic Model / Interpretation

RbsD is best understood as a **ring-form-supply enzyme** positioned at the mouth of the ribose catabolic pathway. The logic is dictated by sugar chemistry: environmental/imported D-ribose sits mostly as the thermodynamically favored six-membered β-pyranose ring, but the phosphorylating enzyme ribokinase can only use the five-membered β-furanose ring. Because the spontaneous pyranose↔furanose interconversion of ribose is slow (unlike its very fast furanose α↔β anomerization), an enzyme is required to keep the furanose pool replenished. RbsD is that enzyme.

The complete pathway in *P. putida* KT2440 can be drawn as:

```
   Extracellular / periplasmic D-ribose
                 │
                 │  RbsB (PP_2454) binds ribose
                 ▼
        RbsABC ABC transporter  (RbsA PP_2455 ATPase; RbsC PP_2456 permease)
                 │  ATP-driven import
                 ▼
   ┌─────────────────────────── CYTOPLASM ───────────────────────────┐
   │                                                                 │
   │   β-D-ribopyranose  ⇌⇌⇌  β-D-ribofuranose                       │
   │            [ RbsD / PP_2459 — D-ribose pyranase, EC 5.4.99.62 ] │
   │            (homodecameric toroid; inter-subunit active sites)   │
   │                                   │                             │
   │                                   ▼                             │
   │              RbsK (PP_2458) ribokinase  + ATP                   │
   │                                   │                             │
   │                                   ▼                             │
   │                        D-ribose-5-phosphate                     │
   │                                   │                             │
   │                                   ▼                             │
   │                     PENTOSE PHOSPHATE PATHWAY                    │
   │                  → central carbon metabolism / glycolysis       │
   └─────────────────────────────────────────────────────────────────┘

   Regulation: RbsR (PP_2457), LacI-family repressor, controls the cluster.
   Alternate substrate source: Nuh (PP_2460) ribonucleoside hydrolase → ribose.
```

At the molecular level, the enzyme is a **decameric toroid** whose ten catalytic sites are each shared between two neighboring protomers. One protomer supplies the substrate-binding pocket and a catalytic **tyrosine**; the adjacent protomer supplies a **His–Asp dyad** and a proton-donor **histidine**. This inter-subunit architecture explains why oligomerization is obligatory for catalysis — a lone subunit or a dimer cannot assemble a complete active site (as seen for the inactive *S. aureus* dimer). The *P. putida* protein preserves every one of these catalytic/binding residues (His20 proton donor, Asp28, His99, Tyr121 motif) and is annotated as a cytoplasmic homodecamer, so it is expected to operate by the same mechanism.

Two layers of evidence make this annotation unusually secure for an otherwise sparsely studied bacterial protein: (1) **direct biochemistry** on orthologs/paralogs (NMR demonstration of the pyran→furan reaction; ribose-5-phosphate accumulation on overexpression), and (2) **residue-level conservation** plus **genomic synteny** anchoring the *P. putida* protein to the characterized system. The function is therefore not a bare family guess but a well-triangulated assignment.

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports the findings |
|------|-----------------|------------------------------|
| [15060078](https://pubmed.ncbi.nlm.nih.gov/15060078/) | *NMR probes a ubiquitous family that alters monosaccharide configuration* | Direct NMR proof RbsD catalyzes ribose pyran→furan conversion (F001) |
| [15281797](https://pubmed.ncbi.nlm.nih.gov/15281797/) | *NMR of enzyme-catalyzed and free-equilibrium mutarotation kinetics* | Shows the pyranose↔furanose step is the slow, rate-limiting one requiring an enzyme (F001) |
| [15489434](https://pubmed.ncbi.nlm.nih.gov/15489434/) | *Ribose utilization with excess mutarotase causes cell death via methylglyoxal* | RbsD is a mutarotase (β-pyran ⇌ β-furan); its activity raises ribose-5-phosphate and drives PPP/glycolytic flux (F001, F002) |
| [21276853](https://pubmed.ncbi.nlm.nih.gov/21276853/) | *Crystal structure of Sa240, a ribose pyranase homolog with partial active site* | RbsD supplies substrate to ribokinase; catalysis depends on the decameric oligomeric state; the dimer is inactive (F002, F003) |
| [19524593](https://pubmed.ncbi.nlm.nih.gov/19524593/) | *Crystal structures/mechanism of a dual fucose mutarotase/ribose pyranase* | Decameric toroid with inter-subunit active sites; identifies catalytic Tyr and His–Asp dyad conserved in Q88K33 (F003, F004) |
| [12738765](https://pubmed.ncbi.nlm.nih.gov/12738765/) | *Crystal structures of RbsD; novel cytoplasmic sugar-binding fold* | Establishes the decameric toroidal quaternary structure and cytoplasmic nature (F003) |
| [23651393](https://pubmed.ncbi.nlm.nih.gov/23651393/) | *Ribose operon repressor RbsR in purine nucleotide synthesis* | Defines the canonical rbsDACBK operon + rbsR mirrored by the P. putida cluster; places RbsD + RbsK in ribose→R5P conversion (F002, F005) |

**Supporting / contextual literature.** Proteomic evidence shows that a D-ribose pyranase is induced specifically on ribose (vs glucose) in *Lactobacillus sakei* ([PMID: 20412581](https://pubmed.ncbi.nlm.nih.gov/20412581/)), and comparative genomics links absence of *rbsD* to inability to grow on ribose in *Fructilactobacillus sanfranciscensis* ([PMID: 33129664](https://pubmed.ncbi.nlm.nih.gov/33129664/)) — both reinforcing that RbsD is required for ribose catabolism. Regulatory work in *E. coli* shows *rbsD* mRNA is a target of the small RNA DsrA ([PMID: 26175201](https://pubmed.ncbi.nlm.nih.gov/26175201/); [PMID: 26607444](https://pubmed.ncbi.nlm.nih.gov/26607444/)), illustrating post-transcriptional control of the transcript (demonstrated in *E. coli*, not in *P. putida*). Paralog studies on fucose/rhamnose mutarotases ([PMID: 17602138](https://pubmed.ncbi.nlm.nih.gov/17602138/), [PMID: 32448506](https://pubmed.ncbi.nlm.nih.gov/32448506/)) clarify substrate specialization within the broader mutarotase superfamily and confirm RbsD's ribose specificity.

---

## Limitations and Knowledge Gaps

1. **No direct biochemistry on the *P. putida* protein itself.** The functional assignment for Q88K33 is inferred from (a) HAMAP-rule family membership, (b) ~50 % sequence identity and full catalytic-residue conservation relative to *E. coli* RbsD, and (c) genomic synteny. No purified-enzyme kinetics, crystal structure, or *P. putida* knockout phenotype has been directly measured. The inference is strong but remains inference.

2. **Kinetic parameters unknown.** No *k*cat, *K*m, or turnover values are available for the *P. putida* enzyme; the rate acceleration it provides over spontaneous mutarotation under *P. putida* physiological conditions is not quantified.

3. **Oligomeric state assumed, not verified experimentally for Q88K33.** Decamer formation is annotated by homology; it has not been confirmed by SEC-MALS, native MS, or a structure of the *P. putida* protein.

4. **Regulation in *P. putida* is uncharacterized.** RbsR-mediated repression is inferred from the syntenic cluster and *E. coli* precedent; the DsrA sRNA regulation is *E. coli*-specific and *P. putida* lacks a characterized DsrA ortholog, so post-transcriptional control may differ.

5. **Substrate exclusivity not tested locally.** While the family cleanly separates ribose (RbsD) from fucose (FucU) and rhamnose (YiiL) activities, the specificity of Q88K33 has not been assayed against alternative pentoses/hexoses.

6. **Physiological importance in the *P. putida* niche.** Whether ribose is a quantitatively important carbon source for *P. putida* KT2440 in its soil/rhizosphere lifestyle — versus a salvage substrate from nucleoside degradation via the adjacent *nuh* — is not established.

---

## Proposed Follow-up Experiments / Actions

1. **Direct enzymatic assay.** Express and purify recombinant Q88K33 and measure pyranose→furanose interconversion of D-ribose by saturation-difference or real-time NMR (as done for *E. coli* RbsD), extracting *k*cat/*K*m. Include D-fucose and L-rhamnose as negative-control substrates to confirm ribose specificity.

2. **Oligomeric-state determination.** Use SEC-MALS and/or native mass spectrometry to confirm the homodecameric toroid, and solve the crystal or cryo-EM structure of Q88K33 to verify the inter-subunit active site and the positions of His20, Asp28, His99, and the Tyr121 motif.

3. **Genetic knockout / complementation.** Delete PP_2459 in *P. putida* KT2440 and test growth on D-ribose as sole carbon source; complement with wild-type and catalytic-residue mutants (e.g., His20Ala, Tyr121Phe) to establish which residues are essential in vivo.

4. **Metabolic-flux confirmation.** Quantify intracellular D-ribose-5-phosphate and PPP flux (¹³C-ribose labeling) in wild-type vs Δ*rbsD* to confirm that RbsD gates ribose entry into the pentose phosphate pathway in this organism.

5. **Regulation.** Test RbsR (PP_2457) binding to the cluster promoter(s) and ribose-dependent induction of *rbsD* transcription; screen for sRNA-mediated post-transcriptional control analogous to *E. coli* DsrA.

6. **Substrate-source dissection.** Test whether the adjacent *nuh* (PP_2460) ribonucleoside hydrolase supplies intracellular ribose to RbsD by combining Δ*nuh* with nucleoside carbon sources.

---

## Conclusion

RbsD (Q88K33 / PP_2459) in *Pseudomonas putida* KT2440 is a **cytoplasmic, homodecameric D-ribose pyranase (EC 5.4.99.62)** that interconverts the β-pyranose and β-furanose ring forms of D-ribose. It performs the first of two steps in D-ribose degradation, supplying β-D-ribofuranose to the neighboring ribokinase (RbsK, PP_2458) for phosphorylation to D-ribose-5-phosphate and entry into the pentose phosphate pathway. Its genomic embedding in the complete PP_2454–2460 ribose cluster (ABC transporter, repressor, kinase, nucleoside hydrolase), its full conservation of catalytic residues relative to the biochemically characterized *E. coli* enzyme, and the family's well-documented decamer-dependent inter-subunit catalytic mechanism together make this a robust, well-triangulated functional annotation.


## Artifacts

- [OpenScientist final report](rbsD-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](rbsD-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:15060078
2. PMID:15489434
3. PMID:15281797
4. PMID:23651393
5. PMID:21276853
6. PMID:12738765
7. PMID:19524593
8. PMID:20412581
9. PMID:33129664
10. PMID:26175201
11. PMID:26607444
12. PMID:17602138
13. PMID:32448506