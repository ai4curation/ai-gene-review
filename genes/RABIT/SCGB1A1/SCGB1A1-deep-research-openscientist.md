---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-24T18:45:47.233605'
end_time: '2026-10-24T18:57:33.972866'
duration_seconds: 706.74
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: RABIT
  gene_id: SCGB1A1
  gene_symbol: SCGB1A1
  uniprot_accession: P02779
  protein_description: 'RecName: Full=Uteroglobin; AltName: Full=Blastokinin; AltName:
    Full=Secretoglobin family 1A member 1; Flags: Precursor;'
  gene_info: Name=SCGB1A1; Synonyms=UGB, UGL;
  organism_full: Oryctolagus cuniculus (Rabbit).
  protein_family: Belongs to the secretoglobin family. .
  protein_domains: Secretoglobin. (IPR016126); Secretoglobin_1C-like. (IPR043215);
    Secretoglobin_sf. (IPR035960); Uteroglobin. (IPR000329); Uteroglobin (PF01099)
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
citation_count: 18
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: SCGB1A1-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: SCGB1A1-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** P02779
- **Protein Description:** RecName: Full=Uteroglobin; AltName: Full=Blastokinin; AltName: Full=Secretoglobin family 1A member 1; Flags: Precursor;
- **Gene Information:** Name=SCGB1A1; Synonyms=UGB, UGL;
- **Organism (full):** Oryctolagus cuniculus (Rabbit).
- **Protein Family:** Belongs to the secretoglobin family. .
- **Key Domains:** Secretoglobin. (IPR016126); Secretoglobin_1C-like. (IPR043215); Secretoglobin_sf. (IPR035960); Uteroglobin. (IPR000329); Uteroglobin (PF01099)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "SCGB1A1" matches the protein description above**
2. **Verify the organism is correct:** Oryctolagus cuniculus (Rabbit).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'SCGB1A1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **SCGB1A1** (gene ID: SCGB1A1, UniProt: P02779) in RABIT.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: Rabbit Uteroglobin (SCGB1A1 / UGB, UniProt P02779)

**Organism:** *Oryctolagus cuniculus* (Rabbit)
**Gene:** SCGB1A1 (synonyms UGB, UGL)
**Protein:** Uteroglobin / Blastokinin / Secretoglobin family 1A member 1 (Precursor)
**Protein family:** Secretoglobin superfamily (founding member); Pfam PF01099 (Uteroglobin); InterPro IPR000329, IPR016126, IPR035960, IPR043215

---

## Summary

Rabbit uteroglobin (SCGB1A1/UGB, P02779) is the **founding member of the secretoglobin (SCGB) superfamily** — a small, secreted, progesterone-inducible protein first isolated from the uterine fluid of early-pregnant rabbits. Its **primary molecular function is not catalytic or transport-based in the classical sense, but rather the reversible binding and sequestration of small hydrophobic ligands** inside a central, enclosed hydrophobic cavity. This cavity is formed by the assembly of two four-α-helix monomers into an **antiparallel, disulfide-linked homodimer**, a quaternary architecture resolved to atomic detail (1.34 Å) by X-ray crystallography. The protein binds progesterone with moderate affinity (Kd ≈ 4.1 × 10⁻⁷ M) and the progesterone metabolite 5α-pregnane-3,20-dione with ~3-fold higher affinity, while also accommodating retinoids, polychlorinated biphenyls (PCBs), phospholipids, and prostaglandins.

Functionally, uteroglobin acts **extracellularly** — on mucosal surfaces and in body fluids (uterine lumen, blood, urine) — as an **anti-inflammatory immunomodulator**. Its mechanism converges on the phospholipase A2 (PLA2)–eicosanoid–NF-κB axis: it inhibits secretory PLA2 (sPLA2) activity, sequesters pro-inflammatory lipid mediators such as prostaglandin F2α (PGF2α) within its hydrophobic cavity (thereby blocking PGF2α–FP receptor signaling, NF-κB activation, and COX-2 induction), and signals through the lipoxin A4/formyl-peptide ALX receptor to antagonize serum-amyloid-A-driven inflammation. In the rabbit specifically, uteroglobin expression is induced by progesterone in the endometrium and is dynamically regulated in the fetal lung, where its abundance is inversely correlated with prostaglandin levels — consistent with a role in maintaining uterine quiescence and protecting pulmonary surfactant phospholipids from PLA2 hydrolysis.

