---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-17T14:19:50.361848'
end_time: '2026-07-17T14:48:48.686467'
duration_seconds: 1738.32
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: dapF__Q88GD4
  gene_symbol: dapF
  uniprot_accession: Q88GD4
  protein_description: 'RecName: Full=Diaminopimelate epimerase {ECO:0000256|HAMAP-Rule:MF_00197,
    ECO:0000256|NCBIfam:TIGR00652}; Short=DAP epimerase {ECO:0000256|HAMAP-Rule:MF_00197};
    EC=5.1.1.7 {ECO:0000256|HAMAP-Rule:MF_00197, ECO:0000256|NCBIfam:TIGR00652}; AltName:
    Full=PLP-independent amino acid racemase {ECO:0000256|HAMAP-Rule:MF_00197};'
  gene_info: Name=dapF {ECO:0000256|HAMAP-Rule:MF_00197}; OrderedLocusNames=PP_3790
    {ECO:0000313|EMBL:AAN69384.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the diaminopimelate epimerase family.
  protein_domains: DAP_epimerase_DapF. (IPR001653); DAP_epimerase (PF01678)
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
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: dapF__Q88GD4-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: dapF__Q88GD4-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88GD4
- **Protein Description:** RecName: Full=Diaminopimelate epimerase {ECO:0000256|HAMAP-Rule:MF_00197, ECO:0000256|NCBIfam:TIGR00652}; Short=DAP epimerase {ECO:0000256|HAMAP-Rule:MF_00197}; EC=5.1.1.7 {ECO:0000256|HAMAP-Rule:MF_00197, ECO:0000256|NCBIfam:TIGR00652}; AltName: Full=PLP-independent amino acid racemase {ECO:0000256|HAMAP-Rule:MF_00197};
- **Gene Information:** Name=dapF {ECO:0000256|HAMAP-Rule:MF_00197}; OrderedLocusNames=PP_3790 {ECO:0000313|EMBL:AAN69384.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the diaminopimelate epimerase family.
- **Key Domains:** DAP_epimerase_DapF. (IPR001653); DAP_epimerase (PF01678)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "dapF" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'dapF' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **dapF** (gene ID: dapF__Q88GD4, UniProt: Q88GD4) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *dapF* (Diaminopimelate epimerase, DapF) in *Pseudomonas putida* KT2440

**Target:** gene `dapF` / locus `PP_3790` / UniProt **Q88GD4** (`dapF__Q88GD4`)
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440), PSEPK
**Enzyme:** Diaminopimelate epimerase (DAP epimerase), **EC 5.1.1.7**; "PLP‑independent amino acid racemase"
**Family:** Diaminopimelate epimerase family — Pfam **PF01678** (DAP_epimerase); InterPro **IPR001653**; HAMAP‑Rule **MF_00197**; TIGRfam **TIGR00652** (dapF)

---

## 1. Summary (Answer to the Research Question)

*dapF* (Q88GD4, PP_3790) encodes **diaminopimelate epimerase (DapF)**, a soluble **cytoplasmic** enzyme that catalyzes the reversible **stereoinversion of LL‑2,6‑diaminopimelate (LL‑DAP) to *meso*‑2,6‑diaminopimelate (*meso*‑DAP)** — the penultimate reaction of the diaminopimelate (DAP) branch of L‑lysine biosynthesis (EC 5.1.1.7). DapF is a **cofactor‑independent (pyridoxal‑5′‑phosphate‑independent) epimerase** that uses an unusual **two‑base "1,1‑proton‑transfer" mechanism** rather than a PLP cofactor. In the classical enzymes this two‑base pair is two active‑site cysteines (thiol/thiolate); however, **a key finding of this report is that Q88GD4 appears to be a member of the recently described DapF‑SS subclass** — its two catalytic‑position residues are **serines (Ser70 and Ser205), not cysteines** — whereas its *P. putida* paralog Q88CF3 (PP_5228) is a canonical DapF‑CC (Cys75/Cys219). Its product, *meso*‑DAP, has two essential fates: (i) direct incorporation into the peptidoglycan stem peptide (position 3) of the Gram‑negative cell wall, and (ii) decarboxylation by LysA (DAP decarboxylase) to yield L‑lysine for protein synthesis. In *P. putida* KT2440, the genome encodes the complete **succinylase branch** that produces DapF's LL‑DAP substrate and **lacks the *ddh* (meso‑DAP dehydrogenase) bypass**, so DapF activity is the **obligate** route to *meso*‑DAP. The functional assignment for Q88GD4 is by strong homology (UniProt evidence level PE:3) to biochemically and structurally characterized orthologs; the mechanistic, structural, and kinetic evidence below derives from those orthologs (*Escherichia coli*, *Haemophilus influenzae*) and from the DapF‑SS characterization of Lamer et al. 2025.

---

## 2. Gene/Protein Identity Verification

The gene symbol **dapF**, the enzyme name **diaminopimelate epimerase**, EC **5.1.1.7**, the "PLP‑independent amino acid racemase" alternate name, the **DAP_epimerase family (PF01678/IPR001653)**, and the organism (*P. putida* KT2440) are **fully mutually consistent** across UniProt and the primary literature. Retrieval of the Q88GD4 sequence and annotations confirmed:

- A **268‑residue** protein, gene `dapF`, locus `PP_3790`.
- UniProt keywords: **Cytoplasm, Lysine biosynthesis, Amino‑acid biosynthesis, Isomerase**.
- UniProt FUNCTION: *"Catalyzes the stereoinversion of LL‑2,6‑diaminopimelate (L,L‑DAP) to meso‑diaminopimelate (meso‑DAP), a precursor of L‑lysine and an essential component of the bacterial peptidoglycan."*
- UniProt PATHWAY: *"L‑lysine biosynthesis via DAP pathway; DL‑2,6‑diaminopimelate from LL‑2,6‑diaminopimelate: step 1/1."*
- The two conserved pK‑modulating residues (His147, Glu196) that flank the catalytic center are present; however, UniProt assigns **no "Active site" cysteine residues** to Q88GD4 (unlike the E. coli enzyme and the Q88CF3 paralog), an early hint that the catalytic residues are non‑cysteine (see §4).

**Conclusion:** the target is unambiguously a diaminopimelate epimerase. No conflicting/paralogous‑symbol literature issue was encountered. (Note: the *phzF* phenazine‑biosynthesis protein shares the DapF fold but is a distinct isomerase lacking the catalytic cysteines — PMID 15545603 — and is *not* the target here.)

---

## 3. Primary Function: The Catalyzed Reaction and Substrate Specificity

**Reaction:** LL‑2,6‑diaminopimelate ⇌ *meso*‑2,6‑diaminopimelate (a 1,1‑proton‑transfer stereoinversion at one of the two α‑stereocenters of the symmetric diamino‑diacid DAP). This is the **penultimate step of L‑lysine biosynthesis**: "D,L‑Diaminopimelate is generated from the corresponding L,L‑isomer by the dapF‑encoded epimerase" (Koo & Blanchard 1999, PMID 10194362); "Diaminopimelate (DAP) epimerase catalyzes the stereoinversion of ll‑DAP to meso‑DAP, a precursor of l‑lysine and an essential component of the bacterial peptidoglycan" (Pillai et al. 2007, PMID 17889830).

**Substrate specificity (experimental, orthologs):** The enzyme is highly specific for the DAP scaffold. Purified *E. coli* LL‑DAP epimerase epimerizes LL‑DAP with **Km ≈ 0.26 mM**; substrate‑analog studies show **N‑hydroxy‑DAP** is the most potent competitive inhibitor (**Ki = 0.0056 mM**), lanthionine isomers inhibit with Ki = 0.18–0.42 mM, N‑amino‑DAP is weak (Ki = 2.9 mM), and 4‑methylene‑DAP is noncompetitive (Ki′ = 0.95 mM) (Lam et al. 1988, PMID 3042781). α‑Methyl amino acids act as slow‑binding inhibitors (Lamer et al. 2025, PMID 40299312). This SAR indicates a tightly complementary active site that recognizes the α‑amino/α‑carboxylate groups flanking the epimerized center and discriminates strongly against non‑DAP amino acids. (Some family members show minor promiscuous activity on lysine/related amino acids, but DAP is the physiological substrate.)

---

## 4. Catalytic Mechanism and Structure

**Cofactor‑independent two‑cysteine mechanism.** Unlike alanine or glutamate racemases, DapF requires **no PLP or metal cofactor**. Catalysis relies on **two active‑site cysteines**, one acting as a base (thiolate) to abstract the Cα proton and the other as an acid (thiol) to re‑donate a proton to the opposite face, inverting stereochemistry:
- Cirilli et al. 1998 (PMID 9843410): in *H. influenzae* DapF, "Cys73 of the amino terminal domain is found in disulfide linkage, at the domain interface, with Cys217 of the carboxy terminal domain, and we suggest that these two cysteine residues in the reduced, active enzyme function as the acid and base in the mechanism."
- Pillai et al. 2007 (PMID 17889830): DapF "belongs to the group of PLP‑independent amino acid racemases that function through a rather unusual mechanism involving two cysteines acting in concert as a base (thiolate) and an acid (thiol)."
- Koo & Blanchard 1999 (PMID 10194362): pH‑dependence and kinetic isotope effects support two catalytic groups (pK ≈ 6–8.5) and a two‑base mechanism.

Recent work has even engineered/discovered natural variants that use paired **serines** (DapF‑SS) in place of cysteines with similar kinetics, underscoring the generality of the two‑base chemistry (Lamer et al. 2025, PMID 40774471).

**Architecture and conformational cycle.** DapF is a **monomeric, two‑domain** protein with internal pseudo‑2‑fold symmetry: "The 274 amino acid enzyme consists of two structurally homologous domains, each containing eight beta‑strands and two alpha‑helices" (Cirilli et al. 1998, PMID 9843410), placing one catalytic cysteine from each domain on opposite faces of the substrate Cα. Catalysis involves a **substrate‑induced domain closure**: "Substrate binding to the C‑terminal domain triggers the closure of the N‑terminal domain coupled with tight encapsulation of the ligand… and expulsion of water molecules with concomitant desolvation of the thiolate base. This structural rearrangement is critical for catalysis" (Pillai et al. 2007, PMID 17889830). Solvent exclusion elevates the effective basicity of the thiolate and enforces strict stereocontrol, preventing non‑productive racemization.

**Mapping to Q88GD4 — a DapF‑SS (serine‑serine) variant.** A precise residue‑level mapping to the *experimentally* annotated *E. coli* DapF (UniProt P0A6K1, PE:1) was performed. In DapF the catalytic residue lies **immediately N‑terminal to an invariant substrate‑binding motif**: *E. coli* has catalytic **Cys73**–Gly74–Asn75 ("GN" binding site) and **Cys217**–Gly218–Ser219 ("GS" binding site). The *P. putida* paralog **Q88CF3 (PP_5228)** is annotated identically as a canonical **DapF‑CC** with catalytic **Cys75/Cys219** (CGN and CG‑T motifs). In the **target Q88GD4 (PP_3790)**, the equivalent catalytic positions — unambiguously fixed by its conserved binding motifs **GN (residues 71–72)** and **GT (residues 206–207)** — are **Ser70 and Ser205, not cysteines**. The pK‑modulating His147 and Glu196 are retained, and UniProt assigns **no catalytic cysteine** to Q88GD4 (whereas it does for both E. coli and the paralog). The cysteines present in Q88GD4 (positions 19, 24, 33, 78, 103, 148, 210, 252, 263) are offset from the catalytic register (e.g., Cys78/Cys210 lie +8/+5 residues downstream of the true catalytic positions) and are **not** the catalytic residues.

This signature — full DAP‑epimerase fold and substrate‑binding residues, but paired **serines** at the two catalytic positions — matches the recently characterized **DapF‑SS** subclass: Lamer et al. 2025 (PMID 40774471) described "enzymes of the cofactor‑independent racemase and epimerase class that use paired catalytic serines (DapF‑SS) instead of cysteines," which "catalyze reversible epimerization of DAP with similar kinetic parameters to that of DapF‑CC enzymes" and were found across "thousands of other predicted DapF‑SS enzymes from diverse bacterial phyla." Q88GD4 is therefore best classified as a **putative DapF‑SS diaminopimelate epimerase**, expected to perform the same LL‑DAP ⇌ meso‑DAP reaction via an analogous two‑base mechanism using serine hydroxyls in place of thiols. (This is a bioinformatic inference from precise active‑site mapping plus the DapF‑SS literature; it has not been experimentally verified for the *P. putida* enzyme.) Notably, KT2440 encodes **both** subclasses — a canonical DapF‑CC (Q88CF3/PP_5228) and this DapF‑SS (Q88GD4/PP_3790).

---

## 5. Subcellular Localization

DapF acts in the **cytoplasm**. This is consistent with (i) UniProt SUBCELLULAR LOCATION "Cytoplasm" (HAMAP‑Rule MF_00197), (ii) UniProt keyword "Cytoplasm," (iii) the absence of any signal peptide, transmembrane segment, or lipobox in the Q88GD4 sequence, and (iv) the fact that its substrate (LL‑DAP) and downstream enzymes (LysA, MurE) are cytoplasmic components of amino‑acid and peptidoglycan‑precursor metabolism. The *meso*‑DAP product is subsequently either decarboxylated in the cytoplasm (→ L‑lysine) or ligated onto the UDP‑MurNAc‑tripeptide precursor by MurE in the cytoplasm before the lipid‑linked precursor is exported for cell‑wall assembly.

---

## 6. Pathway Context in *P. putida* KT2440

A UniProt proteome survey (taxid 160488) shows KT2440 encodes the **complete succinylase branch** of the DAP pathway upstream of DapF:

| Step | Gene(s) / locus | Enzyme (EC) |
|------|-----------------|-------------|
| Aspartate‑β‑semialdehyde | *asd* (PP_1989/PP_1992) | ASADH (1.2.1.11) |
| → HTPA | *dapA* (PP_2639, PP_1237) | 4‑hydroxy‑THDP synthase (4.3.3.7) |
| → THDP | *dapB* (PP_4725) | HTPA reductase (1.17.1.8) |
| → N‑succinyl‑THDP | *dapD* (PP_1530) | THDP N‑succinyltransferase (2.3.1.117) |
| → N‑succinyl‑LL‑DAP | *dapC* (PP_1588) | N‑succinyl‑LL‑DAP aminotransferase (2.6.1.17) |
| → **LL‑DAP** | *dapE* (PP_1525) | succinyl‑DAP desuccinylase (3.5.1.18) |
| → ***meso*‑DAP** | ***dapF* (PP_3790 = Q88GD4; PP_5228)** | **DAP epimerase (5.1.1.7)** |
| → L‑lysine | *lysA* (PP_2077, PP_5227) | DAP decarboxylase (4.1.1.20) |

Critically, **no *ddh* (meso‑diaminopimelate dehydrogenase) gene was found**, so the dehydrogenase shortcut that some bacteria use to make *meso*‑DAP directly from THDP is absent. Therefore **DapF‑catalyzed epimerization is the only route to *meso*‑DAP** in KT2440, feeding both peptidoglycan biosynthesis and lysine production. This obligate position, combined with the essentiality of *meso*‑DAP for Gram‑negative cell‑wall cross‑linking, explains why the DAP/lysine pathway is a validated **antibacterial drug target** — the pathway "provides both lysine for protein synthesis and meso‑diaminopimelate for construction of the bacterial peptidoglycan cell wall" and is absent in mammals (Hutton et al. 2003, PMID 12570844; Girodeau et al. 1986, PMID 3086556).

**Paralogy note (mechanistically distinct paralogs).** KT2440 encodes **two divergent *dapF* paralogs** that appear to belong to *different mechanistic subclasses*: the target **PP_3790 (Q88GD4, 268 aa)** is a **putative DapF‑SS** (catalytic Ser70/Ser205), while **PP_5228 (Q88CF3, 276 aa)** is a **canonical DapF‑CC** (catalytic Cys75/Cys219). They share only ~38–40% pairwise identity (global Needleman‑Wunsch) yet carry identical UniProt FUNCTION/PATHWAY/localization annotations. PP_5228 lies adjacent to a *lysA* paralog (*lysA‑II*, PP_5227), suggesting a lysine‑operon‑associated copy, whereas PP_3790 is a stand‑alone locus. The physiological division of labor — and whether both are catalytically active in vivo — has not been experimentally resolved; the coexistence of a DapF‑CC and a DapF‑SS in one genome is itself a noteworthy observation.

---

## 7. Supported and Refuted Hypotheses

**Supported (by orthologous experimental evidence + Q88GD4 sequence/annotation):**
- H1 — DapF catalyzes LL‑DAP ⇌ *meso*‑DAP (EC 5.1.1.7): **Supported.**
- H2 — Cofactor‑independent (PLP‑independent) two‑base mechanism: **Supported.** (Refinement: for Q88GD4 the two‑base pair is inferred to be **serines, not cysteines** — a DapF‑SS enzyme; see §4.)
- H3 — Monomeric two‑domain fold with substrate‑induced domain closure: **Supported.**
- H4 — Narrow DAP substrate specificity (sub‑mM Km): **Supported.**
- H5 — Cytoplasmic localization: **Supported.**
- H6 — DapF is the obligate meso‑DAP source in KT2440 (no *ddh*): **Supported (bioinformatic).**

**Refuted / ruled out:**
- DapF is **not** PLP‑dependent (distinguishes it from Ala/Glu racemases).
- DapF is **not** the *phzF*‑type isomerase despite the shared fold (lacks that activity; different catalytic residues).

---

## 8. Evidence Quality and Limitations

- **Direct experimental evidence in *P. putida* KT2440 is lacking.** Q88GD4 is annotated PE:3 ("inferred from homology"). All kinetic/mechanistic/structural data come from well‑characterized orthologs (*E. coli*, *H. influenzae*) and family‑wide studies; transfer of these properties is justified by high family conservation (HAMAP MF_00197) but has not been verified with the *P. putida* enzyme itself.
- **Substrate‑specificity constants** (Km, Ki) are from *E. coli* DapF, not the *P. putida* protein.
- **Catalytic residues / DapF‑SS assignment:** the identification of Ser70/Ser205 as the catalytic pair (making Q88GD4 a DapF‑SS enzyme) is a **bioinformatic inference** from precise mapping to experimentally annotated orthologs plus the DapF‑SS literature. It has not been confirmed by an experimental *P. putida* structure or by mutagenesis, and the enzyme's activity has not been directly assayed.
- **Paralog function:** the physiological roles of PP_3790 (DapF‑SS) vs PP_5228 (DapF‑CC) — redundancy, differential expression, conditional use, or whether one is catalytically silent — are untested.

**Future directions:** recombinant expression and steady‑state kinetics of PP_3790 vs PP_5228; Ser70Ala/Ser205Ala (and Ser→Cys) mutagenesis to confirm the DapF‑SS catalytic pair; single/double knockouts to test DAP auxotrophy, essentiality, and functional redundancy; an experimental or AlphaFold structure to verify active‑site geometry.

---

## 9. Key References

- Koo & Blanchard 1999, *Biochemistry* — chemical mechanism of *H. influenzae* DAP epimerase (PMID 10194362).
- Cirilli et al. 1998, *Biochemistry* — first DapF crystal structure; two domains, catalytic Cys73/Cys217 (PMID 9843410).
- Pillai et al. 2007, *J. Mol. Biol.* — mutant structures; open/closed conformational cycle (PMID 17889830).
- Lam et al. 1988, *Biochemistry*/*J. Med. Chem.* — DAP analogs; Km and inhibitor Ki for *E. coli* DapF (PMID 3042781).
- Lamer et al. 2025 — DapF inhibition by slow‑binding α‑methyl amino acids (PMID 40299312); **DapF‑SS serine‑variant epimerases** (PMID 40774471) — the subclass to which Q88GD4 is assigned.
- Hutton et al. 2003, *Mini Rev. Med. Chem.* — lysine‑pathway enzymes as antibacterial targets (PMID 12570844).
- Girodeau et al. 1986 — DAP‑pathway inhibitors; DAP epimerase as target (PMID 3086556).
- UniProt Q88GD4 (HAMAP‑Rule MF_00197); Pfam PF01678; InterPro IPR001653; TIGR00652.


## Artifacts

- [OpenScientist final report](dapF__Q88GD4-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](dapF__Q88GD4-deep-research-openscientist_artifacts/final_report.pdf)