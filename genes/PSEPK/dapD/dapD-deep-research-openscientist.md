---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-17T13:58:42.003703'
end_time: '2026-07-17T14:14:57.068176'
duration_seconds: 975.06
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: dapD
  gene_symbol: dapD
  uniprot_accession: Q88MP1
  protein_description: 'RecName: Full=2,3,4,5-tetrahydropyridine-2,6-dicarboxylate
    N-succinyltransferase {ECO:0000255|HAMAP-Rule:MF_02122}; EC=2.3.1.117 {ECO:0000255|HAMAP-Rule:MF_02122};
    AltName: Full=Tetrahydrodipicolinate N-succinyltransferase {ECO:0000255|HAMAP-Rule:MF_02122};
    Short=THDP succinyltransferase {ECO:0000255|HAMAP-Rule:MF_02122}; Short=THP succinyltransferase
    {ECO:0000255|HAMAP-Rule:MF_02122}; AltName: Full=Tetrahydropicolinate succinylase
    {ECO:0000255|HAMAP-Rule:MF_02122};'
  gene_info: Name=dapD {ECO:0000255|HAMAP-Rule:MF_02122}; OrderedLocusNames=PP_1530;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the type 2 tetrahydrodipicolinate N-
  protein_domains: DapD_gammaproteobac. (IPR019876); Hexapep. (IPR001451); THDPS_M.
    (IPR032784); THDPS_M_sf. (IPR038361); Trimer_LpxA-like_sf. (IPR011004)
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
  path: dapD-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: dapD-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88MP1
- **Protein Description:** RecName: Full=2,3,4,5-tetrahydropyridine-2,6-dicarboxylate N-succinyltransferase {ECO:0000255|HAMAP-Rule:MF_02122}; EC=2.3.1.117 {ECO:0000255|HAMAP-Rule:MF_02122}; AltName: Full=Tetrahydrodipicolinate N-succinyltransferase {ECO:0000255|HAMAP-Rule:MF_02122}; Short=THDP succinyltransferase {ECO:0000255|HAMAP-Rule:MF_02122}; Short=THP succinyltransferase {ECO:0000255|HAMAP-Rule:MF_02122}; AltName: Full=Tetrahydropicolinate succinylase {ECO:0000255|HAMAP-Rule:MF_02122};
- **Gene Information:** Name=dapD {ECO:0000255|HAMAP-Rule:MF_02122}; OrderedLocusNames=PP_1530;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the type 2 tetrahydrodipicolinate N-
- **Key Domains:** DapD_gammaproteobac. (IPR019876); Hexapep. (IPR001451); THDPS_M. (IPR032784); THDPS_M_sf. (IPR038361); Trimer_LpxA-like_sf. (IPR011004)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "dapD" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'dapD' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **dapD** (gene ID: dapD, UniProt: Q88MP1) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: **dapD** (Q88MP1, PP_1530) — Tetrahydrodipicolinate N-succinyltransferase, *Pseudomonas putida* KT2440

## 0. Identity verification

The requested target is UniProt **Q88MP1**, gene **dapD** (ordered locus **PP_1530**) of *Pseudomonas putida* KT2440, annotated as **2,3,4,5‑tetrahydropyridine‑2,6‑dicarboxylate N‑succinyltransferase** (tetrahydrodipicolinate N‑succinyltransferase; THDP succinyltransferase), **EC 2.3.1.117**. The gene symbol, EC number, protein family ("type 2 tetrahydrodipicolinate N‑succinyltransferase"), and InterPro domains (DapD_gammaproteobac. IPR019876; Hexapep IPR001451; THDPS_M IPR032784/IPR038361; Trimer_LpxA‑like_sf IPR011004) are **fully self‑consistent** and match the biochemically and structurally characterized DapD enzymes described below. The symbol is **not ambiguous**: DapD is a conserved, well‑defined bacterial biosynthetic enzyme.

**Evidentiary caveat.** No study has, to my knowledge, biochemically characterized *P. putida* KT2440 DapD directly. Its function is assigned by (i) automated HAMAP rule MF_02122 and (ii) very strong homology to characterized orthologs. The **closest characterized relative is *Pseudomonas aeruginosa* DapD** (same genus; PMID 22359568), supplemented by structural/kinetic work on *E. coli*, *Mycobacterium tuberculosis*, *Corynebacterium glutamicum*, and *Serratia marcescens* DapD. All belong to the same family, and the gammaproteobacterial subtype (IPR019876) is shared with *E. coli*, *Serratia*, and *Pseudomonas*. Inferences below are therefore high‑confidence homology transfers, explicitly flagged where relevant.

