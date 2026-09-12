---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-17T05:28:29.732166'
end_time: '2026-07-17T05:41:43.588046'
duration_seconds: 793.86
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: hisB
  gene_symbol: hisB
  uniprot_accession: Q88R45
  protein_description: 'RecName: Full=Imidazoleglycerol-phosphate dehydratase {ECO:0000255|HAMAP-Rule:MF_00076};
    Short=IGPD {ECO:0000255|HAMAP-Rule:MF_00076}; EC=4.2.1.19 {ECO:0000255|HAMAP-Rule:MF_00076};'
  gene_info: Name=hisB {ECO:0000255|HAMAP-Rule:MF_00076}; OrderedLocusNames=PP_0289;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the imidazoleglycerol-phosphate dehydratase
  protein_domains: IGPD_sf. (IPR038494); ImidazoleglycerolP_deHydtase. (IPR000807);
    ImidazoleglycerP_deHydtase_CS. (IPR020565); Ribosomal_Su5_D2-typ_SF. (IPR020568);
    IGPD (PF00475)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
    save_artifacts: true
    artifact_max_bytes: 5242880
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: hisB-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: hisB-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88R45
- **Protein Description:** RecName: Full=Imidazoleglycerol-phosphate dehydratase {ECO:0000255|HAMAP-Rule:MF_00076}; Short=IGPD {ECO:0000255|HAMAP-Rule:MF_00076}; EC=4.2.1.19 {ECO:0000255|HAMAP-Rule:MF_00076};
- **Gene Information:** Name=hisB {ECO:0000255|HAMAP-Rule:MF_00076}; OrderedLocusNames=PP_0289;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the imidazoleglycerol-phosphate dehydratase
- **Key Domains:** IGPD_sf. (IPR038494); ImidazoleglycerolP_deHydtase. (IPR000807); ImidazoleglycerP_deHydtase_CS. (IPR020565); Ribosomal_Su5_D2-typ_SF. (IPR020568); IGPD (PF00475)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "hisB" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'hisB' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **hisB** (gene ID: hisB, UniProt: Q88R45) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of *hisB* (Q88R45, PP_0289) in *Pseudomonas putida* KT2440

**Gene:** hisB | **Locus:** PP_0289 | **UniProt:** Q88R45
**Protein:** Imidazoleglycerol-phosphate dehydratase (IGPD), EC 4.2.1.19
**Organism:** *Pseudomonas putida* strain ATCC 47054 / DSM 6125 / KT2440 (PSEPK)

---

## 1. Summary (Answer to the Research Question)

*hisB* (PP_0289) encodes **imidazoleglycerol-phosphate dehydratase (IGPD; EC 4.2.1.19)**, a cytoplasmic, manganese(II)-dependent hydro-lyase that catalyzes the **sixth step of the nine-step L-histidine biosynthetic pathway**. It removes water from D-*erythro*-1-(imidazol-4-yl)glycerol 3-phosphate (imidazoleglycerol phosphate, IGP) to yield 3-(imidazol-4-yl)-2-oxopropyl phosphate (imidazoleacetol phosphate, IAP). In *P. putida* the enzyme is the **monofunctional** form (197 aa, a single IGPD/PF00475 domain), in contrast to the bifunctional HisB of *Escherichia coli*; the downstream histidinol-phosphate phosphatase activity is supplied by a **separate gene, PP_3157**. The enzyme operates in the bacterial cytosol and, because the histidine pathway is absent in mammals, IGPD is a validated herbicide/antimicrobial target.

**Gene-identity verification:** CONFIRMED. UniProt Q88R45 (hisB/PP_0289, 197 aa, single IGPD domain, EC 4.2.1.19, cytoplasm) matches KEGG ppu:PP_0289 (K01693, IGPD) and the family/domain signatures (IPR000807, IPR020565, PF00475). All identifiers are internally consistent; there is no gene-symbol ambiguity for this protein.

---

## 2. Primary Function: Reaction Catalyzed and Substrate Specificity

**Reaction (EC 4.2.1.19):**

> D-*erythro*-1-(imidazol-4-yl)glycerol 3-phosphate → 3-(imidazol-4-yl)-2-oxopropyl phosphate + H₂O

This is a **dehydration (hydro-lyase)** reaction: elimination of the C-2′ hydroxyl (as water) from the glycerol-phosphate side chain of the imidazole substrate. The product, imidazoleacetol phosphate, is subsequently transaminated by histidinol-phosphate aminotransferase (HisC/PP_0967) to histidinol phosphate.

