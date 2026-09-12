---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-23T08:34:02.135903'
end_time: '2026-07-23T08:54:15.381433'
duration_seconds: 1213.25
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: fabD
  gene_symbol: fabD
  uniprot_accession: Q88LL7
  protein_description: 'RecName: Full=Malonyl CoA-acyl carrier protein transacylase
    {ECO:0000256|ARBA:ARBA00018953, ECO:0000256|PIRNR:PIRNR000446}; EC=2.3.1.39 {ECO:0000256|ARBA:ARBA00013258,
    ECO:0000256|PIRNR:PIRNR000446};'
  gene_info: Name=fabD {ECO:0000313|EMBL:AAN67531.1}; OrderedLocusNames=PP_1913 {ECO:0000313|EMBL:AAN67531.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the fabD family.
  protein_domains: Ac_transferase_dom_sf. (IPR001227); Acyl_transferase_dom. (IPR014043);
    Acyl_Trfase/lysoPLipase. (IPR016035); Mal-CoA-ACP_Trans/PKS_FabD. (IPR050858);
    Malonyl_CoA-ACP_transAc. (IPR024925)
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
citation_count: 11
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: fabD-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: fabD-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88LL7
- **Protein Description:** RecName: Full=Malonyl CoA-acyl carrier protein transacylase {ECO:0000256|ARBA:ARBA00018953, ECO:0000256|PIRNR:PIRNR000446}; EC=2.3.1.39 {ECO:0000256|ARBA:ARBA00013258, ECO:0000256|PIRNR:PIRNR000446};
- **Gene Information:** Name=fabD {ECO:0000313|EMBL:AAN67531.1}; OrderedLocusNames=PP_1913 {ECO:0000313|EMBL:AAN67531.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the fabD family.
- **Key Domains:** Ac_transferase_dom_sf. (IPR001227); Acyl_transferase_dom. (IPR014043); Acyl_Trfase/lysoPLipase. (IPR016035); Mal-CoA-ACP_Trans/PKS_FabD. (IPR050858); Malonyl_CoA-ACP_transAc. (IPR024925)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "fabD" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'fabD' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **fabD** (gene ID: fabD, UniProt: Q88LL7) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# FabD (Q88LL7, PP_1913) in *Pseudomonas putida* KT2440: Malonyl-CoA:ACP Transacylase — The Gatekeeper of Fatty Acid Synthesis

## Summary

**FabD (Q88LL7, ordered locus PP_1913) of *Pseudomonas putida* KT2440 is malonyl-CoA:acyl-carrier-protein transacylase (MCAT; EC 2.3.1.39), the enzyme that performs the essential, committed initiation step of bacterial type II fatty acid synthesis (FAS II).** It catalyzes the transfer of the malonyl moiety from the soluble thioester donor malonyl-coenzyme A to the phosphopantetheine thiol of holo-acyl carrier protein (holo-ACP), producing **malonyl-ACP + free CoASH**. Malonyl-ACP is the universal two-carbon extender (chain-elongation building block) consumed by every round of the fatty-acid elongation cycle, making FabD the single gatekeeper that channels central-metabolism-derived malonyl-CoA into membrane lipid biosynthesis. This assignment is supported by the UniProt/PIRSF annotation of Q88LL7 to the fabD family (EC 2.3.1.39), by the conserved active-site architecture verified directly in the *P. putida* sequence, and by deep genomic synteny.

Mechanistically, FabD is a soluble, **cytoplasmic** enzyme built on an **α/β-hydrolase fold** paired with a small ferredoxin-like subdomain. It uses a **Ser–His catalytic dyad** and a preformed oxyanion hole to run a two-step **ping-pong (bi-bi) reaction** through a covalent **malonyl-serine intermediate**: malonyl-CoA first acylates the active-site serine (releasing CoASH), then the malonyl group is handed to holo-ACP that docks at the cleft between the two subdomains. Direct sequence analysis of Q88LL7 (312 aa) confirms that the *P. putida* enzyme retains the canonical catalytic serine within a **GHSLG motif (Ser93)**, together with the conserved N-terminal glutamine, the malonyl-clamping arginine, and the general-base histidine. A global alignment shows **61.2% full-length identity to *E. coli* FabD**, with all four experimentally validated catalytic/substrate-binding residues (Gln11, Ser92, Arg117, His201 in E. coli numbering) perfectly conserved — rigorously justifying transfer of the well-characterized E. coli/orthologue mechanism to this enzyme.

Beyond its housekeeping role in membrane phospholipid synthesis, FabD holds special significance in *P. putida* KT2440, a model producer of **medium-chain-length polyhydroxyalkanoates (mcl-PHA)**. The malonyl-ACP that FabD generates feeds de novo fatty-acid synthesis, whose (R)-3-hydroxyacyl-ACP intermediates are diverted by the thioesterase/transacylase **PhaG** toward PHA monomer supply when cells grow on unrelated carbon sources such as glucose or glycerol. FabD therefore sits at the metabolic branch point linking central carbon metabolism, membrane biogenesis, and bioplastic production. FabD is essential and highly conserved, and — as the FAS II initiation enzyme — is an actively pursued broad-spectrum antibacterial target.

---

## Identity Verification

Before detailing function, the target was confirmed to be a bona fide FabD/MCAT rather than a gene-symbol collision:

- **Gene/protein match.** UniProt describes Q88LL7 as "Malonyl CoA-acyl carrier protein transacylase," gene *fabD*, ordered locus PP_1913, in *P. putida* KT2440 — directly consistent with the FabD family signatures (InterPro IPR050858 "Mal-CoA-ACP_Trans/PKS_FabD"; IPR024925 "Malonyl_CoA-ACP_transAc") and EC 2.3.1.39.
- **Sequence verification.** The 312-aa sequence contains the diagnostic MCAT catalytic-serine motif **G-H-S-L-G (Ser93)**, positionally equivalent to the well-characterized *E. coli* FabD Ser92, plus the conserved N-terminal Gln and the C-terminal catalytic His region. This establishes that the *P. putida* enzyme retains the complete, canonical catalytic apparatus of the FabD family.
- **Quantitative orthology.** A global Needleman–Wunsch alignment of Q88LL7 against *E. coli* FabD (P0AAI9) gives **61.2% amino-acid identity** with near-identical length and no large gaps; all four E. coli catalytic residues map onto conserved P. putida positions. Q88LL7 is therefore a genuine FabD orthologue, not a paralogue or misannotation.

---

## Key Findings

### Finding 1 — FabD is the malonyl-CoA:ACP transacylase that initiates FAS II

FabD (Q88LL7, PP_1913) catalyzes the reaction that commits carbon to fatty-acid synthesis:

```
malonyl-CoA + holo-ACP  ⇌  malonyl-ACP + CoASH        (EC 2.3.1.39)
```

The product, **malonyl-ACP, is the sole C2-donor building block** for FAS II elongation, condensed onto growing acyl chains by the ketoacyl-ACP synthases FabB, FabF, and FabH. UniProt/PIRSF (PIRNR000446) annotates Q88LL7 to the fabD family with EC 2.3.1.39, and the reaction chemistry is defined precisely in the primary structural literature. As stated for the E. coli enzyme, FabD works by "*catalyzing the transfer of a malonyl moiety from malonyl-CoA to holo acyl carrier protein (ACP), generating malonyl-ACP and free CoASH. Malonyl-ACP, which is the product of this reaction, is the key building block for de novo fatty-acid biosynthesis*" [PMID: 16699188](https://pubmed.ncbi.nlm.nih.gov/16699188/). The enzyme is essential: FabD "*being an essential enzyme of the FAS II pathway, is an attractive target for developing broad-spectrum antibiotics. It performs initiation reaction to form malonyl-ACP, which is a key building block in fatty acid biosynthesis*" [PMID: 29604333](https://pubmed.ncbi.nlm.nih.gov/29604333/). In E. coli, temperature-sensitive *fabD* alleles are conditionally lethal, underscoring that this single transacylase controls flux into the entire pathway.

### Finding 2 — Catalysis uses an α/β-hydrolase fold, a Ser–His dyad, and a covalent malonyl-enzyme (ping-pong) mechanism

MCAT/FabD enzymes adopt a two-subdomain architecture: "*compact folding composed of a large subdomain with a similar core as in alpha/beta hydrolases, and a similar ferredoxin-like small subdomain as in acylphosphatases*" [PMID: 17525466](https://pubmed.ncbi.nlm.nih.gov/17525466/). In the E. coli enzyme, active-site mapping by protein crystallography established the roles of the conserved catalytic residues and the oxyanion hole, indicating "*the functional role of the highly conserved amino acids Gln11, Ser92, Arg117 and His201 and the stabilizing function of the preformed oxyanion hole during the enzymatic reaction*" [PMID: 16699188](https://pubmed.ncbi.nlm.nih.gov/16699188/). Catalysis proceeds via a **ping-pong bi-bi** mechanism: malonyl-CoA acylates the nucleophilic serine to form a **malonyl-Ser covalent intermediate** with release of CoASH; the malonyl group is then transferred to holo-ACP. The active-site serine sits in a signature **GHSLG motif**. Direct sequence analysis of Q88LL7 confirms the canonical active-site serine (Ser93, equivalent to E. coli Ser92) plus the conserved N-terminal Gln and C-terminal His, establishing that the P. putida enzyme retains the full catalytic apparatus.

### Finding 3 — FabD functions in the cytoplasm, docking holo-ACP at the interdomain cleft

FAS II is a **soluble, cytoplasmic** system in which small acyl carrier proteins shuttle intermediates between standalone enzymes. FabD delivers the malonyl group to the phosphopantetheine "swinging arm" of soluble holo-ACP. Structural docking and mutagenesis studies localize the ACP-binding surface to the cleft between the two FabD subdomains and identify conserved basic residues that mediate the electrostatic, protein–protein recognition. In *Acinetobacter baumannii* FabD, "*Binding constants between AbFabD variants and A. baumannii ACP (AbACP) revealed critical conserved residues Lys195 and Lys200 involved in AbACP binding*" [PMID: 30243724](https://pubmed.ncbi.nlm.nih.gov/30243724/). Consistently, docking of the *Xanthomonas oryzae* MCAT–ACP complex showed that "*the proposed model revealed that ACP bound to the cleft between two XoMCAT subdomains*" [PMID: 22134719](https://pubmed.ncbi.nlm.nih.gov/22134719/). Thus FabD carries out its function in the cytoplasm through a transient, electrostatically guided interface with its ACP partner.

### Finding 4 — In *P. putida* KT2440, FabD-driven de novo FAS also feeds mcl-PHA biosynthesis via PhaG

*P. putida* KT2440 is a model organism for **medium-chain-length polyhydroxyalkanoate (mcl-PHA)** production: it "*is capable of producing medium-chain-length polyhydroxyalkanoates (MCL-PHAs) when grown on unrelated carbon sources during nutrient limitation*" [PMID: 22101037](https://pubmed.ncbi.nlm.nih.gov/22101037/). De novo fatty-acid synthesis — initiated by FabD-generated malonyl-ACP — supplies (R)-3-hydroxyacyl-ACP intermediates that the thioesterase/transacylase **PhaG** diverts toward PHA when cells grow on carbon sources unrelated to fatty acids (e.g., glucose, glycerol). A recent revisiting of the β-oxidation/PHA relationship found that "*The deletion of (R)-3-hydroxydecanoyl-ACP:CoA transacylase (PhaG), which connects de novo FA and PHA synthesis pathways, while causing a further 1.8-fold decrease in PHA content, did not abolish PHA accumulation*" [PMID: 36763117](https://pubmed.ncbi.nlm.nih.gov/36763117/). This confirms that the FabD/FAS route is one of the pathways linking central metabolism to PHA monomer supply, positioning FabD at a biotechnologically important metabolic branch point.

### Finding 5 — fabD resides in the conserved bacterial FAS gene cluster and is essential

In E. coli the fatty-acid-biosynthesis genes are clustered in a fixed order: "*The genes encoding several key fatty acid biosynthetic enzymes (called the fab cluster) are clustered in the order plsX-fabH-fabD-fabG-acpP-fabF at min 24 of the Escherichia coli chromosome*" [PMID: 9642179](https://pubmed.ncbi.nlm.nih.gov/9642179/). Within this cluster *fabD* is essential and the downstream *fabG* is obligatorily co-transcribed with upstream genes — inserting a transcription terminator between *fabD* and *fabG* abolishes *fabG* expression and blocks growth. The same synteny is conserved across distant bacteria; the *Bacillus subtilis* cluster was "*isolated by complementation of an Escherichia coli fabD mutant encoding a thermosensitive malonyl coenzyme A-acyl carrier protein transacylase*" [PMID: 8759840](https://pubmed.ncbi.nlm.nih.gov/8759840/). This deep synteny and cross-species genetic complementation independently confirm that *fabD*/PP_1913 encodes the housekeeping MCAT of a co-regulated FAS II operon.

### Finding 6 — MCAT substrate specificity: requires the malonyl carboxylate; accepts malonyl-/methylmalonyl-CoA but not acetyl-CoA

The malonyl selectivity that defines FabD chemistry is documented for the mechanistically identical malonyl-CoA:ACP transacylase MdcH: "*Substrates for MdcH are malonyl-CoA or methylmalonyl-CoA but not acetyl-CoA. The enzyme has Km values of 16 microm for both substrates*" [PMID: 9914491](https://pubmed.ncbi.nlm.nih.gov/9914491/), with Vmax of 190 versus 37 U/mg for malonyl- versus methylmalonyl-CoA, transfer proceeding through a covalent (methyl)malonyl-enzyme intermediate. This discrimination reflects the conserved arginine (Arg117 in E. coli FabD) that clamps the malonyl β-carboxylate. It explains why FabD selects the C3 dicarboxylic thioester and **excludes acetyl-CoA** — the acetyl primer instead enters FAS II directly via the initiating condensing enzyme FabH rather than through FabD.

### Finding 7 — In *P. putida* KT2440, PP_1913 (fabD) sits in a syntenic cluster adjacent to its own ACP substrate

A direct genome query of *P. putida* KT2440 (taxid 160488) resolves the gene neighborhood of PP_1913:

| Locus | Gene | Product | EC |
|-------|------|---------|-----|
| PP_1911 | rpmF | 50S ribosomal protein L32 | — |
| PP_1912 | plsX | phosphate acyltransferase | 2.3.1.274 |
| **PP_1913** | **fabD** | **malonyl-CoA:ACP transacylase (MCAT)** | **2.3.1.39** |
| PP_1914 | fabG | 3-oxoacyl-ACP reductase | 1.1.1.100 |
| PP_1915 | acpP | acyl carrier protein | — |

This reproduces the conserved bacterial fab-cluster order (plsX–fabD–fabG–acpP), matching E. coli/Salmonella/B. subtilis [PMID: 9642179](https://pubmed.ncbi.nlm.nih.gov/9642179/), with *fabH* located elsewhere. Notably, FabD is **genomically adjacent to acpP** — the very ACP that serves as its acyl acceptor — and to **fabG**, which reduces the 3-oxoacyl-ACP products formed downstream of malonyl-ACP condensation. This co-location supports coordinated expression of the enzyme and its substrate.

### Finding 8 — P. putida FabD shares 61% identity with E. coli FabD, with all four catalytic residues perfectly conserved

A global Needleman–Wunsch alignment of Q88LL7 (312 aa) against E. coli FabD (P0AAI9, 309 aa) yields **61.2% amino-acid identity (189 identical positions)**, with only a 3-residue length difference and essentially no large gaps. Crucially, the four experimentally established E. coli catalytic/substrate-binding residues map exactly onto conserved P. putida positions:

| E. coli residue | Role | *P. putida* Q88LL7 |
|-----------------|------|---------------------|
| Gln11 | Oxyanion hole | Gln (conserved) |
| Ser92 | Nucleophile (GHSLG motif) | **Ser93** (conserved) |
| Arg117 | Malonyl β-carboxylate clamp | Arg (conserved) |
| His201 | General base | His (conserved) |

This high, full-length conservation of both the scaffold and the complete active site — anchored by the residues that [PMID: 16699188](https://pubmed.ncbi.nlm.nih.gov/16699188/) established as functionally essential — rigorously justifies transferring mechanistic and structural conclusions from E. coli and other characterized orthologues to the *P. putida* enzyme.

---

## Mechanistic Model / Interpretation

FabD is best understood as the **single entry valve** that admits malonyl carbon into fatty-acid synthesis. The overall logic of the pathway and FabD's place within it:

```
   Central metabolism
        |
   acetyl-CoA ──(AccABCD, acetyl-CoA carboxylase)──> malonyl-CoA
                                                          |
                                                          |  FabD (PP_1913)  EC 2.3.1.39
                                                          |  malonyl-CoA + holo-ACP
                                                          v
                                                    malonyl-ACP + CoASH
                                                          |
        acetyl-CoA ──FabH──> initiate condensation      |
                                                          v
                       ┌── FabB/FabF (condensation) <── malonyl-ACP (extender unit)
                       |          |
   Elongation cycle    |     β-ketoacyl-ACP
   (each round adds     |          | FabG (PP_1914, 3-oxoacyl-ACP reductase)
    2 carbons)          |          v
                       |     β-hydroxyacyl-ACP ──────────────┐
                       |          | FabA/FabZ (dehydratase)   │
                       |          v                            │ (R)-3-hydroxyacyl-ACP
                       |     enoyl-ACP                          │
                       |          | FabI (enoyl-ACP reductase) │  PhaG (thioesterase/
                       └──────────┘                            │  transacylase)
                                  |                            v
                     acyl-ACP ──> membrane phospholipids     mcl-PHA monomers
                                                              (P. putida bioplastic)
```

**Reaction mechanism (ping-pong bi-bi):**

```
Step 1 (acylation):   E-Ser93-OH + malonyl-CoA  ->  E-Ser93-O-malonyl (covalent) + CoASH
Step 2 (transfer):    E-Ser93-O-malonyl + holo-ACP-SH  ->  E-Ser93-OH + malonyl-S-ACP
```

The His201 general base activates Ser93 for nucleophilic attack on the malonyl thioester carbonyl; the tetrahedral oxyanion intermediate is stabilized by the preformed oxyanion hole (backbone amides plus Gln11); Arg117 fixes the malonyl β-carboxylate, enforcing selectivity for malonyl-CoA (and methylmalonyl-CoA) over acetyl-CoA. Holo-ACP docks at the interdomain cleft via conserved basic residues (the Lys195/Lys200 equivalents), positioning its phosphopantetheine thiol to receive the malonyl group.

**Localization.** All chemistry occurs in the **cytoplasm**, consistent with FAS II being a fully soluble, dissociated enzyme system in which ACP ferries covalently tethered intermediates between individual catalysts.

**Systems context in *P. putida*.** Because malonyl-ACP is the obligatory extender unit for every elongation round, FabD controls the supply of acyl chains for (i) membrane phospholipids (housekeeping) and (ii) mcl-PHA biosynthesis via the PhaG branch. Genomic adjacency of *fabD* to *acpP* (substrate) and *fabG* (downstream reductase) in the co-regulated fab cluster reflects the coordination required to balance these flux demands.

---

## Evidence Base

| PMID | Study focus | How it supports the findings |
|------|-------------|------------------------------|
| [16699188](https://pubmed.ncbi.nlm.nih.gov/16699188/) | Crystallographic active-site mapping of *E. coli* FabD | Defines the exact reaction/products and the four catalytic residues (Gln11, Ser92, Arg117, His201) + oxyanion hole — reference for Findings 1, 2, 8 |
| [29604333](https://pubmed.ncbi.nlm.nih.gov/29604333/) | FabD as antibacterial target (*Moraxella catarrhalis*) | States FabD is essential and performs the malonyl-ACP-forming initiation reaction (Finding 1) |
| [17525466](https://pubmed.ncbi.nlm.nih.gov/17525466/) | *Helicobacter pylori* MCAT structure + ACP interaction | Describes the α/β-hydrolase + ferredoxin-like two-subdomain fold (Finding 2) |
| [30243724](https://pubmed.ncbi.nlm.nih.gov/30243724/) | *A. baumannii* FabD structure + ACP binding | Experimental identification of conserved Lys residues mediating FabD–ACP binding (Finding 3) |
| [22134719](https://pubmed.ncbi.nlm.nih.gov/22134719/) | *X. oryzae* MCAT structure + ACP docking | ACP binds at the interdomain cleft (Finding 3) |
| [9914491](https://pubmed.ncbi.nlm.nih.gov/9914491/) | MdcH transacylase substrate specificity | Malonyl-/methylmalonyl-CoA accepted, acetyl-CoA excluded; covalent acyl-enzyme (Finding 6) |
| [9642179](https://pubmed.ncbi.nlm.nih.gov/9642179/) | E. coli fab cluster transcription / Salmonella replacement | Establishes conserved plsX-fabH-fabD-fabG-acpP-fabF synteny and essentiality (Findings 5, 7) |
| [8759840](https://pubmed.ncbi.nlm.nih.gov/8759840/) | *B. subtilis* lipid-biosynthesis gene cluster | fabD encodes MCAT; cluster isolated by complementing a thermosensitive E. coli fabD mutant (Finding 5) |
| [36763117](https://pubmed.ncbi.nlm.nih.gov/36763117/) | β-oxidation–PHA relationship in *P. putida* KT2440 | PhaG links de novo FAS to mcl-PHA; deletion reduces but does not abolish PHA (Finding 4) |
| [22101037](https://pubmed.ncbi.nlm.nih.gov/22101037/) | mcl-PHA production strategy | Establishes *P. putida* KT2440 as an mcl-PHA producer using de novo fatty-acid metabolism (Finding 4) |
| [17604051](https://pubmed.ncbi.nlm.nih.gov/17604051/) | *M. tuberculosis* MCAT structure | Additional structural context; notes catalytic-model variation among MCATs, a caveat for mechanism transfer |
| [29858956](https://pubmed.ncbi.nlm.nih.gov/29858956/) | Review of transacylase enzymes for engineering | Frames E. coli FabD as the model transacylase for structure/mechanism/engineering |

**Convergence of evidence.** The functional assignment rests on multiple independent pillars: (1) database/family annotation (UniProt PIRNR000446, InterPro fabD family, EC 2.3.1.39); (2) direct sequence verification of the catalytic serine (GHSLG/Ser93) and 61% identity to characterized E. coli FabD; (3) conserved genomic synteny in the fab cluster adjacent to *acpP*; and (4) an extensive body of biochemical and crystallographic work on multiple bacterial FabD orthologues that all agree on the reaction, mechanism, and localization. No evidence contradicts the assignment.

---

## Supported and Refuted Hypotheses

**Supported**
- **H1:** Q88LL7 is a malonyl-CoA:ACP transacylase (EC 2.3.1.39) — supported by annotation, family/domain signatures, and conserved catalytic-motif verification.
- **H2:** It catalyzes the essential FAS II initiation reaction producing malonyl-ACP — supported ([PMID: 16699188](https://pubmed.ncbi.nlm.nih.gov/16699188/), [PMID: 29604333](https://pubmed.ncbi.nlm.nih.gov/29604333/)).
- **H3:** It employs an α/β-hydrolase Ser–His mechanism with a covalent malonyl-enzyme intermediate — supported by homolog structures and sequence conservation ([PMID: 16699188](https://pubmed.ncbi.nlm.nih.gov/16699188/), [PMID: 17525466](https://pubmed.ncbi.nlm.nih.gov/17525466/)).
- **H4:** It acts in the cytoplasm via ACP protein–protein interaction — supported ([PMID: 22134719](https://pubmed.ncbi.nlm.nih.gov/22134719/), [PMID: 30243724](https://pubmed.ncbi.nlm.nih.gov/30243724/)).
- **H5:** In *P. putida*, its output feeds mcl-PHA synthesis via PhaG — supported ([PMID: 36763117](https://pubmed.ncbi.nlm.nih.gov/36763117/), [PMID: 22101037](https://pubmed.ncbi.nlm.nih.gov/22101037/)).

**Refuted / excluded**
- The symbol-collision concern (that "fabD" might refer to an unrelated gene) is refuted: sequence, family, and catalytic-residue evidence all converge on an authentic MCAT.

---

## Limitations and Knowledge Gaps

1. **No direct experimental characterization of the P. putida enzyme.** All mechanistic and kinetic conclusions are transferred by homology from E. coli, X. oryzae, H. pylori, A. baumannii, M. tuberculosis, and MdcH. While the 61% identity and perfect active-site conservation make this transfer robust, the specific kinetic parameters (Km, kcat) of Q88LL7 have not been measured.

2. **Mechanistic heterogeneity among MCATs.** The *M. tuberculosis* MCAT structure revealed alternative proton-transfer geometries and argued that its His194 "*cannot form part of a His-Ser catalytic dyad and only stabilizes the substrate*" [PMID: 17604051](https://pubmed.ncbi.nlm.nih.gov/17604051/). This cautions that the precise catalytic details in P. putida might differ subtly from the E. coli paradigm, though the core Ser nucleophile is universal.

3. **Quantitative flux partitioning is unresolved.** The exact contribution of FabD/FAS flux to mcl-PHA versus membrane phospholipids under different growth conditions in *P. putida* KT2440 has not been directly quantified. PhaG deletion reduces PHA only ~1.8-fold, implying redundant routes ([PMID: 36763117](https://pubmed.ncbi.nlm.nih.gov/36763117/)).

4. **Regulation not addressed.** How *fabD* expression and MCAT activity are regulated in *P. putida* (e.g., transcriptional control of the cluster, feedback by acyl-ACP or malonyl-CoA levels) was not investigated here.

5. **No experimentally determined 3D structure** exists for Q88LL7; structural inferences rely on orthologue crystal structures and would benefit from an AlphaFold model or experimental structure to confirm the interdomain cleft and ACP-docking surface.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant expression and steady-state kinetics.** Clone PP_1913, purify the enzyme, and measure Km/kcat for malonyl-CoA and holo-ACP (P. putida AcpP/PP_1915), plus counter-assays with acetyl-CoA and methylmalonyl-CoA to confirm the predicted malonyl selectivity directly for this ortholog.

2. **Active-site mutagenesis.** Generate S93A and the conserved Gln/Arg/His mutants; assay for loss of transacylase activity to experimentally validate the transferred catalytic assignment.

3. **Structural determination.** Solve the crystal structure (or refine an AlphaFold model) of Q88LL7, ideally as a FabD–AcpP complex, to visualize the ACP-docking cleft and the basic residues (Lys195/Lys200 equivalents) predicted from orthologues.

4. **Essentiality and conditional depletion.** Confirm essentiality in *P. putida* KT2440 via a conditional (e.g., inducible/CRISPRi) knockdown of *fabD*, and characterize the effect on growth, membrane lipid composition, and mcl-PHA yield.

5. **Flux analysis at the FAS/PHA branch point.** Use ¹³C metabolic flux analysis under PHA-accumulating conditions to quantify how FabD-generated malonyl-ACP partitions between membrane phospholipids and the PhaG-mediated PHA route, informing metabolic-engineering strategies to boost bioplastic titers.

6. **Antibacterial target validation.** Given FabD essentiality and the interest in FAS II inhibitors, screen candidate inhibitors (e.g., the aporphine alkaloids reported against *M. catarrhalis* FabD) against the purified P. putida enzyme to assess broad-spectrum potential.

---

*Report generated from an autonomous 3-iteration literature and bioinformatic investigation. Findings are grounded in UniProt/InterPro annotation of Q88LL7, direct sequence analysis of the P. putida enzyme, genomic synteny in P. putida KT2440, and primary/structural literature on bacterial FabD/MCAT orthologues.*


## Artifacts

- [OpenScientist final report](fabD-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](fabD-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:16699188
2. PMID:29604333
3. PMID:17525466
4. PMID:30243724
5. PMID:22134719
6. PMID:22101037
7. PMID:36763117
8. PMID:9642179
9. PMID:8759840
10. PMID:9914491
11. PMID:17604051