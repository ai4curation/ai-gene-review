---
provider: openscientist
model: openscientist-autonomous
cached: true
start_time: '2026-08-31T19:58:27.950546'
end_time: '2026-08-31T19:58:27.984322'
duration_seconds: 0.03
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: pyrE
  gene_symbol: pyrE
  uniprot_accession: Q88C92
  protein_description: 'RecName: Full=Orotate phosphoribosyltransferase {ECO:0000255|HAMAP-Rule:MF_01208};
    Short=OPRT {ECO:0000255|HAMAP-Rule:MF_01208}; Short=OPRTase {ECO:0000255|HAMAP-Rule:MF_01208};
    EC=2.4.2.10 {ECO:0000255|HAMAP-Rule:MF_01208};'
  gene_info: Name=pyrE {ECO:0000255|HAMAP-Rule:MF_01208}; OrderedLocusNames=PP_5291;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the purine/pyrimidine phosphoribosyltransferase
  protein_domains: OPRT. (IPR023031); Or_phspho_trans_dom. (IPR004467); PRTase-like.
    (IPR029057); PRTase_dom. (IPR000836); Pribosyltran (PF00156)
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
citation_count: 14
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: pyrE-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: pyrE-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88C92
- **Protein Description:** RecName: Full=Orotate phosphoribosyltransferase {ECO:0000255|HAMAP-Rule:MF_01208}; Short=OPRT {ECO:0000255|HAMAP-Rule:MF_01208}; Short=OPRTase {ECO:0000255|HAMAP-Rule:MF_01208}; EC=2.4.2.10 {ECO:0000255|HAMAP-Rule:MF_01208};
- **Gene Information:** Name=pyrE {ECO:0000255|HAMAP-Rule:MF_01208}; OrderedLocusNames=PP_5291;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the purine/pyrimidine phosphoribosyltransferase
- **Key Domains:** OPRT. (IPR023031); Or_phspho_trans_dom. (IPR004467); PRTase-like. (IPR029057); PRTase_dom. (IPR000836); Pribosyltran (PF00156)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "pyrE" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'pyrE' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **pyrE** (gene ID: pyrE, UniProt: Q88C92) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *pyrE* (Q88C92) — Orotate Phosphoribosyltransferase from *Pseudomonas putida* KT2440

## Summary

The gene **pyrE** (ordered locus **PP_5291**; UniProt **Q88C92**) of *Pseudomonas putida* strain KT2440 (ATCC 47054 / DSM 6125 / NCIMB 11950) encodes **orotate phosphoribosyltransferase (OPRTase; EC 2.4.2.10)**, a soluble, cytoplasmic, Mg²⁺-dependent enzyme of the de novo pyrimidine nucleotide biosynthesis pathway. Its identity is unambiguous: the gene symbol, the OrderedLocusName, the HAMAP rule MF_01208, the Pfam PRTase domain (PF00156), and the InterPro orotate-phosphoribosyltransferase signatures (IPR004467, IPR023031) all converge on OPRTase, and the target sequence (213 residues) is 66.7% identical to the experimentally characterized *Escherichia coli* PyrE. This report therefore proceeds with high confidence that Q88C92 is a bona fide OPRTase; there is no evidence of gene-symbol ambiguity for this protein.

The enzyme catalyzes the **fifth (penultimate) step of de novo pyrimidine biosynthesis**: the reversible, Mg²⁺-dependent transfer of a phosphoribosyl group from 5-phospho-α-D-ribose-1-diphosphate (PRPP) to orotate, producing **orotidine 5′-monophosphate (OMP)** and pyrophosphate (Rhea:10380). OMP is subsequently decarboxylated by OMP decarboxylase (PyrF) to yield uridine 5′-monophosphate (UMP), the founding pyrimidine nucleotide. Structurally, OPRTase is an obligate **homodimer** built on a Rossmann-fold nucleotide-binding core capped by a base-binding "hood" domain, with a **domain-swapped, flexible catalytic loop** that descends over the active site of the partner subunit. Catalysis proceeds through an ordered Bi-Bi mechanism and a late, associative transition state, with conserved catalytic-loop lysines contributing dramatically to transition-state stabilization.

