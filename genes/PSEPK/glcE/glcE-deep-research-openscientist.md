---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-15T17:08:39.802211'
end_time: '2026-07-15T17:56:01.971537'
duration_seconds: 2842.17
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: glcE
  gene_symbol: glcE
  uniprot_accession: Q88GH7
  protein_description: 'SubName: Full=Glycolate oxidase, putative FAD-binding subunit
    {ECO:0000313|EMBL:AAN69341.1}; EC=1.1.99.14 {ECO:0000313|EMBL:AAN69341.1};'
  gene_info: Name=glcE {ECO:0000313|EMBL:AAN69341.1}; OrderedLocusNames=PP_3746 {ECO:0000313|EMBL:AAN69341.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: FAD-bd_PCMH. (IPR016166); FAD-bd_PCMH-like_sf. (IPR036318); FAD-bd_PCMH_sub2.
    (IPR016169); FAD-linked_Oxase-like_C. (IPR016164); Oxid_FAD_bind_N. (IPR006094)
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
  path: glcE-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: glcE-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88GH7
- **Protein Description:** SubName: Full=Glycolate oxidase, putative FAD-binding subunit {ECO:0000313|EMBL:AAN69341.1}; EC=1.1.99.14 {ECO:0000313|EMBL:AAN69341.1};
- **Gene Information:** Name=glcE {ECO:0000313|EMBL:AAN69341.1}; OrderedLocusNames=PP_3746 {ECO:0000313|EMBL:AAN69341.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** FAD-bd_PCMH. (IPR016166); FAD-bd_PCMH-like_sf. (IPR036318); FAD-bd_PCMH_sub2. (IPR016169); FAD-linked_Oxase-like_C. (IPR016164); Oxid_FAD_bind_N. (IPR006094)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "glcE" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'glcE' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **glcE** (gene ID: glcE, UniProt: Q88GH7) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of *glcE* (PP_3746, UniProt Q88GH7) in *Pseudomonas putida* KT2440

## 1. Summary (Answer to the Research Question)

**glcE** encodes the **FAD-binding subunit of glycolate oxidase (glycolate dehydrogenase), a heterotrimeric, membrane-associated flavoenzyme (GlcD–GlcE–GlcF)** that catalyzes the oxidation of **glycolate (2-hydroxyacetate) to glyoxylate** (EC 1.1.99.14). Rather than reducing O₂, this "oxidase" is mechanistically a **dehydrogenase** that passes electrons from the reduced flavin, via its iron–sulfur subunit (GlcF), into the respiratory electron-transport chain. GlcE itself is the flavin (FAD)-binding module of the complex; it is essential for holoenzyme activity but does not act alone. The enzyme operates in the **cytoplasm/inner-membrane interface** and constitutes the **committed step of glycolate and two-carbon (C2) catabolism**, generating glyoxylate for assimilation via the glyoxylate node (malate synthase / glyoxylate carboligase). In *P. putida* KT2440 this activity is central to metabolizing **ethylene glycol–derived glycolate**, relieving the toxic glycolaldehyde/glycolate bottleneck.

The gene identity is **confirmed and unambiguous**: the *P. putida* KT2440 *glcDEF* operon is directly documented as glycolate oxidase (Franden et al. 2018, PMID 29885475), and the subunit architecture is defined in the classic *E. coli* *glc* locus studies (Pellicer et al. 1996, PMID 8606183).

---

## 2. Gene / Protein Identity Verification

| Attribute | Value | Source |
|---|---|---|
| UniProt accession | Q88GH7 | Task metadata |
| Gene name | *glcE* | UniProt (EMBL AAN69341.1) |
| Ordered locus | PP_3746 | UniProt |
| Organism | *Pseudomonas putida* KT2440 | UniProt |
| Annotated activity | Glycolate oxidase, putative FAD-binding subunit; EC 1.1.99.14 | UniProt |
| Key domains | FAD-bd_PCMH (IPR016166), FAD-bd_PCMH-like_sf (IPR036318), FAD-bd_PCMH_sub2 (IPR016169), FAD-linked oxidase C (IPR016164), Oxid_FAD_bind_N (IPR006094) | InterPro |

**Verification outcome — CONFIRMED.** All independent lines of evidence agree:
- The gene symbol *glcE* corresponds to the FAD/flavin subunit of the **glc** (glycolate) system, exactly matching the UniProt description "Glycolate oxidase, putative FAD-binding subunit."
- The organism-specific literature (Franden et al. 2018) explicitly names the *P. putida* KT2440 **glcDEF** operon as glycolate oxidase.
- The InterPro **FAD-bd_PCMH** domain set places GlcE in the **PCMH-type FAD-binding / vanillyl-alcohol-oxidase (VAO) flavoprotein superfamily**, the same superfamily as the flavo-subunits of bacterial glycolate/D-lactate oxidoreductases — consistent with an FAD-binding role.

No conflicting "same-symbol, different-gene" literature was found; *glcE* is used consistently across bacteria for this subunit. (Note: eukaryotic/plant "glycolate oxidase," GOX, is an unrelated peroxisomal FMN enzyme of the α-hydroxyacid oxidase family and is **not** the same protein; the bacterial GlcDEF system described here is the correct homolog.)

### 2.1 Genome-level confirmation (synteny + orthology, this study)

A KEGG genomic-neighborhood query of *P. putida* KT2440 (retrieved 2026-07-16) shows PP_3746 sits in a **canonical, syntenic glycolate-utilization operon** that mirrors the *E. coli* *glc* locus:

| Locus | Gene | KEGG Ortholog (KO) | Annotation |
|---|---|---|---|
| PP_3744 | *glcC* | K11474 | GlcC glc-operon transcriptional activator (GntR family) — divergently oriented |
| PP_3745 | *glcD* | K00104 | glycolate dehydrogenase, **FAD-linked (catalytic) subunit** (EC 1.1.99.14) |
| **PP_3746** | ***glcE*** | **K11472** | glycolate dehydrogenase, **FAD-binding subunit** (EC 1.1.99.14) ← target |
| PP_3747 | *glcF* | K11473 | glycolate dehydrogenase, **iron–sulfur subunit** |
| PP_3748 | *glcG* | K11477 | glc operon protein GlcG (accessory) |

This places GlcE (K11472) alongside its obligate partners GlcD (K00104) and GlcF (K11473) under the divergent GlcC regulator — genome-level corroboration of the biochemical assignment.

### 2.2 Sequence/domain architecture (this study)

Q88GH7 is a **350-residue** protein bearing a single **FAD-binding PCMH-type domain (residues 1–173; Pfam PF01565 "FAD_binding_4"; InterPro IPR016166/IPR016169/IPR006094; Gene3D 3.30.465.10; SUPFAM SSF56176 + SSF55103)** and **no predicted transmembrane segments**. This is the diagnostic N-terminal FAD-binding fold of the **PCMH/vanillyl-alcohol-oxidase (VAO) flavoprotein superfamily**, which also contains the flavo-subunits of bacterial D-lactate dehydrogenase and related 2-hydroxyacid oxidoreductases. The absence of TM helices indicates GlcE is a **soluble/peripheral flavin-binding subunit** that assembles into the complex rather than an integral membrane protein; membrane association of the complex is provided through the GlcF [Fe-S] subunit and its coupling to the respiratory quinone pool. A crude global alignment gave ~22% identity to *E. coli* GlcE (P52045) and ~26% to GlcD (P0AEP9) — modest but typical for diverged orthologs, with the KO assignment and operon synteny being the decisive evidence.

---

## 3. Key Findings with Evidence

### 3.1 Molecular function: FAD-binding subunit of glycolate oxidase

The founding genetic characterization of the *E. coli* *glc* locus (Pellicer et al. 1996, PMID 8606183) established the three-subunit architecture that defines this enzyme family:

> "The proteins encoded from glcD and glcE displayed similarity to several flavoenzymes, the one from glcF was found to be similar to iron-sulfur proteins."

and, demonstrating essentiality:

> "The insertional mutation … in either glcD, glcE, or glcF abolished glycolate oxidase activity, indicating that presumably these proteins are subunits of this enzyme."

Thus **GlcD** is the catalytic flavo-subunit, **GlcE** is the FAD/flavin-binding subunit, and **GlcF** is the iron–sulfur electron-transfer subunit. Loss of any one — including *glcE* — abolishes activity, so GlcE is an **obligate, non-redundant catalytic component**, not an accessory factor. The InterPro FAD-bd_PCMH domains on Q88GH7 corroborate the flavin-binding role at the sequence level.

### 3.2 Reaction catalyzed and substrate specificity

The holoenzyme catalyzes:

**glycolate + [electron acceptor/respiratory quinone] → glyoxylate + [reduced acceptor]** (EC 1.1.99.14)

The physiological substrate is the **two-carbon 2-hydroxymonocarboxylate glycolate**. Substrate identity is reinforced by the cognate uptake system in the same operon: GlcA (the glycolate permease) is specific for **2-hydroxymonocarboxylates — glycolate, L-lactate, and D-lactate** (Núñez et al. 2001, PMID 11283302):

> "specificity for the 2-hydroxymonocarboxylates glycolate, L-lactate and D-lactate."

The name "oxidase" is historical; the membrane-associated GlcDEF complex functions as a **flavin-dependent, respiratory-chain-linked dehydrogenase** (the flavin is reoxidized by the [Fe-S] subunit feeding electrons to quinone, not directly by O₂), which is why the EC number carries the "99" (acceptor = other/quinone) classification.

### 3.2.1 Structural inference (AlphaFold, this study)

The AlphaFold DB model **AF-Q88GH7-F1 (v6)** is **very high confidence across all 350 residues** (mean pLDDT **93.8**, median 96.2; 89.4% of residues ≥90). Both structural lobes are confidently modeled — the **N-terminal FAD-binding PCMH domain** (res 1–173, mean pLDDT 93.2) and the **C-terminal FAD-linked-oxidase-like "cap" domain** (res 174–350, mean pLDDT 94.4). This **bilobal architecture is the canonical fold of the PCMH/VAO flavoprotein superfamily**, in which the interdomain cleft accommodates the FAD isoalloxazine and substrate. The uniformly high confidence indicates a **well-folded, ordered flavoprotein subunit** (not disordered or degenerate), and the compact globular fold with no predicted transmembrane helices is consistent with a **soluble/peripheral subunit** that docks with GlcD and the [Fe-S] subunit GlcF (which mediate membrane/respiratory-chain coupling).

### 3.3 Pathway context: the glyoxylate node and C2 assimilation

Glycolate oxidation is the **committed entry step** into two-carbon metabolism, producing glyoxylate as the pivotal intermediate (Pellicer et al. 1999, PMID 9880556):

> "The metabolic pathways specified by the glc and ace operons in Escherichia coli yield glyoxylate as a common intermediate, which is acted on by two malate synthase isoenzymes."

Downstream, glyoxylate is assimilated by two routes:
- **Malate synthase (GlcB / AceB):** glyoxylate + acetyl-CoA → malate (glyoxylate shunt), and
- **Glyoxylate carboligase (Gcl):** 2 glyoxylate → tartronate semialdehyde → glycerate → central metabolism.

In *E. coli* the structural genes are organized as the **glcDEFGB** operon (with *glcG* dispensable) under the divergent **GlcC** activator, dependent on **integration host factor (IHF)** and repressed by the respiratory regulator **ArcA-P** — a regulatory logic that cross-induces the glc and ace systems because both converge on glyoxylate (Pellicer et al. 1999, PMID 9880556; Pellicer et al. 1996, PMID 8606183).

### 3.4 Physiological role in *P. putida* KT2440 — ethylene glycol / glycolate catabolism

In *P. putida* KT2440, ethylene glycol is oxidized through the toxic intermediates **glycolaldehyde → glycolate**, and glycolate oxidase (GlcDEF) is the key enzyme that channels glycolate onward. Franden et al. (2018, PMID 29885475) showed that engineering efficient ethylene-glycol utilization required relieving the glycolate bottleneck:

> "the additional overexpression of the glycolate oxidase (glcDEF) operon removes the glycolate bottleneck and minimizes the production of these toxic intermediates."

More recent work on *P. putida* strains confirms that robust ethylene-glycol/glycolate metabolism hinges on **glyoxylate assimilation pathways** downstream of glycolate oxidation (Molpeceres-García et al. 2026, PMID 41453527), reinforcing that GlcDEF-catalyzed glycolate → glyoxylate is the gateway reaction. This makes *glcE* biotechnologically important for **PET/ethylene glycol upcycling** in *Pseudomonas* chassis.

**Position in the EG oxidation cascade and downstream regulation.** In KT2440, EG is catabolized by a sequence of oxidations **EG → glycolaldehyde → glycolate → glyoxylate**, with **glycolate oxidase (GlcDEF) catalyzing the terminal glycolate → glyoxylate step**. Adaptive laboratory evolution demonstrated that the principal limitation on EG growth is not glycolate oxidation itself but **downstream glyoxylate assimilation and flux balancing**: the key growth-enabling mutation lies in the repressor **GclR**, "which represses the glyoxylate carboligase pathway," and secondary mutations improve growth "by balancing fluxes through the initial oxidations of ethylene glycol to glyoxylate" (Li et al. 2019, PMID 31166064). The product glyoxylate is natively assimilated through the **glycerate pathway (glyoxylate carboligase route)**, described as wasteful because it releases CO₂ — which has motivated engineering of alternative routes such as the **β-hydroxyaspartate cycle** to improve EG assimilation (Schada von Borzyskowski et al. 2023, PMID 36731627). Thus GlcE, as the FAD-binding subunit of GlcDEF, sits at the **convergence point where all EG/C2 carbon enters central metabolism** via glyoxylate.

### 3.5 Subcellular localization

The GlcDEF glycolate oxidase is a **membrane-associated (cytoplasmic/inner-membrane) flavoenzyme complex** whose catalytic reaction occurs on the cytoplasmic face; the GlcF iron–sulfur subunit couples flavin reoxidation to the membrane respiratory chain (quinone pool). This localization is inferred from (i) the requirement for a dedicated permease (GlcA) to import glycolate into the cytoplasm before oxidation (PMID 11283302), and (ii) the general architecture of PCMH/VAO-family FAD + [Fe-S] respiratory dehydrogenases, which are anchored/associated at the inner membrane to donate electrons to quinone. GlcE, as the FAD-binding subunit, functions within this complex at the membrane interface rather than as a soluble standalone enzyme.

---

## 4. Supported and Refuted Hypotheses

**Supported:**
- **H1:** *glcE* encodes the FAD-binding subunit of glycolate oxidase (GlcDEF). — Supported by direct organism-specific naming (PMID 29885475), subunit genetics (PMID 8606183), and InterPro FAD-bd_PCMH domains.
- **H2:** The enzyme oxidizes glycolate to glyoxylate as its primary reaction. — Supported by EC 1.1.99.14 assignment and pathway genetics (PMID 9880556, 8606183).
- **H3:** GlcE is obligate for activity (not accessory). — Supported: *glcE* insertional mutants lose all glycolate oxidase activity (PMID 8606183).
- **H4:** The functional role is entry into the glyoxylate node / C2 assimilation, and specifically ethylene-glycol/glycolate catabolism in *P. putida*. — Supported (PMID 9880556, 29885475, 41453527).

**Refuted / excluded:**
- The protein is **not** the eukaryotic peroxisomal FMN glycolate oxidase (GOX, α-hydroxyacid oxidase family). The bacterial GlcDEF system is a distinct PCMH/VAO-family FAD-dependent respiratory dehydrogenase.
- GlcE is **not** a soluble monomeric oxidase; it acts only within the GlcD–GlcE–GlcF complex.

---

## 5. Limitations and Future Directions

- **Direct biochemistry is from the *E. coli* ortholog**, not from purified *P. putida* KT2440 GlcE; the *P. putida* evidence is genetic/physiological (operon-level). Subunit-resolved kinetics (kcat/Km for glycolate, flavin type, redox potentials) for the *P. putida* enzyme are not yet reported.
- **Flavin covalency and cofactor stoichiometry** (whether GlcE binds FAD covalently or non-covalently) are inferred from the PCMH/VAO family and not experimentally verified for Q88GH7.
- **Structural data** (experimental or AlphaFold-validated quaternary arrangement of GlcDEF) would clarify how GlcE positions FAD relative to the GlcD active site and the GlcF [Fe-S] chain.
- Future work: heterologous purification and steady-state kinetics of *P. putida* GlcDEF; identification of the physiological electron acceptor (quinone) and membrane topology; site-directed mutagenesis of GlcE flavin-binding residues.

---

## 6. Key References

- Pellicer MT, Badía J, Aguilar J, Baldomà L. *glc* locus of *Escherichia coli*: characterization of genes encoding the subunits of glycolate oxidase and the *glc* regulator protein. **J Bacteriol** 1996. PMID 8606183.
- Pellicer MT, Fernandez C, Badía J, Aguilar J, Lin ECC, Baldomà L. Cross-induction of *glc* and *ace* operons of *Escherichia coli* … Characterization of the *glc* promoter. **J Biol Chem** 1999. PMID 9880556.
- Núñez MF, Pellicer MT, Badía J, Aguilar J, Baldomà L. The gene *yghK* linked to the *glc* operon of *Escherichia coli* encodes a permease for glycolate … **Microbiology** 2001. PMID 11283302.
- Franden MA, Jayakody LN, Li W-J, et al. Engineering *Pseudomonas putida* KT2440 for efficient ethylene glycol utilization. **Metab Eng** 2018. PMID 29885475.
- Li W-J, Jayakody LN, Franden MA, et al. Laboratory evolution reveals the metabolic and regulatory basis of ethylene glycol metabolism by *Pseudomonas putida* KT2440. **Environ Microbiol** 2019. PMID 31166064.
- Schada von Borzyskowski L, Schulz-Mirbach H, Troncoso Castellanos M, et al. Implementation of the β-hydroxyaspartate cycle increases growth performance of *Pseudomonas putida* on the PET monomer ethylene glycol. **Metab Eng** 2023. PMID 36731627.
- Molpeceres-García FJ, et al. *Pseudomonas putida* JM37 as a novel bacterial chassis for ethylene glycol upcycling. 2026. PMID 41453527.


## Artifacts

- [OpenScientist final report](glcE-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](glcE-deep-research-openscientist_artifacts/final_report.pdf)