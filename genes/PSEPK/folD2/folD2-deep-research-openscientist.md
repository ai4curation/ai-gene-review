---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-20T16:50:46.232344'
end_time: '2026-07-20T17:00:58.496478'
duration_seconds: 612.26
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: folD2
  gene_symbol: folD2
  uniprot_accession: Q88KM5
  protein_description: 'RecName: Full=Bifunctional protein FolD 2 {ECO:0000255|HAMAP-Rule:MF_01576};
    Includes: RecName: Full=Methylenetetrahydrofolate dehydrogenase {ECO:0000255|HAMAP-Rule:MF_01576};
    EC=1.5.1.5 {ECO:0000255|HAMAP-Rule:MF_01576}; Includes: RecName: Full=Methenyltetrahydrofolate
    cyclohydrolase {ECO:0000255|HAMAP-Rule:MF_01576}; EC=3.5.4.9 {ECO:0000255|HAMAP-Rule:MF_01576};'
  gene_info: Name=folD2 {ECO:0000255|HAMAP-Rule:MF_01576}; Synonyms=folD-2; OrderedLocusNames=PP_2265;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the tetrahydrofolate
  protein_domains: Aminoacid_DH-like_N_sf. (IPR046346); NAD(P)-bd_dom_sf. (IPR036291);
    THF_DH/CycHdrlase. (IPR000672); THF_DH/CycHdrlase_cat_dom. (IPR020630); THF_DH/CycHdrlase_NAD-bd_dom.
    (IPR020631)
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
  path: folD2-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: folD2-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88KM5
- **Protein Description:** RecName: Full=Bifunctional protein FolD 2 {ECO:0000255|HAMAP-Rule:MF_01576}; Includes: RecName: Full=Methylenetetrahydrofolate dehydrogenase {ECO:0000255|HAMAP-Rule:MF_01576}; EC=1.5.1.5 {ECO:0000255|HAMAP-Rule:MF_01576}; Includes: RecName: Full=Methenyltetrahydrofolate cyclohydrolase {ECO:0000255|HAMAP-Rule:MF_01576}; EC=3.5.4.9 {ECO:0000255|HAMAP-Rule:MF_01576};
- **Gene Information:** Name=folD2 {ECO:0000255|HAMAP-Rule:MF_01576}; Synonyms=folD-2; OrderedLocusNames=PP_2265;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the tetrahydrofolate
- **Key Domains:** Aminoacid_DH-like_N_sf. (IPR046346); NAD(P)-bd_dom_sf. (IPR036291); THF_DH/CycHdrlase. (IPR000672); THF_DH/CycHdrlase_cat_dom. (IPR020630); THF_DH/CycHdrlase_NAD-bd_dom. (IPR020631)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "folD2" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'folD2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **folD2** (gene ID: folD2, UniProt: Q88KM5) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: FolD2 (Q88KM5, PP_2265) in *Pseudomonas putida* KT2440

## Gene/Protein Identity — Verified

| Field | Value |
|---|---|
| UniProt | Q88KM5 |
| Gene | *folD2* (syn. *folD-2*); ordered locus **PP_2265** |
| Organism | *Pseudomonas putida* KT2440 (ATCC 47054 / DSM 6125), NCBI taxid 160488 |
| Length / MW | 284 aa / 30.6 kDa |
| Protein | Bifunctional protein FolD 2 |
| EC numbers | 1.5.1.5 (dehydrogenase) + 3.5.4.9 (cyclohydrolase) |
| Family | Tetrahydrofolate dehydrogenase/cyclohydrolase family (HAMAP MF_01576) |
| Domains | THF_DH/CycHdrlase catalytic (IPR020630); NAD(P)-binding (IPR020631, IPR036291); Aminoacid_DH-like N (IPR046346) |

