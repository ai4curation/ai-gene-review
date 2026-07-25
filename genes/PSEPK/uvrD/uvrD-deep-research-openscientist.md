---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-25T16:42:45.006083'
end_time: '2026-07-25T16:54:52.568882'
duration_seconds: 727.56
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: uvrD
  gene_symbol: uvrD
  uniprot_accession: Q88C31
  protein_description: 'RecName: Full=DNA helicase II {ECO:0000256|ARBA:ARBA00074869};
    EC=5.6.2.4 {ECO:0000256|ARBA:ARBA00034808}; AltName: Full=DNA 3''-5'' helicase
    II {ECO:0000256|ARBA:ARBA00034923};'
  gene_info: Name=uvrD {ECO:0000313|EMBL:AAN70917.1}; OrderedLocusNames=PP_5352 {ECO:0000313|EMBL:AAN70917.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the helicase family. UvrD subfamily.
  protein_domains: DExx_box_DNA_helicase_dom_sf. (IPR013986); DNA_helicase_UvrD-like_C.
    (IPR014017); DNA_helicase_UvrD/REP. (IPR000212); P-loop_NTPase. (IPR027417); UvrD-like_ATP-bd.
    (IPR014016)
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
  path: uvrD-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: uvrD-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88C31
- **Protein Description:** RecName: Full=DNA helicase II {ECO:0000256|ARBA:ARBA00074869}; EC=5.6.2.4 {ECO:0000256|ARBA:ARBA00034808}; AltName: Full=DNA 3'-5' helicase II {ECO:0000256|ARBA:ARBA00034923};
- **Gene Information:** Name=uvrD {ECO:0000313|EMBL:AAN70917.1}; OrderedLocusNames=PP_5352 {ECO:0000313|EMBL:AAN70917.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the helicase family. UvrD subfamily.
- **Key Domains:** DExx_box_DNA_helicase_dom_sf. (IPR013986); DNA_helicase_UvrD-like_C. (IPR014017); DNA_helicase_UvrD/REP. (IPR000212); P-loop_NTPase. (IPR027417); UvrD-like_ATP-bd. (IPR014016)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "uvrD" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'uvrD' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **uvrD** (gene ID: uvrD, UniProt: Q88C31) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of *uvrD* (DNA helicase II, Q88C31 / PP_5352) in *Pseudomonas putida* KT2440

## 1. Summary / Answer to the Research Question

**Q88C31 is UvrD (DNA helicase II), encoded by *uvrD*/PP_5352 in *Pseudomonas putida* KT2440.** It is an **ATP-dependent, superfamily-1A (SF1A) DNA helicase / single-stranded-DNA (ssDNA) translocase** that moves along DNA with **3'→5' polarity** and hydrolyzes ATP in a DNA-stimulated manner (EC 5.6.2.4). Its physiological substrate is **duplex chromosomal DNA bearing a 3' single-stranded loading region**, and it functions in the **cytoplasm at the nucleoid**. Mechanistically, UvrD unwinds/strips DNA at three converging genome-maintenance pathways: **(i) nucleotide excision repair (NER)** — displacing the lesion-containing strand after UvrABC incision; **(ii) methyl-directed mismatch repair (MMR)** — unwinding the error-containing strand after activation by MutL; and **(iii) recombination control** — acting as an **anti-recombinase** that removes RecA filaments from ssDNA and thereby tunes homologous recombination and the SOS response.

Identity is unambiguous, so function is confidently transferred from the extensively characterized *E. coli*/model-organism enzyme.

---

## 2. Gene / Protein Identity (Verification)

| Property | Value |
|---|---|
| UniProt | Q88C31 |
| Gene / locus | *uvrD* / PP_5352 |
| Protein | DNA helicase II (DNA 3'–5' helicase II); EC 5.6.2.4 |
| Organism | *Pseudomonas putida* KT2440 (ATCC 47054 / DSM 6125) |
| Length / mass | 728 aa / 81.7 kDa |
| Domains | UvrD-like helicase ATP-binding (res 11–289) + UvrD-like C-terminal (res 290–567) |
| Motifs | Walker A / P-loop **AGAGSGKT** (res 32–39) |
| Family / orthology | Helicase SF1, UvrD subfamily; eggNOG **COG0210**; Pfam **PF00580 + PF13361**; InterPro IPR000212, IPR027417, IPR014016/17, IPR013986 |

**Orthology check (this study):** Domain architecture, gene symbol, and COG assignment match *E. coli* UvrD (P03018, 720 aa). A quick sequence comparison found **128 exact shared 5-mers (Jaccard ≈ 0.10)** between the two proteins — far above background for random proteins — and the canonical Walker-A P-loop (GSGKT) is present at the expected N-terminal position. The gene symbol "uvrD" is **not ambiguous** here: it corresponds to the classic, well-conserved bacterial DNA helicase II. Function can therefore be annotated with high confidence.

---

## 3. Primary Molecular Function — the Catalyzed Reaction and Substrate

UvrD is a **DNA-stimulated ATPase** that couples ATP hydrolysis to **directional 3'→5' translocation on ssDNA**, driving separation of duplex DNA (EC 5.6.2.4; GO:0043138 3'-5' DNA helicase, GO:0005524 ATP binding, GO:0016887 ATP hydrolysis).

- **Reaction (UniProt/RHEA):** **ATP + H₂O → ADP + phosphate + H⁺** (RHEA:13065), and formally "couples ATP hydrolysis with the unwinding of duplex DNA by translocating in the 3'-5' direction." Under the 2021 EC revision, helicases were reclassified as **isomerases/translocases (EC 5.6.2.4)**: UvrD does not chemically modify DNA — it is a molecular motor that alters DNA conformation (duplex → two single strands).
- **Substrate specificity:** duplex DNA presenting a **3' single-stranded tail** for loading; the enzyme translocates on the tracking strand toward the duplex. Cofactor: **ATP + Mg²⁺**. Biochemically, the *Deinococcus radiodurans* ortholog is "a DNA-stimulated ATPase, can translocate along ssDNA in the 3'-5' direction and shows ATP-dependent 3'-5'… helicase activity" (PMID 24143224).
- **Activation / regulation:** the **monomer is a processive 3'→5' translocase but a weak helicase**; efficient unwinding requires **activation by dimerization (via the 2B regulatory domain)** or by an **accessory partner protein** (PMID 42444602; PMID 38677494). This switch makes UvrD a *regulatable*, pathway-specific motor rather than a constitutively active unwindase.

---

### 3.1 Structural basis of the mechanism
UvrD-family helicases have a conserved **four-subdomain fold**: subdomains **1A and 2A** form the tandem RecA-like ATPase motor, while **1B and the mobile 2B domain** are accessory/regulatory (conserved in Q88C31: ATP-binding domain res 11–289 with Walker-A **AGAGSGKT**; UvrD_C domain res 290–567). Two RecA-like lobes hydrolyze ATP to ratchet along ssDNA; a **conserved β-hairpin "separation pin"** splits the duplex (its mutation abolishes helicase activity), and structures of the *D. radiodurans* ortholog "trap a DNA helicase undergoing a large-scale spiral movement around duplexed DNA" (PMID 24143224). The **2B domain is an allosteric switch**: it autoinhibits the monomer and is the general dimerization interface for the family, so activity is turned on by dimerization or by partner proteins (PMID 42444602; PMID 29087333). This explains why UvrD is a *regulatable*, context-specific motor.

## 4. Biological Processes / Pathways

### 4.1 Nucleotide excision repair (NER)
After the UvrABC excinuclease dual-incises around a bulky/UV lesion, **UvrD unwinds the duplex 3'→5' to displace the lesion-containing oligonucleotide**, permitting resynthesis (Pol I) and ligation. "UvrD… plays an essential role in bacterial NER by unwinding the duplex DNA in the 3' to 5' direction to displace the lesion-containing strand" (PMID 28120472). Consistent with this, *uvrD* loss confers **UV sensitivity** (PMID 6355763).

### 4.2 Methyl-directed mismatch repair (MMR)
UvrD is the **helicase that excises the error-containing strand** in MMR. **MutL activates UvrD** to "unwind DNA from the strand incision site up to and beyond the mismatch" (PMID 38677494). Because the monomer is a poor helicase, MutL (or dimerization) is the required activator (PMID 38677494). Loss of *uvrD* therefore produces a strong **mutator phenotype**, and *uvrD* is grouped genetically with *mutH/mutL/mutS* in the methyl-directed MMR pathway; the *uvrD* knockout is "mutator and UV-sensitive" (PMID 6355763). This role directly maintains **replication fidelity and genome stability**.

### 4.3 Transcription-coupled repair (TCR) — proposed/debated
Beyond global-genome NER, an emerging model proposes that **UvrD backtracks RNA polymerase stalled at a lesion**, exposing the damage for NER, as an alternative to Mfd-mediated RNAP displacement: damage detection can occur "via transcription-coupled repair using UvrD-mediated backtracking or Mfd-controlled displacement of the RNA polymerase" (PMID 35235801). In live *E. coli*, UvrD recruitment to DNA after UV damage is **strongly UvrA-dependent**, tying it to the NER machinery (PMID 38513450). The relative contributions of the UvrD- vs Mfd-dependent routes remain under active debate.

### 4.4 Recombination control / SOS (anti-recombinase)
UvrD **removes RecA filaments from ssDNA** — "The UvrD helicase removes RecA filaments from RecA" (PMID 17364684) — thereby limiting inappropriate homologous recombination and **modulating the SOS response** (e.g., *uvrD303* alleles decrease SOS expression; PMID 24084169). *uvrD* is itself **DNA-damage–inducible under lexA-recA (SOS) control** (PMID 6355763), integrating it into the DNA-damage response network. GO also annotates **recombinational repair** (GO:0000725).

---

## 5. Localization

UvrD is a **soluble cytoplasmic enzyme** acting on **chromosomal DNA at the nucleoid** (GO:0005829 cytosol; GO:0033202 DNA helicase complex; GO:0003677 DNA binding). The 728-aa sequence contains only the two intracellular helicase domains and a P-loop, with **no signal peptide or transmembrane segment** — it is neither secreted nor membrane-associated. It engages DNA at replication forks and repair/recombination intermediates. (Localization is inferred from ortholog annotation and sequence features; no direct *P. putida* imaging is available.)

---

### 5.1 *P. putida*-specific functional network (STRING)
Independent of ortholog transfer, the STRING v12 interactome for **PP_5352** places UvrD at a genome-maintenance hub, with top partners spanning every pathway above: **uvrB (0.934), dnaB (0.906), mutL (0.868), uvrA (0.840), uvrC (0.761), dnaN β-clamp (0.733), recA (0.717), dinG (0.710), mutY (0.668), mfd (0.647), recQ (0.641), ruvA (0.621)** — i.e., NER excinuclease (UvrABC/Mfd), mismatch repair (MutL/MutY), the replisome (DnaB helicase, DnaN clamp), and recombination/fork processing (RecA, RuvA, RecQ, DinG). This corroborates the pathway assignments directly in *P. putida*.

## 6. Supported vs. Refuted Hypotheses

**Supported:**
- H1 — Q88C31 is a *bona fide* UvrD ortholog (identity/domain/motif/COG evidence). ✔
- H2 — Primary function is ATP-dependent 3'→5' DNA helicase / ssDNA translocase. ✔
- H3 — Functions in NER (post-incision strand displacement). ✔
- H4 — Functions in MMR (MutL-activated; mutator on loss). ✔
- H5 — Acts as an anti-recombinase (RecA removal) within the SOS network. ✔
- H6 — Cytoplasmic, DNA-associated; not secreted/membrane-bound. ✔
- H7 — Activity is allosterically gated by the 2B domain (dimerization/partner activation); β-hairpin acts as the strand-separation pin. ✔
- H8 — In P. putida specifically, UvrD is networked with NER/MMR/replication/recombination machinery (STRING). ✔
- H9 — Possible role in transcription-coupled repair via RNAP backtracking (supported but debated). ◐

**Refuted / excluded:** the gene symbol is **not** ambiguous or misassigned; no evidence supports an alternative (e.g., non-helicase) function.

---

## 7. Limitations and Future Directions

- Nearly all mechanistic and biochemical evidence derives from **orthologs** (*E. coli*, *D. radiodurans*, *Mtb* UvrD1, *P. falciparum*), not from *P. putida* PP_5352 directly; functional transfer relies on strong sequence/domain conservation.
- No *P. putida*-specific knockout, biochemistry, or localization study was located in this search; direct characterization (ATPase/helicase assays, Δ*uvrD* mutator/UV-sensitivity phenotyping, MutL/UvrABC interaction) would confirm the annotation.
- *P. putida* also encodes UvrD-family paralogs (e.g., Rep/PcrA-like helicases); partner specificity and any pathway division of labor in this organism remain to be established experimentally.

---

*Evidence types used:* protein-family/domain bioinformatics (UniProt, InterPro/Pfam, eggNOG-COG), sequence-motif analysis (Walker-A P-loop), *P. putida*-specific functional interactome (STRING v12), reaction/RHEA annotation (RHEA:13065, EC 5.6.2.4), structural/mechanistic studies (PMIDs 24143224, 42444602, 29087333), and primary/review literature on UvrD biochemistry and genetics (PMIDs 38677494, 28120472, 17364684, 24084169, 6355763, 35235801, 38513450, 34081984).


## Artifacts

- [OpenScientist final report](uvrD-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](uvrD-deep-research-openscientist_artifacts/final_report.pdf)