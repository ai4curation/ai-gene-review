---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T02:12:51.974130'
end_time: '2026-09-01T02:24:58.304771'
duration_seconds: 726.33
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: lolB
  gene_symbol: lolB
  uniprot_accession: Q88PX4
  protein_description: 'RecName: Full=Outer-membrane lipoprotein LolB {ECO:0000255|HAMAP-Rule:MF_00233};
    Flags: Precursor;'
  gene_info: Name=lolB {ECO:0000255|HAMAP-Rule:MF_00233}; OrderedLocusNames=PP_0724;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the LolB family. {ECO:0000255|HAMAP-
  protein_domains: LolA/LolB/LppX. (IPR029046); OM_lipoprot_LolB. (IPR004565); LolB
    (PF03550)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
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
  path: lolB-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: lolB-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88PX4
- **Protein Description:** RecName: Full=Outer-membrane lipoprotein LolB {ECO:0000255|HAMAP-Rule:MF_00233}; Flags: Precursor;
- **Gene Information:** Name=lolB {ECO:0000255|HAMAP-Rule:MF_00233}; OrderedLocusNames=PP_0724;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the LolB family. {ECO:0000255|HAMAP-
- **Key Domains:** LolA/LolB/LppX. (IPR029046); OM_lipoprot_LolB. (IPR004565); LolB (PF03550)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "lolB" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'lolB' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **lolB** (gene ID: lolB, UniProt: Q88PX4) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: LolB (Outer-Membrane Lipoprotein LolB)

**Gene:** *lolB* (OrderedLocusName PP_0724)
**Protein:** Outer-membrane lipoprotein LolB (Precursor)
**UniProt:** Q88PX4 (LOLB_PSEPK)
**Organism:** *Pseudomonas putida* strain KT2440 (ATCC 47054 / DSM 6125 / NCIMB 11950)
**Family:** LolB family; Pfam PF03550 (LolB); InterPro IPR004565 (OM_lipoprot_LolB), IPR029046 (LolA/LolB/LppX fold)
**Date:** 2026-09-01

---

## 1. Summary (Answer to the Research Question)

LolB is the **outer-membrane (OM) receptor that catalyzes the terminal step of the Lol lipoprotein-sorting pathway**. It is not an enzyme in the classical sense (it catalyzes no covalent chemistry); rather it is a lipoprotein-specific **chaperone/receptor that physically inserts triacylated lipoproteins into the outer membrane** after receiving them from the periplasmic chaperone LolA. Its substrate is the general population of OM-destined bacterial lipoproteins (defined by their N-terminal lipid anchor, not by sequence), which it accepts from LolA and hands off to the OM lipid bilayer. LolB carries out its function at the **periplasmic (inner) leaflet of the outer membrane**, to which it is itself tethered by an N-terminal triacyl-cysteine anchor. The pathway it completes — **Lol (Localization of Lipoproteins): LolCDE → LolA → LolB** — is essential for outer-membrane biogenesis and hence for viability in Gram-negative bacteria, including *Pseudomonas*.

The gene identity is unambiguous: the symbol *lolB*, the LolB protein family/domains, and the γ-proteobacterial organism all align, and the *P. putida* sequence itself carries every hallmark of a functional LolB (see §5). Function is assigned by HAMAP rule MF_00233 and is supported by direct sequence evidence plus an extensive body of primary mechanistic work on the *Escherichia coli* ortholog and confirmation of pathway conservation within *Pseudomonas*.

---

## 2. Biological Context: The Lol Pathway

Gram-negative bacteria express dozens of lipoproteins (~90 species in *E. coli*) that are anchored to either the inner membrane (IM) or the outer membrane by an N-terminal S-diacylglyceryl-cysteine that is further N-acylated (triacylation). OM-destined lipoproteins must be moved from their site of synthesis (the outer leaflet of the IM) across the aqueous periplasm to the OM. This is accomplished by the **Lol machinery**, which comprises five proteins working in a strict relay [PMID 15672528; PMID 19307584]:

1. **LolCDE** — an ATP-binding-cassette (ABC) transporter in the IM. It recognizes and, using ATP hydrolysis, **extracts** OM-destined lipoproteins from the IM outer leaflet, extruding them onto the periplasmic chaperone. Unlike most ABC transporters, it does not move substrate across a membrane but detaches a membrane-anchored substrate [PMID 18218629].
2. **LolA** — a soluble **periplasmic chaperone** that receives the lipoprotein from LolCDE, shielding its acyl chains inside a hydrophobic cavity, and diffuses across the periplasm.
3. **LolB** — the **OM receptor** that accepts the lipoprotein from LolA and **incorporates it into the outer membrane**, completing sorting [PMID 19307584; PMID 15672528].

Membrane specificity is set at the first step by the **"position-2 rule"**: a lipoprotein with **aspartate at the residue immediately following the lipidated cysteine (+2)** is retained in the IM (an "Lol-avoidance" signal that depends on phosphatidylethanolamine), whereas other residues at +2 permit LolCDE recognition and export to the OM [PMID 15672528; PMID 12032293; PMID 12823819]. Notably, neither LolA nor LolB re-checks this signal — sorting fidelity is imposed upstream at LolCDE [PMID 12823819].

---

## 3. Primary Function of LolB

**LolB is the outer-membrane receptor/inserter for lipoproteins — the last, committed step of the Lol pathway.**

- LolA "transports lipoproteins to the outer membrane where an outer membrane receptor, LolB, incorporates lipoproteins into the outer membrane" [PMID 19307584]. When the LolA–lipoprotein complex "interacts with outer membrane receptor LolB, the lipoproteins are transferred from LolA to LolB and then localized to the outer membrane" [PMID 15672528].
- LolB acts **catalytically**: in reconstituted assays, **a single LolB molecule catalyzes the incorporation of more than 100 molecules** of the lipoprotein Pal into outer membranes, and it does so by engaging specifically the **liganded** (cargo-loaded) form of LolA [PMID 18029423].
- LolB is **required and rate-controlling** for the final step: depletion of LolB causes lipoproteins to accumulate in the periplasm (bound to LolA) rather than reaching the OM [PMID 18029423].

**Substrate specificity.** LolB has no sequence-specific substrate; its "substrate" is the acyl anchor of essentially any OM-directed lipoprotein delivered by LolA. This sequence-independence is structurally rationalized — the LolA/LolB cavity contacts the acyl chains, not the polypeptide, so structurally diverse cargoes are handled by the same machinery [PMID 36037338; PMID 18029423].

---

## 4. Mechanism and Structure

**Shared fold, opposite roles.** LolA and LolB have "remarkably similar" structures — an **unclosed (incomplete) β-barrel capped by an α-helical lid**, forming a **hydrophobic cavity** that sequesters the lipoprotein's acyl chains away from water [PMID 15672528]. This fold defines the LolA/LolB/LppX superfamily (IPR029046).

**Energy-independent, unidirectional transfer.** The LolA→LolB hand-off occurs in the periplasm where **no ATP is available**; directionality is thermodynamic, driven by an **affinity gradient** in which LolB binds cargo more avidly than LolA (LolCDE → LolA → LolB → membrane) [PMID 15672528]. In-vivo photo-cross-linking (p-benzoyl-phenylalanine scanning) mapped a shared "**hot**" interaction area at the **entrance of the hydrophobic cavity** in both proteins, through which they dock in a **"mouth-to-mouth"** fashion, allowing acyl chains to pass directly between cavities without exposure to the aqueous phase; the same LolA surface engages the IM subunit LolC [PMID 19307584].

**The LolB-specific membrane-insertion element (Leu68 loop).** What makes LolB a productive terminal *transferase* rather than a second chaperone is a **loop that protrudes from LolB into the aqueous environment, with no analogous loop in LolA** [PMID 24569999]. Mutagenesis of a soluble LolB (mLolB) showed that replacing **Leu68** in this loop with acidic residues yields, for the first time, derivatives that **still accept lipoproteins from LolA but can no longer localize them to the OM** — cleanly uncoupling cargo binding from membrane insertion [PMID 24569999]. The hydrophobic loop is thus proposed to contact/penetrate the OM bilayer and deliver the acyl chains into it.

**Two separable activities.** Consistent with this, dissection of LolB function distinguishes (i) **lipoprotein binding**, (ii) **membrane targeting**, and (iii) **lipoprotein anchoring** [PMID 19678842].

---

## 5. Localization and the *P. putida* Ortholog

**Where LolB acts.** LolB is itself a **lipoprotein anchored to the outer membrane** (UniProt: "Cell outer membrane; Lipid-anchor"), positioning it at the periplasmic leaflet of the OM where it receives LolA and inserts cargo.

**LolB is itself a Lol substrate.** Because LolB is an OM lipoprotein with a non-Asp +2 signal (Ala in Q88PX4), it is trafficked to the OM by the same pathway it completes. A recent cryo-EM study captured LolCDE in complex with three substrates — Lpp, Pal, and **LolB itself** — showing LolB is recognized and extruded via a sequence-independent, structurally conserved interaction with a cleft on the periplasmic domain of LolE [PMID 41557797]. Thus newly made LolB is released by LolCDE, carried by LolA, and anchored in the OM like any other cargo — a self-referential feature of the receptor.

**Role of LolB's own lipid anchor.** A soluble, anchorless derivative (**mLolB**) still binds lipoproteins, supports *E. coli* growth, and transfers cargo from LolA to membranes — so the anchor is **not required for the core transfer chemistry** [PMID 19678842]. However, OM-anchored LolB is **more active** and correctly enforces OM specificity, whereas periplasmic mLolB shows **no membrane preference** (it will deposit cargo into IM, OM, or liposomes) and transiently mislocalizes some OM lipoproteins to the IM; phosphatidylethanolamine stimulates mLolB-mediated incorporation [PMID 19678842]. Thus the anchor **concentrates and orients** the receptor at the OM to give the terminal reaction its efficiency and destination fidelity.

**Direct evidence that Q88PX4 is a genuine LolB.** Analysis of the 205-residue *P. putida* precursor confirms all diagnostic features:
- A type II (lipoprotein) **signal peptide** (residues 1–17) ending in a canonical **lipobox L15-A16-G17-C18** (matching the [LVI][ASTVI][GAS]C consensus).
- **Cys18** annotated as both **S-diacylglycerol** and **N-palmitoyl cysteine** — i.e., a mature **triacylated** lipoprotein tethered by three acyl chains (mature chain 18–205).
- **Alanine at the +2 position** (Ala19), a **non-aspartate** residue that by the position-2 rule directs OM localization via the Lol pathway [PMID 15672528].
- A single **LolB-family domain** (PF03550; LolA/LolB/LppX fold).

These features, together with the demonstrated conservation of the Lol machinery in *Pseudomonas*, support transferring the *E. coli* LolB function to Q88PX4 on the basis of direct evidence rather than annotation alone.

**Conservation in *Pseudomonas*.** In *P. aeruginosa*, the LolABCDE machinery traffics lipoproteins from IM to OM and is "**essential for the biogenesis of the Gram-negative cell envelope and, consequently, for bacterial viability**" [PMID 32989085]. *E. coli* LolCDE correctly sorts *P. aeruginosa* lipoproteins, demonstrating cross-species mechanistic conservation [PMID 30992347], and the *P. aeruginosa* LolA structure confirms the same acyl-chain-binding chaperone mechanism, explicitly transferring cargo "to the OM receptor LolB" [PMID 20620146]. *P. putida* KT2440, a γ-proteobacterium, encodes the full pathway with *lolB* = PP_0724.

**Evolutionary relationship (bioinformatic evidence).** A global pairwise alignment of *P. putida* LolB (Q88PX4, 205 aa) against the experimentally characterized *E. coli* K-12 LolB (P61320, 207 aa) yields ≈**26% identity and ≈42% similarity** over the full length (this work; Needleman–Wunsch with a simplified substitution matrix, values approximate). This modest identity is typical of the LolB family, whose members **conserve the β-barrel/α-helical-lid fold and hydrophobic cavity far more strongly than their primary sequence** [PMID 24569999]. Together with the identical domain assignment (PF03550), shared lipobox architecture, and HAMAP MF_00233, this establishes Q88PX4 as a clear — if divergent — LolB ortholog whose function is defined by conserved structure rather than sequence. (One caveat: because of this divergence, the residue in Q88PX4 corresponding to *E. coli* LolB's functional Leu68 loop cannot be mapped reliably by simple pairwise alignment and would require structure-based superposition, e.g., of an AlphaFold model.)

---

## 6. Pathway Position and Physiological Significance

- **Pathway:** Lol lipoprotein-sorting/localization pathway (a protein-targeting pathway, not a metabolic one). LolB occupies the **terminal, OM-insertion node**: LolCDE (release) → LolA (transit) → **LolB (OM incorporation)**.
- **Biological process:** **Outer-membrane / cell-envelope biogenesis and maintenance.** By delivering OM lipoproteins (many of which are themselves components of essential envelope machines, e.g., the Bam and Lpt systems, and structural proteins such as Lpp and Pal), LolB is required to build and maintain the OM permeability barrier.
- **Essentiality / therapeutic relevance:** LolB is an **essential** OM lipoprotein [PMID 19678842], and the Lol pathway is a validated, actively pursued **antibacterial target** in Gram-negatives; small-molecule inhibitors (e.g., pyridineimidazoles acting on LolCDE) block lipoprotein OM targeting [PMID 25583975; PMID 32989085]. This essentiality is not a pleiotropic side-effect but a direct consequence of LolB's role — without OM lipoprotein delivery the envelope cannot be assembled.

---

## 7. Supported and Refuted Hypotheses

**Supported:**
- LolB is the OM receptor for the terminal step of the Lol pathway (multiple reconstitution studies) — **strongly supported**.
- LolB works catalytically and specifically on liganded LolA (>100 substrates/LolB) — **supported** [PMID 18029423].
- LolA→LolB transfer is ATP-independent and driven by an affinity/structural gradient via mouth-to-mouth cavity docking — **supported** [PMID 15672528; PMID 19307584].
- A LolB-unique protruding loop (Leu68) executes membrane insertion, separable from cargo binding — **supported** [PMID 24569999].
- Q88PX4 is a genuine triacylated OM lipoprotein with OM sorting signal — **supported by direct sequence evidence**.
- Pathway is conserved and essential in *Pseudomonas* — **supported** [PMID 30992347; PMID 32989085].

**Refuted / excluded:**
- LolB is **not** a metabolic enzyme (no catalyzed chemical reaction; no cofactor/active-site chemistry).
- LolB's lipid anchor is **not** required for the intrinsic transfer chemistry (anchorless mLolB is functional) [PMID 19678842].
- LolB does **not** enforce the OM-vs-IM sorting decision (that is set at LolCDE; LolA/LolB do not reject Asp-at-+2 cargo) [PMID 12823819].

---

## 8. Limitations and Future Directions

- Nearly all mechanistic detail derives from the *E. coli* ortholog; no *P. putida*-specific LolB structure or biochemistry was found. Conclusions for Q88PX4 rest on strong sequence conservation, HAMAP annotation, and demonstrated *Pseudomonas* pathway conservation (chiefly from *P. aeruginosa*).
- Residue numbering for the functionally critical loop (Leu68) is *E. coli*-based; the precise equivalent residue in *P. putida* Q88PX4 was not experimentally mapped here.
- Direct genetic essentiality of *lolB* specifically in *P. putida* KT2440 was inferred from genus/family data rather than a KT2440 knockout study.
- Future work: an experimental or AlphaFold structure of Q88PX4 to locate its protruding loop; verification of triacylation and OM localization in KT2440; and targeted essentiality testing in *P. putida*.

---

## Key References
- Okuda & Tokuda 2009, PNAS — mouth-to-mouth transfer model (PMID 19307584)
- Tokuda & Matsuyama 2004 — review of OM lipoprotein sorting; LolA/LolB fold and energetics (PMID 15672528)
- Watanabe et al. 2007 — LolB catalytic incorporation, liganded-LolA specificity (PMID 18029423)
- Tsukahara et al. 2009 — dissection of LolB function; dispensable anchor (PMID 19678842)
- Hayashi et al. 2014 — LolB protruding loop / Leu68 membrane-insertion role (PMID 24569999)
- Kaplan et al. 2022 — structural basis of lipoprotein recognition by LolA (PMID 36037338)
- Lorenz et al. 2019 — Lol sorting fidelity in *P. aeruginosa* (PMID 30992347)
- Lorenz et al. 2020 — Lol essentiality for envelope biogenesis in *P. aeruginosa* (PMID 32989085)
- Remans et al. 2010 — *P. aeruginosa* LolA structure (PMID 20620146)
- McLeod et al. 2015 — Lol pathway inhibitors (PMID 25583975)
- Szewczyk et al. 2026 — cryo-EM of LolCDE with substrates including LolB itself (PMID 41557797)


## Artifacts

- [OpenScientist final report](lolB-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](lolB-deep-research-openscientist_artifacts/final_report.pdf)