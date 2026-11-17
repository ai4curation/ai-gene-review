---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-11T09:51:58.729953'
end_time: '2026-11-11T10:03:43.519280'
duration_seconds: 704.79
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: ECOLI
  gene_id: sucD
  gene_symbol: sucD
  uniprot_accession: P0AGE9
  protein_description: 'RecName: Full=Succinate--CoA ligase [ADP-forming] subunit
    alpha {ECO:0000255|HAMAP-Rule:MF_01988}; EC=6.2.1.5 {ECO:0000255|HAMAP-Rule:MF_01988,
    ECO:0000269|PubMed:10353839}; AltName: Full=Succinyl-CoA synthetase subunit alpha
    {ECO:0000255|HAMAP-Rule:MF_01988}; Short=SCS-alpha {ECO:0000255|HAMAP-Rule:MF_01988};'
  gene_info: Name=sucD {ECO:0000255|HAMAP-Rule:MF_01988}; OrderedLocusNames=b0729,
    JW0718;
  organism_full: Escherichia coli (strain K12).
  protein_family: Belongs to the succinate/malate CoA ligase alpha subunit
  protein_domains: Cit_synth/succinyl-CoA_lig_AS. (IPR017440); Citrt_syn/SCS-alpha_CS.
    (IPR033847); CoA-bd. (IPR003781); CoA_lig_alpha. (IPR005810); NAD(P)-bd_dom_sf.
    (IPR036291)
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
citation_count: 16
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: sucD-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: sucD-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** P0AGE9
- **Protein Description:** RecName: Full=Succinate--CoA ligase [ADP-forming] subunit alpha {ECO:0000255|HAMAP-Rule:MF_01988}; EC=6.2.1.5 {ECO:0000255|HAMAP-Rule:MF_01988, ECO:0000269|PubMed:10353839}; AltName: Full=Succinyl-CoA synthetase subunit alpha {ECO:0000255|HAMAP-Rule:MF_01988}; Short=SCS-alpha {ECO:0000255|HAMAP-Rule:MF_01988};
- **Gene Information:** Name=sucD {ECO:0000255|HAMAP-Rule:MF_01988}; OrderedLocusNames=b0729, JW0718;
- **Organism (full):** Escherichia coli (strain K12).
- **Protein Family:** Belongs to the succinate/malate CoA ligase alpha subunit
- **Key Domains:** Cit_synth/succinyl-CoA_lig_AS. (IPR017440); Citrt_syn/SCS-alpha_CS. (IPR033847); CoA-bd. (IPR003781); CoA_lig_alpha. (IPR005810); NAD(P)-bd_dom_sf. (IPR036291)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "sucD" matches the protein description above**
2. **Verify the organism is correct:** Escherichia coli (strain K12).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'sucD' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **sucD** (gene ID: sucD, UniProt: P0AGE9) in ECOLI.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *sucD* (P0AGE9) — Succinyl-CoA Synthetase α-Subunit of *Escherichia coli* K-12

**Gene:** `sucD` (OrderedLocusNames b0729, JW0718) · **Organism:** *Escherichia coli* K-12
**Protein:** Succinate–CoA ligase [ADP-forming] subunit alpha (SCS-α); **EC 6.2.1.5**
**Family:** Succinate/malate CoA-ligase α-subunit (ATP-grasp / CoA-binding superfamily)

---

## Summary

The gene **_sucD_** (ordered locus **b0729** / **JW0718**; UniProt **P0AGE9**) of *Escherichia coli* K-12 encodes the **α-subunit of succinyl-CoA synthetase (SCS)**, also called **succinate–CoA ligase [ADP-forming]** or succinate thiokinase, **EC 6.2.1.5**. This enzyme catalyzes the only **substrate-level phosphorylation** step of the citric acid (TCA) cycle, carrying out the reversible reaction:

> **succinyl-CoA + Pᵢ + NDP ⇌ succinate + CoA + NTP** (N = adenosine or guanosine)

The identity, organism, protein family, and catalytic residues given in the UniProt record were all independently verified against the primary literature and against the P0AGE9 sequence itself. There is **no gene-symbol ambiguity**: all authoritative *E. coli* literature using the symbol *sucD* refers to this exact, well-characterized protein.

