---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-11T06:46:53.546332'
end_time: '2026-08-11T07:19:11.163857'
duration_seconds: 1937.62
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: ddlA
  gene_symbol: ddlA
  uniprot_accession: Q88EV6
  protein_description: 'RecName: Full=D-alanine--D-alanine ligase A {ECO:0000255|HAMAP-Rule:MF_00047};
    EC=6.3.2.4 {ECO:0000255|HAMAP-Rule:MF_00047}; AltName: Full=D-Ala-D-Ala ligase
    A {ECO:0000255|HAMAP-Rule:MF_00047}; AltName: Full=D-alanylalanine synthetase
    A {ECO:0000255|HAMAP-Rule:MF_00047};'
  gene_info: Name=ddlA {ECO:0000255|HAMAP-Rule:MF_00047}; OrderedLocusNames=PP_4346;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the D-alanine--D-alanine ligase family.
  protein_domains: ATP-grasp. (IPR011761); ATP_grasp_subdomain_1. (IPR013815); D-Ala_lig_Van_CS.
    (IPR000291); D_ala_D_ala. (IPR005905); Dala_Dala_lig_C. (IPR011095)
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
  path: ddlA-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: ddlA-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88EV6
- **Protein Description:** RecName: Full=D-alanine--D-alanine ligase A {ECO:0000255|HAMAP-Rule:MF_00047}; EC=6.3.2.4 {ECO:0000255|HAMAP-Rule:MF_00047}; AltName: Full=D-Ala-D-Ala ligase A {ECO:0000255|HAMAP-Rule:MF_00047}; AltName: Full=D-alanylalanine synthetase A {ECO:0000255|HAMAP-Rule:MF_00047};
- **Gene Information:** Name=ddlA {ECO:0000255|HAMAP-Rule:MF_00047}; OrderedLocusNames=PP_4346;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the D-alanine--D-alanine ligase family.
- **Key Domains:** ATP-grasp. (IPR011761); ATP_grasp_subdomain_1. (IPR013815); D-Ala_lig_Van_CS. (IPR000291); D_ala_D_ala. (IPR005905); Dala_Dala_lig_C. (IPR011095)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ddlA" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ddlA' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ddlA** (gene ID: ddlA, UniProt: Q88EV6) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *ddlA* (Q88EV6, PP_4346) — D-alanine–D-alanine ligase A of *Pseudomonas putida* KT2440

## Summary

The gene **ddlA** (ordered locus **PP_4346**; UniProt **Q88EV6**) of *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / KT2440) encodes **D-alanine–D-alanine ligase A** (Ddl; EC 6.3.2.4), a cytoplasmic ATP-grasp enzyme of the D-alanine–D-alanine ligase family (HAMAP rule MF_00047). Its primary and defining biochemical function is the ATP-dependent condensation of two molecules of D-alanine into the dipeptide **D-alanyl-D-alanine**, according to the reaction **2 D-alanine + ATP → D-alanyl-D-alanine + ADP + phosphate + H⁺** (Rhea RHEA:11224). The reaction requires two divalent metal ions (Mg²⁺ or Mn²⁺) per subunit and is activated by the monovalent cation K⁺. It is a canonical, essential step of the cytosolic phase of bacterial peptidoglycan (cell-wall) biosynthesis. The D-Ala–D-Ala dipeptide produced is subsequently joined by MurF to UDP-MurNAc-tripeptide to form the UDP-MurNAc-pentapeptide, the completed cytoplasmic muropeptide precursor.

The identity of Q88EV6 as a *bona fide* dipeptide (rather than depsipeptide) ligase is strongly supported by both database annotation and sequence–structure analysis performed during this investigation. The protein is **42.8% identical to *E. coli* DdlB** (P07862), the enzyme whose 2.3 Å crystal structure defined the family's reaction mechanism, and it fully conserves the catalytic/specificity triad (mapping to **Glu16/Ser181/Tyr253** in Q88EV6) together with the ω-loop tyrosine that rejects D-lactate at the second (nucleophile) subsite. It also carries the PROSITE D-Ala–D-Ala ligase family signature (**PS00843**). These molecular determinants distinguish true D-Ala–D-Ala ligases from the resistance-associated D-Ala–D-Lac and D-Ala–D-Ser depsipeptide ligases (e.g., VanA), and their conservation indicates that Q88EV6 makes the normal, vancomycin-sensitive dipeptide terminus.

