---
title: "Bacteriophage Genome Curation & Pathway Hole Filling"
maturity: SCOPING
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [BPT4, 9CAUD, BPZF4, BPBPP, BPPHT, BPD31, ENTM13, ENTPH, SIRV1]
autolink_gene_symbols: false
---

# Bacteriophage Genome Curation & Pathway Hole Filling

**Bottom line:** Bacteriophages are an unusually strong proving ground for combining **end-to-end whole-genome annotation review** with **module-based pathway satisfiability and hole filling** ([`PATHWAY_SATISFIABILITY.md`](PATHWAY_SATISFIABILITY.md)). Phage genomes are compact (4 to ~290 genes), organized into syntenic functional operons, and phenotypically constrained: every plaque-forming phage must execute host attachment, genome entry, replication/transcription, virion assembly, and host release—either via phage-encoded proteins, non-orthologous displacements hidden in "viral dark matter," or explicit hijacking of host machinery. Moreover, unlike cellular metabolic pathways where a missing step is almost always an annotation gap, phage lifecycles provide **true negatives by biology** (for example, the temperate latency/integration module is genuinely absent in obligately lytic phages like T7, T4, φX174, and MS2) and **mutually exclusive variant branches** (four distinct release mechanisms, three tail-ejection mechanisms, four packaging mechanisms), making them ideal for calibrating `evaluate()` and `abduce()` in [`src/ai_gene_review/module_logic.py`](../src/ai_gene_review/module_logic.py).

The repository already holds **61 phage and archaeal-virus gene folders** across 9 taxon codes (49 in T4 `BPT4`—46 `COMPLETE` and 3 `DRAFT` (`DAM`, `E`, `frd`) curated with Falcon deep research from [`SPKW/SPKW-BPT4.md`](SPKW/SPKW-BPT4.md)—plus 12 reviewed genes across `9CAUD`, `BPZF4`, `BPBPP`, `BPPHT`, `BPD31`, `ENTM13`, `ENTPH`, and `SIRV1`) alongside two viral modules (`MODULE:viral_factory` and `MODULE:anti_crispr_suppression`). A focused **5-genome core reference set** (**λ**, **φX174**, **MS2**, **T7**, and **M13/φ6/PRD1**, totaling ~160 genes—roughly the cost of half of T4) covers every branch of every core phage module.

---

## Why Phages for Module Satisfiability & Pathway Hole Filling?

Our module engine in [`src/ai_gene_review/module_logic.py`](../src/ai_gene_review/module_logic.py) treats `variant_sets` as `OR` and required `parts` as `AND`, using gene-product annotation presence as the oracle and `abduce(expr, env)` to propose minimal sets of missing steps ("pathway holes"). Phages test this architecture in five ways that cellular genomes cannot:

1. **Mutually exclusive `variant_sets` grounded in virion & envelope biology:**
   - **Release / Lysis module:** Four distinct routes—canonical 3-step `holin + endolysin + spanin` (λ, T7, T4), 2-step `holin + endolysin` without spanin (Gram-positive phages like φ29, SPO1; or mycolate-cleaving `Lysin A + Lysin B` in Mycobacteriophage L5), `single-gene lysis (Sgl)` inhibiting peptidoglycan biosynthesis (`GO:0039640` in φX174 `E` and Qβ `A2`, or membrane-lesion `L` in MS2), and non-lytic `chronic filamentous extrusion` (`GO:0099045` in M13). Each reference genome should satisfy **exactly one** branch; a module definition that lets M13 satisfy the holin route is wrong.
   - **Genome ejection module:** Three mutually exclusive mechanism children exist in GO (`GO:0099000` contractile tail, `GO:0099001` long flexible tail, `GO:0099002` short tail), plus pilus-retraction (`M13`, `MS2`), DNA pilot tube (`φX174`), and membrane-fusion/spike (`φ6`, `PRD1`) routes.
   - **Genome packaging module:** `GO:0098006` headful packaging (T4, P22, P1) vs. `GO:0098037` 5'-extended `cos` packaging (λ, P2) vs. terminal-protein (`gp3`)/pRNA-primed packaging (φ29) vs. vertex ATPase packaging without a canonical terminase (PRD1, φ6).
2. **True negatives for calibrating abduction false-discovery rates:**
   - In cellular central metabolism (e.g. *E. coli* or *P. putida* glycolysis), an unsatisfied module step is nearly always a curation or homology gap. In phages, the **temperate latency module** (`GO:0098689` latency-replication decision, `GO:0075713` proviral integration, `GO:0032359` provirus excision) is **biologically absent** in obligately lytic genomes (T4, T7, φX174, MS2, φ29). Running `abduce()` across lytic vs. temperate phages measures the false-gap rate of abductive hole-filling leads.
3. **Multi-functional single genes mapping to multiple modules:**
   - Micro-phages compress multiple module roles into single polypeptides—for example, Qβ maturation protein **`A2`** both mediates pilus attachment/RNA protection (`GO:0039666`) and executes single-gene lysis (`GO:0039640`) by inhibiting host MurA (UDP-GlcNAc enolpyruvyl transferase), while MS2 coat protein **`cp`** is both the icosahedral capsid subunit (`GO:0019030`) and the translational operator repressor of the replicase gene.
4. **Cross-genome helper/satellite satisfiability (`P2` + `P4`):**
   - Satellite phage **P4** (`BPP4`, 13 genes) encodes its own replication and size-determination scaffold (`Sid`, which redirects helper P2 capsid protein `gpN` from $T=7$ to smaller $T=4$ heads) plus polarity suppressor (`Psu`), but lacks head, tail, and lysis structural genes. P4's morphogenetic and release modules are unsatisfiable in `BPP4` alone and become satisfiable only over the composite proteome `BPP4 ∪ BPP2`.
5. **Synteny-constrained resolution of "viral dark matter":**
   - Sequence similarity decays rapidly across phages, leaving 30–70% of ORFs unannotated even in model clades. Because phage genes are tightly ordered into co-directional operons (e.g., *terminase small → terminase large → portal → prohead protease → scaffold → major capsid*, or *holin → endolysin → i-spanin / +1 overlapping o-spanin*), an unsatisfied leaf predicate from `abduce()` points directly to a specific genomic slot.

---

## Candidate Phage Genomes (with Verified UniProt Taxon & Proteome Counts)