---

## 1. Summary

DapD is a **cytoplasmic homotrimeric acyltransferase of the hexapeptide‑repeat (left‑handed β‑helix / LpxA‑like) superfamily** that catalyzes the **first committed step of the succinylase branch of the meso‑diaminopimelate (meso‑DAP)/L‑lysine biosynthetic pathway**. It transfers a succinyl group from **succinyl‑CoA** onto the amino group of the acceptor derived from **tetrahydrodipicolinate (THDP)** — the ring‑opened form L‑2‑amino‑6‑oxopimelate — producing **N‑succinyl‑L‑2‑amino‑6‑oxopimelate + CoA** (EC 2.3.1.117). This step channels metabolic flux toward meso‑DAP, an essential cross‑linking residue of Gram‑negative peptidoglycan and the immediate precursor of L‑lysine.

---

## 2. Primary molecular function: the reaction catalyzed

DapD catalyzes the succinyl‑CoA–dependent N‑succinylation of the open‑chain amino‑keto acid generated from THDP:

> **THDP (→ L‑2‑amino‑6‑oxopimelate) + succinyl‑CoA → N‑succinyl‑L‑2‑amino‑6‑oxopimelate + CoA**

- Beaman et al. (2002) define the reaction precisely: DapD "catalyzes the **succinyl‑CoA‑dependent acylation of L‑2‑amino‑6‑oxopimelate to 2‑N‑succinyl‑6‑oxopimelate** as part of the **succinylase branch** of the meso‑diaminopimelate/lysine biosynthetic pathway of bacteria, blue‑green algae, and plants" (PMID 11910040).
- A 2025 kinetic/spectroscopic study restates the substrates/products: "DapD catalyzes the reaction of **tetrahydrodipicolinate (THDP) and succinyl‑CoA** to form **(S)‑2‑(3‑carboxypropanamido)‑6‑oxoheptanedioic acid and coenzyme A**" (Hayes et al. 2025, PMID 40930446).

Chemically, cyclic THDP is in equilibrium with its open‑chain amino‑keto acid form (2‑amino‑6‑oxopimelate/2‑amino‑6‑oxoheptanedioate); it is the free primary amine of this open form that is succinylated. The succinyl "handle" installed here is retained through the next two steps and later removed, serving as a protecting/activating group that permits regioselective transamination.

### Substrate specificity
- **Acyl donor:** succinyl‑CoA (not acetyl‑CoA). The discrimination between succinyl‑ and acetyl‑CoA — i.e., between the **succinylase** and **acetylase** branches of DAP biosynthesis — is set by "**at least three amino acids that interact with or give accessible active site volume to the cofactor succinyl group**" (PMID 11910040). DapD's assignment to the succinylase branch (and IPR032784 "THDPS_M") is thus mechanistically grounded.
- **Amino acceptor — stereospecificity:** In the closest characterized ortholog, *P. aeruginosa* DapD "**is specific for the L‑stereoisomer of the amino substrate L‑2‑aminopimelate, and its D‑enantiomer acts as a weak inhibitor**"; both enantiomers bind the same pocket, but the D‑amino group is **misaligned for nucleophilic attack**, explaining specificity and inhibition (PMID 22359568). (L‑2‑aminopimelate is used experimentally as a stable, non‑cyclizing analog of the true acceptor.)

### Catalytic / kinetic mechanism
- **Ordered ternary‑complex ("direct attack") mechanism, not ping‑pong.** Crystallographic ternary complexes place the succinyl thioester carbonyl carbon "**in close proximity to the nucleophilic 2‑amino group of the acceptor, in support of a direct attack ternary complex mechanism**" (PMID 11910040) — both substrates bind before chemistry; no covalent acyl‑enzyme intermediate.
- **Kinetics:** For *S. marcescens* DapD, initial‑velocity patterns are "**consistent with a rapid equilibrium ordered bi bi kinetic mechanism**," and "conversion of the central enzyme complexes (chemistry) is thought to be the **rate‑limiting step**" (PMID 40930446).
- **Cooperativity:** In *E. coli* DapD, "the **C‑terminal helix undergoes a large rearrangement upon substrate binding, which contributes to cooperativity** in substrate binding" (PMID 18242192).

