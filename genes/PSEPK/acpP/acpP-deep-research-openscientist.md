---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-23T16:15:32.225613'
end_time: '2026-07-23T16:38:20.505159'
duration_seconds: 1368.28
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: acpP
  gene_symbol: acpP
  uniprot_accession: Q88LL5
  protein_description: 'RecName: Full=Acyl carrier protein {ECO:0000255|HAMAP-Rule:MF_01217};
    Short=ACP {ECO:0000255|HAMAP-Rule:MF_01217};'
  gene_info: Name=acpP {ECO:0000255|HAMAP-Rule:MF_01217}; OrderedLocusNames=PP_1915;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the acyl carrier protein (ACP) family.
  protein_domains: ACP. (IPR003231); ACP-like_sf. (IPR036736); PP-bd_ACP. (IPR009081);
    Ppantetheine_attach_site. (IPR006162); PP-binding (PF00550)
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
citation_count: 23
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: acpP-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: acpP-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88LL5
- **Protein Description:** RecName: Full=Acyl carrier protein {ECO:0000255|HAMAP-Rule:MF_01217}; Short=ACP {ECO:0000255|HAMAP-Rule:MF_01217};
- **Gene Information:** Name=acpP {ECO:0000255|HAMAP-Rule:MF_01217}; OrderedLocusNames=PP_1915;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the acyl carrier protein (ACP) family.
- **Key Domains:** ACP. (IPR003231); ACP-like_sf. (IPR036736); PP-bd_ACP. (IPR009081); Ppantetheine_attach_site. (IPR006162); PP-binding (PF00550)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "acpP" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'acpP' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **acpP** (gene ID: acpP, UniProt: Q88LL5) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *acpP* (Acyl Carrier Protein) in *Pseudomonas putida* KT2440

**Gene:** *acpP* | **Ordered Locus:** PP_1915 | **UniProt:** Q88LL5
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / KT2440) — PSEPK
**Protein family:** Acyl carrier protein (ACP) family — HAMAP-Rule MF_01217
**Key domains:** ACP (IPR003231); ACP-like superfamily (IPR036736); PP-binding ACP (IPR009081); phosphopantetheine attachment site (IPR006162); PF00550

---

## Summary

The gene *acpP* (PP_1915, UniProt Q88LL5) of *Pseudomonas putida* KT2440 encodes the **acyl carrier protein (ACP)** — the small (~9 kDa), highly acidic, soluble cytoplasmic protein that sits at the mechanistic heart of type II (dissociated) fatty acid biosynthesis (FAS II). Gene-symbol and organism verification is unambiguous here: the UniProt annotation (HAMAP-Rule MF_01217) assigns Q88LL5 to the ACP family, the domain architecture (phosphopantetheine attachment site IPR006162; PF00550) is the canonical ACP signature, and the surrounding *P. putida* KT2440 fatty-acid/PHA literature is directly applicable. AcpP is not itself a catalytic enzyme; it is a **carrier/adapter protein** that covalently tethers every acyl intermediate of fatty-acid synthesis as a thioester and physically shuttles those intermediates between the successive, freestanding enzymes of the FAS II cycle.

To become functional, AcpP must undergo an essential post-translational modification: a dedicated 4'-phosphopantetheinyl transferase (PPTase) transfers the 4'-phosphopantetheine (Ppant) prosthetic group from coenzyme A onto a conserved, invariant serine residue, converting inactive apo-ACP into active holo-ACP. The terminal thiol of this Ppant "swinging arm" is the attachment point for all acyl cargo. In *Pseudomonas aeruginosa* — the closest well-studied relative — a single PPTase, PcpS, performs this priming and is essential for growth, servicing both fatty-acid synthesis and siderophore metabolism; the same architecture is expected in *P. putida*.

