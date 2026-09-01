---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T22:58:12.165779'
end_time: '2026-08-31T23:30:17.417338'
duration_seconds: 1925.25
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: mrdB
  gene_symbol: mrdB
  uniprot_accession: Q88DL9
  protein_description: 'RecName: Full=Peptidoglycan glycosyltransferase MrdB {ECO:0000256|HAMAP-Rule:MF_02079};
    Short=PGT {ECO:0000256|HAMAP-Rule:MF_02079}; EC=2.4.99.28 {ECO:0000256|HAMAP-Rule:MF_02079};
    AltName: Full=Cell elongation protein RodA {ECO:0000256|HAMAP-Rule:MF_02079};
    AltName: Full=Cell wall polymerase {ECO:0000256|HAMAP-Rule:MF_02079}; AltName:
    Full=Peptidoglycan polymerase {ECO:0000256|HAMAP-Rule:MF_02079}; Short=PG polymerase
    {ECO:0000256|HAMAP-Rule:MF_02079};'
  gene_info: Name=mrdB {ECO:0000256|HAMAP-Rule:MF_02079, ECO:0000313|EMBL:AAN70375.1};
    Synonyms=rodA {ECO:0000256|HAMAP-Rule:MF_02079}; OrderedLocusNames=PP_4806 {ECO:0000313|EMBL:AAN70375.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the SEDS family. MrdB/RodA subfamily.
  protein_domains: Cell_cycle_FtsW-rel_CS. (IPR018365); FtsW/RodA. (IPR001182); RodA/MrdB.
    (IPR011923); FTSW_RODA_SPOVE (PF01098)
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
  path: mrdB-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: mrdB-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88DL9
- **Protein Description:** RecName: Full=Peptidoglycan glycosyltransferase MrdB {ECO:0000256|HAMAP-Rule:MF_02079}; Short=PGT {ECO:0000256|HAMAP-Rule:MF_02079}; EC=2.4.99.28 {ECO:0000256|HAMAP-Rule:MF_02079}; AltName: Full=Cell elongation protein RodA {ECO:0000256|HAMAP-Rule:MF_02079}; AltName: Full=Cell wall polymerase {ECO:0000256|HAMAP-Rule:MF_02079}; AltName: Full=Peptidoglycan polymerase {ECO:0000256|HAMAP-Rule:MF_02079}; Short=PG polymerase {ECO:0000256|HAMAP-Rule:MF_02079};
- **Gene Information:** Name=mrdB {ECO:0000256|HAMAP-Rule:MF_02079, ECO:0000313|EMBL:AAN70375.1}; Synonyms=rodA {ECO:0000256|HAMAP-Rule:MF_02079}; OrderedLocusNames=PP_4806 {ECO:0000313|EMBL:AAN70375.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the SEDS family. MrdB/RodA subfamily.
- **Key Domains:** Cell_cycle_FtsW-rel_CS. (IPR018365); FtsW/RodA. (IPR001182); RodA/MrdB. (IPR011923); FTSW_RODA_SPOVE (PF01098)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "mrdB" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'mrdB' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **mrdB** (gene ID: mrdB, UniProt: Q88DL9) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: mrdB (RodA) in *Pseudomonas putida* KT2440

**UniProt accession:** Q88DL9 · **Gene:** *mrdB* (synonym *rodA*) · **Locus:** PP_4806
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / KT2440), PSEPK
**EC:** 2.4.99.28 · **Family:** SEDS (Shape, Elongation, Division, Sporulation), MrdB/RodA subfamily
**Domains:** PF01098 (FTSW_RODA_SPOVE); IPR001182 (FtsW/RodA); IPR011923 (RodA/MrdB); IPR018365 (Cell_cycle_FtsW-rel_CS)

---

## Summary

The gene **mrdB** (synonym *rodA*; ordered locus PP_4806) of *Pseudomonas putida* KT2440 encodes **RodA**, a member of the **SEDS (Shape, Elongation, Division and Sporulation) family** of integral inner-membrane proteins. Its primary molecular function is that of a **peptidoglycan glycosyltransferase / peptidoglycan polymerase (EC 2.4.99.28)**: it polymerizes the lipid-linked cell-wall precursor **Lipid II** into linear glycan strands, the backbone of the peptidoglycan (murein) sacculus. This role — long assumed to belong exclusively to the class A penicillin-binding proteins (aPBPs) — was reassigned to SEDS proteins by genetic and biochemical work in *Bacillus subtilis* and *Escherichia coli* in 2016–2017, redefining RodA as a founding member of a previously unrecognized, essential class of cell-wall polymerases ([PMID: 27525505](https://pubmed.ncbi.nlm.nih.gov/27525505/); [PMID: 28085152](https://pubmed.ncbi.nlm.nih.gov/28085152/)).

RodA does not act alone. It functions as an **obligate cognate pair** with the class B penicillin-binding protein **PBP2**, encoded by the adjacent gene *mrdA*. RodA provides the **transglycosylase (glycan-polymerizing)** activity while PBP2 provides the **transpeptidase (peptide-crosslinking)** activity, and together they form the enzymatic core of the **elongasome** (Rod complex / Rod system). The elongasome is a multiprotein machine — the actin-like cytoskeletal filament **MreB**, the RodA–PBP2 synthase, and the regulatory membrane proteins **MreC, MreD and RodZ** — that directs the insertion of new peptidoglycan into the **lateral (cylindrical) wall** of rod-shaped bacteria, elongating the cell along its long axis and maintaining the characteristic rod morphology of *P. putida* ([PMID: 33857142](https://pubmed.ncbi.nlm.nih.gov/33857142/); [PMID: 33370261](https://pubmed.ncbi.nlm.nih.gov/33370261/)).

Structurally, RodA is a **ten-transmembrane-helix inner-membrane enzyme** with large periplasmic loops and a **conserved catalytic cavity embedded within the membrane**; it adds new Lipid II monomers to the **reducing end** of the growing glycan chain, releasing polymerized peptidoglycan at the periplasmic (outer) face of the cytoplasmic membrane. Its activity is tuned by the accessory proteins MreC (activator) and MreD (suppressor) together with RodZ, and it is **evolutionarily paralogous** to the divisome SEDS protein **FtsW**, reflecting a deep homology between the machineries of cell elongation and cell division ([PMID: 29590088](https://pubmed.ncbi.nlm.nih.gov/29590088/); [PMID: 31386359](https://pubmed.ncbi.nlm.nih.gov/31386359/); [PMID: 24094808](https://pubmed.ncbi.nlm.nih.gov/24094808/)).

**A note on evidence and organism.** No experimental study to date has characterized the *P. putida* PP_4806 protein directly. The annotation for Q88DL9 is therefore an **orthology-grounded inference**: the gene symbol, the SEDS/MrdB-RodA subfamily assignment (HAMAP MF_02079), the PF01098 (FTSW_RODA_SPOVE) and IPR011923 (RodA/MrdB) domain signatures, and the conserved *mrdAB* gene neighborhood all unambiguously place PP_4806 as the RodA ortholog. The mechanistic detail below is drawn from precise structural, genetic and biochemical studies in the models *E. coli*, *B. subtilis*, *Thermus thermophilus* and *Staphylococcus aureus*. The gene symbol is **not ambiguous** — *mrdB* is the standard Gammaproteobacterial synonym for *rodA* (the *mrd*, "murein cluster d," rod-shape locus: *mrdA* = PBP2, *mrdB* = RodA), and it corresponds cleanly to the well-characterized bacterial elongasome polymerase.

---

## Key Findings

### Finding 1 — RodA is a SEDS-family peptidoglycan glycosyltransferase (a Lipid II polymerase)

The core molecular function of MrdB/RodA is peptidoglycan polymerization. UniProt Q88DL9 assigns **EC 2.4.99.28** and places the protein in the **SEDS family, MrdB/RodA subfamily** via HAMAP rule MF_02079, supported by the domain signatures **PF01098 (FTSW_RODA_SPOVE)** and **IPR011923 (RodA/MrdB)**. These bioinformatic assignments are backed by direct biochemical proof from model organisms. In a landmark study, the SEDS proteins RodA and FtsW were shown to polymerize the lipid-linked precursor Lipid II into glycan strands — an activity that had, for decades, been attributed solely to the class A PBPs. Genetic and biochemical analyses in *B. subtilis* demonstrated that cells can survive without all of their known aPBP polymerases by up-regulating RodA, forcing the conclusion that RodA itself is a bona fide peptidoglycan polymerase ([PMID: 27525505](https://pubmed.ncbi.nlm.nih.gov/27525505/)).

The authors of that work stated plainly that *"our genetic and biochemical analyses indicate that SEDS proteins constitute a family of peptidoglycan polymerases"* — establishing RodA, as a SEDS protein, as a peptidoglycan polymerase and defining the enzymatic function that the EC 2.4.99.28 annotation encodes. A companion study confirmed that *"RodA and possibly other proteins in the wider SEDS (shape, elongation, division and sporulation) family have now emerged as a previously unknown class of essential glycosyltransferase enzymes"* ([PMID: 28085152](https://pubmed.ncbi.nlm.nih.gov/28085152/)). This reclassification is the single most important basis of the modern annotation of *mrdB*: the gene product is not a passive shape determinant but an active, essential biosynthetic enzyme.

**Substrate specificity.** The substrate is **Lipid II** — undecaprenyl-pyrophosphoryl-MurNAc(pentapeptide)-GlcNAc, the universal lipid-linked peptidoglycan precursor. RodA transfers the disaccharide-peptide unit onto the growing glycan chain, releasing undecaprenyl diphosphate — i.e., glycan-chain elongation by successive addition of GlcNAc–MurNAc disaccharide-peptide units (EC 2.4.99.28).

### Finding 2 — RodA acts with the cognate transpeptidase PBP2 (mrdA) in the elongasome to build lateral peptidoglycan and maintain rod shape

RodA is only half of a two-enzyme peptidoglycan synthase. Its cognate partner is the **class B PBP PBP2**, encoded by ***mrdA***, which in *P. putida* — as in most rod-shaped bacteria — lies immediately adjacent to *mrdB* in the conserved *mrdAB* locus. Together the two proteins form the **PG synthase of the Rod complex/elongasome**, synthesizing peptidoglycan along the cylindrical body of the cell. RodA contributes the **transglycosylase** (glycan-polymerizing) activity; PBP2 contributes the **transpeptidase** (peptide-crosslinking) activity that stitches adjacent glycan strands into a load-bearing meshwork ([PMID: 33857142](https://pubmed.ncbi.nlm.nih.gov/33857142/); [PMID: 33370261](https://pubmed.ncbi.nlm.nih.gov/33370261/)).

The functional partnership is stated directly in genetic analyses of the SEDS-bPBP complexes: *"SEDS family peptidoglycan (PG) glycosyltransferases, RodA and FtsW, require their cognate transpeptidases PBP2 and FtsI (class B penicillin binding proteins) to synthesize PG along the cell cylinder and at the septum, respectively"* ([PMID: 33857142](https://pubmed.ncbi.nlm.nih.gov/33857142/)). This sentence encodes three facts at once: (i) RodA's obligate partner is PBP2; (ii) their shared product is lateral wall PG "along the cell cylinder"; and (iii) this elongation machinery is the mechanistic mirror of the FtsW–FtsI septal machinery of division.

The physical basis of the pairing is equally well established: *"PBP2 and RodA form a complex mediated by their transmembrane and periplasmic parts and independent of their catalytic activity"* ([PMID: 33370261](https://pubmed.ncbi.nlm.nih.gov/33370261/)). The interface is coordinated through the extracellular loop 4 (ECL4) of the SEDS protein and the "pedestal" domain of the bPBP, an arrangement resolved by cryo-EM of the assembled complex ([PMID: 32152588](https://pubmed.ncbi.nlm.nih.gov/32152588/)). The broader elongasome comprises **MreB, RodA–PBP2, MreC, MreD and RodZ**; genetic loss of essentially any of these components abolishes rod shape, underscoring that RodA operates within an integrated, spatially organized machine rather than as a free enzyme.

### Finding 3 — RodA is a 10-transmembrane inner-membrane enzyme with a conserved membrane-embedded catalytic cavity that polymerizes at the reducing end

The subcellular localization and active-site architecture of RodA are known at atomic resolution. The **2.9 Å crystal structure of *Thermus thermophilus* RodA** revealed *"a ten-pass transmembrane fold with large extracellular loops, one of which is partially disordered,"* and *"a highly conserved cavity in the transmembrane domain"* ([PMID: 29590088](https://pubmed.ncbi.nlm.nih.gov/29590088/)). Site-directed mutagenesis of residues lining this cavity abolished RodA function both *in vitro* and *in vivo* in *B. subtilis* and *E. coli*, identifying the cavity as the catalytic center. This topology firmly localizes RodA to the **cytoplasmic (inner) membrane**, with its catalytic machinery embedded within the lipid bilayer and its glycan product emerging on the **periplasmic** side — precisely where the growing sacculus resides.

The catalytic mechanism has also been defined. SEDS polymerases *"synthesize peptidoglycan by adding new Lipid II monomers to the reducing end of the growing glycan chain"* ([PMID: 31386359](https://pubmed.ncbi.nlm.nih.gov/31386359/)) — a directionality distinct from that of the aPBP glycosyltransferases, which extend at the non-reducing end. The same work delineated separate lipid requirements for the glycosyl-donor versus glycosyl-acceptor substrates, giving substrate-level insight into how the enzyme engages Lipid II. Finally, cryo-EM of the RodA-bPBP synthase complex showed how the polymerization step (RodA) and the crosslinking step (PBP2) are structurally coordinated in space and time, so that newly polymerized glycan is handed directly to the transpeptidase for insertion into the existing wall ([PMID: 32152588](https://pubmed.ncbi.nlm.nih.gov/32152588/)).

### Finding 4 — RodA activity is regulated by MreC/MreD/RodZ and is evolutionarily paralogous to the divisome SEDS protein FtsW

RodA–PBP2 is a tightly regulated synthase, not a constitutively active one. The accessory proteins **MreC and MreD** act as opposing modulators: MreC changes the PBP2–RodA interaction to switch the synthase to an active "on-state," an effect suppressed by MreD, so that *"the balance between MreC and MreD determines the activity of PBP2"* ([PMID: 33370261](https://pubmed.ncbi.nlm.nih.gov/33370261/)). Consistent with this activator model, gain-of-function mutations in RodA-PBP2 can bypass the normal requirement for MreC, MreD and RodZ, indicating that the Mre proteins and RodZ act as activators/couplers of the synthase rather than as core catalytic subunits ([PMID: 33558391](https://pubmed.ncbi.nlm.nih.gov/33558391/)). RodZ, in turn, connects the synthase to the MreB cytoskeleton, which orients where new PG is deposited.

Evolutionarily, RodA sits within a family that spans both of the bacterium's peptidoglycan-building machines. The elongasome (RodA-PBP2, MreB) and the divisome (FtsW-FtsI/PBP3, FtsA) are **homologous machines**: *"Both integrate closely related penicillin-binding proteins (PBPs) for PG synthesis, use proteins of the RodA/FtsW (SEDS, shape, elongation, division and sporulation) family for Lipid II export and interact with MraY/Mur proteins for Lipid II synthesis"* ([PMID: 24094808](https://pubmed.ncbi.nlm.nih.gov/24094808/)). RodA (elongation) and FtsW (division) are thus **paralogs** derived from a common ancestral SEDS protein; the elongasome is plausibly a modified, redeployed divisome. This paralogy is not merely historical — it explains why RodA and FtsW share the same 10-TM fold, the same cognate-bPBP logic, and the same activation mechanism, and it firmly links RodA to the upstream **Lipid II biosynthetic pathway** (MraY/MurG/Mur enzymes) that furnishes its substrate.

---

## Mechanistic Model / Interpretation

### The RodA reaction in the context of the elongasome

RodA is the glycan-polymerizing engine of the Rod complex. The following schematic places RodA within the assembly line of lateral cell-wall synthesis in *P. putida*:

```
   CYTOPLASM
   ┌──────────────────────────────────────────────────────────────┐
   │  Mur pathway (MurA–F) ─► UDP-MurNAc-pentapeptide              │
   │             │                                                 │
   │          MraY ─► Lipid I ──► MurG ─► Lipid II (cytoplasmic)   │
   │                                        │                      │
   │   MreB filaments ── RodZ ── (orient & position synthase)     │
   └────────────────────────────────────────┼─────────────────────┘
   ═════════════════════════════════════════│═══════════ INNER (cytoplasmic) MEMBRANE
        [ RodA: 10 TM helices ]  ⇄  [ PBP2 (mrdA) ]     ◄─ MreC (activate) / MreD (suppress)
        conserved membrane cavity      pedestal + TP domain
              │ (engages Lipid II)            │
   ───────────┼───────────────────────────────┼─────────── PERIPLASM
              ▼                                ▼
     GLYCAN POLYMERIZATION            PEPTIDE CROSSLINKING
     (add Lipid II to reducing end)   (D,D-transpeptidation)
              └──────────► nascent LATERAL PEPTIDOGLYCAN ◄──────────┘
                          (inserted into the cylindrical sacculus)
                                → cell ELONGATION, ROD SHAPE
```

**Reading the model:**

1. **Substrate supply.** The Mur enzymes build UDP-MurNAc-pentapeptide in the cytoplasm; MraY and MurG assemble **Lipid II** on the undecaprenyl-phosphate carrier at the inner leaflet of the membrane. Lipid II is RodA's substrate.
2. **Polymerization (RodA).** RodA, embedded in the inner membrane via its ten TM helices, uses its conserved membrane-buried cavity to add successive Lipid II units to the **reducing end** of the growing glycan strand, releasing the strand toward the periplasm.
3. **Crosslinking (PBP2/mrdA).** The cognate transpeptidase PBP2, held against RodA through their TM and periplasmic contacts, crosslinks the new glycan into the existing sacculus.
4. **Spatial control (MreB / RodZ / MreC / MreD).** MreB filaments, linked to the synthase via RodZ and the RodA C-terminal tail/PBP2 cytoplasmic region, orient insertion circumferentially around the cell cylinder. MreC (activator) and MreD (suppressor) set the synthase's activity level.
5. **Outcome.** Dispersed insertion of peptidoglycan into the lateral wall lengthens the cell while preserving a constant diameter — the geometric definition of rod-shaped growth.

### Elongasome vs. divisome: a paralogous pair

| Feature | Elongasome (contains RodA) | Divisome (paralogous) |
|---|---|---|
| SEDS polymerase | **RodA** (*mrdB* / PP_4806) | FtsW |
| Cognate class B PBP (transpeptidase) | PBP2 (*mrdA*) | FtsI / PBP3 |
| Cytoskeletal organizer | MreB (actin-like) | FtsZ → FtsA (tubulin/actin-like) |
| PG synthesized | Lateral / cylindrical wall | Septal wall (division) |
| Net morphological output | Cell elongation, rod shape | Cell constriction, septation |
| Shared upstream pathway | Lipid II (MraY / MurG / Mur enzymes) | Lipid II (same pathway) |

The two machines are variations on a single theme, which is why insight from the divisome FtsW-FtsI complex ([PMID: 33857142](https://pubmed.ncbi.nlm.nih.gov/33857142/)) directly informs the RodA-PBP2 mechanism, and vice versa.

### Localization summary

- **Compartment:** integral **inner (cytoplasmic) membrane** protein.
- **Topology:** **10 transmembrane helices**, large periplasmic loops; catalytic cavity within the membrane.
- **Site of catalysis:** glycan polymerization at/near the membrane with product delivered to the **periplasmic face**, where the peptidoglycan sacculus is assembled.
- **Positional targeting within the cell:** dispersed sites along the **lateral cylinder**, patterned by MreB filaments (not at the septum — that is FtsW's domain).

---

## Evidence Base

| PMID | Title (abbreviated) | Contribution to this annotation |
|---|---|---|
| [27525505](https://pubmed.ncbi.nlm.nih.gov/27525505/) | *SEDS proteins are a widespread family of bacterial cell wall polymerases* | **Foundational.** Genetic + biochemical proof that SEDS proteins (RodA) are peptidoglycan polymerases — defines the EC 2.4.99.28 function of *mrdB*. |
| [28085152](https://pubmed.ncbi.nlm.nih.gov/28085152/) | *RodA as the missing glycosyltransferase in B. subtilis…* | Confirms RodA is an **essential glycosyltransferase**, matching the enzymatic assignment for Q88DL9; flags SEDS as an antibiotic target. |
| [33857142](https://pubmed.ncbi.nlm.nih.gov/33857142/) | *Genetic analysis of the FtsWI complex… conserved activation of SEDS-bPBP complexes* | States directly that RodA **requires its cognate PBP2** to synthesize PG **along the cell cylinder** (elongation). |
| [33370261](https://pubmed.ncbi.nlm.nih.gov/33370261/) | *MreC and MreD balance the interaction between PBP2 and RodA* | Shows the **physical RodA-PBP2 complex** and that the **MreC/MreD balance** sets synthase activity. |
| [29590088](https://pubmed.ncbi.nlm.nih.gov/29590088/) | *Structure of RodA resolved by evolutionary coupling analysis* | Crystal structure: **10-TM fold**, conserved **membrane catalytic cavity** essential for function → localization + active site. |
| [31386359](https://pubmed.ncbi.nlm.nih.gov/31386359/) | *Direction of Chain Growth and Substrate Preferences of SEDS PG glycosyltransferases* | Establishes **reducing-end polymerization** mechanism and distinct Lipid II donor/acceptor requirements. |
| [24094808](https://pubmed.ncbi.nlm.nih.gov/24094808/) | *Do the divisome and elongasome share a common evolutionary past?* | Places RodA in the **RodA/FtsW SEDS family**, links to the Lipid II pathway, establishes **elongasome–divisome paralogy**. |
| [33558391](https://pubmed.ncbi.nlm.nih.gov/33558391/) | *Regulatory domains within MreC and MreD* | Activating RodA-PBP2 mutations bypass MreCD/RodZ → Mre proteins act as **activators** of the synthase. |
| [32152588](https://pubmed.ncbi.nlm.nih.gov/32152588/) | *Structural coordination of polymerization and crosslinking by a SEDS-bPBP synthase complex* | Cryo-EM of the assembled synthase; structural coupling of RodA glycosyltransfer and bPBP transpeptidation via ECL4–pedestal. |
| [31086309](https://pubmed.ncbi.nlm.nih.gov/31086309/) | *SEDS-bPBP pairs direct lateral and septal PG synthesis in S. aureus* | Independent confirmation in a second organism that **RodA-type pairs drive lateral (sidewall) PG**. |
| [42394843](https://pubmed.ncbi.nlm.nih.gov/42394843/) | *Direct interaction between MreB and the RodA-PBP2 complex* | Maps the **RodA C-terminal tail / PBP2–MreB** coupling that organizes lateral PG synthesis. |
| [42578761](https://pubmed.ncbi.nlm.nih.gov/42578761/) | *RodZ acts through MreBCD to activate the elongasome* | Defines RodZ's role in activating the RodA-containing elongasome. |

**Supporting context.** The *P. putida* KT2440 genome is fully sequenced and this locus (PP_4806) is annotated within the conserved *mre/mrd* region. The wider *P. putida* functional-genomics literature (e.g., barcoded transposon and CRISPRi toolsets — [PMID: 36093381](https://pubmed.ncbi.nlm.nih.gov/36093381/), [PMID: 36158112](https://pubmed.ncbi.nlm.nih.gov/36158112/)) confirms the organism's tractability but does not report a dedicated study of PP_4806 itself, reinforcing that this annotation rests on orthology to characterized RodA proteins.

---

## Supported vs. Refuted Hypotheses

**Supported**

- mrdB/RodA is a SEDS-family peptidoglycan glycosyltransferase (Lipid II polymerase), EC 2.4.99.28. ✔ ([PMID: 27525505](https://pubmed.ncbi.nlm.nih.gov/27525505/); [PMID: 28085152](https://pubmed.ncbi.nlm.nih.gov/28085152/))
- It functions as a cognate pair with PBP2 (*mrdA*) as the elongasome PG synthase. ✔ ([PMID: 33857142](https://pubmed.ncbi.nlm.nih.gov/33857142/); [PMID: 33370261](https://pubmed.ncbi.nlm.nih.gov/33370261/))
- It localizes to the inner membrane and acts at the periplasmic face; the catalytic cavity is membrane-embedded; it polymerizes at the reducing end. ✔ ([PMID: 29590088](https://pubmed.ncbi.nlm.nih.gov/29590088/); [PMID: 31386359](https://pubmed.ncbi.nlm.nih.gov/31386359/))
- Its role is lateral/sidewall PG synthesis for cell elongation and rod-shape maintenance, coordinated by MreB/MreC/MreD/RodZ and paralogous to divisome FtsW. ✔ ([PMID: 33558391](https://pubmed.ncbi.nlm.nih.gov/33558391/); [PMID: 24094808](https://pubmed.ncbi.nlm.nih.gov/24094808/))

**Refuted / excluded**

- That RodA is merely a passive scaffold or lipid "flippase" with no catalytic activity — refuted; it is the catalytic glycan polymerase ([PMID: 27525505](https://pubmed.ncbi.nlm.nih.gov/27525505/); [PMID: 29590088](https://pubmed.ncbi.nlm.nih.gov/29590088/)).
- That glycan polymerization is exclusively a class A PBP function — refuted; SEDS proteins constitute a second, independent polymerase family.
- Gene-identity ambiguity — excluded; *mrdB* = *rodA* is a standard Gammaproteobacterial synonym fully consistent with the organism and domain architecture.

---

## Limitations and Knowledge Gaps

1. **No direct experimental characterization in *P. putida*.** Every mechanistic claim about RodA function derives from *E. coli*, *B. subtilis*, *T. thermophilus* and *S. aureus*. While orthology is unambiguous (gene symbol, SEDS/MrdB-RodA subfamily, PF01098/IPR011923 domains, conserved *mrdAB* synteny), the *P. putida* PP_4806 protein has not itself been purified, mutated, or assayed. Essentiality, precise kinetics, and any *Pseudomonas*-specific regulation remain formally untested.

2. **Species-specific accessory biology.** *P. putida* is a Gram-negative gammaproteobacterium related to *P. aeruginosa* and *E. coli*, so its elongasome is expected to closely resemble the *E. coli* Rod complex. However, the exact stoichiometry, the relative contribution of aPBPs versus RodA to lateral wall synthesis, and the influence of *Pseudomonas*-specific envelope-stress and outer-membrane systems have not been mapped in this organism.

3. **Structural inference vs. atomic structure for this ortholog.** The 10-TM fold and catalytic cavity are established for *T. thermophilus* RodA and assembled synthase complexes; no experimental structure exists for the *P. putida* protein. An AlphaFold model would likely reproduce the fold with high confidence but has not been validated here.

4. **Quantitative reaction parameters.** EC 2.4.99.28 defines the reaction, but organism-specific substrate affinities, processivity, glycan-strand length distribution, and the precise coordination timing with PBP2 crosslinking in *P. putida* are unquantified.

5. **Regulatory network detail.** The MreC/MreD/RodZ activation logic is drawn from *E. coli*/model systems; whether *P. putida* deploys additional layers of control (transcriptional, post-translational, or via two-component systems) over PP_4806 is unknown.

---

## Proposed Follow-up Experiments / Actions

1. **Confirm essentiality and phenotype in *P. putida* KT2440.** Use the established CRISPRi toolsets for *P. putida* ([PMID: 36093381](https://pubmed.ncbi.nlm.nih.gov/36093381/); [PMID: 36158112](https://pubmed.ncbi.nlm.nih.gov/36158112/)) to knock down PP_4806 and score for loss of rod shape, cell rounding/lysis, and growth defect — the diagnostic elongasome phenotype.

2. **Test the cognate PBP2 (mrdA) partnership locally.** Verify co-operonic organization of PP_4806 (*mrdB*) with the adjacent *mrdA* (PBP2) locus and demonstrate genetic co-dependence (e.g., synthetic phenotypes, co-depletion), confirming the RodA-PBP2 pair in this organism.

3. **Reconstitute activity in vitro.** Purify recombinant *P. putida* RodA (± PBP2) and assay Lipid II polymerization using established SEDS glycosyltransferase assays, to confirm EC 2.4.99.28 activity and measure organism-specific kinetics and reducing-end directionality ([PMID: 31386359](https://pubmed.ncbi.nlm.nih.gov/31386359/)).

4. **Generate and validate a structural model.** Build an AlphaFold model of PP_4806 and superpose it on the *T. thermophilus* RodA structure ([PMID: 29590088](https://pubmed.ncbi.nlm.nih.gov/29590088/)) to confirm the 10-TM fold and conserved catalytic-cavity residues; site-directed mutagenesis of cavity residues should abolish function if conserved.

5. **Map localization.** Fluorescently tag RodA (or PBP2) and image live *P. putida* to confirm dispersed, MreB-patterned lateral (non-septal) localization and circumferential motion, as seen for elongasomes in *E. coli* and *B. subtilis*.

6. **Probe as an antibiotic target.** Because RodA/SEDS enzymes are essential and structurally distinct from aPBPs, and are highlighted as a druggable class ([PMID: 28085152](https://pubmed.ncbi.nlm.nih.gov/28085152/)), screen for small molecules that inhibit *P. putida* RodA polymerization — of interest for antibacterial development and for controlling *P. putida* in biotechnological and environmental settings.

---

## Conclusion

The gene symbol *mrdB* is **not ambiguous**: PP_4806 / Q88DL9 is the unambiguous RodA ortholog of *Pseudomonas putida* KT2440. Its gene product is a **SEDS-family peptidoglycan glycosyltransferase (EC 2.4.99.28)** that **polymerizes Lipid II into glycan strands** during cell-wall elongation. It is an **integral ten-transmembrane inner-membrane enzyme** with a conserved membrane-embedded catalytic cavity, extends glycan at the **reducing end**, and produces peptidoglycan at the **periplasmic face**. RodA works as an **obligate cognate pair with the class B transpeptidase PBP2 (mrdA)**, forming the catalytic core of the **MreB-organized elongasome (Rod complex)** — regulated by MreC/MreD/RodZ and paralogous to the divisome protein FtsW — that inserts peptidoglycan into the **lateral wall** to build and maintain the rod shape of *P. putida*. This annotation is orthology-grounded, resting on precise structural, genetic and biochemical studies in model bacteria; direct characterization in *P. putida* remains an open, tractable experimental target.


## Artifacts

- [OpenScientist final report](mrdB-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](mrdB-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:27525505
2. PMID:28085152
3. PMID:33857142
4. PMID:33370261
5. PMID:29590088
6. PMID:31386359
7. PMID:24094808
8. PMID:32152588
9. PMID:33558391
10. PMID:36093381
11. PMID:36158112