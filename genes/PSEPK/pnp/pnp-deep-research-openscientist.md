---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T19:33:23.401733'
end_time: '2026-08-31T19:43:57.102936'
duration_seconds: 633.7
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: pnp
  gene_symbol: pnp
  uniprot_accession: Q88DW0
  protein_description: 'RecName: Full=Polyribonucleotide nucleotidyltransferase {ECO:0000255|HAMAP-Rule:MF_01595};
    EC=2.7.7.8 {ECO:0000255|HAMAP-Rule:MF_01595}; AltName: Full=Polynucleotide phosphorylase
    {ECO:0000255|HAMAP-Rule:MF_01595}; Short=PNPase {ECO:0000255|HAMAP-Rule:MF_01595};'
  gene_info: Name=pnp {ECO:0000255|HAMAP-Rule:MF_01595}; OrderedLocusNames=PP_4708;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the polyribonucleotide nucleotidyltransferase
  protein_domains: ExoRNase_PH_dom1. (IPR001247); ExoRNase_PH_dom2. (IPR015847); ExoRNase_PH_dom2_sf.
    (IPR036345); KH_dom. (IPR004087); KH_dom_type_1. (IPR004088)
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
citation_count: 17
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: pnp-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: pnp-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88DW0
- **Protein Description:** RecName: Full=Polyribonucleotide nucleotidyltransferase {ECO:0000255|HAMAP-Rule:MF_01595}; EC=2.7.7.8 {ECO:0000255|HAMAP-Rule:MF_01595}; AltName: Full=Polynucleotide phosphorylase {ECO:0000255|HAMAP-Rule:MF_01595}; Short=PNPase {ECO:0000255|HAMAP-Rule:MF_01595};
- **Gene Information:** Name=pnp {ECO:0000255|HAMAP-Rule:MF_01595}; OrderedLocusNames=PP_4708;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the polyribonucleotide nucleotidyltransferase
- **Key Domains:** ExoRNase_PH_dom1. (IPR001247); ExoRNase_PH_dom2. (IPR015847); ExoRNase_PH_dom2_sf. (IPR036345); KH_dom. (IPR004087); KH_dom_type_1. (IPR004088)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "pnp" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'pnp' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **pnp** (gene ID: pnp, UniProt: Q88DW0) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: Polynucleotide Phosphorylase (PNPase) — *pnp* / PP_4708 (UniProt Q88DW0) in *Pseudomonas putida* KT2440

---

## Summary

The *pnp* gene (ordered locus **PP_4708**, UniProt **Q88DW0**) of *Pseudomonas putida* strain KT2440 encodes **polynucleotide phosphorylase (PNPase; polyribonucleotide nucleotidyltransferase; EC 2.7.7.8)**, a highly conserved bacterial RNA-metabolizing enzyme. Its primary molecular function is that of a **processive 3'→5' phosphorolytic exoribonuclease**: it degrades single-stranded RNA in the 3'-to-5' direction using inorganic phosphate as the attacking nucleophile, releasing **nucleoside 5'-diphosphates (NDPs)** rather than nucleoside monophosphates. Because the phosphorolysis reaction is thermodynamically reversible, PNPase can also run in the synthetic direction, using NDPs to add template-independent 3' heteropolymeric tails to RNA — a property that links it to RNA turnover control. This dual identity — a single, well-defined catalytic activity that operates in two directions — is the core of its biological role.

Structurally, PNPase is a **homotrimeric, ring-shaped enzyme**. Each protomer contributes two RNase PH–like domains (IPR001247 and IPR015847) that assemble into a central channel housing three phosphorolytic active sites, while C-terminal **KH (IPR004087/IPR004088) and S1 RNA-binding domains** decorate one face of the ring and thread the single-stranded 3' end of substrate RNA into the catalytic channel. This architecture — validated by crystal structures of the orthologous *Caulobacter crescentus* enzyme — matches exactly the domain composition annotated for Q88DW0, giving high confidence that the *P. putida* protein adopts the same fold and mechanism. Functionally, PNPase operates in the **cytoplasm**, principally as a subunit of the **RNA degradosome**, a multiprotein machine nucleated on the C-terminal scaffold of the endoribonuclease RNase E together with the RhlB DEAD-box helicase and the glycolytic enzyme enolase, and associated with the cytoplasmic membrane.

