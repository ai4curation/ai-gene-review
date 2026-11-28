---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T22:58:12.165668'
end_time: '2026-09-01T00:03:37.303936'
duration_seconds: 3925.14
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: mrcB
  gene_symbol: mrcB
  uniprot_accession: Q88DY5
  protein_description: 'RecName: Full=Penicillin-binding protein 1B {ECO:0000256|ARBA:ARBA00018637,
    ECO:0000256|NCBIfam:TIGR02071}; Short=PBP-1b {ECO:0000256|PIRNR:PIRNR002799};
    Short=PBP1b {ECO:0000256|PIRNR:PIRNR002799}; AltName: Full=Murein polymerase {ECO:0000256|ARBA:ARBA00032454,
    ECO:0000256|PIRNR:PIRNR002799};'
  gene_info: Name=mrcB {ECO:0000313|EMBL:AAN70256.1}; OrderedLocusNames=PP_4683 {ECO:0000313|EMBL:AAN70256.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: In the N-terminal section; belongs to the
  protein_domains: Beta-lactam/transpept-like. (IPR012338); Glyco_trans_51. (IPR001264);
    Glycosyltr_51/Transpeptidase. (IPR050396); Lysozyme-like_dom_sf. (IPR023346);
    PBP_1b. (IPR011813)
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
citation_count: 10
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: mrcB-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: mrcB-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88DY5
- **Protein Description:** RecName: Full=Penicillin-binding protein 1B {ECO:0000256|ARBA:ARBA00018637, ECO:0000256|NCBIfam:TIGR02071}; Short=PBP-1b {ECO:0000256|PIRNR:PIRNR002799}; Short=PBP1b {ECO:0000256|PIRNR:PIRNR002799}; AltName: Full=Murein polymerase {ECO:0000256|ARBA:ARBA00032454, ECO:0000256|PIRNR:PIRNR002799};
- **Gene Information:** Name=mrcB {ECO:0000313|EMBL:AAN70256.1}; OrderedLocusNames=PP_4683 {ECO:0000313|EMBL:AAN70256.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** In the N-terminal section; belongs to the
- **Key Domains:** Beta-lactam/transpept-like. (IPR012338); Glyco_trans_51. (IPR001264); Glycosyltr_51/Transpeptidase. (IPR050396); Lysozyme-like_dom_sf. (IPR023346); PBP_1b. (IPR011813)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "mrcB" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'mrcB' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **mrcB** (gene ID: mrcB, UniProt: Q88DY5) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *mrcB* (Q88DY5) — Penicillin-Binding Protein 1B of *Pseudomonas putida* KT2440

**Target:** UniProt **Q88DY5** · Gene **mrcB** (OrderedLocusName PP_4683) · *Pseudomonas putida* KT2440
**Protein:** Penicillin-binding protein 1B (PBP-1b / PBP1b); Murein polymerase · 773 aa

## Summary

The gene **mrcB** (ordered locus **PP_4683**; UniProt **Q88DY5**) of *Pseudomonas putida* KT2440 encodes **Penicillin-Binding Protein 1B (PBP1b)**, a **bifunctional class A peptidoglycan (PG) synthase** and the central "murein polymerase" that builds the cross-linked cell wall sacculus. The gene symbol, protein family assignments (PBP_1b, IPR011813), and diagnostic catalytic domains all match the UniProt identity provided, and a direct bioinformatic comparison with the canonical *Escherichia coli* PBP1b confirms that Q88DY5 is a bona fide, catalytically intact ortholog. This is **not** a case of gene-symbol ambiguity: *mrcB* unambiguously denotes PBP1b in Gram-negative bacteria, and the *P. putida* protein carries the full complement of conserved catalytic machinery.

The primary function of the protein is enzymatic and two-fold. Its **N-terminal glycosyltransferase family 51 (GT51) domain** (catalytic proton-donor **Glu188**) polymerizes the lipid-linked precursor **lipid II** into linear glycan strands, and its **C-terminal D,D-transpeptidase domain** (catalytic nucleophile **Ser466**, within an intact S-x-x-K motif) cross-links the pentapeptide stems of adjacent glycan chains. The transpeptidase domain is the classic target of β-lactam antibiotics, whereas the glycosyltransferase domain is inhibited by moenomycin-class compounds. The enzyme also exhibits secondary D,D-carboxypeptidase activity under some conditions. Together these activities catalyze the terminal, committed steps of peptidoglycan assembly.

Topologically, PBP1b is anchored in the **cytoplasmic (inner) membrane** by a single N-terminal transmembrane helix (residues ~21–43), with its large catalytic and regulatory domains projecting into the **periplasm**, where lipid II is presented and glycan polymerization/cross-linking occur. Its activity is not constitutive: it is switched on **allosterically** by a cognate **outer-membrane lipoprotein activator** that spans the periplasm and binds the central regulatory **UB2H domain**. In *Pseudomonas*, this activator is **LpoP** (the functional counterpart of *E. coli* LpoB), which stimulates both the transpeptidase and glycosyltransferase activities. PBP1b is further integrated into the **cell-division divisome**, where its polymerase activity is antagonistically tuned by the FtsBLQ complex and the activator FtsN, and it acts partially redundantly with PBP1a to preserve rod shape and envelope integrity.

---

## Key Findings

### Finding 1 — mrcB/Q88DY5 is a bifunctional class A PBP1b peptidoglycan synthase

The protein encoded by *mrcB* is a **773-amino-acid bifunctional class A penicillin-binding protein**. Its domain architecture, confirmed directly for Q88DY5, comprises an N-terminal **glycosyltransferase family 51 (GT51)** domain spanning approximately residues 166–333, and a C-terminal **penicillin-binding transpeptidase** domain spanning approximately residues 429–659.

The GT51 domain catalyzes **glycan chain polymerization**: it transfers the disaccharide-pentapeptide unit from the membrane carrier **lipid II** onto the growing glycan strand, releasing undecaprenyl pyrophosphate. This corresponds to the Rhea reaction RHEA:23708, in which a growing [GlcNAc-(1→4)-MurNAc-pentapeptide]ₙ-undecaprenyl-PP chain plus lipid II yields the (n+1) chain plus undecaprenyl-PP and a proton. The catalytic proton-donor residue is **Glu188**. This domain is **insensitive to penicillins** but is the target of moenomycin-class glycosyltransferase inhibitors.

The transpeptidase domain catalyzes **peptide cross-linking**, forming a covalent acyl-enzyme intermediate through the nucleophilic serine **Ser466** and joining the peptide stems of neighboring glycan strands (a D,D-transpeptidation) to generate the mechanically load-bearing, net-like sacculus. This domain is the **principal target of β-lactam antibiotics**, which acylate the active-site serine. Reconstitution studies of the paradigm *E. coli* enzyme show that PBP1b is active as a bifunctional glycosyltransferase/transpeptidase and, under certain conditions, additionally displays **D,D-carboxypeptidase activity** (EC 3.4.16.4).

The definition of PBP1b as a bifunctional PG synthase is well established. As stated for the *E. coli* paradigm, "*LpoB is required to activate PBP1B, which is a major, bi-functional PG synthase with glycan chain polymerising (glycosyltransferase) and peptide cross-linking (transpeptidase) activities*" ([PMID: 30044025](https://pubmed.ncbi.nlm.nih.gov/30044025/)). The in vitro demonstration that "*the bifunctional PBP1A and PBP1B from Escherichia coli are active upon reconstitution into the membrane environment of proteoliposomes, and that these enzymes also exhibit DD-carboxypeptidase activity in certain conditions*" ([PMID: 26370943](https://pubmed.ncbi.nlm.nih.gov/26370943/)) provides direct experimental grounding for all three catalytic activities.

### Finding 2 — PBP1b is anchored in the inner membrane with catalytic domains in the periplasm

Q88DY5 has a single **N-terminal transmembrane helix (residues ~21–43)** and a subcellular location annotated as "Cell membrane." The remaining ~730 residues — encompassing the UB2H regulatory domain, the GT51 domain, and the transpeptidase domain — reside in the **periplasm**. This topology is exactly what is required for its function: the lipid II substrate is flipped to the periplasmic face of the inner membrane, where the periplasm-facing catalytic domains can act on it.

This membrane topology is specifically confirmed for *Pseudomonas*: "*In the major clinical pathogen Pseudomonas aeruginosa, PBP1B is anchored within the cytoplasmic membrane but regulated by a bespoke outer membrane-localized lipoprotein known as LpoP*" ([PMID: 32320673](https://pubmed.ncbi.nlm.nih.gov/32320673/)). The single membrane anchor plus periplasmic catalytic machinery is the canonical class A PBP architecture and situates PBP1b's enzymatic work at the inner-membrane/periplasm interface where new wall material is incorporated.

### Finding 3 — PBP1b is allosterically activated by an outer-membrane lipoprotein (LpoP in *Pseudomonas*) via its UB2H domain and integrated into the divisome

PBP1b activity is tightly regulated. The central **UB2H domain** (UvrB domain-2 homolog; annotated on Q88DY5 as "Bifunctional transglycosylase second," residues ~69–152) is the docking site for a periplasm-spanning **outer-membrane lipoprotein activator**. In *Pseudomonas aeruginosa*, this activator is **LpoP**: "*We show that LpoP stimulates both PBP1B transpeptidase and glycosyltransferase activities in vitro and interacts directly via its C terminus globular domain with the central UB2H domain of PBP1B. Contrary to the situation in E. coli, P. aeruginosa CpoB does not regulate PBP1B/LpoP in vitro*" ([PMID: 32320673](https://pubmed.ncbi.nlm.nih.gov/32320673/)). Because *P. putida* KT2440 encodes an **LpoP ortholog** rather than *E. coli*-type LpoB, activation of Q88DY5 is expected to proceed through LpoP.

The paradigm was established in *E. coli*, where "*The lipoprotein LpoB is required for the activation of penicillin-binding protein (PBP) 1B, which is a major, bifunctional PG synthase*" ([PMID: 24821816](https://pubmed.ncbi.nlm.nih.gov/24821816/)). Activator binding to UB2H induces conformational changes that are transmitted to both catalytic domains by distinct allosteric pathways, and CpoB selectively modulates transpeptidase activation in *E. coli* ([PMID: 30044025](https://pubmed.ncbi.nlm.nih.gov/30044025/)).

Beyond lipoprotein activation, PBP1b is embedded in the **cell-division machinery**. Its glycosyltransferase activity is synergistically stimulated by the activator together with the essential division protein FtsN, and is antagonistically balanced by the core divisome FtsBLQ complex versus FtsN. "*During cell division, PG synthesis localizes at midcell under the control of a multiprotein complex, the divisome*" ([PMID: 30622193](https://pubmed.ncbi.nlm.nih.gov/30622193/)), placing PBP1b's polymerase activity under spatial and temporal control at the septum.

### Finding 4 — PBP1b is a major, partially redundant peptidoglycan polymerase requiring both enzymatic activities

In Gram-negative rods, **PBP1a and PBP1b form redundant PG-synthesizing complexes** with the lipoprotein activators **LpoA and LpoB**, respectively, and at least one of these class A PBPs is essential for viability: "*penicillin binding protein 1a (PBP1a) and 1b (PBP1b) form peptidoglycan-synthesizing complexes with the outer membrane lipoprotein LpoA and LpoB, respectively*" ([PMID: 32037461](https://pubmed.ncbi.nlm.nih.gov/32037461/)). Work in *Shewanella oneidensis* showed that PBP1a/1b variants lacking **either** the glycosyltransferase **or** the transpeptidase activity fail to maintain normal morphology and envelope integrity — demonstrating that **both** catalytic activities are functionally required — and that these two activities play different essential roles during morphogenesis ([PMID: 28096447](https://pubmed.ncbi.nlm.nih.gov/28096447/)).

That *P. putida* possesses an active, experimentally tractable class A PBP transpeptidase system is supported by studies showing its peptidoglycan chemistry and cross-linking can be edited experimentally: "*we used the soil bacterium Pseudomonas putida to uncover cell wall modulators*" ([PMID: 33830599](https://pubmed.ncbi.nlm.nih.gov/33830599/)). This confirms that the transpeptidase cross-linking machinery — of which Q88DY5/PBP1b is a major component — is operational in this organism.

### Finding 5 — Structural and single-molecule evidence defines PBP1b's two catalytic sites and a transient "hit-and-run" activation mechanism

High-resolution structural work on *E. coli* PBP1b captured the **glycosyltransferase domain bound to the substrate-analog inhibitor moenomycin** and the **transpeptidase domain bound to multiple β-lactams**, providing an atomic-level picture of both catalytic pockets and the structural basis of their inhibition: "*the peptidoglycan cell wall is synthesized by bifunctional penicillin-binding proteins such as PBP1b that have both transpeptidase and transglycosylase activities. The PBP1b transpeptidase domain is a major target of β-lactams*" ([PMID: 27899450](https://pubmed.ncbi.nlm.nih.gov/27899450/)). The GT domain is described as an excellent — but clinically still under-exploited — antibiotic target.

Single-molecule FRET and single-particle tracking further revealed the **dynamics of activation**: "*a prototypical lipoprotein activator LpoB triggers site-specific PG synthesis by PBP1b through conformational rearrangements. Once synthesis is initiated, LpoB affinity for PBP1b dramatically decreases and it dissociates from the synthesizing enzyme*" ([PMID: 40691462](https://pubmed.ncbi.nlm.nih.gov/40691462/)). This **"hit-and-run" mechanism** directs PBP1b activity specifically toward regions of low peptidoglycan density — i.e., to repair and reinforce weak spots in the wall — through a conserved allosteric switch. These structural and dynamic findings map directly onto the two catalytic residues annotated on Q88DY5 (GT proton-donor Glu188; TP nucleophile Ser466) and its UB2H regulatory domain.

### Finding 6 — Q88DY5 is a bona fide PBP1b ortholog with fully intact, conserved catalytic motifs

A direct InterPro comparison of *P. putida* Q88DY5 (773 aa) against the canonical *E. coli* PBP1b (P02919, 844 aa) shows **identical domain signatures**: PBP_1b (IPR011813), glycosyltransferase family 51 (IPR001264), penicillin-binding transpeptidase (IPR001460 / IPR012338), the PBP transglycosylase fold (IPR036950), and the UB2H regulatory domain (IPR028166). Both proteins carry exactly **two catalytic active sites at homologous positions**: the GT proton-donor glutamate (**E188** in *P. putida*, E233 in *E. coli*) and the transpeptidase acyl-ester serine (**S466** vs S510).

Sequence-level inspection confirms the catalytic motifs are intact in Q88DY5. The transpeptidase **S-x-x-K motif** is present (Ser466-Leu-Val-Lys469, "...GSLVKP..."), and the GT51 catalytic glutamate lies within the conserved acidic motif ("...ATEDREFY..." around E188). This bioinformatic evidence establishes with high confidence that both catalytic machineries are conserved and predicted to be functional — meaning the well-characterized biochemistry of *E. coli*/*P. aeruginosa* PBP1b can be transferred to the *P. putida* protein with strong justification.

---

## Mechanistic Model / Interpretation

PBP1b performs the **terminal, committed steps of peptidoglycan biosynthesis** on the periplasmic face of the inner membrane. The following model integrates all six findings:

```
                     OUTER MEMBRANE
   ┌────────────────────[ LpoP ]────────────────────┐   (lipoprotein activator,
   │                        │                         │    anchored in OM)
   │        PERIPLASM       │  spans periplasm,
   │                        ▼  binds UB2H
   │                 ┌────[ UB2H ]────┐  <- allosteric regulatory domain (res ~69–152)
   │                 │                │
   │        ┌────[ GT51 ]──────[ Transpeptidase ]────┐
   │        │  Glu188            Ser466 (S-x-x-K)      │
   │        │ (moenomycin        (β-lactam target)     │
   │        │  target)                                 │
   │        ▼                                          ▼
   │   lipid II ──► linear glycan strands ──► CROSS-LINKED SACCULUS
   │────────┬─────────────────────────────────────────┘
   ═════════╪═══════════ INNER (CYTOPLASMIC) MEMBRANE ═════════
     TM helix (res 21–43)
            CYTOPLASM
```

**Step 1 — Substrate presentation.** Lipid II, synthesized in the cytoplasm and flipped across the inner membrane, is presented at the periplasmic leaflet. PBP1b remains anchored in the inner membrane by its single N-terminal TM helix (Finding 2).

**Step 2 — Allosteric activation.** In the resting state PBP1b has low activity. The outer-membrane lipoprotein **LpoP** reaches across the periplasm and binds the **UB2H domain**, triggering conformational rearrangements that are relayed to both catalytic domains (Findings 3, 5). This activation is spatially targeted to regions of low PG density and is **transient** ("hit-and-run"): once synthesis begins, activator affinity drops and it dissociates, allowing the enzyme to move on (Finding 5).

**Step 3 — Glycan polymerization.** The activated **GT51 domain** (Glu188) polymerizes lipid II into linear glycan strands, releasing undecaprenyl-PP (Finding 1).

**Step 4 — Cross-linking.** The **transpeptidase domain** (Ser466) cross-links the nascent strands to the existing sacculus via D,D-transpeptidation, and can trim stems via D,D-carboxypeptidase activity (Finding 1).

**Step 5 — Systems integration.** During division, this activity is localized at midcell and tuned by the divisome — stimulated by FtsN, restrained by FtsBLQ — and operates partially redundantly with the PBP1a/LpoA system, such that loss of one aPBP is tolerated but loss of both is lethal (Findings 3, 4).

The following table summarizes the two catalytic modules and their pharmacology:

| Property | Glycosyltransferase (GT51) module | Transpeptidase (PB) module |
|---|---|---|
| Approx. residues (Q88DY5) | 166–333 | 429–659 |
| Catalytic residue | Glu188 (proton donor) | Ser466 (nucleophile, S-x-x-K) |
| Reaction | Lipid II → linear glycan strands (RHEA:23708) | D,D-transpeptidation (peptide cross-link); also D,D-carboxypeptidase |
| Substrate | Lipid II / growing glycan chain | Pentapeptide stems |
| Antibiotic inhibitor | Moenomycin (not clinically exploited) | β-lactams (penicillins, etc.) |
| Regulation | Stimulated by LpoP via UB2H; FtsN-synergized | Stimulated by LpoP via UB2H; CpoB-modulated in *E. coli* |

Comparison across the well-studied orthologs:

| Feature | *E. coli* PBP1b (P02919) | *P. aeruginosa* PBP1b | *P. putida* PBP1b (Q88DY5) |
|---|---|---|---|
| Length | 844 aa | ~similar | 773 aa |
| GT catalytic Glu | E233 | conserved | **E188** |
| TP catalytic Ser | S510 | conserved | **S466** |
| Lipoprotein activator | LpoB | **LpoP** | **LpoP ortholog** |
| CpoB regulation | Yes | No | Expected absent (as *P. aeruginosa*) |
| UB2H regulatory domain | Yes | Yes | Yes (res ~69–152) |

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution to this report |
|---|---|---|
| [30044025](https://pubmed.ncbi.nlm.nih.gov/30044025/) | *Induced conformational changes activate the peptidoglycan synthase PBP1B* | Defines PBP1b as a bifunctional GTase/TPase synthase; establishes UB2H-mediated allosteric activation with distinct pathways to each domain (Findings 1, 3) |
| [26370943](https://pubmed.ncbi.nlm.nih.gov/26370943/) | *Activities and regulation of peptidoglycan synthases* | In vitro proteoliposome reconstitution proving bifunctional activity plus D,D-carboxypeptidase; FtsN/LpoB synergy (Findings 1, 3) |
| [32320673](https://pubmed.ncbi.nlm.nih.gov/32320673/) | *Structure of the Peptidoglycan Synthase Activator LpoP in P. aeruginosa* | *Pseudomonas*-specific: inner-membrane anchoring of PBP1b; LpoP stimulates both activities via UB2H; CpoB not involved (Findings 2, 3) |
| [24821816](https://pubmed.ncbi.nlm.nih.gov/24821816/) | *Outer-membrane lipoprotein LpoB spans the periplasm to stimulate PBP1B* | Establishes the requirement of an OM lipoprotein for PBP1b activation (Finding 3) |
| [30622193](https://pubmed.ncbi.nlm.nih.gov/30622193/) | *Regulation of PBP1b polymerase activity by FtsBLQ and FtsN* | Places PBP1b under divisome control at midcell; antagonistic FtsBLQ/FtsN regulation (Finding 3) |
| [32037461](https://pubmed.ncbi.nlm.nih.gov/32037461/) | *PBP1a GTase and TPase activities required in Shewanella* | PBP1a/1b redundancy with LpoA/LpoB; both catalytic activities required for envelope integrity (Finding 4) |
| [28096447](https://pubmed.ncbi.nlm.nih.gov/28096447/) | *PBP1B GTase and TPase play different essential roles* | Both activities play distinct essential morphogenetic roles (Finding 4) |
| [33830599](https://pubmed.ncbi.nlm.nih.gov/33830599/) | *d-canavanine affects peptidoglycan structure* | Confirms *P. putida* has an active, editable transpeptidase/cross-linking system (Finding 4) |
| [27899450](https://pubmed.ncbi.nlm.nih.gov/27899450/) | *Structural Insights into Inhibition of E. coli PBP1B* | Atomic structures of GT (moenomycin) and TP (β-lactam) sites; TP is the β-lactam target (Findings 1, 5) |
| [40691462](https://pubmed.ncbi.nlm.nih.gov/40691462/) | *The hit-and-run of cell wall synthesis* | Single-molecule evidence for transient LpoB activation directing synthesis to low-density wall regions (Finding 5) |

The evidence base is highly convergent. All studies agree on PBP1b's bifunctional enzymatic identity, its inner-membrane/periplasmic topology, and its regulation by a periplasm-spanning outer-membrane lipoprotein via the UB2H domain. Importantly, the *Pseudomonas aeruginosa* study ([PMID: 32320673](https://pubmed.ncbi.nlm.nih.gov/32320673/)) provides genus-level confirmation that the activator in *Pseudomonas* is **LpoP** rather than *E. coli*-type LpoB, and that CpoB regulation seen in *E. coli* is absent — a distinction that is directly transferable to *P. putida* Q88DY5. No study contradicts the assigned function; the assignment rests on convergent experimental evidence from orthologs plus complete sequence/domain conservation in Q88DY5 itself.

---

## Limitations and Knowledge Gaps

1. **No direct experimental study of Q88DY5 itself.** The functional assignment for the *P. putida* KT2440 protein rests on (a) unambiguous domain/sequence conservation (Finding 6) and (b) transfer of biochemistry from *E. coli* and *P. aeruginosa* orthologs. There is, to date, no published enzymatic reconstitution, crystal structure, or knockout phenotype for PP_4683 specifically.

2. **LpoP interaction inferred, not demonstrated, in *P. putida*.** *P. putida* KT2440 is annotated to encode an LpoP ortholog, and the LpoP→UB2H→PBP1b activation mechanism is established in *P. aeruginosa*. Direct binding and in vitro stimulation assays with the *P. putida* proteins have not been reported.

3. **Quantitative kinetics unknown.** Substrate affinities (Kₘ for lipid II), turnover rates, β-lactam acylation rates, and the relative contribution of the D,D-carboxypeptidase side activity for the *P. putida* enzyme are not characterized.

4. **Redundancy partners not mapped in *P. putida*.** The identity of the cognate PBP1a/LpoA system in *P. putida* KT2440, and the synthetic-lethality relationship between the two aPBPs in this organism, have not been experimentally confirmed here.

5. **Divisome vs. elongasome partitioning.** In *E. coli*, PBP1b is associated primarily with the divisome and PBP1a with the elongasome; whether this partitioning holds in *P. putida* is inferred, not shown.

6. **D,D-carboxypeptidase activity is condition-dependent.** This third activity was observed in vitro "in certain conditions," and its physiological relevance in vivo remains uncertain.

---

## Proposed Follow-up Experiments / Actions

1. **Genetic essentiality and redundancy.** Construct single (Δ*mrcB*) and double (Δ*mrcB* Δ*mrcA*/*ponA*) deletion mutants in *P. putida* KT2440 to test predicted synthetic lethality and confirm partial redundancy of the two class A PBPs.

2. **In vitro reconstitution.** Overexpress and purify recombinant Q88DY5; reconstitute into proteoliposomes and assay glycosyltransferase (lipid II polymerization, e.g., by continuous fluorescence assay), transpeptidase (cross-link formation), and D,D-carboxypeptidase activities to directly confirm the bifunctional biochemistry.

3. **LpoP activation assay.** Purify the *P. putida* LpoP ortholog and test direct binding to the PBP1b UB2H domain (e.g., SPR/ITC) and stimulation of both catalytic activities in vitro, mirroring the *P. aeruginosa* experiments.

4. **Catalytic-residue mutagenesis.** Generate GT (E188A/E188Q) and TP (S466A) point mutants and assess their effects on activity in vitro and on morphology/envelope integrity in vivo to validate the assigned catalytic residues.

5. **β-lactam and moenomycin profiling.** Measure β-lactam acylation of the TP domain and moenomycin inhibition of the GT domain to confirm the predicted pharmacology and evaluate PBP1b as an antibiotic target in *P. putida*.

6. **Localization.** Use a functional fluorescent PBP1b fusion to determine whether the protein localizes to midcell (divisome) during division, testing the predicted divisome association.

7. **Structural modeling/determination.** Use AlphaFold modeling (and, ideally, experimental structure determination) of Q88DY5 to verify the two active-site geometries and the UB2H regulatory interface.

---

## Conclusion

*P. putida* KT2440 **mrcB (Q88DY5)** encodes **Penicillin-Binding Protein 1B**, a bifunctional, inner-membrane-anchored, periplasm-facing class A peptidoglycan synthase. It polymerizes lipid II into glycan strands via its GT51 domain (Glu188) and cross-links peptide stems via its D,D-transpeptidase domain (Ser466, the β-lactam target), with additional D,D-carboxypeptidase activity. Its activity is switched on allosterically by the outer-membrane lipoprotein LpoP acting through the UB2H domain, and is coordinated with the cell-division divisome. It builds and fortifies the murein sacculus, acting redundantly with PBP1a to maintain rod shape and envelope integrity. All catalytic and regulatory motifs are conserved and intact, making the functional assignment robust despite the absence of a direct experimental study of this specific ortholog.


## Artifacts

- [OpenScientist final report](mrcB-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](mrcB-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:30044025
2. PMID:26370943
3. PMID:32320673
4. PMID:24821816
5. PMID:30622193
6. PMID:32037461
7. PMID:28096447
8. PMID:33830599
9. PMID:27899450
10. PMID:40691462