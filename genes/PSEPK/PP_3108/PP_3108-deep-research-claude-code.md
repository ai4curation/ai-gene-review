---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5, claude-opus-5-5
cached: false
start_time: '2026-10-30T21:10:59.704792'
end_time: '2026-10-30T21:18:15.211765'
duration_seconds: 435.51
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_3108
  gene_symbol: PP_3108
  uniprot_accession: Q88I91
  protein_description: 'SubName: Full=Rhs-related protein {ECO:0000313|EMBL:AAN68716.1};'
  gene_info: OrderedLocusNames=PP_3108 {ECO:0000313|EMBL:AAN68716.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the colicin/pyosin nuclease family.
  protein_domains: Colicin/pyocin_DNase_dom_sf. (IPR037146); DUF6531. (IPR045351);
    His-Me_finger_sf. (IPR044925); PAAR_motif. (IPR008727); prePAAR_DddA. (IPR057925)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    claude_executable: claude
    skip_permissions: false
    allowed_tools:
    - WebSearch
    - WebFetch
    add_dirs: []
    timeout: 1800
    min_report_chars: 200
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-5-5
  - claude-opus-5
  - claude-opus-5-5
  web_search_requests: 6
  num_turns: 17
  total_cost_usd: 2.0353371350000002
  session_id: aa0e836a-c522-4770-89fa-28dab35bcab8
  stop_reason: end_turn
  assistant_text_blocks: 4
citation_count: 6
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q88I91
- **Protein Description:** SubName: Full=Rhs-related protein {ECO:0000313|EMBL:AAN68716.1};
- **Gene Information:** OrderedLocusNames=PP_3108 {ECO:0000313|EMBL:AAN68716.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the colicin/pyosin nuclease family.
- **Key Domains:** Colicin/pyocin_DNase_dom_sf. (IPR037146); DUF6531. (IPR045351); His-Me_finger_sf. (IPR044925); PAAR_motif. (IPR008727); prePAAR_DddA. (IPR057925)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_3108" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_3108' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_3108** (gene ID: PP_3108, UniProt: Q88I91) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

Continuing — checking whether PP_3108 is the Tke2/Rhs effector by looking at its genomic neighbourhood and domain evidence.

Key hit: the Pseudomonas Genome DB names PP_3108 **tke2**. Verifying the gene neighbourhood.

Neighbourhood resolved. One quick check of the flanking proteins' domains, then I'll write the report.

# Research Report: PP_3108 (UniProt Q88I91), *Pseudomonas putida* KT2440

## 0. Identity verification (mandatory check)

| Check | Result |
|---|---|
| Locus tag | `PP_3108`; UniProt `Q88I91` (`Q88I91_PSEPK`), 1385 aa, 155,812 Da |
| UniProt protein name | "SubName: Full=Rhs-related protein {ECO:0000313\|EMBL:AAN68716.1}" — a **submitter-supplied** name, not curated |
| Organism | *Pseudomonas putida* KT2440 (NCBI taxid 160488) — matches |
| Domains (UniProt/InterPro) | prePAAR_DddA (IPR057925, PF25799, res. 1–58); PAAR motif (IPR008727, PF05488; CDD cd14742 PAAR_RHS); DUF6531 (IPR045351, PF20148, res. 232–305); RHS repeat (PF05593) + 3× Teneurin-like YD-shell (PF25023; res. 479–597, 644–779, 999–1249); Rhs-associated core (TIGR03696); 6× YD_repeat_2x (TIGR01643); **Colicin/pyocin DNase domain superfamily (IPR037146) + His-Me finger endonuclease (SSF54060, IPR044925)** at the C-terminus |
| Family statement | "Belongs to the colicin/pyosin nuclease family" — evidence `ECO:0000256|ARBA:ARBA00006811`, i.e. an **automatic association rule**, not curator- or experiment-backed |
| Family-level classification | PANTHER PTHR32305 / PTHR32305:SF15 "PROTEIN RHSA-RELATED"; IPR050708 "T6SS VgrG/RHS" |

**Verdict: the identity is consistent and the gene is not symbol-ambiguous.** The domain architecture (N-terminal prePAAR → PAAR → DUF6531 → long RHS/YD-shell → C-terminal His-Me finger nuclease) is the textbook organisation of a "specialised"/evolved-PAAR **type VI secretion system (T6SS) Rhs effector**, and it matches the UniProt description.

Note one annotation artefact: UniProt lists two Phobius-predicted transmembrane helices at residues 16–36 and 43–64 (`ECO:0000256|SAM:Phobius`). These coincide exactly with the prePAAR region, and prePAAR effectors are **defined** by hydrophobic N-terminal TMD-like segments that are chaperone-shielded rather than membrane-inserted in the donor cell ([Ahmad et al. 2020, eLife 9:e62816](https://elifesciences.org/articles/62816)). Treating PP_3108 as an inner-membrane protein on the strength of those two helices would be a mis-read.

## 1. Headline conclusion

PP_3108 is, on strong convergent evidence, **Tke2** — the Rhs-type, PAAR-bearing, HNH-nuclease antibacterial effector of the **K1-T6SS** of *P. putida* KT2440 characterised experimentally by Bernal et al. (2017). It is a **toxin delivered into competitor bacteria**, where its C-terminal His-Me finger (colicin/pyocin-like) domain is predicted to act as a nuclease; the producing cell is protected by the cognate immunity protein **Tki2**. Its site of action is the **cytoplasm of the recipient (prey) cell**, not the *P. putida* cytoplasm.

The locus-tag assignment requires an explicit chain of reasoning, given below, because the primary paper names effectors (Tke1–Tke10) without locus tags.

## 2. Establishing that PP_3108 = Tke2

**2.1 Direct database naming.** The Pseudomonas Genome Database gene page for PP_3108 carries the gene name **`tke2`** (https://pseudomonas.com/feature/show/?id=38827688&view=functions). The site refuses automated fetches (HTTP 403), so I verified this only through indexed search snippets, which report the page as "Functions: tke2, Pseudomonas putida KT2440" with PAAR and RHS-repeat domain predictions. This is a database curator's assignment, not a statement in a paper.

**2.2 Genomic context — the decisive evidence.** Bernal et al. (2023) describe the K1-T6SS "V operon" gene order verbatim: *"The vgrG operon encompasses genes encoding proteins with unknown function (PP3104 and PP3105), the VgrG1 protein and associated adapters EagR1a and EagR1b, the Tke2 nuclease toxin and its cognate immunity protein Tki2, and an additional putative effector–immunity pair (Tke3–Tki3)"* ([Bernal et al. 2023, Microbiology 169:001295, PMC9993120](https://pmc.ncbi.nlm.nih.gov/articles/PMC9993120/)). The paper gives locus tags only for the first two genes.

I resolved the rest from the UniProt proteome (REST query, taxid 160488):

| Locus | UniProt | Length | Domains / name | Inferred identity |
|---|---|---|---|---|
| PP_3104 | Q88I95 | 322 | — | stated in paper: unknown function |
| PP_3105 | Q88I94 | 231 | — | stated in paper: unknown function |
| PP_3106 | Q88I93 | 618 | IPR006533 (Rhs-element Vgr), IPR017847 (T6SS VgrG), PF04717 Phage_base_V, PF05954 Phage_GPD | **VgrG1** |
| PP_3107 | Q88I92 | 173 | **PF08786 DUF1795** (IPR014894) | **EagR1** chaperone |
| **PP_3108** | **Q88I91** | **1385** | prePAAR–PAAR–RHS–His-Me finger | **Tke2** |
| PP_3109 | Q88I90 | 143 | PF03527, "RHS protein conserved region domain-containing protein" | **Tki2** (size and position) |
| PP_3110 | Q88I89 | 70 | — | small ORF, possibly within the tke3–tki3 region |

The gene order PP_3104 → PP_3105 → VgrG1 → DUF1795 adaptor → 1385-aa PAAR/Rhs/HNH protein → small downstream protein reproduces the published operon description exactly. Combined with the independent `tke2` naming in the Pseudomonas Genome DB, the assignment PP_3108 = Tke2 is as secure as the published record allows.

*One residual discrepancy to flag honestly:* Bernal et al. name **two** adaptors, EagR1a and EagR1b, but only PP_3107 carries a DUF1795 signature in UniProt. The second may be PP_3105 (231 aa, no assigned domain) or may correspond to a gene model not separately represented. I could not resolve this; the published Figure 2a carries the PP numbers but is an image I could not read.

## 3. Primary molecular function

### 3.1 The toxin domain: a His-Me finger (colicin/pyocin DNase-like) nuclease

Bernal et al. (2017) state that the C-terminal ~110 aa of Tke2 belongs to the **HNH nuclease superfamily**, with similarity to **colicin E7 and pyocin S1** — both of which are well-characterised, metal-dependent, non-specific DNA-degrading HNH/His-Me finger endonucleases ([Bernal et al. 2017, ISME J 11:972–987, PMID:28045455](https://pmc.ncbi.nlm.nih.gov/articles/PMC5363822/)). This agrees with the independent signatures on Q88I91: SUPFAM SSF54060 "His-Me finger endonucleases", Gene3D 3.90.540.10 "Colicin/pyocin, DNase domain", IPR037146 and IPR044925.

Inspecting the sequence directly, the C-terminal region (res. ~1260–1385) contains a candidate ββα-Me active site:

```
1321 KTDKISIREYALELHHNDIPQRVGGAGVHDSSNLLALTPWEHEAVDQFRHVGSDLIRVIK
          ...H1335 H1336 N1337...H1349...N1353...
```

The spacing **H1335/H1336 – N1337 – H1349** is the canonical His-Me finger arrangement (a general-base histidine, a structural asparagine, and a metal-coordinating histidine ~12 residues downstream), matching the colicin E7/E9 DNase and pyocin S-type paradigm. *This residue assignment is my own bioinformatic inference from the sequence and the SSF54060/Gene3D boundaries; no mutagenesis of Tke2 has been reported, so the catalytic residues are a prediction and not an experimental result.*

**Substrate specificity is not established.** The colicin E7/pyocin S1 relatives are non-specific DNases (double- and single-stranded DNA, with Ni²⁺/Zn²⁺/Mg²⁺ dependence varying by member), but HNH-superfamily T6SS effectors also include tRNases and ssDNases. No nuclease assay on Tke2 has been published. UniProt's GOA carries `GO:0004519 endonuclease activity` with evidence code `ECO:0000256` — an automatic, sequence-model-based assertion, with no experimental backing.

Note also that UniProt's "belongs to the colicin/pyocin nuclease family" line is an **ARBA rule** (`ECO:0000256|ARBA:ARBA00006811`) — a prediction, and so is not independent support for the family claim; the independent support is the InterPro/SUPFAM/Gene3D signature set plus the Bernal et al. Phyre2-based structural comparison.

### 3.2 The experimental evidence that Tke2 is a toxin

Three experiments in Bernal et al. (2017) bear directly on this protein:

1. **Toxicity and immunity.** The isolated C-terminal domain (construct pTke2-CT) was expressed in *E. coli*: *"On induction of the effector gene tke2, E. coli growth was significantly impaired but growth could readily be rescued on co-expression of the putative Tki2 immunity protein."* This establishes (i) that the C-terminal domain is the toxic moiety, and (ii) that Tke2–Tki2 is a genuine effector–immunity pair. It does **not** establish the biochemical activity — growth arrest is consistent with, but not proof of, nuclease action.
2. **T6SS-dependent secretion.** Chromosomally V5-tagged Tke2 was detectable only weakly, so secretion was assayed in an *rpoN* background: *"Tke2 was produced in both the rpoN strain and the isogenic T6SS mutant (rpoNΔtssA1), but was only found in the supernatant of the strain with an intact T6SS."* The authors conclude *"Tke2 is an effector of the K1-T6SS."* This is the key localisation result: the protein **leaves the cell through the K1-T6SS apparatus**.
3. **Contribution to interbacterial killing.** The authors report that *"the Tke2 toxin contributes to the antibacterial activity"* of *P. putida*, within a K1-T6SS that kills a broad range of competitors; killing of *E. coli* was abolished in K1 structural mutants but retained in K2 and K3 mutants.

### 3.3 Architecture and delivery mechanism

The non-toxin two-thirds of the protein are delivery and packaging machinery, not catalytic:

- **prePAAR (res. 1–58).** Pfam assigns this as the DddA-type prePAAR motif (PF25799). prePAAR marks a large family of TMD-containing T6SS effectors (>6,000 across ~15 proteobacterial genera) that *"are unified by their requirement for a member of the Eag family of T6SS chaperones for export"*; beyond chaperone binding, *"prePAAR functions to facilitate proper folding of the downstream PAAR domain, which is required for effector interaction with the T6SS spike"* ([Ahmad et al. 2020, eLife 9:e62816](https://elifesciences.org/articles/62816)). The adjacent **PP_3107 DUF1795/Eag chaperone** is precisely the partner this model predicts, and Eag chaperones work by *mimicking transmembrane helical packing to stabilise effector TMDs* (co-crystal structures, e.g. Tse6–EagT6, PDB 6XRF). This is a strong, mechanistically specific prediction for PP_3108 that has not been tested directly in *P. putida*.
- **PAAR domain (~res. 65–150; CDD cd14742 PAAR_RHS).** The PAAR repeat — visible in the sequence as the tandem `…SPNVFINSRKAARV…` / `…STNVFINSVAAARK…` / `…SDNVIIGGGTYRY…` motifs — forms the conical tip that caps the **VgrG1 spike** (PP_3106), sharpening it and physically coupling the toxin to the puncturing device.
- **RHS / YD-shell cage (res. ~230–1250).** DUF6531 plus six YD-repeat/Teneurin-like YD-shell blocks. Bernal et al. summarise the function cautiously: *"Although the function of the Rhs domain is still unknown, it has been suggested that it forms a shell structure that encapsulates the C-terminal region of effectors."* Subsequent structural work on Rhs effectors generally supports this cocoon model, in which the β-barrel shell sequesters the toxin during transit and releases it by aspartyl autoproteolysis in the prey cytoplasm. For Tke2 specifically, neither the encapsulation nor an autoproteolytic release step has been demonstrated.

So the mechanistic chain is: **Eag chaperone (PP_3107) stabilises prePAAR → PAAR caps VgrG1 (PP_3106) → T6SS fires the spike into an adjacent bacterium → the RHS shell releases the HNH domain in the prey cytoplasm → nucleic-acid damage → prey death**, with Tki2 (PP_3109) neutralising any Tke2 that re-enters a sibling cell. Steps 3 (secretion) and the toxin/immunity relationship are experimentally supported; the chaperone, spike-capping and shell-release steps are domain-based inference.

## 4. Localisation

| Compartment | Status |
|---|---|
| *P. putida* cytoplasm | Site of synthesis and of assembly with EagR1/VgrG1 prior to firing (inferred) |
| T6SS spike complex | Predicted component of the VgrG1 tip via PAAR (inference from domain and operon) |
| Extracellular medium | **Experimentally demonstrated** — Tke2-V5 in culture supernatant, strictly dependent on an intact K1-T6SS (Bernal et al. 2017) |
| Prey-cell cytoplasm | Site of toxic action (inferred: HNH nucleic-acid target plus cytoplasmic immunity protein; not directly imaged) |
| Inner membrane | **Not supported.** The two Phobius TM helices are the prePAAR hydrophobic segment, chaperone-shielded rather than membrane-integrated |

The periplasmic-vs-cytoplasmic question was not addressed for Tke2 in the primary paper; the inference to the cytoplasm rests on the nature of the toxin domain and on the general behaviour of PAAR/Rhs effectors.

## 5. Pathway and regulatory context

PP_3108 sits within the **44 kb K1-T6SS gene cluster**, one of three T6SS clusters (K1, K2, K3) in KT2440; the K1 system is the antibacterial one and belongs to T6SS group 4B, with *tagX1* (PP3101.1) as a hallmark (Bernal et al. 2017). Ten effector–immunity pairs (Tke1–Tke10 / Tki1–Tki10) were identified genome-wide; at least three (*tke1-tki1*, *tke2-tki2*, *tke3-tki3*) lie in the K1 cluster. Tke2 and Tke4 are the PAAR-containing "specialised" effectors.

Regulation of the operon containing *tke2* (the "V operon") was mapped in [Bernal et al. 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC9993120/):

- The V operon is a single transcriptional unit driven by two **σ70 promoters, PV1 and PV2**, upstream of PP_3104; intergenic gaps within the operon are 0–25 nt. No internal *tke2* promoter was found, so *tke2* expression is operon-level.
- The cluster is **induced in stationary phase** (PV::lacZ ~5,000 → ~9,000 Miller units).
- **Positively regulated by the GacS–GacA** two-component system (PV activity down 2–3-fold in a *gacS* mutant); **RetS** represses the S operon but did not affect PV.
- **RpoS** represses: PS and PV activity rose in its absence.
- **RpoN represses** the cluster (indirectly, likely via FleQ — "the effect of RpoN is likely indirect since σ factors usually promote instead of inhibiting transcription"). Consistently: *"production of the Tke2 effector was considerably higher in a rpoN mutant"*. This is why the 2017 secretion assay was performed in an *rpoN* background.

Biologically, the K1-T6SS confers **interbacterial competition and biocontrol**: *P. putida* eradicates diverse bacteria, including the phytopathogen *Xanthomonas campestris*, in a K1-T6SS-dependent manner, and reduces necrosis in co-infected *Nicotiana benthamiana* leaves (Bernal et al. 2017). Tke2 is one contributor to that activity, alongside the NAD(P)⁺-degrading Tke1 (a Tse6 orthologue) and the colicin-S4-like pore-formers Tke7/Tke8.

A separate note on genomic context: PP_3108 lies within KT2440 **genomic island 59**, one of three *rhs*-family genes placed in GIs (the others being PP_4085 and PP_4093.2) — consistent with horizontal acquisition of the toxin, as is typical for Rhs/T6SS effector repertoires.

## 6. What is *not* known

1. **No enzymology.** No nuclease assay, no substrate determination (dsDNA vs ssDNA vs tRNA), no metal requirement, no catalytic-residue mutagenesis for Tke2. The `GO:0004519` annotation is purely computational.
2. **No structure** of Tke2 or of the Tke2–Tki2 complex; the Tki2 inhibition mechanism (active-site occlusion, as for Im7/Im9 against colicin DNases, vs. another mode) is unknown.
3. **The RHS cocoon and its release** have not been demonstrated for Tke2; no autoproteolysis site has been mapped.
4. **The EagR1a/EagR1b–Tke2 interaction** is predicted from the prePAAR/Eag paradigm but not shown biochemically in *P. putida*.
5. **Full-length secretion and prey-cell delivery** were shown as supernatant accumulation; direct translocation into a recipient cytoplasm was not visualised.
6. **The Tki2 locus tag (PP_3109) is my inference** from gene order and size, not a published assignment.

## 7. Suggested annotation stance

- Molecular function: the His-Me finger / colicin-pyocin DNase assignment is well supported at the **sequence-family** level (InterPro, SUPFAM, Gene3D, plus the authors' Phyre2 comparison to colicin E7/pyocin S1) but not experimentally; `GO:0004519 endonuclease activity` is a reasonable ISS/ISM-grade claim, not an IDA-grade one. `GO:0004536 DNA nuclease activity` or a deoxyribonuclease child would over-reach without an assay.
- Process: `GO:0033104` (type VI protein secretion system complex) is not appropriate for an effector; the defensible process claims are secretion by the T6SS (experimentally shown for this protein) and **interbacterial antagonism / killing of cells of another organism** — the latter supported for the K1 system as a whole and, per the authors, contributed to by Tke2.
- Component: extracellular region, by IDA (supernatant, T6SS-dependent). Do **not** annotate membrane from the Phobius helices.

---

### Sources

- [Bernal P, Allsopp LP, Filloux A, Llamas MA (2017) *The Pseudomonas putida T6SS is a plant warden against phytopathogens.* ISME J 11:972–987. PMID:28045455](https://pmc.ncbi.nlm.nih.gov/articles/PMC5363822/) — primary experimental source for Tke2 (architecture, toxicity, Tki2 immunity, T6SS-dependent secretion).
- [Bernal P et al. (2023) *Transcriptional organization and regulation of the Pseudomonas putida K1 type VI secretion system gene cluster.* Microbiology 169:001295. PMC9993120](https://pmc.ncbi.nlm.nih.gov/articles/PMC9993120/) — V-operon gene order (VgrG1–EagR1a/b–Tke2–Tki2–Tke3–Tki3), promoters, GacS/RetS/RpoS/RpoN/FleQ regulation.
- [Ahmad S, Tsang KK, Sachar K, et al. (2020) *Structural basis for effector transmembrane domain recognition by type VI secretion system chaperones.* eLife 9:e62816](https://elifesciences.org/articles/62816) — prePAAR motif, Eag/DUF1795 chaperone requirement, evolved-PAAR effector class.
- [Pseudomonas Genome DB, PP_3108 / *tke2* feature page](https://pseudomonas.com/feature/show/?id=38827688&view=functions) — gene-name assignment and domain predictions (page served HTTP 403 to automated retrieval; read via indexed snippets only).
- UniProtKB Q88I91 and REST queries over proteome taxid 160488 (local `PP_3108-uniprot.txt`; neighbours Q88I95, Q88I94, Q88I93, Q88I92, Q88I90, Q88I89) — domain architecture and operon reconstruction.
- [Molina L et al. (2012) *Stability of a Pseudomonas putida KT2440 bacteriophage-carried genomic island…* Appl Environ Microbiol. PMC3457469](https://pmc.ncbi.nlm.nih.gov/articles/PMC3457469/) — placement of PP_3108 in genomic island 59.
- [Hernandez RE, Gallegos-Monterrosa R, Coulthurst SJ, review context: Effector–immunity pairs and T6SS. Molecules 23:1009](https://pmc.ncbi.nlm.nih.gov/articles/PMC6099711/) — general effector–immunity framework.

## Citations

1. https://elifesciences.org/articles/62816
2. https://pseudomonas.com/feature/show/?id=38827688&view=functions
3. https://pmc.ncbi.nlm.nih.gov/articles/PMC9993120/
4. https://pmc.ncbi.nlm.nih.gov/articles/PMC5363822/
5. https://pmc.ncbi.nlm.nih.gov/articles/PMC3457469/
6. https://pmc.ncbi.nlm.nih.gov/articles/PMC6099711/