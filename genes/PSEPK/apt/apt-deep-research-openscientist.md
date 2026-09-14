---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-19T07:16:06.084426'
end_time: '2026-08-19T08:49:42.942428'
duration_seconds: 5616.86
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: apt
  gene_symbol: apt
  uniprot_accession: Q88F33
  protein_description: 'RecName: Full=Adenine phosphoribosyltransferase {ECO:0000255|HAMAP-Rule:MF_00004};
    Short=APRT {ECO:0000255|HAMAP-Rule:MF_00004}; EC=2.4.2.7 {ECO:0000255|HAMAP-Rule:MF_00004};'
  gene_info: Name=apt {ECO:0000255|HAMAP-Rule:MF_00004}; OrderedLocusNames=PP_4266;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the purine/pyrimidine phosphoribosyltransferase
  protein_domains: Ade_phspho_trans. (IPR005764); Adenine_PRTase. (IPR050120); PRTase-like.
    (IPR029057); PRTase_dom. (IPR000836); Pribosyltran (PF00156)
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
citation_count: 16
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: apt-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: apt-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88F33
- **Protein Description:** RecName: Full=Adenine phosphoribosyltransferase {ECO:0000255|HAMAP-Rule:MF_00004}; Short=APRT {ECO:0000255|HAMAP-Rule:MF_00004}; EC=2.4.2.7 {ECO:0000255|HAMAP-Rule:MF_00004};
- **Gene Information:** Name=apt {ECO:0000255|HAMAP-Rule:MF_00004}; OrderedLocusNames=PP_4266;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the purine/pyrimidine phosphoribosyltransferase
- **Key Domains:** Ade_phspho_trans. (IPR005764); Adenine_PRTase. (IPR050120); PRTase-like. (IPR029057); PRTase_dom. (IPR000836); Pribosyltran (PF00156)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "apt" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'apt' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **apt** (gene ID: apt, UniProt: Q88F33) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *apt* (Adenine Phosphoribosyltransferase, APRT) in *Pseudomonas putida* KT2440

**UniProt Accession:** Q88F33 | **Gene:** *apt* | **Ordered Locus:** PP_4266
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440)
**EC:** 2.4.2.7 | **Protein family:** Purine/pyrimidine phosphoribosyltransferase (type I PRTase)
**Domains:** Pfam PF00156 (Pribosyltran); InterPro IPR005764 (Ade_phspho_trans), IPR050120 (Adenine_PRTase), IPR000836 (PRTase_dom), IPR029057 (PRTase-like)

---

## Summary

The gene *apt* (locus PP_4266; UniProt Q88F33) of *Pseudomonas putida* KT2440 encodes **adenine phosphoribosyltransferase (APRT, EC 2.4.2.7)**, a Mg²⁺-dependent cytoplasmic enzyme that catalyzes the single, committed step of the adenine salvage pathway: the transfer of the 5-phosphoribosyl group from 5-phospho-α-D-ribose-1-diphosphate (PRPP) onto the N9 nitrogen of free adenine, producing **adenosine-5′-monophosphate (AMP) and inorganic pyrophosphate (PPi)**. The identity is unambiguous — the gene symbol, the EC number, the protein family, and the diagnostic type I PRTase domains (Pfam PF00156; InterPro IPR005764/IPR000836) all converge on a well-characterized enzyme class, and the assignment is propagated by curated HAMAP rule MF_00004. Although no crystal structure or dedicated kinetic study exists for the *P. putida* enzyme itself, its function can be assigned with high confidence through strong sequence conservation and an extensive body of structural and biochemical work on orthologous APRTs from human, *Giardia lamblia*, *Leishmania tarentolae*, *Francisella tularensis*, and *Fusobacterium nucleatum*.

