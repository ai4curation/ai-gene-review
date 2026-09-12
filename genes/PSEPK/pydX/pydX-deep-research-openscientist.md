---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-26T20:22:36.251897'
end_time: '2026-07-26T21:06:37.853665'
duration_seconds: 2641.6
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: pydX
  gene_symbol: pydX
  uniprot_accession: Q88FQ1
  protein_description: 'RecName: Full=dihydrouracil dehydrogenase (NAD(+)) {ECO:0000256|ARBA:ARBA00049728};
    EC=1.3.1.1 {ECO:0000256|ARBA:ARBA00049728}; AltName: Full=Dihydrothymine dehydrogenase
    {ECO:0000256|ARBA:ARBA00032722}; AltName: Full=Dihydrouracil dehydrogenase {ECO:0000256|ARBA:ARBA00030119};'
  gene_info: Name=pydX {ECO:0000313|EMBL:AAN69628.1}; OrderedLocusNames=PP_4037 {ECO:0000313|EMBL:AAN69628.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: 4Fe4S_Fe-S-bd. (IPR017896); DPD_II. (IPR028261); FAD/NAD-bd_sf.
    (IPR036188); FAD/NAD-binding_dom. (IPR023753); Helical_ferredxn. (IPR009051)
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
citation_count: 5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: pydX-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: pydX-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88FQ1
- **Protein Description:** RecName: Full=dihydrouracil dehydrogenase (NAD(+)) {ECO:0000256|ARBA:ARBA00049728}; EC=1.3.1.1 {ECO:0000256|ARBA:ARBA00049728}; AltName: Full=Dihydrothymine dehydrogenase {ECO:0000256|ARBA:ARBA00032722}; AltName: Full=Dihydrouracil dehydrogenase {ECO:0000256|ARBA:ARBA00030119};
- **Gene Information:** Name=pydX {ECO:0000313|EMBL:AAN69628.1}; OrderedLocusNames=PP_4037 {ECO:0000313|EMBL:AAN69628.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** 4Fe4S_Fe-S-bd. (IPR017896); DPD_II. (IPR028261); FAD/NAD-bd_sf. (IPR036188); FAD/NAD-binding_dom. (IPR023753); Helical_ferredxn. (IPR009051)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "pydX" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'pydX' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **pydX** (gene ID: pydX, UniProt: Q88FQ1) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *pydX* (PP_4037, UniProt Q88FQ1) in *Pseudomonas putida* KT2440

## Summary

**pydX** (ordered locus name **PP_4037**; UniProt **Q88FQ1**) of *Pseudomonas putida* strain KT2440 encodes the **electron-input (PreT-type) subunit of dihydropyrimidine dehydrogenase (DPD; EC 1.3.1.1)**, an NADH-dependent iron–sulfur flavoenzyme. DPD catalyzes the committed, first step of the **reductive pyrimidine catabolic pathway**, reducing the pyrimidine bases uracil and thymine to their 5,6-dihydro derivatives (5,6-dihydrouracil and 5,6-dihydrothymine, respectively) at the expense of NADH. The 455-amino-acid PydX polypeptide is not the catalytic centre itself; rather, it provides the pyridine-nucleotide oxidation and intramolecular electron-relay machinery that feeds reducing equivalents to the pyrimidine-reducing active site housed on its partner subunit, PydA.

The functional enzyme is a **heterotetramer of stoichiometry 2·PydA : 2·PydX** (equivalent to the *E. coli* 2·PreA : 2·PreT architecture). PydX carries a **C-terminal FAD/NAD(H)-binding Rossmann fold** that oxidizes NADH and reduces its bound flavin, and an **N-terminal helical ferredoxin domain harbouring tandem [4Fe-4S] clusters** that shuttle electrons onward to the FMN/pyrimidine active site on the catalytic subunit PydA. This wiring—NADH → FAD (on PydX) → [4Fe-4S] clusters → FMN → pyrimidine (on PydA)—defines DPD as a member of a distinctive NADH-dependent subclass of iron–sulfur flavoenzymes. The reaction takes place in the **cytoplasm**.

Biologically, this pathway allows *P. putida* to use pyrimidines primarily as a **nitrogen source**: uracil/thymine are reduced by DPD, the ring is opened by dihydropyrimidinase (PydB), and the product is hydrolyzed by β-alanine synthase (HyuC), ultimately liberating NH₃ and CO₂ and yielding β-alanine. The genes are organized in a contiguous **pyd cluster (PP_4034–PP_4039)** that also encodes a pyrimidine transporter (PydP) and a TetR/RutR-family repressor (**PydR**) that controls expression. Genetic evidence (a *pydA*-null mutant that cannot grow on uracil or thymine as sole nitrogen source) confirms the physiological essentiality of the DPD step, and derepression in a *pydR* mutant confirms the regulatory logic.

---

## Gene/Protein Identity — Verified

| Field | Value |
|-------|-------|
| Gene symbol | **pydX** |
| Ordered locus name | **PP_4037** |
| UniProt accession | **Q88FQ1** |
| Length | 455 amino acids |
| Organism | *Pseudomonas putida* KT2440 (ATCC 47054 / DSM 6125 / NCIMB 11950) |
| EC number | 1.3.1.1 |
| Protein role | Electron-input (PreT-type) subunit of dihydropyrimidine dehydrogenase |

The gene symbol **pydX** correctly matches the UniProt protein description (dihydrouracil dehydrogenase, EC 1.3.1.1) and the target organism. The InterPro domains listed in the research prompt (4Fe4S_Fe-S-bd IPR017896; DPD_II IPR028261; FAD/NAD-bd_sf IPR036188; FAD/NAD-binding_dom IPR023753; Helical_ferredxn IPR009051) align exactly with the electron-input subunit of DPD. Literature on the target organism (Hidese et al. 2012) explicitly names pydX/pydA as the *P. putida* DPD genes, so there is no ambiguity of identity.

---

## Key Findings

### F001 — pydX encodes a subunit of NADH-dependent dihydropyrimidine dehydrogenase (EC 1.3.1.1)

UniProt entry **Q88FQ1** describes a 455-amino-acid protein encoded by gene **pydX** / ordered locus name **PP_4037**, annotated as "dihydrouracil dehydrogenase (NAD(+))" with **EC 1.3.1.1**. The catalyzed reactions correspond to Rhea **RHEA:20189** (5,6-dihydrouracil + NAD⁺ = uracil + NADH + H⁺) and **RHEA:28791** (5,6-dihydrothymine + NAD⁺ = thymine + NADH + H⁺). Although the reference reaction is written in the oxidative direction (as is conventional for EC 1.3.1.1), *in vivo* the enzyme operates in the **reductive** direction, consuming NADH to convert uracil → 5,6-dihydrouracil and thymine → 5,6-dihydrothymine.

The physiological requirement for this activity is demonstrated genetically: a *P. putida* **pydA-null mutant fails to grow on minimal medium containing uracil or thymine as the sole nitrogen source** ([PMID: 22782928](https://pubmed.ncbi.nlm.nih.gov/22782928/)). This directly ties the DPD genes—explicitly named in that study as **pydX and pydA, "tandemly arranged in the *Pseudomonas putida* genome"**—to pyrimidine utilization. Since pydX and pydA encode the two subunits of a single enzyme, loss of the enzyme's function abolishes the committed first step and blocks pyrimidine catabolism.

> "The putative DPD genes, pydX and pydA, are tandemly arranged in the *Pseudomonas putida* genome." — [PMID: 22782928](https://pubmed.ncbi.nlm.nih.gov/22782928/)

> "a pydA strain of *P. putida* fails to grow on a minimal media containing uracil or thymine as a sole nitrogen source, demonstrating the physiological importance of DPD in the reductive pathway" — [PMID: 22782928](https://pubmed.ncbi.nlm.nih.gov/22782928/)

### F002 — DPD is an iron–sulfur flavoenzyme heterotetramer; pydX is the FAD/NAD(H) electron-input subunit

The domain architecture of **Q88FQ1 (pydX, 455 aa)** comprises: a **Pyr_redox_2 FAD/NAD-binding domain** (PF07992; IPR023753/IPR036188), a **DPD domain II** (IPR028261), a **4Fe-4S Fe-S binding domain** (IPR017896; Fer4_20 / PF14691), and a **helical ferredoxin domain** (IPR009051). The UniProt cofactor annotation includes FMN, and the SUBUNIT annotation specifies a **heterotetramer of two PreA and two PreT subunits**. The partner protein, **Q88FQ0 (pydA, 424 aa, PP_4038)**, contains the **dihydroorotate-dehydrogenase-like catalytic TIM-barrel** (IPR005720) plus a **4Fe-4S** cluster domain (IPR017896/IPR017900)—i.e., the pyrimidine-reducing catalytic subunit.

This organization matches the biochemically characterized *E. coli* ortholog, which was shown to be "the first member of a **novel NADH-dependent subclass of iron–sulfur flavoenzymes** catalyzing the conversion of uracil to 5,6-dihydrouracil *in vivo*" ([PMID: 21169495](https://pubmed.ncbi.nlm.nih.gov/21169495/)). In this two-subunit design, PydX supplies the electron-input chain (NADH-oxidizing flavin + iron–sulfur relay) and PydA supplies the pyrimidine-reducing active site.

> "*E. coli* dihydropyrimidine dehydrogenase is the first member of a novel NADH-dependent subclass of iron–sulfur flavoenzymes catalyzing the conversion of uracil to 5,6-dihydrouracil *in vivo*." — [PMID: 21169495](https://pubmed.ncbi.nlm.nih.gov/21169495/)

### F003 — pydX lies in the pyd operon and is regulated by the RutR-homolog repressor PydR

The gene neighborhood in *P. putida* KT2440 places pydX within a functionally coherent operon: **PP_4035 pydP** (an NCS1-family nucleoside/pyrimidine transporter, Q88FQ2), **PP_4036 pydB** (D-hydantoinase/dihydropyrimidinase, A0A140FWK2), **PP_4037 pydX**, and **PP_4038 pydA**, with **pydR** encoded nearby. Hidese et al. ([PMID: 22782928](https://pubmed.ncbi.nlm.nih.gov/22782928/)) showed that **pydA expression and DPD activity are elevated in a *pydR* mutant**, establishing PydR as a **repressor** of the pathway; PydR is homologous to *E. coli* RutR. Consistent with inducible control, earlier work in *Pseudomonas* found that **all three reductive-pathway enzymes are induced by uracil** ([PMID: 1903745](https://pubmed.ncbi.nlm.nih.gov/1903745/)).

The three-enzyme logic of the pathway is stated directly:

> "The pathway is controlled by three enzymes: dihydropyrimidine dehydrogenase (DPD), dihydropyrimidinase and β-alanine synthase." — [PMID: 22782928](https://pubmed.ncbi.nlm.nih.gov/22782928/)

> "we show that PydR acts as a repressor of the pyrimidine reductive pathway in *P. putida*" — [PMID: 22782928](https://pubmed.ncbi.nlm.nih.gov/22782928/)

> "Induction of pyrimidine catabolism by uracil was observed in this pseudomonad." — [PMID: 1903745](https://pubmed.ncbi.nlm.nih.gov/1903745/)

### F004 — The complete reductive pyrimidine catabolic gene cluster (PP_4034–PP_4039) surrounds pydX

Mapping the KEGG/UniProt loci in KT2440 reveals a contiguous cluster encoding the full pathway plus transport and regulation:

| Locus | Gene | UniProt | Product / role | Pathway step |
|-------|------|---------|----------------|--------------|
| PP_4034 | hyuC | Q88FQ3 | N-carbamoyl-β-alanine amidohydrolase (β-alanine synthase) | Step 3 |
| PP_4035 | pydP | Q88FQ2 | NCS1 nucleoside/pyrimidine transporter | Substrate uptake |
| PP_4036 | pydB | A0A140FWK2 | D-hydantoinase / dihydropyrimidinase | Step 2 |
| PP_4037 | **pydX** | **Q88FQ1** | **DPD electron-input subunit (PreT-type)** | **Step 1** |
| PP_4038 | pydA | Q88FQ0 | DPD catalytic subunit (PreA-type) | Step 1 |
| PP_4039 | rutR/pydR | A0A140FWK3 | TetR/RutR-family transcriptional repressor | Regulation |

This physical co-localization of transporter, all three catabolic enzymes, and the regulator provides strong genomic-context support that pydX functions in reductive pyrimidine degradation rather than in an unrelated redox process.

### F005 — Structural/domain evidence: pydX is a two-[4Fe-4S] ferredoxin module fused to an FAD/NAD(P)-binding Rossmann domain

InterPro/CATH mapping of Q88FQ1 (455 aa) resolves a clear two-module architecture:

- **N-terminal α-helical ferredoxin domain** (IPR009051; CATH G3DSA:1.10.1060.10; ~res 6–138/151), overlapping **DPD domain II** (IPR028261 / PF14691; ~res 20–127) and a **4Fe-4S ferredoxin-type cluster-binding site** (IPR017896 / PS51379; ~res 32–65).
- **C-terminal FAD/NAD(P)-binding Rossmann fold** in two subdomains (IPR023753 / PF07992 Pyr_redox_2; ~res 142–437; CATH G3DSA:3.50.50.60 across res 139–260 and 274–455), further supported by the PRINTS signature PR00368 (FAD-dependent pyridine nucleotide reductase).

At the sequence level, residues 32–65 (`RQAALESARCLYCYDAPCVNACPSEIDIPSFIHR`) contain the canonical **CxxCxxCP ferredoxin [4Fe-4S] motif** (Cys41/44/49/53), and a second cysteine cluster (Cys88/92/98/102/110) indicates a **second [4Fe-4S] site**. PANTHER classifies the entire protein as dihydropyrimidine dehydrogenase (PTHR43073; res 16–449). Together these features are precisely those expected of an electron-input subunit: a flavin/pyridine-nucleotide oxidase fused to an iron–sulfur electron-relay.

The structural role of these N-terminal [4Fe-4S] clusters is further illuminated by comparative work on glutamate synthase, in which four conserved N-terminal cysteines were shown to be essential not only for electron transfer but also for subunit association — a study that explicitly references "the three-dimensional structure of dihydropyrimidine dehydrogenase, an enzyme containing an N-terminal β-subunit-like domain" ([PMID: 15797248](https://pubmed.ncbi.nlm.nih.gov/15797248/)). This supports a model in which PydX's N-terminal ferredoxin/[4Fe-4S] module is both an electron conduit and a structural interface for heterotetramer assembly.

### F006 — pydX is specifically the PreT-type subunit (ortholog of *E. coli* PreT)

The InterPro domain set of pydX/Q88FQ1—{IPR028261 DPD_II; IPR023753 & IPR036188 FAD/NAD-binding; IPR009051 helical ferredoxin}—is **identical to that of *E. coli* PreT** (P76440, b2146, 412 aa; "NAD-dependent dihydropyrimidine dehydrogenase subunit PreT"). Reciprocally, the partner pydA/Q88FQ0 domain set—{IPR017896/IPR017900 4Fe-4S; IPR013785 aldolase TIM; IPR005720 dihydroorotate DH catalytic}—matches ***E. coli* PreA** (P25889, b2147, 411 aa; cofactor [4Fe-4S]). Thus the assignment is unambiguous: **pydX = PreT** (electron input) and **pydA = PreA** (catalytic), assembling into the **2 PreA : 2 PreT** heterotetramer.

The physiological orientation of the pathway toward nitrogen scavenging is supported by growth physiology in *E. coli* B ([PMID: 3553866](https://pubmed.ncbi.nlm.nih.gov/3553866/)), where reductive-pathway intermediates support growth roughly **14-fold better as a sole nitrogen source than as a sole carbon source**:

> "dihydrouracil, N-carbamoyl-beta-alanine, beta-alanine, dihydrothymine and beta-aminoisobutyric acid could sustain the growth of the bacterial cells as sole nitrogen sources by at least a fourteen-fold greater level than that observed if they were included as sole carbon sources" — [PMID: 3553866](https://pubmed.ncbi.nlm.nih.gov/3553866/)

---

## Mechanistic Model / Interpretation

### The enzyme and its electron path

Dihydropyrimidine dehydrogenase in *P. putida* is a bipartite iron–sulfur flavoenzyme. PydX (PreT) is the **electron-input subunit** and PydA (PreA) is the **catalytic subunit**. In the physiologically relevant reductive direction, electrons flow from NADH through PydX's flavin and iron–sulfur relay into PydA's active site, where the pyrimidine ring is reduced across the C5–C6 double bond:

```
             ┌───────────────── PydX (PreT, electron input) ─────────────────┐
   NADH  →   FAD/NAD Rossmann domain  →  [4Fe-4S]  →  [4Fe-4S]  ────────────┐
             (C-terminal, res ~142-437)   (N-terminal ferredoxin, res ~6-138)│
                                                                             ▼
             ┌───────────────── PydA (PreA, catalytic) ──────────────────────┐
             [4Fe-4S]  →  FMN  →  pyrimidine (uracil / thymine)
                                          │
                                          ▼
                          5,6-dihydrouracil / 5,6-dihydrothymine
```

Assembled stoichiometry: **2 × PydA : 2 × PydX** heterotetramer, operating in the **cytoplasm**.

### The pathway and its physiological purpose

DPD catalyzes step 1 of a three-enzyme reductive route that dismantles the pyrimidine ring, primarily to release nitrogen (and secondarily carbon):

```
 uracil ──DPD (PydX/PydA)──▶ 5,6-dihydrouracil ──dihydropyrimidinase (PydB)──▶
   N-carbamoyl-β-alanine ──β-alanine synthase (HyuC)──▶ β-alanine + NH3 + CO2

 thymine ─DPD─▶ 5,6-dihydrothymine ─PydB─▶ N-carbamoyl-β-aminoisobutyrate
                              ─HyuC─▶ β-aminoisobutyrate + NH3 + CO2
```

Substrates enter the cell via the NCS1-family transporter **PydP** (PP_4035), and the whole operon is held under negative control by the RutR-like repressor **PydR** (PP_4039), being derepressed/induced when pyrimidines are available. The ~14-fold preference for pyrimidine intermediates as nitrogen versus carbon source ([PMID: 3553866](https://pubmed.ncbi.nlm.nih.gov/3553866/)) frames the biological "why": this is a **nitrogen-scavenging** pathway, and PydX's role is to power the committed reductive step.

### Substrate specificity

The enzyme is specific for the **pyrimidine bases uracil and thymine** (and, correspondingly, is active on their dihydro forms in the oxidative direction). It reduces the C5=C6 double bond of the pyrimidine ring. Cytosine is not a direct substrate of this pathway (deamination to uracil is required upstream). The two documented Rhea reactions (RHEA:20189 uracil/dihydrouracil; RHEA:28791 thymine/dihydrothymine) capture this specificity.

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution | Support / Challenge |
|------|-----------------|--------------|---------------------|
| [22782928](https://pubmed.ncbi.nlm.nih.gov/22782928/) | *Pseudomonas putida PydR represses DPD gene* | Names **pydX/pydA** as the *P. putida* DPD genes; establishes PydR repressor; *pydA* mutant cannot use uracil/thymine as N source | **Strongly supports** F001, F003, F004 — the only study explicitly on the target organism/genes |
| [21169495](https://pubmed.ncbi.nlm.nih.gov/21169495/) | *E. coli DPD is a novel NAD-dependent heterotetramer* | Defines the enzyme class: NADH-dependent iron–sulfur flavoenzyme heterotetramer producing 5,6-dihydrouracil | **Supports** F002, F006 — biochemical basis for the ortholog |
| [1903745](https://pubmed.ncbi.nlm.nih.gov/1903745/) | *Pyrimidine catabolism in P. aeruginosa* | Reductive-pathway enzymes present and **uracil-inducible** in *Pseudomonas* | **Supports** F003 — regulation/induction |
| [3553866](https://pubmed.ncbi.nlm.nih.gov/3553866/) | *Degradation of uracil and thymine by E. coli B* | Pathway intermediates support growth ~14× better as N than C source | **Supports** F006 — nitrogen-scavenging role |
| [15797248](https://pubmed.ncbi.nlm.nih.gov/15797248/) | *Structural role of glutamate synthase [4Fe-4S] clusters* | Shows N-terminal β-subunit [4Fe-4S] clusters are structural and reference the 3D structure of DPD as a model | **Contextual support** for F005 — role of N-terminal [4Fe-4S]/ferredoxin module in a homologous enzyme |

The evidence is a combination of: (i) **direct genetic evidence in the target organism** (the *pydA* growth phenotype and *pydR* derepression, [PMID: 22782928](https://pubmed.ncbi.nlm.nih.gov/22782928/)); (ii) **biochemical characterization of the close *E. coli* ortholog** ([PMID: 21169495](https://pubmed.ncbi.nlm.nih.gov/21169495/)); (iii) **bioinformatic/structural inference** from InterPro/CATH domain mapping and conserved cysteine motifs (F005, F006); and (iv) **physiological/comparative context** ([PMID: 1903745](https://pubmed.ncbi.nlm.nih.gov/1903745/), [PMID: 3553866](https://pubmed.ncbi.nlm.nih.gov/3553866/)).

---

## Limitations and Knowledge Gaps

1. **No purified-enzyme kinetics for the *P. putida* protein specifically.** Substrate specificity, kinetic parameters (Kₘ, kcat), and cofactor content have not been reported for the KT2440 DPD (Q88FQ1/Q88FQ0). The mechanistic model is inferred from the *E. coli* PreA/PreT ortholog.
2. **Subunit assignment for PydX is confirmed genetically and bioinformatically, not by direct in-organism biochemistry.** The critical growth phenotype was reported for a *pydA* mutant; a dedicated *pydX* knockout phenotype is not documented in the reviewed literature, though the heterotetramer requires both subunits.
3. **No experimental 3D structure of the *P. putida* enzyme.** The [4Fe-4S] cluster count and ligation, and the flavin (FAD on PydX vs. FMN on PydA) assignments, rest on domain homology and conserved cysteine motifs rather than a crystal structure of this protein.
4. **Cofactor ambiguity in annotation.** UniProt lists FMN as a cofactor for Q88FQ1, whereas the electron-input subunit of characterized orthologs is expected to bind FAD (with FMN on the catalytic subunit). The precise flavin composition of each *P. putida* subunit should be verified experimentally.
5. **Operon structure/transcription not directly mapped in KT2440.** The precise transcript boundaries, promoter(s), and PydR operator sites in *P. putida* have not been experimentally delineated in the reviewed sources.
6. **Localization is inferred.** Cytoplasmic localization is the expected and consistent assignment for a soluble NADH-dependent metabolic enzyme but was not directly demonstrated for this protein.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant co-expression and purification** of PydX (Q88FQ1) with PydA (Q88FQ0) from *P. putida* KT2440, followed by confirmation of the 2:2 heterotetramer by size-exclusion chromatography / native mass spectrometry.
2. **Steady-state kinetics** with uracil and thymine (and their dihydro forms) using NADH/NAD⁺, to measure substrate specificity and kinetic constants, and to confirm the enzyme's directional preference (NADH-consuming reduction) *in vitro*.
3. **Cofactor determination**: quantify flavin content (FAD vs. FMN per subunit) and iron/sulfide content, plus EPR/UV–vis spectroscopy to count and characterize the [4Fe-4S] clusters, testing the predicted tandem N-terminal clusters on PydX.
4. **Targeted mutagenesis** of the conserved cysteine motifs (Cys41/44/49/53 and Cys88/92/98/102/110) to test their role in cluster ligation and electron transfer, analogous to the glutamate-synthase study ([PMID: 15797248](https://pubmed.ncbi.nlm.nih.gov/15797248/)).
5. **Dedicated *pydX* deletion mutant** in KT2440 with growth assays on uracil/thymine as sole N (and C) source, to establish the standalone phenotype and complementation.
6. **Transcriptional mapping**: define the *pyd* operon promoter/transcript boundaries and PydR operator by RNA-seq/primer extension and EMSA/ChIP, and confirm uracil-dependent derepression.
7. **Structural determination** (X-ray or cryo-EM) of the *P. putida* DPD heterotetramer to validate the electron-relay path from NADH → FAD → [4Fe-4S] → FMN → pyrimidine.

---

## Conclusion

The gene symbol **pydX** is correctly matched to the target: it is the *P. putida* KT2440 gene (PP_4037, UniProt Q88FQ1) for the **electron-input (PreT-type) subunit of dihydropyrimidine dehydrogenase (EC 1.3.1.1)**. All lines of evidence—organism-specific genetics, ortholog biochemistry, genomic context, and domain/structural bioinformatics—converge on a single, coherent function: PydX supplies NADH-derived reducing equivalents, via an FAD/NAD Rossmann domain and tandem [4Fe-4S] clusters, to the catalytic subunit PydA, enabling the cytoplasmic reduction of uracil and thymine as the committed first step of the reductive pyrimidine catabolic pathway that *P. putida* uses chiefly to acquire nitrogen.


## Artifacts

- [OpenScientist final report](pydX-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](pydX-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:22782928
2. PMID:21169495
3. PMID:1903745
4. PMID:15797248
5. PMID:3553866