In *P. putida* specifically, OPRTase activity is regulated at the transcriptional level, responding to carbon source (catabolite repression by succinate) and to pyrimidine-pathway intermediates/end-products (repression by orotic acid). Loss of OPRTase function causes strict pyrimidine (uracil) auxotrophy, confirming that this enzyme is essential for de novo pyrimidine supply whenever salvage is insufficient. The enzyme also activates orotate analogues such as 5-fluoroorotate, a property relevant to its role as an antimicrobial/antiparasitic drug target in other organisms. Collectively, the evidence supports a precise functional annotation: **Q88C92 is a cytoplasmic Mg²⁺-dependent orotate phosphoribosyltransferase that commits orotate to the pyrimidine nucleotide pool via OMP formation.**

---

## Gene/Protein Identity Verification

Before presenting findings, the mandatory identity checks required by the research brief were completed and **all passed**:

| Verification criterion | Result |
|---|---|
| Gene symbol *pyrE* matches protein description (OPRT) | ✔ Universal bacterial annotation: *pyrE* = orotate phosphoribosyltransferase |
| Organism correct (*P. putida* KT2440) | ✔ Target sequence Q88C92 retrieved from UniProt, 213 aa, PP_5291 |
| Protein family/domains align with literature | ✔ Type I PRTase, PF00156, PRPP-binding vicinal-aspartate motif present |
| Literature consistency (no different gene with same symbol) | ✔ No ambiguity; *pyrE* is consistently OPRTase across all bacteria |

The gene symbol *pyrE* is **not ambiguous**. Across the bacterial world *pyrE* consistently denotes orotate phosphoribosyltransferase. Sequence analysis (Findings F005, F008) directly confirmed that the actual *P. putida* KT2440 product carries the diagnostic OPRTase motifs and is highly similar to characterized orthologs. The research therefore proceeded on solid ground.

---

## Key Findings

### F001 — *pyrE* encodes orotate phosphoribosyltransferase (EC 2.4.2.10), catalyzing OMP formation

The core function of Q88C92 is to catalyze the reaction:

> **orotate + 5-phospho-α-D-ribose-1-diphosphate (PRPP) ⇌ orotidine 5′-monophosphate (OMP) + pyrophosphate (PPi)**

