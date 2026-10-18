---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T09:53:41.660912'
end_time: '2026-09-01T10:06:17.341107'
duration_seconds: 755.68
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: dapB
  gene_symbol: dapB
  uniprot_accession: Q88DU4
  protein_description: 'RecName: Full=4-hydroxy-tetrahydrodipicolinate reductase {ECO:0000255|HAMAP-Rule:MF_00102};
    Short=HTPA reductase {ECO:0000255|HAMAP-Rule:MF_00102}; EC=1.17.1.8 {ECO:0000255|HAMAP-Rule:MF_00102};'
  gene_info: Name=dapB {ECO:0000255|HAMAP-Rule:MF_00102}; OrderedLocusNames=PP_4725;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the DapB family. {ECO:0000255|HAMAP-
  protein_domains: DapB_C. (IPR022663); DapB_N. (IPR000846); DapB_N_CS. (IPR022664);
    DHDPR_bac. (IPR023940); NAD(P)-bd_dom_sf. (IPR036291)
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
citation_count: 9
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: dapB-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: dapB-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88DU4
- **Protein Description:** RecName: Full=4-hydroxy-tetrahydrodipicolinate reductase {ECO:0000255|HAMAP-Rule:MF_00102}; Short=HTPA reductase {ECO:0000255|HAMAP-Rule:MF_00102}; EC=1.17.1.8 {ECO:0000255|HAMAP-Rule:MF_00102};
- **Gene Information:** Name=dapB {ECO:0000255|HAMAP-Rule:MF_00102}; OrderedLocusNames=PP_4725;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the DapB family. {ECO:0000255|HAMAP-
- **Key Domains:** DapB_C. (IPR022663); DapB_N. (IPR000846); DapB_N_CS. (IPR022664); DHDPR_bac. (IPR023940); NAD(P)-bd_dom_sf. (IPR036291)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "dapB" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'dapB' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **dapB** (gene ID: dapB, UniProt: Q88DU4) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *dapB* (Q88DU4, PP_4725) in *Pseudomonas putida* KT2440

**Gene:** *dapB* (OrderedLocusName **PP_4725**)
**Protein:** 4-hydroxy-tetrahydrodipicolinate reductase (HTPA reductase; historically "dihydrodipicolinate reductase", DHDPR)
**UniProt:** Q88DU4 · **EC:** 1.17.1.8 · **Length:** 267 aa · **Family:** DapB family (HAMAP MF_00102)

## Summary

The gene **dapB** (ordered locus **PP_4725**; UniProt **Q88DU4**) of *Pseudomonas putida* strain KT2440 encodes **4-hydroxy-tetrahydrodipicolinate reductase** (HTPA reductase, historically "dihydrodipicolinate reductase"/DHDPR; **EC 1.17.1.8**). This is a **soluble, cytoplasmic, NAD(P)H-dependent oxidoreductase** that catalyzes the **fourth step** of the diaminopimelate (DAP) branch of L-lysine biosynthesis. Its physiological reaction is the reduction of **(2S,4S)-4-hydroxy-2,3,4,5-tetrahydrodipicolinate (HTPA)** — the product of the upstream enzyme DapA (dihydrodipicolinate synthase, DHDPS) — to **(S)-2,3,4,5-tetrahydrodipicolinate**, consuming NADH or NADPH as the hydride donor. The enzyme is notable for its ability to use **both** reduced pyridine nucleotide cofactors, a property conserved across the DapB family.

The functional assignment rests on a convergent, mutually reinforcing body of evidence: (1) UniProt/HAMAP rule-based annotation (MF_00102) placing Q88DU4 firmly in the DapB family; (2) a two-domain architecture — an N-terminal Rossmann dinucleotide-binding domain and a C-terminal substrate-binding domain — matched to InterPro DapB_N/DapB_C signatures and to solved ortholog structures that assemble as homotetramers; (3) **65% amino-acid sequence identity** to the mechanistically characterized *Escherichia coli* DapB, with **strict conservation of the catalytic His/Lys pair** and the glycine-rich dinucleotide-binding fingerprint; (4) NMR identification of the true substrate HTPA as the DapA product, which resolved a decades-old misnaming of the enzyme; and (5) complete genomic pathway context in KEGG ppu00300, where PP_4725 sits within an intact **succinylase-branch** DAP pathway alongside DapA, DapD, DapC, DapE, DapF and LysA.

Functionally, DapB occupies a committed position in a pathway that supplies two indispensable products: **meso-diaminopimelate (m-DAP)**, the cross-linking amino acid of the Gram-negative peptidoglycan cell wall, and **L-lysine** for protein synthesis. Because humans lack the genetic machinery to synthesize DAP or lysine de novo, and because *dapB* is essential in numerous pathogens, the enzyme is a well-validated, selective **antibacterial drug target**. No experimental studies of the *P. putida* enzyme itself were located; the annotation is therefore an orthology-based inference of very high confidence, anchored by direct experimental work on close homologs (*E. coli*, *M. tuberculosis*, *V. vulnificus*, *C. glutamicum*).

---

## Key Findings

### F001 — *dapB* encodes HTPA reductase (EC 1.17.1.8), the fourth step of the DAP pathway

UniProt Q88DU4 (267 aa, *P. putida* KT2440) is annotated with the FUNCTION "Catalyzes the conversion of 4-hydroxy-tetrahydrodipicolinate (HTPA) to tetrahydrodipicolinate." The catalytic activity is written for both cofactors:

> (S)-2,3,4,5-tetrahydrodipicolinate + NAD(P)⁺ + H₂O ⇌ (2S,4S)-4-hydroxy-2,3,4,5-tetrahydrodipicolinate + NAD(P)H + H⁺

The physiological direction is HTPA **reduction** (i.e. HTPA + NAD(P)H → tetrahydrodipicolinate). The pathway annotation places it precisely: "L-lysine biosynthesis via DAP pathway; (S)-tetrahydrodipicolinate from L-aspartate: **step 4/4**." The assignment is made through HAMAP-Rule MF_00102, which defines the DapB family.

The reaction is mechanistically characterized in orthologs. Pote et al. (2021) state directly that "DapB catalyzes the conversion of (2S, 4S)-4-hydroxy-2,3,4,5-tetrahydrodipicolinate (HTPA) to 2,3,4,5-tetrahydrodipicolinate in an NADH/NADPH dependent reaction" [PMID: 32980502](https://pubmed.ncbi.nlm.nih.gov/32980502/). This defines the exact substrate, product, and cofactor usage that matches the UniProt function of Q88DU4.

### F002 — Cytoplasmic, two-domain NAD(P)H oxidoreductase that assembles into a homotetramer

UniProt places the protein in the **cytoplasm** — consistent with a soluble metabolic enzyme with no signal peptide or membrane-spanning segments. The sequence begins **MRRIAVMGAAGRMGK**, containing the canonical glycine-rich dinucleotide-binding fingerprint (binding-site residues ~8–13 contacting NAD(H)). Predicted active-site residues include position **155** (proton donor/acceptor) and **159** (proton donor), with substrate-contacting residues at 156 and 165–166. The domain architecture matches InterPro **DapB_N (IPR000846)**, **DapB_C (IPR022663)**, and the **NAD(P)-binding domain superfamily (IPR036291)**.

Structural work on orthologs establishes both the fold and the quaternary structure. Scapin et al. (1995) showed the *E. coli* enzyme "is composed of two domains" — a dinucleotide-binding domain (a seven-stranded parallel β-sheet plus four helices) and a second β-sandwich substrate-binding domain — and that "dihydrodipicolinate reductase uses both NADH and NADPH as cofactors" [PMID: 7893645](https://pubmed.ncbi.nlm.nih.gov/7893645/). Sagong & Kim (2016) confirmed the same functional division of labor in the *Corynebacterium glutamicum* enzyme: "The N-terminal domain mainly contributes to nucleotide binding, whereas the C-terminal domain is involved in substrate binding" [PMID: 26502738](https://pubmed.ncbi.nlm.nih.gov/26502738/). Both orthologs are homotetramers that accept either reduced nucleotide — properties that transfer to Q88DU4 given its shared domain signatures and high sequence identity.

### F003 — Feeds the meso-DAP/L-lysine branch point; pathway is human-absent, making DapB a validated antibacterial target

The products of the DAP/lysine pathway are physiologically indispensable. Triassi et al. (2014) note that "the penultimate lys precursor meso-DAP (m-DAP) is a cross-linking amino acid in the peptidoglycan (PG) cell wall of most Gram-negative bacteria and lys plays a similar role in the PG of most Gram-positive bacteria" [PMID: 25309529](https://pubmed.ncbi.nlm.nih.gov/25309529/). *P. putida* is Gram-negative, so m-DAP is used directly for cell-wall cross-linking, and L-lysine is drawn off for protein synthesis.

Critically, this pathway is absent from humans: "human genomes do not possess the genes necessary to synthesize these amino acids de novo" [PMID: 25309529](https://pubmed.ncbi.nlm.nih.gov/25309529/), establishing the basis for selective toxicity. *dapB* itself is essential and druggable — Paiva et al. (2001) screened "dihydrodipicolinate reductase, the essential gene product of *dapB*" for inhibitors in *Mycobacterium tuberculosis*, and found inhibitors competitive with the dipicolinate substrate [PMID: 11342032](https://pubmed.ncbi.nlm.nih.gov/11342032/). Pote et al. (2021) reinforce that genes coding for DapBs are essential in many pathogenic bacteria [PMID: 32980502](https://pubmed.ncbi.nlm.nih.gov/32980502/).

### F004 — The physiological substrate is HTPA, the NMR-verified DapA product — justifying the modern enzyme name

For decades the enzyme was called "dihydrodipicolinate reductase," implying that its substrate was dihydrodipicolinate. This was corrected when the true product of the upstream synthase (DapA/DHDPS) was identified. Blickling et al. (1997) combined X-ray crystallography and NMR on *E. coli* DHDPS and, by NMR, showed that "**(4S)-4-hydroxy-2,3,4,5-tetrahydro-(2S)-dipicolinic acid is identified as the only product**" [PMID: 8993314](https://pubmed.ncbi.nlm.nih.gov/8993314/). This species is **HTPA** — the direct substrate of DapB. The finding justified the reclassification of the enzyme to **4-hydroxy-tetrahydrodipicolinate reductase (EC 1.17.1.8)**, the name now carried by Q88DU4, and is fully consistent with Pote et al.'s description of DapB acting on (2S,4S)-HTPA [PMID: 32980502](https://pubmed.ncbi.nlm.nih.gov/32980502/).

### F005 — Complete succinylase-branch DAP pathway; DapB confirmed in-pathway by genomic context

KEGG pathway ppu00300 (Lysine biosynthesis, *P. putida* KT2440) lists a full, ordered enzyme set that places PP_4725 unambiguously within an operational pathway:

| Step | Enzyme | Gene(s) / locus | EC |
|------|--------|-----------------|----|
| 1 | Aspartokinase | *lysC* / PP_4473 | 2.7.2.4 |
| 2 | Aspartate-semialdehyde dehydrogenase | *asd* / PP_1989 | 1.2.1.11 |
| 3 | HTPA synthase (DHDPS) | *dapA* / PP_1237, PP_2639, PP_2036 | 4.3.3.7 |
| **4** | **HTPA reductase (DHDPR)** | ***dapB* / PP_4725** | **1.17.1.8** |
| 5 | THDP N-succinyltransferase | *dapD* / PP_1530 | 2.3.1.117 |
| 6 | N-succinyl-DAP aminotransferase | *dapC* / PP_1588 | 2.6.1.17 |
| 7 | Succinyl-diaminopimelate desuccinylase | *dapE* / PP_1525 | 3.5.1.18 |
| 8 | Diaminopimelate epimerase | *dapF* / PP_5228, PP_3790 | 5.1.1.7 |
| 9 | Diaminopimelate decarboxylase | *lysA* / PP_2077, PP_5227 | 4.1.1.20 |
| — | m-DAP → peptidoglycan | *murE* / PP_1332 | 6.3.2.13 |

The presence of *dapD*, *dapC*, and *dapE* identifies the **succinylase variant** of the DAP pathway. No *dapL* (LL-DAP aminotransferase) or *ddh* (meso-DAP dehydrogenase) shortcut is annotated in KT2440, so DapB's product must flow through the succinylase branch to reach m-DAP and lysine. This full pathway context corroborates the DapB assignment: an isolated reductase would be functionally meaningless, but PP_4725 sits between DapA (its substrate producer) and DapD (its product consumer).

### F006 — 65% identity to mechanistically characterized *E. coli* DapB with strict conservation of catalytic residues

A global Needleman–Wunsch alignment (own analysis) of Q88DU4 (267 aa) versus *E. coli* DapB (P04036, 273 aa) gives **174/267 = 65.2% identity** over aligned positions. The functionally critical residues are strictly conserved:

- **Catalytic His/Lys pair:** the predicted proton donor/acceptor His155(ppu) = His159(Eco), and proton donor Lys159(ppu) = Lys163(Eco) — the catalytic pair of *E. coli* DHDPR — plus His156(ppu) = His160(Eco).
- **Rossmann fingerprint:** the N-terminal glycine-rich motif (G8/A9/G11/R12/M13 → G12/A13/G15/R16/M17 in *E. coli*).
- **Substrate/cofactor-contact residues:** ppu 98–100 (GTT), 122–125 (AANF), and 165–166 (GT) are all conserved.

Because the DapB catalytic mechanism and the His/Lys pair are experimentally defined in orthologs — Pote et al. (2021), who report "the first...detailed mechanism of reaction catalyzed by DapB" [PMID: 32980502](https://pubmed.ncbi.nlm.nih.gov/32980502/), and Scapin et al. (1995) [PMID: 7893645](https://pubmed.ncbi.nlm.nih.gov/7893645/) — this high identity plus strict active-site conservation allows the mechanism to be transferred to the *P. putida* enzyme with high confidence.

---

## Mechanistic Model / Interpretation

DapB catalyzes a single, well-defined redox step in a linear biosynthetic conduit. The following schematic places it in context:

```
  L-Aspartate
      │  lysC (aspartokinase, PP_4473)
      ▼
  L-Aspartyl-4-phosphate
      │  asd (ASA dehydrogenase, PP_1989)
      ▼
  L-Aspartate-4-semialdehyde
      │  dapA (DHDPS / HTPA synthase, PP_1237…)  + pyruvate
      ▼
  (2S,4S)-HTPA  ◄── the substrate of DapB
      │
      │  ┌─────────────────────────────────────────────┐
      └──┤  dapB (HTPA reductase, PP_4725)              │
         │  HTPA + NAD(P)H + H⁺ → THDP + NAD(P)⁺ + H₂O  │
         │  Cytoplasm · homotetramer · His/Lys catalysis │
         └─────────────────────────────────────────────┘
      ▼
  (S)-2,3,4,5-Tetrahydrodipicolinate (THDP)
      │  dapD → dapC → dapE  (SUCCINYLASE BRANCH)
      ▼
  LL-Diaminopimelate
      │  dapF (epimerase, PP_5228/PP_3790)
      ▼
  meso-Diaminopimelate (m-DAP) ──► murE ──► PEPTIDOGLYCAN cross-links
      │  lysA (DAP decarboxylase, PP_2077/PP_5227)
      ▼
  L-LYSINE ──► protein synthesis
```

At the molecular level, DapB is a homotetramer of two-domain subunits. The **N-terminal Rossmann domain** binds the reduced nicotinamide cofactor (NADH or NADPH — the enzyme is promiscuous for the 2′-phosphate), positioning the C4 hydride donor of the dihydronicotinamide ring adjacent to the substrate. The **C-terminal β-sandwich domain** binds HTPA. On substrate/cofactor binding, the two domains close over the active-site cleft. A **conserved histidine** (His155 in the *P. putida* numbering) acts as the catalytic acid/base, and a nearby **conserved lysine** (Lys159) assists proton transfer, enabling stereospecific hydride transfer that reduces HTPA to (S)-2,3,4,5-tetrahydrodipicolinate. The dual-cofactor capability lets the enzyme draw on whichever pyridine nucleotide pool is available, buffering flux through this committed step under varying redox conditions.

The physiological logic is straightforward and non-pleiotropic: DapB exists to make THDP so the cell can produce m-DAP and lysine. In *P. putida*, a Gram-negative soil and rhizosphere organism, m-DAP is the direct cross-linking residue in peptidoglycan, and lysine is a proteinogenic amino acid. Loss of DapB function would be expected to be lethal (as in *E. coli* and *M. tuberculosis*) unless DAP/lysine were supplied exogenously, because KT2440 encodes no bypass (no *dapL*, no *ddh*) for this step.

A worthwhile distinction for *P. putida* specifically: this organism is a prolific **catabolizer** of lysine (via the aminovalerate and aminoadipate pathways [PMID: 16237033](https://pubmed.ncbi.nlm.nih.gov/16237033/); [PMID: 15150230](https://pubmed.ncbi.nlm.nih.gov/15150230/)) and interconverts D-/L-amino acids using racemases [PMID: 23995642](https://pubmed.ncbi.nlm.nih.gov/23995642/). Those catabolic activities are entirely separate from DapB, which is strictly **anabolic** (biosynthetic). The report's remit — the *primary* function — is the biosynthetic reductase role; the extensive lysine-catabolism literature for KT2440 concerns downstream fates of lysine, not DapB, and is noted here only to prevent conflation.

---

## Evidence Base

| PMID | Paper (organism) | How it supports the annotation |
|------|------------------|-------------------------------|
| [32980502](https://pubmed.ncbi.nlm.nih.gov/32980502/) | *Comparative structural and mechanistic studies of HTPA reductases from M. tuberculosis and V. vulnificus* | Defines the exact DapB reaction (HTPA → THDP, NADH/NADPH-dependent) and provides the first detailed catalytic mechanism; the conserved His/Lys pair it identifies is present in Q88DU4. Direct support for F001, F003, F006. |
| [7893645](https://pubmed.ncbi.nlm.nih.gov/7893645/) | *Three-dimensional structure of E. coli dihydrodipicolinate reductase* | Establishes the two-domain fold, homotetramer, and dual NADH/NADPH cofactor usage of the DapB family. Direct support for F002. |
| [26502738](https://pubmed.ncbi.nlm.nih.gov/26502738/) | *Structural insight into DHDPR from C. glutamicum* | Maps the functional roles of the N-terminal (nucleotide) and C-terminal (substrate) domains present in Q88DU4. Supports F002. |
| [8993314](https://pubmed.ncbi.nlm.nih.gov/8993314/) | *Reaction mechanism of E. coli DHDPS by X-ray/NMR* | NMR-identifies the DapA product as (4S)-4-hydroxy-tetrahydrodipicolinate (HTPA), proving DapB's true substrate and justifying the EC 1.17.1.8 name. Direct support for F004. |
| [25309529](https://pubmed.ncbi.nlm.nih.gov/25309529/) | *L,L-diaminopimelate aminotransferase (DapL): a putative narrow-spectrum antibacterial target* | Establishes the downstream role of m-DAP/lysine in peptidoglycan and the pathway's absence in humans (selective-toxicity rationale). Direct support for F003. |
| [11342032](https://pubmed.ncbi.nlm.nih.gov/11342032/) | *Inhibitors of DHDPR of M. tuberculosis* | Documents *dapB* essentiality and its status as a drug target with substrate-competitive inhibitors. Direct support for F003. |
| [23504110](https://pubmed.ncbi.nlm.nih.gov/23504110/) | *Lysine biosynthesis in microbes: relevance as drug target* | Reviews the meso-DAP pathway across bacteria and its drug-target relevance; contextualizes the DapB step. Supporting background. |
| [22783236](https://pubmed.ncbi.nlm.nih.gov/22783236/) | *DAP/lysine pathway in V. spinosum (DapL variant)* | Illustrates DapL/ddh pathway variants that *P. putida* lacks — reinforcing that KT2440 uses the succinylase branch. Contextual support for F005. |
| [16237033](https://pubmed.ncbi.nlm.nih.gov/16237033/) | *L-lysine catabolism in P. putida KT2440* | KT2440-specific; concerns catabolism (aminovalerate/aminoadipate), distinct from DapB's anabolic role. Used to avoid conflation. |
| [15150230](https://pubmed.ncbi.nlm.nih.gov/15150230/) | *davDT operon of P. putida (lysine catabolism)* | KT2440-specific lysine catabolism; not DapB. Contextual. |
| [23995642](https://pubmed.ncbi.nlm.nih.gov/23995642/) | *Amino acid racemization in P. putida KT2440* | KT2440 amino-acid metabolism context; racemases are separate from DapB. Contextual. |

The DapE-focused papers in the literature set ([40973684](https://pubmed.ncbi.nlm.nih.gov/40973684/), [25204745](https://pubmed.ncbi.nlm.nih.gov/25204745/), [24057071](https://pubmed.ncbi.nlm.nih.gov/24057071/)) concern a *different* downstream enzyme (the desuccinylase, step 7) and were reviewed to place DapB within the succinylase branch, not to annotate DapB directly.

**Coherence of the evidence:** No paper contradicts the annotation. The independent lines — HAMAP orthology, InterPro domain architecture, ortholog crystal structures, NMR substrate identification, sequence identity with strict active-site conservation, and complete genomic pathway context — all converge on the same conclusion. This is a textbook case of a highly confident, orthology-based functional assignment for a core primary-metabolism enzyme.

---

## Limitations and Knowledge Gaps

1. **No experimental characterization of the *P. putida* protein.** All enzymological, structural, and mechanistic data derive from orthologs (*E. coli*, *M. tuberculosis*, *V. vulnificus*, *C. glutamicum*). No purified-protein assay, crystal structure, kinetic parameters (kcat, Km for HTPA/NADH/NADPH), or cofactor-preference measurement exists specifically for Q88DU4. The annotation is a high-confidence inference, not a direct measurement.

2. **Catalytic residues are predicted, not experimentally validated in this ortholog.** The His155/Lys159 assignment rests on sequence alignment to *E. coli* plus UniProt feature prediction; no site-directed mutagenesis has been performed on the *P. putida* enzyme.

3. **Quaternary structure inferred.** The homotetramer state is assumed from orthologs; the oligomeric state of the *P. putida* enzyme has not been measured (e.g., by SEC-MALS or crystallography).

4. **Cofactor preference unquantified.** While the family uses both NADH and NADPH, the relative kcat/Km for the two cofactors in *P. putida* DapB is unknown and can vary between species.

5. **Essentiality is inferred, not demonstrated in KT2440.** *dapB* essentiality is documented in *M. tuberculosis* and *E. coli*; a knockout/conditional-depletion experiment in *P. putida* KT2440 has not been reported here, though the absence of any bypass pathway makes essentiality highly likely.

6. **Regulation unexplored.** Transcriptional/allosteric regulation of *dapB* in *P. putida* (e.g., feedback from lysine or coupling to peptidoglycan demand) was not investigated.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant expression and steady-state kinetics.** Clone PP_4725, purify the His-tagged protein, and measure kcat and Km for HTPA, NADH, and NADPH. This would directly confirm activity and quantify the dual-cofactor preference. HTPA is unstable, so couple the assay to purified *P. putida* DapA (PP_1237) generating HTPA in situ.

2. **Site-directed mutagenesis of the predicted catalytic pair.** Generate His155Ala and Lys159Ala variants and assay activity to validate the transferred mechanism experimentally in the *P. putida* enzyme.

3. **Structural determination.** Solve the crystal or cryo-EM structure of *P. putida* DapB, ideally as a ternary complex with NAD(P)⁺ and a substrate analog/inhibitor, to confirm the two-domain fold, tetrameric assembly, and active-site geometry.

4. **Genetic essentiality test.** Construct a conditional *dapB* mutant (or attempt a clean deletion with DAP/lysine supplementation) in KT2440 to demonstrate essentiality and confirm the absence of a functional bypass.

5. **Cofactor-usage under physiological redox states.** Given *P. putida*'s versatile central metabolism, measure how NADH/NADPH ratios in vivo influence DapB flux — relevant for metabolic-engineering efforts that use *P. putida* as a chassis.

6. **Inhibitor cross-testing.** Test substrate-competitive DHDPR inhibitors identified against *M. tuberculosis* DapB [PMID: 11342032](https://pubmed.ncbi.nlm.nih.gov/11342032/) on the *P. putida* enzyme to assess conservation of the druggable pocket, supporting broad-spectrum antibacterial development.

---

## Gene/Protein Identity Verification

The gene symbol *dapB* **matches** the protein described by UniProt Q88DU4. All independent evidence lines agree: (i) the organism is *Pseudomonas putida* KT2440 (Gram-negative), and PP_4725 is the annotated locus; (ii) the DapB/DHDPR family assignment (HAMAP MF_00102; InterPro DapB_N/DapB_C/DHDPR_bac) aligns with the literature retrieved; and (iii) the literature identified concerns the *same* enzyme family (HTPA reductase / dihydrodipicolinate reductase) in closely related bacteria, with 65% sequence identity to the mechanistically characterized *E. coli* ortholog. There was **no** ambiguity or cross-species symbol collision. The annotation is therefore made with high confidence for the correct gene product.


## Artifacts

- [OpenScientist final report](dapB-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](dapB-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:32980502
2. PMID:7893645
3. PMID:26502738
4. PMID:25309529
5. PMID:11342032
6. PMID:8993314
7. PMID:16237033
8. PMID:15150230
9. PMID:23995642