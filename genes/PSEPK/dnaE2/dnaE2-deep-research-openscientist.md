---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-12T23:22:13.679488'
end_time: '2026-08-13T00:09:19.579789'
duration_seconds: 2825.9
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: dnaE2
  gene_symbol: dnaE2
  uniprot_accession: Q88I82
  protein_description: 'RecName: Full=Error-prone DNA polymerase {ECO:0000255|HAMAP-Rule:MF_01902};
    EC=2.7.7.7 {ECO:0000255|HAMAP-Rule:MF_01902};'
  gene_info: Name=dnaE2 {ECO:0000255|HAMAP-Rule:MF_01902}; OrderedLocusNames=PP_3119;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the DNA polymerase type-C family. DnaE2
  protein_domains: DNA_pol3_alpha_NTPase_dom. (IPR011708); DNA_pol3_finger. (IPR040982);
    DnaE2. (IPR023073); DnaE2/DnaE/PolC. (IPR004805); DNAPol_HHH. (IPR029460)
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
  path: dnaE2-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: dnaE2-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88I82
- **Protein Description:** RecName: Full=Error-prone DNA polymerase {ECO:0000255|HAMAP-Rule:MF_01902}; EC=2.7.7.7 {ECO:0000255|HAMAP-Rule:MF_01902};
- **Gene Information:** Name=dnaE2 {ECO:0000255|HAMAP-Rule:MF_01902}; OrderedLocusNames=PP_3119;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the DNA polymerase type-C family. DnaE2
- **Key Domains:** DNA_pol3_alpha_NTPase_dom. (IPR011708); DNA_pol3_finger. (IPR040982); DnaE2. (IPR023073); DnaE2/DnaE/PolC. (IPR004805); DNAPol_HHH. (IPR029460)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "dnaE2" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'dnaE2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **dnaE2** (gene ID: dnaE2, UniProt: Q88I82) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of DnaE2 (gene *dnaE2* / PP_3119; UniProt Q88I82)
## *Pseudomonas putida* KT2440

---

## 1. Summary (Answer to the Research Question)

**DnaE2 (Q88I82, locus PP_3119) is a second, non-essential catalytic subunit of DNA polymerase III belonging to the C-family of DNA polymerases (PolC/DnaE; EC 2.7.7.7, DNA-directed DNA polymerase).** Its primary function is **error-prone, template-directed DNA synthesis across DNA lesions (translesion synthesis, TLS)** as the catalytic engine of the bacterial **"mutasome."** It catalyses the addition of deoxyribonucleotides to a primer 3′-OH using a damaged DNA template as instruction, producing DNA synthesis past bulky/blocking lesions at the cost of introducing point mutations. DnaE2 is **induced by DNA damage as part of the RecA/LexA-controlled SOS response** and acts together with two accessory proteins encoded in the same cassette — **ImuA′** (a RecA paralog) and **ImuB** (a catalytically dead Y-family polymerase that tethers the complex to the β sliding clamp). The gene product functions **in the cytoplasm, at the DNA replication fork**, where it is recruited to stalled replisomes. Physiologically it mediates **damage-induced (SOS) mutagenesis**, contributing to survival of genotoxic stress and to the evolution of adaptive mutations, including antibiotic/drug resistance.

> **Identity check (passed).** The gene symbol, C-family (PolC/DnaE) assignment, the "DnaE2" subfamily InterPro signatures (IPR023073 DnaE2; IPR004805 DnaE2/DnaE/PolC; IPR011708 DNA_pol3_alpha NTPase; IPR040982 DNA_pol3_finger; IPR029460 DNAPol_HHH), and the EC 2.7.7.7 activity all correspond precisely to the *bona fide* error-prone DnaE2 polymerase family. The literature cited below concerns this same protein family in closely related and model bacteria; the *P. putida* ortholog PP_3119 is annotated by orthology (HAMAP rule MF_01902).

---

## 2. Background: what "a second DnaE" means

