---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-23T10:59:15.431478'
end_time: '2026-07-23T12:25:22.347385'
duration_seconds: 5166.92
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: murG
  gene_symbol: murG
  uniprot_accession: Q88N76
  protein_description: 'RecName: Full=UDP-N-acetylglucosamine--N-acetylmuramyl-(pentapeptide)
    pyrophosphoryl-undecaprenol N-acetylglucosamine transferase {ECO:0000255|HAMAP-Rule:MF_00033};
    EC=2.4.1.227 {ECO:0000255|HAMAP-Rule:MF_00033}; AltName: Full=Undecaprenyl-PP-MurNAc-pentapeptide-UDPGlcNAc
    GlcNAc transferase {ECO:0000255|HAMAP-Rule:MF_00033};'
  gene_info: Name=murG {ECO:0000255|HAMAP-Rule:MF_00033}; OrderedLocusNames=PP_1337;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the glycosyltransferase 28 family. MurG
  protein_domains: GlcNAc_MurG. (IPR006009); Glyco_trans_28_C. (IPR007235); GlycoTrans_28_N.
    (IPR004276); Glyco_tran_28_C (PF04101); Glyco_transf_28 (PF03033)
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
citation_count: 13
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: murG-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: murG-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88N76
- **Protein Description:** RecName: Full=UDP-N-acetylglucosamine--N-acetylmuramyl-(pentapeptide) pyrophosphoryl-undecaprenol N-acetylglucosamine transferase {ECO:0000255|HAMAP-Rule:MF_00033}; EC=2.4.1.227 {ECO:0000255|HAMAP-Rule:MF_00033}; AltName: Full=Undecaprenyl-PP-MurNAc-pentapeptide-UDPGlcNAc GlcNAc transferase {ECO:0000255|HAMAP-Rule:MF_00033};
- **Gene Information:** Name=murG {ECO:0000255|HAMAP-Rule:MF_00033}; OrderedLocusNames=PP_1337;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the glycosyltransferase 28 family. MurG
- **Key Domains:** GlcNAc_MurG. (IPR006009); Glyco_trans_28_C. (IPR007235); GlycoTrans_28_N. (IPR004276); Glyco_tran_28_C (PF04101); Glyco_transf_28 (PF03033)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "murG" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'murG' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **murG** (gene ID: murG, UniProt: Q88N76) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# MurG (Q88N76, PP_1337) of *Pseudomonas putida* KT2440: Functional Annotation Report

**Gene:** *murG* — Ordered locus **PP_1337** | **UniProt:** Q88N76 (MURG_PSEPK), 359 aa, PE=3 (inferred from homology)
**Enzyme:** UDP-N-acetylglucosamine–N-acetylmuramyl-(pentapeptide) pyrophosphoryl-undecaprenol N-acetylglucosamine transferase — **EC 2.4.1.227**
**Family:** Glycosyltransferase 28 (GT28), MurG subfamily; GT-B superfamily (HAMAP rule MF_00033)
**Domains:** GlcNAc_MurG (IPR006009); Glyco_trans_28_N (IPR004276, PF03033); Glyco_trans_28_C (IPR007235, PF04101)

---

## Summary

**MurG is the essential, membrane-associated glycosyltransferase that catalyzes the final cytoplasmic step of bacterial peptidoglycan precursor synthesis.** In *Pseudomonas putida* KT2440, the *murG* gene (ordered locus PP_1337; UniProt Q88N76) encodes a 359-residue protein of the glycosyltransferase 28 (GT28) family, MurG subfamily, with enzyme classification EC 2.4.1.227. The enzyme transfers *N*-acetylglucosamine (GlcNAc) from the soluble nucleotide-sugar donor **UDP-GlcNAc** onto the C4 hydroxyl of the *N*-acetylmuramic acid (MurNAc) moiety of the membrane-anchored acceptor **lipid I** (undecaprenyl-pyrophosphoryl-MurNAc-pentapeptide), producing the β-1,4-linked disaccharide **lipid II**. Lipid II is the complete, minimal repeating subunit of peptidoglycan and the substrate that is subsequently flipped across the inner membrane and polymerized into the cell wall.

