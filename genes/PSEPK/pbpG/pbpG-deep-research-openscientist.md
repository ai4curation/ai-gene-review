---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T00:53:42.686706'
end_time: '2026-09-01T01:13:19.268394'
duration_seconds: 1176.58
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: pbpG
  gene_symbol: pbpG
  uniprot_accession: Q88GD0
  protein_description: 'SubName: Full=Periplasmic murein D-alanyl-D-alanine endopeptidase
    {ECO:0000313|EMBL:AAN69388.1}; EC=3.4.-.- {ECO:0000313|EMBL:AAN69388.1};'
  gene_info: Name=pbpG {ECO:0000313|EMBL:AAN69388.1}; OrderedLocusNames=PP_3794 {ECO:0000313|EMBL:AAN69388.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the peptidase S11 family.
  protein_domains: Beta-lactam/transpept-like. (IPR012338); Peptidase_S11. (IPR018044);
    Peptidase_S11_N. (IPR001967); Peptidase_S11 (PF00768)
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
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: pbpG-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: pbpG-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88GD0
- **Protein Description:** SubName: Full=Periplasmic murein D-alanyl-D-alanine endopeptidase {ECO:0000313|EMBL:AAN69388.1}; EC=3.4.-.- {ECO:0000313|EMBL:AAN69388.1};
- **Gene Information:** Name=pbpG {ECO:0000313|EMBL:AAN69388.1}; OrderedLocusNames=PP_3794 {ECO:0000313|EMBL:AAN69388.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the peptidase S11 family.
- **Key Domains:** Beta-lactam/transpept-like. (IPR012338); Peptidase_S11. (IPR018044); Peptidase_S11_N. (IPR001967); Peptidase_S11 (PF00768)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "pbpG" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'pbpG' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **pbpG** (gene ID: pbpG, UniProt: Q88GD0) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: pbpG (PP_3794 / Q88GD0)
### Penicillin-binding protein 7 (PBP7), a periplasmic D,D-endopeptidase of *Pseudomonas putida* KT2440

---

## 1. Summary (Answer to the Research Question)

**pbpG** (locus **PP_3794**, UniProt **Q88GD0**) of *Pseudomonas putida* KT2440 encodes **penicillin-binding protein 7 (PBP7)**, a **low-molecular-weight, serine-type D,D-peptidase (a penicillin-binding protein) of the peptidase S11 family**. Its primary function is the **hydrolytic cleavage of peptide cross-links in peptidoglycan (murein)** — specifically the **D,D-endopeptidase reaction that severs the D‑alanyl–*meso*-diaminopimelate (D‑Ala–mDAP) bond** joining two adjacent stem peptides (EC 3.4.–.–, catalysed via a covalent acyl‑Ser enzyme intermediate). The enzyme carries out this reaction **in the periplasm**, acting on the polymeric cell-wall sacculus, and it does so **as part of peptidoglycan-remodeling multi-enzyme complexes** that couple cross-link cleavage to glycan-strand cleavage (lytic transglycosylases) and to new wall synthesis, enabling controlled enlargement of the sacculus during cell **elongation and division** without lysis. It is a non-essential, functionally redundant component of the cell-wall-remodeling machinery.

> **Identity verification (performed and passed):** The gene symbol *pbpG* is used consistently for PBP7. A global pairwise alignment shows **Q88GD0 shares 61.5% amino-acid identity (over 304 aligned positions) with *E. coli* K-12 PbpG/PBP7 (UniProt P0AFI5)**, whose UniProt description is identically "D-alanyl-D-alanine endopeptidase." The UniProt record for Q88GD0 further confirms (i) the correct organism (*P. putida* KT2440), (ii) peptidase S11 family membership with the D-alanyl-D-alanine carboxypeptidase A N-terminal domain (Pfam PF00768; InterPro IPR001967/IPR018044/IPR012338), and (iii) an intact penicilloyl-serine transferase catalytic apparatus. This is unambiguously the correct protein — a bona fide PBP7 ortholog — and the annotation is internally consistent. One family/activity nuance is discussed in §6.

---

## 2. Molecular Identity and Catalytic Machinery (Direct Evidence)

Analysis of the UniProt Q88GD0 record (308 aa) provides direct, primary-database evidence for the protein's enzymatic nature:

| Feature | Position | Significance |
|---|---|---|
| **Signal peptide** | 1–26 | Sec-dependent export → **periplasmic** catalytic domain |
| **Peptidase S11 (DD-CPase A N-terminal) domain** | 36–264 | Penicilloyl-serine transferase fold of LMW PBPs |
| **SxxK motif** — Ser70‑Val‑Thr‑Lys73 | 70/73 | **Ser70 = catalytic nucleophile** (acyl-ester intermediate); Lys73 = general base |
| **SxN motif** — Ser127‑Glu‑Asn | 127 | Second conserved catalytic motif of the active site |
| **KTG motif** — Lys234‑Thr‑Gly | 234 | Substrate-binding motif lining the active-site cleft |

The co-occurrence of the **SxxK … SxN … KTG** motif triad is the structural signature of the penicilloyl-serine transferase superfamily to which all penicillin-binding proteins belong. The active-site serine (Ser70) attacks the peptide bond of the D‑Ala–containing stem peptide to form a covalent acyl-enzyme intermediate — the same chemistry that β‑lactam antibiotics hijack, explaining why the protein is "penicillin-binding." UniProt keywords ("Cell shape", "Cell wall biogenesis/degradation", "Hydrolase", "Peptidoglycan synthesis") corroborate the cell-wall role.

**Structural corroboration (AlphaFold).** The AlphaFold DB model of Q88GD0 (v6, 308 aa) is highly confident: **mean pLDDT = 91.1** (80% of residues >90), with the catalytic domain (36–264) at **mean pLDDT 97.7**. The four catalytic residues are each modeled at very high confidence (**Ser70 = 98.8, Lys73 = 98.9, Ser127 = 98.6, Lys234 = 98.9**), indicating a spatially coherent, well-formed active-site cleft characteristic of an LMW-PBP. In contrast, the **C-terminal segment (265–308) is lower confidence (mean pLDDT 84.9)**, consistent with a flexible/amphipathic C-terminal α-helix — precisely the region that in the *E. coli* ortholog mediates inner-membrane anchoring and midcell localization (see §5). This independent structural prediction reinforces both the catalytic assignment and the membrane-tethered, periplasm-facing topology.

---

## 3. Primary Function: The Catalyzed Reaction and Substrate Specificity

PBP7 is a **D,D-endopeptidase**. The defining biochemical literature on the ortholog established that:

- The chromosomal ORF directing expression of **PBP7 and PBP8** was identified and the gene **renamed *pbpG***; the predicted protein "contains the consensus motifs associated with other PBPs," and a C-terminal OmpT-cleavage site converts PBP7 into the slightly smaller **PBP8** (a proteolytic derivative, not a separate gene product) (Henderson, Templin & Young, 1995; **PMID 7721700**).
- **PBP7/8 was "shown to be a DD-endopeptidase"** (Romeis & Höltje, 1994; **PMID 8063800**).

**Substrate and reaction.** The physiological substrate is **cross-linked peptidoglycan**. The D,D-endopeptidase reaction hydrolyzes the **D‑alanyl–*meso*-diaminopimelate (D‑Ala⁴–mDAP) peptide cross-bridge** that covalently links two glycan strands (the 4→3 cross-link typical of Gram-negative A1γ peptidoglycan, as in *Pseudomonas*). This **cleaves inter-strand cross-links**, in contrast to the related S11 DD-**carboxypeptidases** (PBP5/PBP6-type) that merely trim the terminal D‑Ala from an uncrosslinked pentapeptide. Biochemically, PBP7 preferentially attacks cross-links within the **intact, high-molecular-weight polymeric sacculus** rather than isolated soluble muropeptides — consistent with a role in editing the mature wall in situ.

Functionally, low-molecular-weight PBPs "act in the modification of peptidoglycan to allow **expansion of the sacculus**" (Gittins, Phoenix & Pratt, 1994; **PMID 8117464**), and cross-link cleavage by endopeptidases is the rate-limiting "space-making" step that permits insertion of newly polymerized glycan during growth.

**Authoritative classification.** In the standard reference on peptidoglycan hydrolases (Vollmer, Joris, Charlier & Foster, 2008; **PMID 18266855**), D,D-endopeptidases are the class that cleaves the **peptide cross-link** (distinct from glycosidases/lytic transglycosylases that cut the glycan backbone, and from carboxypeptidases that trim terminal D-Ala); the reviewed physiological functions of such hydrolases are "the regulation of cell wall growth, the turnover of peptidoglycan during growth, the separation of daughter cells during cell division and autolysis." The substrate is the **cross-linked sacculus** — "a net-like sacculus made of glycan strands crosslinked by peptides" with a layered architecture in Gram-negative cells (Vollmer & Seligman, 2010; **PMID 20060721**). *Pseudomonas*, like *E. coli*, has A1γ-type peptidoglycan in which this cross-link is the **D‑Ala⁴–*meso*-DAP³ (4→3) bond** — the bond hydrolyzed by PBP7.

---

## 4. Subcellular Localization

The enzyme functions in the **periplasm**, acting on the sacculus that lies between the inner and outer membranes:

- Q88GD0 possesses an N-terminal **signal peptide (1–26)** directing Sec export to the periplasm (UniProt; §2).
- Low-M(r) PBPs "are thought to be **periplasmic proteins attached with varying affinities to the inner membrane** via C-terminal amphiphilic α-helices" (**PMID 8117464**). Because PBP7's catalytic domain projects into the periplasm, it accesses the murein layer directly.

The description in UniProt ("**Periplasmic** murein D-alanyl-D-alanine endopeptidase") is therefore consistent with both the sequence evidence and the biochemistry of the ortholog.

---

## 5. Pathway and Complex Context (Where It Fits Mechanistically)

PBP7 does not act in isolation; it is embedded in the **peptidoglycan biosynthesis/remodeling network**:

- **Coupling to lytic transglycosylases.** PBP7/8 binds the **soluble lytic transglycosylase Slt70** in vitro and "not only stabilize[s] but also **stimulate[s] the enzymatic activity of Slt70** by a protein-protein interaction," leading to the conclusion that "**Slt70, PBP7/8, and PBP3 may form a multienzyme complex in vivo**" (**PMID 8063800**). This links **peptide cross-link cleavage (PBP7)** to **glycan backbone cleavage (Slt70)** and to a **division-specific synthase (PBP3/FtsI)**.
- **Adaptor-organized hydrolase complexes.** The outer-membrane lipoprotein **NlpI** is a general adaptor that "can specifically form complexes with various PG endopeptidases," incorporating them into synthase-containing multi-enzyme assemblies that "coordinate the spatiotemporal action of PG synthases and hydrolases" (Banzhaf et al., 2020; **PMID 32009249**).

**Mechanistic model.** During elongation and division, the sacculus must be enlarged by inserting new material into a covalently closed, load-bearing network. Endopeptidases "cleave the crosslinks between adjacent PG strands to allow the incorporation of newly synthesized PG" and are "**collectively essential for bacterial growth**" (Alvarado Obando et al., 2024; **PMID 38598601**). PBP7 thus provides **regulated "space-maker" cleavage of cross-links**, temporally and spatially coordinated (via Slt70/NlpI/synthase complexes and functional interplay with DD-carboxypeptidases such as DacA1/PBP5) with new synthesis so the wall expands without catastrophic breakage — the essence of the "make-before-break" / three-for-one growth logic of Gram-negative peptidoglycan.

**Direct link to cell division (precise role).** A recent cell-biological study of the ortholog sharpens PBP7's specific contribution: "**PBP7 localizes in the lateral cell envelope and at midcell**," with its **C-terminal α-helix crucial for midcell localization** (but dispensable for catalysis); midcell recruitment "relies on the assembly of FtsZ up to FtsN in the divisome, and on the activity of PBP3" (Liu et al., 2024; **PMID 39344863**). Functionally, "the absence of PBP7 slows down the assembly of FtsN at midcell," the ΔpbpG mutant shows weaker HADA (transpeptidase) incorporation, and the authors conclude "**endopeptidase-mediated PG cleavage may be a rate-limiting step for septal PG synthesis**" (PMID 39344863). Thus PBP7 is a **division-associated (and lateral-wall) DD-endopeptidase** whose cross-link cleavage promotes divisome maturation (FtsN recruitment) and rate-limits septal peptidoglycan synthesis — a precise, non-generic role beyond mere bulk remodeling.

**Pleiotropy is limited/redundant, not primary.** Disruption of *pbpG* causes "**no obvious growth defects... suggesting that PBP 7 is not essential**" (**PMID 7721700**), and cells lacking multiple PBPs including PBP7 remain viable (Denome et al., 1999; **PMID 10383966**). This reflects **functional redundancy** among several cell-wall endopeptidases (e.g., MepA/MepS/MepM classes) rather than absence of function; the precise, non-redundant contribution of PBP7 is best captured by its biochemical specificity (cross-link cleavage in the mature sacculus) and its physical partnerships, rather than by knockout phenotypes.

---

## 6. Nuance / Caveat on Family vs. Annotated Activity

The InterPro/Pfam domain of Q88GD0 is literally named "**D-alanyl-D-alanine carboxypeptidase A** N-terminal" (the PBP5/PBP6/DacA — S11 — prototype, whose members are classically DD-**carboxypeptidases**), whereas the EMBL/UniProt name derived from the genome annotation (AAN69388.1) is "D-alanyl-D-alanine **endopeptidase**" (*pbpG*/PBP7). This is a genuine and well-known feature of PBP7: it shares the **S11 carboxypeptidase-type fold** yet functions as an **endopeptidase**, biochemically demonstrated for the *E. coli* ortholog (**PMID 8063800**). Two consequences for interpretation:

1. The **catalytic chemistry is certain** (serine DD-peptidase acting on D‑Ala-containing stem-peptide bonds; §2), and is **direct evidence**.
2. The **endopeptidase (cross-link-cleaving) assignment** for the *P. putida* protein is a **strong homology-based inference** from the *E. coli*/*P. aeruginosa pbpG*/PBP7 orthologs; a residual possibility of DD-carboxypeptidase (or dual) activity cannot be excluded without direct enzymology on the *P. putida* protein. The most parsimonious, evidence-weighted conclusion is that PP_3794 is the *P. putida* **PBP7 D,D-endopeptidase**.

---

## 7. Hypotheses: Supported and Refuted

**Supported**
- **H1 — PP_3794 is a serine-type PBP (penicilloyl-serine transferase).** Supported by direct sequence evidence: SxxK/SxN/KTG triad, active-site Ser70, S11 domain (UniProt Q88GD0); and by AlphaFold structural prediction (catalytic domain mean pLDDT 97.7; all four catalytic residues pLDDT >98).
- **H2 — Its primary reaction is D,D cleavage of peptidoglycan stem-peptide bonds (endopeptidase cleaving D‑Ala–mDAP cross-links).** Supported by orthology to PBP7 and biochemical demonstration in *E. coli* (PMID 8063800, 7721700).
- **H3 — It functions in the periplasm on the sacculus.** Supported by signal peptide and LMW-PBP topology (UniProt; PMID 8117464).
- **H4 — It acts within multi-enzyme PG-remodeling complexes (Slt70/synthase/NlpI).** Supported by PMID 8063800, 32009249.
- **H5 — It is individually non-essential (redundant) but the endopeptidase family is collectively essential.** Supported by PMID 7721700, 10383966, 38598601.
- **H6 — PBP7 has a division-associated role, promoting FtsN recruitment and rate-limiting septal PG synthesis, with midcell targeting via its C-terminal α-helix.** Supported by PMID 39344863 (direct evidence in the ortholog); orthology to Q88GD0 established at 61.5% identity.

**Refuted / down-weighted**
- **The protein is a simple DD-carboxypeptidase only** — down-weighted: although its fold is the DD-CPase-A (S11) type, the ortholog's demonstrated activity and the *pbpG*/endopeptidase annotation indicate cross-link (endopeptidase) cleavage as the primary role (§6).
- **The gene symbol is ambiguous / refers to a different protein** — refuted: gene name, organism, family, domains, and catalytic motifs are all mutually consistent (§1, §2).

---

## 8. Limitations and Future Directions

- **No organism-specific enzymology.** Substrate specificity (endo- vs. carboxypeptidase; preference for polymeric vs. soluble murein) is inferred from *E. coli*/*P. aeruginosa* orthologs, not measured for PP_3794 directly. Direct assays (muropeptide analysis by LC–MS after incubation with purified enzyme ± sacculi) would confirm the reaction.
- **Localization is inferred** from the signal peptide and family topology; direct fractionation/GFP-fusion localization in *P. putida* would confirm periplasmic residence and any inner-membrane association.
- **Interaction partners** (Slt70/MltG homologs, NlpI, PBP3/FtsI) are established in *E. coli*; the specific *P. putida* interactome should be verified (e.g., pulldowns, bacterial two-hybrid).
- **Redundancy mapping.** Combinatorial deletion with other *P. putida* endopeptidases would reveal the conditional, non-redundant role (division vs. elongation; stress; biofilm).
- **Structure.** A high-confidence AlphaFold model is already available (§2) and confirms the LMW-PBP fold and intact active site; an *experimental* structure with a bound cross-linked-muropeptide/transition-state analog would still be valuable to define the active-site cleft geometry that distinguishes endopeptidase from carboxypeptidase substrate binding.

---

## References (PubMed)

1. Henderson TA, Templin M, Young KD. *Identification and cloning of the gene encoding penicillin-binding protein 7 of Escherichia coli.* J Bacteriol, 1995. **PMID 7721700**.
2. Romeis T, Höltje JV. *Specific interaction of penicillin-binding proteins 3 and 7/8 with soluble lytic transglycosylase in Escherichia coli.* 1994. **PMID 8063800**.
3. Gittins JR, Phoenix DA, Pratt JM. *Multiple mechanisms of membrane anchoring of Escherichia coli penicillin-binding proteins.* FEMS Microbiol Rev, 1994. **PMID 8117464**.
4. Denome SA, Elf PK, Henderson TA, Nelson DE, Young KD. *Escherichia coli mutants lacking all possible combinations of eight penicillin binding proteins…* J Bacteriol, 1999. **PMID 10383966**.
5. Banzhaf M, et al. *Outer membrane lipoprotein NlpI scaffolds peptidoglycan hydrolases within multi-enzyme complexes in Escherichia coli.* EMBO J, 2020. **PMID 32009249**.
6. Aliashkevich A, Howell M, Brown ED, Cava F. *d-canavanine affects peptidoglycan structure, morphogenesis and fitness…* (uses *P. putida* cell wall). 2021. **PMID 33830599**.
7. Liu X, Boelter G, Vollmer W, Banzhaf M, den Blaauwen T. *Peptidoglycan Endopeptidase PBP7 Facilitates the Recruitment of FtsN to the Divisome and Promotes Peptidoglycan Synthesis in Escherichia coli.* 2024. **PMID 39344863**.
8. Alvarado Obando M, Rey-Varela D, Cava F, Dörr T. *Genetic interaction mapping reveals functional relationships between peptidoglycan endopeptidases and carboxypeptidases.* 2024. **PMID 38598601**.
9. Vollmer W, Joris B, Charlier P, Foster S. *Bacterial peptidoglycan (murein) hydrolases.* FEMS Microbiol Rev, 2008. **PMID 18266855**.
10. Vollmer W, Seligman SJ. *Architecture of peptidoglycan: more data and more models.* Trends Microbiol, 2010. **PMID 20060721**.
11. Cohen DN, et al. *Shared catalysis in virus entry and bacterial cell wall depolymerization.* 2009. **PMID 19361422** (confirms D,D-endopeptidases cleave the peptide cross-link).
12. UniProt Q88GD0 and P0AFI5 (sequences, domains, catalytic-site motifs, signal peptide; global alignment 61.5% identity over 304 positions); Pfam PF00768; InterPro IPR001967/IPR018044/IPR012338.
13. AlphaFold Protein Structure Database, model AF-Q88GD0-F1 (v6): mean pLDDT 91.1; catalytic domain (36–264) mean pLDDT 97.7; catalytic residues Ser70/Lys73/Ser127/Lys234 pLDDT >98.

*Note on organism-specific evidence:* No direct experimental characterization of the *P. putida* PBP7 (PP_3794) itself was found in the literature; its functional assignment is a high-confidence transfer from the biochemically and cell-biologically characterized *E. coli* ortholog (61.5% identity), supported by conserved catalytic motifs and a high-confidence AlphaFold model.


## Artifacts

- [OpenScientist final report](pbpG-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](pbpG-deep-research-openscientist_artifacts/final_report.pdf)