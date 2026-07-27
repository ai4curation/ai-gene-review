---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-26T20:22:24.575420'
end_time: '2026-07-26T21:22:00.332824'
duration_seconds: 3575.76
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: tgt
  gene_symbol: tgt
  uniprot_accession: Q88PL7
  protein_description: 'RecName: Full=Queuine tRNA-ribosyltransferase {ECO:0000255|HAMAP-Rule:MF_00168};
    EC=2.4.2.29 {ECO:0000255|HAMAP-Rule:MF_00168}; AltName: Full=Guanine insertion
    enzyme {ECO:0000255|HAMAP-Rule:MF_00168}; AltName: Full=tRNA-guanine transglycosylase
    {ECO:0000255|HAMAP-Rule:MF_00168};'
  gene_info: Name=tgt {ECO:0000255|HAMAP-Rule:MF_00168}; OrderedLocusNames=PP_0833;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the queuine tRNA-ribosyltransferase family.
  protein_domains: ArchSynthase1/Queuine_TRR. (IPR050076); TGT. (IPR004803); TGT-like_sf.
    (IPR036511); tRNA_ribo_trans-like. (IPR002616); TGT (PF01702)
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
citation_count: 12
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: tgt-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: tgt-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88PL7
- **Protein Description:** RecName: Full=Queuine tRNA-ribosyltransferase {ECO:0000255|HAMAP-Rule:MF_00168}; EC=2.4.2.29 {ECO:0000255|HAMAP-Rule:MF_00168}; AltName: Full=Guanine insertion enzyme {ECO:0000255|HAMAP-Rule:MF_00168}; AltName: Full=tRNA-guanine transglycosylase {ECO:0000255|HAMAP-Rule:MF_00168};
- **Gene Information:** Name=tgt {ECO:0000255|HAMAP-Rule:MF_00168}; OrderedLocusNames=PP_0833;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the queuine tRNA-ribosyltransferase family.
- **Key Domains:** ArchSynthase1/Queuine_TRR. (IPR050076); TGT. (IPR004803); TGT-like_sf. (IPR036511); tRNA_ribo_trans-like. (IPR002616); TGT (PF01702)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "tgt" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'tgt' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **tgt** (gene ID: tgt, UniProt: Q88PL7) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *tgt* (PP_0833, UniProt Q88PL7) in *Pseudomonas putida* KT2440

## Summary

The gene ***tgt*** (ordered locus **PP_0833**; UniProt **Q88PL7**) of *Pseudomonas putida* KT2440 encodes **queuine tRNA-ribosyltransferase (tRNA-guanine transglycosylase, TGT; EC 2.4.2.29)**, also known as the **guanine insertion enzyme**. This is a soluble, cytoplasmic, zinc-dependent enzyme that catalyzes the **committed first step of de novo queuosine (Q34) biosynthesis that operates on the tRNA substrate**. Specifically, TGT catalyzes an irreversible **base-exchange reaction**: it excises the genetically encoded guanine at the wobble position (**G34**) of tRNAs bearing **GUN anticodons** — the tRNAs for **Asp, Asn, His, and Tyr** — and replaces it with the modified 7-deazaguanine precursor **preQ₁ (7-aminomethyl-7-deazaguanine)**. The preQ₁-modified tRNA is subsequently matured to the hypermodified nucleoside **queuosine (Q34)** by downstream enzymes QueA and QueG.

There is **no *P. putida*-specific experimental study** of this enzyme. The functional annotation is therefore assigned by **strong orthology** to the biochemically and structurally characterized bacterial enzymes from *Escherichia coli* and *Zymomonas mobilis*, and is corroborated in this investigation by four independent, converging lines of computational evidence: (1) **complete conservation of every experimentally validated catalytic and zinc-binding residue** in Q88PL7 (69.8% identity to *E. coli* Tgt); (2) a **very-high-confidence AlphaFold structural model** (global pLDDT 96.6) that reproduces the (α/β)₈ TIM-barrel fold with an intact tetrahedral Cys₃His zinc site; (3) a **conserved *queA-tgt* operon** (PP_0832–PP_0833) mirroring the *E. coli* gene organization; and (4) a **complete de novo queuosine biosynthetic pathway** encoded in the KT2440 genome.

