---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-20T18:18:07.274914'
end_time: '2026-07-20T18:28:51.220024'
duration_seconds: 643.95
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_2482
  gene_symbol: PP_2482
  uniprot_accession: Q88K11
  protein_description: 'SubName: Full=Molybdenum cofactor biosynthesis protein A {ECO:0000313|EMBL:AAN68094.1};'
  gene_info: OrderedLocusNames=PP_2482 {ECO:0000313|EMBL:AAN68094.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: Aldolase_TIM. (IPR013785); Elp3/MiaA/NifB-like_rSAM. (IPR006638);
    MoaA-like. (IPR040064); MoaA_twitch. (IPR010505); MoCo_biosynth_MoaA/MoaC. (IPR050105)
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
  path: PP_2482-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PP_2482-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88K11
- **Protein Description:** SubName: Full=Molybdenum cofactor biosynthesis protein A {ECO:0000313|EMBL:AAN68094.1};
- **Gene Information:** OrderedLocusNames=PP_2482 {ECO:0000313|EMBL:AAN68094.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** Aldolase_TIM. (IPR013785); Elp3/MiaA/NifB-like_rSAM. (IPR006638); MoaA-like. (IPR040064); MoaA_twitch. (IPR010505); MoCo_biosynth_MoaA/MoaC. (IPR050105)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_2482" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_2482' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_2482** (gene ID: PP_2482, UniProt: Q88K11) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: PP_2482 (Q88K11) — MoaA, a Radical SAM GTP 3′,8-Cyclase in *Pseudomonas putida* KT2440

**UniProt:** Q88K11 | **Locus:** PP_2482 | **Organism:** *Pseudomonas putida* KT2440 (PSEPK)
**Annotated name:** Molybdenum cofactor biosynthesis protein A (MoaA)
**Enzyme class:** EC 4.1.99.22 — GTP 3′,8-cyclase (KEGG KO K03639; module M00880)

## Summary

**PP_2482 (UniProt Q88K11) of *Pseudomonas putida* KT2440 encodes MoaA, a cytoplasmic radical S-adenosyl-L-methionine (radical SAM) enzyme that catalyzes the first committed step of molybdenum cofactor (Moco) biosynthesis.** The enzyme is a **GTP 3′,8-cyclase (EC 4.1.99.22)** that converts 5′-GTP into 3′,8-cyclo-7,8-dihydro-GTP (3′,8-cH₂GTP), which its partner enzyme MoaC then processes into cyclic pyranopterin monophosphate (cPMP, historically "precursor Z"). This is the entry point of an ancient, highly conserved four-step pathway that produces Moco, the pterin-based cofactor required by essentially all molybdoenzymes across biology.

The identification is robust and multiply corroborated. The 322-amino-acid Q88K11 sequence carries the two structural hallmarks that define the MoaA subfamily of radical SAM enzymes: an N-terminal **CX₃CX₂C** motif (residues C21–C25–C28) that ligates the SAM-cleaving [4Fe-4S] cluster (cluster I), and a C-terminal "twitch" domain (Pfam PF06463) that provides a second, substrate-binding [4Fe-4S] cluster (cluster II). The protein terminates in the conserved C-terminal di-glycine gate (…SALIMKSV**GG**), which is essential for radical initiation in characterized MoaA orthologs. InterPro, Pfam (PF04055 Radical_SAM), KEGG (ppu:PP_2482 → K03639, EC 4.1.99.22, module M00880), and BioCyc all converge on the same GTP 3′,8-cyclase / Moco-biosynthesis assignment, and the gene sits in a molybdoenzyme-associated genomic neighborhood.

Mechanistically, MoaA is one of the founding and most conserved members of the radical SAM superfamily. Its N-terminal cluster reductively cleaves SAM to generate a transient, highly reactive 5′-deoxyadenosyl radical; its C-terminal cluster binds GTP through direct coordination of the guanine N1 nitrogen to the cluster's unique iron. Radical abstraction and a novel C3′–C8 carbon–carbon bond formation produce the cyclized product. Because Moco is required to activate more than 50 bacterial molybdoenzymes (nitrate reductase, DMSO reductase, formate dehydrogenase, xanthine dehydrogenase, and others), MoaA occupies an essential, upstream, non-redundant position: loss of MoaA function causes pleiotropic loss of all molybdoenzyme activities. In *P. putida* KT2440—a metabolically versatile soil bacterium—MoaA (PP_2482) supplies the Moco needed for anaerobic/microaerobic respiration and purine/nitrogen metabolism carried out by its molybdoenzyme repertoire.

---

## Gene/Protein Identity Verification

Before presenting findings, the mandatory identity checks required by the research brief were completed and **passed**:

| Verification step | Result |
|---|---|
| Gene symbol "PP_2482" matches protein description | ✅ UniProt Q88K11 = "Molybdenum cofactor biosynthesis protein A" (MoaA); OrderedLocusNames PP_2482 |
| Organism correct | ✅ *Pseudomonas putida* strain ATCC 47054 / DSM 6125 / KT2440 (PSEPK); KEGG ppu:PP_2482 |
| Protein family/domains align with literature | ✅ Radical SAM (IPR006638/PF04055), MoaA-like (IPR040064), MoaA_twitch (IPR010505), MoCo_biosynth MoaA/MoaC family (IPR050105), TIM-barrel-like core (IPR013785) — all consistent with the MoaA GTP 3′,8-cyclase |
| No conflicting literature for a different gene | ✅ "MoaA" is unambiguous for this function; the domain architecture and KEGG/BioCyc annotations are internally consistent |

**Conclusion:** This report describes the correct gene/protein. The literature cited concerns the MoaA enzyme family and the Moco biosynthesis pathway. Because no MoaA-specific experimental study has been published *for the P. putida ortholog itself*, functional claims for PP_2482 are made by rigorous inference from (a) the direct sequence/domain signatures present in Q88K11, (b) authoritative biochemical/structural studies of MoaA orthologs (chiefly *Staphylococcus aureus* and *Escherichia coli*), and (c) database orthology assignments. This inferential basis is explicitly flagged in the Limitations section.

---

## Key Findings

### Finding 1 — PP_2482 (Q88K11) is MoaA, a radical SAM GTP 3′,8-cyclase catalyzing the first step of Moco biosynthesis

UniProt accession Q88K11 / locus PP_2482 in *P. putida* KT2440 is annotated as "Molybdenum cofactor biosynthesis protein A." The InterPro domain complement is diagnostic of the MoaA subfamily: a radical SAM domain (IPR006638), the MoaA-like domain (IPR040064), the MoaA "twitch" domain (IPR010505), membership in the MoCo_biosynth MoaA/MoaC family (IPR050105), and a TIM-barrel–like (aldolase-type) partial β-barrel core (IPR013785). The MoaA reaction is one of the most conserved in all of biology: acting together with MoaC, MoaA initiates Moco biosynthesis by converting 5′-GTP into cyclic pyranopterin monophosphate (cPMP, "precursor Z"), the first committed intermediate of the pathway.

The biochemical identity of this first step is well established in the literature. Reviews of *E. coli* Moco biosynthesis state that "the starting point is the formation of the cyclic pyranopterin monophosphate (cPMP) from 5′-GTP" [PMID: 32239579](https://pubmed.ncbi.nlm.nih.gov/32239579/). Mechanistic studies specify that MoaA (and its human ortholog MOCS1A) mediates "the conversion of guanosine 5′-triphosphate (GTP) into cyclic pyranopterin monophosphate" [PMID: 25697423](https://pubmed.ncbi.nlm.nih.gov/25697423/), and the *E. coli* molybdoenzyme maturation review confirms "formation of the cyclic pyranopterin monophosphate" as step one [PMID: 23201473](https://pubmed.ncbi.nlm.nih.gov/23201473/). The alignment of Q88K11's domain architecture with this precisely defined reaction is the foundation of the annotation.

### Finding 2 — Catalytic mechanism: two [4Fe-4S] clusters, a SAM-derived 5′-deoxyadenosyl radical, and a C-terminal GG-motif gate

MoaA is a founding radical SAM enzyme and is bifunctional in its metal-cluster architecture. An **N-terminal [4Fe-4S] cluster (cluster I)**, coordinated by the canonical CX₃CX₂C cysteine triad, reductively cleaves SAM to generate a transient 5′-deoxyadenosyl radical. A **second C-terminal [4Fe-4S] cluster (cluster II)**, housed in the "twitch" domain, binds the GTP substrate. Electron-nuclear double resonance (ENDOR) spectroscopy demonstrated that the guanine **N1** nitrogen of GTP directly coordinates the unique iron of cluster II—"only one nitrogen nucleus is bound to the cluster" [PMID: 19566093](https://pubmed.ncbi.nlm.nih.gov/19566093/)—with the guanine O6 forming a hydrogen bond to a cluster sulfide. This binding mode positions C3′ of the ribose and C8 of the guanine for the subsequent cyclization that forms a new carbon–carbon bond.

Radical initiation is gated by a conserved **C-terminal di-glycine (GG) motif**. Biochemical dissection showed that "the C-terminal tail containing the GG motif interacts with the SAM-binding pocket of MoaA, and is essential for the binding of SAM and subsequent radical initiation" [PMID: 25697423](https://pubmed.ncbi.nlm.nih.gov/25697423/), and that "the GG motif is essential for the activity of MoaA to produce 3′,8-cH₂GTP from GTP" [PMID: 25697423](https://pubmed.ncbi.nlm.nih.gov/25697423/). The overall chemistry rests on the defining radical SAM feature: "reductive cleavage of SAM using an oxygen sensitive 4Fe-4S cluster to transiently generate 5′-deoxyadenosyl radical" [PMID: 29072833](https://pubmed.ncbi.nlm.nih.gov/29072833/). The oxygen sensitivity of the clusters explains why this cytoplasmic reaction is optimally supported under low-oxygen conditions and why MoaA is technically demanding to study in vitro.

### Finding 3 — Cytoplasmic MoaA feeds the four-step Moco pathway that activates molybdoenzymes

Moco biosynthesis is an ancient, ubiquitous, and highly conserved **cytoplasmic** pathway comprising four steps: (1) formation of cPMP from GTP (MoaA + MoaC); (2) sulfur insertion converting cPMP to molybdopterin (MPT), catalyzed by the MoaD/MoaE synthase with MoaB accessory function; (3) molybdenum insertion by MogA/MoeA to form mature Moco; and (4) optional attachment of a nucleotide (GMP or CMP) to yield dinucleotide cofactor variants (bis-Mo-MPT, MGD, MCD). Reviews confirm "the biosynthesis of Moco can be divided into four steps" [PMID: 32239579](https://pubmed.ncbi.nlm.nih.gov/32239579/) with MoaA's reaction as step one.

The product cofactor is inserted into a large downstream enzyme set: "More than 50 molybdoenzymes were identified in bacteria to date" [PMID: 23201473](https://pubmed.ncbi.nlm.nih.gov/23201473/), including nitrate reductase, DMSO reductase, formate dehydrogenase, and xanthine dehydrogenase—enzymes that catalyze oxygen-atom-transfer redox reactions central to anaerobic respiration and carbon/nitrogen metabolism. Critically, MoaA sits at the non-redundant head of this pathway: "A defect in any of the steps of Moco biosynthesis results in the pleiotropic loss of all Mo enzyme activities" [PMID: 16261263](https://pubmed.ncbi.nlm.nih.gov/16261263/). In *P. putida* KT2440, MoaA (PP_2482) therefore provides the committed entry point supplying Moco to the organism's entire molybdoenzyme complement.

### Finding 4 — The Q88K11 sequence directly confirms both radical SAM signatures

Direct inspection of the 322-residue Q88K11 protein sequence confirms both metal-cluster signatures rather than relying on annotation alone. The canonical radical SAM [4Fe-4S]-binding motif **CX₃CX₂C** is present at residues 21–28 (C21-NYA-C25-TY-C28). The protein matches **Pfam PF04055 (Radical_SAM)**, with the radical SAM core spanning approximately residues 5–217, and matches **Pfam PF06463 (MoaA C-terminal / Mob_synth_C "twitch" domain)**, which supplies the second [4Fe-4S] cluster via three conserved C-terminal cysteines. Finally, the protein terminates in **…SALIMKSVGG**, placing the conserved C-terminal di-glycine (GG) gate at positions 321–322. Database cross-references (KEGG ppu:PP_2482; BioCyc PPUT160488:G1G01-2657-MONOMER) are consistent.

These sequence features map one-to-one onto the mechanistically characterized elements of MoaA. The terminal …VGG matches "the GG motif [that] is essential for the activity of MoaA to produce 3′,8-cH₂GTP from GTP" [PMID: 25697423](https://pubmed.ncbi.nlm.nih.gov/25697423/), and the CX₃CX₂C triad at residues 21–28 is the cysteine cluster that "generate[s] [the] 5′-deoxyadenosyl radical" via reductive SAM cleavage [PMID: 29072833](https://pubmed.ncbi.nlm.nih.gov/29072833/). The presence of both signatures in the actual Q88K11 sequence upgrades the functional assignment from database inference to sequence-level evidence.

### Finding 5 — KEGG assigns PP_2482 to GTP 3′,8-cyclase in a molybdoenzyme-associated neighborhood

KEGG maps ppu:PP_2482 to orthology **K03639 = "GTP 3′,8-cyclase [EC:4.1.99.22]"**, pathway ppu00790 (folate/pterin biosynthesis), and module **M00880 "Molybdenum cofactor biosynthesis, GTP ⇒ molybdenum cofactor."** The gene occupies genomic coordinates 2,829,397–2,830,365 (969 bp; 322 aa). Its immediate neighbors reinforce the functional context: PP_2481 (adjacent, same strand) and PP_2480 (a putative xanthine dehydrogenase accessory factor—i.e., a molybdoenzyme maturation function), with an ArsR-family regulator (PP_2484) nearby. The physical co-localization of MoaA with a molybdoenzyme accessory gene is consistent with coordinated Moco-biosynthesis / molybdoenzyme functional organization.

The KEGG EC/KO assignment corresponds exactly to the characterized reaction: EC 4.1.99.22 / K03639 (GTP 3′,8-cyclase) matches "the conversion of guanosine 5′-triphosphate (GTP) into cyclic pyranopterin monophosphate" [PMID: 25697423](https://pubmed.ncbi.nlm.nih.gov/25697423/), and module M00880's "GTP ⇒ cPMP" step matches "the starting point is the formation of the cyclic pyranopterin monophosphate (cPMP) from 5′-GTP" [PMID: 32239579](https://pubmed.ncbi.nlm.nih.gov/32239579/).

---

## Mechanistic Model and Interpretation

### The reaction MoaA catalyzes

MoaA performs the chemically remarkable first half of the GTP → cPMP conversion. In modern nomenclature, MoaA is the GTP 3′,8-cyclase that produces **3′,8-cyclo-7,8-dihydro-GTP (3′,8-cH₂GTP)**; MoaC then rearranges this intermediate into cyclic pyranopterin monophosphate (cPMP). The MoaA step forms a new **C3′–C8 carbon–carbon bond**, an unusual transformation that required decades to resolve and is a signature achievement of radical SAM chemistry.

```
   MoaA (PP_2482)                          MoaC
   radical SAM                             (partner)
   GTP 3',8-cyclase                        isomerase/
                                           cyclase
        │                                      │
        ▼                                      ▼
  5'-GTP ──────────► 3',8-cH2GTP ──────────► cPMP (precursor Z)
        │                                      │
   SAM → 5'-dAdo•                         [step 1 complete]
   (cluster I)                                 │
   guanine N1 → cluster II                     ▼
                                     MPT ─► Moco ─► (MGD/MCD variants)
                                    (steps 2-4)
                                              │
                                              ▼
                                   >50 molybdoenzymes activated
                              (nitrate reductase, DMSO reductase,
                               formate dehydrogenase, xanthine DH...)
```

### The two-cluster architecture

MoaA is unusual even among radical SAM enzymes in requiring **two** distinct [4Fe-4S] clusters:

| Feature | Cluster I (N-terminal) | Cluster II (C-terminal / "twitch") |
|---|---|---|
| Ligating motif | CX₃CX₂C (residues 21–28 in Q88K11) | 3 conserved Cys in PF06463 twitch domain |
| Role | Reductive cleavage of SAM → 5′-deoxyadenosyl radical | Binds GTP substrate |
| Substrate contact | SAM (via GG-gated pocket) | Guanine N1 → unique Fe; O6···sulfide H-bond |
| Evidence | Sequence motif + PMID: 29072833 | ENDOR spectroscopy, PMID: 19566093 |

The **C-terminal GG motif** (…SVGG in Q88K11) acts as a conformational gate: it docks into the SAM-binding pocket and is required for productive SAM binding and radical initiation. Mutation of this motif abolishes activity in characterized MoaA orthologs and, in the human ortholog MOCS1A, causes molybdenum cofactor deficiency (a severe, often lethal inborn error of metabolism) [PMID: 25697423](https://pubmed.ncbi.nlm.nih.gov/25697423/). This human-disease link underscores how tightly the mechanism is conserved from bacteria to humans.

### Localization

Moco biosynthesis is a **cytoplasmic** process; MoaA operates in the cytosol, where GTP, SAM, and the reducing systems needed to regenerate its clusters are available. There is no signal peptide or transmembrane region expected for this soluble enzyme. The oxygen sensitivity of its [4Fe-4S] clusters means the reaction is favored under microaerobic/anaerobic conditions—consistent with the physiological demand for molybdoenzymes (e.g., nitrate/DMSO respiration) under low oxygen.

### Pathway context and physiological role in *P. putida*

*P. putida* KT2440 is a metabolically versatile, biotechnologically important soil bacterium. Its molybdoenzymes (nitrate reductase, formate dehydrogenase, xanthine/purine-degrading dehydrogenases, and others) depend entirely on a functional Moco supply. Because "a defect in any of the steps of Moco biosynthesis results in the pleiotropic loss of all Mo enzyme activities" [PMID: 16261263](https://pubmed.ncbi.nlm.nih.gov/16261263/), MoaA (PP_2482) is a single-point, non-redundant gatekeeper: without it, none of these molybdoenzymes can be matured. The gene's location beside a xanthine dehydrogenase accessory factor (PP_2480) reflects this functional coupling between cofactor supply and cofactor use.

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports the findings |
|---|---|---|
| [PMID: 25697423](https://pubmed.ncbi.nlm.nih.gov/25697423/) | *C-Terminal glycine-gated radical initiation by GTP 3′,8-cyclase…* | Defines the GTP→cPMP reaction; establishes the essential C-terminal GG gate and SAM-dependent radical initiation (F1, F2, F4, F5) |
| [PMID: 19566093](https://pubmed.ncbi.nlm.nih.gov/19566093/) | *ENDOR spectroscopy shows guanine N1 binds [4Fe-4S] cluster II of MoaA* | Direct spectroscopic evidence for GTP coordination to cluster II via guanine N1 (F2) |
| [PMID: 29072833](https://pubmed.ncbi.nlm.nih.gov/29072833/) | *Radical Breakthroughs in Natural Product and Cofactor Biosynthesis* | Describes the radical SAM mechanism—oxygen-sensitive [4Fe-4S] cluster generating 5′-dAdo radical (F2, F4) |
| [PMID: 32239579](https://pubmed.ncbi.nlm.nih.gov/32239579/) | *The biosynthesis of the molybdenum cofactors in E. coli* | cPMP formation from 5′-GTP as step 1; four-step pathway structure (F1, F3, F5) |
| [PMID: 23201473](https://pubmed.ncbi.nlm.nih.gov/23201473/) | *Molybdenum enzymes, their maturation and Moco biosynthesis in E. coli* | Confirms cPMP formation as step 1; >50 bacterial molybdoenzymes depend on Moco (F1, F3) |
| [PMID: 16261263](https://pubmed.ncbi.nlm.nih.gov/16261263/) | *Molybdenum cofactor biosynthesis and deficiency* | Defect in any Moco step → pleiotropic loss of all Mo-enzyme activity, placing MoaA upstream and essential (F3) |
| [PMID: 35480226](https://pubmed.ncbi.nlm.nih.gov/35480226/) | *Resolving the Multidecade-Long Mystery in MoaA Radical SAM Enzyme…* | Reviews the mechanistic resolution of MoaA chemistry and its health relevance (supporting context) |
| [PMID: 30097104](https://pubmed.ncbi.nlm.nih.gov/30097104/) | *Lessons From the Studies of a CC Bond Forming Radical SAM Enzyme…* | MoaA as a founding radical SAM enzyme forming a C–C bond (supporting context) |
| [PMID: 22684071](https://pubmed.ncbi.nlm.nih.gov/22684071/) | *…MoaC2 from M. tuberculosis* | Confirms MoaA + MoaC jointly convert GTP → precursor Z, the first step (partner-enzyme context) |
| [PMID: 23539623](https://pubmed.ncbi.nlm.nih.gov/23539623/) | *The molybdenum cofactor* | Four-step, six-protein pathway; Moco deficiency is lethal (pathway context) |
| [PMID: 16669776](https://pubmed.ncbi.nlm.nih.gov/16669776/) | *Molybdenum cofactor biosynthesis and molybdenum enzymes* | Ancient conserved pathway; Moco synthesized from GTP via cPMP, MPT, adenylated MPT (pathway context) |

**Consistency of the evidence:** All lines of evidence converge. No paper in the reviewed literature contradicts the MoaA / GTP 3′,8-cyclase assignment. The mechanistic studies (PMIDs 25697423, 19566093, 29072833) are precise, low-throughput biochemical/spectroscopic investigations—exactly the type of evidence prioritized by the research brief—performed on MoaA orthologs whose active-site residues and domain architecture are shared by Q88K11.

---

## Limitations and Knowledge Gaps

1. **No direct experimental study of the *P. putida* ortholog.** All functional claims for PP_2482 specifically are made by inference. The mechanistic and structural data derive from MoaA orthologs (chiefly *Staphylococcus aureus*, *E. coli*, and human MOCS1A). While MoaA is one of the most conserved enzymes known—reducing the risk of divergence—the *P. putida* protein has not itself been purified, assayed, crystallized, or genetically knocked out in a published study identified here.

2. **Sequence-motif inference for cluster II cysteines.** The N-terminal CX₃CX₂C motif and the C-terminal GG gate were confirmed at defined positions in Q88K11. The precise identities and spacing of the three twitch-domain cysteines ligating cluster II were inferred from Pfam PF06463 membership rather than mapped residue-by-residue in this investigation; explicit alignment to characterized orthologs would strengthen this.

3. **Downstream molybdoenzyme repertoire of KT2440 not enumerated.** The report asserts MoaA feeds the organism's molybdoenzymes but does not provide a validated inventory of which specific molybdoenzymes are encoded and expressed in *P. putida* KT2440, nor their physiological conditions of use.

4. **Product nomenclature nuance.** Historically, MoaA + MoaC together were said to make "precursor Z"/cPMP. Modern work partitions the chemistry so that MoaA alone produces 3′,8-cH₂GTP and MoaC completes cPMP formation. Some cited abstracts use the older combined description; this report reflects the modern partitioning but readers should be aware of the terminology evolution.

5. **Regulation and expression are uncharacterized here.** The nearby ArsR-family regulator (PP_2484) and operon structure were noted but not experimentally connected to *moaA* expression control in KT2440.

---

## Proposed Follow-up Experiments and Actions

1. **Direct enzymatic confirmation.** Heterologously express and purify Q88K11 (anaerobically, with iron–sulfur cluster reconstitution) and assay GTP 3′,8-cyclase activity in vitro—monitoring conversion of GTP to 3′,8-cH₂GTP (and, with MoaC, to cPMP) by LC-MS. This would upgrade the assignment from inference to direct evidence.

2. **Genetic complementation / knockout.** Delete PP_2482 in *P. putida* KT2440 and test for the predicted pleiotropic loss of molybdoenzyme activities (e.g., nitrate reductase, formate dehydrogenase); complement with the wild-type gene and with a GG-motif mutant to confirm the gate's essentiality in this organism.

3. **Residue-level cluster mapping.** Perform a multiple sequence alignment of Q88K11 against biochemically characterized MoaA orthologs to explicitly identify the cluster II cysteines and the substrate-binding residues, and/or generate an AlphaFold model to inspect the two-cluster architecture and GG-gate geometry.

4. **Molybdoenzyme inventory.** Bioinformatically enumerate and, ideally, transcriptomically profile the molybdoenzymes of KT2440 to define the physiological demand MoaA serves, and correlate *moaA* expression with anaerobic/microaerobic growth conditions.

5. **Operon and regulation analysis.** Determine the transcriptional unit containing PP_2482 (RNA-seq / promoter mapping) and test whether the adjacent ArsR-family regulator (PP_2484) or Moco/molybdate availability modulates its expression.

---

## Conclusion

PP_2482 (Q88K11) of *Pseudomonas putida* KT2440 is **MoaA, a cytoplasmic radical SAM GTP 3′,8-cyclase (EC 4.1.99.22)** that catalyzes the first committed step of molybdenum cofactor biosynthesis. Using two [4Fe-4S] clusters—an N-terminal CX₃CX₂C cluster that cleaves SAM to a 5′-deoxyadenosyl radical and a C-terminal twitch-domain cluster that binds GTP via guanine N1—and a C-terminal GG gate that controls radical initiation, it converts 5′-GTP into 3′,8-cyclo-7,8-dihydro-GTP, forming a new C3′–C8 carbon–carbon bond. Partner enzyme MoaC then completes cyclic pyranopterin monophosphate, launching the conserved four-step pathway that matures Moco for the organism's molybdoenzymes. The assignment is supported at the sequence, domain, database-orthology, genomic-context, and mechanistic-literature levels, with the principal limitation being that the *P. putida* ortholog itself has not yet been directly characterized experimentally.


## Artifacts

- [OpenScientist final report](PP_2482-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PP_2482-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:32239579
2. PMID:25697423
3. PMID:23201473
4. PMID:19566093
5. PMID:29072833
6. PMID:16261263
7. PMID:35480226
8. PMID:30097104
9. PMID:22684071
10. PMID:23539623
11. PMID:16669776