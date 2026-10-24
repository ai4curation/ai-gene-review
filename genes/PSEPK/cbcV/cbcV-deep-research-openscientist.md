---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-13T05:30:07.267959'
end_time: '2026-08-13T06:07:41.929209'
duration_seconds: 2254.66
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: cbcV
  gene_symbol: cbcV
  uniprot_accession: Q88R40
  protein_description: 'SubName: Full=Choline / betaine / carnitine ABC transporter-ATP
    binding subunit {ECO:0000313|EMBL:AAN65925.1}; EC=3.6.3.32 {ECO:0000313|EMBL:AAN65925.1};'
  gene_info: Name=cbcV {ECO:0000313|EMBL:AAN65925.1}; OrderedLocusNames=PP_0294 {ECO:0000313|EMBL:AAN65925.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the ABC transporter superfamily.
  protein_domains: AAA+_ATPase. (IPR003593); ABC_osmolyte_uptake_ATP-bind. (IPR051921);
    ABC_transporter-like_ATP-bd. (IPR003439); ABC_transporter-like_CS. (IPR017871);
    ABC_trnsptr_Choline_ATP-bd. (IPR022473)
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
citation_count: 4
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: cbcV-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: cbcV-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88R40
- **Protein Description:** SubName: Full=Choline / betaine / carnitine ABC transporter-ATP binding subunit {ECO:0000313|EMBL:AAN65925.1}; EC=3.6.3.32 {ECO:0000313|EMBL:AAN65925.1};
- **Gene Information:** Name=cbcV {ECO:0000313|EMBL:AAN65925.1}; OrderedLocusNames=PP_0294 {ECO:0000313|EMBL:AAN65925.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the ABC transporter superfamily.
- **Key Domains:** AAA+_ATPase. (IPR003593); ABC_osmolyte_uptake_ATP-bind. (IPR051921); ABC_transporter-like_ATP-bd. (IPR003439); ABC_transporter-like_CS. (IPR017871); ABC_trnsptr_Choline_ATP-bd. (IPR022473)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "cbcV" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'cbcV' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **cbcV** (gene ID: cbcV, UniProt: Q88R40) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *cbcV* (Q88R40 / PP_0294) in *Pseudomonas putida* KT2440

**Gene:** *cbcV* · **UniProt:** Q88R40 · **Ordered locus:** PP_0294 · **Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / KT2440) · **EC:** 3.6.3.32 (quaternary-amine-transporting ATPase)

---

## Summary

**cbcV encodes the ATP-hydrolyzing (nucleotide-binding) subunit of an ATP-binding cassette (ABC) importer that scavenges quaternary-ammonium osmolytes — choline, glycine betaine and carnitine — from the environment.** In *Pseudomonas putida* KT2440 the gene is the third cistron of the chromosomal *cbcXWV* operon (PP_0296 *cbcX* → PP_0295 *cbcW* → PP_0294 *cbcV*), which encodes, respectively, a periplasmic substrate-binding protein (SBP), an integral-membrane permease, and the cytoplasmic ATPase. The two membrane-associated components, the permease CbcW and the ATPase CbcV, form the **core translocase, designated CbcWV**. CbcV is the molecular engine of this system: it binds and hydrolyzes ATP at the cytoplasmic face of the inner membrane and uses that chemical energy to power conformational cycling of the permease, driving the unidirectional accumulation of substrate delivered by the periplasmic binding protein.

The defining architectural feature of the Cbc system — established by direct biochemical characterization of the orthologous transporters from *Pseudomonas syringae* and *Pseudomonas aeruginosa* — is that the single CbcWV core translocase is served by **multiple, interchangeable, highly specific substrate-binding proteins**. CbcX binds choline (Kₘ ≈ 2.6 µM) and betaine; the same CbcWV core also partners with the carnitine-specific SBP CaiX (Kₘ ≈ 24 µM) and the betaine-specific SBP BetX (Kₘ ≈ 0.6 µM). Substrate specificity is therefore dictated by the swappable binding protein, **not by CbcV**, whose role is the generic, substrate-nonspecific energization of transport. Because it is an ATP-driven, SBP-dependent importer, the Cbc system achieves **high-affinity (micromolar) scavenging**, mechanistically distinct from the low-affinity, ion-gradient-driven BCCT-family secondary carriers (such as BetT) that transport the same compounds.

Physiologically, the imported compounds feed two connected purposes in *P. putida*: **osmoprotection** and **catabolism**. Choline is oxidized to glycine betaine by the BetBA enzymes; glycine betaine is a highly effective compatible solute that confers salt tolerance, and the same compounds can be used as carbon or nitrogen sources. The functional assignment of KT2440 CbcV rests on a strong convergence of evidence — an intact, canonical ABC-ATPase catalytic domain (all Walker A/B and LSGGQ signature motifs present), conserved *XWV* operon synteny, GO/InterPro annotations, and close orthology to the experimentally validated Cbc and ChoXWV systems — while acknowledging that the enzymology of the KT2440 protein itself has not been separately reported.

---

## Gene / Protein Identity Verification

Before presenting findings, the target identity was verified against the UniProt record and the primary literature. **The gene symbol *cbcV*, the organism (*P. putida* KT2440), the EC number (3.6.3.32), and the InterPro domain complement all align internally and with the characterized Cbc/ChoXWV literature.** There is no evidence of a symbol clash with an unrelated, better-studied gene; "cbc" consistently denotes the **c**holine/**b**etaine/**c**arnitine transporter across *Pseudomonas*. The report therefore proceeds with confidence in the target assignment.

| Attribute | Value | Source |
|---|---|---|
| Protein length | 392 aa | UniProt Q88R40 |
| EC number | 3.6.3.32 (quaternary-amine-transporting ATPase) | UniProt / EMBL AAN65925.1 |
| Superfamily | ABC transporter superfamily | UniProt |
| Diagnostic domain | IPR022473 "ABC transporter Choline ATP-binding" | InterPro |
| Other domains | IPR003593 (AAA+ ATPase), IPR003439 & IPR017871 (ABC ATP-binding / signature) | InterPro |
| Operon | *cbcXWV*: PP_0296 (SBP) – PP_0295 (permease) – PP_0294 (ATPase) | UniProt REST genomic mapping |
| GO (molecular function) | ATP binding (GO:0005524); ATP hydrolysis activity (GO:0016887); choline transmembrane transporter activity (GO:0015220) | UniProt |
| GO (cellular component) | ABC transporter complex (GO:0055052) | UniProt |
| GO (biological process) | response to osmotic stress (GO:0006970) | UniProt |

---

## Key Findings

### F001 — cbcV is the ATP-hydrolyzing subunit of the CbcWV core ABC importer for quaternary-ammonium osmolytes

The UniProt record for Q88R40 describes a 392-amino-acid protein carrying EC 3.6.3.32 (quaternary-amine-transporting ATPase) and assigns it to the ABC transporter superfamily, with the diagnostic InterPro domain IPR022473, "ABC transporter Choline ATP-binding." Its Gene Ontology annotations — ATP binding (GO:0005524), ATP hydrolysis activity (GO:0016887), choline transmembrane transporter activity (GO:0015220), ABC transporter complex (GO:0055052), and response to osmotic stress (GO:0006970) — together paint an unambiguous picture of a nucleotide-binding component of a membrane transport complex dedicated to osmolyte uptake.

Genomic mapping via the UniProt REST interface confirms that *cbcV* is embedded in the *cbcXWV* operon of *P. putida* KT2440, with PP_0296 (*cbcX*, the substrate-binding protein), PP_0295 (*cbcW*, the membrane permease) and PP_0294 (*cbcV*, the ATPase) arranged in the canonical order for a Type-I ABC importer. In the experimentally characterized orthologous system, the two membrane-associated subunits — permease plus ATPase — constitute the **core transporter, designated CbcWV**. The characterization of the *Pseudomonas* Cbc system directly established this core as the functional membrane module:

> *"The core transporter CbcWV also interacts with the carnitine-specific SBP CaiX (Kₘ, 24 µM) and the betaine-specific SBP BetX (Kₘ, 0.6 µM)."* — [PMID: 19919675](https://pubmed.ncbi.nlm.nih.gov/19919675/)

CbcV is the ATPase half of this CbcWV core. Functionally, it is the subunit that converts the chemical energy of ATP hydrolysis into the mechanical work of substrate translocation.

### F002 — The Cbc transporter uses interchangeable, highly specific periplasmic SBPs to import choline, betaine and carnitine

The single most distinctive property of the Cbc system — and the property that gives the transporter its name — was defined by Chen, Chen & Beattie (2010) working with the orthologues from *P. syringae* and *P. aeruginosa*. They found that a single core translocase recruits several different periplasmic binding proteins, each exquisitely specific for one substrate:

> *"we identified a choline, betaine and carnitine transporter, designated Cbc, from Pseudomonas syringae and Pseudomonas aeruginosa that is unusual among members of the ATP-binding cassette (ABC) transporter family in its use of multiple periplasmic substrate-binding proteins (SBPs) that are highly specific for their substrates"* — [PMID: 19919675](https://pubmed.ncbi.nlm.nih.gov/19919675/)

> *"The SBP encoded by the cbcXWV operon, CbcX, binds choline with a high affinity (Kₘ, 2.6 µM)."* — [PMID: 19919675](https://pubmed.ncbi.nlm.nih.gov/19919675/)

The operon-encoded SBP CbcX binds choline with high affinity (Kₘ ≈ 2.6 µM) and also binds glycine betaine (Kₘ ≈ 24.2 µM). Separately encoded "orphan" SBPs — CaiX (carnitine-specific, Kₘ ≈ 24 µM) and BetX (betaine-specific, Kₘ ≈ 0.6 µM) — are located elsewhere in the genome but plug into the same CbcWV core. This modular design means that **substrate specificity is a property of the binding protein, while CbcWV (including the ATPase CbcV) provides substrate-agnostic translocation and energization**. For CbcV specifically, this implies that the ATPase does not itself recognize choline, betaine, or carnitine; it responds to the docking of a liganded SBP onto the permease by hydrolyzing ATP to drive the transport cycle.

The following table summarizes the SBP–substrate affinities that funnel into the CbcWV core:

| Substrate-binding protein | Substrate(s) | Affinity (Kₘ) | Genomic location |
|---|---|---|---|
| CbcX | Choline (also betaine) | 2.6 µM (choline); 24.2 µM (betaine) | *cbcXWV* operon |
| CaiX | Carnitine | 24 µM | orphan, separate locus |
| BetX | Glycine betaine | 0.6 µM | orphan, separate locus |

### F003 — Physiological role: choline/betaine uptake feeds osmoprotection and catabolism in *P. putida* KT2440

The downstream fate of the imported substrates anchors the biological purpose of CbcV-powered transport. In *P. putida* KT2440, Galvão and colleagues showed that once choline is inside the cell it is converted to glycine betaine by the BetBA enzymes, and that this conversion underlies both salt endurance and nutrient utilization:

> *"the betBA genes were required for choline transformation into the highly effective compatible solute glycine betaine (and the concomitant endurance to high salt) and also for its utilization as carbon or nitrogen source"* — [PMID: 17116241](https://pubmed.ncbi.nlm.nih.gov/17116241/)

Glycine betaine is one of the most effective compatible solutes known: it accumulates to high cytoplasmic concentrations without perturbing macromolecular function, counterbalancing external osmotic pressure. The *cbcV* GO annotation "response to osmotic stress" (GO:0006970) is consistent with this role. Because the same compounds can also be catabolized as carbon or nitrogen sources, the Cbc importer sits at the head of a pathway that is simultaneously a **stress-defense** and a **nutrient-acquisition** system.

The conserved architecture of the transporter across taxa reinforces the subunit assignment. In the plant symbiont *Agrobacterium tumefaciens*, Aktas and colleagues described the orthologous high-affinity choline importer with exactly the same three-gene layout:

> *"The ABC-type choline transporter is encoded by the chromosomally located choXWV operon (ChoX, binding protein; ChoW, permease; and ChoV, ATPase)."* — [PMID: 21803998](https://pubmed.ncbi.nlm.nih.gov/21803998/)

The "V" gene in this *XWV* nomenclature invariably encodes the ATPase — confirming, by conserved synteny and naming, that *cbcV* (the "V" cistron of *cbcXWV*) is the ATPase subunit.

### F004 — Q88R40 contains a complete, canonical Type-I ABC-importer nucleotide-binding domain

A motif scan of the 392-residue Q88R40 sequence (UniProt FASTA) identified the full catalytic complement expected of a functional ABC ATPase, confirming that CbcV is not a degenerate or pseudo-ATPase but a bona fide, catalytically competent nucleotide-binding domain (NBD):

| Motif | Sequence found | Approx. residues | Function |
|---|---|---|---|
| Walker A / P-loop | `GLSGSGKS` | 60–67 | Binds β/γ phosphates of ATP |
| ABC signature (C-loop / LSGGQ) | `LSGGMQQR` | ~167 | Diagnostic ABC motif; couples ATP binding to transport |
| Walker B | `ILLMDE` | 188–193 | Catalytic Asp/Glu; coordinates Mg²⁺ and activates water for hydrolysis |
| D-loop | `SALD` | downstream of Walker B | Inter-subunit communication in the NBD dimer |
| Switch His | conserved His | downstream | γ-phosphate sensor |

The simultaneous presence of the Walker A P-loop, the Walker B catalytic residues, and — most diagnostically — the **LSGGQ ABC signature** confirms an intact ATP-binding and hydrolysis machine. This is precisely the enzymatic apparatus required to satisfy the EC 3.6.3.32 assignment and matches InterPro AAA+ ATPase (IPR003593) and the ABC ATP-binding domains (IPR003439, IPR022473). The completeness of the motif set is strong structural evidence — independent of any wet-lab enzymology on KT2440 CbcV — that this protein binds and hydrolyzes ATP as the energizing subunit of the transporter.

### F005 — CbcV's ABC system is mechanistically distinct from the BCCT secondary transporter BetT

*Pseudomonas* species possess a second, mechanistically unrelated route for importing the same quaternary-amine compounds: secondary carriers of the betaine/carnitine/choline transporter (BCCT) family, energized by ion gradients rather than ATP. Chen and Beattie characterized one such carrier, BetT, in *P. syringae*:

> *"we identified a betaine/carnitine/choline family transporter (BCCT) in P. syringae pv. tomato strain DC3000 that mediates the transport of choline and acetylcholine. This transporter has a particularly low affinity (Kₘ of 876 µM) and high capacity"* — [PMID: 18156257](https://pubmed.ncbi.nlm.nih.gov/18156257/)

The contrast is informative for understanding what CbcV contributes. BCCT carriers like BetT are **low-affinity (Kₘ ~876 µM), high-capacity, ion-gradient-driven** single-polypeptide transporters. The Cbc ABC system, by contrast, is **high-affinity (micromolar Kₘ), ATP-driven, and multi-subunit**, achieving its affinity through periplasmic SBPs (CbcX choline Kₘ 2.6 µM; BetX betaine Kₘ 0.6 µM; CaiX carnitine Kₘ 24 µM). CbcV is the component that makes the ATP-driven route possible: without ATP hydrolysis by CbcV, the high-affinity SBP-dependent mechanism cannot function. The two systems thus provide the cell with complementary strategies — high-affinity scavenging when substrate is scarce (Cbc/CbcV) versus bulk uptake when substrate is abundant (BetT/BCCT). Notably, *P. putida* encodes six putative BCCT-family transporters in addition to its ABC importers, underscoring the metabolic importance of quaternary-amine acquisition in this organism.

---

## Mechanistic Model / Interpretation

The findings integrate into a single coherent mechanistic picture of a **Type-I ABC importer** in which CbcV is the cytoplasmic power unit.

```
        PERIPLASM
   choline / betaine / carnitine
            │
            ▼
     ┌──────────────┐   Interchangeable, substrate-specific SBPs:
     │  SBP (CbcX /  │     CbcX  → choline (Km 2.6 µM), betaine (24 µM)
     │  CaiX / BetX) │     CaiX  → carnitine (Km 24 µM)
     └──────┬───────┘     BetX  → betaine (Km 0.6 µM)
            │ docks liganded onto permease
════════════▼════════════════════════  INNER MEMBRANE
     ┌──────────────┐
     │ CbcW permease│  (PP_0295)  transmembrane translocation pathway
     └──────┬───────┘
            │ conformational coupling
     ┌──────▼───────┐
     │ CbcV ATPase  │  (PP_0294)  ← THIS PROTEIN, Q88R40
     │  NBD dimer   │  Walker A/B + LSGGQ signature
     └──────────────┘
            │
        ATP → ADP + Pi   (EC 3.6.3.32)
        CYTOPLASM
            │
            ▼  choline ──BetBA──► glycine betaine
                                    ├─► compatible solute (osmoprotection)
                                    └─► C / N source (catabolism)
```

**Transport cycle.** A periplasmic SBP captures its specific substrate with micromolar-to-submicromolar affinity and, in the liganded closed conformation, docks onto the periplasmic face of the CbcW permease. This docking signals across the membrane to the two CbcV NBDs, which are appended to the cytoplasmic face of the permease. ATP binding drives dimerization of the two CbcV NBDs (sandwiching two ATP molecules between the Walker A/B motifs of one protomer and the LSGGQ signature of the other), which reorients the permease to an outward-facing state that accepts the substrate. ATP hydrolysis by CbcV — using the Walker B catalytic Asp/Glu to activate a water molecule — and subsequent Pi/ADP release reset the transporter to the inward-facing state, releasing substrate into the cytoplasm. **CbcV thus performs the energy-transduction step that renders transport unidirectional and concentrative.**

**Division of labor.** The modular Cbc design cleanly separates the three logical functions of an importer: *recognition* (the SBP), *translocation* (the CbcW permease), and *energization* (the CbcV ATPase). Because a single CbcWV core is shared among multiple SBPs, the cell economizes by encoding one translocase/energizer pair while diversifying only the recognition module. This is why CbcV itself is substrate-nonspecific — it is a generic ATP engine, and the "choline/betaine/carnitine" specificity attributed to the operon derives from the binding proteins, not from CbcV.

**Localization.** Consistent with GO:0055052 (ABC transporter complex), CbcV is a **peripheral membrane protein on the cytoplasmic face of the inner membrane**, anchored through its association with the CbcW permease. It carries out ATP hydrolysis in the cytoplasm, at the membrane interface — it is not itself a transmembrane protein, nor is it periplasmic.

**Physiological logic.** The system is deployed when *P. putida* faces osmotic stress or when environmental quaternary amines are available as nutrients. Imported choline is funneled through BetBA to glycine betaine, delivering an osmoprotectant and, alternatively, carbon and nitrogen. The high-affinity ABC route (CbcV-powered) complements the low-affinity BCCT route (BetT), giving the cell coverage across a wide range of external substrate concentrations.

---

## Evidence Base

| PMID | Title (abbreviated) | How it supports the findings |
|---|---|---|
| [19919675](https://pubmed.ncbi.nlm.nih.gov/19919675/) | *The ABC transporter Cbc recruits multiple substrate-binding proteins…* | **Primary, foundational.** Defines the Cbc system in *P. syringae*/*P. aeruginosa*; names the *cbcXWV* operon; establishes CbcWV as the core translocase; quantifies SBP affinities (CbcX choline 2.6 µM; CaiX carnitine 24 µM; BetX betaine 0.6 µM). Direct basis for F001 and F002. |
| [17116241](https://pubmed.ncbi.nlm.nih.gov/17116241/) | *Uncoupling of choline-O-sulphate utilization from osmoprotection in P. putida* | **Physiology in the exact target organism (KT2440).** Shows imported choline → glycine betaine via BetBA, required for salt endurance and for use as C/N source. Basis for F003. |
| [21803998](https://pubmed.ncbi.nlm.nih.gov/21803998/) | *Choline uptake in A. tumefaciens by the high-affinity ChoXWV transporter* | **Orthologous system.** Confirms the conserved *XWV* operon architecture (X = SBP, W = permease, V = ATPase), directly validating cbcV's subunit assignment as the ATPase. Basis for F003. |
| [18156257](https://pubmed.ncbi.nlm.nih.gov/18156257/) | *P. syringae BetT is a low-affinity choline transporter…* | **Mechanistic contrast.** Characterizes the alternative BCCT secondary carrier (Kₘ ~876 µM), distinguishing the low-affinity ion-driven route from the high-affinity ATP-driven Cbc route. Basis for F005. |
| [17660277](https://pubmed.ncbi.nlm.nih.gov/17660277/) | *Characterization of OpuC from P. syringae; CBS domains required…* | Context: another *Pseudomonas* osmoprotectant ABC transporter (OpuC) with broad specificity; illustrates the landscape of quaternary-amine ABC importers and the role of ATPase-associated regulatory (CBS) domains. |
| [18779321](https://pubmed.ncbi.nlm.nih.gov/18779321/) | *Crystal structures of ChoX from S. meliloti…* | Structural insight into the SBP partner (ChoX) of the orthologous ChoVWX system, illuminating substrate recognition upstream of the ATPase. |
| [39141726](https://pubmed.ncbi.nlm.nih.gov/39141726/) | *Structure and mechanism of the osmoregulated choline transporter BetT* | Cryo-EM mechanism of the BCCT-family choline transporter, complementing the mechanistic contrast in F005. |
| [40762496](https://pubmed.ncbi.nlm.nih.gov/40762496/) | *Root exudates protect rhizosphere…* | Ecological context for quaternary-amine osmolyte acquisition in plant-associated pseudomonads. |

**Strength of evidence for cbcV specifically.** The functional assignment rests on **inference from strong orthology plus intrinsic sequence/structural evidence**, not on direct enzymology of the KT2440 protein. This inference is well supported: (1) the biochemically characterized Cbc system (PMID 19919675) is a close *Pseudomonas* orthologue; (2) the *cbcXWV* operon synteny in KT2440 is identical to characterized systems; (3) the ChoXWV nomenclature (PMID 21803998) independently confirms the "V = ATPase" assignment; and (4) the intact ABC-ATPase motif complement (F004) confirms catalytic competence at the protein level. Together these constitute a high-confidence annotation.

---

## Limitations and Knowledge Gaps

1. **No direct enzymology on KT2440 CbcV.** The ATPase activity, kinetic parameters (kcat, Kₘ for ATP), and the coupling stoichiometry of the *P. putida* KT2440 protein itself have not been measured. The functional claims are transferred from orthologues and from sequence analysis.

2. **Substrate specificity is inferred, not demonstrated in KT2440.** The choline/betaine/carnitine substrate range is established for the *P. syringae*/*P. aeruginosa* Cbc systems. Whether the KT2440 *cbcXWV* operon-encoded CbcX, and any orphan CaiX/BetX orthologues, reproduce the same specificities in KT2440 has not been experimentally confirmed here.

3. **No structural model of the KT2440 complex.** There is no experimental structure of CbcWV; the transport-cycle model is a canonical Type-I ABC-importer scheme applied by homology. An AlphaFold or cryo-EM structure of the CbcWV core would refine the mechanistic picture.

4. **Regulation is uncharacterized.** How *cbcXWV* expression responds to osmotic stress, substrate availability, or nitrogen/carbon status in KT2440 (transcriptional regulators, induction conditions) was not investigated.

5. **Orphan SBP inventory in KT2440.** The genomic identities of any KT2440 CaiX/BetX orthologues that partner with CbcWV were not enumerated, so the full substrate repertoire available to the KT2440 core translocase remains to be mapped.

---

## Proposed Follow-up Experiments / Actions

1. **Direct ATPase assay.** Purify recombinant KT2440 CbcV (PP_0294) and reconstitute the CbcWV core in nanodiscs or proteoliposomes; measure basal and SBP/substrate-stimulated ATP hydrolysis to confirm EC 3.6.3.32 activity and obtain kinetic constants.

2. **Transport assays with labeled substrates.** Use radiolabeled or fluorescent choline/betaine/carnitine in whole-cell or proteoliposome uptake assays with a *cbcV* deletion and complementation to demonstrate ATP-dependence and quantify affinity/capacity in KT2440.

3. **Catalytic-mutant validation.** Introduce a Walker B mutation (e.g., the catalytic Glu/Asp in `ILLMDE`, residues 188–193) to create an ATP-binding-but-hydrolysis-dead variant; confirm loss of transport, formally linking CbcV ATP hydrolysis to substrate uptake.

4. **SBP-swap experiments in KT2440.** Identify and clone KT2440 orthologues of CaiX and BetX; test whether they functionally couple to CbcWV, directly validating the interchangeable-SBP model in the target organism.

5. **Structural determination.** Solve a cryo-EM structure of the CbcWV core (± SBP, ± ATP analog) or generate a validated AlphaFold-Multimer model to visualize the NBD dimer interface and the transmembrane coupling helices.

6. **Regulation and phenotype.** Perform RNA-seq/qPCR of *cbcXWV* under osmotic upshift and with choline/betaine/carnitine as sole C/N source, and phenotype a *cbcV* mutant for salt tolerance and growth on these substrates, to define the physiological conditions under which CbcV operates.

---

## Conclusion

*cbcV* (Q88R40 / PP_0294) encodes the **ATP-hydrolyzing (ATPase) subunit of the CbcWV core ABC importer** in *Pseudomonas putida* KT2440. It is the third gene of the *cbcXWV* operon (PP_0296 SBP → PP_0295 permease → PP_0294 ATPase), acts as a **peripheral membrane protein on the cytoplasmic face of the inner membrane**, and binds and hydrolyzes ATP (EC 3.6.3.32; complete Walker A/B and LSGGQ signature motifs present) to energize high-affinity import of the quaternary-ammonium osmolytes **choline, glycine betaine and carnitine**. Substrate specificity is dictated by interchangeable periplasmic binding proteins (CbcX/CaiX/BetX), not by CbcV itself. The imported compounds serve in **osmoprotection** (glycine betaine as a compatible solute, produced from choline by BetBA) and as **carbon/nitrogen nutrients**. The assignment is grounded in strong orthology to the experimentally characterized Cbc/ChoXWV systems, conserved operon synteny, GO/InterPro annotation, and an intact ABC-ATPase catalytic domain, while direct enzymology on the KT2440 protein remains an open experimental target.


## Artifacts

- [OpenScientist final report](cbcV-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](cbcV-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:19919675
2. PMID:17116241
3. PMID:21803998
4. PMID:18156257