# SULT1A1 (human) — curation notes

UniProt: P50225 (ST1A1_HUMAN), 295 aa. EC 2.8.2.1. PANTHER family
`PANTHER:PTHR11783` ("SULFOTRANSFERASE  SULT").

> **Provenance note.** No `deep-research` provider is reachable in this environment
> (`ai-gene-review` exposes no `deep-research` subcommand here), so there is no
> `SULT1A1-deep-research-<provider>.md`. Per the project instructions, the literature
> synthesis is recorded here instead. Every assertion below is anchored to a cached
> publication in `publications/`, to the UniProt record, or to a named web source.

---

## 1. What the protein is

SULT1A1 is a **cytosolic (soluble) sulfotransferase** — the "thermostable"
phenol-sulfating phenol sulfotransferase (TS-PST / P-PST-1), historically also
called HAST1, ST1A3 and aryl sulfotransferase 1. It transfers the sulfonate group
of **PAPS (3'-phosphoadenosine 5'-phosphosulfate)** onto the hydroxyl (or amine)
of small acceptor molecules, releasing PAP.

[file:human/SULT1A1/SULT1A1-uniprot.txt, "Sulfotransferase that utilizes 3'-phospho-5'-adenylyl sulfate
(PAPS) as sulfonate donor to catalyze the sulfate conjugation of a wide variety of acceptor molecules
bearing a hydroxyl or an amine group."]

It is an **obligate homodimer** (UniProt SUBUNIT: `Homodimer`, ECO:0000269 from
PMID:12471039, PMID:16221673, PMID:20417180), dimerising through the conserved
C-terminal KTVE motif shared across the cytosolic SULTs.

Catalytic machinery (UniProt FT):
- `ACT_SITE 108` — proton acceptor (His108)
- `BINDING 48..53, 130, 138, 193, 227..232, 255..259` — PAPS (CHEBI:58339)
- `BINDING 106..108` — substrate (ECO:0000269|PubMed:12471039)

The structural work confirms this directly: *"The refined 3D structure of
SULT1A1-PAP-2NAP revealed a single 2NAP molecule within pocket-1, positioned in a
catalytically competent manner in which the hydroxyl group is positioned 2.34 Å from
the catalytic amine group of His108 and 3.33 Å from Lys106"*
[PMID:22069470 full text].

**Localisation:** cytoplasm/cytosol. UniProt `SUBCELLULAR LOCATION: Cytoplasm`
(ECO:0000269|PubMed:8093002); Reactome places every SULT1A1 reaction in the cytosol.
No membrane, signal peptide or targeting features in the record.

**Tissue distribution:** UniProt `TISSUE SPECIFICITY: Liver, lung, adrenal, brain,
platelets and skin.` SULT1A1 is the dominant hepatic SULT (>50% of total SULT protein
in liver), with substantial gut expression; platelet SULT1A1 activity is the classic
surrogate phenotype used in pharmacogenetic studies
([ScienceDirect SULT1A1 topic page](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/sult1a1)).

---

## 2. Substrate profile — what the enzyme is actually *for*

The defining feature is **broad specificity with a strong preference for small
phenols**, achieved by a plastic, largely hydrophobic acceptor pocket:

> *"For example, SULT1A1 [8] displays substrate preference for small phenolic
> compounds, while SULT1E1 shows a preference for estrogen acceptors [9]."*
> [PMID:22069470]

> *"Cytosolic sulfotransferases (SULTs) are mammalian enzymes that detoxify a wide
> variety of chemicals through the addition of a sulfate group."* [PMID:22069470]

### 2.1 Small phenols / model xenobiotics (highest-confidence core)
- **4-nitrophenol**, Km **0.6 µM** — the canonical P-PST substrate.
  *"COS-expressed HAST1 was shown to be enzymatically active in sulphating
  p-nitrophenol with high affinity (Km 0.6 microM)"* [PMID:8093002].
  (HAST1 = SULT1A1; HAST3 = SULT1A3.)
- 2-naphthol, 3-cyano-7-hydroxycoumarin — co-crystallised acceptors [PMID:22069470].
- Drugs: acetaminophen/paracetamol, minoxidil (UniProt, by similarity;
  Reactome R-HSA-158468 and R-HSA-9753277 both place APAP sulfation on SULT1A1).

### 2.2 Iodothyronines — the *highest-affinity* documented substrates
This is the most striking kinetic fact about the enzyme and is under-represented in GO.

> *"In all cases, the substrate preference was 3,3'-T2 >> rT3 > T3 > T4."*
> [PMID:10199779]

> *"The apparent Km values of 3,3'-T2 and T3 [at 50 micromol/L
> 3'-phosphoadenosine-5'-phosphosulfate (PAPS)] were 1.02 and 54.9 micromol/L for
> liver cytosol, 0.64 and 27.8 micromol/L for kidney cytosol, 0.14 and 29.1
> micromol/L for SULT1A1, and 33 and 112 micromol/L for SULT1A3, respectively."*
> [PMID:10199779]

