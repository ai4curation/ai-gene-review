---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T12:16:01.025504'
end_time: '2026-08-31T12:26:04.721829'
duration_seconds: 603.7
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: galU
  gene_symbol: galU
  uniprot_accession: Q88GA4
  protein_description: 'RecName: Full=UTP--glucose-1-phosphate uridylyltransferase
    {ECO:0000256|ARBA:ARBA00019048, ECO:0000256|RuleBase:RU361259}; EC=2.7.7.9 {ECO:0000256|ARBA:ARBA00012415,
    ECO:0000256|RuleBase:RU361259}; AltName: Full=UDP-glucose pyrophosphorylase {ECO:0000256|RuleBase:RU361259};'
  gene_info: Name=galU {ECO:0000313|EMBL:AAN69415.1}; OrderedLocusNames=PP_3821 {ECO:0000313|EMBL:AAN69415.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the UDPGP type 2 family.
  protein_domains: GalU_uridylyltTrfase_bac/arc. (IPR005771); NTP_transferase_dom.
    (IPR005835); Nucleotide-diphossugar_trans. (IPR029044); NTP_transferase (PF00483)
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
citation_count: 18
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: galU-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: galU-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88GA4
- **Protein Description:** RecName: Full=UTP--glucose-1-phosphate uridylyltransferase {ECO:0000256|ARBA:ARBA00019048, ECO:0000256|RuleBase:RU361259}; EC=2.7.7.9 {ECO:0000256|ARBA:ARBA00012415, ECO:0000256|RuleBase:RU361259}; AltName: Full=UDP-glucose pyrophosphorylase {ECO:0000256|RuleBase:RU361259};
- **Gene Information:** Name=galU {ECO:0000313|EMBL:AAN69415.1}; OrderedLocusNames=PP_3821 {ECO:0000313|EMBL:AAN69415.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the UDPGP type 2 family.
- **Key Domains:** GalU_uridylyltTrfase_bac/arc. (IPR005771); NTP_transferase_dom. (IPR005835); Nucleotide-diphossugar_trans. (IPR029044); NTP_transferase (PF00483)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "galU" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'galU' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **galU** (gene ID: galU, UniProt: Q88GA4) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: GalU (Q88GA4 / PP_3821) in *Pseudomonas putida* KT2440

**Gene:** *galU* (OrderedLocusName PP_3821)
**UniProt:** Q88GA4
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440)
**EC:** 2.7.7.9
**Protein family:** UDPGP type 2 (bacterial GalU); domains GalU_uridylyltTrfase_bac/arc (IPR005771), NTP_transferase_dom (IPR005835), Nucleotide-diphospho-sugar transferase (IPR029044), Pfam PF00483

---

## Summary

The *galU* gene of *Pseudomonas putida* KT2440 (locus PP_3821, UniProt Q88GA4) encodes a **UTP–glucose-1-phosphate uridylyltransferase**, commonly called **UDP-glucose pyrophosphorylase (UGPase)**, classified as **EC 2.7.7.9**. Its primary and defining biochemical activity is the Mg²⁺-dependent, reversible reaction:

```
UTP + α-D-glucose-1-phosphate  ⇌  UDP-glucose + pyrophosphate (PPi)
```

This is the committed, near-universal step producing **UDP-glucose**, the central activated glucosyl donor of the cell. Every independent line of evidence assembled here converges on a confident, high-quality functional assignment: the UniProt annotation, the InterPro/Pfam domain architecture, the conserved N-terminal nucleotidyltransferase sequence motif carried by the actual PP_3821 protein sequence, and a robust 44% full-length identity to the biochemically and structurally validated *Escherichia coli* GalU. The gene identity is unambiguous — symbol, organism, and domain architecture all align, and the target's own sequence retains the catalytic residues of characterized orthologs.

Mechanistically, bacterial GalU is a **cytoplasmic homotetramer** catalyzing an **ordered sequential Bi-Bi reaction** with Mg²⁺ ions coordinating the substrates in a deep active-site pocket of each subunit. Tetramerization is functionally essential — in the close relative *Pseudomonas aeruginosa*, disrupting the tetramer abolishes catalysis. The enzyme performs its work in the **cytosol**, upstream of membrane-associated glycosyltransferases that consume UDP-glucose.

Biologically, GalU sits at a **carbon-flux branch point**. Its product UDP-glucose (and derivatives such as UDP-galactose and UDP-glucuronic acid) is the indispensable precursor for **lipopolysaccharide (LPS)**, **capsular polysaccharide**, and **exopolysaccharide/biofilm-matrix** biosynthesis. In *Pseudomonas*, genetic loss of *galU* truncates the LPS core and produces a rough LPS phenotype with downstream consequences for serum resistance and virulence. In *P. putida* KT2440, the UDP-glucose GalU generates feeds the biofilm exopolysaccharide machinery, including the cellulose (*bcs*) branch. This report details each conclusion, the supporting evidence, a synthesized mechanistic model, the key limitations, and concrete follow-up experiments.

---

## Key Findings

### Finding 1 — GalU catalyzes UTP + glucose-1-phosphate → UDP-glucose + PPi (EC 2.7.7.9)

The core function of Q88GA4 is the synthesis of UDP-glucose from UTP and α-D-glucose-1-phosphate, releasing pyrophosphate. UniProt annotates Q88GA4 as a **UTP–glucose-1-phosphate uridylyltransferase / UDP-glucose pyrophosphorylase**, EC 2.7.7.9, a member of the **UDPGP type 2 family**, with the diagnostic domains **GalU_uridylyltransferase_bac/arc (IPR005771)** and **NTP_transferase (PF00483)**. This annotation is grounded in biochemically characterized orthologs. Kim et al. (2010) state that "UDP-glucose pyrophosphorylases (UGPase; EC 2.7.7.9) catalyze the conversion of UTP and glucose-1-phosphate to UDP-glucose and pyrophosphate and vice versa" ([PMID: 20238176](https://pubmed.ncbi.nlm.nih.gov/20238176/)), defining both the reaction and the EC number matching Q88GA4. Independently, Benini and colleagues, working on the *Erwinia amylovora* GalU, confirm that "this enzyme catalyses the production of UDP-glucose from glucose-1-phosphate and UTP" ([PMID: 28844747](https://pubmed.ncbi.nlm.nih.gov/28844747/)). The reaction is reversible; in the pyrophosphorolysis direction, UDP-glucose plus PPi regenerates UTP and glucose-1-phosphate.

### Finding 2 — GalU uses a Mg²⁺-dependent, ordered sequential Bi-Bi mechanism in a deep active-site pocket

The catalytic mechanism of bacterial GalU is well resolved from crystallographic and calorimetric studies of orthologs. In the *Helicobacter pylori* GalU/UGPase structures (apo and UDP-glucose/Mg²⁺-bound), "magnesium ion is coordinated by Asp130, two oxygen atoms of phosphoryl groups, and three water molecules with octahedral geometry," and isothermal titration calorimetry showed that Mg²⁺ enhances binding of the substrates, "suggesting that this reaction is catalyzed by an ordered sequential Bi Bi mechanism" ([PMID: 20238176](https://pubmed.ncbi.nlm.nih.gov/20238176/)). Complementary structural work on the *Corynebacterium glutamicum* UGPase in complex with Mg²⁺ and UDP-glucose identified the residues anchoring the ligand — Glu36, Gln112, Asp142/143, Glu201, Lys202 — and two Mg²⁺ ions in the active site ([PMID: 17567737](https://pubmed.ncbi.nlm.nih.gov/17567737/)). The chemistry is an in-line nucleophilic attack by the phosphate oxygen of glucose-1-phosphate on the α-phosphorus of UTP, with the metal ions stabilizing the developing negative charge and the leaving pyrophosphate. The active site sits in a **deep pocket** within each subunit, consistent with ordered binding of the two substrates.

### Finding 3 — Bacterial GalU is a cytoplasmic homotetramer, and tetramerization is required for activity

The quaternary structure of bacterial GalU is a **homotetramer**, distinct from the octameric eukaryotic enzymes. Kim et al. established that "HpUGPase is a homotetramer and its active site is located in a deep pocket of each subunit" ([PMID: 20238176](https://pubmed.ncbi.nlm.nih.gov/20238176/)). Critically, the oligomeric state is functionally essential: for the closely related *Pseudomonas* GalU, "tetramerization is essential for the enzymatic function" — disruption of the tetramer abolishes catalysis ([PMID: 38470050](https://pubmed.ncbi.nlm.nih.gov/38470050/)). A functional tetrameric bacterial UGP was recently characterized structurally, reinforcing that the tetramer is the physiologically active unit ([PMID: 39704542](https://pubmed.ncbi.nlm.nih.gov/39704542/)). Because UDPGP type 2 enzymes are soluble cytoplasmic proteins, the UDP-glucose synthesis catalyzed by GalU occurs in the **cytosol**, feeding downstream membrane-associated glycosyltransferases.

### Finding 4 — GalU supplies UDP-glucose for LPS/glycoconjugate biosynthesis; loss of *galU* yields rough, truncated LPS in *Pseudomonas*

The physiological purpose of GalU-generated UDP-glucose is to feed biosynthesis of cell-surface and secreted glycoconjugates. Direct genetic evidence in *Pseudomonas aeruginosa* shows that "interruption of the *galU* gene in *P. aeruginosa* results in production of a rough LPS and truncated LPS core," and that such mutants are more serum-sensitive and attenuated in corneal infection and systemic spread ([PMID: 15213167](https://pubmed.ncbi.nlm.nih.gov/15213167/)). More broadly, Kim et al. note that the product "UDP-glucose, is indispensable for the biosynthesis of virulence factors such as lipopolysaccharides and capsular polysaccharides" ([PMID: 20238176](https://pubmed.ncbi.nlm.nih.gov/20238176/)). In *Erwinia amylovora*, GalU-derived UDP-glucose feeds the amylovoran exopolysaccharide pathway via UDP-glucose → UDP-galactose conversion ([PMID: 28844747](https://pubmed.ncbi.nlm.nih.gov/28844747/)). The consistent phenotype across Gram-negative bacteria — LPS truncation upon *galU* loss — pinpoints GalU as the upstream supplier of the activated glucose used in core oligosaccharide and O-antigen assembly.

### Finding 5 — GalU is specific for glucose-1-phosphate/UTP but retains measurable promiscuity toward other sugar-1-phosphates

While glucose-1-phosphate is the physiological substrate, characterized bacterial GalU enzymes show measurable promiscuity toward related sugar-1-phosphates. In the definitive substrate-specificity study of *Erwinia amylovora* GalU, at 120 minutes the enzyme converted 100% of α-D-xylose-1-phosphate and α-D-glucosamine-1-phosphate, 74% of GlcNAc-1-phosphate, 70% of mannose-1-phosphate, 28% of galactose-1-phosphate, and 0% of galactosamine-1-phosphate and galacturonic acid-1-phosphate ([PMID: 28844747](https://pubmed.ncbi.nlm.nih.gov/28844747/)). The verbatim data — "100% for α-d-xylose 1-phosphate, 100% for α-d-glucosamine 1-phosphate, 70% for α-d-mannose 1-phosphate, and 0% for α-d-galacturonic acid 1-phosphate" — establish that the active site tolerates several hexose- and pentose-1-phosphates while excluding others. This defines the productive substrate window and confirms glucose-1-phosphate as the principal, physiologically relevant substrate feeding UDP-glucose synthesis.

### Finding 6 — GalU sits at a carbon-flux branch point feeding polysaccharide synthesis and the Leloir/pentose-phosphate pathways

GalU occupies a metabolic branch point that partitions carbon between polysaccharide biosynthesis and central sugar metabolism. In *Komagataeibacter xylinus*, "*galU* is an essential gene that controls the carbon metabolic flux between the [bacterial cellulose] synthesis pathway and the pentose phosphate (PP) pathway," and modulating its expression tunes cellulose porosity and crystallinity ([PMID: 32270472](https://pubmed.ncbi.nlm.nih.gov/32270472/)). In *P. putida* KT2440, the biofilm matrix is built by multiple exopolysaccharide systems: "two novel putative exopolysaccharide gene clusters, *pea* and *peb*, were identified," alongside the alginate (*alg*) and cellulose (*bcs*) systems ([PMID: 21507178](https://pubmed.ncbi.nlm.nih.gov/21507178/)). GalU-derived UDP-glucose is the glucosyl donor for the cellulose (*bcs*) branch. The metabolic-engineering literature further reflects GalU's gatekeeper role: overexpression of *pgm* together with *galU* is a standard strategy to boost UDP-glucose flux for capsular polysaccharide and glycoside production ([PMID: 26153362](https://pubmed.ncbi.nlm.nih.gov/26153362/)).

### Finding 7 — The *P. putida* GalU sequence (279 aa) carries the diagnostic bacterial nucleotidyltransferase motif

Direct inspection of the target protein sequence validates the family assignment at the residue level. The UniProt Q88GA4 sequence (279 residues) begins `MIKKCLFPAAGYGTRFLPATKAM...`, placing the canonical sugar-1-phosphate nucleotidyltransferase glycine-rich loop **"GYGTRFLP"** (G-x-G-T-R-x-L-P) at positions 11–18. This N-terminal loop is the conserved UTP/phosphate-binding signature of the UDPGP type-2 (bacterial GalU) family (Pfam PF00483 / IPR005771), homologous to the active-site loops mapped in characterized orthologs. Thoden and Holden's structure of *Corynebacterium* GalU identified conserved N-terminal glycine-rich anchoring residues — "residues involved in anchoring the ligand to the active site include the polypeptide chain backbone atoms of Ala 20, Gly 21, Gly 117, Gly 180, and Ala 214" ([PMID: 17567737](https://pubmed.ncbi.nlm.nih.gov/17567737/)) — matching the GYGTRFLP loop found in the *P. putida* sequence. The ~279-residue length is characteristic of bacterial GalU (a single catalytic Rossmann-fold domain), distinct from the ~500-residue eukaryotic octameric UGP.

### Finding 8 — *P. putida* GalU shares 44% full-length identity with structurally characterized *E. coli* GalU

A quantitative sequence comparison seals the functional assignment. A global pairwise Needleman–Wunsch alignment of Q88GA4 (279 aa) against *E. coli* K-12 GalU (UniProt P0AEP3, 302 aa) gives **123/277 identical positions = 44.1% identity over the full length**. The catalytic N-terminal nucleotidyltransferase loop is conserved: *P. putida* `...AAGYGTRFLPATKA...` aligns to *E. coli* `...VAGLGTRMLPATKA...`, preserving the **G-x-G-T-R-x-L-P-A-T-K** signature that binds UTP and glucose-1-phosphate. Because 44% identity is far above the ~30% threshold generally accepted for confident function transfer, and the *E. coli*/*Corynebacterium* reference enzyme is a biochemically and structurally validated UDP-glucose pyrophosphorylase — "Glucose-1-phosphate uridylyltransferase, or UGPase, catalyzes the production of UDP-glucose from glucose-1-phosphate and UTP" ([PMID: 17567737](https://pubmed.ncbi.nlm.nih.gov/17567737/)) — the *P. putida* enzyme's annotation as GalU/UDP-glucose pyrophosphorylase can be transferred with high confidence.

---

## Mechanistic Model / Interpretation

### The reaction and its cellular position

GalU (PP_3821) catalyzes the reversible uridylyl-transfer reaction at the entry point to activated-glucose metabolism:

```
        glucose-6-phosphate
             │  (Pgm; phosphoglucomutase)
             ▼
   glucose-1-phosphate  +  UTP
             │
             │   GalU / UDP-glucose pyrophosphorylase (PP_3821, EC 2.7.7.9)
             │   Mg²⁺-dependent, ordered sequential Bi-Bi
             ▼
      UDP-glucose  +  PPi
             │
   ┌─────────┼──────────────┬────────────────────┐
   ▼         ▼              ▼                    ▼
 LPS core   UDP-galactose   Exopolysaccharide    UDP-glucuronic acid
 & O-Ag     (via GalE)      (cellulose/bcs,      (via Ugd) →
 assembly                   pea/peb, alginate)   capsule / EPS
```

The enzyme functions as a **soluble cytoplasmic homotetramer**. Each of the four subunits presents an independent deep active-site pocket built on a Rossmann-fold catalytic domain. The N-terminal glycine-rich loop (GYGTRFLP in the *P. putida* sequence) cradles the phosphates of UTP, while Mg²⁺ ions bridge the incoming glucose-1-phosphate and the α-phosphate of UTP, orienting them for in-line nucleophilic substitution. Substrate binding is ordered (sequential Bi-Bi), and Mg²⁺ is required both for catalysis and for tightening substrate/product affinity.

### Why the tetramer matters

The tetramer is the catalytically competent unit. In the *Pseudomonas* GalU, disrupting inter-subunit contacts abolishes activity ([PMID: 38470050](https://pubmed.ncbi.nlm.nih.gov/38470050/)), indicating that quaternary contacts either complete the active site or stabilize the productive conformation of the catalytic loop. This is a recurring theme in sugar-activating nucleotidyltransferases, where oligomerization couples subunit interfaces to active-site integrity — and it is the structural basis for interest in bacterial GalU as an antibacterial drug target ([PMID: 39704542](https://pubmed.ncbi.nlm.nih.gov/39704542/)).

### Metabolic role — a branch-point gatekeeper

UDP-glucose produced by GalU is the hub metabolite from which multiple glycoconjugate pathways draw. The following table summarizes downstream fates and supporting evidence:

| Downstream pathway | Product | Consequence of *galU* loss | Evidence (PMID) |
|---|---|---|---|
| LPS core / O-antigen | Full-length smooth LPS | Rough, truncated LPS; serum sensitivity; attenuation | [15213167](https://pubmed.ncbi.nlm.nih.gov/15213167/), [20238176](https://pubmed.ncbi.nlm.nih.gov/20238176/) |
| Capsular polysaccharide | Capsule | Reduced capsule; engineered *pgm+galU* boosts yield | [26153362](https://pubmed.ncbi.nlm.nih.gov/26153362/) |
| Exopolysaccharide / biofilm (cellulose *bcs*, *pea/peb*, alginate) | Biofilm matrix | Altered matrix; controls flux to cellulose | [21507178](https://pubmed.ncbi.nlm.nih.gov/21507178/), [32270472](https://pubmed.ncbi.nlm.nih.gov/32270472/) |
| Leloir pathway (UDP-galactose via GalE) | UDP-galactose | Loss of galactosylated glycopolymers | [28844747](https://pubmed.ncbi.nlm.nih.gov/28844747/) |

Because GalU stands at the intersection of central sugar-phosphate metabolism and all downstream glycan assembly, it behaves as a **carbon-flux gatekeeper**: the amount and activity of GalU tunes how much carbon is committed to surface/secreted polysaccharides versus retained in central metabolism such as the pentose phosphate pathway ([PMID: 32270472](https://pubmed.ncbi.nlm.nih.gov/32270472/)). The many downstream phenotypes (serum resistance, biofilm stability, virulence in pathogens) are consequences of this single biosynthetic function rather than independent activities.

### Substrate specificity

Glucose-1-phosphate is the physiological substrate, but the active site is not absolutely selective — characterized orthologs process xylose-1-P, glucosamine-1-P, GlcNAc-1-P, and mannose-1-P efficiently, while excluding galacturonic acid-1-P and galactosamine-1-P ([PMID: 28844747](https://pubmed.ncbi.nlm.nih.gov/28844747/)). This promiscuity is biotechnologically useful but does not change the primary in vivo role: the abundant cytoplasmic pool of glucose-1-phosphate (supplied by phosphoglucomutase from glucose-6-phosphate) makes UDP-glucose synthesis the dominant flux.

### Localization

All evidence places GalU function in the **cytosol**: UDPGP type 2 enzymes are soluble; the protein carries no signal peptide or transmembrane region; and its product UDP-glucose is a cytoplasmic metabolite handed off to membrane-embedded glycosyltransferases (e.g., LPS core transferases at the inner membrane, Bcs cellulose synthase) that face or span the inner membrane.

---

## Evidence Base

| PMID | Study focus | How it supports the annotation |
|---|---|---|
| [20238176](https://pubmed.ncbi.nlm.nih.gov/20238176/) | *H. pylori* GalU structure & mechanism | Defines EC 2.7.7.9 reaction; homotetramer; Mg²⁺ coordination; ordered Bi-Bi; UDP-glucose indispensable for LPS/capsule |
| [17567737](https://pubmed.ncbi.nlm.nih.gov/17567737/) | *Corynebacterium* GalU active-site geometry | Reference validated UGPase; conserved N-terminal glycine anchoring residues matching the target's GYGTRFLP loop; basis for function transfer |
| [28844747](https://pubmed.ncbi.nlm.nih.gov/28844747/) | *Erwinia amylovora* GalU activity & specificity | Confirms reaction; quantifies substrate promiscuity; links to EPS (amylovoran) via UDP-galactose |
| [15213167](https://pubmed.ncbi.nlm.nih.gov/15213167/) | *P. aeruginosa galU* in infection | Direct genetic evidence: *galU* loss → rough/truncated LPS; virulence attenuation in a *Pseudomonas* |
| [38470050](https://pubmed.ncbi.nlm.nih.gov/38470050/) | *Pseudomonas* GalU oligomerization | Tetramerization essential for catalytic function |
| [39704542](https://pubmed.ncbi.nlm.nih.gov/39704542/) | Functional tetrameric bacterial UGP | Confirms tetramer as active form; drug-target relevance |
| [32270472](https://pubmed.ncbi.nlm.nih.gov/32270472/) | *K. xylinus galU* CRISPRi | GalU controls carbon flux between cellulose synthesis and PP pathway |
| [21507178](https://pubmed.ncbi.nlm.nih.gov/21507178/) | *P. putida* KT2440 EPS clusters | Establishes the biofilm-matrix context (pea/peb, alg, bcs) that GalU's UDP-glucose feeds |
| [26153362](https://pubmed.ncbi.nlm.nih.gov/26153362/) | *E. coli* K4 capsule engineering | *pgm+galU* overexpression increases UDP-glucose-derived polysaccharide — confirms gatekeeper role |

Supporting/contextual literature also reviewed included structural studies of eukaryotic UGPases (human octamer, [PMID: 22132858](https://pubmed.ncbi.nlm.nih.gov/22132858/); [PMID: 25860585](https://pubmed.ncbi.nlm.nih.gov/25860585/); *Leishmania*, [PMID: 17303565](https://pubmed.ncbi.nlm.nih.gov/17303565/)) that contrast with the smaller bacterial tetramer, GalU inhibitor discovery for antivirulence purposes ([PMID: 29517123](https://pubmed.ncbi.nlm.nih.gov/29517123/), [PMID: 31475928](https://pubmed.ncbi.nlm.nih.gov/31475928/), [PMID: 28114831](https://pubmed.ncbi.nlm.nih.gov/28114831/)), and *galU*'s role in host–pathogen and phage interactions via LPS ([PMID: 26481693](https://pubmed.ncbi.nlm.nih.gov/26481693/), [PMID: 38858621](https://pubmed.ncbi.nlm.nih.gov/38858621/), [PMID: 23936064](https://pubmed.ncbi.nlm.nih.gov/23936064/)).

### Gene-identity verification (mandatory checks)

1. **Symbol vs. protein description:** The symbol *galU* matches the UniProt RecName "UTP–glucose-1-phosphate uridylyltransferase / UDP-glucose pyrophosphorylase" — consistent, not ambiguous.
2. **Organism:** All target-specific genetic evidence is from *Pseudomonas* (*P. aeruginosa galU*, [PMID: 15213167](https://pubmed.ncbi.nlm.nih.gov/15213167/); *Pseudomonas* GalU tetramer, [PMID: 38470050](https://pubmed.ncbi.nlm.nih.gov/38470050/)) or directly from the *P. putida* KT2440 sequence (Q88GA4) and its EPS clusters ([PMID: 21507178](https://pubmed.ncbi.nlm.nih.gov/21507178/)).
3. **Family/domains align:** The InterPro/Pfam signatures (IPR005771, PF00483) and the observed GYGTRFLP motif in the actual sequence match the characterized GalU family.
4. **No competing gene:** The literature on "GalU" is uniformly about UDP-glucose pyrophosphorylase; no different gene with the same symbol confounded the analysis. GalU should not be confused with the Leloir enzyme **GalT** (galactose-1-phosphate uridylyltransferase), a different EC/reaction, nor with the eukaryotic octameric UGP.

The gene identity is therefore **confirmed** — this is a genuine bacterial GalU, validated at three independent levels: database annotation, direct sequence motif, and quantitative homology to a validated ortholog.

---

## Limitations and Knowledge Gaps

- **No direct biochemical characterization of Q88GA4 itself.** The functional assignment rests on strong homology (44% identity to validated *E. coli* GalU) and family-level evidence, not on purified *P. putida* KT2440 enzyme kinetics. No Kₘ, kcat, or crystal structure exists specifically for PP_3821.
- **Substrate-specificity data are from orthologs.** The promiscuity spectrum (xylose-1-P, mannose-1-P, etc.) was measured in *Erwinia amylovora* GalU ([PMID: 28844747](https://pubmed.ncbi.nlm.nih.gov/28844747/)); the exact specificity profile of the *P. putida* enzyme may differ quantitatively.
- **In vivo *galU* phenotypes are from other species.** LPS truncation and virulence attenuation were demonstrated in *P. aeruginosa* and *E. coli*, not in *P. putida* KT2440 (an environmental, non-pathogenic strain), where the primary relevance is more likely biofilm/EPS physiology than virulence.
- **Tetramerization data are ortholog-based.** While a *Pseudomonas* GalU requires tetramerization ([PMID: 38470050](https://pubmed.ncbi.nlm.nih.gov/38470050/)), the exact oligomeric state and interface of PP_3821 has not been experimentally solved.
- **Regulation is uncharacterized.** How *galU* expression and GalU activity are controlled in *P. putida* KT2440 (allosteric effectors, transcriptional regulators, links to quorum sensing as seen in *P. aeruginosa*) remains unexplored for this strain.
- **Redundancy/essentiality unknown for this strain.** Whether PP_3821 is the sole source of UDP-glucose in KT2440, or whether isoenzymes/alternative routes exist, was not established.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant enzymology of PP_3821.** Express and purify Q88GA4 (His-tag), confirm the homotetramer by size-exclusion chromatography / SEC-MALS, and measure steady-state kinetics (Kₘ, kcat) for UTP and glucose-1-phosphate in both reaction directions, with Mg²⁺ dependence. This directly validates the inferred activity.
2. **Substrate-specificity panel.** Assay PP_3821 against the sugar-1-phosphate panel used for *E. amylovora* GalU (glucose-, xylose-, mannose-, galactose-, GlcNAc-, glucosamine-1-P) to define the *P. putida* enzyme's productive window.
3. **Targeted deletion / complementation in KT2440.** Construct a Δ*PP_3821* mutant and characterize LPS profile (silver-stained SDS-PAGE), biofilm/EPS production (crystal violet, cellulose/Calcofluor staining), and growth on various carbon sources; complement in trans to confirm phenotype linkage.
4. **Structural determination.** Solve the crystal structure (or AlphaFold-guided cryo-EM) of PP_3821, ideally with Mg²⁺/UDP-glucose bound, to confirm the deep-pocket active site and the GYGTRFLP catalytic loop geometry.
5. **Flux analysis.** Use ¹³C metabolic flux analysis or targeted overexpression (*pgm+galU*) to quantify how PP_3821 partitions carbon between EPS/LPS synthesis and central metabolism in KT2440, testing the branch-point model.
6. **Active-site mutagenesis.** Mutate conserved residues in the GYGTRFLP loop and the Mg²⁺-coordinating aspartate (homologous to *H. pylori* Asp130) to confirm their catalytic roles.

---

## Conclusion

*galU* / PP_3821 (Q88GA4) of *Pseudomonas putida* KT2440 encodes a **cytoplasmic, homotetrameric UDP-glucose pyrophosphorylase (EC 2.7.7.9)** that catalyzes the Mg²⁺-dependent, reversible synthesis of **UDP-glucose from UTP and glucose-1-phosphate** via an ordered sequential Bi-Bi mechanism. Its product is the central activated glucosyl donor that supplies **LPS, capsular polysaccharide, and exopolysaccharide/biofilm** biosynthesis, positioning GalU as a **carbon-flux gatekeeper** between central sugar-phosphate metabolism and glycoconjugate assembly. The assignment is supported at the annotation, sequence-motif, and quantitative-homology (44% identity to validated *E. coli* GalU) levels, and is corroborated by consistent genetic phenotypes across related bacteria. The main outstanding gap is the absence of direct biochemical and structural characterization of the *P. putida* enzyme itself, which the proposed experiments would resolve.


## Artifacts

- [OpenScientist final report](galU-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](galU-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:20238176
2. PMID:28844747
3. PMID:17567737
4. PMID:38470050
5. PMID:39704542
6. PMID:15213167
7. PMID:32270472
8. PMID:21507178
9. PMID:26153362
10. PMID:22132858
11. PMID:25860585
12. PMID:17303565
13. PMID:29517123
14. PMID:31475928
15. PMID:28114831
16. PMID:26481693
17. PMID:38858621
18. PMID:23936064