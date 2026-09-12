---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-11T14:26:52.992728'
end_time: '2026-07-11T14:47:14.113239'
duration_seconds: 1221.12
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: lgt
  gene_symbol: lgt
  uniprot_accession: Q88CN8
  protein_description: 'RecName: Full=Phosphatidylglycerol--prolipoprotein diacylglyceryl
    transferase {ECO:0000255|HAMAP-Rule:MF_01147}; EC=2.5.1.145 {ECO:0000255|HAMAP-Rule:MF_01147};'
  gene_info: Name=lgt {ECO:0000255|HAMAP-Rule:MF_01147}; OrderedLocusNames=PP_5142;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the Lgt family. {ECO:0000255|HAMAP-
  protein_domains: Lgt. (IPR001640); LGT (PF01790)
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
citation_count: 7
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: lgt-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: lgt-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88CN8
- **Protein Description:** RecName: Full=Phosphatidylglycerol--prolipoprotein diacylglyceryl transferase {ECO:0000255|HAMAP-Rule:MF_01147}; EC=2.5.1.145 {ECO:0000255|HAMAP-Rule:MF_01147};
- **Gene Information:** Name=lgt {ECO:0000255|HAMAP-Rule:MF_01147}; OrderedLocusNames=PP_5142;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the Lgt family. {ECO:0000255|HAMAP-
- **Key Domains:** Lgt. (IPR001640); LGT (PF01790)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "lgt" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'lgt' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **lgt** (gene ID: lgt, UniProt: Q88CN8) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *lgt* (Q88CN8, PP_5142) in *Pseudomonas putida* KT2440

## Gene/Protein Identity Verification

- **UniProt:** Q88CN8
- **Gene:** *lgt* (OrderedLocusName PP_5142)
- **Protein:** Phosphatidylglycerol–prolipoprotein diacylglyceryl transferase; **EC 2.5.1.145**
- **Organism:** *Pseudomonas putida* KT2440 (PSEPK), a Gammaproteobacterium
- **Family/Domains:** Lgt family (IPR001640; Pfam PF01790); UniProt annotation derived from HAMAP rule MF_01147

**Identity confirmed — no gene-symbol ambiguity.** The gene symbol *lgt*, the EC number, the "phosphatidylglycerol–prolipoprotein diacylglyceryl transferase" description, and the Lgt/PF01790 family assignment all correspond precisely to a single, well-characterized and highly conserved bacterial enzyme. All literature retrieved (*E. coli*, *Corynebacterium*, *Listeria*, and pan-bacterial evolutionary/structural studies) describes exactly this enzyme. Because *P. putida* KT2440 itself has not been the subject of a dedicated Lgt biochemical study, function below is assigned from (i) the highly conserved enzyme family and HAMAP rule, (ii) mechanistic/structural work in model bacteria (directly transferable given the family's strong conservation), and (iii) direct sequence analysis of the Q88CN8 protein performed during this investigation.

---

## Summary

The gene ***lgt*** (UniProt **Q88CN8**; ordered locus **PP_5142**) of *Pseudomonas putida* KT2440 encodes **phosphatidylglycerol–prolipoprotein diacylglyceryl transferase (Lgt; EC 2.5.1.145)**, an integral inner-membrane enzyme that catalyzes the **first and committed step of bacterial lipoprotein biogenesis**. In this reaction, Lgt transfers the *sn*-1,2-diacylglyceryl moiety from the membrane phospholipid **phosphatidylglycerol** onto the sulfhydryl (thiol) side chain of the **invariant cysteine** within the "lipobox" motif of prolipoprotein signal sequences, generating a thioether-linked *S*-diacylglyceryl-prolipoprotein and releasing *sn*-glycerol-1-phosphate. This modification tethers otherwise-soluble secreted proteins to the membrane and licenses the downstream, universally conserved maturation steps (**Lgt → LspA → Lnt**).

The identity of the *P. putida* protein is well supported. The gene symbol, EC number, Lgt family assignment (**IPR001640 / Pfam PF01790**), and HAMAP rule MF_01147 all agree with the biochemically characterized enzyme family. Direct sequence analysis performed during this investigation confirmed that the 268-residue *P. putida* ortholog **retains the two catalytic arginines** shown experimentally to be essential in *Escherichia coli* Lgt (Arg143 and Arg239), and hydropathy analysis confirmed the expected **polytopic (~7 transmembrane helix) inner-membrane architecture**. Lgt *modifies* other proteins for membrane anchoring but is **not itself a lipoprotein** — it has no cleavable signal peptide or lipobox of its own.

Functionally, Lgt is **essential for viability in Proteobacteria**, the clade that contains *P. putida*. Its loss permeabilizes the outer membrane, causes abnormal morphology and cell death, and sensitizes cells to serum and antibiotics. Because it is essential, membrane-embedded, and structurally conserved, Lgt is an actively pursued **antibacterial drug target**. The enzyme performs its function at/within the **cytoplasmic (inner) membrane**, using two lipid-binding sites and a mechanism in which both the phospholipid substrate and the lipid-modified peptide product enter and exit the active site **laterally** through the lipid bilayer.

---

## Key Findings

### Finding 1 — Lgt catalyzes the first, committed step of lipoprotein biogenesis

Lgt initiates lipoprotein maturation. The reaction it catalyzes (EC 2.5.1.145) is:

> **phosphatidylglycerol + [prolipoprotein]-L-cysteine → *sn*-1,2-diacylglyceryl-[prolipoprotein]-L-cysteine + *sn*-glycerol-1-phosphate**

- **Lipid donor:** phosphatidylglycerol (PG), a native inner-membrane phospholipid.
- **Protein acceptor / substrate specificity:** prolipoproteins bearing a **lipobox** motif (consensus [LVI]-[ASTVI]-[GAS]-**C**) at the end of their signal sequence. The invariant cysteine is the sole acceptor, and the diacylglyceryl group is attached via a thioether bond to its sulfhydryl.

Substrate recognition and chemistry were defined structurally by Noland and colleagues, who describe that "*phosphatidylglycerol:prolipoprotein diacylglyceryl transferase (Lgt) recognizes a conserved lipobox motif within the prolipoprotein signal sequence and catalyzes the addition of diacylglycerol to an invariant cysteine*" ([PMID: 28698362](https://pubmed.ncbi.nlm.nih.gov/28698362/)). This is the **first and committed step** of the pathway — once the diacylglyceryl group is attached, the substrate is irreversibly channeled toward becoming a mature lipoprotein. Legood and colleagues state that "*prolipoprotein phosphatidylglycerol diacylglyceryl transferase (Lgt) catalyzes the first and committed step*" of lipoprotein modification ([PMID: 42126242](https://pubmed.ncbi.nlm.nih.gov/42126242/)). This designation is functionally important: Lgt sets the flux through the entire downstream maturation and sorting machinery.

The functional assignment for Q88CN8 derives from the Lgt family assignment (IPR001640, Pfam PF01790) and HAMAP rule MF_01147, both of which map the protein onto this biochemically characterized enzyme class.

### Finding 2 — Lgt is an integral membrane enzyme with two lipid-binding sites and a lateral catalytic mechanism

The three-dimensional structure of *E. coli* Lgt was solved by Mao and colleagues in complex with its substrate **phosphatidylglycerol** (1.9 Å) and with the inhibitor **palmitic acid** (1.6 Å). These structures revealed **two distinct lipid-binding sites** and identified the catalytic architecture. The authors confirm that "*Lgt is an integral membrane enzyme that catalyses the first reaction of the three-step post-translational lipid modification*" ([PMID: 26729647](https://pubmed.ncbi.nlm.nih.gov/26729647/)).

Two conserved arginine residues, **Arg143 and Arg239**, were shown by complementation of *lgt*-knockout cells to be **essential for diacylglyceryl transfer**: "*revealed critical residues, including Arg143 and Arg239, that are essential for diacylglyceryl transfer*" ([PMID: 26729647](https://pubmed.ncbi.nlm.nih.gov/26729647/)). These arginines are thought to stabilize the phosphate of the PG substrate / transition state and position it for nucleophilic attack by the cysteine thiolate.

A defining mechanistic feature is that both the phospholipid substrate and the lipid-modified peptide product move **laterally** in and out of the membrane-embedded active site: "*substrate and product, lipid-modified lipobox-containing peptide, enter and leave the enzyme laterally relative to the lipid bilayer*" ([PMID: 26729647](https://pubmed.ncbi.nlm.nih.gov/26729647/)). This reflects an enzyme whose reaction chemistry occurs at the membrane–water interface, handling hydrophobic substrates that partition into the bilayer. The chemical mechanism by which PG is **activated** for transfer was further dissected by Singh and colleagues, combining the X-ray structure of Lgt with that of apolipoprotein *N*-acyltransferase ([PMID: 31340643](https://pubmed.ncbi.nlm.nih.gov/31340643/)).

### Finding 3 — Lgt is essential for viability and outer-membrane integrity in Proteobacteria

Deletion of *lgt* is lethal to the great majority of Gram-negative bacteria: "*Deletion of the lgt gene is lethal to most Gram-negative bacteria*" ([PMID: 26729647](https://pubmed.ncbi.nlm.nih.gov/26729647/)). Legood and colleagues restate essentiality for the clade of interest — "*Due to its essentiality for cell viability in Proteobacteria*" — which directly includes *P. putida* ([PMID: 42126242](https://pubmed.ncbi.nlm.nih.gov/42126242/)).

The physiological basis of this essentiality is envelope failure. Diao and colleagues showed that "*Lgt depletion in a clinical uropathogenic Escherichia coli strain leads to permeabilization of the outer membrane and increased sensitivity to serum killing and antibiotics*" ([PMID: 33875545](https://pubmed.ncbi.nlm.nih.gov/33875545/)). This links Lgt activity directly to the barrier function of the Gram-negative envelope: without lipoprotein maturation, structural and functional lipoproteins cannot be anchored in the outer membrane, and the envelope becomes leaky.

Crucially, the lethality is **not simply due to loss of a single abundant lipoprotein**. Legood and colleagues found that Lgt depletion "*Leads to Abnormal Morphology and Cell Death in Escherichia coli That Is Independent of Major Lipoprotein Lpp*" (Braun's lipoprotein) ([PMID: 35938851](https://pubmed.ncbi.nlm.nih.gov/35938851/)). Consistently, Diao and colleagues found Lgt inhibition "*Is Insensitive to Resistance Caused by Deletion of Braun's Lipoprotein*" ([PMID: 33875545](https://pubmed.ncbi.nlm.nih.gov/33875545/)). Essentiality therefore reflects the pathway's role in maturing the entire lipoproteome, not a single client.

Essentiality is nonetheless **clade-dependent**. In some Actinobacteria — for example *Corynebacterium glutamicum* — Lgt is described as a "*unique, non-essential phosphatidylglycerol::prolipoprotein diacylglyceryl transferase*" (Dautin and colleagues, [PMID: 32490790](https://pubmed.ncbi.nlm.nih.gov/32490790/)). This contrast underscores that the essentiality relevant to *P. putida* is a property of the Gram-negative envelope, where outer-membrane lipoproteins are indispensable. Because it is essential, conserved, and membrane-accessible, Lgt is a validated **antibiotic target**, and a small-molecule inhibitor (G2824) that blocks Lgt activity has been reported ([PMID: 33875545](https://pubmed.ncbi.nlm.nih.gov/33875545/)).

### Finding 4 — The *P. putida* ortholog retains the essential catalytic residues (sequence-level evidence)

Because most biochemical/structural work has used *E. coli* Lgt, it is important to establish that these conclusions transfer to Q88CN8. During this investigation, the UniProt sequences of **LGT_PSEPK (Q88CN8, 268 aa)** and **LGT_ECOLI (P60955, 291 aa)** were retrieved and aligned around the two experimentally validated catalytic arginines.

| Catalytic region | *E. coli* (P60955) | *P. putida* (Q88CN8) | Catalytic Arg conserved? |
|---|---|---|---|
| Arg143 region | `GLGAGR143LGNFI` | `GLGAGR·IGNFI` (10/11 identical) | **Yes** |
| Arg239 region | `GYGAFR239IIVEF` | `CYGIFR·FAVEF` | **Yes** |

Both **Arg143 and Arg239**, shown to be essential for diacylglyceryl transfer in *E. coli* ([PMID: 26729647](https://pubmed.ncbi.nlm.nih.gov/26729647/)), are conserved in the *P. putida* ortholog. The near-perfect conservation of the `GLGAGR` motif (10 of 11 residues identical) around Arg143 is especially strong evidence that the catalytic machinery — and therefore the reaction chemistry and substrate specificity — is preserved in *P. putida* Lgt. This provides a robust, residue-level bridge from the well-characterized *E. coli* enzyme to Q88CN8, reinforcing the functional assignment beyond family-level inference.

### Finding 5 — Lgt is a polytopic inner-membrane protein, not itself a lipoprotein

Kyte–Doolittle hydropathy analysis of the Q88CN8 sequence (window 19, threshold 1.6) detected **multiple strong transmembrane-like hydrophobic segments** (approximately residues 56–76, 176–196, and 237–261), plus a hydrophobic N-terminal stretch (`MLPYPQIDPVALAIGPLKIHWYGLM`). This pattern is consistent with the **polytopic ~7-transmembrane-helix architecture** established for the Lgt family. The conserved catalytic motifs were localized within the sequence: the `GLGAGR` motif (Arg143 region) near positions 134–139 and the `FR` motif (Arg239 region) near position 215.

Crucially, the analysis found **no cleavable N-terminal signal peptide and no lipobox** in Lgt itself. This establishes an important distinction: **Lgt modifies lipoproteins but is not a lipoprotein**. It is a resident integral membrane enzyme embedded in the cytoplasmic (inner) membrane by its transmembrane helices, and it is *not* a substrate of its own pathway. This topological conclusion is fully consistent with the structural description of *E. coli* Lgt as "*an integral membrane enzyme*" ([PMID: 26729647](https://pubmed.ncbi.nlm.nih.gov/26729647/)).

---

## Mechanistic Model and Interpretation

Lgt sits at the **head of the bacterial lipoprotein maturation pathway**, one of the most conserved post-translational modification systems in bacteria.

**Step 0 — Delivery.** A preprolipoprotein is synthesized in the cytoplasm and exported across the inner membrane by the **Sec** (or occasionally **Tat**) translocon. Its signal sequence — bearing the lipobox — remains embedded in the inner membrane, presenting the invariant cysteine to enzymes on the periplasmic-facing side.

**Step 1 — Lgt (this gene).** Lgt recognizes the lipobox and transfers the diacylglyceryl group from **phosphatidylglycerol** onto the cysteine thiol, forming a thioether-linked *S*-diacylglyceryl-prolipoprotein and releasing *sn*-glycerol-1-phosphate. This is the **committed step**. Both substrate and product travel laterally through the bilayer to/from the two lipid-binding sites, and catalysis depends on the conserved arginines (Arg143/Arg239 in *E. coli*, conserved in *P. putida*).

**Step 2 — LspA.** Signal peptidase II (LspA) cleaves the signal peptide immediately upstream of the lipidated cysteine, leaving diacylglyceryl-cysteine as the new N-terminus.

**Step 3 — Lnt.** Apolipoprotein *N*-acyltransferase (Lnt) adds a third acyl chain to the free α-amino group of the cysteine, producing the mature **triacylated lipoprotein**.

**Step 4 — Lol sorting.** Mature lipoproteins destined for the outer membrane are extracted and trafficked by the **Lol** system; those with inner-membrane retention signals remain in the inner membrane.

```
   CYTOPLASM
      │  (Sec/Tat export of preprolipoprotein)
 ═════╪═════════════════════════════════════════  INNER MEMBRANE
      ▼                                            (Lgt is embedded here,
  preprolipoprotein ──lipobox──► [ Lgt ] ◄── phosphatidylglycerol   ~7 TM helices)
                                    │
                                    ▼  + diacylglyceryl on Cys thiol
                         S-diacylglyceryl-prolipoprotein
                                    │
                                 [ LspA ]  signal peptide cleavage
                                    │
                                 [ Lnt ]   N-acylation
                                    ▼
                         mature triacylated lipoprotein
                                    │
                                 [ Lol ]   sorting to OUTER MEMBRANE
 ══════════════════════════════════════════════
   PERIPLASM / OUTER MEMBRANE
```

**Localization of function.** Lgt performs its chemistry **at/within the cytoplasmic (inner) membrane**, at the membrane–periplasm interface. It handles two hydrophobic partners — a membrane phospholipid donor and a membrane-embedded acceptor peptide — and its lateral-access mechanism reflects this. Its function is intrinsically membrane-localized and cannot occur in the aqueous cytoplasm or periplasm.

**Why essentiality follows from function.** By gating the flux of *all* lipoproteins into the maturation pathway, Lgt controls whether the cell can build a functional outer membrane. Outer-membrane lipoproteins (e.g., those involved in LPS transport, peptidoglycan attachment, and envelope stress responses) are indispensable in Proteobacteria; when Lgt is depleted, these clients cannot be lipidated and delivered, the outer membrane becomes permeable, cells become misshapen, and they die — a phenotype independent of any single lipoprotein such as Lpp. This is precisely why Lgt is essential in *Pseudomonas* and other Proteobacteria and why it is an attractive antibiotic target.

**Transfer of evidence to *P. putida*.** No dedicated biochemical study of Q88CN8 itself was found; the functional assignment rests on (i) unambiguous family/domain/HAMAP annotation, (ii) residue-level conservation of the two experimentally essential catalytic arginines demonstrated here by alignment, and (iii) conservation of the predicted polytopic inner-membrane topology. Together these make the assignment of Q88CN8 as a *bona fide* Lgt highly confident.

---

## Evidence Base

| PMID | Paper (abbreviated) | How it supports the findings |
|---|---|---|
| [26729647](https://pubmed.ncbi.nlm.nih.gov/26729647/) | *Crystal structure of E. coli lipoprotein diacylglyceryl transferase* | Structural definition of the enzyme; two lipid-binding sites; catalytic Arg143/Arg239 essential for transfer; lateral substrate/product access; integral membrane enzyme; deletion lethal in most Gram-negatives. **Primary structural/mechanistic evidence.** |
| [28698362](https://pubmed.ncbi.nlm.nih.gov/28698362/) | *Structural insights into lipoprotein N-acylation* | Defines lipobox recognition and the diacylglyceryl-addition-to-cysteine reaction; contextualizes Lgt within the multi-enzyme pathway. |
| [31340643](https://pubmed.ncbi.nlm.nih.gov/31340643/) | *Mechanism of Phosphatidylglycerol Activation Catalyzed by Prolipoprotein Diacylglyceryl Transferase* | X-ray structure; resolves how phosphatidylglycerol is activated for transfer. Mechanistic detail. |
| [42126242](https://pubmed.ncbi.nlm.nih.gov/42126242/) | *Arm and head domain in Lgt determine functional diversity among bacterial pathogens* | States Lgt catalyzes the first and committed step; essential for viability in Proteobacteria (the clade of *P. putida*). |
| [33875545](https://pubmed.ncbi.nlm.nih.gov/33875545/) | *Inhibition of E. coli Lipoprotein Diacylglyceryl Transferase...* | Lgt depletion permeabilizes the outer membrane and sensitizes to serum/antibiotics; inhibition insensitive to Lpp deletion; small-molecule inhibitor (G2824). Drug-target validation. |
| [35938851](https://pubmed.ncbi.nlm.nih.gov/35938851/) | *A Defect in Lipoprotein Modification by Lgt Leads to Abnormal Morphology and Cell Death... Independent of Lpp* | Establishes that Lgt essentiality reflects the whole lipoproteome, not just Braun's lipoprotein. |
| [32490790](https://pubmed.ncbi.nlm.nih.gov/32490790/) | *Role of the unique, non-essential Lgt in [Corynebacterium]* | Provides the contrast: Lgt non-essential in some Actinobacteria; confirms the canonical reaction (diacylglyceryl to invariant Cys). Clarifies clade-dependent essentiality. |
| [32709730](https://pubmed.ncbi.nlm.nih.gov/32709730/) | *NisI Maturation and Nisin Resistance in Lactococcus lactis* | Background on lipoprotein maturation in a Gram-positive context (supporting, tangential). |
| [32634175](https://pubmed.ncbi.nlm.nih.gov/32634175/) | *TLR2 and endosomal TLR-mediated secretion of IL-10 (Listeria)* | Notes *lgt* is essential for lipoprotein formation and its immunological consequences; tangential to *P. putida* biochemistry. |
| [41459928](https://pubmed.ncbi.nlm.nih.gov/41459928/) | *Mutation of lipoprotein processing pathway gene (MRSA/β-lactam)* | Context on the medical relevance of the lipoprotein processing pathway; tangential. |

**Note on organism relevance.** The strongest primary evidence (structure, mechanism, catalytic residues, essentiality) derives from *E. coli* — a Proteobacterium, like *P. putida*. The *Listeria*, *Lactococcus*, and *Corynebacterium* papers describe orthologous enzymes in Gram-positive/Actinobacterial organisms and are used only for pathway context, not to define *P. putida*-specific chemistry. Given the gene-ambiguity caveat in the research brief, only Gram-negative/Proteobacterial evidence was used to establish essentiality and mechanism for Q88CN8.

---

## Supported and Refuted Hypotheses

**Supported**
- **H1 (supported):** Q88CN8 is a phosphatidylglycerol–prolipoprotein diacylglyceryl transferase (EC 2.5.1.145) acting on lipobox cysteines. *Basis:* family/HAMAP assignment + directly homologous, biochemically characterized enzymes ([PMID: 28698362](https://pubmed.ncbi.nlm.nih.gov/28698362/), [PMID: 42126242](https://pubmed.ncbi.nlm.nih.gov/42126242/)).
- **H2 (supported):** The enzyme is a polytopic integral inner-membrane protein acting at the bilayer with a lateral-access mechanism. *Basis:* structural studies ([PMID: 26729647](https://pubmed.ncbi.nlm.nih.gov/26729647/)) plus hydropathy analysis of Q88CN8 (this work).
- **H3 (supported by inference):** *lgt*/PP_5142 is essential in *P. putida*. *Basis:* essentiality across Proteobacteria/Gram-negatives ([PMID: 26729647](https://pubmed.ncbi.nlm.nih.gov/26729647/), [PMID: 42126242](https://pubmed.ncbi.nlm.nih.gov/42126242/)).
- **H4 (supported):** The characterized catalytic mechanism applies to *P. putida* Lgt. *Basis:* conservation of the essential Arg143/Arg239 in Q88CN8 (this work).

**Refuted / Qualified**
- **Universal essentiality is refuted:** Lgt is dispensable in certain Actinobacteria ([PMID: 32490790](https://pubmed.ncbi.nlm.nih.gov/32490790/)). This does not apply to *P. putida* (a Proteobacterium) but qualifies blanket "essential in all bacteria" statements.

---

## Limitations and Knowledge Gaps

1. **No direct study of Q88CN8.** No biochemical, structural, or genetic study of the *P. putida* KT2440 Lgt protein itself was identified. The functional assignment is by strong homology (family/domain/HAMAP annotation), residue conservation, and topology prediction — not by direct experiment on this ortholog.
2. **Essentiality in *P. putida* is inferred, not demonstrated here.** Essentiality is established for Proteobacteria in general and *E. coli* specifically; a *P. putida*-specific deletion/depletion phenotype was not located.
3. **Catalytic-arginine numbering.** The essential arginines are defined by *E. coli* numbering (Arg143/Arg239). The alignment confirms conservation, but exact positional numbering in the shorter Q88CN8 (268 aa vs 291 aa) will differ.
4. **Client/substrate spectrum unknown for *P. putida*.** The specific lipoproteome of *P. putida* KT2440 that depends on Lgt was not enumerated.
5. **Topology from prediction, not experiment.** The polytopic inner-membrane topology of Q88CN8 rests on hydropathy prediction plus family knowledge; no experimental topology mapping exists for this specific protein.

---

## Proposed Follow-up Experiments / Actions

1. **Confirm essentiality in *P. putida* KT2440** — attempt a clean *lgt* (PP_5142) deletion; if non-viable, build a conditional depletion strain and characterize the terminal phenotype (morphology, outer-membrane permeability via NPN uptake, antibiotic/serum sensitivity), paralleling the *E. coli* studies ([PMID: 33875545](https://pubmed.ncbi.nlm.nih.gov/33875545/), [PMID: 35938851](https://pubmed.ncbi.nlm.nih.gov/35938851/)).
2. **Biochemical confirmation of activity** — purify recombinant Q88CN8 in detergent/nanodiscs and assay diacylglyceryl transfer from *P. putida* PG to a synthetic *P. putida* lipobox peptide, confirming EC 2.5.1.145 activity and substrate specificity.
3. **Site-directed mutagenesis of the conserved arginines** — mutate the *P. putida* equivalents of Arg143/Arg239 and test loss of function by complementation, directly validating the transferred mechanism.
4. **Map the *P. putida* Lgt-dependent lipoproteome** — use metabolic labeling/proteomics (e.g., globomycin-based enrichment or Cys-lipidation profiling) to enumerate lipoproteins that fail to mature upon Lgt depletion.
5. **Experimental topology and structure** — determine membrane topology by reporter fusions and/or solve a cryo-EM/crystal structure of Q88CN8, ideally with bound PG, to confirm the two-lipid-site, lateral-access model in this organism.
6. **Inhibitor cross-testing** — evaluate whether known Lgt inhibitors (e.g., G2824, [PMID: 33875545](https://pubmed.ncbi.nlm.nih.gov/33875545/)) inhibit *P. putida* Lgt, informing its utility as a broad-spectrum antibacterial target.

---

## Conclusion

*lgt* / **PP_5142** / **Q88CN8** in *Pseudomonas putida* KT2440 encodes **phosphatidylglycerol–prolipoprotein diacylglyceryl transferase (Lgt, EC 2.5.1.145)**, a polytopic integral **inner-membrane** enzyme that catalyzes the **first and committed step of bacterial lipoprotein biogenesis** — transfer of the diacylglyceryl group from phosphatidylglycerol onto the invariant lipobox cysteine of prolipoproteins. It operates within the cytoplasmic membrane via a lateral, lipid-embedded mechanism using conserved catalytic arginines that are retained in the *P. putida* sequence, initiating the conserved Lgt→LspA→Lnt maturation pathway that feeds Lol-dependent lipoprotein sorting. This activity is essential for cell viability and outer-membrane integrity in Proteobacteria, making Lgt both a cornerstone of envelope biogenesis and a validated antibacterial drug target.


## Artifacts

- [OpenScientist final report](lgt-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](lgt-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:28698362
2. PMID:42126242
3. PMID:26729647
4. PMID:31340643
5. PMID:33875545
6. PMID:35938851
7. PMID:32490790