Mechanistically, AcpP delivers its cargo through transient, highly dynamic protein–protein interactions (PPIs) that involve "chain-flipping" of the acyl group out of the ACP hydrophobic core and into the active site of each partner enzyme. A landmark 1.9 Å crystal structure of a cross-linked *E. coli* AcpP–FabA complex captured this recognition process in atomic detail. In *P. putida*, these AcpP-bound intermediates feed two physiologically important destinations: (1) canonical membrane phospholipid and lipid A synthesis via the FAS II elongation cycle (initiated by FabH1/FabH2, MadB, and FabB/FabF), and (2) a metabolically important branch into **medium-chain-length polyhydroxyalkanoate (mcl-PHA)** carbon-storage polymer, via the transacylase PhaG, which diverts (R)-3-hydroxyacyl-ACP intermediates directly out of FAS II. AcpP is essential for viability, and its interaction *strength* with partner enzymes has been shown, in *P. putida* itself, to govern acyl-chain-length selectivity.

---

## Gene/Protein Identity Verification

Before proceeding, the mandatory identity checks were satisfied:

| Verification step | Result |
|---|---|
| Gene symbol "acpP" matches protein description | ✅ Yes — UniProt RecName is "Acyl carrier protein" |
| Organism correct (*P. putida* KT2440) | ✅ Yes — OrderedLocusName PP_1915 is KT2440 |
| Protein family/domains align with literature | ✅ Yes — ACP family, Ppant attachment site (PF00550) match canonical ACP |
| Risk of same-symbol confusion | Low — "acpP" is the standard, near-universal bacterial ACP gene name; the ACP function is deeply conserved, so orthologous data (E. coli, P. aeruginosa) transfer with high confidence |

The gene is **not** ambiguous. "acpP" is the conserved gene name for the housekeeping FAS II acyl carrier protein throughout the γ-proteobacteria, and the mechanistic paradigm established for the *E. coli* ortholog applies directly to the *P. putida* protein, supplemented by *Pseudomonas*-specific studies.

---

## Key Findings

### Finding 1 — AcpP is the central acyl-shuttling cofactor of type II fatty-acid synthesis

AcpP (Q88LL5, PP_1915) is the **acyl carrier protein**, the small, highly acidic, soluble cytoplasmic protein that carries all acyl intermediates as thioesters throughout fatty-acid biosynthesis. UniProt annotation (HAMAP-Rule MF_01217) assigns Q88LL5 to the ACP family with the phosphopantetheine attachment site (IPR006162; PF00550). In type II (dissociated) FAS systems characteristic of bacteria, the individual enzymatic activities exist as separate, freestanding proteins rather than as domains of one megasynthase; ACP is the mobile hub that physically connects them by ferrying the growing acyl chain from one active site to the next.

