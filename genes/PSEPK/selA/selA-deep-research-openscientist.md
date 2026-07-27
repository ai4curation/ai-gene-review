---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-26T20:22:13.159240'
end_time: '2026-07-26T21:34:35.873442'
duration_seconds: 4342.71
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: selA
  gene_symbol: selA
  uniprot_accession: Q88QJ8
  protein_description: 'RecName: Full=L-seryl-tRNA(Sec) selenium transferase {ECO:0000255|HAMAP-Rule:MF_00423};
    EC=2.9.1.1 {ECO:0000255|HAMAP-Rule:MF_00423}; AltName: Full=Selenocysteine synthase
    {ECO:0000255|HAMAP-Rule:MF_00423}; Short=Sec synthase {ECO:0000255|HAMAP-Rule:MF_00423};
    AltName: Full=Selenocysteinyl-tRNA(Sec) synthase {ECO:0000255|HAMAP-Rule:MF_00423};'
  gene_info: Name=selA {ECO:0000255|HAMAP-Rule:MF_00423}; OrderedLocusNames=PP_0493;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the SelA family. {ECO:0000255|HAMAP-
  protein_domains: PyrdxlP-dep_Trfase. (IPR015424); PyrdxlP-dep_Trfase_major. (IPR015421);
    SelA-like. (IPR018319); SelA_trans. (IPR004534); SelA_trans_N_dom. (IPR025862)
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
  path: selA-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: selA-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88QJ8
- **Protein Description:** RecName: Full=L-seryl-tRNA(Sec) selenium transferase {ECO:0000255|HAMAP-Rule:MF_00423}; EC=2.9.1.1 {ECO:0000255|HAMAP-Rule:MF_00423}; AltName: Full=Selenocysteine synthase {ECO:0000255|HAMAP-Rule:MF_00423}; Short=Sec synthase {ECO:0000255|HAMAP-Rule:MF_00423}; AltName: Full=Selenocysteinyl-tRNA(Sec) synthase {ECO:0000255|HAMAP-Rule:MF_00423};
- **Gene Information:** Name=selA {ECO:0000255|HAMAP-Rule:MF_00423}; OrderedLocusNames=PP_0493;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the SelA family. {ECO:0000255|HAMAP-
- **Key Domains:** PyrdxlP-dep_Trfase. (IPR015424); PyrdxlP-dep_Trfase_major. (IPR015421); SelA-like. (IPR018319); SelA_trans. (IPR004534); SelA_trans_N_dom. (IPR025862)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "selA" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'selA' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **selA** (gene ID: selA, UniProt: Q88QJ8) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: SelA (L-seryl-tRNA(Sec) selenium transferase) in *Pseudomonas putida* KT2440

**Gene:** `selA` (Ordered locus **PP_0493**)
**UniProt:** Q88QJ8 · **Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / KT2440)
**EC 2.9.1.1** · **Family:** SelA family; fold-type-I pyridoxal-5′-phosphate (PLP)-dependent transferase superfamily
**Synonyms:** Selenocysteine synthase; Sec synthase; Selenocysteinyl-tRNA(Sec) synthase
**Date:** 2026-07-27

---

## 0. Identity verification (mandatory)

The requested target is **SelA of *P. putida* KT2440 (Q88QJ8, PP_0493)**. The UniProt descriptors — gene symbol *selA*, EC 2.9.1.1, "L-seryl-tRNA(Sec) selenium transferase / selenocysteine synthase", membership in the **SelA family**, and the diagnostic domain set (PyrdxlP-dependent transferase IPR015421/IPR015424; **SelA_trans** IPR004534; **SelA_trans_N_dom** IPR025862; SelA-like IPR018319) — are all mutually consistent and unambiguously identify a **bacterial selenocysteine synthase**.

There is no significant gene-symbol ambiguity: in bacterial genetics *selA* has a single, stable meaning (the selenocysteine synthase of the *sel* operon), distinct from the eukaryotic/archaeal counterpart **SepSecS** (which uses a different substrate). Direct experimental literature exists for orthologs in *Escherichia coli*, *Aquifex aeolicus*, and *Moorella thermoacetica*; the *P. putida* protein is annotated by homology (HAMAP rule MF_00423). Because SelA is a highly conserved housekeeping enzyme with essentially one biochemical function across bacteria, the mechanistic and structural conclusions from these orthologs transfer directly to the *P. putida* protein. All function-level claims below are therefore made with high confidence; strain-specific *P. putida* biochemical studies of PP_0493 itself are not available and this is noted as a limitation.

---

## 1. Summary (answer to the research question)

**SelA (PP_0493) is a pyridoxal-5′-phosphate (PLP)-dependent selenocysteine synthase (EC 2.9.1.1) that catalyzes the terminal, committed step of selenocysteine (Sec, the 21st amino acid) biosynthesis in the bacterial cytoplasm.** It converts **L-seryl-tRNA(Sec) into L-selenocysteinyl-tRNA(Sec)**, replacing the serine hydroxyl with a selenol group using **selenophosphate** as the activated selenium donor. Its substrate is not a free amino acid but an **aminoacylated tRNA(Sec)**, and its exquisite specificity for tRNA(Sec) (over the near-identical Ser-tRNA(Ser)) is enforced by a large **homodecameric (≈500 kDa) quaternary structure** whose N-terminal domains read the tRNA(Sec)-specific D-arm. The charged Sec-tRNA(Sec) it produces is handed to the dedicated elongation factor **SelB**, which recodes in-frame UGA codons (via SECIS elements) to insert Sec co-translationally into bacterial selenoproteins.

---

## 2. Primary molecular function — the catalyzed reaction

### 2.1 Reaction and substrate specificity

SelA catalyzes:

> **L-seryl-tRNA(Sec) + selenophosphate → L-selenocysteinyl-tRNA(Sec) + phosphate** (PLP-dependent).

The pathway context: tRNA(Sec) (the product of *selC*) is first charged with **serine** by the canonical seryl-tRNA synthetase, producing Ser-tRNA(Sec); SelA then converts this to Sec-tRNA(Sec) [PMID 1839607; 23266652]. Critically, **SelA acts on the tRNA-bound amino acid, not free serine**, and it specifically recognizes tRNA(Sec): "Selenocysteine synthase catalyses the synthesis of selenocysteyl-tRNA(Sec) from seryl-tRNA(Sec) in a pyridoxal phosphate-dependent reaction mechanism. The enzyme specifically recognizes the tRNA(Sec) molecule" [PMID 1839607]. The *E. coli* enzyme is formally defined as "Selenocysteine Synthase (SELA, E.C. 2.9.1.1) … responsible for the conversion of seryl-tRNA(sec) into selenocysteyl-tRNA(sec)" [PMID 23266652].

### 2.2 Cofactor and chemical mechanism

SelA is a **PLP (vitamin B6)-dependent enzyme** of the **fold-type-I PLP superfamily** [PMID 24456689]. Mechanistically, PLP forms a Schiff-base (aldimine) with the α-amino group of the tRNA-bound seryl residue; β-elimination of the serine hydroxyl generates a PLP-stabilized **dehydroalanyl (aminoacrylyl)-tRNA** intermediate, to which the selenol nucleophile derived from **selenophosphate** is added, yielding selenocysteinyl-tRNA(Sec). Structural work on *Aquifex aeolicus* SelA shows that "SelA catalyzes pyridoxal 5′-phosphate-dependent Sec formation involving **Arg residues** nonhomologous to those in SepSecS" [PMID 23559248] — i.e., bacterial SelA uses a distinct constellation of catalytic residues from the archaeal/eukaryotic enzyme, evidence that the two Sec-synthesis systems arose by **independent (convergent) evolution** despite both being PLP enzymes.

### 2.3 Selenium donor

The activated selenium substrate is **selenophosphate**, produced by **selenophosphate synthetase (SelD)** from selenide and ATP. This is conserved across all three domains of life: the eukaryotic/archaeal counterpart likewise "required selenophosphate and O-phosphoseryl-tRNA([Ser]Sec) as substrates to generate selenocysteyl-tRNA([Ser]Sec)" [PMID 17194211]. The key bacterial-vs-eukaryotic distinction is the serine intermediate: **bacterial SelA acts directly on Ser-tRNA(Sec)**, whereas eukaryotic/archaeal SepSecS first requires phosphorylation of the seryl moiety to O-phosphoseryl-tRNA(Sec) [PMID 18093968; 17194211].

---

## 3. Structure–function: how specificity is achieved

- **Quaternary structure.** SelA "has an exceptional homodecameric quaternary structure with a molecular mass of about 500kDa" [PMID 24456689]. The *E. coli* enzyme is a homodecamer of ~500 kDa (pI ≈ 6.03), assembling by stepwise addition of oligomeric intermediates rather than a direct monomer→decamer jump [PMID 23266652].
- **A pentamer of dimers.** The ring "is composed of pentamerized SelA dimers," and the **catalytic site lies close to the dimer–dimer interface**. Engineered "depentamerized" (dimeric) variants "formed a distorted and inactivated catalytic site," proving that higher-order assembly is required to build a productive active site [PMID 24456689].
- **tRNA recognition and substrate discrimination.** The decamer "binds 10 tRNA(Sec) molecules, each interacting with four SelA subunits," and "The SelA **N-terminal domain binds the tRNA(Sec)-specific D-arm structure, thereby discriminating Ser-tRNA(Sec) from Ser-tRNA(Ser)**" [PMID 23559248]. This corresponds to the InterPro **SelA_trans_N_dom (IPR025862)** annotated in Q88QJ8. Binding stoichiometry is ~1 tRNA(Sec) per SelA monomer with D5 point-group symmetry [PMID 23428847].
- **Decamerization is functionally essential**, confirmed by in vivo and in vitro assays [PMID 23559248].

Together these establish that the large ring is the functional unit; oligomerization simultaneously creates the composite catalytic sites and the extended surface that reads tRNA(Sec) identity elements, guaranteeing that only the correct tRNA is selenylated.

---

## 3b. Organism-specific confirmation in *P. putida* KT2440 (bioinformatic evidence)

Direct inspection of the UniProt/genomic record for the target protein and its genomic neighborhood corroborates every functional claim at the level of *P. putida* KT2440 itself (not just orthologs):

- **Q88QJ8 (PP_0493)** is a **475-residue** protein carrying the diagnostic **PLP Schiff-base lysine at position 297** (annotated "N6-(pyridoxal phosphate)lysine") — the catalytic residue expected for a fold-type-I PLP enzyme.
- Annotated **catalytic activity (Rhea:22728):** *L-seryl-tRNA(Sec) + selenophosphate + H⁺ = L-selenocysteinyl-tRNA(Sec) + phosphate*; **cofactor:** pyridoxal 5′-phosphate; **pathway:** "selenocysteinyl-tRNA(Sec) from L-seryl-tRNA(Sec) (bacterial route), step 1/1"; **subcellular location:** Cytoplasm.
- **Genomic clustering — a complete, co-localized Sec machinery.** *selA* (PP_0493) is **immediately adjacent to *selB* (PP_0494)**, reproducing the *E. coli* *selAB* operon arrangement. The upstream neighborhood encodes a **formate-dehydrogenase operon**: **PP_0489 (*fdoG*, 1022 aa)** — the catalytic major subunit that **contains a genetically encoded selenocysteine at position 197** (UniProt "Non-standard residue: Selenocysteine") — together with **PP_0490** (formate dehydrogenase iron-sulfur subunit) and **PP_0492** (FdhE maturation homolog). The selenium-donor enzyme **SelD / selenophosphate synthetase (PP_0823)**, which "synthesizes selenophosphate from selenide and ATP," resides elsewhere in the genome.

**Interpretation:** This is direct, organism-specific evidence for SelA's role. *P. putida* KT2440 encodes a bona-fide selenoprotein (FdoG, Sec-197). The in-frame UGA that specifies that Sec can only be translated if SelA has generated **Sec-tRNA(Sec)**. Thus SelA (PP_0493) is functionally required to mature the cell's **selenocysteine-dependent formate dehydrogenase**, and the physical clustering of *selAB* with the *fdo* formate-dehydrogenase genes ties the enzyme to a concrete downstream client rather than a merely inferred one.

## 3c. Sequence/evolutionary evidence — an intact, canonical active site

A global pairwise alignment shows **P. putida SelA (Q88QJ8, 475 aa) is 65.2% identical (283/434 aligned positions) to *E. coli* SelA (P0A821)** — the enzyme experimentally validated as a PLP-dependent, ~500 kDa homodecameric selenocysteine synthase. Critically, the **catalytic PLP-Schiff-base lysine is conserved within an invariant fold-type-I motif**: P. putida `VTF**SGDK²⁹⁷LLGGPQ**` vs *E. coli* `VSF**SGDKLLGGPQ**` (only a conservative T/S difference outside the core motif). This is fully consistent with UniProt's independent annotation of **Lys297** as the N6-(pyridoxal phosphate)lysine.

**Interpretation:** The high whole-length identity to a functionally proven ortholog, plus strict conservation of the catalytic lysine and its signature motif, is strong evolutionary evidence that the *P. putida* enzyme has an intact, canonical selenocysteine-synthase active site. It is a genuine SelA ortholog — not a divergent or pseudo-enzymatic paralog — which justifies transferring the *E. coli*/*A. aeolicus* mechanistic and structural conclusions to this protein.

## 4. Localization

SelA is a **soluble cytoplasmic (cytosolic) enzyme**. It has no signal peptide, no transmembrane segments, and acts on a cytoplasmic substrate (an aminoacyl-tRNA) in a process tightly coupled to ribosomal translation. Recombinant *E. coli* SelA is purified as a soluble ~500 kDa protein by standard chromatography [PMID 23266652]. Its product is consumed in the cytoplasm by SelB during translation [PMID 1839607; 12486013]. This is consistent with the UniProt/HAMAP annotation of a cytoplasmic location.

---

## 5. Pathway context — the bacterial selenocysteine incorporation machinery

SelA is one of four dedicated components (plus seryl-tRNA synthetase) that recode UGA to insert Sec:

| Gene | Product | Role relative to SelA |
|------|---------|-----------------------|
| *selC* | tRNA(Sec) | Scaffold substrate; charged with Ser, then converted by SelA |
| *selD* | Selenophosphate synthetase | Makes the selenium donor (selenophosphate) used by SelA |
| **selA** | **Selenocysteine synthase (this protein)** | **Converts Ser-tRNA(Sec) → Sec-tRNA(Sec)** |
| *selB* | Sec-specific elongation factor (EF-Tu-like) | Accepts SelA's product; decodes UGA at SECIS elements |

- SelA's product is channeled to SelB: "SELB is an EF-Tu-like protein which specifically complexes selenocysteyl-tRNA(Sec)… Interaction with the selenol group of the side chain … is a prerequisite for the formation of a stable SELB·tRNA complex" [PMID 1839607]. This selenol-dependent recognition is the checkpoint ensuring only fully synthesized Sec-tRNA(Sec) (SelA's output) is used.
- Downstream, the **SECIS element** immediately 3′ of the UGA "tether[s] a complex of the selenocysteine-specific elongation factor SelB, GTP and selenocysteyl-tRNA(Sec) to the site of UGA decoding" [PMID 12486013].
- **Operon organization and regulation.** In *E. coli*, "The **selAB operon** codes for the proteins selenocysteine synthase and SELB" [PMID 1839607], and a SECIS-like element in the *selAB* leader couples expression of the pathway to selenium availability [PMID 12486013]. This *selAB* arrangement is **conserved in *P. putida***, where *selA* (PP_0493) and *selB* (PP_0494) are immediately adjacent (§3b); *selD* (PP_0823) lies elsewhere in the genome.
- **Biological end-products.** The Sec-tRNA(Sec) generated by SelA is used to synthesize bacterial **selenoproteins**, canonically the anaerobic/formate-linked oxidoreductases (e.g., **formate dehydrogenases**) and related redox enzymes, where Sec provides a highly reactive catalytic selenol. **In *P. putida* KT2440 specifically, the identified selenoprotein client is FdoG (PP_0489), a formate dehydrogenase major subunit bearing selenocysteine at residue 197**, encoded in a *fdo* operon immediately upstream of *selAB* (see §3b).
- **Why the Sec matters (mechanistic payoff).** In Mo/W-containing formate dehydrogenases, "a selenocysteine (SeCys) or cysteine (Cys) ligand at the Mo atom in the active site is **essential for the reaction**" [PMID 25514355]. The *E. coli* FDH-H crystal structure shows the **molybdenum "directly coordinated to selenium"** and a mechanism "directly involv[ing] SeCys140 and His141 in proton abstraction" [PMID 9036855]. Thus SelA sits at the head of a precise mechanistic chain — **SelA → Sec-tRNA(Sec) → SelB-mediated UGA recoding → Sec-FdoG → Mo–Se catalytic center** — and its activity is a prerequisite for assembling a catalytically competent selenium-dependent formate dehydrogenase. (Note: the *fdo*-type enzyme is a cysteine/selenocysteine-ligand FDH; SelA is specifically required for the Sec-containing form.)

---

## 6. Evidence summary and confidence

- **Reaction/EC/cofactor:** Strong experimental evidence in orthologs (biochemical characterization of *E. coli* and archaeal/thermophilic enzymes) [PMID 1839607; 23266652; 23559248]. Confidence for *P. putida*: **High** (conserved family, HAMAP MF_00423).
- **Mechanism (PLP, dehydroalanine intermediate, selenophosphate donor):** Strong; supported by crystallography and enzymology of SelA and the parallel eukaryotic enzyme [PMID 23559248; 18093968; 17194211]. Confidence: **High**.
- **Quaternary structure / specificity determinants:** Direct structural + mutational evidence in *A. aeolicus* / *E. coli* SelA [PMID 23559248; 24456689; 23428847]. Confidence: **High** (family-conserved; *P. putida*-specific structure not solved).
- **Localization (cytoplasmic):** Inferred from sequence features, biochemistry, and pathway logic. Confidence: **High**.
- **Pathway/operon role:** Strong genetic and biochemical evidence [PMID 1839607; 12486013], plus confirmed *P. putida* genomic context (*selAB* = PP_0493–PP_0494 adjacent; *selD* = PP_0823; Sec-selenoprotein FdoG = PP_0489). Confidence: **High**.

---

## 7. Supported vs. refuted hypotheses

**Supported**
1. SelA is a PLP-dependent enzyme converting Ser-tRNA(Sec) → Sec-tRNA(Sec) (EC 2.9.1.1). ✔
2. Selenophosphate is the selenium donor. ✔
3. SelA is a ~500 kDa homodecamer (pentamer of dimers); oligomerization is essential for catalysis and tRNA(Sec) discrimination. ✔
4. SelA is cytoplasmic and functions within the selA/selB/selC/selD pathway, feeding Sec-tRNA(Sec) to SelB for UGA recoding. ✔

**Refuted / excluded**
1. SelA acts on **free** serine or free selenocysteine — refuted; the substrate is the **tRNA-bound** seryl residue [PMID 1839607].
2. SelA uses the eukaryotic-type **O-phosphoseryl** intermediate — refuted for bacteria; that phosphoserine route is specific to archaeal/eukaryotic **SepSecS** [PMID 18093968; 17194211].
3. SelA is a small monomeric transferase — refuted; the functional unit is the decameric ring [PMID 24456689].

---

## 8. Limitations and future directions

- No biochemical or structural study of the *P. putida* KT2440 protein (PP_0493) itself exists; all mechanistic/structural detail is transferred from orthologs (*E. coli*, *A. aeolicus*) of a highly conserved family — justified here by 65% identity and a strictly conserved active site (§3c). A direct enzymatic assay and/or cryo-EM of PP_0493 would confirm strain-level parameters.
- The *P. putida* selenoprotein complement identified from annotation is the FdoG-type formate dehydrogenase (PP_0489, Sec-197); the growth conditions under which it (and hence the SelA pathway) is required — e.g., anaerobic/microaerophilic formate metabolism and selenium availability — warrant targeted expression and knockout studies.
- Whether *P. putida* SelA-dependent Sec incorporation is regulated by selenium availability via a SECIS-like leader (as in *E. coli*) is a testable, unresolved question.

---

## 9. Key references (PMIDs)

- 1839607 — Forchhammer, Boesmiller, Böck (1991): biochemical characterization of selenocysteine synthase (SelA) and SELB; selAB operon; PLP mechanism; substrate = Ser-tRNA(Sec).
- 23266652 — Manzine et al. (2013): *E. coli* SELA, EC 2.9.1.1, ~500 kDa PLP homodecamer converting seryl- to selenocysteyl-tRNA(Sec).
- 23559248 — Itoh et al. (2013, *Science*): decameric SelA·tRNA(Sec) ring structure; mechanism; D-arm–based substrate discrimination; PLP/Arg catalysis; independent evolution vs SepSecS.
- 24456689 — Itoh et al. (2014): fold-type-I PLP superfamily; pentamer-of-dimers assembly essential for active-site formation and specificity.
- 23428847 — Manzine et al. (2013): 1:1 SelA:tRNA(Sec) stoichiometry; D5 symmetry.
- 12486013 — Thanbichler & Böck (2002): SECIS/SelB UGA recoding; selAB operon regulation by selenium.
- 18093968 — Ganichkin et al. (2008): eukaryotic SecS structure/mechanism (contrast; phosphoserine route).
- 17194211 — Xu et al. (2007): eukaryotic Sec biosynthesis pathway; selenophosphate + phosphoseryl-tRNA substrates (contrast).
- 25514355 — Hartmann, Schwanhold & Leimkühler (2015): review of bacterial Mo/W formate dehydrogenases; Sec/Cys ligand at Mo essential for catalysis (downstream significance of SelA).
- 9036855 — Boyington et al. (1997, *Science*): FDH-H crystal structure; Sec140 directly coordinates Mo and participates in proton abstraction (downstream significance of SelA).


## Artifacts

- [OpenScientist final report](selA-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](selA-deep-research-openscientist_artifacts/final_report.pdf)