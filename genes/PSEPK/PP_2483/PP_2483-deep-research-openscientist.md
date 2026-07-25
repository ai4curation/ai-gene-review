---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-20T20:19:30.361972'
end_time: '2026-07-20T20:45:56.028007'
duration_seconds: 1585.67
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_2483
  gene_symbol: PP_2483
  uniprot_accession: Q88K10
  protein_description: 'RecName: Full=MobA-like NTP transferase domain-containing
    protein {ECO:0000259|Pfam:PF12804};'
  gene_info: OrderedLocusNames=PP_2483 {ECO:0000313|EMBL:AAN68095.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: MobA-like_NTP_Trfase. (IPR025877); Nucleotide-diphossugar_trans.
    (IPR029044); NTP_transf_3 (PF12804)
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
  path: PP_2483-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PP_2483-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88K10
- **Protein Description:** RecName: Full=MobA-like NTP transferase domain-containing protein {ECO:0000259|Pfam:PF12804};
- **Gene Information:** OrderedLocusNames=PP_2483 {ECO:0000313|EMBL:AAN68095.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** MobA-like_NTP_Trfase. (IPR025877); Nucleotide-diphossugar_trans. (IPR029044); NTP_transf_3 (PF12804)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_2483" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_2483' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_2483** (gene ID: PP_2483, UniProt: Q88K10) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of PP_2483 (UniProt Q88K10) in *Pseudomonas putida* KT2440

## 1. Summary — Answer to the Research Question

**PP_2483 (Q88K10) is a MobA-superfamily nucleotidyltransferase, specifically a MocA-type CTP:molybdopterin cytidylyltransferase (EC 2.7.7.76).** Its primary function is to catalyze the Mg²⁺-dependent, CTP-specific transfer of a cytidylyl (CMP) group onto the C4′ terminal phosphate of molybdopterin (Mo‑MPT), producing the **molybdopterin cytosine dinucleotide (MCD)** form of the molybdenum cofactor plus pyrophosphate. It acts in the **cytoplasm** as a biosynthetic (cofactor-maturation) enzyme. Genomic context pinpoints its physiological purpose: PP_2483 lies in a self-contained gene cluster (PP_2477–PP_2483) that also encodes an **isoquinoline 1-oxidoreductase** (PP_2477/PP_2478; a xanthine-oxidase-family molybdo-hydroxylase experimentally shown to carry the MCD cofactor), an **XdhC-type MCD-insertion chaperone** (PP_2480), and the Moco-biosynthesis enzyme **MoaA** (PP_2482) — so PP_2483 supplies the MCD cofactor that activates this local molybdo-hydroxylase, contributing to N-heterocyclic aromatic compound catabolism. The identification rests on domain architecture, orthology (KEGG K07141), paralog discrimination, this operonic context with a genuine MCD enzyme, and homology to biochemically characterized *E. coli* MocA.

> ⚠️ **Identity/evidence note:** Q88K10 is a TrEMBL (computationally annotated, unreviewed) entry and there is **no primary experimental study of PP_2483 itself**. The functional call is an *inference* from orthology, conserved domains, genomic context, and experimentally characterized homologs (chiefly *E. coli* MocA). It should be regarded as a high-confidence prediction, not a directly demonstrated activity.

---

## 2. Protein at a Glance

| Property | Value |
|---|---|
| UniProt | Q88K10 (Q88K10_PSEPK), **unreviewed/TrEMBL** |
| Gene / locus | PP_2483 (ordered locus name); GenBank AAN68095; RefSeq WP_010953419.1 |
| Organism | *Pseudomonas putida* KT2440 (taxid 160488) |
| Length / mass | 199 aa / 21.2 kDa |
| Genomic position | complement(2,830,343..2,830,942) |
| Domain | MobA-like NTP transferase (Pfam PF12804, res. 12–171) |
| Fold | Nucleotide-diphospho-sugar transferase / SpsA-like (SUPFAM SSF53448; Gene3D 3.90.550.10; CDD cd04182 "GT_2_like_f") |
| InterPro | IPR025877 (MobA-like NTP transferase); IPR029044 (Nucleotide-diphospho-sugar transferases superfamily) |
| Orthology | KEGG **K07141** = molybdenum cofactor cytidylyltransferase, **EC 2.7.7.76**; eggNOG **COG2068** |
| GO | GO:0016779 (nucleotidyltransferase activity) |
| Cofactor | Mg²⁺ (UniProt "Magnesium" keyword) |
| Predicted localization | Cytoplasm (no signal peptide / transmembrane segment) |

---

## 3. Key Findings and Evidence

### 3.1 The protein is a Mg²⁺-dependent nucleotidyltransferase of the MobA-like superfamily
- The single structural domain (res. 12–171) is a MobA-like NTP transferase domain (Pfam PF12804), belonging to the nucleotide-diphospho-sugar transferase / SpsA-like fold (SSF53448, Gene3D 3.90.550.10). The GO annotation is nucleotidyltransferase activity (GO:0016779).
- The N-terminus carries the canonical nucleotidyltransferase phosphate-binding motif (…G‑L‑V‑L‑A‑A‑G‑**T**‑G‑Q‑**R**…), which in this superfamily binds the α-phosphate of the incoming NTP and coordinates a catalytic Mg²⁺ — consistent with the UniProt Magnesium ligand keyword.
- **Bioinformatic/evolutionary evidence.** This superfamily (MobA, MocA, GlmU, RmlA, IspD, sugar-1-P nucleotidyltransferases) shares a common fold and mechanism: NTP + acceptor-phosphate → NDP/NMP-acceptor + PPi.

### 3.2 Orthology and paralog discrimination pin the substrate to CTP + molybdopterin (MocA, EC 2.7.7.76), not GTP (MobA, EC 2.7.7.77)
- KEGG assigns PP_2483 to **K07141 (molybdenum cofactor cytidylyltransferase, EC 2.7.7.76)**.
- Critically, the *guanylyl*-transferring paralog **MobA (K03752, EC 2.7.7.77)** is encoded by a **separate** KT2440 gene, **PP_3457**. Because the two activities are catalyzed by distinct, nucleotide-specific paralogs (~22 % identity), the presence of a dedicated MobA elsewhere in the genome supports PP_2483 being the **cytidylyl** (MocA) branch (a second K07141 paralog, PP_4230, also exists).
- In the characterized *E. coli* system, MocA is strictly CTP-specific (ATP and GTP are not used) and requires Mg²⁺, and the two paralogs differ functionally by two sub-domains: the **N-terminal domain dictates nucleotide (C vs G) specificity**, while the **C-terminal domain dictates which acceptor molybdoenzyme is bound** (Neumann et al., 2009, PMID 19542235; Neumann et al., 2011, PMID 21081498).

### 3.3 Reaction catalyzed
$$\text{CTP} + \text{Mo-molybdopterin} \;\xrightarrow[\text{Mg}^{2+}]{\text{PP\_2483 (MocA)}}\; \text{molybdopterin cytosine dinucleotide (MCD)} + \text{PP}_i$$
- Substrate specificity: donor = **CTP** (specific); acceptor = **Mo‑MPT** (molybdenum-loaded molybdopterin); essential metal = **Mg²⁺**. (By homology to *E. coli* MocA: K_d ≈ 0.23 µM for CTP, ≈ 1.2 µM for Mo‑MPT; k_cat ≈ 0.37 min⁻¹.)

### 3.4 Genomic context identifies the specific downstream molybdoenzyme: an isoquinoline 1-oxidoreductase
PP_2483 sits at the end of a complete, self-contained molybdo-hydroxylase gene cluster (PP_2477–PP_2483) that encodes both a xanthine-oxidase-family enzyme **and** its dedicated cofactor-biosynthesis/maturation machinery:

| Gene | Product | Role |
|---|---|---|
| **PP_2477** | Isoquinoline 1-oxidoreductase **α** subunit (K07302, EC 1.3.99.16; Pfam Fer2/Fer2_2) | [2Fe-2S] electron-transfer subunit |
| **PP_2478** | Isoquinoline 1-oxidoreductase **β** subunit (K07303, EC 1.3.99.16; Pfam **MoCoBD** + Ald_Xan_dh_C) | Molybdopterin (MCD)-binding catalytic subunit |
| **PP_2480** | **XdhC-family** accessory factor (Pfam XdhC_C, XdhC_CoxI) | MCD sulfuration + insertion chaperone |
| **PP_2482** | **MoaA / GTP 3′,8-cyclase** (K03639, EC 4.1.99.22) | First committed step of Moco biosynthesis |
| **PP_2483** | **MocA cytidylyltransferase** (this gene) | Synthesizes the MCD cofactor |

**Isoquinoline 1-oxidoreductase (IOR) is an experimentally established MCD enzyme.** Purified IOR from *Pseudomonas / Brevundimonas diminuta* is a molybdenum hydroxylase containing **1 mol CMP per enzyme**, molybdenum, and two [2Fe-2S] clusters, with the CMP originating from a **molybdopterin cytosine dinucleotide (MCD)** cofactor (Lehmann et al., 1994, PMID 8157655; Canne et al., 1997, PMID 9245410; Israel et al., 2002, PMID 12023088). XdhC-type chaperones (as encoded by PP_2480) are specifically required to sulfurate and insert MCD into xanthine-oxidase-family apoenzymes (Neumann & Leimkühler, 2011, PMID 21151514).

**Therefore the biological role of PP_2483 is to synthesize the MCD cofactor for the co-operonic isoquinoline 1-oxidoreductase (PP_2477/PP_2478),** a molybdo-hydroxylase that hydroxylates isoquinoline to 1-oxo-1,2-dihydroisoquinoline — linking PP_2483 to catabolism of N-heterocyclic aromatic compounds. This dedicated co-localization with a genuine MCD enzyme is decisive evidence for the cytidylyl (MCD/MocA) assignment over the guanylyl (MobA) alternative.

**Confirming the acceptor-specific "one MocA per molybdoenzyme operon" architecture.** KT2440 encodes a second MocA/K07141 paralog, **PP_4230**, which lies in its *own* independent molybdo-hydroxylase operon: PP_4231 (XdhC accessory factor, K07402), PP_4232 (cytochrome c), PP_4233 ([2Fe-2S] small oxidoreductase subunit), and **PP_4234 (aldehyde oxidase / xanthine dehydrogenase, large MoCoBD subunit)**. Thus each of the two Pseudomonas MocA paralogs is co-encoded with a distinct xanthine-oxidase-family molybdoenzyme and its own XdhC chaperone. This parallel genomic architecture is direct evidence for **dedicated, acceptor-specific MCD delivery** — matching the biochemical finding that the MocA C-terminal domain determines binding to its specific acceptor protein (Neumann et al., 2011, PMID 21081498) — and pins **PP_2483 to the isoquinoline 1-oxidoreductase** while PP_4230 serves the aldehyde oxidase/xanthine dehydrogenase.

### 3.4b Caveat — nucleotide specificity is NOT assignable from global sequence identity
Needleman-Wunsch global identity: PP_2483 is actually closer to *E. coli* **MobA** (34.3%) than to *E. coli* **MocA** (25.3%), while *E. coli* MobA vs MocA share only 24.2%, and PP_2483 vs its paralog PP_4230 = 48.1%. Because C- vs G-selectivity is dictated by a few N-terminal active-site residues rather than by overall identity (Neumann et al., 2011, PMID 21081498), the higher global similarity to MobA does **not** imply guanylyl specificity. The cytidylyl (MCD) assignment rests on orthology (KEGG K07141) **plus** the functional/genomic context above, not on sequence identity — this is an inference and should be experimentally confirmed.

### 3.5 Localization
- Molybdenum-cofactor and MCD biosynthesis are cytoplasmic processes; the 199-aa protein has no predicted signal peptide or transmembrane helix, consistent with a **soluble cytoplasmic** enzyme. (Inference; no experimental localization data exist for PP_2483.)

---

## 4. Pathway Context
- **Pathway:** Molybdenum cofactor (Moco) biosynthesis → molybdopterin *dinucleotide* branch. Upstream: MoaA→MoaC→MoaD/MoaE (cPMP → MPT), MogA/MoeA (Mo insertion → Mo‑MPT). PP_2483 (MocA) then adds CMP to Mo‑MPT to yield **MCD**, which is delivered by an XdhC-type chaperone to apo-molybdoenzymes of the xanthine oxidase family. (KEGG maps this branch under ppu00790 "folate biosynthesis," the map that also houses molybdopterin biosynthesis.)
- **Downstream physiology:** the MCD product is inserted (via XdhC PP_2480) into the co-encoded isoquinoline 1-oxidoreductase (PP_2477/PP_2478), which hydroxylates isoquinoline to 1-oxo-1,2-dihydroisoquinoline (EC 1.3.99.16). This links PP_2483 to catabolism of N-heterocyclic aromatic compounds in this metabolically versatile soil bacterium. A second MocA paralog (PP_4230) likely serves a different molybdoenzyme.

---

## 5. Supported and Refuted Hypotheses

| Hypothesis | Verdict | Basis |
|---|---|---|
| Member of MobA-like NTP-transferase superfamily; Mg²⁺-dependent nucleotidyltransferase | **Supported** | Pfam PF12804, SSF53448, GO:0016779, Mg keyword, N-terminal motif |
| Specifically a CTP:molybdopterin **cytidylyltransferase (MocA, EC 2.7.7.76)** producing MCD | **Supported (high-confidence inference)** | KEGG K07141; distinct MobA gene (PP_3457) present; operonic with a genuine MCD enzyme (isoquinoline 1-oxidoreductase) + XdhC chaperone |
| PP_2483 supplies MCD specifically to the co-encoded **isoquinoline 1-oxidoreductase** (PP_2477/PP_2478) | **Supported (strong inference)** | Operon structure; IOR shown to contain MCD (PMID 8157655/9245410/12023088); XdhC PP_2480 present |
| Cytidylyl specificity can be read from global sequence identity to MobA/MocA | **Refuted** | PP_2483 is closer to *E. coli* MobA (34%) than MocA (25%); specificity is set by local residues, not global identity |
| It is the MobA **guanylyltransferase (EC 2.7.7.77)** | **Refuted** | MobA/K03752 is a separate gene (PP_3457) |
| It is a sugar-1-phosphate nucleotidyltransferase (NDP-sugar biosynthesis) | **Refuted / unlikely** | Orthology + Moco/molybdoenzyme genomic context favor MCD biosynthesis over sugar-nucleotide metabolism |
| Cytoplasmic, soluble enzyme | **Supported (inference)** | No signal/TM; Moco biosynthesis is cytoplasmic |

---

## 6. Limitations and Future Directions
- **No direct experimental data** exist for PP_2483; the annotation is inferred from orthology, conserved domains, genomic context, and characterized homologs. Q88K10 is an unreviewed TrEMBL entry.
- KEGG K07141 is an automated ortholog assignment; two KT2440 paralogs (PP_2483, PP_4230) carry it. Operon structure assigns PP_2483 to the isoquinoline 1-oxidoreductase (PP_2477/PP_2478) and PP_4230 to the aldehyde oxidase/xanthine dehydrogenase (PP_4233/PP_4234), but the acceptor specificity of each MocA (set by its C-terminal domain) has not been experimentally verified in *P. putida*.
- The isoquinoline 1-oxidoreductase MCD evidence derives from orthologous enzymes in *Pseudomonas/Brevundimonas diminuta*; the KT2440 IOR (PP_2477/PP_2478) itself has not been directly shown to carry MCD, though its MoCoBD/Ald_Xan_dh_C domain architecture and operon are diagnostic.
- **Recommended experiments:** (i) in-vitro reconstitution (MocA + Mo‑MPT + CTP + Mg²⁺ → MCD) to confirm cytidylyltransferase activity and CTP specificity; (ii) ΔPP_2483 phenotyping for loss of isoquinoline 1-oxidoreductase activity / isoquinoline degradation; (iii) AlphaFold model + active-site residue mapping against MobA/MocA structures to verify the cytosine-selecting N-terminal motif; (iv) confirm the dedicated PP_2483→IOR versus PP_4230→aldehyde oxidase acceptor pairing (e.g., cross-complementation).

---

## 7. Key References
- Lehmann M., Tshisuaka B., Fetzner S., Röger P., Lingens F. **Purification and characterization of isoquinoline 1-oxidoreductase from *Pseudomonas diminuta* 7, a novel molybdenum-containing hydroxylase.** *J Biol Chem* 1994. PMID **8157655**. (IOR contains MCD: 1 mol CMP/enzyme.)
- Canne C. *et al.* **Comparative EPR and redox studies of three prokaryotic enzymes of the xanthine oxidase family… isoquinoline 1-oxidoreductase.** *Eur J Biochem* 1997. PMID **9245410**.
- Israel I., Sohni M., Fetzner S. **Expression of the iorAB genes … encoding the molybdenum hydroxylase isoquinoline 1-oxidoreductase in *Pseudomonas putida*.** 2002. PMID **12023088**.
- Neumann M., Leimkühler S. **The role of system-specific molecular chaperones in the maturation of molybdoenzymes in bacteria.** 2011. PMID **21151514**. (XdhC-family MCD insertion.)
- Neumann M., Mittelstädt G., Seduk F., Iobbi-Nivol C., Leimkühler S. **MocA is a specific cytidylyltransferase involved in molybdopterin cytosine dinucleotide biosynthesis in *Escherichia coli*.** *J Biol Chem* 2009. PMID **19542235**.
- Neumann M., Seduk F., Iobbi-Nivol C., Leimkühler S. **Molybdopterin dinucleotide biosynthesis in *E. coli*: amino acid residues of molybdopterin dinucleotide transferases that determine specificity for guanine or cytosine nucleotides.** *J Biol Chem* 2011. PMID **21081498**.
- Belda E. *et al.* **The revisited genome of *Pseudomonas putida* KT2440 enlightens its value as a robust metabolic chassis.** *Environ Microbiol* 2016. PMID **26913973**.
- Database sources: UniProt Q88K10; KEGG ppu:PP_2483 (K07141, EC 2.7.7.76); InterPro IPR025877/IPR029044; Pfam PF12804; eggNOG COG2068.


## Artifacts

- [OpenScientist final report](PP_2483-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PP_2483-deep-research-openscientist_artifacts/final_report.pdf)