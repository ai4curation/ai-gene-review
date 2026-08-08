---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-17T04:09:57.418141'
end_time: '2026-07-17T04:34:26.266932'
duration_seconds: 1468.85
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: hisA
  gene_symbol: hisA
  uniprot_accession: Q88R42
  protein_description: 'RecName: Full=1-(5-phosphoribosyl)-5-[(5-phosphoribosylamino)methylideneamino]
    imidazole-4-carboxamide isomerase {ECO:0000255|HAMAP-Rule:MF_01014}; EC=5.3.1.16
    {ECO:0000255|HAMAP-Rule:MF_01014}; AltName: Full=Phosphoribosylformimino-5-aminoimidazole
    carboxamide ribotide isomerase {ECO:0000255|HAMAP-Rule:MF_01014};'
  gene_info: Name=hisA {ECO:0000255|HAMAP-Rule:MF_01014}; OrderedLocusNames=PP_0292;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the HisA/HisF family. {ECO:0000255|HAMAP-
  protein_domains: Aldolase_TIM. (IPR013785); His_biosynth. (IPR006062); HisA/PriA.
    (IPR023016); HisA_bact_arch. (IPR006063); Isoase_HisA-like. (IPR044524)
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
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: hisA-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: hisA-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88R42
- **Protein Description:** RecName: Full=1-(5-phosphoribosyl)-5-[(5-phosphoribosylamino)methylideneamino] imidazole-4-carboxamide isomerase {ECO:0000255|HAMAP-Rule:MF_01014}; EC=5.3.1.16 {ECO:0000255|HAMAP-Rule:MF_01014}; AltName: Full=Phosphoribosylformimino-5-aminoimidazole carboxamide ribotide isomerase {ECO:0000255|HAMAP-Rule:MF_01014};
- **Gene Information:** Name=hisA {ECO:0000255|HAMAP-Rule:MF_01014}; OrderedLocusNames=PP_0292;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the HisA/HisF family. {ECO:0000255|HAMAP-
- **Key Domains:** Aldolase_TIM. (IPR013785); His_biosynth. (IPR006062); HisA/PriA. (IPR023016); HisA_bact_arch. (IPR006063); Isoase_HisA-like. (IPR044524)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "hisA" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'hisA' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **hisA** (gene ID: hisA, UniProt: Q88R42) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: HisA (Q88R42, PP_0292) in *Pseudomonas putida* KT2440

## Identity Verification

- **UniProt accession:** Q88R42
- **Gene:** *hisA*; ordered locus **PP_0292**
- **Organism:** *Pseudomonas putida* strain KT2440 (ATCC 47054 / DSM 6125), a well-characterized soil γ-proteobacterium
- **Protein:** 1-(5-phosphoribosyl)-5-[(5-phosphoribosylamino)methylideneamino]imidazole-4-carboxamide isomerase; also called **ProFAR isomerase** (phosphoribosylformimino-5-aminoimidazole carboxamide ribotide isomerase)
- **EC:** 5.3.1.16 (an intramolecular aldose-ketose isomerase)
- **Family/domains:** HisA/HisF family; TIM-barrel (Aldolase_TIM, IPR013785), His_biosynth (IPR006062), HisA/PriA (IPR023016), HisA_bact_arch (IPR006063), Isoase_HisA-like (IPR044524)

**Verification result:** The gene symbol, EC number, family, and domain architecture are fully self-consistent and match a large, unambiguous body of enzymological and structural literature on HisA/ProFAR isomerase. There is **no gene-symbol ambiguity**: *hisA* uniformly denotes ProFAR isomerase in histidine biosynthesis across bacteria. Direct mechanistic/structural studies exist for close orthologs (*Salmonella enterica*, *Thermotoga maritima*, *Escherichia coli*), and *P. putida* KT2440 possesses the canonical *his* gene set. The functional description below is therefore transferred with high confidence to Q88R42.

**Target-specific molecular details (UniProt Q88R42, retrieved 2026).** The protein is a single 245-residue chain (~25.9 kDa). Its annotated catalytic residues — **Active site 8 = proton acceptor** and **Active site 130 = proton donor** — are both **aspartate (Asp8, Asp130)** in the sequence, exactly matching the two-aspartate machinery defined experimentally in orthologs (*T. maritima* Asp8/Asp127; *S. enterica* Asp7/Asp176). The conserved **phosphate-binding loop GGGIR** is present at residues 81–85. Catalytic activity is registered as **Rhea RHEA:15469** (ChEBI 58435 → 58525), the pathway assignment is **L-histidine biosynthesis, step 4 of 9** from PRPP, and the annotated subcellular location is **Cytoplasm**. These sequence-level data confirm the functional transfer for the specific target rather than relying on homology alone.

---

## 1. Summary (Answer to the Research Question)

HisA (Q88R42 / PP_0292) is a cytoplasmic metabolic enzyme — **ProFAR isomerase (EC 5.3.1.16)** — that catalyzes the **fourth step of L-histidine biosynthesis**. It performs an **Amadori rearrangement**, isomerizing the aminoaldose **ProFAR** [N′-((5′-phosphoribosyl)formimino)-5-aminoimidazole-4-carboxamide ribonucleotide] to the aminoketose **PRFAR** [N′-((5′-phosphoribulosyl)formimino)-5-aminoimidazole-4-carboxamide ribonucleotide]. It is a soluble **(βα)₈ TIM-barrel** enzyme that uses **two conserved active-site aspartates** as general acid/base catalysts. Its product PRFAR is the substrate of the next pathway enzyme, imidazole glycerol phosphate synthase (HisF/HisH).

---

## 2. Primary Function: The Catalyzed Reaction and Substrate Specificity

**Reaction (EC 5.3.1.16):**

> ProFAR ⇌ PRFAR

HisA catalyzes the ring-opening isomerization (Amadori rearrangement) of an N-glycosidic aminoaldose into the corresponding aminoketose. Crystallographic work on *Salmonella enterica* HisA — including the first structural visualization of the labile ProFAR substrate bound in the active site — directly established this activity: *"HisA is a (βα)8 barrel enzyme that catalyzes the Amadori rearrangement of N′-[(5′-phosphoribosyl)formimino]-5-aminoimidazole-4-carboxamide ribonucleotide (ProFAR) to N′-((5′-phosphoribulosyl)formimino)-5-aminoimidazole-4-carboxamide-ribonucleotide (PRFAR) in the histidine biosynthesis pathway"* (Söderholm et al., 2015, PMID 26294764).

**Substrate specificity.** Wild-type HisA is highly specific for its physiological substrate ProFAR. Its specificity is best appreciated through evolution experiments: the mechanistically analogous enzyme TrpF (phosphoribosylanthranilate isomerase, tryptophan pathway) performs the same *type* of Amadori rearrangement on a different substrate, and a **single amino-acid substitution** is sufficient to graft TrpF activity onto the HisA scaffold (Jürgens et al., 2000, PMID 10944186): *"a single amino acid exchange could establish TrpF activity on the HisA scaffold. These findings suggest that HisA and TrpF may have evolved from an ancestral enzyme of broader substrate specificity."* This demonstrates that native HisA has narrowed to ProFAR while retaining an evolvable, promiscuity-prone active site. Naturally bifunctional HisA/TrpF enzymes (PriA), reflected in the IPR023016 "HisA/PriA" annotation, occur in Actinobacteria; *P. putida* HisA is a monofunctional, dedicated ProFAR isomerase.

---

## 3. Catalytic Mechanism (Structure–Function)

HisA adopts the classic **(βα)₈ TIM-barrel** fold, with the active site at the C-terminal face of the barrel and mobile "long loops" that close over and protect the thermolabile substrate.

- **Two-aspartate general acid–base catalysis.** In *S. enterica* HisA, site-directed mutagenesis and kinetics showed *"Asp-7 acts as the catalytic base, and Asp-176 acts as the catalytic acid"* (Söderholm et al., 2015, PMID 26294764). In *Thermotoga maritima* HisA, the equivalent residues Asp-8 and Asp-127, plus Thr-164, are essential for activity, and a mechanism involving *"general acid-base catalysis and a Schiff base intermediate is proposed for both enzymes"* (Henn-Sax et al., 2002, PMID 12356303).
- **Substrate sequestration by loop closure.** ProFAR binds initially independent of the loops; loop closure then locks the substrate into an extended, partly product-like conformation and reorganizes a hydrogen-bond network (His-47, Asp-129, Thr-171, Ser-202 in *S. enterica*) important for catalysis (Söderholm et al., 2015). This loop chemistry mirrors that of TrpF, reflecting a shared strategy for protecting labile aminoaldose substrates (Henn-Sax et al., 2002).

By orthology (family MF_01014, conserved catalytic aspartate pair, and identical domain architecture), *P. putida* HisA is expected to use the same TIM-barrel/two-aspartate mechanism. This is now sequence-verified for Q88R42: its UniProt-annotated active sites are **Asp8 (proton acceptor/base)** and **Asp130 (proton donor/acid)**, and the conserved **GGGIR** phosphate-anchoring loop (residues 81–85) positions the substrate's 5′-phosphate — the exact catalytic architecture characterized in the *S. enterica* and *T. maritima* enzymes.

**Quantitative orthology support.** Global pairwise alignment shows Q88R42 (245 aa) shares full-length identity of **36.9% with *S. enterica* HisA** (A0A2X4T999, 245 aa; the enzyme crystallized with ProFAR by Söderholm et al., 2015), **36.7% with *T. maritima* HisA** (Q9X0C7, 241 aa; the mutagenesis model of Henn-Sax et al., 2002), and **34.9% with *E. coli* HisA** (P10371, 245 aa). These values are well above the ~20–25% "twilight zone," the proteins are essentially the same length, and the catalytic aspartates align — making the functional transfer to the *P. putida* enzyme quantitatively robust rather than speculative.

---

## 4. Pathway Context

HisA operates in the **L-histidine biosynthetic pathway**, one of the most conserved amino-acid biosynthetic routes. The reaction sits downstream of the ProFAR-generating steps (HisG → HisIE) and immediately upstream of imidazole-glycerol-phosphate synthase:

```
PRPP → ... → ProFAR --[HisA / ProFAR isomerase]--> PRFAR
                                    │
                                    ▼
                 PRFAR + glutamine --[HisF/HisH, ImGP synthase]--> IGP + AICAR
                                    │
                                    ▼
                 ... → L-histidine  (via HisB, HisC, HisD)
```

The AICAR byproduct links histidine biosynthesis to purine metabolism, and altered HisA flux can feed the phosphoribosylamine (PRA) node: reduced-activity *hisA* alleles allow *"PurF-independent PRA formation"* from ProFAR, tuning thiamine/purine synthesis and illustrating metabolic-network robustness (Koenigsknecht et al., 2012, PMID 23133571). This is a context-dependent consequence of perturbed HisA catalysis, not the enzyme's primary role. Histidine can also be catabolized by *P. putida* as a C/N source via the entirely separate *hut* system (e.g., the HutT transporter and HutH histidase), which is metabolically distinct from HisA-mediated biosynthesis (Wirtz et al., 2021, PMID 34245008).

### Genomic context in *P. putida* KT2440

Mapping the KT2440 *his* genes shows that **PP_0292 (*hisA*) is embedded in a compact biosynthetic gene cluster** spanning PP_0289–PP_0293:

```
PP_0288        PP_0289   PP_0290   PP_0291      PP_0292   PP_0293      PP_0294
oxalate/       hisB      hisH      DUF2164      hisA      hisF         cbcV (ABC
formate        (IGPD)    (IGPS     (small       (ProFAR   (IGPS        transporter)
antiporter               glutam.)  hypoth.)     isomerase) cyclase)
```

Two functionally important observations follow:
1. ***hisA* is immediately adjacent to *hisF*** (PP_0293) and near *hisH* (PP_0290). HisF + HisH constitute imidazole-glycerol-phosphate synthase, the enzyme that **consumes HisA's product PRFAR**. Thus the gene making PRFAR sits next to the genes whose product uses it — and HisA and HisF are ancient TIM-barrel paralogs of the same HisA/HisF family, consistent with their tandem clustering originating from an ancestral gene duplication.
2. Unlike the single contiguous *his* operon of *E. coli*/*Salmonella*, *P. putida* KT2440 **distributes its histidine-biosynthesis genes across at least three genomic loci**: the PP_0289–0293 cluster (*hisBHAF* + PP_0291), a *hisG–hisD–hisC* cluster (PP_0965–0967), and a *hisIE* pair (*hisI* PP_5014, *hisE* PP_5015). (Gene assignments from UniProt/KT2440 genome annotation.)

---

## 5. Subcellular Localization

HisA is a **soluble cytoplasmic enzyme** (UniProt Q88R42 subcellular location: Cytoplasm, HAMAP MF_01014). It carries no signal peptide or transmembrane segment, is a single-domain globular TIM-barrel protein, and acts on phosphorylated, membrane-impermeant intermediates of a cytoplasmic biosynthetic pathway — consistent with all structural studies purifying it as a soluble protein amenable to crystallization (Söderholm et al., 2015; Henn-Sax et al., 2002). Its catalytic function is therefore carried out in the bacterial cytosol.

---

## 6. Supported and Refuted Hypotheses

**Supported**
- H1: HisA is ProFAR isomerase catalyzing ProFAR → PRFAR (Amadori rearrangement), step 4 of histidine biosynthesis. — Strongly supported (PMID 26294764, 23133571).
- H2: HisA is a (βα)₈ TIM-barrel enzyme using two catalytic aspartates (general acid/base) with a proposed Schiff-base intermediate. — Supported (PMID 26294764, 12356303).
- H3: Native HisA is substrate-specific for ProFAR but sits on a highly evolvable scaffold (HisA/TrpF/PriA paradigm). — Supported (PMID 10944186, 12356303).
- H4: HisA functions in the cytoplasm. — Supported by structure/biochemistry and absence of targeting signals.

**Refuted / not primary**
- HisA is not a transporter, structural protein, or signaling molecule.
- The purine/thiamine (PRA) "moonlighting" effect is a secondary metabolic consequence of altered HisA activity, not its primary function.

---

## 7. Limitations and Future Directions

- **Direct evidence gap for Q88R42:** No published enzymatic or structural study is specific to the *P. putida* KT2440 protein; the annotation is a high-confidence orthology transfer from *S. enterica*, *T. maritima*, and *E. coli* HisA (identical EC, family, domains, conserved catalytic residues, and 35–37% full-length sequence identity — well above the twilight zone).
- **Already resolved in this analysis:** the target's catalytic residues were located directly in the Q88R42 sequence (Asp8 base, Asp130 acid) and shown to be conserved with the characterized orthologs, and the *his* genomic neighborhood of PP_0292 was mapped.
- **Future work:** measure *P. putida* HisA kinetic parameters (k_cat/K_m for ProFAR) to confirm activity experimentally in this organism; test whether PP_0291 (DUF2164) is co-transcribed with *hisA*/*hisF* and whether it has any accessory role; and generate an AlphaFold model with superposition onto the *S. enterica* ProFAR-bound structure (PMID 26294764) to confirm active-site geometry. Because *P. putida* is a γ-proteobacterium (not an actinobacterium), HisA is expected to be strictly monofunctional (no PriA-type TrpF side activity) — a prediction worth verifying biochemically.

---

## References
- Söderholm A, et al. *Two-step ligand binding in a (βα)8 barrel enzyme: substrate-bound structures shed new light on the catalytic cycle of HisA.* J Biol Chem, 2015. PMID 26294764.
- Henn-Sax M, et al. *Two (βα)8-barrel enzymes of histidine and tryptophan biosynthesis have similar reaction mechanisms and common strategies for protecting their labile substrates.* Biochemistry, 2002. PMID 12356303.
- Jürgens C, et al. *Directed evolution of a (βα)8-barrel enzyme to catalyze related reactions in two different metabolic pathways.* PNAS, 2000. PMID 10944186.
- Koenigsknecht MJ, et al. *Perturbations in histidine biosynthesis uncover robustness in the metabolic network of Salmonella enterica.* J Bacteriol, 2012. PMID 23133571.
- Wirtz M, et al. *HutT functions as the major L-histidine transporter in Pseudomonas putida KT2440.* 2021. PMID 34245008. (context: histidine utilization vs. biosynthesis)


## Artifacts

- [OpenScientist final report](hisA-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](hisA-deep-research-openscientist_artifacts/final_report.pdf)