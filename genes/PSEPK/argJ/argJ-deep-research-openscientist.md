---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-17T17:22:54.945581'
end_time: '2026-07-17T17:45:44.719246'
duration_seconds: 1369.77
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: argJ
  gene_symbol: argJ
  uniprot_accession: P59612
  protein_description: 'RecName: Full=Arginine biosynthesis bifunctional protein ArgJ
    {ECO:0000255|HAMAP-Rule:MF_01106}; Includes: RecName: Full=Glutamate N-acetyltransferase
    {ECO:0000255|HAMAP-Rule:MF_01106}; EC=2.3.1.35 {ECO:0000255|HAMAP-Rule:MF_01106};
    AltName: Full=Ornithine acetyltransferase {ECO:0000255|HAMAP-Rule:MF_01106}; Short=OATase
    {ECO:0000255|HAMAP-Rule:MF_01106}; AltName: Full=Ornithine transacetylase {ECO:0000255|HAMAP-Rule:MF_01106};
    Includes: RecName: Full=Amino-acid acetyltransferase {ECO:0000255|HAMAP-Rule:MF_01106};
    EC=2.3.1.1 {ECO:0000255|HAMAP-Rule:MF_01106}; AltName: Full=N-acetylglutamate
    synthase {ECO:0000255|HAMAP-Rule:MF_01106}; Short=AGSase {ECO:0000255|HAMAP-Rule:MF_01106};
    Contains: RecName: Full=Arginine biosynthesis bifunctional protein ArgJ alpha
    chain {ECO:0000255|HAMAP-Rule:MF_01106}; Contains: RecName: Full=Arginine biosynthesis
    bifunctional protein ArgJ beta chain {ECO:0000255|HAMAP-Rule:MF_01106};'
  gene_info: Name=argJ {ECO:0000255|HAMAP-Rule:MF_01106}; OrderedLocusNames=PP_1346;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the ArgJ family. {ECO:0000255|HAMAP-
  protein_domains: Arg_biosynth_ArgJ. (IPR002813); ArgJ-like_dom_sf. (IPR016117);
    ArgJ_beta_C. (IPR042195); ArgJ (PF01960)
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
citation_count: 8
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: argJ-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: argJ-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** P59612
- **Protein Description:** RecName: Full=Arginine biosynthesis bifunctional protein ArgJ {ECO:0000255|HAMAP-Rule:MF_01106}; Includes: RecName: Full=Glutamate N-acetyltransferase {ECO:0000255|HAMAP-Rule:MF_01106}; EC=2.3.1.35 {ECO:0000255|HAMAP-Rule:MF_01106}; AltName: Full=Ornithine acetyltransferase {ECO:0000255|HAMAP-Rule:MF_01106}; Short=OATase {ECO:0000255|HAMAP-Rule:MF_01106}; AltName: Full=Ornithine transacetylase {ECO:0000255|HAMAP-Rule:MF_01106}; Includes: RecName: Full=Amino-acid acetyltransferase {ECO:0000255|HAMAP-Rule:MF_01106}; EC=2.3.1.1 {ECO:0000255|HAMAP-Rule:MF_01106}; AltName: Full=N-acetylglutamate synthase {ECO:0000255|HAMAP-Rule:MF_01106}; Short=AGSase {ECO:0000255|HAMAP-Rule:MF_01106}; Contains: RecName: Full=Arginine biosynthesis bifunctional protein ArgJ alpha chain {ECO:0000255|HAMAP-Rule:MF_01106}; Contains: RecName: Full=Arginine biosynthesis bifunctional protein ArgJ beta chain {ECO:0000255|HAMAP-Rule:MF_01106};
- **Gene Information:** Name=argJ {ECO:0000255|HAMAP-Rule:MF_01106}; OrderedLocusNames=PP_1346;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the ArgJ family. {ECO:0000255|HAMAP-
- **Key Domains:** Arg_biosynth_ArgJ. (IPR002813); ArgJ-like_dom_sf. (IPR016117); ArgJ_beta_C. (IPR042195); ArgJ (PF01960)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "argJ" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'argJ' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **argJ** (gene ID: argJ, UniProt: P59612) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: ArgJ (argJ / PP_1346, UniProt P59612) in *Pseudomonas putida* KT2440

**Gene:** argJ (Ordered Locus PP_1346) · **UniProt:** P59612 · **Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / KT2440)
**Protein:** Arginine biosynthesis bifunctional protein ArgJ · **Family:** ArgJ family (Pfam PF01960; InterPro IPR002813, IPR016117, IPR042195)

## Summary

**argJ** (ordered locus **PP_1346**; UniProt **P59612**) of *Pseudomonas putida* KT2440 encodes the **bifunctional arginine-biosynthesis protein ArgJ**, a cytoplasmic enzyme that is the central acetyl-group–handling catalyst of the arginine biosynthetic pathway. Its physiologically dominant activity is **ornithine acetyltransferase / glutamate N-acetyltransferase (OATase, EC 2.3.1.35)**: it transfers the acetyl group from **N²-acetyl-L-ornithine** onto **L-glutamate**, releasing free **L-ornithine** (the direct precursor of citrulline and arginine) while simultaneously regenerating **N-acetyl-L-glutamate**. This transacetylation is the fifth step of the "cyclic" (economical) arginine pathway and constitutes an internal **acetyl cycle** that conserves acetyl groups rather than hydrolyzing them, which distinguishes it from the "linear" pathway used by enteric bacteria such as *Escherichia coli*. The same enzyme active site additionally carries **N-acetylglutamate synthase (AGSase/NAGS, EC 2.3.1.1)** activity, an acetyl-CoA–dependent *de novo* synthesis of N-acetyl-L-glutamate that replenishes the cycle. This dual catalytic assignment is directly annotated in UniProt P59612 and supported by biochemical precedent from characterized bacterial ArgJ orthologs.

Mechanistically, ArgJ is an **N-terminal nucleophile (Ntn) hydrolase**. The 405-residue precursor **autoproteolytically self-cleaves at Ala188|Thr189** into an **α chain (residues 1–188)** and a **β chain (residues 189–405)**, exposing **Thr189** as the catalytic N-terminal nucleophile. The mature enzyme assembles as an **α₂β₂ heterotetramer** and runs catalysis through a **covalent acetyl-Thr189 (acyl-enzyme) intermediate** with **ping-pong bi-bi kinetics**, stabilized by an oxyanion hole formed by the conserved **Thr115/Gly116** pair. **L-ornithine acts as a feedback inhibitor** of the acetyl cycle, making it a key regulatory molecule.

For the specific *P. putida* KT2440 protein, direct enzymological data are not yet published, but the functional assignment is strongly supported by convergent in-silico and comparative evidence: (i) the P59612 sequence carries the **complete, family-conserved catalytic apparatus** (Thr189 nucleophile, Thr115/Gly116 oxyanion hole, and conserved substrate-binding residues); (ii) the **AlphaFold model AF-P59612-F1 is very high confidence** (mean pLDDT 96.5), reproducing the canonical ArgJ fold, with low confidence localized precisely to the flexible self-cleavage loop; and (iii) KEGG genome annotation places **argJ (PP_1346)** in the arginine-biosynthesis pathway (ppu00220) and ornithine-biosynthesis module (M00028) as a **standalone gene**, working alongside a **separate classical, arginine-feedback-regulated NAGS (argA, PP_5185)** that provides the primary regulated *de novo* N-acetylglutamate supply.

---

## Key Findings

### Finding 1 — ArgJ is a bifunctional acetyltransferase (EC 2.3.1.35 + EC 2.3.1.1)

UniProt P59612 annotates two distinct catalytic activities for this single gene product. The first is the **ornithine acetyltransferase (OATase) reaction** (EC 2.3.1.35, Rhea:15349):

> N²-acetyl-L-ornithine + L-glutamate → N-acetyl-L-glutamate + L-ornithine

The second is the **N-acetylglutamate synthase (AGSase/NAGS) reaction** (EC 2.3.1.1, Rhea:24292):

> L-glutamate + acetyl-CoA → N-acetyl-L-glutamate + CoA + H⁺

The bifunctionality of bacterial ArgJ is not merely a database inference — it is established biochemically in orthologous enzymes. Purified bifunctional ArgJ enzymes from *Thermotoga neapolitana* and *Bacillus stearothermophilus* complement both *argE* (acetylornithine deacetylase) and *argA* (N-acetylglutamate synthase) mutations in *E. coli*, and they catalyze both reactions in vitro. As reported in [PMID: 10931207](https://pubmed.ncbi.nlm.nih.gov/10931207/), "*whereas bacterial genes additionally complement an argA mutant (deficient in N-acetylglutamate synthetase, the first enzyme of the pathway)*" and "*T. neapolitana and B. stearothermophilus ArgJ also catalyze the conversion of glutamate to N-acetylglutamate using acetylCoA as the acetyl donor*." The bifunctional identity of the argJ product is further confirmed by [PMID: 16409639](https://pubmed.ncbi.nlm.nih.gov/16409639/): "*the bifunctional version of ornithine acetyltransferase (OAT, gene argJ) present in Bacteria, Archaea and many Eukaryotes*." This establishes that in bacteria such as *Pseudomonas*, a single ArgJ polypeptide can supply both the recycling transacetylase and the anabolic NAGS activity.

### Finding 2 — ArgJ is a self-cleaving Ntn-hydrolase using an N-terminal Thr nucleophile and an acyl-enzyme intermediate

ArgJ belongs to the **N-terminal nucleophile (Ntn) hydrolase superfamily**. UniProt P59612 records that the precursor is autolytically cleaved between residues **188 and 189**, generating the **α chain (1–188)** and the **β chain (189–405)**; the newly exposed N-terminal **Thr189** of the β chain is the catalytic nucleophile, with oxyanion-hole stabilizing residues at positions **115/116**, and the enzyme assembling as an **α₂β₂ heterotetramer**.

The mechanistic model is grounded in detailed biophysical work on ornithine acetyltransferase (OAT2). As stated in [PMID: 19105697](https://pubmed.ncbi.nlm.nih.gov/19105697/), "*OAT2 is a member of the N-terminal nucleophile (Ntn) hydrolase enzyme superfamily and catalyzes the reversible transfer of an acetyl group between the alpha-amino groups of ornithine and glutamate in a mechanism proposed to involve an acyl-enzyme complex*," and mass spectrometry directly identified the catalytic residue: "*Mass spectrometric studies identified Thr-181 as the residue acetylated during OAT2 catalysis*." Consistent with a covalent acetyl-enzyme intermediate, the reaction follows **ping-pong bi-bi kinetics** — "*ArgJ-mediated catalysis follows ping-pong bi-bi kinetic mechanism*" ([PMID: 10931207](https://pubmed.ncbi.nlm.nih.gov/10931207/)). The requirement for autocatalytic maturation is a hallmark of these enzymes; as noted in [PMID: 40140419](https://pubmed.ncbi.nlm.nih.gov/40140419/), Thr-Ntn enzymes including ornithine acetyltransferase "*require autocatalytic cleavage of their N-terminal propeptides*" to generate the catalytic N-terminal Thr.

### Finding 3 — ArgJ operates in the cytoplasm as the recycling (5th) step of arginine biosynthesis, with ornithine as a feedback inhibitor

UniProt P59612 gives the subcellular location as **cytoplasm**, and assigns ArgJ to L-arginine biosynthesis: production of *L-ornithine and N-acetyl-L-glutamate from L-glutamate and N²-acetyl-L-ornithine* (cyclic, step 1/1) and *N²-acetyl-L-ornithine from L-glutamate* (step 1/4). Functionally, this corresponds to the fifth step of the pathway, where acetylornithine is converted to ornithine. As described in [PMID: 1339419](https://pubmed.ncbi.nlm.nih.gov/1339419/), "*the conversion of acetylornithine to ornithine. This reaction is catalyzed by the enzyme ornithine acetyltransferase, which is a product of the argJ gene*."

A key regulatory feature is product/feedback inhibition by **L-ornithine**: "*L-ornithine acts as an inhibitor; this amino acid therefore appears to be a key regulatory molecule in the acetyl cycle of L-arginine synthesis*" ([PMID: 10931207](https://pubmed.ncbi.nlm.nih.gov/10931207/)). This provides a direct control point that couples ArgJ throughput to downstream ornithine demand. Notably, the bacterial enzyme is cytoplasmic, in contrast to the eukaryotic mitochondrial localization of the orthologous ornithine acetyltransferase — "*the yeast ARG7 gene encoding mitochondrial ornithine acetyltransferase*" ([PMID: 9428669](https://pubmed.ncbi.nlm.nih.gov/9428669/)) — underscoring that in *P. putida*, ArgJ carries out its function in the cytosol.

### Finding 4 — The P59612 sequence retains the complete, conserved ArgJ/Ntn-hydrolase catalytic apparatus

Direct inspection of the 405-residue P59612 sequence confirms all the structural determinants expected of a functional bifunctional ArgJ:

- The **autolytic cleavage site is Ala188|Thr189**, exposing Thr189 as the new β-chain N-terminal nucleophile — the defining feature of Ntn-hydrolase self-processing.
- The annotated **oxyanion-hole residues at positions 115/116 are Thr115–Gly116**, directly paralleling the experimentally defined OAT2 oxyanion hole formed by "*the backbone amide NH of Gly-112 and the alcohol of Thr-111*" ([PMID: 19105697](https://pubmed.ncbi.nlm.nih.gov/19105697/)).
- **Substrate-binding residues are conserved**: Thr152, Lys178, Thr189, Glu276, Asn400, Thr405.

This is orthology- and structure-based (in-silico) evidence rather than direct assay of the *P. putida* protein, but the residue-level conservation across the catalytic pentad and oxyanion hole strongly indicates that P59612 is a catalytically competent bifunctional acetyltransferase.

### Finding 5 — *P. putida* KT2440 encodes both a bifunctional ArgJ (PP_1346) and a separate classical NAGS ArgA (PP_5185); argJ is a standalone gene

KEGG genome annotation assigns **argJ = PP_1346** (KEGG Orthology K00620; glutamate N-acetyltransferase / amino-acid N-acetyltransferase; EC 2.3.1.35 + 2.3.1.1), genomic position 1,534,992–1,536,209, in pathway ppu00220 (arginine biosynthesis) and module M00028 (ornithine biosynthesis, glutamate ⇒ ornithine). Crucially, argJ's immediate genomic neighbors are **functionally unrelated** — PP_1345 (secA), PP_1347 (glutathione S-transferase), and PP_1348 (nudix/8-oxo-dGTPase) — meaning **argJ is not embedded in an arg operon** but is transcribed as a standalone locus.

Separately, **PP_5185 (argA**, KEGG Orthology K14682, EC 2.3.1.1) is annotated as the **classical NAGS**, containing an amino-acid kinase (AAK) regulatory domain fused to an N-acetyltransferase (GNAT) domain — the arginine-feedback-regulated first enzyme of the pathway — also assigned to ppu00220/M00028. This genomic architecture indicates a **division of labor**: ArgJ handles the main transacetylation/recycling step (and can supply auxiliary NAGS activity), while the dedicated ArgA performs the primary, allosterically regulated *de novo* N-acetylglutamate synthesis. The mechanism of arginine feedback control on classical NAGS enzymes is well characterized in the closely related *Pseudomonas aeruginosa* ([PMID: 22447897](https://pubmed.ncbi.nlm.nih.gov/22447897/); [PMID: 19084009](https://pubmed.ncbi.nlm.nih.gov/19084009/)).

### Finding 6 — The AlphaFold model of P59612 is very high confidence, with low confidence localized precisely to the autoproteolytic cleavage loop

AlphaFold DB model **AF-P59612-F1 (v6)** has a **global mean pLDDT of 96.5**; 97.0% of the 405 residues are modeled at very high confidence (pLDDT ≥ 90) and 99.3% at confident level (≥ 70). All annotated catalytic and substrate-binding residues are modeled with very high confidence: Thr115 (96.4), Gly116 (94.9), Thr152 (93.6), Lys178 (96.8), Glu276 (94.9), Asn400 (92.1). Strikingly, confidence drops sharply and specifically at the **autolytic cleavage site — Ala188 (58.2) and Thr189 (65.9)** — the lowest-confidence region of the entire protein. This is mechanistically meaningful: the self-cleavage loop is expected to be conformationally flexible in the uncleaved precursor (as AlphaFold models the single-chain precursor), and its localized low confidence is consistent with a mobile loop that undergoes autoproteolytic maturation. The high-confidence prediction across the rest of the structure reproduces the canonical ArgJ/Ntn-hydrolase αββα sandwich fold.

---

## Mechanistic Model / Interpretation

### The arginine "acetyl cycle" and ArgJ's central role

*Pseudomonas putida*, like most bacteria other than the *Enterobacteriaceae*, uses the **economical (cyclic) route** for the N-acetylated steps of ornithine biosynthesis. In this cycle, the acetyl group is not lost by hydrolysis (the "linear" ArgE route of *E. coli*) but is instead conserved and recycled by ArgJ:

```
                          acetyl-CoA          CoA
                              \               /
   L-glutamate  ───────────────►  N-acetyl-L-glutamate   (ArgA / ArgJ-AGSase, EC 2.3.1.1)
        ▲                                  │
        │                                  │  ArgB (NAGK), ArgC, ArgD
        │  (acetyl group recycled)         ▼
        │                          N²-acetyl-L-ornithine
        │                                  │
        └──────────  ArgJ (OATase, EC 2.3.1.35)  ──────────┘
                                           │
                                           ▼
                                     L-ornithine  ──► citrulline ──► arginine
```

**ArgJ is the linchpin of this cycle.** Its dominant transacetylase (OATase) activity performs a single, elegant group-transfer: it strips the acetyl group off N²-acetyl-L-ornithine and hands it directly to L-glutamate. This simultaneously (a) liberates **L-ornithine** for carbamoylation to citrulline and onward conversion to arginine, and (b) regenerates **N-acetyl-L-glutamate**, feeding the acetyl group back to the top of the acetylated branch. Because the acetyl group is transferred rather than hydrolyzed, the cell avoids the ATP/acetyl-CoA cost of re-acetylating glutamate on every turn. The auxiliary AGSase (NAGS) activity of ArgJ, and the dedicated classical NAGS ArgA (PP_5185), top up the cycle with fresh N-acetyl-L-glutamate from glutamate + acetyl-CoA whenever net synthesis (rather than pure recycling) is required.

### Catalytic mechanism at the residue level

ArgJ is a **Thr-Ntn-hydrolase** that operates through a two-stage, ping-pong (double-displacement) mechanism:

| Stage | Event | Key residues |
|-------|-------|--------------|
| Maturation | Precursor autoproteolysis at Ala188\|Thr189 → α (1–188) + β (189–405) chains; assembly as α₂β₂ | Thr189 (new N-terminal nucleophile) |
| Half-reaction 1 | Acetyl donor (N²-acetyl-ornithine *or* acetyl-CoA) acetylates Thr189 → covalent **acetyl-Thr189** acyl-enzyme; first product (ornithine or CoA) released | Thr189, oxyanion hole Thr115/Gly116 |
| Half-reaction 2 | L-glutamate α-amino group attacks the acyl-enzyme → **N-acetyl-L-glutamate** released, Thr189 regenerated | Thr189, Glu276, Lys178, Asn400 |

The **oxyanion hole (Thr115/Gly116)** stabilizes the tetrahedral transition-state carbonyl during formation and breakdown of the acyl-enzyme, mirroring the OAT2 Thr111/Gly112 pair defined crystallographically. **L-ornithine feedback inhibition** provides product-level regulation of the transacetylase, while the pathway's primary allosteric control resides in the arginine-inhibited classical NAGS (ArgA).

### *P. putida*-specific evidence integration

For the exact KT2440 protein, the evidence is convergent though computational/comparative rather than direct enzymology:

- **Sequence:** complete conserved catalytic pentad and oxyanion hole (Finding 4).
- **Structure:** AlphaFold pLDDT 96.5 canonical ArgJ fold; flexible self-cleavage loop flagged by localized low confidence (Finding 6).
- **Genome context:** standalone argJ (PP_1346) plus separate ArgA (PP_5185), both mapped to the arginine-biosynthesis pathway/module (Finding 5).

Together these place P59612 unambiguously within the ArgJ family and assign it the bifunctional OATase/NAGS role in the cytoplasmic acetyl cycle.

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution |
|------|-----------------|--------------|
| [10931207](https://pubmed.ncbi.nlm.nih.gov/10931207/) | *Mono- and bifunctional ornithine acetyltransferases from thermophiles* | Direct biochemical demonstration that bacterial ArgJ is bifunctional (complements *argA*), catalyzes glutamate→NAG with acetyl-CoA, follows ping-pong bi-bi kinetics, and is inhibited by L-ornithine. Core support for Findings 1, 2, 3. |
| [19105697](https://pubmed.ncbi.nlm.nih.gov/19105697/) | *Anatomy of a simple acyl intermediate: OAT* | Assigns OAT to Ntn-hydrolase superfamily; identifies acetylated catalytic Thr; defines Thr/Gly oxyanion hole. Core support for Findings 2, 4. |
| [16409639](https://pubmed.ncbi.nlm.nih.gov/16409639/) | *Unusual gene-enzyme relationship in marine γ-proteobacteria* | Confirms argJ encodes bifunctional OAT in Bacteria/Archaea/Eukaryotes. Supports Finding 1. |
| [1339419](https://pubmed.ncbi.nlm.nih.gov/1339419/) | *argJ from Neisseria gonorrhoeae* | Defines the physiological (5th-step) acetylornithine→ornithine reaction as argJ-encoded. Supports Finding 3. |
| [40140419](https://pubmed.ncbi.nlm.nih.gov/40140419/) | *Catalytic pentad mechanism for Ntn enzymes* | Confirms Thr-Ntn enzymes (incl. ornithine acetyltransferase) require autocatalytic propeptide cleavage. Supports Finding 2. |
| [9428669](https://pubmed.ncbi.nlm.nih.gov/9428669/) | *Yeast ARG7 ornithine acetyltransferase* | Shows eukaryotic OAT is also endowed with acetylglutamate synthase activity and is mitochondrial — contrasts with bacterial cytoplasmic localization. Supports Findings 1, 3. |
| [22447897](https://pubmed.ncbi.nlm.nih.gov/22447897/) | *Functional dissection of NAGS (ArgA) of P. aeruginosa* | Characterizes the classical AAK+GNAT NAGS and its arginine feedback — the paralogous ArgA role. Context for Finding 5. |
| [19084009](https://pubmed.ncbi.nlm.nih.gov/19084009/) | *Mechanism of arginine regulation of NAGS* | Mechanism of arginine feedback on classical NAGS. Context for Finding 5. |
| [15175299](https://pubmed.ncbi.nlm.nih.gov/15175299/) | *ArgR regulon in P. aeruginosa* | Transcriptional control of arginine biosynthesis (argF, carAB, argG repressed by ArgR) — regulatory backdrop for the pathway ArgJ serves. |
| [28943401](https://pubmed.ncbi.nlm.nih.gov/28943401/) | *Crystal structure of ArgA from M. tuberculosis* | Structural reference for the class III NAGS (GNAT fold) alternative to ArgJ. Comparative context. |

**How the evidence coheres:** No paper directly assays the *P. putida* KT2440 ArgJ (P59612) protein, so all functional claims for this specific protein rest on (a) authoritative biochemistry of orthologous bacterial and eukaryotic ArgJ/OAT enzymes, (b) the ArgJ family/domain assignment (Pfam PF01960; InterPro IPR002813, IPR016117, IPR042195), and (c) sequence/structure conservation of the catalytic machinery in P59612. This is a coherent, mutually reinforcing body of evidence, but it is inferential for the target organism.

---

## Limitations and Knowledge Gaps

1. **No direct enzymology on the target protein.** There is no published purification, kinetic characterization, crystal structure, or knockout phenotype for *P. putida* KT2440 ArgJ (P59612) specifically. All catalytic, mechanistic, and regulatory claims are transferred by orthology from other organisms (*T. neapolitana*, *B. stearothermophilus*, *N. gonorrhoeae*, yeast OAT2/Arg7) and from UniProt/KEGG rule-based (HAMAP MF_01106) annotation.

2. **Relative contribution of ArgJ vs. ArgA to NAGS activity is untested in *P. putida*.** The genome encodes both a bifunctional ArgJ (PP_1346) and a classical NAGS ArgA (PP_5185). Which enzyme dominates de novo N-acetylglutamate supply, and under what growth conditions, has not been measured for KT2440. The division-of-labor model (ArgJ = recycling; ArgA = regulated de novo) is inferred from annotation and paralog function, not demonstrated experimentally in this strain.

3. **Autoprocessing and quaternary structure not experimentally verified for P59612.** The Ala188|Thr189 cleavage and α₂β₂ assembly are annotation/AlphaFold-based; the AlphaFold model itself flags this loop as its lowest-confidence region, and it models the single-chain precursor, not the mature cleaved heterotetramer.

4. **Substrate specificity and kinetic parameters unknown for the target.** K_m and k_cat for N²-acetyl-ornithine, glutamate, and acetyl-CoA, plus the quantitative strength of L-ornithine feedback inhibition, are not available for the *P. putida* enzyme.

5. **Localization is inferred.** Cytoplasmic localization follows from UniProt annotation and general bacterial biology; there is no direct fractionation or imaging evidence for P59612.

---

## Proposed Follow-up Experiments / Actions

1. **Heterologous expression and complementation.** Clone *P. putida* argJ (PP_1346) and test complementation of *E. coli* argE and argA mutants to confirm both OATase and NAGS activities experimentally for this specific protein.

2. **Purification and steady-state kinetics.** Purify recombinant P59612 and measure K_m/k_cat for N²-acetyl-L-ornithine, L-glutamate, and acetyl-CoA; confirm ping-pong bi-bi kinetics and quantify the L-ornithine inhibition constant (K_i).

3. **Verify autoprocessing.** Use SDS-PAGE/mass spectrometry to confirm cleavage at Ala188|Thr189 into α (1–188) and β (189–405) chains, and native MS or SEC-MALS to confirm α₂β₂ heterotetramer assembly. Mutate Thr189 to Ala/Ser to test its role as the maturation and catalytic nucleophile.

4. **Structure determination.** Solve a crystal or cryo-EM structure of mature ArgJ (ideally with acetyl-ornithine/glutamate analogs bound) to validate the AlphaFold fold and directly visualize the Thr189 acyl-enzyme and Thr115/Gly116 oxyanion hole.

5. **Genetic dissection of ArgJ vs. ArgA.** Construct single and double knockouts of argJ (PP_1346) and argA (PP_5185); assess arginine auxotrophy, growth on minimal medium, and metabolomic pools of acetylornithine/N-acetylglutamate to define each enzyme's in-vivo contribution and any redundancy.

6. **Regulation and flux.** Measure argJ expression under arginine-replete vs. -limited conditions and in an argR background to determine transcriptional control, and use ¹³C flux analysis to quantify the acetyl-recycling flux through ArgJ relative to de novo NAGS input.

---

*Report generated from a 5-iteration autonomous investigation. Findings F001–F006 are recorded in the knowledge state with verified literature citations. All functional claims for the target protein P59612 are supported by orthologous experimental biochemistry combined with sequence/structure conservation analysis of the P. putida KT2440 protein.*


## Artifacts

- [OpenScientist final report](argJ-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](argJ-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:10931207
2. PMID:16409639
3. PMID:19105697
4. PMID:40140419
5. PMID:1339419
6. PMID:9428669
7. PMID:22447897
8. PMID:19084009