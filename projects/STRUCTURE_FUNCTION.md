# Structure-Based Function Prediction for Gene Review

How can protein structure help with function prediction, especially for distant homologs where sequence-based HMMs fail?

## The Problem

HMMs (Pfam, InterPro) encode structural constraints implicitly -- conserved positions reflect buried residues, active sites, and structural contacts. But they fail in the twilight zone (<20-30% sequence identity) where structural similarity persists but sequence signals are washed out.

This project explores what we gain by using structure explicitly -- at multiple granularity levels.

## Three Levels Where Structure Helps

### Level 1: Global Fold (SCOP/CATH/ECOD)

Fold-level match tells you the structural scaffold but is necessary-not-sufficient for function.

- **TIM barrel**: ~10% of all enzymes, 57 families, 5/6 EC classes, 34+ reactions
- **Rossmann folds**: diverse NAD/FAD/nucleotide binding with different substrates
- **Ig-like folds**: binding, signaling, enzymatic functions

**What's new (2024-2026):**
- ECOD now integrates AlphaFold structures -- 1.8M domains classified (NAR 2025)
- CATH-eMMA uses Foldseek distances for automated classification

**For gene review**: Useful as "what kind of protein is this?" but insufficient for GO annotation alone. Function transfer is reliable only at superfamily level (CATH H-level, ECOD H-group).

### Level 2: Local Structural Motifs (Highest Value)

This is where structure gives you something sequence often cannot:

**M-CSA + EnzyMM** (EBI, December 2025):
- 6,870 catalytic site templates
- Searches PDB, AlphaFoldDB, or user-uploaded structures
- Detects known catalytic motifs by geometric similarity
- Web: https://www.ebi.ac.uk/thornton-srv/m-csa/

**PARSE** (PNAS 2025):
- Embeds local structural environments (COLLAPSE embeddings), then enrichment analysis
- F1 >= 85% for catalytic function, with residue-level attribution
- Works with only one known example -- no large training set needed
- Applied to the dark proteome; discovered novel bacterial metalloproteases
- Code: https://github.com/awfderry/PARSE

**Key insight**: A shared catalytic motif provides much stronger evidence for shared function than overall fold similarity. Local geometry is the true functional determinant, not the global fold.

### Level 3: Learned Structural Representations (pLMs + GNNs)

The revolution is the **3Di structural alphabet** (Foldseek) and models built on it:

| Model | Approach | Key advantage |
|-------|----------|---------------|
| **SaProt** (650M/1.3B) | Interleaves AA + 3Di tokens | Best structure-aware pLM; HuggingFace |
| **ProstT5** | Translates AA <-> 3Di bidirectionally | 3Di from sequence in seconds (~3600x faster than AlphaFold) |
| **ESM3** (98B) | Joint sequence + structure + function tracks | Function tokens encode InterPro/GO |
| **DPFunc** | Domain-guided GNN + ESM-2 | Best structure-based GO predictor (Nat Comm 2025) |
| **DeepGO-SE** | ESM-2 into GO axiom space | Neuro-symbolic; zero-shot; fast (Nat Mach Intell 2024) |
| **DeepFRI** | GCN on contact map | Residue-level grad-CAM attribution |

## Practical Tool Landscape

### Structural Search

| Tool | Input | Speed | What you get |
|------|-------|-------|-------------|
| **Foldseek** | 3D structure or 3Di | Seconds | Structural neighbors + E-values |
| **ProstT5** | Sequence only | Seconds | 3Di strings for Foldseek input |
| **Dali/TM-align** | 3D coordinates | Hours | Gold-standard structural alignment |

Foldseek: 4-5 orders of magnitude faster than Dali/TM-align, 86-133% sensitivity.
Foldseek Clusters: 2.3M clusters from 214M AlphaFold structures; 31% of clusters unannotated.

### GO Term Prediction from Structure

| Tool | Publication | Code | Notes |
|------|------------|------|-------|
| **DPFunc** | Nat Comm 2025 | github.com/CSUBioGroup/DPFunc | Best current; domain-guided |
| **DeepGO-SE** | Nat Mach Intell 2024 | github.com/bio-ontology-research-group/deepgo2 | Sequence-only; ontology-aware |
| **TransFun** | Bioinformatics 2023 | github.com/jianlin-cheng/TransFun | Equivariant GNN + ESM |
| **DeepFRI** | Nat Comm 2021 | github.com/flatironinstitute/DeepFRI | Older but residue-level maps |
| **NetGO 3.0** | 2025 | web server | Ensemble method |

