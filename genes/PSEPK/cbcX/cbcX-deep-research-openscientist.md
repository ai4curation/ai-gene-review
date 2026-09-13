---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-13T05:34:10.093568'
end_time: '2026-08-13T05:46:26.335196'
duration_seconds: 736.24
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: cbcX
  gene_symbol: cbcX
  uniprot_accession: Q88R38
  protein_description: 'SubName: Full=Choline / betaine / carnitine ABC transporter-substrate
    binding protein {ECO:0000313|EMBL:AAN65927.1}; EC=3.6.3.32 {ECO:0000313|EMBL:AAN65927.1};'
  gene_info: Name=cbcX {ECO:0000313|EMBL:AAN65927.1}; OrderedLocusNames=PP_0296 {ECO:0000313|EMBL:AAN65927.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: ABC_choline_sub-bd. (IPR017783); ABC_Gly_betaine_transp_sub-bd.
    (IPR007210); OpuAC (PF04069)
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
  path: cbcX-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: cbcX-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88R38
- **Protein Description:** SubName: Full=Choline / betaine / carnitine ABC transporter-substrate binding protein {ECO:0000313|EMBL:AAN65927.1}; EC=3.6.3.32 {ECO:0000313|EMBL:AAN65927.1};
- **Gene Information:** Name=cbcX {ECO:0000313|EMBL:AAN65927.1}; OrderedLocusNames=PP_0296 {ECO:0000313|EMBL:AAN65927.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** ABC_choline_sub-bd. (IPR017783); ABC_Gly_betaine_transp_sub-bd. (IPR007210); OpuAC (PF04069)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "cbcX" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'cbcX' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **cbcX** (gene ID: cbcX, UniProt: Q88R38) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: **cbcX** (PP_0296, UniProt Q88R38)
### *Pseudomonas putida* KT2440 — Choline substrate-binding protein of the Cbc ABC transporter

---

## 1. Summary (Answer to the Research Question)

**cbcX / PP_0296 (Q88R38) encodes the periplasmic, choline-specific substrate-binding protein (SBP) of the Cbc (choline/betaine/carnitine) ATP-binding-cassette (ABC) import system.** Its primary molecular function is to capture the quaternary-ammonium compound **choline** from the periplasm with high affinity (and glycine betaine with lower affinity) and deliver it to the membrane-embedded **CbcWV** permease/ATPase core for ATP-driven uptake into the cytoplasm. It is **not itself a catalytic enzyme or a membrane transporter**; despite the EC 3.6.3.32 tag inherited from the transport reaction of the whole complex, CbcX is the recognition/receptor subunit. The imported choline is subsequently oxidized (BetAB) to the osmoprotectant **glycine betaine**, supporting osmotic-stress tolerance, and can also be catabolized as a **carbon/nitrogen source**. CbcX carries out its function in the **periplasm** (it bears a cleavable Sec signal peptide and adopts the class-II periplasmic-binding-protein / "Venus-flytrap" fold).

Identity is confirmed: the UniProt description ("Choline / betaine / carnitine ABC transporter-substrate binding protein"), gene symbol (cbcX), domains (OpuAC/PF04069; IPR017783 ABC_choline_sub-bd), and *P. putida* KT2440 genomic context all match the experimentally characterized Cbc system of *Pseudomonas* and its orthologs. There is no gene-symbol ambiguity.

---

## 2. Gene/Protein Identity Verification

| Attribute | Value | Source |
|---|---|---|
| UniProt accession | Q88R38 | UniProt |
| Gene symbol / locus | cbcX / PP_0296 | UniProt, KEGG `ppu:PP_0296` |
| Organism | *Pseudomonas putida* KT2440 | UniProt |
| Length | 315 aa | UniProt |
| Signal peptide | residues 1–21 (Sec; cleaved), mature chain 22–315 | UniProt |
| Domain | ABC-type glycine betaine transport SBP, res. 29–284 | UniProt |
| Pfam / InterPro | PF04069 (OpuAC); IPR017783, IPR007210 | UniProt/InterPro |
| Ortholog group | eggNOG COG2113; KEGG K02002 | UniProt/KEGG |
| Fold | Periplasmic binding protein-like II (SSF53850; Gene3D 3.40.190.10/100) | UniProt |
| Genomic neighbour | PP_0295 = CbcW permease (K02001) | KEGG |

**Conclusion:** All annotations converge on a single, unambiguous assignment. The gene is correctly identified; the symbol is not confused with any unrelated "cbcX."

---

## 3. Primary Function and Substrate Specificity

CbcX is the periplasmic **substrate-binding protein (SBP)** — the receptor subunit — of a Type I ABC importer. Its direct experimental characterization comes from the orthologous Cbc system of *Pseudomonas syringae*/*P. aeruginosa*, where the SBP encoded by the **cbcXWV** operon binds:

- **Choline** with high affinity — K_m ≈ **2.6 µM** (preferred substrate)
- **Glycine betaine** with lower affinity — K_m ≈ **24.2 µM**

Critically, **CbcXWV-mediated betaine uptake does not occur in the presence of choline**, establishing choline as the physiologically dominant substrate of CbcX (Chen et al. 2010, PMID 19919675). The *P. putida* KT2440 protein (PP_0296) is the direct ortholog and carries the identical annotation and KEGG ortholog (K02002).

Within the transporter, CbcX supplies **specificity**: the shared **CbcWV** core also partners with dedicated SBPs for other quaternary amines — **BetX** (betaine-specific, K_m ≈ 0.6 µM) and **CaiX** (carnitine-specific, K_m ≈ 24 µM) (Chen et al. 2010). Short-chain acylcarnitines and free carnitine are imported through the **CaiX–CbcWV** assembly (Meadows et al. 2018, PMID 29517479), independently confirming CbcWV as a common translocation core served by interchangeable binding proteins. **CbcX is therefore the choline-recognition module of this modular importer.**

> Note on EC 3.6.3.32: this number denotes the *choline-transporting ATPase* reaction of the intact ABC complex (ATP + H₂O + choline_out → ADP + Pᵢ + choline_in). CbcX contributes the substrate-recognition step but has no intrinsic ATPase/hydrolase activity — the ATPase resides in the CbcV nucleotide-binding subunit.

---

## 4. Structural Basis of Substrate Recognition

CbcX belongs to the **OpuAC / ProX family of class-II periplasmic binding proteins** (Pfam PF04069; SSF53850). Structural understanding derives from crystallized orthologs of the same fold:

- **ChoX** (*Sinorhizobium meliloti*), the direct ortholog of CbcX, was crystallized bound to **choline** and **acetylcholine**, plus closed-unliganded and semi-closed states — revealing the canonical two-lobe **"Venus-flytrap"** SBP architecture (Oswald et al. 2008, PMID 18779321; Oswald et al. 2009, PMID 19642870). Chen et al. reported that ChoX and CbcX share very similar binding properties.
- In the *Agrobacterium tumefaciens* **ChoXWV** ortholog, two pocket **tryptophan residues (W40, W87)** are essential for choline binding, and the model is built on *S. meliloti* ChoX; the system is a high-affinity transporter "with a preference for choline" (Aktas et al. 2011, PMID 21803998).
- The paradigm compatible-solute SBP **ProX** (*E. coli*) shows that **cation-π interactions** between the ligand's positively charged quaternary amine and a **rectangular box of three tryptophans** are the key determinants of high-affinity binding (Schiefner et al. 2004, PMID 14612446).

**Mechanistic inference:** CbcX recognizes the trimethyl-ammonium head-group of choline through cation-π interactions inside an aromatic (tryptophan) cage and closes around the ligand in a Venus-flytrap motion, priming delivery to CbcWV. This explains both the high affinity and the selectivity for choline over structural analogues.

---

## 5. Subcellular Localization

CbcX carries out its function in the **periplasm** (outside the cytoplasmic membrane):

- It bears a **cleavable N-terminal Sec signal peptide (residues 1–21)** with a mature chain beginning at residue 22 — the hallmark of a **soluble periplasmic protein** (not a lipobox-anchored lipoprotein). This contrasts with the *Bacillus subtilis* ortholog OpuAC, which is a membrane-anchored lipoprotein because Gram-positive SBPs must be tethered (Kempf et al. 1997, PMID 9335265).
- Chen et al. (2010) explicitly describe the Cbc system as using "multiple **periplasmic** substrate-binding proteins."
- The mature protein diffuses in the periplasmic space, scavenges choline that crosses the outer membrane, and docks onto the periplasmic face of the CbcWV inner-membrane complex to release ligand for translocation.

---

## 6. Biological Process / Pathway Context

CbcX is the **entry gatekeeper** of a quaternary-ammonium-compound assimilation and osmoadaptation module in *P. putida*:

```
periplasmic choline
      │  (capture)
   CbcX  ── docks on ──▶  CbcWV (inner-membrane permease + ATPase, ATP-driven)
      │                         │
      ▼                         ▼
                        cytoplasmic choline
                                │  BetA (choline dehydrogenase) → betaine aldehyde
                                │  BetB (betaine aldehyde dehydrogenase)
                                ▼
                        GLYCINE BETAINE
                          │                 │
        (compatible solute; osmotic       (carbon / nitrogen /
         stress tolerance)                  energy source)
```

- In *P. putida* KT2440, the **betBA** genes convert imported choline into the highly effective compatible solute **glycine betaine**, which is required both for endurance to high salt and for use of choline-derived compounds as a **carbon or nitrogen source** (Galvão et al. 2006, PMID 17116241).
- The Cbc/Cho ABC system is the **high-affinity** route for choline acquisition (Aktas et al. 2011), complementing low-affinity BCCT-family secondary transporters such as BetT (Chen & Beattie 2008, PMID 18156257).
- Because CbcX occupancy by choline blocks CbcWV-mediated uptake of other ligands (Chen et al. 2010), CbcX effectively prioritizes choline import when it is available.

This pathway is central to how *P. putida* — a soil and plant-associated bacterium living in environments rich in plant-derived choline — obtains osmoprotectants and nutrients.

---

## 7. Hypotheses: Supported and Refuted

**Supported:**
- **H1 — CbcX is the periplasmic choline-specific SBP of an ABC importer.** Supported by direct biochemistry of the ortholog (K_m choline 2.6 µM; Chen et al. 2010), matching annotation, and genomic adjacency to the CbcW permease.
- **H2 — CbcX acts in the periplasm.** Supported by the cleavable Sec signal peptide (UniProt) and the "periplasmic SBP" description (Chen et al. 2010).
- **H3 — Recognition is via a Venus-flytrap aromatic (Trp) cage / cation-π mechanism.** Supported by crystal structures of ChoX and ProX and mutagenesis of essential tryptophans (PMIDs 18779321, 19642870, 21803998, 14612446).
- **H4 — CbcX feeds osmoprotection and choline catabolism.** Supported by BetAB pathway data in *P. putida* (Galvão et al. 2006).
- **H5 — CbcX is one interchangeable module of a shared CbcWV core.** Supported by BetX/CaiX partnership and CaiX–CbcWV acylcarnitine import (Chen et al. 2010; Meadows et al. 2018).

**Refuted / corrected:**
- **CbcX is itself an ATPase/enzyme (as the EC 3.6.3.32 tag might suggest).** Refuted — the EC number describes the whole-complex transport reaction; CbcX is the non-catalytic receptor subunit, and the ATPase activity belongs to CbcV.
- **CbcX is a membrane-integral or lipid-anchored lipoprotein (as in Gram-positive OpuAC).** Refuted for *P. putida* — the Sec signal peptide is cleaved (no lipobox), indicating a soluble periplasmic protein.

---

## 8. Evidence Quality and Limitations

- **Strongest (experimental, precise):** ligand-binding affinities and transporter reconstitution for the *Pseudomonas* Cbc system (Chen et al. 2010); crystal structures/mutagenesis of orthologs ChoX and ProX (Oswald 2008/2009; Schiefner 2004; Aktas 2011).
- **Bioinformatic/inference:** signal peptide, domain, fold, ortholog group, and gene neighborhood for the exact *P. putida* PP_0296 protein (UniProt, KEGG, InterPro).
- **Limitation:** Direct biochemical characterization of the *P. putida* KT2440 CbcX protein itself (e.g., its own K_d for choline) has not, to my knowledge, been published; the functional assignment rests on very close orthology (identical operon architecture, domain, and KEGG ortholog) to the experimentally validated *P. syringae*/*P. aeruginosa* CbcX and *S. meliloti*/*A. tumefaciens* ChoX. Given the >high sequence/architecture conservation, this inference is robust.
- **Future directions:** (i) purify *P. putida* CbcX and measure choline/betaine affinities directly; (ii) solve/predict its structure (AlphaFold model available) to confirm the tryptophan aromatic cage; (iii) test cbcX deletion phenotypes for choline uptake and osmoprotection in KT2440; (iv) clarify the exact fate/regulation (the adjacent PP_0298 AraC-family, glycine-betaine-responsive activator suggests substrate-inducible expression).

---

## 9. References (PMID)

1. Chen C, Malek AA, Wargo MJ, Hogan DA, Beattie GA. *The ATP-binding cassette transporter Cbc (choline/betaine/carnitine) recruits multiple substrate-binding proteins with strong specificity for distinct quaternary ammonium compounds.* Mol Microbiol. 2010. **PMID 19919675.**
2. Meadows JA, Willsey GG, Wargo MJ. *Differential requirements for processing and transport of short-chain versus long-chain O-acylcarnitines in Pseudomonas aeruginosa.* 2018. **PMID 29517479.**
3. Galvão TC, de Lorenzo V, Cánovas D. *Uncoupling of choline-O-sulphate utilization from osmoprotection in Pseudomonas putida.* Mol Microbiol. 2006. **PMID 17116241.**
4. Aktas M, Jost KA, Fritz C, Narberhaus F. *Choline uptake in Agrobacterium tumefaciens by the high-affinity ChoXWV transporter.* J Bacteriol. 2011. **PMID 21803998.**
5. Oswald C, Smits SHJ, Höing M, Sohn-Bösser L, Dupont L, Le Rudulier D, Schmitt L, Bremer E. *Crystal structures of the choline/acetylcholine substrate-binding protein ChoX from Sinorhizobium meliloti.* J Biol Chem. 2008. **PMID 18779321.**
6. Oswald C, Smits SHJ, Höing M, Bremer E, Schmitt L. *Structural analysis of the choline-binding protein ChoX in a semi-closed and ligand-free conformation.* 2009. **PMID 19642870.**
7. Schiefner A, Breed J, Bösser L, et al. *Cation-pi interactions as determinants for binding of the compatible solutes glycine betaine and proline betaine by ProX from E. coli.* J Biol Chem. 2004. **PMID 14612446.**
8. Kempf B, Gade J, Bremer E. *Lipoprotein from the osmoregulated ABC transport system OpuA of Bacillus subtilis.* J Bacteriol. 1997. **PMID 9335265.**
9. Chen C, Beattie GA. *Pseudomonas syringae BetT is a low-affinity choline transporter responsible for superior osmoprotection by choline over glycine betaine.* J Bacteriol. 2008. **PMID 18156257.**

*Database sources: UniProt (Q88R38), KEGG (ppu:PP_0296), InterPro/Pfam, eggNOG.*


## Artifacts

- [OpenScientist final report](cbcX-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](cbcX-deep-research-openscientist_artifacts/final_report.pdf)