---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T05:00:03.248349'
end_time: '2026-08-31T05:19:11.932487'
duration_seconds: 1148.68
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_0076
  gene_symbol: PP_0076
  uniprot_accession: Q88RQ3
  protein_description: 'SubName: Full=Choline betaine-binding protein {ECO:0000313|EMBL:AAN65710.2};'
  gene_info: OrderedLocusNames=PP_0076 {ECO:0000313|EMBL:AAN65710.2};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: ABC_choline_sub-bd. (IPR017783); ABC_Gly_betaine_transp_sub-bd.
    (IPR007210); OpuAC (PF04069)
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
citation_count: 12
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PP_0076-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PP_0076-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88RQ3
- **Protein Description:** SubName: Full=Choline betaine-binding protein {ECO:0000313|EMBL:AAN65710.2};
- **Gene Information:** OrderedLocusNames=PP_0076 {ECO:0000313|EMBL:AAN65710.2};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** ABC_choline_sub-bd. (IPR017783); ABC_Gly_betaine_transp_sub-bd. (IPR007210); OpuAC (PF04069)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_0076" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_0076' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_0076** (gene ID: PP_0076, UniProt: Q88RQ3) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: PP_0076 (Q88RQ3) in *Pseudomonas putida* KT2440

**Gene:** PP_0076 (OrderedLocusName) · **UniProt:** Q88RQ3
**Organism:** *Pseudomonas putida* strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440 (PSEPK)
**UniProt description:** "Choline betaine-binding protein"

## Summary