Km for 3,3'-T2 is **0.14 µM** — ~240× tighter than SULT1A3's 33 µM, and the tightest
Km anywhere in this gene's record. UniProt also records `KM=0.12 uM for
3,3'-diiodothyronine`. Sulfation channels iodothyronines toward degradation:
*"Sulfation is an important pathway of thyroid hormone metabolism that facilitates
the degradation of the hormone by the type I iodothyronine deiodinase"* [PMID:10199779].

**Known unknown** (the authors' own words):
> *"Of the latter, SULT1A1 clearly shows the highest affinity for both iodothyronines
> and PAPS, but it remains to be established whether it is the prominent isoenzyme for
> sulfation of thyroid hormone in human liver and kidney."* [PMID:10199779]

There is **no GO term for iodothyronine/thyroid-hormone sulfotransferase activity**
(checked: `GO:0008146` descendants contain nothing thyroid-related). Proposed below.

### 2.3 Procarcinogen bioactivation (the "dark side" of the same chemistry)
SULT1A1 O-sulfonates **N-hydroxy-arylamines and N-hydroxy-heterocyclic amines**,
producing unstable sulfate esters that decompose to nitrenium ions and form DNA adducts.

> *"In the 12 human hepatic cytosols studied, the extent of
> 3'-phosphoadenosine-5'-phosphosulfate-dependent DNA binding of the N-hydroxy
> derivatives were all significantly correlated with levels of thermostable phenol
> ST (TS-PST) activity but not with thermolabile phenol ST or dehydroepiandrosterone
> ST activities."* [PMID:7834621]

> *"A major human sulfotransferase, SULT1A1, metabolizes and/or bioactivates many
> endogenous compounds and is implicated in a range of cancers because of its ability
> to modify diverse promutagen and procarcinogen xenobiotics."* [PMID:12471039]

Reactome R-HSA-158860 ("SULT1A1 dimer sulfonates NHABP") captures the
N-hydroxy-4-aminobiphenyl case. Mouse SULT1A knockout/humanisation studies confirm
the toxification role in vivo for 4-aminobiphenyl and methyleugenol
([Essays Biochem 2024, PMC11625864](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11625864/)).

### 2.4 Dietary flavonoids
> *"SULT1A2 and SULT1A1 catalyze preferably and most efficiently the formation of
> hesperetin 3'-O-sulfate, and SULT1C4 catalyzes preferably and most efficiently the
> formation of hesperetin 7-O-sulfate."* [PMID:20056724]

**Important for annotation:** hesperetin is a **flavanone**, and the SULT1A1 product is
the **3'-O**-sulfate (B-ring). The GO term currently used, `GO:0047894 flavonol
3-sulfotransferase activity`, is defined as *"3'-phospho-5'-adenylyl sulfate +
quercetin = adenosine 3',5'-diphosphate + H+ + quercetin 3-sulfate"* — a different
substrate class (flavonol) and a different position (3, C-ring). Quercetin was not
assayed in PMID:20056724. `GO:1990135 flavonoid sulfotransferase activity` is the
correct term. (Note these two are *siblings* under GO:0008146, not parent/child.)

### 2.5 Gut-microbial 4-ethylphenol → 4-EPS
> *"We observed sulfation of 4EP to 4EPS by the sulfotransferase SULT1A1 and others
> during in vitro biochemical reactions"* [PMID:35165440]

4-EPS crosses the blood–brain barrier, impairs oligodendrocyte maturation and
myelination, and produces anxiety-like behaviour in mice. UniProt records this with
ECO:0000269|PubMed:35165440 and RHEA:70607. The paper itself flags the open question:
*"though the site(s) of 4EP sulfation remains unknown"*. **Not currently in GOA** —
a genuine annotation gap.

### 2.6 Marginal / low-affinity activities (real in vitro, weak in vivo)
These are the ones most at risk of over-annotation:

| Substrate | SULT1A1 kinetics | Physiological isoform | Source |
|---|---|---|---|
| Dopamine | Km **345 µM**, Vmax 0.16 nmol/min/mg | **SULT1A3** (M-PST), Km 9.7 µM | [PMID:8093002], UniProt |
| 17β-estradiol | sulfated, but with substrate inhibition; crystal has E2 in a **non-productive** mode | **SULT1E1** (nM affinity) | [PMID:16221673] |
| Ethanol | one of four ethanol-sulfating SULTs; ethyl sulfate is a *minor* metabolite | shared; small intestine highest activity | [PMID:23207770] |

> *"HAST1 could also sulphate dopamine, as could HAST3 sulphate p-nitrophenol, but the
> Km for these reactions were at least two orders of magnitude greater than for the
> preferred substrates."* [PMID:8093002]

> *"The crystal structure of SULT1A1 that we present here has PAP and one molecule of
> E2 bound in a nonproductive mode in the active site."* [PMID:16221673]

> *"Ethyl sulfate, a minor and direct ethanol metabolite in adult human body, has been
> implicated as a biomarker for alcohol consumption and in utero exposure to ethanol."*
> [PMID:23207770]

Note also that **ethanol is an aliphatic alcohol, not a phenol** — so the
PMID:23207770-based `GO:0004062 aryl sulfotransferase activity` IDA is mis-typed for
its own evidence; `GO:0004027 alcohol sulfotransferase activity` is what that
experiment shows.

---

## 3. Substrate inhibition and active-site plasticity

A recurring theme across three structural papers: SULT1A1 binds a *second*, catalytically
unproductive acceptor molecule, which explains its partial substrate inhibition.

> *"An unexpected finding is that the enzyme accommodates not one but two molecules of
> the xenobiotic model substrate p-nitrophenol in the active site."* [PMID:12471039]

> *"In agreement with previous reports, the enzyme shows partial substrate inhibition at
> high concentrations of E2."* [PMID:16221673]

> *"We found that active site plasticity enables binding of different acceptors and
> identified dramatic structural changes in the SULT1A1 active site leading to the
> binding of a second acceptor molecule in a conserved yet non-productive manner."*
> [PMID:22069470]

This plasticity is the mechanistic explanation for the broad specificity, and is why
substrate-specific MF terms should be applied to SULT1A1 sparingly.

---

## 4. Protein–protein interactions

- **SULT2B1 (O00204)** — UniProt `INTERACTION: P50225; O00204: SULT2B1; NbExp=8`.
  Four separate large-scale interactome papers (PMID:25416956, PMID:25910212,
  PMID:31515488, PMID:33961781) each generate a bare `GO:0005515 protein binding` IPI
  with `WITH/FROM UniProtKB:O00204`. None of these assigns a molecular function.
- **SULT4A1 (Q9BR01)** — mechanistically informative, unlike the above:
  > *"Using immunoprecipitation, SULT4A1 was shown to interact with both SULT1A1 and
  > SULT1A3 when expressed in human cells."* [PMID:32152050]
  > *"Mutation of the conserved dimerization motif located in the C terminus of the
  > sulfotransferases prevented this interaction."* [PMID:32152050]

  SULT4A1 lowers SULT1A1/1A3 protein levels in neuronal cells and may act as a
  chaperone. Because the interaction is shown to require the conserved dimerisation
  motif, `GO:0046982 protein heterodimerization activity` is a defensible, more
  informative replacement for the bare `protein binding` term.
- **Homodimerisation** (`GO:0042803`) is experimentally established (UniProt SUBUNIT,
  3 ECO:0000269 references) but is **not annotated in GOA** — an annotation gap.

---

## 5. Reference provenance problem: PMID:8661000 is about the *paralog*

Two legacy TAS annotations assigned by PINC in 2003 (`GO:0008146 sulfotransferase
activity` and `GO:0009308 amine metabolic process`) cite:

> Her C, Raftogianis R, Weinshilboum RM (1996) **"Human phenol sulfotransferase STP2
> gene: molecular cloning, structural characterization, and chromosomal localization."**
> Genomics 33:409–420. [PMID:8661000]

**STP2 is SULT1A2, not SULT1A1.** Checked directly against UniProt:
- P50225 (SULT1A1): `GN   Name=SULT1A1; Synonyms=STP, STP1;`
- P50226 (SULT1A2): `GN   Name=SULT1A2; Synonyms=STP2;` — and PMID:8661000 is
  reference 4 of the P50226 entry.

The abstract is explicit that the object of study is the STP2 gene:
> *"We have determined the structure and chromosomal localization of the gene for one
> of these two cDNAs, STP2, as a step toward understanding molecular genetic mechanisms
> involved in the regulation of this enzyme activity in humans."* [PMID:8661000]

The paper is a genomic-structure/cloning study; it contains no amine-metabolism assay
for either gene. `GO:0008146` happens to be true of SULT1A1 anyway (abundant
independent experimental support), so that row survives on its merits but should be
re-sourced. `GO:0009308 amine metabolic process` has neither support from this
reference nor a good fit to the gene — SULT1A1 is the *phenol*-preferring form, while
monoamine sulfation belongs to SULT1A3 — so it is treated as an over-annotation.

Nomenclature confirmed via
[Her et al. 1996 / STP1-STP2 genomic organisation, PMID:8912648](https://pubmed.ncbi.nlm.nih.gov/8912648/)
and [OMIM 171150](https://www.omim.org/entry/171150).

---

## 6. Polymorphism / pharmacogenetics (context, not GO-annotatable)

UniProt `POLYMORPHISM: There are several alleles. The sequence shown is that of allele
SULT1A1*3.` The best-known variant is **Arg213His (`SULT1A1*2`, rs1042028)** —
UniProt: *"R -> H (in allele SULT1A1*2; has a lower sulfotransferase activity)"*. It
reduces both activity and thermostability and is the basis of a very large
epidemiological literature on cancer risk and drug response. Copy-number variation at
the locus also modulates activity. These are allele-level facts and do not by
themselves justify GO annotations.

## 7. Loss-of-function

`Sult1a1` knockout mice are viable and outwardly normal — *"Sult1a1 or Sult1d1 knockouts
were healthy and showed no obvious deficiencies"*, in contrast to `Sult1e1` (reduced
fertility) and `Sult4a1` (early postnatal death)
([Essays Biochem 2024, PMC11625864](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11625864/)).
The knockouts *are* protected against DNA-adduct formation by 4-aminobiphenyl and
methyleugenol, confirming the bioactivation role in vivo. So the gene's indispensable
role is chemical-defence/bioactivation rather than a developmental program.

---

## 8. Annotation decisions taken (summary)

| Term | Evidence | Action | Why |
|---|---|---|---|
| GO:0004062 aryl sulfotransferase activity | IBA, IEA, 5×EXP, 3×IDA | ACCEPT | Core MF; EC 2.8.2.1; multiple structures |
| GO:0008146 sulfotransferase activity | IEA, 2×IDA, TAS | ACCEPT / MODIFY | See per-row notes |
| GO:0050656 PAPS binding | IDA | ACCEPT | Crystal structures + 6 UniProt BINDING sites |
| GO:0005737 / GO:0005829 | IBA/IEA/EXP/7×TAS | ACCEPT | Cytosolic enzyme, no membrane features |
| GO:0051923 sulfation, GO:0050427 PAPS metabolic process | IBA/IDA | ACCEPT | Direct consequence of catalysis |
| GO:0006805 xenobiotic metabolic process | 2×IDA | ACCEPT | Core biological role |
| GO:0042403 thyroid hormone metabolic process | IDA | ACCEPT | Highest-affinity substrate class |
| GO:0009812 flavonoid metabolic process | IDA | ACCEPT | Dietary phenol first-pass conjugation |
| GO:0006790 sulfur compound metabolic process | IEA (ARBA) | MODIFY → GO:0051923 | Uninformative ancestor |
| GO:0047894 flavonol 3-sulfotransferase | IDA | MODIFY → GO:1990135 | Hesperetin is a flavanone, product is 3'-O-sulfate |
| GO:0004062 (IDA, PMID:23207770) | IDA | MODIFY → GO:0004027 | Ethanol is an aliphatic alcohol, not a phenol |
| GO:0005515 (PMID:32152050) | IPI | MODIFY → GO:0046982 | Dimerisation-motif-dependent SULT4A1 heterodimer |
| GO:0005515 × 4 (SULT2B1) | IPI | MARK_AS_OVER_ANNOTATED | Bare interactome hits, no MF content |
| GO:0050294 steroid sulfotransferase / GO:0008210 estrogen metabolic process | IEA + 2×IDA | KEEP_AS_NON_CORE | Real but low-affinity; SULT1E1 is the physiological enzyme |
| GO:0042420 dopamine catabolic process | IDA | MARK_AS_OVER_ANNOTATED | Km 345 µM; SULT1A3 is the physiological form |
| GO:0006068 ethanol catabolic process | IDA | MARK_AS_OVER_ANNOTATED | Authors call ethyl sulfate a "minor" metabolite |
| GO:0009308 amine metabolic process | TAS | MARK_AS_OVER_ANNOTATED | Unsupported by the (paralog's) cited paper |
| GO:0042803 protein homodimerization activity | — | NEW | Obligate homodimer; absent from GOA |

The `GO:0008146` IDA from PMID:10199779 was left as **ACCEPT** rather than modified to
`GO:0004062`: the same paper already carries a `GO:0004062` EXP row, so the modification
would only have created a duplicate. What is actually missing there is a thyroid-hormone
sulfotransferase term, which is raised under proposed terms instead.

### One deliberate validation warning

`ai-gene-review validate` reports exactly one warning:

> Inconsistent review actions for term GO:0004062: ACCEPT (IBA, IEA, EXP×5, IDA×2);
> MODIFY (IDA)

This is intentional and is explained in the review's `reason` field. The consistency
check is a good heuristic — a term is normally either right for a gene or not — but here
the divergence is evidence-level, not gene-level: SULT1A1 unambiguously *has* aryl
sulfotransferase activity (nine rows on phenolic acceptors), while the single
PMID:23207770 row assayed only **ethanol**, an aliphatic alcohol, which cannot
demonstrate a reaction GO defines as requiring a phenol. The file is therefore `DRAFT`
rather than `COMPLETE`.

### Proposed new terms
1. **thyroid hormone sulfotransferase activity** — no GO term exists for the
   iodothyronine sulfation reaction, despite it being SULT1A1's highest-affinity
   chemistry and having five RHEA reactions (RHEA:67876, 67888, 67892, 83575) in UniProt.

### Gaps in GOA worth filling
- `GO:0042803 protein homodimerization activity` — the enzyme is an obligate homodimer
  with three experimental UniProt references, and Reactome models every reaction on the
  "SULT1A1 dimer"/"SULT1A1 homodimer".
- 4-ethylphenol sulfation (RHEA:70607, PMID:35165440) is in UniProt but absent from GOA.