To avoid strain/host taxon fragmentation in UniProt (several phages such as λ, Mu, P1, P2, and T5 have multiple taxon IDs across isolates), gene folders should pin the canonical UniProt Taxon IDs and mnemonics listed below. Counts reflect current UniProt proteomes (`Reviewed` = Swiss-Prot curated entries; `Total` = Swiss-Prot + TrEMBL entries, which may include a few variant or fragment records).

### Tier 1: Small Genomes — Tractable 100% End-to-End Curation (4–28 Genes)

| Phage | UniProt Taxon | Mnemonic | Reviewed / Total | Lifestyle & Virion | Role in End-to-End Curation & Module Testing |
|-------|--------------:|----------|-----------------:|--------------------|----------------------------------------------|
| **φX174** (*Sinsheimervirus phiX174*) | `1217068` (also `10847`) | `BPPHS` (`BPPHX`) | **10 / 10** | Lytic ssDNA circular microvirus ($T=1$, tailless, 5.39 kb, 11 genes) | **100% Swiss-Prot reviewed minimal DNA genome:** Overlapping ORFs (`A`, `A*`, `B`, `C`, `D`, `E`, `F`, `G`, `H`, `J`, `K`). Defines rolling-circle ssDNA replication (`gpA`, `GO:0039683`), internal/external scaffolding (`gpB`, `gpD`), DNA pilot tube (`gpH`), and **single-gene lysis via MraY inhibition** (`gpE`, `GO:0039640`). |
| **MS2** (*Emesvirus zinderi*) | `12022` | `BPMS2` | **4 / 33** | Lytic (+)ssRNA levivirus ($T=3$, tailless, 3.57 kb, 4 genes) | **Complete viral lifecycle in 4 proteins:** Maturation/adhesin (`mat`, F-pilus attachment `GO:0039666`), coat/translational repressor (`cp`), single-gene lysis (`lys`/`L` — membrane lesion without PG-biosynthesis inhibition), and RdRp $\beta$-subunit (`rep`, `GO:0003968`, which hijacks host EF-Tu, EF-Ts, and ribosomal S1). |
| **Qβ** (*Qbetavirus qbeta*) | `39803` | `BPQBE` | **4 / 92** | Lytic (+)ssRNA levivirus ($T=3$, 4.22 kb, 4 genes) | **Dual-module single protein (`A2`) + readthrough coat (`A1`):** `A2` serves as both the F-pilus maturation/attachment protein (`GO:0039666`) and the single-gene lysis effector (`GO:0039640`) by inhibiting host MurA. |
| **M13** (*Inovirus M13*) | `1977402` | `BPM13` (`ENTM13` / `ENTPH`) | **9 / 19** | Chronic ssDNA filamentous phage (6.41 kb, ~10–11 genes) | **Non-lytic chronic extrusion (`GO:0099045`):** Already has `gpI` (`P03656`) reviewed in `genes/ENTM13/` and `genes/ENTPH/`. Curating the remaining 9 genes (`gpII`–`gpX`, including F-pilus tip adhesin `gpIII` and outer-membrane secretin `gpIV`) covers the sole non-lytic extrusion branch. |
| **φ6** (*Cystovirus phi6*) | `2928686` (also `10879`) | `BPPH6` | **13 / 13** | Lytic enveloped segmented dsRNA phage (*P. syringae*, 13.4 kb, 13 genes) | **100% reviewed enveloped dsRNA phage:** Exercises `GO:0019031` (*viral envelope*), type IV pilus attachment (`P3`/`P6`), membrane fusion (`P6`), virion peptidoglycan endopeptidase (`P5`), hexameric packaging NTPase (`P4`), and intra-capsid RdRp (`P2`, `GO:0039694`). |
| **PRD1** (*Alphatectivirus PRD1*) | `10658` | `BPPRD` | **25 / 30** | Lytic dsDNA tectivirus with internal lipid membrane (14.9 kb, ~25–30 genes) | **Internal viral membrane (`GO:0039641`) & terminase-independent ATPase packaging:** Structurally related to adenoviruses; uses a lipid vesicle inside the icosahedral capsid that transforms into a tail-like tube for DNA ejection, plus protein-primed replication (`gp8` TP + `gp1` Pol) and vertex packaging ATPase (`gp9`). |
| **φ29** (*Salasvirus phi29*) | `2884424` (also `10756`) | `BPPH2` | **25 / 28** | Lytic Gram-positive podovirus (*B. subtilis*, 19.3 kb, ~25 genes) | **Gram-positive comparator + protein-primed replication:** Pairs with [`BACSU.md`](BACSU.md). Defines protein-primed replication (`gp2` Pol + `gp3` TP), pRNA-assisted packaging motor (`gp16`), and 2-step Gram-positive lysis (holin `gp14` + lysozyme `gp15`, no spanin). |

### Tier 2: Canonical Tailed Phages (`Caudoviricetes`) — Core Module Satisfiability Benchmarks

