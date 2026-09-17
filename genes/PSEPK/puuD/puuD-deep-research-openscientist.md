---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-19T07:57:16.385646'
end_time: '2026-08-19T08:29:46.383882'
duration_seconds: 1950.0
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: puuD
  gene_symbol: puuD
  uniprot_accession: Q88IA0
  protein_description: 'SubName: Full=Uricase/urate oxidase {ECO:0000313|EMBL:AAN68707.1};
    EC=1.7.3.3 {ECO:0000313|EMBL:AAN68707.1};'
  gene_info: Name=puuD {ECO:0000313|EMBL:AAN68707.1}; OrderedLocusNames=PP_3099 {ECO:0000313|EMBL:AAN68707.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: T6SS_TssC-like. (IPR010269); TssC1_C. (IPR044032); TssC1_N. (IPR044031);
    VipB (PF05943); VipB_2 (PF18945)
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
  path: puuD-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: puuD-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88IA0
- **Protein Description:** SubName: Full=Uricase/urate oxidase {ECO:0000313|EMBL:AAN68707.1}; EC=1.7.3.3 {ECO:0000313|EMBL:AAN68707.1};
- **Gene Information:** Name=puuD {ECO:0000313|EMBL:AAN68707.1}; OrderedLocusNames=PP_3099 {ECO:0000313|EMBL:AAN68707.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** T6SS_TssC-like. (IPR010269); TssC1_C. (IPR044032); TssC1_N. (IPR044031); VipB (PF05943); VipB_2 (PF18945)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "puuD" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'puuD' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **puuD** (gene ID: puuD, UniProt: Q88IA0) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: puuD / PP_3099 (UniProt Q88IA0) in *Pseudomonas putida* KT2440

## Summary

The gene annotated as **puuD** (locus **PP_3099**, UniProt **Q88IA0**) in *Pseudomonas putida* strain KT2440 is **not** a uricase/urate oxidase, despite the legacy UniProt SubName "Uricase/urate oxidase; EC=1.7.3.3." That enzymatic label is a **pre-2017 automatic-annotation artifact** (ECO:0000313, derived solely from the original EMBL genome-submission record AAN68707.1) and is contradicted by every independent line of structural, evolutionary, and genomic-context evidence gathered in this investigation. The protein is, in fact, **TssC1 (also called VipB)** — the large subunit of the **contractile sheath of the antibacterial K1-type Type VI Secretion System (K1-T6SS)** of *P. putida* KT2440.

TssC1 is a cytoplasmic structural/mechanical protein, not an enzyme. Together with its obligate partner **TssB1 (VipA; PP_3100)**, it polymerizes into a long phage-tail-like sheath wrapped around an inner Hcp tube. Upon a firing signal, the sheath contracts, converting stored elastic energy into a mechanical thrust that drives the Hcp tube and its associated toxic effectors (such as the Rhs-family nuclease **Tke2**) across the envelopes of neighboring competitor bacteria. After contraction, an N-terminal four-helix-bundle domain of TssC/VipB exposes a **ClpV recognition motif**, triggering ATP-driven sheath disassembly and subunit recycling. The protein therefore functions in **interbacterial competition**, operating from the bacterial cytoplasm/inner-membrane-anchored apparatus, and is a core component of a well-defined secretion nanomachine rather than a purine-catabolic enzyme.

This report documents the misannotation, establishes the correct identity through domain architecture, orthology, protein length, and genomic neighborhood, and details the mechanistic role, subcellular localization, and pathway context of the protein. The correction is important: purine metabolism (the pathway implied by "puuD/uricase") and Type VI secretion (the real pathway) are entirely unrelated, and any downstream metabolic model relying on the uricase annotation of PP_3099 would be erroneous.

---

## Gene-Identity Verification (mandatory)

| Attribute | UniProt "name" evidence | Actual evidence |
|---|---|---|
| Protein name | "Uricase/urate oxidase", EC 1.7.3.3 | **Refuted** |
| Domains (InterPro/Pfam) | — | IPR010269 **T6SS_TssC-like**; IPR044031 **TssC1_N**; IPR044032 **TssC1_C**; PF05943 **VipB**; PF18945 **VipB_2** |
| Orthology | — | eggNOG **COG3517 = "Type VI secretion protein VipB/TssC"** |
| Length | uricase ≈ 300 aa (T-fold) | **500 aa** — matches TssC/VipB (~490–510 aa) |
| Keyword | "Oxidoreductase" | Derived solely from the erroneous SubName |

**Conclusion of verification:** The "uricase" annotation is a misannotation. All independent evidence identifies Q88IA0 as **TssC/VipB**. Note also that the gene symbol *puuD* elsewhere denotes γ-glutamyl-γ-aminobutyrate hydrolase of the putrescine-utilization pathway — an unrelated protein whose literature does **not** apply to this locus.

---

## Key Findings

### Finding 1 — PP_3099/Q88IA0 is a T6SS sheath protein (TssC/VipB), not a uricase

The UniProt SubName "Uricase/urate oxidase (EC 1.7.3.3, gene puuD)" is an automatic annotation (ECO:0000313) imported directly from the original genome-submission EMBL record (AAN68707.1). Multiple independent, orthogonal lines of evidence overturn it:

- **Domain architecture.** Every InterPro/Pfam signature on the protein is a Type VI secretion sheath domain: IPR010269 (T6SS_TssC-like), IPR044031 (TssC1_N), IPR044032 (TssC1_C), PF05943 (VipB), and PF18945 (VipB_2). None corresponds to the uricase T-fold.
- **Orthology.** The eggNOG orthologous group is **COG3517**, defined explicitly as "Type VI secretion protein VipB/TssC."
- **Protein length.** Q88IA0 is **500 amino acids**, matching the ~490–510 aa size of TssC/VipB sheath proteins and far larger than the ~300-aa T-fold uricase.
- **Absence of catalytic machinery.** The protein contains no uricase catalytic residues and no tunneling-fold (T-fold) domain, the diagnostic features of genuine urate oxidases. The "Oxidoreductase" keyword on the UniProt entry is inherited solely from the erroneous SubName and has no supporting evidence.

Taken together, the weight of evidence unambiguously reclassifies PP_3099 as a T6SS sheath component. The uricase/EC 1.7.3.3 label should be treated as a documented legacy error.

### Finding 2 — PP_3099 (TssC) sits in a canonical T6SS structural operon and pairs with TssB (PP_3100)

The genomic neighborhood of PP_3099 in *P. putida* KT2440 is a textbook T6SS sheath/baseplate arrangement:

| Locus | Component | Pfam / feature | Role |
|-------|-----------|----------------|------|
| PP_3096 | TssG | PF06996 | Baseplate |
| PP_3097 | TssF | PF05947 | Baseplate |
| PP_3098 | TssE (Gp25-like) | PF04965 | Baseplate |
| **PP_3099** | **TssC (VipB)** | **PF05943 / PF18945** | **Sheath large subunit (this protein)** |
| PP_3100 | TssB (VipA) | PF05591 (191 aa) | Sheath small subunit |

This conserved **TssF–TssE–TssC–TssB** gene order is the canonical, phylogenetically conserved sheath/baseplate module of T6SSs. TssB and TssC are **obligate partners** that stabilize one another and co-assemble into the sheath. This partnership was demonstrated directly in *Agrobacterium tumefaciens*, where TssB (Atu4342) and TssC41 (Atu4341) were shown to interact with and stabilize each other as functional orthologs of the sheath components VipA/VipB: *"Atu4342 (TssB) and Atu4341 (TssC41) interact with and stabilize each other, which suggests that they are functional orthologs of the sheath components TssB (VipA) and TssC (VipB), respectively"* ([PMID: 23861778](https://pubmed.ncbi.nlm.nih.gov/23861778/)). The PP_3099/PP_3100 pair is the direct *P. putida* equivalent of this mutually stabilizing sheath dyad.

### Finding 3 — Mechanistic role: contractile sheath that propels the Hcp tube and effectors into target cells

TssC/VipB, in complex with TssB/VipA, forms a **phage-tail-like contractile sheath** wrapped around the inner Hcp tube. The mechanistic details are well established:

- **Structural homology to phage tail sheaths.** Cryo-EM of the *Vibrio cholerae* VipA/VipB tubule revealed that the C-terminal segment of VipB (TssC) is structurally homologous to the T4 bacteriophage tail-sheath protein: *"We localized VipA and VipB in the protomer and identified structural homology between the C-terminal segment of VipB and the tail-sheath protein of T4 phages"* ([PMID: 24953649](https://pubmed.ncbi.nlm.nih.gov/24953649/)). The 3.3 Å atomic structure of the *P. aeruginosa* TssB1/TssC1 sheath confirmed that *"the two T6SS components, TssB/VipA and TssC/VipB, assemble to form tubules that conserve structural/functional homology with tail sheaths of contractile bacteriophages and pyocins"* ([PMID: 29307484](https://pubmed.ncbi.nlm.nih.gov/29307484/)), supporting a coiled-spring contraction mechanism.
- **Contraction-state-specific recycling.** In the extended sheath, the ClpV recognition motif is buried; *"contraction leads to exposure of the ClpV recognition motif, which is embedded in the type VI-specific four-helix-bundle N-domain of VipB"* ([PMID: 24953649](https://pubmed.ncbi.nlm.nih.gov/24953649/)), restricting ClpV-driven disassembly to the post-contraction state. This ensures the sheath is only recycled after it has fired.
- **Assembly polarity and energetics.** Sheath subunits are added exclusively at the distal end, away from the baseplate/membrane anchor ([PMID: 28703218](https://pubmed.ncbi.nlm.nih.gov/28703218/)). Rapid contraction releases stored energy that pushes the tube and toxins across the membranes of neighboring target cells ([PMID: 31226022](https://pubmed.ncbi.nlm.nih.gov/31226022/)).
- **Payload in *P. putida*.** In KT2440, the K1-T6SS — the very system this sheath serves — is a potent antibacterial device: *"We show that the K1-T6SS is a potent antibacterial device, which secretes a toxic Rhs-type effector Tke2"* ([PMID: 28045455](https://pubmed.ncbi.nlm.nih.gov/28045455/)).

Thus PP_3099's function is mechanical: it stores elastic energy in the extended state and, upon contraction, delivers the kinetic thrust required to inject toxins into competitor cells.

### Finding 4 — PP_3099 is embedded in a complete, membrane-complex-containing T6SS cluster; KT2440 encodes three such systems

The PP_3099 cluster contains a full complement of T6SS genes spanning all three functional modules:

- **Membrane complex:** PP_3090 (OmpA/TssJ-like lipoprotein), PP_3091 (ImcF/TssM, 1267 aa), PP_3092 (DotU/TssL)
- **Baseplate:** TssK, TssE, TssF, TssG
- **Sheath:** TssC (PP_3099) + TssB (PP_3100)

The presence of a complete membrane complex plus baseplate plus sheath confirms this is a functional, envelope-anchored secretion system rather than an isolated gene. Moreover, *P. putida* KT2440 encodes **three** T6SS clusters, evidenced by three TssB/VipA (PF05591) paralogs — PP_3100, PP_2624, PP_4074 — each with its cognate TssC partner (PP_3099, PP_2623, and the PP_4074-cluster copy). This matches the report that *"we analyze the genome of the biocontrol agent Pseudomonas putida KT2440 and identify three T6SS gene clusters (K1-, K2- and K3-T6SS)"* ([PMID: 28045455](https://pubmed.ncbi.nlm.nih.gov/28045455/)). PP_3099 lies in the structural region (~PP_3090–PP_3105) of the well-characterized antibacterial **K1-T6SS**.

### Finding 5 — PP_3099 = tssC1 of the K1-T6SS structural operon; the "uricase" name reflects historic misannotation

The 44-kb K1-T6SS cluster of KT2440 comprises a **structural operon** of 15 genes — the 12 core components TssABCDEFGHJKLM plus accessory genes (TagF1/TagP1/TagB1) — and a separate **vgrG operon** (VgrG1, adapters EagR1a/b, the Rhs/nuclease toxin Tke2 with its immunity protein Tki2, and Tke3/Tki3). The structural operon occupies the PP_309x region, placing **PP_3099 as tssC1**, the sheath large subunit of the K1-T6SS ([PMID: 28045455](https://pubmed.ncbi.nlm.nih.gov/28045455/); transcriptional-organization follow-up [PMID: 36748579](https://pubmed.ncbi.nlm.nih.gov/36748579/)).

Critically, before these bioinformatic analyses, only ~5 T6SS genes in KT2440 were annotated; the remaining structural genes — including PP_3099 — carried erroneous automatic names such as "uricase/urate oxidase." This directly explains the ECO:0000313 EMBL misannotation of Q88IA0 as puuD/uricase.

---

## Mechanistic Model / Interpretation

### The corrected identity

```
  LEGACY ANNOTATION (wrong)          CORRECTED IDENTITY (this report)
  ─────────────────────────          ────────────────────────────────
  puuD / Uricase, EC 1.7.3.3    →    tssC1 / TssC (VipB)
  Purine catabolism             →    Type VI Secretion System (K1-T6SS)
  ~300 aa T-fold enzyme         →    500 aa contractile sheath subunit
  Metabolic oxidoreductase      →    Structural/mechanical nanomachine part
```

### The K1-T6SS structural operon and the sheath dyad

```
 PP_3090   PP_3091   PP_3092  ...  PP_3096  PP_3097  PP_3098  PP_3099   PP_3100
 TssJ      TssM      TssL          TssG     TssF     TssE     TssC      TssB
 (OmpA)    (ImcF)    (DotU)        └──────── baseplate ───────┘ └── sheath ──┘
 └──── membrane complex ────┘

 Sheath dyad:  TssC1 (PP_3099, 500 aa)  +  TssB1 (PP_3100, 191 aa)
               obligate, mutually stabilizing partners
```

### The firing cycle

```
   1. ASSEMBLY          2. LOADING            3. FIRING             4. RECYCLING
   ───────────          ──────────            ─────────             ────────────
   Membrane complex     Hcp tube +            Extended sheath       ClpV recognizes
   (TssJLM) anchors     effectors (Tke2)      contracts → thrust    exposed N-domain
   baseplate; TssBC     load onto/into        pushes tube+toxin     motif on contracted
   sheath polymerizes   sheath                across neighbor's     TssC → ATP-driven
   at distal end                              envelope              disassembly
```

The subcellular localization of the process is the **bacterial cytoplasm and inner membrane**: the sheath (TssC/TssB) assembles in the cytoplasm anchored via the membrane complex to the cell envelope; the effector payload is delivered **outside the cell, into the cytoplasm of a directly contacted target bacterium**. This is a contact-dependent, antibacterial mechanism relevant to *P. putida*'s role as a rhizosphere biocontrol agent that outcompetes phytopathogens.

### Why this matters

The two candidate functions are biologically unrelated. Uricase (EC 1.7.3.3) catalyzes the oxidation of urate to 5-hydroxyisourate in purine degradation. TssC is a structural piston component of a protein-injection nanomachine. No enzymatic activity — oxidoreductase or otherwise — should be attributed to PP_3099. The correct function is **mechanical energy storage and delivery for interbacterial toxin injection**.

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports the findings |
|------|-----------------|------------------------------|
| [28045455](https://pubmed.ncbi.nlm.nih.gov/28045455/) | *The P. putida T6SS is a plant warden against phytopathogens* | Establishes KT2440's three T6SS clusters (K1/K2/K3), the antibacterial K1-T6SS, and its Rhs effector Tke2 — the system PP_3099 serves. |
| [36748579](https://pubmed.ncbi.nlm.nih.gov/36748579/) | *Transcriptional organization and regulation of the T6SS* | Defines the K1-T6SS structural vs. vgrG operon organization placing PP_3099 as tssC1. |
| [23861778](https://pubmed.ncbi.nlm.nih.gov/23861778/) | *Systematic dissection of the Agrobacterium T6SS* | Shows TssB and TssC are mutually stabilizing sheath partners (VipA/VipB orthologs) — the model for PP_3099/PP_3100. |
| [24953649](https://pubmed.ncbi.nlm.nih.gov/24953649/) | *Structure of the VipA/B T6SS complex* | Identifies VipB (TssC) as phage-tail-sheath-homologous and defines the contraction-state ClpV recycling mechanism. |
| [29307484](https://pubmed.ncbi.nlm.nih.gov/29307484/) | *Atomic structure of Type VI contractile sheath from P. aeruginosa* | Confirms TssB/TssC form phage-tail-like sheath tubules in *Pseudomonas*; coiled-spring contraction. |
| [28703218](https://pubmed.ncbi.nlm.nih.gov/28703218/) | *T6SS sheath assembles at the end distal from the membrane anchor* | Establishes sheath assembly polarity. |
| [31226022](https://pubmed.ncbi.nlm.nih.gov/31226022/) | *Assembly and subcellular localization of bacterial T6SS* | Reviews the contraction-driven energy release that propels tube and toxins across membranes; subcellular localization. |
| [35178858](https://pubmed.ncbi.nlm.nih.gov/35178858/) | *Wsp system modulates K1-T6SS via FleQ-FleN* | Confirms the K1-T6SS structural operon (containing PP_3099) is transcriptionally regulated by c-di-GMP signaling. |
| [41526723](https://pubmed.ncbi.nlm.nih.gov/41526723/) | *Structural insights into the P. putida effector Tke5* | Documents additional K1-T6SS effectors (Tke5) delivered by the system. |
| [40176102](https://pubmed.ncbi.nlm.nih.gov/40176102/) | *Engineering the T6SS of Pseudomonas* | Demonstrates KT2440 T6SS as an engineerable effector-delivery platform. |

**Convergence of evidence:** Domain composition (all VipB/TssC), orthology (COG3517 = VipB/TssC), protein length (500 aa), genomic context (canonical sheath/baseplate operon with obligate partner TssB1), and cluster completeness (full membrane complex + baseplate + sheath in the K1-T6SS) all point to the same conclusion. No evidence supports the uricase annotation.

---

## Supported and Refuted Hypotheses

- **Refuted:** PP_3099 is a uricase/urate oxidase (EC 1.7.3.3). No T-fold, no catalytic residues; the annotation is a computational artifact from the original 2002 genome submission.
- **Supported:** PP_3099 = TssC1 (VipB), the T6SS contractile-sheath large subunit (domains, COG3517 orthology, 500-aa length, operon context, homology to characterized orthologs).
- **Supported:** The function is structural/mechanical — sheath contraction to deliver antibacterial effectors (e.g., Tke2) — not enzymatic.

---

## Limitations and Knowledge Gaps

1. **No PP_3099-specific experimental structure or biochemistry.** The mechanistic model is built on strong orthology to well-characterized TssC/VipB proteins from *V. cholerae*, *P. aeruginosa*, and *A. tumefaciens*, plus KT2440 cluster-level functional studies. A direct structural or biochemical study of the *P. putida* KT2440 TssB1/TssC1 sheath itself has not been reported here; the assignment rests on homology and genomic context.
2. **Effector-delivery specificity.** While Tke2 (Rhs nuclease) and Tke5 (pore-forming toxin) are documented K1-T6SS effectors, the precise coupling of the PP_3099 sheath to individual effector-loading events has not been dissected at the single-protein level.
3. **Formal database correction pending.** The UniProt entry Q88IA0 still carries the uricase SubName and Oxidoreductase keyword (ECO:0000313 automatic annotation). This report documents the error, but correcting the public record is a separate action.
4. **Paralog discrimination.** KT2440 has three TssC paralogs (PP_3099, PP_2623, and the PP_4074-cluster copy). The functional distinctions among the K1/K2/K3 sheaths — e.g., differential effector repertoires or regulation — remain only partially characterized.

---

## Proposed Follow-up Experiments / Actions

1. **Submit a UniProt annotation correction** for Q88IA0: replace "Uricase/urate oxidase, EC 1.7.3.3, puuD" with "Type VI secretion system contractile sheath large subunit TssC1 (VipB)"; remove the EC number and Oxidoreductase keyword; add T6SS/interbacterial-competition GO terms and the InterPro TssC signatures already present.
2. **Experimentally verify the sheath dyad** in KT2440: co-express and co-purify PP_3099 (TssC1) with PP_3100 (TssB1); test mutual stabilization and in vitro tubule/sheath assembly by negative-stain or cryo-EM, mirroring the VipA/VipB and *P. aeruginosa* TssB1C1 studies.
3. **Genetic knockout phenotyping:** delete PP_3099 and assay loss of K1-T6SS antibacterial activity (interbacterial killing assays vs. a susceptible prey, and secretion of Hcp/VgrG1 into culture supernatant) to confirm it is essential for a functional sheath.
4. **Live-cell fluorescence imaging** of a TssC1-sfGFP fusion to visualize sheath assembly/contraction dynamics and subcellular localization in KT2440.
5. **ClpV-recycling assay:** test whether the KT2440 ClpV recognizes the contracted-state N-domain motif of PP_3099, confirming the recycling arm of the mechanism.
6. **Assay for absence of uricase activity:** as a definitive negative control, purify PP_3099 and confirm it has no urate-oxidase activity, formally closing out the legacy annotation.

---

## Conclusion

PP_3099 (Q88IA0), historically mislabeled "puuD / uricase (EC 1.7.3.3)," is **TssC1 (VipB)**, the large subunit of the contractile sheath of the antibacterial **K1-Type VI Secretion System** of *Pseudomonas putida* KT2440. It is a cytoplasmic structural/mechanical protein that, with its obligate partner TssB1 (PP_3100), forms a phage-tail-like sheath that contracts to inject toxic effectors (e.g., the Rhs nuclease Tke2) into competitor bacteria during contact-dependent interbacterial competition. It has no enzymatic (uricase or oxidoreductase) activity; the metabolic annotation is a documented pre-2017 automatic-annotation error.


## Artifacts

- [OpenScientist final report](puuD-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](puuD-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:23861778
2. PMID:24953649
3. PMID:29307484
4. PMID:28703218
5. PMID:31226022
6. PMID:28045455
7. PMID:36748579