---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-17T14:07:59.687344'
end_time: '2026-07-17T14:32:23.994588'
duration_seconds: 1464.31
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: dapE
  gene_symbol: dapE
  uniprot_accession: Q88MP5
  protein_description: 'RecName: Full=Succinyl-diaminopimelate desuccinylase {ECO:0000255|HAMAP-Rule:MF_01690};
    Short=SDAP desuccinylase {ECO:0000255|HAMAP-Rule:MF_01690}; EC=3.5.1.18 {ECO:0000255|HAMAP-Rule:MF_01690};
    AltName: Full=N-succinyl-LL-2,6-diaminoheptanedioate amidohydrolase {ECO:0000255|HAMAP-Rule:MF_01690};'
  gene_info: Name=dapE {ECO:0000255|HAMAP-Rule:MF_01690}; OrderedLocusNames=PP_1525;
    ORFNames=PP1525;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the peptidase M20A family. DapE subfamily.
  protein_domains: ArgE/DapE_CS. (IPR001261); Bact_exopeptidase_dim_dom. (IPR036264);
    DapE_proteobac. (IPR005941); Peptidase_M20. (IPR002933); Peptidase_M20_dimer.
    (IPR011650)
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
citation_count: 8
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: dapE-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: dapE-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88MP5
- **Protein Description:** RecName: Full=Succinyl-diaminopimelate desuccinylase {ECO:0000255|HAMAP-Rule:MF_01690}; Short=SDAP desuccinylase {ECO:0000255|HAMAP-Rule:MF_01690}; EC=3.5.1.18 {ECO:0000255|HAMAP-Rule:MF_01690}; AltName: Full=N-succinyl-LL-2,6-diaminoheptanedioate amidohydrolase {ECO:0000255|HAMAP-Rule:MF_01690};
- **Gene Information:** Name=dapE {ECO:0000255|HAMAP-Rule:MF_01690}; OrderedLocusNames=PP_1525; ORFNames=PP1525;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the peptidase M20A family. DapE subfamily.
- **Key Domains:** ArgE/DapE_CS. (IPR001261); Bact_exopeptidase_dim_dom. (IPR036264); DapE_proteobac. (IPR005941); Peptidase_M20. (IPR002933); Peptidase_M20_dimer. (IPR011650)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "dapE" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'dapE' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **dapE** (gene ID: dapE, UniProt: Q88MP5) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *dapE* (Q88MP5, PP_1525) — Succinyl-diaminopimelate Desuccinylase in *Pseudomonas putida* KT2440

## Summary

The gene **dapE** (ordered locus **PP_1525**; UniProt **Q88MP5**) of *Pseudomonas putida* strain KT2440 (ATCC 47054 / DSM 6125) encodes **succinyl-diaminopimelate desuccinylase (SDAP desuccinylase; EC 3.5.1.18)**, a soluble cytoplasmic metalloenzyme of the **peptidase M20A family, DapE subfamily**. Its primary and specific function is to catalyze the **hydrolytic cleavage of the amide (succinyl) bond of N-succinyl-L,L-2,6-diaminopimelate (SDAP)**, releasing **L,L-2,6-diaminopimelate (L,L-DAP) and succinate** (Rhea:22608). This is the third and final step of the **succinylase branch** of the diaminopimelate (DAP)/lysine biosynthetic pathway, and its product feeds directly into two essential downstream fates: epimerization/decarboxylation to L-lysine for protein synthesis, and conversion to meso-DAP for cross-linking of the peptidoglycan cell wall.

Identity verification was rigorous and positive. The gene symbol, EC number, family, and domain architecture assigned by UniProt/HAMAP (rule MF_01690) match the biochemically and structurally characterized DapE orthologs described throughout the literature. The *P. putida* protein is 383 residues (~41.2 kDa), shares **62% sequence identity with the biochemically characterized *Escherichia coli* DapE**, and has **100% conservation of all seven catalytic and metal-binding residues** (His73, Asp75, Asp107, Glu141, Glu142, Glu170, His356). A very-high-confidence AlphaFold model (mean pLDDT 96.4) recapitulates the canonical two-domain M20A DapE fold. No literature for a different, unrelated gene sharing the "dapE" symbol was encountered — the annotation is unambiguous.

