---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-11T18:53:40.522889'
end_time: '2026-07-11T19:17:01.236775'
duration_seconds: 1400.71
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: sdhA
  gene_symbol: sdhA
  uniprot_accession: Q88FA7
  protein_description: 'RecName: Full=Succinate dehydrogenase flavoprotein subunit
    {ECO:0000256|ARBA:ARBA00019965, ECO:0000256|NCBIfam:TIGR01816}; EC=1.3.5.1 {ECO:0000256|ARBA:ARBA00012792,
    ECO:0000256|RuleBase:RU362051};'
  gene_info: Name=sdhA {ECO:0000313|EMBL:AAN69772.1}; OrderedLocusNames=PP_4191 {ECO:0000313|EMBL:AAN69772.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the FAD-dependent oxidoreductase 2 family.
  protein_domains: FAD-dep_OxRdtase_2_FAD-bd. (IPR003953); FAD/NAD-bd_sf. (IPR036188);
    FRD_SDH_FAD_BS. (IPR003952); Fum_R/Succ_DH_flav-like_C_sf. (IPR037099); Fum_Rdtase/Succ_DH_flav-like_C.
    (IPR015939)
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
  path: sdhA-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: sdhA-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88FA7
- **Protein Description:** RecName: Full=Succinate dehydrogenase flavoprotein subunit {ECO:0000256|ARBA:ARBA00019965, ECO:0000256|NCBIfam:TIGR01816}; EC=1.3.5.1 {ECO:0000256|ARBA:ARBA00012792, ECO:0000256|RuleBase:RU362051};
- **Gene Information:** Name=sdhA {ECO:0000313|EMBL:AAN69772.1}; OrderedLocusNames=PP_4191 {ECO:0000313|EMBL:AAN69772.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the FAD-dependent oxidoreductase 2 family.
- **Key Domains:** FAD-dep_OxRdtase_2_FAD-bd. (IPR003953); FAD/NAD-bd_sf. (IPR036188); FRD_SDH_FAD_BS. (IPR003952); Fum_R/Succ_DH_flav-like_C_sf. (IPR037099); Fum_Rdtase/Succ_DH_flav-like_C. (IPR015939)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "sdhA" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'sdhA' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **sdhA** (gene ID: sdhA, UniProt: Q88FA7) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *sdhA* (Q88FA7 / PP_4191) in *Pseudomonas putida* KT2440

## Summary

**sdhA** (UniProt **Q88FA7**, ordered locus **PP_4191**) encodes the **catalytic flavoprotein subunit of succinate dehydrogenase**, respiratory **Complex II** (succinate:quinone oxidoreductase, **EC 1.3.5.1**), in *Pseudomonas putida* strain KT2440 (PSEPK). The gene symbol, protein description, organism, protein family (FAD-dependent oxidoreductase 2 family), and characteristic domains (FAD-binding and C-terminal fumarate-reductase/succinate-dehydrogenase flavoprotein-like domains) are all mutually consistent, and every piece of literature recovered maps cleanly onto this identity. **The gene identity is confirmed — there is no ambiguity or gene-symbol confusion.** *P. putida* SdhA is a *bona fide* orthologue of the biochemically and structurally characterized *Escherichia coli* SdhA, to which it is 70% identical with complete conservation of every catalytic residue.

The primary function of SdhA is to **oxidize the C4-dicarboxylate succinate to fumarate** at a single, dicarboxylate-specific active site, transferring the two abstracted electrons (as a hydride) onto a **covalently bound FAD cofactor** attached at **His46** (an 8α-*N*-histidyl-FAD linkage). From the reduced flavin, electrons pass one at a time to the iron–sulfur clusters of the partner subunit SdhB and ultimately reduce the membrane quinone pool. In this way SdhA sits precisely at the junction of two central pathways: the **tricarboxylic acid (TCA / Krebs) cycle** — where it catalyzes the succinate → fumarate step — and the **aerobic respiratory electron-transport chain**, where Complex II feeds electrons into quinone. The physiological substrates are succinate and fumarate; malonate and oxaloacetate are its classic competitive inhibitors.

SdhA is a **cytoplasm-facing, peripheral protein of the cell inner membrane**, held there as part of the membrane-anchored **SdhA/SdhB/SdhC/SdhD heterotetramer**. The four subunits are co-encoded in the canonical **sdhCDAB operon** (gene order PP_4193–PP_4192–PP_4191–PP_4190) embedded within a larger TCA gene cluster flanked by citrate synthase (*gltA*) and 2-oxoglutarate dehydrogenase (*sucA*), mirroring the classic enterobacterial arrangement. The covalent flavinylation of SdhA — absolutely required for succinate oxidation — is installed by the dedicated assembly factor **SdhE** through its conserved RGxxE motif, with a small residual autocatalytic (SdhE-independent) capacity of ~5%.

---

## Key Findings

### Finding 1 — SdhA is the catalytic flavoprotein subunit of respiratory Complex II (EC 1.3.5.1)

SdhA (Q88FA7 / PP_4191) is annotated in UniProt with **EC 1.3.5.1** and the catalytic activity *"a quinone + succinate = fumarate + a quinol"* (Rhea RHEA:40523). It belongs to the **FAD-dependent oxidoreductase 2 family, FRD/SDH subfamily**, is 590 amino acids long, and carries an N-terminal FAD-binding domain (residues ~10–407) and a C-terminal flavoprotein capping domain (residues ~463–590). The UniProt pathway annotation places it in the *"tricarboxylic acid cycle; fumarate from succinate (bacterial route): step 1/1"* — i.e., it performs the single enzymatic step converting succinate to fumarate in the TCA cycle.

Complex II is a **heterotetramer** consisting of a catalytic flavoprotein (SdhA), an iron–sulfur subunit (SdhB), and two hydrophobic membrane anchors (SdhC and SdhD). As McNeil & Fineran ([PMID: 22985599](https://pubmed.ncbi.nlm.nih.gov/22985599/)) state: *"Complex II consists of four subunits including a catalytic flavoprotein (SdhA), an iron-sulphur subunit (SdhB) and two hydrophobic membrane anchors (SdhC and SdhD),"* which *"mediate electron transfer from succinate oxidation to the reduction of the mobile electron carrier ubiquinone."* This directly establishes SdhA as the specific subunit that binds and oxidizes succinate. More broadly, Complex II *"is traditionally studied for its participation in two key respiratory processes: the electron transport chain and the Krebs cycle"* ([PMID: 37119852](https://pubmed.ncbi.nlm.nih.gov/37119852/)), confirming SdhA's dual metabolic role. Because *P. putida* KT2440 is an obligate aerobe, the enzyme operates in the oxidative (succinate → fumarate) direction as the aerobic succinate:ubiquinone oxidoreductase, rather than as an anaerobic fumarate reductase.

### Finding 2 — SdhA carries a covalently bound 8α-histidyl-FAD at His46, essential for catalysis and installed by SdhE

Unusually among flavoproteins, SdhA binds its FAD cofactor **covalently**. The UniProt record for Q88FA7 lists a modified residue at position 46, *"Tele-8alpha-FAD histidine"*, and the sequence around this residue (…RS**H46**TV…) is consistent with the documented covalent-attachment motif. An N-terminal Rossmann-type dinucleotide-binding motif (GxGxxG; observed as GGGGAG, residues 15–20) provides the non-covalent scaffold that cradles the adenine-nucleotide moiety of FAD.

This covalent linkage is not a curiosity but a mechanistic necessity: *"A covalently bound FAD cofactor is present in the flavoprotein subunit, and the covalent flavin linkage is absolutely required to enable the enzyme to oxidize succinate"* ([PMID: 36089066](https://pubmed.ncbi.nlm.nih.gov/36089066/)). Only a small minority of flavoproteins attach FAD covalently — *"FAD is predominantly bound non-covalently to flavoproteins, with only a small percentage of flavoproteins, such as complex II, binding FAD covalently"* ([PMID: 22985599](https://pubmed.ncbi.nlm.nih.gov/22985599/)). The covalent bond raises the redox potential of the flavin sufficiently to make succinate oxidation thermodynamically favourable.

The flavinylation reaction is promoted by a dedicated assembly factor. *"Both prokaryotic SdhE and mammalian SDHAF2 enhance FAD binding to their respective apoprotein of complex II"* ([PMID: 36089066](https://pubmed.ncbi.nlm.nih.gov/36089066/)). Structural work on the human orthologue further shows that *"a small molecule dicarboxylate … acts as an essential cofactor in this process and works in synergy with SDHAF2 to properly orient the flavin and capping domains of SDHA"* ([PMID: 32887801](https://pubmed.ncbi.nlm.nih.gov/32887801/)) — i.e., the assembly factor and a dicarboxylate together correctly configure the active-site region for covalent flavin attachment. Mechanistically, succinate is oxidized by hydride transfer from its C–H bond to the covalent FAD, coupled to proton abstraction by an active-site base; the two-electron-reduced flavin is then re-oxidized one electron at a time by the downstream Fe–S chain.

### Finding 3 — SdhA is a peripheral inner-membrane flavoprotein exposed to the cytoplasm and relays electrons to quinone

UniProt assigns Q88FA7 the subcellular location *"Cell inner membrane; Peripheral membrane protein; Cytoplasmic side."* SdhA is thus not an integral membrane protein itself but is tethered to the cytoplasmic face of the inner membrane through its association (with SdhB) onto the membrane-integral SdhC/SdhD anchor. Its **proton-accepting active site is at residue 289**, with additional FAD/substrate-binding residues distributed around the flavin/dicarboxylate pocket (residues ~15–20, 38–53, 224, 245, 257, 356, 390, 401, 406–407). Gene Ontology terms reinforce the functional picture: succinate dehydrogenase (quinone) activity (GO:0008177), FAD binding (GO:0050660), electron transfer activity (GO:0009055), TCA cycle (GO:0006099), and electron transport chain (GO:0022900).

Mechanistically, electrons flow from the SdhA flavin to a chain of iron–sulfur clusters in SdhB ([2Fe-2S] → [4Fe-4S] → [3Fe-4S]) and finally to quinone at the membrane anchors. Studies of the closely related fumarate reductase show that conserved SdhB/FrdB residues near the [3Fe-4S] cluster tune this transfer: *"The close proximity of these residues to the [3Fe-4S] cluster and the quinone binding pocket provided an excellent opportunity to investigate factors controlling the reduction potential of the [3Fe-4S] cluster, the directionality of electron transfer and catalysis"* ([PMID: 23711795](https://pubmed.ncbi.nlm.nih.gov/23711795/)). Furthermore, there is long-range functional coupling across the enzyme: a *"long distance interaction between the succinate (fumarate) binding and ubiquinone (ubiquinol) reactive sites"* ([PMID: 27810396](https://pubmed.ncbi.nlm.nih.gov/27810396/)). As a side reaction, the flavoprotein redox centres can leak electrons to O₂ and generate reactive oxygen species — *"Bovine heart mitochondrial respiratory complex II generates ROS, mostly as superoxide"* ([PMID: 27810396](https://pubmed.ncbi.nlm.nih.gov/27810396/)).

### Finding 4 — *sdhA* lies in the canonical sdhCDAB operon within a TCA gene cluster

The genomic neighbourhood of PP_4191 in *P. putida* KT2440 recapitulates the classic bacterial succinate-dehydrogenase operon. KEGG annotations give:

| Locus | Gene | Product | KEGG orthology |
|-------|------|---------|----------------|
| PP_4193 | *sdhC* | succinate dehydrogenase cytochrome b-556 | K00241 |
| PP_4192 | *sdhD* | membrane anchor subunit | K00242 |
| **PP_4191** | ***sdhA*** | **flavoprotein subunit (EC 1.3.5.1)** | **K00239** |
| PP_4190 | *sdhB* | iron–sulfur subunit | K00240 |

i.e., the operon order **sdhC-sdhD-sdhA-sdhB (sdhCDAB)**. Immediately flanking the operon are **PP_4194 = citrate synthase (*gltA*, K01647)** and **PP_4189 = 2-oxoglutarate dehydrogenase E1 (*sucA*, K00164)**, so the whole locus forms a *gltA–sdhCDAB–sucAB* TCA-cycle gene cluster that mirrors the classic *E. coli* arrangement. The co-encoding of all four subunits is exactly what is required to assemble the SdhA(flavoprotein)/SdhB(Fe-S)/SdhC(cyt b-556)/SdhD(anchor) heterotetramer ([PMID: 22985599](https://pubmed.ncbi.nlm.nih.gov/22985599/)). *P. putida* KT2440 is an obligate aerobe with a fully operational, tightly regulated TCA cycle: *"The classic textbook scheme of central metabolism includes the Embden-Meyerhof-Parnas (EMP) pathway of glycolysis, the pentose phosphate pathway, and the citric acid cycle"* ([PMID: 24951791](https://pubmed.ncbi.nlm.nih.gov/24951791/)) — placing SdhA firmly within this organism's central carbon metabolism.

### Finding 5 — A single dicarboxylate-specific active site defines substrate specificity

The SdhA active site is a **single dicarboxylate-specific pocket**. Classic biochemical studies of succinate dehydrogenase established that succinate, fumarate, malonate, and oxaloacetate all compete for one site: *"succinate dehydrogenase interaction with succinate and oxaloacetate results from the competition for a single dicarboxylate-specific site"* ([PMID: 6733163](https://pubmed.ncbi.nlm.nih.gov/6733163/)), and the same body of work characterized *"the relative affinities of succinate, fumarate, malonate and oxaloacetate to the reduced and oxidized species of the enzyme"* ([PMID: 6691982](https://pubmed.ncbi.nlm.nih.gov/6691982/)). Thus the **physiological substrates are succinate (oxidized to fumarate) and fumarate**, while **malonate and oxaloacetate are competitive inhibitors**. The affinity of the site is redox-state dependent, with substantial (>10-fold) differences between oxidized and reduced enzyme — an important regulatory feature that gates catalysis. In Q88FA7, the proton-accepting active-site residue (289) together with the substrate/FAD-binding residues (224, 245, 257, 356, 390, 401, 406–407) line this dicarboxylate/flavin pocket, and the covalent 8α-histidyl-FAD at His46 provides the hydride acceptor for succinate C–H oxidation.

### Finding 6 — 70% identity to the structurally characterized *E. coli* SdhA licenses transfer of mechanistic knowledge

A global (Needleman–Wunsch) alignment of Q88FA7 (*P. putida*, 590 aa) against *E. coli* SdhA (P0AC41, 588 aa) yields **70.1% identity** (411/586 aligned columns). Crucially, **every functionally critical residue is conserved** position-for-position:

| Function | *P. putida* (Q88FA7) | *E. coli* (P0AC41) | Status |
|----------|----------------------|--------------------|--------|
| Covalent-FAD histidine | His46 | His45 | Conserved |
| FAD-binding Rossmann glycine | Gly15 | Gly14 | Conserved |
| Active-site proton acceptor | Arg289 | Arg286 | Conserved |
| Dicarboxylate/FAD binding | Asp224 | Asp221 | Conserved |
| FAD-binding | Ser406 | Ser404 | Conserved |

Because *E. coli* SdhCDAB is the crystallographically and spectroscopically characterized succinate:ubiquinone oxidoreductase, this high identity and complete active-site conservation justify transferring its detailed mechanism to *P. putida* SdhA with high confidence. The conserved His46 (= *E. coli* His45) is precisely the covalent-FAD attachment residue whose covalent linkage *"is absolutely required to enable the enzyme to oxidize succinate"* ([PMID: 36089066](https://pubmed.ncbi.nlm.nih.gov/36089066/)).

### Finding 7 — Experimental evidence that SdhE flavinylates folded SdhA via its RGxxE motif

Beyond bioinformatic inference, direct experimental work in enterobacteria demonstrates the flavinylation mechanism. In *E. coli* and *Serratia*, *"the covalent attachment of FAD to SdhA is dependent on the FAD assembly factor SdhE (YgfY)"* ([PMID: 24070374](https://pubmed.ncbi.nlm.nih.gov/24070374/)). A highly conserved **RGxxE motif** in SdhE is required, and SdhE interacts with and flavinylates **folded** SdhA without requiring assembly of the whole SDH complex. Importantly, *"SdhA was also partially active in the absence of SdhE, suggesting that SdhA is able to attach FAD through an inefficient autocatalytic mechanism"* ([PMID: 24070374](https://pubmed.ncbi.nlm.nih.gov/24070374/)) — matching the UniProt note for Q88FA7 that *"about 5% flavinylation occurs in the absence of SdhE."* The same assembly factor is bifunctional across the FRD/SDH family: SdhE *"flavinylates and activates the respiratory enzyme succinate dehydrogenase (SDH)"* and also the paralogous fumarate reductase flavoprotein FrdA ([PMID: 24374335](https://pubmed.ncbi.nlm.nih.gov/24374335/)). Since SDH/FRD and SdhE are conserved across bacteria, these findings are of widespread relevance and can be confidently applied to *P. putida* SdhA.

---

## Mechanistic Model / Interpretation

Combining all findings yields a coherent mechanistic picture of SdhA as the electron-input flavoprotein of *P. putida* Complex II.

**Reaction catalyzed (EC 1.3.5.1):**

```
   succinate  +  quinone (Q)  →  fumarate  +  quinol (QH2)
```

**Electron relay architecture (Complex II):**

```
  Cytoplasm
  ┌───────────────────────────────────────────────┐
  │  SUCCINATE                                     │
  │     │  (binds single dicarboxylate site;      │
  │     │   Arg289 = proton acceptor)             │
  │     ▼                                          │
  │  SdhA  ──[8α-His46-FAD]──► FADH2               │  ← flavoprotein (Q88FA7)
  │     │        (covalent, installed by SdhE)     │     peripheral, cytoplasmic side
  │     ▼                                          │
  │  SdhB  [2Fe-2S] → [4Fe-4S] → [3Fe-4S]          │  ← iron–sulfur subunit (PP_4190)
  └───────┼────────────────────────────────────────┘
          ▼
  ═══════ SdhC/SdhD (cyt b-556 + anchors) ═════════   ← inner membrane (PP_4193/PP_4192)
          │  quinone-binding site
          ▼
       QUINONE  →  QUINOL   → aerobic respiratory chain
```

The catalytic cycle proceeds as follows: succinate binds in the single dicarboxylate-specific pocket on the cytoplasmic face; the active-site base (Arg289 region) deprotonates while a **hydride is transferred from succinate's C–H bond to the covalently bound 8α-histidyl-FAD (His46)**, producing fumarate and reduced FADH₂. The covalent flavin linkage — installed post-translationally by the SdhE assembly factor through its RGxxE motif — is what raises the flavin redox potential enough to make succinate oxidation feasible; without it the enzyme is essentially inactive (only ~5% residual autocatalytic flavinylation). Electrons then tunnel one at a time through the SdhB iron–sulfur relay ([2Fe-2S] → [4Fe-4S] → [3Fe-4S]) to the quinone-binding site at the SdhC/SdhD membrane anchors, reducing quinone to quinol, which diffuses into the membrane pool to feed the aerobic respiratory chain. Long-range conformational coupling links the distal dicarboxylate and quinone sites, coordinating the two half-reactions.

**Dual pathway placement:** SdhA is the physical and metabolic node connecting the **TCA cycle** (succinate → fumarate, step 1/1 of the "fumarate from succinate" bacterial route) to the **oxidative respiratory chain** (electron donation to quinone). In the obligately aerobic *P. putida* KT2440, whose TCA cycle is fully operational and central to carbon metabolism, this makes SdhA essential for efficient aerobic energy generation and for channelling C4-dicarboxylate carbon flux.

**Substrate specificity summary:**

| Ligand | Role at active site |
|--------|---------------------|
| Succinate | Physiological substrate (oxidized → fumarate) |
| Fumarate | Product / reverse-reaction substrate |
| Malonate | Competitive inhibitor (non-oxidizable dicarboxylate analogue) |
| Oxaloacetate | Competitive inhibitor (tight-binding, regulatory) |

---

## Evidence Base

| PMID | Title (abbreviated) | How it supports the findings |
|------|--------------------|------------------------------|
| [22985599](https://pubmed.ncbi.nlm.nih.gov/22985599/) | Prokaryotic assembly factors for attachment of flavin to complex II | Defines the four-subunit Complex II architecture; SdhA = catalytic flavoprotein; covalent FAD is rare; succinate oxidation coupled to ubiquinone reduction |
| [37119852](https://pubmed.ncbi.nlm.nih.gov/37119852/) | An evolving view of complex II | Confirms Complex II operates at the junction of the electron-transport chain and the Krebs cycle |
| [36089066](https://pubmed.ncbi.nlm.nih.gov/36089066/) | How an assembly factor enhances covalent FAD attachment | Covalent flavin linkage absolutely required for succinate oxidation; SdhE/SDHAF2 enhance FAD binding |
| [32887801](https://pubmed.ncbi.nlm.nih.gov/32887801/) | Roles of SDHAF2 and dicarboxylate in flavinylation of SDHA | Dicarboxylate + assembly factor orient the flavin/capping domains during flavinylation |
| [24070374](https://pubmed.ncbi.nlm.nih.gov/24070374/) | Conserved RGxxE motif of SdhE required for flavinylation | Direct experimental evidence: SdhA flavinylation depends on SdhE; residual autocatalytic activity explains ~5% |
| [24374335](https://pubmed.ncbi.nlm.nih.gov/24374335/) | SdhE required for flavinylation of fumarate reductase | SdhE flavinylates and activates SDH (and the paralogous FRD) across bacteria |
| [6733163](https://pubmed.ncbi.nlm.nih.gov/6733163/) | Interaction of succinate dehydrogenase and oxaloacetate | Single dicarboxylate-specific site shared by substrate and inhibitor |
| [6691982](https://pubmed.ncbi.nlm.nih.gov/6691982/) | Membrane-bound SDH with substrate and competitive inhibitors | Succinate/fumarate substrates and malonate/oxaloacetate inhibitors define specificity |
| [23711795](https://pubmed.ncbi.nlm.nih.gov/23711795/) | Conserved lysine controls Fe-S redox chemistry in FRD | Describes the Fe-S/quinone electron-transfer path downstream of the flavin |
| [27810396](https://pubmed.ncbi.nlm.nih.gov/27810396/) | Complex II: ROS production and ubiquinone reduction kinetics | Long-distance coupling between dicarboxylate and quinone sites; ROS side reaction |
| [24951791](https://pubmed.ncbi.nlm.nih.gov/24951791/) | Central carbon metabolism in *P. putida* KT2440 | Establishes the TCA cycle as tightly regulated central metabolism in the target organism |

The evidence base is internally consistent: multiple independent lines (UniProt/KEGG annotation, comparative genomics of the operon, sequence-alignment conservation, classic enzymology, structural/assembly studies, and direct genetic experiments on SdhE) all converge on the same functional assignment. One nuance worth noting is that the assembly-factor requirement is not absolute in every system — in human breast cancer cells *"SDHAF2/SDH5 is dispensable for SDHA flavination"* via an alternative mechanism ([PMID: 27587393](https://pubmed.ncbi.nlm.nih.gov/27587393/)) — but in bacteria the SdhE dependence with residual autocatalysis is well documented and matches the Q88FA7 annotation.

---

## Supported and Refuted Hypotheses

**Supported:**

- *SdhA is the catalytic flavoprotein of Complex II catalyzing succinate:quinone oxidoreduction* — supported by UniProt/KEGG annotation, operon structure, and homology (Findings 1, 4, 6).
- *SdhA uses a covalent 8α-histidyl-FAD (His46) essential for catalysis, installed by SdhE* — supported by UniProt features and Cecchini-group biochemistry plus direct SdhE genetics (Findings 2, 7).
- *Substrate specificity is limited to C4-dicarboxylates with malonate/oxaloacetate as competitive inhibitors* — supported by Vinogradov-group kinetics (Finding 5).
- *The enzyme is a cytoplasm-facing peripheral inner-membrane protein feeding electrons to quinone via SdhB Fe–S clusters* — supported by localization annotation and structural literature (Finding 3).

**Refuted / ruled out:**

- *That PP_4191 could be an anaerobic fumarate reductase (FrdA)* — ruled out by the dedicated *sdhCDAB* operon (separate from any *frd* operon), the aerobic physiology of *P. putida*, and the SDH-type (not FRD-type) sequence signature.
- *That the gene symbol is ambiguous* — ruled out; all identity checks (EC number, family, domains, operon context, 70% identity to *E. coli* SdhA) converge on the SDH flavoprotein.

---

## Limitations and Knowledge Gaps

1. **No direct experimental characterization of the *P. putida* protein itself.** All mechanistic detail is transferred by orthology from *E. coli* (70% identity, full active-site conservation) and from mitochondrial/enterobacterial Complex II. No published crystal structure, enzyme kinetics, or knockout phenotype specific to *P. putida* KT2440 SdhA was located. The functional assignment is therefore highly confident but inferential for this exact protein.

2. **Quinone specificity not experimentally defined for *P. putida*.** *Pseudomonas* uses ubiquinone (UQ-9) aerobically, so ubiquinone is the inferred acceptor; the specific quinone kinetics of the *P. putida* enzyme have not been directly measured in the reviewed literature.

3. **Regulation of the operon in *P. putida* is not detailed.** While the *sdhCDAB* operon structure and TCA-cluster context are established, the transcriptional regulators and carbon-source-dependent expression of *sdhA* in KT2440 (which relies on the Entner–Doudoroff route and a tightly regulated TCA cycle) were not investigated here. This is peripheral to molecular function but relevant to *when* the enzyme is most active.

4. **SdhE dependence assumed by orthology.** *P. putida* is expected to encode an SdhE homologue, but the specific KT2440 gene and its RGxxE motif were confirmed by orthology to enterobacteria rather than by direct analysis of the KT2440 genome.

5. **Reverse (fumarate reductase) activity not assessed.** Whether *P. putida* SdhA contributes any fumarate-reductase activity under microaerobic conditions was not examined; given the obligately aerobic physiology this is likely negligible.

---

## Proposed Follow-up Experiments / Actions

1. **Confirm covalent flavinylation biochemically.** Purify recombinant *P. putida* SdhA and demonstrate covalent 8α-His46-FAD attachment (SDS-PAGE with in-gel flavin fluorescence, mass spectrometry of tryptic peptides) and its dependence on a co-expressed *P. putida* SdhE.

2. **Kinetic characterization.** Measure succinate:quinone oxidoreductase activity (k_cat, K_m for succinate and quinone) and competitive-inhibition constants (K_i) for malonate and oxaloacetate to confirm the single dicarboxylate site quantitatively in the KT2440 enzyme.

3. **His46 mutagenesis.** Construct a His46Ala (or His46Ser) variant to test the predicted loss of covalent flavinylation and succinate oxidation, directly validating the transferred mechanism.

4. **Identify and delete the *P. putida* SdhE homologue.** Locate the KT2440 *sdhE/ygfY* orthologue, verify the RGxxE motif, and generate a knockout to test the predicted ~5% residual (SdhE-independent) SdhA activity.

5. **Physiological knockout phenotyping.** Delete *sdhA* (PP_4191) and assess growth on succinate and other TCA substrates, respiration rates, and metabolic-flux redistribution to confirm the enzyme's role in aerobic central carbon metabolism.

6. **Structural determination.** Solve a cryo-EM or crystal structure of the *P. putida* SdhCDAB complex to directly confirm the dicarboxylate active-site geometry, the Fe-S relay, and the quinone-binding site predicted by the *E. coli* model.

---

*Report prepared from 5 iterations of autonomous investigation; 7 confirmed findings and 20 papers reviewed. Gene identity (sdhA / Q88FA7 / PP_4191, Pseudomonas putida KT2440) verified against UniProt protein description, family, domains, and operon context — no ambiguity found.*


## Artifacts

- [OpenScientist final report](sdhA-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](sdhA-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:22985599
2. PMID:37119852
3. PMID:36089066
4. PMID:32887801
5. PMID:23711795
6. PMID:27810396
7. PMID:24951791
8. PMID:6733163
9. PMID:6691982
10. PMID:24070374
11. PMID:24374335
12. PMID:27587393