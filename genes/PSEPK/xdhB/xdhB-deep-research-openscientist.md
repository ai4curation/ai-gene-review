---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-19T08:48:07.276094'
end_time: '2026-08-19T09:33:47.595931'
duration_seconds: 2740.32
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: xdhB
  gene_symbol: xdhB
  uniprot_accession: Q88F20
  protein_description: 'SubName: Full=Xanthine dehydrogenase subunit XdhB {ECO:0000313|EMBL:AAN69859.1};
    EC=1.17.1.4 {ECO:0000313|EMBL:AAN69859.1};'
  gene_info: Name=xdhB {ECO:0000313|EMBL:AAN69859.1}; OrderedLocusNames=PP_4279 {ECO:0000313|EMBL:AAN69859.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the xanthine dehydrogenase family.
  protein_domains: Ald_Oxase/Xan_DH_a/b. (IPR000674); Ald_Oxase/Xan_DH_a/b_sf. (IPR036856);
    Ald_Oxase/xanthine_DH-like. (IPR016208); AldOxase/xan_DH_MoCoBD1. (IPR008274);
    AldOxase/xan_DH_MoCoBD2. (IPR046867)
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
citation_count: 7
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: xdhB-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: xdhB-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88F20
- **Protein Description:** SubName: Full=Xanthine dehydrogenase subunit XdhB {ECO:0000313|EMBL:AAN69859.1}; EC=1.17.1.4 {ECO:0000313|EMBL:AAN69859.1};
- **Gene Information:** Name=xdhB {ECO:0000313|EMBL:AAN69859.1}; OrderedLocusNames=PP_4279 {ECO:0000313|EMBL:AAN69859.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the xanthine dehydrogenase family.
- **Key Domains:** Ald_Oxase/Xan_DH_a/b. (IPR000674); Ald_Oxase/Xan_DH_a/b_sf. (IPR036856); Ald_Oxase/xanthine_DH-like. (IPR016208); AldOxase/xan_DH_MoCoBD1. (IPR008274); AldOxase/xan_DH_MoCoBD2. (IPR046867)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "xdhB" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'xdhB' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **xdhB** (gene ID: xdhB, UniProt: Q88F20) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *xdhB* (Q88F20, PP_4279) — Xanthine Dehydrogenase Catalytic Subunit in *Pseudomonas putida* KT2440

**Target:** UniProt **Q88F20** (Q88F20_PSEPK) · Gene **xdhB** · Ordered locus **PP_4279**
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / NCIMB 11950 / **KT2440**)
**Protein:** Xanthine dehydrogenase subunit XdhB · **EC 1.17.1.4** · 799 aa, ~88 kDa

## Summary

The gene ***xdhB*** (ordered locus **PP_4279**; UniProt **Q88F20**) of *Pseudomonas putida* KT2440 encodes the **large molybdenum-cofactor (molybdopterin)-binding catalytic subunit of a two-subunit bacterial xanthine dehydrogenase** (EC 1.17.1.4). The 799-amino-acid, ~88 kDa protein carries the molybdopterin (Moco) catalytic center at which the committed step of oxidative purine catabolism occurs: the molybdenum-dependent oxidative hydroxylation of **xanthine to urate** (uric acid), and, upstream, of **hypoxanthine to xanthine**. The domain architecture of Q88F20 — comprising an N-terminal aldehyde-oxidase/xanthine-dehydrogenase "a/b" hammerhead domain and C-terminal molybdopterin-binding domains (MoCoBD1/MoCoBD2) — contains *only* the catalytic-subunit modules, with no FAD- or iron-sulfur-binding regions. This split architecture directly mirrors the well-characterized two-subunit xanthine dehydrogenase of *Rhodobacter capsulatus*, in which the redox cofactors are distributed across separate polypeptides.

XdhB does not work in isolation. It partners with the adjacent gene product **XdhA** (PP_4278, Q88F21), which houses the two [2Fe-2S] clusters and the FAD, to form a catalytically active **XdhA₂B₂ heterotetramer**. In this assembly XdhB abstracts electrons from the purine substrate at its Mo center and relays them intramolecularly through the XdhA iron-sulfur clusters to FAD and ultimately to the NAD⁺/electron acceptor. Maturation of XdhB requires a third co-encoded protein, the **XdhC accessory factor** (PP_4280, Q88F19), which is necessary for insertion of the molybdopterin cofactor into the apo-enzyme but is not itself a subunit of the mature complex. The enzyme is a soluble cytoplasmic protein.

Biologically, *xdhB* sits within an **xdhA–xdhB–xdhC–guaD gene cluster** (PP_4278–PP_4281) that constitutes a purine-catabolic module. Guanine is deaminated to xanthine by GuaD (guanine deaminase), and XdhAB then oxidizes xanthine to urate, funneling purine ring nitrogen and carbon into downstream uricase/allantoin pathways. This enables *P. putida* to exploit purines (adenine, guanine, hypoxanthine, xanthine, uric acid) as sole nitrogen and carbon sources — a physiology reinforced by the organism's dedicated purine chemoreceptor McpH. A high-confidence AlphaFold model (mean pLDDT 96.4) confirms XdhB folds as a single compact multidomain globular catalytic subunit, consistent with its assigned function.

---

## Key Findings

### Finding 1 — Q88F20 is the molybdopterin catalytic subunit of a two-subunit bacterial xanthine dehydrogenase

UniProt entry Q88F20 describes a **799-amino-acid (~88 kDa)** protein submitted as "Xanthine dehydrogenase subunit XdhB," carrying EC number **1.17.1.4**, from *Pseudomonas putida* KT2440 (taxid 160488). Critically, the InterPro/Pfam domain architecture of this protein contains **only molybdopterin-subunit domains** and none of the FAD or iron-sulfur binding modules found in single-chain eukaryotic xanthine oxidoreductases. Specifically, the annotated domains are: the N-terminal aldehyde-oxidase/xanthine-dehydrogenase **a/b "hammerhead" domain** (residues 39–146, IPR000674), a molybdopterin-binding domain (Gene3D 3.30.365.10), **MoCoBD_1 (PF02738)**, **MoCoBD_2 (PF20256)**, **Ald_Xan_dh_C (PF01315)**, and the **Xanthine_DH_Mopterin-bd_su** signature (IPR014309). Gene Ontology annotations include GO:0004854 (xanthine dehydrogenase activity) and GO:0030151 (molybdenum ion binding).

The adjacent gene, **PP_4278 (Q88F21, xdhA, 484 aa)**, encodes the complementary electron-transfer subunit carrying the FAD and the two [2Fe-2S] clusters. This division of cofactors across two polypeptides is the diagnostic hallmark of the bacterial (as opposed to eukaryotic single-chain) xanthine dehydrogenase, and it directly mirrors the *Rhodobacter capsulatus* two-subunit split. As reported for the *R. capsulatus* enzyme, "*the deduced amino acid sequence of XDHA contains binding sites for two [2Fe-2S] clusters and FAD, whereas XDHB is predicted to contain the molybdopterin cofactor*" ([PMID: 9515710](https://pubmed.ncbi.nlm.nih.gov/9515710/)). The same paper notes that "*in contrast to R. capsulatus, these three cofactor binding sites reside within a single polypeptide chain in eukaryotic xanthine dehydrogenases*" — a key point that explains why family-level annotations for FAD or [2Fe-2S] binding are sometimes inappropriately propagated onto the isolated bacterial XdhB subunit, which does **not** bind these cofactors.

### Finding 2 — Primary function: molybdenum-dependent hydroxylation of xanthine to urate

The primary catalytic function of XdhB is to carry out **EC 1.17.1.4** chemistry:

> xanthine + NAD⁺ + H₂O → urate + NADH + H⁺

The enzyme also oxidizes **hypoxanthine to xanthine** in the preceding step. The catalytic chemistry occurs at the **Mo-molybdopterin center** — in bacteria typically the molybdopterin cytosine dinucleotide form (Mo-MCD; ChEBI:71308) — located on XdhB. The Mo=O/Mo–OH group performs the nucleophilic hydroxylation at purine carbon **C8**, which constitutes the reductive half-reaction. Electrons then flow **XdhB(Mo) → XdhA([2Fe-2S]) → XdhA(FAD) → NAD⁺**, the oxidative half-reaction.

The genomic context strongly reinforces this pathway role: the *xdhAB(C)* cluster (PP_4278–4280) sits immediately upstream of *guaD* (PP_4281, guanine deaminase), which produces xanthine and thereby directly supplies XdhB's substrate. Classic biochemical work on *Pseudomonas putida* established that "*the xanthine would seem to be channeled through conventional pathways of purine degradation through the action of xanthine dehydrogenase and uricase, both induced by growth on caffeine*" ([PMID: 1158847](https://pubmed.ncbi.nlm.nih.gov/1158847/)), and later work on *P. putida* CBB5 explicitly confirmed that "*xanthine was eventually oxidized to uric acid*" ([PMID: 19447909](https://pubmed.ncbi.nlm.nih.gov/19447909/)). These directly document the xanthine → urate oxidation catalyzed at XdhB's molybdenum center.

### Finding 3 — XdhB operates in purine catabolism, enabling purines as nitrogen sources; encoded in an xdhABC-guaD cluster

The genes form a coherent catabolic module in *P. putida* KT2440:

| Locus | Gene | UniProt | Product | Role |
|-------|------|---------|---------|------|
| PP_4278 | *xdhA* | Q88F21 | XDH electron-transfer subunit (484 aa) | Binds FAD + 2×[2Fe-2S] |
| PP_4279 | *xdhB* | Q88F20 | **XDH catalytic subunit (799 aa)** | **Mo-molybdopterin center; xanthine→urate** |
| PP_4280 | *xdhC* | Q88F19 | XDH accessory factor (281 aa) | Moco insertase/chaperone |
| PP_4281 | *guaD* | Q88F18 | Guanine deaminase (EC 3.5.4.3, Zn²⁺) | guanine → xanthine |

The pathway logic is: **guanine →(GuaD)→ xanthine →(XdhAB)→ urate**, with **hypoxanthine →(XdhAB)→ xanthine** feeding in as well. Downstream, urate is processed by uricase/allantoin pathway enzymes. This module allows *P. putida* to use purines as sole nitrogen sources. Consistent with this, the KT2440 chemoreceptor **McpH** specifically binds "*adenine, guanine, xanthine, hypoxanthine and uric acid. The latter five compounds form part of the purine degradation pathway, permitting their use as sole nitrogen sources*" ([PMID: 26355499](https://pubmed.ncbi.nlm.nih.gov/26355499/)). The same study describes McpH as "*a chemoreceptor from Pseudomonas putida KT2440... which specifically recognizes purine and its derivatives*," confirming that KT2440 actively senses and metabolizes exactly the intermediates that flank XdhB's reaction.

### Finding 4 — XdhB requires the XdhC accessory factor for molybdenum-cofactor insertion; the enzyme is cytoplasmic

The co-transcribed **xdhC** gene product (PP_4280) is homologous to *R. capsulatus* XDHC. In *R. capsulatus*, active XDH is an **(αβ)₂ = XDHA₂XDHB₂ heterotetramer**, and XDHC is *not* a subunit of the mature enzyme; rather, it is required for activity because in an *xdhC* mutant no molybdopterin cofactor is present in the XDHAB tetramer, even though FAD and the iron-sulfur clusters still assemble normally. As stated by Leimkühler and Klipp: "*The absence of MPT from XDH isolated from an xdhC mutant indicates that XDHC either acts as a specific MPT insertase or might be a specific chaperone facilitating the insertion of MPT and/or folding of XDH during or after cofactor insertion*" ([PMID: 10217763](https://pubmed.ncbi.nlm.nih.gov/10217763/)). The same paper confirms that "*XDHC is not a subunit of active XDH, which forms an alpha2beta2 heterotetramer in R. capsulatus*."

By homology, *P. putida* XdhC serves the same role: it inserts the molybdopterin cofactor into apo-XdhB, defining XdhB's post-translational maturation requirement. Xanthine dehydrogenase is a soluble **cytosolic** enzyme; Q88F20 has no signal peptide or transmembrane segments, consistent with cytoplasmic localization where its purine substrates are generated.

### Finding 5 — XdhB houses conserved xanthine-oxidoreductase active-site motifs and a broad purine/methylxanthine substrate range

The Mo-molybdopterin domain carried by XdhB is the catalytic locus at which xanthine and hypoxanthine are oxidized. In the extensively studied mammalian xanthine oxidase, catalysis involves the critical active-site residues **Arg880** and **Glu802**, plus the catalytic base **Glu1261**. A bioinformatic scan of Q88F20 (799 aa) recovers the diagnostic conserved xanthine-oxidoreductase/molybdopterin motifs: the **GGGFGGKE** active-site loop (~pos 247), the **AYRGFGGPQG** hammerhead–MoCo linker (~pos 362), **TATNTDK** (~pos 518), and the C-terminal **IQGMGW** substrate-funnel motif (~pos 673) — all located within the MoCoBD1/MoCoBD2 domains (PF02738/PF20256).

Molecular-docking and spectroscopy studies confirm that "*its molybdopterin (Mo-Pt) domain is an important catalytic center when xanthine and hypoxanthine are oxidated*" ([PMID: 37209475](https://pubmed.ncbi.nlm.nih.gov/37209475/)), and identify the conserved residues "*interacting with critical amino acid residues (Arg880 and Glu802) in catalysis reaction of XO*" ([PMID: 32777423](https://pubmed.ncbi.nlm.nih.gov/32777423/)). Importantly, in *Pseudomonas* the xanthine-oxidizing activity has a broad substrate range: "*a broad-substrate-range xanthine-oxidizing enzyme was responsible for the formation of these methyluric acids*" ([PMID: 19447909](https://pubmed.ncbi.nlm.nih.gov/19447909/)), converting 1- and 3-methylxanthines to their corresponding methyluric acids in addition to xanthine and hypoxanthine. This broad specificity is physiologically relevant to *P. putida* strains that degrade caffeine and other methylxanthines.

### Finding 6 — AlphaFold model supports a well-folded single-chain molybdopterin catalytic subunit

The AlphaFold DB model **AF-Q88F20-F1 (v6)**, covering the full length (residues 1–799), is of very high confidence: **mean pLDDT = 96.4, median = 98.1**; 95.1% of residues have pLDDT > 90 (very high), 98.7% > 70 (confident), and only 0.5% < 50. The model spans the entire polypeptide as one compact, multidomain globular chain comprising the N-terminal aldehyde-oxidase/xanthine-DH a/b hammerhead domain and the C-terminal molybdopterin-binding (MoCoBD1/MoCoBD2) domains. This structural prediction is fully consistent with XdhB being a well-folded catalytic subunit, and provides an independent, structure-based line of evidence supporting the domain-based functional assignment.

---

## Mechanistic Model / Interpretation

XdhB is best understood as the catalytic engine of a **modular, multi-cofactor electron-transfer machine** distributed across two polypeptides. The following schematic integrates the findings:

```
   PURINE CATABOLIC MODULE (P. putida KT2440, PP_4278–4281)
   ─────────────────────────────────────────────────────────

     guanine
        │  GuaD (PP_4281, Zn2+)
        ▼
     xanthine ◄──── hypoxanthine
        │                 │
        │   XdhA2B2 heterotetramer (EC 1.17.1.4)
        │                 │
        ▼                 ▼
   ┌───────────────────────────────────────────────┐
   │  XdhB (Q88F20)          XdhA (Q88F21)          │
   │  Mo-molybdopterin  ─►  [2Fe-2S] ─► FAD ─► NAD+ │
   │  (C8 hydroxylation)     (electron relay)       │
   └───────────────────────────────────────────────┘
        │
        ▼
     urate (uric acid)
        │  uricase / allantoin pathway
        ▼
   ring nitrogen + carbon  → used as N and C source

   MATURATION:  apo-XdhB + Moco --[ XdhC (PP_4280) ]--> holo-XdhB
```

**Reductive half-reaction (on XdhB).** The molybdenum center, coordinated by the pyranopterin dithiolene of the molybdopterin cofactor (in bacteria typically the MCD form), attacks C8 of the bound purine. The Mo–OH/Mo=O oxo/hydroxyl group is transferred to the substrate, hydroxylating xanthine at C8 to yield urate (and hypoxanthine to xanthine). This step reduces Mo(VI) toward Mo(IV).

**Electron relay and oxidative half-reaction (on XdhA).** The two electrons generated are passed one at a time from the reduced Mo center to the proximal [2Fe-2S] cluster, then to the distal [2Fe-2S] cluster, then to FAD, and finally to the terminal acceptor NAD⁺. Because these downstream cofactors reside entirely on the separate XdhA polypeptide, XdhB alone cannot complete a full catalytic cycle — the physiologically active unit is the **XdhA₂B₂ heterotetramer**.

**Maturation dependency.** XdhB is synthesized as an apo-protein and must acquire its molybdopterin cofactor. The accessory factor XdhC (not a structural subunit) mediates or chaperones Moco insertion; without it, the tetramer assembles with FAD and [2Fe-2S] but lacks the Mo center and is inactive. This makes *xdhC* an obligatory partner gene for producing functional XdhB.

**Physiological role.** The whole module allows *P. putida* to route purine ring atoms into central metabolism, using purines/methylxanthines as nitrogen (and carbon) sources. The tight genomic linkage to *guaD* (which supplies xanthine) and the existence of the dedicated purine chemoreceptor McpH indicate this is an ecologically important, coordinated catabolic capacity rather than an incidental activity.

The one important caveat in interpretation concerns the **EC/name convention**. The submission names the enzyme "xanthine dehydrogenase" (EC 1.17.1.4, NAD⁺-linked), which is the most parsimonious assignment given the two-subunit architecture and pathway context. Some bacterial xanthine-oxidizing enzymes use O₂ or other acceptors; the precise terminal acceptor for the KT2440 enzyme has not been directly demonstrated in the primary literature reviewed here and is inferred from the EC assignment and the presence of an FAD/NAD-compatible XdhA subunit.

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports the annotation |
|------|-----------------|-------------------------------|
| [9515710](https://pubmed.ncbi.nlm.nih.gov/9515710/) | *Xanthine dehydrogenase from Rhodobacter capsulatus...* | Establishes the canonical bacterial two-subunit architecture: XDHB = molybdopterin (catalytic) subunit; XDHA = FAD + 2×[2Fe-2S]. Explains why single-chain cofactor annotations should not be propagated to the isolated XdhB subunit. |
| [1158847](https://pubmed.ncbi.nlm.nih.gov/1158847/) | *Metabolism of N-methylpurines by a P. putida strain* | Documents that in *P. putida* xanthine dehydrogenase (with uricase) oxidizes xanthine and drives conventional purine ring degradation — defining XdhB's pathway role. |
| [19447909](https://pubmed.ncbi.nlm.nih.gov/19447909/) | *Two distinct pathways for theophylline/caffeine metabolism in P. putida CBB5* | Confirms xanthine → uric acid oxidation and documents a broad-substrate-range xanthine-oxidizing enzyme that also produces methyluric acids. |
| [26355499](https://pubmed.ncbi.nlm.nih.gov/26355499/) | *Chemoreceptor for metabolizable purine derivatives (McpH)* | Places xanthine/hypoxanthine/uric acid in the KT2440 purine-degradation pathway used as nitrogen sources — the exact pathway of XdhB. |
| [10217763](https://pubmed.ncbi.nlm.nih.gov/10217763/) | *Role of XDHC in Moco insertion into XDH of R. capsulatus* | Establishes XdhC as an MPT insertase/chaperone required for XdhB activity, and defines the α₂β₂ (XdhA₂B₂) heterotetramer as the active form. |
| [37209475](https://pubmed.ncbi.nlm.nih.gov/37209475/) | *XO–osmundacetone interaction mechanism* | Confirms the molybdopterin (Mo-Pt) domain as the catalytic center oxidizing xanthine and hypoxanthine. |
| [32777423](https://pubmed.ncbi.nlm.nih.gov/32777423/) | *XO inhibitors in galangal* | Identifies conserved active-site residues (Arg880, Glu802) of the xanthine oxidoreductase Mo center embedded in the XdhB-type subunit. |
| [30397129](https://pubmed.ncbi.nlm.nih.gov/30397129/) | *Crystal structure of human mARC1* | Provides structural/evolutionary context for the broader molybdenum-enzyme (xanthine oxidase) superfamily. |
| [30545001](https://pubmed.ncbi.nlm.nih.gov/30545001/) | *From eukaryotic Moco biosynthesis to mARC* | Reviews Moco chemistry (pyranopterin + dithiolene chelating Mo) relevant to XdhB's cofactor. |

The evidence base combines (i) **direct organism-specific biochemistry** in *P. putida* (PMIDs 1158847, 19447909), (ii) **mechanistic homology** to the extensively characterized *R. capsulatus* two-subunit enzyme (PMIDs 9515710, 10217763), (iii) **genomic/physiological context** in KT2440 (PMID 26355499), (iv) **active-site conservation** from XO structural studies (PMIDs 37209475, 32777423), and (v) **structure prediction** (AlphaFold AF-Q88F20-F1, mean pLDDT 96.4). All lines converge on the same assignment.

---

## Limitations and Knowledge Gaps

1. **No direct enzymology on Q88F20 itself.** The functional assignment rests on domain architecture, genomic context, AlphaFold structure, and strong homology to characterized enzymes (*R. capsulatus* XDH; *P. putida* CBB5/other strains). No purified-protein kinetic study specific to the KT2440 PP_4279 gene product (Kₘ, kcat, substrate profile) has been identified.

2. **Terminal electron acceptor not experimentally established.** The EC 1.17.1.4 (NAD⁺) assignment is inferred. Whether the KT2440 enzyme preferentially uses NAD⁺ (dehydrogenase) versus O₂ (oxidase) or another acceptor in vivo has not been directly demonstrated in the primary literature reviewed.

3. **Molybdopterin form assumed.** The bacterial Mo-MCD (molybdopterin cytosine dinucleotide) form is inferred from homology; the exact pterin variant in KT2440 XdhB has not been chemically verified here.

4. **Quaternary structure by homology.** The XdhA₂B₂ heterotetramer is established for *R. capsulatus*; the precise stoichiometry/assembly of the KT2440 complex is presumed by homology, not directly measured.

5. **Substrate specificity breadth.** Broad methylxanthine oxidation is documented for *Pseudomonas* xanthine-oxidizing enzymes generally, but the quantitative substrate profile of the specific KT2440 XdhAB enzyme is not directly determined.

6. **Regulation.** How the *xdhABC-guaD* cluster is transcriptionally regulated in KT2440 (inducers, regulators) was not resolved in the reviewed literature, though induction by purine/caffeine growth is documented in related *P. putida* strains.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant expression and kinetic characterization.** Co-express PP_4278 (*xdhA*), PP_4279 (*xdhB*), and PP_4280 (*xdhC*) in a Moco-competent host; purify the complex and measure steady-state kinetics (Kₘ, kcat) for xanthine, hypoxanthine, and methylxanthines, using both NAD⁺ and O₂ as acceptors to settle the dehydrogenase-vs-oxidase question.

2. **Cofactor analysis.** Determine the molybdopterin variant (MCD vs. MPT) by HPLC/MS of the denatured cofactor, and confirm Mo, FAD, and [2Fe-2S] content by ICP-MS/UV-vis, verifying that XdhB carries only Mo and XdhA carries FAD + Fe-S.

3. **Genetic knockouts.** Construct clean *ΔxdhB* and *ΔxdhC* mutants in KT2440 and test growth on xanthine/hypoxanthine/guanine/uric acid as sole N (and C) sources to confirm the pathway assignment and the XdhC maturation dependency in this organism.

4. **Quaternary structure.** Use size-exclusion chromatography–MALS and/or cryo-EM to confirm the XdhA₂B₂ heterotetramer stoichiometry and to visualize the Mo→[2Fe-2S]→FAD electron-transfer wire.

5. **Substrate-range screen.** Assay the purified enzyme against a panel of purines and 1-/3-/7-methylxanthines and caffeine metabolites to quantify the "broad substrate range" specifically for the KT2440 enzyme.

6. **Structure with substrate.** Obtain a crystal or cryo-EM structure of XdhB with bound xanthine/urate or an inhibitor (e.g., allopurinol/febuxostat analogs) to confirm the active-site residues predicted from the AlphaFold model and homology (Arg/Glu catalytic residues, C8 orientation).

7. **Regulation.** Map the promoter and identify the transcriptional regulator of the *xdhABC-guaD* cluster, and test induction by purines and methylxanthines.

---

### Verification Statement

The gene symbol **xdhB** and organism ***Pseudomonas putida* KT2440** were confirmed against the UniProt record (Q88F20; PP_4279; EC 1.17.1.4; xanthine dehydrogenase family). The protein's domain complement (aldehyde-oxidase/xanthine-DH a/b hammerhead + MoCoBD1/MoCoBD2 molybdopterin-binding domains) is fully consistent with the catalytic subunit of a two-subunit bacterial xanthine dehydrogenase. Literature was drawn from *P. putida* purine/caffeine catabolism studies and from mechanistically homologous *R. capsulatus* XDH work; no evidence of gene-symbol ambiguity that would misdirect the annotation was found. The assignment is therefore made with high confidence.


## Artifacts

- [OpenScientist final report](xdhB-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](xdhB-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:9515710
2. PMID:1158847
3. PMID:19447909
4. PMID:26355499
5. PMID:10217763
6. PMID:37209475
7. PMID:32777423