### Catalytic Site Detection

| Tool | Approach | Status |
|------|----------|--------|
| **EnzyMM** (M-CSA) | Geometric search of 6,870 templates | Web tool (Dec 2025) |
| **PARSE** | Local structural embeddings + enrichment | GitHub (PNAS 2025) |
| **PROSITE** | Patterns/profiles with 3D annotations | Maintained |

## The Fold-Function Problem

Three hard cases where no single method works:

1. **Same fold, different function** (TIM barrel, Rossmann, Ig-like) -- global match uninformative; need local motif analysis
2. **Different fold, same function** (convergent evolution: serine proteases via chymotrypsin vs subtilisin vs alpha/beta hydrolase) -- structural search misses these
3. **Fold switching** (same sequence, different structures) -- AlphaFold cannot predict; active research area

**Hierarchy of evidence for function transfer by similarity:**
- Sequence identity >40%: generally safe
- 30-40%: likely but verify with domain/motif analysis
- 20-30%: structure-based methods essential
- <20%: structure + local motif detection; expect divergence

## Integration into Gene Review Pipeline

### Recommended workflow for twilight-zone proteins:

1. Get AlphaFold structure (AFDB or ColabFold)
2. Run Foldseek against PDB + AFDB clusters
3. Run EnzyMM/PARSE for catalytic motif detection
4. Run DPFunc or DeepGO-SE for ML-based GO prediction
5. Check ECOD classification for evolutionary context

### Implementation priorities (effort vs. value):

**Low effort, high value:**
- Foldseek web search (search.foldseek.com) -- structural neighbors in seconds
- EnzyMM (M-CSA web tool) -- catalytic motif detection
- DeepGO-SE -- pip-installable, sequence-only input

**Medium effort, high value:**
- ProstT5 -> Foldseek pipeline -- fully automatable
- DPFunc -- best GO predictor using structure
- PARSE -- local motif analysis with residue attribution

## Prototype: `scripts/structural_search.py`

See `projects/quantum-sensing-bioinformatics/` and REE project for test cases.

## Demonstrator Use Cases

### Case 1: lanmodulin (lanM) — Misleading domain annotation [PRIORITY]

**UniProt**: C5B164 (Methylorubrum extorquens AM1)
**The problem**: InterPro detects EF-hand motifs → IEA annotates as "calcium ion binding" (GO:0005509). But lanM has 100-million-fold selectivity for lanthanides over calcium. The EF-hand has unusual proline residues that create a lanthanide-selective coordination geometry visible only in the structure.
**What structure reveals**: The proline substitutions distort the canonical EF-hand loop, creating a larger coordination sphere that preferentially accommodates the larger ionic radii of Ln(III) over Ca(II). This is invisible to sequence-based HMMs which just see "EF-hand."
**Demonstrator value**: Poster child for "HMM says one thing, structure says another."
**Status**: Already reviewed in `genes/METEA/lanM/`; annotation flagged as KEEP_AS_NON_CORE.

### Case 2: Cryptochrome vs Photolyase — Same fold, different function

**Proteins**: dCRY (O77059), hCRY1 (Q16526), hCRY2 (Q49AN0), AtCRY1 (Q43125)
**The problem**: Cryptochromes and photolyases share the same fold (photolyase/cryptochrome superfamily). Photolyases repair UV-damaged DNA; cryptochromes sense light and possibly magnetic fields. Global structural search returns photolyases as top hits, but the function is completely different.
**What structure reveals**: Differences in the FAD-binding pocket geometry, antenna chromophore binding, and C-terminal tail distinguish sensory from repair function. Local motif analysis should distinguish them.
**Demonstrator value**: Classic fold-function problem. Tests whether local motif methods outperform global fold matching.
**Status**: PDB structures available; data in `projects/quantum-sensing-bioinformatics/`.

### Case 3: Novel EF-hands from NMDC metagenomes — Dark proteome

