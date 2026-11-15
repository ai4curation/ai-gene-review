---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-12T04:04:13.658608'
end_time: '2026-11-12T04:16:28.033893'
duration_seconds: 734.38
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: ECOLI
  gene_id: P11458
  gene_symbol: nadA
  uniprot_accession: P11458
  protein_description: 'RecName: Full=Quinolinate synthase {ECO:0000255|HAMAP-Rule:MF_00567,
    ECO:0000303|PubMed:18651751}; EC=2.5.1.72 {ECO:0000255|HAMAP-Rule:MF_00567, ECO:0000269|PubMed:10648170,
    ECO:0000269|PubMed:15898769, ECO:0000269|PubMed:15967443, ECO:0000269|PubMed:18674537};
    AltName: Full=Quinolinate synthetase A {ECO:0000303|PubMed:2841129};'
  gene_info: Name=nadA {ECO:0000255|HAMAP-Rule:MF_00567, ECO:0000303|PubMed:2841129};
    Synonyms=nicA; OrderedLocusNames=b0750, JW0733;
  organism_full: Escherichia coli (strain K12).
  protein_family: Belongs to the quinolinate synthase family. Type 1
  protein_domains: NadA. (IPR003473); NadA_sf. (IPR036094); Quinolinate_synth_A_type1.
    (IPR023513); NadA (PF02445)
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
citation_count: 19
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: nadA-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: nadA-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** P11458
- **Protein Description:** RecName: Full=Quinolinate synthase {ECO:0000255|HAMAP-Rule:MF_00567, ECO:0000303|PubMed:18651751}; EC=2.5.1.72 {ECO:0000255|HAMAP-Rule:MF_00567, ECO:0000269|PubMed:10648170, ECO:0000269|PubMed:15898769, ECO:0000269|PubMed:15967443, ECO:0000269|PubMed:18674537}; AltName: Full=Quinolinate synthetase A {ECO:0000303|PubMed:2841129};
- **Gene Information:** Name=nadA {ECO:0000255|HAMAP-Rule:MF_00567, ECO:0000303|PubMed:2841129}; Synonyms=nicA; OrderedLocusNames=b0750, JW0733;
- **Organism (full):** Escherichia coli (strain K12).
- **Protein Family:** Belongs to the quinolinate synthase family. Type 1
- **Key Domains:** NadA. (IPR003473); NadA_sf. (IPR036094); Quinolinate_synth_A_type1. (IPR023513); NadA (PF02445)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "nadA" matches the protein description above**
2. **Verify the organism is correct:** Escherichia coli (strain K12).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'nadA' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **nadA** (gene ID: P11458, UniProt: P11458) in ECOLI.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *nadA* / Quinolinate Synthase (P11458, *Escherichia coli* K-12)

**UniProt:** P11458 | **Gene:** *nadA* (syn. *nicA*; b0750 / JW0733) | **EC 2.5.1.72**
**Organism:** *Escherichia coli* (strain K-12) | **Family:** Quinolinate synthase family, Type 1 (Pfam PF02445; InterPro IPR003473/IPR023513)

## Summary

The *E. coli* K-12 gene **nadA** (UniProt **P11458**; ordered locus **b0750 / JW0733**; synonym *nicA*) encodes **quinolinate synthase** (**EC 2.5.1.72**, also historically "quinolinate synthetase A"), a soluble cytoplasmic iron–sulfur enzyme that catalyzes the **committed step of de novo NAD biosynthesis**. The enzyme condenses **dihydroxyacetone phosphate (DHAP)** with **iminoaspartate (IA)** — the latter supplied by the upstream flavoenzyme L-aspartate oxidase (NadB) — to produce **quinolinic acid (QA)**, the universal precursor of nicotinamide adenine dinucleotide (NAD). This identification is unambiguous and fully consistent with the UniProt annotation: the gene symbol, organism (*E. coli* K-12), EC number, protein family (quinolinate synthase, Type 1), and Pfam/InterPro domains (NadA, PF02445; IPR003473) all converge on the same well-characterized enzyme. No gene-symbol ambiguity was encountered; the literature for *E. coli* nadA is deep and internally consistent.

