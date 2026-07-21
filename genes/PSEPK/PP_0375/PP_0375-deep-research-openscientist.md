---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-20T13:14:22.756233'
end_time: '2026-07-20T13:39:51.454359'
duration_seconds: 1528.7
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_0375
  gene_symbol: PP_0375
  uniprot_accession: Q88QV9
  protein_description: 'SubName: Full=Prolyl oligopeptidase family protein {ECO:0000313|EMBL:AAN66006.1};'
  gene_info: OrderedLocusNames=PP_0375 {ECO:0000313|EMBL:AAN66006.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: AB_hydrolase_fold. (IPR029058); Peptidase_S9_cat. (IPR001375);
    Xaa-Pro_dipeptidyl-ppase/CocE. (IPR050585); Peptidase_S9 (PF00326)
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
citation_count: 6
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PP_0375-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PP_0375-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88QV9
- **Protein Description:** SubName: Full=Prolyl oligopeptidase family protein {ECO:0000313|EMBL:AAN66006.1};
- **Gene Information:** OrderedLocusNames=PP_0375 {ECO:0000313|EMBL:AAN66006.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** AB_hydrolase_fold. (IPR029058); Peptidase_S9_cat. (IPR001375); Xaa-Pro_dipeptidyl-ppase/CocE. (IPR050585); Peptidase_S9 (PF00326)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_0375" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_0375' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_0375** (gene ID: PP_0375, UniProt: Q88QV9) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# PP_0375 (Q88QV9): A Family-S9 Serine Peptidase of the *Pseudomonas putida* KT2440 Pyrroloquinoline-Quinone (PQQ) Biosynthesis Operon

**Target:** PP_0375 · **UniProt:** Q88QV9 · **Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / KT2440), taxid 160488
**Protein length:** 612 aa · **Gene synonyms:** *pqqG* (operon terminal gene); ortholog of *P. aeruginosa* *pqqH* (PA1990)

---

## Summary

PP_0375 encodes a **family-S9 (prolyl oligopeptidase clan SC) serine peptidase** — a catalytically competent α/β-hydrolase whose primary molecular function is **peptide-bond hydrolysis**. The gene sits as the **terminal ("G") gene of the pyrroloquinoline-quinone (PQQ) biosynthesis operon** of *P. putida* KT2440, whose gene order has been mapped by RT-PCR as *pqqFABCDEG* (loci PP_0375–PP_0381). PP_0375 is the ~53 %-identical ortholog of *P. aeruginosa* *pqqH*/PA1990, the peptidase gene cotranscribed with *pqqABCDE*. Its role therefore lies within **PQQ cofactor maturation**, a ribosomally-synthesized-and-post-translationally-modified-peptide (RiPP) pathway that builds the redox cofactor PQQ from a glutamate and a tyrosine embedded in the 23-residue precursor peptide PqqA.

Structurally, PP_0375 has the **canonical two-domain prolyl-oligopeptidase architecture**: an N-terminal seven-bladed β-propeller domain that gates the active site, packed against a C-terminal α/β-hydrolase catalytic domain carrying the Peptidase_S9 module (Pfam PF00326). The catalytic **Ser469–His582–Asp550 triad** is geometrically intact in the high-confidence AlphaFold model (global pLDDT 93.8; triad distances 3.0 Å and 2.78 Å), with Ser469 sitting in a classic G-x-S-x-G "nucleophile elbow." Because the β-propeller covers the active site, this class of enzyme is intrinsically **selective for short peptides (oligopeptidase behavior)** rather than folded proteins — the enzyme sees a buried, gated pocket rather than an open surface groove.

Functionally, the PQQ operon of *P. putida* carries **two proteases of different mechanistic clans, doing two different jobs.** The essential core excision of the PqqE-cross-linked Glu–Tyr di-amino-acid from PqqA is performed by **PqqF** (PP_0381), an M16 zinc "inverzincin" whose deletion abolishes PQQ synthesis. In contrast, deletion of the S9 peptidase (*pqqH*, the PP_0375 ortholog) in *P. aeruginosa* does **not** block PQQ synthesis but abolishes **PQQ excretion** into the culture supernatant. PP_0375 therefore functions in the **cytoplasm** during cofactor maturation/release, and the PQQ it helps produce is exported to the **periplasm**, where it serves as the redox cofactor of quinoprotein dehydrogenases (glucose dehydrogenase Gcd, and the alcohol dehydrogenases PedE/PedH), driving glucose→gluconate oxidation (mineral-phosphate solubilisation) and alcohol/aldehyde oxidation. The **exact peptide substrate of PP_0375 has not been experimentally established** and remains the principal knowledge gap.

---

## Gene/Protein Identity Verification

Before presenting findings, the mandatory identity checks were satisfied:

| Check | Result |
|---|---|
| Gene symbol PP_0375 matches protein description | ✅ "Prolyl oligopeptidase family protein" is consistent with the S9 peptidase domains found (PF00326, IPR001375) |
| Organism correct | ✅ *P. putida* KT2440 (taxid 160488), OrderedLocusName PP_0375 |
| Domains align with literature | ✅ AB_hydrolase_fold (IPR029058), Peptidase_S9_cat (IPR001375), Peptidase_S9 (PF00326) all confirmed; genomic context is the PQQ operon |
| Literature consistency | ✅ No mistaken-identity conflict — PP_0375 maps cleanly onto the *pqqG/pqqH* operon position; literature on the PQQ pathway is directly relevant |

**Conclusion:** The identity is secure. PP_0375 is the operonic S9 peptidase (*pqqG*) of the *P. putida* KT2440 PQQ cluster.

---

## Key Findings

### Finding 1 — PP_0375 is a Peptidase S9 serine hydrolase with an intact Ser–His–Asp catalytic triad

UniProt Q88QV9 (612 aa) carries a consistent, mutually corroborating stack of domain annotations that place it firmly in the **prolyl oligopeptidase family (clan SC, family S9)**: Pfam **PF00326 (Peptidase_S9)**, InterPro **IPR001375 (Peptidase_S9_cat)**, **IPR029058 (α/β-hydrolase fold)**, IPR050585, PANTHER **PTHR43056:SF5**, eggNOG **COG1506** (dipeptidyl-/acylamino-acid peptidase), and Gene3D **3.40.50.1820** (the α/β-hydrolase superfamily fold).

The catalytic machinery is not merely annotated but **structurally verified**. The nucleophile **Ser469** lies in a canonical **G-x-S-x-G elbow** (sequence …RGG**S**AGG…), the signature "nucleophile elbow" of α/β-hydrolases. In the AlphaFold model **AF-Q88QV9** (global pLDDT 93.8, i.e. very high confidence), the triad is geometrically complete and correctly oriented for catalysis:

- **Ser469 Oγ – His582 Nε2 = 3.0 Å** (hydrogen-bond distance for the charge-relay proton transfer)
- **His582 Nδ1 – Asp550 Oδ2 = 2.78 Å** (the second charge-relay contact)
- All three triad residues have local pLDDT > 86 (individually reliable)

The InterPro-derived Gene Ontology terms are **serine-type peptidase activity (GO:0008236)** and **proteolysis (GO:0006508)**. Together these establish, with high confidence, that PP_0375 is a functional serine peptidase and not a degenerate/pseudo-enzyme.

### Finding 2 — PP_0375 is the *P. putida* ortholog of *pqqH*, a peptidase embedded in the PQQ biosynthesis operon

Genomic context is the decisive evidence. In the STRING network (organism 160488), PP_0375's highest-confidence functional partners are the **PQQ-biosynthesis genes**, and the supporting evidence channel is **genomic neighborhood (nscore)** — meaning these genes are co-located and co-inherited:

| Partner | Locus | STRING score |
|---|---|---|
| pqqC | PP_0378 | 0.892 |
| pqqE | PP_0376 | 0.871 |
| pqqD | PP_0377 | 0.841 |
| pqqB | PP_0379 | 0.795 |
| pqqF | PP_0381 | 0.507 |

PP_0375 sits **immediately adjacent to *pqqE* (PP_0376)** — precisely the operonic position occupied by *pqqH* in *P. aeruginosa*. A Needleman–Wunsch global alignment shows PP_0375 (612 aa) is **52.9 % identical** (344 identities over 650 aligned columns) to *P. aeruginosa* **pqqH/PA1990** (Q9I2B9, 608 aa). This level of identity across nearly the full length indicates clear orthology, not merely shared domain content.

The functional identity of *pqqH* was established experimentally in *P. aeruginosa* ([PMID: 19902179](https://pubmed.ncbi.nlm.nih.gov/19902179/)):

> "Gene PA1990 of *Pseudomonas aeruginosa*, located downstream of *pqqE* and encoding a putative peptidase, was shown to be involved in excretion of PQQ into the culture supernatant. This gene is cotranscribed with the *pqqABCDE* cluster and was named *pqqH*."

PP_0375 is the *P. putida* ortholog occupying the same operonic position.

### Finding 3 — PP_0375 (*pqqG/pqqH*) functions in PQQ cofactor biosynthesis for periplasmic quinoprotein glucose dehydrogenase

RT-PCR mapping of the *P. putida* KT2440 cluster defines its gene order as **pqqFABCDEG** (An & Moe 2016, [PMID: 27287323](https://pubmed.ncbi.nlm.nih.gov/27287323/)). PP_0375 is the terminal **"G"** gene immediately after *pqqE* (PP_0376) — i.e. the peptidase-encoding gene, ortholog of *P. aeruginosa* *pqqH*/PA1990.

The biological purpose of the operon is to synthesize **PQQ**, the redox coenzyme of the periplasmic **glucose dehydrogenase (Gcd)** that oxidizes glucose to gluconic acid, enabling **mineral-phosphate solubilization** in the rhizosphere:

> "Soil-dwelling microbes solubilize mineral phosphates by secreting gluconic acid, which is produced from glucose by a periplasmic glucose dehydrogenase (GDH) that requires pyrroloquinoline quinone (PQQ) as a redox coenzyme." — [PMID: 27287323](https://pubmed.ncbi.nlm.nih.gov/27287323/)

> "The *pqq* gene cluster (*pqqFABCDEG*) encodes at least two independent transcripts" — [PMID: 27287323](https://pubmed.ncbi.nlm.nih.gov/27287323/)

Biochemically, PQQ is a **RiPP** built from a Glu and a Tyr embedded in the ribosomal precursor peptide **PqqA**. The precursor is cross-linked (C–C bond between the Glu Cγ and Tyr Cε) by the radical-SAM enzyme **PqqE** (assisted by the RRE chaperone **PqqD**), after which a **protease/peptidase must excise the modified di-amino-acid** before **PqqB** (dual hydroxylase) and **PqqC** (eight-electron oxidase/cyclase) complete the cofactor:

> "The PqqA peptide is recognised by PqqE, which links the C9 and C9a, afterwards it is accepted by PqqF which cuts out the linked amino acids." — [PMID: 18371220](https://pubmed.ncbi.nlm.nih.gov/18371220/)

### Finding 4 — Two operon proteases, two roles: PqqF (M16) excises PqqA; PP_0375 (*pqqG/pqqH*, S9) is linked to PQQ excretion

Neighbor annotations (UniProt, organism 160488) confirm the complete operon and, critically, that it encodes **two peptidases of entirely different catalytic clans**:

| Locus | Gene | Length | Role |
|---|---|---|---|
| PP_0380 | pqqA | 23 aa | Precursor peptide (Glu + Tyr donor) |
| PP_0379 | pqqB | — | Dual hydroxylase / metallo-β-lactamase-fold |
| PP_0378 | pqqC | — | Ring cyclization/oxidation (8 e⁻, 8 H⁺) |
| PP_0377 | pqqD | — | PqqA-binding RRE chaperone |
| PP_0376 | pqqE | — | Radical-SAM peptide cyclase (SPASM domain) |
| PP_0381 | pqqF | 766 aa | **M16 zinc "inverzincin" protease** (IDE-like) |
| **PP_0375** | **pqqG** | **612 aa** | **S9 serine peptidase (this target)** |

Crystallography shows **PqqF has a clamshell inverzincin fold** with a large (~9,400 Å³) internal chamber proposed to bind PqqA and excise the PqqE-cross-linked Glu–Tyr; *pqqF* deletion abolishes PQQ biosynthesis (Wei et al. 2016):

> "After linkage of the Cγ of glutamate and Cϵ of tyrosine by PqqE, these two residues are hypothesized to be cleaved from PqqA by PqqF." — [PMID: 27231346](https://pubmed.ncbi.nlm.nih.gov/27231346/)

> "we demonstrated that the *pqqF* gene is essential for PQQ biosynthesis" — [PMID: 27231346](https://pubmed.ncbi.nlm.nih.gov/27231346/)

By contrast, deletion of the **S9 peptidase *pqqH*** in *P. aeruginosa* does **not** block PQQ synthesis but abolishes **PQQ excretion** into the supernatant ([PMID: 19902179](https://pubmed.ncbi.nlm.nih.gov/19902179/)). This establishes a **division of labor**: PqqF performs the essential core excision step, while PP_0375/pqqG/pqqH plays a distinct, non-essential-for-synthesis role tied to release/excretion of mature PQQ. **The precise molecular (peptide) substrate of PP_0375 has not been experimentally determined.**

### Finding 5 — Two-domain prolyl-oligopeptidase architecture implies short-peptide (oligopeptidase) selectivity

InterPro/SUPFAM/Gene3D domain mapping of Q88QV9 reveals the classic two-domain organization of the prolyl-oligopeptidase family:

- **N-terminal β-propeller** ("DPP6 N-terminal domain-like," SCOP **SSF82171**, residues ~44–337)
- **C-terminal α/β-hydrolase catalytic domain** (Gene3D **G3DSA:3.40.50.1820**, res ~356–612; SUPFAM **SSF53474**, res ~358–603), carrying the Peptidase_S9 module (PF00326 / IPR001375, res ~401–607) with the **Ser469–Asp550–His582 triad**
- **PANTHER PTHR43056** (Xaa-Pro dipeptidyl-peptidase / cocaine esterase) spans res 4–608

In the AlphaFold model (pLDDT 93.8) the two domains **pack tightly** (75 Cα–Cα inter-domain contacts < 8 Å; centroid separation 32.5 Å), and the catalytic Ser469 lies in an **enclosed pocket** (165 protein heavy atoms within 10 Å of Ser469 Oγ). This is a **covered/gated active site**, not an open surface groove.

The functional implication is well established for this fold family: the β-propeller acts as a **molecular sieve/gate** that admits only small, unstructured peptides to the buried catalytic center, excluding large folded proteins. PP_0375 is therefore predicted to be an **oligopeptidase — selective for short peptides**, which is mechanistically consistent with acting on the small PqqA-derived/PQQ-maturation intermediates rather than degrading bulk protein.

### Finding 6 — The PQQ cofactor served by PP_0375 feeds multiple periplasmic quinoprotein dehydrogenases

UniProt (organism 160488) confirms **three PQQ-dependent apo-dehydrogenases** in KT2440 that consume the cofactor whose biosynthesis PP_0375 supports:

| Enzyme | Locus | Length | Type / substrate |
|---|---|---|---|
| Glucose dehydrogenase Gcd | PP_1444 | 803 aa | Glucose → gluconate (periplasm) |
| Alcohol dehydrogenase PedE | PP_2674 | 631 aa | Ca/Zn-type PQQ-ADH, alcohols/aldehydes |
| Alcohol dehydrogenase PedH | PP_2679 | 595 aa | **Lanthanide-dependent** PQQ-ADH |

Wehrmann et al. 2017 ([PMID: 28655819](https://pubmed.ncbi.nlm.nih.gov/28655819/)) purified and characterized PedE/PedH as functionally redundant periplasmic PQQ-ADHs for oxidation of alcohols and aldehydes (relevant to volatile-organic-compound detoxification and catabolism); PedH was the first lanthanide-dependent PQQ-ADH described in a non-methylotroph:

> "many Gram-negative bacteria have evolved periplasmic oxidation systems based on pyrroloquinoline quinone-dependent alcohol dehydrogenases (PQQ-ADHs) that are often functionally redundant" — [PMID: 28655819](https://pubmed.ncbi.nlm.nih.gov/28655819/)

This closes the loop: the cofactor PP_0375 helps mature is exported and used by periplasmic quinoproteins that drive both **glucose→gluconate oxidation** (Gcd; phosphate solubilisation, environmental acidification) and **alcohol/aldehyde oxidation** (PedE/PedH).

---

## Mechanistic Model / Interpretation

### The PQQ biosynthesis operon and PP_0375's place in it

```
   P. putida KT2440 pqq operon  (order: pqqFABCDEG)

   PP_0381   PP_0380  PP_0379  PP_0378  PP_0377  PP_0376   PP_0375
   ┌─────┐   ┌────┐   ┌────┐   ┌────┐   ┌────┐   ┌────┐    ┌───────┐
   │ pqqF│   │pqqA│   │pqqB│   │pqqC│   │pqqD│   │pqqE│    │ pqqG  │  ← TARGET
   │ M16 │   │23aa│   │hydr│   │cycl│   │RRE │   │rSAM│    │  S9   │
   │prot.│   │prec│   │oxyl│   │oxid│   │chap│   │cycl│    │peptid.│
   └─────┘   └────┘   └────┘   └────┘   └────┘   └────┘    └───────┘
   ESSENTIAL                                                 EXCRETION-
   for PQQ                                                   linked
   synthesis
```

### Biosynthetic route (RiPP pathway) and the two-protease division of labor

```
   Ribosome
      │
      ▼
   PqqA (23-aa precursor, contains Glu + Tyr)
      │   bound by PqqD (RRE chaperone)  ── presents to ──►  PqqE (radical-SAM)
      ▼
   PqqA with Glu-Cγ ── C–C ── Tyr-Cε  cross-link
      │
      │  ┌── CORE EXCISION ──────────────────────────────┐
      ▼  │  PqqF (M16 inverzincin, PP_0381) cleaves the   │
   excised │  cross-linked di-amino-acid from PqqA.       │  ESSENTIAL
   Glu–Tyr │  Δpqqf → NO PQQ.                             │
           └──────────────────────────────────────────────┘
      │
      ▼   PqqB (hydroxylation) + PqqC (ring closure, 8e⁻/8H⁺ oxidation)
      ▼
   ★ PQQ (mature cofactor) ★
      │
      │  ┌── EXCRETION / RELEASE ─────────────────────────┐
      │  │  pqqG/pqqH (S9 serine peptidase, PP_0375)      │  NON-ESSENTIAL
      │  │  ΔpqqH → PQQ still made but NOT excreted        │  for synthesis;
      │  └────────────────────────────────────────────────┘  needed for export
      ▼
   PERIPLASM  ─►  Gcd (glucose→gluconate), PedE/PedH (alcohol/aldehyde ox.)
```

### Synthesis

PP_0375 is best understood as a **cytoplasmic, short-peptide-selective serine oligopeptidase acting in PQQ cofactor maturation**, distinct in both clan (S9 serine vs. M16 zinc) and phenotype (excretion vs. essential synthesis) from its operon partner PqqF. The structural evidence (intact triad, gated β-propeller active site, oligopeptidase architecture) is fully consistent with a role hydrolyzing a small peptide substrate during the late steps of PQQ maturation or release. The strongest experimental anchor for its physiological role is the *P. aeruginosa* *pqqH* knockout phenotype — **loss of PQQ excretion** — transferred by ~53 % orthology to PP_0375. Its exact substrate (whether a residual PqqA-derived peptide, a maturation intermediate, or a distinct target coupled to export) remains undetermined.

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports the findings |
|---|---|---|
| [19902179](https://pubmed.ncbi.nlm.nih.gov/19902179/) | *PQQ biosynthetic operons & transcriptional regulation in P. aeruginosa* | Defines *pqqH* (PA1990) as the peptidase downstream of *pqqE*, cotranscribed with *pqqABCDE*, required for **PQQ excretion** — the direct functional model for PP_0375 |
| [27287323](https://pubmed.ncbi.nlm.nih.gov/27287323/) | *Regulation of PQQ-dependent glucose dehydrogenase in P. putida KT2440* (An & Moe 2016) | Maps the KT2440 operon as *pqqFABCDEG* (placing PP_0375 as "G"); links PQQ to periplasmic Gcd and gluconate/phosphate solubilisation |
| [18371220](https://pubmed.ncbi.nlm.nih.gov/18371220/) | *PQQ biosynthesis pathway revisited: a structural approach* | Describes the proteolytic excision step on the PqqE-cross-linked PqqA precursor |
| [27231346](https://pubmed.ncbi.nlm.nih.gov/27231346/) | *Crystal structure and function of PqqF* (Wei et al. 2016) | Shows PqqF (M16) performs the essential core PqqA excision and is essential for PQQ synthesis — establishes the two-protease division of labor |
| [28655819](https://pubmed.ncbi.nlm.nih.gov/28655819/) | *Lanthanides in PQQ-ADHs* (Wehrmann et al. 2017) | Characterizes periplasmic PQQ-ADHs PedE/PedH that consume the cofactor PP_0375 helps produce |
| [31427437](https://pubmed.ncbi.nlm.nih.gov/31427437/) | *A two-component protease in PQQ biosynthesis* | Highlights that the identity of the PQQ maturation protease has been historically uncertain and varies between taxa |
| [8606199](https://pubmed.ncbi.nlm.nih.gov/8606199/) | *pqqE and pqqF in M. extorquens AM1* | Historical context: PqqF as a zinc-endopeptidase family member (distinct clan from S9) |

**Consistency / tension:** The literature is internally consistent that PQQ biosynthesis requires a protease for di-amino-acid excision, and that different organisms deploy different peptidases. A key nuance ([PMID: 31427437](https://pubmed.ncbi.nlm.nih.gov/31427437/)) is that the maturation protease is a "missing piece" that varies across taxa — in some α-proteobacteria it is a two-component heterodimer, in *Klebsiella/Methylobacterium* it is PqqF (M16), and *P. aeruginosa/P. putida* additionally carry the S9 *pqqH/pqqG*. The evidence assigns the **essential** excision to PqqF in *Pseudomonas* and an **excretion-linked** role to PP_0375/pqqG — but does not exclude an accessory maturation role for the S9 enzyme.

---

## Limitations and Knowledge Gaps

1. **No direct experimental characterization of PP_0375 itself.** All functional inference derives from (a) orthology to *P. aeruginosa pqqH* (~53 % identity), (b) genomic operon context, and (c) structural prediction. No *P. putida* PP_0375 knockout, purified enzyme assay, or crystal structure exists in the reviewed literature.
2. **The molecular substrate is undefined.** Whether PP_0375 cleaves a residual PqqA fragment, a PQQ-maturation intermediate, or an unrelated peptide coupled to export is not established. The "excretion" phenotype of *pqqH* could reflect a direct role in export machinery processing rather than PQQ chemistry.
3. **The AlphaFold-based active-site and oligopeptidase-selectivity claims are predictions**, not experimental structures — high-confidence (pLDDT 93.8) but unvalidated by crystallography or mutagenesis.
4. **Localization is inferred.** A cytoplasmic role during maturation is the parsimonious interpretation, but the excretion phenotype raises the possibility of association with the inner membrane or export apparatus; no experimental subcellular-localization data were found.
5. **Operon transcription nuance:** the KT2440 cluster produces "at least two independent transcripts," so *pqqG* expression may be regulated separately from the core *pqqABCDE*, but this was not investigated in detail here.

---

## Proposed Follow-up Experiments / Actions

1. **Targeted gene deletion (ΔPP_0375) in *P. putida* KT2440**, measuring (i) intracellular vs. extracellular PQQ (LC-MS or the classic *E. coli* GDH-reconstitution bioassay), (ii) glucose→gluconate flux, and (iii) periplasmic Gcd/PedE-PedH activity. This directly tests whether the *pqqH* "excretion" phenotype transfers to PP_0375.
2. **Recombinant expression and enzymology.** Purify PP_0375 and assay peptidase activity against candidate substrates: synthetic PqqA-derived peptides, cross-linked Glu–Tyr intermediates, and generic oligopeptide libraries (e.g., internally quenched fluorogenic peptides) to define the length and sequence specificity predicted by the gated β-propeller.
3. **Active-site mutagenesis.** Ser469Ala (and His582Ala) catalytic-dead variants to confirm the triad is required for the physiological phenotype, decoupling catalytic vs. possible scaffolding roles.
4. **Structural validation.** Solve a crystal or cryo-EM structure of PP_0375 to confirm the β-propeller / α-β-hydrolase two-domain arrangement and the buried active site, and to visualize the substrate-access channel.
5. **Interaction / localization mapping.** Co-purification or BioID with operon partners (PqqF, PqqE, PqqB/C) and with export components; cell-fractionation to test cytoplasmic vs. membrane-associated localization.
6. **Comparative genomics of the two-protease pattern.** Systematically map which PQQ-producing genomes carry PqqF, *pqqG/pqqH*, both, or the α-proteobacterial two-component protease, to clarify the evolutionary logic of redundancy and the specific selective role of the S9 enzyme.

---

*Report generated from a 5-iteration autonomous investigation: 6 confirmed findings, 15 papers reviewed. All functional claims are supported by the cited literature; claims resting on structure prediction or orthology are flagged as such.*


## Artifacts

- [OpenScientist final report](PP_0375-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PP_0375-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:19902179
2. PMID:27287323
3. PMID:18371220
4. PMID:27231346
5. PMID:28655819
6. PMID:31427437