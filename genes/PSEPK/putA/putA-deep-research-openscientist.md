---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-13T02:15:22.787112'
end_time: '2026-08-13T02:31:38.408392'
duration_seconds: 975.62
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: putA
  gene_symbol: putA
  uniprot_accession: Q88D80
  protein_description: 'RecName: Full=Bifunctional protein PutA {ECO:0000256|PIRNR:PIRNR000197};
    Includes: RecName: Full=Proline dehydrogenase {ECO:0000256|PIRNR:PIRNR000197};
    EC=1.5.5.2 {ECO:0000256|PIRNR:PIRNR000197}; AltName: Full=Proline oxidase {ECO:0000256|PIRNR:PIRNR000197};
    Includes: RecName: Full=Delta-1-pyrroline-5-carboxylate dehydrogenase {ECO:0000256|PIRNR:PIRNR000197};
    Short=P5C dehydrogenase {ECO:0000256|PIRNR:PIRNR000197}; EC=1.2.1.88 {ECO:0000256|PIRNR:PIRNR000197};
    AltName: Full=L-glutamate gamma-semialdehyde dehydrogenase {ECO:0000256|PIRNR:PIRNR000197};'
  gene_info: Name=putA {ECO:0000313|EMBL:AAN70514.1}; OrderedLocusNames=PP_4947 {ECO:0000313|EMBL:AAN70514.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: In the N-terminal section; belongs to the proline
  protein_domains: Ald_DH/histidinol_DH. (IPR016161); Ald_DH_C. (IPR016163); Ald_DH_CS_CYS.
    (IPR016160); Ald_DH_N. (IPR016162); Aldehyde_DH_dom. (IPR015590)
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
citation_count: 15
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: putA-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: putA-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88D80
- **Protein Description:** RecName: Full=Bifunctional protein PutA {ECO:0000256|PIRNR:PIRNR000197}; Includes: RecName: Full=Proline dehydrogenase {ECO:0000256|PIRNR:PIRNR000197}; EC=1.5.5.2 {ECO:0000256|PIRNR:PIRNR000197}; AltName: Full=Proline oxidase {ECO:0000256|PIRNR:PIRNR000197}; Includes: RecName: Full=Delta-1-pyrroline-5-carboxylate dehydrogenase {ECO:0000256|PIRNR:PIRNR000197}; Short=P5C dehydrogenase {ECO:0000256|PIRNR:PIRNR000197}; EC=1.2.1.88 {ECO:0000256|PIRNR:PIRNR000197}; AltName: Full=L-glutamate gamma-semialdehyde dehydrogenase {ECO:0000256|PIRNR:PIRNR000197};
- **Gene Information:** Name=putA {ECO:0000313|EMBL:AAN70514.1}; OrderedLocusNames=PP_4947 {ECO:0000313|EMBL:AAN70514.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** In the N-terminal section; belongs to the proline
- **Key Domains:** Ald_DH/histidinol_DH. (IPR016161); Ald_DH_C. (IPR016163); Ald_DH_CS_CYS. (IPR016160); Ald_DH_N. (IPR016162); Aldehyde_DH_dom. (IPR015590)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "putA" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'putA' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **putA** (gene ID: putA, UniProt: Q88D80) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: PutA (Q88D80) of *Pseudomonas putida* KT2440

**Gene:** *putA* (ordered locus PP_4947)
**UniProt:** Q88D80
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / NCIMB 11950 / KT2440), PSEPK
**Protein length:** 1,317 aa · **Mass:** 142.6 kDa · **Cofactor:** FAD (non-covalent)
**EC numbers:** 1.5.5.2 (proline dehydrogenase) and 1.2.1.88 (L-glutamate-5-semialdehyde / Δ¹-pyrroline-5-carboxylate dehydrogenase)

---

## Summary

PutA (Q88D80, PP_4947) of *Pseudomonas putida* KT2440 is a large (~1,317-residue, ~142.6 kDa) FAD-dependent **trifunctional flavoenzyme** that carries out the complete catabolic conversion of L-proline to L-glutamate and, in addition, acts as the autogenous transcriptional repressor of its own proline-utilization (*put*) genes. It belongs to the enteric-type ("Type C") trifunctional PutA class: a global sequence alignment shows it is **~74% identical over its full length to *Escherichia coli* PutA (P09546)**, and direct experimental characterization of the *P. putida* enzyme confirmed that a single 1,315-residue polypeptide catalyzes both oxidative steps of proline degradation. This licenses a high-confidence transfer of the extensively studied *E. coli*/*Salmonella* PutA mechanism to the *P. putida* protein, reinforced by residue-level conservation of every catalytically important side chain.

Mechanistically, PutA couples three functions within one polypeptide. (1) A **proline dehydrogenase (PRODH)** domain built on a (βα)₈ barrel uses a non-covalently bound FAD to oxidize L-proline to Δ¹-pyrroline-5-carboxylate (P5C), passing the electrons to a membrane ubiquinone (EC 1.5.5.2). (2) An **aldehyde-dehydrogenase-superfamily domain** (P5C / L-glutamate-γ-semialdehyde dehydrogenase; EC 1.2.1.88; catalytic Glu881 general base and Cys915 nucleophile) oxidizes the ring-opened intermediate L-glutamate-γ-semialdehyde (GSA) to L-glutamate using NAD⁺. The reactive P5C/GSA intermediate is not released to bulk solvent; it is **channeled through a buried internal tunnel (~42 Å) between the two active sites**, a mechanism that also facilitates the thermodynamically unfavorable P5C→GSA hydrolysis. (3) Through an **N-terminal ribbon-helix-helix (RHH) DNA-binding domain**, PutA binds the operator of the divergently transcribed *putA*/*putP* genes and represses them.

Uniquely for this protein family, its **subcellular localization and function are conditional and redox-controlled.** When proline is scarce, the FAD is oxidized and PutA behaves as a cytoplasmic DNA-bound repressor. When proline is abundant, proline binding in the PRODH site reduces the FAD; reduction triggers a global conformational change (mediated by a flavin 2′-OH "toggle" and the FAD N5 environment) that dramatically increases membrane affinity, converting PutA into a **peripheral inner-membrane catabolic enzyme** that feeds electrons into the respiratory chain. In *P. putida* specifically, the repressor role was shown to be genetically **separable from catalysis** (a catalytically dead Glu896→Lys mutant still represses), and full proline-dependent induction additionally requires an unidentified σ⁵⁴(RpoN)-dependent activator. The partner protein **PutP**, an integral inner-membrane Na⁺/proline symporter encoded divergently, supplies the substrate.

---

## Key Findings

### F001 — Q88D80 is a trifunctional PutA: proline-catabolic enzyme plus *put*-gene repressor

UniProt Q88D80 (*P. putida* KT2440, PP_4947) is a 1,317-amino-acid, 142.6 kDa protein with a modular, multidomain architecture characteristic of the enteric trifunctional PutA. From N- to C-terminus it comprises: an **N-terminal ribbon-helix-helix (RHH) DNA-binding domain** (residues ~11–43); a PRODH N-terminal "arm" region (~87–257); a **proline dehydrogenase (βα)₈ barrel** carrying the FAD (~267–567); an **aldehyde-dehydrogenase / P5C(GSAL) dehydrogenase domain** (~654–1101, with catalytic residues near 881 and 915); and a **C-terminal domain** (~1102–1317). Two enzymatic activities are annotated: EC 1.5.5.2 (L-proline + quinone → (S)-1-pyrroline-5-carboxylate + quinol) and EC 1.2.1.88 (L-glutamate-5-semialdehyde + NAD⁺ + H₂O → L-glutamate + NADH), with FAD as cofactor. The presence of the N-terminal RHH domain places Q88D80 in the trifunctional ("Type C") class rather than the minimal bifunctional Type A/B PutAs, matching the ~1,320-residue *E. coli* enzyme.

The dual catalytic/regulatory nature of this enzyme family is well established. As stated for the enzyme mechanism, *"The bifunctional enzyme proline utilization A (PutA) catalyzes the two-step oxidation of L-proline to L-glutamate using proline dehydrogenase (PRODH) and L-glutamate-γ-semialdehyde dehydrogenase (GSALDH) domains"* ([PMID: 40738191](https://pubmed.ncbi.nlm.nih.gov/40738191/)), and the trifunctional character is captured by *"The trifunctional flavoprotein proline utilization A (PutA) links metabolism and gene regulation in Gram-negative bacteria by catalyzing the two-step oxidation of proline to glutamate and repressing transcription of the proline utilization regulon"* ([PMID: 22013066](https://pubmed.ncbi.nlm.nih.gov/22013066/)).

### F002 — The reactive P5C/GSA intermediate is channeled through a buried internal tunnel

The two catalytic sites in PutA are physically distant — approximately **42 Å apart** — yet the intermediate produced by PRODH must reach the P5CDH/GSALDH site. Structural work shows the sites are *"42 Å apart and connected by a buried tunnel that is hypothesized to channel the intermediates"* ([PMID: 40738191](https://pubmed.ncbi.nlm.nih.gov/40738191/)). Kinetic evidence directly demonstrates channeling: the coupled PRODH–P5CDH reaction *"is best described by a mechanism in which the intermediate is not released into the bulk medium, i.e., substrate channeling"* ([PMID: 24352662](https://pubmed.ncbi.nlm.nih.gov/24352662/)). An independent study of the *Salmonella* enzyme reached the same conclusion, indicating that *"PutA directly transfers the intermediate P5C between the two enzymatic functions via a 'leaky channel' mechanism"* ([PMID: 9637737](https://pubmed.ncbi.nlm.nih.gov/9637737/)).

Channeling is more than a kinetic curiosity: P5C is in a pH-dependent equilibrium with its ring-opened form GSA, and the hydrolysis of P5C to GSA is unfavorable at physiological pH. Sequestering the intermediate in a buried tunnel is proposed to facilitate this conversion and improve the overall efficiency of proline catabolism ([PMID: 22201749](https://pubmed.ncbi.nlm.nih.gov/22201749/)). Because Q88D80 possesses the same two-domain catalytic architecture and is ~74% identical to *E. coli* PutA (F005), the channeling mechanism is expected to be conserved in the *P. putida* enzyme. Supporting the generality of the mechanism, channeling has even been demonstrated between separate monofunctional PRODH and P5CDH enzymes, implying the core channeling pathway of bifunctional PutAs is broadly conserved ([PMID: 25492892](https://pubmed.ncbi.nlm.nih.gov/25492892/)).

### F003 — A redox-dependent switch moves PutA between cytoplasmic repressor and membrane-bound enzyme

One of the most distinctive features of trifunctional PutA is that its localization and function are governed by the redox state of its own flavin. Proline binding in the PRODH active site reduces the FAD, and *"the binding of proline in the proline dehydrogenase (PRODH) active site and subsequent reduction of the FAD trigger global conformational changes that enhance PutA-membrane affinity. These events cause PutA to switch from its repressor to its enzymatic role"* ([PMID: 19994913](https://pubmed.ncbi.nlm.nih.gov/19994913/)). Membrane binding is tightly coupled to flavin chemistry: *"Membrane binding was thus coincident with both flavin reduction and a change in protein conformation"*, with ~0.1 mM proline producing half-maximal FAD bleaching and half-maximal membrane association ([PMID: 8473341](https://pubmed.ncbi.nlm.nih.gov/8473341/)).

The molecular toggle responsible has been localized to the flavin itself: *"the FAD 2'-OH group acts as a redox-sensitive toggle switch that controls PutA-membrane binding"*, with the FAD N5–Arg interaction required for reductive activation of membrane binding ([PMID: 17209558](https://pubmed.ncbi.nlm.nih.gov/17209558/)). Importantly, PutA is a **peripheral, not integral, membrane protein**: *"PutA is a multifunctional, peripheral membrane protein which acts both as a transcriptional repressor for the put operon and enzyme catalyzing the two-step conversion of proline to glutamate"* ([PMID: 9637737](https://pubmed.ncbi.nlm.nih.gov/9637737/)). In the PRODH half-reaction the electrons ultimately pass to a membrane quinone (ubiquinone; EC 1.5.5.2), physically linking proline oxidation to the respiratory chain and rationalizing why the catalytically active form must associate with the inner membrane. Tryptophan-fluorescence stopped-flow studies further established that FAD reduction *precedes* the conformational transition, with W211 serving as the primary molecular marker of the change ([PMID: 16156643](https://pubmed.ncbi.nlm.nih.gov/16156643/)).

### F004 — Quaternary structure and domain roles: N-terminal domain dimerizes, C-terminal domain is a channel "lid"

Small-angle X-ray scattering of the 1,320-residue *E. coli* trifunctional PutA revealed a symmetric, V-shaped homodimer (~205 × 85 × 55 Å). Domain-deletion analysis assigned specific roles: *"Domain deletion analysis shows that the N-terminal DNA-binding domain mediates dimerization"* ([PMID: 22013066](https://pubmed.ncbi.nlm.nih.gov/22013066/)) — so the same RHH module that binds operator DNA also holds the dimer together. The ~200-residue C-terminal domain, in turn, was proposed to seal the channeling cavity: *"this domain serves as a lid that covers the internal substrate channeling cavity, thus preventing escape of the catalytic intermediate"* ([PMID: 22013066](https://pubmed.ncbi.nlm.nih.gov/22013066/)).

The modularity of the three functions is demonstrated by engineering studies: fusing a DNA-binding domain onto a naturally bifunctional PutA converts it into a functional trifunctional chimera ([PMID: 27742866](https://pubmed.ncbi.nlm.nih.gov/27742866/)), and in Type B PutAs the C-terminal domain contributes to aldehyde dehydrogenase activity and channeling ([PMID: 25137435](https://pubmed.ncbi.nlm.nih.gov/25137435/)). Because Q88D80 retains all of these modules, the same structural logic — RHH-mediated dimerization and C-terminal capping of the tunnel — is expected to apply.

### F005 — Q88D80 is a full-length ortholog of *E. coli* PutA (~74% identity) with conserved ALDH catalytic residues

A banded Needleman–Wunsch global alignment of Q88D80 (1,317 aa) against *E. coli* trifunctional PutA P09546 (1,320 aa) yielded **988 identical positions over 1,337 aligned columns = 73.9% amino-acid identity across the entire length**, spanning the N-terminal RHH region, the PRODH (βα)₈ barrel, and the ALDH/P5CDH domain. The aldehyde-dehydrogenase catalytic dyad is intact: **Glu881** sits in the canonical ALDH general-base motif (…IPLIA-**E**TGG-QN…), and **Cys915** is the nucleophilic catalytic cysteine (…SAGQR-**C**-SALRV…). This is the same catalytic pairing found throughout the aldehyde-dehydrogenase superfamily.

This high, full-length identity is the linchpin that justifies transferring the mechanistic conclusions from the enteric model enzymes to the *P. putida* protein. The reference class is defined by *"The trifunctional flavoprotein proline utilization A (PutA) links metabolism and gene regulation in Gram-negative bacteria by catalyzing the two-step oxidation of proline to glutamate and repressing transcription of the proline utilization regulon"* ([PMID: 22013066](https://pubmed.ncbi.nlm.nih.gov/22013066/)).

### F006 — *P. putida*-specific: PutA is a single 1,315-aa polypeptide catalyzing both steps; PutP is the inner-membrane proline permease

Beyond inference from homology, the *P. putida* *put* system has been directly characterized. The *putA* gene *"codes for a protein of 1,315 amino acid residues which is homologous to the PutA protein of Escherichia coli, Salmonella enterica serovar Typhimurium, Rhodobacter capsulatus, and several Rhizobium strains"* ([PMID: 10613867](https://pubmed.ncbi.nlm.nih.gov/10613867/)). Its central region is homologous to proline dehydrogenase and its C-terminal region to P5C dehydrogenase, so *"in P. putida, both enzymatic steps for proline conversion to glutamic acid are catalyzed by a single polypeptide"* ([PMID: 10613867](https://pubmed.ncbi.nlm.nih.gov/10613867/)). The reported size (1,315 aa) matches UniProt Q88D80 (1,317 aa; PP_4947), confirming the identity of the research target.

The adjacent, divergently transcribed *putP* gene encodes the substrate-supplying transporter: *"its gene product is an integral inner-membrane protein involved in the uptake of proline"* ([PMID: 10613867](https://pubmed.ncbi.nlm.nih.gov/10613867/)). Both genes are induced by proline — including proline present in corn root exudates, relevant to *P. putida*'s rhizosphere lifestyle. Notably, the *P. aeruginosa* PutA is only ~47% identical to the *P. putida* enzyme and lacks the regulatory function ([PMID: 12270821](https://pubmed.ncbi.nlm.nih.gov/12270821/)), underscoring that *P. putida* PutA belongs firmly to the enteric-type, regulatory class rather than the divergent *P. aeruginosa* type.

### F007 — *P. putida* PutA is an autogenous repressor; repression is separable from catalysis, and induction needs a σ⁵⁴-dependent activator

In *P. putida* the *putA* and *putP* genes are transcribed divergently and PutA represses both. Genetic evidence is direct: *"The PutA protein acts as a repressor of put gene expression in P. putida because expression from the put promoters is constitutive in a host background with a knockout putA gene"* ([PMID: 11097893](https://pubmed.ncbi.nlm.nih.gov/11097893/)). Crucially, the regulatory function is separable from catalysis: *"This regulatory activity is independent of the catabolic activity of PutA, because we show that a point mutation (Glu896-->Lys) that prevents catalytic activity allowed the protein to retain its regulatory activity"* ([PMID: 11097893](https://pubmed.ncbi.nlm.nih.gov/11097893/)). This confirms that DNA binding is an autonomous property of the RHH module and not a byproduct of the catalytic domains.

Full proline-dependent induction, however, requires more than relief of repression. The system *"requires a positive regulatory protein, still unidentified, whose expression seems to be sigma(54) dependent"* ([PMID: 11097893](https://pubmed.ncbi.nlm.nih.gov/11097893/)). This is a genuine mechanistic distinction from the enteric paradigm and from *P. aeruginosa*, where the AraC/XylS-family activator PruR controls *putAP* ([PMID: 12270821](https://pubmed.ncbi.nlm.nih.gov/12270821/)).

### F008 — PRODH FAD-binding and redox-switch residues are fully conserved in Q88D80

Mapping the crystallographically defined *E. coli* PRODH active-site residues onto Q88D80 via the global alignment shows every one is conserved: **Ec Lys329 → Q88D80 Lys327** (the lysine covalently crosslinked to FAD N5 by the mechanism-based inactivator N-propargylglycine), **Ec Asp370 → Asp368** (part of the FAD N5 electrostatic network), **Ec Arg431 → Arg429** (hydrogen-bonds FAD N5), and **Ec Arg556 → Arg554** (hydrogen-bonds the FAD ribityl 2′-OH redox toggle). The inactivation chemistry that pinpointed the key lysine is described as follows: *"N-propargylglycine irreversibly inactivates PutA by covalently linking the flavin N(5) atom to the epsilon-amino of Lys329"* ([PMID: 19994913](https://pubmed.ncbi.nlm.nih.gov/19994913/)); and the 2′-OH toggle contacted by Arg554 is the element that *"acts as a redox-sensitive toggle switch that controls PutA-membrane binding"* ([PMID: 17209558](https://pubmed.ncbi.nlm.nih.gov/17209558/)). Combined with the conserved ALDH dyad (Glu881/Cys915, F005), both active sites and the full flavin redox-switch machinery are structurally intact in the *P. putida* enzyme.

---

## Mechanistic Model / Interpretation

### The reaction PutA catalyzes

PutA carries out the complete four-electron oxidation of proline to glutamate in two coupled half-reactions:

```
        PRODH domain (FAD)                     P5CDH/GSALDH domain (NAD+)
                                    (spontaneous
                                     ring opening/
                                     hydrolysis)
 L-proline  ──────────►  Δ1-P5C  ◄════════►  L-glutamate-γ-      ──────────►  L-glutamate
   + FAD                  + FADH2              semialdehyde (GSA)   + NAD+        + NADH
   (EC 1.5.5.2)                                                    (EC 1.2.1.88)
      │                                                                │
      ▼  electrons                                                     ▼  hydride
   membrane quinone (ubiquinone) → respiratory chain             to NAD+ → NADH

   [====================  buried ~42 Å channeling tunnel  ====================]
                 (P5C/GSA never released to bulk solvent; C-terminal domain = lid)
```

**Step 1 (PRODH, EC 1.5.5.2):** The (βα)₈-barrel PRODH domain uses non-covalently bound FAD to abstract two electrons and two protons from L-proline, generating Δ¹-pyrroline-5-carboxylate (P5C) and reduced flavin. The reduced flavin is reoxidized by a membrane-embedded quinone, coupling proline oxidation to aerobic respiration. Active-site residues Lys327, Asp368, Arg429 (FAD N5 network) and Arg554 (ribityl 2′-OH) — all conserved in Q88D80 — organize the flavin and transmit its redox state to the protein surface.

**Intermediate handling:** P5C is in equilibrium with its hydrolyzed, ring-opened tautomer, L-glutamate-γ-semialdehyde (GSA). Rather than releasing this reactive species, PutA channels it through a buried internal tunnel (~42 Å) to the second active site. The C-terminal domain caps this cavity as a "lid," and channeling is thought to help drive the otherwise unfavorable P5C→GSA hydrolysis.

**Step 2 (P5CDH/GSALDH, EC 1.2.1.88):** The aldehyde-dehydrogenase-superfamily domain oxidizes GSA to L-glutamate using NAD⁺. Catalysis follows the canonical ALDH chemistry: Cys915 acts as the nucleophile that attacks the aldehyde to form a thiohemiacetal, and Glu881 serves as the general base — both conserved in Q88D80.

### The regulatory / localization switch

PutA is a **functional switch (a "moonlighting" flavoprotein)** whose behavior is dictated by proline availability, read out through FAD redox state:

| Condition | FAD state | Conformation | Localization | Role |
|---|---|---|---|---|
| Low proline | Oxidized | "Repressor" conformation | Cytoplasmic, DNA-bound | Represses divergent *putA*/*putP* promoters via N-terminal RHH domain |
| High proline | Reduced (proline-driven) | Global conformational change (2′-OH toggle, FAD N5 network, flexible W211 domain) | Peripheral inner-membrane | Catabolic enzyme; feeds electrons to respiratory quinone |

This design elegantly links metabolism and gene regulation: the same molecule *senses* proline (by trying to oxidize it), and the very act of catalysis (flavin reduction) flips it off the DNA and onto the membrane, de-repressing the genes exactly when substrate is present. In *P. putida* the two functions are experimentally separable (a catalytically dead mutant still represses), and de-repression alone is insufficient for full induction — a σ⁵⁴(RpoN)-dependent positive regulator is also required.

### Pathway context and localization

```
   Extracellular / periplasm            Inner membrane                 Cytoplasm
   ------------------------      ------------------------------    ------------------
        L-proline  ───────►   PutP (Na+/proline symporter,  ───►  L-proline
     (e.g. root exudates)       integral IM permease)                  │
                                                                       ▼
                          PutA (peripheral IM, reduced FAD) ── proline → glutamate
                                       │                                │
                                electrons → quinone/                    ▼
                                respiratory chain                  L-glutamate
                                                             (into central N/C metabolism:
                                                              TCA cycle / amino acid pools)
```

PutA thus enables *P. putida* to use proline as a **carbon, nitrogen, and energy source.** PutP concentrates proline across the inner membrane; PutA oxidizes it to glutamate, feeding both the carbon/nitrogen economy (glutamate → α-ketoglutarate / transamination) and the electron-transport chain (via the PRODH-to-quinone route). The rhizospheric relevance is notable: *P. putida put* genes respond to proline in corn root exudates ([PMID: 10613867](https://pubmed.ncbi.nlm.nih.gov/10613867/)).

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports this report |
|---|---|---|
| [22013066](https://pubmed.ncbi.nlm.nih.gov/22013066/) | *SAXS of trifunctional E. coli PutA* | Defines the trifunctional class; assigns N-terminal domain to dimerization and C-terminal domain to a channel lid (F001, F004). |
| [40738191](https://pubmed.ncbi.nlm.nih.gov/40738191/) | *Covalent intermediates & conformational states of PutA* | States the two catalytic activities and the 42 Å buried channeling tunnel (F001, F002). |
| [24352662](https://pubmed.ncbi.nlm.nih.gov/24352662/) | *Hysteretic substrate channeling in PutA* | Kinetic proof of substrate channeling — intermediate not released to solvent (F002). |
| [9637737](https://pubmed.ncbi.nlm.nih.gov/9637737/) | *Salmonella PutA leaky channel* | Independent channeling evidence; establishes peripheral membrane + dual repressor/enzyme roles (F002, F003). |
| [22201749](https://pubmed.ncbi.nlm.nih.gov/22201749/) | *Substrate channeling in proline metabolism (review)* | Rationale: channeling drives unfavorable P5C→GSA hydrolysis (F002). |
| [25492892](https://pubmed.ncbi.nlm.nih.gov/25492892/) | *Channeling in monofunctional PRODH–P5CDH pair* | Shows the channeling pathway is conserved even in separate enzymes — reinforces F002. |
| [19994913](https://pubmed.ncbi.nlm.nih.gov/19994913/) | *N-propargylglycine-inactivated PRODH structure* | Redox-driven repressor→enzyme switch; identifies Lys329 at FAD N5 (F003, F008). |
| [8473341](https://pubmed.ncbi.nlm.nih.gov/8473341/) | *Conformation & membrane association coincident with FAD reduction* | Couples FAD reduction, conformational change, and membrane binding; ~0.1 mM proline half-maximal (F003). |
| [17209558](https://pubmed.ncbi.nlm.nih.gov/17209558/) | *Flavin N5 and ribityl 2′-OH in PutA–membrane binding* | Identifies the FAD 2′-OH redox toggle controlling membrane binding (F003, F008). |
| [16156643](https://pubmed.ncbi.nlm.nih.gov/16156643/) | *Trp fluorescence of proline-dependent conformational change* | Shows FAD reduction precedes the conformational transition; W211 as molecular marker (F003). |
| [10613867](https://pubmed.ncbi.nlm.nih.gov/10613867/) | ***P. putida** put genes cloning/characterization* | Direct evidence: single 1,315-aa polypeptide catalyzes both steps; PutP is IM permease; root-exudate induction (F006). |
| [11097893](https://pubmed.ncbi.nlm.nih.gov/11097893/) | *Control of divergent **P. putida** put promoters* | PutA is a repressor; regulation separable from catalysis (E896K); σ⁵⁴-dependent activator required (F007). |
| [12270821](https://pubmed.ncbi.nlm.nih.gov/12270821/) | ***P. aeruginosa** putAP / PruR* | Contrast: *P. aeruginosa* PutA only ~47% identical and non-regulatory — distinguishes *P. putida*'s enteric-type system (F006, F007). |
| [27742866](https://pubmed.ncbi.nlm.nih.gov/27742866/) | *Engineering a trifunctional PutA chimera* | Demonstrates modularity of the three PutA functions (F004). |
| [25137435](https://pubmed.ncbi.nlm.nih.gov/25137435/) | *Type B PutA C-terminal domain* | C-terminal domain contributes to ALDH activity and channeling (F004). |
| [28712849](https://pubmed.ncbi.nlm.nih.gov/28712849/) | *Structure, function, mechanism of PutA (review)* | Authoritative synthesis of PutA biology underpinning the whole report. |

**Consistency of the evidence.** Multiple independent lines converge: two organisms (*E. coli*, *Salmonella*) independently demonstrate substrate channeling; structural, kinetic, and spectroscopic methods all support the redox-driven localization switch; and direct genetic/biochemical work in *P. putida* itself confirms the single-polypeptide bifunctional catalysis and the repressor role. No reviewed study contradicts the annotation. The only cross-species caveat is regulatory: *P. aeruginosa* diverges from *P. putida*, which is why the direct *P. putida* studies (F006, F007) are weighted most heavily for the regulation claims.

---

## Limitations and Knowledge Gaps

1. **No experimental structure of Q88D80 itself.** The domain assignments, catalytic residues, channeling tunnel, and redox switch for the *P. putida* protein are inferred from ~74% full-length identity to *E. coli* PutA and from residue-level conservation, not from a *P. putida* crystal structure or in vitro kinetics of the purified enzyme. Confidence is high but the specific values (Km, kcat, channeling efficiency) for Q88D80 are not directly measured.

2. **Quinone identity and respiratory coupling.** The PRODH electron acceptor is annotated as a membrane quinone (ubiquinone) based on the enteric model. The specific physiological electron acceptor in *P. putida* under aerobic vs. microaerobic conditions has not been experimentally pinned down here.

3. **The σ⁵⁴-dependent activator is unidentified.** *P. putida put* induction requires a positive regulator whose expression appears RpoN-dependent, but the identity of this activator and its binding site remain unknown ([PMID: 11097893](https://pubmed.ncbi.nlm.nih.gov/11097893/)).

4. **Operator/DNA-binding site not mapped for *P. putida*.** While PutA is established as an autogenous repressor, the precise operator sequence(s) at the divergent *putA*/*putP* promoters and the stoichiometry of PutA–DNA binding in *P. putida* are not detailed.

5. **Membrane-association determinants in *P. putida*.** The redox toggle residues are conserved, but whether *P. putida* PutA associates with the same membrane lipids/regions and with identical proline-response thresholds (~0.1 mM in *E. coli*) has not been directly measured.

6. **Physiological/ecological role.** Proline utilization is linked to rhizosphere colonization (root-exudate induction), but the quantitative contribution of PutA to *P. putida* fitness, osmotic stress response, or plant association is outside the reviewed dataset.

---

## Proposed Follow-up Experiments / Actions

1. **Purify and kinetically characterize recombinant Q88D80.** Measure steady-state parameters for PRODH (proline + quinone analog) and P5CDH (GSA + NAD⁺), and demonstrate coupled-assay channeling directly for the *P. putida* enzyme (mirroring [PMID: 24352662](https://pubmed.ncbi.nlm.nih.gov/24352662/)). This would convert the strongest inferences (F002, F005) into direct measurements.

2. **Determine the structure of Q88D80** by cryo-EM or X-ray crystallography (or validate a high-quality AlphaFold model with Phenix), confirming the RHH domain, (βα)₈ PRODH barrel, ALDH domain, the ~42 Å tunnel, and the C-terminal lid.

3. **Test the redox-driven membrane switch in *P. putida*.** Use proline titration with flavin-bleaching spectroscopy and membrane-fractionation/co-sedimentation assays to confirm reduction-coupled peripheral membrane association, and site-directed mutagenesis of Arg554 (2′-OH toggle) / Lys327 to test the switch.

4. **Identify the σ⁵⁴-dependent activator.** Combine RpoN-dependent promoter prediction, transposon/CRISPRi screens for loss of proline induction, and ChIP/EMSA to find the activator and its binding site at the divergent *put* promoters ([PMID: 11097893](https://pubmed.ncbi.nlm.nih.gov/11097893/)).

5. **Map the *put* operator and quantify repression.** EMSA and DNase footprinting with purified PutA and the *P. putida* *putA*/*putP* intergenic region; complement with the catalytically dead E896K variant to reproduce the catalysis-independent repression result in vivo.

6. **Confirm the physiological electron acceptor.** Test PRODH activity with the native *P. putida* quinone pool and probe respiratory coupling (e.g., in quinone-biosynthesis or terminal-oxidase mutants).

7. **Assess ecological relevance.** Compare wild-type vs. Δ*putA* / Δ*putP* strains for growth on proline as sole C/N source, osmotic-stress tolerance, and root/rhizosphere colonization to quantify PutA's physiological contribution.

---

## Conclusion

All available evidence — full-length ~74% identity to the well-studied *E. coli* enzyme, conservation of every catalytic and redox-switch residue, and direct biochemical/genetic characterization of the *P. putida* *put* system — supports a confident, high-resolution functional annotation. **PutA (Q88D80, PP_4947) is a trifunctional FAD-dependent flavoenzyme that oxidizes L-proline to L-glutamate in two channeled steps (PRODH, EC 1.5.5.2; P5C/GSAL dehydrogenase, EC 1.2.1.88) and, through an N-terminal ribbon-helix-helix domain, serves as the redox-regulated autogenous repressor of the divergent *put* genes, switching between a cytoplasmic DNA-bound repressor and a peripheral inner-membrane catabolic enzyme in response to proline-driven flavin reduction.**


## Artifacts

- [OpenScientist final report](putA-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](putA-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:40738191
2. PMID:22013066
3. PMID:24352662
4. PMID:9637737
5. PMID:22201749
6. PMID:25492892
7. PMID:19994913
8. PMID:8473341
9. PMID:17209558
10. PMID:16156643
11. PMID:27742866
12. PMID:25137435
13. PMID:10613867
14. PMID:12270821
15. PMID:11097893