The mechanistic and structural understanding of MurG derives predominantly from precise work on the *Escherichia coli* ortholog, which is the archetype of a large superfamily of metal-ion–independent, NDP-sugar–utilizing glycosyltransferases. MurG adopts a two-domain **GT-B fold**: the C-terminal domain binds the UDP-GlcNAc donor and the N-terminal domain binds the lipid I acceptor, with catalysis occurring in the interdomain cleft. Kinetically, MurG follows a **compulsory ordered Bi-Bi mechanism** in which UDP-GlcNAc binds before lipid I. As a **peripheral membrane protein**, MurG operates on the cytoplasmic (inner) leaflet of the inner membrane; a hydrophobic patch ringed by basic residues mediates membrane docking, and the anionic phospholipid **cardiolipin** specifically enhances its activity on lipid I.

Because MurG is essential, universally present in peptidoglycan-synthesizing bacteria, and absent from humans, it is a long-standing target for antibacterial drug discovery. Its function in *P. putida* KT2440 is assigned by strong sequence homology (HAMAP rule MF_00033; UniProt protein-existence level PE=3, "inferred from homology"); no *P. putida*-specific enzymological study exists, but the conservation of the catalytic architecture and the essentiality of the pathway make the annotation highly reliable. Identity verification confirms the correct target: the gene symbol *murG*, the EC number, GT28/MurG family membership, and the InterPro/Pfam domains are all mutually consistent with the UniProt record for Q88N76 in *Pseudomonas putida* KT2440, and the retrieved 359-aa sequence (`MAAEGKNVLIMAGGTGGH…`) contains the conserved N-terminal glycine-rich acceptor-binding motif characteristic of the family.

---

## Key Findings

### Finding 1 — MurG catalyzes the final cytoplasmic step of lipid II synthesis