Mechanistically, APRT is a symmetric **homodimer** in which each subunit is built on a Rossmann-fold core capped by a small "hood" domain unique to APRTs; the active site lies at or near the dimer interface. Catalysis proceeds through an ordered mechanism in which PRPP binds first (stabilizing the active conformation and forming a pyrophosphate-binding pocket via a non-proline *cis*-peptide bond), a flexible catalytic loop closes over the active site, a conserved active-site glutamate acts as a general base to deprotonate adenine N9, and the deprotonated purine attacks the anomeric carbon of PRPP through a **dissociative, oxocarbenium-ion-like transition state**. The reaction is thermodynamically and kinetically driven toward AMP synthesis — the reverse reaction is >100-fold slower. Strict specificity for the 6-**amino**purine adenine (as opposed to the 6-**oxo**purines hypoxanthine, guanine, and xanthine handled by the separate HG(X)PRTase family) is enforced by an N–H···N1 hydrogen bond from a rigid, aromatic/proline-stabilized base-binding loop.

Physiologically, APRT is the terminal recycling node of adenine metabolism. The free adenine it salvages arises both from exogenous uptake and, importantly, from the endogenous **MTAN reaction** (5′-methylthioadenosine/S-adenosylhomocysteine nucleosidase), which releases adenine as a byproduct of polyamine (spermidine) biosynthesis, SAM-dependent methylation, and autoinducer/quorum-sensing metabolism. By returning this adenine to the AMP/adenylate pool, APRT keeps these metabolic fluxes running and prevents inhibitory adenine accumulation. In *P. putida* KT2440, which retains a functional de novo purine biosynthesis pathway, *apt* is a **dispensable, non-essential** salvage enzyme: it is not required for viability on glucose minimal medium, and its loss manifests phenotypically only under purine limitation, when de novo synthesis is blocked, or through loss of the ability to activate (and hence resistance to) toxic adenine analogs such as 2,6-diaminopurine and 6-methylpurine.

---

## Gene/Protein Identification and Verification

The mandatory identity check is satisfied on all counts:

| Verification criterion | Result |
|---|---|
| Gene symbol "*apt*" matches protein description | ✅ *apt* is the canonical symbol for adenine phosphoribosyltransferase across bacteria |
| Organism | ✅ *Pseudomonas putida* KT2440 (PSEPK), locus PP_4266 |
| Protein family / domains align with literature | ✅ Type I PRTase, Pfam PF00156, matches structurally characterized APRTs (human, *Giardia*, *Leishmania*, *Francisella*, *Fusobacterium*) |
| Diagnostic sequence motif | ✅ Q88F33 carries the type I PRTase PRPP-binding motif (Asp–Asp…TGG dyad coordinating the ribose 2′,3′-OH) |
| Risk of symbol ambiguity | Low — "*apt*" unambiguously denotes APRT in bacterial genetics; EC 2.4.2.7 and HAMAP MF_00004 fix the assignment |

Literature is abundant for the **enzyme class** (APRT) even though it is limited for the *P. putida* ortholog specifically. Functional assignment therefore relies on orthology transfer from biochemically and structurally characterized homologs — an appropriate and robust approach for a highly conserved housekeeping salvage enzyme.

---

## Key Findings

### Finding 1 — *apt* encodes adenine phosphoribosyltransferase catalyzing adenine + PRPP → AMP + PPi

The primary function of the *apt* gene product is enzymatic. APRT catalyzes the Mg²⁺-dependent transfer of the 5-phosphoribosyl group from **PRPP** to the **N9 position of adenine**, yielding **AMP + pyrophosphate**:

```
        adenine  +  PRPP  ──(APRT, Mg²⁺)──►  AMP  +  PPi
       (6-aminopurine)                     (adenylate)
```