The **α-subunit (sucD) is the catalytic heart of the enzyme.** It carries the active-site **histidine (His246α)** that is transiently phosphorylated during catalysis (forming a 3-phosphohistidine intermediate) and provides the **binding site for coenzyme A / succinyl-CoA**. The companion **β-subunit (sucC)** supplies the **nucleotide-binding site**, which lies in an ATP-grasp fold roughly **35 Å away** from His246α. Consequently, the phosphoryl group is relayed across the enzyme by a large-scale conformational movement of the His246α loop — the "swinging histidine." The functional enzyme is a **soluble, cytoplasmic (αβ)₂ heterotetramer** in which each α-subunit contacts only β-subunits, and the two active sites are built at α/β interfaces.

Physiologically, *sucD* is the distal gene of the nine-gene **_sdhCDAB–sucABCD_** operon encoding core aerobic TCA-cycle enzymes. Its expression is coordinately regulated with the 2-oxoglutarate dehydrogenase genes (*sucAB*) and is **repressed anaerobically through ArcA and FNR**, matching its role in aerobic energy metabolism. The enzyme conserves the thioester-bond energy of succinyl-CoA as a nucleoside triphosphate; in *E. coli* it can use both GDP/GTP and ADP/ATP but **prefers ADP/ATP**.

---

## Gene / Protein Identity Verification

Because gene symbols can be ambiguous, the first priority of this investigation was to confirm the target. All four UniProt-supplied identity checks passed:

