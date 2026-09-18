---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-13T08:16:31.936930'
end_time: '2026-08-13T09:13:24.089753'
duration_seconds: 3412.15
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: xpt
  gene_symbol: xpt
  uniprot_accession: Q88CB6
  protein_description: 'RecName: Full=Xanthine phosphoribosyltransferase {ECO:0000255|HAMAP-Rule:MF_01184};
    Short=XPRTase {ECO:0000255|HAMAP-Rule:MF_01184}; EC=2.4.2.22 {ECO:0000255|HAMAP-Rule:MF_01184};'
  gene_info: Name=xpt {ECO:0000255|HAMAP-Rule:MF_01184}; OrderedLocusNames=PP_5265;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the purine/pyrimidine phosphoribosyltransferase
  protein_domains: PRTase-like. (IPR029057); PRTase_dom. (IPR000836); Pur/Pyrimidine_PRTase.
    (IPR050118); Xanthine_PRibTrfase. (IPR010079)
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
  path: xpt-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: xpt-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88CB6
- **Protein Description:** RecName: Full=Xanthine phosphoribosyltransferase {ECO:0000255|HAMAP-Rule:MF_01184}; Short=XPRTase {ECO:0000255|HAMAP-Rule:MF_01184}; EC=2.4.2.22 {ECO:0000255|HAMAP-Rule:MF_01184};
- **Gene Information:** Name=xpt {ECO:0000255|HAMAP-Rule:MF_01184}; OrderedLocusNames=PP_5265;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the purine/pyrimidine phosphoribosyltransferase
- **Key Domains:** PRTase-like. (IPR029057); PRTase_dom. (IPR000836); Pur/Pyrimidine_PRTase. (IPR050118); Xanthine_PRibTrfase. (IPR010079)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "xpt" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'xpt' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **xpt** (gene ID: xpt, UniProt: Q88CB6) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of *xpt* — Xanthine Phosphoribosyltransferase (Q88CB6, PP_5265)
### *Pseudomonas putida* KT2440

## 0. Gene/Protein Identity Verification

Before research, the target identity was confirmed against UniProt and matches the literature used here:

| Attribute | Value (verified) |
|---|---|
| UniProt accession | **Q88CB6** (reviewed / Swiss-Prot) |
| Gene name | **xpt**; ordered locus **PP_5265** |
| Protein | Xanthine phosphoribosyltransferase (XPRTase), **EC 2.4.2.22** |
| Length | 190 aa; **homodimer**; **cytoplasm** |
| Organism | *Pseudomonas putida* KT2440 (ATCC 47054 / DSM 6125 / KT2440) |
| Family | Purine/pyrimidine phosphoribosyltransferase, **Xpt subfamily** (HAMAP MF_01184) |
| Domains | Type I PRTase (PRTase-like, IPR029057; PRTase_dom, IPR000836; Xanthine_PRibTrfase, IPR010079) |

The gene symbol *xpt* is **unambiguous and correct** for this protein: it is the canonical symbol for xanthine phosphoribosyltransferase, and the domain architecture, EC number, family, and reaction all align with the literature cited below. (Note: the *E. coli* gene *gpt*, encoding xanthine–**guanine** PRT / XGPRT, and human/parasite *hprt/hpt* are related but distinct family members with broader base specificity; where their structural/mechanistic data are used below, this is explicitly to inform the conserved catalytic machinery of the type I PRTase family, not to substitute a different gene.)

---

## 1. Summary (Answer to the Research Question)

**xpt encodes xanthine phosphoribosyltransferase (XPRTase, EC 2.4.2.22), a cytoplasmic, Mg²⁺-dependent enzyme of the purine *salvage* pathway.** Its primary and essentially sole catalytic function is to transfer the 5-phosphoribosyl group of 5-phospho-α-D-ribose-1-diphosphate (PRPP) onto the N9 nitrogen of the free purine base **xanthine**, producing **xanthosine-5′-monophosphate (XMP)** and inorganic pyrophosphate. This single reaction ("XMP from xanthine: step 1/1") reclaims xanthine — a product of nucleic-acid and purine turnover — into the nucleotide pool, where XMP is converted to GMP by GMP synthetase and channels into guanine-nucleotide metabolism. The enzyme acts in the **cytosol**, works as a homodimer of a type I PRTase fold, and is genomically and regulatorily embedded in a xanthine-utilization module together with a xanthine permease (pbuX-type), controlled by purine availability.

