---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-16T10:14:09.960042'
end_time: '2026-07-16T10:27:57.439253'
duration_seconds: 827.48
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: rpoC
  gene_symbol: rpoC
  uniprot_accession: Q88QP1
  protein_description: 'RecName: Full=DNA-directed RNA polymerase subunit beta'' {ECO:0000255|HAMAP-Rule:MF_01322};
    Short=RNAP subunit beta'' {ECO:0000255|HAMAP-Rule:MF_01322}; EC=2.7.7.6 {ECO:0000255|HAMAP-Rule:MF_01322};
    AltName: Full=RNA polymerase subunit beta'' {ECO:0000255|HAMAP-Rule:MF_01322};
    AltName: Full=Transcriptase subunit beta'' {ECO:0000255|HAMAP-Rule:MF_01322};'
  gene_info: Name=rpoC {ECO:0000255|HAMAP-Rule:MF_01322}; OrderedLocusNames=PP_0448;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the RNA polymerase beta' chain family.
  protein_domains: DNA-dir_RpoC_beta_prime. (IPR045867); DNA-dir_RpoC_beta_prime_bact.
    (IPR012754); RNA_pol_asu. (IPR000722); RNA_pol_N. (IPR006592); RNA_pol_Rpb1_1.
    (IPR007080)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 33
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: rpoC-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: rpoC-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88QP1
- **Protein Description:** RecName: Full=DNA-directed RNA polymerase subunit beta' {ECO:0000255|HAMAP-Rule:MF_01322}; Short=RNAP subunit beta' {ECO:0000255|HAMAP-Rule:MF_01322}; EC=2.7.7.6 {ECO:0000255|HAMAP-Rule:MF_01322}; AltName: Full=RNA polymerase subunit beta' {ECO:0000255|HAMAP-Rule:MF_01322}; AltName: Full=Transcriptase subunit beta' {ECO:0000255|HAMAP-Rule:MF_01322};
- **Gene Information:** Name=rpoC {ECO:0000255|HAMAP-Rule:MF_01322}; OrderedLocusNames=PP_0448;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the RNA polymerase beta' chain family.
- **Key Domains:** DNA-dir_RpoC_beta_prime. (IPR045867); DNA-dir_RpoC_beta_prime_bact. (IPR012754); RNA_pol_asu. (IPR000722); RNA_pol_N. (IPR006592); RNA_pol_Rpb1_1. (IPR007080)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "rpoC" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'rpoC' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **rpoC** (gene ID: rpoC, UniProt: Q88QP1) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# rpoC (β′ subunit of RNA polymerase) in *Pseudomonas putida* KT2440 — Functional Annotation Report

**Gene:** rpoC | **Ordered locus:** PP_0448 | **UniProt:** Q88QP1
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / NCIMB 11950 / KT2440), abbreviated PSEPK
**Enzyme:** DNA-directed RNA polymerase subunit β′ (RNAP β′) | **EC 2.7.7.6**

---

## Summary

**rpoC encodes the β′ subunit, the largest (1,399 aa; ~154.8 kDa) and catalytic subunit of the multisubunit DNA-dependent RNA polymerase (RNAP) of *Pseudomonas putida* KT2440.** Its primary function is template-directed synthesis of RNA (EC 2.7.7.6): using a DNA template and the four ribonucleoside triphosphates (NTPs) as substrates, it catalyzes the reaction RNA(n) + NTP → RNA(n+1) + diphosphate (Rhea:21248). β′ carries the catalytic center of the enzyme: it chelates the essential catalytic Mg²⁺ ion through an absolutely conserved aspartate-triad motif (**NADFDGD**), which in the Q88QP1 sequence lies at residues 458–464, placing the metal-coordinating aspartates at positions 460, 462, and 464. The subunit also binds two structural Zn²⁺ ions. Because *P. putida* has a single bacterial RNAP, rpoC is essential and non-redundant: every mRNA, rRNA, and tRNA in the cell is made by an enzyme containing this subunit.

