---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-13T00:06:54.757387'
end_time: '2026-08-13T00:21:07.293818'
duration_seconds: 852.54
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_1703
  gene_symbol: PP_1703
  uniprot_accession: Q88M71
  protein_description: 'SubName: Full=Assimilatory nitrate reductase/sulfite reductase
    {ECO:0000313|EMBL:AAN67324.2}; EC=1.7.99.4 {ECO:0000313|EMBL:AAN67324.2};'
  gene_info: OrderedLocusNames=PP_1703 {ECO:0000313|EMBL:AAN67324.2};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the prokaryotic molybdopterin-containing
  protein_domains: Asp_de-COase-like_dom_sf. (IPR009010); CT_Nitrate-R-NapA-like.
    (IPR041957); CysJ-like_FAD-binding. (IPR003097); FAD-bd_FR_type. (IPR017927);
    Flavdoxin-like. (IPR001094)
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
  path: PP_1703-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PP_1703-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88M71
- **Protein Description:** SubName: Full=Assimilatory nitrate reductase/sulfite reductase {ECO:0000313|EMBL:AAN67324.2}; EC=1.7.99.4 {ECO:0000313|EMBL:AAN67324.2};
- **Gene Information:** OrderedLocusNames=PP_1703 {ECO:0000313|EMBL:AAN67324.2};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the prokaryotic molybdopterin-containing
- **Key Domains:** Asp_de-COase-like_dom_sf. (IPR009010); CT_Nitrate-R-NapA-like. (IPR041957); CysJ-like_FAD-binding. (IPR003097); FAD-bd_FR_type. (IPR017927); Flavdoxin-like. (IPR001094)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_1703" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_1703' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_1703** (gene ID: PP_1703, UniProt: Q88M71) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# PP_1703 (Q88M71) — Functional Annotation Report

**Gene:** PP_1703 (OrderedLocusNames PP_1703) · **UniProt:** Q88M71 · **Organism:** *Pseudomonas putida* strain KT2440 (ATCC 47054 / DSM 6125 / NCIMB 11950) · **Nominal EC:** 1.7.99.4

---

## Summary

PP_1703 (UniProt **Q88M71**) encodes the **assimilatory nitrate reductase (Nas)** of *Pseudomonas putida* KT2440 — a large (1,341-amino-acid) soluble, cytoplasmic molybdoenzyme that catalyzes the first and rate-limiting step of nitrate assimilation: the two-electron reduction of nitrate to nitrite (NO₃⁻ + 2e⁻ + 2H⁺ → NO₂⁻ + H₂O). The enzyme uses NAD(P)H as its physiological electron donor. Its most distinctive structural feature is that it is a **self-contained monomeric "diflavin" nitrate reductase**: a single polypeptide fuses an N-terminal molybdopterin catalytic module (Mo-bis(molybdopterin guanine dinucleotide) plus a [4Fe-4S] cluster) to a C-terminal NAD(P)H diaphorase module containing both FAD and FMN. This architecture allows one polypeptide to accept electrons from NAD(P)H and relay them internally all the way to the molybdenum active site, without requiring separate electron-transfer partner proteins.

Functionally, PP_1703 sits at the head of the nitrate assimilation pathway. Its nitrite product is handed to the adjacent NAD(P)H-dependent nitrite reductase **nirBD** (encoded by the neighbouring genes PP_1705/PP_1706), which reduces nitrite to ammonium. The ammonium generated then feeds the **glutamine synthetase / glutamate synthase (GS/GOGAT)** cycle for incorporation into amino acids. Consistent with an assimilatory (biosynthetic) rather than respiratory role, the gene is induced under nitrogen limitation (ammonium deficiency) and its expression is genetically coupled to the GOGAT subunit gene *gltB*.

Two database labels attached to this protein are **automated misannotations** that should be treated with caution. The UniProt "periplasmic nitrate reductase NapAB / signal peptide" annotation and the KEGG "sulfite reductase (NADPH) flavoprotein CysJ (K00380, EC 1.8.1.2)" assignment both arise from recognition of a *single* shared domain rather than the full protein architecture. The full domain map — a molybdopterin catalytic core fused to a diflavin reductase — is incompatible with both periplasmic NapA (which lacks a fused diaphorase) and with sulfite reductase (which uses siroheme, absent here). The correct primary function is **cytoplasmic assimilatory nitrate reduction**.

