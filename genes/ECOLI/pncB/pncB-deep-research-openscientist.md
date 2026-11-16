---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-12T04:27:19.722375'
end_time: '2026-11-12T04:37:00.651011'
duration_seconds: 580.93
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: ECOLI
  gene_id: P18133
  gene_symbol: pncB
  uniprot_accession: P18133
  protein_description: 'RecName: Full=Nicotinate phosphoribosyltransferase {ECO:0000255|HAMAP-Rule:MF_00570};
    Short=NAPRTase {ECO:0000255|HAMAP-Rule:MF_00570}; EC=6.3.4.21 {ECO:0000255|HAMAP-Rule:MF_00570};'
  gene_info: Name=pncB {ECO:0000255|HAMAP-Rule:MF_00570}; OrderedLocusNames=b0931,
    JW0914;
  organism_full: Escherichia coli (strain K12).
  protein_family: Belongs to the NAPRTase family. {ECO:0000255|HAMAP-
  protein_domains: N/Namide_PRibTrfase. (IPR041525); NAPRTase_N. (IPR040727); Nic_PRibTrfase.
    (IPR006406); Nic_PRibTrfase-Fam. (IPR007229); Nicotinate_pribotase-like_C. (IPR036068)
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
citation_count: 19
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
- **UniProt Accession:** P18133
- **Protein Description:** RecName: Full=Nicotinate phosphoribosyltransferase {ECO:0000255|HAMAP-Rule:MF_00570}; Short=NAPRTase {ECO:0000255|HAMAP-Rule:MF_00570}; EC=6.3.4.21 {ECO:0000255|HAMAP-Rule:MF_00570};
- **Gene Information:** Name=pncB {ECO:0000255|HAMAP-Rule:MF_00570}; OrderedLocusNames=b0931, JW0914;
- **Organism (full):** Escherichia coli (strain K12).
- **Protein Family:** Belongs to the NAPRTase family. {ECO:0000255|HAMAP-
- **Key Domains:** N/Namide_PRibTrfase. (IPR041525); NAPRTase_N. (IPR040727); Nic_PRibTrfase. (IPR006406); Nic_PRibTrfase-Fam. (IPR007229); Nicotinate_pribotase-like_C. (IPR036068)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "pncB" matches the protein description above**
2. **Verify the organism is correct:** Escherichia coli (strain K12).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'pncB' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **pncB** (gene ID: P18133, UniProt: P18133) in ECOLI.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *pncB* (Nicotinate Phosphoribosyltransferase), *Escherichia coli* K-12

**UniProt:** P18133 | **Gene:** *pncB* (b0931, JW0914) | **EC:** 6.3.4.21 (also historically EC 2.4.2.11) | **Organism:** *Escherichia coli* strain K-12

---

## Summary

The *E. coli* K-12 gene ***pncB*** (UniProt **P18133**) encodes **nicotinate phosphoribosyltransferase (NAPRTase, NAPRT)**, a soluble cytoplasmic enzyme that catalyzes the committed, rate-limiting entry step of the **Preiss–Handler NAD⁺ salvage pathway**. The enzyme transfers a phosphoribosyl group from 5-phospho-α-D-ribose 1-diphosphate (**PRPP**) onto **nicotinate (nicotinic acid, NA)**, producing **nicotinate mononucleotide (NaMN)** plus pyrophosphate (PPi). NaMN is a direct precursor of NAD⁺, feeding into the downstream, essential and conserved NadD→NadE segment shared with the de novo pathway. The gene identity is unambiguous: the UniProt annotation (NAPRTase family; NAPRTase/Nic_PRibTrfase domains), the catalyzed reaction, the organism, and the primary literature all converge on the same well-characterized *E. coli* enzyme.

The most distinctive mechanistic feature of NAPRTase is that it is a **facultative ATPase**: it couples the hydrolysis of ATP (1:1 with NaMN synthesis) to the phosphoribosyl-transfer reaction, thereby driving the reaction thermodynamically far past its chemical equilibrium. This ATP coupling proceeds through a **covalent phospho-histidine intermediate at His-219**, which transiently phosphorylates the enzyme and dramatically increases its affinity for substrates — the structural basis for its classification as a ligase (EC 6.3.4.21) rather than a simple glycosyltransferase. This energy-coupling mechanism was described as "a new paradigm for biochemical energy coupling" and distinguishes NAPRTase from most other phosphoribosyltransferases.

Functionally, *pncB*/NAPRTase sits at a key metabolic and regulatory node. Its product NaMN converges on the same downstream chemistry as the de novo quinolinate route, making it the branch-point enzyme of the deamidating nicotinamide/nicotinate salvage route. Its expression is feedback-controlled by the **NAD-sensing bifunctional regulator NadR**, which uses NAD⁺ as a corepressor to repress *pncB* coordinately with the de novo genes *nadA*/*nadB*, tying nicotinate salvage to intracellular NAD⁺ status. Because the enzyme controls NAD(H) pool size, *pncB* overexpression has become a widely used metabolic-engineering lever for boosting NAD(H) availability in industrial *E. coli* strains.

---

## Gene/Protein Identity Verification

Before proceeding, the mandatory identity check was completed and **confirms the target is correctly identified**:

| Verification criterion | UniProt P18133 annotation | Literature match | Status |
|---|---|---|---|
| Gene symbol matches protein | *pncB* = nicotinate phosphoribosyltransferase | *pncB* cloned from *E. coli* encodes NAPRTase ([PMID: 2211655](https://pubmed.ncbi.nlm.nih.gov/2211655/)) | ✅ Match |
| Organism | *E. coli* K-12 | *E. coli* K-12 *pncB* characterized directly | ✅ Match |
| Protein family / domains | NAPRTase family; Nic_PRibTrfase domains (IPR006406, IPR007229, IPR040727, IPR041525, IPR036068) | Type II PRTase fold confirmed by crystallography of ortholog ([PMID: 15753098](https://pubmed.ncbi.nlm.nih.gov/15753098/)) | ✅ Match |
| Reaction / EC | EC 6.3.4.21 (NaMN formation from NA + PRPP) | NaMN formation experimentally demonstrated ([PMID: 12616693](https://pubmed.ncbi.nlm.nih.gov/12616693/)) | ✅ Match |

The gene symbol *pncB* is **not ambiguous** in this context — there is abundant, specific primary literature on the *E. coli* / *Salmonella* enzyme, and it aligns perfectly with the UniProt family and domain annotations.

---

## Key Findings

### Finding 1 — *pncB* encodes NAPRTase, the committed, rate-limiting entry enzyme of the Preiss–Handler NAD⁺ salvage pathway

NAPRTase catalyzes the formation of nicotinate mononucleotide (NaMN) and pyrophosphate from nicotinate and PRPP:

```
Nicotinate (NA) + PRPP  →  Nicotinate mononucleotide (NaMN) + PPi
```

The *pncB* gene of *E. coli* was cloned on a 1.5-kb TaqI–EcoRI fragment and shown to encode nicotinic acid phosphoribosyltransferase ([PMID: 2211655](https://pubmed.ncbi.nlm.nih.gov/2211655/)): *"The pncB gene from Escherichia coli, which encodes nicotinic acid phosphoribosyltransferase (EC 2.4.2.11), was cloned on a 1.5-kilobase TaqI-EcoRI fragment."* Overexpression of the cloned gene produced a **25-fold increase in enzyme activity** and a **5-fold increase in intracellular NAD⁺** — direct evidence that NAPRTase activity controls the size of the cellular NAD pool: *"increased nicotinic acid phosphoribosyltransferase activity effects a 5-fold increase in the intracellular concentration of NAD"* (Wubbolts et al., 1990; [PMID: 2211655](https://pubmed.ncbi.nlm.nih.gov/2211655/)).

The reaction product and the enzyme's position in the pathway are explicitly defined in the metabolic-engineering literature ([PMID: 12616693](https://pubmed.ncbi.nlm.nih.gov/12616693/)): NAPRTase *"catalyzes the formation of nicotinate mononucleotide (NAMN), a direct precursor of NAD, from NA. This reaction is believed to be the rate-limiting step in the NAD salvage pathway."* The description of NAPRTase as the **rate-limiting enzyme of the NAD(H) salvage pathway** is corroborated repeatedly across independent metabolic-engineering studies that use *pncB* overexpression to raise NAD pools ([PMID: 22975127](https://pubmed.ncbi.nlm.nih.gov/22975127/), [PMID: 23740313](https://pubmed.ncbi.nlm.nih.gov/23740313/), [PMID: 12009797](https://pubmed.ncbi.nlm.nih.gov/12009797/)).

**Substrate specificity:** The enzyme is specific for **nicotinate (the deamidated pyridine, nicotinic acid)** as the pyridine-base substrate and **PRPP** as the phosphoribosyl donor. It does not act on nicotinamide directly; in the deamidating salvage route nicotinamide must first be converted to nicotinate by nicotinamidase (PncA) before NAPRTase can act (see Finding 5).

### Finding 2 — NAPRTase is an ATP-dependent enzyme that couples ATP hydrolysis to NaMN synthesis via a covalent phospho-His-219 intermediate (basis for EC 6.3.4.21)

Although the chemical transglycosylation (NA + PRPP ⇌ NaMN + PPi) is near thermodynamic equilibrium, NAPRTase is unusual among phosphoribosyltransferases in that it consumes ATP to drive the reaction strongly forward. Vinitsky & Grubmeyer (1993) showed that **NAPRTase hydrolyzes ATP in 1:1 molar stoichiometry with NaMN synthesis**, shifting the products/substrates ratio from the equilibrium value of **0.67** to a steady-state value of **~1100** — an ~1000-fold thermodynamic enhancement ([PMID: 7503993](https://pubmed.ncbi.nlm.nih.gov/7503993/)): *"NAPRTase hydrolyzes ATP in 1:1 molar stoichiometry to NAMN synthesis. Hydrolysis of ATP alters the ratio of products/substrates for the reaction nicotinate + PRPP <--> NAMN + PPi from its equilibrium value of 0.67 to a steady-state value of 1100."* This paper framed the behavior as "a new paradigm for biochemical energy coupling."

The mechanism of this coupling is a **covalent phosphoenzyme intermediate**. ATP phosphorylates a specific active-site histidine, **His-219**, forming an acid-labile/base-stable phosphoramidate (phosphohistidine). Gross et al. (1996) identified His-219 as the site of phosphorylation and demonstrated that the phospho-His-219 species is a genuine catalytic intermediate shared by both the ATPase and NaMN-synthesis functions ([PMID: 8672422](https://pubmed.ncbi.nlm.nih.gov/8672422/)): *"NAPRTase phosphorylated at His-219 is an intermediate in the energy transduction mechanism of NAPRTase."*

Mechanistically, phosphorylation of the enzyme **dramatically tightens substrate binding**. Gross et al. (1998) showed that the phosphoenzyme (E-P) binds PRPP with a **K_D of 0.6 µM — ~2000-fold tighter than the unphosphorylated enzyme** — and lowers the K_m for both nicotinate and PRPP by roughly 200-fold ([PMID: 9521741](https://pubmed.ncbi.nlm.nih.gov/9521741/)): *"The phosphoenzyme (E-P) binds PRPP with a KD of 0.6 microM, a value 2000-fold lower than that measured for the nonphosphorylated enzyme."* Thus the energy of ATP hydrolysis is transduced into a high-affinity, catalytically poised phosphoenzyme that is subsequently discharged during product formation. This ATP-coupling behavior is the biochemical justification for reclassifying NAPRTase from a transferase (old EC 2.4.2.11) to a **ligase, EC 6.3.4.21**.

| Parameter | Non-phosphorylated enzyme | Phospho-His-219 enzyme | Effect |
|---|---|---|---|
| PRPP binding K_D | ~1,200 µM (2000× higher) | 0.6 µM | ~2000-fold tighter |
| K_m (NA, PRPP) | baseline | ~200-fold lower | tighter substrate binding |
| Products/substrates ratio | 0.67 (equilibrium) | ~1100 (steady state) | ~1000-fold forward drive |
| ATP:NaMN stoichiometry | — | 1:1 | obligate energy coupling |

### Finding 3 — *pncB* transcription is feedback-repressed by the NAD-sensing bifunctional regulator NadR, coordinately with de novo NAD genes

NAPRTase is embedded in a NAD-responsive regulatory network. In *Salmonella typhimurium* — the close enteric relative in which much of this regulation was dissected — the pyridine-nucleotide salvage pathway is controlled at *pncB*, and *pncB*, *nadA*, and *nadB* are **coordinately regulated by the product of the *nadR* gene** (Foster et al., 1990; [PMID: 2198247](https://pubmed.ncbi.nlm.nih.gov/2198247/)): *"the pyridine nucleotide salvage pathway is controlled at pncB. The transcriptional expression of these three loci is coordinately regulated by the product of nadR."*

NadR is a **NAD-dependent DNA-binding repressor** that binds conserved "NAD box" operator sequences as a multimer, using NAD⁺ itself as the physiological corepressor. Penfound & Foster (1999) demonstrated that **NAD is the relevant in vivo corepressor** ([PMID: 9882682](https://pubmed.ncbi.nlm.nih.gov/9882682/)): *"NAD proved to be the relevant in vivo corepressor."* When intracellular NAD⁺ is abundant, NadR–NAD represses the salvage and de novo genes; when NAD⁺ is scarce, repression is relieved and salvage flux increases. Consistent with this feedback logic, growth of *E. coli* in the presence of nicotinic acid (which raises NAD) **strongly represses NAPRTase activity** ([PMID: 2211655](https://pubmed.ncbi.nlm.nih.gov/2211655/)): *"Growth of E. coli in the presence of nicotinic acid leads to strong repression of nicotinic acid phosphoribosyltransferase activity."*

NadR is itself a remarkable **multifunctional/trifunctional protein**: an N-terminal DNA-binding (repressor) domain, a central NMN adenylyltransferase domain that senses NAD, and a C-terminal ribosylnicotinamide kinase domain ([PMID: 15805524](https://pubmed.ncbi.nlm.nih.gov/15805524/), [PMID: 12446641](https://pubmed.ncbi.nlm.nih.gov/12446641/)). It also modulates the activity of the PnuC NMN transport system ([PMID: 1991724](https://pubmed.ncbi.nlm.nih.gov/1991724/)). More recently, NadR has been shown to be a **c-di-GMP effector**, linking the second messenger c-di-GMP to NAD biosynthesis by de-repressing NadR-controlled genes ([PMID: 40823837](https://pubmed.ncbi.nlm.nih.gov/40823837/)) — placing *pncB* within an even broader signaling context.

### Finding 4 — NAPRTase adopts a type II PRTase (α/β) fold and functions as a soluble cytoplasmic enzyme

The crystal structure of a NAPRTase ortholog from *Thermoplasma acidophilum* revealed a multidomain architecture whose central functional domain has a **type II phosphoribosyltransferase fold** ([PMID: 15753098](https://pubmed.ncbi.nlm.nih.gov/15753098/)): *"the functional domain has a type II phosphoribosyltransferase fold that may be a common architecture for both nicotinic acid and quinolinic acid (QA) phosphoribosyltransferases (PRTase)."* This fold is shared with quinolinate PRTase despite low primary sequence similarity, reflecting deep evolutionary convergence on a common catalytic architecture for pyridine-mononucleotide biosynthesis.

The structure also defines the **molecular basis of nicotinate recognition**: the active-site pocket forms at a dimer interface, and the nicotinate moiety of the product NaMN is **intercalated between the highly conserved aromatic residues Tyr21 and Phe138** ([PMID: 15753098](https://pubmed.ncbi.nlm.nih.gov/15753098/)): *"the nicotinate moiety of NAMN is intercalated between highly conserved aromatic residues Tyr(21) and Phe(138)."* These aromatic clamps provide π-stacking interactions that confer specificity for the planar pyridine ring.

**Localization:** The *E. coli* enzyme (~401 aa; the *S. typhimurium* ortholog is 399 aa) is purified and assayed as a **soluble protein**, consistent with a **cytoplasmic** location where all three of its substrates — PRPP, nicotinate, and ATP — reside. UniProt P18133 annotates **no signal peptide and no transmembrane segment**, supporting an exclusively cytosolic function. There is no evidence of membrane association or secretion; the enzyme operates within the cytoplasm as part of soluble central metabolism.

### Finding 5 — *pncB* is the branch-point enzyme of the deamidating nicotinamide salvage route, converging on the shared, essential NadD→NadE segment

NAPRTase occupies the convergence point between salvage and de novo NAD⁺ synthesis. The salvage pathway recycles both intracellular NAD breakdown products and preformed pyridine compounds taken up from the environment, such as nicotinic acid ([PMID: 12616693](https://pubmed.ncbi.nlm.nih.gov/12616693/)): *"The salvage pathway recycles intracellular NAD breakdown products and preformed pyridine compounds from the environment, such as nicotinic acid (NA)."* In the **deamidating route**, exogenous or recycled **nicotinamide is first deamidated to nicotinate by nicotinamidase (PncA)**, and **PncB/NAPRTase then converts nicotinate to NaMN**.

Crucially, NaMN is the **same product** generated by the de novo pathway's quinolinate phosphoribosyltransferase (NadC). Both routes therefore funnel into the shared terminal two steps: **NadD (nicotinate/nicotinamide mononucleotide adenylyltransferase)**, which adenylylates NaMN to nicotinate adenine dinucleotide (NaAD), and **NadE (NAD synthetase)**, which amidates NaAD to NAD⁺. Sorci et al. (2010) emphasize that these last two steps are **conserved and essential in most bacteria** ([PMID: 20926389](https://pubmed.ncbi.nlm.nih.gov/20926389/)): *"Enzymes involved in the last steps of NAD biogenesis, nicotinate mononucleotide adenylyltransferase (NadD) and NAD synthetase (NadE), are conserved and essential in most bacterial species."* Thus *pncB* supplies NaMN to a conserved, essential downstream segment, making it the metabolic gateway for nicotinate utilization.

---

## Mechanistic Model / Interpretation

### The reaction and its energy coupling

```
        ATP        ADP + Pi (via phospho-His-219 intermediate)
         \          /
          \        /
   NA + PRPP  ──NAPRTase──►  NaMN + PPi
   (nicotinate)                (nicotinate mononucleotide)

   Net driving force: ATP hydrolysis shifts [products]/[substrates]
   from ~0.67 (equilibrium) to ~1100 (steady state)
```

The enzyme cycles between a low-affinity resting state and a high-affinity phospho-His-219 state:

```
   E  + ATP  ──►  E~P(His219) + ADP        (autophosphorylation; primes the enzyme)
   E~P + PRPP     ──►  E~P·PRPP  (K_D 0.6 µM, ~2000× tighter)
   E~P·PRPP + NA  ──►  E + NaMN + PPi + Pi  (catalysis + dephosphorylation)
```

ATP is not chemically incorporated into the product; instead its hydrolysis energy is stored transiently as a phosphohistidine and spent to raise substrate affinity and pull the equilibrium forward. This is the "new paradigm" of biochemical energy coupling — a phosphoribosyltransferase behaving as a ligase.

### Position in NAD⁺ metabolism

```
 DE NOVO (from aspartate)          SALVAGE / IMPORT
   Asp → ... → Quinolinate          Nicotinamide (Nam, from NAD turnover/import)
                   │                          │  PncA (nicotinamidase, deamidation)
                   │ NadC (QaPRT)             ▼
                   │                      Nicotinate (NA) ◄── import
                   ▼                          │  *** pncB / NAPRTase *** (+ATP)
              ┌──────────── NaMN ◄────────────┘
              │  (nicotinate mononucleotide — convergence point)
              ▼
            NadD  (NaMN adenylyltransferase)  → NaAD
              ▼
            NadE  (NAD synthetase)            → NAD⁺
```

### Regulatory logic

```
   High intracellular NAD⁺
          │
          ▼
   NadR + NAD⁺ (corepressor) ──► binds "NAD box" operators
          │
          ▼
   REPRESSES pncB, nadA, nadB  ──►  less salvage/de novo flux
   (feedback inhibition of NAD biosynthesis)

   Low NAD⁺ → NadR releases DNA → derepression → more pncB → more NaMN → more NAD⁺
   (c-di-GMP also modulates NadR, de-repressing NAD biosynthesis)
```

### Synthesis

*pncB*/NAPRTase is best understood as the **energy-invested, feedback-controlled gatekeeper of nicotinate salvage**. It commits scavenged nicotinate to NAD⁺ synthesis, spends an ATP to make this commitment thermodynamically decisive, and is transcriptionally throttled by the cell's NAD⁺ status via NadR. Because it is rate-limiting, it functions as the principal control point that sets NAD(H) pool size — which is precisely why metabolic engineers exploit it (see below). Its product NaMN is the common currency into which both de novo and salvage routes convert, feeding the essential NadD→NadE finishing steps.

---

## Metabolic-Engineering Relevance (illustrating the rate-limiting role)

A consistent body of applied studies confirms, in vivo, that *pncB* sets NAD(H) availability. Overexpressing NAPRTase raises total NAD(H) and lowers the NADH/NAD⁺ ratio, restoring redox balance in strains engineered for anaerobic chemical production:

| Study (PMID) | System | Effect of *pncB* overexpression |
|---|---|---|
| [PMID: 2211655](https://pubmed.ncbi.nlm.nih.gov/2211655/) | *E. coli* K-12 | 25× enzyme activity; 5× intracellular NAD⁺ |
| [PMID: 12616693](https://pubmed.ncbi.nlm.nih.gov/12616693/) | *E. coli* | Raised total NAD; altered NADH/NAD⁺ and metabolite distribution |
| [PMID: 22975127](https://pubmed.ncbi.nlm.nih.gov/22975127/) | *E. coli* NZN111 (ΔldhA ΔpflB) | NADH/NAD⁺ fell 0.64→0.13; NAD⁺ up 6.2×; restored glucose use; ↑succinate |
| [PMID: 23740313](https://pubmed.ncbi.nlm.nih.gov/23740313/) | *E. coli* BA016 (+PYC) | Total NAD(H) 9.8× higher; NADH/NAD⁺ 0.60→0.04; ↑succinate |
| [PMID: 24564896](https://pubmed.ncbi.nlm.nih.gov/24564896/) | *E. coli* BA209 (+PEPCK) | Total NAD(H) 1.25×; NADH/NAD⁺ 0.28→0.11; ↑succinate from xylose |
| [PMID: 22506415](https://pubmed.ncbi.nlm.nih.gov/22506415/) | *E. coli* S17-1 (+NadE) | ↑NAD; +40.9% productivity converting 1,4-BD→4-HB |

These studies corroborate, from an orthogonal (applied) angle, the biochemical conclusion that NAPRTase is the flux-controlling step of NAD(H) salvage.

---

## Evidence Base

| PMID | Paper (abbreviated) | Supports finding | Nature of evidence |
|---|---|---|---|
| [2211655](https://pubmed.ncbi.nlm.nih.gov/2211655/) | *Variation of cofactor levels… expression of the pncB gene…* (Wubbolts et al. 1990) | F1, F3 | Experimental: cloning, overexpression (25× activity, 5× NAD), NA repression |
| [12616693](https://pubmed.ncbi.nlm.nih.gov/12616693/) | *Effect of NAPRTase overexpression on NAD, NADH/NAD⁺…* | F1, F5 | Experimental: NaMN as product; rate-limiting step; salvage definition |
| [7503993](https://pubmed.ncbi.nlm.nih.gov/7503993/) | *A new paradigm for biochemical energy coupling…* (Vinitsky & Grubmeyer 1993) | F2 | Biochemical: 1:1 ATP coupling; 0.67→1100 ratio shift |
| [8672422](https://pubmed.ncbi.nlm.nih.gov/8672422/) | *Energy coupling… identification of His-219…* (Gross et al. 1996) | F2 | Biochemical: phospho-His-219 covalent intermediate |
| [9521741](https://pubmed.ncbi.nlm.nih.gov/9521741/) | *Kinetic mechanism of NAPRTase…* (Gross et al. 1998) | F2 | Kinetics: phosphoenzyme PRPP K_D 0.6 µM (2000× tighter) |
| [2198247](https://pubmed.ncbi.nlm.nih.gov/2198247/) | *Regulation of NAD metabolism in S. typhimurium… nadR…* | F3 | Genetics: pncB/nadA/nadB coordinately controlled by NadR |
| [9882682](https://pubmed.ncbi.nlm.nih.gov/9882682/) | *NAD-dependent DNA-binding activity of NadR…* | F3 | Biochemical: NAD is the in vivo corepressor |
| [15753098](https://pubmed.ncbi.nlm.nih.gov/15753098/) | *Crystal structure of NAPRTase from T. acidophilum…* | F4 | Structural: type II PRTase fold; Tyr21/Phe138 nicotinate clamp |
| [20926389](https://pubmed.ncbi.nlm.nih.gov/20926389/) | *Genomics-driven reconstruction of Acinetobacter NAD metabolism…* (Sorci et al. 2010) | F5 | Comparative genomics: NadD/NadE conserved, essential downstream |
| [15805524](https://pubmed.ncbi.nlm.nih.gov/15805524/), [12446641](https://pubmed.ncbi.nlm.nih.gov/12446641/), [1991724](https://pubmed.ncbi.nlm.nih.gov/1991724/), [40823837](https://pubmed.ncbi.nlm.nih.gov/40823837/) | NadR multifunctionality, NMN transport, c-di-GMP control | F3 (context) | Supporting regulatory context |

**Note on structural evidence:** The definitive crystallographic data (F4) come from a *Thermoplasma acidophilum* ortholog rather than the *E. coli* enzyme itself. The fold, dimeric active-site architecture, and conserved aromatic recognition residues are expected to be conserved across the NAPRTase family given the shared domains annotated for P18133, but direct *E. coli* structural confirmation is inferred rather than solved here.

---

## Limitations and Knowledge Gaps

1. **Structural data are from an ortholog.** The type II PRTase fold and the Tyr21/Phe138 nicotinate-binding residues (F4) were determined for the *Thermoplasma acidophilum* NAPRTase, not *E. coli* P18133. Residue numbering and precise active-site geometry in the *E. coli* enzyme are inferred by homology.

2. **Energy-coupling mechanism characterized largely in *Salmonella*.** The phospho-His-219 intermediate and kinetic coupling parameters (F2) were elucidated primarily in *S. typhimurium* NAPRTase. Given the very high identity between the enterobacterial orthologs, these conclusions almost certainly transfer to *E. coli*, but the His-219 numbering should be mapped onto the *E. coli* sequence for certainty.

3. **Regulation dissected mainly in *Salmonella*.** The NadR corepressor mechanism and coordinate control of *pncB*/*nadA*/*nadB* (F3) were established in *S. typhimurium*. *E. coli* NadR is homologous and the NA-repression phenotype is reproduced in *E. coli* ([PMID: 2211655](https://pubmed.ncbi.nlm.nih.gov/2211655/)), but quantitative operator/affinity data specific to *E. coli pncB* are less complete.

4. **No direct *E. coli* subcellular-localization experiment.** The cytoplasmic assignment (F4) rests on solubility during purification, the absence of a signal peptide/TM segment in P18133, and the cytosolic location of its substrates — strong but inferential rather than a direct localization assay.

5. **ATP coupling is "facultative."** NAPRTase can run without ATP (at the unfavorable 0.67 equilibrium). The physiological conditions under which the cell toggles between ATP-coupled and uncoupled operation, and the in vivo flux consequences, are not fully quantified.

6. **mRNA-level regulation.** Translational enhancement by downstream adenine-rich motifs in the *pncB* coding sequence ([PMID: 17085569](https://pubmed.ncbi.nlm.nih.gov/17085569/)) adds a layer of expression control that was noted but not integrated into a quantitative model here.

---

## Proposed Follow-up Experiments / Actions

1. **Solve or model the *E. coli* NAPRTase structure.** Determine a crystal/cryo-EM structure of *E. coli* P18133 (or build a validated AlphaFold model) to confirm the type II PRTase fold, map the His-219 equivalent, and verify the Tyr/Phe nicotinate-clamp residues directly in the *E. coli* enzyme.

2. **Site-directed mutagenesis of the phospho-acceptor His.** Mutate the *E. coli* His-219 equivalent (H→A, H→Q) and measure: (a) loss of ATPase activity, (b) loss of the ~1000-fold thermodynamic enhancement, and (c) in vivo NAD pool size — confirming the energy-coupling residue in *E. coli*.

3. **Quantify in vivo ATP coupling.** Use ¹³C/isotope flux and metabolomics under energy-limited vs. energy-replete conditions to determine when NAPRTase runs in ATP-coupled vs. uncoupled mode and how this sets NaMN/NAD flux.

4. **Direct localization assay.** Confirm cytoplasmic localization with a functional fluorescent fusion or cell-fractionation + immunoblot in *E. coli*.

5. **Map *E. coli* NadR operators on *pncB*.** Perform ChIP-seq / DNase footprinting and EMSA with purified *E. coli* NadR ± NAD to quantify operator affinity and define the NAD-dependent repression threshold for *pncB* specifically.

6. **Probe the c-di-GMP–NadR–*pncB* axis in *E. coli*.** Test whether manipulating c-di-GMP levels de-represses *pncB* and raises NAD⁺ in *E. coli*, extending the recently reported c-di-GMP/NadR link ([PMID: 40823837](https://pubmed.ncbi.nlm.nih.gov/40823837/)).

---

## Conclusion

*E. coli* K-12 ***pncB*** (P18133) encodes **nicotinate phosphoribosyltransferase (NAPRTase)**, the soluble cytoplasmic, rate-limiting entry enzyme of the Preiss–Handler NAD⁺ salvage pathway. It transfers a phosphoribosyl group from PRPP to nicotinate to yield NaMN + PPi, uniquely coupling ATP hydrolysis (via a phospho-His-219 intermediate) to drive the reaction ~1000-fold past equilibrium — the basis of its ligase classification (EC 6.3.4.21). Its product NaMN feeds the conserved, essential NadD→NadE steps that complete NAD⁺ synthesis, and its expression is feedback-repressed by the NAD-sensing regulator NadR, embedding *pncB* in the cell's central NAD⁺ homeostatic circuitry.


## Artifacts

- [OpenScientist final report](pncB-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](pncB-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:2211655
2. PMID:15753098
3. PMID:12616693
4. PMID:22975127
5. PMID:23740313
6. PMID:12009797
7. PMID:7503993
8. PMID:8672422
9. PMID:9521741
10. PMID:2198247
11. PMID:9882682
12. PMID:15805524
13. PMID:12446641
14. PMID:1991724
15. PMID:40823837
16. PMID:20926389
17. PMID:24564896
18. PMID:22506415
19. PMID:17085569