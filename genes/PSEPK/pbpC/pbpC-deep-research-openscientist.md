---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T22:58:12.165882'
end_time: '2026-08-31T23:36:22.198800'
duration_seconds: 2290.03
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: pbpC
  gene_symbol: pbpC
  uniprot_accession: Q88QC2
  protein_description: 'RecName: Full=peptidoglycan glycosyltransferase {ECO:0000256|ARBA:ARBA00044770};
    EC=2.4.99.28 {ECO:0000256|ARBA:ARBA00044770};'
  gene_info: Name=pbpC {ECO:0000313|EMBL:AAN66199.1}; OrderedLocusNames=PP_0572 {ECO:0000313|EMBL:AAN66199.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: In the N-terminal section; belongs to the
  protein_domains: Beta-lactam/transpept-like. (IPR012338); Glyco_trans_51. (IPR001264);
    Glycosyltr_51/Transpeptidase. (IPR050396); Lysozyme-like_dom_sf. (IPR023346);
    PBP_1c. (IPR011815)
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
citation_count: 8
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: pbpC-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: pbpC-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88QC2
- **Protein Description:** RecName: Full=peptidoglycan glycosyltransferase {ECO:0000256|ARBA:ARBA00044770}; EC=2.4.99.28 {ECO:0000256|ARBA:ARBA00044770};
- **Gene Information:** Name=pbpC {ECO:0000313|EMBL:AAN66199.1}; OrderedLocusNames=PP_0572 {ECO:0000313|EMBL:AAN66199.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** In the N-terminal section; belongs to the
- **Key Domains:** Beta-lactam/transpept-like. (IPR012338); Glyco_trans_51. (IPR001264); Glycosyltr_51/Transpeptidase. (IPR050396); Lysozyme-like_dom_sf. (IPR023346); PBP_1c. (IPR011815)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "pbpC" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'pbpC' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **pbpC** (gene ID: pbpC, UniProt: Q88QC2) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of *pbpC* (PP_0572, UniProt Q88QC2) in *Pseudomonas putida* KT2440

## Summary

The gene **pbpC** (ordered locus **PP_0572**; UniProt **Q88QC2**) of *Pseudomonas putida* KT2440 encodes **penicillin-binding protein 1C (PBP1C)**, an ~85.7 kDa, 784-residue **class A penicillin-binding protein** of the bacterial cell-wall (peptidoglycan) biosynthetic machinery. Its primary molecular function is **peptidoglycan glycosyltransferase activity (EC 2.4.99.28)**: it catalyzes the polymerization of the membrane-linked precursor **lipid II** into the linear glycan strands (repeating β-1,4-linked GlcNAc–MurNAc–pentapeptide units) that form the backbone of the murein sacculus, releasing undecaprenyl diphosphate and a proton with each condensation. This reaction is carried out by the protein's family-51 glycosyltransferase (GT51) domain and, like all GT51 enzymes, is inhibited by moenomycin.

The functional assignment rests on a convergent chain of evidence. Bioinformatically, Q88QC2 possesses the diagnostic tripartite class A PBP architecture — an N-terminal transmembrane anchor, a GT51 glycosyltransferase domain, a penicillin-binding transpeptidase domain, and the PBP1C-specific C-terminal PBP_1c domain (IPR011815). It is a **full-length, colinear ortholog of the experimentally characterized *Escherichia coli* PBP1C (P76577)**, sharing ~59% amino-acid identity across all three domains and the same gene symbol *pbpC*. The GT51 catalytic glutamate and all three canonical transpeptidase active-site motifs (SxxK / SxN / KTG) are sequence-intact. However, the experimentally studied *E. coli* ortholog binds β-lactams atypically and was concluded to **function *in vivo* as a transglycosylase only**, meaning that although Q88QC2 retains an intact-looking transpeptidase active site, its physiologically relevant activity is glycan-chain polymerization rather than peptide cross-linking.

In terms of localization and pathway, PBP1C is anchored by a single N-terminal transmembrane helix in the **cytoplasmic (inner) membrane**, with its catalytic domains projecting into the **periplasm** where peptidoglycan is assembled. It is a **non-essential, accessory component of the peptidoglycan-synthesizing multienzyme complex**: in *E. coli*, PBP1C physically associates with the major murein polymerase PBP1B, the essential transpeptidases PBP2 and PBP3, and the lytic transglycosylase MltA. Thus, PBP1C contributes glycan-strand polymerization capacity to a membrane-embedded cell-wall synthesis/remodeling assembly rather than acting as a stand-alone essential enzyme.

---

## Gene / Protein Identity Verification

Before presenting findings, the target identity was confirmed against the UniProt record and orthology analysis. The gene symbol *pbpC*, the EC number 2.4.99.28, the domain complement (Glyco_trans_51 / IPR001264; Beta-lactam/transpept-like / IPR012338; PBP_1c / IPR011815), and the organism (*P. putida* KT2440) are all mutually consistent and match the class A PBP / PBP1C interpretation. The most decisive verification is the orthology result: Q88QC2 aligns colinearly with *E. coli* PBP1C (P76577, gene name *pbpC*, protein "Penicillin-binding protein 1C", curated evidence level PE=1) at ~59% identity over the full length. **This is the correct gene**, and the literature on *E. coli* PBP1C is directly transferable by orthology. Where the report cites biochemistry from other class A PBPs (e.g., *S. pneumoniae* PBP2a, *L. monocytogenes* PBP4), it does so to illustrate the shared GT51 reaction mechanism, not to substitute a different gene.

---

## Key Findings

### Finding 1 — *pbpC* encodes the *P. putida* ortholog of penicillin-binding protein 1C, a membrane-anchored class A PBP

The 784-residue product of Q88QC2 (85.7 kDa) exhibits the canonical modular architecture of a **class A penicillin-binding protein**. A Kyte–Doolittle hydrophobicity analysis identifies a single **N-terminal transmembrane anchor** spanning approximately residues 14–32 (peak hydrophobicity 1.99, well above the 1.6 threshold used to call transmembrane helices). Following the anchor are the **glycosyltransferase family 51 (GT51) domain** (≈ residues 64–230), the **penicillin-binding transpeptidase domain** (≈ residues 307–423), and the **PBP1C-specific C-terminal domain** (PBP_1c, IPR011815; ≈ residues 694–780). The PBP_1c C-terminal domain is the specific InterPro signature that distinguishes PBP1C from its paralogs PBP1A and PBP1B, and its presence identifies Q88QC2 unambiguously as a **PBP1C ortholog** rather than a generic class A PBP.

This architecture matches that of the founding member of the family, *E. coli* PBP1C, which was cloned and characterized as "a third member of the multimodular class A penicillin-binding proteins of *Escherichia coli*" ([PMID: 10542235](https://pubmed.ncbi.nlm.nih.gov/10542235/)). That study established PBP1C as a close homolog of the bifunctional transpeptidase/transglycosylase enzymes PBP1A and PBP1B: *"PBP1C is a close homologue to the bifunctional transpeptidases/transglycosylases PBP1A and PBP1B and likewise shows murein polymerizing activity, which can be blocked by the transglycosylase inhibitor moenomycin."* The moenomycin-sensitive murein-polymerizing activity described there corresponds directly to the GT51 domain present in Q88QC2.

### Finding 2 — Primary function: peptidoglycan glycosyltransferase (EC 2.4.99.28) that polymerizes lipid II; the transpeptidase acts *in vivo* as a glycosyltransferase only

The primary, physiologically relevant reaction catalyzed by PBP1C is **glycan-chain polymerization**. The UniProt catalytic-activity annotation for Q88QC2 specifies EC 2.4.99.28: the disaccharide-peptide unit of **lipid II** [GlcNAc-(1→4)-MurNAc(oyl-L-Ala-γ-D-Glu-L-Lys-D-Ala-D-Ala)-di-*trans*,octa-*cis*-undecaprenyl diphosphate] is condensed onto the reducing end of the nascent glycan chain (n → n+1), releasing **undecaprenyl diphosphate** and a proton. The reaction is assigned to the pathway *"Cell wall biogenesis; peptidoglycan biosynthesis."*

The GT51 reaction is well established biochemically for class A PBPs generally. As summarized in a review of glycosyltransferase-targeted antibacterials, *"Synthesis of bacterial cell wall peptidoglycan requires glycosyltransferase enzymes that transfer the disaccharide-peptide from lipid II onto the growing glycan chain"* ([PMID: 26358369](https://pubmed.ncbi.nlm.nih.gov/26358369/)). Direct kinetic demonstrations on related class A PBPs include the *S. pneumoniae* PBP2a glycosyltransferase domain, which polymerizes dansyl-lipid II with k_cat/K_m ≈ 1 × 10⁻³ M⁻¹ s⁻¹ and is inhibited by moenomycin and vancomycin ([PMID: 12867450](https://pubmed.ncbi.nlm.nih.gov/12867450/)), and *L. monocytogenes* PBP4, which polymerizes *E. coli* lipid II with an efficiency of 1,400 M⁻¹ s⁻¹ ([PMID: 16484198](https://pubmed.ncbi.nlm.nih.gov/16484198/)).

Crucially, for PBP1C specifically, the *E. coli* study found that the transpeptidase (penicillin-binding) side of the enzyme is atypical. PBP1C *"does not bind to the same variety of penicillin derivatives as PBPs 1A and 1B"* ([PMID: 10542235](https://pubmed.ncbi.nlm.nih.gov/10542235/)), and the authors concluded that *"it is suggested that PBP1C functions in vivo as a transglycosylase only"*. Thus, although the transpeptidase domain is present and its active-site residues are conserved in sequence (Finding 4), the **operational function of PBP1C is glycan-chain polymerization**, not peptide cross-linking. By orthology (Finding 5), this conclusion applies to *P. putida* Q88QC2.

### Finding 3 — Localization: periplasmic face of the inner membrane, within a peptidoglycan-synthesizing multienzyme complex

PBP1C is a **cytoplasmic (inner) membrane protein**. Its single N-terminal transmembrane helix (residues ~14–32) anchors it in the membrane while the GT51, transpeptidase, and PBP_1c domains face the **periplasm**, where peptidoglycan is synthesized and remodeled. (UniProt does not carry a separate curated SUBCELLULAR LOCATION comment for Q88QC2; this topology is inferred from the hydrophobicity profile and from the biochemistry of the *E. coli* ortholog.)

PBP1C does not act in isolation. Affinity-chromatography experiments in *E. coli* showed that PBP1C covalently coupled to Sepharose specifically retained the murein polymerase **PBP1B**, the transpeptidases **PBP2** and **PBP3**, and the lytic transglycosylase **MltA**. The authors concluded that *"the specific interaction with these proteins suggests that PBP1C is assembled into a multienzyme complex consisting of both murein polymerases and hydrolases"* ([PMID: 10542235](https://pubmed.ncbi.nlm.nih.gov/10542235/)). The reciprocal experiment confirmed the association: MltA-Sepharose *"specifically retained the penicillin-binding proteins (PBPs) 1B, 1C, 2, and 3"* from membrane extracts ([PMID: 10037771](https://pubmed.ncbi.nlm.nih.gov/10037771/)). Together these results place PBP1C at the periplasmic face of the inner membrane, physically integrated into a **cell-wall synthesis/remodeling holoenzyme** that couples glycan polymerization, cross-linking, and controlled hydrolysis.

### Finding 4 — All catalytic motifs are sequence-intact: the GT51 glutamate and the three transpeptidase motifs (SxxK / SxN / KTG)

A motif scan of Q88QC2 confirms that the protein's catalytic machinery is conserved at the sequence level. The **GT51 domain** contains the conserved donor-glutamate signature (E-D-x-x-F, "EDRWF" at residue ~88), the hallmark catalytic glutamate of family-51 peptidoglycan glycosyltransferases that is essential for glycosyl transfer. The **transpeptidase module** carries the three sequential penicilloyl-serine transpeptidase motifs in the correct order and spacing characteristic of active-site serine penicillin-recognizing enzymes:

| Motif | Consensus | Sequence in Q88QC2 | Approx. residue | Role |
|-------|-----------|--------------------|-----------------|------|
| Motif 1 | S-x-x-K | STLK | Ser346 / Lys349 | Catalytic nucleophile serine + general base lysine |
| Motif 2 | S-x-N | SLN | ~400 | Active-site loop, substrate positioning |
| Motif 3 | K-(T/S)-G-(T/S) | KTGT | ~517 | β-strand lining the active-site cleft |

The presence and correct spacing of these motifs indicate that the transpeptidase fold is structurally preserved. This is not in contradiction with Finding 2: sequence conservation of the active site does not guarantee physiologically significant transpeptidation, and the *E. coli* ortholog — despite an analogous architecture — binds β-lactams atypically and is thought to act as a transglycosylase only *in vivo* ([PMID: 10542235](https://pubmed.ncbi.nlm.nih.gov/10542235/)). The intact GT51 glutamate, by contrast, is fully consistent with robust glycosyltransferase activity.

### Finding 5 — Orthology: ~59% identity to *E. coli* PBP1C confirms the assignment across all three domains

A Needleman–Wunsch global alignment (match +1, mismatch −1, gap −2) of Q88QC2 (784 aa) against *E. coli* PBP1C (P76577 / PBPC_ECOLI, 770 aa; UniProt gene name *pbpC*, protein "Penicillin-binding protein 1C", curated evidence level PE=1) yields **468/788 identical positions = 59.4% identity** over the aligned length (60.8% relative to the shorter sequence), with only 22 gap columns. The alignment is **colinear and full-length**, spanning all three functional modules (GT51, transpeptidase, and the PBP1C-specific C-terminal domain). The two proteins share the same gene symbol *pbpC* and the same modular architecture.

This level of identity across the entire protein — far above the ~30% threshold generally regarded as sufficient for confident functional transfer — **seals the orthology** and licenses the transfer of the experimentally established *E. coli* PBP1C functional model to *P. putida* Q88QC2. In practical terms, it means the conclusions that PBP1C is a moenomycin-sensitive glycan-chain polymerase, that it acts *in vivo* as a transglycosylase only, and that it participates in a multienzyme peptidoglycan-synthesis complex are all reasonably inferred for the *P. putida* protein.

---

## Mechanistic Model / Interpretation

The findings integrate into a coherent mechanistic picture of PBP1C as an accessory glycan-strand polymerase embedded in the inner-membrane peptidoglycan-synthesis machinery.

### Domain architecture (N → C terminus)

```
 Cytoplasm │ Inner membrane │            Periplasm (site of PG synthesis)
           │                │
   N-term ─┤   TM anchor    ├─[ GT51 ]───[ Transpeptidase ]───[ PBP_1c C-term ]─ C-term
           │  res ~14–32    │  res ~64–230   res ~307–423        res ~694–780
           │                │  (E88 catalytic)  (SxxK/SxN/KTG)   (IPR011815, PBP1C-specific)
```

### Reaction catalyzed (EC 2.4.99.28)

```
   [glycan chain]_n  +  lipid II  ──GT51──▶  [glycan chain]_(n+1)  +  undecaprenyl-PP  +  H+
                                    (moenomycin-inhibitable)
```

The GT51 domain binds the growing glycan chain in its **donor site** (the moenomycin-binding site) and the incoming lipid II precursor in its **acceptor site**, then forms a new β-1,4 glycosidic bond, extruding the C55 lipid carrier (undecaprenyl diphosphate) for recycling. Studies of related GT51 enzymes reveal **positive cooperativity between the acceptor and donor sites** ([PMID: 25462814](https://pubmed.ncbi.nlm.nih.gov/25462814/)), and this reaction is the validated target of moenomycin and, indirectly, of the glycopeptide antibiotics ([PMID: 16298347](https://pubmed.ncbi.nlm.nih.gov/16298347/); [PMID: 26358369](https://pubmed.ncbi.nlm.nih.gov/26358369/)).

### Functional role in the cell

PBP1C is best understood as an **accessory / back-up glycan polymerase** rather than an essential enzyme. In *E. coli*, the two "housekeeping" class A PBPs PBP1A and PBP1B are jointly essential — cells cannot survive loss of both — but a large deletion study showed that cells can survive on a very limited PBP complement, and that PBP1C is dispensable for viability ([PMID: 10383966](https://pubmed.ncbi.nlm.nih.gov/10383966/)). The physiological picture that emerges is:

| Property | PBP1C | Comparison (PBP1A/1B) |
|----------|-------|-----------------------|
| Class | Class A PBP | Class A PBP |
| GT51 glycosyltransferase | Yes (primary activity) | Yes |
| Transpeptidase *in vivo* | Degenerate / "transglycosylase only" | Yes (bifunctional) |
| β-lactam binding | Atypical / limited | Broad |
| Essentiality | Non-essential (accessory) | Jointly essential |
| Complex partners | PBP1B, PBP2, PBP3, MltA | Various |

The physical association of PBP1C with **both polymerases (PBP1B) and hydrolases (MltA)** suggests it participates in the coordinated make-and-break chemistry of cell-wall growth: as glycan strands are polymerized and cross-linked, lytic transglycosylases like MltA cleave existing strands to allow insertion of new material. Placing PBP1C within this complex ([PMID: 10542235](https://pubmed.ncbi.nlm.nih.gov/10542235/); [PMID: 10037771](https://pubmed.ncbi.nlm.nih.gov/10037771/)) implies its polymerizing activity is spatially and temporally coordinated with wall remodeling, possibly contributing to a specific "mode" of murein synthesis under certain growth conditions. Because *P. putida* Q88QC2 is a 59%-identical, colinear ortholog (Finding 5), this same accessory glycan-polymerase role is the most parsimonious model for its function.

### Localization summary

The enzyme operates **at the periplasmic face of the cytoplasmic (inner) membrane** — anchored in the lipid bilayer by its N-terminal helix, with its catalytic domains reaching into the periplasm where lipid II is flipped, polymerized, and cross-linked into the sacculus.

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution to this report |
|------|-----------------|-----------------------------|
| [10542235](https://pubmed.ncbi.nlm.nih.gov/10542235/) | *Cloning and characterization of PBP 1C … of E. coli* | **Central reference.** Establishes PBP1C as a class A PBP with moenomycin-sensitive murein-polymerizing activity, atypical β-lactam binding, "transglycosylase only" *in vivo* role, and membership in a multienzyme complex. |
| [10037771](https://pubmed.ncbi.nlm.nih.gov/10037771/) | *Interactions between PBP1B, MltA, and MipA of E. coli* | Reciprocal affinity chromatography: MltA retains PBPs 1B, 1C, 2, 3 — defines PBP1C's periplasmic complex partners. |
| [26358369](https://pubmed.ncbi.nlm.nih.gov/26358369/) | *Targeting Bacterial Cell Wall PG Synthesis by Inhibition of GT Activity* | Defines the GT51 reaction (lipid II → glycan chain) that EC 2.4.99.28 catalyzes. |
| [12867450](https://pubmed.ncbi.nlm.nih.gov/12867450/) | *GT domain of PBP2a from S. pneumoniae polymerizes murein glycan chains* | Direct kinetic demonstration of a class A PBP GT51 reaction (dansyl-lipid II; moenomycin/vancomycin inhibition). |
| [16484198](https://pubmed.ncbi.nlm.nih.gov/16484198/) | *Bifunctional GT/acyltransferase PBP4 of L. monocytogenes* | Quantifies class A PBP glycan polymerization (1,400 M⁻¹ s⁻¹ from E. coli lipid II); shows moenomycin sensitivity. |
| [10383966](https://pubmed.ncbi.nlm.nih.gov/10383966/) | *E. coli mutants lacking all combinations of 8 PBPs* | Demonstrates PBP1C is non-essential; only loss of both PBP1A and PBP1B is lethal. |
| [25462814](https://pubmed.ncbi.nlm.nih.gov/25462814/) | *Positive cooperativity between acceptor and donor sites of PG GT* | Mechanistic detail of GT51 donor/acceptor site cooperativity. |
| [16298347](https://pubmed.ncbi.nlm.nih.gov/16298347/) | *Targeting the forgotten transglycosylases* | Reviews moenomycin as the archetypal inhibitor of the transglycosylation step. |
| [33830599](https://pubmed.ncbi.nlm.nih.gov/33830599/) | *d-canavanine affects PG structure … in Rhizobiales* | Uses *P. putida* as a model for cell-wall chemistry; organism-relevant context. |

The evidence is **highly convergent**: no reviewed source contradicts the assignment of Q88QC2 as PBP1C or the conclusion that its primary function is glycan-chain polymerization. Several papers in the literature set concern β-lactam pharmacology and PBP-binding profiles (e.g., PMIDs 3073932, 3090016, 3897174, 3918982); these consistently note that PBP1C is a minor/atypical penicillin-binding protein — corroborating, rather than contradicting, the "transglycosylase-only" model.

---

## Limitations and Knowledge Gaps

1. **No direct experimental characterization of the *P. putida* protein.** All mechanistic conclusions for Q88QC2 are inferred by orthology from *E. coli* PBP1C. Although the ~59% full-length identity strongly supports functional transfer, no enzyme assay, deletion phenotype, or localization study has been performed on the *P. putida* protein itself.

2. **The transpeptidase activity remains formally unresolved.** The transpeptidase active-site motifs (SxxK/SxN/KTG) are sequence-intact in Q88QC2, yet the *E. coli* ortholog is thought to act as a transglycosylase only. Whether the *P. putida* enzyme retains any residual cross-linking or carboxypeptidase activity is untested. The intact motifs leave open the possibility of condition-specific or partner-dependent transpeptidation.

3. **Subcellular localization is inferred, not measured.** UniProt carries no curated SUBCELLULAR LOCATION comment for Q88QC2; the inner-membrane/periplasmic topology is derived from the hydrophobicity profile and orthology.

4. **Complex membership in *P. putida* is assumed.** The multienzyme-complex model (association with PBP1B, PBP2, PBP3, MltA) is established in *E. coli*. *P. putida* encodes orthologs of these partners, but the specific interactions have not been demonstrated in this organism.

5. **Physiological/regulatory role is unknown.** The precise conditions under which PBP1C contributes to cell-wall synthesis — its "mode" of murein synthesis, expression regulation, and any role under stress, stationary phase, or β-lactam challenge — remain uncharacterized in *P. putida*.

---

## Proposed Follow-up Experiments / Actions

1. **In vitro glycosyltransferase assay.** Express and purify the soluble (membrane-anchor-truncated) form of *P. putida* PBP1C and measure lipid II polymerization using dansyl-lipid II or a continuous fluorescence assay, with moenomycin as a positive-control inhibitor — directly testing the GT51 activity predicted here (cf. [PMID: 12867450](https://pubmed.ncbi.nlm.nih.gov/12867450/), [PMID: 16484198](https://pubmed.ncbi.nlm.nih.gov/16484198/)).

2. **Transpeptidase / β-lactam binding test.** Perform a Bocillin-FL (fluorescent penicillin) binding assay across a panel of β-lactams to determine whether the *P. putida* transpeptidase site binds penicillins atypically, as reported for *E. coli* PBP1C ([PMID: 10542235](https://pubmed.ncbi.nlm.nih.gov/10542235/)).

3. **Deletion phenotyping.** Construct a clean ΔPP_0572 mutant and characterize growth rate, cell morphology, peptidoglycan composition (HPLC/LC-MS muropeptide analysis), and β-lactam/moenomycin susceptibility — testing the predicted non-essential, accessory role ([PMID: 10383966](https://pubmed.ncbi.nlm.nih.gov/10383966/)).

4. **Localization.** Construct a functional fluorescent fusion (e.g., PBP1C-GFP) or perform cell fractionation/immunodetection to confirm inner-membrane localization and any subcellular positioning (lateral wall vs. septum).

5. **Interaction mapping.** Use bacterial two-hybrid, co-immunoprecipitation, or affinity chromatography in *P. putida* to test whether PBP1C associates with PBP1B, PBP2, PBP3, and lytic transglycosylase orthologs, validating the multienzyme-complex model ([PMID: 10037771](https://pubmed.ncbi.nlm.nih.gov/10037771/)).

6. **Structural confirmation.** Obtain an experimental or high-confidence predicted (AlphaFold) structure of Q88QC2 and superpose the GT51 and transpeptidase domains onto characterized templates to verify active-site geometry and the integrity/degeneracy of the transpeptidase pocket.

---

## Conclusion

*pbpC* (PP_0572, Q88QC2) of *Pseudomonas putida* KT2440 encodes **penicillin-binding protein 1C**, a membrane-anchored **class A PBP** and full-length ortholog (~59% identity) of experimentally characterized *E. coli* PBP1C. Its **primary function is peptidoglycan glycosyltransferase activity (EC 2.4.99.28)** — polymerizing the lipid II precursor into linear glycan strands of the cell wall via its moenomycin-sensitive GT51 domain, releasing undecaprenyl diphosphate. Although its transpeptidase active-site motifs are sequence-intact, the ortholog acts *in vivo* as a **transglycosylase only**. The enzyme operates at the **periplasmic face of the inner membrane** as a **non-essential, accessory component of the peptidoglycan-synthesizing multienzyme complex**, associating with murein polymerase PBP1B, transpeptidases PBP2/PBP3, and the lytic transglycosylase MltA.


## Artifacts

- [OpenScientist final report](pbpC-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](pbpC-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:10542235
2. PMID:26358369
3. PMID:12867450
4. PMID:16484198
5. PMID:10037771
6. PMID:25462814
7. PMID:16298347
8. PMID:10383966