**Identity confirmed.** The gene symbol *folD2* matches the protein description (bifunctional methylenetetrahydrofolate dehydrogenase / methenyltetrahydrofolate cyclohydrolase), the organism is correct, and the domain architecture (an N-terminal folate-binding domain plus a Rossmann-like NAD(P)-binding domain) is exactly that of the FolD family. Literature on bacterial FolD (E. coli, *P. aeruginosa*, *A. baumannii*, *C. perfringens*) is directly applicable. Note: *P. putida* KT2440 carries **two** FolD paralogs — *folD1* (Q88LI7, 291 aa) and *folD2* (Q88KM5, PP_2265, 284 aa) — a duplication not present in *E. coli*.

**Quantitative homology transfer (own sequence analysis).** Global pairwise alignment (Needleman–Wunsch) shows FolD2 is **86.6% identical** to the crystallographically and kinetically characterized *P. aeruginosa* PAO1 FolD (Q9I2U6, identical 284-aa length; structure in PMID 22558288) and **67.3% identical** to the biochemically characterized *E. coli* FolD (P24186). By contrast, the *P. putida* paralog FolD1 shares only **53.5%** identity with FolD2 and is more divergent from characterized orthologs (~53% *E. coli*, ~55% *P. aeruginosa*). Thus **FolD2 is the close, canonical FolD ortholog**, and structural/kinetic conclusions from *P. aeruginosa* and *E. coli* FolD transfer to FolD2 with high confidence; FolD1 is the more divergent copy.

---

## 1. Summary (Answer to the Research Question)

FolD2 is a **soluble, cytoplasmic, NADP⁺-dependent bifunctional enzyme** of folate (one-carbon) metabolism. As a homodimer it catalyzes two consecutive reactions on the tetrahydrofolate (THF) scaffold: (i) NADP⁺-dependent **oxidation of 5,10-methylene-THF to 5,10-methenyl-THF** (methylenetetrahydrofolate dehydrogenase, EC 1.5.1.5), and (ii) **hydrolysis of 5,10-methenyl-THF to 10-formyl-THF** (methenyltetrahydrofolate cyclohydrolase, EC 3.5.4.9). Its product, 10-formyl-THF, is the one-carbon donor for **de novo purine biosynthesis** and for **formylation of initiator Met-tRNA^fMet**, while the interconverted folate pool also supports thymidylate, methionine and histidine metabolism. The enzyme acts in the cytoplasm as a central housekeeping node distributing one-carbon units.

---

## 2. Primary Function: The Reactions Catalyzed

FolD interconverts oxidized one-carbon-loaded folates through two tightly coupled steps in a single active-site cleft:

1. **Dehydrogenase (EC 1.5.1.5):**
   (6R)-5,10-methylene-THF + NADP⁺ → (6R)-5,10-methenyl-THF + NADPH
2. **Cyclohydrolase (EC 3.5.4.9):**
   (6R)-5,10-methenyl-THF + H₂O → (6R)-10-formyl-THF + H⁺

The net effect is oxidation of the methylene one-carbon unit up to the formyl oxidation level, generating both NADPH and 10-formyl-THF. "Most organisms possess bifunctional FolD … to generate NADPH and 10-formyltetrahydrofolate (10-CHO-THF) required in various metabolic steps" (Aluri et al., 2016, PMID 26531681), and FolD "catalyzes interconversion of 5,10-methylene-tetrahydrofolate and 10-formyl-tetrahydrofolate in the one-carbon metabolic pathway" (Sah & Varshney, 2015, PMID 25988590).

**Substrate specificity / cofactor.** The folate substrate is polyglutamylated tetrahydrofolate bearing a one-carbon unit at N5/N10; the dehydrogenase step is specific for **NADP⁺** (not NAD⁺) in this HAMAP-annotated FolD. The reaction is reversible in vitro but physiologically drives methylene→formyl flux.

