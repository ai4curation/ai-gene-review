---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-25T16:45:16.936309'
end_time: '2026-07-25T17:04:27.601219'
duration_seconds: 1150.67
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: tauD
  gene_symbol: tauD
  uniprot_accession: Q88RA3
  protein_description: 'RecName: Full=Alpha-ketoglutarate-dependent taurine dioxygenase
    {ECO:0000303|PubMed:22221834}; EC=1.14.11.17 {ECO:0000269|PubMed:22221834};'
  gene_info: Name=tauD {ECO:0000303|PubMed:22221834}; Synonyms=atsK {ECO:0000312|EMBL:AAN65862.1};
    OrderedLocusNames=PP_0230 {ECO:0000312|EMBL:AAN65862.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the TfdA dioxygenase family. .
  protein_domains: AtsK-like. (IPR051323); CHASE_dom. (IPR006189); TauD-like_sf. (IPR042098);
    TauD/TfdA-like. (IPR003819); TauD (PF02668)
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
  path: tauD-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: tauD-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88RA3
- **Protein Description:** RecName: Full=Alpha-ketoglutarate-dependent taurine dioxygenase {ECO:0000303|PubMed:22221834}; EC=1.14.11.17 {ECO:0000269|PubMed:22221834};
- **Gene Information:** Name=tauD {ECO:0000303|PubMed:22221834}; Synonyms=atsK {ECO:0000312|EMBL:AAN65862.1}; OrderedLocusNames=PP_0230 {ECO:0000312|EMBL:AAN65862.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the TfdA dioxygenase family. .
- **Key Domains:** AtsK-like. (IPR051323); CHASE_dom. (IPR006189); TauD-like_sf. (IPR042098); TauD/TfdA-like. (IPR003819); TauD (PF02668)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "tauD" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'tauD' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **tauD** (gene ID: tauD, UniProt: Q88RA3) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *tauD* (Q88RA3) in *Pseudomonas putida* KT2440

**Gene:** *tauD* (synonym *atsK*; ordered locus PP_0230)
**Protein:** Alpha-ketoglutarate-dependent taurine dioxygenase (TauD)
**UniProt:** Q88RA3 · **EC:** 1.14.11.17 · **Length:** 277 aa · **Organism:** *Pseudomonas putida* KT2440 (PSEPK)

---

## 1. Summary (Answer to the Research Question)

*tauD* encodes a soluble, cytoplasmic **Fe(II)/α-ketoglutarate (2-oxoglutarate)-dependent taurine dioxygenase** (EC 1.14.11.17). Its primary function is to catalyze the O₂- and α-ketoglutarate-dependent **hydroxylation of taurine (2-aminoethanesulfonate)** at its C1 carbon; the resulting unstable 1-hydroxy intermediate spontaneously decomposes to release **inorganic sulfite** plus aminoacetaldehyde, while the co-substrate α-ketoglutarate is oxidatively decarboxylated to succinate and CO₂. The enzyme's biological role is **organosulfonate → sulfur assimilation**: it liberates sulfite for cysteine biosynthesis when preferred sulfur sources (sulfate, cysteine) are scarce. This exact protein (TauD_Pp, PP_0230) has been directly characterized biochemically, kinetically, and crystallographically (Knauer et al., 2012, PMID 22221834).

---

## 2. Identity Verification (Critical Check)

The target was cross-checked against UniProt Q88RA3 and the primary literature:

- **Gene symbol match:** UniProt lists `Name=tauD`, `Synonyms=atsK`, `OrderedLocusNames=PP_0230`. The recommended protein name is "Alpha-ketoglutarate-dependent taurine dioxygenase," consistent with the target description.
- **Organism match:** *Pseudomonas putida* KT2440 confirmed.
- **Family/domain match:** Belongs to the **TfdA/TauD dioxygenase family** (Pfam PF02668 "TauD"; InterPro IPR003819 TauD/TfdA-like, IPR042098 TauD-like superfamily). This matches the enzymology in the literature.
- **Direct experimental confirmation:** Knauer et al. (2012) explicitly purified, kinetically characterized, and solved three apo crystal structures of the taurine dioxygenase **from *P. putida* KT2440 (TauD_Pp)** — i.e., this exact protein — and showed it closely mirrors *E. coli* TauD in spectra, structure, and kinetics (PMID 22221834).

**Note on the *atsK* synonym (potential source of confusion):** The genome-annotation synonym *atsK* refers to a paralogous 2-oxoglutarate-dependent **alkylsulfatase** biochemically characterized in a *different* strain, *P. putida* **S-313** (Kahnert & Kertesz, 2000, PMID 10913158; Müller et al., 2004/2005, PMID 15023059/15542595). AtsK cleaves alkyl **sulfate esters** (C4–C12), whereas the KT2440 PP_0230 product was directly shown to be a bona fide **taurine sulfonate** dioxygenase. The two are homologous members of the same superfamily (~38% identity between AtsK and *E. coli* TauD) with the same fold and chemistry, but distinct substrate specificity. The AtsK work is therefore used here for **mechanistic/structural inference**, while function of Q88RA3 itself rests on the KT2440-specific study.

---

## 3. Primary Function: Reaction and Substrate Specificity

### Reaction catalyzed (EC 1.14.11.17)
> **taurine + 2-oxoglutarate + O₂ → aminoacetaldehyde + sulfite + succinate + CO₂ + H⁺**

TauD is a **dioxygenase** that splits molecular O₂: one oxygen atom is incorporated into succinate (via oxidative decarboxylation of α-ketoglutarate) and the other is used to hydroxylate the substrate. Hydroxylation occurs at **C1 of taurine**, producing an unstable 1-hydroxy-2-aminoethanesulfonate that decomposes non-enzymatically to **sulfite + aminoacetaldehyde** (UniProt FUNCTION, ECO:0000269 PMID 22221834; Knauer et al. 2012).

### Substrate specificity
- **Primary substrate:** taurine (2-aminoethanesulfonate), a naturally abundant aminosulfonate. TauD "preferentially liberates sulfite from taurine" (van der Ploeg et al., 2001, PMID 11479697).
- **Co-substrate:** α-ketoglutarate (2-oxoglutarate), consumed stoichiometrically and converted to succinate + CO₂.
- **Cofactor:** one catalytic **Fe(II)** ion per subunit (UniProt COFACTOR, PMID 22221834); activity requires O₂ and is stimulated by ascorbate (a common feature of this family that re-reduces adventitiously oxidized iron).
- The homologous alkylsulfatase AtsK, by contrast, accepts **alkyl sulfate esters** and even a range of α-keto-acid co-substrates, illustrating how small active-site differences retune substrate scope within this superfamily (Kahnert & Kertesz, 2000, PMID 10913158).

---

## 4. Catalytic Mechanism (Structural & Spectroscopic Evidence)

TauD is the **paradigm system** for the Fe(II)/αKG dioxygenase superfamily:

- **Active-site iron** is held by the canonical **2-His-1-carboxylate "facial triad"** (Nam et al., 2014, PMID 24524675). Residue-level mapping of Q88RA3 (from its crystal structures, UniProt feature table) assigns this triad to **His97, Asp99 and His253** (the diagnostic HXD…H motif). The co-substrate 2-oxoglutarate is coordinated by **Thr124, His253 (bidentate to Fe), Arg264 and Arg268**, and the **taurine/sulfonate pocket** is formed by **His68, Tyr71, Asn93, Val100 and Arg268** — providing a structural basis for taurine substrate specificity. Three apo crystal structures of this exact protein are deposited: **PDB 3PVJ, 3V15, 3V17** (Knauer et al., 2012, PMID 22221834).
- **Catalytic cycle:** Fe(II) binds α-ketoglutarate and then O₂; oxidative decarboxylation of α-ketoglutarate produces CO₂, succinate, and a highly reactive **high-valent Fe(IV)=O (ferryl) intermediate**. TauD was the **first enzyme in which a mononuclear nonheme iron(IV)-oxo intermediate was spectroscopically characterized (2003)** (Nam et al., 2014, PMID 24524675). The ferryl species abstracts a hydrogen atom from taurine C1, and oxygen rebound yields the hydroxylated product.
- **Self-inactivation control:** In the closely related AtsK, non-productive O₂ activation is quenched by **self-hydroxylation of an active-site tyrosine (Tyr168)** that coordinates iron — a built-in protective mechanism against harmful side reactions (Müller et al., 2005, PMID 15542595). This structural insight extends to TauD-family enzymes generally.
- **Fold:** The AtsK/TauD fold is a double-stranded β-helix (cupin/jelly-roll) "distorted barrel" typical of the superfamily; the AtsK structure is "closely related to that of the taurine/α-ketoglutarate dioxygenase TauD" (Müller et al., 2004, PMID 15023059).

---

## 5. Quaternary Structure

The *P. putida* KT2440 TauD is a **homotetramer (dimer of dimers)**, binding one Fe(II) per subunit (UniProt SUBUNIT/COFACTOR, PMID 22221834; Knauer et al. 2012 title: the taurine dioxygenases from *P. putida* and *E. coli* "are tetramers"). This oligomeric state — shared with the homotetrameric AtsK (Kahnert & Kertesz, 2000, PMID 10913158) — is unusual for the superfamily, whose members are more often monomeric or dimeric.

---

## 6. Subcellular Localization

TauD is a **cytoplasmic, soluble enzyme**. Evidence/inference:
- **Bioinformatic check (this work):** the Q88RA3 sequence carries **no signal peptide and no transmembrane segment** (no Sec/Tat export or membrane-anchoring features), and the N-terminus (MSLTITPLSPALGA…) is not a cleavable signal — consistent with a soluble cytoplasmic protein.
- The protein was purified as a soluble crystallizable tetramer (PMID 22221834), consistent with cytoplasmic residence.
- **Pathway logic:** Taurine is first imported across the inner membrane by the **TauABC ABC transporter**, after which the intracellular TauD desulfonates it (van der Ploeg et al., 2001, PMID 11479697). Desulfonation therefore occurs **inside the cell, in the cytoplasm**, where the liberated sulfite feeds the cysteine-biosynthetic (sulfate assimilation) branch.

---

## 7. Pathway and Physiological Context

- **Pathway:** Aerobic **organosulfonate (taurine) catabolism for sulfur assimilation**. TauD provides the desulfonation step that converts an organic sulfonate into inorganic **sulfite (SO₃²⁻)**, which is reduced to sulfide and incorporated into cysteine.
- **Genetic organization / regulation:** In the model *E. coli* system, *tauD* is the fourth gene of the **tauABCD operon** (TauABC = ABC importer; TauD = desulfonase). Expression is induced under **sulfate/cysteine starvation** and requires the **LysR-type regulators CysB (master sulfur regulator) and Cbl** (van der Ploeg et al., 2001, PMID 11479697). The homologous *P. putida* αKG-dependent sulfonatase system (AtsK) is likewise "only expressed under sulfur starvation conditions, providing a selective advantage for bacterial growth in soils and rhizosphere" (Müller et al., 2004, PMID 15023059).
- **Strain-specific genomic evidence (this work):** In the *P. putida* KT2440 genome, *tauD* (PP_0230) is directly clustered with a complete taurine ABC-transporter operon — **PP_0231 *tauC*** (permease), **PP_0232 *tauB*** (ATP-binding), **PP_0233 *tauA*** (periplasmic taurine-binding protein) — i.e. the PP_0230–PP_0233 module recapitulates the *E. coli* *tauABCD* architecture. Immediately adjacent lies the parallel **ssuEADCB** cluster (PP_0236–PP_0240: SsuE FMN reductase, SsuA binding protein, SsuD alkanesulfonate monooxygenase, SsuC permease, SsuB ATPase) for FMNH₂-dependent desulfonation of other aliphatic sulfonates, and the master regulator **CysB** is encoded elsewhere (PP_2327). This confirms — *in the actual target organism* — that TauD works within an intact import-and-desulfonation module rather than by inference from *E. coli* alone: periplasmic **TauA** captures taurine, **TauBC** import it across the inner membrane, and cytoplasmic **TauD** liberates sulfite.
- **Ecological role:** For a soil/rhizosphere organism like *P. putida* KT2440, the ability to mine sulfur from abundant environmental sulfonates (taurine and related compounds) when inorganic sulfate is limiting is a competitive advantage.

---

## 8. Supported and Refuted Hypotheses

| Hypothesis | Verdict | Basis |
|---|---|---|
| Q88RA3 is a taurine/αKG dioxygenase (EC 1.14.11.17) | **Supported** | UniProt + direct characterization of KT2440 TauD (PMID 22221834) |
| Reaction yields sulfite + aminoacetaldehyde (+ succinate + CO₂) | **Supported** | UniProt catalytic activity; PMID 22221834 |
| Uses mononuclear nonheme Fe(II), 2-His-1-carboxylate triad, ferryl intermediate | **Supported** | PMID 24524675; superfamily mechanism |
| Homotetramer, 1 Fe(II)/subunit | **Supported** | UniProt; PMID 22221834 |
| Functions cytoplasmically in sulfur-starvation-induced sulfonate assimilation | **Supported** | Pathway logic + PMID 11479697, 15023059 |
| KT2440 possesses an intact tauABCD-type import/desulfonation module around PP_0230 | **Supported** | Genomic clustering PP_0230–PP_0233 (tauD-tauCBA) + adjacent ssuEADCB, this work |
| The gene product is the S-313 alkylsulfatase AtsK (alkyl sulfate esters) | **Refuted for this protein** | AtsK is a paralog from a different strain; KT2440 PP_0230 was shown to be a taurine dioxygenase (PMID 22221834). *atsK* is only a genome-annotation synonym. |

---

## 9. Limitations and Future Directions

- **Substrate range not exhaustively mapped for KT2440 TauD:** while taurine is the confirmed physiological substrate, quantitative kinetics for alternative sulfonates/α-keto-acids in the KT2440 enzyme specifically were not fully detailed; broader specificity is inferred from *E. coli* TauD and *P. putida* AtsK.
- **Localization is inferred** (soluble/cytoplasmic) from sequence features and pathway logic rather than an explicit fractionation experiment for Q88RA3.
- **Direct regulatory data in KT2440** (CysB/Cbl control of PP_0230) is extrapolated from *E. coli*; although the *tauABCD* and *ssuEADCB* gene clusters and *cysB* are all present in the KT2440 genome (this work), strain-specific transcriptional/promoter confirmation would further strengthen the model.
- Future work: substrate-bound/holo crystal structures of TauD_Pp, in-vivo growth phenotypes of a KT2440 *tauD* deletion on taurine as sole sulfur source, and quantitative regulon mapping.

---

## Key References

- Knauer SH, Hartl-Spiegelhauer O, Schwarzinger S, Hänzelmann P, Dobbek H. *The Fe(II)/α-ketoglutarate-dependent taurine dioxygenases from Pseudomonas putida and Escherichia coli are tetramers.* FEBS J, 2012. **PMID 22221834.** *(Direct characterization of the target protein.)*
- van der Ploeg JR, Eichhorn E, Leisinger T. *Sulfonate-sulfur metabolism and its regulation in Escherichia coli.* Arch Microbiol, 2001. **PMID 11479697.** *(Pathway and regulation.)*
- Nam W, Lee YM, Fukuzumi S. *Tuning reactivity and mechanism in oxidation reactions by mononuclear nonheme iron(IV)-oxo complexes.* Acc Chem Res, 2014. **PMID 24524675.** *(Ferryl intermediate; 2-His-1-carboxylate triad.)*
- Kahnert A, Kertesz MA. *Characterization of a sulfur-regulated oxygenative alkylsulfatase from Pseudomonas putida S-313.* J Biol Chem, 2000. **PMID 10913158.** *(Homologous AtsK; substrate scope; tetramer.)*
- Müller I, et al. *Crystal structure of the alkylsulfatase AtsK...* J Mol Biol, 2004. **PMID 15023059.** *(Fold, mechanism, sulfur-starvation induction.)*
- Müller I, et al. *Succinate complex crystal structures of ... AtsK: steric aspects of enzyme self-hydroxylation.* J Mol Biol, 2005. **PMID 15542595.** *(Self-hydroxylation protection.)*


## Artifacts

- [OpenScientist final report](tauD-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](tauD-deep-research-openscientist_artifacts/final_report.pdf)