Two nuances are important. First, **no direct enzymatic or genetic study of the *P. putida* KT2440 DapE protein itself exists** — the functional assignment is a strong bioinformatic/evolutionary inference anchored on high sequence identity, complete active-site conservation, full pathway context, and structural modeling, rather than on a dedicated in vitro assay of Q88MP5. Second, unlike bypass-lacking pathogens (e.g., *Helicobacter pylori*, *Mycobacterium smegmatis*) where dapE deletion is lethal, *P. putida* KT2440 **also encodes a DapL-type L,L-DAP aminotransferase (PP_3786)** that converts tetrahydrodipicolinate directly to L,L-DAP in a single step, bypassing the entire succinylase branch. DapE is therefore expected to be **genetically redundant** in this organism, even though the enzyme itself is fully functional.

---

## Key Findings

### Finding 1 — DapE catalyzes hydrolytic desuccinylation of N-succinyl-L,L-DAP to L,L-DAP + succinate (EC 3.5.1.18)

The defining catalytic activity of DapE is the hydrolysis of the amide bond linking a succinyl group to the α-amino group of L,L-2,6-diaminopimelate. The reaction is:

> **N-succinyl-(2S,6S)-2,6-diaminopimelate + H₂O → (2S,6S)-2,6-diaminopimelate + succinate** (Rhea:22608)

