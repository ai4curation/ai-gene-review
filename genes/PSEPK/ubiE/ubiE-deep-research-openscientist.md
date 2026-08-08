---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-18T17:53:44.072926'
end_time: '2026-07-18T19:37:20.671753'
duration_seconds: 6216.6
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: ubiE
  gene_symbol: ubiE
  uniprot_accession: Q88D17
  protein_description: 'RecName: Full=Ubiquinone/menaquinone biosynthesis C-methyltransferase
    UbiE {ECO:0000255|HAMAP-Rule:MF_01813}; EC=2.1.1.163 {ECO:0000255|HAMAP-Rule:MF_01813};
    EC=2.1.1.201 {ECO:0000255|HAMAP-Rule:MF_01813}; AltName: Full=2-methoxy-6-polyprenyl-1,4-benzoquinol
    methylase {ECO:0000255|HAMAP-Rule:MF_01813}; AltName: Full=Demethylmenaquinone
    methyltransferase {ECO:0000255|HAMAP-Rule:MF_01813};'
  gene_info: Name=ubiE {ECO:0000255|HAMAP-Rule:MF_01813}; OrderedLocusNames=PP_5011;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the class I-like SAM-binding methyltransferase
  protein_domains: SAM-dependent_MTases_sf. (IPR029063); UbiE/COQ5_MeTrFase. (IPR004033);
    UbiE/COQ5_MeTrFase_CS. (IPR023576); Ubie_methyltran (PF01209)
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
citation_count: 13
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: ubiE-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: ubiE-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88D17
- **Protein Description:** RecName: Full=Ubiquinone/menaquinone biosynthesis C-methyltransferase UbiE {ECO:0000255|HAMAP-Rule:MF_01813}; EC=2.1.1.163 {ECO:0000255|HAMAP-Rule:MF_01813}; EC=2.1.1.201 {ECO:0000255|HAMAP-Rule:MF_01813}; AltName: Full=2-methoxy-6-polyprenyl-1,4-benzoquinol methylase {ECO:0000255|HAMAP-Rule:MF_01813}; AltName: Full=Demethylmenaquinone methyltransferase {ECO:0000255|HAMAP-Rule:MF_01813};
- **Gene Information:** Name=ubiE {ECO:0000255|HAMAP-Rule:MF_01813}; OrderedLocusNames=PP_5011;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the class I-like SAM-binding methyltransferase
- **Key Domains:** SAM-dependent_MTases_sf. (IPR029063); UbiE/COQ5_MeTrFase. (IPR004033); UbiE/COQ5_MeTrFase_CS. (IPR023576); Ubie_methyltran (PF01209)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ubiE" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ubiE' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ubiE** (gene ID: ubiE, UniProt: Q88D17) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: UbiE (Q88D17, PP_5011) in *Pseudomonas putida* KT2440

**Gene:** *ubiE* (Ordered locus PP_5011) · **UniProt:** Q88D17 · **Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / KT2440) · **EC:** 2.1.1.201 and 2.1.1.163

---

## Summary

**UbiE (UniProt Q88D17, ordered locus PP_5011) of *Pseudomonas putida* KT2440 is a cytoplasmic, S-adenosyl-L-methionine (SAM)–dependent class I C-methyltransferase that catalyzes a single, chemically distinctive ring carbon-methylation step shared by two respiratory-quinone biosynthetic pathways.** In the ubiquinone (coenzyme Q, CoQ) pathway it acts as 2-methoxy-6-polyprenyl-1,4-benzoquinol methylase (EC 2.1.1.201), transferring a methyl group from SAM to the C5 position of the quinone ring. In the menaquinone (vitamin K2) pathway the same enzyme acts as demethylmenaquinone methyltransferase (EC 2.1.1.163), converting demethylmenaquinone (DMK) to menaquinone (MK). This dual EC assignment and the "bifunctional" description are directly encoded in the UniProt record and are firmly supported by classical genetics in the model organism *Escherichia coli*, where loss of *ubiE* abolishes the C-methylation step in **both** quinone pathways.

