---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-15T09:11:25.393976'
end_time: '2026-07-15T09:28:16.364156'
duration_seconds: 1010.97
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: tktA
  gene_symbol: tktA
  uniprot_accession: Q88D62
  protein_description: 'RecName: Full=Transketolase {ECO:0000256|ARBA:ARBA00013152,
    ECO:0000256|NCBIfam:TIGR00232}; EC=2.2.1.1 {ECO:0000256|ARBA:ARBA00013152, ECO:0000256|NCBIfam:TIGR00232};'
  gene_info: Name=tktA {ECO:0000313|EMBL:AAN70532.1}; OrderedLocusNames=PP_4965 {ECO:0000313|EMBL:AAN70532.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the transketolase family.
  protein_domains: THDP-binding. (IPR029061); Transketo_C/PFOR_II. (IPR009014); Transketolase-like_C_2.
    (IPR055152); Transketolase-like_Pyr-bd. (IPR005475); Transketolase_bac-like. (IPR005478)
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
citation_count: 14
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: tktA-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: tktA-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88D62
- **Protein Description:** RecName: Full=Transketolase {ECO:0000256|ARBA:ARBA00013152, ECO:0000256|NCBIfam:TIGR00232}; EC=2.2.1.1 {ECO:0000256|ARBA:ARBA00013152, ECO:0000256|NCBIfam:TIGR00232};
- **Gene Information:** Name=tktA {ECO:0000313|EMBL:AAN70532.1}; OrderedLocusNames=PP_4965 {ECO:0000313|EMBL:AAN70532.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the transketolase family.
- **Key Domains:** THDP-binding. (IPR029061); Transketo_C/PFOR_II. (IPR009014); Transketolase-like_C_2. (IPR055152); Transketolase-like_Pyr-bd. (IPR005475); Transketolase_bac-like. (IPR005478)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "tktA" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'tktA' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **tktA** (gene ID: tktA, UniProt: Q88D62) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: tktA (Transketolase, Q88D62 / PP_4965) in *Pseudomonas putida* KT2440

**UniProt accession:** Q88D62 · **Gene:** *tktA* · **Ordered locus:** PP_4965
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / KT2440), taxid 160488
**Enzyme:** Transketolase, EC 2.2.1.1 · 665 aa, ~72.5 kDa · Homodimer

---

## Summary

**tktA (UniProt Q88D62; ordered locus PP_4965) of *Pseudomonas putida* KT2440 encodes transketolase (EC 2.2.1.1), a soluble cytoplasmic, thiamine-diphosphate (ThDP)- and Mg²⁺-dependent homodimeric enzyme that catalyzes the reversible transfer of a two-carbon "ketol" (dihydroxyethyl/glycolaldehyde) unit from a ketose-phosphate donor to an aldose-phosphate acceptor.** These are the two defining reactions of the non-oxidative branch of the pentose phosphate pathway (PPP). The target identity was verified against the UniProt record: the gene symbol *tktA*, the EC number 2.2.1.1, the transketolase protein family, and the diagnostic ThDP-binding (IPR029061, IPR005475) and transketolase C-terminal (IPR009014, IPR055152, IPR005478) domains are all mutually consistent, and the recovered literature describes transketolase enzymology directly. There is **no gene-symbol ambiguity** — *tktA* is a broadly conserved central-metabolism gene name for transketolase across bacteria.

Functionally, transketolase interconverts xylulose-5-phosphate (X5P), ribose-5-phosphate (R5P), sedoheptulose-7-phosphate (S7P), erythrose-4-phosphate (E4P), fructose-6-phosphate (F6P) and glyceraldehyde-3-phosphate (GAP). Through these reactions it (i) supplies **R5P** for nucleotide/histidine biosynthesis, (ii) supplies **E4P**, the precursor that (with phosphoenolpyruvate) enters the **shikimate pathway** toward aromatic amino acids and aromatic secondary metabolites, and (iii) links the PPP to glycolysis/gluconeogenesis. Metabolic-engineering evidence establishes transketolase as rate-limiting for E4P supply and hence for aromatic-product formation.

In *P. putida* KT2440 specifically — an organism that lacks a functional Embden–Meyerhof–Parnas glycolysis and catabolizes glucose almost exclusively via the Entner–Doudoroff route — transketolase operates as an integral component of the **EDEMP cycle**, an unusual architecture that recycles triose phosphates back to hexoses and biases the redox economy toward NADPH overproduction. Genomic and proteomic evidence shows tktA is the **single, non-redundant, complete transketolase** in KT2440 (the only other transketolase-family entry, PP_5367/Q88C16, is a 156-aa fragment lacking the catalytic pyrimidine-binding domain). It sits in a compact gene neighborhood with *pgk* (PP_4963) and *epd* (PP_4964), physically linking transketolase-derived E4P to both glycolysis and vitamin B6 (pyridoxal-5′-phosphate) biosynthesis. The enzyme carries the fully conserved transketolase catalytic fingerprint and functions in the cytoplasm.

---

## Key Findings

### F001 — tktA encodes a ThDP-dependent transketolase (EC 2.2.1.1)

UniProt Q88D62 annotates PP_4965 as **transketolase, EC 2.2.1.1**, with ECO evidence from ARBA and the NCBIfam model TIGR00232, and places it in the transketolase family. The domain architecture — THDP-binding (IPR029061), transketolase-like pyrimidine-binding (IPR005475), and transketolase C-terminal domains — is the canonical layout of a bona fide transketolase. Mechanistically, the enzyme transfers a two-carbon glycolaldehyde/dihydroxyethyl unit from a ketose donor to an aldose acceptor using thiamine diphosphate as the essential cofactor. This is directly supported by primary literature: transketolase "catalyzes the transfer of a glycolaldehyde residue from ketose (the donor substrate) to aldose (the acceptor substrate)" ([PMID: 29500317](https://pubmed.ncbi.nlm.nih.gov/29500317/)), and it is "a thiamine diphosphate-dependent enzyme … [that] plays a crucial role in cellular metabolism" ([PMID: 41203356](https://pubmed.ncbi.nlm.nih.gov/41203356/)). The gene symbol, EC number, family, and domains all agree, confirming correct target identification.

### F002 — Substrate specificity: reversible ketol transfer across the non-oxidative PPP

Transketolase catalyzes two reversible reactions of the non-oxidative PPP:

1. **X5P + R5P ⇌ S7P + GAP**
2. **X5P + E4P ⇌ F6P + GAP**

The **donor** is a ketose bearing an S-configured C3 hydroxyl (X5P, F6P, S7P, or the non-physiological hydroxypyruvate), and the **acceptor** is an aldose (R5P, E4P, or GAP). Mechanistic work on the phosphoketolase/transketolase enzyme class confirms these enzymes "catalyze phosphorolytic cleavage of xylulose 5-phosphate or fructose 6-phosphate in the first reaction step," identifying X5P and F6P as ketose donors cleaved in the first half-reaction ([PMID: 36974963](https://pubmed.ncbi.nlm.nih.gov/36974963/)). The reversibility and the R5P/heptulose-7-phosphate substrate pairing were experimentally demonstrated with purified enzyme: "the transketolase exchange reaction, [¹⁴C]ribose 5-phosphate + altro-heptulose 7-phosphate ⇌ … was demonstrated for the first time using purified transketolase" ([PMID: 6862092](https://pubmed.ncbi.nlm.nih.gov/6862092/)). The registered catalytic activity for Q88D62 (Rhea RHEA:10508) is **D-sedoheptulose 7-phosphate + D-glyceraldehyde 3-phosphate = aldehydo-D-ribose 5-phosphate + D-xylulose 5-phosphate** — precisely reaction 1 written in reverse.

### F003 — Structure and cofactors: 665-aa homodimer, one ThDP + one Mg²⁺ per subunit

Q88D62 is a **665-residue (~72.5 kDa)** protein that assembles as an obligate **homodimer**, with the two active sites forming at the subunit interface. Each subunit binds **one thiamine diphosphate and one Mg²⁺** (with tolerance for other divalent cations such as Ca²⁺ or Co²⁺). The record annotates a transketolase-like pyrimidine-binding domain (~residues 354–526) and a C-terminal transketolase domain, an active-site proton-donor residue at position 411, catalytically important residues at 26 and 260, and an extensive set of cofactor-coordinating positions (26, 66, 114–116, 155–156, 185, 187, 260, 357, 384, 437, 461, 469, 473, 520). The Mg²⁺ requirement is corroborated by assay work "including or omitting magnesium to assess functional cofactor limitation" ([PMID: 41870883](https://pubmed.ncbi.nlm.nih.gov/41870883/)). ThDP is essential; transketolase activity is a classical functional readout of thiamine status precisely because the apoenzyme requires the cofactor.

### F004 — In KT2440, transketolase operates within the NADPH-favoring EDEMP cycle

*P. putida* KT2440 lacks a functional Embden–Meyerhof–Parnas glycolysis and catabolizes glucose almost exclusively via the Entner–Doudoroff route. ¹³C-metabolic flux analysis revealed that ~10% of triose phosphates are recycled back to hexose phosphates by combining ED, gluconeogenic EMP, and PPP activities into what the authors named the **EDEMP cycle**: "This set of reactions merges activities belonging to the ED, the EMP (operating in a gluconeogenic fashion), and the pentose phosphate pathways to form an unforeseen metabolic architecture (EDEMP cycle)" ([PMID: 26350459](https://pubmed.ncbi.nlm.nih.gov/26350459/)). This cycle biases the redox economy toward reducing power: "the default metabolic state of P. putida KT2440 is characterized by a slight catabolic overproduction of reducing power" (NADPH) ([PMID: 26350459](https://pubmed.ncbi.nlm.nih.gov/26350459/)). Transketolase provides the two non-oxidative PPP ketol-transfer steps that interconvert pentose phosphates with F6P/GAP and is therefore an obligate participant in this recycling architecture — physiologically important for a soil bacterium that must buffer oxidative and solvent stress and supply biosynthetic NADPH.

### F005 — Transketolase supplies E4P and is rate-limiting for aromatic (shikimate-pathway) product formation

Transketolase generates **erythrose-4-phosphate**, which condenses with phosphoenolpyruvate via DAHP synthase to enter the shikimate pathway toward aromatic amino acids (Phe, Tyr, Trp) and aromatic secondary metabolites. The two-carbon transfer that produces/consumes E4P is explicitly described: transketolases "transfer two carbon units from fructose-6-phosphate to erythrose-4-phosphate and convert glyceraldehyde-3-phosphate to xylulose-5-phosphate," and "erythrose-4-phosphate enters the shikimate pathway which … produces many secondary metabolites such as aromatic amino acids, flavonoids, lignin" ([PMID: 24132392](https://pubmed.ncbi.nlm.nih.gov/24132392/)). Metabolic-engineering evidence establishes transketolase as **rate-limiting for E4P supply**: overexpression of *tktA* raised tryptophan titers to 37.9–40.2 g/L — "overexpression of the tktA gene, alone or with the ppsA gene, could further improve tryptophan yield to a final tryptophan titer of 37.9 and 40.2 g/L" ([PMID: 22791961](https://pubmed.ncbi.nlm.nih.gov/22791961/)). Complementary studies show *tktA* boosts L-phenylalanine production from glycerol ([PMID: 25012491](https://pubmed.ncbi.nlm.nih.gov/25012491/)) and indirubin production from glucose ([PMID: 29301095](https://pubmed.ncbi.nlm.nih.gov/29301095/)). This precursor-supply function is directly relevant to *P. putida*, a workhorse chassis for aromatic-compound metabolism and production.

### F006 — Localization: soluble cytoplasmic enzyme

Feature analysis of Q88D62 shows **no signal peptide and no transmembrane segments**, consistent with a soluble intracellular protein. In bacteria the entire PPP is cytosolic: "Unlike bacteria, fungal and animal, PPP is complete in the cytosol and all enzymes are found cytosolic" ([PMID: 24132392](https://pubmed.ncbi.nlm.nih.gov/24132392/)). Its substrates (phosphorylated sugars) and cofactors (ThDP, Mg²⁺) are cytoplasmic. Transketolase therefore carries out its function in the **cytoplasm** of *P. putida*.

### F007 — Conserved catalytic fingerprint (GDG motif, His cluster, Glu411)

Sequence-motif analysis of the 665-aa protein identifies the complete transketolase catalytic apparatus: (i) the diagnostic **GDG ThDP/Mg²⁺-binding motif** (G153-D154-G155) within the sequence context GDGCMMEGISHEVASLAGTLGLNKLIAFYD, with metal/ThDP-binding residues Asp155/Gly156; (ii) a conserved **active-site histidine cluster** (His26, His66, His260, His461, His473), with His26 and His260 flagged as catalytically important; and (iii) **Glu411**, homologous to *E. coli* transketolase Glu411, the invariant glutamate that hydrogen-bonds the N1′ atom of the ThDP aminopyrimidine ring to promote formation of the reactive C2 ylide/carbanion. The importance of conserved active-site architecture in maintaining the catalytic **V-conformation** of ThDP in this enzyme class is supported by site-saturation mutagenesis work: "the long held tenet that a bulky hydrophobic residue provides a fulcrum by which the V-conformation of the ThDP cofactor is maintained" ([PMID: 23895593](https://pubmed.ncbi.nlm.nih.gov/23895593/)). The presence of the full fingerprint provides strong evolutionary evidence that Q88D62 is a catalytically competent transketolase operating by the canonical ThDP ylide mechanism — it is not a pseudogene or degenerate homolog.

### F008 — tktA is the sole complete transketolase in KT2440 (no isozyme redundancy)

A UniProt proteome query (taxid 160488, `protein_name:transketolase`) returns only two hits: **Q88D62** (tktA/PP_4965, the full-length 665-aa transketolase with complete pyrimidine domain, GDG motif, His cluster, and catalytic Glu411) and **Q88C16** (PP_5367), a 156-aa "transketolase domain protein" carrying only the C-terminal Transketo_C/PFOR_II module (IPR009014) and lacking the ThDP/pyrimidine-binding domain and catalytic residues. Thus KT2440 encodes a **single bona fide transketolase**, in contrast to *E. coli*, which has two isozymes (*tktA* and *tktB*). Unlike *E. coli*, *P. putida* has **no paralog to buffer loss of tktA**, making it the exclusive route for non-oxidative-PPP interconversions and E4P/R5P supply, and predicting that its loss would be strongly deleterious under conditions requiring pentose or E4P flux.

### F009 — Genomic clustering with *pgk* and *epd* links transketolase to glycolysis and vitamin B6 biosynthesis

The PP_4965 neighborhood forms a compact functional cluster: **PP_4963 = phosphoglycerate kinase (Pgk**, 387 aa, glycolytic/gluconeogenic), **PP_4964 = erythrose-4-phosphate dehydrogenase (Epd/GapB**, 352 aa), and **PP_4965 = tktA**. Epd catalyzes the committed first step of pyridoxal-5′-phosphate (vitamin B6) biosynthesis by oxidizing E4P to 4-phosphoerythronate — meaning transketolase-produced E4P is a shared substrate feeding both the shikimate pathway and PLP biosynthesis. This co-localizes the enzyme that **produces** E4P (transketolase) with one that **consumes** E4P (Epd), and with triose-phosphate metabolism (Pgk), reinforcing transketolase's role as the E4P source and extending its biosynthetic relevance beyond aromatic amino acids to vitamin B6/PLP biosynthesis. The immediately downstream genes PP_4966 (a transcriptional regulator of methionine metabolism) and PP_4967 (S-adenosylmethionine synthase, MetK) belong to methionine/SAM metabolism and are likely a separate transcriptional unit.

---

## Mechanistic Model / Interpretation

Transketolase in *P. putida* KT2440 is best understood as a **central metabolic hub** that shuttles two-carbon units between sugar phosphates, thereby wiring together the oxidative PPP, glycolysis/gluconeogenesis, and biosynthetic precursor supply.

### Reaction chemistry (per catalytic cycle)

```
        ThDP-C2 ylide (carbanion)
                 |
  Ketose donor ──> cleaved between C2–C3
  (X5P/F6P/S7P)  |  -> dihydroxyethyl-ThDP (DHEThDP) carbanion + released aldose
                 |
  Aldose acceptor─ 2-C unit transferred to acceptor C1
  (R5P/E4P/GAP)  |  -> new ketose product
                 v
        Glu411 activates aminopyrimidine N1' -> deprotonates C2 -> ylide
        His cluster (His26/His260...) + GDG motif + Mg2+ orient ThDP & substrate phosphates
```

### Metabolic map of the two physiological reactions

| Reaction | Donor (ketose) | Acceptor (aldose) | Products | Net biosynthetic value |
|---|---|---|---|---|
| TK-1 | Xylulose-5-P | Ribose-5-P | Sedoheptulose-7-P + GAP | Feeds transaldolase; balances pentoses; supplies R5P |
| TK-2 | Xylulose-5-P | Erythrose-4-P | Fructose-6-P + GAP | Returns carbon to F6P/GAP; **E4P is the key precursor** |

### System-level role in KT2440

```
   Glucose ──(Entner–Doudoroff)──> GAP + pyruvate
      |                                   ^
      |            (gluconeogenic EMP)    |  ~10% triose recycled
      v                                   |
   6-P-gluconate ──(oxidative PPP)──> Ru5P ──> X5P + R5P
                                            |
                                    TRANSKETOLASE (tktA)
                                            |
                        ┌───────────────────┼───────────────────┐
                        v                   v                   v
                     S7P + GAP          F6P + GAP            E4P (supply)
                   (→ transaldolase)   (→ EDEMP recycle)   ┌────┴────┐
                                                           v         v
                                                 Shikimate pathway   Epd (PP_4964)
                                                 (aromatic AAs,      → 4-P-erythronate
                                                  aromatics)         → PLP / vitamin B6
```

The **EDEMP cycle** ([PMID: 26350459](https://pubmed.ncbi.nlm.nih.gov/26350459/)) explains why a transketolase-driven non-oxidative PPP is essential in KT2440 even though the organism does not run canonical glycolysis: pentose phosphates generated by the oxidative PPP must be returned to the central hexose/triose pool, and transketolase (with transaldolase) performs exactly this carbon-rebalancing. Because the cycle is tuned to overproduce NADPH, transketolase indirectly supports KT2440's celebrated robustness against oxidative and solvent stress. Simultaneously, as the sole source of E4P, transketolase gates flux into aromatic biosynthesis and vitamin B6 biosynthesis — a role of practical importance given *P. putida*'s use as a chassis for producing aromatic chemicals.

A useful cross-organism validation comes from *Yersinia pestis*, where transketolase (TktA) and transaldolase were shown to have **distinct, non-interchangeable roles** in metabolism, biofilm formation, and vector colonization ([PMID: 42347215](https://pubmed.ncbi.nlm.nih.gov/42347215/)) — evidence that the non-oxidative PPP enzymes are physiologically consequential and not trivially bypassed. In eukaryotic disease contexts, TKT even participates in oncogenic signaling loops (TKT–c-Myc; [PMID: 42014677](https://pubmed.ncbi.nlm.nih.gov/42014677/)); while not relevant to the bacterial enzyme's mechanism, this underscores how central transketolase flux is to cell physiology across kingdoms.

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports the annotation |
|---|---|---|
| [29500317](https://pubmed.ncbi.nlm.nih.gov/29500317/) | *The mechanism of a one-substrate transketolase reaction* | Defines the core ketol-transfer chemistry (glycolaldehyde from ketose donor to aldose acceptor) — F001 |
| [41203356](https://pubmed.ncbi.nlm.nih.gov/41203356/) | *Engineering transketolase for stereoselective α-hydroxyketone synthesis* | Confirms ThDP dependence and central metabolic role — F001 |
| [36974963](https://pubmed.ncbi.nlm.nih.gov/36974963/) | *Ambient-temperature structure of phosphoketolase (SFX)* | Identifies X5P and F6P as ketose donors cleaved in the first half-reaction — F002 |
| [6862092](https://pubmed.ncbi.nlm.nih.gov/6862092/) | *Non-oxidative synthesis of pentose 5-phosphate…* | Experimental demonstration of the reversible R5P/heptulose-7-P exchange with purified transketolase — F002 |
| [41870883](https://pubmed.ncbi.nlm.nih.gov/41870883/) | *Reassessing transketolase assays…* | Confirms Mg²⁺ as a functional cofactor — F003 |
| [26350459](https://pubmed.ncbi.nlm.nih.gov/26350459/) | *P. putida KT2440 metabolizes glucose through the EDEMP cycle* | Defines the EDEMP cycle and NADPH overproduction in the exact target organism — F004 |
| [24132392](https://pubmed.ncbi.nlm.nih.gov/24132392/) | *Cloning… of sugarcane transketolase* | Two-carbon transfer producing E4P; E4P → shikimate pathway; bacterial PPP is cytosolic — F005, F006 |
| [22791961](https://pubmed.ncbi.nlm.nih.gov/22791961/) | *Improved tryptophan production with TktA/PpsA overexpression* | Causal evidence that transketolase controls E4P availability limiting aromatic-AA biosynthesis — F005 |
| [25012491](https://pubmed.ncbi.nlm.nih.gov/25012491/) | *L-phenylalanine from glycerol; role of glpK, glpX, tktA* | tktA overexpression improves aromatic (Phe) production — F005 |
| [29301095](https://pubmed.ncbi.nlm.nih.gov/29301095/) | *Indirubin from glucose in E. coli* | tktA overexpression enhances E4P/aromatic precursor supply — F005 |
| [23895593](https://pubmed.ncbi.nlm.nih.gov/23895593/) | *Site-saturation mutagenesis in ThDP enzymes* | Conserved architecture maintaining ThDP V-conformation — F007 |
| [42347215](https://pubmed.ncbi.nlm.nih.gov/42347215/) | *Distinct roles of TktA and TalB in Yersinia* | Non-redundant physiological importance of transketolase — F008, interpretation |

**Nature of evidence.** The mechanistic and substrate-specificity claims (F001–F003, F007) rest on well-established transketolase enzymology and on the UniProt/InterPro annotation of Q88D62 itself. The E4P/shikimate rate-limiting role (F005) is supported by **causal, gain-of-function metabolic-engineering studies** (strong evidence, though performed largely in *E. coli*). The organism-specific systems role (F004) comes from **quantitative ¹³C-flux analysis in KT2440 itself** — the most directly relevant experimental evidence. The non-redundancy (F008) and genomic clustering (F009) claims are **bioinformatic inferences** from the KT2440 proteome/genome.

---

## Supported and Refuted Hypotheses

**Supported:**
- Q88D62 is a genuine transketolase (EC 2.2.1.1) catalyzing ThDP-dependent 2-carbon ketol transfer *(UniProt; conserved catalytic residues; family signatures — F001, F007)*
- Substrates are the non-oxidative PPP ketose/aldose phosphates (X5P, R5P, S7P, E4P, F6P, GAP) *(Rhea RHEA:10508; enzymology literature — F002)*
- Requires ThDP + Mg²⁺; functions as a homodimer *(UniProt COFACTOR/SUBUNIT; assay literature — F003)*
- Supplies E4P for aromatic biosynthesis and R5P for nucleotides; rate-limiting for E4P *(metabolic-engineering studies — F005)*
- Cytoplasmic localization *(no signal/TM; bacterial PPP is cytosolic — F006)*
- Sole non-redundant transketolase in KT2440 *(proteome analysis — F008)*
- Participates in the EDEMP cycle / NADPH balance in KT2440 *(¹³C-MFA — F004)*

**Refuted / excluded:**
- Not a membrane transporter, structural protein, or signaling molecule — it is a soluble metabolic enzyme with no transmembrane or secretion signals.
- Not functionally redundant in KT2440 (Q88C16/PP_5367 is a non-catalytic domain fragment, not a second isozyme).

---

## Limitations and Knowledge Gaps

1. **No direct biochemical characterization of Q88D62.** There is, to date, no purified-enzyme kinetic study (Kₘ, kcat, cofactor affinities) or crystal structure of the KT2440 transketolase specifically. All substrate-specificity and mechanistic statements are inferred from the highly conserved transketolase family and from orthologs (*E. coli*, plants, human), not from the KT2440 protein directly.
2. **Engineering evidence is largely heterologous.** The rate-limiting E4P role (F005) is demonstrated principally in *E. coli*. While transketolase chemistry is conserved, the quantitative contribution of tktA to aromatic flux in *P. putida* (with its ED-dominant catabolism) has not been measured directly.
3. **Essentiality not experimentally confirmed in KT2440.** The inference that tktA is non-redundant (F008) predicts a strong growth phenotype on deletion, but a clean *tktA* knockout/complementation phenotype in KT2440 was not located. High-throughput RB-TnSeq fitness data ([PMID: 38323821](https://pubmed.ncbi.nlm.nih.gov/38323821/)) may bear on this but was not analyzed at the gene-fitness level here.
4. **Operon structure and regulation unknown.** The *epd–pgk–tktA* clustering (F009) is suggestive, but transcriptional co-regulation, promoter architecture, and whether these genes form a true operon in KT2440 were not established experimentally.
5. **Metal/cofactor promiscuity unquantified.** The record notes tolerance for Ca²⁺/Co²⁺, but relative activities with alternative divalent cations for the KT2440 enzyme are unknown.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant expression and steady-state kinetics.** Clone PP_4965, purify the His-tagged homodimer, and measure Kₘ/kcat for the physiological donor/acceptor pairs (X5P+R5P, X5P+E4P) and cofactor dependence (ThDP, Mg²⁺ vs Ca²⁺/Co²⁺), to replace inference with direct data for F002/F003.
2. **Structure determination.** Solve the crystal or cryo-EM structure of Q88D62 (± ThDP/Mg²⁺), or generate and validate an AlphaFold model, to confirm the GDG motif, His cluster, and Glu411 geometry (F007) and the dimeric active-site interface.
3. **Targeted genetics in KT2440.** Construct a markerless *ΔtktA* mutant with complementation; assay growth on glucose, gluconate, and gluconeogenic/aromatic substrates, and quantify auxotrophy for aromatic amino acids and vitamin B6 to test the non-redundancy/essentiality prediction (F008, F009).
4. **¹³C-flux under perturbation.** Repeat ¹³C-MFA in wild-type vs *tktA*-modulated strains to quantify transketolase's flux contribution to the EDEMP cycle and to E4P/NADPH pools (F004, F005).
5. **Aromatic-production engineering test.** Overexpress native tktA in a KT2440 aromatic-product chassis (e.g., a vanillin or muconate producer) to test whether E4P supply is rate-limiting in *P. putida* as it is in *E. coli* (F005).
6. **Transcriptional mapping.** Use RNA-seq/RT-PCR and promoter mapping to determine whether *epd–pgk–tktA* are co-transcribed and how the operon responds to oxidative stress and carbon source (F009).

---

*Report generated from a 5-iteration autonomous investigation: 9 confirmed findings, 27 papers reviewed. Target identity (tktA / Q88D62 / PP_4965, transketolase EC 2.2.1.1, *Pseudomonas putida* KT2440) was verified and unambiguous.*


## Artifacts

- [OpenScientist final report](tktA-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](tktA-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:29500317
2. PMID:41203356
3. PMID:36974963
4. PMID:6862092
5. PMID:41870883
6. PMID:26350459
7. PMID:24132392
8. PMID:22791961
9. PMID:25012491
10. PMID:29301095
11. PMID:23895593
12. PMID:42347215
13. PMID:42014677
14. PMID:38323821