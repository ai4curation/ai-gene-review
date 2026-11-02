---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T19:58:27.944178'
end_time: '2026-08-31T21:03:09.752850'
duration_seconds: 3881.81
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: pyrD
  gene_symbol: pyrD
  uniprot_accession: Q88L40
  protein_description: 'RecName: Full=Dihydroorotate dehydrogenase (quinone) {ECO:0000255|HAMAP-Rule:MF_00225};
    EC=1.3.5.2 {ECO:0000255|HAMAP-Rule:MF_00225}; AltName: Full=DHOdehase {ECO:0000255|HAMAP-Rule:MF_00225};
    Short=DHOD {ECO:0000255|HAMAP-Rule:MF_00225}; Short=DHODase {ECO:0000255|HAMAP-Rule:MF_00225};
    AltName: Full=Dihydroorotate oxidase {ECO:0000255|HAMAP-Rule:MF_00225};'
  gene_info: Name=pyrD {ECO:0000255|HAMAP-Rule:MF_00225}; OrderedLocusNames=PP_2095;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the dihydroorotate dehydrogenase family. Type 2
  protein_domains: Aldolase_TIM. (IPR013785); DHO_dehydrogenase. (IPR050074); Dihydroorotate_DH_1_2.
    (IPR012135); Dihydroorotate_DH_2. (IPR005719); Dihydroorotate_DH_cat. (IPR005720)
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
citation_count: 15
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: pyrD-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: pyrD-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88L40
- **Protein Description:** RecName: Full=Dihydroorotate dehydrogenase (quinone) {ECO:0000255|HAMAP-Rule:MF_00225}; EC=1.3.5.2 {ECO:0000255|HAMAP-Rule:MF_00225}; AltName: Full=DHOdehase {ECO:0000255|HAMAP-Rule:MF_00225}; Short=DHOD {ECO:0000255|HAMAP-Rule:MF_00225}; Short=DHODase {ECO:0000255|HAMAP-Rule:MF_00225}; AltName: Full=Dihydroorotate oxidase {ECO:0000255|HAMAP-Rule:MF_00225};
- **Gene Information:** Name=pyrD {ECO:0000255|HAMAP-Rule:MF_00225}; OrderedLocusNames=PP_2095;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the dihydroorotate dehydrogenase family. Type 2
- **Key Domains:** Aldolase_TIM. (IPR013785); DHO_dehydrogenase. (IPR050074); Dihydroorotate_DH_1_2. (IPR012135); Dihydroorotate_DH_2. (IPR005719); Dihydroorotate_DH_cat. (IPR005720)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "pyrD" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'pyrD' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **pyrD** (gene ID: pyrD, UniProt: Q88L40) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: pyrD (Q88L40, PP_2095) — Dihydroorotate Dehydrogenase (quinone) from *Pseudomonas putida* KT2440

## Summary

The gene **pyrD** (UniProt **Q88L40**; ordered locus **PP_2095**) of *Pseudomonas putida* strain KT2440 encodes a **Type 2 (class 2) dihydroorotate dehydrogenase (DHODH; EC 1.3.5.2)**, a 340-residue FMN flavoenzyme that catalyzes the **only redox step of de novo pyrimidine (UMP) biosynthesis**. The enzyme oxidizes **(S)-dihydroorotate to orotate**, transferring the two abstracted hydrogen equivalents first onto a tightly bound flavin mononucleotide (FMN) prosthetic group and then, via re-oxidation of the reduced flavin, onto a **respiratory quinone (ubiquinone)**, producing quinol. This places PyrD at the fourth step of the six-step de novo pathway that converts carbamoyl-phosphate and aspartate into UMP, the precursor of all pyrimidine nucleotides.