| Verification criterion | Expected (UniProt P0AGE9) | Found in literature / sequence | Status |
|---|---|---|---|
| Gene symbol matches protein | *sucD* = SCS α-subunit | Buck et al. 1985: *sucD* encodes the α-subunit ([PMID: 3002435](https://pubmed.ncbi.nlm.nih.gov/3002435/)) | ✅ Confirmed |
| Organism | *E. coli* K-12 | All cited primary work is *E. coli* K-12 | ✅ Confirmed |
| Protein family / domains | Succinate/malate CoA-ligase α; CoA-binding; NAD(P)-binding fold | Crystal structures confirm CoA-binding + nucleotide-binding motifs on α ([PMID: 8144675](https://pubmed.ncbi.nlm.nih.gov/8144675/)) | ✅ Confirmed |
| No conflicting same-symbol gene | — | No ambiguity; all *E. coli sucD* literature is consistent | ✅ Confirmed |

The P0AGE9 canonical sequence (289 aa including the initiator Met; 288 aa mature) matches the length deduced by Buck et al. 1985 (288 codons). The catalytic histidine appears in the motif `...KGKRMG`**`H`**`AGAI...` (full-length His247 = His246 in the Met-cleaved "mature" numbering used throughout the literature as "His246α"); the conserved cysteine appears as `...RMIGPN`**`C`**`PGVI...` ("Cys123α"); and the N-terminus (`MSILIDKNTKVICQGF`**`TGSQ`**`...`) carries the conserved succinyl-CoA-ligase α CoA/nucleotide-binding signature (Finding F008). **Conclusion:** this report describes the correct protein with high confidence.

---

## Key Findings

### Finding 1 — *sucD* encodes the catalytic α-subunit of succinyl-CoA synthetase (EC 6.2.1.5)

The foundational identification comes from **Buck, Spencer & Guest (1985)**, who sequenced the *E. coli sucABCD* gene cluster and showed that *"The sucD gene comprises 864 base pairs (288 codons, excluding the start and stop codons), and it encodes a product of Mr 29 644, corresponding to the alpha subunit of succinyl-CoA synthetase"* ([PMID: 3002435](https://pubmed.ncbi.nlm.nih.gov/3002435/)). This directly ties the gene symbol to the α-subunit protein of calculated mass ~29.6 kDa.

The catalytic role in central metabolism is stated plainly by **Fraser, James, Bridger & Wolodko (1999)**: *"Succinyl-CoA synthetase (SCS) carries out the substrate-level phosphorylation of GDP or ADP in the citric acid cycle"* ([PMID: 9917402](https://pubmed.ncbi.nlm.nih.gov/9917402/)). SCS is the **only TCA-cycle enzyme that generates a nucleoside triphosphate directly** (rather than a reduced cofactor such as NADH/FADH₂), making it the sole point of net substrate-level ATP/GTP conservation in the cycle. The full reversible reaction, `succinyl-CoA + Pᵢ + NDP ⇌ succinate + CoA + NTP`, is given by Fraser et al. 2000 ([PMID: 10873456](https://pubmed.ncbi.nlm.nih.gov/10873456/)). (Finding F001)

### Finding 2 — The α-subunit carries the catalytic phosphohistidine (His246α) and the CoA-binding site

The 2.5 Å crystal structure of *E. coli* SCS by **Wolodko, Fraser, James & Bridger (1994)** localized both key chemical functions to the α-subunit: *"One molecule of coenzyme A is bound to each alpha-subunit at a typical nucleotide-binding motif, and His-246 of each alpha-subunit is phosphorylated. This phosphohistidine, a catalytic intermediate, is stabilized by two helix dipoles (the 'power' helices), one from each of the two subunit types"* ([PMID: 8144675](https://pubmed.ncbi.nlm.nih.gov/8144675/)).

This establishes two cardinal facts: (1) **CoA/succinyl-CoA binds the α-subunit**, and (2) **His246α is the residue transiently phosphorylated** during catalysis. The "power helix" dipoles that stabilize the labile phosphohistidine are contributed one each by α and β — which is why the chemistry requires the intact heterodimer. Buck et al. 1985 had already noted that the α-subunit contains a 12-residue stretch identical to a previously isolated active-site histidine peptide, foreshadowing this structural result. The phosphorylated-His246α intermediate was later confirmed in the ADP complex structure (Joyce et al. 2000, [PMID: 10625475](https://pubmed.ncbi.nlm.nih.gov/10625475/)). (Finding F002)

### Finding 3 — SCS is an (αβ)₂ heterotetramer; α contacts only β, and active sites lie at α/β interfaces

Wolodko et al. 1994 also defined the quaternary architecture: *"The quaternary organization of the E. coli enzyme is an alpha 2 beta 2 heterotetramer. In this tetramer, the alpha-subunits interact only with the beta-subunits, whereas the beta-subunits interact to form the dimer of alpha beta-dimers. The two active site pockets are located at regions of contact between alpha- and beta-subunits"* ([PMID: 8144675](https://pubmed.ncbi.nlm.nih.gov/8144675/)).

The structural implication is that the **α-subunit cannot function alone** — its active site is completed by the β-subunit, and the tetramer is held together by β–β contacts. Fraser et al. 1999 refined the (αβ)₂ tetramer at 2.3 Å with two αβ copies per asymmetric unit ([PMID: 9917402](https://pubmed.ncbi.nlm.nih.gov/9917402/)). This explains why *sucC* and *sucD* are co-expressed and **translationally coupled** (the *sucC* stop codon overlaps the *sucD* start by one nucleotide; Buck et al. 1985), ensuring stoichiometric 1:1 subunit production. (Finding F003)

### Finding 4 — The phosphoryl relay requires a ~35 Å movement of His246α ("swinging histidine")

A defining mechanistic feature of SCS is that its two chemical sub-sites are far apart. Fraser et al. 1999 reasoned: *"the binding site for the nucleotide may reside in the N-terminal domain of the beta-subunit. If this is so, the catalytic histidine residue would have to move about 35 A to react with the nucleotide"* ([PMID: 9917402](https://pubmed.ncbi.nlm.nih.gov/9917402/)).

This was confirmed experimentally. **Joyce et al. (2000)** solved the structure with *"an ADP-Mg(2+) complex bound in the ATP-grasp fold of the N-terminal domain of each beta-subunit"* ([PMID: 10625475](https://pubmed.ncbi.nlm.nih.gov/10625475/)), proving the nucleotide binds on β, distant from His246α on α. Earlier, **Joyce et al. (1999)** had localized the nucleotide site to the N-terminal ATP-grasp domain of β by 8-azido-ATP photoaffinity labeling and site-directed mutagenesis, concluding the H246α loop moves between the two sites during catalysis ([PMID: 10353839](https://pubmed.ncbi.nlm.nih.gov/10353839/)). The mechanism therefore proceeds in discrete chemical steps linked by a large conformational excursion of the His246α loop — the "swinging histidine" model. (Finding F004)

### Finding 5 — *E. coli* SCS uses both GDP/GTP and ADP/ATP, preferring ADP/ATP; Cys123α tunes but is not a covalent intermediate

Nucleotide specificity is a property of the β-subunit site, not α. **Joyce et al. (2012)** contrast organisms: *"...Escherichia coli SCS, which uses GDP/GTP but prefers ADP/ATP"* ([PMID: 22751660](https://pubmed.ncbi.nlm.nih.gov/22751660/)). Specificity is governed by residues around the β-site; e.g., the P20βQ mutation lowered the apparent Kₘ for GTP more than 5-fold (Joyce et al. 1999, [PMID: 10353839](https://pubmed.ncbi.nlm.nih.gov/10353839/)). The true nucleotide substrate is an **ADP·Mg²⁺ complex** (Joyce et al. 2000, [PMID: 10625475](https://pubmed.ncbi.nlm.nih.gov/10625475/)), so Mg²⁺ is required.

A conserved α-subunit residue, **Cys123α**, lies near both the CoA-binding site and His246α, raising the possibility of a covalent succinyl-thioester intermediate. **Hidber et al. (2007)** tested this directly by mutating Cys123α to Ala/Ser/Thr/Val; all mutants remained catalytically active, and the authors concluded: *"This proved that the specific formation of a thioester bond with Cys123alpha is not part of the catalytic mechanism"* ([PMID: 17642514](https://pubmed.ncbi.nlm.nih.gov/17642514/)). The residue's *size* nonetheless matters for optimal activity, so it plays a tuning/structural role near the active site rather than a direct chemical one. (Finding F005)

### Finding 6 — His246α is catalytically essential; the enzyme is a soluble cytoplasmic protein

The essentiality of His246α was demonstrated by loss-of-function genetics. **Buck & Guest (1989)** replaced the phosphorylation-site histidine with aspartate and found: *"No activity was detected after the histidine residue at the phosphorylation site of the alpha-subunit was replaced by aspartate (His-246 alpha----Asp)"* ([PMID: 2548486](https://pubmed.ncbi.nlm.nih.gov/2548486/)). This is direct causal proof that His246α of the *sucD* product is the indispensable catalytic residue.

The same study established subcellular localization by biochemical fractionation: upon overexpression of *sucCD*, *"the alpha and beta subunits accounted for almost 30% of the protein in supernatant fractions of the cell-free extracts"* ([PMID: 2548486](https://pubmed.ncbi.nlm.nih.gov/2548486/)). Recovery in the soluble supernatant (not the membrane/pellet fraction) identifies SCS as a **soluble, cytoplasmic enzyme**, consistent with its role in the cytosolic TCA cycle of *E. coli* and with the absence of any membrane-spanning or targeting sequence. The study further showed that the β-subunit CoA-site residues Trp-43β/His-50β are essential, while Cys-47β is not. (Finding F006)

### Finding 7 — *sucD* is the distal gene of the *sdhCDAB–sucABCD* operon, co-regulated with aerobic TCA genes and repressed anaerobically by ArcA/FNR

Buck et al. 1985/1986 established the genetic organization: *sucC/sucD* are the distal genes of the *sucABCD* operon within the nine-gene citric-acid-cycle cluster *gltA–sdhCDAB–sucABCD*, and *"expression of succinyl-CoA synthetase is coordinately regulated with 2-oxoglutarate dehydrogenase"* ([PMID: 3543212](https://pubmed.ncbi.nlm.nih.gov/3543212/)).

Regulation was characterized by **Park, Chao & Gunsalus (1997)**, who showed *sucABCD* is primarily transcribed from the upstream *sdhC* promoter, varies ~14-fold with carbon source and ~4-fold with oxygen, and is anaerobically repressed: *"The negative control of sucABCD gene expression seen under anaerobic conditions, like that for the sdhCDAB genes, is provided by the arcA and fnr gene products"* ([PMID: 9209026](https://pubmed.ncbi.nlm.nih.gov/9209026/)). **Cunningham & Guest (1998)** added that the weaker internal *suc* promoter is repressed by IHF and partially activated by σ³⁸ (RpoS), with primary regulation occurring at the upstream *sdh* promoter and extensive RNase III processing of the long readthrough transcript ([PMID: 9720032](https://pubmed.ncbi.nlm.nih.gov/9720032/)). Together these place *sucD* firmly in the **aerobic TCA-cycle regulon**, expressed when a complete oxidative cycle operates. (Finding F007)

### Finding 8 — Sequence-level confirmation of catalytic residues in P0AGE9

As an internal consistency check, the P0AGE9 canonical sequence was inspected directly. The catalytic His246α appears in the motif `KGKRMG`**`H`**`AGAI` (full-length His247 = mature His246); the conserved Cys123α appears as `RMIGPN`**`C`**`PGVI` (full-length Cys124 = mature Cys123); and the N-terminal CoA-ligase α signature `...GF`**`TGSQ`**`...` is present. These map exactly to the InterPro domain assignments (IPR003781 CoA-binding; IPR005810 CoA-ligase α; IPR017440 active-site signature), independently corroborating the structural and mutagenesis evidence. All literature-reported functional positions are confirmed at the expected places in the actual sequence, closing the loop between annotation, structure, and sequence. (Finding F008)

---

## Mechanistic Model / Interpretation

SCS catalyzes a **three-step, ping-pong mechanism** that couples the free energy of the succinyl-CoA thioester bond to phosphoanhydride-bond (NTP) synthesis. The α-subunit (sucD) is central to the first two steps; the β-subunit (sucC) performs the third.

```
STEP 1 (α-site):   succinyl-CoA + Pi  →  succinyl-phosphate + CoA
                   (CoA and succinyl-CoA bound at the α-subunit)

STEP 2 (α-site):   succinyl-phosphate + His246α  →  P~His246α + succinate
                   (His246α becomes 3-phosphohistidine; phosphoryl captured)

   ── His246α loop swings ~35 Å from the α CoA/succinate site
      to the β nucleotide (ATP-grasp) site ──

STEP 3 (β-site):   P~His246α + NDP  →  His246α + NTP
                   (phosphoryl transferred to ADP/GDP → ATP/GTP)
```

A schematic of the subunit architecture and the two spatially separated sub-sites:

```
            (αβ)2 HETEROTETRAMER   —   soluble, cytoplasmic
      ┌─────────────────────────────────────────────────┐
      │   α (sucD, P0AGE9)            β (sucC)            │
      │  ┌───────────────┐         ┌────────────────┐    │
      │  │ CoA / succinyl │  ~35 Å │ nucleotide site │   │
      │  │  -CoA site     │◄──────►│ (ATP-grasp fold)│   │
      │  │  His246α ●     │ swing  │  ADP/GDP·Mg2+   │    │
      │  │  Cys123α (tune)│        │  P20β specificity│   │
      │  └───────┬───────┘         └───────┬────────┘     │
      │          └── "power helices" (α+β) stabilize P~His │
      │   α contacts ONLY β   │   β–β contacts form dimer   │
      └─────────────────────────────────────────────────┘
```

**Division of labor.** The α-subunit (sucD) supplies the chemistry of CoA/succinyl handling and the mobile phosphocarrier histidine; the β-subunit supplies the nucleotide site and determines nucleotide specificity. Neither subunit is catalytically competent alone — the active site is built at the α/β interface, and both "power helix" dipoles (one per subunit type) are needed to stabilize the otherwise highly labile phosphohistidine intermediate. This explains the strict genetic coupling of *sucC* and *sucD*.

**Physiological context.** Within the TCA cycle, SCS acts between 2-oxoglutarate dehydrogenase (which produces succinyl-CoA) and succinate dehydrogenase (which oxidizes succinate). It is the single cycle step that conserves thioester energy as a nucleoside triphosphate (substrate-level phosphorylation). In *E. coli*, which prefers ADP/ATP, this yields ATP directly. Succinyl-CoA is also a biosynthetic branch-point metabolite (e.g., for lysine/methionine and tetrapyrrole/heme pathways), so SCS activity helps set the cellular succinyl-CoA/CoA balance. The operon-level regulation (aerobic induction, ArcA/FNR anaerobic repression) matches the aerobic functioning of the full oxidative TCA cycle; a reported phenotype in which Δ*sucC*/Δ*sucD* mutants show altered high-hydrostatic-pressure resistance via elevated RpoS activity ([PMID: 30497599](https://pubmed.ncbi.nlm.nih.gov/30497599/)) is a pleiotropic consequence rather than the primary function.

**Comparative perspective.** Across species the enzyme family shows diversity in nucleotide specificity and quaternary structure, but the catalytic logic is conserved. Pig GTP-specific SCS is an αβ-heterodimer with CoA bound to the α-subunit N-terminal domain, its free thiol extending toward the catalytic histidine ([PMID: 26249701](https://pubmed.ncbi.nlm.nih.gov/26249701/)); the pig enzyme's phosphorylated/dephosphorylated structures confirm the power-helix stabilization motif ([PMID: 10873456](https://pubmed.ncbi.nlm.nih.gov/10873456/)). The same swinging-phosphohistidine chemistry recurs in related enzymes such as ATP-citrate lyase, where His273α is the phosphorylated residue ([PMID: 12135479](https://pubmed.ncbi.nlm.nih.gov/12135479/)), and the phosphohistidine strategy is shared with nucleoside diphosphate kinase ([PMID: 7669763](https://pubmed.ncbi.nlm.nih.gov/7669763/)). These cross-family comparisons reinforce, rather than challenge, the *E. coli sucD* assignment.

---

## Evidence Base

| PMID | Study (abbrev.) | Key contribution to this annotation |
|---|---|---|
| [3002435](https://pubmed.ncbi.nlm.nih.gov/3002435/) | Buck et al. 1985, *Primary structure of E. coli SCS* | Defines *sucD* = 864 bp/288 codons → α-subunit (Mr 29,644); operon structure; translational coupling |
| [3543212](https://pubmed.ncbi.nlm.nih.gov/3543212/) | Buck et al. 1986, *Cloning and expression* | *sucCD* co-regulated with 2-oxoglutarate dehydrogenase |
| [2548486](https://pubmed.ncbi.nlm.nih.gov/2548486/) | Buck & Guest 1989, *Overexpression & mutagenesis* | His246α→Asp abolishes activity; soluble (supernatant) localization; α₂β₂ expression |
| [8144675](https://pubmed.ncbi.nlm.nih.gov/8144675/) | Wolodko et al. 1994, *2.5 Å crystal structure* | CoA + phospho-His246 on α; α₂β₂ assembly; power helices; active sites at α/β interface |
| [9917402](https://pubmed.ncbi.nlm.nih.gov/9917402/) | Fraser et al. 1999, *Detailed structure* | Confirms substrate-level phosphorylation; predicts ~35 Å His movement; nucleotide site on β |
| [10353839](https://pubmed.ncbi.nlm.nih.gov/10353839/) | Joyce et al. 1999, *Nucleotide-binding site probe* | Photoaffinity + mutagenesis localize nucleotide site to β N-terminal ATP-grasp; P20β specificity; ~35 Å relay |
| [10625475](https://pubmed.ncbi.nlm.nih.gov/10625475/) | Joyce et al. 2000, *ADP-binding site* | ADP-Mg²⁺ bound in β ATP-grasp fold; confirms spatial separation |
| [17642514](https://pubmed.ncbi.nlm.nih.gov/17642514/) | Hidber et al. 2007, *Cys123α* | Cys123α not a covalent intermediate; size tunes activity |
| [22751660](https://pubmed.ncbi.nlm.nih.gov/22751660/) | Joyce et al. 2012, *T. aquaticus SCS* | *E. coli* SCS uses GDP/GTP but prefers ADP/ATP |
| [9209026](https://pubmed.ncbi.nlm.nih.gov/9209026/) | Park et al. 1997, *Aerobic regulation* | ArcA/FNR anaerobic repression; carbon/oxygen responsiveness |
| [9720032](https://pubmed.ncbi.nlm.nih.gov/9720032/) | Cunningham & Guest 1998, *Transcription of operon* | IHF repression, σ³⁸ activation; primary control at upstream *sdh* promoter; RNase III processing |
| [10873456](https://pubmed.ncbi.nlm.nih.gov/10873456/) | Fraser et al. 2000, *Pig GTP-specific SCS* | Reaction equation; power-helix stabilization in phospho/dephospho forms |
| [26249701](https://pubmed.ncbi.nlm.nih.gov/26249701/) | Pig SCS·CoA complex 2015 | CoA binds α N-terminal domain; thiol toward catalytic His (comparative support) |
| [12135479](https://pubmed.ncbi.nlm.nih.gov/12135479/) | ATP-citrate lyase 2002 | Related phosphohistidine chemistry (His273α) in a homologous enzyme |
| [7669763](https://pubmed.ncbi.nlm.nih.gov/7669763/) | NDP kinase phosphohistidine 1995 | Phosphohistidine mechanism precedent; compares to SCS |
| [31282474](https://pubmed.ncbi.nlm.nih.gov/31282474/) | Blastocystis SCS 2019 | "Gatekeeper" residue theory of nucleotide specificity (comparative) |
| [30497599](https://pubmed.ncbi.nlm.nih.gov/30497599/) | HHP-resistance screen 2018 | Δ*sucC*/Δ*sucD* increase HHP resistance via RpoS — physiological context |

**Strength of the evidence.** The core annotation rests on **direct, precise experimental evidence**: an X-ray crystal structure visualizing CoA and phospho-His246 on the α-subunit ([PMID: 8144675](https://pubmed.ncbi.nlm.nih.gov/8144675/)); loss-of-function mutagenesis proving His246α is essential ([PMID: 2548486](https://pubmed.ncbi.nlm.nih.gov/2548486/)); and photoaffinity labeling plus additional crystal structures placing the nucleotide on β ([PMID: 10353839](https://pubmed.ncbi.nlm.nih.gov/10353839/), [PMID: 10625475](https://pubmed.ncbi.nlm.nih.gov/10625475/)). These are gold-standard, low-throughput biochemical/structural studies specific to *E. coli* — exactly the type of evidence the research question prioritizes. High-throughput/physiological data (e.g., the HHP-resistance transposon screen, [PMID: 30497599](https://pubmed.ncbi.nlm.nih.gov/30497599/)) are consistent but peripheral, providing context rather than mechanistic definition.

### Supported vs. Refuted Hypotheses

**Supported**
- sucD = catalytic α-subunit of SCS; EC 6.2.1.5; TCA-cycle substrate-level phosphorylation. ✔
- His246α is the essential, transiently phosphorylated catalytic residue. ✔
- CoA/succinyl-CoA binds the α-subunit; nucleotide binds the β-subunit; His246α relays the phosphoryl group across ~35 Å. ✔
- Obligate (αβ)₂ heterotetramer; soluble/cytoplasmic. ✔
- ADP/ATP preferred over GDP/GTP in *E. coli*. ✔

**Refuted / ruled out**
- A covalent succinyl-cysteine intermediate at Cys123α is **not** part of the mechanism ([PMID: 17642514](https://pubmed.ncbi.nlm.nih.gov/17642514/)). ✘
- Nucleotide specificity is **not** determined by sucD residues but by the β-subunit ([PMID: 10353839](https://pubmed.ncbi.nlm.nih.gov/10353839/)). ✘

---

## Limitations and Knowledge Gaps

1. **Static structural snapshots.** The ~35 Å "swinging histidine" motion is inferred from multiple crystal structures of distinct catalytic states (free, phosphorylated, ADP-bound) rather than from a single continuous dynamic measurement. Time-resolved, cryo-EM, or computational studies of the loop trajectory in *E. coli* SCS are not available in the reviewed literature.

2. **In vivo nucleotide usage.** Although *E. coli* SCS can use GDP/GTP and prefers ADP/ATP *in vitro* ([PMID: 22751660](https://pubmed.ncbi.nlm.nih.gov/22751660/)), the actual in vivo partitioning between ADP/ATP and GDP/GTP under different growth conditions was not quantified here, and precise steady-state kinetic constants (Kₘ, k_cat) were not compiled.

3. **Role of Cys123α.** Its size affects optimal activity ([PMID: 17642514](https://pubmed.ncbi.nlm.nih.gov/17642514/)), but the precise structural reason (steric gating of CoA/succinyl positioning vs. His246α mobility) is not fully resolved.

4. **Localization inference.** Localization evidence is biochemical (solubility, absence of targeting signals) rather than from direct imaging.

5. **Regulatory fine structure.** While ArcA/FNR anaerobic repression and the dominant upstream *sdh* promoter are established, the quantitative contribution of each promoter/processing site to steady-state *sucD* protein levels across growth phases is not precisely delineated.

---

## Proposed Follow-up Experiments / Actions

1. **Time-resolved / cryo-EM capture of the swinging histidine.** Use time-resolved crystallography or cryo-EM of *E. coli* SCS trapped in intermediate states to directly visualize the His246α loop trajectory between the α and β sub-sites.

2. **Quantify in vivo NTP output.** Use ¹³C/³¹P metabolic flux or in-cell assays to measure whether SCS produces predominantly ATP vs. GTP under aerobic vs. microaerobic growth, and compile Kₘ/k_cat for ADP vs. GDP.

3. **Dissect Cys123α geometry.** Combine the existing Cys123α mutant panel with structural determination to clarify how side-chain volume at position 123α influences substrate positioning and catalytic rate.

4. **Promoter contribution mapping.** Build chromosomal reporter fusions isolating each promoter/RNase III processing site in *sdhCDAB–sucABCD* to quantify their individual contributions to *sucD* expression across carbon sources and oxygen tensions.

5. **Mechanism of the RpoS/HHP link.** Test whether altered succinyl-CoA/succinate pools in Δ*sucD* cells causally drive elevated basal RpoS activity, clarifying the connection to stress resistance.

---

### Key References

- Wolodko et al. 1994, *J Biol Chem* — [PMID: 8144675](https://pubmed.ncbi.nlm.nih.gov/8144675/) (2.5 Å structure; α₂β₂; His246α phospho-intermediate).
- Fraser et al. 1999, *J Mol Biol* — [PMID: 9917402](https://pubmed.ncbi.nlm.nih.gov/9917402/) (detailed 2.3 Å structure; ~35 Å movement).
- Joyce et al. 2000, *Biochemistry* — [PMID: 10625475](https://pubmed.ncbi.nlm.nih.gov/10625475/) (ADP·Mg²⁺ bound in β ATP-grasp fold).
- Joyce et al. 1999 — [PMID: 10353839](https://pubmed.ncbi.nlm.nih.gov/10353839/) (nucleotide-site mapping; β-subunit).
- Buck & Guest 1989 — [PMID: 2548486](https://pubmed.ncbi.nlm.nih.gov/2548486/) (His246α→Asp inactivation; α₂β₂ expression; soluble).
- Buck, Spencer & Guest 1985/1986 — [PMID: 3002435](https://pubmed.ncbi.nlm.nih.gov/3002435/), [PMID: 3543212](https://pubmed.ncbi.nlm.nih.gov/3543212/) (sucD sequence, operon).
- Hidber et al. 2007 — [PMID: 17642514](https://pubmed.ncbi.nlm.nih.gov/17642514/) (Cys123α not a covalent intermediate).
- Joyce et al. 2012 — [PMID: 22751660](https://pubmed.ncbi.nlm.nih.gov/22751660/) (*E. coli* prefers ADP/ATP).
- Park et al. 1997; Cunningham & Guest 1998 — [PMID: 9209026](https://pubmed.ncbi.nlm.nih.gov/9209026/), [PMID: 9720032](https://pubmed.ncbi.nlm.nih.gov/9720032/) (operon regulation).
- Fraser et al. 2000 — [PMID: 10873456](https://pubmed.ncbi.nlm.nih.gov/10873456/) (reversible reaction; comparative structures).


## Artifacts

- [OpenScientist final report](sucD-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](sucD-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:3002435
2. PMID:8144675
3. PMID:9917402
4. PMID:10873456
5. PMID:10625475
6. PMID:10353839
7. PMID:22751660
8. PMID:17642514
9. PMID:2548486
10. PMID:3543212
11. PMID:9209026
12. PMID:9720032
13. PMID:30497599
14. PMID:26249701
15. PMID:12135479
16. PMID:7669763