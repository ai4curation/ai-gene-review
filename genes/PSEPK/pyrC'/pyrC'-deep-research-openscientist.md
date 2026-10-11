---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T19:58:28.063282'
end_time: '2026-08-31T20:18:47.251427'
duration_seconds: 1219.19
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: Q88D29
  gene_symbol: pyrC'
  uniprot_accession: Q88D29
  protein_description: 'SubName: Full=Dihydroorotase-like protein {ECO:0000313|EMBL:AAN70565.1};
    EC=3.5.2.3 {ECO:0000313|EMBL:AAN70565.1};'
  gene_info: Name=pyrC' {ECO:0000313|EMBL:AAN70565.1}; OrderedLocusNames=PP_4999 {ECO:0000313|EMBL:AAN70565.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: Amidohydro_3. (IPR013108); DHOase. (IPR004722); DHOase/Allantoinase_Hydrolase.
    (IPR050138); DHOase_cat. (IPR024403); Metal-dep_hydrolase_composite. (IPR011059)
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
  path: pyrC'-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: pyrC'-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88D29
- **Protein Description:** SubName: Full=Dihydroorotase-like protein {ECO:0000313|EMBL:AAN70565.1}; EC=3.5.2.3 {ECO:0000313|EMBL:AAN70565.1};
- **Gene Information:** Name=pyrC' {ECO:0000313|EMBL:AAN70565.1}; OrderedLocusNames=PP_4999 {ECO:0000313|EMBL:AAN70565.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** Amidohydro_3. (IPR013108); DHOase. (IPR004722); DHOase/Allantoinase_Hydrolase. (IPR050138); DHOase_cat. (IPR024403); Metal-dep_hydrolase_composite. (IPR011059)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "pyrC'" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'pyrC'' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **pyrC'** (gene ID: Q88D29, UniProt: Q88D29) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: pyrC′ (Q88D29 / PP_4999) in *Pseudomonas putida* KT2440

## Summary

**pyrC′ (UniProt Q88D29; ordered locus PP_4999) in *Pseudomonas putida* KT2440 does NOT encode a functional dihydroorotase (DHOase), despite its database annotation as a "Dihydroorotase-like protein, EC 3.5.2.3." It encodes a catalytically inactive dihydroorotase homolog — a *pseudo-dihydroorotase* (also historically called a "vestigial" DHOase). Its primary function is structural: it is an obligatory subunit of the aspartate transcarbamoylase (ATCase) holoenzyme.** The gene product's real job is not to catalyze a chemical reaction of its own, but to co-assemble with the ATCase catalytic subunit (PyrB, encoded by the adjacent PP_4998) into a large ~480-kDa dodecameric ATCase complex that catalyzes the second committed step of de novo pyrimidine biosynthesis (carbamoyl-phosphate + L-aspartate → N-carbamoyl-L-aspartate).

This conclusion rests on three independent, mutually reinforcing lines of evidence. First, the classic genetic and biochemical work of Schurr and colleagues (1995) on *P. putida* itself established that the pyrC′ product is homologous to dihydroorotase but lacks histidyl residues critical for DHOase catalysis and cannot complement an *E. coli* pyrC (DHOase) auxotroph — so it provides no DHOase activity to the pyrimidine pathway. Second, direct sequence analysis of the KT2440 protein Q88D29 performed in this investigation confirms, at the residue level, that the diagnostic N-terminal His-x-His α-metal-binding motif of active dihydroorotases is entirely absent, abolishing the binuclear metal chemistry required for the reaction. Third, work on the closely related *Pseudomonas aeruginosa* ortholog ("pDHO") shows directly and quantitatively that the pseudo-DHOase chain is inactive yet essential: a stoichiometric mixture of catalytic and pseudo-DHOase subunits assembles into an active dodecamer, and complex formation raises the melting temperature by ~30 °C.

