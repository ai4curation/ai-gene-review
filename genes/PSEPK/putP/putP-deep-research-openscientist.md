---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T20:20:02.139195'
end_time: '2026-08-31T20:50:15.007926'
duration_seconds: 1812.87
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: putP
  gene_symbol: putP
  uniprot_accession: Q88D81
  protein_description: 'RecName: Full=Sodium/proline symporter {ECO:0000256|ARBA:ARBA00067214,
    ECO:0000256|RuleBase:RU366012}; AltName: Full=Proline permease {ECO:0000256|ARBA:ARBA00082709,
    ECO:0000256|RuleBase:RU366012};'
  gene_info: Name=putP {ECO:0000313|EMBL:AAN70513.2}; OrderedLocusNames=PP_4946 {ECO:0000313|EMBL:AAN70513.2};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the sodium:solute symporter (SSF) (TC 2.A.21)
  protein_domains: Na/Glc_symporter_sf. (IPR038377); Na/Pro_symporter. (IPR011851);
    Na/solute_symporter. (IPR001734); Na/solute_symporter_CS. (IPR018212); Sodium:Solute_Symporter.
    (IPR050277)
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
citation_count: 15
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: putP-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: putP-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88D81
- **Protein Description:** RecName: Full=Sodium/proline symporter {ECO:0000256|ARBA:ARBA00067214, ECO:0000256|RuleBase:RU366012}; AltName: Full=Proline permease {ECO:0000256|ARBA:ARBA00082709, ECO:0000256|RuleBase:RU366012};
- **Gene Information:** Name=putP {ECO:0000313|EMBL:AAN70513.2}; OrderedLocusNames=PP_4946 {ECO:0000313|EMBL:AAN70513.2};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the sodium:solute symporter (SSF) (TC 2.A.21)
- **Key Domains:** Na/Glc_symporter_sf. (IPR038377); Na/Pro_symporter. (IPR011851); Na/solute_symporter. (IPR001734); Na/solute_symporter_CS. (IPR018212); Sodium:Solute_Symporter. (IPR050277)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "putP" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'putP' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **putP** (gene ID: putP, UniProt: Q88D81) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# PutP (PP_4946, UniProt Q88D81) of *Pseudomonas putida* KT2440: A Sodium/Proline Symporter — Functional Annotation Report

## Summary

**PutP (PP_4946; UniProt Q88D81) of *Pseudomonas putida* KT2440 is an integral inner-membrane sodium/proline symporter that catalyzes the electrogenic, Na⁺-coupled uptake of extracellular L-proline into the cytoplasm.** It belongs to the solute:sodium symporter family (SSS/SSF; Transporter Classification TC 2.A.21; human SLC5 superfamily), and it harnesses the transmembrane electrochemical Na⁺ gradient as the thermodynamic driving force to accumulate proline against a concentration gradient. Its primary, dedicated biological role is to serve as the **import step of the proline-utilization (*put*) pathway**, delivering proline to the cytoplasmic bifunctional enzyme PutA, which oxidizes it to glutamate and thereby enables *P. putida* to grow on proline as a sole source of both carbon and nitrogen.

