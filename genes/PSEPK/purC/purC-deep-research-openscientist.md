---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-25T15:13:38.946633'
end_time: '2026-07-25T15:29:23.504947'
duration_seconds: 944.56
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: purC
  gene_symbol: purC
  uniprot_accession: Q88NG9
  protein_description: 'RecName: Full=Phosphoribosylaminoimidazole-succinocarboxamide
    synthase {ECO:0000255|HAMAP-Rule:MF_00137}; EC=6.3.2.6 {ECO:0000255|HAMAP-Rule:MF_00137};
    AltName: Full=SAICAR synthetase {ECO:0000255|HAMAP-Rule:MF_00137};'
  gene_info: Name=purC {ECO:0000255|HAMAP-Rule:MF_00137}; OrderedLocusNames=PP_1240;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the SAICAR synthetase family.
  protein_domains: SAICAR_synt/ADE2_N. (IPR028923); SAICAR_synt_PurC. (IPR033934);
    SAICAR_synth. (IPR001636); SAICAR_synthetase. (IPR050089); SAICAR_synthetase_CS.
    (IPR018236)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
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
  path: purC-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: purC-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88NG9
- **Protein Description:** RecName: Full=Phosphoribosylaminoimidazole-succinocarboxamide synthase {ECO:0000255|HAMAP-Rule:MF_00137}; EC=6.3.2.6 {ECO:0000255|HAMAP-Rule:MF_00137}; AltName: Full=SAICAR synthetase {ECO:0000255|HAMAP-Rule:MF_00137};
- **Gene Information:** Name=purC {ECO:0000255|HAMAP-Rule:MF_00137}; OrderedLocusNames=PP_1240;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the SAICAR synthetase family.
- **Key Domains:** SAICAR_synt/ADE2_N. (IPR028923); SAICAR_synt_PurC. (IPR033934); SAICAR_synth. (IPR001636); SAICAR_synthetase. (IPR050089); SAICAR_synthetase_CS. (IPR018236)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "purC" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'purC' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **purC** (gene ID: purC, UniProt: Q88NG9) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: purC (Q88NG9) — SAICAR synthetase from *Pseudomonas putida* KT2440

## 1. Summary / Answer to the Research Question

**purC** (UniProt **Q88NG9**, entry name **PUR7_PSEPK**; ordered locus **PP_1240**) encodes **phosphoribosylaminoimidazole-succinocarboxamide synthetase**, better known as **SAICAR synthetase** (**EC 6.3.2.6**). It is a soluble, cytoplasmic, ATP-dependent carbon–nitrogen ligase that catalyzes the **seventh step of the de novo purine (IMP) biosynthetic pathway**: the Mg²⁺- and ATP-dependent condensation of **4-carboxy-5-aminoimidazole ribonucleotide (CAIR)** with **L-aspartate** to produce **SAICAR** (N-succinocarboxamide-5-aminoimidazole ribonucleotide), ADP and inorganic phosphate. Its primary biological role is to supply, together with the rest of the *pur* pathway, the purine nucleotides (ATP, GTP and their deoxy forms) required for nucleic acid synthesis and energy metabolism. The *P. putida* protein itself is annotated by homology, but the reaction, mechanism, structure and physiology are firmly established for the highly conserved SAICAR synthetase family.

> **Identity verification (per instructions):** The gene symbol *purC*, the description "SAICAR synthetase / EC 6.3.2.6", the SAICAR_synt/PurC domains (IPR001636, IPR033934, IPR050089, IPR028923, IPR018236) and the organism *Pseudomonas putida* KT2440 (taxid 160488) are all mutually consistent and match the UniProt record retrieved for Q88NG9 (236 aa, ~26.9 kDa). There is **no ambiguity**: this is the canonical bacterial purine-biosynthesis gene *purC*. (Note: "PurC" is unrelated to the *Staphylococcus aureus* accessory-gene regulator context or to eukaryotic bifunctional PAICS naming; those share pathway chemistry, not gene-symbol confusion here.)

---

## 2. Molecular Identity