The reaction is defined by EC 2.4.2.7. Detailed kinetics from the closely related *Giardia lamblia* enzyme establish substrate specificity and directionality: adenine has a *K*ₘ of 4.2 µM and PRPP a *K*ₘ of 143 µM, with a forward *k*cat of 2.8 s⁻¹. The reverse reaction (AMP + PPi → adenine + PRPP) is more than 100-fold slower (*k*cat = 9.5 × 10⁻³ s⁻¹; AMP and PPi *K*ₘ values of 87 and 450 µM), which drives net flux toward AMP synthesis — exactly what a salvage enzyme must do to replenish the nucleotide pool. Product-inhibition studies show the forward reaction follows a **random Bi-Bi mechanism** [PMID: 12171924](https://pubmed.ncbi.nlm.nih.gov/12171924/):

> "Adenine and alpha-d-5-phosphoribosyl-1-pyrophosphate (PRPP) have K(m) values of 4.2 and 143 microm with a k(cat) of 2.8 s(-1) in the forward reaction, whereas AMP and PP(i) have K(m) values of 87 and 450 microm with a k(cat) of 9.5 x 10(-3) s(-1) in the reverse reaction. Product inhibition studies indicated that the forward reaction follows a random Bi Bi mechanism."

The salvage role is stated directly in the structural literature: "APRT is an enzyme involved in the salvage of adenine (a 6-aminopurine), converting it to AMP" [PMID: 29694705](https://pubmed.ncbi.nlm.nih.gov/29694705/).

> **Evidence quality:** High. Kinetic mechanism and parameters are from precise enzymological studies of orthologs; the EC assignment and conserved catalytic motifs are present in the target sequence.

### Finding 2 — Adenine specificity is imposed by an N–H···N1 hydrogen bond from a rigid base-binding loop

APRT must select adenine (a 6-**amino**purine) and exclude the 6-**oxo**purines (hypoxanthine, guanine, xanthine), which are handled by the mechanistically and structurally distinct HG(X)PRTase family. Crystallographic and bioinformatic analysis — including a survey of ~4,000 APRT sequences at an 80% identity cutoff — shows this discrimination is achieved through an **N–H···N hydrogen bond between the backbone of the base-binding loop and the N1 atom of adenine** [PMID: 29694705](https://pubmed.ncbi.nlm.nih.gov/29694705/): "an N-H···N hydrogen bond between the base-binding loop and the N1 atom of adenine is the key interaction that differentiates adenine from 6-oxopurines." The 6-amino group's electronic configuration positions N1 as a hydrogen-bond acceptor in a geometry incompatible with 6-oxopurines.

The base-binding loop is rigidified by conserved aromatic and proline residues, and its integrity is functionally essential: an **F23A mutation** on this loop "severely affects the efficiency of the enzyme" [PMID: 29694705](https://pubmed.ncbi.nlm.nih.gov/29694705/). Evolutionarily, APRTs are structurally distinct from HG(X)PRTases and are most closely related to orotate phosphoribosyltransferases, consistent with a shared type I PRTase ancestry but divergent base-recognition modules. This same substrate promiscuity toward adenine analogs (2,6-diaminopurine, 6-methylpurine) is the basis of the analog-activation phenotype discussed in Finding 4.

> **Evidence quality:** High. Combines crystallography, large-scale sequence bioinformatics, and site-directed mutagenesis on an APRT ortholog.

### Finding 3 — APRT is a cytoplasmic homodimeric type I PRTase with a Rossmann-fold core, catalytic loop, Mg-PRPP chemistry, and a general-base glutamate

Multiple independent crystal structures define the architecture and mechanism of the APRT family: human APRT [PMID: 18399692](https://pubmed.ncbi.nlm.nih.gov/18399692/), *Leishmania tarentolae* APRT [PMID: 14726202](https://pubmed.ncbi.nlm.nih.gov/14726202/), and *Giardia lamblia* APRT [PMID: 12171925](https://pubmed.ncbi.nlm.nih.gov/12171925/).

- **Quaternary structure:** APRT is a **symmetric homodimer**; each monomer is built around a Rossmann-fold core "common to all known purine phosphoribosyltransferases," capped by a small **hood domain unique to the APRTases**, with catalytic sites at/near the subunit interface [PMID: 12171925](https://pubmed.ncbi.nlm.nih.gov/12171925/): "Giardia APRTase is a symmetric homodimer with the monomers built around Rossman fold cores, an element common to all known purine phosphoribosyltransferases. The catalytic sites are capped with a small hood domain that is unique to the APRTases."
- **PPi-binding chemistry:** A non-proline *cis*-peptide bond forms the pyrophosphate-binding site upon Mg-PRPP binding, and "the pyrophosphoryl charge is neutralized by a single Mg2+ ion and Arg(63), in contrast to the hypoxanthine-guanine phosphoribosyltransferases, which use two Mg2+ ions" [PMID: 12171925](https://pubmed.ncbi.nlm.nih.gov/12171925/). This single-Mg²⁺/Arg mechanism is a defining feature separating APRT from HGPRT.
- **Catalytic base:** A conserved active-site glutamate (Glu100 in *Giardia*, Glu104 in human) functions as the general acid/base. Structural work proposes "the role of Glu104 as the residue that abstracts the proton of adenine N9 atom before its nucleophilic attack on the PRPP anomeric carbon" [PMID: 18399692](https://pubmed.ncbi.nlm.nih.gov/18399692/).
- **Substrate binding order & transition state:** PRPP binds first and AMP leaves last [PMID: 14726202](https://pubmed.ncbi.nlm.nih.gov/14726202/); the reaction proceeds via a **dissociative, oxocarbenium-ion-like transition state** with a flexible catalytic loop closing over the active site during turnover, a paradigm supported by transition-state analysis of related phosphoribosyltransferases [PMID: 28872824](https://pubmed.ncbi.nlm.nih.gov/28872824/).

Because this is a soluble metabolic housekeeping enzyme with no signal peptide or membrane-spanning region, its site of action is the **cytoplasm**, where PRPP, adenine, and Mg²⁺ are available.

> **Evidence quality:** High. Three independent crystal structures across divergent organisms converge on the same architecture and mechanism.

### Finding 4 — Physiological role: adenine salvage into AMP; loss confers resistance to toxic adenine analogs

Classic *Escherichia coli* K-12 genetics directly establishes the in vivo physiological role. In *E. coli*, "Two pathways of adenine utilization are only known in Escherichia coli K-12: the conversion to adenosine monophosphate by adenine phosphoribosyltransferase (apt gene) and ribosylation to adenine nucleosides by purine nucleoside phosphorylase (deoD gene)" [PMID: 6809533](https://pubmed.ncbi.nlm.nih.gov/6809533/). APRT is thus one of only two routes by which a cell assimilates exogenous adenine, and the only route that directly yields a nucleotide.

Genetic mapping placed *apt* between *proC* and *purE*, and showed that *apt* mutations block growth of purine auxotrophs (*pur* mutants) on adenine — and, in *pur pup* backgrounds, on purine ribonucleosides — with the degree of blocking scaling with residual APRT activity.

Crucially, loss-of-function *apt* mutations confer **resistance to the toxic adenine analogs 2,6-diaminopurine (DAP) and 6-methylpurine (MP)** because APRT activates these analogs into cytotoxic nucleotides: "Independently obtained mutations (apt) of resistance to DAP (2,6-diaminopurine) and MP (6-methylpurine), that affect adenine phosphoribosyltransferase (APRT) in Escherichia coli" [PMID: 348574](https://pubmed.ncbi.nlm.nih.gov/348574/). This gain-of-resistance-on-loss phenotype is a hallmark of salvage enzymes that inadvertently activate substrate mimics, and it is the classic genetic handle used to isolate *apt* mutants. Complementary work confirmed that *pur apt* mutants fail to grow on DAP as sole purine source [PMID: 334631](https://pubmed.ncbi.nlm.nih.gov/334631/).

> **Evidence quality:** High for the enzyme class (direct *E. coli* genetics); inferred for *P. putida* by orthology.

### Finding 5 — APRT recycles adenine generated by MTAN, linking it to polyamine synthesis, methylation, and quorum sensing

APRT does not act in isolation — a major endogenous source of the free adenine it salvages is the **MTAN (5′-methylthioadenosine/S-adenosylhomocysteine nucleosidase)** reaction. MTAN irreversibly hydrolyzes the N-ribosidic bond of two key metabolites:

- **MTA (5′-methylthioadenosine)** — a byproduct of spermidine/polyamine biosynthesis
- **SAH (S-adenosylhomocysteine)** — a byproduct of SAM-dependent methylation reactions and of autoinducer (AI-2) synthesis in quorum sensing

Each hydrolysis releases **adenine** plus the corresponding thioribose (5-methylthioribose or S-ribosylhomocysteine). This adenine is then returned to the nucleotide pool by APRT. The MTAN literature states this coupling explicitly: MTAN "is therefore involved in quorum sensing, recycling MTA from the polyamine pathway via adenine phosphoribosyltransferase and recycling MTR to methionine" [PMID: 15749708](https://pubmed.ncbi.nlm.nih.gov/15749708/).

MTAN "plays a central role in three essential metabolic pathways in bacteria: methionine salvage, purine salvage, and polyamine biosynthesis" [PMID: 20954236](https://pubmed.ncbi.nlm.nih.gov/20954236/). APRT provides the **terminal purine-recycling step** downstream of MTAN, keeping these fluxes running and preventing the accumulation of adenine, which could feedback-inhibit upstream reactions. This is the most specific, non-pleiotropic pathway context for *apt*: it is the downstream metabolic partner of MTAN.

> **Evidence quality:** High for the MTAN→APRT coupling in bacteria generally; the *P. putida* MTAN/polyamine pathways are present but the coupling has not been experimentally traced in this organism.

### Finding 6 — *apt* is a dispensable (non-essential) salvage enzyme in *P. putida* KT2440, which retains de novo purine biosynthesis

*P. putida* KT2440 grows on glucose minimal medium, which requires an operative **de novo purine biosynthesis** pathway (synthesizing IMP → AMP/GMP from simple precursors). When de novo synthesis supplies AMP, the salvage enzyme APRT is not required for viability. A genome-wide **mini-Tn5 transposon conditional-essentiality screen** on glucose minimal medium — which rescued 48 conditionally essential knockouts and cross-checked results against an in silico model predicting 68 essential genes — did **not** identify *apt*/PP_4266 among essential or conditionally essential genes [PMID: 20158506](https://pubmed.ncbi.nlm.nih.gov/20158506/): "a genome-wide collection of single-gene P. putida KT2440 knockouts was generated by mini-Tn5 transposon mutagenesis and used to identify genes essential for growth in minimal medium with glucose."

This is fully consistent with salvage-enzyme biochemistry: APRT's phenotype manifests only under purine limitation, when de novo synthesis is blocked, or through activation of toxic adenine analogs. Its non-essentiality does not diminish its physiological importance for energy-efficient nucleotide recycling, but it defines its role as auxiliary/optimizing rather than obligatory.

> **Evidence quality:** Moderate-to-high — direct genome-wide data in the target organism, though absence-of-essentiality is inferential (the screen documents the essential set; *apt* is not in it).

---

## Mechanistic Model / Interpretation

APRT sits at a well-defined node in purine and methyl-cycle metabolism. The integrated model is:

```
   POLYAMINE SYNTHESIS          SAM-DEPENDENT METHYLATION / QUORUM SENSING
   (spermidine)                 (methyltransferases, AI-2 synthesis)
        │                                     │
        ▼                                     ▼
       MTA                                   SAH
        │                                     │
        └──────────────► MTAN ◄───────────────┘
                          │  (irreversible N-ribosidic hydrolysis)
                          ▼
                     free ADENINE  ◄──── exogenous adenine uptake
                          │
                          │  + PRPP + Mg²⁺
                          ▼
                    ╔═══════════════╗
                    ║  APRT (apt,   ║   general-base Glu deprotonates N9;
                    ║   PP_4266)    ║   single Mg²⁺ + Arg neutralize PPi;
                    ║  EC 2.4.2.7   ║   dissociative oxocarbenium-like TS
                    ╚═══════════════╝
                          │
                          ▼
                    AMP  +  PPi   ──►  adenylate/energy pool (ADP, ATP)

   Parallel/independent supply:  de novo purine biosynthesis ──► IMP ──► AMP
   (makes APRT dispensable for viability on minimal medium)
```

**Reaction chemistry (subunit level).** Each of the two identical active sites in the homodimer operates by an ordered pathway: PRPP binds first and stabilizes the catalytically competent conformation; a non-proline *cis*-peptide creates the pyrophosphate pocket; a single Mg²⁺ ion together with a conserved arginine neutralizes the developing negative charge on the leaving pyrophosphate; the conserved active-site glutamate abstracts the proton from adenine N9; and the resulting nucleophile attacks the anomeric (C1′) carbon of the ribose through a dissociative, oxocarbenium-ion-like transition state, forming the β-N9-glycosidic bond of AMP. Substrate selection for adenine over 6-oxopurines occurs upstream of chemistry, via the N–H···N1 hydrogen bond from the rigid base-binding loop.

**Substrate specificity summary:**

| Property | Value / assignment | Source |
|---|---|---|
| Purine base substrate | Adenine (6-aminopurine) only | [PMID: 29694705](https://pubmed.ncbi.nlm.nih.gov/29694705/) |
| Ribose-phosphate donor | PRPP (5-phospho-α-D-ribose-1-diphosphate) | [PMID: 12171924](https://pubmed.ncbi.nlm.nih.gov/12171924/) |
| Metal cofactor | Single Mg²⁺ | [PMID: 12171925](https://pubmed.ncbi.nlm.nih.gov/12171925/) |
| Products | AMP + PPi | [PMID: 12171924](https://pubmed.ncbi.nlm.nih.gov/12171924/) |
| Directionality | Forward (synthesis) favored >100-fold | [PMID: 12171924](https://pubmed.ncbi.nlm.nih.gov/12171924/) |
| Kinetic mechanism | Random Bi-Bi | [PMID: 12171924](https://pubmed.ncbi.nlm.nih.gov/12171924/) |
| Toxic analog substrates | 2,6-diaminopurine, 6-methylpurine (activated to toxic nucleotides) | [PMID: 348574](https://pubmed.ncbi.nlm.nih.gov/348574/) |

**Localization.** APRT is a soluble **cytoplasmic** enzyme (no signal peptide, no transmembrane region; substrates PRPP, adenine, and Mg²⁺ are cytoplasmic). It carries out its function inside the cell, feeding the intracellular adenylate pool.

**Pathway placement and energetics.** APRT is the single, committed step of adenine salvage. Its importance is set by demand: salvaging one adenine to AMP costs one PRPP, far cheaper than de novo synthesis of a purine ring (which consumes multiple ATP, glutamine, glycine, formyl-tetrahydrofolate, and aspartate). PRPP is a shared currency also feeding de novo purine/pyrimidine synthesis, histidine and tryptophan biosynthesis, and NAD salvage, so APRT competes for the cellular PRPP pool. In *P. putida*, which grows well on minimal medium via de novo synthesis, APRT is an efficiency/recycling enzyme rather than a survival-critical one — hence its dispensability.

---

## Evidence Base

| PMID | Title (abbreviated) | Role in this report |
|---|---|---|
| [12171924](https://pubmed.ncbi.nlm.nih.gov/12171924/) | *G. lamblia* APRT unique reaction mechanism & substrate binding | Kinetic parameters, random Bi-Bi mechanism, directionality → **F1** |
| [29694705](https://pubmed.ncbi.nlm.nih.gov/29694705/) | *F. tularensis* APRT structures; N–H···N1 specificity | Adenine-vs-6-oxopurine discrimination; F23A mutagenesis; salvage role → **F1, F2** |
| [12171925](https://pubmed.ncbi.nlm.nih.gov/12171925/) | Closed-site complexes of *Giardia* APRT | Homodimer, Rossmann fold + hood domain, single Mg²⁺/Arg63 PPi chemistry → **F3** |
| [18399692](https://pubmed.ncbi.nlm.nih.gov/18399692/) | Human APRT structural complexes | Glu104 as general base abstracting adenine N9 proton → **F3** |
| [14726202](https://pubmed.ncbi.nlm.nih.gov/14726202/) | *L. tarentolae* APRT structure | Substrate order (PRPP first, AMP last), type I PRTase mechanism → **F3** |
| [6809533](https://pubmed.ncbi.nlm.nih.gov/6809533/) | *E. coli* K-12 adenine assimilation pathways | *apt*/APRT as one of two adenine-utilization routes; AMP formation → **F4** |
| [348574](https://pubmed.ncbi.nlm.nih.gov/348574/) | *apt* mutations conferring DAP/MP resistance | APRT activates toxic adenine analogs; loss → resistance → **F4** |
| [334631](https://pubmed.ncbi.nlm.nih.gov/334631/) | Genetic control of DAP assimilation in *E. coli* | *pur apt* fails to grow on DAP; corroborates salvage role → **F4** |
| [15749708](https://pubmed.ncbi.nlm.nih.gov/15749708/) | Femtomolar MTAN inhibitors | Explicit MTAN→APRT recycling of MTA/polyamine-derived adenine → **F5** |
| [20954236](https://pubmed.ncbi.nlm.nih.gov/20954236/) | *H. pylori* MTAN active-site rearrangements | MTAN central to methionine/purine salvage + polyamine synthesis → **F5** |
| [20158506](https://pubmed.ncbi.nlm.nih.gov/20158506/) | Conditionally essential genes in *P. putida* KT2440 | Genome-wide essentiality screen; *apt* not essential → **F6** |

**Supporting context (not primary evidence):** Structural work on related type I PRTases — human nicotinic acid PRTase [PMID: 26042198](https://pubmed.ncbi.nlm.nih.gov/26042198/), *B. subtilis* xanthine PRTase [PMID: 16716072](https://pubmed.ncbi.nlm.nih.gov/16716072/), ATP-PRTase transition-state analysis [PMID: 28872824](https://pubmed.ncbi.nlm.nih.gov/28872824/) — reinforces the dissociative-transition-state model and the family-wide "PRPP binds first at a dimer interface" theme. MTAN transition-state and inhibitor studies [PMID: 16128565](https://pubmed.ncbi.nlm.nih.gov/16128565/), [PMID: 27019223](https://pubmed.ncbi.nlm.nih.gov/27019223/), [PMID: 15122881](https://pubmed.ncbi.nlm.nih.gov/15122881/) corroborate the upstream adenine-generating chemistry. A recent bacterial APRT structure — *Fusobacterium nucleatum* FnAPRT, which captured **ligand-induced conformational changes** on binding the products AMP and phosphate [PMID: 41588988](https://pubmed.ncbi.nlm.nih.gov/41588988/) — confirms the closing-loop/product-recognition model in a bacterial APRT, strengthening orthology transfer to *P. putida*.

**How the evidence converges vs. challenges the annotation:** No reviewed paper challenges the assignment. All lines of evidence — sequence motifs in Q88F33, three independent crystal structures across kingdoms, precise enzyme kinetics, and classical bacterial genetics — support the annotation "adenine phosphoribosyltransferase, adenine salvage, cytoplasmic, non-essential." The only genuine gap is the absence of organism-specific (*P. putida*) biochemical characterization.

---

## Supported vs. Refuted Hypotheses

- **Supported:** *apt*/PP_4266 encodes adenine phosphoribosyltransferase catalyzing adenine + PRPP → AMP + PPi (EC 2.4.2.7); it is a Mg²⁺-dependent, homodimeric, cytoplasmic type I PRTase; substrate specificity for adenine is structurally hard-wired via the base-binding loop N–H···N1 contact; it functions in adenine salvage, activates toxic adenine analogs, and is the terminal purine-recycling partner of MTAN; it is non-essential in KT2440 under standard growth.
- **Refuted / excluded:** APRT is *not* a 6-oxopurine salvage enzyme (guanine/hypoxanthine/xanthine are handled by HGPRT/XPRT); it is not membrane-associated; it does not participate in *de novo* purine ring synthesis; it is not essential for viability on glucose minimal medium.

---

## Limitations and Knowledge Gaps

1. **No *P. putida*-specific experimental data.** There is no published crystal structure, kinetic characterization, or knockout phenotype study for the PP_4266 gene product itself. All mechanistic and kinetic detail is transferred by orthology from human, *Giardia*, *Leishmania*, *Francisella*, and *Fusobacterium* enzymes. Given the high conservation of APRT and the HAMAP rule assignment, this transfer is reliable, but organism-specific kinetic constants (*K*ₘ, *k*cat) for the *P. putida* enzyme are unknown.

2. **Essentiality is inferred from absence in a screen.** Finding 6 rests on *apt* not appearing among essential/conditionally essential genes in a mini-Tn5 screen. Transposon screens can miss genes due to insertion-site bias or redundancy, so "non-essential on glucose minimal medium" is well-supported but a dedicated clean-deletion phenotype under purine-limited conditions would be more definitive.

3. **MTAN→APRT coupling not directly traced in *P. putida*.** The coupling is firmly established in *E. coli* and other bacteria and the relevant pathways (polyamine synthesis, SAM methylation, MTAN) exist in *P. putida*, but the specific metabolic flux from MTAN-derived adenine through PP_4266 has not been experimentally measured in this organism.

4. **Regulation unknown.** Whether *apt* expression in *P. putida* is constitutive or regulated (e.g., by purine availability, PurR-type repression, or growth phase), and whether APRT activity is allosterically modulated, has not been characterized here.

5. **Kinetic parameters are from a divergent eukaryote.** The quantitative kinetics (Finding 1) come from *G. lamblia*; absolute values likely differ for the bacterial enzyme, though the qualitative mechanism (random Bi-Bi, forward-favored, Mg²⁺-dependent) is conserved.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant expression and kinetic characterization** of PP_4266. Clone, His-tag, and purify the *P. putida* APRT; determine *K*ₘ/*k*cat for adenine and PRPP, Mg²⁺ dependence, and pH optimum, replacing orthology-inferred parameters with organism-specific values.

2. **Substrate-specificity panel.** Assay the purified enzyme against adenine, 2,6-diaminopurine, 6-methylpurine, and 6-oxopurines (hypoxanthine, guanine) to confirm strict 6-aminopurine specificity and quantify analog activation.

3. **Clean deletion phenotyping.** Construct an unmarked ΔPP_4266 strain and test growth on (i) glucose minimal medium (expected: no defect), (ii) purine-limited / de novo-blocked conditions with adenine as sole purine source (expected: defect), and (iii) media containing DAP or 6-methylpurine (expected: resistance vs. sensitive wild type). This directly validates Findings 4 and 6 in the target organism.

4. **MTAN–APRT flux tracing.** Use ¹³C/¹⁵N-labeled MTA or SAH with metabolomics/isotope tracing in wild-type vs. ΔPP_4266 to confirm that MTAN-derived adenine is recycled into AMP via APRT in *P. putida*, testing Finding 5 in situ.

5. **Structure determination.** Solve the crystal (or high-confidence AlphaFold) structure — apo, PRPP-bound, and AMP-bound — of *P. putida* APRT to confirm the homodimer, hood domain, catalytic loop closure, the base-binding loop N–H···N1 contact, and the identity of the general-base glutamate and Mg²⁺/Arg pyrophosphate site.

6. **Expression/regulation analysis.** RT-qPCR or RNA-seq of *apt* under purine-replete vs. purine-limited growth, and in stationary vs. exponential phase, to determine whether salvage capacity is regulated.

---

## Conclusion

*apt* (PP_4266; Q88F33) of *Pseudomonas putida* KT2440 encodes **adenine phosphoribosyltransferase (APRT, EC 2.4.2.7)**, a cytoplasmic, Mg²⁺-dependent, homodimeric type I purine phosphoribosyltransferase. Its primary and specific function is to catalyze the committed step of adenine salvage — transfer of a phosphoribosyl group from PRPP to the N9 of adenine to form AMP + pyrophosphate — with strict selectivity for the 6-aminopurine adenine enforced by an N–H···N1 hydrogen bond from a rigid base-binding loop, and with catalysis driven by a conserved general-base glutamate through a dissociative transition state. Biologically, it is the terminal recycling node that returns free adenine — including adenine released by MTAN from the polyamine, methylation, and quorum-sensing branches of sulfur/methyl metabolism — to the adenylate pool. In *P. putida* KT2440, which retains de novo purine biosynthesis, APRT is a dispensable, energy-saving salvage enzyme whose phenotype emerges only under purine limitation or through activation of, and hence resistance to, toxic adenine analogs.


## Artifacts

- [OpenScientist final report](apt-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](apt-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:12171924
2. PMID:29694705
3. PMID:18399692
4. PMID:14726202
5. PMID:12171925
6. PMID:28872824
7. PMID:6809533
8. PMID:15749708
9. PMID:20954236
10. PMID:20158506
11. PMID:26042198
12. PMID:16716072
13. PMID:16128565
14. PMID:27019223
15. PMID:15122881
16. PMID:41588988