The gene symbol and protein identity are unambiguous and internally consistent. The organism (*P. putida* KT2440), the gene name (*ubiE*), the family assignment (class I-like SAM-binding methyltransferase; UbiE/COQ5 family; Pfam PF01209; InterPro IPR004033/IPR023576/IPR029063), and the two EC activities all point to one well-defined enzyme. There is no evidence of a symbol clash: "ubiE" reliably denotes the ubiquinone/menaquinone biosynthesis C-methyltransferase across γ-proteobacteria. While no *P. putida*-specific enzymology study of UbiE was located, the functional assignment is transferred with high confidence from the experimentally characterized *E. coli* UbiE (72.6% sequence identity) and the crystallographically characterized yeast ortholog Coq5 (~44–47% identity), whose catalytic residues and SAM-binding motifs are conserved in Q88D17.

Mechanistically and physiologically, UbiE operates in a **soluble cytoplasmic "Ubi" metabolon** — a ~1-MDa multienzyme complex that carries out the last several ring-modification reactions of CoQ biosynthesis — rather than as a membrane-embedded enzyme. In *P. putida*, an obligate aerobe, the dominant end-product of the pathway is **ubiquinone-9 (UQ9)**, the redox-active carrier that feeds electrons into a **branched aerobic respiratory chain** terminating at multiple ubiquinol oxidases (cytochrome *bo₃*/Cyo, the cyanide-insensitive oxidase CIO, and *cbb₃*/*aa₃*-type oxidases). Beyond bioenergetics, the ubiquinone pool serves as a redox signal sensed by the hybrid sensor kinase HskA, linking UbiE's metabolic output to regulatory remodeling of the respiratory chain in response to oxygen availability.

---

## Key Findings

### 1. UbiE is a bifunctional SAM-dependent C-methyltransferase serving both ubiquinone and menaquinone biosynthesis

The core identity of UbiE is that of a single enzyme catalyzing the same class of chemistry — SAM-dependent carbon methylation of an aromatic quinone ring — in two distinct pathways. The UniProt record for Q88D17 annotates two enzyme activities: **EC 2.1.1.201** (2-methoxy-6-polyprenyl-1,4-benzoquinol methylase, the ubiquinone pathway) and **EC 2.1.1.163** (demethylmenaquinone methyltransferase, the menaquinone pathway). The protein is 256 amino acids and adopts the class I SAM-methyltransferase fold.

This dual role was established genetically in *E. coli*. Strains carrying *ubiE* mutations "are not able to catalyze the carbon methylation reaction in the biosynthesis of ubiquinone (coenzyme Q) and menaquinone (vitamin K2), essential isoprenoid quinone components of the respiratory electron transport chain" ([PMID: 9045837](https://pubmed.ncbi.nlm.nih.gov/9045837/)). A second study independently confirms that "the *ubiE* gene encodes a C-methyltransferase required for the synthesis of both CoQ and menaquinone" ([PMID: 10960098](https://pubmed.ncbi.nlm.nih.gov/10960098/)). The convergence of the UniProt EC assignments with two independent genetic reports makes this the highest-confidence claim in the report.

### 2. Loss of UbiE causes accumulation of defined pathway intermediates and a respiratory-growth defect

The metabolic consequence of UbiE loss provides a precise readout of which reaction it catalyzes. In *E. coli*, both a *ubiE* disruption and the point mutant **ubiE401 (Gly142→Asp)** accumulate **2-octaprenyl-6-methoxy-1,4-benzoquinone** — the immediate substrate of the ubiquinone C-methylation — and **demethylmenaquinone (DMK)** — the substrate of the menaquinone C-methylation. These mutants fail to grow on succinate, a non-fermentable carbon source that requires a functional aerobic respiratory chain ([PMID: 9045837](https://pubmed.ncbi.nlm.nih.gov/9045837/)).

The *ubiE401* allele is mechanistically informative: "DNA sequence analysis of the *ubiE401* allele identified a missense mutation resulting in the amino acid substitution of Asp for Gly142" ([PMID: 9045837](https://pubmed.ncbi.nlm.nih.gov/9045837/)). This glycine lies in the conserved glycine-rich loop characteristic of SAM-binding class I methyltransferases; substituting a bulky, charged aspartate for it is expected to disrupt cofactor binding, explaining the loss of function. The substrate-accumulation phenotype directly demonstrates that UbiE acts **at** the C-methylation node — upstream substrates pile up because the methyl-transfer step is blocked.

### 3. UbiE acts within a soluble cytoplasmic Ubi metabolon, not a membrane-bound complex

A key advance in understanding where UbiE does its work came from the demonstration that CoQ biosynthesis in *E. coli* is carried out by a soluble multienzyme assembly. "Seven Ubi proteins form the Ubi complex, a stable metabolon that catalyzes the last six reactions of the UQ biosynthetic pathway in *Escherichia coli*" ([PMID: 30686758](https://pubmed.ncbi.nlm.nih.gov/30686758/)). Crucially, "we purify the Ubi complex from cytoplasmic extracts and demonstrate that UQ biosynthesis occurs in this fraction, challenging the current thinking of a membrane-associated biosynthetic process" ([PMID: 30686758](https://pubmed.ncbi.nlm.nih.gov/30686758/)).

This finding localizes UbiE's catalytic activity to the **cytoplasm**, where the hydrophobic polyprenyl-quinone intermediates are handled by the SCP2 lipid-binding domain of the accessory protein UbiJ, keeping otherwise membrane-partitioning substrates soluble and channeled between active sites. UbiE, as the C-methyltransferase of this pathway, is a member of this metabolon, and its reaction is one of the sequential ring modifications performed within the complex. This reframes the classical textbook picture of quinone biosynthesis as a purely membrane-bound process.

### 4. UbiE belongs to the class I SAM-binding methyltransferase family (UbiE/COQ5), homologous to yeast Coq5

Q88D17 carries the diagnostic sequence hallmarks of a class I (Rossmann-fold) SAM-dependent methyltransferase. The 256-residue protein contains the SAM-binding **motif I** (visible as the sequence "DIAGGTGD" around residues 72–79), with UniProt-annotated SAM-contact residues at positions 79, 100, and 128–129. Its domain complement — InterPro **IPR004033** (UbiE/COQ5_MeTrFase), **IPR023576** (UbiE/COQ5 conserved site), **IPR029063** (SAM-dependent MTase superfamily) and Pfam **PF01209** (Ubie_methyltran) — places it firmly in the UbiE/COQ5 subfamily.

The eukaryotic ortholog, yeast Coq5, anchors the functional interpretation: it shares "44% sequence identity over 262 amino acids to UbiE, which is required for a C-methyltransferase step in the Q and menaquinone biosynthetic pathways in *Escherichia coli*" ([PMID: 9083049](https://pubmed.ncbi.nlm.nih.gov/9083049/)), and "both the *ubiE* and *COQ5* coding sequences contain sequence motifs common to a wide variety of S-adenosyl-L-methionine-dependent methyltransferases" ([PMID: 9083049](https://pubmed.ncbi.nlm.nih.gov/9083049/)). Coq5 is a mitochondrial C-methyltransferase in eukaryotic Q biosynthesis — the compartment-specific counterpart of bacterial UbiE.

### 5. *P. putida* UbiE is a close ortholog (72.6% identity) of the experimentally characterized *E. coli* UbiE

Because no direct enzymology on *P. putida* UbiE was found, the strength of the functional transfer rests on orthology. A Needleman–Wunsch global alignment of Q88D17 (256 aa) against *E. coli* UbiE (P0A887, 251 aa) gives **180/248 = 72.6% identity** over aligned columns — well above the ~40% threshold generally considered sufficient to transfer detailed enzymatic function. Critically, the functionally essential regions are conserved: the class I SAM-MTase motif I ("DIAGGTGD") and the catalytic glycine-rich loop (*E. coli* "…SFGLRNV…" ≈ *P. putida* "…AFGLRNV…") that contains the very glycine whose mutation (Gly142→Asp) inactivates *E. coli* UbiE. Conservation of both the cofactor-binding and catalytic elements makes it near-certain that *P. putida* UbiE performs the identical chemistry.

### 6. UbiE catalyzes the ring C-methylation step within a super-structured, multi-enzyme Ubi pathway

Authoritative reviews place UbiE's reaction in the context of an ordered series of ring modifications carried out by physically associated enzymes. "Studies in model microorganisms elucidated the details of CoQ biosynthesis and revealed the existence of multiprotein complexes composed of several enzymes that catalyze consecutive reactions in the CoQ pathways of *Saccharomyces cerevisiae* and *Escherichia coli*" ([PMID: 35178585](https://pubmed.ncbi.nlm.nih.gov/35178585/)). UbiE performs the **sole C-methylation** of the pathway: in ubiquinone synthesis it methylates 2-methoxy-6-polyprenyl-1,4-benzoquinol (EC 2.1.1.201); in menaquinone synthesis it methylates demethylmenaquinone to menaquinone (EC 2.1.1.163). The end-product, ubiquinone, "functions in the respiratory electron transport chain and plays a pivotal role in energy generating processes" ([PMID: 24480387](https://pubmed.ncbi.nlm.nih.gov/24480387/)).

### 7. Structural and mechanistic basis: a class I SAM-MTase adding the ring methyl at C5

The crystallographic characterization of the yeast ortholog Coq5 provides an atomic-resolution model for UbiE's mechanism. Coq5 "is an S-adenosyl methionine (SAM)-dependent methyltransferase (SAM-MTase) that catalyzes the only C-methylation step in the coenzyme Q (CoQ) biosynthesis pathway, in which 2-methoxy-6-polyprenyl-1,4-benzoquinone (DDMQH2) is converted to 2-methoxy-5-methyl-6-polyprenyl-1,4-benzoquinone (DMQH2)" ([PMID: 25084328](https://pubmed.ncbi.nlm.nih.gov/25084328/)). Structurally, "Coq5 displays a typical class I SAM-MTase structure with two minor variations beyond the core domain, both of which are considered to participate in dimerization and/or substrate recognition" ([PMID: 25084328](https://pubmed.ncbi.nlm.nih.gov/25084328/)). This defines the exact regiochemistry: the methyl group is installed at **C5** of the quinone ring.

Direct functional equivalence between UbiE and Coq5 was proven by cross-species complementation: among yeast *coq5* point mutants, "only the *coq5-2* and *coq5-5* mutants are rescued by expression of *Escherichia coli ubiE*, a homolog of *COQ5*" ([PMID: 14701817](https://pubmed.ncbi.nlm.nih.gov/14701817/)). The ability of bacterial UbiE to substitute for eukaryotic Coq5 in vivo confirms that the two enzymes catalyze the same reaction on chemically analogous substrates.

### 8. The proposed catalytic general base is conserved in *P. putida* UbiE (Arg149 ≡ Coq5 Arg201)

A putative catalytic mechanism for the family was proposed from the Coq5 structure: "Arg201 acts as a general base to initiate catalysis with the help of a water molecule" ([PMID: 25084328](https://pubmed.ncbi.nlm.nih.gov/25084328/)). Pairwise alignment of yeast Coq5 (P49017) against *P. putida* UbiE (Q88D17) — 47.1% identity over 255 columns, consistent with the ~44% Coq5–*E. coli* UbiE figure — maps this catalytic Arg201 onto a conserved **Arg149** in *P. putida* UbiE. Together with the conserved SAM-binding residues (positions 79, 100, 128–129) and motif I ("DIAGGTGD"), the full catalytic apparatus predicted from structural studies is present in Q88D17, completing the case that it is a fully functional C-methyltransferase.

### 9. Physiological output: UbiE-derived ubiquinone-9 powers a branched aerobic respiratory chain

In *P. putida*, the metabolic product of UbiE's activity feeds directly into respiration. The species uses **ubiquinone-9 (UQ9)** as its dominant respiratory quinone ([PMID: 11359512](https://pubmed.ncbi.nlm.nih.gov/11359512/); [PMID: 18323682](https://pubmed.ncbi.nlm.nih.gov/18323682/)). *P. putida* KT2440 "contains a branched aerobic respiratory chain with several terminal oxidases" ([PMID: 16958757](https://pubmed.ncbi.nlm.nih.gov/16958757/)) — including the cytochrome *bo₃* (Cyo) **ubiquinol oxidase**, the cyanide-insensitive oxidase (CIO), and *cbb₃*-1/*cbb₃*-2/*aa₃*-type oxidases ([PMID: 18341582](https://pubmed.ncbi.nlm.nih.gov/18341582/)). These terminal oxidases oxidize ubiquinol, the reduced form of the very quinone pool UbiE helps build, closing the loop between quinone biosynthesis and energy conservation.

### 10. UbiE output as a redox signal and operon context

Beyond serving as an electron carrier, the ubiquinone pool acts as a signaling molecule in *P. putida*. The hybrid sensor kinase HskA senses the ubiquinone oxidation state: "HskA autophosphorylation is inhibited by ubiquinone but not by ubiquinol, its reduced derivative" ([PMID: 24249291](https://pubmed.ncbi.nlm.nih.gov/24249291/)), linking the UbiE-produced quinone pool to regulatory remodeling of the electron transport chain in response to oxygen availability. In terms of genomic context, *ubiE* lies in a conserved operon: it is described as being co-located in an operon containing *ubiE*, *yigP* (*ubiJ*), and *ubiB* ([PMID: 10960098](https://pubmed.ncbi.nlm.nih.gov/10960098/)) — a gene neighborhood that co-encodes members of the same Ubi metabolon.

---

## Mechanistic Model / Interpretation

### The reaction catalyzed

UbiE installs a methyl group directly onto a ring **carbon** of a polyprenylated quinone/quinol, using SAM as the methyl donor and producing S-adenosyl-L-homocysteine (SAH) as the by-product. It performs this same C-methylation chemistry in two pathways:

```
UBIQUINONE (CoQ) PATHWAY  — EC 2.1.1.201
  2-methoxy-6-polyprenyl-1,4-benzoquinol   ──UbiE (SAM)──►  2-methoxy-5-methyl-6-polyprenyl-1,4-benzoquinol
  (DDMQH2)                                  + SAM → + SAH     (DMQH2)
                                                             methyl added at ring C5

MENAQUINONE (MK) PATHWAY  — EC 2.1.1.163
  demethylmenaquinone (DMK)                ──UbiE (SAM)──►  menaquinone (MK / vitamin K2)
                                            + SAM → + SAH
```

UbiE is the **only** C-methyltransferase of the CoQ pathway; all other ring modifications are hydroxylations, decarboxylation, or O-methylations carried out by other Ubi enzymes. This makes UbiE a non-redundant, essential node for building a mature respiratory quinone.

### Where it acts: the soluble Ubi metabolon

```
        CYTOPLASM
   ┌─────────────────────────────────────────────────┐
   │   Ubi metabolon (~1 MDa, soluble)                │
   │   UbiE (C-methyl) ─ UbiG (O-methyl) ─ UbiH/UbiI  │
   │   (hydroxylases) ─ UbiJ (SCP2 lipid carrier)     │
   │        │                                         │
   │        └── hydrophobic polyprenyl-quinone        │
   │            intermediates shuttled by UbiJ        │
   └──────────────────────┬──────────────────────────┘
                          │ mature ubiquinone-9 (UQ9)
                          ▼
        INNER MEMBRANE — aerobic respiratory chain
   dehydrogenases → UQ9/UQ9H2 pool → ubiquinol oxidases
       (cyt bo3 / CIO / cbb3 / aa3) → O2
                          │
                          ▼
             HskA senses UQ oxidation state
             (regulatory feedback on ETC composition)
```

The metabolon model resolves a long-standing puzzle: how extremely hydrophobic isoprenoid-quinone intermediates are processed by soluble enzymes. UbiJ's SCP2 lipid-binding domain sequesters these intermediates and presents them sequentially to the active sites of the complex, including UbiE. The reaction therefore occurs in the aqueous cytoplasm, with the finished UQ9 subsequently partitioning into the inner membrane where it functions in respiration.

### Confidence chain for the annotation

| Evidence type | Source organism | Strength | What it establishes |
|---|---|---|---|
| Genetic loss-of-function (both pathways) | *E. coli* | Direct/high | UbiE = C-methyltransferase for CoQ + MK ([9045837](https://pubmed.ncbi.nlm.nih.gov/9045837/)) |
| Intermediate accumulation + point mutant | *E. coli* | Direct/high | Reaction node & essential Gly142 ([9045837](https://pubmed.ncbi.nlm.nih.gov/9045837/)) |
| Crystal structure + mechanism | Yeast Coq5 | Structural/high | Class I fold, C5 regiochemistry, Arg catalytic base ([25084328](https://pubmed.ncbi.nlm.nih.gov/25084328/)) |
| Cross-species complementation | *E. coli* UbiE → yeast | Functional/high | Same reaction as Coq5 ([14701817](https://pubmed.ncbi.nlm.nih.gov/14701817/)) |
| Sequence orthology 72.6% | *P. putida* vs *E. coli* | Inferential/high | Function transfer to Q88D17 |
| Conserved catalytic residues | *P. putida* vs Coq5 | Inferential/high | Arg149, SAM motifs present in Q88D17 |
| Respiratory context (UQ9, oxidases) | *P. putida* | Direct/high | Physiological role of the product ([16958757](https://pubmed.ncbi.nlm.nih.gov/16958757/), [18341582](https://pubmed.ncbi.nlm.nih.gov/18341582/)) |

The functional annotation of *P. putida* UbiE is thus supported by a robust chain: direct experimental evidence in two model organisms (*E. coli*, yeast), structural/mechanistic detail from a crystallized ortholog, and high sequence conservation of both cofactor-binding and catalytic residues in Q88D17 itself.

---

## Evidence Base

| PMID | Title (abbreviated) | Contribution |
|---|---|---|
| [9045837](https://pubmed.ncbi.nlm.nih.gov/9045837/) | *A C-methyltransferase involved in both ubiquinone and menaquinone biosynthesis: isolation of E. coli ubiE* | **Foundational.** Genetic proof UbiE catalyzes C-methylation in both pathways; identifies ubiE401 (Gly142→Asp); documents intermediate accumulation and succinate-growth defect. |
| [10960098](https://pubmed.ncbi.nlm.nih.gov/10960098/) | *Identification of E. coli ubiB…* | Confirms UbiE required for CoQ + MK; defines the ubiE–yigP(ubiJ)–ubiB operon context. |
| [30686758](https://pubmed.ncbi.nlm.nih.gov/30686758/) | *A Soluble Metabolon Synthesizes the Isoprenoid Lipid Ubiquinone* | Localizes CoQ biosynthesis (including methylation) to a soluble ~1-MDa cytoplasmic complex; UbiJ SCP2 domain binds hydrophobic intermediates. |
| [9083049](https://pubmed.ncbi.nlm.nih.gov/9083049/) | *Characterization of COQ5 from S. cerevisiae* | Establishes UbiE↔Coq5 homology (44% identity) and shared SAM-MTase motifs. |
| [25084328](https://pubmed.ncbi.nlm.nih.gov/25084328/) | *Crystal structures and catalytic mechanism of Coq5* | Class I SAM-MTase fold; C5 regiochemistry (DDMQH2→DMQH2); Arg201 general-base mechanism. |
| [14701817](https://pubmed.ncbi.nlm.nih.gov/14701817/) | *Yeast Coq5 required for stability of other CoQ polypeptides* | Cross-species complementation: E. coli ubiE rescues yeast coq5 mutants. |
| [35178585](https://pubmed.ncbi.nlm.nih.gov/35178585/) | *Recent advances in metabolic pathways and microbial production of CoQ* | Review: multiprotein complexes catalyze consecutive CoQ reactions. |
| [24480387](https://pubmed.ncbi.nlm.nih.gov/24480387/) | *Biosynthesis and physiology of coenzyme Q in bacteria* | Review: ubiquinone function in respiration and signaling. |
| [24249291](https://pubmed.ncbi.nlm.nih.gov/24249291/) | *P. putida HskA hybrid sensor kinase responds to redox signals* | UQ (not UQH2) inhibits HskA autophosphorylation — ubiquinone as redox signal in *P. putida*. |
| [16958757](https://pubmed.ncbi.nlm.nih.gov/16958757/) | *Inactivation of P. putida cyt o ubiquinol oxidase…* | *P. putida* branched aerobic chain; Cyo is a ubiquinol oxidase. |
| [18341582](https://pubmed.ncbi.nlm.nih.gov/18341582/) | *Coordinate regulation of multiple terminal oxidases by ANR* | Confirms branched chain with multiple ubiquinol oxidases. |
| [11359512](https://pubmed.ncbi.nlm.nih.gov/11359512/) / [18323682](https://pubmed.ncbi.nlm.nih.gov/18323682/) | Ubiquinone profiling / *Pseudomonas* taxonomy | *P. putida* uses UQ9 as dominant respiratory quinone. |

**How the evidence coheres:** The *E. coli* genetics ([PMID: 9045837](https://pubmed.ncbi.nlm.nih.gov/9045837/)) and the yeast structural work ([PMID: 25084328](https://pubmed.ncbi.nlm.nih.gov/25084328/)) are mutually reinforcing — one defines the reaction genetically, the other defines it structurally and mechanistically — and the complementation study ([PMID: 14701817](https://pubmed.ncbi.nlm.nih.gov/14701817/)) bridges them by showing the bacterial and eukaryotic enzymes are functionally interchangeable. The metabolon paper ([PMID: 30686758](https://pubmed.ncbi.nlm.nih.gov/30686758/)) updates the subcellular localization. The *P. putida*-specific papers supply the physiological endpoint (UQ9, branched respiration, redox signaling). No retrieved paper contradicts the annotation.

---

## Limitations and Knowledge Gaps

1. **No direct biochemical characterization of *P. putida* UbiE.** All enzymatic evidence derives from orthologs (*E. coli* UbiE, yeast Coq5). The assignment for Q88D17 is inferential, albeit at high confidence given 72.6% identity and conservation of catalytic/cofactor residues. Purified-enzyme kinetics (kcat, Km for SAM and quinol substrate) for the *P. putida* protein have not been reported.

2. **No experimental structure of UbiE from any organism.** The mechanistic model (Arg general base, C5 regiochemistry) is transferred from the crystallized yeast ortholog Coq5, not from a UbiE crystal structure. An AlphaFold model could be assessed but was not analyzed here.

3. **Relative flux between the two pathways in *P. putida* is unquantified.** *P. putida* is an obligate aerobe that relies overwhelmingly on ubiquinone; whether it makes functionally significant menaquinone (and hence how much EC 2.1.1.163 activity matters physiologically) is not established from the retrieved literature. In many strict aerobes the menaquinone branch is minor or absent.

4. **Metabolon composition in *P. putida* not verified.** The soluble Ubi metabolon was demonstrated in *E. coli*. Whether *P. putida* forms an identical complex (and the identity/stoichiometry of its UbiJ-like accessory) is assumed by orthology, not shown.

5. **Essentiality and phenotype in *P. putida* untested here.** No *P. putida ubiE* knockout phenotype was retrieved; predicted consequences (loss of UQ9, respiratory-growth defect) are extrapolated from *E. coli*.

---

## Proposed Follow-up Experiments / Actions

1. **Heterologous complementation:** Express *P. putida ubiE* (PP_5011) in an *E. coli* Δ*ubiE* strain and score restoration of ubiquinone synthesis and succinate growth — a fast, definitive functional confirmation.

2. **In vitro enzymology:** Purify recombinant Q88D17 and assay SAM-dependent methyltransferase activity against a demethyl-Q intermediate (or a soluble analog), measuring kcat/Km and confirming SAH production. Include a Gly-loop mutant (equivalent to *E. coli* Gly142→Asp) and the Arg149→Ala mutant as negative controls to validate the predicted catalytic apparatus.

3. **Structural determination / modeling:** Solve a crystal or cryo-EM structure of *P. putida* UbiE (or rigorously evaluate its AlphaFold model with SAM docked) to verify the class I fold and the positioning of Arg149 and the SAM-binding motif I.

4. **Targeted knockout in *P. putida* KT2440:** Delete PP_5011 and characterize the quinone pool by LC-MS (expecting loss of UQ9 and accumulation of 2-methoxy-6-nonaprenyl-1,4-benzoquinol), plus aerobic respiratory-growth and HskA-signaling phenotypes.

5. **Metabolon co-purification:** Test whether UbiE co-purifies with a UbiJ/UbiG-containing soluble complex from *P. putida* cytoplasm, confirming the metabolon architecture in this organism.

6. **Menaquinone-branch relevance:** Quantify menaquinone/demethylmenaquinone in *P. putida* under microaerobic/anaerobic-mimicking conditions to determine the physiological weight of the EC 2.1.1.163 activity.

---

## Conclusion

*P. putida* KT2440 UbiE (Q88D17, PP_5011) is confidently annotated as the **cytoplasmic, SAM-dependent class I C-methyltransferase** that performs the single ring carbon-methylation step shared by the ubiquinone (EC 2.1.1.201) and menaquinone (EC 2.1.1.163) biosynthetic pathways, adding the C5 ring methyl using SAM and generating SAH. It operates within a soluble multienzyme Ubi metabolon and its principal product, ubiquinone-9, is the redox carrier and redox signal of *P. putida*'s branched aerobic respiratory chain. The assignment rests on direct genetic and structural evidence in *E. coli* and yeast, cross-species functional complementation, and high sequence conservation (72.6% to *E. coli* UbiE; catalytic Arg149 and SAM-binding motifs intact in Q88D17), with the main gap being the absence of direct enzymology on the *P. putida* protein itself.


## Artifacts

- [OpenScientist final report](ubiE-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](ubiE-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:9045837
2. PMID:10960098
3. PMID:30686758
4. PMID:9083049
5. PMID:35178585
6. PMID:24480387
7. PMID:25084328
8. PMID:14701817
9. PMID:11359512
10. PMID:18323682
11. PMID:16958757
12. PMID:18341582
13. PMID:24249291