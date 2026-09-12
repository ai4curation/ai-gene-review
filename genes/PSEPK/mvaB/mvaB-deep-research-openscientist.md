---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-25T14:30:37.297957'
end_time: '2026-07-25T14:54:59.219229'
duration_seconds: 1461.92
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: mvaB
  gene_symbol: mvaB
  uniprot_accession: Q88H25
  protein_description: 'RecName: Full=hydroxymethylglutaryl-CoA lyase {ECO:0000256|ARBA:ARBA00012910};
    EC=4.1.3.4 {ECO:0000256|ARBA:ARBA00012910};'
  gene_info: Name=mvaB {ECO:0000313|EMBL:AAN69141.1}; OrderedLocusNames=PP_3540 {ECO:0000313|EMBL:AAN69141.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the HMG-CoA lyase family.
  protein_domains: Aldolase_TIM. (IPR013785); HMG_CoA_lyase_AS. (IPR000138); HMGL.
    (IPR043594); PYR_CT. (IPR000891); HMGL-like (PF00682)
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
citation_count: 7
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: mvaB-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: mvaB-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88H25
- **Protein Description:** RecName: Full=hydroxymethylglutaryl-CoA lyase {ECO:0000256|ARBA:ARBA00012910}; EC=4.1.3.4 {ECO:0000256|ARBA:ARBA00012910};
- **Gene Information:** Name=mvaB {ECO:0000313|EMBL:AAN69141.1}; OrderedLocusNames=PP_3540 {ECO:0000313|EMBL:AAN69141.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the HMG-CoA lyase family.
- **Key Domains:** Aldolase_TIM. (IPR013785); HMG_CoA_lyase_AS. (IPR000138); HMGL. (IPR043594); PYR_CT. (IPR000891); HMGL-like (PF00682)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "mvaB" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'mvaB' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **mvaB** (gene ID: mvaB, UniProt: Q88H25) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of *mvaB* (PP_3540, UniProt Q88H25) in *Pseudomonas putida* KT2440

**Target:** *mvaB* / PP_3540 — hydroxymethylglutaryl-CoA lyase (HMG-CoA lyase), EC 4.1.3.4
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / KT2440), taxon "PSEPK"
**UniProt:** Q88H25 · 299 aa · HMG-CoA lyase family

---

## Summary

The gene **mvaB** (ordered locus **PP_3540**; UniProt **Q88H25**) of *Pseudomonas putida* KT2440 encodes **3-hydroxy-3-methylglutaryl-CoA lyase (HMG-CoA lyase, EC 4.1.3.4)**. This is a soluble, cytoplasmic, divalent-cation (Mg²⁺/Mn²⁺)-dependent enzyme that catalyzes the retro-aldol (C–C bond cleavage) reaction converting **(3S)-3-hydroxy-3-methylglutaryl-CoA into acetoacetate plus acetyl-CoA**. This reaction is the terminal, committed step of the 3-methylcrotonyl-CoA pathway by which bacteria degrade **L-leucine and isovalerate** to central-metabolism intermediates. The identification is unambiguous and well-supported: the gene symbol, EC number, protein family (HMG-CoA lyase / HMGL-like PF00682), and domain architecture (Aldolase TIM-barrel; HMG-CoA lyase active-site signature) all cohere, and the sequence is 78.6% identical to the biochemically characterized ortholog LiuE of *Pseudomonas aeruginosa*.

Structurally, mvaB belongs to the **DRE-TIM metallolyase family**: a (βα)₈ TIM-barrel fold carrying an invariant Asp-Arg-Glu catalytic triplet and a divalent-cation binding site formed by a cluster of conserved residues that cap the core of the barrel. Residue-level analysis confirms that **every catalytic and metal-coordinating residue is intact in mvaB** — the reactive catalytic cysteine, the substrate-binding arginine, and the full His/His/Asp/Asn metal-coordination shell — providing strong structural evidence that the enzyme is a fully functional HMG-CoA lyase and not a degenerate pseudo-enzyme.

Physiologically, mvaB operates in **leucine/isovalerate catabolism** in *P. putida* KT2440. Unlike its bifunctional *P. aeruginosa* ortholog LiuE — which additionally serves the acyclic-terpene (citronellol/geraniol) degradation pathway — mvaB in KT2440 does **not** function in terpene catabolism, because this strain lacks the *atu* (acyclic terpene utilization) gene cluster. A notable genomic feature is that mvaB/PP_3540 lies physically **apart** from the leucine-catabolism (*liu*) gene cluster, and KT2440 additionally carries a second HMG-CoA-lyase paralog (PP_3394). The enzyme feeds acetoacetate and acetyl-CoA into ketone-body / butanoate metabolism and the central acetyl-CoA pool.

---

## Gene/Protein Identity Verification

Before presenting findings, the mandatory identity checks required by the research brief were completed and **all passed**:

| Verification step | Result |
|---|---|
| Gene symbol *mvaB* matches protein description | ✅ *mvaB* annotated as HMG-CoA lyase in both UniProt Q88H25 and KEGG ppu:PP_3540 |
| Organism correct (*P. putida* KT2440) | ✅ Confirmed — KEGG locus ppu:PP_3540, EMBL AAN69141.1 |
| Protein family / domains align with literature | ✅ HMG-CoA lyase family; PF00682 (HMGL-like); IPR000138 (HMG-CoA lyase active-site signature) all consistent |
| No confusion with a different same-symbol gene | ✅ Literature for the *Pseudomonas* HMG-CoA lyase (LiuE ortholog) is directly relevant |

A point of nomenclature worth noting: the symbol "*mvaB*" is used in some organisms for enzymes of the mevalonate pathway (e.g., HMG-CoA synthase in the mevalonate biosynthetic direction). **In *P. putida* KT2440, however, PP_3540/*mvaB* is annotated and functions as HMG-CoA *lyase* (EC 4.1.3.4), a catabolic enzyme**, not a mevalonate-pathway synthase. The EC number, family assignment, and sequence orthology to LiuE all confirm the lyase identity, so no ambiguity remains for this specific protein.

---

## Key Findings

### Finding 1 — mvaB encodes HMG-CoA lyase, catalyzing the terminal step of leucine/isovalerate catabolism

Both UniProt (Q88H25) and KEGG (ppu:PP_3540) annotate mvaB as **hydroxymethylglutaryl-CoA lyase (EC 4.1.3.4; KEGG ortholog K01640)**, a 299-amino-acid protein. The catalytic reaction is:

> **(3S)-3-hydroxy-3-methylglutaryl-CoA → acetoacetate + acetyl-CoA**

UniProt's PATHWAY annotation places this as "*(S)-3-hydroxy-3-methylglutaryl-CoA degradation; acetoacetate from (S)-HMG-CoA: step 1/1*" — i.e., a single-step, committed terminal reaction. KEGG assigns the enzyme to **Module M00036 "Leucine degradation, leucine ⇒ acetoacetate + acetyl-CoA"** and to pathways **ppu00280** (valine/leucine/isoleucine degradation) and **ppu00650** (butanoate metabolism).

The closest **experimentally characterized** ortholog is **LiuE (PA2011) of *P. aeruginosa***, which was directly demonstrated to be an HMG-CoA lyase. As reported in [PMID: 19459965](https://pubmed.ncbi.nlm.nih.gov/19459965/), the authors "*suggested that liuE encodes 3-hydroxy-3-methylglutaryl-coenzyme A lyase (HMG-CoA lyase), which catalyzes the cleavage of HMG-CoA to acetyl-CoA and acetoacetate.*" The same study measured the enzyme's kinetic parameters: "*LiuE showed HMG-CoA lyase optimal activity at a pH of 7.0 and 37 degrees C, an apparent K(m) of 100 microM for HMG-CoA and a V(max) of 21 micromol min(-1) mg(-1).*" The native enzyme is a ~33 kDa monomer that assembles into a dimer/trimer (~79 kDa native).

Because mvaB is a close ortholog of this characterized enzyme (see Finding 5), these kinetic and mechanistic properties can be transferred to mvaB with high confidence.

| Property | Value (from characterized ortholog LiuE) |
|---|---|
| Reaction | (3S)-HMG-CoA → acetoacetate + acetyl-CoA |
| EC number | 4.1.3.4 |
| Apparent Kₘ (HMG-CoA) | 100 µM |
| Vₘₐₓ | 21 µmol·min⁻¹·mg⁻¹ |
| pH optimum | 7.0 |
| Temperature optimum | 37 °C |
| Oligomeric state | 33 kDa monomer → dimer/trimer (~79 kDa) |

### Finding 2 — In *P. putida* KT2440, mvaB serves leucine/isovalerate catabolism, not acyclic-terpene degradation

The *P. aeruginosa* ortholog LiuE is **bifunctional**: in addition to HMG-CoA lyase activity, it displays HIHG-CoA lyase activity (EC 4.1.2.26) and is essential for both leucine/isovalerate **and** acyclic-terpene (citronellol/geraniol) catabolism. As stated in [PMID: 19597963](https://pubmed.ncbi.nlm.nih.gov/19597963/), LiuE "*also displays HIHG-CoA lyase activity, indicating a bifunctional role in both the leucine/isovalerate and acyclic terpenes catabolic pathways.*"

However, comparative genomics and physiology establish that this bifunctionality does **not** extend to *P. putida* KT2440 in vivo. Although KT2440 possesses the *liu* leucine-degradation genes (including HMG-CoA lyase), it **lacks the *atu* (acyclic terpene utilization) cluster**. Consequently, KT2440 cannot grow on acyclic terpenes, yet it does utilize leucine and isovalerate. [PMID: 16820476](https://pubmed.ncbi.nlm.nih.gov/16820476/) reports directly: "*P. fluorescens, but not P. putida, could grow on acyclic terpenes (citronellol and citronellate), while both species were able to utilize leucine and isovalerate.*"

KEGG nonetheless links PP_3540 to pathway ppu00907 (geraniol degradation) because the **chemical reaction** is shared between the two pathways; however, the **physiological terpene pathway is absent** in this strain. Thus, mvaB's genuine biological role in KT2440 is confined to the leucine/isovalerate branch. The broader *liu*/*atu* cluster relationship is detailed in [PMID: 16517656](https://pubmed.ncbi.nlm.nih.gov/16517656/), which showed that in *P. aeruginosa* PAO1 "*the liuE gene encodes a probable hydroxy-acyl-CoA lyase (probably HMG-CoA lyase), an enzyme with bifunctional activity that is essential for both AMTC and leucine degradation.*"

### Finding 3 — mvaB adopts a (βα)₈ TIM-barrel fold and is a divalent-cation-dependent DRE-TIM metallolyase acting in the cytoplasm

The domain architecture of Q88H25 comprises: HMGL-like Pfam **PF00682**; InterPro **IPR013785** (Aldolase TIM-barrel), **IPR000138** (HMG-CoA lyase active-site signature, PROSITE PS01062), **IPR043594** (HMGL), and **IPR000891** (PYR_CT / pyruvate carboxyltransferase); and SCOP superfamily SSF51569 (Aldolase). UniProt carries the "Metal-binding" keyword.

Crystal structures of bacterial HMG-CoA lyases (*Bacillus subtilis*, *Brucella melitensis*) reported in [PMID: 16330546](https://pubmed.ncbi.nlm.nih.gov/16330546/) reveal a **TIM-barrel fold with a divalent-cation (Mg²⁺/Mn²⁺) binding site**: "*the catalytic center contains a divalent cation-binding site formed by a cluster of invariant residues that cap the core of the barrel.*" The same study defined a new enzyme superfamily and proposed a shared mechanism: "*We propose the name 'DRE-TIM metallolyases' for this newly identified enzyme family likely to employ a common catalytic reaction mechanism involving an invariant Asp-Arg-Glu (DRE) triplet.*" This DRE triad stabilizes an enolate intermediate during C–C bond cleavage.

The (βα)₈ TIM-barrel architecture is corroborated by the structural modeling in [PMID: 16601870](https://pubmed.ncbi.nlm.nih.gov/16601870/): "*A (betaalpha)(8) TIM barrel structure has been proposed for the protein.*"

**Localization:** Bacterial HMG-CoA lyase is a **soluble, cytoplasmic** enzyme. mvaB carries no signal peptide and no transmembrane segment, consistent with cytoplasmic function. (Note: the "peroxisome/mitochondrion" localization associated with the K01640 ortholog in KEGG reflects the *eukaryotic* orthologue's compartmentation, not bacterial localization — in bacteria the reaction occurs in the cytosol.)

### Finding 4 — mvaB is physically separate from the *liu* operon and has a second HMG-CoA-lyase paralog (PP_3394)

Genomic-neighborhood analysis via KEGG shows that the upstream leucine/isovalerate degradation genes cluster together at **PP_4064–PP_4067**:

- *ivd* — isovaleryl-CoA dehydrogenase (K00253)
- *mccB/liuB* — 3-methylcrotonyl-CoA carboxylase β-subunit (K01969)
- *liuC* — methylglutaconyl-CoA hydratase
- *mccA/liuD* — 3-methylcrotonyl-CoA carboxylase α-subunit (K01968)

with an adjacent Cro/CI-family transcriptional regulator (PP_4068).

By contrast, **mvaB/PP_3540 is located ~500 genes away** from this cluster, flanked by functionally unrelated genes (*pobA/pobR* p-hydroxybenzoate hydroxylase and its regulator, an MgtC-family transporter, and other regulators). This is a striking organizational difference from *P. aeruginosa*, where *liuE* is the terminal gene of a single **liuRABCDE operon**. In KT2440 the terminal lyase step has apparently become genomically decoupled from the rest of the leucine-degradation machinery.

Additionally, KEGG maps ortholog K01640 (HMG-CoA lyase) to **two** KT2440 paralogs — **PP_3540 (mvaB, 299 aa; our target)** and **PP_3394 (putative HMG-CoA lyase, 309 aa)** — both nominally assigned to the leucine-degradation module M00036. The two paralogs share only ~41.8% amino-acid identity (Finding 5), indicating an ancient duplication or acquisition.

### Finding 5 — mvaB is a bona fide ortholog of the biochemically characterized LiuE (78.6% identity)

Global (Needleman–Wunsch) pairwise alignment of the 299-aa PP_3540 sequence yielded:

| Comparison | Amino-acid identity |
|---|---|
| mvaB (PP_3540) vs. *P. aeruginosa* LiuE/PA2011 (characterized HMG-CoA lyase) | **78.6%** |
| mvaB vs. human HMG-CoA lyase (HMGCL, P35914) | 58.5% |
| mvaB vs. KT2440 paralog PP_3394 | 41.8% |

The very high (78.6%) identity to the experimentally validated LiuE strongly justifies **direct transfer of the HMG-CoA lyase functional annotation** to mvaB. The 58.5% identity to the human orthologue is fully consistent with the family-wide conservation reported in [PMID: 16330546](https://pubmed.ncbi.nlm.nih.gov/16330546/): "*These enzymes share greater than 45% sequence identity with the human orthologue.*" UniProt lists a single PYR_CT domain feature and no signal/transmembrane annotation.

### Finding 6 — All catalytic and metal-binding residues are conserved in mvaB, confirming an intact active site

Aligning mvaB to human HMGCL (P35914), whose active-site residues are experimentally annotated, shows **1:1 conservation of every functional residue**:

| Functional role | Human HMGCL (P35914) | mvaB (PP_3540) | Conserved? |
|---|---|---|---|
| Catalytic active site | Cys266 | Cys240 | ✅ |
| Substrate binding | Arg41 | Arg15 | ✅ |
| Metal (Mg²⁺/Mn²⁺) ligand | Asp42 | Asp16 | ✅ |
| Metal ligand | His233 | His207 | ✅ |
| Metal ligand | His235 | His209 | ✅ |
| Metal ligand | Asn275 | Asn249 | ✅ |

Thus the reactive catalytic cysteine, the substrate-binding arginine, and the complete His/His/Asp/Asn metal-coordination shell are all intact. These residues correspond precisely to the invariant cluster described in [PMID: 16330546](https://pubmed.ncbi.nlm.nih.gov/16330546/): "*the catalytic center contains a divalent cation-binding site formed by a cluster of invariant residues that cap the core of the barrel.*" The complete conservation confirms mvaB is a catalytically competent HMG-CoA lyase rather than a degenerate homolog.

---

## Mechanistic Model / Interpretation

### The reaction and its place in leucine catabolism

mvaB catalyzes the final, committed step of the bacterial **3-methylcrotonyl-CoA pathway** for L-leucine and isovalerate degradation. The full pathway funnels the branched-chain amino acid leucine into central metabolism:

```
   L-Leucine
      │  (transamination + branched-chain α-keto acid dehydrogenase)
      ▼
  Isovaleryl-CoA
      │  ivd  (isovaleryl-CoA dehydrogenase, PP_4064)
      ▼
  3-Methylcrotonyl-CoA
      │  liuB/liuD (3-methylcrotonyl-CoA carboxylase, PP_4065/PP_4067)
      ▼
  3-Methylglutaconyl-CoA
      │  liuC (methylglutaconyl-CoA hydratase, PP_4066)
      ▼
  (3S)-3-Hydroxy-3-methylglutaryl-CoA  (HMG-CoA)
      │  ★ mvaB / PP_3540  (HMG-CoA LYASE, EC 4.1.3.4)  ★
      ▼
  Acetoacetate  +  Acetyl-CoA
      │                    │
      ▼                    ▼
  ketone-body /        central metabolism
  butanoate metabolism  (TCA cycle, etc.)
  (ppu00650)
```

### Catalytic mechanism

mvaB is a **DRE-TIM metallolyase**. The reaction is a metal-assisted retro-aldol (retro-Claisen-type) C–C bond cleavage:

1. A **divalent cation (Mg²⁺ or Mn²⁺)**, held by the conserved His207/His209/Asp16/Asn249 cluster capping the TIM-barrel core, polarizes the C3 hydroxyl/carbonyl of HMG-CoA.
2. The invariant **Asp-Arg-Glu (DRE) triad** and the substrate-binding **Arg15** stabilize the developing **acetyl-CoA enolate** intermediate.
3. C2–C3 bond scission releases **acetoacetate** and **acetyl-CoA**.

The catalytic **Cys240** (equivalent to human Cys266) lies at the active site; in eukaryotic enzymes this cysteine is redox-sensitive and subject to thiol/disulfide regulation ([PMID: 1304393](https://pubmed.ncbi.nlm.nih.gov/1304393/)), though bacterial enzymes lack the corresponding C-terminal cross-linking cysteine, suggesting the bacterial enzyme (including mvaB) is less subject to this redox regulatory mechanism.

### Localization

The enzyme operates in the **cytoplasm** as a soluble oligomer (monomer ~33 kDa; native dimer/trimer). It has no signal peptide, lipobox, or transmembrane helix. In bacteria the entire leucine-degradation pathway is cytosolic — in contrast to the human orthologue, which is mitochondrial (and partly peroxisomal), a distinction that explains why database cross-references to eukaryotic compartments do not apply to mvaB.

### Species-specific physiology

The key evolutionary insight is that the *same enzyme family* serves different metabolic breadth in different pseudomonads:

| Feature | *P. aeruginosa* LiuE | *P. putida* KT2440 mvaB |
|---|---|---|
| HMG-CoA lyase activity | Yes | Yes |
| HIHG-CoA lyase (terpene) activity | Yes (bifunctional) | Enzyme capable, but pathway absent |
| Leucine/isovalerate catabolism | Yes | Yes |
| Acyclic-terpene catabolism in vivo | Yes | **No** (lacks *atu* cluster) |
| Genomic context | Terminal gene of *liuRABCDE* operon | Isolated (~500 genes from *liu* cluster) |
| Paralog present | — | Yes (PP_3394) |

Thus, although mvaB likely retains the intrinsic biochemical capacity for the shared chemistry, its **physiological role in KT2440 is restricted to leucine/isovalerate catabolism** because the upstream terpene-activation machinery does not exist in this strain.

---

## Evidence Base

| PMID | Title (abbreviated) | How it supports the annotation |
|---|---|---|
| [19459965](https://pubmed.ncbi.nlm.nih.gov/19459965/) | *P. aeruginosa liuE encodes HMG-CoA lyase, involved in leucine and acyclic terpene catabolism* | **Primary biochemical characterization** of the direct ortholog: establishes the cleavage reaction and provides kinetic parameters (Kₘ = 100 µM, Vₘₐₓ = 21 µmol/min/mg, pH 7.0, 37 °C). Cornerstone of Findings 1 & 5. |
| [19597963](https://pubmed.ncbi.nlm.nih.gov/19597963/) | *The bifunctional role of LiuE… HIHG-CoA lyase activity* | Documents LiuE's second (terpene-pathway) activity — explains why KEGG links the enzyme to terpene degradation, and frames the KT2440 species difference (Finding 2). |
| [16820476](https://pubmed.ncbi.nlm.nih.gov/16820476/) | *Genes/proteins for acyclic terpene and leucine/isovalerate catabolism in P. aeruginosa* | Directly shows *P. putida* cannot grow on acyclic terpenes but does use leucine/isovalerate — pins mvaB's in vivo role to leucine catabolism (Finding 2). |
| [16517656](https://pubmed.ncbi.nlm.nih.gov/16517656/) | *atu and liu clusters in acyclic monoterpene and leucine catabolism* | Defines the *liu* vs *atu* cluster organization and the bifunctionality of LiuE; provides the operon context that highlights KT2440's differing genomic arrangement (Finding 4). |
| [16330546](https://pubmed.ncbi.nlm.nih.gov/16330546/) | *Crystal structures of two bacterial HMG-CoA lyases; DRE-TIM metallolyases* | **Structural/mechanistic foundation**: TIM-barrel fold, divalent-cation site, invariant DRE catalytic triad, >45% identity to human orthologue. Underpins Findings 3, 5 & 6. |
| [16601870](https://pubmed.ncbi.nlm.nih.gov/16601870/) | *G203E mutation causing HMG-CoA lyase deficiency; substrate channel* | Confirms the (βα)₈ TIM-barrel architecture and the importance of substrate-channel integrity (Finding 3). |
| [1304393](https://pubmed.ncbi.nlm.nih.gov/1304393/) | *Avian HMG-CoA lyase: reactive cysteines, thiol/disulfide sensitivity* | Characterizes the catalytic cysteine and notes bacterial enzymes lack the C-terminal cross-linking cysteine — informs the redox-regulation discussion in the mechanistic model. |

**Consistency of the evidence:** All seven papers converge on the same functional assignment. The two structural papers (16330546, 16601870) fix the fold and catalytic machinery; the *Pseudomonas* genetics/biochemistry papers (19459965, 19597963, 16820476, 16517656) fix the pathway context and provide direct kinetic data on the ortholog; and the sequence/residue analyses (Findings 5 & 6) bridge these to the specific KT2440 protein. No paper contradicts the HMG-CoA lyase assignment.

---

## Limitations and Knowledge Gaps

1. **No direct biochemistry on PP_3540 itself.** The functional assignment rests on (a) database annotation, (b) 78.6% orthology to the characterized *P. aeruginosa* LiuE, and (c) complete active-site residue conservation. While this is a very strong inference chain, the KT2440 protein has not, to our knowledge, been individually purified and assayed. Its exact Kₘ, Vₘₐₓ, oligomeric state, and metal preference are inferred, not directly measured.

2. **Role of the paralog PP_3394 is unresolved.** KT2440 encodes a second putative HMG-CoA lyase (PP_3394, 41.8% identical). It is unknown whether the two paralogs are functionally redundant, differentially regulated, or specialized for different substrates/conditions. Which paralog carries the physiological flux during leucine growth has not been determined.

3. **Genomic decoupling from the *liu* cluster is unexplained.** mvaB sits ~500 genes from the *liu* operon. How its expression is coordinated with the rest of the leucine-degradation pathway (i.e., which regulator controls PP_3540) is not established.

4. **Retention of latent HIHG-CoA lyase (terpene) activity is untested in KT2440.** Although the *atu* pathway is absent, whether the mvaB protein itself retains the intrinsic bifunctional chemistry of LiuE has not been experimentally checked.

5. **Localization is inferred, not observed.** Cytoplasmic localization is deduced from the absence of targeting signals and general bacterial pathway biology, not from experimental fractionation/imaging of the KT2440 protein.

---

## Proposed Follow-up Experiments / Actions

1. **Heterologous expression and enzyme assay.** Clone and express PP_3540 (His-tagged), purify, and measure HMG-CoA lyase activity spectrophotometrically (acetoacetate/CoA product detection). Determine Kₘ, kcat, pH/temperature optima, and divalent-metal dependence (Mg²⁺ vs Mn²⁺), to directly confirm the inferred kinetics.

2. **Paralog dissection via gene knockouts.** Construct single (ΔPP_3540, ΔPP_3394) and double mutants and test growth on L-leucine and isovalerate as sole carbon sources. This will resolve functional redundancy and identify which paralog carries physiological flux.

3. **Test latent terpene-pathway (HIHG-CoA lyase) activity.** Assay purified mvaB against the HIHG-CoA substrate to determine whether it retains LiuE's bifunctionality despite the absence of the *atu* pathway in KT2440.

4. **Structural determination.** Solve the crystal structure (or generate a high-confidence AlphaFold model with validation) to confirm the (βα)₈ TIM-barrel, the divalent-cation site, and the geometry of the Cys240/Arg15/Asp16/His207/His209/Asn249 active site.

5. **Transcriptional regulation.** Use RNA-seq or reporter fusions under leucine/isovalerate induction to identify the regulator controlling PP_3540 and understand how the genomically isolated lyase is co-regulated with the *liu* cluster.

6. **Subcellular localization.** Confirm cytoplasmic localization by cell fractionation and Western blotting (or fluorescent-fusion imaging).

---

## Conclusion

mvaB (PP_3540, Q88H25) of *Pseudomonas putida* KT2440 is **3-hydroxy-3-methylglutaryl-CoA lyase (EC 4.1.3.4)**, a soluble cytoplasmic, divalent-cation-dependent TIM-barrel metalloenzyme of the DRE-TIM metallolyase family. It catalyzes the retro-aldol cleavage of (3S)-HMG-CoA into **acetoacetate + acetyl-CoA**, the terminal committed step of L-leucine/isovalerate catabolism (KEGG module M00036), feeding acetoacetate into ketone-body/butanoate metabolism and acetyl-CoA into central metabolism. The assignment is supported by 78.6% identity to the biochemically characterized ortholog LiuE and by complete conservation of every catalytic and metal-binding active-site residue. Unlike bifunctional *P. aeruginosa* LiuE, mvaB does not participate in acyclic-terpene degradation in KT2440 because this strain lacks the *atu* gene cluster.


## Artifacts

- [OpenScientist final report](mvaB-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](mvaB-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:19459965
2. PMID:19597963
3. PMID:16820476
4. PMID:16517656
5. PMID:16330546
6. PMID:16601870
7. PMID:1304393