**Substrate specificity.** IGPD is highly specific for its physiological substrate IGP; recognition is dominated by the imidazole ring, which is anchored between the two active-site Mn(II) ions, while the phosphate and hydroxyl groups are held by a network of conserved basic and acidic residues. In the *Mycobacterium tuberculosis* IGPD–IGP complex the substrate contacts Glu21, Arg99, Glu180, Arg121 and Lys184 contributed by three different protomers (Ahangar et al., 2013, PMID 24311587). The imidazole-focused recognition also explains inhibition by the imidazole/triazole mimic **3-amino-1,2,4-triazole (ATZ)**, which is a competitive inhibitor (PMID 24311587), and by triazole-phosphonate herbicides (Glynn et al., 2005, PMID 16338409).

**Cofactor requirement.** IGPD is a **Mn(II) metalloenzyme**; two manganese ions per active site are essential both for catalysis and for assembly of the functional oligomer (PMID 16338409).

---

## 3. Catalytic Mechanism (Structural/Mechanistic Evidence)

Although no *P. putida* IGPD structure has been solved, the mechanism is well established from high-resolution structures of orthologs that share the same fold and conserved residues:

- **Quaternary structure:** The active enzyme is a **24-mer with 432 point-group symmetry**, containing **24 equivalent active sites**, each built at the interface of three protomers. Assembly of the 24-mer from an inactive trimeric precursor is triggered by formation of a **dimanganese cluster** (*Arabidopsis thaliana* IGPD; Glynn et al., 2005, PMID 16338409). The same 24-meric architecture was confirmed for *M. tuberculosis* IGPD (PMID 24311587).

- **Chemical mechanism:** The substrate's imidazole ring binds between the two Mn(II) ions as an **imidazolate**, which collapses to a high-energy **diazafulvene intermediate**; this activation enables elimination of water (PMID 16338409). Trapped catalytic-cycle snapshots of an inactive IGPD2 mutant show that substrate binding **switches an active-site Mn(II) between six- and five-coordinate states**, priming the site and facilitating the imidazolate intermediate (Bisson et al., 2015, PMID 26095028). This is a striking example of a metalloenzyme using controlled metal-coordination changes to drive discrete catalytic steps.

- **Evolutionary/bioinformatic support for the P. putida enzyme:** The 197-aa Q88R45 sequence contains the **two internally homologous, His-rich metal-binding motifs** diagnostic of IGPD — Region 1 `KGDT**H**IDD**HH**` (His62/His66/His67) and Region 2 `RG**H**NT**HH**Q` (His159/His162/His163). This intra-subunit two-fold pseudosymmetry reflects the **ancient gene duplication** that created the two metal-binding half-sites (PMID 16338409), so the *P. putida* enzyme is predicted with high confidence to use the identical dimanganese mechanism.

---

## 4. Biological Process and Pathway Context

**Pathway:** L-histidine biosynthesis from 5-phospho-α-D-ribose-1-diphosphate (PRPP) — KEGG map ppu00340 (Histidine metabolism) and module M00026 (PRPP ⇒ histidine). IGPD catalyzes **step 6 of 9** (UniProt/HAMAP MF_00076).

In *P. putida* KT2440 the pathway enzymes are encoded by a **distributed (non-operonic) set of genes**, mapped here via KEGG:

| Step | Enzyme (EC) | KO | *P. putida* locus |
|------|-------------|----|-------------------|
| 1 | ATP phosphoribosyltransferase (2.4.2.17), *hisG* | K00765 | PP_0965 |
| 5 | Imidazoleglycerol-phosphate synthase (4.3.2.10), *hisF* | K02500 | PP_0293 |
| **6** | **Imidazoleglycerol-phosphate dehydratase (4.2.1.19), *hisB*** | **K01693** | **PP_0289** |
| 7 | Histidinol-phosphate aminotransferase (2.6.1.9), *hisC* | K00817 | PP_0967 |
| 8 | Histidinol-phosphate phosphatase (3.1.3.15) | K05602 | PP_3157 |
| 9 | Histidinol dehydrogenase (1.1.1.23), *hisD* | K00013 | PP_0966 |