Beyond bulk mRNA decay, PNPase performs **RNA quality-control and regulatory functions**: it clears structured decay intermediates and defective ribosomal RNA fragments (a role redundant with the hydrolytic exoribonuclease RNase R, such that the two together are collectively essential), and — via its KH-S1 domains — it destabilizes the **regulatory small RNAs RsmY and RsmZ** of the Gac/Rsm signaling circuit, thereby tuning secretion systems and virulence in pseudomonads. Notably, direct study of *P. putida pnp* deletion mutants shows the gene is **non-essential** and, unlike in *Escherichia coli*, its loss does **not** produce cold sensitivity, and its transcriptional response to cold shock differs markedly from that of *E. coli* — evidence that while the enzyme's catalytic function is deeply conserved, its physiological deployment and regulation are species-specific.

---

## Key Findings

### Finding 1 — PNPase is a processive 3'→5' phosphorolytic exoribonuclease (EC 2.7.7.8)

The central, defining function of the *pnp* gene product is enzymatic RNA degradation. UniProt Q88DW0 assigns **EC 2.7.7.8** (polyribonucleotide nucleotidyltransferase / polynucleotide phosphorylase), and the biochemistry of this enzyme has been characterized in detail across bacteria. PNPase degrades single-stranded RNA in the **3'→5' direction by phosphorolysis** — that is, it uses inorganic phosphate (Pi), rather than water, as the nucleophile that attacks the terminal phosphodiester bond. The products are therefore **nucleoside 5'-diphosphates (NDPs)**, distinguishing PNPase from hydrolytic exoribonucleases (such as RNase R or RNase II) that release nucleoside 5'-monophosphates. The enzyme acts **processively**, translocating along the RNA and removing successive nucleotides without releasing the substrate.

A key consequence of the phosphorolytic mechanism is **reversibility**. When NDP concentrations are high relative to Pi, PNPase can catalyze the reverse (synthetic/polymerizing) reaction, adding nucleotides to the 3' end of an RNA in a **template-independent** manner. In vivo this manifests as the addition of **heteropolymeric 3' tails**, which serve as toeholds that mark transcripts for further degradation. Work in *Bacillus subtilis* demonstrated that, in the absence of poly(A) polymerase (PAP I), 3' tailing still occurs through the synthetic activity of PNPase — direct genetic evidence for the physiological relevance of the reverse reaction.

The domain architecture of Q88DW0 — two **ExoRNase_PH domains** (IPR001247, IPR015847) forming the catalytic core, plus **KH** (IPR004087) and S1 RNA-binding domains — is the textbook signature of this enzyme family and independently supports the catalytic assignment.

