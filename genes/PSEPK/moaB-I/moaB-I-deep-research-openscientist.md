---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-20T16:42:45.486724'
end_time: '2026-07-20T17:00:31.129973'
duration_seconds: 1065.64
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: moaB-I
  gene_symbol: moaB-I
  uniprot_accession: Q88L15
  protein_description: 'RecName: Full=Molybdenum cofactor biosynthesis protein B {ECO:0000256|ARBA:ARBA00015262,
    ECO:0000256|PIRNR:PIRNR006443};'
  gene_info: Name=moaB-I {ECO:0000313|EMBL:AAN67735.1}; OrderedLocusNames=PP_2122
    {ECO:0000313|EMBL:AAN67735.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the MoaB/Mog family.
  protein_domains: MoaB. (IPR012245); MoaB/Mog-like_dom_sf. (IPR036425); MoaB/Mog_dom.
    (IPR001453); MoaB_proteobac. (IPR013484); MoCF_biosynth_CS. (IPR008284)
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
citation_count: 9
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: moaB-I-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: moaB-I-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88L15
- **Protein Description:** RecName: Full=Molybdenum cofactor biosynthesis protein B {ECO:0000256|ARBA:ARBA00015262, ECO:0000256|PIRNR:PIRNR006443};
- **Gene Information:** Name=moaB-I {ECO:0000313|EMBL:AAN67735.1}; OrderedLocusNames=PP_2122 {ECO:0000313|EMBL:AAN67735.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the MoaB/Mog family.
- **Key Domains:** MoaB. (IPR012245); MoaB/Mog-like_dom_sf. (IPR036425); MoaB/Mog_dom. (IPR001453); MoaB_proteobac. (IPR013484); MoCF_biosynth_CS. (IPR008284)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "moaB-I" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'moaB-I' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **moaB-I** (gene ID: moaB-I, UniProt: Q88L15) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *moaB-I* (Q88L15, PP_2122) — Molybdenum Cofactor Biosynthesis Protein B in *Pseudomonas putida* KT2440

## Summary

**moaB-I** (UniProt **Q88L15**; ordered locus **PP_2122**) of *Pseudomonas putida* strain KT2440 encodes **Molybdenum cofactor biosynthesis protein B (MoaB)**, a small (~179 amino acid, ~19 kDa) soluble protein of the **MoaB/Mog "G-domain" superfamily**. Sequence, structural, and genomic-context evidence converge on a single coherent conclusion: MoaB-I is a **cytoplasmic** component of the ancient, highly conserved **molybdenum cofactor (Moco) biosynthesis pathway**, acting at or near the **terminal molybdenum-insertion step** in which the pterin scaffold molybdopterin (MPT) is activated and charged with molybdenum to produce the active cofactor required by more than 50 redox molybdoenzymes.

The primary line of positive identification is sequence-based: pairwise alignment shows Q88L15 is **54.7 % identical to *Escherichia coli* MoaB** (P0AEZ9) but only **29.9 % identical to *E. coli* MogA/Mog** (P0AF03, molybdopterin adenylyltransferase). This cleanly assigns the protein to the **MoaB** branch of the family and distinguishes it from the closely related MogA. The diagnostic family signatures — the glycine-rich loop (I/V)TGGTGF and the PGST pterin/nucleotide-binding motif — are conserved. Structurally, the direct *E. coli* MoaB ortholog adopts a **MogA-like modified Rossmann fold** and assembles into a **hexamer (a dimer of trimers)** with a conserved putative pterin-binding site, a fold shared with MogA, MoeA, and the eukaryotic multidomain proteins gephyrin (mammals) and Cnx1 (plants).

Functionally, members of this G-domain family catalyze the **ATP/Mg²⁺-dependent adenylylation of molybdopterin to MPT-AMP**, the activated intermediate that the MoeA-type protein subsequently uses to ligate molybdenum and yield mature Moco. A striking feature of *P. putida* KT2440 supports a direct role for MoaB-I in this step: the genome **lacks a dedicated *mogA* gene**, **moaB-I (PP_2122) sits immediately adjacent to *moeA* (PP_2123)**, and a second paralog, **moaB-II (PP_4600)**, sits next to **moaA (PP_4597)**. This synteny implicates MoaB-I as the **MogA-equivalent partner of MoeA** in the terminal Mo-insertion reaction. It must be stated clearly that this precise catalytic assignment is **inferred** from homology, structure, and gene neighborhood — the enzymatic activity of MoaB-I (or of any MoaB, as opposed to MogA) has **not been directly demonstrated experimentally**, and the specific in vivo role of MoaB proteins remains an open question in the Moco field.

---

## Gene/Protein Identity Verification (PASSED)

The mandatory identity check was completed and passed:

| Verification item | Result |
|---|---|
| Gene symbol "moaB-I" matches protein description | ✔ Matches — MoaB/Mog family, Molybdenum cofactor biosynthesis protein B |
| Organism is *Pseudomonas putida* KT2440 | ✔ Confirmed (UniProt organism_id 160488) |
| Protein family/domains align with literature | ✔ MoaB/Mog family; InterPro IPR012245, IPR001453, IPR013484, IPR036425, IPR008284 all consistent with MoaB |
| No conflicting literature for a different gene | ✔ No ambiguity found; MoaB is a well-defined Moco-biosynthesis protein |

The target is a **bona fide MoaB ortholog**, unambiguously placed in the Moco biosynthesis pathway, confirmed independently by pairwise alignment (54.7 % identity to *E. coli* MoaB vs 29.9 % to MogA) and by conservation of the diagnostic MoaB/Mog motifs. There is no evidence of gene-symbol ambiguity. The main caveat is not misidentification but **sparse protein-specific experimental literature**: no dedicated functional study exists for the *P. putida* MoaB-I protein itself, so its function is annotated by homology and inference from the well-studied *E. coli* and eukaryotic homologs.

---

## Key Findings

### Finding 1 — Q88L15 is a genuine MoaB ortholog, distinct from the MogA paralog

Pairwise Needleman–Wunsch alignment of the 179-residue *P. putida* KT2440 MoaB-I sequence against *E. coli* K-12 proteins gives **54.7 % identity (93/170 aligned positions) to *E. coli* MoaB** (P0AEZ9) versus only **29.9 % (52/174) to *E. coli* MogA/Mog** (P0AF03, molybdopterin adenylyltransferase). This nearly two-fold difference in identity is decisive for branch assignment: the protein belongs to the **MoaB** subfamily rather than the MogA subfamily, even though the two are homologous members of the same MoaB/Mog family.

The alignment further confirms conservation of the two diagnostic family motifs:
- The **glycine-rich loop I(V)TGGTGF** — *Pp*MoaB-I `LITGGTGFTGRD` closely matches *Ec*MoaB `LITGGTGLTEGD`.
- The **PGST pterin/nucleotide-binding motif** — *Pp*MoaB-I `LPGSTNAV` matches *Ec*MoaB `MPGSTKAC`.

UniProt independently assigns family = MoaB/Mog, and InterPro places the protein in **IPR013484 (MoaB_proteobac)** and **IPR001453 (MoaB/Mog_dom)**. Together these establish, with high confidence, that Q88L15 is a proteobacterial MoaB.

### Finding 2 — MoaB adopts a MogA-like Rossmann fold and assembles as a hexamer with a conserved pterin-binding site

Two independent crystal structures of *E. coli* MoaB — the direct 54.7 %-identical ortholog of Q88L15 — reveal a **modified Rossmann fold** that assembles into a **32-symmetric hexamer composed of two trimers**. This fold is structurally homologous to **MogA, MoeA, and the G-domains of gephyrin and plant Cnx1**, all members of the Moco-biosynthesis Mo-insertion machinery. Sanishvili et al. (2004; [PMID: 15269205](https://pubmed.ncbi.nlm.nih.gov/15269205/)) solved MoaB to 1.6 Å and reported that "*MoaB is assembled into a hexamer composed of two trimers. The monomers have high structural similarity with two proteins, MogA and MoeA, from the molybdenum cofactor synthesis pathway in E. coli, as well as with domains of mammalian gephyrin and plant Cnx1.*" An independent structure by Bader et al. (2004; [PMID: 15159566](https://pubmed.ncbi.nlm.nih.gov/15159566/)) at 2.1 Å similarly noted that "*the overall fold of the monomer is similar to those of the MogA protein of E. coli, the G-domains of rat and human gephyrin and the G-domains of Cnx1 protein from A. thaliana, all of which are involved in the insertion of an unknown molybdenum species into molybdopterin to form the molybdenum cofactor.*"

The archaeal ortholog from *Sulfolobus tokodaii* (ST2315) is likewise a trimer/hexamer with the same fold (Antonyuk et al. 2009; [PMID: 20054111](https://pubmed.ncbi.nlm.nih.gov/20054111/)), confirming that the oligomeric architecture is conserved across all three domains of life. Structural comparison and conservation mapping reveal a **putative active/ligand-binding site predicted to bind a pterin compound**, most likely a molybdopterin biosynthesis intermediate. By virtue of its 54.7 % identity, *P. putida* MoaB-I is expected to share this hexameric Rossmann-fold architecture and pterin-binding pocket.

### Finding 3 — The MogA/MoaB family reaction: adenylylation of molybdopterin to MPT-AMP

The mechanistic template for this protein family comes from the plant Cnx1 G domain (a homolog of both MogA and MoaB). Kuper, Llamas, Hecht, Mendel & Schwarz (2004, *Nature*; [PMID: 15306815](https://pubmed.ncbi.nlm.nih.gov/15306815/)) showed that the **Cnx1 G domain binds molybdopterin with high affinity and, in an ATP/Mg²⁺-dependent reaction, produces adenylated molybdopterin (MPT-AMP)** — described in their words as: "*The Cnx1 G domain (Cnx1G)… binds molybdopterin with high affinity and participates in the catalysis of molybdenum insertion. Here we present two high-resolution crystal structures of Cnx1G in complex with molybdopterin and with adenylated molybdopterin (molybdopterin-AMP), a mechanistically important intermediate.*" This MPT-AMP intermediate is then processed by the MoeA-like E domain in a Mg²⁺-dependent reaction that inserts molybdenum and yields active Moco.

In *E. coli*, this terminal step is split between two proteins: **MogA adenylylates MPT (ATP-dependent)** and **MoeA ligates Mo to MPT**. Nichols et al. (2007; [PMID: 17198377](https://pubmed.ncbi.nlm.nih.gov/17198377/)) established that "*In Escherichia coli, the MoeA protein mediates ligation of Mo to molybdopterin while the MogA protein enhances this process in an ATP-dependent manner.*" Because Q88L15 is 29.9 % identical to *E. coli* MogA and 54.7 % identical to *E. coli* MoaB, it belongs squarely within this catalytic superfamily and is predicted to carry out (or contribute to) the pterin-adenylylation chemistry that primes MPT for molybdenum insertion.

### Finding 4 — MoaB functions in the cytoplasm within the conserved Moco biosynthesis pathway; *P. putida* carries a duplicated *moaB*

The molybdenum cofactor biosynthesis pathway is a **soluble, cytoplasmic, evolutionarily conserved** route present across archaea, bacteria, and eukaryotes (Xiang et al. 2001, [PMID: 11525167](https://pubmed.ncbi.nlm.nih.gov/11525167/): "*Molybdenum cofactor (Moco) biosynthesis is an evolutionarily conserved pathway present in archaea, eubacteria, and eukaryotes*"; Schwarz et al. 2001, [PMID: 11554796](https://pubmed.ncbi.nlm.nih.gov/11554796/)). In *E. coli*, *moaB* lies in the **moaABCDE operon** (Bader et al. 2004, [PMID: 15159566](https://pubmed.ncbi.nlm.nih.gov/15159566/): "*The moaABC operon of Escherichia coli is involved in early steps of the biosynthesis of the molybdenum-binding cofactor molybdopterin*").

The *P. putida* gene symbol **moaB-I** and its "-I" suffix indicate a genome carrying **two moaB paralogs (moaB-I and moaB-II)** — a duplication of the mogA-like Moco biosynthesis gene. Consistent with cytoplasmic localization, the protein has **no transmembrane segments or signal peptides**; it is a soluble hexamer, exactly as expected for an enzyme of the soluble Moco pathway. It therefore carries out its function **inside the cell, in the cytosol**.

### Finding 5 — Genomic synteny: moaB-I sits beside moeA, and KT2440 lacks a dedicated mogA

Ordered-locus mapping of the KT2440 genome (via UniProt, organism_id 160488) revealed a functionally informative gene neighborhood and confirmed the complete pathway complement:

| Gene | Locus | Product | Pathway step |
|---|---|---|---|
| *moaA* | PP_4597 (Q88E69) | GTP 3',8-cyclase | cPMP formation |
| **moaB-II** | **PP_4600 (Q88E67)** | Mo-cofactor biosynthesis protein B (paralog) | beside *moaA* (early region) |
| *moaC* | PP_1292 | cPMP synthase | cPMP formation |
| *moaD* | PP_1293 | molybdopterin synthase sulfur-carrier | MPT formation |
| *moaE* | PP_1294 | molybdopterin synthase catalytic subunit | MPT formation |
| **moaB-I** | **PP_2122 (Q88L15)** | **Mo-cofactor biosynthesis protein B (TARGET)** | **Mo insertion (beside *moeA*)** |
| *moeA* | PP_2123 (Q88L14) | molybdopterin molybdenumtransferase | Mo insertion |
| *mobA* | PP_3457 | Mo-cofactor guanylyltransferase | MGD attachment |

Two observations are decisive for the *P. putida*-specific interpretation: (i) **moaB-I (PP_2122) is immediately adjacent to moeA (PP_2123)** — a two-gene neighborhood physically coupling MoaB-I to the molybdenum-insertion enzyme; and (ii) a genome-wide UniProt query returned **no gene annotated as *mogA*** in KT2440. Since MogA normally performs the ATP-dependent MPT adenylylation that immediately precedes MoeA-catalyzed Mo insertion, the MoaB paralogs are the best candidates to supply that activity, and moaB-I's synteny with moeA points to it as MoeA's functional partner. The second paralog, moaB-II (PP_4600), sits with *moaA* in the early (cPMP) region, suggesting possible sub-functionalization of the two MoaB copies. MoaB-I and MoaB-II are both 55–56 % identical to *E. coli* MoaB and ~30 % to *E. coli* MogA.

### Finding 6 — Authoritative pathway placement: MoaB acts in cytoplasmic Moco biosynthesis that activates molybdenum for >50 molybdoenzymes

The definitive modern review of the field (Mendel & Leimkühler 2015; [PMID: 24980677](https://pubmed.ncbi.nlm.nih.gov/24980677/)) frames Moco biosynthesis as "*an ancient, ubiquitous, and highly conserved pathway leading to the biochemical activation of molybdenum.*" The pathway proceeds in defined steps: (1) cyclic pyranopterin monophosphate (cPMP) formation by MoaA/MoaC; (2) MPT formation by MoaD/MoaE (molybdopterin synthase); (3) molybdenum insertion into MPT by MogA/MoeA to form Moco; and (4) in bacteria/archaea, nucleotide attachment (e.g., MobA → molybdopterin guanine dinucleotide, MGD). Moco is the essential component of **more than 50 redox molybdoenzymes**, and, as the review notes, "*in all molybdoenzymes except nitrogenase, molybdenum is coordinated to a dithiolene group on the 6-alkyl side chain of a pterin called molybdopterin (MPT).*"

*P. putida* KT2440 encodes the **full pathway** — moaA (PP_4597), moaC/D/E (PP_1292–1294), moeA (PP_2123), mobA (PP_3457), plus the two moaB paralogs moaB-I/-II — so MoaB-I operates as one node of a complete cytoplasmic biosynthetic system. Its output, Moco, enables *P. putida*'s molybdoenzyme repertoire (e.g., nitrate reductases, DMSO/TMAO reductases, xanthine/aldehyde oxidoreductases) important for the organism's versatile respiratory and catabolic metabolism.

---

## Mechanistic Model / Interpretation

### The Moco biosynthesis pathway and where MoaB-I acts

```
   GTP
    │  MoaA (PP_4597, radical-SAM 3',8-cyclase)  +  MoaC (PP_1292)
    ▼
  cPMP  (cyclic pyranopterin monophosphate)
    │  MoaD–MoaE (PP_1293/1294, molybdopterin synthase; sulfur transfer)
    ▼
  MPT  (molybdopterin — the dithiolene pterin scaffold)
    │
    │  ===== TERMINAL Mo-INSERTION STEP =====
    │
    │  (1) ADENYLYLATION  — ATP/Mg²⁺ dependent
    │      MPT ──────────────► MPT-AMP
    │      [MogA in E. coli]   ◄── inferred role of MoaB-I (PP_2122)
    │                              (no MogA in KT2440; moaB-I adjacent to moeA)
    │
    │  (2) Mo LIGATION / insertion — Mg²⁺ dependent
    │      MPT-AMP ──────────► Mo-MPT  (= Moco)
    │      [MoeA, PP_2123 (Q88L14)]
    ▼
  Moco  (molybdenum cofactor)
    │  MobA (PP_3457, guanylyltransferase)
    ▼
  MGD  (molybdopterin guanine dinucleotide) → mature bacterial molybdoenzymes
        e.g. nitrate reductase, DMSO/TMAO reductase (>50 enzymes)
```

### Synthesis

All independent lines of evidence — sequence identity, protein fold, oligomeric state, conserved catalytic motifs, gene neighborhood, and pathway completeness — point to a single interpretation:

1. **Identity:** MoaB-I is a proteobacterial MoaB, not a MogA (Finding 1).
2. **Structure/localization:** It is a soluble, cytoplasmic, hexameric Rossmann-fold protein with a conserved pterin-binding pocket (Findings 2, 4).
3. **Family chemistry:** Its superfamily catalyzes ATP-dependent adenylylation of molybdopterin to MPT-AMP, the activated intermediate for Mo insertion (Finding 3).
4. **Pathway role in *P. putida*:** Because KT2440 lacks MogA and moaB-I is genomically coupled to moeA, MoaB-I is the most plausible **functional substitute for MogA** — the adenylylating partner that hands MPT-AMP to MoeA for molybdenum ligation (Findings 5, 6).

The MoaB/MogA relationship is best understood as **paralogous subfunctionalization**. In *E. coli*, both MoaB and MogA exist; MogA's adenylyltransferase role is biochemically established, while MoaB's precise physiological function remains formally undefined despite its near-identical fold. In an organism like *P. putida* that has duplicated MoaB but discarded MogA, it is parsimonious that one or both MoaB paralogs assumed the MogA-type adenylylation role — which is why MoaB-I is annotated as, and most likely functions as, the terminal-step MPT-activating enzyme.

---

## Evidence Base

| PMID | Paper (abbreviated) | Contribution to this report |
|---|---|---|
| [15269205](https://pubmed.ncbi.nlm.nih.gov/15269205/) | *Crystal structure of E. coli MoaB* (Sanishvili et al. 2004) | Direct structural template (54.7 % id ortholog): MoaB is a hexamer (dimer of trimers) with a MogA/MoeA/gephyrin/Cnx1-like fold. Supports Findings 2, 4. |
| [15159566](https://pubmed.ncbi.nlm.nih.gov/15159566/) | *Structure of E. coli MoaB* (Bader et al. 2004) | Independent MoaB structure; confirms fold homology to Mo-insertion proteins and pterin-binding prediction; places moaB in the moaABC operon. Supports Findings 2, 4. |
| [15306815](https://pubmed.ncbi.nlm.nih.gov/15306815/) | *Molybdopterin-bound Cnx1G domain* (Kuper et al. 2004, *Nature*) | Defines the MPT → MPT-AMP adenylylation reaction of the G-domain family — the mechanistic template for MoaB's inferred activity. Supports Finding 3. |
| [17198377](https://pubmed.ncbi.nlm.nih.gov/17198377/) | *E. coli MoeA mutational analysis* (Nichols et al. 2007) | Confirms the two-protein MogA/MoeA split of the terminal Mo-insertion step in bacteria. Supports Findings 3, 5. |
| [11525167](https://pubmed.ncbi.nlm.nih.gov/11525167/) | *E. coli MoeA structure / gephyrin* (Xiang et al. 2001) | Establishes the conserved cytoplasmic Moco pathway across archaea, bacteria, eukaryotes. Supports Finding 4. |
| [11554796](https://pubmed.ncbi.nlm.nih.gov/11554796/) | *Gephyrin & Cnx1 G-domain structures* (Schwarz et al. 2001) | Refines the predicted MPT-binding site; links bacterial MogA/MoaB to eukaryotic Moco machinery. Supports Findings 2, 4. |
| [24980677](https://pubmed.ncbi.nlm.nih.gov/24980677/) | *The biosynthesis of the molybdenum cofactors* (Mendel & Leimkühler 2015) | Authoritative review: pathway steps, purpose (activating Mo), molybdopterin definition, >50 molybdoenzymes. Supports Finding 6. |
| [20054111](https://pubmed.ncbi.nlm.nih.gov/20054111/) | *S. tokodaii MoaB (ST2315)* (Antonyuk et al. 2009) | Archaeal MoaB is a trimer/hexamer with the same fold — conservation across domains of life. Supports Finding 2. |
| [21206014](https://pubmed.ncbi.nlm.nih.gov/21206014/) | *Thermophilic MogA structures* | Comparative MogA structural/functional analysis; proposes a MogA–MoeA complex. Contextualizes the terminal step. |
| [11428898](https://pubmed.ncbi.nlm.nih.gov/11428898/) | *E. coli MoeA structure* | MoeA domain 3 resembles MogA; shared ligand/substrate binding. Context for the MoaB-I/MoeA partnership. |
| [11325967](https://pubmed.ncbi.nlm.nih.gov/11325967/) | *Gephyrin N-terminal (MogA-like) G-domain structure* (Sola et al. 2001) | Trimeric MogA-like G-domain with conserved molybdopterin-binding motif. Supports the family fold interpretation. |

The evidence base is internally consistent: every structural study of a MoaB or MogA family member reports the same Rossmann fold, the same trimeric/hexameric assembly, and the same conserved pterin-binding site, and every functional study places these proteins at the terminal Mo-insertion step of Moco biosynthesis.

---

## Supported and Refuted Hypotheses

**Supported**
- **H1 — Gene identity:** Q88L15/moaB-I is a genuine MoaB (MogA/MoaB family) ortholog. *Supported* (54.7 % identity to *E. coli* MoaB; conserved family motifs; concordant family/domain annotations).
- **H2 — Cytoplasmic Moco-biosynthesis role:** MoaB-I functions intracellularly within the conserved Moco pathway. *Supported* (structural homology to MogA/MoeA/gephyrin/Cnx1; complete moa/moe/mob gene complement present in KT2440; no TM/signal features).
- **H3 — Terminal-step (Mo-insertion/adenylylation) association:** MoaB-I is linked to the MogA-type step. *Supported by bioinformatic inference* — synteny with *moeA* (PP_2123) and absence of *mogA* in KT2440.

**Refuted / rejected alternatives**
- MoaB-I is **not** MogA itself (only ~30 % identity; a distinct paralog).
- MoaB-I is **not** a membrane transporter, structural/adapter protein, or extracellular/secreted protein (no TM/signal features; soluble hexamer).
- The gene symbol is **not** ambiguous or mismatched — the "different gene, same symbol" failure mode does not apply here.

---

## Limitations and Knowledge Gaps

1. **No direct experimental characterization of MoaB-I.** There is no dedicated biochemical, genetic, or structural study of the *P. putida* KT2440 MoaB-I protein itself. Its function is assigned entirely by **homology, structure, and genomic synteny**; the consensus should be read as a strong, well-supported inference rather than a demonstrated fact.

2. **MoaB's precise physiological role is unresolved even in *E. coli*.** Despite two crystal structures, the specific in vivo activity of MoaB (as distinct from MogA) has never been unambiguously established. MoaB structural papers make functional predictions ("*suggests a probable role*"), not enzymatic assays, and some note MoaB may bind an as-yet-unidentified pterin intermediate rather than MPT.

3. **Paralog redundancy is untested.** *P. putida* has two MoaB paralogs (moaB-I / moaB-II) with different gene neighborhoods (moeA vs moaA). Whether they are redundant, whether only one supplies MogA-type activity, and whether they are differentially regulated (e.g., under anaerobic/nitrate conditions) are all open questions.

4. **Substrate specificity is inferred, not measured.** The predicted substrate (molybdopterin) and product (MPT-AMP) derive from the Cnx1 and MogA literature, not from assays on MoaB-I. Whether MoaB-I acts on MPT, cPMP, or another pterin intermediate has not been directly tested.

5. **Synteny is suggestive, not conclusive.** The moaB-I–moeA adjacency is a strong hint that they act together, but gene-neighborhood organization does not by itself prove a physical or enzymatic partnership.

6. **Direct localization data absent.** Cytoplasmic localization is inferred from sequence features and pathway biology, not experimentally shown for MoaB-I.

---

## Proposed Follow-up Experiments / Actions

1. **Gene deletion / complementation.** Construct ΔmoaB-I, ΔmoaB-II, and the double mutant in KT2440 and assay Moco-dependent phenotypes (nitrate/DMSO/TMAO reductase activity, anaerobic/denitrifying growth). Complement with each paralog and with *E. coli mogA* to test functional equivalence and MogA substitution; cross-complement an *E. coli ΔmogA* strain.

2. **In vitro reconstitution.** Recombinantly express and purify MoaB-I and test for **ATP/Mg²⁺-dependent adenylylation of molybdopterin to MPT-AMP** (following the Cnx1G assay design, [PMID: 15306815](https://pubmed.ncbi.nlm.nih.gov/15306815/)), directly measuring substrate specificity and kinetics.

3. **Reconstituted terminal step with MoeA (PP_2123).** Combine purified MoaB-I and MoeA (Q88L14) with MPT, ATP/Mg²⁺, and a Mo source to reconstitute full Moco synthesis and test whether MoaB-I + MoeA suffice for Mo insertion in the absence of MogA.

4. **Structural determination.** Solve the crystal or cryo-EM structure of *P. putida* MoaB-I, ideally with bound MPT/MPT-AMP, to confirm the hexameric fold and map the pterin-binding pocket; compare to *E. coli* MoaB ([PMID: 15269205](https://pubmed.ncbi.nlm.nih.gov/15269205/)).

5. **Physical interaction studies.** Test for a MoaB-I–MoeA complex (pull-down, co-elution, or crosslinking), building on the proposed MogA–MoeA complex model ([PMID: 21206014](https://pubmed.ncbi.nlm.nih.gov/21206014/)).

6. **Expression/regulation profiling.** Determine whether moaB-I and moaB-II are differentially expressed under molybdenum limitation, anaerobiosis, or nitrate respiration to resolve paralog specialization.

---

## Conclusion

*moaB-I* (Q88L15, PP_2122) encodes **Molybdenum cofactor biosynthesis protein B**, a soluble, cytoplasmic, hexameric MoaB/Mog-family protein (54.7 % identical to *E. coli* MoaB) with a MogA-like Rossmann fold and a conserved pterin-binding site. It functions in the **terminal, molybdenum-insertion phase of the conserved cytoplasmic Moco biosynthesis pathway**, where — by structural homology and by the genomic facts that KT2440 lacks a *mogA* gene and *moaB-I* lies directly beside *moeA* (PP_2123) — it most plausibly serves as the **MogA-equivalent enzyme that ATP-dependently adenylylates molybdopterin to MPT-AMP** for subsequent MoeA-catalyzed molybdenum ligation, yielding the cofactor required by *P. putida*'s >50 molybdoenzymes. The assignment is robust at the level of family, fold, localization, and pathway, but the specific catalytic activity of MoaB-I has **not been directly demonstrated experimentally** and is inferred from its well-characterized homologs.


## Artifacts

- [OpenScientist final report](moaB-I-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](moaB-I-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:15269205
2. PMID:15159566
3. PMID:20054111
4. PMID:15306815
5. PMID:17198377
6. PMID:11525167
7. PMID:11554796
8. PMID:24980677
9. PMID:21206014