---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-17T06:32:25.709171'
end_time: '2026-07-17T06:53:16.480060'
duration_seconds: 1250.77
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: bioC
  gene_symbol: bioC
  uniprot_accession: Q88QW9
  protein_description: 'RecName: Full=Malonyl-[acyl-carrier protein] O-methyltransferase
    {ECO:0000256|ARBA:ARBA00012327, ECO:0000256|HAMAP-Rule:MF_00835}; Short=Malonyl-ACP
    O-methyltransferase {ECO:0000256|HAMAP-Rule:MF_00835}; EC=2.1.1.197 {ECO:0000256|ARBA:ARBA00012327,
    ECO:0000256|HAMAP-Rule:MF_00835}; AltName: Full=Biotin synthesis protein BioC
    {ECO:0000256|HAMAP-Rule:MF_00835};'
  gene_info: Name=bioC {ECO:0000256|HAMAP-Rule:MF_00835, ECO:0000313|EMBL:AAN65996.1};
    OrderedLocusNames=PP_0365 {ECO:0000313|EMBL:AAN65996.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the methyltransferase superfamily.
  protein_domains: BioC. (IPR011814); Malonyl-ACP_OMT. (IPR050602); Methyltransf_11.
    (IPR013216); SAM-dependent_MTases_sf. (IPR029063); Methyltransf_11 (PF08241)
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
citation_count: 9
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: bioC-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: bioC-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88QW9
- **Protein Description:** RecName: Full=Malonyl-[acyl-carrier protein] O-methyltransferase {ECO:0000256|ARBA:ARBA00012327, ECO:0000256|HAMAP-Rule:MF_00835}; Short=Malonyl-ACP O-methyltransferase {ECO:0000256|HAMAP-Rule:MF_00835}; EC=2.1.1.197 {ECO:0000256|ARBA:ARBA00012327, ECO:0000256|HAMAP-Rule:MF_00835}; AltName: Full=Biotin synthesis protein BioC {ECO:0000256|HAMAP-Rule:MF_00835};
- **Gene Information:** Name=bioC {ECO:0000256|HAMAP-Rule:MF_00835, ECO:0000313|EMBL:AAN65996.1}; OrderedLocusNames=PP_0365 {ECO:0000313|EMBL:AAN65996.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the methyltransferase superfamily.
- **Key Domains:** BioC. (IPR011814); Malonyl-ACP_OMT. (IPR050602); Methyltransf_11. (IPR013216); SAM-dependent_MTases_sf. (IPR029063); Methyltransf_11 (PF08241)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "bioC" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'bioC' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **bioC** (gene ID: bioC, UniProt: Q88QW9) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# BioC (Q88QW9, PP_0365) in *Pseudomonas putida* KT2440 — Malonyl-[acyl-carrier-protein] O-Methyltransferase

**Gene:** bioC | **Ordered locus:** PP_0365 | **UniProt:** Q88QW9
**Protein:** Malonyl-[acyl-carrier protein] O-methyltransferase (Malonyl-ACP O-methyltransferase)
**EC:** 2.1.1.197 | **Length:** 272 aa | **Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / KT2440)

## Summary

**BioC** (UniProt **Q88QW9**; ordered locus **PP_0365**) of *Pseudomonas putida* KT2440 is a soluble, cytoplasmic, S-adenosyl-L-methionine (SAM)-dependent Class I methyltransferase that catalyzes the **committed initiating step of the biotin pimelate moiety**. Its curated catalytic activity (EC **2.1.1.197**, RHEA:17105) is: **malonyl-[ACP] + S-adenosyl-L-methionine → malonyl-[ACP] methyl ester + S-adenosyl-L-homocysteine**. By methyl-esterifying the free ω-carboxyl group of a malonyl-thioester, BioC "disguises" an atypical dicarboxylic substrate so that it is accepted by the type II fatty acid synthase (FAS II) machinery, which normally rejects such substrates. This single chemical modification repurposes a fatty-acid-like elongation pathway to build the seven-carbon α,ω-dicarboxylic pimelate backbone of biotin.

The functional assignment for the *P. putida* protein rests on strong orthology to the biochemically characterized *Escherichia coli* BioC. Pairwise global alignment of Q88QW9 against the *E. coli* enzyme (P12999) gives **49.4% sequence identity**, the SAM-binding glycine-rich Motif I (LDLGSGTG) is conserved at position 58, and the protein carries the Methyltransferase type 11 domain (PF08241) within the Class I Rossmann-fold SAM-dependent methyltransferase superfamily. Annotation is propagated by HAMAP rule MF_00835. Critically, *bioC* (PP_0365) sits within an **intact, syntenic biotin gene cluster** (PP_0362–PP_0366: *bioB, bioF, bioH, bioC, bioD*), immediately flanked by its physiological esterase partner *bioH* (PP_0364) and by *bioD* (PP_0366). This genomic context strongly supports the canonical BioC–BioH pimelate-synthesis route rather than one of the several non-orthologous bypasses found in other bacteria.

BioC performs its function in the **cytoplasm**. Sequence and hydropathy analysis of the 272-residue protein reveals no signal peptide, no transmembrane or intramembrane segment, and no lipidation site; the overall GRAVY value of −0.034 and the absence of any membrane-spanning hydrophobic window are consistent with a fully soluble enzyme that acts on the soluble acyl-carrier-protein-tethered substrate pool in the cytosol, in concert with the soluble FAS II enzymes and downstream biotin-synthesis proteins.

---

## Key Findings

### F001 — BioC is a SAM-dependent malonyl-ACP O-methyltransferase (EC 2.1.1.197)

BioC (Q88QW9, PP_0365) is a 272-amino-acid protein encoded by the *bioC*/PP_0365 gene of *P. putida* KT2440. Its curated catalytic activity, deposited as RHEA:17105, is the SAM-dependent methylation of a malonyl-thioester:

> malonyl-[ACP] + S-adenosyl-L-methionine = malonyl-[ACP] methyl ester + S-adenosyl-L-homocysteine

The enzyme contains a **Methyltransferase type 11 domain** (residues ~58–152; Pfam PF08241) embedded within the **Class I Rossmann-fold SAM-dependent methyltransferase superfamily**. The methyl group is transferred from SAM to the free ω-carboxyl group of the malonyl-thioester, generating a methyl ester and releasing S-adenosyl-L-homocysteine (SAH) as the demethylated cofactor product. This chemistry was mechanistically demonstrated in *E. coli* by Lin, Hanson & Cronan (2010) and has been independently confirmed for BioC enzymes from other bacteria, including the *Acinetobacter baumannii* and *Klebsiella pneumoniae* isoenzymes characterized in 2024, both of which act as malonyl-ACP methyltransferases that initiate biotin synthesis.

The defining statement of the reaction comes from the *E. coli* work: *"the omega-carboxyl group of a malonyl-thioester is methylated by BioC, which allows recognition of this atypical substrate by the fatty acid synthetic enzymes"* [PMID: 20693992]. The 2024 ESKAPE study reinforces the general validity of this assignment across pathogens: *"two BioC isoenzymes (AbBioC for A. baumannii and KpBioC for K. pneumoniae) that act as malonyl-ACP methyltransferase and initiate bi[otin synthesis]"* [PMID: 39705367]. For the *P. putida* protein the assignment is by orthology (see F003), with the reaction curated in UniProt via HAMAP rule MF_00835.

### F002 — BioC initiates the pimelate moiety by disguising malonyl-thioester for FAS II elongation

The biological purpose of BioC's methylation reaction is to launch the **pimelate (C7 α,ω-dicarboxylic acid) moiety of biotin**. Genetic and in vitro reconstitution experiments in *E. coli* established that the pimeloyl moiety is built by a **modified fatty acid synthetic pathway**. BioC methyl-esterifies the ω-carboxyl of a malonyl-thioester; the resulting methyl ester substitutes for the usual acetyl thioester primer and enters FAS. It then undergoes **two reiterations of the fatty acid elongation cycle** to yield **pimeloyl-ACP methyl ester**, which is subsequently hydrolyzed to pimeloyl-ACP plus methanol by BioH.

As the *E. coli* study describes: *"The malonyl-thioester methyl ester enters fatty acid synthesis as the primer and undergoes two reiterations of the fatty acid elongation cycle to give pimeloyl-acyl carrier protein (ACP) methyl ester, which is hydrolyzed to pimeloyl-ACP and methanol by BioH"* [PMID: 20693992]. A reconstituted desthiobiotin-synthesis system confirmed that malonyl-ACP is converted to pimeloyl-ACP via the pimeloyl-ACP methyl ester intermediate with the aid of FAS II: *"make pimeloyl-acyl carrier protein (ACP) from the substrate malonyl-ACP with the aid of the FAS II pathway, through the expected pimeloyl-ACP methyl ester intermediate"* [PMID: 30915508].

The strategic logic is elegant: the methyl ester acts as a chemical "disguise" that masks the extra carboxyl group of the dicarboxylic precursor, so that the strictly-specific FAS II enzymes — which would otherwise reject a charged, polar ω-carboxyl — accept and elongate it as though it were an ordinary fatty acyl chain. Methylation at the start (BioC) and demethylation at the end (BioH) bracket the FAS II elongation and control chain length. This places BioC firmly in the **cofactor biosynthesis; biotin biosynthesis** pathway (UniProt pathway annotation).

### F003 — bioC (PP_0365) sits in an intact, syntenic biotin gene cluster with its BioH esterase partner

A survey of the *P. putida* KT2440 genome shows the biotin genes are organized as a contiguous cluster at the **PP_0362–PP_0366** locus:

| Locus | Gene | Enzyme | EC |
|-------|------|--------|-----|
| PP_0362 | *bioB* | Biotin synthase | 2.8.1.6 |
| PP_0363 | *bioF* | KAPA/AON (8-amino-7-oxononanoate) synthase | 2.3.1.47 |
| PP_0364 | *bioH* | Pimeloyl-ACP methyl ester esterase | 3.1.1.85 |
| **PP_0365** | ***bioC*** | **Malonyl-ACP O-methyltransferase** | **2.1.1.197** |
| PP_0366 | *bioD* | Dethiobiotin synthetase | 6.3.3.3 |
| PP_4984 | *bioA* | DAPA (7,8-diaminononanoate) aminotransferase | 2.6.1.62 |

*bioC* is immediately flanked by *bioH* (PP_0364) — its physiological downstream esterase partner — and by *bioD* (PP_0366). The co-localization of *bioC* and *bioH* in the same cluster is a strong genomic signature of the canonical BioC-methylation route. *bioA* (PP_4984) lies elsewhere in the genome, a common arrangement in Pseudomonads.

The orthology evidence for the functional call is quantitative. Pairwise global alignment of Q88QW9 against the biochemically characterized *E. coli* BioC (P12999) gives **49.4% identity (118/239 aligned columns)**, and the SAM-binding glycine-rich Motif I (**LDLGSGTG**) is conserved at position 58 — the hallmark of a functional Class I methyltransferase SAM-binding pocket. Together, sequence identity, motif conservation, and genomic synteny establish that PP_0365 is a bona fide *bioC* ortholog operating in the canonical route.

### F004 — BioC's methyl acceptor is malonyl-ACP; the BioC–BioH route is one of several convergent pimelate strategies

Multiple reconstitution studies specify **malonyl-ACP** as the BioC methyl-acceptor substrate that is converted to pimeloyl-ACP via the pimeloyl-ACP methyl ester intermediate with FAS II [PMID: 30915508; PMID: 39705367]. The reaction is curated in UniProt/Rhea as malonyl-[ACP] + SAM → malonyl-[ACP] methyl ester + SAH (RHEA:17105). (In *E. coli*, malonyl-CoA can also serve as a substrate in vitro, with the ACP-tethered species being the physiological acceptor for downstream FAS II elongation.)

Importantly, the BioC–BioH strategy is only **one of several convergent, non-orthologous solutions** bacteria use to build pimeloyl-ACP. Alternative routes do **not** use BioC:

- **BioZ route**: BioZ is a domesticated β-ketoacyl-ACP synthase III that condenses glutaryl-CoA (or glutaryl-ACP) with malonyl-ACP to give 5-keto-pimeloyl-ACP — a completely different chemistry that bypasses BioC methylation entirely: *"BioZ catalyzes the condensation of glutaryl-CoA (or ACP) with malonyl-ACP to give 5'-keto-pimeloyl ACP"* [PMID: 33824341].
- **BioW/BioI-type routes** exist in yet other lineages.
- Downstream, the esterase step can be performed by evolutionarily distinct enzymes: **BioH** (the *E. coli* paradigm, present in *P. putida*), **BioG**, **BioK**, or the Helicobacter-restricted **BioV** — all catalyzing a common reaction with unrelated protein scaffolds [PMID: 23152908; PMID: 26868423].

In *P. putida* KT2440, the presence of both bona fide *bioC* (PP_0365) and *bioH* (PP_0364) unambiguously indicates the **canonical BioC-methylation route** rather than any of these bypasses. This comparative context sharpens the specific role of the *P. putida* enzyme: it is the SAM-dependent methyltransferase, not a condensing enzyme, and its output feeds a BioH esterase rather than a BioG/BioK/BioV alternative.

### F005 — BioC is a soluble cytoplasmic enzyme with no signal peptide or transmembrane segment

Sequence and feature analysis of the 272-residue Q88QW9 protein localizes BioC to the **cytoplasm**. UniProt annotates only a Domain feature (Methyltransferase type 11) and records **no signal peptide, no transmembrane helix, no intramembrane segment, and no lipidation site**. A Kyte-Doolittle hydropathy scan (window 19) gives a maximum windowed hydropathy of **1.25**, below the ~1.6 threshold indicative of a membrane-spanning helix — i.e., no predicted transmembrane region. The overall **GRAVY value is −0.034**, consistent with a hydrophilic, soluble protein. The N-terminus (MTDLSRPTLPGALPDKRQ…) lacks a cleavable signal-peptide hydrophobic core.

This localization is exactly what the biochemistry requires: BioC acts on ACP-tethered malonyl-thioesters, which are soluble cytosolic species processed by the equally soluble FAS II enzymes and the downstream biotin-synthesis proteins (BioF, BioA, BioD, BioB). All of these steps occur in the cytoplasm, and BioC is fully compatible with that compartment.

---

## Mechanistic Model / Interpretation

BioC catalyzes the very first, committed step that diverts primary fatty-acid-synthesis building blocks into the biotin biosynthetic pathway. The mechanistic logic is a "methyl-on / methyl-off" disguise strategy that allows a specialized C7 dicarboxylic acid to be assembled by the general-purpose fatty acid synthase.

```
                         SAM     SAH
                          \       /
                           \     /
   malonyl-ACP  ───────────► BioC ───────────►  malonyl-ACP methyl ester
   (free ω-COOH)          (PP_0365)              (ω-COOH now "disguised"
                          EC 2.1.1.197            as a methyl ester)
                                                          │
                                                          │  enters FAS II
                                                          │  as an atypical primer
                                                          ▼
                                          ── 2 cycles of FAS II elongation ──
                                          (FabB/F, FabG, FabA/Z, FabI; malonyl-ACP)
                                                          │
                                                          ▼
                                             pimeloyl-ACP methyl ester
                                                          │
                                                          │  BioH (PP_0364)
                                                          │  esterase, EC 3.1.1.85
                                                          │  (+ H2O → methanol)
                                                          ▼
                                                   pimeloyl-ACP
                                                          │
                                                          ▼
   BioF (PP_0363) ── + L-alanine ──► KAPA (AON)
   BioA (PP_4984) ── transamination ──► DAPA (DAN)
   BioD (PP_0366) ── + CO2/ATP ──► dethiobiotin
   BioB (PP_0362) ── + S ──► BIOTIN
```

The key conceptual points:

1. **BioC is the "gate-opener."** Without the methyl ester, FAS II would reject the malonyl species' extra carboxyl. Methylation makes the substrate look like an ordinary acyl primer, so the standard elongation cycle proceeds.
2. **Chain-length control is bracketed by methylation/demethylation.** BioC installs the methyl ester at the start; BioH removes it at exactly the right chain length (pimeloyl, C7), which both stops further elongation and hands off pimeloyl-ACP to the amino-transfer/ring-forming steps. This is why the two enzymes are functionally coupled and genomically co-located.
3. **BioC defines the pathway's identity.** The presence of *bioC* + *bioH* (rather than BioZ, BioW, or a BioG/BioK/BioV esterase) tells us *P. putida* uses the *E. coli*-type modified-FAS route. This is the single most informative diagnostic for the organism's pimelate strategy.
4. **All chemistry is cytosolic.** BioC, FAS II, BioH, and the downstream Bio enzymes are soluble and operate on soluble ACP-tethered intermediates in the cytoplasm.

The confidence level for the *P. putida* assignment is high but is fundamentally an **orthology-based inference**: the reaction has not been directly measured on the purified *P. putida* enzyme. However, 49% identity to a biochemically validated enzyme, a conserved SAM-binding motif, an intact syntenic operon, and consistency with a well-established, conserved pathway together make the assignment robust.

---

## Evidence Base

| PMID | Title / Focus | How it supports the findings |
|------|---------------|------------------------------|
| [PMID: 20693992](https://pubmed.ncbi.nlm.nih.gov/20693992/) | *Biotin synthesis begins by hijacking the fatty acid synthetic pathway* (Lin, Hanson & Cronan, 2010) | Foundational mechanism: BioC methylates the ω-carboxyl of a malonyl-thioester; the methyl ester enters FAS as a primer, is elongated twice to pimeloyl-ACP methyl ester, then hydrolyzed by BioH. Supports F001 and F002. |
| [PMID: 30915508](https://pubmed.ncbi.nlm.nih.gov/30915508/) | *Functional Replacement of BioC and BioH by Ehrlichia chaffeensis Novel Proteins* | Reconstitution confirming malonyl-ACP → pimeloyl-ACP via the pimeloyl-ACP methyl ester intermediate with FAS II. Supports F002 and F004 (substrate = malonyl-ACP). |
| [PMID: 39705367](https://pubmed.ncbi.nlm.nih.gov/39705367/) | *A bacterial methyltransferase that initiates biotin synthesis, an attractive anti-ESKAPE druggable pathway* (2024) | Independent characterization of AbBioC and KpBioC as malonyl-ACP methyltransferases that initiate biotin synthesis. Supports F001 and F004 across diverse bacteria. |
| [PMID: 33824341](https://pubmed.ncbi.nlm.nih.gov/33824341/) | *Biochemical and structural characterization of BioZ* | Documents the BioZ condensation route (glutaryl-CoA + malonyl-ACP → 5-keto-pimeloyl-ACP), an alternative that bypasses BioC. Supports F004 (convergent strategies). |
| [PMID: 23045647](https://pubmed.ncbi.nlm.nih.gov/23045647/) | *Structure of the BioH–ACP substrate gatekeeper complex* | Cocrystal structure showing BioH is the physiological "gatekeeper" whose substrate is pimeloyl-ACP methyl ester — the product of BioC-initiated elongation. Contextualizes the BioC→BioH handoff. |
| [PMID: 23152908](https://pubmed.ncbi.nlm.nih.gov/23152908/) | *Remarkable diversity in the enzymes catalyzing the last step of pimelate synthesis* | Shows BioH can be replaced by evolutionarily distinct BioG/BioK esterases; a BioG-BioC fusion can replace both functions. Supports F004 (diversity of the esterase step). |
| [PMID: 26868423](https://pubmed.ncbi.nlm.nih.gov/26868423/) | *A Biotin Biosynthesis Gene Restricted to Helicobacter* (BioV) | Identifies BioV as a Helicobacter-specific pimeloyl-ACP methyl ester esterase — another esterase alternative to BioH. Supports F004. |
| [PMID: 32117167](https://pubmed.ncbi.nlm.nih.gov/32117167/) | Pimeloyl-ACP methyl ester esterase (BioH paradigm) | Reinforces BioH's role as the esterase catalyzing the last biosynthetic step of the pimelate moiety, the partner reaction to BioC. |
| [PMID: 31085296](https://pubmed.ncbi.nlm.nih.gov/31085296/) | *Multi-level metabolic engineering of Pseudomonas mutabilis for biotin production* | Demonstrates the biotin pathway (including BioC-type initiation) is engineerable in Pseudomonads for overproduction — relevant applied context. |

Across the 9 papers reviewed, the mechanism of BioC (ω-carboxyl methylation of a malonyl-thioester to initiate a modified FAS route) is consistently supported, and no study challenges the core assignment. The primary source of uncertainty is not the mechanism but the fact that direct biochemistry has been done on *E. coli* and ESKAPE-pathogen orthologs rather than on the *P. putida* protein itself.

---

## Limitations and Knowledge Gaps

1. **No direct biochemical characterization of the *P. putida* enzyme.** The catalytic activity, substrate specificity, and kinetics for Q88QW9 have not been measured experimentally. The assignment is by orthology (49% identity to *E. coli* BioC, conserved SAM-binding motif, HAMAP MF_00835) and genomic context. While robust, this is inference, not measurement.

2. **No experimental structure.** There is no crystal or cryo-EM structure of *P. putida* BioC; the Rossmann-fold/Methyltransferase type 11 architecture is inferred from family assignment. An AlphaFold model with confidence analysis of the SAM-binding pocket and catalytic residues would strengthen the structural picture.

3. **Substrate form not directly confirmed for *P. putida*.** Whether the physiological acceptor in *P. putida* is malonyl-ACP (versus malonyl-CoA) is inferred from the general FAS II mechanism; it has not been directly tested in this organism.

4. **Regulation and expression context unstudied.** Operon regulation (e.g., a BirA/biotin-repressor system), expression conditions, and metabolic flux control for the *P. putida* biotin cluster were not characterized in this investigation.

5. **Localization is predicted, not observed.** Cytoplasmic localization is inferred from the absence of a signal peptide/TM helix and hydropathy analysis, consistent with the biochemistry, but has not been experimentally verified for this protein.

---

## Proposed Follow-up Experiments / Actions

1. **Direct enzymatic assay of purified *P. putida* BioC.** Express and purify Q88QW9, and measure SAM-dependent methylation of malonyl-ACP (and malonyl-CoA) by monitoring SAH production or methyl-ester formation. Determine kcat/Km and confirm substrate preference.

2. **Genetic complementation.** Test whether *P. putida* PP_0365 restores biotin prototrophy to an *E. coli* Δ*bioC* strain, the classic in vivo confirmation of function used for BioG/BioK/BioV orthologs.

3. **In vitro reconstitution.** Reconstitute pimeloyl-ACP synthesis from malonyl-ACP using purified *P. putida* BioC + FAS II + BioH (PP_0364), following the desthiobiotin-synthesis reconstitution approach [PMID: 30915508], to verify the full BioC→BioH handoff in this organism.

4. **Structural determination / modeling.** Solve or model (AlphaFold) the *P. putida* BioC structure; validate the SAM-binding pocket (Motif I LDLGSGTG at position 58) and identify the catalytic residue(s) that position the ω-carboxyl for methyl transfer.

5. **Deletion phenotyping.** Construct a PP_0365 knockout and assess biotin auxotrophy and rescue by exogenous biotin, pimelate, or pimeloyl-ACP methyl ester, confirming the committed-step role.

6. **Comparative pathway confirmation.** Bioinformatically confirm the absence of BioZ/BioW/BioG/BioK/BioV genes in *P. putida* KT2440, cementing that the canonical BioC–BioH route is the sole pimelate strategy in this strain.

---

## Conclusion

BioC (Q88QW9, PP_0365) is the *Pseudomonas putida* KT2440 malonyl-[acyl-carrier-protein] O-methyltransferase (EC 2.1.1.197), a soluble cytoplasmic SAM-dependent Class I methyltransferase that catalyzes the committed first step of biotin's pimelate moiety. It methyl-esterifies the free ω-carboxyl of malonyl-ACP, disguising it so FAS II elongates it to pimeloyl-ACP methyl ester, which the adjacent BioH esterase (PP_0364) converts to pimeloyl-ACP feeding the BioF→BioA→BioD→BioB biotin ring-assembly steps. The assignment is supported by 49% identity to biochemically validated *E. coli* BioC, a conserved SAM-binding motif, HAMAP rule MF_00835, and an intact syntenic bioBFHCD operon — pending direct biochemical confirmation on the *P. putida* enzyme itself.


## Artifacts

- [OpenScientist final report](bioC-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](bioC-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:20693992
2. PMID:39705367
3. PMID:30915508
4. PMID:33824341
5. PMID:23152908
6. PMID:26868423
7. PMID:23045647
8. PMID:32117167
9. PMID:31085296