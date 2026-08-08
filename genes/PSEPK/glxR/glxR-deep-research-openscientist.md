---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-15T17:12:03.393668'
end_time: '2026-07-15T17:43:36.678972'
duration_seconds: 1893.29
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: glxR
  gene_symbol: glxR
  uniprot_accession: Q88F01
  protein_description: 'SubName: Full=Tartronate semialdehyde reductase {ECO:0000313|EMBL:AAN69879.1};
    EC=1.1.1.60 {ECO:0000313|EMBL:AAN69879.1};'
  gene_info: Name=glxR {ECO:0000313|EMBL:AAN69879.1}; OrderedLocusNames=PP_4299 {ECO:0000313|EMBL:AAN69879.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: 6-PGluconate_DH-like_C_sf. (IPR008927); 6PGD_dom2. (IPR013328);
    6PGDH_NADP-bd. (IPR006115); HIBADH-like_NADP-bd. (IPR029154); HIBADH-related.
    (IPR015815)
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
citation_count: 14
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: glxR-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: glxR-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88F01
- **Protein Description:** SubName: Full=Tartronate semialdehyde reductase {ECO:0000313|EMBL:AAN69879.1}; EC=1.1.1.60 {ECO:0000313|EMBL:AAN69879.1};
- **Gene Information:** Name=glxR {ECO:0000313|EMBL:AAN69879.1}; OrderedLocusNames=PP_4299 {ECO:0000313|EMBL:AAN69879.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** 6-PGluconate_DH-like_C_sf. (IPR008927); 6PGD_dom2. (IPR013328); 6PGDH_NADP-bd. (IPR006115); HIBADH-like_NADP-bd. (IPR029154); HIBADH-related. (IPR015815)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "glxR" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'glxR' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **glxR** (gene ID: glxR, UniProt: Q88F01) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of *glxR* (PP_4299, UniProt Q88F01) in *Pseudomonas putida* KT2440

## Summary

**The gene *glxR* (PP_4299; UniProt Q88F01) in *Pseudomonas putida* KT2440 encodes tartronate semialdehyde reductase (TSA reductase; EC 1.1.1.60; also named 2-hydroxy-3-oxopropionate reductase).** This is a soluble, cytoplasmic, homotetrameric NAD(P)H-dependent oxidoreductase belonging to the β-hydroxyacid dehydrogenase superfamily (which also contains 6-phosphogluconate dehydrogenase and 3-hydroxyisobutyrate dehydrogenase). Its primary catalytic function is the reduction of tartronate semialdehyde (2-hydroxy-3-oxopropionate) to D-glycerate, using NADH or NADPH as the electron donor. The enzyme is the committed reductive step of the **glycerate pathway of glyoxylate assimilation**.

The UniProt-provided annotation ("Tartronate semialdehyde reductase, EC 1.1.1.60") is strongly corroborated by multiple independent lines of evidence: (1) genomic context — *glxR* sits within the experimentally-defined *gcl* operon (PP_4297–PP_4301: *gcl*–*hyi*–*glxR*–glycerate kinase–pyruvate kinase); (2) direct in vitro biochemistry on the very close ortholog from *P. aeruginosa* (PA1500, 89.6% identical); (3) matching InterPro domain architecture (6-PGDH NADP-binding and HIBADH-like NAD-binding domains); and (4) conservation of the family catalytic lysine at position 171. Functionally, this enzyme allows *P. putida* to convert glyoxylate — a metabolite arising from allantoin/purine, glycolate, ethylene glycol, and glucarate catabolism — into 2-phosphoglycerate, feeding central carbon metabolism.

A **critical disambiguation** must be noted: the gene symbol "*glxR*" is also used in *Corynebacterium glutamicum* for a completely unrelated protein — a global cAMP receptor protein (a Crp/CRP-family transcription factor). The *P. putida* GlxR (Q88F01) is an NAD(P)-dependent metabolic **enzyme**, not a DNA-binding regulator. This report concerns exclusively the metabolic enzyme. The evidence base is robust and internally consistent; the primary limitation is that the direct enzymological characterization was performed on the *P. aeruginosa* ortholog rather than the KT2440 protein itself, but the ~90% sequence identity and conserved active-site residues make function transfer secure.

---

## Key Findings

### Finding 1 — *glxR* (PP_4299) is tartronate semialdehyde reductase in the *P. putida* KT2440 *gcl* (glyoxylate-assimilation) operon

The genomic organization of *glxR* provides the first and most decisive piece of functional evidence. In *P. putida* KT2440, PP_4299 (*glxR*) is co-transcribed with *gcl* (glyoxylate carboligase), *hyi* (hydroxypyruvate isomerase), *ttuD* (glycerate kinase), and *pykF* (pyruvate kinase), forming the *gcl* operon. Franden et al. (2018) demonstrated that "all of the four genes in genomic proximity to *gcl* (*hyi*, *glxR*, *ttuD*, and *pykF*) are transcribed as an operon," and that "the expression of only two genes (*gcl* and *glxR*) resulted in growth in ethylene glycol" [PMID: 29885475](https://pubmed.ncbi.nlm.nih.gov/29885475/). Because ethylene glycol catabolism proceeds through glyoxylate, this experiment places *glxR* squarely in the glyoxylate-assimilation route and shows it is functionally required for growth on a glyoxylate-generating substrate.

This pathway is under transcriptional control. Li et al. (2019) established "a central role of the transcriptional regulator GclR, which represses the glyoxylate carboligase pathway as part of a larger metabolic context of purine and allantoin metabolism" [PMID: 31166064](https://pubmed.ncbi.nlm.nih.gov/31166064/). This ties the operon containing *glxR* to the broader biological role of processing glyoxylate derived from nitrogen/purine catabolism.

### Finding 2 — GlxR catalyzes NAD(P)H-dependent reduction of tartronate semialdehyde to D-glycerate (EC 1.1.1.60)

The precise reaction catalyzed is well established for this enzyme family. Njau et al. (2000) purified a recombinant member of this family and showed that "the purified recombinant protein very specifically catalyzed the NAD(+)-dependent oxidation of D-glycerate and the NADH-dependent reduction of tartronate semialdehyde, identifying this protein as a tartronate semialdehyde reductase" [PMID: 10978349](https://pubmed.ncbi.nlm.nih.gov/10978349/). The physiological direction of the reaction is reductive:

```
tartronate semialdehyde (2-hydroxy-3-oxopropionate) + NAD(P)H + H+
        │
        ▼   GlxR (EC 1.1.1.60)
D-glycerate + NAD(P)+
```

The gene naming convention is also confirmed: Cusa et al. (1999) described the glycerate pathway genes as "encoding tartronic semialdehyde reductase (*glxR*) and glycerate kinase (*glxK*)" [PMID: 10601204](https://pubmed.ncbi.nlm.nih.gov/10601204/), directly linking the symbol *glxR* to this enzymatic activity. The reaction represents the final step of D-glycerate biosynthesis in the glycerate pathway (Osipiuk et al. 2009).

### Finding 3 — GlxR belongs to the β-hydroxyacid dehydrogenase / 6-PGDH-like family with a conserved catalytic lysine and NAD(P)-binding Rossmann fold

The structural and mechanistic class of the enzyme is well defined. Osipiuk et al. (2009), reporting the 1.65 Å crystal structure of the GarR tartronate semialdehyde reductase from *Salmonella typhimurium*, noted that "these enzymes belong to family of structurally and mechanically related beta-hydroxyacid dehydrogenases which differ in substrate specificity" [PMID: 19184529](https://pubmed.ncbi.nlm.nih.gov/19184529/). This family includes 6-phosphogluconate dehydrogenase and 3-hydroxyisobutyrate dehydrogenase, and the structure revealed a putative NADPH-binding site and a product-mimic (L-tartrate) in the active site.

The catalytic mechanism relies on a conserved active-site lysine. In the homologous plant enzyme AtGLYR1, Hoover et al. (2013) demonstrated through "kinetic studies and binding assays [that] Lys170 is essential for catalysis," functioning as a general acid in an acid/base mechanism [PMID: 24076009](https://pubmed.ncbi.nlm.nih.gov/24076009/). This family assignment matches precisely the InterPro domains annotated for Q88F01: 6PGDH_NADP-bd (IPR006115), HIBADH-like_NADP-bd (IPR029154), and 6-PGluconate_DH-like_C (IPR008927).

### Finding 4 — GlxR shows strong D-glycerate substrate/enantio-specificity, dual NAD/NADP usage, and A-side hydride stereospecificity in *Pseudomonas*

The enzyme exhibits well-defined substrate and cofactor specificity. Liu et al. (2011), characterizing a functional TSA reductase (Tsr1), found that it "showed dual specificity to cofactors NAD(+) and NADP(+) and strong substrate specificity and enantioselectivity for D-glycerate" [PMID: 21305026](https://pubmed.ncbi.nlm.nih.gov/21305026/). This dual cofactor promiscuity and D-glycerate enantioselectivity are hallmark features of the enzyme.

Importantly, *Pseudomonas putida*-specific stereochemical evidence exists. do Nascimento & Davies (1975) showed that in *P. putida*, tartronate semialdehyde reductase (along with hydroxypyruvate reductase and meso-tartrate dehydrogenase) is A-side (pro-R) stereospecific for NAD hydride transfer: "such as hydroxypyruvate reductase and tartronate semialdehyde reductase, were also shown to be A-specific" [PMID: 1200995](https://pubmed.ncbi.nlm.nih.gov/1200995/). This stereospecificity is consistent with an evolutionary origin from malate dehydrogenase.

### Finding 5 — GlxR is a soluble ~31 kDa cytoplasmic NAD(P)-binding enzyme with a dedicated TSA-reductase InterPro signature

Structurally, UniProt Q88F01 is a 297-amino-acid (30.9 kDa) protein composed of two domains: an N-terminal 6-phosphogluconate dehydrogenase NADP-binding domain (Pfam PF03446, residues 3–162) and a C-terminal HIBADH-like NAD-binding domain (Pfam PF14833, residues 165–283), with an annotated active site at residue 171. The protein carries the specific InterPro family signature IPR006398 ("Tartronate semialdehyde reductase") and is annotated with GO terms GO:0008679 (2-hydroxy-3-oxopropionate reductase activity), GO:0051287/GO:0050661 (NAD/NADP binding), and GO:0046487 (glyoxylate metabolic process).

Crucially for localization, **no signal peptide or transmembrane segment is annotated**, indicating a soluble, cytoplasmic protein. This is consistent with its role as a metabolic enzyme in the cytosolic glycerate pathway. Database cross-references include KEGG ppu:PP_4299 and BioCyc PPUT160488:G1G01-4576-MONOMER.

### Finding 6 — GlxR is a tetrameric enzyme kinetically specific for Gcl-derived tartronate semialdehyde over its hydroxypyruvate tautomer (direct *Pseudomonas* evidence)

The most direct and recent biochemical evidence comes from the very close ortholog in *P. aeruginosa*. Parkhill et al. (2025) characterized an allantoin-inducible glyoxylate cluster (PA1498–PA1502) that converts glyoxylate to pyruvate. They showed that "the purified proteins encoded by PA1502 and PA1500 have glyoxylate carboligase (Gcl) and tartronate semialdehyde (TSA) reductase (GlxR) activity, respectively, in vitro. Gcl condenses two molecules of glyoxylate to yield TSA, which is then reduced by GlxR to yield D-glycerate" [PMID: 41369682](https://pubmed.ncbi.nlm.nih.gov/41369682/).

The enzyme displays refined substrate discrimination: "GlxR displayed much greater specificity (kcat/KM) for Gcl-derived TSA than it did for the TSA tautomer, hydroxypyruvate." This shows that GlxR is optimized for the authentic substrate produced by the upstream carboligase, and the adjacent hydroxypyruvate isomerase (Hyi) likely limits unwanted tautomerization. X-ray crystallography further revealed that "apo-GlxR is a configurationally flexible enzyme that can adopt two distinct tetrameric assemblies in vitro," establishing the **homotetrameric quaternary structure** of GlxR.

### Finding 7 — Disambiguation: *P. putida* glxR (Q88F01) is an enzyme, NOT the *Corynebacterium* 'GlxR' cAMP-receptor transcriptional regulator

The symbol "GlxR" is used for a completely unrelated protein in *Corynebacterium glutamicum*, where it is a global cAMP receptor protein — a homolog of enterobacterial Crp. Schulte et al. (2017) described that "cAMP acts as effector of the global transcriptional regulator GlxR, a homolog of enterobacterial Crp. The cAMP-GlxR complex activates or represses the expression of about 200 target genes" [PMID: 28698098](https://pubmed.ncbi.nlm.nih.gov/28698098/). This *Corynebacterium* GlxR is a DNA-binding transcription factor with no enzymatic activity.

By contrast, *P. putida* KT2440 *glxR*/PP_4299 (Q88F01) is an NAD(P)-dependent metabolic enzyme with InterPro IPR006398 and 6-PGDH/HIBADH-like domains — it has no DNA-binding or cAMP-binding features. These are two distinct proteins that happen to share a gene symbol, and they must not be conflated.

### Finding 8 — KEGG confirms PP_4299/glxR = K00042 embedded in the complete KT2440 glycerate-pathway gene cluster

KEGG annotation independently confirms the pathway context. The contiguous *P. putida* KT2440 cluster is annotated as:

| Locus | Gene | KEGG Ortholog | Enzyme | EC |
|-------|------|---------------|--------|-----|
| PP_4297 | *gcl* | K01608 | glyoxylate carboligase (tartronate-semialdehyde synthase) | 4.1.1.47 |
| PP_4298 | *hyi* | K01816 | hydroxypyruvate isomerase | 5.3.1.22 |
| **PP_4299** | ***glxR*** | **K00042** | **tartronate semialdehyde reductase (2-hydroxy-3-oxopropionate reductase)** | **1.1.1.60** |
| PP_4300 | *ttuD* | K11529 | glycerate 2-kinase | 2.7.1.165 |
| PP_4301 | *pykF* | K00873 | pyruvate kinase | 2.7.1.40 |

This matches the experimentally defined *gcl* operon (*gcl*-*hyi*-*glxR*-*ttuD*-*pykF*) from Franden et al. (2018) [PMID: 29885475](https://pubmed.ncbi.nlm.nih.gov/29885475/).

### Finding 9 — *P. putida* GlxR (PP_4299) is 89.6% identical to the experimentally characterized *P. aeruginosa* GlxR (PA1500)

A global Needleman-Wunsch alignment of UniProt Q88F01 (*P. putida* KT2440 GlxR/PP_4299, 297 aa) against Q9I3L2 (*P. aeruginosa* PAO1 GlxR/PA1500, 296 aa) yields 266 identical positions over a 297-column alignment with a single gap = **89.6% amino-acid identity** (89.9% over the shorter sequence). Because Q9I3L2/PA1500 is the enzyme directly demonstrated in vitro to be a tartronate semialdehyde reductase forming D-glycerate and to crystallize as flexible tetramers [PMID: 41369682](https://pubmed.ncbi.nlm.nih.gov/41369682/), this near-identity provides strong justification for transferring the experimentally-verified function to PP_4299. At ~90% identity, essentially all functional residues, fold, oligomeric state, and catalytic properties can be confidently assumed to be shared.

### Finding 10 — The family catalytic lysine is directly conserved at position 171 in *P. putida* GlxR (Q88F01)

Direct inspection of the UniProt Q88F01 sequence confirms that the residue at the annotated active-site position 171 is a lysine (K), within the sequence context `GDGQTAKVANQIIVAL`. This corresponds to the essential catalytic lysine of the β-hydroxyacid dehydrogenase family — the same residue shown to be essential for catalysis (Lys170) in AtGLYR1 by Hoover et al. (2013): "kinetic studies and binding assays established that Lys170 is essential for catalysis" [PMID: 24076009](https://pubmed.ncbi.nlm.nih.gov/24076009/). The conservation of this catalytic residue at the expected position in the *P. putida* enzyme completes the mechanistic argument that Q88F01 is a catalytically active tartronate semialdehyde reductase.

---

## Mechanistic Model / Interpretation

### The glycerate pathway of glyoxylate assimilation

GlxR performs the committed reductive step of the **glycerate pathway** — a route that allows *P. putida* to salvage the carbon in glyoxylate (a two-carbon compound) and convert it into central metabolic intermediates. The complete pathway operates as follows:

```
   2 × glyoxylate (2C)
        │
        │  Gcl (glyoxylate carboligase, PP_4297, EC 4.1.1.47)
        │  condenses two glyoxylate + releases CO2
        ▼
   tartronate semialdehyde (TSA, 3C, 2-hydroxy-3-oxopropionate)
        │                              ⇄  hydroxypyruvate (tautomer)
        │                                 [Hyi isomerase, PP_4298, limits
        │                                  unwanted tautomerization]
        │  ►►► GlxR (PP_4299, EC 1.1.1.60) ◄◄◄
        │      NAD(P)H-dependent reduction; high specificity
        │      for authentic TSA over hydroxypyruvate
        ▼
   D-glycerate (3C)
        │
        │  glycerate 2-kinase (TtuD, PP_4300, EC 2.7.1.165)
        │  + ATP
        ▼
   2-phosphoglycerate
        │
        │  → enolase → pyruvate kinase (PykF, PP_4301)
        ▼
   central carbon metabolism (pyruvate / gluconeogenesis)
```

The key mechanistic insights are:

1. **Position in pathway**: GlxR acts immediately downstream of glyoxylate carboligase (Gcl). Gcl condenses two glyoxylate molecules (with loss of CO₂) to make tartronate semialdehyde, and GlxR then reduces this to D-glycerate. The tight substrate specificity of GlxR for Gcl-derived TSA (rather than its hydroxypyruvate tautomer) indicates the enzymes are kinetically coupled, and the adjacent Hyi isomerase helps channel the correct tautomer.

2. **Catalytic mechanism**: GlxR uses a Rossmann-fold NAD(P)-binding architecture. Hydride is transferred from the A-face (pro-R) of the nicotinamide cofactor to the aldehyde/keto carbon of TSA, while the conserved active-site Lys171 acts as a general acid/base to protonate the developing alkoxide, yielding the D-glycerate hydroxyl. The A-side stereospecificity and catalytic lysine are both experimentally supported and conserved in the *P. putida* sequence.

3. **Cofactor flexibility**: The enzyme can use either NADH or NADPH, giving metabolic flexibility depending on the redox state of the cell.

4. **Quaternary structure**: GlxR is a homotetramer that can adopt distinct configurational states, consistent with the flexible tetrameric assemblies seen crystallographically for the *P. aeruginosa* ortholog.

### Physiological role and metabolic entry points

The glyoxylate that feeds this pathway can arise from several catabolic routes, all of which converge on the *gcl* operon:

| Upstream substrate | Route to glyoxylate | Relevance |
|--------------------|---------------------|-----------|
| Allantoin / purines | Purine degradation → glyoxylate | Regulated by GclR; primary "native" role |
| Ethylene glycol | EG → glycolaldehyde → glycolate → glyoxylate | Biotechnology (PET upcycling) |
| Glycolate | Glycolate oxidation → glyoxylate | Photorespiration-like carbon salvage |
| Glucarate/galactarate | Sugar acid catabolism → TSA directly | Hexaric acid utilization |

This explains why *glxR* is of considerable biotechnological interest: the ethylene glycol (a PET monomer) utilization capability of *P. putida* KT2440 depends directly on this glyoxylate assimilation pathway, and *gcl* + *glxR* expression alone can confer growth on ethylene glycol.

### Localization

All evidence points to a **cytoplasmic** localization. The protein has no signal peptide or transmembrane region, is soluble, and its substrates (TSA, D-glycerate) and cofactors (NAD/NADP) are cytosolic metabolites. The enzyme carries out its function in the cytosol as part of the soluble glycerate-pathway enzyme complement.

---

## Evidence Base

| PMID | Study | How it supports the findings |
|------|-------|------------------------------|
| [29885475](https://pubmed.ncbi.nlm.nih.gov/29885475/) | *Engineering P. putida KT2440 for efficient ethylene glycol utilization* (Franden et al. 2018) | Directly establishes the *gcl* operon (*gcl*-*hyi*-*glxR*-*ttuD*-*pykF*) and shows *gcl*+*glxR* suffice for glyoxylate-derived growth. Primary genetic evidence for pathway membership. |
| [41369682](https://pubmed.ncbi.nlm.nih.gov/41369682/) | *An allantoin-inducible glyoxylate utilization pathway in Pseudomonas* (Parkhill et al. 2025) | Direct in vitro biochemistry on the ~90%-identical *P. aeruginosa* ortholog: confirms GlxR = TSA reductase forming D-glycerate, substrate specificity over hydroxypyruvate, and tetrameric structure. Strongest primary enzymological evidence. |
| [10978349](https://pubmed.ncbi.nlm.nih.gov/10978349/) | *Novel β-hydroxyacid dehydrogenases in E. coli and H. influenzae* (Njau et al. 2000) | Direct biochemical demonstration of the NAD(P)-dependent TSA reductase reaction for the enzyme family. |
| [10601204](https://pubmed.ncbi.nlm.nih.gov/10601204/) | *Genetic analysis of allantoin/glyoxylate metabolism in E. coli* (Cusa et al. 1999) | Confirms the gene symbol *glxR* corresponds to tartronate semialdehyde reductase in the glycerate pathway. |
| [19184529](https://pubmed.ncbi.nlm.nih.gov/19184529/) | *X-ray structure of GarR TSA reductase from S. typhimurium* (Osipiuk et al. 2009) | Assigns the enzyme to the β-hydroxyacid dehydrogenase structural family; reveals NADPH-binding site and active-site geometry. |
| [24076009](https://pubmed.ncbi.nlm.nih.gov/24076009/) | *Catalytically important residues for glyoxylate reduction in plants* (Hoover et al. 2013) | Identifies the essential catalytic lysine (Lys170 in AtGLYR1), conserved as Lys171 in Q88F01. |
| [21305026](https://pubmed.ncbi.nlm.nih.gov/21305026/) | *TSA reductase in Ustilago maydis* (Liu et al. 2011) | Documents dual NAD/NADP cofactor specificity and D-glycerate enantioselectivity. |
| [1200995](https://pubmed.ncbi.nlm.nih.gov/1200995/) | *Stereospecificity of NAD-dependent oxidoreductases* (do Nascimento & Davies 1975) | *P. putida*-specific evidence for A-side (pro-R) hydride stereospecificity of TSA reductase. |
| [31166064](https://pubmed.ncbi.nlm.nih.gov/31166064/) | *Metabolic and regulatory basis of ethylene glycol metabolism* (Li et al. 2019) | Establishes GclR regulation of the pathway in the context of purine/allantoin metabolism. |
| [28698098](https://pubmed.ncbi.nlm.nih.gov/28698098/) | *Single-cell GlxR-based cAMP biosensor for C. glutamicum* (Schulte et al. 2017) | Documents the unrelated *Corynebacterium* GlxR (cAMP receptor transcription factor) — the basis for symbol disambiguation. |

Supporting/contextual literature includes reports of the same enzyme family in the glucarate/galactarate pathway ([PMID: 9772162](https://pubmed.ncbi.nlm.nih.gov/9772162/)), review of β-hydroxyacid dehydrogenases ([PMID: 11306094](https://pubmed.ncbi.nlm.nih.gov/11306094/)), the glyoxylate-to-glycerate conversion in *Hyphomicrobium* grown on allantoin ([PMID: 6614900](https://pubmed.ncbi.nlm.nih.gov/6614900/)), and photorespiratory-bypass engineering that used bacterial TSA reductase ([PMID: 17435746](https://pubmed.ncbi.nlm.nih.gov/17435746/)).

**Convergence of evidence:** Ten independent lines of evidence — genomic context, KEGG annotation, InterPro/Pfam domains, family crystal structures, direct ortholog biochemistry, cofactor and stereochemical specificity, catalytic-residue conservation, and near-identity to a characterized enzyme — all point to the same conclusion. There are no contradictory findings.

---

## Limitations and Knowledge Gaps

1. **No direct enzymology on the KT2440 protein itself.** The most detailed biochemical characterization (kcat/KM, substrate discrimination, tetramer structure) was performed on the *P. aeruginosa* ortholog PA1500 (Q9I3L2). While 89.6% identity and conserved catalytic residues make function transfer secure, kinetic constants for the actual KT2440 GlxR (Q88F01) have not been directly measured. Absolute kcat, KM for TSA, and cofactor preference (NADH vs NADPH ratio) for the KT2440 enzyme are inferred, not measured.

2. **No experimentally determined 3D structure of Q88F01.** Structural inferences rest on the *S. typhimurium* GarR structure and the *P. aeruginosa* GlxR crystallography. An experimental structure of the *P. putida* enzyme (or a high-quality AlphaFold model verification) would confirm the active-site geometry and the two-tetramer configurational flexibility.

3. **Catalytic Lys171 not directly mutated in *P. putida*.** The catalytic essentiality of the lysine is established in AtGLYR1 (Lys170) and inferred by conservation; site-directed mutagenesis of Lys171 in Q88F01 has not been reported.

4. **Precise physiological flux and redundancy.** *P. putida* may possess additional or redundant reductases/aldehyde-processing enzymes (as recently suggested for the related strain JM37, which has genetic redundancy in glyoxylate assimilation). The quantitative contribution of *glxR* to glyoxylate flux under different growth conditions has not been isolated by clean single-gene knockout studies in KT2440 specifically.

5. **Cofactor preference in vivo.** Although the family is dual-specific (NAD/NADP), which cofactor dominates in vivo under specific growth conditions in KT2440 remains uncharacterized.

---

## Proposed Follow-up Experiments / Actions

1. **Direct enzymatic characterization of Q88F01.** Express and purify recombinant KT2440 GlxR (His-tagged), and measure steady-state kinetics (kcat, KM) for tartronate semialdehyde reduction with both NADH and NADPH. Confirm the specificity ratio for TSA vs hydroxypyruvate observed in the *P. aeruginosa* ortholog.

2. **Site-directed mutagenesis of Lys171.** Generate a K171A (or K171R) variant and measure the loss of catalytic activity to confirm the predicted catalytic role of the conserved lysine, mirroring the AtGLYR1 Lys170 experiments.

3. **Clean *glxR* knockout in KT2440.** Delete PP_4299 and test growth phenotypes on glyoxylate-generating substrates (allantoin, glycolate, ethylene glycol, glucarate). Complement with plasmid-borne *glxR* to confirm the phenotype is due to loss of this gene, and quantify residual growth to assess redundancy.

4. **Structural determination.** Solve the X-ray crystal structure (or cryo-EM) of KT2440 GlxR, ideally with bound cofactor and substrate/product analog (e.g., L-tartrate as used for GarR), to confirm active-site architecture and the tetrameric assembly flexibility.

5. **Metabolic flux analysis.** Use ¹³C-labeled ethylene glycol or allantoin to trace carbon flux through the glycerate pathway and quantify the in vivo contribution of GlxR, and determine the dominant cofactor used under each condition.

6. **Kinetic coupling assay.** Reconstitute Gcl + Hyi + GlxR in vitro to test the proposed substrate channeling / tautomer-limiting model, confirming that Hyi improves overall flux by maintaining the correct TSA tautomer for GlxR.

---

## Conclusion

The gene *glxR* (PP_4299; UniProt Q88F01) in *Pseudomonas putida* KT2440 encodes **tartronate semialdehyde reductase (EC 1.1.1.60)**, a soluble, cytoplasmic, homotetrameric NAD(P)H-dependent oxidoreductase of the β-hydroxyacid dehydrogenase superfamily. It catalyzes the reduction of tartronate semialdehyde to D-glycerate — the committed reductive step of the glycerate pathway of glyoxylate assimilation — acting downstream of glyoxylate carboligase within the chromosomal *gcl* operon. Through this pathway, glyoxylate derived from allantoin/purine, glycolate, ethylene-glycol, and glucarate catabolism is funneled into 2-phosphoglycerate and central carbon metabolism. The functional annotation provided by UniProt is fully validated by convergent genomic, biochemical, structural, and comparative-sequence evidence. The enzyme should not be confused with the unrelated *Corynebacterium* "GlxR" cAMP-receptor transcription factor.


## Artifacts

- [OpenScientist final report](glxR-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](glxR-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:29885475
2. PMID:31166064
3. PMID:10978349
4. PMID:10601204
5. PMID:19184529
6. PMID:24076009
7. PMID:21305026
8. PMID:1200995
9. PMID:41369682
10. PMID:28698098
11. PMID:9772162
12. PMID:11306094
13. PMID:6614900
14. PMID:17435746