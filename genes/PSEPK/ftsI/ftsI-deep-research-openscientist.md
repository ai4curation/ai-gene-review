---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T22:58:12.164957'
end_time: '2026-08-31T23:10:21.370845'
duration_seconds: 729.21
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: ftsI
  gene_symbol: ftsI
  uniprot_accession: Q88N82
  protein_description: 'RecName: Full=Peptidoglycan D,D-transpeptidase FtsI {ECO:0000256|HAMAP-Rule:MF_02080};
    EC=3.4.16.4 {ECO:0000256|HAMAP-Rule:MF_02080}; AltName: Full=Penicillin-binding
    protein 3 {ECO:0000256|HAMAP-Rule:MF_02080}; Short=PBP-3 {ECO:0000256|HAMAP-Rule:MF_02080};'
  gene_info: Name=ftsI {ECO:0000256|HAMAP-Rule:MF_02080, ECO:0000313|EMBL:AAN66954.1};
    OrderedLocusNames=PP_1331 {ECO:0000313|EMBL:AAN66954.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the transpeptidase family. FtsI subfamily.
  protein_domains: Beta-lactam/transpept. (IPR050515); Beta-lactam/transpept-like.
    (IPR012338); FtsI_transpept. (IPR037532); PBP_dimer. (IPR005311); PBP_dimer_sf.
    (IPR036138)
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
citation_count: 13
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: ftsI-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: ftsI-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88N82
- **Protein Description:** RecName: Full=Peptidoglycan D,D-transpeptidase FtsI {ECO:0000256|HAMAP-Rule:MF_02080}; EC=3.4.16.4 {ECO:0000256|HAMAP-Rule:MF_02080}; AltName: Full=Penicillin-binding protein 3 {ECO:0000256|HAMAP-Rule:MF_02080}; Short=PBP-3 {ECO:0000256|HAMAP-Rule:MF_02080};
- **Gene Information:** Name=ftsI {ECO:0000256|HAMAP-Rule:MF_02080, ECO:0000313|EMBL:AAN66954.1}; OrderedLocusNames=PP_1331 {ECO:0000313|EMBL:AAN66954.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the transpeptidase family. FtsI subfamily.
- **Key Domains:** Beta-lactam/transpept. (IPR050515); Beta-lactam/transpept-like. (IPR012338); FtsI_transpept. (IPR037532); PBP_dimer. (IPR005311); PBP_dimer_sf. (IPR036138)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ftsI" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ftsI' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ftsI** (gene ID: ftsI, UniProt: Q88N82) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: FtsI (Penicillin-Binding Protein 3 / PBP-3), *Pseudomonas putida* KT2440

**UniProt:** Q88N82 | **Gene:** *ftsI* (PP_1331) | **Organism:** *Pseudomonas putida* KT2440 (ATCC 47054 / DSM 6125 / NCIMB 11950) | **EC:** 3.4.16.4 | **Family:** Transpeptidase family, FtsI subfamily (HAMAP MF_02080)

---

## Summary

**FtsI (PBP-3) encoded by PP_1331 in *Pseudomonas putida* KT2440 is the cell-division-specific D,D-transpeptidase that cross-links septal peptidoglycan.** It is a monofunctional, class B, high-molecular-weight penicillin-binding protein (PBP). Its primary catalytic function is to form 4→3 (D,D) peptide cross-links between adjacent peptidoglycan (PG) stem peptides — transferring the terminal D-alanine of a pentapeptide donor onto the meso-diaminopimelate residue of an acceptor stem peptide — thereby covalently stitching together the newly synthesized glycan strands that build the division septum during cytokinesis. Catalysis proceeds through an active-site serine nucleophile (Ser292 in the Q88N82 sequence) that forms a transient acyl-enzyme intermediate, the defining mechanism of the serine-based D,D-transpeptidase (penicillin-binding protein) enzyme class.

The identity of PP_1331 as a bona fide *ftsI* ortholog is exceptionally secure. The protein carries every diagnostic feature of the FtsI/PBP3 subfamily on its own sequence: a single N-terminal transmembrane anchor, a non-catalytic "pedestal"/dimerization module, and a C-terminal transpeptidase module containing the three conserved catalytic motifs (SxxK with the nucleophilic Ser292, an SxN loop, and the KTG/KSG β3-strand box). It is ~48–51% identical to the extensively characterized *Escherichia coli* PBP3 across its full length, and PP_1331 sits in the canonical, syntenic *dcw*/*mra* (division-and-cell-wall) gene cluster flanked by *ftsL*, *murE*, *murF* and *mraY* — the same genomic context as *ftsI* in nearly all rod-shaped Gram-negative bacteria. This orthology and synteny, together with the intact catalytic machinery, allow confident transfer of the deep mechanistic knowledge from *E. coli*, *Pseudomonas aeruginosa*, *Caulobacter crescentus* and other model systems to the *P. putida* protein.

Functionally, FtsI operates in the **periplasm at the mid-cell division septum**, tethered to the inner membrane by a single N-terminal transmembrane helix with only a short (~23-residue) cytoplasmic tail. It acts as the obligate cross-linking partner of the SEDS-family glycosyltransferase **FtsW**, which polymerizes Lipid II into glycan strands that FtsI then cross-links. The FtsW–FtsI pair is recruited late to the FtsZ ring, is controlled by the **FtsQLB (FtsBLQ)** regulatory subcomplex, and is switched on by the activator **FtsN**. Because its active-site serine is covalently acylated (and thus irreversibly inhibited) by division-targeting β-lactams such as aztreonam, ceftazidime and cephalexin, FtsI is a clinically validated antibiotic target; its inhibition blocks septation and produces filamentous, non-dividing cells, and mutations in *ftsI* are a recognized β-lactam resistance mechanism.

---

## Key Findings

### F001 — FtsI is the class B PBP / D,D-transpeptidase that cross-links septal peptidoglycan

The core function of the gene product is settled by both database annotation and a large body of experimental literature on FtsI/PBP3 orthologs. UniProt Q88N82 is annotated as peptidoglycan D,D-transpeptidase FtsI / penicillin-binding protein 3, EC 3.4.16.4, in the transpeptidase family (FtsI subfamily), under the curated HAMAP rule MF_02080. FtsI is a **monofunctional class B PBP**: unlike bifunctional class A PBPs, it has no glycosyltransferase activity of its own; its enzymatic contribution is confined to transpeptidation.

The enzyme catalyzes the **cross-linking step of peptidoglycan maturation** specifically in the division septum. In *E. coli*, "Penicillin-binding protein 3 (PBP3; also called FtsI) is a transpeptidase that catalyzes cross-linking of the peptidoglycan cell wall in the division septum" ([PMID: 12813065](https://pubmed.ncbi.nlm.nih.gov/12813065/)), and it is "a central component of the divisome, catalyzing cross-linking of the cell wall peptidoglycan during cell division" ([PMID: 24875494](https://pubmed.ncbi.nlm.nih.gov/24875494/)). The reaction mechanism and substrate are defined by the PBP enzyme class: "D,D-transpeptidases of the penicillin-binding protein (PBP) family are active-site serine enzymes that use pentapeptide precursors and are the main or exclusive cross-linking enzymes in nearly all bacteria" ([PMID: 25006233](https://pubmed.ncbi.nlm.nih.gov/25006233/)). Concretely, FtsI forms 4→3 cross-links: it accepts a pentapeptide donor stem, cleaves the D-Ala⁴–D-Ala⁵ bond to form an acyl-enzyme, and transfers the carbonyl of D-Ala⁴ onto the side-chain amine of meso-diaminopimelate (position 3) of a neighboring acceptor peptide, releasing the terminal D-Ala. This is the covalent bond that gives the septal wall its mechanical integrity.

### F002 — Bitopic inner-membrane topology with a periplasmic catalytic domain and a two-module architecture

FtsI is a **bitopic (single-pass) inner-membrane protein** with its business end in the periplasm. The crystal structure of *E. coli* PBP3 (residues 57–577) revealed the classic two-module architecture of high-molecular-weight class B PBPs: "the two modules of high molecular weight class B PBPs, a carboxy terminal module exhibiting transpeptidase activity and an amino terminal module of unknown function" ([PMID: 24875494](https://pubmed.ncbi.nlm.nih.gov/24875494/)). The N-terminal (pedestal/anchor-associated) module is non-catalytic and is thought to mediate protein–protein interactions and dimerization; the C-terminal module carries the transpeptidase active site.

The membrane topology places nearly the entire protein outside the cytoplasm: "PBP3 is mainly periplasmic, with a 23 residues cytoplasmic tail and a single transmembrane helix" ([PMID: 24875494](https://pubmed.ncbi.nlm.nih.gov/24875494/)). Precise domain mapping in *E. coli* defines the arrangement as "a short intracellular M1-R23 peptide fused to a F24-L39 membrane anchor that is linked via a G40-S70 peptide to an R71-I236 noncatalytic module itself linked to a D237-V577 catalytic penicillin-binding module" ([PMID: 15342580](https://pubmed.ncbi.nlm.nih.gov/15342580/)). The *P. putida* protein shares this organization, carrying the InterPro PBP_dimer (IPR005311) and FtsI_transpept (IPR037532) signatures. This topology is functionally essential: the catalytic domain must reside in the periplasm where the peptidoglycan substrate is located, while the membrane anchor couples the enzyme to the membrane-embedded divisome machinery.

### F003 — FtsI is the cognate transpeptidase of the SEDS glycosyltransferase FtsW, regulated by FtsQLB and activated by FtsN

FtsI does not act alone; it forms a functional module with the septal glycan polymerase **FtsW**. FtsW is a SEDS (Shape, Elongation, Division, Sporulation)-family glycosyltransferase that polymerizes Lipid II into nascent glycan strands, and it depends on FtsI to cross-link those strands: "SEDS family peptidoglycan (PG) glycosyltransferases, RodA and FtsW, require their cognate transpeptidases PBP2 and FtsI (class B penicillin binding proteins) to synthesize PG along the cell cylinder and at the septum, respectively" ([PMID: 33857142](https://pubmed.ncbi.nlm.nih.gov/33857142/)). FtsW builds the glycan backbone; FtsI cross-links it — together they constitute the core septal PG synthase.

This synthase is tightly regulated. The essential FtsWI enzymes "are controlled by the regulatory FtsBLQ subcomplex and the activator FtsN" ([PMID: 35408901](https://pubmed.ncbi.nlm.nih.gov/35408901/)). Genetic epistasis places FtsI as a signal-relay node in the activation pathway: "the FtsN-triggered activation signal goes from FtsQLB to FtsI to FtsW" ([PMID: 33857142](https://pubmed.ncbi.nlm.nih.gov/33857142/)). Thus FtsI is both an enzyme and a conformational transducer: the activation signal that unleashes septal wall synthesis passes through FtsI to reach the FtsW polymerase. FtsI is recruited late in divisome assembly and is itself required to recruit downstream division proteins — "FtsI (also called PBP3) of Escherichia coli is a transpeptidase required for synthesis of peptidoglycan in the division septum and is one of several proteins that localize to the septal ring" ([PMID: 14702319](https://pubmed.ncbi.nlm.nih.gov/14702319/)), and its presence is a prerequisite for FtsN arrival.

### F004 — Septal (mid-cell) localization is FtsZ-ring-dependent and requires both the membrane anchor and the catalytic site

FtsI is targeted specifically to the incipient division site. In *Caulobacter crescentus*, "the recruitment of PBP3 to the FtsZ ring is progressive and initiated very early on, shortly after FtsZ ring formation and well before cell constriction starts" ([PMID: 18786147](https://pubmed.ncbi.nlm.nih.gov/18786147/)) — i.e., localization is driven by, and downstream of, the FtsZ cytoskeletal ring. Two determinants govern this targeting. First, the N-terminal membrane region carries the primary localization signal: in *E. coli*, "the first 56 amino acid residues of PBP3 containing the membrane anchor and the G40-E56 peptide contain the structural determinants required to target the protein to the cell division site" ([PMID: 15342580](https://pubmed.ncbi.nlm.nih.gov/15342580/)); substitutions at R23, L39 or Q46 abolish septal localization ([PMID: 14702319](https://pubmed.ncbi.nlm.nih.gov/14702319/)). Second, the catalytic domain contributes: in *Caulobacter*, "localization of PBP3 at both midcell and pole appears multifactorial, primarily requiring the catalytic site of PBP3" ([PMID: 18786147](https://pubmed.ncbi.nlm.nih.gov/18786147/)). Together these place the enzyme precisely where and when septal wall synthesis must occur.

### F005 — FtsI is the lethal target of division-specific β-lactams; inhibition blocks septation and causes filamentation

As a penicillin-binding protein, FtsI's active-site serine is covalently acylated by β-lactam antibiotics that structurally mimic the D-Ala–D-Ala terminus of its substrate. In growing *E. coli* cells, researchers "assayed acylation of PBP3 with three beta-lactams (cephalexin, aztreonam, and piperacillin)" ([PMID: 12813065](https://pubmed.ncbi.nlm.nih.gov/12813065/)) — these are the classic "division-specific" β-lactams whose primary target is PBP3. Acylation traps the enzyme as a dead-end acyl-enzyme, blocking cross-linking; the cell continues to elongate but cannot septate, producing long non-dividing filaments.

The most directly relevant organism is *Pseudomonas aeruginosa*, the closest well-studied relative of *P. putida*. Overproduction of PBP3 there specifically raised resistance to PBP3-targeted agents, and "PBP3 has to achieve a certain level of saturation, with beta-lactams targeted to this protein, to result in cell inhibition or death" ([PMID: 9145889](https://pubmed.ncbi.nlm.nih.gov/9145889/)) — establishing that killing by these drugs is mechanistically coupled to inactivation of PBP3. Clinically, *ftsI*/PBP3 alterations are a documented resistance mechanism: "resistance to aztreonam-avibactam among clinical isolates of Escherichia coli is primarily mediated by altered penicillin-binding protein 3" ([PMID: 38925228](https://pubmed.ncbi.nlm.nih.gov/38925228/)). These observations confirm both the enzyme's essentiality and its identity as a validated antibacterial target.

### F006 — The Q88N82 sequence itself carries an intact FtsI/PBP3 catalytic architecture

Direct analysis of the 582-residue *P. putida* FtsI sequence (Q88N82) confirms every diagnostic feature on the actual target rather than relying solely on homology transfer. The protein carries a single N-terminal transmembrane helix (~residues 12–32), a PBP dimerization ("pedestal") domain (~55–205), and a PBP transpeptidase domain (~245–545), followed by a C-terminal disordered Pro-rich/low-complexity tail (~556–582). The catalytic nucleophile is the annotated active-site **Ser292**, which forms the acyl-ester intermediate and sits in the canonical class-B-PBP **SxxK** motif (S292-T-V-K295, in the sequence context …VFEPGSTVKPI…). The two additional conserved transpeptidase motifs are present: an **SxN**-type loop and the **KTG/KSG** β3-strand box (KTG at ~253, KSG at ~483). This mirrors the *E. coli* PBP3 catalytic serine (Ser307 in an SVVK motif) and satisfies the FtsI subfamily HAMAP rule MF_02080. The presence of all three catalytic motifs — the nucleophile, the general base/acid loop, and the substrate-positioning KTG box — indicates a catalytically competent enzyme, not a degenerate pseudo-transpeptidase.

### F007 — PP_1331 lies in the conserved *dcw*/*mra* cluster and is ~48–51% identical to *E. coli* PBP3

Genomic context clinches orthology and pathway placement. PP_1331 sits within the canonical *dcw* (*mra*) division-and-cell-wall cluster in the conserved gene order:

```
PP_1329  mraW/rsmH   (rRNA methyltransferase)
PP_1330  ftsL        (cell division protein)
PP_1331  ftsI        ← TARGET (PBP3 / D,D-transpeptidase)
PP_1332  murE        (UDP-MurNAc-tripeptide:meso-DAP ligase)
PP_1333  murF        (D-Ala-D-Ala-adding ligase)
PP_1334  mraY        (phospho-MurNAc-pentapeptide transferase)
```

This is precisely the arrangement of the *mra*/*dcw* cluster in *E. coli* and nearly all rod-shaped Gram-negative bacteria, where *ftsI* is flanked by division genes and peptidoglycan-precursor biosynthesis genes. Pairwise global alignment of Q88N82 (582 aa) against *E. coli* K-12 PBP3/FtsI (P0AD68, 588 aa) yields ~47–51% amino-acid identity full-length (296 identical positions; ~51% over the shorter sequence). Roughly 50% identity across ~580 residues, combined with identical domain order and identical genomic synteny, places PP_1331 unambiguously as the septal transpeptidase ortholog and justifies transferring the *E. coli*/*Pseudomonas* mechanistic model.

---

## Mechanistic Model / Interpretation

FtsI is best understood as the **cross-linking half of the core septal peptidoglycan synthase**, embedded in a regulated, membrane-spanning molecular machine (the divisome). The following model synthesizes the findings.

**1. Assembly and localization.** Cell division begins with polymerization of the tubulin homolog FtsZ into a ring (the Z-ring) at mid-cell. FtsZ recruits early membrane proteins, and later the septal PG synthesis module — FtsW, FtsI, and the FtsQLB regulators — arrives (F004). FtsI's N-terminal membrane anchor (first ~56 residues) provides the primary targeting signal, with a secondary contribution from its catalytic domain (F004). Localization is progressive and precedes visible constriction.

**2. The enzymatic pair.** FtsW (SEDS glycosyltransferase) polymerizes the lipid-linked precursor Lipid II into glycan strands; FtsI (class B PBP transpeptidase) cross-links those strands (F003). They are obligate cognate partners — the polymerase cannot build a load-bearing wall without the transpeptidase, and vice versa.

```
   CYTOPLASM
      │  Lipid II (from MurF → MraY → MurG pathway; note murE/murF/mraY are
      │            co-clustered with ftsI in the dcw operon, F007)
      │  (flipped across membrane by MurJ)
 ─────┼──────────────────────────  INNER MEMBRANE
      │        FtsW ── FtsI (TM anchors)
   PERIPLASM   │        │
              glycan   4→3 cross-link
              strand   (D-Ala⁴ → meso-DAP³)
              polymer.  via Ser292 acyl-enzyme
                 └────► MATURE SEPTAL PEPTIDOGLYCAN
```

**3. Catalytic chemistry (F001, F006).** FtsI's transpeptidase domain uses the active-site Ser292 as a nucleophile. Ser292 attacks the carbonyl of D-Ala⁴ in a pentapeptide donor stem, expelling the terminal D-Ala⁵ and forming a covalent acyl-enzyme intermediate. The side-chain amine of meso-diaminopimelate (position 3) on an acceptor stem then resolves the intermediate, forming the D-Ala⁴→meso-DAP³ isopeptide (4→3) cross-link and regenerating free enzyme. The SxxK, SxN, and KTG motifs cooperatively position the substrate, activate the nucleophile, and stabilize the transition state.

**4. Regulation (F003).** The synthase is kept "off" until the cell commits to division. The FtsQLB (FtsBLQ) subcomplex holds FtsWI in check; the arrival and action of the activator FtsN triggers a conformational relay — **FtsN → FtsQLB → FtsI → FtsW** — that switches on processive glycan polymerization and cross-linking. FtsI is thus not only an enzyme but a signal transducer within this relay.

**5. Pharmacology and essentiality (F005).** Because the D-Ala–D-Ala terminus of the donor is mimicked by the β-lactam ring, division-specific β-lactams (aztreonam, ceftazidime, cephalexin, piperacillin) acylate Ser292 and lock the enzyme in a dead acyl-enzyme state. This halts septal cross-linking; elongation continues, producing filamentous cells that eventually lyse. In *Pseudomonas*, killing correlates with the degree of PBP3 saturation, and *ftsI* mutations that lower β-lactam affinity confer resistance.

**Comparison of FtsI orthologs (evidence transfer to *P. putida*):**

| Feature | *E. coli* PBP3 (P0AD68) | *P. putida* FtsI (Q88N82) | Evidence |
|---|---|---|---|
| Length | 588 aa | 582 aa | F007 |
| Full-length identity to *E. coli* | — | ~48–51% | F007 |
| Catalytic Ser (SxxK) | Ser307 (SVVK) | Ser292 (STVK) | F006 |
| Membrane topology | 1 TM, ~23-aa cyto tail | 1 TM (~12–32), short cyto tail | F002, F006 |
| Two-module architecture | pedestal + TPase | pedestal (55–205) + TPase (245–545) | F002, F006 |
| *dcw*/*mra* synteny | ftsL–ftsI–murE–murF–mraY | PP_1330–1331–1332–1333–1334 | F007 |
| Cognate polymerase | FtsW | FtsW (predicted) | F003 |
| β-lactam target | Yes (aztreonam etc.) | Yes (inferred; *P. aeruginosa* data) | F005 |

The convergence of intact catalytic motifs, conserved architecture, ~50% identity, and perfect operon synteny makes the functional assignment for *P. putida* FtsI as secure as such assignments get by homology.

---

## Evidence Base

| PMID | Title (abbrev.) | Supports | Nature |
|---|---|---|---|
| [12813065](https://pubmed.ncbi.nlm.nih.gov/12813065/) | *Probing the catalytic activity of a cell division-specific transpeptidase in vivo with β-lactams* | F001, F005 | Primary, in vivo (*E. coli*) |
| [24875494](https://pubmed.ncbi.nlm.nih.gov/24875494/) | *Crystal structure of PBP3 from Escherichia coli* | F001, F002 | Primary, structural |
| [15342580](https://pubmed.ncbi.nlm.nih.gov/15342580/) | *Structural determinants required to target PBP3 to the septum* | F002, F004 | Primary, genetics |
| [14702319](https://pubmed.ncbi.nlm.nih.gov/14702319/) | *Genetic analysis of FtsI: septal localization and FtsN recruitment* | F003, F004 | Primary, genetics |
| [18786147](https://pubmed.ncbi.nlm.nih.gov/18786147/) | *Localization of PBP3 in Caulobacter is dynamic and relies on the TPase domain* | F004 | Primary, cell biology |
| [33857142](https://pubmed.ncbi.nlm.nih.gov/33857142/) | *Genetic analysis of the FtsWI complex: conserved activation of SEDS-bPBP* | F003 | Primary, genetics |
| [35408901](https://pubmed.ncbi.nlm.nih.gov/35408901/) | *An updated model of the divisome* | F003 | Review |
| [25006233](https://pubmed.ncbi.nlm.nih.gov/25006233/) | *STP-mediated control of the L,D-transpeptidase pathway in E. faecium* | F001 | Primary (mechanism of PBP class) |
| [9145889](https://pubmed.ncbi.nlm.nih.gov/9145889/) | *Susceptibility to β-lactams of P. aeruginosa overproducing PBP3* | F005 | Primary (*Pseudomonas*) |
| [38925228](https://pubmed.ncbi.nlm.nih.gov/38925228/) | *Aztreonam-avibactam resistance mediated by altered PBP3* | F005 | Primary, clinical |
| [35274942](https://pubmed.ncbi.nlm.nih.gov/35274942/) | *The Bacterial Cell Wall: from Lipid II flipping to polymerization* | F003 (context) | Review |

**How the evidence supports the conclusions.** The catalytic identity (F001) rests on a converging set: structural work on *E. coli* PBP3 ([PMID: 24875494](https://pubmed.ncbi.nlm.nih.gov/24875494/)), in vivo β-lactam probing that directly demonstrates transpeptidase activity ([PMID: 12813065](https://pubmed.ncbi.nlm.nih.gov/12813065/)), and the general PBP-class mechanism ([PMID: 25006233](https://pubmed.ncbi.nlm.nih.gov/25006233/)). The FtsW–FtsI cognate-pair model and its regulation (F003) are established by genetic dissection of the FtsWI complex ([PMID: 33857142](https://pubmed.ncbi.nlm.nih.gov/33857142/)) and synthesized in a recent divisome review ([PMID: 35408901](https://pubmed.ncbi.nlm.nih.gov/35408901/)). Localization (F004) is supported by *Caulobacter* live-cell imaging ([PMID: 18786147](https://pubmed.ncbi.nlm.nih.gov/18786147/)) and *E. coli* targeting genetics ([PMID: 15342580](https://pubmed.ncbi.nlm.nih.gov/15342580/); [PMID: 14702319](https://pubmed.ncbi.nlm.nih.gov/14702319/)). The pharmacology and essentiality (F005) are anchored by *Pseudomonas* data ([PMID: 9145889](https://pubmed.ncbi.nlm.nih.gov/9145889/)) — the closest relative with direct evidence — and clinical resistance ([PMID: 38925228](https://pubmed.ncbi.nlm.nih.gov/38925228/)).

**Important caveat on redundancy.** The literature also documents that PBP3 function is not universally identical across bacteria. *Salmonella* encodes a pathogen-specific PBP3 paralogue (PBP3ₛₐₗ) that can promote division independently ([PMID: 39233506](https://pubmed.ncbi.nlm.nih.gov/39233506/)), and *Clostridioides difficile* dispenses with functional FtsW/FtsI orthologs entirely, using a class A PBP for division ([PMID: 41118402](https://pubmed.ncbi.nlm.nih.gov/41118402/)). These exceptions do not apply to *P. putida* — a canonical Gram-negative γ-proteobacterium with a standard *dcw* cluster (F007) — but they underscore that the FtsI model is a strong default, not an inviolable rule, and that direct *P. putida* validation would remove residual uncertainty.

---

## Limitations and Knowledge Gaps

1. **No direct experimental characterization in *P. putida*.** All mechanistic conclusions for Q88N82 are inferred from homology (~50% identity to *E. coli*), conserved catalytic motifs, and operon synteny. No published study has purified *P. putida* FtsI, measured its transpeptidase kinetics, deleted/depleted PP_1331, or imaged its localization. The assignment is high-confidence but computational/comparative, not directly demonstrated in the target organism.

2. **Substrate stem-peptide details assumed.** The 4→3 D-Ala→meso-DAP cross-link is the standard for Gram-negative γ-proteobacteria and is highly likely for *P. putida*, but the exact stem-peptide composition and any L,D-transpeptidase (3→3) contribution in *P. putida* have not been verified here.

3. **Cognate FtsW partner not directly confirmed in *P. putida*.** The FtsW–FtsI pairing is inferred from universal divisome architecture; the specific *P. putida* FtsW gene and a demonstrated physical/genetic interaction with PP_1331 were not established.

4. **Regulatory relay (FtsN→FtsQLB→FtsI→FtsW) is transferred from *E. coli*.** While the *dcw* cluster and *ftsL* are present, the full complement and behavior of FtsQ/FtsB/FtsN in *P. putida* were not individually verified.

5. **Quantitative β-lactam affinity unknown.** *P. putida* FtsI's specific acylation kinetics and MIC contributions for particular β-lactams were inferred from *P. aeruginosa*; species-specific differences in drug affinity are plausible.

6. **C-terminal tail function.** The disordered Pro-rich C-terminal tail (~556–582) has no assigned function; in some orthologs such regions mediate interactions or localization, but this was not investigated.

---

## Proposed Follow-up Experiments / Actions

1. **Conditional depletion / essentiality test.** Use a CRISPRi or inducible-degron system in *P. putida* KT2440 to knock down PP_1331 and confirm the predicted phenotype: blocked septation, filamentation, and eventual lysis. (CRISPRi tooling for *P. putida* exists — cf. [PMID: 39163848](https://pubmed.ncbi.nlm.nih.gov/39163848/).)

2. **In vitro transpeptidase assay.** Express and purify the periplasmic domain of Q88N82 and assay D,D-transpeptidase / cross-linking activity on native-like peptidoglycan precursors (e.g., a continuous spectrophotometric transpeptidation assay), confirming Ser292 dependence with an S292A mutant.

3. **β-lactam binding (Bocillin-FL / acylation).** Measure covalent labeling of purified FtsI by fluorescent penicillin (Bocillin-FL) and determine acylation rates for aztreonam, ceftazidime, and cephalexin to validate PBP3-targeted pharmacology in *P. putida*.

4. **Localization imaging.** Construct a functional fluorescent fusion (e.g., mNeonGreen-FtsI) and confirm FtsZ-ring-dependent mid-cell recruitment and its dependence on the N-terminal anchor and catalytic site, paralleling the *Caulobacter*/*E. coli* results.

5. **Cognate-partner confirmation.** Identify the *P. putida* FtsW ortholog and test the FtsW–FtsI genetic/physical interaction (bacterial two-hybrid, co-purification, or in vivo cross-linking).

6. **Peptidoglycan chemotype analysis.** Perform muropeptide (HPLC/MS) analysis of *P. putida* sacculi ± FtsI depletion to quantify 4→3 vs 3→3 cross-links and directly attribute septal cross-linking to FtsI.

7. **Resistance-mutation mapping.** Sequence *ftsI* in β-lactam-resistant *P. putida* derivatives to test whether target-site mutations (analogous to *E. coli* PBP3 inserts) modulate susceptibility, informing antibiotic strategy.

---

## Conclusion

*Pseudomonas putida* KT2440 FtsI (PBP-3; Q88N82; PP_1331) is the **essential, inner-membrane-anchored, class B penicillin-binding protein that serves as the D,D-transpeptidase of the cell-division machinery.** Using pentapeptide precursors, it forms 4→3 cross-links between adjacent peptidoglycan stem peptides (donor D-Ala → acceptor meso-diaminopimelate) via its active-site Ser292, building and stabilizing the septal wall during cytokinesis. It functions in the **periplasm at the mid-cell septum** as the cognate cross-linking partner of the SEDS glycan polymerase **FtsW**, within a divisome assembled on the FtsZ ring and regulated by **FtsQLB** and the activator **FtsN**. Its active-site serine is the lethal target of division-specific β-lactams, and its inhibition blocks septation and causes filamentation. These conclusions rest on unusually strong comparative evidence — an intact catalytic architecture on the target sequence itself, ~50% identity to the deeply characterized *E. coli* PBP3, and perfect *dcw*/*mra* operon synteny — though direct experimental validation in *P. putida* remains a worthwhile next step.


## Artifacts

- [OpenScientist final report](ftsI-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](ftsI-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:12813065
2. PMID:24875494
3. PMID:25006233
4. PMID:15342580
5. PMID:33857142
6. PMID:35408901
7. PMID:14702319
8. PMID:18786147
9. PMID:9145889
10. PMID:38925228
11. PMID:39233506
12. PMID:41118402
13. PMID:39163848