Critically, *P. putida* KT2440 solves the "missing DHOase" problem by gene division of labor. A **separate** gene — the genuine pyrC = PP_1086 (Q88NW7) — encodes a canonical, catalytically competent monofunctional dihydroorotase that performs the actual third step of pyrimidine biosynthesis. Thus KT2440 carries two dihydroorotase-fold paralogs with cleanly divided roles: PP_1086 does the chemistry, while PP_4999/pyrC′ is the catalytically dead structural scaffold that activates ATCase. The gene product functions in the **cytoplasm**, embedded in the soluble de novo pyrimidine biosynthesis machinery.

---

## Gene / Protein Identity Verification

The mandatory identity check was completed and **passed**. The literature and sequence evidence align precisely with the UniProt-provided identity.

| Attribute | UniProt (target) | What the evidence confirms |
|---|---|---|
| Accession | Q88D29 | Sequence directly analyzed (423 aa) |
| Gene symbol | pyrC′ | Named pyrC′ (prime) by Schurr *et al.* 1995 explicitly to distinguish it from true pyrC |
| Locus | PP_4999 | Sits in a pyrB–pyrC′ operon adjacent to PP_4998 (pyrB / ATCase) |
| Organism | *P. putida* KT2440 (PSEPK) | Studied strain; genomic context confirmed for taxid 160488 |
| Annotation | "Dihydroorotase-like protein, EC 3.5.2.3" | Confirmed to be a *misleading* annotation — the protein is a pseudoenzyme |
| Domains | Amidohydro_3 / DHOase-fold (IPR004722, IPR013108, IPR024403, IPR011059) | Consistent with a divergent DHOase-fold paralog that has lost catalysis |
| Size | 423 aa | Matches the ~424 aa / 44.2 kDa pyrC′ product of Schurr *et al.* 1995 |

The gene symbol "pyrC′" is **not** ambiguous here — it was coined specifically for this protein. The essential caveat a reader must carry forward is that the EC number 3.5.2.3 is inherited from the DHOase fold and does **not** reflect a demonstrated enzymatic activity for this particular protein.

---

## Key Findings

### Finding 1 — pyrC′ is a catalytically INACTIVE dihydroorotase homolog (a pseudo-DHOase)

