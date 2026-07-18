---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-18T13:30:36.420249'
end_time: '2026-07-18T13:54:59.545357'
duration_seconds: 1463.13
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_4452
  gene_symbol: PP_4452
  uniprot_accession: Q88EL0
  protein_description: 'RecName: Full=2-dehydropantoate 2-reductase {ECO:0000256|ARBA:ARBA00019465};
    EC=1.1.1.169 {ECO:0000256|ARBA:ARBA00013014}; AltName: Full=Ketopantoate reductase
    {ECO:0000256|ARBA:ARBA00032024};'
  gene_info: OrderedLocusNames=PP_4452 {ECO:0000313|EMBL:AAN70027.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: 6-PGluconate_DH-like_C_sf. (IPR008927); 6PGD_dom2. (IPR013328);
    KPR_N. (IPR013332); NAD(P)-bd_dom_sf. (IPR036291); Opine/Lysopine_DH. (IPR051729)
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
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PP_4452-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PP_4452-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88EL0
- **Protein Description:** RecName: Full=2-dehydropantoate 2-reductase {ECO:0000256|ARBA:ARBA00019465}; EC=1.1.1.169 {ECO:0000256|ARBA:ARBA00013014}; AltName: Full=Ketopantoate reductase {ECO:0000256|ARBA:ARBA00032024};
- **Gene Information:** OrderedLocusNames=PP_4452 {ECO:0000313|EMBL:AAN70027.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** 6-PGluconate_DH-like_C_sf. (IPR008927); 6PGD_dom2. (IPR013328); KPR_N. (IPR013332); NAD(P)-bd_dom_sf. (IPR036291); Opine/Lysopine_DH. (IPR051729)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_4452" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_4452' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_4452** (gene ID: PP_4452, UniProt: Q88EL0) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of PP_4452 (Q88EL0) in *Pseudomonas putida* KT2440

**Target:** Gene PP_4452 / UniProt **Q88EL0** / *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / NCIMB 11950 / **KT2440**), organism code PSEPK.
**Protein:** 359 aa, soluble cytoplasmic NAD(P)-dependent oxidoreductase.
**Report date:** 2026-07-18

---

## 1. Summary (Answer to the Research Question)

PP_4452 encodes a **cytoplasmic NAD(P)-dependent oxidoreductase of the opine/lysopine dehydrogenase family** (an "opine dehydrogenase," EC 1.5.1.28-type; KEGG ortholog **K04940**). Its most likely primary reaction is the reversible NAD(P)(H)-dependent interconversion between an **"opine" (an N-(carboxyalkyl)-amino acid / secondary-amine conjugate) and its constituent amino acid + 2‑oxo (keto) acid** — i.e., reductive condensation in the anabolic direction, or oxidative cleavage in the catabolic direction. The gene lies at the head of a **complete opine-utilization operon** (opine ABC importer + a two-subunit octopine oxidase OoxAB + a LysR regulator), which strongly indicates a **catabolic role in the uptake and breakdown of opine growth substrates** in this soil/rhizosphere bacterium. The enzyme works in the **cytoplasm**.

> **Important annotation caveat.** The UniProt name "2‑dehydropantoate 2‑reductase / ketopantoate reductase (EC 1.1.1.169)" attached to Q88EL0 is an **automated (ARBA) electronic prediction, not an experimental or manually curated assignment, and is almost certainly a mis-annotation.** It arises because ketopantoate reductase (KPR/PanE) and opine dehydrogenases share the same two-domain protein fold. Family-level classifiers, KEGG orthology, genomic context, and the presence of three *bona fide* ketopantoate reductases elsewhere in the genome all indicate PP_4452 is **not** the pantothenate-pathway KPR. This report treats PP_4452 as an opine dehydrogenase and explains the evidence in full.

**No experimental study of PP_4452 itself exists**; the functional assignment is based on rigorous bioinformatic and evolutionary inference plus the biochemistry of characterized homologs.

---

## 2. Gene/Protein Identity Verification

| Attribute | Value | Source |
|---|---|---|
| UniProt accession | Q88EL0 | UniProtKB |
| Locus tag | PP_4452 (GenBank AAN70027) | EMBL AAN70027.1 |
| Organism | *P. putida* KT2440 (PSEPK) | UniProt |
| Length / location | 359 aa; genome complement 5,051,434–5,052,513 | KEGG ppu:PP_4452 |
| UniProt RecName (automated) | 2-dehydropantoate 2-reductase, EC 1.1.1.169 | ARBA (ECO:0000256) |
| KEGG ortholog | **K04940 opine dehydrogenase (EC 1.5.1.28)** | KEGG |
| GenBank product | "NAD/NADP octopine/nopaline dehydrogenase family protein" | KEGG/GenBank |
| eggNOG / OrthoDB | COG0240 / 6135265at2 | UniProt xrefs |

The locus tag, organism, and accession all match the target. **The disagreement is purely at the level of assigned function** (KPR vs. opine dehydrogenase), which Section 3 resolves. The gene is genuine and correctly identified; the literature below concerns the protein *family*, since no paper addresses PP_4452 directly.

---

## 3. Resolving the Function: Opine Dehydrogenase, Not Ketopantoate Reductase

Ketopantoate reductase (KPR) and opine dehydrogenases are **structural homologs**: both are built from an N‑terminal Rossmann NAD(P)(H)-binding domain plus a C‑terminal α‑helical domain, and KPR is a member of the 6‑phosphogluconate‑dehydrogenase C‑terminal‑domain‑like superfamily [PMID 11724562]. This shared fold is exactly what causes automated pipelines to cross-label members of one family as the other. Five independent lines of evidence show PP_4452 belongs to the **opine dehydrogenase** side of this fold:

1. **Family-level classification (strongest signal).** InterPro assigns Q88EL0 to **family IPR051729 "Opine/Lysopine Dehydrogenase,"** and PANTHER independently assigns **family PTHR38015 "Opine/Lysopine Dehydrogenase."** In InterPro, family membership is the functional classification; the ketopantoate-reductase match (IPR013332 "KPR N-terminal domain," Pfam PF02558 PanE/ApbA) is only a **domain-level** hit reflecting the shared Rossmann fold.
2. **Diagnostic domain and structural signatures.** Pfam also matches **PF02317 "NAD/NADP octopine/nopaline dehydrogenase, α-helical domain,"** and the CATH homologous superfamily for the C-terminal domain is **G3DSA:1.10.1040.10 "N-(1-D-carboxylethyl)-L-norvaline dehydrogenase"** (CENDH, a characterized bacterial opine dehydrogenase).
3. **KEGG orthology.** PP_4452 is assigned **K04940 opine dehydrogenase (EC 1.5.1.28)** — not the KPR ortholog K00077.
4. **The real KPRs are elsewhere.** *P. putida* KT2440's genuine pantothenate-pathway ketopantoate reductases are **PP_1351, PP_2325, and PP_2998**, all annotated K00077 / EC 1.1.1.169. PP_4452 is therefore redundant to and distinct from the housekeeping KPR — it is not needed for vitamin B5/CoA synthesis.
5. **Protein length.** PP_4452 is **359 aa**, matching the opine dehydrogenase family (e.g., *Arthrobacter* sp. 1C opine DH, UniProt Q44297 = 359 aa; *Pecten maximus* octopine DH ≈ 399 aa) and clearly longer than single-domain KPR (*E. coli* PanE = 303 aa).
6. **Quantitative pairwise identity** (global BLOSUM62 alignment, this work). PP_4452 is **most similar to a characterized bacterial opine dehydrogenase** — *Arthrobacter* sp. 1C opine DH (Q44297): **29.6% identity / 49.3% similarity over a near-full-length 351-residue alignment** — and to *P. aeruginosa* pseudopaline synthase CntM (Q9HUX5): 24.6% / 42.4% over 354 aa. By contrast it aligns to *E. coli* ketopantoate reductase (P0A9J4) at only **22.7% identity over 295 aa**, meaning ~64 residues of PP_4452 have **no KPR counterpart** — only the shared N-terminal Rossmann region aligns. Thus PP_4452 matches opine dehydrogenases along essentially its entire length but matches KPR only in the common cofactor-binding subdomain.

**Conclusion:** The evidence overwhelmingly favors an **opine/lysopine dehydrogenase**. The KPR RecName should be regarded as a low-confidence electronic artifact.

---

## 4. Primary Function and Reaction Chemistry

### 4.1 Reaction class
Opine dehydrogenases (OpDHs) catalyze the **NAD(P)(H)-dependent reductive condensation of an amino acid and a 2‑oxo acid into a secondary-amine "opine,"** and the reverse oxidative cleavage. The archetype is octopine dehydrogenase (OcDH) from the scallop *Pecten maximus*, which "catalyzes the reductive condensation of L‑arginine and pyruvate to octopine … [and] oxidizes glycolytically born NADH to NAD⁺" [PMID 18599075]. Generic scheme:

> amino acid + 2‑oxo acid + NAD(P)H + H⁺ ⇌ opine (N‑(carboxyalkyl)amino acid) + NAD(P)⁺ + H₂O

The hydride is delivered from/accepted by the nicotinamide cofactor bound in the N‑terminal Rossmann domain; the reaction creates (or breaks) a C–N bond and generates a new chiral center.

### 4.2 Substrate specificity
The **exact opine substrate of PP_4452 has not been experimentally determined.** In characterized OpDHs, substrate identity is set by **size selection in the active site** — a "molecular ruler" that combines electrostatic recognition of the amino-acid α-carboxylate/side chain with steric gating of the 2‑oxo-acid moiety [PMID 18599075]. Family members differ widely in their amino-acid partner (arginine → octopine/nopaline; ornithine/lysine → various; norvaline → CENDH product; glutamate → staphylopine/pseudopaline-type). Based on family and genomic context, PP_4452 is predicted to act on an **opine-type N-(carboxyalkyl)amino acid**; defining the precise pair requires enzymology.

### 4.3 Cofactor
NAD(P)(H)-dependent (the family uses NADH or NADPH depending on the member). The intact N-terminal glycine-rich dinucleotide-binding motif is present near the N-terminus of PP_4452 (…**GIIGAGGIG**…, residues ~10–18), confirming a functional Rossmann cofactor site.

---

## 5. Structural Basis

- **Fold:** two-domain architecture — N‑terminal **Rossmann NAD(P)(H)-binding domain** (CATH 3.40.50.720 / SSF51735) + C‑terminal **α-helical substrate/dimerization domain** (6‑phosphogluconate-dehydrogenase-like; SSF48179, CATH 1.10.1040.10). This is the canonical opine-dehydrogenase/KPR superfamily fold [PMID 11724562].
- **Catalytic logic (from homologs):** catalysis occurs in the interdomain cleft; cofactor binds in the Rossmann lobe and the amino-acid/2-oxo-acid substrates bind in the cleft, with domain closure bringing catalytic residues into register. In the homologous KPR this closure repositions a catalytic Lys/Glu pair over the substrate [PMID 17229734, PMID 11123955]; opine dehydrogenases use an analogous interdomain active site with substrate-recognition residues that impose the "molecular ruler" specificity [PMID 18599075].
- An **AlphaFold model (AlphaFoldDB Q88EL0)** is available and is expected to reproduce this bilobed fold, offering a route to computational substrate docking.

---

## 6. Subcellular Localization

PP_4452 is a **soluble cytoplasmic protein**. A Kyte–Doolittle hydropathy scan (19-residue window, this work) gives a maximum local hydropathy of only **1.36**, below the ~1.6–1.9 threshold for a membrane-spanning helix, so there is **no predicted transmembrane segment**; the N-terminus begins directly with the glycine-rich Rossmann motif (MEMQSYKVGIIGAGGIG…) rather than a cleavable signal peptide. NAD(P)-dependent dehydrogenases of this family act in the cytosol. This is consistent with its pathway role: the substrate (an opine) is first **imported across the inner membrane by the co-encoded ABC transporter** (membrane-bound permeases + periplasmic/lipoprotein substrate-binding protein), after which PP_4452 processes it **intracellularly**.

---

## 7. Pathway Context: A Complete Opine-Utilization Operon

PP_4452 is the first gene of a contiguous, co-oriented (minus-strand) gene cluster spanning ~5.051–5.061 Mb that encodes a full opine uptake-and-catabolism system:

| Locus | KEGG KO | Annotated product | Role |
|---|---|---|---|
| **PP_4452** | K04940 | opine dehydrogenase (EC 1.5.1.28) | **NAD(P)-dependent opine dehydrogenase (this gene)** |
| PP_4453 | K02031 | ABC transporter ATP-binding | Importer — ATPase |
| PP_4454 | K02034 | "Opine ABC transporter" permease | Importer — permease |
| PP_4455 | K02033 | ABC permease | Importer — permease |
| PP_4458 | K02035 | ABC substrate-binding protein | Importer — solute-binding subunit |
| PP_4456 | K24954 | **octopine oxidase subunit A (OoxA)** | Flavin/Fe-S opine-catabolic oxidase |
| PP_4457 | K24955 | **octopine oxidase subunit B (OoxB)** | Flavin/Fe-S opine-catabolic oxidase |
| PP_4460 | — | LysR-family transcriptional regulator | Substrate-responsive induction |
| PP_4461 | — | Major facilitator superfamily transporter | Auxiliary transport |
| PP_4462 | — | putative keto-acid (HMG/oxaloacetate) aldolase | Downstream product catabolism |

Bacterial opine dehydrogenases function in **opine catabolism** — for example, "Opines, such as nopaline and octopine … are specifically catabolized by opine dehydrogenase (OpnDH)" [PMID 40581604]. The classical multi-subunit OpnDH/opine oxidase "contain[s] FAD, FMN, and 2 iron-sulfur clusters as cofactors" [PMID 40581604], matching the two-subunit **OoxAB (PP_4456/PP_4457)** in this operon. Thus the cluster contains **two complementary opine-degrading activities** — the NAD(P)-linked opine dehydrogenase (PP_4452) and the flavin/Fe-S opine oxidase (OoxAB) — alongside a dedicated importer and a LysR regulator that likely induces the operon when an opine is available. The most parsimonious interpretation is that this locus lets *P. putida* **import and consume opine (N-carboxyalkyl-amino-acid) compounds as carbon and nitrogen sources**, with PP_4452 cleaving the opine into an amino acid + 2‑oxo acid that feed central metabolism.

### Distinction from the metallophore branch
The same superfamily includes **biosynthetic** "opine" dehydrogenases that build nicotianamine-like metallophores (staphylopine, pseudopaline, yersinopine) used by pathogens to counter host nutritional immunity [PMID 31300464]. Those enzymes (CntM-type) sit in *cnt* operons together with a **nicotianamine synthase (CntL)** and a dedicated metallophore exporter — none of which are present at the PP_4452 locus. This further supports a **catabolic**, nutrient-utilization role rather than metallophore biosynthesis.

---

## 8. Evidence Summary

| Claim | Evidence type | Strength |
|---|---|---|
| Belongs to opine/lysopine dehydrogenase family (not KPR) | Bioinformatic: InterPro & PANTHER family assignment, CATH/Pfam signatures, KEGG orthology | Strong |
| Housekeeping KPRs are separate genes (PP_1351/2325/2998) | Comparative genomics (KEGG K00077) | Strong |
| Catalyzes NAD(P)-dependent opine ⇌ amino acid + 2-oxo acid | Homology to characterized OpDHs [PMID 18599075] | Moderate–strong (by inference) |
| Functions in opine catabolism/uptake | Genomic context: complete importer + OoxAB oxidase + LysR [PMID 40581604] | Strong (contextual) |
| Cytoplasmic localization | Sequence features (no signal/TM) + family biochemistry | Strong |
| Exact opine substrate | — | **Unknown (experimental gap)** |
| Direct enzymology of PP_4452 | — | **None available** |

---

## 9. Supported and Refuted Hypotheses

- **REFUTED (as the primary function): Ketopantoate reductase / 2-dehydropantoate 2-reductase (EC 1.1.1.169).** The UniProt ARBA name is a fold-based electronic artifact; family classifiers, KEGG orthology, and the existence of three dedicated KPRs elsewhere argue against it. (A residual, unproven possibility that the enzyme retains weak promiscuous 2-oxo-acid reductase activity cannot be formally excluded without assays, but it is not the physiological role.)
- **SUPPORTED: NAD(P)-dependent opine/lysopine dehydrogenase (EC 1.5.1.28-type, K04940)** acting in the cytoplasm.
- **SUPPORTED: Catabolic role in an opine-utilization operon** (uptake + degradation of an opine growth substrate), based on the co-encoded ABC importer, OoxAB opine oxidase, and LysR regulator.
- **NOT SUPPORTED: Metallophore (staphylopine/pseudopaline-type) biosynthesis** — the diagnostic nicotianamine synthase (CntL) and metallophore exporter are absent.

---

## 10. Limitations and Future Directions

- **No direct biochemistry** exists for PP_4452; conclusions rest on bioinformatics, homology, and genomic context. High-throughput/automated database annotations conflict, and the UniProt RecName is misleading.
- **The precise opine substrate and cofactor preference (NADH vs NADPH) are undetermined.** Priority experiments: (i) recombinant expression and an activity screen against candidate opines and amino-acid/2‑oxo-acid pairs (arginine+pyruvate, ornithine/lysine/glutamate + pyruvate/α-ketoglutarate); (ii) steady-state kinetics and cofactor specificity; (iii) AlphaFold-guided substrate docking and active-site "molecular-ruler" analysis; (iv) growth phenotyping of a PP_4452 (and operon) deletion on candidate opines as sole C/N source; (v) transcriptional induction tests to confirm LysR (PP_4460) control.
- Confirming which of PP_1351/PP_2325/PP_2998 is the functional pantothenate-pathway KPR would complete the vitamin B5 picture but is outside this gene's scope.

---

## Key References
- Matak-Vinković et al. (2001) *Biochemistry* — E. coli ketopantoate reductase structure; shared 6PGD-like superfamily fold. **PMID 11724562**
- Zheng & Blanchard (2000) — KPR catalytic residues (Lys/Glu). **PMID 11123955**
- Ciulli et al. (2007) — KPR ternary complex, domain closure. **PMID 17229734**
- Smits et al. (2008) *J. Biol. Chem.* — octopine dehydrogenase structure; reaction and "molecular ruler" specificity. **PMID 18599075**
- Laffont et al. (2019) — opine-type metallophores (staphylopine/pseudopaline/yersinopine). **PMID 31300464**
- Watanabe et al. (2025) — bacterial opine catabolism; monomeric flavin opine dehydrogenase and multi-subunit OpnDH cofactors. **PMID 40581604**
- Database sources: UniProt Q88EL0; KEGG ppu:PP_4452 and neighbors; InterPro/PANTHER/CATH/Pfam classifications.


## Artifacts

- [OpenScientist final report](PP_4452-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PP_4452-deep-research-openscientist_artifacts/final_report.pdf)