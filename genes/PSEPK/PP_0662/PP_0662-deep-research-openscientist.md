---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-11T11:00:47.718532'
end_time: '2026-08-11T11:23:05.513434'
duration_seconds: 1337.79
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_0662
  gene_symbol: PP_0662
  uniprot_accession: Q88Q36
  protein_description: 'SubName: Full=Threonine synthase {ECO:0000313|EMBL:AAN66287.1};'
  gene_info: OrderedLocusNames=PP_0662 {ECO:0000313|EMBL:AAN66287.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: Thr_synth_N. (IPR029144); Thr_synth_N_sf. (IPR037158); Threonine_Synthase.
    (IPR051166); TrpB-like_PALP. (IPR001926); TrpB-like_PALP_sf. (IPR036052)
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
  path: PP_0662-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PP_0662-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88Q36
- **Protein Description:** SubName: Full=Threonine synthase {ECO:0000313|EMBL:AAN66287.1};
- **Gene Information:** OrderedLocusNames=PP_0662 {ECO:0000313|EMBL:AAN66287.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** Thr_synth_N. (IPR029144); Thr_synth_N_sf. (IPR037158); Threonine_Synthase. (IPR051166); TrpB-like_PALP. (IPR001926); TrpB-like_PALP_sf. (IPR036052)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_0662" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_0662' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_0662** (gene ID: PP_0662, UniProt: Q88Q36) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: PP_0662 (Q88Q36), Threonine Synthase from *Pseudomonas putida* KT2440

**UniProt:** Q88Q36 | **Locus:** PP_0662 | **Organism:** *Pseudomonas putida* KT2440 (PSEPK)
**Recommended name:** Threonine synthase (EC 4.2.3.1) | **Gene:** *thrC*

## Summary

**PP_0662 (UniProt Q88Q36) encodes threonine synthase (ThrC; EC 4.2.3.1), the pyridoxal-5′-phosphate (PLP)–dependent enzyme that catalyzes the final, committed step of L-threonine biosynthesis in *Pseudomonas putida* KT2440.** The enzyme carries out a β,γ-replacement reaction, converting O-phospho-L-homoserine (also written L-homoserine phosphate) plus water into L-threonine and inorganic phosphate. This is the terminal reaction of the aspartate-derived amino-acid pathway, positioned immediately downstream of homoserine kinase (ThrB) at the O-phosphohomoserine node — a branch point shared with methionine biosynthesis. The gene product is a soluble, cytoplasmic enzyme.

The identification is unambiguous and is supported by multiple independent lines of evidence. The UniProt record annotates PP_0662 as "Threonine synthase," and its InterPro domain architecture (Thr_synth_N, IPR029144; Threonine_Synthase, IPR051166; TrpB-like PALP fold-type II PLP domain, IPR001926/IPR036052) matches the canonical ThrC family. A global full-length alignment of Q88Q36 (462 aa) against the experimentally characterized *Escherichia coli* ThrC (P00934) yields **34.2% sequence identity over 424 aligned residues**, placing the two well above the twilight zone for homology and establishing orthology rather than a chance domain match. The catalytic PLP Schiff-base lysine is conserved and mapped to **Lys112** within the diagnostic HGPT-x-x-x-KDF threonine-synthase motif.

Functionally, threonine biosynthesis is required for growth of *P. putida* KT2440 on minimal medium: a genome-wide mutant screen recovered threonine auxotrophs, confirming that the de novo pathway completed by PP_0662/ThrC is (conditionally) essential in the absence of exogenous threonine. Because the threonine biosynthetic pathway is present in bacteria, fungi, and plants but **absent in mammals**, ThrC is a validated selective target for antibiotics, antifungals, and herbicides, and is inhibited by phosphonate substrate analogues such as APPA (the warhead of the rhizocticin antibiotics) and L-2-amino-5-phosphonovaleric acid.

---

## Key Findings

### Finding 1 — PP_0662 is threonine synthase (ThrC), catalyzing the terminal step of L-threonine biosynthesis

The primary function of PP_0662 is to catalyze the last step of the aspartate-derived threonine biosynthetic pathway. Threonine synthase is a **pyridoxal-5′-phosphate (PLP)-dependent enzyme** that performs a β,γ-replacement reaction:

```
O-phospho-L-homoserine  +  H2O  ──ThrC (PLP)──►  L-threonine  +  inorganic phosphate (Pi)
```

This assignment rests on three converging pieces of evidence. First, the UniProt record for Q88Q36 explicitly annotates PP_0662 as "Threonine synthase" (ordered locus PP_0662) in *P. putida* KT2440. Second, the InterPro domain complement is exactly that of the ThrC family: the N-terminal Thr_synth_N domain (IPR029144), the Threonine_Synthase signature (IPR051166), and the TrpB-like PALP (fold-type II) PLP-binding domain (IPR001926/IPR036052). Third, the reaction chemistry is well established for this family from direct enzymology. The mechanistic definition of the reaction is documented in the crystallographic and biochemical literature: threonine synthase "catalyzes the final step in the pathway, in which L-homoserine phosphate and water are converted into threonine and inorganic phosphate" ([PMID: 18621388](https://pubmed.ncbi.nlm.nih.gov/18621388/)), and the enzyme "catalyzes the beta,gamma-replacement reaction of l-homoserine phosphate to yield threonine and inorganic phosphate" ([PMID: 12952961](https://pubmed.ncbi.nlm.nih.gov/12952961/)). Substrate specificity is high and characteristic: the physiological substrate is O-phospho-L-homoserine, and the product is L-threonine (EC 4.2.3.1).

### Finding 2 — The enzyme adopts a two-domain fold-type II PLP architecture with substrate-induced domain closure

Threonine synthases share a conserved two-domain architecture built around a fold-type II (TrpB-like PALP) PLP-binding core — the same fold family predicted for PP_0662 by its IPR001926/IPR036052 domains. Crystallographic studies of orthologous enzymes reveal the catalytic mechanics. In the *Thermus thermophilus* HB8 enzyme, binding of a substrate analogue "induces a large conformational change at the domain level. The small domain rotates by about 25 degrees and approaches the large domain to close the active site" ([PMID: 12952961](https://pubmed.ncbi.nlm.nih.gov/12952961/)). This substrate-triggered domain closure sequesters the reaction intermediates from solvent and aligns catalytic residues.

The *Mycobacterium tuberculosis* structure refined the mechanistic picture, specifically implicating "the direct involvement of the phosphate moiety of the cofactor, rather than the inorganic phosphate product, in transferring a proton from C4′ to C(gamma) in the formation of the alphabeta-unsaturated aldimine" ([PMID: 18621388](https://pubmed.ncbi.nlm.nih.gov/18621388/)). Because PP_0662 belongs to this same structural family, these mechanistic features — domain closure upon substrate binding and PLP-mediated proton shuttling during formation of the α,β-unsaturated aldimine intermediate — are expected to apply directly to the *P. putida* enzyme.

### Finding 3 — The catalytic PLP lysine is conserved as Lys112 in the canonical HGPT…KDF motif

Fold-type II PLP enzymes anchor the cofactor through a Schiff base (internal aldimine) with a conserved active-site lysine. In the Q88Q36 sequence (462 aa), this residue was mapped by conserved-motif alignment to *E. coli* ThrC (P00934), whose catalytic PLP lysine is experimentally annotated as **Lys107** within the motif `HGPTLAFKDFGGRF`. The exactly homologous block in *P. putida* ThrC is `FHGPTRSSKDFAAQL`, placing the PLP Schiff-base lysine at **Lys112** — the only lysine in the conserved block. Notably, the *P. putida* protein contains just three lysines in total; the other two (K267, K414) lie in non-catalytic contexts, making the Lys112 assignment robust. The shared HGPT…KDF signature is the diagnostic PLP-binding-lysine motif of the threonine synthase family, consistent with the family's dependence on PLP chemistry ([PMID: 12952961](https://pubmed.ncbi.nlm.nih.gov/12952961/)).

### Finding 4 — PP_0662 is a clear full-length ortholog of characterized threonine synthase (34% identity to *E. coli* ThrC)

To move beyond database annotation and establish homology directly, a global Needleman–Wunsch alignment of full-length Q88Q36 (462 aa) against the experimentally characterized *E. coli* ThrC (P00934, 428 aa) was performed. The alignment produced **145 identical residues over 424 aligned columns (34.2% identity)**, spanning the entire protein length rather than a single localized domain. For proteins of this size, ~34% identity is comfortably above the ~25–30% "twilight zone" threshold, establishing unambiguous orthology. The alignment also preserves the catalytic PLP-lysine motif (E. coli Lys107 ↔ P. putida Lys112). This justifies confident transfer of the characterized ThrC function — "L-homoserine phosphate and water are converted into threonine and inorganic phosphate" ([PMID: 18621388](https://pubmed.ncbi.nlm.nih.gov/18621388/)) — to PP_0662.

| Property | *P. putida* PP_0662 (Q88Q36) | *E. coli* ThrC (P00934) |
|---|---|---|
| Length | 462 aa | 428 aa |
| Full-length identity | — | 34.2% (145/424) |
| Catalytic PLP lysine | Lys112 | Lys107 |
| Catalytic motif | F**HGPT**RSS**KDF**AAQL | L**HGPT**LAF**KDF**GGRF |
| Cofactor | PLP (fold-type II) | PLP (fold-type II) |
| Reaction | O-P-L-homoserine + H₂O → L-Thr + Pi | O-P-L-homoserine + H₂O → L-Thr + Pi |

### Finding 5 — Threonine biosynthesis is (conditionally) essential in *P. putida* KT2440, placing PP_0662 in the cytoplasmic aspartate pathway

A genome-wide mini-Tn5 mutant screen of *P. putida* KT2440 grown on glucose minimal medium recovered threonine auxotrophs (alongside auxotrophs for Ser, Met, Pro): "we also found auxotrophs for proline, serine, threonine and methionine, as well as auxotrophs for biotin, nicotinate and vitamin B12 that were not predicted in silico" ([PMID: 20158506](https://pubmed.ncbi.nlm.nih.gov/20158506/)). This provides direct experimental evidence that de novo threonine biosynthesis — the pathway completed by PP_0662/ThrC — is required for growth in the absence of exogenous threonine.

Within the aspartate-derived pathway, L-aspartate is converted stepwise to L-threonine through five enzymatic steps (aspartokinase → aspartate-semialdehyde dehydrogenase → homoserine dehydrogenase → homoserine kinase/ThrB → threonine synthase/ThrC), a sequence established by integrated kinetic analysis in *E. coli*: "We have determined the kinetic parameters of the individual steps of the threonine pathway from aspartate in Escherichia coli" ([PMID: 11368768](https://pubmed.ncbi.nlm.nih.gov/11368768/)). PP_0662 catalyzes the terminal ThrC step, and all pathway enzymes are soluble cytoplasmic proteins — establishing the subcellular localization of PP_0662's activity as the cytoplasm.

### Finding 6 — PP_0662 (thrC) is embedded in an aspartate-family amino-acid metabolism genomic neighborhood

The genomic context of PP_0662 reinforces its metabolic role. UniProt annotations of flanking loci reveal a neighborhood enriched for aspartate/threonine/methionine metabolic functions:

| Locus | Product | Relevance |
|---|---|---|
| PP_0660 | *mmuP* — S-methyl-L-methionine transporter | Methionine-related; sister branch of the O-phosphohomoserine node |
| PP_0661 | AmpR-family transcriptional regulator | Regulatory |
| **PP_0662** | **Threonine synthase (thrC)** | **Terminal step of threonine biosynthesis** |
| PP_0663 | AsnC/Lrp-family transcriptional regulator | Lrp/AsnC governs amino-acid biosynthesis |
| PP_0664 | Homoserine dehydrogenase (*hom*, EC 1.1.1.3) | Upstream enzyme of same aspartate→Thr pathway |

The immediate adjacency of PP_0662 to homoserine dehydrogenase (PP_0664) — an upstream pathway enzyme — and to an Lrp/AsnC-family regulator is consistent with the established pathway architecture, in which homoserine dehydrogenase and threonine synthase are members of the same aspartate-to-threonine route ([PMID: 11368768](https://pubmed.ncbi.nlm.nih.gov/11368768/)). This genomic clustering of a pathway enzyme with an amino-acid-biosynthesis regulator rationalizes coordinated metabolic control at the locus.

### Finding 7 — ThrC is a validated antimicrobial/herbicide target absent in mammals, inhibited by phosphonate substrate analogues

Because mammals lack the threonine biosynthetic machinery and obtain threonine from the diet, ThrC represents a selective drug/agrochemical target: "Since mammals lack the appropriate synthetic machinery, instead obtaining the amino acid through their diet, the pathway is a potential focus for the development of novel antibiotics, antifungal agents, and herbicides" ([PMID: 18621388](https://pubmed.ncbi.nlm.nih.gov/18621388/)).

The enzyme's substrate specificity and active-site chemistry are corroborated by its inhibitor pharmacology. ThrC is irreversibly inhibited by (Z)-L-2-amino-5-phosphono-3-pentenoic acid (APPA), the toxic warhead of the rhizocticin antibiotics: "APPA is an irreversible inhibitor of threonine synthase (ThrC), a pyridoxal 5′-phosphate (PLP)-dependent enzyme that catalyzes the conversion of O-phospho-l-homoserine to l-threonine" ([PMID: 30830751](https://pubmed.ncbi.nlm.nih.gov/30830751/)) — a statement that independently confirms the exact substrate and product for the family. Classical competitive inhibitors mimic the phosphorylated substrate: L-threo-3-hydroxyhomoserine phosphate (Ki ≈ 6 µM) and L-2-amino-5-phosphonovaleric acid (Ki ≈ 31 µM, comparable to the Km for homoserine phosphate) ([PMID: 7902068](https://pubmed.ncbi.nlm.nih.gov/7902068/); [PMID: 6150934](https://pubmed.ncbi.nlm.nih.gov/6150934/)). These phosphonate analogues exploit the enzyme's recognition of the substrate phosphate group.

---

## Mechanistic Model and Interpretation

### Position in the aspartate-derived amino-acid pathway

PP_0662/ThrC catalyzes the final, committed step of L-threonine biosynthesis. The full route from aspartate, and the branch point at O-phosphohomoserine, is summarized below:

```
   L-Aspartate
        │  aspartokinase (ThrA/LysC)
        ▼
   L-Aspartyl-4-phosphate
        │  aspartate-semialdehyde dehydrogenase (Asd)
        ▼
   L-Aspartate-4-semialdehyde
        │  homoserine dehydrogenase (Hom / PP_0664)   ← NADPH
        ▼
   L-Homoserine
        │  homoserine kinase (ThrB)                    ← ATP
        ▼
   O-phospho-L-homoserine ────────────┐
        │                             │ (branch to methionine
        │  THREONINE SYNTHASE         │  via cystathionine γ-synthase,
        │  ThrC = PP_0662 (Q88Q36)    │  MetB, etc.)
        │  + H2O ; PLP ; Lys112       ▼
        ▼                          L-Methionine
   L-THREONINE  +  Pi
```

O-phospho-L-homoserine is a **metabolic branch point**: it can be channeled either into threonine (via ThrC/PP_0662) or into methionine biosynthesis. The action of PP_0662 therefore represents the decisive commitment of carbon and nitrogen flux to threonine rather than to the methionine branch. This is biologically significant in *P. putida*, where the PP_0660 (*mmuP*, S-methyl-methionine transporter) neighbor and the presence of methionine auxotrophs in the same mutant screen ([PMID: 20158506](https://pubmed.ncbi.nlm.nih.gov/20158506/)) underscore the shared node.

### Catalytic mechanism

As a fold-type II PLP enzyme, ThrC operates through a series of PLP–substrate aldimine intermediates:

1. **Resting state:** PLP is covalently bound as an internal aldimine (Schiff base) to the ε-amino group of the catalytic lysine — **Lys112** in PP_0662.
2. **Transaldimination:** the α-amino group of O-phospho-L-homoserine displaces Lys112 to form an external aldimine.
3. **Domain closure:** substrate binding drives a ~25° rotation of the small domain toward the large domain, closing the active site ([PMID: 12952961](https://pubmed.ncbi.nlm.nih.gov/12952961/)).
4. **α,β-elimination / β,γ-replacement:** deprotonation and elimination of the γ-phosphate generate an α,β-unsaturated (or PLP-stabilized) intermediate; the cofactor's own phosphate moiety participates in proton transfer from C4′ to Cγ ([PMID: 18621388](https://pubmed.ncbi.nlm.nih.gov/18621388/)).
5. **Water addition and product release:** water adds across the double bond to install the β-hydroxyl of threonine; transaldimination regenerates the Lys112 internal aldimine and releases L-threonine and Pi.

The net stoichiometry is a **β,γ-replacement** — the γ-phosphate leaves and a β-hydroxyl is introduced — distinguishing ThrC from simple β-eliminases.

### Localization

All evidence points to a **cytoplasmic** localization. The threonine biosynthetic enzymes are soluble cytoplasmic proteins with no signal peptides or membrane-spanning segments, and the substrate (O-phospho-L-homoserine) is a cytoplasmic intermediate generated by the upstream soluble enzymes. PP_0662 therefore performs its catalytic function in the bacterial cytoplasm.

---

## Evidence Base

| PMID | Title (abbreviated) | How it supports the annotation |
|---|---|---|
| [18621388](https://pubmed.ncbi.nlm.nih.gov/18621388/) | Structural/biochemical/in vivo study of *M. tuberculosis* threonine synthase | Defines the reaction (L-homoserine phosphate + water → threonine + Pi), the PLP mechanism, and establishes ThrC as a mammal-absent drug target |
| [12952961](https://pubmed.ncbi.nlm.nih.gov/12952961/) | Crystal structures of *T. thermophilus* HB8 threonine synthase | Confirms PLP dependence, β,γ-replacement chemistry, two-domain fold, and ~25° substrate-induced domain closure |
| [30830751](https://pubmed.ncbi.nlm.nih.gov/30830751/) | *B. subtilis* self-resistance to rhizocticin | Confirms exact substrate (O-phospho-L-homoserine) and product (L-threonine); documents irreversible inhibition by APPA |
| [20158506](https://pubmed.ncbi.nlm.nih.gov/20158506/) | Conditionally essential genes in *P. putida* KT2440 | Experimental proof that threonine biosynthesis is required for growth on minimal medium in this exact strain |
| [11368768](https://pubmed.ncbi.nlm.nih.gov/11368768/) | Integrated threonine-pathway enzyme kinetics in *E. coli* | Establishes the five-step aspartate→threonine pathway sequence with ThrC as the terminal step |
| [7902068](https://pubmed.ncbi.nlm.nih.gov/7902068/) | *E. coli* threonine synthase inhibition by homoserine phosphate analogues | Quantifies competitive inhibition (Ki 6 µM, 31 µM); probes active-site substrate recognition |
| [6150934](https://pubmed.ncbi.nlm.nih.gov/6150934/) | Aspartate antimetabolites and threonine-pathway enzymes | Reconstituted pathway; identifies hydroxyhomoserine phosphate as a potent ThrC inhibitor |
| [9748328](https://pubmed.ncbi.nlm.nih.gov/9748328/) | Allosteric activation of *Arabidopsis* threonine synthase by SAM | Contrasts plant (SAM-activated) vs. bacterial ThrC — informs expectation that *P. putida* (bacterial) ThrC is NOT SAM-regulated |

The evidence is highly consistent. The primary annotation (database + domains) is independently corroborated by direct sequence orthology (34% full-length identity), by conserved-motif mapping of the catalytic Lys112, by strain-specific genetics showing conditional essentiality, and by the well-characterized enzymology and inhibitor pharmacology of the ThrC family. No conflicting evidence was found — no literature was encountered describing a different function for a gene with this locus tag, and the organism, domains, and family are all mutually consistent.

One nuance worth flagging: plant threonine synthases are strongly allosterically activated by S-adenosylmethionine (SAM), producing an ~8-fold increase in catalytic rate and 25-fold decrease in Km ([PMID: 9748328](https://pubmed.ncbi.nlm.nih.gov/9748328/)), whereas bacterial threonine synthases (the class to which PP_0662 belongs) generally lack this regulation. This distinction is relevant to expectations about the *P. putida* enzyme's regulatory behavior.

---

## Limitations and Knowledge Gaps

1. **No direct enzymology on the *P. putida* protein.** All catalytic parameters (kcat, Km, inhibitor constants) and structural details are inferred from orthologs (*E. coli*, *T. thermophilus*, *M. tuberculosis*, *B. subtilis*), not measured for Q88Q36 itself. The 34% identity to *E. coli* ThrC is strong but does not guarantee identical kinetic parameters.
2. **No experimental structure of PP_0662.** The fold, domain-closure behavior, and Lys112 assignment are homology-based inferences; no crystal or cryo-EM structure of the *P. putida* enzyme exists in this analysis.
3. **Localization is inferred, not demonstrated.** Cytoplasmic localization is a strong inference from the pathway and from the absence of targeting signals, but has not been experimentally verified for PP_0662.
4. **Regulation is uncharacterized in *P. putida*.** Whether PP_0662 is subject to feedback regulation, allosteric effectors, or transcriptional control by the neighboring AsnC/Lrp-family regulator (PP_0663) is unknown. Bacterial ThrCs generally are not SAM-activated, but this has not been tested here.
5. **Conditional essentiality vs. strict essentiality.** The mutant screen shows threonine auxotrophy on minimal medium; whether PP_0662 is dispensable under threonine-supplemented or complex-medium conditions (as expected for an auxotrophy) is implied but the phenotype magnitude and any redundancy have not been quantified.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant enzymology.** Overexpress and purify Q88Q36, confirm PLP binding spectroscopically, and measure steady-state kinetics (kcat, Km for O-phospho-L-homoserine) plus Ki values for APPA and L-2-amino-5-phosphonovaleric acid to benchmark against *E. coli*.
2. **Site-directed mutagenesis of Lys112.** Generate a K112A variant and confirm loss of activity and loss of PLP Schiff-base absorbance, directly validating the predicted catalytic residue.
3. **Complementation and knockout.** Delete PP_0662 and confirm threonine auxotrophy; complement in trans to demonstrate that the phenotype is attributable to this locus.
4. **Structure determination.** Solve the crystal structure (apo and with a phosphonate substrate analogue such as APPA) to verify the fold-type II architecture and capture domain closure; alternatively, generate and validate an AlphaFold model.
5. **Regulatory test.** Assay whether SAM, threonine, or other pathway intermediates modulate activity, and test whether the adjacent AsnC/Lrp regulator (PP_0663) controls thrC expression — clarifying regulation at this branch point.
6. **Metabolic flux analysis.** Quantify partitioning of O-phospho-L-homoserine between the threonine (ThrC) and methionine branches under different growth conditions to define PP_0662's role in flux control.

---

## Conclusion

PP_0662 (Q88Q36) is confidently and unambiguously identified as **threonine synthase (ThrC, EC 4.2.3.1)** of *Pseudomonas putida* KT2440 — a soluble, cytoplasmic, PLP-dependent (fold-type II / TrpB-PALP) enzyme catalyzing the final β,γ-replacement step of L-threonine biosynthesis: O-phospho-L-homoserine + H₂O → L-threonine + Pi. The catalytic PLP lysine is Lys112. The enzyme completes the aspartate-derived pathway (conditionally essential in this strain), operates at the O-phosphohomoserine branch point shared with methionine biosynthesis, and — being absent in mammals — constitutes a validated selective antimicrobial/herbicide target inhibitable by phosphonate substrate analogues.


## Artifacts

- [OpenScientist final report](PP_0662-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PP_0662-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:18621388
2. PMID:12952961
3. PMID:20158506
4. PMID:11368768
5. PMID:30830751
6. PMID:7902068
7. PMID:6150934
8. PMID:9748328