The mechanistic paradigm is firmly established for the orthologous *E. coli* AcpP, which "transports the growing fatty acid chain between enzymatic domains of fatty acid synthase (FAS) during biosynthesis" ([PMID: 24362570](https://pubmed.ncbi.nlm.nih.gov/24362570/)). This carrier function is not organism-specific but universal: ACP "is a universal and highly conserved carrier of acyl intermediates during fatty acid biosynthesis" ([PMID: 19850612](https://pubmed.ncbi.nlm.nih.gov/19850612/)). The high degree of sequence and structural conservation of ACP — a four-helix bundle fold — across bacteria means the well-characterized *E. coli* and *Bacillus* data provide a reliable functional template for the *P. putida* protein.

**Interpretation:** AcpP is best classified functionally as a **carrier/adapter protein**, not an enzyme. It has no intrinsic catalytic activity; its "job" is molecular logistics — holding and delivering intermediates. This is the primary function requested by the research question.

### Finding 2 — AcpP must be 4'-phosphopantetheinylated on a conserved serine to become active

AcpP is synthesized as an inactive **apo-protein** and must be converted to the active **holo-form** by covalent attachment of the 4'-phosphopantetheine (Ppant) prosthetic group. This is catalyzed by a dedicated **4'-phosphopantetheinyl transferase (PPTase)**, which transfers the Ppant moiety from coenzyme A. As stated in the *Pseudomonas aeruginosa* PPTase study, carrier proteins "need to be primed with the 4'-phosphopantetheine moiety of coenzyme A by a dedicated phosphopantetheine transferase (PPTase)" ([PMID: 12381736](https://pubmed.ncbi.nlm.nih.gov/12381736/)). More precisely, PPTases "catalyze the transfer of the essential prosthetic group 4'-phosphopantetheine (4'-Ppant) from coenzyme A (CoA) to a highly conserved serine residue in all PCPs and ACPs" ([PMID: 15065855](https://pubmed.ncbi.nlm.nih.gov/15065855/)).

The modified serine corresponds to the invariant Asp-Ser-Leu motif at the N-terminal cap of helix II — the exact residue flagged by UniProt as the phosphopantetheine attachment site (IPR006162) for Q88LL5. The free terminal thiol (–SH) of the attached Ppant arm is the chemical handle onto which all acyl groups are esterified.

Critically for *Pseudomonas*, this activation is essential and is provided by a single PPTase. In *P. aeruginosa*, "PcpS is essential for growth of *P. aeruginosa*, and biochemical data indicate its association with both fatty acid synthesis and siderophore metabolism" ([PMID: 12381736](https://pubmed.ncbi.nlm.nih.gov/12381736/)). By close homology, *P. putida* is expected to carry an orthologous single Sfp-type PPTase that primes AcpP, making AcpP activation an essential, non-redundant step for viability.

**Interpretation:** The Ppant arm is the functional "business end" of AcpP. Without phosphopantetheinylation, AcpP cannot bind cargo, and FAS II halts — explaining why both the carrier and its activating PPTase are essential genes.

### Finding 3 — AcpP delivers intermediates via transient, dynamic PPIs and "chain-flipping"

AcpP does not simply diffuse its cargo into partner active sites; it engages each FAS II enzyme through specific, transient protein–protein interactions and a substrate-presentation mechanism known as chain-flipping. The definitive structural evidence comes from the 1.9 Å crystal structure of a cross-linked *E. coli* AcpP–FabA (β-hydroxyacyl-ACP dehydratase) complex, which showed that "the 4'-phosphopantetheine group of AcpP first binds an arginine-rich groove of FabA, then an AcpP helical conformational change locks AcpP and FabA in place" ([PMID: 24362570](https://pubmed.ncbi.nlm.nih.gov/24362570/)). In this two-step recognition, the acyl chain — normally sequestered inside ACP's hydrophobic four-helix core to protect the reactive thioester — is "flipped" out and threaded down a channel into the partner enzyme's active site.

This PPI-gated delivery is a general feature of the pathway. Ketosynthases (FabB/FabF), which catalyze carbon–carbon bond formation, require ACP-mediated substrate delivery through PPIs for catalysis ([PMID: 36187225](https://pubmed.ncbi.nlm.nih.gov/36187225/)). Because these interactions are electrostatically driven (acidic ACP surface docking to basic patches on partners), engineering efforts have specifically tuned the electrostatic term to redesign AcpP PPIs ([PMID: 37671411](https://pubmed.ncbi.nlm.nih.gov/37671411/)).

Most importantly, this principle has been demonstrated in *P. putida* itself. The β-ketoacyl-ACP reductase PpFabG4 exhibits chain-length selectivity that is governed not by an active-site pocket but by the strength of the enzyme–ACP interaction: "substrate preference arises instead from a weak enzyme-ACP interaction that is stabilized by medium acyl chains but not by short chains" ([PMID: 40891111](https://pubmed.ncbi.nlm.nih.gov/40891111/)). This shows that in *P. putida*, AcpP is not a passive tether — the affinity of the AcpP–enzyme complex is an active determinant of which substrates get processed.

**Interpretation:** AcpP encodes recognition information on its surface. The transient, tunable nature of AcpP–enzyme PPIs is what allows a single carrier to service ~8 different enzymatic steps in the correct order, and it provides a mechanism for controlling chain-length distribution in the *P. putida* fatty-acid/PHA network.

### Finding 4 — AcpP-bound intermediates feed both FAS II elongation and the mcl-PHA branch

In *P. putida* KT2440, AcpP is the substrate-bearing hub for a fatty-acid initiation and elongation network with characteristic *Pseudomonas* features, and it also serves as the branch point to carbon-storage polymer synthesis.

**Initiation.** *P. putida* KT2440 uses multiple redundant routes to prime FAS, all acting on ACP-linked substrates: "Pseudomonas putida KT2440 contains three distinct pathways to initiate fatty acid biosynthesis" — via the β-ketoacyl-ACP synthase III enzymes FabH1 and FabH2 and the malonyl-ACP decarboxylase MadB ([PMID: 36796578](https://pubmed.ncbi.nlm.nih.gov/36796578/)). In addition, FabB participates in *Pseudomonas* initiation: "P. putida FabB decarboxylates malonyl-ACP and condenses the acetyl-ACP product with malonyl-ACP for initiation of FAS" ([PMID: 38335573](https://pubmed.ncbi.nlm.nih.gov/38335573/)). The unsaturated-fatty-acid pathway further involves a cryptic long-chain 3-ketoacyl-ACP synthase (FabF2) that can functionally replace FabB when derepressed ([PMID: 34181948](https://pubmed.ncbi.nlm.nih.gov/34181948/)).

**Elongation.** Each round of the elongation cycle acts on ACP-thioester intermediates: condensation (FabB/FabF), reduction (FabG), dehydration (FabA/FabZ), and enoyl reduction (FabI), regenerating a two-carbon-extended acyl-ACP for the next cycle.

**Branch to PHA storage.** A defining feature of *Pseudomonas* metabolism is the diversion of FAS II intermediates into medium-chain-length polyhydroxyalkanoates. This is mediated by PhaG, an "(R)-3-hydroxydecanoyl-ACP:CoA transacylase in Pseudomonas putida, which directly links the fatty acid de novo biosynthesis and polyhydroxyalkanoate (PHA) biosynthesis" ([PMID: 10713430](https://pubmed.ncbi.nlm.nih.gov/10713430/)). PhaG intercepts AcpP-bound (R)-3-hydroxyacyl intermediates (notably 3-hydroxydecanoyl-ACP) and transfers them to CoA, feeding the PHA polymerase. This link has been exploited in lignin-consolidated bioprocessing and syngas-derived polymer production ([PMID: 30030226](https://pubmed.ncbi.nlm.nih.gov/30030226/); [PMID: 27520812](https://pubmed.ncbi.nlm.nih.gov/27520812/)), and phaG orthologs are widespread among *Pseudomonas* and *Burkholderia* ([PMID: 15859323](https://pubmed.ncbi.nlm.nih.gov/15859323/)).

**Interpretation:** AcpP is the metabolic nexus where central carbon (acetyl-CoA/malonyl-CoA) is committed to both membrane lipid synthesis and PHA storage polymer. Its 3-hydroxyacyl intermediates are the precise chemical bridge to mcl-PHA — the trait that makes *P. putida* an important industrial biopolymer producer.

---

## Mechanistic Model / Interpretation

AcpP functions as a mobile, prosthetic-group-bearing shuttle. The following model integrates the four findings:

```
                    apo-AcpP (inactive)
                         |
        PPTase (e.g. PcpS ortholog) + CoA   [ESSENTIAL priming]
                         |  transfers 4'-phosphopantetheine
                         v  onto conserved Ser (helix II N-cap)
                    holo-AcpP  ==Ppant-SH   (active carrier)
                         |
            acetyl / malonyl loaded onto Ppant thiol
                         |
   +---------------------+-------------------------------------------+
   |            FAS II ELONGATION CYCLE (cytoplasm)                  |
   |                                                                 |
   |  Initiation:  FabH1/FabH2, MadB, FabB   (act on X-ACP)          |
   |       |                                                         |
   |       v                                                         |
   |  [1] Condensation      FabB / FabF  -- acyl-ACP + malonyl-ACP   |
   |       v                                                         |
   |  [2] Reduction         FabG        -- 3-ketoacyl-ACP            |
   |       v                (PpFabG4: chain length gated by          |
   |  [3] Dehydration       FabA / FabZ    ACP-interaction strength) |
   |       v                                                         |
   |  [4] Enoyl reduction   FabI        -- trans-2-enoyl-ACP         |
   |       |                                                         |
   |       +------> elongated acyl-ACP (loop back to [1])            |
   +--------+----------------------------------+---------------------+
            |                                  |
            v                                  v
   Membrane phospholipids /          (R)-3-hydroxyacyl-ACP
   lipid A (cell envelope)                     |
                                      PhaG transacylase
                                               | (ACP -> CoA)
                                               v
                                    (R)-3-hydroxyacyl-CoA
                                               | PhaC polymerase
                                               v
                                     mcl-PHA storage granule
```

Every arrow labeled "-ACP" is a step in which AcpP physically presents cargo to a partner enzyme via a transient, chain-flipping PPI. The recognition is largely electrostatic (acidic AcpP surface ↔ basic enzyme grooves), and — critically in *P. putida* — the *affinity* of the complex can itself select substrate chain length (Finding 3, PpFabG4). The pathway terminates in two fates: incorporation into membrane phospholipids and lipid A (the housekeeping role that makes AcpP essential), or diversion by PhaG into mcl-PHA carbon-storage polymer (the industrially prized role).

### Subcellular localization

AcpP is a **soluble cytoplasmic protein**. All FAS II enzymatic partners are likewise cytoplasmic (though the final acyltransferase steps that consume acyl-ACP for phospholipid synthesis, e.g., PlsB/PlsC/PlsX-type reactions, act at the inner face of the cytoplasmic membrane). Thus AcpP carries out its carrier function in the cytoplasm, delivering its final products toward the inner membrane for envelope assembly and to cytoplasmic PhaG for polymer synthesis.

### Functional classification summary

| Question posed | Answer for AcpP (Q88LL5) |
|---|---|
| Enzyme, transporter, structural, or signaling? | **Carrier/adapter protein** (intracellular acyl shuttle) — not catalytic |
| Reaction catalyzed | None intrinsically; it is a substrate-presenting cofactor |
| "Substrate" carried | All FAS II acyl intermediates (acetyl-, malonyl-, 3-keto-, 3-hydroxy-, enoyl-, saturated/unsaturated acyl-), as thioesters on the Ppant arm |
| Essential prosthetic group | 4'-phosphopantetheine (from CoA), attached to conserved Ser by a PPTase |
| Localization | Soluble cytoplasm (products delivered toward inner membrane) |
| Pathways | FAS II (membrane phospholipid / lipid A synthesis); mcl-PHA biosynthesis (via PhaG) |
| Essentiality | Essential for growth (as is its activating PPTase) |

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports the findings |
|---|---|---|
| [24362570](https://pubmed.ncbi.nlm.nih.gov/24362570/) | *Trapping the dynamic acyl carrier protein in fatty acid biosynthesis* | Defines AcpP's transport function and provides the 1.9 Å AcpP–FabA structure showing Ppant→arginine groove binding + helical locking (Findings 1, 3) |
| [19850612](https://pubmed.ncbi.nlm.nih.gov/19850612/) | *…acyl carrier protein in Bacillus subtilis* | Establishes ACP as a universal, highly conserved carrier of acyl intermediates (Finding 1) |
| [12381736](https://pubmed.ncbi.nlm.nih.gov/12381736/) | *A new type of phosphopantetheinyl transferase…in P. aeruginosa* | Carrier proteins must be Ppant-primed by a PPTase; PcpS is essential and links FAS to siderophore metabolism in *Pseudomonas* (Finding 2) |
| [15065855](https://pubmed.ncbi.nlm.nih.gov/15065855/) | *Structure-based analysis of PPTase Sfp* | Defines the exact chemistry: Ppant transfer from CoA to a conserved serine in all ACPs/PCPs (Finding 2) |
| [36187225](https://pubmed.ncbi.nlm.nih.gov/36187225/) | *Gating mechanism of elongating ketosynthases* | Ketosynthases require ACP-mediated substrate delivery through PPIs (Finding 3) |
| [37671411](https://pubmed.ncbi.nlm.nih.gov/37671411/) | *Interface engineering of carrier-protein pathways* | AcpP PPIs are electrostatically driven and can be redesigned (Finding 3) |
| [40891111](https://pubmed.ncbi.nlm.nih.gov/40891111/) | *Protein–protein complex stability controls substrate scope in a β-ketoacyl-ACP reductase* | *P. putida*-specific: PpFabG4 chain-length preference set by AcpP-interaction strength (Finding 3) |
| [36796578](https://pubmed.ncbi.nlm.nih.gov/36796578/) | *Initiation of fatty acid biosynthesis in P. putida KT2440* | Three initiation routes (FabH1, FabH2, MadB) act on ACP-linked substrates in the exact target strain (Finding 4) |
| [38335573](https://pubmed.ncbi.nlm.nih.gov/38335573/) | *FabB initiates FAS in P. putida F1* | FabB decarboxylates malonyl-ACP and condenses acetyl-ACP for initiation (Finding 4) |
| [34181948](https://pubmed.ncbi.nlm.nih.gov/34181948/) | *Cryptic long-chain 3-ketoacyl-ACP synthase (FabF2)* | FabF2 can replace FabB in UFA synthesis when derepressed (Finding 4 context) |
| [10713430](https://pubmed.ncbi.nlm.nih.gov/10713430/) | *phaG gene product in P. aeruginosa* | PhaG is the (R)-3-hydroxyacyl-ACP:CoA transacylase linking FAS to PHA (Finding 4) |
| [15859323](https://pubmed.ncbi.nlm.nih.gov/15859323/) | *Identification of phaG from Pseudomonas/Burkholderia* | phaG-mediated mcl-PHA route is widespread (Finding 4 context) |
| [30030226](https://pubmed.ncbi.nlm.nih.gov/30030226/) | *PHA production from lignin derivative* | Applied context for the FAS→PHA link in *Pseudomonas* (Finding 4 context) |

Additional supporting/contextual literature reviewed includes studies on ACP–PKS chimeras ([PMID: 35073057](https://pubmed.ncbi.nlm.nih.gov/35073057/)), unsaturation control in carrier-protein pathways ([PMID: 35255690](https://pubmed.ncbi.nlm.nih.gov/35255690/)), PPTase substrate specificity and carrier-protein recognition ([PMID: 15248752](https://pubmed.ncbi.nlm.nih.gov/15248752/), [PMID: 12127488](https://pubmed.ncbi.nlm.nih.gov/12127488/), [PMID: 25785780](https://pubmed.ncbi.nlm.nih.gov/25785780/), [PMID: 35337986](https://pubmed.ncbi.nlm.nih.gov/35337986/)), the role of Ppant as a "swinging arm" activating multidomain enzymes ([PMID: 19933275](https://pubmed.ncbi.nlm.nih.gov/19933275/)), ACP conformational/aggregation behavior ([PMID: 33667556](https://pubmed.ncbi.nlm.nih.gov/33667556/)), and FabH/FabD ACP-specificity in *Streptomyces* ([PMID: 12173933](https://pubmed.ncbi.nlm.nih.gov/12173933/)).

### Consistency and independent lines of evidence

The functional assignment rests on multiple, mutually reinforcing lines of evidence:

1. **Sequence/domain (bioinformatic):** Canonical ACP domain and Ppant attachment site (UniProt/InterPro/HAMAP).
2. **Structural:** Atomic-resolution AcpP–FabA complex (E. coli ortholog) directly visualizing the shuttle mechanism.
3. **Biochemical:** Defined PPTase-catalyzed activation chemistry; ACP substrate use by FAS II enzymes.
4. **Genetic/physiological:** Essentiality of the Pseudomonas PPTase; multiple ACP-dependent initiation routes in KT2440.
5. **Organism-specific:** PpFabG4 and FabB/FabF2 studies performed in *P. putida* itself, plus the PhaG FAS→PHA link.

The convergence across evolution, structure, biochemistry, and *P. putida*-specific genetics gives high confidence in the annotation.

---

## Limitations and Knowledge Gaps

1. **No direct structural or biochemical study of Q88LL5 itself.** The functional assignment for the specific *P. putida* KT2440 protein is inferred from (a) its unambiguous domain signature and (b) exceptionally strong orthology to characterized ACPs (E. coli AcpP, P. aeruginosa system). No published crystal structure, NMR structure, or direct enzymatic partner-binding study of PP_1915 was identified. Given ACP's deep conservation, this inference is robust, but strictly it remains inference rather than direct measurement.

2. **The activating PPTase in *P. putida* is inferred, not experimentally confirmed here.** The essential single-PPTase model is established for *P. aeruginosa* (PcpS). The orthologous *P. putida* PPTase and its essentiality were not directly verified in this investigation.

3. **Quantitative flux partitioning between membrane lipids and PHA is not resolved.** While PhaG is established as the FAS→PHA conduit, the precise conditions and regulatory logic that partition AcpP-bound 3-hydroxyacyl intermediates between phospholipid synthesis and PHA storage in KT2440 remain incompletely mapped.

4. **Chain-length control generalization.** The elegant "interaction-strength selects chain length" mechanism was demonstrated for PpFabG4; whether the same principle quantitatively governs other *P. putida* FAS II partners (FabA/FabZ, FabB/FabF, PhaG) is not established.

5. **No experimental data files were analyzed.** This is a literature/annotation-based functional report; no primary datasets (e.g., omics, structures) specific to Q88LL5 were available for independent statistical analysis.

---

## Proposed Follow-up Experiments / Actions

1. **Directly confirm holo-ACP formation for PP_1915.** Express recombinant apo-AcpP (Q88LL5), incubate with the candidate *P. putida* PPTase + CoA, and confirm holo-ACP by intact-mass MS / conformationally sensitive urea-PAGE band shift. This would experimentally validate Finding 2 for the specific protein.

2. **Identify and test essentiality of the *P. putida* PPTase.** Use bioinformatics to identify the PcpS ortholog in KT2440, then attempt a conditional knockout / CRISPRi knockdown to confirm essentiality and its coupling to FAS (and siderophore) metabolism.

3. **Solve or model the AcpP structure and map partner interfaces.** Obtain an NMR/crystal structure of *P. putida* AcpP (or a high-confidence AlphaFold model with validation) and use crosslinking-MS or SPR to quantify AcpP affinities for FabG4, FabA/FabZ, FabB/FabF, and PhaG — testing whether interaction strength systematically tracks chain-length selectivity beyond FabG4.

4. **Trace flux partitioning at the AcpP node.** Use ¹³C metabolic-flux analysis under growth vs. PHA-accumulation conditions to quantify how AcpP-bound 3-hydroxyacyl intermediates are split between phospholipid synthesis and PhaG-mediated PHA formation.

5. **Engineer AcpP PPIs for bioproduction.** Building on the electrostatic-interface engineering framework ([PMID: 37671411](https://pubmed.ncbi.nlm.nih.gov/37671411/)), rationally tune AcpP–PhaG or AcpP–FabG interfaces to shift mcl-PHA monomer chain-length distributions, testing AcpP as a control point for tailored biopolymer properties.

---

*Report generated from an autonomous literature-and-annotation investigation (1 iteration; 4 confirmed findings; 23 papers reviewed). All functional claims are attributed to the cited literature; where the specific P. putida protein has not been directly studied, assignments are explicitly flagged as orthology-based inference.*


## Artifacts

- [OpenScientist final report](acpP-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](acpP-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:24362570
2. PMID:19850612
3. PMID:12381736
4. PMID:15065855
5. PMID:36187225
6. PMID:37671411
7. PMID:40891111
8. PMID:36796578
9. PMID:38335573
10. PMID:34181948
11. PMID:10713430
12. PMID:30030226
13. PMID:27520812
14. PMID:15859323
15. PMID:35073057
16. PMID:35255690
17. PMID:15248752
18. PMID:12127488
19. PMID:25785780
20. PMID:35337986
21. PMID:19933275
22. PMID:33667556
23. PMID:12173933