The foundational finding is that the pyrC′ gene product is a **pseudoenzyme**. In the original characterization of the *P. putida* ATCase system, the pyrC-like gene was found to encode a 424-residue, 44.2-kDa polypeptide that is clearly homologous to dihydroorotase yet **lacks specific histidyl residues thought to be critical for DHOase enzymatic function**, and — decisively — **does not complement *Escherichia coli* pyrC auxotrophs** ([PMID: 7896697](https://pubmed.ncbi.nlm.nih.gov/7896697/)). An auxotroph complementation test is a stringent functional assay: if the *P. putida* protein possessed even modest DHOase activity, it would rescue an *E. coli* strain that cannot make dihydroorotate. It does not. Because functional cellular DHOase activity in *P. putida* is physically separate from the ATCase complex, the pyrC′ product is not the source of the pathway's DHOase activity. It was for exactly this reason that the gene was deliberately renamed **pyrC′ (prime)** — to flag that it is *not* a true pyrC.

This is not a peculiarity of one organism. The orthologous protein in *Pseudomonas aeruginosa* — the "pseudo dihydroorotase" or **pDHO** — has been characterized directly, and the conclusion is unambiguous: **"The pDHO chain is inactive but is necessary for ATCase activity"** ([PMID: 32126100](https://pubmed.ncbi.nlm.nih.gov/32126100/)). This "inactive-but-necessary" phrase captures the paradox at the heart of the protein's biology and motivates the structural function described below.

### Finding 2 — The primary function is structural: assembling and activating the dodecameric ATCase holoenzyme

If pyrC′ is not an enzyme, what does it do? It is an **architectural component** of aspartate transcarbamoylase. In *P. putida*, ATCase is a large (~480-kDa) dodecamer composed of two types of chain translated coordinately from overlapping genes: six copies of the pyrB-encoded catalytic chain (334 aa, 36.4 kDa) and six copies of the pyrC′-encoded chain (424 aa, 44.2 kDa). The paper states the model explicitly: **"the P. putida ATCase is a dodecameric protein composed of two types of polypeptide chains translated coordinately from overlapping genes"** and **"The proposed function for the vestigial DHOase is to maintain ATCase activity by conserving the dodecameric assembly of the native enzyme"** ([PMID: 7896697](https://pubmed.ncbi.nlm.nih.gov/7896697/)). In other words, the pseudo-DHOase is the scaffold that holds the catalytic subunits in a productive quaternary arrangement.

The *P. aeruginosa* work turns this proposal into direct, quantitative demonstration. The isolated ATCase catalytic chain is **monomeric and inactive** — on its own it cannot form the composite active site, which spans the interface between adjacent catalytic monomers. Only when the catalytic chain is mixed with the pseudo-DHOase does an active enzyme appear: **"A stoichiometric mixture of the subunits associates into a dodecamer with full ATCase activity"** ([PMID: 32126100](https://pubmed.ncbi.nlm.nih.gov/32126100/)). The magnitude of the stabilization is striking: **"Formation of the complex increases the melting temperature by about 30°C"** ([PMID: 32126100](https://pubmed.ncbi.nlm.nih.gov/32126100/)). A ~30 °C jump in thermal stability upon assembly is compelling physical evidence of a profound, obligate structural partnership — not an incidental association.

This structural logic recurs across the enzyme family. In the multienzymatic animal protein CAD, even a *fungal* DHO-like domain that has lost catalytic activity retains a **conserved structural function** in oligomerization, arranging as a "dimer of trimers" whether or not it is catalytically active ([PMID: 28552578](https://pubmed.ncbi.nlm.nih.gov/28552578/)). The recurring theme — that DHOase-fold modules serve as quaternary-structure organizers regardless of catalysis — provides strong evolutionary context for why *Pseudomonas* would retain a catalytically dead DHOase paralog next to its ATCase gene.

### Finding 3 — Localization and pathway context: a cytoplasmic subunit whose DHO-like loops mediate intersubunit communication

ATCase and (pseudo-)DHOase subunits are **soluble cytoplasmic** enzymes of de novo pyrimidine biosynthesis; there is no evidence of membrane association, secretion, or compartmentalization beyond the cytosol. The homologous CAD complex localizes exclusively in the cytoplasm, consistent with the cytoplasmic placement of the entire pathway.

The structural biology of the closely related *Aquifex aeolicus* DHO–ATC dodecamer illuminates how pyrC′-type subunits engage their catalytic partners. In that system, **"six DHO and six ATC chains form a hollow dodecamer, in which the 12 active sites face an internal reaction chamber that is approximately 60 A in diameter and connected to the cytosol by narrow tunnels"** ([PMID: 19128030](https://pubmed.ncbi.nlm.nih.gov/19128030/)) — a substrate-channeling "one-pot reactor." Three active-site loops that are disordered in the free, inactive DHO become ordered upon complex formation. One loop in particular, loop A, interdigitates between the ATC domains and mediates reciprocal communication: **"Structural studies identified a DHO loop, loop A, interdigitating between the ATC domains that would be expected to interfere with domain closure essential for ATC catalysis"** ([PMID: 24353170](https://pubmed.ncbi.nlm.nih.gov/24353170/)). Binding of the ATC bisubstrate analog PALA inhibits the distal DHO, and a peptide mimic of loop A inhibits ATC with a Ki of 22 µM — showing precisely how the DHO(-like) subunit is physically wired into the ATCase catalytic domains.

For *Pseudomonas* pyrC′, the interpretation is nuanced: because the resident pseudo-DHOase is catalytically dead, the DHO half of the "one-pot reactor" is not operative for dihydroorotase chemistry (that reaction is handled elsewhere; see Finding 5). But the *same* DHO scaffold and its interdigitating loops still perform the assembly and quaternary-structure role — holding the dodecamer together and presenting the ATCase composite active sites in their active configuration.

### Finding 4 — Direct sequence analysis of Q88D29 confirms loss of the conserved α-metal His-x-His motif

Beyond the 1995 literature, this investigation independently verified the pseudoenzyme status at the residue level using the actual KT2440 sequence. Dihydroorotase is a metallo-amidohydrolase; catalysis requires a metal center coordinated by conserved histidines, the most diagnostic being an N-terminal **His-x-His (HxH) α-metal-binding motif**. In the catalytically active *E. coli* dihydroorotase (PyrC, P05020, 348 aa), residues 16–20 are **W-H-L-H-L**, with His17 and His19 serving as α-zinc ligands.

Aligning the KT2440 pyrC′ sequence (Q88D29, 423 aa) against this reference, the structurally corresponding N-terminal position in Q88D29 reads **S-G-L-D-Q** — containing **no histidines at all**. A regex scan for the HxH pattern (`H.H`) in the first 40 residues returns **one** hit in *E. coli* but **zero** in Q88D29. Overall histidine content is also reduced (11 His across the longer 423-residue Q88D29 versus 14 His in the shorter 348-residue *E. coli* enzyme), and global sequence identity to *E. coli* DHOase is only ~26 % — the signature of a divergent DHOase-fold paralog rather than a functional orthologue. Loss of the binuclear metal center is sufficient to abolish the amidohydrolase chemistry needed to cyclize N-carbamoyl-L-aspartate to L-dihydroorotate. This analysis pins down *exactly which* histidyl residues Schurr *et al.* described as "missing" — the N-terminal α-metal ligands — confirming their 1995 claim at the residue level for the specific KT2440 protein: **"the 44.2-kDa polypeptide lacks specific histidyl residues thought to be critical for DHOase enzymatic function"** ([PMID: 7896697](https://pubmed.ncbi.nlm.nih.gov/7896697/)).

| Feature | *E. coli* PyrC (active, P05020) | KT2440 pyrC′ (Q88D29, pseudo) | KT2440 pyrC (PP_1086, Q88NW7, active) |
|---|---|---|---|
| Length | 348 aa | 423 aa | 348 aa |
| N-terminal α-metal motif | W-**H**-L-**H**-L (His17/His19) | S-G-L-D-Q (no His) | DDW-**H**-I-**H**-L (His14/His16) |
| HxH hits in first 40 aa | 1 | 0 | present |
| DHOase activity | Yes | **No** | Yes |
| Role | Catalysis (pyrimidine step 3) | ATCase assembly subunit | Catalysis (pyrimidine step 3) |

### Finding 5 — Genomic context and division of labor: pyrB–pyrC′ operon vs. a separate true pyrC (PP_1086)

The final piece resolves an apparent paradox: if pyrC′ cannot make dihydroorotate, how does KT2440 complete pyrimidine biosynthesis? The genome answers cleanly. The immediate neighbor of pyrC′ is **PP_4998 = pyrB (Q88D30, PYRB_PSEPK)**, the aspartate carbamoyltransferase catalytic subunit (ATCase, EC 2.1.3.2, 334 aa). Its 334-aa length matches exactly the catalytic chain reported by Schurr *et al.* (1995), and its direct adjacency to PP_4999 confirms the **pyrB–pyrC′ operon** in this precise strain — the two "overlapping genes" whose products are translated coordinately into the dodecamer ([PMID: 7896697](https://pubmed.ncbi.nlm.nih.gov/7896697/)). (The next locus over, PP_5000, is the unrelated protease hslV and is not part of this system.)

Meanwhile, a distinct and genomically distant gene, **PP_1086 = pyrC (Q88NW7, PYRC_PSEPK)**, is annotated as the genuine **dihydroorotase (EC 3.5.2.3, 348 aa)** — the canonical monofunctional DHOase size. Sequence inspection provides a clean within-organism control: the true pyrC (PP_1086) retains the diagnostic N-terminal His-x-His α-zinc motif (N-terminus MSDRLTLLRPDDW-**H**-I-**H**-L…, His14/His16, essentially identical to the *E. coli* DDWHLHL), whereas pyrC′ (PP_4999) entirely lacks any N-terminal HxH (MTISILGARVIDPNSGLDQVTDLHL…). KT2440 therefore encodes **two dihydroorotase-fold paralogs with divided labor**: PP_1086 catalyzes step 3 of de novo pyrimidine biosynthesis, while PP_4999/pyrC′ is the catalytically dead assembly subunit of ATCase.

| Gene | Locus | UniProt | Length | EC | Role |
|---|---|---|---|---|---|
| **pyrB** | PP_4998 | Q88D30 (PYRB_PSEPK) | 334 aa | 2.1.3.2 | ATCase catalytic subunit — immediate neighbor of pyrC′ |
| **pyrC′** | PP_4999 | **Q88D29** (target) | 423 aa | 3.5.2.3* | **inactive** pseudo-DHOase / ATCase assembly subunit |
| **pyrC (true)** | PP_1086 | Q88NW7 (PYRC_PSEPK) | 348 aa | 3.5.2.3 | **genuine** dihydroorotase — pathway step 3 |

\*EC on pyrC′ is a family inference, not a demonstrated activity.

---

## Mechanistic Model / Interpretation

The de novo pyrimidine biosynthesis pathway proceeds through a fixed early sequence. In *P. putida* KT2440 the enzymes and genes map as follows:

```
STEP 1  Carbamoyl-phosphate synthetase (CarAB)
            glutamine + HCO3- + 2 ATP  ->  carbamoyl-phosphate
                                   |
                                   v
STEP 2  ASPARTATE TRANSCARBAMOYLASE  <-- the reaction pyrC' serves
            carbamoyl-phosphate + L-aspartate  ->  N-carbamoyl-L-aspartate
            Enzyme: dodecameric ATCase holoenzyme
                    = 6 x PyrB  (PP_4998, catalytic, 334 aa)
                    + 6 x PyrC' (PP_4999 / Q88D29, INACTIVE pseudo-DHOase, 424 aa)
                                   |
                                   v
STEP 3  DIHYDROOROTASE (the actual chemistry)
            N-carbamoyl-L-aspartate  ->  L-dihydroorotate
            Enzyme: TRUE PyrC = PP_1086 (Q88NW7), a SEPARATE, active DHOase
                                   |
                                   v
STEP 4+ Dihydroorotate dehydrogenase -> ... -> UMP
```

The counterintuitive architecture is this: the ATCase enzyme (step 2) is built from a catalytic subunit **plus** a *dihydroorotase-shaped* subunit — but that DHOase-shaped subunit (pyrC′) is a fossil that no longer catalyzes anything. It has been evolutionarily repurposed from an enzyme into a **structural chaperone/scaffold**. Its job is purely quaternary: it is required for the six catalytic PyrB chains to fold into an active dodecamer. Without it, the catalytic chain is a monomer that cannot form its composite active site (built across the interface between two catalytic monomers) and therefore has no ATCase activity.

```
   PyrB alone           PyrB + PyrC' (pyrC')
   (monomer,            (dodecamer,
    INACTIVE)            ACTIVE ATCase)
      O                    O-O-O
                          /  |  \        Tm up ~30 C
                        [ PyrC' x6 stabilizes ]
   No composite         Composite active sites formed
   active site          at PyrB-PyrB interfaces
```

Why keep a broken enzyme? The comparative evidence from the DHO–ATC family gives the answer. From the hyperthermophile *Aquifex aeolicus* to animal CAD, the DHOase domain/subunit is the **oligomerization organizer** of the complex — its interdigitating loops (e.g., "loop A") lock the assembly together and mediate communication between the DHO and ATC halves. In lineages where DHOase activity became redundant (because a separate gene supplies it), the DHOase fold was retained for its *structural* value while its *catalytic* machinery (the metal-binding histidines) was allowed to erode. *Pseudomonas* pyrC′ is a textbook example of this **enzyme-to-scaffold repurposing**: same fold, same partner, same quaternary role — but catalysis discarded and outsourced to a paralog (PP_1086). The result is a robust, thermally hyper-stable ATCase machine and a division of labor that decouples "building the complex" from "doing the DHOase chemistry."

**Localization.** All of this occurs in the **cytoplasm**, within the soluble de novo pyrimidine biosynthetic machinery. There is no evidence for membrane insertion, secretion, or organellar targeting; the protein's functional "site of action" is the protein–protein interface with PyrB, not a small-molecule active site.

---

## Evidence Base

| PMID | Paper (abbrev.) | How it supports the findings |
|---|---|---|
| [7896697](https://pubmed.ncbi.nlm.nih.gov/7896697/) | *ATCase genes of P. putida: requirement for an inactive dihydroorotase for assembly into the dodecameric holoenzyme* (Schurr et al., 1995) | **Primary, organism-specific evidence.** pyrC′ product lacks critical histidyl residues; fails to complement *E. coli* pyrC auxotrophs; ATCase is a two-component dodecamer; proposed function is to conserve the dodecameric assembly. Supports Findings 1, 2, 4, 5. |
| [32126100](https://pubmed.ncbi.nlm.nih.gov/32126100/) | *Characterization and assembly of the P. aeruginosa ATCase–pseudo-dihydroorotase complex* (Patel et al., 2020) | **Direct biochemical proof in a close ortholog.** pDHO is inactive but necessary for ATCase activity; stoichiometric mixture assembles into an active dodecamer; complex formation raises Tm by ~30 °C. Supports Findings 1, 2. |
| [19128030](https://pubmed.ncbi.nlm.nih.gov/19128030/) | *DHO from A. aeolicus activated by association with ATCase; one-pot reactor* (Zhang et al., 2009) | Cytoplasmic dodecameric "nanoreactor" architecture (60 Å chamber, tunnels to cytosol) that the pyrC′/pyrB complex adopts. Supports Finding 3. |
| [24353170](https://pubmed.ncbi.nlm.nih.gov/24353170/) | *Intersubunit communication in the DHO–ATCase complex of A. aeolicus* (Evans et al., 2014) | DHO "loop A" interdigitates between ATC domains and mediates reciprocal linkage; peptide mimic inhibits ATC (Ki = 22 µM). Mechanistic basis of the structural role. Supports Finding 3. |
| [28552578](https://pubmed.ncbi.nlm.nih.gov/28552578/) | *Structural insight into the core of CAD* (Moreno-Morcillo et al., 2017) | Even an **inactive** fungal DHO-like domain retains a conserved structural oligomerization function, reinforcing the enzyme-to-scaffold model. Supports Finding 2. |
| [24314009](https://pubmed.ncbi.nlm.nih.gov/24314009/) | *Mononuclear metal center of type-I DHO from A. aeolicus* (Edwards et al., 2013) | Details the metal-site histidine ligands whose absence in Q88D29 abolishes catalysis. Context for Finding 4. |
| [27746403](https://pubmed.ncbi.nlm.nih.gov/27746403/) | *Activation of latent DHO from A. aeolicus by pressure* | Isolated DHO is latent/occluded and activated by complex formation (loop displacement) — analogous conditional-activation logic for DHO-fold subunits. Context for Findings 2–3. |

**Note on the CAD literature and off-target hits.** Several reviewed papers ([PMID: 39447673](https://pubmed.ncbi.nlm.nih.gov/39447673/), [36677714](https://pubmed.ncbi.nlm.nih.gov/36677714/), [36671534](https://pubmed.ncbi.nlm.nih.gov/36671534/), [32338152](https://pubmed.ncbi.nlm.nih.gov/32338152/), [31939163](https://pubmed.ncbi.nlm.nih.gov/31939163/), [28591622](https://pubmed.ncbi.nlm.nih.gov/28591622/), [31997698](https://pubmed.ncbi.nlm.nih.gov/31997698/), [41101239](https://pubmed.ncbi.nlm.nih.gov/41101239/)) describe the animal multienzyme CAD. They are relevant as family-level context for how DHOase and ATCase domains oligomerize and how DHO-like domains can be structural, but they concern a fused eukaryotic protein and do not directly describe the *Pseudomonas* pyrC′ protein. Two unrelated papers surfaced by symbol/keyword collision ([PMID: 26792711](https://pubmed.ncbi.nlm.nih.gov/26792711/), *Anopheles* population genetics using a "CAD" locus; [PMID: 23028505](https://pubmed.ncbi.nlm.nih.gov/23028505/), herpesvirus centromere/"CAD complex") are **not** relevant to this gene and were correctly excluded.

---

## Supported and Refuted Hypotheses

| Hypothesis | Status | Basis |
|---|---|---|
| H1: pyrC′ is a functional dihydroorotase catalyzing pyrimidine step 3 (as the EC 3.5.2.3 annotation implies) | **Refuted** | Lacks catalytic histidines; no complementation of *E. coli* pyrC; ortholog biochemically inactive (PMID 7896697, 32126100) |
| H2: pyrC′ is a catalytically inactive DHOase paralog (pseudoenzyme) | **Supported** | Direct genetic + biochemical evidence (PMID 7896697, 32126100) |
| H3: pyrC′'s primary role is structural — assembly/activation of the dodecameric ATCase | **Supported** | Dodecamer stoichiometry; reconstitution to full activity; ~30 °C thermal stabilization (PMID 7896697, 32126100) |
| H4: pyrC′ functions in the cytoplasm | **Supported (strong inference)** | Family/complex are soluble cytoplasmic; channeling chamber opens to cytosol (PMID 19128030) |
| H5: The pathway's DHOase (step 3) is supplied by a separate gene, not pyrC′ | **Supported** | KT2440 encodes a distinct true pyrC = PP_1086 (Q88NW7, 348 aa) retaining catalytic His; pyrC′ lacks them |
| H6: Q88D29 itself (not just orthologs) has lost the DHOase catalytic residues | **Supported** | Residue-level sequence analysis: α-site His-x-His absent in Q88D29 |

---

## Limitations and Knowledge Gaps

1. **No experimental structure of the KT2440 protein.** The pseudoenzyme conclusion for Q88D29 rests on (a) 1995 genetic/biochemical data for *P. putida*, (b) direct sequence analysis of the metal-binding motif, and (c) direct biochemical data for the *P. aeruginosa* ortholog. No crystal or cryo-EM structure of the KT2440 PyrB–PyrC′ dodecamer itself has been analyzed here; the quaternary model is inferred by strong homology to *P. aeruginosa* and *A. aeolicus*.

2. **The active-DHOase assignment of PP_1086 is annotation- and sequence-based.** The identification of PP_1086 (Q88NW7) as the genuine catalytic dihydroorotase relies on database annotation plus the presence of the intact His-x-His motif. Direct enzymatic characterization of PP_1086 (kinetics, complementation) was not performed in this investigation, though the retained metal-binding residues strongly support the assignment.

3. **Reaction assignment is inferred, not directly assayed here.** That the ATCase reaction (carbamoyl-phosphate + L-aspartate → N-carbamoyl-L-aspartate) is the step served by pyrC′ follows from the well-established biochemistry of the PyrB catalytic subunit and its dependence on the pseudo-DHOase for activity; no new activity assays were run in this study.

4. **Regulatory and stoichiometric details in KT2440 specifically.** Whether pyrB and pyrC′ are perfectly coordinately expressed in KT2440 under all conditions, and whether pyrC′ has any moonlighting or condition-specific role beyond ATCase assembly, remains uncharacterized. Current evidence indicates no residual catalytic function.

5. **EC-number caveat.** The UniProt annotation "EC 3.5.2.3" is inherited from the DHOase fold and is **misleading** for this protein — it should be read as a family/homology annotation, not a functional assignment.

---

## Proposed Follow-up Experiments / Actions

1. **Structural determination of the KT2440 ATCase.** Solve a cryo-EM or crystal structure of the reconstituted PyrB (PP_4998) + PyrC′ (PP_4999) dodecamer to confirm the six-plus-six architecture and visualize the degraded pyrC′ metal site and interdigitating loops in this exact strain.

2. **Direct activity and complementation assays.**
   - Purify recombinant PyrC′ (Q88D29) and test for any residual DHOase activity in vitro (predicted: none).
   - Confirm PP_1086/PyrC (Q88NW7) as the functional DHOase by (a) in vitro assay of N-carbamoyl-L-aspartate → L-dihydroorotate and (b) complementation of an *E. coli* pyrC auxotroph.

3. **Reconstitution and stability quantification in KT2440.** Reproduce the *P. aeruginosa* experiment for the *P. putida* subunits: show that isolated PyrB is monomeric/inactive, that mixing with PyrC′ yields an active dodecamer, and measure the ΔTm of assembly (predicted ~30 °C).

4. **Genetic dissection in KT2440.** Construct clean deletions of pyrC′ (PP_4999) and pyrC (PP_1086), individually and together. Predictions: ΔpyrC′ abolishes ATCase activity (pyrimidine auxotrophy despite an intact catalytic gene); ΔpyrC (PP_1086) abolishes the DHOase step but leaves ATCase assembly intact.

5. **Mutational rescue/loss test of the scaffold hypothesis.** Engineer point mutations in the pyrC′ "loop A"-equivalent region to test whether disrupting the intersubunit contacts, rather than the (already absent) catalytic site, is what breaks ATCase assembly.

6. **Database annotation correction.** Flag UniProt Q88D29 so that the "EC 3.5.2.3 / Dihydroorotase" annotation is qualified as a *pseudo-dihydroorotase / structural ATCase subunit*, preventing propagation of the misleading functional call to newly sequenced *Pseudomonas* genomes.

---

## Conclusion

pyrC′ (Q88D29, PP_4999) in *P. putida* KT2440 is a **catalytically inactive pseudo-dihydroorotase** whose real, cytoplasmic function is **structural**: six PyrC′ chains co-assemble with six PyrB catalytic chains (PP_4998, from the adjacent pyrB–pyrC′ operon) to build and stabilize a ~480-kDa dodecameric aspartate transcarbamoylase holoenzyme that catalyzes the second step of de novo pyrimidine biosynthesis. The genuine dihydroorotase step is carried out by a separate gene, the true pyrC = PP_1086 (Q88NW7). The protein's "dihydroorotase, EC 3.5.2.3" annotation reflects its fold and evolutionary origin, not a catalytic activity — the diagnostic metal-binding histidines are gone, and the protein has been repurposed from enzyme to scaffold.

---

## References (PMIDs)

- **7896697** — Schurr *et al.* (1995) *J. Bacteriol.* Aspartate transcarbamoylase genes of *Pseudomonas putida*: requirement for an inactive dihydroorotase for assembly into the dodecameric holoenzyme. *(Definitive study of this gene.)*
- **32126100** — Patel *et al.* (2020) Characterization and assembly of the *Pseudomonas aeruginosa* aspartate transcarbamoylase–pseudo-dihydroorotase complex.
- **19128030** — Zhang *et al.* (2009) Dihydroorotase from *Aquifex aeolicus* is activated by association with aspartate transcarbamoylase and forms a one-pot reactor for pyrimidine biosynthesis.
- **24353170** — Evans *et al.* (2014) Intersubunit communication in the dihydroorotase–aspartate transcarbamoylase complex of *A. aeolicus*.
- **24314009** — Edwards *et al.* (2013) The mononuclear metal center of type-I dihydroorotase from *A. aeolicus*.
- **28552578** — Moreno-Morcillo *et al.* (2017) Structural insight into the core of CAD, the multifunctional protein leading de novo pyrimidine biosynthesis.
- **27746403** — Activation of latent dihydroorotase from *Aquifex aeolicus* by pressure.


## Artifacts

- [OpenScientist final report](pyrC'-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](pyrC'-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:7896697
2. PMID:32126100
3. PMID:28552578
4. PMID:19128030
5. PMID:24353170
6. PMID:39447673
7. PMID:26792711
8. PMID:23028505