Most bacteria replicate their chromosome with a single, essential replicative polymerase DnaE (the α catalytic subunit of DNA Pol III). A subset of bacteria — including *Pseudomonas*, *Caulobacter*, *Mycobacterium*, and many other Proteobacteria and Actinobacteria — carry a **second, paralogous *dnaE* gene, *dnaE2***. The existence of these "extra" replicative-type polymerases was long an "unresolved enigma," resolved by the demonstration that one copy participates in **error-prone DNA repair synthesis** rather than in bulk genome replication (Boshoff et al. 2003, *Cell*, PMID 12705867). Importantly, DnaE2 substitutes functionally for the Y-family **UmuDC/Pol V** mutagenic system, which is **absent** in these organisms (Galhardo et al. 2005, PMID 15886391). *P. putida* KT2440 lacks *umuDC*, so DnaE2 provides the RecA-dependent branch of induced mutagenesis.

---

## 3. Primary Molecular Function (the catalyzed reaction and substrate)

- **Reaction:** DNA-templated (DNA-directed) DNA polymerization — nucleotidyl transfer:
  *(DNA)ₙ + dNTP → (DNA)ₙ₊₁ + diphosphate* (**EC 2.7.7.7**).
- **Substrate specificity:** a **primer–template DNA duplex** with a free 3′-OH primer terminus, plus the four **dNTPs** and the catalytic divalent metal ions (Mg²⁺). Unlike the high-fidelity replicative DnaE, DnaE2 is **error-prone** and, as part of the mutasome, is able to extend primers opposite **damaged/distorting template bases** (e.g., lesions produced by UV or by cross-linking agents such as mitomycin C). This lesion-bypass capacity is the defining, functionally important activity (Galhardo et al. 2005, PMID 15886391; Boshoff et al. 2003, PMID 12705867).
- **Domain basis:** the PolIIIα-type NTPase/polymerase domain (IPR011708) provides the catalytic center; the "polymerase-III finger" (IPR040982) and helix-hairpin-helix (HHH, IPR029460) domains support DNA binding — architecture shared with the replicative DnaE but tuned toward lower fidelity.

DnaE2 is **not** a general-purpose replicase: knockouts are viable and do not impair normal growth; the phenotype appears specifically after genotoxic stress (reduced survival and greatly reduced induced mutation frequency) (Boshoff 2003, PMID 12705867; Galhardo 2005, PMID 15886391).

---

## 4. The Functional Unit: the ImuA′–ImuB–DnaE2 "mutasome"

DnaE2 does **not** act alone. In *P. putida* (as in *Caulobacter* and *Mycobacterium*) the *dnaE2* gene is the third gene of the **imuA–imuB–dnaE2 cassette**, and **all three products are required** for error-prone lesion processing (Galhardo et al. 2005, PMID 15886391). Recent biochemical/genetic work defines the roles of the partners:

- **ImuB** — a **catalytically inactive Y-family DNA polymerase**. It cannot itself synthesize DNA but carries a **β-clamp-binding motif** and "is predicted to enable mutasome function via its interaction with the β clamp" (Santos et al. 2025, PMID 39706264). ImuB thus acts as a **non-catalytic scaffold/adaptor** that tethers DnaE2 to the DNA Pol III sliding clamp at the replication fork.
- **ImuA′** — a **RecA homolog** of accessory (non-recombinase) function. ImuB carries a **RecA-N-terminus (RecA-NT) homology motif** that mediates the ImuB–ImuA′ interaction; disrupting this motif (e.g., hydrophobic residues L378/V383) abolishes the ImuA′–ImuB interaction, and this interaction is **essential for DNA damage-induced mutagenesis** (Santos et al. 2023, PMID 37034714; Santos et al. 2025, PMID 39706264).

**Decisive genetic-biochemical dissection (Warner et al. 2010, PMID 20615954).** In *M. tuberculosis*: (i) *imuA′* and *imuB* are each **individually essential** for induced mutagenesis and damage tolerance; (ii) yeast two-hybrid shows **ImuB interacts simultaneously with ImuA′, with DnaE2, and with the β-clamp** — i.e., ImuB is the central adaptor; (iii) **disrupting the ImuB–β-clamp interaction reduces induced mutagenesis and damage tolerance, phenocopying the deletion mutants** — establishing replisome recruitment as essential; (iv) ImuB retains Y-family fold but **lacks the conserved active-site residues** needed for catalysis; and, most importantly, (v) **replacing DnaE2's own catalytic residues reproduces the *dnaE2* deletion phenotype, directly implying that the DnaE2 α-subunit is the catalytic polymerase of mutagenic lesion bypass.** Gessner et al. 2023 (PMID 37530405) further dissect mutasome composition and recruitment.

