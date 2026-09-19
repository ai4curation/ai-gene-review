---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T22:58:12.165264'
end_time: '2026-08-31T23:57:04.351495'
duration_seconds: 3532.19
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: mrcA
  gene_symbol: mrcA
  uniprot_accession: Q88CU6
  protein_description: 'RecName: Full=Penicillin-binding protein 1A {ECO:0000256|ARBA:ARBA00018638};
    EC=2.4.99.28 {ECO:0000256|ARBA:ARBA00044770}; EC=3.4.16.4 {ECO:0000256|ARBA:ARBA00012448};'
  gene_info: Name=mrcA {ECO:0000313|EMBL:AAN70649.1}; OrderedLocusNames=PP_5084 {ECO:0000313|EMBL:AAN70649.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: In the N-terminal section; belongs to the
  protein_domains: Beta-lactam/transpept-like. (IPR012338); Glyco_trans_51. (IPR001264);
    Glycosyltr_51/Transpeptidase. (IPR050396); Lysozyme-like_dom_sf. (IPR023346);
    PBP_transglycosylase. (IPR036950)
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
citation_count: 17
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: mrcA-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: mrcA-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88CU6
- **Protein Description:** RecName: Full=Penicillin-binding protein 1A {ECO:0000256|ARBA:ARBA00018638}; EC=2.4.99.28 {ECO:0000256|ARBA:ARBA00044770}; EC=3.4.16.4 {ECO:0000256|ARBA:ARBA00012448};
- **Gene Information:** Name=mrcA {ECO:0000313|EMBL:AAN70649.1}; OrderedLocusNames=PP_5084 {ECO:0000313|EMBL:AAN70649.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** In the N-terminal section; belongs to the
- **Key Domains:** Beta-lactam/transpept-like. (IPR012338); Glyco_trans_51. (IPR001264); Glycosyltr_51/Transpeptidase. (IPR050396); Lysozyme-like_dom_sf. (IPR023346); PBP_transglycosylase. (IPR036950)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "mrcA" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'mrcA' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **mrcA** (gene ID: mrcA, UniProt: Q88CU6) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *mrcA* (PBP1a) — Penicillin-Binding Protein 1A of *Pseudomonas putida* KT2440

**Gene:** *mrcA* (OrderedLocusName PP_5084)
**Protein:** Penicillin-Binding Protein 1A (PBP1a)
**UniProt:** Q88CU6
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440)
**EC numbers:** 2.4.99.28 (peptidoglycan glycosyltransferase) · 3.4.16.4 (serine-type D-Ala-D-Ala carboxypeptidase / DD-peptidase)

---

## Summary

The gene *mrcA* (PP_5084) of *Pseudomonas putida* KT2440 encodes **Penicillin-Binding Protein 1A (PBP1a)**, a **bifunctional class A penicillin-binding protein (aPBP)** that is one of the principal cell-wall–building enzymes of the bacterium. Its identity is unambiguous: the UniProt entry (Q88CU6) annotates two distinct catalytic activities — a **peptidoglycan glycosyltransferase** (EC 2.4.99.28) and a **serine-type DD-carboxypeptidase/transpeptidase** (EC 3.4.16.4) — carried on the two signature domains of the family, the GT51 glycosyltransferase domain (IPR001264) and the beta-lactam/transpeptidase-like penicillin-binding domain (IPR012338). This two-domain architecture, together with the gene name *mrcA* and the ordered locus PP_5084, matches the canonical class A PBP and is fully consistent with the target identity supplied. There is no gene-symbol ambiguity: *mrcA* denotes PBP1a in γ-proteobacteria generally, and the *P. putida* protein is a direct ortholog of the biochemically characterized *E. coli* PBP1A.

Mechanistically, PBP1a **polymerizes the glycan backbone of peptidoglycan from the membrane-anchored precursor lipid II** (its GT domain, EC 2.4.99.28) and **cross-links adjacent glycan strands through their peptide stems** (its transpeptidase domain), thereby building and expanding the stress-bearing murein sacculus that surrounds the cytoplasmic membrane. The transpeptidase domain also displays DD-carboxypeptidase activity under certain conditions, which accounts for the second EC annotation (3.4.16.4). The enzyme works at the **periplasmic face of the inner (cytoplasmic) membrane**, to which it is tethered by a **single N-terminal transmembrane/signal-anchor helix** — a topology directly confirmed here by hydropathy analysis of the Q88CU6 sequence, which shows exactly one strong membrane-spanning segment at the extreme N-terminus and a large, otherwise soluble periplasmic catalytic region.

Physiologically, PBP1a does not act alone. It is activated *in trans* by the **outer-membrane lipoprotein LpoA**, a regulatory module restricted to γ-proteobacteria (which includes *Pseudomonas*), and it operates inside the **dynamic, cytoskeleton-organized elongasome and divisome complexes** that coordinate wall growth with cell elongation and division. PBP1a is functionally **semi-redundant with PBP1b (mrcB)** for viability — losing one is largely compensated by the other — but the two enzymes have distinct preferential roles. In the close relative *P. aeruginosa*, PBP1a localizes to the cell poles and its loss impairs motility. Because it carries an active transpeptidase serine, PBP1a is a **molecular target of β-lactam antibiotics**, and changes in its expression and drug-binding affinity are associated with β-lactam resistance in *Pseudomonas*.

---

## Gene/Protein Identity Verification

Before presenting the functional narrative, the mandatory identity checks required by the research brief were completed and all passed:

| Verification step | Result |
|---|---|
| Does the symbol *mrcA* match the protein description? | **Yes.** *mrcA* is the standard γ-proteobacterial gene name for PBP1a; UniProt Q88CU6 gives `Name=mrcA`, and the RecName is "Penicillin-binding protein 1A." |
| Is the organism correct? | **Yes.** *Pseudomonas putida* KT2440 (ATCC 47054 / DSM 6125 / NCIMB 11950), locus PP_5084 (EMBL AAN70649.1). |
| Do the family/domains align with literature? | **Yes.** Two catalytic EC activities (2.4.99.28 + 3.4.16.4) and two domains (GT51 glycosyltransferase + beta-lactam/transpeptidase-like) are exactly the class A PBP architecture described across the primary literature. |
| Any competing gene with the same symbol? | **No conflicting identity.** In *Stenotrophomonas maltophilia* the same *mrcA*/PBP1a symbol is used and refers to the same class of protein; there is no cross-organism symbol collision that would misdirect the annotation. |

**Conclusion:** The gene symbol is *not* ambiguous for this protein. All research below concerns the correct target: the class A PBP1a of *P. putida* KT2440.

---

## Key Findings

### Finding 1 — *mrcA* encodes a bifunctional class A PBP with both glycosyltransferase and transpeptidase activities

UniProt Q88CU6 annotates two catalytic EC activities on the same polypeptide: **EC 2.4.99.28 (peptidoglycan glycosyltransferase)** and **EC 3.4.16.4 (serine-type D-Ala-D-Ala carboxypeptidase / DD-peptidase)**, carried respectively on the **Glyco_trans_51 (GT51, IPR001264)** domain and the **Beta-lactam/transpeptidase-like (IPR012338)** domain. This is the defining two-domain architecture of class A penicillin-binding proteins (aPBPs). The primary literature is unequivocal on what these enzymes do: aPBPs "possess both PG glycosyltransferase (PGT) and transpeptidase (TP) activity to polymerize the wall glycans and cross-link them, respectively" ([PMID: 34429361](https://pubmed.ncbi.nlm.nih.gov/34429361/)), and each "possess[es] a PG glycosyltransferase (PGT) domain and a transpeptidase (TP) domain" ([PMID: 24341982](https://pubmed.ncbi.nlm.nih.gov/24341982/)).

In practical terms, PBP1a is a **peptidoglycan synthase**: one enzyme performs the two chemically distinct reactions needed to grow the bacterial cell wall — building the sugar (glycan) polymer, and stitching those polymers together through peptide cross-links. This dual capability is exactly what distinguishes class A PBPs from class B PBPs (transpeptidase only) and from monofunctional glycosyltransferases.

### Finding 2 — The substrate is lipid II; the enzyme also shows DD-carboxypeptidase activity

The glycosyltransferase reaction consumes **lipid II** — the membrane-embedded peptidoglycan precursor, GlcNAc-β-1,4-MurNAc-pentapeptide-pyrophosphoryl-undecaprenol. Reconstituted biochemical systems for this family "accept the basic unit N-acetylglucosamine-beta-1,4-N-acetyl-muramyl-pentapeptide-pyrophosphoryl-undecaprenol (lipid II), and lead to polymerization of the … segment into peptidoglycan" ([PMID: 10828288](https://pubmed.ncbi.nlm.nih.gov/10828288/)). The GT domain therefore takes individual lipid-II units and processively extends the glycan strand, releasing the undecaprenyl-pyrophosphate carrier for recycling.

The second annotated activity, **DD-carboxypeptidase (EC 3.4.16.4)**, is explained by the observation that these bifunctional synthases "also exhibit DD-carboxypeptidase activity in certain conditions" ([PMID: 26370943](https://pubmed.ncbi.nlm.nih.gov/26370943/)). The transpeptidase active site, which normally forms 4→3 cross-links by attacking the D-Ala–D-Ala bond of a donor stem peptide, can instead hydrolyze the terminal D-Ala (carboxypeptidation) when an acceptor amine is not engaged. This reconciles both EC numbers on a single active-site chemistry: the enzyme's serine nucleophile acylates the D-Ala-D-Ala terminus and can resolve the acyl-enzyme either by transpeptidation (cross-link) or by hydrolysis (carboxypeptidation).

**Substrate specificity summary:** primary substrate = **lipid II** (GT reaction); acyl-donor = **D-Ala–D-Ala–terminated pentapeptide stem** (TP/carboxypeptidase reaction); acyl-acceptor = the diamino acid (e.g., *meso*-DAP) side chain of a neighboring stem peptide (cross-linking).

### Finding 3 — PBP1a acts in the periplasm and is activated *in trans* by the outer-membrane lipoprotein LpoA

Class A PBPs are anchored in the cytoplasmic (inner) membrane by a single N-terminal transmembrane helix, with their GT and TP domains projecting into the **periplasm**, where the sacculus is assembled and remodeled. A defining regulatory feature in γ-proteobacteria is activation by a cognate outer-membrane lipoprotein: "Two OM lipoproteins, LpoA and LpoB, are essential for the function, respectively, of PBP1A and PBP1B … Each Lpo protein binds specifically to its cognate PBP and stimulates its transpeptidase activity, thereby facilitating attachment of new PG to the sacculus" ([PMID: 21183073](https://pubmed.ncbi.nlm.nih.gov/21183073/)). Critically for *Pseudomonas*, "LpoA/LpoB and their PBP-docking regions are restricted to γ-proteobacteria" ([PMID: 21183073](https://pubmed.ncbi.nlm.nih.gov/21183073/)), so this trans-envelope activation applies to *P. putida*.

The mechanism couples the two catalytic domains: "**LpoA directly increases the rate of the PBP1A TP reaction, which also results in enhanced PGT activity**" ([PMID: 24341982](https://pubmed.ncbi.nlm.nih.gov/24341982/)). LpoA reaches through the peptidoglycan mesh from the outer membrane to contact PBP1a at the inner membrane, forming a trans-envelope regulatory bridge that ensures new wall is added where and when the outer membrane signals the need — a spatial control mechanism for wall growth.

### Finding 4 — PBP1a is semi-redundant with PBP1b, shows polar localization/motility links in *Pseudomonas*, and is a β-lactam target

The two major aPBPs of γ-proteobacteria — PBP1a (*mrcA*) and PBP1b (*mrcB*) — are **semi-redundant**: "they are semiredundant; disruption of either is rescued by the other to maintain envelope homeostasis and promote proper growth" ([PMID: 36317921](https://pubmed.ncbi.nlm.nih.gov/36317921/)). This explains why single knockouts of *mrcA* are typically viable, while simultaneous loss of both is lethal. Despite the overlap, the two enzymes have distinct preferential roles, with PBP1a classically associated with cell elongation and PBP1b with division/septation.

In the close relative *P. aeruginosa*, PBP1a has a specific spatial and behavioral signature: "Knockout of PBP1a led to impaired motility, and this observation, together with its localization at the cell poles, suggests its involvement in flagellar function" ([PMID: 27821444](https://pubmed.ncbi.nlm.nih.gov/27821444/)). This links PBP1a-mediated wall synthesis to polar cell biology and motility, beyond generic wall maintenance.

Because PBP1a's transpeptidase reacts covalently with β-lactams (which mimic the D-Ala–D-Ala substrate), it is a **clinically relevant drug target**. In pan-β-lactam-resistant *P. aeruginosa* clinical strains, investigators report "significant variation of PBP1a/b binding affinities" ([PMID: 22733064](https://pubmed.ncbi.nlm.nih.gov/22733064/)), showing that altered PBP1a expression and drug binding contribute to resistance phenotypes.

### Finding 5 — PBP1a functions inside dynamic elongasome/divisome complexes coordinated by the MreB/FtsZ cytoskeleton

PBP1a does not act as an isolated enzyme but as a component of larger machines. Authoritative reviews establish that "**Sacculus growth during elongation and cell division is mediated by dynamic and transient multiprotein complexes, the elongasome and divisome**" ([PMID: 32424210](https://pubmed.ncbi.nlm.nih.gov/32424210/)). Within these, "peptidoglycan synthases are regulated by multiple and specific interactions with cell morphogenesis proteins that are linked to a dynamic cytoskeletal protein, either the actin-like MreB or the tubulin-like FtsZ" ([PMID: 32424210](https://pubmed.ncbi.nlm.nih.gov/32424210/)). Thus PBP1a's placement and timing are governed by the actin-like MreB cytoskeleton (elongation) and the tubulin-like FtsZ ring (division), and its activity requires the LpoA activator described above. This integrates PBP1a into the cell-cycle-regulated program of wall expansion rather than treating it as a free-running polymerase.

### Finding 6 — Sequence analysis confirms a single N-terminal membrane anchor with a large periplasmic catalytic region

A Kyte–Doolittle hydropathy analysis (window = 19) of the 817-residue *P. putida* PBP1a sequence (Q88CU6) identifies **exactly one strong transmembrane-like hydrophobic segment at the extreme N-terminus** (window-mean hydropathy peak ≈ 2.29, well above the ~1.6 TM threshold; centered near residues 9–24, spanning roughly residues 1–33). The remaining ~780 residues contain no segment exceeding the TM threshold (maximum hydropathy only ~0.87 beyond residue 100). The N-terminal sequence (MIRLLKFFWWSSVAVICALVLGVSGAFLYL…) shows a short positively charged cytoplasmic segment (MIRLLK — consistent with the "positive-inside" rule) followed by a long hydrophobic membrane-spanning stretch. This is the canonical **non-cleaved signal-anchor of a bitopic (type-II, N-in/C-out) inner-membrane protein**.

This bioinformatic result independently confirms the topology inferred from family membership: PBP1a is tethered to the cytoplasmic membrane by one N-terminal helix, its cytoplasmic tail is small and positively charged, and its two catalytic domains face the periplasm — exactly where lipid II is flipped and where the sacculus is built. The single-anchor architecture also distinguishes PBP1a from proteins with internal or multiple transmembrane segments.

---

## Mechanistic Model / Interpretation

Bringing the six findings together yields a coherent picture of where PBP1a sits and what it does.

### Topology and reaction (single-molecule view)

```
   PERIPLASM  (site of wall synthesis; LpoA activates from OM side)
   ────────────────────────────────────────────────────────────
        [ GT51 domain ]        [ Transpeptidase domain ]
        EC 2.4.99.28           EC 3.4.16.4
        lipid II  ->           D-Ala–D-Ala donor ->
        glycan strand          4→3 cross-link (or DD-carboxypeptidation)
              \                     /
               \___ periplasmic catalytic region (~residues 34–817) ___/
                                 |
   ==============================||================================  INNER
        single N-terminal TM / signal-anchor (res ~1–33)             MEMBRANE
                                 |
        MIRLLK...  (short, positively charged cytoplasmic N-tail; "positive-inside")
   ────────────────────────────────────────────────────────────
   CYTOPLASM
```

The enzyme grabs membrane-embedded **lipid II**, its GT51 domain polymerizes the disaccharide-peptide units into a growing **glycan strand**, and its transpeptidase domain then **cross-links** that strand to the existing sacculus by forming a 4→3 (DD-type) peptide bond. When no acceptor is engaged, the same transpeptidase serine can trim the terminal D-Ala (DD-carboxypeptidation), explaining the dual EC annotation.

### Regulatory and cellular context (systems view)

```
        OUTER MEMBRANE ── LpoA (lipoprotein activator, γ-proteobacteria only)
                              │  reaches through the PG mesh
                              ▼  binds PBP1a; stimulates TP → boosts GT (domain coupling)
   PEPTIDOGLYCAN  ┌───────────────────────────────────────────────┐
   SACCULUS       │   PBP1a builds/expands wall here (periplasm)   │
                  └───────────────────────────────────────────────┘
   INNER MEMBRANE ── PBP1a anchored; positioned within
                     ├─ ELONGASOME (MreB-linked)  → cell elongation
                     └─ DIVISOME  (FtsZ-linked)   → septation/division
                     semi-redundant partner: PBP1b (mrcB)
```

PBP1a is one of two interchangeable "workhorse" synthases (with PBP1b); it is switched on by the outer-membrane sensor LpoA, and it is steered in space and time by the MreB and FtsZ cytoskeletal systems. In *Pseudomonas* specifically, PBP1a additionally concentrates at the **cell poles**, where its activity supports motility/flagellar function. Its transpeptidase active site is the covalent target of **β-lactam antibiotics**, making PBP1a both a physiological cornerstone and a pharmacological pressure point.

### Comparison of the two γ-proteobacterial class A PBPs

| Property | PBP1a (*mrcA*, PP_5084) | PBP1b (*mrcB*) |
|---|---|---|
| Class | Class A (bifunctional) | Class A (bifunctional) |
| Activities | GT (EC 2.4.99.28) + TP/DD-CPase (EC 3.4.16.4) | GT + TP |
| Cognate activator | **LpoA** (OM lipoprotein) | LpoB (OM lipoprotein) |
| Preferential role | Elongation; polar localization in *Pseudomonas* | Division/septation |
| Essentiality | Non-essential alone (semi-redundant with PBP1b) | Non-essential alone (double KO lethal) |
| Drug relevance | β-lactam target; affinity altered in resistant strains | β-lactam target |

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports the annotation |
|---|---|---|
| [34429361](https://pubmed.ncbi.nlm.nih.gov/34429361/) | *LpoA activator stimulates PBP1a polymerase activity* | States aPBPs have both PGT and TP activity — defines PBP1a's two catalytic functions. |
| [24341982](https://pubmed.ncbi.nlm.nih.gov/24341982/) | *Lipoprotein activators stimulate E. coli PBPs* | Confirms two-domain (GT+TP) architecture; shows LpoA boosts TP and couples GT activity. |
| [10828288](https://pubmed.ncbi.nlm.nih.gov/10828288/) | *Inhibition of transglycosylation in PG synthesis* | Identifies **lipid II** as the GT substrate polymerized into peptidoglycan. |
| [26370943](https://pubmed.ncbi.nlm.nih.gov/26370943/) | *Activities and regulation of PG synthases* | Documents secondary **DD-carboxypeptidase** activity (EC 3.4.16.4) of these enzymes. |
| [21183073](https://pubmed.ncbi.nlm.nih.gov/21183073/) | *Regulation of PG synthesis by OM proteins* | Establishes **LpoA** as PBP1a's specific activator; module restricted to γ-proteobacteria. |
| [36317921](https://pubmed.ncbi.nlm.nih.gov/36317921/) | *PBP1A interacts with divisome in A. baumannii* | Shows PBP1a/PBP1b **semi-redundancy** and divisome interaction. |
| [27821444](https://pubmed.ncbi.nlm.nih.gov/27821444/) | *PBP3 essential in P. aeruginosa* | Reports PBP1a **polar localization** and **motility** phenotype in *P. aeruginosa*. |
| [22733064](https://pubmed.ncbi.nlm.nih.gov/22733064/) | *Pan-β-lactam resistance in P. aeruginosa* | Documents PBP1a as a **β-lactam target** with altered binding in resistant strains. |
| [32424210](https://pubmed.ncbi.nlm.nih.gov/32424210/) | *Regulation of PG synthesis and remodelling* | Places PBP1a in **elongasome/divisome** complexes coordinated by MreB/FtsZ. |

Supporting context papers reviewed include the murein synthase/hydrolase interaction studies ([PMID: 10037771](https://pubmed.ncbi.nlm.nih.gov/10037771/), [PMID: 10542235](https://pubmed.ncbi.nlm.nih.gov/10542235/)), reviews of cell-wall growth regulation ([PMID: 27862967](https://pubmed.ncbi.nlm.nih.gov/27862967/), [PMID: 28214390](https://pubmed.ncbi.nlm.nih.gov/28214390/)), SPOR-domain requirements for aPBP function ([PMID: 33144379](https://pubmed.ncbi.nlm.nih.gov/33144379/)), and *Pseudomonas*/related-organism β-lactam and PBP-profiling studies ([PMID: 36475840](https://pubmed.ncbi.nlm.nih.gov/36475840/), [PMID: 28861525](https://pubmed.ncbi.nlm.nih.gov/28861525/), [PMID: 22252801](https://pubmed.ncbi.nlm.nih.gov/22252801/)). Note that most direct biochemical demonstrations (lipid-II polymerization, LpoA activation, DD-carboxypeptidation) come from *E. coli* and other γ-proteobacteria; their applicability to the *P. putida* ortholog rests on strong sequence/domain conservation and shared family membership.

---

## Limitations and Knowledge Gaps

1. **No direct biochemistry on the *P. putida* protein.** The functional assignment for Q88CU6 rests on (a) UniProt EC/domain annotations, (b) sequence/hydropathy analysis performed here, and (c) transfer of well-established biochemistry from orthologs (chiefly *E. coli* PBP1A). No purified-enzyme kinetics, lipid-II turnover measurements, or LpoA-binding assays exist specifically for the *P. putida* KT2440 protein.

2. **Phenotype inference is cross-species.** The polar-localization/motility link and semi-redundancy data come from *P. aeruginosa* and *A. baumannii*, respectively. While these are close relatives, *P. putida*–specific knockout phenotypes were not directly established in this investigation.

3. **DD-carboxypeptidase activity is context-dependent.** EC 3.4.16.4 is annotated and supported for the family, but the physiological significance and conditions of carboxypeptidation for PBP1a specifically remain less defined than its transpeptidase/glycosyltransferase roles.

4. **LpoA in *P. putida* not experimentally confirmed here.** LpoA's presence and PBP1a-activating function are inferred from the γ-proteobacterial restriction of the module; the *P. putida* LpoA ortholog and interaction were not experimentally validated.

5. **Structural data are homolog-based.** No experimental 3D structure of the *P. putida* PBP1a was analyzed; topology is inferred from hydropathy and family conservation.

---

## Proposed Follow-up Experiments / Actions

1. **In vitro reconstitution.** Purify recombinant *P. putida* PBP1a and assay (i) glycosyltransferase activity on fluorescent/radiolabeled lipid II, and (ii) transpeptidase/DD-carboxypeptidase activity on synthetic stem-peptide substrates; determine kinetic parameters and moenomycin (GT) / β-lactam (TP) sensitivity.

2. **LpoA interaction and activation.** Identify the *P. putida* LpoA ortholog, test direct binding to PBP1a (SPR/pull-down), and measure LpoA-dependent stimulation of TP and coupled GT activity, mirroring the *E. coli* assays in [PMID: 24341982](https://pubmed.ncbi.nlm.nih.gov/24341982/).

3. **Genetics in KT2440.** Construct clean Δ*mrcA*, Δ*mrcB*, and Δ*mrcA* Δ*mrcB* strains to confirm semi-redundancy and lethality of the double knockout; phenotype for growth, cell shape (microscopy), and β-lactam susceptibility.

4. **Localization and motility.** Build a functional fluorescent PBP1a fusion to test polar localization in *P. putida*, and assay swimming/swarming motility in the Δ*mrcA* background to confirm the *P. aeruginosa*-reported motility link.

5. **Structural determination.** Solve the crystal or cryo-EM structure (or refine an AlphaFold model with experimental restraints) to map the GT51 and transpeptidase active sites and validate the single-anchor topology predicted by hydropathy analysis.

6. **Resistance surveillance.** Profile PBP1a expression/β-lactam binding affinity across *P. putida* isolates to assess its contribution to intrinsic and acquired β-lactam resistance, extending the *P. aeruginosa* findings of [PMID: 22733064](https://pubmed.ncbi.nlm.nih.gov/22733064/).

---

## Conclusion

*mrcA* (PP_5084, Q88CU6) encodes **Penicillin-Binding Protein 1A**, a bifunctional, inner-membrane-anchored **class A peptidoglycan synthase**. Its GT51 glycosyltransferase domain (EC 2.4.99.28) polymerizes glycan strands from the precursor **lipid II**, and its transpeptidase domain (with secondary DD-carboxypeptidase activity, EC 3.4.16.4) cross-links the peptide stems to build the peptidoglycan sacculus. It functions at the **periplasmic face of the cytoplasmic membrane**, to which it is tethered by a single N-terminal signal-anchor helix, and it acts within **dynamic, cytoskeleton-organized elongasome/divisome complexes**, activated *in trans* by the γ-proteobacterial outer-membrane lipoprotein **LpoA**. PBP1a is **semi-redundant with PBP1b (mrcB)**, shows polar localization linked to motility in *Pseudomonas*, and — bearing an active transpeptidase serine — is a molecular **target of β-lactam antibiotics**.


## Artifacts

- [OpenScientist final report](mrcA-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](mrcA-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:34429361
2. PMID:24341982
3. PMID:10828288
4. PMID:26370943
5. PMID:21183073
6. PMID:36317921
7. PMID:27821444
8. PMID:22733064
9. PMID:32424210
10. PMID:10037771
11. PMID:10542235
12. PMID:27862967
13. PMID:28214390
14. PMID:33144379
15. PMID:36475840
16. PMID:28861525
17. PMID:22252801