Mechanistically, NadA is a **[4Fe-4S]-cluster enzyme**. The cluster is ligated by only three conserved cysteines (**Cys113, Cys200, Cys297**), leaving a **unique, non-cysteinyl-ligated iron** exposed; this special iron functions as a **Lewis acid** that activates DHAP (analogous to the catalytic Zn²⁺ of class II aldolases) and orchestrates a demanding multi-step chemical transformation — dephosphorylation, isomerization, cyclization, and two dehydrations — within a narrow active site formed at the convergence of the protein's three homologous domains. The cluster is highly **oxygen-labile** and is **absolutely required** for activity; its loss upon air exposure inactivates the enzyme. Reconstitution experiments with purified *E. coli* enzymes demonstrate that **NadA + NadB alone are sufficient** to make quinolinate from L-aspartate, DHAP, and O₂, definitively excluding any additional enzymes in the bacterial de novo pathway.

Physiologically, NadA acts in the **cytosol** as the central enzyme of the linear route **NadB → NadA → NadC** (where NadC, quinolinate phosphoribosyltransferase, next condenses QA with PRPP). It is **physically and functionally coupled to NadB**, and loss of nadA produces a nicotinic-acid-requiring (Nic⁻) auxotroph that must rely on the pyridine salvage pathway. Expression of nadA is **trans-repressed by the multifunctional regulator NadR** according to cellular NAD status, tying de novo flux to demand. Assembly of the catalytic cluster depends on the cell's **Fe–S biogenesis machinery** (ISC/SUF systems and NifS-type cysteine desulfurases, with a specific documented connection to the *E. coli* CsdA–CsdE system), and the cluster additionally contributes to correct folding and structural stability of the protein. NadA's sole physiological role is de novo quinolinate/NAD synthesis.

---

## Key Findings

### F001 — NadA is quinolinate synthase: it condenses iminoaspartate with DHAP to form quinolinate, the committed de novo NAD step

