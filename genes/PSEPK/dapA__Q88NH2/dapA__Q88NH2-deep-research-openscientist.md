---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-17T13:44:40.268367'
end_time: '2026-07-17T14:06:01.675685'
duration_seconds: 1281.41
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: dapA__Q88NH2
  gene_symbol: dapA
  uniprot_accession: Q88NH2
  protein_description: 'RecName: Full=4-hydroxy-tetrahydrodipicolinate synthase {ECO:0000256|ARBA:ARBA00012086,
    ECO:0000256|HAMAP-Rule:MF_00418}; Short=HTPA synthase {ECO:0000256|HAMAP-Rule:MF_00418};
    EC=4.3.3.7 {ECO:0000256|ARBA:ARBA00012086, ECO:0000256|HAMAP-Rule:MF_00418};'
  gene_info: Name=dapA {ECO:0000256|HAMAP-Rule:MF_00418}; Synonyms=dapA-I {ECO:0000313|EMBL:AAN66861.1};
    OrderedLocusNames=PP_1237 {ECO:0000313|EMBL:AAN66861.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the DapA family. {ECO:0000256|ARBA:ARBA00007592,
  protein_domains: Aldolase_TIM. (IPR013785); DapA. (IPR005263); DapA-like. (IPR002220);
    Schiff_base-form_aldolases_AS. (IPR020625); Schiff_base-form_aldolases_CS. (IPR020624)
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
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: dapA__Q88NH2-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: dapA__Q88NH2-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88NH2
- **Protein Description:** RecName: Full=4-hydroxy-tetrahydrodipicolinate synthase {ECO:0000256|ARBA:ARBA00012086, ECO:0000256|HAMAP-Rule:MF_00418}; Short=HTPA synthase {ECO:0000256|HAMAP-Rule:MF_00418}; EC=4.3.3.7 {ECO:0000256|ARBA:ARBA00012086, ECO:0000256|HAMAP-Rule:MF_00418};
- **Gene Information:** Name=dapA {ECO:0000256|HAMAP-Rule:MF_00418}; Synonyms=dapA-I {ECO:0000313|EMBL:AAN66861.1}; OrderedLocusNames=PP_1237 {ECO:0000313|EMBL:AAN66861.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the DapA family. {ECO:0000256|ARBA:ARBA00007592,
- **Key Domains:** Aldolase_TIM. (IPR013785); DapA. (IPR005263); DapA-like. (IPR002220); Schiff_base-form_aldolases_AS. (IPR020625); Schiff_base-form_aldolases_CS. (IPR020624)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "dapA" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'dapA' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **dapA** (gene ID: dapA__Q88NH2, UniProt: Q88NH2) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of *dapA* (Q88NH2, PP_1237) in *Pseudomonas putida* KT2440

**Gene / protein:** *dapA* (synonym *dapA-I*; ordered locus PP_1237)
**UniProt:** Q88NH2
**Protein:** 4-hydroxy-tetrahydrodipicolinate synthase (HTPA synthase; classically "dihydrodipicolinate synthase", DHDPS), **EC 4.3.3.7** (formerly EC 4.2.1.52)
**Organism:** *Pseudomonas putida* strain KT2440 (ATCC 47054 / DSM 6125)
**Family:** DapA family; Aldolase_TIM fold (InterPro IPR013785, IPR005263, IPR002220, IPR020624/IPR020625)
**Length:** 295 aa

---

## 1. Summary (answer to the research question)

Q88NH2 is a **cytoplasmic biosynthetic aldolase-type lyase** that catalyzes the **first committed step of the diaminopimelate (DAP) / L‑lysine branch of the aspartate amino-acid pathway**. It condenses **pyruvate** with **L‑aspartate‑4‑semialdehyde (ASA)** to form **(4S)‑4‑hydroxy‑2,3,4,5‑tetrahydro‑(2S)‑dipicolinate (HTPA)**, the committed precursor of both *meso*-diaminopimelate (a cross-linking residue of Gram-negative peptidoglycan) and L‑lysine. Catalysis proceeds through a Schiff-base (ping-pong) mechanism using a strictly conserved active-site lysine; the enzyme is a homotetramer of (β/α)₈ TIM-barrel subunits with active sites built across a tight-dimer interface. The gene product is a soluble cytoplasmic enzyme. Its identity as a *bona fide* DapA-family enzyme is directly supported by the presence of the PROSITE Schiff-base-forming aldolase signature and the catalytic lysine in the Q88NH2 sequence.

The gene symbol is **unambiguous and consistent** with the UniProt description: "*dapA*" here denotes the canonical DHDPS/HTPA-synthase, and the domain architecture, family membership, and conserved catalytic motifs all align with the extensive DHDPS literature. Note that most detailed biochemistry comes from orthologs (*E. coli*, *M. tuberculosis*, *B. anthracis*, *C. jejuni*, plants); direct experimental characterization of the *P. putida* KT2440 enzyme itself is limited, so organism-specific kinetic/regulatory details below are **inferred from family conservation and sequence analysis**.

---

## 2. Primary function: the reaction catalyzed and substrate specificity

**Reaction (EC 4.3.3.7):**

> pyruvate + L‑aspartate‑4‑semialdehyde → (4S)‑4‑hydroxy‑2,3,4,5‑tetrahydro‑(2S)‑dipicolinate (HTPA) + H₂O

DapA "converts pyruvate and L‑aspartate‑4‑semialdehyde to 4‑hydroxy‑2,3,4,5‑tetrahydrodipicolinic acid" in a multistep reaction (Schmitz et al., 2020, PMID 32356521). Historically the enzyme was named dihydrodipicolinate synthase and assigned EC 4.2.1.52 on the assumption that the product was 2,3‑dihydrodipicolinate; it is now recognized that the direct enzymatic product is the cyclic **hydroxy‑tetrahydrodipicolinate (HTPA)**, and that conversion to dihydrodipicolinate occurs subsequently (spontaneous dehydration and/or the action of the next enzyme DapB). Hence the modern name/EC (4‑hydroxy‑tetrahydrodipicolinate synthase, EC 4.3.3.7). The two substrates are highly specific: the **keto-donor is pyruvate** (which forms the covalent Schiff-base intermediate) and the **aldehyde acceptor is L‑aspartate‑4‑semialdehyde**. Reported bacterial kinetics are in the sub-millimolar to low-millimolar K_M range (e.g., *M. tuberculosis*: K_M^ASA ≈ 0.43 mM, K_M^pyruvate ≈ 0.17 mM; Kefala et al., 2008, PMID 18062777).

**Biological role of the product:** DHDPS "catalyses the first committed step in the biosynthetic pathway yielding two essential bacterial metabolites, *meso*-diaminopimelate (DAP) and (S)-lysine" (Domigan et al., 2009, PMID 19595801) — i.e., HTPA is the branch-point precursor that ultimately gives *meso*-DAP (peptidoglycan cross-link) and L-lysine (protein synthesis).

---

## 3. Catalytic mechanism

DHDPS is a **class I (Schiff-base) aldolase-type lyase** operating by a **ping-pong** kinetic mechanism (Skovpen & Palmer, 2013, PMID 23902434):

1. **Pyruvate binds first** and forms a **Schiff base (imine)** with the ε-amino group of a strictly conserved active-site lysine. Crystallography of the *M. tuberculosis* ortholog captured the enzyme "in complex with its substrate, pyruvate, covalently bonded through a Schiff base to the catalytic l-lysine" (Rosa et al., 2025, PMID 41022234).
2. The resulting **enamine** performs **aldol addition** onto the aldehyde carbon of ASA.
3. **Transimination/cyclization and dehydration** release the cyclic product HTPA and regenerate the free lysine.

A **catalytic proton-relay triad Tyr–Thr–Tyr** (e.g., Tyr143–Thr54–Tyr117 in *M. tuberculosis*; the equivalent Tyr133–Thr44–Tyr107 in *E. coli*) shuttles protons during catalysis; importantly the second tyrosine is donated **across the tight-dimer interface**, which is why the oligomeric state is functionally essential (Kefala et al., 2008, PMID 18062777).

**Direct sequence evidence in Q88NH2.** Analysis of the retrieved 295-aa sequence located the PROSITE Schiff-base-forming aldolase active-site signature (PS00665) within the segment **`TVPNIIGIKE`**, placing the **catalytic Schiff-base lysine at position ~164** (the *P. putida* equivalent of *E. coli* Lys161). A global pairwise alignment of Q88NH2 against the experimentally characterized *E. coli* DHDPS (UniProt P0A6L2) gave **58.6% identity (170/290 positions)** with **one-to-one conservation of every catalytic residue**:

| *E. coli* residue | Role | Q88NH2 equivalent |
|---|---|---|
| Thr44 | proton-relay triad | **Thr44** |
| Tyr107 | proton-relay triad | **Tyr110** |
| Tyr133 | proton-relay triad | **Tyr136** |
| Lys161 | Schiff-base lysine | **Lys164** |
| Arg138 | ASA α-carboxylate binding | **Arg141** |

The *E. coli* triad was experimentally validated by site-directed mutagenesis — Y133F, T44V and Y107F each "have substantially reduced activity, consistent with the catalytic triad hypothesis" (Dobson, Valegård & Gerrard 2004, PMID 15066435). Their complete conservation in Q88NH2 elevates the annotation from family-level inference to **residue-level mechanistic evidence** that Q88NH2 is a fully functional DHDPS using the identical mechanism.

**Family specificity (not a mis-annotated aldolase).** The DapA/NAL superfamily includes several Schiff-base aldolases that share the catalytic lysine but act on different substrates (e.g., N-acetylneuraminate lyase). Q88NH2 is **58.6% identical to *E. coli* DHDPS** but only **29.9% to *E. coli* N-acetylneuraminate lyase (NanA, P0A6L4)** and 31.1% to *Thermotoga* DHDPS — i.e., it is specifically a DHDPS, not a NAL-type aldolase.

---

## 3b. Paralogy: which copy is the "real" DHDPS?

*P. putida* KT2440 encodes **three** proteins auto-annotated as HTPA synthase (EC 4.3.3.7): **dapA-I/PP_1237/Q88NH2** (target, 295 aa), **dapA-II/PP_2639/Q88JL0** (288 aa), and **PP_2036/Q88L99** (295 aa). Mapping the *E. coli* catalytic and allosteric residues onto each resolves their status:

| Paralog | % id to *E. coli* DHDPS | Catalytic residues (5) | Lysine allosteric site (5) | Verdict |
|---|---|---|---|---|
| **Q88NH2 (dapA-I)** | **58.6%** | **5/5** (Thr44, Tyr110, Tyr136, Lys164, Arg141) | **5/5** | **Canonical, feedback-regulated DHDPS** |
| Q88JL0 (dapA-II) | 35.6% | 5/5 (Thr45, Tyr107, Tyr133, Lys161, Arg138) | 3/5 (His56→Gln, Tyr106→Cys) | Competent but likely **lysine-insensitive** backup isozyme |
| Q88L99 (PP_2036) | 30.3% | 2/5 (proton-relay Thr44→Ser, Tyr107→Trp, Arg138→Thr all lost) | 2/5 | Divergent DapA-like aldolase; **probably not a true DHDPS** (annotation-transfer artefact) |

**Conclusion:** Q88NH2 is the **primary housekeeping DHDPS** — closest to the validated *E. coli* enzyme, with a complete active site and the only intact L-lysine feedback pocket among the three. This resolves the ambiguity implied by the "*dapA-I*" synonym.

---

## 4. Structure, oligomeric state, and subcellular localization

- **Fold:** Each subunit comprises an **N-terminal (β/α)₈ TIM barrel** followed by a **C-terminal α-helical domain** (Kefala et al., 2008, PMID 18062777), consistent with Q88NH2's InterPro annotations (Aldolase_TIM IPR013785; DapA IPR005263/IPR002220).
- **Active site:** Located at the **C-terminal face of the barrel** and formed by **residues from two adjacent subunits across the dimer interface** (PMID 18062777).
- **Quaternary structure:** The functional unit is a **homotetramer** ("dimer of dimers"), demonstrated to be "tetrameric in solution" by analytical ultracentrifugation for orthologous DHDPS enzymes (PMID 18062777). The tight-dimer is the minimal catalytic unit; tetramerization further stabilizes the enzyme.
- **Localization:** DHDPS is a **soluble cytoplasmic enzyme**. Q88NH2 contains no signal peptide or transmembrane segment, consistent with a cytosolic amino-acid biosynthetic enzyme that acts on soluble small-molecule substrates.

---

## 5. Pathway context and regulation

**Position in metabolism.** DapA acts downstream of aspartate kinase and aspartate-semialdehyde dehydrogenase (which produce ASA). By committing ASA to cyclic HTPA, DapA **diverts flux into the DAP/lysine branch** (as opposed to the homoserine → methionine/threonine branch). Downstream, HTPA is reduced by **DapB** (4-hydroxy-tetrahydrodipicolinate reductase) and processed via the DAP sub-pathway to *meso*-DAP, with **DapF/LysA** yielding L-lysine. Thus DapA is the **gatekeeper of lysine and cell-wall DAP biosynthesis**, "essential for bacterial growth and ... considered a target for novel antibiotics" (Skovpen & Palmer, 2013, PMID 23902434).

**KEGG pathway placement in *P. putida* KT2440.** KEGG assigns PP_1237/dapA-I to orthology **K01714 (EC 4.3.3.7)** in Lysine biosynthesis (ppu00300), Biosynthesis of amino acids (ppu01230), and Monobactam biosynthesis (ppu00261). It participates in two modules — **M00016 (succinyl-DAP pathway)** and **M00527 (DAP-aminotransferase pathway)** — that both place DapA (K01714) **immediately downstream of aspartate-4-semialdehyde dehydrogenase (Asd, K00133) and upstream of DapB (K00215)**. The routes then diverge and reconverge:
- *Succinyl-DAP (M00016):* DapB → DapD (K00674) → DapC/ArgD (K00821/K14267) → DapE (K01439) → **DapF (K01778) → LysA (K01586)**
- *DAP-aminotransferase (M00527):* DapB → DapL (K10206) → **DapF (K01778) → LysA (K01586)**

DapA is the single committed entry step feeding both routes, which converge on DAP epimerase (DapF) and *meso*-DAP decarboxylase (LysA) to yield L-lysine; the *meso*-DAP intermediate is drawn off for peptidoglycan cross-linking.

**Genomic organization.** PP_1237 (nt 1,414,728–1,415,615) is **not part of a *dap* operon**: its flanking genes are functionally unrelated (PP_1238 putative lipoprotein, PP_1239 metallo-β-lactamase-family protein, PP_1240 *purC*). Like many scattered bacterial *dap* genes, *dapA-I* appears to be an isolated, monocistronic transcription unit rather than co-transcribed with downstream *dap* genes — consistent with regulation occurring at the enzyme level (allosteric feedback) rather than through operonic co-expression.

**Allosteric regulation.** In many organisms the enzyme is **feedback-inhibited by L-lysine**: "In many organisms, lysine binds allosterically to DapA, causing negative feedback, thus making the enzyme an important regulatory component of the pathway" (Schmitz et al., 2020, PMID 32356521). Lysine binds cooperatively at a cleft on the tight-dimer 2-fold axis (Hill n > 2 in *C. jejuni*; Atkinson et al., 2013, PMID 23354837 for the structural basis in plants). However, **lysine sensitivity is not universal** — the *M. tuberculosis* enzyme "is insensitive to feedback inhibition by (S)-lysine" because the binding site is not conserved (PMID 18062777), and the *B. anthracis* enzyme is likewise not lysine-inhibited (PMID 19595801).

**Prediction for Q88NH2 (sequence-based).** In *E. coli* DHDPS the L-lysine allosteric pocket at the tight-dimer interface is lined by Tyr106, His56, Glu84, Asn80 and Ala49. My alignment shows **all of these are conserved in Q88NH2** (His56→His56, Glu84→Glu87, Tyr106→Tyr109, Asn80→Asn83, Ala49→Ala49). Because it is precisely the *loss* of these residues that abolishes feedback in *M. tuberculosis*/*B. anthracis*, their full conservation **predicts that *P. putida* DapA (Q88NH2) retains E. coli-type L-lysine feedback inhibition**. This is a bioinformatic inference; direct kinetic confirmation for the *P. putida* enzyme has not been reported. Notably, among the three *P. putida* paralogs (§3b), Q88NH2/dapA-I is the **only** copy that retains the full lysine-binding pocket, suggesting it carries the feedback-regulated "housekeeping" role while dapA-II may provide unregulated backup activity.

**Physiological/biotechnological relevance.** Because DAP and lysine are indispensable (cell-wall cross-linking and protein synthesis) and the pathway is absent in mammals, DHDPS is a **validated antibacterial and herbicide target** (PMID 19595801, PMID 23902434), and engineered lysine-feedback-insensitive DHDPS variants are used to boost lysine yields in plants and industrial strains (e.g., PMID 39392917).

---

## 6. Supported vs. refuted hypotheses

| Hypothesis | Status | Basis |
|---|---|---|
| Q88NH2 is a DHDPS/HTPA synthase (EC 4.3.3.7) catalyzing pyruvate + ASA → HTPA | **Supported** | UniProt/HAMAP annotation; DapA family; conserved motifs; ortholog biochemistry |
| Catalysis via Schiff-base to a conserved active-site Lys (ping-pong) | **Supported** | PROSITE PS00665 + catalytic Lys~164 in Q88NH2; ortholog crystallography (PMID 41022234, 18062777) |
| Homotetrameric (β/α)₈ TIM-barrel, cytoplasmic, inter-subunit active site | **Supported** | Family structural data (PMID 18062777); no signal/TM in sequence |
| First committed, gatekeeping step feeding *meso*-DAP + L-lysine | **Supported** | Pathway biochemistry (PMID 32356521, 23902434, 19595801) |
| All catalytic residues (triad + Schiff Lys + ASA-binding Arg) conserved in Q88NH2 | **Supported** | 58.6% identity to E. coli DapA; 1:1 residue mapping; mutagenesis validation (PMID 15066435) |
| Q88NH2 is allosterically lysine-inhibited *in P. putida* | **Predicted (sequence-based), not experimentally verified** | E. coli lysine-pocket residues His56/Glu87/Tyr109/Asn83/Ala49 all conserved; contrast with lysine-insensitive orthologs (PMID 18062777) |

---

## 7. Limitations and future directions

- **No direct experimental characterization** of the *P. putida* KT2440 enzyme was found in the literature searched; kinetic constants, structure, and regulation are inferred from orthologs and sequence analysis.
- **Paralogy is confirmed** (three EC 4.3.3.7 copies: PP_1237/dapA-I, PP_2639/dapA-II, PP_2036). Residue analysis marks Q88NH2 as the canonical DHDPS and dapA-II as a likely lysine-insensitive backup, but the *in vivo* activity, expression, and genetic essentiality/redundancy of each copy (e.g., via RB-TnSeq fitness data, PMID 38323821) remain to be tested experimentally. Whether dapA-II can rescue a dapA-I knockout is unknown.
- **Lysine feedback sensitivity** of Q88NH2 should be tested directly (enzyme kinetics ± L-lysine; identification of the allosteric-site residues by alignment to lysine-sensitive vs. -insensitive orthologs).
- A **structural model** (e.g., AlphaFold) could pinpoint the catalytic triad (Tyr/Thr/Tyr) and putative allosteric cleft to firm up the regulatory prediction.

---

### Key references
- Schmitz et al. 2020, *Acta Cryst F* — DapA definition, substrates, product, allostery (PMID 32356521)
- Kefala et al. 2008, *Biochem J* — *M. tuberculosis* DHDPS structure, TIM barrel, tetramer, proton relay, kinetics, lysine-insensitivity (PMID 18062777)
- Rosa et al. 2025 — pyruvate Schiff base to catalytic lysine (PMID 41022234)
- Skovpen & Palmer 2013 — ping-pong mechanism, essentiality, antibiotic target, cooperative lysine inhibition (PMID 23902434)
- Domigan et al. 2009 — first committed step yielding *meso*-DAP and lysine; antibiotic target (PMID 19595801)
- Atkinson et al. 2013 — structural basis of allosteric lysine inhibition (PMID 23354837)


## Artifacts

- [OpenScientist final report](dapA__Q88NH2-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](dapA__Q88NH2-deep-research-openscientist_artifacts/final_report.pdf)