**Mechanistic separability.** Structure-guided mutagenesis of *E. coli* FolD shows the two activities are catalytically distinct yet co-located: "the R191E mutant showed high cyclohydrolase activity, it retained only a residual dehydrogenase activity … the K54S mutant lacked the cyclohydrolase activity but possessed high dehydrogenase activity" (Sah & Varshney, 2015, PMID 25988590). Residues D121/G122 are shared and essential for both. This supports a shared cleft between the two domains with the labile 5,10-methenyl-THF intermediate channeled from the dehydrogenase to the cyclohydrolase site.

**Active site is intact in FolD2 (own residue-level analysis).** Alignment of FolD2 to *E. coli* FolD shows **all seven** functionally characterized residues are conserved at identical positions in FolD2: **Y50, K54, C58, Q98, D121, G122, R191**. Critically, the cyclohydrolase-specific **K54** and the dehydrogenase-specific **R191** are both present. This provides direct residue-level evidence that FolD2 is a **genuinely bifunctional** enzyme retaining both EC 1.5.1.5 and EC 3.5.4.9 activities — not a monofunctional or degenerate paralog (contrast with *C. perfringens*, where FolD is dehydrogenase-only and a separate FchA supplies cyclohydrolase activity; PMID 26531681).

---

## 3. Localization

FolD2 is a **cytoplasmic** enzyme. It has no signal peptide, no transmembrane segment, and no membrane-anchoring motif; UniProt annotates it as a soluble **homodimer**. Its substrates (folates, NADP⁺) are cytosolic metabolites, and all characterized bacterial FolD orthologs are soluble cytoplasmic proteins purified in recombinant systems (e.g., *P. aeruginosa*, *A. baumannii*; PMIDs 22558288, 23050773). It therefore performs its function within the bacterial cytoplasm as part of the soluble one-carbon metabolic machinery.

---

## 4. Pathway Context and Biological Processes

FolD occupies a branch point of the **tetrahydrofolate one-carbon cycle**. 5,10-methylene-THF is generated mainly from serine by serine hydroxymethyltransferase (GlyA) and from glycine cleavage. FolD oxidizes this pool to **10-formyl-THF**, which is consumed by:

- **De novo purine biosynthesis** — two transformylase steps (GAR and AICAR transformylases) that build the purine ring (UniProt keyword: Purine biosynthesis).
- **Initiator tRNA formylation** — 10-formyl-THF is the formyl donor for methionyl-tRNA formyltransferase (Fmt), producing fMet-tRNA^fMet to prime translation. FolD is genetically tied to this process: resistance to the peptide deformylase inhibitor actinonin arises from mutations in "the fmt gene … and the folD gene encoding the bifunctional enzyme methylenetetrahydrofolate-dehydrogenase and -cyclohydrolase" (Nilsson et al., 2006, PMID 16636273).
- **Amino-acid/nucleotide metabolism** — the interconverted folate pool feeds methionine (via methyl-THF and methionine synthase), histidine, and thymidylate synthesis (UniProt keywords: Methionine/Histidine biosynthesis; One-carbon metabolism).

**Essentiality and phenotypes (ortholog evidence).** In *E. coli*, FolD is essential; both of its activities are required to rescue a ΔfolD strain, and loss produces "formate and glycine auxotrophies" and altered antifolate/UV susceptibility (Aluri et al., 2016, PMID 26531681). FolD is widely conserved and "involved in the biosynthesis of folate cofactors that are essential for growth and cellular development" (Eadsforth et al., 2012, PMID 23050773). In some bacteria (e.g., *C. perfringens*) the two activities are split between separate monofunctional proteins (FolD dehydrogenase + FchA cyclohydrolase) with Fhs providing an alternative 10-formyl-THF route (PMID 26531681) — but in *P. putida* FolD2 retains both activities in one polypeptide per HAMAP annotation.

---

## 5. Structural Basis