MurG (Q88N76, PP_1337) is the terminal enzyme of the intracellular (cytoplasmic) phase of peptidoglycan biosynthesis. It is a membrane-associated glycosyltransferase that couples *N*-acetylglucosamine to the **C4 hydroxyl** of the lipid-linked *N*-acetylmuramic acid derivative (lipid I), forming the β-linked disaccharide (lipid II) that constitutes the minimal repeating subunit of peptidoglycan ([PMID: 12022887](https://pubmed.ncbi.nlm.nih.gov/12022887/)). The reaction can be written explicitly as:

```
UDP-GlcNAc  +  lipid I  →  UDP  +  lipid II
(donor)        (acceptor)

lipid I  = undecaprenyl-PP-MurNAc-pentapeptide
lipid II = undecaprenyl-PP-MurNAc(-pentapeptide)-β(1→4)-GlcNAc
```

The regiochemistry is precise: GlcNAc is joined through a **β-1,4 glycosidic linkage** to the C4-hydroxyl of MurNAc, matching the glycan backbone geometry of mature peptidoglycan. The UniProt annotation for Q88N76 assigns EC 2.4.1.227 with the systematic name "UDP-*N*-acetylglucosamine—*N*-acetylmuramyl-(pentapeptide) pyrophosphoryl-undecaprenol *N*-acetylglucosamine transferase," placing the protein in the GT28 family, MurG subfamily, under HAMAP rule MF_00033. As stated in the primary literature, MurG is "the last enzyme involved in the intracellular phase of peptidoglycan synthesis, [and] is a membrane-associated glycosyltransferase that couples N-acetyl glucosamine to the C4 hydroxyl of a lipid-linked N-acetyl muramic acid derivative (lipid I) to form the beta-linked disaccharide (lipid II) that is the minimal subunit of peptidoglycan" ([PMID: 12022887](https://pubmed.ncbi.nlm.nih.gov/12022887/)).

The lipid intermediates lipid I and lipid II serve as the specific molecular **link between the intracellular synthesis of the peptidoglycan monomer unit and the subsequent extracytoplasmic polymerization reactions** ([PMID: 18063720](https://pubmed.ncbi.nlm.nih.gov/18063720/)). MurG therefore completes the assembly of the disaccharide-pentapeptide building block on the cytoplasmic face before it is exported and stitched into the sacculus.

**Substrate specificity.** The donor is the soluble nucleotide sugar UDP-GlcNAc; the acceptor is specifically lipid I, with its 55-carbon (C55) undecaprenyl-pyrophosphate anchor and MurNAc-pentapeptide headgroup. Notably, studies with lipid-chain-truncated analogues showed that MurG's intrinsic acceptor preference does not strictly require the full undecaprenyl chain — a shortened lipid acceptor is in fact catalytically preferred in vitro — indicating that the C55 carrier is important for membrane anchoring and downstream pathway steps rather than for MurG catalysis per se ([PMID: 12022887](https://pubmed.ncbi.nlm.nih.gov/12022887/)).

**Organism-specific note.** In Gram-negative bacteria such as *P. putida*, the third residue of the stem pentapeptide is *meso*-diaminopimelate (mDAP) rather than L-Lys. MurG's chemistry acts on the sugar/lipid portion and is insensitive to the stem-peptide identity, so the DAP-type peptidoglycan of *P. putida* is fully compatible with the conserved MurG reaction.

### Finding 2 — Two-domain GT-B fold and ordered Bi-Bi mechanism

The three-dimensional architecture of MurG was established by the 2.5-Å crystal structure of *E. coli* MurG in complex with its donor substrate UDP-GlcNAc: "Here we present the 2.5-Å crystal structure of *Escherichia coli* MurG in complex with its donor substrate, UDP-GlcNAc" ([PMID: 12538870](https://pubmed.ncbi.nlm.nih.gov/12538870/)). MurG has a **two-domain (GT-B) architecture** typical of a superfamily of metal-ion–independent NDP-glycosyltransferases: the **C-terminal domain binds the UDP-GlcNAc donor**, while the **N-terminal domain binds the lipid I acceptor**, with the catalytic cleft formed between the two domains. This matches the two-domain Pfam architecture of Q88N76 (Glyco_trans_28_N and Glyco_trans_28_C).

Kinetically, MurG follows a **compulsory ordered Bi-Bi mechanism in which the donor sugar (UDP-GlcNAc) binds first**, before the lipid acceptor ([PMID: 12022887](https://pubmed.ncbi.nlm.nih.gov/12022887/)). This ordered binding is mechanistically consistent with the structure: donor binding in the C-terminal domain likely organizes the interdomain cleft for productive acceptor engagement. MurG is regarded as **"a paradigm for a large family of metal ion-independent glycosyltransferases found in both eukaryotes and prokaryotes"** ([PMID: 12455415](https://pubmed.ncbi.nlm.nih.gov/12455415/)), meaning that lessons learned from MurG generalize across the GT-B superfamily (see also the broader structural survey in [PMID: 11042447](https://pubmed.ncbi.nlm.nih.gov/11042447/)).

The *P. putida* protein Q88N76 is 359 amino acids long, and its N-terminus (`MAAEGKNVLIMAGGTGGH…`) contains the conserved glycine-rich motif characteristic of the acceptor-binding N-terminal domain. This sequence conservation with *E. coli* MurG is the structural basis for the HAMAP MF_00033 annotation transfer and provides confidence that the *P. putida* enzyme adopts the same GT-B fold and uses the same ordered catalytic mechanism.

### Finding 3 — Peripheral membrane protein acting at the cytoplasmic face; cardiolipin preference

MurG is not an integral membrane protein but a **peripheral (membrane-associated) glycosyltransferase**. The *E. coli* crystal structure "contains a hydrophobic patch surrounded by basic residues that may represent a membrane association site" ([PMID: 12813070](https://pubmed.ncbi.nlm.nih.gov/12813070/)). This amphipathic surface feature allows MurG to dock onto the inner membrane and reach into the lipid bilayer to access its membrane-embedded acceptor, rather than spanning the membrane via a transmembrane helix.

Critically, the lipid environment modulates catalytic activity. When lipid I was incorporated into pure lipid vesicles of defined composition, **"the MurG activity is higher for vesicles containing cardiolipin than for vesicles with phosphatidylglycerol"** ([PMID: 12813070](https://pubmed.ncbi.nlm.nih.gov/12813070/)), indicating a special role for the anionic phospholipid cardiolipin in supporting the enzyme's function. Cardiolipin is enriched at bacterial cell poles and division septa — the very sites of active cell-wall synthesis — so its stimulation of MurG plausibly couples the enzyme's activity to the spatial organization of the growing cell envelope.

The topology of the reaction is well defined: both the substrate lipid I and the product lipid II are anchored to the membrane by the C55 undecaprenyl chain ([PMID: 12022887](https://pubmed.ncbi.nlm.nih.gov/12022887/)); the glycosyl transfer occurs on the **inner (cytoplasmic) leaflet**; and the resulting lipid II is subsequently **translocated across the cytoplasmic membrane** by a flippase before its extracytoplasmic polymerization ([PMID: 18063720](https://pubmed.ncbi.nlm.nih.gov/18063720/)). MurG thus performs the last chemical modification of the precursor that is accessible from the cytoplasm.

### Finding 4 — Essential, conserved enzyme and validated antibacterial target

MurG is described as **"an essential bacterial glycosyltransferase that is involved in the biosynthesis of peptidoglycan. The enzyme is found in all organisms that synthesize peptidoglycan and is a target for the design of new antibiotics"** ([PMID: 12455415](https://pubmed.ncbi.nlm.nih.gov/12455415/)). Within the peptidoglycan pathway, the two membrane-linked catalysts **MraY and MurG serve as essential catalysts for lipid I and lipid II formation**, respectively ([PMID: 42128180](https://pubmed.ncbi.nlm.nih.gov/42128180/); see also the comprehensive review [PMID: 28201974](https://pubmed.ncbi.nlm.nih.gov/28201974/)). MraY generates lipid I from UDP-MurNAc-pentapeptide and undecaprenyl phosphate; MurG then converts lipid I to lipid II. These are the only two membrane steps of the cytoplasmic pathway, and both are indispensable.

The essentiality and druggability of MurG have been exploited experimentally. A scintillation proximity assay developed for *E. coli* MurG inhibitors showed that the lantibiotic **nisin** and the glycopeptide **vancomycin** inhibit the MurG reaction — in these cases by sequestering the lipid II product/substrate rather than by binding the enzyme's active site directly ([PMID: 15793120](https://pubmed.ncbi.nlm.nih.gov/15793120/)). By contrast, inhibitors of other peptidoglycan enzymes (penicillin G, moenomycin, bacitracin) had no effect on the MurG step, underscoring the specificity of the assay. Importantly, the antibiotic **ramoplanin**, once proposed to inhibit MurG by binding lipid I, was shown instead to act downstream by binding lipid II as a dimer, inhibiting the transglycosylases rather than MurG directly ([PMID: 12862463](https://pubmed.ncbi.nlm.nih.gov/12862463/)) — a useful correction when reasoning about MurG-targeting strategies.

In *P. putida* KT2440, *murG* is annotated as the ordered locus **PP_1337**, consistent with its expected residence within the conserved **division and cell-wall (dcw/mra) gene cluster**, physically adjacent to *ftsW* and the *mur* ligases (*murC–murF*) and *mraY*. This genomic context — conserved across Gram-negative bacteria — reinforces the functional assignment, because genes in the *dcw* cluster are co-regulated components of the same peptidoglycan-synthesis and cell-division machine, and MurG's product lipid II is the substrate for the divisome's peptidoglycan synthases during septation and elongation.

---

## Mechanistic Model / Interpretation

MurG sits at the pivotal junction between the soluble, cytoplasmic assembly of the peptidoglycan monomer and its membrane-embedded export and polymerization. The following schematic places PP_1337 in the *P. putida* peptidoglycan "lipid cycle":

```
 CYTOPLASM
   UDP-GlcNAc ─► [GlmS/GlmM/GlmU] ─► UDP-MurNAc ─► [MurA–MurF ligases]
                                                          │
                                                          ▼
                                            UDP-MurNAc-pentapeptide
                                                          │
 INNER MEMBRANE ── MraY (integral) ───────────────────────┤
 (cytoplasmic        C55-P + UDP-MurNAc-pentapeptide      │
  leaflet)                 → LIPID I + UMP                 ▼
                                                     ┌──────────┐
                    UDP-GlcNAc (donor) ─────────────►│   MurG   │ ◄── cardiolipin
                                                     │ PP_1337  │     (activity ↑)
                                    LIPID I ────────►│  GT-B    │
                                   (acceptor)        └────┬─────┘
                                                          │ β(1→4) GlcNAc transfer
                                                          ▼
                                                    LIPID II + UDP
                                                          │
                                   ── flippase (MurJ/FtsW) translocation ──►
 PERIPLASM
                                   transglycosylation / transpeptidation (PBPs)
                                                     → mature PEPTIDOGLYCAN
```

Three features integrate the findings into a coherent picture:

1. **Chemistry (Findings 1 & 2).** MurG is a GT-B glycosyltransferase that transfers GlcNAc with formation of a β-1,4 bond to the MurNAc C4-OH. The ordered Bi-Bi kinetics (UDP-GlcNAc first, lipid I second) match the structural logic of donor binding in the C-terminal domain preceding acceptor engagement in the interdomain cleft. The enzyme is metal-ion independent.

2. **Location (Finding 3).** The reaction is spatially confined to the cytoplasmic face of the inner membrane. MurG's peripheral association — via a hydrophobic, basic-residue-rimmed patch — lets it capture the membrane-anchored lipid I while drawing soluble UDP-GlcNAc from the cytoplasm. Cardiolipin, enriched at poles and septa, stimulates the enzyme, spatially coupling lipid II production to sites of active envelope growth.

3. **Pathway role and essentiality (Finding 4).** MurG and MraY are the two essential membrane catalysts that convert the soluble precursor into the exportable lipid II. Blocking MurG halts peptidoglycan synthesis and is lethal — the basis for its status as an antibacterial target. Its position immediately downstream of MraY and immediately upstream of lipid II flipping makes it a strategic bottleneck.

The following table summarizes the enzyme's defining parameters:

| Property | Value / Description | Evidence |
|---|---|---|
| Gene / locus | *murG* / PP_1337 | UniProt Q88N76 |
| Length | 359 aa | UniProt Q88N76 |
| Enzyme class | EC 2.4.1.227 | UniProt; HAMAP MF_00033 |
| Family / fold | GT28, MurG subfamily; GT-B two-domain fold | [PMID: 12538870](https://pubmed.ncbi.nlm.nih.gov/12538870/) |
| Donor substrate | UDP-GlcNAc (binds C-terminal domain) | [PMID: 12538870](https://pubmed.ncbi.nlm.nih.gov/12538870/) |
| Acceptor substrate | Lipid I (binds N-terminal domain) | [PMID: 12022887](https://pubmed.ncbi.nlm.nih.gov/12022887/) |
| Product | Lipid II (β-1,4 GlcNAc-MurNAc disaccharide) | [PMID: 12022887](https://pubmed.ncbi.nlm.nih.gov/12022887/) |
| Linkage formed | β-1,4 to MurNAc C4-OH | [PMID: 12022887](https://pubmed.ncbi.nlm.nih.gov/12022887/) |
| Kinetic mechanism | Compulsory ordered Bi-Bi (donor first) | [PMID: 12022887](https://pubmed.ncbi.nlm.nih.gov/12022887/) |
| Metal requirement | None (metal-ion–independent) | [PMID: 12455415](https://pubmed.ncbi.nlm.nih.gov/12455415/) |
| Localization | Peripheral membrane, cytoplasmic (inner) leaflet | [PMID: 12813070](https://pubmed.ncbi.nlm.nih.gov/12813070/); [PMID: 18063720](https://pubmed.ncbi.nlm.nih.gov/18063720/) |
| Lipid preference | Cardiolipin > phosphatidylglycerol | [PMID: 12813070](https://pubmed.ncbi.nlm.nih.gov/12813070/) |
| Essentiality | Essential; validated antibacterial target | [PMID: 12455415](https://pubmed.ncbi.nlm.nih.gov/12455415/); [PMID: 42128180](https://pubmed.ncbi.nlm.nih.gov/42128180/) |

---

## Evidence Base

The functional annotation rests on a well-developed body of enzymology and structural biology, almost entirely on the *E. coli* ortholog, transferred to *P. putida* Q88N76 by strong homology (HAMAP MF_00033; UniProt PE=3).

| PMID | Title (abbrev.) | Contribution | Support / caveat |
|---|---|---|---|
| [12022887](https://pubmed.ncbi.nlm.nih.gov/12022887/) | *Intrinsic lipid preferences and kinetic mechanism of E. coli MurG* | Defines the reaction (GlcNAc → C4-OH of MurNAc, β-linkage), ordered Bi-Bi mechanism, membrane-anchored substrates | Strong primary evidence; *E. coli* enzyme |
| [12538870](https://pubmed.ncbi.nlm.nih.gov/12538870/) | *Crystal structure of the MurG:UDP-GlcNAc complex* | 2.5-Å structure establishing GT-B two-domain fold; donor binds C-terminal domain | Definitive structural evidence; *E. coli* |
| [12455415](https://pubmed.ncbi.nlm.nih.gov/12455415/) | *E. coli MurG: a paradigm for a superfamily of glycosyltransferases* | Establishes essentiality, universal conservation, metal-independence, antibiotic-target status | Authoritative review/analysis |
| [12813070](https://pubmed.ncbi.nlm.nih.gov/12813070/) | *Membrane interaction of MurG: a special role for cardiolipin* | Identifies peripheral-membrane hydrophobic/basic patch; cardiolipin enhances activity over PG | Primary biochemical evidence; *E. coli* |
| [18063720](https://pubmed.ncbi.nlm.nih.gov/18063720/) | *Lipid intermediates in the biosynthesis of bacterial peptidoglycan* | Places lipid I/II as the link between cytoplasmic synthesis and extracytoplasmic polymerization; lipid II made cytoplasmically then translocated | Authoritative review (van Heijenoort) |
| [15793120](https://pubmed.ncbi.nlm.nih.gov/15793120/) | *Scintillation proximity assay for E. coli MurG/MraY inhibitors* | Demonstrates assayable MurG reaction; nisin and vancomycin inhibit by sequestering lipid II | Primary methods/screening paper |
| [12862463](https://pubmed.ncbi.nlm.nih.gov/12862463/) | *Ramoplanin inhibits transglycosylases by binding lipid II* | Corrects prior belief that ramoplanin blocks the MurG step; it acts downstream on lipid II | Primary evidence; refutes a MurG-inhibition model |
| [42128180](https://pubmed.ncbi.nlm.nih.gov/42128180/) | *Exploiting Mur enzyme characteristics for antibacterial drug design* | Confirms MraY and MurG as essential membrane catalysts for lipid I/II | Recent review |
| [28201974](https://pubmed.ncbi.nlm.nih.gov/28201974/) | *Mur Ligase Inhibitors as Anti-bacterials* | Situates MurG at the end of the cytoplasmic Mur pathway; no human homolog | Comprehensive review |
| [11042447](https://pubmed.ncbi.nlm.nih.gov/11042447/) | *Glycosyltransferase structure and mechanism* | Places MurG among solved GT structures; structural basis of catalysis and classification | Review; structural context |

Additional structural context comes from related GT-B glycosyltransferases that share MurG's architecture — bacteriophage T4 β-glucosyltransferase, *Bacillus subtilis* SpsA, and the antibiotic glucosyltransferase GtfB ([PMID: 11470430](https://pubmed.ncbi.nlm.nih.gov/11470430/)) — and from family-28 relatives such as *Campylobacter jejuni* PseG, whose structure is explicitly noted to resemble *E. coli* MurG ([PMID: 19483088](https://pubmed.ncbi.nlm.nih.gov/19483088/)).

**Identity verification.** Every line of evidence is congruent with the target record: the gene symbol *murG*, EC 2.4.1.227, GT28/MurG family membership, the InterPro (GlcNAc_MurG IPR006009; Glyco_trans_28_C IPR007235; GlycoTrans_28_N IPR004276) and Pfam (PF04101, PF03033) domains, and the *P. putida* KT2440 organism all agree. No conflicting literature for a different "murG"-symbol gene was encountered. The annotation transfer to *P. putida* Q88N76 is well justified.

---

## Supported vs. Refuted Hypotheses

**Supported (strong evidence):**
- MurG is a UDP-GlcNAc:lipid I β-1,4-GlcNAc transferase producing lipid II (EC 2.4.1.227). *(Direct enzymology + structure in E. coli; homology for Q88N76.)*
- Two-domain GT-B fold; ordered Bi-Bi mechanism, donor first; metal-ion independent.
- Peripheral inner-membrane protein acting on the cytoplasmic face; anionic-lipid/cardiolipin preference.
- Essential, dcw-cluster gene, validated antibacterial target with no human homolog.

**Refuted / corrected:**
- MurG is **not** the direct target of ramoplanin; that antibiotic binds lipid II downstream of the MurG step ([PMID: 12862463](https://pubmed.ncbi.nlm.nih.gov/12862463/)).
- The natural undecaprenyl (C55) chain is **not** required for MurG catalysis — a shorter lipid acceptor is kinetically preferred in vitro — so the carrier lipid's role is anchoring/downstream processing, not MurG chemistry ([PMID: 12022887](https://pubmed.ncbi.nlm.nih.gov/12022887/)).

---

## Limitations and Knowledge Gaps

1. **No *P. putida*-specific enzymology.** All kinetic, structural, and lipid-preference data derive from *E. coli* (or other bacteria). The *P. putida* KT2440 MurG has not been crystallized, purified, or assayed directly. UniProt lists Q88N76 at protein-existence level PE=3 ("inferred from homology"). Given the high sequence conservation and pathway essentiality, the inference is strong, but species-specific kinetic parameters (Km, kcat), exact lipid preferences, and any *Pseudomonas*-specific regulation remain unmeasured.

2. **Catalytic-residue identity not mapped onto Q88N76.** While the GT-B fold and donor/acceptor domain assignment are established, this report does not pinpoint the exact catalytic base(s) and donor-binding residues in the *P. putida* sequence. In related GT-B enzymes, conserved acidic residues (e.g., an Asp general base) and Lys/Glu donor-binding residues are identified; mapping the equivalents onto Q88N76 would require alignment and, ideally, mutagenesis.

3. **Transition-state chemistry.** The β-linkage stereochemistry is established, but the detailed mechanism (single-displacement vs alternatives) for MurG specifically remains an active question for GT-B enzymes generally.

4. **Quaternary state and interactions.** Some literature suggests higher-order functional units for lipid II–synthesizing glycosyltransferases ([PMID: 34258006](https://pubmed.ncbi.nlm.nih.gov/34258006/)); the oligomeric state of *P. putida* MurG in vivo, and its coordination with MraY, MurJ, FtsW, and the elongasome/divisome, are not directly established for this strain.

---

## Proposed Follow-up Experiments / Actions

1. **Direct enzymatic validation in *P. putida*.** Clone and overexpress PP_1337, reconstitute a lipid I → lipid II assay (e.g., the scintillation-proximity or a fluorescence-based method), and measure Km(UDP-GlcNAc), Km(lipid I), and kcat for the *Pseudomonas* enzyme; confirm the ordered Bi-Bi mechanism.

2. **Structure determination.** Solve the *P. putida* MurG structure (X-ray, cryo-EM, or a high-confidence AlphaFold model with experimental validation) in apo and UDP-GlcNAc–bound states to confirm the GT-B fold and locate the membrane-association patch and catalytic residues; dock an mDAP-type lipid I.

3. **Catalytic-residue mapping.** Align Q88N76 against *E. coli* MurG and characterized GT-B enzymes to nominate the general base and donor-binding residues, then test by site-directed mutagenesis with activity assays.

4. **Membrane/lipid dependence.** Reconstitute *P. putida* MurG activity in defined vesicles (cardiolipin vs phosphatidylglycerol vs phosphatidylethanolamine) to test whether the cardiolipin preference observed in *E. coli* holds; use a MurG fluorescent fusion to test pole/septum localization.

5. **Essentiality and inhibitor sensitivity.** Confirm *murG* essentiality in *P. putida* KT2440 (conditional knockdown/CRISPRi) and test whether nisin, vancomycin, and candidate MurG-targeting compounds inhibit growth and cause lipid II accumulation, exploiting *P. putida*'s value as a robust chassis organism.

6. **Genomic-context confirmation.** Verify the *dcw/mra* cluster organization around PP_1337 (adjacency to *ftsW*, *murC–murF*, *mraY*) to consolidate the functional and regulatory context in this strain.

---

## Conclusion

MurG (Q88N76 / PP_1337) of *Pseudomonas putida* KT2440 is the essential, peripheral-membrane, GT-B–fold glycosyltransferase (GT28 family, EC 2.4.1.227) that carries out the last cytoplasmic reaction of peptidoglycan precursor synthesis: β-1,4 transfer of GlcNAc from UDP-GlcNAc onto the MurNAc C4-hydroxyl of lipid I to form lipid II, via a metal-independent, ordered Bi-Bi mechanism at the cytoplasmic face of the inner membrane, where cardiolipin promotes its activity. The assignment for *P. putida* is inferred from strong homology to experimentally characterized orthologs (chiefly *E. coli*), and the enzyme is a validated, universally conserved antibacterial target with no human counterpart.


## Artifacts

- [OpenScientist final report](murG-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](murG-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:12022887
2. PMID:18063720
3. PMID:12538870
4. PMID:12455415
5. PMID:11042447
6. PMID:12813070
7. PMID:42128180
8. PMID:28201974
9. PMID:15793120
10. PMID:12862463
11. PMID:11470430
12. PMID:19483088
13. PMID:34258006