The functional assignment rests on multiple converging lines of evidence. Direct experimental work in the exact target strain (*P. putida* KT2440) demonstrated that proline uptake is mediated by PutP and that the organism uses proline as sole C and N source, with *putP* and *putA* transcribed divergently from a proline-inducible intergenic region ([PMID: 11097893](https://pubmed.ncbi.nlm.nih.gov/11097893/)). The genomic architecture in KT2440 — with PP_4946 (*putP*) immediately adjacent to PP_4947 (*putA*, the bifunctional proline dehydrogenase/Δ¹-pyrroline-5-carboxylate dehydrogenase) — confirms an intact, co-regulated proline-utilization module. The mechanistic details of transport, though not solved directly for the *P. putida* protein, are transferable at high confidence from the intensively studied *Escherichia coli* ortholog (~80% identical), a canonical model of the SSS family whose LeuT-like 5+5 inverted-repeat fold, Na⁺-coordination chemistry, and gating residues have been mapped by decades of biochemistry.

Critically, a residue-level comparison performed in this investigation showed that **every experimentally characterized functional residue of *E. coli* PutP — the Na⁺-coordinating aspartate, the substrate-pathway serines/glycines, the external-gate glutamate, and the TM IX threonine/serine ion-binding cluster — is 100% conserved in the *P. putida* protein.** This near-perfect conservation of the ion/substrate machinery, combined with direct transport evidence in KT2440 and the preserved *putP–putA* genomic pairing, provides high-confidence, self-consistent support for annotating PP_4946 as a Na⁺-coupled L-proline symporter operating at the cytoplasmic (inner) membrane. A secondary, family-associated role in osmoadaptation — supplying proline as an osmoprotective compatible solute — is plausible but not directly demonstrated for this ortholog.

---

## Gene/Protein Identity Verification

Before presenting findings, the mandatory identity checks were completed and **all passed**. This is not a case of gene-symbol ambiguity — the retrieved literature is specifically about *putP*/PutP sodium-proline transporters, and includes a direct study in the exact target strain.

| Verification item | Expected (from UniProt Q88D81) | Confirmed |
|---|---|---|
| Gene symbol | *putP* | ✅ PP_4946 annotated as *putP* |
| Ordered locus | PP_4946 | ✅ |
| Protein | Sodium/proline symporter (proline permease) | ✅ Matches literature and family assignment |
| Organism | *P. putida* KT2440 (ATCC 47054 / DSM 6125 / KT2440) | ✅ Direct experimental study exists in this strain (Vílchez et al. 2000) |
| Length / MW | 542 aa / ~57.9 kDa | ✅ |
| Family / domains | SSS family (TC 2.A.21 / SLC5); Na/solute symporter domains | ✅ LeuT-like 5+5 fold; 12–13 TMs |
| Subcellular location | Cell inner membrane | ✅ |

---

## Key Findings

### Finding 1 — PutP is a Na⁺-coupled L-proline symporter (primary function verified)

The primary function of PP_4946 is the sodium-dependent uptake of extracellular L-proline. UniProt Q88D81 annotates the 542-residue (~57.9 kDa) protein as PutP / OrderedLocusName PP_4946 with the function "catalyzes the sodium-dependent uptake of extracellular L-proline," and places it in the solute/sodium symporter family (SSS/SSF; TC 2.A.21; SLC5).

This is not merely a database inference. In the exact target organism, *P. putida* KT2440, direct experimental work established that **proline uptake is mediated by the PutP protein**: *"Utilization of this amino acid involves its uptake, which is mediated by the PutP protein, and its conversion into glutamate, mediated by the PutA protein"* ([PMID: 11097893](https://pubmed.ncbi.nlm.nih.gov/11097893/)). At the family level, the *H. pylori* PutP ortholog was reconstituted into proteoliposomes and shown to be **obligately Na⁺-coupled** — *"L-proline transport is exclusively dependent on Na(+) as coupling ion, i.e., Na(+)/L-proline symport"* ([PMID: 24358297](https://pubmed.ncbi.nlm.nih.gov/24358297/)). A dedicated review formally assigns PutP: *"The Na⁺/L-proline transporter PutP is a member of the Na⁺/solute symporter family (TC 2A.21, SLC5)"* ([PMID: 22201772](https://pubmed.ncbi.nlm.nih.gov/22201772/)).

The transport reaction can be written:

> **L-proline(out) + Na⁺(out) → L-proline(in) + Na⁺(in)**

**Substrate specificity:** the physiological substrate is L-proline, co-transported with Na⁺ (Li⁺ can substitute for Na⁺ in some orthologs but with lower affinity). The transport is **electrogenic** — charge is displaced during both Na⁺ and proline binding, as demonstrated by solid-supported-membrane electrophysiology on the *E. coli* carrier ([PMID: 15476811](https://pubmed.ncbi.nlm.nih.gov/15476811/); [PMID: 19366604](https://pubmed.ncbi.nlm.nih.gov/19366604/)).

### Finding 2 — PutP is an inner-membrane transporter with a LeuT-like 5+5 inverted-repeat fold; mechanism transferable from *E. coli* (80% identity)

PutP is an integral protein of the **cell inner (cytoplasmic) membrane**, where it carries out transport. UniProt annotates 12 transmembrane helices and an inner-membrane location; detailed topology work on the *E. coli* ortholog established a **13-helix motif** with the N-terminus in the periplasm and the C-terminus in the cytoplasm, subsequently refined to a **LeuT-like core of 5+5 inverted-repeat transmembrane domains** ([PMID: 9756872](https://pubmed.ncbi.nlm.nih.gov/9756872/); [PMID: 22201772](https://pubmed.ncbi.nlm.nih.gov/22201772/)).

The *P. putida* protein is highly similar to characterized orthologs, licensing mechanistic transfer. A global Needleman–Wunsch alignment computed in this investigation gave **80.3% identity** (391/487 aligned residues) between Q88D81 and *E. coli* PutP (P07117). This is independently corroborated by the observation that *P. aeruginosa* PutP is *"80% identity to the P. putida counterpart"* ([PMID: 12270821](https://pubmed.ncbi.nlm.nih.gov/12270821/)). The review literature defines the fold: *"PutP has a core structure of five plus five transmembrane domains forming an inverted repeat similar as originally revealed by the crystal structure of the Na+/leucine transporter LeuT"* ([PMID: 22201772](https://pubmed.ncbi.nlm.nih.gov/22201772/)). Within this core, **Asp55 (TM II) is essential for transport and directly coordinates Na⁺**: *"Asp55 (putative TM II) is essential for transport and proposed to interact directly with Na+"* ([PMID: 9693722](https://pubmed.ncbi.nlm.nih.gov/9693722/)).

### Finding 3 — PutP is the uptake step of the proline-utilization (*put*) pathway, feeding proline catabolism to glutamate

PutP operates at the head of a two-component catabolic module. It imports L-proline; the downstream **bifunctional flavoenzyme PutA** then oxidizes proline → Δ¹-pyrroline-5-carboxylate (P5C) → glutamate via its proline dehydrogenase and P5C dehydrogenase activities: *"Proline utilization A (PutA) is a membrane-associated multifunctional enzyme that catalyzes the oxidation of proline to glutamate in a two-step process"* ([PMID: 18767154](https://pubmed.ncbi.nlm.nih.gov/18767154/)). This enables *P. putida* KT2440 to use **proline as sole carbon and nitrogen source**: *"Pseudomonas putida KT2440 uses proline as the sole C and N source"* ([PMID: 11097893](https://pubmed.ncbi.nlm.nih.gov/11097893/)).

The pathway is autoregulated. In *P. putida*, PutA moonlights as an **autogenous transcriptional repressor** of the *put* genes: *"The PutA protein acts as a repressor of put gene expression in P. putida because expression from the put promoters is constitutive in a host background with a knockout putA gene"* ([PMID: 11097893](https://pubmed.ncbi.nlm.nih.gov/11097893/)). The DNA-binding function is mediated by an N-terminal ribbon-helix-helix domain (PpPutA45) that binds the *put* operator ([PMID: 18767154](https://pubmed.ncbi.nlm.nih.gov/18767154/)). A secondary, family-associated role in osmoadaptation is proposed: *"the transporter may supply cells with compatible solute during adaptation to osmotic stress"* ([PMID: 22201772](https://pubmed.ncbi.nlm.nih.gov/22201772/)). (In the related *P. aeruginosa*, the *putAP* genes form an operon regulated by the AraC/XylS-family activator PruR — [PMID: 12270821](https://pubmed.ncbi.nlm.nih.gov/12270821/) — illustrating divergence in regulatory architecture among pseudomonads.)

### Finding 4 — All experimentally-defined ion/substrate/gating residues of *E. coli* PutP are 100% conserved in *P. putida* PutP

A pairwise global alignment (Q88D81 vs *E. coli* P07117) performed in this investigation mapped **every experimentally characterized functional residue** of *E. coli* PutP onto an identical residue in the *P. putida* protein. Conservation is 100% for the residues below (a ~+48 positional offset reflects a ~40-residue N-terminal extension in the *P. putida* protein; 542 vs 502 aa). This elevates the mechanistic annotation from family-level inference to residue-level support.

| *E. coli* PutP residue | Location / role | *P. putida* PutP equivalent | Conserved? |
|---|---|---|---|
| Tyr14 | TM I; Na⁺-coupled cotransport | Tyr62 | ✅ |
| Ser54 | TM II; proline pathway | Ser102 | ✅ |
| **Asp55** | TM II; **essential, direct Na⁺ coordination** | Asp103 | ✅ |
| Met56 | TM II; near ion site | Met104 | ✅ |
| Ser57 | TM II; cation/substrate affinity | Ser105 | ✅ |
| Gly58 | TM II; proline pathway | Gly106 | ✅ |
| **Glu311** | External loop 4; **external gate closure** | Glu359 | ✅ |
| Ser332 | TM IX; ligand binding | Ser380 | ✅ |
| Ser340 | TM IX; translocation pathway | Ser388 | ✅ |
| **Thr341** | TM IX; **direct Na⁺ binding** | Thr389 | ✅ |
| Gln345 | TM IX; Na⁺/proline affinity | Gln393 | ✅ |
| Leu346 | TM IX; proline affinity/Vmax | Leu394 | ✅ |

Supporting citations: Asp55 is essential and directly interacts with Na⁺ ([PMID: 9693722](https://pubmed.ncbi.nlm.nih.gov/9693722/)); Thr341 directly participates in Na⁺ binding — *"it is proposed that the side chain of Thr-341 directly participates in Na+ binding"* ([PMID: 18156179](https://pubmed.ncbi.nlm.nih.gov/18156179/)); Glu311 is the external-gate residue — *"Glu-311 at the tip of eL4, and various amino acids around the outer end of TM10' are identified as particularly crucial for function"* ([PMID: 26728461](https://pubmed.ncbi.nlm.nih.gov/26728461/)); Ser54/Ser57/Gly58 line the proline pathway ([PMID: 11756453](https://pubmed.ncbi.nlm.nih.gov/11756453/)); S332/Q345/L346 in TM IX are important for uptake ([PMID: 18692508](https://pubmed.ncbi.nlm.nih.gov/18692508/)); the conserved Tyr14→Tyr62 in TM I is specifically implicated in Na⁺-coupled substrate co-transport ([PMID: 21705334](https://pubmed.ncbi.nlm.nih.gov/21705334/)). This conservation is the strongest single piece of evidence that the *P. putida* protein uses the identical transport chemistry as the biochemically dissected *E. coli* carrier.

### Finding 5 — Genomic context confirms the divergent *putP–putA* pair (PP_4946/PP_4947)

Genome/UniProt lookup shows that PP_4946 = *putP* (Q88D81, Na⁺/proline symporter) is immediately adjacent to **PP_4947 = *putA*** (Q88D80, "Bifunctional protein PutA," proline dehydrogenase + Δ¹-pyrroline-5-carboxylate dehydrogenase). The other flanking locus, PP_4945 (Q88D82), is an unrelated rRNA large-subunit methyltransferase and is not part of the module. This adjacency matches the experimentally characterized divergently-transcribed, proline-inducible arrangement in KT2440: *"Sequence analysis revealed that the putA and putP genes are transcribed divergently"* ([PMID: 11097893](https://pubmed.ncbi.nlm.nih.gov/11097893/)). The genomic pairing independently corroborates the functional assignment — PutP is co-located and co-regulated with the enzyme that consumes its transported product.

---

## Mechanistic Model / Interpretation

The findings assemble into a coherent, self-consistent model of PutP function in *P. putida* KT2440:

```
      EXTRACELLULAR / PERIPLASM              (high Na+, extracellular L-proline)
   ─────────────────────────────────────────────────────────────────────────
        L-proline  +  Na+
             │            │
             ▼            ▼          ┌──────────────────────────────────────┐
   ══════════════════════════════════│  PutP  (PP_4946, Q88D81, 542 aa)      │
   INNER (CYTOPLASMIC) MEMBRANE       │  SSS family, TC 2.A.21 / SLC5         │
                                      │  LeuT-like 5+5 inverted-repeat fold   │
                                      │  Na+ site: Asp103, Thr389 (100% cons.)│
   ══════════════════════════════════│  Gate: Glu359; pathway: Ser102/105... │
             │            │           └──────────────────────────────────────┘
             ▼            ▼            (alternating-access, electrogenic symport)
        L-proline  +  Na+
      CYTOPLASM
             │
             ▼
        ┌─────────────────────────────────────────────┐
        │  PutA  (PP_4947, Q88D80, bifunctional)        │
        │  proline → P5C (proline dehydrogenase, FAD)   │
        │  P5C → glutamate (P5C dehydrogenase)          │
        └─────────────────────────────────────────────┘
             │
             ▼
        L-GLUTAMATE  →  central carbon & nitrogen metabolism
                        (growth on proline as sole C + N source)

   Regulation: PutA is a bifunctional trigger enzyme — it also acts as an
   autogenous repressor of the divergent putP/putA promoters (via its
   N-terminal ribbon-helix-helix / PpPutA45 domain). Proline induction
   relieves repression.
```

**Transport mechanism.** PutP is a secondary active transporter that couples the downhill movement of Na⁺ (driven by the membrane electrochemical Na⁺ gradient) to the uphill accumulation of L-proline — a **symport** mechanism. Structurally it adopts the LeuT-like 5+5 inverted-repeat fold shared across the SSS family, which operates by **alternating access**: the substrate/ion binding site is alternately exposed to the periplasmic and cytoplasmic sides through coordinated movement of the two inverted-repeat halves and opening/closing of external and internal gates. The conserved residue set defines the machine: **Asp103** (≡ *E. coli* Asp55) and **Thr389** (≡ Thr341) form the Na⁺ coordination chemistry; **Ser102/Ser105/Gly106** and TM IX residues line the proline translocation pathway; **Glu359** (≡ Glu311) at external loop 4 controls external-gate closure; and **Tyr62** (≡ Tyr14) in TM I participates in the Na⁺-coupled co-transport network. Electrophysiological studies of the *E. coli* carrier show that both Na⁺ and the neutral proline substrate generate charge displacements on binding, that either substrate can bind individually but an ordered mechanism dominates under physiological conditions, and that the two binding sites cooperate ([PMID: 15476811](https://pubmed.ncbi.nlm.nih.gov/15476811/)).

**Physiological role.** The transporter is the committed **uptake step of proline catabolism**. Imported proline is handed to PutA, a membrane-associated bifunctional flavoenzyme that converts it to glutamate in two oxidation steps, funneling proline-derived carbon and nitrogen into central metabolism. Because *putP* and *putA* are divergently transcribed from a shared, proline-inducible intergenic region and PutA autoregulates the operon, PutP expression is tightly coupled to substrate availability — the transporter is made when proline is present and catabolism is warranted. A **secondary osmoadaptive role** — importing proline as a compatible solute during osmotic stress — is a recognized function of SSS-family proline transporters and is proposed for PutP, though in many organisms this is handled by dedicated osmoregulated transporters (e.g., OpuE in *Bacillus subtilis*, [PMID: 11902719](https://pubmed.ncbi.nlm.nih.gov/11902719/)) rather than the catabolic PutP.

**Localization.** PutP carries out its function embedded in the **inner (cytoplasmic) membrane**, with its transport pathway spanning the lipid bilayer; the N-terminus faces the periplasm and the C-terminus the cytoplasm. Its catalytic "output" (delivery of proline to the cytoplasmic face) is spatially matched to the location of PutA at/near the inner membrane.

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution to this report |
|---|---|---|
| [11097893](https://pubmed.ncbi.nlm.nih.gov/11097893/) | Control of divergent *P. putida* *put* promoters | **Direct evidence in the target strain**: PutP mediates proline uptake; KT2440 uses proline as sole C+N; *putP*/*putA* divergently transcribed; PutA is autogenous repressor |
| [22201772](https://pubmed.ncbi.nlm.nih.gov/22201772/) | *The Na⁺/L-proline transporter PutP* (review) | Family assignment (SSS, TC 2.A.21, SLC5); LeuT-like 5+5 fold; osmoadaptive role |
| [24358297](https://pubmed.ncbi.nlm.nih.gov/24358297/) | PutP of *Helicobacter pylori* | Proteoliposome proof of obligatory Na⁺-coupled proline symport |
| [12270821](https://pubmed.ncbi.nlm.nih.gov/12270821/) | *P. aeruginosa* *putAP* operon / PruR | Independent confirmation of ~80% PutP identity between *Pseudomonas* species; divergent regulation |
| [9693722](https://pubmed.ncbi.nlm.nih.gov/9693722/) | Topology/function of *E. coli* PutP | Asp55 essential and directly coordinates Na⁺ (conserved as Asp103); 13-TM topology |
| [18156179](https://pubmed.ncbi.nlm.nih.gov/18156179/) | Ser-340/Thr-341 in TM IX | Thr341 directly participates in Na⁺ binding (conserved as Thr389) |
| [26728461](https://pubmed.ncbi.nlm.nih.gov/26728461/) | Glu-311 in external loop 4 | Glu311 crucial for external-gate closure (conserved as Glu359) |
| [21705334](https://pubmed.ncbi.nlm.nih.gov/21705334/) | Conserved Tyr in TM1 of SSSs | Tyr14 (conserved as Tyr62) involved in Na⁺-coupled co-transport |
| [11756453](https://pubmed.ncbi.nlm.nih.gov/11756453/) | Na⁺/substrate binding sites, TM II | Roles of Ser54, Asp55, Met56, Ser57, Gly58 (all conserved) |
| [18692508](https://pubmed.ncbi.nlm.nih.gov/18692508/) | Function of TM IX | S332, Q345, L346 important for Na⁺-coupled proline uptake |
| [15476811](https://pubmed.ncbi.nlm.nih.gov/15476811/) | Charge translocation in *E. coli* PutP | Electrogenic, ordered, cooperative Na⁺/proline binding mechanism |
| [19366604](https://pubmed.ncbi.nlm.nih.gov/19366604/) | Bacterial transporters: charge translocation | Places PutP mechanism among electrogenic secondary transporters |
| [11248195](https://pubmed.ncbi.nlm.nih.gov/11248195/) | Molecular mechanism of Na⁺/solute symport | 13-helix motif; TM II critical for Na⁺/proline binding |
| [9756872](https://pubmed.ncbi.nlm.nih.gov/9756872/) | Topology of *E. coli* PutP | Establishes 13-TM topology, periplasmic N-terminus / cytoplasmic C-terminus |
| [18767154](https://pubmed.ncbi.nlm.nih.gov/18767154/) | Structure of *P. putida* PpPutA45–DNA | Downstream PutA oxidizes proline→glutamate; DNA-binding regulatory domain |
| [9753469](https://pubmed.ncbi.nlm.nih.gov/9753469/) | Asp187 in *E. coli* PutP | Additional conserved acidic residue near the Na⁺ pathway |
| [11902719](https://pubmed.ncbi.nlm.nih.gov/11902719/) | OpuE of *B. subtilis* | Contrast: SSS-family proline transporter dedicated to osmoprotection |
| [33668649](https://pubmed.ncbi.nlm.nih.gov/33668649/) | SSS family review | Broad family context; PutP role in bacteria–host interactions |

**How the evidence fits together:** the annotation is anchored by a *direct* study in the target strain ([PMID: 11097893](https://pubmed.ncbi.nlm.nih.gov/11097893/)), reinforced by an *obligatory-Na⁺-coupling* proteoliposome study on a family ortholog ([PMID: 24358297](https://pubmed.ncbi.nlm.nih.gov/24358297/)), and made mechanistically precise by the transfer of *E. coli* PutP biochemistry through 100% conservation of all characterized functional residues. No retrieved paper contradicts the assignment; the only nuance is the distinction between catabolic PutP and osmoregulated OpuE-type transporters, which clarifies (rather than challenges) PutP's primary catabolic role.

---

## Supported vs. Refuted Hypotheses

| Hypothesis | Verdict |
|---|---|
| PutP is a Na⁺-coupled L-proline symporter | **Supported** (UniProt + KT2440 study + orthologs) |
| PutP localizes to the inner (cytoplasmic) membrane | **Supported** |
| PutP is the uptake step feeding PutA-mediated proline→glutamate catabolism | **Supported** |
| PutP can also supply proline as an osmoprotective compatible solute | **Supported as a secondary role** (proposed for the family; not directly tested for this ortholog) |
| Gene symbol is ambiguous / wrong gene | **Refuted** — identity is unambiguous and strain-specific literature exists |

---

## Limitations and Knowledge Gaps

1. **No direct biochemistry on the *P. putida* protein.** Transport kinetics (Kₘ for proline, K₀.₅ for Na⁺, Vmax, Na⁺:proline stoichiometry) have not been measured for Q88D81 specifically. All quantitative mechanistic parameters are inferred from *E. coli*/*H. pylori* orthologs. The inference is strong (80% identity; 100% functional-residue conservation) but remains an inference.

2. **No experimental structure.** There is no crystal or cryo-EM structure of *P. putida* PutP; the LeuT-like 5+5 fold and residue roles are transferred from homology/topology models and the *E. coli* mutagenesis literature.

3. **N-terminal extension not characterized.** The *P. putida* protein is ~40 residues longer than *E. coli* PutP (542 vs 502 aa). The function/topology of this N-terminal extension is unknown and could add regulatory or localization features.

4. **Osmoadaptive role unproven for this ortholog.** The compatible-solute/osmoprotection role is a family-level proposal ([PMID: 22201772](https://pubmed.ncbi.nlm.nih.gov/22201772/)); whether *P. putida* PutP contributes to osmotolerance has not been tested. In several bacteria this role is served by a separate transporter (OpuE-type).

5. **Regulatory details specific to KT2440.** While PutA autorepression and divergent transcription are established, the identity of the σ⁵⁴-dependent positive regulator of the *P. putida put* system remains unresolved (noted as still unidentified in the primary study).

6. **Substrate range not exhaustively mapped.** L-proline is the established substrate; whether the *P. putida* carrier accepts proline analogs (e.g., 3,4-dehydroproline, L-azetidine-2-carboxylate — competitive substrates in orthologs) or uses Li⁺ as an alternative coupling ion has not been directly tested here.

---

## Proposed Follow-up Experiments / Actions

1. **Direct transport assay in a defined background.** Express *P. putida* PP_4946 in an *E. coli putP⁻* strain and measure Na⁺-dependent [¹⁴C]-proline uptake to obtain Kₘ(proline), K₀.₅(Na⁺), and confirm obligatory Na⁺ coupling for this specific ortholog.

2. **Proteoliposome reconstitution.** Purify Q88D81 and reconstitute into proteoliposomes (as done for *H. pylori* PutP, [PMID: 24358297](https://pubmed.ncbi.nlm.nih.gov/24358297/)) to determine Na⁺:proline stoichiometry and test Li⁺ substitution and electrogenicity via SSM electrophysiology.

3. **Targeted mutagenesis validation.** Mutate the predicted Na⁺-site (Asp103, Thr389) and gate (Glu359) residues to confirm that the conserved positions perform the same roles as their *E. coli* counterparts; loss of transport would validate the homology-based mechanistic transfer.

4. **Structural prediction analysis.** Retrieve and analyze the AlphaFold model for Q88D81 (pLDDT, PAE), superpose onto vSGLT/LeuT and *E. coli* PutP models, structurally place the conserved functional residues, and characterize the N-terminal extension.

5. **Genetic phenotyping in KT2440.** Construct a clean PP_4946 deletion and test (a) growth on proline as sole C/N source, (b) proline uptake rate, and (c) osmotolerance with proline as sole osmoprotectant — to directly quantify PutP's catabolic vs osmoadaptive contributions in the native host.

6. **Regulation mapping.** Use RT-qPCR/reporter fusions to map proline-inducibility of the PP_4946/PP_4947 divergent promoters in KT2440, test PutA-dependent autorepression, and identify the σ⁵⁴-dependent activator.

---

## Conclusion

**PutP (PP_4946, UniProt Q88D81) of *Pseudomonas putida* KT2440 is an integral inner-membrane sodium/proline symporter of the solute:sodium symporter family (TC 2.A.21 / SLC5) that catalyzes electrogenic, Na⁺-coupled uptake of extracellular L-proline into the cytoplasm.** It functions as the dedicated import step of the proline-utilization (*put*) regulon — physically paired with and divergently transcribed from *putA* (PP_4947), whose bifunctional enzyme oxidizes the imported proline to glutamate — enabling growth on proline as sole carbon and nitrogen source, with a probable secondary role supplying proline as an osmoprotective compatible solute. The assignment is supported by direct transport evidence in KT2440, obligate Na⁺-coupling in family orthologs, the preserved *putP–putA* genomic architecture, and 100% conservation of all experimentally-defined ion, substrate, and gating residues from the ~80%-identical, intensively studied *E. coli* ortholog.

---

*Report generated for UniProt Q88D81 / putP / PP_4946, Pseudomonas putida KT2440.*


## Artifacts

- [OpenScientist final report](putP-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](putP-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:11097893
2. PMID:24358297
3. PMID:22201772
4. PMID:15476811
5. PMID:19366604
6. PMID:9756872
7. PMID:12270821
8. PMID:9693722
9. PMID:18767154
10. PMID:18156179
11. PMID:26728461
12. PMID:11756453
13. PMID:18692508
14. PMID:21705334
15. PMID:11902719