The functional significance of the reaction is that queuosine at the wobble position **fine-tunes decoding accuracy and translational speed** at NAU/NAC codons. Q34 is non-essential for viability but supports **translational fidelity and proteostasis**: loss of the modification, particularly in combination with the loss of other anticodon-loop modifications, increases codon misreading/frameshifting and promotes protein aggregation. The enzyme acts entirely in the **cytoplasm**, on tRNA, as a **homodimer** using a covalent enzyme–RNA catalytic intermediate anchored on a catalytic aspartate.

---

## Key Findings

### Finding 1 — TGT catalyzes base-exchange of guanine-34 for preQ₁ in GUN-anticodon tRNAs (the primary function)

The primary catalytic function of the *tgt* gene product is the **irreversible transglycosylation (base-exchange) of guanine at the tRNA wobble position (position 34)** for the premodified 7-deazaguanine base **preQ₁ (7-aminomethyl-7-deazaguanine)**. This reaction (EC 2.4.2.29) is the **committed insertion step of queuosine biosynthesis** and is specific to the four tRNA isoacceptors that carry a **GUN anticodon**: tRNA-Asp, tRNA-Asn, tRNA-His, and tRNA-Tyr. Mechanistically, the enzyme breaks the N-glycosidic bond of G34, releases free guanine, and forms a new glycosidic bond to preQ₁ at the same ribose. The product, preQ₁-tRNA, is not the final modification — preQ₁ is subsequently converted **at the tRNA level** to mature queuosine by the downstream enzymes QueA (forming epoxyqueuosine) and QueG (forming Q34).