This is a **reversible, Mg²⁺-dependent phosphoribosyl-transfer** reaction and constitutes the fifth step of the de novo pyrimidine biosynthetic pathway. The reaction is directly documented in the primary literature: OPRTase "catalyzes the reversible phosphoribosyl transfer from 5′-phospho-α-D-ribose 1′-diphosphate (PRPP) to orotic acid (OA), forming pyrophosphate and orotidine 5′-monophosphate (OMP)" ([PMID: 22075667](https://pubmed.ncbi.nlm.nih.gov/22075667/)). A second independent source frames the physiological importance: "Orotate phosphoribosyltransferases (OPRT) catalyze the formation of orotidine 5′-monophosphate (OMP) from alpha-D-phosphoribosylpyrophosphate (PRPP) and orotate, an essential step in the de novo biosynthesis of pyrimidines" ([PMID: 19292447](https://pubmed.ncbi.nlm.nih.gov/19292447/)).

The identity assignment rests on multiple orthogonal lines of evidence: the EC number 2.4.2.10 (a glycosyltransferase transferring pentosyl groups), the HAMAP family rule MF_01208, the Pfam PRTase domain PF00156, and the universal bacterial convention that *pyrE* = OPRTase. The product OMP is the immediate substrate for OMP decarboxylase (PyrF), which produces UMP.

### F002 — Homodimeric Type I PRTase with a Rossmann-fold core, a base-binding hood, and a domain-swapped catalytic loop

OPRTase belongs to the **Type I phosphoribosyltransferase** structural class. The enzyme is an **obligate homodimer** built on an α/β Rossmann nucleotide-binding fold, topped by a base-enclosing "hood" domain that recognizes the orotate ring, and equipped with a solvent-exposed, **domain-swapped catalytic loop**. Direct structural description: "The homodimeric enzyme has a Rossman α/β core topped by a base-enclosing 'hood' domain and a flexible domain-swapped catalytic loop" ([PMID: 23315339](https://pubmed.ncbi.nlm.nih.gov/23315339/)).

A critical architectural feature is that the catalytic loop of one subunit reaches over and completes the active site of the *other* subunit: "one of the two identical solvent-exposed loops can descend to cover the active site of the adjacent subunit of the dimeric enzyme" ([PMID: 9890909](https://pubmed.ncbi.nlm.nih.gov/9890909/)). This makes the functional active site an **intersubunit, shared entity** — the dimer is not merely two independent monomers but a cooperatively assembled catalytic unit.

The loop is conformationally dynamic. In the apo (unliganded) enzyme it is highly flexible/disordered — "the surface loop is highly flexible in the unliganded enzyme" ([PMID: 9890909](https://pubmed.ncbi.nlm.nih.gov/9890909/)) — and it undergoes a **disorder-to-order transition** upon substrate binding: "a general compacting of the core as well as movement of the hood and a major disorder-to-order transition of the loop occur upon binding of ligands MgPRPP and orotate" ([PMID: 23315339](https://pubmed.ncbi.nlm.nih.gov/23315339/)). This induced-fit closure sequesters the substrates from solvent and positions catalytic residues for chemistry.

### F003 — Catalytic-loop lysines drive chemistry; ordered Bi-Bi mechanism; cytoplasmic localization

The mobile catalytic loop is not just a lid — it carries residues essential for catalysis. Alanine-scanning mutagenesis of the *Salmonella typhimurium* enzyme shows that loop lysine K103 is catalytically dominant: "the K103A mutant enzyme exhibited a 10⁴-fold decrease in k_cat/K_M for PRPP; the K100A enzyme suffered a 50-fold decrease" ([PMID: 22531099](https://pubmed.ncbi.nlm.nih.gov/22531099/)). Importantly, these mutations barely affect substrate binding — "Equilibrium binding of OMP or PRPP in binary complexes was affected little by loop mutation" ([PMID: 22531099](https://pubmed.ncbi.nlm.nih.gov/22531099/)) — demonstrating that the loop contributes to **transition-state stabilization** rather than ground-state substrate affinity.

Kinetically, the enzyme follows an ordered mechanism. Isothermal titration calorimetry and product-inhibition studies of the *M. tuberculosis* enzyme "suggest a Mono-Iso Ordered Bi-Bi kinetic mechanism" ([PMID: 22075667](https://pubmed.ncbi.nlm.nih.gov/22075667/)). Transition-state analysis (kinetic isotope effects plus computation) reveals the chemical nature of catalysis: "The enzymes form late associative D(N)*A(N)‡ transition states with complete orotate loss and partially associative nucleophile" ([PMID: 19292447](https://pubmed.ncbi.nlm.nih.gov/19292447/)) — a largely dissociative-to-associative SN1-like migration of the ribosyl anomeric carbon.

The active site sits atop the Rossmann fold and is solvent-exposed; the protein has no signal peptide or transmembrane segment, consistent with a **soluble cytoplasmic** enzyme carrying out its function in the cytosol.

### F004 — In *P. putida*, OPRTase is pyrimidine-regulated and carbon-source-responsive

Regulation of this enzyme has been studied directly in *Pseudomonas putida*. In *P. putida* ATCC 17536, the de novo pyrimidine pathway enzymes — including OPRTase and OMP decarboxylase — are subject to both catabolite and end-product control. Enzyme activities "were higher in glucose-grown cells than in succinate-grown cells, indicating catabolite repression by succinate" ([PMID: 12619820](https://pubmed.ncbi.nlm.nih.gov/12619820/)). End-product/intermediate control is also evident: "When glucose was the carbon source, orotic acid supplementation significantly decreased orotate phosphoribosyltransferase and orotidine 5′-monophosphate (OMP) decarboxylase activities" ([PMID: 12619820](https://pubmed.ncbi.nlm.nih.gov/12619820/)). This regulation operates at the transcriptional level: "Regulation at the transcriptional level of de novo pyrimidine biosynthetic enzyme synthesis in P. putida ATCC 17536 was observed" ([PMID: 12619820](https://pubmed.ncbi.nlm.nih.gov/12619820/)).

In enterobacteria, additional regulatory layers apply to *pyrE*: UTP-dependent transcriptional attenuation in the *rph-pyrE* operon ([PMID: 1375912](https://pubmed.ncbi.nlm.nih.gov/1375912/)) and repression by guanine nucleotides ([PMID: 2689594](https://pubmed.ncbi.nlm.nih.gov/2689594/)). These illustrate the general principle that *pyrE* expression is tuned to nucleotide pool balance, though the precise mechanism in *P. putida* was demonstrated at the transcriptional/activity level rather than the attenuator level.

### F005 — Sequence analysis of Q88C92 confirms a 213-aa soluble Type I PRTase with the canonical PRPP-binding motif

Direct analysis of the actual target sequence (retrieved from UniProt) confirmed the annotation at the residue level. Q88C92 is **213 residues** long, matching characterized bacterial OPRTases (e.g., *E. coli* PyrE is also 213 aa). It contains the diagnostic **Type I PRTase PRPP-binding loop** at positions 120–134 (LIIDDVITAGTAIRE) with the critical **vicinal aspartates D124/D125** that coordinate Mg²⁺ and the PRPP 5′-phosphate/ribose, plus the conserved hood/loop segment 96-FNRK-99.

Hydropathy analysis (Kyte-Doolittle, window 19) gave a maximum hydrophobicity of only 1.75 at an internal β-strand (residue ~174), while the N-terminus (MQPYQRDFIR…) is hydrophilic and charged. There is **no N-terminal Sec signal peptide and no transmembrane helix**, and only two cysteines (no expected disulfides), with a net charge of approximately −6. These features are exactly those of a soluble cytoplasmic enzyme. The literature confirms the structural context — "with a solvent-exposed active site atop a Rossman-type nucleotide binding fold" ([PMID: 9890909](https://pubmed.ncbi.nlm.nih.gov/9890909/)) — and the conservation of function-determining residues: "The catalytic residues and consensus sequences for substrate binding in the enzyme were conserved among other organisms" ([PMID: 15003844](https://pubmed.ncbi.nlm.nih.gov/15003844/)).

### F006 — OPRTase is required for pyrimidine prototrophy and activates orotate analogues (5-fluoroorotate)

Genetic evidence establishes OPRTase as essential for de novo pyrimidine supply. In *Trypanosoma brucei*, ablation of the combined OPRT+OMPDC (UMP synthase) activities produced strict pyrimidine auxotrophy: "The DKO was unable to grow in pyrimidine-depleted medium in vitro, unless supplemented with uracil, uridine, deoxyuridine or UMP" ([PMID: 23980694](https://pubmed.ncbi.nlm.nih.gov/23980694/)). The same knockout demonstrated OPRT's substrate handling of orotate analogues: "DKO parasites were completely resistant to 5-fluoroorotate and hypersensitive to 5-fluorouracil, consistent with loss of UMPS" ([PMID: 23980694](https://pubmed.ncbi.nlm.nih.gov/23980694/)). The resistance to 5-fluoroorotate arises because OPRTase normally activates this orotate analogue; without the enzyme, the toxic conversion cannot occur.

In bacteria, *pyrE* loss likewise generates uracil-requiring auxotrophs ([PMID: 6358797](https://pubmed.ncbi.nlm.nih.gov/6358797/)). By extension, in *P. putida* the *pyrE* product is expected to be essential for pyrimidine prototrophy whenever exogenous pyrimidine salvage is unavailable.

### F007 — Residue-level active-site map confirms the Mg²⁺-dependent OPRT reaction with a shared, domain-swapped active site

Curated UniProt/Rhea annotation of the exact target protein Q88C92 provides a residue-resolution confirmation. The annotated catalytic activity is **RHEA:10380** (orotidine 5′-phosphate + diphosphate ⇌ orotate + PRPP), the cofactor is **Mg²⁺**, the subunit assembly is **homodimer**, and the pathway is "Pyrimidine metabolism; UMP biosynthesis via de novo pathway; UMP from orotate: step 1/2" — i.e., OPRT is step 1 of the two-step orotate→UMP module, OMP decarboxylase being step 2.

Critically, curated ligand-binding residues map onto the sequence features identified in F005: substrate/PRPP binding at residues 34–35, 99, 103, 105, the 124–132 DDVITAGT PRPP loop, 128, and 156. Several binding residues — 26, 72–73, 100, and the 124–132 loop — are annotated **"in other chain,"** meaning they contribute to the *partner* subunit's active site. This is the molecular signature of the domain-swapped intersubunit architecture, experimentally supported by the observation that "one of the two identical solvent-exposed loops can descend to cover the active site of the adjacent subunit of the dimeric enzyme" ([PMID: 9890909](https://pubmed.ncbi.nlm.nih.gov/9890909/)). The Mg²⁺ requirement is corroborated by the *M. tuberculosis* studies conducted "in presence of Mg" ([PMID: 22075667](https://pubmed.ncbi.nlm.nih.gov/22075667/)), and the pathway assignment by the description of OPRT catalysis as "an essential step in the de novo biosynthesis of pyrimidines" ([PMID: 19292447](https://pubmed.ncbi.nlm.nih.gov/19292447/)).

### F008 — Q88C92 is highly conserved with experimentally characterized OPRTases, justifying functional transfer

A rigorous quantification of orthology was performed by global pairwise (Needleman-Wunsch) alignment of Q88C92 against characterized bacterial OPRTase orthologs:

| Ortholog | UniProt | Length | Identity to Q88C92 |
|---|---|---|---|
| *E. coli* PyrE | P0A7E3 | 213 aa | **66.7%** |
| *M. tuberculosis* PyrE | P9WFX7 | — | 32.4% |

The 66.7% identity (with identical length) to the well-characterized *E. coli* enzyme is far above the ~30–40% threshold generally sufficient for confident enzyme-function transfer. In both alignments the diagnostic PRPP-binding motif (…DDVITAGT…) and catalytic loop (FNRKE…) are conserved. The literature supports function transfer on this basis: OPRT catalytic and substrate-binding consensus sequences are "conserved among other organisms" ([PMID: 15003844](https://pubmed.ncbi.nlm.nih.gov/15003844/)), and the reference enzyme was "found to be most similar to that of Escherichia coli" ([PMID: 15003844](https://pubmed.ncbi.nlm.nih.gov/15003844/)). The high conservation makes the functional assignment of Q88C92 as OPRTase essentially certain.

---

## Mechanistic Model / Interpretation

### Position in the de novo pyrimidine pathway

OPRTase (PyrE) catalyzes the penultimate step in the biosynthesis of UMP, the master pyrimidine nucleotide from which all other pyrimidines (UDP, UTP, CTP, dTTP) derive:

```
 Glutamine + HCO3- + ATP
        │  (PyrA / carbamoyl-phosphate synthetase)
        ▼
 Carbamoyl phosphate
        │  (PyrB / aspartate transcarbamoylase)  + Aspartate
        ▼
 Carbamoyl aspartate
        │  (PyrC / dihydroorotase)
        ▼
 Dihydroorotate
        │  (PyrD / dihydroorotate dehydrogenase)
        ▼
 OROTATE ───────────────┐
                        │  ★ PyrE / OPRTase  (Q88C92, PP_5291)   ← THIS ENZYME
        PRPP ───────────┤    + Mg2+
                        ▼
 OROTIDINE 5'-MONOPHOSPHATE (OMP) + PPi
        │  (PyrF / OMP decarboxylase)
        ▼
 UMP  →  UDP  →  UTP / CTP / dTTP …
```

Within the UniProt/Rhea "UMP from orotate" module, PyrE is **step 1 of 2** and PyrF (OMP decarboxylase) is step 2. PyrE thus commits free orotate (produced by PyrD) into the ribonucleotide pool by ribosylphosphorylating it, an irreversible-in-practice commitment under cellular conditions despite the intrinsic reversibility of the chemistry.

### Catalytic mechanism

```
            SUBUNIT A                          SUBUNIT B
   ┌──────────────────────┐          ┌──────────────────────┐
   │  Rossmann α/β core    │          │  Rossmann α/β core    │
   │  + "hood" (orotate)   │          │  + "hood" (orotate)   │
   │                       │          │                       │
   │   ACTIVE SITE  ◄──────┼── loop ──┤   (loop from B caps   │
   │   (capped by loop     │  swap    │    A's active site)   │
   │    from subunit B)    │          │                       │
   └──────────────────────┘          └──────────────────────┘
       Catalytic-loop lysines (K100, K103 in S. typhimurium
       numbering) stabilize the transition state — NOT ground state.
```

- **Cofactor:** A single Mg²⁺ ion neutralizes the pyrophosphate leaving group of PRPP (by analogy to the closely related APRTase, [PMID: 12171925](https://pubmed.ncbi.nlm.nih.gov/12171925/)) and orients the substrates.
- **Order of binding:** Mono-Iso Ordered Bi-Bi ([PMID: 22075667](https://pubmed.ncbi.nlm.nih.gov/22075667/)).
- **Chemistry:** A late, associative transition state (D_N*A_N‡) with complete departure of orotate from the ribosyl anomeric carbon; the ribosyl C1′ migrates ~2 Å while base and 5′-phosphate remain largely fixed — an electrophile-migration (SN1-like) nucleophilic displacement ([PMID: 19292447](https://pubmed.ncbi.nlm.nih.gov/19292447/), [PMID: 12171925](https://pubmed.ncbi.nlm.nih.gov/12171925/)).
- **Induced fit:** The flexible catalytic loop transitions from disorder to order on MgPRPP + orotate binding, closing over the shared active site and delivering the catalytic lysines that stabilize the transition state ([PMID: 23315339](https://pubmed.ncbi.nlm.nih.gov/23315339/), [PMID: 22531099](https://pubmed.ncbi.nlm.nih.gov/22531099/)).

### Localization

Every structural and sequence indicator points to a **cytoplasmic** localization: a solvent-exposed active site atop a soluble Rossmann fold, no signal peptide, no transmembrane helix, a hydrophilic charged surface (net charge ≈ −6), and a substrate (PRPP) that is itself a cytosolic central metabolite. The enzyme therefore carries out its function freely in the cytosol, where its substrates orotate (from the upstream membrane-associated PyrD in many bacteria) and PRPP are available.

### Physiological role and regulation in *P. putida*

PyrE sits at a control point of pyrimidine homeostasis. In *P. putida* its transcription/activity responds to carbon source (catabolite repression by succinate) and to pathway flux signals (repression by orotic acid) ([PMID: 12619820](https://pubmed.ncbi.nlm.nih.gov/12619820/)). This allows the cell to match de novo pyrimidine production to growth rate and nutrient status. Loss of the enzyme collapses de novo pyrimidine supply, forcing dependence on salvage and producing uracil auxotrophy ([PMID: 23980694](https://pubmed.ncbi.nlm.nih.gov/23980694/), [PMID: 6358797](https://pubmed.ncbi.nlm.nih.gov/6358797/)).

---

## Evidence Base

| PMID | Title (abbreviated) | How it supports the findings |
|---|---|---|
| [22075667](https://pubmed.ncbi.nlm.nih.gov/22075667/) | Characterization of *M. tuberculosis* OPRT | States the exact reaction and substrates (F001); Mono-Iso Ordered Bi-Bi mechanism and Mg²⁺ requirement (F003, F007) |
| [19292447](https://pubmed.ncbi.nlm.nih.gov/19292447/) | Transition states of *P. falciparum* & human OPRT | Confirms reaction as essential de novo step (F001); late associative transition state (F003, F007) |
| [23315339](https://pubmed.ncbi.nlm.nih.gov/23315339/) | NMR of yeast OMP synthase | Rossmann core + hood + domain-swapped loop; ligand-induced disorder-to-order transition (F002) |
| [9890909](https://pubmed.ncbi.nlm.nih.gov/9890909/) | Motional dynamics of the catalytic loop in OMP synthase | Intersubunit loop covers adjacent active site; apo-state loop flexibility; solvent-exposed active site (F002, F005, F007) |
| [22531099](https://pubmed.ncbi.nlm.nih.gov/22531099/) | Loop residues and catalysis in OMP synthase | K103A ~10⁴-fold, K100A ~50-fold k_cat/K_M loss; loop stabilizes TS not ground state (F003) |
| [12619820](https://pubmed.ncbi.nlm.nih.gov/12619820/) | Control of pyrimidine formation in *P. putida* ATCC 17536 | Direct *P. putida* evidence: catabolite repression and orotic-acid repression of OPRTase; transcriptional regulation (F004) |
| [15003844](https://pubmed.ncbi.nlm.nih.gov/15003844/) | Malaria parasite OPRT kinetics | Conservation of catalytic/substrate-binding consensus sequences; similarity to *E. coli* (F005, F008) |
| [23980694](https://pubmed.ncbi.nlm.nih.gov/23980694/) | *T. brucei* UMP synthase null mutants | OPRT loss → pyrimidine auxotrophy; 5-fluoroorotate resistance shows orotate-analogue activation (F006) |
| [12171925](https://pubmed.ncbi.nlm.nih.gov/12171925/) | Closed-site APRTase complexes (ribosyl migration) | Mechanistic analogy: single-Mg²⁺ PPi neutralization; ribosyl migration; APRTase is nearest structural neighbor of OPRTase |
| [1375912](https://pubmed.ncbi.nlm.nih.gov/1375912/) | Attenuation in *rph-pyrE* operon of *E. coli* | UTP-dependent attenuation regulates *pyrE* (regulatory context, F004) |
| [2689594](https://pubmed.ncbi.nlm.nih.gov/2689594/) | *pyr* gene regulation in *S. typhimurium* | Guanine-nucleotide repression of *pyrE* (regulatory context, F004) |
| [6358797](https://pubmed.ncbi.nlm.nih.gov/6358797/) | *trans*-acting regulatory factor for pyrimidine pathway | *pyrE* loss → uracil auxotrophy in *E. coli* (F006) |
| [28446777](https://pubmed.ncbi.nlm.nih.gov/28446777/) | Structural investigations on *M. tuberculosis* OPRT | Independent structural/functional confirmation of the reaction and Mg²⁺ dependence |
| [36637052](https://pubmed.ncbi.nlm.nih.gov/36637052/) | QM/MM analysis of OPRT inhibitor complexes | Supports mechanistic description of phosphoribosyl transfer |

The mammalian/cancer literature reviewed (UMPS, 5-FU chemosensitivity; e.g., [PMID: 17237621](https://pubmed.ncbi.nlm.nih.gov/17237621/), [PMID: 35674867](https://pubmed.ncbi.nlm.nih.gov/35674867/)) is not directly about the bacterial enzyme but reinforces the conserved biochemical role of OPRTase in activating orotate-analogue drugs — a property parallel to the 5-fluoroorotate handling observed in the trypanosome knockout.

---

## Limitations and Knowledge Gaps

1. **No direct experimental characterization of Q88C92 itself.** The functional assignment rests on (a) very high sequence identity to characterized orthologs (66.7% to *E. coli* PyrE), (b) curated UniProt/Rhea residue-level annotation, and (c) mechanistic studies of homologs from *S. typhimurium*, *M. tuberculosis*, *P. falciparum*, yeast, and human. No kinetic constants (K_M, k_cat), crystal structure, or knockout phenotype have been reported for the *P. putida* KT2440 protein specifically. Function transfer is nonetheless robust given the conservation.

2. **Regulation data are from a different *P. putida* strain.** The transcriptional-regulation evidence (F004) comes from *P. putida* ATCC 17536, not the KT2440 target strain. While the de novo pathway architecture is conserved, strain-specific regulatory details (e.g., presence/structure of an *rph-pyrE* attenuator, operon context of PP_5291) were not experimentally verified for KT2440.

3. **Kinetic mechanism generalization.** The Mono-Iso Ordered Bi-Bi mechanism and transition-state parameters derive from mycobacterial and parasite/yeast enzymes. Although OPRTase mechanism is broadly conserved, subtle differences in substrate order or rate-limiting step in the *P. putida* enzyme cannot be excluded.

4. **Quaternary structure assumption.** Homodimer assembly is annotated for Q88C92 and universal among characterized OPRTases; however, the oligomeric state of the *P. putida* protein has not been experimentally measured.

5. **Localization inferred, not measured.** Cytoplasmic localization is a strong bioinformatic inference (no signal peptide/TM, soluble fold) but has not been experimentally demonstrated for this specific protein.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant expression and steady-state kinetics.** Clone PP_5291, express in *E. coli*, purify, and measure K_M for orotate and PRPP, k_cat, and Mg²⁺ dependence to obtain organism-specific catalytic parameters and confirm the reaction directly for the target protein.

2. **X-ray crystallography or AlphaFold-guided structure validation.** Solve or model the *P. putida* enzyme in apo and MgPRPP/orotate-bound states to confirm the Rossmann-fold + hood + domain-swapped-loop architecture and the "in other chain" intersubunit binding residues (34–35, 99, 103, 105, 124–132, 26, 72–73, 100).

3. **Gene knockout / complementation in KT2440.** Delete PP_5291 and test for uracil auxotrophy; complement to confirm. Test 5-fluoroorotate sensitivity as an activity readout, predicting resistance in the knockout.

4. **Site-directed mutagenesis of the catalytic loop.** Mutate the *P. putida* equivalents of K100/K103 and the vicinal aspartates D124/D125 to verify transition-state contributions and PRPP/Mg²⁺ coordination in this ortholog.

5. **Operon and regulation mapping in KT2440.** Determine the genomic context of PP_5291 (is it in an *rph-pyrE*-like operon?), and test transcriptional responses to carbon source and pyrimidine/orotate availability by RT-qPCR or reporter assays, extending the ATCC 17536 findings to the reference strain.

6. **Oligomeric-state determination.** Use size-exclusion chromatography–multi-angle light scattering (SEC-MALS) or analytical ultracentrifugation to confirm the homodimeric assembly.

---

## Conclusion

The gene *pyrE* (PP_5291, UniProt Q88C92) of *Pseudomonas putida* KT2440 encodes **orotate phosphoribosyltransferase (OPRTase, EC 2.4.2.10)**, a soluble cytoplasmic, Mg²⁺-dependent Type I phosphoribosyltransferase. It catalyzes the fifth step of de novo pyrimidine biosynthesis — the reversible transfer of a phosphoribosyl group from PRPP to orotate, producing orotidine 5′-monophosphate (OMP) and pyrophosphate — committing orotate to the pyrimidine nucleotide pool that ultimately yields UMP and all downstream pyrimidines. The enzyme functions as an obligate homodimer with a domain-swapped, flexible catalytic loop that closes over a shared intersubunit active site, operating through an ordered Bi-Bi mechanism and a late associative transition state stabilized by conserved loop lysines. In *P. putida* its expression/activity is transcriptionally regulated by carbon source and pyrimidine availability, and its loss causes pyrimidine (uracil) auxotrophy. The assignment is supported by residue-level curated annotation of the exact target protein and by 66.7% sequence identity to the experimentally characterized *E. coli* PyrE, making the functional annotation highly reliable.


## Artifacts

- [OpenScientist final report](pyrE-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](pyrE-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:22075667
2. PMID:19292447
3. PMID:23315339
4. PMID:9890909
5. PMID:22531099
6. PMID:12619820
7. PMID:1375912
8. PMID:2689594
9. PMID:15003844
10. PMID:23980694
11. PMID:6358797
12. PMID:12171925
13. PMID:17237621
14. PMID:35674867