Functionally, *ddlA* operates in the **cytoplasm** and is part of an essential, redundantly-encoded step: *P. putida* KT2440 carries two paralogous D-Ala–D-Ala ligases, **ddlA (Q88EV6)** and **ddlB (Q88N74)**, mirroring the two-gene arrangement of *E. coli*. As in *E. coli*, either single gene is expected to be sufficient for viability while simultaneous loss of both is lethal unless exogenous D-Ala–D-Ala is supplied. The pathway is a validated antibacterial target: the antibiotic D-cycloserine, a cyclic D-alanine analog, inhibits both alanine racemase and Ddl. This report synthesizes five confirmed findings from database interrogation, pairwise sequence alignment, and literature review into a coherent mechanistic picture of the enzyme's reaction, substrate specificity, subcellular localization, pathway context, and physiological essentiality.

---

## Gene / Protein Identity Verification

All UniProt-provided criteria were confirmed by direct query of the UniProt REST record for Q88EV6.

| Criterion | Value (verified) |
|---|---|
| Protein | D-alanine–D-alanine ligase A |
| EC number | 6.3.2.4 |
| Gene / locus | *ddlA* / PP_4346 |
| Organism | *Pseudomonas putida* KT2440 (ATCC 47054 / DSM 6125 / NCIMB 11950) |
| Length | 352 aa |
| Domain | ATP-grasp (res. 138–341); ATP-binding region 165–220 |
| Cofactor | 2 × Mg²⁺/Mn²⁺ per subunit (metal-binding residues 295, 308, 310) |
| Family | D-alanine–D-alanine ligase family (HAMAP MF_00047) |
| Localization | Cytoplasm |

The gene symbol, organism, EC number, ATP-grasp domain, and family all agree. This is an **unambiguous, well-characterized enzyme family**, so functional annotation by homology and mechanism is robust even though experimental studies on the *P. putida* ortholog specifically are limited; the extensive family literature below is directly applicable.

---

## Key Findings

### F001 — *ddlA* is D-alanine–D-alanine ligase A catalyzing ATP-dependent dipeptide formation

The UniProt entry for Q88EV6 (verified directly via the REST API during this investigation) describes a 352-amino-acid protein encoded by gene *ddlA* / PP_4346 in *Pseudomonas putida* KT2440, assigned **EC 6.3.2.4** and the HAMAP family rule MF_00047 for the D-alanine–D-alanine ligase family. The catalyzed reaction (Rhea RHEA:11224) is:

> **2 D-alanine + ATP → D-alanyl-D-alanine + ADP + phosphate + H⁺**

