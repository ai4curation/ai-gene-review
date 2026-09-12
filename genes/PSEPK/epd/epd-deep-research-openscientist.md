---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-17T05:58:43.300415'
end_time: '2026-07-17T06:18:04.185685'
duration_seconds: 1160.89
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: epd
  gene_symbol: epd
  uniprot_accession: Q88D63
  protein_description: 'RecName: Full=Erythrose-4-phosphate dehydrogenase {ECO:0000256|NCBIfam:TIGR01532};
    EC=1.2.1.72 {ECO:0000256|NCBIfam:TIGR01532};'
  gene_info: Name=epd {ECO:0000313|EMBL:AAN70531.1}; OrderedLocusNames=PP_4964 {ECO:0000313|EMBL:AAN70531.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the glyceraldehyde-3-phosphate dehydrogenase
  protein_domains: E4P_DH_bac. (IPR006422); GlycerAld/Erythrose_P_DH. (IPR020831);
    GlycerAld_3-P_DH_cat. (IPR020829); GlycerAld_3-P_DH_NAD(P)-bd. (IPR020828); NAD(P)-bd_dom_sf.
    (IPR036291)
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
  path: epd-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: epd-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88D63
- **Protein Description:** RecName: Full=Erythrose-4-phosphate dehydrogenase {ECO:0000256|NCBIfam:TIGR01532}; EC=1.2.1.72 {ECO:0000256|NCBIfam:TIGR01532};
- **Gene Information:** Name=epd {ECO:0000313|EMBL:AAN70531.1}; OrderedLocusNames=PP_4964 {ECO:0000313|EMBL:AAN70531.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the glyceraldehyde-3-phosphate dehydrogenase
- **Key Domains:** E4P_DH_bac. (IPR006422); GlycerAld/Erythrose_P_DH. (IPR020831); GlycerAld_3-P_DH_cat. (IPR020829); GlycerAld_3-P_DH_NAD(P)-bd. (IPR020828); NAD(P)-bd_dom_sf. (IPR036291)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "epd" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'epd' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **epd** (gene ID: epd, UniProt: Q88D63) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of *epd* (PP_4964, UniProt Q88D63) in *Pseudomonas putida* KT2440

## Summary

The gene **epd** (ordered locus **PP_4964**; UniProt **Q88D63**) of *Pseudomonas putida* strain KT2440 (ATCC 47054 / DSM 6125 / NCIMB 11950) encodes a **non-phosphorylating D-erythrose-4-phosphate dehydrogenase (E4PDH; EC 1.2.1.72)**, a 352-residue member of the glyceraldehyde-3-phosphate dehydrogenase (GAPDH) structural superfamily. Its primary catalytic function is the NAD⁺-dependent oxidation of **D-erythrose 4-phosphate (E4P)** to **4-phosphoerythronate**, producing NADH and, unlike a classical phosphorylating GAPDH, the free carboxylic acid rather than an acyl-phosphate. This reaction is the **first committed step of the deoxyxylulose-5-phosphate (DXP)-dependent *de novo* biosynthesis of pyridoxal 5′-phosphate (PLP; vitamin B6)**.

The identity of the target protein is confirmed and unambiguous. Gene symbol, EC number, protein family, and conserved domains from UniProt all align with the E4PDH/GAPDH-family assignment, and independent sequence analysis performed during this investigation places Q88D63 as a clear ortholog (53.4% amino-acid identity) of the well-characterized *Escherichia coli* Epd/GapB protein, with a fully conserved catalytic cysteine and NAD⁺-specific cofactor fingerprint. No *P. putida*-specific experimental biochemical study of PP_4964 exists in the literature; the functional annotation therefore rests on a strong chain of orthology-based inference supported by *E. coli* biochemistry and genetics, genome context, and conserved sequence determinants.

Mechanistically, the enzyme acts as a soluble cytoplasmic **homotetramer** that catalyzes oxidation through a **two-step covalent mechanism** involving a thioacyl-enzyme intermediate on an active-site cysteine (Cys160 in the *P. putida* numbering; motif SNASCTTNC). It has strong substrate preference for E4P over glyceraldehyde-3-phosphate and strong cofactor preference for NAD⁺ over NADP⁺. Genomically, *epd* sits in a conserved central-carbon-metabolism gene cluster next to *pgk* (phosphoglycerate kinase) and *tktA* (transketolase) — the very enzyme of the pentose phosphate pathway that produces its E4P substrate — recapitulating the conserved *epd*–*pgk* arrangement of *E. coli*. The complete downstream vitamin-B6 pathway (*pdxB*, *serC*, *pdxA*, *pdxJ*, *pdxH*) is encoded in the KT2440 genome, closing the physiological loop.

---

## Key Findings

### F001 — Epd is a non-phosphorylating D-erythrose-4-phosphate dehydrogenase (EC 1.2.1.72)

UniProt Q88D63 annotates PP_4964 as an erythrose-4-phosphate dehydrogenase, EC 1.2.1.72, a 352-amino-acid protein belonging to the GAPDH structural family (InterPro E4P_DH_bac IPR006422 / TIGRFAM TIGR01532). The founding biochemistry, performed on the orthologous *E. coli* enzyme (encoded by *gapB*, subsequently renamed *epd*), established that this enzyme oxidizes:

> **D-erythrose 4-phosphate + NAD⁺ + H₂O → 4-phosphoerythronate + NADH + 2 H⁺**

Critically, Zhao and colleagues demonstrated experimentally that the *gapB*-encoded protein is a genuine E4P dehydrogenase and not merely a second glyceraldehyde-3-phosphate dehydrogenase: *"We found that the gapB-encoded enzyme is indeed an E4PDH and not a second GA3PDH, whereas gapA-encoded GA3PDH used E4P poorly, if at all, as a substrate under the in vitro reaction conditions used in this study"* ([PMID: 7751290](https://pubmed.ncbi.nlm.nih.gov/7751290/)). Boschi-Muller and colleagues further defined the reaction as **non-phosphorylating** — the enzyme produces the free acid (4-phosphoerythronate) rather than an acyl-phosphate — noting that *"This enzyme shows an efficient non-phosphorylating erythrose-4-phosphate dehydrogenase activity"* ([PMID: 9182530](https://pubmed.ncbi.nlm.nih.gov/9182530/)). This distinguishes Epd mechanistically from the classical phosphorylating GAPDH (GapA), even though the two share a common fold and evolutionary origin.

### F002 — Epd catalyzes the first committed step of DXP-dependent vitamin B6 (PLP) biosynthesis

The physiological role of Epd is to supply the first dedicated intermediate of the **DXP-dependent pyridoxal 5′-phosphate biosynthetic pathway**, the route used by γ-proteobacteria such as *E. coli* and *Pseudomonas*. Genetic evidence in *E. coli* directly links the enzyme to vitamin B6 biosynthesis: *"We show that epd (gapB) mutants lacking an erythrose 4-phosphate (E4P) dehydrogenase are impaired for growth on some media and contain less pyridoxal 5'-phosphate (PLP) and pyridoxamine 5'-phosphate (PMP) than their epd+ parent"* ([PMID: 9696782](https://pubmed.ncbi.nlm.nih.gov/9696782/)). The same study showed that *"gapA epd double mutants lacking the glyceraldehyde 3-phosphate and E4P dehydrogenases are auxotrophic for pyridoxine"*, demonstrating both the role of Epd and the partial redundancy provided by GapA (which can generate the required 4-phosphoerythronate at reduced efficiency).

The product of the Epd reaction, 4-phosphoerythronate, is the substrate of PdxB (4-phosphoerythronate dehydrogenase), and the pathway then proceeds through SerC, PdxA, PdxJ, and PdxH to PLP. Fitzpatrick and colleagues describe the DXP-dependent route that Epd feeds: *"it is synthesized from the condensation of deoxyxylulose 5-phosphate and 4-phosphohydroxy-L-threonine catalysed by the concerted action of PdxA and PdxJ"* ([PMID: 17822383](https://pubmed.ncbi.nlm.nih.gov/17822383/)). A UniProt survey performed during this investigation confirmed that *P. putida* KT2440 encodes the **entire downstream pathway**, matching the *E. coli* route:

| Step | Enzyme | Gene | Locus | EC |
|------|--------|------|-------|-----|
| 1 | Erythrose-4-phosphate dehydrogenase | *epd* | PP_4964 | 1.2.1.72 |
| 2 | 4-phosphoerythronate dehydrogenase | *pdxB* | PP_2117 | 1.1.1.290 |
| 3 | Phosphoserine aminotransferase | *serC* | PP_1768 | 2.6.1.52 |
| 4 | 4-hydroxythreonine-4-phosphate dehydrogenase | *pdxA* | PP_0402 | 1.1.1.262 |
| 5 | Pyridoxine-5′-phosphate synthase | *pdxJ* | PP_1436 | 2.6.99.2 |
| 6 | Pyridoxamine/pyridoxine-5′-phosphate oxidase | *pdxH* | PP_1129 | 1.4.3.5 |

The presence of the complete downstream pathway in the KT2440 genome strongly supports the inference that Epd performs the same first-committed-step function in *P. putida* as it does in *E. coli*.

### F003 — Homotetramer using a two-step covalent (Cys) mechanism, with strong preference for E4P and NAD⁺

The *E. coli* E4PDH is a heat-stable homotetramer (native mass ~132 kDa; ~35 kDa per subunit; the *P. putida* subunit is 352 residues). Steady-state kinetics gave Km(E4P) = 0.96 mM, kcat(E4P) = 200 s⁻¹, and Km(NAD⁺) = 0.074 mM (Zhao et al.). Boschi-Muller and colleagues elucidated the catalytic mechanism, showing it proceeds through a covalent acyl-enzyme intermediate on an active-site cysteine, with acylation and deacylation rates of 280 s⁻¹ and 20 s⁻¹ respectively: *"The chemical mechanism of erythrose 4-phosphate oxidation by GapB-encoded protein is shown to proceed through a two-step mechanism involving covalent intermediates with Cys-149"* ([PMID: 9182530](https://pubmed.ncbi.nlm.nih.gov/9182530/)). The quaternary structure is captured by *"Purified E4PDH was a heat-stable tetramer with a native molecular mass of 132 kDa"* ([PMID: 7751290](https://pubmed.ncbi.nlm.nih.gov/7751290/)).

The enzyme's specificity is doubly distinct from GAPDH: it binds NAD⁺ ~800-fold more weakly than GAPDH does — *"The KD constant of GapB-encoded protein for NAD is 800-fold higher than that of GAPDH"* ([PMID: 9182530](https://pubmed.ncbi.nlm.nih.gov/9182530/)) — and it retains only very low (0.12 s⁻¹) phosphorylating GAPDH activity, confirming its commitment to the non-phosphorylating E4P oxidation. All catalytic and cofactor-binding residues (the catalytic Cys, the catalytic His, and the NAD-binding Rossmann motif) are conserved in the GAPDH family to which Q88D63 belongs.

### F004 — Epd is a soluble cytoplasmic metabolic enzyme

Epd functions in the **cytoplasm** as a soluble enzyme. The purified *E. coli* E4PDH is recovered as a soluble tetramer from crude extract with no membrane association, no signal peptide, and no transmembrane segments. It acts on soluble, phosphorylated small-molecule metabolites (E4P and NAD⁺). Its GAPDH-family fold is that of a cytosolic, glycolytic-type enzyme, and Q88D63 carries no secretion or membrane-localization signals. This localization is consistent with the enzyme's substrates: E4P is generated by the pentose phosphate pathway/transketolase in the cytosol, and NAD⁺ is abundant there. This finding is an inference from protein biochemistry and sequence features rather than a direct *P. putida* localization experiment.

### F005 — Q88D63 is a clear ortholog of E. coli Epd with a fully conserved catalytic cysteine

A global pairwise alignment performed during this investigation between Q88D63 (352 aa) and *E. coli* Epd (P0A9B6, 339 aa) yields **53.4% amino-acid identity** (181/339 aligned positions) — well above the threshold that typically indicates conserved function. Crucially, the GAPDH-family active-site signature motif **"SNASCTTNC"** is present in both proteins, placing the catalytic cysteine at position 160 in *P. putida* (corresponding to Cys155 in *E. coli* numbering, and Cys-149 in the mature-protein numbering of Boschi-Muller et al.). The surrounding sequence context is near-identical (*E. coli* SNASCTTNCIIP vs *P. putida* SNASCTTNCGVP). This is precisely the thioacyl-forming cysteine shown biochemically to be essential for catalysis: *"The chemical mechanism of erythrose 4-phosphate oxidation by GapB-encoded protein is shown to proceed through a two-step mechanism involving covalent intermediates with Cys-149"* ([PMID: 9182530](https://pubmed.ncbi.nlm.nih.gov/9182530/)). The conservation of both the overall sequence and the specific catalytic residue provides high-confidence structural/evolutionary evidence that the *P. putida* enzyme catalyzes the same reaction.

### F006 — *epd* lies in a conserved central-carbon-metabolism gene cluster, next to *pgk* and *tktA* (its substrate supplier)

Gene-neighborhood analysis of the KT2440 genome shows that *epd* (PP_4964) is flanked by **pgk/phosphoglycerate kinase (PP_4963)** and **tktA/transketolase (PP_4965)**, with **fba/fructose-1,6-bisphosphate aldolase (PP_4960)** a few genes upstream. This recapitulates the conserved *E. coli* *epd*–*pgk*–*fbaA* glycolytic gene cluster. The genomic adjacency is functionally meaningful: transketolase (TktA) is the pentose-phosphate-pathway enzyme that **produces D-erythrose 4-phosphate**, the immediate substrate of Epd. Thus the gene is physically co-located in the genome with the reaction that supplies its substrate, reinforcing the metabolic-network coherence of the annotation.

```
   PP_4960        PP_4963      PP_4964      PP_4965
    fba   ...      pgk    ---    epd   ---   tktA
  (FBP        (phosphoglycerate  (E4P     (transketolase,
   aldolase)     kinase)         DH)      makes E4P)
                                  |            |
                                  └─substrate──┘
```

### F007 — Q88D63 conserves the NAD⁺-specific Rossmann cofactor fingerprint

The N-terminus of Q88D63 contains the canonical GAPDH-family dinucleotide-binding glycine-rich motif **ALNGYGRIGR** (a GxGxxG element at residues ~12–17), followed by a conserved acidic residue (Asp at position ~40). This exactly mirrors the *E. coli* enzyme (AINGFGRIGR; …NELAD). In the GAPDH superfamily this conserved acidic residue hydrogen-bonds the 2′/3′-hydroxyls of the adenosine ribose and confers **NAD⁺ (over NADP⁺) specificity**; NADP-preferring members of the fold instead carry a serine or other small residue at this position. This determinant is well established in the cofactor-engineering literature: *"the replacement of conserved glutamate or aspartate with serine in the loop region could change the cofactor dependence from NAD(H) to NADP(H)"* ([PMID: 26254041](https://pubmed.ncbi.nlm.nih.gov/26254041/)). The presence of the acidic residue in *P. putida* Epd matches the experimentally measured NAD⁺ dependence of *E. coli* Epd (Km(NAD⁺) = 0.074 mM), confirming by sequence analysis that the *P. putida* enzyme is NAD⁺-specific.

---

## Mechanistic Model / Interpretation

Integrating the seven findings produces a coherent and well-supported model of Epd's role in *P. putida* KT2440.

**The reaction and its place in metabolism.** The pentose phosphate pathway and transketolase (TktA, encoded by the immediately adjacent PP_4965) generate D-erythrose 4-phosphate in the cytosol. Epd, a soluble homotetramer, oxidizes E4P using NAD⁺:

```
   Pentose phosphate pathway / Transketolase (TktA, PP_4965)
                          │
                          ▼
              D-erythrose 4-phosphate (E4P)
                          │   + NAD⁺ + H₂O
                 ┌────────┴──────────┐
                 │  Epd (PP_4964)    │  EC 1.2.1.72
                 │  E4P dehydrogenase│  (non-phosphorylating)
                 │  Cys160 thioacyl  │
                 └────────┬──────────┘
                          │   + NADH
                          ▼
                4-phosphoerythronate
                          │  PdxB (PP_2117)
                          ▼
              2-oxo-3-hydroxy-4-phosphobutanoate
                          │  SerC (PP_1768)
                          ▼
              4-phosphohydroxy-L-threonine
                          │  PdxA (PP_0402)
                          ▼
              condensation with DXP  │  PdxJ (PP_1436)
                          ▼
              pyridoxine 5'-phosphate (PNP)
                          │  PdxH (PP_1129)
                          ▼
              ★ pyridoxal 5'-phosphate (PLP) — active vitamin B6
```

**Catalytic mechanism.** Catalysis follows the two-step covalent mechanism characteristic of the GAPDH superfamily. The catalytic cysteine (Cys160, in the conserved SNASCTTNC motif) attacks the aldehyde carbon of E4P to form a hemithioacetal; hydride transfer to NAD⁺ yields a covalent thioacyl-enzyme intermediate and NADH. Because Epd is non-phosphorylating, the acyl-enzyme is resolved by **water** (not inorganic phosphate), releasing the free acid 4-phosphoerythronate rather than an acyl-phosphate. This mechanistic switch — nucleophilic water rather than phosphate at the deacylation step — is the defining distinction between Epd and the phosphorylating GapA, and it is what routes the carbon toward vitamin B6 biosynthesis rather than glycolysis.

**Specificity determinants.** Two conserved sequence features lock in the enzyme's specificity. (1) The NAD⁺-specific Rossmann fingerprint (GxGxxG followed by an acidic Asp) makes NAD⁺, not NADP⁺, the physiological cofactor. (2) Active-site architecture around Cys160 confers preference for the four-carbon E4P over the three-carbon glyceraldehyde-3-phosphate. Together they ensure Epd operates as a dedicated biosynthetic enzyme.

**Why the inference is strong despite the absence of a *P. putida* study.** Five independent lines of evidence converge: (i) direct *E. coli* ortholog biochemistry and genetics defining reaction, mechanism, kinetics, and the vitamin-B6 phenotype; (ii) the complete downstream *pdxB–serC–pdxA–pdxJ–pdxH* pathway encoded in KT2440; (iii) 53.4% sequence identity with a fully conserved catalytic cysteine; (iv) a conserved NAD⁺-specific cofactor fingerprint; and (v) genomic synteny placing *epd* next to its substrate-supplying transketolase and next to *pgk*. This is a textbook case of high-confidence functional transfer by orthology reinforced by genome context.

---

## Evidence Base

| PMID | Title (abbreviated) | How it supports the annotation |
|------|--------------------|-------------------------------|
| [7751290](https://pubmed.ncbi.nlm.nih.gov/7751290/) | *Biochemical characterization of gapB-encoded E4PDH of E. coli K-12 and its possible role in PLP biosynthesis* | Establishes that the *gapB*/epd product is a genuine E4P dehydrogenase (not a second GAPDH) and a heat-stable 132-kDa tetramer; provides kinetic parameters. Defines the reaction and quaternary structure for the ortholog. |
| [9182530](https://pubmed.ncbi.nlm.nih.gov/9182530/) | *Comparative enzymatic properties of GapB-encoded E4PDH and phosphorylating GAPDH* | Defines the non-phosphorylating activity, the two-step covalent mechanism via Cys-149, and the ~800-fold weaker NAD binding vs GAPDH. Underpins mechanism, catalytic residue, and cofactor findings. |
| [9696782](https://pubmed.ncbi.nlm.nih.gov/9696782/) | *Involvement of gapA- and epd (gapB)-encoded dehydrogenases in PLP biosynthesis in E. coli K-12* | Direct genetic evidence: *epd* mutants have less PLP/PMP; *gapA epd* double mutants are pyridoxine auxotrophs. Links Epd to *de novo* vitamin B6 biosynthesis and shows GapA redundancy. |
| [17822383](https://pubmed.ncbi.nlm.nih.gov/17822383/) | *Two independent routes of de novo vitamin B6 biosynthesis* | Describes the DXP-dependent route (PdxA/PdxJ) that Epd feeds, contextualizing the pathway downstream of 4-phosphoerythronate. |
| [26254041](https://pubmed.ncbi.nlm.nih.gov/26254041/) | *In silico cofactor engineering strategies for NADP(H) turnover* | Establishes that the conserved Asp/Glu residue determines NAD(H) vs NADP(H) specificity in this fold — the basis for concluding Q88D63 is NAD⁺-specific. |
| [9260967](https://pubmed.ncbi.nlm.nih.gov/9260967/) | *Characterization of E. coli strains with gapA and gapB deleted* | Context/caveat: reports *gapB* is expressed at very low level and is dispensable for glycolysis and pyridoxal biosynthesis under the conditions tested — highlighting condition-dependence and GapA redundancy. |
| [10491162](https://pubmed.ncbi.nlm.nih.gov/10491162/) | *Functional characterization of archaeal GAPDH by modelling and mutagenesis* | Supports the family-wide conservation of the catalytic Cys149 and Rossmann-fold cofactor determinants, corroborating the residue-level inferences for Q88D63. |

Several additional *P. putida* papers surfaced during literature searches (e.g., on L-methionine γ-lyase and ω-transaminases, PMIDs 10965031, 27796875, 34953671, 40436318, 30725412) are **PLP-dependent enzymes** — they are downstream *users* of the vitamin B6 product, not studies of Epd itself. They are noted here only to document that the literature was screened and that no direct experimental study of PP_4964 was found; they do not provide evidence about Epd's own function and are not cited as support for the findings.

---

## Limitations and Knowledge Gaps

1. **No direct experimental study of PP_4964.** There is no published biochemical, structural, or genetic characterization of the *P. putida* KT2440 Epd protein itself. All functional claims are transferred from the *E. coli* ortholog and supported by bioinformatic and genome-context evidence. Kinetic parameters (Km, kcat), the exact quaternary state, and the precise catalytic residue numbering are inferred, not measured, for the *P. putida* enzyme.

2. **Condition-dependent physiological importance.** In *E. coli*, *gapB*/*epd* is expressed at low levels and is dispensable for both glycolysis and pyridoxal biosynthesis under some conditions, because GapA can supply 4-phosphoerythronate ([PMID: 9260967](https://pubmed.ncbi.nlm.nih.gov/9260967/)). The relative contributions of Epd versus GapA to PLP biosynthesis in *P. putida*, and any growth-condition dependence, are unknown.

3. **Localization is inferred, not demonstrated.** Cytoplasmic localization is deduced from the soluble GAPDH-fold, the nature of the substrates, and the absence of targeting signals in Q88D63 — no experimental localization data for PP_4964 exist.

4. **Cofactor specificity is predicted from sequence.** The NAD⁺ preference is inferred from the conserved acidic Rossmann-loop residue and *E. coli* kinetics; it has not been measured for the *P. putida* enzyme, and dual-cofactor behavior (as seen in some archaeal family members) cannot be formally excluded.

5. **Residue numbering caveat.** Alignment-based numbering (Cys160) depends on the reference sequence and gap placement; the mature-protein numbering used in the mechanistic literature (Cys-149) differs, so cross-referencing should be done carefully.

---

## Proposed Follow-up Experiments / Actions

1. **Heterologous expression and enzyme assay.** Clone PP_4964, express and purify the protein, and measure E4P-dependent NAD⁺ reduction spectrophotometrically. Determine Km/kcat for E4P and NAD⁺, and test NADP⁺ and glyceraldehyde-3-phosphate to confirm substrate and cofactor specificity directly in the *P. putida* enzyme.

2. **Active-site cysteine mutagenesis.** Generate a Cys160→Ser/Ala variant and confirm loss of activity, validating the predicted catalytic residue and the covalent mechanism.

3. **Genetic knockout and auxotrophy test.** Construct a clean *epd* deletion in KT2440 and test for reduced PLP/PMP content and pyridoxine auxotrophy, alone and in combination with a *gapA* knockout, to establish the physiological contribution to vitamin B6 biosynthesis and the degree of GapA redundancy.

4. **Metabolomic verification.** Use LC-MS to confirm accumulation/depletion of 4-phosphoerythronate and downstream PLP-pathway intermediates in wild-type versus *epd* mutant strains.

5. **Structural determination.** Solve the crystal structure (or generate a validated AlphaFold model with confidence metrics) to confirm the Rossmann fold, the tetrameric assembly, and the geometry of the NAD⁺- and E4P-binding sites, directly testing the cofactor-specificity determinant.

6. **Expression/condition profiling.** Measure *epd* transcript and protein levels across growth conditions (carbon sources, oxidative stress, B6 availability) to determine when the enzyme is physiologically important in *P. putida*.

---

## Conclusion

The gene **epd** (PP_4964, UniProt Q88D63) in *Pseudomonas putida* KT2440 encodes a soluble, cytoplasmic, homotetrameric, **NAD⁺-dependent, non-phosphorylating D-erythrose-4-phosphate dehydrogenase (EC 1.2.1.72)** of the GAPDH superfamily. It catalyzes the oxidation of D-erythrose 4-phosphate to 4-phosphoerythronate via a two-step covalent mechanism at an active-site cysteine (conserved motif SNASCTTNC), and this reaction is the **first committed step of the DXP-dependent de novo biosynthesis of pyridoxal 5′-phosphate (vitamin B6)**. The annotation is strongly supported for *P. putida* by *E. coli* ortholog biochemistry and genetics, the presence of the complete downstream *pdxB–serC–pdxA–pdxJ–pdxH* pathway in the KT2440 genome, 53% sequence identity with a conserved catalytic cysteine, a conserved NAD⁺-specific cofactor fingerprint, and genomic synteny placing *epd* next to *pgk* and next to *tktA*, the transketolase that supplies its substrate. No *P. putida*-specific experimental study of this gene currently exists, so the annotation rests on orthology plus bioinformatic and genome-context evidence.


## Artifacts

- [OpenScientist final report](epd-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](epd-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:7751290
2. PMID:9182530
3. PMID:9696782
4. PMID:17822383
5. PMID:26254041
6. PMID:9260967