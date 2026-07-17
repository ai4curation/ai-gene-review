---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-17T04:57:50.767060'
end_time: '2026-07-17T05:24:49.335692'
duration_seconds: 1618.57
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: hisI
  gene_symbol: hisI
  uniprot_accession: Q88D15
  protein_description: 'RecName: Full=Phosphoribosyl-AMP cyclohydrolase {ECO:0000255|HAMAP-Rule:MF_01021};
    Short=PRA-CH {ECO:0000255|HAMAP-Rule:MF_01021}; EC=3.5.4.19 {ECO:0000255|HAMAP-Rule:MF_01021};'
  gene_info: Name=hisI {ECO:0000255|HAMAP-Rule:MF_01021}; OrderedLocusNames=PP_5014;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the PRA-CH family. {ECO:0000255|HAMAP-
  protein_domains: PRA-CH. (IPR026660); PRib_AMP_CycHydrolase_dom. (IPR002496); PRib_AMP_CycHydrolase_sf.
    (IPR038019); PRA-CH (PF01502)
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
citation_count: 6
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: hisI-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: hisI-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88D15
- **Protein Description:** RecName: Full=Phosphoribosyl-AMP cyclohydrolase {ECO:0000255|HAMAP-Rule:MF_01021}; Short=PRA-CH {ECO:0000255|HAMAP-Rule:MF_01021}; EC=3.5.4.19 {ECO:0000255|HAMAP-Rule:MF_01021};
- **Gene Information:** Name=hisI {ECO:0000255|HAMAP-Rule:MF_01021}; OrderedLocusNames=PP_5014;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the PRA-CH family. {ECO:0000255|HAMAP-
- **Key Domains:** PRA-CH. (IPR026660); PRib_AMP_CycHydrolase_dom. (IPR002496); PRib_AMP_CycHydrolase_sf. (IPR038019); PRA-CH (PF01502)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "hisI" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'hisI' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **hisI** (gene ID: hisI, UniProt: Q88D15) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *hisI* (PP_5014, Q88D15) — Phosphoribosyl-AMP Cyclohydrolase from *Pseudomonas putida* KT2440

## Summary

**The gene *hisI* (locus PP_5014; UniProt Q88D15) of *Pseudomonas putida* KT2440 encodes phosphoribosyl-AMP cyclohydrolase (PRA-CH; EC 3.5.4.19), the enzyme that catalyzes the third step of the *de novo* L-histidine biosynthetic pathway.** Its identity is unambiguous: the UniProt/HAMAP annotation (rule MF_01021), the InterPro/Pfam domain architecture (PRA-CH family, PF01502), and the primary and structural literature on orthologous PRA-CH enzymes all converge on the same function. The gene symbol *hisI* is used consistently across bacteria for this cyclohydrolase activity, and no conflicting gene-identity issues were encountered during the investigation.

The enzyme performs a chemically distinctive reaction: the **hydrolytic opening of the adenine (purine) ring** of the intermediate N1-(5′-phospho-β-D-ribosyl)-AMP (PR-AMP) by cleaving the **N1–C6 bond**, producing the ring-opened formimino compound **ProFAR** (N-(5′-phospho-D-ribosylformimino)-5-amino-1-(5″-phospho-D-ribosyl)-4-imidazolecarboxamide), which is then handed to the downstream isomerase HisA. This ring-opening chemistry is unique to histidine biosynthesis and represents the committed conversion of a purine-derived precursor into the histidine-specific portion of the pathway. HisI is a **Zn²⁺/Mg²⁺-dependent metalloenzyme**: it carries one essential, tightly bound catalytic Zn²⁺ (coordinated by three cysteines, Cys78/Cys95/Cys102 in the *P. putida* sequence) plus a lower-affinity Mg²⁺ requirement, and it functions as an **obligate cytoplasmic homodimer** with a shared, inter-subunit active site.

A notable organism-specific feature is that in *P. putida* KT2440, *hisI* is a **standalone monofunctional gene** (PP_5014, 130 aa) sitting adjacent to a separate monofunctional *hisE* gene (PP_5015, phosphoribosyl-ATP pyrophosphohydrolase, EC 3.6.1.31). This contrasts with the enteric bacteria (*E. coli*, *Salmonella*) and plants, where the two activities are fused into a single bifunctional HisIE/HISN2 polypeptide. This organization reflects the "piecewise" evolutionary assembly of the proteobacterial histidine operon into scattered mini-operons. Below, each of these conclusions is developed with its supporting evidence, followed by a mechanistic model, an evaluation of the evidence base, limitations, and proposed follow-up work.

---

## Key Findings

### Finding 1 — HisI catalyzes step 3 of histidine biosynthesis: hydrolytic opening of the purine ring of PR-AMP

The core function of PP_5014 is defined by its EC number and pathway annotation. UniProt Q88D15 assigns **EC 3.5.4.19** and the reaction:

> 1-(5-phospho-β-D-ribosyl)-5′-AMP + H₂O → 1-(5-phospho-β-D-ribosyl)-5-[(5-phospho-β-D-ribosylamino)methylideneamino]imidazole-4-carboxamide (ProFAR)

This is annotated as **step 3 of 9** in L-histidine biosynthesis. The protein is small (130 aa, ~15 kDa) and belongs to the PRA-CH family (Pfam PF01502). Mechanistically, the enzyme opens the adenine (purine) ring by hydrolyzing the **N1–C6 bond**, a transformation that occurs nowhere else in metabolism, marking this as the histidine-committed step.

The primary literature directly corroborates this assignment. A structural study of the orthologous archaeal enzyme states plainly that "**Hydrolysis of phosphoribosyl-AMP, the third step in the histidine biosynthetic pathway, is carried out by PR-AMP cyclohydrolase, the product of the *hisI* gene**" ([PMID: 16042384](https://pubmed.ncbi.nlm.nih.gov/16042384/)). The biochemical characterization of the monofunctional enzyme specifies the exact chemistry, describing the enzyme as "**catalyzing the hydrolysis of the N1-C6 bond of the purine substrate, a reaction unique to this pathway**" ([PMID: 9931020](https://pubmed.ncbi.nlm.nih.gov/9931020/)). Taken together, these establish HisI as the PRA-CH of *P. putida*, catalyzing the ring-opening hydrolysis that defines the third step of histidine biosynthesis.

### Finding 2 — HisI is a Zn²⁺/Mg²⁺-dependent metalloenzyme with three cysteine zinc ligands

HisI requires two metal cofactors. The UniProt/HAMAP annotation (MF_01021) for Q88D15 lists both **Zn²⁺** and **Mg²⁺**. The *P. putida* sequence contains exactly three cysteines — **Cys78, Cys95, Cys102** — which serve as the annotated Zn²⁺ ligands, while the Mg²⁺ site is built from aspartate side chains (**Asp77, Asp79, Asp81**).

The functional roles of these metals are established biochemically. In the monofunctional PRA-CH, "**Bound to the enzyme is 1 equiv of Zn²⁺ that can be removed only by extended dialysis with 1,10-phenanthroline (Kd ≤ 10⁻⁹ M). Removal of the Zn²⁺ correlates with the loss of enzyme activity**" — demonstrating that the tightly bound Zn²⁺ is catalytically essential ([PMID: 9931020](https://pubmed.ncbi.nlm.nih.gov/9931020/)). The same study shows that, in addition, "**free Mg²⁺ (Ks = 4.9 ± 0.7 µM) is required for catalytic activity**," matching the dual-cofactor UniProt annotation ([PMID: 9931020](https://pubmed.ncbi.nlm.nih.gov/9931020/)).

The structural basis of the zinc site is resolved in the 1.7 Å crystal structure of the *Methanobacterium thermoautotrophicum* enzyme, in which "**These metal binding sites include three cysteine ligands, two from one monomer and the third from the second monomer**" ([PMID: 16042384](https://pubmed.ncbi.nlm.nih.gov/16042384/)). This three-cysteine coordination — spanning the dimer interface — is consistent with the three cysteines (Cys78/Cys95/Cys102) present in *P. putida* HisI. The Zn²⁺ almost certainly serves to activate a water molecule (or polarize the substrate) for the hydrolytic ring-opening attack, while Mg²⁺ likely stabilizes the anionic phosphoribosyl groups of the substrate.

### Finding 3 — HisI is an obligate cytoplasmic homodimer with a shared inter-subunit active site

The enzyme's quaternary structure and localization are well defined. UniProt Q88D15 (via HAMAP MF_01021) annotates the **subunit as a homodimer** and the **subcellular location as cytoplasm**. Because histidine biosynthesis is a soluble metabolic pathway using phosphorylated, highly polar intermediates, cytoplasmic localization is expected and consistent with the enzyme carrying no signal peptide or transmembrane segments.

Structural analysis shows the dimerization is not incidental but functionally required. In the *M. thermoautotrophicum* structure, "**The putative substrate-binding cleft is formed at the interface between the two monomers of the dimer. This fact, combined with the localization of the Zn²⁺-binding site, indicates that the enzyme is an obligate dimer**" ([PMID: 16042384](https://pubmed.ncbi.nlm.nih.gov/16042384/)). Because one of the three zinc ligands is contributed by the partner subunit (Finding 2), the active site literally cannot be assembled by a monomer. HisI therefore carries out its function as a **soluble cytoplasmic homodimer**, with each of the two composite active sites built from residues of both protomers.

### Finding 4 — In *P. putida*, *hisI* (PRA-CH) and *hisE* (PRA-PH) are separate monofunctional genes, not a fused bifunctional enzyme

A genome-level distinction of *P. putida* is that the two consecutive activities of the pathway — phosphoribosyl-ATP pyrophosphohydrolase (PRA-PH; step 2) and phosphoribosyl-AMP cyclohydrolase (PRA-CH; step 3) — are encoded by **two separate genes**. *hisI* = PP_5014 (Q88D15, 130 aa, EC 3.5.4.19, PRA-CH only) lies immediately adjacent to *hisE* = PP_5015 (Q88D14, 111 aa, EC 3.6.1.31, PRA-PH), forming a *hisIE* gene pair of two standalone polypeptides.

This organization differs from the enteric bacteria and plants, where PRA-PH and PRA-CH are fused into a single bifunctional polypeptide. The Arabidopsis study that mapped the two domains notes that "**the functional domains for the PRA-CH (hisI) and PRA-PH (hisE) resided in the N-terminal and the C-terminal halves**" of the fused enzyme ([PMID: 9733547](https://pubmed.ncbi.nlm.nih.gov/9733547/)) — a fusion that in *P. putida* corresponds instead to two distinct genes. Evolutionary analyses explain this pattern: across proteobacteria the histidine genes were assembled "piecewise" from scattered monofunctional units into mini-operons, and in *P. putida* KT2440 the his genes remain in three separate genomic clusters — *hisGDC*, the *hisBHAF* core, and *hisIE* — "**three mini-operons (hisGDC, hisBHAF, hisIE) transcribed from independent promoters**" ([PMID: 15871048](https://pubmed.ncbi.nlm.nih.gov/15871048/)). That *hisI* can encode a purely unifunctional PRA-CH is directly precedented in *Rhodobacter sphaeroides*, where "**the R. sphaeroides hisI gene encodes a unifunctional protein**" ([PMID: 8760919](https://pubmed.ncbi.nlm.nih.gov/8760919/)). *P. putida* HisI therefore represents the standalone, monofunctional cyclohydrolase form of this enzyme.

### Finding 5 — Catalytic mechanism: adenine ring-opening followed by rate-limiting proton transfer, yielding ProFAR

The chemical mechanism has been probed by pre-steady-state kinetics of the bifunctional HisIE enzyme, whose HisI-like cyclohydrolase domain is homologous to *P. putida* HisI. In the pathway, the upstream **HisE/PRA-PH** converts PR-ATP to PR-AMP, and **HisI/PRA-CH** then hydrolyzes PR-AMP to **ProFAR**, which the downstream **HisA** isomerizes. Kinetic dissection revealed a lag followed by a burst in ProFAR formation, a large solvent deuterium kinetic isotope effect that decreases at basic pH, and no solvent viscosity effect — a pattern that pinpoints a slow chemical step: "**These observations are consistent with a rate-limiting unimolecular step involving a proton transfer following adenine ring opening**" ([PMID: 37288093](https://pubmed.ncbi.nlm.nih.gov/37288093/)). The same study identifies the product and the responsible domain: "**cyclohydrolysis of PRAMP to N-(5′-phospho-D-ribosylformimino)-5-amino-1-(5″-phospho-D-ribosyl)-4-imidazolecarboxamide (ProFAR) in the N-terminal HisI-like domain**" ([PMID: 37288093](https://pubmed.ncbi.nlm.nih.gov/37288093/)).

This mechanistic picture is complemented by the pH dependence of the monofunctional enzyme, which "**shows a single titration event in the kcat/Km profile with a pKa of 7.3 that is consistent with the functional role of a metal site in catalysis**" ([PMID: 9931020](https://pubmed.ncbi.nlm.nih.gov/9931020/)). Together these data support a mechanism in which the active-site metal (Zn²⁺) activates water/hydroxide to attack the N1–C6 bond and open the purine ring, after which a rate-limiting unimolecular proton-transfer step completes formation of the ring-opened ProFAR product.

### Finding 6 — HisI adopts the conserved HisI-like α/β fold diagnostic of the PRA-CH family

Domain and fold annotations independently corroborate the functional assignment. InterPro annotation of Q88D15 includes family **IPR026660** (Phosphoribosyl-AMP cyclohydrolase), domain **IPR002496**, and superfamily **IPR038019**; Pfam **PF01502**; HAMAP **MF_01021** (hisI); NCBIfam **NF000768**; PANTHER **PTHR42945** (Histidine biosynthesis PRA-CH/PRA-PH); CATH-Gene3D **G3DSA:3.10.20.810**; and SCOP/SUPERFAMILY **SSF141734** ("HisI-like"). This set of orthogonal classifications reinforces the UniProt PRA-CH call, and the fold matches the experimentally determined *M. thermoautotrophicum* HisI structure (PDB, 1.7 Å; [PMID: 16042384](https://pubmed.ncbi.nlm.nih.gov/16042384/)). The consistency of family, domain, superfamily, and fold assignments provides high confidence that Q88D15 is a *bona fide* member of the PRA-CH family and shares the catalytic architecture characterized in the structural studies.

### Finding 7 — HisI is required for *de novo* histidine biosynthesis and links the pathway to purine/nucleotide metabolism

The biological necessity of the PRA-CH step is established genetically by complementation. Bacterial *hisI* mutants are histidine auxotrophs that can be rescued by heterologous PRA-CH genes or domains. The Arabidopsis study reports that "**By complementing a hisI mutation of Escherichia coli with an Arabidopsis cDNA library, we isolated an Arabidopsis cDNA (At-IE)**" ([PMID: 9733547](https://pubmed.ncbi.nlm.nih.gov/9733547/)), demonstrating that the PRA-CH activity is essential for histidine prototrophy and is functionally interchangeable across large evolutionary distances.

Histidine biosynthesis is also metabolically interwoven with nucleotide metabolism. The pathway consumes PRPP and ATP to build the imidazole ring, and downstream the HisHF (imidazole-glycerol-phosphate synthase) step releases AICAR (5-aminoimidazole-4-carboxamide ribotide), an intermediate that re-enters *de novo* purine biosynthesis. Evolutionary analyses note this interconnection, describing "**the his 'core,' a cluster consisting of four genes (hisBHAF) whose products interconnect histidine biosynthesis to both de novo synthesis of purine metabolism**" ([PMID: 15871048](https://pubmed.ncbi.nlm.nih.gov/15871048/)). HisI sits at the entry to this histidine-committed branch, converting a purine-derived (AMP-containing) precursor into the first histidine-specific intermediate.

### Finding 8 — The catalytic Zn-binding cysteine cluster is conserved between *P. putida* HisI and the *E. coli* HisIE cyclohydrolase domain

Sequence comparison confirms that the zinc-ligating cysteine set is conserved across the monofunctional and bifunctional forms. *P. putida* HisI (Q88D15, 130 aa) carries exactly three cysteines at positions **78, 95, 102**, embedded in the conserved PRA-CH motif `...GHIACHTGRESC...` (residues ~91–102). The N-terminal HisI (cyclohydrolase) domain of the *E. coli* bifunctional HisIE (P06987, 355 aa) carries a matching N-terminal cysteine cluster at positions **93, 101, 103**, whereas its remaining cysteines (254, 265, 269) belong to the separate C-terminal HisE/PRA-PH domain. Thus the three-cysteine Zn²⁺ ligand set is conserved between the *P. putida* monofunctional enzyme and the *E. coli* bifunctional enzyme, and matches the structurally defined zinc site of the *M. thermoautotrophicum* HisI, where "**These metal binding sites include three cysteine ligands, two from one monomer and the third from the second monomer**" ([PMID: 16042384](https://pubmed.ncbi.nlm.nih.gov/16042384/)). This conservation strongly implies that *P. putida* HisI uses the same zinc-dependent catalytic machinery.

---

## Mechanistic Model / Interpretation

### Position in the histidine biosynthetic pathway

HisI operates at the third of nine steps in the *de novo* L-histidine biosynthetic pathway. The immediate upstream and downstream context is:

```
 Step 1: HisG (ATP-PRT)      PRPP + ATP ──────────────► PR-ATP
 Step 2: HisE (PRA-PH)       PR-ATP + H2O ────────────► PR-AMP + PPi
 Step 3: HisI (PRA-CH)  ***  PR-AMP + H2O ────────────► ProFAR      <-- THIS ENZYME
 Step 4: HisA (isomerase)    ProFAR ───────────────────► PRFAR
 Step 5: HisHF (IGPS)        PRFAR + glutamine ────────► ImGP + AICAR (+ Glu)
   ...   HisB, HisC, HisD    ──────────────────────────► L-histidine
```

HisI catalyzes the committed ring-opening that converts the AMP-derived, purine-ring-containing intermediate PR-AMP into the open-chain formimino compound **ProFAR**. The imidazole ring of PR-AMP is preserved and ultimately becomes the imidazole side chain of histidine, while the pyrimidine portion of the former adenine ring, once opened at N1–C6, is later cleaved off as AICAR at the HisHF step and recycled into purine biosynthesis. HisI thus marks the metabolic branch point where a purine-nucleotide precursor is committed to histidine.

### Catalytic architecture and chemistry

```
        Subunit A                         Subunit B
     ┌───────────────┐                ┌───────────────┐
     │ Cys78  Cys95  │   Zn2+ site    │               │
     │ Cys102 ───────┼──── Zn2+ ──────┼─── (3rd Cys   │
     │               │   (shared)     │    from        │
     │ Asp77/79/81 ──┼──── Mg2+       │    partner)    │
     └───────┬───────┘                └───────┬───────┘
             │      shared active-site cleft  │
             └──────── at dimer interface ────┘

   Chemistry:  Zn2+-activated water/OH- attacks N1-C6 bond
               → adenine (purine) ring opens
               → rate-limiting unimolecular proton transfer
               → ProFAR released
```

The enzyme is an **obligate homodimer**: each active site is assembled at the interface, drawing zinc ligands from both subunits. The catalytically essential Zn²⁺ (Kd ≤ 10⁻⁹ M) is best interpreted as a Lewis acid that activates a water molecule for nucleophilic attack on the N1–C6 bond, consistent with the single kcat/Km titration (pKa 7.3) attributed to a metal-water site. Kinetics of the homologous HisIE enzyme indicate that ring opening is followed by a **rate-limiting unimolecular proton-transfer step**; the large solvent deuterium isotope effect that diminishes at basic pH is the diagnostic signature of this proton transfer. A lower-affinity Mg²⁺ (Ks ≈ 4.9 µM), coordinated by the Asp77/Asp79/Asp81 cluster, likely stabilizes the two anionic 5′-phosphoribosyl moieties of the substrate/product.

### Genomic and evolutionary organization

| Feature | *P. putida* KT2440 | *E. coli* / *Salmonella* | Plants (Arabidopsis, *Medicago*) |
|---|---|---|---|
| PRA-CH (step 3) | *hisI* = PP_5014 (standalone, 130 aa) | N-terminal domain of HisIE | PRA-CH domain of bifunctional HISN2 |
| PRA-PH (step 2) | *hisE* = PP_5015 (standalone, 111 aa) | C-terminal domain of HisIE | PRA-PH domain of HISN2 |
| Architecture | Two separate monofunctional genes (*hisIE* pair) | Single fused bifunctional gene | Single fused bifunctional gene |
| Genomic layout | Three mini-operons: *hisGDC*, *hisBHAF*, *hisIE* | Single compact *his* operon | Nuclear genes |

This comparison highlights that the *P. putida* enzyme is one polypeptide with one job — a "clean" model system for studying PRA-CH catalysis without the confounding presence of a fused PRA-PH domain. The scattered, three-cluster genomic layout in *P. putida* reflects the "piecewise" assembly model of the proteobacterial histidine operon, in which small units (some with their own promoters) were accreted over evolutionary time rather than assembled at once.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [16042384](https://pubmed.ncbi.nlm.nih.gov/16042384/) | *Crystal structure of M. thermoautotrophicum PRA-CH HisI* | **Primary structural evidence.** Defines HisI as PR-AMP cyclohydrolase (step 3); establishes the three-cysteine Zn site spanning the dimer interface; shows the inter-subunit active-site cleft and obligate dimer. Underpins Findings 1, 2, 3, 6, 8. |
| [9931020](https://pubmed.ncbi.nlm.nih.gov/9931020/) | *N1-(5′-phosphoribosyl)AMP cyclohydrolase: a unique metalloenzyme* | **Primary biochemical evidence.** Demonstrates essential tightly-bound Zn²⁺ (Kd ≤ 10⁻⁹ M), separate Mg²⁺ requirement (Ks 4.9 µM), N1–C6 bond cleavage unique to the pathway, and pKa 7.3 metal-water titration. Underpins Findings 1, 2, 5. |
| [37288093](https://pubmed.ncbi.nlm.nih.gov/37288093/) | *Catalytic cycle of bifunctional PRA-PH/PRA-CH* | **Primary kinetic/mechanistic evidence.** Pre-steady-state kinetics reveal ring opening followed by rate-limiting proton transfer, and identify ProFAR as the product of the HisI-like domain. Underpins Finding 5. (Study is of the bifunctional enzyme's HisI-like domain, homologous to *P. putida* HisI — an inference across orthologs.) |
| [9733547](https://pubmed.ncbi.nlm.nih.gov/9733547/) | *Arabidopsis bifunctional PRA-PH/PRA-CH (At-IE)* | Defines the *hisI* (PRA-CH) and *hisE* (PRA-PH) functional domains; provides complementation evidence that PRA-CH is essential for His prototrophy. Underpins Findings 4, 7. |
| [15871048](https://pubmed.ncbi.nlm.nih.gov/15871048/) | *Piecewise building of the proteobacterial histidine operon* | Documents the *hisIE* mini-operon and three-cluster his-gene organization; links histidine to purine metabolism via the *hisBHAF* core. Underpins Findings 4, 7. |
| [8760919](https://pubmed.ncbi.nlm.nih.gov/8760919/) | *R. sphaeroides hisL/hisI unifunctionality* | Precedent that a bacterial *hisI* can encode a purely unifunctional PRA-CH, as in *P. putida*. Underpins Finding 4. |
| [33958623](https://pubmed.ncbi.nlm.nih.gov/33958623/) | *Structural/mechanistic insights into plant HISN2* | Corroborating structural context: crystal structures of the bifunctional plant PRA-CH/PRA-PH with AMP bound to each domain; PRA-CH domain analogous to bacterial *hisI*. Supports the domain-homology framework (Findings 4, 5). |
| [19888544](https://pubmed.ncbi.nlm.nih.gov/19888544/) | *Evolution of his genes in archaea / LUCA* | Context: in most Archaea his genes are monofunctional and scattered, consistent with the standalone monofunctional *hisI* seen in *P. putida*. Supports Finding 4. |

Additional *P. putida*-focused papers reviewed (e.g., on CbrA/B carbon/nitrogen regulation, Crc catabolite control, and c-di-GMP/biofilm signaling — PMIDs 25031426, 20553554, 19526543, 27489550, 35001503) confirmed that histidine metabolism in *P. putida* is embedded in the organism's broader carbon/nitrogen regulatory networks (histidine is a usable carbon/nitrogen source), but none of them implicate the biosynthetic PRA-CH (HisI) in any moonlighting or signaling role. This absence is itself informative: it supports the conclusion that HisI's function is confined to biosynthetic catalysis.

---

## Limitations and Knowledge Gaps

1. **No direct experimental characterization of the *P. putida* protein.** All catalytic, metal-binding, and structural conclusions rest on **orthologous** enzymes — the *M. thermoautotrophicum* crystal structure, the monofunctional archaeal metalloenzyme biochemistry, and the bifunctional HisIE/HISN2 kinetics. The functional transfer to Q88D15 is a well-supported inference (family membership, domain conservation, and the conserved Cys78/Cys95/Cys102 zinc cluster all align), but no purified *P. putida* HisI has been kinetically or structurally characterized in the literature reviewed.

2. **Residue numbering for metal ligands is inferred.** The Zn (Cys78/95/102) and Mg (Asp77/79/81) positions are derived from the *P. putida* sequence and the conserved PRA-CH motif, consistent with the structural ortholog, but have not been experimentally mutated/verified in Q88D15 itself.

3. **Mechanistic detail is extrapolated from the bifunctional enzyme.** The "ring-opening then rate-limiting proton transfer" mechanism ([PMID: 37288093](https://pubmed.ncbi.nlm.nih.gov/37288093/)) was established on a bifunctional HisIE. While the HisI-like domain is homologous, subtle kinetic differences between fused and standalone enzymes cannot be excluded.

4. **Regulation and expression in *P. putida* are not fully resolved.** The *hisIE* mini-operon is transcribed from an independent promoter, but the specific regulatory inputs (e.g., histidine-mediated feedback, growth-condition dependence) on PP_5014 expression were not directly established here.

5. **No structure of the *P. putida* enzyme (experimental or predicted) was analyzed.** An AlphaFold model of Q88D15 exists in principle but was not evaluated; doing so could confirm the dimer interface and metal-site geometry computationally.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant expression and enzyme assay.** Clone PP_5014, express and purify the His-tagged protein, and measure PRA-CH activity (PR-AMP → ProFAR) spectrophotometrically. Determine kcat, Km for PR-AMP, and the pH-rate profile to confirm the predicted pKa ≈ 7.3 metal-water titration.

2. **Metal-dependence and stoichiometry.** Quantify bound Zn²⁺ (ICP-MS / atomic absorption) and test activity loss upon chelation (1,10-phenanthroline), replicating the ≤10⁻⁹ M Zn²⁺ affinity result for the *P. putida* ortholog. Titrate Mg²⁺ to verify the low-affinity requirement.

3. **Site-directed mutagenesis of the predicted ligands.** Mutate Cys78, Cys95, Cys102 (Zn) and Asp77/79/81 (Mg) individually to confirm their roles in catalysis and metal binding, directly testing the inferred residue assignments.

4. **Quaternary-structure confirmation.** Use size-exclusion chromatography with multi-angle light scattering (SEC-MALS) or analytical ultracentrifugation to verify the obligate homodimer, and, if feasible, solve the crystal or cryo-EM structure of *P. putida* HisI to confirm the inter-subunit active site.

5. **Genetic essentiality/complementation.** Construct a PP_5014 deletion in *P. putida* KT2440 and confirm histidine auxotrophy (growth rescued by histidine supplementation), and complement an *E. coli hisI* mutant with PP_5014 to demonstrate functional PRA-CH activity *in vivo*.

6. **Computational validation.** Analyze the AlphaFold model of Q88D15 (pLDDT, dimer prediction via AlphaFold-Multimer) to corroborate the metal-site geometry and dimer interface, and dock PR-AMP to test the proposed catalytic arrangement.

7. **Expression/regulation profiling.** Use RT-qPCR or RNA-seq under histidine-replete vs. limited conditions to characterize regulation of the *hisIE* mini-operon in *P. putida*.

---

## Conclusion

The evidence — spanning UniProt/HAMAP annotation, InterPro/Pfam/CATH/SCOP domain and fold classification, a high-resolution crystal structure of an archaeal ortholog, detailed metalloenzyme biochemistry, pre-steady-state mechanistic kinetics of the homologous bifunctional enzyme, complementation genetics, and comparative genomics — converges on a single, high-confidence conclusion. **HisI (PP_5014, Q88D15) is a soluble cytoplasmic, Zn²⁺/Mg²⁺-dependent, obligate homodimeric phosphoribosyl-AMP cyclohydrolase (PRA-CH, EC 3.5.4.19) that catalyzes the third step of *de novo* L-histidine biosynthesis** — the hydrolytic opening of the adenine ring (N1–C6 bond cleavage) of PR-AMP to form ProFAR. In *P. putida* KT2440 it is a standalone monofunctional enzyme encoded separately from the adjacent *hisE* (PRA-PH), reflecting the piecewise evolutionary assembly of the proteobacterial histidine genes. Its function is squarely biochemical and biosynthetic; no signaling or moonlighting role is indicated.


## Artifacts

- [OpenScientist final report](hisI-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](hisI-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:16042384
2. PMID:9931020
3. PMID:9733547
4. PMID:15871048
5. PMID:8760919
6. PMID:37288093