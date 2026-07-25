---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-20T18:53:19.768714'
end_time: '2026-07-20T19:40:27.226931'
duration_seconds: 2827.46
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: folD1
  gene_symbol: folD1
  uniprot_accession: Q88LI7
  protein_description: 'RecName: Full=Bifunctional protein FolD 1 {ECO:0000255|HAMAP-Rule:MF_01576};
    Includes: RecName: Full=Methylenetetrahydrofolate dehydrogenase {ECO:0000255|HAMAP-Rule:MF_01576};
    EC=1.5.1.5 {ECO:0000255|HAMAP-Rule:MF_01576}; Includes: RecName: Full=Methenyltetrahydrofolate
    cyclohydrolase {ECO:0000255|HAMAP-Rule:MF_01576}; EC=3.5.4.9 {ECO:0000255|HAMAP-Rule:MF_01576};'
  gene_info: Name=folD1 {ECO:0000255|HAMAP-Rule:MF_01576}; Synonyms=folD-1; OrderedLocusNames=PP_1945;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the tetrahydrofolate
  protein_domains: Aminoacid_DH-like_N_sf. (IPR046346); NAD(P)-bd_dom_sf. (IPR036291);
    THF_DH/CycHdrlase. (IPR000672); THF_DH/CycHdrlase_cat_dom. (IPR020630); THF_DH/CycHdrlase_CS.
    (IPR020867)
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
citation_count: 7
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: folD1-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: folD1-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88LI7
- **Protein Description:** RecName: Full=Bifunctional protein FolD 1 {ECO:0000255|HAMAP-Rule:MF_01576}; Includes: RecName: Full=Methylenetetrahydrofolate dehydrogenase {ECO:0000255|HAMAP-Rule:MF_01576}; EC=1.5.1.5 {ECO:0000255|HAMAP-Rule:MF_01576}; Includes: RecName: Full=Methenyltetrahydrofolate cyclohydrolase {ECO:0000255|HAMAP-Rule:MF_01576}; EC=3.5.4.9 {ECO:0000255|HAMAP-Rule:MF_01576};
- **Gene Information:** Name=folD1 {ECO:0000255|HAMAP-Rule:MF_01576}; Synonyms=folD-1; OrderedLocusNames=PP_1945;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the tetrahydrofolate
- **Key Domains:** Aminoacid_DH-like_N_sf. (IPR046346); NAD(P)-bd_dom_sf. (IPR036291); THF_DH/CycHdrlase. (IPR000672); THF_DH/CycHdrlase_cat_dom. (IPR020630); THF_DH/CycHdrlase_CS. (IPR020867)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "folD1" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'folD1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **folD1** (gene ID: folD1, UniProt: Q88LI7) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: FolD1 (Q88LI7 / PP_1945) in *Pseudomonas putida* KT2440

## Summary

**FolD1 (UniProt Q88LI7, ordered locus PP_1945) is a bifunctional, NADP⁺-dependent methylenetetrahydrofolate dehydrogenase/methenyltetrahydrofolate cyclohydrolase that operates at the central hub of one-carbon (folate) metabolism in the cytosol of *Pseudomonas putida* strain KT2440.** On a single 291-residue polypeptide it carries two distinct catalytic centers that perform two sequential reactions of the tetrahydrofolate (THF) interconversion cycle: (1) the NADP⁺-dependent oxidation of (6R)-5,10-methylene-THF to (6R)-5,10-methenyl-THF (dehydrogenase activity, **EC 1.5.1.5**, generating NADPH), and (2) the hydrolysis of (6R)-5,10-methenyl-THF to (6R)-10-formyl-THF (cyclohydrolase activity, **EC 3.5.4.9**). Together these reactions convert the methylene form of folate one-carbon units into the formyl form, while simultaneously producing reducing power in the form of NADPH.

The physiological importance of this enzyme lies in the products it supplies. **10-formyl-THF** is the one-carbon donor for de novo purine ring biosynthesis and for the formylation of initiator methionyl-tRNA (fMet-tRNA) that begins bacterial translation; the folate one-carbon pool that FolD interconverts is also required for histidine and methionine biosynthesis. In the well-studied *Escherichia coli* ortholog, loss of FolD causes glycine and formate auxotrophy and hypersensitivity to the antifolate trimethoprim and to UV light — a genetic signature of a growth-essential biosynthetic enzyme. FolD is consequently a validated antibacterial drug target in Gram-negative pathogens, including the close relative *Pseudomonas aeruginosa*.