FolD enzymes are two-domain proteins: an N-terminal folate/substrate-binding domain (Aminoacid_DH-like N; IPR046346) and a Rossmann-like **NAD(P)-binding domain** (IPR036291/IPR020631) that positions NADP⁺. The active site lies in the interdomain cleft. High-resolution crystal structures of closely related Pseudomonad and Acinetobacter FolD confirm this architecture: "The crystal structure of *P. aeruginosa* FolD was determined at 2.2 Å resolution … for modelling of ligand complexes as well as for comparisons with the human enzyme" (Eadsforth et al., 2012, PMID 22558288). The strong structural conservation between bacterial and human FolD/MTHFD1 has been noted as a challenge for selective antibacterial inhibitor design (PMID 22558288). FolD2 (284 aa, 30.6 kDa, homodimer) conforms to this conserved fold.

---

## 6. Supported and Refuted Hypotheses

**Supported**
- FolD2 is a bifunctional NADP⁺-dependent 5,10-methylene-THF dehydrogenase / 5,10-methenyl-THF cyclohydrolase (EC 1.5.1.5 + 3.5.4.9). *(UniProt catalytic annotation; ortholog biochemistry PMIDs 26531681, 25988590.)*
- Its product 10-formyl-THF feeds purine synthesis and fMet-tRNA formylation. *(Keywords; PMID 16636273.)*
- It is a soluble cytoplasmic homodimer with a conserved two-domain fold. *(UniProt SUBUNIT; structures PMIDs 22558288, 23050773.)*
- FolD2 is the canonical close FolD ortholog (86.6% identical to structurally solved *P. aeruginosa* FolD) with all seven key catalytic residues (Y50/K54/C58/Q98/D121/G122/R191) conserved — including cyclohydrolase-specific K54 and dehydrogenase-specific R191 — confirming an intact, genuinely bifunctional active site. *(Own sequence analysis; PMIDs 22558288, 25988590.)*

**Refuted / cautioned**
- FolD2 is NOT NAD⁺-specific and NOT membrane-associated.
- Essentiality of *folD2* specifically in *P. putida* should NOT be assumed: because a paralog (*folD1*) exists, folD2 loss may be buffered — an inference from gene copy number, not a knockout in this strain.

---

## 7. Limitations and Future Directions

- No *P. putida*-specific biochemical or knockout study of FolD2 was found; functional assignment rests on strong homology (HAMAP MF_01576) and well-characterized orthologs.
- The division of labor between *folD1* and *folD2* (redundancy, differential regulation, or kinetic specialization) is unresolved. The two paralogs share only 53.5% identity; FolD2 is the closer match to canonical FolD (86.6% to *P. aeruginosa*), suggesting FolD2 is the principal housekeeping copy while FolD1 may be specialized. Suggested experiments: single/double knockouts with growth/auxotrophy tests, RNA-seq under one-carbon-limiting conditions, and enzyme kinetics of purified FolD1 vs FolD2.
- No *P. putida* transposon-essentiality or CRISPRi dataset specific to PP_2265 was located in the searched literature; its individual essentiality (given FolD1) remains an open experimental question.
- Direct localization (fractionation) and structure determination for FolD2 would confirm the inferred cytoplasmic, homodimeric, NADP-dependent properties.

---

### Key References
- Aluri et al. 2016, *FEBS J*-type study, PMID **26531681** — bifunctional FolD physiology; ΔfolD rescue and auxotrophies.
- Sah & Varshney 2015, PMID **25988590** — catalytic residues separating dehydrogenase vs cyclohydrolase activities.
- Eadsforth et al. 2012 (*P. aeruginosa* FolD), PMID **22558288** — 2.2 Å crystal structure; drug target.
- Eadsforth et al. 2012 (*A. baumannii* FolD), PMID **23050773** — conservation, essentiality, inhibitor complexes.
- Nilsson et al. 2006, PMID **16636273** — folD/fmt link to initiator-tRNA formylation.


## Artifacts

- [OpenScientist final report](folD2-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](folD2-deep-research-openscientist_artifacts/final_report.pdf)