---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-17T06:57:20.122872'
end_time: '2026-07-17T07:18:05.491058'
duration_seconds: 1245.37
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: bioD
  gene_symbol: bioD
  uniprot_accession: Q88QW8
  protein_description: 'RecName: Full=ATP-dependent dethiobiotin synthetase BioD {ECO:0000256|HAMAP-Rule:MF_00336};
    EC=6.3.3.3 {ECO:0000256|HAMAP-Rule:MF_00336}; AltName: Full=DTB synthetase {ECO:0000256|HAMAP-Rule:MF_00336};
    Short=DTBS {ECO:0000256|HAMAP-Rule:MF_00336}; AltName: Full=Dethiobiotin synthase
    {ECO:0000256|HAMAP-Rule:MF_00336};'
  gene_info: Name=bioD {ECO:0000256|HAMAP-Rule:MF_00336, ECO:0000313|EMBL:AAN65997.1};
    OrderedLocusNames=PP_0366 {ECO:0000313|EMBL:AAN65997.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the dethiobiotin synthetase family.
  protein_domains: DTB_synth_BioD. (IPR004472); P-loop_NTPase. (IPR027417); AAA_26
    (PF13500)
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
citation_count: 7
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: bioD-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: bioD-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88QW8
- **Protein Description:** RecName: Full=ATP-dependent dethiobiotin synthetase BioD {ECO:0000256|HAMAP-Rule:MF_00336}; EC=6.3.3.3 {ECO:0000256|HAMAP-Rule:MF_00336}; AltName: Full=DTB synthetase {ECO:0000256|HAMAP-Rule:MF_00336}; Short=DTBS {ECO:0000256|HAMAP-Rule:MF_00336}; AltName: Full=Dethiobiotin synthase {ECO:0000256|HAMAP-Rule:MF_00336};
- **Gene Information:** Name=bioD {ECO:0000256|HAMAP-Rule:MF_00336, ECO:0000313|EMBL:AAN65997.1}; OrderedLocusNames=PP_0366 {ECO:0000313|EMBL:AAN65997.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the dethiobiotin synthetase family.
- **Key Domains:** DTB_synth_BioD. (IPR004472); P-loop_NTPase. (IPR027417); AAA_26 (PF13500)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "bioD" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'bioD' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **bioD** (gene ID: bioD, UniProt: Q88QW8) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# bioD (PP_0366, UniProt Q88QW8) in *Pseudomonas putida* KT2440: ATP-Dependent Dethiobiotin Synthetase

**Target:** UniProt **Q88QW8** · Gene **bioD** · Ordered locus **PP_0366**
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / NCIMB 11950 / **KT2440**)
**EC number:** 6.3.3.3 · **Family:** Dethiobiotin synthetase family (Pfam AAA_26 PF13500; InterPro DTB_synth_BioD IPR004472, P-loop_NTPase IPR027417)

## Summary

The gene **bioD** (ordered locus **PP_0366**, UniProt accession **Q88QW8**) of *Pseudomonas putida* KT2440 encodes **ATP-dependent dethiobiotin synthetase (DTBS/DTB synthetase, EC 6.3.3.3)**, a soluble cytoplasmic enzyme that catalyzes the **penultimate step of de novo biotin (vitamin B7) biosynthesis**. The enzyme converts **7,8-diaminopelargonic acid (DAPA, also called 7,8-diaminononanoic acid)** and **CO₂/bicarbonate** into **dethiobiotin (DTB)** in an ATP- and Mg²⁺-dependent reaction, forming the ureido (five-membered urea) ring of the biotin bicyclic scaffold and releasing ADP + inorganic phosphate. Biotin synthase (BioB) then performs the final step — insertion of sulfur to close the thiophane ring and complete biotin.

Mechanistically, dethiobiotin synthetase is one of the best-characterized ATP-dependent carboxylases in structural enzymology. High-resolution crystallographic and kinetic-crystallography studies of the *Escherichia coli* ortholog established that the reaction proceeds via an initial **N7-carbamate** formed from CO₂, which is then phosphorylated by ATP to a **mixed carbamic–phosphoric anhydride** intermediate, followed by intramolecular cyclization to form the ureido ring. Two Mg²⁺ ions bridge the phosphate groups and stabilize the reaction intermediate. The enzyme is a **homodimeric α/β P-loop NTPase** whose composite active site sits at the dimer interface, with DAPA binding one subunit and ATP the other. Nucleotide selectivity is set by a "gate-keeper" asparagine that hydrogen-bonds the adenine base and excludes other NTPs.

Although no biochemical study has been performed on the *P. putida* protein itself, its identity as a functional dethiobiotin synthetase is secure. The Q88QW8 sequence (226 aa) shares **48% identity with the experimentally characterized *E. coli* enzyme**, retains the DTBS-family deviant Walker-A P-loop and family-diagnostic motifs, and carries no signal peptide or transmembrane segment — consistent with a cytoplasmic location. Independently, genome-wide transposon screening in *P. putida* KT2440 recovered biotin auxotrophs, confirming the biotin biosynthetic pathway (of which bioD is a required member) is functional and essential for growth on minimal medium. Because the biotin pathway is absent in humans, DTBS/BioD is a validated antibacterial and antitubercular drug target.

---

## Key Findings

### Finding 1 — bioD is a dethiobiotin synthetase catalyzing the penultimate step of biotin biosynthesis

UniProt annotation of Q88QW8 (via HAMAP-Rule **MF_00336**) assigns the protein to the **dethiobiotin synthetase family** with **EC 6.3.3.3**, carrying the **DTB_synth_BioD** domain (IPR004472). Biochemical and structural studies of orthologs firmly establish the reaction catalyzed: dethiobiotin synthetase performs the **ATP-dependent formation of dethiobiotin from CO₂ and 7,8-diaminopelargonic acid (DAPA)**, the penultimate step of biotin biosynthesis, immediately before biotin synthase (BioB) carries out the final sulfur-insertion step.

Crystallographic work on the *E. coli* enzyme describes "the crystal structures of six complexes of homodimeric *Escherichia coli* dethiobiotin synthetase with a variety of substrates, substrate analogs, and products" ([PMID: 7669756](https://pubmed.ncbi.nlm.nih.gov/7669756/)), confirming DTBS/BioD is a homodimeric enzyme acting on DAPA-derived substrates. More recent work explicitly restates that "**dethiobiotin synthetase (DTBS) catalyzes the penultimate step of biotin biosynthesis**" ([PMID: 34597430](https://pubmed.ncbi.nlm.nih.gov/34597430/)).

Critically for the *P. putida* assignment, a genome-wide mutant screen of KT2440 grown on minimal medium recovered biotin auxotrophs — the study reports that "we also found auxotrophs for biotin, nicotinate and vitamin B12 that were not predicted in silico" ([PMID: 20158506](https://pubmed.ncbi.nlm.nih.gov/20158506/)) — demonstrating that the biotin biosynthetic pathway (which includes bioD/PP_0366) is functional and required for growth of this organism in the absence of exogenous biotin.

### Finding 2 — Reaction mechanism: carbamate formation, ATP-dependent phosphoryl transfer, and cyclization

The catalytic mechanism has been dissected in atomic detail by kinetic crystallography of the *E. coli* enzyme at 1.6–1.9 Å resolution, capturing both the enzyme·MgATP·DAPA complex and a trapped enzyme·MgADP·carbamic-phosphoric-anhydride intermediate. The reaction is initiated when CO₂/bicarbonate reacts with the N7 amino group of DAPA to form a **carbamate**; ATP then phosphorylates this carbamate to yield a **mixed carbamic–phosphoric anhydride**; finally, the second amino group attacks intramolecularly to close the ureido ring, releasing phosphate. The authors state that "**the reaction is initiated by the formation of a carbamate and proceeds through a phosphorylated intermediate, a mixed carbamic phosphoric anhydride**" ([PMID: 9576910](https://pubmed.ncbi.nlm.nih.gov/9576910/)).

Two magnesium ions play an essential catalytic role at the phosphate-transfer center: "**these magnesium ions compensate the negative charges at both phosphate groups after phosphoryl transfer and contribute to the stabilization of the reaction intermediate**" ([PMID: 9576910](https://pubmed.ncbi.nlm.nih.gov/9576910/)). The phosphoryl transfer proceeds with inversion of configuration at phosphorus, consistent with a single in-line attack.

The nucleotide-binding architecture was mapped to a classical mononucleotide fold. The *E. coli* structure places "the phosphate groups close to the **phosphate binding loop Gly8–Thr16** between β-strand β1 and the N-terminus of α-helix α1" ([PMID: 7669756](https://pubmed.ncbi.nlm.nih.gov/7669756/)) — the Walker-A-like P-loop — with divalent-cation coordination provided by Asp54, Thr16, and Glu115.

### Finding 3 — Homodimeric α/β P-loop enzyme with active site at the dimer interface

The 1.80 Å structure of *E. coli* DTBS revealed the enzyme's quaternary organization: each subunit folds as a single globular α/β domain, and the biological unit is a homodimer whose active site straddles the subunit interface. The structural study "establishes that the **enzyme active site is situated at the dimer interface, with the substrate binding to one monomer and ATP to the other**" ([PMID: 7881906](https://pubmed.ncbi.nlm.nih.gov/7881906/)). This composite-active-site architecture explains why the enzyme is obligately dimeric.

The DTBS fold belongs to the diverse **P-loop NTPase superfamily**. The overall fold "closely resembles that of three other enzymes, **adenylosuccinate synthetase (purA), Ha-ras-p21, and nitrogenase iron protein**" ([PMID: 7881906](https://pubmed.ncbi.nlm.nih.gov/7881906/)) — a set of proteins related by fold rather than by detectable sequence similarity (the SIMIBI / adenylosuccinate-synthetase-like clade). DTBS shows no significant sequence similarity to proteins outside its own family. This is fully consistent with the UniProt annotation of Q88QW8, which carries both the **P-loop_NTPase** (IPR027417) and **DTB_synth_BioD** (IPR004472) domain signatures.

### Finding 4 — Position in the cytoplasmic biotin ring-assembly module; ATP-specificity gate-keeper

Biotin biosynthesis is organized into two conceptual stages: (1) synthesis of the **pimelate moiety** (via BioC–BioH in *E. coli* and related γ-proteobacteria) and (2) assembly of the **bicyclic ring** by the sequential action of BioF (KAPA synthase) → BioA (DAPA aminotransferase) → **BioD (DTBS)** → BioB (biotin synthase). A review of the pathway describes how "**a pimelate moiety is synthesized and used to begin assembly of the biotin bicyclic ring structure**" ([PMID: 21437340](https://pubmed.ncbi.nlm.nih.gov/21437340/)). BioD performs the ring-closure carboxylation that generates the ureido ring — notably a *non*-biotin-dependent carboxylation, distinguishing it from the biotin-dependent carboxylases downstream in metabolism.

Nucleotide specificity across the family is governed by a small number of C-terminal residues. In the *E. coli*-type enzyme, "**mutational analysis performed alongside in silico experiments revealed a gate-keeper role for Asn175 in *Escherichia coli* DTBS that excludes binding of other nucleotide triphosphates**" ([PMID: 25801336](https://pubmed.ncbi.nlm.nih.gov/25801336/)), conferring ATP preference. Interestingly, the *Mycobacterium tuberculosis* enzyme lacks this residue and shows broad NTP promiscuity with highest affinity for CTP — illustrating that nucleotide recognition, not the core chemistry, is the most variable feature among orthologs.

The pathway's absence in humans makes the enzyme a clean drug target: "**due to its importance in bacterial pathogenesis, and the absence of a human homologue, DTBS is a promising target for the development of new antibacterials**" ([PMID: 25801336](https://pubmed.ncbi.nlm.nih.gov/25801336/)).

### Finding 5 — The *P. putida* sequence carries the DTBS-family deviant Walker-A P-loop

The Q88QW8 sequence retrieved from UniProt is **226 residues** long and begins `MSQAFFIAGTDTDVGKTTIAAGLLH…`. This N-terminal region contains the dethiobiotin-synthetase **deviant Walker-A phosphate-binding loop** (`G-x-x-x-x-GKTT`), with the diagnostic `GKTT` at approximately residues 15–18. This directly corresponds to the *E. coli* DTBS Gly8–Thr16 P-loop identified crystallographically ([PMID: 7669756](https://pubmed.ncbi.nlm.nih.gov/7669756/)). The overall protein length (~226 aa) is typical of monofunctional bacterial dethiobiotin synthetases (the *E. coli* enzyme is 225 aa). This sequence-level evidence links the *P. putida* ortholog directly to the experimentally characterized enzyme family, rather than relying solely on automated database annotation transfer.

### Finding 6 — 48% sequence identity to experimentally characterized *E. coli* DTBS

A global pairwise alignment (Needleman–Wunsch) of *P. putida* BioD (Q88QW8, 226 aa) against *E. coli* BioD (UniProt P13000, 225 aa) yields **48.2% identity over 222 aligned columns (107/222 identical residues)**. Both proteins retain the DTBS deviant Walker-A P-loop (*P. putida* `GTDTDVGKTT` vs *E. coli* `GTDTEVGKTV`) and the family-diagnostic motifs `EGAGGW` (*P. putida* `IEGAGGWRVP`; *E. coli* `VEGAGGWFTP`) and the `ILVVGV(K/R)LGCI` nucleotide/catalytic loop.

This level of identity is far above the ~30% threshold generally taken to indicate conserved three-dimensional structure and function, establishing **unambiguous orthology** between the *P. putida* enzyme and the reference enzyme whose structure and carbamate/anhydride mechanism were determined crystallographically ([PMID: 7669756](https://pubmed.ncbi.nlm.nih.gov/7669756/), [PMID: 9576910](https://pubmed.ncbi.nlm.nih.gov/9576910/)). Function, mechanism, and structural fold can therefore be confidently transferred to Q88QW8.

### Finding 7 — Sequence-based localization: cytoplasmic, no signal peptide

Kyte–Doolittle hydropathy analysis of Q88QW8 (226 aa) shows the N-terminal 30-residue mean hydropathy is **0.42** — there is no hydrophobic signal-peptide h-region and no Sec/Tat export signal. The overall grand average of hydropathy (GRAVY) is **0.283**. Internal hydrophobic windows (the strongest being a 19-residue peak hydropathy of 1.95 near residue 136, within the conserved `ILVVGVRLGCISHALL` catalytic-core loop) map to **buried β-strands of the globular α/β P-loop fold**, not to transmembrane helices. This is fully consistent with the experimentally determined **soluble, cytosolic, homodimeric** structures of DTBS orthologs, in which "**the protein forms a homodimer with each subunit folded as a single globular alpha/beta domain**" ([PMID: 7881906](https://pubmed.ncbi.nlm.nih.gov/7881906/)), and with the established fact that de novo biotin ring assembly occurs in the bacterial cytoplasm.

---

## Mechanistic Model / Interpretation

### Position of BioD in the biotin biosynthetic pathway

```
   PIMELATE-MOIETY STAGE                RING-ASSEMBLY STAGE (cytoplasm)
 ┌─────────────────────────┐   ┌───────────────────────────────────────────────┐
 (BioC → ... → BioH)  →  pimeloyl-ACP  →  BioF   →   BioA    →  ┌────────┐ →  BioB  → BIOTIN
                                       (KAPA      (DAPA       │  BioD  │   (biotin
                                        synthase)  amino-      │ DTBS   │    synthase,
                                                   transferase)│ EC     │    S insertion)
                                                               │6.3.3.3 │
                                                               └────────┘
                                          KAPA → DAPA ────────────►  DETHIOBIOTIN

   BioD-catalyzed reaction:
     DAPA + CO2 + ATP  --(Mg2+)-->  dethiobiotin + ADP + Pi + H2O
```

### The BioD chemical mechanism, step by step

```
 1. Carbamate formation:
      DAPA-N7-NH2  +  CO2   ->   DAPA-N7-NH-COO-   (carbamate)

 2. ATP-dependent phosphorylation (Mg2+-assisted):
      carbamate-COO-  +  ATP  ->  mixed carbamic-phosphoric anhydride  +  ADP
      (two Mg2+ ions bridge phosphates, stabilize the intermediate;
       phosphoryl transfer occurs with inversion at P)

 3. Intramolecular cyclization (ring closure):
      N8 amino group attacks the anhydride carbon
      ->  UREIDO RING closes  ->  DETHIOBIOTIN  +  Pi
```

### Structural logic

BioD is an obligate **homodimer**. Its P-loop NTPase fold (shared with adenylosuccinate synthetase, Ras, and nitrogenase Fe-protein) binds and orients MgATP through the Walker-A/deviant P-loop (`GKTT`), while the second, adjacent subunit contributes residues that bind DAPA — placing the composite catalytic machinery at the **dimer interface**. This explains three otherwise-independent observations: (i) the requirement for dimerization; (ii) the strict Mg²⁺ dependence for phosphoryl transfer; and (iii) the concentration of species-variable residues in C-terminal nucleotide-recognition loops (the gate-keeper Asn and adjacent motifs), which tune nucleotide specificity without altering the conserved DAPA-carboxylation chemistry.

### Confidence in the *P. putida* assignment

| Line of evidence | Result | Interpretation |
|---|---|---|
| UniProt/HAMAP annotation | EC 6.3.3.3, DTB_synth_BioD (IPR004472) | Family & EC assignment |
| Domain content | P-loop_NTPase (IPR027417) + DTB_synth_BioD | Correct fold + family |
| Sequence identity to *E. coli* BioD | 48.2% over 222 aa | Unambiguous orthology |
| Conserved motifs | Deviant Walker-A `GKTT`, `EGAGGW`, `ILVVGV(K/R)LGCI` | Catalytic machinery intact |
| Signal-peptide / TM analysis | None (N-term hydropathy 0.42; GRAVY 0.283) | Cytoplasmic |
| Pathway genetics in KT2440 | Biotin auxotrophs recovered | Pathway functional & required |

All independent lines converge: PP_0366/Q88QW8 is a functional, cytoplasmic dethiobiotin synthetase.

---

## Evidence Base

| PMID | Title (abbrev.) | Organism | How it supports the findings |
|---|---|---|---|
| [7669756](https://pubmed.ncbi.nlm.nih.gov/7669756/) | *Mechanism of an ATP-dependent carboxylase (DTBS)…* | *E. coli* | Six substrate/product/analog complexes; defines homodimer, P-loop (Gly8–Thr16), metal site; reference enzyme for orthology |
| [9576910](https://pubmed.ncbi.nlm.nih.gov/9576910/) | *Snapshot of a phosphorylated substrate intermediate…* | *E. coli* | Kinetic crystallography traps carbamate + mixed carbamic-phosphoric anhydride; establishes 2-Mg²⁺ mechanism |
| [7881906](https://pubmed.ncbi.nlm.nih.gov/7881906/) | *Mechanistic implications and family relationships…* | *E. coli* | 1.80 Å structure; active site at dimer interface; fold homology to PurA/Ras/nitrogenase; globular α/β (cytosolic) |
| [21437340](https://pubmed.ncbi.nlm.nih.gov/21437340/) | *Closing in on complete pathways of biotin biosynthesis* | Review | Two-stage pathway; places BioD in ring-assembly module |
| [25801336](https://pubmed.ncbi.nlm.nih.gov/25801336/) | *Nucleotide triphosphate promiscuity in MtDTBS* | *M. tuberculosis* / *E. coli* | Gate-keeper Asn175 confers ATP specificity; DTBS as drug target (no human homolog) |
| [34597430](https://pubmed.ncbi.nlm.nih.gov/34597430/) | *A conserved…E. coli biotin biosynthesis gene…* | *E. coli* | Restates DTBS catalyzes the penultimate step |
| [20158506](https://pubmed.ncbi.nlm.nih.gov/20158506/) | *Conditionally essential genes…P. putida KT2440* | *P. putida* KT2440 | Biotin auxotrophs recovered — pathway functional/required in the target organism |
| [22284390](https://pubmed.ncbi.nlm.nih.gov/22284390/) | *Structural characterization of H. pylori DTBS…* | *H. pylori* | Confirms family breadth; C-terminal nucleotide-recognition regions differ across species |
| [22547782](https://pubmed.ncbi.nlm.nih.gov/22547782/) | *Bifunctional DTBS–DAPA-AT (Arabidopsis)…* | *A. thaliana* | Eukaryotic BioD–BioA fusion; substrate channeling; contrasts with bacterial monofunctional BioD |
| [30289406](https://pubmed.ncbi.nlm.nih.gov/30289406/) | *Precipitant-ligand exchange…MtDTBS ADP…* | *M. tuberculosis* | ADP-bound structure; supports inhibitor/drug-target program |

**Consistency of the evidence.** All primary structural/mechanistic papers agree on the core chemistry (carbamate → anhydride → cyclization), the homodimeric P-loop architecture, and the cytosolic nature of the enzyme. The principal *inter-species variation* is in nucleotide recognition (E. coli ATP-specific gate-keeper Asn vs. Mtb NTP promiscuity vs. H. pylori's unusual single-motif GTPase-like site with ATP preference). Because the *P. putida* sequence retains the *E. coli*-type C-terminal motifs, ATP specificity is the most parsimonious expectation for Q88QW8. No paper contradicts the assignment of PP_0366 as dethiobiotin synthetase.

---

## Limitations and Knowledge Gaps

1. **No direct biochemistry on the *P. putida* protein.** All kinetic and structural data derive from orthologs (*E. coli*, *M. tuberculosis*, *H. pylori*, *A. thaliana*). The function, mechanism, and localization for Q88QW8 are inferred from strong sequence/domain homology (48% identity to *E. coli*), not measured directly. No purified-enzyme assay, K_m, k_cat, or crystal structure exists for PP_0366.

2. **Nucleotide specificity not experimentally confirmed for Q88QW8.** While the sequence retains *E. coli*-type C-terminal motifs, the specific gate-keeper residue and any NTP promiscuity have not been tested in the *P. putida* enzyme.

3. **Localization is bioinformatic.** The cytoplasmic assignment rests on the absence of a signal peptide/TM segment and on the soluble nature of orthologous structures — no experimental fractionation or microscopy has localized the *P. putida* protein.

4. **Gene-level essentiality is indirect.** The KT2440 mutant screen recovered biotin auxotrophs but did not, in the material reviewed here, pin the phenotype specifically to PP_0366 versus other biotin genes; essentiality of bioD is inferred from pathway logic.

5. **Pathway upstream context in *P. putida* not detailed here.** The exact route to the pimelate moiety and DAPA (BioC/BioH/BioF/BioA homologs) in *P. putida* was not fully mapped in this investigation, though the presence of biotin auxotrophy implies a complete pathway.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant expression and enzyme assay.** Clone PP_0366, express and purify the His-tagged protein, and measure DTBS activity (DAPA + CO₂/HCO₃⁻ + ATP → dethiobiotin) by coupled ADP/Pi release or LC-MS detection of dethiobiotin. Determine K_m for DAPA and ATP, k_cat, and Mg²⁺ dependence.

2. **Nucleotide-specificity profiling.** Test ATP vs. GTP/CTP/UTP to confirm the predicted ATP preference and identify the gate-keeper residue by site-directed mutagenesis (analogous to *E. coli* Asn175 / Mtb promiscuity studies).

3. **Structural determination.** Solve the crystal structure (or refine an AlphaFold model against the *E. coli* template) of the *P. putida* enzyme, ideally with MgADP and a DAPA analog, to verify the dimer-interface active site and P-loop geometry.

4. **Targeted genetics in KT2440.** Construct a clean ΔPP_0366 deletion and confirm biotin auxotrophy (growth rescue by exogenous biotin or dethiobiotin), formally establishing gene–phenotype linkage and pathway position (rescue by dethiobiotin but *not* by DAPA would confirm BioD acts on DAPA to make DTB).

5. **Localization confirmation.** Cytoplasmic localization could be verified by cell fractionation or a fluorescent-protein fusion.

6. **Inhibitor cross-evaluation.** Given DTBS's validated drug-target status, test whether inhibitors developed against *M. tuberculosis*/*E. coli* DTBS also inhibit the *P. putida* enzyme, informing broad-spectrum antibacterial potential.

---

## Conclusion

**bioD / PP_0366 / Q88QW8** encodes **ATP-dependent dethiobiotin synthetase (DTBS, EC 6.3.3.3)**, a soluble, cytoplasmic, homodimeric P-loop enzyme that catalyzes the **penultimate step of de novo biotin biosynthesis**: the Mg²⁺/ATP-dependent carboxylation and ureido-ring closure of 7,8-diaminopelargonic acid (DAPA) with CO₂ to form dethiobiotin, releasing ADP + Pi. It acts immediately downstream of the aminotransferase BioA and upstream of biotin synthase BioB in the cytoplasmic biotin-ring-assembly module. The reaction proceeds via an N7-carbamate and a mixed carbamic–phosphoric anhydride intermediate stabilized by two Mg²⁺ ions, with the composite active site formed at the dimer interface. Direct experimental characterization exists for orthologs (*E. coli*, *M. tuberculosis*, *H. pylori*, *Arabidopsis*); the *P. putida* assignment is supported by 48% sequence identity to *E. coli* DTBS, conserved DTBS domains and the diagnostic Walker-A P-loop in its 226-aa sequence, the absence of any export signal, and the biotin auxotrophy of pathway mutants in KT2440.


## Artifacts

- [OpenScientist final report](bioD-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](bioD-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:7669756
2. PMID:34597430
3. PMID:20158506
4. PMID:9576910
5. PMID:7881906
6. PMID:21437340
7. PMID:25801336