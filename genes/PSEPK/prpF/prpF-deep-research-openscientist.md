---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-23T13:30:29.288445'
end_time: '2026-07-23T13:42:07.726197'
duration_seconds: 698.44
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: prpF
  gene_symbol: prpF
  uniprot_accession: Q88KF3
  protein_description: 'SubName: Full=Aconitate isomerase {ECO:0000313|EMBL:AAN67950.1};'
  gene_info: Name=prpF {ECO:0000313|EMBL:AAN67950.1}; OrderedLocusNames=PP_2337 {ECO:0000313|EMBL:AAN67950.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the PrpF family.
  protein_domains: PrpF. (IPR012709); PrpF-like. (IPR007400); PrpF (PF04303)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 1
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: prpF-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: prpF-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88KF3
- **Protein Description:** SubName: Full=Aconitate isomerase {ECO:0000313|EMBL:AAN67950.1};
- **Gene Information:** Name=prpF {ECO:0000313|EMBL:AAN67950.1}; OrderedLocusNames=PP_2337 {ECO:0000313|EMBL:AAN67950.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the PrpF family.
- **Key Domains:** PrpF. (IPR012709); PrpF-like. (IPR007400); PrpF (PF04303)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "prpF" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'prpF' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **prpF** (gene ID: prpF, UniProt: Q88KF3) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: PrpF (Q88KF3 / PP_2337)

**Gene:** prpF · **Locus:** PP_2337 · **UniProt:** Q88KF3 (Q88KF3_PSEPK)
**Organism:** *Pseudomonas putida* KT2440 (ATCC 47054 / DSM 6125 / NCIMB 11950)
**Family/domains:** PrpF family; Pfam PF04303 (PrpF); InterPro IPR012709 (PrpF), IPR007400 (PrpF-like)
**Length:** 396 aa · **KEGG ortholog:** K09788 (2-methylaconitate isomerase, EC 5.3.3.-)

---

## 1. Summary (Answer to the Research Question)

**PrpF (PP_2337) is a cofactor-independent 2-methylaconitate (cis–trans) isomerase that functions in the cytoplasm as an essential accessory enzyme of the AcnD-dependent branch of the 2-methylcitric acid cycle (2-MCC), the route by which *Pseudomonas putida* catabolizes propionate.** Its specific reaction is the geometric isomerization of the 2-methyl-*trans*-aconitate produced by the Fe/S dehydratase AcnD (PP_2336) into 2-methyl-*cis*-aconitate, the only isomer that the housekeeping aconitase (AcnB) can hydrate to 2-methyl-D-isocitrate. Without PrpF the AcnD dehydration step is a metabolic dead end. This assignment is transferred with high confidence from the experimentally characterized, 83.9%-identical *Shewanella oneidensis* ortholog and is reinforced by the enzyme's location in a complete methylcitrate operon and by perfect conservation of the catalytic residues Lys73 and Cys107.

---

## 2. Gene Identity Verification

The target was rigorously confirmed as the correct protein:

- **Symbol match:** UniProt lists gene name `prpF`, ordered locus `PP_2337`; the submitted protein name "Aconitate isomerase" is consistent with the characterized PrpF function.
- **Family match:** Pfam PF04303 and InterPro IPR012709/IPR007400 all define the **PrpF family**, matching the target's stated domains exactly.
- **Orthology match:** Global Needleman–Wunsch alignment against the reviewed Swiss-Prot entry **Q8EJW4 (PRPF_SHEON, "2-methyl-aconitate isomerase," PE=1)** gives **83.9% identity (328/391 positions)**. The literature I found describes exactly this protein/family — there is **no gene-symbol ambiguity**.
- **Organism match:** UniProt proteome UP000000556, KEGG `ppu:PP_2337`, chromosome-encoded — all *P. putida* KT2440.

The functional evidence below is therefore drawn from direct experimental studies on close PrpF orthologs (*S. oneidensis*, *Salmonella enterica* complementation system) combined with organism-specific bioinformatic/genomic-context evidence for *P. putida*.

---

## 3. Primary Function: The Reaction Catalyzed

### 3.1 Metabolic problem PrpF solves
Bacteria degrade propionate (and odd-chain fatty-acid–derived propionyl-CoA) via the **2-methylcitric acid cycle**: propionyl-CoA + oxaloacetate → 2-methylcitrate (PrpC) → **2-methyl-*cis*-aconitate** (a dehydration) → 2-methyl-D-isocitrate (aconitase) → pyruvate + succinate (PrpB). The dehydration of 2-methylcitrate is carried out by one of two alternative enzyme systems:

- **PrpD** — a cofactor-less 2-methylcitrate dehydratase (EC 4.2.1.79) that directly yields **2-methyl-*cis*-aconitate**, the aconitase substrate. Organisms using PrpD do **not** need PrpF.
- **AcnD** — an Fe/S, aconitase-like 2-methylcitrate dehydratase (EC 4.2.1.117) that yields a **different geometric isomer** of 2-methylaconitate (2-methyl-*trans*-aconitate), which aconitase **cannot** use. Organisms using AcnD **require PrpF** (Grimek & Escalante-Semerena, *J. Bacteriol.* 2004, **PMID 14702315**).

### 3.2 PrpF's catalytic role
PrpF is the isomerase that reconciles the AcnD product with aconitase:

> "the SoPrpF protein isomerizes the product of the AcnD reaction into the PrpD product (2-MCA], a known substrate of the housekeeping aconitase (AcnB]" — Rocco *et al.*, *J. Bacteriol.* 2017 (**PMID 29145506**).

Thus PrpF catalyzes:

**2-methyl-*trans*-aconitate ⇌ 2-methyl-*cis*-aconitate** (EC 5.3.3.-, KEGG K09788)

Mechanistically it is a **non-PLP, cofactor-less cis–trans isomerase**: a base-catalyzed proton abstraction coupled to rotation about the C2–C3 bond of 2-methylaconitate (Garvey *et al.*, *Protein Sci.* 2007, **PMID 17567742**). On the unmethylated analog PrpF interconverts **trans-aconitate ⇌ cis-aconitate** in vitro, the assay used to demonstrate its activity:

> "Results from in vitro studies show that PrpF isomerizes trans-aconitate to cis-aconitate" (PMID 17567742).

Careful in-vitro/NMR work refined the model: AcnD dehydrates 2-methylcitrate to an isomer of 2-methyl-*cis*-aconitate (proposed to be 4-methylaconitate / 2-methyl-*trans*-aconitate), which is not an aconitase substrate; PrpF converts it to the productive isomer (PMID 29145506; PMID 14702315).

### 3.3 Substrate specificity
The physiological substrate is the **C7 branched tricarboxylate 2-methylaconitate** (both geometric isomers). PrpF also acts on the non-methylated **aconitate** (citrate-derived) as a model substrate, consistent with a tricarboxylic-acid isomerase active site. There is **no aconitase (hydratase) activity** — PrpF only isomerizes; it does not add/remove water:

> "No aconitase-like activity was found for PrpF" (PMID 14702315).

### 3.4 Catalytic residues (structural/bioinformatic evidence)
The *S. oneidensis* PrpF crystal structure (2.0 Å, with bound trans-aconitate; and 1.22 Å K73E variant with trans-aconitate/malonate) shows a **two-domain, pseudo-2-fold fold of the PLP-independent isomerase superfamily** — closely resembling diaminopimelate epimerase and proline racemase (PMID 17567742; PMID 29145506). Catalysis uses a pair of general acid/base residues; **Lys73** and **Cys107** are essential:

> "SoPrpF variants with substitutions of residues K73 or C107 failed to support growth with propionate" (PMID 29145506).

In my alignment, **both Lys73 and Cys107 are perfectly conserved in the *P. putida* ortholog** (identical alignment columns), providing strong bioinformatic support that Q88KF3 uses the same catalytic machinery and reaction.

---

## 4. Biological Process & Pathway Context

PrpF operates within the **2-methylcitric acid cycle for propionate degradation**. In *P. putida* KT2440 the entire pathway is encoded in a single chromosomal operon around PP_2337 (KEGG genome annotation):

| Locus | Gene | Enzyme | EC / KO |
|-------|------|--------|---------|
| PP_2333 | prpR | GntR-family transcriptional regulator | — |
| PP_2334 | prpB | 2-methylisocitrate lyase | 4.1.3.30 / K03417 |
| PP_2335 | prpC | 2-methylcitrate synthase | 2.3.3.5 / K01659 |
| PP_2336 | **acnD** | 2-methylcitrate dehydratase (2-methyl-*trans*-aconitate forming), Fe/S | 4.2.1.117 / K20455 |
| **PP_2337** | **prpF** | **2-methylaconitate isomerase** | **5.3.3.- / K09788** |
| PP_2338 | prpD | 2-methylcitrate dehydratase (cofactor-less) | 4.2.1.79 / K01720 |
| PP_2339 | acnB | aconitate hydratase 2 / 2-methylisocitrate dehydratase | 4.2.1.3 / 4.2.1.99 / K01682 |

PrpF (PP_2337) is **immediately adjacent to and co-operonic with acnD (PP_2336)** — the exact genomic pairing seen where the AcnD/PrpF partnership was experimentally proven. This is decisive functional-context evidence. The presence of the enzyme in this operon means PrpF is co-regulated with the propionate-catabolic machinery (2-MCC operons are typically induced by propionate/2-methylcitrate via the PrpR regulator).

**Pathway flux with PrpF:**
propionyl-CoA → (PrpC) 2-methylcitrate → (AcnD) 2-methyl-*trans*-aconitate → **(PrpF) 2-methyl-*cis*-aconitate** → (AcnB aconitase) 2-methyl-D-isocitrate → (PrpB) pyruvate + succinate.

The physiological importance of this pathway in *Pseudomonas* is underscored by studies showing that disrupting 2-MCC enzymes (e.g., prpB) redirects propionate/propionyl-CoA into polyhydroxyalkanoate (PHA) synthesis, altering odd-chain monomer content (PMID 37995793) — evidence that the 2-MCC (of which PrpF is part) is the principal propionate-oxidation route in these bacteria.

---

## 5. Subcellular Localization

PrpF is a **soluble cytoplasmic enzyme**. Evidence: (i) all 2-MCC reactions occur in the cytosol where propionyl-CoA and TCA-cycle intermediates reside; (ii) the protein has no predicted signal peptide, no transmembrane segment, and no membrane/secretion annotation (UniProt keywords are only "Isomerase" and "Reference proteome"); (iii) the characterized orthologs were purified and assayed as soluble proteins from cytoplasmic extracts (PMID 18295882, PMID 14702315). It carries out its function in the cytoplasm, in direct metabolic coupling with the cytoplasmic dehydratase AcnD and aconitase AcnB.

---

## 6. Evidence Summary

| Claim | Evidence type | Source |
|-------|---------------|--------|
| PrpF = 2-methylaconitate cis–trans isomerase | Direct in vitro enzymology (ortholog) | PMID 14702315, 17567742, 29145506 |
| Isomerizes AcnD product → aconitase substrate | In vitro + NMR (ortholog) | PMID 29145506 |
| Required with AcnD for propionate growth | In vivo complementation (*S. enterica*) | PMID 14702315 |
| Cofactor-less; PLP-independent isomerase fold | X-ray crystallography (ortholog) | PMID 17567742, 29145506 |
| Catalytic residues Lys73, Cys107 | Mutagenesis + structure; conserved in Q88KF3 | PMID 29145506 + this analysis (83.9% id; K73/C107 conserved) |
| Membership in 2-MCC operon with acnD in *P. putida* | Genomic context (KEGG) | KEGG ppu:PP_2333–2339 |
| Cytoplasmic localization | Sequence features + biochemical purification | UniProt Q88KF3; PMID 18295882 |
| 2-MCC is main propionate route in *Pseudomonas* | Mutant physiology | PMID 37995793 |

---

## 7. Supported and Refuted Hypotheses

- **Supported:** PrpF is a 2-methylaconitate isomerase acting in the AcnD-dependent 2-methylcitrate cycle (converts 2-methyl-*trans*- to 2-methyl-*cis*-aconitate). ✔
- **Supported:** PrpF is a cytoplasmic, cofactor-independent (non-PLP, non-metal) enzyme with catalytic Lys73/Cys107. ✔
- **Supported:** In *P. putida* KT2440, prpF is genomically embedded in a complete methylcitrate operon adjacent to acnD. ✔
- **Refuted:** PrpF is itself an aconitase/hydratase — no hydratase activity was detected; it is strictly an isomerase. ✘
- **Refuted (superseded model):** PrpF's role is merely to protect the AcnD Fe/S cluster from oxidative damage (an early hypothesis in PMID 14702315). Later enzymology (PMID 29145506) established the direct isomerase mechanism as the primary function.

---

## 8. Limitations & Future Directions

- Direct enzymatic characterization exists for the *S. oneidensis* ortholog, not for *P. putida* Q88KF3 specifically; the assignment relies on very high sequence identity (83.9%), conserved catalytic residues, and conserved operon context — strong but inferential.
- The precise identity of the AcnD product isomer (2-methyl-*trans*-aconitate vs. 4-methylaconitate) remains a point of mechanistic refinement in the literature.
- *P. putida* KT2440 encodes **both** PrpF/AcnD and a PrpD homolog (PP_2338); the relative in-vivo flux through each branch and any conditional regulation is not established and would benefit from targeted deletion + metabolomic studies.
- No experimental subcellular-localization or structural study of the *P. putida* protein has been reported; an AlphaFold model plus a *P. putida* prpF knockout growth phenotype on propionate would close the remaining gaps.


## Artifacts

- [OpenScientist final report](prpF-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](prpF-deep-research-openscientist_artifacts/final_report.pdf)