Importantly, the investigation clarified that the anti-inflammatory activity resides in the **intact folded dimer**, not in the short "antiflammin" sequence motif that was historically derived from uteroglobin and lipocortin-I; independent studies showed those nonapeptides lack genuine PLA2-inhibitory or anti-inflammatory activity. Across evolution, the disulfide-linked homodimer enclosing a hydrophobic cavity is the conserved ancestral functional unit of subfamily A secretoglobins, stabilized by invariant cysteines and a conserved internal Lys–Asp salt bridge. The physiological importance of the protein is demonstrated by gene-knockout mice, which develop an IgA-nephropathy-like phenotype linked to uteroglobin's additional ability to bind fibronectin and prevent pathological aggregation.

---

## Gene / Protein Identity Verification

The target was verified against all mandatory criteria before and throughout the investigation:

| Criterion | UniProt Specification | Literature Confirmation |
|-----------|----------------------|-------------------------|
| Gene symbol matches protein | SCGB1A1 = Uteroglobin | Confirmed: "founding member of a growing superfamily of proteins called Secretoglobin (Scgb)" [PMID: 17916741] |
| Organism | *Oryctolagus cuniculus* (Rabbit) | Confirmed: "Isolated from the uterus of rabbits during early pregnancy" [PMID: 17916741] |
| Protein family / domains | Secretoglobin / Uteroglobin (PF01099) | Confirmed: rabbit UG is the subfamily-A founder [PMID: 11193762] |

The literature for rabbit uteroglobin is **abundant and unambiguous** — this is one of the most extensively characterized small secreted proteins, with a high-resolution crystal structure, biochemical ligand-binding data, and genetic loss-of-function models. No gene-symbol ambiguity problem was encountered. The report that follows is grounded in primary structural, biochemical, and physiological studies.

---

## Key Findings

### Finding 1 — Uteroglobin is a secreted progesterone-binding protein and the founding secretoglobin

Rabbit uteroglobin was originally isolated as the dominant protein of rabbit uterine fluid during the preimplantation phase of early pregnancy, which is why it also carries the historical name **"blastokinin."** Quantitative equilibrium-binding studies established that it binds progesterone with relatively high affinity (**Kd = 4.1 × 10⁻⁷ M**) and binds the 5α-reduced progesterone metabolite **5α-pregnane-3,20-dione with ~3-fold higher affinity (Kd = 1.3 × 10⁻⁷ M)**, whereas estradiol binds only non-specifically and with very low affinity [PMID: 11093]. This established that the binding pocket is tuned for reduced, planar/hydrophobic steroid ligands rather than aromatic estrogens.

Uteroglobin is the **founding member of the secretoglobin (Scgb) superfamily** — a fact that anchors its classification and its relationship to homologues such as the human Clara cell 10-kDa protein (CC10/CCSP), mammaglobin, and lipophilins [PMID: 17916741]. This founder status matters functionally: the architecture and ligand-sequestering behavior first defined in rabbit uteroglobin became the template for understanding the entire family.

