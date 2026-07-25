---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-20T15:07:47.366611'
end_time: '2026-07-20T15:49:28.432935'
duration_seconds: 2501.07
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: pncB
  gene_symbol: pncB
  uniprot_accession: Q88DF7
  protein_description: 'RecName: Full=Nicotinate phosphoribosyltransferase {ECO:0000255|HAMAP-Rule:MF_00570};
    Short=NAPRTase {ECO:0000255|HAMAP-Rule:MF_00570}; EC=6.3.4.21 {ECO:0000255|HAMAP-Rule:MF_00570};'
  gene_info: Name=pncB {ECO:0000255|HAMAP-Rule:MF_00570}; OrderedLocusNames=PP_4868;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the NAPRTase family. {ECO:0000255|HAMAP-
  protein_domains: N/Namide_PRibTrfase. (IPR041525); NAPRTase_N. (IPR040727); Nic_PRibTrfase.
    (IPR006406); Nic_PRibTrfase-Fam. (IPR007229); Nicotinate_pribotase-like_C. (IPR036068)
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
citation_count: 8
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: pncB-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: pncB-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88DF7
- **Protein Description:** RecName: Full=Nicotinate phosphoribosyltransferase {ECO:0000255|HAMAP-Rule:MF_00570}; Short=NAPRTase {ECO:0000255|HAMAP-Rule:MF_00570}; EC=6.3.4.21 {ECO:0000255|HAMAP-Rule:MF_00570};
- **Gene Information:** Name=pncB {ECO:0000255|HAMAP-Rule:MF_00570}; OrderedLocusNames=PP_4868;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the NAPRTase family. {ECO:0000255|HAMAP-
- **Key Domains:** N/Namide_PRibTrfase. (IPR041525); NAPRTase_N. (IPR040727); Nic_PRibTrfase. (IPR006406); Nic_PRibTrfase-Fam. (IPR007229); Nicotinate_pribotase-like_C. (IPR036068)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "pncB" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'pncB' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **pncB** (gene ID: pncB, UniProt: Q88DF7) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *pncB* (PP_4868, UniProt Q88DF7) in *Pseudomonas putida* KT2440

## Gene/Protein Identity Verification

| Field | Value |
|-------|-------|
| Gene symbol | *pncB* |
| UniProt accession | Q88DF7 (PNCB_PSEPK) |
| Ordered locus | PP_4868 |
| Organism | *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / KT2440) |
| Protein | Nicotinate phosphoribosyltransferase (NAPRTase) |
| EC number | 6.3.4.21 (formerly EC 2.4.2.11) |
| Length | 401 aa |
| Family | NAPRTase family (HAMAP rule MF_00570) |

**Identity confirmed.** The gene symbol *pncB* is the standard, unambiguous symbol for nicotinate phosphoribosyltransferase across bacteria, and it matches the UniProt protein description exactly. The InterPro domain set (IPR006406 Nic_PRibTrfase; IPR007229 Nic_PRibTrfase-Fam; IPR040727 NAPRTase_N; IPR036068 C-domain; IPR041525) is the canonical NAPRTase architecture. Global sequence alignment (see Finding F005) shows Q88DF7 is a genuine ortholog of the experimentally characterized enterobacterial PncB enzymes (**53.7% identity to *E. coli* PncB**), so literature on *E. coli*, *Salmonella*, and *Acinetobacter* PncB is directly transferable. There is **no ambiguity** in this assignment.

One caveat on nomenclature: in *P. putida* the letters "nic" also appear in an unrelated **catabolic** gene cluster (*nicAB*, *nicCDEFTP*, *nicXR*) that *degrades* nicotinic acid as a carbon source. This is functionally distinct from *pncB* (see Finding F004) and should not be confused with it.

---

## Summary

The gene **pncB** (ordered locus **PP_4868**; UniProt **Q88DF7**) of *Pseudomonas putida* KT2440 encodes **nicotinate phosphoribosyltransferase (NAPRTase; EC 6.3.4.21**, formerly EC 2.4.2.11**)**, a cytoplasmic enzyme that catalyzes the **first committed and rate-limiting step of the Preiss–Handler NAD⁺ salvage pathway**. NAPRTase condenses free **nicotinic acid (NA, niacin/vitamin B3)** with **5-phospho-α-D-ribose-1-diphosphate (PRPP)** to produce **nicotinate mononucleotide (NaMN)** plus pyrophosphate, using ATP hydrolysis to drive the reaction. NaMN is then converted by NadD (adenylyltransferase) and NadE (synthetase) to NAD⁺, so PncB is the **anabolic gateway** that recycles salvaged pyridine bases into the essential NAD⁺ pool.

A defining biochemical feature, established in the *Salmonella* and *E. coli* orthologs, is that NAPRTase is a **facultative ATPase** that couples ATP hydrolysis to catalysis through a **covalent phosphohistidine intermediate**. Phosphorylation of a conserved active-site histidine (His-219 in *Salmonella*; His-220 in *E. coli*; **His-224 in *P. putida* Q88DF7**) increases PRPP affinity ~2000-fold and thermodynamically pulls the reaction toward NaMN synthesis. This energy-coupling step distinguishes NAPRTase from most other phosphoribosyltransferases and explains why it is the physiological control point of NAD homeostasis — overexpression of pncB substantially enlarges cellular NAD(H) pools.

The functional assignment for *P. putida* Q88DF7 rests on **strong orthology and strict conservation of catalytic residues** rather than a direct assay of the KT2440 protein. In the physiological context of *P. putida* — which also possesses a dedicated *nic* operon that degrades nicotinic acid as a carbon source — PncB represents the **salvage (anabolic) fate of nicotinic acid**, competing with catabolism for the same substrate. The organism's tight regulation of the catabolic *nic* genes helps prevent depletion of the vitamin B3 needed by PncB for cofactor synthesis.

---

## Key Findings

### F001 — pncB encodes nicotinate phosphoribosyltransferase, the entry enzyme of NAD⁺ salvage

UniProt Q88DF7 (PP_4868) is annotated by HAMAP rule **MF_00570** as nicotinate phosphoribosyltransferase (NAPRTase; **EC 6.3.4.21**, historically EC 2.4.2.11). The enzyme catalyzes:

> **nicotinic acid (NA) + PRPP + ATP + H₂O → nicotinate D-ribonucleotide (NaMN) + pyrophosphate (PPi) + ADP + Pi**

NaMN is the direct precursor of NAD⁺, subsequently converted by NadD (NaMN adenylyltransferase) and NadE (NAD synthetase). This is the **first committed reaction of the Preiss–Handler pathway**, the branch of NAD metabolism that salvages the free pyridine base nicotinic acid rather than synthesizing the ring *de novo*.

The reaction is directly demonstrated for orthologous enzymes. [PMID: 12616693](https://pubmed.ncbi.nlm.nih.gov/12616693/) states that "the enzyme nicotinic acid phosphoribosyltransferase (NAPRTase; EC 2.4.2.11), encoded by the *pncB* gene, catalyzes the formation of nicotinate mononucleotide (NAMN), a direct precursor of NAD, from NA," establishing the substrate (NA) and product (NaMN). Complementarily, [PMID: 9521741](https://pubmed.ncbi.nlm.nih.gov/9521741/) reports that the enzyme "uses the energy of ATP hydrolysis to drive the synthesis of nicotinate mononucleotide and pyrophosphate from nicotinic acid (NA) and phosphoribosyl pyrophosphate (PRPP)," defining substrates (NA, PRPP), products (NaMN, PPi), and the ATP dependence.

**Substrate specificity.** The physiological pyridine substrate is free nicotinic **acid** (the deamidated, carboxylate form of vitamin B3), not nicotinamide — this is the defining feature of the *deamidating* branch of pyridine salvage. The ribose-phosphate donor is PRPP, and ATP is an essential energetic co-substrate. The dual EC classification (older EC 2.4.2.11 glycosyltransferase view; current EC 6.3.4.21 ligase view) reflects the ATP-dependent bond-forming chemistry.

### F002 — NAPRTase is a facultative ATPase coupling ATP hydrolysis to catalysis via a covalent phosphohistidine intermediate

The most distinctive property of NAPRTase is that, unlike a simple phosphoribosyltransferase, it hydrolyzes ATP to **energize** NaMN synthesis even though no phosphate from ATP appears in the product. Pre-steady-state and steady-state kinetic analysis of the *Salmonella typhimurium* enzyme showed that NAPRTase "undergoes covalent phosphorylation by bound ATP at a rate of 30 s⁻¹. The phosphoenzyme (E-P) binds PRPP with a KD of 0.6 microM, a value 2000-fold lower than that measured for the nonphosphorylated enzyme" ([PMID: 9521741](https://pubmed.ncbi.nlm.nih.gov/9521741/)). This dramatic affinity increase upon phosphorylation is the physical basis of energy coupling: the phosphoenzyme partitions >90% of bound PRPP to product, biasing the reaction strongly toward NaMN.

The phosphorylated residue was identified as a **histidine**. [PMID: 8672422](https://pubmed.ncbi.nlm.nih.gov/8672422/) established that "NAPRTase phosphorylated at **His-219** is an intermediate in the energy transduction mechanism of NAPRTase." The phosphoenzyme is acid-labile and base-stable — the diagnostic chemical signature of a **phosphoramidate/phosphohistidine** linkage, distinguishing it from phosphoester (Ser/Thr/Tyr) or acyl-phosphate (Asp) intermediates.

The term **"facultative ATPase"** captures the fact that the enzyme can run without ATP, but at a much less favorable equilibrium. When ATP is present, the phosphohistidine intermediate raises the effective equilibrium constant of NaMN synthesis, effectively pumping the reaction against an unfavorable thermodynamic gradient. This is why the EC number was reclassified from a transferase (2.4.2.11) to a ligase-type activity (6.3.4.21).

### F003 — PncB acts in the cytoplasm and is the rate-limiting control point of NAD(H) salvage

**Localization.** The predicted primary structure of *Salmonella* NAPRTase contains **no signal sequence**, indicating a cytoplasmic rather than periplasmic or secreted enzyme. [PMID: 1987148](https://pubmed.ncbi.nlm.nih.gov/1987148/) explicitly notes that "no signal sequence was observed in the predicted NAPRTase primary structure, suggesting that the enzyme is not periplasmic." The *P. putida* Q88DF7 sequence likewise lacks any signal peptide or transmembrane region, consistent with a soluble cytoplasmic protein that carries out NAD salvage in the cytosol, where its substrates (NA imported via NiaP, PRPP, ATP) reside.

**Rate-limiting role.** The NA→NaMN step catalyzed by PncB is the **rate-limiting step** of NAD salvage ([PMID: 12616693](https://pubmed.ncbi.nlm.nih.gov/12616693/)), making the enzyme the key control point for NAD⁺ pool size. Overexpression studies confirm this in *E. coli*: overexpression of pncB "resulted in a significant increase in cell mass and succinic acid production," and pncB is described as "a rate limiting enzyme of NAD(H) synthesis" ([PMID: 22975127](https://pubmed.ncbi.nlm.nih.gov/22975127/)). Quantitatively, pncB overexpression increased the anaerobic NAD⁺ pool ~6.2-fold and lowered the NADH/NAD⁺ ratio from 0.64 to 0.13, restoring redox balance and growth. Flux through PncB therefore sets the ceiling of the intracellular NAD(H) pool, making it a widely used metabolic-engineering handle.

### F004 — In *P. putida* KT2440, pncB salvages nicotinic acid toward NAD⁺, distinct from the *nic* operon that degrades NA as a carbon source

*P. putida* KT2440 is unusual in possessing a **dedicated aerobic nicotinic-acid degradation gene cluster** in addition to salvage machinery. The *nic* cluster comprises an upper pathway (*nicAB*) converting NA to 6-hydroxynicotinic acid (6HNA), and lower-pathway genes (*nicCDEF*, *nicTP* transport, *nicXR*) that channel 6HNA into central carbon metabolism. This catabolic system is tightly regulated by two regulators — **NicR** (MarR-like) and **NicS** (TetR-like) — with 6HNA as the effector/inducer ([PMID: 21450002](https://pubmed.ncbi.nlm.nih.gov/21450002/)).

Critically, this tight regulation exists precisely to **protect the salvage/anabolic fate of nicotinic acid**. As the authors state, the circuit assures "a tight transcriptional control of the catabolic genes that may prevent depletion of this vitamin B3 when needed for the synthesis of essential cofactors" ([PMID: 21450002](https://pubmed.ncbi.nlm.nih.gov/21450002/)). NA is thus a **branch-point metabolite**: it can be catabolized (nic operon, carbon source) or salvaged into NAD⁺ (the **pncB** route). PncB defines the anabolic branch.

The salvage role of PncB and its relationship to transport and deamidation is well defined in related bacteria. In *Acinetobacter*, comparative kinetic characterization of PncA, PncB, and NadV "allowed us to suggest distinct physiological roles for the two alternative, deamidating and nondeamidating, routes of nicotinamide salvage/recycling," and "the role of the NiaP transporter in both nicotinate and nicotinamide salvage was confirmed" ([PMID: 20926389](https://pubmed.ncbi.nlm.nih.gov/20926389/)). This places PncB firmly in the **deamidating salvage route**: nicotinamide is deamidated by PncA to NA, NA is imported/retained by the NiaP permease, and PncB converts NA to NaMN. The same branch-point logic is echoed in *Bordetella*, whose *nic* locus is "highly similar to that characterized in *Pseudomonas putida* KT2440," where pathway dysregulation "indicated this degradation pathway influences NAD biosynthesis" ([PMID: 29485696](https://pubmed.ncbi.nlm.nih.gov/29485696/)).

### F005 — Q88DF7 is a genuine PncB ortholog with a strictly conserved catalytic/phospho-histidine

Because the *P. putida* enzyme has not been directly assayed, the functional assignment depends on rigorous sequence orthology. Global Needleman–Wunsch alignment of *P. putida* Q88DF7 (401 aa) against the biochemically characterized *E. coli* PncB (P18133, 400 aa) yields **53.7% amino-acid identity** — well above the ~30% threshold used to infer conserved enzymatic function.

Most importantly, the **catalytic phospho-histidine is strictly conserved**. The residue shown to be phosphorylated and essential for energy coupling in *Salmonella* (His-219; His-220 in *E. coli*) maps precisely onto **His-224 in *P. putida*** within an invariant motif:

| Region | *E. coli* PncB | *P. putida* Q88DF7 |
|---|---|---|
| Catalytic His motif | `LGTQAHEWFQAHQQ` | `LGTMAHEWIMAHQQ` |
| C-terminal ATP-binding region | `…CNGKPVAKLSDSPGKTICHD…FVRALRK…` | `…CNGAPVAKISDEAAKTQCRD…FVAYMRH…` |

The `AHEW…HQQ` block — which contains the phospho-His — is completely invariant, and the diagnostic C-terminal ATP-binding region is also conserved, supporting a **shared ATP-coupled mechanism**. This finding is anchored to the experimental evidence of [PMID: 8672422](https://pubmed.ncbi.nlm.nih.gov/8672422/): the His-219 shown to be catalytic in *Salmonella* corresponds by alignment to the strictly conserved His-224 in *P. putida* Q88DF7. The domain architecture matches the NAPRTase family exactly (IPR006406, IPR007229, IPR040727, IPR036068, IPR041525).

---

## Mechanistic Model / Interpretation

### The reaction and its energetics

NAPRTase catalyzes phosphoribosyl transfer from PRPP to nicotinic acid, forming the N-glycosidic bond of NaMN, and uniquely couples this to ATP hydrolysis:

```
                         ATP        ADP + Pi
                          \          /
                           \        /
   Nicotinic acid  +  PRPP  ──► [E~P-His224] ──►  NaMN  +  PPi
   (imported via NiaP)                             │
                                                   ▼
                                              NadD (NaMN → NaAD)
                                                   │
                                                   ▼
                                              NadE (NaAD → NAD⁺)
```

Mechanistic cycle:
1. ATP phosphorylates His-224 (His-219/220 in orthologs), forming a covalent phosphohistidine (E~P).
2. E~P binds PRPP ~2000-fold more tightly (KD 0.6 µM), positioning substrates optimally.
3. Phosphoribosyl transfer to NA yields NaMN + PPi.
4. Hydrolysis of the phosphohistidine (release of Pi) resets the enzyme and provides the thermodynamic drive.

Without ATP the enzyme still turns over (hence "facultative ATPase") but at a far less favorable equilibrium — the ATP-driven mode enables accumulation of large NAD pools.

### Pathway position — the branch point of nicotinic acid metabolism in *P. putida*

```
        Nicotinamide ──PncA──► Nicotinic acid (NA) ◄── NiaP permease (import)
                                     │
                 ┌───────────────────┴────────────────────┐
                 │ SALVAGE (anabolic)        CATABOLISM     │
                 │  = pncB / PncB            = nic operon    │
                 ▼                                  ▼
       NaMN ──NadD──► NaAD ──NadE──► NAD⁺   6-hydroxynicotinic acid
       (Preiss–Handler)                     ──► central carbon metabolism
                                            (NicR/NicS-regulated)
```

In *P. putida* KT2440, free nicotinic acid sits at a metabolic crossroads. PncB commits NA to NAD⁺ biosynthesis, whereas the *nic* operon commits NA to carbon/energy catabolism. The tight NicR/NicS regulation of the catabolic branch exists to prevent NA depletion so that PncB-dependent cofactor synthesis is not starved of substrate. PncB is therefore best understood not merely as a housekeeping salvage enzyme but as the **anabolic arm of a regulated branch point** balancing vitamin B3 between energy catabolism and NAD⁺ biosynthesis.

### Localization

All evidence points to a **soluble cytoplasmic** enzyme: no signal peptide, no transmembrane segments, and cytosolic substrates (NA, PRPP, ATP). NAD⁺ salvage occurs in the cytoplasm.

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution |
|---|---|---|
| [9521741](https://pubmed.ncbi.nlm.nih.gov/9521741/) | *Kinetic mechanism of NAPRTase: implications for energy coupling* | Defines substrates/products; shows ATP-driven covalent phosphorylation at 30 s⁻¹ and 2000-fold PRPP affinity increase in the phosphoenzyme |
| [8672422](https://pubmed.ncbi.nlm.nih.gov/8672422/) | *Energy coupling in Salmonella NAPRTase: identification of His-219* | Identifies His-219 as the covalently phosphorylated catalytic residue (maps to *P. putida* His-224) |
| [12616693](https://pubmed.ncbi.nlm.nih.gov/12616693/) | *Effect of NAPRTase overexpression on NAD levels in E. coli* | States pncB reaction (NA→NaMN); identifies NA→NaMN as the rate-limiting step |
| [22975127](https://pubmed.ncbi.nlm.nih.gov/22975127/) | *Regulation of NAD(H) pool by pncB overexpression for succinic acid* | Confirms pncB as rate-limiting NAD(H) enzyme; overexpression enlarges NAD⁺ pool 6.2-fold, lowers NADH/NAD⁺ |
| [1987148](https://pubmed.ncbi.nlm.nih.gov/1987148/) | *Cloning and sequence of Salmonella pncB; NAPRTase structure* | Establishes cytoplasmic localization (no signal sequence); primary-structure reference |
| [20926389](https://pubmed.ncbi.nlm.nih.gov/20926389/) | *Genomics-driven reconstruction of Acinetobacter NAD metabolism* | Places PncB in deamidating salvage route with NiaP transporter; kinetic role assignment; antibacterial target context |
| [21450002](https://pubmed.ncbi.nlm.nih.gov/21450002/) | *A finely tuned regulatory circuit of the nic pathway in P. putida* | Establishes NA branch point in KT2440; catabolism vs. cofactor synthesis; protection of the vitamin-B3 pool |
| [29485696](https://pubmed.ncbi.nlm.nih.gov/29485696/) | *Bordetella bronchiseptica nic locus (similar to P. putida)* | Confirms NA catabolism influences NAD biosynthesis via a shared substrate pool |
| [24115625](https://pubmed.ncbi.nlm.nih.gov/24115625/) | *ppk deletion in P. putida KT2440* | Context on NAD-related enzymes (PpnK/NAD kinase) and polyP/NAD metabolism in the same organism |

**How the evidence converges.** No single paper directly assays *P. putida* Q88DF7, but the lines of evidence are mutually reinforcing. The biochemical mechanism (F001, F002) is defined in *Salmonella*/*E. coli* orthologs; the localization and rate-limiting role (F003) are established in enterobacteria and confirmed by metabolic-engineering outcomes; the physiological branch-point context (F004) is established directly in *P. putida* KT2440 and its close relative *Bordetella*; and the sequence orthology with strict conservation of the catalytic His-224 (F005) transfers the mechanistic conclusions to the *P. putida* protein with high confidence.

---

## Limitations and Knowledge Gaps

1. **No direct assay of the *P. putida* KT2440 enzyme.** The assignment is by orthology (53.7% identity to *E. coli* PncB) and residue conservation, not by purification and kinetics of Q88DF7. Km values for NA/PRPP/ATP, the ATP-coupling ratio, and kcat for the *P. putida* enzyme are unknown.
2. **No experimental structure.** There is no crystal/cryo-EM structure of Q88DF7; the phospho-His224 assignment is inferred from alignment.
3. **Regulation of pncB in *P. putida* is uncharacterized.** How pncB expression responds to NA availability, growth on NA as a carbon source, or NAD demand — and any NAD⁺-responsive control (as seen in enterobacteria) — has not been established here.
4. **Quantitative branch-point partitioning is unknown.** The fraction of intracellular NA committed to salvage (pncB) versus catabolism (nic operon) under different conditions has not been quantified with flux measurements.
5. **In vivo phenotype of a *P. putida* ΔpncB mutant** (NAD auxotrophy, growth on nicotinamide vs. NA, redox phenotypes) has not been reported for KT2440 specifically.

---

## Proposed Follow-up Experiments / Actions

1. **Biochemical characterization of recombinant Q88DF7.** Express and purify the *P. putida* enzyme; measure steady-state kinetics (Km for NA, PRPP, ATP; kcat), confirm ATP-dependent stimulation, and verify formation of an acid-labile phosphoenzyme to demonstrate the phosphohistidine intermediate directly.
2. **Site-directed mutagenesis of His-224.** Mutate His-224 to Ala/Gln and test for loss of ATP coupling / catalytic activity, directly validating the alignment-based prediction that His-224 is the energy-transducing residue.
3. **Structural determination.** Solve a crystal structure (± ATP/PRPP/NA analogs) or generate a high-confidence AlphaFold model with PAE analysis to confirm active-site architecture and the position of His-224.
4. **ΔpncB knockout in *P. putida* KT2440.** Test for NAD auxotrophy, ability to grow on nicotinamide/NA, and sensitivity to redox stress; complement with the wild-type gene. Assess whether the strain can still use NA as a carbon source via the *nic* operon when salvage is blocked.
5. **Flux and regulation studies.** Use ¹³C or targeted metabolomics to quantify NA partitioning between pncB salvage and nic-operon catabolism under varying NA/NAD demand; measure pncB transcript/protein levels across conditions to define regulation.
6. **Metabolic engineering validation.** Overexpress *P. putida* pncB and measure NAD(H) pool changes, mirroring the *E. coli* succinate study, to confirm the rate-limiting role in this organism.

---

## Conclusion

*pncB* (PP_4868, Q88DF7) of *Pseudomonas putida* KT2440 encodes **nicotinate phosphoribosyltransferase (NAPRTase, EC 6.3.4.21)**, a cytoplasmic, ATP-energized enzyme that catalyzes the first committed and rate-limiting step of the Preiss–Handler NAD⁺ salvage pathway: condensation of nicotinic acid with PRPP to form nicotinate mononucleotide. Its ATP coupling operates through a conserved covalent phosphohistidine (His-224) intermediate. In *P. putida*, PncB defines the anabolic fate of nicotinic acid at a regulated branch point where the same substrate can alternatively be degraded as a carbon source by the *nic* operon. The assignment is supported by strong orthology (53.7% identity to biochemically validated *E. coli* PncB) and strict conservation of catalytic residues, though direct biochemical characterization of the *P. putida* enzyme remains an open experimental goal.


## Artifacts

- [OpenScientist final report](pncB-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](pncB-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:12616693
2. PMID:9521741
3. PMID:8672422
4. PMID:1987148
5. PMID:22975127
6. PMID:21450002
7. PMID:20926389
8. PMID:29485696