| Phage | UniProt Taxon | Mnemonic | Reviewed / Total | Lifestyle & Virion | Role in End-to-End Curation & Module Testing |
|-------|--------------:|----------|-----------------:|--------------------|----------------------------------------------|
| **λ (Lambda)** (*Lambdavirus lambda*) | `2681611` (also `10710`) | `LAMBD` | **62 / 67** | Temperate siphovirus (*E. coli*, 48.5 kb, ~70 genes) | **Primary recommended starting genome:** >90% Swiss-Prot reviewed and literature-dense. Populates every core module simultaneously: `cos` 5'-extended packaging (`Nu1`/`A`, `GO:0098037`), head-tail joining (`GO:0098005`), long flexible tail ejection (`gpJ`/`gpH`, `GO:0099001`), canonical holin/endolysin/spanin lysis (`S`/`R`/`Rz`/`Rz1`), proviral integration/excision (`Int`/`Xis`, `GO:0075713`/`GO:0032359`), transcription antitermination (`N`/`Q`, `GO:0031564`), and the `CI`–`Cro`–`CII`–`CIII` latency-replication switch (`GO:0098689`). |
| **T7** (*Teseptimavirus T7*) | `10760` | `BPT7` | **57 / 157** | Obligately lytic podovirus (*E. coli*, 39.9 kb, ~57 genes) | **Lytic tailed contrast to λ:** Short-tail ejection (`GO:0099002`) with internal core proteins (`gp14`/`gp15`/`gp16`), anti-R-M DNA mimic `Ocr` (`gp0.3`, `GO:0099018`), host RNAP shutoff (`gp0.7`, `gp2`, `GO:0039653`), autonomous single-subunit RNAP (`gp1`), minimal 4-protein replisome (`gp5` Pol + host `trxA`, `gp4`, `gp2.5`), and amidase endolysin (`gp3.5`, `GO:0008745`). |
| **P22** (*Lederbergvirus P22*) | `10754` | `BPP22` | **65 / 142** | Temperate podovirus (*S. enterica*, 41.7 kb, ~65 genes) | **Temperate podovirus contrast to λ & T7:** Combines λ-like lysogeny (`c2`, `int`, `xis`, plus antirepressor `Ant` and superinfection exclusion `sieA`/`sieB`) with podovirus morphology, LPS-cleaving tailspike (`gp9`, `GO:0039638`), non-proteolytic scaffold recycling (`gp8`), and headful `pac` packaging (`gp3`/`gp2`, `GO:0098006`). |
| **Mu** (*Muvirus mu*) | `2681603` (also `10677`) | `BPMU` | **56 / 74** | Temperate transposable myovirus (36.7 kb, ~56 genes) | **Transposition-driven replication & integration:** Replaces standard replication/integration with `MuA`/`MuB` transposase (`GO:0004803`), includes the `Gin` invertible G-segment tail-fiber switch (`S`/`U` vs. `S'`/`U'`) and `Mom` DNA carbamoylmethyltransferase (`GO:0099018`). |
| **P2 + Satellite P4** | `2905681` (`P2`) / `10680` (`P4`) | `BPP2` / `BPP4` | **39 / 43** (`P2`) & **13 / 13** (`P4`) | Temperate contractile myovirus + capsid-pirating satellite | **Compact myovirus + cross-genome helper dependency:** P2 (43 genes) is the most compact autonomous myovirus for curating a complete contractile tail/baseplate; P4 (13/13 reviewed) tests **multi-genome satisfiability** where P4's assembly/lysis modules require P2 helper proteins. |
| **Mycobacteriophage L5** (*L5virus L5*) | `31757` | `BPML5` | **84 / 90** | Temperate siphovirus (*Mycobacterium*, 52.3 kb, ~85 genes) | **Non-proteobacterial / mycolata envelope benchmark:** >90% reviewed in Swiss-Prot; tests how the mycolic-acid outer membrane reshapes the entry and lysis modules (requiring both peptidoglycan-cleaving **Lysin A** and mycolylarabinogalactan-cleaving **Lysin B** esterase). |
| **T4** (*Tequatrovirus T4*) | `10665` | `BPT4` | **269 / 288** | Obligately lytic myovirus (*E. coli*, 168.9 kb, ~288 genes) | **Curated in `genes/BPT4/` (46 `COMPLETE`, 3 `DRAFT`):** The richest model myovirus—contractile tail ejection (`GO:0099000`), 28-protein baseplate/tail assembly, dCMP $\to$ 5-hmC $\to$ ghmdC DNA hypermodification, ADP-ribosylation & sigma-factor takeover (`Alt`, `ModA/B`, `AsiA`, `gp55`), and lysis inhibition (`rI`, `GO:0039639`). All 46 Falcon-seeded genes are now `COMPLETE` (`DAM`, `E`, and `frd` remain `DRAFT`), providing full myovirus structural and counter-defense coverage without making all ~288 genes a prerequisite for the module library. |

### Tier 3: Large / Jumbo & Specialized Counter-Defense Phages (Targeted Module Cohorts)

| Phage | UniProt Taxon | Mnemonic | Existing Repo Footprint | Strategic Module Value |
|-------|--------------:|----------|-------------------------|------------------------|
| **Punavirus P1** | `10678` | `BPP1` / `9CAUD` | `darB` (`Q9XJG2`, `DRAFT`) | **Episomal plasmid latency (`GO:0075720`):** `ParA`/`ParB` partition, `Cre-loxP` recombinase, pinholin (`lydA`) + SAR-endolysin (`lyz`), and capsid-injected `DarA`/`DarB` antirestriction. |
| **Bacillus phage phi3T / SPβ** | `10736` | `BPPHT` | `AimP` (`P0DOE2`, `DRAFT`) | **Arbitrium quorum-sensing latency switch (`GO:0098689`):** `AimP` hexapeptide + `AimR` receptor TF + `aimX` non-coding RNA regulator. |
| **Bordetella phage BPP-1** | `2885909` | `BPBPP` | `brt` (`Q775D8`, `DRAFT`) | **Diversity-Generating Retroelement (DGR):** Mutagenic reverse transcription (`brt` + `avd` + `TR`) hypermutating the `mtd` tail-fiber receptor-binding protein. |
| **Anti-CRISPR phages (JBD5, D3112, ZF40, LP-101, SIRV1)** | `1223261`, `2907964`, `1127516`, `1458856`, `157898` | `9CAUD`, `BPD31`, `BPZF4`, `SIRV1` | `acrIF3`, `orf30`, `AcrF8`, `ACA2`, `acrIIA2`, `orf114` (all `COMPLETE`) | **Counter-defense islands (`MODULE:anti_crispr_suppression`):** Benchmarks for `GO:0098672` and `Aca` autoregulatory operons. |
| **Pseudomonas jumbo phages 201φ2-1 & ΦKZ** | `536053`, `169683` | `BPFKZ` | `MODULE:viral_factory` (`chmA` shell) | **Phage nucleus compartmentalization:** Chimallin (`chmA`) protein shell, PhuZ tubulin spindle, and virion/non-virion multisubunit RNAPs. |

---

## Existing Phage & Viral Footprint in the Repository