The review by Reuter & Ficner (2025) states that TGTs "exchange a guanine base in the primary RNA transcript by various 7-substituted 7-deazaguanines leading to the modified nucleosides queuosine and archaeosine ... queuosine in the anticodon of bacterial and eukaryotic tRNAs specific for Asp, Asn, His and Tyr" ([PMID: 39956694](https://pubmed.ncbi.nlm.nih.gov/39956694/)). This directly establishes both the base-exchange chemistry and the anticodon (wobble) specificity for the four GUN-anticodon tRNAs.

The **substrate specificity for preQ₁** (over the earlier pathway intermediate preQ₀, 7-cyano-7-deazaguanine) is governed by active-site residues including a conserved cysteine (Cys158 in *Z. mobilis* numbering) and is gated by a general acid/base glutamate (Glu235). Tidten et al. (2007) confirmed the reaction identity — "Bacterial tRNA-guanine transglycosylase (Tgt) catalyses the exchange of guanine in the wobble position of particular tRNAs by the modified base preQ(0)" — and showed through kinetics and crystallography that preQ₁-over-preQ₀ selectivity is achieved through **higher catalytic turnover rather than tighter binding affinity** ([PMID: 17949745](https://pubmed.ncbi.nlm.nih.gov/17949745/)).

### Finding 2 — TGT is a homodimeric (β/α)₈ TIM-barrel zinc metalloenzyme using an aspartate-nucleophile covalent mechanism

The bacterial (queuosine-class) TGT catalytic domain folds into an **(α/β)₈ (TIM) barrel** carrying a **characteristic structural zinc-binding site**. Ishitani et al. (2002), in solving the archaeosine TGT structure, noted that "the N-terminal catalytic domain folds into an (alpha/beta)(8) barrel with a characteristic zinc-binding site, showing structural similarity with that of the bacterial queuosine TGT (QueTGT)" ([PMID: 12054814](https://pubmed.ncbi.nlm.nih.gov/12054814/)). The enzyme is a **functional homodimer**; while an isolated anticodon stem-loop bearing the UGU recognition motif serves as a minimal substrate, full-length tRNA binds with higher affinity through multiple contacts with the dimeric enzyme (Reuter & Ficner 2025, [PMID: 39956694](https://pubmed.ncbi.nlm.nih.gov/39956694/)).

Catalysis proceeds via a **covalent enzyme–RNA intermediate**. Xie, Liu & Huang (2003) chemically trapped and crystallized a *Z. mobilis* TGT covalent intermediate, showing that "the crystal structure of the TGT-RNA-9dzG ternary complex at a resolution of 2.9 A reveals, unexpectedly, that RNA is tethered to TGT through the side chain of Asp280. Thus, Asp280, instead of the previously proposed Asp102, acts as the nucleophile for the reaction" ([PMID: 12949492](https://pubmed.ncbi.nlm.nih.gov/12949492/)). The target nucleotide is flipped out of the anticodon loop into the active-site pocket. Heterocyclic-base recognition and general acid/base chemistry are handled by **Asp143** and **Glu235** (Todorov & Garcia 2006, [PMID: 16401090](https://pubmed.ncbi.nlm.nih.gov/16401090/); Tidten et al. 2007, [PMID: 17949745](https://pubmed.ncbi.nlm.nih.gov/17949745/)). Aspartate 143 in particular maintains anticodon identity: mutations invert the guanine-versus-xanthine recognition preference, confirming its role in preserving the correct wobble base-pairing properties.

### Finding 3 — TGT operates in the cytoplasmic de novo queuosine pathway; Q34 fine-tunes translation, and its loss impairs fidelity and proteostasis

In *E. coli*, *tgt* lies within a **queuosine biosynthesis gene cluster/operon together with *queA***, directly linking TGT to downstream Q maturation. Reuter et al. (1991) reported that "the genes are arranged in the following order: ORF 14 (transcribed in the counterclockwise direction), queA, tgt, and ORF 12" ([PMID: 1706703](https://pubmed.ncbi.nlm.nih.gov/1706703/)). TGT acts **before QueA**, which uses S-adenosylmethionine to transfer and isomerize a ribosyl moiety onto preQ₁-tRNA to form epoxyqueuosine (oQ). Slany et al. (1993) demonstrated that "the Q precursor (oQ), carrying a 2,3-epoxy-4,5-dihydroxycyclopentane ring, is formed from tRNA precursors containing 7-(aminomethyl)-7-deazaguanine (preQ1) by the queA gene product" ([PMID: 8347586](https://pubmed.ncbi.nlm.nih.gov/8347586/)), placing TGT's product squarely as the substrate for the next pathway enzyme. Both TGT and QueA act on the anticodon stem-loop, and their tRNA identity elements cluster in the anticodon region (Mueller & Slany 1995, [PMID: 7698334](https://pubmed.ncbi.nlm.nih.gov/7698334/); Iwata-Reuyl 2003 review, [PMID: 12697167](https://pubmed.ncbi.nlm.nih.gov/12697167/)).

Functionally, **Q34 is non-essential but fine-tunes translational speed and fidelity**. Sun et al. (2026) showed that "simultaneous absence of Q34 and ms2i6A37 increases +1 frameshifting at tyrosine codons and promotes protein aggregation, indicating impaired tRNATyr function" ([PMID: 42391044](https://pubmed.ncbi.nlm.nih.gov/42391044/)). This directly links TGT-dependent Q34 modification to **decoding accuracy (suppression of +1 frameshifting)** and **proteostasis (prevention of protein aggregation)**.

### Finding 4 — All catalytic and zinc-binding residues are conserved in Q88PL7, confirming a functional bacterial preQ₁-inserting TGT

Global pairwise alignment shows Q88PL7 (371 aa) is **69.8% identical to *E. coli* Tgt (P0A847)** and **54.8% identical to *Z. mobilis* Tgt (P28720)** — the two enzymes with solved crystal structures and full mechanistic characterization. Every experimentally validated functional residue maps to a conserved equivalent in the *P. putida* protein:

| Function | *Z. mobilis* / *E. coli* residue | *P. putida* (Q88PL7) equivalent |
|---|---|---|
| Catalytic nucleophile | Asp280 (Zm) / Asp280 (Ec) | **Asp262** |
| Heterocyclic base recognition | Asp143 (Ec) | **Asp143** |
| preQ₁ specificity (bacterial signature) | Cys145 (Ec) / Cys158 (Zm) | **Cys145** |
| Substrate-pocket specificity | Val233 (Zm) | **Val215** |
| General acid/base | Glu235 (Zm) | **Glu217** |
| Structural Zn ligand 1 | Cys318 (Zm) | **Cys300** |
| Structural Zn ligand 2 | Cys320 (Zm) | **Cys302** |
| Structural Zn ligand 3 | Cys323 (Zm) | **Cys305** |
| Structural Zn ligand 4 | His349 (Zm) | **His331** |

Critically, Q88PL7 carries a **cysteine (Cys145) at the specificity position** — the diagnostic **bacterial** residue that selects preQ₁ — rather than the valine found in eukaryotic queuine-inserting TGTs. Chen et al. (2011) established that "the Cys145 evolved in eubacterial TGTs to recognize preQ(1) but not queuine, whereas the eukaryal equivalent, Val161, evolved for increased recognition of queuine and a concomitantly decreased recognition of preQ(1)" ([PMID: 21131277](https://pubmed.ncbi.nlm.nih.gov/21131277/)). This confirms that Q88PL7 is a **bacterial, preQ₁-inserting** TGT (not a eukaryal queuine-inserting one), consistent with a de novo queuosine pathway. The role of the specificity cysteine and Val233 was further dissected by Biela et al. (2013), who showed by enzyme kinetics and X-ray crystallography that a Cys158Val mutation reduces preQ₁ affinity while a Val233Gly exchange enlarges the pocket to accommodate queuine ([PMID: 23704982](https://pubmed.ncbi.nlm.nih.gov/23704982/)).

### Finding 5 — PP_0833 sits in a *queA-tgt* operon within a complete de novo queuosine pathway in KT2440

Genomic analysis (KEGG, *P. putida* KT2440) shows **PP_0833** (*tgt*, K00773, EC 2.4.2.29; genomic coordinates 970,152–971,267, forward strand) is immediately preceded by **PP_0832 = *queA*** (K07568, S-adenosylmethionine:tRNA ribosyltransferase-isomerase; 969,088–970,137, forward strand, ~15 bp intergenic gap). This recapitulates the *E. coli* *queA-tgt* operon organization ([PMID: 1706703](https://pubmed.ncbi.nlm.nih.gov/1706703/)), supporting an operonic, co-regulated pathway context.

The **full de novo 7-deazaguanine/queuosine pathway is encoded** in the KT2440 genome:

| Step | Enzyme | KT2440 locus |
|---|---|---|
| GTP → 7,8-dihydroneopterin triphosphate | GTP cyclohydrolase I (FolE) | PP_1823, PP_2512 |
| → CPH₄ | QueD | PP_2341 |
| → CDG | QueE | PP_1225 |
| CDG → preQ₀ | QueC | PP_1226 (adjacent to queE) |
| preQ₀ → preQ₁ (base) | QueF | PP_2160 |
| **preQ₁ base → preQ₁-tRNA (G34 exchange)** | **TGT (this gene)** | **PP_0833** |
| preQ₁-tRNA → epoxyqueuosine-tRNA | QueA | PP_0832 |
| epoxyqueuosine-tRNA → queuosine-tRNA | QueG (epoxyQ reductase) | PP_4900 |

Notably, *queH* (the alternative Fe-S-dependent epoxyqueuosine reductase) is **absent**, consistent with *P. putida* using QueG for the final reduction step. The presence of a complete de novo pathway, including the preQ₁-synthesizing branch (FolE→QueD→QueE→QueC→QueF), confirms that *P. putida* **synthesizes queuosine de novo** and that TGT inserts an endogenously produced preQ₁ base.

### Finding 6 — The AlphaFold model of Q88PL7 confirms a folded TGT with an intact tetrahedral structural zinc site

The AlphaFold DB model of Q88PL7 (AF-Q88PL7-F1, v6) is **very high confidence**: global pLDDT **96.62**, with 93.3% of residues in the very-high-confidence band (pLDDT > 90) and 0% in the low/very-low bands. All nine mechanistically important residues identified by ortholog mapping are present and confidently modeled: Asp143 (95.9), Cys145 (89.4), Val215 (89.9), Glu217 (93.8), Asp262 nucleophile (97.9), and the four zinc ligands Cys300 (97.8), Cys302 (98.5), Cys305 (98.4), His331 (98.8).

The predicted zinc site forms a **compact tetrahedral coordination cage**: the ligand side-chain atoms (three Cys SG plus one His NE2) are all mutually 3.2–4.2 Å apart and converge on a common centroid within 2.4 Å — the geometry expected for a single Zn²⁺ ion coordinated with each ligand ~2.3 Å from the metal. The base-recognition residues Asp143 and Cys145 are adjacent (6.3 Å Cα–Cα), while the catalytic Asp262 and Glu217 sit across the substrate-binding cleft, consistent with a large active-site pocket that accommodates the flipped-out target nucleotide of the tRNA anticodon loop. This structural prediction matches the "characteristic zinc-binding site" of the TGT (α/β)₈ barrel defined by Ishitani et al. ([PMID: 12054814](https://pubmed.ncbi.nlm.nih.gov/12054814/)).

---

## Mechanistic Model / Interpretation

### The reaction catalyzed

```
                          TGT (PP_0833, Q88PL7)
                          homodimer, Zn2+, cytoplasm
                                    |
   tRNA(Asp/Asn/His/Tyr)           v            tRNA(Asp/Asn/His/Tyr)
   ...G34 (wobble)...  +  preQ1  -------->  ...preQ1-34...  +  guanine
        [GUN anticodon]        (base-exchange, irreversible)

   Mechanism: Asp262 nucleophile attacks C1' of G34 ribose ->
              covalent TGT-RNA intermediate + free guanine ->
              preQ1 attacks -> new N-glycosidic bond -> release
```

### Placement in the queuosine pathway

```
 GTP
  | FolE (PP_1823/PP_2512)
  v
 H2NTP --QueD(PP_2341)--> CPH4 --QueE(PP_1225)--> CDG --QueC(PP_1226)--> preQ0
                                                                          | QueF (PP_2160)
                                                                          v
                                                                        preQ1 (free base)
                                                                          |
                                    ============ TGT / PP_0833 ===========|
                                    | inserts preQ1 into tRNA G34         v
   tRNA-G34  ------------------------------------------------------>  tRNA-preQ1
                                                                          | QueA (PP_0832)  +SAM
                                                                          v
                                                                    tRNA-epoxyQ (oQ)
                                                                          | QueG (PP_4900)
                                                                          v
                                                                    tRNA-Q34 (queuosine)
```

TGT is the **gatekeeper that channels a small-molecule precursor (preQ₁) onto the tRNA polymer**. It is the only step at which the 7-deazaguanine core enters the tRNA; all subsequent chemistry (side-chain construction by QueA, epoxide reduction by QueG) occurs on the tRNA-bound base. Because the *queA* and *tgt* genes are adjacent and co-oriented (PP_0832–PP_0833), the two tRNA-level modification enzymes are likely **co-expressed**, ensuring that preQ₁-tRNA is efficiently handed off to QueA.

### Biological role and localization

TGT is a **soluble cytoplasmic enzyme** (no signal peptide, no transmembrane segments; it acts on cytoplasmic tRNA). Its biological output — queuosine at position 34 — modulates **wobble decoding** at NAU/NAC codon pairs read by the Asp/Asn/His/Tyr tRNAs. The modification is dispensable for growth under standard conditions but contributes to **translational fidelity** (suppressing +1 frameshifting) and **proteostasis** (limiting protein aggregation), particularly under conditions of combined anticodon-loop modification loss ([PMID: 42391044](https://pubmed.ncbi.nlm.nih.gov/42391044/)). In pathogenic relatives, bacterial Tgt is linked to efficient pathogenicity (e.g., *Shigella*), making it a validated antibacterial drug target ([PMID: 23704982](https://pubmed.ncbi.nlm.nih.gov/23704982/)); in the non-pathogenic soil/rhizosphere organism *P. putida* the enzyme's role is confined to the housekeeping fine-tuning of translation.

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports the annotation |
|---|---|---|
| [39956694](https://pubmed.ncbi.nlm.nih.gov/39956694/) | *RNA-modification by Base Exchange: Structure, Function and Application of TGTs* | Authoritative 2025 review; defines base-exchange chemistry and specificity for Asp/Asn/His/Tyr anticodon tRNAs |
| [17949745](https://pubmed.ncbi.nlm.nih.gov/17949745/) | *Glu vs Gln exchange swaps substrate selectivity in TGT* | Kinetics/crystallography of preQ₁/preQ₀ selectivity; role of Glu235 general acid/base |
| [12054814](https://pubmed.ncbi.nlm.nih.gov/12054814/) | *Crystal structure of archaeosine TGT* | Defines (α/β)₈ TIM-barrel fold + characteristic zinc site shared with bacterial QueTGT |
| [12949492](https://pubmed.ncbi.nlm.nih.gov/12949492/) | *Chemical trapping and crystal structure of TGT covalent intermediate* | Identifies Asp280 as catalytic nucleophile; covalent enzyme-RNA mechanism |
| [16401090](https://pubmed.ncbi.nlm.nih.gov/16401090/) | *Role of Asp143 in E. coli TGT* | Asp143 governs heterocyclic base recognition / anticodon identity |
| [21131277](https://pubmed.ncbi.nlm.nih.gov/21131277/) | *Evolution of eukaryal TGT* | Cys145 = bacterial preQ₁-specificity residue vs eukaryal Val161 (queuine); diagnostic for bacterial TGT |
| [23704982](https://pubmed.ncbi.nlm.nih.gov/23704982/) | *Specificity determinants in bacterial Tgt* | Dissects Cys158/Val233 specificity; drug-target relevance |
| [1706703](https://pubmed.ncbi.nlm.nih.gov/1706703/) | *E. coli queuine biosynthesis gene organization* | Establishes *queA-tgt* operon organization (mirrored in PP_0832–PP_0833) |
| [8347586](https://pubmed.ncbi.nlm.nih.gov/8347586/) | *Ribosyl moiety of AdoMet is precursor of queuine* | Shows preQ₁-tRNA (TGT product) is QueA substrate; pathway ordering |
| [7698334](https://pubmed.ncbi.nlm.nih.gov/7698334/) | *Interaction of Tgt and QueA with substrate tRNA* | tRNA identity elements cluster in anticodon; both enzymes accept anticodon stem-loop |
| [12697167](https://pubmed.ncbi.nlm.nih.gov/12697167/) | *Biosynthesis of 7-deazaguanosine nucleosides (review)* | Comprehensive pathway review; TGT and QueA as key enzymes |
| [42391044](https://pubmed.ncbi.nlm.nih.gov/42391044/) | *Defective Q and i6A/ms2i6A of tRNATyr cause frameshifting and aggregation* | Links Q34 loss to +1 frameshifting and protein aggregation (fidelity/proteostasis) |

**Consistency of evidence:** All twelve primary/review sources converge on the same enzymatic identity. No source contradicts the assignment. The only caveat is that all mechanistic and structural data derive from orthologs (*E. coli*, *Z. mobilis*, and *Pyrococcus furiosus* for the archaeal counterpart), not from *P. putida* itself — but the extremely high sequence identity (69.8% to *E. coli*), complete residue conservation, and high-confidence structural model make the orthology-based inference robust.

---

## Limitations and Knowledge Gaps

1. **No *P. putida*-specific experimental characterization.** There is no published biochemical, structural, kinetic, or genetic study of Q88PL7 / PP_0833. The functional assignment rests entirely on orthology and computational inference. No enzyme assay has directly demonstrated preQ₁ insertion by the *P. putida* protein, and no *P. putida* Δ*tgt* phenotype has been reported.

2. **Structural evidence is predictive, not experimental.** The zinc site, tetrahedral geometry, and residue positions come from an AlphaFold model, not an experimental crystal or cryo-EM structure. AlphaFold does not model the Zn²⁺ ion itself, substrate, or the tRNA complex; the "intact zinc site" is inferred from ligand side-chain geometry.

3. **tRNA substrate scope not verified in *P. putida*.** The GUN-anticodon (Asp/Asn/His/Tyr) specificity is assumed from orthology. The exact tRNA gene complement and any species-specific identity elements have not been experimentally mapped in KT2440.

4. **Pathway operation inferred from gene presence.** The complete de novo pathway is inferred from KEGG gene calls; flux through the pathway, actual queuosine content of *P. putida* tRNA, and regulation of the *queA-tgt* operon have not been measured.

5. **Quantitative kinetics unknown.** k_cat, K_m for preQ₁ and tRNA substrates, and the degree of preQ₁-over-preQ₀ selectivity in the *P. putida* enzyme are not measured; values are extrapolated from *E. coli*/*Z. mobilis*.

---

## Proposed Follow-up Experiments / Actions

1. **Direct enzymatic assay.** Heterologously express and purify Q88PL7, and assay guanine/preQ₁ base-exchange activity on in vitro-transcribed *P. putida* tRNA-Tyr/Asp (or the anticodon stem-loop), monitoring incorporation of radiolabeled or fluorescent preQ₁ and release of guanine. Determine k_cat and K_m.

2. **Genetic knockout and modification mapping.** Construct a *P. putida* KT2440 Δ*tgt* (ΔPP_0833) strain and quantify tRNA queuosine content by LC-MS/MS of digested total tRNA in wild-type vs mutant, confirming loss of Q34.

3. **Phenotypic characterization.** Test the Δ*tgt* strain for translational fidelity phenotypes (reporter-based +1 frameshifting/misreading assays) and proteostasis/aggregation, and probe stress conditions (oxidative, stationary phase, alternative carbon sources relevant to *P. putida* physiology).

4. **Operon regulation.** Verify co-transcription of PP_0832 (*queA*) and PP_0833 (*tgt*) by RT-PCR across the intergenic region, and map the promoter/transcription start site to confirm operonic organization.

5. **Structural validation.** Solve an experimental structure (X-ray/cryo-EM) of Q88PL7, ideally in complex with preQ₁ and/or a substrate anticodon stem-loop, to confirm the predicted zinc site and active-site geometry.

6. **Specificity confirmation.** Mutate Cys145→Val in the *P. putida* enzyme and test whether preQ₁ affinity/turnover drops (as predicted from ortholog studies), directly validating the bacterial-type specificity signature.

---

## Conclusion

The *tgt* gene (PP_0833, Q88PL7) of *Pseudomonas putida* KT2440 encodes a **bacterial queuosine-class tRNA-guanine transglycosylase (EC 2.4.2.29)**: a cytoplasmic, homodimeric, zinc-dependent (α/β)₈ TIM-barrel enzyme that irreversibly exchanges wobble-position guanine (G34) of GUN-anticodon tRNAs (Asp, Asn, His, Tyr) for the precursor base preQ₁ via a covalent aspartate-linked intermediate. It is the committed insertion step of de novo queuosine biosynthesis, feeding preQ₁-tRNA to the adjacent QueA (PP_0832) and downstream QueG (PP_4900). The resulting Q34 modification fine-tunes wobble decoding to support translational fidelity and proteostasis. This annotation is supported by strong orthology to biochemically and structurally characterized enzymes, complete conservation of all catalytic and zinc-binding residues (including the diagnostic bacterial preQ₁-specificity residue Cys145), a high-confidence AlphaFold model with an intact tetrahedral zinc site, and a complete genomic queuosine pathway — while no *P. putida*-specific experimental study yet exists.


## Artifacts

- [OpenScientist final report](tgt-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](tgt-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:39956694
2. PMID:17949745
3. PMID:12054814
4. PMID:12949492
5. PMID:16401090
6. PMID:1706703
7. PMID:8347586
8. PMID:7698334
9. PMID:12697167
10. PMID:42391044
11. PMID:21131277
12. PMID:23704982