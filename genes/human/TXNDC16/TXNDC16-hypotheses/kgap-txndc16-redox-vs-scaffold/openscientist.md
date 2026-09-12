# TXNDC16/ERp90: Catalytic PDI-Family Oxidoreductase or Non-Catalytic ER-Luminal Scaffold?

## Summary

**TXNDC16/ERp90 is a non-catalytic ER-luminal scaffold/adaptor protein, not a catalytic oxidoreductase.** Despite belonging to the protein disulfide isomerase (PDI) superfamily by virtue of its multiple thioredoxin-like folds, human TXNDC16 (UniProt Q9P2K2, 825 amino acids) completely lacks the canonical CXXC active-site motifs that are the hallmark of catalytically active PDI-family members. Its ten mature cysteines are arranged in spacings (CX6C, CX8C) incompatible with thioredoxin-fold redox catalysis, and its only annotated disulfide bond (C449–C456) has structural rather than catalytic character. No purified-protein redox assay, cysteine-to-serine mutagenesis study, disulfide-state trapping experiment, or in vitro enzymatic characterization has been published in the 15 years since the protein was first described.

The functional evidence that does exist positions TXNDC16 squarely in the ER-associated degradation (ERAD) pathway as a substrate recruiter. Its co-immunoprecipitation with ERFAD — a luminal flavoprotein that itself interacts with the ERAD machinery components SEL1L, OS-9, and the catalytic reductase ERdj5 — indicates a hand-off role in which TXNDC16 captures or presents misfolded substrates for delivery to the retrotranslocation complex. The original characterizing paper explicitly proposed this model, stating that "the function of ERp90 is related to substrate recruitment or delivery to the ERAD retrotranslocation machinery by ERFAD" ([PMID: 21359175](https://pubmed.ncbi.nlm.nih.gov/21359175/)).

Based on the totality of available evidence — sequence analysis, domain architecture, absence of catalytic motifs, interaction data, and the complete absence of direct enzymatic evidence — the only defensible Gene Ontology molecular function annotation for TXNDC16 is **protein binding (GO:0005515)** in the context of ERAD substrate recruitment. Annotation as an oxidoreductase (GO:0016491), protein disulfide isomerase (GO:0003756), or disulfide oxidoreductase (GO:0015036) is not supported by any direct experimental evidence and would constitute unjustified inference from family membership alone.

---

## Key Findings

### Finding 1: TXNDC16 Completely Lacks Canonical CXXC Active-Site Motifs

The defining feature of catalytically active PDI-family members is the CXXC motif — two cysteines separated by exactly two intervening residues — located at the N-terminus of an alpha-helix within the thioredoxin fold. This motif enables the reversible formation of a disulfide bond whose reduction potential is tuned by the intervening residues, allowing the protein to catalyze oxidation, reduction, or isomerization of substrate disulfides.

Systematic computational analysis of the full human TXNDC16 sequence (Q9P2K2, 825 amino acids) reveals 10 cysteine residues in the mature protein at positions C51, C84, C93, C216, C226, C449, C456, C664, C767, and C821. Exhaustive regex searches for CXC, CXXC, and CXXXC motifs returned **zero matches**. The closest cysteine pairs are C84–C93 (CX8C spacing, with 8 intervening residues) and C449–C456 (CX6C spacing, with 6 intervening residues). Both spacings are far wider than the CXXC pattern required for thioredoxin-fold catalysis.

This absence is conserved across evolution: the mouse ortholog (UniProt Q7TN22) also completely lacks CXXC motifs, as do the zebrafish, cow, and rat orthologs. The original characterization by Riemer et al. (2011) explicitly acknowledged this, noting: *"While none of the Trx domains contain a canonical Cys-Xaa-Xaa-Cys active-site motif, other conserved cysteines could endow the protein with redox activity"* ([PMID: 21359175](https://pubmed.ncbi.nlm.nih.gov/21359175/)). Crucially, this speculative suggestion was never experimentally tested — by the original authors or by anyone subsequently.

The significance of CXXC absence cannot be overstated. The extensive literature on PDI-family catalysis demonstrates that the CXXC motif is not merely a conserved sequence feature but a mechanistic requirement. Studies on yeast PDI showed that mutation of the CXXC active sites to SGAS abolished catalytic function ([PMID: 9298979](https://pubmed.ncbi.nlm.nih.gov/9298979/)), and work on the CXXC motif in thioredoxin demonstrated that an enzymatic thiolate with appropriate reduction potential is "both necessary and sufficient for the formation of native disulfide bonds in the cell" ([PMID: 8654363](https://pubmed.ncbi.nlm.nih.gov/8654363/)). The crystal structure of a CXXC-containing thioredoxin variant (CVWC) confirmed that the motif's geometry directly tunes reduction potential through modulation of the N-terminal cysteine pKa ([PMID: 10489448](https://pubmed.ncbi.nlm.nih.gov/10489448/)).

{{figure:txndc16_domain_analysis.png|caption=Domain architecture comparison of TXNDC16/ERp90 versus canonical PDI-family members. TXNDC16 contains five thioredoxin-like domains but none harbor the CXXC active-site motif required for catalytic redox activity. Cysteine positions and spacings are shown, highlighting the absence of any catalytically competent motif.}}

### Finding 2: The C449–C456 Disulfide Is Structural, Not Catalytic

UniProt annotates a disulfide bond between C449 and C456, based on evidence from the original characterization ([PMID: 21359175](https://pubmed.ncbi.nlm.nih.gov/21359175/)). The motif is CADWSDVC — a CX6C pattern with six intervening residues. This spacing is conserved in the mouse ortholog (CADWSDIC).

Canonical catalytic CXXC disulfides are solvent-exposed at the end of an alpha-helix within the thioredoxin fold, where they undergo reversible oxidation and reduction during catalytic cycles. By contrast, CX6C disulfides are characteristic of structural bonds that stabilize the domain fold. Their larger loop size creates a geometrically distinct conformation incompatible with the concerted two-electron transfer mechanism of thioredoxin-fold catalysis. Both C449 and C456 reside within the sole canonical thioredoxin domain (approximately residues 392–495), which would be the domain most expected to exhibit catalytic activity if any existed. The fact that even this domain uses a CX6C structural disulfide rather than CXXC further argues against catalytic function.

Riemer et al. confirmed that *"Mature ERp90 contains 10 cysteine residues, of which at least some form intramolecular disulfides"* ([PMID: 21359175](https://pubmed.ncbi.nlm.nih.gov/21359175/)), but did not demonstrate that these disulfides undergo catalytic cycling — a critical distinction between structural and active-site disulfides.

### Finding 3: TXNDC16 Co-Immunoprecipitates with ERFAD, an ERAD-Pathway Flavoprotein

The strongest functional evidence for TXNDC16 comes from its physical interaction with ERFAD (ER flavoprotein associated with degradation). Riemer et al. (2011) demonstrated co-immunoprecipitation of ERp90/TXNDC16 with ERFAD in cultured human cells and proposed that *"the function of ERp90 is related to substrate recruitment or delivery to the ERAD retrotranslocation machinery by ERFAD"* ([PMID: 21359175](https://pubmed.ncbi.nlm.nih.gov/21359175/)).

This interaction is particularly informative when viewed in the context of the broader ERFAD complex. ERFAD itself was characterized by Riemer et al. (2009) as an ER-luminal flavoprotein that interacts with ERAD components SEL1L, OS-9, and ERdj5. The paper demonstrated that *"We also identify the ERAD components SEL1L, OS-9 and ERdj5, a known reductase of ERAD substrates, as interaction partners of ERFAD"* ([PMID: 19706418](https://pubmed.ncbi.nlm.nih.gov/19706418/)).

The presence of ERdj5 in this complex is highly significant. ERdj5 (also known as DNAJC10) is a bona fide catalytic reductase with demonstrated disulfide reductase activity — it cleaves disulfide bonds in misfolded proteins to facilitate their retrotranslocation through the Sec61 channel. Ushioda et al. (2008) showed that ERdj5 *"had a reductase activity, cleaved the disulfide bonds of misfolded proteins, and accelerated ERAD through its physical and functional associations with EDEM and an ER-resident chaperone BiP"* ([PMID: 18653895](https://pubmed.ncbi.nlm.nih.gov/18653895/)).

The fact that the ERFAD complex already contains a dedicated catalytic reductase (ERdj5) makes it unnecessary — and functionally redundant — for TXNDC16 to possess catalytic activity. Instead, TXNDC16 likely serves as a substrate recognition or hand-off component that captures misfolded glycoproteins and delivers them to ERFAD, which in turn connects them to ERdj5 for disulfide reduction prior to retrotranslocation.

### Finding 4: No In Vitro Enzymatic Assay Has Been Published for TXNDC16

Exhaustive PubMed searches for TXNDC16 oxidoreductase activity, ERp90 redox assays, cysteine mutant studies, insulin reduction assays, and disulfide-state mapping experiments returned zero results. The only two primary publications on TXNDC16 are:

1. **Riemer et al. (2011)** — characterization, ERFAD interaction, domain architecture ([PMID: 21359175](https://pubmed.ncbi.nlm.nih.gov/21359175/))
2. **Harz et al. (2014)** — meningioma autoantigen, secretion mechanisms ([PMID: 25122923](https://pubmed.ncbi.nlm.nih.gov/25122923/))

Neither reports any in vitro enzymatic assay, cysteine-to-serine mutagenesis, alkylation-based redox-state trapping, or substrate oxidation/reduction experiment. This is a critical absence. For comparison, other PDI-family members with confirmed catalytic function — PDIA1, ERp57, ERp72, ERdj5, TXNDC5 — have all been subjected to extensive biochemical characterization including insulin turbidimetric reduction assays, RNase A refolding/reoxidation assays, redox potential measurements, and cysteine mutant analyses. The complete lack of such data for TXNDC16 after 15 years suggests either that the community does not consider it a likely enzyme, or that attempts to demonstrate activity have failed and gone unreported.

The original authors themselves noted that *"other conserved cysteines could endow the protein with redox activity"* ([PMID: 21359175](https://pubmed.ncbi.nlm.nih.gov/21359175/)) — but notably did not test this hypothesis experimentally, despite having the protein in hand.

### Finding 5: GO Annotation Supports Only Protein Binding

Query of the Gene Ontology database for TXNDC16 (Q9P2K2) returns only 7 annotations: one molecular function term — **protein binding (GO:0005515)**, with IPI (Inferred from Physical Interaction) evidence from the ERFAD co-immunoprecipitation — and six cellular component terms (ER lumen by IDA, extracellular space/exosome). Critically absent are all enzymatic function annotations:

| GO Term | Description | Present for TXNDC16? |
|---------|-------------|----------|
| GO:0016491 | Oxidoreductase activity | **No** |
| GO:0003756 | Protein disulfide isomerase activity | **No** |
| GO:0015036 | Disulfide oxidoreductase activity | **No** |
| GO:0016853 | Isomerase activity | **No** |
| GO:0005515 | Protein binding | **Yes (IPI)** |

This annotation state reflects the careful curation practice of not extending enzymatic function annotations based solely on domain homology when direct evidence is lacking.

{{figure:txndc16_evidence_synthesis.png|caption=Comprehensive evidence synthesis for TXNDC16/ERp90 molecular function. The weight of evidence across multiple independent lines — sequence analysis, structural features, interaction data, functional assays (or lack thereof), and GO annotation — consistently supports a non-catalytic scaffold role rather than oxidoreductase activity.}}

---

## Mechanistic Model: TXNDC16 as an ERAD Substrate Adaptor

Based on the convergent evidence, we propose the following mechanistic model for TXNDC16 function within the ERAD pathway:

```
  Misfolded glycoprotein in ER lumen
          |
          v
  ┌───────────────────────┐
  │    TXNDC16/ERp90      │  ◄── Substrate recognition/capture
  │   (scaffold/adaptor)   │      via five thioredoxin-like domains
  │   No CXXC, no redox    │      (hydrophobic binding surfaces,
  │   5× Trx-like folds    │       analogous to PDI b/b' domains)
  └──────────┬────────────┘
             │  substrate hand-off (co-IP confirmed)
             v
  ┌───────────────────────┐
  │        ERFAD           │  ◄── Luminal FAD-containing
  │   (FOXRED2 flavoprotein)│      bridging adaptor
  └──────────┬────────────┘
             │
       ┌─────┴──────┐
       v             v
  ┌──────────┐  ┌───────────┐
  │  SEL1L   │  │   ERdj5   │  ◄── CATALYTIC reductase
  │  OS-9    │  │ (DNAJC10) │      (cleaves substrate disulfides
  │ (lectin  │  │   + BiP   │       via functional CXXC motifs)
  │ sorting) │  └─────┬─────┘
  └────┬─────┘        │
       │              │  reduced, unfolded substrate
       v              v
  ┌───────────────────────┐
  │    HRD1 / Sec61       │  ◄── Retrotranslocation channel
  │  (to cytosol for      │
  │   proteasomal          │
  │   degradation)         │
  └───────────────────────┘
```

### Key Features of This Model

1. **TXNDC16 as a multi-domain binding platform.** Its five thioredoxin-like domains — which retain the fold topology but lack catalytic CXXC motifs — provide extensive surface area for substrate binding. This is directly analogous to the well-characterized non-catalytic b and b' domains of canonical PDI (PDIA1), which serve as the primary substrate-binding sites. The crystal structure of PDI's b'-a' domains in complex with a substrate peptide showed that hydrophobic interactions on the b' domain (a non-catalytic Trx-like domain) mediate substrate recognition ([PMID: 26350503](https://pubmed.ncbi.nlm.nih.gov/26350503/)). TXNDC16 can be understood as a protein in which all five Trx-like domains resemble these non-catalytic substrate-binding domains.

2. **ERFAD as a bridging adaptor.** The ERFAD flavoprotein connects TXNDC16-bound substrates to the downstream ERAD machinery. ERFAD's own interaction partners (SEL1L, OS-9, ERdj5) represent the core retrotranslocation-associated complex ([PMID: 19706418](https://pubmed.ncbi.nlm.nih.gov/19706418/)).

3. **ERdj5 as the dedicated catalytic reductase.** ERdj5 possesses the actual CXXC-based reductase activity required to cleave substrate disulfide bonds before retrotranslocation ([PMID: 18653895](https://pubmed.ncbi.nlm.nih.gov/18653895/)). This division of labor — non-catalytic substrate recognition by TXNDC16 feeding into catalytic processing by ERdj5 — is consistent with the modular organization of ERAD complexes, where substrate selection, processing, and translocation functions are carried out by distinct proteins.

4. **TXNDC16's N-glycosylation** (at N460) suggests it may participate in glycan-mediated interactions within the ER lumen, potentially contributing to its ability to recognize misfolded glycoprotein clients.

---

## Distinguishing Direct Catalytic Evidence from Indirect Inference

A critical methodological principle in this analysis is the distinction between **direct evidence for catalytic function** and **indirect inference from family membership, localization, or interaction**:

| Evidence Type | What It Shows | What It Does NOT Show |
|--------------|---------------|----------------------|
| Thioredoxin-like domain folds | Structural similarity to catalytic PDIs | Catalytic activity (fold ≠ function) |
| ER lumen localization | Correct compartment for PDI activity | That the protein is enzymatically active |
| ERFAD co-immunoprecipitation | Physical interaction with ERAD complex | Catalytic role (could be scaffold/adaptor) |
| Presence of 10 cysteines | Potential for disulfide chemistry | That any cysteine participates in catalysis |
| PDI-family classification | Evolutionary relationship by fold homology | Conservation of catalytic function |
| Intramolecular disulfides | Structural stabilization | Catalytic cycling between redox states |

**None of the available evidence for TXNDC16 falls in the "direct catalytic evidence" category.** Direct evidence would require:
- In vitro oxidoreductase activity (e.g., insulin reduction, RNase refolding)
- Demonstration that cysteine mutations abolish a measurable enzymatic function
- Redox-state cycling of cysteines during substrate processing
- Measurement of reduction potential for any cysteine pair

All of these remain untested for TXNDC16.

---

## Evidence Base: Key Literature

### Primary Literature on TXNDC16

| Reference | Key Contribution | PMID |
|-----------|-----------------|------|
| Riemer et al. (2011), *"Identification of the PDI-family member ERp90 as an interaction partner of ERFAD"* | Original characterization; domain architecture; ERFAD co-IP; proposed scaffold function; noted absence of CXXC | [21359175](https://pubmed.ncbi.nlm.nih.gov/21359175/) |
| Harz et al. (2014), *"Secretion and immunogenicity of the meningioma-associated antigen TXNDC16"* | Secretion via masked KDEL; meningioma autoantigen; cytosolic localization | [25122923](https://pubmed.ncbi.nlm.nih.gov/25122923/) |

### ERFAD and ERAD Pathway Literature

| Reference | Relevance | PMID |
|-----------|-----------|------|
| Riemer et al. (2009), *"A luminal flavoprotein in ER-associated degradation"* | Characterized ERFAD and its interactions with SEL1L, OS-9, ERdj5 | [19706418](https://pubmed.ncbi.nlm.nih.gov/19706418/) |
| Ushioda et al. (2008), *"ERdj5 is required as a disulfide reductase for degradation of misfolded proteins in the ER"* | Demonstrated ERdj5's catalytic reductase activity in ERAD; showed it cleaves substrate disulfides | [18653895](https://pubmed.ncbi.nlm.nih.gov/18653895/) |

### CXXC Motif and PDI Catalysis Literature

| Reference | Relevance | PMID |
|-----------|-----------|------|
| Chivers et al. (1996), *"The CXXC motif: imperatives for the formation of native disulfide bonds in the cell"* | Established CXXC as necessary and sufficient for cellular disulfide bond formation | [8654363](https://pubmed.ncbi.nlm.nih.gov/8654363/) |
| Jäger et al. (1997), *"Active site mutations in yeast PDI cause DTT sensitivity and reduced protein folding"* | Showed CXXC→SGAS mutation abolishes PDI catalytic activity in vivo | [9298979](https://pubmed.ncbi.nlm.nih.gov/9298979/) |
| Ren et al. (1999), *"The CXXC motif: crystal structure of an active-site variant of E. coli thioredoxin"* | Structural basis for CXXC reduction potential; the motif tunes cysteine pKa | [10489448](https://pubmed.ncbi.nlm.nih.gov/10489448/) |
| Yagi-Utsumi et al. (2015), *"Structural basis of redox-dependent substrate binding of PDI"* | Showed how PDI's non-catalytic b' domain mediates substrate binding via hydrophobic interactions | [26350503](https://pubmed.ncbi.nlm.nih.gov/26350503/) |

### Contextual PDI-Family Reviews

The broader PDI-family literature consistently reinforces that catalytic activity requires CXXC motifs. Reviews of the 21-member human PDI family ([PMID: 35965326](https://pubmed.ncbi.nlm.nih.gov/35965326/), [PMID: 39319369](https://pubmed.ncbi.nlm.nih.gov/39319369/)) emphasize the thioredoxin domain CXXC motif as the signature of catalytic members. The recent ROB-Fold structural analysis explicitly used the CXXC motif as the anchor for identifying the conserved catalytic scaffold across PDI-family members ([PMID: 42253318](https://pubmed.ncbi.nlm.nih.gov/42253318/)). TXNDC16's absence from catalytic discussions in these comprehensive reviews is itself informative and consistent with its non-catalytic status.

The characterization of other thioredoxin-domain-containing proteins with confirmed catalytic activity — such as TXNDC5 ([PMID: 38629066](https://pubmed.ncbi.nlm.nih.gov/38629066/), [PMID: 35934705](https://pubmed.ncbi.nlm.nih.gov/35934705/)), which has three Trx-like domains each with functional CXXC motifs — provides a useful contrast. TXNDC5 has been extensively characterized with purified-protein assays demonstrating disulfide isomerase activity, underscoring the feasibility of such experiments and making TXNDC16's 15-year lack of enzymatic data all the more conspicuous.

---

## Limitations and Knowledge Gaps

### What We Do Not Know

1. **No crystal or cryo-EM structure** of TXNDC16 exists. AlphaFold predictions provide fold models but cannot reveal whether noncanonical cysteines are positioned in geometries that might allow unconventional redox chemistry.

2. **No in vitro biochemistry** has been performed. While the absence of CXXC makes catalytic activity unlikely, it cannot be formally excluded without direct testing. Some non-canonical oxidoreductases exist (e.g., certain single-cysteine mechanisms in bacterial DsbA-like proteins), though these are rare and mechanistically distinct from PDI-family catalysis.

3. **The precise substrate repertoire** of TXNDC16 is unknown. Which misfolded proteins it recognizes, and whether recognition requires its thioredoxin-like domains or glycan-binding properties, has not been determined.

4. **The stoichiometry and dynamics** of the TXNDC16–ERFAD interaction are uncharacterized. Whether binding is constitutive or substrate-induced is unknown.

5. **Publication bias**: It is possible that negative results from redox assays have been obtained but not published, which would further support the non-catalytic conclusion but remains invisible in the literature.

6. **Small literature base**: Only two primary publications exist on TXNDC16 itself, limiting the diversity of experimental approaches that have been applied. The protein remains understudied relative to other PDI-family members.

### Caveats

- Absence of evidence is not evidence of absence — the non-catalytic conclusion, while strongly supported, remains a default inference pending direct experimental testing.
- The CX6C disulfide at C449–C456 could theoretically participate in non-canonical redox chemistry under specific conditions, though no evidence supports this and the spacing is inconsistent with known catalytic mechanisms.
- TXNDC16's secretion (shown by [PMID: 25122923](https://pubmed.ncbi.nlm.nih.gov/25122923/)) raises the possibility of extracellular functions that have not been explored — though any such function would be distinct from intracellular PDI-type catalysis.

---

## Proposed Follow-up Experiments

### Priority 1: Definitive Enzymatic Testing

1. **Purified recombinant TXNDC16 in standard PDI assays**: Express and purify full-length TXNDC16 and test in:
   - Insulin turbidimetric reduction assay (reductase activity)
   - Scrambled RNase A refolding assay (isomerase activity)
   - Di-E-GSSG fluorescent assay (oxidase activity)
   - Compare to PDIA1 positive control and buffer-only negative control

2. **Cysteine-to-serine mutagenesis panel**: Systematically mutate each of the 10 mature cysteines (individually and in combinations, especially C449S, C456S, C84S, C93S) and test for:
   - Loss of any detectable redox activity (if found in experiment 1)
   - Loss of ERFAD binding
   - Loss of ERAD substrate recruitment function

### Priority 2: Redox-State Characterization

3. **Differential alkylation / redox-state trapping**: Treat cells with NEM (to trap free thiols) vs. DTT+NEM (to reduce then trap all cysteines), followed by mass spectrometry, to determine which cysteines are in disulfide bonds vs. free thiols under native ER conditions.

4. **Redox-dependent mobility shift**: Use AMS/mPEG-mal alkylation followed by non-reducing SDS-PAGE to determine whether TXNDC16 cysteines undergo redox cycling in response to ER stress or substrate load.

### Priority 3: Substrate and Complex Characterization

5. **Proximity labeling (BioID/TurboID)** of TXNDC16 to identify its full interactome and potential substrates in the ER lumen.

6. **TXNDC16 knockout / knockdown** followed by measurement of ERAD kinetics for model substrates (e.g., NHK/null Hong Kong variant of alpha-1 antitrypsin, ribophorin 332) to determine whether loss of TXNDC16 delays substrate degradation.

7. **Co-immunoprecipitation under varying redox conditions** to determine whether TXNDC16–ERFAD interaction is redox-sensitive (which would suggest functional coupling to the redox state of the complex).

### Priority 4: Structural Biology

8. **AlphaFold Multimer prediction** of the TXNDC16–ERFAD complex to identify the binding interface and predict whether any TXNDC16 cysteines are positioned near the interaction surface.

9. **Cryo-EM of the TXNDC16–ERFAD complex** to determine the structural basis of their interaction and the spatial relationship between TXNDC16's thioredoxin-like domains and ERFAD's FAD cofactor.

---

## Defensible Molecular Function Annotation

| Annotation | Defensible? | Basis |
|------------|-------------|-------|
| **Protein binding (GO:0005515)** | **Yes** | IPI evidence from ERFAD co-IP ([PMID: 21359175](https://pubmed.ncbi.nlm.nih.gov/21359175/)) |
| Oxidoreductase activity (GO:0016491) | **No** | No CXXC, no enzymatic assay, no direct evidence |
| Protein disulfide isomerase activity (GO:0003756) | **No** | No CXXC, no isomerase assay |
| Disulfide oxidoreductase activity (GO:0015036) | **No** | No catalytic motif, no redox assay |
| Unfolded protein binding (GO:0051082) | **Plausible but unproven** | Consistent with proposed model but not directly demonstrated |
| ERAD pathway involvement (GO:0030433) | **Plausible** | ERFAD interaction supports this, but direct evidence of ERAD function for TXNDC16 itself is lacking |

**Recommended curation:** TXNDC16/ERp90 should be annotated as an ER-luminal multi-domain scaffold protein with protein binding function in the context of ERAD. The PDI "family" classification based on Trx-fold homology should be noted as structural, not functional. If a more specific term is needed, "ERAD substrate adaptor/recruiter" would be defensible based on the original authors' own interpretation and the interaction network evidence. Annotating TXNDC16 as an oxidoreductase or disulfide isomerase based solely on the presence of thioredoxin-like folds would be an unjustified inference — the catalytic motifs are absent, and catalytic activity has never been demonstrated. The protein's gene name ("thioredoxin domain-containing 16") accurately describes its structure but should not be mistaken as evidence for enzymatic function.

---

## References

1. Riemer J, Hansen HG, Appenzeller-Herzog C, Johansson L, Ellgaard L. *Identification of the PDI-family member ERp90 as an interaction partner of ERFAD.* J Cell Sci. 2011;124(Pt 7):1117-1126. [PMID: 21359175](https://pubmed.ncbi.nlm.nih.gov/21359175/)
2. Riemer J, Appenzeller-Herzog C, Johansson L, Bodenmiller B, Hartmann-Petersen R, Ellgaard L. *A luminal flavoprotein in endoplasmic reticulum-associated degradation.* Proc Natl Acad Sci USA. 2009;106(35):14831-14836. [PMID: 19706418](https://pubmed.ncbi.nlm.nih.gov/19706418/)
3. Harz C, Ludwig N, Lang S, et al. *Secretion and immunogenicity of the meningioma-associated antigen TXNDC16.* J Immunol. 2014;193(7):3146-3154. [PMID: 25122923](https://pubmed.ncbi.nlm.nih.gov/25122923/)
4. Ushioda R, Hoseki J, Araki K, Jansen G, Thomas DY, Nagata K. *ERdj5 is required as a disulfide reductase for degradation of misfolded proteins in the ER.* Science. 2008;321(5888):569-572. [PMID: 18653895](https://pubmed.ncbi.nlm.nih.gov/18653895/)
5. Yagi-Utsumi M, Satoh T, Kato K. *Structural basis of redox-dependent substrate binding of protein disulfide isomerase.* Sci Rep. 2015;5:13909. [PMID: 26350503](https://pubmed.ncbi.nlm.nih.gov/26350503/)
6. Chivers PT, Laboissiere MC, Raines RT. *The CXXC motif: imperatives for the formation of native disulfide bonds in the cell.* EMBO J. 1996;15(11):2659-2667. [PMID: 8654363](https://pubmed.ncbi.nlm.nih.gov/8654363/)
7. Jäger M, Dendle M, Kelly JW. *Active site mutations in yeast protein disulfide isomerase cause dithiothreitol sensitivity and a reduced rate of protein folding in the endoplasmic reticulum.* J Biol Chem. 1997;272(18):11749-11756. [PMID: 9298979](https://pubmed.ncbi.nlm.nih.gov/9298979/)
8. Ren G, et al. *The CXXC motif: crystal structure of an active-site variant of Escherichia coli thioredoxin.* Protein Sci. 1999;8(10):2089-2095. [PMID: 10489448](https://pubmed.ncbi.nlm.nih.gov/10489448/)
9. Sato Y, et al. *Functions and mechanisms of protein disulfide isomerase family in cancer emergence.* Cell Death Discov. 2022;8:407. [PMID: 35965326](https://pubmed.ncbi.nlm.nih.gov/35965326/)
10. Zhang X, et al. *The role of protein disulfide isomerase inhibitors in cancer therapy.* Molecules. 2024;29(18):4389. [PMID: 39319369](https://pubmed.ncbi.nlm.nih.gov/39319369/)
11. Bonadio RS, et al. *Nature's economy as blueprint: regional overlap & block-based algorithm for protein design.* BMC Bioinformatics. 2025;26:127. [PMID: 42253318](https://pubmed.ncbi.nlm.nih.gov/42253318/)