| Taxon Code | Organism | NCBITaxon | Reviewed (`COMPLETE` / `DRAFT`) | Seeded (`INITIALIZED` w/ Deep Research) | Key Genes & Biology Covered |
|------------|----------|-----------|--------------------------------:|----------------------------------------:|-----------------------------|
| **BPT4** | *Tequatrovirus T4* | `NCBITaxon:10665` | 49 (`46 COMPLETE`, `3 DRAFT`) | 0 | Prior `DRAFT` reviews: <gene species="BPT4" symbol="DAM">DAM</gene> (`P04392`, DNA adenine MTase / R-M evasion `GO:0099018`), <gene species="BPT4" symbol="E">E</gene> (`P00720`, endolysin muramidase `GO:0003796` / cytolytic release `GO:0044659`), <gene species="BPT4" symbol="frd">frd</gene> (`P04382`, DHFR `GO:0004146`). Completed (`COMPLETE`) with Falcon deep research: 28 structural/tail/baseplate/capsid genes (`gp5`, `gp6`–`gp12`, `gp18`–`gp20`, `gp23`, `gp25`–`gp29`, `gp35`–`gp38`, `gp48`, `gp51`, `gp53`, `gp54`, `gp57`, `soc`, `wac`), 10 counter-defense/host-takeover genes (`gp2`, `adfA`, `agt`, `arn`, `bgt`, `stp`, `ndd`, `gp46`, `gp47`, `denA`), and 8 replication/lysis/caution genes (`ac`, `gp41`, `dda`, `uvsW`, `rI`, `t`, `y13J`, `y13K`). See [`SPKW/SPKW-BPT4.md`](SPKW/SPKW-BPT4.md). |
| **9CAUD** | *Caudoviricetes* (JBD5, LP-101, P1, phiNIT1, phiR8-01) | Various | 5 (`3 COMPLETE`, `2 DRAFT`) | 0 | `acrIF3` (`L7P7R7`), `acrIIA2` (`A0A059T5F6`), `darB` (`Q9XJG2`), `dfrP` (`D0VXF2`), `g022` (`I7J3R9`). |
| **BPZF4** | *Pectobacterium phage ZF40* | `NCBITaxon:1127516` | 2 (`COMPLETE`) | 0 | `AcrF8` (`H9C181`) and `ACA2` (`H9C180`). |
| **BPD31** | *Pseudomonas phage D3112* | `NCBITaxon:2907964` | 1 (`COMPLETE`) | 0 | `orf30` (`Q6TM72`, AcrIF2 DNA-mimic anti-CRISPR). |
| **BPBPP** | *Bordetella phage BPP-1* | `NCBITaxon:2885909` | 1 (`DRAFT`) | 0 | `brt` (`Q775D8`, DGR reverse transcriptase). |
| **BPPHT** | *Bacillus phage phi3T* | `NCBITaxon:10736` | 1 (`DRAFT`) | 0 | `AimP` (`P0DOE2`, arbitrium quorum-sensing peptide). |
| **ENTM13** / **ENTPH** | *Inovirus M13* | `NCBITaxon:1977402` | 2 (`COMPLETE`) | 0 | `I` (`P03656`, G1P/G11P assembly/extrusion ATPase). |
| **SIRV1** | *Sulfolobus islandicus rod-shaped virus 1* | `NCBITaxon:157898` | 1 (`COMPLETE`) | 0 | `orf114` (`Q8QL27`, AcrIII-1 $\text{cA}_4$ ring nuclease). |

---

## Module-Route Matrix Across the Core Reference Genomes

Each reference phage takes a specific, testable path through the modular lifecycle. Satisfiability evaluation (`evaluate()`) should verify that each genome satisfies its active variant branch while rejecting alternative branches (and leaving the temperate module unsatisfied in obligately lytic phages):

| Lifecycle Module | **λ** (`LAMBD`) | **T7** (`BPT7`) | **T4** (`BPT4`) | **φX174** (`BPPHS`) | **MS2 / Qβ** (`BPMS2` / `BPQBE`) | **M13** (`BPM13`) | **φ29** (`BPPH2`) | **P2 + P4** (`BPP2` + `BPP4`) |
|------------------|-----------------|-----------------|-----------------|---------------------|----------------------------------|-------------------|-------------------|-------------------------------|
| **1. Attachment (`GO:0019062`)** | `gpJ` $\to$ LamB (`GO:0098670`) | `gp17` $\to$ LPS (`GO:0039638`) | `gp37` (`GO:0098671`) $\to$ `gp12` (`GO:0098670`) | `gpF`/`gpG` $\to$ LPS | `mat` / `A2` $\to$ F-pilus (`GO:0039666`) | `gpIII` $\to$ F-pilus (`GO:0039666`) + TolA | `gp12` $\to$ wall teichoic acid | P2 tail fibers `gpH`/`gpG` |
| **2. Genome Ejection (`GO:0039678`)** | Long flexible tail (`GO:0099001`, `gpH`) | Short tail + internal core (`GO:0099002`, `gp14/15/16`) | Contractile tail + spike lysozyme (`GO:0099000`, `gp18/19/5`) | DNA pilot tube (`gpH`) | Pilus retraction RNA entry (`mat`/`A2`) | Pilus retraction + TolQRA import | Short tail + peptidoglycan hydrolase (`gp13`) | Contractile tail (`GO:0099000`, P2 `FI`/`FII`) |
| **3. Temperate Latency (`GO:0019042`)** | **SATISFIED:** `CI`/`Cro`/`CII`/`CIII` (`GO:0098689`) + `Int`/`Xis` (`GO:0075713`, `GO:0032359`) | *Unsatisfied (True Negative — obligately lytic)* | *Unsatisfied (True Negative — obligately lytic)* | *Unsatisfied (True Negative — obligately lytic)* | *Unsatisfied (True Negative — obligately lytic)* | *Unsatisfied (Chronic persistent episome)* | *Unsatisfied (True Negative — obligately lytic)* | **SATISFIED:** `C`/`Cox` + `Int` |
| **4. Transcription (`GO:0019083`)** | Host RNAP + `N`/`Q` antitermination (`GO:0031564`) | Host RNAP early $\to$ phage RNAP (`gp1`) + host shutoff (`gp2`, `GO:0039653`) | Host RNAP remodeled via `Alt`/`ModA/B`, `MotA`/`AsiA`, `gp55`/`gp33` | Host RNAP | None (ssRNA genome is directly translated) | Host RNAP | Host RNAP + viral TF `gp4` | Host RNAP + P2 `Ogr` / P4 `PSU` antiterminator |
| **5. Genome Replication (`GO:0039693` / `GO:0039694`)** | `O`/`P` recruit host DnaB/Pol III ($\theta \to \sigma$ `GO:0039686` $\to$ `GO:0039683`) + Red (`exo`/`bet`) | Autonomous replisome (`gp5` Pol + host `trxA`, `gp4`, `gp2.5`) | Autonomous replisome + RDR (`gp43`, `gp44/62`, `gp45`, `gp41/61`, `gp32`, `uvsX/Y`) + ghmdC pathway | Rolling-circle (`gpA` nickase + host Pol III/Rep, `GO:0039683`) | Viral RdRp (`rep` + host EF-Tu/EF-Ts/S1, `GO:0039694`) | Rolling-circle (`gpII` nickase + `gpV` SSB + host Pol III, `GO:0039683`) | Protein-primed (`gp2` Pol + `gp3` TP + `gp5`/`gp6`) | Rolling-circle (`gpA` in P2; `α` primase-helicase in P4) |
| **6. Capsid & Packaging (`GO:0019069`, `GO:0019073`)** | `cos` 5' packaging (`Nu1`/`A`, `GO:0098037`), `gpB` portal, `gpC` protease, `gpE` coat, `gpD` decoration | Headful/concatemer packaging (`gp18`/`gp19`), `gp8` portal, `gp9` scaffold, `gp10` coat | Headful packaging (`gp16`/`gp17`, `GO:0098006`), `gp20` portal, `gp21` protease, `gp22` scaffold, `gp23` coat, `Hoc`/`Soc` | `gpB`/`gpD` scaffolds, `gpF` coat, `gpG` spike, `gpJ` DNA-condensing protein | Co-replicative RNA encapsidation by `cp` coat dimers (`GO:0019030`) | Coupled membrane assembly/coat replacement (`gpV` $\to$ `gpVIII`/`gpIII`/`gpVI`/`gpVII`/`gpIX`) | `gp7` scaffold, `gp8` coat, `gp10` portal + `gp16` ATPase/pRNA motor | **P4 pirates P2 `gpN`/`gpO`/`gpQ`** via P4 `Sid` external scaffold ($T=7 \to T=4$) |
| **7. Virion Release (`GO:0019076`)** | **3-step cytolysis (`GO:0044659`):** Holin `S` (`GO:0044660`) + endolysin `R` + spanin `Rz`/`Rz1` | **3-step cytolysis (`GO:0044659`):** Holin `gp17.5` + amidase `gp3.5` (`GO:0008745`) + spanin `gp18.5`/`gp18.7` | **3-step cytolysis + LIN:** Holin `t` + lysozyme `E` (`GO:0003796`) + spanin `pseT.3`/`pseT.2` + LIN `rI` (`GO:0039639`) | **Single-gene lysis (`GO:0039640`):** `E` inhibits host MraY | **Single-gene lysis:** Qβ `A2` inhibits MurA (`GO:0039640`); MS2 `L` membrane pore | **Non-lytic extrusion (`GO:0099045`):** `gpI`/`gpXI` IM ATPase + `gpIV` OM secretin | **2-step Gram+ cytolysis:** Holin `gp14` + lysozyme `gp15` (no spanin) | P2 holin `Y` + endolysin `K` + `LysA`/`LysB`/`LysC` |