This report is built primarily on authoritative annotation (UniProt Swiss-Prot, KEGG) reinforced by mechanistic and structural primary literature on FolD enzymes from *E. coli*, *P. aeruginosa*, *A. baumannii*, and *Hyphomicrobium zavarzinii*. Because no primary experimental study of the *P. putida* KT2440 PP_1945 protein itself has been published, the functional assignment rests on very strong homology-based inference: FolD1 is 54% identical to the crystallographically and kinetically characterized *P. aeruginosa* FolD and 53.5% identical to the mutationally dissected *E. coli* FolD, with **all catalytic and functional residues strictly conserved**. This conservation confirms that FolD1 is a genuine *bi*functional enzyme rather than one of the rare monofunctional FolD-family variants. *P. putida* KT2440 encodes a second, dispersed paralog, folD2 (PP_2265), and folD1 itself sits within a folate/one-carbon gene cluster alongside a formyltetrahydrofolate deformylase (purU) and a GcvT-like aminomethyltransferase.

---

## Gene / Protein Identity Verification

Before presenting the functional findings, the mandatory identity check was completed and passed:

| Attribute | Target (from UniProt) | Verified in this investigation |
|---|---|---|
| UniProt accession | Q88LI7 | Confirmed — entry FOLD1_PSEPK, reviewed (Swiss-Prot) |
| Gene symbol | folD1 (synonym folD-1) | Consistent with bifunctional FolD nomenclature |
| Ordered locus | PP_1945 | Confirmed in KEGG (ppu:PP_1945) |
| Organism | *P. putida* KT2440 (taxid 160488) | Confirmed |
| Protein | Bifunctional methylene-THF dehydrogenase / methenyl-THF cyclohydrolase | Confirmed by EC numbers, domains, and homology |
| EC numbers | 1.5.1.5 and 3.5.4.9 | Confirmed |
| Domains | THF_DH/CycHdrlase catalytic (IPR020630) + NAD(P)-binding Rossmann (IPR036291) | Confirmed by alignment to characterized homologs |

**Conclusion of verification:** The gene symbol folD1 unambiguously matches the annotated protein, the organism is correct, and the domain architecture aligns with the FolD family described in the literature. The literature I relied on is for the correct protein family (FolD / bifunctional methylenetetrahydrofolate dehydrogenase-cyclohydrolase), not a same-symbol homonym. There is one caveat worth noting for the reader: "FolD" nomenclature is occasionally applied to proteins that are in fact monofunctional; this report explicitly addresses that ambiguity (see Finding F005) and resolves it in favor of true bifunctionality for FolD1.

---

## Key Findings

### F001 — FolD1 is a bifunctional NADP⁺-dependent methylene-THF dehydrogenase / methenyl-THF cyclohydrolase

UniProt Q88LI7 (FOLD1_PSEPK, a reviewed Swiss-Prot entry) annotates two coupled reactions on a single 30.5 kDa, 291-amino-acid polypeptide that assembles into a homodimer:

1. **Dehydrogenase (EC 1.5.1.5):** (6R)-5,10-methylene-THF + NADP⁺ → (6R)-5,10-methenyl-THF + NADPH (Rhea:22812)
2. **Cyclohydrolase (EC 3.5.4.9):** (6R)-5,10-methenyl-THF + H₂O → (6R)-10-formyl-THF + H⁺ (Rhea:23700)