| Property | Value | Source |
|---|---|---|
| UniProt accession / entry | Q88NG9 / PUR7_PSEPK | UniProtKB |
| Gene | *purC*; locus PP_1240 | UniProtKB |
| Organism | *Pseudomonas putida* KT2440 (taxid 160488) | UniProtKB |
| Length / MW | 236 aa / 26,916 Da | UniProtKB |
| EC number | 6.3.2.6 | UniProtKB; PMID 26100042 |
| Family | SAICAR synthetase family | UniProtKB (HAMAP MF_00137) |
| Cross-refs | KEGG ppu:PP_1240; STRING 160488.PP_1240; BioCyc PPUT160488:G1G01-1326-MONOMER; RefSeq WP_003254733.1; AlphaFoldDB Q88NG9 | UniProtKB |
| Keywords | ATP-binding, Ligase, Nucleotide-binding, Purine biosynthesis | UniProtKB |
| Evidence level | Protein existence 3 (inferred from homology) | UniProtKB |

---

## 3. Primary Function — The Catalyzed Reaction

PurC catalyzes the ATP-dependent ligation of CAIR and L-aspartate:

**CAIR + L-aspartate + ATP → SAICAR + ADP + Pᵢ + 2 H⁺**

Formally (UniProt catalytic activity for Q88NG9):
*5-amino-1-(5-phospho-D-ribosyl)imidazole-4-carboxylate + L-aspartate + ATP = (2S)-2-[5-amino-1-(5-phospho-β-D-ribosyl)imidazole-4-carboxamido]succinate + ADP + phosphate + 2 H⁺.*

This is **the seventh step of the ten-step de novo pathway** that builds inosine 5′-monophosphate (IMP) from 5-phospho-α-D-ribose 1-diphosphate (PRPP) (Wolf et al., *S. pneumoniae* PurC structures, PMID 24598753). It is classified in UniProt within the sub-pathway "IMP biosynthesis via de novo pathway; AICAR from CAIR, step 1/2" — i.e., PurC (step 1) forms SAICAR, and the following enzyme **PurB** (adenylosuccinate lyase) cleaves fumarate from SAICAR to yield **AICAR** (step 2).

### Substrate specificity
- **Amidino-donor substrate:** CAIR (also written 4-carboxy-AIR). Structural studies show the imidazole-ribonucleotide sub-site is highly specific for the phosphoribosyl-imidazole scaffold; the enzyme's nucleotide-recognition pocket shows a preference for pyrimidine-like mimics in co-crystals but the physiological substrate is CAIR (Manjunath et al., *P. horikoshii*, PMID 26072057).
- **Amino donor:** **L-aspartate**, whose α-amino group is ligated to the CAIR carboxyl to form the succinocarboxamide (Wolf et al., PMID 24598753 — first PurC structure with Asp in the active site).
- **Energy/cofactor:** **ATP** (hydrolyzed to ADP + Pᵢ) with an obligatory **Mg²⁺** cofactor.

---

## 4. Catalytic Mechanism (inferred from family structures)

Multiple crystal structures and molecular-dynamics studies of orthologous SAICAR synthetases define the mechanism, which is conserved and therefore applicable to the *P. putida* enzyme by homology:

- **Dimeric, three-site active center.** Structures of *S. pneumoniae* PurC (with ADP·Mg²⁺·AIR·Asp; PMID 24598753) and of the hyperthermophile *Pyrococcus horikoshii* SAICAR synthetase (native dimer, PMID 23137517; eight ligand complexes + MD, PMID 26072057) reveal separate sub-sites for the nucleotide, the imidazole-ribonucleotide, and L-aspartate arranged so the reacting groups are juxtaposed.
- **Acyl-phosphate intermediate ("phosphorylation-first" relay).** ATP is proposed to first phosphorylate the CAIR carboxylate, generating a reactive acyl-phosphate; the L-aspartate α-amino group then performs nucleophilic attack, displacing phosphate and forming the new amide (C–N) bond of SAICAR. Wolf et al. explicitly propose "a relay mechanism for the formation of the product SAICAR," and Manjunath et al. found a phosphate ion positioned between the ATP and CAIR sites that "strengthens one of the two probable pathways ... and suggests the possibility of a phosphorylation taking place before the ASP's att[ack]" (PMID 24598753; PMID 26072057).
- **Mg²⁺ dependence** for nucleotide positioning and phosphoryl transfer (PMID 24598753).

---

## 5. Localization