> *"Uteroglobin had a relatively high affinity for progesterone (KD=4.1 X 10(-7)M) but a threefold higher affinity for 5alpha-pregnane-3,20-dione (KD=1.3 X 10(-7)M)."* [[PMID: 11093](https://pubmed.ncbi.nlm.nih.gov/11093/)]

### Finding 2 — The protein is a disulfide-linked antiparallel homodimer enclosing an internal hydrophobic cavity

The structural basis of ligand binding is a **homodimer of two four-α-helix monomers aligned in antiparallel fashion and covalently joined by two intermolecular disulfide bridges**. The refined 1.34 Å crystal structure of oxidized rabbit uteroglobin shows that this assembly encloses a **closed central hydrophobic cavity** large enough to hold roughly 14 water molecules (~15.6 Å long × 9 Å wide) [PMID: 3656405]. This enclosed, boat-shaped cavity is the physical basis for sequestering hydrophobic ligands away from the aqueous environment.

Molecular modeling built on the homologous human protein's crystal structure localized the ligand-binding site specifically to the space **between helix-3 and helix-3′ of the two monomers**, into which hydrophobic ligands such as progesterone, PCBs, and retinol can "slip" [PMID: 11193750]. The dimeric, cavity-enclosing design is therefore not incidental — it is the functional heart of the molecule.

> *"In the core of the dimeric protein molecule, between the two monomers that are held together by two disulfide bridges, we have observed a closed cavity."* [[PMID: 3656405](https://pubmed.ncbi.nlm.nih.gov/3656405/)]
> *"Uteroglobin is a dimer and its secondary structure consists of four alpha-helices per monomer that align in an anti-parallel fashion."* [[PMID: 3656405](https://pubmed.ncbi.nlm.nih.gov/3656405/)]

### Finding 3 — Uteroglobin is an extracellular anti-inflammatory protein that inhibits secretory PLA2 and sequesters pro-inflammatory lipid mediators

The dominant physiological role of uteroglobin is **anti-inflammatory immunomodulation carried out extracellularly**. Two complementary mechanisms operate:

1. **Enzyme inhibition:** uteroglobin inhibits soluble/secretory phospholipase A2 (sPLA2) activity, the rate-limiting enzyme that liberates arachidonic acid for eicosanoid synthesis [PMID: 17916741].
2. **Ligand sequestration:** it binds and sequesters hydrophobic ligands — progesterone, retinols, PCBs, phospholipids, and prostaglandins [PMID: 17916741].

The sequestration mechanism was demonstrated with molecular precision for prostaglandin F2α: uteroglobin **binds and sequesters PGF2α into its central hydrophobic cavity, preventing the FP receptor–PGF2α interaction**, which in turn suppresses FP-mediated NF-κB activation and cyclooxygenase-2 (COX-2) gene expression [PMID: 16061484]. This directly links the structural cavity (Finding 2) to a signaling outcome: by removing the lipid ligand from circulation, uteroglobin shuts down a pro-inflammatory transcriptional program.

A receptor-level mechanism was also identified: uteroglobin is a ligand of the **lipoxin A4 / formyl-peptide ALX receptor**, and this interaction inhibits serum-amyloid-A (SAA)-driven responses, attenuating PLA2 activation and cellular chemotaxis [PMID: 24782597]. This places uteroglobin within pro-resolution/anti-inflammatory receptor signaling as well as acting as a soluble scavenger.

> *"It inhibits soluble phospholipase A(2) activity and binds and perhaps sequesters hydrophobic ligands such as progesterone, retinols, polychlorinated biphenyls, phospholipids, and prostaglandins."* [[PMID: 17916741](https://pubmed.ncbi.nlm.nih.gov/17916741/)]
> *"uteroglobin inhibits FP-mediated NF-kappaB activation and cyclooxygenase-2 gene expression by binding and most likely by sequestering PGF2alpha into its central hydrophobic cavity..."* [[PMID: 16061484](https://pubmed.ncbi.nlm.nih.gov/16061484/)]
> *"Uteroglobin's interaction with ALX resulted in the inhibition of SAA responses, such as attenuation of phospholipase A2 activation and cellular chemotaxis."* [[PMID: 24782597](https://pubmed.ncbi.nlm.nih.gov/24782597/)]

### Finding 4 — Rabbit uteroglobin is a progesterone-induced endometrial secretory product with broad mucosal localization

Expression of the rabbit *ug* gene is **induced by progesterone in the endometrium**, primarily through binding of the progesterone receptor (PR) to the distal region of the *ug* promoter, with additional progesterone-dependent factors (SOX17, E-box-binding TRBPs) conferring tissue specificity [PMID: 17427959; PMID: 9989939]. **Prolactin further augments progesterone-dependent transcription** via the RUSH/SMARCA3 transcription factor binding a promoter element at −126/−121 [PMID: 12198246].

Beyond the uterus, uteroglobin is expressed by the **mucosal epithelia of virtually all organs that communicate with the external environment** — most notably airway Clara/club cells — and is present in blood, urine, and other body fluids [PMID: 17916741]. This broad secretory distribution establishes uteroglobin as a general mucosal-surface protective protein, not merely a reproductive one. Its localization — **secreted into luminal/extracellular fluids on mucosal surfaces** — is exactly where its anti-PLA2 and lipid-sequestering functions are needed.

> *"The transcription of the uteroglobin gene (ug) is induced by progesterone in the rabbit endometrium, primarily through the binding of the progesterone receptor to the distal region of the ug promoter."* [[PMID: 17427959](https://pubmed.ncbi.nlm.nih.gov/17427959/)]
> *"The mucosal epithelia of virtually all organs that communicate with the external environment express UG, and it is present in the blood, urine, and other body fluids."* [[PMID: 17916741](https://pubmed.ncbi.nlm.nih.gov/17916741/)]

### Finding 5 — Uteroglobin binds fibronectin and prevents pathological IgA–fibronectin deposition (genetic loss-of-function evidence)

The physiological necessity of uteroglobin was demonstrated by gene-knockout (UG-KO) and antisense-transgenic (UG-AS) mice, which develop an **IgA-nephropathy-like phenotype** — microhematuria, albuminuria, and renal glomerular deposition of IgA, fibronectin (Fn), collagen, and C3 complement [PMID: 11193759]. Mechanistically, uteroglobin forms **Fn–UG heteromers** that are detectable in the plasma of normal mice but absent in UG-KO mice, and coadministration of UG+Fn or UG+IgA to knockout mice prevents the glomerular deposits [PMID: 11193759]. This reveals a second ligand-binding function — binding fibronectin to block Fn–Fn and IgA–Fn aggregation — and provides the clearest genetic evidence that uteroglobin performs an essential homeostatic role in vivo.

> *"Both the UG-KO and UG-AS mice develop immunoglobulin A (IgA) nephropathy (IgAN)..."* [[PMID: 11193759](https://pubmed.ncbi.nlm.nih.gov/11193759/)]
> *"...the formation of Fn-UG heteromers in vitro and these heteromers are detectable in the plasma of normal mice, but not UG-KO mice."* [[PMID: 11193759](https://pubmed.ncbi.nlm.nih.gov/11193759/)]

### Finding 6 — Uteroglobin founds the secretoglobin superfamily; conserved cysteines and a salt-bridge define the fold

Rabbit uteroglobin is the founder of a mammalian family of **>20 small, secreted, rarely glycosylated dimeric proteins** expressed mainly in mucosal tissues. Phylogeny divides the family into five subfamilies (A–E); **subfamily A (uteroglobin and its orthologues) forms antiparallel homodimers via two intermolecular disulfide bonds** [PMID: 11193762]. Across all family members, only two cysteines and a single central lysine are strictly conserved; in known uteroglobin structures this lysine forms an **exposed salt bridge with an almost universally conserved aspartate** — an invariant structural signature of the fold [PMID: 11193762]. The human orthologues (CC10, lipophilins A/B, lacryglobin, mammaglobin, lymphoglobin) cluster on chromosome 11q12.2. The evolutionary conservation of the disulfide-linked dimer with its hydrophobic cavity confirms that this architecture — not any single later-evolved feature — is the ancestral functional unit.

> *"Subfamily A contains rabbit uteroglobin and its orthologues from various species; most of these have been described to form antiparallel homodimers via two intermolecular disulfide bonds."* [[PMID: 11193762](https://pubmed.ncbi.nlm.nih.gov/11193762/)]
> *"...only one central lysine is conserved in all family members. In the known uteroglobin structures, this lysine forms an exposed salt bridge with an aspartate side chain..."* [[PMID: 11193762](https://pubmed.ncbi.nlm.nih.gov/11193762/)]

### Finding 7 — In the rabbit, uteroglobin expression tracks an anti-eicosanoid, PLA2-inhibitory role in uterus and fetal lung

Rabbit-specific expression data tie the biochemistry to physiology. The *ug* gene is expressed in the uterus throughout gestation with a **precipitous decline just before parturition**, and is **dramatically up-regulated in the fetal lung with increasing gestational age** (shown by RT-PCR, in situ hybridization, immunofluorescence, and radioimmunoassay) [PMID: 7615804]. In the developing fetal lung, uteroglobin levels show an **inverse relationship with the prostaglandins PGE2 and PGF2α** (and a positive correlation with leukotriene C4) [PMID: 7615804]. The authors characterize uteroglobin as a cytokine-like, PLA2-inhibitory protein proposed to **maintain uterine quiescence / prevent premature labor** and to **protect the respiratory organ by preventing hydrolysis of surfactant phospholipids by a lung-specific phospholipase A2** [PMID: 7615804]. This in vivo correlation is direct rabbit evidence for the anti-eicosanoid function inferred from biochemistry.

> *"...there is an inverse relationship between the levels of UG, PGE2, and PGF2 alpha, a positive correlation was found in that of UG and leukotriene C4 in the fetal lung"* [[PMID: 7615804](https://pubmed.ncbi.nlm.nih.gov/7615804/)]
> *"This latter function of UG is suggested to be accomplished by preventing hydrolysis of surfactant phospholipids by a lung-specific phospholipase A2."* [[PMID: 7615804](https://pubmed.ncbi.nlm.nih.gov/7615804/)]

### Finding 8 — The anti-inflammatory activity resides in the intact folded dimer, not in the "antiflammin" sequence motif

A historically important correction: short **"antiflammin" nonapeptides (P1/P2)** derived from a region of sequence similarity shared between uteroglobin and lipocortin-I were once proposed as the active PLA2-inhibitory motif. Independent testing refuted this. The peptides **do NOT inhibit porcine pancreatic PLA2** across 0.5–50 µM, do not reduce PGE2/LTC4 release from stimulated cells, and show no anti-inflammatory activity in carrageenan-induced rat paw oedema [PMID: 2141575]. A separate study found the peptides fail to inhibit PLA2-induced oedema, acting instead weakly on mast-cell/histamine responses [PMID: 7535228], and a related analysis concluded antiflammins act on transglutaminase rather than directly on PLA2 [PMID: 16399636]. The functional implication is clear: uteroglobin's PLA2-inhibitory and ligand-sequestering activities are **emergent properties of the correctly folded, disulfide-linked dimer and its hydrophobic cavity**, not of a linear peptide epitope.

> *"Porcine pancreatic phospholipase A2 was not inhibited at concentrations of 0.5-50 microM."* [[PMID: 2141575](https://pubmed.ncbi.nlm.nih.gov/2141575/)]
> *"...the peptides were not able to inhibit phospholipase A2-induced oedema"* [[PMID: 7535228](https://pubmed.ncbi.nlm.nih.gov/7535228/)]

---

## Mechanistic Model / Interpretation

The findings integrate into a single coherent model in which **structure dictates function**: a dimeric hydrophobic-ligand "sponge" acts as an extracellular brake on inflammatory lipid signaling.

```
          PROGESTERONE (in uterus)          Mucosal epithelium
                 │                            (airway Clara cells,
                 ▼                             endometrium, etc.)
         PR binds distal ug promoter               │
         (+ SOX17, TRBPs; prolactin/RUSH)          │  secretion
                 │                                  ▼
                 ▼                          ┌──────────────────────┐
        ug gene TRANSCRIPTION ───────────▶  │  UTEROGLOBIN DIMER   │
                                            │  4-helix × 2 monomers│
                                            │  2 S–S bridges       │
                                            │  central hydrophobic │
                                            │  cavity (helix3/3')  │
                                            └──────────┬───────────┘
                                                       │ acts EXTRACELLULARLY
            ┌──────────────────────┬───────────────────┼────────────────────┐
            ▼                      ▼                    ▼                    ▼
   Inhibits secretory      Sequesters PGF2α     Binds ALX/lipoxin     Binds fibronectin
   PLA2 (sPLA2)            into cavity →         receptor →            → blocks Fn–Fn &
   → less arachidonic      blocks FP receptor    antagonizes SAA-      IgA–Fn aggregation
   acid liberated          → ↓NF-κB, ↓COX-2      driven PLA2 &         → prevents IgA
                                                 chemotaxis            nephropathy (KO)
            └──────────────────────┴───────────────────┴────────────────────┘
                                   │
                                   ▼
             NET EFFECT: ↓ eicosanoid production, ↓ inflammation,
             protection of surfactant phospholipids, uterine quiescence
```

**Classification of function.** Uteroglobin is best described not as an enzyme or a membrane transporter, but as a **secreted ligand-sequestering / enzyme-inhibitory immunomodulator**. The "reaction" it influences is upstream eicosanoid biogenesis: it inhibits sPLA2 (the enzyme that releases arachidonic acid from membrane phospholipids) and removes downstream lipid products (prostaglandins) from the system by physical encapsulation. Its "substrate specificity" is therefore for **small, hydrophobic, roughly planar ligands** — reduced progestins > progesterone ≫ estrogens, plus retinoids, PCBs, phospholipids and prostaglandins — defined by the geometry and chemistry of the inter-monomer cavity.

**Site of action.** The protein performs its function **extracellularly**: in the uterine lumen, in airway lining fluid, and in systemic fluids (plasma, urine). It is synthesized in and secreted from mucosal epithelial cells (endometrial glands, airway Clara/club cells).

**Pathway placement.** Uteroglobin sits at the apex of the **PLA2 → arachidonic acid → COX-2 → prostaglandin → FP receptor → NF-κB** inflammatory cascade and dampens it at multiple nodes (enzyme inhibition, ligand sequestration, receptor signaling via ALX). A parallel, distinct function is scavenging fibronectin to prevent pathological immune-complex aggregation in the kidney.

| Functional axis | Molecular action | Cellular/anatomic location | Key evidence |
|-----------------|------------------|----------------------------|--------------|
| Steroid binding | Binds progesterone / 5α-pregnanedione in cavity | Uterine fluid (secreted) | [PMID: 11093] |
| Anti-eicosanoid | Inhibits sPLA2; sequesters PGF2α; ↓NF-κB/COX-2 | Extracellular / mucosal | [PMID: 17916741], [PMID: 16061484] |
| Receptor signaling | Ligand of ALX/lipoxin receptor; ↓SAA inflammation | Cell surface (immune cells) | [PMID: 24782597] |
| Anti-aggregation | Binds fibronectin; prevents IgA–Fn deposition | Plasma / renal glomerulus | [PMID: 11193759] |
| Structural basis | Disulfide-linked antiparallel 4-helix homodimer | N/A (intrinsic) | [PMID: 3656405], [PMID: 11193750] |

---

## Evidence Base

| PMID | Title (abbreviated) | Contribution | Strength |
|------|--------------------|--------------|----------|
| [11093](https://pubmed.ncbi.nlm.nih.gov/11093/) | *Interaction of uteroglobin with progesterone, 5α-pregnane-3,20-dione and estrogens* | Quantitative ligand-binding affinities (Kd) | Primary, biochemical — high |
| [3656405](https://pubmed.ncbi.nlm.nih.gov/3656405/) | *Refinement of the C222₁ crystal form of oxidized uteroglobin at 1.34 Å* | Atomic-resolution rabbit UG structure; dimer, disulfides, cavity | Primary, structural — very high |
| [11193750](https://pubmed.ncbi.nlm.nih.gov/11193750/) | *Crystal structure of recombinant human uteroglobin and molecular modeling of ligand binding* | Localizes ligand site between helix-3/3′ | Primary, structural/modeling — high |
| [17916741](https://pubmed.ncbi.nlm.nih.gov/17916741/) | *Uteroglobin: a steroid-inducible immunomodulatory protein that founded the Secretoglobin superfamily* | Authoritative review; PLA2 inhibition, sequestration, mucosal localization | Review — high |
| [16061484](https://pubmed.ncbi.nlm.nih.gov/16061484/) | *Uteroglobin inhibits PGF2α receptor-mediated expression of pro-inflammatory lipid-mediator genes* | Mechanism: cavity sequestration of PGF2α → ↓NF-κB/COX-2 | Primary, mechanistic — high |
| [24782597](https://pubmed.ncbi.nlm.nih.gov/24782597/) | *Uteroglobin, a possible ligand of the lipoxin receptor, inhibits SAA-driven inflammation* | Identifies ALX receptor mechanism | Primary — moderate/high |
| [17427959](https://pubmed.ncbi.nlm.nih.gov/17427959/) | *SOX17 in transcriptional control of the uteroglobin gene in rabbit endometrium* | Progesterone/PR-driven rabbit endometrial expression | Primary — high |
| [12198246](https://pubmed.ncbi.nlm.nih.gov/12198246/) | *RUSH mediates prolactin augmentation of progesterone-dependent gene expression* | Prolactin/RUSH transcriptional control | Primary — high |
| [11193759](https://pubmed.ncbi.nlm.nih.gov/11193759/) | *Physiological function of uteroglobin by gene-knockout and antisense-transgenic approaches* | Genetic loss-of-function; fibronectin binding; IgA nephropathy | Primary, genetic — high |
| [11193762](https://pubmed.ncbi.nlm.nih.gov/11193762/) | *All human genes of the uteroglobin family localized on chromosome 11q12.2* | Family/phylogeny; conserved Cys and Lys–Asp salt bridge | Primary, bioinformatic — high |
| [7615804](https://pubmed.ncbi.nlm.nih.gov/7615804/) | *Uteroglobin expression in rabbit uterus and fetal lung; relationship to eicosanoids* | Rabbit in vivo inverse UG–prostaglandin correlation | Primary — high |
| [2141575](https://pubmed.ncbi.nlm.nih.gov/2141575/) | *'Antiflammins': two nonapeptides have no PLA2-inhibitory/anti-inflammatory activity* | Refutes antiflammin-peptide mechanism | Primary — high |
| [7535228](https://pubmed.ncbi.nlm.nih.gov/7535228/) | *Effect of nonapeptide fragments on oedema and mast cell degranulation* | Confirms peptides do not block PLA2-driven oedema | Primary — moderate |
| [16399636](https://pubmed.ncbi.nlm.nih.gov/16399636/) | *Effects of antiflammins on transglutaminase and PLA2 activation* | Antiflammins act on transglutaminase, not PLA2 directly | Primary — moderate |

**Supporting cross-species corroboration.** The functional conservation of this protein is reinforced by work on its orthologues: rat Clara cell 17-kDa protein shares 55.7% sequence identity and the same disulfide-bonded antiparallel dimer with an internal hydrophobic cavity able to accommodate progesterone [PMID: 1560460]; human CC10 (CC16) is a secretory PLA2 inhibitor with a mucosal expression pattern "very similar, if not identical" to rabbit UG [PMID: 8227325]; and recombinant CC10/CC16 proteins inhibit the cPLA2/COX2 and NF-κB pathways in airway models [PMID: 32172202; PMID: 25716019]. These are consistent with — but secondary to — the rabbit-specific evidence above.

---

## Limitations and Knowledge Gaps

1. **In vivo loss-of-function is from mouse, not rabbit.** The definitive genetic phenotype (IgA nephropathy, fibronectin binding) comes from UG-knockout mice [PMID: 11193759]; a rabbit knockout does not exist. Function in the rabbit is inferred from biochemistry, structure, and expression correlations [PMID: 7615804].

2. **sPLA2 inhibition mechanism is not fully resolved.** Whether uteroglobin inhibits sPLA2 by direct enzyme binding, by sequestering phospholipid substrate, or both, remains partly unsettled — and the magnitude/physiological relevance of direct inhibition has been debated. The antiflammin episode [PMID: 2141575] shows how easily the mechanism was mis-assigned.

3. **The endogenous physiological ligand in the rabbit uterus is not definitively established.** Progesterone binding is real but of modest affinity (µM Kd) [PMID: 11093]; whether progesterone, a progesterone metabolite, a prostaglandin, or a phospholipid is the principal in vivo cargo at relevant concentrations is not fully resolved.

4. **ALX-receptor signaling needs rabbit-specific confirmation.** The lipoxin/ALX receptor interaction [PMID: 24782597] was defined in non-rabbit systems; its contribution to rabbit physiology is untested.

5. **Quantitative structure–function links are incomplete.** While the cavity and the conserved Lys–Asp salt bridge are defined [PMID: 3656405; PMID: 11193762], site-directed mutants that would prove which residues are essential for each function (ligand binding vs. PLA2 inhibition vs. fibronectin binding) are limited.

---

## Proposed Follow-up Experiments / Actions

1. **Rabbit-specific ligand quantification.** Use isothermal titration calorimetry or competition binding on recombinant rabbit UG to directly compare affinities for progesterone, 5α-pregnane-3,20-dione, PGF2α, PGE2, retinoids, and phospholipids under physiological conditions, defining the true in vivo cargo hierarchy.

2. **Structure-guided mutagenesis.** Mutate cavity-lining residues (helix-3/3′), the conserved intermolecular cysteines, and the invariant Lys–Asp salt-bridge pair, then assay each mutant for (a) dimer formation, (b) steroid binding, (c) sPLA2 inhibition, and (d) fibronectin binding — to deconvolve which structural features drive which function.

3. **Mechanism of sPLA2 inhibition.** Use enzyme kinetics with defined substrate presentations (micelles vs. vesicles) plus co-crystallization or crosslinking to determine whether UG inhibits sPLA2 by direct protein–protein contact or by substrate sequestration.

4. **Rabbit fetal-lung causal test.** Beyond the existing correlative data [PMID: 7615804], apply recombinant rabbit UG (or neutralizing antibody) in rabbit lung explants/organoids and measure PGE2/PGF2α output and surfactant phospholipid integrity to establish causality for the surfactant-protection hypothesis.

5. **ALX-receptor dependence.** Test whether UG's anti-chemotactic/anti-SAA effects are abolished by ALX/FPR2 antagonism or knockdown in rabbit (or rabbit-cell) systems to confirm the receptor-mediated arm of the mechanism.

6. **Reproductive-tract phenotyping.** Given progesterone-induced endometrial expression and the pre-parturition decline [PMID: 7615804; PMID: 17427959], examine whether UG modulation affects uterine prostaglandin tone and timing of parturition — testing the "uterine quiescence" hypothesis directly.

---

## Conclusion

Rabbit uteroglobin (SCGB1A1/UGB, P02779) is a secreted, progesterone-inducible, disulfide-linked antiparallel four-helix **homodimer** whose central hydrophobic cavity reversibly binds and sequesters small hydrophobic ligands (progesterone, Kd ≈ 4 × 10⁻⁷ M; reduced progestins, retinoids, PCBs, phospholipids, and prostaglandins). It is **not an enzyme or transporter** but the founding secretoglobin and an **extracellular anti-inflammatory immunomodulator** acting on mucosal surfaces and in body fluids. It dampens the PLA2–eicosanoid–NF-κB pathway by inhibiting secretory PLA2, sequestering lipid mediators such as PGF2α (blocking FP-receptor/NF-κB/COX-2 signaling), and signaling through the lipoxin/ALX receptor; it additionally binds fibronectin in plasma to prevent pathological IgA–fibronectin deposition. This anti-inflammatory activity is a property of the intact folded dimer, not of the discredited "antiflammin" peptide motif.


## Artifacts

- [OpenScientist final report](SCGB1A1-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](SCGB1A1-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:17916741
2. PMID:11193762
3. PMID:3656405
4. PMID:11193750
5. PMID:16061484
6. PMID:24782597
7. PMID:17427959
8. PMID:9989939
9. PMID:12198246
10. PMID:11193759
11. PMID:7615804
12. PMID:2141575
13. PMID:7535228
14. PMID:16399636
15. PMID:1560460
16. PMID:8227325
17. PMID:32172202
18. PMID:25716019