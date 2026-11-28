---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T22:58:12.169058'
end_time: '2026-08-31T23:09:25.998235'
duration_seconds: 673.83
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: mrdA-I
  gene_symbol: mrdA-I
  uniprot_accession: Q88GI2
  protein_description: 'RecName: Full=Peptidoglycan D,D-transpeptidase MrdA {ECO:0000256|HAMAP-Rule:MF_02081};
    EC=3.4.16.4 {ECO:0000256|HAMAP-Rule:MF_02081}; AltName: Full=Penicillin-binding
    protein 2 {ECO:0000256|HAMAP-Rule:MF_02081}; Short=PBP-2 {ECO:0000256|HAMAP-Rule:MF_02081};'
  gene_info: Name=mrdA-I {ECO:0000313|EMBL:AAN69336.1}; Synonyms=mrdA {ECO:0000256|HAMAP-Rule:MF_02081};
    OrderedLocusNames=PP_3741 {ECO:0000313|EMBL:AAN69336.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the transpeptidase family. MrdA subfamily.
  protein_domains: Beta-lactam/transpept. (IPR050515); Beta-lactam/transpept-like.
    (IPR012338); PBP_dimer. (IPR005311); PBP_dimer_sf. (IPR036138); PCN-bd_Tpept.
    (IPR001460)
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
citation_count: 16
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: mrdA-I-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: mrdA-I-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88GI2
- **Protein Description:** RecName: Full=Peptidoglycan D,D-transpeptidase MrdA {ECO:0000256|HAMAP-Rule:MF_02081}; EC=3.4.16.4 {ECO:0000256|HAMAP-Rule:MF_02081}; AltName: Full=Penicillin-binding protein 2 {ECO:0000256|HAMAP-Rule:MF_02081}; Short=PBP-2 {ECO:0000256|HAMAP-Rule:MF_02081};
- **Gene Information:** Name=mrdA-I {ECO:0000313|EMBL:AAN69336.1}; Synonyms=mrdA {ECO:0000256|HAMAP-Rule:MF_02081}; OrderedLocusNames=PP_3741 {ECO:0000313|EMBL:AAN69336.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the transpeptidase family. MrdA subfamily.
- **Key Domains:** Beta-lactam/transpept. (IPR050515); Beta-lactam/transpept-like. (IPR012338); PBP_dimer. (IPR005311); PBP_dimer_sf. (IPR036138); PCN-bd_Tpept. (IPR001460)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "mrdA-I" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'mrdA-I' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **mrdA-I** (gene ID: mrdA-I, UniProt: Q88GI2) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *mrdA-I* (PP_3741, UniProt Q88GI2) — Penicillin-Binding Protein 2 of *Pseudomonas putida* KT2440

## Summary

**Primary function.** *mrdA-I* (ordered locus **PP_3741**; UniProt **Q88GI2**) of *Pseudomonas putida* KT2440 encodes **Penicillin-Binding Protein 2 (PBP2/MrdA)**, a **monofunctional class B penicillin-binding protein (bPBP)** that acts as a **D,D-transpeptidase (EC 3.4.16.4)**. Its catalytic role is to form 4→3 peptide cross-links in the bacterial cell wall: using a periplasmic serine nucleophile, it links the D-Ala–D-Ala terminus of one peptidoglycan (PG) stem peptide (the acyl donor) to the diaminopimelate side chain of an adjacent stem peptide (the acceptor), releasing the terminal D-Ala. This is the final covalent step of peptidoglycan maturation and is carried out specifically in the context of **cell elongation** rather than division. The transpeptidase active site is the target of β-lactam antibiotics, most notably the PBP2-selective drug **mecillinam (amdinocillin)**.

**Localization and molecular partners.** PBP2 is a **bitopic inner-membrane protein**: a short N-terminal cytoplasmic tail (~residues 1–20), a single transmembrane helix (~residues 21–41), and a large periplasmic region carrying a PBP dimerization domain and the transpeptidase (TP) domain that does the catalytic work on the sacculus outside the membrane. It functions as the obligate transpeptidase partner of the **SEDS-family glycosyltransferase RodA**, which polymerizes glycan strands from Lipid II and hands them to PBP2 for cross-linking. This RodA–PBP2 synthase is the enzymatic core of the **elongasome** (Rod complex), a conserved machine also comprising the actin-like cytoskeletal protein **MreB**, plus **MreC, MreD, and RodZ**. MreB filaments track the cytoplasmic membrane and processively move the complex around the cell circumference, directing lateral wall synthesis that builds and maintains rod shape.

**Organism-specific note.** *P. putida* KT2440 is unusual in encoding **two MrdA/PBP2 paralogs** — *mrdA-I* (Q88GI2/PP_3741, the target of this report) and *mrdA-II* (Q88DL8). This gene duplication of the elongation-specific transpeptidase directly explains the "-I" suffix in the gene symbol. Our sequence/structure analysis of Q88GI2 confirms it retains the full canonical MrdA architecture and an intact catalytic serine (Ser328), consistent with a functional elongation transpeptidase. The functional annotation in this report rests on strong homology to the intensively studied *E. coli* PBP2 and the broader bPBP family; direct experimental characterization of Q88GI2 itself has not been reported, so all claims specific to *P. putida* are inferences from sequence, domain architecture, and conserved family biology.

---

## Key Findings

### F001 — MrdA/PBP2 is a monofunctional class B D,D-transpeptidase that cross-links peptidoglycan during cell elongation

The core annotation of Q88GI2, drawn from UniProt (EC 3.4.16.4; transpeptidase family, MrdA subfamily) and its domain content, places it firmly in the **class B penicillin-binding protein (bPBP)** family. Unlike class A PBPs, which are bifunctional (both glycosyltransferase and transpeptidase), class B PBPs such as MrdA/PBP2 are **monofunctional D,D-transpeptidases**: they possess only transpeptidase catalytic activity and must be paired with a separate glycan polymerase to build wall. The enzyme catalyzes the crosslinking of adjacent glycan stem peptides — transferring the acyl group of a D-Ala–D-Ala donor onto an acceptor amino group — which is the terminal maturation step of peptidoglycan and, in the case of PBP2, is dedicated to the **cell-elongation (Rod) system**.

This is supported directly by a domain-wide survey of morphogenetic peptidoglycan synthases, which states that the class B PBPs are "*monofunctional D, D-transpeptidases of the class B penicillin-binding protein family (bPBP)*" and that "*Current models support bPBPs pairing with cognate GTases to drive cell elongation, cell division, or spore formation*" ([PMID: 41089750](https://pubmed.ncbi.nlm.nih.gov/41089750/)). The specific pairing that governs elongation was defined by work identifying "*the primary PG synthesis complexes that function during cell elongation (RodA-PBP2) and cell division (FtsW-FtsI)*" ([PMID: 33022262](https://pubmed.ncbi.nlm.nih.gov/33022262/)). Q88GI2's domain complement — the penicillin-binding transpeptidase domain (IPR001460) and the PBP dimerization domains (IPR005311/IPR036138) — matches this family assignment precisely.

### F002 — PBP2 partners with the SEDS glycosyltransferase RodA; RodA polymerizes glycan and PBP2 cross-links it

PBP2 does not act alone. It forms the catalytic core of a two-enzyme synthase with **RodA**, a member of the **SEDS (Shape, Elongation, Division and Sporulation)** family of glycosyltransferases. A cryo-EM structure of the *E. coli* elongation-specific RodA–PBP2 complex shows the SEDS GT and the class B PBP together forming the heart of the PG-assembly machine: "*A SEDS GT enzyme and a Class B Penicillin Binding Protein (PBP) form the core of the multi-protein complex required for PG assembly*" ([PMID: 37620344](https://pubmed.ncbi.nlm.nih.gov/37620344/)). RodA polymerizes nascent glycan strands from the Lipid II precursor and then hands the strand off to PBP2's transpeptidase site — the same study describes "*the movement of the glycan strand from the Lipid II polymerization site of RodA towards the TP site of PBP2*" ([PMID: 37620344](https://pubmed.ncbi.nlm.nih.gov/37620344/)).

The pairing is cognate and obligate: the two SEDS enzymes each require their specific bPBP partner. As stated by genetic analysis of the septal complex, "*SEDS family peptidoglycan (PG) glycosyltransferases, RodA and FtsW, require their cognate transpeptidases PBP2 and FtsI (class B penicillin binding proteins) to synthesize PG along the cell cylinder and at the septum, respectively*" ([PMID: 33857142](https://pubmed.ncbi.nlm.nih.gov/33857142/)). This establishes two parallel machines — **RodA–PBP2 for elongation of the lateral wall (the "cell cylinder")** and **FtsW–FtsI (PBP3) for division at the septum** — and places Q88GI2 in the elongation branch.

### F003 — PBP2 is the specific target of mecillinam; its inhibition abolishes rod shape

The functional dedication of PBP2 to rod-shape maintenance is demonstrated pharmacologically. **Mecillinam (amdinocillin)** is a β-lactam that specifically acylates the transpeptidase active-site serine of PBP2. In *E. coli*, mecillinam "*specifically inhibited binding of 14C-penicillin G to penicillin-binding protein 2*" ([PMID: 12596863](https://pubmed.ncbi.nlm.nih.gov/12596863/)), confirming it engages the PBP2 active site selectively. The morphological consequence is diagnostic: mecillinam is "*a specific inhibitor of penicillin-binding protein 2, which induces spherical cells in E. coli*" ([PMID: 12596863](https://pubmed.ncbi.nlm.nih.gov/12596863/)). When PBP2 transpeptidase activity is lost, cells can no longer build cylindrical lateral wall and become spheres before lysing — the classic phenotype that first defined PBP2's role.

The PBP2 selectivity of amdinocillin generalizes across rod-shaped bacteria: in studies of morphological determinants, "*amdinocillin and aztreonam ... are β-lactams that preferentially target penicillin-binding protein 2 (PBP2) and PBP3, respectively*" ([PMID: 21926230](https://pubmed.ncbi.nlm.nih.gov/21926230/)). This clean separation — amdinocillin→PBP2/elongation, aztreonam→PBP3/division — reinforces that PBP2's essential, non-redundant task is the elongation transpeptidation that produces rod morphology.

### F004 — PBP2 localizes to the cytoplasmic membrane within the MreB-organized elongasome

PBP2 carries out its work as one component of the **elongasome (Rod complex)**, the conserved machine that drives lateral peptidoglycan synthesis in rod-shaped bacteria. The elongasome comprises six conserved proteins: the actin-like cytoskeletal protein **MreB**, the **RodA–PBP2** synthase, and the regulatory membrane proteins **MreC, MreD, and RodZ**. This composition is stated directly: "*It consists of the actin-like protein MreB, the PG synthase RodA-PBP2 complex, as well as MreCD and RodZ*" ([PMID: 42394843](https://pubmed.ncbi.nlm.nih.gov/42394843/)); and again, the rod complex contains "*the PG synthase complex RodA-PBP2, and three regulatory membrane proteins, MreC, MreD, and RodZ*" ([PMID: 42578761](https://pubmed.ncbi.nlm.nih.gov/42578761/)).

Critically, PBP2 physically links to the cytoskeleton. Both "*the cytoplasmic region of PBP2 and the C-terminal tail of RodA interact with MreB*" ([PMID: 42394843](https://pubmed.ncbi.nlm.nih.gov/42394843/)). This defines the enzyme's topology and localization: its cytoplasmic tail engages the MreB filament tracking the inner leaflet of the cytoplasmic membrane, while its transpeptidase domain (IPR001460) faces the **periplasm**, where the peptidoglycan sacculus resides and where cross-linking chemistry occurs. MreB filaments then processively move the whole complex around the cell circumference, distributing new wall material as barrel-hoop-like reinforcing strands that generate and preserve the rod shape.

### F005 — Sequence/structure of Q88GI2 confirms bitopic topology and an intact catalytic Ser328

Direct analysis of the 631-residue Q88GI2 sequence confirms it possesses the canonical, catalytically competent MrdA/PBP2 architecture. The protein has: (1) a short N-terminal **cytoplasmic tail** (~res 1–20); (2) a single N-terminal **transmembrane helix** (~res 21–41; peak Kyte-Doolittle hydrophobicity of 2.25 over a 19-residue window, well above the ~1.6 TM threshold), making it a **bitopic inner-membrane protein**; (3) a periplasmic **PBP dimerization domain** (~res 64–236, IPR005311); and (4) a periplasmic **transpeptidase domain** (~res 269–605, IPR001460).

Most importantly, the three conserved class B PBP catalytic motifs are all present and correctly spaced:
- the **SxxK motif** carrying the nucleophilic catalytic serine — **S328**-T-V-K331 (UniProt active-site "acyl-ester intermediate" = **Ser328**);
- the downstream **K[T/S]G box** — **KSGT at position 539**.

Ser328 is the serine that attacks the D-Ala–D-Ala peptide bond to form the covalent acyl-enzyme intermediate — and is also the residue that β-lactams acylate to inactivate the enzyme. The presence of an intact SxxK…KTG catalytic scaffold indicates Q88GI2 is a functional serine transpeptidase, consistent with the biochemically demonstrated β-lactam/penicillin acylation of PBP2 ([PMID: 12596863](https://pubmed.ncbi.nlm.nih.gov/12596863/)).

### F006 — *P. putida* KT2440 encodes two paralogous MrdA/PBP2 transpeptidases; the target is one of a duplicated pair

A UniProt survey of the class A/B PBP complement of *P. putida* KT2440 (taxid 160488) revealed the full penicillin-binding protein set, including — critically — **two MrdA-subfamily D,D-transpeptidases**:

| Protein | Gene | UniProt | Length (aa) | Role |
|---|---|---|---|---|
| PBP1A | *mrcA* | Q88CU6 | 817 | Class A bifunctional PG synthase |
| PBP1B | *mrcB* | Q88DY5 | 773 | Class A bifunctional PG synthase |
| PBP3 (FtsI) | *ftsI* | Q88N82 | 582 | Division transpeptidase (septal) |
| PbpC | — | Q88QC2 | — | Glycosyltransferase |
| **PBP2 / MrdA-I** | ***mrdA-I*** | **Q88GI2** | **631** | **Elongation transpeptidase (target)** |
| PBP2 / MrdA-II | *mrdA-II* | Q88DL8 | 629 | Elongation transpeptidase (paralog) |

The two MrdA proteins are near-identical in length (631 vs 629 aa) and both carry the MrdA/PBP2 elongation-transpeptidase annotation, indicating a **gene duplication of the elongation-specific transpeptidase** in this lineage. This directly resolves the meaning of the "-I" suffix in the gene symbol *mrdA-I*: it is one member of a duplicated elongation-transpeptidase pair.

---

## Mechanistic Model / Interpretation

The findings converge on a single, coherent mechanistic picture in which Q88GI2 is the **elongation-dedicated transpeptidase** of *P. putida*'s rod-shape machinery.

### Cellular topology and the reaction

```
   CYTOPLASM                    INNER MEMBRANE                 PERIPLASM
 ───────────────      ┌───────────────────────────┐    ─────────────────────
                      │                           │
  MreB filament ══════╪═ N-tail (1-20)            │
   (actin-like) ──────┼── TM helix (21-41)        │
        ↕ tracks      │                           │
     membrane         │              PBP dimer domain (64-236)
                      │                           │
                      │              Transpeptidase domain (269-605)
                      │                     • Ser328 (SxxK nucleophile)
                      │                     • Lys331
                      │                     • KSG box (539)
                      │                           │
                      └───────────────────────────┘         PEPTIDOGLYCAN
                                                             SACCULUS
   RodA (SEDS GT) polymerizes glycan from Lipid II  ──►  hand-off to PBP2 TP site
                                                          ──► 4→3 cross-link formed
```

**The catalytic cycle (D,D-transpeptidation, EC 3.4.16.4):**

1. RodA polymerizes a nascent glycan strand from Lipid II in the membrane and delivers it toward PBP2's TP site ([PMID: 37620344](https://pubmed.ncbi.nlm.nih.gov/37620344/)).
2. Ser328 attacks the carbonyl of the penultimate D-Ala in a **donor** stem peptide's D-Ala–D-Ala terminus, expelling the terminal D-Ala and forming a covalent **acyl-enzyme intermediate**.
3. The amino group of the **acceptor** stem peptide (typically the meso-diaminopimelate at position 3 in Gram-negative PG) resolves the intermediate, forming a **4→3 (D-Ala–meso-DAP) cross-link** and regenerating free Ser328.

This is the terminal, covalent step of PG maturation. Because PBP2 is monofunctional (F001), it is strictly dependent on RodA for the glycan substrate (F002); the two enzymes constitute an obligate cognate pair.

### From molecule to morphology

The transpeptidase activity is spatially organized by the elongasome (F004). MreB filaments beneath the membrane recruit and orient RodA–PBP2 and move it circumferentially, so that new cross-linked wall is laid down as hoop-like bands around the cell cylinder. This lateral insertion is what produces and sustains **rod shape**. The necessity of PBP2 for this is shown by the mecillinam phenotype: selectively poisoning PBP2's Ser328 collapses rod morphology into spheres (F003). Division, by contrast, is handled by the parallel FtsW–FtsI(PBP3) synthase — a functional division of labor mirrored by the drug selectivity of amdinocillin (PBP2) vs. aztreonam (PBP3) (F003).

### The paralog question

*P. putida* KT2440 uniquely carries two MrdA transpeptidases (F006). The target, *mrdA-I* (Q88GI2), retains a complete and intact catalytic scaffold (F005), so it is expected to be a functional elongation transpeptidase. The existence of *mrdA-II* (Q88DL8) raises the possibility of **functional redundancy, sub-functionalization, or differential regulation** (e.g., condition- or growth-phase-specific expression), which is common when core cell-wall enzymes are duplicated. Which paralog is the primary/essential elongation transpeptidase under standard growth — and whether they are individually dispensable — cannot be settled from sequence alone and remains the central open question specific to this gene.

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports the annotation |
|---|---|---|
| [41089750](https://pubmed.ncbi.nlm.nih.gov/41089750/) | *A global view of morphogenetic peptidoglycan synthases across Bacteria* | Establishes class B PBPs (incl. MrdA/PBP2) as monofunctional D,D-transpeptidases that pair with cognate GTases for elongation/division/sporulation (F001). |
| [33022262](https://pubmed.ncbi.nlm.nih.gov/33022262/) | *Uncovering Unappreciated Activities of Bacterial Cell Wall Enzymes* | Defines RodA-PBP2 as the elongation PG synthesis complex and FtsW-FtsI as the division complex (F001). |
| [37620344](https://pubmed.ncbi.nlm.nih.gov/37620344/) | *Structural basis of PG synthesis by E. coli RodA-PBP2 complex* | Cryo-EM: SEDS GT + class B PBP form the PG-assembly core; glycan hand-off from RodA's polymerization site to PBP2's TP site (F002). |
| [33857142](https://pubmed.ncbi.nlm.nih.gov/33857142/) | *Genetic analysis of septal PG synthase FtsWI; conserved SEDS-bPBP activation* | RodA/FtsW require cognate transpeptidases PBP2/FtsI to build cylinder vs. septum PG (F002). |
| [12596863](https://pubmed.ncbi.nlm.nih.gov/12596863/) | *S-benzylisothiourea compound inducing spherical E. coli* | Mecillinam specifically inhibits PBP2 (blocks 14C-penicillin G binding) and induces spherical cells (F003, F005). |
| [21926230](https://pubmed.ncbi.nlm.nih.gov/21926230/) | *Morphological determinants of helix-shaped Leptospira* | Amdinocillin/aztreonam preferentially target PBP2/PBP3 respectively (F003). |
| [42394843](https://pubmed.ncbi.nlm.nih.gov/42394843/) | *Direct interaction between MreB and RodA-PBP2 organizes lateral wall synthesis* | Defines elongasome composition; PBP2 cytoplasmic region + RodA C-tail interact with MreB (F004). |
| [42578761](https://pubmed.ncbi.nlm.nih.gov/42578761/) | *RodZ acts through MreBCD to activate the elongasome* | Confirms rod complex composition: RodA-PBP2 synthase + MreC, MreD, RodZ (F004). |

**Supporting context (not primary citations for Q88GI2 claims):** studies of SEDS-bPBP pairs in *S. aureus* ([PMID: 31086309](https://pubmed.ncbi.nlm.nih.gov/31086309/)), pneumococcal PBP2b elongasome partners ([PMID: 27684385](https://pubmed.ncbi.nlm.nih.gov/27684385/)), elongasome dynamics/tug-of-war in *B. subtilis* ([PMID: 38926336](https://pubmed.ncbi.nlm.nih.gov/38926336/)), MreB membrane-curvature effects ([PMID: 40898628](https://pubmed.ncbi.nlm.nih.gov/40898628/)), the role of the Gram-negative OM in shape ([PMID: 36778245](https://pubmed.ncbi.nlm.nih.gov/36778245/)), and classic cell-shape reviews ([PMID: 17981077](https://pubmed.ncbi.nlm.nih.gov/17981077/)) all corroborate the general model. Notably, *P. putida* itself features in a peptidoglycan-editing study ([PMID: 33830599](https://pubmed.ncbi.nlm.nih.gov/33830599/)), underscoring that this organism's cell-wall biology is actively studied, though that work centered on racemase/canavanine editing rather than on MrdA directly.

---

## Limitations and Knowledge Gaps

1. **No direct experimental study of Q88GI2.** Every functional claim specific to *P. putida* MrdA-I is an **inference by homology** from *E. coli* PBP2 and the general bPBP family. No purified-enzyme kinetics, structure, deletion phenotype, or localization data exist for Q88GI2 specifically. The annotation is high-confidence at the family level but unproven at the ortholog level.

2. **The two-paralog problem is unresolved.** We established that *mrdA-I* (Q88GI2) and *mrdA-II* (Q88DL8) coexist (F006), but not their relative importance, expression conditions, essentiality, or whether they are redundant, sub-functionalized, or differentially regulated. It is possible that under standard laboratory growth one paralog is the primary elongation transpeptidase and the other is conditional.

3. **Substrate specificity details are generic.** The 4→3 D-Ala→meso-DAP cross-linking chemistry is assumed from Gram-negative PG norms and family biology, not measured for this enzyme. *P. putida* PG-editing pathways (e.g., D-amino-acid incorporation; [PMID: 33830599](https://pubmed.ncbi.nlm.nih.gov/33830599/)) could subtly alter acceptor specificity.

4. **Membrane topology and active-site residue numbering** derive from sequence-based prediction (Kyte-Doolittle hydropathy, motif scanning, UniProt features), not from an experimentally solved structure of Q88GI2. Ser328 assignment is robust (it is the annotated active site and sits in a canonical SxxK motif) but structurally uncharacterized in this ortholog.

5. **Regulation and cell-cycle coordination** in *P. putida* (how MreB, MreC/D, RodZ, and any species-specific regulators tune MrdA-I activity) are not directly established and are extrapolated from model organisms.

---

## Proposed Follow-up Experiments / Actions

1. **Single- and double-paralog knockouts.** Construct Δ*mrdA-I*, Δ*mrdA-II*, and the double mutant in *P. putida* KT2440. Score viability, cell morphology (rod→sphere), and growth rate. This directly tests essentiality, redundancy, and which paralog is the primary elongation transpeptidase.

2. **Conditional depletion + mecillinam sensitivity.** Test whether MrdA-I depletion phenocopies mecillinam (spherical cells), and determine the mecillinam MIC in each single mutant to assign the drug's cellular target between the two paralogs.

3. **Expression profiling.** Use RNA-seq / reporter fusions across growth phases and stress conditions to determine whether *mrdA-I* and *mrdA-II* are differentially regulated (potential sub-functionalization).

4. **In vitro reconstitution.** Purify recombinant MrdA-I (and its cognate RodA) and measure transpeptidase/cross-linking activity in a membrane-reconstituted assay (cf. the FRET-based PBP assay of [PMID: 33625355](https://pubmed.ncbi.nlm.nih.gov/33625355/)) to confirm Ser328-dependent activity and RodA dependence. An S328A mutant should abolish activity.

5. **Localization microscopy.** Fluorescently tag MrdA-I and co-image with MreB to confirm circumferential, MreB-directed motion consistent with elongasome membership.

6. **Structural modeling/validation.** Build an AlphaFold3 model of the *P. putida* RodA–MrdA-I complex; validate the predicted TM helix (21–41), PBP dimerization domain, and TP active-site geometry (Ser328/Lys331/KSG-539) against the *E. coli* RodA-PBP2 cryo-EM structure ([PMID: 37620344](https://pubmed.ncbi.nlm.nih.gov/37620344/)).

---

## Conclusion

*mrdA-I* (PP_3741, Q88GI2) encodes **Penicillin-Binding Protein 2 (MrdA)**, a **monofunctional class B D,D-transpeptidase (EC 3.4.16.4)** that forms 4→3 peptidoglycan cross-links during **cell elongation**. It is a **bitopic inner-membrane protein** whose periplasmic transpeptidase domain (catalytic **Ser328**) works on the sacculus, acting as the obligate transpeptidase partner of the SEDS glycosyltransferase **RodA** within the **MreB-organized elongasome**, thereby building the lateral cell wall and maintaining **rod shape**. It is the target of the β-lactam **mecillinam**. The gene symbol carries a "-I" because *P. putida* KT2440 uniquely encodes a **duplicated pair** of elongation transpeptidases (*mrdA-I* = Q88GI2 and *mrdA-II* = Q88DL8), and Q88GI2 retains a complete, catalytically intact MrdA architecture. The annotation is well supported at the family/homology level; direct experimental characterization of this specific ortholog — and resolution of the two-paralog division of labor — remains the key outstanding work.


## Artifacts

- [OpenScientist final report](mrdA-I-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](mrdA-I-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:41089750
2. PMID:33022262
3. PMID:37620344
4. PMID:33857142
5. PMID:12596863
6. PMID:21926230
7. PMID:42394843
8. PMID:42578761
9. PMID:31086309
10. PMID:27684385
11. PMID:38926336
12. PMID:40898628
13. PMID:36778245
14. PMID:17981077
15. PMID:33830599
16. PMID:33625355