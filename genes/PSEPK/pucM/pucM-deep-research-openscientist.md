---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-19T07:57:16.385672'
end_time: '2026-08-19T08:39:23.635741'
duration_seconds: 2527.25
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: pucM
  gene_symbol: pucM
  uniprot_accession: Q88F14
  protein_description: 'RecName: Full=5-hydroxyisourate hydrolase {ECO:0000256|ARBA:ARBA00017539,
    ECO:0000256|RuleBase:RU361270}; Short=HIU hydrolase {ECO:0000256|RuleBase:RU361270};
    Short=HIUHase {ECO:0000256|RuleBase:RU361270}; EC=3.5.2.17 {ECO:0000256|ARBA:ARBA00012609,
    ECO:0000256|RuleBase:RU361270};'
  gene_info: Name=pucM {ECO:0000313|EMBL:AAN69865.1}; OrderedLocusNames=PP_4285 {ECO:0000313|EMBL:AAN69865.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the transthyretin family. 5-hydroxyisourate
  protein_domains: Hydroxyisourate_hydrolase. (IPR014306); Thyroxine_BS. (IPR023418);
    Transthyretin/HIU_hydrolase. (IPR000895); Transthyretin/HIU_hydrolase_d. (IPR023416);
    Transthyretin/HIU_hydrolase_sf. (IPR036817)
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
citation_count: 6
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: pucM-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: pucM-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88F14
- **Protein Description:** RecName: Full=5-hydroxyisourate hydrolase {ECO:0000256|ARBA:ARBA00017539, ECO:0000256|RuleBase:RU361270}; Short=HIU hydrolase {ECO:0000256|RuleBase:RU361270}; Short=HIUHase {ECO:0000256|RuleBase:RU361270}; EC=3.5.2.17 {ECO:0000256|ARBA:ARBA00012609, ECO:0000256|RuleBase:RU361270};
- **Gene Information:** Name=pucM {ECO:0000313|EMBL:AAN69865.1}; OrderedLocusNames=PP_4285 {ECO:0000313|EMBL:AAN69865.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the transthyretin family. 5-hydroxyisourate
- **Key Domains:** Hydroxyisourate_hydrolase. (IPR014306); Thyroxine_BS. (IPR023418); Transthyretin/HIU_hydrolase. (IPR000895); Transthyretin/HIU_hydrolase_d. (IPR023416); Transthyretin/HIU_hydrolase_sf. (IPR036817)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "pucM" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'pucM' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **pucM** (gene ID: pucM, UniProt: Q88F14) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *pucM* (Q88F14, PP_4285) — 5-Hydroxyisourate Hydrolase from *Pseudomonas putida* KT2440

**Gene:** *pucM* (OrderedLocusName PP_4285) · **Protein:** 5-hydroxyisourate hydrolase (HIU hydrolase / HIUHase), EC 3.5.2.17 · **Organism:** *Pseudomonas putida* KT2440 (ATCC 47054 / DSM 6125) · **UniProt:** Q88F14 (117 aa)

---

## Summary

The gene **pucM** (UniProt **Q88F14**; ordered locus **PP_4285**) of *Pseudomonas putida* strain KT2440 encodes **5-hydroxyisourate hydrolase (HIU hydrolase; HIUHase; EC 3.5.2.17)**, a soluble cytoplasmic enzyme belonging to the **transthyretin-related protein (TRP) family**. Its primary and defining function is to catalyze the **second step of the aerobic uric-acid (purine) degradation pathway**: the hydrolysis of the unstable intermediate **5-hydroxyisourate (HIU)**, the product of urate oxidase (uricase), to yield **2-oxo-4-hydroxy-4-carboxy-5-ureidoimidazoline (OHCU)**. The reaction consumes one water molecule and releases a proton (Rhea:23736). Every identity check — organism, gene name, EC number, catalyzed reaction, and protein family — aligns consistently, and the investigation found no evidence of gene-symbol ambiguity or misannotation. The *pucM* name is the archetype originally established in *Bacillus subtilis*, where the PucM protein was first characterized experimentally as the HIU hydrolase.

The physiological importance of *pucM* lies in **kinetic and stereochemical channeling** of a reactive intermediate. HIU decays spontaneously, but slowly (over hours) and non-stereospecifically, producing racemic allantoin. The full three-enzyme complement — uricase, HIU hydrolase (PucM), and OHCU decarboxylase — instead converts urate to the biologically relevant enantiomer, **(S)-(+)-allantoin**, within seconds. Thus PucM accelerates the collapse of a short-lived intermediate and, together with OHCU decarboxylase, enforces the correct stereochemistry of the pathway's output. In *P. putida* KT2440, *pucM* (PP_4285) is embedded in a dedicated purine-catabolism/ureide gene cluster together with a purine permease (PP_4284), allantoinase (PP_4286), OHCU decarboxylase (PP_4287), and a GntR-family transcriptional regulator (PP_4283), placing it firmly within the organism's KEGG purine-metabolism pathway (ppu00230).

Structurally, Q88F14 is a 117-residue single-domain polypeptide that assembles into a **homotetramer**, with active sites formed at subunit interfaces. Sequence analysis confirms the enzyme retains the full complement of catalytic residues diagnostic of active HIU hydrolases — His13, Arg45, His99/His101, and the absolutely conserved C-terminal **Tyr-Arg-Gly-Ser (YRGS)** motif — mapping one-to-one onto the experimentally validated catalytic residues of *B. subtilis* PucM. This distinguishes Q88F14 from vertebrate transthyretin, a homolog that arose by gene duplication of an ancestral HIUase-like gene and subsequently lost these catalytic residues, becoming a hormone distributor rather than an enzyme. The bacterial protein lacks any peroxisomal targeting signal or signal peptide and therefore operates in the **cytoplasm**, alongside soluble uricase.

---

## Key Findings

### Finding 1 — Q88F14 is a genuine 5-hydroxyisourate hydrolase catalyzing the second step of uricolysis

The target protein is unambiguously annotated in UniProt (Q88F14) as **5-hydroxyisourate hydrolase, EC 3.5.2.17**, catalyzing:

> 5-hydroxyisourate + H₂O → OHCU (5-hydroxy-2-oxo-4-ureido-2,5-dihydro-1H-imidazole-5-carboxylate) + H⁺ (Rhea:23736)

The gene symbol **pucM** is not a source of ambiguity. It is the archetype name established in *Bacillus subtilis*, where PucM was experimentally characterized and found to catalyze the hydrolysis of HIU, the product of uricase in the first step of the pathway. As stated directly in the primary literature, *"PucM from Bacillus subtilis was recently characterized and found to catalyze the second reaction of the pathway, hydrolyzing 5-hydroxyisourate (HIU), a product of uricase in the first step"* [PMID: 16782815](https://pubmed.ncbi.nlm.nih.gov/16782815/). The reaction context — HIU as substrate, OHCU as product — was independently established through phylogenetic reconstruction of the complete uric-acid degradation pathway, which defined three sequential activities including *"hydrolysis of HIU to give 2-oxo-4-hydroxy-4-carboxy-5-ureidoimidazoline (OHCU) and decarboxylation of OHCU to give S-(+)-allantoin"* [PMID: 16462750](https://pubmed.ncbi.nlm.nih.gov/16462750/).

Every identity check converges: the **organism** (*P. putida* KT2440), the **gene name** (*pucM*), the **EC number** (3.5.2.17), and the **catalyzed reaction** all match the target protein. There is no competing gene with the same symbol producing a conflicting functional literature. This establishes with high confidence that Q88F14 is a bona fide HIU hydrolase, and not a misannotation.

### Finding 2 — Q88F14 retains the intact TRP catalytic active site of HIU hydrolases

Sequence analysis of the 117-amino-acid Q88F14 protein reveals the diagnostic C-terminal TRP motif **Tyr114-Arg115-Gly116-Ser117 (YRGS)** together with the conserved active-site residues **His13, Arg45, and His99/His101**. These map one-to-one onto the residues that were experimentally shown to form the active site of *B. subtilis* PucM. The primary work concluded that *"the absolutely conserved residues across the TRP family, including His-14, Arg-49, His-105, and the C-terminal Tyr-118-Arg-119-Gly-120-Ser-121, indeed form the active site of PucM"* [PMID: 16782815](https://pubmed.ncbi.nlm.nih.gov/16782815/). The presence of this complete catalytic constellation is strong structural evidence that Q88F14 is a catalytically competent enzyme rather than an inactive transthyretin-like binding protein.

Consistent with other characterized bacterial HIU hydrolases, Q88F14 is annotated as a **homotetramer** (UniProt SUBUNIT = Homotetramer). This quaternary organization is shared with the *Klebsiella pneumoniae* HIU hydrolase, of which it was reported that *"KpHIUH is a homotetrameric protein that, based on sequence and structural similarity, belongs to the transthyretin-related protein family"* [PMID: 21795808](https://pubmed.ncbi.nlm.nih.gov/21795808/). In these enzymes, the catalytically productive active sites are assembled at the interfaces between subunits, so the tetrameric assembly is a functional requirement rather than merely a structural detail.

### Finding 3 — Physiological role: accelerating HIU decay and enforcing stereospecific (S)-allantoin production

The biological rationale for a dedicated HIU hydrolase is that its substrate is unstable and its spontaneous breakdown is both slow and stereochemically uncontrolled. Direct kinetic comparison demonstrated that *"urate oxidation produces racemic allantoin on a time scale of hours, whereas the full enzymatic complement produces dextrorotatory allantoin on a time scale of seconds"* [PMID: 16462750](https://pubmed.ncbi.nlm.nih.gov/16462750/). HIU hydrolase (PucM), operating together with OHCU decarboxylase, therefore performs two coupled functions:

1. **Kinetic acceleration** — it channels the reactive HIU intermediate through controlled hydrolysis, preventing its accumulation and non-productive spontaneous decay.
2. **Stereochemical control** — it ensures the pathway output is the single (S)-(+)-allantoin enantiomer rather than a racemate.

This role as an intermediate-channeling, rate- and stereo-controlling enzyme is the precise mechanistic contribution of *pucM* to purine catabolism, and it is what distinguishes enzymatic urate degradation from spontaneous chemical decay.

### Finding 4 — Evolutionary context and cytoplasmic localization

HIU hydrolysis is the **ancestral enzymatic function of the transthyretin family**. As summarized in the evolutionary literature, *"all transthyretin-like proteins studied to date have been demonstrated to function in purine metabolism by hydrolysing the oxidative product of uric acid, 5-hydroxyisourate"* [PMID: 19725880](https://pubmed.ncbi.nlm.nih.gov/19725880/). Vertebrate transthyretin — the well-known thyroxine/retinol distributor — arose later, by gene duplication of a HIUase-like ancestral gene followed by substitutions that abolished catalytic activity and created a thyroxine-binding channel. Ancestral-sequence reconstruction confirmed that the pre-duplication ancestor was unable to bind thyroxine and likely presented the modern HIUase reaction mechanism, while post-duplication substitutions prevented that activity and conferred stable thyroxine binding [PMID: 33956179](https://pubmed.ncbi.nlm.nih.gov/33956179/). Q88F14, retaining all catalytic residues (Finding 2), clearly falls on the **enzyme** side of this evolutionary divide.

With respect to subcellular localization, eukaryotic HIU hydrolase isoforms are distinguished by whether they carry an N-terminal **peroxisomal targeting signal-2 (PTS2)**: the two isoforms comprise *"HIUHase 1 (which has an N-terminal peroxisomal targeting signal-2 [PTS2]) and HIUHase 2 (which does not have an N-terminal PTS2)"* [PMID: 23994290](https://pubmed.ncbi.nlm.nih.gov/23994290/). The bacterial *P. putida* protein possesses no PTS2 and no signal peptide; as a prokaryote lacking peroxisomes, Q88F14 acts in the **cytoplasm**, co-localized with the soluble uricase that generates its substrate. This co-localization is mechanistically important given the instability of HIU: physical proximity to the enzyme producing HIU minimizes spontaneous decay before hydrolysis.

### Finding 5 — PP_4285 (pucM) lies in a dedicated purine-degradation / ureide gene cluster

KEGG genomic-neighborhood analysis of *P. putida* KT2440 places PP_4285 within a coherent, pathway-consistent operonic region encoding consecutive steps of purine/ureide catabolism:

| Locus | Gene / product | KEGG orthology | EC | Pathway role |
|-------|----------------|----------------|-----|--------------|
| PP_4283 | GntR-family transcriptional regulator | — | — | Likely regulator of the cluster |
| PP_4284 | Adenine/guanine/hypoxanthine permease | K06901 | — | Purine base uptake |
| **PP_4285 (*pucM*)** | **5-hydroxyisourate hydrolase** | **K07127** | **3.5.2.17** | **Step 2: HIU → OHCU** |
| PP_4286 | Allantoinase | K16842 | 3.5.2.5 | Later step: (S)-allantoin → allantoate |
| PP_4287 | OHCU decarboxylase | K13485 | 4.1.1.97 | Step 3: OHCU → (S)-allantoin |

PP_4287 (OHCU decarboxylase) is immediately adjacent to / overlapping with PP_4286 (allantoinase). All catalytic genes map to the KEGG **purine metabolism pathway ppu00230**. The clustering of three consecutive ureide-pathway enzymes (PP_4285 → PP_4287 → PP_4286: HIU → OHCU → (S)-allantoin → allantoate) together with a purine permease and a dedicated regulator provides strong organism-specific evidence for a coordinated, physiologically active purine-degradation module in which *pucM* performs the second enzymatic step.

---

## Mechanistic Model / Interpretation

### The uricolytic (ureide) pathway and PucM's place within it

Aerobic degradation of purines converts the purine skeleton into allantoin and ultimately into ammonia/CO₂, liberating nitrogen for assimilation. The three-enzyme core that converts urate to (S)-allantoin is:

```
                 O2, uricase              HIU hydrolase (PucM/PP_4285)
   Uric acid  ───────────────►   HIU   ─────────────────────────────►  OHCU
   (urate)      (EC 1.7.3.3)   (5-hydroxy-    + H2O, - H+ (EC 3.5.2.17)  (2-oxo-4-hydroxy-
                                isourate;      Rhea:23736                 4-carboxy-5-
                                unstable)                                 ureidoimidazoline)
                                                                            │
                                                     OHCU decarboxylase     │  - CO2
                                                     (PP_4287; EC 4.1.1.97) │
                                                                            ▼
                                                                   (S)-(+)-allantoin
                                                                            │
                                                     allantoinase           │  + H2O
                                                     (PP_4286; EC 3.5.2.5)  │
                                                                            ▼
                                                                       allantoate
                                                                (→ further N release)
```

Without PucM (and OHCU decarboxylase), HIU still breaks down, but spontaneously, slowly, and to **racemic** allantoin. With the enzymes present, the pathway runs in **seconds** and produces exclusively **(S)-(+)-allantoin**. PucM's chemistry is a straightforward hydrolysis — hydrating/opening the HIU ring to generate OHCU — but its physiological value is disproportionate to the simplicity of the reaction, because it (a) removes a reactive intermediate before it can decay or react off-pathway, and (b) sets the stereochemical stage for OHCU decarboxylase to deliver the correct allantoin enantiomer.

### Structure–function logic

PucM is a compact (~117 aa) single-domain subunit of the transthyretin / HIU-hydrolase superfamily fold (InterPro IPR000895, IPR014306, IPR036817). Four subunits assemble into a homotetramer, and catalysis occurs at subunit interfaces where the conserved His13, Arg45, His99/His101 and the C-terminal YRGS motif come together to bind and hydrolyze HIU. The absolute conservation of the C-terminal Tyr-Arg-Gly-Ser sequence is the single most diagnostic feature distinguishing an active HIU hydrolase from an inactivated transthyretin, and Q88F14 carries it intact.

### Evolutionary framing

The transthyretin family provides a textbook case of neofunctionalization: an ancestral HIU hydrolase gene duplicated in the chordate lineage, and one copy accumulated substitutions that destroyed catalysis while creating a hydrophobic channel able to bind thyroxine — the modern transthyretin. Q88F14 represents the **retained ancestral enzymatic state**: a bacterial HIU hydrolase that never underwent this transition. This framing matters for annotation confidence, because it explains why a protein assigned to the "transthyretin family" is nonetheless an enzyme, not a hormone carrier — the family label spans both the ancestral enzyme and its derived non-enzymatic offshoot.

### Localization

As a bacterial cytoplasmic protein with no PTS2 and no secretion signal, PucM functions in the cytosol, physically alongside the uricase that generates HIU and the downstream OHCU decarboxylase and allantoinase encoded in the same gene cluster. This spatial co-organization is consistent with efficient handoff of the unstable HIU intermediate.

---

## Evidence Base

| PMID | Title (abbreviated) | How it supports the findings |
|------|---------------------|------------------------------|
| [16782815](https://pubmed.ncbi.nlm.nih.gov/16782815/) | *Structural and functional analysis of PucM, a hydrolase in the ureide pathway and a member of the transthyretin-related protein family* | Defines PucM (the archetype) as the HIU hydrolase catalyzing the step after uricase; identifies the conserved catalytic residues (His-14, Arg-49, His-105, C-terminal YRGS) that map onto Q88F14. Primary support for Findings 1 & 2. |
| [16462750](https://pubmed.ncbi.nlm.nih.gov/16462750/) | *Completing the uric acid degradation pathway through phylogenetic comparison of whole genomes* | Establishes substrate (HIU) → product (OHCU) → (S)-allantoin; demonstrates racemic (hours) vs. stereospecific (seconds) kinetics. Primary support for Findings 1 & 3. |
| [21795808](https://pubmed.ncbi.nlm.nih.gov/21795808/) | *Structural and kinetic insights into the mechanism of 5-hydroxyisourate hydrolase from Klebsiella pneumoniae* | Confirms homotetrameric, TRP-family nature of a bacterial HIU hydrolase homologous to Q88F14. Support for Finding 2. |
| [19725880](https://pubmed.ncbi.nlm.nih.gov/19725880/) | *Evolutionary changes to transthyretin: structure and function of a transthyretin-like ancestral protein* | Establishes HIU hydrolysis as the conserved ancestral function of the transthyretin-like family. Support for Finding 4. |
| [23994290](https://pubmed.ncbi.nlm.nih.gov/23994290/) | *Characterization of Oncorhynchus mykiss 5-hydroxyisourate hydrolase/transthyretin superfamily* | Shows HIUHase subcellular targeting is governed by an N-terminal PTS2; the bacterial enzyme lacks this signal → cytoplasmic. Support for Finding 4. |
| [33956179](https://pubmed.ncbi.nlm.nih.gov/33956179/) | *Reenacting the Birth of a Function: Functional Divergence of HIUases and Transthyretins* | Ancestral-reconstruction evidence that the pre-duplication ancestor used the HIUase mechanism; substitutions later abolished catalysis and enabled thyroxine binding. Support for Finding 4. |
| [20167108](https://pubmed.ncbi.nlm.nih.gov/20167108/) | *Functional characterization of Arabidopsis thaliana transthyretin-like protein* | Independent confirmation that TRP-family proteins form tetramers with 5-HIU hydrolase activity and share the C-terminal Tyr-Arg-Gly-Ser motif; some are bifunctional (HIU hydrolase + OHCU decarboxylase). Contextual support for Findings 2 & 3. |
| [25863347](https://pubmed.ncbi.nlm.nih.gov/25863347/) | *Characterization of little skate recombinant transthyretin* | Illustrates the derived (non-enzymatic) branch — a transthyretin with no HIUHase activity — contrasting with the retained enzymatic function of Q88F14. Contextual support for Finding 4. |
| [25678373](https://pubmed.ncbi.nlm.nih.gov/25678373/) | *Genetic characterization of caffeine degradation by bacteria* | Notes that C-8 oxidation genes in *Pseudomonas* encode enzymes similar to the uric-acid metabolic pathway of *Klebsiella pneumoniae*, contextualizing purine/urate catabolism in *Pseudomonas*. Background support for Finding 5. |

**Note on evidence type:** The most direct experimental evidence (enzymatic assays, crystal structures, mutagenesis) comes from orthologs — *B. subtilis* PucM and *K. pneumoniae* HIUHase — rather than from Q88F14 itself. The assignment for Q88F14 rests on (i) sequence-level conservation of the complete catalytic residue set, (ii) family/domain assignments (InterPro/Pfam transthyretin / HIU-hydrolase), and (iii) genomic context within a purine-degradation cluster. This is a strong inference-by-homology case, but not a direct in vitro characterization of the *P. putida* protein.

---

## Supported and Refuted Hypotheses

**Supported:**
- Q88F14 is a 5-hydroxyisourate hydrolase (EC 3.5.2.17) — supported by ortholog biochemistry, conserved catalytic residues, and coherent database annotation.
- It is a cytoplasmic homotetramer of the TRP family acting as step 2 of urate degradation.
- It provides kinetic and stereochemical control over allantoin formation, directing flux to (S)-(+)-allantoin.

**Refuted / excluded:**
- Q88F14 is **not** a thyroid-hormone-binding transthyretin; that paralogous function evolved later by loss of the very catalytic residues that Q88F14 retains.
- The enzyme is not needed merely because HIU is otherwise inert — HIU does decay spontaneously; the enzyme's role is speed and stereospecificity, not the mere possibility of breakdown.

---

## Limitations and Knowledge Gaps

1. **No direct biochemical characterization of Q88F14.** The functional assignment is inferred from close orthologs (*B. subtilis* PucM, *K. pneumoniae* HIUHase) and from conserved catalytic residues, InterPro domains, and genomic context. No published in vitro kinetic parameters (kcat, Km for HIU), crystal structure, or activity assay specific to the *P. putida* KT2440 protein was identified.
2. **Localization inferred, not measured.** Cytoplasmic localization is inferred from the absence of a signal peptide/PTS2 and the bacterial (peroxisome-free) context, not from experimental fractionation or imaging of KT2440.
3. **Tetramer inferred from family/UniProt annotation.** The homotetrameric assembly is annotated and consistent with characterized homologs, but has not been directly demonstrated for Q88F14.
4. **Regulation and induction conditions unmapped.** The GntR-family regulator (PP_4283) presumably controls the cluster, but the inducing signals (e.g., urate, allantoin, nitrogen limitation) and the operon's precise transcriptional structure in KT2440 were not experimentally verified here.
5. **Upstream urate oxidase locus.** The canonical urate oxidase generating HIU was not co-localized within this cluster in the KEGG analysis, implying the urate → HIU step is encoded elsewhere or is carried out by a non-canonical urate oxidase; this was not resolved.
6. **Residue numbering.** Active-site residues were mapped by alignment to *B. subtilis* PucM; minor offsets in exact numbers (e.g., His99 vs. His101) reflect alignment/annotation uncertainty and would benefit from structure-guided confirmation.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant expression and enzymatic assay.** Express Q88F14 (PP_4285) in *E. coli*, purify, and measure HIU hydrolase activity directly (e.g., a coupled spectrophotometric assay following HIU decay at ~312 nm, with HIU generated in situ by uricase), reporting kcat and Km for HIU. This would convert the current homology-based assignment into direct evidence.
2. **Active-site mutagenesis.** Individually mutate the predicted catalytic residues (His13, Arg45, His99/His101, and the C-terminal Tyr114/Arg115) to Ala and confirm loss of activity, validating the mapped active site.
3. **Structural determination.** Solve the crystal structure (or generate a high-confidence AlphaFold model with PAE analysis) to confirm the transthyretin fold, the homotetramer, and the interfacial active-site geometry.
4. **Localization confirmation.** Perform subcellular fractionation or fluorescent tagging in *P. putida* KT2440 to confirm cytoplasmic localization.
5. **Operon and regulation mapping.** Use RT-PCR/RNA-seq to define the transcriptional structure of the PP_4283–PP_4287 region, test whether the GntR regulator responds to urate/allantoin or nitrogen status, and construct a *pucM* deletion strain to assay growth on uric acid or hypoxanthine as sole nitrogen source.
6. **Stereochemical output assay.** Confirm that the reconstituted KT2440 uricase + PucM + OHCU decarboxylase system produces (S)-(+)-allantoin by chiral analysis, replicating the stereochemical-control phenotype reported for the archetypal system.

---

## Conclusion

All lines of evidence — UniProt/EC annotation, the archetypal *pucM* nomenclature, conserved TRP catalytic residues, homotetrameric family membership, evolutionary reconstruction, and genomic clustering with purine-catabolism genes — converge on a single, confident conclusion: **pucM (Q88F14, PP_4285) encodes a cytoplasmic 5-hydroxyisourate hydrolase (EC 3.5.2.17) that catalyzes the second step of the uricolytic (ureide) purine-degradation pathway in *Pseudomonas putida* KT2440**, hydrolyzing 5-hydroxyisourate to OHCU and thereby driving rapid, stereospecific conversion of uric acid to (S)-(+)-allantoin. The gene symbol is not ambiguous, and no evidence of misidentification was found. The principal caveat is that these conclusions rest on inference from close orthologs and conserved features rather than direct biochemical characterization of the *P. putida* protein itself.


## Artifacts

- [OpenScientist final report](pucM-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](pucM-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:16782815
2. PMID:16462750
3. PMID:21795808
4. PMID:19725880
5. PMID:33956179
6. PMID:23994290