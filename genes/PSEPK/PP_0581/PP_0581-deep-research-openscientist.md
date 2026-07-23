---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-23T10:01:40.041487'
end_time: '2026-07-23T10:28:00.559668'
duration_seconds: 1580.52
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_0581
  gene_symbol: PP_0581
  uniprot_accession: Q88QB3
  protein_description: 'SubName: Full=3-oxoacyl-(Acyl-carrier-protein) reductase {ECO:0000313|EMBL:AAN66208.1};'
  gene_info: OrderedLocusNames=PP_0581 {ECO:0000313|EMBL:AAN66208.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the short-chain dehydrogenases/reductases (SDR)
  protein_domains: KR_dom. (IPR057326); NAD(P)-bd_dom_sf. (IPR036291); Sc_DH/Rdtase_CS.
    (IPR020904); SDR_fam. (IPR002347); adh_short_C2 (PF13561)
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
citation_count: 11
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PP_0581-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PP_0581-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88QB3
- **Protein Description:** SubName: Full=3-oxoacyl-(Acyl-carrier-protein) reductase {ECO:0000313|EMBL:AAN66208.1};
- **Gene Information:** OrderedLocusNames=PP_0581 {ECO:0000313|EMBL:AAN66208.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the short-chain dehydrogenases/reductases (SDR)
- **Key Domains:** KR_dom. (IPR057326); NAD(P)-bd_dom_sf. (IPR036291); Sc_DH/Rdtase_CS. (IPR020904); SDR_fam. (IPR002347); adh_short_C2 (PF13561)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_0581" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_0581' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_0581** (gene ID: PP_0581, UniProt: Q88QB3) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: PP_0581 (Q88QB3) — A High-Molecular-Weight FabG β-Ketoacyl-Thioester Reductase in *Pseudomonas putida* KT2440

## Summary

**PP_0581 (UniProt Q88QB3) encodes a soluble, cytoplasmic, NAD(H)-dependent β-ketoacyl (3-oxoacyl) thioester reductase of the short-chain dehydrogenase/reductase (SDR) superfamily.** The catalyzed reaction is the stereospecific reduction of a 3-oxoacyl (β-ketoacyl) thioester to the corresponding (R)-3-hydroxyacyl thioester, using NADH as the hydride donor. Critically, this protein is **NOT** the essential housekeeping type-II fatty acid synthase (FAS-II) FabG that performs the ketoreduction step of every fatty-acid elongation cycle. That housekeeping role in *P. putida* KT2440 belongs to the separate, canonical 246-residue enzyme PP_1914, encoded in the classical *fabD–fabG–acpP* operon.

Instead, PP_0581 is a **high-molecular-weight FabG (HMwFabG, also called the FabG4-type)** — a 457-residue, ~47.8 kDa protein roughly double the size of a canonical FabG. It has a diagnostic two-domain architecture: an N-terminal "flavodoxin-type" domain fused to a C-terminal SDR ketoreductase (oxoreductase) domain. This architecture is the structural hallmark of the phylogenetically distinct HMwFabG group prototyped by *Mycobacterium tuberculosis* FabG4 (Rv0242c). An AlphaFold model (AF-Q88QB3-F1, global mean pLDDT 94.4) confirms a confidently folded two-domain protein with a geometrically competent SDR catalytic triad (Ser350–Tyr363–Lys367) and an NAD-selective aspartate (Asp251) cofactor-specificity determinant, consistent with the NADH preference characteristic of the FabG4/HMwFabG class.

Functionally, PP_0581 sits at the head of a **compact, self-contained, AraC-regulated acyl-CoA/β-oxidation-type metabolic module**. Genomic-context analysis places it in a tightly spaced, co-directional operon (PP_0581–PP_0580–PP_0579) that is divergently transcribed from a thiolase gene (PP_0582) and controlled by an adjacent AraC-family regulator (PP_0583). Its immediate neighbor PP_0580 is a MaoC-domain (R)-specific enoyl-CoA hydratase — the enzyme family that channels (R)-3-hydroxyacyl-CoA between β-oxidation and polyhydroxyalkanoate (PHA) metabolism in *Pseudomonas*. The absence of a co-localized transporter or acyl-CoA synthetase indicates the physiological substrate is an **intracellular CoA-thioester intermediate**, and the dedicated AraC regulator implies an inducible, substrate-specific catabolic function rather than constitutive housekeeping fatty-acid synthesis. **Confidence is high** for the enzyme chemistry, family, cofactor class, and cytoplasmic localization (structure/sequence/genomic evidence), and **moderate** for the exact physiological substrate, which has not been experimentally determined and remains the principal knowledge gap.

---

## Target Identity Verification

| Property | Value |
|---|---|
| UniProt | Q88QB3 (Q88QB3_PSEPK), TrEMBL, unreviewed |
| Locus | PP_0581 (OrderedLocusNames); GenBank AAN66208.1 |
| Organism | *Pseudomonas putida* KT2440 (ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950); TaxID 160488 |
| Length / MW | 457 aa / ~47.8 kDa |
| Genome position | chromosome, complement(677,644–679,017) |
| KEGG orthology | K00059, 3-oxoacyl-[ACP] reductase, EC 1.1.1.100 |
| Family | SDR superfamily; NCBIfam **PRK08261** (HMwFabG model) |
| Domains | Two NAD(P)-binding Rossmann domains (Gene3D 3.40.50.720 ×2); C-terminal ketoreductase (SMART, res 221–394); Pfam adh_short_C2 (PF13561); PROSITE ADH_SHORT (PS00061) |
| PANTHER | PTHR42760:SF78 "3-oxoacyl-[ACP] reductase **[NADH]**" |

The gene symbol, organism, protein family, and domain content in the provided UniProt record are internally consistent and were confirmed against KEGG, InterPro/Gene3D, and NCBIfam. "PP_0581" is an unambiguous ordered-locus name specific to KT2440, so there is no cross-organism symbol ambiguity. The only nuance is that the generic annotation "3-oxoacyl-ACP reductase / FabG" **understates** the protein's true identity as a *high-molecular-weight* FabG paralog.

---

## Key Findings

### Finding 1: PP_0581 is a high-molecular-weight FabG (HMwFabG/FabG4-type), not the housekeeping FAS-II FabG

PP_0581 is 457 amino acids long (~47.8 kDa), roughly double the length of a canonical FabG (~245 residues, ~25 kDa). This size difference reflects a fundamentally different domain organization. Structural-domain classifiers (Gene3D) assign **two** NAD(P)-binding Rossmann-fold domains (CATH 3.40.50.720 × 2): an N-terminal domain spanning roughly residues 1–215 and a C-terminal SDR ketoreductase domain (SMART ketoreductase 221–394; Pfam adh_short_C2, PF13561). This tandem "N-terminal flavodoxin-type domain + C-terminal oxoreductase domain" arrangement is the defining, diagnostic feature of the HMwFabG group.

The HMwFabGs form a phylogenetically separate clade distinct from the low-molecular-weight housekeeping FabGs. As established for the *Mycobacterium tuberculosis* prototype FabG4, "HMwFabGs (high-molecular-weight FabG) form a phylogenetically separate group of FabG enzymes. FabG4, an HMwFabG from *Mycobacterium tuberculosis*, contains two distinct domains, an N-terminal 'flavodoxin-type' domain and a C-terminal oxoreductase domain" ([PMID: 23163771](https://pubmed.ncbi.nlm.nih.gov/23163771/)). PP_0581 reproduces exactly this architecture. Independent classifiers corroborate the assignment: PANTHER places PP_0581 in PTHR42760:SF78, "3-oxoacyl-[ACP] reductase [NADH]," and the NCBIfam model PRK08261 — the specific HMwFabG model — is matched.

Importantly, HMwFabGs are structurally and cofactor-distinct from the canonical enzymes. Work on *Acinetobacter baumannii* reductases describes the "high-molecular weight 3-oxoacyl-ACP reductase (HMwFabG), showing differences in structure and coenzyme preference" ([PMID: 33782435](https://pubmed.ncbi.nlm.nih.gov/33782435/)), supporting the conclusion that PP_0581 does not fulfill the housekeeping FabG role.

The genuine housekeeping FAS-II FabG in KT2440 is a separate protein: the 246-residue PP_1914, encoded in the classical fatty-acid synthesis operon (PP_1913 *fabD*, malonyl-CoA:ACP transacylase / PP_1914 *fabG* / PP_1915 *acpP*, acyl carrier protein). KT2440 carries five K00059-annotated (3-oxoacyl-ACP reductase) paralogs — PP_0581, PP_1852 (249 aa), PP_1914 (246 aa), PP_2540 (258 aa), and PP_2783 (245 aa) — but only PP_0581 is high-molecular-weight and genomically remote from the *fab* operon, further distinguishing it from the pack.

### Finding 2: PP_0581 has intact SDR catalytic machinery — a predicted NAD(H)-dependent β-ketoacyl reductase, cytoplasmic

The C-terminal SDR domain of PP_0581 contains all the canonical sequence motifs required for a functional short-chain dehydrogenase/reductase. The cofactor-binding Rossmann glycine motif (TGxxxGxG) is present as **V-T-G-A-A-R-G-I-G at residues 225–233**, and the SDR catalytic Tyr-x-x-x-Lys motif appears as **Y363-A-A-S-K367**. The upstream catalytic serine is in the ~S350/S352 region, completing the canonical SDR **Ser–Tyr–Lys catalytic triad**. The PROSITE ADH_SHORT signature (PS00061) and the Sc_DH/Rdtase conserved-site pattern (IPR020904) are both matched.

By homology to the FabG4 prototype — whose catalytic triad is Ser347/Tyr360/Lys364 — PP_0581 is predicted to reduce a β-ketoacyl (3-oxoacyl) thioester to the corresponding (R)-3-hydroxyacyl thioester using NAD(P)H, belonging to the EC 1.1.1.100 reaction family (oxidoreductase acting on the CH–OH/keto group, GO:0016616). The direct enzymatic characterization of FabG4 establishes both the reaction and the mechanism: "The enzyme exhibits ketoacyl CoA reductase activity by reducing acetoacyl CoA to 3-hydroxyacyl CoA in presence of NADH. Conserved catalytic triad Ser347, Tyr360, and Lys364 constitute the active site residues of the KAR domain" ([PMID: 21081168](https://pubmed.ncbi.nlm.nih.gov/21081168/)).

Two additional features refine the substrate and cofactor predictions. First, the FabG4 prototype accepts both CoA- and ACP-based substrates: "Structural data ACP inhibition studies indicate that FabG4 can accept both CoA- and ACP-based fatty-acyl substrates" ([PMID: 23163771](https://pubmed.ncbi.nlm.nih.gov/23163771/)). Second, the NADH cofactor preference is a defining feature of the class: "The enzyme requires NADH for β-ketoacyl reductase activity" ([PMID: 22750865](https://pubmed.ncbi.nlm.nih.gov/22750865/)), consistent with PP_0581's PANTHER "[NADH]" subfamily assignment.

Regarding localization, PP_0581 carries no annotated signal peptide and no predicted transmembrane region, consistent with a **soluble cytoplasmic enzyme** — the compartment where both fatty-acid and acyl-CoA metabolism occur.

### Findings 3 & 5: PP_0581 heads a compact, AraC-regulated acyl-CoA/β-oxidation-type module

Genomic-context analysis provides the strongest available evidence for the physiological role of PP_0581. The gene sits within a functionally coherent cluster on the KT2440 chromosome (around 676–681 kb):

| Locus | Product / annotation | Function in module |
|-------|---------------------|---------------------|
| PP_0579 | conserved hypothetical protein | co-operonic; unknown accessory |
| PP_0580 | MaoC-domain protein | (R)-specific enoyl-CoA hydratase |
| **PP_0581** | **HMwFabG reductase (this protein)** | **β-ketoacyl-CoA → (R)-3-hydroxyacyl-CoA** |
| PP_0582 | thiolase (acetyl-CoA C-acetyltransferase, K00626, EC 2.3.1.9) | thiolytic C–C cleavage / condensation |
| PP_0583 | AraC-family transcriptional regulator | inducible, substrate-specific control |

Precise coordinate analysis shows that PP_0581 (−strand, 677,644–679,017), PP_0580 (−strand, 676,790–677,641; only a 2-bp gap to PP_0581), and PP_0579 (−strand, 676,407–676,805; a 16-bp overlap with PP_0580) form a co-directional, tightly spaced operon transcribed in the order PP_0581 → PP_0580 → PP_0579. The thiolase PP_0582 (+strand, 679,114–680,391) is **divergently transcribed** just 96 bp from the PP_0581 start, and the AraC-family regulator PP_0583 (+strand, 680,481–681,260) lies immediately beyond it — the classic layout of an AraC-controlled divergent catabolic locus.

The wider genomic neighborhood is functionally unrelated — PP_0578 is a methyltransferase, PP_0584 is a chemotaxis methyl-accepting protein (MCP), and PP_0585–PP_0588 handle metal/copper homeostasis — so the metabolic module is confined to PP_0579–PP_0583.

The enzymatic logic of this cluster is decisive. A **thiolase + (R)-specific hydratase + β-ketoacyl reductase** trio is the enzymatic hallmark of a CoA-dependent β-oxidation-type / (R)-3-hydroxyacyl-CoA metabolic module. In *Pseudomonas*, MaoC-family (R)-hydratases specifically bridge β-oxidation and PHA biosynthesis: "MaoC is a new enoyl-CoA hydratase involved in supplying (R)-3-hydroxyacyl-CoA from the beta-oxidation pathway to PHA biosynthetic pathway" ([PMID: 12949091](https://pubmed.ncbi.nlm.nih.gov/12949091/)). The presence of PP_0580 as a co-operonic (R)-hydratase strongly defines the CoA-thioester pathway context of the PP_0581 reductase.

Two negative observations sharpen the interpretation. First, no cognate transporter or acyl-CoA synthetase is co-localized with the module, indicating the substrate is an **intracellular CoA-thioester intermediate** rather than an imported or newly activated fatty acid. Second, the dedicated adjacent AraC regulator implies an **inducible, substrate-specific catabolic operon** rather than constitutive housekeeping fatty-acid synthesis — reinforcing that PP_0581 is not the housekeeping FabG.

### Finding 4: AlphaFold confirms a folded two-domain HMwFabG with a competent SDR catalytic triad

The AlphaFold DB model AF-Q88QB3-F1 (v6) covers all 457 residues at very high confidence: **global mean pLDDT = 94.4, with 98% of residues at pLDDT > 70**. Crucially, both structural modules are well-folded rather than one being a disordered extension: the N-terminal domain (residues 1–215) has mean pLDDT 91.9, and the C-terminal SDR ketoreductase domain (216–457) has mean pLDDT 96.6. This directly confirms a genuine two-domain (N-terminal flavodoxin-type + C-terminal oxoreductase) HMwFabG architecture rather than a disordered N-terminal extension.

In the modeled active site, the catalytic triad is geometrically competent and adopts canonical SDR proton-relay geometry: **Tyr363-OH···Lys367-NZ = 4.29 Å** and **Ser350-OG···Tyr363-OH = 4.24 Å**. The YxxxK motif (Y363-AAS-K367) and the cofactor glycine-rich motif (VTGAARGIG, residues 225–233) are both positioned within the same C-terminal domain, and the conserved SDR asparagine (H-N-A-G, ~residues 301–304) is also present — consistent with a fully assembled, catalytically poised active site. This upgrades the catalytic assignment from motif-matching to structure-supported.

### Finding 6: An NAD-selective aspartate (Asp251) supports NADH over NADPH preference

The cofactor specificity of SDR/Rossmann enzymes is dictated by the residue at the C-terminus of the βB strand, roughly 18 residues downstream of the glycine-rich motif. In PP_0581 this position is an acidic aspartate — **Asp251** (in the context ...DVADVLLL**D251**VPQ...). An acidic residue at this canonical position hydrogen-bonds the 2′- and 3′-hydroxyls of the adenosine ribose and is the classical fingerprint of **NAD(+)-specific** SDR enzymes. NADP-specific enzymes instead carry a basic residue and a 2′-phosphate-binding pocket. The presence of Asp251 therefore predicts NAD(H) rather than NADPH dependence.

This structural determinant is fully concordant with two independent lines of evidence: the PANTHER subfamily classifier PTHR42760:SF78 ("3-oxoacyl-[ACP] reductase [NADH]") and the experimentally established NADH dependence of the FabG4/HMwFabG prototype ([PMID: 22750865](https://pubmed.ncbi.nlm.nih.gov/22750865/)). It also further distinguishes PP_0581 from the typically NADPH-using housekeeping FAS-II FabG. The other conserved SDR residues — the N-A-G asparagine motif (~residues 301–304), catalytic Ser350, Tyr363, and Lys367 — are all present, completing a canonical, NADH-selective SDR active site.

---

## Mechanistic Model / Interpretation

### The reaction

PP_0581 catalyzes the NADH-dependent ketoreduction step of a CoA-thioester (and possibly ACP-thioester) metabolic cycle:

```
        3-oxoacyl-thioester        (R)-3-hydroxyacyl-thioester
   R-CO-CH2-CO-S-CoA  +  NADH  ──►  R-CH(OH)-CH2-CO-S-CoA  +  NAD+
                                     │
              catalytic triad: Ser350 / Tyr363 / Lys367
              cofactor: NADH (Asp251 selects NAD over NADP)
```

Mechanistically, in the SDR proton relay: catalytic Tyr363 donates a proton to the developing alkoxide of the reduced substrate; Lys367 lowers the pKa of Tyr363 and binds the nicotinamide ribose; and Ser350 stabilizes and orients the substrate carbonyl. The AlphaFold model places these residues in canonical distance geometry (Tyr–Lys 4.29 Å, Ser–Tyr 4.24 Å), indicating a poised, functional active site.

### The pathway context

The genomic module assembles a complete CoA-thioester processing unit:

```
   AraC (PP_0583) ──regulates──►  [ divergent promoter region ]
                                          │
      ┌───────────────────────────────────┴──────────────────────────────┐
      │                                                                    │
  thiolase (PP_0582)              operon:  PP_0581 ─ PP_0580 ─ PP_0579
  acetyl-CoA C-acetyltransferase           reductase  (R)-hydratase  hyp.
  (K00626, EC 2.3.1.9)                      (this gene)  (MaoC)

   Combined enzymatic logic (β-oxidation / (R)-3-hydroxyacyl-CoA metabolism):

   acyl-CoA ──(dehydrogenase)──► trans-2-enoyl-CoA
                                     │
                        PP_0580 MaoC (R)-hydratase
                                     ▼
                          (R)-3-hydroxyacyl-CoA ◄── PP_0581 reductase
                                     │                (NADH)
                        [oxidation]  ▼
                          3-ketoacyl-CoA
                                     │
                        PP_0582 thiolase
                                     ▼
                     acyl-CoA(-2C) + acetyl-CoA
```

The thiolase + (R)-hydratase + NADH-reductase combination is diagnostic of a CoA-dependent β-oxidation-type module. In *Pseudomonas*, the MaoC (R)-hydratase specifically supplies (R)-3-hydroxyacyl-CoA — a direct precursor for medium-chain-length polyhydroxyalkanoate (PHA) synthesis — linking this module to the intersection of fatty-acid β-oxidation and PHA carbon-storage metabolism. PP_0581's NADH-dependent ketoreductase activity provides the reductive step that generates or interconverts the 3-hydroxyacyl-CoA/3-ketoacyl-CoA pool.

Two features mark this as a **dedicated, inducible catabolic module** rather than housekeeping biosynthesis: (1) the standalone AraC regulator implies substrate-inducible expression, and (2) the lack of a co-localized transporter or acyl-CoA synthetase indicates the substrate is generated intracellularly as a CoA-thioester intermediate. This is entirely consistent with PP_0581 being an HMwFabG — a class functionally and phylogenetically separate from the housekeeping FAS-II FabG (PP_1914), which handles constitutive membrane-lipid fatty-acid synthesis.

### Why PP_0581 is not the housekeeping FabG — summary comparison

| Property | PP_0581 (Q88QB3) | Housekeeping FabG (PP_1914) |
|----------|------------------|------------------------------|
| Length | 457 aa (~47.8 kDa) | 246 aa (~25 kDa) |
| Domain architecture | Two domains (N-flavodoxin-type + C-oxoreductase) | Single SDR domain |
| Class | HMwFabG / FabG4-type | Low-molecular-weight canonical FabG |
| Genomic context | AraC-regulated acyl-CoA module (PP_0579–0583) | *fabD–fabG–acpP* FAS-II operon |
| Cofactor | NADH (Asp251 determinant) | typically NADPH |
| PANTHER | PTHR42760:SF78 "[NADH]" | canonical 3-oxoacyl-ACP reductase |
| NCBIfam model | PRK08261 (HMwFabG) | canonical FabG model |
| Role | Inducible CoA-thioester ketoreduction | Essential FAS-II elongation |

---

## Evidence Base

The functional model rests on a combination of homology to a well-characterized structural prototype (FabG4), bioinformatic domain/motif analysis, AlphaFold structural modeling, and genomic-context inference. No experimental study on PP_0581 itself was located; the assignment is therefore an evidence-based inference. Key supporting literature:

| PMID | Title (abbrev.) | How it supports the findings |
|------|-----------------|------------------------------|
| [23163771](https://pubmed.ncbi.nlm.nih.gov/23163771/) | *Crystal structure of hexanoyl-CoA bound to β-ketoacyl reductase FabG4 of M. tuberculosis* | Defines the HMwFabG group and its diagnostic two-domain architecture (N-flavodoxin + C-oxoreductase) that PP_0581 shares; shows FabG4 accepts both CoA- and ACP-based substrates. |
| [21081168](https://pubmed.ncbi.nlm.nih.gov/21081168/) | *Crystal structure of FabG4 from M. tuberculosis reveals importance of C-terminal residues* | Establishes the reaction (acetoacetyl-CoA → 3-hydroxyacyl-CoA, NADH) and the Ser347/Tyr360/Lys364 triad that PP_0581's C-terminal domain reproduces. |
| [22750865](https://pubmed.ncbi.nlm.nih.gov/22750865/) | *Crystallization of high-molecular-weight ketoacyl reductase FabG4 complexed with NADH* | Confirms the NADH cofactor requirement characteristic of the HMwFabG class, matching PP_0581's Asp251 determinant and PANTHER "[NADH]" assignment. |
| [33782435](https://pubmed.ncbi.nlm.nih.gov/33782435/) | *Insights into A. baumannii fatty acid synthesis 3-oxoacyl-ACP reductases* | Confirms HMwFabGs are structurally and cofactor-distinct from canonical FabG, supporting that PP_0581 is not the housekeeping enzyme. |
| [12949091](https://pubmed.ncbi.nlm.nih.gov/12949091/) | *New enoyl-CoA hydratase in mcl-PHA biosynthesis* | Identifies the co-operonic PP_0580 MaoC-domain protein as an (R)-specific enoyl-CoA hydratase supplying (R)-3-hydroxyacyl-CoA from β-oxidation to PHA, defining the CoA-based pathway context. |

Additional context papers illustrate the broader theme that FabG-like SDRs are functionally diverse and that database annotation alone can be misleading:

- **Annotation can be misleading:** [PMID: 31443964](https://pubmed.ncbi.nlm.nih.gov/31443964/) describes an *A. baumannii* SDR annotated as "putative FabG" whose crystal structure showed a FabG-like fold but which was **not** active against the canonical FabG substrate acetoacetyl-CoA — a caution that structural hallmarks do not guarantee canonical substrate specificity. This directly motivates experimental verification of PP_0581's substrate.
- **Specialized FabG paralogs exist:** [PMID: 31560825](https://pubmed.ncbi.nlm.nih.gov/31560825/) (FabG3 in *Xanthomonas* xanthomonadin biosynthesis) and [PMID: 33846444](https://pubmed.ncbi.nlm.nih.gov/33846444/) (ApeQ in aryl-polyene biosynthesis) show that FabG-family reductases can be dedicated to specialized secondary-metabolite pathways rather than housekeeping FAS-II — consistent with PP_0581 being a specialized, AraC-regulated paralog.
- **The catalytic-triad concept has nuance:** [PMID: 33545175](https://pubmed.ncbi.nlm.nih.gov/33545175/) reported that *E. coli* FabG mutants lacking the assigned Ser/Tyr/Lys triad residues retained activity, suggesting canonical FabG may not be a classical SDR. This tempers over-reliance on the triad alone but does not alter the overall reductase assignment for PP_0581.
- **Multiple functional OARs can coexist:** [PMID: 26975437](https://pubmed.ncbi.nlm.nih.gov/26975437/) (S. meliloti NodG) demonstrates a bacterium can possess several 3-oxoacyl-ACP reductases capable of fatty-acid synthesis — consistent with KT2440's five K00059 paralogs.
- **Inhibitor validation of FabG4:** [PMID: 24129589](https://pubmed.ncbi.nlm.nih.gov/24129589/) confirms FabG4 is a validated β-ketoacyl-CoA reductase whose inhibitors bind the NADH cofactor domain, reinforcing the KAR-domain functional assignment for the HMwFabG class.

---

## Limitations and Knowledge Gaps

1. **No direct experimental study of PP_0581 exists.** All conclusions are inferred from homology (to *M. tuberculosis* FabG4), sequence-motif analysis, AlphaFold structural modeling, and genomic context. The gene has not been cloned, expressed, purified, or assayed in the reviewed literature.

2. **The precise physiological substrate is unknown.** While the module context indicates an intracellular CoA-thioester β-ketoacyl substrate, the chain length, degree of substitution, and whether ACP-linked substrates are also accepted have not been determined. The cautionary example of the *A. baumannii* SDR that failed to reduce acetoacetyl-CoA despite a FabG-like fold ([PMID: 31443964](https://pubmed.ncbi.nlm.nih.gov/31443964/)) underscores that substrate specificity cannot be assumed from fold alone.

3. **Cofactor preference is predicted, not measured.** The Asp251 determinant and PANTHER classification strongly predict NADH, but this has not been confirmed enzymatically for PP_0581 specifically.

4. **The metabolic destination is inferred.** The link to β-oxidation and/or PHA metabolism is based on the MaoC (R)-hydratase neighbor and thiolase, but flux through this module and the inducer sensed by AraC PP_0583 are unknown.

5. **The function of PP_0579** (co-operonic conserved hypothetical protein) is undefined and could modify the module's activity or substrate range.

6. **The role of the N-terminal "flavodoxin-type" domain** in PP_0581 is not established. In FabG4 this domain is non-catalytic and contributes to oligomerization/substrate handling; its specific contribution in PP_0581 is unmodeled beyond the confident fold.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant expression and enzyme assay.** Clone PP_0581, express in *E. coli*, purify, and assay β-ketoacyl reductase activity spectrophotometrically (NAD(P)H oxidation at 340 nm) against a panel: acetoacetyl-CoA, longer β-ketoacyl-CoAs (C6–C14), and β-ketoacyl-ACP. This tests the reaction, substrate specificity, and CoA-vs-ACP preference.

2. **Cofactor-preference determination.** Measure kinetics with NADH vs NADPH to confirm the Asp251-predicted NAD(H) selectivity, and test directly via a D251→basic mutant that should switch specificity toward NADPH.

3. **Catalytic-triad mutagenesis.** Generate S350A, Y363F, and K367A mutants and assay activity to confirm the SDR mechanism — while heeding the *E. coli* FabG precedent ([PMID: 33545175](https://pubmed.ncbi.nlm.nih.gov/33545175/)) that residual activity is possible.

4. **Operon/transcription mapping and AraC induction.** Use RT-PCR/RNA-seq to confirm the PP_0581–PP_0580–PP_0579 operon boundaries and the divergent PP_0582/PP_0583 arrangement, and identify the small-molecule inducer that activates the AraC regulator PP_0583.

5. **Phenotypic gene-deletion analysis.** Construct a PP_0581 knockout in KT2440 and screen for growth phenotypes on defined carbon sources (fatty acids of varying chain length, aromatics, alkanoates), altered fatty-acid/PHA profiles, and stress conditions — to place the module in β-oxidation vs PHA metabolism.

6. **In vitro reconstitution of the module.** Co-purify PP_0581, PP_0580 (MaoC hydratase), and PP_0582 (thiolase) and reconstitute the pathway with a defined acyl-CoA to establish the metabolic direction (degradative β-oxidation vs (R)-3-hydroxyacyl-CoA supply for PHA).

7. **Structural validation.** Solve the crystal structure of PP_0581 ± NADH ± substrate to confirm the AlphaFold-predicted two-domain architecture and active-site geometry, and to superpose on FabG4 to quantify fold homology.

---

## Conclusion

PP_0581 (Q88QB3) is best annotated as a **soluble, cytoplasmic, NADH-dependent, high-molecular-weight FabG (HMwFabG/FabG4-type) β-ketoacyl (3-oxoacyl) thioester reductase** that catalyzes the reduction of a 3-oxoacyl-thioester to an (R)-3-hydroxyacyl-thioester. It is functionally and phylogenetically distinct from the essential housekeeping FAS-II FabG (PP_1914) and instead operates as the ketoreduction step of a compact, AraC-regulated (PP_0583) acyl-CoA/β-oxidation-type module — a co-directional PP_0581–PP_0580 (MaoC (R)-hydratase)–PP_0579 operon divergent from a thiolase (PP_0582) — acting on an intracellular CoA-thioester intermediate at the intersection of fatty-acid β-oxidation and (R)-3-hydroxyacyl-CoA/PHA metabolism. This assignment is well-supported by structural homology, motif analysis, AlphaFold modeling, and genomic context, but awaits direct experimental confirmation of its substrate, cofactor, and physiological role.

## References (PubMed)

- Dutta D. et al. *Crystal structure of hexanoyl-CoA bound to β-ketoacyl reductase FabG4 of M. tuberculosis.* [PMID: 23163771](https://pubmed.ncbi.nlm.nih.gov/23163771/) (2013).
- Dutta D. et al. *Crystal structure of FabG4 from M. tuberculosis reveals importance of C-terminal residues in ketoreductase activity.* [PMID: 21081168](https://pubmed.ncbi.nlm.nih.gov/21081168/) (2011).
- Dutta D. et al. *Crystallization/preliminary X-ray analysis of HMw ketoacyl reductase FabG4–NADH.* [PMID: 22750865](https://pubmed.ncbi.nlm.nih.gov/22750865/) (2012).
- Cross P.J. et al. *Insights into Acinetobacter baumannii fatty acid synthesis 3-oxoacyl-ACP reductases (HMwFabG).* [PMID: 33782435](https://pubmed.ncbi.nlm.nih.gov/33782435/) (2021).
- *Design, synthesis and characterization of novel inhibitors against mycobacterial β-ketoacyl CoA reductase FabG4.* [PMID: 24129589](https://pubmed.ncbi.nlm.nih.gov/24129589/) (2013).
- *Structural characterization of a short-chain dehydrogenase/reductase from multi-drug resistant Acinetobacter baumannii.* [PMID: 31443964](https://pubmed.ncbi.nlm.nih.gov/31443964/) (2019).
- *A novel 3-oxoacyl-ACP reductase (FabG3) involved in xanthomonadin biosynthesis of Xanthomonas campestris.* [PMID: 31560825](https://pubmed.ncbi.nlm.nih.gov/31560825/) (2019).
- *Structural comparison of A. baumannii β-ketoacyl-ACP reductases in fatty acid and aryl polyene biosynthesis (ApeQ).* [PMID: 33846444](https://pubmed.ncbi.nlm.nih.gov/33846444/) (2021).
- Hu Z. et al. *E. coli FabG proteins lacking assigned catalytic-triad residues are active enzymes.* [PMID: 33545175](https://pubmed.ncbi.nlm.nih.gov/33545175/) (2021).
- *Sinorhizobium meliloti functionally replaces FabG by overexpressing NodG during fatty acid synthesis.* [PMID: 26975437](https://pubmed.ncbi.nlm.nih.gov/26975437/) (2016).
- Park S.J. & Lee S.Y. *New enoyl-CoA hydratase (MaoC) supplying (R)-3-hydroxyacyl-CoA to PHA biosynthesis.* [PMID: 12949091](https://pubmed.ncbi.nlm.nih.gov/12949091/) (2003).


## Artifacts

- [OpenScientist final report](PP_0581-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PP_0581-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:23163771
2. PMID:33782435
3. PMID:21081168
4. PMID:22750865
5. PMID:12949091
6. PMID:31443964
7. PMID:31560825
8. PMID:33846444
9. PMID:33545175
10. PMID:26975437
11. PMID:24129589