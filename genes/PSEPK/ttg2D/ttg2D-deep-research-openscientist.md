---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T02:37:34.072031'
end_time: '2026-09-01T02:52:53.999727'
duration_seconds: 919.93
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: ttg2D
  gene_symbol: ttg2D
  uniprot_accession: Q88P91
  protein_description: 'SubName: Full=Toluene tolerance protein {ECO:0000313|EMBL:AAN66586.1};'
  gene_info: Name=ttg2D {ECO:0000313|EMBL:AAN66586.1}; OrderedLocusNames=PP_0961 {ECO:0000313|EMBL:AAN66586.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: MlaC/ttg2D. (IPR008869); Tgt2/MlaC_sf. (IPR042245); MlaC (PF05494)
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
citation_count: 9
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: ttg2D-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: ttg2D-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88P91
- **Protein Description:** SubName: Full=Toluene tolerance protein {ECO:0000313|EMBL:AAN66586.1};
- **Gene Information:** Name=ttg2D {ECO:0000313|EMBL:AAN66586.1}; OrderedLocusNames=PP_0961 {ECO:0000313|EMBL:AAN66586.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** MlaC/ttg2D. (IPR008869); Tgt2/MlaC_sf. (IPR042245); MlaC (PF05494)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ttg2D" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ttg2D' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ttg2D** (gene ID: ttg2D, UniProt: Q88P91) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *ttg2D* (PP_0961 / Q88P91) in *Pseudomonas putida* KT2440

## Summary

The gene **ttg2D** (ordered locus name **PP_0961**; UniProt **Q88P91**) of *Pseudomonas putida* strain KT2440 encodes the **soluble periplasmic phospholipid-binding protein of the Ttg2 ABC transport system** — the *Pseudomonas* ortholog of **MlaC** in the **Mla (Maintenance of Lipid Asymmetry) pathway**. Despite its historical "toluene-tolerance protein" name (which derives from a solvent-tolerance genetic screen, not from any role in toluene metabolism), its molecular function is not enzymatic. Rather, Ttg2D is a **glycerophospholipid carrier/shuttle** that binds diacyl phospholipids inside a hydrophobic internal cavity and ferries them across the aqueous periplasm between the inner and outer membranes.

The functional assignment is exceptionally well supported. The direct ortholog in *Pseudomonas aeruginosa* (also named Ttg2D) has been experimentally characterized by X-ray crystallography and native mass spectrometry as "the soluble periplasmic phospholipid-binding component of an ABC transport system," carrying two diacyl glycerophospholipids or one cardiolipin per molecule, with notably promiscuous binding across molecular species [PMID: 33837253]. The *P. putida* KT2440 protein itself has been crystallized in a **lipid-bound state (PDB 5UWB)**, providing direct structural evidence for the target protein rather than mere inference from an ortholog. The two proteins are 65% identical over their full length, well above the threshold for confident functional transfer.

Ttg2D operates in the periplasm as the mobile intermediary of the Mla pathway, which spans the entire Gram-negative cell envelope: the outer-membrane MlaA–OmpC/F complex, the periplasmic shuttle MlaC/Ttg2D, and the inner-membrane ABC transporter MlaFEDB (encoded in *P. putida* by the adjacent PP_0958–PP_0960 + PP_0962 genes, i.e. the Ttg2ABC system). By transporting mislocalized phospholipids from the outer membrane back to the inner membrane (retrograde transport), the system maintains the lipid asymmetry of the outer membrane that constitutes the primary permeability barrier of the cell. This barrier function underlies the observed physiological roles of the *ttg2* locus in *P. putida* organic-solvent (toluene) tolerance and in low-level intrinsic resistance to lipophilic antibiotics.

---

## Gene/Protein Identity Verification

Before presenting findings, the mandatory identity checks required by the research brief were completed and **all passed**:

| Verification step | Result |
|---|---|
| Gene symbol "ttg2D" matches protein description | ✅ "Toluene tolerance protein"; ttg2D nomenclature originates from the *toluene tolerance gene 2* locus [PMID: 9658016] |
| Organism correct | ✅ *Pseudomonas putida* KT2440 (ATCC 47054 / DSM 6125 / NCIMB 11950); KEGG entry ppu:PP_0961 |
| Protein family/domains align with literature | ✅ Pfam PF05494 (MlaC), InterPro IPR008869 (MlaC/ttg2D) and IPR042245 (Tgt2/MlaC_sf) — all correspond to the MlaC periplasmic phospholipid shuttle family |
| Literature is for the same gene, not a homonym | ✅ The experimentally-characterized *P. aeruginosa* Ttg2D (PA4453) is a direct 65%-identical ortholog in the same genus |

There was **no gene-symbol ambiguity problem**: the literature retrieved describes the same protein family in the same and closely related organisms. Functional transfer is therefore direct, not analogical. Importantly, the "toluene tolerance" name should not be confused with the *TtgABC*/*TtgGHI* RND-family efflux pumps of *P. putida*, which are distinct multidrug/solvent efflux systems; Ttg2D is not itself an efflux transporter.

### Molecular identity card

| Attribute | Value |
|---|---|
| UniProt accession | Q88P91 (Q88P91_PSEPK) |
| Gene / locus | *ttg2D* / PP_0961 |
| Organism | *Pseudomonas putida* KT2440 |
| Length | 215 aa |
| Signal peptide | Sec-type, residues 1–22 (cleaved) → mature soluble chain 23–215 |
| Domain / family | Pfam **PF05494 (MlaC)**; InterPro **IPR008869 (MlaC/ttg2D)**, **IPR042245 (Tgt2/MlaC_sf)**; Gene3D 3.10.450.710 |
| Structures | **PDB 4FCZ** (apo), **PDB 5UWB** (lipid-bound) — both of the *P. putida* protein |
| KEGG | ppu:PP_0961 |

---

## Key Findings

### Finding 1 — Identity: Ttg2D is the MlaC-family periplasmic component of the Ttg2/Mla ABC system

Ttg2D (PP_0961 / Q88P91) is a 215-amino-acid protein bearing an N-terminal Sec-dependent signal peptide (residues 1–22) that is cleaved to yield the mature soluble chain (residues 23–215). It is assigned to Pfam **PF05494 (MlaC)** and InterPro families **IPR008869 (MlaC/ttg2D)** and **IPR042245 (Tgt2/MlaC_sf)**, with the Gene3D superfamily fold 3.10.450.710. The KEGG identifier is ppu:PP_0961, and two crystal structures exist (PDB **4FCZ** and **5UWB**).

The definitive functional anchor is the experimentally-characterized *P. aeruginosa* ortholog, also named Ttg2D, which is described as *"the soluble periplasmic phospholipid-binding component of an ABC transport system thought to be involved in maintaining the asymmetry of the outer membrane"* [PMID: 33837253]. The *ttg2* nomenclature itself traces to a *P. putida* solvent-tolerance study that identified Ttg1 and Ttg2 as ATP-binding-cassette (ABC) transporter homologs [PMID: 9658016]. Together these place Ttg2D unambiguously as the periplasmic phospholipid-binding subunit of a Ttg2/Mla ABC transporter.

### Finding 2 — Primary function: a promiscuous glycerophospholipid carrier

Ttg2D's primary molecular function is **non-enzymatic phospholipid binding and transport**. It does not catalyze a chemical reaction; it captures glycerophospholipid molecules in a hydrophobic internal cavity and carries them.

The strongest biochemical evidence comes from the *P. aeruginosa* ortholog. Its 2.5 Å crystal structure shows a cavity accommodating **four acyl chains**, and native/denaturing mass spectrometry of protein produced both heterologously and isolated directly from the periplasm confirmed that *"Ttg2D … can carry two diacyl glycerophospholipids as well as one cardiolipin"* [PMID: 33837253]. Crucially, *"binding is notably promiscuous, allowing the transport of various molecular species"* [PMID: 33837253] — establishing broad substrate specificity spanning phosphatidylethanolamine, phosphatidylglycerol and cardiolipin rather than a single lipid species.

At the mechanistic level, the homologous *E. coli* MlaC structure reveals a **pivoting β-sheet mechanism** that opens and closes the phospholipid-binding pocket, enabling capture and release of cargo: the authors *"solve the crystal structure of MlaC in its phospholipid-free closed apo conformation, revealing a pivoting β-sheet mechanism that functions to open and close the phospholipid-binding pocket"* [PMID: 31235958]. In the assembled pathway, *"Mla uses a shuttle-like mechanism to move lipids between the MlaFEDB inner membrane complex and the MlaA-OmpF/C OM complex, via a periplasmic lipid-binding protein, MlaC"* [PMID: 37100290]. Ttg2D is therefore the mobile lipid-carrier module of this shuttle.

### Finding 3 — Localization and pathway: soluble periplasmic shuttle in retrograde Mla transport

Consistent with its cleaved Sec signal peptide and the **absence of a lipobox** (i.e., it is not lipid-anchored to a membrane), Ttg2D is a **soluble protein resident in the periplasmic space**. The Mla system has *"elements in all compartments of the cell envelope: the lipoprotein MlaA in complex with the trimeric porins OmpC/F in the OM, MlaC in the periplasmic space and an ABC transporter in the inner membrane called MlaFEDB"* [PMID: 36459067]. Ttg2D corresponds to the periplasmic MlaC.

The pathway operates predominantly in the **retrograde (outer-membrane → inner-membrane) direction**. In the first hand-off step, *"the OmpC-MlaA complex transfers PLs to the periplasmic chaperone MlaC"* [PMID: 38092770], which then delivers them to the inner-membrane MlaFEDB transporter. Recent biochemical work *"strongly support[s] retrograde transport"* as the physiological direction [PMID: 36459067]. Directionality is powered by ATP: ATP hydrolysis at MlaFEDB disrupts the lipid-binding equilibrium to drive directional retrograde movement critical for outer-membrane asymmetry [PMID: 34873038]. Thus Ttg2D performs its function **in the periplasm**, cycling between docking at the outer-membrane and inner-membrane complexes.

### Finding 4 — Physiological consequences: solvent tolerance and intrinsic antibiotic resistance via barrier integrity

The downstream physiological roles of the Ttg2 system flow from its maintenance of outer-membrane barrier integrity. In the original *P. putida* genetics, the *ttg2* locus was recovered by transposon mutagenesis as an ABC-transporter locus whose disruption sensitizes cells to toluene; the study concluded that *"active efflux mechanism and efficient repair of damaged membranes were important in toluene resistance"* [PMID: 9658016]. In *P. aeruginosa*, *"gene knockout experiments in … multidrug-resistant strains reveal that the Ttg2 system is involved in low-level intrinsic resistance against certain antibiotics that use a lipid-mediated pathway to permeate through membranes"* [PMID: 33837253]. These are the precise, mechanism-linked phenotypes (barrier maintenance) rather than broad pleiotropy — they are downstream consequences of the single molecular role of Ttg2D, not separate activities.

### Finding 5 — Genomic context: a complete ttg2/Mla operon at PP_0958–PP_0962

Ttg2D sits within a canonical Mla gene cluster. KEGG annotation of PP_0958–PP_0962 in KT2440 assigns:

| Locus | Annotation | Mla / Ttg2 equivalent |
|---|---|---|
| PP_0958 | Phospholipid ABC transporter ATP-binding subunit | MlaF / Ttg2A (ATPase) |
| PP_0959 | Phospholipid ABC transporter permease | MlaE / Ttg2B |
| PP_0960 | Phospholipid ABC transporter binding protein (MCE domain) | MlaD / Ttg2C |
| **PP_0961** | **ttg2D — toluene-tolerance protein** | **MlaC (periplasmic shuttle) — this target** |
| PP_0962 | Second toluene-tolerance protein | candidate MlaB (regulatory) |

This recapitulates the canonical MlaFEDB(+MlaC) architecture — *"the lipoprotein MlaA in complex with the trimeric porins OmpC/F in the OM, MlaC in the periplasmic space and an ABC transporter in the inner membrane called MlaFEDB"* [PMID: 36459067] — providing genomic-context ("guilt-by-association") support for the functional assignment of PP_0961 as the periplasmic MlaC/Ttg2D subunit.

### Finding 6 — Strong orthology justifies functional transfer

A global pairwise alignment (Needleman–Wunsch) of *P. putida* Ttg2D (Q88P91, 215 aa) against the experimentally-characterized *P. aeruginosa* Ttg2D (PA4453 / Q9HVW4, 215 aa) yields **143/220 = 65.0% identity**, with an essentially identical N-terminal Sec signal peptide (MISILRRGLLVLLAAFPLLALA vs MLTLLRRGLLVFLAAFPLLSMAA). Against *E. coli* MlaC (P0ADV7, 211 aa) identity is ~34% over the aligned region — sufficient to confirm shared family and fold. Structural analysis shows that *"the available structures of Ttg2D orthologs … conform a new substrate-binding-protein structural cluster"* [PMID: 33837253], meaning the *P. putida* protein belongs to the same conserved lipid-binding structural family. At 65% identity within the same genus, functional transfer from the *P. aeruginosa* biochemistry to the *P. putida* protein is robust.

### Finding 7 — Direct structural evidence for the target protein (PDB 5UWB)

Unusually for a less-characterized protein, direct structural data exist for the exact target. PDB **4FCZ** is the *"Crystal Structure of Toluene-tolerance protein from Pseudomonas putida (strain KT2440)"* (Northeast Structural Genomics Consortium target PpR99; X-ray, 2.6 Å), and PDB **5UWB** is a re-refinement of 4FCZ as the **lipid-bound crystal structure** of the same toluene-tolerance protein. These structures are of Q88P91 / PP_0961 itself, not merely an ortholog, and they fall within the Ttg2D substrate-binding-protein structural cluster [PMID: 33837253]. The lipid-bound state directly demonstrates that the *P. putida* protein binds lipid in its cavity, closing the loop between sequence-based inference and species-specific experimental fact.

---

## Mechanistic Model / Interpretation

The findings integrate into a single coherent mechanistic picture of Ttg2D as the periplasmic ferry of the Mla lipid-asymmetry pathway:

```
        OUTER MEMBRANE (OM)
   outer leaflet: LPS  ┌──────────────┐   mislocalized
                       │ MlaA–OmpC/F  │◄── phospholipid in
                       └──────┬───────┘    OM outer leaflet
                              │ (1) PL hand-off
                              ▼
        PERIPLASM      ● Ttg2D / MlaC ●      ← soluble shuttle
                       (PP_0961, Q88P91)       binds 2 diacyl PLs
                              │                 or 1 cardiolipin;
                              │ (2) shuttles     promiscuous
                              ▼
                       ┌──────────────┐
        INNER          │  MlaFEDB     │   (3) ATP hydrolysis
        MEMBRANE (IM)  │ (Ttg2 A/B/C) │       drives directionality
                       └──────────────┘
                    PP_0958 / PP_0959 / PP_0960 (+PP_0962 = MlaB?)
```

**Step 1 — Capture at the OM.** The outer-membrane MlaA–OmpC/F complex extracts phospholipids that have aberrantly accumulated in the outer leaflet of the outer membrane and transfers them to Ttg2D [PMID: 38092770].

**Step 2 — Periplasmic transit.** Ttg2D, a soluble MlaC-family protein, sequesters up to two diacyl glycerophospholipids (or one cardiolipin) in its hydrophobic cavity [PMID: 33837253]. A pivoting β-sheet closes over the pocket to shield the acyl chains from the aqueous periplasm during transit [PMID: 31235958]. Loaded Ttg2D diffuses across the periplasm to the inner membrane.

**Step 3 — Delivery to the IM and reset.** Ttg2D docks on the MlaFEDB ABC transporter (via the MlaD/Ttg2C MCE-domain hexamer) and releases its cargo. ATP hydrolysis by the MlaF/Ttg2A ATPase disrupts the lipid-binding equilibrium, imposing net retrograde directionality (OM→IM) and recycling Ttg2D for another round [PMID: 34873038; PMID: 37100290]. Cryo-EM of the MlaC–MlaD complex reveals the docking geometry and that phospholipids pass between the C-terminal helices of the MlaD hexamer to reach its central pore [PMID: 39080293].

The **net physiological output** is preservation of outer-membrane lipid asymmetry (LPS-rich outer leaflet, phospholipid inner leaflet). This asymmetry is what makes the Gram-negative OM an effective barrier to lipophilic toxins. When the *ttg2* system is lost, the barrier degrades, and the cell becomes sensitive to organic solvents such as toluene [PMID: 9658016] and to lipid-permeant antibiotics [PMID: 33837253]. This explains why a phospholipid-transport protein was originally discovered — and named — in a *toluene-tolerance* screen: the connection is indirect, through membrane-barrier integrity, not through any role in toluene metabolism.

**On directionality.** The literature notes that the transport direction of the Mla system was historically debated (anterograde IM→OM vs retrograde OM→IM), and the field's own reviews frame this explicitly ("Forward or backward, that is the question") [PMID: 36459067]. The current weight of biochemical evidence supports the retrograde model [PMID: 36459067; PMID: 38092770], and directional ATP-driven transport has been reconstituted in proteoliposomes [PMID: 34873038; PMID: 33199922]. Ttg2D's role as the periplasmic carrier is invariant regardless of the finally-settled net direction.

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution to this report |
|---|---|---|
| [PMID: 33837253](https://pubmed.ncbi.nlm.nih.gov/33837253/) | *The Pseudomonas aeruginosa substrate-binding protein Ttg2D functions as a general glycerophospholipid transporter across the periplasm* | **Cornerstone.** Direct biochemistry on the 65%-identical *P. aeruginosa* Ttg2D ortholog: periplasmic phospholipid-binding component; carries 2 diacyl PLs or 1 cardiolipin; promiscuous binding; knockout → loss of intrinsic antibiotic resistance; orthologs form a distinct SBP structural cluster |
| [PMID: 9658016](https://pubmed.ncbi.nlm.nih.gov/9658016/) | *Isolation and characterization of toluene-sensitive mutants from the toluene-resistant bacterium Pseudomonas putida GM73* | Origin of *ttg2* nomenclature; identifies Ttg2 as an ABC-transporter homolog required for toluene tolerance/membrane integrity |
| [PMID: 37100290](https://pubmed.ncbi.nlm.nih.gov/37100290/) | *Protein–protein interactions in the Mla lipid transport system probed by computational structure prediction and deep mutational scanning* | Establishes the shuttle-like mechanism: MlaC moves lipids between MlaFEDB and MlaA-OmpF/C |
| [PMID: 34873038](https://pubmed.ncbi.nlm.nih.gov/34873038/) | *ATP disrupts lipid-binding equilibrium to drive retrograde transport critical for bacterial outer membrane asymmetry* | Energetics/directionality: ATP hydrolysis drives directional retrograde transport for OM asymmetry |
| [PMID: 36459067](https://pubmed.ncbi.nlm.nih.gov/36459067/) | *Forward or backward, that is the question: phospholipid trafficking by the Mla system* | Defines the three-compartment architecture; MlaC in periplasm; supports retrograde direction |
| [PMID: 38092770](https://pubmed.ncbi.nlm.nih.gov/38092770/) | *Molecular mechanism of phospholipid transport at the bacterial outer membrane interface* | Defines the first hand-off step: OmpC-MlaA transfers PLs to periplasmic MlaC |
| [PMID: 31235958](https://pubmed.ncbi.nlm.nih.gov/31235958/) | *Evidence for phospholipid export from the bacterial inner membrane by the Mla ABC transport system* | Structural mechanism: pivoting β-sheet opens/closes the MlaC lipid pocket |
| [PMID: 33199922](https://pubmed.ncbi.nlm.nih.gov/33199922/) | *Structural insights into outer membrane asymmetry maintenance in Gram-negative bacteria by MlaFEDB* | Cryo-EM of the inner-membrane partner complex; reconstituted transport with MlaC and MlaA-OmpF |
| [PMID: 39080293](https://pubmed.ncbi.nlm.nih.gov/39080293/) | *Structure of the MlaC-MlaD complex reveals molecular basis of periplasmic phospholipid transport* | Molecular basis of the periplasmic-shuttle → inner-membrane hand-off (MlaC docking on MlaD hexamer) |

Structural databases (RCSB PDB **4FCZ**, **5UWB**), UniProt (**Q88P91**), Pfam (**PF05494**), InterPro (**IPR008869**, **IPR042245**), and KEGG (**ppu:PP_0961** and the PP_0958–PP_0962 operon) provided the sequence, domain, signal-peptide and genomic-context annotations, cross-validated against the primary literature above.

---

## Limitations and Knowledge Gaps

1. **No direct biochemistry on the KT2440 protein itself.** The quantitative binding data (stoichiometry, cardiolipin binding, promiscuity) derive from the *P. aeruginosa* ortholog [PMID: 33837253]. Although the *P. putida* protein is 65% identical and has a lipid-bound crystal structure (5UWB), its specific binding constants and lipid-species preferences have not been independently measured.

2. **Transport directionality not settled organism-specifically.** The retrograde (OM→IM) model is well supported in *E. coli*/*P. aeruginosa* systems, but the physiological direction (and whether it can be bidirectional/anterograde under some conditions) remains an active debate in the field [PMID: 36459067]. This has not been resolved specifically for *P. putida*.

3. **Regulatory subunit identity is inferred.** PP_0962 is annotated as a "second toluene-tolerance protein" and assigned as a candidate MlaB regulatory subunit by architectural analogy; this has not been experimentally confirmed in KT2440.

4. **Outer-membrane partner not enumerated here.** The identity of the *P. putida* MlaA–OmpC/F equivalent (the outer-membrane docking partner for Ttg2D) was not explicitly resolved in this investigation, though homologs are expected to be present.

5. **No knockout phenotype in KT2440 specifically.** The solvent-tolerance phenotype was demonstrated in *P. putida* GM73 [PMID: 9658016] and the antibiotic-resistance phenotype in *P. aeruginosa* [PMID: 33837253]; a clean KT2440 *ttg2D*-specific knockout characterization was not part of the reviewed evidence.

---

## Proposed Follow-up Experiments / Actions

1. **Native/denaturing MS on KT2440 Ttg2D.** Reproduce the *P. aeruginosa* experiment [PMID: 33837253] on periplasm-isolated PP_0961 to confirm identical stoichiometry (2 diacyl PLs / 1 cardiolipin) and promiscuity in the exact target.

2. **Directionality reconstitution in a *P. putida* system.** Build a proteoliposome assay (as in [PMID: 33199922]) with KT2440 MlaFEDB (PP_0958–0960/0962), Ttg2D, and the OM partner to measure net transport direction and ATP-dependence in this organism.

3. **Clean *ttg2D* (PP_0961) deletion in KT2440.** Quantify toluene/solvent MIC and lipophilic-antibiotic susceptibility, and assay OM permeability (e.g., NPN uptake), to directly link Ttg2D loss to barrier degradation in the target strain.

4. **Confirm PP_0962 as MlaB.** Test physical interaction with the MlaF/Ttg2A ATPase (PP_0958) and its effect on ATPase activity to validate the regulatory-subunit assignment.

5. **Structure–function of the lipid pocket.** Use the 5UWB lipid-bound structure and the 4FCZ apo structure to guide cavity-lining mutants; test binding and complementation to map determinants of promiscuous glycerophospholipid recognition and to confirm the pivoting-β-sheet gating.

6. **Map the hand-off interfaces.** Apply deep mutational scanning / computational structure prediction ([PMID: 37100290]) and the MlaC–MlaD structural framework ([PMID: 39080293]) to the *P. putida* proteins to identify the Ttg2D docking residues on Ttg2C/MlaD.

---

## Supported and Refuted Hypotheses

**Supported**
- **Identity:** ttg2D = MlaC-family periplasmic phospholipid-binding protein (domain + ortholog evidence).
- **Function:** substrate is glycerophospholipid; role is promiscuous carrier/shuttle (structure + native MS).
- **Localization:** soluble, periplasmic (cleaved Sec signal peptide; system architecture).
- **Pathway:** component of Mla retrograde transport maintaining OM lipid asymmetry.

**Refuted / excluded**
- **Not an enzyme** — no catalytic reaction; ATPase/permease activity belongs to MlaFEDB/Ttg2ABC, not to Ttg2D.
- **Not itself a toluene/drug efflux pump** — the "toluene tolerance" phenotype is an indirect consequence of OM-barrier maintenance, distinct from the *P. putida* TtgABC/TtgGHI RND efflux systems.

---

### Conclusion

*ttg2D* (PP_0961 / Q88P91) encodes the **soluble periplasmic phospholipid-shuttle protein (MlaC ortholog) of the Ttg2/Mla ABC transport system** in *Pseudomonas putida* KT2440. Its primary, non-enzymatic function is to bind glycerophospholipids promiscuously in a hydrophobic cavity and carry them across the periplasm between the inner-membrane MlaFEDB (Ttg2ABC) transporter and the outer-membrane MlaA–OmpC/F complex, driving retrograde phospholipid transport that maintains outer-membrane lipid asymmetry — the barrier function that underlies *P. putida*'s toluene tolerance and low-level intrinsic resistance to lipophilic antibiotics.

---

*Key references:* Yero et al. 2021 (PMID 33837253); Kim et al. 1998 (PMID 9658016); Hughes et al. 2019 (PMID 31235958); Tang et al. 2021 (PMID 33199922); Abellón-Ruiz 2023 review (PMID 36459067); MacRae et al. 2023 (PMID 37100290); Yeow et al. 2023 (PMID 38092770); Wotherspoon et al. 2024 (PMID 39080293); Low et al. 2021 (PMID 34873038).


## Artifacts

- [OpenScientist final report](ttg2D-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](ttg2D-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:33837253
2. PMID:9658016
3. PMID:31235958
4. PMID:37100290
5. PMID:36459067
6. PMID:38092770
7. PMID:34873038
8. PMID:39080293
9. PMID:33199922