---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-20T16:15:47.303439'
end_time: '2026-07-20T16:25:28.490789'
duration_seconds: 581.19
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_1969
  gene_symbol: PP_1969
  uniprot_accession: Q88LG4
  protein_description: 'SubName: Full=Molybdenum cofactor biosynthesis protein A {ECO:0000313|EMBL:AAN67584.1};'
  gene_info: OrderedLocusNames=PP_1969 {ECO:0000313|EMBL:AAN67584.1};
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
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PP_1969-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PP_1969-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88LG4
- **Protein Description:** SubName: Full=Molybdenum cofactor biosynthesis protein A {ECO:0000313|EMBL:AAN67584.1};
- **Gene Information:** OrderedLocusNames=PP_1969 {ECO:0000313|EMBL:AAN67584.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** Aldolase_TIM. (IPR013785); Elp3/MiaA/NifB-like_rSAM. (IPR006638); MoaA-like. (IPR040064); MoaA_twitch. (IPR010505); MoCo_biosynth_MoaA/MoaC. (IPR050105)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_1969" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_1969' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_1969** (gene ID: PP_1969, UniProt: Q88LG4) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of PP_1969 (MoaA) in *Pseudomonas putida* KT2440

**Gene:** PP_1969 (OrderedLocusName) · **UniProt:** Q88LG4 · **Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / NCIMB 11950 / **KT2440**), NCBI TaxID PSEPK

---

## 1. Summary (answer to the research question)

PP_1969 encodes **MoaA**, a cytoplasmic **radical S‑adenosyl‑L‑methionine (radical SAM) metalloenzyme** that catalyzes the **first committed step of molybdenum cofactor (Moco) biosynthesis**. Its primary function is that of a **GTP 3′,8‑cyclase (EC 4.1.99.22)**: it converts **guanosine‑5′‑triphosphate (5′‑GTP)** into the cyclic intermediate **3′,8‑cyclo‑7,8‑dihydro‑GTP (3′,8‑cH₂GTP)**, which the partner enzyme MoaC then converts into **cyclic pyranopterin monophosphate (cPMP, "precursor Z")**. The enzyme carries **two [4Fe‑4S] clusters** — an N‑terminal radical‑SAM cluster that reductively cleaves SAM to generate a 5′‑deoxyadenosyl radical, and a MoaA‑unique C‑terminal ("twitch") cluster that binds and activates the GTP substrate. MoaA acts in the **cytoplasm**, feeding the pterin scaffold that is ultimately matured into the molybdenum cofactor required by all of the cell's molybdoenzymes (e.g., nitrate reductase, sulfite oxidase, xanthine/aldehyde oxidoreductases, DMSO/TMAO reductases).

Identity is unambiguous: the protein's domain set (radical SAM, MoaA‑like, MoaA_twitch, TIM‑barrel), its sequence motifs, and its KEGG orthology (K03639) all define a canonical MoaA. **The gene symbol is NOT ambiguous** for this entry.

---

## 2. Gene/Protein identity verification

| Criterion | Finding |
|---|---|
| Symbol vs. description | "Molybdenum cofactor biosynthesis protein A" ⇒ *moaA*; consistent. |
| Organism | *P. putida* KT2440 (PSEPK); confirmed via UniProt/KEGG (`ppu:PP_1969`). |
| Domains/family | Radical SAM core (IPR006638), MoaA‑like (IPR040064), MoaA_twitch (IPR010505), MoCo_biosynth_MoaA/MoaC (IPR050105), TIM‑barrel (IPR013785) — the exact diagnostic set of the MoaA family. |
| Literature match | Extensive primary literature on MoaA (bacterial) / MOCS1A (human ortholog) aligns precisely with the domains and reaction. |

**Sequence-level confirmation (Q88LG4, 337 aa, 36.7 kDa; this work, UniProt):**
- N‑terminal radical‑SAM **CX₃CX₂C** motif: **C36**‑N‑Y‑A‑**C40**‑T‑Y‑**C43**.
- C‑terminal "twitch"‑domain cluster cysteines: **Cys268, Cys271, Cys285** (C‑R‑T‑C…W‑L‑H‑G‑C) — a three‑Cys ligation leaving a unique, substrate‑binding Fe.
- Conserved C‑terminal **di‑glycine (GG) motif**: the protein ends in **…KVIGG**.
- UniProt keywords: 4Fe‑4S, GTP‑binding, Iron‑sulfur, S‑adenosyl‑L‑methionine, Molybdenum cofactor biosynthesis, Lyase. **No signal peptide or transmembrane segment.**

All of these are hallmark, functionally essential features of MoaA, so the identification is secure both by homology/domain analysis and by direct motif inspection.

---

## 3. Primary function: the reaction catalyzed and substrate specificity

**Reaction (step 1 of Moco biosynthesis):**