PurC functions in the **cytoplasm**. The de novo purine pathway is a soluble, cytosolic system; the Q88NG9 sequence carries **no signal peptide and no transmembrane segment**, and UniProt keywords (ATP-binding, Nucleotide-binding, Ligase) describe a soluble metabolic enzyme. The very high AlphaFold confidence (mean pLDDT 96.7, 0% low-confidence, no disordered stretches) further supports a compact, well-folded globular protein rather than a membrane or secreted product. PurC itself is a soluble **homodimer** (conserved across the family crystal structures, PMID 23137517); transient co-clustering of consecutive purine-pathway enzymes (a "purinosome," best characterized in eukaryotic cells) may enhance metabolic channelling, but PurC's catalytic activity is intrinsic to the free dimer.

---

## 6. Pathway Context and Physiological Role

1. **Central role — de novo purine (IMP) biosynthesis.** SAICAR is an obligate intermediate en route to IMP, the common precursor of AMP/ATP and GMP/GTP. Loss of PurC blocks this route (bypassable only by purine salvage), so the enzyme is essential for growth in purine-free media. PurC "has been shown to be conditionally essential for bacterial replication" (PMID 24598753).
2. **Downstream step.** SAICAR → (PurB, adenylosuccinate lyase) → **AICAR** + fumarate; AICAR is then processed by the bifunctional PurH to IMP.
3. **Link to thiamine (vitamin B1) biosynthesis.** The purine intermediate **AIR** is the precursor of the thiamine pyrimidine moiety. In *Salmonella enterica*, a functional PurC is required for a secondary route that converts accumulated AICAR to AIR, connecting purine and thiamine biosynthesis; this PurC-dependent AICAR→AIR conversion was reconstituted in vitro (PMID 26100042). This illustrates the metabolic-network importance of PurC beyond the linear IMP pathway.
4. **Nucleotide-responsive regulation.** In *E. coli*, *purC* is a member of the **pur regulon** and is transcriptionally repressed 5–17-fold by the purine repressor **PurR** binding a conserved 16-bp operator overlapping its promoter, coordinating expression with intracellular purine pools (PMID 2198266). *P. putida* possesses a homologous PurR-type regulatory system, so equivalent feedback regulation is expected.

---

## 7. Evolutionary and Bioinformatic Evidence

- **High orthology to a validated enzyme.** A global Needleman–Wunsch alignment of *P. putida* PurC (Q88NG9, 236 aa) against the biochemically- and genetically-characterized *E. coli* PurC (P0A7D7, 237 aa) yields **71.6% amino-acid identity** over 237 aligned positions with essentially no gaps — far above the sequence-homology "twilight zone." This confidently transfers the *E. coli* enzyme's defined function (reaction, substrate specificity, Mg²⁺/ATP dependence, cytoplasmic localization) to the *P. putida* protein.
- **Database orthology / pathway assignment.** KEGG (ppu:PP_1240) assigns KEGG Orthology **K01923** [EC 6.3.2.6], maps the gene to **ppu00230 Purine metabolism** and to module **M00048 "De novo purine biosynthesis, PRPP + glutamine → IMP,"** and lists the Pfam **SAICAR_synt** motif (gene coordinates 1,417,542–1,418,252; NCBI protein AAN66864).
- **Gene neighborhood.** *purC* (PP_1240) is **not embedded in a pur operon**: flanking genes (PP_1238 lipoprotein, PP_1239 metallo-β-lactamase family, PP_1241/PP_1242 conserved hypotheticals on the opposite strand) are unrelated to purine biosynthesis. This mirrors *E. coli*, where *pur* genes are physically dispersed and coordinated at the **regulon** level (PurR) rather than as a single operon (PMID 2198266).
- **Conservation across all domains of life.** *P. putida* PurC aligns to **every crystallographically-characterized SAICAR synthetase** across the conserved SAICAR_synt core: *E. coli* PurC (P0A7D7) **71.6%**, *P. horikoshii* PurC (O57978, PMID 23137517/26072057) **51.1%**, *S. pneumoniae* PurC (Q8DRM7, PMID 24598753) **47.2%**, and *S. cerevisiae* Ade1 (P27616, PDB 2CNU) **43.2%** identity. SAICAR synthetases are "reasonably similar in sequence and three-dimensional structure," differing mainly in stability determinants (PMID 23137517), and the reaction is "one of the highly conserved pathways among all organisms and is essential for cell viability" (PMID 26072057). This domain-spanning conservation makes the substrate-binding sub-sites and catalytic mechanism defined in those structures directly transferable to Q88NG9.
- **Structural inference (AlphaFold).** The AlphaFold DB model of Q88NG9 (v6, 236 aa) is of very high quality — **mean pLDDT 96.7; 100% of residues confidently modeled (pLDDT > 70), 94.1% very high (> 90), 0% low** — indicating a single, compact, well-ordered SAICAR-synthetase fold with no disordered or membrane-embedded segments, fully consistent with a soluble cytoplasmic enzyme.
- **Domain signatures.** The protein carries the diagnostic SAICAR_synt/PurC domains (InterPro IPR001636, IPR033934, IPR050089, IPR028923, plus the family conserved-site IPR018236), and UniProt assigns it via HAMAP rule MF_00137 — a rule-based, family-specific automated annotation with high reliability for this well-defined enzyme family.
- **Eukaryotic counterpart.** In humans the same chemistry (plus the adjacent AIR carboxylase step) is performed by the bifunctional enzyme **PAICS**, an emerging cancer target (PMID 32571877), underscoring the biological importance and druggability of this reaction.