Structurally, β′ is far more than a catalytic scaffold — it is the organizing and regulatory hub of the enzyme. It forms one pincer of the "crab-claw"-shaped RNAP and builds the mobile **clamp** that opens to load DNA and closes to confer the high stability of initiation complexes and the processivity of elongation complexes. The β′ **switch regions** couple clamp motion to promoter DNA opening; the β′ **secondary channel** is the conduit for incoming NTP substrates and the docking port for regulatory factors (GreA/GreB, DksA) and the stringent-response alarmone (p)ppGpp; and the β′ **clamp-helices domain** is the universal platform onto which σ factors dock during initiation and NusG/Spt5 dock during elongation. β′ is the last subunit recruited during core assembly, a step chaperoned by the ω subunit.

The enzyme functions in the **cytoplasm, associated with the nucleoid**, and concentrates into RNAP condensates at sites of high ribosomal-RNA synthesis. In *P. putida* KT2440 specifically, the single β′-containing core partners with **24 σ factors** (19 of them extracytoplasmic-function, ECF, σ factors) to generate a large repertoire of promoter-specific holoenzymes that drive this metabolically versatile soil bacterium's adaptation to solvents, iron limitation, oxidative stress, and stationary-phase transitions. β′ is thus both the catalytic engine and the master regulatory node of gene expression in this organism, and its clamp, switch, and secondary-channel elements are validated antibiotic targets.

---

## Gene/Protein Identity Verification

Before reporting function, the target identity was rigorously confirmed. **The gene symbol "rpoC" matches the UniProt protein description exactly**, and all literature located is consistent with the correct gene, organism, and family:

| Criterion | UniProt reference | Verification result |
|---|---|---|
| Gene symbol | rpoC | ✅ Matches — rpoC universally denotes RNAP β′ across bacteria |
| Protein | DNA-directed RNA polymerase subunit β′ (EC 2.7.7.6) | ✅ Confirmed by sequence, family, and catalytic motif |
| Organism | *P. putida* KT2440 (PSEPK) | ✅ PP_0448 is the KT2440 ordered locus for rpoC |
| Family | RNA polymerase β′ chain family | ✅ IPR000722, IPR012754 present |
| Catalytic motif | β′ aspartate triad | ✅ NADFDGD found at residues 458–464 in Q88QP1 |
| Operon context | — | ✅ rpoB (Q88QP2, PP_0447) immediately upstream (rpoBC operon) |