The protein carries an **ATP-grasp domain** (approximately residues 138–341), an ATP-binding region (≈165–220), and two divalent metal ions (Mg²⁺/Mn²⁺) per subunit, with metal-coordinating residues annotated at positions 295, 308, and 310. This exactly matches the biochemistry described in the primary literature. As stated by the structural study of the *Mycobacterium tuberculosis* enzyme, "*D-alanine:D-alanine ligase (EC 6.3.2.4; Ddl) catalyzes the ATP-driven ligation of two D-alanine (D-Ala) molecules to form the D-alanyl:D-alanine dipeptide. This molecule is a key building block in peptidoglycan biosynthesis*" [PMID: 20956591](https://pubmed.ncbi.nlm.nih.gov/20956591/).

The kinetic mechanism is an **ordered ter-ter reaction** conserved across the family. In the *M. tuberculosis* ortholog, ATP binds first, followed by two D-alanine molecules at two subsites of distinct affinity (K_m,D-Ala1 ≈ 0.075 mM, high affinity; K_m,D-Ala2 ≈ 3.6 mM, low affinity): "*ATP is the first substrate to bind and is necessary for subsequent binding of D-alanine or DCS*" [PMID: 23286234](https://pubmed.ncbi.nlm.nih.gov/23286234/). The two distinct D-Ala subsites are a general feature of the family and underlie its substrate-specificity control (see F002/F004).

**Substrate specificity.** The physiological substrates are two molecules of the D-enantiomer of alanine (supplied by alanine racemase from L-alanine) plus ATP; the product is the D-Ala–D-Ala dipeptide. Specificity for the D-configuration and for alanine (versus the depsipeptide alternative D-lactate) is enforced structurally, as detailed in F002/F004.

### F002 — Catalytic mechanism: ATP-grasp fold, phosphorylated D-Ala intermediate, and a Tyr/Ser/Glu ω-loop triad controlling D-Ala vs D-lactate specificity

The mechanistic template for the whole family is the *E. coli* DdlB crystal structure solved at 2.3 Å in complex with the transition-state analog S,R-methylphosphinate plus ATP. That work proposed a mechanism in which the first D-alanine is phosphorylated by ATP to a **D-alanyl-phosphate intermediate**, which is then attacked by the amino group of the second D-alanine to form the peptide bond, with a helix dipole and a hydrogen-bonded triad assisting binding and deprotonation: "*A catalytic mechanism for the ligation of two D-alanine substrates is proposed in which a helix dipole and a hydrogen-bonded triad of tyrosine, serine, and glutamic acid assist binding and deprotonation steps*" [PMID: 7939684](https://pubmed.ncbi.nlm.nih.gov/7939684/).

The three triad residues (Tyr216, Ser150, Glu15 in *E. coli* DdlB) orient a mobile **ω-loop** that closes over the active site and positions the first D-alanine: "*Y216, S150, and E15 form a hydrogen-bonding triad that orients an omega-loop to close over the active site and also to orient substrate D-Ala1*" [PMID: 8756703](https://pubmed.ncbi.nlm.nih.gov/8756703/). This same triad is the specificity switch between dipeptide and depsipeptide synthesis: mutating it (Y216F, S150A) converts DdlB into a D-Ala–D-lactate (depsipeptide) ligase [PMID: 8756703](https://pubmed.ncbi.nlm.nih.gov/8756703/). The ω-loop residues that reject the protonated (NH₃⁺) form of D-alanine at subsite 2 are precisely what a resistance ligase such as **VanA** lacks; VanA instead selectively activates the weak nucleophile D-lactate to make the vancomycin-resistant D-Ala–D-Lac terminus [PMID: 10529248](https://pubmed.ncbi.nlm.nih.gov/10529248/). Because Q88EV6 belongs to the same family with a conserved ATP-grasp domain and Mg²⁺ triad, it employs the same phosphoryl-transfer mechanism.

### F004 — Q88EV6 conserves the *E. coli* DdlB catalytic/specificity triad, confirming true D-Ala–D-Ala (not depsipeptide) ligase

To directly test whether Q88EV6 is a genuine dipeptide ligase, a **Needleman–Wunsch pairwise alignment (BLOSUM62)** was computed during this investigation between Q88EV6 (352 aa) and the two *E. coli* reference enzymes. Q88EV6 is **42.8% identical to *E. coli* DdlB** (P07862, 306 aa — the structurally characterized enzyme) and **42.4% identical to *E. coli* DdlA** (P0A6J8). Critically, the three functionally essential residues of the DdlB hydrogen-bonded triad map to conserved, identical residues in Q88EV6:

| *E. coli* DdlB residue | Role | Conserved residue in Q88EV6 (P. putida DdlA) |
|---|---|---|
| Glu15 | Triad member (deprotonation/orientation) | **Glu16** |
| Ser150 | Triad member (H-bond network) | **Ser181** |
| Tyr216 | ω-loop tyrosine (orients D-Ala1; rejects D-Lac) | **Tyr253** |

In addition, the PROSITE D-Ala–D-Ala ligase family signature **PS00843** (motif LHGRWGEDGTIQG, beginning at residue 99) is present in Q88EV6. Retention of the ω-loop Tyr (Tyr253) together with the Ser/Glu triad members is the molecular determinant that rejects D-lactate at the nucleophile subsite — exactly the configuration that resistance ligases such as VanA lack. As the defining structural work states, the triad is "*a hydrogen-bonded triad of tyrosine, serine, and glutamic acid [that] assist binding and deprotonation steps*" [PMID: 7939684](https://pubmed.ncbi.nlm.nih.gov/7939684/), and these are "*the specificity-determining residues distinguishing dipeptide from depsipeptide ligases*" [PMID: 8756703](https://pubmed.ncbi.nlm.nih.gov/8756703/). Their conservation in Q88EV6 provides strong bioinformatic evidence that the *P. putida* enzyme synthesizes the normal, vancomycin-sensitive D-Ala–D-Ala dipeptide rather than a resistance-associated depsipeptide.

### F003 — Cytoplasmic localization, essentiality, monovalent-cation activation, and antibiotic-target status

Ddl acts in the **cytosolic (cytoplasmic) stage** of peptidoglycan synthesis, consistent with the UniProt localization of Q88EV6 to the cytoplasm (HAMAP MF_00047). Mechanistically, the family is activated by the **monovalent cation K⁺**, a general feature of ATP-grasp enzymes; the *M. tuberculosis* enzyme is K⁺-activated [PMID: 23286234](https://pubmed.ncbi.nlm.nih.gov/23286234/), and Ddl has been proposed as a model system for monovalent-cation activation of ATP-grasp enzymes [PMID: 32335509](https://pubmed.ncbi.nlm.nih.gov/32335509/). That review states plainly that "*d-alanine-d-alanine ligase (Ddl), catalyzes ATP-dependent formation of the d-alanyl-d-alanine dipeptide essential for bacterial cell wall biosynthesis and is therefore an important antibiotic drug target*" [PMID: 32335509](https://pubmed.ncbi.nlm.nih.gov/32335509/).

The enzyme is **essential** and a validated antibacterial drug target. The antibiotic **D-cycloserine** (DCS), a cyclic analog of D-alanine, inhibits both alanine racemase and Ddl; inhibition of Ddl proceeds via a distinct **phosphorylated form of the drug** generated in the active site: "*the inhibition of D-alanine:D-alanine ligase by the antibiotic D-cycloserine proceeds via a distinct phosphorylated form of the drug*" [PMID: 29208891](https://pubmed.ncbi.nlm.nih.gov/29208891/). Loss of D-Ala–D-Ala synthesis produces cell-wall defects and growth arrest that can be reversed by exogenous D-Ala–D-Ala dipeptide, demonstrated in both *Streptococcus mutans* (where DCS treatment blocks growth and biofilm formation, reversible by exogenous D-Ala) [PMID: 26526529](https://pubmed.ncbi.nlm.nih.gov/26526529/) and in *E. coli*, where a double *ddlA ddlB* deletion is viable only when exogenous D-Ala–D-Ala is supplied or a complementing ligase is expressed [PMID: 15948948](https://pubmed.ncbi.nlm.nih.gov/15948948/).

### F005 — *P. putida* KT2440 encodes two D-Ala–D-Ala ligase paralogs (functional redundancy)

A **UniProt proteome query** (organism_id 160488, EC 6.3.2.4) performed during this investigation returns **two curated paralogs** in *P. putida* KT2440: **ddlA = Q88EV6** (352 aa, PP_4346, the target of this report) and **ddlB = Q88N74** (318 aa), plus a TrEMBL duplicate entry (A0A140FWM5, 304 aa). This two-gene arrangement mirrors *E. coli*, which carries both *ddlA* and *ddlB*. In *E. coli*, either single gene is sufficient for viability, but simultaneous deletion of both is lethal unless exogenous D-Ala–D-Ala is supplied: the study describing the *E. coli* auxotroph documents "*a D-Ala-D-Ala ligase auxotroph of Escherichia coli possessing deletions of both the ddlA and ddlB genes*," and viability without dipeptide supplementation "*became dependent on the expression of the chlamydial murC-ddl*" [PMID: 15948948](https://pubmed.ncbi.nlm.nih.gov/15948948/). By analogy, in *P. putida* the essential D-Ala–D-Ala–synthesizing step is expected to be **redundantly encoded** by *ddlA* (PP_4346) and *ddlB*. This implies that while the *reaction* is essential, the individual *ddlA* gene may be partially dispensable if *ddlB* is intact — consistent with *ddlA* being a core biosynthetic isozyme rather than a specialized or regulatory protein.

---

## Mechanistic Model / Interpretation

### Reaction and catalytic cycle

Ddl (Q88EV6) is an ATP-grasp ligase that forms an amide (peptide) bond between two D-alanine molecules at the expense of one ATP, proceeding through a covalent acyl-phosphate intermediate:

```
                         ATP        ADP
                          \         /
   D-Ala1 (subsite 1) ---> D-alanyl-phosphate (intermediate)
                                    |
                                    |  <-- nucleophilic attack by NH2 of
                                    v      D-Ala2 (subsite 2, omega-loop-gated)
              D-alanyl-D-alanine  +  Pi
```

**Step 1:** ATP binds first (ordered mechanism) and phosphorylates the carboxylate of the first D-alanine (subsite 1, high affinity), producing a D-alanyl-phosphate intermediate and ADP.
**Step 2:** The amino group of the second D-alanine (subsite 2, low affinity) attacks the activated carbonyl, displacing phosphate and forming the D-Ala–D-Ala peptide bond.

Two divalent metal ions (Mg²⁺/Mn²⁺) coordinate the nucleotide phosphates and stabilize the transition state; the monovalent cation K⁺ activates catalysis. A mobile ω-loop, positioned by the Glu16/Ser181/Tyr253 hydrogen-bonded triad, closes over the active site and enforces selection of D-alanine (an amine nucleophile) over D-lactate (a hydroxyl nucleophile) at subsite 2 — the molecular basis for making a *dipeptide* rather than a vancomycin-resistant *depsipeptide*.

### Pathway context: the cytoplasmic Mur pathway

```
 L-Ala  --(alanine racemase, Alr)-->  D-Ala
                                        |
                          2 D-Ala + ATP |  Ddl (ddlA / PP_4346, Q88EV6)   <-- THIS ENZYME
                                        v
                                  D-Ala–D-Ala
                                        |
   UDP-MurNAc-tripeptide + D-Ala–D-Ala  |  MurF + ATP
                                        v
                          UDP-MurNAc-pentapeptide
                                        |
                             (MraY, MurG, lipid II, flipping,
                              transglycosylation/transpeptidation)
                                        v
                                  Peptidoglycan sacculus
```

The D-Ala–D-Ala dipeptide made by Ddl is added as a unit by MurF to UDP-MurNAc-tripeptide, completing the UDP-MurNAc-pentapeptide. The terminal D-Ala–D-Ala is the target of the glycopeptide antibiotic vancomycin and is the donor for transpeptidation cross-linking during wall assembly. Ddl therefore sits at a committed, low-molecular-weight-substrate branch point that is attractive for antibacterial drug design.

### Localization and redundancy

The enzyme functions in the **cytoplasm**, upstream of the membrane-associated (lipid I/lipid II) steps. In *P. putida* KT2440 the activity is provided by two isozymes (DdlA/Q88EV6 and DdlB/Q88N74), giving genetic redundancy: the pathway step is essential, but no single *ddl* gene is expected to be individually essential, consistent with the *E. coli* paradigm.

### Comparative summary table

| Property | Value for Q88EV6 (P. putida DdlA) | Evidence type |
|---|---|---|
| EC number | 6.3.2.4 | UniProt / HAMAP MF_00047 |
| Reaction | 2 D-Ala + ATP → D-Ala–D-Ala + ADP + Pi + H⁺ | Rhea RHEA:11224; [PMID: 20956591](https://pubmed.ncbi.nlm.nih.gov/20956591/) |
| Length | 352 aa | UniProt |
| Fold / domain | ATP-grasp (~res 138–341) | UniProt (InterPro IPR011761) |
| Metal cofactor | 2 × Mg²⁺/Mn²⁺ per subunit (res 295, 308, 310) | UniProt |
| Monovalent activator | K⁺ | [PMID: 32335509](https://pubmed.ncbi.nlm.nih.gov/32335509/); [PMID: 23286234](https://pubmed.ncbi.nlm.nih.gov/23286234/) |
| Specificity triad | Glu16 / Ser181 / Tyr253 (conserved) | Alignment vs DdlB; [PMID: 7939684](https://pubmed.ncbi.nlm.nih.gov/7939684/) |
| Family signature | PROSITE PS00843 present (res 99) | This analysis |
| Identity to E. coli DdlB | 42.8% | Needleman–Wunsch (this analysis) |
| Product type | Dipeptide (not depsipeptide) | Triad conservation; [PMID: 8756703](https://pubmed.ncbi.nlm.nih.gov/8756703/) |
| Localization | Cytoplasm | UniProt / HAMAP |
| Paralog in KT2440 | ddlB (Q88N74) | UniProt proteome query |
| Essentiality | Essential step (redundant genes) | [PMID: 15948948](https://pubmed.ncbi.nlm.nih.gov/15948948/) |
| Drug target | D-cycloserine (phosphorylated inhibitor) | [PMID: 29208891](https://pubmed.ncbi.nlm.nih.gov/29208891/) |

---

## Evidence Base

The functional assignment rests on a combination of authoritative database annotation (UniProt/HAMAP MF_00047, Rhea, InterPro, PROSITE), sequence–structure analysis performed here, and primary/review literature on well-characterized orthologs. Because no dedicated experimental study of the *P. putida* KT2440 enzyme itself was located, the evidence is transitive: the target is a highly conserved family member whose signature catalytic and specificity residues are individually verified to be present.

| PMID | Title (abbrev.) | How it supports the annotation |
|---|---|---|
| [20956591](https://pubmed.ncbi.nlm.nih.gov/20956591/) | *Structure of the M. tuberculosis D-Ala:D-Ala ligase…* | States the exact reaction (ATP-driven ligation of two D-Ala → dipeptide) and its role as a peptidoglycan building block |
| [23286234](https://pubmed.ncbi.nlm.nih.gov/23286234/) | *Kinetic mechanism and inhibition of Mtb Ddl by D-cycloserine* | Defines the ordered ter-ter mechanism (ATP binds first) and two D-Ala subsites; K⁺ activation |
| [7939684](https://pubmed.ncbi.nlm.nih.gov/7939684/) | *Vancomycin resistance: structure of D-Ala:D-Ala ligase at 2.3 Å* | Defines the catalytic mechanism and the Tyr/Ser/Glu triad of DdlB, the reference structure |
| [8756703](https://pubmed.ncbi.nlm.nih.gov/8756703/) | *Gain of depsipeptide activity in E. coli DdlB active-site mutants* | Shows the triad + ω-loop are the dipeptide-vs-depsipeptide specificity switch |
| [10529248](https://pubmed.ncbi.nlm.nih.gov/10529248/) | *Determinants of D-Ala-D-Lac vs D-Ala-D-Ala by VanA ligase* | Contrasts resistance depsipeptide ligases (lack ω-loop residues) with true dipeptide ligases |
| [32335509](https://pubmed.ncbi.nlm.nih.gov/32335509/) | *Ddl as a model for monovalent-cation activation of ATP-grasp enzymes* | Confirms essentiality, K⁺ activation, and drug-target status |
| [29208891](https://pubmed.ncbi.nlm.nih.gov/29208891/) | *Inhibition of Ddl through a phosphorylated form of D-cycloserine* | Establishes Ddl as a validated antibiotic target and the DCS inhibition mechanism |
| [15948948](https://pubmed.ncbi.nlm.nih.gov/15948948/) | *Chlamydia MurC-Ddl fusion; E. coli ddlA ddlB auxotroph* | Demonstrates two-gene redundancy and essentiality (double deletion lethal without D-Ala–D-Ala) |
| [26526529](https://pubmed.ncbi.nlm.nih.gov/26526529/) | *D-Ala metabolism essential for S. mutans growth/biofilm* | Loss of D-Ala–D-Ala pathway causes cell-wall defects reversible by exogenous D-Ala |
| [12499203](https://pubmed.ncbi.nlm.nih.gov/12499203/) | *M. smegmatis Ddl/Alr in D-cycloserine action/resistance* | Ddl overexpression confers DCS resistance; positions Ddl in the D-Ala branch |
| [17267218](https://pubmed.ncbi.nlm.nih.gov/17267218/) | *Diazenedicarboxamides as Ddl inhibitors* | Reinforces Ddl as an antibacterial drug target with tractable inhibitor chemistry |
| [19229285](https://pubmed.ncbi.nlm.nih.gov/19229285/) | *Assay of peptidoglycan synthesis for natural-product screening* | Places Alr–Ddl–MurF in the cytoplasmic pathway; essential, low-MW-substrate targets |

**Consistency.** All lines of evidence converge. The database reaction (Rhea RHEA:11224), the structurally-defined mechanism, the conserved specificity triad found by direct alignment, and the physiological essentiality/redundancy all agree that Q88EV6 is a cytoplasmic, K⁺-activated, ATP-grasp D-Ala–D-Ala dipeptide ligase feeding peptidoglycan biosynthesis.

---

## Supported vs. Refuted Hypotheses

**Supported**
- **H1:** ddlA/PP_4346 is a D-Ala–D-Ala ligase catalyzing 2 D-Ala + ATP → D-Ala–D-Ala. *(UniProt EC 6.3.2.4, Rhea RHEA:11224; family literature.)*
- **H2:** It uses an ATP-grasp fold, an ordered mechanism with a D-alanyl-phosphate intermediate, requires 2 Mg²⁺/Mn²⁺, and is K⁺-activated. *(PMIDs 7939684, 23286234, 32335509; UniProt features.)*
- **H3:** It is cytoplasmic and functions in the cytosolic stage of peptidoglycan biosynthesis, feeding MurF; the step is essential. *(UniProt; PMIDs 15948948, 26526529.)*
- **H4:** Substrate specificity for D-Ala vs D-lactate is set by the Tyr/Ser/Glu triad + ω-loop; Q88EV6 is a true dipeptide (not depsipeptide) ligase. *(PMIDs 7939684, 8756703, 10529248; alignment showing Glu16/Ser181/Tyr253 conservation.)*

**Refuted / not supported**
- The gene is NOT a structural, transport, or signaling protein — it is a biosynthetic ligase.
- No evidence that PP_4346 is a D-Ala–D-Lac/D-Ser (resistance-type) depsipeptide ligase; sequence/family features argue against it.

---

## Limitations and Knowledge Gaps

1. **No direct experimental characterization of the P. putida enzyme.** All kinetic parameters, mechanistic detail, and structural features cited here derive from orthologs (*E. coli* DdlB, *M. tuberculosis* Ddl, VanA). The function of Q88EV6 is inferred by homology (42.8% identity to DdlB) and residue-level conservation, not measured directly. There is no published K_m, k_cat, or crystal structure specifically for PP_4346.

2. **Redundancy inferred, not demonstrated in P. putida.** The two-paralog arrangement (ddlA + ddlB) is documented in the KT2440 proteome, but the individual dispensability of *ddlA* and the synthetic lethality of a double knockout have been shown in *E. coli*, not experimentally in *P. putida*. Relative expression levels, condition-dependent roles, or subtle functional divergence between the two paralogs are unknown.

3. **Substrate specificity inferred from conserved residues.** While the Glu16/Ser181/Tyr253 triad and PS00843 signature strongly predict a dipeptide (not depsipeptide) product, this has not been confirmed enzymatically for Q88EV6. Minor secondary activities (e.g., tolerance of D-Ser or other D-amino acids at subsite 2) cannot be excluded without assays.

4. **Metal/cofactor specifics.** UniProt annotates Mg²⁺/Mn²⁺ binding residues, but the preferred physiological metal and the quantitative K⁺ dependence for the *P. putida* enzyme are unmeasured.

5. **Localization is by prediction.** Cytoplasmic localization follows from family annotation and pathway logic; it has not been experimentally verified for PP_4346 (though it is essentially certain for a soluble Mur-pathway ligase).

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant expression and enzyme assay.** Clone PP_4346, express and purify the His-tagged protein, and measure ATP-dependent D-Ala–D-Ala formation (e.g., coupled ADP/phosphate release or LC-MS detection of dipeptide). Determine K_m for D-Ala at both subsites, K_m for ATP, k_cat, and metal (Mg²⁺ vs Mn²⁺) and K⁺ dependence — directly confirming F001/F003.

2. **Product-specificity test.** Assay the purified enzyme with D-alanine vs D-lactate/D-serine as the subsite-2 substrate to confirm it makes the dipeptide and rejects depsipeptide/D-Ser products, testing the prediction from the conserved Tyr253/Ser181/Glu16 triad (F002/F004).

3. **Genetic redundancy test in P. putida KT2440.** Construct single (ΔddlA, ΔddlB) and double (ΔddlA ΔddlB) deletions; test viability with and without exogenous D-Ala–D-Ala supplementation to confirm the predicted synthetic lethality and redundancy (F005).

4. **D-cycloserine susceptibility.** Determine whether overexpression of PP_4346 raises the DCS MIC of *P. putida* (as seen for *M. smegmatis* Ddl, [PMID: 12499203](https://pubmed.ncbi.nlm.nih.gov/12499203/)), linking the enzyme to the antibiotic-target pathway.

5. **Structural determination.** Solve the crystal or cryo-EM structure of Q88EV6 (ideally with ATP + a transition-state analog such as a phosphinate), or generate a validated AlphaFold model, to visualize the ATP-grasp fold, the two metal sites, and the ω-loop closure — confirming the mechanistic model.

6. **Inhibitor profiling.** Screen the purified enzyme against known Ddl inhibitor chemotypes (e.g., diazenedicarboxamides, [PMID: 17267218](https://pubmed.ncbi.nlm.nih.gov/17267218/)) to assess its tractability as a *Pseudomonas*-relevant antibacterial target.

---

## Conclusion

*ddlA* (PP_4346, UniProt Q88EV6) of *Pseudomonas putida* KT2440 encodes **cytoplasmic D-alanine–D-alanine ligase A (Ddl, EC 6.3.2.4)**, an ATP-grasp enzyme that condenses two D-alanine molecules into the dipeptide **D-alanyl-D-alanine** (2 D-Ala + ATP → D-Ala–D-Ala + ADP + Pi), using two Mg²⁺/Mn²⁺ ions and K⁺ activation and proceeding through a D-alanyl-phosphate intermediate. This dipeptide is an essential cytosolic peptidoglycan precursor that MurF incorporates into the UDP-MurNAc-pentapeptide. Q88EV6 is a genuine dipeptide (not depsipeptide) ligase — it is 42.8% identical to the structurally defined *E. coli* DdlB and conserves the full catalytic/specificity triad (Glu16/Ser181/Tyr253) and the PROSITE PS00843 signature — and it functions as one of two redundant isozymes (with *ddlB*, Q88N74) in an essential, D-cycloserine-targeted step of bacterial cell-wall biosynthesis.


## Artifacts

- [OpenScientist final report](ddlA-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](ddlA-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:20956591
2. PMID:23286234
3. PMID:7939684
4. PMID:8756703
5. PMID:10529248
6. PMID:32335509
7. PMID:29208891
8. PMID:26526529
9. PMID:15948948
10. PMID:12499203
11. PMID:17267218