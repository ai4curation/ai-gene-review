---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-14T06:40:44.839473'
end_time: '2026-07-14T06:53:28.004471'
duration_seconds: 763.17
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: lspA
  gene_symbol: lspA
  uniprot_accession: Q88Q91
  protein_description: 'RecName: Full=Lipoprotein signal peptidase {ECO:0000255|HAMAP-Rule:MF_00161};
    EC=3.4.23.36 {ECO:0000255|HAMAP-Rule:MF_00161}; AltName: Full=Prolipoprotein signal
    peptidase {ECO:0000255|HAMAP-Rule:MF_00161}; AltName: Full=Signal peptidase II
    {ECO:0000255|HAMAP-Rule:MF_00161}; Short=SPase II {ECO:0000255|HAMAP-Rule:MF_00161};'
  gene_info: Name=lspA {ECO:0000255|HAMAP-Rule:MF_00161}; OrderedLocusNames=PP_0604;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the peptidase A8 family. {ECO:0000255|HAMAP-
  protein_domains: Peptidase_A8. (IPR001872); Peptidase_A8 (PF01252)
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
citation_count: 12
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: lspA-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: lspA-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88Q91
- **Protein Description:** RecName: Full=Lipoprotein signal peptidase {ECO:0000255|HAMAP-Rule:MF_00161}; EC=3.4.23.36 {ECO:0000255|HAMAP-Rule:MF_00161}; AltName: Full=Prolipoprotein signal peptidase {ECO:0000255|HAMAP-Rule:MF_00161}; AltName: Full=Signal peptidase II {ECO:0000255|HAMAP-Rule:MF_00161}; Short=SPase II {ECO:0000255|HAMAP-Rule:MF_00161};
- **Gene Information:** Name=lspA {ECO:0000255|HAMAP-Rule:MF_00161}; OrderedLocusNames=PP_0604;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the peptidase A8 family. {ECO:0000255|HAMAP-
- **Key Domains:** Peptidase_A8. (IPR001872); Peptidase_A8 (PF01252)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "lspA" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'lspA' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **lspA** (gene ID: lspA, UniProt: Q88Q91) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# LspA (Q88Q91, PP_0604) in *Pseudomonas putida* KT2440: Lipoprotein Signal Peptidase II

**Gene:** *lspA* (ordered locus **PP_0604**) · **Protein:** Lipoprotein signal peptidase II (SPase II)
**UniProt:** Q88Q91 · **EC 3.4.23.36** · **Family:** Peptidase A8 (Pfam PF01252 / InterPro IPR001872)
**Organism:** *Pseudomonas putida* KT2440 (ATCC 47054 / DSM 6125 / NCIMB 11950)

---

## Summary

**LspA (Q88Q91; locus tag PP_0604) in *Pseudomonas putida* strain KT2440 is lipoprotein signal peptidase II (Signal Peptidase II / SPase II; also called prolipoprotein signal peptidase; EC 3.4.23.36).** It is an essential, integral inner-membrane **aspartyl protease** that performs the committed, second step of the universal bacterial lipoprotein biogenesis pathway. Its primary catalytic function is precise: it hydrolyzes the peptide bond immediately N-terminal to the lipid-modified cysteine of a diacylglyceryl-prolipoprotein, thereby removing the signal peptide and generating the mature apolipoprotein N-terminus. Gene-symbol, organism, protein family (peptidase A8; Pfam PF01252 / InterPro IPR001872), and domain architecture all align cleanly with the UniProt-provided identity — **there is no gene-symbol ambiguity**; "lspA" unambiguously denotes lipoprotein signal peptidase II across bacteria.

The enzyme's substrate specificity is defined by the conserved **lipobox** motif: it cleaves at –Xaa–Yaa–Zaa–|–(*S*,diacylglyceryl)Cys–, where Xaa is hydrophobic (preferentially Leu), and Yaa (Ala/Ser) and Zaa (Gly/Ala) carry small, neutral side chains. Critically, LspA acts *only after* the upstream enzyme Lgt (phosphatidylglycerol::prolipoprotein diacylglyceryl transferase) has attached a diacylglyceryl group to the invariant lipobox cysteine — LspA is specific for prolipoproteins and does not process ordinary secretory preproteins (which are handled by signal peptidase I / LepB). After LspA cleavage, the downstream enzyme Lnt N-acylates the cysteine, completing the mature triacylated lipoprotein that is then sorted by the Lol system. This places LspA firmly in the linear pathway **Lgt → LspA → Lnt**.

LspA carries out catalysis within the **cytoplasmic (inner) membrane** as a multi-pass membrane protein (five predicted transmembrane helices), with its two catalytic aspartates (Asp126 and Asp145 in Q88Q91) positioned in a membrane-embedded active site that faces the periplasmic/outer-leaflet side, where the lipid-anchored prolipoprotein presents its signal peptide. This functional assignment is supported by high-confidence bioinformatic evidence (exact conservation of catalytic residues and flanking motifs with experimentally validated *E. coli*, *P. aeruginosa*, and *S. aureus* orthologs; a conserved ileS–lspA genomic neighborhood; and an AlphaFold structural model of the catalytic dyad) and, indirectly but strongly, by extensive experimental characterization of those orthologs — including crystal structures, catalytic-residue mutagenesis, and inhibition by the natural-product antibiotics globomycin and myxovirescin (antibiotic TA). LspA is a validated, essential antibiotic target in Gram-negative bacteria.

---

## Key Findings

### Finding 1 — LspA is an integral inner-membrane aspartyl protease that removes prolipoprotein signal peptides (EC 3.4.23.36)

UniProt entry **Q88Q91** (*P. putida* KT2440, locus PP_0604, 171 amino acids) annotates the FUNCTION as specifically catalyzing "the removal of signal peptides from prolipoproteins," classifies the enzyme under **EC 3.4.23.36**, assigns it to **peptidase family A8**, and applies the molecular-function keyword **"Aspartyl protease."** Two annotated active-site residues are both aspartates, which was verified by direct sequence indexing of Q88Q91: position **126 = Asp** (local context HVV**D**FIL) and position **145 = Asp** (local context NVA**D**SAI). The sequence is ~56% hydrophobic and contains five predicted transmembrane helices (residues 12–32, 42–62, 70–90, 96–116, and 137–157), consistent with an integral membrane protease.

This assignment is corroborated by direct experimental work on close orthologs. Crystal-structure and mutagenesis studies of *P. aeruginosa* LspA established that "posttranslational processing requires a signal peptidase II (LspA) that removes the signal peptide" and that "mutagenesis studies identify LspA as an aspartyl peptidase" ([PMID: 26912896](https://pubmed.ncbi.nlm.nih.gov/26912896/)). Because the two catalytic aspartates and their sequence context are conserved between the *P. aeruginosa*/*E. coli* orthologs and Q88Q91, this experimental definition of catalytic class transfers with high confidence to the *P. putida* enzyme. LspA therefore belongs to the unusual group of **membrane-embedded aspartyl proteases** that use a paired-aspartate mechanism rather than the classic serine-protease chemistry of signal peptidase I.

### Finding 2 — LspA catalyzes the committed second step of the conserved lipoprotein biogenesis pathway (Lgt → LspA → Lnt)

UniProt assigns Q88Q91 to the PATHWAY "Protein modification; lipoprotein biosynthesis (signal peptide cleavage)." In the canonical, conserved bacterial pathway, preprolipoproteins are exported across the inner membrane by the Sec (or Tat) machinery. The first committed enzyme, **Lgt**, recognizes the lipobox and "converts them to prolipoproteins by adding a diacylglyceryl group to the sulfhydryl side chain of the invariant Cys" ([PMID: 32490790](https://pubmed.ncbi.nlm.nih.gov/32490790/)). **LspA then cleaves the signal peptide immediately N-terminal to this now-modified cysteine**, producing apolipoprotein. Finally, **Lnt** N-acylates the free α-amino group of the cysteine to yield the mature triacylated lipoprotein.

LspA's role as the processing enzyme in this pathway is reinforced by antibiotic-mechanism studies. In *E. coli*, "the lspA gene … encodes the type II signal peptidase that cleaves signal sequences from prolipoproteins," and the myxobacterial antibiotic TA (myxovirescin) "was shown to inhibit Lpp prolipoprotein processing, similar to the known LspA inhibitor globomycin" ([PMID: 22232277](https://pubmed.ncbi.nlm.nih.gov/22232277/)). The fact that specific small molecules block prolipoprotein maturation by targeting LspA firmly places the enzyme at the signal-peptide-cleavage node of the pathway.

### Finding 3 — Substrate specificity: cleavage at the lipobox, requiring pre-attached diacylglyceryl-cysteine

The UniProt CATALYTIC ACTIVITY for EC 3.4.23.36 states that LspA "hydrolyzes –Xaa–Yaa–Zaa–|–(*S*,diacylglyceryl)Cys–, in which Xaa is hydrophobic (preferably Leu), and Yaa (Ala or Ser) and Zaa (Gly or Ala) have small, neutral side chains." This corresponds to the conserved **lipobox** consensus **[LVI]-[ASTVI]-[GAS]-C**. Two features define the specificity:

1. **Sequence context** — LspA recognizes the small-residue lipobox rather than a single rigid sequence, enabling it to process the diverse repertoire of cellular lipoproteins.
2. **Prior lipid modification** — LspA acts strictly *after* Lgt has diacylglyceryl-modified the invariant cysteine. It is therefore specific for **prolipoproteins**, and does not substitute for signal peptidase I (LepB), which processes standard secretory preproteins.

Structural studies of orthologs explain both the breadth and the chemistry. Antibiotic-bound structures show that globomycin and myxovirescin "appear to inhibit identically as non-cleavable tetrahedral intermediate analogs" ([PMID: 31919415](https://pubmed.ncbi.nlm.nih.gov/31919415/)), meaning they occupy the substrate groove and mimic the transition state that forms during peptide-bond hydrolysis. Complementary molecular-dynamics and spectroscopic work concludes that LspA possesses "a flexible and adaptable active site, which explains how LspA accommodates and processes such a variety of substrates" ([PMID: 35505611](https://pubmed.ncbi.nlm.nih.gov/35505611/)). Thus the enzyme achieves broad lipoprotein coverage by recognizing the conserved lipobox and its lipid anchor within a conformationally plastic pocket.

### Finding 4 — Localization: inner (cytoplasmic) membrane, multi-pass, with a periplasm-facing active site

UniProt SUBCELLULAR LOCATION for Q88Q91 is "Cell inner membrane; Multi-pass membrane protein." The sequence supports this directly: five predicted TM helices and ~56% hydrophobic residues. Crystal structures of the *P. aeruginosa* ([PMID: 26912896](https://pubmed.ncbi.nlm.nih.gov/26912896/)) and *S. aureus* ([PMID: 31919415](https://pubmed.ncbi.nlm.nih.gov/31919415/)) orthologs reveal a compact transmembrane fold in which the two catalytic aspartates sit in a membrane-embedded active site accessible from the periplasmic/outer-leaflet side. This orientation matches the biology of the substrate: "lipoproteins are synthesized with a signal peptide securing them to the cytoplasmic membrane with the lipoprotein domain in the periplasm or outside the cell" ([PMID: 26912896](https://pubmed.ncbi.nlm.nih.gov/26912896/)), so LspA must cleave at the membrane–periplasm interface. Dynamic studies further show that "the periplasmic helix fluctuates on the nanosecond timescale and samples unique conformations in the different states" ([PMID: 35505611](https://pubmed.ncbi.nlm.nih.gov/35505611/)), identifying a periplasm-facing helix that gates the active site during catalysis. LspA therefore performs its reaction *within the inner membrane*, presenting its catalytic dyad toward the periplasmic face where the lipid-anchored prolipoprotein extends.

### Finding 5 — Evolutionary conservation: *P. putida* catalytic aspartates align exactly with validated *E. coli* residues

A direct comparison of UniProt active-site annotations shows precise conservation. *E. coli* LspA (**P00804**, 164 aa) has catalytic **Asp123** (context FVV**D**MID) and **Asp141** (context NLA**D**TAI); *P. putida* Q88Q91 (171 aa) has catalytic **Asp126** (context HVV**D**FIL) and **Asp145** (context NVA**D**SAI). Both aspartates and their flanking motifs — a **[FH]VVD** hydrophobic-Asp motif and a conserved **N-x-A-D-x-A-I** motif — are conserved, and both orthologs belong to peptidase family A8 (Pfam PF01252 / IPR001872). Because the *E. coli*/*P. aeruginosa* catalytic aspartates were experimentally validated by mutagenesis ("mutagenesis studies identify LspA as an aspartyl peptidase," [PMID: 26912896](https://pubmed.ncbi.nlm.nih.gov/26912896/)), this exact alignment permits high-confidence transfer of the catalytic-dyad assignment to the *P. putida* enzyme.

| Feature | *E. coli* LspA (P00804) | *P. putida* LspA (Q88Q91) |
|---|---|---|
| Length | 164 aa | 171 aa |
| Catalytic Asp #1 | Asp123 (FVV**D**MID) | Asp126 (HVV**D**FIL) |
| Catalytic Asp #2 | Asp141 (NLA**D**TAI) | Asp145 (NVA**D**SAI) |
| Family / Pfam | Peptidase A8 / PF01252 | Peptidase A8 / PF01252 |
| Localization | Inner membrane, multi-pass | Inner membrane, multi-pass |

Broader phylogenetic evidence reinforces functional interchangeability across the family: in *Myxococcus xanthus*, LspA orthologs "contained nearly all the conserved residues characteristic of SPaseII family members," could complement an *E. coli* ΔlspA mutation, and conferred globomycin/TA resistance when overexpressed ([PMID: 24391051](https://pubmed.ncbi.nlm.nih.gov/24391051/)).

### Finding 6 — LspA is an essential, validated antibiotic target

Multiple independent studies describe LspA/SPase II as essential to the Gram-negative lipoprotein biosynthetic pathway and an attractive antibacterial target. It is "an essential enzyme in the lipoprotein biosynthetic pathway of Gram-negative bacteria, making it an attractive target for antibacterial drug discovery" ([PMID: 38712757](https://pubmed.ncbi.nlm.nih.gov/38712757/)), and members of this pathway "are essential in Gram-negative bacteria, are important for virulence in Gram-positive bacteria" ([PMID: 35505611](https://pubmed.ncbi.nlm.nih.gov/35505611/)). LspA is inhibited by the natural cyclic depsipeptide **globomycin** and the macrocyclic **myxovirescin/antibiotic TA**, which act as non-cleavable tetrahedral-intermediate mimics ([PMID: 31919415](https://pubmed.ncbi.nlm.nih.gov/31919415/); [PMID: 26912896](https://pubmed.ncbi.nlm.nih.gov/26912896/)). Inhibition causes a toxic buildup of unprocessed prolipoprotein: "a block in Lpp expression or prevention of Lpp covalent cell wall attachment confers TA resistance by alleviating a toxic buildup of mislocalized pro-Lpp" ([PMID: 22232277](https://pubmed.ncbi.nlm.nih.gov/22232277/)), explaining why the step is essential. Active drug-discovery programs target LspA with optimized globomycin analogs and computationally designed cyclic peptides ([PMID: 32768648](https://pubmed.ncbi.nlm.nih.gov/32768648/); [PMID: 38712757](https://pubmed.ncbi.nlm.nih.gov/38712757/)). Biophysically, LspA is a ~20 kDa integral membrane enzyme amenable to reconstitution and structural study ([PMID: 40119522](https://pubmed.ncbi.nlm.nih.gov/40119522/)).

### Finding 7 — Genomic context: the conserved ileS–lspA neighborhood

UniProt locus queries of the *P. putida* KT2440 genome place lspA in a conserved neighborhood: **PP_0603 = Q88Q92** (isoleucine–tRNA ligase, ileS, 943 aa) immediately upstream of **PP_0604 = Q88Q91** (lspA, 171 aa), with **PP_0605 = Q88Q90** (peptidyl-prolyl cis-trans isomerase, 145 aa) downstream. The **ileS–lspA** juxtaposition is a conserved feature across many bacterial genomes — including *E. coli*, where lspA is co-transcribed with ileS in an operon — providing an additional orthology signal that reinforces the functional assignment.

### Finding 8 — AlphaFold model confirms a juxtaposed catalytic aspartyl dyad

The AlphaFold DB model **AF-Q88Q91-F1** (v6; global pLDDT 90.1; core residues 20–160 mean pLDDT 94.6) predicts the two annotated catalytic aspartates at very high local confidence (Asp126 pLDDT 98.4; Asp145 pLDDT 98.2). Their carboxyl groups are directly juxtaposed — minimum OD–OD oxygen distance **3.67 Å** and CG–CG distance **5.70 Å** — the hallmark geometry of a **paired-aspartate (aspartyl protease) active site**, in which the two carboxylates coordinate a catalytic water/proton for peptide-bond hydrolysis. The predicted pocket assembles residues from the conserved GNLYD motif (Asn114 region), the Asp126 loop, and the N140–Asp145 (N-x-A-D-x-A-I) motif, plus TM-helix residues near positions 54–56, matching the active-site architecture observed in ortholog crystal structures. This structural prediction independently corroborates, at the level of 3D geometry, the catalytic-dyad assignment derived from sequence and homology.

---

## Mechanistic Model / Interpretation

LspA is the **committed maturation protease** of bacterial lipoproteins. The pathway and LspA's place in it can be summarized as follows:

```
 Cytoplasm            Preprolipoprotein (N-signal-lipobox-mature)
    |                         | Sec / Tat export
    v                         v
 ============ INNER MEMBRANE ==================================================
   Step 1  Lgt  : adds diacylglyceryl to invariant lipobox Cys  (prolipoprotein)
                         |
   Step 2  LspA : cleaves  ...Xaa-Yaa-Zaa | (diacylglyceryl)Cys...   <-- THIS ENZYME
                         |   (removes signal peptide -> apolipoprotein)
   Step 3  Lnt  : N-acylates the Cys alpha-amine (mature triacyl-lipoprotein)
 ============================================================================
                         |  Lol system sorts to inner vs outer membrane
                         v
                  Periplasm / Outer membrane
```

**Reaction catalyzed:** hydrolysis of the peptide bond on the N-terminal side of the diacylglyceryl-modified cysteine within the lipobox. **Substrate:** diacylglyceryl-prolipoproteins bearing the lipobox –Xaa(hydrophobic/Leu)–Yaa(Ala/Ser)–Zaa(Gly/Ala)–|–Cys–. **Product:** the mature apolipoprotein N-terminus (a lipid-anchored, diacylglyceryl-Cys-headed protein) plus the released signal peptide. **Catalytic mechanism:** a membrane-embedded aspartyl-protease dyad (Asp126 + Asp145) activating a water molecule for nucleophilic attack, proceeding through a tetrahedral intermediate — the exact species that globomycin and myxovirescin mimic to inhibit the enzyme.

**Localization and topology:** LspA is embedded in the inner membrane with five TM helices; its active site sits within the membrane and faces the periplasmic/outer-leaflet side, where the lipid-anchored substrate presents its cleavage site. A mobile periplasmic helix gates the active site during turnover.

**Why it matters (essentiality):** Blocking LspA halts lipoprotein maturation and causes a toxic accumulation of unprocessed diacylglyceryl-prolipoprotein in the inner membrane, compromising envelope integrity. This is the biochemical basis for LspA's essentiality in Gram-negative bacteria and for its appeal as an antibiotic target. In *P. putida* KT2440 specifically, downstream lipoproteins whose maturation depends on LspA include envelope-integrity and biotechnologically relevant proteins such as the peptidoglycan-associated lipoprotein OprL/Pal ([PMID: 8626299](https://pubmed.ncbi.nlm.nih.gov/8626299/); [PMID: 38608840](https://pubmed.ncbi.nlm.nih.gov/38608840/)) and OprI ([PMID: 40607986](https://pubmed.ncbi.nlm.nih.gov/40607986/)) — illustrating the broad physiological reach of a single upstream processing enzyme.

---

## Evidence Base

| PMID | Title (abbreviated) | How it supports the findings |
|---|---|---|
| [26912896](https://pubmed.ncbi.nlm.nih.gov/26912896/) | *Structural basis of LspA action and inhibition by globomycin* | Crystal structure + mutagenesis of *P. aeruginosa* LspA; defines aspartyl-peptidase class, signal-peptide removal, and inner-membrane/periplasm topology (F001, F002, F004, F005) |
| [31919415](https://pubmed.ncbi.nlm.nih.gov/31919415/) | *Structures of S. aureus LspA with globomycin and myxovirescin* | Inhibitors act as non-cleavable tetrahedral-intermediate analogs; supports mechanism and substrate-groove specificity (F003, F006) |
| [35505611](https://pubmed.ncbi.nlm.nih.gov/35505611/) | *Conformational dynamics of LspA upon antibiotic/substrate binding* | Flexible active site accommodates diverse substrates; periplasmic helix gates catalysis; essentiality (F003, F004, F006) |
| [22232277](https://pubmed.ncbi.nlm.nih.gov/22232277/) | *Myxovirescin inhibits type II signal peptidase* | LspA cleaves prolipoprotein signal sequences; inhibition causes toxic pro-Lpp buildup (F002, F006) |
| [32490790](https://pubmed.ncbi.nlm.nih.gov/32490790/) | *Role of Lgt in lipoprotein biogenesis* | Establishes the upstream Lgt step producing LspA's diacylglyceryl-Cys substrate (F002) |
| [38712757](https://pubmed.ncbi.nlm.nih.gov/38712757/) | *Computational design of cyclic peptide LspA inhibitors* | States LspA is essential in Gram-negatives and a validated drug target (F006) |
| [32768648](https://pubmed.ncbi.nlm.nih.gov/32768648/) | *Optimization of globomycin analogs* | LspA as essential pathway member and antibacterial target; SAR of inhibitors (F006) |
| [40119522](https://pubmed.ncbi.nlm.nih.gov/40119522/) | *ssNMR of membrane proteins in lipid cubic phase* | Describes LspA as a ~20 kDa integral membrane enzyme (F006) |
| [24391051](https://pubmed.ncbi.nlm.nih.gov/24391051/) | *lspA redundancy in M. xanthus* | LspA orthologs conserve SPaseII residues; complement *E. coli* ΔlspA; confer globomycin/TA resistance when overexpressed (F005, F006) |
| [8626299](https://pubmed.ncbi.nlm.nih.gov/8626299/) | *P. putida Pal/OprL lipoprotein* | Example of a *P. putida* KT2440 lipoprotein (LspA substrate) important for envelope integrity (mechanistic context) |
| [38608840](https://pubmed.ncbi.nlm.nih.gov/38608840/) | *PHA proteomics; OprL as phasin* | Further characterizes a *P. putida* outer-membrane lipoprotein downstream of LspA processing (context) |
| [40607986](https://pubmed.ncbi.nlm.nih.gov/40607986/) | *Engineered vesicle production via OprF/OprI deletion* | OprI, a *P. putida* lipoprotein, matures via the LspA pathway (context) |

The evidence base is unusually strong for the *mechanism and general biology* of LspA because multiple orthologs have been solved crystallographically and dissected by mutagenesis and antibiotic-inhibition studies. The assignment to the specific *P. putida* protein (Q88Q91) rests on **orthology inference** — exact conservation of catalytic residues, family membership, membrane topology, and syntenic gene context — reinforced by an independent AlphaFold structural model that reproduces the paired-aspartate active-site geometry.

---

## Limitations and Knowledge Gaps

1. **No direct biochemical characterization of the *P. putida* enzyme.** All catalytic, structural, and inhibition data derive from orthologs (*E. coli*, *P. aeruginosa*, *S. aureus*, *M. xanthus*). The functional assignment for Q88Q91 is therefore inferential (homology + structure + synteny), albeit high-confidence. No purified-enzyme assay, crystal structure, or knockout phenotype specific to PP_0604 has been reported here.
2. **Essentiality in *P. putida* KT2440 is inferred, not demonstrated.** LspA essentiality is documented in *E. coli* and other Gram-negatives; a *P. putida*-specific conditional-lethal or transposon-essentiality confirmation was not located.
3. **Substrate repertoire in *P. putida* is not experimentally mapped.** While the lipobox specificity is well established generically, the full set of *P. putida* KT2440 lipoproteins processed by LspA has not been enumerated experimentally in this investigation.
4. **AlphaFold caveats.** The model confidently predicts the catalytic-dyad geometry, but a predicted static model cannot capture substrate-bound conformational states or membrane-embedding details that only experimental structures/dynamics provide.
5. **Regulation and expression** of lspA in *P. putida* (promoter, operon boundaries, growth-phase dependence) were inferred from the ileS–lspA synteny rather than measured.

---

## Proposed Follow-up Experiments / Actions

1. **Genetic essentiality test in *P. putida* KT2440.** Attempt a clean lspA (PP_0604) deletion; if non-recoverable, construct a conditional (e.g., inducible or complemented) mutant to confirm essentiality and characterize the depletion phenotype (accumulation of diacylglyceryl-prolipoprotein, envelope defects, sensitivity to SDS/EDTA).
2. **Heterologous complementation.** Test whether PP_0604 complements an *E. coli* ΔlspA strain (as demonstrated for *M. xanthus* orthologs, [PMID: 24391051](https://pubmed.ncbi.nlm.nih.gov/24391051/)), directly confirming SPaseII activity.
3. **Catalytic-residue mutagenesis.** Generate D126A and D145A variants and assay loss of prolipoprotein processing (e.g., via globomycin-comparable pro-Lpp accumulation assays), experimentally validating the predicted aspartyl dyad in the *P. putida* enzyme.
4. **In vitro reconstitution and inhibitor profiling.** Purify PP_0604 (a ~20 kDa integral membrane enzyme; cf. [PMID: 40119522](https://pubmed.ncbi.nlm.nih.gov/40119522/)), reconstitute in lipid, and measure globomycin/myxovirescin inhibition to confirm conserved pharmacology.
5. **Substrate mapping.** Use a globomycin-block plus radioactive-palmitate labeling strategy and proteomics to enumerate the *P. putida* KT2440 lipoprotein maturome dependent on LspA, including confirmed lipoproteins such as OprL/Pal and OprI.
6. **Structural determination.** Solve the *P. putida* LspA structure (X-ray in lipid cubic phase, cryo-EM, or ssNMR) to move the active-site geometry from prediction (AlphaFold) to experiment.

---

## Conclusion

**LspA (Q88Q91 / PP_0604) in *Pseudomonas putida* KT2440 is lipoprotein signal peptidase II (SPase II, EC 3.4.23.36): an essential, integral inner-membrane aspartyl protease that removes the signal peptide from diacylglyceryl-modified prolipoproteins by cleaving immediately N-terminal to the lipid-anchored lipobox cysteine.** It uses a conserved catalytic aspartate dyad (Asp126 + Asp145), acts at the inner-membrane/periplasm interface, and performs the committed second step of the universal lipoprotein biogenesis pathway (Lgt → LspA → Lnt). The assignment is made with high confidence from exact catalytic-residue and family conservation, conserved ileS–lspA synteny, an AlphaFold-predicted paired-aspartate active site, and the deep experimental characterization of its bacterial orthologs.


## Artifacts

- [OpenScientist final report](lspA-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](lspA-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:26912896
2. PMID:32490790
3. PMID:22232277
4. PMID:31919415
5. PMID:35505611
6. PMID:24391051
7. PMID:38712757
8. PMID:32768648
9. PMID:40119522
10. PMID:8626299
11. PMID:38608840
12. PMID:40607986