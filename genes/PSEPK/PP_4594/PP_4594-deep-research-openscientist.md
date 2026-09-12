---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-11T16:19:41.806440'
end_time: '2026-07-11T17:07:02.816135'
duration_seconds: 2841.01
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_4594
  gene_symbol: PP_4594
  uniprot_accession: Q88E72
  protein_description: 'SubName: Full=Cystathionine gamma-synthase {ECO:0000313|EMBL:AAN70167.1};'
  gene_info: OrderedLocusNames=PP_4594 {ECO:0000313|EMBL:AAN70167.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the trans-sulfuration enzymes family.
  protein_domains: Cys/Met-Metab_PyrdxlP-dep_enz. (IPR000277); PyrdxlP-dep_Trfase.
    (IPR015424); PyrdxlP-dep_Trfase_major. (IPR015421); PyrdxlP-dep_Trfase_small.
    (IPR015422); Cys_Met_Meta_PP (PF01053)
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
citation_count: 5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PP_4594-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PP_4594-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88E72
- **Protein Description:** SubName: Full=Cystathionine gamma-synthase {ECO:0000313|EMBL:AAN70167.1};
- **Gene Information:** OrderedLocusNames=PP_4594 {ECO:0000313|EMBL:AAN70167.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the trans-sulfuration enzymes family.
- **Key Domains:** Cys/Met-Metab_PyrdxlP-dep_enz. (IPR000277); PyrdxlP-dep_Trfase. (IPR015424); PyrdxlP-dep_Trfase_major. (IPR015421); PyrdxlP-dep_Trfase_small. (IPR015422); Cys_Met_Meta_PP (PF01053)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_4594" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_4594' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_4594** (gene ID: PP_4594, UniProt: Q88E72) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: PP_4594 (Q88E72), *Pseudomonas putida* KT2440

**Gene:** PP_4594 (OrderedLocusNames PP_4594)
**UniProt:** Q88E72
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440) — proteome code PSEPK
**Submitted name:** Cystathionine gamma-synthase
**Protein family:** Trans-sulfuration enzymes family (Cys/Met metabolism, PLP-dependent, fold-type I "γ-family")

---

## Summary

PP_4594 encodes a **393-residue, cytoplasmic, pyridoxal-5′-phosphate (PLP)-dependent enzyme** belonging to the **fold-type I Cys/Met-metabolism "γ-family"** of trans-sulfuration enzymes (Pfam **PF01053**, Cys_Met_Meta_PP; InterPro **IPR000277**). Its sequence carries a **fully intact catalytic apparatus** — the Schiff-base lysine (Lys205) that forms the internal aldimine with PLP, and the conserved aspartate (Asp180) that anchors the PLP pyridinium nitrogen — so the protein is very likely a **catalytically active PLP enzyme**, not a pseudoenzyme. Enzymes of this family carry out **α,γ-elimination and γ-replacement reactions on sulfur-containing amino acids** (cystathionine, homocysteine, methionine and their O-substituted derivatives) and share a common three-domain, homotetrameric fold.

Assigning the **precise reaction** catalyzed by PP_4594 is the central challenge of this annotation, because two credible calls exist and no direct enzymology has ever been performed on the PP_4594 protein itself. The **original 2002 genome annotation and PIRSF/CDD signatures name it "cystathionine γ-synthase"**, whereas **KEGG assigns it the orthology K01758 = cystathionine γ-lyase (EC 4.4.1.1)**. The weight of convergent bioinformatic evidence favors the **γ-lyase-type function**: PP_4594 falls into the **same PANTHER subfamily (PTHR11808:SF15)** as the experimentally characterized *P. aeruginosa* cystathionine γ-lyase PA0400, its **closest characterized homolog at ~47% identity**, and in a pairwise-identity/phylogenetic comparison it clusters with the **γ-elimination clade** (human CTH 42%, *P. putida* methionine γ-lyase 42%) and is clearly separated from the β-lyase clade (E. coli MetC 28%, KT2440 MetC/PP_4348 24%). Importantly, PP_4594 is **distinct from KT2440's dedicated forward methionine-biosynthetic genes** metB (PP_0659) and metC (PP_4348), and it sits immediately adjacent to a **cysteine-sensing Lrp/AsnC-family transcriptional activator (PP_4595)** — a genomic arrangement consistent with a cysteine-inducible, accessory catabolic role rather than a housekeeping biosynthetic one.

The most defensible functional statement is therefore: **PP_4594 is a cytoplasmic PLP-dependent γ-family trans-sulfuration enzyme, most probably acting as a cystathionine γ-lyase (γ-elimination on cystathionine/homocysteine-type substrates, potentially producing H₂S), likely functioning as an accessory, cysteine-inducible enzyme in sulfur-amino-acid metabolism.** This assignment rests on orthology and sequence/structure inference; the exact substrate specificity and reaction direction remain to be confirmed by direct biochemical characterization. A significant caveat is that Vermeij & Kertesz (1999) could **not detect cystathionine γ-lyase activity in *P. putida***, which tempers over-confident acceptance of the K01758 label.

---

## Key Findings

### Finding 1 — PP_4594 is a cytoplasmic PLP-dependent trans-sulfuration (Cys/Met γ-family) enzyme

UniProt entry Q88E72 describes a **393-amino-acid protein** whose cofactor is **pyridoxal 5′-phosphate (PLP)** and whose family membership is annotated as "Belongs to the trans-sulfuration enzymes family." This placement is supported by a dense, mutually consistent set of domain signatures:

| Signature | Database | Meaning |
|---|---|---|
| PF01053 (Cys_Met_Meta_PP) | Pfam | Cys/Met metabolism PLP-dependent enzyme |
| IPR000277 (Cys/Met-Metab_PyrdxlP-dep_enz) | InterPro | Cys/Met metabolism, PLP-dependent |
| IPR015421 / IPR015422 / IPR015424 | InterPro | PLP-dependent transferase, fold-type I (major/small/overall) |
| SSF53383 | SUPFAM | PLP-dependent transferases superfamily |
| COG0626 | eggNOG | Cystathionine β-lyase / γ-synthase family |

Gene Ontology terms assigned to the entry are **pyridoxal phosphate binding (GO:0030170)**, **cytoplasm (GO:0005737)**, and **transsulfuration (GO:0019346)**. All of these localization/function terms are currently **IEA (inferred from electronic annotation)**, meaning they are computational rather than experimentally verified for this specific protein. Nonetheless, the convergence of independent domain databases makes the **fold assignment (fold-type I PLP transferase) and the broad functional category (Cys/Met γ-family trans-sulfuration enzyme) highly secure**. The predicted cytoplasmic localization is fully consistent with the biology of this enzyme family, whose members are soluble cytosolic proteins with no signal peptides or membrane-spanning segments.

### Finding 2 — PP_4594 is annotated as cystathionine γ-lyase (K01758 / EC 4.4.1.1) and is distinct from KT2440's dedicated forward-transsulfuration genes

There is a genuine **annotation conflict** at the heart of this gene. KEGG assigns `ppu:PP_4594` to ortholog **K01758 (cystathionine γ-lyase, EC 4.4.1.1)**, whereas the original 2002 genome submission and the UniProt "SubName" call it **cystathionine γ-synthase**. Resolving this required situating PP_4594 relative to the other Cys/Met enzymes encoded in the KT2440 genome and relative to characterized reference enzymes.

In KT2440 the canonical forward methionine-biosynthetic genes are **separate loci**:
- **metB (cystathionine γ-synthase, K01739) = PP_0659**
- **metC (cystathionine β-lyase, K01760) = PP_4348**
- **methionine γ-lyase (K01761) = PP_1308**

Because these dedicated biosynthetic functions are already accounted for elsewhere in the genome, PP_4594 is **not** the housekeeping γ-synthase or β-lyase of methionine biosynthesis; it is an additional, paralogous γ-family enzyme.

An independent Needleman–Wunsch pairwise-identity analysis places PP_4594 firmly in the **γ-elimination clade**:

| Reference enzyme | % identity to PP_4594 | Clade |
|---|---|---|
| Human CGL/CTH (cystathionine γ-lyase) | 42.4% | γ-lyase |
| *P. putida* methionine γ-lyase (PpMGL) | 41.7% | γ-family |
| Yeast CGL/CYS3 | 40.5% | γ-lyase |
| *E. coli* MetB (γ-synthase) | 37.6% | γ-synthase |
| KT2440 MetB / PP_0659 | 37.4% | γ-synthase |
| *E. coli* MetC (β-lyase) | 28.4% | β-lyase |
| KT2440 MetC / PP_4348 (β-lyase) | 23.7% | β-lyase |

PP_4594 is **most similar to γ-lyases and clearly separated from the β-lyase clade**, supporting a γ-elimination (γ-lyase / γ-family) rather than a β-elimination function. Its genomic neighbor, **PP_4595, is a Lrp/AsnC-family cysteine-sensing transcriptional activator (K05800)** — a regulatory context that strongly suggests PP_4594 expression is **cysteine-responsive**.

### Finding 3 — Physiological context: *P. putida* uses direct sulfhydrylation for methionine synthesis; transsulfuration enzymes are low-level and cysteine-inducible

The physiology of sulfur metabolism in *P. putida* was directly measured by **Vermeij & Kertesz (1999)** [PMID: 10482527](https://pubmed.ncbi.nlm.nih.gov/10482527/). Their findings frame the likely role of PP_4594:

- *P. putida* (and *P. aeruginosa*) **"used direct sulfhydrylation of O-succinylhomoserine for the synthesis of methionine"** and also contained substantial O-acetylserine sulfhydrylase (cysteine synthase) activity. This means the **main methionine-biosynthetic route bypasses the transsulfuration enzymes**, casting them as accessory rather than essential.
- **"The enzymes of the transsulfuration pathway (cystathionine gamma-synthase and cystathionine beta-lyase) were expressed at low levels in both pseudomonads but were strongly upregulated during growth with cysteine as the sole sulfur source."** This matches the presence of the cysteine-sensing Lrp/AsnC regulator (PP_4595) beside PP_4594 and supports a **cysteine-inducible** expression pattern.
- Critically, **"P. putida S-313 also grew well with methionine as the sulfur source, but no cystathionine gamma-lyase, the key enzyme of the reverse transsulfuration pathway, was found in this species"** — instead, methionine was degraded via methionine γ-lyase. This is important **counter-evidence** that cautions against uncritically accepting the KEGG K01758 (cystathionine γ-lyase) call for PP_4594 as its principal in vivo activity.

Structural context reinforces the shared fold. Motoshima et al. (2000) [PMID: 10965031](https://pubmed.ncbi.nlm.nih.gov/10965031/) showed that *P. putida* methionine γ-lyase adopts a fold in which "the spatial fold of subunits, with three functionally distinct domains and their quarternary arrangement, is **similar to those of L-cystathionine beta-lyase and L-cystathionine gamma-synthase from Escherichia coli**," confirming the common fold-type I, three-domain architecture across the entire γ-family to which PP_4594 belongs.

### Finding 4 — PP_4594 has a fully intact fold-type I PLP catalytic apparatus (Schiff-base Lys205, PLP-anchoring Asp180)

Motif mapping of the 393-residue Q88E72 sequence identified **all signature catalytic elements** of the fold-type I Cys/Met γ-family, indicating the protein is a **catalytically competent enzyme**, not a degenerate pseudoenzyme:

| Catalytic element | Residues / motif | Role |
|---|---|---|
| Schiff-base lysine | **Lys205** in H-S-A-S-**K**-Y (201–206) | Forms internal aldimine with PLP; central to catalysis |
| Conserved aspartate | **Asp180** in **D**-N-T-F (180–183) | Hydrogen-bonds/orients the PLP pyridinium nitrogen |
| PLP phosphate-binding loop | E-S-P-T-N-P (151–156) | Binds the PLP phosphate group |
| N-terminal substrate/cofactor loop | G-N-P-T-R (57–61) | Substrate and cofactor positioning |

Additional structural classifiers agree: **CDD cd00614 (CGS_like)**, **PIRSF001434 (Cystathionine gamma-synthase)**, and **CATH 3.40.640.10 / 3.90.1150.10** (aspartate aminotransferase-like two-domain PLP fold). This is the canonical architecture shared by cystathionine γ-synthase, cystathionine γ-lyase, and methionine γ-lyase (Motoshima 2000). The presence of a complete, unmutated catalytic set means the enzyme **retains the machinery to perform PLP-dependent α,γ-eliminations/γ-replacements** on appropriate sulfur-amino-acid substrates.

### Finding 5 — PP_4594 co-classifies with, and is the closest characterized homolog of, the *P. aeruginosa* cystathionine γ-lyase PA0400 — favoring a γ-lyase over a γ-synthase call

The single most informative comparison for narrowing PP_4594's function is to **PA0400 (Q9I6A0) of *P. aeruginosa* PAO1**, annotated as "probable cystathionine γ-lyase" and the subject of a 2024 structure/specificity study, Pedretti et al. [PMID: 38654065](https://pubmed.ncbi.nlm.nih.gov/38654065/). PP_4594 and PA0400:

- are assigned to the **same PANTHER subfamily, PTHR11808:SF15**, and
- share **47.4% pairwise identity** — **higher than to any other characterized reference** (human CTH 42.4%, PpMGL 41.7%, E. coli MetB 37.6%, E. coli MetC β-lyase 28.4%).

Because PA0400 is a *characterized* enzyme placed in **bacterial defense against oxidative stress and antibiotics via H₂S production**, and because PP_4594 is its nearest characterized relative in the same fine-grained subfamily, the balance of evidence favors a **cystathionine γ-lyase-type (γ-elimination, potentially H₂S-generating) function** for PP_4594. The Pedretti et al. study frames this defense role explicitly: "The escalating drug resistance among microorganisms underscores the urgent need for innovative therapeutic strategies and a comprehensive understanding of bacteria's defense mechanisms against oxidative stress and antibiotics." KEGG's independent assignment of K01758 to PP_4594 is consistent with the γ-lyase call.

The **counter-evidence for a synthase call** should be stated plainly: the original 2002 genome name, the PIRSF001434 label ("Cystathionine gamma-synthase"), and the CDD cd00614 name ("CGS_like") all describe the broader clade as γ-synthase-like, and PP_4594's identity to true γ-synthases (E. coli MetB 37.6%; KT2440 metB/PP_0659 37.4%) is only modestly lower than its identity to γ-lyases. The γ-synthase vs. γ-lyase distinction within this fold can hinge on a small number of active-site residues, so **the assignment is a probabilistic lean, not a certainty.**

---

## Mechanistic Model / Interpretation

### The enzyme family and its chemistry

PP_4594 belongs to the **fold-type I (aspartate-aminotransferase-like) PLP enzyme superfamily**, specifically the **Cys/Met-metabolism "γ-family"** (trans-sulfuration enzymes). Members are typically **homotetramers** in which each active site is built from residues of two adjacent subunits, with a bound PLP cofactor tethered as an internal aldimine (Schiff base) to the catalytic lysine (here **Lys205**). Substrate amino acids displace this lysine to form an external aldimine, after which PLP stabilizes carbanionic intermediates enabling elimination or replacement chemistry at the Cβ or Cγ position.

```
        Cys/Met γ-family reactions on sulfur amino acids
        (fold-type I PLP enzymes; PP_4594 belongs here)

  γ-synthase (metB):  O-succinyl-L-homoserine + L-cysteine
                          → L-cystathionine + succinate       (γ-replacement)

  β-lyase   (metC):  L-cystathionine + H2O
                          → L-homocysteine + pyruvate + NH3   (β-elimination)

  γ-lyase   (CTH):   L-cystathionine + H2O
                          → L-cysteine + 2-oxobutanoate + NH3 (γ-elimination)
                       (side reactions can release H2S from Cys/homocysteine)

  Met γ-lyase(MGL): L-methionine + H2O
                          → methanethiol + 2-oxobutanoate + NH3 (α,γ-elimination)
```

All four activities are performed by structurally near-identical enzymes; **substrate specificity and reaction type are dictated by a small set of active-site residues**, which is precisely why sequence-only annotation is ambiguous here. Structural studies of *P. putida* MGL (e.g., [PMID: 28329912](https://pubmed.ncbi.nlm.nih.gov/28329912/), [PMID: 34953671](https://pubmed.ncbi.nlm.nih.gov/34953671/)) demonstrate that single active-site substitutions can switch substrate preference between methionine and homocysteine, underscoring the limits of homology-only calls.

### Where PP_4594 sits

```
   KT2440 sulfur-amino-acid enzyme inventory
   ─────────────────────────────────────────────
   PP_0659  metB   cystathionine γ-synthase   K01739   (forward Met biosynth)
   PP_4348  metC   cystathionine β-lyase      K01760   (forward Met biosynth)
   PP_1308  ---    methionine γ-lyase         K01761   (Met catabolism)
   PP_4594  ???    "γ-synthase"/γ-lyase       K01758   ← THIS GENE
   PP_4595  ---    Lrp/AsnC Cys-sensing activator  K05800  (neighbor/regulator)

   Pairwise identity places PP_4594 in the γ-LYASE clade,
   closest to P. aeruginosa PA0400 (47%) — a characterized γ-lyase.
```

The presence of dedicated metB and metC elsewhere means PP_4594 is a **surplus γ-family paralog**. Combined with (a) its clustering with γ-lyases, (b) its ~47% identity to the characterized *P. aeruginosa* γ-lyase PA0400 in the same PANTHER subfamily, and (c) its cysteine-sensing regulatory neighbor PP_4595, the coherent model is:

> **PP_4594 is a cytoplasmic, cysteine-inducible, accessory PLP-dependent γ-family enzyme most likely performing a cystathionine γ-lyase-type γ-elimination, contributing to sulfur-amino-acid interconversion/catabolism (with possible H₂S generation), rather than serving as the primary methionine-biosynthetic γ-synthase.**

The one loose thread is Vermeij & Kertesz's failure to detect classical *reverse-transsulfuration* cystathionine γ-lyase activity in *P. putida*. This can be reconciled if PP_4594's true in vivo activity is a related γ-elimination (e.g., on homocysteine or a non-canonical substrate) that was not assayed, or if the enzyme is expressed only under conditions not tested in that study — but it does mean the **K01758 = "cystathionine γ-lyase" label should be treated as a best-available hypothesis, not an established fact.**

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports / challenges the annotation |
|---|---|---|
| [10482527](https://pubmed.ncbi.nlm.nih.gov/10482527/) | *Pathways of assimilative sulfur metabolism in P. putida* | **Supports & tempers.** Establishes direct sulfhydrylation as the main Met route (transsulfuration is accessory); shows transsulfuration enzymes are cysteine-inducible (matches PP_4595 neighbor). **But** reports cystathionine γ-lyase activity was *not detected* in *P. putida* — key caveat against the K01758 call. |
| [10965031](https://pubmed.ncbi.nlm.nih.gov/10965031/) | *Crystal structure of PLP-dependent L-methionine γ-lyase from P. putida* | **Supports fold.** Confirms shared fold-type I, three-domain architecture across γ-family enzymes (β-lyase, γ-synthase, γ-lyase, MGL), validating PP_4594's structural class. |
| [38654065](https://pubmed.ncbi.nlm.nih.gov/38654065/) | *Catalytic specificity and crystal structure of cystathionine γ-lyase from P. aeruginosa* | **Supports γ-lyase call.** PA0400 is PP_4594's closest characterized homolog (47%, same PANTHER SF15); places bacterial γ-lyase in oxidative-stress/antibiotic defense via H₂S, suggesting an analogous role for PP_4594. |
| [8586629](https://pubmed.ncbi.nlm.nih.gov/8586629/) | *Structural analysis of the L-methionine γ-lyase gene from P. putida* | Documents the extensive homology of MGL with cystathionine γ-lyase and γ-synthase — the same α,γ-elimination/γ-replacement PLP enzyme group PP_4594 belongs to. |
| [26913973](https://pubmed.ncbi.nlm.nih.gov/26913973/) | *Revisited genome of P. putida KT2440* | Provides the re-annotation framework for KT2440 gene functions used to distinguish PP_4594 from metB/metC. |
| [28329912](https://pubmed.ncbi.nlm.nih.gov/28329912/), [34953671](https://pubmed.ncbi.nlm.nih.gov/34953671/) | *Mechanistic / mutant studies of P. putida MGL* | Illustrate how single active-site substitutions switch substrate preference (Met↔homocysteine) in this fold — explaining why γ-synthase vs. γ-lyase cannot be settled by sequence alone. |
| [39427081](https://pubmed.ncbi.nlm.nih.gov/39427081/) | *Reverse transsulfuration pathway and colitis* | Defines cystathionine γ-lyase (CTH) chemistry (cystathionine→cysteine) — the reaction KEGG proposes for PP_4594. |

**Confidence in fold/family assignment: very high.** Multiple independent domain databases (Pfam, InterPro, SUPFAM, CDD, CATH, eggNOG) concur, and all catalytic residues are intact.

**Confidence in precise reaction (γ-lyase vs. γ-synthase): moderate.** The lean is toward γ-lyase (KEGG K01758; closest to characterized PA0400; γ-clade clustering), but the original genome/PIRSF/CDD names say γ-synthase, and no direct assay exists.

---

## Limitations and Knowledge Gaps

1. **No direct enzymology on the PP_4594 protein.** Every functional statement here is inferred from orthology, domain signatures, and sequence/structure comparison. The substrate specificity (cystathionine? homocysteine? O-substituted homoserine?), reaction direction (elimination vs. replacement), and kinetic parameters have never been measured for Q88E72.
2. **Annotation conflict is unresolved.** KEGG (γ-lyase, K01758) vs. original genome/PIRSF/CDD (γ-synthase). Within this fold, specificity can hinge on a few active-site residues, so bioinformatics cannot fully settle it.
3. **All GO localization/function terms are IEA (computational).** No experimental localization data confirm the predicted cytoplasmic site (though it is biologically near-certain for a soluble PLP enzyme with no targeting signals).
4. **Contradictory physiology.** Vermeij & Kertesz did not detect cystathionine γ-lyase activity in *P. putida*, in tension with the K01758 assignment — possibly a condition- or substrate-dependent gap rather than a true contradiction.
5. **Regulatory linkage is inferred, not proven.** PP_4595 is a cysteine-sensing Lrp/AsnC activator by annotation; direct evidence that it controls PP_4594 (operon structure, ChIP, promoter mapping) has not been established.
6. **H₂S-generating / defense role is by analogy only** to *P. aeruginosa* PA0400 and has not been tested in *P. putida*.

---

## Proposed Follow-up Experiments / Actions

1. **Heterologous expression and enzymatic assay.** Clone PP_4594, purify the His-tagged protein, confirm PLP loading (absorbance at ~420 nm), and assay candidate reactions: cystathionine γ-elimination (→ cysteine + 2-oxobutanoate + NH₃), cystathionine γ-synthesis (O-succinyl/acetyl-homoserine + cysteine), methionine/homocysteine γ-elimination, and H₂S release (lead-acetate or fluorescent probe). Report kcat/Km for each substrate to settle the γ-lyase-vs-γ-synthase question definitively.
2. **Crystal structure or AlphaFold-model active-site comparison.** Solve/model the structure and superpose the active site onto PA0400 (γ-lyase) vs. E. coli MetB (γ-synthase) to identify the specificity-determining residues and predict substrate scope.
3. **Transcriptional regulation test.** Fuse the PP_4594 promoter to a reporter and measure induction under cysteine vs. sulfate vs. methionine as sole sulfur source; delete PP_4595 to test whether it is the activating regulator, confirming or refuting the cysteine-inducible model.
4. **Phenotypic characterization of a knockout.** Construct a ΔPP_4594 mutant and test growth on various sulfur sources, sensitivity to oxidative stress/antibiotics (the PA0400 defense hypothesis), and endogenous H₂S levels.
5. **Metabolomic tracing.** Use ³⁴S- or ¹³C-labeled cysteine/cystathionine to trace flux through PP_4594 in vivo, distinguishing forward biosynthetic from catabolic/reverse-transsulfuration roles.

---

## Conclusion

PP_4594 (Q88E72) of *Pseudomonas putida* KT2440 is a **cytoplasmic, 393-residue, PLP-dependent fold-type I enzyme of the Cys/Met-metabolism γ-family (trans-sulfuration family)** with an intact catalytic apparatus (Schiff-base Lys205, PLP-anchoring Asp180). Convergent bioinformatic evidence — KEGG ortholog K01758, shared PANTHER subfamily PTHR11808:SF15 with the characterized *P. aeruginosa* cystathionine γ-lyase PA0400 (its closest characterized homolog at ~47% identity), and clustering with the γ-elimination clade — indicates its **most probable activity is a cystathionine γ-lyase-type γ-elimination (EC 4.4.1.1)** acting on cystathionine/homocysteine-type sulfur amino acids in the cytosol, possibly generating H₂S. It is **distinct from KT2440's dedicated forward methionine-biosynthetic genes metB (PP_0659) and metC (PP_4348)** and is most consistent with an **accessory, cysteine-inducible catabolic role** (adjacent to the cysteine-sensing Lrp regulator PP_4595). This assignment is inference-based: the original genome/PIRSF annotation calls it "cystathionine γ-synthase," no direct enzymology has been performed on the protein, and *P. putida* was reported to lack detectable cystathionine γ-lyase activity — so the exact substrate and reaction direction await experimental confirmation.


## Artifacts

- [OpenScientist final report](PP_4594-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PP_4594-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:10482527
2. PMID:10965031
3. PMID:38654065
4. PMID:28329912
5. PMID:34953671