---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-13T02:53:07.603754'
end_time: '2026-08-13T03:18:53.568541'
duration_seconds: 1545.96
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_2585
  gene_symbol: PP_2585
  uniprot_accession: Q88JR4
  protein_description: 'RecName: Full=2,5-dioxovalerate dehydrogenase {ECO:0000256|ARBA:ARBA00067023};
    EC=1.2.1.26 {ECO:0000256|ARBA:ARBA00067023};'
  gene_info: OrderedLocusNames=PP_2585 {ECO:0000313|EMBL:AAN68193.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the aldehyde dehydrogenase family.
  protein_domains: Ald_DH/histidinol_DH. (IPR016161); Ald_DH_C. (IPR016163); Ald_DH_N.
    (IPR016162); Aldehyde_DH_dom. (IPR015590); Aldehyde_DH_Superfamily. (IPR050740)
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
citation_count: 4
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PP_2585-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PP_2585-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88JR4
- **Protein Description:** RecName: Full=2,5-dioxovalerate dehydrogenase {ECO:0000256|ARBA:ARBA00067023}; EC=1.2.1.26 {ECO:0000256|ARBA:ARBA00067023};
- **Gene Information:** OrderedLocusNames=PP_2585 {ECO:0000313|EMBL:AAN68193.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the aldehyde dehydrogenase family.
- **Key Domains:** Ald_DH/histidinol_DH. (IPR016161); Ald_DH_C. (IPR016163); Ald_DH_N. (IPR016162); Aldehyde_DH_dom. (IPR015590); Aldehyde_DH_Superfamily. (IPR050740)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_2585" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_2585' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_2585** (gene ID: PP_2585, UniProt: Q88JR4) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: PP_2585 (Q88JR4) — α-Ketoglutarate Semialdehyde Dehydrogenase

**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / KT2440), PSEPK
**Gene:** PP_2585 (OrderedLocusName); GenBank protein AAN68193 — **UniProt:** Q88JR4 — **KEGG:** ppu:PP_2585 / K13877
**EC:** 1.2.1.26 — **Protein family:** Aldehyde dehydrogenase (ALDH) superfamily

---

## Summary

**PP_2585 encodes α-ketoglutarate semialdehyde dehydrogenase (KGSADH; EC 1.2.1.26), a cytoplasmic, NAD(P)⁺-dependent enzyme of the aldehyde dehydrogenase (ALDH) superfamily.** Its primary catalytic function is the oxidation of α-ketoglutarate semialdehyde (2,5-dioxopentanoate, also called 2,5-dioxovalerate) to the tricarboxylic-acid-cycle intermediate 2-oxoglutarate (α-ketoglutarate). The reaction couples aldehyde oxidation to reduction of NAD⁺ or NADP⁺ and consumes a water molecule: **2,5-dioxopentanoate + NAD(P)⁺ + H₂O → 2-oxoglutarate + NAD(P)H + 2H⁺**. This is a terminal, energy-conserving step that channels carbon from several peripheral degradation routes into central metabolism.

Functionally, PP_2585 sits at a **convergent metabolic node**. α-Ketoglutarate semialdehyde is the shared penultimate metabolite produced by two distinct catabolic systems in *P. putida*: (i) the degradation of *trans*-4-hydroxy-L-proline (a major component of collagen and plant cell-wall proteins) and (ii) the catabolism of the sugar acids D-galactarate and D-glucarate (aldarate metabolism). By oxidizing this common intermediate to α-ketoglutarate, KGSADH allows the cell to harvest carbon, nitrogen, and reducing equivalents from all of these substrates. The enzyme is one of **three redundant KGSADH isozymes** (K13877 paralogs) in KT2440 — PP_1256, PP_2585, and PP_3602 — a redundancy that mirrors the multi-isozyme arrangements characterized biochemically in related bacteria.

The functional assignment rests on a coherent chain of evidence: authoritative UniProt/KEGG orthology annotation (K13877, EC 1.2.1.26); direct biochemical characterization of KGSADH orthologs by Watanabe and colleagues, who purified the enzymes and measured their substrate and coenzyme specificities; conserved sequence hallmarks of the ALDH mechanism (catalytic Cys301 in an F-C-T-N-P-G motif plus a Rossmann-type nucleotide-binding region); and genomic-context analysis (KEGG modules, STRING networks) placing PP_2585 within the hydroxyproline/aldarate metabolic landscape. The enzyme is predicted to be soluble and cytoplasmic (no signal peptide or transmembrane region), consistent with characterized homotetrameric KGSADH orthologs.

---

## Key Findings

### Finding 1 — PP_2585 is α-ketoglutarate semialdehyde dehydrogenase (KGSADH, EC 1.2.1.26)

PP_2585 catalyzes the NAD(P)⁺-dependent oxidation of α-ketoglutarate semialdehyde to α-ketoglutarate. UniProt Q88JR4 records **two catalytic-activity reactions** distinguished only by coenzyme: Rhea:47152 (NAD⁺) and Rhea:11296 (NADP⁺), both describing **2,5-dioxopentanoate + NAD(P)⁺ + H₂O = 2-oxoglutarate + NAD(P)H + 2H⁺** under EC 1.2.1.26. The KEGG entry `ppu:PP_2585` maps to orthology **K13877, "2,5-dioxopentanoate dehydrogenase [EC:1.2.1.26]"**, with the GenBank product name "Alpha-ketoglutaric semialdehyde dehydrogenase." The protein is 526 amino acids and belongs to the ALDH superfamily (Pfam PF00171 *Aldedh*; COG1012; InterPro IPR015590 / IPR016161–3).

This annotation is grounded in direct enzymology of orthologous KGSADH enzymes. Watanabe et al. explicitly defined the reaction: *"Here we focused on the fifth enzyme, alpha-ketoglutaric semialdehyde (alphaKGSA) dehydrogenase, catalyzing the conversion of alphaKGSA to alpha-ketoglutarate"* ([PMID: 16835232](https://pubmed.ncbi.nlm.nih.gov/16835232/)). A companion study confirmed that *"alpha-ketoglutaric semialdehyde (alphaKGSA) dehydrogenase (KGSADH) is involved in the last step, the conversion of alphaKGSA to alpha-ketoglutarate"* ([PMID: 17202142](https://pubmed.ncbi.nlm.nih.gov/17202142/)). Together, these establish that the reaction annotated for PP_2585/K13877 is the biochemically demonstrated function of this enzyme class.

### Finding 2 — PP_2585 is the convergent terminal step of hydroxyproline and aldarate catabolism

KEGG assigns PP_2585 to **Module M00948, "Hydroxyproline degradation, trans-4-hydroxy-L-proline ⇒ 2-oxoglutarate,"** and to three pathway maps: ppu00040 (Pentose and glucuronate interconversions), ppu00053 (Ascorbate and aldarate metabolism), and ppu00470 (D-Amino acid metabolism). The unifying feature of all these routes is that their shared penultimate metabolite is **α-ketoglutarate semialdehyde (2,5-dioxopentanoate)**, which KGSADH oxidizes to 2-oxoglutarate. In effect, PP_2585 is the funnel through which chemically diverse growth substrates converge on a single TCA-cycle output.

The hydroxyproline arm is well documented: *"Pseudomonas putida and Pseudomonas aeruginosa convert L-hydroxyproline to α-ketoglutarate via four hypothetical enzymatic steps different from known mammalian pathways"* ([PMID: 22833679](https://pubmed.ncbi.nlm.nih.gov/22833679/)). The aldarate arm is likewise established, with the same enzyme class acting in both routes: Watanabe et al. described *"d-glucarate/d-galactarate-inducible KGSADH-II and hydroxy-l-proline-inducible KGSADH-III"* ([PMID: 17202142](https://pubmed.ncbi.nlm.nih.gov/17202142/)), demonstrating that distinct inducing substrates recruit KGSADH isozymes for the identical terminal chemistry — exactly matching PP_2585's multi-pathway KEGG assignment.

### Finding 3 — A cytoplasmic, dual-coenzyme ALDH-superfamily enzyme with high specificity for αKGSA

UniProt Q88JR4 records **both** the NAD⁺ (Rhea:47152) and NADP⁺ (Rhea:11296) reactions, indicating a dual or relaxed coenzyme preference typical of KGSADH isozymes. The 526-residue sequence carries the ALDH Rossmann-type nucleotide-binding region and the catalytic cysteine motif (Pfam *Aldedh* PF00171). No signal peptide or transmembrane segment is annotated — the only sequence keywords are Oxidoreductase and Reference proteome — consistent with a **soluble, cytoplasmic** localization where the enzyme meets its water-soluble aldehyde substrate and pyridine-nucleotide coenzyme.

Biochemically characterized orthologs support both the specificity and the coenzyme diversity. Watanabe et al. reported that *"KGSADH-II and KGSADH-III showed similar high substrate specificity for alphaKGSA and different coenzyme specificity; that is, NAD(+)-dependent KGSADH-II and NADP(+)-dependent KGSADH-III"* ([PMID: 17202142](https://pubmed.ncbi.nlm.nih.gov/17202142/)). This directly rationalizes why Q88JR4 is annotated with both coenzymes: different isozymes of this family split along NAD⁺/NADP⁺ preference. On substrate scope, *"Higher catalytic efficiency of ALDH was found with alphaKGSA and succinic semialdehyde among the tested aldehyde substrates"* ([PMID: 16835232](https://pubmed.ncbi.nlm.nih.gov/16835232/)) — αKGSA is the preferred physiological substrate, with succinic semialdehyde a minor alternative. Characterized KGSADH orthologs assemble as active homotetramers/oligomers.

### Finding 4 — One of three redundant KGSADH isozymes; PP_1256 is the hydroxyproline-cluster copy, PP_2585 has its own operon

KEGG's link for `ppu/K13877` returns **three paralogs — PP_1256, PP_2585, and PP_3602 —** all annotated EC 1.2.1.26 and module M00948. The hydroxyproline catabolic gene cluster is composed of PP_1255 (D-hydroxyproline dehydrogenase, K21060), **PP_1256 (KGSADH, K13877)**, PP_1257 (Δ¹-pyrroline-4-hydroxy-2-carboxylate deaminase, K21062), and PP_1258 (4-hydroxyproline epimerase, K12658). Thus the KGSADH physically embedded within the hydroxyproline operon is PP_1256, not PP_2585.

STRING analysis (160488.PP_2585) shows all three paralogs co-occurring (dscore ≈ 0.9) and each linking strongly to *kdgD*/PP_3599 (2-keto-3-deoxy-glucarate dehydratase; score 0.958) — the enzyme that generates αKGSA in the aldarate route — and to α-ketoglutarate-consuming enzymes *icd*/*idh*/*sucA* (dscore ≈ 0.8), tying the product to the TCA cycle. Critically, PP_2585's **unique local genomic neighborhood** (neighborhood score) associates it with **PP_2584 (oguA, an amidohydrolase; nscore 0.47)** and **PP_2586 (a putative amino-acid transporter; nscore 0.48)**, defining a distinct operon separate from the hydroxyproline cluster. This suggests PP_2585 serves a substrate whose supply is coordinated by a dedicated hydrolase and transporter.

The multi-isozyme arrangement is a recognized feature of this enzyme family: *"A. brasilense possesses two different KGSADH isozymes from l-arabinose-related enzyme (KGSADH-I)"* ([PMID: 17202142](https://pubmed.ncbi.nlm.nih.gov/17202142/)). This precedent — one bacterium harboring multiple KGSADH isozymes tuned to different inducing substrates — parallels the three K13877 paralogs in KT2440 and explains why PP_2585 can exist alongside the hydroxyproline-dedicated PP_1256.

### Finding 5 — Conserved ALDH catalytic machinery: catalytic Cys301 and a Rossmann nucleotide-binding motif

Inspection of the Q88JR4 sequence confirms the hallmarks of the canonical ALDH thioacyl mechanism. The **strictly conserved catalytic cysteine is present at position 301**, embedded in the diagnostic **F-C-T-N-P-G ("FCTNPG") motif** — structurally equivalent to the catalytic Cys302 of human ALDH2 and to PROSITE PS00070 (aldehyde-dehydrogenase cysteine active site). The **glycine-rich nucleotide (NAD(P))-binding region** appears as "GASNFP" beginning at residue ~157. The two-domain architecture — an N-terminal catalytic domain and a C-terminal cofactor-binding domain (InterPro Ald_DH_N IPR016162 / Ald_DH_C IPR016163) — matches the classic ALDH fold. The sequence contains six cysteines (positions 180, 249, 297, 301, 396, 492), of which Cys301 is the catalytic nucleophile.

Mechanistically, these residues enable the standard ALDH two-step catalysis: the active-site cysteine thiolate attacks the aldehyde carbon to form a covalent thiohemiacetal, hydride is transferred to NAD(P)⁺ to yield a thioacyl-enzyme intermediate, and hydrolysis by an activated water molecule releases the carboxylic-acid product (2-oxoglutarate) and regenerates the free enzyme. The presence of both the catalytic Cys and the Rossmann motif is strong structural evidence that PP_2585 operates by this canonical mechanism.

---

## Mechanistic Model / Interpretation

### The reaction

```
        α-ketoglutarate semialdehyde (2,5-dioxopentanoate / 2,5-dioxovalerate)
                    O=CH–CH2–CH2–CO–COOH
                              |
                              |   + NAD(P)+  + H2O
              PP_2585 / KGSADH |   (catalytic Cys301; Rossmann NAD(P) site)
                              v
                    HOOC–CH2–CH2–CO–COOH
              2-oxoglutarate (α-ketoglutarate)   + NAD(P)H + 2 H+
```

The enzyme oxidizes the terminal aldehyde of α-ketoglutarate semialdehyde to a carboxylate, producing α-ketoglutarate — a hub metabolite of the TCA cycle and the principal cellular carbon skeleton for nitrogen assimilation (via glutamate/glutamine).

### Convergent metabolic funnel

```
   trans-4-hydroxy-L-proline                 D-galactarate / D-glucarate
   (collagen / plant proteins)                    (aldarates / sugar acids)
            |                                             |
   [PP_1258 epimerase]                          [ ... aldarate enzymes ... ]
   [PP_1255 D-Hyp dehydrogenase]                        |
   [PP_1257 Pyr4H2C deaminase]                  [PP_3599 kdgD:
            |                                     2-keto-3-deoxy-glucarate
            v                                         dehydratase]
     α-ketoglutarate semialdehyde  <----------------------+
     (2,5-dioxopentanoate)
            |
            |   KGSADH isozymes: PP_1256 / PP_2585 / PP_3602   (K13877, EC 1.2.1.26)
            v
       α-ketoglutarate  ──►  TCA cycle (icd/idh, sucA)  ──►  energy + biosynthesis + N assimilation
```

Two chemically unrelated classes of nutrient — a hydroxylated imino acid (hydroxyproline) and six-carbon dicarboxylic sugar acids (aldarates) — are catabolized by separate upstream enzyme sets, yet both routes converge on **α-ketoglutarate semialdehyde**. KGSADH performs the single terminal oxidation that unites them, delivering α-ketoglutarate into central metabolism. This is a textbook example of **metabolic convergent evolution**, the theme emphasized by Watanabe et al.

### Isozyme division of labor

| Locus | Orthology | Genomic context | Likely primary role |
|-------|-----------|-----------------|---------------------|
| **PP_1256** | K13877 (EC 1.2.1.26) | Embedded in hydroxyproline operon (PP_1255–PP_1258) | Terminal step of *trans*-4-hydroxy-L-proline degradation |
| **PP_2585** | K13877 (EC 1.2.1.26) | Own operon with *oguA* amidohydrolase (PP_2584) + amino-acid transporter (PP_2586) | αKGSA oxidation for a substrate supplied via a dedicated hydrolase/transporter arm |
| **PP_3602** | K13877 (EC 1.2.1.26) | Third paralog | Additional/backup KGSADH capacity |

All three paralogs share the same chemistry but are embedded in different regulatory/genomic contexts, allowing *P. putida* to induce KGSADH activity in response to whichever inducing substrate is present — precisely the isozyme strategy documented in *Azospirillum brasilense* and other bacteria.

### Localization

PP_2585 is a **soluble cytoplasmic enzyme**. There is no signal peptide, lipobox, or transmembrane region annotated; the ALDH fold is that of a globular cytosolic oxidoreductase. This localization is functionally appropriate: both the aldehyde substrate and the NAD(P)⁺ coenzyme are water-soluble cytoplasmic species, and the product α-ketoglutarate feeds directly into cytoplasmic TCA-cycle and nitrogen-assimilation enzymes.

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports the annotation |
|------|-----------------|-------------------------------|
| [17202142](https://pubmed.ncbi.nlm.nih.gov/17202142/) | *α-KGSA dehydrogenase isozymes in D-glucarate, D-galactarate, and hydroxy-L-proline pathways; convergent evolution* | Direct biochemical characterization: defines KGSADH's terminal reaction; documents NAD⁺- vs NADP⁺-dependent isozymes (II vs III) with high αKGSA specificity; shows aldarate- and hydroxyproline-inducible isozymes; establishes multi-isozyme precedent |
| [16835232](https://pubmed.ncbi.nlm.nih.gov/16835232/) | *A novel α-KGSA dehydrogenase: L-arabinose metabolism* | Defines the αKGSA → α-ketoglutarate reaction; shows the enzyme's highest catalytic efficiency is on αKGSA (and succinic semialdehyde), fixing substrate specificity |
| [22833679](https://pubmed.ncbi.nlm.nih.gov/22833679/) | *D-hydroxyproline dehydrogenase and Pyr4H2C deaminase in L-hydroxyproline metabolism* | Establishes that *P. putida*/*P. aeruginosa* convert L-hydroxyproline to α-ketoglutarate — the M00948 pathway whose terminal KGSADH step includes PP_2585/PP_1256 |
| [5764334](https://pubmed.ncbi.nlm.nih.gov/5764334/) | *Inducible degradation of hydroxyproline in Pseudomonas putida* | Classic study showing the *P. putida* hydroxyproline pathway is inducible, coordinately regulated, and coupled to an inducible hydroxyproline uptake system — physiological context for the pathway |

**Database evidence (supporting):** UniProt Q88JR4 (two Rhea reactions, EC 1.2.1.26, ALDH family, no localization signals); KEGG ppu:PP_2585 = K13877, module M00948 and pathways ppu00040/00053/00470; Pfam PF00171 (*Aldedh*), COG1012, InterPro IPR015590/IPR016161–3; STRING 160488.PP_2585 (paralog co-occurrence; strong links to kdgD/PP_3599 and icd/sucA; unique neighborhood with PP_2584/PP_2586); PROSITE PS00070 catalytic-cysteine motif matched at Cys301.

**Note on evidence type:** The functional assignment for PP_2585 itself derives from orthology and sequence/genomic-context inference rather than from a dedicated biochemical study of the KT2440 PP_2585 protein. However, the enzyme *class* (KGSADH, EC 1.2.1.26) has been rigorously characterized by purification and kinetics in closely related orthologs, and the sequence carries all diagnostic catalytic and cofactor-binding motifs, giving high confidence in the annotation.

---

## Limitations and Knowledge Gaps

1. **No direct enzymology on PP_2585 specifically.** The catalytic assignment is by orthology (K13877) and sequence analysis. The purified-enzyme kinetics (Kₘ, kcat, coenzyme preference) come from KGSADH orthologs (Watanabe et al.), not from the KT2440 PP_2585 gene product itself. Whether PP_2585 is NAD⁺-preferring, NADP⁺-preferring, or dual has not been experimentally resolved for this specific isozyme.

2. **Isozyme-specific physiological role is inferred.** Which of the three paralogs (PP_1256, PP_2585, PP_3602) is dominant under which growth condition has not been established here by gene-deletion or expression studies. PP_1256 is assigned to hydroxyproline by genomic co-localization, but PP_2585's precise inducing substrate is inferred from its neighbors (oguA amidohydrolase PP_2584, transporter PP_2586) rather than measured.

3. **Quaternary structure and localization are predicted.** Homotetramer assembly and cytoplasmic localization are inferred from family properties and the absence of targeting signals; no experimental structure of PP_2585 is cited.

4. **Function of the PP_2584/PP_2586 operon partners is hypothetical.** The amidohydrolase (oguA) and transporter annotations are database-level; the exact substrate that this operon processes upstream of PP_2585 remains to be defined.

5. **Regulation is unresolved for PP_2585.** The classic inducibility data ([PMID: 5764334](https://pubmed.ncbi.nlm.nih.gov/5764334/)) pertain to the hydroxyproline pathway broadly; the promoter/regulator controlling PP_2585 specifically is not identified.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant expression and kinetic characterization of PP_2585.** Clone, express, and purify the KT2440 PP_2585 protein; measure Kₘ/kcat for α-ketoglutarate semialdehyde and succinic semialdehyde, and determine NAD⁺ vs NADP⁺ preference to place it as a KGSADH-II- or KGSADH-III-type isozyme.

2. **Single- and combinatorial gene knockouts.** Construct ΔPP_1256, ΔPP_2585, ΔPP_3602 single, double, and triple mutants and assay growth on *trans*-4-hydroxy-L-proline, D-galactarate, and D-glucarate to define each isozyme's non-redundant contribution and the degree of functional overlap.

3. **Transcriptional induction profiling.** Use RT-qPCR or RNA-seq to determine which substrates (hydroxyproline, aldarates, or the substrate of the PP_2584/PP_2586 operon) induce PP_2585, identifying its regulon and inducer.

4. **Characterize the operon partners.** Biochemically test PP_2584 (oguA amidohydrolase) and PP_2586 (putative amino-acid transporter) to identify the substrate they mobilize, clarifying the specific catabolic arm PP_2585 serves.

5. **Structural determination.** Solve the crystal or cryo-EM structure of PP_2585 (apo and NAD(P)⁺/substrate-bound) to confirm the homotetramer, validate the Cys301 active site and Rossmann fold, and rationalize coenzyme selectivity at the atomic level.

6. **Metabolic-flux analysis.** Use ¹³C-labeled hydroxyproline and aldarates to trace flux through α-ketoglutarate semialdehyde and quantify each KGSADH isozyme's flux contribution in vivo.

---

## Conclusion

PP_2585 (Q88JR4) of *Pseudomonas putida* KT2440 is **α-ketoglutarate semialdehyde dehydrogenase (KGSADH, EC 1.2.1.26 / KEGG K13877)** — a cytoplasmic, NAD(P)⁺-dependent ALDH-superfamily enzyme that oxidizes α-ketoglutarate semialdehyde (2,5-dioxopentanoate) to the TCA-cycle metabolite 2-oxoglutarate. It performs the convergent terminal step that channels carbon from *trans*-4-hydroxy-L-proline degradation and from D-galactarate/D-glucarate (aldarate) catabolism into central metabolism. It is one of three redundant KGSADH isozymes in KT2440 (the hydroxyproline-cluster copy being PP_1256), and its own genomic neighborhood — an amidohydrolase (PP_2584/oguA) and an amino-acid transporter (PP_2586) — points to a dedicated substrate-supply arm. The enzyme carries the full canonical ALDH catalytic apparatus (catalytic Cys301 in an FCTNPG motif; Rossmann NAD(P)-binding region), supporting the standard thioacyl-intermediate mechanism, with high substrate specificity for α-ketoglutarate semialdehyde and succinic semialdehyde as a minor alternative substrate.


## Artifacts

- [OpenScientist final report](PP_2585-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PP_2585-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:16835232
2. PMID:17202142
3. PMID:22833679
4. PMID:5764334