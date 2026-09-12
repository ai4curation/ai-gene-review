---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-11T17:37:16.263062'
end_time: '2026-07-11T18:05:14.246823'
duration_seconds: 1677.98
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_0897
  gene_symbol: PP_0897
  uniprot_accession: Q88PF3
  protein_description: 'RecName: Full=Fumarate hydratase class I {ECO:0000256|PIRNR:PIRNR001394};
    EC=4.2.1.2 {ECO:0000256|PIRNR:PIRNR001394};'
  gene_info: OrderedLocusNames=PP_0897 {ECO:0000313|EMBL:AAN66522.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the class-I fumarase family.
  protein_domains: Fe-S_hydro-lyase_TtdA-typ_cat. (IPR004646); Fe-S_hydro-lyase_TtdB-typ_cat.
    (IPR004647); Fe-S_hydroAse_TtdB_cat_sf. (IPR036660); Fe_dep_fumarate_hydratase.
    (IPR011167); Fumerase (PF05681)
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
citation_count: 7
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PP_0897-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PP_0897-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88PF3
- **Protein Description:** RecName: Full=Fumarate hydratase class I {ECO:0000256|PIRNR:PIRNR001394}; EC=4.2.1.2 {ECO:0000256|PIRNR:PIRNR001394};
- **Gene Information:** OrderedLocusNames=PP_0897 {ECO:0000313|EMBL:AAN66522.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the class-I fumarase family.
- **Key Domains:** Fe-S_hydro-lyase_TtdA-typ_cat. (IPR004646); Fe-S_hydro-lyase_TtdB-typ_cat. (IPR004647); Fe-S_hydroAse_TtdB_cat_sf. (IPR036660); Fe_dep_fumarate_hydratase. (IPR011167); Fumerase (PF05681)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_0897" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_0897' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_0897** (gene ID: PP_0897, UniProt: Q88PF3) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of PP_0897 (UniProt Q88PF3): The Class I [4Fe-4S] Fumarate Hydratase of *Pseudomonas putida* KT2440

## Summary

**PP_0897 (UniProt Q88PF3) encodes the class I fumarate hydratase (fumarase; EC 4.2.1.2) of *Pseudomonas putida* KT2440.** It is a soluble, cytoplasmic, iron–sulfur enzyme that uses a catalytic [4Fe-4S] cluster to catalyze the reversible hydration/dehydration reaction interconverting fumarate and (S)-malate (L-malate). This is the penultimate step of the oxidative branch of the tricarboxylic acid (TCA) cycle (succinate → fumarate → **malate** → oxaloacetate). The gene identity, organism, protein family, and domain architecture supplied by the UniProt record are all internally consistent and are corroborated by sequence, structural, and biochemical evidence drawn from well-characterized homologs, so this annotation is made with high confidence.

Mechanistically, PP_0897 belongs to the **class I fumarase family**, which is biochemically and evolutionarily distinct from the more familiar iron-independent class II fumarases. Class I enzymes are single-chain (or two-subunit) proteins that carry a catalytic [4Fe-4S] cluster whose **unique, non-cysteine-ligated iron** binds substrate directly and acts as a Lewis acid during catalysis. This cofactor makes the enzyme heat-labile and oxygen-sensitive. PP_0897 is a FumA/FumB-type enzyme: global sequence alignment shows ~36% identity to *Escherichia coli* FumA (class I) versus only ~21–23% identity to class II fumarases (*E. coli* FumC, human FH), placing it unambiguously in the class I lineage. Three conserved cysteines — predicted here to be **C66, C185, and C277** — are positionally conserved with the *E. coli* FumA cluster ligands and are contributed by both of the protein's catalytic domains.

Within *P. putida* KT2440, PP_0897 is the **sole class I fumarase among three fumarase isozymes**, the other two being class II enzymes (PP_0944 and PP_1755). This mirrors the *E. coli* arrangement of iron-dependent class I enzymes (FumA/FumB) coexisting with an iron-independent class II enzyme (FumC) that is specifically induced under iron limitation and oxidative (superoxide) stress. The implication is that PP_0897 provides the principal, iron-dependent fumarase activity of the aerobic TCA cycle under nutrient-replete conditions, while the class II isozymes offer a redundant, iron- and oxidative-stress-resistant backup — a division of labor with important consequences for metabolic robustness in this environmentally versatile, biotechnologically important soil bacterium.

---

## Key Findings

### F001 — PP_0897 is a class I [4Fe-4S] fumarate hydratase catalyzing reversible fumarate ↔ (S)-malate (EC 4.2.1.2)

The primary function of PP_0897 is enzymatic: it catalyzes the **reversible hydration of fumarate to (S)-malate** (equivalently, the dehydration of (S)-malate to fumarate), classified as EC 4.2.1.2. The UniProt Q88PF3 record annotates the FUNCTION as "Catalyzes the reversible hydration of fumarate to (S)-malate," specifies the catalytic activity as (S)-malate = fumarate + H₂O (RHEA:12460), lists a [4Fe-4S] cluster cofactor (ChEBI:49883), and carries the keywords 4Fe-4S / Iron-sulfur / Lyase, with the family assignment "Belongs to the class-I fumarase family." The protein is a 507-amino-acid single polypeptide organized into two catalytic domains: an Fe-S hydro-lyase tartrate-dehydratase alpha-type domain (residues ~11–285) and a beta-type domain (residues ~289–488).

This annotation is grounded in decades of biochemistry. Class I fumarases were biochemically defined in *E. coli*, which contains **three biochemically distinct fumarases**: the *fumA* and *fumB* gene products are heat-labile, iron-containing enzymes, while *fumC* encodes a heat-stable enzyme that does not require iron ([PMID: 7592392](https://pubmed.ncbi.nlm.nih.gov/7592392/)). The mechanistic hallmark of the class I family is its cofactor: class I fumarate hydratases "use a [4Fe-4S] cluster to catalyze the reversible conversion of fumarate to" malate ([PMID: 31743022](https://pubmed.ncbi.nlm.nih.gov/31743022/)). The reaction and enzyme classification are confirmed independently: "Fumarate hydratases (FHs; EC 4.2.1.2) are enzymes that catalyze the reversible hydration of fumarate to S-malate" ([PMID: 22569531](https://pubmed.ncbi.nlm.nih.gov/22569531/)). Every element of the Q88PF3 annotation — the reaction, the EC number, the cofactor, and the family — is therefore consistent with the established biochemistry of class I fumarases.

### F002 — Catalytic mechanism: substrate coordinates the unique Fe of the [4Fe-4S] cluster; the enzyme is oxygen-sensitive

The catalytic mechanism of PP_0897 can be inferred with confidence from crystal structures of its close structural/mechanistic homolog, the class I fumarate hydratase of *Leishmania major*. In these structures, "the substrate S-malate is bound bidentate to the unique iron of the [4Fe-4S] cluster" ([PMID: 27528683](https://pubmed.ncbi.nlm.nih.gov/27528683/)). This unique iron — the one cluster iron *not* ligated by a protein cysteine — functions as a **Lewis acid**, polarizing the substrate and facilitating the *anti* addition/elimination of water across the C=C double bond of fumarate.

The catalytic importance and class-specificity of this unique iron is demonstrated by inhibitor studies: the selectivity of the inhibitor 2-thiomalate for class I FHs "is due to direct coordination of the inhibitor to the unique Fe of the catalytic [4Fe-4S] cluster that is found in class I parasitic FHs but is absent from class II human FH" ([PMID: 30645090](https://pubmed.ncbi.nlm.nih.gov/30645090/)). This is the defining biochemical difference between the two fumarase classes: class I enzymes contain the substrate-binding iron; class II enzymes do not.

A direct physiological consequence of relying on a solvent-exposed [4Fe-4S] cluster is **oxygen sensitivity**. The catalytic efficiency of class I FHs "under aerobic and anaerobic environments suggests that they are both highly sensitive to oxidation and damaged by oxygen" ([PMID: 22569531](https://pubmed.ncbi.nlm.nih.gov/22569531/)). Consistent with the redox chemistry of such clusters, the *E. coli* class I FumA/FumB [4Fe-4S] Lewis-acid active center has a reduction potential of approximately −290 mV ([PMID: 23405168](https://pubmed.ncbi.nlm.nih.gov/23405168/)). PP_0897 is therefore predicted to be an oxygen-labile, iron-dependent enzyme whose activity can be compromised under oxidative stress — a property that rationalizes the existence of the oxidatively robust class II backups (see F005).

### F003 — Sequence/evolutionary evidence: PP_0897 is a FumA/FumB-type single-chain class I fumarase

A Needleman–Wunsch global alignment of Q88PF3 (507 aa) against reference fumarases places PP_0897 firmly in the class I lineage. It shares **35.6% identity with *E. coli* FumA** (P0AC33, aerobic class I) and **33.4% with FumB** (P14407, anaerobic class I), but only **22.9% with *E. coli* FumC** (P05042, class II) and **20.6% with human FH** (P07954, class II). The latter two values are at the level expected for unrelated proteins of similar length, so the sequence data cleanly separate PP_0897 (class I) from the class II fumarases.

| Reference enzyme | UniProt | Class | Identity to PP_0897 |
|---|---|---|---|
| *E. coli* FumA | P0AC33 | I (aerobic) | 35.6% |
| *E. coli* FumB | P14407 | I (anaerobic) | 33.4% |
| *E. coli* FumC | P05042 | II | 22.9% |
| Human FH | P07954 | II | 20.6% |
| *E. coli* TtdA (α subunit only) | P0AC35 | I (tartrate dehydratase α) | 21.9% |

The 21.9% identity to the standalone tartrate-dehydratase alpha subunit TtdA (201 aa) is consistent with PP_0897 being a **fused single chain containing both the alpha and beta catalytic domains** — in some organisms these are separate polypeptides (TtdA/TtdB), whereas here they are combined in one 507-residue protein. This matches the UniProt/InterPro domain architecture: a TtdA-type alpha-catalytic domain (IPR004646, res ~11–285) followed by a TtdB-type beta-catalytic domain (IPR004647, res ~289–488), assembling as a homodimer.

The FumA/FumB enzymes to which PP_0897 is homologous are well characterized: "FumA and FumB are essentially identical in their Michaelis–Menten kinetics of the reversible fumarate to L-malate conversion; however, FumB has a significantly greater catalytic efficiency for the conversion of D-tartrate to oxaloacetate consistent with the requirement of the fumB gene for growth on D-tartrate" ([PMID: 23405168](https://pubmed.ncbi.nlm.nih.gov/23405168/)). This establishes both the main reaction and a possible secondary D-tartrate activity that class I enzymes can support. Structurally, the class I fold is dimeric with "a dimeric architecture for this FH that resembles a heart, with each lobe comprised of two domains that are arranged around the active site" ([PMID: 27528683](https://pubmed.ncbi.nlm.nih.gov/27528683/)) — matching PP_0897's fused alpha+beta domains and annotated homodimeric state.

### F004 — Localization and pathway: a cytoplasmic soluble enzyme performing the fumarase step of the TCA cycle

PP_0897 is predicted to be a **soluble cytoplasmic protein**. The Q88PF3 record shows no signal peptide, no transmembrane segment, and no lipoprotein or secretion features — the profile of a cytosolic enzyme. Bacterial class I fumarases (*E. coli* FumA/FumB) are cytoplasmic TCA-cycle enzymes. In eukaryotes that possess class I FHs, the isoforms partition between organelles — "Intracellular localization studies located LmFH-1 in the mitochondrion, whereas LmFH-2 was found predominantly in the cytosol with possibly also some in glycosomes" ([PMID: 22569531](https://pubmed.ncbi.nlm.nih.gov/22569531/)) — but prokaryotes such as *P. putida* lack these compartments, so PP_0897 necessarily acts in the cytoplasm.

Functionally, the reaction fumarate + H₂O ⇌ (S)-malate is the **penultimate step of the oxidative TCA cycle** (succinate → fumarate → malate → oxaloacetate). Fumarase is a canonical TCA-cycle enzyme: "The tricarboxylic acid cycle enzyme fumarase catalyzes the interconversion of fumarate to L-malate" ([PMID: 7592392](https://pubmed.ncbi.nlm.nih.gov/7592392/)). *P. putida* KT2440 is an obligate aerobe that operates a complete TCA cycle for energy generation and biosynthetic precursor supply, while routing sugar catabolism through the Entner–Doudoroff pathway. PP_0897 thus sits at the heart of central carbon and energy metabolism, supplying malate/oxaloacetate for respiration, anaplerosis, and gluconeogenesis.

### F005 — PP_0897 is the sole class I fumarase among three fumarase isozymes in *P. putida* KT2440

A UniProt survey of the KT2440 proteome (taxid 160488) returns **three fumarate hydratases**: PP_0897 / Q88PF3 (class I, 507 aa, [4Fe-4S]) plus two class II enzymes, PP_0944 / Q88PA6 (459 aa) and PP_1755 / Q88M20 (464 aa). PP_0897 is therefore the organism's only iron-sulfur, class I fumarase.

| Locus | UniProt | Class | Length | Cofactor |
|---|---|---|---|---|
| **PP_0897** | Q88PF3 | **I** | 507 aa | [4Fe-4S] |
| PP_0944 | Q88PA6 | II | 459 aa | none (Fe-independent) |
| PP_1755 | Q88M20 | II | 464 aa | none (Fe-independent) |

This arrangement recapitulates the well-studied *E. coli* paradigm, in which iron-dependent class I enzymes (FumA/FumB) coexist with an iron-independent class II enzyme (FumC). The two systems are differentially regulated by iron and oxidative stress: "Cellular iron limitation stimulated fumC but not fumA expression. Superoxide radicals also caused increased fumC gene expression; fumA expression was unaffected. Both the superoxide control and the iron control of fumC expression required the SoxR regulatory protein" ([PMID: 7592392](https://pubmed.ncbi.nlm.nih.gov/7592392/)). The most likely physiological interpretation is that PP_0897 provides the principal fumarase activity under iron-replete, low-oxidative-stress conditions, while the class II isozymes (which lack the vulnerable Fe-S cluster) act as backups when iron is scarce or superoxide is elevated — precisely the conditions under which the class I enzyme's cluster would be at risk. That class I [4Fe-4S] fumarases can be differentially regulated to serve distinct niches is directly supported: "The highly homologous [4Fe-4S] containing fumarases FumA and FumB, sharing 90% amino acid sequence identity, from *Escherichia coli* are differentially regulated, which suggests a difference in their physiological function" ([PMID: 23405168](https://pubmed.ncbi.nlm.nih.gov/23405168/)).

PP_0897 carries conserved cysteine motifs in both catalytic domains — alpha-domain C58 (…RMCATGH…) / C66 (…PICQDTG…) and beta-domain C272/C277 (…CMIPNC…) — consistent with the three-cysteine ligation of a catalytic [4Fe-4S] cluster that leaves the unique Fe available for substrate binding.

### F006 — Refined [4Fe-4S] cluster ligand prediction: three conserved cysteines C66, C185, C277

Class I fumarate hydratases coordinate their catalytic [4Fe-4S] cluster with **three** cysteines, leaving the fourth "unique" iron free for substrate binding (F002). To identify which of PP_0897's five cysteines serve as cluster ligands, a global (Needleman–Wunsch) alignment of PP_0897 (Q88PF3) to *E. coli* FumA (P0AC33) was performed. Exactly three of PP_0897's cysteines are positionally conserved with FumA cysteines:

| PP_0897 residue | Aligns to FumA | Conserved motif | Domain |
|---|---|---|---|
| **C66** | C105 | …PI**C**QDTG… ('CQDTG') | α / TtdA-type |
| **C185** | C224 | …GW**C**PPG… ('CPP') | α / TtdA-type |
| **C277** | C318 | …MIPN**C**AA… | β / TtdB-type |
| C58 (not conserved) | A97 | — | α |
| C272 (not conserved) | G313 | — | β |

The three conserved cysteines (C66, C185, C277) are contributed by **both** catalytic domains — C66 and C185 from the alpha/TtdA-type domain and C277 from the beta/TtdB-type domain — which is exactly the expected topology for a two-domain class I fumarase assembling a single inter-domain cluster. The two non-conserved cysteines (C58, C272) align to non-cysteine residues in FumA (Ala97 and Gly313, respectively) and are therefore not predicted to be cluster ligands.

This prediction rests on two experimentally established facts: the class I fold "reveals a previously undiscovered protein fold that coordinates a catalytically essential [4Fe-4S] cluster" ([PMID: 27528683](https://pubmed.ncbi.nlm.nih.gov/27528683/)), and the reference enzyme is a genuine [4Fe-4S] protein — "The highly homologous [4Fe-4S] containing fumarases FumA and FumB" ([PMID: 23405168](https://pubmed.ncbi.nlm.nih.gov/23405168/)). C66, C185, and C277 are thus the most probable [4Fe-4S] cluster ligands of PP_0897, with the unique fourth iron reserved for fumarate/(S)-malate coordination.

---

## Mechanistic Model / Interpretation

Bringing the findings together, PP_0897 can be modeled as follows.

**Reaction and role in metabolism.** PP_0897 catalyzes one specific, reversible step of central metabolism:

```
                        PP_0897 (class I FH, [4Fe-4S])
   ... succinate ──► fumarate  +  H2O  ⇌  (S)-malate ──► oxaloacetate ...
        (SDH)                                                (MDH)
                     └──────── oxidative TCA cycle ────────┘
```

The enzyme operates in the cytoplasm of an aerobically respiring cell, feeding the malate/oxaloacetate node that supports respiration, anaplerosis, and gluconeogenesis. Because *P. putida* KT2440 catabolizes sugars via the Entner–Doudoroff pathway, the TCA cycle — and hence PP_0897 — is central to energy conservation and precursor supply rather than to glycolytic flux per se.

**Active-site chemistry.** The catalytic engine is a [4Fe-4S] cluster ligated by three cysteines (predicted C66, C185, C277), with the fourth "unique" iron left open:

```
        Cys66  Cys185   Cys277           substrate
            \    |      /                  |
             [4Fe-4S] cluster ── Fe_unique ── O–C (S)-malate / fumarate
                                (Lewis acid)
```

The unique iron binds substrate bidentate and polarizes it as a Lewis acid, enabling stereospecific *anti* hydration/dehydration across the olefinic bond. This is the same chemistry demonstrated crystallographically for the *Leishmania major* enzyme and probed with the class-I-selective inhibitor 2-thiomalate. The solvent-exposed, redox-active cluster is the source of the enzyme's heat lability and oxygen sensitivity.

**Isozyme division of labor.** KT2440 hedges against the vulnerability of its class I enzyme by maintaining two iron-independent class II fumarases:

```
   Iron-replete, low oxidative stress   ──►  PP_0897 (class I, [4Fe-4S])  = primary
   Iron limitation / superoxide stress  ──►  PP_0944, PP_1755 (class II)  = robust backup
```

By analogy with the *E. coli* FumA/FumC system (SoxR-controlled induction of the class II enzyme under iron limitation and superoxide stress), the class II isozymes likely safeguard fumarase flux precisely when the class I cluster would be damaged. This makes PP_0897's physiological role **conditional and partly redundant**: it is the workhorse fumarase under favorable conditions, but not indispensable, because backup capacity exists. This is consistent with the general finding that many central-metabolic genes in KT2440 are only conditionally essential ([PMID: 20158506](https://pubmed.ncbi.nlm.nih.gov/20158506/)).

---

## Evidence Base

| PMID | Study (abbrev.) | How it supports the findings |
|---|---|---|
| [7592392](https://pubmed.ncbi.nlm.nih.gov/7592392/) | Oxygen, iron, carbon, superoxide control of *E. coli* fumA/fumC | Defines the three-fumarase system; distinguishes iron-containing class I (FumA/FumB) from iron-independent class II (FumC); establishes SoxR-dependent induction of class II under iron/superoxide stress (F001, F004, F005) |
| [31743022](https://pubmed.ncbi.nlm.nih.gov/31743022/) | Structural/biochemical study of a [4Fe-4S] fumarate hydratase | States class I FHs use a [4Fe-4S] cluster for the reversible reaction (F001) |
| [22569531](https://pubmed.ncbi.nlm.nih.gov/22569531/) | FH isoforms of *Leishmania major* | Confirms EC 4.2.1.2 and reversible fumarate ↔ (S)-malate; documents oxygen sensitivity; shows cytosolic/mitochondrial localization of class I FHs (F001, F002, F004) |
| [27528683](https://pubmed.ncbi.nlm.nih.gov/27528683/) | Crystal structure of *L. major* Fe-S FH | Shows substrate S-malate bound bidentate to the unique Fe of the [4Fe-4S] cluster; describes the novel dimeric "heart-shaped" two-domain fold; establishes the cluster is catalytically essential (F002, F003, F006) |
| [30645090](https://pubmed.ncbi.nlm.nih.gov/30645090/) | *L. major* FH with 2-thiomalate | Class I selectivity arises from inhibitor coordination to the unique Fe — present in class I, absent in class II human FH (F002) |
| [23405168](https://pubmed.ncbi.nlm.nih.gov/23405168/) | Biochemistry of *E. coli* FumA vs FumB | Characterizes the [4Fe-4S] class I enzymes PP_0897 is homologous to; reports reduction potential (~−290 mV), differential regulation, and secondary D-tartrate activity of FumB (F002, F003, F005, F006) |
| [20158506](https://pubmed.ncbi.nlm.nih.gov/20158506/) | Conditionally essential genes of KT2440 | Context for the conditional/redundant essentiality of central-metabolic genes in this organism (interpretation, F005) |

**How the evidence converges.** No primary study characterizes PP_0897 (Q88PF3) directly; the annotation is an inference from (i) the UniProt/InterPro record, (ii) high sequence identity to the experimentally characterized *E. coli* class I enzymes FumA/FumB, and (iii) crystallographic and mechanistic work on the structurally homologous *Leishmania major* class I FH. Every independent line — reaction chemistry, cofactor, fold, cluster-ligand topology, and isozyme complement — agrees. The literature corpus also contains many recent papers on mammalian FH in cancer and inflammation (e.g., fumarate/succination biology in renal cell carcinoma, colon cancer, and renal fibrosis). These concern the *class II* human enzyme and downstream fumarate signaling; while they reinforce the centrality of the fumarase reaction to metabolism, they are **not** direct evidence for the bacterial class I enzyme PP_0897 and were not used to support the mechanistic claims here.

---

## Limitations and Knowledge Gaps

1. **No direct experimental characterization of PP_0897.** There is, to date, no purified-protein biochemistry, crystal structure, EPR/Mössbauer cluster characterization, or knockout phenotype specifically for the *P. putida* KT2440 gene. All functional claims are inferences by homology (albeit strong ones).

2. **Cluster-ligand assignment is computational.** The C66/C185/C277 prediction rests on global sequence alignment to *E. coli* FumA. It has not been confirmed by structure or by site-directed mutagenesis. Alignment-based ligand mapping can be misled by insertions/deletions near the active site.

3. **Kinetic parameters are unknown.** K_m, k_cat, substrate specificity (including any secondary D-tartrate dehydratase activity as seen for FumB), and the exact reduction potential of PP_0897's cluster have not been measured.

4. **Regulation and isozyme division of labor are assumed, not demonstrated.** The proposed iron-/oxidative-stress-conditional role and the backup function of PP_0944/PP_1755 are extrapolated from the *E. coli* SoxR paradigm. KT2440 uses different regulatory circuitry (e.g., HexR governs much of its central carbon metabolism), and whether the three fumarases are differentially expressed across iron/oxygen/carbon conditions in KT2440 remains untested.

5. **Localization is inferred from sequence features.** The cytoplasmic assignment follows from the absence of signal/transmembrane features and general prokaryotic cell biology, not from a localization experiment.

6. **Quaternary structure is annotation-based.** The homodimer assignment follows InterPro/UniProt and homology to the "heart-shaped" dimeric class I fold; it has not been verified for PP_0897 (e.g., by size-exclusion chromatography or native mass spectrometry).

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant expression and anaerobic purification.** Express PP_0897 (with an affinity tag) in *E. coli* or *P. putida* under anaerobic/low-oxygen conditions to protect the [4Fe-4S] cluster; confirm cluster incorporation by UV-visible spectroscopy (~400 nm shoulder), iron/sulfide analysis, and EPR/Mössbauer.

2. **Steady-state kinetics.** Measure K_m and k_cat for fumarate hydration and (S)-malate dehydration; test for secondary D-tartrate dehydratase activity (as in FumB). Assess heat lability and O₂ sensitivity quantitatively to confirm the class I phenotype.

3. **Site-directed mutagenesis of predicted ligands.** Individually mutate C66, C185, and C277 to Ser/Ala and confirm loss of cluster and catalysis, while mutating C58 and C272 as negative controls, to test the F006 ligand-assignment prediction.

4. **Structure determination.** Solve the PP_0897 crystal or cryo-EM structure (ideally with bound (S)-malate or the 2-thiomalate inhibitor) to verify the fold, the dimeric assembly, and the substrate–unique-Fe coordination geometry.

5. **Genetic and physiological dissection of the three-fumarase system.** Construct single and combinatorial deletions of PP_0897, PP_0944, and PP_1755; assay growth on succinate/malate/fumarate and TCA-dependent carbon sources across iron-replete vs. iron-limited and oxidative-stress (paraquat) conditions to test the proposed conditional/redundant roles.

6. **Expression profiling.** Use RT-qPCR/RNA-seq to measure how the three fumarase genes respond to iron limitation, superoxide stress, and different carbon sources, and identify the regulators controlling them in KT2440 (e.g., relationship to HexR and iron/oxidative-stress regulons).

7. **Localization confirmation.** Verify cytoplasmic localization by cell fractionation or a fluorescent fusion, controlling for possible cluster/fusion artifacts.

---

## Gene Identity Verification

The gene symbol PP_0897, the organism (*Pseudomonas putida* KT2440, PSEPK; strain ATCC 47054 / DSM 6125 / NCIMB 11950 / KT2440), the protein family (class-I fumarase), and the domain architecture (Fe-S hydro-lyase TtdA-type + TtdB-type catalytic domains; PF05681 Fumerase; IPR011167 Fe-dependent fumarate hydratase) supplied in the research brief are mutually consistent and are corroborated by the sequence, structural, and biochemical evidence assembled above. There is no evidence of gene-symbol ambiguity for this locus. **PP_0897 (Q88PF3) is confidently annotated as the class I [4Fe-4S] fumarate hydratase of *P. putida* KT2440.**


## Artifacts

- [OpenScientist final report](PP_0897-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PP_0897-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:7592392
2. PMID:31743022
3. PMID:22569531
4. PMID:27528683
5. PMID:30645090
6. PMID:23405168
7. PMID:20158506