---

## Reference Phage GO Term Catalog (Verified Against Current OLS)

Every GO ID and label below has been verified against the current Gene Ontology in OLS (none obsolete). Curators and automated module definitions should draw from this vocabulary rather than generic roots (`GO:0016032 viral process`, `GO:0019058 viral life cycle`, `GO:0044423 virion component`) or eukaryote-centric immune terms (`GO:0052170`, `GO:0042742`).

### 1. Lifecycle — Biological Process (`BP`)

#### Adsorption and Entry
| Stage | GO Term | Typical Phage Examples |
|-------|---------|------------------------|
| Attachment (general) | `GO:0019062` virion attachment to host cell | All phages (use when receptor class is unknown) |
| Reversible binding | `GO:0098671` adhesion receptor-mediated virion attachment to host cell | T4 long tail fibers (`gp37`) binding LPS or OmpC |
| Irreversible binding | `GO:0098670` entry receptor-mediated virion attachment to host cell | λ `gpJ` binding LamB; T5 binding FhuA; T4 short tail fibers (`gp12`) |
| To lipopolysaccharide | `GO:0039638` lipopolysaccharide-mediated virion attachment to host cell | P22 tailspike (`gp9`), T7 tail fiber (`gp17`) |
| To pilus | `GO:0039666` virion attachment to host cell pilus | M13 `pIII` on F-pilus; MS2 `mat` / Qβ `A2` on F-pilus; φ6 `P3` on type IV pilus |
| To flagellum | `GO:0098931` virion attachment to host cell flagellum | Flagellotropic phage χ (chi) |
| Entry (general) | `GO:0046718` symbiont entry into host cell | General parent (prefer specific ejection/disruption child when known) |
| Genome ejection (parent) | `GO:0039678` symbiont genome ejection through host cell envelope | General ejection across bacterial envelope |
| — Contractile tail | `GO:0099000` symbiont genome ejection through host cell envelope, contractile tail mechanism | T4 (`gp18`/`gp19`/`gp5`), P2, Mu (myoviruses) |
| — Long flexible tail | `GO:0099001` symbiont genome ejection through host cell envelope, long flexible tail mechanism | λ (`gpH`/`gpJ`), T5, L5 (siphoviruses) |
| — Short tail | `GO:0099002` symbiont genome ejection through host cell envelope, short tail mechanism | T7 (`gp14`/`gp15`/`gp16`), P22, φ29 (podoviruses) |
| Cell wall degradation during entry | `GO:0098932` symbiont entry into host cell via disruption of host cell wall peptidoglycan | T4 baseplate central spike lysozyme (`gp5`); T7 internal core (`gp16`); φ6 `P5` |
| Inner membrane crossing | `GO:0099008` symbiont entry into host cell via permeabilization of inner membrane | Ejectosome / pilot-protein inner-membrane channels |

#### Host Takeover and Counter-Defence
- `GO:0019080` viral gene expression; `GO:0019083` viral transcription
- `GO:0031564` transcription antitermination (λ `N` and `Q`, P4 `Psu`)
- `GO:0039653` symbiont-mediated suppression of host transcription (T7 `gp2`, T4 `Alc`)
- `GO:0099015` degradation of host chromosome by virus (T4 `denA`, `denB`, `gp46`/`gp47`)
- `GO:0098673` symbiont-mediated suppression of host DNA replication (T4 `ndd`)
- `GO:0099018` symbiont-mediated evasion of host restriction-modification system (T7 `Ocr`, P1 `DarB`, T4 `DAM` / `agt` / `bgt` / `arn` / `stp`, Mu `Mom`)
- `GO:0099016` symbiont-mediated evasion of DNA end degradation by host (T4 `gp2`, λ `Gam`, T7 `gp5.9`)
- `GO:0098672` symbiont-mediated suppression of host CRISPR-cas system (`AcrIF2`/`orf30`, `AcrIF3`, `AcrIF8`, `AcrIIA2`, `AcrIII-1`/`orf114`)
- `GO:0098669` superinfection exclusion (T4 `Imm`/`Sp`, P22 `SieA`/`SieB`)