**The problem**: Environmental metagenomes from REE-rich sites may contain novel EF-hand proteins. Are they calcium-binding or lanthanide-binding? Sequence HMMs can't distinguish.
**What structure could reveal**: Coordination geometry of the EF-hand loop — canonical (Ca-selective) vs distorted (Ln-selective).
**Demonstrator value**: Can structure predict function for uncharacterized environmental proteins?
**Status**: Can search NMDC using PF00036/PF13499 (EF-hand domains) filtered to lanthanide-relevant environments.

### Case 4: mll cluster lesser genes — Function from structural context

**Proteins**: mllF (C5B1I7), mllG (C5B1I8), mllH (C5B1I9)
**The problem**: These are annotated by HMMs as generic xylose isomerase-like, aldolase, and N-acetyltransferase respectively. But they function in methylolanthanin (lanthanophore) biosynthesis. Can structural search find more specific functional analogs?
**Demonstrator value**: Tests whether Foldseek finds metallophore/siderophore biosynthetic homologs that sequence methods miss.
**Status**: Reviews exist in `genes/METEA/mll*/`; all have sparse (1-4) IEA annotations.

## Worked Example: Lanmodulin (lanM) — Honest Assessment of Structural Methods

### The annotation problem

InterPro analysis of lanM (C5B164, 133 aa) detects:
- **PF13202** (EF-hand_5) x3
- **IPR002048** (EF-hand domain)
- **IPR018247** (EF-Hand 1, calcium-binding site)
- **IPR011992** (EF-hand domain pair)
- Gene3D classification: **1.10.238.10** (EF-hand superfamily)

Every classification says **calcium**. The IEA annotation is GO:0005509 "calcium ion binding." But lanM has 10^8-fold selectivity for lanthanides over calcium.

### What would structure-based tools actually tell us?

**Honest answer: not much beyond what InterPro already says.**

- **AlphaFold** (AF-C5B164-F1, pLDDT 83.94): Predicts the apo form. Would confirm "EF-hand fold" — the same conclusion as InterPro. AlphaFold does not predict metal specificity.
- **Foldseek**: Would return calmodulin, troponin C, S100 proteins as top hits. Correct fold, wrong function. Global structural similarity provides no information about metal selectivity.
- **PARSE/EnzyMM**: Designed to detect catalytic motifs, not metal-binding specificity. Would detect metal-binding loops but has no template for distinguishing Ca2+ vs Ln3+ selectivity.
- **DPFunc/DeepGO-SE**: Would predict GO:0005509 "calcium ion binding" — trained on existing annotations, which are all calcium for EF-hands.

**The key structural features** — conserved prolines (P36, P60, P85, P109) that distort EF-hand loop geometry to create a larger coordination sphere matching Ln3+ ionic radii — are known only from experimental structures solved with lanthanide ions (8FNS with Nd3+ at 1.01 A, PMID:37259003; 6MI5 with Y3+ NMR, PMID:30352145) and mutagenesis (P→A restores Ca2+ preference, PMID:30351021). No current computational tool would predict this from structure alone.

### Why lanM illustrates the limits, not the promise

| Approach | What it would conclude | Correct? |
|----------|----------------------|----------|
| **HMM/InterPro** | "calcium ion binding" | Misleading |
| **AlphaFold + Foldseek** | "EF-hand protein, similar to calmodulin" | Same as InterPro |
| **ML-based GO prediction** | "calcium ion binding" (trained on existing data) | Same as InterPro |
| **Local motif analysis** | "metal-binding loops detected" | Generic; no Ca/Ln discrimination |
| **What actually resolves it** | Experimental crystallography with Ln3+ ions + mutagenesis + genomic context | Requires wet-lab biochemistry |

The function that distinguishes lanM from calmodulin — picomolar lanthanide affinity via a ~0.03 A difference in coordination sphere — is below the resolution of any current structure prediction or comparison method. This is a case where **biochemistry, not computation, reveals function**.

### Convergent evolution compounds the problem

Lanpepsy (LanP, Mfla_0908) binds lanthanides using **PepSY domains** — a completely different fold (JBC 2023, PMID:36702252). Structural search from LanM would never find LanP, and vice versa.

### What lanM teaches us about where structure-based methods need to go