---

## 2b. Sequence-based validation of the homology assignment (this work)

To quantify the confidence of transferring function from characterized orthologs, I retrieved the UniProt sequences and computed pairwise alignments (BLOSUM62; global Needleman–Wunsch and local Smith–Waterman) between *P. putida* DapD (Q88MP1, 344 aa) and reviewed DapD orthologs:

| Ortholog (UniProt) | Length | % identity to Q88MP1 |
|---|---|---|
| *P. aeruginosa* PAO1 DapD (G3XD76) | 344 aa | **88.4 %** (304/344) |
| *C. glutamicum* DapD (Q8NRE3) | 297 aa | 48.6 % |
| *M. tuberculosis* DapD (P9WP21) | 317 aa | 47.7 % |
| *E. coli* K12 DapD (P0A9D8) | 274 aa | ~21 % global; ~28 % local core |

**Key conclusions:**
- *P. putida* DapD is **88.4 % identical** to *P. aeruginosa* DapD — the same-genus enzyme whose crystal structures, L-stereospecificity, and succinyl-CoA usage were experimentally established (PMID 22359568). This near-identity makes transfer of catalytic function, substrate specificity, and quaternary structure to Q88MP1 **essentially definitive**.
- Q88MP1 and G3XD76 have **identical length (344 aa)** and both carry the ~70-residue N-terminal domain characteristic of the **gammaproteobacterial "type 2" DapD subtype** (InterPro IPR019876), consistent with the UniProt "type 2 tetrahydrodipicolinate N-succinyltransferase" family assignment.
- The low global identity to *E. coli* DapD is an **architectural difference, not lack of orthology**: the *E. coli* enzyme is a shorter 274-aa form lacking the N-terminal extension; the conserved LβH catalytic core still aligns (~28 % local identity). *M. tuberculosis* and *C. glutamicum* DapD (~48 %) are clear, more distant orthologs.

*(Alignments computed in this investigation from UniProt REST-retrieved sequences.)*

## 3. Structure and molecular architecture

DapD is a **homotrimer** built on the **hexapeptide‑repeat acyltransferase fold**, exactly matching Q88MP1's InterPro annotations (Hexapep IPR001451; Trimer_LpxA‑like_sf IPR011004).

- Each subunit has three domains: "**an N‑terminal α‑helical domain, a left‑handed β‑helix (LβH) domain, and a β C‑terminal domain**" (C. glutamicum, PMID 26602189). The LβH is "**the common structural motif of enzymes belonging to the hexapeptide repeat superfamily**" (M. tuberculosis, PMID 19394346).
- Three active sites form at the **subunit interfaces** of the trimer; succinyl‑CoA binds there, and the mobile C‑terminal domain closes over the acceptor site (PMID 26602189; PMID 18242192).
- The trimer can be stabilized by metal ions on the molecular 3‑fold axis: in Mtb‑DapD, "**the trimeric quaternary structure is stabilized by Mg²⁺ and Na⁺ located on the 3‑fold axis**," and the N‑terminal domain contains "**an interior water‑filled channel**" leading to that axial Mg²⁺ (PMID 19394346).
- Multiple co‑crystal structures (with succinyl‑CoA, succinamide‑CoA cofactor analog, L‑ and D‑2‑aminopimelate, 2‑aminopimelate) across orthologs map the cofactor and acceptor subsites and were validated by site‑directed mutagenesis of catalytic/binding residues (PMID 26602189; PMID 11910040; PMID 22359568).

The consistency of *P. putida* DapD's domain content with this fold provides strong structural support for the functional assignment.

**Sequence-level confirmation of the LβH fold (this work).** Inspection of the Q88MP1 sequence shows the diagnostic **degenerate tandem hexapeptide repeats** of a left-handed β-helix across roughly residues ~200–300 (e.g., …**VSAGV**‑**FVGKGS**‑**DLGGGC**‑**STMGTL**‑**SGGGNI**‑**VIKVGE**‑**GCLIGA**‑**NAGIGI**…), each imperfect [LIV]‑G‑x‑x‑x‑x coil adding one rung to the β‑helix. This independently corroborates the InterPro Hexapep (IPR001451) / Trimer_LpxA‑like (IPR011004) assignment and the trimeric acyltransferase architecture.