---

## 8. Drug-Target Relevance

Because de novo purine synthesis is essential/conditionally essential and PurC has no direct human single-domain ortholog (humans use bifunctional PAICS), bacterial PurC is pursued as an **antibacterial target**; the *S. pneumoniae* structural work was explicitly performed to enable inhibitor discovery against "a multidrug-resistant pathogen" (PMID 24598753). This is relevant context for *P. putida* PurC as a representative of the conserved bacterial enzyme.

---

## 9. Supported vs. Refuted Hypotheses

**Supported:**
- H1 — Q88NG9 is SAICAR synthetase (EC 6.3.2.6) catalyzing CAIR + L-Asp + ATP → SAICAR + ADP + Pᵢ. **Strongly supported** (UniProt catalytic annotation + family biochemistry, PMID 24598753/26100042).
- H2 — Enzyme is cytoplasmic, Mg²⁺-dependent, homodimeric, using an acyl-phosphate relay mechanism. **Supported** by orthologous structures (PMID 24598753/23137517/26072057) and sequence features (no TM/signal).
- H3 — *purC* is embedded in nucleotide-responsive (PurR/pur-regulon) control and is (conditionally) essential; contributes to a purine–thiamine metabolic link via AIR. **Supported** (PMID 2198266, 24598753, 26100042).

**Refuted / not applicable:**
- Any transporter, structural, or signaling function — **refuted**: all evidence points to a metabolic ligase (EC 6.3.2.6) in nucleotide biosynthesis, not transport or signaling.

---

## 10. Limitations and Future Directions

- **Homology-based annotation:** The *P. putida* KT2440 protein has protein-existence level 3 (inferred from homology); no *P. putida*-specific enzymology, knockout, or structure has been published. Direct biochemical/genetic confirmation in KT2440 (e.g., *purC* deletion → purine auxotrophy; in-vitro assay of the recombinant enzyme) would upgrade the evidence.
- **Mechanistic detail:** The order of substrate binding and the precise identity of the phosphorylated intermediate are inferred from orthologs and MD; species-specific kinetics (Km for CAIR, Asp, ATP; possible allosteric inhibition by CTP/UTP as seen in yeast) remain to be measured for the *P. putida* enzyme.
- **Regulation:** PurR-mediated repression is documented in *E. coli*; the exact operator and regulatory factors at PP_1240 in *P. putida* should be verified experimentally.

---

### Key References
- Wolf, Abad-Zapatero, Johnson, Fung. *Structures of SAICAR synthetase (PurC) from Streptococcus pneumoniae with ADP, Mg2+, AIR and Asp.* PMID **24598753**.
- Manjunath, Jeyakanthan, Sekar. *Catalytic pathway, substrate binding and stability in SAICAR synthetase: A structure and molecular dynamics study.* PMID **26072057**.
- Manjunath et al. *Structure of SAICAR synthetase from Pyrococcus horikoshii OT3.* PMID **23137517**.
- Bazurto, Heitman, Downs. *Aminoimidazole Carboxamide Ribotide ... Thiamine Synthesis in Salmonella enterica.* PMID **26100042**.
- He, Shiau, Choi, Zalkin, Smith. *Genes of the E. coli pur regulon are negatively controlled by a repressor-operator interaction.* PMID **2198266**.
- Škerlová et al. *Crystal structures of human PAICS...* PMID **32571877**.
- UniProtKB Q88NG9 (PUR7_PSEPK); HAMAP rule MF_00137.


## Artifacts

- [OpenScientist final report](purC-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](purC-deep-research-openscientist_artifacts/final_report.pdf)