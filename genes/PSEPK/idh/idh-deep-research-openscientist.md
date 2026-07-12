---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-11T18:21:04.931568'
end_time: '2026-07-11T18:32:15.114708'
duration_seconds: 670.18
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: idh
  gene_symbol: idh
  uniprot_accession: Q88FS1
  protein_description: 'RecName: Full=Isocitrate dehydrogenase [NADP] {ECO:0000256|PIRNR:PIRNR009407};
    EC=1.1.1.42 {ECO:0000256|PIRNR:PIRNR009407}; AltName: Full=Oxalosuccinate decarboxylase
    {ECO:0000256|PIRNR:PIRNR009407};'
  gene_info: Name=idh {ECO:0000313|EMBL:AAN69606.1}; OrderedLocusNames=PP_4012 {ECO:0000313|EMBL:AAN69606.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the monomeric-type IDH family.
  protein_domains: Isocitrate_DH_NADP_mono. (IPR004436); IDH (PF03971)
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
citation_count: 10
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: idh-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: idh-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88FS1
- **Protein Description:** RecName: Full=Isocitrate dehydrogenase [NADP] {ECO:0000256|PIRNR:PIRNR009407}; EC=1.1.1.42 {ECO:0000256|PIRNR:PIRNR009407}; AltName: Full=Oxalosuccinate decarboxylase {ECO:0000256|PIRNR:PIRNR009407};
- **Gene Information:** Name=idh {ECO:0000313|EMBL:AAN69606.1}; OrderedLocusNames=PP_4012 {ECO:0000313|EMBL:AAN69606.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the monomeric-type IDH family.
- **Key Domains:** Isocitrate_DH_NADP_mono. (IPR004436); IDH (PF03971)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "idh" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'idh' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **idh** (gene ID: idh, UniProt: Q88FS1) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *idh* (PP_4012, UniProt Q88FS1) — Monomeric NADP⁺-Dependent Isocitrate Dehydrogenase of *Pseudomonas putida* KT2440

---

## Summary

The gene **idh** (ordered locus **PP_4012**; UniProt **Q88FS1**) of *Pseudomonas putida* strain KT2440 (ATCC 47054 / DSM 6125 / NCIMB 11950) encodes a **monomeric-type, NADP⁺-dependent isocitrate dehydrogenase** (IDH; EC 1.1.1.42). The protein is a single polypeptide of **741 amino acids with a molecular mass of ~79.9 kDa**, a size that is the structural signature of the monomeric IDH family and stands in contrast to the smaller (~45–50 kDa) subunits of the more familiar dimeric IDHs. Its identity is anchored by multiple orthogonal lines of evidence: the UniProt annotation (monomeric-type IDH family, InterPro IPR004436 "Isocitrate_DH_NADP_mono," Pfam PF03971 "IDH"), the annotated catalytic activity (D-*threo*-isocitrate + NADP⁺ → 2-oxoglutarate + CO₂ + NADPH), a required divalent metal cofactor (Mg²⁺ or Mn²⁺), and mapped active-site residues for isocitrate, NADP⁺, and the catalytic metal. The gene symbol "idh" and the UniProt description are fully consistent with the literature on monomeric bacterial NADP-IDHs; there is no evidence of gene-symbol ambiguity for this protein.

Functionally, Q88FS1 catalyzes the **third reaction of the tricarboxylic acid (TCA) cycle**: the metal-assisted, two-step oxidative decarboxylation of isocitrate. The reaction proceeds through the transient intermediate **oxalosuccinate** — the basis of the enzyme's alternative name "oxalosuccinate decarboxylase" — via a conserved **Tyr–Asp–Lys catalytic triad**, yielding 2-oxoglutarate (α-ketoglutarate), CO₂, and NADPH. The enzyme is located in the **cytoplasm** (no signal peptide, no transmembrane segments) and displays near-absolute specificity for NADP⁺ over NAD⁺ and for isocitrate over related substrates. Because IDH sits precisely at the branch point between the CO₂-generating steps of the TCA cycle and the carbon-conserving glyoxylate bypass, its product NADPH feeds anabolism and oxidative-stress defense, while its product 2-oxoglutarate is the primary carbon skeleton for nitrogen assimilation into glutamate and glutamine.

A key mechanistic conclusion of this investigation is that, unlike the paradigmatic *Escherichia coli* dimeric NADP-IDH, the *P. putida* monomeric enzyme is **not controlled by the AceK phosphorylation switch**. Monomeric-type IDHs lack the flexible phosphorylation loop (built around the *E. coli* Ser-113 site) that AceK kinase/phosphatase uses to inactivate the dimeric enzyme during acetate growth; in monomeric IDHs the corresponding region is a rigid α-helix. Consequently, the activity of Q88FS1 is governed chiefly by substrate and coenzyme availability and by transcriptional/metabolic control rather than by covalent modification.

---

## Key Findings

### Finding 1 — Q88FS1 is a monomeric-type, NADP⁺-dependent isocitrate dehydrogenase (EC 1.1.1.42)

The UniProt record for Q88FS1 assigns the protein to the **monomeric-type IDH family**, with InterPro domain **IPR004436 (Isocitrate_DH_NADP_mono)** and Pfam **PF03971 (IDH)**, EC number **1.1.1.42**, and the alternate name **oxalosuccinate decarboxylase**. NADP⁺-dependent isocitrate dehydrogenase belongs to the β-decarboxylating dehydrogenase family and catalyzes the oxidative decarboxylation of (2R,3S)-isocitrate to yield 2-oxoglutarate and CO₂ within the Krebs cycle ([PMID: 12467571](https://pubmed.ncbi.nlm.nih.gov/12467571/)). Monomeric NADP-IDHs are distinguished from dimeric IDHs by being single-chain enzymes of ~80–100 kDa; the characterized *Streptomyces lividans* monomeric IDH (SlIDH), for example, has a molecular mass of about 80 kDa, described as "typical of a monomeric NADP-IDH" ([PMID: 19631711](https://pubmed.ncbi.nlm.nih.gov/19631711/)). The ~79.9 kDa mass of Q88FS1 (see Finding 8) places it squarely within this family and distinguishes it from the ~45 kDa subunits that assemble into dimeric IDHs.

### Finding 2 — Monomeric IDH arose by intragenic domain duplication that recreates the dimeric active site within one chain

The evolutionary and structural logic of the monomeric IDH family explains how a single polypeptide accomplishes what dimeric IDHs achieve only by assembling two subunits. The 1.95 Å crystal structure of the *Azotobacter vinelandii* monomeric IDH (AvIDH) revealed that the enzyme is built from two distinct domains related by a duplicated structural motif; this **"fusional structure by domain duplication enables a single polypeptide chain to form a structure at the catalytic site that is homologous to the dimeric IDH, the catalytic site of which is located at the interface of two identical subunits"** ([PMID: 12467571](https://pubmed.ncbi.nlm.nih.gov/12467571/)). The NADP⁺-bound closed-form structure of AvIDH further confirmed that this reconstituted active site is a genuine, fully functional β-decarboxylating dehydrogenase catalyzing "the dehydration and decarboxylation of isocitrate to yield 2-oxoglutarate and CO₂ in the Krebs cycle" ([PMID: 12855708](https://pubmed.ncbi.nlm.nih.gov/12855708/)). Because Q88FS1 is a member of this family, its catalytic architecture is inferred, by strong homology, to follow the same single-chain domain-duplication design.

### Finding 3 — High NADP⁺ coenzyme specificity and divalent-metal dependence; cytoplasmic role at the TCA/glyoxylate branch and in NADPH supply

Monomeric IDHs display an extreme preference for NADP⁺ over NAD⁺. The recombinant *S. lividans* SlIDH showed a **62,000-fold (kcat/Km) preference for NADP⁺ over NAD⁺ with Mn²⁺, and 85,000-fold with Mg²⁺** ([PMID: 19631711](https://pubmed.ncbi.nlm.nih.gov/19631711/)), underscoring both the coenzyme selectivity and the requirement for a divalent cation. Structurally, the 2′-phosphate of NADP⁺ that confers this selectivity is coordinated in the monomeric IDH of *Corynebacterium glutamicum* by two arginines, a histidine, and (via water) a lysine ([PMID: 21931217](https://pubmed.ncbi.nlm.nih.gov/21931217/)). The same work emphasized that IDH "lies at a crucial bifurcation point between CO₂-generating steps in the cycle and carbon-conserving steps in the glyoxylate bypass. Hence, the enzyme is a focus of regulation" ([PMID: 21931217](https://pubmed.ncbi.nlm.nih.gov/21931217/)). In the specific physiological context of *P. putida* KT2440, this NADPH-producing role is central: determination of the NADPH balance "revealed that the default metabolic state of *P. putida* KT2440 is characterized by a slight catabolic overproduction of reducing power" ([PMID: 26350459](https://pubmed.ncbi.nlm.nih.gov/26350459/)), which serves anabolism and stress defense.

### Finding 4 — Two-step catalytic mechanism via an oxalosuccinate intermediate with a conserved Tyr–Asp–Lys catalytic triad

The reaction catalyzed by Q88FS1 proceeds in two chemical steps. First, a metal-assisted dehydrogenation transfers a hydride to NADP⁺, converting isocitrate to the unstable β-keto acid **oxalosuccinate**; second, β-decarboxylation of oxalosuccinate releases CO₂ and yields 2-oxoglutarate. The crystal structure of the *Thermus thermophilus* NADP-IDH explicitly describes the enzyme as "catalyzing oxidative decarboxylation of isocitrate into oxalosuccinate (intermediate) and finally the product α-ketoglutarate" ([PMID: 24832735](https://pubmed.ncbi.nlm.nih.gov/24832735/)). This intermediate is the structural basis of the enzyme's alternate name, **oxalosuccinate decarboxylase**, recorded in the UniProt entry for Q88FS1. The same structure showed that "the overall TtIDH structure exhibits closed conformation with catalytic triad residues, Tyr144-Asp248-Lys191 are conserved" ([PMID: 24832735](https://pubmed.ncbi.nlm.nih.gov/24832735/)), identifying the acid–base machinery that mediates the chemistry. In the monomeric AvIDH, binding of NADP⁺ induces a closed conformation that positions the nicotinamide ring for immediate hydride transfer, accounting for the exceptionally high turnover of monomeric IDHs ([PMID: 12855708](https://pubmed.ncbi.nlm.nih.gov/12855708/)).

### Finding 5 — Physiological role: NADPH and 2-oxoglutarate provision links IDH to anabolism, nitrogen assimilation, and oxidative-stress defense

In *Pseudomonas* and other aerobic bacteria, NADP-dependent IDH is a principal source of both NADPH and 2-oxoglutarate (α-ketoglutarate, KG). KG is itself a non-enzymatic antioxidant that neutralizes reactive oxygen species (yielding succinate + CO₂), while NADPH fuels the glutathione and thioredoxin antioxidant systems. In *Pseudomonas fluorescens* challenged with H₂O₂, "the increased production of KG mediated by NADP-dependent isocitrate dehydrogenase (NADP-ICDH) and its decreased utilization via the TCA cycle confer a unique strategy to modulate the cellular redox environment" ([PMID: 17668068](https://pubmed.ncbi.nlm.nih.gov/17668068/)), with NAD-linked TCA enzymes simultaneously downregulated. The centrality of NADPH provision in the related strain is reinforced by the observation that "cells growing on glucose thus run a biochemical cycle that favors NADPH formation" in *P. putida* KT2440 ([PMID: 26350459](https://pubmed.ncbi.nlm.nih.gov/26350459/)). In parallel, the KG produced by IDH is the entry-point carbon skeleton for glutamate/glutamine biosynthesis and therefore for nitrogen assimilation.

### Finding 6 — The monomeric enzyme is NOT controlled by the AceK phosphorylation switch used for *E. coli* dimeric IDH

The best-characterized regulatory device for bacterial IDH is the *E. coli* phosphorylation cycle, in which the bifunctional IDH kinase/phosphatase AceK phosphorylates Ser-113 to inactivate the dimeric enzyme and thereby divert isocitrate into the glyoxylate bypass during growth on acetate; "it is the phosphorylation of the Ser-113 residue that renders the enzyme catalytically inactive as it prevents isocitrate from binding to the active site" ([PMID: 16415587](https://pubmed.ncbi.nlm.nih.gov/16415587/)). Monomeric-type IDHs lack this switch. In the *C. glutamicum* monomeric IDH, "the amino acid residues corresponding to the *Escherichia coli* IDH phosphorylation-loop are α-helical compared with the more flexible random-coil region in the *E. coli* protein where IDH activation is controlled by phosphorylation. This more structured region supports the idea that activation of CgIDH is not controlled by phosphorylation" ([PMID: 16416443](https://pubmed.ncbi.nlm.nih.gov/16416443/)). By homology, Q88FS1 is expected to be regulated by substrate/coenzyme availability and by transcriptional control rather than by reversible phosphorylation.

### Finding 7 — Exceptional isocitrate/NADP⁺ specificity and catalytic efficiency; a catalytic lysine demonstrated by mutagenesis; a family spanning the proteobacteria

Direct biochemical comparison shows that monomeric IDHs are not merely equivalent to dimeric IDHs but frequently superior in efficiency and selectivity. The *C. glutamicum* monomeric IDH is "10-fold more active (calculated as kcat/Km.isocitrate/Km.NADP) and 7-fold more NADP-specific than the dimeric enzyme, favoring NADP over NAD by a factor of 50,000" ([PMID: 11185559](https://pubmed.ncbi.nlm.nih.gov/11185559/)). Crucially, direct experimental (rather than purely structural) evidence for the catalytic apparatus exists: "the role of Lys253 as catalytic residue has been demonstrated by site-directed mutagenesis" ([PMID: 11185559](https://pubmed.ncbi.nlm.nih.gov/11185559/)). The monomeric family is widely distributed: "Monomeric NADP⁺-specific IDHs have been identified from about 50 different bacterial species, such as proteobacteria, actinobacteria, and planctomycetes" ([PMID: 16416443](https://pubmed.ncbi.nlm.nih.gov/16416443/)), placing the proteobacterial *P. putida* enzyme within a well-populated and well-studied clade.

### Finding 8 — Sequence-level confirmation: a 741-aa, ~79.9 kDa single-chain cytoplasmic NADP-IDH with mapped substrate/cofactor/metal binding sites

The UniProt Q88FS1 record (retrieved programmatically) provides the definitive molecular-level confirmation of identity. The protein is **741 amino acids** long with a molecular weight of **79,900 Da (~80 kDa)** — matching the single-chain size of monomeric-type IDHs — encoded by gene *idh*, ordered locus **PP_4012**. The annotated catalytic activity is **D-*threo*-isocitrate + NADP⁺ = 2-oxoglutarate + CO₂ + NADPH**, with the cofactor **Mg²⁺ or Mn²⁺**. Functional keywords include "Tricarboxylic acid cycle," "Glyoxylate bypass," "NADP," "Oxidoreductase," "Metal-binding," and "Magnesium." The record contains **no signal peptide and no transmembrane segment**, consistent with a **cytoplasmic** localization. Mapped functional sites include NADP⁺-binding residues (approximately 83–88, 136, 585–586, 590, 601–603, 650), D-*threo*-isocitrate/substrate-binding residues (~133–140, 146, 548), and Mg²⁺-coordinating residues (351, 549, 553).

---

## Mechanistic Model / Interpretation

### The reaction and its place in metabolism

Q88FS1 catalyzes the third step of the oxidative TCA cycle, converting isocitrate to 2-oxoglutarate. The overall reaction and its two-step mechanism can be summarized:

```
                     Mg2+/Mn2+                        Mg2+/Mn2+
   D-threo-isocitrate  ---->  [oxalosuccinate]  ---->  2-oxoglutarate
        + NADP+     (dehydrogenation,        (beta-decarboxylation,    + CO2
                     hydride -> NADP+)          loss of CO2)            + NADPH
                          |___________ Tyr-Asp-Lys catalytic triad __________|
```

The enzyme sits at a pivotal metabolic junction:

```
                 Citrate
                    |  (aconitase)
                    v
               Isocitrate
                 /       \
   IDH (PP_4012)/         \  isocitrate lyase (glyoxylate bypass)
              /            \
   2-oxoglutarate         glyoxylate + succinate
   + CO2 + NADPH            |
       |                    v  (carbon-conserving; used on C2 substrates)
       |  --> glutamate/glutamine (N assimilation)
       |  --> NADPH: biosynthesis + antioxidant systems
       v
   rest of TCA cycle
```

### Why the monomeric design matters

The monomeric IDH family solves the same catalytic problem as dimeric IDH but with a fundamentally different architecture. Dimeric IDHs build their active site at the interface between two identical ~45 kDa subunits. The monomeric enzymes instead fuse two domains within a single ~80 kDa chain by intragenic duplication, reconstituting an interface-like active site within one polypeptide ([PMID: 12467571](https://pubmed.ncbi.nlm.nih.gov/12467571/)). This design is not merely an evolutionary curiosity — the *C. glutamicum* enzyme demonstrates that the monomeric form can be an order of magnitude more catalytically efficient and dramatically more NADP⁺- and isocitrate-specific than its dimeric counterpart ([PMID: 11185559](https://pubmed.ncbi.nlm.nih.gov/11185559/)).

### Regulation: substrate-driven, not phosphorylation-driven

The most consequential regulatory distinction for Q88FS1 is the **absence of the AceK phosphorylation switch**. In *E. coli*, the flux partition between the TCA cycle and glyoxylate bypass is enforced by phosphorylation of dimeric IDH at Ser-113 ([PMID: 16415587](https://pubmed.ncbi.nlm.nih.gov/16415587/)). Monomeric IDHs replace the *E. coli* flexible phosphorylation loop with a rigid α-helix and therefore cannot be regulated this way ([PMID: 16416443](https://pubmed.ncbi.nlm.nih.gov/16416443/)). This implies that in *P. putida* KT2440, partitioning of isocitrate between the TCA cycle and the glyoxylate bypass — and the setting of IDH flux itself — is governed by isocitrate and NADP⁺/NADPH pool concentrations and by transcriptional regulation, rather than by rapid covalent modification of the enzyme.

### Comparative summary

| Property | *P. putida* Q88FS1 (monomeric) | *E. coli* dimeric NADP-IDH |
|---|---|---|
| Quaternary structure | Single chain (~80 kDa) | Homodimer (~2 × 45 kDa) |
| Active-site origin | Intragenic domain duplication | Subunit interface |
| Family / domains | Monomeric IDH (IPR004436, PF03971) | Dimeric IDH |
| Coenzyme specificity | NADP⁺ ≫ NAD⁺ (10⁴–10⁵-fold) | NADP⁺-specific, less extreme |
| Phospho-regulation (AceK) | **Absent** (rigid α-helix) | **Present** (Ser-113 loop) |
| Catalytic triad | Tyr–Asp–Lys (conserved) | Conserved acid–base residues |
| Cofactor | Mg²⁺ or Mn²⁺ | Mg²⁺/Mn²⁺ |

### Localization and pathway integration

All evidence points to a **cytoplasmic** enzyme: Q88FS1 has no signal peptide and no transmembrane helix, and its substrates (isocitrate, NADP⁺) and products (2-oxoglutarate, NADPH) are cytosolic metabolites of central carbon metabolism. Its outputs integrate directly into three programs: (1) continuation of the oxidative TCA cycle; (2) **anabolic NADPH supply**, consistent with the observation that glucose-grown *P. putida* KT2440 runs a cycle favoring NADPH formation and maintains a slight catabolic overproduction of reducing power ([PMID: 26350459](https://pubmed.ncbi.nlm.nih.gov/26350459/)); and (3) **oxidative-stress defense and nitrogen assimilation** through 2-oxoglutarate, which both scavenges ROS non-enzymatically and serves as the carbon skeleton for glutamate/glutamine synthesis ([PMID: 17668068](https://pubmed.ncbi.nlm.nih.gov/17668068/)).

---

## Evidence Base

| PMID | Study (subject) | How it supports the annotation |
|---|---|---|
| [12467571](https://pubmed.ncbi.nlm.nih.gov/12467571/) | Structure of monomeric IDH (*A. vinelandii*); domain duplication | Defines the reaction (isocitrate → 2-oxoglutarate + CO₂), the β-decarboxylating family, and the single-chain domain-duplication architecture (Findings 1, 2) |
| [12855708](https://pubmed.ncbi.nlm.nih.gov/12855708/) | NADP⁺-bound monomeric IDH structure (*A. vinelandii*) | Confirms cofactor recognition, closed conformation for hydride transfer, and reaction chemistry (Findings 2, 4) |
| [19631711](https://pubmed.ncbi.nlm.nih.gov/19631711/) | Monomeric IDH from *S. lividans* | Confirms ~80 kDa single-chain mass and quantifies 62,000–85,000-fold NADP⁺ preference with divalent metal (Findings 1, 3) |
| [21931217](https://pubmed.ncbi.nlm.nih.gov/21931217/) | Highly NADP⁺-specific monomeric IDH structure (*C. glutamicum*) | Structural basis of 2′-phosphate recognition; establishes the TCA/glyoxylate branch-point role and regulatory importance (Finding 3) |
| [24832735](https://pubmed.ncbi.nlm.nih.gov/24832735/) | NADP-IDH structure (*T. thermophilus*) | Documents the oxalosuccinate intermediate and identifies the conserved Tyr144–Asp248–Lys191 catalytic triad (Finding 4) |
| [11185559](https://pubmed.ncbi.nlm.nih.gov/11185559/) | Highly specific monomeric IDH (*C. glutamicum*) | Quantifies superior efficiency/specificity vs. dimeric IDH; mutagenesis demonstrates catalytic Lys253 (Finding 7) |
| [16416443](https://pubmed.ncbi.nlm.nih.gov/16416443/) | Substrate-free monomeric IDH structure; phylogeny | Shows monomeric IDHs lack the *E. coli* phosphorylation loop (rigid α-helix) and span ~50 proteobacterial/actinobacterial/planctomycete species (Findings 6, 7) |
| [16415587](https://pubmed.ncbi.nlm.nih.gov/16415587/) | Phosphoregulation of *E. coli* IDH | Describes the AceK/Ser-113 device that the monomeric family lacks (Finding 6) |
| [26350459](https://pubmed.ncbi.nlm.nih.gov/26350459/) | Central metabolism of *P. putida* KT2440 (EDEMP cycle) | Places NADP-IDH's NADPH output in the strain-specific physiological context of default reducing-power overproduction (Findings 3, 5) |
| [17668068](https://pubmed.ncbi.nlm.nih.gov/17668068/) | TCA cycle "novel twist"; KG in redox defense (*Pseudomonas*) | Links NADP-IDH's product (KG) and its regulation to oxidative-stress defense (Finding 5) |

The evidence base is internally consistent and mutually reinforcing. Structural studies of four different bacterial monomeric IDHs (*A. vinelandii*, *C. glutamicum*, *S. lividans*, *T. thermophilus*) converge on the same architecture, mechanism, and specificity, and the *P. putida* UniProt record's sequence-level features (741 aa, ~80 kDa, mapped NADP⁺/isocitrate/Mg²⁺ sites, cytoplasmic) match this family exactly. No literature was found that would reassign the "idh" symbol for this organism to a different protein, so there is no gene-symbol ambiguity here.

---

## Limitations and Knowledge Gaps

1. **No direct biochemical study of Q88FS1 itself.** All kinetic parameters (coenzyme preference, kcat/Km, metal dependence), the catalytic-triad assignment, and the absence of phosphoregulation are inferred by strong homology from other monomeric IDHs (*C. glutamicum*, *A. vinelandii*, *S. lividans*, *T. thermophilus*), not measured on the purified *P. putida* KT2440 enzyme. The specific catalytic residue numbering (e.g., Lys253 in *C. glutamicum*, the Tyr144–Asp248–Lys191 triad in *T. thermophilus*) has not been mapped experimentally onto the Q88FS1 sequence.

2. **Localization is predicted, not experimentally demonstrated.** The cytoplasmic assignment rests on the absence of a signal peptide/transmembrane segment and on the known biochemistry of central metabolism, not on direct fractionation or imaging of *P. putida* KT2440.

3. **Regulatory mechanism inferred, not tested.** The conclusion that Q88FS1 lacks AceK-type phosphoregulation is based on the structural rigidity of the phospho-loop region in other monomeric IDHs. Whether *P. putida* possesses any alternative post-translational regulation of IDH, and how transcription of PP_4012 responds to carbon source (glucose vs. acetate/C2 substrates), remains uncharacterized here.

4. **Quantitative flux role in *P. putida* is indirect.** The NADPH and 2-oxoglutarate physiology is drawn largely from *P. fluorescens* oxidative-stress studies and the *P. putida* EDEMP-cycle work; the precise fractional contribution of IDH (versus the ED pathway's NADPH-producing steps and the pentose phosphate pathway) to the KT2440 NADPH budget was not partitioned in this investigation.

5. **Possible isozymes not excluded.** Some bacteria carry both monomeric and dimeric IDHs (e.g., *Colwellia*, *Xylella fastidiosa*). Whether *P. putida* KT2440 encodes a second IDH isozyme was not exhaustively assessed; PP_4012 is treated here as the annotated *idh*.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant expression and steady-state kinetics.** Clone PP_4012, purify the protein, and measure kcat, Km(isocitrate), Km(NADP⁺), and the NADP⁺/NAD⁺ and isocitrate specificity ratios with both Mg²⁺ and Mn²⁺ — directly confirming the family-based inferences for the *P. putida* enzyme.

2. **Active-site mutagenesis.** Map the *T. thermophilus* Tyr–Asp–Lys triad and the *C. glutamicum* catalytic Lys onto the Q88FS1 sequence and test alanine substitutions for loss of activity, verifying the acid–base machinery and the catalytic lysine in this specific protein.

3. **Phosphorylation test.** Assay whether purified Q88FS1 can be phosphorylated/inactivated (e.g., incubation with cell extracts, phospho-specific detection, or an AceK homolog if present) to experimentally confirm the predicted absence of AceK-type regulation.

4. **Structural determination.** Solve the crystal structure (or generate a high-confidence AlphaFold model with PAE analysis) of Q88FS1 to verify the domain-duplication architecture, the rigid (α-helical) phospho-loop region, and the cofactor-2′-phosphate recognition residues.

5. **Physiological flux and knockout studies.** Construct a PP_4012 deletion (or knockdown) in *P. putida* KT2440 and quantify effects on growth on glucose vs. C2 substrates, NADPH/NADP⁺ ratios, 2-oxoglutarate pools, glutamate auxotrophy, and oxidative-stress (H₂O₂) tolerance — directly testing the proposed roles in NADPH supply, nitrogen assimilation, and redox defense.

6. **Genome survey for IDH isozymes.** Confirm whether KT2440 encodes any additional (dimeric or second monomeric) IDH, to establish whether PP_4012 is the sole isocitrate dehydrogenase and thus solely responsible for this TCA step.

---

## Consensus Answer

*P. putida* KT2440 **idh** (PP_4012, Q88FS1) encodes a **monomeric-type, NADP⁺-dependent isocitrate dehydrogenase** (EC 1.1.1.42; 741 aa, ~80 kDa single chain) that catalyzes the cytoplasmic, Mg²⁺/Mn²⁺-dependent oxidative decarboxylation of D-*threo*-isocitrate to 2-oxoglutarate + CO₂ + NADPH — the third step of the TCA cycle at its branch point with the glyoxylate bypass — proceeding via an oxalosuccinate intermediate through a conserved Tyr–Asp–Lys catalytic triad with near-absolute specificity for NADP⁺ and isocitrate. Its products supply NADPH for biosynthesis and oxidative-stress defense and 2-oxoglutarate for nitrogen assimilation, and, unlike the *E. coli* dimeric IDH, it lacks the AceK phosphorylation switch, so its activity is set by substrate/coenzyme levels rather than covalent modification.


## Artifacts

- [OpenScientist final report](idh-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](idh-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:12467571
2. PMID:19631711
3. PMID:12855708
4. PMID:21931217
5. PMID:26350459
6. PMID:24832735
7. PMID:17668068
8. PMID:16415587
9. PMID:16416443
10. PMID:11185559