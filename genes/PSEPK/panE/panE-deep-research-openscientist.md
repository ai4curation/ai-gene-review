---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-18T13:27:40.818602'
end_time: '2026-07-18T13:43:28.361062'
duration_seconds: 947.54
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: panE
  gene_symbol: panE
  uniprot_accession: Q88N64
  protein_description: 'RecName: Full=2-dehydropantoate 2-reductase {ECO:0000256|ARBA:ARBA00019465,
    ECO:0000256|RuleBase:RU362068}; EC=1.1.1.169 {ECO:0000256|ARBA:ARBA00013014, ECO:0000256|RuleBase:RU362068};
    AltName: Full=Ketopantoate reductase {ECO:0000256|ARBA:ARBA00032024, ECO:0000256|RuleBase:RU362068};'
  gene_info: Name=panE {ECO:0000313|EMBL:AAN66974.1}; OrderedLocusNames=PP_1351 {ECO:0000313|EMBL:AAN66974.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the ketopantoate reductase family.
  protein_domains: 6-PGluconate_DH-like_C_sf. (IPR008927); 6PGD_dom2. (IPR013328);
    ApbA. (IPR003710); Ketopantoate_reductase. (IPR050838); KPA_reductase. (IPR013752)
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
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: panE-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: panE-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88N64
- **Protein Description:** RecName: Full=2-dehydropantoate 2-reductase {ECO:0000256|ARBA:ARBA00019465, ECO:0000256|RuleBase:RU362068}; EC=1.1.1.169 {ECO:0000256|ARBA:ARBA00013014, ECO:0000256|RuleBase:RU362068}; AltName: Full=Ketopantoate reductase {ECO:0000256|ARBA:ARBA00032024, ECO:0000256|RuleBase:RU362068};
- **Gene Information:** Name=panE {ECO:0000313|EMBL:AAN66974.1}; OrderedLocusNames=PP_1351 {ECO:0000313|EMBL:AAN66974.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the ketopantoate reductase family.
- **Key Domains:** 6-PGluconate_DH-like_C_sf. (IPR008927); 6PGD_dom2. (IPR013328); ApbA. (IPR003710); Ketopantoate_reductase. (IPR050838); KPA_reductase. (IPR013752)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "panE" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'panE' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **panE** (gene ID: panE, UniProt: Q88N64) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: panE (Q88N64), 2-Dehydropantoate 2-Reductase (Ketopantoate Reductase) in *Pseudomonas putida* KT2440

## Gene/Protein Identity Verification

- **UniProt accession:** Q88N64
- **Gene:** *panE* (ordered locus **PP_1351**)
- **Organism:** *Pseudomonas putida* strain ATCC 47054 / DSM 6125 / KT2440 (PSEPK)
- **Enzyme:** 2-dehydropantoate 2-reductase / ketopantoate reductase (KPR), **EC 1.1.1.169**
- **Family:** Ketopantoate reductase family (InterPro IPR050838); ApbA / KPA_reductase (IPR003710, IPR013752); 6-phosphogluconate-dehydrogenase-like C-terminal fold (IPR008927, IPR013328)

**Verification outcome — CONFIRMED.** The gene symbol *panE* is consistent with the UniProt description: *panE* is the canonical bacterial gene symbol for ketopantoate reductase. The reaction (EC 1.1.1.169), the family assignment, and the diagnostic InterPro domains (ApbA/KPA_reductase + 6-PGDH-like C-terminal fold) all coincide with the extensively characterized enzyme class. No conflicting gene of the same symbol was found. There are **no dedicated primary studies of the *P. putida* KT2440 enzyme itself**; this housekeeping biosynthetic gene has instead been characterized in detail in the direct ortholog *Escherichia coli panE* and other bacteria/archaea. The functional narrative below is therefore built on (i) the highly conserved, experimentally characterized ortholog and family, and (ii) UniProt/InterPro domain evidence for Q88N64 specifically. Confidence is high because KPR is mechanistically and structurally well-defined and the domain signatures of Q88N64 match the family precisely.

---

## 1. Summary (Answer to the Research Question)

*panE* (PP_1351, Q88N64) encodes **ketopantoate reductase**, a soluble **cytoplasmic** NADPH-dependent oxidoreductase that catalyzes the **stereospecific reduction of 2-dehydropantoate (ketopantoate) to D-(−)-pantoate** (EC 1.1.1.169). This is the **second committed step of the pantothenate (vitamin B5) biosynthetic pathway**, which supplies pantoate → pantothenate → **coenzyme A (CoA)** and acyl-carrier protein. The enzyme is highly specific for its 2-oxo-acid substrate and for the NADPH cofactor, uses an **ordered sequential mechanism** (NADPH binds first), and relies on a conserved active-site lysine acting as the catalytic general acid. It has no transport, structural, or signaling role; its physiological importance is defined by maintenance of cellular CoA pools.

---

## 2. Primary Function: The Catalyzed Reaction and Substrate Specificity

**Reaction (EC 1.1.1.169):**

> 2-dehydropantoate (ketopantoate) + NADPH + H⁺ → D-pantoate + NADP⁺

Ketopantoate reductase catalyzes the NADPH-dependent reduction of the C-2 keto group of ketopantoate to the corresponding secondary alcohol, producing D-(−)-pantoate [PMID 11724562; 10736170]. The hydride is delivered stereospecifically as the **pro-S hydrogen of NADPH to C-2 of ketopantoate**, generating the D-configured product [PMID 10736170].

**Substrate specificity.** The enzyme is strongly selective for ketopantoate over structurally related 2-oxo-acids: for the *E. coli* ortholog, V and V/K for ketopantoate are 5- and 365-fold higher than for α-ketoisovalerate, and 20- and 648-fold higher than for α-keto-β-methyl-n-valerate. Cofactor specificity is likewise strict — V/K for β-NADPH is 3–500-fold higher than for other pyridine nucleotides, establishing NADPH (not NADH) as the physiological reductant [PMID 14503879].

**Kinetic parameters (E. coli ortholog).** K_M(NADPH) ≈ 20 µM, K_M(ketopantoate) ≈ 60 µM, k_cat ≈ 40 s⁻¹ [PMID 11724562]. Kinetic isotope-effect analysis indicates that hydride transfer is **not** rate-limiting under physiological substrates [PMID 10736170; 14503879].

---

## 3. Catalytic Mechanism

- **Order of binding:** Steady-state initial-velocity and product-inhibition patterns are consistent with an **ordered sequential mechanism**: NADPH binds first, then ketopantoate; pantoate is released before NADP⁺ [PMID 10736170].
- **General acid/base catalysis:** A single ionizable group functions as general acid in the reduction direction (apparent pK_a ≈ 8.4) and general base in the reverse oxidation (pK_a ≈ 7.8) [PMID 10736170]. Site-directed mutagenesis with chemical rescue identified **Lys176** (E. coli numbering) as the catalytic general acid: K176A reduced V_max ~233-fold and was rescued by exogenous primary amines; **Glu256** is also important (E256A, ~42-fold) [PMID 11123955].
- **Substrate recognition / conformational change:** Ternary-complex crystallography (NADP⁺ + pantoate) revealed a hinge-bending closure between the N- and C-terminal domains that switches Lys176 into position to hydrogen-bond the C2-hydroxyl of pantoate; conserved Asn98, Ser244 (and Asn180/Asn194/Asn241) contribute to substrate binding, with Asn98, Lys176 and Glu256 implicated in catalysis [PMID 17229734; 15966718].
- **Cooperativity/oligomeric variation:** *E. coli* KPR is monomeric with a strictly ordered mechanism, whereas some orthologs (e.g., *S. aureus*) are dimeric and display kinetic cooperativity (NADPH-first random pathway) — illustrating mechanistic diversity within the family [PMID 25946571].

---

## 4. Structure and Domain Architecture

The 1.7 Å *E. coli* KPR structure shows a **monomeric ~34 kDa** enzyme with two domains separated by a cleft that forms the active site:
- an **N-terminal Rossmann-fold (αβ)** domain that binds NADPH, and
- a **C-terminal all-α-helical domain** (eight α-helices),
placing KPR in the **6-phosphogluconate-dehydrogenase C-terminal-domain-like superfamily** [PMID 11724562].

For Q88N64 specifically, UniProt/InterPro assign exactly the matching signatures — **ApbA / KPA_reductase (IPR003710, IPR013752)**, **Ketopantoate_reductase (IPR050838)**, and the **6-PGluconate_DH-like C-terminal fold (IPR008927, IPR013328)** — providing independent bioinformatic confirmation that PP_1351 is a genuine KPR rather than a related dehydrogenase. Rule-based classification methods have been developed precisely because the KPR family is embedded in the larger, sequence-diverse 6-PGDH superfamily and must be distinguished from other members [PMID 20876192].

---

## 4b. Sequence-Level Verification of Orthology (P. putida-specific evidence)

To bridge the E. coli characterization to the actual target protein, a global pairwise alignment (Needleman–Wunsch, BLOSUM62) was performed between **Q88N64** (305 aa) and experimentally characterized **E. coli panE/KPR** (UniProt P0A9J4, 303 aa):

- **35.4% sequence identity** over 294 aligned positions — well above the ortholog/twilight threshold and typical for confidently transferable enzyme function.
- **All six functionally validated E. coli residues are conserved** in Q88N64 (a consistent ~+8 numbering offset):

| Role | *E. coli* (P0A9J4) | *P. putida* (Q88N64) |
|------|--------------------|----------------------|
| Cofactor binding | Arg31 | **Arg33** |
| Cofactor binding | Lys72 | **Lys79** |
| Substrate binding / catalysis | Asn98 | **Asn105** |
| **Catalytic general acid** | **Lys176** | **Lys184** |
| Substrate binding | Ser244 | **Ser252** |
| Catalysis | Glu256 | **Glu264** |

- Q88N64 also carries the **N-terminal Rossmann glycine-rich dinucleotide-binding fingerprint** (…ILGAGSLG…, ~res 7–14; cf. E. coli …VLGCGALG…) and the conserved active-site **WRKL…NC…INPLT** motif.

This provides direct, target-specific evidence that PP_1351 is a genuine, mechanistically identical KPR, and identifies **Lys184** as the predicted catalytic general acid in the *P. putida* enzyme. It licenses high-confidence transfer of the E. coli mechanistic/kinetic model to Q88N64 [alignment vs PMID 11123955; 17229734].

## 5. Pathway Context, Biological Process, and Localization

**Pathway.** panE catalyzes the second of four reactions of the bacterial **pantothenate (vitamin B5) biosynthetic pathway** [PMID 18726075]:
1. **PanB** (ketopantoate hydroxymethyltransferase): 2-oxoisovalerate (α-ketoisovalerate) + 5,10-CH₂-THF → **ketopantoate**
2. **PanE** (this enzyme, ketopantoate reductase): **ketopantoate + NADPH → pantoate**
3. **PanD** (aspartate-α-decarboxylase): L-aspartate → β-alanine
4. **PanC** (pantothenate synthetase): **pantoate + β-alanine → pantothenate**

Pantothenate is then phosphorylated and elaborated to **coenzyme A** and the **acyl-carrier protein** 4′-phosphopantetheine prosthetic group. The pathway also intersects branched-chain amino acid (valine) biosynthesis at the shared precursor 2-oxoisovalerate.

**Physiological role.** Loss of PanE reduces the cellular CoA pool: in *Salmonella enterica*, elimination of 2-dehydropantoate 2-reductase both lowers total CoA and produces a conditional thiamine (HMP-P) auxotrophy, directly demonstrating that the enzyme's biosynthetic output governs CoA homeostasis [PMID 29791499]. Consistent with an essential-vitamin route, *panE* disruption confers **pantothenate auxotrophy** in organisms lacking a compensating activity [PMID 23243306; 12948643].

**Enzymatic redundancy (context).** In several bacteria the ketol-acid reductoisomerase **IlvC** moonlights as a second ketopantoate reductase (in *Corynebacterium glutamicum* IlvC is the *only* KPR), and some pathogens (e.g., *Francisella*) use an unrelated KPR, **PanG** [PMID 12948643; 23243306; 25527092]. *P. putida* KT2440 does appear to carry such redundancy — a dedicated *panE* (PP_1351) plus two additional ApbA-family paralogs and a moonlighting IlvC — as detailed in Section 5b.

**Feedback regulation (family context).** In archaea, KPR is the feedback-inhibition target of CoA (CoA competes with the nicotinamide cofactor), whereas in bacteria the primary feedback node is pantothenate kinase; regulatory behavior can therefore differ across lineages [PMID 26757028; 23941541]. This is provided as family context; bacterial *panE* itself is not the canonical bacterial feedback node.

**Subcellular localization.** KPR is a soluble monomeric/oligomeric enzyme with a cytoplasmic Rossmann-fold architecture; it has no signal peptide or transmembrane segments and acts on small soluble metabolites. This was confirmed directly on the **Q88N64 sequence**: Kyte–Doolittle hydropathy analysis (19-aa window) gives a maximum of only **1.23**, below the ~1.6–1.9 transmembrane threshold (no TM helix), and the N-terminus lacks a hydrophobic signal-peptide h-region (mean KD of residues 1–30 = 0.44; one positive charge in the first 20 aa), beginning instead directly with the Rossmann motif. Its function is therefore carried out in the **bacterial cytoplasm**, where CoA/pantothenate biosynthesis occurs [target-specific hydropathy analysis; architecture consistent with PMID 11724562].

## 5b. Genomic Context and Redundancy in P. putida KT2440 (target-specific bioinformatic evidence)

KEGG assigns PP_1351/panE to **KO K00077** (EC 1.1.1.169) within **ppu00770 (Pantothenate and CoA biosynthesis)** and **ppu01240 (Biosynthesis of cofactors)**, confirming the UniProt annotation from an independent database.

**Genomic context.** *panE* lies at complement(1,540,607–1,541,524) and is **monocistronic** — it is *not* part of a pantothenate operon. Its flanking genes are unrelated and divergently oriented: PP_1350 (two-component sensory histidine kinase/response regulator) and PP_1352 (UPF0234 cyclic-di-GMP-binding protein). The rest of the pathway is dispersed across the genome but complete: **panB (PP_4699)** and **panC (PP_4700)** as an adjacent pair, plus the CoA-completing enzymes **coaX/panK (PP_0438)**, **coaD (PP_5123)**, **coaE (PP_0631)**, and the bifunctional **dfp/coaBC (PP_5285)**. This confirms an intact, cytoplasmic pantothenate→CoA network into which PanE feeds pantoate. (β-alanine for PanC can be supplied via the reductive pyrimidine-degradation route pydA/pydB/pydX/hyuC, an alternative to PanD.)

**Potential redundancy.** The KT2440 genome encodes **two additional K00077 paralogs — PP_2325 and PP_2998** (each 315 aa, both bearing the ApbA + ApbA_C ketopantoate-reductase-family Pfam domains) — plus the ketol-acid reductoisomerase **IlvC (PP_4678)**, which is known to moonlight as a ketopantoate reductase [PMID 12948643; 25527092]. Thus *P. putida* may harbor several ketopantoate-reductase activities, so *panE* is likely **not uniquely essential**. Notably, alignment of both paralogs to E. coli panE shows that **PP_2325 (28.8% id) and PP_2998 (29.4% id) also conserve all six catalytic/cofactor residues** (the Rossmann Arg/Lys pair, catalytic Asn, catalytic general-acid Lys, substrate-binding Ser, and catalytic Glu), so they retain intact KPR-like active sites and are plausible functional back-ups. However, these residues are broadly conserved across the ApbA family, and KO/active-site conservation alone does not prove identical substrate specificity; the physiological ketopantoate flux carrier is untested. PP_1351 remains the sequence-verified, canonically designated *panE* and the top ortholog of the characterized E. coli enzyme (35.4% id, highest of the three).

---

## 6. Supported and Refuted Hypotheses

**Supported:**
- H1 — *panE/PP_1351 encodes ketopantoate reductase (EC 1.1.1.169)*: Supported by UniProt/InterPro domain evidence and the fully characterized *E. coli* ortholog [PMID 11724562; 14503879].
- H2 — *The enzyme reduces ketopantoate to D-pantoate using NADPH via an ordered mechanism with a catalytic Lys*: Supported [PMID 10736170; 11123955; 17229734].
- H3 — *panE acts in cytoplasmic pantothenate→CoA biosynthesis and its loss lowers CoA*: Supported [PMID 18726075; 29791499].

**Refuted / excluded:**
- The protein is **not** a transporter, structural protein, or signaling molecule — its fold, catalytic residues, and small-molecule substrate define it as a metabolic oxidoreductase.
- NADH is **not** the physiological cofactor in the bacterial enzyme (NADPH strongly preferred) [PMID 14503879].

---

## 7. Limitations and Future Directions

- **No P. putida KT2440-specific biochemistry or structure** exists; all mechanistic/kinetic parameters are transferred from the *E. coli* ortholog and the KPR family. This transfer is now supported by a direct sequence alignment (35.4% identity; all six catalytic/cofactor residues conserved; predicted catalytic general acid = Lys184), but experimental confirmation in KT2440 is still lacking.
- **Oligomeric state** of the *P. putida* enzyme is unknown (family members range from monomer to dimer).
- **Genetic redundancy** is likely: KT2440 encodes two additional ApbA-family K00077 paralogs (PP_2325, PP_2998) and a moonlighting IlvC (PP_4678). Their contribution to ketopantoate reduction, and the essentiality of *panE*, remain to be tested experimentally (e.g., single vs. combinatorial deletions with CoA-pool/auxotrophy readouts).
- **Future work:** recombinant expression and steady-state kinetics of PP_1351; structural determination or AlphaFold-based active-site mapping to verify Lys/Glu/Asn catalytic residues; gene-deletion auxotrophy/CoA-pool measurements in KT2440.

---

## References (PMIDs)
- 11724562 — Matak-Vinković et al. 2001, *E. coli* KPR crystal structure & kinetics
- 10736170 — Zheng & Blanchard 2000, kinetic/mechanistic analysis of *E. coli* panE-KPR
- 11123955 — Zheng & Blanchard 2000, active-site residues (Lys176) by mutagenesis/chemical rescue
- 14503879 — Zheng & Blanchard 2003, substrate specificity & kinetic isotope effects
- 15966718 — Lobley et al. 2005, KPR·NADP⁺ structure
- 17229734 — Ciulli et al. 2007, ternary complex, substrate recognition & conformational change
- 25946571 — Sanchez et al. 2015, dimeric *S. aureus* KPR & cooperativity
- 20876192 — Mondal et al. 2010, discrimination of KPR within the 6-PGDH superfamily
- 18726075 — Chakauya et al. 2008, four-enzyme pantothenate pathway (panB/panD/panC/panE)
- 29791499 — Ernst et al. 2018, PanE loss lowers CoA / CoA–thiamine cross-talk in *Salmonella*
- 23243306 — Miller et al. 2013, PanG novel KPR; panE/ilvC context; auxotrophy
- 12948643 — Merkamm et al. 2003, IlvC moonlighting as sole KPR in *C. glutamicum*
- 25527092 — Price & Wilson 2014, substrate-ambiguous IlvC replacing KPR in symbiont
- 26757028 / 23941541 — Aikawa et al. 2016 / Tomita et al. 2013, archaeal KPR feedback regulation by CoA


## Artifacts

- [OpenScientist final report](panE-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](panE-deep-research-openscientist_artifacts/final_report.pdf)