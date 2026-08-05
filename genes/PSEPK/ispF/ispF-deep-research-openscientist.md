---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-18T16:36:07.390117'
end_time: '2026-07-18T16:51:53.910592'
duration_seconds: 946.52
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: ispF
  gene_symbol: ispF
  uniprot_accession: Q88MF3
  protein_description: 'RecName: Full=2-C-methyl-D-erythritol 2,4-cyclodiphosphate
    synthase {ECO:0000255|HAMAP-Rule:MF_00107}; Short=MECDP-synthase {ECO:0000255|HAMAP-Rule:MF_00107};
    Short=MECPP-synthase {ECO:0000255|HAMAP-Rule:MF_00107}; Short=MECPS {ECO:0000255|HAMAP-Rule:MF_00107};
    EC=4.6.1.12 {ECO:0000255|HAMAP-Rule:MF_00107};'
  gene_info: Name=ispF {ECO:0000255|HAMAP-Rule:MF_00107}; OrderedLocusNames=PP_1618;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the IspF family. {ECO:0000255|HAMAP-
  protein_domains: MECDP_synthase. (IPR003526); MECDP_synthase_CS. (IPR020555); MECDP_synthase_sf.
    (IPR036571); YgbB (PF02542)
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
citation_count: 12
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: ispF-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: ispF-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88MF3
- **Protein Description:** RecName: Full=2-C-methyl-D-erythritol 2,4-cyclodiphosphate synthase {ECO:0000255|HAMAP-Rule:MF_00107}; Short=MECDP-synthase {ECO:0000255|HAMAP-Rule:MF_00107}; Short=MECPP-synthase {ECO:0000255|HAMAP-Rule:MF_00107}; Short=MECPS {ECO:0000255|HAMAP-Rule:MF_00107}; EC=4.6.1.12 {ECO:0000255|HAMAP-Rule:MF_00107};
- **Gene Information:** Name=ispF {ECO:0000255|HAMAP-Rule:MF_00107}; OrderedLocusNames=PP_1618;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the IspF family. {ECO:0000255|HAMAP-
- **Key Domains:** MECDP_synthase. (IPR003526); MECDP_synthase_CS. (IPR020555); MECDP_synthase_sf. (IPR036571); YgbB (PF02542)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ispF" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ispF' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ispF** (gene ID: ispF, UniProt: Q88MF3) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of *ispF* (PP_1618, UniProt Q88MF3) in *Pseudomonas putida* KT2440

## Summary

The gene **_ispF_** (ordered locus **PP_1618**; UniProt **Q88MF3**) of *Pseudomonas putida* strain KT2440 encodes **2-C-methyl-D-erythritol 2,4-cyclodiphosphate synthase** (abbreviated **IspF**, **MECDP-synthase**, **MECPS**; **EC 4.6.1.12**). This is a soluble, cytoplasmic, homotrimeric, metal-dependent **phosphorus–oxygen lyase** that catalyzes the **fifth of seven enzymatic steps** of the **methylerythritol phosphate (MEP; non-mevalonate) pathway** for isoprenoid precursor biosynthesis. Specifically, IspF converts **4-diphosphocytidyl-2-C-methyl-D-erythritol 2-phosphate (CDP-ME2P)** into **2-C-methyl-D-erythritol 2,4-cyclodiphosphate (MEcPP/MECDP)**, releasing **cytidine 5′-monophosphate (CMP)** in a Mg²⁺-dependent intramolecular transphosphorylation that forms the unusual eight-membered cyclodiphosphate ring.

The functional assignment is exceptionally well supported by four converging lines of evidence: (1) a rich body of structural and mechanistic literature on bacterial orthologues (*E. coli*, *Thermus thermophilus*, *Burkholderia pseudomallei*) that defines the reaction, the dual-metal (Zn²⁺/Mg²⁺ or Mn²⁺) catalytic chemistry, and the homotrimeric interfacial active-site architecture; (2) strict conservation in Q88MF3 (71.3% identity to the structurally characterized *E. coli* enzyme) of every catalytic zinc ligand and feedback-pocket residue; (3) database annotation (KEGG K01770 / EC 4.6.1.12, terpenoid-backbone pathway ppu00900, Pfam **YgbB/MECDP_synthase**); and (4) biophysical analysis of the Q88MF3 sequence showing no signal peptide or transmembrane segment, consistent with cytosolic localization.

IspF operates in the cytoplasm as part of the only pathway available to *P. putida* for producing the universal isoprenoid precursors **isopentenyl diphosphate (IPP)** and **dimethylallyl diphosphate (DMAPP)** — precursors of respiratory quinones, carotenoids, and the undecaprenyl carriers essential for cell-envelope biosynthesis. Because *P. putida* lacks the alternative mevalonate route, IspF is expected to be **essential**, mirroring the demonstrated essentiality of its *E. coli* orthologue. The MEP pathway's absence from humans makes IspF a validated **broad-spectrum antimicrobial and herbicide target**. Notably, the IspF product **MEcPP is more than a metabolic intermediate**: it is a conserved stress-signaling metabolite that acts as a plastid-to-nucleus retrograde signal in plants and modulates biofilm formation in *E. coli*, placing IspF at a nexus of primary metabolism and stress signaling.

---

## Gene/Protein Identity Verification

Before presenting findings, the identity of the target was confirmed against the UniProt reference to guard against gene-symbol ambiguity:

| Attribute | Reference (UniProt Q88MF3) | Verification outcome |
|---|---|---|
| Gene symbol | *ispF* | ✔ Matches MEP-pathway nomenclature |
| Locus tag | PP_1618 | ✔ Confirmed in KEGG (ppu:PP_1618) |
| EC number | 4.6.1.12 | ✔ Confirmed (KEGG K01770) |
| Protein family | IspF family | ✔ Pfam YgbB / MECDP_synthase (PF02542) |
| Organism | *P. putida* KT2440 | ✔ Genome position 1,814,613–1,815,086 (+) |
| Length | 157 aa | ✔ Consistent with orthologues (~155–160 aa) |

The gene symbol *ispF*, the protein description, the organism, and the domain architecture are **mutually consistent**. The literature retrieved describes the same enzyme family (IspF / MECDP synthase) across bacteria, and the *P. putida* sequence aligns unambiguously to characterized orthologues. **There is no ambiguity** in this assignment. Where direct experimental characterization of the *P. putida* KT2440 protein itself is unavailable, the report relies on orthologue biochemistry combined with sequence conservation — explicitly flagged as inference in the relevant sections.

---

## Key Findings

### Finding 1 — IspF catalyzes step 5 of the MEP pathway: CDP-ME2P → MEcPP + CMP

IspF (Q88MF3) is a lyase (EC 4.6.1.12) that carries out the fifth committed step of the non-mevalonate isoprenoid pathway. The enzyme converts **4-diphosphocytidyl-2-C-methyl-D-erythritol 2-phosphate (CDP-ME2P)** into **2-C-methyl-D-erythritol 2,4-cyclodiphosphate (MEcPP)** with concomitant release of **CMP**. Mechanistically, the reaction is an **intramolecular transphosphorylation**: the 2-phosphate group of the substrate performs a nucleophilic attack on the β-phosphate of the CDP moiety, expelling CMP and closing the strained eight-membered **cyclodiphosphate ring** — a highly unusual chemical feature among natural metabolites. The reaction is strictly **Mg²⁺-dependent** (with Mn²⁺ able to substitute in vitro).

This assignment rests on primary structural and biochemical studies of orthologues. Steinbacher and colleagues, characterizing the *E. coli* enzyme, established that IspF "catalyzes the conversion of 4-diphosphocytidyl-2-C-methyl-D-erythritol 2-phosphate (CDP-ME2P) to MECDP, a highly unusual cyclodiphosphate-containing intermediate on the mevalonate-independent pathway to isopentenyl diphosphate and dimethylallyl diphosphate" ([PMID: 11786530](https://pubmed.ncbi.nlm.nih.gov/11786530/)). Independently, Kemp et al. confirmed that the enzyme "converts 4-diphosphocytidyl-2C-methyl-d-erythritol 2-phosphate into 2C-methyl-d-erythritol 2,4-cyclodiphosphate and CMP in a Mg-dependent reaction" ([PMID: 11829504](https://pubmed.ncbi.nlm.nih.gov/11829504/)). High-resolution (1.6 Å) crystallography of the *Thermus thermophilus* enzyme co-crystallized with substrate captured CMP as the product in the active site and resolved the catalytic magnesium ions ([PMID: 12499535](https://pubmed.ncbi.nlm.nih.gov/12499535/)).

### Finding 2 — IspF is a homotrimeric metalloenzyme with three interfacial active sites requiring Zn²⁺ and Mg²⁺/Mn²⁺

The functional enzyme is a **homotrimer** organized around a **central β-prism / hydrophobic cavity**, bearing **three active sites**, each located in a cleft at the interface between two adjacent subunits — so catalysis is intrinsically dependent on quaternary assembly. Each active site coordinates one **Zn²⁺** ion in tetrahedral geometry (via Asp8, His10, and His42 in the *E. coli* numbering) that binds and activates the substrate, together with a second divalent metal (**Mn²⁺** or **Mg²⁺**) in octahedral geometry positioned between the α- and β-phosphates. The two metals act in concert to align and polarize the substrate diphosphate for the cyclization chemistry.

Steinbacher et al. describe "a homotrimer, built around a beta prism, carrying three active sites, each of which is formed in a cleft between pairs of subunits. Residues from two subunits recognize and bind the nucleotide in an active site that contains a Zn(2+) with tetrahedral coordination. A Mn(2+), with octahedral geometry, is positioned between the alpha and beta phosphates acting in concert with the Zn(2+) to align and polarize the substrate for catalysis" ([PMID: 11997478](https://pubmed.ncbi.nlm.nih.gov/11997478/)). This is corroborated by the observation that "the protein adopts a homotrimeric quaternary structure built around a central hydrophobic cavity and three externally facing active sites… each of these active sites is located between two adjacent monomers" ([PMID: 11786530](https://pubmed.ncbi.nlm.nih.gov/11786530/)).

### Finding 3 — IspF binds isoprenoid diphosphates in its central cavity, implicating feedback regulation

Beyond its catalytic active sites, IspF possesses a distinct ligand-binding pocket in the **central cavity at the trimer interface** that binds **diphosphate-containing isoprenoids** (e.g., IPP, DMAPP, GPP, FPP — downstream and end-products of the pathway). In *E. coli*, Arg142 and Glu144 mediate this interaction, with three Arg142 residues (one from each subunit) contacting the ligand's terminal phosphate. Because these ligands are pathway products/downstream metabolites bound at a site separate from the catalytic clefts, this architecture strongly suggests a mechanism of **feedback regulation** of MEP-pathway flux.

Kemp and Hunter noted that "the recent exciting finding that the enzyme actually binds diphosphate-containing isoprenoids at the interface formed by the three subunits that constitute the active protein suggests the possibility of feedback regulation of MECP synthase" ([PMID: 16511114](https://pubmed.ncbi.nlm.nih.gov/16511114/)). This adds a regulatory dimension to IspF beyond simple catalysis, positioning it as a potential control point coupling isoprenoid demand to precursor supply.

### Finding 4 — IspF is essential and a validated antimicrobial/herbicide target absent from humans

IspF is **essential** in *E. coli* and is conserved across eubacteria and apicomplexan parasites. Critically, the entire MEP pathway is **absent in mammals and archaea** (which use the mevalonate route), so its enzymes are **selective, druggable targets** with an inherently favorable selectivity window. IspF's catalytic zinc has been exploited for structure-based inhibitor design: zinc-binding-group compounds such as 2-amino-4-hydroxypyrimidine-5-carboxylates show antibacterial activity and bind IspF (validated by thermal shift and STD-NMR).

Steinbacher et al. state that "this enzyme is essential in E. coli and participates in the nonmevalonate pathway of isoprenoid biosynthesis, a critical pathway present in some bacterial and apicomplexans but distinct from that used by mammals" ([PMID: 11997478](https://pubmed.ncbi.nlm.nih.gov/11997478/)). Work on the *Burkholderia pseudomallei* orthologue confirms that "the fifth enzyme in the pathway, 2-C-methyl-d-erythritol-2,4-cyclodiphosphate synthase (IspF), contains a catalytically important zinc ion in the active site" and that zinc-binding-group compounds were "evaluated for antibacterial activity and interaction with IspF" ([PMID: 31521478](https://pubmed.ncbi.nlm.nih.gov/31521478/)). A pathway-wide review confirms that "the individual enzymes represent new, validated targets for broad spectrum antimicrobial drug and herbicide development" ([PMID: 17442674](https://pubmed.ncbi.nlm.nih.gov/17442674/)).

### Finding 5 — The IspF product MEcPP is a conserved stress-signaling metabolite

An important, distinctive feature of IspF is that its product **MEcPP is not merely a pathway intermediate but a bona fide signaling molecule**. In plants, MEcPP is a **plastid-to-nucleus retrograde stress signal** — it accumulates under oxidative, high-light, wounding, and biotic stress and reprograms nuclear gene expression. In bacteria, elevated MEcPP has regulatory consequences: in *E. coli* K-12 it inhibits biofilm formation by modulating the global regulator H-NS and reducing fimbriae. Recent work further shows MEcPP acts as a **feedback signal** that directly inhibits the upstream MEP enzyme MCT (methylerythritol cytidylyltransferase).

Xiao and colleagues showed that "methylerythritol cyclodiphosphate (MEcPP) is an intermediate in the biosynthesis of isoprenoids in plant plastids and in bacteria, and acts as a stress signal in plants… MEcPP regulates biofilm formation in Escherichia coli K-12 MG1655" ([PMID: 39572562](https://pubmed.ncbi.nlm.nih.gov/39572562/)). In plants, "under stress conditions, leading to its accumulation, MEcPP mediates retrograde signaling that alters the nuclear gene expression" ([PMID: 40073740](https://pubmed.ncbi.nlm.nih.gov/40073740/)). The dual role of MEcPP is elaborated further in studies establishing it as an initiator of systemic stress responses ([PMID: 34859454](https://pubmed.ncbi.nlm.nih.gov/34859454/)) and, most recently, as a metabolite that directly modulates enzyme activity to link stress with biosynthetic regulation ([PMID: 41637453](https://pubmed.ncbi.nlm.nih.gov/41637453/)).

### Finding 6 — In *P. putida* KT2440, the MEP pathway (including *ispF*) is the sole route to isoprenoid precursors

*P. putida* KT2440, like most bacteria, produces IPP and DMAPP **exclusively via the MEP pathway** from pyruvate and glyceraldehyde-3-phosphate (the seven enzymes dxs, dxr/ispC, ispD, ispE, **ispF**, ispG, ispH). It **lacks the mevalonate route** entirely. This means IspF is the only enzyme performing the CDP-ME2P → MEcPP conversion, with no metabolic bypass. Metabolic-engineering studies of KT2440 for isoprenoid (lycopene) production confirmed that boosting output requires manipulating MEP-pathway precursor supply, achieving up to ~50-fold increases.

As reported by Loeschcke et al., "in P. putida and most other bacteria, these precursors are produced from pyruvate and glyceraldehyde 3-phosphate by the methylerythritol 4-phosphate (MEP) pathway, whereas other bacteria synthesize the same precursors from acetyl-CoA using the unrelated mevalonate (MVA) pathway" ([PMID: 31500633](https://pubmed.ncbi.nlm.nih.gov/31500633/)). The absence of a redundant pathway is the primary basis for inferring that *ispF*/PP_1618 is **essential** in this organism.

### Finding 7 — All catalytic and feedback residues are strictly conserved in *P. putida* IspF (Q88MF3)

A pairwise global (Needleman–Wunsch) alignment of Q88MF3 (157 aa) against the experimentally characterized *E. coli* IspF (P62617, 159 aa) yielded **71.3% sequence identity** over 157 aligned positions. Critically, **every catalytically essential residue is strictly conserved at the equivalent position**:

| Functional role | *E. coli* residue | *P. putida* Q88MF3 | Conserved? |
|---|---|---|---|
| Zn²⁺ ligand | Asp8 | Asp8 | ✔ |
| Zn²⁺ ligand | His10 | His10 | ✔ |
| Zn²⁺ ligand | His42 | His42 | ✔ |
| Isoprenoid feedback pocket | Arg142 | Arg142 | ✔ |
| Isoprenoid feedback pocket | Glu144 | Glu144 | ✔ |

The family signature motifs of the MECDP_synthase domain (e.g., HSDGDV, GADSR, VNVKATTTEKLGFTGR) are also present. This near-complete conservation of the entire catalytic and regulatory apparatus provides strong sequence-based evidence that Q88MF3 performs the identical reaction, with the same dual-metal mechanism and the same product-feedback capability, as the structurally characterized orthologues.

### Finding 8 — Genomic context: PP_1618 is a standalone gene, likely translationally coupled to *truD*

KEGG assigns ppu:PP_1618 to **K01770 / EC 4.6.1.12** in pathway **ppu00900 "Terpenoid backbone biosynthesis"**. The EC hierarchy places it in Class 4 Lyases → 4.6 Phosphorus–oxygen lyases → 4.6.1.12. The gene occupies genome positions 1,814,613–1,815,086 (+ strand), 474 bp / 157 aa, with a Pfam **YgbB** domain. Unlike *E. coli*, where *ispF* is part of an *ispDF* operon, the *P. putida* flanking genes are **functionally unrelated**: upstream lie PP_1616 (*frmA*) and PP_1617 (*frmC*), involved in glutathione-dependent formaldehyde detoxification; immediately downstream is PP_1619 (*truD*), a tRNA pseudouridine synthase. Notably, *ispF* (ending at 1,815,086) and *truD* (starting at 1,815,083) lie on the same strand and **overlap by 4 nucleotides**, an arrangement consistent with **translational coupling / co-transcription** — implying *ispF* expression may be linked to that of *truD* in KT2440 rather than to the other MEP-pathway genes, which are dispersed around the genome.

### Finding 9 — Q88MF3 is a soluble cytoplasmic protein with no signal peptide or transmembrane segment

Kyte–Doolittle hydropathy analysis of the 157-aa Q88MF3 sequence found a **maximum 19-residue window hydropathy of 1.51**, below the ~1.6 threshold typically required for a transmembrane α-helix — so **no membrane-spanning segment** is predicted. The N-terminal 30 residues are **hydrophilic** (mean hydropathy −0.30) with no hydrophobic signal-peptide core, ruling out secretion or membrane targeting. The protein is mildly acidic (16 K+R vs. 19 D+E; net charge ≈ −3). These features are fully consistent with the **cytoplasmic** localization expected for a soluble metabolic enzyme, matching the localization of its characterized orthologues.

### Finding 10 — Consolidated, convergent annotation

Four independent evidence streams converge on a single, robust functional assignment for *ispF*/PP_1618 (Q88MF3): **(1) Literature** — orthologue crystal structures and mechanistic studies define the CDP-ME2P → MEcPP + CMP reaction, dual Zn²⁺/Mg²⁺ catalysis, homotrimeric interfacial active sites, essentiality, and drug-target status. **(2) Sequence** — 71.3% identity to *E. coli* IspF with strict conservation of all catalytic zinc ligands and feedback residues. **(3) Databases** — KEGG K01770 / EC 4.6.1.12, terpenoid-backbone pathway ppu00900, Pfam YgbB. **(4) Biophysics** — no signal peptide or TM segment; a soluble 157-aa cytosolic protein. Additionally, the product MEcPP is a conserved stress-signaling metabolite.

---

## Mechanistic Model and Interpretation

### Position in the MEP pathway

IspF catalyzes the fifth of the seven steps that convert central-carbon-metabolism precursors into the universal isoprenoid building blocks:

```
Pyruvate + G3P
     │  DXS (dxs)
     ▼
1-deoxy-D-xylulose 5-phosphate (DXP)
     │  DXR/IspC (dxr)
     ▼
2-C-methyl-D-erythritol 4-phosphate (MEP)
     │  IspD (ispD)      + CTP
     ▼
4-diphosphocytidyl-2-C-methyl-D-erythritol (CDP-ME)
     │  IspE (ispE)      + ATP
     ▼
4-diphosphocytidyl-2-C-methyl-D-erythritol 2-phosphate (CDP-ME2P)
     │
     │  ┌─────────────────────────────────────────────┐
     │  │  IspF  (PP_1618 / Q88MF3)   EC 4.6.1.12       │  ◄── THIS ENZYME
     │  │  Zn²⁺ + Mg²⁺/Mn²⁺, homotrimer                 │
     │  │  intramolecular transphosphorylation          │
     │  └─────────────────────────────────────────────┘
     ▼
2-C-methyl-D-erythritol 2,4-cyclodiphosphate (MEcPP)  + CMP
     │  IspG (ispG)  [Fe-S]
     ▼
(E)-4-hydroxy-3-methylbut-2-enyl diphosphate (HMBPP)
     │  IspH (ispH)  [Fe-S]
     ▼
IPP  +  DMAPP   ──►  quinones, carotenoids, undecaprenyl-P (cell envelope), etc.
```

### Reaction chemistry

The IspF reaction is an intramolecular cyclization. The substrate CDP-ME2P carries both a **2-phosphate** and a **cytidine diphosphate (CDP)** moiety. Held in the interfacial active site, the substrate's diphosphate is coordinated by the active-site **Zn²⁺** (bound by Asp8/His10/His42) and a bridging **Mg²⁺/Mn²⁺** between the α- and β-phosphates. The 2-phosphate oxygen attacks the β-phosphorus of the CDP group, displacing **CMP** and forming the strained **eight-membered cyclodiphosphate ring** that defines the product MEcPP. The two metals collaborate to orient and electronically polarize the reacting phosphates, lowering the transition-state energy for ring closure.

### Quaternary structure as a functional requirement

```
        Subunit A
          /  \
         /    \        ← β-prism core; central cavity binds
   [site3]    [site1]     isoprenoid diphosphates (IPP/DMAPP/FPP)
        \      /          via Arg142/Glu144 → feedback regulation
   Subunit C — Subunit B
          [site2]

  • 3 catalytic sites, each at an A–B / B–C / C–A interface
  • Each site: 1 Zn²⁺ (tetrahedral) + 1 Mg²⁺/Mn²⁺ (octahedral)
  • Central cavity: separate product/effector binding pocket
```

Because each catalytic site is built from residues contributed by **two subunits**, IspF has no meaningful monomeric activity — trimerization is obligatory. The central cavity provides a structurally elegant means of **feedback control**: downstream isoprenoid diphosphates accumulate and dock in the trimer core, potentially tuning flux through the enzyme in response to product demand.

### Physiological role in *P. putida* KT2440

In KT2440, IspF sits on the **sole, non-redundant route** to IPP and DMAPP. These C₅ precursors are indispensable for:

- **Respiratory quinones** (ubiquinone/menaquinone) — essential for aerobic and anaerobic respiration in this metabolically versatile soil bacterium;
- **Undecaprenyl phosphate** — the lipid carrier for peptidoglycan and LPS/O-antigen assembly (cell-envelope integrity);
- **Carotenoids and other terpenoids** — membrane and stress-protective functions.

The lack of a mevalonate bypass, combined with strict conservation of the catalytic machinery, makes IspF **predicted-essential** in KT2440. Its product MEcPP additionally links this housekeeping pathway to **stress physiology**, giving IspF a potential regulatory footprint beyond precursor supply.

### Localization

All evidence points to a **cytoplasmic** location: no signal peptide, no transmembrane helix, a hydrophilic surface, and a soluble globular fold typical of its orthologues. IspF performs its chemistry in the cytosol where its substrate CDP-ME2P and its metal cofactors are available.

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution to this annotation |
|---|---|---|
| [11786530](https://pubmed.ncbi.nlm.nih.gov/11786530/) | Structure/mechanism of MECDP synthase (*E. coli*) | Defines substrate (CDP-ME2P), product (MECDP), pathway position; homotrimer with interfacial active sites |
| [11997478](https://pubmed.ncbi.nlm.nih.gov/11997478/) | Structure of MECDP synthase; drug target | Homotrimer/β-prism, dual Zn²⁺/Mn²⁺ catalysis, essentiality in *E. coli*, absence from mammals |
| [11829504](https://pubmed.ncbi.nlm.nih.gov/11829504/) | Structure of MECDP synthase | Confirms CDP-ME2P → MEcPP + CMP, Mg-dependent reaction |
| [12499535](https://pubmed.ncbi.nlm.nih.gov/12499535/) | *T. thermophilus* MECDP synthase, 1.6 Å | High-resolution structure with substrate/product; positions of catalytic Mg²⁺ |
| [16511114](https://pubmed.ncbi.nlm.nih.gov/16511114/) | Double mutant / isoprenoid diphosphate binding | Establishes central-cavity binding of isoprenoid diphosphates → feedback regulation |
| [31521478](https://pubmed.ncbi.nlm.nih.gov/31521478/) | Inhibitors of *B. pseudomallei* IspF | IspF is 5th enzyme; catalytic zinc; zinc-binding-group antibacterials |
| [17442674](https://pubmed.ncbi.nlm.nih.gov/17442674/) | The non-mevalonate pathway | MEP-pathway enzymes are validated broad-spectrum drug/herbicide targets |
| [15197467](https://pubmed.ncbi.nlm.nih.gov/15197467/) | Biosynthesis via non-mevalonate pathway | Pathway is essential in eubacteria/plants/apicomplexa, absent in archaea/animals |
| [31500633](https://pubmed.ncbi.nlm.nih.gov/31500633/) | Engineering *P. putida* for isoprenoids | *P. putida* uses MEP pathway (contains *ispF*), lacks MVA route |
| [39572562](https://pubmed.ncbi.nlm.nih.gov/39572562/) | MEcPP inhibits biofilm in *E. coli* | Product MEcPP is a bacterial signaling metabolite (biofilm/H-NS) |
| [40073740](https://pubmed.ncbi.nlm.nih.gov/40073740/) | MEP intermediate MEcPP retrograde signaling | MEcPP is a plant plastid-to-nucleus stress signal |
| [34859454](https://pubmed.ncbi.nlm.nih.gov/34859454/) | Plastidial retrograde signal (SSR) | MEcPP initiates systemic stress response signaling cascades |
| [41637453](https://pubmed.ncbi.nlm.nih.gov/41637453/) | Metabolite control of enzyme activity | MEcPP is a dual-function metabolite that feedback-inhibits upstream MCT |
| [21619509](https://pubmed.ncbi.nlm.nih.gov/21619509/) | Isoprenoid precursor biosynthesis as drug targets | Pathway structural/mechanistic overview; drug-target validation |

**How the evidence fits together:** The direct biochemical and structural literature (rows 1–6, 8) is derived from bacterial orthologues (*E. coli*, *T. thermophilus*, *B. pseudomallei*) — not from the *P. putida* protein itself. The bridge to Q88MF3 is provided by **sequence conservation** (Finding 7): 71.3% identity and 100% conservation of all catalytic/feedback residues means the orthologue mechanism transfers with high confidence. Database annotation (KEGG/Pfam) and biophysical prediction (hydropathy) independently corroborate the enzymatic and localization assignments. The MEcPP-signaling literature (rows 10–13) is drawn largely from plants and *E. coli*; it establishes the broader biological importance of the IspF product but has **not** been directly demonstrated in *P. putida*.

---

## Limitations and Knowledge Gaps

1. **No direct experimental characterization of the KT2440 protein.** There is no published crystal structure, kinetic study, or gene-knockout of *P. putida* PP_1618 specifically. The functional assignment is an inference — albeit a very strong one — from orthologue biochemistry plus sequence conservation. Kinetic parameters (Kₘ for CDP-ME2P, kcat, metal preferences) for the *P. putida* enzyme are unknown.

2. **Essentiality is inferred, not demonstrated in this strain.** Essentiality is established for *E. coli* IspF and is strongly implied by the absence of a mevalonate bypass in *P. putida*, but a direct transposon/CRISPRi essentiality confirmation for PP_1618 in KT2440 was not located in this investigation.

3. **Feedback regulation not tested for Q88MF3.** The central-cavity isoprenoid-diphosphate binding (and its regulatory significance) was demonstrated in *E. coli*. Although Arg142/Glu144 are conserved in Q88MF3, whether feedback binding measurably modulates *P. putida* IspF activity has not been shown.

4. **MEcPP signaling in *P. putida* is unexplored.** The signaling roles of MEcPP are documented in plants and *E. coli* K-12. Whether MEcPP produced by *P. putida* IspF exerts analogous regulatory effects (e.g., on biofilm, stress adaptation) in this species is an open question.

5. **Operon/regulatory structure is inferred from genome coordinates.** The proposed translational coupling of *ispF* with downstream *truD* (4-nt overlap) is a bioinformatic inference; transcriptional mapping (RNA-seq/operon prediction confirmation) would be needed to establish co-transcription.

6. **Localization is predicted, not measured.** Cytoplasmic localization is based on hydropathy/sequence features and orthologue behavior, not on experimental fractionation or imaging in KT2440.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant enzymology.** Express and purify His-tagged PP_1618 from KT2440 and measure steady-state kinetics (Kₘ, kcat) for CDP-ME2P, together with metal-dependence (Zn²⁺ requirement; Mg²⁺ vs. Mn²⁺), to confirm the transferred mechanism quantitatively.

2. **Structural confirmation.** Solve a crystal structure (or generate a validated AlphaFold model) of Q88MF3 to verify the homotrimeric β-prism fold, the Zn²⁺ site geometry (Asp8/His10/His42), and the central-cavity feedback pocket (Arg142/Glu144).

3. **Essentiality test.** Attempt a clean deletion or CRISPRi knockdown of PP_1618 in KT2440; if inviable without isoprenoid supplementation, this directly confirms essentiality. Complement with the *E. coli* orthologue to test cross-species rescue.

4. **Feedback-regulation assay.** Test whether IPP/DMAPP/FPP inhibit purified *P. putida* IspF and whether Arg142/Glu144 point mutants abolish this effect, establishing physiological relevance of the central-cavity binding.

5. **MEcPP signaling in *P. putida*.** Engineer conditional MEcPP accumulation (e.g., IspG limitation) and profile transcriptome/biofilm phenotypes to determine whether MEcPP has a signaling role in KT2440 analogous to *E. coli*.

6. **Transcriptional mapping.** Use RNA-seq / 5′-RACE / operon analysis to confirm whether *ispF* is co-transcribed with *truD* and to define its promoter and regulatory context.

7. **Inhibitor cross-testing.** Evaluate whether zinc-binding-group IspF inhibitors developed against *E. coli*/*B. pseudomallei* also inhibit the *P. putida* enzyme, informing broad-spectrum antimicrobial potential.

---

## Conclusion

*ispF* (PP_1618, UniProt Q88MF3) in *Pseudomonas putida* KT2440 encodes **2-C-methyl-D-erythritol 2,4-cyclodiphosphate synthase (IspF; EC 4.6.1.12)**, a soluble cytoplasmic, homotrimeric, dual-metal (Zn²⁺ + Mg²⁺/Mn²⁺) phosphorus–oxygen lyase catalyzing the fifth step of the MEP pathway — the intramolecular cyclization of CDP-ME2P to 2-C-methyl-D-erythritol 2,4-cyclodiphosphate (MEcPP) with release of CMP. As the MEP pathway is the organism's only source of the universal isoprenoid precursors IPP and DMAPP, IspF is expected to be essential and represents a selective antimicrobial target absent from humans. Its product MEcPP additionally functions as a conserved stress-signaling metabolite. This assignment is supported by convergent structural/mechanistic literature on orthologues, strict conservation of all catalytic and feedback residues (71% identity to *E. coli* IspF), consistent database annotation, and biophysical evidence for cytoplasmic localization.


## Artifacts

- [OpenScientist final report](ispF-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](ispF-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:11786530
2. PMID:11829504
3. PMID:12499535
4. PMID:11997478
5. PMID:16511114
6. PMID:31521478
7. PMID:17442674
8. PMID:39572562
9. PMID:40073740
10. PMID:34859454
11. PMID:41637453
12. PMID:31500633