---

## 2. Primary Molecular Function — the Reaction Catalyzed

**Reaction (UniProt Q88CB6 / HAMAP MF_01184):**

> XMP + diphosphate ⇌ xanthine + 5-phospho-α-D-ribose 1-diphosphate  (EC 2.4.2.22)

i.e. in the physiological (salvage) direction:

> **xanthine + PRPP → XMP + PPᵢ**  (Mg²⁺-dependent)

UniProt describes the function as: *"Converts the preformed base xanthine, a product of nucleic acid breakdown, to xanthosine 5'-monophosphate (XMP), so it can be reused for RNA or DNA synthesis."* The metabolic pathway assignment is *"Purine metabolism; XMP biosynthesis via salvage pathway; XMP from xanthine: step 1/1"* — meaning xpt performs the complete, one-step salvage conversion of xanthine to a nucleotide.

**Substrate specificity.** The Xpt subfamily is defined by *specific* recognition of xanthine, in contrast to the broader hypoxanthine-guanine PRTs (HGPRT) or the xanthine-guanine PRT (XGPRT/*gpt*) of *E. coli*. This specificity was established biochemically for the founding member of the subfamily in *Bacillus subtilis*, where **"the *xpt* gene encodes a specific xanthine phosphoribosyltransferase"** [Christiansen et al., 1997, PMID 9098051]. The *P. putida* protein Q88CB6 is a direct orthologue in the same Xpt subfamily and is annotated with the identical dedicated activity.

**Direction / thermodynamics.** Like all type I purine PRTases the reaction is formally reversible (pyrophosphorolysis is measurable in vitro), but in vivo it is driven forward by (i) the high group-transfer potential of PRPP and (ii) hydrolysis of the released pyrophosphate by inorganic pyrophosphatase, making salvage effectively unidirectional under cellular conditions.

---

## 3. Catalytic Mechanism and Structural Basis

XPRTase belongs to the **type I PRTase structural family**, built on a Rossmann-like α/β core domain that binds PRPP plus a smaller "hood" subdomain that caps the purine base (IPR029057/IPR000836/IPR010079). Precise mechanistic understanding derives from high-resolution structures and kinetics of the closely related 6-oxopurine PRTases (HPRT/HGPRT/HG(X)PRT), whose catalytic residues and reaction chemistry are conserved across the family:

1. **Ordered sequential (bi-bi) kinetics.** Substrates add in a defined order — **PRPP (with Mg²⁺) binds first, then the purine base** — and products leave in order — **pyrophosphate first, then the nucleotide**. This was shown by steady-state kinetics of *Tritrichomonas foetus* HG(X)PRTase: *"the substrates bind to the enzyme (first PRPP followed by the purine bases), and the products released (first PPi followed by purine nucleotide) in a defined order"* [Munagala et al., 1998, PMID 9521725].

2. **Two-metal-ion ribosyl transfer.** The *Trypanosoma cruzi* HPRT ternary complex revealed that *"the ligands are positioned for in-line nucleophilic attack at the PRPP ribose C1' by two metal ions which straddle the pyrophosphate leaving group,"* consistent with SN2-type/oxocarbenium-stabilized chemistry at the anomeric carbon [Focia et al., 1998, PMID 9860824]. Catalysis inverts the anomeric configuration, forming the β-N9-glycosidic bond of the nucleotide.

3. **Flexible catalytic loop closure.** A mobile active-site loop closes over the bound substrates to sequester the reaction from solvent and to position the pyrophosphate for departure. Free vs. liganded human HGPRT structures show that *"significant conformational changes have to occur for the substrate(s) to bind and for catalysis to proceed"* [Keough et al., 2005, PMID 15990111]; the conserved Ser-Tyr loop dipeptide participates in PPᵢ liberation.

4. **Cofactor and quaternary structure.** The enzyme requires **Mg²⁺** (as the Mg-PRPP complex and as active-site catalytic metal) and functions as a **homodimer** in *P. putida* (UniProt Q88CB6); other family members are dimers or tetramers.

These features are directly transferable to Q88CB6 by strong sequence/structural homology within the Xpt subfamily, and constitute *inference from structure and evolution* for the P. putida enzyme.

### 3.5 Active-site residues mapped on Q88CB6 itself
Curated UniProt features (HAMAP MF_01184) place the catalytic machinery on specific residues of the 190-aa P. putida chain, providing direct sequence-level evidence rather than pure homology transfer:

| Ligand | Residues in Q88CB6 | Note |
|---|---|---|
| **Xanthine** (purine base) | Leu20, Asn27, Lys156 | base recognition in the "hood" region; specificity determinants |
| **PRPP** (5-phosphoribosyl-1-PP) | loop 128–132 (…ANGK A…) | phosphate/ribose binding |
| **Twin-aspartate motif** | Asp-Asp within "…V I **D D** F L A N G K…" (~res 127–129) | invariant type I PRTase PRPP-binding signature (PROSITE PS00103); coordinates ribose-5-phosphate and catalytic Mg²⁺ |

The presence and correct spacing of the diagnostic Asp-Asp PRPP loop plus dedicated xanthine contacts confirm Q88CB6 is a catalytically competent, xanthine-specific type I PRTase independent of homology arguments alone.

---

### 3.6 Structural-model confidence (AlphaFold)
The AlphaFold DB model of Q88CB6 (v6, 190 aa) is of very high quality — **mean pLDDT 94.9** (median 97.8; 88 % of residues > 90, 97 % > 70, none < 50) — describing a single, well-ordered globular domain with no substantial disordered regions. Critically, all curated ligand-binding residues are modelled at very-high confidence (Leu20 = 97.4, Asn27 = 97.3, Lys156 = 97.6; PRPP loop 128–132 = 94–95), giving independent structural support that the enzyme adopts a properly constituted type I PRTase fold (Rossmann-like PRPP core + purine "hood") with an intact xanthine/PRPP active site.

## 4. Subcellular Localization

XPRTase is a soluble **cytoplasmic** enzyme (UniProt Q88CB6, subcellular location: Cytoplasm), consistent with (i) its role in intracellular nucleotide metabolism, (ii) its use of the cytosolic metabolites PRPP and free purine bases, and (iii) the absence of signal peptides or membrane-spanning segments in the 190-residue chain. The upstream/co-operonic xanthine permease (PbuX-type) is the membrane component that supplies the base; the PRTase itself acts in the cytosol immediately downstream of import.

---

## 5. Pathway Context and Biological Role

### 5.1 Position in purine salvage
xpt is the committed, terminal step that converts free xanthine into a nucleotide. Its product **XMP is the direct precursor of GMP**: XMP → GMP is catalyzed by GMP synthetase (guaA). Thus xanthine salvaged by XPRTase feeds specifically into the **guanine nucleotide pool** (XMP → GMP → GDP/GTP, dGTP). This wiring is made explicit by the conserved operon in *Staphylococcus aureus*, *"an operon encoding xanthine phosphoribosyltransferase (xpt), xanthine permease (pbuX), inosine-5'-monophosphate dehydrogenase (guaB), and GMP synthetase (guaA)"* [Kofoed et al., 2016, PMID 27161118] — grouping the transporter, the salvage PRTase, and the two enzymes that convert its product toward GMP.

### 5.2 The xanthine-utilization module (transport + salvage) — and its divergence in *P. putida*
xpt is functionally linked to a **xanthine-specific permease** that supplies its substrate. In *B. subtilis*, *xpt* and *pbuX* have overlapping reading frames and *"an operon organization,"* with pbuX translation dependent on xpt translation [PMID 9098051]; the same *xpt–pbuX* coupling recurs in *S. aureus* [PMID 27161118]. The logic is: import xanthine, then immediately phosphoribosylate it.

**Important organism-specific correction (this work).** This operonic coupling is **not** conserved in *P. putida* KT2440. Genome-context analysis (KEGG) shows **xpt = PP_5265 is monocistronic**: it lies at 6,013,223–6,013,795 flanked by functionally unrelated genes — a Rep-type ssDNA-dependent helicase (PP_5264) and an acetyl-CoA-hydrolase-family protein (PP_5266), with a GGDEF protein (PP_5263) and a putative cytochrome c5 (PP_5267) nearby. **No xanthine permease is adjacent.** The candidate xanthine/uracil (NCS2-family) permeases of KT2440 (PP_3655, PP_4035, PP_4309) are dispersed elsewhere on the chromosome and are genomically unlinked to xpt. Thus in *P. putida* the salvage *reaction* is conserved, but xanthine transport is supplied **in trans** by separately encoded permeases rather than by an operon-linked pbuX. Consequently the riboswitch-in-operon regulatory model established in Firmicutes (§5.3) should **not** be assumed to hold in this organism.

### 5.3 Regulation — responsive to purine availability
Because salvage is only useful when preformed purines are present, xpt expression is tuned to purine levels:
- **Purine repression / riboswitch control.** The *B. subtilis xpt-pbuX* operon is preceded by a **guanine riboswitch** that *"directly binds guanine, hypoxanthine or xanthine to terminate transcription"* [Batey et al., 2004, PMID 15549109; the same aptamer structural class characterized in PMID 17959930]. Expression is repressed up to 160-fold by hypoxanthine+guanine via transcription antitermination [PMID 9098051]. This couples XPRTase production to intracellular purine sufficiency.
- **Physiological dispensability.** As a salvage (not de novo) function, xpt is individually non-essential when de novo synthesis operates: in *S. aureus*, *"deletion of the purine salvage genes xpt-pbuX had none of these effects"* on growth/virulence, whereas loss of the downstream de novo/GMP enzymes was deleterious [PMID 27161118]. This pinpoints xpt's role as an economizing salvage route rather than an indispensable biosynthetic step.

### 5.4 Organism-specific relevance in *P. putida*
*P. putida* is a metabolically versatile soil bacterium capable of purine and methylxanthine catabolism. Classic work on *P. putida* showed degradation of xanthine through **uric acid → allantoin → allantoic acid** (e.g., during caffeine/methylxanthine breakdown) [Blecher & Lingens, 1977, PMID 561017]. XPRTase sits at the **branch point** between this catabolic fate of xanthine (oxidation to urate for use as C/N source) and the **anabolic salvage** fate (phosphoribosylation to XMP for nucleotide synthesis). By capturing xanthine as XMP, xpt allows the cell to recycle purine bases into GTP/dGTP pools rather than committing them to oxidative catabolism, thereby conserving carbon, nitrogen, and biosynthetic energy.

---

## 6. Evidence Summary

| Claim | Type of evidence | Source |
|---|---|---|
| xpt = xanthine PRTase, EC 2.4.2.22; reaction xanthine+PRPP→XMP+PPᵢ; salvage step 1/1; cytoplasm; homodimer | Curated database annotation (HAMAP rule, reviewed) | UniProt Q88CB6 |
| Xpt is *specific* for xanthine (defines subfamily specificity) | Direct biochemical (cloning + enzyme characterization) | PMID 9098051 |
| Two-metal-ion, in-line ribosyl transfer at PRPP C1′ | Experimental structure (ternary complex) of homologue | PMID 9860824 |
| Ordered bi-bi kinetics (PRPP first; PPᵢ released first) | Steady-state kinetics of homologue | PMID 9521725 |
| Flexible catalytic-loop conformational change during catalysis | Experimental structures (apo vs. liganded) | PMID 15990111 |
| xpt–pbuX operon (transport+salvage coupling) | Genetic/transcriptional (operon mapping) | PMID 9098051 |
| xpt→XMP feeds guaB/guaA→GMP; salvage genes dispensable | Genetic (operon architecture, deletions) | PMID 27161118 |
| Purine/guanine-riboswitch regulation of xpt operon | Structural + genetic | PMID 15549109; 9098051; 17959930 |
| Xanthine catabolism (urate/allantoin) in *P. putida* | Biochemical pathway characterization | PMID 561017 |
| Q88CB6 active site: xanthine at L20/N27/K156; PRPP loop 128–132 with twin-Asp motif | Curated sequence features / motif analysis | UniProt Q88CB6; PROSITE PS00103 |
| xpt (PP_5265) is monocistronic in *P. putida*; NCS2 permeases (PP_3655/4035/4309) unlinked | Genome-context (bioinformatic) analysis | KEGG ppu:PP_5265 & neighbours |
| Q88CB6 folds as a confident type I PRTase (mean pLDDT 94.9; active-site residues >94) | Structural prediction | AlphaFold DB Q88CB6 (v6) |

**Evidence tiers:** Q88CB6-specific claims (reaction, EC, pathway, localization, oligomeric state) rest on curated, rule-based database annotation. Substrate specificity is supported by direct biochemistry on the orthologous B. subtilis Xpt. Mechanistic details are strong *inferences from structure and evolution* using experimentally solved structures/kinetics of closely related type I purine PRTases (HPRT/HG(X)PRT), whose catalytic apparatus is conserved.

---

## 7. Supported and Refuted Hypotheses

- **Supported:** *xpt* catalyzes xanthine + PRPP → XMP + PPᵢ (dedicated xanthine salvage). ✔
- **Supported:** The enzyme is cytoplasmic, Mg²⁺-dependent, homodimeric, type I PRTase fold with ordered bi-bi mechanism. ✔ (annotation + homology/mechanistic inference)
- **Supported:** XMP product feeds guanine-nucleotide synthesis (via guaB/guaA→GMP); xpt is a purine-availability-regulated salvage function. ✔
- **Refuted / not supported:** That *P. putida* xpt is a broad-specificity xanthine-**guanine** PRT like *E. coli* gpt — the Xpt subfamily and the founding biochemistry indicate *xanthine-specific* activity, not the dual xanthine/guanine XGPRT. ✘
- **Refuted / not supported:** That xpt is an essential/de novo biosynthetic enzyme — it is a dispensable salvage route under de novo-competent conditions. ✘
- **Refuted for *P. putida* (revised in Iteration 2):** That xpt is operon-coupled to a pbuX xanthine permease in *P. putida* as in Firmicutes — genome context shows PP_5265 is monocistronic; transport is supplied in trans by unlinked NCS2 permeases. ✘

---

## 8. Limitations and Future Directions

1. **No direct enzymology on Q88CB6 itself.** Kinetic constants (Km for xanthine and PRPP, kcat), metal-ion stoichiometry, and an experimental structure have not, to my knowledge, been reported specifically for the *P. putida* KT2440 protein; the functional assignment relies on curated annotation and orthology to the biochemically characterized *B. subtilis* Xpt and to structurally characterized family members. Recombinant expression + steady-state kinetics and a crystal/cryo-EM or AlphaFold-validated structure would confirm specificity and mechanism directly.
2. **Regulatory architecture in *P. putida* not fully mapped.** The guanine-riboswitch/purine-repression model is best established in Gram-positive Firmicutes; the precise *cis*-regulatory elements and operon boundaries around PP_5265 in *P. putida* KT2440 should be verified transcriptomically.
3. **Metabolic partitioning.** The quantitative flux split between xanthine salvage (via Xpt) and xanthine catabolism (urate/allantoin) in *P. putida* under different C/N regimes is an open, experimentally testable question (e.g., ¹³C/¹⁵N tracing, Δxpt mutant phenotyping on xanthine as N source).

---

*Prepared as an autonomous functional-annotation report. Finalized in Iteration 3 of 3. Six findings recorded across iterations: reaction/specificity, mechanism, salvage-module context, Q88CB6 active-site mapping, P. putida monocistronic genomic context, and AlphaFold structural confidence.*


## Artifacts

- [OpenScientist final report](xpt-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](xpt-deep-research-openscientist_artifacts/final_report.pdf)