The gene symbol is **not** ambiguous in this case: rpoC is one of the most conserved and well-annotated genes in all of biology. Much of the deep mechanistic literature comes from model systems (*Escherichia coli*, *Thermus aquaticus*, *Bacillus subtilis*, *Salmonella*), but the extraordinary sequence and structural conservation of β′ — high enough that the *E. coli* core structure was interpreted directly from the *T. aquaticus* crystal model [PMID: 11904365](https://pubmed.ncbi.nlm.nih.gov/11904365/) — makes these findings directly transferable to the *P. putida* orthologue. Organism-specific findings are drawn from KT2440 studies where available.

---

## Key Findings

### F001 / F011 — β′ is the catalytic subunit carrying the Mg²⁺ active site, encoded in the rpoBC operon

Q88QP1 is a 1,399-amino-acid, ~154.8-kDa polypeptide catalyzing the core reaction of transcription (EC 2.7.7.6): **RNA(n) + a ribonucleoside triphosphate → RNA(n+1) + diphosphate** (Rhea:21248). The defining catalytic feature is the **absolutely conserved aspartate-triad motif NADFDGD**. Computational re-verification of the Q88QP1 sequence localized this motif to residues 458–464, positioning the three Mg²⁺-chelating aspartates at **positions 460, 462, and 464**. These aspartates coordinate the catalytic Mg²⁺ ion that performs the two-metal-ion nucleotidyl-transfer reaction. The subunit additionally binds two structural Zn²⁺ ions. Annotation is governed by HAMAP-Rule MF_01322, and the protein belongs to the RNA polymerase β′ chain family (IPR000722, IPR012754).

The gene sits in the classic bacterial **rpoBC operon**: UniProt locus-tag adjacency confirms that rpoB (Q88QP2 = PP_0447, encoding the β subunit) lies immediately upstream of rpoC (Q88QP1 = PP_0448, β′). This gene arrangement — the two large catalytic subunits co-transcribed — is conserved across bacteria and ensures stoichiometric co-production of the β/β′ catalytic pair.

### F002 — β′ forms the "crab-claw" active-center wall and houses the catalytic Mg²⁺

The 3.3 Å crystal structure of *Thermus aquaticus* core RNAP (Zhang et al., *Cell* 1999) revealed a **"crab claw"-shaped molecule with a 27 Å-wide internal channel**; a catalytic Mg²⁺ ion sits on the back wall of the channel, chelated by an absolutely conserved motif — the β′ NADFDGD aspartate triad — that is conserved in **all bacterial and eukaryotic cellular RNA polymerases** [PMID: 10499798](https://pubmed.ncbi.nlm.nih.gov/10499798/). β′, the largest subunit, forms one pincer of the claw and the mobile clamp. The conservation is so high that the *E. coli* core enzyme structure could be interpreted directly from the *T. aquaticus* model [PMID: 11904365](https://pubmed.ncbi.nlm.nih.gov/11904365/). This establishes that the *P. putida* β′ likewise builds the active-center wall and holds the catalytic metal.

### F005 — β′ builds the secondary channel: the NTP-substrate conduit and regulator docking site

The RNAP **secondary channel** — a β′-lined pore — is the route by which incoming NTP substrates reach the catalytic center and through which the 3′ RNA end threads during backtracking. It also accepts the transcript-cleavage factors **GreA/GreB** [PMID: 15200953](https://pubmed.ncbi.nlm.nih.gov/15200953/). In proteobacteria (which include *P. putida*), the stringent-response alarmones **(p)ppGpp bind two RNAP sites**: site 1 at the interface of the β′ and ω subunits, and site 2 at the interface of the β′ secondary channel and the transcription factor **DksA** [PMID: 30200857](https://pubmed.ncbi.nlm.nih.gov/30200857/); this two-site architecture is corroborated in *Azotobacter* [PMID: 38574051](https://pubmed.ncbi.nlm.nih.gov/38574051/). Gre factors entering the β′ secondary channel improve elongation fidelity and resolve transcriptional pauses in metabolic-gene transcription during oxidative stress [PMID: 37014914](https://pubmed.ncbi.nlm.nih.gov/37014914/). Thus β′ is not only catalytic but the physical gateway through which substrate entry and the most important stress-signaling regulators act.

### F003 — The β′ mobile clamp confers initiation-complex stability and elongation processivity

Single-molecule FRET studies show that the β′-formed **clamp is open in free RNAP and early initiation intermediates, and closes upon formation of a catalytically competent initiation complex, remaining closed through initial transcription and elongation**. Clamp closure "accounts for the high stability of initiation complexes and the high stability and processivity of elongation complexes," while clamp opening allows DNA loading and unwinding in the active-center cleft [PMID: 22859489](https://pubmed.ncbi.nlm.nih.gov/22859489/). The clamp interconverts dynamically among three conformational states on 0.1–1 s timescales, and the alarmone **ppGpp selectively stabilizes a partly-closed-clamp state**, thereby modulating promoter opening [PMID: 29878276](https://pubmed.ncbi.nlm.nih.gov/29878276/). Clamp dynamics are therefore a central regulatory lever on the transcription cycle.

### F009 — β′ switch regions couple clamp motion to promoter DNA opening and are validated antibiotic targets

The RNAP **switch regions** are the hinges connecting the mobile clamp to the enzyme body; they control the clamp conformational change required for open-promoter-complex formation and template-DNA loading. The natural-product antibiotic **myxopyronin** binds the switch regions to block these rearrangements [PMID: 22965125](https://pubmed.ncbi.nlm.nih.gov/22965125/). X-ray cocrystal structures of *E. coli* RNAP with **squaramide** inhibitors show displacement of switch 2, "predicted to interfere with the conformational change of the clamp domain and/or with binding of template DNA, a mechanism akin to that of natural product myxopyronin" [PMID: 25798859](https://pubmed.ncbi.nlm.nih.gov/25798859/). β′ additionally forms the secondary-channel target of the peptide antibiotic **microcin J25** [PMID: 15200953](https://pubmed.ncbi.nlm.nih.gov/15200953/). These findings establish β′ conformational machinery as a druggable surface.

### F010 — The β′ clamp-helices domain is the universal docking hub for σ (initiation) and NusG/Spt5 (elongation) factors

Among the core RNAP elements contacting downstream duplex DNA that stabilize initiation and persist into elongation, "**the β′ clamp domain plays the most prominent role**" [PMID: 27956639](https://pubmed.ncbi.nlm.nih.gov/27956639/). The universally conserved **NusG/Spt5** elongation factors "bind to the conserved clamp helices domain of RNA polymerase, which also interacts with non-homologous initiation factors in all domains of life, and reach across the DNA channel to form processivity clamps that enable uninterrupted RNA chain synthesis" [PMID: 25640595](https://pubmed.ncbi.nlm.nih.gov/25640595/). Cryo-EM shows the NusG N-terminal domain binding the β′ clamp helices (together with the β protrusion/lobe), constraining the clamp and enhancing processivity [PMID: 27899640](https://pubmed.ncbi.nlm.nih.gov/27899640/); key β′ clamp-helix residues R270/R278/R281 form the NusG interface, itself a validated antimicrobial target [PMID: 39196895](https://pubmed.ncbi.nlm.nih.gov/39196895/). Rho-dependent termination requires opening of the β′ clamp and engages the β′ Zn-binding domain/clamp helices [PMID: 33243850](https://pubmed.ncbi.nlm.nih.gov/33243850/), [PMID: 39730149](https://pubmed.ncbi.nlm.nih.gov/39730149/). This mutually exclusive docking on a single β′ surface is what makes the clamp helices the master switchboard of the transcription cycle. A separate, earlier study mapping the σ⁷⁰-binding site to β′ residues 260–309 (a coiled-coil, equivalent to the clamp-helices region) reinforces this: point mutations there (R275Q, E295K, A302D) disrupt holoenzyme formation and are lethal [PMID: 10764785](https://pubmed.ncbi.nlm.nih.gov/10764785/).

### F006 — β′ is the last subunit recruited during RNAP assembly; ω chaperones its folding

The bacterial core enzyme is α₂ββ′ω. The smallest subunit, ω, "has a structural role in maintaining the conformation of the largest subunit, β′, and its recruitment in the enzyme assembly" [PMID: 33238579](https://pubmed.ncbi.nlm.nih.gov/33238579/). ω is universally conserved, with orthologues even in obligate intracellular bacteria [PMID: 36719197](https://pubmed.ncbi.nlm.nih.gov/36719197/). The canonical *E. coli* assembly order is α → α₂ → α₂β → α₂ββ′ → holoenzyme, with β′ added after the β subunit; a noncanonical branch in *B. subtilis* allows the α-dimer to associate with either β or β′ before core formation [PMID: 42001948](https://pubmed.ncbi.nlm.nih.gov/42001948/). β′ is therefore the capstone subunit whose correct incorporation completes the catalytically competent core.

### F007 — Localization: cytoplasm, on the nucleoid, in rRNA-synthesis condensates

As the core transcription enzyme acting directly on chromosomal DNA, RNAP (and thus β′) is a **cytoplasmic, nucleoid-associated enzyme**. Bacterial RNAP condensates colocalize with pre-rRNA synthesis, assemble in proportion to high rRNA synthesis, and dissolve upon nutritional stress; the ω subunit (which contributes to (p)ppGpp binding site 1 with β′) is critical for condensate maintenance during acid stress, and condensate persistence correlates with survival during acid-stress recovery [PMID: 41959101](https://pubmed.ncbi.nlm.nih.gov/41959101/). This positions β′-containing RNAP conceptually close to the eukaryotic nucleolus in its spatial organization.

### F008 — In *P. putida* KT2440, the single β′-containing core partners with 24 σ factors for environmental adaptation

Genome analysis of KT2440 identified **24 σ factors, 19 of them ECF σ factors, with 13 FecI-like (iron-acquisition) σ factors** [PMID: 12534467](https://pubmed.ncbi.nlm.nih.gov/12534467/). A genome-wide microarray study of the KT2440 transcriptional machinery examined the RNAP core-subunit genes and the 24 σ factors, showing that expression of the RNAP core and the vegetative σ decreased in stationary phase while σ^S (RpoS) increased [PMID: 16343331](https://pubmed.ncbi.nlm.nih.gov/16343331/). Specific ECF σ factors reprogram the β′-containing holoenzyme to control physiology: **RpoT/ECF-Pp12** governs solvent (toluene) tolerance and efflux-pump expression [PMID: 17071759](https://pubmed.ncbi.nlm.nih.gov/17071759/), and **ECF-10** controls stress resistance, multidrug efflux (TtgABC), and biofilm formation [PMID: 24907323](https://pubmed.ncbi.nlm.nih.gov/24907323/). The single, essential β′ subunit is the common core onto which all these regulatory σ factors dock (via the clamp-helices platform of F010) to steer this versatile soil bacterium's adaptation.

### F004 — Organism context: essential housekeeping subunit of an industrial chassis

PP_0448 = rpoC is the single-copy β′ subunit of the sole bacterial RNAP in *P. putida* KT2440, a "versatile soil bacterium" and emerging industrial cell factory that uses the Entner–Doudoroff pathway for glucose metabolism [PMID: 39837196](https://pubmed.ncbi.nlm.nih.gov/39837196/). As the catalytic subunit responsible for all mRNA/rRNA/tRNA synthesis, rpoC is essential; genome-scale omics and fitness studies treat the core transcription machinery as essential housekeeping genes [PMID: 36853682](https://pubmed.ncbi.nlm.nih.gov/36853682/), [PMID: 32826213](https://pubmed.ncbi.nlm.nih.gov/32826213/).

---

## Mechanistic Model / Interpretation

### The dual identity of β′: catalytic engine + regulatory switchboard

β′ can be understood as two integrated machines built into one polypeptide. First, it is the **catalytic engine**: its NADFDGD aspartate triad (residues 460/462/464 in Q88QP1) holds the Mg²⁺ that performs nucleotidyl transfer at the back wall of the crab-claw channel. Second, it is the **regulatory switchboard**: its clamp, switch regions, secondary channel, and clamp-helices are the moving parts and docking surfaces through which the entire transcription cycle is controlled.

```
                    P. putida RNA polymerase core (a2 b b' w)
                    ============= "crab claw" =============

                            b' CLAMP  (mobile pincer)
                          /  \    <- opens to load DNA
       s / NusG dock ->  CLAMP HELICES   -> closes for processivity
                          \  /
        downstream DNA  ---+          SWITCH REGIONS (hinges)
        contacts (b')  ----|          <- myxopyronin, squaramides bind
                           |
             +-------------+-------------+
             |   ACTIVE CENTER           |
             |   Mg2+ <= NADFDGD         |  <- catalysis
             |   (D460/D462/D464)        |
             +-------------+-------------+
                           |
                    SECONDARY CHANNEL (b'-lined)
                    <- NTP substrate entry
                    <- GreA/GreB (cleavage/fidelity)
                    <- DksA + (p)ppGpp site 2 (stringent response)
                    <- microcin J25 (antibiotic)

      (p)ppGpp site 1  =  b'-w interface
```

### How the parts work together across the transcription cycle

| Phase | β′ element in action | Consequence |
|---|---|---|
| Assembly | β′ recruited last; ω chaperones its fold | Completes catalytically competent core |
| Holoenzyme formation | Clamp-helices (~res 260–309) bind σ factor | Promoter specificity conferred (24 σ options in KT2440) |
| Promoter opening | Switch regions transmit clamp closure | Open complex forms; DNA loaded/melted |
| Initiation → elongation | Clamp closes and stays closed | Stability + processivity |
| Substrate loading | NTPs enter via secondary channel | Nucleotide addition at Mg²⁺ center |
| Fidelity / pausing | GreA/GreB enter secondary channel | Proofreading, pause resolution |
| Stress signaling | (p)ppGpp at β′–ω (site 1) + DksA/β′ channel (site 2) | Stringent response reprograms transcription |
| Elongation control | NusG/Spt5 bind clamp-helices | Enhanced processivity, coupling |
| Termination | Rho opens β′ clamp; engages β′ Zn-domain | Enzyme inactivation, transcript release |

### Why this matters for *P. putida* biology

Because *P. putida* KT2440 possesses only one RNAP core but 24 σ factors, β′ is the physical convergence point of the organism's regulatory logic. Environmental cues — solvent stress (RpoT), iron limitation (13 FecI-like ECF σ factors), general stress/stationary phase (RpoS), oxidative stress (Gre/stringent response) — all ultimately act by loading a particular σ or regulator onto the same β′ clamp-helices/secondary-channel surfaces. This makes β′ simultaneously the most conserved housekeeping enzyme and the master integrator of adaptive gene expression in this industrially important chassis.

---

## Evidence Base

| PMID | Study (system) | Supports finding | Key contribution |
|---|---|---|---|
| [10499798](https://pubmed.ncbi.nlm.nih.gov/10499798/) | *T. aquaticus* core RNAP crystal, 3.3 Å | F002 | Crab-claw shape; catalytic Mg²⁺ chelated by conserved β′ motif |
| [11904365](https://pubmed.ncbi.nlm.nih.gov/11904365/) | *E. coli* cryo-EM | F002 | β′ conservation lets Taq model interpret *E. coli*; clamp flexibility |
| [22859489](https://pubmed.ncbi.nlm.nih.gov/22859489/) | smFRET clamp (*E. coli*) | F003 | Clamp open→closed transition = stability + processivity |
| [29878276](https://pubmed.ncbi.nlm.nih.gov/29878276/) | smFRET clamp | F003 | Three clamp states; ppGpp stabilizes partly-closed clamp |
| [15200953](https://pubmed.ncbi.nlm.nih.gov/15200953/) | Microcin J25 mechanism | F005, F009 | Secondary channel = NTP/Gre route; antibiotic target |
| [30200857](https://pubmed.ncbi.nlm.nih.gov/30200857/) | Review (ppGpp/DksA) | F005 | Two (p)ppGpp sites: β′–ω and β′ channel/DksA |
| [38574051](https://pubmed.ncbi.nlm.nih.gov/38574051/) | *Azotobacter* stringent response | F005 | Corroborates two-site (p)ppGpp architecture |
| [37014914](https://pubmed.ncbi.nlm.nih.gov/37014914/) | *Salmonella* Gre factors | F005 | Gre in β′ channel improves metabolic-gene fidelity |
| [22965125](https://pubmed.ncbi.nlm.nih.gov/22965125/) | Myxopyronin / switch regions | F009 | Switch regions control clamp/open-complex; drug target |
| [25798859](https://pubmed.ncbi.nlm.nih.gov/25798859/) | Squaramide cocrystals (*E. coli*) | F009 | Switch-2 displacement blocks clamp/DNA loading |
| [27956639](https://pubmed.ncbi.nlm.nih.gov/27956639/) | Gate loop / clamp study | F010 | β′ clamp "most prominent" downstream-DNA contact |
| [25640595](https://pubmed.ncbi.nlm.nih.gov/25640595/) | NusG/Spt5 review | F010 | Clamp-helices = universal σ + NusG docking hub |
| [27899640](https://pubmed.ncbi.nlm.nih.gov/27899640/) | NusG–RNAP cryo-EM | F010 | NGN binds β′ clamp helices, constrains clamp |
| [39196895](https://pubmed.ncbi.nlm.nih.gov/39196895/) | NusG–CH inhibitors | F010 | β′ R270/R278/R281 = NusG interface, drug target |
| [33243850](https://pubmed.ncbi.nlm.nih.gov/33243850/) | Rho termination cryo-EM | F010 | Clamp opening + β′ Zn-domain in termination |
| [39730149](https://pubmed.ncbi.nlm.nih.gov/39730149/) | Rho genetic network | F010 | β′ Zn-finger/clamp helices functionally in termination |
| [10764785](https://pubmed.ncbi.nlm.nih.gov/10764785/) | β′260–309 σ⁷⁰ mutants | F010 | β′ coiled-coil is σ-binding site; mutations lethal |
| [33238579](https://pubmed.ncbi.nlm.nih.gov/33238579/) | ω subunit review | F006 | ω maintains β′ conformation, aids β′ recruitment |
| [36719197](https://pubmed.ncbi.nlm.nih.gov/36719197/) | ω in intracellular bacteria | F006 | ω universally conserved |
| [42001948](https://pubmed.ncbi.nlm.nih.gov/42001948/) | *B. subtilis* assembly | F006 | β′ added after β; noncanonical branch exists |
| [41959101](https://pubmed.ncbi.nlm.nih.gov/41959101/) | RNAP condensates | F007 | RNAP condensates at rRNA sites; ω-dependent under acid stress |
| [12534467](https://pubmed.ncbi.nlm.nih.gov/12534467/) | KT2440 σ-factor genome analysis | F008 | 24 σ factors (19 ECF, 13 FecI-like) |
| [16343331](https://pubmed.ncbi.nlm.nih.gov/16343331/) | KT2440 microarray | F008 | RNAP core + σ expression across growth phases |
| [17071759](https://pubmed.ncbi.nlm.nih.gov/17071759/) | RpoT regulon (*P. putida*) | F008 | ECF σ RpoT controls solvent tolerance/efflux |
| [24907323](https://pubmed.ncbi.nlm.nih.gov/24907323/) | ECF-10 knockout (KT2440) | F008 | ECF σ controls efflux/biofilm/stress |
| [39837196](https://pubmed.ncbi.nlm.nih.gov/39837196/) | Industrial chassis review | F004 | KT2440 as versatile industrial platform |

Supporting mechanistic detail on the nucleotide-addition cycle and active-site dynamics (trigger loop, bridge helix, F loop) further underpins the catalytic model: [PMID: 19855007](https://pubmed.ncbi.nlm.nih.gov/19855007/), [PMID: 17679091](https://pubmed.ncbi.nlm.nih.gov/17679091/), [PMID: 19481445](https://pubmed.ncbi.nlm.nih.gov/19481445/), and [PMID: 23283976](https://pubmed.ncbi.nlm.nih.gov/23283976/) (active-center "tuning" and the two-Mg²⁺ mechanism, with Gre-factor acceleration of intrinsic cleavage 3,000–4,000-fold).

---

## Limitations and Knowledge Gaps

1. **Species of experimental evidence.** The deep structural and mechanistic data derive from model organisms (*T. aquaticus*, *E. coli*, *B. subtilis*, *Salmonella*, *Azotobacter*), not from *P. putida* β′ directly. The inference to Q88QP1 rests on the extreme conservation of β′ (the catalytic motif and clamp/switch/secondary-channel architecture are universal), which is very strong but remains inference for the KT2440 orthologue specifically.

2. **No *P. putida* β′ structure.** There is no experimentally determined structure of the *P. putida* KT2440 RNAP reported here; residue-level annotations (e.g., D460/462/464, clamp-helix residues) are mapped by homology/sequence to Q88QP1 rather than solved crystallographically for this protein.

3. **σ-factor pairing specifics.** While 24 σ factors are documented for KT2440, the precise β′ contact residues for each ECF σ and the quantitative promoter repertoires are not fully resolved for most of the 19 ECF σ factors.

4. **Essentiality is inferred, not directly demonstrated here.** rpoC essentiality is treated as established housekeeping biology and is consistent with genome-scale fitness data, but a clean conditional-knockout demonstration in KT2440 was not located in this investigation.

5. **Stringent-response nuances.** The (p)ppGpp/DksA two-site model is well established in proteobacteria generally; some downstream effects (e.g., polyphosphate, PHB synthesis) show that DksA and (p)ppGpp can act via distinct routes [PMID: 30745375](https://pubmed.ncbi.nlm.nih.gov/30745375/), [PMID: 38574051](https://pubmed.ncbi.nlm.nih.gov/38574051/), so the precise regulon in *P. putida* would need dedicated study.

---

## Proposed Follow-up Experiments / Actions

1. **Cryo-EM structure of *P. putida* KT2440 RNAP** (core and representative ECF-σ holoenzymes) to confirm the β′ active-center geometry, clamp-helix docking residues, and any *Pseudomonas*-specific insertions.

2. **Site-directed mutagenesis of D460/D462/D464** (or conditional depletion) to experimentally validate the catalytic aspartate triad and quantify the effect on RNA synthesis in KT2440.

3. **ChIP-seq / genome-wide occupancy of β′-containing holoenzymes** paired with each of the 24 σ factors to map the promoter repertoires and directly link β′ to the adaptive regulons (solvent tolerance, iron acquisition, biofilm).

4. **Stringent-response profiling** (relA/spoT and dksA mutants) with transcriptomics to define the *P. putida* (p)ppGpp/DksA regulon acting through the β′ secondary channel and β′–ω interface.

5. **Antibiotic susceptibility mapping** targeting the β′ switch regions (myxopyronin/squaramide class), secondary channel (microcin J25), and clamp-helix–NusG interface, given the intrinsic multidrug-efflux phenotypes of *P. putida* — to assess whether transcription inhibitors bypass efflux-based resistance.

6. **In vivo imaging of RNAP condensates in KT2440** under nutrient shift and acid/solvent stress to test whether the ω/β′-dependent condensate behavior observed in other bacteria governs stress survival in this chassis.

---

## Conclusion

rpoC (PP_0448; Q88QP1) encodes the **β′ subunit** — the largest, catalytic subunit of the single essential DNA-dependent RNA polymerase of *Pseudomonas putida* KT2440. It catalyzes template-directed RNA synthesis (EC 2.7.7.6) through a Mg²⁺-dependent, two-metal-ion mechanism anchored by the absolutely conserved NADFDGD aspartate triad (D460/462/464). Beyond catalysis, β′ forms the crab-claw active-center wall, the mobile clamp and switch regions that load DNA and confer processivity, the secondary channel that admits NTP substrates and stringent-response regulators, and the clamp-helices platform that universally docks σ factors (initiation) and NusG/Spt5 (elongation). It functions in the cytoplasm on the nucleoid, concentrating in rRNA-synthesis condensates, and in KT2440 it is the common core for 24 σ factors that reprogram transcription for environmental adaptation. β′ is thus both the catalytic engine and the master regulatory hub of gene expression in this organism, and a validated antibiotic target.


## Artifacts

- [OpenScientist final report](rpoC-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](rpoC-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:11904365
2. PMID:10499798
3. PMID:15200953
4. PMID:30200857
5. PMID:38574051
6. PMID:37014914
7. PMID:22859489
8. PMID:29878276
9. PMID:22965125
10. PMID:25798859
11. PMID:27956639
12. PMID:25640595
13. PMID:27899640
14. PMID:39196895
15. PMID:33243850
16. PMID:39730149
17. PMID:10764785
18. PMID:33238579
19. PMID:36719197
20. PMID:42001948
21. PMID:41959101
22. PMID:12534467
23. PMID:16343331
24. PMID:17071759
25. PMID:24907323
26. PMID:39837196
27. PMID:36853682
28. PMID:32826213
29. PMID:19855007
30. PMID:17679091
31. PMID:19481445
32. PMID:23283976
33. PMID:30745375