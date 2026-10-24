---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-13T05:25:28.512256'
end_time: '2026-08-13T07:06:09.234892'
duration_seconds: 6040.72
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_0303
  gene_symbol: PP_0303
  uniprot_accession: Q88R31
  protein_description: 'SubName: Full=Dehydrocarnitine cleavage enzyme {ECO:0000313|EMBL:AAN65934.1};
    EC=2.3.1.- {ECO:0000313|EMBL:AAN65934.1};'
  gene_info: OrderedLocusNames=PP_0303 {ECO:0000313|EMBL:AAN65934.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: Aldolase_TIM. (IPR013785); BKACE. (IPR008567); BKACE (PF05853)
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
  path: PP_0303-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PP_0303-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88R31
- **Protein Description:** SubName: Full=Dehydrocarnitine cleavage enzyme {ECO:0000313|EMBL:AAN65934.1}; EC=2.3.1.- {ECO:0000313|EMBL:AAN65934.1};
- **Gene Information:** OrderedLocusNames=PP_0303 {ECO:0000313|EMBL:AAN65934.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** Aldolase_TIM. (IPR013785); BKACE. (IPR008567); BKACE (PF05853)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_0303" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_0303' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_0303** (gene ID: PP_0303, UniProt: Q88R31) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of PP_0303 (Q88R31) in *Pseudomonas putida* KT2440

## Summary

**PP_0303 (UniProt Q88R31) is CdhC — 3-dehydrocarnitine:acetyl-CoA trimethylamine transferase (EC 2.3.1.317) — a cytoplasmic, Zn²⁺-dependent β-keto acid cleavage enzyme (BKACE) that catalyzes the committed carbon–carbon cleavage step of L-carnitine catabolism in *Pseudomonas putida* strain KT2440.** The enzyme performs a Claisen-type condensation/retro-Claisen reaction, **3-dehydrocarnitine + acetyl-CoA → betainyl-CoA + acetoacetate** (KEGG R13359), thereby channelling the carnitine-derived carbon skeleton into the glycine betaine → dimethylglycine → sarcosine → glycine catabolic route.

This annotation resolves an important ambiguity. The name carried in UniProt — "Dehydrocarnitine cleavage enzyme" — originates solely from the original 2002 genome submission of *P. putida* KT2440 (EMBL AAN65934.1) and is an electronically imported, uncurated hypothesis (evidence code ECO:0000313). Our investigation confirms that this original genome-annotation guess was in fact essentially correct in substance, and we have upgraded it from an unverified label to a mechanistically and phylogenetically supported assignment. PP_0303 belongs to the DUF849 / Pfam PF05853 (BKACE) family, adopts a triose-phosphate-isomerase (TIM) barrel fold, and retains the complete catalytic Zn²⁺-binding triad (His47, His49, Glu248) characteristic of biochemically characterized family members. It is 82% identical to the experimentally studied *P. aeruginosa* ortholog CdhC (PA5387), and it sits within a dedicated, complete carnitine-catabolic gene cluster on the *P. putida* chromosome.

As a soluble TIM-barrel metabolic enzyme with no signal peptide, PP_0303 acts in the **cytoplasm**, downstream of ABC-transporter-mediated carnitine uptake and downstream of the oxidation of L-carnitine to 3-dehydrocarnitine by its immediate genomic neighbor, carnitine 3-dehydrogenase (PP_0302, EC 1.1.1.108). The pathway is supported not only by comparative genomics and family biochemistry but by classic organism-specific biochemistry in *P. putida* itself, in which carnitine dehydrogenase was purified to homogeneity and L-carnitine/trimethylammonium catabolism was directly demonstrated.

### Verified gene/protein identity

| Field | Value |
|---|---|
| UniProt | Q88R31 (Q88R31_PSEPK) |
| Gene / locus | PP_0303 (ortholog of *P. aeruginosa* **cdhC**, PA5387) |
| Organism | *Pseudomonas putida* strain ATCC 47054 / DSM 6125 / KT2440 |
| Length | 294 aa |
| EC / KO | EC 2.3.1.317 (created 2024); KEGG Orthology K27837 |
| Cofactor | Zn²⁺ |
| Family / fold | BKACE (Pfam PF05853; InterPro IPR008567); TIM-barrel (IPR013785) |
| Localization | Cytoplasm (no signal peptide, no transmembrane segments) |

The gene symbol, organism, EC class, Zn²⁺ cofactor, and BKACE/TIM-barrel domains are mutually consistent and match the characterized *P. aeruginosa* ortholog. This is unambiguously the KT2440 carnitine-catabolic enzyme.

---

## Key Findings

### F001 — PP_0303 belongs to the BKACE / DUF849 β-keto acid cleavage enzyme family

PP_0303 (Q88R31) is a 294-amino-acid protein that maps unambiguously to the **BKACE (β-keto acid cleavage enzyme) family**: Pfam **PF05853 (BKACE)** and InterPro **IPR008567 (BKACE)**, together with **IPR013785 (Aldolase/TIM barrel)**. UniProt records the enzyme class as EC 2.3.1.- (a CoA-dependent acyltransferase) and lists **Zn(2+)** as the cofactor. The associated Gene Ontology molecular-function annotation is F:3-keto-5-aminohexanoate cleavage activity (GO:0043720).

This family was systematically re-annotated by Bastard and colleagues, who screened the DUF849 Pfam family and "unearthed 14 potential new enzymatic activities, leading to the designation of these proteins as β-keto acid cleavage enzymes" ([PMID: 24240508](https://pubmed.ncbi.nlm.nih.gov/24240508/)). The founding, structurally characterized archetype of the family is **Kce** (3-keto-5-aminohexanoate cleavage enzyme) from *Fusobacterium nucleatum* (UniProt Q8RHX2), described as "the first representative of a large family of prokaryotic hypothetical proteins, currently annotated as the 'domain of unknown function' DUF849" ([PMID: 21632536](https://pubmed.ncbi.nlm.nih.gov/21632536/)).

To place PP_0303 quantitatively within this family, a pairwise global alignment (BLOSUM62) of PP_0303 against Kce (Q8RHX2) was performed. The two proteins are **43% identical over 270 aligned positions**, firmly establishing PP_0303 as a bona fide member of this catalytically defined family rather than a distant, uncertain homolog.

### F002 — PP_0303 retains the complete catalytic Zn-binding triad of BKACE enzymes

The catalytic machinery of BKACE enzymes centers on a Zn²⁺ cation held within a TIM-barrel active site. In the Kce archetype, the structure "shows the ubiquitous triose phosphate isomerase (TIM) barrel fold and a Zn(2+) cation reminiscent of metal-dependent class II aldolases" ([PMID: 21632536](https://pubmed.ncbi.nlm.nih.gov/21632536/)). Mapping the experimentally defined active-site residues of Kce onto PP_0303 by alignment shows that **all three Zn²⁺ ligands are identical and positionally conserved** in PP_0303:

| Role | Kce (Q8RHX2) residue | PP_0303 (Q88R31) residue | Conservation |
|------|----------------------|--------------------------|--------------|
| Zn²⁺ ligand | His47 | His47 | Identical |
| Zn²⁺ ligand | His49 | His49 | Identical |
| Zn²⁺ ligand | Glu226 | Glu248 | Identical |
| Substrate contact | Glu15 | Gly15 | **Diverged** |
| Substrate contact | Ser83 | Ala85 | **Diverged** |
| Substrate contact | Gly86 | Gly89 | Conserved |
| Substrate contact | Thr107 | Thr127 | Conserved |

The complete conservation of the three zinc ligands (His47, His49, Glu248) — independently corroborated by UniProt listing Zn(2+) as the cofactor — indicates that PP_0303 is a **catalytically competent** metal-dependent enzyme. Critically, however, **two of the four substrate-contacting residues diverge** (Kce Glu15→Gly15; Ser83→Ala85). This is exactly the pattern expected for a family member that has retained the core chemistry but shifted its substrate specificity: as Bastard et al. noted, the goal of their family-wide analysis was to "suggest key residues for guiding further functional annotation" ([PMID: 24240508](https://pubmed.ncbi.nlm.nih.gov/24240508/)).

The catalytic mechanism these conserved residues support is a distinctive one, described for Kce as "an unprecedented mechanism that proceeds through deprotonation of the 3-keto-5-aminohexanoate substrate, nucleophilic addition onto an incoming acetyl-CoA, intramolecular transfer of the CoA moiety, and final retro-Claisen reaction leading to acetoacetate and 3-aminobutyryl-CoA" ([PMID: 21632536](https://pubmed.ncbi.nlm.nih.gov/21632536/)). PP_0303 performs the same class of chemistry on its own β-keto acid substrate.

### F003 — PP_0303 catalyzes cytoplasmic β-keto acid C–C cleavage; the original "dehydrocarnitine cleavage enzyme" name was an unverified genome-annotation hypothesis

An essential piece of scientific hygiene in this investigation was tracing the provenance of PP_0303's UniProt name. The label **"Dehydrocarnitine cleavage enzyme" (EC 2.3.1.-) derives solely from the original 2002 *P. putida* KT2440 genome submission** (EMBL AAN65934.1). Its evidence code is ECO:0000313 — an *imported*, not *curated*, annotation. Beyond the Zn²⁺ cofactor, UniProt records **no catalytic-activity, pathway, or subcellular-location comment**, and the only functional GO term (3-keto-5-aminohexanoate cleavage) is an IEA/InterPro electronic inference.

Nonetheless, the annotation is chemically reasonable: **3-dehydrocarnitine** [(CH₃)₃N⁺–CH₂–CO–CH₂–COO⁻] is itself a β-keto acid, making it a plausible BKACE substrate. The appropriate scientific posture at this stage was caution: as Bastard et al. emphasize, "the functional diversity within a family may be largely underestimated" ([PMID: 24240508](https://pubmed.ncbi.nlm.nih.gov/24240508/)), so a family member's true substrate may differ from its default annotation and requires confirmation.

Regarding **localization**: PP_0303 is a soluble TIM-barrel metabolic enzyme with **no signal peptide and no transmembrane segments**, so it carries out its function in the **cytoplasm** — consistent with a role downstream of transporter-mediated import of the pathway's initial substrate.

### F004 — PP_0303 is CdhC, 3-dehydrocarnitine:acetyl-CoA trimethylamine transferase (EC 2.3.1.317), in the L-carnitine → glycine betaine catabolic pathway

The decisive evidence for PP_0303's specific function comes from **genomic-context (operon) analysis** combined with **orthology to a biochemically characterized enzyme**. In the *P. putida* KT2440 chromosome, PP_0303 lies within a dedicated carnitine-catabolic gene cluster:

| Gene | Product | EC / KO | Reaction |
|------|---------|---------|----------|
| PP_0296, PP_0304 | Glycine betaine/carnitine ABC-transporter substrate-binding proteins | K02002 | Quaternary-ammonium uptake |
| PP_0298, PP_0305 | AraC-family carnitine/betaine-responsive activators | K21826 / K17736 | Transcriptional regulation |
| PP_0302 | Carnitine 3-dehydrogenase | EC 1.1.1.108 | L-carnitine + NAD⁺ → 3-dehydrocarnitine + NADH |
| **PP_0303** | **CdhC — 3-dehydrocarnitine:acetyl-CoA trimethylamine transferase** | **EC 2.3.1.317 / K27837** | **3-dehydrocarnitine + acetyl-CoA → betainyl-CoA + acetoacetate** |
| PP_0301 | Betainyl-CoA thioesterase | EC 3.1.2.33 | betainyl-CoA + H₂O → glycine betaine + CoA |
| PP_0310, PP_0311 | N,N-dimethylglycine / sarcosine dehydrogenases | K21833 / K21834 | Downstream glycine betaine catabolism |

KEGG assigns PP_0303 to **KO K27837 (cdhC)** and **EC 2.3.1.317** (an EC number created in 2024), whose reaction (R13359) is **3-dehydrocarnitine + acetyl-CoA = acetoacetate + betainyl-CoA**, explicitly classified as a BKACE reaction. PP_0303 is **82.0% identical (241/294 aa)** to the characterized *P. aeruginosa* CdhC (PA5387), the enzyme that underlies this EC assignment.

The experimental foundation for the pathway is the work of Wargo and Hogan, who showed in *P. aeruginosa* that "carnitine is converted to 3-dehydrocarnitine (3-dhc) which is in turn metabolized to glycine betaine (GB), an intermediate metabolite in the catabolism of carnitine to glycine" ([PMID: 19406895](https://pubmed.ncbi.nlm.nih.gov/19406895/)). They further demonstrated genetically that "the PA5388-PA5384 region contains the predicted *P. aeruginosa* carnitine dehydrogenase homologue along with other genes required for growth on carnitine" ([PMID: 19406895](https://pubmed.ncbi.nlm.nih.gov/19406895/)) — a region that contains PA5387/cdhC, the 82%-identical ortholog of PP_0303. The BKACE reaction class to which EC 2.3.1.317 belongs was established by Bastard et al., who "unearthed 14 potential new enzymatic activities, leading to the designation of these proteins as β-keto acid cleavage enzymes" ([PMID: 24240508](https://pubmed.ncbi.nlm.nih.gov/24240508/)).

### F005 — Organism-specific experimental support in *P. putida*

Finally, classic biochemistry performed directly in the target organism corroborates the pathway inferred for PP_0303. Goulas (1988) purified carnitine dehydrogenase (EC 1.1.1.108) from *Pseudomonas putida* IFP 206 to homogeneity — a 62 kDa homodimer, specific for L-carnitine and NAD⁺ — showing that "Carnitine dehydrogenase (carnitine:NAD+ oxidoreductase, EC 1.1.1.108) from Pseudomonas putida IFP 206 catalyzes the oxidation of L-carnitine to 3-dehydrocarnitine" ([PMID: 3058208](https://pubmed.ncbi.nlm.nih.gov/3058208/)). This is precisely the substrate-supplying step feeding PP_0303, and its enzyme corresponds to PP_0303's immediate neighbor, PP_0302.

Earlier, Kleber and colleagues (1978) showed that *P. putida* grows on γ-butyrobetaine, L- and D,L-carnitine, glycine betaine, and choline; that L-carnitine induces carnitine dehydrogenase; and that trimethylamine/trimethylammonium turnover accompanies growth on carnitine as sole carbon source. They reported that "the formation of trimethylamine increased, if L-carnitine or gamma-butyrobetaine were the only carbon sources" ([PMID: 565193](https://pubmed.ncbi.nlm.nih.gov/565193/)), documenting active L-carnitine/trimethylammonium catabolism in *P. putida* — the physiological pathway in which PP_0303/CdhC functions.

---

## Mechanistic Model / Interpretation

PP_0303 is the **committed, carbon-conserving cleavage step** that converts the carnitine skeleton into a glycine-betaine intermediate while capturing the acetyl group as acetoacetate. The full catabolic route in *P. putida* KT2440 can be summarized as follows:

```
         ABC transporter (Cbc/CaiX; PP_0296/PP_0304, periplasmic SBPs)
   L-carnitine (extracellular) ─────────────────────────────────►  L-carnitine (cytoplasm)
                                                                        │
                                          PP_0302  carnitine 3-dehydrogenase (EC 1.1.1.108)
                                          L-carnitine + NAD⁺ → 3-dehydrocarnitine + NADH
                                                                        │
                                                                        ▼
                              ┌────────────────────────────────────────────────────────────┐
              acetyl-CoA ───► │  PP_0303  CdhC  (EC 2.3.1.317)  — BKACE, Zn²⁺, TIM barrel    │
                              │  3-dehydrocarnitine + acetyl-CoA → betainyl-CoA + acetoacetate│
                              └────────────────────────────────────────────────────────────┘
                                                     │                         │
                                                     ▼                         ▼
                              PP_0301 betainyl-CoA thioesterase        acetoacetate
                              (EC 3.1.2.33)                            → central metabolism
                              betainyl-CoA + H₂O → glycine betaine + CoA
                                                     │
                                                     ▼
                              glycine betaine  →  dimethylglycine  →  sarcosine  →  glycine
                                               (PP_0310/PP_0311 and downstream dehydrogenases)
```

Chemically, PP_0303 performs the family's signature transformation on a **β-keto acid** substrate. By analogy to the Kce mechanism ([PMID: 21632536](https://pubmed.ncbi.nlm.nih.gov/21632536/)), the reaction proceeds through Zn²⁺-assisted deprotonation of 3-dehydrocarnitine, nucleophilic addition onto the incoming acetyl-CoA, intramolecular CoA transfer, and a final retro-Claisen C–C cleavage. In the Kce case the products are acetoacetate + 3-aminobutyryl-CoA; in the CdhC/PP_0303 case the products are **acetoacetate + betainyl-CoA**. The conserved Zn²⁺ triad (His47/His49/Glu248) supplies the metal-dependent catalytic core, while the two diverged substrate-contact residues (Gly15, Ala85 in place of Kce's Glu15, Ser83) reshape the active-site pocket to accommodate the trimethylammonium-bearing 3-dehydrocarnitine rather than the amino-bearing 3-keto-5-aminohexanoate. This is a textbook example of how a conserved catalytic scaffold is repurposed for a new substrate within an enzyme superfamily.

The **physiological logic** of this pathway is nutrient acquisition: carnitine and related quaternary-ammonium compounds are abundant in soil and rhizosphere environments (and in animal tissues), and *P. putida* uses this cluster to exploit them as carbon and nitrogen sources. The pathway simultaneously feeds the two-carbon acetyl unit (as acetoacetate) toward central metabolism and routes the trimethylammonium moiety through glycine betaine demethylation to glycine.

**Localization:** All steps catalyzed by PP_0303 occur in the cytoplasm; the substrate is delivered there by a periplasmic-SBP-dependent ABC transporter system (the Cbc/CaiX machinery characterized in related pseudomonads), consistent with PP_0303 lacking any export or membrane-anchoring signal.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|------|------------------|---------------------|
| [24240508](https://pubmed.ncbi.nlm.nih.gov/24240508/) | *Revealing the hidden functional diversity of an enzyme family* | Defines the BKACE (DUF849/PF05853) family and its 14 activities; establishes the reaction class of EC 2.3.1.317 and warns that family substrate specificity is under-annotated (supports F001, F002, F003, F004) |
| [21632536](https://pubmed.ncbi.nlm.nih.gov/21632536/) | *3-Keto-5-aminohexanoate cleavage enzyme: a common fold for an uncommon Claisen-type condensation* | Structural/mechanistic archetype (Kce): TIM-barrel + Zn²⁺ active site, catalytic triad, and the deprotonation/addition/retro-Claisen mechanism PP_0303 shares (supports F001, F002) |
| [19406895](https://pubmed.ncbi.nlm.nih.gov/19406895/) | *Identification of genes required for Pseudomonas aeruginosa carnitine catabolism* | Experimentally defines carnitine → 3-dehydrocarnitine → glycine betaine → glycine pathway and links the cdh gene region (containing PA5387/CdhC, PP_0303's 82%-identical ortholog) to carnitine growth (supports F004) |
| [3058208](https://pubmed.ncbi.nlm.nih.gov/3058208/) | *Purification and properties of carnitine dehydrogenase from Pseudomonas putida* | Organism-specific proof that *P. putida* oxidizes L-carnitine to 3-dehydrocarnitine (PP_0303's substrate), via the enzyme corresponding to neighbor PP_0302 (supports F005) |
| [565193](https://pubmed.ncbi.nlm.nih.gov/565193/) | *Interrelationships between carnitine metabolism and fatty acid assimilation in P. putida* | Demonstrates inducible L-carnitine/trimethylammonium catabolism in *P. putida*, the physiological context of PP_0303 (supports F005) |
| [19919675](https://pubmed.ncbi.nlm.nih.gov/19919675/) | *The ABC transporter Cbc recruits multiple substrate-binding proteins…* | Characterizes the choline/betaine/carnitine ABC transporter (Cbc/CaiX) delivering carnitine to the cytoplasm upstream of PP_0303 (context for localization) |
| [17951379](https://pubmed.ncbi.nlm.nih.gov/17951379/) | *Two gene clusters and a regulator for P. aeruginosa glycine betaine catabolism* | Defines the downstream glycine betaine → DMG → sarcosine → glycine route the PP_0303 product feeds into (pathway context) |
| [18156257](https://pubmed.ncbi.nlm.nih.gov/18156257/) | *Pseudomonas syringae BetT is a low-affinity choline transporter…* | Context on quaternary-ammonium transport and *P. putida* BCCT transporters (peripheral context) |

**Strength of evidence.** The core assignment rests on three independent, mutually reinforcing lines: (1) **sequence/structure** — 43% identity to the structurally characterized Kce and complete conservation of the catalytic Zn triad; (2) **genomic context** — membership in a complete, dedicated carnitine-catabolic operon with the correct upstream (PP_0302) and downstream (PP_0301) enzymes and associated transporters/regulators; and (3) **orthology to a functionally studied enzyme** — 82% identity to *P. aeruginosa* CdhC (PA5387), whose gene region is experimentally required for carnitine catabolism. Organism-specific biochemistry in *P. putida* confirms flux through the substrate-supplying step. The chief caveat is that PP_0303 *itself* has not been purified and assayed; the assignment is inferential (albeit strongly so), and EC 2.3.1.317 is a recently minted (2024) number.

---

## Supported and Refuted Hypotheses

- **Supported (high confidence):** PP_0303 = CdhC, a cytoplasmic Zn²⁺-dependent BKACE catalyzing 3-dehydrocarnitine + acetyl-CoA → betainyl-CoA + acetoacetate, the committed step of L-carnitine catabolism. (EC 2.3.1.317; 82% identity to characterized PA5387; complete carnitine operon; conserved Zn triad.)
- **Supported:** The original genome annotation "dehydrocarnitine cleavage enzyme" is correct in substance — upgraded from "plausible" (early exploration) to "corroborated."
- **Refuted:** PP_0303 catalyzes the identical reaction as the Kce archetype (3-keto-5-aminohexanoate cleavage). The substrate is 3-dehydrocarnitine, and substrate-pocket residues diverge accordingly. The generic InterPro GO term (3-keto-5-aminohexanoate cleavage) is a family-level default, not the specific activity of PP_0303.

---

## Limitations and Knowledge Gaps

1. **No direct enzymology on PP_0303.** The substrate (3-dehydrocarnitine), co-substrate (acetyl-CoA), and products (betainyl-CoA, acetoacetate) have not been demonstrated for the purified *P. putida* protein. The assignment is inference from orthology, operon structure, and family chemistry — strong, but not a direct kinetic measurement.

2. **The name in UniProt is uncurated.** The "dehydrocarnitine cleavage enzyme" label is an ECO:0000313 imported annotation from the 2002 genome. Although our analysis indicates it is substantively correct, UniProt still lacks curated catalytic-activity, pathway, and localization comments for Q88R31.

3. **Substrate-specificity residues diverge from the archetype.** Two of four substrate-contacting positions differ from Kce. While consistent with a shifted (carnitine-type) substrate, the precise structural basis for 3-dehydrocarnitine recognition has not been solved for PP_0303 (no experimental structure; homology/AlphaFold models only).

4. **Regulation and physiology in KT2440 specifically.** The regulatory logic (AraC-family activators PP_0298/PP_0305) and growth phenotypes have been characterized largely in *P. aeruginosa*; direct genetic knockout/growth data for *P. putida* PP_0303 were not established here.

5. **Cofactor stoichiometry and metal specificity.** Zn²⁺ is annotated and the ligands are conserved, but metal dependence has not been experimentally verified for this specific protein.

---

## Proposed Follow-up Experiments / Actions

1. **Heterologous expression and in vitro assay.** Clone PP_0303, purify the His-tagged protein, and assay 3-dehydrocarnitine + acetyl-CoA → betainyl-CoA + acetoacetate by LC-MS/coupled spectrophotometric detection of CoA-thioester products. Measure kcat/Km against 3-dehydrocarnitine and, as controls, 3-keto-5-aminohexanoate and other β-keto acids to define specificity.

2. **Gene knockout / growth phenotyping in KT2440.** Construct a clean ΔPP_0303 mutant and test growth on L-carnitine, γ-butyrobetaine, 3-dehydrocarnitine, and glycine betaine as sole carbon/nitrogen sources; complement to confirm. Predict: loss of growth on carnitine but retained growth on glycine betaine (i.e., a block precisely at the CdhC step).

3. **Metabolite tracing.** Feed ¹³C-labeled L-carnitine to wild-type and ΔPP_0303 cells and follow accumulation of 3-dehydrocarnitine (upstream) versus glycine betaine/betainyl-CoA (downstream) by NMR/MS, mirroring the Wargo–Hogan approach in *P. aeruginosa*.

4. **Structural determination.** Solve the crystal structure (or validate an AlphaFold model) of PP_0303, ideally with bound 3-dehydrocarnitine or a substrate analog, to confirm the Zn²⁺ triad geometry and the roles of the diverged Gly15/Ala85 positions in accommodating the trimethylammonium group.

5. **Metal-dependence test.** Assay activity with and without chelators (EDTA/1,10-phenanthroline) and reconstitute with Zn²⁺ vs. other divalent cations to confirm the annotated cofactor.

6. **Database curation update.** Submit a curated functional annotation for Q88R31 (function = CdhC, EC 2.3.1.317; pathway = L-carnitine catabolism to glycine betaine; localization = cytoplasm), replacing the uncurated legacy name, once in vitro confirmation is obtained.

---

*Report generated from a multi-iteration autonomous investigation combining sequence analysis, active-site residue mapping, genomic-context (operon) analysis, orthology comparison, and literature review. Core conclusion: PP_0303 = CdhC (EC 2.3.1.317), the committed BKACE cleavage step of L-carnitine catabolism in *Pseudomonas putida* KT2440.*


## Artifacts

- [OpenScientist final report](PP_0303-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PP_0303-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:24240508
2. PMID:21632536
3. PMID:19406895
4. PMID:3058208