LanM is an honest negative result for current tools. A future pipeline that could help would need:
1. **Binding site geometry comparison** — not just "is there a metal site?" but "how does the coordination geometry compare to canonical examples?" (not yet available)
2. **Sequence deviation flagging** — "this EF-hand has prolines where no characterized EF-hand does" (achievable now with MSA analysis, but not a structural method)
3. **Genomic context integration** — "adjacent to lanthanide-dependent MDH genes in a methylotroph" (this is what actually resolves the function)

**Bottom line**: For lanM, structure adds nothing over InterPro. The case is valuable as a benchmark for what future methods should aspire to, but claiming current structural tools would help here is dishonest.

## Published Cases Where Structure Genuinely Helped

These are cases from the literature where structural analysis provided correct function predictions that sequence methods missed — not retrospective narratives but actual computational discoveries.

### DUF-to-Function: DALI Remote Homology (Holm, Protein Science 2023)

Holm systematically identified 100 remote homologous relationships unreported in Pfam 35.0, linking **35 DUFs (domains of unknown function)** to characterized families using DALI structural search. Key examples:

| DUF | Discovered Function | Key Evidence |
|-----|-------------------|-------------|
| PF03690 (UPF0160) | DHH family phosphoesterase | Structural match to PDB 6mtzB |
| PF06356 (DUF1064) | TnsA-like endonuclease | Structural match to PDB 1t0fA |
| PF08795 (DUF1796) | Papain-like cysteine protease | Conserved Cys/His catalytic dyad in structure |
| PF10223 (DUF2181) | Phosphodiesterase | Conserved Mg-binding motif (H, ExD, H) |
| PF14033 (DUF4246) | 2OG-Fe(II) oxygenase superfamily | Structural match to PDB 6n1fA |
| PF11904 (GPCR-chaperone) | LolA/B superfamily | Conserved RxD motif, undetectable by sequence |

These are genuine positives: DALI found structural similarity that Pfam HMMs missed entirely.

### Dark Proteome Enzymes: PARSE (PNAS 2025)

PARSE scanned 34,015 "dark proteome" structures (no sequence similarity to known families) from AlphaFold and predicted **183 putative novel enzymes** from 51 EC classes. Most striking:

- **11 putative zinc-dependent endopeptidases** (EC 3.4.24.83) from diverse bacterial species with completely unique global folds but **5 conserved catalytic residues** aligned to reference PDB 1PWV. High active site conservation despite no global fold or sequence similarity — only local structural geometry reveals the shared function.
- Additional novel acylphosphatases, beta-lactamases, nucleoside deoxyribosyltransferases — all from proteins with zero detectable sequence homology to known enzymes.

### Cross-Phyla Annotation: Sponge Proteome (Ruperti et al., Genome Biol 2023)

MorphologFinder (ColabFold + Foldseek) annotated the *Spongilla lacustris* proteome — **50% more proteins** than eggNOG-mapper (sequence-based). Key specific discovery:

- **Spongilla FGF ligand**: Structural morpholog of chicken FGF4 (UniProt P48804), RMSD 0.89 A over 543 atoms, but only **11.8% sequence identity**. BLAST completely missed it. Revealed FGF signaling in sponge epithelia — previously unknown.

### Phage Protein Annotation: Phold (NAR 2025)

Over 65% of phage proteins lack sequence-detectable homologs. Phold (ColabFold + Foldseek) annotated **>50% of genes on an average phage** vs. significantly less by sequence methods alone. Structure-based annotation revealed RNA ligase T-like phosphodiesterases that hydrolyze host immune-activating cyclic dinucleotides.

### Classic: MJ0577 from *M. jannaschii* (Zarembinski et al., PNAS 1998)

MJ0577 — a hypothetical protein with no sequence-detectable function. Crystal structure at 1.7 A revealed **bound ATP**. Experimentally confirmed as an ATPase. Structural comparisons found only 11-17% sequence identity to the nearest characterized homologs. The classic "structure reveals what sequence cannot" paper.

### What these share

The pattern: structure adds genuine value when:
1. **No sequence homology exists at all** (dark proteome, DUFs, phage proteins)
2. **Sequence identity is <20%** (twilight zone; sponge FGF at 11.8%)
3. **Local active site geometry is conserved** despite divergent global fold (PARSE metalloproteases)

Structure does NOT help when the functional difference is subtle chemistry within the same fold (lanM: same EF-hand fold, different metal selectivity).

## Candidates from Our Pipeline

### Best candidate: cds1 (L-Cysteine Desulfhydrase) — IBA Annotation Failure