**Model:** ImuB, docked on the β-clamp at a stalled fork, recruits ImuA′ (via RecA-NT) and DnaE2. DnaE2 supplies the catalytic polymerase activity that inserts nucleotides opposite the lesion and/or extends the primer past it. This modular design explains how a C-family (normally replicative) polymerase performs specialized translesion synthesis only when assembled into the mutasome.

---

## 5. Subcellular Localization

The gene product functions in the **cytoplasm**, specifically **at the chromosomal DNA / the replication fork**. It is a **DNA-binding enzyme** recruited to stalled replisomes through the ImuB–β-clamp interaction (Santos et al. 2025, PMID 39706264). There is no signal peptide or transmembrane region expected for a C-family polymerase; its site of action is wherever replication is blocked by template damage. Single-molecule/imaging studies of bacterial TLS confirm that lesion-bypass polymerases act at or behind the replication fork, either co-replicationally or on post-replicative gaps (Joseph & Badrinarayanan 2020, PMID 32556198).

---

## 6. Pathway / Regulatory Context: the SOS (DNA-damage) response

- DnaE2/*imuAB dnaE2* is a member of the **RecA/LexA-controlled SOS regulon**. The operon is **damage-inducible in a RecA-dependent manner**, and induction requires DNA-damaging signals (UV, mitomycin C, and other genotoxins) (Galhardo et al. 2005, PMID 15886391). In *M. tuberculosis*, *dnaE2* is upregulated by several DNA-damaging agents and during infection (Boshoff 2003, PMID 12705867).
- Mechanistically, DNA damage generates ssDNA, RecA forms a nucleoprotein filament, LexA autocleaves, and SOS genes (including *imuA–imuB–dnaE2*) are de-repressed — the canonical SOS pathway that operates in *P. putida*.
- **Functional output of the pathway:** conversion of otherwise lethal, replication-blocking lesions into survivable (but mutagenic) events — i.e., **DNA damage tolerance via error-prone translesion synthesis**. This is a *distinct* pathway from the *RecA-independent*, stationary-phase mutagenesis driven by Pol IV/DinB in *P. putida* (Tegova et al. 2004, PMID 15090515), which underscores that DnaE2 specifically provides the **RecA-dependent, SOS-inducible** mutagenic branch.

---

## 7. Physiological / Evolutionary Significance

- **Survival of genotoxic stress:** loss of DnaE2 reduces survival after UV irradiation (Boshoff 2003, PMID 12705867).
- **Induced mutagenesis / adaptive evolution:** DnaE2 is responsible for most UV- and mitomycin-C-induced mutations in *Caulobacter*, including unusual substitution spectra (e.g., G:C→C:G transversions) (Galhardo 2005, PMID 15886391).
- **Drug/antibiotic resistance:** by generating point mutations under stress, DnaE2 can directly contribute to the emergence of drug resistance in vivo (Boshoff 2003, PMID 12705867) — a clinically relevant consequence of the same TLS activity.

**Genus-level (Pseudomonas) evidence.** The closest well-studied relative, *Pseudomonas aeruginosa*, provides direct functional support: the **damage-inducible SOS-response *imuBC* gene products contribute (together with *dinB*/Pol IV and RpoS) to the generation of ciprofloxacin-resistance mutations** (Fahey et al. 2023, PMID 37625357). This demonstrates that the *imuAB dnaE2* module is an active, SOS-inducible mutagenesis system within the *Pseudomonas* genus and reinforces the annotation-by-orthology of *P. putida* PP_3119 as the catalytic translesion polymerase of that module.

For *P. putida* KT2440 specifically, these roles are inferred by **strong orthology** and conserved operon structure rather than by dedicated single-gene knockout studies; *P. putida* mutagenesis research has more often focused on Pol IV/DinB (RecA-independent stationary-phase mutagenesis, PMID 15090515), leaving a defined niche for DnaE2 as the RecA/SOS-dependent mutagenic polymerase.

---

## 8. Supported vs. Refuted Hypotheses