> **Evidence:** *"Polynucleotide phosphorylase (PNPase) is an exoribonuclease that cleaves single-stranded RNA substrates with 3'-5' directionality and processive behaviour."* — [PMID: 22724061](https://pubmed.ncbi.nlm.nih.gov/22724061/). *"the addition of 3' tails also occurs in the absence of PAP I via the synthetic activity of polynucleotide phosphorylase (PNPase)"* — [PMID: 15995184](https://pubmed.ncbi.nlm.nih.gov/15995184/).

### Finding 2 — A homotrimeric ring: the RNase PH core catalyzes, the KH/S1 domains channel the RNA 3' end

The three-dimensional organization of PNPase directly explains its processivity and single-strand specificity. Crystal structures of the orthologous *Caulobacter crescentus* PNPase (both apo and RNA-bound) reveal a **ring-like, trimeric architecture** in which the RNase PH–like domains create a **central channel** that houses the phosphorolytic active sites. One face of the ring is **decorated with the KH and S1 RNA-binding domains**. Upon RNA binding, the **three KH domains collectively close upon the RNA and direct its 3' end toward a constricted aperture** at the entrance of the central channel, feeding the single strand into the catalytic core. Structural non-equivalence (asymmetry) among the three catalytic sites has been proposed to act as a molecular ratchet that advances the substrate.

This fold is evolutionarily related to **RNase PH**, another phosphorolytic exoribonuclease: the RNase PH hexameric ring is structurally homologous to the PNPase core homotrimer, reinforcing the shared phosphorolytic mechanism. Because Q88DW0 carries exactly this domain set (two ExoRNase_PH domains + KH + S1), the *P. putida* enzyme is confidently modeled to adopt the same trimeric ring and substrate-channeling mechanism.

> **Evidence:** *"Its ring-like, trimeric architecture creates a central channel where phosphorolytic active sites reside. One face of the ring is decorated with RNA-binding K-homology (KH) and S1 domains"* and *"the three KH domains collectively close upon the RNA and direct the 3' end towards a constricted aperture at the entrance of the central channel"* — [PMID: 22724061](https://pubmed.ncbi.nlm.nih.gov/22724061/). *"This ring structure resembles that of the polynucleotide phosphorylase core domain homotrimer, another phosphorolytic exoribonuclease."* — [PMID: 12746447](https://pubmed.ncbi.nlm.nih.gov/12746447/).

### Finding 3 — PNPase is a core subunit of the membrane-associated cytoplasmic RNA degradosome

PNPase does not act alone in bulk mRNA decay; it is a stable component of the **RNA degradosome**, the principal RNA-degrading machine of proteobacteria. In *E. coli*, the **C-terminal half of RNase E** serves as an unstructured scaffold that binds the three other major degradosomal components: the 3' exoribonuclease **PNPase**, the DEAD-box RNA helicase **RhlB**, and the glycolytic enzyme **enolase**. This organization places PNPase's exonucleolytic activity downstream of RNase E's endonucleolytic cleavages, so that internal cuts generate 3' ends that PNPase then processively degrades, with RhlB unwinding secondary structure to feed structured substrates into the PNPase channel.

The degradosome is **spatially organized within the cell**: in vivo it associates with the **cytoplasmic membrane via the N-terminal region of RNase E**, and FRET/imaging experiments confirm that RNase E is held in close proximity to PNPase. Independent of the RNase E scaffold, PNPase and RhlB can also assemble into a ribonucleolytically active **α₃β₂ complex** capable of degrading double-stranded RNA — a degradosome-independent activity. Homologous PNPase–RNase E interactions are documented across proteobacteria (including *Caulobacter* and *Yersinia*), strongly implying that *P. putida* PNPase likewise operates in a degradosome context.

> **Evidence:** *"the carboxy-terminal half (CTH) of ribonuclease E (RNase E) contains the binding sites for the three other major degradosomal components, the DEAD-box RNA helicase RhlB, enolase, and polynucleotide phosphorylase (PNPase)"* — [PMID: 9732274](https://pubmed.ncbi.nlm.nih.gov/9732274/). *"degradosomes exist in vivo in E. coli as multicomponent structures that associate with the cytoplasmic membrane via the N-terminal region of RNase E"* — [PMID: 11134527](https://pubmed.ncbi.nlm.nih.gov/11134527/). *"Rh1B can physically bind to PNPase, both in vitro and in vivo"* — [PMID: 12181321](https://pubmed.ncbi.nlm.nih.gov/12181321/).

### Finding 4 — In *P. putida*, *pnp* is non-essential and, unlike *E. coli*, its deletion does not cause cold sensitivity

The most direct experimental evidence for the target gene itself comes from Favaro & Dehò (2003), who **identified the *pnp* gene of *Pseudomonas putida* and constructed deletion mutants**. Critically, these Δ*pnp* mutants **did not exhibit cold sensitivity** — a sharp contrast with *E. coli*, where PNPase is required for growth at low temperature and is a canonical cold-shock protein. Moreover, the **transcription pattern of *pnp* upon cold shock in *P. putida* was markedly different from that in *E. coli***, indicating that the regulatory circuitry governing *pnp* expression has diverged between the two species even though the enzyme's catalytic role is conserved.

For context, in *E. coli* *pnp* is subject to **post-transcriptional autoregulation**: RNase III (encoded by *rnc*) cleaves the *pnp* 5' untranslated leader, after which PNPase represses its own translation; cold induction of PNPase results from a reversal of this autoregulatory loop. The divergent behavior in *P. putida* implies that this autoregulatory/cold-induction logic is not simply transplanted between species. The non-essentiality of *P. putida pnp* also has a mechanistic explanation (see Finding 6): functional redundancy with RNase R.

> **Evidence:** *"We identified the PNPase-encoding gene (pnp) of Pseudomonas putida and constructed deletion mutants that did not exhibit cold sensitivity."* and *"the transcription pattern of pnp upon cold shock in P. putida was markedly different from that in Escherichia coli"* — [PMID: 12923102](https://pubmed.ncbi.nlm.nih.gov/12923102/). Autoregulation context: *"RNase III … cleaves the pnp untranslated leader, whereupon PNPase represses its own translation"* — [PMID: 11123693](https://pubmed.ncbi.nlm.nih.gov/11123693/).

### Finding 5 — PNPase's KH-S1 domains control regulatory small RNAs (RsmY/RsmZ), tuning secretion systems and virulence

A regulatory function of PNPase that is directly relevant to *Pseudomonas* comes from work in *Pseudomonas aeruginosa*, which encodes a Gac/Rsm signaling system orthologous to that of *P. putida*. The **C-terminal KH-S1 domains of PNPase directly bind the regulatory small RNAs RsmY and RsmZ and destabilize them**. Deletion of the KH-S1 domains did **not** change RsmY/Z transcription but **increased their stability**, and both in vivo pull-down and in vitro EMSA demonstrated a **direct physical interaction** between RsmY/Z and the KH-S1 fragment. This identifies PNPase as a post-transcriptional turnover factor acting on sRNAs within the Gac/Rsm circuit.

The downstream physiological consequences are substantial: through its effect on RsmY/Z levels, PNPase controls the expression of *exsA* (the master regulator of the **type III secretion system, T3SS**), modulates **pilus biosynthesis**, and reciprocally regulates the **type VI secretion system (T6SS)**. Because *P. putida* carries the orthologous Gac/Rsm regulatory architecture, this KH-S1–dependent sRNA turnover activity is highly likely to be conserved in the target organism, providing a mechanistic bridge from PNPase's enzymatic activity to global regulatory outputs.

> **Evidence:** *"deletion of the KH-S1 domains did not affect the transcription of RsmY/Z, but increased their stabilities. An in vivo pull-down and in vitro electrophoretic mobility shift assay (EMSA) demonstrated a direct interaction between RsmY/Z and the KH-S1 fragment"* and *"the KH-S1 domains of PNPase are required for the type III secretion system (T3SS) and bacterial virulence"* — [PMID: 26973625](https://pubmed.ncbi.nlm.nih.gov/26973625/).

### Finding 6 — PNPase is functionally redundant with RNase R in clearing structured RNA and rRNA fragments; together the pair is essential

PNPase (phosphorolytic) and **RNase R** (hydrolytic, helicase-containing) are the two principal 3'→5' exoribonucleases capable of attacking **structured RNA**. Studies of RNase R helicase function show that cells lacking PNPase and dependent for growth on RNase R **grow extremely poorly at 34, 37, and 42 °C and do not grow at all at 31 °C** when RNase R helicase activity is impaired. Under these conditions, **fragments of 16S and 23S rRNA accumulate to high levels, interfering with ribosome maturation and ultimately causing cell death**. This defines a shared function — **degradation of structured decay intermediates and defective rRNA fragments as part of ribosome quality control** — and establishes that the PNPase/RNase R pair is **collectively essential** even though neither is individually essential.

This redundancy elegantly explains the viability and often mild phenotypes of single Δ*pnp* mutants, including those constructed in *P. putida* (Finding 4): RNase R can substitute for PNPase in clearing structured RNA, so long as at least one of the two enzymes retains full activity.

> **Evidence:** *"cells also lacking polynucleotide phosphorylase (PNPase), and dependent for growth on RNase R, grow extremely poorly at 34, 37, and 42 °C and do not grow at all at 31 °C"* and *"fragments of 16S and 23S rRNA accumulate to high levels, leading to interference with ribosome maturation and ultimately to cell death"* — [PMID: 27022019](https://pubmed.ncbi.nlm.nih.gov/27022019/).

---

## Mechanistic Model / Interpretation

The findings assemble into a coherent picture of PNPase as a **cytoplasmic RNA-processing engine with one catalytic activity deployed across three functional arenas**: bulk mRNA decay, RNA quality control, and post-transcriptional regulation.

### Catalytic logic

```
   Phosphorolysis (degradation)          Reverse reaction (synthesis)
   5'---RNA---3' + Pi                     5'---RNA---3' + NDP
        |  processive 3'->5'                   |  template-independent
        v                                      v
   5'--(RNA shortened)--3' + NDP         5'--(RNA + 3' hetero-tail)--3' + Pi
```

The direction of net flux is set by the local ratio of **inorganic phosphate to nucleoside diphosphates**. In degradation mode, PNPase shortens transcripts and recycles ribonucleotides as NDPs; in synthetic mode, it appends destabilizing 3' tails that recruit the decay machinery. Both modes serve RNA turnover.

### Structural mechanism

```
        Top view of the PNPase homotrimer (ring)
                     ___________
                    /   KH  KH  \      <- KH + S1 domains grip and thread
                   |   \  ||  /   |       the ssRNA 3' end into the channel
                   |    central    |
                   |    channel    |    <- three RNase PH active sites;
                   |  (Pi attack)  |       phosphorolysis occurs here
                    \___KH________/
                          |
                     ssRNA 3' end enters, NDPs exit
```

Single-strand specificity and processivity both emerge from this architecture: only an unstructured 3' end can be threaded through the constricted KH/S1 aperture into the buried catalytic channel, and once engaged the RNA is degraded residue-by-residue without dissociating. Duplex or highly structured substrates require an unwinding partner — hence the functional coupling to the **RhlB helicase** in the degradosome, and the parallel role of the intrinsically helicase-equipped **RNase R** for structured RNA that PNPase cannot process alone.

### Cellular integration

```
  RNase E (endonuclease, membrane-anchored via N-terminus)
     |  C-terminal scaffold binds:
     +-- PNPase  (3'->5' phosphorolytic exonuclease)  <-- TARGET GENE PRODUCT
     +-- RhlB    (DEAD-box helicase; unwinds structure)
     +-- Enolase (glycolytic enzyme; metabolic sensing)
                 = RNA DEGRADOSOME (cytoplasm, membrane-associated)

  Parallel / redundant pathway:
     RNase R (hydrolytic 3'->5' exonuclease + helicase)
        \___ shares structured-RNA & rRNA-fragment clearance with PNPase

  Regulatory branch (Pseudomonas Gac/Rsm circuit):
     PNPase KH-S1 domains --| RsmY / RsmZ sRNA stability
                                   |
                                   v
                        RsmA availability --> T3SS, pili, T6SS, virulence
```

The table below summarizes the three functional arenas.

| Functional arena | Substrate / target | Partner(s) | Outcome | Localization |
|---|---|---|---|---|
| Bulk mRNA decay | ssRNA 3' ends from RNase E cuts | RNase E, RhlB, enolase (degradosome) | Timely transcript turnover; nucleotide recycling | Cytoplasm / inner membrane |
| RNA quality control | Structured decay intermediates; 16S/23S rRNA fragments | Redundant with RNase R | Ribosome maturation; prevents toxic fragment accumulation | Cytoplasm |
| Post-transcriptional regulation | RsmY / RsmZ small RNAs | KH-S1 domains (direct binding) | Tunes T3SS, pili, T6SS, virulence via Gac/Rsm | Cytoplasm |

### Species-specific tuning in *P. putida*

While the enzyme and its mechanism are conserved from *E. coli* through *Caulobacter*, *Yersinia*, and *Pseudomonas*, the **physiological deployment differs**. In *E. coli*, *pnp* is a cold-shock gene governed by RNase III–dependent autoregulation, and its loss confers cold sensitivity. In *P. putida*, deletion of *pnp* is **not** cold-sensitive and the cold-shock transcriptional response of *pnp* is different — indicating rewired regulation. The non-essentiality of the single deletion is best explained by **redundancy with RNase R**. Thus for *P. putida* KT2440 the safest, evidence-grounded statement is: the enzyme's catalytic identity and degradosome/regulatory roles are conserved, but its stress-response regulation is organism-specific and should not be assumed to mirror *E. coli*.

---

## Evidence Base

| PMID | Title (abbreviated) | How it supports the annotation |
|---|---|---|
| [22724061](https://pubmed.ncbi.nlm.nih.gov/22724061/) | *Crystal structure of Caulobacter crescentus PNPase…* | Defines the processive 3'→5' ssRNA exoribonuclease activity; the trimeric ring, central catalytic channel, and KH/S1 substrate-channeling mechanism (Findings 1, 2) |
| [12746447](https://pubmed.ncbi.nlm.nih.gov/12746447/) | *Crystal structure of RNase PH from Aquifex aeolicus* | Establishes structural homology between the PNPase core homotrimer and RNase PH, confirming the phosphorolytic-exoribonuclease fold (Finding 2) |
| [15995184](https://pubmed.ncbi.nlm.nih.gov/15995184/) | *Addition of poly(A) and heteropolymeric 3' ends in B. subtilis…* | Genetic evidence for PNPase's reverse/synthetic activity adding 3' tails (Finding 1) |
| [9732274](https://pubmed.ncbi.nlm.nih.gov/9732274/) | *RNase E organizes the E. coli RNA degradosome* | Establishes PNPase as a degradosome subunit bound to the RNase E C-terminal scaffold alongside RhlB and enolase (Finding 3) |
| [11134527](https://pubmed.ncbi.nlm.nih.gov/11134527/) | *RNA degradosomes… associated with the cytoplasmic membrane via RNase E* | Defines the subcellular localization of the degradosome (and PNPase) at the inner membrane (Finding 3) |
| [12181321](https://pubmed.ncbi.nlm.nih.gov/12181321/) | *RhlB physically associates with PNPase…* | Documents a degradosome-independent PNPase–RhlB α₃β₂ complex active on dsRNA (Finding 3) |
| [12923102](https://pubmed.ncbi.nlm.nih.gov/12923102/) | *Polynucleotide phosphorylase-deficient mutants of Pseudomonas putida* | **Direct study of the target gene**: identifies *P. putida pnp*, shows Δ*pnp* is not cold-sensitive, and reports divergent cold-shock transcription (Finding 4) |
| [11123693](https://pubmed.ncbi.nlm.nih.gov/11123693/) | *Cold-temperature induction of E. coli PNPase…* | Describes RNase III–dependent autoregulation of *pnp* in *E. coli* for comparative context (Finding 4) |
| [26973625](https://pubmed.ncbi.nlm.nih.gov/26973625/) | *PNPase regulates virulence factors and RsmY/Z stability in P. aeruginosa* | Shows PNPase KH-S1 domains directly bind and destabilize RsmY/Z sRNAs, controlling T3SS/pili/T6SS/virulence (Finding 5) |
| [27022019](https://pubmed.ncbi.nlm.nih.gov/27022019/) | *Helicase activity… for RNase R function in vivo* | Demonstrates PNPase/RNase R redundancy, collective essentiality, and rRNA-fragment/ribosome quality-control role (Finding 6) |

Supporting degradosome literature reviewed and consistent with the above includes proteomic analyses of degradosome composition ([PMID: 19161840](https://pubmed.ncbi.nlm.nih.gov/19161840/), [PMID: 16139413](https://pubmed.ncbi.nlm.nih.gov/16139413/)), the demonstration that RhlB (not enolase) is the β-subunit of the PNPase α₃β₂ complex ([PMID: 16275923](https://pubmed.ncbi.nlm.nih.gov/16275923/)), a review of the *E. coli* degradosome ([PMID: 12035760](https://pubmed.ncbi.nlm.nih.gov/12035760/)), in vivo FRET assembly measurements ([PMID: 23927922](https://pubmed.ncbi.nlm.nih.gov/23927922/)), the enolase-specific role in phosphosugar-stress mRNA decay ([PMID: 15522087](https://pubmed.ncbi.nlm.nih.gov/15522087/)), and the *Yersinia* degradosome study showing that PNPase's cold-growth role is degradosome-independent while its oxidative-stress role is degradosome-dependent ([PMID: 23082859](https://pubmed.ncbi.nlm.nih.gov/23082859/)).

---

## Limitations and Knowledge Gaps

1. **Most mechanistic evidence is from orthologs, not the target strain.** The catalytic mechanism, trimeric ring structure, degradosome assembly, and RsmY/Z regulation are established in *E. coli*, *Caulobacter crescentus*, *Yersinia pseudotuberculosis*, and *Pseudomonas aeruginosa* — not in *P. putida* KT2440 itself. The strongest strain-specific evidence ([PMID: 12923102](https://pubmed.ncbi.nlm.nih.gov/12923102/)) concerns non-essentiality and cold-shock behavior, not direct biochemistry or structure. Conservation is inferred from domain architecture and phylogeny, which is well justified but not equivalent to direct demonstration.

2. **No experimental structure of Q88DW0.** The trimeric ring / KH-S1 channeling model rests on homology to the *Caulobacter* structure. An AlphaFold or experimental structure of the *P. putida* enzyme has not been examined here.

3. **Degradosome composition in *P. putida* is inferred.** Whether *P. putida* RNase E recruits PNPase, RhlB, and enolase in exactly the *E. coli* configuration — and whether additional or alternative partners exist — has not been directly demonstrated in the target organism. Degradosome composition is known to be flexible and condition-dependent.

4. **RsmY/Z regulation shown in *P. aeruginosa*, not *P. putida*.** Although *P. putida* encodes an orthologous Gac/Rsm system, the direct KH-S1–RsmY/Z interaction and its virulence consequences were demonstrated in *P. aeruginosa*, a pathogen; *P. putida* is a non-pathogenic soil/rhizosphere organism, so the downstream physiological outputs (e.g., T3SS/virulence) may differ or be attenuated even if the biochemical sRNA-turnover activity is conserved.

5. **Quantitative parameters absent.** Substrate-specificity constants (Km, kcat), phosphate/NDP concentration thresholds governing degradation-vs-synthesis flux, and processivity length distributions have not been measured for the *P. putida* enzyme.

---

## Proposed Follow-up Experiments / Actions

1. **Direct biochemical characterization of purified Q88DW0.** Express and purify recombinant *P. putida* PNPase and confirm (i) phosphorolytic 3'→5' ssRNA degradation releasing NDPs, (ii) reversible synthetic activity, and (iii) Pi/NDP flux thresholds, using defined ssRNA and structured substrates.

2. **Structural confirmation.** Solve or model (cryo-EM / X-ray, or validate an AlphaFold model with `phenix` tools) the *P. putida* PNPase to confirm the homotrimeric ring and KH-S1 channel geometry predicted from the *Caulobacter* ortholog.

3. **Degradosome pull-down in *P. putida* KT2440.** Affinity-tag RNase E (or PNPase) and use co-IP/MudPIT to determine whether PNPase, RhlB, and enolase co-assemble in this organism, and identify any species-specific partners. Localize the complex relative to the inner membrane by fluorescence microscopy.

4. **Test RsmY/Z regulation in *P. putida*.** Delete the KH-S1 domains specifically (rather than the whole gene) and measure RsmY/RsmZ stability and downstream Gac/Rsm outputs (e.g., biofilm, root colonization, secondary metabolism) relevant to the non-pathogenic lifestyle.

5. **Synthetic-lethality / redundancy test.** Construct Δ*pnp* Δ*rnr* (RNase R) combinations in *P. putida* to test whether the collective essentiality and rRNA-fragment accumulation observed in *E. coli* also hold, confirming the redundancy model that explains Δ*pnp* viability.

6. **Transcriptome-wide substrate mapping.** Apply RNA-seq / degradome-seq on Δ*pnp* vs wild-type *P. putida* under normal and cold conditions to define the endogenous substrate spectrum and clarify the divergent cold-shock physiology.

---

*Report prepared from an autonomous 3-iteration literature and database investigation. Target verified: UniProt Q88DW0, gene* pnp*, locus PP_4708,* Pseudomonas putida *KT2440. All gene-identity checks passed — the "pnp" symbol, EC 2.7.7.8 assignment, polyribonucleotide-nucleotidyltransferase family membership, and ExoRNase_PH/KH/S1 domain architecture are mutually consistent and match the retrieved literature.*


## Artifacts

- [OpenScientist final report](pnp-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](pnp-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:22724061
2. PMID:15995184
3. PMID:12746447
4. PMID:9732274
5. PMID:11134527
6. PMID:12181321
7. PMID:12923102
8. PMID:11123693
9. PMID:26973625
10. PMID:27022019
11. PMID:19161840
12. PMID:16139413
13. PMID:16275923
14. PMID:12035760
15. PMID:23927922
16. PMID:15522087
17. PMID:23082859