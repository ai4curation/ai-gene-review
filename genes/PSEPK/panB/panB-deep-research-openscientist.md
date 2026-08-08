---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-18T13:47:00.329862'
end_time: '2026-07-18T14:44:27.433264'
duration_seconds: 3447.1
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: panB
  gene_symbol: panB
  uniprot_accession: Q88DW9
  protein_description: 'RecName: Full=3-methyl-2-oxobutanoate hydroxymethyltransferase
    {ECO:0000255|HAMAP-Rule:MF_00156}; EC=2.1.2.11 {ECO:0000255|HAMAP-Rule:MF_00156};
    AltName: Full=Ketopantoate hydroxymethyltransferase {ECO:0000255|HAMAP-Rule:MF_00156};
    Short=KPHMT {ECO:0000255|HAMAP-Rule:MF_00156};'
  gene_info: Name=panB {ECO:0000255|HAMAP-Rule:MF_00156}; OrderedLocusNames=PP_4699;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the PanB family. {ECO:0000255|HAMAP-
  protein_domains: Pantoate_hydroxy_MeTrfase. (IPR003700); Pyrv/PenolPyrv_kinase-like_dom.
    (IPR015813); Pyrv_kinase-like_dom_sf. (IPR040442); Pantoate_transf (PF02548)
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
citation_count: 8
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: panB-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: panB-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88DW9
- **Protein Description:** RecName: Full=3-methyl-2-oxobutanoate hydroxymethyltransferase {ECO:0000255|HAMAP-Rule:MF_00156}; EC=2.1.2.11 {ECO:0000255|HAMAP-Rule:MF_00156}; AltName: Full=Ketopantoate hydroxymethyltransferase {ECO:0000255|HAMAP-Rule:MF_00156}; Short=KPHMT {ECO:0000255|HAMAP-Rule:MF_00156};
- **Gene Information:** Name=panB {ECO:0000255|HAMAP-Rule:MF_00156}; OrderedLocusNames=PP_4699;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the PanB family. {ECO:0000255|HAMAP-
- **Key Domains:** Pantoate_hydroxy_MeTrfase. (IPR003700); Pyrv/PenolPyrv_kinase-like_dom. (IPR015813); Pyrv_kinase-like_dom_sf. (IPR040442); Pantoate_transf (PF02548)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "panB" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'panB' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **panB** (gene ID: panB, UniProt: Q88DW9) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *panB* (PP_4699, UniProt Q88DW9) in *Pseudomonas putida* KT2440

## Summary

The gene **panB** (ordered locus **PP_4699**; UniProt accession **Q88DW9**) of *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / KT2440) encodes **ketopantoate hydroxymethyltransferase (KPHMT; EC 2.1.2.11)**, also systematically named **3-methyl-2-oxobutanoate hydroxymethyltransferase**. This enzyme catalyzes the **first committed step of the *de novo* pantothenate (vitamin B5) biosynthetic pathway**, which ultimately produces coenzyme A (CoA). The reaction transfers a one-carbon hydroxymethyl unit from the folate cofactor **5,10-methylene-tetrahydrofolate** onto the branched-chain keto acid **3-methyl-2-oxobutanoate (α-ketoisovalerate)**, yielding **2-dehydropantoate (ketopantoate)** and **tetrahydrofolate**. All gene-symbol, organism, protein-family, and domain criteria from the UniProt reference were verified during this investigation, and the identification is unambiguous: twelve independent signature databases concordantly classify Q88DW9 as a member of the PanB/KPHMT family, and the *P. putida* protein is a bona fide ortholog of the structurally and biochemically characterized *Escherichia coli* and *Mycobacterium tuberculosis* KPHMT enzymes (59.4% and 45% sequence identity, respectively).

Mechanistically, PanB is a **Mg²⁺-dependent, Class II aldolase-type one-carbon transferase**. It adopts the **(β/α)₈ TIM-barrel fold** of the phosphoenolpyruvate/pyruvate superfamily and assembles into a **homodecamer** — a pentamer of dimers built by domain-swapping of C-terminal α-helices between two opposing pentameric rings. The active site coordinates the substrate keto acid to a catalytic magnesium ion, orienting its C3 carbon for deprotonation and subsequent condensation with the folate-derived one-carbon unit. A high-confidence AlphaFold model of the *P. putida* protein (global mean pLDDT = 97.5) recapitulates this fold and shows every catalytic and metal/substrate-binding residue ordered at very high confidence, corroborating the KPHMT assignment.

Functionally, PanB operates in the **cytoplasm** and sits at a key metabolic **branch point**: its acceptor substrate, α-ketoisovalerate, is the immediate precursor of valine in branched-chain amino-acid biosynthesis, so PanB commits carbon flux out of that pathway and into pantothenate/CoA production. In *P. putida* KT2440, *panB* (PP_4699) is genomically clustered with **panC** (PP_4700, pantothenate synthetase), and the remaining pathway genes needed to complete pantothenate → CoA synthesis are all present in the genome (panE ketopantoate reductase, coaBC, coaD, coaE). PanB is therefore the entry-point enzyme of an intact, essential cofactor-biosynthesis pathway.

---

## Gene/Protein Identity — Verified

The target is unambiguously the correct protein. Every line of evidence converges on one assignment, satisfying all mandatory verification criteria:

- **Gene symbol** *panB* matches the protein description (3-methyl-2-oxobutanoate hydroxymethyltransferase / ketopantoate hydroxymethyltransferase / KPHMT).
- **Organism** is confirmed as *Pseudomonas putida* KT2440 (KEGG ppu:PP_4699).
- **Protein family and domains** align with the literature: PanB family, Pantoate_transf (PF02548), IPR003700, and the pyruvate-kinase-like (β/α)₈ domain superfamily (IPR015813/IPR040442).
- **Twelve independent signature databases** (HAMAP, Pfam, InterPro, two NCBIfam models, PIRSF, PANTHER, CDD, CATH-Gene3D, SCOP, and InterPro homologous superfamilies) unanimously return KPHMT/PanB with no conflicting assignment (see finding F006).

No literature for a different gene with the same symbol was mistakenly adopted; all cited primary studies concern the KPHMT/PanB enzyme family in *E. coli*, *M. tuberculosis*, and the broader bacterial pathway.

---

## Key Findings

### F001 — PanB catalyzes the first committed step of pantothenate/CoA biosynthesis

The primary function of Q88DW9 is enzymatic. UniProt annotation, the Rhea reaction database, and the enzyme classification all agree that PanB is **ketopantoate hydroxymethyltransferase, EC 2.1.2.11**. The catalyzed reaction (Rhea RHEA:11824) is:

> (6R)-5,10-methylene-tetrahydrofolate + 3-methyl-2-oxobutanoate (α-ketoisovalerate) + H₂O → 2-dehydropantoate (ketopantoate) + (6S)-tetrahydrofolate

This is annotated as step 1 of 2 in the sub-pathway "(R)-pantoate from 3-methyl-2-oxobutanoate," which itself is the opening segment of (R)-pantothenate biosynthesis. The reaction is a **hydroxymethyl (one-carbon) transfer** in which methylene-tetrahydrofolate serves as the C1 donor and α-ketoisovalerate as the acceptor.

The role of the KPHMT/PanB family is firmly established in the literature. Work on the *E. coli* enzyme states plainly that "*Escherichia coli* ketopantoate hydroxymethyltransferase (KPHMT) catalyzes the first step in the biosynthesis pathway of pantothenate (vitamin B5), the transfer of a hydroxymethyl group onto alpha-ketoisovalerate" ([PMID: 12837791](https://pubmed.ncbi.nlm.nih.gov/12837791/)). Structural work on the *M. tuberculosis* enzyme adds that "Ketopantoate hydroxymethyltransferase (KPHMT) catalyzes the first committed step in the biosynthesis of pantothenate, which is a precursor to coenzyme A" ([PMID: 12842039](https://pubmed.ncbi.nlm.nih.gov/12842039/)). The four-enzyme architecture of the bacterial pathway — "ketopantoate hydroxymethyltransferase (KPHMT), L-aspartate-alpha-decarboxylase (ADC), pantothenate synthetase (PS) and ketopantoate reductase (KPR) encoded by *panB*, *panD*, *panC* and *panE* genes, respectively" — places PanB unambiguously first ([PMID: 18726075](https://pubmed.ncbi.nlm.nih.gov/18726075/)).

**Substrate specificity** was measured directly in the classic biochemical characterization of the *E. coli* enzyme (Powers & Snell, 1976), which reported "apparent Km values are 0.18, 1.1 and 5.9 mM for tetrahydrofolate, alpha-ketoisovalerate, and formaldehyde" ([PMID: 6463](https://pubmed.ncbi.nlm.nih.gov/6463/)). These kinetics identify the folate C1-donor and the α-ketoisovalerate acceptor as the physiological substrates (the enzyme can also use free formaldehyde as an alternative one-carbon source *in vitro*, but with much lower affinity). The *P. putida* enzyme is expected to share this specificity given its 59.4% identity (155/261 aligned residues) to the *E. coli* ortholog.

### F002 — PanB is a Mg²⁺-dependent Class II aldolase-type enzyme with a conserved (β/α)₈-barrel active site

Q88DW9 is annotated with an **Mg²⁺ cofactor** and conserved metal/substrate-binding residues **Asp45, Asp84, Glu114**, plus the catalytic general base **Glu181** (proton acceptor). All four residues are present at the expected positions in the *P. putida* sequence. The enzyme belongs to the **PanB / Pantoate_transf (Pfam PF02548)** family, InterPro IPR003700, and its fold is the pyruvate-kinase-like (β/α)₈ barrel.

The catalytic chemistry is illuminated by the 1.9 Å *E. coli* KPHMT crystal structure solved in complex with ketopantoate and Mg²⁺: "The active site contains a ketopantoate bidentately coordinated to Mg(2+). Similar binding is likely for the substrate, alpha-ketoisovalerate, orienting the C3 for deprotonation" ([PMID: 12906829](https://pubmed.ncbi.nlm.nih.gov/12906829/)). The metal ion therefore does double duty — anchoring the substrate and polarizing it so that the C3 carbon can be deprotonated to generate the nucleophilic enolate that attacks the folate-derived one-carbon unit. The same structural study confirms the fold: "KPHMT adopts the (betaalpha)(8) barrel fold and is a member of the phosphoenolpyruvate/pyruvate superfamily" ([PMID: 12906829](https://pubmed.ncbi.nlm.nih.gov/12906829/)), consistent with the InterPro and Pfam domain signatures of Q88DW9.

The mechanistic class was pinned down biochemically. The enzyme "requires Mg²⁺ for activity; Mn²⁺, Co²⁺, Zn²⁺ are progressively less active" ([PMID: 6463](https://pubmed.ncbi.nlm.nih.gov/6463/)), and critically, it "is not inactivated by borohydride reduction in the presence of excess substrates, i.e. it is a Class II aldolase" ([PMID: 6463](https://pubmed.ncbi.nlm.nih.gov/6463/)). The lack of borohydride inactivation rules out a Schiff-base (Class I) mechanism and confirms a **metal-dependent (Class II) aldol-type condensation**. The reported pH optimum is 7.0–7.6.

### F003 — PanB acts in the cytoplasm as a homodecamer built by C-terminal domain swapping

UniProt localizes Q88DW9 to the **cytoplasm** and annotates its quaternary structure as a **homodecamer (pentamer of dimers)**. This oligomeric state is a deeply conserved feature of the family. In the *E. coli* enzyme, biochemical sizing found a ~255 kDa particle composed of "10 identical subunits" of ~27 kDa each ([PMID: 6463](https://pubmed.ncbi.nlm.nih.gov/6463/)). The structural basis of assembly was resolved in the *M. tuberculosis* enzyme: "The protein forms a decameric complex, with subunits in opposing pentameric rings held together by a swapping of their C-terminal alpha helices" ([PMID: 12842039](https://pubmed.ncbi.nlm.nih.gov/12842039/)). The *E. coli* crystal structure independently confirmed the decamer, being solved by locating "160 selenomethionine sites and phase 560 kDa of protein" in the asymmetric unit ([PMID: 12906829](https://pubmed.ncbi.nlm.nih.gov/12906829/)). The *P. putida* monomer (266 aa, ~29 kDa) is fully consistent with this same decameric architecture.

### F004 — PanB (PP_4699) sits in a panB–panC gene cluster and feeds the intact P. putida pantothenate → CoA pathway; its acceptor substrate branches from valine biosynthesis

Genomic context reinforces the functional assignment. In KEGG, **ppu:PP_4699 = panB**, orthology **K00606** (EC 2.1.2.11), mapped to pathway **ppu00770 "Pantothenate and CoA biosynthesis"** and **ppu01240 "Biosynthesis of cofactors."** The gene occupies genomic coordinates 5,340,894–5,341,694. Its immediate neighbor, **PP_4700 = panC** (pantothenate synthetase, K01918), forms a **panB–panC cluster**, while the other flanking gene **PP_4698 = folK** participates in folate biosynthesis — notably relevant because folate provides PanB's one-carbon donor.

The downstream pathway is complete in KT2440: ketopantoate reductase (**panE**, K00077; candidate loci PP_1351/PP_2325/PP_2998), **panC** (PP_4700), and the CoA-synthesis genes **coaBC** (PP_5285, K13038), **coaD** (PP_5123, K00954), and **coaE** (PP_0631, K00859). The acceptor substrate 3-methyl-2-oxobutanoate (α-ketoisovalerate) is the **branch-point intermediate of branched-chain (valine) amino-acid biosynthesis**, linking PanB to that pathway (KEGG links α-ketoisovalerate via *ilvE*/K00826 = PP_3511). This establishes PanB as the enzyme that diverts carbon from valine precursor supply into cofactor biosynthesis.

The literature confirms the four-enzyme framework into which PanB feeds: the pathway comprises "four enzymic reactions catalysed by ketopantoate hydroxymethyltransferase (KPHMT), L-aspartate-alpha-decarboxylase (ADC), pantothenate synthetase (PS) and ketopantoate reductase (KPR) encoded by *panB*, *panD*, *panC* and *panE* genes" ([PMID: 18726075](https://pubmed.ncbi.nlm.nih.gov/18726075/)), and that PanB "catalyzes the first committed step in the biosynthesis of pantothenate, which is a precursor to coenzyme A" ([PMID: 12842039](https://pubmed.ncbi.nlm.nih.gov/12842039/)). One caveat: a canonical *panD* (aspartate 1-decarboxylase, K01579) was not recovered by KEGG orthology linkage in *ppu*, implying that β-alanine (the second substrate of PanC) may be supplied by an alternative route in *P. putida* — but this concerns a downstream step, not PanB itself.

### F005 — The AlphaFold model is very high confidence with a well-ordered, conserved active site

The AlphaFold DB model **AF-Q88DW9-F1 (v6)** has a **global mean pLDDT of 97.5** across all 266 residues: 97% of residues are modeled at very high confidence (pLDDT > 90), 3% at 70–90, and none below 70 (minimum 63.4 at a terminus). Every annotated catalytic and metal/substrate-binding residue is modeled at very high confidence: Asp45 (98.7), Asp84 (98.9), Lys112 (98.9), Glu114 (98.6), and the general base Glu181 (98.5). These positions are conserved relative to the *E. coli* enzyme (59% overall identity), whose crystal structure shows the equivalent residues coordinating Mg²⁺ and ketopantoate in a (β/α)₈ barrel ([PMID: 12906829](https://pubmed.ncbi.nlm.nih.gov/12906829/)). The model thus provides independent structural corroboration that the *P. putida* protein possesses an intact, canonical KPHMT active site.

### F006 — Twelve independent signature databases unanimously classify Q88DW9 as PanB/KPHMT

InterPro member-database analysis of Q88DW9 returns concordant KPHMT/PanB assignments from all signatures examined: **HAMAP MF_00156, Pfam PF02548, InterPro family IPR003700, NCBIfam TIGR00222 and NF001452, PIRSF000388, PANTHER PTHR20881, CDD cd06557 (KPHMT-like)**, plus fold-level signatures **CATH-Gene3D G3DSA:3.20.20.60** and **SCOP SSF51621** (phosphoenolpyruvate/pyruvate domain) and InterPro homologous superfamilies **IPR015813/IPR040442** (pyruvate-kinase-like domain). No conflicting family assignment exists. Combined with the ortholog-level sequence identities to characterized enzymes, this makes the identity of Q88DW9 as PanB/KPHMT effectively certain.

---

## Mechanistic Model / Interpretation

### The reaction and its position in metabolism

PanB catalyzes a magnesium-dependent aldol-type one-carbon transfer. In the enzyme's active site, α-ketoisovalerate is chelated bidentately by the catalytic Mg²⁺; the metal polarizes the substrate and the general base (Glu181) abstracts a proton from the C3 methyl-adjacent position, generating a nucleophilic enolate. This carbanion attacks the reactive one-carbon unit carried by 5,10-methylene-tetrahydrofolate, installing the hydroxymethyl group and releasing tetrahydrofolate. The product, ketopantoate (2-dehydropantoate), carries the hallmark hydroxymethyl group that defines the pantoate/pantothenate moiety.

```
   Branched-chain amino-acid (valine) biosynthesis
                     │
                     ▼
        3-methyl-2-oxobutanoate  (α-ketoisovalerate)
                     │
     5,10-CH2-THF ──►│  ◄── PanB / KPHMT  (EC 2.1.2.11)   [PP_4699, Q88DW9]
         THF   ◄─────│      Mg2+-dependent Class II aldolase
                     ▼
              2-dehydropantoate  (ketopantoate)
                     │  ◄── PanE / ketopantoate reductase (NADPH)
                     ▼
                 (R)-pantoate
                     │  ◄── PanC / pantothenate synthetase (+ β-alanine)
                     ▼
              (R)-pantothenate  (vitamin B5)
                     │  ◄── CoaBC → CoaD → CoaE
                     ▼
                Coenzyme A (CoA)
```

### Structure–function synthesis

| Property | Value / description | Evidence |
|---|---|---|
| Enzyme | Ketopantoate hydroxymethyltransferase (KPHMT), EC 2.1.2.11 | UniProt; [PMID: 12837791](https://pubmed.ncbi.nlm.nih.gov/12837791/) |
| Reaction | 5,10-CH₂-THF + α-ketoisovalerate + H₂O → ketopantoate + THF | Rhea RHEA:11824 |
| Cofactor | Mg²⁺ (Mn²⁺/Co²⁺/Zn²⁺ less active) | [PMID: 6463](https://pubmed.ncbi.nlm.nih.gov/6463/) |
| Mechanism | Class II (metal-dependent) aldolase; no Schiff base | [PMID: 6463](https://pubmed.ncbi.nlm.nih.gov/6463/) |
| Catalytic residues | Asp45, Asp84, Glu114 (metal/substrate); Glu181 (general base); Lys112 | UniProt; AlphaFold model |
| Fold | (β/α)₈ TIM-barrel, PEP/pyruvate superfamily | [PMID: 12906829](https://pubmed.ncbi.nlm.nih.gov/12906829/) |
| Quaternary structure | Homodecamer (pentamer of dimers); C-terminal helix swap | [PMID: 12842039](https://pubmed.ncbi.nlm.nih.gov/12842039/); [PMID: 6463](https://pubmed.ncbi.nlm.nih.gov/6463/) |
| Localization | Cytoplasm | UniProt |
| Monomer size | 266 aa, ~29 kDa | UniProt / sequence |
| Gene context | panB–panC cluster (PP_4699–PP_4700); folK neighbor | KEGG ppu |
| Model confidence | AlphaFold pLDDT 97.5 (97% > 90) | AF-Q88DW9-F1 v6 |

### Biological significance

Coenzyme A is an essential, universal cofactor for acyl-group transfer, fatty-acid metabolism, and central carbon metabolism (TCA cycle). Because *P. putida* KT2440 encodes the complete pantothenate → CoA route and PanB is the committed entry point, PanB is expected to be metabolically essential (or conditionally essential in pantothenate-free media). Its position at the valine/branched-chain branch point also means PanB competes for α-ketoisovalerate flux with valine biosynthesis, giving it a regulatory role in balancing amino-acid versus cofactor demands. The absence of a canonical *panD* in the KEGG orthology set suggests *P. putida* obtains β-alanine (needed downstream by PanC) via an alternative route — a downstream detail that does not affect PanB's own function but is worth noting for full pathway reconstruction.

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution |
|---|---|---|
| [12837791](https://pubmed.ncbi.nlm.nih.gov/12837791/) | *Comparative analysis of the E. coli KPHMT crystal structure … (βα)₈ PEP/pyruvate superfamily* | Defines the KPHMT reaction (hydroxymethyl transfer onto α-ketoisovalerate) and superfamily membership |
| [6463](https://pubmed.ncbi.nlm.nih.gov/6463/) | *Ketopantoate hydroxymethyltransferase II. Physical, catalytic, regulatory properties* (Powers & Snell) | Direct kinetics (Km values), Mg²⁺ dependence, Class II aldolase classification, decamer of 10 subunits, pH optimum |
| [12906829](https://pubmed.ncbi.nlm.nih.gov/12906829/) | *Structure of E. coli KPHMT complexed with ketopantoate and Mg²⁺* | Active-site Mg²⁺ coordination and C3 orientation; (βα)₈ fold; 560 kDa decamer |
| [12842039](https://pubmed.ncbi.nlm.nih.gov/12842039/) | *Crystal structure of KPHMT from M. tuberculosis* | First committed step; CoA precursor; decamer via C-terminal helix swapping |
| [18726075](https://pubmed.ncbi.nlm.nih.gov/18726075/) | *Towards engineering increased pantothenate (vitamin B5) levels in plants* | Four-enzyme pathway definition (panB/panD/panC/panE); PanB is first |

Supporting/contextual literature reviewed but not directly used for core claims includes reviews on CoA-biosynthesis as an antimicrobial/antiparasitic/antifungal drug target ([PMID: 41967290](https://pubmed.ncbi.nlm.nih.gov/41967290/), [PMID: 41914741](https://pubmed.ncbi.nlm.nih.gov/41914741/), [PMID: 40801835](https://pubmed.ncbi.nlm.nih.gov/40801835/)), which underscore the pathway's essentiality and therapeutic relevance, and a *B. thuringiensis* expression study that identifies a PanB homolog among development-related transcripts ([PMID: 26191639](https://pubmed.ncbi.nlm.nih.gov/26191639/)).

**Cross-species consistency.** The three independently characterized orthologs — *E. coli* (biochemistry + structure), *M. tuberculosis* (structure), and by inference *P. putida* (sequence + AlphaFold) — agree on reaction, cofactor, mechanism, fold, and oligomeric state. No paper challenges the assignment. The main gap is that all direct experimental data derive from orthologs rather than the *P. putida* protein itself.

---

## Limitations and Knowledge Gaps

1. **No direct experimental characterization of the *P. putida* enzyme.** All kinetic, mechanistic, and structural data come from *E. coli* and *M. tuberculosis* orthologs. The *P. putida* assignment rests on strong homology (59.4% identity to *E. coli*), conserved catalytic residues, and a high-confidence AlphaFold model — robust but inferential.

2. **Substrate-specificity numbers are borrowed.** The reported Km values (0.18/1.1/5.9 mM for THF/α-ketoisovalerate/formaldehyde) are *E. coli* values ([PMID: 6463](https://pubmed.ncbi.nlm.nih.gov/6463/)); *P. putida*-specific kinetics have not been measured here.

3. **β-alanine supply route unresolved.** A canonical *panD* (aspartate-1-decarboxylase) was not retrieved by KEGG orthology in *ppu*, leaving the source of β-alanine (needed by PanC downstream) unclear. This is a pathway-level gap, not a PanB-level one.

4. **panE assignment is ambiguous.** Three candidate ketopantoate reductase loci (PP_1351/PP_2325/PP_2998) were flagged; the physiologically relevant one is not pinned down.

5. **Essentiality not experimentally confirmed** in *P. putida* KT2440; it is inferred from pathway completeness and the essential nature of CoA.

6. **The AlphaFold model is a monomer.** It does not directly validate the decameric assembly or the domain-swapped inter-subunit interface, which are inferred from orthologous crystal structures.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant expression and enzymatic assay.** Clone PP_4699, purify the His-tagged protein, and measure KPHMT activity spectrophotometrically (or by coupled assay), determining *P. putida*-specific Km/kcat for methylene-THF and α-ketoisovalerate and confirming the Mg²⁺ requirement.

2. **Confirm quaternary structure.** Use size-exclusion chromatography with multi-angle light scattering (SEC-MALS) or native mass spectrometry to verify the ~290 kDa homodecamer, and consider cryo-EM/crystallography to confirm the domain-swapped assembly.

3. **Site-directed mutagenesis** of Asp45, Asp84, Glu114, and Glu181 to validate their predicted roles in Mg²⁺/substrate binding and general-base catalysis.

4. **Gene-essentiality test.** Attempt markerless deletion of PP_4699 and test for pantothenate auxotrophy (rescue by exogenous pantothenate or β-alanine) to confirm the committed-step, essential role.

5. **Resolve the β-alanine and panE gaps.** Use transcriptomics/metabolomics or targeted knockouts to identify the β-alanine source and the operative ketopantoate reductase among PP_1351/PP_2325/PP_2998.

6. **Structural biology on the native protein.** Determine an experimental structure of the *P. putida* enzyme, ideally with bound Mg²⁺ and ketopantoate, to directly validate the AlphaFold active-site model.

---

*Report compiled from 5 investigation iterations, 6 confirmed findings, and 12 reviewed papers. Gene identity verified against UniProt Q88DW9 and 12 concordant signature databases; no conflicting family assignment was found.*


## Artifacts

- [OpenScientist final report](panB-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](panB-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:12837791
2. PMID:12842039
3. PMID:18726075
4. PMID:12906829
5. PMID:41967290
6. PMID:41914741
7. PMID:40801835
8. PMID:26191639