**PP_0076 (UniProt Q88RQ3) is the periplasmic, high-affinity substrate-binding protein (SBP) of a binding-protein-dependent ATP-binding cassette (ABC) importer, and its primary physiological substrate is choline (the quaternary ammonium compound (CH₃)₃N⁺-CH₂-CH₂-OH).** It is not an enzyme: it catalyzes no chemical reaction. Rather, it functions as the extracytoplasmic recognition and capture component of a transporter, binding choline in the periplasm with micromolar affinity and delivering it to the cognate integral-membrane permease (PP_0075) and cytoplasmic ATPase (PP_0074) for ATP-driven translocation across the inner membrane. This assignment is supported by (i) domain architecture placing PP_0076 in the OpuAC/ProX family of quaternary-ammonium-binding SBPs (Pfam PF04069, COG2113, InterPro IPR017783 "ABC transporter, choline substrate-binding"), (ii) 44% amino-acid identity to the experimentally validated choline-binding protein ChoX of *Sinorhizobium meliloti*, and (iii) conserved operon synteny matching the well-characterized *cbcXWV*/*choXWV* choline-uptake systems of other bacteria.

The protein carries out its function in the **periplasmic space** (GO:0042597). It is synthesized with an N-terminal cleavable Sec signal peptide and is a soluble periplasmic protein rather than a membrane-anchored lipoprotein. Mechanistically, the family recognizes the positively charged trimethylammonium head-group of choline through an aromatic "box" of tryptophan residues that provides cation-π stabilization, and clamps around the ligand via a **Venus-flytrap** closure of its two lobes. PP_0076 contains eight tryptophan residues, providing candidate positions for this aromatic cage.

Physiologically, PP_0076 sits within a genomic locus in *P. putida* KT2440 dedicated to **choline and choline-O-sulfate (COS) utilization**, immediately adjacent to a choline sulfatase (*betC*, PP_0077) and a LysR-type transcriptional regulator (PP_0079). Imported choline in *P. putida* can serve as a carbon, nitrogen, and energy source and as a precursor for the osmoprotectant glycine betaine (via the BetA/BetB oxidation pathway). Notably, in *P. putida* this specific *betC*-linked COS locus has been shown to serve nutritional utilization rather than osmoprotection, distinguishing the physiological logic of this transporter from classic osmostress betaine-uptake systems.

---

## Key Findings

### Finding 1 — PP_0076 is the periplasmic substrate-binding protein of a quaternary-ammonium ABC importer

PP_0076 (Q88RQ3) is a 307-amino-acid protein bearing an N-terminal cleavable **Sec-type signal peptide** (approximately residues 1–20), with the +1 mature residue being alanine and no lipobox cysteine — indicating a **soluble periplasmic protein**, not a lipoprotein. The bulk of the protein (residues ~29–278) comprises a single recognizable domain annotated as an "ABC-type glycine betaine transport system substrate-binding" module. This corresponds to **Pfam PF04069 (OpuAC)**, **InterPro IPR017783 (ABC transporter, choline substrate-binding)** and **IPR007210 (ABC glycine betaine transporter substrate-binding)**, and the SCOP/SUPFAM classification SSF53850 (periplasmic-binding-protein-like II fold, the class II SBP fold). The Gene3D assignment (3.40.190.100 + 3.40.190.10) and eggNOG orthology to **COG2113** ("ABC-type proline/glycine betaine transport system, periplasmic component") are fully concordant.

The InterPro-derived Gene Ontology annotations place the protein in the **periplasmic space (GO:0042597)** and the **ABC transporter complex (GO:0043190)**, with molecular function **choline binding (GO:0033265)** and biological process **choline transport (GO:0015871)**.

The functional logic of this family is established by biochemical and structural work on the homologous OpuAC subunit of the OpuA ABC transporter. In *Bacillus subtilis* and *Lactococcus lactis*, OpuAC "binds glycine betaine and proline betaine with high specificity and targets it to OpuAB for ATP-dependent translocation across the plasma membrane" [PMID: 16645306](https://pubmed.ncbi.nlm.nih.gov/16645306/). This defines exactly the role inferred for PP_0076: it is the specificity-conferring capture module that hands its ligand to the membrane permease for ATP-driven import. Structurally, the recognition mechanism is well understood — in the closed, liganded OpuA structure "the binding pocket is formed by three tryptophans (Trp-prism) coordinating the quaternary ammonium group of glycine betaine" [PMID: 20454456](https://pubmed.ncbi.nlm.nih.gov/20454456/). PP_0076's eight tryptophan residues (at sequence positions 37, 84, 122, 170, 199, 219, 276, 287) provide the candidate aromatic residues for this cation-π binding cage.

### Finding 2 — PP_0076 lies in the choline-O-sulfate/choline utilization locus adjacent to choline sulfatase (betC)

The genomic neighborhood of PP_0076 in *P. putida* KT2440 defines a complete SBP-dependent ABC transporter co-localized with choline-catabolic and regulatory genes:

| Locus tag | UniProt | Length (aa) | Annotation / role |
|-----------|---------|-------------|-------------------|
| PP_0074 | Q88RQ5 | 274 | ABC transporter **ATPase** (nucleotide-binding domain) |
| PP_0075 | Q88RQ4 | 521 | Membrane **permease** ("choline sulfate transporter") |
| **PP_0076** | **Q88RQ3** | **307** | **Periplasmic substrate-binding protein (this protein)** |
| PP_0077 | Q88RQ2 | 505 | **Choline sulfatase (betC)** |
| PP_0079 | Q88RQ0 | 299 | LysR-type transcriptional regulator |

This arrangement matches the described organization of the *P. putida bet* genes for choline-O-sulfate (COS) utilization, in which *betC* (choline sulfatase) "lies adjacent to an ATP-binding cassette transporter and a LysR type regulator" [PMID: 17116241](https://pubmed.ncbi.nlm.nih.gov/17116241/). Thus PP_0074/PP_0075/PP_0076 together constitute an ATPase/permease/binding-protein ABC importer physically embedded within the choline/COS catabolic locus.

Importantly, the same study established that this locus serves **nutritional utilization, not osmoprotection**, in *P. putida*: "betC is unrelated to osmoprotection in *Pseudomonas putida* while the betBA genes are required for both betaine synthesis and tolerance to high osmotic pressure" [PMID: 17116241](https://pubmed.ncbi.nlm.nih.gov/17116241/). This distinguishes the physiological purpose of the PP_0076 transporter (feeding COS/choline catabolism as a carbon/nitrogen source) from the classic osmostress-inducible betaine uptake systems, even though both belong to the same SBP superfamily.

### Finding 3 — Inferred substrate class: small quaternary-ammonium compounds (choline / betaine / choline-O-sulfate class)

The specificity of this SBP family is narrow and high-affinity, as shown by characterized homologs. *L. lactis* OpuAC "is highly specific for glycine betaine and the related proline betaine. Other compatible solutes like proline and carnitine bound with affinities that were 3 to 4 orders of magnitude lower" [PMID: 20454456](https://pubmed.ncbi.nlm.nih.gov/20454456/). *B. subtilis* OpuAC binds glycine betaine (K_D 17 ± 1 µM) and proline betaine (K_D 295 ± 27 µM) via the three-tryptophan cation-π prism [PMID: 16445940](https://pubmed.ncbi.nlm.nih.gov/16445940/), and the family retains the plasticity to bind additional related solutes — "important principles that enable OpuAC to specifically bind various compatible solutes were uncovered" [PMID: 18567662](https://pubmed.ncbi.nlm.nih.gov/18567662/).

Two lines of evidence narrow PP_0076's ligand within this class to a **choline-derived** quaternary ammonium. First, InterPro assigns PP_0076 the more specific signature IPR017783 ("ABC transporter, choline substrate-binding") and the GO terms "choline binding"/"choline transport." Second, the genomic coupling to choline sulfatase (*betC*, PP_0077, which hydrolyzes choline-O-sulfate to choline + sulfate) and to a choline-sulfate permease (PP_0075) argues that the physiological ligand is choline and/or choline-O-sulfate feeding COS catabolism.

### Finding 4 — PP_0076 is the Pseudomonas CbcX/ChoX ortholog: a high-affinity periplasmic choline-binding protein

The closest experimentally characterized homologs of PP_0076 are the choline-specific SBPs **CbcX** (*Pseudomonas syringae* / *P. aeruginosa*) and **ChoX** (*S. meliloti*; *Agrobacterium tumefaciens*). The evidence for these proteins directly informs PP_0076's function:

| Protein | Organism | Operon | Choline affinity | Betaine affinity | Reference |
|---------|----------|--------|-----------------|------------------|-----------|
| CbcX | *P. syringae* / *P. aeruginosa* | *cbcXWV* | K_m 2.6 µM (high) | K_m 24.2 µM (weaker) | [PMID: 19919675](https://pubmed.ncbi.nlm.nih.gov/19919675/) |
| ChoX | *S. meliloti* | *choXWV* | K_D 2.7 µM (high) | none | [PMID: 15342567](https://pubmed.ncbi.nlm.nih.gov/15342567/) |
| ChoX | *A. tumefaciens* | *choXWV* | K_D ~2 µM (high) | — | [PMID: 21803998](https://pubmed.ncbi.nlm.nih.gov/21803998/) |

In *P. syringae*/*P. aeruginosa*, the *cbcXWV* operon encodes CbcX (binding protein), CbcW (permease), and CbcV (ATPase); "CbcX binds choline with a high affinity (K_m, 2.6 microM) and, although it also binds betaine (K_m, 24.2 microM), CbcXWV-mediated betaine uptake did not occur in the presence of choline" [PMID: 19919675](https://pubmed.ncbi.nlm.nih.gov/19919675/) — i.e., choline is strongly preferred. In *S. meliloti*, ChoX "binds choline with a high affinity (K_D, 2.7 microM) and acetylcholine with a low affinity (K_D, 145 microM) but binds none of the betaines… Thus, Cho is a highly specific high-affinity choline transporter" [PMID: 15342567](https://pubmed.ncbi.nlm.nih.gov/15342567/).

The transport mechanism is defined by the *A. tumefaciens* ChoX studies: "Two tryptophan residues (W40 and W87) located in the predicted ligand-binding pocket are essential for choline binding. The structural model of ChoX… resembles the typical structure of substrate binding proteins with a so-called 'Venus flytrap mechanism' of substrate binding" [PMID: 21803998](https://pubmed.ncbi.nlm.nih.gov/21803998/). Crystal structures of *S. meliloti* ChoX in complex with choline and acetylcholine, and in closed substrate-free states, have been solved, defining the binding-site architecture in atomic detail [PMID: 18779321](https://pubmed.ncbi.nlm.nih.gov/18779321/), [PMID: 19642870](https://pubmed.ncbi.nlm.nih.gov/19642870/).

Critically, **PP_0076's operon architecture mirrors *cbcXWV*/*choXWV* exactly**: PP_0074 (ATPase, 274 aa) / PP_0075 (permease, 521 aa) / PP_0076 (SBP, this protein), and PP_0076 shares the PF04069/COG2113 SBP fold along with the candidate pocket tryptophans.

### Finding 5 — PP_0076 shares 44% identity with the experimentally validated choline-binding protein ChoX

A global Needleman–Wunsch pairwise alignment of PP_0076 (307 aa) against *S. meliloti* ChoX (UniProt Q92N37, 318 aa, annotated "Choline ABC transporter, periplasmic solute-binding component") yields **135 identical residues over 307 aligned positions = 44.0% identity**. At this level of sequence identity, orthology and functional conservation are strongly supported: ChoX is a biochemically validated high-affinity choline-binding SBP (K_D ~2.7 µM for choline; binds no betaines) [PMID: 15342567](https://pubmed.ncbi.nlm.nih.gov/15342567/). Transferring that function by orthology, PP_0076 is predicted to be a high-affinity choline-binding protein.

*P. putida* KT2440 additionally encodes a related paralog (UniProt Q88R38, "Choline/betaine/carnitine ABC transporter substrate-binding protein," 315 aa), indicating that this bacterium possesses **multiple quaternary-ammonium SBPs**. This is fully consistent with the multi-SBP Cbc transporter model, in which "a choline, betaine and carnitine transporter, designated Cbc… is unusual among members of the ATP-binding cassette (ABC) transporter family in its use of multiple periplasmic substrate-binding proteins (SBPs) that are highly specific for their substrates" [PMID: 19919675](https://pubmed.ncbi.nlm.nih.gov/19919675/). In such systems, one core permease/ATPase can recruit several substrate-specific SBPs (e.g., CbcX for choline, BetX for betaine, CaiX for carnitine).

---

## Mechanistic Model and Interpretation

The findings converge on a coherent picture of PP_0076 as the recognition module of a choline-importing ABC transporter operating in the periplasm.

### Transport architecture

```
        PERIPLASM                          |    INNER MEMBRANE    |   CYTOPLASM
                                           |                      |
   choline (from environment /             |                      |
   from betC hydrolysis of                 |                      |
   choline-O-sulfate)                      |                      |
        │                                  |                      |
        ▼                                  |                      |
   ┌──────────────┐   choline captured     |   ┌──────────────┐   |
   │  PP_0076 SBP │ ─────────────────────► │   │   PP_0075    │   |
   │ (Q88RQ3)     │   Venus-flytrap        |   │  permease    │   |
   │ Trp cation-π │   closure              |   │ (Q88RQ4)     │   |
   │  pocket      │ ◄───── docks onto ─────┼──►│              │   |
   └──────────────┘   permease             |   └──────┬───────┘   |
                                           |          │ conformational
                                           |          │ change powered by
                                           |   ┌──────┴───────┐   |
                                           |   │   PP_0074    │◄──┤  ATP
                                           |   │  ATPase      │   │  binding/
                                           |   │ (Q88RQ5)     │──►│  hydrolysis
                                           |   └──────────────┘   │  ADP + Pi
                                           |                      |    │
                                           |                      |    ▼
                                           |                      |  choline
                                           |                      |  imported
```

### Recognition mechanism

Choline is a small, hydrophilic cation whose defining chemical feature is the fixed positive charge on its trimethylammonium head-group. SBPs of the OpuAC/ChoX family solve the problem of recognizing this cation in water by constructing an **aromatic box** of tryptophan (and sometimes tyrosine) side-chains whose π-electron faces provide **cation-π stabilization** of the quaternary ammonium — the same physical principle used by acetylcholine-binding proteins and choline-binding enzymes. In the fully characterized homologs, this box comprises two or three essential tryptophans (e.g., W40/W87 in *A. tumefaciens* ChoX; a three-Trp prism in OpuAC). PP_0076's eight tryptophans supply more than enough candidates for this cage. Ligand binding triggers the classic **Venus-flytrap** closure, in which the two lobes of the SBP hinge shut around the substrate; the closed, liganded SBP then docks onto the periplasmic face of the PP_0075 permease and delivers the substrate into the translocation pathway, with the energy for transport supplied by ATP binding and hydrolysis at the PP_0074 ATPase.

A biomimetic-chemistry study underscores how discriminating this pocket is: a synthetic receptor designed to mimic the ChoX cavity reproduced its "synergistic dual-site binding mode that allows it to discriminate choline over structural analogues" [PMID: 29038482](https://pubmed.ncbi.nlm.nih.gov/29038482/), reinforcing that the ChoX-type architecture inferred for PP_0076 is genuinely choline-selective.

### Physiological role

The genomic context integrates PP_0076 into choline/choline-O-sulfate metabolism. Choline-O-sulfate is a widespread compatible solute and sulfur reserve in plants and fungi; bacteria that colonize soil and the rhizosphere (like *P. putida* KT2440) can scavenge it. In this locus, the choline sulfatase **BetC (PP_0077)** liberates choline (and sulfate) from choline-O-sulfate, and the PP_0074–0076 ABC transporter imports choline (and/or COS). Once in the cytoplasm, choline can be:

1. **Catabolized** as a carbon, nitrogen, and energy source; and/or
2. **Oxidized to glycine betaine** via the BetA (choline dehydrogenase) / BetB (betaine aldehyde dehydrogenase) pathway. In *P. putida*, the *betBA* genes — not *betC* — are what confer osmotic tolerance [PMID: 17116241](https://pubmed.ncbi.nlm.nih.gov/17116241/). Consistently, exogenous glycine betaine enhances salinity tolerance and growth of *P. putida* under salt stress [PMID: 16579486](https://pubmed.ncbi.nlm.nih.gov/16579486/), demonstrating that the choline→betaine axis is physiologically active in this species.

The key nuance from the primary literature is that this particular *betC*-associated transporter operates in the **nutritional** arm of choline/COS metabolism rather than the osmoprotective arm. PP_0076 therefore is best described as a **high-affinity choline scavenging receptor** whose captured substrate feeds downstream utilization (and can secondarily supply the betaine osmoprotection pathway).

---

## Evidence Base

| PMID | Title (abbreviated) | How it supports the annotation |
|------|--------------------|-------------------------------|
| [15342567](https://pubmed.ncbi.nlm.nih.gov/15342567/) | *S. meliloti* ABC transporter Cho highly specific for choline | Validates the 44%-identical ortholog ChoX as a highly specific high-affinity (K_D 2.7 µM) choline-binding SBP that binds no betaines — the strongest transfer-of-function anchor for PP_0076 |
| [19919675](https://pubmed.ncbi.nlm.nih.gov/19919675/) | Cbc transporter recruits multiple SBPs for quaternary ammonium compounds | Establishes the Pseudomonas CbcX choline-binding SBP (K_m 2.6 µM) and the multi-SBP *cbcXWV* architecture that PP_0076's operon mirrors; explains the KT2440 paralog |
| [21803998](https://pubmed.ncbi.nlm.nih.gov/21803998/) | Choline uptake in *A. tumefaciens* by ChoXWV | Defines the Venus-flytrap mechanism and the essential tryptophans (W40, W87) in the choline pocket — the inferred binding mechanism of PP_0076 |
| [17116241](https://pubmed.ncbi.nlm.nih.gov/17116241/) | Uncoupling of choline-O-sulfate utilization from osmoprotection in *P. putida* | Documents the exact genomic locus (ABC transporter adjacent to *betC* and a LysR regulator) and shows it serves nutritional COS utilization, not osmoprotection, in *P. putida* |
| [20454456](https://pubmed.ncbi.nlm.nih.gov/20454456/) | Ligand binding and crystal structures of OpuA SBP | Establishes the three-tryptophan (Trp-prism) cation-π recognition of quaternary ammonium and the narrow, high-affinity specificity of the family |
| [16645306](https://pubmed.ncbi.nlm.nih.gov/16645306/) | Structural analysis of *B. subtilis* OpuA and subunits | Defines the generic role of the OpuAC-family SBP: bind the solute and target it to the permease for ATP-dependent translocation |
| [16445940](https://pubmed.ncbi.nlm.nih.gov/16445940/) | Substrate specificity determinants of OpuAC | Quantifies GB (K_D 17 µM) vs PB (K_D 295 µM) binding and the cation-π prism; template for predicting SBP structures in this family |
| [18567662](https://pubmed.ncbi.nlm.nih.gov/18567662/) | *B. subtilis* OpuAC ligand binding & mutagenesis | Shows the family binds several related compatible solutes, supporting the choline/betaine-class substrate range |
| [18779321](https://pubmed.ncbi.nlm.nih.gov/18779321/) | Crystal structures of ChoX (liganded and unliganded-closed) | Atomic-resolution structures of the ChoX choline/acetylcholine binding pocket — the structural template for PP_0076 |
| [19642870](https://pubmed.ncbi.nlm.nih.gov/19642870/) | ChoX semi-closed and ligand-free structures | Reveals the sub-domain movements of the Venus-flytrap cycle in the ChoX ortholog |
| [29038482](https://pubmed.ncbi.nlm.nih.gov/29038482/) | Biomimetic choline receptor modeled on ChoX | Confirms the ChoX dual-site/aromatic-box binding mode confers selectivity for choline over analogues |
| [16579486](https://pubmed.ncbi.nlm.nih.gov/16579486/) | Glycine betaine enhances salinity tolerance of *P. putida* | Demonstrates the choline→betaine osmoprotection axis is active in *P. putida*, contextualizing downstream fate of imported choline |
| [10515910](https://pubmed.ncbi.nlm.nih.gov/10515910/) | BusA high-affinity betaine uptake in *L. lactis* | Illustrates the ABC-transporter/SBP functional organization for betaine uptake (K_m 1.7 µM), contextualizing the family |

**Concordance of evidence:** All 5 confirmed findings point consistently to the same conclusion. The domain/family assignment (Findings 1, 3), the operon synteny (Finding 2), and the quantitative sequence homology to a validated choline-binding protein (Findings 4, 5) are mutually reinforcing, and no evidence contradicts the choline-SBP assignment.

---

## Limitations and Knowledge Gaps

1. **No direct biochemical characterization of PP_0076 itself.** The functional assignment rests entirely on homology, domain signatures, operon context, and transfer of function from characterized orthologs (ChoX, CbcX). No published ligand-binding assay, K_D/K_m measurement, or transport assay has been performed on PP_0076 specifically. The precise affinity and the exact rank-order of choline vs. betaine vs. choline-O-sulfate for PP_0076 remain experimentally undetermined.

2. **No experimental structure of PP_0076.** The Venus-flytrap mechanism and the identity of the specific tryptophans forming the cation-π box are inferred from homolog structures (ChoX, OpuAC). Although PP_0076 has eight tryptophans, which of these actually line the binding pocket has not been confirmed by structure determination or mutagenesis. (An AlphaFold model would help but was not analyzed in this investigation.)

3. **Substrate ambiguity within the quaternary-ammonium class.** InterPro/GO annotate "choline," and the closest ortholog (ChoX, 44% identity) is choline-specific, but some family members (e.g., CbcX) also bind betaine, and the operon's linkage to choline sulfatase raises the possibility that choline-O-sulfate itself, rather than (or in addition to) free choline, is a physiological substrate. The permease PP_0075 is annotated as a "choline sulfate transporter," which keeps this open.

4. **Paralog redundancy and cross-talk.** KT2440 encodes at least one additional quaternary-ammonium SBP (Q88R38). In multi-SBP Cbc systems, several SBPs share a core permease/ATPase, so the functional boundaries between PP_0076 and its paralog(s), and whether they compete for or complement one another at PP_0074/PP_0075, are unresolved.

5. **Regulation not experimentally mapped for PP_0076.** The adjacent LysR-type regulator (PP_0079) is presumed to control the locus, and the *P. putida* study indicates the locus is tied to COS utilization rather than osmostress, but the exact inducer, promoter, and expression conditions for PP_0076 have not been directly demonstrated here.

---

## Proposed Follow-up Experiments and Actions

1. **Recombinant ligand-binding assays.** Express and purify mature PP_0076 (signal peptide removed) and measure equilibrium binding of choline, glycine betaine, proline betaine, acetylcholine, carnitine, and choline-O-sulfate by intrinsic tryptophan fluorescence quenching or isothermal titration calorimetry. This would directly establish substrate specificity and affinity (predicted: choline K_D in the low-µM range, betaines much weaker or absent — mirroring ChoX).

2. **Structural determination.** Solve the crystal structure (or generate and validate an AlphaFold model) of PP_0076 in ligand-free and choline-bound states to identify the pocket tryptophans and confirm the cation-π aromatic box and Venus-flytrap closure. Compare against the ChoX (PDB entries from PMID 18779321/19642870) and OpuAC structures.

3. **Site-directed mutagenesis of candidate pocket tryptophans.** By analogy to ChoX W40/W87, mutate the tryptophans predicted (from the structure/model) to line the pocket and test loss of choline binding, pinpointing the essential cation-π residues among the eight Trp in PP_0076.

4. **In vivo transport and genetics.** Construct a PP_0076 (and PP_0074/PP_0075) deletion in *P. putida* KT2440 and assay radiolabeled or LC-MS-based choline/choline-O-sulfate uptake and growth on choline/COS as sole carbon, nitrogen, and sulfur sources. Complement with the wild-type gene to confirm.

5. **Regulation studies.** Test PP_0079 (LysR regulator) control of the operon, identify the inducing metabolite (choline vs. choline-O-sulfate), and map the promoter/operator by reporter fusions and RNA-seq under choline/COS versus osmotic-stress conditions to formally confirm the nutritional (non-osmoprotective) physiology reported for this locus.

6. **Resolve paralog division of labor.** Compare PP_0076 and Q88R38 for substrate range and their ability to functionally couple to the shared permease/ATPase, clarifying whether KT2440 operates a multi-SBP Cbc-type system.

---

## Conclusion

PP_0076 (Q88RQ3) of *Pseudomonas putida* KT2440 is confidently annotated as the **periplasmic, high-affinity choline-binding substrate-binding protein of a binding-protein-dependent ABC importer** (with the membrane permease PP_0075 and ATPase PP_0074). It is a soluble periplasmic protein that recognizes the trimethylammonium head-group of choline through an aromatic tryptophan cation-π pocket and a Venus-flytrap closure, then delivers the substrate to the membrane transporter for ATP-driven import. The assignment is anchored by 44% identity to the experimentally validated choline-binding protein ChoX, conserved *cbcXWV*/*choXWV* operon synteny, and InterPro/GO/Pfam signatures, and it sits within a choline/choline-O-sulfate utilization locus (adjacent to choline sulfatase BetC) that serves nutrient acquisition and supplies choline for downstream metabolism, including the glycine-betaine osmoprotection pathway. The primary gap is the absence of direct biochemical or structural characterization of PP_0076 itself, which the proposed experiments would resolve.


## Artifacts

- [OpenScientist final report](PP_0076-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PP_0076-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:16645306
2. PMID:20454456
3. PMID:17116241
4. PMID:16445940
5. PMID:18567662
6. PMID:19919675
7. PMID:15342567
8. PMID:21803998
9. PMID:18779321
10. PMID:19642870
11. PMID:29038482
12. PMID:16579486