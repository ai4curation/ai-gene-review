---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-17T12:56:46.456529'
end_time: '2026-07-17T13:36:07.255584'
duration_seconds: 2360.8
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: ilvE
  gene_symbol: ilvE
  uniprot_accession: Q88H54
  protein_description: 'RecName: Full=Branched-chain-amino-acid aminotransferase {ECO:0000256|ARBA:ARBA00018179,
    ECO:0000256|RuleBase:RU004517}; EC=2.6.1.42 {ECO:0000256|ARBA:ARBA00013053, ECO:0000256|RuleBase:RU004517};'
  gene_info: Name=ilvE {ECO:0000313|EMBL:AAN69112.1}; OrderedLocusNames=PP_3511 {ECO:0000313|EMBL:AAN69112.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the class-IV pyridoxal-phosphate-dependent
  protein_domains: Aminotrans_IV. (IPR001544); Aminotrans_IV_CS. (IPR018300); Aminotransferase-like.
    (IPR036038); B_amino_transII. (IPR005786); BCAT-like_C. (IPR043132)
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
  path: ilvE-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: ilvE-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88H54
- **Protein Description:** RecName: Full=Branched-chain-amino-acid aminotransferase {ECO:0000256|ARBA:ARBA00018179, ECO:0000256|RuleBase:RU004517}; EC=2.6.1.42 {ECO:0000256|ARBA:ARBA00013053, ECO:0000256|RuleBase:RU004517};
- **Gene Information:** Name=ilvE {ECO:0000313|EMBL:AAN69112.1}; OrderedLocusNames=PP_3511 {ECO:0000313|EMBL:AAN69112.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the class-IV pyridoxal-phosphate-dependent
- **Key Domains:** Aminotrans_IV. (IPR001544); Aminotrans_IV_CS. (IPR018300); Aminotransferase-like. (IPR036038); B_amino_transII. (IPR005786); BCAT-like_C. (IPR043132)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ilvE" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ilvE' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ilvE** (gene ID: ilvE, UniProt: Q88H54) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *ilvE* (Q88H54, PP_3511) — Branched-Chain-Amino-Acid Aminotransferase of *Pseudomonas putida* KT2440

**Gene:** *ilvE* &nbsp;|&nbsp; **Ordered locus:** PP_3511 &nbsp;|&nbsp; **UniProt:** Q88H54 (Q88H54_PSEPK) &nbsp;|&nbsp; **EC:** 2.6.1.42 &nbsp;|&nbsp; **Length:** 339 aa
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440)

---

## Summary

The gene **ilvE** (ordered locus **PP_3511**; UniProt **Q88H54**) of *Pseudomonas putida* KT2440 encodes a **branched-chain-amino-acid aminotransferase (BCAT)**, historically known as **"transaminase B,"** classified as **EC 2.6.1.42**. This is a **soluble, cytoplasmic, pyridoxal-5′-phosphate (PLP)-dependent enzyme** of the **class-IV / fold-type IV aminotransferase family**. The family assignment is fully consistent with the gene symbol, the enzyme's InterPro domain architecture (Aminotrans_IV IPR001544, Aminotrans_IV_CS IPR018300, B_amino_transII IPR005786, BCAT-like_C IPR043132), and a ~48% amino-acid identity to the biochemically characterized *Escherichia coli* IlvE ortholog. Target identity was verified against the UniProt reference; the gene symbol, organism, protein family, and domain content all converge on a single, unambiguous functional annotation, and no evidence of gene-symbol ambiguity was encountered.

Functionally, IlvE catalyzes the **reversible transamination** that interconverts **L-glutamate/2-oxoglutarate (α-ketoglutarate)** with the **three branched-chain 2-oxo acids and their corresponding amino acids — valine, isoleucine, and leucine**. In the **biosynthetic direction**, IlvE performs the **final step of branched-chain amino acid (BCAA) biosynthesis**, aminating the 2-oxo acids produced by the upstream acetohydroxyacid pathway (ilvBN/ilvC/ilvD) and the leucine pathway (leuABCD). In the **catabolic direction**, the same enzyme performs the **first committed step of BCAA degradation**, removing the α-amino group to regenerate the branched-chain 2-oxo acids that are the direct substrates of the inducible **branched-chain 2-oxo (keto) acid dehydrogenase (Bkd) complex** encoded by the *bkd* operon. IlvE thus sits at the **central transamination node** coupling BCAA anabolism and catabolism to cellular glutamate/nitrogen metabolism.

Mechanistically, the enzyme operates by a **ping-pong bi-bi kinetic mechanism** through a **PLP↔PMP (pyridoxamine-5′-phosphate) cofactor cycle**, with catalysis occurring on the distinctive **re-face** of the cofactor — a hallmark of fold-type IV enzymes. The **catalytic Schiff-base lysine** that forms the internal aldimine with PLP is strictly conserved in Q88H54 (**Lys183**, within the invariant A-A-K-x-G-G-N-Y motif). Substrate and stereospecificity for the L-branched-chain substrates are set by a **hydrophobic active-site pocket** and **glutamate-selective polar contacts**, features established by crystallographic studies of homologous BCATs and structurally conserved in bacterial IlvE. The *E. coli*-type BCAT (closest characterized ortholog) is a **homohexamer arranged as a double trimer**, distinguishing it from the homodimeric BCATs of most other organisms.

---

## Gene/Protein Identity — Verification

The UniProt annotation, gene symbol, organism, and domain architecture are **mutually consistent and unambiguous**:

- **Description:** Branched-chain-amino-acid aminotransferase, EC 2.6.1.42 — matches the gene symbol *ilvE* ("transaminase B"), the historical name of this enzyme in the isoleucine–valine (*ilv*) system ([PMID: 14273641](https://pubmed.ncbi.nlm.nih.gov/14273641/)).
- **Domains:** Aminotrans_IV (IPR001544), Aminotrans_IV_CS (IPR018300), B_amino_transII (IPR005786), BCAT-like_C (IPR043132) — the canonical signature of fold-type IV BCATs ([PMID: 11642362](https://pubmed.ncbi.nlm.nih.gov/11642362/)).
- **Orthology (bioinformatic evidence):** A Needleman–Wunsch global alignment shows Q88H54 (339 aa) shares **47.7% identity** (132/277 aligned positions) with the biochemically characterized *E. coli* IlvE/transaminase B (P0AB80, 309 aa) — the enzyme whose EC 2.6.1.42 activity was directly measured ([PMID: 378964](https://pubmed.ncbi.nlm.nih.gov/378964/)). This exceeds the threshold for confident orthology and functional-annotation transfer for a single-domain enzyme.

There is **no evidence of gene-symbol ambiguity**: the *ilvE* symbol, EC number, family, and domains all converge on the same enzyme, and the closest experimentally characterized homolog (*E. coli* transaminase B) has exactly this activity.

---

## Key Findings

### F001 — IlvE is a branched-chain-amino-acid aminotransferase (EC 2.6.1.42) catalyzing the final transamination step of BCAA biosynthesis

UniProt Q88H54 annotates PP_3511/*ilvE* as a **Branched-chain-amino-acid aminotransferase, EC 2.6.1.42**, a class-IV PLP-dependent enzyme (Aminotrans_IV, IPR001544). BCATs catalyze the reversible transamination between L-glutamate and the branched-chain 2-oxo acids: 2-oxoisovalerate ↔ valine, (S)-3-methyl-2-oxopentanoate ↔ isoleucine, and 4-methyl-2-oxopentanoate ↔ leucine. In the biosynthetic direction IlvE catalyzes the **last (transamination) step**; because the reaction is freely reversible, the same enzyme initiates BCAA catabolism.

The functional assignment is anchored by direct study of orthologs. In *Mycobacterium tuberculosis*, the IlvE enzyme "**is responsible for the final step of the synthesis of the branched-chain amino acids isoleucine, leucine, and valine**" ([PMID: 27780341](https://pubmed.ncbi.nlm.nih.gov/27780341/)). Classical genetics of the *ilv* operon named *ilvE* "**transaminase B**," identifying it among the "structural genes ilvE (transaminase B), ilvD (dehydrase), and ilvA (threonine deaminase)" ([PMID: 14273641](https://pubmed.ncbi.nlm.nih.gov/14273641/)). The substrate scope of the enzyme class is defined by the observation that "**Branched chain aminotransferases (BCATs) catalyze transamination of the branched chain amino acids (BCAAs) leucine, isoleucine, and valine**" ([PMID: 11642362](https://pubmed.ncbi.nlm.nih.gov/11642362/)).

### F002 — IlvE is a PLP-dependent fold-type IV aminotransferase using a ping-pong bi-bi mechanism with re-face catalysis

The Q88H54 domain architecture (Aminotrans_IV, Aminotrans_IV_CS, B_amino_transII, BCAT-like_C) places the enzyme firmly in the **class-IV / fold-type IV PLP enzyme family**. As the authoritative BCAT review states, "**Structurally, the BCATs belong to the fold type IV class of pyridoxal phosphate (PLP) enzymes**" ([PMID: 11642362](https://pubmed.ncbi.nlm.nih.gov/11642362/)). The family is mechanistically distinctive: "**Catalysis is on the re face of the PLP cofactor, whereas in other classes, catalysis occurs from the si face of PLP**" ([PMID: 11642362](https://pubmed.ncbi.nlm.nih.gov/11642362/)). This distinguishes IlvE from the aspartate-aminotransferase (fold-type I) superfamily. The fold-type IV family also includes D-amino-acid aminotransferase and 4-amino-4-deoxychorismate lyase, which share the same active-site architecture around the cofactor ([PMID: 10876155](https://pubmed.ncbi.nlm.nih.gov/10876155/)).

Kinetically, the *M. tuberculosis* IlvE study confirmed that "**As seen in other aminotransferases, MtIlvE displays a ping-pong kinetic mechanism**" ([PMID: 27780341](https://pubmed.ncbi.nlm.nih.gov/27780341/)). This is consistent with the two half-reactions of transamination proceeding through a PLP↔PMP cofactor cycle mediated by an active-site lysine Schiff base: the amino donor binds first, transfers its amino group to PLP (forming PMP) and departs as a 2-oxo acid, after which the acceptor 2-oxo acid binds and is aminated.

### F003 — IlvE functions in the cytoplasm as the single bacterial BCAT, linking BCAA metabolism to glutamate/nitrogen metabolism

Bacteria characteristically use one BCAT for both anabolic and catabolic transamination: "**The BCATs are widely distributed in the bacterial kingdom, where they are involved in the synthesis/degradation of the BCAAs. Bacteria contain a single BCAT**" ([PMID: 11642362](https://pubmed.ncbi.nlm.nih.gov/11642362/)). Bacterial BCATs are soluble cytoplasmic enzymes, in contrast to the eukaryotic mitochondrial BCATm isozyme. Q88H54 carries **no predicted signal peptide and no transmembrane segment**, consistent with a cytosolic protein that is not membrane-associated.

Positionally, in *P. putida* KT2440 the enzyme sits at the branch point of **BCAA anabolism** (downstream of the ilvBN/ilvC/ilvD acetohydroxyacid pathway and the leuABCD leucine pathway) and **BCAA catabolism** (upstream of the branched-chain 2-oxo acid dehydrogenase, Bkd). In both directions it uses **glutamate/2-oxoglutarate as the nitrogen carrier**, coupling BCAA carbon skeletons to the cell's central nitrogen pool.

### F004 — Substrate specificity: all three branched-chain 2-oxo acids/amino acids with 2-oxoglutarate, plus minor activity toward aromatic substrates

The definitive substrate-specificity data come from direct enzymology of the *E. coli ilvE* product (Transaminase B, EC 2.6.1.42), the closest well-characterized ortholog. Purified enzyme "**catalyzed transamination between alpha-ketoglutarate and l-isoleucine, l-leucine, l-valine, and, to a lesser extent, l-phenylalanine and l-tyrosine, the latter reacting very sluggishly**," and was "free of aspartate transaminase and of transaminase C" with an "absence of a separate valine-alpha-ketoglutarate activity" — i.e., a **single enzyme handles all three BCAAs** ([PMID: 378964](https://pubmed.ncbi.nlm.nih.gov/378964/)). The apparent Km values reveal a preference for the 2-oxo-acid substrates: "**The apparent K(m) values for the branched-chain alpha-ketoacids were smaller than those for the corresponding amino acids**" ([PMID: 378964](https://pubmed.ncbi.nlm.nih.gov/378964/)); the lowest Km was for the isoleucine 2-oxo acid, the highest for L-valine.

The physiological dominance of IlvE — and its partial redundancy for some substrates — is quantified by a *Lactococcus lactis ilvE* knockout, in which "**the mutant retained <2, 4.5, 43, 40, and 76% of its aminotransferase activity with Ile, Val, Leu, Met, and Phe, respectively**" ([PMID: 10831406](https://pubmed.ncbi.nlm.nih.gov/10831406/)). This establishes IlvE as the **principal (near-sole) aminotransferase for isoleucine and valine**, while leucine, methionine, and phenylalanine transamination is partly served by other enzymes.

| Substrate | Relative activity retained in *ilvE* knockout (*L. lactis*) | Interpretation |
|---|---|---|
| Isoleucine | < 2% | IlvE essentially the sole transaminase |
| Valine | 4.5% | IlvE strongly dominant |
| Leucine | 43% | IlvE major, partial redundancy |
| Methionine | 40% | Partial contribution |
| Phenylalanine | 76% | Minor contribution; largely redundant |

### F005 — IlvE is cytosolic; the *E. coli*-type BCAT is a homohexamer (double trimer)

Analysis of the *E. coli* Transaminase B established that "**the oligomeric structure of the enzyme, as determined by analytical ultracentrifugation and sodium dodecyl sulfate-polyacrylamide gel electrophoresis, was confirmed to be that of a hexamer**," with a molecular weight of ~182,000 and apparently identical subunits "consistent with a double-trimer arrangement" ([PMID: 378964](https://pubmed.ncbi.nlm.nih.gov/378964/)). This quaternary structure is unusual within the family: "**Except for the Escherichia coli and Salmonella proteins, which are homohexamers arranged as a double trimer, the BCATs are homodimers**" ([PMID: 11642362](https://pubmed.ncbi.nlm.nih.gov/11642362/)). Because *P. putida* IlvE is a close *E. coli*-type ortholog, a hexameric assembly is the most likely quaternary state, though this has not been directly demonstrated for Q88H54.

For subcellular localization, the *Lactococcus* IlvE study reported that "**Hydrophobicity plot analysis of the deduced amino acid sequence and the lack of a signal peptide sequence suggest IlvE is a cytosolic protein**" ([PMID: 10831406](https://pubmed.ncbi.nlm.nih.gov/10831406/)). Q88H54 likewise has no predicted signal peptide or transmembrane region, supporting cytoplasmic localization.

### F006 — In *P. putida*, IlvE connects to BCAA catabolism upstream of the branched-chain 2-oxo acid dehydrogenase (Bkd) complex

*P. putida* degrades branched-chain amino acids via the **inducible branched-chain keto acid dehydrogenase (Bkd) multienzyme complex**, encoded by the *bkd* operon. Transcription is controlled by the activator **BkdR**, and "**the L-branched-chain amino acids and D-leucine are the inducers of the bkd operon**" ([PMID: 10217783](https://pubmed.ncbi.nlm.nih.gov/10217783/)). The operon is additionally subject to catabolite repression: "**The bkd operons of P. putida and P. aeruginosa encode the inducible multienzyme complex branched-chain keto acid dehydrogenase, which is regulated in both species by catabolite repression**," mediated by Crc ([PMID: 10648542](https://pubmed.ncbi.nlm.nih.gov/10648542/)).

In the **catabolic direction**, IlvE removes the α-amino group from valine/isoleucine/leucine to yield the corresponding branched-chain 2-oxo acids, which are the **direct substrates oxidatively decarboxylated by the Bkd complex**. IlvE thereby supplies the entry substrates for the *bkd* pathway while regenerating glutamate from 2-oxoglutarate. In the **biosynthetic direction**, IlvE acts downstream of the ilvBN/ilvC/ilvD (valine/isoleucine) and leuABCD (leucine) pathways to aminate the same 2-oxo acids. The regulatory apparatus of the catabolic branch is well characterized in *P. putida*: BkdR is a tetrameric Lrp homolog that binds the *bkdR–bkdA1* intergenic region ([PMID: 7836297](https://pubmed.ncbi.nlm.nih.gov/7836297/), [PMID: 8670279](https://pubmed.ncbi.nlm.nih.gov/8670279/), [PMID: 9068646](https://pubmed.ncbi.nlm.nih.gov/9068646/)), with catabolite repression in rich medium acting posttranscriptionally on *bkdR* expression ([PMID: 10648543](https://pubmed.ncbi.nlm.nih.gov/10648543/)).

### F007 — Q88H54 is a 339-aa ortholog sharing ~48% identity with the biochemically characterized *E. coli* transaminase B

A Needleman–Wunsch global alignment of the UniProt sequences shows that **Q88H54 (339 aa) shares 47.7% amino-acid identity (132/277 aligned positions)** with *E. coli* IlvE/transaminase B (P0AB80, 309 aa), the enzyme whose EC 2.6.1.42 activity and substrate specificity were directly measured ([PMID: 378964](https://pubmed.ncbi.nlm.nih.gov/378964/)). For a single-domain fold-type IV aminotransferase, ~48% identity is comfortably within the range supporting **confident orthology and functional-annotation transfer**. This bioinformatic result is the bridge that licenses transferring the direct *E. coli* enzymology to the *P. putida* protein.

### F008 — Q88H54 conserves the fold-type IV catalytic lysine (Lys183) and the A-A-K-x-G-G-N-Y PLP-binding motif

Alignment of Q88H54 to *E. coli* IlvE (P0AB80) shows that the **catalytic PLP-Schiff-base lysine is strictly conserved**. The *E. coli* active-site lysine (in the motif TAAK-AGGNYLSSL) aligns to **Q88H54 Lys183** within the conserved motif …GAAK-VGGNYAASL…. The invariant **A-A-K…G-G-N-Y** region that harbors the Schiff-base lysine of fold-type IV aminotransferases is therefore retained in the *P. putida* enzyme. This is the residue that, in structurally characterized BCATs, forms the internal aldimine with pyridoxal-5′-phosphate (e.g., Lys202 in human mitochondrial BCAT; Lys159 in *E. coli* IlvE; the equivalent catalytic Lys159 is also present in the homologous 4-amino-4-deoxychorismate lyase, [PMID: 10876155](https://pubmed.ncbi.nlm.nih.gov/10876155/)). Conservation of this residue is strong structural evidence that Q88H54 is a catalytically competent transaminase rather than a pseudo-enzyme.

### F009 — Substrate/stereospecificity is set by a hydrophobic active-site pocket and glutamate-selective contacts (structural evidence)

Crystal structures of human mitochondrial BCAT reaction intermediates (isoleucine ketimine and pyridoxamine-phosphate forms, 1.9 Å) provide the structural logic for BCAT specificity and catalysis. They show that "**The active site lysine, Lys202, undergoes large conformational changes, and the pyridine ring of the cofactor tilts by about 18 degrees during catalysis**," and that "**A major determinant of the enzyme's substrate and stereospecificity for L-branched chain amino acids is a group of hydrophobic residues that form three hydrophobic surfaces and lock the side chain in place**" ([PMID: 12269802](https://pubmed.ncbi.nlm.nih.gov/12269802/)). The same structures explain amino-donor selectivity, showing that "**glutamate but not aspartate can form hydrogen bond interactions**" ([PMID: 12269802](https://pubmed.ncbi.nlm.nih.gov/12269802/)).

These two active-site features — a **hydrophobic pocket** that accommodates branched aliphatic side chains and locks them in the correct L-configuration, and **glutamate-selective polar contacts** that enforce use of glutamate/2-oxoglutarate as the amino donor/acceptor — are conserved architectural elements across BCATs, including bacterial IlvE. They provide a structure-based rationalization of the substrate preferences measured biochemically in F004.

### F010 — Consolidated annotation

Convergent evidence across all nine preceding findings establishes that **ilvE (Q88H54) is the cytoplasmic branched-chain aminotransferase governing the transamination node of *P. putida* BCAA metabolism**. Specifically: (1) EC 2.6.1.42 / fold-type IV family assignment is consistent with the gene symbol, domains, and ~48% identity to experimentally characterized *E. coli* transaminase B; (2) the reaction is reversible PLP-dependent transamination of L-glutamate/2-oxoglutarate with the three branched-chain 2-oxo acids/amino acids; (3) substrate specificity favors all three BCAAs with minor Phe/Tyr activity and a glutamate-selective amino donor; (4) catalysis proceeds by a ping-pong bi-bi mechanism via the conserved Schiff-base Lys183 in the A-A-K-x-G-G-N-Y motif; (5) the enzyme is a soluble cytoplasmic protein of *E. coli*-type homohexameric assembly; and (6) it performs a dual biosynthetic (final BCAA step) and catabolic (first step feeding the Bkd complex) role. No contradictory evidence and no gene-symbol ambiguity were found.

---

## Mechanistic Model / Interpretation

IlvE is best understood as the **reversible transamination hub** connecting the branched-chain amino acids to central nitrogen metabolism. The reaction it catalyzes can be written generically as:

```
  branched-chain 2-oxo acid  +  L-glutamate
             │                        │
             ▼   (IlvE, PLP)          ▼
     branched-chain L-amino acid  +  2-oxoglutarate
```

with the specific substrate pairs:

| 2-oxo acid | ↔ | Branched-chain amino acid |
|---|---|---|
| 2-oxoisovalerate (3-methyl-2-oxobutanoate) | ↔ | L-valine |
| (S)-3-methyl-2-oxopentanoate | ↔ | L-isoleucine |
| 4-methyl-2-oxopentanoate (2-oxoisocaproate) | ↔ | L-leucine |

Catalysis proceeds by the classic **ping-pong bi-bi** two-half-reaction scheme on the **re-face** of PLP:

```
 Half-reaction 1 (deamination of donor):
   E–PLP·Lys183 (internal aldimine) + amino acid
        → external aldimine → quinonoid → ketimine
        → E–PMP + 2-oxo acid (product 1 leaves)

 Half-reaction 2 (amination of acceptor):
   E–PMP + acceptor 2-oxo acid
        → ketimine → quinonoid → external aldimine
        → E–PLP·Lys183 + new amino acid (product 2 leaves)
```

The **conserved Lys183** forms the internal aldimine (Schiff base) with PLP in the resting enzyme and acts as the general acid/base that shuttles protons during the reaction; crystallography of the homologous human enzyme shows this lysine undergoing large conformational swings while the cofactor pyridine ring tilts ~18°. Specificity is imposed twice: on the **branched-chain side** by a hydrophobic pocket of three hydrophobic surfaces that grips aliphatic isopropyl/sec-butyl/isobutyl side chains and enforces L-stereochemistry, and on the **glutamate side** by polar residues that hydrogen-bond glutamate's γ-carboxylate but not aspartate's.

Placed in the metabolic map of *P. putida* KT2440, IlvE occupies a single node with two directional roles:

```
 BIOSYNTHESIS (final step)                    CATABOLISM (first step)
 ─────────────────────────                    ────────────────────────
 pyruvate / 2-oxobutanoate                     Val / Ile / Leu (from
   │ ilvBN (AHAS)                                environment or turnover)
   │ ilvC (reductoisomerase)                          │
   │ ilvD (dihydroxyacid dehydratase)                 │  IlvE  (+ 2-OG → Glu)
   ▼                                                   ▼
 branched-chain 2-oxo acids  ─────►  IlvE  ─────►  branched-chain 2-oxo acids
   (+ leuABCD for leucine)     (+ Glu → 2-OG)              │
   │  IlvE (+ Glu → 2-OG)                                  │  Bkd complex
   ▼                                                       ▼  (BkdR-induced,
 Val / Ile / Leu                                    branched-chain acyl-CoA
                                                     → TCA / energy)
```

Because the reaction is thermodynamically near-reversible, the **direction of flux is set by demand and by regulation of the flanking pathways**, not by IlvE itself. When BCAAs are scarce and being synthesized, IlvE aminates the 2-oxo acids using glutamate; when BCAAs are available as carbon/nitrogen sources, IlvE runs in reverse to feed the **Bkd complex**, whose operon is transcriptionally induced by branched-chain amino acids (via BkdR) and repressed by Crc under carbon-catabolite-repression conditions. IlvE therefore acts as a **constitutive gateway** whose flux is gated by the inducible catabolic machinery downstream and by biosynthetic demand upstream. Its consumption/production of glutamate ↔ 2-oxoglutarate ties BCAA metabolism directly into the cell's core nitrogen economy.

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports the annotation |
|---|---|---|
| [27780341](https://pubmed.ncbi.nlm.nih.gov/27780341/) | *Chemical Mechanism of the BCAT IlvE from M. tuberculosis* | IlvE catalyzes the final step of BCAA synthesis; demonstrates ping-pong kinetic mechanism (F001, F002). |
| [14273641](https://pubmed.ncbi.nlm.nih.gov/14273641/) | *Regulatory mechanisms in Ile/Val biosynthesis* | Names *ilvE* as "transaminase B" within the *ilv* operon (F001). |
| [11642362](https://pubmed.ncbi.nlm.nih.gov/11642362/) | *Structure and function of branched chain aminotransferases* | Defines BCAT substrate scope, fold-type IV class, re-face catalysis, single bacterial BCAT, *E. coli*-type hexamer (F001–F005). |
| [378964](https://pubmed.ncbi.nlm.nih.gov/378964/) | *Transaminase B from E. coli: quaternary structure, substrate specificity* | Direct enzymology of closest ortholog: BCAA + minor aromatic specificity, Km ordering, hexameric double-trimer (F004, F005, F007). |
| [10831406](https://pubmed.ncbi.nlm.nih.gov/10831406/) | *Cloning/inactivation of BCAT of L. lactis* | Knockout quantifies IlvE dominance for Ile/Val, redundancy for Leu/Met/Phe; supports cytosolic localization (F004, F005). |
| [12269802](https://pubmed.ncbi.nlm.nih.gov/12269802/) | *Crystal structures of human mitochondrial BCAT intermediates* | Structural basis of substrate/stereospecificity (hydrophobic surfaces), catalytic Lys/PLP dynamics, glutamate selectivity (F009). |
| [10217783](https://pubmed.ncbi.nlm.nih.gov/10217783/) | *In vitro transcription of bkd operon of P. putida* | Establishes the BCAA catabolic pathway (Bkd) downstream of IlvE; BCAAs are inducers (F006). |
| [10648542](https://pubmed.ncbi.nlm.nih.gov/10648542/) | *Crc in catabolite repression of bkd operons* | Confirms Bkd complex as P. putida catabolic machinery; Crc-mediated repression (F006). |
| [10876155](https://pubmed.ncbi.nlm.nih.gov/10876155/) | *3D structure of ADC lyase from E. coli* | Fold-type IV relative; conserved Arg59/Lys159/Glu193 cofactor contacts illuminate the shared catalytic architecture (F002, F008). |
| [7836297](https://pubmed.ncbi.nlm.nih.gov/7836297/), [8670279](https://pubmed.ncbi.nlm.nih.gov/8670279/), [9068646](https://pubmed.ncbi.nlm.nih.gov/9068646/), [10648543](https://pubmed.ncbi.nlm.nih.gov/10648543/) | *BkdR / bkd operon regulation in P. putida* | Characterize regulation of the catabolic branch that consumes IlvE's 2-oxo-acid products (F006 context). |

The strongest support comes from a **combination of direct orthologous enzymology** (*E. coli* transaminase B, [PMID: 378964](https://pubmed.ncbi.nlm.nih.gov/378964/); *M. tuberculosis* IlvE, [PMID: 27780341](https://pubmed.ncbi.nlm.nih.gov/27780341/); *L. lactis* IlvE knockout, [PMID: 10831406](https://pubmed.ncbi.nlm.nih.gov/10831406/)) and **structural biology** ([PMID: 12269802](https://pubmed.ncbi.nlm.nih.gov/12269802/); [PMID: 10876155](https://pubmed.ncbi.nlm.nih.gov/10876155/)), tied to Q88H54 by **sequence-based orthology** (~48% identity, conserved catalytic Lys183 motif). This layered evidence — biochemical, genetic, structural, and bioinformatic — makes the annotation robust despite the absence of direct biochemical characterization of the *P. putida* protein itself.

### Supported and refuted hypotheses

**Supported:**
- *ilvE*/Q88H54 is a branched-chain aminotransferase (EC 2.6.1.42). ✔ (annotation, orthology, family, EC)
- It transaminates all three BCAAs with glutamate/2-oxoglutarate. ✔ (*E. coli* enzymology)
- It is a cytoplasmic, PLP-dependent fold-type IV enzyme. ✔ (sequence, family, structure)
- It functions both in BCAA biosynthesis (final step) and catabolism (first step, feeding Bkd). ✔ (pathway genetics)

**Refuted / bounded:**
- Not an aspartate- or aromatic-specific transaminase — Phe/Tyr activity is minor/sluggish, and the enzyme is free of aspartate-transaminase activity ([PMID: 378964](https://pubmed.ncbi.nlm.nih.gov/378964/)).
- Not membrane-bound or secreted — no signal peptide or transmembrane segment ([PMID: 10831406](https://pubmed.ncbi.nlm.nih.gov/10831406/)).

---

## Limitations and Knowledge Gaps

1. **No direct biochemical characterization of Q88H54.** The functional annotation rests on orthology transfer from *E. coli*, *M. tuberculosis*, and *L. lactis* IlvE enzymes and on structural studies of the human enzyme. Kinetic constants (Km, kcat), exact substrate ranking, and the quaternary state have not been measured for the *P. putida* protein itself.
2. **Quaternary structure is inferred, not observed.** The homohexameric double-trimer assembly is documented for *E. coli*/*Salmonella* BCATs; while Q88H54 is an *E. coli*-type ortholog, its oligomeric state has not been experimentally determined.
3. **Residue numbering for the catalytic lysine is alignment-based.** Lys183 is assigned by pairwise alignment to *E. coli* IlvE; a crystal structure or PLP-labeling experiment on Q88H54 would confirm the identity of the Schiff-base lysine directly.
4. **In vivo directionality and flux control in *P. putida* are not directly measured.** The dual biosynthetic/catabolic role is inferred from pathway topology and from regulation of the flanking *bkd* operon; the actual flux direction under given growth conditions in KT2440 has not been quantified.
5. **Redundancy in *P. putida* is unquantified.** The *L. lactis* knockout shows partial redundancy for Leu/Met/Phe; whether *P. putida* possesses additional aminotransferases that back up IlvE for these substrates is not established.
6. **Localization is predictive.** Cytoplasmic localization is inferred from the absence of a signal peptide/transmembrane region and from homolog studies, not from experimental fractionation of *P. putida*.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant expression and steady-state kinetics.** Express Q88H54 in *E. coli*, purify, and measure Km/kcat for each branched-chain 2-oxo acid and amino acid, plus 2-oxoglutarate/glutamate, to confirm the predicted substrate ranking and the minor Phe/Tyr activity directly for the *P. putida* enzyme.
2. **Cofactor and mechanism confirmation.** Verify PLP binding spectroscopically (characteristic ~415 nm internal aldimine), demonstrate the PLP↔PMP cycle, and confirm ping-pong kinetics by initial-velocity analysis.
3. **Site-directed mutagenesis of Lys183.** Mutate the predicted Schiff-base lysine (K183A) and show loss of activity, directly validating the alignment-based catalytic residue assignment.
4. **Quaternary structure determination.** Use size-exclusion chromatography with multi-angle light scattering (SEC-MALS) and/or crystallography/cryo-EM to test whether Q88H54 forms the *E. coli*-type homohexamer.
5. **Gene knockout in *P. putida* KT2440.** Construct a Δ*ilvE* (ΔPP_3511) strain and test (a) BCAA auxotrophy (biosynthetic role), (b) inability to grow on Val/Ile/Leu as sole nitrogen/carbon source (catabolic role, coupling to Bkd), and (c) residual transaminase activity toward each substrate to quantify redundancy.
6. **Subcellular localization.** Confirm cytoplasmic localization by cell fractionation and/or a functional fluorescent fusion in KT2440.
7. **Flux/regulation analysis.** Combine transcriptomics/proteomics with ¹⁵N/¹³C metabolic-flux analysis under BCAA-biosynthetic versus BCAA-catabolic growth conditions to determine in vivo reaction directionality and how IlvE flux couples to *bkd* operon induction and Crc-mediated catabolite repression.

---

*Report prepared for the functional annotation of ilvE (UniProt Q88H54, PP_3511) in Pseudomonas putida KT2440. Target identity was verified against the UniProt reference; gene symbol, organism, protein family (class-IV PLP-dependent), and domain architecture all converge on a single, unambiguous BCAT annotation, with no gene-symbol ambiguity detected. All quoted statements are verbatim from the cited PubMed abstracts; sequence identity and residue mapping were computed from UniProt sequences Q88H54 and P0AB80.*


## Artifacts

- [OpenScientist final report](ilvE-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](ilvE-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:14273641
2. PMID:11642362
3. PMID:27780341
4. PMID:10876155
5. PMID:10831406
6. PMID:10217783
7. PMID:10648542
8. PMID:7836297
9. PMID:8670279
10. PMID:9068646
11. PMID:10648543
12. PMID:12269802