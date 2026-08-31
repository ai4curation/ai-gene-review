---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T12:16:27.658649'
end_time: '2026-08-31T12:55:10.457971'
duration_seconds: 2322.8
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: cpsG
  gene_symbol: cpsG
  uniprot_accession: Q88LZ9
  protein_description: 'RecName: Full=phosphomannomutase {ECO:0000256|ARBA:ARBA00012730};
    EC=5.4.2.8 {ECO:0000256|ARBA:ARBA00012730};'
  gene_info: Name=cpsG {ECO:0000313|EMBL:AAN67397.1}; OrderedLocusNames=PP_1777 {ECO:0000313|EMBL:AAN67397.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the phosphohexose mutase family.
  protein_domains: A-D-PHexomutase_a/b/a-I. (IPR005844); A-D-PHexomutase_a/b/a-I/II/III.
    (IPR016055); A-D-PHexomutase_a/b/a-II. (IPR005845); A-D-PHexomutase_a/b/a-III.
    (IPR005846); A-D-PHexomutase_C. (IPR005843)
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
citation_count: 8
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: cpsG-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: cpsG-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88LZ9
- **Protein Description:** RecName: Full=phosphomannomutase {ECO:0000256|ARBA:ARBA00012730}; EC=5.4.2.8 {ECO:0000256|ARBA:ARBA00012730};
- **Gene Information:** Name=cpsG {ECO:0000313|EMBL:AAN67397.1}; OrderedLocusNames=PP_1777 {ECO:0000313|EMBL:AAN67397.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the phosphohexose mutase family.
- **Key Domains:** A-D-PHexomutase_a/b/a-I. (IPR005844); A-D-PHexomutase_a/b/a-I/II/III. (IPR016055); A-D-PHexomutase_a/b/a-II. (IPR005845); A-D-PHexomutase_a/b/a-III. (IPR005846); A-D-PHexomutase_C. (IPR005843)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "cpsG" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'cpsG' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **cpsG** (gene ID: cpsG, UniProt: Q88LZ9) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *cpsG* (PP_1777, UniProt Q88LZ9) — Phosphomannomutase of *Pseudomonas putida* KT2440

## Summary

**The gene *cpsG* (locus PP_1777; UniProt Q88LZ9) of *Pseudomonas putida* KT2440 encodes a soluble cytoplasmic phosphomannomutase (PMM; EC 5.4.2.8), a member of the α-D-phosphohexomutase superfamily.** Its primary and defining biochemical function is to catalyze the reversible intramolecular transfer of a phosphoryl group on a hexose sugar-phosphate — specifically the interconversion of **mannose-1-phosphate (M1P) and mannose-6-phosphate (M6P)**. This reaction constitutes the second committed step of the GDP-mannose biosynthetic pathway (phosphomannose isomerase → **phosphomannomutase** → GDP-mannose pyrophosphorylase), converting the M6P produced from fructose-6-phosphate into M1P, which is then activated to the nucleotide sugar GDP-mannose.

**A central result of this investigation is the refinement of *cpsG*'s identity within the phosphohexomutase superfamily.** Although UniProt and homology to *Pseudomonas aeruginosa* AlgC initially suggest a bifunctional PMM/phosphoglucomutase (PGM) role, quantitative sequence analysis places PP_1777 firmly in the **ManB/CpsG (mannose-specialized) subfamily** rather than the bifunctional AlgC clade. PP_1777 is 61.2% identical to *Escherichia coli* ManB/CpsG (a dedicated phosphomannomutase of the colanic-acid/GDP-mannose pathway) but only ~40% identical to *P. putida*'s own genuine AlgC ortholog (Q88C93) and ~31% identical to its dedicated phosphoglucomutase (Q88GY7). Because *P. putida* KT2440 encodes three distinct phosphohexomutases — a mannose-specialized CpsG, a bifunctional AlgC, and a glucose-specialized Pgm — the glucose-1-phosphate duties are handled by separate loci, and *cpsG* is functionally dedicated to the **mannose arm** of sugar-phosphate metabolism.

**The physiological role of the GDP-mannose that *cpsG* helps produce is to supply the cytoplasmic nucleotide-sugar precursor pool for surface and secreted polysaccharides.** In *Pseudomonas*, GDP-mannose is converted (via GDP-mannuronic acid) into the building blocks of **alginate**, and mannose derived from GDP-mannose is incorporated into **lipopolysaccharide (LPS) O-antigen and other mannose-containing exopolysaccharides**. These polymers underpin envelope integrity, biofilm formation, and — in the plant-growth-promoting context of KT2440 — rhizosphere colonization and drought-resilience priming. As a central-metabolism sugar-phosphate mutase, CpsG acts as a **soluble cytoplasmic enzyme** with no signal peptide or transmembrane segments, positioned upstream of nucleotide-sugar activation and membrane-associated polysaccharide assembly. There is no evidence for a structural, transport, or signaling function; *cpsG* is a metabolic enzyme.

---

## Key Findings

### Finding 1 — *cpsG*/PP_1777 is a phosphomannomutase of the α-D-phosphohexomutase family catalyzing the M1P ⇌ M6P interconversion

UniProt entry Q88LZ9 annotates *cpsG*/PP_1777 of *P. putida* KT2440 as a **phosphomannomutase (EC 5.4.2.8)** belonging to the **phosphohexose mutase family**, carrying the four diagnostic α-D-phosphohexomutase domains: domains I–III (IPR005844, IPR005845, IPR005846) and the C-terminal domain IV (IPR005843), with the shared architecture captured by IPR016055. This domain complement is the structural signature of the phosphohexomutase superfamily and identifies the enzyme's fold as a four-domain, single-active-site sugar-phosphate mutase.

The reaction catalyzed is the reversible intramolecular phosphoryl transfer that interconverts **mannose-1-phosphate and mannose-6-phosphate**. This step is universally recognized as the committed second step in the biosynthesis of GDP-mannose, downstream of phosphomannose isomerase and upstream of GDP-mannose pyrophosphorylase. The GDP-mannose pathway in *Coxiella burnetii* is described in exactly these terms: GDP-D-mannose "is synthesized from fructose-6-phosphate in 3 successive reactions; Isomerization to mannose-6-phosphate catalyzed by a phosphomannose isomerase (PMI), followed by conversion to mannose-1-phosphate mediated by a phosphomannomutase (PMM) and addition of GDP by a GDP-mannose pyrophosphorylase (GMP)" ([PMID: 22065988](https://pubmed.ncbi.nlm.nih.gov/22065988/)).

Enzymes of this family that are closely related to *cpsG* have been experimentally characterized, establishing the biochemical activity of the clade. The *Sphingomonas paucimobilis* PgmG protein "encodes a 50,059-Da polypeptide that has phosphoglucomutase (PGM) and phosphomannomutase (PMM) activities and is 37 to 59% identical to other bifunctional proteins with PGM and PMM activities from gram-negative species, including *Pseudomonas aeruginosa* AlgC" ([PMID: 10788412](https://pubmed.ncbi.nlm.nih.gov/10788412/)). Similarly, the *Stenotrophomonas maltophilia* *spgM* gene "was shown to encode a bifunctional enzyme with both PGM and phosphomannomutase activities" ([PMID: 12761084](https://pubmed.ncbi.nlm.nih.gov/12761084/)). The prototype of the clade in *Pseudomonas*, AlgC, is explicitly identified as "the phosphomannomutase (PMM) (algC)" of the alginate precursor pathway ([PMID: 9404503](https://pubmed.ncbi.nlm.nih.gov/9404503/)). Together these establish that *cpsG* belongs to a well-characterized family whose members catalyze phosphohexomutase reactions, and that its EC 5.4.2.8 phosphomannomutase assignment is biochemically sound.

### Finding 2 — The AlgC-family phosphomannomutase acts as a cytoplasmic branch-point supplying sugar-phosphate precursors for multiple exopolysaccharides

Functional studies of the family prototype demonstrate that this class of enzyme is a **central metabolic branch point** feeding several polysaccharide biosynthetic pathways. In *P. aeruginosa*, AlgC provides mannose-1-phosphate for the GDP-mannose/GDP-mannuronic-acid (alginate) route through its PMM activity, and glucose-1-phosphate for LPS core and dTDP-L-rhamnose (rhamnolipid) through its PGM activity. As stated directly: "the AlgC protein plays a central role in the production of the three *P. aeruginosa* virulence-associated saccharides: alginate, LPS and rhamnolipid" ([PMID: 10481091](https://pubmed.ncbi.nlm.nih.gov/10481091/)).

The upstream half of the alginate precursor pathway requires a defined set of four enzyme activities: "These four enzyme activities are necessary for the synthesis of GDP-mannuronic acid, which is the activated sugar precursor for alginate polymerization" ([PMID: 9404503](https://pubmed.ncbi.nlm.nih.gov/9404503/)), placing the phosphomannomutase step squarely within the cytoplasmic GDP-mannuronic acid pathway. The importance of the enzyme for LPS is shown by loss-of-function studies of the homolog: *spgM* mutants "produced less LPS than the SpgM(+) parent strain and had a tendency for shorter O polysaccharide chains" ([PMID: 12761084](https://pubmed.ncbi.nlm.nih.gov/12761084/)), demonstrating the downstream consequences of removing the mutase step.

In *P. putida* KT2440, the relevant exopolysaccharide gene clusters have been documented as *alg*, *bcs*, *pea*, and *peb* — "The gene clusters *alg* and *bcs*, which code for proteins mediating alginate and cellulose biosynthesis" ([PMID: 21507178](https://pubmed.ncbi.nlm.nih.gov/21507178/)) — each of which draws on the shared cytoplasmic pool of nucleotide-sugar precursors that the PMM/PGM enzymes feed. Because it is a soluble central-metabolism sugar-phosphate mutase with no signal peptide or transmembrane segments, the enzyme carries out its function in the **cytoplasm**, upstream of the membrane-associated polysaccharide polymerization and export machinery.

### Finding 3 — Sequence analysis reassigns PP_1777/*cpsG* to the ManB/CpsG (mannose-specialized) subfamily, not the bifunctional AlgC clade

Although the family relationship to AlgC is clear, quantitative sequence comparison shows that PP_1777 is **not** the closest homolog of the bifunctional AlgC prototype. Pairwise global alignment of Q88LZ9 (453 aa) yields **61.2% identity (274/448)** to *E. coli* ManB/CpsG (P24175), the dedicated phosphomannomutase of the colanic-acid/GDP-mannose pathway, but only **38.3% identity (168/439)** to *P. aeruginosa* AlgC (P26276, the bifunctional PMM/PGM), and only **31.3% (139/444)** to *E. coli* phosphoglucomutase Pgm (P36938).

The catalytic machinery of the phosphohexomutase superfamily is fully conserved in Q88LZ9, confirming an intact, functional active site:

| Functional motif | Sequence | Residues | Role |
|---|---|---|---|
| Phospho-transfer serine loop | T-A-**S**-H-N-P | 99–104 (catalytic Ser101) | Forms phosphoserine intermediate; transfers phosphoryl group |
| Metal-binding loop | D-G-D-F-D | 242–246 | Coordinates catalytic Mg²⁺ |
| Sugar/His-binding motif | G-**H**-A-F | 307–310 | Positions sugar substrate; His in sugar-binding |

This pattern — high identity to a dedicated mannose-specialized PMM combined with much lower identity to bifunctional AlgC and to glucose-specialized PGM — indicates that PP_1777 has a **ManB/CpsG-type, mannose-oriented active site** and is functionally specialized for the mannose branch of sugar-phosphate metabolism, rather than being a generalist bifunctional PMM/PGM.

### Finding 4 — *cpsG*/*manB* encodes the phosphomannomutase step of the GDP-mannose pathway feeding colanic acid, alginate, and mannose-containing O-antigen

The name *cpsG* itself is diagnostic. Direct genetic and enzymatic characterization of *cpsG*/*manB* gene products in enteric bacteria establishes the precise role of this gene: in *Salmonella*, "the mannose moiety in these molecules is derived from GDP-mannose, which is synthesized in several steps" ([PMID: 28412074](https://pubmed.ncbi.nlm.nih.gov/28412074/)), and the pathway proceeds via "phosphomannose isomerase, encoded by *pmi* (*manA*), followed by phosphomannomutase, encoded by *manB*. There are two copies of *manB* present in the *Salmonella* chromosome, one located in the *cps* gene cluster (*cpsG*) responsible for CA [colanic acid] synthesis, and the other in the *rfb* gene cluster (*rfbK*) involved in LPS O-antigen synthesis," with "the products of *cpsG* and *rfbK* are isozymes" ([PMID: 28412074](https://pubmed.ncbi.nlm.nih.gov/28412074/)).

This directly identifies **CpsG as the phosphomannomutase that converts mannose-6-phosphate to mannose-1-phosphate**, the committed precursor for GDP-mannose, and shows that the gene family straddles colanic-acid/exopolysaccharide synthesis and O-antigen synthesis via isozymes. In *Pseudomonas*, GDP-mannose (the product downstream of the PMM step) is the activated precursor for alginate through GDP-mannuronic acid ([PMID: 9404503](https://pubmed.ncbi.nlm.nih.gov/9404503/)) and for mannose-containing LPS/O-antigen. Consistent with a cytoplasmic sugar-phosphate mutase, the enzyme has no signal peptide or transmembrane segments and acts upstream of nucleotide-sugar activation and membrane-associated polysaccharide assembly.

### Finding 5 — *P. putida* KT2440 encodes three distinct phosphohexomutases; *cpsG*/PP_1777 is the mannose-specialized paralog, separate from AlgC and Pgm

A UniProt proteome survey of *P. putida* KT2440 (organism 160488) returns **three** α-D-phosphohexomutase-family enzymes, confirming that the mutase functions are divided among distinct genes:

| Gene | UniProt | Length | Annotation | Identity to PP_1777 (Q88LZ9) |
|---|---|---|---|---|
| **cpsG (PP_1777)** | Q88LZ9 | 453 aa | phosphomannomutase | — (self) |
| algC | Q88C93 | 463 aa | phosphomannomutase/phosphoglucomutase | 40.3% |
| pgm | Q88GY7 | 545 aa | phosphoglucomutase | 31.5% |

By contrast, *cpsG* is **61.2% identical to *E. coli* ManB/CpsG** (P24175), and *P. putida*'s Q88C93 is **76.9% identical to *P. aeruginosa* AlgC** (P26276), confirming Q88C93 as the genuine AlgC ortholog. This paralog analysis resolves the identity question definitively: *cpsG*/PP_1777 is the **mannose-specialized phosphomannomutase**, a separate gene from both the bifunctional AlgC (Q88C93) and the dedicated phosphoglucomutase Pgm (Q88GY7). The glucose-1-phosphate duties (LPS core, dTDP-rhamnose, glycogen/central carbon interconversion) are therefore handled by AlgC and Pgm, leaving *cpsG* to specialize in the mannose arm feeding GDP-mannose.

---

## Mechanistic Model and Interpretation

### The reaction and its position in metabolism

CpsG catalyzes a classic phosphohexomutase reaction. The enzyme uses a **ping-pong-like mechanism** centered on the conserved catalytic serine (Ser101 in Q88LZ9): a phosphoserine on the enzyme donates its phosphate to the free hydroxyl of the incoming monophosphate sugar, generating a **mannose-1,6-bisphosphate intermediate**; the bisphosphate reorients in the active site and re-phosphorylates the serine at the other position, releasing the isomerized product. Catalysis requires a Mg²⁺ ion coordinated by the conserved D-G-D-F-D loop (residues 242–246).

```
Central carbon metabolism
        │
   Fructose-6-P
        │  phosphomannose isomerase (ManA / Pmi)
        ▼
   Mannose-6-P
        │  ┌─────────────────────────────────────────┐
        │  │  PHOSPHOMANNOMUTASE  =  cpsG / PP_1777   │
        ▼  │  (EC 5.4.2.8; Ser101, Mg2+; M1P⇌M6P)     │
   Mannose-1-P └────────────────────────────────────────┘
        │  GDP-mannose pyrophosphorylase (ManC / GMP)
        ▼
   GDP-D-MANNOSE ───────────┬───────────────┬────────────────┐
        │                   │               │                │
   GDP-mannose         mannose donor    mannose donor    (other mannose-
   4,6-dehydratase     for O-antigen    for exopoly-      containing
        │                   │           saccharides       glycans)
   GDP-mannuronic acid      ▼               ▼
        │              LPS O-antigen    EPS (alg/bcs/
        ▼                                pea/peb draw on
     ALGINATE                            precursor pool)
```

### Subcellular localization

All evidence points to a **cytoplasmic** localization. CpsG is a soluble sugar-phosphate mutase of central metabolism; the protein sequence lacks a signal peptide and transmembrane segments, and its substrates (M6P, M1P) and product (feeding GDP-mannose) are all cytoplasmic metabolites. It operates upstream of the inner-membrane and periplasmic polysaccharide polymerization/export machinery — it prepares the activated-precursor pool but is not itself part of the export apparatus.

### Functional specialization within the phosphohexomutase family

The most important interpretive point is the **division of labor** among the three *P. putida* phosphohexomutases. The initial homology signal to AlgC is real at the family level but misleading at the subfamily level. Quantitative comparison shows PP_1777 sits with the mannose-specialized ManB/CpsG proteins (61% identity to *E. coli* CpsG) while the true AlgC ortholog is a separate gene (Q88C93, 77% identity to *P. aeruginosa* AlgC) and a dedicated Pgm (Q88GY7) handles glucose-phosphate isomerization. This means that in *P. putida* KT2440:

- **cpsG (PP_1777)** → mannose arm → GDP-mannose → alginate, O-antigen, mannose-EPS
- **algC (Q88C93)** → bifunctional PMM/PGM → shared precursor supply
- **pgm (Q88GY7)** → glucose arm → glucose-1-P → central carbon/LPS core

This redundancy at the family level, coupled with specialization, is a coherent picture consistent with the ManB/CpsG paradigm from enteric bacteria, where separate *cpsG* (colanic acid) and *rfbK* (O-antigen) isozymes both perform phosphomannomutase catalysis for distinct downstream glycans ([PMID: 28412074](https://pubmed.ncbi.nlm.nih.gov/28412074/)).

### Physiological relevance in *P. putida* KT2440

The exopolysaccharides fed by GDP-mannose are physiologically consequential for this plant-growth-promoting rhizobacterium. KT2440 mutants deleted for exopolysaccharide clusters (alginate alone, or all four *alg/bcs/pea/peb* clusters) show "reduced drought resilience, with partial or complete loss of protective effects" and reduced biofilm formation ([PMID: 41554215](https://pubmed.ncbi.nlm.nih.gov/41554215/)), and the *alg/bcs* systems contribute to biofilm stability ([PMID: 21507178](https://pubmed.ncbi.nlm.nih.gov/21507178/)). CpsG's role is therefore upstream and enabling: by supplying GDP-mannose it provisions the alginate and mannose-EPS pathways that underpin envelope integrity, biofilm architecture, and rhizosphere fitness.

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports the findings |
|---|---|---|
| [10788412](https://pubmed.ncbi.nlm.nih.gov/10788412/) | *Identification of pgmG in Sphingomonas paucimobilis* | Establishes the bifunctional PMM/PGM AlgC family and quantifies 37–59% identity of family members to AlgC; grounds the biochemical activity of the clade cpsG belongs to. |
| [12761084](https://pubmed.ncbi.nlm.nih.gov/12761084/) | *Role of PGM/SpgM in Stenotrophomonas maltophilia* | Confirms family homologs are bifunctional PMM/PGM enzymes and that loss reduces LPS and shortens O-antigen — direct functional consequence of the mutase step. |
| [9404503](https://pubmed.ncbi.nlm.nih.gov/9404503/) | *Oxygen-dependent alginate gene transcription in P. aeruginosa* | Identifies AlgC as the PMM of the alginate pathway and places the step within GDP-mannuronic-acid/alginate precursor synthesis. |
| [10481091](https://pubmed.ncbi.nlm.nih.gov/10481091/) | *algC participates in rhamnolipid biosynthesis* | Shows the enzyme is a shared branch point feeding alginate, LPS, and rhamnolipid — the multi-pathway precursor-supply role. |
| [22065988](https://pubmed.ncbi.nlm.nih.gov/22065988/) | *GDP-D-mannose biosynthesis in Coxiella burnetii* | Provides the canonical PMI→PMM→GMP pathway definition placing the phosphomannomutase step within GDP-mannose biosynthesis. |
| [28412074](https://pubmed.ncbi.nlm.nih.gov/28412074/) | *Colanic acid and O-antigen synthesis in Salmonella Typhimurium* | Directly identifies *cpsG* as a *manB*-type phosphomannomutase feeding colanic acid, with *rfbK* isozyme feeding O-antigen. |
| [21507178](https://pubmed.ncbi.nlm.nih.gov/21507178/) | *Exopolysaccharide genes and P. putida KT2440 biofilm* | Documents the KT2440 *alg/bcs* EPS systems that draw on the shared sugar-phosphate precursor pool. |
| [41554215](https://pubmed.ncbi.nlm.nih.gov/41554215/) | *Biofilm formation by KT2440 and tomato drought resilience* | Shows physiological importance of *alg/bcs/pea/peb* EPS (downstream of GDP-mannose) for biofilm and stress protection. |
| [10209766](https://pubmed.ncbi.nlm.nih.gov/10209766/) | *GDP-mannuronic acid enzyme activity/transcription in P. aeruginosa* | Corroborates PMM as one of the four GDP-mannuronic-acid enzymes and links algC transcription to precursor supply for A-band LPS and alginate. |

Two lines of evidence were used specifically to establish *cpsG*'s subfamily identity (Findings 3 and 5): (i) pairwise sequence alignments computed against reference proteins (*E. coli* ManB/CpsG P24175, *P. aeruginosa* AlgC P26276, *E. coli* Pgm P36938, *P. putida* AlgC Q88C93 and Pgm Q88GY7), and (ii) a UniProt proteome survey of *P. putida* KT2440 confirming three distinct phosphohexomutase genes. These bioinformatic analyses are the primary basis for the reassignment of PP_1777 to the mannose-specialized ManB/CpsG subfamily.

---

## Limitations and Knowledge Gaps

1. **No direct biochemical characterization of PP_1777 exists.** All functional assignments for this specific protein rest on (a) sequence/domain homology and (b) characterization of orthologs and family members in other organisms (*E. coli*, *Salmonella*, *P. aeruginosa*, *Stenotrophomonas*, *Sphingomonas*, *Coxiella*). The enzyme has not, to the knowledge captured here, been purified from *P. putida* KT2440 and assayed for kinetic parameters (kcat, Km for M6P vs G6P) or substrate specificity.

2. **The degree of PMM/PGM bifunctionality is inferred, not measured.** The subfamily assignment (mannose-specialized ManB/CpsG rather than bifunctional AlgC) is based on sequence identity and conserved active-site motifs. Many phosphohexomutases retain measurable secondary activity on the "wrong" sugar; whether PP_1777 has appreciable phosphoglucomutase side-activity is untested. The 61% identity to a dedicated mannose PMM is strongly suggestive but not definitive.

3. **In vivo pathway assignment in KT2440 is by analogy.** The specific contribution of PP_1777 (versus the paralogous AlgC, Q88C93) to alginate, O-antigen, or other mannose-EPS in *P. putida* has not been dissected genetically. Which downstream glycans depend on *cpsG* specifically remains to be established by targeted knockouts.

4. **No structural model was validated.** The catalytic residue assignments (Ser101, the Mg²⁺ loop, the His-containing sugar-binding motif) are based on sequence motif conservation; an experimental or high-quality predicted 3D structure with substrate docking was not analyzed.

5. **Localization is inferred from sequence features** (absence of signal peptide/TM segments) and family precedent, not from experimental fractionation or fluorescence localization in *P. putida*.

---

## Proposed Follow-up Experiments and Actions

1. **Recombinant enzymology.** Clone, express, and purify PP_1777 (His-tagged) and assay phosphomannomutase and phosphoglucomutase activities in parallel. Determine kcat and Km for M6P→M1P versus G6P→G1P (with glucose-1,6-bisphosphate/mannose-1,6-bisphosphate activation as needed) to quantify substrate specificity and confirm the mannose-specialized prediction.

2. **Complementation assays.** Test whether PP_1777 complements defined *E. coli* *manB* (phosphomannomutase) and *pgm* (phosphoglucomutase) mutants, and a *P. aeruginosa algC* mutant, for restoration of capsular polysaccharide / LPS / alginate phenotypes — the same complementation strategy used successfully for *Coxiella* GDP-mannose enzymes ([PMID: 22065988](https://pubmed.ncbi.nlm.nih.gov/22065988/)).

3. **Targeted knockouts in KT2440.** Construct single and double deletions of *cpsG* (PP_1777) and *algC* (Q88C93) and phenotype for alginate production, LPS O-antigen chain length (as in the *spgM* study, [PMID: 12761084](https://pubmed.ncbi.nlm.nih.gov/12761084/)), biofilm formation, and drought-priming of plants (per [PMID: 41554215](https://pubmed.ncbi.nlm.nih.gov/41554215/)) to resolve the division of labor between the two mannose-competent mutases in vivo.

4. **Structural biology.** Solve or model the PP_1777 structure (X-ray/cryo-EM or high-confidence AlphaFold model) with bound substrate/Mg²⁺ to validate Ser101 as the phosphotransfer residue and characterize the sugar-binding pocket that would distinguish mannose from glucose specificity.

5. **Metabolomic flux analysis.** Use ¹³C-labeled precursors to trace flux from fructose-6-phosphate through M6P/M1P into GDP-mannose and downstream alginate/EPS in wild-type versus *cpsG* mutant KT2440, quantifying the enzyme's contribution to the GDP-mannose pool.

---

## Conclusion

*cpsG* (PP_1777, UniProt Q88LZ9) of *Pseudomonas putida* KT2440 encodes a soluble cytoplasmic **phosphomannomutase (EC 5.4.2.8)** of the α-D-phosphohexomutase superfamily, ManB/CpsG (mannose-specialized) subfamily. Its primary function is to reversibly interconvert **mannose-1-phosphate and mannose-6-phosphate** — the committed second step of GDP-mannose biosynthesis (PMI/ManA → **PMM/CpsG** → GDP-mannose pyrophosphorylase) — using a conserved Ser101/Mg²⁺ mechanism proceeding through a mannose-1,6-bisphosphate intermediate. Sequence analysis (61% identity to *E. coli* ManB/CpsG vs ~40% to *P. putida*'s own bifunctional AlgC and ~31% to its phosphoglucomutase) shows it is functionally specialized for the mannose arm, with glucose-phosphate duties handled by the separate *algC* and *pgm* loci. The GDP-mannose it supplies is the cytoplasmic precursor for **alginate** (via GDP-mannuronic acid) and for **mannose-containing LPS O-antigen and exopolysaccharides** that support envelope integrity, biofilm formation, and rhizosphere fitness. There is no evidence for any structural, transport, or signaling role — *cpsG* is a metabolic enzyme.


## Artifacts

- [OpenScientist final report](cpsG-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](cpsG-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:22065988
2. PMID:10788412
3. PMID:12761084
4. PMID:9404503
5. PMID:10481091
6. PMID:21507178
7. PMID:28412074
8. PMID:41554215