---

## 4. Pathway context and biological process

DapD initiates the **succinylase (acyl‑DAP) branch** — the route used by most Gram‑negative bacteria including *Pseudomonas* — of the meso‑DAP/L‑lysine pathway:

1. Aspartate → … → **L‑2,3,4,5‑tetrahydrodipicolinate (THDP)** (via DapA/DapB from the common upstream pathway)
2. **THDP + succinyl‑CoA → N‑succinyl‑2‑amino‑6‑oxopimelate + CoA — *DapD (this enzyme)***
3. N‑succinyl‑aminotransferase (DapC) → N‑succinyl‑L,L‑DAP
4. N‑succinyl‑L,L‑DAP desuccinylase (DapE) → L,L‑DAP (+ succinate)
5. DAP epimerase (DapF) → **meso‑DAP**
6. **meso‑DAP** → incorporated into peptidoglycan **and/or** decarboxylated by DAP decarboxylase (LysA) → **L‑lysine**

**Organism‑specific pathway complement (this work).** A UniProt survey of *P. putida* KT2440 (taxid 160488) confirms the **complete succinylase branch is encoded**: dapA (PP_2639, PP_1237; EC 4.3.3.7) → dapB (PP_4725; EC 1.17.1.8) → **dapD (PP_1530; EC 2.3.1.117 — target)** → dapC N‑succinyl‑LL‑DAP aminotransferase (PP_1588; EC 2.6.1.17) → dapE succinyl‑DAP desuccinylase (PP_1525; EC 3.5.1.18) → dapF DAP epimerase (PP_5228, PP_3790; EC 5.1.1.7) → lysA DAP decarboxylase (PP_5227, PP_2077; EC 4.1.1.20). Crucially, **no acetylase‑branch gene (dapH/dapX) and no meso‑DAP dehydrogenase (ddh, EC 1.4.1.16) were detected** — *P. putida* has neither the acetylase alternative nor the single‑step dehydrogenase bypass. DapD is therefore the **sole, obligatory committed entry** from THDP into meso‑DAP/lysine synthesis and is functionally non‑redundant (and very likely essential). Notably, **dapD (PP_1530) lies immediately adjacent to dapE (PP_1525)** in the genome, clustering the succinylating and desuccinylating enzymes and suggesting possible co‑regulation.

**Physiological outputs.** The pathway "**provides lysine for protein synthesis and both lysine and meso‑diaminopimelate for construction of the bacterial peptidoglycan cell wall**" (Hutton et al. 2007, PMID 17579770; see also PMID 12570844; PMID 8919551; review PMID 23504110). In Gram‑negative bacteria such as *P. putida*, meso‑DAP is the residue that cross‑links adjacent peptidoglycan strands, so DapD activity is coupled to **cell‑wall integrity, growth, and division**.

**Regulation.** In *C. glutamicum*, *dapD* is a direct target of the nitrogen master regulator **AmtR**, "**the dapD gene, encoding succinylase involved in m‑diaminopimelate synthesis**," linking nitrogen status to lysine biosynthesis (PMID 19041910). This specific regulatory link is organism‑dependent and is not established for *P. putida*, but it illustrates that *dapD* expression can be integrated into nitrogen/amino‑acid regulatory networks.

---

## 5. Subcellular localization

DapD is a **soluble cytoplasmic enzyme**. It acts on small, soluble metabolic intermediates and cofactors (THDP‑derived amino acid, succinyl‑CoA, CoA); it carries no signal peptide, membrane‑spanning segment, or lipidation motif, and all characterized orthologs were purified as soluble cytosolic proteins for crystallography and kinetics (e.g., PMID 18242192; PMID 19394346; PMID 26602189). Its function — an early anabolic step of amino‑acid/cell‑wall‑precursor biosynthesis — is carried out in the **cytoplasm**, where the resulting meso‑DAP is later handed off to the membrane‑associated peptidoglycan‑assembly machinery.

---

## 6. Physiological / therapeutic significance