> 5′‑GTP + SAM + 2e⁻ → 3′,8‑cyclo‑7,8‑dihydro‑GTP (3′,8‑cH₂GTP) + 5′‑deoxyadenosine + L‑methionine
> (MoaC subsequently: 3′,8‑cH₂GTP → cyclic pyranopterin monophosphate, cPMP / precursor Z)

- **The substrate is intact 5′‑GTP**, bound with high affinity; nucleotide‑specificity determinants were mapped biochemically and structurally [Hänzelmann & Schindelin 2006, PMID 16632608; 2004, PMID 15317939].
- The reaction is a **radical‑initiated intramolecular rearrangement** that inserts the **guanine C8 carbon** into the new pyranopterin ring — a chemically demanding C–C bond formation characteristic of radical SAM chemistry [Pang & Yokoyama 2018, PMID 30097104; Yokoyama 2017, PMID 29072833].
- The classical description of "MoaA + MoaC convert GTP → precursor Z" was refined by Yokoyama and colleagues, who showed **MoaA alone acts as a GTP 3′,8‑cyclase producing 3′,8‑cH₂GTP**, with MoaC completing cPMP formation [Hover et al. 2015, PMID 25697423; review Yokoyama, Li & Pang 2022, PMID 35480226].

**EC number:** 4.1.99.22 (GTP 3′,8‑cyclase). UniProt classifies molecular function as **Lyase**, consistent with C–C bond formation/cyclization.

---

## 4. Cofactors and catalytic mechanism (structural evidence)

MoaA is a **homodimer**; each subunit is built on an **incomplete (β/α) TIM‑barrel** and carries **two [4Fe‑4S] clusters ~17 Å apart** flanking a large active‑site pocket [Hänzelmann & Schindelin 2004, PMID 15317939]:

1. **N‑terminal radical‑SAM cluster** (CX₃CX₂C = Cys36/40/43): SAM chelates the unique Fe as an N/O chelate and is **reductively cleaved to give L‑methionine and a 5′‑deoxyadenosyl radical (5′‑dA•)** [PMID 15317939; PMID 16632608].
2. **C‑terminal MoaA‑unique "twitch" cluster** (Cys268/271/285): its **non‑cysteinyl‑ligated unique Fe binds the substrate**. The crystal structure with 5′‑GTP and ENDOR spectroscopy showed the **guanine N1 nitrogen coordinates this Fe**, positioning the substrate and preventing escape of radical intermediates via a tightly anchored triphosphate [Hänzelmann & Schindelin 2006, PMID 16632608; Lees et al. 2009, PMID 19566093].
3. The **conserved C‑terminal GG motif** (…KVIGG in PP_1969) folds into the SAM‑binding pocket and is **essential for SAM binding and radical initiation**; its mutation abolishes activity and, in the human ortholog MOCS1A, causes Moco deficiency [Hover et al. 2015, PMID 25697423].

The mechanism and residues are strongly conserved between bacterial MoaA and the human ortholog **MOCS1A** — indeed **>50 % of human Moco‑deficiency (MoCD) patients carry MOCS1A mutations**, underscoring the reaction's conservation and importance [Hover et al. 2015, PMID 25697423; Hänzelmann & Schindelin 2004, PMID 15317939].

---

## 5. Localization

MoaA carries out its function in the **bacterial cytoplasm**:
- It has **no signal peptide and no transmembrane segments** (Q88LG4 keywords/features) and the prototype is a soluble homodimer purified/crystallized from cell lysate [PMID 15317939].
- Its two **oxygen‑labile [4Fe‑4S] clusters** and the **oxygen‑sensitive tetrahydropyranopterin product** require the **reducing cytoplasmic environment**; the Moco biosynthesis network relies on **protected metabolic channelling** of these oxygen‑sensitive intermediates between enzymes [Hänzelmann & Schindelin 2006, PMID 16632608; Kaufholdt et al. 2017, PMID 29184564].

---

## 6. Pathway context in *P. putida* KT2440

Moco biosynthesis is a **conserved four‑step bacterial pathway** [Mendel & Leimkühler 2015, PMID 24980677]:

1. **GTP → cPMP** — **MoaA (PP_1969)** [step 1a, this enzyme] → **MoaC** [step 1b];
2. **cPMP → molybdopterin (MPT)** — MPT synthase **MoaD/MoaE** (+ activating enzyme MoeB);
3. **Mo insertion into MPT → Moco** — **MogA/MoeA**;
4. **(bacteria)** nucleotide addition to form the dinucleotide (MGD) variant — **MobA**.