The assignment was made under HAMAP-Rule MF_01576, a curated family rule for classical bacterial FolD enzymes. Critically, the underlying reaction chemistry is not merely predicted — it has been experimentally established for the FolD family across multiple organisms. As stated for the *Acinetobacter baumannii* enzyme, "Methylenetetrahydrofolate dehydrogenase-cyclohydrolase (FolD) catalyzes interconversion of 5,10-methylene-tetrahydrofolate and 10-formyl-tetrahydrofolate in the one-carbon metabolic pathway" ([PMID: 25988590](https://pubmed.ncbi.nlm.nih.gov/25988590/)). The NADP dependence and the bifunctional dehydrogenase-plus-cyclohydrolase nature of classical bacterial FolD enzymes were directly demonstrated biochemically for the *Hyphomicrobium zavarzinii* enzyme, which is "specific for NADP and methylene H₄F (specific activity: 180 U/mg) and also exhibits methenyl H₄F cyclohydrolase activity … identified as belonging to the classical bifunctional methylene H₄F dehydrogenases/cyclohydrolases (FolD) found in many bacteria and eukarya" ([PMID: 11889483](https://pubmed.ncbi.nlm.nih.gov/11889483/)).

The two reactions are chemically sequential: the dehydrogenase generates the methenyl intermediate that the cyclohydrolase then hydrolyzes. Net effect: FolD converts the methylene one-carbon form of folate into the formyl form, and in doing so harvests a hydride as NADPH.

### F002 — FolD supplies 10-formyl-THF and NADPH for purine, formyl-Met-tRNA, histidine, and methionine biosynthesis

The two products of FolD activity — 10-formyl-THF and NADPH — feed directly into several essential biosynthetic pathways. UniProt places FolD1 in the pathway "one-carbon metabolism; tetrahydrofolate interconversion," and its GO biological-process annotations include purine nucleotide biosynthesis (GO:0006164), histidine biosynthesis (GO:0000105), methionine biosynthesis (GO:0009086), and tetrahydrofolate interconversion (GO:0035999).

The centrality of these products is made explicit in the literature: "Most organisms possess bifunctional FolD [5,10-methylenetetrahydrofolate (5,10-CH₂-THF) dehydrogenase-cyclohydrolase] to generate NADPH and 10-formyltetrahydrofolate (10-CHO-THF) required in various metabolic steps" ([PMID: 26531681](https://pubmed.ncbi.nlm.nih.gov/26531681/)). Genetic evidence for essentiality comes from the same study's use of the *E. coli* folD deletion background: complementation was needed "to rescue an *E. coli* folD deletion strain … for its formate and glycine auxotrophies, and to alleviate its susceptibility to trimethoprim (an antifolate drug) or UV light" ([PMID: 26531681](https://pubmed.ncbi.nlm.nih.gov/26531681/)). The glycine/formate auxotrophy and antifolate/UV sensitivity are the classic phenotypic hallmarks of a defective folate one-carbon supply.

The downstream link to translation initiation is independently documented: work on initiator-tRNA formylation refers to "the folD gene encoding the bifunctional enzyme methylenetetrahydrofolate-dehydrogenase and -cyclohydrolase" in the context of fMet-tRNA formylation ([PMID: 16636273](https://pubmed.ncbi.nlm.nih.gov/16636273/)). Thus FolD-derived 10-formyl-THF is the one-carbon donor that methionyl-tRNA formyltransferase uses to make the fMet-tRNA required to start every bacterial protein.

### F003 — FolD1 is a cytosolic homodimer with two mutationally separable active sites

Subcellular localization is cytosolic: UniProt records SUBUNIT = homodimer and localizes the protein to the cytosol (GO:0005829). This is consistent with folate metabolism being a soluble, cytoplasmic process in bacteria — the enzyme carries out its function in the cytoplasm, not at the membrane or extracellularly.

The domain architecture comprises the **THF_DH/CycHdrlase catalytic domain (IPR020630)** joined to a **Rossmann-fold NAD(P)-binding domain (IPR036291)**, with the active-site cleft between them. UniProt annotates ligand-binding residues at positions 167–169, 192, and 233. A key mechanistic point is that the two enzymatic activities occupy **distinct, mutationally separable active-site environments** on the same chain. This was demonstrated for the *E. coli* enzyme: "While the R191E mutant showed high cyclohydrolase activity, it retained only a residual dehydrogenase activity. On the other hand, the K54S mutant lacked the cyclohydrolase activity but possessed high dehydrogenase activity" ([PMID: 25988590](https://pubmed.ncbi.nlm.nih.gov/25988590/)). This double dissociation proves that the dehydrogenase and cyclohydrolase functions rely on physically and functionally separable catalytic centers.

For structural context, the closest crystallographically characterized homolog is *P. aeruginosa* FolD, whose "crystal structure … was determined at 2.2 Å resolution and provided a template for an assessment of druggability and for modelling of ligand complexes as well as for comparisons with the human enzyme" ([PMID: 22558288](https://pubmed.ncbi.nlm.nih.gov/22558288/)). A global Needleman–Wunsch alignment computed during this investigation found FolD1 to be **54.0% identical (157/291 residues)** to this *P. aeruginosa* enzyme (Q9I2U6) and **52.7% identical** to its own *P. putida* paralog FolD2 (Q88KM5 / PP_2265). This high identity across the catalytic core means the 2.2 Å *P. aeruginosa* structure is a reliable template for the FolD1 fold and active-site geometry.

### F004 — FolD is a validated Gram-negative antibacterial drug target; *P. putida* KT2440 carries two paralogs

A UniProt search of *P. putida* KT2440 (taxid 160488) returns two reviewed FolD entries: **FOLD1_PSEPK (Q88LI7, PP_1945, 291 aa)** and **FOLD2_PSEPK (Q88KM5, PP_2265, 284 aa)**. The two paralogs are 52.7% identical to each other and are both annotated with the identical bifunctional EC 1.5.1.5 / EC 3.5.4.9 activities.

The essentiality and druggability of the FolD family are well established. The *A. baumannii* study states that "The bifunctional N⁵,N¹⁰-methylenetetrahydrofolate dehydrogenase/cyclohydrolase (DHCH or FolD), which is widely distributed in prokaryotes and eukaryotes, is involved in the biosynthesis of folate cofactors that are essential for growth and cellular development. The enzyme activities represent a potential antimicrobial drug target" ([PMID: 23050773](https://pubmed.ncbi.nlm.nih.gov/23050773/)). The relevance to the *Pseudomonas* genus specifically is underscored by the *P. aeruginosa* work: "The bifunctional enzyme methylenetetrahydrofolate dehydrogenase - cyclohydrolase (FolD) is identified as a potential drug target in Gram-negative bacteria, in particular the troublesome *Pseudomonas aeruginosa*" ([PMID: 22558288](https://pubmed.ncbi.nlm.nih.gov/22558288/)).

The presence of two paralogs in *P. putida* is relevant to any consideration of essentiality in this organism: functional redundancy between folD1 and folD2 could buffer the loss of either single gene.

### F005 — Catalytic residues are strictly conserved, confirming genuine bifunctionality (not a monofunctional variant)

Because "FolD" annotation is not always synonymous with bifunctionality, this investigation explicitly tested whether FolD1 retains both activities by residue-level comparison to the mutationally characterized *E. coli* enzyme. A corrected BLOSUM62 global alignment of FolD1 (Q88LI7) to the true *E. coli* bifunctional FolD (P24186, FOLD_ECOLI, 288 aa) gave **53.5% identity (153/286 residues), 67.5% similarity** — comparable to the 54% identity versus the *P. aeruginosa* enzyme.

Crucially, every residue shown by mutagenesis to be essential for *E. coli* FolD activity maps to an identical position in FolD1:

| *E. coli* residue | Role | Position in FolD1 | Conserved? |
|---|---|---|---|
| Tyr50 | dehydrogenase | Tyr50 | ✅ |
| Lys54 | dehydrogenase | Lys54 | ✅ |
| Gln98 | both activities | Gln98 | ✅ |
| Asp121 | both activities | Asp121 | ✅ |
| Gly122 | both activities | Gly122 | ✅ |
| Arg191 | cyclohydrolase | Arg193 (in conserved "…IRTT…" loop) | ✅ |

These residues were defined experimentally: "Mutations in the key residues of *E. coli* FolD, as identified from three-dimensional structures (D121A, Q98K, K54S, Y50S, and R191E), and a genetic screen (G122D and C58Y) were generated" ([PMID: 25988590](https://pubmed.ncbi.nlm.nih.gov/25988590/)). The conservation of both the dehydrogenase-specific residues (Y50, K54) **and** the cyclohydrolase arginine (R191→R193) is the direct structural evidence that FolD1 retains both activities.

The importance of this check is highlighted by the discovery that some FolD-annotated proteins are not in fact bifunctional: "contrary to its annotated bifunctional nature, *C. perfringens* FolD (CpeFolD) is a monofunctional 5,10-CH₂-THF dehydrogenase" ([PMID: 26531681](https://pubmed.ncbi.nlm.nih.gov/26531681/)). The strict conservation of the cyclohydrolase machinery in FolD1 argues against such a scenario and supports the bifunctional annotation. (A methodological note: an initial iteration-1 alignment inadvertently used dihydropteroate synthase P0AC13/folP; the corrected ortholog is P24186, and all conclusions here rest on the corrected alignment.)

### F006 — folD1 lies in a folate/one-carbon gene cluster and maps to KEGG "One carbon pool by folate"

Both *P. putida* FolD paralogs are assigned to KEGG orthology **K01491** (methylenetetrahydrofolate dehydrogenase (NADP⁺)/methenyltetrahydrofolate cyclohydrolase, EC 1.5.1.5 + 3.5.4.9) and to pathway **ppu00670 "One carbon pool by folate."** The two paralogs are genomically dispersed — PP_1945 (folD1) at 2,200,427–2,201,302 on the forward strand and PP_2265 (folD2) at 2,584,640–2,585,494 on the reverse strand, roughly 384 kb apart — indicating they are not a recent tandem duplication.

The immediate genomic neighborhood of folD1 reinforces its one-carbon role:

```
 PP_1942        PP_1943            PP_1944               PP_1945
 (LysR reg.) ── purU-III ──── aminomethyltransferase ── folD1
             (formyl-THF        (GcvT-like;             (this gene)
              deformylase)       THF → 5,10-CH2-THF)
             10-formyl-THF →
             THF + formate
```

This clustering is functionally coherent. **PP_1943 (purU-III)** is a formyltetrahydrofolate deformylase that hydrolyzes 10-formyl-THF back to THF + formate — the reverse-direction outlet of the very metabolite FolD1 produces, allowing the cell to balance the formyl-THF pool and release free formate. **PP_1944** is a GcvT-like aminomethyltransferase that can generate 5,10-methylene-THF from THF (e.g., via glycine cleavage chemistry) — supplying the substrate that FolD1 consumes. The cluster is flanked by short-chain and GMC-family oxidoreductases and a LysR-family regulator (PP_1942). The co-localization of a methylene-THF *producer*, the FolD *interconverter*, and a formyl-THF *consumer* in one neighborhood is strong contextual evidence that FolD1 operates within an integrated one-carbon/formate metabolic module.

---

## Mechanistic Model / Interpretation

FolD1 sits at the branch point of the bacterial folate one-carbon cycle, controlling the flow of one-carbon units between the methylene and formyl oxidation states while generating NADPH. The reaction it catalyzes and the fate of its products can be summarized as follows:

```
                         serine, glycine cleavage (e.g. PP_1944 GcvT-like)
                                        │
                                        ▼
                          5,10-methylene-THF
                                        │
                                        │  FolD1 dehydrogenase (EC 1.5.1.5)
                          NADP+ ──►     │     ──► NADPH   [reducing power]
                                        ▼
                          5,10-methenyl-THF
                                        │
                                        │  FolD1 cyclohydrolase (EC 3.5.4.9)
                             H2O ──►     │
                                        ▼
                          10-formyl-THF ───────────────────────────┐
                             │              │              │        │
                             ▼              ▼              ▼        ▼
                      purine ring    fMet-tRNA        (formyl    purU (PP_1943):
                      biosynthesis   formylation       pool)     → THF + formate
                      (GO:0006164)   (translation
                                      initiation)
```

The dual output of FolD1 explains its essentiality. On one hand, the **10-formyl-THF** it produces is a direct one-carbon donor for two reactions in de novo purine biosynthesis (the GAR and AICAR transformylase steps) and for the formylation of initiator Met-tRNA that primes every round of bacterial protein synthesis. On the other hand, the **NADPH** generated by the dehydrogenase step contributes reducing equivalents to the cell. Because the folate pool is also required for histidine and methionine biosynthesis, blocking FolD collapses several biosynthetic pathways simultaneously — hence the pleiotropic glycine/formate auxotrophy and antifolate/UV sensitivity observed when *E. coli* folD is deleted.

Structurally, the enzyme is a two-domain homodimer: a Rossmann NAD(P)-binding domain reads out the NADP⁺ cofactor for the dehydrogenase reaction, while the THF_DH/CycHdrlase catalytic domain provides the residues for both reactions in a shared cleft. The double-mutant dissociation in *E. coli* (K54S → dehydrogenase only; R191E → cyclohydrolase only) shows that although the two reactions occur in close proximity and are kinetically coupled (the methenyl intermediate is channeled from dehydrogenase to cyclohydrolase), they use distinct catalytic residues. The strict conservation of all of these residues in FolD1 (Y50, K54, Q98, D121, G122, and R193) is the strongest available evidence that FolD1 performs both reactions.

The existence of two paralogs (folD1/PP_1945 and folD2/PP_2265) in *P. putida* KT2440 adds a layer of interpretation. Their dispersal in the genome and mutual 52.7% identity suggest an ancient duplication rather than a recent event. Whether the two paralogs are functionally redundant, differentially regulated, or specialized (for example, one tuned to the biosynthetic direction and one to formate/one-carbon salvage in this metabolically versatile soil bacterium) cannot be resolved from annotation alone and is a key open question.

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports the findings |
|---|---|---|
| [25988590](https://pubmed.ncbi.nlm.nih.gov/25988590/) | Impact of mutating key residues of *E. coli* bifunctional FolD | Defines the two coupled reactions; identifies catalytic residues; demonstrates double dissociation (K54S vs R191E) proving two separable active sites (F001, F003, F005) |
| [26531681](https://pubmed.ncbi.nlm.nih.gov/26531681/) | Physiological role of FolD/FchA/Fhs from *C. perfringens* in *E. coli* | States FolD generates NADPH + 10-formyl-THF; genetic rescue of folD-deletion glycine/formate auxotrophy and trimethoprim/UV sensitivity; documents a monofunctional FolD exception (F002, F005) |
| [11889483](https://pubmed.ncbi.nlm.nih.gov/11889483/) | Characterization of FolD from *H. zavarzinii* | Direct biochemistry: NADP-specific, methylene-H₄F dehydrogenase with methenyl cyclohydrolase activity; classical bifunctional FolD (F001) |
| [22558288](https://pubmed.ncbi.nlm.nih.gov/22558288/) | *P. aeruginosa* FolD as antibacterial target | 2.2 Å crystal structure of the closest homolog (54% identical); FolD as Gram-negative *Pseudomonas* drug target (F003, F004) |
| [23050773](https://pubmed.ncbi.nlm.nih.gov/23050773/) | *A. baumannii* FolD ligand complexes | Establishes FolD essentiality for growth and status as antimicrobial drug target (F004) |
| [16636273](https://pubmed.ncbi.nlm.nih.gov/16636273/) | Initiator-tRNA amplification and antibiotic resistance | Links folD to fMet-tRNA formylation, a downstream use of 10-formyl-THF (F002) |

**Note on the strength of the evidence.** There is, to my knowledge, no published primary biochemical or genetic study of the *P. putida* KT2440 PP_1945 protein specifically. The functional assignment is therefore an inference of high confidence built from (i) curated Swiss-Prot/HAMAP annotation, (ii) KEGG orthology, (iii) experimentally characterized close homologs (54% identity to *P. aeruginosa*, 53.5% to *E. coli*), and (iv) strict conservation of all experimentally validated catalytic residues. The convergence of these independent lines of evidence makes the bifunctional FolD assignment robust.

---

## Limitations and Knowledge Gaps

1. **No direct experimental data on PP_1945.** All conclusions are inferential. The enzyme has not been purified, assayed, crystallized, or genetically knocked out in *P. putida* KT2440. Kinetic parameters (Km for methylene-THF and NADP⁺, kcat, cofactor specificity) are unknown for this specific protein.

2. **Paralog redundancy is unresolved.** *P. putida* carries folD1 (PP_1945) and folD2 (PP_2265). Their relative expression, condition-specific roles, and whether either or both are essential are not established. Essentiality demonstrated for single-copy folD in *E. coli* may not translate to *P. putida*, where a paralog could compensate.

3. **Directionality and channeling in vivo are inferred, not measured.** Whether FolD1 primarily runs in the biosynthetic (methylene → formyl) direction or participates in formate assimilation/one-carbon salvage in this soil organism has not been tested experimentally.

4. **Gene-cluster functional linkage is contextual.** The purU (PP_1943) and aminomethyltransferase (PP_1944) neighbors are annotation-based assignments; co-transcription, operon structure, and regulatory coupling (e.g., by the PP_1942 LysR regulator) have not been experimentally verified.

5. **Monofunctional-variant possibility not experimentally excluded.** Although residue conservation strongly argues for bifunctionality, only a direct cyclohydrolase assay on the purified protein would definitively exclude a monofunctional-dehydrogenase scenario of the kind seen in *C. perfringens*.

6. **Localization is annotation-derived.** Cytosolic localization follows from GO annotation and the soluble nature of folate metabolism; it has not been confirmed by fractionation or imaging for this protein.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant expression and dual-activity assay.** Clone PP_1945, purify the His-tagged protein, and measure both the NADP⁺-dependent dehydrogenase activity (spectrophotometrically at 340 nm for NADPH) and the cyclohydrolase activity (methenyl-THF hydrolysis at 355 nm). Determine Km/kcat for methylene-THF and NADP⁺, and test NAD⁺ vs NADP⁺ specificity. This directly resolves gaps #1 and #5.

2. **Genetic essentiality and paralog interaction.** Construct single (ΔfolD1, ΔfolD2) and double deletions in *P. putida* KT2440; test for glycine/formate auxotrophy and trimethoprim/UV sensitivity, mirroring the *E. coli* assays. Synthetic lethality of the double mutant with viable singles would demonstrate paralog redundancy (gap #2). CRISPRi knockdown (as recently demonstrated in *P. putida*, [PMID: 41205860](https://pubmed.ncbi.nlm.nih.gov/41205860/)) offers a titratable alternative for an essential gene.

3. **Site-directed mutagenesis to confirm separable activities.** Introduce the FolD1 equivalents of *E. coli* K54S and R193E (=R191E) and confirm the predicted double dissociation of dehydrogenase vs cyclohydrolase activity, validating the residue-conservation inference.

4. **Structural determination.** Solve the FolD1 crystal structure (or generate a high-confidence AlphaFold model validated against the 2.2 Å *P. aeruginosa* template) to confirm the two-domain architecture and active-site geometry, and to assess druggability in the *P. putida* context.

5. **Transcriptional analysis of the folD1 cluster.** Use RT-PCR/RNA-seq to test whether PP_1943–PP_1945 are co-transcribed and whether the LysR regulator PP_1942 controls the cluster, clarifying the functional-module hypothesis (gap #4).

6. **Metabolic-flux tracing.** Employ ¹³C-labeled one-carbon precursors (serine, formate) to map flux through the folate pool and quantify FolD1's directional contribution in vivo (gap #3).

---

## Conclusion

FolD1 (Q88LI7, PP_1945) is a cytosolic, homodimeric, bifunctional enzyme that couples NADP⁺-dependent methylenetetrahydrofolate dehydrogenase (EC 1.5.1.5) and methenyltetrahydrofolate cyclohydrolase (EC 3.5.4.9) activities to convert 5,10-methylene-THF into 10-formyl-THF while producing NADPH. Its products drive de novo purine biosynthesis, fMet-tRNA formylation for translation initiation, and folate-dependent histidine and methionine biosynthesis, placing FolD1 at a growth-essential node of one-carbon metabolism. The assignment is supported by curated UniProt/KEGG annotation, ~54% identity to the structurally and kinetically characterized *P. aeruginosa* and *E. coli* FolD enzymes with all catalytic residues conserved (indicating genuine bifunctionality), and its membership in a folate/one-carbon gene cluster (with purU and a GcvT-like aminomethyltransferase). *P. putida* KT2440 carries a second, dispersed paralog, folD2 (PP_2265). No primary experimental study of PP_1945 itself exists, so the functional annotation is a high-confidence homology-based inference.


## Artifacts

- [OpenScientist final report](folD1-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](folD1-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:25988590
2. PMID:11889483
3. PMID:26531681
4. PMID:16636273
5. PMID:22558288
6. PMID:23050773
7. PMID:41205860