---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-11T17:51:31.294852'
end_time: '2026-07-11T18:05:44.839436'
duration_seconds: 853.54
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: mqo2
  gene_symbol: mqo2
  uniprot_accession: Q88NF9
  protein_description: 'RecName: Full=Probable malate:quinone oxidoreductase 2 {ECO:0000255|HAMAP-Rule:MF_00212};
    EC=1.1.5.4 {ECO:0000255|HAMAP-Rule:MF_00212}; AltName: Full=MQO 2 {ECO:0000255|HAMAP-Rule:MF_00212};
    AltName: Full=Malate dehydrogenase [quinone] 2 {ECO:0000255|HAMAP-Rule:MF_00212};'
  gene_info: Name=mqo2 {ECO:0000255|HAMAP-Rule:MF_00212}; Synonyms=mqo-2; OrderedLocusNames=PP_1251;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the MQO family. {ECO:0000255|HAMAP-
  protein_domains: FAD/NAD-bd_sf. (IPR036188); MQO. (IPR006231); Mqo (PF06039)
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
citation_count: 6
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: mqo2-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: mqo2-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88NF9
- **Protein Description:** RecName: Full=Probable malate:quinone oxidoreductase 2 {ECO:0000255|HAMAP-Rule:MF_00212}; EC=1.1.5.4 {ECO:0000255|HAMAP-Rule:MF_00212}; AltName: Full=MQO 2 {ECO:0000255|HAMAP-Rule:MF_00212}; AltName: Full=Malate dehydrogenase [quinone] 2 {ECO:0000255|HAMAP-Rule:MF_00212};
- **Gene Information:** Name=mqo2 {ECO:0000255|HAMAP-Rule:MF_00212}; Synonyms=mqo-2; OrderedLocusNames=PP_1251;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the MQO family. {ECO:0000255|HAMAP-
- **Key Domains:** FAD/NAD-bd_sf. (IPR036188); MQO. (IPR006231); Mqo (PF06039)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "mqo2" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'mqo2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **mqo2** (gene ID: mqo2, UniProt: Q88NF9) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *mqo2* (Q88NF9, PP_1251) in *Pseudomonas putida* KT2440

## Summary

**The gene *mqo2* (UniProt Q88NF9; ordered locus PP_1251) of *Pseudomonas putida* KT2440 encodes Malate:quinone oxidoreductase 2 (MQO 2), an FAD-dependent flavoenzyme that oxidizes L-(S)-malate to oxaloacetate while transferring the abstracted electrons to a membrane quinone rather than to NAD⁺.** The reaction it catalyzes is `(S)-malate + a quinone → oxaloacetate + a quinol` (EC 1.1.5.4; formerly EC 1.1.99.16). This is the oxaloacetate-regenerating (malate → OAA) step of the tricarboxylic acid (TCA) cycle, but instead of producing NADH the enzyme deposits reducing equivalents directly into the respiratory quinone pool, thereby fusing this metabolic step to the aerobic electron-transport chain and to proton-motive-force generation.

MQO 2 is a **peripheral membrane flavoprotein** that operates on the cytoplasmic face of the inner (cytoplasmic) membrane. It is not an integral membrane protein: sequence and hydropathy analysis of the 527-residue chain reveal an N-terminal FAD-binding Rossmann fold but no transmembrane helix, consistent with the experimental observation in the orthologous *Corynebacterium glutamicum* enzyme that MQO can be stripped from the membrane by chelators. FAD is a tightly, but non-covalently, bound prosthetic group.

The functional assignment for the *P. putida* protein is made primarily by strong homology rather than direct biochemical study. *mqo2* is one of **three MQO paralogs** in *P. putida* KT2440 (*mqo1*/PP_0751, *mqo2*/PP_1251, *mqo3*/PP_2925), and of these it is the paralog most similar (~70% identity) to the biochemically characterized *Escherichia coli* MQO. It is independently assigned by KEGG to orthology K00116 (EC 1.1.5.4) and mapped to the TCA cycle, pyruvate metabolism, and the methylcitrate cycle. Direct enzymological characterization of the *P. putida* protein itself has not yet been performed; the model rests on conserved catalytic architecture (HAMAP rule MF_00212, Pfam PF06039) and on the well-established enzymology of its orthologs in *E. coli* and *C. glutamicum*.

---

## Gene / Protein Identity Verification

Before presenting findings, the target identity was explicitly verified against the UniProt record, satisfying all mandatory checks:

| Attribute | Target (from UniProt) | Verified in this investigation |
|---|---|---|
| Accession | Q88NF9 | Confirmed via UniProt REST API (527 aa, 58.1 kDa) |
| Gene symbol | *mqo2* (syn. *mqo-2*) | Matches UniProt record; KEGG lists as *mqo-II* |
| Locus | PP_1251 | Confirmed (KEGG ppu:PP_1251) |
| Organism | *P. putida* KT2440 (taxid 160488) | Confirmed |
| Protein family | MQO family | Pfam PF06039, InterPro IPR006231 |
| Key domains | FAD/NAD-bd_sf (IPR036188); MQO (IPR006231); Mqo (PF06039) | Rossmann fingerprint identified at res 14–19 |
| EC number | 1.1.5.4 | Assigned by HAMAP MF_00212 |

**The gene symbol, organism, protein family, and domain architecture are all mutually consistent, confirming the correct target.** No conflicting literature for a different "mqo2" gene was encountered. The main caveat is that literature specific to the *P. putida* enzyme is limited, so the functional narrative is built on orthologs and on well-conserved sequence/structure features (see Limitations).

---

## Key Findings

### F001 — MQO 2 catalyzes FAD-dependent, quinone-linked oxidation of malate to oxaloacetate (EC 1.1.5.4)

The UniProt record for Q88NF9 (verified via REST API) describes a 527-amino-acid, 58.1-kDa protein annotated as malate:quinone oxidoreductase 2 with the catalytic activity **"(S)-malate + a quinone = a quinol + oxaloacetate."** The cofactor is FAD, and the enzyme is placed in the TCA cycle at the step "oxaloacetate from (S)-malate (quinone route): step 1/1." Its keyword set — FAD, Flavoprotein, Oxidoreductase, Tricarboxylic acid cycle — encapsulates its chemistry. At the sequence level the N-terminus carries a Rossmann-type dinucleotide-binding fingerprint (…VLLVGGGIMSS… near residues 11–19) that is diagnostic of the FAD/NAD-binding superfamily domain (IPR036188) and of the Pfam Mqo domain (PF06039).

The reaction chemistry is anchored by enzymology performed on the orthologous *C. glutamicum* enzyme, which established that MQO **oxidizes L-malate to oxaloacetate and donates electrons to ubiquinone-1** (and to artificial acceptors, or via the electron-transfer chain to oxygen), and that **NAD is not an acceptor** — the natural direct acceptor is most likely a quinone [PMID: 9660197](https://pubmed.ncbi.nlm.nih.gov/9660197/). The same study showed that **FAD is a tightly but non-covalently bound prosthetic group** and that the enzyme is activated by lipids. In *E. coli*, the gene *mqo* was defined as encoding the **membrane-associated malate:quinone-oxidoreductase (MQO)** [PMID: 11092847](https://pubmed.ncbi.nlm.nih.gov/11092847/) (the EC number was later renumbered from 1.1.99.16 to 1.1.5.4). Together these establish both the substrate specificity (L-/(S)-malate) and the electron acceptor (quinone, not NAD⁺) that define MQO 2's primary function.

Mechanistically, catalysis proceeds by reduction of the enzyme-bound FAD by malate (yielding oxaloacetate and reduced flavin), followed by reoxidation of the flavin by a membrane quinone (yielding quinol). Because the quinone/quinol couple has a substantially higher midpoint potential than the NAD⁺/NADH couple, coupling malate oxidation to quinone reduction makes this step strongly thermodynamically favorable and effectively **irreversible** in the oxidative direction — in contrast to the near-equilibrium, reversible reaction of the NAD-dependent malate dehydrogenase (MDH, EC 1.1.1.37).

### F002 — MQO is a peripheral inner-membrane flavoprotein feeding TCA electrons to the quinone pool

MQO carries out its half-reaction at the cytoplasmic face of the inner membrane. Crucially, the *C. glutamicum* ortholog is a **peripheral membrane protein that can be released from the membrane by addition of chelators** [PMID: 9660197](https://pubmed.ncbi.nlm.nih.gov/9660197/) — behavior characteristic of a protein anchored by surface association rather than by a transmembrane span. In *E. coli* the enzyme is likewise described as **membrane-associated** [PMID: 11092847](https://pubmed.ncbi.nlm.nih.gov/11092847/). Functionally, malate oxidation occurs on the cytoplasmic side (oxidizing cytoplasmic L-malate and releasing cytoplasmic oxaloacetate) while quinone is reduced within the lipid bilayer; the enzyme therefore physically bridges the cytoplasmic metabolite pool and the membrane quinone pool, directly coupling the TCA cycle to aerobic respiration and to proton-motive-force generation. UniProt localizes the activity to the cell (inner-membrane periphery) and annotates no soluble, periplasmic, or secreted signal.

### F003 — MQO performs the malate → oxaloacetate TCA step and its flux is redox-regulated

UniProt places Q88NF9 at the TCA-cycle step "oxaloacetate from (S)-malate (quinone route): step 1/1." Physiological studies of orthologs demonstrate that this step can be biologically dominant and is tightly integrated with cellular redox state. In *C. glutamicum*, **MQO is the principal enzyme catalyzing the oxidation of malate to oxaloacetate** [PMID: 11092847](https://pubmed.ncbi.nlm.nih.gov/11092847/), and an *mqo*-null mutant grows poorly on several substrates despite retaining an intact NAD-dependent malate dehydrogenase. In *E. coli*, both MQO and the cytoplasmic NAD-MDH are simultaneously active, and *mqo* transcription is controlled by the **ArcA–ArcB two-component (redox/O₂-sensing) system**, peaking during exponential aerobic growth and dropping in stationary phase [PMID: 11092847](https://pubmed.ncbi.nlm.nih.gov/11092847/). The redox-sensitive nature of the enzyme's flux is underscored by metabolic-engineering work in *C. glutamicum*, where disrupting *mqo* increased L-lysine production by ~18%: **loss of MQO activity down-regulates TCA-cycle flux to maintain redox balance and redirects oxaloacetate into L-lysine biosynthesis** [PMID: 17090916](https://pubmed.ncbi.nlm.nih.gov/17090916/). This positions MQO at a key oxaloacetate branch point that partitions carbon between energy-yielding oxidation and biosynthesis (aspartate/lysine biosynthesis and, via PEP carboxykinase, gluconeogenesis).

### F004 — *P. putida* KT2440 encodes three MQO paralogs; *mqo2* is one member of an expanded family

A proteome query of *P. putida* KT2440 (taxid 160488) returns three distinct MQO-family proteins: **Q88PU7 *mqo1* (PP_0751, 502 aa), Q88NF9 *mqo2* (PP_1251, 527 aa), and Q88IS4 *mqo3* (PP_2925, 539 aa)**. All three are assigned EC 1.1.5.4 by HAMAP rule MF_00212 and belong to the MQO family (Pfam PF06039, InterPro IPR006231). This paralog expansion contrasts sharply with *E. coli* and *C. glutamicum*, each of which carries a single *mqo* gene. The gene name *mqo2* and locus PP_1251 exactly match the target UniProt record, reconfirming gene identity. The existence of three paralogs raises the possibility of functional specialization (e.g., different quinone preferences, expression conditions, or subtle substrate differences) or condition-specific redundancy, although all retain the canonical catalytic architecture. This is biologically plausible for *P. putida*, an obligately aerobic, metabolically versatile soil bacterium with a TCA-centric, respiration-driven lifestyle.

### F005 — *mqo2* is the paralog closest to the biochemically characterized *E. coli* MQO (~70% identity)

Pairwise global (Needleman–Wunsch) alignments computed in this investigation place *mqo2* as the *P. putida* paralog most similar to the experimentally characterized enterobacterial enzyme:

| Comparison | % identity |
|---|---|
| **mqo2 (PP_1251) vs *E. coli* MQO (P33940)** | **70.2%** |
| mqo3 (PP_2925) vs *E. coli* MQO | 65.9% |
| mqo1 (PP_0751) vs *E. coli* MQO | 57.4% |
| mqo2 vs mqo3 | 79.9% |
| mqo1 vs mqo2 / mqo3 | 55.8–57.4% |

The pattern indicates that **mqo2 and mqo3 arose from a comparatively recent duplication** (they are ~80% identical to each other), whereas **mqo1 is an ancient outgroup paralog**. Because *mqo2* is the closest homolog of the enzyme whose reaction, cofactor, and acceptor are experimentally established, homology-based transfer of the canonical malate:quinone oxidoreductase function to *mqo2* is well supported. The FAD/NAD-binding Rossmann domain and the MQO signature (PF06039) are conserved across all three paralogs.

### F006 — KEGG independently assigns *mqo2* to K00116/EC 1.1.5.4; the gene sits among mobile genetic elements

KEGG independently corroborates the annotation: **ppu:PP_1251 (name *mqo-II*) → ORTHOLOGY K00116, malate dehydrogenase (quinone) [EC 1.1.5.4]**, mapped to pathways ppu00020 (Citrate/TCA cycle), ppu00620 (Pyruvate metabolism), ppu01200 (Carbon metabolism), and ppu01120 (Microbial metabolism in diverse environments), and to modules M00009 (TCA cycle), M00011 (second carbon oxidation, 2-oxoglutarate → oxaloacetate), and M00982 (methylcitrate cycle). Thus two independent annotation systems (UniProt/HAMAP and KEGG) converge on the same identity and pathway placement.

Notably, the **genomic neighborhood of *mqo2* is not a metabolic operon**: PP_1249 is a DUF4223 protein, PP_1250 and PP_1252 are group-II-intron-encoded maturases, and PP_1253 is an ArsR-family transcriptional regulator. In other words, *mqo2* is flanked by mobile genetic elements rather than by co-transcribed TCA or respiratory-chain genes. This context is consistent with the MQO paralog expansion having involved duplication/mobile-element-associated events, and implies *mqo2* is regulated in *trans* (as the single *E. coli mqo* is, via ArcAB) rather than by co-transcribed metabolic partners.

### F007 — Structural inference: N-terminal FAD-binding Rossmann fold and no transmembrane helix

Direct sequence/structure analysis of Q88NF9 (527 aa) supports a peripheral, not integral, membrane flavoprotein. The N-terminus contains the βαβ dinucleotide-binding fingerprint **"LLVGGG" at residues 14–19** (within …VDVLLVGGGIMSSTLAVWLH…), the hallmark of the FAD/NAD-binding Rossmann superfamily (IPR036188) and the diagnostic N-terminal motif of the MQO family (PF06039). A Kyte–Doolittle hydropathy scan (window 19) shows a single region exceeding the membrane-interaction threshold (window-mean 1.70) at residues ~11–29 — but this coincides precisely with the **buried FAD-binding hydrophobic core**, not a discrete transmembrane span. No other segment anywhere in the 527-residue chain reaches transmembrane-helix hydrophobicity. This structural evidence independently reinforces F002: MQO 2 is a peripheral membrane protein — a soluble catalytic core docked at the membrane surface where the reduced flavin reduces membrane quinone — rather than an integral, membrane-spanning enzyme.

---

## Mechanistic Model / Interpretation

The findings converge on a coherent mechanistic picture in which MQO 2 acts as an interface between the soluble TCA cycle and the membrane respiratory chain.

```
             CYTOPLASM (inner-membrane cytoplasmic face)
   ┌───────────────────────────────────────────────────────────┐
   │                                                             │
   │   (S)-malate ──────────►  oxaloacetate                     │
   │        \                     ↑                             │
   │         \   [ MQO 2 / PP_1251 ]  (peripheral flavoprotein) │
   │          \      FAD (non-covalent)                          │
   │           \        │  2e⁻                                   │
   │            ▼        ▼                                        │
   │========== quinone ⇌ quinol ===============================  │  INNER
   │              (ubiquinone / demethylmenaquinone pool)        │  MEMBRANE
   └───────────────────────────────────────────────────────────┘
                          │  electrons
                          ▼
              Terminal oxidases → O₂ (aerobic respiration)
                          │
                          ▼
              Proton-motive force → ATP synthesis
```

**Reaction and energetics.** MQO 2 abstracts a hydride from (S)-malate, forming oxaloacetate, and passes the electrons via its tightly-bound FAD to a membrane quinone (F001). Unlike the canonical NAD⁺-dependent malate dehydrogenase, MQO does not generate NADH; instead it reduces quinone directly (F001, [PMID: 9660197](https://pubmed.ncbi.nlm.nih.gov/9660197/)). This makes the malate → OAA reaction essentially irreversible in the oxidative direction under aerobic conditions and couples it energetically to the respiratory chain and proton-motive force (F002). By feeding electrons in at the quinone level, MQO also bypasses the need to reoxidize NADH at Complex I.

**Localization.** The enzyme works at the cytoplasmic face of the inner membrane as a peripheral flavoprotein — supported both experimentally in orthologs (chelator-releasable; [PMID: 9660197](https://pubmed.ncbi.nlm.nih.gov/9660197/)) and by structural inference for the *P. putida* protein (Rossmann FAD fold, no TM helix; F007).

**Metabolic role and regulation.** MQO performs step 1/1 of the "oxaloacetate from (S)-malate (quinone route)" and, in at least some bacteria, is the principal enzyme for this step (F003). Its activity is redox/oxygen-responsive (ArcA–ArcB regulation in *E. coli*) and sits at the oxaloacetate branch point that partitions carbon between continued TCA oxidation and biosynthetic withdrawal (as demonstrated by L-lysine overproduction upon *mqo* disruption in *C. glutamicum*; [PMID: 17090916](https://pubmed.ncbi.nlm.nih.gov/17090916/)). KEGG additionally maps the enzyme to pyruvate metabolism and the methylcitrate cycle (F006), consistent with its central position in oxaloacetate handling.

**Paralog context.** *P. putida* has expanded the MQO family to three copies (F004). *mqo2* is the copy most similar to the characterized *E. coli* enzyme (F005), making it the best candidate for the "canonical" housekeeping MQO function, while its residence among mobile genetic elements (F006) hints that its regulation and physiological deployment may differ from the core respiratory genes. The near-identity between *mqo2* and *mqo3* suggests these two provide overlapping or condition-specific malate:quinone oxidoreductase capacity, whereas the divergent *mqo1* may have specialized.

### Comparison: MQO vs. NAD-dependent MDH

| Feature | MQO 2 (this gene, EC 1.1.5.4) | NAD-MDH (EC 1.1.1.37) |
|---|---|---|
| Electron acceptor | Membrane quinone | NAD⁺ |
| Cofactor | Non-covalent FAD | None (uses NAD⁺) |
| Localization | Peripheral inner-membrane | Soluble cytoplasmic |
| Thermodynamics | Essentially irreversible (oxidative) | Near-equilibrium, reversible |
| Respiratory coupling | Direct (feeds quinone pool) | Indirect (NADH → Complex I) |

---

## Evidence Base

| PMID | Title | Relevance |
|---|---|---|
| [9660197](https://pubmed.ncbi.nlm.nih.gov/9660197/) | *Biochemical and genetic characterization of the membrane-associated malate dehydrogenase (acceptor) from Corynebacterium glutamicum.* | **Core enzymology.** Establishes that MQO oxidizes L-malate to oxaloacetate, donates electrons to ubiquinone (not NAD), uses FAD as a non-covalent prosthetic group, and is a chelator-releasable peripheral membrane protein. Directly supports F001, F002. |
| [11092847](https://pubmed.ncbi.nlm.nih.gov/11092847/) | *Functions of the membrane-associated and cytoplasmic malate dehydrogenases in the citric acid cycle of Escherichia coli.* | **Gene/function and regulation.** Defines *mqo* as encoding membrane-associated MQO; shows MQO can be the principal malate→OAA enzyme and that its transcription is ArcA–ArcB (redox/O₂) regulated. Supports F001, F002, F003. |
| [17090916](https://pubmed.ncbi.nlm.nih.gov/17090916/) | *Disruption of malate:quinone oxidoreductase increases L-lysine production by Corynebacterium glutamicum.* | **Metabolic role.** Demonstrates MQO's control over TCA flux and the oxaloacetate branch point; loss redirects OAA into biosynthesis to preserve redox balance. Supports F003. |
| [42203459](https://pubmed.ncbi.nlm.nih.gov/42203459/) | *Mitochondrial Membrane-Associated L-2-Hydroxyglutarate Dehydrogenase Catalyzes Electron Transport to Ubiquinone In Vitro.* | **Comparative flavoenzyme mechanism.** Confirms that homologous FAD membrane dehydrogenases reduce ubiquinone and are inhibited by ferulenol; explicitly references MQO as the homologous quinone-reducing enzyme. Contextual support for the quinone-acceptor mechanism. |
| [19505951](https://pubmed.ncbi.nlm.nih.gov/19505951/) | *Siccanin rediscovered as a species-selective succinate dehydrogenase inhibitor.* | **Respiratory-chain context.** Illustrates *P. putida* membrane-bound quinone-linked dehydrogenases and quinone-binding-site pharmacology; contextual for membrane/quinone coupling. |
| [39969994](https://pubmed.ncbi.nlm.nih.gov/39969994/) | *Cryo-EM of native membranes reveals an intimate connection between the Krebs cycle and aerobic respiration in mycobacteria.* | **Systems context.** Supports the general model that TCA-cycle membrane dehydrogenases are structurally and functionally coupled to aerobic respiration. |
| [34150510](https://pubmed.ncbi.nlm.nih.gov/34150510/) | *Effect of pyruvate kinase gene deletion on the physiology of [Pseudomonas].* | **Organism context.** Relevant to central-carbon flux in *Pseudomonas*, framing MQO's position at the oxaloacetate node. |

Two additional lines of evidence were generated computationally in this investigation and are not from the literature list: (1) pairwise sequence alignments establishing *mqo2* as the *E. coli*-closest paralog (F005), and (2) hydropathy/motif analysis establishing the FAD Rossmann fold and absence of a transmembrane helix (F007). KEGG orthology and pathway mapping (F006) provide independent database-level corroboration.

---

## Supported and Refuted Hypotheses

**Supported**
- *mqo2* encodes an FAD-dependent malate:quinone oxidoreductase (EC 1.1.5.4) — supported by UniProt/HAMAP rule, family/domain assignment, sequence motif, and orthologous biochemistry ([PMID: 9660197](https://pubmed.ncbi.nlm.nih.gov/9660197/); [PMID: 11092847](https://pubmed.ncbi.nlm.nih.gov/11092847/)).
- Substrate = L-malate; electron acceptor = quinone (not NAD⁺); product = oxaloacetate.
- Peripheral inner-membrane, cytoplasm-facing localization (experimental in orthologs; structural inference here).
- Functions in the TCA cycle at the oxaloacetate-regenerating step, coupled to aerobic respiration and redox-regulated; independently confirmed by KEGG (K00116, EC 1.1.5.4).
- Among the three *P. putida* paralogs, *mqo2* is the closest homolog (70.2%) of the experimentally characterized *E. coli* MQO — bioinformatic support that *mqo2* carries the canonical activity.

**Refuted / ruled out**
- MQO is **not** an NAD-dependent enzyme and is **not** interchangeable in cofactor use with cytoplasmic MDH.
- The gene symbol is **not** ambiguous here: organism, locus (PP_1251), family, and domains all match; no conflicting literature for an unrelated "mqo2" was found.

---

## Limitations and Knowledge Gaps

1. **No direct biochemical characterization of the *P. putida* enzyme.** The reaction, cofactor, acceptor, and localization for MQO 2 are inferred from orthologs (*E. coli*, *C. glutamicum*) and from conserved sequence/structure. The *P. putida* protein itself has not been purified, kinetically characterized, or crystallized. Its exact quinone preference (ubiquinone-8 vs. demethylmenaquinone), *k*cat/*K*m for malate, and lipid-activation behavior remain unmeasured. Annotation of Q88NF9 is rule-based ("Probable").

2. **Paralog functional differentiation is unresolved.** With three MQO paralogs (mqo1/2/3), it is unknown whether they are redundant, condition-specific, or subtly specialized. No expression, deletion, or complementation data distinguishing PP_0751, PP_1251, and PP_2925 were established. The assignment of *mqo2* as the "canonical" copy is based on homology ranking, not physiology.

3. **Regulation in *P. putida* is inferred, not measured.** ArcA–ArcB regulation is documented for *E. coli*; whether *mqo2* is similarly redox-regulated in *P. putida* is not established. Its location among group-II-intron maturases and an ArsR-family regulator suggests possibly distinct regulation that has not been experimentally tested.

4. **Localization topology is inferred.** The "cytoplasmic face, peripheral" model is drawn from ortholog behavior and hydropathy analysis; it has not been experimentally verified for MQO 2 (e.g., by fractionation or protease-protection assays). No experimentally solved MQO crystal structure was found in the searched literature.

5. **EC-number provenance.** The EC 1.1.5.4 / K00116 assignment derives from automated rules (HAMAP MF_00212) and KEGG orthology. These are high-confidence for this well-conserved family but are annotation-transfer rather than direct assay.

---

## Proposed Follow-up Experiments / Actions

1. **Purify and assay MQO 2.** Heterologously express PP_1251, purify the flavoprotein, and measure malate:quinone oxidoreductase activity with defined quinone analogs (e.g., ubiquinone-1/decylubiquinone). Determine *K*m for (S)-malate, quinone specificity, FAD stoichiometry, and lipid activation — directly testing F001.

2. **Confirm cofactor and acceptor.** Spectroscopically confirm non-covalent FAD binding and test NAD⁺ as a (non-)acceptor, replicating the *C. glutamicum* result for the *P. putida* enzyme.

3. **Test membrane association.** Perform cell fractionation and chelator/high-salt/carbonate extraction to verify peripheral (vs. integral) membrane localization and the cytoplasmic-face topology predicted in F002/F007.

4. **Dissect paralog roles.** Construct single and combinatorial deletions of *mqo1*, *mqo2*, *mqo3* and assay growth on malate/succinate/glucose/aromatics; complement with individual paralogs to establish redundancy vs. specialization (addresses F004/F005). Pair with RT-qPCR/RNA-seq across O₂/redox conditions.

5. **Probe regulation.** Use reporter fusions or RNA-seq across oxygen tensions and carbon sources to determine whether *mqo2* is redox/O₂-regulated in *P. putida*, and whether the neighboring ArsR-family regulator (PP_1253) or the mobile-element context influences its expression (addresses F006).

6. **Structural determination.** Solve the crystal or cryo-EM structure of MQO 2 with bound FAD and substrate/quinone analog to confirm the Rossmann fold, the membrane-interaction surface, and the quinone-binding site predicted from F007 — enabling inhibitor design (MQO is an antimicrobial target in pathogens such as *M. tuberculosis* and *H. pylori* that lack NAD-MDH).

7. **Flux analysis.** Use ¹³C metabolic flux analysis in wild-type vs. *mqo* mutants to quantify MQO 2's contribution to the malate → OAA node and its role in partitioning carbon toward biosynthesis vs. energy metabolism (extends F003).

---

## Conclusion

*mqo2* (Q88NF9, PP_1251) encodes **Malate:quinone oxidoreductase 2**, an FAD-dependent peripheral inner-membrane flavoenzyme that catalyzes the quinone-linked oxidation of (S)-malate to oxaloacetate (EC 1.1.5.4). It performs the oxaloacetate-regenerating step of the TCA cycle while feeding electrons directly into the respiratory quinone pool, thereby coupling central carbon metabolism to aerobic respiration and proton-motive-force generation. Of the three MQO paralogs in *P. putida* KT2440, *mqo2* is the closest homolog of the biochemically characterized *E. coli* enzyme, and its function is inferred with high confidence from conserved catalytic architecture and ortholog enzymology, pending direct biochemical validation of the *P. putida* protein.

---

## References

1. Molenaar D, van der Rest ME, Petrović S. *Biochemical and genetic characterization of the membrane-associated malate dehydrogenase (acceptor) from Corynebacterium glutamicum.* Eur J Biochem. 1998. [PMID: 9660197](https://pubmed.ncbi.nlm.nih.gov/9660197/)
2. van der Rest ME, Frank C, Molenaar D. *Functions of the membrane-associated and cytoplasmic malate dehydrogenases in the citric acid cycle of Escherichia coli.* J Bacteriol. 2000. [PMID: 11092847](https://pubmed.ncbi.nlm.nih.gov/11092847/)
3. Mitsuhashi S, Hayashi M, Ohnishi J, Ikeda M. *Disruption of malate:quinone oxidoreductase increases L-lysine production by Corynebacterium glutamicum.* Biosci Biotechnol Biochem. 2006. [PMID: 17090916](https://pubmed.ncbi.nlm.nih.gov/17090916/)
4. *Mitochondrial Membrane-Associated L-2-Hydroxyglutarate Dehydrogenase Catalyzes Electron Transport to Ubiquinone In Vitro.* [PMID: 42203459](https://pubmed.ncbi.nlm.nih.gov/42203459/)
5. *Siccanin rediscovered as a species-selective succinate dehydrogenase inhibitor.* 2009. [PMID: 19505951](https://pubmed.ncbi.nlm.nih.gov/19505951/)
6. *Cryo-EM of native membranes reveals an intimate connection between the Krebs cycle and aerobic respiration in mycobacteria.* [PMID: 39969994](https://pubmed.ncbi.nlm.nih.gov/39969994/)

*Database evidence:* UniProt Q88NF9 (verified via REST API); KEGG ppu:PP_1251 (K00116, EC 1.1.5.4); InterPro IPR006231/IPR036188; Pfam PF06039; HAMAP MF_00212. *Comparative analysis (this work):* Needleman–Wunsch pairwise identities of the three *P. putida* MQO paralogs against *E. coli* MQO (P33940); Kyte–Doolittle hydropathy and Rossmann-motif analysis of Q88NF9.


## Artifacts

- [OpenScientist final report](mqo2-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](mqo2-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:9660197
2. PMID:11092847
3. PMID:17090916
4. PMID:42203459
5. PMID:19505951
6. PMID:39969994