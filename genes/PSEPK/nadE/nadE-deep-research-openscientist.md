---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-20T15:07:47.259104'
end_time: '2026-07-20T15:40:20.105702'
duration_seconds: 1952.85
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: nadE
  gene_symbol: nadE
  uniprot_accession: Q88DF6
  protein_description: 'RecName: Full=NH(3)-dependent NAD(+) synthetase {ECO:0000255|HAMAP-Rule:MF_00193};
    EC=6.3.1.5 {ECO:0000255|HAMAP-Rule:MF_00193};'
  gene_info: Name=nadE {ECO:0000255|HAMAP-Rule:MF_00193}; OrderedLocusNames=PP_4869;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the NAD synthetase family. {ECO:0000255|HAMAP-
  protein_domains: NAD/GMP_synthase. (IPR022310); NAD_synthase. (IPR003694); NH(3)-dep_NAD(+)_synth.
    (IPR022926); Rossmann-like_a/b/a_fold. (IPR014729); NAD_synthase (PF02540)
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
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: nadE-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: nadE-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88DF6
- **Protein Description:** RecName: Full=NH(3)-dependent NAD(+) synthetase {ECO:0000255|HAMAP-Rule:MF_00193}; EC=6.3.1.5 {ECO:0000255|HAMAP-Rule:MF_00193};
- **Gene Information:** Name=nadE {ECO:0000255|HAMAP-Rule:MF_00193}; OrderedLocusNames=PP_4869;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the NAD synthetase family. {ECO:0000255|HAMAP-
- **Key Domains:** NAD/GMP_synthase. (IPR022310); NAD_synthase. (IPR003694); NH(3)-dep_NAD(+)_synth. (IPR022926); Rossmann-like_a/b/a_fold. (IPR014729); NAD_synthase (PF02540)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "nadE" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'nadE' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **nadE** (gene ID: nadE, UniProt: Q88DF6) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of *nadE* (NH₃-dependent NAD⁺ synthetase, UniProt Q88DF6) in *Pseudomonas putida* KT2440

## 0. Identity Verification (Mandatory)

The target is confirmed and unambiguous. UniProt **Q88DF6** (gene **nadE**, ordered locus **PP_4869**) from *Pseudomonas putida* strain KT2440 (ATCC 47054 / DSM 6125) is a **275-residue, ~29.3 kDa** protein annotated as **NH(3)-dependent NAD(+) synthetase, EC 6.3.1.5** (HAMAP rule MF_00193). It belongs to the **NAD synthetase family** (Pfam PF02540; InterPro IPR003694 "NAD_synthase", IPR022926 "NH(3)-dep_NAD(+)_synth", IPR022310 "NAD/GMP_synthase", IPR014729 Rossmann-like α/β/α fold). The gene symbol, EC number, protein family and domain content are internally consistent and match the well-characterized bacterial NadE family. Function is described below from primary literature on the enzyme family (chiefly the near-identical *Bacillus subtilis* enzyme, whose structure/mechanism is solved to atomic resolution) combined with the organism-specific UniProt annotation; no gene-symbol ambiguity was encountered.

---

## 1. Summary (Answer to the Research Question)

NadE (Q88DF6) is the enzyme that catalyzes the **final, committed step of NAD⁺ biosynthesis**. It performs the **ATP-dependent amidation of nicotinic acid adenine dinucleotide (NaAD, "deamido-NAD⁺") to NAD⁺**, using **ammonia (NH₄⁺)** as the nitrogen donor:

> **deamido-NAD⁺ + NH₄⁺ + ATP → NAD⁺ + AMP + diphosphate (PPi) + H⁺**  (EC 6.3.1.5)

It is a **cytoplasmic homodimer** that acts through a **two-step mechanism via a covalent NaAD-adenylate intermediate**, and it is the single terminal enzyme on which both the *de novo* and salvage NAD⁺ pathways converge — making it central to redox metabolism and typically essential.

---

## 2. Primary Function: Reaction Catalyzed and Substrate Specificity

**Reaction (from UniProt catalytic-activity annotation):**
deamido-NAD⁺ + NH₄⁺ + ATP = AMP + diphosphate + NAD⁺ + H⁺ (EC 6.3.1.5).

**Pathway position:** "Cofactor biosynthesis; NAD⁺ biosynthesis; NAD⁺ from deamido-NAD⁺ (ammonia route): step 1/1" — i.e., NadE is the **terminal step** that installs the amide nitrogen that chemically distinguishes NAD⁺ from its precursor NaAD.

The final step of NAD⁺ biosynthesis "includes an amide transfer to nicotinic acid adenine dinucleotide (NaAD) catalyzed by NAD⁺ synthetase" (Symersky et al., 2002, PMID 12077433). The enzyme is ubiquitous and "transform[s] deamido-NAD⁺ into NAD⁺ by a two-step reaction" (Rizzi et al., 1998, PMID 9753692).

**Substrate specificity / nitrogen-donor selectivity.** Q88DF6 is a **short-form, NH₃-dependent** NAD synthetase: at 275 aa it consists of only the synthetase (Rossmann-like α/β/α) catalytic domain and **lacks the N-terminal glutaminase (glutamine amidotransferase) domain** found in glutamine-dependent enzymes (e.g., yeast Qns1, ~700 aa). Consequently it uses **free ammonium from the cellular pool** as the amide donor rather than generating ammonia in situ from glutamine. This contrasts with the two-domain glutamine-dependent enzyme, which "utilizes a glutamine aminotransferase domain to supply ammonia for amidation of nicotinic acid adenine dinucleotide (NaAD⁺) to NAD⁺" (Wojcik et al., 2006, PMID 16954203). (Note: many bacterial "NH₃-dependent" NadE enzymes retain some capacity to use glutamine in vitro, but the diagnostic architectural feature is the absence of a dedicated glutaminase domain; the physiological/annotated donor for Q88DF6 is ammonia.)

**Cofactor requirements:** ATP (hydrolyzed to AMP + PPi, characteristic of the N-type ATP pyrophosphatase superfamily) and divalent **Mg²⁺** (a binuclear Mg²⁺ cluster at the ATP site).

---

## 3. Catalytic Mechanism (Structural/Mechanistic Evidence)

NadE is a member of the **N-type ATP pyrophosphatase / PP-loop amidotransferase superfamily**. Catalysis proceeds in two chemical steps:

1. **Adenylation:** the nicotinate carboxylate of NaAD attacks the α-phosphate of ATP to form a reactive **NaAD-adenylate (NAD-adenylate) intermediate**, releasing pyrophosphate; this step is assisted by a **binuclear Mg²⁺ (trimetallic) constellation** rather than by protein side-chain catalysis.
2. **Amidation:** **ammonia performs a nucleophilic attack on the adenylate intermediate**, displacing AMP and yielding NAD⁺.

The mechanism is directly supported by high-resolution *B. subtilis* crystal structures that **trapped the intermediate**: the enzyme was solved "in complex with the trapped reaction intermediate NAD-adenylate" (Rizzi et al., 1998, PMID 9753692), and an atomic-resolution (1.0 Å) structure showed that "both binding sites are occupied by the NAD-adenylate intermediate, pyrophosphate and two magnesium ions," with "a mechanism … proposed for the second catalytic step, which includes a nucleophilic attack by the ammonia molecule on the intermediate" (Symersky et al., 2002, PMID 12077433).

**Active-site / ligand-binding residues in Q88DF6 (UniProt features):** an ATP/Mg-binding **P-loop (SGGxDS motif, ⁵⁰GISGGVDS⁵⁷)** and additional substrate-contacting residues at positions 56, 147, 167, 172, 180, 187, 196, 218, and 267–268. The SGGxD signature is the hallmark of the ATP-pyrophosphatase family and directly rationalizes the AMP + PPi product stoichiometry.

**Evolutionary justification for transferring this mechanism (Iteration 2 analysis).** Global pairwise alignment (Needleman–Wunsch) shows Q88DF6 shares **52.4% amino-acid identity (140/267 aligned positions) with the experimentally characterized *E. coli* NadE** (UniProt P18843, 275 aa) and **48.5% identity (129/266) with the *B. subtilis* NAD synthetase** (P08164, 272 aa) whose intermediate-trapped crystal structures defined the mechanism. All three are ~272–275 aa single-domain enzymes, and the catalytic PP-loop is conserved (Q88DF6 **SGGVDS** at res 52; *B. subtilis* **SGGQDS** at res 47). This level of identity across the full length, together with conservation of the catalytic motif, means the fold, active-site geometry, homodimeric assembly, and two-step adenylate chemistry established for the model enzymes apply directly to the *P. putida* protein. Critically, **all 11 UniProt-annotated ATP/substrate-binding residues of Q88DF6 are strictly identical** to their aligned positions in the *B. subtilis* structural enzyme (G50, D56, R147, T167, E172, K180, D187, K196, T218, H267, K268 — 11/11 conserved), confirming the active-site chemistry is preserved residue-for-residue.

**Non-redundancy (Iteration 3 analysis).** Proteome-wide UniProt queries of *P. putida* KT2440 (taxid 160488) return **exactly one** protein for EC 6.3.1.5, for the NAD synthetase family, and for gene *nadE* — Q88DF6 (PP_4869). There is **no paralogous isozyme**, so loss of NadE cannot be compensated, reinforcing its essential, non-redundant terminal role in NAD⁺ biosynthesis.

---

## 4. Quaternary Structure and Subcellular Localization

- **Quaternary structure:** **Homodimer** (UniProt SUBUNIT), consistent with "the *Bacillus subtilis* homodimeric NAD⁺ synthetase" (PMID 9753692). The deamido-NAD⁺ binding site lies at the subunit interface in the homolog, implying the dimer is the functional unit.
- **Localization:** **Cytoplasmic.** The protein has no signal peptide, no transmembrane segment, and no lipidation/secretion signals; as a soluble metabolic enzyme it carries out its reaction in the bacterial cytosol where NaAD, ATP, Mg²⁺ and ammonium are available. This is the expected compartment for a central intermediary-metabolism enzyme.

---

## 5. Pathway Context and Biological Role

NAD⁺ biosynthesis in bacteria funnels multiple inputs to a common intermediate, **nicotinic acid mononucleotide (NaMN)**, which is adenylylated by **NadD (NaMN adenylyltransferase)** to **NaAD**, and finally amidated by **NadE** to NAD⁺:

```
 de novo:  L-aspartate → (NadB/NadA/NadC) → NaMN
 salvage:  nicotinamide/nicotinic acid/NR → ... → NaMN
                                   │
                                   ▼
                     NaMN --NadD--> NaAD --NadE--> NAD⁺
```

Because **both the de novo (aspartate) route and the salvage routes converge on NaAD**, NadE is the **single terminal enzyme producing NAD⁺** in the cell; its activity cannot be bypassed by nicotinamide/nicotinic acid salvage. NAD⁺ (with NADH, and NADP(H) after phosphorylation by NAD kinase) is the electron carrier for respiration, redox balancing, and hundreds of biosynthetic and catabolic reactions.

**Essentiality and target validation (inference from close relatives).** In *M. tuberculosis*, NadD and NadE "were selected as promising candidate drug targets," and induced degradation of either enzyme "showed a strong bactericidal effect which coincided with anticipated changes in relative levels of NaMN and NaAD intermediates (substrates of NadD and NadE, respectively) and ultimate depletion of the NAD(H) pool," producing a metabolic catastrophe (Rodionova et al., 2014, PMID 24549842). More recent work confirms NadE (NAD synthesis) as metabolically distinct from and essential alongside NAD kinase in defining NAD(P) essentiality (Sharma et al., 2023, PMID 37350592). By strong homology and identical pathway position, NadE is expected to be essential in *P. putida* KT2440, where a robust NAD(H)/NADPH supply underpins the organism's noted redox-balancing systems (e.g., PntAB/SthA transhydrogenases, PMID 42335895) and industrial biotransformation capacity. Consistent with this, genome-wide transposon (Tn-seq/RB-TnSeq) studies of KT2440 build saturating libraries that disrupt "nearly all (4,778) non-essential genes" (Eng et al., 2021, PMID 33964456) — the terminal NAD-biosynthesis genes are expected to reside in the complementary essential-gene set that tolerates no insertions, although PP_4869 is not individually called out in those reports.

---

## 6. Evidence Summary

| Claim | Evidence type | Source |
|---|---|---|
| Reaction = ATP-dependent amidation of deamido-NAD⁺ → NAD⁺, NH₄⁺ donor, EC 6.3.1.5 | Curated annotation (HAMAP MF_00193) | UniProt Q88DF6 |
| Terminal step of NAD⁺ biosynthesis (step 1/1 from deamido-NAD⁺) | Curated pathway annotation | UniProt Q88DF6 |
| Two-step mechanism via trapped NAD-adenylate intermediate + Mg²⁺ + PPi | Atomic-resolution crystal structures (homolog) | PMID 9753692; PMID 12077433 |
| Ammonia nucleophilic attack in step 2 | Structural mechanism (homolog) | PMID 12077433 |
| Homodimer; interfacial deamido-NAD⁺ site | Curated + structural | UniProt; PMID 9753692 |
| Short NH₃-dependent form lacks glutaminase domain (vs glutamine-dependent Qns1) | Comparative/biochemical | PMID 16954203; sequence length 275 aa |
| Essential terminal enzyme / druggable, loss depletes NAD(H) | Genetic knockdown + ¹³C metabolomics (homolog) | PMID 24549842; PMID 37350592 |
| Cytoplasmic; ATP-pyrophosphatase P-loop (SGGxD, res 50–57) | Sequence/feature analysis | UniProt Q88DF6 |
| 52.4% id to *E. coli* NadE, 48.5% to *B. subtilis* NadE; PP-loop conserved | Pairwise alignment (this work) | UniProt P18843, P08164 |
| 11/11 annotated active-site residues identical to *B. subtilis* enzyme | Alignment residue mapping (this work) | UniProt Q88DF6, P08164 |
| Sole NAD synthetase (EC 6.3.1.5) in KT2440 — no paralog | Proteome query (this work) | UniProt taxid 160488 |

---

## 7. Supported and Refuted Hypotheses

- **Supported:** Q88DF6 is a bona fide NH₃-dependent NAD⁺ synthetase catalyzing the terminal amidation of NaAD to NAD⁺ via a NaAD-adenylate intermediate; it is a cytoplasmic homodimer of the ATP-pyrophosphatase superfamily; it occupies the essential convergence point of de novo and salvage NAD⁺ biosynthesis.
- **Refuted / excluded:** It is **not** a glutamine-dependent (two-domain, glutaminase-containing) NAD synthetase (too short, no glutaminase domain); it is not a membrane, transport, structural, or signaling protein.

## 8. Limitations and Future Directions

- Direct enzymological/structural data are for *P. putida* **inferred from homologs** (chiefly *B. subtilis*, and mycobacterial genetics); no KT2440-specific kinetic study of PP_4869 was located. The family is highly conserved, so transfer of mechanism is well justified, but organism-specific K_m/k_cat, in-vivo essentiality (e.g., a KT2440 knockout), and glutamine-vs-ammonia usage remain to be measured directly.
- Future work: solve/AlphaFold-validate the KT2440 structure, measure ammonia vs glutamine kinetics, and confirm essentiality by conditional knockdown in *P. putida* KT2440.

---

*Report generated Iteration 1. Databases consulted: UniProt (Q88DF6, live REST fetch), PubMed. Key primary references: PMID 9753692, 12077433, 16954203, 24549842, 37350592.*


## Artifacts

- [OpenScientist final report](nadE-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](nadE-deep-research-openscientist_artifacts/final_report.pdf)