#### Genome Replication
- `GO:0039693` viral DNA genome replication
  - `GO:0039686` bidirectional double-stranded viral DNA replication (λ early $\theta$ replication)
  - `GO:0039683` rolling circle double-stranded viral DNA replication (λ late $\sigma$ replication, φX174 `gpA`, M13 `gpII`, P2 `gpA`)
- `GO:0039694` viral RNA genome replication (MS2/Qβ `rep`, φ6 `P2`)

#### Assembly and Packaging
- `GO:0019068` virion assembly
- `GO:0019069` viral capsid assembly $\to$ `GO:0046797` viral procapsid maturation
- `GO:0019082` viral protein processing (prohead maturation protease, e.g. T4 `gp21`, λ `gpC`)
- `GO:0019073` viral DNA genome packaging, with mechanism-specific children:
  - `GO:0098006` viral DNA genome packaging, headful (T4 `gp16`/`gp17`, P22 `gp3`/`gp2`, P1 `pacA`/`pacB`)
  - `GO:0098037` viral DNA genome packaging, 5' extended cos packaging (λ `Nu1`/`A`, P2 `M`/`P`)
  - `GO:0098036` viral DNA genome packaging, 3' extended cos packaging
  - `GO:0098035` viral DNA genome packaging via site-specific sequence recognition
- `GO:0098005` viral head-tail joining (λ `gpW`/`gpFII`, T4 `gp13`/`gp14`/`gp15`)
- `GO:0098003` viral tail assembly; `GO:0098004` virus tail fiber assembly (T4 `gp38`, `gp57A`)

#### Virion Release and Lysis
| Mode | GO Term | Typical Phage Examples |
|------|---------|------------------------|
| General | `GO:0019076` viral release from host cell | Root release term |
| Lysis (dsDNA phages) | `GO:0044659` viral release from host cell by cytolysis | λ (`R`/`S`/`Rz`/`Rz1`), T4 (`E`/`t`), T7 (`gp3.5`/`gp17.5`), φ29 (`gp15`) |
| Holin pore formation | `GO:0044660` viral release via pore formation in host cell membrane | λ `S`, T4 `t`, T7 `gp17.5`, φ29 `gp14` |
| Single-gene lysis (PG synthesis inhibition) | `GO:0039640` viral release via suppression of host peptidoglycan biosynthetic process | φX174 `E` (inhibits MraY), Qβ `A2` (inhibits MurA). *(Note: Not MS2 `L`, which lyses without inhibiting PG synthesis.)* |
| Lysis inhibition (LIN) | `GO:0039639` suppression by virus of host cell lysis in response to superinfection | T4 `rI`, `rIII` |
| Non-lytic extrusion | `GO:0099045` viral extrusion | M13 (`gpI`/`gpIV`) and other filamentous inoviruses |

#### Temperate Decisions (Lysogeny / Viral Latency)
- `GO:0098689` latency-replication decision (λ `CI`, `Cro`, `CII`, `CIII`; arbitrium `AimP`/`AimR`/`AimX` in phi3T/SPβ)
- `GO:0019042` viral latency $\to$ `GO:0019043` establishment of viral latency
  - `GO:0075713` establishment of integrated proviral latency (λ `Int`, P22 `Int`, L5 `Int`)
  - `GO:0075720` establishment of episomal latency (P1 plasmid prophage; N15 $\to$ `GO:0075530` establishment of latency as a linear episome)
- `GO:0019044` maintenance of viral latency (λ `CI`, P1 `ParA`/`ParB` + `C1`)
- `GO:0019046` release from viral latency (prophage induction)
- `GO:0032359` provirus excision (λ `Xis`/`Int`)
- `GO:0015074` DNA integration

### 2. Cellular Components (`CC`)

| Structure | GO Terms |
|-----------|----------|
| Root | `GO:0044423` virion component *(avoid as final core term when a specific substructure term below applies)* |
| Head / Capsid | `GO:0019028` viral capsid; `GO:0019030` icosahedral viral capsid; `GO:0039621` T=13 icosahedral viral capsid (T4 `gp23`) |
| Decoration proteins | `GO:0098021` viral capsid, decoration (λ `gpD`, T4 `Hoc`/`Soc`) |
| Precursor head | `GO:0046729` viral procapsid; `GO:0046806` viral scaffold (T4 `gp22`, P22 `gp8`, φ29 `gp7`) |
| Portal | `GO:0046798` viral portal complex (T4 `gp20`, λ `gpB`, T7 `gp8`, φ29 `gp10`) |
| Packaging motor | `GO:0043493` viral terminase complex; `GO:0098009` viral terminase, large subunit; `GO:0097710` viral terminase, small subunit |
| Tail & Substructures | `GO:0098015` virus tail · `GO:0098026` virus tail, tube · `GO:0098027` virus tail, sheath · `GO:0098025` virus tail, baseplate · `GO:0098024` virus tail, fiber · `GO:0098023` virus tail, tip (λ `gpJ`) |
| Viral Membranes | `GO:0019031` viral envelope (φ6); `GO:0039641` viral inner membrane (PRD1); `GO:0055036` virion membrane |
| Host Subcellular Locations | `GO:0020002` host cell plasma membrane (holins, M13 `gpI` assembly complex); `GO:0044229` host cell periplasmic space (spanins, active endolysins); `GO:0039662` host cell outer membrane (`Rz1` o-spanin, M13 `gpIV` secretin); `GO:0030430` host cell cytoplasm |

### 3. High-Frequency Molecular Functions (`MF`)
- `GO:0039660` **structural constituent of virion** — Use this as the core `molecular_function` for major/minor capsid, tail tube, tail sheath, baseplate wedge, and portal structural subunits in place of generic `GO:0005515 protein binding`.
- **Endolysins & virion muralytic enzymes:** `GO:0003796` lysozyme activity (T4 `E`, T4 `gp5`, φ29 `gp15`); `GO:0008745` N-acetylmuramoyl-L-alanine amidase activity (T7 `gp3.5`); lytic transglycosylase activity (λ `R`).
- **Holins:** `GO:0140911` pore-forming activity (paired with `BP` `GO:0044660`).
- **Integrases & Recombinases:** `GO:0008979` prophage integrase activity; `GO:0009009` site-specific recombinase activity (λ `Int`, P1 `Cre`, Mu `Gin`); `GO:0004803` transposase activity (Mu `MuA`).
- **Packaging motors:** `GO:0015616` DNA translocase activity (terminase large subunits `A`, `gp17`, `gp19`, and φ29 `gp16`).
- **RNA phage replicase:** `GO:0003968` RNA-directed RNA polymerase activity (MS2/Qβ `rep`, φ6 `P2`).

