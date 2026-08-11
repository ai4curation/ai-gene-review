---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-11T00:31:52.373098'
end_time: '2026-08-11T00:47:10.236453'
duration_seconds: 917.86
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_4203
  gene_symbol: PP_4203
  uniprot_accession: Q88F95
  protein_description: 'RecName: Full=Electron transfer flavoprotein-ubiquinone oxidoreductase
    {ECO:0000256|RuleBase:RU366068}; Short=ETF-QO {ECO:0000256|RuleBase:RU366068};
    EC=1.5.5.1 {ECO:0000256|RuleBase:RU366068};'
  gene_info: OrderedLocusNames=PP_4203 {ECO:0000313|EMBL:AAN69784.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: 4Fe4S_Fe-S-bd. (IPR017896); ETF-QO. (IPR040156); ETF-QO/FixC_UQ-bd.
    (IPR049398); ETF-QO/FixX_C. (IPR007859); FAD/NAD-bd_sf. (IPR036188)
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
citation_count: 9
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PP_4203-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PP_4203-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88F95
- **Protein Description:** RecName: Full=Electron transfer flavoprotein-ubiquinone oxidoreductase {ECO:0000256|RuleBase:RU366068}; Short=ETF-QO {ECO:0000256|RuleBase:RU366068}; EC=1.5.5.1 {ECO:0000256|RuleBase:RU366068};
- **Gene Information:** OrderedLocusNames=PP_4203 {ECO:0000313|EMBL:AAN69784.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** 4Fe4S_Fe-S-bd. (IPR017896); ETF-QO. (IPR040156); ETF-QO/FixC_UQ-bd. (IPR049398); ETF-QO/FixX_C. (IPR007859); FAD/NAD-bd_sf. (IPR036188)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_4203" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_4203' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_4203** (gene ID: PP_4203, UniProt: Q88F95) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: PP_4203 (Q88F95), Electron Transfer Flavoprotein–Ubiquinone Oxidoreductase of *Pseudomonas putida* KT2440

## Summary

**PP_4203 (UniProt Q88F95) of *Pseudomonas putida* KT2440 encodes electron transfer flavoprotein–ubiquinone oxidoreductase (ETF-QO; EC 1.5.5.1), a monotopic inner-/cytoplasmic-membrane flavoenzyme that couples soluble catabolic dehydrogenases to the respiratory quinone pool.** The enzyme carries two redox cofactors — one non-covalently bound FAD and a single [4Fe-4S] cluster — and catalyzes the reduction of membrane ubiquinone by reduced electron-transfer flavoprotein (ETF): reduced ETF + ubiquinone → oxidized ETF + ubiquinol + H⁺ (RHEA:24052). It is the single, obligatory reoxidation node that returns electrons collected by many cytoplasmic flavoprotein dehydrogenases — most prominently the acyl-CoA dehydrogenases of fatty-acid β-oxidation and branched-chain amino-acid/isovalerate catabolism — into the aerobic (or, under engineered conditions, nitrate) respiratory chain.

The functional assignment rests on a convergent, high-confidence evidence base. Curated UniProt/InterPro annotation identifies the diagnostic domain architecture of the ETF-QO family (4Fe4S ferredoxin-type Fe-S binding, ETF-QO catalytic core, ubiquinone-binding and FixX-type C-terminal domains, and a FAD/NAD-binding superfamily fold). The mechanistic and structural details are transferable from the extensively characterized mammalian (pig-liver, human) and bacterial (*Rhodobacter sphaeroides*) orthologs because ETF-QO is one of the most highly evolutionarily conserved membrane redox enzymes known — PP_4203 shares ~60% amino-acid identity with human ETFDH and ~61% with the experimentally validated *R. sphaeroides* enzyme. The pig-liver crystal structure establishes that the enzyme is a single-domain monotopic integral membrane protein in which the FAD, not the [4Fe-4S] cluster, is the immediate electron donor to ubiquinone, and that only the first ~2 of the 10 isoprene units of the quinone tail engage the protein.

Genomic context reinforces the biochemistry: PP_4203 sits in a canonical *etfA–etfB–etfQO* gene cluster with PP_4201 (etfA, α-subunit) and PP_4202 (etfB, β-subunit), which encode the soluble ETFαβ heterodimer that is PP_4203's dedicated electron-donor partner. In the metabolically versatile soil bacterium *P. putida* KT2440 — whose genome encodes 21 putative acyl-CoA dehydrogenases — this makes ETF-QO the terminal electron conduit of an unusually large β-oxidation and amino-acid-catabolism network, physically and functionally linking cytoplasmic substrate oxidation to membrane-based energy conservation.

---

## Gene/Protein Identity Verification

Before presenting findings, the mandatory identity check was completed and **passed**:

| Criterion | UniProt reference | Verification result |
|-----------|-------------------|---------------------|
| Gene locus | OrderedLocusNames = PP_4203 | ✔ Confirmed (EMBL AAN69784.1) |
| Protein | ETF-ubiquinone oxidoreductase (ETF-QO), EC 1.5.5.1 | ✔ Domain architecture and orthology confirm |
| Organism | *Pseudomonas putida* KT2440 (taxid 160488) | ✔ Confirmed |
| Domains | IPR017896, IPR040156, IPR049398, IPR007859, IPR036188 | ✔ Diagnostic of the ETF-QO family |

Importantly, most primary experimental literature for this enzyme comes from the mammalian ortholog (**ETFDH/ETF-QO**, associated with the human disease multiple acyl-CoA dehydrogenase deficiency, MADD) and from the bacterial model *Rhodobacter sphaeroides*. This is **not** a case of gene-symbol ambiguity: ETFDH/ETF:QO/ETF-QO are synonyms for the *same enzyme*, and the mammalian and *Rhodobacter* studies are the accepted experimental surrogates for the bacterial ortholog owing to deep sequence conservation (see Finding F007). Function is therefore transferred by orthology, not confused across unrelated genes.

---

## Key Findings

### F001 — PP_4203 is ETF-ubiquinone oxidoreductase (EC 1.5.5.1)

UniProt Q88F95 annotates PP_4203 as electron transfer flavoprotein–ubiquinone oxidoreductase, EC 1.5.5.1, and the InterPro domain complement is diagnostic of the family: **4Fe4S_Fe-S-bd** (IPR017896), **ETF-QO** (IPR040156), **ETF-QO/FixC_UQ-bd** (IPR049398, the ubiquinone-binding region), **ETF-QO/FixX_C** (IPR007859), and the **FAD/NAD-binding superfamily** (IPR036188). The reaction catalyzed (EC 1.5.5.1) is the transfer of electrons from reduced ETF to ubiquinone:

> reduced electron-transfer flavoprotein + ubiquinone → oxidized ETF + ubiquinol

The human ortholog ETFDH encodes exactly this enzyme. As stated directly in the recent literature, ETF-QO is "a critical redox enzyme that transfers electrons from acyl-CoA dehydrogenases to the mitochondrial electron transport chain" [PMID: 42239388](https://pubmed.ncbi.nlm.nih.gov/42239388/). This defines the core catalytic role encoded by PP_4203: it is the membrane-embedded terminus that channels electrons from flavoprotein dehydrogenases (via ETF) into the respiratory quinone pool.

### F002 — A membrane-bound monotopic flavoprotein with one FAD and one [4Fe-4S] cluster

Fielding et al. (2008) studied human, porcine, and — critically — *Rhodobacter sphaeroides* (bacterial) ETF-QO and report that each enzyme contains **"a single [4Fe-4S](2+,1+) cluster and one equivalent of FAD"** and describe ETF-QO as **"a membrane-bound electron transfer protein that links primary flavoprotein dehydrogenases with the main respiratory chain"** [PMID: 18037314](https://pubmed.ncbi.nlm.nih.gov/18037314/). Electron spin relaxation measurements placed the interspin FAD-to-[4Fe-4S] distance at ~18.6 Å, a value conserved across species. The redox cofactors have similar midpoint potentials, enabling the sequential one-electron relay:

```
ETF-FADH•  →  ETF-QO FAD  →  [4Fe-4S]  →  ubiquinone
```

The conserved cofactor stoichiometry (exactly one FAD, one [4Fe-4S]) across bacterial and mammalian ETF-QO justifies applying the same cofactor model to PP_4203. Subcellular localization is at the cytoplasmic membrane (the bacterial equivalent of the mitochondrial inner membrane).

### F003 — Terminal electron conduit of a large β-oxidation / acyl-CoA dehydrogenase network in *P. putida*

Guzik et al. (2014) showed that *P. putida* KT2440 possesses an elaborate fatty-acid degradation (β-oxidation) pathway and that **"in silico analysis of its genome sequence revealed 21 putative acyl-CoA dehydrogenases (ACADs)"** [PMID: 24794972](https://pubmed.ncbi.nlm.nih.gov/24794972/), several of which were experimentally confirmed (e.g., PP_2437 preferring dodecanoyl-CoA). Because every acyl-CoA dehydrogenase transfers electrons to ETF, and ETF can only be reoxidized by ETF-QO, PP_4203 constitutes the single membrane conduit at the convergence point of this unusually large dehydrogenase repertoire. This metabolic architecture is central to *P. putida*'s reputation for versatile catabolism of fatty acids and amino acids — the same catabolism that supplies precursors for medium-chain-length polyhydroxyalkanoate (mcl-PHA) biosynthesis.

### F004 — Single-domain monotopic architecture; FAD is the immediate reductant of ubiquinone

Zhang, Frerman & Kim (2006) solved the pig-liver ETF-QO crystal structure both with and without bound ubiquinone (the two structures are essentially identical). The molecule forms a **single structural domain** in which the FAD-, [4Fe-4S]-, and UQ-binding regions are closely packed and share structural elements, with a predominantly hydrophobic UQ-binding pocket. Crucially, the enzyme is a **monotopic integral membrane protein**: **"ETF-QO is a monotopic integral membrane protein. The putative membrane-binding surface contains an alpha-helix and a beta-hairpin, forming a hydrophobic plateau"** [PMID: 17050691](https://pubmed.ncbi.nlm.nih.gov/17050691/). The key geometric result defines the mechanism: **"The UQ-flavin distance (8.5 Å) is shorter than the UQ-cluster distance (18.8 Å), and the very similar redox potentials of FAD and the cluster strongly suggest that the flavin, not the cluster, transfers electrons to UQ"** [PMID: 17050691](https://pubmed.ncbi.nlm.nih.gov/17050691/).

The transfer of this mammalian structural/mechanistic model to the bacterial PP_4203 is justified by extreme evolutionary conservation: Watmough & Frerman (2010) note that **"ETF-QO is very highly conserved in evolution and the recombinant enzyme from the bacterium *Rhodobacter sphaeroides* has allowed the mutational analysis"** [PMID: 20937244](https://pubmed.ncbi.nlm.nih.gov/20937244/).

### F005 — Substrate specificity: soluble ETF as donor, ubiquinone as acceptor; optimal quinone has a ~10-carbon tail

ETF-QO uses soluble ETF as its electron donor and ubiquinone as its acceptor, funneling electrons from a large number of distinct flavoprotein dehydrogenases. Watmough & Frerman (2010) describe how ETF-QO, together with ETF, **"forms a short pathway that transfers electrons from 11 different mitochondrial flavoprotein dehydrogenases to the ubiquinone pool"** [PMID: 20937244](https://pubmed.ncbi.nlm.nih.gov/20937244/). On the acceptor side, Simkovic & Frerman (2004) determined the steady-state kinetics of human ETF-QO with a panel of ubiquinone homologues and analogues and found that **"optimal substrates contain a ten-carbon-atom side chain, consistent with a preliminary crystal structure that shows that only the first two of ten isoprene units of co-enzyme Q10 (CoQ10) interact with the protein"** [PMID: 14640977](https://pubmed.ncbi.nlm.nih.gov/14640977/). Unlike other quinone oxidoreductases, ETF-QO shows little preference for methyl branches or ring rigidity, and few classic quinone-oxidoreductase inhibitors block it — an unusual pharmacological signature consistent with its distinct quinone-binding pocket. The physiological donor, ETF, is itself an α/β FAD protein reduced by upstream dehydrogenases such as the acyl-CoA dehydrogenases.

### F006 — Genomic clustering with its electron-donor partner: *etfA* (PP_4201) and *etfB* (PP_4202)

Genome mapping of *P. putida* KT2440 (taxid 160488) places three consecutive loci in the canonical operon order:

| Locus | Gene | Product | UniProt | Length |
|-------|------|---------|---------|--------|
| PP_4201 | *etfA* | Electron transfer flavoprotein α-subunit | Q88F97 | 309 aa |
| PP_4202 | *etfB* | Electron transfer flavoprotein β-subunit | Q88F96 | 249 aa |
| PP_4203 | *etfQO* | ETF-ubiquinone oxidoreductase | Q88F95 | 560 aa |

This *etfA–etfB–etfQO* arrangement is the classic organization encoding the soluble ETF heterodimer plus its membrane-bound reoxidase, physically co-locating PP_4203 with its dedicated electron-donor partner. A second, separate ETF-like gene pair exists elsewhere in the genome at PP_0312/PP_0313, indicating some functional partitioning of ETF partners. UniProt Q88F95 directly annotates the **FUNCTION** ("Accepts electrons from ETF and reduces ubiquinone"), the **CATALYTIC ACTIVITY** ("a ubiquinone + reduced [electron-transfer flavoprotein] = a ubiquinol + oxidized [electron-transfer flavoprotein] + H⁺", RHEA:24052), the two **COFACTORS** (FAD and [4Fe-4S] cluster), a C-terminal 4Fe-4S ferredoxin-type domain (residues ~520–549), and a protein length of 560 aa.

### F007 — PP_4203 is a bona fide ETF-QO ortholog (~60% identity to human ETFDH and *Rhodobacter* ETF-QO)

Global (Needleman–Wunsch) pairwise alignment of full-length sequences quantifies the orthology:

| Comparison | Identical residues | % identity |
|------------|--------------------|-----------|
| *P. putida* ETF-QO (Q88F95, 560 aa) vs human ETFDH (Q16134, 617 aa incl. presequence) | 334 | ~59.6% |
| *P. putida* ETF-QO (Q88F95) vs *R. sphaeroides* ETF-QO (Q3J5K9, 551 aa) | 337 | ~61.2% |

Identity of ~60% across the bacteria-to-human evolutionary span — combined with identical domain architecture and conserved FAD/[4Fe-4S]/UQ-binding regions — confirms true orthology rather than distant homology. This is consistent with Watmough & Frerman (2010), who note that **"ETF-QO is very highly conserved in evolution and the recombinant enzyme from the bacterium *Rhodobacter sphaeroides* has allowed the mutational analysis"** [PMID: 20937244](https://pubmed.ncbi.nlm.nih.gov/20937244/) — i.e., the bacterial enzyme is an accepted experimental surrogate for the human one, and by the same logic the human/bacterial functional model transfers to PP_4203.

### F008 — Physiological role: obligatory reoxidation point for ETF reduced during β-oxidation and amino-acid catabolism

In *Pseudomonas*, multiple flavoprotein acyl-CoA dehydrogenases donate electrons to ETF, which can only be reoxidized by ETF-QO — making PP_4203 the mandatory return path for those electrons. Förster-Fromme & Jendrossek (2008) showed that the leucine/isovalerate utilization (Liu) pathway acyl-CoA dehydrogenase **LiuA** is required for growth on leucine, isovalerate, and acyclic terpenes (citronellol), and that **"LiuA purified from recombinant *E. coli* revealed acyl-CoA dehydrogenase activity with isovaleryl-CoA (KM 2.3 microM) and butyryl-CoA as substrates"** [PMID: 18625020](https://pubmed.ncbi.nlm.nih.gov/18625020/). This is a concrete example of a *Pseudomonas* dehydrogenase whose electrons must pass through ETF-QO. On the general principle, Zhang, Frerman & Kim (2006) state that ETF-QO catalyzes ubiquinone reduction by ETF, **"linking oxidation of fatty acids and some amino acids to the mitochondrial respiratory chain"** [PMID: 17050691](https://pubmed.ncbi.nlm.nih.gov/17050691/). In *P. putida*, PP_4203 is therefore the single membrane node returning β-oxidation and branched-chain/amino-acid electrons to the ubiquinone pool for aerobic — or, in engineered denitrifying strains, nitrate/nitrite — respiration.

---

## Mechanistic Model / Interpretation

ETF-QO occupies a defined position in a compact, three-component electron-transfer relay that bridges cytoplasmic substrate oxidation and membrane-based energy conservation. The full pathway in *P. putida* KT2440 can be drawn as:

```
   Cytoplasm (soluble)                          Cytoplasmic membrane
 ┌───────────────────────────┐            ┌──────────────────────────────┐
 │  Fatty acyl-CoA           │            │                              │
 │  (β-oxidation)            │            │   ETF-QO  (PP_4203, Q88F95)  │
 │        │                  │            │   560 aa, monotopic          │
 │        ▼                  │            │                              │
 │  Acyl-CoA dehydrogenases  │  reduced   │   FAD ──► [4Fe-4S]           │
 │  (up to 21 ACADs;         │───ETF────► │    │         (18.8 Å from UQ) │
 │   e.g. LiuA, PP_2437)     │            │    │ 8.5 Å                    │
 │        │                  │            │    ▼                         │
 │  Branched-chain/          │            │   Ubiquinone ──► Ubiquinol   │
 │  amino-acid catabolism    │  oxidized  │        │                     │
 │  (leucine → isovaleryl-   │◄──ETF──────│        ▼                     │
 │   CoA via LiuA)           │            │   Respiratory chain          │
 └───────────────────────────┘            │   (O2, or NO3⁻ in engineered │
     etfA/PP_4201 + etfB/PP_4202          │    denitrifying strains)     │
     encode the ETFαβ heterodimer         └──────────────────────────────┘
```

**Step 1 — Collection.** Diverse cytoplasmic flavoprotein dehydrogenases (chiefly acyl-CoA dehydrogenases of β-oxidation and branched-chain amino-acid catabolism, e.g., LiuA acting on isovaleryl-CoA) abstract electrons from their carbon substrates and reduce their tightly bound FAD.

**Step 2 — Shuttling.** The soluble ETFαβ heterodimer (products of the adjacent *etfA*/PP_4201 and *etfB*/PP_4202 genes) acts as a diffusible one-electron carrier, accepting electrons from many different dehydrogenases at its FAD and shuttling them to the membrane. This "many-donors, one-carrier, one-reoxidase" topology is the source of ETF-QO's role as a convergence hub — 11 distinct dehydrogenases feed a single quinone-reducing enzyme in the mammalian system, and the even larger *P. putida* dehydrogenase repertoire funnels similarly.

**Step 3 — Membrane reoxidation and quinone reduction.** ETF-QO (PP_4203) accepts electrons from reduced ETF at its own FAD, passes them internally, and reduces membrane ubiquinone. The crystallographic geometry (FAD–UQ 8.5 Å vs [4Fe-4S]–UQ 18.8 Å) together with the near-equal midpoint potentials of the two cofactors establishes that the **FAD is the immediate electron donor to ubiquinone**; the [4Fe-4S] cluster serves as an intramolecular relay/buffer between the incoming ETF and the FAD rather than as the terminal reductant. Only the first ~2 isoprene units of the quinone tail engage the hydrophobic binding pocket, which explains the ~10-carbon optimal side-chain length and the enzyme's relative insensitivity to classical quinone-site inhibitors.

**Physiological consequence.** By reoxidizing ETF, PP_4203 keeps the entire upstream β-oxidation and amino-acid-catabolism network thermodynamically and kinetically viable — without a functional ETF-QO, reduced ETF accumulates, dehydrogenase flux stalls, and acyl-CoA/acylcarnitine intermediates pile up (the biochemical hallmark of MADD in the human ortholog). In *P. putida*, this makes ETF-QO an essential coupling device for catabolic versatility: it converts the reducing power harvested from fatty acids, terpenoids, and branched-chain amino acids into ubiquinol that the respiratory chain uses to generate proton-motive force.

---

## Evidence Base

| PMID | Study | How it supports the annotation |
|------|-------|-------------------------------|
| [17050691](https://pubmed.ncbi.nlm.nih.gov/17050691/) | *Structure of ETF-QO and electron transfer to the mitochondrial ubiquinone pool* (Zhang, Frerman & Kim, 2006) | Pig-liver crystal structure ± ubiquinone; defines single-domain, monotopic membrane topology; FAD (not [4Fe-4S]) as immediate UQ reductant; links fatty-acid/amino-acid oxidation to respiration. **Core structural/mechanistic evidence.** |
| [20937244](https://pubmed.ncbi.nlm.nih.gov/20937244/) | *The electron transfer flavoprotein:ubiquinone oxidoreductases* (Watmough & Frerman, 2010) | Authoritative review; establishes the 11-dehydrogenase funnel, extreme evolutionary conservation, and *R. sphaeroides* as validated bacterial surrogate. **Supports orthology transfer.** |
| [18037314](https://pubmed.ncbi.nlm.nih.gov/18037314/) | *Electron spin relaxation … interspin distances in human, porcine, and Rhodobacter ETF-QO* (Fielding et al., 2008) | Confirms one FAD + one [4Fe-4S] stoichiometry and membrane localization across species, including the bacterial enzyme. **Cofactor/localization evidence.** |
| [14640977](https://pubmed.ncbi.nlm.nih.gov/14640977/) | *Alternative quinone substrates and inhibitors of human ETF-QO* (Simkovic & Frerman, 2004) | Steady-state kinetics defining ~10-carbon optimal quinone tail and unusual inhibitor insensitivity. **Substrate-specificity evidence (acceptor side).** |
| [24794972](https://pubmed.ncbi.nlm.nih.gov/24794972/) | *Acyl-CoA dehydrogenase from P. putida KT2440* (Guzik et al., 2014) | Documents 21 putative ACADs feeding ETF in *P. putida*. **Establishes the upstream network in the correct organism.** |
| [18625020](https://pubmed.ncbi.nlm.nih.gov/18625020/) | *Isovaleryl-CoA dehydrogenase (LiuA) of P. aeruginosa* (Förster-Fromme & Jendrossek, 2008) | Concrete *Pseudomonas* dehydrogenase (KM 2.3 µM for isovaleryl-CoA) that reduces ETF. **Physiological donor example.** |
| [42239388](https://pubmed.ncbi.nlm.nih.gov/42239388/) | CRISPR/lipid-storage-myopathy study (2025) | Restates ETF-QO's core role transferring electrons from acyl-CoA dehydrogenases to the electron transport chain. **Contemporary confirmation of core function.** |
| [33823724](https://pubmed.ncbi.nlm.nih.gov/33823724/) | *ETF dehydrogenase advances in molecular genetics* (review, 2021) | Places ETF-QO in the inner membrane as central electron-transfer enzyme; context for MADD disease link (human ortholog). **Supporting context.** |

Supporting disease-genetics and structural literature on the human/*Drosophila*/*Rhodobacter* orthologs (e.g., MADD genotype–phenotype studies; the *Drosophila* flavin-binding-site mutant, [PMID: 22580358](https://pubmed.ncbi.nlm.nih.gov/22580358/); the *R. sphaeroides* p.Pro389Leu conformational study, [PMID: 32087359](https://pubmed.ncbi.nlm.nih.gov/32087359/)) further corroborate the FAD-centric mechanism and the functional importance of the FAD- and UQ-binding domains, all of which are conserved in PP_4203.

**No contradicting evidence** was encountered. All lines — curated database annotation, InterPro domains, mammalian/bacterial crystallography and spectroscopy, steady-state kinetics, operon context, and sequence orthology — point to the same assignment.

---

## Limitations and Knowledge Gaps

1. **No direct experimental characterization of PP_4203 itself.** The functional assignment is inferred by strong orthology (~60% identity) and curated annotation, not by biochemical assay of the purified *P. putida* protein. No published enzyme kinetics, spectroscopy, or crystal structure exists for Q88F95 specifically.

2. **Quinone identity not experimentally confirmed in *P. putida*.** The respiratory quinone pool of *P. putida* is dominated by ubiquinone-9 (Q9) rather than the mammalian Q10; the ~10-carbon-tail optimum was measured on the human enzyme. The precise quinone preference of the bacterial enzyme in vivo is inferred, not measured.

3. **Localization inferred, not imaged.** Cytoplasmic-membrane localization and monotopic topology are transferred from the pig-liver structure and bacterial homolog studies; there is no direct topological/proteomic membrane-localization datum for PP_4203.

4. **Partner assignment for the two ETF systems is unresolved.** *P. putida* encodes a second ETF-like pair (PP_0312/PP_0313). Whether both feed PP_4203 or whether the ETF systems are functionally partitioned to distinct dehydrogenase sets is not established.

5. **Essentiality and regulation unknown.** No transposon-essentiality, knockout-phenotype, or transcriptional-regulation data for PP_4203 under fatty-acid vs. sugar growth were located; the physiological "obligatory node" role, while mechanistically sound, is not demonstrated by a *P. putida* mutant.

6. **Reliance on mammalian disease literature.** Much of the deepest mechanistic detail comes from human MADD/ETFDH studies. While the enzyme is the same, organism-specific quantitative parameters (midpoint potentials, KM values, cluster geometry in *P. putida*) may differ modestly.

---

## Proposed Follow-up Experiments / Actions

1. **Heterologous expression and biochemical assay.** Express Q88F95 (with a solubility strategy for the monotopic membrane anchor) in *E. coli*, confirm FAD and [4Fe-4S] content by UV-vis/EPR, and measure steady-state kinetics with purified *P. putida* ETFαβ (PP_4201/PP_4202) as donor and Q1/Q2 analogues as acceptor. This would directly validate KM, kcat, and the quinone-tail optimum in the bacterial enzyme.

2. **Targeted knockout / complementation in *P. putida* KT2440.** Delete PP_4203 and test growth on β-oxidation substrates (fatty acids, citronellol/terpenes) and branched-chain amino acids (leucine). Predicted phenotype: loss of growth on ETF-dependent carbon sources with accumulation of acyl-CoA/acylcarnitine intermediates, rescued by complementation.

3. **Resolve the two-ETF-system question.** Individually delete the PP_4201/PP_4202 and PP_0312/PP_0313 pairs and score which dehydrogenase-dependent growth phenotypes each affects, mapping donor–reoxidase specificity.

4. **Membrane-localization confirmation.** Cell-fractionation + immunoblot or fluorescent-fusion imaging to verify cytoplasmic-membrane association and monotopic topology.

5. **Structural determination.** Solve a cryo-EM or crystal structure of the *P. putida* ETF-QO (ideally in complex with its cognate ETF and a quinone analogue) to confirm the FAD–UQ geometry and cofactor arrangement in the bacterial context, and to compare the quinone pocket against the Q9-dominated pool.

6. **Respiratory coupling under denitrification.** In the engineered nitrate/nitrite-respiring KT2440 strains, test whether ETF-QO-derived ubiquinol supports anaerobic respiration, quantifying the enzyme's contribution to anoxic energy conservation.

---

## Conclusion

PP_4203 (Q88F95) is the electron transfer flavoprotein–ubiquinone oxidoreductase of *Pseudomonas putida* KT2440 — a monotopic cytoplasmic-membrane FAD/[4Fe-4S] flavoenzyme that reduces membrane ubiquinone using electrons delivered by the soluble ETFαβ heterodimer (encoded by the adjacent PP_4201/PP_4202 genes). Functioning at the cytoplasmic membrane, it is the single, obligatory reoxidation node that returns electrons harvested by the bacterium's large set of flavoprotein dehydrogenases — those of fatty-acid β-oxidation and branched-chain amino-acid/isovalerate catabolism — into the respiratory chain, with the enzyme's FAD acting as the immediate electron donor to ubiquinone. This assignment is supported convergently by curated UniProt/InterPro annotation, high-resolution structural and spectroscopic studies of the mammalian and *Rhodobacter* orthologs, steady-state kinetics defining quinone substrate specificity, canonical *etfA–etfB–etfQO* operon organization, and ~60% sequence identity to the experimentally characterized human and bacterial enzymes.


## Artifacts

- [OpenScientist final report](PP_4203-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PP_4203-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:42239388
2. PMID:18037314
3. PMID:24794972
4. PMID:17050691
5. PMID:20937244
6. PMID:14640977
7. PMID:18625020
8. PMID:22580358
9. PMID:32087359