**Proteins**: MYCTU/cds1 (O69652), VIBCH/cds1 (Q9KT44)

**The problem**: Both annotated via IBA (phylogenetic inference) with "L-cysteine biosynthetic process" (GO:0019344). But cds1 is a cysteine **catabolic** enzyme — EC 4.4.1.1 (desulfhydrase) vs EC 2.5.1.47 (synthase). The IBA propagated from the PANTHER family root node to all descendants, but the cds1 subfamily underwent neo-functionalization. Active site motif differs: ASSGST (desulfhydrase) vs PTSGNTG (synthase). Only 24% sequence identity to synthases.

**Why structure could help here**: Unlike lanM, the functional difference between desulfhydrase and synthase involves different active site architecture — detectable by structural comparison. Foldseek search of the cds1 structure should return desulfhydrase hits, not synthase hits. EnzyMM catalytic site matching should match EC 4.4.1.1 templates, not EC 2.5.1.47.

**Status**: Both genes already reviewed in our pipeline with the IBA error documented.

### Also promising: PHYKPL — Wrong Enzyme Class from Family Membership

**Protein**: Human PHYKPL (Q8IUZ5)

**The problem**: Annotated as "transaminase activity" (GO:0008483) based on family membership. Actually functions as an ammoniophospholyase (EC 4.2.3.134). The active site is structurally distinct from transaminases despite belonging to the same fold family.

### Also promising: mll cluster genes — Sparse IEA on Novel Pathway

**Proteins**: mllA (C5B1I4), mllBC (C5B1I5), mllH (C5B1I9)

**The problem**: 1-4 IEA annotations each. Annotated as generic siderophore biosynthesis enzymes, but they synthesize methylolanthanin (a lanthanophore, not a siderophore). Foldseek might find metallophore biosynthetic homologs that refine the functional prediction beyond "siderophore."

## Worked Example: DUF4246 — Structure Finds What Sequence Cannot

This is a genuine positive result, computed live (not narrated from literature).

### The protein

**A0A2N3VF44** from *Nocardia fluminea* (actinobacterium), 496 aa.

- **InterPro**: "Protein of unknown function (DUF4246)" — PF14033
- **GO terms**: None
- **Pfam clan**: Cupin (CL0029)
- **Sequence search**: BLAST and HMM find only other DUF4246 proteins. No characterized homolog detectable by sequence.

### What Foldseek finds

AlphaFold model AF-A0A2N3VF44-F1 (pLDDT 90.81) submitted to Foldseek search against PDB100:

| Rank | PDB | Description | SeqId | E-value |
|------|-----|-------------|-------|---------|
| 1 | **7EEH** | Fe(II)/alpha-ketoglutarate-dependent dioxygenase TqaL | 10.4% | 1.3e-5 |
| 3 | **6LNH** | Indoleamine 2,3-dioxygenase (IDO), *B. thuringiensis* | 12.6% | 7.8e-5 |
| 7 | **3PL0** | BsmA homolog, *Methylobium petroleophilum* | 12.0% | 6.6e-4 |
| 8 | **4J25** | Prolyl-4-hydroxylase (P4H), *P. putida* | 13.6% | 5.3e-4 |
| 9 | **4NHY** | Human OGFOD1, 2OG-Fe(II) oxygenase | 12.3% | 4.7e-3 |
| 11 | **6N1F** | 2OG-Fe(II) oxygenase, *B. pseudomallei* | 8.3% | 1.4e-2 |
| 14 | **6ZYK** | Non-heme monooxygenase ThoJ | 13.2% | 2.4e-4 |

**ALL 20 top PDB hits are 2-oxoglutarate and iron(II)-dependent oxygenases** or closely related iron-dependent oxidoreductases. The sequence identity ranges from 8-15% — deep twilight zone where no sequence method would detect homology.

### Validation