### 4. Known Ontology Gaps (`proposed_new_terms` Targets)
- **No specific MF or BP terms for "spanin" (inner/outer membrane fusion during lysis), "holin", or "endolysin":**
  - Holins are currently captured by combining `GO:0140911 pore-forming activity` + `GO:0044660 viral release via pore formation in host cell membrane`.
  - **Spanins** (two-component periplasmic coiled-coil/lipoprotein complexes like λ `Rz`/`Rz1` and T7 `gp18.5`/`gp18.7`, or unimolecular `T1 gp11`, which fuse the host inner and outer membranes after peptidoglycan degradation) lack any specific MF or BP term. Proposing a new term for **spanin-mediated host outer membrane disruption / inner-outer membrane fusion involved in viral release** is a high-priority ontology contribution.
- **No GO labels containing "lysogeny" or "prophage induction" as primary names:** GO uses the pan-viral `latency` hierarchy (`GO:0019042`–`GO:0019046`, `GO:0098689`); reviews should use these IDs while noting bacteriophage lysogeny synonyms in prose.
- **No phage-specific terms for sigma-factor appropriation / remodeling:** T4 `AsiA` (anti-$\sigma^{70}$ / co-activator) and `gp55` (late $\sigma$ factor tethered to the `gp45` sliding DNA clamp) rely on generic transcription regulation/initiation terms.
- **Phage nucleus & barrier-mediated CRISPR evasion:** Documented in [`modules/viral_factory.yaml`](../modules/viral_factory.yaml) (`phage nucleus` under `CC`, and `symbiont-mediated evasion of host CRISPR-cas system` under `BP` for physical/chemical shielding distinct from direct `GO:0098672` inhibitor binding).

---

## Synteny & Domain Rules for Resolving Phage Pathway Holes

When `abduce()` flags an unsatisfied step in a phage module (and the step is not excluded by a lytic/morphotype variant or fulfilled by a host protein), curators can locate the missing gene in the phage genome using conserved **operon synteny** and **biophysical/structural signatures**:

| Missing Module Step (Abduction Lead) | Expected Syntenic Slot | Structural / Biophysical Resolution Signature |
|--------------------------------------|------------------------|-----------------------------------------------|
| **Outer-membrane o-spanin (`Rz1`)** | Embedded in the **+1 reading frame** of `i-spanin` (`Rz`), overlapping its 3' end, or immediately adjacent downstream of `endolysin` | Small (40–70 aa) proline-rich polypeptide with an N-terminal Signal Peptidase II **lipobox** (`[LVI][ASTVI][GAS]C`); routinely missed by ORF callers and absent from many UniProt proteomes. |
| **Inner-membrane i-spanin (`Rz`) or u-spanin (`gp11`)** | Immediately downstream of `endolysin` (`R`) | `i-spanin`: N-terminal transmembrane helix (TMD) + periplasmic $\alpha$-helical coiled-coil. `u-spanin`: N-terminal OM lipobox + periplasmic domain + C-terminal IM TMD. |
| **Holin / Pinholin (`S`, `t`, `gp17.5`)** | Immediately upstream of (or adjacent to) `endolysin` | Small (60–150 aa) protein with 1–4 TMDs and a hydrophilic, positively charged C-terminal cytoplasmic tail (>50 sequence-unrelated families). |
| **Small terminase subunit (`terS`, `Nu1`, `gp16`)** | Immediately upstream of `terL` (large terminase `GO:0098009`) | 15–25 kDa oligomer (8–12-mer ring) with an N-terminal HTH/winged-HTH DNA-binding domain and central coiled-coil oligomerization bundle. |
| **Prohead scaffold (`gp22`, `gp8`, `gp7`)** | Between `portal`/`prohead_protease` and `major_capsid` (or fused as an N-terminal $\Delta$-domain on the major capsid protein, as in HK97) | Charged, $\alpha$-helical coiled-coil / intrinsically disordered protein (20–35 kDa). |
| **Head-tail neck adaptors (`gpW`/`gpFII`, `gp13`/`gp14`)** | Immediately downstream of `major_capsid` | Small (10–20 kDa) dodecameric/hexameric rings identifiable via AlphaFold/Foldseek ([`STRUCTURAL_REASONING.md`](STRUCTURAL_REASONING.md)) even below 15% sequence identity. |
| **Tail assembly frameshift chaperone (`gpG`/`gpGT`)** | Between `major_tail_protein` (`gpV`) and `tape_measure_protein` (`gpH`) in siphoviruses and myoviruses | Overlapping $-1$ programmed ribosomal frameshift cassette producing a shorter (`gpG`) and longer (`gpGT`) isoform at ~30:1 stoichiometry. |
| **Prophage excisionase (`xis`)** | Immediately adjacent to prophage integrase (`int`) | Tiny (50–90 aa) basic winged-HTH DNA architectural protein required for `GO:0032359` provirus excision. |
| **dCTPase/dUTPase sanitation enzyme (T4 `gp56`)** | Co-inherited in phages encoding a pyrimidine hydroxymethylase (T4 `gp42` dCMP HMase or SPO1 dUMP HMase) or PurZ | Pyrophosphohydrolase that purges canonical dCTP/dTTP/dATP so the viral polymerase incorporates only the modified nucleotide. |

---

## Concrete Execution Plan (5-Genome Core Reference Set $\approx$ 160 Genes)

Rather than attempting all ~288 genes of T4 upfront, we can cover **every branch of every phage lifecycle module** in roughly **160 genes across 5 core reference genomes** (plus targeted completion of the already-seeded T4 and specialty phage genes):

### Step 1: Start with Phage λ (`LAMBD`, Taxon `2681611` — 62/67 Reviewed)
- **Why first:** At ~67 proteins (93% Swiss-Prot reviewed) and the highest literature density per gene in virology, complete end-to-end curation of λ is achievable in a few focused batches and immediately populates **all five core lifecycle modules** (`phage_attachment_and_genome_ejection`, `phage_genome_replication_and_transcription`, `phage_temperate_latency_switch`, `phage_capsid_packaging_and_tail_assembly`, and `phage_virion_release_and_lysis`).
- **Action:** Verify `just fetch-gene LAMBD <gene>` (or taxon `2681611`) pipeline handling, partition the ~67 genes into 4 operon batches (*immunity & latency switch*, *early recombination & replication*, *head & tail morphogenesis*, *lysis & accessory b2/nin regions*), and draft the core YAML modules.