The primary function of the nadA gene product is the **synthesis of quinolinic acid**, the universal precursor of NAD. The enzyme (EC 2.5.1.72) catalyzes a **unique condensation reaction between iminoaspartate and dihydroxyacetone phosphate**, affording quinolinic acid ([PMID: 18803397](https://pubmed.ncbi.nlm.nih.gov/18803397/)). In *E. coli*, this reaction constitutes the second and committed step of the **de novo branch** of NAD biosynthesis: NAD "derives from quinolinic acid (QUIN) which in *Escherichia coli* is obtained through a pyridine salvage pathway or a de novo synthesis pathway. In the latter case, two enzymes, L-aspartate oxidase (NadB) and quinolinate synthase (NadA), are required for the synthesis of QUIN" ([PMID: 24120364](https://pubmed.ncbi.nlm.nih.gov/24120364/)).

The quinolinate produced is then handed off to the downstream enzyme **NadC** (quinolinate phosphoribosyltransferase), which condenses QA with phosphoribosyl pyrophosphate (PRPP). Thus NadA sits at the chemical heart of de novo NAD production. Measured specific activity of Fe/S-loaded *E. coli* NadA is on the order of ~0.10 µmol/min/mg (Saunders et al., 2008), consistent with a bona fide enzymatic catalyst rather than a scaffold. This identification matches the UniProt record precisely in gene symbol, organism, EC number, and reaction, confirming we are researching the correct protein.

### F002 — The enzyme carries an essential catalytic [4Fe-4S] cluster ligated by only three conserved cysteines (Cys113, Cys200, Cys297)

NadA is an **iron–sulfur enzyme**. The protein "was later shown to harbor a [4Fe-4S] cluster" ([PMID: 18803397](https://pubmed.ncbi.nlm.nih.gov/18803397/)). Careful dissection of the cluster ligands — combining in vivo complementation with enzymatic, spectroscopic (Mössbauer, EPR), and structural analyses of Cys→Ala variants — established that "**only three cysteine residues, the conserved Cys113, Cys200 and Cys297, are ligands of the cluster**" ([PMID: 18674537](https://pubmed.ncbi.nlm.nih.gov/18674537/)). This corrected an earlier hypothesis that a ferredoxin-like C291XXC294XXC297 motif coordinated the cluster. Instead, the study "demonstrated that **Cys291 and Cys294 form a disulfide bridge and are important for activity**" ([PMID: 18674537](https://pubmed.ncbi.nlm.nih.gov/18674537/)) — a distinct structural/redox feature, not a cluster ligand.

The three-cysteine ligation is functionally decisive: by leaving one iron of the cube **non-cysteinyl-ligated**, it creates the open coordination site required for substrate binding and catalysis (see F003). [4Fe-4S] clusters were shown to be a **common feature across NadA orthologues** from *E. coli*, *M. tuberculosis*, and *P. horikoshii*, establishing the cofactor as a conserved hallmark of this enzyme class rather than an idiosyncrasy of one organism.

### F003 — The unique non-cysteinyl iron acts as a Lewis acid during the multi-step condensation

High-resolution crystallography of NadA (from the thermophile *P. horikoshii*) in complex with DHAP, iminoaspartate analogues, and quinolinate revealed the catalytic logic of the special iron. In these structures, "**DHAP adopts a nearly planar conformation and chelates the [4Fe-4S] cluster via its keto and hydroxyl groups. The active site architecture suggests that the cluster acts as a Lewis acid in enediolate formation, like zinc in class II aldolases**" ([PMID: 27404889](https://pubmed.ncbi.nlm.nih.gov/27404889/)). This places NadA mechanistically alongside the class II aldolases, but using an iron of an Fe–S cluster rather than a mononuclear Zn²⁺ as the electrophilic catalyst.

The overall transformation is chemically demanding. Starting from DHAP and IA, "its synthesis comprises the condensation of dihydroxyacetone phosphate (DHAP) and iminoaspartate (IA), which involves **dephosphorylation, isomerization, cyclization, and two dehydration steps**" ([PMID: 34609124](https://pubmed.ncbi.nlm.nih.gov/34609124/)). Direct chemical evidence that the unique iron is the catalytic/substrate site comes from inhibitor studies: the dithiol phthalate intermediate analogue **DTHPA** blocks NAD biosynthesis in *E. coli*, and "the inhibitory effect can be explained by the **coordination of DTHPA thiolate groups to a unique Fe site of the NadA [4Fe-4S] cluster**" ([PMID: 22715136](https://pubmed.ncbi.nlm.nih.gov/22715136/)). Together these data identify the open iron as the locus where substrates are activated and intermediates are processed.

### F004 — NadA has a distinctive pseudo-threefold triangular fold built from three homologous domains (gene triplication)

The architecture of quinolinate synthase is unusual and informative. The first NadA crystal structure (*P. horikoshii*, 2.0 Å, with malate as a substrate analogue) revealed that "the overall structure exhibits a **unique triangular architecture composed of a 3-fold repeat of three-layer (alphabetaalpha) sandwich folding**" ([PMID: 15937336](https://pubmed.ncbi.nlm.nih.gov/15937336/)), with no similarity to previously known structures and the active site located at the interface of the three domains on the pseudo-3-fold axis. Structural work on the *P. furiosus* enzyme confirmed the evolutionary interpretation: "the structure is a homodimer consisting of **three domains per protomer**. Each domain shows the same topology with a four-stranded parallel β-sheet flanked by four α-helices, suggesting that the **domains are the result of gene triplication**" ([PMID: 23999292](https://pubmed.ncbi.nlm.nih.gov/23999292/)).

The active site is therefore a product of domain convergence, and it is **conformationally plastic**. "A tunnel, which can be opened or closed depending on the nature (or absence) of the bound ligand, connects this cofactor to the protein surface" ([PMID: 34609124](https://pubmed.ncbi.nlm.nih.gov/34609124/)). Site-directed mutagenesis, crystallography, and molecular dynamics indicate that a **transient second active-site cavity** forms to accommodate both substrates during the condensation — a dynamic feature well suited to a multi-step reaction that must sequester reactive intermediates from bulk solvent and from the oxygen-sensitive cluster.

### F005 — NadA functions in the cytoplasm, coupled to NadB, within the NadB → NadA → NadC route

NadA operates in the **cytosol** as a soluble protein; it has no signal peptide or membrane anchor, consistent with UniProt's cytoplasmic assignment. Functionally it is tightly linked to its upstream partner NadB, which produces the reactive intermediate iminoaspartate. The NadA–NadB interaction is genuine and conserved: "the **interaction between NadA and NadB is not species-specific** between *B. subtilis* and *Escherichia coli*" ([PMID: 18959769](https://pubmed.ncbi.nlm.nih.gov/18959769/)), implying a functional coupling that channels the labile IA intermediate.

This coupling has been exploited and demonstrated in metabolic engineering: "quinolinic acid production was accelerated by **assembling NadB and NadA as an enzyme complex** with the help of peptide-peptide interaction peptides RIAD and RIDD" ([PMID: 34192552](https://pubmed.ncbi.nlm.nih.gov/34192552/)), achieving high quinolinate titres (3.7 g/L) by channeling iminoaspartate directly from NadB to NadA. The physiological importance of the pathway is underscored by genetics: silencing of nadA/nadB generates a nicotinic-acid-requiring auxotroph, since "this phenotype depends on the silencing of the **nadB and nadA genes**" ([PMID: 24120364](https://pubmed.ncbi.nlm.nih.gov/24120364/)). In other words, NadA's role is restricted to de novo quinolinate/NAD synthesis; without it (or NadB), the cell must salvage preformed pyridines.

### F006 — nadA expression is trans-regulated by the NAD-responsive repressor NadR; the gene maps to min ~17 (b0750), separate from nadB/nadR

De novo NAD flux is demand-controlled at the level of nadA transcription. Classical *E. coli* K-12 genetics mapped nadA near min 17 of the chromosome and identified a regulatory locus "tentatively **designated nadR based on its regulation of the unlinked nadA gene**" ([PMID: 4349027](https://pubmed.ncbi.nlm.nih.gov/4349027/)); nadR maps near min 49, adjacent to nadB, and all of nadA, nadB, and nadR mutants show a phenotypic requirement for NAD or an immediate precursor. NadR is a **multifunctional protein**: it comprises "(i) an **N-terminal DNA-binding domain involved in the transcriptional regulation of NAD biosynthesis**, (ii) a central nicotinamide mononucleotide adenylyltransferase (NMNAT) domain, and (iii) a C-terminal RNK domain" ([PMID: 12446641](https://pubmed.ncbi.nlm.nih.gov/12446641/)), and it also carries NMN adenylyltransferase catalytic activity, synthesizing NAD from NMN and ATP ([PMID: 10464228](https://pubmed.ncbi.nlm.nih.gov/10464228/)).

The repression link is confirmed by engineering experiments where deactivating NadR boosts flux: production strains inactivated **"NadR (to eliminate the repression of L-aspartate oxidase and quinolinate synthase)"** ([PMID: 34192552](https://pubmed.ncbi.nlm.nih.gov/34192552/)). Thus NadR acts as a sensor-effector that represses nadA (and nadB) when NAD is abundant, coupling de novo synthesis to cellular NAD status.

### F007 — NadA activity depends on Fe–S biogenesis machinery to assemble its oxygen-labile cluster, which also stabilizes the fold

Because NadA's catalytic cluster is destroyed by O₂, the enzyme depends on the cell's iron–sulfur cluster assembly systems to be made and kept active. The cluster's oxygen sensitivity explains the historical difficulty in obtaining active enzyme: its "observed labile activity, **especially in the presence of hyperbaric oxygen**" ([PMID: 18803397](https://pubmed.ncbi.nlm.nih.gov/18803397/)). Co-expression with the **isc or suf** operons (or using IscR-deficient / "SufFeScient" hosts) increases NadA yield and cluster occupancy, and importantly "**the presence of the Fe-S cluster is contributing to correct folding and structural stability of the proteins**" ([PMID: 36527507](https://pubmed.ncbi.nlm.nih.gov/36527507/)) — so the cofactor is both catalytic and structural.

Direct enzymology of maturation shows cysteine desulfurases can build the cluster onto apo-NadA: in *B. subtilis*, "**NifS is catalytically competent in promoting cluster assembly onto apo-NadA**" ([PMID: 41066930](https://pubmed.ncbi.nlm.nih.gov/41066930/)), and nifS inactivation causes NAD-pathway failure and nicotinic-acid auxotrophy. The principle extends across kingdoms: in *Arabidopsis*, the chloroplast NadA equivalent (SufE3) "carr[ies] a **highly oxygen-sensitive (4Fe-4S) cluster at its NadA domain**," reconstitutable via its own SufE/CpNifS system ([PMID: 17452319](https://pubmed.ncbi.nlm.nih.gov/17452319/)). Collectively, these results place NadA firmly within the Fe–S client network and explain its characteristic oxygen lability.

### F008 — Direct *E. coli* evidence: purified NadA + NadB alone suffice to make quinolinate, and the [4Fe-4S] cluster is absolutely required

The most decisive evidence comes from reconstitution with purified *E. coli* enzymes. Ceciliani et al. (2000) showed that "it is possible to **synthesize quinolinic acid from L-aspartate, dihydroxyacetone phosphate, and O₂ by using only nadA and nadB gene overexpressed products**" ([PMID: 10648170](https://pubmed.ncbi.nlm.nih.gov/10648170/)) — definitively excluding any third enzyme from the bacterial de novo QA pathway and confirming NadA as the sole quinolinate-forming catalyst.

The cofactor requirement is equally clear-cut. Anaerobically purified *E. coli* NadA "contains **3–3.5 iron and 3–3.5 sulfide/polypeptide chain**" ([PMID: 15967443](https://pubmed.ncbi.nlm.nih.gov/15967443/)), with Mössbauer spectroscopy assigning the majority as a [4Fe-4S]²⁺ cluster; critically, "**the cluster is absolutely required for NadA activity**" ([PMID: 15967443](https://pubmed.ncbi.nlm.nih.gov/15967443/)), and air exposure degrades the cluster and inactivates the enzyme. Finally, a host-specific maturation route is documented in *E. coli*: analysis of the heteromeric cysteine desulfurase "pointed to a **specific connection between the CSD system and quinolinate synthetase NadA**" ([PMID: 15901727](https://pubmed.ncbi.nlm.nih.gov/15901727/)), identifying CsdA–CsdE as a relevant Fe–S maturation partner in *E. coli* itself.

---

## Mechanistic Model / Interpretation

### The de novo NAD pathway in *E. coli*

NadA is the central enzyme of a short, linear de novo route that feeds into universal NAD biosynthesis. In *E. coli*, two routes supply quinolinate / NAD: the **de novo** pathway (shown below) and a **salvage** pathway that recycles preformed pyridines. NadA is required only for the former.

```
                     NadB                      NadA                      NadC
 L-aspartate ───────────────────►  Iminoaspartate ───────────►  Quinolinic acid ───────────►  NaMN ─ ... ─► NAD
  + O2      (L-aspartate oxidase,      (IA)       + DHAP        (QA, universal     + PRPP
             flavoenzyme, FAD)                  [4Fe-4S]        NAD precursor)    (− CO2, − PPi)
                                              quinolinate
                                                synthase
                                              (EC 2.5.1.72)
                   │                             │
                   └──── physical/functional ────┘
                         coupling (channels
                         the labile IA intermediate)
```

The reaction catalyzed by NadA is not a simple aldol condensation but a cascade requiring **dephosphorylation, isomerization, cyclization, and two dehydrations**, all performed within a single, solvent-shielded active site at the junction of NadA's three homologous domains.

### The active site: a Lewis-acid iron in a triplicated fold

```
  NadA protomer (pseudo-3-fold symmetric; 3 domains from gene triplication)
  ┌──────────────────────────────────────────────────┐
  │   Domain 1 ┐                                       │
  │   Domain 2 ┼──► converge at pseudo-3-fold axis     │
  │   Domain 3 ┘           │                           │
  │                        ▼                           │
  │                [4Fe-4S] cluster                    │
  │        Cys113 ┐                                    │
  │        Cys200 ┼─ ligate 3 of the 4 Fe              │
  │        Cys297 ┘                                    │
  │                4th Fe = UNIQUE, non-cysteinyl       │
  │                        │  ← Lewis acid              │
  │                        ▼                            │
  │          binds/activates DHAP (keto + OH),          │
  │          forms enediolate (cf. class II aldolase)   │
  │                                                     │
  │   Cys291—Cys294 disulfide bridge (NOT ligands;      │
  │           important for activity)                   │
  │   Ligand-gated tunnel to surface; transient 2nd     │
  │           cavity accommodates both substrates       │
  └──────────────────────────────────────────────────┘
```

The cluster is a dual-purpose cofactor: (1) **catalytic** — its unique iron is a Lewis acid that activates DHAP, as shown by both crystallography (DHAP chelating the cluster) and inhibitor chemistry (DTHPA thiolates coordinating the unique Fe); and (2) **structural** — it contributes to correct folding and stability. Its extreme O₂-sensitivity is the price of this open, reactive iron, and it makes NadA dependent on cellular Fe–S assembly and reducing/anaerobic conditions for full activity.

### Regulation and physiological logic

| Layer | Component | Role |
|---|---|---|
| Substrate supply | NadB (L-aspartate oxidase) | Produces the labile IA intermediate; physically coupled to NadA |
| Catalysis | **NadA** | Condenses IA + DHAP → quinolinate; committed de novo step |
| Downstream | NadC (QA phosphoribosyltransferase) | Consumes QA + PRPP → NaMN → NAD |
| Transcriptional control | NadR | NAD-responsive repressor of nadA/nadB; also an NMNAT/RNK bifunctional salvage enzyme |
| Cofactor maturation | ISC / SUF; NifS-type desulfurases; CsdA–CsdE in *E. coli* | Assemble and insert the [4Fe-4S] cluster |

The system is economical: NadR senses NAD status and represses de novo genes when NAD is plentiful, while itself contributing salvage enzymatic activity — so the cell shifts between de novo synthesis and salvage according to supply. Loss of NadA (or NadB) collapses the de novo branch, forcing dependence on salvage and producing the classic **Nic⁻ auxotrophy**.

### Localization

All available evidence places NadA in the **cytoplasm**: it is a soluble protein lacking a signal peptide or transmembrane segment, its substrates (DHAP, IA from NadB) are cytosolic metabolites, and its partner enzymes NadB and NadC are cytosolic. This is consistent with the UniProt subcellular assignment.

---

## Evidence Base

| PMID | Paper (abbrev.) | How it supports the findings |
|---|---|---|
| [18803397](https://pubmed.ncbi.nlm.nih.gov/18803397/) | Characterization of quinolinate synthases from *E. coli*, *M. tuberculosis*, *P. horikoshii* | States the reaction (IA + DHAP → QA); confirms [4Fe-4S] cluster is common across orthologues; documents O₂ lability (F001, F002, F007) |
| [24120364](https://pubmed.ncbi.nlm.nih.gov/24120364/) | Molecular evolution of nicotinic acid requirement in Shigella/EIEC | Places NadA with NadB in the *E. coli* de novo QA route; nadA/nadB silencing → Nic⁻ auxotrophy (F001, F005) |
| [18674537](https://pubmed.ncbi.nlm.nih.gov/18674537/) | [4Fe-4S] cluster of *E. coli* NadA: cluster ligands | Identifies Cys113/Cys200/Cys297 as the only cluster ligands; Cys291–Cys294 form a disulfide (F002) |
| [27404889](https://pubmed.ncbi.nlm.nih.gov/27404889/) | Crystal structures of NadA with DHAP, IA analogues, quinolinate | DHAP chelates the cluster; Lewis-acid role like class II aldolase Zn (F003) |
| [34609124](https://pubmed.ncbi.nlm.nih.gov/34609124/) | Transient second active-site cavity during QA synthesis | Enumerates the reaction steps; describes ligand-gated tunnel and transient cavity (F003, F004) |
| [22715136](https://pubmed.ncbi.nlm.nih.gov/22715136/) | Inhibitor binding to the NadA [4Fe-4S] cluster | DTHPA thiolates coordinate a unique Fe site — defines the catalytic Fe (F003) |
| [15937336](https://pubmed.ncbi.nlm.nih.gov/15937336/) | First crystal structure of quinolinate synthase (*P. horikoshii*) | Triangular 3-fold (αβα) sandwich architecture; active site at domain interface (F004) |
| [23999292](https://pubmed.ncbi.nlm.nih.gov/23999292/) | Active-site models for NadA complexes (*P. furiosus*) | Three domains per protomer from gene triplication (F004) |
| [18959769](https://pubmed.ncbi.nlm.nih.gov/18959769/) | L-aspartate oxidase & quinolinate synthase from *B. subtilis* | NadA–NadB interaction is functional and not species-specific (F005) |
| [34192552](https://pubmed.ncbi.nlm.nih.gov/34192552/) | Metabolic engineering of *E. coli* for QA (NadB–NadA complex) | NadB+NadA channeled as complex; NadR represses both enzymes (F005, F006) |
| [4349027](https://pubmed.ncbi.nlm.nih.gov/4349027/) | Recognition of the NAD-biosynthesis regulatory gene | Defines NadR as trans-regulator of unlinked nadA; maps loci (F006) |
| [12446641](https://pubmed.ncbi.nlm.nih.gov/12446641/) | Ribosylnicotinamide kinase domain of NadR | NadR is multifunctional with a DNA-binding regulatory domain (F006) |
| [10464228](https://pubmed.ncbi.nlm.nih.gov/10464228/) | NadR has NMN adenylyltransferase activity | NadR is also a catalytic salvage enzyme (F006) |
| [36527507](https://pubmed.ncbi.nlm.nih.gov/36527507/) | Maturation strategy influences Fe-S cofactor occupancy | Fe-S cluster contributes to NadA folding/stability; maturation affects occupancy (F007) |
| [41066930](https://pubmed.ncbi.nlm.nih.gov/41066930/) | Direct cluster assembly on NadA by *B. subtilis* NifS | NifS directly matures apo-NadA; links activity to Fe-S biogenesis (F007) |
| [17452319](https://pubmed.ncbi.nlm.nih.gov/17452319/) | *Arabidopsis* SufE2/SufE3 in chloroplast Fe-S & NAD synthesis | Plant NadA domain carries O₂-sensitive [4Fe-4S] cluster; cross-kingdom conservation (F007) |
| [10648170](https://pubmed.ncbi.nlm.nih.gov/10648170/) | Cloning/overexpression/purification of *E. coli* quinolinate synthetase | NadA + NadB alone suffice to make QA from Asp + DHAP + O₂ (F008) |
| [15967443](https://pubmed.ncbi.nlm.nih.gov/15967443/) | Quinolinate synthetase, an Fe-S enzyme in NAD biosynthesis | 3–3.5 Fe/S per chain; [4Fe-4S]²⁺; cluster absolutely required for activity (F008) |
| [15901727](https://pubmed.ncbi.nlm.nih.gov/15901727/) | Heteromeric CsdA–CsdE cysteine desulfurase in *E. coli* | Specific connection between the CSD system and NadA maturation (F008) |

**Strength of evidence.** The core function (F001, F008) rests on **direct, precise biochemistry with purified *E. coli* enzymes** — the gold standard — rather than on high-throughput inference. The cofactor chemistry (F002, F003) is supported by convergent spectroscopy (Mössbauer, EPR), site-directed mutagenesis, crystallography, and inhibitor studies. Structural insights (F004) come primarily from thermophilic orthologues (*P. horikoshii*, *P. furiosus*) but are strongly conserved and transferable. Regulation (F006) is grounded in classical genetics plus modern engineering confirmation.

---

## Limitations and Knowledge Gaps

1. **Structure of the *E. coli* enzyme specifically.** The most detailed active-site and mechanistic structures derive from **thermophilic orthologues** (*P. horikoshii*, *P. furiosus*). While the [4Fe-4S] cluster, three-cysteine ligation, triplicated fold, and Lewis-acid mechanism are conserved (and the *E. coli* cluster ligands were independently mapped), a complete high-resolution *E. coli* NadA structure with bound intermediates would close any residual species gap.

2. **Reaction intermediates remain partially inferred.** The multi-step pathway (dephosphorylation → isomerization → cyclization → two dehydrations) is well supported chemically, and an unexpected crystallographic species possibly representing an intermediate has been reported, but the full sequence of discrete intermediates and the exact order of steps are not completely resolved experimentally.

3. **Physiological maturation route in *E. coli*.** Multiple systems can mature the cluster (ISC, SUF, CsdA–CsdE; NifS in *B. subtilis*). Which system is the primary, physiologically dominant maturase for NadA **in vivo in *E. coli*** under various growth/oxygen conditions is not fully settled.

4. **Quantitative in vivo kinetics and flux control.** Precise in vivo kinetic parameters, the degree of metabolic channeling of iminoaspartate from NadB to NadA under native (non-engineered) conditions, and the quantitative contribution of de novo vs salvage flux across growth states are incompletely characterized.

5. **Regulatory detail.** The exact NadR operator sequences at the nadA promoter, binding affinities, and the small-molecule effector(s) (NAD, NMN, or related) that toggle NadR between repressor and non-repressor states in *E. coli* could be specified more precisely.

---

## Proposed Follow-up Experiments / Actions

1. **High-resolution *E. coli* NadA structures** trapped with DHAP, iminoaspartate analogues, and reaction intermediates under strictly anaerobic conditions — to confirm the Lewis-acid mechanism and transient second-cavity model directly in the target organism.

2. **Time-resolved mechanistic trapping** (rapid freeze-quench Mössbauer/EPR coupled with mass spectrometry) to capture and order the dephosphorylation/isomerization/cyclization/dehydration intermediates on the cluster's unique iron.

3. **Systematic in vivo maturase dependency test** — measure NadA holo-enzyme formation and activity in defined *E. coli* mutants (Δisc, Δsuf, ΔcsdA/csdE, under aerobic vs anaerobic growth) to rank the physiological maturation routes.

4. **Quantitative NadB–NadA channeling assay** using isotope-labelled aspartate and rapid-mixing to measure whether iminoaspartate is kinetically channeled between the two enzymes in native (non-fusion) complexes.

5. **Define the NadR–nadA regulatory circuit** — DNase footprinting/ChIP and in vitro binding assays to map the operator and determine the effector metabolite controlling NadR repression of nadA.

6. **Inhibitor / antibiotic development** — because de novo NAD synthesis is essential in many pathogens that lack robust salvage, structure-guided optimization of unique-Fe-targeting inhibitors (e.g., DTHPA analogues) against NadA is a promising antibacterial avenue; profile selectivity against host enzymes.

---

## Conclusion

*E. coli* nadA (P11458) encodes **quinolinate synthase (EC 2.5.1.72)**, a soluble **cytoplasmic [4Fe-4S] iron–sulfur enzyme** that catalyzes the committed step of **de novo NAD biosynthesis**: the condensation of **DHAP** with **iminoaspartate** (from NadB) to form **quinolinic acid**, the universal NAD precursor. A unique non-cysteinyl iron of the cluster (coordinated by Cys113/Cys200/Cys297) acts as a **Lewis acid** driving a multi-step condensation within a distinctive triplicated three-domain fold. Purified NadA + NadB are sufficient for the reaction, the oxygen-labile cluster is absolutely required for activity and also stabilizes the fold, cluster assembly depends on cellular Fe–S biogenesis, and expression is repressed by the NAD-responsive regulator NadR. NadA's sole physiological role is de novo quinolinate/NAD synthesis, and its loss causes nicotinic-acid auxotrophy.


## Artifacts

- [OpenScientist final report](nadA-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](nadA-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:18803397
2. PMID:24120364
3. PMID:18674537
4. PMID:27404889
5. PMID:34609124
6. PMID:22715136
7. PMID:15937336
8. PMID:23999292
9. PMID:18959769
10. PMID:34192552
11. PMID:4349027
12. PMID:12446641
13. PMID:10464228
14. PMID:36527507
15. PMID:41066930
16. PMID:17452319
17. PMID:10648170
18. PMID:15967443
19. PMID:15901727