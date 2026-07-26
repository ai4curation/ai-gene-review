---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-20T18:53:19.768714'
end_time: '2026-07-20T19:23:42.992786'
duration_seconds: 1823.22
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: fau
  gene_symbol: fau
  uniprot_accession: Q88CH8
  protein_description: 'RecName: Full=5-formyltetrahydrofolate cyclo-ligase {ECO:0000256|RuleBase:RU361279};
    EC=6.3.3.2 {ECO:0000256|RuleBase:RU361279};'
  gene_info: Name=fau {ECO:0000313|EMBL:AAN70768.1}; OrderedLocusNames=PP_5203 {ECO:0000313|EMBL:AAN70768.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the 5-formyltetrahydrofolate cyclo-ligase
  protein_domains: FTHF_cligase. (IPR002698); FTHF_cligase-like_sf. (IPR024185); NagB/RpiA_transferase-like.
    (IPR037171); 5-FTHF_cyc-lig (PF01812)
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
citation_count: 15
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: fau-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: fau-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88CH8
- **Protein Description:** RecName: Full=5-formyltetrahydrofolate cyclo-ligase {ECO:0000256|RuleBase:RU361279}; EC=6.3.3.2 {ECO:0000256|RuleBase:RU361279};
- **Gene Information:** Name=fau {ECO:0000313|EMBL:AAN70768.1}; OrderedLocusNames=PP_5203 {ECO:0000313|EMBL:AAN70768.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the 5-formyltetrahydrofolate cyclo-ligase
- **Key Domains:** FTHF_cligase. (IPR002698); FTHF_cligase-like_sf. (IPR024185); NagB/RpiA_transferase-like. (IPR037171); 5-FTHF_cyc-lig (PF01812)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "fau" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'fau' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **fau** (gene ID: fau, UniProt: Q88CH8) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *fau* (PP_5203, UniProt Q88CH8) — 5-Formyltetrahydrofolate Cyclo-Ligase from *Pseudomonas putida* KT2440

## Summary

The *Pseudomonas putida* KT2440 gene **fau** (ordered locus **PP_5203**; UniProt **Q88CH8**) encodes **5-formyltetrahydrofolate cyclo-ligase**, an enzyme far better known in the biochemical literature as **5,10-methenyltetrahydrofolate synthetase (MTHFS)**, EC **6.3.3.2**. This is a small (~202-residue), soluble, cytoplasmic enzyme of the folate-mediated one-carbon metabolic network. Its identity is unambiguous: the UniProt annotation, the Pfam domain assignment (PF01812, "5-FTHF_cyc-lig"), the InterPro signatures (IPR002698, IPR024185, IPR037171), and independent sequence analysis performed during this investigation all converge on the same assignment. Importantly, this is **not** a case of gene-symbol ambiguity — although the three-letter symbol "fau" collides with the unrelated eukaryotic *FAU* ribosomal/ubiquitin fusion gene, the *P. putida* gene product's sequence, length, domain architecture, and conserved active-site residues place it firmly in the well-characterized cyclo-ligase/MTHFS family.

The enzyme catalyzes a single, highly specific, and physiologically important reaction: the **only known ATP-dependent, irreversible conversion of 5-formyltetrahydrofolate (5-formyl-THF; folinic acid / leucovorin, including its polyglutamate forms) to 5,10-methenyltetrahydrofolate**. The reaction requires Mg²⁺ and proceeds through a phosphorylated **N5-iminium phosphate intermediate**, a mechanism established by isotope-exchange, ³¹P-NMR, and X-ray crystallography of orthologous enzymes. Because the spontaneous (non-enzymatic) equilibrium strongly favors 5-formyl-THF, the cell must expend ATP to drive the ring closure — making MTHFS the sole biochemical "gate" that empties the 5-formyl-THF pool back into the metabolically active one-carbon folate cycle.

Physiologically, MTHFS is the master regulator of 5-formyl-THF levels. 5-Formyl-THF is simultaneously an intracellular storage form of folate and a potent inhibitor of key folate enzymes (serine hydroxymethyltransferase, SHMT, and AICAR formyltransferase). By clearing this pool, MTHFS relieves that inhibition and returns one-carbon units to the biosynthesis of purines, thymidylate, and methionine. In bacteria this activity has clinically relevant downstream consequences: loss of MTHFS/*ygfA* causes accumulation of polyglutamylated folinic acid, hypersusceptibility to antifolate drugs, and altered antibiotic persistence/tolerance. The functional assignment for the *P. putida* enzyme rests on strong homology (44% identity to *E. coli* ygfA), intact family motifs, and conservation of all three catalytically essential residues (E60, R140, Y148); no direct biochemical characterization of the *P. putida* protein itself has yet been reported, so the annotation is a robust homology-based inference (UniProt evidence level PE=3).

---

## Key Findings

### Finding 1 — *fau*/PP_5203 encodes a 5-formyltetrahydrofolate cyclo-ligase (MTHFS, EC 6.3.3.2)

UniProt Q88CH8 annotates the *P. putida* KT2440 *fau*/PP_5203 gene product as **5-formyltetrahydrofolate cyclo-ligase (EC 6.3.3.2)**, assigning it to the 5-formyltetrahydrofolate cyclo-ligase family with Pfam **PF01812** ("5-FTHF_cyc-lig") and InterPro signatures IPR002698 and IPR024185. The enzyme's second common name, **5,10-methenyltetrahydrofolate synthetase (MTHFS)**, reflects the product it forms.

This enzyme catalyzes what the literature repeatedly emphasizes is a *unique* reaction. As stated in the foundational review of bacterial folinic-acid conversion, MTHFS activity is "responsible for the only ATP-dependent, irreversible conversion of folinic acid to 5,10-methenyltetrahydrofolate" ([PMID: 21372133](https://pubmed.ncbi.nlm.nih.gov/21372133/)). No other enzyme in the cell performs this conversion, which makes MTHFS the singular exit route from the 5-formyl-THF pool.

The assignment is strengthened by the enzyme's deep evolutionary conservation. Structural and functional characterization of the *Mycoplasma pneumoniae* ortholog notes that MTHFS "belongs to a large cycloligase protein family with 97 sequence homologues from bacteria to human" ([PMID: 16104022](https://pubmed.ncbi.nlm.nih.gov/16104022/)). This broad conservation across the tree of life is precisely what licenses confident transfer of the biochemical function — established in human, *M. pneumoniae*, and *Bacillus anthracis* orthologs — to the *P. putida* enzyme.

### Finding 2 — Catalytic mechanism: ATP-coupled phosphorylation via an N5-iminium phosphate intermediate, Mg²⁺-dependent

The chemistry of MTHFS is mechanistically distinctive. Because the non-enzymatic equilibrium strongly favors 5-formyl-THF over 5,10-methenyl-THF, the enzyme must **couple ring closure to ATP hydrolysis** to drive the reaction forward. The mechanism runs through a phosphorylated intermediate: the substrate's formyl oxygen is activated by phosphoryl transfer from ATP, generating a reactive **N5-iminium phosphate** species that then cyclizes.

Two independent lines of experimental evidence establish this. First, isotopic and NMR studies of the coupling reaction showed that "the formyl oxygen of the substrate was transferred to the product phosphate during the reaction. This further supports the existence of a phosphorylated intermediate" ([PMID: 7673211](https://pubmed.ncbi.nlm.nih.gov/7673211/)). Second, crystallography of the human ortholog directly captured the enzyme "bound with the N5-iminium phosphate reaction intermediate" ([PMID: 19738041](https://pubmed.ncbi.nlm.nih.gov/19738041/)), providing atomic-resolution confirmation of the proposed catalytic species.

The reaction is Mg²⁺-dependent: characterization of the *M. pneumoniae* enzyme established that "the role of Mg²⁺ in the reaction is to form the ATP–Mg²⁺-enzyme complex" ([PMID: 16104022](https://pubmed.ncbi.nlm.nih.gov/16104022/)), with reported Km values near 165 µM for 5-formyl-THF and ~166 µM for MgATP. Structural work on the *B. anthracis* ortholog (BA4489), solved in complex with Mg-bound ADP and phosphate at 1.6 Å, provided "a detailed picture of the proposed catalytic mechanism of the enzyme" ([PMID: 17329806](https://pubmed.ncbi.nlm.nih.gov/17329806/)). Substrate specificity is strict: only one of the two formyl rotamers is a competent substrate, and kcat is on the order of ~5 s⁻¹.

### Finding 3 — Physiological role: clearing the 5-formyl-THF storage/inhibitor pool to regenerate active one-carbon folates

5-Formyl-THF occupies an unusual dual position in folate biology. It is simultaneously "an intracellular storage form of folate and … an inhibitor of the folate-dependent enzymes phosphoribosylaminoimidazolecarboxamide formyltransferase (AICARFT) and serine hydroxymethyltransferase (SHMT)" ([PMID: 30867454](https://pubmed.ncbi.nlm.nih.gov/30867454/)). Its intracellular level is set by a **futile cycle**: SHMT generates 5-formyl-THF, while MTHFS consumes it in the ATP-driven cyclo-ligase reaction.

A hybrid-stochastic computational model of folate-mediated one-carbon metabolism demonstrated that "MTHFS plays an essential role in preventing 5fTHF accumulation, which consequently averts inhibition of all other reactions in the metabolic network" ([PMID: 30867454](https://pubmed.ncbi.nlm.nih.gov/30867454/)). In other words, without MTHFS the inhibitory 5-formyl-THF pool would build up and throttle the entire one-carbon network. The same modeling work found that the SHMT/MTHFS futile cycle additionally dampens stochastic noise in the pathway.

The consequences of losing this activity have been demonstrated experimentally in bacteria: "Absence of MTHFS resulted in marked cellular accumulation of polyglutamylated species of folinic acid" ([PMID: 21372133](https://pubmed.ncbi.nlm.nih.gov/21372133/)). This confirms that MTHFS is the physiological clearance route for the 5-formyl-THF (folinic acid) pool, including its polyglutamate forms, and that its loss disrupts folate homeostasis and the utilization of exogenous reduced folates.

### Finding 4 — Downstream phenotypes: antifolate resistance, antibiotic persistence, and cytoplasmic localization

Because MTHFS controls the flux of folinic acid back into the active folate pool, its activity has direct pharmacological consequences in bacteria. Loss of the enzyme sensitizes cells to antifolate drugs: "*Escherichia coli* mutants lacking MTHFS became susceptible to antifolates. These results indicate that folinic acid conversion by MTHFS" is required for the resistance phenotype ([PMID: 21372133](https://pubmed.ncbi.nlm.nih.gov/21372133/)). The same study reported hypersusceptibility in *Mycobacterium smegmatis* MTHFS mutants, indicating a conserved bacterial phenomenon.

The *E. coli* ortholog, **ygfA** ("5-formyl-tetrahydrofolate cyclo-ligase"), was independently identified in a genome-wide screen of global regulators and nucleotide metabolism as a gene contributing to **antibiotic tolerance/persistence** ([PMID: 18519731](https://pubmed.ncbi.nlm.nih.gov/18519731/)). In the pathogen *Francisella tularensis*, the cyclo-ligase gene FTL_0724 is required for full virulence and modulates macrophage inflammasome activation, further linking the enzyme's metabolic role to host–pathogen outcomes ([PMID: 23115038](https://pubmed.ncbi.nlm.nih.gov/23115038/)).

Structurally, the enzyme adopts a **NagB/RpiA-transferase-like (Rossmann-like) fold** (InterPro IPR037171), a fold shared with sugar isomerases, eIF2B, DeoR transcription factors, and acyl-CoA transferases; a fold-diversification analysis explicitly groups "acetyl-CoA transferases and methenyltetrahydrofolate synthetase" within this assemblage ([PMID: 16376935](https://pubmed.ncbi.nlm.nih.gov/16376935/)). All characterized orthologs are soluble, monomeric or homodimeric, cytoplasmic proteins — consistent with the *P. putida* enzyme carrying out its function in the **cytoplasm**.

### Finding 5 — Sequence-level confirmation: Q88CH8 is a bona fide MTHFS ortholog with intact motifs and no membrane anchor

Independent sequence analysis of the 202-residue Q88CH8 protein (performed during this investigation) confirms the database annotation. Global Needleman–Wunsch alignment (BLOSUM62) gives **44.1% identity to *E. coli* ygfA** (P0AC28) and 28.6% identity to human MTHFS (P49914). Both values are well above the "twilight zone" of homology for ~200-residue proteins, so functional transfer from the characterized orthologs is robust. The protein's length (202 aa) matches the family (human 203 aa; *E. coli* 182 aa).

The conserved family motifs are intact, including the glycine-rich folate/nucleotide-binding loop **G-M-G-G-G-F-Y-D** (around position 142) and the conserved **LPNDGE** (position 55) and **DLILLPL** (position 125) regions, consistent with Pfam PF01812. Hydropathy analysis (Kyte–Doolittle) gives a maximum 19-residue window value of +1.41, below the ~+1.6 threshold for a transmembrane segment; the GRAVY score is −0.545, and the protein contains 37 Arg+Lys residues. Together these indicate a **hydrophilic, soluble protein with no transmembrane segment and no signal peptide** — consistent with cytoplasmic localization. UniProt lists evidence level PE=3 (inferred from homology).

### Finding 6 — All three catalytically essential residues are conserved in *P. putida* fau

Alignment of Q88CH8 to the *M. pneumoniae* MTHFS (P75430; 37.9% identity) — the ortholog used in the definitive site-directed mutagenesis studies — maps the experimentally validated catalytic residues onto the *P. putida* sequence:

| *M. pneumoniae* residue | Role | *P. putida fau* equivalent | Mutagenesis phenotype |
|---|---|---|---|
| E55 | 5-formyl-THF binding / ionic interaction | **E60** | E55A and E55Q both abolish activity |
| R115 | Catalysis | **R140** | R115A shows no activity |
| Y123 | Substrate binding/turnover | **Y148** (= human Y152) | Y123A abolishes activity |

In *M. pneumoniae*, replacement of any of these residues with alanine (and the conservative E55Q substitution) eliminates detectable enzyme activity ([PMID: 18473156](https://pubmed.ncbi.nlm.nih.gov/18473156/); [PMID: 31401777](https://pubmed.ncbi.nlm.nih.gov/31401777/)). All three indispensable residues are conserved in the *P. putida* enzyme. The ATP-loop residues F118/K120 fall within the glycine-rich GMGGGFYD nucleotide-binding loop (*P. putida* residues ~142–149); although exact column registration within the loop is ambiguous, the Gly-rich loop itself is intact. This residue-level conservation provides the strongest possible evidence, short of a direct assay, that the *P. putida* enzyme possesses a fully functional active site.

---

## Mechanistic Model / Interpretation

### The reaction

```
        5-formyl-THF (folinic acid)          5,10-methenyl-THF
    (storage form; enzyme inhibitor)      (active one-carbon folate)
                 |                                    ^
                 |    fau / PP_5203 (MTHFS, EC 6.3.3.2) |
                 |    + ATP·Mg2+  ---->  ADP + Pi       |
                 |                                      |
                 +----[ N5-iminium phosphate ]----------+
                       (phosphorylated intermediate)
```

MTHFS catalyzes an **intramolecular cyclization**: the C5 formyl group of 5-formyl-THF condenses with the N10 nitrogen to close the imidazoline ring of 5,10-methenyl-THF. Because this ring closure is thermodynamically uphill under cellular conditions, the enzyme phosphorylates the formyl oxygen using ATP, forming the reactive N5-iminium phosphate. Collapse of this intermediate, with loss of inorganic phosphate, yields the methenyl product. The Mg²⁺ ion is required to present ATP in the catalytically competent ATP·Mg²⁺ complex.

### Position in the one-carbon network

```
   Serine  --SHMT-->  Glycine + 5,10-CH2-THF
                                   |
                    (side reaction / hydrolysis)
                                   v
                            5-formyl-THF   <----- exogenous folinic acid / leucovorin
                                   |
                    fau/MTHFS + ATP (the ONLY exit)
                                   v
                          5,10-methenyl-THF
                            /      |       \
                  10-formyl-THF  5,10-CH2-THF  ...
                       |            |
             purine synthesis   thymidylate / methionine
             (AICARFT, GARFT)   (TS, methionine cycle)
```

The central logic is that **5-formyl-THF is a metabolic dead-end and an inhibitor unless MTHFS rescues it**. SHMT and other reactions can generate 5-formyl-THF; the compound then sequesters folate and inhibits SHMT and AICAR formyltransferase. MTHFS is the sole ATP-driven valve that returns this carbon and folate to the productive pool of interconvertible one-carbon folates (5,10-methenyl-, 10-formyl-, and 5,10-methylene-THF), which feed purine biosynthesis, thymidylate synthesis, and the methionine/methylation cycle. The SHMT↔MTHFS futile cycle both sets the steady-state 5-formyl-THF concentration and buffers stochastic fluctuations in pathway flux.

### Why this matters in *P. putida*

*P. putida* KT2440 is a metabolically versatile soil bacterium with an extensive biosynthetic capacity that depends heavily on one-carbon folate chemistry (nucleotide and amino-acid biosynthesis). The *fau* gene product ensures that the reduced-folate pool remains available and uninhibited. While direct phenotypic studies in *P. putida* have not been reported, the conserved bacterial consequences — folinic-acid accumulation on loss of function, antifolate hypersusceptibility, and modulation of antibiotic persistence/tolerance — are expected to apply, given the strong orthology and intact active site.

---

## Evidence Base

| PMID | Title (abbreviated) | Contribution to this report |
|---|---|---|
| [21372133](https://pubmed.ncbi.nlm.nih.gov/21372133/) | *Bacterial conversion of folinic acid is required for antifolate resistance* | Defines EC number, synonyms, the unique irreversible ATP-dependent reaction; shows loss of MTHFS causes polyglutamyl folinic-acid accumulation and antifolate susceptibility in *E. coli*/*M. smegmatis* |
| [16104022](https://pubmed.ncbi.nlm.nih.gov/16104022/) | *Structural and functional characterization of MTHFS from M. pneumoniae* | Establishes ~97-member conserved family; Mg²⁺ role in forming the ATP–Mg²⁺-enzyme complex; kinetic parameters |
| [7673211](https://pubmed.ncbi.nlm.nih.gov/7673211/) | *Mechanism for the coupling of ATP hydrolysis…* | Isotope/NMR evidence for phosphorylated intermediate; formyl oxygen transferred to product phosphate |
| [19738041](https://pubmed.ncbi.nlm.nih.gov/19738041/) | *Structural basis for inhibition of human MTHFS…* | Crystallographic capture of the N5-iminium phosphate reaction intermediate |
| [17329806](https://pubmed.ncbi.nlm.nih.gov/17329806/) | *Structure of 5-FTHF cyclo-ligase from B. anthracis (BA4489)* | 1.6 Å structure with Mg-ADP + phosphate; detailed catalytic mechanism picture |
| [30867454](https://pubmed.ncbi.nlm.nih.gov/30867454/) | *5-formyl-THF futile cycle reduces pathway stochasticity* | Defines 5fTHF as storage form + inhibitor of AICARFT/SHMT; MTHFS essential to prevent 5fTHF accumulation |
| [18473156](https://pubmed.ncbi.nlm.nih.gov/18473156/) | *Roles of Arg115 and Lys120 in the MTHFS active site* | R115A abolishes activity; K120A raises Km — maps to *P. putida* R140 |
| [31401777](https://pubmed.ncbi.nlm.nih.gov/31401777/) | *Amino acids in the 5-FTHF binding site of MTHFS* | E55 and Y123 essential (E55A/E55Q/Y123A inactive) — map to *P. putida* E60 and Y148 |
| [22773193](https://pubmed.ncbi.nlm.nih.gov/22773193/) | *Amino acids in the ATP binding site of MTHFS* | Coulombic/proximity model of ATP-site residues; supports the phosphoryl-transfer mechanism |
| [16376935](https://pubmed.ncbi.nlm.nih.gov/16376935/) | *Diversification of the shared NagB/RpiA-transferase-like fold* | Places MTHFS in the Rossmann-like fold assemblage (IPR037171) |
| [18519731](https://pubmed.ncbi.nlm.nih.gov/18519731/) | *Global regulators and nucleotide metabolism in antibiotic tolerance* | Identifies *E. coli ygfA* as a persister/antibiotic-tolerance gene |
| [23115038](https://pubmed.ncbi.nlm.nih.gov/23115038/) | *F. tularensis folate metabolism and inflammasome* | Cyclo-ligase FTL_0724 required for virulence; modulates inflammasome activation |
| [22948925](https://pubmed.ncbi.nlm.nih.gov/22948925/) | *Structure of E. faecalis thymidylate synthase* | Shows 5-FTHF as a metabolite of cyclo-ligase and a weak TS inhibitor; supports 5-FTHF's regulatory role |
| [19022216](https://pubmed.ncbi.nlm.nih.gov/19022216/) | *MTHFS activity increased in tumors, modifies antipurine efficacy* | MTHFS increases 10-formyl-THF availability for purine synthesis (GARFT), linking the enzyme to purine flux |

**Human-disease and physiology context** (supporting, not central to the *P. putida* assignment): reviews on B-vitamins/homocysteine ([PMID: 15831132](https://pubmed.ncbi.nlm.nih.gov/15831132/)), folate and DNA stability ([PMID: 15831129](https://pubmed.ncbi.nlm.nih.gov/15831129/)), causal susceptibility genes in ischemic stroke ([PMID: 20161734](https://pubmed.ncbi.nlm.nih.gov/20161734/)), and dopamine-stimulated phospholipid methylation ([PMID: 11520899](https://pubmed.ncbi.nlm.nih.gov/11520899/)) illustrate the broader importance of the one-carbon folate pool that MTHFS regulates. These concern mammalian systems and, in several cases, the distinct MTHFR enzyme rather than the *P. putida* cyclo-ligase directly, and are therefore contextual rather than definitive for the target protein.

---

## Limitations and Knowledge Gaps

1. **No direct biochemical characterization of the *P. putida* enzyme.** The functional assignment for Q88CH8 rests entirely on homology-based inference (UniProt PE=3) plus the computational sequence/active-site analysis performed in this investigation. Kinetic parameters (Km, kcat), substrate polyglutamate preference, and the oligomeric state of the *P. putida* protein have not been experimentally measured.

2. **No experimental structure of the *P. putida* protein.** Mechanistic conclusions are transferred from human, *M. pneumoniae*, and *B. anthracis* orthologs. While the fold and active-site residues are highly conserved, an experimental *P. putida* structure (or a validated AlphaFold model with the intermediate docked) has not been examined here.

3. **No genetic/phenotypic data in *P. putida*.** Antifolate susceptibility, folinic-acid accumulation, and persistence phenotypes are documented in *E. coli*, *M. smegmatis*, and *F. tularensis*, not in *P. putida* KT2440. Whether *fau* deletion is tolerated and produces the expected phenotypes in this organism is untested.

4. **Gene-symbol collision.** The symbol "fau" is shared with the unrelated eukaryotic *FAU* (Finkel–Biskis–Reilly murine sarcoma virus-associated ubiquitously expressed / ribosomal protein S30 fusion) gene. This report confirms — via sequence, domains, and active-site residues — that PP_5203 is the folate cyclo-ligase and is unrelated to the ribosomal *FAU*. Care should be taken when mining literature by symbol alone.

5. **Regulation and expression are uncharacterized.** How *fau*/PP_5203 expression is controlled in *P. putida*, and whether it is co-regulated with folate-biosynthesis or one-carbon-metabolism genes, remains unknown.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant expression and enzyme assay.** Clone PP_5203, purify the His-tagged protein, and measure the cyclo-ligase reaction (ATP-dependent conversion of 5-formyl-THF to 5,10-methenyl-THF) spectrophotometrically. Determine Km for 5-formyl-THF and MgATP, and kcat, for comparison with the *M. pneumoniae* and human enzymes.

2. **Polyglutamate substrate specificity.** Test mono- versus polyglutamylated 5-formyl-THF as substrates, since bacterial phenotypes involve accumulation of polyglutamyl folinic acid.

3. **Site-directed mutagenesis validation.** Mutate the predicted catalytic residues E60, R140, and Y148 to alanine and confirm loss of activity, directly testing the homology-based active-site mapping.

4. **Structural determination.** Solve the *P. putida* structure by X-ray crystallography or cryo-EM (or generate and validate an AlphaFold model), ideally trapping the Mg-ADP/phosphate or N5-iminium intermediate state to confirm the conserved mechanism.

5. **Gene knockout in *P. putida* KT2440.** Delete PP_5203 and assay (i) intracellular folinic-acid/5-formyl-THF accumulation by LC-MS, (ii) antifolate (e.g., trimethoprim/sulfonamide) susceptibility, and (iii) antibiotic persistence/tolerance, to test whether the conserved bacterial phenotypes hold in this organism.

6. **Metabolic-flux and expression profiling.** Use ¹³C- or one-carbon-labeled tracers to quantify flux through the SHMT↔MTHFS futile cycle in *P. putida*, and profile *fau* expression under folate stress, antifolate challenge, and different carbon sources.

---

*Report prepared from a 3-iteration autonomous investigation: 6 confirmed findings, 19 papers reviewed. All functional claims are supported by the cited literature and by independent sequence/active-site analysis of UniProt Q88CH8. No dedicated experimental study of the *P. putida* PP_5203 protein was found; the functional assignment is a robust homology-based inference validated at the active-site-residue level.*


## Artifacts

- [OpenScientist final report](fau-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](fau-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:21372133
2. PMID:16104022
3. PMID:7673211
4. PMID:19738041
5. PMID:17329806
6. PMID:30867454
7. PMID:18519731
8. PMID:23115038
9. PMID:16376935
10. PMID:18473156
11. PMID:31401777
12. PMID:15831132
13. PMID:15831129
14. PMID:20161734
15. PMID:11520899