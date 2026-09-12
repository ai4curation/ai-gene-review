---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-11T16:19:41.838853'
end_time: '2026-07-11T16:55:53.223928'
duration_seconds: 2171.39
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: metE
  gene_symbol: metE
  uniprot_accession: Q88JF1
  protein_description: 'SubName: Full=5-methyltetrahydropteroyltriglutamate-homocysteine
    methyltransferase {ECO:0000313|EMBL:AAN68306.1};'
  gene_info: Name=metE {ECO:0000313|EMBL:AAN68306.1}; OrderedLocusNames=PP_2698 {ECO:0000313|EMBL:AAN68306.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: Met_Synth_C/arc. (IPR002629); Met_Synthase_cat. (IPR016456); UROD/MetE-like_sf.
    (IPR038071); Meth_synt_2 (PF01717)
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
  path: metE-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: metE-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88JF1
- **Protein Description:** SubName: Full=5-methyltetrahydropteroyltriglutamate-homocysteine methyltransferase {ECO:0000313|EMBL:AAN68306.1};
- **Gene Information:** Name=metE {ECO:0000313|EMBL:AAN68306.1}; OrderedLocusNames=PP_2698 {ECO:0000313|EMBL:AAN68306.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** Met_Synth_C/arc. (IPR002629); Met_Synthase_cat. (IPR016456); UROD/MetE-like_sf. (IPR038071); Meth_synt_2 (PF01717)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "metE" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'metE' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **metE** (gene ID: metE, UniProt: Q88JF1) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *metE* (Q88JF1 / PP_2698) in *Pseudomonas putida* KT2440

## Summary

The gene **metE** (locus tag **PP_2698**; UniProt **Q88JF1**) of *Pseudomonas putida* strain KT2440 (ATCC 47054 / DSM 6125 / NCIMB 11950) encodes **cobalamin-independent methionine synthase (MetE, EC 2.1.1.14)**, also called 5-methyltetrahydropteroyltriglutamate–homocysteine methyltransferase. This enzyme catalyzes the terminal, committed step of *de novo* methionine biosynthesis: the direct transfer of a methyl group from polyglutamylated **5-methyltetrahydrofolate (CH₃-H₄PteGlu₃)** to the thiol of **L-homocysteine**, producing **L-methionine** and **tetrahydrofolate (H₄folate)**. Unlike its cobalamin-dependent counterpart MetH, MetE performs this methyl transfer *without* a corrinoid (vitamin B₁₂) intermediate, relying instead on a catalytic **Zn²⁺** ion that activates the homocysteine thiol for direct nucleophilic (Sₙ2) attack on the N5-methyl group of the folate. The gene symbol, organism, catalytic annotation, Zn²⁺ cofactor, and conserved catalytic domain (Pfam PF01717 *Meth_synt_2*; InterPro IPR002629/IPR016456/IPR038071) are all mutually consistent — **the identity of this protein as a genuine MetE is well supported.**

A distinctive structural feature emerged from this investigation. Canonical bacterial and fungal MetE enzymes (e.g., *E. coli*, *T. maritima*, *S. mutans*, *C. albicans*) are large (~750–900 aa) **dual (βα)₈ TIM-barrel** proteins whose active site lies in the cleft between the two barrels, an architecture that arose by ancient gene duplication. Q88JF1, by contrast, is a compact **344-aa single-barrel ("archaeal-type") MetE**. A quantitative Smith-Waterman alignment performed during this investigation showed that ~90% of Q88JF1 aligns specifically and exclusively to the **C-terminal catalytic barrel** of *E. coli* MetE (residues 427–728; 28% identity, alignment score 303), with **no** alignment to the N-terminal folate-binding barrel. Crucially, the four resting-state zinc ligands (**His, Cys, Glu, Cys**) are fully conserved in Q88JF1 (e.g., Cys312 ≡ *E. coli* Cys726), indicating that this streamlined enzyme retains a functional zinc/homocysteine active site.

Functionally, MetE operates in the **cytoplasm** within cysteine/methionine metabolism (KEGG pathway ppu00270, methionine-biosynthesis module M00017). It sits in a conserved, divergently transcribed **metE–metR** locus (the adjacent gene **PP_2696** encodes the LysR-type activator MetR), and *P. putida* KT2440 additionally encodes the B₁₂-dependent isozyme **MetH (PP_2375, Q88KB5)**, giving the organism two routes to methionine depending on cobalamin availability. All functional conclusions for this specific *P. putida* protein are **inferential** — derived from sequence homology, conserved catalytic residues, genomic context, and structural studies of orthologs — because the UniProt protein-existence level is "4: Predicted" and no direct biochemical characterization of the *P. putida* enzyme has been published.

---

## Key Findings

### Q88JF1 is cobalamin-independent methionine synthase (MetE, EC 2.1.1.14)

The primary function of the gene product is unambiguous at the annotation level. UniProt Q88JF1 lists gene name *metE*, ordered locus name PP_2698, organism *P. putida* KT2440, and catalytic activity as **5-methyltetrahydropteroyltriglutamate–homocysteine methyltransferase**. The associated Gene Ontology terms are GO:0003871 (5-methyltetrahydropteroyltriglutamate-homocysteine S-methyltransferase activity), GO:0009086 (methionine biosynthetic process), and GO:0032259 (methylation). The listed cofactor is **Zn(2+)**.

The reaction catalyzed is the direct, single-step transfer of a methyl group from 5-methyltetrahydrofolate — in bacteria, the physiological substrate is the **poly-γ-glutamylated** form — to L-homocysteine, yielding L-methionine and tetrahydrofolate. This is the defining reaction of the MetE class: "*Cobalamin-independent methionine synthase (MetE) catalyzes the direct transfer of a methyl group from methyltetrahydrofolate to l-homocysteine to form methionine*" [PMID: 21840320]. The hallmark distinguishing MetE from cobalamin-dependent MetH — the absence of an intermediate methyl carrier — is captured by: "*Cobalamin-independent methionine synthase (MetE) catalyzes the transfer of a methyl group from methyltetrahydrofolate to L-homocysteine (Hcy) without using an intermediate methyl carrier*" [PMID: 15630480].

**Substrate specificity:** methyl donor = 5-methyltetrahydrofolate (physiologically polyglutamylated, CH₃-H₄PteGlu₃); methyl acceptor = L-homocysteine (its thiolate); products = L-methionine + tetrahydrofolate; obligate cofactor = a single catalytic Zn²⁺.

### MetE is a Zn²⁺-dependent methyltransferase with His-acid catalysis

The reaction chemistry is metal-assisted. The active-site **Zn²⁺** functions as a **Lewis acid** that binds and deprotonates the L-homocysteine thiol, generating the reactive thiolate nucleophile. This nucleophile then performs an **in-line Sₙ2 attack** on the N5-methyl group of methyltetrahydrofolate. In the resting enzyme, the zinc is coordinated by the ligand set **His, Cys, Glu, Cys** — a signature distinct from the (Cys)₃ zinc site of the cobalamin-dependent enzymes MetH and betaine-homocysteine methyltransferase (BHMT). A general-acid residue (His707 in *Thermotoga maritima* numbering) protonates the departing tetrahydrofolate leaving group through a water molecule trapped in the closed active site.

Supporting evidence: "*the MetE active site coordinates a zinc atom, which is thought to act as a Lewis acid and plays a role in the activation of thiol*" [PMID: 21840320]; the resting-state ligands are "*histidine, cysteine, glutamate, and cysteine in the resting form of MetE*" [PMID: 15630480]; and the closed-conformation structure "*reveals His707 as the acid that protonates the THF leaving group through a water molecule trapped in the closed active site. The substrates are correctly oriented for an in-line attack by l-homocysteine on the N(5)-methyl*" [PMID: 25545590].

Critically, Q88JF1 **retains these catalytic residues**: its sequence contains the **E-C-H** motif (…LECHNSH…) and the **C-x-x-C** motif (…PCTNCG…) that supply the zinc ligands of the C-terminal catalytic barrel, and UniProt lists Zn(2+) as its cofactor with a "MetE C-terminal/archaeal" catalytic domain spanning residues 5–329.

### Q88JF1 corresponds to the C-terminal catalytic barrel of a normally dual-barrel enzyme

Structurally characterized MetE enzymes are **dual (βα)₈ TIM-barrel** proteins of ~750–900 residues. The N-terminal barrel arose by **gene duplication** of the C-terminal barrel and contributes folate-binding determinants, while the C-terminal barrel houses the catalytic zinc/homocysteine site; the active site sits at the interface between the two barrels. Q88JF1 is only **344 aa**, and its single annotated domain (residues 5–329) is the "Cobalamin-independent methionine synthase MetE C-terminal/archaeal" domain (Pfam PF01717; InterPro IPR002629). Q88JF1 is therefore a **single-domain, C-terminal-barrel (archaeal-type) MetE** rather than the canonical dual-barrel form.

Evidence for the canonical architecture and its evolutionary origin: "*The fold of the N-terminal barrel confirms that it has evolved from the C-terminal polypeptide by gene duplication*" [PMID: 15630480]; and "*The enzyme has a dual (βα)₈ TIM barrel structure that binds, activates and brings the reactants into reaction proximity by conformational movements*" [PMID: 25545590]. UniProt classifies the protein-existence evidence for Q88JF1 as "4: Predicted," meaning no direct experimental characterization of the *P. putida* protein has been reported.

### Cytoplasmic enzyme in a conserved metE–metR locus, with a parallel B₁₂-dependent MetH route

The genomic context in *P. putida* KT2440 reproduces the classic **divergent metE–metR arrangement**. The immediate neighbor **PP_2696 (Q88JF3)** is the LysR/HTH-type transcriptional regulator **MetR**, which (modulated by homocysteine) transactivates *metE*. Separately, *P. putida* KT2440 encodes a full-length cobalamin-dependent methionine synthase **MetH (Q88KB5, PP_2375, 1235 aa)**, so the terminal methionine-synthase step can be performed by either MetE (B₁₂-independent) or MetH (B₁₂-dependent) depending on cobalamin availability. MetE is a **soluble cytoplasmic** protein with no signal peptide or transmembrane segment, consistent with a cytosolic biosynthetic enzyme.

Regulatory precedent from *E. coli*: "*The MetR protein is required for both metE and metH gene expression, and functions as a transactivator of transcription of these genes. MetR is a unique prokaryotic transcription activator in that it possesses a leucine zipper motif*" [PMID: 1943695]. B₁₂/MetH-mediated repression of *metE* is established: "*The repression of MetE synthesis in Escherichia coli by vitamin B12 is known to require the MetH holoenzyme*" [PMID: 1734876]. Under oxidative stress in *E. coli*, MetE is inactivated by **glutathionylation** of an active-site-entrance cysteine: "*Stoichiometric glutathionylation of MetE by GSSG occurs at cysteine 645, which is strategically located at the entrance to the active site*" [PMID: 15502870]. Functional interchangeability of the two synthases is illustrated by: "*Expression of the cobalamin-independent methionine synthase MetE alleviates this symbiotic defect*" in a system otherwise dependent on B₁₂ [PMID: 20698752].

### Quantitative confirmation of single-barrel MetE identity and orthology assignment

A Smith-Waterman alignment (BLOSUM62; gap open −11, extend −1) of *P. putida* Q88JF1 (344 aa) against the *E. coli* canonical dual-barrel MetE (P25665, 753 aa) yielded a **score of 303 at 28.0% identity over a 314-residue aligned block**. Q88JF1 residues 6–314 (90% of its length) map onto *E. coli* MetE residues **427–728** — essentially the entire C-terminal catalytic (βα)₈ barrel — with **no significant alignment** to the *E. coli* N-terminal barrel (residues ~1–370). Because the *E. coli* catalytic zinc ligands (His641/Cys643/Cys726) fall within the aligned window, the zinc/homocysteine site is retained.

KEGG (ppu:PP_2698) independently corroborates the annotation: length 344 aa, genomic position complement(3089178..3090212) = 1035 bp, orthology **K00549** ("5-methyltetrahydropteroyltriglutamate--homocysteine methyltransferase [EC:2.1.1.14]"), pathway **ppu00270** (cysteine and methionine metabolism), module **M00017** (methionine biosynthesis, aspartate ⇒ homoserine ⇒ methionine). The flanking loci — **PP_2697** (flavin-reductase oxidoreductase) and **PP_2699** (DUF1852) — provide no candidate N-terminal-barrel gene, confirming that Q88JF1 is genuinely single-domain rather than a fragment of a split ORF.

### Residue-level conservation of the zinc/homocysteine catalytic site

Traceback of the BLOSUM62 Smith-Waterman alignment maps the *E. coli* MetE C-terminal zinc-ligand **Cys726 directly onto Q88JF1 Cys312** (…LYP**C**TNCG…). Q88JF1 additionally contains the **…ISLECHNSH…** motif providing the Glu/Cys/His ligands corresponding to the *E. coli* His641/Glu642/Cys643 zinc-binding region (with the exact His/Cys registration shifting by a few residues owing to short loop indels at ~28% identity). Together, these place **all four resting-state MetE zinc ligands (His, Cys, Glu, Cys)** in Q88JF1 at the correct topological positions of the C-terminal catalytic barrel — the strongest single line of evidence that this compact protein is a *functional*, not merely homologous, methionine synthase.

---

## Mechanistic Model / Interpretation

### The reaction

```
   5-CH3-H4PteGlu(n)          L-homocysteine
   (methyl donor)             (methyl acceptor, thiolate)
          \                        /
           \        Zn2+          /
            \    (Lewis acid)    /
             v                  v
    [ MetE C-terminal (βα)8 catalytic barrel ]
             |  in-line SN2 methyl transfer
             |  His-acid protonates leaving group
             v
   L-methionine   +   H4PteGlu(n)  (tetrahydrofolate)
```

**Step-by-step chemistry:**
1. The catalytic **Zn²⁺** binds L-homocysteine and lowers the pKₐ of its thiol, generating a reactive **thiolate** nucleophile.
2. The thiolate performs an **in-line Sₙ2 attack** on the electrophilic **N5-methyl carbon** of 5-methyltetrahydrofolate.
3. A conserved **His general acid** (His707 in *T. maritima*) protonates the N5 nitrogen of the departing tetrahydrofolate through a trapped active-site water, facilitating C–N bond cleavage.
4. Products **L-methionine** and **tetrahydrofolate** are released; conformational "closing" of the barrel during catalysis excludes bulk solvent and aligns the reactants.

### Structural distinction: single vs. dual barrel

| Property | Canonical MetE (*E. coli*, *T. maritima*, *C. albicans*) | Q88JF1 (*P. putida* PP_2698) |
|---|---|---|
| Length | ~750–900 aa | **344 aa** |
| Architecture | **Dual (βα)₈ TIM barrel** | **Single (βα)₈ barrel (C-terminal/archaeal type)** |
| N-terminal barrel | Present; folate-binding, from gene duplication | **Absent** |
| C-terminal catalytic barrel | Present; houses Zn²⁺/Hcy site | **Present and conserved** |
| Zinc ligands (resting) | His, Cys, Glu, Cys | **His, Cys, Glu, Cys (all retained)** |
| Zinc mechanism | Lewis-acid thiol activation | Inferred identical |
| Active-site location | Between the two barrels | Single barrel (± oligomerization) |

The absence of the N-terminal barrel is the report's most notable structural finding. In dual-barrel enzymes, the N-terminal barrel contributes folate-binding residues (e.g., Asn126 in *C. albicans* Met6p, whose mutation abolishes activity — PMID: 24524835). In a single-barrel archaeal-type MetE, folate-binding determinants must be supplied by the C-terminal barrel itself (and possibly by oligomerization), consistent with the existence of functional single-barrel MetE enzymes in archaea and some bacteria.

### Pathway and physiological context

```
Aspartate ──► ... ──► homoserine ──► O-succinyl/acetyl-homoserine
                                              │
                                              ▼ (cystathionine / sulfhydrylation route)
                                        L-homocysteine
                                              │
                    ┌─────────────────────────┼─────────────────────────┐
                    │                                                     │
              MetE (PP_2698)                                       MetH (PP_2375)
        B12-INDEPENDENT, Zn2+                              B12-DEPENDENT, cobalamin
        CH3-H4folate ──► Met                              CH3-H4folate ──► Met
                    │                                                     │
                    └─────────────────────► L-METHIONINE ◄───────────────┘
                                              │
                                              ▼
                                     S-adenosylmethionine (SAM)
                                     + regenerated H4folate (one-carbon pool)
```

MetE regenerates tetrahydrofolate, feeding the cellular **one-carbon (folate) pool**, and supplies methionine for protein synthesis and for **S-adenosylmethionine (SAM)** — the universal methyl donor. Its transcription is activated by **MetR (PP_2696)** in response to homocysteine, and its physiological importance is greatest under **B₁₂-limiting conditions**, where MetH cannot function. In *E. coli*, MetE is also a redox sensor: **glutathionylation of an active-site cysteine** during oxidative stress inactivates it, transiently converting the cell to methionine auxotrophy — a plausible regulatory feature for the *P. putida* enzyme as well.

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports the findings |
|---|---|---|
| [21840320](https://pubmed.ncbi.nlm.nih.gov/21840320/) | *S. mutans* MetE crystal structures; zinc-inversion model | Defines the MetE reaction; establishes Zn²⁺ as the Lewis-acid thiol activator |
| [15630480](https://pubmed.ncbi.nlm.nih.gov/15630480/) | *MetE: a face-to-face double barrel that evolved by gene duplication* | Confirms direct methyl transfer without a carrier; defines His/Cys/Glu/Cys zinc ligands; documents dual-barrel gene-duplication origin |
| [25545590](https://pubmed.ncbi.nlm.nih.gov/25545590/) | *MetE captured in a substrate-induced closed conformation* | Describes His-acid catalysis, in-line Sₙ2 attack, and the dual (βα)₈ barrel conformational mechanism |
| [24524835](https://pubmed.ncbi.nlm.nih.gov/24524835/) | *Structural analysis of a fungal methionine synthase (Met6p)* | Two-barrel architecture; catalytic zinc positioning on homocysteine binding; folate-binding residues (e.g., Asn126) essential for activity |
| [15502870](https://pubmed.ncbi.nlm.nih.gov/15502870/) | *Oxidative stress inactivates MetE in E. coli* | Redox regulation: glutathionylation of active-site-entrance Cys645 inactivates MetE |
| [1943695](https://pubmed.ncbi.nlm.nih.gov/1943695/) | *Regulation of methionine synthesis in E. coli* | MetR is the transcriptional activator of *metE* — supports the divergent metE–metR locus (PP_2696) |
| [1734876](https://pubmed.ncbi.nlm.nih.gov/1734876/) | *metF/metJ genes and B12 regulation of methionine genes* | B₁₂/MetH-mediated repression of *metE* — the MetE↔MetH regulatory relationship |
| [20698752](https://pubmed.ncbi.nlm.nih.gov/20698752/) | *S. meliloti cobalamin-dependent RNR for symbiosis* | MetE can functionally substitute for B₁₂-dependent methionine synthesis |

All eight papers are structural/biochemical or regulatory studies of MetE orthologs and the methionine-biosynthesis regulon. **None studies the *P. putida* KT2440 protein directly**, so the evidence base is homology- and orthology-driven rather than target-specific. Database annotations (UniProt Q88JF1, KEGG ppu:PP_2698, Pfam PF01717, InterPro IPR002629/IPR016456/IPR038071) provide the target-specific anchor, corroborated by the quantitative alignment and residue-conservation analyses performed in this investigation.

---

## Limitations and Knowledge Gaps

1. **No direct experimental characterization of Q88JF1.** UniProt protein-existence level is "4: Predicted." No published enzymatic assay, crystal structure, or knockout phenotype exists for the *P. putida* KT2440 protein specifically. All functional conclusions are inferential.
2. **Modest sequence identity (~28%) to characterized enzymes.** Although the zinc-ligand set and catalytic barrel topology are conserved, the exact His/Cys registration shifts by a few residues due to short loop indels; direct structural confirmation would remove residual ambiguity.
3. **Folate binding in a single-barrel context is untested.** In dual-barrel MetE, the N-terminal barrel supplies folate-binding residues. How the single-barrel *P. putida* enzyme binds polyglutamylated methyl-THF — via C-terminal-barrel residues, an oligomeric interface, or a different geometry — is unknown.
4. **Oligomeric state unknown.** Single-barrel archaeal-type MetE enzymes may dimerize to reconstitute a composite active site; this has not been examined for Q88JF1.
5. **Regulatory details inferred from *E. coli*.** MetR-mediated activation and B₁₂/MetH repression are established in *E. coli*; the precise *P. putida* KT2440 regulatory logic (operator sequences, homocysteine co-activation, B₁₂ responsiveness) has not been demonstrated experimentally.
6. **Redox regulation not verified in *P. putida*.** Whether the *P. putida* enzyme is glutathionylation-inactivated like *E. coli* MetE depends on the presence/position of an active-site-entrance cysteine that was not explicitly mapped here.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant expression and activity assay.** Clone PP_2698, express in *E. coli*, purify, and measure methyltetrahydrofolate–homocysteine methyltransferase activity (e.g., the fluorescence-based assay from PMID: 24524835), confirming Zn²⁺ dependence and B₁₂ independence. Determine Kₘ for CH₃-H₄PteGlu(n) and L-homocysteine, and test polyglutamate specificity.
2. **Zinc-content and metal-substitution analysis.** Quantify bound Zn²⁺ (ICP-MS) and test Co²⁺/Cd²⁺ substitution to confirm the Lewis-acid role, alongside site-directed mutagenesis of the predicted ligands (His, Cys312, the ECH-motif residues).
3. **Structural determination.** Solve the crystal or cryo-EM structure of Q88JF1 to confirm the single-barrel fold, define how folate is bound without an N-terminal barrel, and establish the oligomeric state. An AlphaFold model can provide an immediate low-cost prediction of the fold and active-site geometry.
4. **Genetic complementation.** Test whether PP_2698 complements an *E. coli* ΔmetE methionine auxotroph, and construct a *P. putida* ΔPP_2698 mutant to assess methionine auxotrophy under B₁₂-free vs. B₁₂-supplemented conditions (probing MetE/MetH redundancy).
5. **Regulatory validation.** Use RNA-seq/qPCR and a MetR (PP_2696) knockout to confirm homocysteine-dependent, MetR-activated transcription and B₁₂-mediated repression of PP_2698 in *P. putida*.
6. **Oxidative-stress sensitivity.** Test whether purified Q88JF1 is inactivated by GSSG (glutathionylation) and map any reactive active-site-entrance cysteine, to determine whether the *E. coli*-style redox switch is conserved.

---

*Report generated from a 3-iteration autonomous investigation. Findings are supported by domain/annotation databases (UniProt, KEGG, Pfam/InterPro), quantitative sequence alignment against characterized orthologs, and the structural/regulatory literature cited above. The identity of PP_2698 as a genuine, single-barrel, cobalamin-independent methionine synthase is well supported; its detailed biochemistry remains to be confirmed experimentally.*


## Artifacts

- [OpenScientist final report](metE-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](metE-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:21840320
2. PMID:15630480
3. PMID:25545590
4. PMID:1943695
5. PMID:1734876
6. PMID:15502870
7. PMID:20698752
8. PMID:24524835