In *P. putida* KT2440, KEGG mapping (this work) places the downstream partners in a **separate genomic cluster** — **moaC = PP_1292, moaD = PP_1293, moaB = PP_1294**, with **moeA = PP_2123** and **mogA = PP_3457** — whereas **PP_1969 is not in a classical *moaABCDE* operon** (its neighbors are an unrelated DNA‑pol‑III subunit PP_1966, tRNA D‑aminoacylase PP_1967, a TetR‑family regulator PP_1968, and a lipoprotein PP_1970). The GTP‑3′,8‑cyclase orthology group (KO **K03639**) additionally contains **three** *P. putida* loci — **PP_1969, PP_2482, PP_4597** — indicating MoaA‑family/radical‑SAM paralogs; PP_1969 is the reference‑annotated *moaA*.

**Physiological purpose:** the Moco produced downstream is the catalytic cofactor of the cell's **molybdoenzymes** (nitrate reductases, sulfite oxidase, xanthine/aldehyde oxidoreductases, DMSO/TMAO reductases, etc.), which are central to redox and anaerobic/assimilatory metabolism [Mendel & Leimkühler 2015, PMID 24980677; Schwarz, Mendel & Ribbe 2009, PMID 19675644]. MoaA thus sits at the **entry point** of this essential cofactor supply line.

---

## 7. Supported and refuted hypotheses

**Supported:**
- H1 — *PP_1969 is a MoaA ortholog (GTP 3′,8‑cyclase), not a metabolic aldolase despite the TIM‑barrel annotation.* Supported by domain set, KEGG K03639, and all catalytic motifs.
- H2 — *It is a radical‑SAM enzyme with two [4Fe‑4S] clusters.* Supported by CX₃CX₂C + three‑Cys twitch motifs and UniProt Fe‑S/SAM keywords, mirroring the crystallographically characterized prototype.
- H3 — *Its substrate is 5′‑GTP and its product is 3′,8‑cH₂GTP (→ cPMP with MoaC).* Supported by biochemical/structural literature.
- H4 — *It functions in the cytoplasm.* Supported by absence of signal/TM features and O₂‑sensitivity of clusters and product.

**Refuted / set aside:**
- The literal "Aldolase_TIM" (IPR013785) annotation as a *functional* aldolase is misleading — the TIM‑barrel is a structural scaffold, not evidence of aldolase activity.
- The older idea that MoaA+MoaC jointly synthesize precursor Z in one indivisible step is superseded: MoaA alone is a GTP 3′,8‑cyclase (product 3′,8‑cH₂GTP).

---

## 8. Evidence quality and limitations

- **Direct experimental evidence** (crystallography, ENDOR/EPR spectroscopy, in‑vitro reconstitution, mutagenesis) exists for the **MoaA family prototype** (from *Staphylococcus aureus*/*E. coli* systems) and the human ortholog MOCS1A — not specifically for the *P. putida* PP_1969 protein. Given the very high conservation of sequence, domains, and the essential motifs verified here, transfer of function to PP_1969 is well justified (inference from homology/structure), but a *P. putida*‑specific biochemical study was not identified.
- The three K03639 paralogs (PP_1969/2482/4597) raise the possibility of functional redundancy or specialization; distinguishing their individual roles would require targeted knockouts/complementation, not available here.
- No experimental subcellular‑localization study specific to PP_1969 was found; cytoplasmic assignment is a well‑supported inference.

## 9. Future directions

- In‑vitro reconstitution of PP_1969 to confirm GTP 3′,8‑cyclase activity and kinetics.
- Genetic dissection of the three *P. putida* K03639 paralogs (single/multiple deletions; Moco‑dependent phenotypes such as nitrate reductase activity).
- Test whether PP_1969 physically channels its product to MoaC (PP_1292) despite genomic separation.

---

### Key references
- Hänzelmann P, Schindelin H. *PNAS* 2004 (PMID **15317939**) — MoaA crystal structure; identification of 5′‑GTP as substrate; two [4Fe‑4S] clusters; MoCD relevance.
- Hänzelmann P, Schindelin H. *PNAS* 2006 (PMID **16632608**) — MoaA·5′‑GTP structure; N‑terminal cluster cleaves SAM → 5′‑dA•; C‑terminal cluster binds substrate.
- Lees NS, Hänzelmann P, … Hoffman BM. 2009 (PMID **19566093**) — ENDOR: guanine N1 binds cluster II.
- Hover BM, … Yokoyama K. *JACS* 2015 (PMID **25697423**) — MoaA = GTP 3′,8‑cyclase producing 3′,8‑cH₂GTP; essential C‑terminal GG motif; MOCS1A/MoCD link.
- Pang H, Yokoyama K. 2018 (PMID **30097104**); Yokoyama K, Li & Pang 2022 (PMID **35480226**); Yokoyama K 2017 (PMID **29072833**) — mechanism reviews.
- Mendel RR, Leimkühler S. 2015 (PMID **24980677**); Schwarz, Mendel & Ribbe 2009 (PMID **19675644**); Kaufholdt et al. 2017 (PMID **29184564**) — Moco pathway/network reviews.


## Artifacts

- [OpenScientist final report](PP_1969-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PP_1969-deep-research-openscientist_artifacts/final_report.pdf)