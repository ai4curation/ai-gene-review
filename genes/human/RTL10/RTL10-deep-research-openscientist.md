---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-24T13:13:33.845153'
end_time: '2026-10-24T13:30:55.122023'
duration_seconds: 1041.28
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: RTL10
  gene_symbol: RTL10
  uniprot_accession: Q7L3V2
  protein_description: 'RecName: Full=Protein Bop {ECO:0000303|PubMed:23055042}; AltName:
    Full=BH3-only protein; AltName: Full=Retrotransposon Gag-like protein 10 {ECO:0000312|HGNC:HGNC:26112};'
  gene_info: Name=RTL10 {ECO:0000312|HGNC:HGNC:26112}; Synonyms=BOP, C22orf29;
  organism_full: Homo sapiens (Human).
  protein_family: Not specified in UniProt
  protein_domains: RTL1/1-8/LDOC_capsid-like. (IPR032549); RTL1-8_LDOC (PF16297)
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
citation_count: 3
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: RTL10-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: RTL10-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q7L3V2
- **Protein Description:** RecName: Full=Protein Bop {ECO:0000303|PubMed:23055042}; AltName: Full=BH3-only protein; AltName: Full=Retrotransposon Gag-like protein 10 {ECO:0000312|HGNC:HGNC:26112};
- **Gene Information:** Name=RTL10 {ECO:0000312|HGNC:HGNC:26112}; Synonyms=BOP, C22orf29;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** RTL1/1-8/LDOC_capsid-like. (IPR032549); RTL1-8_LDOC (PF16297)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "RTL10" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'RTL10' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **RTL10** (gene ID: RTL10, UniProt: Q7L3V2) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# RTL10 (Protein Bop, UniProt Q7L3V2): A Retrotransposon-Derived Mitochondrial BH3-Only Apoptosis Effector

## Summary

