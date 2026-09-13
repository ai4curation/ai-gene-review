---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-11T06:27:44.375886'
end_time: '2026-08-11T06:40:56.352525'
duration_seconds: 791.98
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: cysK
  gene_symbol: cysK
  uniprot_accession: Q88E95
  protein_description: 'RecName: Full=Cysteine synthase {ECO:0000256|ARBA:ARBA00019371,
    ECO:0000256|RuleBase:RU003985}; EC=2.5.1.47 {ECO:0000256|ARBA:ARBA00012681, ECO:0000256|RuleBase:RU003985};'
  gene_info: Name=cysK {ECO:0000313|EMBL:AAN70144.1}; OrderedLocusNames=PP_4571 {ECO:0000313|EMBL:AAN70144.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the cysteine synthase/cystathionine beta-
  protein_domains: Cys_synth. (IPR005856); Cys_Synth/Cystath_Beta-Synth. (IPR050214);
    CysK. (IPR005859); P-phosphate_BS. (IPR001216); TrpB-like_PALP. (IPR001926)
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
citation_count: 7
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: cysK-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: cysK-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88E95
- **Protein Description:** RecName: Full=Cysteine synthase {ECO:0000256|ARBA:ARBA00019371, ECO:0000256|RuleBase:RU003985}; EC=2.5.1.47 {ECO:0000256|ARBA:ARBA00012681, ECO:0000256|RuleBase:RU003985};
- **Gene Information:** Name=cysK {ECO:0000313|EMBL:AAN70144.1}; OrderedLocusNames=PP_4571 {ECO:0000313|EMBL:AAN70144.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the cysteine synthase/cystathionine beta-
- **Key Domains:** Cys_synth. (IPR005856); Cys_Synth/Cystath_Beta-Synth. (IPR050214); CysK. (IPR005859); P-phosphate_BS. (IPR001216); TrpB-like_PALP. (IPR001926)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "cysK" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'cysK' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **cysK** (gene ID: cysK, UniProt: Q88E95) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *cysK* (PP_4571, UniProt Q88E95) in *Pseudomonas putida* KT2440

**Gene:** *cysK* · **Locus:** PP_4571 · **UniProt:** Q88E95 · **Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / NCIMB 11950 / KT2440), taxid 160488 · **EC:** 2.5.1.47

---

## Summary

**CysK (PP_4571, UniProt Q88E95) is O-acetylserine sulfhydrylase A (OASS-A; cysteine synthase A, EC 2.5.1.47)** — a soluble, cytoplasmic, pyridoxal-5′-phosphate (PLP)-dependent, fold-type II enzyme that catalyzes the second and committing step of de novo cysteine biosynthesis in *Pseudomonas putida* KT2440. The reaction it performs is a PLP-dependent β-replacement: **O-acetyl-L-serine + hydrogen sulfide → L-cysteine + acetate.** The enzyme incorporates inorganic sulfur (produced by the reductive sulfate-assimilation pathway) into the carbon/nitrogen backbone supplied by serine, thereby generating the cell's only reduced-sulfur amino acid precursor and, downstream, the sulfur destined for methionine, coenzymes, Fe–S clusters, and glutathione.

This identity is established with high confidence through convergent lines of evidence. UniProt directly annotates Q88E95 as "Cysteine synthase," EC 2.5.1.47, with the explicit catalytic reaction and the pathway step "L-cysteine biosynthesis; L-cysteine from L-serine: step 2/2." The protein carries every fold-type II OASS structural hallmark, including the catalytic PLP-attachment lysine at **Lys44** (N6-(pyridoxal phosphate)lysine), the glycine-rich PLP-phosphate binding loop, and the N-terminal substrate "asparagine loop." Reciprocal, whole-sequence identity analysis places PP_4571 unambiguously in the **CysK/OASS-A subfamily** (70.2% identical to the experimentally characterized *Escherichia coli* CysK, versus only ~41% to CysM/OASS-B enzymes), while the genome's separate paralogue Q88MC0 is the true CysM orthologue.

Beyond catalysis, CysK is a well-documented **moonlighting protein**. Through the same active-site cleft that engages the sulfur-donor chemistry, it (i) assembles the regulatory **cysteine synthase complex (CSC)** with serine acetyltransferase (CysE), and (ii) acts as an essential activating scaffold for **contact-dependent growth inhibition (CDI) CdiA-CT ribonuclease toxins**. Because this biosynthetic route is present in bacteria, protozoa, and plants but **absent in humans**, CysK/OASS is an actively pursued antibacterial drug target. This report synthesizes the sequence, structural, evolutionary, and literature evidence supporting these conclusions and identifies the remaining gaps specific to the *P. putida* KT2440 enzyme.

---

## Gene/Protein Identity Verification

Per the mandatory verification protocol, the gene symbol, organism, and domain architecture were all confirmed to be internally consistent before and during research:

| Verification criterion | Result |
|---|---|
| Gene symbol "cysK" matches protein description | ✅ UniProt Q88E95 RecName = "Cysteine synthase," EC 2.5.1.47 — exactly the reaction catalyzed by CysK/OASS |
| Organism correct | ✅ *Pseudomonas putida* KT2440 (taxid 160488); locus PP_4571; EMBL AAN70144.1 |
| Protein family/domains align with literature | ✅ Cys_synth (IPR005856), CysK (IPR005859), PLP binding site (IPR001216), TrpB-like PALP fold (IPR001926) — all diagnostic of fold-type II PLP cysteine-synthase enzymes |
| Literature is for the correct gene, not a same-symbol homolog | ✅ Reciprocal orthology (70% to *E. coli* CysK) confirms subfamily; supporting literature is on genuine OASS/CysK enzymes, with a same-genus (*P. aeruginosa*) orthologue characterized biochemically |

**No ambiguity was encountered.** "cysK" here refers to the canonical bacterial O-acetylserine sulfhydrylase A, and all cited literature concerns genuine CysK/OASS enzymes. Where direct experimental data on the *P. putida* KT2440 protein itself are lacking, the report relies on (a) the protein's own sequence/annotation and (b) the closest experimentally characterized orthologues (same-genus *P. aeruginosa*; and *E. coli*/*Salmonella*), which is the appropriate evidentiary basis for a well-conserved housekeeping enzyme.

---

## Key Findings

### F001 — CysK is O-acetylserine sulfhydrylase A catalyzing the final step of de novo cysteine biosynthesis

The primary function of PP_4571 is enzymatic. UniProt Q88E95 annotates the protein as **Cysteine synthase, EC 2.5.1.47**, a member of the **cysteine synthase/cystathionine β-synthase family** — the fold-type II class of PLP-dependent enzymes (InterPro CysK IPR005859, Cys_synth IPR005856, PLP binding site IPR001216, TrpB-like PALP fold IPR001926). The enzyme catalyzes the PLP-dependent **β-replacement reaction**:

```
O-acetyl-L-serine  +  H2S  →  L-cysteine  +  acetate
```

Mechanistically, PLP forms a Schiff base (internal aldimine) with the catalytic lysine; O-acetyl-L-serine (OAS) displaces this to form an external aldimine, β-elimination of acetate generates an α-aminoacrylate intermediate, and nucleophilic addition of sulfide yields L-cysteine. This is the **second and committing step of the two-step de novo (sulfide-incorporation) cysteine biosynthesis pathway**; the first step (serine → O-acetyl-L-serine) is catalyzed by **serine acetyltransferase (CysE)**.

This two-enzyme architecture is a defining, conserved feature of bacterial cysteine biosynthesis. As reviewed in [PMID: 38965664](https://pubmed.ncbi.nlm.nih.gov/38965664/): *"Serine acetyltransferase (SAT), also known as CysE in certain bacterial species, and O-acetylserine sulfhydrylase (OASS), also known as CysK in select bacteria, are indispensable enzymes within the cysteine biosynthesis pathway of various pathogenic microorganisms."* A second independent review ([PMID: 39940875](https://pubmed.ncbi.nlm.nih.gov/39940875/)) confirms the ordering: *"Pathogenic bacteria synthesize cysteine via a two-step enzymatic process using serine as the starting material. The first step is catalyzed by serine acetyltransferase, also known as CysE, and the second by"* OASS/CysK. Together these establish beyond doubt that CysK performs the terminal sulfur-incorporation step producing cysteine.

### F002 — CysK preferentially uses sulfide as the sulfur donor and forms the cysteine synthase complex (CSC) with CysE

Two functional properties distinguish CysK/OASS-A from its paralogue CysM/OASS-B: **sulfur-donor preference** and **complex formation**.

On sulfur-donor specificity, the most directly relevant experimental evidence comes from the **same genus**. In *Pseudomonas aeruginosa*, [PMID: 41676964](https://pubmed.ncbi.nlm.nih.gov/41676964/) showed that *"PaCysK exhibits optimal activity with sulfide, supporting its primary function in sulfide-dependent cysteine biosynthesis,"* whereas the paralogous CysM enzyme displays broader specificity that includes **thiosulfate**. Given the 70% identity between *P. putida* PP_4571 and characterized CysK enzymes (F006), the *P. putida* CysK is expected to share this **preference for free sulfide** as the physiological sulfur donor.

On complex formation, CysK is the isoform that assembles the **cysteine synthase complex (CSC)**. The same review states: *"Most bacteria encode two OASS isoforms: CysK, which forms the cysteine synthase complex (CSC) with CysE, and CysM, which typically acts independently"* ([PMID: 41676964](https://pubmed.ncbi.nlm.nih.gov/41676964/)). Structurally, the CSC is built by insertion of the **C-terminal tail of CysE** into the CysK active-site cleft. As described in [PMID: 27531961](https://pubmed.ncbi.nlm.nih.gov/27531961/): *"E. coli serine O-acetyltransferase uses a similar Gly-Asp-Gly-Ile motif to form the 'cysteine synthase' complex with CysK. The cysteine synthase complex is found throughout bacteria, protozoa, and plants."* This CSC is a **regulatory device**: complex formation modulates the activities of both enzymes and couples cysteine output to the availability of OAS and sulfide, providing feedback control over sulfur-amino-acid flux.

### F003 — CysK is cytoplasmic and moonlights to activate CDI toxins via its active-site cleft

**Subcellular localization:** As a soluble metabolic enzyme of the sulfate-assimilation/cysteine-biosynthesis pathway, CysK/OASS operates in the **bacterial cytoplasm**. UniProt Q88E95 records **no signal peptide and no membrane or secretion annotation**, consistent with a cytosolic housekeeping enzyme. This is where its substrates (OAS from CysE, and sulfide from the reductive sulfate-assimilation branch) are generated and where cysteine is consumed.

**Moonlighting function:** The very active-site cleft that binds CysE's C-terminal peptide is repurposed in a striking second activity. CysK is **required to activate the ribonuclease (tRNase/Ntox28) activity of contact-dependent growth inhibition CdiA-CT toxins**. [PMID: 27531961](https://pubmed.ncbi.nlm.nih.gov/27531961/) showed that *"CdiA-CT(EC536) inserts its C-terminal Gly-Tyr-Gly-Ile peptide tail into the active-site cleft of CysK to anchor the interaction"* — the same cleft used by CysE's Gly-Asp-Gly-Ile tail. Functionally, *"CysK significantly increases CdiA-CT(EC536) thermostability and is required for toxin interaction with tRNA substrates."* In other words, CysK acts as an **activating scaffold/chaperone**: it stabilizes the toxin fold and organizes its active site so it can cleave tRNA in target cells during interbacterial competition. A **single conserved C-terminal peptide/active-site-cleft interaction** thus underlies two very different biological roles — metabolic CSC assembly and toxin weaponization.

### F004 — The pathway is absent in humans and is a validated antibacterial drug target

The de novo cysteine biosynthesis pathway (**CysE + CysK/OASS**) is present in bacteria, protozoa, and plants but **absent in humans**, who obtain cysteine from the diet and via the transsulfuration pathway (which uses different enzymes). This makes the pathway attractive for selective antimicrobial intervention. [PMID: 41676964](https://pubmed.ncbi.nlm.nih.gov/41676964/) notes that *"This pathway is absent in humans, and its inhibition impairs microbial fitness, virulence, and antibiotic resistance, making its enzymes attractive antimicrobial targets."* A second review ([PMID: 38691891](https://pubmed.ncbi.nlm.nih.gov/38691891/)) independently confirms that *"The de novo cysteine biosynthesis pathway, one of the microbial metabolic pathways, plays a crucial role in pathogenicity and drug resistance. This pathway notably differs from that in humans."*

Reported inhibitor chemotypes exploit the conserved active-site cleft — the same one that binds CysE and CdiA peptides. These include **CymR-derived pentapeptides** with nanomolar potency ([PMID: 39705018](https://pubmed.ncbi.nlm.nih.gov/39705018/)), the fungal natural product **gliotoxin** ([PMID: 39940875](https://pubmed.ncbi.nlm.nih.gov/39940875/)), and small-molecule leads such as cyclopropane-carboxylic-acid derivatives ([PMID: 33513010](https://pubmed.ncbi.nlm.nih.gov/33513010/)) — most acting as **antibacterial adjuvants** that potentiate conventional antibiotics rather than as standalone bactericides. Although *P. putida* KT2440 is a non-pathogenic, biotechnologically important soil bacterium, these findings define the general biological importance and druggability of the enzyme family to which PP_4571 belongs.

### F005 — The PP_4571 sequence directly confirms OASS-A catalytic architecture, and KT2440 encodes a separate CysM paralogue

Direct inspection of the *P. putida* protein — not merely inference from homologs — corroborates the assignment. UniProt Q88E95 (324 aa, ~34.4 kDa) records the catalytic activity **O-acetyl-L-serine + hydrogen sulfide = L-cysteine + acetate** and pathway **"L-cysteine biosynthesis; L-cysteine from L-serine: step 2/2."** Sequence analysis identifies every fold-type II OASS hallmark in PP_4571:

| Structural element | Residue(s) in PP_4571 | Role |
|---|---|---|
| PLP-attachment lysine | **Lys44** (SVK motif; Y-S-V-**K44**-C-R-I) | Forms Schiff base (internal aldimine) with PLP cofactor |
| Glycine-rich PLP-phosphate loop | T71-S-G-**N74**-T-G | Anchors the PLP 5′-phosphate; Asn74 annotated binding residue |
| N-terminal substrate "asparagine loop" | T15-P-L-V | Positions O-acetylserine substrate |
| Additional binding residues | 179–183 (GTGGT); 274 | Substrate/cofactor coordination |

A UniProt proteome query of *P. putida* KT2440 returns **three** cysteine-synthase-family members, allowing clean orthologue discrimination: **cysK / Q88E95** (324 aa — this protein), **cysM / Q88MC0** (299 aa), and an additional, more distant OASS-family protein **Q88NU1** (300 aa). The presence of a distinct CysM confirms that PP_4571 is specifically the **CysK (OASS-A)** isoform, not a mis-annotated CysM.

### F006 — Reciprocal sequence-identity analysis unambiguously assigns PP_4571 to the CysK/OASS-A subfamily

Because CysK and CysM are close paralogues that can be conflated by annotation pipelines, an explicit, quantitative discrimination was performed. Global Needleman–Wunsch pairwise identities for PP_4571 (Q88E95, 324 aa) are:

| Comparison | % identity | Interpretation |
|---|---|---|
| PP_4571 vs *E. coli* CysK / OASS-A (P0ABK5) | **70.2%** | Best match → CysK subfamily |
| PP_4571 vs *Salmonella* Typhimurium CysK (P0A1E3) | **68.6%** | Confirms CysK subfamily |
| PP_4571 vs *E. coli* CysM / OASS-B (P16703) | 40.9% | Distant → not CysM |
| PP_4571 vs KT2440 CysM paralogue (Q88MC0) | 40.0% | Distant → different isoform |
| KT2440 CysM (Q88MC0) vs *E. coli* CysM | 66.1% | Reciprocal: Q88MC0 = CysM |
| KT2440 CysM (Q88MC0) vs *E. coli* CysK | 41.1% | Reciprocal confirmation |
| Third OASS-family protein (Q88NU1) vs PP_4571 | 26.4% | Distant relative |

The **reciprocal best-match pattern** is decisive: PP_4571 is ~70% identical to characterized CysK enzymes and only ~40% to CysM enzymes, while the KT2440 CysM paralogue shows the mirror-image relationship. This locks in Q88E95 as a bona fide **CysK/OASS-A orthologue** and Q88MC0 as the **CysM/OASS-B** counterpart, resolving any residual annotation ambiguity.

---

## Mechanistic Model / Interpretation

CysK sits at the terminal node of the **reductive sulfate-assimilation pathway**, the route by which *P. putida* converts environmental sulfate into organic reduced sulfur. Two converging inputs feed the enzyme:

```
   SULFUR BRANCH                          CARBON/NITROGEN BRANCH
   -------------                          -----------------------
   Sulfate (SO4^2-)                       L-Serine
      | Cys sulfate activation               | CysE (serine acetyltransferase)
      v   / reduction (CysNDC, CysH)         |   + acetyl-CoA
   Sulfite (SO3^2-)                          v
      | CysJI (sulfite reductase)        O-acetyl-L-serine (OAS)
      v                                       |
   Sulfide (H2S) ----------------+            |
                                 |            |
                                 v            v
                         +-----------------------------+
                         |   CysK  (PP_4571, OASS-A)   |  <-- CYTOPLASM
                         |   PLP / Lys44; fold-type II |
                         |   OAS + H2S -> L-Cys + OAc  |
                         +-----------------------------+
                                       |
                                       v
                                   L-CYSTEINE
                        (-> methionine, glutathione,
                         Fe-S clusters, CoA, thiamine, biotin)
```

**Regulatory layer — the cysteine synthase complex (CSC).** CysK and CysE physically associate. The C-terminal Gly-Asp-Gly-Ile tail of CysE docks into the CysK active-site cleft. Because this same cleft binds OAS, complex formation ties the two enzymes' activities together: when OAS is abundant it competes off CysE and frees CysK for catalysis, whereas low OAS/high sulfide favors the complexed, regulated state. The CSC thereby buffers the pathway against accumulation of the reactive intermediate OAS and coordinates carbon and sulfur flux into cysteine.

**A single cleft, three ligands.** The most elegant unifying insight is that CysK's active-site cleft is a **promiscuous C-terminal-peptide receptor**:

| Ligand C-terminal peptide | Partner | Outcome |
|---|---|---|
| Gly-**Asp**-Gly-Ile | CysE | Assembles CSC; metabolic regulation |
| Gly-**Tyr**-Gly-Ile | CdiA-CT toxin | Activates tRNase; interbacterial competition |
| (peptidomimetics) | Inhibitors (e.g., gliotoxin, CymR pentapeptides) | Block catalysis; antibacterial adjuvants |

This explains, in one structural framework, CysK's metabolic role, its moonlighting toxin-activation role, and its druggability — all governed by which peptide occupies the cleft.

**Localization and physiological role.** All of this occurs in the **cytoplasm**. CysK produces the cell's primary reduced-sulfur amino acid, cysteine, which is the sulfur source for methionine, glutathione (redox buffering), coenzyme A, thiamine, biotin, lipoic acid, and iron–sulfur cluster biogenesis. In a metabolically versatile soil organism like *P. putida* KT2440, robust de novo cysteine synthesis supports redox homeostasis and biosynthetic autonomy across variable environmental sulfur availability.

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports the findings |
|---|---|---|
| [27531961](https://pubmed.ncbi.nlm.nih.gov/27531961/) | *Unraveling the essential role of CysK in CDI toxin activation* | Primary structural/functional study: CysE Gly-Asp-Gly-Ile and CdiA-CT Gly-Tyr-Gly-Ile peptides both dock into CysK's active-site cleft; CysK stabilizes the toxin and is required for tRNA cleavage (F002, F003) |
| [41676964](https://pubmed.ncbi.nlm.nih.gov/41676964/) | *Distinct contributions of OASSs to cysteine biosynthesis in P. aeruginosa* | **Same-genus** biochemical characterization: CysK prefers sulfide, CysM broader (incl. thiosulfate); CysK forms CSC; pathway absent in humans (F002, F004) |
| [38965664](https://pubmed.ncbi.nlm.nih.gov/38965664/) | *Advancements in inhibitors of SAT and OASS* | Review establishing CysK=OASS, CysE=SAT as indispensable two-enzyme cysteine pathway (F001) |
| [39940875](https://pubmed.ncbi.nlm.nih.gov/39940875/) | *Gliotoxin as inhibitor of bacterial OASS* | Confirms two-step pathway ordering (CysE then OASS); identifies natural-product inhibitor (F001, F004) |
| [38691891](https://pubmed.ncbi.nlm.nih.gov/38691891/) | *Targeting the cysteine biosynthesis pathway in microorganisms* | Independent confirmation that pathway differs from humans; role in pathogenicity/resistance (F004) |
| [39705018](https://pubmed.ncbi.nlm.nih.gov/39705018/) | *CymR-derived pentapeptides as nanomolar OASS inhibitors* | Demonstrates druggability of the active-site cleft with peptidomimetics (F004) |
| [33513010](https://pubmed.ncbi.nlm.nih.gov/33513010/) | *Cyclopropane-carboxylic acid derivative targeting OASS* | Small-molecule adjuvant lead against the enzyme (F004) |
| [30675454](https://pubmed.ncbi.nlm.nih.gov/30675454/) | *Insights into multifaceted activities of CysK* | Review of CysK's multiple (moonlighting) activities (supports F003 framing) |

**Nature of the evidence.** The identity and catalytic assignment for PP_4571 rest on **direct annotation and sequence evidence** (UniProt Q88E95 catalytic reaction, Lys44 PLP site, InterPro domains) combined with **quantitative reciprocal orthology** (70% to *E. coli* CysK). Functional properties (sulfide preference, CSC formation, CDI-toxin activation) are supported by **primary experimental studies on close orthologues** — most importantly a same-genus *P. aeruginosa* enzyme, plus the well-studied *E. coli*/*Salmonella* enzymes. No experimental study on the KT2440 enzyme itself was identified; the assignment is nonetheless robust because CysK is a highly conserved housekeeping enzyme with a strongly diagnostic sequence signature.

---

## Limitations and Knowledge Gaps

1. **No direct biochemical characterization of the KT2440 enzyme.** Kinetic parameters (kcat, Km for OAS and sulfide), sulfur-donor specificity, and CSC affinity for *P. putida* PP_4571 have not been measured directly. Functional properties are inferred from orthologues (strongest: same-genus *P. aeruginosa*).
2. **No experimental structure of PP_4571.** Active-site residues (Lys44 etc.) are annotation- and homology-based; there is no crystal or cryo-EM structure of the KT2440 protein, and no AlphaFold-confidence analysis was performed in this investigation.
3. **CSC formation not experimentally verified in *P. putida*.** Physical association of PP_4571 with the KT2440 CysE has not been demonstrated directly; it is inferred from strong conservation of the CysK/CysE interface.
4. **Moonlighting role untested in *P. putida*.** Whether PP_4571 activates CDI toxins in KT2440 (or in *P. putida* interbacterial competition) is unknown; the CDI-activation data derive from *E. coli*.
5. **Roles of the two paralogues in vivo.** The physiological division of labor between CysK (Q88E95), CysM (Q88MC0), and the third OASS-family protein (Q88NU1) — e.g., under sulfide- vs. thiosulfate-rich or oxidative conditions — has not been dissected genetically in KT2440.
6. **Drug-target literature is pathogen-centric.** Inhibitor/adjuvant findings concern pathogens; *P. putida* is non-pathogenic, so therapeutic relevance is indirect (though the enzymology transfers).

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant enzymology.** Express and purify His-tagged PP_4571; confirm PLP incorporation (420 nm absorbance), and measure steady-state kinetics for OAS + sulfide, plus activity with thiosulfate, to test the predicted CysK sulfide preference relative to the CysM paralogue Q88MC0.
2. **CSC reconstitution.** Co-purify or perform pulldown/SPR/ITC of PP_4571 with KT2440 CysE (and with a CysE C-terminal Gly-Asp-Gly-Ile peptide) to confirm cysteine synthase complex formation and quantify affinity.
3. **Structure determination.** Solve a crystal or cryo-EM structure (apo, PLP-bound, and OAS/α-aminoacrylate intermediate), or at minimum analyze the AlphaFold model + PAE, to validate Lys44 and the phosphate-binding loop and to map the active-site cleft geometry.
4. **Genetics of the three-paralogue system.** Construct single and combinatorial deletions of *cysK* (PP_4571), *cysM* (Q88MC0), and PP-Q88NU1; assay growth on sulfate vs. thiosulfate vs. sulfide, and under oxidative stress, to define each isoform's physiological niche.
5. **Moonlighting test.** Determine whether PP_4571 activates a cognate or heterologous CdiA-CT toxin in vitro (thermostability shift, tRNase activation), probing conservation of the moonlighting function in *P. putida*.
6. **Inhibitor cross-reactivity.** Screen known OASS inhibitors (CymR pentapeptides, gliotoxin, cyclopropane-carboxylic acid derivatives) against purified PP_4571 to test whether the *P. putida* active-site cleft shares the druggable pharmacophore of pathogen orthologues.

---

## Conclusion

*cysK* / PP_4571 (UniProt Q88E95) encodes **O-acetylserine sulfhydrylase A (cysteine synthase A, EC 2.5.1.47)**, a soluble, cytoplasmic, homodimeric, PLP-dependent fold-type II enzyme (catalytic Lys44) that catalyzes the final committing step of de novo cysteine biosynthesis — **O-acetyl-L-serine + H₂S → L-cysteine + acetate** — with a preference for free sulfide as the sulfur donor. It assembles the regulatory cysteine synthase complex with serine acetyltransferase (CysE) via docking of CysE's C-terminal peptide into the CysK active-site cleft, and it moonlights as an essential activating scaffold for CDI ribonuclease toxins through the same cleft. This assignment is supported by direct UniProt catalytic annotation, diagnostic fold-type II active-site residues, and ~70% reciprocal sequence identity to the experimentally characterized *E. coli* and *Salmonella* CysK enzymes — cleanly distinguishing PP_4571 from the genome's separate CysM paralogue (Q88MC0).


## Artifacts

- [OpenScientist final report](cysK-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](cysK-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:38965664
2. PMID:39940875
3. PMID:41676964
4. PMID:27531961
5. PMID:38691891
6. PMID:39705018
7. PMID:33513010