**Monofunctional vs bifunctional HisB.** KEGG module M00026 encodes two mutually exclusive branches for the dehydratase/phosphatase steps: (i) a **monofunctional IGPD (K01693)** plus a **separate histidinol-phosphatase**, or (ii) a **bifunctional IGPD/phosphatase (K01089)**, as found in enterobacteria. *E. coli hisB* is the bifunctional 355-aa enzyme (Chiariotti et al., 1986, PMID 3007936). *P. putida* uses branch (i): the monofunctional 197-aa IGPD (PP_0289) works together with a **separate PHP-family histidinol-phosphate phosphatase (PP_3157, K05602)**. This definitively resolves that *hisB*/PP_0289 carries out **only** the dehydration step.

---

## 5. Subcellular Localization

The enzyme is **cytoplasmic** (UniProt Q88R45, HAMAP MF_00076). It has no signal peptide, no transmembrane segments, and no lipidation signal; the entire histidine biosynthetic pathway operates as a soluble cytosolic route. The catalytic reaction therefore occurs **in the bacterial cytoplasm**, where the enzyme functions as a large soluble homo-24-meric particle.

---

## 6. Biological / Translational Significance

- **Essentiality:** IGPD activity is required for histidine prototrophy; loss abolishes de novo histidine synthesis (histidine auxotrophy).
- **Drug/herbicide target:** Because the histidine pathway is absent in mammals, IGPD is an attractive, selective target. It is competitively inhibited by 3-amino-1,2,4-triazole (PMID 24311587) and is the target of triazole-phosphonate herbicides (PMID 16338409). Histidine metabolism/IGPD has also been implicated in bacterial biofilm formation (Zhou et al., 2018, PMID 29675012).

---

## 7. Supported and Refuted Hypotheses

**Supported:**
- H1: *hisB*/PP_0289 is a monofunctional IGPD catalyzing step 6 of histidine biosynthesis (IGP → IAP + H₂O). — Supported by UniProt catalytic-activity annotation, KEGG K01693 mapping, and sequence length/domain content.
- H2: The enzyme uses a conserved dimanganese active site and imidazolate/diazafulvene mechanism. — Supported by ortholog crystal structures (PMID 16338409, 26095028, 24311587) and conservation of the two His-rich motifs in Q88R45.
- H3: The enzyme is cytoplasmic. — Supported by UniProt/HAMAP and absence of localization/membrane signals.
- H4: In *P. putida* the phosphatase step is encoded separately (not by hisB). — Supported by KEGG module logic and identification of PP_3157 (K05602).

**Refuted / ruled out:**
- *hisB* of *P. putida* is NOT the bifunctional IGPD+histidinol-phosphatase enzyme found in *E. coli* (197 aa single domain vs 355 aa two-domain; separate PP_3157 phosphatase present).

---

## 8. Limitations and Future Directions

- **No direct P. putida experimental data:** Function is assigned by strong homology/annotation transfer and family-wide structural/mechanistic studies (Mtb, *Arabidopsis*), not by biochemical characterization of the *P. putida* enzyme itself. Enzyme kinetics (kcat/Km for IGP), metal dependence, and a *P. putida* IGPD structure remain to be determined experimentally.
- **Start-codon note:** UniProt annotates a 197-aa product; KEGG lists a 210-aa product with a 13-residue N-terminal extension. This is a start-site annotation discrepancy and does not affect the catalytic domain or function.
- **Regulation:** Transcriptional/feedback regulation of the *P. putida* his genes (e.g., attenuation, feedback inhibition of HisG by histidine) was not examined in detail and would refine the physiological picture.

---

## References (PMIDs)

- Glynn SE, et al. Structure and mechanism of imidazoleglycerol-phosphate dehydratase. *Structure* 2005. **PMID 16338409**.
- Bisson C, et al. Crystal structures reveal that the reaction mechanism of IGPD is controlled by switching Mn(II) coordination. *Structure* 2015. **PMID 26095028**.
- Ahangar MS, et al. Structures of native, substrate-bound and inhibited forms of *M. tuberculosis* IGPD. *Acta Cryst D* 2013. **PMID 24311587**.
- Chiariotti L, et al. Gene structure in the histidine operon of *E. coli*: identification and nucleotide sequence of the hisB gene. 1986. **PMID 3007936**.
- Zhou X, et al. Histidine metabolism and IGPD play a key role in cefquinome inhibiting biofilm formation. 2018. **PMID 29675012**.
- Database annotations: UniProt Q88R45 (HAMAP MF_00076); KEGG ppu:PP_0289 (K01693), module M00026; InterPro IPR000807/IPR020565/IPR038494; Pfam PF00475.


## Artifacts

- [OpenScientist final report](hisB-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](hisB-deep-research-openscientist_artifacts/final_report.pdf)