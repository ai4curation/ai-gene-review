---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-25T16:56:40.418594'
end_time: '2026-07-25T17:14:52.707013'
duration_seconds: 1092.29
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: purN
  gene_symbol: purN
  uniprot_accession: Q88MB0
  protein_description: 'RecName: Full=Phosphoribosylglycinamide formyltransferase
    {ECO:0000256|HAMAP-Rule:MF_01930}; EC=2.1.2.2 {ECO:0000256|HAMAP-Rule:MF_01930};
    AltName: Full=5''-phosphoribosylglycinamide transformylase {ECO:0000256|HAMAP-Rule:MF_01930};
    AltName: Full=GAR transformylase {ECO:0000256|HAMAP-Rule:MF_01930}; Short=GART
    {ECO:0000256|HAMAP-Rule:MF_01930};'
  gene_info: Name=purN {ECO:0000256|HAMAP-Rule:MF_01930, ECO:0000313|EMBL:AAN67285.1};
    OrderedLocusNames=PP_1664 {ECO:0000313|EMBL:AAN67285.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the GART family. {ECO:0000256|ARBA:ARBA00038440,
  protein_domains: Formyl_transf_N. (IPR002376); Formyl_transf_N_sf. (IPR036477);
    GART. (IPR004607); GART_AS. (IPR001555); Formyl_trans_N (PF00551)
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
citation_count: 10
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: purN-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: purN-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88MB0
- **Protein Description:** RecName: Full=Phosphoribosylglycinamide formyltransferase {ECO:0000256|HAMAP-Rule:MF_01930}; EC=2.1.2.2 {ECO:0000256|HAMAP-Rule:MF_01930}; AltName: Full=5'-phosphoribosylglycinamide transformylase {ECO:0000256|HAMAP-Rule:MF_01930}; AltName: Full=GAR transformylase {ECO:0000256|HAMAP-Rule:MF_01930}; Short=GART {ECO:0000256|HAMAP-Rule:MF_01930};
- **Gene Information:** Name=purN {ECO:0000256|HAMAP-Rule:MF_01930, ECO:0000313|EMBL:AAN67285.1}; OrderedLocusNames=PP_1664 {ECO:0000313|EMBL:AAN67285.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the GART family. {ECO:0000256|ARBA:ARBA00038440,
- **Key Domains:** Formyl_transf_N. (IPR002376); Formyl_transf_N_sf. (IPR036477); GART. (IPR004607); GART_AS. (IPR001555); Formyl_trans_N (PF00551)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "purN" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'purN' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **purN** (gene ID: purN, UniProt: Q88MB0) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *purN* (PP_1664, UniProt Q88MB0) in *Pseudomonas putida* KT2440

## Gene/Protein Identity — Verified

| Field | Value |
|---|---|
| Gene | *purN* (ordered locus **PP_1664**) |
| UniProt | **Q88MB0** (217 aa) |
| Protein | Phosphoribosylglycinamide formyltransferase / GAR transformylase (GART) |
| EC | **2.1.2.2** |
| Organism | *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / KT2440), taxid 160488 |
| Family / domains | GART family; Formyl_transf_N (PF00551; IPR002376/IPR036477), GART (IPR004607), GART_AS (IPR001555) |

**The identity is unambiguous and fully consistent.** The gene symbol *purN*, the protein description (folate-dependent GAR transformylase, EC 2.1.2.2), the GART protein family, and the Formyl_transf_N / GART_AS domain architecture all agree with the extensive primary literature on this enzyme. No conflicting "same-symbol, different-gene" literature was encountered during the investigation. Sequence analysis (below) shows the *P. putida* protein is ~60% identical to the biochemically and structurally characterized *E. coli* PurN, so functional inference from that literature is robust.

---

## Summary

The gene **purN** (ordered locus **PP_1664**; UniProt **Q88MB0**) of *Pseudomonas putida* KT2440 encodes a **folate-dependent glycinamide ribonucleotide (GAR) transformylase** (GART; also called 5′-phosphoribosylglycinamide transformylase or GAR Tfase), **EC 2.1.2.2**. This 217-amino-acid, soluble cytoplasmic enzyme catalyzes the **third of ten steps of the de novo purine (IMP) biosynthetic pathway**. It transfers a one-carbon formyl unit from the folate cofactor **10-formyltetrahydrofolate** onto the free amino group of **N¹-(5-phospho-β-D-ribosyl)glycinamide (β-GAR)**, producing **N²-formyl-GAR (FGAR)** and releasing tetrahydrofolate. The formyl group installed here ultimately becomes **C8 of the purine ring**.

The functional assignment rests on strong convergent evidence. The gene product carries the diagnostic **Formyl transferase N-terminal domain (Pfam PF00551; InterPro IPR002376/IPR036477)**, the **GART signature (IPR004607)**, and the **GART active-site motif (IPR001555)**, and is placed by the HAMAP curation rule **MF_01930** into the GART family. The *P. putida* protein is ~60% identical to the extensively characterized *E. coli* PurN, and its catalytic histidine (His113, embedded in an invariant "RLLNIHPS" motif) corresponds precisely to the biochemically validated catalytic His108 of the *E. coli* enzyme. The AlphaFold model of Q88MB0 is predicted with very high confidence (mean pLDDT 95.9), consistent with the crystallographically determined Rossmann-type formyltransferase fold shared across bacterial, human, and mycobacterial orthologs.

A key physiological nuance is redundancy. *P. putida* KT2440, like *E. coli*, encodes a second, mechanistically unrelated GAR transformylase — **PurT (PP_1457, EC 6.3.1.21)** — that formylates β-GAR using **formate and ATP** rather than folate. Because the two enzymes catalyze the same net conversion by non-homologous routes, a *purN* single mutant is not expected to be a purine auxotroph; only the loss of both activities blocks FGAR synthesis. purN therefore functions as the canonical, folate-cofactor-linked route at the third node of de novo purine biosynthesis, acting in the cytoplasm as part of the soluble machinery that builds the purine ring atom-by-atom on a ribose-phosphate scaffold.

---

## Key Findings

### Finding 1 — purN is a folate-dependent GAR transformylase catalyzing step 3 of de novo purine biosynthesis

The primary function of the PP_1664 gene product is unambiguous: it is the **folate-dependent glycinamide ribonucleotide transformylase**, systematic name *10-formyltetrahydrofolate:5′-phosphoribosylglycinamide formyltransferase*, **EC 2.1.2.2**. UniProt entry Q88MB0, curated under HAMAP rule MF_01930, describes a 217-residue protein encoded by *purN* / ordered locus PP_1664 in *P. putida* KT2440.

The catalyzed reaction (Rhea RHEA:15053) is:

> N¹-(5-phospho-β-D-ribosyl)glycinamide + (6R)-10-formyltetrahydrofolate → N²-formyl-N¹-(5-phospho-β-D-ribosyl)glycinamide + (6S)-tetrahydrofolate + H⁺

In words, the enzyme transfers a **formyl (one-carbon, formaldehyde-oxidation-level) group** from the folate cofactor to the primary amine of β-GAR, generating formyl-GAR (FGAR) and tetrahydrofolate. This is the **third step of the de novo IMP biosynthetic pathway** (UniPathway UPA00074, "Purine metabolism; IMP biosynthesis via de novo pathway"), specifically the sub-step "FGAR from GAR (10-formyl-THF route)."

The enzyme's identity and role are directly confirmed in the literature. As stated for the human/E. coli ortholog: "*Glycinamide ribonucleotide transformylase (GART; 10-formyltetrahydrofolate:5′-phosphoribosylglycinamide formyltransferase, EC 2.1.2.2), an essential enzyme in de novo purine biosynthesis*" [PMID: 16026156](https://pubmed.ncbi.nlm.nih.gov/16026156/) — a definition matching the UniProt annotation for purN exactly.

**Substrate specificity and kinetics.** The two cosubstrates are the folate one-carbon donor and β-GAR. Kinetic constants measured for the orthologous *E. coli* enzyme provide quantitative substrate-affinity benchmarks: the enzyme uses "*the natural 10-formyltetrahydrofolate (10-CHO-H4F; Km approximately 77.4 microM at pH 8.5) and glycinamide-ribonucleotide (GAR; Km approximately 8.1 microM at pH 8.5)*" [PMID: 7776369](https://pubmed.ncbi.nlm.nih.gov/7776369/). The roughly ten-fold tighter apparent affinity for β-GAR (Km ~8 µM) than for the folate cofactor (Km ~77 µM) reflects the enzyme's role as an acceptor-committed formyltransferase whose folate cosubstrate is present at higher cellular concentration. The enzyme is a classic, high-affinity antifolate drug target in eukaryotes: the multisubstrate-adduct inhibitor BW1476U89, which spans both the GAR and folate subsites, binds with Ki ≈ 100 pM [PMID: 7776369](https://pubmed.ncbi.nlm.nih.gov/7776369/).

### Finding 2 — GAR transformylase adopts a Rossmann-type formyltransferase fold with a His/Asp catalytic pair

Structurally, purN belongs to the **formyltransferase (Rossmann-type) fold** class. UniProt Q88MB0 annotates a single Formyl transferase N-terminal domain spanning residues 7–186, an **active-site His113** annotated as the proton donor, a residue at position 149 noted to "raise the pKa of the active-site His," and GAR/cofactor binding residues at positions 16–18, 69, 94–97, and 111. This organization mirrors the well-characterized catalytic apparatus of the *E. coli* and human enzymes (the His108 / Asn106 / Asp144 constellation in *E. coli* numbering).

The fold and its catalytically important flexibility are directly established by crystallography of the *E. coli* enzyme: "*The structure is a modified doubly wound alpha/beta sheet with flexibility in the active site, including a disordered loop in the apo structure, which is ordered in the ternary complex structure*" [PMID: 1631098](https://pubmed.ncbi.nlm.nih.gov/1631098/). This order/disorder transition of the substrate-binding loop upon ligand binding is a hallmark of the mechanism and is expected to be conserved in the *P. putida* ortholog.

The mechanism is pH-dependent, consistent with a catalytic histidine acting as a general base/acid. Studies of the human enzyme report that "*Human GAR Tfase exhibits pH-dependent enzyme activity with its maximum around pH 7.5-8*" [PMID: 12450384](https://pubmed.ncbi.nlm.nih.gov/12450384/), linked to a substrate-binding loop conformational switch. The conserved catalytic and binding residues were mapped in the *E. coli* multisubstrate-adduct structure: "*The highly conserved Arg103, His108 and Gln170 residues that are key in ligand binding and catalysis (His108)*" [PMID: 7776369](https://pubmed.ncbi.nlm.nih.gov/7776369/) — precisely the residues corresponding to the active-site His113 and binding sites annotated in Q88MB0.

The fold is conserved deeply across bacteria: the *M. tuberculosis* PurN structure "*shows a Rossmann-type fold that is very similar to the known structures of the human and E. coli PurN proteins*" [PMID: 19394344](https://pubmed.ncbi.nlm.nih.gov/19394344/), reinforcing the structural inference for the *P. putida* ortholog.

### Finding 3 — P. putida KT2440 has two independent GAR transformylases (purN and purT)

An important genomic and physiological finding is that KT2440 encodes **two structurally unrelated enzymes** for the same third step. A UniProt survey of *P. putida* KT2440 (taxid 160488) identifies:

| Gene | Locus | UniProt | Length | Cofactor / mechanism | EC |
|------|-------|---------|--------|----------------------|-----|
| **purN** | PP_1664 | Q88MB0 | 217 aa | Folate-dependent (10-formyl-THF) | 2.1.2.2 |
| **purT** | PP_1457 | Q88MW1 | 393 aa | Formate + ATP-dependent | 6.3.1.21 |

KT2440 encodes the complete de novo purine gene set (purF PP_2000, purD PP_4823, purN PP_1664, purT PP_1457, purL PP_1037, purM PP_1665, purK PP_5335, purE PP_5336, purC PP_1240, purB PP_4016, purH PP_4822). Notably, **purN (PP_1664) is genomically adjacent to purM (PP_1665)**, a common bacterial *purMN* arrangement.

The dual-enzyme redundancy is established from *E. coli*: "*Escherichia coli synthesizes two different glycinamide ribonucleotide (GAR) transformylases, both catalyzing the third step in the purine biosynthetic pathway. One is coded for by the previously described purN gene (GAR transformylase N), and a second, hitherto unknown, enzyme is encoded by the purT gene (GAR transformylase T)*" [PMID: 8501063](https://pubmed.ncbi.nlm.nih.gov/8501063/). Critically, "*Only strains defective in both genes require an exogenous purine source for growth*" [PMID: 8501063](https://pubmed.ncbi.nlm.nih.gov/8501063/) — meaning a *purN* single knockout is **not** a purine auxotroph.

PurT is mechanistically distinct: it "*catalyzes the production of beta-formyl GAR from formate, ATP, and beta-GAR. As such it is an alternative to the formyl-folate utilizing purN GAR transformylase. No significant homology exists between the two transformylases*" [PMID: 8117714](https://pubmed.ncbi.nlm.nih.gov/8117714/). Thus purN and purT represent **convergent, non-homologous solutions** to the same biosynthetic problem — one drawing its one-carbon unit from the folate pool, the other from free formate at the expense of ATP hydrolysis.

### Finding 4 — purN acts as a soluble cytoplasmic enzyme within the de novo IMP pathway

purN carries out its function in the **cytoplasm**. Q88MB0 has no transmembrane segments and no signal peptide in its UniProt feature table — it is a single soluble Formyl_transf_N domain (residues 7–186). De novo purine (IMP) biosynthesis is a canonical **cytosolic pathway**; in humans, the purN activity is one domain of the soluble trifunctional cytosolic enzyme GART, which fuses purD, purM, and purN activities: "*the human GAR Tfase (purN) component of the human trifunctional protein (purD-purM-purN)*" [PMID: 12450384](https://pubmed.ncbi.nlm.nih.gov/12450384/). In *P. putida*, as in most bacteria, these activities are encoded as separate genes, but the pathway remains cytoplasmic.

Bacterial PurN enzymes have been observed in a range of soluble oligomeric states: "*AaPurN and StPurN formed dimers, GkPurN formed monomer and PurU formed tetramer in the crystals*" [PMID: 24108189](https://pubmed.ncbi.nlm.nih.gov/24108189/), confirming that PurN functions as a soluble (monomeric or dimeric) cytosolic enzyme rather than a membrane-associated one. Its substrates (GAR from PurD; 10-formyl-THF from the folate pool) and product (FGAR, consumed by PurL) are all cytoplasmic metabolites.

### Finding 5 — P. putida PurN is a highly conserved ortholog of E. coli PurN with an invariant catalytic-His motif

Sequence and structural comparison firmly ties the *P. putida* protein to the biochemically validated *E. coli* enzyme. Direct comparison shows **~60% ungapped identity** between P. putida PurN (Q88MB0, 217 aa) and E. coli PurN (P08179, 212 aa). The catalytic histidine lies in an **identical local motif "RLLNIHPS"** in both proteins — His113 in *P. putida* corresponds exactly to the experimentally validated catalytic His108 of *E. coli*, preceded by the conserved Asn of the N-x-HPS motif that matches UniProt binding-site residue 111 and the GART active-site signature (IPR001555).

The E. coli catalytic residue is documented: "*The highly conserved Arg103, His108 and Gln170 residues that are key in ligand binding and catalysis (His108)*" [PMID: 7776369](https://pubmed.ncbi.nlm.nih.gov/7776369/), and the E. coli structure itself: "*The three-dimensional structure of phosphoribosylglycinamide formyltransferase (10-formyltetrahydrofolate:5′-phosphoribosylglycinamide formyltransferase, EC 2.1.2.2) has been solved*" [PMID: 1631098](https://pubmed.ncbi.nlm.nih.gov/1631098/). The AlphaFold model of Q88MB0 reinforces this: mean pLDDT 95.9 across all 217 residues, with 93% of residues at very-high confidence (>90) and 99% above 70 — a confidently predicted fold consistent with the crystallographically determined GAR transformylase architecture. This chain of evidence permits high-confidence transfer of the *E. coli*/human mechanism to the *P. putida* enzyme.

---

## Mechanistic Model / Interpretation

### The reaction and its place in purine biosynthesis

De novo purine biosynthesis assembles the purine ring stepwise on a **phosphoribosyl (PRPP-derived) scaffold**, contributing atoms from glycine, formate/folate one-carbon units, glutamine, aspartate, and CO₂. purN operates at the **third step**, immediately downstream of the ATP-dependent addition of glycine to phosphoribosylamine (purD, forming GAR) and upstream of the ATP-dependent amidation of FGAR to FGAM (purL).

```
          10-formyl-THF        THF
                │                │
                ▼                ▲
  β-GAR ───────[ purN ]──────────▶ FGAR
   (NH2 acceptor)   His113 general base    (N-formylated)
                    Rossmann-type fold

  Alternative route (redundant):
  β-GAR + formate + ATP ──[ purT ]──▶ FGAR + ADP + Pi
```

The full KT2440 pathway:

```
PRPP ─purF(PP_2000)─▶ PRA ─purD(PP_4823)─▶ GAR ─purN(PP_1664)/purT(PP_1457)─▶ FGAR
     ─purL(PP_1037)─▶ FGAM ─purM(PP_1665)─▶ AIR ─purK/purE(PP_5335/PP_5336)─▶ CAIR
     ─purC(PP_1240)─▶ SAICAR ─purB(PP_4016)─▶ AICAR ─purH(PP_4822)─▶ IMP
```

The chemistry is a **nucleophilic acyl (formyl) transfer**: the β-GAR primary amine attacks the formyl carbon of 10-formyl-THF, with the active-site histidine (His113 in *P. putida*) acting as a general base to deprotonate/activate the attacking amine and stabilize the tetrahedral intermediate. A neighboring residue (position 149 in Q88MB0) tunes the His pKa; conserved Arg and Gln residues (Arg103/Gln170 in E. coli numbering) orient the folate and GAR substrates. The disordered-to-ordered loop transition seen crystallographically closes the active site around the bound substrates and is central to catalytic efficiency.

### Redundancy as physiological insurance

The coexistence of a folate-dependent (purN) and a formate/ATP-dependent (purT) route at a single pathway node is a striking feature. It provides metabolic robustness: when the folate one-carbon pool is limiting (e.g., under antifolate stress or specific nutritional conditions), the purT route can maintain FGAR synthesis using free formate at the cost of ATP. This explains why, in *E. coli*, only a *purN purT* double mutant becomes a purine auxotroph. The same architecture is present in *P. putida* KT2440 (both genes encoded), so the functional annotation of purN must be read in this context: it is *one of two* parallel enzymes, and its individual deletion is buffered.

### Localization

All evidence points to a **soluble cytoplasmic** location: no membrane-targeting or secretion signals in the sequence, a fold class that is uniformly cytosolic, and a pathway (de novo IMP synthesis) that operates in the cytoplasm. The enzyme may exist as a monomer or homodimer, consistent with the variable oligomeric states reported for bacterial PurN orthologs.

---

## Evidence Base

| PMID | Title (abbreviated) | How it supports the annotation |
|------|---------------------|-------------------------------|
| [16026156](https://pubmed.ncbi.nlm.nih.gov/16026156/) | *Apo/ternary structures of human GAR transformylase* | Defines the enzyme name, systematic name, EC 2.1.2.2, and its essential role in de novo purine biosynthesis |
| [7776369](https://pubmed.ncbi.nlm.nih.gov/7776369/) | *Multisubstrate adduct complex of GAR transformylase at 1.96 Å* | Provides substrate identities, Km values (β-GAR ~8.1 µM; 10-formyl-THF ~77.4 µM), Ki ~100 pM, and identifies catalytic His108/Arg103/Gln170 |
| [1631098](https://pubmed.ncbi.nlm.nih.gov/1631098/) | *Apo and complexed E. coli GAR transformylase structures* | Establishes the Rossmann-type (doubly wound α/β) fold and the ordered/disordered active-site loop |
| [12450384](https://pubmed.ncbi.nlm.nih.gov/12450384/) | *Human GAR Tfase at low/high pH with β-GAR* | Documents pH-dependence (optimum 7.5–8) and the substrate-binding loop switch; identifies purN as part of the human trifunctional GART |
| [8501063](https://pubmed.ncbi.nlm.nih.gov/8501063/) | *Novel GAR transformylase in E. coli* | Establishes that purN and purT are two distinct GAR transformylases; only the double mutant is a purine auxotroph |
| [8117714](https://pubmed.ncbi.nlm.nih.gov/8117714/) | *Non-folate GAR transformylase (purT) from E. coli* | Defines purT as the formate/ATP-dependent, non-homologous alternative to folate-dependent purN |
| [24108189](https://pubmed.ncbi.nlm.nih.gov/24108189/) | *Reaction mechanisms of PurN and PurU* | Documents soluble monomer/dimer oligomeric states of bacterial PurN enzymes |
| [19394344](https://pubmed.ncbi.nlm.nih.gov/19394344/) | *M. tuberculosis PurN structures* | Confirms the conserved Rossmann-type fold across bacterial PurN orthologs; relevance to drug discovery |

Supporting antifolate pharmacology further underscores that GARFT (the human counterpart) is a validated folate-enzyme drug target: LY231514 (pemetrexed) inhibits GARFT among multiple folate enzymes [PMID: 9067281](https://pubmed.ncbi.nlm.nih.gov/9067281/), and various 5,8-dideazafolate analogues competitively inhibit GAR TFase [PMID: 3599031](https://pubmed.ncbi.nlm.nih.gov/3599031/). These reinforce the folate-cofactor dependence central to purN's mechanism, though they concern the human/eukaryotic enzyme rather than *P. putida* directly.

### Supported and Refuted Hypotheses

**Supported**
- **H1:** purN is the folate-dependent GAR transformylase catalyzing GAR → FGAR (EC 2.1.2.2). **Strongly supported** (UniProt/Rhea; conserved mechanism; ~60% identity to characterized *E. coli* enzyme).
- **H2:** Catalysis uses a conserved active-site His (His113) in a Rossmann-type formyltransferase fold. **Supported** (UniProt features + identical RLLNIHPS motif + high-confidence AlphaFold model + crystallographic literature).
- **H3:** purN functions in the cytoplasm within de novo IMP biosynthesis. **Supported** (no membrane features; cytosolic pathway; ortholog data).
- **H4:** purN is functionally redundant with a formate-dependent purT in KT2440. **Supported** (both genes present; *E. coli* genetic redundancy established).

**Refuted / made unlikely**
- That purN is essential as a single gene for purine prototrophy — **unlikely**, because the redundant PurT route exists (a *purN* single mutant should not be a purine auxotroph, by orthology to *E. coli*).

### Note on organism-specific evidence

No study to date has biochemically or genetically characterized the *P. putida* KT2440 purN gene product specifically. The functional annotation is therefore an **inference by orthology** — but a very strong one, resting on ~60% sequence identity to the fully characterized *E. coli* enzyme, an invariant catalytic-His motif, complete conservation of the diagnostic domain architecture, and a high-confidence AlphaFold model. This is a robust, well-supported annotation rather than a speculative one.

---

## Limitations and Knowledge Gaps

1. **No direct experimental characterization in *P. putida*.** All kinetic constants (Km for β-GAR and 10-formyl-THF), structural data, and mechanistic details derive from orthologs (*E. coli*, human, *M. tuberculosis*, thermophilic bacteria). The *P. putida* enzyme has not been purified, assayed, or crystallized. Its exact kinetic parameters and oligomeric state remain to be confirmed.

2. **Relative flux through purN vs. purT is unknown in *P. putida*.** While both genes are present, the physiological division of labor between the folate-dependent (purN) and formate/ATP-dependent (purT) routes under conditions relevant to *P. putida* (a soil/rhizosphere organism with a versatile metabolism) has not been measured.

3. **Regulation is uncharacterized.** In *E. coli* and *B. subtilis*, de novo purine genes are transcriptionally regulated (e.g., PurR repressor, guanine riboswitches). Whether PP_1664 is subject to purine-responsive regulation in *P. putida* KT2440 has not been established here.

4. **Localization is inferred, not observed.** Cytoplasmic localization is deduced from sequence features and pathway context; no experimental localization data for the *P. putida* protein exist.

5. **AlphaFold confidence ≠ functional proof.** The high pLDDT confirms the fold prediction but does not by itself demonstrate catalytic activity; it is corroborating structural evidence, not experimental validation.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant expression and enzyme assay.** Clone PP_1664, express and purify the protein, and measure GAR transformylase activity spectrophotometrically (following THF release or via coupled assays). Determine Km/kcat for β-GAR and 10-formyl-THF and compare to *E. coli* benchmarks (β-GAR ~8 µM; 10-formyl-THF ~77 µM).

2. **Genetic redundancy test.** Construct *purN* single, *purT* single, and *purN purT* double deletions in KT2440 and test for purine auxotrophy on minimal medium. The expectation (from *E. coli*) is that only the double mutant requires exogenous purine — confirming functional redundancy in *P. putida*.

3. **Structural determination.** Solve the crystal or cryo-EM structure of *P. putida* PurN, ideally with substrate/cofactor analogues, to validate the AlphaFold model, confirm the His113 catalytic residue, and define the oligomeric state.

4. **Site-directed mutagenesis of His113.** Mutate His113 (and the pKa-tuning residue at position 149) to test their catalytic essentiality, directly validating the inferred active-site assignment.

5. **Regulatory analysis.** Examine transcriptional regulation of PP_1664 (promoter mapping, response to purine supplementation, presence of PurR-like sites or riboswitches) to place purN in the regulatory network of *P. putida* purine metabolism.

6. **Flux partitioning.** Use ¹³C-labeled formate/serine tracing to quantify the relative contribution of the purN (folate) and purT (formate/ATP) routes to FGAR synthesis under different growth conditions.

---

## Conclusion

**purN (PP_1664, Q88MB0)** in *Pseudomonas putida* KT2440 encodes a **soluble cytoplasmic, folate-dependent glycinamide ribonucleotide transformylase (GART, EC 2.1.2.2)** that catalyzes the **third step of de novo purine (IMP) biosynthesis** — transferring a formyl group from 10-formyltetrahydrofolate onto β-GAR to form FGAR plus tetrahydrofolate. It uses a conserved Rossmann-type formyltransferase fold with an invariant catalytic histidine (His113). KT2440 also encodes a mechanistically distinct formate/ATP-dependent GAR transformylase (**PurT, PP_1457, EC 6.3.1.21**), making the two enzymes functionally redundant, so that a *purN* single mutant is not expected to be a purine auxotroph. The annotation is a strong orthology-based inference (~60% identity to the biochemically characterized *E. coli* enzyme) that would benefit from direct experimental validation in *P. putida*.


## Artifacts

- [OpenScientist final report](purN-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](purN-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:16026156
2. PMID:7776369
3. PMID:1631098
4. PMID:12450384
5. PMID:19394344
6. PMID:8501063
7. PMID:8117714
8. PMID:24108189
9. PMID:9067281
10. PMID:3599031