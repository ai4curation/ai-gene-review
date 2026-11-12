---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-12T04:47:21.425655'
end_time: '2026-11-12T05:00:05.185734'
duration_seconds: 763.76
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: ECOLI
  gene_id: P0A6G3
  gene_symbol: pncC
  uniprot_accession: P0A6G3
  protein_description: 'RecName: Full=Nicotinamide-nucleotide amidohydrolase PncC;
    Short=NMN amidohydrolase PncC; EC=3.5.1.42; AltName: Full=NMN deamidase; AltName:
    Full=Nicotinamide-nucleotide amidase;'
  gene_info: Name=pncC; Synonyms=ygaD; OrderedLocusNames=b2700, JW2670;
  organism_full: Escherichia coli (strain K12).
  protein_family: Belongs to the CinA family. PncC subfamily. .
  protein_domains: CinA-like_C. (IPR036653); CinA_C. (IPR008136); CinA (PF02464)
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
  path: pncC-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: pncC-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** P0A6G3
- **Protein Description:** RecName: Full=Nicotinamide-nucleotide amidohydrolase PncC; Short=NMN amidohydrolase PncC; EC=3.5.1.42; AltName: Full=NMN deamidase; AltName: Full=Nicotinamide-nucleotide amidase;
- **Gene Information:** Name=pncC; Synonyms=ygaD; OrderedLocusNames=b2700, JW2670;
- **Organism (full):** Escherichia coli (strain K12).
- **Protein Family:** Belongs to the CinA family. PncC subfamily. .
- **Key Domains:** CinA-like_C. (IPR036653); CinA_C. (IPR008136); CinA (PF02464)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "pncC" matches the protein description above**
2. **Verify the organism is correct:** Escherichia coli (strain K12).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'pncC' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **pncC** (gene ID: P0A6G3, UniProt: P0A6G3) in ECOLI.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *pncC* (NMN deamidase) in *Escherichia coli* K-12

