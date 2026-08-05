---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-20T18:53:19.768713'
end_time: '2026-07-20T19:34:52.677724'
duration_seconds: 2492.91
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: metF
  gene_symbol: metF
  uniprot_accession: Q88D51
  protein_description: 'RecName: Full=Methylenetetrahydrofolate reductase {ECO:0000256|RuleBase:RU003862};
    EC=1.5.1.54 {ECO:0000256|RuleBase:RU003862};'
  gene_info: Name=metF {ECO:0000313|EMBL:AAN70543.1}; OrderedLocusNames=PP_4977 {ECO:0000313|EMBL:AAN70543.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the methylenetetrahydrofolate reductase family.
  protein_domains: FAD-linked_oxidoreductase-like. (IPR029041); Mehydrof_redctse-like.
    (IPR003171); MTHF_reductase_bac. (IPR004620); MTHFR (PF02219)
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
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: metF-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: metF-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88D51
- **Protein Description:** RecName: Full=Methylenetetrahydrofolate reductase {ECO:0000256|RuleBase:RU003862}; EC=1.5.1.54 {ECO:0000256|RuleBase:RU003862};
- **Gene Information:** Name=metF {ECO:0000313|EMBL:AAN70543.1}; OrderedLocusNames=PP_4977 {ECO:0000313|EMBL:AAN70543.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the methylenetetrahydrofolate reductase family.
- **Key Domains:** FAD-linked_oxidoreductase-like. (IPR029041); Mehydrof_redctse-like. (IPR003171); MTHF_reductase_bac. (IPR004620); MTHFR (PF02219)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "metF" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'metF' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **metF** (gene ID: metF, UniProt: Q88D51) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: metF (Q88D51, PP_4977) — Methylenetetrahydrofolate Reductase of *Pseudomonas putida* KT2440

## Gene/Protein Identity Verification

Before research, the target identity was confirmed against the supplied UniProt record and independent database retrieval:

| Attribute | Value |
|---|---|
| UniProt accession | **Q88D51** |
| Gene name | **metF** (ordered locus **PP_4977**) |
| Organism | *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / KT2440) |
| Protein | Methylenetetrahydrofolate reductase (MTHFR) |
| EC number | **1.5.1.54** |
| Length / mass | 295 aa / ~33.0 kDa |
| Cofactor | **FAD** (one per subunit; ChEBI:57692) |
| Family | Methylenetetrahydrofolate reductase family |
| Domains | Pfam **PF02219** (MTHFR); InterPro IPR004620 (MTHF_reductase, bacterial), IPR003171 (Mehydrof_redctse-like), IPR029041 (FAD-linked oxidoreductase-like) |
| KEGG | ppu:PP_4977 |

**Verification outcome:** The gene symbol *metF*, the MTHFR protein description, the FAD flavoprotein family, and the domain architecture are fully mutually consistent. *metF* is the universally used symbol for the bacterial methylenetetrahydrofolate reductase gene (as in *E. coli*, *Salmonella*, *Streptomyces*). This is an unambiguous identification. The literature on the bacterial *metF*/MTHFR family (especially the well-characterized *E. coli* MetF) is directly applicable, and a direct sequence comparison (below) confirms Q88D51 is a bona fide member of this family. Note: the mammalian *MTHFR* gene shares the enzyme name but encodes a larger, differently regulated enzyme (NADPH-specific, with a regulatory domain); it is a distinct ortholog family member and is used here only where the shared catalytic chemistry is relevant.

---

## 1. Summary (Answer to the Research Question)

*metF* (PP_4977, Q88D51) encodes **methylenetetrahydrofolate reductase (MTHFR; EC 1.5.1.54)**, a **cytoplasmic FAD-dependent flavoenzyme** that catalyzes the **NADH-dependent reduction of 5,10-methylenetetrahydrofolate (CH₂-THF) to 5-methyltetrahydrofolate (CH₃-THF)**. This is the **penultimate, committed step of de novo L-methionine biosynthesis**: the 5-methyl-THF product is the one-carbon (methyl) donor used by methionine synthase (MetH/MetE) to remethylate homocysteine to methionine. The enzyme therefore sits at the branch point of folate one-carbon metabolism that channels one-carbon units into methyl-group (methionine/S-adenosylmethionine) metabolism.

---

## 2. Primary Function: The Catalyzed Reaction and Substrate Specificity

**Reaction (physiological direction, reductive):**

> 5,10-methylene-THF + NADH + H⁺ → 5-methyl-THF + NAD⁺  (Rhea:19821; EC 1.5.1.54)

**Substrate specificity and cofactors (evidence):**
- **Folate substrate:** (6R)-5,10-methylene-5,6,7,8-tetrahydrofolate; **product:** (6S)-5-methyl-5,6,7,8-tetrahydrofolate (UniProt catalytic-activity annotation, ChEBI-defined stereochemistry).
- **Electron donor:** **NADH** (bacterial MetF-type enzymes are NADH-specific, in contrast to NADPH-specific eukaryotic MTHFR).
- **Prosthetic group:** a non-covalently but tightly bound **FAD**, one per subunit, which acts as the redox intermediary between NADH and folate (UniProt COFACTOR annotation; keyword "Flavoprotein").
- The closely related, biochemically characterized *E. coli* enzyme "catalyzes the reduction of 5,10-methylenetetrahydrofolate (CH₂-H₄folate) to 5-methyltetrahydrofolate (CH₃-H₄folate)" and is a flavoprotein (Trimmer et al., 2001, PMID 11371182). The general family reaction is "the reduction of methylenetetrahydrofolate to methyltetrahydrofolate" (Yu et al., 2025, PMID 40016375).

**Mechanism (inferred from the characterized homolog):** Catalysis proceeds by a two–half-reaction (ping-pong) mechanism through the FAD: in the **reductive half-reaction** NADH reduces FAD to FADH⁻; in the **oxidative half-reaction** the reduced flavin transfers a hydride to CH₂-THF (via a proposed 5-iminium cation intermediate) to give CH₃-THF. In *E. coli*, an active-site aspartate (Asp120) sits near the flavin N1–C2=O locus — a feature that "distinguishes MTHFR from all other known flavin oxidoreductases" — and is required for folate reduction and stabilization of the iminium intermediate; glutamate 28 also contributes to folate activation/catalysis (Trimmer et al., 2001, PMID 11371182). In the physiological direction the reaction is essentially irreversible.

---

## 3. Structural Basis and Bioinformatic Evidence for Function

**Fold and quaternary structure:** The bacterial MTHFR catalytic domain is a **β₈α₈ (TIM) barrel** that binds one FAD; this fold is conserved from *E. coli* to *Thermus thermophilus*, "quite similar to the β(8)α(8) barrel of E. coli MTHFR," with "one flavin adenine dinucleotide (FAD) prosthetic group bound per dimer" (Igari et al., 2011, PMID 21858212). The *E. coli* MetF enzyme assembles as a **homotetramer** (the same study refers to "the tetramer of E. coli MTHFR"; Igari et al., 2011, PMID 21858212), and FAD binding is coupled to large intersubunit conformational changes — so PP_4977 is expected to be an oligomeric (tetrameric) flavoprotein rather than acting as a monomer.

**Direct evidence that Q88D51 is a true MetF-type MTHFR (this analysis):**
- Q88D51 (295 aa) is essentially the **same length as *E. coli* MetF (296 aa)**; it is a **"short," catalytic-domain-only bacterial MTHFR** and lacks the ~300-residue C-terminal regulatory (SAM-binding) domain found in eukaryotic MTHFR.
- A Needleman–Wunsch global alignment of Q88D51 vs. *E. coli* MetF (UniProt P0AEZ1) gave **40.7 % identity over 290 aligned residues** — well within the ortholog range for this family.
- The two experimentally validated *E. coli* catalytic residues are **strictly conserved** in Q88D51: **Glu28 → Glu24** and **Asp120 → Asp116** (plus flanking conserved positions, e.g., E. coli Pro122 → Pro118, Tyr60 → Tyr56).

Because the complete catalytic apparatus is conserved, the substrate specificity, cofactor usage, and mechanism established for *E. coli* MetF can be transferred to Q88D51 with high confidence.

**Regulatory implication of the "short" architecture:** Lacking the eukaryotic C-terminal regulatory domain, Q88D51 is **not expected to be allosterically inhibited by S-adenosylmethionine (SAM)**, unlike human MTHFR. Regulation of the bacterial enzyme is exerted primarily at the level of gene expression (Section 5).

---

## 4. Subcellular Localization

The gene product is a **soluble cytoplasmic enzyme**. No signal peptide or transmembrane segment is annotated for Q88D51, and MTHFR-family enzymes are cytosolic flavoproteins. This localization is expected because both substrates — 5,10-methylene-THF (generated by cytoplasmic serine hydroxymethyltransferase/one-carbon metabolism) and NADH — are cytoplasmic, as is the downstream methionine-synthase reaction. The enzyme thus carries out its function in the cytosol, within the folate one-carbon/methionine biosynthetic machinery. (Inference from sequence features and family biochemistry; no experimental localization study specific to PP_4977 was found.)

---

## 5. Pathway Context and Regulation

**Pathway membership (UniProt):**
- *Amino-acid biosynthesis; L-methionine biosynthesis via de novo pathway.*
- *One-carbon metabolism; tetrahydrofolate interconversion.*

**Position in the pathway:** In prokaryotes, "methylenetetrahydrofolate reductase and cobalamin-dependent methionine synthase catalyze the penultimate and ultimate steps in the biosynthesis of methionine" (Matthews et al., 1998, PMID 9587027). MetF produces CH₃-THF, which methionine synthase (MetH, B12-dependent; or MetE, B12-independent) uses to convert homocysteine → methionine; methionine is then the precursor of SAM, the cell's principal methyl donor.

**Essentiality:** Disruption of *metF* causes methionine auxotrophy — "Disruption of the metF gene led to methionine auxotrophy" in *Streptomyces lividans* (Blanco et al., 1998, PMID 9515933) — demonstrating that the folate branch through MetF is required for methionine synthesis in bacteria. High-throughput RB-TnSeq fitness analysis in *P. putida* KT2440 (Borchert et al., 2024, PMID 38323821) provides genome-scale functional-module context consistent with such biosynthetic gene assignments.

**Pathway reconstruction in *P. putida* KT2440 (this analysis, via KEGG):** KEGG assigns PP_4977 to orthology **K00297** (methylenetetrahydrofolate reductase, NADH; EC 1.5.1.54), pathway **ppu00670 "One carbon pool by folate"** (chromosome 5,669,524–5,670,411). The strain encodes a complete methionine/one-carbon route around MetF: serine hydroxymethyltransferase **glyA** (PP_0322, PP_0671) generates the 5,10-CH₂-THF substrate; **both** a B12-dependent methionine synthase **metH** (PP_2375) and B12-independent **metE** (PP_2698, PP_4637) consume the 5-methyl-THF product; and **metK** SAM synthetase (four paralogs) converts the resulting methionine to SAM. Because KT2440 has both MetH and MetE, MetF's 5-methyl-THF output is required for methionine synthesis **regardless of vitamin-B12 availability**.

**Note — a second MTHFR paralog:** KT2440 carries a second K00297-annotated gene, **PP_4638**, but it is a divergent **495-aa two-domain** protein (only 36.8% identity to *E. coli* MetF and 39.0% to PP_4977) located next to *metE* (PP_4637). PP_4977/Q88D51 — a single-domain ~33 kDa protein with the highest similarity to the characterized *E. coli* MetF — is therefore the **canonical, housekeeping short-form MetF**, while PP_4638 likely represents a specialized/regulated MTHFR-family variant.

**Transcriptional regulation (from bacterial paradigms):** *metF* is part of the methionine regulon. In enterobacteria the MetR activator coordinates *metE/metH* and modulates the *metF* branch, with vitamin-B12 signaling (MetR "acts in trans to activate the metE and metH genes"; Urbanowski et al., 1987, PMID 3549685). In actinomycetes the activator NdgR binds *metH* and *metF* upstream regions ("NdgR was enriched from crude cell lysates with a strong affinity to metH and metF upstream sequences"; Kim et al., 2012, PMID 23065973). This places *metF* expression under control tied to sulfur-amino-acid demand rather than to any pleiotropic housekeeping program.

---

## 6. Supported and Refuted Hypotheses

**Supported:**
1. Q88D51 is a genuine FAD-dependent MTHFR (EC 1.5.1.54) — supported by domain signatures, 40.7 % identity to *E. coli* MetF, and conservation of both catalytic residues.
2. Primary function = NADH-dependent reduction of CH₂-THF to CH₃-THF — supported by UniProt catalytic activity and homolog biochemistry.
3. Physiological role = penultimate step of de novo methionine biosynthesis (essential; auxotrophy on knockout in relatives) — supported.
4. Cytoplasmic, soluble localization — supported by absence of targeting signals and family biochemistry (inference).

**Refuted / not applicable:**
- Q88D51 is **not** a SAM-regulated long-form MTHFR (it lacks the regulatory domain), so allosteric SAM inhibition described for eukaryotic MTHFR does **not** apply.
- It is not a membrane, transport, or structural protein.

---

## 7. Limitations and Future Directions

- **No PP_4977-specific biochemical or structural study exists.** Function is assigned by (i) authoritative UniProt/EC annotation, (ii) strong homology and catalytic-residue conservation with the biochemically dissected *E. coli* MetF, and (iii) the conserved bacterial MTHFR fold. Direct kinetic characterization (Km for CH₂-THF and NADH, kcat, cofactor stoichiometry) of the purified *P. putida* enzyme would confirm the transferred parameters.
- **Localization is inferred**, not experimentally measured for PP_4977.
- **Regulation** is described from other bacteria; the specific *cis*/*trans* regulators of *P. putida metF* have not been mapped here.
- A recently described variant subfamily (S6MTHFR; Yu et al., 2025, PMID 40016375) runs the reaction in the **oxidative** direction coupled to THF-dependent demethylases. Q88D51's high similarity to canonical MetF and its methionine-biosynthesis pathway annotation indicate it is a **conventional reductive MTHFR**, but confirming reaction directionality experimentally would fully exclude the alternative.

---

## References (PMIDs)
- Trimmer, Ballou, Ludwig, Matthews (2001) *Biochemistry* — E. coli MTHFR catalysis; Asp120/Glu28. PMID **11371182**
- Igari et al. (2011) — *T. thermophilus* MTHFR crystal structure; β8α8 barrel, FAD. PMID **21858212**
- Matthews, Sheppard, Goulding (1998) — MTHFR & methionine synthase review. PMID **9587027**
- Blanco, Coque, Martin (1998) — *metF* disruption → methionine auxotrophy. PMID **9515933**
- Yu et al. (2025) — MTHFR family / reverse-reaction subtype. PMID **40016375**
- Kim et al. (2012) — NdgR regulation of *metH/metF*. PMID **23065973**
- Urbanowski et al. (1987) — MetR regulatory gene. PMID **3549685**
- Borchert et al. (2024) — RB-TnSeq functional modules in *P. putida* KT2440. PMID **38323821**
- Primary data: UniProt Q88D51; *E. coli* MetF P0AEZ1 (sequence alignment performed in this study).


## Artifacts

- [OpenScientist final report](metF-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](metF-deep-research-openscientist_artifacts/final_report.pdf)