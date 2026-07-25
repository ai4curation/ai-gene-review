---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-18T16:41:33.334756'
end_time: '2026-07-18T17:00:52.642170'
duration_seconds: 1159.31
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: ispH
  gene_symbol: ispH
  uniprot_accession: Q88Q89
  protein_description: 'RecName: Full=4-hydroxy-3-methylbut-2-enyl diphosphate reductase
    {ECO:0000255|HAMAP-Rule:MF_00191}; Short=HMBPP reductase {ECO:0000255|HAMAP-Rule:MF_00191};
    EC=1.17.7.4 {ECO:0000255|HAMAP-Rule:MF_00191};'
  gene_info: Name=ispH {ECO:0000255|HAMAP-Rule:MF_00191}; OrderedLocusNames=PP_0606;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the IspH family. {ECO:0000255|HAMAP-
  protein_domains: LytB/IspH. (IPR003451); LYTB (PF02401)
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
citation_count: 12
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: ispH-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: ispH-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88Q89
- **Protein Description:** RecName: Full=4-hydroxy-3-methylbut-2-enyl diphosphate reductase {ECO:0000255|HAMAP-Rule:MF_00191}; Short=HMBPP reductase {ECO:0000255|HAMAP-Rule:MF_00191}; EC=1.17.7.4 {ECO:0000255|HAMAP-Rule:MF_00191};
- **Gene Information:** Name=ispH {ECO:0000255|HAMAP-Rule:MF_00191}; OrderedLocusNames=PP_0606;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the IspH family. {ECO:0000255|HAMAP-
- **Key Domains:** LytB/IspH. (IPR003451); LYTB (PF02401)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ispH" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ispH' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ispH** (gene ID: ispH, UniProt: Q88Q89) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: IspH (Q88Q89, PP_0606) in *Pseudomonas putida* KT2440

**Gene:** *ispH* (also historically *lytB*) · **UniProt:** Q88Q89 (ISPH_PSEPK) · **Locus:** PP_0606
**Protein:** 4-hydroxy-3-methylbut-2-enyl diphosphate reductase (HMBPP reductase) · **EC 1.17.7.4**
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / KT2440), PSEPK
**Family:** IspH family · LytB/IspH domain (IPR003451, Pfam PF02401)

---

## Summary

**IspH (Q88Q89, encoded by *ispH*/PP_0606) is the terminal enzyme of the 2-*C*-methyl-D-erythritol 4-phosphate (MEP, or non-mevalonate/DOXP) pathway of isoprenoid biosynthesis in *Pseudomonas putida* KT2440.** It is an oxygen-sensitive [4Fe-4S] metalloenzyme (EC 1.17.7.4) that catalyzes the 2-electron/2-proton reductive dehydroxylation of (E)-4-hydroxy-3-methylbut-2-enyl diphosphate (HMBPP), eliminating the C4 hydroxyl group as water and producing the two universal five-carbon isoprenoid precursors: isopentenyl diphosphate (IPP) and dimethylallyl diphosphate (DMAPP), in an approximately 4–6:1 ratio. Reduced [2Fe-2S] ferredoxin serves as the physiological electron donor.

The enzyme is a soluble, cytoplasmic protein (no signal peptide or transmembrane segment), consistent with the requirement of a reducing intracellular environment to protect its labile Fe–S cluster. Catalysis occurs at a unique "apical" fourth iron of a cubane [4Fe-4S] cluster ligated by three conserved cysteines (Cys12/Cys96/Cys198 in the *P. putida* sequence). HMBPP binds directly to this apical iron, and the reaction proceeds through an organometallic (η²-metallacycle) intermediate coupled to a threonine-mediated proton relay. Because *P. putida* synthesizes all of its IPP and DMAPP exclusively through the MEP pathway (it lacks the mevalonate pathway), IspH is an essential, non-redundant metabolic node. As the MEP pathway is absent in humans, IspH is a validated and actively pursued target for the development of new antibacterial and antimalarial drugs.

The functional assignment of Q88Q89 as an authentic IspH is supported by **seven converging lines of evidence**: (1) the biochemically and structurally characterized function of the IspH/LytB family; (2) conservation of the three catalytic cluster cysteines and the proton-donor residue in the *P. putida* sequence; (3) conserved genomic synteny (an *ileS–lspA–PPIase–ispH* cluster mirroring the *E. coli* arrangement); (4) a very high-confidence AlphaFold structural model (mean pLDDT 96.2); (5) a 0.31 Å backbone superposition of that model onto the experimental *E. coli* IspH:HMBPP complex; (6) UniProt/HAMAP domain and catalytic-site annotation; and (7) organism-specific metabolic-engineering evidence establishing the MEP pathway as the sole isoprenoid-precursor route in *P. putida* KT2440.

---

## Gene/Protein Identity Verification

Per the mandatory verification protocol, the gene symbol, organism, family, and domain annotations were all cross-checked and **confirmed to be internally consistent and matched by the literature**:

| Check | Expected (UniProt) | Finding |
|---|---|---|
| Gene symbol matches protein description | *ispH* = HMBPP reductase | ✅ Confirmed — *ispH*/*lytB* universally denotes HMBPP reductase (EC 1.17.7.4) |
| Organism | *P. putida* KT2440 (PSEPK) | ✅ Confirmed — locus PP_0606; MEP pathway verified in this exact strain (PMID 31500633) |
| Protein family / domains | IspH family, LytB/IspH (PF02401) | ✅ Confirmed — three cluster cysteines and fold conserved |
| Risk of symbol ambiguity | — | ✅ Low — "IspH", "LytB" and "HDR" are synonyms for the *same* enzyme across bacteria, plants and protozoa |

The literature is **abundant and directly relevant**. While most detailed mechanistic and structural studies were performed on the *E. coli*, *Aquifex aeolicus* and *Plasmodium falciparum* orthologues rather than on the *P. putida* protein specifically, the very high sequence identity (67% to *E. coli* IspH over the aligned core) and near-identical predicted fold justify transferring these mechanistic conclusions to Q88Q89 with high confidence. No conflicting "same-symbol, different-gene" literature was encountered.

---

## Key Findings

### Finding 1 — IspH catalyzes the terminal step of the MEP pathway: reductive dehydroxylation of HMBPP to IPP + DMAPP

IspH (LytB/HDR, EC 1.17.7.4) catalyzes the **last of the seven steps** of the MEP (DOXP/non-mevalonate) pathway. It performs a two-electron, two-proton reductive dehydroxylation of (E)-4-hydroxy-3-methylbut-2-enyl diphosphate (HMBPP): the C4 hydroxyl group is eliminated as water, generating a mixture of the two universal C5 isoprenoid building blocks, **isopentenyl diphosphate (IPP)** and **dimethylallyl diphosphate (DMAPP)**. In bacterial enzymes the products are formed in an approximately **4–6:1 IPP:DMAPP ratio**.

This assignment for Q88Q89 rests on HAMAP-Rule MF_00191 (IspH family, PF02401) applied on the basis of strong sequence and domain homology to biochemically characterized bacterial IspH enzymes. The reaction chemistry is directly established in the literature: *"[IspH] catalyzes the terminal step of the MEP/DOXP pathway where it converts (E)-4-hydroxy-3-methylbut-2-enyl diphosphate (HMBPP) into the two products, isopentenyl diphosphate and dimethylallyl diphosphate. The reaction involves the reductive elimination of the C4 hydroxyl group, using a total of two electrons"* ([PMID: 22646150](https://pubmed.ncbi.nlm.nih.gov/22646150/)). The product ratio and pathway placement are corroborated by studies noting *"the reductive dehydroxylation of HMBPP to isopentenyl diphosphate (IPP) and dimethylallyl diphosphate (DMAPP) in the last step of methylerythritol phosphate (MEP) pathway… known to produce 4-6:1 ratio of IPP and DMAPP mixture by the last enzyme, IspH"* ([PMID: 28139297](https://pubmed.ncbi.nlm.nih.gov/28139297/)).

**The catalyzed reaction:**

```
HMBPP  +  2 e⁻  +  2 H⁺   ──IspH [4Fe-4S]──►   IPP  +  DMAPP (~4–6:1)  +  H₂O
(E)-4-hydroxy-3-methyl-                          isopentenyl-PP + dimethylallyl-PP
but-2-enyl diphosphate
```

### Finding 2 — IspH is an oxygen-sensitive [4Fe-4S] metalloenzyme using an apical-iron / organometallic mechanism with a Thr proton relay

Extensive spectroscopic (EPR, Mössbauer, NRVS) and crystallographic studies of the *E. coli* and *A. aeolicus* enzymes establish that catalytically active IspH carries a **cubane [4Fe-4S]²⁺ cluster (not [3Fe-4S])** ligated by three conserved cysteines. This leaves a **unique "apical" fourth iron** (of the aconitase type) that binds three water/hydroxide ligands in the resting enzyme. HMBPP binds directly to this apical iron through its C4–OH group (alkoxide coordination), and the cluster is the **direct electron source** for the reaction. Crystal structures of substrate, converted-substrate, product and pyrophosphate complexes reveal a **hairpin substrate conformation** and a hydrogen-bonding network that acts as a proton reservoir via a **Thr167 proton relay** (*E. coli* numbering). Mechanistic evidence (X-ray, Mössbauer, DFT/QM-MM) favors an **organometallic (η²-metallacycle/allyl) intermediate** over a purely inner-sphere alkoxide (Birch-type) pathway. The solvent-exposed Fe–S active site makes the enzyme oxygen-sensitive.

Supporting quotes: *"the active form of IspH contains a [4Fe-4S] cluster and not the [3Fe-4S] form… the cluster is the direct electron source for the reaction and… a reaction intermediate is bound directly to the cluster"* ([PMID: 22646150](https://pubmed.ncbi.nlm.nih.gov/22646150/)); *"an unusual [4Fe-4S]²⁺ cluster is attached to the protein by three conserved cysteines and contains a hexacoordinated iron linked to three sulfurs of the cluster and three additional oxygen or nitrogen ligands"* ([PMID: 19708647](https://pubmed.ncbi.nlm.nih.gov/19708647/)); *"The IspH:substrate complex reveals a hairpin conformation of the ligand with the C(1) hydroxyl group coordinated to the unique site in a [4Fe-4S] cluster of aconitase type… coupled to a hydrogen-bonding network, which serves as proton reservoir via a Thr167 proton relay"* ([PMID: 20080550](https://pubmed.ncbi.nlm.nih.gov/20080550/)); and *"the last two enzymes of this pathway, IspG and IspH, are [Fe4S4] proteins that are not produced by humans and catalyze 2 H⁺/2 e⁻ reductions with novel mechanisms"* ([PMID: 24481599](https://pubmed.ncbi.nlm.nih.gov/24481599/)). The organometallic η²-bound intermediate is further supported by broken-symmetry DFT computations showing that η²-bound states are lower in energy than ROH-bound states upon one-electron reduction ([PMID: 26098647](https://pubmed.ncbi.nlm.nih.gov/26098647/)).

### Finding 3 — In *P. putida* KT2440 the MEP pathway is the sole source of IPP/DMAPP; IspH is essential and human-absent, making it an antimicrobial target

Metabolic-engineering work in the **exact source strain**, *P. putida* KT2440, confirms that the isoprenoid precursors IPP and DMAPP are produced from pyruvate and glyceraldehyde-3-phosphate **exclusively via the MEP pathway** — the organism lacks the alternative mevalonate (MVA) pathway. As the terminal MEP enzyme, IspH is therefore the committed, non-redundant producer of *both* IPP and DMAPP that feed downstream cytoplasmic prenyltransferases (for quinones, carotenoids, bactoprenol/undecaprenyl phosphate, tRNA prenylation, etc.). The MEP pathway is essential in most bacteria but **absent in humans and animals**, which is why IspH is actively pursued as an antibacterial/antimalarial drug target; inhibitor-bound crystal structures (e.g., with the HMBPP analogues TMBPP and AMBPP) have been solved to guide rational design.

Supporting quotes: *"In P. putida and most other bacteria, these precursors are produced from pyruvate and glyceraldehyde 3-phosphate by the methylerythritol 4-phosphate (MEP) pathway, whereas other bacteria synthesize the same precursors from acetyl-CoA using the unrelated mevalonate (MVA) pathway"* ([PMID: 31500633](https://pubmed.ncbi.nlm.nih.gov/31500633/)); *"The absence of this pathway in mammalians makes it an interesting target for the discovery of novel anti-infectives. As last enzyme of this pathway, IspH is an oxygen sensitive [4Fe-4S] metalloenzyme"* ([PMID: 35163971](https://pubmed.ncbi.nlm.nih.gov/35163971/)); and *"IspH, also called LytB, a protein involved in the biosynthesis of isoprenoids through the methylerythritol phosphate pathway, is an attractive target for the development of new antimicrobial drugs"* ([PMID: 28862365](https://pubmed.ncbi.nlm.nih.gov/28862365/)).

### Finding 4 — Sequence-level confirmation: conserved cluster cysteines, proton donor, and [2Fe-2S] ferredoxin electron donor

The 315-residue *P. putida* IspH sequence (Q88Q89, ISPH_PSEPK) was retrieved and analyzed. It contains only four cysteines, three of which — **Cys12, Cys96 and Cys198** — occupy the exact positions of the [4Fe-4S] cluster-ligating cysteines of characterized bacterial IspH (*E. coli* Cys12/Cys96/Cys197), confirming the conserved 3-Cys/apical-iron architecture. UniProt annotates residue **126 as the catalytic proton donor** and lists substrate (HMBPP/IPP/DMAPP; ChEBI 128753/57623/128769) binding residues at positions 41, 74, 124, 168, 226–228 and 270. The two annotated catalytic-activity reactions (RHEA:24488 and RHEA:24825) explicitly consume/produce reduced/oxidized **[2Fe-2S]-ferredoxin**, identifying reduced [2Fe-2S] ferredoxin as the physiological electron donor. UniProt/HAMAP assigns the reaction as isopentenyl-diphosphate biosynthesis step 6/6 (DXP pathway) and dimethylallyl-diphosphate biosynthesis step 1/1. No signal peptide or transmembrane segment is present.

The ferredoxin electron-donor assignment is independently supported by structural work on the *Plasmodium falciparum* orthologue: *"Its distinct electron donor [2Fe-2S] ferredoxin was modeled to its binding site by docking calculations"* ([PMID: 24188825](https://pubmed.ncbi.nlm.nih.gov/24188825/)). The three-cysteine ligation is confirmed by in vivo Mössbauer studies: *"an unusual [4Fe-4S]²⁺ cluster is attached to the protein by three conserved cysteines"* ([PMID: 19708647](https://pubmed.ncbi.nlm.nih.gov/19708647/)).

### Finding 5 — PP_0606 lies in a conserved *ileS–lspA–PPIase–ispH* gene cluster mirroring the *E. coli* context

KEGG genome analysis of the PP_0606 neighborhood (~710–715 kb on the KT2440 chromosome) shows the gene order: **PP_0603 *ileS*** (isoleucyl-tRNA synthetase, K01870) → **PP_0604 *lspA*** (lipoprotein signal peptidase II, K03101) → **PP_0605 *slpA*/*fkpB*** (FKBP-type peptidyl-prolyl cis-trans isomerase, K03774) → **PP_0606 *ispH*** (K03527, EC 1.17.7.4), all on the forward strand, with *ispH* ending immediately before the divergently oriented *fimT* (PP_0607). *ispH* begins only ~15 bp after the end of PP_0605, consistent with tight linkage. This **ileS–lspA–(fkpB)–ispH** arrangement recapitulates the well-known genomic context of *ispH*/*lytB* in *Escherichia coli*, where the gene sits immediately downstream of the *ileS–lspA* locus. Conserved synteny across distantly related γ-proteobacteria provides strong evolutionary evidence that PP_0606 is a genuine *ispH* orthologue rather than a paralogue or mis-annotation.

### Finding 6 — AlphaFold model is very high confidence with all catalytic residues confidently placed

The AlphaFold DB monomer model **AF-Q88Q89-F1** (v6, AlphaFold Monomer v2.0) has a global **mean pLDDT of 96.19**, with 94.9% of residues at very-high confidence (pLDDT ≥ 90), 98.4% confident (≥ 70), and only 1.0% very-low (< 50, confined to a short terminal/loop region). All functionally assigned residues are modeled at very-high confidence: the three cluster cysteines **Cys12 (98.2), Cys96 (98.5), Cys198 (97.9)**; proton-donor **residue 126 (98.5)**; and HMBPP-binding residues 41 (97.1), 74 (98.0), 124 (96.8), 168 (98.4), 226 (97.7) and 270 (97.2). This confirms the protein is confidently predicted to adopt the compact three-domain "cloverleaf" α/β fold characteristic of the IspH family, with a fully formed central active-site pocket at the domain interface where the [4Fe-4S] cluster and substrate sit.

### Finding 7 — Q88Q89 superposes on the experimental *E. coli* IspH:HMBPP structure at 0.31 Å backbone RMSD

Phenix `superpose_pdbs` alignment of the AlphaFold model of Q88Q89 onto the experimental ***E. coli* IspH:HMBPP complex (PDB 3KE8**, Gräwert et al. 2010) gave a global sequence alignment of **67.1% identity over 208 aligned residues** and, after least-squares fitting, a backbone (N, Cα, C) **RMSD of 0.307 Å** on the 210-atom core (0.799 Å over all 518 matching atoms) — excellent agreement (< 1 Å). The alignment shows conservation of the diagnostic IspH sequence motifs, including the N-terminal cluster-cysteine motif …NPRGF-**C12**-AGVDRAI…, the FDAT-**C96**-PLVT motif, and the DDI-**C198**-YAT motif — i.e., all three [4Fe-4S]-ligating cysteines align and structurally superimpose with those of *E. coli* IspH bound to its natural substrate. The reference structure derives from the crystallographic study reporting *"five crystal structures of IspH in complex with substrate, converted substrate, products and PP(i)"* ([PMID: 20080550](https://pubmed.ncbi.nlm.nih.gov/20080550/)). This near-identity of the catalytic scaffold to a substrate-bound experimental structure is the strongest single piece of structural evidence that Q88Q89 catalyzes the same reaction on the same substrate.

---

## Mechanistic Model / Interpretation

The evidence assembles into a coherent, high-confidence mechanistic picture of IspH function in *P. putida* KT2440.

### Pathway context

```
Glycolysis
  pyruvate + glyceraldehyde-3-phosphate
        │  DXS (Dxs)
        ▼
  1-deoxy-D-xylulose 5-phosphate (DXP)
        │  DXR/IspC
        ▼
  2-C-methyl-D-erythritol 4-phosphate (MEP)
        │  IspD → IspE → IspF → IspG
        ▼
  (E)-4-hydroxy-3-methylbut-2-enyl diphosphate (HMBPP)
        │
        │   ★ IspH / PP_0606 / Q88Q89   [4Fe-4S], 2e⁻/2H⁺
        ▼
  IPP  +  DMAPP   (~4–6:1)
        │
        ▼
  Downstream prenyltransferases → quinones (ubiquinone, menaquinone),
  carotenoids, bactoprenol (undecaprenyl-P for peptidoglycan/LPS),
  prenylated tRNA, hopanoids, etc.
```

IspH sits at the **committed branch point** where a single linear precursor (HMBPP) is converted into the two isomeric building blocks that seed *all* isoprenoid biosynthesis. Because *P. putida* has no mevalonate pathway (Finding 3), there is no metabolic bypass — IspH activity is strictly required for viability, and its product ratio (~4–6:1 IPP:DMAPP; Finding 1) sets the initial supply balance of the two precursors, which is subsequently re-equilibrated by IPP isomerase (Idi) where present.

### Catalytic mechanism at the active site

```
         Cys12   Cys96   Cys198        (3 protein cysteines)
            \      |      /
             [4Fe-4S]²⁺ cubane cluster
                   |
              apical Fe (4th, "unique" iron)
                   |
        ┌──────────┴───────────┐
        │  resting: 3 H₂O/OH⁻  │
        │  substrate-bound:    │
        │   HMBPP C4–OH  →  η² olefin coordination
        └──────────────────────┘
                   │
        proton relay via Thr + H-bond network "proton reservoir"
                   │
        electron source: reduced [2Fe-2S] ferredoxin → cluster
```

1. **Substrate binding.** HMBPP enters in a hairpin conformation; its diphosphate is anchored by conserved basic/polar residues (positions 41, 74, 124, 168, 226–228, 270), and its C4–OH coordinates the apical iron of the [4Fe-4S] cluster (Findings 2, 4).
2. **Reduction.** The [4Fe-4S] cluster, re-reduced by physiological reduced [2Fe-2S] ferredoxin, delivers electrons directly to the bound substrate (Findings 2, 4).
3. **Organometallic intermediate.** Upon one-electron reduction, the C4–OH rotates away and the olefin forms an η²-metallacycle with the apical iron (favored energetically by DFT; Finding 2 / PMID 26098647).
4. **Dehydroxylation and protonation.** The C4 hydroxyl departs as water; a Thr-mediated proton relay and H-bond reservoir supply protons, and a second electron completes the 2e⁻/2H⁺ reduction, yielding the allylic products IPP and DMAPP (Findings 1, 2).

### Localization

All annotations and physicochemical evidence converge on a **soluble cytoplasmic** localization: no signal peptide, no transmembrane helix (Finding 4), and an oxygen-labile Fe–S active site that requires the reducing cytoplasmic milieu (Findings 2, 3). Its substrate (HMBPP) and products (IPP, DMAPP) are likewise soluble cytoplasmic metabolites, and its electron donor (ferredoxin) is cytoplasmic. IspH therefore carries out its function **in the cytoplasm**.

### Confidence assessment

| Aspect of annotation | Evidence type | Confidence |
|---|---|---|
| Reaction (HMBPP → IPP + DMAPP), EC 1.17.7.4 | Family biochemistry + HAMAP + sequence/structure | **Very high** |
| [4Fe-4S] cluster, 3-Cys ligation (C12/C96/C198) | Sequence conservation + spectroscopy (orthologues) | **Very high** |
| Apical-iron / organometallic mechanism, Thr relay | Crystallography, Mössbauer, NRVS, DFT (orthologues) | **High** |
| [2Fe-2S] ferredoxin as electron donor | UniProt/RHEA + docking (orthologue) | **High** |
| Cytoplasmic localization | Sequence features + cofactor chemistry | **High** |
| MEP pathway sole precursor source in KT2440 | Metabolic engineering in the exact strain | **Very high** |
| Essentiality / drug-target status | Family-wide genetic + pharmacological data | **High** (KT2440-specific essentiality inferred) |

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports the annotation |
|---|---|---|
| [22646150](https://pubmed.ncbi.nlm.nih.gov/22646150/) | Spectroscopic reaction intermediates in WT/mutant HMBPP reductase | States the reaction, substrate, products, 2e⁻ chemistry; establishes active [4Fe-4S] as direct electron source with intermediate bound to cluster |
| [28139297](https://pubmed.ncbi.nlm.nih.gov/28139297/) | Ginkgo IspH active-site Phe / IPP:DMAPP ratio | Confirms last-step MEP reaction and ~4–6:1 IPP:DMAPP product ratio |
| [20080550](https://pubmed.ncbi.nlm.nih.gov/20080550/) | Probing IspH mechanism by X-ray | Crystal structures (incl. PDB 3KE8 reference) showing apical-iron substrate binding + Thr167 proton relay |
| [19708647](https://pubmed.ncbi.nlm.nih.gov/19708647/) | In vivo Mössbauer of LytB | Defines 3-cysteine ligation and unique apical iron with extra O/N ligands |
| [24481599](https://pubmed.ncbi.nlm.nih.gov/24481599/) | Bioorganometallic chemistry of IspG/IspH | Confirms [Fe4S4] protein performing 2H⁺/2e⁻ reduction via novel mechanism; human-absent |
| [26098647](https://pubmed.ncbi.nlm.nih.gov/26098647/) | Broken-symmetry DFT of IspH pathway | Computational support for η²-bound organometallic intermediate over Birch mechanism |
| [31500633](https://pubmed.ncbi.nlm.nih.gov/31500633/) | Engineering *P. putida* for isoprenoid production | Organism-specific: KT2440 makes IPP/DMAPP solely via MEP pathway (no MVA) |
| [35163971](https://pubmed.ncbi.nlm.nih.gov/35163971/) | IspH reductive dehydroxylation / anti-infectives | Last enzyme of pathway; absent in mammals; oxygen-sensitive [4Fe-4S] |
| [28862365](https://pubmed.ncbi.nlm.nih.gov/28862365/) | *E. coli* IspH:inhibitor crystal structures | Drug-target status; inhibitor-bound structures for rational design |
| [24188825](https://pubmed.ncbi.nlm.nih.gov/24188825/) | Structure of *P. falciparum* HMBPP reductase | Identifies [2Fe-2S] ferredoxin as electron donor via docking |
| [26118554](https://pubmed.ncbi.nlm.nih.gov/26118554/) | NRVS of *E. coli* LytB/IspH cluster | Apical iron linked to three waters in substrate-free enzyme; substrate/inhibitor complexes |
| [40432238](https://pubmed.ncbi.nlm.nih.gov/40432238/) | Fe–S enzymes of MEP pathway: IspG and IspH (review) | Oxygen sensitivity and protective mechanisms of the Fe–S active site |
| [31756006](https://pubmed.ncbi.nlm.nih.gov/31756006/) | Enzymatic evidence for rotation in LytB/IspH reaction | Independent evidence for the rotation/organometallic step in catalysis |

**Plant/orthologue corroboration.** Functional studies of Arabidopsis HDR (the plant IspH orthologue) using site-directed mutagenesis confirmed that the conserved cysteines form the Fe–S cluster and identified substrate-binding/catalytic residues, with most residues *"absolutely conserved from bacteria to plants"* ([PMID: 25037211](https://pubmed.ncbi.nlm.nih.gov/25037211/), [PMID: 25723575](https://pubmed.ncbi.nlm.nih.gov/25723575/)). These cross-kingdom conservation data reinforce the transferability of mechanistic conclusions to the *P. putida* enzyme.

**Structural/computational support specific to Q88Q89.** The AlphaFold model (mean pLDDT 96.2; Finding 6) and its 0.31 Å superposition on the substrate-bound *E. coli* structure (Finding 7) provide direct, protein-specific structural evidence that Q88Q89 possesses an intact IspH catalytic scaffold.

---

## Limitations and Knowledge Gaps

1. **No direct biochemical characterization of the *P. putida* protein.** All enzymatic, spectroscopic and crystallographic mechanistic data derive from orthologues (*E. coli*, *A. aeolicus*, *P. falciparum*, plants). The function of Q88Q89 is assigned by very strong homology/synteny/structure rather than by an in vitro assay of the purified KT2440 enzyme. Kinetic parameters (kcat, Km for HMBPP), the exact IPP:DMAPP ratio, and the identity/affinity of its cognate ferredoxin remain to be measured for *P. putida*.

2. **Essentiality inferred, not directly demonstrated in KT2440.** Essentiality is strongly expected (sole precursor route; no MVA bypass) but was not confirmed here by a *P. putida ispH* knockout/conditional-depletion experiment. Available KT2440 Tn-seq/transposon fitness datasets (e.g., PMID 40302248, 33964456, 32826213) were not specifically mined for *ispH* fitness scores in this investigation.

3. **Electron-donor identity.** The physiological electron donor is annotated as reduced [2Fe-2S] ferredoxin (UniProt/RHEA; docking in *P. falciparum*), but the specific ferredoxin(s)/flavodoxin(s) and the ferredoxin-reduction system supplying IspH in *P. putida* have not been experimentally identified.

4. **Structural model, not an experimental structure.** No experimental crystal or cryo-EM structure of the *P. putida* IspH exists; the AlphaFold model does not include the [4Fe-4S] cluster or bound substrate, so cluster geometry and substrate contacts are inferred from the *E. coli* template.

5. **Product-ratio determinants.** The ~4–6:1 IPP:DMAPP ratio is a bacterial family generalization; active-site residues that tune this ratio (e.g., the Phe effect noted in Ginkgo, PMID 28139297) were not examined for the specific *P. putida* residues.

---

## Proposed Follow-up Experiments / Actions

1. **Heterologous expression and in vitro assay.** Clone PP_0606, express in *E. coli* under anaerobic/Fe–S-reconstitution conditions, and assay HMBPP-reductase activity (e.g., photometric/HPLC detection of IPP + DMAPP), measuring kcat, Km(HMBPP), the IPP:DMAPP product ratio, and O₂ sensitivity — providing direct, protein-specific confirmation of Finding 1.

2. **Cofactor characterization.** Use EPR/Mössbauer/UV-vis on the reconstituted enzyme to confirm the [4Fe-4S]²⁺ cluster and apical-iron water ligation directly for Q88Q89 (validating Finding 2 for this protein).

3. **Genetic essentiality test.** Attempt a clean *ispH* deletion in KT2440 with and without an inducible complementing copy (or CRISPRi knockdown) to formally demonstrate essentiality and characterize the depletion phenotype (growth arrest, loss of quinone/carotenoid/bactoprenol-dependent processes).

4. **Mine existing fitness data.** Extract the PP_0606 fitness/essentiality call from published KT2440 RB-TnSeq/Tn-seq datasets (PMID 33964456, 32826213, 40302248) as rapid, no-cost genetic evidence for essentiality.

5. **Site-directed mutagenesis.** Mutate Cys12/Cys96/Cys198 and the annotated proton-donor residue 126 and substrate-binding residues, then test activity/complementation to confirm their catalytic roles in the *P. putida* enzyme (analogous to the Arabidopsis HDR study, PMID 25037211).

6. **Electron-donor identification.** Identify and reconstitute the physiological ferredoxin/flavodoxin + reductase system of *P. putida* that reduces IspH, and measure electron-transfer kinetics.

7. **Inhibitor susceptibility.** Test known IspH inhibitors (HMBPP analogues such as AMBPP/TMBPP, and cell-penetrant prodrug variants) against *P. putida* and its purified IspH to evaluate the enzyme's tractability as an antibacterial target in this organism.

---

## Conclusion

IspH (Q88Q89 / *ispH* / PP_0606) in *Pseudomonas putida* KT2440 is unambiguously identified as **4-hydroxy-3-methylbut-2-enyl diphosphate reductase (HMBPP reductase, EC 1.17.7.4)**, the oxygen-sensitive [4Fe-4S] metalloenzyme that catalyzes the final, committed step of the MEP isoprenoid-biosynthesis pathway. It performs the 2e⁻/2H⁺ reductive dehydroxylation of HMBPP to the universal C5 precursors IPP and DMAPP in the cytoplasm, using reduced [2Fe-2S] ferredoxin as electron donor and an apical-iron / organometallic mechanism. Because this pathway is the sole route to isoprenoid precursors in *P. putida* and is absent from humans, IspH is an essential, non-redundant enzyme and a validated antimicrobial drug target. The annotation is supported by seven converging lines of biochemical, spectroscopic, structural, sequence, synteny and organism-specific metabolic evidence; the principal remaining gap is the absence of direct biochemical and genetic characterization of the *P. putida* protein itself.


## Artifacts

- [OpenScientist final report](ispH-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](ispH-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:22646150
2. PMID:28139297
3. PMID:19708647
4. PMID:20080550
5. PMID:24481599
6. PMID:26098647
7. PMID:31500633
8. PMID:35163971
9. PMID:28862365
10. PMID:24188825
11. PMID:25037211
12. PMID:25723575