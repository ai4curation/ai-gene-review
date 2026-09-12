---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-23T16:39:02.901615'
end_time: '2026-07-23T16:52:44.657719'
duration_seconds: 821.76
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: fabV
  gene_symbol: fabV
  uniprot_accession: Q88E33
  protein_description: 'RecName: Full=Enoyl-[acyl-carrier-protein] reductase [NADH]
    {ECO:0000255|HAMAP-Rule:MF_01838}; Short=ENR {ECO:0000255|HAMAP-Rule:MF_01838};
    EC=1.3.1.9 {ECO:0000255|HAMAP-Rule:MF_01838};'
  gene_info: Name=fabV {ECO:0000255|HAMAP-Rule:MF_01838}; OrderedLocusNames=PP_4635;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the TER reductase family. {ECO:0000255|HAMAP-
  protein_domains: Eno_Rdtase_FAD-bd_dom. (IPR024906); Enoyl-CoA_Rdtase_cat_dom. (IPR024910);
    FabV-like_NADH_b. (IPR050048); Trans-2-enoyl-CoA_reductase. (IPR010758); Eno-Rase_FAD_bd
    (PF07055)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 1
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
  path: fabV-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: fabV-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88E33
- **Protein Description:** RecName: Full=Enoyl-[acyl-carrier-protein] reductase [NADH] {ECO:0000255|HAMAP-Rule:MF_01838}; Short=ENR {ECO:0000255|HAMAP-Rule:MF_01838}; EC=1.3.1.9 {ECO:0000255|HAMAP-Rule:MF_01838};
- **Gene Information:** Name=fabV {ECO:0000255|HAMAP-Rule:MF_01838}; OrderedLocusNames=PP_4635;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the TER reductase family. {ECO:0000255|HAMAP-
- **Key Domains:** Eno_Rdtase_FAD-bd_dom. (IPR024906); Enoyl-CoA_Rdtase_cat_dom. (IPR024910); FabV-like_NADH_b. (IPR050048); Trans-2-enoyl-CoA_reductase. (IPR010758); Eno-Rase_FAD_bd (PF07055)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "fabV" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'fabV' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **fabV** (gene ID: fabV, UniProt: Q88E33) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: FabV (Q88E33) — Enoyl-[acyl-carrier-protein] reductase [NADH] of *Pseudomonas putida* KT2440

**Gene:** *fabV* (OrderedLocusName PP_4635)
**UniProt:** Q88E33
**Organism:** *Pseudomonas putida* strain ATCC 47054 / DSM 6125 / KT2440 (PSEPK)
**Enzyme:** Enoyl-[acyl-carrier-protein] reductase [NADH]; ENR; EC 1.3.1.9
**Family:** TER reductase / FabV-like NADH-dependent reductase family (InterPro IPR050048, IPR010758, IPR024906, IPR024910; Pfam PF07055 Eno-Rase_FAD_bd)
**Report date:** 2026-07-23

---

## 0. Gene/Protein Identity Verification (MANDATORY)

The target was cross-checked against the four verification criteria before any research claims were made:

1. **Symbol vs. description:** The gene symbol *fabV* matches the UniProt description "Enoyl-[acyl-carrier-protein] reductase [NADH]" exactly. In the *fab* (fatty acid biosynthesis) nomenclature, *fabV* is the established, unambiguous name for the fourth class of enoyl-ACP reductase (ENR). This is *not* a case of symbol collision.
2. **Organism:** Literature confirms that *Pseudomonas* species (notably *P. aeruginosa* PAO1) carry a *fabV* gene alongside *fabI*; the *P. putida* KT2440 ortholog PP_4635/Q88E33 sits in the same lineage and enzyme family.
3. **Family/domain alignment:** The UniProt family assignment ("TER reductase family") and domains (Trans-2-enoyl-CoA reductase IPR010758; FabV-like NADH-b IPR050048; Eno-Rase FAD-binding PF07055) align precisely with the published FabV/TER class — larger (~400 aa) than FabI, a short-chain dehydrogenase/reductase (SDR) with a Rossmann fold and a Y-X₈-K catalytic motif.
4. **No conflicting literature:** The symbol *fabV* returns a single, internally consistent body of literature (all enoyl-ACP/CoA reductases). No divergent gene shares this symbol.

**Conclusion:** Identity is confirmed. *fabV*/PP_4635/Q88E33 is a *bona fide* FabV-class enoyl-ACP reductase. Because no *P. putida*-specific enzymological paper was located, function is established by (i) the defining biochemistry of the FabV class and (ii) direct orthology, with organism-specific inferences flagged as such.

---

## 1. Summary (Answer to the Research Question)

**FabV (Q88E33, PP_4635) is the NADH-dependent enoyl-[acyl-carrier-protein] reductase (ENR; EC 1.3.1.9) of *Pseudomonas putida* KT2440.** It catalyzes the **final, committed reduction step of every elongation cycle of the bacterial type II fatty acid synthesis (FAS-II) pathway**: the stereospecific NADH-dependent reduction of the *trans*-2 double bond of *trans*-2-enoyl-ACP to the saturated acyl-ACP. This reaction pulls each round of chain elongation to completion and thereby drives the production of the acyl chains used for membrane phospholipid biosynthesis. FabV works as a soluble, **cytoplasmic monomeric enzyme** within the dissociated FAS-II system. It is a member of the short-chain dehydrogenase/reductase (SDR) superfamily and defines a distinct fourth ENR class (alongside FabI, FabL, and FabK), being larger (~400 residues) and displaying a **strong kinetic preference for NADH over NADPH**. A hallmark of the FabV class — highly relevant in *Pseudomonas* — is **intrinsic resistance to the biocide triclosan**, which inhibits the alternative isozyme FabI.

---

## 2. Primary Function: The Catalyzed Reaction and Substrate Specificity

### 2.1 The reaction
FabV catalyzes the last of the four reactions in each round of the FAS-II elongation cycle (condensation → ketoreduction → dehydration → **enoyl reduction**):

> *trans*-2-enoyl-[acyl-carrier-protein] + NADH + H⁺ → acyl-[acyl-carrier-protein] + NAD⁺   (EC 1.3.1.9)

Enoyl-ACP reductase "catalyzes the last step of the fatty acid elongation cycle" and is essential because it commits the elongated intermediate to a saturated acyl chain, making elongation effectively irreversible (Massengo-Tiassé & Cronan, 2008, PMID 18032386). Across the enzyme class, "FabI and its isoforms (FabL, FabK, FabV and InhA) are essential enoyl-ACP reductases" (Rana et al., 2020, PMID 32883635).

### 2.2 Substrate specificity and cofactor preference
- **Acyl-chain carrier:** The physiological substrate is enoyl-**ACP** (acyl carrier protein-linked). Purified FabV "is active with both crotonyl-ACP and the model substrate, crotonyl-CoA" (Massengo-Tiassé & Cronan, 2008, PMID 18032386), confirming it accepts short-chain enoyl thioesters and elongates the growing acyl chain through successive cycles.
- **Cofactor:** FabV has a "very strong preference for NADH over NADP(H)" (Massengo-Tiassé & Cronan, 2008, PMID 18032386) — reflected in the UniProt name "[NADH]." This contrasts with some ENR isoforms that can use NADPH, and is mechanistically explained by an ordered mechanism in which NADH binds first (Section 3).
- **Functional equivalence to FabI:** FabV is fully interchangeable with FabI at this step: heterologous *fabV* "restored fatty acid synthesis" to a conditionally lethal *E. coli fabI* mutant both in vivo and in vitro (Massengo-Tiassé & Cronan, 2008, PMID 18032386), and independently, "wild-type ucFabV, but not the [catalytic] mutant, functionally replaced FabI within living cells" (Fischer et al., 2015, PMID 26683704).

---

## 3. Catalytic Mechanism and Structural Basis

### 3.1 Kinetic mechanism
Detailed kinetics of the *Burkholderia mallei* ortholog show that "bmFabV catalyzes a sequential bi-bi mechanism with NADH binding first and NAD(+) dissociating last" (Lu & Tonge, 2010, PMID 20055482) — an **ordered bi-bi mechanism** in which cofactor binding precedes and gates substrate binding. This ordering rationalizes the strong NADH preference.

### 3.2 Active-site chemistry
FabV is an SDR-superfamily enzyme whose "catalytic tyrosine (Y235) and lysine (K244) residues are organized in the consensus Tyr-(Xaa)₈-Lys motif" and both "are involved in acid-base chemistry during substrate reduction," while a second lysine (K245) "has an important role in binding of the enoyl substrate" (Lu & Tonge, 2010, PMID 20055482). The catalytic Tyr protonates the substrate carbonyl-derived enolate while the nicotinamide ring delivers hydride to Cα, reducing the C2=C3 double bond.

### 3.3 Three-dimensional architecture
- The *Xanthomonas oryzae* FabV crystal structure (1.6 Å) is "a canonical Rossmann fold architecture," with the conserved Y236/K245 Y-X₈-K motif plus additional catalytically important residues (Y53, D111, Y226; T276) (Li et al., 2011, PMID 22039545).
- The *Yersinia pestis* FabV structure shows "the common architecture of the short-chain dehydrogenase reductase superfamily, but contains additional structural elements that are mostly folded around the usually flexible substrate-binding loop, thereby stabilizing it in a very tight conformation that seals the active site" (Hirschbeck et al., 2012, PMID 22244758). This extra loop structure is the defining feature that makes FabV larger than FabI and underlies its distinct inhibitor profile.
- FabV-class enzymes and their close relatives (trans-2-enoyl-CoA reductases, TERs) "function as monomers and consist of a cofactor-binding domain and a substrate-binding domain with the catalytic active site located at the interface of the two domains" (Hu et al., 2013, PMID 23050861). The FabV/TER relationship (>45% shared identity in TER structural studies; the target's family is literally "TER reductase family") confirms that Q88E33 is a monomeric two-domain reductase of this type.

---

## 4. Localization

FabV carries out its function in the **bacterial cytoplasm**. The bacterial FAS-II system is a *dissociated* (soluble, freestanding-enzyme) system in which each reaction — including the enoyl reduction performed by FabV — occurs on ACP-tethered intermediates in the cytosol; the fully elongated acyl chains are subsequently transferred to glycerophosphate acyltransferases at the inner membrane for phospholipid assembly. Consistent with this, FabV has no predicted signal peptide or transmembrane segment (it is a soluble SDR-fold protein purified to homogeneity as a monomer; Massengo-Tiassé & Cronan, 2008, PMID 18032386; Hu et al., 2013, PMID 23050861). Localization is therefore **cytoplasmic/soluble**, inferred from the biochemistry of the purified enzyme and the well-established topology of the FAS-II pathway.

---

## 5. Biochemical Pathway and Physiological Role

### 5.1 Pathway context
FabV operates within the **type II fatty acid synthesis (FAS-II) pathway**, "a crucial component of the universal bacterial fatty acid biosynthetic pathway (FasII)" (Bulai et al., 2025, PMID 40472483). In each elongation cycle: FabB/FabF condense malonyl-ACP with the growing acyl-ACP; FabG reduces the β-ketoacyl group; FabA/FabZ dehydrate the β-hydroxyacyl-ACP to *trans*-2-enoyl-ACP; and **FabV (or FabI) reduces enoyl-ACP to acyl-ACP**, readying it for the next condensation. The products feed directly into membrane glycerophospholipid biosynthesis.

### 5.2 Two ENR isozymes in *Pseudomonas*
A distinctive feature of *Pseudomonas* is the presence of **two ENR isozymes**. In *P. aeruginosa* PAO1, the organism "contains two enoyl-ACP reductase isozymes, the previously characterized FabI homologue plus a homologue of FabV" (Zhu et al., 2010, PMID 19933806), and this pathogen "co-expresses FabV with its more common isozyme FabI" (Bulai et al., 2025, PMID 40472483). By direct orthology, *P. putida* KT2440 FabV (PP_4635) is expected to act as a second, parallel ENR alongside the KT2440 FabI homolog, providing redundancy/robustness at the committed reduction step. *(Organism-specific inference; the deletion genetics were performed in P. aeruginosa, not P. putida.)*

### 5.3 Triclosan resistance
The biocide **triclosan** is a mechanism-based inhibitor of the FabI ENR but is a poor inhibitor of FabV. In *P. aeruginosa*, FabV is the actual determinant of triclosan resistance: "Upon deletion of the *fabV* gene, the mutant strain became extremely sensitive to triclosan (>2,000-fold more sensitive than the wild-type strain), whereas the mutant strain lacking FabI remained completely resistant to the biocide" (Zhu et al., 2010, PMID 19933806). The structural cause is the tightly sealed substrate-binding loop of FabV, which prevents productive triclosan binding (Hirschbeck et al., 2012, PMID 22244758). *P. putida* FabV is inferred to confer the same intrinsic triclosan tolerance.

### 5.4 Biotechnological and drug-target relevance
- Because FabV is essential to FAS-II and structurally distinct from FabI, it is an actively pursued **antibacterial target**; diaryl-ether and 2-pyridone inhibitor series have been developed specifically against FabV (Bulai et al., 2025, PMID 40472483; Neckles et al., 2016, PMID 27136302; Hirschbeck et al., 2012, PMID 22244758).
- The triclosan-resistance phenotype has been exploited as an **antibiotic-free plasmid-selection system** ("FabV–triclosan selection") for recombinant protein production in *E. coli* (Ali et al., 2015, PMID 26642325).
- The closely related NADH-dependent trans-2-enoyl-CoA reductases (TER family, to which FabV belongs) are workhorse enzymes in **engineered n-butanol and fatty-acid biosynthesis** pathways because they drive the reduction equilibrium forward (Hu et al., 2013, PMID 23050861; Bond-Watts et al., 2012, PMID 22906002).

---

## 6. Evidence Summary

| Claim | Evidence type | Source (PMID) |
|---|---|---|
| FabV = enoyl-ACP reductase, final FAS-II step | Direct biochemistry; complementation of *E. coli fabI* mutant | 18032386 |
| Reduces enoyl-ACP/CoA; strong NADH preference | Purified-enzyme assays | 18032386 |
| Ordered bi-bi mechanism (NADH first) | Steady-state kinetics (bmFabV) | 20055482 |
| Y-X₈-K catalytic motif; Tyr/Lys acid–base; K245 substrate binding | Site-directed mutagenesis | 20055482, 22039545 |
| Rossmann-fold SDR; sealed substrate loop | X-ray crystallography (xoFabV 1.6 Å; ypFabV) | 22039545, 22244758 |
| Monomeric two-domain reductase (FabV/TER family) | Crystallography + sequence analysis | 23050861 |
| FabV interchangeable with FabI in vivo | Functional complementation | 18032386, 26683704 |
| *Pseudomonas* carries both FabI and FabV | Genome + genetics (P. aeruginosa) | 19933806, 40472483 |
| FabV confers triclosan resistance (>2000-fold) | Gene-deletion phenotype | 19933806 |
| Drug target / biotech tool | Inhibitor SAR; selection system | 40472483, 27136302, 26642325 |

**Nature of evidence:** For the *P. putida* protein specifically, function rests on **strong orthology inference** (family/domain identity + a large, consistent body of FabV-class enzymology). The core reaction, mechanism, cofactor preference, structure, and triclosan phenotype are supported by **direct experimental evidence** in closely related orthologs (*V. cholerae*, *P. aeruginosa*, *B. mallei*, *Y. pestis*, *X. oryzae*).

---

## 7. Supported and Refuted Hypotheses

**Supported:**
- H1 — *fabV*/Q88E33 encodes an NADH-dependent enoyl-ACP reductase (EC 1.3.1.9) that performs the final reduction of the FAS-II elongation cycle. ✔ Strongly supported.
- H2 — The enzyme is a cytoplasmic, monomeric SDR-superfamily protein with a Rossmann fold and Y-X₈-K active site. ✔ Supported (structure of orthologs; soluble monomer).
- H3 — FabV prefers NADH via an ordered bi-bi mechanism. ✔ Supported.
- H4 — FabV confers intrinsic triclosan resistance and coexists with FabI in *Pseudomonas*. ✔ Supported in *P. aeruginosa*; inferred for *P. putida*.

**Refuted / not supported:**
- The earlier notion that *Pseudomonas* triclosan resistance is due solely to efflux is superseded — FabV is the primary genetic determinant (Zhu et al., 2010, PMID 19933806).
- No evidence supports any function outside FAS-II enoyl reduction (e.g., no transporter, structural, or signaling role); the domain architecture and biochemistry are exclusively consistent with an ENR.

---

## 8. Limitations and Future Directions

- **No *P. putida* KT2440-specific enzymology** was located; all mechanistic/structural data derive from orthologs. Direct enzymatic characterization, an *fabV* knockout phenotype, and a *P. putida* crystal structure would confirm inferred properties.
- **Essentiality/redundancy in KT2440** is inferred from *P. aeruginosa*. Whether *P. putida* FabV is individually essential or redundant with FabI (single- vs. double-knockout lethality) should be tested.
- **Chain-length substrate profile** (short vs. long enoyl-ACP preference) and precise kinetic constants for the *P. putida* enzyme are unknown.
- **Regulation** (transcriptional control, condition-dependent expression relative to FabI) in *P. putida* is uncharacterized.

---

## 9. Key References
- Massengo-Tiassé RP, Cronan JE. *Vibrio cholerae* FabV defines a new class of enoyl-acyl carrier protein reductase. *J Biol Chem* 2008. PMID 18032386.
- Zhu L, Lin J, Ma J, Cronan JE, Wang H. Triclosan resistance of *Pseudomonas aeruginosa* PAO1 is due to FabV. *Antimicrob Agents Chemother* 2010. PMID 19933806.
- Lu H, Tonge PJ. Mechanism and inhibition of the FabV enoyl-ACP reductase from *Burkholderia mallei*. *Biochemistry* 2010. PMID 20055482.
- Li H, Zhang Y, et al. Crystal structure and active residues of FabV from *Xanthomonas oryzae*. 2011. PMID 22039545.
- Hirschbeck M, Kuper J, et al. Structure of the *Yersinia pestis* FabV. *Structure* 2012. PMID 22244758.
- Hu K, et al. Structures of trans-2-enoyl-CoA reductases (TER/FabV family). 2013. PMID 23050861.
- Rana P, et al. FabI (enoyl-ACP reductase) — a potential broad-spectrum target and its inhibitors. 2020. PMID 32883635.
- Bulai A, et al. SAR of diaryl-ether-based paFabV inhibitors. 2025. PMID 40472483.
- Fischer C, et al. ucFabV requires functional reductase activity. 2015. PMID 26683704.
- Neckles C, et al. Selectivity of inhibitors for *Y. pestis* FabV. 2016. PMID 27136302.
- Ali S, et al. FabV–Triclosan plasmid selection system. 2015. PMID 26642325.


## Artifacts

- [OpenScientist final report](fabV-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](fabV-deep-research-openscientist_artifacts/final_report.pdf)