### Step 2: Add Micro-Genomes φX174 (`BPPHS`, 10/10), MS2 (`BPMS2`, 4/33), and Qβ (`BPQBE`, 4/92)
- **Why second:** Only **18 reviewed proteins total** across all three phages.
- **Module payoff:** Adds the two non-canonical single-gene lysis branches (`GO:0039640` MraY/MurA inhibition in φX174 `E` and Qβ `A2`, plus MS2 `L`), rolling-circle ssDNA replication (`GO:0039683`), ssRNA replication (`GO:0039694`), F-pilus attachment (`GO:0039666`), dual-module gene assignment (`Qβ A2`), and the first **obligately lytic true negatives** for the temperate latency module.

### Step 3: Curate Phage T7 (`BPT7`, Taxon `10760` — 57/157 Reviewed)
- **Why third:** The ~57 Swiss-Prot reviewed genes of T7 provide the **obligately lytic tailed contrast to λ**: short-tail podovirus ejection (`GO:0099002`), autonomous single-subunit RNAP (`gp1`), host transcription shutoff (`gp2`, `GO:0039653`), `Ocr` anti-restriction DNA mimicry (`GO:0099018`), self-contained 4-protein DNA replisome, and an amidase endolysin (`gp3.5`, `GO:0008745`).

### Step 4: Opportunistically Complete the 46 Seeded T4 Genes (`BPT4`, Taxon `10665` — 269/288 Reviewed)
- **Why fourth:** 49 T4 genes are in `genes/BPT4/` (46 now `COMPLETE` with UniProt, GOA, and Falcon deep-research reports, plus 3 prior `DRAFT` reviews: `DAM`, `E`, `frd`).
- **Module payoff:** These 46 completed reviews give immediate coverage of the **contractile myovirus tail/baseplate branch** (`GO:0099000`, `GO:0098025`, `GO:0098027`), **hmC glucosylation & R-M/CRISPR evasion** (`DAM`, `agt`, `bgt`, `arn`, `stp`), **DNA-end protection** (`gp2`, `GO:0099016`), and **lysis inhibition** (`rI`, `GO:0039639`) without blocking on the remaining ~240 T4 genes.

### Step 5: Expand to Morphotype & Envelope Outliers (`BPM13`, `BPPH6`, `BPPRD`, `BPPH2`, `BPP2`/`BPP4`, `BPML5`)
- **M13 (`BPM13` / `ENTM13`, 9 remaining genes):** Completes the filamentous chronic extrusion branch (`GO:0099045`).
- **φ6 (`BPPH6`, 13/13 reviewed) & PRD1 (`BPPRD`, 25/30 reviewed):** Covers viral envelopes (`GO:0019031`), internal viral membranes (`GO:0039641`), and terminase-independent packaging ATPases.
- **φ29 (`BPPH2`, 25/28 reviewed) & Mycobacteriophage L5 (`BPML5`, 84/90 reviewed):** Covers Gram-positive 2-step lysis, protein-primed DNA replication, and mycolate-envelope (`Lysin A + Lysin B`) lysis.
- **P2 (`BPP2`, 39/43) + Satellite P4 (`BPP4`, 13/13):** Tests cross-genome helper/satellite satisfiability in `src/ai_gene_review/module_logic.py`.

---

## Related Projects & Modules

- [`SPKW/SPKW-BPT4.md`](SPKW/SPKW-BPT4.md) & [`SPKW/SPKW-VIRUS.md`](SPKW/SPKW-VIRUS.md) — ViralZone-primary vs. non-ViralZone Swiss-Prot keyword analysis in phage T4 and viruses.
- [`PATHWAY_SATISFIABILITY.md`](PATHWAY_SATISFIABILITY.md) & [`PATHWAY_SATISFIABILITY/background.md`](PATHWAY_SATISFIABILITY/background.md) — Boolean satisfiability (`evaluate`) and abductive pathway hole filling (`abduce`) in `src/ai_gene_review/module_logic.py`.
- [`CRISPR_ANTI_CRISPR.md`](CRISPR_ANTI_CRISPR.md) & [`ANTI_CRISPR.md`](ANTI_CRISPR.md) — Mechanistic curation of phage anti-CRISPR proteins (`acrIF3`, `acrIIA2`, `AcrF8`, `ACA2`, `orf30`, `orf114`) and [`modules/anti_crispr_suppression.yaml`](../modules/anti_crispr_suppression.yaml).
- [`PROKARYOTIC_IMMUNITY_TERM_PREDICTION.md`](PROKARYOTIC_IMMUNITY_TERM_PREDICTION.md) — Ontology gap analysis for prokaryotic defense and phage counter-defense systems.
- [`modules/viral_factory.yaml`](../modules/viral_factory.yaml) — Viral replication compartments, including the *Chimalliviridae* (`201φ2-1` / `ΦKZ`) `chmA` phage nucleus.
- [`P_PUTIDA/P_PUTIDA_MODULE_PLAN.md`](P_PUTIDA/P_PUTIDA_MODULE_PLAN.md) — Template for lightweight whole-proteome metadata partitioning and module-first batch curation.
- [`modules/phage_attachment_and_genome_ejection.yaml`](../modules/phage_attachment_and_genome_ejection.yaml) — Bacteriophage host receptor recognition and envelope genome ejection mechanisms.
- [`modules/phage_genome_replication_and_transcription.yaml`](../modules/phage_genome_replication_and_transcription.yaml) — Bacteriophage genome replication, transcriptional takeover, and anti-restriction/counter-defense.
- [`modules/phage_temperate_latency_switch.yaml`](../modules/phage_temperate_latency_switch.yaml) — Temperate phage lysis-lysogeny decision, prophage integration/excision, and episomal latency.
- [`modules/phage_capsid_packaging_and_tail_assembly.yaml`](../modules/phage_capsid_packaging_and_tail_assembly.yaml) — Bacteriophage procapsid morphogenesis, genome packaging motors, and tail assembly.
- [`modules/phage_virion_release_and_lysis.yaml`](../modules/phage_virion_release_and_lysis.yaml) — Bacteriophage host lysis (holin-endolysin-spanin, single-gene lysis) and chronic filamentous extrusion.