- **PDB 6N1F** (hit #11) is the exact structure Holm identified in his 2023 paper as the functional match for DUF4246 — our Foldseek search independently reproduced his DALI result.
- The cupin clan assignment by Pfam is consistent (2OG-Fe(II) oxygenases are members of the cupin superfamily), but Pfam's HMM cannot resolve the specific function.
- DUF4246 currently has **5,315 proteins** in Pfam, all annotated as "unknown function" — this structural prediction could inform functional annotation across the entire family.

### What this demonstrates

| Method | Prediction for A0A2N3VF44 | Correct? |
|--------|--------------------------|----------|
| **HMM/InterPro** | "Protein of unknown function (DUF4246)" | No prediction |
| **BLAST** | Only other DUF4246 proteins | No prediction |
| **Pfam clan** | Cupin superfamily | Correct scaffold, no specific function |
| **Foldseek (AlphaFold → PDB)** | **2OG-Fe(II) oxygenase** | Specific, correct, validated by Holm 2023 |

**Key contrast with the lanM case**: For lanM, structure adds nothing over InterPro — both say "EF-hand" and neither can distinguish calcium from lanthanide binding. For DUF4246, sequence says *nothing at all* and structure provides a specific, validated functional prediction. This is the sweet spot for structure-based annotation: the twilight zone below ~15% sequence identity where HMMs fail but fold similarity persists.

### Implications for the gene review pipeline

DUF4246 is not in our current review pipeline, but this demonstrates a generalizable approach:
1. For any protein with only DUF annotations or no functional annotation, download the AlphaFold structure
2. Submit to Foldseek against PDB100
3. If top hits are functionally characterized proteins at <20% sequence identity, this is a structure-based function prediction that sequence methods miss
4. The prediction should be treated as provisional (equivalent to ISS evidence, not experimental) but can guide annotation review

## Next Steps

### Immediate
- Run the same Foldseek analysis on **cds1** (O69652) and **PHYKPL** (Q8IUZ5) from our pipeline — do structural hits correctly predict the function that IBA/IEA gets wrong?
- Try **DeepGO-SE** (pip-installable) on the same proteins as a complementary ML approach

### Medium-term
- Systematically screen all DUF-containing proteins in the review pipeline through Foldseek
- Set up a reproducible script for AlphaFold → Foldseek → functional annotation
- Evaluate PARSE for catalytic site detection on cds1 (desulfhydrase vs. synthase active site)

## Key References

### Structural search tools
- Foldseek: van Kempen et al., Nat Biotech 2023 (doi:10.1038/s41587-023-01773-0)
- Foldseek Clusters: Barrio-Hernandez et al., Nature 2023 (doi:10.1038/s41586-023-06510-w)
- DALI 100 remote homology discoveries: Holm, Protein Science 2023 (doi:10.1002/pro.4519)

### Structure-aware models
- SaProt: Su et al., ICLR 2024
- ProstT5: Heinzinger et al., NAR G&B 2024
- ESM3: Hayes et al., Science 2025

### GO/function prediction from structure
- DPFunc: Wang et al., Nat Comm 2025 (doi:10.1038/s41467-024-54816-8)
- DeepGO-SE: Kulmanov & Hoehndorf, Nat Mach Intell 2024
- DeepFRI: Gligorijevic et al., Nat Comm 2021 (doi:10.1038/s41467-021-23303-9)
- GraphEC: Sun et al., Nat Comm 2024 (doi:10.1038/s41467-024-52533-w)

### Local motif / catalytic site detection
- PARSE: Goldford et al., PNAS 2025 (doi:10.1073/pnas.2513219122)
- EnzyMM / M-CSA: ebi.ac.uk/thornton-srv/m-csa/

### Case studies: structure beats sequence
- Cross-phyla morphologs: Ruperti et al., Genome Biol 2023 (doi:10.1186/s13059-023-02942-9)
- Phage annotation (Phold): Bouras et al., NAR 2025 (doi:10.1093/nar/gkaf1448)
- MJ0577 ATPase: Zarembinski et al., PNAS 1998 (doi:10.1073/pnas.95.26.15189)

### Classification
- ECOD 2025: NAR 2025 (doi:10.1093/nar/gkae1104)
- TIM barrel review: Sterner & Hocker 2005; Nagano et al. 2002

## Open Questions

- Can we systematically run PARSE/EnzyMM on all proteins in the review pipeline and flag cases where structural motifs suggest functions not captured by existing annotations?
- For REE-related proteins (mll cluster, lut cluster, lanM): does structural analysis reveal additional functional sites missed by InterPro?
- How well do 3Di-based methods handle multi-domain proteins where domain orientation matters?
- For fold-switching proteins: can we detect these computationally and flag them during review?