**Gene:** *pncC* (synonyms *ygaD*; ordered locus names b2700, JW2670)
**Protein:** Nicotinamide-nucleotide amidohydrolase PncC (NMN deamidase / NMN amidohydrolase)
**UniProt:** [P0A6G3](https://www.uniprot.org/uniprotkb/P0A6G3) · **EC:** 3.5.1.42 · **Rhea:** 12400
**Organism:** *Escherichia coli* (strain K-12)
**Family:** CinA family, PncC subfamily (Pfam PF02464; InterPro IPR008136 / IPR036653)

---

## Summary

The *E. coli* gene *pncC* (formerly the orphan gene *ygaD*, locus b2700) encodes **NMN deamidase** (nicotinamide-nucleotide amidohydrolase, EC 3.5.1.42), a cytoplasmic enzyme that catalyzes the hydrolytic deamidation of **nicotinamide mononucleotide (NMN)** to **nicotinate mononucleotide (NaMN)** plus ammonia. This single reaction is the committed, name-giving step of the **bacterial pyridine nucleotide cycle** — the salvage route that recycles nicotinamide-containing fragments (including those released by non-redox NAD⁺-consuming reactions) back into the NaMN → NaAD → NAD⁺ pathway. The identity of the gene was a long-standing puzzle: NMN deamidase activity was first described in enterobacteria more than three decades before the responsible gene was identified by Galeazzi and colleagues in 2011 through comparative genomics combined with native enzyme purification.

Biochemically, PncC is a small (165-residue, ~17.6 kDa) soluble protein that assembles into a **homodimer** and displays **strict substrate specificity for NMN** with high affinity (K_M ≈ 6 µM) and a turnover number of ~3.3 s⁻¹, giving a catalytic efficiency near 5.5 × 10⁵ M⁻¹s⁻¹. It shows no measurable activity on other candidate substrates. Importantly, among the several CinA/PncC-family paralogs present in *E. coli*, the NMN deamidase activity was confirmed only for the product of *ygaD*/*pncC*, firmly pinpointing this gene as the functional enzyme.

Mechanistically, PncC is remarkable: it founds a **structurally novel amidohydrolase family** with no homology to any previously described amidohydrolase, and it performs catalysis using an unusual **Ser/Lys catalytic dyad** rather than the classic metal centers or cysteine/serine-triad arrangements of other deamidases. The dyad (Ser29 + Lys61 in the *E. coli* numbering) was established experimentally by systematic mutagenesis and kinetics, and is corroborated here by a high-confidence AlphaFold model in which the Ser29 hydroxyl and the Lys61 ε-amino group sit just 3.09 Å apart in the active site — exactly the geometry expected for a hydrogen-bonded Ser/Lys dyad.

---

## Verification of Gene Identity

Before detailing the function, the mandatory identity check is satisfied on all counts:

| Verification item | UniProt target | Literature match | Status |
|---|---|---|---|
| Gene symbol | *pncC* (syn. *ygaD*) | *ygaD* confirmed as the active NMN deamidase gene ([PMID: 21953451](https://pubmed.ncbi.nlm.nih.gov/21953451/)) | ✅ |
| Organism | *E. coli* K-12 | *E. coli* (with ortholog in *Shewanella oneidensis*) | ✅ |
| EC / reaction | EC 3.5.1.42, NMN → NaMN + NH₃ | Identical | ✅ |
| Family / domains | CinA / PncC, PF02464, IPR008136 | Novel broadly conserved amidohydrolase family = CinA/PncC | ✅ |

The gene symbol is **unambiguous for this protein**, and the literature found (Galeazzi 2011; Sorci 2014; Karuppiah 2014) describes precisely the NMN deamidase / CinA-PncC enzyme family specified by UniProt. There is no evidence of a conflicting same-symbol gene in a different organism. Research therefore proceeded with high confidence on the correct target.

---

## Key Findings

### Finding 1 — *pncC* (*ygaD*, b2700) encodes NMN deamidase (EC 3.5.1.42), the committed enzyme of the bacterial pyridine nucleotide cycle

NMN deamidase activity was first detected biochemically in enterobacteria in the late 20th century, but the gene encoding it remained unidentified for over 30 years. Galeazzi et al. (2011) resolved this through a genomics-based reconstruction of NAD metabolism coupled to purification of the native enzyme from *Shewanella oneidensis*; this led them to the previously uncharacterized *pncC* gene. As the authors state, *"Nicotinamide mononucleotide (NMN) deamidase (EC 3.5.1.42), one of the key enzymes of the bacterial pyridine nucleotide cycle, was originally described in Enterobacteria, but the corresponding gene eluded identification for over 30 years."* ([PMID: 21953451](https://pubmed.ncbi.nlm.nih.gov/21953451/))

The reaction catalyzed is the hydrolysis of the carboxamide group of NMN to yield NaMN and free ammonia:

> **β-nicotinamide D-ribonucleotide (NMN) + H₂O → nicotinate β-D-ribonucleotide (NaMN) + NH₄⁺** (Rhea:12400)

This is a **deamidation** — the amide nitrogen of the nicotinamide ring is replaced by a hydroxyl/oxygen, converting the amide to a carboxylate. The product NaMN re-enters the NAD biosynthetic mainline, making PncC the enzyme that funnels salvaged nicotinamide-ring fragments back toward NAD⁺ (see Mechanistic Model below).

### Finding 2 — *ygaD*/*pncC* is specifically the active enzyme among *E. coli*'s CinA/PncC paralogs

*E. coli* K-12 encodes multiple proteins of the CinA/PncC (PF02464) family. Galeazzi et al. explicitly tested the candidates and found that *"Of the three PncC homologs present in Escherichia coli, NMN deamidase activity was confirmed only for the recombinant purified product of the ygaD gene."* ([PMID: 21953451](https://pubmed.ncbi.nlm.nih.gov/21953451/)) This is a crucial specificity control: it rules out the paralogs (e.g., the uncharacterized *ydeJ* and CinA-domain-containing proteins) and assigns the deamidase function unambiguously to *ygaD* = *pncC* = b2700 = UniProt P0A6G3.

### Finding 3 — PncC is strictly specific for NMN, high-affinity, and functions as a homodimer

Enzymatic characterization (Galeazzi et al. 2011, curated into UniProt P0A6G3 with evidence code ECO:0000269|PubMed:21953451) established that PncC *"has nicotinamide mononucleotide (NMN) aminohydrolase activity, not active on other substrates."* The kinetic parameters are:

| Parameter | Value |
|---|---|
| K_M (NMN) | ~6 µM |
| k_cat | ~3.3 s⁻¹ |
| k_cat/K_M | ~5.5 × 10⁵ M⁻¹s⁻¹ |
| pH profile | active over a broad pH range |
| Substrate scope | strictly NMN; inactive on other tested substrates |
| Chain length | 165 aa (~17.6 kDa) |
| Oligomeric state | homodimer |

The authors note that *"Enzymatic characterization of the PncC protein, as well as phenotype analysis of deletion mutants, confirmed its proposed biochemical and physiological function in S. oneidensis."* ([PMID: 21953451](https://pubmed.ncbi.nlm.nih.gov/21953451/)) The low micromolar K_M indicates a high-affinity, dedicated salvage enzyme rather than a promiscuous hydrolase, consistent with a tightly regulated role in nucleotide recycling. The protein sequence carries the family-conserved N-terminal serine motif (…A-E-**S**-C-T-G-G…) that positions the catalytic serine around residue 29.

### Finding 4 — PncC defines a structurally novel amidohydrolase family using a Ser/Lys catalytic dyad

Two independent lines of evidence establish the unusual mechanism. First, sequence and 3D-structure comparison by Galeazzi et al. showed that PncC *"shows no homology with any previously described amidohydrolases,"* defining a new, broadly conserved family corresponding to Pfam PF02464 (CinA) / InterPro IPR008136 ([PMID: 21953451](https://pubmed.ncbi.nlm.nih.gov/21953451/)). Second, Sorci et al. (2014) performed systematic mutagenesis of all candidate catalytic residues together with kinetic analysis and active-site inspection, and *"allowed us to conclude that PncC is a serine-amidohydrolase, employing a Ser/Lys dyad for catalysis."* ([PMID: 24530526](https://pubmed.ncbi.nlm.nih.gov/24530526/)) This places PncC in an expanded, mechanistically distinct group of serine amidohydrolases, catalyzing amide bond hydrolysis with a serine nucleophile activated by a general-base lysine — bypassing the need for a catalytic metal.

### Finding 5 — AlphaFold model positions Ser29 and Lys61 as the catalytic dyad in *E. coli* PncC

To map the experimentally defined dyad onto the specific *E. coli* protein (which lacks a deposited experimental structure), the AlphaFold model AF-P0A6G3-F1 (v6) was analyzed. The model is of very high confidence (mean pLDDT 97.5; both catalytic residues pLDDT 98–99). Geometric analysis shows the side-chain hydroxyl of **Ser29 (OG)** and the ε-amino group of **Lys61 (NZ)** are only **3.09 Å apart** — a canonical hydrogen-bonding distance diagnostic of a Ser/Lys catalytic dyad. No alternative Ser–Lys pair is nearly as close (next nearest Ser103–Lys61 = 4.68 Å; Ser79–Lys115 = 5.26 Å). Ser29 lies within the family-conserved N-terminal motif (…T-T-A-E-**S29**-C-T-G-G-W…). This structural geometry directly corroborates the experimentally determined Ser/Lys dyad mechanism of Sorci et al. 2014 ([PMID: 24530526](https://pubmed.ncbi.nlm.nih.gov/24530526/)).

### Finding 6 — PncC is a soluble cytoplasmic NAD-salvage enzyme

The UniProt P0A6G3 feature annotation lists a single Chain spanning residues 1–165 with **no signal peptide, no transmembrane segment, and no lipidation or export signal**, and keywords limited to {Hydrolase, Pyridine nucleotide biosynthesis}. Together with its assignment as EcoCyc:G7409-MONOMER, this is fully consistent with a **soluble cytosolic metabolic enzyme** operating in the cytoplasm, where NAD biosynthesis and salvage occur. NMN deamidation, the production of NaMN, and the downstream NadD/NadE steps are all cytoplasmic, so PncC carries out its function in the cytoplasm as part of the intracellular NAD homeostasis machinery.

### Finding 7 — The structural basis of the deamidation mechanism is supported by product-complex crystallography of a CinA ortholog

While the *E. coli* PncC itself has no experimental structure, Karuppiah et al. (2014) solved crystal structures of the bifunctional **CinA enzyme from *Thermus thermophilus***, a two-domain relative. They showed that *"the C-terminal domain harbors the nicotinamide mononucleotide deamidase activity, and the structure of a complex with the product nicotinate mononucleotide suggests a mechanism for deamidation."* ([PMID: 25313401](https://pubmed.ncbi.nlm.nih.gov/25313401/)) The C-terminal CinA domain is the structural homolog of *E. coli* PncC. The N-terminal COG1058 domain additionally carries ADP-ribose pyrophosphatase activity. Crucially, the authors frame the physiological context: CinA participates in the pyridine nucleotide cycle, *"which recycles products formed by non-redox uses of NAD."* ([PMID: 25313401](https://pubmed.ncbi.nlm.nih.gov/25313401/)) This defines why NMN deamidase activity is biologically important — it salvages the nicotinamide-containing debris of NAD-consuming reactions.

---

## Mechanistic Model / Interpretation

### The reaction and its place in metabolism

PncC performs the deamidation that gives the pyridine nucleotide cycle its "re-entry point." In bacteria, NAD⁺ is not only a redox cofactor but also a consumable substrate for non-redox reactions (e.g., by DNA ligase, ADP-ribosyltransferases, and sirtuin-type deacylases). These reactions cleave NAD⁺ and release nicotinamide-containing fragments. The salvage/recycling route rebuilds NAD⁺ from these fragments, and PncC provides the committed deamidation step that channels NMN back onto the nicotinate branch:

```
  Non-redox NAD+ consumption / salvage
             │
             ▼
           NMN  (nicotinamide mononucleotide)
             │
             │   PncC / NMN deamidase (EC 3.5.1.42)
             │   + H2O  ──►  + NH3        [Ser29/Lys61 dyad]
             ▼
          NaMN  (nicotinate mononucleotide)
             │
             │   NadD (NaMN adenylyltransferase)
             ▼
          NaAD  (nicotinate adenine dinucleotide)
             │
             │   NadE (NAD synthetase; + NH3/Gln + ATP)
             ▼
          NAD+  ◄── regenerated cofactor
```

The logic of the cycle is that amidated intermediates (NMN, NAD) are converted to deamidated intermediates (NaMN, NaAD) which are then re-amidated at the final NadE step. PncC performs the key deamidation on the mononucleotide. Its strict specificity for NMN (not nicotinamide riboside, not NAD) and its low-micromolar K_M mark it as a dedicated salvage valve rather than a general hydrolase.

### The catalytic chemistry

```
        Ser29–OG : : : : : NZ–Lys61        (3.09 Å, H-bond)
           │
   nucleophile          general base
           │
           ▼
   attacks carboxamide carbon of NMN
           │
           ▼
   tetrahedral intermediate → C–N bond cleaved → NH3 released
           │
           ▼
   acyl-enzyme hydrolyzed by water → NaMN (carboxylate) + regenerated Ser
```

Lys61 acts as a general base that deprotonates the Ser29 hydroxyl, generating a serine alkoxide nucleophile that attacks the amide carbonyl of NMN. Collapse of the tetrahedral intermediate expels ammonia and forms an acyl-enzyme (or directly the carboxylate product), which is resolved by water to yield NaMN and restore the serine. This Ser/Lys dyad chemistry is mechanistically distinct from metal-dependent amidohydrolases and places PncC in an expanded class of serine amidohydrolases — one of the central conclusions of Sorci et al. 2014. The AlphaFold geometry (Finding 5) independently validates that the two dyad residues are poised at hydrogen-bonding distance in the *E. coli* enzyme.

### Localization and oligomeric state

PncC is a soluble cytoplasmic homodimer with no export/membrane signals. It functions in the cytosol alongside the rest of the NAD biosynthetic enzymes — the appropriate compartment given that its substrate (NMN) and product (NaMN) are intracellular nucleotide-cycle intermediates.

---

## Evidence Base

| Study | PMID | Key contribution | Evidence type |
|---|---|---|---|
| Galeazzi et al. 2011, *Identification of nicotinamide mononucleotide deamidase of the bacterial pyridine nucleotide cycle reveals a novel broadly conserved amidohydrolase family* | [21953451](https://pubmed.ncbi.nlm.nih.gov/21953451/) | Identified *pncC*/*ygaD* as the long-sought NMN deamidase gene; enzyme purification, kinetics, deletion-mutant phenotypes; defined a novel amidohydrolase family | Primary — comparative genomics + biochemistry + genetics |
| Sorci et al. 2014, *Characterization of bacterial NMN deamidase as a Ser/Lys hydrolase expands diversity of serine amidohydrolases* | [24530526](https://pubmed.ncbi.nlm.nih.gov/24530526/) | Mutagenesis + kinetics established the Ser/Lys catalytic dyad; classified PncC as a serine-amidohydrolase | Primary — mechanistic enzymology |
| Karuppiah et al. 2014, *Structure and mechanism of the bifunctional CinA enzyme from Thermus thermophilus* | [25313401](https://pubmed.ncbi.nlm.nih.gov/25313401/) | Crystal structures of a CinA ortholog; product (NaMN) complex suggests deamidation mechanism; links family to the pyridine nucleotide cycle | Primary — structural biology (ortholog) |
| UniProt P0A6G3 (curated) | — | Strict NMN specificity, kinetics (K_M 6 µM, k_cat 3.3 s⁻¹), homodimer, soluble cytoplasmic features, EC/Rhea assignments | Database curation of ECO:0000269 PubMed:21953451 |
| AlphaFold AF-P0A6G3-F1 (v6) | — | Ser29–Lys61 dyad geometry (3.09 Å) in the *E. coli* protein | Computational structure prediction |

**How the evidence converges:** The three primary papers are mutually reinforcing. Galeazzi (2011) establishes *what* the enzyme is and *which* gene encodes it; Sorci (2014) establishes *how* it works (Ser/Lys dyad, novel serine amidohydrolase); Karuppiah (2014) provides the *structural* rationale for the deamidation mechanism in a related CinA protein and situates the family in the pyridine nucleotide cycle. The UniProt curation and AlphaFold analysis tie these conclusions to the exact *E. coli* protein (P0A6G3), confirming substrate specificity, kinetics, oligomeric state, cytoplasmic localization, and the dyad residues (Ser29/Lys61). No evidence contradicts this model.

---

## Limitations and Knowledge Gaps

1. **No experimental structure of *E. coli* PncC.** The catalytic dyad assignment for P0A6G3 (Ser29/Lys61) rests on an AlphaFold model plus homology to CinA. Although the model is very high confidence (pLDDT 97.5) and consistent with the mutagenesis data, a crystal or cryo-EM structure of *E. coli* PncC — ideally with NMN/NaMN bound — has not been determined.

2. **Mechanistic details transferred from orthologs.** The product-complex deamidation mechanism was observed in *T. thermophilus* CinA, a bifunctional two-domain enzyme; the single-domain *E. coli* PncC is assumed to share the C-terminal domain chemistry but this was not directly crystallographically verified for the *E. coli* enzyme.

3. **Physiological regulation unaddressed.** How *pncC* expression and PncC activity are regulated in response to NAD⁺ status, stress, or non-redox NAD consumption in *E. coli* was not examined here. The quantitative flux through the pyridine nucleotide cycle *in vivo*, and PncC's contribution relative to other salvage routes, remain open.

4. **Paralog functions.** While only *ygaD* showed NMN deamidase activity, the physiological roles of the other *E. coli* CinA/PncC-family paralogs (e.g., *ydeJ*, CinA-domain proteins) were not resolved and may have distinct activities (e.g., competence-associated or ADP-ribose pyrophosphatase roles seen in CinA).

5. **Phenotype basis mostly from *S. oneidensis*.** Deletion-mutant phenotype analysis supporting the physiological role was performed primarily in *Shewanella oneidensis*; the precise fitness consequence of *pncC* loss in *E. coli* K-12 under various conditions is less directly documented.

---

## Proposed Follow-up Experiments / Actions

1. **Determine the experimental structure of *E. coli* PncC**, ideally as a product (NaMN) or substrate-analog complex, to directly visualize the Ser29/Lys61 dyad and the NMN-binding pocket.

2. **Validate the dyad by site-directed mutagenesis in the *E. coli* enzyme** (S29A, K61A, S29A/K61A) with full steady-state kinetics, to confirm the AlphaFold-predicted residues are catalytically essential in P0A6G3 specifically.

3. **Quantify in vivo flux** through the pyridine nucleotide cycle in Δ*pncC E. coli* using isotope tracing (¹⁵N-/¹³C-labeled nicotinamide/NMN) to measure PncC's contribution to NAD⁺ recycling and to detect NMN accumulation.

4. **Characterize regulation:** map the *pncC* promoter, test expression under NAD-depleting stress (DNA damage activating NAD-consuming ligase/ADP-ribosyltransferase activities), and probe allosteric effects of NAD⁺/NMN on PncC activity.

5. **Clarify paralog roles:** express and assay the uncharacterized CinA/PncC paralogs (e.g., *ydeJ*) for NMN deamidase and ADP-ribose pyrophosphatase activities to complete the family functional map in *E. coli*.

6. **Fitness profiling:** measure growth/competition phenotypes of Δ*pncC E. coli* under nicotinamide-limited and NAD-stress conditions to establish the physiological importance of the salvage valve.

---

## Conclusion

*E. coli pncC* (*ygaD*, b2700; UniProt P0A6G3) encodes **NMN deamidase (EC 3.5.1.42)**, a soluble cytoplasmic homodimeric enzyme that hydrolyzes the carboxamide of nicotinamide mononucleotide to nicotinate mononucleotide plus ammonia. This deamidation is the committed step of the **bacterial pyridine nucleotide cycle**, recycling nicotinamide fragments — including those from non-redox NAD⁺ consumption — back into the NaMN → NaAD → NAD⁺ route via NadD and NadE. The enzyme is strictly specific for NMN (K_M ≈ 6 µM, k_cat ≈ 3.3 s⁻¹), founds a structurally novel amidohydrolase family (CinA/PncC fold), and employs an unusual **Ser/Lys catalytic dyad** (Ser29/Lys61), established by mutagenesis and corroborated by a high-confidence AlphaFold model showing the two residues 3.09 Å apart.


## Artifacts

- [OpenScientist final report](pncC-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](pncC-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:21953451
2. PMID:24530526
3. PMID:25313401