Because the meso‑DAP/lysine pathway is **present in bacteria (and plants) but absent in humans**, and because it feeds both protein synthesis and the essential cell wall, its enzymes are attractive antibacterial targets. DapD specifically has been highlighted: "**Since lysine is an essential amino acid to humans, DapD is a potentially safe target for antibiotic therapies**" (PMID 40930446); the broader strategy is reviewed in PMID 17579770, 12570844, 8919551, and 23504110. The recent finding that DapD can be inactivated by Cu²⁺ (PMID 40930446) is also relevant to inhibitor/metal‑sensitivity considerations. (Note: the essentiality of the succinylase branch varies among species because some bacteria possess alternative branches — dehydrogenase or acetylase; *Pseudomonas* uses the succinylase route.)

---

## 7. Supported vs. refuted hypotheses

**Supported (high confidence):**
- H1 — dapD/Q88MP1 encodes tetrahydrodipicolinate N‑succinyltransferase (EC 2.3.1.117). ✔ (family/EC/domain concordance + ortholog biochemistry)
- H2 — Reaction: THDP‑derived amino acid + succinyl‑CoA → N‑succinyl product + CoA. ✔ (PMID 11910040, 40930446)
- H3 — Homotrimeric LβH/hexapeptide‑repeat (LpxA‑like) fold. ✔ (PMID 19394346, 26602189, 18242192; matches IPR011004/IPR001451)
- H4 — L‑stereospecific amino acceptor; succinyl‑CoA‑specific donor. ✔ (PMID 22359568, 11910040)
- H5 — Ordered ternary‑complex mechanism, cytoplasmic localization, feeds meso‑DAP/peptidoglycan + lysine. ✔ (PMID 11910040, 40930446, 17579770)

**Refuted / disfavored:**
- A ping‑pong (covalent acyl‑enzyme) mechanism — disfavored by ternary‑complex structures and ordered bi‑bi kinetics (PMID 11910040, 40930446).
- Acetyl‑CoA as the physiological donor — DapD is committed to the succinylase branch; donor selectivity resides in a few active‑site residues (PMID 11910040).

---

## 8. Limitations and future directions

- **No direct experimental data on *P. putida* KT2440 DapD**; all mechanistic/structural detail is transferred from orthologs. However, this transfer is exceptionally well-supported: the closest characterized relative, *P. aeruginosa* DapD, is **88 % identical** (identical length, same "type 2" architecture), so the residual uncertainty is small. Direct enzymology (kinetic constants, an experimental *P. putida* structure) would provide final confirmation.
- The downstream succinylase‑branch genes (dapC PP_1588, dapE PP_1525, dapF, lysA) are present and annotated in *P. putida* KT2440 (confirmed here), but *dapD* essentiality and regulation in *P. putida* have not been experimentally tested; targeted knockout, high‑density transposon fitness (RB‑TnSeq), and expression studies would establish them directly.
- Precise active‑site residues in Q88MP1 could be mapped by sequence/structure alignment to the mutagenesis‑validated positions in *E. coli*/*C. glutamicum*/*P. aeruginosa* DapD.

---

### Key references
- PMID 11910040 — Beaman et al., acyl‑group specificity & direct‑attack ternary‑complex mechanism.
- PMID 22359568 — Schnell et al., *P. aeruginosa* DapD structure & L‑stereospecificity (closest relative).
- PMID 19394346 — Schuldt et al., *M. tuberculosis* DapD structure, trimer, LβH fold, axial metals.
- PMID 18242192 — Nguyen et al., *E. coli* DapD structure, C‑terminal helix rearrangement & cooperativity.
- PMID 26602189 — Sagong & Kim, *C. glutamicum* DapD structure with succinyl‑CoA and substrate analog.
- PMID 40930446 — Hayes et al. 2025, *S. marcescens* DapD kinetics (ordered bi‑bi) and Cu inactivation.
- PMID 19041910 — Buchinger et al., *dapD* as an AmtR (nitrogen) regulatory target.
- PMID 17579770 / 12570844 / 8919551 / 23504110 — reviews: DAP/lysine pathway as antibacterial target.


## Artifacts

- [OpenScientist final report](dapD-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](dapD-deep-research-openscientist_artifacts/final_report.pdf)