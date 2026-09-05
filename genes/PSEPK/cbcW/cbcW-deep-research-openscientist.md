---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-13T05:30:07.267941'
end_time: '2026-08-13T05:57:34.483594'
duration_seconds: 1647.22
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: cbcW
  gene_symbol: cbcW
  uniprot_accession: Q88R39
  protein_description: 'SubName: Full=Choline / betaine / carnitine ABC transporter-membrane
    subunit {ECO:0000313|EMBL:AAN65926.1}; EC=3.6.3.32 {ECO:0000313|EMBL:AAN65926.1};'
  gene_info: Name=cbcW {ECO:0000313|EMBL:AAN65926.1}; OrderedLocusNames=PP_0295 {ECO:0000313|EMBL:AAN65926.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the binding-protein-dependent transport system
  protein_domains: ABC_transptr_choline_permease. (IPR017784); MetI-like. (IPR000515);
    MetI-like_sf. (IPR035906); BPD_transp_1 (PF00528)
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
citation_count: 3
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: cbcW-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: cbcW-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88R39
- **Protein Description:** SubName: Full=Choline / betaine / carnitine ABC transporter-membrane subunit {ECO:0000313|EMBL:AAN65926.1}; EC=3.6.3.32 {ECO:0000313|EMBL:AAN65926.1};
- **Gene Information:** Name=cbcW {ECO:0000313|EMBL:AAN65926.1}; OrderedLocusNames=PP_0295 {ECO:0000313|EMBL:AAN65926.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the binding-protein-dependent transport system
- **Key Domains:** ABC_transptr_choline_permease. (IPR017784); MetI-like. (IPR000515); MetI-like_sf. (IPR035906); BPD_transp_1 (PF00528)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "cbcW" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'cbcW' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **cbcW** (gene ID: cbcW, UniProt: Q88R39) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: cbcW (PP_0295, UniProt Q88R39) in *Pseudomonas putida* KT2440

## Summary

**cbcW (locus PP_0295; UniProt Q88R39) encodes the integral inner-membrane permease (translocation) subunit of the Cbc ATP-binding cassette (ABC) importer for quaternary ammonium compounds in *Pseudomonas putida* KT2440.** The protein is a 281-residue, highly hydrophobic polypeptide with six transmembrane helices that adopts the MetI-like ABC-importer permease fold. It is not itself an enzyme in the classical sense: although the EMBL/UniProt record carries EC 3.6.3.32, the ATP-hydrolysis chemistry that powers transport belongs to the partner nucleotide-binding subunit CbcV, while CbcW forms the membrane channel through which substrate is translocated. CbcW therefore functions as the conduit and conformational-coupling module of a Type I ABC importer.

The transporter's substrates are **choline, glycine betaine, and L-carnitine** — quaternary ammonium compounds that serve as osmoprotective compatible solutes and as carbon/nitrogen nutrient sources. A defining feature of the Cbc system, established biochemically in the closely related *Pseudomonas aeruginosa* and *P. syringae* orthologs, is that a single membrane core (permease CbcW + ATPase CbcV) recruits **multiple, interchangeable periplasmic substrate-binding proteins (SBPs)** that confer specificity: CbcX (choline, K<sub>m</sub> 2.6 µM; betaine, K<sub>m</sub> 24.2 µM), CaiX (L-carnitine, K<sub>m</sub> 24 µM), and BetX (betaine, K<sub>m</sub> 0.6 µM). In *P. putida* KT2440 the cbcX-cbcW-cbcV genes are arranged as a co-transcribed operon (PP_0296–PP_0295–PP_0294).

The functional assignment for the *P. putida* protein rests on strong homology-based inference: the KT2440 CbcW is **80.2% identical** to the experimentally characterized *P. aeruginosa* PAO1 CbcW over 278 aligned residues, both belonging to the same InterPro "ABC transporter choline permease" family (IPR017784). Physiologically, the choline imported by this system is oxidized by BetBA to glycine betaine, which is required in *P. putida* KT2440 for endurance to high salt and for use as a carbon or nitrogen source. The transporter thus sits at the entry point of the choline→glycine-betaine (*bet*) catabolic and osmoadaptive pathway. This report synthesizes sequence/structural evidence and the primary literature on the characterized orthologs to build a confident functional annotation, while transparently noting that direct biochemical characterization of the *P. putida* KT2440 protein itself has not been reported.

---

## Gene/Protein Identity Verification

Before presenting findings, the mandatory identity checks were completed and all passed:

| Check | Result |
|-------|--------|
| Gene symbol "cbcW" matches protein description? | **Yes** — UniProt Q88R39 describes a "Choline / betaine / carnitine ABC transporter-membrane subunit," consistent with *cbc* (choline/betaine/carnitine) transporter nomenclature. |
| Organism correct? | **Yes** — *Pseudomonas putida* strain ATCC 47054 / DSM 6125 / KT2440 (PSEPK, taxid 160488). |
| Protein family/domains align with literature? | **Yes** — InterPro IPR017784 (ABC_transptr_choline_permease), IPR000515/IPR035906 (MetI-like fold/superfamily), Pfam PF00528 (BPD_transp_1) all correspond to binding-protein-dependent ABC-importer permeases. |
| Literature refers to same gene? | **Yes** — the biochemically characterized Cbc system (Chen et al. 2010) is a choline/betaine/carnitine transporter from *Pseudomonas*; the KT2440 protein is an 80%-identical ortholog. |

The gene symbol is **not ambiguous** in this case, and the identity is secure. One nomenclature caveat: the same permease is annotated "choW" in some *Pseudomonas* genomes, but this is a synonym for the same choline-permease family and does not represent a different gene.

### Molecular identity at a glance

| Property | Value | Source |
|---|---|---|
| UniProt | Q88R39 | UniProtKB |
| Gene / locus | cbcW / PP_0295 | UniProtKB, EMBL AAN65926.1 |
| Length | 281 aa | UniProtKB |
| Transmembrane helices | 6 | UniProtKB features |
| Localization | Cytoplasmic (inner) membrane | UniProtKB keywords: Cell membrane, Transmembrane |
| Fold / superfamily | MetI-like ABC permease | InterPro IPR000515 / IPR035906 |
| Specific family | ABC transporter choline permease | InterPro IPR017784 |
| Pfam | PF00528 (BPD_transp_1) | UniProtKB |

---

## Key Findings

### Finding 1 — CbcW is the transmembrane permease subunit of the Cbc ABC importer

The core annotation, supported by convergent database and genomic evidence, is that **PP_0295/CbcW is the membrane-spanning permease of a binding-protein-dependent (Type I) ABC importer**. UniProt Q88R39 records a 281-amino-acid protein localized to the cell membrane with six transmembrane helices. Its domain architecture is diagnostic of an ABC-importer permease: InterPro IPR017784 specifically names the "ABC transporter choline permease" family, while IPR000515 and IPR035906 assign the protein to the **MetI-like permease fold and superfamily** — the structural class defined by the *E. coli* methionine-importer permease MetI. Pfam PF00528 (BPD_transp_1, "binding-protein-dependent transport system inner membrane component") reinforces this.

Genomic context in *P. putida* KT2440 is fully consistent with an operonic ABC transporter. The three genes are arranged head-to-tail:

```
PP_0296 (cbcX)  →  PP_0295 (cbcW)  →  PP_0294 (cbcV)
periplasmic SBP    membrane permease   ATP-binding subunit
315 aa             281 aa              392 aa
```

This is the canonical three-component minimal architecture of a bacterial ABC importer (SBP + permease + nucleotide-binding domain). The homologous *cbcXWV* operon was biochemically dissected in *P. syringae* and *P. aeruginosa* by Chen and colleagues, who showed that the periplasmic binding protein CbcX binds choline with high affinity (K<sub>m</sub> 2.6 µM) and also binds betaine (K<sub>m</sub> 24.2 µM), functionally defining the operon as a choline/betaine transporter [PMID: 19919675](https://pubmed.ncbi.nlm.nih.gov/19919675/):

> "The SBP encoded by the cbcXWV operon, CbcX, binds choline with a high affinity (K(m), 2.6 microM) and, although it also binds betaine (K(m), 24.2 microM), CbcXWV-mediated betaine uptake did not occur in the presence of choline."

Together these lines of evidence establish CbcW as the permease of the choline/betaine transporter operon.

### Finding 2 — The CbcWV core recruits multiple substrate-specific binding proteins, defining a broad quaternary-ammonium substrate range

A distinctive mechanistic feature of the Cbc transporter, and one of the most important for understanding CbcW's function, is that the **membrane core (permease CbcW + ATPase CbcV) is a shared translocation module that pairs with several different periplasmic SBPs**, each highly specific for a distinct quaternary ammonium compound. Chen et al. demonstrated that beyond the co-operonic CbcX (choline/betaine), the same CbcWV core interacts productively with the carnitine-specific CaiX (K<sub>m</sub> 24 µM) and the betaine-specific BetX (K<sub>m</sub> 0.6 µM) [PMID: 19919675](https://pubmed.ncbi.nlm.nih.gov/19919675/):

> "The core transporter CbcWV also interacts with the carnitine-specific SBP CaiX (K(m), 24 microM) and the betaine-specific SBP BetX (K(m), 0.6 microM)."

Notably, the *caiX* and *betX* genes are located elsewhere in the genome, physically separate from the *cbcXWV* operon, yet their products dock onto the same CbcWV permease/ATPase core. The authors summarize the design principle as the transporter's:

> "...use of multiple periplasmic substrate-binding proteins (SBPs) that are highly specific for their substrates."

This modularity has an important corollary for how CbcW's substrate specificity should be understood: **the permease itself does not select the substrate; specificity is imposed by the exchangeable SBP that delivers ligand to the periplasmic face of CbcW.** The system thus imports at least three physiologically important quaternary ammonium compounds — choline, glycine betaine, and L-carnitine — through one permease. The study also provided the first in vivo evidence that ligand-bound SBPs are preferentially engaged by the core transporter over ligand-free SBPs, indicating a substrate-loaded SBP is the productive docking partner.

The following table summarizes the SBP–substrate relationships characterized for the Cbc core:

| SBP | Genomic location | Substrate(s) | Affinity (K<sub>m</sub>) |
|-----|------------------|--------------|--------------------------|
| CbcX | *cbcXWV* operon (co-operonic) | Choline | 2.6 µM |
| CbcX | *cbcXWV* operon | Betaine | 24.2 µM |
| CaiX | Separate locus | L-carnitine | 24 µM |
| BetX | Separate locus | Glycine betaine | 0.6 µM |

### Finding 3 — Physiological role: entry point for osmoprotection and choline catabolism

The biological purpose of importing these substrates is to supply **compatible solutes for osmotic protection and nutrients for carbon/nitrogen metabolism**. In *P. putida* KT2440, choline that enters the cell (via the Cbc system) is oxidized to glycine betaine by the BetBA enzymes. Galvão and colleagues showed that the *betBA* genes are required both for the conversion of choline to the potent osmoprotectant glycine betaine — and hence for endurance to high salinity — and for the use of choline as a carbon or nitrogen source [PMID: 17116241](https://pubmed.ncbi.nlm.nih.gov/17116241/):

> "the betBA genes were required for choline transformation into the highly effective compatible solute glycine betaine (and the concomitant endurance to high salt) and also for its utilization as carbon or nitrogen source."

The Cbc transporter is the upstream gateway that makes this pathway possible: without import of the substrate, downstream oxidation and osmoadaptation cannot proceed. In the related pathogen *P. aeruginosa*, the same choline→glycine-betaine axis is medically relevant — choline catabolism supports bacterial survival during murine lung infection and induces the secreted virulence factor hemolytic phospholipase C (PlcH) through the transcriptional regulator GbdR [PMID: 23457628](https://pubmed.ncbi.nlm.nih.gov/23457628/). While *P. putida* KT2440 is a non-pathogenic soil/rhizosphere organism, the conserved biochemistry underscores the central metabolic importance of quaternary ammonium compound acquisition in the genus. In *P. putida* specifically, the relevant outputs are osmotolerance and the scavenging of plant/soil-derived quaternary amines as nutrients.

### Finding 4 — Sequence and topology are consistent with a MetI-like coupling permease

Independent sequence analysis corroborates the structural class. The Q88R39 sequence (281 aa) is strongly hydrophobic; Kyte-Doolittle hydropathy analysis (window 19) confirms extensive membrane-embedded character consistent with the UniProt-curated six transmembrane helices. The protein contains a cytoplasmic **coupling-helix region** — including a segment around residues ~190–205 (…SRRQLLTRIELPHAMP…) and a C-terminal element (…MLDRICKQPELPVRGEA) — that corresponds to the conserved "EAA loop" (L-loop) motif that binding-protein-dependent ABC permeases use to dock onto and transmit conformational signals to the nucleotide-binding domain (here CbcV). The fold is assigned to the MetI-like importer permease superfamily (InterPro IPR000515/IPR035906; SCOP MetI-type), Pfam PF00528. These features mark CbcW as a genuine translocation/coupling permease rather than a peripheral or regulatory membrane protein. The functional unit is expected to be a CbcW homodimer (6 + 6 = 12 transmembrane helices) undergoing alternating-access (outward-facing ↔ inward-facing) transitions.

### Finding 5 — 80% identity to the experimentally characterized *P. aeruginosa* CbcW justifies function transfer

Because no direct biochemical study of the KT2440 protein exists, the confidence of the functional annotation depends on the strength of orthology to a characterized protein. A Needleman-Wunsch global alignment of *P. putida* KT2440 CbcW (Q88R39, 281 aa) against *P. aeruginosa* PAO1 CbcW (Q9HTI7, 279 aa — the strain background used by Chen et al. 2010) gives **223/278 identical residues = 80.2% identity** over 278 aligned positions (79.9% over the shorter length). Both proteins are ~279–282 aa MetI-like members of the choline-permease family (IPR017784). This level of identity is far above the ~30–40% threshold generally regarded as sufficient for confident transfer of molecular function, and the alignment spans essentially the full length of both proteins with conserved membrane topology.

The characterized transporter is explicitly from *P. aeruginosa*/*P. syringae* [PMID: 19919675](https://pubmed.ncbi.nlm.nih.gov/19919675/):

> "We identified a choline, betaine and carnitine transporter, designated Cbc, from Pseudomonas syringae and Pseudomonas aeruginosa."

Genus-wide, this permease is broadly conserved (dozens of *Pseudomonas* orthologs annotated "choW"/"cbcW," ~279–282 aa, IPR017784), indicating a well-conserved, ancestral quaternary-ammonium uptake function. The homology therefore transfers with high confidence the conclusion that *P. putida* CbcW is the permease of a choline/betaine/carnitine ABC importer.

---

## Mechanistic Model / Interpretation

The findings assemble into a coherent mechanistic picture of a modular Type I ABC importer in which CbcW is the central translocation channel.

```
                          PERIPLASM
                 ┌───────────────────────────┐
   choline ─────►│  CbcX  (Km 2.6 µM)        │
   betaine ─────►│  CbcX/BetX (Km 24/0.6 µM) │  ← interchangeable
   L-carnitine ─►│  CaiX  (Km 24 µM)         │    substrate-binding
                 └──────────┬────────────────┘    proteins (SBPs)
                            │ ligand-loaded SBP docks
 ════════════════╦═════════▼═════════╦════════════ INNER MEMBRANE
                 ║   CbcW  (PP_0295)  ║   6 TM helices, MetI-like fold
                 ║  permease channel  ║   ← THIS PROTEIN
 ════════════════╩═════════▲═════════╩════════════
                            │ coupling helix / EAA loop
                       ┌────┴────┐
                       │  CbcV   │  (PP_0294) ATP-binding subunit
                       │  ATPase │  hydrolyzes ATP → power stroke
                       └────┬────┘
                            ▼
                          CYTOPLASM
              imported choline/betaine/carnitine
                            │
                     BetBA oxidation
                            ▼
                   GLYCINE BETAINE
              ┌─────────────┴─────────────┐
       osmoprotection            C / N nutrient source
       (salt endurance)          (catabolism)
```

**Reaction/transport logic.** A quaternary ammonium compound in the periplasm is captured by a soluble SBP with the appropriate specificity. The ligand-loaded SBP preferentially docks onto the periplasmic face of the CbcW permease. ATP binding and hydrolysis by the cytoplasmic CbcV dimer drives conformational cycling of CbcW between outward- and inward-facing states, translocating the substrate across the inner membrane into the cytoplasm. The nominal EC number 3.6.3.32 (ABC-type quaternary-amine transporter, ATP-hydrolysis-coupled) describes the transport reaction of the complete complex; the chemical bond-breaking (ATP hydrolysis) resides in CbcV, whereas CbcW provides the membrane pathway and the coupling helices that mechanically link ATPase motion to gate opening.

**Substrate specificity is delegated.** The single most important conceptual point is that CbcW does not itself discriminate among choline, betaine, and carnitine. Specificity is set by which SBP delivers the substrate. This "one core, many SBPs" architecture lets *Pseudomonas* scavenge a chemically related family of osmolytes/nutrients economically, using one permease/ATPase pair. Consequently, the correct functional description of CbcW is "permease of a broad-specificity quaternary ammonium ABC importer," not "choline-specific permease."

**Localization.** CbcW carries out its function in the cytoplasmic (inner) membrane. Its partner SBPs act in the periplasm; CbcV acts on the cytoplasmic face. The physiological consequences (osmoadaptation, choline catabolism) play out in the cytoplasm downstream of import.

**Pathway placement.** CbcW is the committed uptake step upstream of the *bet* pathway. Imported choline → glycine betaine (via BetBA) serves two fates: accumulation as a compatible solute for salt/osmotic stress endurance, and catabolic breakdown as a carbon/nitrogen source. In pathogenic relatives, the same axis feeds GbdR-dependent virulence regulation, but in *P. putida* the relevant outputs are osmoprotection and nutrient assimilation.

---

## Evidence Base

| PMID | Title (abbrev.) | Organism | How it supports the annotation |
|------|-----------------|----------|-------------------------------|
| [19919675](https://pubmed.ncbi.nlm.nih.gov/19919675/) | *The ABC transporter Cbc recruits multiple substrate-binding proteins…* | *P. aeruginosa* / *P. syringae* | **Primary, decisive.** Defines the CbcWV core as a choline/betaine/carnitine transporter, gives SBP affinities (CbcX 2.6 µM choline; CaiX 24 µM carnitine; BetX 0.6 µM betaine), and establishes the modular SBP mechanism. Basis for Findings 1, 2, 5. |
| [17116241](https://pubmed.ncbi.nlm.nih.gov/17116241/) | *Uncoupling of choline-O-sulphate utilization from osmoprotection in P. putida* | ***P. putida* KT2440** | **Same-organism physiology.** Shows imported choline is converted to glycine betaine by BetBA, required for salt endurance and for use as C/N source. Basis for Finding 3 (downstream fate in the target organism). |
| [23457628](https://pubmed.ncbi.nlm.nih.gov/23457628/) | *Choline catabolism to glycine betaine contributes to P. aeruginosa survival…* | *P. aeruginosa* | Contextual. Demonstrates the medical/physiological importance of the choline→betaine axis fed by Cbc-type uptake; induces PlcH via GbdR. Supports Finding 3's pathway significance. |
| [23667230](https://pubmed.ncbi.nlm.nih.gov/23667230/) | *Anr and its activation by PlcH activity…* | *P. aeruginosa* | Contextual. Links choline/glycine-betaine catabolism to Anr-regulated physiology and virulence, illustrating the downstream regulatory reach of the pathway. |
| [28791946](https://pubmed.ncbi.nlm.nih.gov/28791946/) | *P. aeruginosa gbdR transcribed from σ54 promoter under NtrC/CbrB, IHF, BetI* | *P. aeruginosa* | Contextual. Describes regulatory integration (carbon/nitrogen status via CbrB/NtrC) of the choline-catabolic regulon that the Cbc transporter feeds. |

**Strength of the evidence.** The molecular identity and mechanism of CbcW rest primarily on one rigorous, low-throughput biochemical study of the orthologous system (PMID 19919675) combined with strong sequence homology (80% identity). The same-organism paper (PMID 17116241) anchors the downstream physiology directly in *P. putida* KT2440. The remaining papers are pathogenesis-focused and provide corroborating pathway context rather than direct evidence about CbcW itself. No study contradicts the annotation.

---

## Supported vs. Refuted Hypotheses

- **Supported:** CbcW is the transmembrane permease of a Type I binding-protein-dependent ABC importer for quaternary ammonium compounds (choline / glycine betaine / L-carnitine); it acts at the inner membrane together with the ATPase CbcV and periplasmic SBPs; imported substrate feeds osmoprotection and catabolism via the *bet* pathway.
- **Refuted / corrected:** CbcW is *not* itself a hydrolase/enzyme despite the transferred EC 3.6.3.32 label — the ATP-hydrolysis activity belongs to CbcV. CbcW has no known function outside the assembled transporter complex.

---

## Limitations and Knowledge Gaps

1. **No direct biochemical characterization of the *P. putida* KT2440 protein.** The functional assignment is inferred from an 80%-identical *P. aeruginosa* ortholog. Although this is a high-confidence inference, transport kinetics, substrate range, and SBP partnerships have not been measured for the KT2440 CbcW specifically.

2. **SBP repertoire in KT2440 not experimentally mapped.** CbcX is co-operonic (PP_0296), but whether *P. putida* KT2440 encodes functional CaiX and BetX orthologs that engage this specific CbcWV core — and thus whether the KT2440 system imports carnitine and betaine as efficiently as choline — remains to be confirmed experimentally in this strain.

3. **EC number nuance.** The record carries EC 3.6.3.32 (an ATP-hydrolysis-coupled transport activity). This describes the holo-transporter; CbcW itself has no catalytic ATPase activity. Treating CbcW as an "enzyme" per se would be misleading — it is the permease/channel component.

4. **No experimental structure.** The MetI-like fold and six-TM topology are assigned from InterPro/Pfam and hydropathy analysis, not from a solved structure. Coupling-helix (EAA-loop) positions are inferred from sequence motifs.

5. **Regulation in KT2440 not detailed.** How *cbcXWV* expression is controlled in *P. putida* (e.g., by osmolarity, choline availability, or global C/N regulators such as CbrB/NtrC) was characterized in *P. aeruginosa* contexts, not directly for the KT2440 operon.

---

## Proposed Follow-up Experiments / Actions

1. **Targeted uptake assays in KT2440.** Construct a *cbcW* (PP_0295) deletion mutant and measure radiolabeled choline, glycine betaine, and L-carnitine uptake versus wild type to directly confirm substrate range and the permease's essentiality for transport in this strain.

2. **SBP complementation panel.** Clone and purify candidate KT2440 SBPs (CbcX/PP_0296 plus genomic CaiX/BetX orthologs) and test which reconstitute transport through the CbcWV core, quantifying K<sub>m</sub>/K<sub>d</sub> to establish the strain-specific specificity map.

3. **Structural modeling and cryo-EM.** Generate an AlphaFold model of CbcW (and the CbcWV/CbcX complex), validate the six-TM MetI-like fold, pinpoint the coupling helices/EAA-loop residues that contact CbcV, and pursue cryo-EM of the assembled CbcWV core.

4. **Osmostress phenotyping.** Test growth of Δ*cbcW* under high-salt conditions with choline/betaine/carnitine as the sole osmoprotectant to link the transporter directly to salt endurance in KT2440, complementing the established *betBA* phenotype.

5. **Expression/regulation profiling.** Use qRT-PCR or reporter fusions to determine whether *cbcXWV* transcription responds to osmolarity, substrate availability, and C/N status (CbrB/NtrC), clarifying how uptake is integrated with the *bet* catabolic regulon.

---

## Conclusion

*cbcW* (PP_0295, Q88R39) encodes the inner-membrane permease subunit of the Cbc ABC importer in *Pseudomonas putida* KT2440 — a 281-residue, six-transmembrane-helix, MetI-like translocation channel that, together with the ATPase CbcV and interchangeable periplasmic binding proteins (co-operonic CbcX plus separately encoded CaiX and BetX), imports the quaternary ammonium compounds choline, glycine betaine, and L-carnitine across the cytoplasmic membrane. Substrate specificity is delegated to the exchangeable binding proteins rather than to the permease itself, and the imported solutes feed osmoprotection (as compatible solutes) and carbon/nitrogen catabolism via the choline→glycine-betaine (*bet*) pathway. This annotation is assigned with high confidence based on 80% sequence identity to the experimentally characterized *P. aeruginosa* CbcW, conserved domain architecture, and same-organism physiological evidence for the downstream pathway.

---

*Key references: PMID 19919675 (Chen et al. 2010, *Mol. Microbiol.*), PMID 17116241 (Galvão et al. 2006), PMID 23457628 (Wargo 2013), PMID 23667230, PMID 28791946; UniProt Q88R39; InterPro IPR017784/IPR000515/IPR035906; Pfam PF00528.*


## Artifacts

- [OpenScientist final report](cbcW-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](cbcW-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:19919675
2. PMID:17116241
3. PMID:23457628