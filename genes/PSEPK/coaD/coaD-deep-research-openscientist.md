---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-18T13:07:59.406654'
end_time: '2026-07-18T13:29:56.397285'
duration_seconds: 1316.99
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: coaD
  gene_symbol: coaD
  uniprot_accession: Q88CQ7
  protein_description: 'RecName: Full=Phosphopantetheine adenylyltransferase {ECO:0000255|HAMAP-Rule:MF_00151};
    EC=2.7.7.3 {ECO:0000255|HAMAP-Rule:MF_00151}; AltName: Full=Dephospho-CoA pyrophosphorylase
    {ECO:0000255|HAMAP-Rule:MF_00151}; AltName: Full=Pantetheine-phosphate adenylyltransferase
    {ECO:0000255|HAMAP-Rule:MF_00151}; Short=PPAT {ECO:0000255|HAMAP-Rule:MF_00151};'
  gene_info: Name=coaD {ECO:0000255|HAMAP-Rule:MF_00151}; OrderedLocusNames=PP_5123;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the bacterial CoaD family. {ECO:0000255|HAMAP-
  protein_domains: Cyt_trans-like. (IPR004821); PPAT. (IPR001980); Rossmann-like_a/b/a_fold.
    (IPR014729); CTP_transf_like (PF01467)
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
  path: coaD-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: coaD-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88CQ7
- **Protein Description:** RecName: Full=Phosphopantetheine adenylyltransferase {ECO:0000255|HAMAP-Rule:MF_00151}; EC=2.7.7.3 {ECO:0000255|HAMAP-Rule:MF_00151}; AltName: Full=Dephospho-CoA pyrophosphorylase {ECO:0000255|HAMAP-Rule:MF_00151}; AltName: Full=Pantetheine-phosphate adenylyltransferase {ECO:0000255|HAMAP-Rule:MF_00151}; Short=PPAT {ECO:0000255|HAMAP-Rule:MF_00151};
- **Gene Information:** Name=coaD {ECO:0000255|HAMAP-Rule:MF_00151}; OrderedLocusNames=PP_5123;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the bacterial CoaD family. {ECO:0000255|HAMAP-
- **Key Domains:** Cyt_trans-like. (IPR004821); PPAT. (IPR001980); Rossmann-like_a/b/a_fold. (IPR014729); CTP_transf_like (PF01467)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "coaD" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'coaD' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **coaD** (gene ID: coaD, UniProt: Q88CQ7) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# coaD (PP_5123, UniProt Q88CQ7): Phosphopantetheine Adenylyltransferase of *Pseudomonas putida* KT2440

**Gene:** *coaD* (OrderedLocusName PP_5123)
**Protein:** Phosphopantetheine adenylyltransferase (PPAT); also called dephospho-CoA pyrophosphorylase / pantetheine-phosphate adenylyltransferase
**UniProt:** Q88CQ7 · **EC:** 2.7.7.3 · **Organism:** *Pseudomonas putida* KT2440 (PSEPK)

## Summary

The gene **coaD** (ordered locus **PP_5123**, UniProt **Q88CQ7**) of *Pseudomonas putida* KT2440 encodes **phosphopantetheine adenylyltransferase (PPAT; EC 2.7.7.3)**, also historically called dephospho-CoA pyrophosphorylase and pantetheine-phosphate adenylyltransferase. PPAT catalyzes the **penultimate (4th of 5) step of the universal coenzyme A (CoA) biosynthetic pathway**: the reversible, Mg-ATP–dependent transfer of an adenylyl group to (R)-4′-phosphopantetheine (PhP/PNS), producing **3′-dephospho-CoA (dPCoA) and pyrophosphate**. This assignment is unambiguous and is supported convergently by three independent lines of evidence: (i) primary biochemical and structural literature on close bacterial orthologs, including the enzyme from the sister species *Pseudomonas aeruginosa*; (ii) direct sequence analysis of Q88CQ7 itself, which is 64% identical to the biochemically characterized *E. coli* CoaD and retains every catalytic residue; and (iii) curated UniProt/KEGG annotation of the *P. putida* protein.

The enzyme is a **soluble, cytoplasmic homohexamer** in which each ~161-residue protomer folds into a dinucleotide-binding (Rossmann-like α/β/α) fold. It carries out catalysis via an **in-line (SN2-like) displacement mechanism** in which the 4′-phosphopantetheine phosphate attacks the α-phosphate of ATP; the reaction is oriented by a small set of invariant active-site residues (Thr9, His17, Arg87, Arg90 in *P. putida* numbering). PPAT is a **rate-limiting control point** of CoA synthesis and is **allosterically feedback-inhibited by the pathway end-product CoA** (and by acetyl-CoA), competitively with its substrates. It hands its product, dephospho-CoA, to a separate enzyme, dephospho-CoA kinase (CoaE), which phosphorylates the 3′-OH to complete CoA.

Because CoA and its thioester derivatives are central to fatty-acid metabolism, the TCA cycle, and — in *P. putida* specifically — to the many CoA-dependent catabolic and polyhydroxyalkanoate (PHA)-biosynthetic pathways that make this organism a versatile metabolic chassis, PPAT sits at a metabolic bottleneck upstream of all acyl-CoA chemistry. The bacterial CoaD family is structurally and mechanistically distinct from the bifunctional human enzyme (COASY), which is one reason the CoA-biosynthetic pathway is an actively pursued antibacterial drug target.

---

## Key Findings

### F001 — coaD encodes phosphopantetheine adenylyltransferase (PPAT, EC 2.7.7.3), catalyzing the penultimate step of CoA biosynthesis

The core functional assignment rests on the classical biochemical characterization of the *E. coli* ortholog. Geerlof and colleagues purified recombinant PPAT and showed that it **"catalyzes the penultimate step in coenzyme A (CoA) biosynthesis: the reversible adenylation of 4′-phosphopantetheine yielding 3′-dephospho-CoA and pyrophosphate"** ([PMID: 10480925](https://pubmed.ncbi.nlm.nih.gov/10480925/)). That same study **renamed the gene coaD** and noted that it "is found in a wide range of microorganisms, indicating that it plays a key role in the synthesis of 3′-dephospho-CoA." Overexpression yielded highly purified recombinant PPAT that assembled as a **homohexamer of 108 kDa**. Importantly, the purified enzyme **lacked dephospho-CoA kinase activity**, establishing PPAT as a dedicated enzyme for the fourth of five CoA-biosynthesis steps rather than a bifunctional enzyme.

The kinetic behavior of the enzyme was subsequently defined by Miller et al., who showed the reaction follows a **random bi-bi ternary-complex mechanism** ([PMID: 17873050](https://pubmed.ncbi.nlm.nih.gov/17873050/)). The reaction catalyzed is:

> (R)-4′-phosphopantetheine + ATP + H⁺ ⇌ 3′-dephospho-CoA + diphosphate (pyrophosphate)

This is a nucleotidyltransferase reaction (transfer of an AMP/adenylyl moiety), not a simple kinase step, and it is fully reversible.

### F002 — PPAT is a rate-limiting, allosteric enzyme feedback-inhibited by CoA; the *Pseudomonas* enzyme is structurally characterized

PPAT is not merely a catalytic step; it is a **regulatory hub**. Miller et al. demonstrated that **"CoA inhibits PPAT and is competitive with ATP, PhP, and dPCoA"** ([PMID: 17873050](https://pubmed.ncbi.nlm.nih.gov/17873050/)), i.e., the end-product of the pathway feeds back onto this enzyme by competing with all three of its substrates/products at the active site. This makes PPAT a rate-limiting control point of CoA homeostasis.

Directly relevant to *P. putida*, the closely related enzyme from *Pseudomonas aeruginosa* has been crystallized in multiple states. Chatterjee et al. captured X-ray structures with AMP-PNP, CoA, and acetyl-CoA and showed that **"the enzyme is allosteric in nature and regulated by Coenzyme A (CoA) through feedback inhibition,"** with the transition from a catalytic to an allosteric state proceeding via ternary-complex formation ([PMID: 27041211](https://pubmed.ncbi.nlm.nih.gov/27041211/)). Structural work on the *Helicobacter pylori* ortholog established the general architecture: **"HpPPAT is hexameric in solution and as a crystal. Each protomer has a well-packed dinucleotide-binding fold in which CoA binds"** ([PMID: 21527250](https://pubmed.ncbi.nlm.nih.gov/21527250/)), confirming the hexameric assembly and the Rossmann-like dinucleotide-binding fold that is diagnostic of this family.

### F003 — PPAT/CoaD operates in the cytoplasm within the universal five-step CoA biosynthetic pathway

CoA is a universal, essential cofactor. As reviewed by Leonardi et al., **"CoA is assembled in five steps from pantothenic acid and pathway intermediates are common to both prokaryotes and eukaryotes"** ([PMID: 15893380](https://pubmed.ncbi.nlm.nih.gov/15893380/)). PPAT (CoaD) performs step 4 of this pathway, converting 4′-phosphopantetheine + ATP to dephospho-CoA. Because purified PPAT lacks dephospho-CoA kinase activity, **"the two final steps of CoA biosynthesis in E. coli must be catalyzed by separate enzymes"** ([PMID: 10480925](https://pubmed.ncbi.nlm.nih.gov/10480925/)) — the fifth and final step is carried out by dephospho-CoA kinase (CoaE). All of these reactions occur in the **cytoplasm**, consistent with the soluble nature of the enzyme. The pathway as a whole is a validated antibacterial drug target ([PMID: 17873050](https://pubmed.ncbi.nlm.nih.gov/17873050/)).

### F004 — Sequence analysis confirms Q88CQ7 is a bona fide single-domain PPAT with an intact catalytic signature (direct evidence for the *P. putida* protein)

Rather than relying solely on ortholog inference, the *P. putida* protein was analyzed directly. Q88CQ7 is a **compact 161-residue protein**, matching the length of standalone bacterial CoaD enzymes (*E. coli* is 159 aa). A Needleman–Wunsch global alignment of Q88CQ7 against the biochemically and kinetically characterized *E. coli* CoaD (P0A6I6) gives **64.3% identity and 80.5% similarity** (99 of 154 aligned positions identical). Both proteins carry the diagnostic N-terminal PPAT/nucleotidyltransferase signature **"(G)TFDPIT(K/N)GH"** (*P. putida* residues 8–17), which includes the invariant catalytic histidine (His17 in *P. putida*, equivalent to His18 in *E. coli*) that contacts the ATP α-phosphate. Conserved downstream motifs — the basic "RGLRAV" loop around residue 87 and the "ISS" catalytic region near residues 118–120 — are also retained. This level of identity across a compact, single-domain enzyme leaves no ambiguity: Q88CQ7 is a genuine, catalytically intact PPAT.

### F005 — All experimentally validated PPAT catalytic residues are conserved in *P. putida* CoaD; the mechanism is an SN2-like in-line adenylyl transfer

Recent structure/mutagenesis work on *H. pylori* PPAT pinned down the catalytic machinery to the residue level. Ko et al. identified **"critical active site residues Thr10, His18, Arg88, and Arg91, conserved in Escherichia coli PPAT (EcPPAT)"** and showed by alanine-scanning that **"mutations of these residues, except for Thr10 and Lys42, resulted in a complete loss of enzymatic activity"** — i.e., His18, Arg88, and Arg91 are catalytically essential ([PMID: 40843967](https://pubmed.ncbi.nlm.nih.gov/40843967/)). Mechanistically, **"these residues are expected to orient the nucleophile for an in-line displacement mechanism"** — an SN2-like transfer in which the 4′-phosphopantetheine phosphate attacks the α-phosphate of ATP, displacing pyrophosphate.

Alignment mapping shows all four residues are **exactly conserved in *P. putida* Q88CQ7**: *E. coli* Thr10→Thr9, His18→His17, Arg88→Arg87, and Arg91→Arg90 (*P. putida* numbering; motifs "FLRGLRAV" at residues 85–92 and "PGTFDPITKGHG" at residues 7–18). Furthermore, the binding modes of ligands are conserved across the whole family: **"the binding modes of ATP, ADP, Ppant, and dPCoA are highly similar in all known structures"** ([PMID: 21912874](https://pubmed.ncbi.nlm.nih.gov/21912874/)), and structures of the *Mycobacterium tuberculosis* enzyme in apo, ATP-bound, dPCoA-bound, and CoA-bound states document the conformational cycle of the catalyzed reaction ([PMID: 23151631](https://pubmed.ncbi.nlm.nih.gov/23151631/)). This transfer of well-established structural knowledge to the *P. putida* enzyme is fully justified by the near-complete conservation of active-site residues.

### F006 — UniProt curation of Q88CQ7 independently corroborates the reaction, hexamer, cytoplasmic localization, and pathway position

The curated UniProt entry for Q88CQ7 independently agrees with every conclusion drawn from literature and sequence analysis:

| UniProt field | Annotation |
|---|---|
| **Function** | "Reversibly transfers an adenylyl group from ATP to 4′-phosphopantetheine, yielding dephospho-CoA (dPCoA) and pyrophosphate" |
| **Catalytic activity** | "(R)-4′-phosphopantetheine + ATP + H⁺ = 3′-dephospho-CoA + diphosphate" |
| **Pathway** | "coenzyme A biosynthesis; CoA from (R)-pantothenate: step 4/5" |
| **Subunit** | "Homohexamer" |
| **Subcellular location** | "Cytoplasm" |
| **Family** | Bacterial CoaD family; orthology cluster COG0669 |

Critically, the **annotated binding-site residues (positions 9–10, 17, 41, 73, 87, 88–90, 98, 123–129) coincide exactly with the catalytic residues independently mapped by alignment** (Thr9, His17, Arg87, and the 88–90 basic loop). An AlphaFold model (AlphaFoldDB Q88CQ7) and STRING/KEGG (ppu:PP_5123) cross-references are available. The convergence of curated annotation with de novo sequence analysis provides strong, mutually reinforcing support for the functional assignment.

---

## Mechanistic Model and Interpretation

### Position in the CoA biosynthetic pathway

Coenzyme A is synthesized from (R)-pantothenate (vitamin B5) in five universally conserved enzymatic steps. PPAT/CoaD catalyzes **step 4**:

```
 (R)-Pantothenate
     │  1. Pantothenate kinase (CoaA / PanK)              [+ATP]
     ▼
 4′-Phosphopantothenate
     │  2. Phosphopantothenoylcysteine synthetase (CoaB)  [+Cys, +CTP]
     ▼
 4′-Phosphopantothenoyl-cysteine
     │  3. Phosphopantothenoylcysteine decarboxylase (CoaC)
     ▼
 4′-Phosphopantetheine (PhP / PNS)
     │  ►►► 4. PHOSPHOPANTETHEINE ADENYLYLTRANSFERASE (PPAT / CoaD) ◄◄◄
     │        4′-phosphopantetheine + ATP → 3′-dephospho-CoA + PPi
     │        [ EC 2.7.7.3 — the coaD/PP_5123 gene product ]
     ▼
 3′-Dephospho-CoA (dPCoA)
     │  5. Dephospho-CoA kinase (CoaE)                    [+ATP]
     ▼
 Coenzyme A (CoA)
```

The reaction is an **adenylyl (AMP) transfer**, not a phosphoryl transfer: the α-phosphate of ATP is attacked by the terminal phosphate of 4′-phosphopantetheine, forming a new phosphoanhydride bond and releasing pyrophosphate. This is why the enzyme is a nucleotidyltransferase (EC 2.7.7.-) rather than a kinase, and why the product dephospho-CoA still requires a final phosphorylation by CoaE to become mature CoA.

### Catalytic mechanism at the residue level

Each protomer presents a dinucleotide-binding (Rossmann-like) fold that binds ATP and 4′-phosphopantetheine adjacently. The conserved active-site residues perform the following roles (numbering for *P. putida* Q88CQ7):

| Residue (P. putida) | E. coli / H. pylori equiv. | Role | Effect of Ala mutation |
|---|---|---|---|
| **His17** | His18 | Contacts/stabilizes ATP α-phosphate; positions nucleophile | Complete loss of activity |
| **Arg87** | Arg88 | Stabilizes transition state / phosphates | Complete loss of activity |
| **Arg90** | Arg91 | Stabilizes transition state / phosphates | Complete loss of activity |
| **Thr9** | Thr10 | Substrate positioning | Substantial activity retained |

The reaction proceeds through an **in-line (SN2-like) displacement**: the invariant His and two Arg residues orient the incoming 4′-phosphopantetheine phosphate for backside attack on the ATP α-phosphate, with pyrophosphate as the leaving group. The near-symmetric kinetics (random bi-bi ternary complex) reflect a single active site that must simultaneously accommodate both substrates.

### Quaternary structure and allosteric regulation

```
        Hexamer (dimer of trimers) — cytoplasmic
        ┌──────────────────────────────────┐
        │   6 identical ~161-aa protomers   │
        │   central water-filled channel    │
        │   along the 3-fold axis           │
        └──────────────────────────────────┘
                 │
     Each active site:  ATP + 4'-PhP  ⇌  dPCoA + PPi
                 │
     Feedback:  CoA / acetyl-CoA bind competitively
                → transition to allosteric (low-activity) state
```

The enzyme functions as a homohexamer (a dimer of trimers) with a central water-filled channel running along the three-fold axis. Feedback inhibition by CoA — competitive with ATP, PhP, and dPCoA — allows the cell to throttle CoA production when supply is adequate. Structural snapshots in *P. aeruginosa* and *M. tuberculosis* show that binding of CoA/acetyl-CoA drives a conformational transition from a catalytically competent to an allosterically inhibited state, mediated by ternary complex formation.

### Physiological significance in *P. putida*

*P. putida* KT2440 is a metabolically versatile soil bacterium whose lifestyle depends heavily on acyl-CoA chemistry: β-oxidation of fatty acids and alcohols, catabolism of aromatic and terpenoid compounds, and the biosynthesis of medium-chain-length polyhydroxyalkanoates (PHAs) all consume or generate CoA thioesters ([PMID: 32826213](https://pubmed.ncbi.nlm.nih.gov/32826213/); [PMID: 16085828](https://pubmed.ncbi.nlm.nih.gov/16085828/); [PMID: 16820476](https://pubmed.ncbi.nlm.nih.gov/16820476/)). As the rate-limiting supplier of the CoA backbone, PPAT/CoaD sits upstream of this entire acyl-CoA economy. While the CoaD enzyme itself has broadly conserved housekeeping function, its output is what fuels the specialized catabolic and biosynthetic capabilities that make *P. putida* a favored metabolic-engineering chassis. Because CoA biosynthesis is essential, coaD is expected to be an essential gene.

---

## Evidence Base

| PMID | Study (organism) | Contribution to this report |
|---|---|---|
| [10480925](https://pubmed.ncbi.nlm.nih.gov/10480925/) | Geerlof et al., *E. coli* PPAT purification | Defines the reaction, names the gene coaD, establishes homohexamer, shows PPAT lacks kinase activity (steps 4 & 5 are separate) |
| [17873050](https://pubmed.ncbi.nlm.nih.gov/17873050/) | Miller et al., *E. coli* kinetics | Random bi-bi mechanism; CoA feedback inhibition competitive with all substrates; rate-limiting/drug-target status |
| [27041211](https://pubmed.ncbi.nlm.nih.gov/27041211/) | Chatterjee et al., *P. aeruginosa* structures | Directly relevant *Pseudomonas* ortholog; catalytic→allosteric transition via ternary complex; CoA feedback |
| [21527250](https://pubmed.ncbi.nlm.nih.gov/21527250/) | Cheng et al., *H. pylori* structure | Hexameric assembly; dinucleotide-binding (Rossmann-like) fold; CoA binding site |
| [40843967](https://pubmed.ncbi.nlm.nih.gov/40843967/) | Ko et al., *H. pylori* structure/mutagenesis | Identifies and validates catalytic residues (His18, Arg88, Arg91 essential); in-line displacement mechanism |
| [21912874](https://pubmed.ncbi.nlm.nih.gov/21912874/) | Yoon et al., *E. faecalis* structures | Conserved binding modes of ATP, ADP, Ppant, dPCoA across all known PPAT structures |
| [23151631](https://pubmed.ncbi.nlm.nih.gov/23151631/) | Timofeev et al., *M. tuberculosis* structures | Apo/ATP/dPCoA/CoA structures document conformational cycle and hexameric central channel |
| [15893380](https://pubmed.ncbi.nlm.nih.gov/15893380/) | Leonardi et al., review | Establishes the universal five-step cytoplasmic CoA pathway |
| [25109998](https://pubmed.ncbi.nlm.nih.gov/25109998/) | Leonardi & Jackowski, review | Broader CoA pathway regulation (PanK-centric) context |
| [29107839](https://pubmed.ncbi.nlm.nih.gov/29107839/) | Enzymatic depCoA synthesis | Demonstrates PPAT (CoaD) used with PanK to make dephospho-CoA from phosphopantetheine + ATP — confirms substrate/product |
| [38456905](https://pubmed.ncbi.nlm.nih.gov/38456905/), [40689715](https://pubmed.ncbi.nlm.nih.gov/40689715/), [41069273](https://pubmed.ncbi.nlm.nih.gov/41069273/) | *K. pneumoniae* / *Enterobacter* structures | Additional structural confirmations of the reaction and PNS/ATP binding sites |

The evidence base is notable for its **convergence across three independent modalities** — direct biochemistry/enzymology, X-ray crystallography of multiple orthologs (including a *Pseudomonas* species), and de novo sequence/curation analysis of the exact target protein Q88CQ7. No paper in the reviewed literature challenges the functional assignment.

### On gene-symbol ambiguity

The gene symbol "coaD" is unambiguous and matches the protein description. The only historical caveat is that the *E. coli* ortholog was originally mis-named **kdtB** (falsely implicated in Kdo/lipopolysaccharide biology) before Geerlof et al. formally corrected it to **coaD** upon biochemical characterization ([PMID: 10480925](https://pubmed.ncbi.nlm.nih.gov/10480925/)). This does not affect the *P. putida* assignment, which is corroborated by direct sequence and curation evidence.

---

## Limitations and Knowledge Gaps

1. **No direct experimental characterization of the *P. putida* KT2440 protein.** All enzymological and structural data derive from orthologs (*E. coli*, *P. aeruginosa*, *H. pylori*, *M. tuberculosis*, *E. faecalis*, *K. pneumoniae*, *Enterobacter*). The assignment for Q88CQ7 rests on inference from high sequence identity (64% to *E. coli*) and complete active-site conservation. While this inference is extremely robust for such a conserved single-domain housekeeping enzyme, kinetic constants (Km, kcat), the precise CoA-inhibition constant, and a crystal structure specific to the *P. putida* enzyme have not been reported.

2. **Essentiality not directly demonstrated in *P. putida*.** CoA biosynthesis is essential in bacteria generally, and coaD would be expected to be essential in KT2440, but a specific gene-deletion/conditional-knockout study for PP_5123 has not been documented here.

3. **Regulation in vivo is uncharacterized for this organism.** Transcriptional/translational regulation of PP_5123 and its integration with the heavy acyl-CoA flux of *P. putida* (PHA production, aromatic catabolism) are not established.

4. **Structural data is a model, not experimental.** Only an AlphaFold model (AlphaFoldDB Q88CQ7) exists for the *P. putida* protein; no experimental structure has been solved.

---

## Proposed Follow-up Experiments and Actions

1. **Recombinant expression and enzymology.** Clone PP_5123, purify the His-tagged protein, and measure steady-state kinetics (Km for ATP and 4′-phosphopantetheine, kcat) and the Ki for CoA/acetyl-CoA feedback inhibition, to confirm the inferred rate-limiting/allosteric behavior in the *P. putida* enzyme directly. (Note: expression tags can occupy the PNS-binding site — see [PMID: 40689715](https://pubmed.ncbi.nlm.nih.gov/40689715/) — so tag placement/removal should be considered.)

2. **Confirm quaternary structure.** Use size-exclusion chromatography–MALS or native MS to verify the homohexameric assembly predicted by the family.

3. **Solve an experimental structure.** Crystallize the *P. putida* enzyme with ATP/AMP-PNP, 4′-phosphopantetheine, dephospho-CoA, and CoA to validate the AlphaFold model and directly visualize the mapped catalytic residues (Thr9, His17, Arg87, Arg90).

4. **Genetic essentiality test.** Attempt a chromosomal deletion or construct a conditional (e.g., inducible) knockdown of PP_5123 to formally establish essentiality in KT2440, ideally with rescue by an ectopic copy.

5. **Active-site mutagenesis in situ.** Introduce His17Ala, Arg87Ala, and Arg90Ala substitutions and confirm loss of function, directly transferring the *H. pylori* mutagenesis result ([PMID: 40843967](https://pubmed.ncbi.nlm.nih.gov/40843967/)) to the *P. putida* enzyme.

6. **Metabolic-engineering relevance.** Given *P. putida*'s reliance on acyl-CoA chemistry, quantify how CoaD activity/expression limits CoA pools during PHA accumulation and aromatic/fatty-acid catabolism — potentially identifying PPAT as an engineering target to relieve CoA bottlenecks.

---

## Conclusion

**coaD (PP_5123, Q88CQ7) encodes phosphopantetheine adenylyltransferase (PPAT, EC 2.7.7.3)**, a soluble cytoplasmic homohexamer that catalyzes step 4 of the five-step coenzyme A biosynthetic pathway — the reversible, Mg-ATP–dependent adenylyl transfer to (R)-4′-phosphopantetheine, yielding 3′-dephospho-CoA and pyrophosphate via an in-line (SN2-like) mechanism using conserved residues Thr9, His17, Arg87, and Arg90. It is the rate-limiting, CoA/acetyl-CoA–feedback-inhibited control point of CoA synthesis and passes its product to dephospho-CoA kinase (CoaE) for the final step. This conclusion is supported convergently by primary biochemical/structural literature on close orthologs (including *P. aeruginosa*), direct sequence analysis of Q88CQ7 (64% identity to the characterized *E. coli* enzyme with a fully conserved catalytic signature), and curated UniProt/KEGG annotation.


## Artifacts

- [OpenScientist final report](coaD-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](coaD-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:10480925
2. PMID:17873050
3. PMID:27041211
4. PMID:21527250
5. PMID:15893380
6. PMID:40843967
7. PMID:21912874
8. PMID:23151631
9. PMID:32826213
10. PMID:16085828
11. PMID:16820476
12. PMID:40689715