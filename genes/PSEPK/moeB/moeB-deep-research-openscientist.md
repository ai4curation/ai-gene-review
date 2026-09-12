---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-20T18:25:35.004328'
end_time: '2026-07-20T18:48:55.072666'
duration_seconds: 1400.07
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: moeB
  gene_symbol: moeB
  uniprot_accession: Q88PW3
  protein_description: 'RecName: Full=Molybdopterin-synthase adenylyltransferase {ECO:0000256|ARBA:ARBA00073635};
    EC=2.7.7.80 {ECO:0000256|ARBA:ARBA00066884}; AltName: Full=MoaD protein adenylase
    {ECO:0000256|ARBA:ARBA00078531}; AltName: Full=Molybdopterin-converting factor
    subunit 1 adenylase {ECO:0000256|ARBA:ARBA00075110}; AltName: Full=Sulfur carrier
    protein MoaD adenylyltransferase {ECO:0000256|ARBA:ARBA00075328};'
  gene_info: Name=moeB {ECO:0000313|EMBL:AAN66360.1}; OrderedLocusNames=PP_0735 {ECO:0000313|EMBL:AAN66360.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the HesA/MoeB/ThiF family.
  protein_domains: ThiF/MoeB/HesA. (IPR045886); ThiF_NAD_FAD-bd. (IPR000594); Ubiquitin-activating_enz.
    (IPR035985); ThiF (PF00899)
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
  path: moeB-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: moeB-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88PW3
- **Protein Description:** RecName: Full=Molybdopterin-synthase adenylyltransferase {ECO:0000256|ARBA:ARBA00073635}; EC=2.7.7.80 {ECO:0000256|ARBA:ARBA00066884}; AltName: Full=MoaD protein adenylase {ECO:0000256|ARBA:ARBA00078531}; AltName: Full=Molybdopterin-converting factor subunit 1 adenylase {ECO:0000256|ARBA:ARBA00075110}; AltName: Full=Sulfur carrier protein MoaD adenylyltransferase {ECO:0000256|ARBA:ARBA00075328};
- **Gene Information:** Name=moeB {ECO:0000313|EMBL:AAN66360.1}; OrderedLocusNames=PP_0735 {ECO:0000313|EMBL:AAN66360.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the HesA/MoeB/ThiF family.
- **Key Domains:** ThiF/MoeB/HesA. (IPR045886); ThiF_NAD_FAD-bd. (IPR000594); Ubiquitin-activating_enz. (IPR035985); ThiF (PF00899)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "moeB" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'moeB' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **moeB** (gene ID: moeB, UniProt: Q88PW3) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: MoeB (Q88PW3, PP_0735) in *Pseudomonas putida* KT2440

**Gene:** moeB (OrderedLocusName PP_0735) · **UniProt:** Q88PW3 · **EC:** 2.7.7.80
**Organism:** *Pseudomonas putida* strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440 (PSEPK)
**Protein family:** HesA/MoeB/ThiF (Pfam PF00899; InterPro IPR045886, IPR000594, IPR035985)

---

## Summary

**MoeB (Q88PW3, locus PP_0735) of *Pseudomonas putida* KT2440 is a cytoplasmic molybdopterin-synthase adenylyltransferase (EC 2.7.7.80), an E1-like enzyme that uses ATP to activate the ubiquitin-like sulfur-carrier protein MoaD.** Its primary catalytic function is to adenylylate the conserved C-terminal Gly-Gly motif of MoaD, forming a MoaD-acyl-adenylate (MoaD-AMP) intermediate. This activated intermediate is the obligatory precursor for thiocarboxylation of the MoaD C-terminus, which in turn supplies the two sulfur atoms of the molybdopterin dithiolene group. MoeB therefore performs the ATP-dependent "recharging" step of the MoaD sulfur relay within Step 2 of molybdenum-cofactor (Moco) biosynthesis — the conversion of cyclic pyranopterin monophosphate (precursor Z) to molybdopterin (MPT).

The functional assignment rests on two mutually reinforcing lines of evidence. First, the biochemistry and structural biology of the *Escherichia coli* ortholog MoeB are exceptionally well characterized: crystal structures of the MoeB–MoaD complex captured the apo, ATP-bound, and MoaD-adenylate states, directly demonstrating adenylylation chemistry, and mutagenesis of the terminal glycine of MoaD abolishes MoaD-AMP formation. Second, direct sequence analysis of Q88PW3 confirms it is a canonical, "classic" MoeB: the 251-residue protein carries the diagnostic Rossmann-like GxGxxG ATP-binding motif and the paired CxxC zinc-binding cysteine motifs of the ThiF/MoeB/HesA family, has the same length as *E. coli* MoeB (~249 aa), and lacks any C-terminal rhodanese domain. A global alignment against *E. coli* MoeB (P12282) yields ~54% identity over the full length, far above the homology "twilight zone," establishing Q88PW3 as a high-confidence cross-genus ortholog to which the experimentally validated function can be transferred with confidence.

Beyond its narrow enzymatic role, MoeB occupies a position of considerable biological and evolutionary importance. The MoeB–MoaD system is the mechanistic and evolutionary ancestor of the eukaryotic ubiquitin-activating (E1) enzyme system, sharing the same adenylation chemistry and protein fold despite negligible sequence similarity. Functionally, because Moco is the essential cofactor for more than 50 molybdoenzymes catalyzing redox reactions across the carbon, nitrogen, and sulfur cycles (e.g., nitrate reductase, formate dehydrogenase), MoeB activity is indirectly required for the function of the entire molybdoenzyme complement of the cell. This report synthesizes the experimental, structural, sequence, and evolutionary evidence supporting these conclusions.

---

## Gene/Protein Identity Verification

Before presenting findings, the mandatory identity checks were completed and all passed:

| Verification Item | Result |
|---|---|
| Gene symbol "moeB" matches protein description | ✅ Yes — "molybdopterin-synthase adenylyltransferase" is the canonical MoeB function |
| Organism correct | ✅ *Pseudomonas putida* KT2440 (ATCC 47054 / DSM 6125 / NCIMB 11950) |
| Protein family/domains align with literature | ✅ HesA/MoeB/ThiF family (PF00899); ThiF/MoeB/HesA (IPR045886); confirmed by sequence motif analysis |
| Literature refers to same gene (not a same-symbol paralog) | ✅ No ambiguity — "moeB" is a well-defined molybdenum-cofactor biosynthesis gene |

**Note on the gene name:** The UniProt record lists the gene name as `moeB`, while the protein carries EC 2.7.7.80 and several alternative names (MoaD protein adenylase; molybdopterin-converting factor subunit 1 adenylase; sulfur carrier protein MoaD adenylyltransferase). All of these describe the same activity — ATP-dependent adenylylation of the MoaD sulfur carrier — so there is no ambiguity. The gene symbol, the EC number, the protein family, and the direct sequence analysis are all mutually consistent. This is a genuine MoeB, not a same-symbol paralog from another organism.

---

## Key Findings

### Finding 1 — Primary function: MoeB is an ATP-dependent adenylyltransferase that activates the MoaD C-terminus

MoeB (Q88PW3) is a **molybdopterin-synthase adenylyltransferase** (EC 2.7.7.80). Its defining catalytic activity is the ATP-dependent adenylylation of the C-terminal Gly-Gly motif of the sulfur-carrier protein MoaD, producing a MoaD-acyl-adenylate (MoaD-AMP) intermediate. This function is directly established for the *E. coli* ortholog by both structural and biochemical work. Lake et al. (2001) solved crystal structures of the MoeB–MoaD complex in three functionally informative states — apo, ATP-bound, and the MoaD-adenylate product state — and explicitly reported that, *"Similar to the E1 enzymes, MoeB activates the C terminus of MoaD to form an acyl-adenylate"* ([PMID: 11713534](https://pubmed.ncbi.nlm.nih.gov/11713534/)).

The chemistry hinges on the extreme C-terminal glycine of MoaD (Gly81 in *E. coli*), which provides the carboxylate that attacks the α-phosphate of ATP. Schmitz et al. (2007) showed by mutagenesis that this terminal residue is indispensable: *"the terminal MoaD residue (Gly81) is important for transfer of sulfur to precursor Z and essential for formation of the MoaD-AMP complex"* ([PMID: 17223713](https://pubmed.ncbi.nlm.nih.gov/17223713/)). The abolition of MoaD-AMP formation upon Gly81 mutation demonstrates that adenylylation occurs precisely at the MoaD C-terminus and confirms the mechanistic model.

Because Q88PW3 is a high-confidence ortholog of *E. coli* MoeB (see Finding 6) and possesses the required ATP-binding machinery (see Finding 5), this experimentally validated adenylyltransferase activity is transferred to the *P. putida* protein with high confidence. **The reaction catalyzed is: MoaD-COO⁻ + ATP → MoaD-CO-AMP (MoaD-adenylate) + PPᵢ.** The substrate specificity is narrow and defined by protein-protein recognition: the enzyme is specific for its cognate ubiquitin-fold sulfur carrier MoaD, engaging its C-terminal di-glycine motif.

### Finding 2 — Biological process: MoeB recharges the MoaD sulfur carrier in Step 2 of molybdenum-cofactor biosynthesis

MoeB's adenylylation activity is not an end in itself; it is the ATP-priming step of a cyclic sulfur-relay that builds the dithiolene group of molybdopterin. During MPT formation, MoaD alternates between two distinct heterotetrameric complexes. Schmitz et al. (2007) described this cycle precisely: *"MoaD cycles between two different heterotetrameric complexes, one with MoaE to form MPT synthase and the other with MoeB, a protein similar to E1 in the ubiquitin pathway, to regenerate its transferrable sulfur"* ([PMID: 17223713](https://pubmed.ncbi.nlm.nih.gov/17223713/)). In the MoaD–MoaE (MPT synthase) complex, MoaD delivers sulfur to precursor Z; once depleted, MoaD dissociates and binds MoeB, which re-activates its C-terminus for a fresh round of thiocarboxylation.

The MoeB-generated MoaD-adenylate is the direct substrate for the next chemical step. Lake et al. (2001) established the downstream fate: *"Subsequently, a sulphurtransferase converts the MoaD acyl-adenylate to a thiocarboxylate that acts as the sulphur donor during Moco biosynthesis"* ([PMID: 11713534](https://pubmed.ncbi.nlm.nih.gov/11713534/)). The importance of the thiocarboxylated form was demonstrated by Gutzke et al. (2001), who generated carboxylated and thiocarboxylated MoaD *in vitro* and found that *only* the thiocarboxylated MPT synthase complex could convert precursor Z to MPT ([PMID: 11459846](https://pubmed.ncbi.nlm.nih.gov/11459846/)). Finally, Daniels et al. (2008) traced the ultimate fate of the sulfur: MPT formation *"involves the transfer of sulfur atoms from a C-terminal MoaD thiocarboxylate to the C-1' and C-2' positions of precursor Z"* ([PMID: 18092812](https://pubmed.ncbi.nlm.nih.gov/18092812/)), forming the two dithiolene sulfurs that ultimately coordinate molybdenum.

MoeB thus performs the essential ATP-consuming step that keeps the MoaD sulfur carrier in a re-usable state. Without MoeB, MoaD cannot be thiocarboxylated, MPT synthase cannot regenerate, and molybdopterin cannot be made.

### Finding 3 — Evolutionary role: MoeB–MoaD is the ancestor of ubiquitin activation

MoeB belongs to the **HesA/MoeB/ThiF family** (Pfam PF00899; InterPro IPR045886, IPR000594, IPR035985). This family is famous not only for its metabolic role but for its deep evolutionary connection to eukaryotic protein modification. MoaD adopts the ubiquitin fold and carries a C-terminal Gly-Gly motif exactly like ubiquitin, and MoeB catalyzes the same adenylation chemistry as the ubiquitin-activating E1 enzymes — despite the two systems sharing little primary sequence similarity. Lake et al. (2001) drew the explicit conclusion: *"These findings suggest that ubiquitin and E1 are derived from two ancestral genes closely related to moaD and moeB"* ([PMID: 11713534](https://pubmed.ncbi.nlm.nih.gov/11713534/)).

The same ancestral chemistry recurs in related bacterial sulfur-transfer systems. Appleyard et al. (1998), in their characterization of the *Aspergillus* cnxF gene, noted that MoeB is *"similar in sequence to the prokaryotic proteins MoeB, which is thought to encode molybdopterin synthase sulfurylase, ThiF, required for thiamine biosynthesis, and HesA, involved in heterocyst formation, as well as eukaryotic ubiquitin-activating protein E1"* ([PMID: 9614089](https://pubmed.ncbi.nlm.nih.gov/9614089/)). ThiF/ThiS (thiamine biosynthesis) is the direct mechanistic parallel in a different pathway — ThiF adenylylates the ThiS sulfur carrier just as MoeB adenylylates MoaD. This family membership is the basis for the domain-based annotation of Q88PW3 and reinforces the functional assignment: the ThiF/MoeB/HesA fold *is* the adenylyltransferase machine.

### Finding 4 — Localization and pathway context: cytoplasmic sulfur relay enabling all molybdoenzyme activity

Moco biosynthesis, including the MoeB-catalyzed MoaD-activation step, occurs in the **cytoplasm**. Mendel & Leimkühler (2015) describe the pathway as *"an ancient, ubiquitous, and highly conserved pathway leading to the biochemical activation of molybdenum"* ([PMID: 24980677](https://pubmed.ncbi.nlm.nih.gov/24980677/)). This conservation is what justifies transferring the *E. coli* mechanism to *P. putida*: the pathway components and chemistry are essentially invariant across bacteria.

The downstream product Moco is the cofactor for a large and diverse enzyme set — more than 50 molybdoenzymes catalyzing redox reactions in carbon, nitrogen, and sulfur metabolism, including nitrate reductase and formate dehydrogenase. In *P. putida*, a metabolically versatile soil bacterium, these enzymes support respiratory and anaerobic/microaerobic metabolic flexibility. MoeB is thus a "linchpin" upstream enzyme: its activity is indirectly required for the function of the entire molybdoenzyme complement.

Importantly, MoeB's sulfur-relay chemistry does not operate in isolation. Leimkühler (2017) showed that *"the pathways for FeS cluster assembly and thio-modifications of tRNA are connected to Moco biosynthesis by sharing the same protein components"* ([PMID: 28284029](https://pubmed.ncbi.nlm.nih.gov/28284029/)). The persulfide-generating and sulfurtransferase machinery that ultimately thiocarboxylates MoaD-AMP is shared with FeS-cluster assembly (IscS-type cysteine desulfurases) and tRNA thiolation, placing MoeB within a broader, integrated cellular sulfur-trafficking network.

### Finding 5 — Direct sequence evidence: Q88PW3 carries the diagnostic ThiF/MoeB catalytic motifs and is a "classic" MoeB

Direct analysis of the 251-residue Q88PW3 sequence provides organism-specific confirmation of the annotation rather than relying solely on database inheritance. Three diagnostic features were identified:

1. **Rossmann-like nucleotide (ATP)-binding motif:** A `GLGGLG` sequence at residues 36–41 matches the canonical GxGxxG P-loop-like motif that binds ATP — the functional hallmark of the ThiF/MoeB/HesA family.
2. **Paired metal (zinc)-binding CxxC motifs:** Two cysteine-pair motifs — `CYHC` (C171–C174) and `CTVC` (C243–C246, at the extreme C-terminus) — match the structural zinc-binding site characteristic of *E. coli* MoeB.
3. **Architecture:** At 251 aa, the protein closely matches *E. coli* MoeB (~249 aa) and comprises a single ThiF domain with **no C-terminal rhodanese (sulfurtransferase) extension**. This distinguishes it from MoeZ/MoeB-rhodanese fusion enzymes, which append a sulfurtransferase domain to transfer sulfur directly. Q88PW3 is therefore a "classic" adenylyltransferase that requires a separate downstream sulfurtransferase to complete thiocarboxylation.

These observations are consistent with the family definition given by Appleyard et al. (1998): *"Sequence comparisons indicate the presence of one and possibly two nucleotide binding motifs, Gly-X-Gly-X-X-Gly, as well as two metal binding Cys-X-X-Cys motifs"* ([PMID: 9614089](https://pubmed.ncbi.nlm.nih.gov/9614089/)). The ATP-binding motif detected in Q88PW3 is precisely the element required for the adenylation activity described by Lake et al. (2001): *"MoeB activates the C terminus of MoaD to form an acyl-adenylate"* ([PMID: 11713534](https://pubmed.ncbi.nlm.nih.gov/11713534/)).

### Finding 6 — Q88PW3 is a high-confidence ortholog of experimentally characterized *E. coli* MoeB (~54% identity)

The strongest single piece of evidence for functional transfer is the global sequence identity between Q88PW3 and the biochemically/structurally characterized *E. coli* MoeB (P12282). A Needleman-Wunsch global alignment of the two proteins (251 aa vs. 249 aa) yields **133 identical residues = 53.8% identity** over aligned columns (53.0% over the full Q88PW3 length), with near-identical length and no large insertions or deletions (alignment length 253).

This level of identity is far above the ~25–30% "twilight zone" where homology becomes uncertain, and is typical of unambiguous cross-genus orthologs that retain the same molecular function. Combined with the conserved catalytic motifs (Finding 5), the alignment allows the experimentally established activity of *E. coli* MoeB — *"MoeB activates the C terminus of MoaD to form an acyl-adenylate"* ([PMID: 11713534](https://pubmed.ncbi.nlm.nih.gov/11713534/)) — to be transferred to Q88PW3 with high confidence.

| Comparison | Value |
|---|---|
| Q88PW3 length | 251 aa |
| *E. coli* MoeB (P12282) length | 249 aa |
| Identical residues | 133 |
| % identity (aligned columns) | 53.8% |
| % identity (full Q88PW3 length) | 53.0% |
| Alignment length | 253 |
| Large indels | None |
| Homology confidence | High (well above twilight zone) |

---

## Mechanistic Model / Interpretation

The findings assemble into a single coherent mechanistic narrative. MoeB is the ATP-consuming "recharger" of a cyclic sulfur relay that constructs the molybdopterin dithiolene, the sulfur-bearing chelate that ultimately binds molybdenum in Moco.

```
   MOLYBDENUM COFACTOR BIOSYNTHESIS — STEP 2 (MPT formation)
   ==========================================================

        GTP  --(MoaA/MoaC)-->  Precursor Z (cyclic pyranopterin
                                            monophosphate, cPMP)
                                       |
                                       |  needs 2 sulfur atoms
                                       v
     +----------------------  MoaD sulfur-relay cycle  ---------------------+
     |                                                                      |
     |   MoaD-COO-  +  ATP                                                   |
     |        |                                                             |
     |        |  <=== MoeB (Q88PW3)  ADENYLYLTRANSFERASE (EC 2.7.7.80)      |
     |        v        [GLGGLG ATP-site; CxxC Zn sites]                     |
     |   MoaD-CO-AMP  (MoaD-adenylate)   + PPi                              |
     |        |                                                             |
     |        |  <=== sulfurtransferase (persulfide donor;                  |
     |        v         shared with FeS / tRNA-thiolation machinery)        |
     |   MoaD-COSH  (MoaD-thiocarboxylate)   + AMP                          |
     |        |                                                             |
     |        |  binds MoaE  ==> MPT SYNTHASE (MoaD2-MoaE2)                  |
     |        v                                                             |
     |   Sulfur transferred to C-1' and C-2' of precursor Z                 |
     |        |                                                             |
     |        v                                                             |
     |   MoaD-COO-  (spent carrier) ---> re-enters cycle at MoeB -----------+
                             |
                             v
                    MOLYBDOPTERIN (MPT, with dithiolene)
                             |
                       (+ Mo via MogA/MoeA)
                             v
                    MOLYBDENUM COFACTOR (Moco)
                             |
                             v
      >50 molybdoenzymes: nitrate reductase, formate dehydrogenase,
      DMSO reductase, etc. — C, N, S redox metabolism (cytoplasm/membrane)
```

Key interpretive points:

- **MoeB acts at a branch point of a cycle, not a linear step.** MoaD is a reusable carrier that shuttles between MoeB (recharge) and MoaE (delivery). MoeB's job is to reset the carrier for another round by installing the adenylate that makes thiocarboxylation possible.
- **The chemistry is E1-like.** The MoaD-AMP intermediate is chemically and structurally analogous to the ubiquitin-AMP intermediate formed by E1 enzymes. MoeB is, in effect, a primitive E1. This is not merely an analogy but a documented evolutionary ancestry ([PMID: 11713534](https://pubmed.ncbi.nlm.nih.gov/11713534/)).
- **Q88PW3 is the "classic" (non-fused) enzyme.** Because it lacks a rhodanese domain, it does not perform sulfur transfer itself; it requires a partner sulfurtransferase. This means the full pathway in *P. putida* depends on a separate persulfide-generating system, consistent with the shared-component model of Leimkühler (2017).
- **Localization is cytoplasmic**, and the downstream impact is genome-wide across the molybdoenzyme complement — but MoeB's own role is precise and biochemical, not pleiotropic in the regulatory sense.

---

## Evidence Base

| PMID | Study (abbreviated) | How it supports the annotation |
|---|---|---|
| [11713534](https://pubmed.ncbi.nlm.nih.gov/11713534/) | *Mechanism of ubiquitin activation revealed by the structure of a bacterial MoeB-MoaD complex* | **Cornerstone.** Crystal structures (apo, ATP-bound, MoaD-adenylate) directly show MoeB adenylylates MoaD C-terminus; establishes E1/ubiquitin evolutionary link and the sulfurtransferase → thiocarboxylate handoff. |
| [17223713](https://pubmed.ncbi.nlm.nih.gov/17223713/) | *Role of the C-terminal Gly-Gly motif of E. coli MoaD* | Mutagenesis shows terminal Gly81 is essential for MoaD-AMP formation; defines the MoaD cycling between MoeB and MoaE complexes. |
| [11459846](https://pubmed.ncbi.nlm.nih.gov/11459846/) | *Thiocarboxylation of molybdopterin synthase...* | Only thiocarboxylated MPT synthase converts precursor Z to MPT *in vitro*, validating the functional importance of the thiocarboxylate that MoeB's product enables. |
| [18092812](https://pubmed.ncbi.nlm.nih.gov/18092812/) | *Crystal structure of a molybdopterin synthase-precursor Z complex* | Traces sulfur transfer from MoaD thiocarboxylate to C-1'/C-2' of precursor Z, forming the dithiolene. |
| [9614089](https://pubmed.ncbi.nlm.nih.gov/9614089/) | *The Aspergillus nidulans cnxF gene...* | Defines the ThiF/MoeB/HesA/E1 family and the diagnostic GxGxxG and CxxC motifs found in Q88PW3. |
| [24980677](https://pubmed.ncbi.nlm.nih.gov/24980677/) | *The biosynthesis of the molybdenum cofactors* | Establishes the pathway as ancient, ubiquitous, highly conserved, and cytoplasmic — justifying cross-species transfer. |
| [28284029](https://pubmed.ncbi.nlm.nih.gov/28284029/) | *Shared function and moonlighting proteins in Moco biosynthesis* | Places MoeB's sulfur relay within shared FeS-cluster and tRNA-thiolation networks. |
| [25514355](https://pubmed.ncbi.nlm.nih.gov/25514355/) | *Assembly and catalysis of Mo/W formate dehydrogenases* | Illustrates a key downstream molybdoenzyme dependent on Moco (and thus on MoeB). |
| [31517366](https://pubmed.ncbi.nlm.nih.gov/31517366/) | *Regulation of Moco biosynthesis by Mo and Fe* | Context on how Moco/molybdoenzyme gene expression is regulated by metal availability. |
| [23317461](https://pubmed.ncbi.nlm.nih.gov/23317461/) | *Molybdenum cofactor in M. tuberculosis pathogenesis* | Shows physiological importance of Moco biosynthesis in a pathogen; supports broad relevance. |

**Consistency of the evidence:** All lines converge. The structural/biochemical *E. coli* data define the mechanism; the mutagenesis pins the chemistry to the MoaD C-terminus; the *in vitro* reconstitution confirms the downstream sulfur donation; the family/motif analyses confirm Q88PW3 possesses the required machinery; and the ~54% ortholog identity licenses the functional transfer to *P. putida*. No evidence contradicts the assignment.

---

## Limitations and Knowledge Gaps

1. **No direct experimental characterization of Q88PW3 itself.** The functional assignment is inferred from the *E. coli* ortholog (P12282) via high sequence identity (~54%) and conserved motifs. No published enzymatic assay, structure, or knockout of the *P. putida* PP_0735 protein was identified. The inference is strong but remains inferential for this specific protein.

2. **Identity of the *P. putida* partner proteins not confirmed here.** The cognate MoaD, MoaE, and the sulfurtransferase(s) that thiocarboxylate MoaD-AMP in *P. putida* were not explicitly mapped. The shared-component model ([PMID: 28284029](https://pubmed.ncbi.nlm.nih.gov/28284029/)) predicts an IscS-type cysteine desulfurase supplies the persulfide, but the specific *P. putida* genes were not verified.

3. **Zinc-binding assignment is inferred from motifs, not measured.** The two CxxC motifs are consistent with the *E. coli* structural zinc site, but metal occupancy in Q88PW3 was not experimentally determined.

4. **Regulation in *P. putida* is uncharacterized.** How PP_0735 expression responds to molybdenum/iron availability, oxygen, or growth conditions in *P. putida* specifically was not established (though general bacterial regulatory logic is reviewed in [PMID: 31517366](https://pubmed.ncbi.nlm.nih.gov/31517366/)).

5. **Physiological consequences of MoeB loss in *P. putida* not tested.** By inference, loss would abolish Moco and hence all molybdoenzyme activity (e.g., nitrate reductase, formate dehydrogenase), impairing anaerobic/microaerobic metabolism, but this has not been demonstrated for this strain.

---

## Proposed Follow-up Experiments / Actions

1. **Direct biochemical assay of recombinant Q88PW3.** Express and purify PP_0735, incubate with purified *P. putida* MoaD + ATP, and detect MoaD-AMP formation (mass spectrometry / native gel / ³²P-ATP). This would convert the inference to direct evidence.

2. **Genetic knockout / complementation.** Delete PP_0735 in *P. putida* KT2440 and assay for loss of molybdoenzyme activities (nitrate reductase, formate dehydrogenase, DMSO reductase). Complement with the *E. coli* moeB gene to confirm functional interchangeability predicted by orthology.

3. **Structural determination or AlphaFold modeling with validation.** Generate an AlphaFold model of Q88PW3 and use structural tools (e.g., superposition against the *E. coli* MoeB–MoaD complex from [PMID: 11713534](https://pubmed.ncbi.nlm.nih.gov/11713534/)) to confirm the ATP pocket and zinc site geometry; validate model confidence (pLDDT) at the active site.

4. **Map the *P. putida* Moco operon and partners.** Identify the co-transcribed/adjacent moaD, moaE, moaA/moaC, and the cysteine desulfurase supplying sulfur; confirm operon structure around PP_0735 to define the complete pathway in this organism.

5. **Metal-content analysis.** Determine zinc stoichiometry of purified Q88PW3 (ICP-MS) to confirm the structural zinc predicted by the CxxC motifs.

6. **Confirm absence of rhodanese/sulfurtransferase activity.** Test whether Q88PW3 requires a separate sulfurtransferase (as predicted for a "classic" MoeB) versus performing direct sulfur transfer, distinguishing it definitively from MoeZ-type fusion enzymes.

---

## Conclusion

MoeB (Q88PW3, PP_0735) in *Pseudomonas putida* KT2440 is a cytoplasmic, ATP-dependent molybdopterin-synthase adenylyltransferase (EC 2.7.7.80) of the HesA/MoeB/ThiF (E1-like) family. It activates the ubiquitin-like sulfur carrier MoaD by adenylylating its C-terminal Gly-Gly motif to form MoaD-AMP, the obligatory precursor for MoaD thiocarboxylation, thereby recharging the sulfur carrier in Step 2 of molybdenum-cofactor biosynthesis. This function — supported by structural and biochemical characterization of the *E. coli* ortholog, mutagenesis, *in vitro* reconstitution, family/motif analysis, and ~54% ortholog identity — makes MoeB indirectly essential for the activity of the cell's entire molybdoenzyme complement.


## Artifacts

- [OpenScientist final report](moeB-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](moeB-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:11713534
2. PMID:17223713
3. PMID:11459846
4. PMID:18092812
5. PMID:9614089
6. PMID:24980677
7. PMID:28284029
8. PMID:31517366