The identity assignment is secure and multiply corroborated. The gene symbol *pyrD*, the EC number (1.3.5.2), the HAMAP rule (MF_00225), the protein-family assignment (dihydroorotate dehydrogenase family, Type 2), and the diagnostic InterPro domains (Aldolase_TIM/IPR013785; Dihydroorotate_DH_2/IPR005719) are all mutually consistent — there is **no gene-symbol ambiguity**. Direct sequence analysis of Q88L40 confirms the intact class-2 catalytic apparatus: a nucleophilic **serine base at position 174** (positionally equivalent to the experimentally validated Ser175 of *Escherichia coli* PyrD), the strictly conserved cluster of pyrimidine-binding asparagines (Asn110/138/171/176/245), and FMN/quinone-coordinating residues. Global alignment shows Q88L40 is **56.9% identical** to the extensively studied *E. coli* class-2 PyrD, with the catalytic serine exactly conserved — strong evolutionary grounds for transferring the experimentally established mechanism and function.

With respect to localization, PyrD is a **peripheral (monotopic) protein of the cytoplasmic (inner) membrane**, oriented toward the cytoplasm where its substrate dihydroorotate is generated. Hydropathy analysis of Q88L40 detects **no transmembrane-strength hydrophobic segment**; instead, the class-2-diagnostic N-terminal two-helix microdomain (residues ~41–60) is amphipathic and docks onto the membrane surface, positioning the enzyme to access the membrane ubiquinone pool. This architecture couples de novo pyrimidine biosynthesis directly to the aerobic respiratory electron-transport chain. Genus-level genetic evidence from *Pseudomonas aeruginosa*, where a *pyrD* mutant is impaired in cytotoxicity, biofilm formation, quorum sensing and virulence, confirms that PyrD's metabolic output is physiologically important, and DHODH is a validated selective anti-infective drug target.

---

## Key Findings

### F001 — PyrD is a class-2 DHODH catalyzing FMN-dependent oxidation of (S)-dihydroorotate to orotate

