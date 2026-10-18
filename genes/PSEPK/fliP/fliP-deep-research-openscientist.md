---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T16:50:57.255741'
end_time: '2026-08-31T17:08:14.021081'
duration_seconds: 1036.77
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: fliP
  gene_symbol: fliP
  uniprot_accession: Q88EU8
  protein_description: 'RecName: Full=Flagellar biosynthetic protein FliP {ECO:0000256|ARBA:ARBA00021714,
    ECO:0000256|RuleBase:RU362069};'
  gene_info: Name=fliP {ECO:0000256|RuleBase:RU362069, ECO:0000313|EMBL:AAN69933.1};
    OrderedLocusNames=PP_4355 {ECO:0000313|EMBL:AAN69933.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the FliP/MopC/SpaP family.
  protein_domains: FliP. (IPR005837); T3SS_IM_P. (IPR005838); FliP (PF00813)
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
citation_count: 14
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: fliP-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: fliP-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88EU8
- **Protein Description:** RecName: Full=Flagellar biosynthetic protein FliP {ECO:0000256|ARBA:ARBA00021714, ECO:0000256|RuleBase:RU362069};
- **Gene Information:** Name=fliP {ECO:0000256|RuleBase:RU362069, ECO:0000313|EMBL:AAN69933.1}; OrderedLocusNames=PP_4355 {ECO:0000313|EMBL:AAN69933.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the FliP/MopC/SpaP family.
- **Key Domains:** FliP. (IPR005837); T3SS_IM_P. (IPR005838); FliP (PF00813)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "fliP" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'fliP' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **fliP** (gene ID: fliP, UniProt: Q88EU8) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of FliP (Q88EU8, PP_4355) — Flagellar Type III Secretion Export Gate Core Subunit in *Pseudomonas putida* KT2440

## Summary

**FliP (UniProt Q88EU8; ordered locus PP_4355) is an essential integral inner-membrane structural subunit of the bacterial flagellar type III secretion system (fT3SS) export apparatus.** It is neither an enzyme nor a solute transporter. Its primary molecular function is to oligomerize into a channel-forming core that constitutes the protein-conducting conduit of the flagellar export gate. Through this conduit, unfolded flagellar axial subunits (rod, hook, and filament proteins) are translocated from the cytoplasm across the inner membrane and delivered to the distal tip of the growing flagellum, where they polymerize. In *P. putida* KT2440 this role is assigned by strong orthology: the protein belongs to the FliP/MopC/SpaP family (InterPro IPR005837/IPR005838; Pfam PF00813), and its bacterial homologs in *Salmonella* and other model organisms have been characterized in detail through genetics, biochemistry, and high-resolution cryo-electron microscopy.

The definitive structural picture comes from a 4.2 Å cryo-EM structure of the *Salmonella* Typhimurium FliP–FliQ–FliR complex, which revealed that FliP assembles as **five copies** in a helical export-gate core with a **5:4:1 FliP:FliQ:FliR stoichiometry**. Remarkably, none of the three subunits adopts a canonical integral-membrane topology; instead, shared helix-turn-helix elements pack into a helical assembly that forms the periplasmic core of the secretion channel and templates the helical architecture of downstream rod and hook/needle components. Chemical-modification and channel-conductance experiments independently established that the protein-conducting conduit is formed "primarily, and possibly entirely, by FliP," with a methionine-rich loop at the inner mouth that may form a gasket around exported cargo.

FliP localizes to the cytoplasmic membrane at the core of the basal-body MS ring, and it is one of five essential membrane proteins (FlhA, FlhB, FliP, FliQ, FliR) of the export apparatus. It has an unusual biogenesis for a cytoplasmic-membrane protein — a cleavable N-terminal signal peptide, four predicted transmembrane helices, and a periplasmic domain (FliP_P) between TM-2 and TM-3. The gate it helps form is energized by the proton-motive force and acts as a proton–protein antiporter. The system is evolutionarily conserved with the virulence-associated injectisome, in which FliP corresponds to SctR. This report synthesizes six confirmed findings drawn from 19 reviewed papers to describe FliP's function, localization, and pathway context.

### Identity verification

The gene symbol *fliP*, the "flagellar biosynthetic protein" description, and the FliP/PF00813 domain architecture are mutually consistent and unambiguous. FliP is a deeply conserved core component of the flagellar T3SS. Direct experimental studies exist for orthologs in *Salmonella enterica*, *Escherichia coli*, and *Bacillus subtilis*; the *P. putida* KT2440 protein Q88EU8 (PP_4355) is a clear ortholog (family PF00813), so its function is assigned by strong, high-confidence orthology. No literature ambiguity or wrong-gene conflict was found.

---

## Key Findings

### F001 — FliP is an essential membrane component of the flagellar T3SS export apparatus

FliP is one of five essential membrane-embedded proteins — FlhA, FlhB, FliP, FliQ, and FliR — that together form the transmembrane core of the flagellar type III export apparatus. This apparatus is the machine that exports the structural subunits of the flagellum during its assembly. In a study of the export machinery, the membrane-embedded part of the apparatus was defined as containing exactly these five essential proteins ([PMID: 29076571](https://pubmed.ncbi.nlm.nih.gov/29076571/)): *"The membrane-embedded part of the flagellar export apparatus contains five essential proteins: FlhA, FlhB, FliP, FliQ and FliR."*

The genetic essentiality of *fliP* was established early in *Salmonella typhimurium*, where *fliO*, *fliP*, *fliQ*, and *fliR* were characterized as putative components required for flagellar assembly. These genes are needed for flagellation but do not themselves encode recognizable structural components of the finished flagellum or obvious regulators; rather, they act in the export process itself ([PMID: 9324257](https://pubmed.ncbi.nlm.nih.gov/9324257/)): *"They are needed for flagellation but do not encode any known structural or regulatory components. They may be involved in flagellar protein export, which proceeds by a type III export pathway."*

Because the *P. putida* KT2440 protein Q88EU8 / PP_4355 is a member of the FliP/MopC/SpaP family (Pfam PF00813; InterPro IPR005837 "FliP" and IPR005838 "T3SS inner-membrane protein P"), this essential export role is assigned to it by strong orthology to the well-characterized *Salmonella* and *E. coli* FliP proteins. *P. putida* KT2440 is a motile soil bacterium that assembles a polar flagellum for swimming motility, and FliP is a required core component of the export machine that builds that flagellum.

### F002 — FliP forms the protein-conducting channel/pore of the export gate

Beyond being essential, FliP is the primary channel-forming subunit — the protein whose oligomer creates the conduit through which exported flagellar subunits pass. Multiple orthogonal biophysical approaches converge on this conclusion. Chemical-modification assays, chemical-sensitivity assays, and direct channel-conductance measurements support the view that the protein-conducting conduit is built primarily, and possibly entirely, by FliP ([PMID: 29076571](https://pubmed.ncbi.nlm.nih.gov/29076571/)): *"the protein-conducting conduit is formed primarily, and possibly entirely, by FliP."*

The same work identified a functional feature of the channel: a **methionine-rich loop** predicted to lie at the inner mouth of the pore that strongly modulates its conductance and may form a flexible gasket around cargo molecules as they thread through during export ([PMID: 29076571](https://pubmed.ncbi.nlm.nih.gov/29076571/)): *"Conductance properties are strongly modulated by mutations in a methionine-rich loop that is predicted to lie at the inner mouth of the channel, which might form a gasket around cargo molecules undergoing export."* This "gasket" concept is mechanistically appealing because it would allow the channel to accommodate and seal against unfolded polypeptides of varying sequence while maintaining the membrane permeability barrier.

Consistent with FliP nucleating the gate, FliP self-assembles into a ring that initiates assembly of the entire export-gate core complex ([PMID: 28771466](https://pubmed.ncbi.nlm.nih.gov/28771466/)). FliP is therefore both the seed of gate assembly and the material that lines the export pore.

### F003 — Membrane topology and localization: cleavable signal peptide, four TM helices, periplasmic domain, within the MS ring

FliP is a hydrophobic integral cytoplasmic-membrane protein. Topology prediction and structural analysis of the periplasmic domain established that FliP carries an N-terminal signal peptide, has four transmembrane (TM) helices, and possesses a periplasmic domain (FliP_P) located between TM-2 and TM-3 ([PMID: 25195894](https://pubmed.ncbi.nlm.nih.gov/25195894/)): *"FliP has an N-terminal signal peptide and is predicted to have four transmembrane (TM) helices and a periplasmic domain (FliPP) between TM-2 and TM-3."*

An unusual and diagnostic property of FliP is that it undergoes signal-peptide cleavage — a rare event for prokaryotic cytoplasmic-membrane proteins. Experimentally, FliP exists as two forms: an uncleaved 25-kDa form and a cleaved 23-kDa form. N-terminal sequencing of the 23-kDa form confirmed removal of a signal peptide, and mutation of the cleavage site impairs both processing and function ([PMID: 9324257](https://pubmed.ncbi.nlm.nih.gov/9324257/)): *"N-terminal amino acid analysis of the 23-kDa form demonstrated that it had undergone cleavage of a signal peptide—a rare process for prokaryotic cytoplasmic membrane proteins."*

Spatially, the FliP-containing gate complex (FlhA, FlhB, FliP, FliQ, FliR) assembles inside the basal-body MS ring, and this assembly begins with formation of the FliP ring ([PMID: 28771466](https://pubmed.ncbi.nlm.nih.gov/28771466/)): *"FlhA, FlhB, FliP, FliQ, and FliR form the gate complex inside the basal body MS ring."* Thus FliP does its work at a precise subcellular location — embedded in the cytoplasmic membrane at the center of the MS ring, at the base of the flagellar basal body, with its channel oriented to receive cytoplasmic cargo and deliver it toward the periplasmic/extracellular assembly channel.

### F004 — The export gate is energized by proton-motive force and drives directional export to the flagellar tip

The FliP-containing export apparatus is a powered, directional machine. It exports flagellar proteins from the cytoplasm to the distal end of the nascent flagellar structure, using both ATP and the proton-motive force (PMF) across the cytoplasmic membrane as energy sources ([PMID: 24064315](https://pubmed.ncbi.nlm.nih.gov/24064315/)): *"the flagellar type III export apparatus utilizes both ATP and proton motive force across the cytoplasmic membrane and exports flagellar proteins from the cytoplasm to the distal end of the nascent structure."*

The central energy-coupling insight is that the export gate itself operates as a proton–protein antiporter — coupling the inward flow of protons down the PMF to the outward translocation of protein substrate ([PMID: 24064315](https://pubmed.ncbi.nlm.nih.gov/24064315/)): *"The export gate by itself is a proton-protein antiporter."* FliP, as a core structural element of that gate, is part of the machinery that converts electrochemical energy into vectorial protein transport. The directionality — cytoplasm to distal tip — ensures that thousands of subunits are delivered to and polymerize at the growing end of the rod, hook, and filament. Substrate delivery and unfolding are assisted by the cytoplasmic FliH–FliI–FliJ ATPase complex.

### F005 — Evolutionary conservation with the injectisome subunit SctR defines a shared secretion-conduit architecture

The flagellar T3SS and the virulence-associated injectisome T3SS are evolutionarily related nanomachines that share several homologous components. This homology was recognized early: the two structures share several proteins with highly homologous amino acid sequences ([PMID: 11520608](https://pubmed.ncbi.nlm.nih.gov/11520608/)): *"The two structures share several proteins with highly homologous amino acid sequences."*

In the injectisome, the secretion conduit is formed by a helical assembly of three hydrophobic proteins — SctR, SctS, and SctT ([PMID: 31183905](https://pubmed.ncbi.nlm.nih.gov/31183905/)): *"The secretion conduit of injectisomes is formed by a helical assembly of three hydrophobic proteins (SctR, SctS and SctT)."* These three proteins are the direct homologs of flagellar **FliP, FliQ, and FliR**, respectively. This means the channel-forming role of FliP is conserved across both branches of the T3SS superfamily, and structural or mechanistic insights from one system transfer to the other. The assembly of this helical core is driven in part by conserved charged residues and salt bridges buried within the otherwise hydrophobic transmembrane domains ([PMID: 34303721](https://pubmed.ncbi.nlm.nih.gov/34303721/)), highlighting a shared and evolutionarily constrained assembly mechanism.

### F006 — Cryo-EM structure: a 5:4:1 FliP–FliQ–FliR helical core with non-canonical topology

The most definitive structural characterization of FliP's role comes from a 4.2 Å cryo-EM structure of the *Salmonella* Typhimurium FliP–FliQ–FliR complex. The three proteins assemble into a helical complex with a precise stoichiometry of **5 FliP : 4 FliQ : 1 FliR**, using shared helix-turn-helix structural elements ([PMID: 29967543](https://pubmed.ncbi.nlm.nih.gov/29967543/)): *"common helix-turn-helix structural elements allow them to form a helical assembly with 5:4:1 stoichiometry."* FliP is therefore the major, most abundant subunit of the export-gate core. This structure revised an earlier model that had proposed a FliP hexamer; the essential conclusion — that FliP oligomerizes to line the conduit — is robust across both.

A key and initially surprising structural result is that none of the three subunits adopts a canonical integral-membrane protein topology ([PMID: 29967543](https://pubmed.ncbi.nlm.nih.gov/29967543/)): *"None of the subunits adopt canonical integral membrane protein topologies."* Rather than spanning the membrane as simple bundles of parallel TM helices, the subunits form a compact helical assembly whose bulk sits above the plane of the inner membrane. Fitting the atomic structure into cryo-EM reconstructions of intact secretion systems, combined with cross-linking, localized this export gate as a core component of the **periplasmic** portion of the machinery ([PMID: 29967543](https://pubmed.ncbi.nlm.nih.gov/29967543/)): *"Fitting of the structure into reconstructions of intact secretion systems, combined with cross-linking, localize the export gate as a core component of the periplasmic portion of the machinery."* The FliP–FliQ–FliR core is the key element of the secretion channel and primes the helical architecture of downstream components (the inner rod and, in the injectisome, the needle). The structure is deposited in the Protein Data Bank as **PDB 6F2D** (the accession was corrected from 6F2E in [PMID: 30018321](https://pubmed.ncbi.nlm.nih.gov/30018321/)).

---

## Mechanistic Model / Interpretation

FliP is best understood as the **channel-forming heart of the flagellar export gate**. The following model integrates the six findings.

### Assembly hierarchy and stoichiometry

```
   Flagellar basal body assembly (inside-out)
   ─────────────────────────────────────────────
   1.  FliF assembles the MS ring in the inner membrane
   2.  FliP self-assembles into a ring  ← nucleates the gate (F002, F003)
   3.  FliP(5) + FliQ(4) + FliR(1) form the helical
       export-gate CORE  (5:4:1)        ← cryo-EM (F006)
   4.  FlhB and FlhA join to complete the transmembrane
       export apparatus (5 essential proteins)  (F001)
   5.  Rod → hook → filament subunits exported through the
       FliP conduit to the distal tip  (F002, F004)
```

### Architecture of the export gate

```
        DISTAL TIP  (growing flagellum: rod → hook → filament)
                     ▲   unfolded axial subunits polymerize here
                     │
   ══════════════════│══════════════  Outer membrane / periplasm
                     │
     ┌───────────────┴───────────────┐
     │  FliP₅ – FliQ₄ – FliR₁ core   │  ← periplasmic-facing helical
     │  (helical, non-canonical fold)│     conduit; Met-rich gasket
     │  protein-conducting CHANNEL   │     at inner mouth
     └───────────────┬───────────────┘
   ══════════════════│══════════════  Inner (cytoplasmic) membrane
       within the    │   FlhA / FlhB ring around the core
       MS ring       │   ← PMF-driven proton–protein antiporter
                     ▲
        CYTOPLASM  (unfolded axial subunits + chaperones,
                    delivered by FliI ATPase / FliJ / FliH)
```

### Functional narrative

1. **Substrate:** FliP is not a solute transporter; its "substrate" is the set of **unfolded flagellar axial proteins** — rod (FlgB/C/F/G), hook (FlgE), hook-associated, and filament (FliC/flagellin) subunits, plus regulators such as the anti-sigma factor FlgM. These are threaded through the FliP conduit as extended polypeptides.

2. **Reaction / mechanism:** The FliP-containing gate does not catalyze a chemical reaction. It performs **vectorial protein translocation** across the inner membrane. Energy comes principally from the proton-motive force, with the gate acting as a proton–protein antiporter (F004); the cytoplasmic ATPase complex (FliI/FliH/FliJ) assists substrate delivery and unfolding.

3. **Localization:** FliP works at the **cytoplasmic membrane, within the MS ring at the base of the basal body** (F003). The bulk of the assembled FliP₅Q₄R core faces the periplasmic side of the machine (F006), positioning the channel to hand off cargo to the nascent rod/hook.

4. **Structural role:** The five FliP copies form the largest fraction of the helical core (F006) and both **template** the downstream helical architecture and **line the conduit** through which cargo passes (F002). The methionine-rich loop at the inner mouth likely forms an adaptable seal around cargo.

5. **Conservation:** Because FliP = injectisome SctR (F005), the same architecture underpins virulence secretion systems, underscoring that this is an ancient, constrained protein-export solution.

### Comparative summary table

| Property | FliP (this protein) | Notes / evidence |
|---|---|---|
| Family | FliP/MopC/SpaP (PF00813; IPR005837/8) | Assignment for Q88EU8 |
| Class | Structural / channel-forming, **not** enzyme or solute transporter | F001, F002 |
| Copies in core | **5** | 5:4:1 FliP:FliQ:FliR (F006) |
| Topology | N-term cleavable signal peptide; 4 TM helices; periplasmic FliP_P domain; non-canonical in assembled state | F003, F006 |
| Localization | Inner membrane, within MS ring; core faces periplasm | F003, F006 |
| Energy source | Proton-motive force (+ ATP); gate = proton–protein antiporter | F004 |
| Substrate | Unfolded flagellar axial subunits (rod/hook/filament) | F002, F004 |
| Injectisome homolog | SctR | F005 |
| Structure | PDB 6F2D, 4.2 Å cryo-EM | F006 |

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports the findings |
|---|---|---|
| [29076571](https://pubmed.ncbi.nlm.nih.gov/29076571/) | *Type-III secretion pore formed by flagellar protein FliP* | Core evidence that FliP forms the protein-conducting conduit (F002) and is one of five essential membrane proteins (F001); identifies the Met-rich gasket loop. |
| [29967543](https://pubmed.ncbi.nlm.nih.gov/29967543/) | *Structure of the core of the T3SS export apparatus* | 4.2 Å cryo-EM defining 5:4:1 stoichiometry, non-canonical topology, and periplasmic localization of the gate core (F006). |
| [30018321](https://pubmed.ncbi.nlm.nih.gov/30018321/) | *Author Correction* | Corrects PDB accession to 6F2D (F006). |
| [28771466](https://pubmed.ncbi.nlm.nih.gov/28771466/) | *Assembly and stoichiometry of the core structure of the export gate* | FliP ring nucleates gate assembly inside MS ring; gate = FlhA/FlhB/FliP/FliQ/FliR (F002, F003). |
| [9324257](https://pubmed.ncbi.nlm.nih.gov/9324257/) | *FliO, FliP, FliQ, FliR of S. typhimurium* | Genetics establishing *fliP* essentiality for flagellation via type III export (F001); demonstrates signal-peptide cleavage (F003). |
| [25195894](https://pubmed.ncbi.nlm.nih.gov/25195894/) | *Crystallization of the periplasmic domain of FliP* | Defines topology: signal peptide, 4 TM helices, periplasmic FliP_P domain (F003). |
| [24064315](https://pubmed.ncbi.nlm.nih.gov/24064315/) | *Protein export through the flagellar T3S pathway* | PMF + ATP energization; export gate = proton–protein antiporter; directional export to distal tip (F004). |
| [31183905](https://pubmed.ncbi.nlm.nih.gov/31183905/) | *Inner rod of injectisome T3SS* | SctR/S/T form the injectisome conduit — homologs of FliP/FliQ/FliR (F005). |
| [34303721](https://pubmed.ncbi.nlm.nih.gov/34303721/) | *Conserved salt bridges facilitate core assembly* | Conserved buried charges drive helical core assembly across T3SS (F005). |
| [11520608](https://pubmed.ncbi.nlm.nih.gov/11520608/) | *Bacterial flagella and T3SS* | Documents shared homologous components between flagellum and injectisome (F005). |

Additional context papers reviewed but not central to the core annotation include studies on the flagellar secretion-specificity switch ([PMID: 42262106](https://pubmed.ncbi.nlm.nih.gov/42262106/)), functional activation of the export apparatus via SwrB acting on FliP in *B. subtilis* ([PMID: 26244495](https://pubmed.ncbi.nlm.nih.gov/26244495/)), FlgM secretion requiring the FliO/P/Q/R/FlhA/FlhB apparatus ([PMID: 25313396](https://pubmed.ncbi.nlm.nih.gov/25313396/)), and *Pseudomonas*-specific flagellar regulation via the PilZ-domain protein FlgZ and c-di-GMP signaling ([PMID: 24504373](https://pubmed.ncbi.nlm.nih.gov/24504373/)). Several *P. putida* genome/metabolism papers appeared in searches but are unrelated to FliP function and were excluded from the annotation.

---

## Limitations and Knowledge Gaps

1. **Direct experimental evidence for the *P. putida* KT2440 protein is lacking.** All mechanistic and structural findings derive from orthologs, chiefly *Salmonella* Typhimurium, with contributions from *E. coli* and *B. subtilis*. The functional assignment for Q88EU8 rests on **strong orthology** (PF00813 family membership and high sequence conservation of the T3SS core), not on direct study of PP_4355. No *P. putida fliP* knockout, complementation, or structural study was identified.

2. **Species-specific features are unquantified.** *P. putida* KT2440 assembles a **polar** flagellum, and its flagellar regulatory circuitry (e.g., c-di-GMP / FlgZ signaling; [PMID: 24504373](https://pubmed.ncbi.nlm.nih.gov/24504373/)) differs from peritrichously flagellated enterics. Whether *P. putida* FliP has organism-specific regulatory partners or assembly kinetics is unknown.

3. **The signal-peptide cleavage question in Pseudomonas is unresolved.** Cleavage was demonstrated in *Salmonella* FliP ([PMID: 9324257](https://pubmed.ncbi.nlm.nih.gov/9324257/)); it has not been verified for the *P. putida* ortholog, though the N-terminal features are expected to be conserved.

4. **Mechanistic details of gating and cargo threading remain partial.** The Met-rich "gasket" model is inferred from conductance mutants ([PMID: 29076571](https://pubmed.ncbi.nlm.nih.gov/29076571/)); an atomic-resolution structure of the channel with cargo engaged is not yet available. Export-gate stoichiometry itself evolved in the literature (early hexamer model → 5:4:1 helical core), so a *P. putida*-specific structure would confirm the local architecture.

5. **No quantitative kinetics** (export rates, PMF dependence coefficients) are available for the *P. putida* system; energy-coupling data derive from enteric models ([PMID: 24064315](https://pubmed.ncbi.nlm.nih.gov/24064315/)). The precise coupling of FliP to proton flux versus FlhA/FlhB remains an active research area.

---

## Proposed Follow-up Experiments / Actions

1. **Sequence and structural verification for Q88EU8.** Align *P. putida* PP_4355 against *Salmonella* FliP and injectisome SctR; confirm conservation of the four TM helices, the periplasmic FliP_P domain, the signal-peptide cleavage site, and the methionine-rich inner-mouth loop. Generate an AlphaFold model of PP_4355 and superpose it onto the FliP chain(s) of PDB 6F2D to confirm the non-canonical fold and predicted 5-copy interface.

2. **Genetic validation in KT2440.** Construct a clean *fliP* (PP_4355) deletion and test for loss of swimming motility on soft agar; complement with the wild-type allele and with the *Salmonella fliP* ortholog to test functional interchangeability.

3. **Topology and processing.** Use dual-tag/reporter fusions and immunoblotting to test whether *P. putida* FliP undergoes signal-peptide cleavage (25→23 kDa shift) and to confirm the periplasmic orientation of FliP_P.

4. **Assembly stoichiometry in situ.** Apply cryo-EM / cryo-ET of *P. putida* polar flagellar basal bodies to test whether the 5:4:1 FliP:FliQ:FliR core is conserved in this organism.

5. **Substrate-channel interaction.** Site-directed mutagenesis of the Met-rich loop in *P. putida* FliP, coupled with export assays of a reporter axial substrate, to test the gasket model in this species.

6. **Regulatory integration.** Investigate whether *P. putida*-specific factors (e.g., c-di-GMP effectors such as FlgZ) influence FliP-dependent export or gate activation, analogous to SwrB in *B. subtilis* ([PMID: 26244495](https://pubmed.ncbi.nlm.nih.gov/26244495/)).

---

## Conclusion

FliP (Q88EU8, PP_4355) in *Pseudomonas putida* KT2440 is an essential, integral inner-membrane **structural/channel-forming subunit** of the flagellar type III secretion export apparatus. Five copies of FliP assemble with FliQ and FliR in a 5:4:1 helical core that forms the protein-conducting conduit of the export gate, translocating unfolded flagellar axial subunits from the cytoplasm to the distal tip of the growing flagellum under proton-motive-force energization. It functions at the cytoplasmic membrane within the MS ring of the basal body, its core facing the periplasm, and it is evolutionarily conserved as the injectisome subunit SctR. The annotation is exceptionally well supported for the protein family by genetics, biochemistry, and 4.2 Å cryo-EM in model organisms, and is transferred to the *P. putida* protein by strong orthology.


## Artifacts

- [OpenScientist final report](fliP-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](fliP-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:29076571
2. PMID:9324257
3. PMID:28771466
4. PMID:25195894
5. PMID:24064315
6. PMID:11520608
7. PMID:31183905
8. PMID:34303721
9. PMID:29967543
10. PMID:30018321
11. PMID:42262106
12. PMID:26244495
13. PMID:25313396
14. PMID:24504373