This is annotated for Q88MP5 through HAMAP-Rule MF_01690 as EC 3.5.1.18 (N-succinyl-LL-2,6-diaminoheptanedioate amidohydrolase). The reaction identity is not merely a database assertion: it is grounded in direct enzymatic and structural work on orthologs. Crystallographic product-bound structures of DapE unambiguously establish that the enzyme "converts N-succinyl-L,L-diaminopimelic acid to L,L-diaminopimelic acid and succinate" ([PMID: 20138056](https://pubmed.ncbi.nlm.nih.gov/20138056/)). A validated ninhydrin/spectrophotometric assay quantifies the desuccinylase activity of *Haemophilus influenzae* DapE and confirms enzyme identity — "succinyl-diaminopimelate desuccinylase (DapE, E.C. 3.5.1.18)" — reporting inhibitor potencies (e.g., captopril IC₅₀ ≈ 3.4 µM) that match the EC number applied to Q88MP5 ([PMID: 29698518](https://pubmed.ncbi.nlm.nih.gov/29698518/)). Because P. putida DapE shares this exact catalytic machinery (see Findings 5–6), the same reaction and substrate specificity are assigned to it.

### Finding 2 — DapE is a dinuclear metallohydrolase acting as a homodimer with catalytic and dimerization domains

DapE enzymes are **dinuclear (two-metal) metallohydrolases**. High-resolution X-ray structures of *H. influenzae* DapE resolved "one and two zinc ions bound in the active site" and demonstrated distinct catalytic behavior for the mono- versus di-metalated forms ([PMID: 20138056](https://pubmed.ncbi.nlm.nih.gov/20138056/)). Each subunit "consisted of a catalytic domain and a dimerization domain" ([PMID: 25204745](https://pubmed.ncbi.nlm.nih.gov/25204745/)). A striking, mechanistically central feature is a **large substrate-induced conformational change**: upon substrate/product binding, "the catalytic domain rotates ∼50° and shifts ∼10.1 Å (as measured at the position of the Zn atoms) relative to the dimerization domain," closing over the dinuclear Zn(II) cluster (Zn–Zn distance ~3.8 Å) and completing the oxyanion hole — notably with His194 contributed *in trans* by the opposing subunit ([PMID: 29272107](https://pubmed.ncbi.nlm.nih.gov/29272107/)). This inter-subunit contribution explains why the **homodimer** is the functional unit. Spectroscopic studies of Co(II)-substituted enzyme show the two metals are antiferromagnetically coupled and can be bridged by a thiolate when the inhibitor captopril binds ([PMID: 26186504](https://pubmed.ncbi.nlm.nih.gov/26186504/)).

### Finding 3 — DapE operates in the succinylase branch of the DAP/lysine pathway, supplying peptidoglycan and lysine precursors

DapE acts at a **late stage of the anabolic pathway** leading to both L-lysine and meso-DAP, catalyzing "the desuccinylation of N-succinyl-L,L-diaminopimelic acid (SDAP) in a late stage of the anabolic pathway towards both lysine and a crucial building block of the peptidoglycan cell wall" ([PMID: 24057071](https://pubmed.ncbi.nlm.nih.gov/24057071/)). Genetic ordering studies in *E. coli* (using ΔdapD ΔdapE mutants) place dapE between the succinyl-transfer/aminotransferase steps and the DapF epimerase ([PMID: 17093042](https://pubmed.ncbi.nlm.nih.gov/17093042/)). The biological importance of this reaction is that its downstream products are "essential for protein synthesis and the cross-linking of the bacterial peptidoglycan cell wall" ([PMID: 40973684](https://pubmed.ncbi.nlm.nih.gov/40973684/)). Thus DapE sits at a metabolic branch point that provisions two indispensable macromolecular processes.

### Finding 4 — DapE is essential in many bacteria, has no human homolog, and is a validated antibacterial target

Across bypass-lacking bacteria, dapE is **essential**: its deletion is lethal to *H. pylori* and *M. smegmatis* ([PMID: 20138056](https://pubmed.ncbi.nlm.nih.gov/20138056/)), and lethal to *H. pylori* specifically because "deletion of DapE gene is lethal to H. pylori, since the organism has no alternative pathway for lysine biosynthesis" ([PMID: 25204745](https://pubmed.ncbi.nlm.nih.gov/25204745/)). Because "there are no similar pathways in humans, inhibitors that target DapE may have selective toxicity against only bacteria" ([PMID: 20138056](https://pubmed.ncbi.nlm.nih.gov/20138056/)). DapE is highly conserved across diverse bacterial species ([PMID: 40973684](https://pubmed.ncbi.nlm.nih.gov/40973684/)). One important pharmacological caveat is **metal heterogeneity**: the physiologically relevant "Mn(2+)-enzyme, which is also a physiologically relevant isoform in bacteria, is not inhibited" by L-captopril, which targets only the Zn(2+) isoform ([PMID: 24057071](https://pubmed.ncbi.nlm.nih.gov/24057071/)). This finding contextualizes DapE as a drug target in general; the redundancy in *P. putida* (Finding 7) means DapE is unlikely to be an effective target in this non-pathogenic organism specifically.

### Finding 5 — P. putida DapE has a fully conserved dinuclear metal active site with residue-level mapping

The 383-residue Q88MP5 sequence (41.2 kDa) carries residue-level HAMAP annotations that reproduce the canonical M20A dinuclear coordination sphere. The **active sites are Asp75 and Glu141** (the latter acting as the proton acceptor / catalytic general base), and the **metal ligands are His73, Asp107 (bridging both metals), Glu142, Glu170, and His356**, binding **two Zn(2+) or Co(2+) ions per subunit**. Direct mapping onto the primary sequence confirms these residues and their local motifs (…FAGH-TDV… at positions 73–75; …TSD-EE… at 141–142), matching the classic "2 His + bridging Asp + Glu general base" arrangement of the peptidase M20A dinuclear metallopeptidases. Supporting cross-references include Rhea:22608 for the catalytic activity, pathway UPA00034/UER00021 (L-lysine biosynthesis via DAP, succinylase route, step 3 of 3), homodimer quaternary structure, family peptidase M20A/DapE subfamily, eggNOG COG0624, CDD cd03891 (M20_DapE_proteobac), and TIGRFAM TIGR01246 (dapE_proteo). These conserved residues are interpreted against the canonical DapE mechanism, for which the ortholog structural work proposed "a revised catalytic mechanism of peptide bond cleavage by DapE enzymes" ([PMID: 20138056](https://pubmed.ncbi.nlm.nih.gov/20138056/)).

### Finding 6 — 62% identity to characterized E. coli DapE with 100% catalytic-residue conservation; gene is monocistronic

A global Needleman–Wunsch alignment of Q88MP5 (383 aa) against biochemically characterized *E. coli* DapE (P0AED7, 375 aa) yields **232/374 identical residues = 62.0% identity over the full length**. Critically, **all seven functional residues are strictly conserved**: His73, Asp75, Asp107, Glu141, Glu142, Glu170, and His356 each align to the identical residue in *E. coli*. KEGG independently annotates PP_1525 as **K01439** (succinyl-diaminopimelate desuccinylase, EC 3.5.1.18) in pathway ppu00300 (Lysine biosynthesis). Genomic context analysis shows PP_1525 occupies complement(1729936..1731087), flanked by PP_1524 (23S rRNA methyltransferase), PP_1526 (glucosyltransferase), PP_1523/PP_1528 (unknown), and PP_1522 (cold-shock protein) — **none are other DAP/lysine pathway genes** (dapA/B/C/D/F, lysA, asd map elsewhere on the chromosome). The gene is therefore **effectively monocistronic and independently regulated**, not co-transcribed in a dap operon. The shared function of the DapE orthologs to which the 62%-identical P. putida protein is compared is captured by the observation that "the dapE operon enzymes synthesize both meso-diaminopimelic acid and lysine" ([PMID: 20138056](https://pubmed.ncbi.nlm.nih.gov/20138056/)).

| Feature | *P. putida* DapE (Q88MP5) | *E. coli* DapE (P0AED7) |
|---|---|---|
| Length | 383 aa (~41.2 kDa) | 375 aa |
| Sequence identity | — | 62.0% (232/374) |
| His73 / Asp75 / Asp107 | conserved | identical |
| Glu141 / Glu142 / Glu170 | conserved | identical |
| His356 | conserved | identical |
| Metal ions per subunit | 2 (Zn²⁺ or Co²⁺) | 2 (Zn²⁺) |
| KEGG ortholog | K01439 | K01439 |
| Genomic context | monocistronic (PP_1525) | — |

### Finding 7 — P. putida encodes both the succinylase branch and a DapL bypass, so dapE is likely genetically redundant

The KEGG ortholog inventory for *P. putida* KT2440 (ppu) confirms the **succinylase branch is present**: dapD = PP_1530 (K00674); the N-succinyl-DAP aminotransferase (dapC) step is supplied by the promiscuous bifunctional **ArgD = PP_0372** (K00821; a dedicated dapC/K05822 gene is absent); and dapE = PP_1525 (K01439). Downstream steps are present: dapF = PP_3790 (K01778) and lysA = PP_2077/PP_5227 (K01586). Critically, *P. putida* **also encodes a DapL-type L,L-diaminopimelate aminotransferase, PP_3786** (K10206, EC 2.6.1.83) — "an aminotransferase that may directly convert tetrahydrodipicolinate to L,L-diaminopimelic acid" ([PMID: 17093042](https://pubmed.ncbi.nlm.nih.gov/17093042/)) — bypassing the entire dapD→dapC→dapE succinylase branch in a single transamination. The meso-DAP dehydrogenase (ddh, K03340) and acetylase-branch genes (dapH/dapX) are absent. This contrasts sharply with organisms lacking any bypass, where "deletion of DapE gene is lethal to H. pylori, since the organism has no alternative pathway for lysine biosynthesis" ([PMID: 25204745](https://pubmed.ncbi.nlm.nih.gov/25204745/)). Hydropathy analysis of Q88MP5 shows **no transmembrane segment** (max Kyte–Doolittle 19-residue window = 0.85; 0 windows above the ~1.6 threshold) and **no cleavable N-terminal signal peptide**, consistent with a **soluble cytoplasmic** localization.

### Finding 8 — AlphaFold model is very high confidence, supporting the two-domain M20A DapE fold

The AlphaFold DB model for Q88MP5 (383 residues, version 6) has a **mean pLDDT of 96.4**, with **94.5% of residues at very-high confidence (pLDDT > 90)**, 98.7% confident (pLDDT > 70), and only 0.8% at low confidence (pLDDT < 50). The uniformly high confidence across the full length is consistent with a well-defined **two-domain fold** — a catalytic Peptidase_M20 domain plus an M20_dimer dimerization domain — matching the architecture observed in experimentally solved DapE structures, in which "the catalytic domain rotates ∼50° and shifts ∼10.1 Å … relative to the dimerization domain" ([PMID: 29272107](https://pubmed.ncbi.nlm.nih.gov/29272107/)).

---

## Mechanistic Model / Interpretation

### Position in the diaminopimelate/lysine biosynthetic pathway

DapE catalyzes step 3 of 3 in the **succinylase branch** that converts tetrahydrodipicolinate (THDP) into L,L-DAP:

```
                          L-aspartate
                              │  (asd, dapA, dapB)
                              ▼
                 (S)-tetrahydrodipicolinate (THDP)
                        │                       │
     succinylase branch │                       │  DapL bypass
         (dapD)         │                       │  (PP_3786, K10206)
                        ▼                       │  single transamination
        N-succinyl-2-amino-6-ketopimelate       │
                        │  (dapC / ArgD, PP_0372)│
                        ▼                       │
        N-succinyl-L,L-DAP (SDAP)               │
                        │                       │
       ┌────────────────┘                       │
       │  ►► dapE (PP_1525, Q88MP5) ◄◄          │
       │     SDAP + H2O → L,L-DAP + succinate    │
       ▼                                        │
     L,L-2,6-diaminopimelate  ◄─────────────────┘
                        │
          ┌─────────────┴─────────────┐
          ▼ (dapF, PP_3790)            │
      meso-DAP                         │
          │                            ▼ (lysA, PP_2077/PP_5227)
   peptidoglycan cross-linking      L-lysine → protein synthesis
```

DapE removes the succinyl "handle" that was installed by DapD to make the downstream transamination stereospecific. The product L,L-DAP is then epimerized by DapF to meso-DAP (a direct peptidoglycan cross-linking residue) and decarboxylated by LysA to L-lysine. In *P. putida*, the DapL aminotransferase provides a parallel route to L,L-DAP that does not require the succinyl handle, which is why DapE is likely dispensable here.

### Catalytic mechanism at the dinuclear metal center

The active-site chemistry is that of a classic M20A dinuclear metallohydrolase. Two divalent metals (Zn²⁺ or, physiologically, possibly Mn²⁺ or Co²⁺) are held ~3.8 Å apart by a bridging aspartate (Asp107) plus terminal His/Glu ligands (His73, Glu142, Glu170, His356). A bridging water/hydroxide, polarized by the metals and by the general base **Glu141**, performs nucleophilic attack on the scissile amide carbonyl. The developing oxyanion is stabilized in an oxyanion hole that is only assembled after the substrate-triggered ~50° domain closure, and which is completed *in trans* by a histidine from the partner subunit — explaining the strict requirement for the homodimer. This mechanism, worked out from mono- and di-metalated *H. influenzae* structures and from substrate-bound conformational-change structures, applies directly to the P. putida enzyme because every ligand and catalytic residue is conserved.

### Localization

All evidence points to a **cytoplasmic** enzyme: no transmembrane helices, no signal peptide, a soluble globular two-domain fold, and a substrate (SDAP) that is a cytoplasmic metabolic intermediate. There is no evidence for periplasmic, membrane, or secreted localization.

### Reconciling function with redundancy

The key interpretive point for *P. putida* is that **an enzyme can be fully functional yet genetically redundant**. Q88MP5's active site is 100% conserved and its fold is textbook-perfect, so the protein almost certainly retains full desuccinylase activity. However, the co-existence of the DapL bypass (PP_3786) means that loss of dapE need not be lethal — in contrast to bypass-lacking pathogens. This distinction matters for any consideration of DapE as an antibacterial target: it is validated in pathogens with an obligate succinylase branch, but not in organisms like *P. putida* that carry the DapL shortcut.

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports / challenges the findings |
|---|---|---|
| [20138056](https://pubmed.ncbi.nlm.nih.gov/20138056/) | Structural basis for catalysis by mono-/dimetalated DapE | Defines substrate→products (L,L-DAP + succinate), dinuclear Zn active site, essentiality in H. pylori/M. smegmatis, no human homolog, revised mechanism. Core anchor for Findings 1, 2, 4, 5. |
| [29272107](https://pubmed.ncbi.nlm.nih.gov/29272107/) | Major conformational change on substrate binding in DapE | Documents ~50° / 10.1 Å catalytic-domain closure and two-domain architecture; underpins mechanism and AlphaFold fold interpretation (Findings 2, 8). |
| [25204745](https://pubmed.ncbi.nlm.nih.gov/25204745/) | In silico inhibitors of H. pylori DapE | Confirms catalytic + dimerization domain organization; establishes essentiality where no bypass exists — the key contrast for P. putida redundancy (Findings 2, 4, 7). |
| [24057071](https://pubmed.ncbi.nlm.nih.gov/24057071/) | Zinc-selective inhibition / metal heterogeneity | Places DapE in late DAP/lysine pathway toward lysine + peptidoglycan; documents Mn²⁺ vs Zn²⁺ isoform inhibitor differences (Findings 3, 4). |
| [29698518](https://pubmed.ncbi.nlm.nih.gov/29698518/) | Spectrophotometric DapE assay | Validated activity assay confirming enzyme identity/EC 3.5.1.18 and inhibitor IC₅₀ values (Finding 1). |
| [26186504](https://pubmed.ncbi.nlm.nih.gov/26186504/) | L-captopril inhibition of N. meningitidis DapE | EPR/MCD/crystallography showing antiferromagnetically coupled dinuclear metals and thiolate bridge on inhibitor binding (Finding 2). |
| [17093042](https://pubmed.ncbi.nlm.nih.gov/17093042/) | L,L-DAP aminotransferase (DapL) trans-kingdom | Establishes the DapL bypass that directly converts THDP to L,L-DAP, the basis for P. putida redundancy; helps order the succinylase branch (Findings 3, 7). |
| [40973684](https://pubmed.ncbi.nlm.nih.gov/40973684/) | Zinc-binding DapE inhibitors in K. pneumoniae | States biological role (protein synthesis + peptidoglycan cross-linking) and broad conservation of DapE (Findings 3, 4). |
| [32860896](https://pubmed.ncbi.nlm.nih.gov/32860896/) | DapE–flavonoid interactions | Reinforces DapE as an antimicrobial metal-center target across genera including *Pseudomonas*; supports the general drug-target framing. |

**Database evidence:** UniProt/HAMAP MF_01690 (EC 3.5.1.18; residue-level active-site and metal annotations), Rhea:22608, MetaCyc/UniPathway UPA00034/UER00021, KEGG K01439 / ppu00300 / PP_1525, eggNOG COG0624, CDD cd03891, TIGRFAM TIGR01246, and AlphaFold DB (mean pLDDT 96.4). These are consistent with, and mutually reinforced by, the primary literature above.

---

## Limitations and Knowledge Gaps

1. **No direct study of the P. putida KT2440 protein.** Every functional claim about Q88MP5 is a bioinformatic/evolutionary inference. No purified-protein kinetics, metal-content determination, crystal structure, or gene-knockout phenotype exists for this specific ortholog. The inference is strong (62% identity to a characterized enzyme, 100% active-site conservation, complete pathway context, pLDDT 96.4) but remains inference.

2. **Redundancy is predicted, not demonstrated.** The expectation that dapE is dispensable in *P. putida* rests on the presence of the DapL gene (PP_3786) and comparison to bypass-lacking organisms. No knockout has been reported to confirm that ΔdapE is viable in *P. putida*, nor whether DapL flux is sufficient under all growth conditions. It is possible the two routes are differentially regulated or condition-dependent.

3. **Physiological metal identity is unresolved.** DapE orthologs show metal heterogeneity (Zn²⁺ vs. Mn²⁺ vs. Co²⁺) with functional and pharmacological consequences. The in vivo metal used by *P. putida* DapE is unknown.

4. **Substrate stereospecificity assumed by homology.** The L,L-DAP (not meso- or D,D-) stereospecificity is inferred from orthologs and the conserved active site, not measured for Q88MP5.

5. **Regulation is uncharacterized.** The monocistronic genomic context implies independent regulation, but no promoter, transcription-factor, or expression data were established for PP_1525 in this investigation.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant expression and kinetic assay.** Clone PP_1525, purify Q88MP5, and measure desuccinylase activity on synthetic SDAP using the validated spectrophotometric/ninhydrin assay ([PMID: 29698518](https://pubmed.ncbi.nlm.nih.gov/29698518/)). Determine kcat, Km, and metal dependence (apo-reconstitution with Zn²⁺, Mn²⁺, Co²⁺).

2. **Gene knockout / bypass test.** Construct a ΔdapE (ΔPP_1525) mutant and test viability and lysine/DAP auxotrophy with and without a co-deletion of the DapL gene (ΔPP_3786). A synthetic-lethal ΔdapE ΔdapL phenotype rescued by exogenous lysine/DAP would directly confirm both DapE function and the redundancy model.

3. **Structural confirmation.** Solve the X-ray or cryo-EM structure of Q88MP5, ideally with substrate/product or captopril bound, to confirm the dinuclear metal geometry and the substrate-induced domain closure predicted by the AlphaFold model and ortholog structures.

4. **Metal-content analysis.** Use ICP-MS/EPR on natively purified enzyme to determine the physiologically bound metal(s), informing both mechanism and any inhibitor-design considerations.

5. **Expression profiling.** Quantify PP_1525 transcript/protein levels across growth phases and nitrogen/carbon conditions to test the independent-regulation hypothesis implied by its monocistronic context, and compare against DapL (PP_3786) expression to assess which route dominates flux.

---

## Conclusion

*dapE* (Q88MP5 / PP_1525) in *Pseudomonas putida* KT2440 is confidently annotated as **succinyl-diaminopimelate desuccinylase (EC 3.5.1.18)**, a soluble cytoplasmic homodimeric dinuclear-metal hydrolase of the peptidase M20A / DapE subfamily. It hydrolyzes N-succinyl-L,L-2,6-diaminopimelate to L,L-2,6-diaminopimelate plus succinate, performing the final L,L-DAP–forming step of the succinylase branch of DAP/lysine biosynthesis and thereby supplying meso-DAP for peptidoglycan cross-linking and lysine for protein synthesis. The assignment is inferential for this specific organism but strongly supported by 62% identity to characterized *E. coli* DapE with fully conserved catalytic residues, complete pathway context, and a very-high-confidence structural model. Because *P. putida* additionally encodes a DapL aminotransferase bypass, DapE is likely genetically redundant in this organism — a notable contrast to bypass-lacking pathogens in which dapE is essential and a validated drug target.


## Artifacts

- [OpenScientist final report](dapE-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](dapE-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:20138056
2. PMID:29698518
3. PMID:25204745
4. PMID:29272107
5. PMID:26186504
6. PMID:24057071
7. PMID:17093042
8. PMID:40973684