---

## Protein Identity and Verification

| Property | Value |
|---|---|
| UniProt | Q88M71 |
| Locus | PP_1703 (KEGG `ppu:PP_1703`) |
| Organism | *Pseudomonas putida* KT2440 (PSEPK) |
| Length | 1,341 aa |
| Submitted name | Assimilatory nitrate reductase/sulfite reductase; EC 1.7.99.4 |
| Family (UniProt) | Prokaryotic molybdopterin-containing oxidoreductase, NasA/NapA/NarB subfamily |
| Orthology | COG0243 (Mo oxidoreductase) + COG0369 (CysJ/CPR-like diflavin reductase) |

The submitted UniProt name, the "Nitrate assimilation / Molybdenum / 4Fe-4S / FAD / FMN / NADP" keyword set, and the annotated cofactor list all point to an assimilatory nitrate reductase. Independent genetic work in the KT2440 lineage identified the assimilatory nitrate reductase gene *nasB* ([PMID: 10852866](https://pubmed.ncbi.nlm.nih.gov/10852866/)), and the domain architecture is fully consistent. This confirms the research target; the analysis below is specific to it. The gene symbol PP_1703 is **not** ambiguous once the full domain architecture is considered — the analysis explicitly resolves the two competing database labels (see Finding F003 and F006).

---

## Key Findings

### F001 — PP_1703 is the cytoplasmic assimilatory nitrate reductase (Nas), reducing nitrate to nitrite

The core identity of Q88M71 is an assimilatory nitrate reductase. The UniProt submitted name is "Assimilatory nitrate reductase" (EC 1.7.99.4), and the annotated cofactor set — Mo-bis(molybdopterin guanine dinucleotide), a [4Fe-4S] cluster, FAD, and FMN, together with keywords "Nitrate assimilation," "Molybdenum," "4Fe-4S," "FAD," "FMN," and "NADP" — is exactly the cofactor complement expected for an NAD(P)H-driven molybdopterin nitrate reductase. The sequence-similarity classification places the protein in the prokaryotic molybdopterin-containing oxidoreductase family, in the NasA/NapA/NarB subfamily of nitrate-reducing enzymes.

Direct genetic evidence for this identity in the *P. putida* KT2440 lineage comes from work on the closely related strain KT2442. A transposon-tagging study identified an insertion within the **assimilatory nitrate reductase gene *nasB*** of *P. putida* KT2442, a gene induced under ammonium deficiency ([PMID: 10852866](https://pubmed.ncbi.nlm.nih.gov/10852866/)). The verbatim finding — *"is demonstrated to bear the transposon within the assimilatory nitrate reductase gene (nasB) of P. putida KT2442"* — provides a direct genetic name for the assimilatory nitrate reductase in this organism, corresponding to the PP_1703 locus in the sequenced KT2440 genome.

The reaction chemistry and electron-donor logic are supported by comparative biochemistry in the related organism *Acinetobacter calcoaceticus*, whose soluble assimilatory nitrate reductase reduces nitrate to nitrite using either chemically reduced viologen dyes or, physiologically, NAD(P)H acting through specific diaphorases ([PMID: 849099](https://pubmed.ncbi.nlm.nih.gov/849099/)): *"The reduction of nitrate to nitrite is mediated by an enzyme of 96000 molecular weight that can use as electron donors either viologen dyes chemically reduced with dithionite or enzymatically reduced with NAD(P)H, through specific diaphorases."* This establishes both the catalyzed reaction (nitrate → nitrite) and the NAD(P)H/diaphorase mode of electron donation that characterizes bacterial assimilatory nitrate reductases.

**Reaction catalyzed:**

```
NO3-  +  NAD(P)H  +  H+   -->   NO2-  +  NAD(P)+  +  H2O
```

### F002 — A large (1,341-aa) monomeric diflavin enzyme fusing a Mo-bisMGD/[4Fe-4S] core to an FAD+FMN NAD(P)H diaphorase

The domain architecture of Q88M71 explains how a single polypeptide performs the complete electron-transfer chain from NAD(P)H to nitrate. Mapping InterPro/Pfam domains onto the 1,341-residue sequence gives two clearly separable modules:

| Region (approx. residues) | Domain (Pfam / InterPro) | Role |
|---|---|---|
| 3–59 | Molybdop_Fe4S4 (PF04879) | Binds N-terminal [4Fe-4S] cluster |
| ~60–800 | Molybdopterin (PF00384) + Molydop_binding (PF01568); COG0243; IPR041957 CT_Nitrate-R-NapA-like | Mo-bis(MGD) catalytic center; nitrate reduction site |
| 819–957 | Flavodoxin-like / FMN domain (PF00258; IPR001094) | Binds FMN |
| 981–1191 | FAD-binding FR-type (PF00667; IPR017927) | Binds FAD |
| C-terminal | NAD_binding_1 (PF00175); CysJ-like FAD-binding (IPR003097); NADPH-cyt-P450-reductase-alpha (IPR023173); COG0369 | NAD(P)H binding / diaphorase |

The N-terminal sequence **MANSEVRSVCPYCGVGCGIVMS** carries the characteristic **CxxCxxCxxxG** cysteine motif (CPYCGVGCG) that ligates the [4Fe-4S] cluster — an iron-sulfur-binding motif, not an export signal. The combination of a molybdopterin catalytic core with a C-terminal diflavin (FAD + FMN) reductase module is precisely the "diflavin-containing monomeric nitrate reductase" architecture described as being responsible for highly efficient bacterial nitrate assimilation ([PMID: 32111737](https://pubmed.ncbi.nlm.nih.gov/32111737/)): the assimilatory nitrate reductase (NAS) *"catalyzes the rate-limiting reduction of nitrate to nitrite."* This confirms both the NAS function and the fused diflavin+Mo design that lets Q88M71 operate as a self-sufficient monomer.

### F003 — The protein functions in the cytoplasm; "periplasmic NapAB / signal peptide" is an automated misannotation

Q88M71 carries **no signal-peptide or transit-peptide feature** in UniProt; its only structural features are the three domains listed above ([4Fe-4S] Mo/W bis-MGD 3–59, Flavodoxin-like 819–957, FAD-binding FR-type 981–1191). The N-terminal cysteine-rich motif (CPYCGVGCG) is a [4Fe-4S]-ligating motif, **not** a Sec- or Tat-type export signal, so there is no sequence basis for periplasmic export.

The conflicting automated FUNCTION statement — describing Q88M71 as the "catalytic subunit of the periplasmic nitrate reductase complex NapAB … receiving electrons from NapB" — is an ARBA rule transfer (evidence code ECO:0000256) that is directly contradicted by the protein's own architecture. Genuine periplasmic NapA is a stand-alone Mo-protein that receives electrons from a separate small partner (NapB) and lacks any fused flavin diaphorase. Q88M71, by contrast, contains its own fused FAD+FMN NAD(P)H diaphorase, which is a hallmark of the *cytoplasmic assimilatory* enzymes, not the periplasmic respiratory Nap system. Comparative biochemistry reinforces cytoplasmic localization: the assimilatory nitrate reductase of *Acinetobacter calcoaceticus* is a **soluble** enzyme ([PMID: 849099](https://pubmed.ncbi.nlm.nih.gov/849099/)): *"A soluble nitrate reductase from the bacterium Acinetobacter calcoaceticus grown on nitrate has been characterized."* Soluble assimilatory enzymes of this type act in the cytoplasm, where NAD(P)H is available as the reductant.

### F004 — PP_1703 acts in nitrate assimilation feeding the GS/GOGAT route, and is induced under nitrogen limitation

The physiological context of the enzyme is nitrogen scavenging. The KT2442 genetics study showed that *nasB* is **induced upon ammonium deficiency** (nitrogen limitation) — the reporter screen selected *"insertion mutants that responded to ammonium deficiency by induction of bioluminescence"* ([PMID: 10852866](https://pubmed.ncbi.nlm.nih.gov/10852866/)). This establishes nitrogen-status-dependent regulation: the enzyme is made when preferred nitrogen (ammonium) is scarce and the cell must assimilate nitrate instead.

The same study genetically links assimilatory nitrate reductase expression to the downstream ammonium-assimilation machinery. Second-site mutations that abolished *nasB* induction mapped to *gltB*, encoding the major (large) subunit of **glutamate synthase (GOGAT)**: *"in all three mutants the secondary transposon had inserted at different sites in the gltB gene of P. putida KT2442 encoding the major subunit of the glutamate synthase."* *gltB* mutants cannot use nitrate or other nitrogen sources, tying the nitrate-reduction step to the GS/GOGAT cycle that ultimately fixes ammonium into glutamate/glutamine. Consistent with an assimilatory role, this class of enzyme is repressed by ammonia ([PMID: 849099](https://pubmed.ncbi.nlm.nih.gov/849099/)), and the UniProt keywords for Q88M71 include "Nitrate assimilation" and "Amino-acid biosynthesis."

### F005 — Genomic adjacency to nirBD couples nitrate reduction to nitrite reduction and ammonium production

The genomic neighbourhood cements the pathway assignment. In the KEGG *P. putida* KT2440 genome (organism code *ppu*), the genes immediately downstream of PP_1703 encode the two-subunit NAD(P)H nitrite reductase:

| Locus | Gene | KEGG KO | Product |
|---|---|---|---|
| **PP_1703** | *nasB* | (Mo nitrate reductase) | **Assimilatory nitrate reductase (this protein)** |
| PP_1704 | — | — | Short uncharacterized ORF |
| PP_1705 | *nirB* | K00362 | Nitrite reductase [NAD(P)H], large subunit |
| PP_1706 | *nirD* | K00363 | Nitrite reductase [NAD(P)H], small subunit |

PP_1703 (genome coordinates ≈ 1,899,450–1,903,475) lies immediately upstream of *nirBD*. The nitrate reductase is therefore co-localized with — and functionally coupled to — the NAD(P)H nitrite reductase that reduces its own product (nitrite) onward to ammonium. This clustering is the classic *nas* assimilatory operon organization: nitrate → nitrite (PP_1703) → ammonium (PP_1705/PP_1706), and it argues decisively against a sulfur-metabolism role.

### F006 — The KEGG "sulfite reductase flavoprotein CysJ (K00380)" call is a domain-driven misannotation

KEGG assigns ppu:PP_1703 to **K00380** ("sulfite reductase (NADPH) flavoprotein alpha component, CysJ," EC 1.8.1.2) and places it in sulfur-metabolism modules (assimilatory sulfate reduction, M00176/M00616). This is incorrect. A bona fide CysJ — for example *E. coli* P38038 — is only ~599 aa and consists **solely** of a Flavodoxin-like domain plus an FAD-binding FR-type domain, with **no molybdopterin motif**. PP_1703 is more than twice that size (1,341 aa) and contains full molybdopterin catalytic domains (Pfam Molybdopterin, Molydop_binding, Molybdop_Fe4S4) that bind Mo-bis(MGD) and a [4Fe-4S] cluster — features entirely absent from sulfite reductases, which instead use a **siroheme** cofactor for their catalytic chemistry. The K00380 assignment thus reflects only recognition of the C-terminal CysJ/CPR-like diflavin *electron-input* module and ignores the N-terminal molybdopterin catalytic domain that actually defines the enzyme's chemistry. The same reasoning refutes the ARBA "sulfite reductase (NADPH) EC 1.8.1.2" activity annotation carried in UniProt (see F003): the protein lacks the siroheme/[4Fe-4S]-siroheme sulfite-reductase catalytic domain, so it cannot be a genuine sulfite reductase.

---

## Mechanistic Model / Interpretation

The findings converge on a single, internally consistent model: **Q88M71 / PP_1703 is a monomeric, cytoplasmic, NAD(P)H-dependent assimilatory nitrate reductase** that carries out the entire electron path from pyridine nucleotide to nitrate within one polypeptide.

**Intramolecular electron-transfer relay:**

```
                 C-terminal diflavin diaphorase        N-terminal Mo catalytic module
                 (CysJ/CPR-like, ~residues 800-1341)   (~residues 3-800)
   NAD(P)H  -->  FAD  -->  FMN  ------------------->   [4Fe-4S]  -->  Mo-bis(MGD)  -->  NO3-
   (electron     (FAD-      (Flavodoxin-               (Molybdop_    (Molybdopterin      |
    donor)        binding    like/FMN                   Fe4S4         catalytic)          v
                  FR-type)   domain)                    domain)                         NO2- + H2O
```

Electrons enter from NAD(P)H at the C-terminal diaphorase, pass through FAD then FMN (the "diflavin" pair), cross into the N-terminal catalytic half, reduce the [4Fe-4S] cluster, and finally reach the molybdenum center where nitrate is reduced to nitrite. Because both the electron-input flavin module and the catalytic Mo module are on the same chain, the enzyme needs no separate ferredoxin, flavodoxin, or cytochrome partner — this is the defining feature of the "recently evolved diflavin-containing monomeric nitrate reductase" that supports highly efficient nitrate assimilation ([PMID: 32111737](https://pubmed.ncbi.nlm.nih.gov/32111737/)).

**Pathway context (nitrate assimilation → nitrogen into biomass):**

```
   NO3- (taken up)
      |  PP_1703  (nas nitrate reductase; this protein)  -- induced under N limitation
      v
   NO2-
      |  PP_1705/PP_1706  nirBD  (NAD(P)H nitrite reductase; adjacent genes)
      v
   NH4+
      |  glutamine synthetase (GS) / glutamate synthase (GOGAT, gltB)
      v
   glutamate / glutamine  -->  amino acids, nucleotides, biomass
```

The pathway is switched on when the preferred nitrogen source, ammonium, runs low, and it is genetically wired to the GS/GOGAT assimilation cycle through *gltB* ([PMID: 10852866](https://pubmed.ncbi.nlm.nih.gov/10852866/)). This is an **assimilatory** (anabolic, nitrogen-acquiring) system that operates in the cytoplasm, and is mechanistically and physiologically distinct from **respiratory** nitrate reduction (periplasmic Nap or membrane Nar), which serves energy conservation. The two database misannotations — periplasmic NapAB and sulfite reductase CysJ — are both artifacts of partial domain matching and are refuted by the complete domain architecture and by the genomic neighbourhood.

**Localization summary**

| Property | Assignment | Basis |
|---|---|---|
| Subcellular location | Cytoplasm (soluble) | No signal/Tat peptide; fused NAD(P)H diaphorase; soluble homolog in *Acinetobacter* |
| Oligomeric state | Monomer | Single-chain fusion of catalytic + diaphorase modules |
| Physiological electron donor | NAD(P)H | Diflavin diaphorase; comparative biochemistry |
| Metal/cofactor set | Mo-bis(MGD), [4Fe-4S], FAD, FMN | UniProt cofactor annotation; Pfam domain map |

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports/challenges the findings |
|---|---|---|
| [10852866](https://pubmed.ncbi.nlm.nih.gov/10852866/) | *Inactivation of gltB abolishes expression of the assimilatory nitrate reductase gene (nasB) in P. putida KT2442* | **Primary genetic evidence.** Names the assimilatory nitrate reductase gene (*nasB*) in the KT2440 lineage; shows induction under ammonium deficiency; links expression/function to GOGAT (*gltB*). Supports F001, F004. |
| [32111737](https://pubmed.ncbi.nlm.nih.gov/32111737/) | *A recently evolved diflavin-containing monomeric nitrate reductase is responsible for highly efficient bacterial nitrate assimilation* | Establishes that diflavin-containing monomeric nitrate reductases perform the rate-limiting nitrate→nitrite step in assimilation — matches Q88M71's fused Mo + FAD/FMN architecture. Supports F002. |
| [849099](https://pubmed.ncbi.nlm.nih.gov/849099/) | *Assimilatory nitrate reductase from Acinetobacter calcoaceticus* | Comparative biochemistry: a **soluble** enzyme reduces nitrate → nitrite using NAD(P)H via diaphorases and is repressed by ammonia. Supports reaction chemistry, cytoplasmic localization, and ammonium repression (F001, F003, F004). |
| [2141097](https://pubmed.ncbi.nlm.nih.gov/2141097/) | *Molybdenum cofactor requirement for in vitro activation of apo-molybdoenzymes of E. coli* | Background support that the molybdenum cofactor (molybdopterin) is required for nitrate reductase activity, consistent with Q88M71's Mo-bis(MGD) dependence. |

The evidence is strongest for the **reaction and pathway assignment** — multiple independent lines converge: direct genetics in the same species lineage, comparative biochemistry in a related organism, domain architecture, and genomic context. The **cytoplasmic localization** and **monomeric diflavin mechanism** are supported by bioinformatic/structural inference (domain map, absence of an export signal) plus homology to characterized soluble assimilatory enzymes, rather than by direct experiments on Q88M71 itself.

---

## Limitations and Knowledge Gaps

- **No direct biochemical characterization of Q88M71 itself.** The reaction, kinetics, substrate specificity, and cofactor content are inferred from UniProt annotation, domain architecture, and homologs (*Acinetobacter*, other diflavin nitrate reductases). No purified-protein assay of PP_1703 was located.
- **NADH vs NADPH preference is unresolved.** The diaphorase module can, in principle, use either; the CysJ/CPR homology and the UniProt "NADP" keyword suggest NADPH, but the physiological pyridine-nucleotide specificity of PP_1703 has not been measured directly.
- **Localization is inferred, not demonstrated.** The cytoplasmic assignment rests on the absence of an export signal and homology; no fractionation or fluorescent-fusion experiment for PP_1703 was found.
- **EC 1.7.99.4 is a legacy/generic number** (nitrate reductase with an unspecified acceptor) and does not itself specify NAD(P)H as donor; the donor assignment comes from the diflavin architecture and homolog biochemistry.
- **Database misannotations persist.** Both UniProt (periplasmic NapAB; sulfite reductase EC 1.8.1.2) and KEGG (CysJ, K00380, sulfur metabolism) carry incorrect labels; downstream automated pipelines may propagate these errors.
- **Regulatory detail is incomplete.** While nitrogen-limitation induction and a *gltB* link are established, the specific transcription factors (e.g., NasS/NasT- or Ntr-type regulators) controlling PP_1703 in KT2440 were not resolved here.

---

## Proposed Follow-up Experiments / Actions

1. **Direct enzymology.** Heterologously express and purify Q88M71; assay nitrate → nitrite activity with NADH and NADPH to determine kₐₜ/Kₘ and pyridine-nucleotide preference; confirm the cofactor complement (Mo-bis(MGD), [4Fe-4S], FAD, FMN) by metal/flavin analysis and EPR.
2. **Localization test.** Cell fractionation and/or a C-terminal fluorescent fusion in KT2440 to experimentally confirm cytoplasmic (soluble) localization and rule out periplasmic export.
3. **Genetic phenotyping in KT2440.** Construct a clean PP_1703 deletion and test growth on nitrate as sole nitrogen source (expected: loss of nitrate assimilation, rescued by ammonium); confirm epistasis with *nirBD* (PP_1705/6) and *gltB*.
4. **Regulation.** Map the promoter and identify the transcriptional regulators; test induction under nitrogen limitation and repression by ammonium at the transcript level (qRT-PCR/RNA-seq).
5. **Database correction.** Submit annotation corrections to UniProt (remove periplasmic NapAB and sulfite-reductase EC 1.8.1.2) and to KEGG (reassign from K00380 sulfur metabolism to an assimilatory nitrate reductase KO / nitrogen metabolism), citing the full domain architecture and *nirBD* genomic context.
6. **Structural confirmation.** Obtain an experimental or AlphaFold structure and verify the intramolecular electron-transfer chain (NAD(P)H → FAD → FMN → [4Fe-4S] → Mo) by cofactor geometry and inter-center distances.

---

## References

- Eberl L. et al. (2000) *Inactivation of gltB abolishes expression of the assimilatory nitrate reductase gene (nasB) in Pseudomonas putida KT2442.* [PMID: 10852866](https://pubmed.ncbi.nlm.nih.gov/10852866/)
- Tan Z. et al. (2020) *A recently evolved diflavin-containing monomeric nitrate reductase is responsible for highly efficient bacterial nitrate assimilation.* [PMID: 32111737](https://pubmed.ncbi.nlm.nih.gov/32111737/)
- Villalobo A. et al. (1977) *Assimilatory nitrate reductase from Acinetobacter calcoaceticus.* [PMID: 849099](https://pubmed.ncbi.nlm.nih.gov/849099/)
- Amy N.K. (1990) *Molybdenum cofactor requirement for in vitro activation of apo-molybdoenzymes of Escherichia coli.* [PMID: 2141097](https://pubmed.ncbi.nlm.nih.gov/2141097/)
- UniProt Q88M71; InterPro/Pfam/KEGG annotations.

---

*Report generated from a 3-iteration autonomous investigation; 6 findings confirmed, 4 papers reviewed.*


## Artifacts

- [OpenScientist final report](PP_1703-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PP_1703-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:10852866
2. PMID:32111737
3. PMID:2141097