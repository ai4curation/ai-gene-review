---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-13T05:25:28.512229'
end_time: '2026-08-13T06:50:11.223314'
duration_seconds: 5082.71
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_0301
  gene_symbol: PP_0301
  uniprot_accession: Q88R33
  protein_description: 'SubName: Full=Betainyl-CoA thiolase {ECO:0000313|EMBL:AAN65932.1};
    EC=2.3.1.- {ECO:0000313|EMBL:AAN65932.1};'
  gene_info: OrderedLocusNames=PP_0301 {ECO:0000313|EMBL:AAN65932.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: 4-hydroxybenzoyl-CoA_TE. (IPR050563); HotDog_dom_sf. (IPR029069);
    4HBT_2 (PF13279)
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
citation_count: 12
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PP_0301-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PP_0301-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88R33
- **Protein Description:** SubName: Full=Betainyl-CoA thiolase {ECO:0000313|EMBL:AAN65932.1}; EC=2.3.1.- {ECO:0000313|EMBL:AAN65932.1};
- **Gene Information:** OrderedLocusNames=PP_0301 {ECO:0000313|EMBL:AAN65932.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** 4-hydroxybenzoyl-CoA_TE. (IPR050563); HotDog_dom_sf. (IPR029069); 4HBT_2 (PF13279)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_0301" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_0301' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_0301** (gene ID: PP_0301, UniProt: Q88R33) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# PP_0301 (Q88R33) in *Pseudomonas putida* KT2440: A Cytoplasmic Betainyl-CoA Thioesterase of the L-Carnitine Catabolic Pathway

## Summary

The gene **PP_0301** (UniProt **Q88R33**; OrderedLocusNames PP_0301) of *Pseudomonas putida* KT2440 encodes a small (156-residue), single-domain, **HotDog-fold acyl-CoA thioesterase** belonging to the 4-hydroxybenzoyl-CoA thioesterase (4HBT) family. Its physiological function is that of a **betainyl-CoA thioesterase** (gene name **cdhB**; EC **3.1.2.33**; KEGG ortholog **K27492**), catalyzing the hydrolysis of the CoA thioester of glycine betaine:

> **betainyl-CoA + H₂O → glycine betaine + CoA**

This reaction is the third, CoA-releasing step of the **L-carnitine catabolic pathway** encoded by the compact, co-oriented operon **PP_0301–PP_0305**. Within this pathway, L-carnitine is first oxidized to 3-dehydrocarnitine by carnitine 3-dehydrogenase (lcdH/cdhA, PP_0302, EC 1.1.1.108), the 3-dehydrocarnitine is then cleaved by the β-keto-acid cleavage enzyme cdhC (PP_0303, EC 2.3.1.317) to yield **betainyl-CoA** (with concomitant acetoacetate formation from acetyl-CoA), and finally PP_0301/cdhB hydrolyzes betainyl-CoA to release **glycine betaine** and free CoA. Glycine betaine is a central branch-point metabolite that is subsequently funneled into the conserved, cytoplasmic glycine-betaine demethylation pathway (GB → dimethylglycine → sarcosine → glycine), enabling the bacterium to use L-carnitine as a source of carbon and nitrogen.

A key outcome of this investigation is an **annotation correction**. The legacy name carried in the genome submission — "betainyl-CoA thiolase" with EC 2.3.1.- (an acyltransferase/thiolase class) — is a **misannotation**. Every domain and family assignment for Q88R33 is unanimous for a HotDog-fold thioester **hydrolase** (EC class 3.1.2.-), and the protein's small size (~156 aa, a single HotDog domain) is inconsistent with genuine thiolases (~400 aa, two-domain acyltransferases). The correct designation is a **betainyl-CoA thioesterase (hydrolase)**. This functional assignment is strongly supported by 1:1 orthology to the experimentally validated *Pseudomonas aeruginosa* gene PA5385 (cdhB), which resides in a transposon-screen-confirmed carnitine-catabolism locus.

The protein is a soluble, **cytoplasmic** enzyme — it has no signal peptide or transmembrane segments (confirmed by a hydropathy scan), and its CoA-thioester substrate is strictly intracellular. Its L-carnitine substrate enters the cell through the co-encoded ABC transporter (substrate-binding protein PP_0304). An experimental crystal structure of the *P. putida* protein itself exists (PDB 2HLJ, 2.00 Å), confirming the HotDog thioesterase fold.

---

## Key Findings

### F001 — PP_0301 is a HotDog-fold thioesterase, not a thiolase (annotation corrected)

UniProt Q88R33 is a small **156-amino-acid single-domain protein**. The domain and family assignments across all major resources converge unanimously on a **HotDog-fold acyl-CoA thioesterase**:

| Resource | Assignment |
|---|---|
| InterPro | IPR050563 (4-hydroxybenzoyl-CoA thioesterase family) + IPR029069 (HotDog domain superfamily) |
| Pfam | PF13279 (4HBT_2) |
| CDD | cd00586 (4HBT) |
| Gene3D | 3.10.129.10 (HotDog Thioesterase) |
| SUPFAM | SSF54637 (Thioesterase/thiol ester dehydrase-isomerase) |
| PANTHER | PTHR31793 (4-hydroxybenzoyl-CoA thioesterase family) |
| eggNOG | COG0824 (predicted thioesterase) |
| GO (molecular function) | GO:0047617 (fatty acyl-CoA hydrolase activity) |

Critically, an **experimental crystal structure exists**: **PDB 2HLJ**, an X-ray structure at 2.00 Å resolution (chains A = residues 1–156), solved by the Joint Center for Structural Genomics (JCSG/PSI-2) and titled *"Crystal structure of a putative thioesterase from Pseudomonas putida KT2440."* This directly confirms the HotDog thioesterase fold experimentally for the exact protein in question.

The legacy genome-submission name "betainyl-CoA **thiolase**" (EC 2.3.1.-) is therefore a **misnomer**. Thiolases and other EC 2.3.1.- acyltransferases *transfer* an acyl group and are typically ~400-residue, two-domain enzymes. PP_0301 is instead a **hydrolase** (EC 3.1.2.-): it cleaves a thioester bond with water, releasing a free acid and CoA. Its small single-domain architecture is diagnostic of the HotDog thioesterase superfamily rather than the thiolase superfamily.

The mechanistic identity of the family is well established in the literature. HotDog-fold thioesterases catalyze hydrolysis of thioester bonds of acyl-CoA substrates ([PMID: 26067557](https://pubmed.ncbi.nlm.nih.gov/26067557/): *"It belongs to the hotdog-fold thioesterase superfamily and catalyzes hydrolysis of thioester bonds of acyl-CoA in vitro, while its in vivo function remains unrevealed."*). Acyl-CoA thioesterases more broadly *"catalyze the hydrolysis of fatty acyl-CoA to free fatty acid and CoA and thereby regulate lipid metabolism and cellular signaling"* ([PMID: 17563367](https://pubmed.ncbi.nlm.nih.gov/17563367/)), and the structural determinants for substrate recognition and catalysis by these enzymes have been dissected in the *E. coli* paralogs YbdB and YdiI ([PMID: 25010423](https://pubmed.ncbi.nlm.nih.gov/25010423/): *"the structural determinants for substrate recognition and catalysis in two hotdog-fold thioesterase paralogs, YbdB and YdiI from Escherichia coli, are identified and analyzed"*).

### F002 — PP_0301 = cdhB, betainyl-CoA thioesterase (EC 3.1.2.33)

KEGG assigns **ppu:PP_0301** to ortholog **K27492 = cdhB = "betainyl-CoA thioesterase [EC:3.1.2.33]."** The EC 3.1.2.33 entry (reaction RN R13307) defines the catalyzed reaction as:

> **betainyl-CoA + H₂O = glycine betaine + CoA** (systematic name: *betaine-CoA hydrolase*)

The KEGG comment notes that *"the enzyme, characterized from the bacterium Pseudomonas aeruginosa, is involved in an L-carnitine degradation pathway."* The **substrate specificity** is the CoA thioester of glycine betaine (betainyl-CoA); the enzyme hydrolyzes this thioester to release free glycine betaine plus CoA. This assignment is fully consistent with (i) the HotDog 4HBT fold — a small, single-domain thioesterase scaffold — and (ii) the substrate implied by the protein's own legacy name ("betainyl-CoA"). The reaction it catalyzes matches the general acyl-CoA thioesterase chemistry of the family (hydrolysis of an acyl-CoA to free acid + CoA), specialized here for the quaternary-ammonium acyl group of glycine betaine.

### F003 — PP_0301 lies in a carnitine-catabolism operon (cdhABC / PP_0301–PP_0305)

Genomic context is highly informative. KEGG genomic positions place PP_0301 (complement 362036–362506) within a tight, co-oriented gene cluster:

| Locus | Gene | KEGG ortholog | Enzyme / role | EC |
|---|---|---|---|---|
| PP_0301 | cdhB | K27492 | Betainyl-CoA thioesterase | 3.1.2.33 |
| PP_0302 | lcdH / cdhA | K17735 | Carnitine 3-dehydrogenase | 1.1.1.108 |
| PP_0303 | cdhC | K27837 | 3-dehydrocarnitine:acetyl-CoA trimethylamine transferase (BKACE) | 2.3.1.317 |
| PP_0304 | — | K02002 | Glycine betaine/carnitine ABC-transporter substrate-binding protein | — |
| PP_0305 | cdhR | K17736 | AraC-family carnitine-catabolism transcriptional activator | — |
| PP_0298 | — | K21826 | AraC-family glycine-betaine-responsive activator | — |

STRING (160488.PP_0301) corroborates the functional linkage: its top-scoring partner is **lcdH (score 0.995)**, followed by **caiX** (carnitine transport, 0.632) and **cdhR** (0.592). Integrating these data yields the reconstructed pathway:

```
L-carnitine
   │  cdhA / lcdH  (PP_0302, EC 1.1.1.108; NAD+ → NADH)
   ▼
3-dehydrocarnitine
   │  cdhC  (PP_0303, EC 2.3.1.317; + acetyl-CoA → acetoacetate)
   ▼
betainyl-CoA
   │  cdhB / PP_0301  (EC 3.1.2.33; + H2O)
   ▼
glycine betaine  +  CoA
```

PP_0301 catalyzes the **final, CoA-releasing step** of this three-enzyme route, regenerating free CoA and liberating glycine betaine for downstream catabolism.

### F004 — Cytoplasmic localization; product feeds the GbdR-regulated demethylation pathway

PP_0301 is a **soluble, single-domain cytoplasmic enzyme**. It carries no signal peptide and no transmembrane segments (confirmed by a hydropathy scan), and its CoA-thioester substrate is strictly intracellular (CoA thioesters do not cross membranes). The upstream substrate, L-carnitine, is imported via the co-encoded ABC transporter (substrate-binding protein PP_0304). Thus the enzyme performs its chemistry in the **cytoplasm**.

Its product, **glycine betaine (GB)**, is the branch-point metabolite of quaternary-amine catabolism in pseudomonads. In the closely related *P. aeruginosa*, GB is degraded in the cytoplasm by a multistep demethylation route (GB → dimethylglycine → sarcosine → glycine), which lets the bacterium use GB — and its precursors choline and carnitine — as sole sources of carbon and nitrogen ([PMID: 23354714](https://pubmed.ncbi.nlm.nih.gov/23354714/): *"a variety of soil- and water-dwelling bacteria have catabolic pathways for the multistep conversion of choline, via GB, to glycine and can thereby use choline and GB as sole sources of carbon and nitrogen"*). This catabolic locus is controlled by the AraC-family regulator **GbdR**, whose regulon *"includes the genes encoding GB, dimethylglycine, sarcosine, glycine, and serine catabolic enzymes and the BetX and CbcXWV quaternary amine transport proteins"* ([PMID: 24097953](https://pubmed.ncbi.nlm.nih.gov/24097953/)). This mirrors the CdhR/AraC regulator (PP_0305) that governs the carnitine branch in *P. putida*.

### F005 — Primary literature confirms the carnitine → 3-dehydrocarnitine → glycine betaine route

The two enzymatic steps flanking and including PP_0301 are anchored in primary experimental literature:

- **Wargo & Hogan 2009** ([PMID: 19406895](https://pubmed.ncbi.nlm.nih.gov/19406895/)) performed a transposon-mutant genetic screen in *P. aeruginosa* PA14 that experimentally established the carnitine catabolic route: *"carnitine is converted to 3-dehydrocarnitine (3-dhc) which is in turn metabolized to glycine betaine (GB), an intermediate metabolite in the catabolism of carnitine to glycine."* They also *"confirmed that an intact GB catabolic pathway is required for growth on carnitine,"* showing that carnitine catabolism funnels through glycine betaine — the very product of PP_0301.

- **Bastard et al. 2014** ([PMID: 24240508](https://pubmed.ncbi.nlm.nih.gov/24240508/)) defined the **DUF849 / β-keto acid cleavage enzyme (BKACE)** family that provides the EC 2.3.1.317 activity (cdhC): *"we investigated the DUF849 Pfam family and unearthed 14 potential new enzymatic activities, leading to the designation of these proteins as β-keto acid cleavage enzymes."* This is the enzyme that generates the **betainyl-CoA substrate** hydrolyzed by PP_0301.

- **Wargo, Szwergold & Hogan 2008** ([PMID: 17951379](https://pubmed.ncbi.nlm.nih.gov/17951379/)) biochemically defined the downstream glycine-betaine demethylation genes and the AraC regulator GbdR in *P. aeruginosa*: *"Glycine betaine (GB), which occurs freely in the environment and is an intermediate in the catabolism of choline and carnitine, can serve as a sole source of carbon or nitrogen in Pseudomonas aeruginosa."*

The KT2440 cluster PP_0301–PP_0305 (cdhB, lcdH/cdhA, cdhC, transporter, cdhR) is the direct ortholog of the *P. aeruginosa* carnitine-catabolism locus.

### F006 — PP_0301/cdhB is the direct ortholog of *P. aeruginosa* PA5385, within an experimentally validated locus

KEGG orthology links K27492 (cdhB) to *P. aeruginosa* PAO1 gene **PA5385** (and PA14 gene PA14_71120). The adjacent cluster resolves cleanly into an ortholog-by-ortholog match:

| *P. putida* KT2440 | *P. aeruginosa* PAO1 | Gene | Function |
|---|---|---|---|
| PP_0301 | PA5385 | cdhB | Betainyl-CoA thioesterase (K27492, EC 3.1.2.33) |
| PP_0302 | PA5386 | lcdH/cdhA | Carnitine 3-dehydrogenase (K17735, EC 1.1.1.108) |
| PP_0303 | PA5387 | cdhC | BKACE (K27837, EC 2.3.1.317) |
| PP_0305 | PA5389 | cdhR | AraC regulator (K17736) |

This is precisely the **"PA5388–PA5384 region"** (with adjacent regulator PA5389) that Wargo & Hogan 2009 identified by transposon screen as containing the carnitine-dehydrogenase homologue and genes required for growth on carnitine ([PMID: 19406895](https://pubmed.ncbi.nlm.nih.gov/19406895/): *"The PA5388-PA5384 region contains the predicted P. aeruginosa carnitine dehydrogenase homologue along with other genes required for growth on carnitine."*), with PA5389 required to induce those transcripts in response to carnitine. Consequently, *P. putida* PP_0301 (cdhB) is **1:1 orthologous to an experimentally validated carnitine-catabolism gene (PA5385)**, and its operon PP_0301–PP_0305 mirrors PA5385–PA5389. This transfers strong experimental support from the *P. aeruginosa* system to the *P. putida* annotation.

---

## Mechanistic Model / Interpretation

PP_0301 is best understood as the **CoA-recycling hydrolase of the carnitine catabolic operon** in *P. putida* KT2440. The pathway integrates transport, oxidation, thioester-generating cleavage, and thioester hydrolysis:

```
                 ┌─────────────────────────────────────────────┐
  L-carnitine ──►│ ABC transporter (PP_0304, SBP)              │  IMPORT
                 └───────────────────┬─────────────────────────┘
                                     ▼  (cytoplasm)
                          L-carnitine
                                     │  cdhA / lcdH (PP_0302)
                                     │  EC 1.1.1.108, NAD+ → NADH
                                     ▼
                          3-dehydrocarnitine
                                     │  cdhC (PP_0303)  BKACE / DUF849
                                     │  EC 2.3.1.317; acetyl-CoA → acetoacetate
                                     ▼
                          betainyl-CoA
                                     │  cdhB / PP_0301  ◄── THIS GENE
                                     │  EC 3.1.2.33; + H2O
                                     ▼
                 glycine betaine  +  CoA (recycled)
                                     │
                                     │  GbdR-regulated demethylation
                                     ▼
              dimethylglycine ► sarcosine ► glycine  ► central metabolism (C + N)

  Regulation: CdhR / AraC (PP_0305) activates the carnitine branch in response
              to carnitine; GbdR-type AraC regulators activate the downstream
              glycine-betaine demethylation genes.
```

**Why the "thiolase" name is wrong and the "thioesterase" assignment is right.** The genome-submission label reflects an early, sequence-blind guess. Three independent lines of evidence overturn it:

1. **Fold / size** — Q88R33 is a 156-aa single HotDog domain (confirmed experimentally by PDB 2HLJ), not a ~400-aa two-domain thiolase. Every domain database (InterPro, Pfam, CDD, Gene3D, SUPFAM, PANTHER, eggNOG) classifies it as a 4HBT HotDog thioesterase.
2. **Chemistry** — HotDog 4HBT enzymes *hydrolyze* acyl-CoA thioesters (EC 3.1.2.-), releasing free acid + CoA; thiolases (EC 2.3.1.-) instead *transfer* acyl groups. The KEGG-assigned EC 3.1.2.33 reaction (betainyl-CoA + H₂O → glycine betaine + CoA) is a hydrolysis.
3. **Pathway logic and orthology** — The enzyme sits immediately downstream of a BKACE that *produces* betainyl-CoA, and it is 1:1 orthologous to the experimentally validated *P. aeruginosa* cdhB (PA5385). A thioesterase that liberates glycine betaine + CoA is exactly what the pathway requires at this position; a thiolase would not fit.

**Biological role.** By hydrolyzing betainyl-CoA, PP_0301 (i) liberates glycine betaine for entry into the demethylation pathway, and (ii) regenerates free CoA, which is essential for continued flux through the acetyl-CoA-dependent cdhC step. The enzyme thereby couples carnitine breakdown to the universal quaternary-amine catabolic hub (glycine betaine → glycine), allowing *P. putida* to exploit carnitine as a carbon and nitrogen source in the soil and rhizosphere environments where carnitine and its relatives are common.

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports the findings |
|---|---|---|
| [19406895](https://pubmed.ncbi.nlm.nih.gov/19406895/) | *Identification of genes required for P. aeruginosa carnitine catabolism* | **Primary experimental anchor.** Transposon screen establishing carnitine → 3-dehydrocarnitine → glycine betaine; identifies the PA5388–PA5384 region (containing PP_0301's ortholog PA5385) as required for growth on carnitine. |
| [24240508](https://pubmed.ncbi.nlm.nih.gov/24240508/) | *Revealing the hidden functional diversity of an enzyme family* | Defines the DUF849 / BKACE family that provides cdhC (EC 2.3.1.317), the enzyme generating PP_0301's betainyl-CoA substrate. |
| [17951379](https://pubmed.ncbi.nlm.nih.gov/17951379/) | *Two gene clusters and a regulator for P. aeruginosa glycine betaine catabolism* | Confirms glycine betaine (PP_0301's product) is a carnitine-catabolism intermediate usable as sole C/N source; defines downstream demethylation genes and GbdR. |
| [24097953](https://pubmed.ncbi.nlm.nih.gov/24097953/) | *Characterization of the GbdR regulon in P. aeruginosa* | Documents downstream GB→DMG→sarcosine→glycine catabolic enzymes and AraC-family (GbdR) regulation receiving PP_0301's product. |
| [23354714](https://pubmed.ncbi.nlm.nih.gov/23354714/) | *Homeostasis and catabolism of choline and glycine betaine* | Establishes the cytoplasmic multistep demethylation of glycine betaine to glycine in soil/water pseudomonads. |
| [26067557](https://pubmed.ncbi.nlm.nih.gov/26067557/) | *Crystal structure of zebrafish fTHEM2* | Establishes that HotDog-fold thioesterases (PP_0301's family) hydrolyze acyl-CoA thioester bonds. |
| [17563367](https://pubmed.ncbi.nlm.nih.gov/17563367/) | *Structural basis for tandem hotdog domains in ACOT7* | Defines the HotDog acyl-CoA thioesterase reaction class (acyl-CoA → free acid + CoA). |
| [25010423](https://pubmed.ncbi.nlm.nih.gov/25010423/) | *Structure and catalysis in E. coli YdiI and YbdB* | Confirms defined active-site residues drive thioester hydrolysis in the HotDog mechanistic class. |

Additional context papers on choline/glycine-betaine physiology and sarcosine regulation in *P. aeruginosa* and *Burkholderia* ([PMID: 22753069](https://pubmed.ncbi.nlm.nih.gov/22753069/), [PMID: 23457628](https://pubmed.ncbi.nlm.nih.gov/23457628/), [PMID: 26503852](https://pubmed.ncbi.nlm.nih.gov/26503852/), [PMID: 27381916](https://pubmed.ncbi.nlm.nih.gov/27381916/)) reinforce the conservation and regulatory logic of the quaternary-amine catabolic network into which PP_0301 feeds.

**Nature of the evidence.** The strongest evidence for PP_0301's specific function is **inference by orthology** to an experimentally characterized system: the enzyme is a 1:1 ortholog of *P. aeruginosa* cdhB/PA5385, whose operon was validated genetically. The reaction assignment (EC 3.1.2.33) derives from biochemical characterization of the *P. aeruginosa* enzyme (per KEGG). Structural evidence is direct and experimental for the *P. putida* protein itself (PDB 2HLJ crystal structure). There is, to date, no published *direct in vitro* enzymatic assay of the *P. putida* KT2440 PP_0301 protein specifically.

---

## Limitations and Knowledge Gaps

1. **No direct biochemical assay of PP_0301 itself.** The EC 3.1.2.33 activity was characterized in the *P. aeruginosa* enzyme; the *P. putida* ortholog's activity and kinetic parameters (kcat, Km for betainyl-CoA) are inferred, not measured. The PDB 2HLJ structure was deposited as a "putative thioesterase" without a bound substrate or functional assay.
2. **Substrate specificity breadth is unquantified.** HotDog thioesterases can be promiscuous. Whether PP_0301 is strictly specific for betainyl-CoA or also hydrolyzes other short-chain or quaternary-amine acyl-CoAs is unknown.
3. **Regulation in *P. putida* is inferred from *P. aeruginosa*.** The role of PP_0305 (CdhR) and PP_0298 (a glycine-betaine-responsive AraC regulator) in inducing PP_0301 in KT2440 is predicted by orthology and operon context, not directly demonstrated.
4. **Phenotype not directly tested in KT2440.** A PP_0301 deletion has not been reported; its necessity for growth of *P. putida* on carnitine is inferred from the *P. aeruginosa* transposon screen.
5. **Legacy annotation persistence.** Public databases still carry the "betainyl-CoA thiolase / EC 2.3.1.-" label; downstream tools relying on this may propagate the misannotation.

---

## Proposed Follow-up Experiments / Actions

1. **In vitro enzyme assay.** Express and purify recombinant PP_0301 (Q88R33) and measure thioesterase activity against **betainyl-CoA** and a panel of acyl-CoA substrates (acetyl-CoA, short-chain acyl-CoAs, 4-hydroxybenzoyl-CoA) to confirm EC 3.1.2.33 and quantify substrate specificity (kcat/Km).
2. **Genetic knockout / complementation.** Construct a ΔPP_0301 mutant in *P. putida* KT2440 and test growth on L-carnitine and glycine betaine as sole C/N sources; complement to confirm the phenotype maps to PP_0301. Metabolite profiling should show betainyl-CoA accumulation in the mutant.
3. **Structure–function analysis.** Use PDB 2HLJ to identify the catalytic residue(s) (typically an Asp/Glu or backbone-water general base in 4HBT enzymes) and test by site-directed mutagenesis.
4. **Transcriptional regulation.** Test induction of the PP_0301–PP_0305 operon by carnitine and glycine betaine, and confirm CdhR (PP_0305) / PP_0298 dependence via reporter fusions and EMSAs.
5. **Database correction.** Submit a curation request to UniProt/KEGG to update Q88R33 from "betainyl-CoA thiolase (EC 2.3.1.-)" to **"betainyl-CoA thioesterase / cdhB (EC 3.1.2.33)"** with the supporting orthology and structural evidence.

---

## Conclusion

PP_0301 (Q88R33) is a cytoplasmic, single-domain HotDog-fold (4HBT) acyl-CoA thioesterase functioning as a **betainyl-CoA thioesterase (cdhB; EC 3.1.2.33)**. It hydrolyzes betainyl-CoA to glycine betaine + CoA, performing the third, CoA-releasing step of the L-carnitine catabolic pathway encoded by the PP_0301–PP_0305 operon, and thereby channels carnitine-derived carbon and nitrogen into the conserved glycine-betaine demethylation route. The genome-legacy name "betainyl-CoA thiolase" (EC 2.3.1.-) is a misannotation; the enzyme is a thioester hydrolase, not a thiolase.


## Artifacts

- [OpenScientist final report](PP_0301-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PP_0301-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:26067557
2. PMID:17563367
3. PMID:25010423
4. PMID:23354714
5. PMID:24097953
6. PMID:19406895
7. PMID:24240508
8. PMID:17951379
9. PMID:22753069
10. PMID:23457628
11. PMID:26503852
12. PMID:27381916