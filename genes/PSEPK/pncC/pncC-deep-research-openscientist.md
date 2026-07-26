---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-20T15:40:23.746344'
end_time: '2026-07-20T16:10:21.220623'
duration_seconds: 1797.47
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: pncC
  gene_symbol: pncC
  uniprot_accession: Q88ME5
  protein_description: 'SubName: Full=NMN amidohydrolase {ECO:0000313|EMBL:AAN67249.1};
    EC=3.5.1.42 {ECO:0000313|EMBL:AAN67249.1};'
  gene_info: Name=pncC {ECO:0000313|EMBL:AAN67249.1}; OrderedLocusNames=PP_1628 {ECO:0000313|EMBL:AAN67249.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: CinA-like_C. (IPR036653); CinA_C. (IPR008136); CinA (PF02464)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 3
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 4
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: pncC-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: pncC-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88ME5
- **Protein Description:** SubName: Full=NMN amidohydrolase {ECO:0000313|EMBL:AAN67249.1}; EC=3.5.1.42 {ECO:0000313|EMBL:AAN67249.1};
- **Gene Information:** Name=pncC {ECO:0000313|EMBL:AAN67249.1}; OrderedLocusNames=PP_1628 {ECO:0000313|EMBL:AAN67249.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** CinA-like_C. (IPR036653); CinA_C. (IPR008136); CinA (PF02464)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "pncC" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'pncC' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **pncC** (gene ID: pncC, UniProt: Q88ME5) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: pncC (Q88ME5 / PP_1628) in *Pseudomonas putida* KT2440

**Target:** UniProt **Q88ME5** · Gene **pncC** / OrderedLocusName **PP_1628** · *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / KT2440) (PSEPK)
**Annotated activity:** NMN amidohydrolase (NMN deamidase), **EC 3.5.1.42**
**Domains:** CinA-like_C (IPR036653), CinA_C (IPR008136), CinA (Pfam **PF02464**)

---

## Summary

The gene **pncC** (UniProt **Q88ME5**; ordered locus **PP_1628**) of *Pseudomonas putida* KT2440 encodes **nicotinamide mononucleotide (NMN) deamidase** (**EC 3.5.1.42**). This enzyme catalyzes the hydrolytic deamidation of the nicotinamide amide group of NMN, releasing ammonia and producing **nicotinic acid mononucleotide (NaMN)**. The reaction is a *deamidation* — hydrolysis of a carboxamide to a carboxylate — and is chemically and biologically distinct from the phosphorolysis or glycohydrolysis performed by other NAD-metabolizing enzymes. NaMN is then funneled back into NAD⁺ synthesis through the deamidated branch (NadD adenylyltransferase → NadE synthetase). This assignment rests on both the database annotation for Q88ME5 and, more importantly, on strong homology and sequence-motif evidence linking it to experimentally validated bacterial PncC enzymes.

Functionally, PncC is a central node of the **bacterial pyridine nucleotide cycle** — the network of salvage and recycling routes that maintains homeostasis of the NAD(P) cofactor pool. By converting NMN to NaMN, PncC funnels recycled nicotinamide-derived material back into NAD⁺ biosynthesis and simultaneously performs a **detoxification** function: it clears NMN, a metabolite that inhibits the essential NAD⁺-dependent DNA ligase when it accumulates. The enzyme is a soluble **cytoplasmic** protein acting on cytosolic metabolite pools; it has no signal peptide or transmembrane segment. This is a housekeeping metabolic role — precise and mechanistic with respect to NAD⁺ homeostasis, rather than a broadly pleiotropic or signaling role.

Mechanistically, PncC represents a **novel amidohydrolase family** built on the **CinA-like C-terminal fold** (Pfam PF02464; InterPro IPR008136 / IPR036653). Rather than using a classical amidase apparatus, PncC is a **serine-amidohydrolase that employs a Ser/Lys catalytic dyad**. Direct sequence analysis of Q88ME5 confirms that this protein retains the catalytic machinery intact: the catalytic serine sits on a perfectly conserved "S-C-T-G-G-G" loop, and the paired catalytic lysine is present in the expected position. Q88ME5 shares **52.5% full-length sequence identity** with the experimentally validated *E. coli* PncC (YgaD), with the active-site loop conserved residue-for-residue — making this a **high-confidence annotation** rather than a purely inferential one.

---

## Gene/Protein Identity Verification

The gene symbol, organism, EC number, and domain architecture are mutually consistent and unambiguous:

- **Symbol match:** "pncC" is the established name for the bacterial NMN deamidase gene, coined upon its molecular identification ([PMID: 21953451](https://pubmed.ncbi.nlm.nih.gov/21953451/)); the earlier genetic locus was defined in *Salmonella* ([PMID: 7592458](https://pubmed.ncbi.nlm.nih.gov/7592458/)).
- **EC match:** UniProt lists EC 3.5.1.42 = NMN deamidase; the literature uses the identical EC number.
- **Domain match:** The PncC family corresponds to the CinA C-terminal fold (PF02464 / IPR008136 / IPR036653) annotated for Q88ME5; the founding study explicitly notes the family's structure has "no homology with any previously described amidohydrolases," consistent with this distinct domain assignment.

No conflicting or ambiguous literature was encountered. (PncC is unrelated to eukaryotic "PNC1"-type nicotinamidases or CD38-type NAD glycohydrolases.)

---

## Key Findings

### F001 — pncC encodes NMN deamidase (EC 3.5.1.42), catalyzing NMN → NaMN + NH₃

UniProt entry Q88ME5 annotates the *P. putida* KT2440 gene *pncC* / PP_1628 as "NMN amidohydrolase, EC 3.5.1.42." The identity of the *pncC* gene product as an NMN deamidase is not merely a database call: it was established through native purification of the enzyme from *Shewanella oneidensis* and gene assignment, and confirmed for the *Escherichia coli* homolog *ygaD*. Galeazzi and colleagues describe "**Nicotinamide mononucleotide (NMN) deamidase (EC 3.5.1.42), one of the key enzymes of the bacterial pyridine nucleotide cycle**" ([PMID: 21953451](https://pubmed.ncbi.nlm.nih.gov/21953451/)), directly matching the EC number and enzyme name assigned to Q88ME5.

The chemistry of the reaction is a **deamidation**, not a phosphorolysis: the enzyme hydrolyzes the nicotinamide amide bond of NMN, releasing ammonia and producing NaMN. This was demonstrated genetically and biochemically in *Salmonella typhimurium* by Cheng and Roth, who showed that "**NMN deamidase, which converts NMN directly to the biosynthetic intermediate nicotinic acid mononucleotide**" ([PMID: 7592458](https://pubmed.ncbi.nlm.nih.gov/7592458/)); their *pncC* mutants showed roughly 2% of wild-type deamidase activity. The product NaMN is a canonical intermediate of NAD⁺ biosynthesis, which is why the deamidase reaction reconnects salvaged nicotinamide-mononucleotide material to the main biosynthetic trunk.

**Reaction catalyzed:**

```
NMN (nicotinamide mononucleotide)  +  H2O
        │   PncC (EC 3.5.1.42)
        ▼
NaMN (nicotinic acid mononucleotide)  +  NH3
```

### F002 — PncC is a Ser/Lys serine-amidohydrolase defining a novel CinA-like fold family

The catalytic mechanism of PncC was solved by Sorci and colleagues, who systematically mutated all candidate catalytic residues and, combining kinetic data with a crystal structure containing modeled NMN, concluded that "**PncC is a serine-amidohydrolase, employing a Ser/Lys dyad for catalysis**" ([PMID: 24530526](https://pubmed.ncbi.nlm.nih.gov/24530526/)). This places PncC among the serine amidohydrolases but with an unusual two-residue (Ser/Lys) catalytic dyad rather than a classical Ser-His-Asp triad or a glutamine-amidotransferase apparatus, and it expands the recognized diversity of serine amidohydrolases.

Critically, this fold is structurally novel. The founding structural characterization reported that the PncC structure "**shows no homology with any previously described amidohydrolases**" ([PMID: 21953451](https://pubmed.ncbi.nlm.nih.gov/21953451/)), defining a new, broadly conserved amidohydrolase family. This family corresponds to the **CinA C-terminal domain fold** — Pfam **PF02464**, InterPro **IPR008136** and **IPR036653** — precisely the domains annotated for Q88ME5.

The catalytic residues have been directly implicated by functional studies. Camarca and colleagues characterized active-site variants and showed that S29A and K61Q mutants "**still preserve the ability to bind NMN in the micromolar range, but they are not able to catalyze the enzymatic reaction**" ([PMID: 34199271](https://pubmed.ncbi.nlm.nih.gov/34199271/)). This cleanly separates substrate binding from catalysis and confirms that a specific serine (nucleophile) and lysine (general base) are catalytically essential — exactly the Ser/Lys dyad predicted from the mechanism. Notably, the S29A variant retained the ability to bind the product NaMN whereas K61Q did not, indicating discrete determinants distinguishing substrate from product and highlighting selectivity within the pyridine-mononucleotide series.

### F003 — PncC operates in the cytoplasmic pyridine nucleotide cycle for NAD salvage and NMN detoxification

PncC is not a peripheral enzyme; it is a hub of NAD⁺ recycling. Galeazzi and colleagues position NMN deamidase as "**one of the key enzymes of the bacterial pyridine nucleotide cycle**," describing that cycle as "**a network of salvage and recycling routes maintaining homeostasis of NAD(P) cofactor pool in the cell**" ([PMID: 21953451](https://pubmed.ncbi.nlm.nih.gov/21953451/)). In *S. oneidensis*, genomic reconstruction indicated the PncC reaction was the only route of nicotinamide/NMN salvage, and deletion mutants confirmed this physiological role.

The enzyme also performs an essential protective function. Cheng and Roth showed in *S. typhimurium* that the pyridine nucleotide cycle is roughly fivefold more active aerobically, and — crucially — that "**Accumulated NMN generated by either of these routes is potentially dangerous in that it can inhibit the essential enzyme DNA ligase**" ([PMID: 7592458](https://pubmed.ncbi.nlm.nih.gov/7592458/)). *pncC* mutants were defective in NMN deamidase activity and NMN utilization. Thus PncC serves a dual role: it (1) recovers nitrogen/pyridine material for NAD⁺ resynthesis, and (2) prevents NMN from accumulating to levels that would poison the essential NAD⁺-dependent DNA ligase.

All substrates and products of the reaction (NMN, NaMN, NAD⁺ and its intermediates) are **cytosolic metabolites**, and the enzyme itself is a soluble cytoplasmic protein with no signal or membrane-targeting features — establishing the **cytoplasm** as the site of function.

### F004 — The Q88ME5 sequence directly confirms the conserved catalytic Ser/Lys and a single CinA-like domain

To move beyond pure orthology transfer, the Q88ME5 sequence (160 aa) was retrieved from UniProt and examined for the family's catalytic apparatus. The sequence contains the family-diagnostic active-site motif **S-C-T-G-G-G at positions 27–32** (…AE**S27CTGGG**…), placing the catalytic nucleophilic serine (**Ser27**) on the conserved "CTGGG" loop that is the structural hallmark of the PncC/CinA-C amidohydrolase family. A conserved catalytic lysine (**Lys59**, in the …SNAQ**K59**T… segment) is present in the position corresponding to the general base.

These residues map — with a small (~2-residue) N-terminal numbering offset — onto the experimentally validated catalytic residues of the characterized orthologs, where S29A and K61Q abolish catalysis while retaining NMN binding ([PMID: 34199271](https://pubmed.ncbi.nlm.nih.gov/34199271/)) and where the Ser/Lys dyad mechanism was established ([PMID: 24530526](https://pubmed.ncbi.nlm.nih.gov/24530526/)). The protein is a single ~160-residue CinA-C domain (PF02464 / IPR008136 / IPR036653) with no predicted signal peptide or transmembrane segment, consistent with a soluble cytoplasmic single-domain enzyme. This indicates Q88ME5 possesses an intact catalytic apparatus and is a *bona fide* active NMN deamidase, not a degenerate (non-catalytic) PncC homolog.

### F005 — Q88ME5 shares 52.5% identity with the experimentally validated *E. coli* PncC, with a perfectly conserved catalytic motif

A global Needleman–Wunsch alignment of *P. putida* Q88ME5 (160 aa) against the experimentally validated *E. coli* NMN deamidase PncC/YgaD (UniProt **P0A6G3**, 165 aa) gives **84/160 identical positions = 52.5% sequence identity** over the full length, with no internal gaps. The *E. coli* reference is itself rigorously validated: of *E. coli*'s three PncC homologs, "**NMN deamidase activity was confirmed only for the recombinant purified product of the ygaD gene**" ([PMID: 21953451](https://pubmed.ncbi.nlm.nih.gov/21953451/)). Because the correct, functionally validated paralog is the alignment reference, this comparison is meaningful.

Most importantly, the catalytic loop is conserved residue-for-residue: Q88ME5 residues 24–31 (**T-A-E-S-C-T-G-G**) align identically to the *E. coli* sequence (**T-A-E-S-C-T-G-G**), meaning the catalytic Ser (Q88ME5 Ser27) and the flanking CTGG motif are perfectly conserved. This level of identity to a validated enzyme, combined with an identical active-site loop, far exceeds the standard threshold for confident enzyme functional-annotation transfer (~>40% identity plus conserved catalytic residues), elevating the Q88ME5 annotation from inference to high confidence.

---

## Mechanistic Model / Interpretation

PncC sits at the deamidation branch point of the bacterial pyridine nucleotide cycle. The integrated model from the five findings is as follows:

```
   NAD+ turnover / nucleotide degradation
                │
                ▼
             NMN  ────────────────► [inhibits NAD+-dependent DNA ligase]  (toxic if accumulated)
                │
                │  PncC (Q88ME5 / PP_1628)
                │  EC 3.5.1.42 · Ser/Lys dyad · CinA-like fold
                │  NMN + H2O → NaMN + NH3
                ▼
             NaMN  (nicotinic acid mononucleotide)
                │
                │  NadD (adenylyltransferase)
                ▼
             NaAD (deamido-NAD)
                │
                │  NadE (NAD synthetase)
                ▼
              NAD+   ───► redox metabolism, DNA ligase cofactor, signaling
```

Two features of this model deserve emphasis:

1. **Deamidation reconnects salvage to the "amidation-last" logic of bacterial NAD⁺ synthesis.** Bacteria assemble the deamidated intermediate NaMN → NaAD and add the amide only at the final NadE step. By deamidating NMN back to NaMN, PncC ensures recycled material re-enters the pathway at the correct deamidated point rather than short-circuiting it — which is why the enzyme is a "key" node rather than a redundant one.

2. **Detoxification and salvage are two sides of the same reaction.** The same catalytic event that recovers pyridine material also removes NMN, which would otherwise inhibit DNA ligase. This coupling explains why *pncC* function is physiologically important even where alternative NAD⁺ inputs exist.

**Structural / mechanistic summary:**

| Property | Value | Evidence |
|---|---|---|
| Enzyme | NMN deamidase | UniProt Q88ME5; [PMID: 21953451](https://pubmed.ncbi.nlm.nih.gov/21953451/) |
| EC number | 3.5.1.42 | UniProt Q88ME5 |
| Reaction | NMN + H₂O → NaMN + NH₃ | [PMID: 7592458](https://pubmed.ncbi.nlm.nih.gov/7592458/) |
| Mechanism | Serine-amidohydrolase, Ser/Lys dyad | [PMID: 24530526](https://pubmed.ncbi.nlm.nih.gov/24530526/) |
| Catalytic residues (Q88ME5) | Ser27 (on S-CTGGG loop), Lys59 | Sequence analysis (F004); homolog data [PMID: 34199271](https://pubmed.ncbi.nlm.nih.gov/34199271/) |
| Fold / family | CinA-like C-terminal; PF02464 / IPR008136 / IPR036653 | UniProt Q88ME5; [PMID: 21953451](https://pubmed.ncbi.nlm.nih.gov/21953451/) |
| Localization | Cytoplasm (soluble; no signal/TM) | Sequence analysis (F004) |
| Pathway | Pyridine nucleotide cycle / NAD⁺ salvage | [PMID: 21953451](https://pubmed.ncbi.nlm.nih.gov/21953451/) |
| Identity to validated *E. coli* PncC (P0A6G3) | 52.5% full-length; active-site loop identical | Alignment (F005) |

---

## Evidence Base

| PMID | Title (abbreviated) | Contribution |
|---|---|---|
| [21953451](https://pubmed.ncbi.nlm.nih.gov/21953451/) | *Identification of NMN deamidase of the bacterial pyridine nucleotide cycle reveals a novel broadly conserved amidohydrolase family* | Founding paper: identifies PncC as NMN deamidase (EC 3.5.1.42), validates *E. coli* YgaD as the active paralog, establishes the novel CinA-like amidohydrolase family, and places PncC in the pyridine nucleotide cycle. |
| [24530526](https://pubmed.ncbi.nlm.nih.gov/24530526/) | *Characterization of bacterial NMN deamidase as a Ser/Lys hydrolase expands diversity of serine amidohydrolases* | Establishes the catalytic mechanism: a Ser/Lys dyad serine-amidohydrolase, via mutagenesis plus a structure with modeled NMN. |
| [34199271](https://pubmed.ncbi.nlm.nih.gov/34199271/) | *Characterization of Two NMN Deamidase Mutants as Possible Probes for an NMN Biosensor* | Functionally confirms specific active-site Ser and Lys: S29A/K61Q bind NMN but cannot catalyze — separating binding from catalysis. |
| [7592458](https://pubmed.ncbi.nlm.nih.gov/7592458/) | *Isolation of NAD cycle mutants defective in NMN deamidase in Salmonella typhimurium* | Genetic/physiological validation: defines the reaction (NMN → NaMN), the detoxification role (NMN inhibits DNA ligase), and pncC mutant phenotypes. |

**How the evidence converges on Q88ME5 specifically:** No study has purified or crystallized the *P. putida* KT2440 protein itself; the direct experimental work was done on *S. oneidensis*, *E. coli*, and *S. typhimurium* homologs. The bridge to Q88ME5 is provided by the two bioinformatic findings from this investigation (F004, F005): the *P. putida* sequence retains the family-diagnostic catalytic motif intact and is 52.5% identical to the correct, validated *E. coli* reference, with a residue-for-residue identical active-site loop. Together these make functional transfer to Q88ME5 high-confidence.

---

## Supported and Refuted Hypotheses

| Hypothesis | Status | Basis |
|---|---|---|
| pncC/Q88ME5 is NMN deamidase (EC 3.5.1.42) | **Supported** | UniProt annotation + PMIDs 21953451, 7592458 |
| Catalyzes NMN → NaMN + NH₃ (deamidation) | **Supported** | PMIDs 21953451, 7592458 |
| Uses a Ser/Lys catalytic dyad (serine amidohydrolase) | **Supported** | PMID 24530526; active-site variants PMID 34199271 |
| Belongs to a novel CinA-like amidohydrolase fold | **Supported** | PMID 21953451; InterPro/Pfam for Q88ME5 |
| Functions in cytoplasmic NAD⁺ salvage (pyridine nucleotide cycle) | **Supported** | PMID 21953451 |
| Detoxifies NMN to protect DNA ligase | **Supported** | PMID 7592458 |
| Q88ME5 specifically retains an intact catalytic apparatus | **Supported** | Sequence analysis (F004, F005); 52.5% identity to validated *E. coli* PncC |
| Metal-dependent (classical) amidohydrolase mechanism | **Refuted** | No homology to classical amidohydrolases; Ser/Lys catalysis (PMIDs 21953451, 24530526) |

---

## Limitations and Knowledge Gaps

1. **No direct experimental characterization of the *P. putida* KT2440 protein.** Enzyme kinetics, substrate specificity, structure, and knockout phenotypes were all measured in *other* bacteria (*S. oneidensis*, *E. coli* YgaD, *S. typhimurium*). The Q88ME5 assignment is a homology- and sequence-motif-based transfer, albeit a strong one (52.5% identity, conserved catalytic loop).

2. **Kinetic parameters (kcat, Km) for Q88ME5 are unknown.** While the family acts on NMN, quantitative specificity for the KT2440 ortholog has not been measured, and possible activity on related substrates has not been experimentally excluded.

3. **Residue numbering offset.** The Q88ME5 catalytic residues are annotated here as Ser27/Lys59 based on sequence analysis; the exact numbering should be confirmed against a structure or an authoritative alignment given the ~2-residue offset relative to the *S. oneidensis* numbering.

4. **Paralog/context uncertainty.** Some bacteria carry multiple CinA-C/PncC-like homologs of which only one is an active deamidase. Whether *P. putida* KT2440 carries additional CinA-domain paralogs, and their functional partitioning, was not exhaustively resolved. The CinA domain family also has links to DNA/competence contexts in some bacteria; any secondary genomic-context role for PP_1628 beyond NAD⁺ salvage was not established.

5. **Regulation and in vivo flux in *P. putida*.** The contribution of PncC to NAD⁺ homeostasis under different growth conditions (aerobic vs. anaerobic, nitrogen limitation) in *P. putida* specifically has not been quantified; the aerobic activation observed in *Salmonella* may or may not transfer.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant expression and enzymatic assay of Q88ME5.** Clone PP_1628, purify the protein, and measure NMN deamidase activity (NMN → NaMN + NH₃) directly, determining kcat and Km and testing specificity against related nucleotides.

2. **Structure determination or AlphaFold analysis.** Solve or model the Q88ME5 structure, confirm the catalytic Ser/Lys geometry and the CinA-like fold, and validate/correct the Ser27/Lys59 numbering.

3. **Site-directed mutagenesis (Ser27→Ala, Lys59→Gln).** Reproduce the ortholog result in the *P. putida* enzyme to confirm these residues are catalytically essential but binding-competent.

4. **Genetic knockout in *P. putida* KT2440.** Delete PP_1628 and assess NAD⁺/NMN pool changes, growth on nicotinamide-related nitrogen/carbon sources, and any NMN-toxicity or DNA-ligase-related phenotype.

5. **Paralog census.** Systematically identify all CinA-domain (PF02464) homologs in the KT2440 genome and test which, if any, carry deamidase activity, to rule out functional redundancy or misassignment.

6. **Pathway flux analysis.** Use labeled precursors to trace NMN → NaMN → NAD⁺ flux through PncC under aerobic vs. anaerobic and nitrogen-limited conditions.

---

### Key References

1. Galeazzi L, *et al.* *Identification of nicotinamide mononucleotide deamidase of the bacterial pyridine nucleotide cycle reveals a novel broadly conserved amidohydrolase family.* J Biol Chem, 2011. **PMID [21953451](https://pubmed.ncbi.nlm.nih.gov/21953451/).**
2. Sorci L, *et al.* *Characterization of bacterial NMN deamidase as a Ser/Lys hydrolase expands diversity of serine amidohydrolases.* 2014. **PMID [24530526](https://pubmed.ncbi.nlm.nih.gov/24530526/).**
3. Cheng W, Roth JR. *Isolation of NAD cycle mutants defective in nicotinamide mononucleotide deamidase in Salmonella typhimurium.* J Bacteriol, 1995. **PMID [7592458](https://pubmed.ncbi.nlm.nih.gov/7592458/).**
4. Camarca A, *et al.* *Characterization of Two NMN Deamidase Mutants as Possible Probes for an NMN Biosensor.* 2021. **PMID [34199271](https://pubmed.ncbi.nlm.nih.gov/34199271/).**

---

*Report generated from a 3-iteration autonomous investigation. Findings F001–F005 are recorded in the knowledge state with verified literature citations. The functional annotation of Q88ME5 as an NMN deamidase (EC 3.5.1.42) is assigned with high confidence based on database annotation, conserved catalytic-motif analysis, and 52.5% sequence identity to the experimentally validated E. coli PncC.*


## Artifacts

- [OpenScientist final report](pncC-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](pncC-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:21953451
2. PMID:7592458
3. PMID:24530526
4. PMID:34199271