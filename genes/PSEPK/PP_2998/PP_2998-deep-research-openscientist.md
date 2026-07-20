---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-18T13:50:19.320391'
end_time: '2026-07-18T14:30:01.978302'
duration_seconds: 2382.66
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_2998
  gene_symbol: PP_2998
  uniprot_accession: Q88IK1
  protein_description: 'RecName: Full=2-dehydropantoate 2-reductase {ECO:0000256|ARBA:ARBA00019465,
    ECO:0000256|RuleBase:RU362068}; EC=1.1.1.169 {ECO:0000256|ARBA:ARBA00013014, ECO:0000256|RuleBase:RU362068};
    AltName: Full=Ketopantoate reductase {ECO:0000256|ARBA:ARBA00032024, ECO:0000256|RuleBase:RU362068};'
  gene_info: OrderedLocusNames=PP_2998 {ECO:0000313|EMBL:AAN68606.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the ketopantoate reductase family.
  protein_domains: 6-PGluconate_DH-like_C_sf. (IPR008927); 6PGD_dom2. (IPR013328);
    ApbA. (IPR003710); KPA_reductase. (IPR013752); KPR-Related. (IPR051402)
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
  path: PP_2998-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PP_2998-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88IK1
- **Protein Description:** RecName: Full=2-dehydropantoate 2-reductase {ECO:0000256|ARBA:ARBA00019465, ECO:0000256|RuleBase:RU362068}; EC=1.1.1.169 {ECO:0000256|ARBA:ARBA00013014, ECO:0000256|RuleBase:RU362068}; AltName: Full=Ketopantoate reductase {ECO:0000256|ARBA:ARBA00032024, ECO:0000256|RuleBase:RU362068};
- **Gene Information:** OrderedLocusNames=PP_2998 {ECO:0000313|EMBL:AAN68606.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the ketopantoate reductase family.
- **Key Domains:** 6-PGluconate_DH-like_C_sf. (IPR008927); 6PGD_dom2. (IPR013328); ApbA. (IPR003710); KPA_reductase. (IPR013752); KPR-Related. (IPR051402)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_2998" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_2998' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_2998** (gene ID: PP_2998, UniProt: Q88IK1) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: PP_2998 (Q88IK1) — Ketopantoate Reductase (PanE) of *Pseudomonas putida* KT2440

## Summary

**PP_2998** (UniProt **Q88IK1**) of *Pseudomonas putida* strain KT2440 (ATCC 47054 / DSM 6125) encodes **ketopantoate reductase**, also called **2-dehydropantoate 2-reductase** or **PanE** (**EC 1.1.1.169**). Its primary and defining function is enzymatic: it catalyzes the **NADPH-dependent, stereospecific reduction of 2-dehydropantoate (ketopantoate) to (R)-pantoate**, the second of the two committed steps that convert the branched-chain-amino-acid precursor 3-methyl-2-oxobutanoate (α-ketoisovalerate) into pantoate. This reaction is a required node in the **pantothenate (vitamin B5) → coenzyme A (CoA)** biosynthetic pathway. The gene is a member of the **ketopantoate reductase family**, and its InterPro/Pfam domain architecture — an N-terminal Rossmann-fold dinucleotide-binding domain (ApbA / KPA_reductase, IPR003710 / IPR013752) fused to a C-terminal α-helical domain of the 6-phosphogluconate-dehydrogenase C-terminal-domain-like superfamily (IPR008927 / IPR013328) — is diagnostic of this enzyme class and is fully consistent with the experimentally solved structure of the *E. coli* ortholog.

The identity of PP_2998 as a bona fide PanE was verified at three levels. First, the UniProt annotation, EC number, family assignment, and domain complement all agree. Second, a direct sequence alignment to the biochemically and structurally characterized *E. coli* PanE (P0A9J4) shows conservation of the two experimentally defined active-site residues — the catalytic **Lys** (Lys176 in *E. coli* → **Lys186** in PP_2998) and the substrate-binding **Asn** (Asn98 → **Asn103**) — together with an intact Rossmann-fold GxGxxG cofactor fingerprint (GAGALG, residues 7–12). Third, the full pantothenate pathway was reconstructed in KT2440: PP_2998 (PanE) sits between **PP_4699 (PanB)** and **PP_4700 (PanC)**, confirming its pathway context. Because no crystal structure, knockout, or enzymology has been published for the *P. putida* protein itself, its detailed mechanistic and structural properties are inferred by strong orthology from the extensively studied *E. coli* and *Salmonella* enzymes.

Functionally, the enzyme operates in the **cytoplasm** as a soluble, monomeric ~34 kDa protein (by orthology; no signal peptide or transmembrane helix is present). It uses an **ordered sequential kinetic mechanism** (NADPH binds first, then ketopantoate; pantoate is released before NADP⁺), transfers the **pro-S hydride of NADPH** to C-2 of the substrate, and is highly specific for ketopantoate over related α-keto acids and for NADPH over other nucleotides. In *P. putida*, *panE* is **monocistronic**, physically separated from the *panBC* genes — mirroring the arrangement in *E. coli* — and the pathway supplies pantoate for the essential, human-absent CoA biosynthetic route that is of active interest as an antibacterial/antitubercular/antiparasitic drug target.

---

## Key Findings

### Finding 1 — PP_2998 is a ketopantoate reductase (EC 1.1.1.169) catalyzing NADPH-dependent reduction of ketopantoate to pantoate

The core molecular function of PP_2998 is established by convergent database annotation and orthologous biochemistry. UniProt Q88IK1 annotates the protein as **2-dehydropantoate 2-reductase (ketopantoate reductase), EC 1.1.1.169**, placing it in the ketopantoate reductase family and carrying the diagnostic **ApbA / KPA_reductase** domains (IPR003710, IPR013752). The reaction catalyzed is:

> **2-dehydropantoate + NADPH + H⁺ → (R)-pantoate + NADP⁺**

This chemistry is directly and quantitatively established for the orthologous *E. coli* PanE enzyme. Matak-Vinković *et al.* (2001) measured **K_M(NADPH) = 20 µM, K_M(ketopantoate) = 60 µM, and k_cat = 40 s⁻¹**, defining the reaction as "the NADPH-dependent reduction of ketopantoate to pantoate on the pantothenate (vitamin B5) biosynthetic pathway" ([PMID: 11724562](https://pubmed.ncbi.nlm.nih.gov/11724562/)). Genetic evidence that this activity is encoded by *panE* comes from classic *Salmonella* work: *panE* strains had "greatly reduced levels of ketopantoic acid reductase (3 to 12% of the activity present in DU201)," and such mutants are pantoate auxotrophs ([PMID: 6401279](https://pubmed.ncbi.nlm.nih.gov/6401279/)). Together these anchor the reaction, EC number, and physiological requirement for the family to which PP_2998 belongs.

### Finding 2 — Ordered sequential kinetic mechanism with general acid/base catalysis and pro-S hydride transfer

The catalytic mechanism, established for the *E. coli* ortholog, is expected to hold for PP_2998 given full active-site conservation. Zheng & Blanchard (2000) showed that steady-state initial-velocity and product-inhibition patterns fit an **ordered sequential mechanism in which NADPH binds first, ketopantoate binds second, and pantoate is released before NADP⁺** ([PMID: 10736170](https://pubmed.ncbi.nlm.nih.gov/10736170/)). A single general acid/base residue is implicated by pH studies (pK ≈ 8.4 acting as general acid in the reduction direction; pK ≈ 7.8 as general base in the oxidation direction). ¹H-NMR demonstrated the **stereospecific transfer of the pro-S hydrogen of NADPH to the C-2 position of ketopantoate** ([PMID: 10736170](https://pubmed.ncbi.nlm.nih.gov/10736170/)). Small primary deuterium kinetic isotope effects (1.3–1.5) indicate that hydride transfer is not fully rate-limiting.

The enzyme is also **highly substrate-specific**. Zheng & Blanchard (2003) reported that "the enzyme exhibits high specificity for ketopantoate, with V and V/K for ketopantoate being 5- and 365-fold higher than those values for alpha-ketoisovalerate" ([PMID: 14503879](https://pubmed.ncbi.nlm.nih.gov/14503879/)); V/K for ketopantoate is also ~648-fold higher than for α-keto-β-methyl-n-valerate, and NADPH is strongly preferred over other dinucleotides. This specificity underscores that the enzyme's dedicated physiological role is pantoate production, not general α-keto acid reduction.

### Finding 3 — Monomeric two-domain architecture of the 6-phosphogluconate dehydrogenase C-terminal superfamily

The structural class of PP_2998 is fixed by both its InterPro domains and the crystal structure of its ortholog. The *E. coli* KPR structure (1.7 Å; Matak-Vinković *et al.* 2001) is a **monomer of ~34 kDa with two domains separated by a cleft**: an N-terminal Rossmann-fold dinucleotide-binding domain and a C-terminal eight-helix domain. The authors describe it as having "two domains separated by a cleft. The N-terminal domain has an alphabeta-fold of the Rossmann type," and show that "KPR is … a member of the 6-phosphogluconate dehydrogenase C-terminal domain-like superfamily" ([PMID: 11724562](https://pubmed.ncbi.nlm.nih.gov/11724562/)). These match exactly the InterPro annotations on Q88IK1: 6-PGluconate_DH-like_C_sf (IPR008927), 6PGD_dom2 (IPR013328), ApbA (IPR003710), and KPA_reductase (IPR013752).

The NADP⁺-bound structure (Lobley *et al.* 2005, 2.1 Å) places the cofactor in the interdomain cleft and quantifies cofactor thermodynamics by ITC: **K_d(NADP⁺) = 6.5 µM, 20-fold larger than K_d(NADPH) = 0.34 µM** ("The dissociation constant for NADP(+) was found to be 6.5 muM, 20-fold larger than that for NADPH (0.34 muM)"), consistent with the enzyme's preference for the reduced cofactor ([PMID: 15966718](https://pubmed.ncbi.nlm.nih.gov/15966718/)). The same study proposes "a conformational switch of the essential Lys176 from the 'resting' state … to an 'active' state, to bind ketopantoate," and identifies "the importance of Asn98 for substrate binding and enzyme catalysis" ([PMID: 15966718](https://pubmed.ncbi.nlm.nih.gov/15966718/)) — the two residues conserved in PP_2998 (see Finding 5).

### Finding 4 — Pathway role in pantothenate/CoA biosynthesis, with a partially redundant moonlighting route via IlvC

PP_2998/PanE operates in the **pantothenate (vitamin B5) / coenzyme A biosynthetic pathway**. It reduces ketopantoate — the product of PanB (ketopantoate hydroxymethyltransferase) — to pantoate, which PanC (pantothenate synthetase) then condenses with β-alanine to form pantothenate. Importantly, the pantoate step has a **partially redundant backup**: in *Salmonella*, the acetohydroxyacid isomeroreductase **IlvC moonlights as a 2-dehydropantoate 2-reductase**. Primerano & Burns (1983) found that "the acetohydroxy acid isomeroreductase from S. typhimurium efficiently bound alpha-ketopantoate (K(m) = 0.25 mM) and catalyzed its reduction at 1/20 the rate at which alpha-acetolactate was reduced" ([PMID: 6401279](https://pubmed.ncbi.nlm.nih.gov/6401279/)); only a *panE ilvC* double block abolishes pantoate synthesis.

The physiological consequence of losing PanE is a measurable drop in CoA supply. Ernst *et al.* (2018) demonstrated that "elimination of the 2-dehydropantoate 2-reductase, PanE, both reduces total coenzyme A (CoA) levels and causes a conditional HMP-P auxotrophy in *Salmonella enterica*" ([PMID: 29791499](https://pubmed.ncbi.nlm.nih.gov/29791499/)), directly tying the enzyme to CoA output and revealing cross-talk with thiamine biosynthesis.

### Finding 5 — Sequence-level confirmation of PP_2998 identity: conserved catalytic residues and Rossmann motif

Direct sequence analysis confirms PP_2998 is a genuine PanE rather than a mis-annotated homolog. UniProt Q88IK1 (Q88IK1_PSEPK) is *Pseudomonas putida* KT2440 (taxId 160488), gene PP_2998 (EMBL AAN68606.1), **315 aa**, with a Ketopantoate reductase N-terminal domain (residues 3–152) and C-terminal domain (residues 178–303). Its listed catalytic activity is "(R)-pantoate + NADP⁺ = 2-dehydropantoate + NADPH + H⁺" (RHEA:16233, EC 1.1.1.169), and its pathway assignment is "(R)-pantothenate biosynthesis; (R)-pantoate from 3-methyl-2-oxobutanoate: step 2/2."

A global Needleman–Wunsch (BLOSUM62) alignment to *E. coli* PanE (P0A9J4) gives **28.9% overall identity** but shows **exact conservation of the two experimentally defined catalytic residues**: *E. coli* Asn98 → PP_2998 **Asn103**, and *E. coli* Lys176 → PP_2998 **Lys186**. The Rossmann-fold dinucleotide-binding fingerprint (**GxGxxG = GAGALG**) is present at residues 7–12. The moderate global identity paired with perfect conservation of functional residues is the expected signature of a true functional ortholog across the large evolutionary distance separating *Pseudomonas* and *Escherichia*. The catalytic residues correspond to those the *E. coli* structural work implicated: "the essential Lys176 … to bind ketopantoate … the importance of Asn98 for substrate binding and enzyme catalysis" ([PMID: 15966718](https://pubmed.ncbi.nlm.nih.gov/15966718/)).

### Finding 6 — PP_2998 is a monocistronic, cytoplasmic *panE* — not clustered with *panBCD*

Genomic-neighborhood analysis of the KT2440 reference proteome shows PP_2998 is flanked by **functionally unrelated genes** — PP_2997 (CnmA), PP_2996 (transmembrane protein), PP_2995 (FlaR kinase), PP_2999 (glyoxalase family), PP_3000 (MaoC domain), PP_3001 (CaiB/BaiF family), PP_3002 (shikimate dehydrogenase). None are pantothenate-pathway genes, indicating *panE* is **not part of a *pan* operon** — an arrangement that mirrors *E. coli*, where *panE* maps separately from the *panBCD* cluster.

Regarding localization, UniProt lists no subcellular-location annotation, but the biochemistry is unambiguous: the sequence has **no cleavable Sec/Tat signal peptide and no genuine transmembrane helix**. The only Kyte–Doolittle hydropathy window exceeding 1.6 coincides with the buried N-terminal Rossmann-fold GxGxxG motif (GAGALG, residues 7–12), i.e., a βαβ cofactor-binding element rather than a membrane anchor. The characterized *E. coli* ortholog is a soluble cytoplasmic monomer (~34 kDa). PP_2998 is therefore assigned to the **cytoplasm**, where it acts on soluble small-molecule substrates.

### Finding 7 — Full pantothenate pathway reconstructed in KT2440: PanE (PP_2998) is the reductase between PanB (PP_4699) and PanC (PP_4700)

Mapping the pathway partners in KT2440 places PP_2998 precisely in the biosynthetic sequence. **panB = PP_4699** (Q88DW9, 3-methyl-2-oxobutanoate hydroxymethyltransferase / ketopantoate hydroxymethyltransferase) and **panC = PP_4700** (Q88DW8, pantothenate synthetase) are adjacent to one another, whereas **panE = PP_2998** (Q88IK1) is at a distinct locus. The reaction sequence is:

```
3-methyl-2-oxobutanoate (α-ketoisovalerate)
        │  PanB (PP_4699) + 5,10-CH2-THF
        ▼
2-dehydropantoate (ketopantoate)
        │  PanE (PP_2998) + NADPH        ◄── this gene
        ▼
(R)-pantoate
        │  PanC (PP_4700) + β-alanine + ATP
        ▼
(R)-pantothenate  ──►  CoaA/B/C/D/E  ──►  Coenzyme A
```

This pathway is essential in bacteria and absent in humans, making it an actively pursued antibacterial, antitubercular, and antiparasitic drug target. Review literature confirms the framing: "Pantothenate (Pan, vitamin B5) is the precursor for the synthesis of an essential cofactor, coenzyme A (CoA)" ([PMID: 34969059](https://pubmed.ncbi.nlm.nih.gov/34969059/)), and "novel chemical entities with new mechanisms of action are therefore earnestly required" ([PMID: 33384970](https://pubmed.ncbi.nlm.nih.gov/33384970/)).

### Finding 8 — No canonical *panD* annotated in KT2440 — β-alanine likely supplied by an alternative route

Searches of the KT2440 reference proteome (taxId 160488) for *panD*, "aspartate 1-decarboxylase," and "aspartate alpha-decarboxylase" returned **no hits**, whereas *panB* (PP_4699), *panC* (PP_4700), and *panE* (PP_2998) are all clearly annotated. This is consistent with reports that some pseudomonads lack a classical PanD and derive β-alanine from alternative sources (e.g., polyamine/spermidine or pyrimidine/uracil degradation). Critically, this concerns only the **parallel β-alanine branch** feeding PanC and **does not affect the PP_2998/PanE reductase step**, which produces the pantoate moiety. It is noted here to complete the pathway reconstruction, not because it alters the assignment of PP_2998's function.

---

## Mechanistic Model / Interpretation

Synthesizing all eight findings yields a coherent, well-supported model of PP_2998's role.

**Molecular function.** PP_2998 is the *P. putida* KT2440 ketopantoate reductase (PanE, EC 1.1.1.169). It sits at the committed **step 2 of 2** in the conversion of 3-methyl-2-oxobutanoate into pantoate. The enzyme is a soluble, cytoplasmic, monomeric ~34 kDa NADPH-dependent oxidoreductase.

**Catalytic cycle (by orthology to *E. coli*):**

```
         NADPH               ketopantoate                pantoate      NADP+
           │                      │                          │            │
           ▼                      ▼                          ▼            ▼
[E] ──► [E·NADPH] ──► [E·NADPH·ketopantoate] ──► [E·NADP+·pantoate] ──► [E·NADP+] ──► [E]
           └──── ordered binding ────┘   pro-S hydride     └── pantoate released ──┘
                                          transfer to C-2      before NADP+
```

The active site couples a **Rossmann-fold cofactor pocket** (NADPH held via the GxGxxG motif) to a **substrate pocket** formed at the interdomain cleft. A **conformational switch of Lys186** (Lys176 in *E. coli*) is proposed to move the essential lysine into an "active" state that binds and orients ketopantoate, while **Asn103** (Asn98 in *E. coli*) contributes to substrate binding and catalysis. A single ionizable group (pK ≈ 8.4 acid / 7.8 base in the two directions) mediates proton transfer as the pro-S hydride of NADPH is delivered stereospecifically to C-2, generating the R-configured pantoate.

**Comparison of PP_2998 with its characterized *E. coli* ortholog:**

| Property | PP_2998 (*P. putida*, Q88IK1) | *E. coli* PanE (P0A9J4) | Basis |
|---|---|---|---|
| Reaction | ketopantoate + NADPH → (R)-pantoate + NADP⁺ | same | UniProt / PMID 11724562 |
| EC number | 1.1.1.169 | 1.1.1.169 | UniProt |
| Length | 315 aa | ~303 aa | UniProt |
| Catalytic Lys | Lys186 | Lys176 | alignment / PMID 15966718 |
| Substrate-binding Asn | Asn103 | Asn98 | alignment / PMID 15966718 |
| Rossmann motif | GAGALG (res 7–12) | present | sequence analysis |
| Oligomeric state | monomer (inferred) | monomer, ~34 kDa | PMID 11724562 |
| Mechanism | ordered sequential (inferred) | ordered sequential | PMID 10736170 |
| Cofactor preference | NADPH ≫ others (inferred) | NADPH (K_d 0.34 µM) ≫ NADP⁺ (6.5 µM) | PMID 15966718 |
| Localization | cytoplasm | cytoplasm | inference / orthology |
| Gene organization | monocistronic, separate from *panBC* | separate from *panBCD* | genomic analysis |

**Physiological role and redundancy.** The pantoate produced by PanE is the immediate precursor of pantothenate and thence CoA — one of the most central metabolic cofactors. Because CoA is essential, the pantoate step is buffered by a moonlighting activity of IlvC (acetohydroxyacid isomeroreductase), which reduces ketopantoate at ~1/20 the rate it reduces its native substrate. This redundancy explains why *panE* single mutants can retain residual pantoate synthesis, while eliminating PanE still measurably lowers CoA pools and produces conditional phenotypes (e.g., HMP-P/thiamine auxotrophy in *Salmonella*). In *P. putida*, PanE (PP_2998) is spatially and transcriptionally independent of *panB*/*panC* (PP_4699/PP_4700), consistent with the enzyme being a stand-alone metabolic component rather than part of a co-regulated operon.

**Localization and site of action.** All evidence points to the **cytoplasm** as the compartment where PP_2998 functions: it is a soluble globular enzyme with no signal peptide or transmembrane segment, acting on freely diffusing small-molecule metabolites (ketopantoate, NADPH). This is the expected localization for a core intermediary-metabolism biosynthetic enzyme.

---

## Evidence Base

| PMID | Paper (abbrev.) | How it supports the annotation |
|---|---|---|
| [11724562](https://pubmed.ncbi.nlm.nih.gov/11724562/) | *Crystal structure of E. coli ketopantoate reductase at 1.7 Å* (Matak-Vinković et al. 2001) | Defines the reaction/EC, kinetics (K_M/k_cat), monomeric two-domain architecture, and 6-PGDH C-terminal superfamily assignment matching Q88IK1 domains |
| [10736170](https://pubmed.ncbi.nlm.nih.gov/10736170/) | *Kinetic and mechanistic analysis of E. coli panE KPR* (Zheng & Blanchard 2000) | Establishes ordered sequential mechanism and pro-S hydride stereochemistry |
| [14503879](https://pubmed.ncbi.nlm.nih.gov/14503879/) | *Substrate specificity and KIE analysis of E. coli KPR* (Zheng & Blanchard 2003) | Quantifies high specificity for ketopantoate over alternative α-keto acids |
| [15966718](https://pubmed.ncbi.nlm.nih.gov/15966718/) | *E. coli KPR with NADP⁺ bound* (Lobley et al. 2005) | Cofactor thermodynamics and identification of catalytic Lys176 / substrate-binding Asn98 (conserved as Lys186/Asn103) |
| [6401279](https://pubmed.ncbi.nlm.nih.gov/6401279/) | *IlvC in pantothenate biosynthesis in S. typhimurium* (Primerano & Burns 1983) | Genetic proof that *panE* encodes KPR; documents redundant IlvC moonlighting route |
| [29791499](https://pubmed.ncbi.nlm.nih.gov/29791499/) | *CoA–thiamine cross-talk in S. enterica* (Ernst et al. 2018) | Shows PanE loss lowers CoA and causes conditional auxotrophy, tying the enzyme to CoA supply |
| [34969059](https://pubmed.ncbi.nlm.nih.gov/34969059/) | *Pantothenate/CoA in Apicomplexa as drug targets* | Confirms pantothenate is the CoA precursor (pathway context) |
| [33384970](https://pubmed.ncbi.nlm.nih.gov/33384970/) | *Targeting pantothenate/CoA for antituberculosis agents* | Supports the pathway's relevance as a drug-target route |
| [41914741](https://pubmed.ncbi.nlm.nih.gov/41914741/) | *CoA metabolism in fungi as antifungal target* | Broader context on CoA biosynthesis essentiality |

**Nature and strength of evidence.** The reaction, mechanism, structure, and kinetics are supported by **precise, low-throughput experimental studies** (X-ray crystallography, steady-state and pre-steady-state enzyme kinetics, NMR stereochemistry, ITC, genetics) — but all on the *E. coli* and *Salmonella* orthologs, not on the *P. putida* protein itself. The assignment to PP_2998 specifically rests on **bioinformatic inference**: UniProt/InterPro annotation, exact conservation of catalytic residues (Asn103/Lys186) and the Rossmann motif, pathway reconstruction in KT2440, and hydropathy/signal-peptide analysis. The chain of inference is robust because the family is well-defined, the diagnostic residues are conserved, and the pathway is fully reconstructable in the target organism.

---

## Limitations and Knowledge Gaps

1. **No direct experimental data on the *P. putida* protein.** Every kinetic, structural, and mechanistic parameter is transferred by orthology from *E. coli*/*Salmonella*. No purified PP_2998 enzyme assay, crystal structure, or *P. putida panE* knockout has been reported. The functional assignment, while strong, remains an inference.

2. **Moderate global sequence identity (28.9%).** Although the catalytic residues and cofactor motif are conserved, the low overall identity means quantitative parameters (K_M, k_cat, exact substrate promiscuity, cofactor selectivity) could differ from the *E. coli* values.

3. **Localization is inferred, not measured.** The cytoplasmic assignment rests on the absence of targeting signals and orthology, not on experimental fractionation or fluorescence localization in *P. putida*.

4. **β-alanine branch incompletely resolved.** No canonical *panD* was found in KT2440; the actual β-alanine source (polyamine vs. pyrimidine degradation) is not established here. This does not affect PP_2998's assignment but leaves the full pathway context partly open.

5. **Redundancy in *P. putida* untested.** Whether *P. putida* IlvC (or another enzyme) provides a PanE-independent route to pantoate, as in *Salmonella*, has not been verified in this organism.

6. **Regulation unknown.** How *panE* expression is controlled in *P. putida*, and whether the enzyme is subject to feedback by pantothenate/CoA, was not investigated.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant enzymology.** Clone, express, and purify PP_2998; measure K_M(NADPH), K_M(ketopantoate), k_cat, and cofactor selectivity (NADPH vs NADH), and confirm the ordered sequential mechanism and NADPH pro-S stereospecificity. This would convert the orthology-based assignment into direct evidence.

2. **Structural determination.** Solve the crystal or cryo-EM structure of PP_2998 (apo, NADP⁺-bound, and with a ketopantoate/pantoate analog) to verify the Rossmann + C-terminal α-helical two-domain fold and the proposed Lys186 conformational switch.

3. **Genetic knockout and complementation.** Delete *PP_2998* in KT2440 and assay for pantoate/pantothenate auxotrophy and reduced CoA pools; test complementation by *E. coli panE*. Combine with an *ilvC* deletion to probe redundancy of the pantoate step in *P. putida*.

4. **Metabolomic confirmation.** Quantify ketopantoate, pantoate, pantothenate, and CoA in wild-type vs Δ*PP_2998* strains by LC-MS to confirm the metabolic block and any downstream (e.g., thiamine/HMP-P) cross-talk analogous to *Salmonella*.

5. **Resolve the β-alanine branch.** Identify the β-alanine source in KT2440 (test polyamine/spermidine and pyrimidine/uracil degradation routes) to complete the pathway map feeding PanC.

6. **Active-site mutagenesis.** Mutate Lys186 and Asn103 to confirm their catalytic/substrate-binding roles predicted by conservation with *E. coli* Lys176/Asn98.

---

*Report generated from an autonomous multi-iteration investigation (5 iterations; 8 confirmed findings; 9 papers reviewed). All quantitative and mechanistic claims for the enzyme family derive from experimental studies of the E. coli/Salmonella orthologs; assignment to PP_2998 rests on UniProt/InterPro annotation plus sequence, pathway, and localization bioinformatics for P. putida KT2440.*


## Artifacts

- [OpenScientist final report](PP_2998-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PP_2998-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:11724562
2. PMID:6401279
3. PMID:10736170
4. PMID:14503879
5. PMID:15966718
6. PMID:29791499
7. PMID:34969059
8. PMID:33384970