---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-17T14:34:04.775207'
end_time: '2026-07-17T15:16:43.923594'
duration_seconds: 2559.15
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: lysA-I
  gene_symbol: lysA-I
  uniprot_accession: Q88L58
  protein_description: 'RecName: Full=Diaminopimelate decarboxylase {ECO:0000256|HAMAP-Rule:MF_02120,
    ECO:0000256|NCBIfam:TIGR01048}; Short=DAP decarboxylase {ECO:0000256|HAMAP-Rule:MF_02120};
    Short=DAPDC {ECO:0000256|HAMAP-Rule:MF_02120}; EC=4.1.1.20 {ECO:0000256|HAMAP-Rule:MF_02120,
    ECO:0000256|NCBIfam:TIGR01048};'
  gene_info: Name=lysA-I {ECO:0000313|EMBL:AAN67691.1}; Synonyms=lysA {ECO:0000256|HAMAP-Rule:MF_02120};
    OrderedLocusNames=PP_2077 {ECO:0000313|EMBL:AAN67691.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the Orn/Lys/Arg decarboxylase class-II family.
  protein_domains: Ala_racemase/Decarboxylase_C. (IPR009006); DAP_deCOOHase_LysA.
    (IPR002986); De-COase2_CS. (IPR022657); De-COase2_N. (IPR022644); De-COase2_pyr-phos_BS.
    (IPR022653)
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
  path: lysA-I-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: lysA-I-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88L58
- **Protein Description:** RecName: Full=Diaminopimelate decarboxylase {ECO:0000256|HAMAP-Rule:MF_02120, ECO:0000256|NCBIfam:TIGR01048}; Short=DAP decarboxylase {ECO:0000256|HAMAP-Rule:MF_02120}; Short=DAPDC {ECO:0000256|HAMAP-Rule:MF_02120}; EC=4.1.1.20 {ECO:0000256|HAMAP-Rule:MF_02120, ECO:0000256|NCBIfam:TIGR01048};
- **Gene Information:** Name=lysA-I {ECO:0000313|EMBL:AAN67691.1}; Synonyms=lysA {ECO:0000256|HAMAP-Rule:MF_02120}; OrderedLocusNames=PP_2077 {ECO:0000313|EMBL:AAN67691.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the Orn/Lys/Arg decarboxylase class-II family.
- **Key Domains:** Ala_racemase/Decarboxylase_C. (IPR009006); DAP_deCOOHase_LysA. (IPR002986); De-COase2_CS. (IPR022657); De-COase2_N. (IPR022644); De-COase2_pyr-phos_BS. (IPR022653)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "lysA-I" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'lysA-I' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **lysA-I** (gene ID: lysA-I, UniProt: Q88L58) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# lysA-I (Q88L58 / PP_2077): Diaminopimelate Decarboxylase of *Pseudomonas putida* KT2440

**Gene:** lysA-I (synonym *lysA*; ordered locus PP_2077)
**Protein:** Diaminopimelate decarboxylase (DAPDC / DAP decarboxylase)
**UniProt:** Q88L58 · **EC:** 4.1.1.20 · **Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / KT2440), PSEPK

---

## Summary

**lysA-I encodes diaminopimelate decarboxylase (DAPDC; EC 4.1.1.20), the pyridoxal-5′-phosphate (PLP)-dependent enzyme that catalyzes the terminal, committed, and irreversible step of L-lysine biosynthesis: meso-2,6-diaminopimelate + H⁺ → L-lysine + CO₂ (RHEA:15101).** This identification is unambiguous and internally consistent: the target gene symbol, UniProt annotation, enzyme classification, protein family (Orn/Lys/Arg decarboxylase class-II, i.e., fold-type III / alanine-racemase fold), and conserved catalytic domains all converge on this single biochemical function. The verification steps mandated by the research brief are satisfied — the gene symbol lysA-I matches the DAP decarboxylase description, the organism is correctly *P. putida* KT2440, and the family/domain architecture aligns with the DAPDC literature. No competing gene identity was encountered.

The enzyme is a soluble, cytoplasmic, obligate homodimer with no signal peptide and no membrane-spanning segment. It performs its chemistry in the cytosol, where it sits at a pivotal **metabolic branch point**: its substrate, meso-diaminopimelate (meso-DAP), is simultaneously a direct cross-linking residue of Gram-negative peptidoglycan and the immediate precursor of free L-lysine. By decarboxylating meso-DAP, DAPDC partitions carbon and nitrogen flux between cell-wall construction (retaining meso-DAP) and protein synthesis (producing L-lysine). It is the single convergent terminal enzyme onto which two annotated meso-DAP-producing routes in *P. putida* — the succinyl-DAP pathway (KEGG M00016) and the DAP-aminotransferase pathway (KEGG M00527) — both feed.

Mechanistically, DAPDC is a fold-type III PLP decarboxylase that is highly specific for meso-DAP. Specificity is achieved by recognition of the L-configured stereocenter of the substrate combined with a system of ionic "molecular rulers" — two active-site arginines (Arg262/Arg298 in Q88L58) — that gauge substrate length. Catalysis proceeds by a **two-base mechanism** involving the PLP internal aldimine to Lys45 and a catalytic Cys332 proton donor, and the reaction runs with **net inversion of configuration** at the reacting carbon, a hallmark that distinguishes meso-DAP decarboxylase from other α-amino-acid decarboxylases. An AlphaFold model (global pLDDT 95.1) independently reproduces the canonical two-domain architecture and places all functional residues at very-high confidence, with a composite active site assembled across the dimer interface. Because the DAP/lysine pathway is absent in mammals and is essential in bacteria where tested, DAPDC is a validated, selective antibacterial target — although in *P. putida* a second, ~48%-identical paralog (lysA-II / PP_5227) may provide functional redundancy.

---

## Key Findings

### F001 — Core identity and reaction

Q88L58 (lysA-I / PP_2077) is a PLP-dependent diaminopimelate decarboxylase catalyzing the final step of lysine biosynthesis. UniProtKB assigns EC 4.1.1.20 and the catalytic reaction **meso-2,6-diaminopimelate + H⁺ → L-lysine + CO₂** (RHEA:15101). The cofactor pyridoxal-5′-phosphate is bound as an internal aldimine (Schiff base) to **Lys45** (annotated feature "N6-(pyridoxal phosphate)lysine" at position 45). The mature protein is 410 amino acids and assembles as a **homodimer**. It occupies the terminal position in the diaminopimelate (DAP) pathway of L-lysine biosynthesis, formally "L-lysine from DL-2,6-diaminopimelate: step 1/1." Gene Ontology annotations are fully consistent: GO:0008836 (diaminopimelate decarboxylase activity), GO:0030170 (PLP binding), and GO:0009089 (L-lysine biosynthesis via DAP). The active-site lysine/proton-donor and substrate/PLP-binding residues are annotated at positions 218, 259, 262, 298, 302, 332/333, 367. The protein belongs to the Orn/Lys/Arg decarboxylase class-II family (fold-type III, alanine-racemase fold). This is the anchoring finding: the identity of the gene product as DAPDC is unambiguous and self-consistent across reaction, cofactor, pathway, and family annotations.

### F002 — Two divergent DAPDC paralogs in *P. putida* KT2440

*P. putida* KT2440 encodes **two** divergent DAP decarboxylase paralogs. A UniProt taxonomy search (taxid 160488, EC 4.1.1.20) returns exactly two entries: **Q88L58 = lysA-I / PP_2077 (410 aa)** and **Q88CF4 = lysA-II / PP_5227 (415 aa)**, both annotated as diaminopimelate decarboxylase. A Needleman–Wunsch global alignment of the two sequences yields 174/364 aligned identical positions = **47.8% pairwise identity**. Both retain the class-II Orn/Lys/Arg decarboxylase fold and the DAP-decarboxylase family signatures. The presence of two moderately divergent paralogs raises the possibility of functional redundancy, differential regulation, or subtle substrate/kinetic specialization — an important caveat for any inference about essentiality of lysA-I alone in this organism.

### F003 — Mechanism and substrate specificity: fold-type III PLP decarboxylase acting with inversion

DAPDC recognizes the L-stereocenter of meso-DAP and decarboxylates with inversion of configuration. Cocrystal structures of *Methanococcus jannaschii* DAPDC with a substrate analog (azelaic acid, Ki = 89 µM) and with the L-lysine product (2.0–2.6 Å) demonstrated that **substrate specificity arises from recognition of the L-chiral center of diaminopimelate and a system of ionic "molecular rulers" that dictate substrate length** ([PMID: 12429091](https://pubmed.ncbi.nlm.nih.gov/12429091/), Ray et al. 2002). meso-DAP possesses one D- and one L-configured stereocenter; DAPDC removes CO₂ from the D-configured carbon while recognizing the L-stereocenter, and the reaction proceeds with **inversion of configuration** at the reacting carbon. This stereochemical course was established by ²H-labeling/NMR studies for the *Bacillus sphaericus* and wheat-germ meso-DAP decarboxylases ([PMID: 3927976](https://pubmed.ncbi.nlm.nih.gov/3927976/), Kelland et al. 1985), and it contrasts with the *retention* of configuration seen with many other α-amino-acid decarboxylases — a mechanistically diagnostic distinction. In Q88L58 the corresponding functional features are the PLP internal aldimine to Lys45, the catalytic proton donor at the active site, and substrate/PLP-binding residues at 218/259/262/298/302/333/367.

> "This PLP-dependent enzyme is responsible for the final step of L-lysine biosynthesis in bacteria" — [PMID: 12429091](https://pubmed.ncbi.nlm.nih.gov/12429091/)

### F004 — Branch-point role and validated antibacterial target

The lysA-I product, L-lysine, sits at the branch point between protein synthesis and peptidoglycan/cell-wall metabolism, and the DAP pathway is an essential, validated antibacterial target. DAPDC catalyzes the terminal step converting meso-DAP → L-lysine (UniProt: step 1/1). Crucially, **meso-DAP itself is a direct cross-linking residue of Gram-negative peptidoglycan**, so DAPDC governs the flux split between a cell-wall precursor (meso-DAP retained) and free L-lysine (committed to protein synthesis). As noted by Zheng et al. 2022, "*Diaminopimelic acid (DAP) is a unique component of the cell wall of Gram-negative bacteria*" ([PMID: 36040174](https://pubmed.ncbi.nlm.nih.gov/36040174/)). Genetic essentiality of the terminal enzyme has been demonstrated in other bacteria: conditional knockdown of *lysA* in *Mycobacterium tuberculosis* confirmed its essentiality for growth ([PMID: 22840772](https://pubmed.ncbi.nlm.nih.gov/22840772/), Abrahams et al. 2012). Because mammals lack the DAP pathway entirely (they obtain lysine from the diet), DAPDC has **no human ortholog**, making it an attractive antibacterial and herbicide target. Regarding localization, Q88L58 has no signal peptide and no membrane-spanning segment (maximum Kyte–Doolittle 19-residue hydropathy = 1.11, well below the ~1.6 transmembrane threshold), consistent with a **soluble cytoplasmic enzyme** with homodimeric quaternary structure.

> "The essentiality of panC and lysA" — [PMID: 22840772](https://pubmed.ncbi.nlm.nih.gov/22840772/)

### F005 — Two-base active site: PLP–Lys45, catalytic Cys332, and Arg262/Arg298 molecular rulers

UniProt residue-level features for Q88L58 (verified against the sequence) define the catalytic machinery: the **modified residue Lys45** carries the N6-(pyridoxal-phosphate)lysine internal aldimine; the **active site Cys332** is the proton donor (in the motif GPLCESGD); and substrate/PLP-binding residues include Glu259, Arg262, Arg298, Tyr302, Glu333, and Tyr367. The two active-site arginines, **Arg262 and Arg298**, correspond to the ionic "molecular rulers" that recognize the distal carboxylate/amino groups of meso-DAP and thereby dictate substrate length — the same feature demonstrated crystallographically in the *M. jannaschii* enzyme ([PMID: 12429091](https://pubmed.ncbi.nlm.nih.gov/12429091/)). The catalytic cysteine sits on the opposite face of the PLP–substrate aldimine from Lys45, providing the **second base** required for decarboxylation with net inversion of configuration. Notably, the catalytic-Cys motif GP[L/I]C[E][S/T]GD is conserved in **both** *P. putida* paralogs — lysA-I "GPLCESGD" (Cys332) and lysA-II "GPICETGD" (aligned Cys) — indicating both paralogs preserve the canonical two-base mechanism. Tyr367 is a cross-subunit residue, consistent with the obligate homodimer in which the active site is completed by the partner monomer.

### F006 — Divergent LysR regulator (PP_2078) implies local transcriptional control

lysA-I (PP_2077) is genomically divergent from a dedicated LysR-family transcriptional regulator (PP_2078). KEGG genomic coordinates (*P. putida* KT2440) place **PP_2077/lysA-I on the complement strand, complement(2364209..2365441)**, immediately adjacent to **PP_2078/lysR (LysR-family transcriptional activator) on the forward strand, 2365565..2366470**. The two genes are **divergently transcribed**, with their 5′ ends facing each other across a ~124 bp intergenic region (2365442–2365564) — the canonical architecture of a LysR-type transcriptional regulator (LTTR) controlling a divergent target gene. The flanking genes PP_2075/PP_2076 (complement strand, "unknown function") are separated from lysA-I by a ~330 bp gap, arguing against a single operon with DAP-synthesis genes; lysA-I appears to be its own transcriptional unit. KEGG orthology K01586 (EC 4.1.1.20); Pfam motifs Orn_Arg_deC_N, Orn_DAP_Arg_deC, Ala_racemase_N. This genomic architecture suggests local, likely lysine/DAP-responsive transcriptional control of the terminal biosynthetic step.

### F007 — Convergent terminal enzyme for two meso-DAP routes

In *P. putida* KT2440, lysA-I acts as the common terminal enzyme for two annotated meso-DAP-producing routes. KEGG maps PP_2077 (K01586) to the Lysine biosynthesis pathway ppu00300 and to two lysine-biosynthesis modules: **M00016 (Lysine biosynthesis, succinyl-DAP pathway, aspartate ⇒ lysine)** and **M00527 (Lysine biosynthesis, DAP-aminotransferase pathway, aspartate ⇒ lysine)**. Both modules share the early aspartate → tetrahydrodipicolinate steps and converge on meso-2,6-diaminopimelate, which DAPDC (LysA) decarboxylates to L-lysine. Additional KEGG pathway memberships include D-amino acid metabolism (ppu00470) and biosynthesis of amino acids (ppu01230). DAPDC is therefore the single convergent funnel through which two upstream routes reach lysine.

### F008 — AlphaFold confirms the two-domain fold and composite dimer-interface active site

The AlphaFold model of Q88L58 (AF-Q88L58-F1, v6) confirms a high-confidence two-domain DAPDC fold. The **global pLDDT = 95.1**, with 89% of residues at very-high confidence (>90) and 97% above 70. All annotated functional residues are modeled at very-high confidence: Lys45 = 98.4, Glu259 = 97.5, Arg262 = 96.7, Arg298 = 97.5, Tyr302 = 93.5, Cys332 = 97.6, Glu333 = 97.6, Tyr367 = 98.2. Within the monomer, the PLP-binding Lys45 clusters spatially with Glu259 (Cα–Cα 11.0 Å), Arg262 (9.3 Å), and Arg298 (13.9 Å), forming a contiguous substrate/cofactor pocket, whereas the catalytic Cys332 lies 27.7 Å from Lys45 and Tyr367 is a cross-subunit residue — geometry consistent with DAPDC's known **composite active site assembled across the homodimer interface**. The N-terminal region (residues 1–290, mean pLDDT 94.3) corresponds to the (β/α)₈ TIM-barrel-like PLP-binding domain, and the C-terminal region (300–410, 96.9) to the β-sandwich domain — the canonical two-domain fold-type III architecture (Pfam Orn_Arg_deC_N + Orn_DAP_Arg_deC; InterPro IPR009006/IPR002986).

### F009 — Authoritative review validates the dual metabolic destination and target status

An authoritative review confirms that lysine biosynthesis provides both L-lysine (protein synthesis) and meso-DAP (peptidoglycan), validating DAPDC's branch-point role and antibacterial-target status. Hutton, Southwood & Turner (2003), *Inhibitors of lysine biosynthesis as antibacterial agents* ([PMID: 12570844](https://pubmed.ncbi.nlm.nih.gov/12570844/)), state that the bacterial lysine biosynthetic pathway "provides both lysine for protein synthesis and meso-diaminopimelate for construction of the bacterial peptidoglycan cell wall," and has "come under increased scrutiny as a target for novel antibacterial agents." DAPDC (LysA) catalyzes the terminal meso-DAP → L-lysine step, sitting exactly at this branch. Combined with the mammalian absence of the pathway and demonstrated bacterial essentiality of *lysA* ([PMID: 22840772](https://pubmed.ncbi.nlm.nih.gov/22840772/)), this establishes DAPDC as a selective antibacterial target.

> "it provides both lysine for protein synthesis and meso-diaminopimelate for construction of the bacterial peptidoglycan cell wall" — [PMID: 12570844](https://pubmed.ncbi.nlm.nih.gov/12570844/)

> "Bacterial biosynthesis of lysine has come under increased scrutiny as a target for novel antibacterial agents" — [PMID: 12570844](https://pubmed.ncbi.nlm.nih.gov/12570844/)

---

## Mechanistic Model and Interpretation

### The catalyzed reaction

```
   meso-2,6-diaminopimelate  +  H+   ──DAPDC (PLP)──►   L-lysine  +  CO2
   (RHEA:15101, EC 4.1.1.20)
```

DAPDC is a **PLP-dependent, fold-type III (alanine-racemase-fold)** decarboxylase. The reaction is the **terminal, committed, irreversible** step of the DAP pathway and is the sole biochemical route in bacteria for generating free L-lysine from the DAP intermediate pool.

### Catalytic cycle (two-base mechanism)

```
  1. Resting state:   PLP ═ Nε-Lys45  (internal aldimine / Schiff base)
  2. Transaldimination: meso-DAP amino group displaces Lys45
                        → external aldimine (PLP ═ substrate)
  3. Decarboxylation: CO2 lost from the D-carboxyl; PLP acts as
                      electron sink → quinonoid intermediate
                      (Arg262 / Arg298 molecular rulers clamp the
                       distal carboxylate & amino group, enforcing
                       meso-DAP length/geometry)
  4. Reprotonation:   catalytic Cys332 delivers H+ to the OPPOSITE
                      face → NET INVERSION of configuration
  5. Product release: L-lysine released; Lys45 re-forms internal aldimine
```

The two-base arrangement — Lys45 on one face (forms the aldimine) and Cys332 on the opposite face (reprotonates the quinonoid) — is what produces the diagnostic **inversion of configuration** observed by NMR/²H-labeling in orthologous enzymes ([PMID: 3927976](https://pubmed.ncbi.nlm.nih.gov/3927976/)). The "molecular rulers" (Arg262/Arg298) explain the strict specificity for meso-DAP over shorter diamino acids ([PMID: 12429091](https://pubmed.ncbi.nlm.nih.gov/12429091/)).

### Quaternary structure and active-site geometry

The enzyme is an **obligate homodimer**. Within a single monomer the PLP pocket (Lys45, Glu259, Arg262, Arg298) is contiguous, but the catalytic Cys332 (~28 Å away in the monomer model) and the cross-subunit residue Tyr367 indicate that a **complete active site is built across the dimer interface**, requiring both protomers. AlphaFold (pLDDT 95) independently reproduces the two-domain fold and the spatial clustering of functional residues, corroborating the crystallographic paradigm without an experimental *P. putida* structure.

### Position in metabolism — the branch point

```
        aspartate
           │  (shared early steps → tetrahydrodipicolinate)
           ▼
   ┌───────────────────────────────┐
   │  succinyl-DAP route (M00016)  │──┐
   ├───────────────────────────────┤  │
   │  DAP-aminotransferase (M00527)│──┤ converge on
   └───────────────────────────────┘  ▼
                          meso-2,6-DIAMINOPIMELATE  ◄── peptidoglycan
                                   │                     cross-linking
                            lysA-I │ (DAPDC, PP_2077)    (meso-DAP retained)
                                   ▼
                               L-LYSINE  ──► protein synthesis
```

DAPDC is the **convergent funnel** for both annotated meso-DAP routes (F007) and the **valve** that decides whether meso-DAP is committed to lysine or retained for cell-wall cross-linking (F004, F009). Its genomic pairing with a divergent LysR regulator (PP_2078; F006) suggests this valve is under local transcriptional control, plausibly responsive to lysine/DAP status.

### Localization

| Property | Value | Interpretation |
|---|---|---|
| Signal peptide | Absent | Not secreted |
| Transmembrane segments | 0 (max hydropathy 1.11 < 1.6) | Not membrane-associated |
| Quaternary structure | Homodimer | Composite active site |
| Compartment | Cytoplasm | Soluble cytosolic enzyme |

### Paralog comparison

| Feature | lysA-I (Q88L58 / PP_2077) | lysA-II (Q88CF4 / PP_5227) |
|---|---|---|
| Length | 410 aa | 415 aa |
| Annotation | Diaminopimelate decarboxylase | Diaminopimelate decarboxylase |
| Catalytic-Cys motif | GPLCESGD | GPICETGD |
| Pairwise identity | — | 47.8% to lysA-I |
| Fold / family | Class-II Orn/Lys/Arg deCase (fold-type III) | Same |

Both paralogs preserve the two-base catalytic motif, so functional redundancy is plausible; whether they differ in regulation, expression, or fine kinetics is unresolved.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [12429091](https://pubmed.ncbi.nlm.nih.gov/12429091/) | *Cocrystal structures of diaminopimelate decarboxylase* (Ray et al. 2002) | Primary structural evidence for L-stereocenter recognition and "molecular ruler" substrate-length specificity; confirms PLP dependence and terminal-step role. Supports F003, F005. |
| [3927976](https://pubmed.ncbi.nlm.nih.gov/3927976/) | *Stereochemistry of lysine formation by meso-DAP decarboxylase (wheat germ)* (Kelland et al. 1985) | ²H-NMR evidence establishing **inversion of configuration** — mechanistic hallmark. Supports F003. |
| [22840772](https://pubmed.ncbi.nlm.nih.gov/22840772/) | *Pathway-selective sensitization of M. tuberculosis* (Abrahams et al. 2012) | Demonstrates genetic **essentiality of lysA** in a bacterium. Supports F004, F009. |
| [12570844](https://pubmed.ncbi.nlm.nih.gov/12570844/) | *Inhibitors of lysine biosynthesis as antibacterial agents* (Hutton et al. 2003) | Authoritative review: dual destination (lysine + meso-DAP for peptidoglycan); antibacterial-target status. Supports F004, F009. |
| [36040174](https://pubmed.ncbi.nlm.nih.gov/36040174/) | *Diaminopimelic Acid Metabolism* (Zheng et al. 2022) | meso-DAP as a unique Gram-negative cell-wall component, defining the branch point. Supports F004. |
| [8206742](https://pubmed.ncbi.nlm.nih.gov/8206742/) | *Regulation of DHDPS and DAP decarboxylase in B. stearothermophilus* | Context on feedback inhibition of DAP decarboxylase by L-lysine in a related bacterium (background). |

**Database and computational evidence:** UniProtKB Q88L58 (reaction, cofactor, residue-level features, GO terms, family); KEGG *P. putida* KT2440 (K01586, ppu00300, modules M00016/M00527, genomic coordinates); AlphaFold DB AF-Q88L58-F1 (pLDDT 95.1); Pfam/InterPro domain assignments; Needleman–Wunsch paralog alignment (47.8% identity); Kyte–Doolittle hydropathy analysis.

**Note on organism specificity:** the mechanistic and structural details (F003, F005) are drawn from orthologous DAPDC enzymes (*M. jannaschii*, wheat germ, *B. sphaericus*), transferred to Q88L58 by sequence/family homology and the conservation of the exact catalytic residues (Lys45, Cys332, Arg262/Arg298). No experimental study of the *P. putida* KT2440 lysA-I protein itself was found; conclusions about it rest on annotation, homology, and AlphaFold modeling.

---

## Limitations and Knowledge Gaps

1. **No direct experimental characterization of Q88L58.** All functional claims for the *P. putida* KT2440 protein derive from UniProt/KEGG annotation, homology to structurally characterized orthologs, and AlphaFold modeling. There is no published enzymology (kinetics, Km/kcat for meso-DAP), no crystal structure, and no gene-knockout phenotype specifically for lysA-I.

2. **Paralog redundancy is unresolved.** *P. putida* KT2440 has two DAPDC paralogs (~48% identical). Whether lysA-I is individually essential — or whether lysA-II can compensate — is unknown. Essentiality was demonstrated for *lysA* in *M. tuberculosis* (single-copy), which does not necessarily transfer to a two-paralog organism.

3. **Regulation is inferred, not demonstrated.** The divergent LysR regulator (PP_2078) implies local transcriptional control, but no experiment defines the effector, the operator, or whether PP_2078 activates or represses lysA-I. Feedback inhibition of DAP decarboxylase by L-lysine is documented in *B. stearothermophilus* but not verified for *P. putida* lysA-I.

4. **Stereochemistry/inversion is transferred from orthologs.** The inversion-of-configuration mechanism was established in wheat-germ and *B. sphaericus* enzymes; it is assumed conserved in lysA-I based on identical catalytic-residue architecture but not directly measured.

5. **Which upstream route dominates in vivo is unknown.** KEGG lists both the succinyl-DAP and DAP-aminotransferase routes; the relative in-vivo flux through each in *P. putida* KT2440 has not been quantified.

6. **AlphaFold is a monomer model.** The composite dimer-interface active site is inferred from residue geometry and orthologous structures; the dimer itself was not modeled or experimentally confirmed for this protein.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant enzymology.** Express and purify Q88L58, reconstitute with PLP, and measure steady-state kinetics (Km, kcat) with meso-DAP; test specificity against LL-DAP, DD-DAP, and shorter diamino acids to confirm the "molecular ruler" prediction.

2. **Active-site mutagenesis.** Generate K45A, C332A/C332S, R262A, and R298A variants to validate the two-base mechanism and the ionic-ruler roles; expect loss of activity for K45/C332 and relaxed length specificity for R262/R298.

3. **Stereochemical assay.** Use ²H₂O incubation with chiral NMR (as in [PMID: 3927976](https://pubmed.ncbi.nlm.nih.gov/3927976/)) to directly confirm inversion of configuration for the *P. putida* enzyme.

4. **Genetics of redundancy.** Construct single (ΔlysA-I, ΔlysA-II) and double knockouts in KT2440; test lysine auxotrophy and cross-complementation to establish individual vs. combined essentiality.

5. **Regulation.** Build a lysA-I promoter–reporter fusion; delete/overexpress PP_2078 (LysR) and vary lysine availability to define the regulatory logic and effector.

6. **Structure.** Determine an experimental crystal or cryo-EM structure of the homodimer, ideally with PLP and a substrate analog (e.g., azelaic acid), to confirm the cross-subunit composite active site predicted by AlphaFold.

7. **Feedback inhibition.** Test L-lysine (and analogs such as S-2-aminoethyl-cysteine) as inhibitors of purified DAPDC, paralleling the *B. stearothermophilus* observations ([PMID: 8206742](https://pubmed.ncbi.nlm.nih.gov/8206742/)).

8. **Inhibitor / target validation.** Given the mammalian absence of the pathway, screen DAPDC-directed inhibitors against both paralogs for antibacterial-lead potential.

---

## Conclusion

lysA-I (Q88L58 / PP_2077) of *Pseudomonas putida* KT2440 is **diaminopimelate decarboxylase (DAPDC, EC 4.1.1.20)** — a PLP-dependent, fold-type III, cytoplasmic homodimeric enzyme that catalyzes the final, committed, irreversible step of L-lysine biosynthesis (meso-2,6-diaminopimelate → L-lysine + CO₂). It is highly specific for meso-DAP via L-stereocenter recognition and Arg262/Arg298 molecular rulers, uses a two-base (PLP-Lys45 / Cys332) mechanism proceeding with inversion of configuration, sits at the meso-DAP branch point between protein synthesis and peptidoglycan, is the convergent terminal enzyme for two upstream DAP routes, is under likely LysR (PP_2078) control, and — being absent in mammals — is a validated antibacterial target, with a ~48%-identical paralog (lysA-II / PP_5227) as a possible redundancy factor.


## Artifacts

- [OpenScientist final report](lysA-I-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](lysA-I-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:12429091
2. PMID:3927976
3. PMID:36040174
4. PMID:22840772
5. PMID:12570844
6. PMID:8206742