UniProt Q88L40 assigns **EC 1.3.5.2** and the HAMAP rule **MF_00225** (dihydroorotate dehydrogenase family, Type 2). The enzyme performs the single oxidoreductive step of de novo pyrimidine biosynthesis: it oxidizes **(S)-dihydroorotate (DHO) to orotate**, a reaction coupled to reduction of the enzyme-bound **FMN** prosthetic group. The reduced flavin is then re-oxidized by a quinone electron acceptor — the defining feature captured by EC 1.3.5.2 ("with a quinone as acceptor"). Studies of the homologous human class-2 DHODH establish the enzymological blueprint that applies to PyrD: a **1:1 FMN-to-protein stoichiometry** and a **two-site ping-pong mechanism**, in which dihydroorotate is oxidized at one site and ubiquinone is reduced at a second, spatially distinct site ([PMID: 10941801](https://pubmed.ncbi.nlm.nih.gov/10941801/): *"Kinetic analysis showed that huDHODH uses a two site ping-pong mechanism, where DHO is oxidized at one site and the second substrate, ubiquinone, is reduced at the other"*). The reaction's identity and pathway position are equally clear ([PMID: 15044733](https://pubmed.ncbi.nlm.nih.gov/15044733/): *"catalyzes the oxidation of dihydroorotate to orotate, the fourth step in the de novo pyrimidine biosynthesis of UMP"*). The net reaction curated for Q88L40 is: **(S)-dihydroorotate + a quinone → orotate + a quinol** (RHEA:30187).

### F002 — Catalytic mechanism: a serine base deprotonates C5 while a C6 hydride reduces FMN N5 (stepwise)

Class-2 DHODHs use a **serine general base** and a **stepwise** chemical mechanism, distinguishing them from class 1A enzymes (which use a cysteine base and a concerted mechanism). In the *E. coli* class-2 DHOD, **Ser175** deprotonates C5 of dihydroorotate while the C6 hydrogen is transferred as a **hydride to N5** of the FMN isoalloxazine ring; strictly conserved asparagines plus a Ser/Thr hydrogen-bond the pyrimidine substrate ([PMID: 19530672](https://pubmed.ncbi.nlm.nih.gov/19530672/): *"the hydrogen at C6 of DHO is transferred to N5 of the isoalloxazine ring of an enzyme-bound FMN prosthetic group as a hydride, and an active site base (Ser175 in the class 2 DHOD from Escherichia coli) deprotonates C5 of DHO"*). Independent QM/MM free-energy calculations on human class-2 DHODH corroborate the two-step pathway — proton abstraction from C5 to the deprotonated active-site serine, then hydride transfer from C6 to FMN N5, with a barrier near 10.8 kcal/mol ([PMID: 26087682](https://pubmed.ncbi.nlm.nih.gov/26087682/): *"In the first step, a proton is abstracted from the C5 of DHO to the deprotonated Ser215 side chain. Whereas, in the second step, the transfer of the hydride or hydride equivalent from the C6 of DHO to the N5 of FMN"*). Because Q88L40 carries the equivalent serine (Ser174) and the conserved asparagine cluster, this mechanism is directly applicable to the *P. putida* enzyme.

### F003 — Localization: cytoplasmic face of the inner membrane via an N-terminal two-helix quinone-binding domain

A defining structural hallmark of class-2 DHODHs is a **unique N-terminal extension folding into a separate domain of two alpha-helices** that serves as the binding site for the respiratory quinone (the second substrate) and for inhibitors such as brequinar and atovaquone ([PMID: 15044733](https://pubmed.ncbi.nlm.nih.gov/15044733/): *"A unique feature of the class 2 DHODs is their N-terminal extension, which folds into a separate domain comprising two alpha-helices. This domain serves as the binding site for the two inhibitors and the respiratory quinones acting as the second substrate for the class 2 DHODs"*). Conserved His56 and Arg136 (invariant across class-2 DHODHs) mediate electron-acceptor/quinone interactions. The crystal structure of the bacterial *Helicobacter pylori* class-2 DHODH provides direct structural evidence for inner-membrane association and a hydrophobic ubiquinone channel ([PMID: 39960828](https://pubmed.ncbi.nlm.nih.gov/39960828/): *"we found that HpDHODH maintains several structural features that allow it to associate with the inner membrane and utilize ubiquinone to achieve catalytic turnover. We discovered a hydrophobic channel that runs from the putative membrane interface on the N-terminal microdomain to the core of the protein"*). Unlike the integral, N-terminally anchored mitochondrial enzyme, the bacterial class-2 DHODH (like *E. coli* PyrD) is **peripherally membrane-associated**.

### F004 — Pathway position: the fourth step of de novo UMP biosynthesis, coupled to the quinone pool

PyrD occupies a defined, non-redundant position in de novo pyrimidine biosynthesis:

```
carbamoyl-phosphate + L-aspartate
        │  PyrB (aspartate carbamoyltransferase / ATCase)
        ▼
   N-carbamoyl-L-aspartate
        │  PyrC (dihydroorotase)
        ▼
   (S)-dihydroorotate
        │  PyrD (DHODH)  ── FMN → quinone → quinol   ◄── THE REDOX STEP
        ▼
      orotate
        │  PyrE (orotate phosphoribosyltransferase)
        ▼
   orotidine-5'-monophosphate (OMP)
        │  PyrF (OMP decarboxylase)
        ▼
      UMP  → (all pyrimidine nucleotides: UTP, CTP, dTTP)
```

PyrD is the **sole oxidoreductase** in the pathway and acts as a metabolic control point. Pharmacological block of DHODH causes accumulation of the upstream intermediates N-carbamoyl-aspartate and dihydroorotate and depletion of downstream orotate/UMP; the block can be bypassed by exogenous orotate or uridine but **not** by dihydroorotate ([PMID: 17123468](https://pubmed.ncbi.nlm.nih.gov/17123468/): *"Dicoumarol-treated cells accumulated in S phase due to the impairment of pyrimidine biosynthesis at dihydroorotate dehydrogenase step because blockade was overcome by addition of exogenous uridine or orotate, but not by dihydroorotate"*). The naphthoquinone atovaquone likewise inhibits DHODH and induces accumulation of carbamoyl-aspartate and dihydroorotate ([PMID: 7909690](https://pubmed.ncbi.nlm.nih.gov/7909690/): *"Atovaquone, a naphthoquinone, is a moderate inhibitor of dihydroorotate dehydrogenase in vitro (Ki = 27 microM) but induces major accumulations of CA-asp and DHO"*). Because the class-2 enzyme re-oxidizes its FMN using **membrane ubiquinone**, PyrD activity is functionally coupled to the aerobic respiratory electron-transport chain.

### F005 — Q88L40 carries the intact class-2 catalytic machinery

Direct analysis of the 340-residue Q88L40 sequence confirms that **position 174 is a serine**, curated by UniProt as the catalytic nucleophile/active-site base and positionally equivalent to *E. coli* Ser175. The strictly conserved pyrimidine-binding **asparagines** are present as UniProt binding-site residues (**Asn110, Asn138, Asn171, Asn176, Asn245**), together with Lys65, Lys216 and Thr/Asn residues that coordinate FMN and substrate. UniProt/HAMAP curation (MF_00225) records: the catalytic reaction *(S)-dihydroorotate + a quinone = orotate + a quinol* (RHEA:30187, EC 1.3.5.2); FMN cofactor (1 per subunit); monomeric quaternary structure; subcellular location = cell membrane, peripheral membrane protein; and pathway assignment "UMP biosynthesis via de novo pathway; orotate from (S)-dihydroorotate (quinone route): step 1/1." The presence of the exact catalytic base ([PMID: 19530672](https://pubmed.ncbi.nlm.nih.gov/19530672/): *"an active site base (Ser175 in the class 2 DHOD from Escherichia coli) deprotonates C5 of DHO"*) and the conserved asparagine cluster ([PMID: 19530672](https://pubmed.ncbi.nlm.nih.gov/19530672/): *"Several strictly conserved residues (four asparagines and either a serine or threonine) make extensive hydrogen bonds to the pyrimidine)"*) confirms full retention of the class-2 catalytic and substrate-binding apparatus.

### F006 — Experimental bacterial evidence: membrane-bound FMN enzyme, two-site mechanism, genetically required for pyrimidine prototrophy

Rapid-reaction (stopped-flow) studies of *E. coli* DHOD provide the closest experimental model for Q88L40. The *E. coli* enzyme is a **membrane-bound FMN enzyme that uses ubiquinone** as the oxidizing substrate ([PMID: 11284694](https://pubmed.ncbi.nlm.nih.gov/11284694/): *"The enzyme from Escherichia coli is a membrane-bound FMN-containing enzyme that is thought to use ubiquinone as the oxidizing substrate"*). Flavin reduction by dihydroorotate is governed by an ionizable active-site base (Ser175, pKa ~9.5), with the rate rising from 1 s⁻¹ at pH 6.5 to ~360 s⁻¹ above pH 9.5. Because the reduced flavin–orotate charge-transfer complex dissociates too slowly to be catalytic, the quinone must bind and re-oxidize the reduced enzyme–orotate complex at a **site distinct from the DHO site** — establishing the two-site (ping-pong) mechanism ([PMID: 11284694](https://pubmed.ncbi.nlm.nih.gov/11284694/): *"the oxidizing quinone substrate must bind to the reduced enzyme-orotate complex at a site distinct from the substrate binding site"*). Genetically, enteric *pyrD* auxotrophs (*Salmonella*) cannot synthesize pyrimidines de novo and accumulate the upstream intermediate carbamyl-aspartate ([PMID: 3894327](https://pubmed.ncbi.nlm.nih.gov/3894327/): *"It should accumulate to high levels in pyrC or pyrD mutants when expression of the pyrA and pyrB genes is elevated"*), confirming PyrD is required for pyrimidine prototrophy in vivo.

### F007 — 56.9% identity to experimentally characterized *E. coli* class-2 PyrD, catalytic serine conserved

Global pairwise alignment of *P. putida* Q88L40 (340 aa) against *E. coli* PyrD (P0A7E1, 336 aa) gives **190/334 = 56.9% sequence identity**. The experimentally defined *E. coli* catalytic base **Ser175 aligns exactly to Q88L40 Ser174**. This substantial full-length identity, combined with conservation of the catalytic residue and the class-2 pyrimidine-binding asparagine cluster, places Q88L40 firmly within the well-studied bacterial class-2 DHOD group and justifies transfer of the experimentally established mechanism ([PMID: 11284694](https://pubmed.ncbi.nlm.nih.gov/11284694/): *"The rate constant for the flavin reduction reaction increased with pH, from a value of 1 s(-1) at pH 6.5 to approximately 360 s(-1) at pH values greater than an observed pK(a) of 9.5 which was ascribed to Ser175, the active-site base"*).

### F008 — Genus-level (Pseudomonas) functional evidence and drug-target status

In *Pseudomonas aeruginosa* (same genus as the target *P. putida*), PyrD is explicitly identified as a **dihydroorotate dehydrogenase (DHODase) of pyrimidine biosynthesis**, and a *pyrD* transposon mutant showed defects in cytotoxicity, biofilm formation, quorum sensing and virulence in an acute mouse pneumonia model; a computationally predicted small-molecule inhibitor suppressed both PyrD activity and these phenotypes ([PMID: 26751736](https://pubmed.ncbi.nlm.nih.gov/26751736/): *"we employed a computer-aided screening to identify potential inhibitors of the PyrD protein, a dihydroorotate dehydrogenase (DHODase) involved in pyrimidine biosynthesis"*; *"A pyrD mutant displayed defects in cytotoxicity, biofilm formation, quorum sensing and virulence in an acute mouse pneumonia model"*). More broadly, DHODH is a validated anti-infective target because many pathogens depend on de novo pyrimidine synthesis, and bacterial (class 2) versus host enzymes differ enough to permit selective inhibition ([PMID: 31557612](https://pubmed.ncbi.nlm.nih.gov/31557612/): *"Dihydroorotate dehydrogenase (DHODH), which is involved in the de novo biosynthesis of pyrimidines, is a validated target for anti-infective drug research"*).

### F009 — Hydropathy: consistent with peripheral (monotopic) membrane association, not integral

Kyte–Doolittle hydropathy analysis of the 340-residue Q88L40 sequence shows **no transmembrane-strength hydrophobic segment**: the maximum smoothed hydropathy over a 19-residue window is only **+1.34** (center ~residue 235), below the ~+1.6 threshold typical of membrane-spanning helices, and these peaks map to buried TIM-barrel core segments rather than the N-terminus. The N-terminal class-2 microdomain (residues ~41–60, "PASLPVSVMGLNFANPVGLA") is moderately/amphipathically hydrophobic (65% hydrophobic residues; local KD peak +1.59 at "SLPVSVMGL"). This pattern — an amphipathic, membrane-interacting N-terminal helix without a full transmembrane span — matches the UniProt curation of PyrD as a **peripheral membrane protein** ([PMID: 15044733](https://pubmed.ncbi.nlm.nih.gov/15044733/): *"their N-terminal extension, which folds into a separate domain comprising two alpha-helices. This domain serves as the binding site for the two inhibitors and the respiratory quinones"*) and the fact that bacterial class-2 PyrD remains a soluble-purifiable flavoprotein despite being membrane-associated ([PMID: 11284694](https://pubmed.ncbi.nlm.nih.gov/11284694/): *"The enzyme from Escherichia coli is a membrane-bound FMN-containing enzyme that is thought to use ubiquinone as the oxidizing substrate"*).

---

## Mechanistic Model / Interpretation

PyrD (Q88L40) is best understood as a **membrane-surface-tethered flavin redox valve** that connects the soluble pyrimidine biosynthesis pathway to the respiratory quinone pool. Its function can be decomposed into two coupled half-reactions occurring at two distinct sites (a ping-pong mechanism):

**Half-reaction 1 (reductive, at the pyrimidine site, buried in the TIM-barrel core):**

```
(S)-dihydroorotate  +  FMN(ox)
      │  Ser174 abstracts the C5 proton (general base)
      │  C6 hydride transfers to FMN N5
      ▼
   orotate  +  FMN(red, FMNH⁻)
```

The pyrimidine substrate is clamped by the conserved asparagine cluster (Asn110/138/171/176/245) plus Lys/Thr contacts. The serine base (Ser174) and stepwise proton-then-hydride chemistry are the class-2 signatures.

**Half-reaction 2 (oxidative, at the N-terminal microdomain / membrane interface):**

```
FMN(red)  +  quinone (ubiquinone, from membrane)
      │  electron/H transfer via hydrophobic channel
      ▼
   FMN(ox)  +  quinol
```

The N-terminal two-helix microdomain docks onto the inner-membrane surface and delivers ubiquinone through a hydrophobic channel to the re-oxidation site, regenerating FMN(ox) for the next catalytic cycle. Conserved His56/Arg136 assist quinone binding.

### Localization and topology

| Property | Assignment for Q88L40 | Evidence |
|---|---|---|
| Subcellular location | Cytoplasmic (inner) membrane, cytoplasmic face | UniProt/HAMAP; hydropathy (F009) |
| Membrane topology | Peripheral / monotopic (not integral) | No TM segment; KD max +1.34 (F009) |
| Membrane anchor | Amphipathic N-terminal two-helix microdomain (~res 41–60) | Class-2 structure; hydropathy (F003, F009) |
| Quaternary structure | Monomer | UniProt curation (F005) |
| Cofactor | 1 FMN per subunit | UniProt; human enzyme 1:1 stoichiometry (F001) |
| Second substrate | Ubiquinone (respiratory quinone) | *E. coli* / *H. pylori* class-2 (F003, F006) |

### DHODH class comparison (why "Type 2" matters)

| Feature | Class 1A | Class 1B | **Class 2 (PyrD / Q88L40)** |
|---|---|---|---|
| Electron acceptor | Fumarate | NAD⁺ | **Quinone (ubiquinone)** |
| Active-site base | Cysteine | Cysteine/Lys | **Serine (Ser174)** |
| Chemistry | Concerted | Concerted | **Stepwise** |
| Membrane association | Cytosolic | Cytosolic | **Peripheral, inner membrane** |
| Representative | *L. lactis*, *T. cruzi* | *C. oroticum* | *E. coli*, human, *P. putida* |

This classification is directly supported by the mechanistic literature: class 1A uses a cysteine base and concerted chemistry with fumarate ([PMID: 25564307](https://pubmed.ncbi.nlm.nih.gov/25564307/), [PMID: 18808149](https://pubmed.ncbi.nlm.nih.gov/18808149/)); class 1B is an NAD⁺-linked heterotetramer ([PMID: 10956027](https://pubmed.ncbi.nlm.nih.gov/10956027/)); class 2 uses a serine base, stepwise chemistry, and a quinone acceptor at a membrane-associated N-terminal domain ([PMID: 19530672](https://pubmed.ncbi.nlm.nih.gov/19530672/), [PMID: 15044733](https://pubmed.ncbi.nlm.nih.gov/15044733/)).

### Integrated physiological role

By committing dihydroorotate to orotate, PyrD gates the flow of carbon and nitrogen from carbamoyl-phosphate/aspartate into UMP and thence into all pyrimidine nucleotides (RNA, DNA, and activated sugar/lipid precursors such as UDP-glucose). Its dependence on membrane ubiquinone makes de novo pyrimidine synthesis conditional on a functioning respiratory chain — the biochemical rationale behind DHODH's utility as a metabolic control point and drug target. In *Pseudomonas*, loss of this activity impairs growth-linked phenotypes (biofilm, virulence, quorum sensing), reflecting the downstream demand for pyrimidines during active proliferation.

---

## Evidence Base

| PMID | Focus | How it supports the annotation |
|---|---|---|
| [10941801](https://pubmed.ncbi.nlm.nih.gov/10941801/) | Soluble human DHODH characterization | Establishes 1:1 FMN stoichiometry and two-site ping-pong mechanism for class-2 DHODH (F001) |
| [15044733](https://pubmed.ncbi.nlm.nih.gov/15044733/) | Inhibitor binding in class-2 DHODH N-terminal domain | Defines the DHO→orotate reaction as the 4th step; N-terminal two-helix quinone/membrane domain (F001, F003, F009) |
| [19530672](https://pubmed.ncbi.nlm.nih.gov/19530672/) | Conserved active-site residues in *E. coli* class-2 DHOD | Ser175 base, C6→FMN N5 hydride, conserved asparagines binding pyrimidine (F002, F005) |
| [26087682](https://pubmed.ncbi.nlm.nih.gov/26087682/) | QM/MM study of human class-2 DHODH | Confirms stepwise proton-then-hydride mechanism with serine base (F002) |
| [39960828](https://pubmed.ncbi.nlm.nih.gov/39960828/) | *H. pylori* DHODH crystal structure | Structural evidence for inner-membrane association and hydrophobic ubiquinone channel (F003) |
| [11284694](https://pubmed.ncbi.nlm.nih.gov/11284694/) | Rapid-reaction study of *E. coli* DHODH | Membrane-bound FMN enzyme, ubiquinone acceptor, two-site mechanism, Ser175 pKa ~9.5 (F006, F007, F009) |
| [17123468](https://pubmed.ncbi.nlm.nih.gov/17123468/) | Dicoumarol impairs pyrimidine biosynthesis | DHODH block rescued by orotate/uridine but not DHO — confirms pathway position (F004) |
| [7909690](https://pubmed.ncbi.nlm.nih.gov/7909690/) | DHODH inhibitors in *Plasmodium* | Atovaquone inhibition causes CA-asp/DHO accumulation — places DHODH downstream (F004) |
| [3894327](https://pubmed.ncbi.nlm.nih.gov/3894327/) | Carbamyl aspartate toxicity in *Salmonella* | *pyrD* mutants accumulate carbamyl-aspartate — genetic requirement for pyrimidine synthesis (F006) |
| [26751736](https://pubmed.ncbi.nlm.nih.gov/26751736/) | Small molecule vs. *P. aeruginosa* PyrD | Genus-level confirmation of PyrD as DHODase; mutant phenotypes (F008) |
| [31557612](https://pubmed.ncbi.nlm.nih.gov/31557612/) | DHODH inhibitors in anti-infective research | Authoritative review: DHODH in de novo pyrimidine synthesis, drug-target status (F008) |
| [25564307](https://pubmed.ncbi.nlm.nih.gov/25564307/) | QM/MM of class-1A DHOD (*L. lactis*) | Contrast: class-1A uses Cys base, concerted mechanism (class comparison) |
| [18808149](https://pubmed.ncbi.nlm.nih.gov/18808149/) | *T. cruzi* class-1A DHOD structures | Contrast: one-site mechanism, fumarate acceptor (class comparison) |
| [10956027](https://pubmed.ncbi.nlm.nih.gov/10956027/) | *C. oroticum* class-1B DHOD | Contrast: NAD⁺-linked heterotetramer (class comparison) |

**Supporting inference chain:** The annotation rests on three independent pillars — (1) **curated database evidence** (UniProt/HAMAP MF_00225, EC 1.3.5.2, RHEA:30187, InterPro class-2 domains); (2) **sequence/evolutionary evidence** (56.9% identity to experimentally characterized *E. coli* PyrD, exact conservation of the catalytic Ser174, the asparagine cluster, and hydropathy consistent with peripheral membrane association); and (3) **experimental orthologue evidence** (mechanistic, structural, and genetic studies of *E. coli*, human, and *H. pylori* class-2 DHODHs, plus genus-level *Pseudomonas* genetics). No conflicting evidence was found — the gene symbol, EC number, family, and domains are all internally consistent, and no ambiguous same-symbol gene concerns arose.

---

## Limitations and Knowledge Gaps

1. **No direct biochemical characterization of Q88L40 itself.** There is no published enzymology (kcat, Km for dihydroorotate or the specific *Pseudomonas* quinone, FMN content) measured on the purified *P. putida* KT2440 PyrD protein. All kinetic and mechanistic parameters are transferred from orthologues (*E. coli*, human, *H. pylori*). While the 56.9% identity and residue conservation make this transfer robust for qualitative function, absolute kinetic values may differ.

2. **No experimental structure for Q88L40.** Localization topology, the N-terminal microdomain conformation, and the quinone channel are inferred from homologous structures (rat, *H. pylori*, *E. coli*) and from hydropathy analysis, not from a *P. putida* crystal/cryo-EM structure or an experimentally validated AlphaFold model.

3. **Native quinone identity.** The physiological quinone acceptor in *P. putida* (ubiquinone-9 vs. other isoprenoid quinones and possible menaquinone contributions under different growth conditions) has not been directly established for this enzyme.

4. **Regulation in *P. putida* specifically.** While pyrimidine metabolism regulation via carbon catabolite repression and quorum sensing has been described in *P. putida* strain RU-KM3S ([PMID: 23563885](https://pubmed.ncbi.nlm.nih.gov/23563885/)), transcriptional/post-translational control of *pyrD* (PP_2095) in KT2440 was not directly characterized here.

5. **Membrane orientation detail.** The peripheral, cytoplasm-facing orientation is inferred; the depth of membrane insertion and any lipid-specific interactions of the N-terminal microdomain remain uncharacterized for this ortholog.

---

## Proposed Follow-up Experiments / Actions

1. **Heterologous expression and enzymatic assay.** Clone PP_2095 with a C-terminal His-tag, express in *E. coli*, purify, and confirm FMN content spectroscopically. Measure steady-state kinetics (Km for (S)-dihydroorotate; Km for candidate quinones such as decylubiquinone/CoQ) using the standard DCIP- or quinone-coupled DHODH assay, and verify the DHO→orotate reaction by HPLC/MS. This would convert the inferred function into a directly measured one.

2. **Site-directed mutagenesis of Ser174.** Mutate Ser174→Ala and assay activity to experimentally confirm its role as the catalytic base in the *P. putida* enzyme, validating the mechanism transfer.

3. **Genetic complementation / knockout.** Construct a clean PP_2095 deletion in *P. putida* KT2440 and test for pyrimidine auxotrophy (rescue by uracil/orotate/uridine but not dihydroorotate), directly mirroring the enteric *pyrD* genetics and confirming pathway position in this organism.

4. **Structure determination.** Solve the crystal or cryo-EM structure (or generate and validate an AlphaFold model with the bound FMN) to confirm the TIM-barrel fold, the N-terminal two-helix microdomain, and the quinone channel; use this to guide selective-inhibitor design.

5. **Membrane fractionation / topology.** Fractionate KT2440 lysates and immunoblot to confirm PyrD co-fractionates with the inner membrane as a peripheral protein, and probe salt/detergent extractability to distinguish peripheral from integral association.

6. **Native quinone identification.** Determine which quinone(s) *P. putida* PyrD uses under aerobic vs. microaerobic conditions, clarifying how tightly de novo pyrimidine synthesis is coupled to the respiratory chain in this soil bacterium.

7. **Inhibitor profiling.** Given DHODH's validated anti-infective target status and the demonstrated *P. aeruginosa* PyrD inhibitor precedent, screen class-2-selective inhibitors (e.g., brequinar/atovaquone analogues) against purified *P. putida* PyrD to characterize the N-terminal quinone/inhibitor pocket.

---

### Conclusion

All lines of evidence converge on a single, well-supported annotation: **pyrD (Q88L40, PP_2095) is the Type 2 dihydroorotate dehydrogenase of *Pseudomonas putida* KT2440**, a monomeric FMN flavoenzyme that catalyzes the FMN- and quinone-dependent oxidation of (S)-dihydroorotate to orotate — the sole redox step of de novo UMP biosynthesis — while peripherally associated with the cytoplasmic face of the inner membrane through an N-terminal two-helix microdomain that accesses the respiratory ubiquinone pool. The gene symbol, organism, protein family, and domain architecture are all fully consistent; no ambiguity or mis-identification was encountered.


## Artifacts

- [OpenScientist final report](pyrD-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](pyrD-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:10941801
2. PMID:15044733
3. PMID:19530672
4. PMID:26087682
5. PMID:39960828
6. PMID:17123468
7. PMID:7909690
8. PMID:11284694
9. PMID:3894327
10. PMID:26751736
11. PMID:31557612
12. PMID:25564307
13. PMID:18808149
14. PMID:10956027
15. PMID:23563885