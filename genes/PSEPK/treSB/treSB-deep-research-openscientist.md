---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T16:01:33.190947'
end_time: '2026-09-01T16:18:39.166511'
duration_seconds: 1025.98
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: treSB
  gene_symbol: treSB
  uniprot_accession: Q88FN0
  protein_description: 'RecName: Full=Maltokinase {ECO:0000256|ARBA:ARBA00013882};
    EC=2.7.1.175 {ECO:0000256|ARBA:ARBA00011962}; EC=5.4.99.16 {ECO:0000256|ARBA:ARBA00012619};
    AltName: Full=Maltose alpha-D-glucosyltransferase {ECO:0000256|ARBA:ARBA00031378};
    AltName: Full=Maltose-1-phosphate synthase {ECO:0000256|ARBA:ARBA00031251};'
  gene_info: Name=treSB {ECO:0000313|EMBL:AAN69649.1}; OrderedLocusNames=PP_4059 {ECO:0000313|EMBL:AAN69649.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the glycosyl hydrolase 13 family. TreS
  protein_domains: GH. (IPR017853); GH13_cat_dom. (IPR006047); Glyco_hydro_b. (IPR013780);
    Kinase-like_dom_sf. (IPR011009); Mak_N_cap. (IPR040999)
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
  path: treSB-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: treSB-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88FN0
- **Protein Description:** RecName: Full=Maltokinase {ECO:0000256|ARBA:ARBA00013882}; EC=2.7.1.175 {ECO:0000256|ARBA:ARBA00011962}; EC=5.4.99.16 {ECO:0000256|ARBA:ARBA00012619}; AltName: Full=Maltose alpha-D-glucosyltransferase {ECO:0000256|ARBA:ARBA00031378}; AltName: Full=Maltose-1-phosphate synthase {ECO:0000256|ARBA:ARBA00031251};
- **Gene Information:** Name=treSB {ECO:0000313|EMBL:AAN69649.1}; OrderedLocusNames=PP_4059 {ECO:0000313|EMBL:AAN69649.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the glycosyl hydrolase 13 family. TreS
- **Key Domains:** GH. (IPR017853); GH13_cat_dom. (IPR006047); Glyco_hydro_b. (IPR013780); Kinase-like_dom_sf. (IPR011009); Mak_N_cap. (IPR040999)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "treSB" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'treSB' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **treSB** (gene ID: treSB, UniProt: Q88FN0) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: treSB (PP_4059 / Q88FN0), *Pseudomonas putida* KT2440

## Summary

**treSB** (ordered locus name **PP_4059**; UniProt **Q88FN0**) of *Pseudomonas putida* KT2440 encodes a large (~1,106-residue, ~125.6 kDa), cytoplasmic, **bifunctional "fused trehalose synthase B / maltokinase"** enzyme. It carries two catalytic modules on a single polypeptide chain: an **N-terminal glycoside hydrolase family 13 (GH13) domain** with **trehalose synthase (TreS) activity** (EC 5.4.99.16), and a **C-terminal protein-kinase-like domain** with **maltokinase activity** (EC 2.7.1.175). Acting in sequence, these two activities catalyze the **first two committed steps of the GlgE α-glucan biosynthetic pathway**: the TreS domain reversibly isomerizes **trehalose to maltose**, and the maltokinase domain then uses **ATP to phosphorylate maltose into α-maltose-1-phosphate**.

The product of treSB, **α-maltose-1-phosphate**, is the specific glucosyl donor for the neighboring maltosyltransferase **GlgE** (PP_4060), which extends α-1,4-linked maltooligosaccharide chains; these are then branched with α-1,6 linkages by the branching enzyme **GlgB** (PP_4058) to build intracellular, branched **α-glucan (glycogen)**. treSB sits within a contiguous, syntenic trehalose–glycogen interconversion gene island (PP_4050–PP_4060) that co-encodes both the GlgE route (trehalose → α-glucan) and the TreY/TreZ route (glycogen → trehalose), physically embedding this enzyme in the cell's carbon-storage and stress-response machinery.

Genome-wide ortholog mapping indicates that treSB is the **sole, non-redundant source** of both the trehalose↔maltose isomerase and the maltose kinase activities in *P. putida* KT2440 — there are no standalone TreS or maltokinase genes elsewhere in the genome. Because the downstream GlgE reaction is essentially irreversible and pulls its substrate forward (and because unregulated GlgE activity can otherwise cause toxic maltose-1-phosphate accumulation), the treSB fusion functions as the metabolic **gatekeeper** channeling trehalose into the α-glucan storage polymer. This route has been linked in the genus *Pseudomonas* to desiccation and osmotic stress tolerance. Note that all catalytic and localization assignments for Q88FN0 itself derive from strong sequence/domain homology and pathway synteny; direct biochemical characterization of the *P. putida* enzyme has not been published, and the mechanistic detail is transferred from well-studied orthologs in mycobacteria and actinomycetes.

---

## Gene/Protein Identity Verification

Before presenting findings, the mandatory identity checks are satisfied as follows:

| Verification item | Result |
|---|---|
| Gene symbol matches protein description | **Yes.** "treSB" = trehalose synthase B; UniProt describes a maltokinase / maltose α-D-glucosyltransferase / maltose-1-phosphate synthase — all consistent with a fused TreS–maltokinase. |
| Organism correct | **Yes.** *Pseudomonas putida* KT2440 (ATCC 47054 / DSM 6125 / NCIMB 11950); KEGG locus **ppu:PP_4059**. |
| Protein family / domains align with literature | **Yes.** GH13 catalytic domain (IPR006047), kinase-like domain superfamily (IPR011009), and Mak_N_cap (IPR040999) match the TreS + maltokinase fusion architecture described for orthologs. |
| Risk of confusion with a same-symbol gene | **Low.** The literature basis is the GlgE-pathway TreS/maltokinase enzymology, which is the correct functional context. Mechanistic parameters are transferred from orthologs (mycobacteria, actinomycetes) because no direct *P. putida* treSB study exists. |

The research below is therefore correctly targeted. Where evidence is transferred from orthologs rather than measured on Q88FN0 directly, this is stated explicitly.

---

## Key Findings

### F001 — Q88FN0 is a bifunctional TreS–maltokinase fusion protein

UniProt Q88FN0 is a **1,106-amino-acid, ~125.6 kDa** protein carrying **two EC numbers**: **EC 5.4.99.16** (maltose↔trehalose isomerase, i.e., trehalose synthase / TreS) and **EC 2.7.1.175** (maltokinase). Its domain architecture consists of an **N-terminal GH13 catalytic domain** (approximately residues 24–425; CDD cd11334 "AmyAc_TreS"; InterPro IPR012810 TreS/α-amylase N) **fused to a C-terminal maltokinase module** (Pfam PF18085 "Mak_N_cap"; SUPFAM SSF56112 protein-kinase-like fold; IPR012811 TreS_maltokinase C domain). The two catalytic activities listed by UniProt are precisely:

- `D-maltose = α,α-trehalose` (the TreS isomerase reaction), and
- `D-maltose + ATP = α-maltose 1-phosphate + ADP + H⁺` (the maltokinase reaction).

Annotated keywords include ATP-binding, Calcium, Isomerase, and Transferase, consistent with the dual catalytic nature. This fused architecture combines, in one polypeptide, the two enzymes that in mycobacteria are separate proteins — trehalose synthase **TreS** and maltokinase **Pep2** — which together perform the first two steps of the cytoplasmic GlgE pathway that converts trehalose to α(1→4),α(1→6)-linked glucan [[PMID: 23901909](https://pubmed.ncbi.nlm.nih.gov/23901909/)].

### F002 — The TreS domain is an intramolecular, retaining GH13 isomerase (maltose ↔ trehalose)

The N-terminal GH13 domain catalyzes the **reversible interconversion of maltose and trehalose** [[PMID: 21840994](https://pubmed.ncbi.nlm.nih.gov/21840994/)]. Mechanistic work on the *Mycobacterium smegmatis* TreS ortholog establishes three key mechanistic features that apply to this domain by homology:

1. **Retaining, double-displacement mechanism.** TreS is a member of the retaining GH13 family and follows a **two-step, double-displacement mechanism** with a catalytic nucleophile aspartate (Asp230 in *M. smegmatis*) forming a covalent glycosyl-enzyme intermediate [[PMID: 21840994](https://pubmed.ncbi.nlm.nih.gov/21840994/)].
2. **Strictly intramolecular isomerization.** TreS is unable to incorporate isotope-labeled exogenous glucose into maltose or trehalose, demonstrating that the isomerization occurs **without releasing free glucose** — it is an internal rearrangement of the disaccharide's glycosidic linkage (α,α-1,1 in trehalose ↔ α-1,4 in maltose) [[PMID: 21840994](https://pubmed.ncbi.nlm.nih.gov/21840994/)].
3. **Conformational rate-limiting step.** The rate-limiting step is an active-site opening/closing conformational change rather than the chemical glycosyl transfer.

This defines the substrate specificity of the N-terminal domain of Q88FN0: it acts on the disaccharides trehalose and maltose, interconverting them intramolecularly.

### F003 — The maltokinase domain phosphorylates maltose to α-maltose-1-phosphate using ATP

The C-terminal domain is an **ATP:maltose 1-phosphotransferase (maltokinase)**. Characterization of maltokinase from *Actinoplanes* sp. showed that the reaction product, after purification, is **α-maltose-1-phosphate**, determined by chemical analysis and NMR spectroscopy [[PMID: 8690081](https://pubmed.ncbi.nlm.nih.gov/8690081/)]. Kinetic characterization of the *A. missouriensis* enzyme gave a **Km of 2.6 mM for maltose** and **0.54 mM for ATP**, and demonstrated strict substrate specificity: **only maltose acted effectively as the phosphoryl-group acceptor, and ATP was not replaceable as the phosphoryl-group donor** [[PMID: 12879214](https://pubmed.ncbi.nlm.nih.gov/12879214/)].

Importantly, in mycobacteria the maltokinase (Pep2) forms a **hetero-octameric complex with TreS tetramers**, and complex formation **markedly accelerates the maltokinase activity** [[PMID: 23901909](https://pubmed.ncbi.nlm.nih.gov/23901909/)]. This physical and functional coupling between the two enzymes provides the rationale for their **fusion into a single polypeptide** in *P. putida* treSB: the fusion enforces proximity that in mycobacteria is achieved by complex assembly, channeling the maltose produced by the TreS domain directly to the adjacent kinase domain.

### F004 — The enzyme is cytoplasmic and feeds glycogen/α-glucan synthesis and stress tolerance

The GlgE pathway is explicitly a **cytoplasmic** pathway — described as "the cytoplasmic GlgE-pathway" [[PMID: 23901909](https://pubmed.ncbi.nlm.nih.gov/23901909/)]. Q88FN0 has **no signal peptide or transmembrane features** — it is a single soluble catalytic protein — consistent with a **cytosolic location** where its substrates (trehalose, maltose, ATP) and downstream partners (GlgE, GlgB) reside.

Physiologically, in the closely related *Pseudomonas aeruginosa* PAO1, **trehalose metabolism is integrated with the biosynthesis of branched α-glucan (glycogen)**, and mutants in either biosynthetic pathway are **significantly compromised for survival on abiotic surfaces** [[PMID: 33872310](https://pubmed.ncbi.nlm.nih.gov/33872310/)]. Critically, **desiccation tolerance is mediated directly by GlgE-derived α-glucan**, whereas trehalose supports osmotic stress tolerance [[PMID: 33872310](https://pubmed.ncbi.nlm.nih.gov/33872310/)]. This directly ties the downstream physiological output of the pathway — fed by the α-maltose-1-phosphate product of treSB's maltokinase domain — to concrete stress-survival phenotypes in the genus *Pseudomonas*.

### F005 — PP_4059 lies in a syntenic GlgE-pathway gene cluster (GlgB–treSB–GlgE)

KEGG genomic mapping of *P. putida* KT2440 places **treSB / PP_4059** (complement 4,580,107–4,583,427) immediately between two GlgE-pathway genes on the same strand:

- **PP_4058 = GlgB**, 1,4-α-glucan branching enzyme (K00700, EC 2.4.1.18; complement 4,577,900–4,580,110 — directly abutting PP_4059), and
- **PP_4060 = GlgE**, α-1,4-glucan:maltose-1-phosphate maltosyltransferase (K16147, EC 2.4.99.16; complement 4,583,598–4,585,583).

Nearby also lie PP_4055 (GlgX/isoamylase debranching, K01214) and PP_4050 (glycogen synthase GlgA, K00703). KEGG annotates PP_4059 itself as "fused trehalose synthase B/maltokinase" (ortholog **K05343**). This synteny is functionally meaningful: **GlgE transfers maltose from a maltose-1-phosphate donor to an α-glucan/maltooligosaccharide acceptor**, and blocking GlgE leads to a **toxic accumulation of maltose-1-phosphate that culminates in cellular death** [[PMID: 26616850](https://pubmed.ncbi.nlm.nih.gov/26616850/)]. The maltose-1-phosphate used by PP_4060 (GlgE) is exactly the product of the treSB maltokinase domain — physically tying treSB output to its immediate neighbor.

### F006 — Metabolic directionality: treSB channels trehalose toward glycogen/α-glucan

KEGG (ppu:PP_4059) assigns treSB to **Starch and sucrose metabolism (ppu00500)** and lists the motifs Alpha-amylase, Malt_amylase_C, and Mak_N_cap consistent with the TreS + maltokinase fusion. Although the TreS reaction is thermodynamically reversible, mechanistic work states that TreS **"has been shown recently to function primarily in the mobilization of trehalose as a glycogen precursor"** [[PMID: 21840994](https://pubmed.ncbi.nlm.nih.gov/21840994/)]. The coupling of the reversible isomerase to an essentially **irreversible, ATP-dependent maltokinase step** — and further to the downstream GlgE reaction that consumes maltose-1-phosphate — drives net flux in the direction **trehalose → maltose → α-maltose-1-phosphate → α-glucan**. The ATP investment at the kinase step acts as a thermodynamic ratchet that commits carbon to the storage polymer.

### F007 — Bioinformatic evidence: intact GH13 catalytic triad and kinase motifs

Sequence analysis of Q88FN0 (1,106 aa) locates all the canonical **GH13 conserved sequence regions (CSRs)** in the N-terminal domain, indicating a catalytically competent isomerase:

| CSR | Role | Motif in Q88FN0 | Residue |
|---|---|---|---|
| CSR-I (β3) | His | `VINH` | His114 |
| CSR-II | catalytic nucleophile Asp | `RLDA` | Asp212 |
| CSR-III | general acid/base Glu | `LLAEANQ` | Glu254 |
| CSR-IV | transition-state-stabilizing Asp | `NHDE` | Asp322 |

The CSR-II aspartate (Asp212) corresponds to the experimentally identified TreS nucleophile — **Asp230 in *M. smegmatis* TreS was identified as the catalytic nucleophile** [[PMID: 21840994](https://pubmed.ncbi.nlm.nih.gov/21840994/)]. The C-terminal maltokinase module contains **protein-kinase-like catalytic motifs**: a Brenner/HGD-type catalytic loop `VHGDLHLGQ` (Asp955/His952) and a downstream DFE metal-binding motif `IDFEGE` (Asp973) plus `DYAA` — hallmarks of the aminoglycoside-phosphotransferase / eukaryotic-like protein-kinase (ELK) superfamily to which maltokinases (Mak/Pep2) belong (consistent with the UniProt SUPFAM SSF56112 "Protein kinase-like" assignment). The presence of intact catalytic machinery in both modules argues that Q88FN0 is a genuinely **bifunctional, catalytically active** enzyme, not a fusion in which one domain has degenerated.

### F008 — treSB is embedded in an integrated trehalose–glycogen interconversion gene island (PP_4050–PP_4060)

The contiguous KT2440 locus block around treSB co-encodes both directions of trehalose–glycogen interconversion:

| Locus | Gene | Enzyme | EC |
|---|---|---|---|
| PP_4050 | GlgA | glycogen synthase | 2.4.1.21 |
| PP_4051 | TreZ | maltooligosyltrehalose trehalohydrolase | 3.2.1.141 |
| PP_4052 | MalQ | 4-α-glucanotransferase / amylomaltase | 2.4.1.25 |
| PP_4053 | TreY | maltooligosyltrehalose synthase | 5.4.99.15 |
| PP_4055 | GlgX | glycogen-debranching isoamylase | 3.2.1.68 |
| PP_4058 | GlgB | 1,4-α-glucan branching enzyme | 2.4.1.18 |
| **PP_4059** | **treSB** | **fused TreS / maltokinase** | **5.4.99.16 / 2.7.1.175** |
| PP_4060 | GlgE | maltose-1-phosphate maltosyltransferase | 2.4.99.16 |

Both the **GlgE route** (trehalose → maltose → maltose-1-P → α-glucan) and the **TreY/TreZ route** (glycogen → trehalose) are co-encoded around treSB. Notably, the canonical OtsA/OtsB (trehalose-6-phosphate synthase/phosphatase) KOs did not map to this region. This gene-island organization is the physical manifestation, in *Pseudomonas*, of the finding that **trehalose metabolism is integrated with the biosynthesis of branched α-glucan (glycogen)** [[PMID: 33872310](https://pubmed.ncbi.nlm.nih.gov/33872310/)].

### F009 — treSB catalyzes the first two committed steps of the TreS–Pep2–GlgE pathway

The GlgE pathway sequence is biochemically defined: **"Trehalose is first converted to maltose, which is phosphorylated by maltose kinase Pep2 to give α-maltose 1-phosphate. This is the donor substrate of the maltosyl transferase GlgE that is known to extend α-1,4-linked maltooligosaccharides, which are thought to be branched with α-1,6 linkages"** [[PMID: 27121970](https://pubmed.ncbi.nlm.nih.gov/27121970/)]. In *M. tuberculosis*, **α-glucan is exclusively assembled intracellularly utilizing the building block α-maltose-1-phosphate as the substrate for the maltosyltransferase GlgE, with subsequent branching of the polymer by the branching enzyme GlgB** [[PMID: 27513637](https://pubmed.ncbi.nlm.nih.gov/27513637/)].

Genetic evidence confirms that this pathway is both necessary and sufficient for α-glucan synthesis and identifies maltose-1-phosphate as the key intermediate: a *glgE*-null mutant **accumulated α-maltose 1-phosphate and maltose but no α-glucan** [[PMID: 27121970](https://pubmed.ncbi.nlm.nih.gov/27121970/)]. In *P. putida*, the two enzymatic activities that carry out the first two steps (TreS + maltokinase/Pep2) are **fused into the single treSB polypeptide**, immediately upstream of the adjacent GlgE (PP_4060) and GlgB (PP_4058) — making treSB the entry enzyme of the pathway.

### F010 — treSB is the sole, non-redundant source of TreS and maltokinase activity in KT2440

KEGG KO mapping across the entire *P. putida* KT2440 genome shows:

- Standalone maltokinase (Pep2/Mak, **K16146**): **none**
- Standalone trehalose synthase TreS (**K13057**): **none**
- Fused TreS/maltokinase (**K05343**): maps **uniquely to PP_4059 (treSB)**

Downstream **GlgE (K16147) = PP_4060** and **GlgB (K00700) = PP_4058** are each single-copy. Therefore treSB is the **only** gene encoding either the trehalose→maltose isomerase activity or the maltose→maltose-1-phosphate kinase activity in this organism. Its loss cannot be compensated by any paralog, reinforcing its role as the committed, non-redundant entry point that supplies the α-maltose-1-phosphate donor to the single-copy GlgE [[PMID: 27121970](https://pubmed.ncbi.nlm.nih.gov/27121970/)].

---

## Mechanistic Model and Interpretation

### The reaction carried out by treSB

treSB is a **two-step molecular assembly line on one polypeptide**:

```
                    ┌───────────────── treSB (PP_4059, Q88FN0, ~1106 aa) ─────────────────┐
                    │                                                                       │
   TREHALOSE  ──────►  [ N-terminal GH13 / TreS domain ]  ──────►  MALTOSE                  │
   (α,α-1,1)         Step 1: EC 5.4.99.16                        (α-1,4)                     │
                     reversible, intramolecular                                             │
                     retaining double-displacement                                          │
                     (nucleophile Asp212)                                                   │
                                                                    │                        │
                                                                    ▼                        │
   MALTOSE  + ATP  ──►  [ C-terminal kinase-like / maltokinase ]  ──►  α-MALTOSE-1-PHOSPHATE │
                     Step 2: EC 2.7.1.175                             + ADP + H⁺            │
                     ATP-specific, essentially irreversible                                 │
                     (kinase motifs Asp955/His952, Asp973)                                  │
                    └───────────────────────────────────────────────────────────────────────┘
                                                                    │
                                                                    ▼
                              GlgE (PP_4060, EC 2.4.99.16): transfers maltosyl unit
                              from α-maltose-1-P onto growing α-1,4 glucan chain
                                                                    │
                                                                    ▼
                              GlgB (PP_4058, EC 2.4.1.18): introduces α-1,6 branches
                                                                    │
                                                                    ▼
                              BRANCHED α-GLUCAN / GLYCOGEN  (cytoplasmic carbon store)
                                                                    │
                                                                    ▼
                              Desiccation tolerance (α-glucan); osmotic tolerance (trehalose)
```

### Why the fusion matters

In mycobacteria, TreS and Pep2 are distinct proteins that must **assemble into a hetero-octameric complex** to accelerate maltokinase activity [[PMID: 23901909](https://pubmed.ncbi.nlm.nih.gov/23901909/)]. In *P. putida*, the same functional coupling is hard-wired by **gene fusion**: the intramolecular tether guarantees that maltose produced by the TreS domain is handed directly to the kinase domain, minimizing release of the freely diffusible intermediate and improving pathway throughput. This is a clean example of evolutionary "metabolic channeling by fusion."

### Directionality and regulation logic

The TreS step is reversible, but the pathway operates net **toward α-glucan** because (i) the maltokinase step consumes ATP and is essentially irreversible, and (ii) GlgE continuously consumes α-maltose-1-phosphate. This creates a **thermodynamic pull** that commits trehalose-derived carbon to storage polymer. The finding that a *glgE* block causes **toxic accumulation of maltose-1-phosphate** [[PMID: 26616850](https://pubmed.ncbi.nlm.nih.gov/26616850/); [PMID: 27121970](https://pubmed.ncbi.nlm.nih.gov/27121970/)] highlights that flux through treSB must be balanced with downstream GlgE capacity — treSB is effectively the "faucet," and GlgE the "drain," of a potentially cytotoxic intermediate.

### Localization

All evidence points to a **cytoplasmic** site of action: the GlgE pathway is described as cytoplasmic [[PMID: 23901909](https://pubmed.ncbi.nlm.nih.gov/23901909/)], α-glucan is assembled intracellularly [[PMID: 27513637](https://pubmed.ncbi.nlm.nih.gov/27513637/)], and Q88FN0 lacks any signal peptide or transmembrane segment. Its substrates (trehalose, maltose, ATP) and its immediate downstream partner GlgE are all cytosolic.

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports the findings |
|---|---|---|
| [23901909](https://pubmed.ncbi.nlm.nih.gov/23901909/) | *Synthesis of α-glucan involves a hetero-octameric complex of TreS and maltokinase Pep2* | Defines the cytoplasmic GlgE pathway (TreS→Pep2→GlgE→GlgB); shows TreS–Pep2 complex accelerates maltokinase — rationale for the treSB fusion (F001, F003, F004). |
| [21840994](https://pubmed.ncbi.nlm.nih.gov/21840994/) | *Mechanistic analysis of TreS from M. smegmatis* | Establishes reversible maltose↔trehalose interconversion, retaining GH13 double-displacement mechanism, intramolecular isomerization, catalytic nucleophile Asp230, and TreS as glycogen-precursor mobilizer (F002, F006, F007). |
| [8690081](https://pubmed.ncbi.nlm.nih.gov/8690081/) | *Maltokinase from Actinoplanes sp.* | Identifies the maltokinase product as α-maltose-1-phosphate by NMR/chemical analysis (F003). |
| [12879214](https://pubmed.ncbi.nlm.nih.gov/12879214/) | *Maltokinase from A. missouriensis* | Kinetics (Km maltose 2.6 mM, ATP 0.54 mM) and strict substrate specificity — only maltose/ATP (F003). |
| [26616850](https://pubmed.ncbi.nlm.nih.gov/26616850/) | *Structure of M. thermoresistibile GlgE* | GlgE uses maltose-1-phosphate donor; blocking it causes toxic maltose-1-P accumulation — ties treSB product to adjacent GlgE (F005). |
| [27121970](https://pubmed.ncbi.nlm.nih.gov/27121970/) | *S. venezuelae glgE null developmental delay* | Defines the exact TreS→Pep2→GlgE reaction order; glgE mutant accumulates maltose-1-P and maltose, no α-glucan (F009, F010). |
| [27513637](https://pubmed.ncbi.nlm.nih.gov/27513637/) | *Metabolic network for α-glucan in M. tuberculosis* | α-glucan assembled intracellularly from α-maltose-1-P via GlgE, branched by GlgB (F009). |
| [33872310](https://pubmed.ncbi.nlm.nih.gov/33872310/) | *Trehalose and α-glucan stress responses in P. aeruginosa* | In *Pseudomonas*: trehalose metabolism integrated with α-glucan; GlgE-derived α-glucan mediates desiccation tolerance; trehalose mediates osmotic tolerance (F004, F008). |
| [30877199](https://pubmed.ncbi.nlm.nih.gov/30877199/) | *Crystal structure of the TreS:Pep2 complex* | Structural basis of the α-glucan-initiating TreS:Pep2 assembly in the GlgE pathway (supports F001/F003 architecture). |
| [38485491](https://pubmed.ncbi.nlm.nih.gov/38485491/) | *Targeting (TB)* | Context on the GlgE pathway as an antitubercular target; corroborates pathway importance. |

**Strength of evidence.** The *pathway-level* assignment (TreS + maltokinase → α-maltose-1-phosphate → GlgE → GlgB → α-glucan) is supported by strong primary biochemical, genetic, and structural studies in mycobacteria, streptomycetes, and actinomycetes, plus direct genetic/physiological data in the same genus (*Pseudomonas aeruginosa*). The *organism-specific* assignment to Q88FN0/PP_4059 rests on UniProt/KEGG annotation, domain architecture, conserved catalytic-residue analysis, and gene synteny — robust inference, but not direct enzymology on the *P. putida* protein.

---

## Limitations and Knowledge Gaps

1. **No direct biochemical characterization of Q88FN0.** All kinetic parameters (Km values, substrate specificities) and mechanistic details are transferred from orthologs (*Actinoplanes*, *M. smegmatis*). The *P. putida* enzyme has not been purified or assayed; its actual kinetics, optimal conditions, and any regulatory features are unknown.
2. **No experimental structure of Q88FN0.** The catalytic-residue and motif assignments (Asp212, Glu254, Asp322; kinase Asp955/His952/Asp973) are from sequence alignment. An experimental or AlphaFold-validated structure would confirm active-site geometry and the inter-domain arrangement of the fusion.
3. **Calcium role unverified.** UniProt lists a Calcium keyword; whether Ca²⁺ (or another metal) is required for the *P. putida* enzyme's activity is not experimentally established.
4. **Physiological phenotype in *P. putida* not directly tested.** The stress-tolerance link (desiccation, osmotic) is demonstrated in *P. aeruginosa* PAO1, not KT2440. A *treSB* knockout phenotype in *P. putida* has not been reported.
5. **Directionality in vivo not measured.** Net flux direction (trehalose → glycogen) is inferred from thermodynamic coupling and ortholog data, not from flux measurements in *P. putida*.
6. **Interaction with the parallel TreY/TreZ and OtsAB routes.** How treSB flux is balanced against the co-encoded TreY/TreZ (glycogen→trehalose) route and any OtsAB trehalose synthesis is not characterized in this organism.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant expression and dual-activity assay.** Express Q88FN0 in *E. coli*; assay (a) TreS activity (trehalose↔maltose interconversion by HPLC/TLC) and (b) maltokinase activity (ATP-dependent maltose phosphorylation, ADP or α-maltose-1-P detection). Determine Km/kcat for both domains and compare to ortholog values (maltose Km ~2.6 mM, ATP Km ~0.54 mM).
2. **Product confirmation by NMR/MS.** Verify that the kinase product is specifically **α-maltose-1-phosphate** (as opposed to a 6-phosphate), mirroring the *Actinoplanes* determination.
3. **Domain-dissection and mutagenesis.** Express N- and C-terminal domains separately to test whether the fusion is required for maltokinase acceleration. Mutate predicted catalytic residues (Asp212, Glu254 in GH13; Asp955/Asp973 in kinase) to confirm their roles.
4. **Structure determination.** Solve the crystal or cryo-EM structure of Q88FN0, or validate an AlphaFold model, to define the inter-domain arrangement and test for a channeling conduit between the two active sites.
5. **Metal-dependence assay.** Test Ca²⁺/Mg²⁺/Mn²⁺ requirements for each activity to resolve the annotated Calcium keyword.
6. **Genetics in *P. putida* KT2440.** Construct a clean *treSB* (PP_4059) deletion; measure α-glucan/glycogen content, intracellular maltose-1-phosphate and maltose (watch for toxic accumulation), and desiccation/osmotic stress survival. Complement to confirm specificity.
7. **Flux analysis.** Use ¹³C-labeled trehalose to trace carbon flow through treSB into α-glucan in vivo and quantify net directionality, including cross-talk with the co-encoded TreY/TreZ route.

---

## Conclusion

**treSB (PP_4059 / Q88FN0)** is a cytoplasmic, bifunctional **fused trehalose synthase B / maltokinase** that catalyzes the first two committed steps of the GlgE α-glucan biosynthetic pathway in *Pseudomonas putida* KT2440. Its N-terminal GH13 domain isomerizes **trehalose to maltose** (EC 5.4.99.16), and its C-terminal kinase-like domain phosphorylates maltose with ATP to **α-maltose-1-phosphate** (EC 2.7.1.175). This product is the specific donor for the adjacent maltosyltransferase GlgE (PP_4060), which — with the branching enzyme GlgB (PP_4058) — builds intracellular branched α-glucan/glycogen, a carbon store linked in *Pseudomonas* to desiccation and osmotic stress tolerance. treSB is the sole, non-redundant entry enzyme of this route, embedded in a syntenic trehalose–glycogen interconversion gene island (PP_4050–PP_4060). All catalytic assignments are strongly supported by ortholog biochemistry, conserved catalytic-residue analysis, and gene synteny, though direct biochemical characterization of the *P. putida* enzyme remains to be performed.


## Artifacts

- [OpenScientist final report](treSB-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](treSB-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:23901909
2. PMID:21840994
3. PMID:8690081
4. PMID:12879214
5. PMID:33872310
6. PMID:26616850
7. PMID:27121970
8. PMID:27513637