**Supported**
- DnaE2 is a C-family (PolC/DnaE) DNA polymerase catalysing DNA-directed DNA synthesis (EC 2.7.7.7). *(family/domain + literature)*
- Its specialized function is **error-prone translesion synthesis / damage-induced mutagenesis**, not bulk replication. *(PMID 12705867, 15886391)*
- It operates within the **ImuA′–ImuB–DnaE2 mutasome**, tethered to the **β-clamp** at the replication fork. *(PMID 20615954, 37530405, 37034714, 39706264, 15886391)*
- **DnaE2 is the direct catalytic polymerase** for lesion bypass: mutating its catalytic residues phenocopies deletion, while its partner ImuB is catalytically dead. *(PMID 20615954)*
- It is **SOS/RecA-regulated** and induced by DNA damage. *(PMID 15886391, 12705867)*
- Localization: **cytoplasmic, DNA/replication-fork associated.** *(PMID 39706264, 32556198)*

**Refuted / excluded**
- DnaE2 is the essential replicative replicase — **refuted** (knockouts viable; phenotype only under damage).
- DnaE2 mediates the RecA-*independent* stationary-phase mutagenesis of *P. putida* — that role belongs to Pol IV/DinB (PMID 15090515); DnaE2 provides the RecA-*dependent* branch.

---

## 9. Limitations & Future Directions

- **Direct experimental evidence in *P. putida* KT2440 (PP_3119) is limited;** the functional annotation rests primarily on (i) unambiguous C-family/DnaE2 domain and family signatures, (ii) HAMAP orthology rule MF_01902, and (iii) detailed genetics/biochemistry of orthologs in *Caulobacter crescentus* and *Mycobacterium tuberculosis*.
- The precise *P. putida* mutational spectrum, the exact ImuA/ImuB residues, and in vivo fork localization for PP_3119 have not been directly measured.
- **Future work:** clean *dnaE2* / *imuB* deletions in *P. putida* KT2440 with UV/MMC survival and rifampicin-resistance mutagenesis assays; confirmation of a functional LexA/SOS box upstream of *imuA*; reconstitution of the *P. putida* mutasome to measure lesion-bypass fidelity and β-clamp dependence.

---

## 10. Key References
- Boshoff HIM, Reed MB, Barry CE III, Mizrahi V. *DnaE2 polymerase contributes to in vivo survival and the emergence of drug resistance in Mycobacterium tuberculosis.* **Cell** 2003. PMID 12705867.
- Galhardo RS, Rocha RP, Marques MV, Menck CFM. *An SOS-regulated operon involved in damage-inducible mutagenesis in Caulobacter crescentus.* **Nucleic Acids Res** 2005. PMID 15886391.
- Warner DF, Ndwandwe DE, Abrahams GL, Kana BD, Machowski EE, Venclovas Č, Mizrahi V. *Essential roles for imuA′- and imuB-encoded accessory factors in DnaE2-dependent mutagenesis in Mycobacterium tuberculosis.* **PNAS** 2010. PMID 20615954.
- Gessner S, et al. *Investigating the composition and recruitment of the mycobacterial ImuA′-ImuB-DnaE2 mutasome.* 2023. PMID 37530405.
- Santos JA, Timinskas K, Lamers MH, Venclovas Č, Warner DF, Gessner S. *RecA-NT homology motif in ImuB is essential for mycobacterial ImuA′–ImuB protein interaction and mutasome function.* 2023. PMID 37034714.
- Santos JA, et al. *The RecA-NT homology motif in ImuB mediates the interaction with ImuA′, which is essential for DNA damage-induced mutagenesis.* 2025. PMID 39706264.
- Joseph AM, Badrinarayanan A. *Visualizing mutagenic repair: novel insights into bacterial translesion synthesis.* **FEMS Microbiol Rev** 2020. PMID 32556198.
- Tegova R, Tover A, Tarassova K, Tark M, Kivisaar M. *Involvement of error-prone DNA polymerase IV in stationary-phase mutagenesis in Pseudomonas putida.* **J Bacteriol** 2004. PMID 15090515.
- Fahey C, O'Brien J, Pagnon J, Page D, Wilson S, Slamen N, Roddam L, Ambrose M. *DinB (DNA polymerase IV), ImuBC and RpoS contribute to the generation of ciprofloxacin-resistance mutations in Pseudomonas aeruginosa.* 2023. PMID 37625357.


## Artifacts

- [OpenScientist final report](dnaE2-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](dnaE2-deep-research-openscientist_artifacts/final_report.pdf)