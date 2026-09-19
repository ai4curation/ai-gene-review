---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-13T02:25:17.530243'
end_time: '2026-08-13T02:42:40.554322'
duration_seconds: 1043.02
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: eutC
  gene_symbol: eutC
  uniprot_accession: Q88QF2
  protein_description: 'RecName: Full=Ethanolamine ammonia-lyase small subunit {ECO:0000255|HAMAP-Rule:MF_00601};
    Short=EAL small subunit {ECO:0000255|HAMAP-Rule:MF_00601}; EC=4.3.1.7 {ECO:0000255|HAMAP-Rule:MF_00601};'
  gene_info: Name=eutC {ECO:0000255|HAMAP-Rule:MF_00601}; OrderedLocusNames=PP_0542;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the EutC family. {ECO:0000255|HAMAP-
  protein_domains: EutC. (IPR009246); EutC_C. (IPR042251); EutC_N. (IPR042255); EutC
    (PF05985)
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
  path: eutC-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: eutC-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88QF2
- **Protein Description:** RecName: Full=Ethanolamine ammonia-lyase small subunit {ECO:0000255|HAMAP-Rule:MF_00601}; Short=EAL small subunit {ECO:0000255|HAMAP-Rule:MF_00601}; EC=4.3.1.7 {ECO:0000255|HAMAP-Rule:MF_00601};
- **Gene Information:** Name=eutC {ECO:0000255|HAMAP-Rule:MF_00601}; OrderedLocusNames=PP_0542;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the EutC family. {ECO:0000255|HAMAP-
- **Key Domains:** EutC. (IPR009246); EutC_C. (IPR042251); EutC_N. (IPR042255); EutC (PF05985)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "eutC" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'eutC' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **eutC** (gene ID: eutC, UniProt: Q88QF2) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *eutC* (Q88QF2) — Ethanolamine ammonia-lyase small subunit, *Pseudomonas putida* KT2440

## Gene/Protein Identity Verification

| Field | Value |
|---|---|
| UniProt | Q88QF2 |
| Gene | *eutC* (ordered locus **PP_0542**) |
| Organism | *Pseudomonas putida* KT2440 (ATCC 47054 / DSM 6125 / NCIMB 11950) |
| Protein | Ethanolamine ammonia-lyase (EAL) small subunit; **EC 4.3.1.7** |
| Length | 272 aa |
| Domains | Pfam **PF05985 (EutC)**; InterPro EutC (IPR009246), EutC_N (IPR042255), EutC_C (IPR042251) |
| Partner gene | *eutB* (PP_0543), EAL large subunit (Q88QF1) |

**Verification passed.** The gene symbol *eutC*, the EutC/PF05985 domain set, the EC number 4.3.1.7, and the immediately adjacent *eutB* large-subunit gene all agree with the UniProt-provided identity. The literature on "EutC" as the ethanolamine ammonia-lyase small subunit is directly on-target; no gene-symbol ambiguity was encountered. Direct biochemical/structural characterization exists for the *E. coli* and *Salmonella* orthologues; the *P. putida* protein is annotated by homology (HAMAP rule MF_00601), and I add a *P. putida*-specific genomic-context analysis below.

---

## 1. Summary (answer to the research question)

**EutC is the small (β) subunit of ethanolamine ammonia-lyase (EAL, EC 4.3.1.7), an adenosylcobalamin (coenzyme B12)-dependent enzyme.** Working as an obligate heterodimer with the large subunit EutB, EAL catalyzes the deamination of ethanolamine to **acetaldehyde + ammonia** by radical chemistry. EutC itself does not contain the catalytic TIM barrel; rather it partners with EutB to complete the cobalamin-binding pocket at the subunit interface and is required for a functional enzyme. In *P. putida* KT2440 the enzyme lets the cell use ethanolamine as a carbon and nitrogen source (given exogenous/endogenous B12), operating as a **soluble cytoplasmic enzyme** within a minimal, microcompartment-independent ethanolamine-utilization gene cluster.

---

## 2. Primary function: the catalyzed reaction and substrate specificity

**Reaction (EC 4.3.1.7, Rhea:15313):**

> ethanolamine → acetaldehyde + NH4⁺

EAL is the committed, first catabolic step of ethanolamine degradation. Comparative genomics states plainly that "ethanolamine-ammonia lyase, the enzyme that breaks ethanolamine into acetaldehyde and ammonia, is encoded by the gene tandem *eutBC*" (Tsoy et al., 2009, PMID 19783625). The products feed central metabolism: the ammonia serves as a nitrogen source, and acetaldehyde is oxidized (by the neighboring aldehyde dehydrogenase, below) toward acetyl-CoA/acetate as a carbon and energy source.

**Substrate specificity.** The physiological substrate is ethanolamine (2-aminoethanol). The family is characterized as deaminating "various vicinal amino-alcohols to oxo compounds" (UniProt FUNCTION, MF_00601), i.e. it is a vicinal-amino-alcohol ammonia-lyase; ethanolamine is the canonical and best substrate. The enzyme also deaminates **both enantiomers of 2-amino-1-propanol** (2-aminopropanol), non-stereospecifically; enantiomer-bound crystal structures rationalize the lower affinity for the (R)-form via a Val-α326 side-chain conformational change and predict pro-S hydrogen abstraction at C1 (Shibata et al., 2011, PMID 21142024), consistent with ¹⁵N-isotope-effect/EPR studies on ethanolamine and (R/S)-2-aminopropanol (Poyner et al., 2006, PMID 16734439). The specificity is thus narrow — small 1,2-amino alcohols. Crystallographic work shows the substrate is held by six hydrogen bonds to active-site residues, with Arg(α160) contributing binding through the substrate O1 hydroxyl (Shibata et al., 2010, PMID 20519496) — the spectator hydroxyl group is mechanistically essential (Wetmore et al., 2002, PMID 12440904).

**Note on division of labor.** The catalytic and substrate/cobalamin-binding residues lie on the **large subunit EutB**. Site-directed mutagenesis shows Arg160 of EutB is critical for both oligomer assembly and radical catalysis (R160A is inactive; R160K lowers k꜀ₐₜ/K_M ~180-fold) (Sun et al., 2008, PMID 18444665). This reinforces that **EutC is the non-catalytic structural partner** that completes the interfacial cobalamin site.

---

## 3. Mechanism and cofactor (radical, B12-dependent catalysis)

EAL is a **class II (adenosylcobalamin-dependent) isomerase/eliminase**. Its cofactor is **adenosylcob(III)alamin** (coenzyme B12; ChEBI:18408), which UniProt notes "binds between the large and small subunits."

The chemistry is radical-based, not hydrolytic:
1. Homolytic cleavage of the cobalt–carbon bond of AdoCbl generates a **5′-deoxyadenosyl radical** (Frey, 2001, PMID 11395404).
2. This radical abstracts a hydrogen atom from ethanolamine, producing a substrate radical.
3. The substrate radical undergoes a **1,2-amino-group shift** to a carbinolamine radical, which collapses to acetaldehyde + ammonia (Wetmore et al., 2002, PMID 12440904).

Experimental EPR of purified EAL confirms "the formation of substrate-derived radicals during catalysis and the binding of cobalamin in the base-on mode," i.e. with 5,6-dimethylbenzimidazole coordinating the cobalt (Akita et al., 2010, PMID 19762342).

---

## 4. Structural role of EutC (the small subunit) and localization within the enzyme

**Quaternary structure.** The functional unit is a **EutB·EutC heterodimer** (α·β) that assembles into a **heterododecamer (EutB)6(EutC)6** — "the enzyme existed as the heterododecamer α6β6" (Akita et al., 2010, PMID 19762342). Structurally it is a "trimer of the (αβ)2 dimer," with "6 large subunits form[ing] a core ring with 6 small subunits projecting outwards" (UniProt SUBUNIT; Shibata et al., 2010).

**What EutC does structurally.** The catalytic machinery — the (β/α)8 TIM barrel that holds the active site — resides in the **large subunit EutB**. The **small subunit EutC "covers the lower part of the cobalamin that is bound in the interface of the α- and β-subunits"** (Shibata et al., 2010, PMID 20519496). Thus EutC:
- forms the obligate protein partner of EutB (both genes are required for activity),
- helps build and cap the cobalamin-binding site at the subunit interface,
- is present in 1:1 stoichiometry with EutB, consistent with the finding that binding one cobalamin-analog inhibitor per αβ unit completely inhibits the enzyme (Akita et al., 2010).

**Domain architecture / evolution.** EutC arose by recruitment of a **Rossmann-fold domain fused to an N-terminal α-helical domain** (EutB is the paired TIM-barrel + N-terminal helical subunit) (Tsoy et al., 2009, PMID 19783625) — matching the InterPro EutC_N/EutC_C two-domain layout of Q88QF2. The N-terminal region is dispensable for catalysis: N-terminally truncated EAL retains catalytic properties, and "a short N-terminal sequence is sufficient to change the solubility and stability of the enzyme" (Akita et al., 2010).

---

## 5. Subcellular localization

EAL is a **cytoplasmic (soluble) enzyme**. In enterobacteria such as *Salmonella* and *E. coli*, EAL is encapsulated inside a **bacterial microcompartment (metabolosome)** — a proteinaceous organelle whose shell (e.g., EutL, PMID 19451619) confines the volatile/toxic intermediate acetaldehyde (Sturms et al., 2015, PMID 25962913). UniProt's HAMAP-inferred "Bacterial microcompartment" localization for Q88QF2 is transferred from these organisms.

**However, a *P. putida* KT2440-specific caveat applies.** Genomic-neighborhood analysis (this work) shows the KT2440 *eut* cluster is minimal — *eutC* (PP_0542), *eutB* (PP_0543), an ethanolamine transporter (PP_0544, EutH-like), an aldehyde dehydrogenase (PP_0545, *aldB-I*, EutE-like), and a σ54-dependent regulator (PP_0546) — and **contains no microcompartment shell-protein genes**. A **genome-wide** UniProt proteome search (this work) confirms this: Pfam **PF00936 = 0 hits**, Pfam **PF03319 = 0 hits**, keyword "carboxysome" = 0, and keyword "microcompartment" returns only *eutC*/*eutB* themselves. Therefore *P. putida* KT2440 builds **no** bacterial microcompartment, and EutBC functions as a **free cytoplasmic enzyme** rather than inside a BMC. The HAMAP-inferred microcompartment localization is an over-transfer from enterobacteria and should be regarded as inapplicable to this organism.

**Cofactor supply is intrinsic.** Although UniProt phrases activity as requiring "external vitamin B12," KT2440 encodes cobalamin biosynthesis/salvage genes (*cobN* PP_3507, *cobS* PP_1681, *cobD* PP_1675, *cobE* PP_3409) and — critically — the corrinoid adenosyltransferase **PduO (PP_1349, EC 2.5.1.17)** that generates **adenosylcobalamin**, the exact AdoCbl coenzyme EutBC requires, plus periplasmic cobalamin transport proteins (PP_2418; HutB PP_0524). The organism can therefore both import and adenosylate B12 to feed EAL.

---

## 6. Pathway context in *P. putida* KT2440

EutC functions in **amine degradation / ethanolamine catabolism** (UniProt PATHWAY). The reconstructed minimal pathway from the gene cluster:

1. **Uptake:** ethanolamine enters via the EutH-like transporter (PP_0544).
2. **Deamination:** cytoplasmic **EutBC (EutC = PP_0542 small subunit)** converts ethanolamine → acetaldehyde + NH3 using AdoCbl.
3. **Aldehyde oxidation:** the EutE-like aldehyde dehydrogenase (PP_0545, EC 1.2.1.3) oxidizes acetaldehyde, channeling carbon toward acetyl-CoA/acetate and central metabolism.
4. **Nitrogen assimilation:** released NH3 is assimilated as a nitrogen source.
5. **Regulation:** a σ54-dependent transcriptional regulator (PP_0546) controls cluster expression, consistent with the σ54 (RpoN)/NtrC regulatory cascade shown to govern *eut* loci in other proteobacteria (Barnes et al., 2024, PMID 38713723) and linking induction to nitrogen status.
6. **Cofactor dependency:** activity requires the coenzyme adenosylcobalamin; KT2440 supplies it via cobalamin biosynthesis/salvage plus the PduO corrinoid adenosyltransferase (PP_1349), and can also import B12 (PP_2418, HutB).

Ethanolamine itself is a widespread nutrient derived from turnover of the membrane phospholipid **phosphatidylethanolamine** (Kaval & Garsin, 2018, PMID 29463652); catabolizing it lets *P. putida* scavenge additional carbon and nitrogen from its (soil/rhizosphere and host-associated) environment.

This "stripped-down," microcompartment-free architecture is consistent with the variable *eut* gene content across bacteria, including loss/absence of auxiliary genes in many lineages (Tsoy et al., 2009, PMID 19783625).

---

## 7. Supported and refuted hypotheses

**Supported**
- EutC is the small subunit of AdoCbl-dependent EAL (EC 4.3.1.7) catalyzing ethanolamine → acetaldehyde + NH3. *(UniProt; PMID 19783625, 19762342)*
- EutC is an obligate structural partner of EutB, capping the interfacial cobalamin site in an (EutB)6(EutC)6 dodecamer. *(PMID 20519496, 19762342)*
- Catalysis proceeds via AdoCbl Co–C homolysis → 5′-deoxyadenosyl radical → 1,2-amino shift. *(PMID 11395404, 12440904, 19762342)*
- EutC = Rossmann-fold + N-terminal α-helical domain; N-terminus dispensable for catalysis. *(PMID 19783625, 19762342)*
- Substrate range is narrow (small 1,2-amino alcohols): ethanolamine (physiological) plus both enantiomers of 2-aminopropanol; catalytic residues (Arg160) reside on EutB, confirming EutC's structural (non-catalytic) role. *(PMID 21142024, 16734439, 18444665)*

**Refuted / corrected for this organism**
- The HAMAP-inferred "bacterial microcompartment" localization is **not** supported for *P. putida* KT2440. A genome-wide proteome scan finds **no** BMC shell-protein genes (Pfam PF00936 = 0, PF03319 = 0; "carboxysome" = 0), so EutC acts in the **cytoplasm**. *(genome-wide bioinformatic analysis; contrast with PMID 19451619, 25962913)*
- The "requires external vitamin B12" wording is only partially apt: KT2440 encodes cobalamin biosynthesis/salvage plus the PduO adenosyltransferase (PP_1349) that makes the AdoCbl coenzyme, so cofactor provision is intrinsic. *(bioinformatic analysis)*

## 8. Limitations and future directions

- Direct biochemical/structural data are from *E. coli*/*Salmonella* EAL; **no *P. putida*-specific experimental study of EutC was found** (literature searches returned none). The *P. putida* protein is annotated by strong homology (HAMAP) and reconstructed pathway logic, not by dedicated in-vitro study — assignments should be read as high-confidence inference.
- Confirmation that *P. putida* KT2440 grows on ethanolamine (as C and/or N source) and the B12 dependence would benefit from targeted growth/knockout experiments; the σ54-regulator and inducer are candidates for regulatory study.
- An AlphaFold/experimental structure of the *P. putida* EutBC complex could confirm the interfacial cobalamin-capping role of EutC in this organism.


## Artifacts

- [OpenScientist final report](eutC-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](eutC-deep-research-openscientist_artifacts/final_report.pdf)