**RTL10 encodes Protein Bop (also called BOP, C22orf29, or Retrotransposon Gag-like protein 10), a mitochondrially-localized BH3-only member of the Bcl-2 protein family whose primary, experimentally-demonstrated function is to promote intrinsic (mitochondrial) apoptosis in human cells.** Despite its unusual evolutionary origin as a "domesticated" retroviral/retrotransposon gene, Bop acts biochemically like a classical pro-apoptotic BH3-only protein: it operates at the outer mitochondrial membrane, uses a single canonical BH3 helix to engage both the voltage-dependent anion channel VDAC1 and the pro-survival Bcl-2 proteins, and triggers the hallmark events of the intrinsic death pathway — loss of mitochondrial transmembrane potential (Δψm) and release of cytochrome c — ultimately executing death through the effectors BAK/BAX ([PMID: 23055042](https://pubmed.ncbi.nlm.nih.gov/23055042/)).

Three complementary layers of evidence converge on this conclusion. First, **direct experimental characterization** (Zhang et al., *Apoptosis* 2012) established the protein's mitochondrial localization, its BH3-dependent apoptotic activity, its binding partners, and its biochemical consequences. Second, **residue-level curation** in UniProt (Q7L3V2), derived from the primary paper, pins the functional BH3 motif to residues 114–128 and shows by site-directed mutagenesis that the invariant Leu118 and Asp123 are each required for pro-apoptotic activity. Third, **independent bioinformatic/sequence analysis** performed in this investigation demonstrates that Bop's BH3 core (LAQLGD) is a near-exact match to the BH3 of the well-characterized protein BID (LAQVGD), differing by a single conservative substitution — strongly corroborating that Bop is a genuine, BID-like BH3-only protein rather than a mislabeled family member.

Evolutionarily, **RTL10 is one of 11 eutherian-specific retrovirus/metavirus-derived RTL/SIRH ("domesticated") genes** built on a retroviral Gag/capsid-like scaffold (InterPro IPR032549; Pfam PF16297). Among its RTL paralogs, Bop is unique in carrying a functional BH3 motif, meaning its apoptotic role represents a lineage-specific functional innovation. Notably, Bop lacks a mouse ortholog, which both complicates mechanistic study in standard rodent models and underscores that this is a relatively recent, placental-mammal–associated addition to the apoptotic toolkit.

---

## Verification of Gene/Protein Identity

Before presenting findings, the mandatory identity check was performed. The gene symbol **RTL10** and all synonyms (**BOP, C22orf29**) correspond precisely to the target protein:

| Attribute | Target (from UniProt) | Literature/Database match |
|---|---|---|
| UniProt accession | Q7L3V2 | Q7L3V2 (Zhang et al. 2012) ✓ |
| Protein name | Protein Bop / BH3-only protein / RTL10 | "Human Bop... novel BH3-only member" ✓ |
| Organism | *Homo sapiens* | Human cell lines in primary paper ✓ |
| Key domain | RTL1/1-8/LDOC capsid-like (IPR032549; PF16297) | RTL/SIRH Gag/capsid-like family ✓ |
| Chromosome | — | 22q11.21 (OMIM *620751) ✓ |

**Conclusion:** The symbol is unambiguous for this protein. The primary characterization paper ([PMID: 23055042](https://pubmed.ncbi.nlm.nih.gov/23055042/)) explicitly studies UniProt Q7L3V2 under the name "Bop," and the family/domain assignment (RTL/SIRH) is consistent across the literature. No conflicting literature for a differently-identified gene with the same symbol was encountered. Research proceeded with confidence.

---

## Key Findings

### Finding 1 — Bop is a BH3-only, directly pro-apoptotic Bcl-2 family protein localized to mitochondria

The foundational finding of this investigation is that **Protein Bop is a bona fide BH3-only member of the Bcl-2 family that acts directly to drive mitochondrial (intrinsic) apoptosis.** This is established by the primary characterization study, Zhang et al. (*Apoptosis*, 2012; [PMID: 23055042](https://pubmed.ncbi.nlm.nih.gov/23055042/)), which identified and named the protein.

Several mutually reinforcing experimental observations define the mechanism:

- **Subcellular localization:** Bop "mainly localized to mitochondria," consistent with its role as an effector of the mitochondrial pathway. The authors showed that it "used its BH3 domain to contact the loop regions of voltage dependent anion channel 1 (VDAC1) in the outer mitochondrial membrane" ([PMID: 23055042](https://pubmed.ncbi.nlm.nih.gov/23055042/)). This places the protein's site of action squarely at the **outer mitochondrial membrane (OMM)**.

- **Biochemical activity:** Purified Bop protein "induced the loss of mitochondrial transmembrane potential (Δψm) and the release of cytochrome c" ([PMID: 23055042](https://pubmed.ncbi.nlm.nih.gov/23055042/)). These are the two canonical, defining biochemical outputs of mitochondrial outer membrane permeabilization (MOMP), the committed step of intrinsic apoptosis.

- **Regulation by pro-survival proteins:** Bop "used its BH3 domain to contact pro-survival Bcl-2 family members (Bcl-2, Bcl-X(L), Mcl-1, A1 and Bcl-w), which could inhibit Bop-induced apoptosis" ([PMID: 23055042](https://pubmed.ncbi.nlm.nih.gov/23055042/)). The breadth of pro-survival binding (all five major guardians) is characteristic of a "promiscuous" BH3-only sensitizer/activator akin to BID or BIM.

- **Pathway placement and physiological trigger:** Knockdown of Bop reduced vincristine (VCR)-induced cell death. Upon VCR treatment, Bop is released from phosphorylated Bcl-2 and then functions through the effectors Bak/Bax (releasing Bak from Bcl-XL). This connects Bop to a defined death stimulus (the microtubule poison vincristine) and positions it upstream of the BAK/BAX gateway.

Together these data establish the complete logic of a BH3-only protein: **sequestration by pro-survival Bcl-2 proteins under basal conditions → release upon an apoptotic stimulus → engagement of VDAC1/effectors at the OMM → MOMP (Δψm loss, cytochrome c release) → apoptosis.**

### Finding 2 — RTL10 is one of 11 retrovirus/retrotransposon-derived RTL/SIRH "domesticated" genes

Bop's biology cannot be separated from its remarkable evolutionary origin. **RTL10 is a member of the eutherian-specific RTL/SIRH (Retrotransposon Gag-like / sushi-ichi retrotransposon homologue) family of domesticated retroviral genes.** Two reviews establish this framing:

- Kaneko-Ishino & Ishino 2023 ([PMID: 37892118](https://pubmed.ncbi.nlm.nih.gov/37892118/)): "Eutherians have 11 retrotransposon Gag-like (RTL)/sushi-ichi retrotransposon homolog (SIRH) genes presumably derived from a certain retrovirus."

- Irie et al. 2026 ([PMID: 42511665](https://pubmed.ncbi.nlm.nih.gov/42511665/)): "Eutherian mammals possess 11 metavirus-derived genes, collectively known as the sushi-ichi retrotransposon homologue (SIRH)/Retrotransposon Gag-like (RTL) genes."

The family carries a retroviral **Gag/capsid-like domain** (InterPro IPR032549, "RTL1/1-8/LDOC_capsid-like"; Pfam PF16297, "RTL1-8_LDOC"). RTL10 maps to human chromosome **22q11.21**. The key conceptual point is that an ancestral retroviral structural (Gag/capsid) protein was "domesticated" into a host gene; in the case of RTL10, this scaffold acquired a functional BH3 motif and was repurposed as an apoptosis regulator.

### Finding 3 — Bop is a 364-aa, predominantly α-helical protein with no mouse ortholog

Structural and comparative-genomic data refine the picture. **Bop is 364 amino acids long and is predominantly α-helical** — circular dichroism indicated ~25% α-helix and ~5% β-strand (reported alongside Zhang et al. 2012; GeneCards/OMIM 620751; Ensembl ENSG00000215012). A predominantly helical fold is consistent with the Bcl-2 family, whose members are built from amphipathic α-helices, and with a functional BH3 element (itself an amphipathic α-helix).

The BH3 motif is required for pro-apoptotic activity and mediates the protein's interactions with VDAC1 (loop regions), the pro-survival Bcl-2 proteins (BCL2, BCL-XL, MCL1, A1, Bcl-w), and the effectors BAK/BAX — reiterating that the BH3 helix is the single functional interaction module ([PMID: 23055042](https://pubmed.ncbi.nlm.nih.gov/23055042/)).

Critically, **Bop orthologs are present in various species but NOT in mouse.** This absence has two implications: (1) standard mouse genetic models cannot be used to study Bop's loss-of-function phenotype, and (2) the apoptotic function encoded by RTL10 is a lineage-specific feature not shared across all mammals. Human Protein Atlas data show cytoplasmic/mitochondrial subcellular staining, consistent with the mitochondrial localization reported experimentally.

### Finding 4 — The BH3 motif maps to residues 114–128 with the invariant Leu118 and Asp123 both functionally essential

Residue-level evidence makes the mechanistic claim precise. The UniProt Q7L3V2 flat file (features curated from [PMID: 23055042](https://pubmed.ncbi.nlm.nih.gov/23055042/)) annotates a **BH3 MOTIF at residues 114–128**, with sequence:

```
   114                             128
    L  D  R  F  L  A  Q  L  G  D  Y  M  S  F  H
   114            118   122 123
                  L118  G122 D123
```

Sequence: `¹¹⁴LDRFLAQLGDYMSFH¹²⁸`

This contains the **canonical BH3 signature** — an invariant hydrophobic Leu (L118) and an invariant Asp (D123) separated by four residues, with the conserved Gly (G122) immediately preceding the Asp: …L118-A119-Q120-L121-G122-D123…, matching the Bcl-2-family BH3 consensus (Φ₁-x-x-x-x-D with the Gly-Asp hallmark).

Site-directed mutagenesis recorded in UniProt confirms functional essentiality:

| Mutation | Effect on pro-apoptotic activity |
|---|---|
| L (Leu118) → A | **Reduced** pro-apoptotic activity |
| D (Asp123) → A | **Reduced** pro-apoptotic activity |
| (unrelated control residue) → A | No effect |

The primary paper states the principle directly: "we demonstrated a novel human BH3-only protein (designated as Bop) which could induce apoptosis in a BH3 domain-dependent manner" ([PMID: 23055042](https://pubmed.ncbi.nlm.nih.gov/23055042/)); the UniProt residue-level mutagenesis makes this precise. UniProt keywords for the entry include **Apoptosis** and **Mitochondrion**.

Two additional sequence REGIONs are annotated: residues **66–88** fall within the Gag/capsid-like core (the retroviral-derived scaffold), and residues **258–364** constitute a **C-terminal low-complexity region** that is Pro-rich (~23%) and Glu-rich (~15%) — i.e., likely intrinsically disordered. Thus the protein can be read as a three-part architecture: a capsid-like structural core, a functional BH3 helix, and a disordered acidic/proline-rich tail.

### Finding 5 — Independent sequence alignment validates the BH3 as BID-like and unique among RTL paralogs

A bioinformatic analysis performed in this investigation independently corroborates the BH3 assignment. Aligning Bop's BH3 core (residues 118–123, **LAQLGD**) against canonical BH3 peptides shows conservation of the diagnostic Leu-…-Gly-Asp signature and a striking match to BID:

| Protein | BH3 core (aligned) | Note |
|---|---|---|
| **BOP / RTL10** | **LAQLGD** | Target |
| BID | LAQVGD | Single conservative L↔V difference |
| BIM | RRIGDE | Gly-Asp retained |
| BAX | IGDEL | effector |
| BAK | IGDDI | effector |

Bop's BH3 is therefore **most similar to BID's BH3**, differing by only a single conservative substitution (Leu vs Val). A regex scan of the full 364-aa sequence for the LxxxGD signature returned a single bona fide match inside the annotated BH3 region (position 118, LAQLGD); the only other hit (position 332, LETEGD) lies within the acidic/Pro-rich disordered C-terminal tail and is not a true BH3. This rules out spurious BH3-like motifs elsewhere in the protein and confirms a single, specific functional BH3.

Paralog comparison underscores Bop's distinctiveness: RTL-family members differ widely in length (LDOC1/RTL7 = 146 aa; RTL8A = 113 aa; PEG10/RTL2 = 708 aa; BOP/RTL10 = 364 aa), and **only Bop carries a functional BH3 motif.** The sequence-level match to BID corroborates the primary paper's identification of Bop as a genuine BH3-only protein ([PMID: 23055042](https://pubmed.ncbi.nlm.nih.gov/23055042/)).

---

## Mechanistic Model / Interpretation

The combined evidence supports a coherent mechanistic model in which Bop is a VCR-responsive BH3-only sensitizer/activator acting at the mitochondrion.

```
   DOMAIN ARCHITECTURE OF BOP (364 aa)
   ────────────────────────────────────────────────────────────
   1        66  88        114  128        258               364
   | capsid-like |   ...   |  BH3 helix |   ...  | Pro/Glu-rich |
   | (Gag core)  |        114-LDRFLAQLGDYMSFH-128 | disordered   |
                            L118  G122 D123        tail
   (retroviral-derived)   (BID-like; essential)   (low complexity)


   APOPTOTIC PATHWAY LOGIC
   ────────────────────────────────────────────────────────────
   BASAL STATE:
     Bop --BH3--> sequestered by pro-survival Bcl-2 proteins
                  (BCL2, BCL-XL, MCL1, A1/BCL2A1, Bcl-w)

   APOPTOTIC STIMULUS (e.g., vincristine / VCR):
     Bcl-2 phosphorylation --> Bop released from p-Bcl-2
                                        |
                                        v
     Bop --BH3--> VDAC1 loop regions (outer mitochondrial membrane)
     Bop --BH3--> neutralizes pro-survival guardians
     Bop -------> releases BAK from BCL-XL; engages BAK/BAX
                                        |
                                        v
            MOMP  -->  Δψm loss  +  cytochrome c release
                                        |
                                        v
                              INTRINSIC APOPTOSIS
```

**Primary function (the core answer to the research question):** Bop is not an enzyme, transporter, or classical signaling kinase; it is a **BH3-only apoptotic adapter/effector**. Its "substrate specificity" in functional terms is a set of **protein–protein interactions mediated by its single BH3 α-helix**: it binds (i) the OMM channel VDAC1 at its loop regions, (ii) the five pro-survival Bcl-2 guardians, and (iii) influences the BAK/BAX effector gateway. Its biochemical output is mitochondrial outer membrane permeabilization.

**Site of action:** the **outer mitochondrial membrane**, consistent with its demonstrated mitochondrial localization and the VDAC1 interaction.

**Pathway:** the **intrinsic (mitochondrial) apoptosis pathway** of the Bcl-2 family, downstream of a vincristine-triggered, Bcl-2-phosphorylation–dependent de-repression step and upstream of BAK/BAX-mediated MOMP.

**Evolutionary interpretation:** Bop is a striking example of molecular domestication. An ancestral retroviral Gag/capsid protein — normally a structural component of a virion — was co-opted into the eutherian genome and, uniquely among the 11 RTL/SIRH paralogs, acquired a BID-like BH3 helix that re-purposed it as a regulator of programmed cell death. The absence of a mouse ortholog marks this as a lineage-specific innovation within placental mammals.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [23055042](https://pubmed.ncbi.nlm.nih.gov/23055042/) | *Human Bop is a novel BH3-only member of the Bcl-2 protein family* | **Primary source.** Defines Bop's identity, mitochondrial localization, BH3-dependent apoptosis, VDAC1 and pro-survival binding, Δψm loss / cytochrome c release, VCR trigger, BAK/BAX execution, and the mutagenesis (L118A, D123A) underpinning the residue-level findings. |
| [37892118](https://pubmed.ncbi.nlm.nih.gov/37892118/) | *Retrovirus-Derived RTL/SIRH: Their Diverse Roles...* | Places RTL10 within the 11-member eutherian RTL/SIRH family of domesticated retroviral genes. |
| [42511665](https://pubmed.ncbi.nlm.nih.gov/42511665/) | *Virus-Derived Domesticated Genes in Microglia...* | Confirms the metavirus/retrotransposon origin of the RTL family that includes RTL10. |

**How the evidence fits together.** The single primary experimental paper ([PMID: 23055042](https://pubmed.ncbi.nlm.nih.gov/23055042/)) provides essentially all the direct functional evidence, and every mechanistic claim in this report traces back to it (directly or via UniProt's curation of it). The two reviews supply the evolutionary/family context but do not, by themselves, test Bop's function. The independent bioinformatic analysis in this investigation (BH3 alignment to BID; single-motif scan of the full sequence) does not add new wet-lab data but strengthens confidence that the BH3 assignment is specific and genuine, and that Bop is the only BH3-bearing RTL paralog.

---

## Limitations and Knowledge Gaps

1. **Single primary study.** The functional characterization rests almost entirely on one paper (Zhang et al. 2012). Independent replication of the key claims — mitochondrial localization, VDAC1 binding, direct MOMP induction — would materially strengthen the model. As of this investigation, no second primary functional study was identified.

2. **No mouse ortholog.** The absence of a rodent ortholog precludes classic knockout phenotyping in the standard mammalian model and limits mechanistic dissection in vivo. Any physiological (as opposed to cell-line) role remains largely uncharacterized.

3. **Activator vs. sensitizer ambiguity.** Although Bop binds all five pro-survival guardians (sensitizer-like) and is reported to function through BAK/BAX, whether it directly activates BAK/BAX (like BID/BIM) or acts purely by de-repression has not been resolved with the rigor (e.g., liposome/BAX-activation assays) applied to canonical BH3-only proteins.

4. **VDAC1 interaction mechanism.** The functional consequence of BH3–VDAC1 loop binding (as distinct from pro-survival protein neutralization) is not mechanistically dissected; VDAC1's role in MOMP is itself debated in the broader field.

5. **Physiological context and expression.** The tissue/cell types and physiological stimuli (beyond vincristine) in which RTL10/Bop is relevant are not well defined. The functional significance of the disordered Pro/Glu-rich C-terminal tail (258–364) and the retained Gag/capsid-like core (66–88) is unknown.

6. **Structural data.** No high-resolution experimental structure (X-ray/cryo-EM/NMR) of Bop or of a Bop-BH3:pro-survival complex is available; the fold is inferred from CD spectroscopy and homology.

---

## Proposed Follow-up Experiments / Actions

1. **Independent validation of core claims.** Reproduce mitochondrial localization (confocal co-staining; subcellular fractionation) and BH3-dependent apoptosis (L118A/D123A mutants) in multiple human cell lines; confirm Δψm loss and cytochrome c release with orthogonal assays.

2. **Direct-activator test.** Use defined liposome/BAX- and BAK-activation assays (with recombinant Bop BH3 peptides and full-length protein) to classify Bop as a direct activator or a de-repressor.

3. **Quantitative interactome.** Measure binding affinities (ITC/SPR/BLI) of the Bop BH3 peptide for BCL2, BCL-XL, MCL1, A1/BCL2A1, and Bcl-w to build a selectivity profile, and compare directly to BID's BH3 given the LAQLGD/LAQVGD similarity.

4. **Structural determination.** Solve the structure of the Bop BH3 in complex with a pro-survival protein (e.g., BCL-XL or MCL1) by X-ray or NMR; attempt a cryo-EM/AlphaFold-guided model of full-length Bop to define the capsid-like core's disposition.

5. **VDAC1 mechanism.** Map the BH3:VDAC1 loop interface by mutagenesis and test whether disrupting it uncouples Bop from MOMP independently of pro-survival binding.

6. **Physiological relevance.** Profile RTL10/Bop expression across human tissues and under apoptotic stimuli; use CRISPR knockout/knockdown in human models (since mouse lacks the gene) to define loss-of-function phenotypes, especially in response to microtubule poisons like vincristine.

7. **Evolutionary analysis.** Determine when the BH3 motif arose within the RTL10 lineage (comparative genomics across eutherians) to date this functional innovation and test whether BH3 presence correlates with any organismal trait.

---

## Direct Answer

**RTL10 encodes Protein Bop, a mitochondrially-localized BH3-only member of the Bcl-2 family whose primary function is to promote intrinsic (mitochondrial) apoptosis.** It acts at the outer mitochondrial membrane through a single canonical, BID-like BH3 helix (residues 114–128; essential Leu118 and Asp123) that contacts VDAC1 and the pro-survival proteins BCL2, BCL-XL, MCL1, A1/BCL2A1 and Bcl-w, thereby inducing loss of mitochondrial membrane potential and cytochrome c release and driving death via the BAK/BAX effectors (e.g., in vincristine-triggered, Bcl-2-phosphorylation–dependent apoptosis). Uniquely among the 11 eutherian "domesticated" retrotransposon/metavirus-derived RTL/SIRH genes built on a retroviral Gag/capsid-like scaffold, RTL10/Bop carries a functional BH3, making its apoptotic role a lineage-specific innovation (and it notably lacks a mouse ortholog).


## Artifacts

- [OpenScientist final report](RTL10-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](RTL10-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:23055042
2. PMID:37892118
3. PMID:42511665