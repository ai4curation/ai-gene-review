---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T21:02:35.292537'
end_time: '2026-08-31T21:56:30.943404'
duration_seconds: 3235.65
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_3195
  gene_symbol: PP_3195
  uniprot_accession: Q88I07
  protein_description: 'RecName: Full=Peptidase S9 prolyl oligopeptidase catalytic
    domain-containing protein {ECO:0000259|Pfam:PF00326};'
  gene_info: OrderedLocusNames=PP_3195 {ECO:0000313|EMBL:AAN68803.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: AB_hydrolase_fold. (IPR029058); FrsA_esterase. (IPR050261); Peptidase_S9_cat.
    (IPR001375); Peptidase_S9 (PF00326)
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
citation_count: 4
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PP_3195-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PP_3195-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88I07
- **Protein Description:** RecName: Full=Peptidase S9 prolyl oligopeptidase catalytic domain-containing protein {ECO:0000259|Pfam:PF00326};
- **Gene Information:** OrderedLocusNames=PP_3195 {ECO:0000313|EMBL:AAN68803.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** AB_hydrolase_fold. (IPR029058); FrsA_esterase. (IPR050261); Peptidase_S9_cat. (IPR001375); Peptidase_S9 (PF00326)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_3195" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_3195' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_3195** (gene ID: PP_3195, UniProt: Q88I07) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of PP_3195 (Q88I07): FdeB, a Serine δ-Lactone Hydrolase of the Naringenin Degradation Pathway in *Pseudomonas putida* KT2440

## Summary

**PP_3195 (UniProt Q88I07) is FdeB, a cytoplasmic α/β-hydrolase-fold serine hydrolase that catalyzes a δ-lactone-hydrolysis (lactonase) step in the lower naringenin meta-cleavage pathway of *Pseudomonas putida* KT2440.** Its primary function is to hydrolyze the ring-opened flavonoid intermediate 5-(4-hydroxyphenyl)-3-oxovalero-δ-lactone into 5-hydroxy-5-(4-hydroxyphenyl)-3-oxopentanoate (KEGG reaction R13077), thereby channeling carbon from the plant flavonoid naringenin toward central metabolism. Although the UniProt record labels the protein a "Peptidase S9 prolyl oligopeptidase catalytic domain-containing protein," this name is a fold-based electronic inference — the protein is an ester/lactone hydrolase, not a true peptidase.

The identification rests on convergent lines of evidence. Genomically, PP_3195 sits within a co-localized flavonoid-catabolic (*fde*) gene cluster alongside a dioxygenase, monooxygenase, and cyclase; KEGG assigns it to ortholog K26184 (symbol *fdeB*) in pathway ppu00946 ("Degradation of flavonoids"). Structurally, an AlphaFold model of Q88I07 (mean pLDDT 91.6) reveals a fully assembled, canonical serine-hydrolase catalytic triad — Ser268–Asp359–His394 — with hydrogen-bond distances of ~2.7 Å, and Ser268 lying in a GxSxG nucleophile-elbow motif ("GVSLG"). Evolutionarily, PP_3195 shares only ~28% identity with the enteric fermentation/respiration-switch protein FrsA and, unlike FrsA, retains the nucleophilic serine, marking it as a bona fide serine hydrolase rather than a cofactor-independent decarboxylase.

**Important caveat:** No direct biochemical or genetic characterization of PP_3195/FdeB itself has been published. The functional assignment is an inference-based conclusion — strongly supported by orthology, genomic context, KEGG pathway reconstruction, and a structurally validated catalytic triad, but not yet confirmed by enzyme assays, knockout phenotypes, or crystallography on the *P. putida* protein. This report presents the assignment as a well-supported hypothesis and flags where experimental confirmation is still needed.

---

## Gene/Protein Identity Verification

Before presenting the functional analysis, the mandatory identity checks were completed:

| Attribute | Value |
|-----------|-------|
| UniProt | Q88I07 (unreviewed / TrEMBL) |
| Locus | PP_3195; EMBL AAN68803.1 |
| Organism | *Pseudomonas putida* KT2440 (PSEPK), a **strict aerobe**, γ-proteobacterium |
| Length | 420 aa (~46 kDa); genome position complement(3,624,225–3,625,487) |
| UniProt name | "Peptidase S9 prolyl oligopeptidase catalytic domain-containing protein" (from Pfam PF00326, ECO:0000259) |
| KEGG ortholog | **K26184 — *fdeB*, naringenin degradation protein FdeB** |
| COG | COG1506 |
| Pathway | ppu00946 — Degradation of flavonoids |
| InterPro | IPR050261 (FrsA/Cutinase/Hydrolase-like family), IPR001375 (Peptidase S9 catalytic domain, MEROPS clan SC), IPR029058 (α/β-hydrolase fold superfamily) |

| Check | Result |
|-------|--------|
| Gene symbol match | UniProt uses OrderedLocusName **PP_3195**; KEGG independently assigns the symbol **fdeB** to this locus (K26184). Consistent. |
| Organism | *Pseudomonas putida* strain KT2440. Confirmed. |
| Domains/family align | All UniProt/InterPro signatures are α/β-hydrolase-superfamily signatures consistent with a serine hydrolase. |
| Literature ambiguity | No literature exists for the *P. putida* PP_3195 protein directly. The *fde* nomenclature and pathway derive from a homologous system in *Herbaspirillum seropedicae* (PMID 27059806). This is a genuine ortholog, not a same-symbol collision, so research proceeds — but the conclusion is inference-based. |

The gene symbol is **not** ambiguous in the problematic sense (no competing gene with the same symbol in a different organism was found). Rather, PP_3195 is simply an **uncharacterized** protein whose function must be inferred from orthology, domain architecture, structure, and pathway context. The "peptidase S9 / prolyl oligopeptidase" wording is a **fold/clan-based** annotation (MEROPS clan SC groups many esterases and lipases, not only peptidases) and is refined and superseded by the more specific KEGG *fdeB* assignment.

---

## Key Findings

### Finding 1 — PP_3195 is *fdeB*, an α/β-hydrolase-fold enzyme in the naringenin/flavonoid degradation (*fde*) gene cluster

PP_3195 is not an isolated hydrolase; it is embedded in a dedicated flavonoid-catabolic operon. KEGG assigns PP_3195 to ortholog **K26184** (SYMBOL *fdeB*, "naringenin degradation protein FdeB"), places it in pathway **ppu00946 "Degradation of flavonoids,"** and classifies it in **COG1506**. The locus lies within a co-localized cluster of *fde* genes, each mapped to a distinct catabolic ortholog:

| Locus | *fde* gene | KEGG KO | Predicted role |
|-------|-----------|---------|----------------|
| PP_3195 | *fdeB* | K26184 | α/β-hydrolase (lactonase) — **this protein** |
| PP_3197 | *fdeC* | K26181 | Ring-cleaving dioxygenase |
| PP_3198 | *fdeD* | K26179 | Accessory / oxygenase component |
| PP_3204 | *fdeH* | K26182 | Dioxygenase-associated |
| PP_3205 | *fdeI* | K26185 | Downstream converting enzyme |
| PP_3206 | *fdeJ* | K26183 | Cyclase |

InterPro classifies Q88I07 into IPR050261 (FrsA/Cutinase/Hydrolase-like family), IPR001375 (Peptidase S9 prolyl oligopeptidase catalytic domain, MEROPS clan SC), and IPR029058 (the α/β-hydrolase-fold superfamily). All three signatures converge on a serine-hydrolase fold.

The *fde* nomenclature and pathway logic come from *Herbaspirillum seropedicae* SmR1, where the naringenin meta-cleavage pathway was genetically dissected. As reported in [PMID: 27059806](https://pubmed.ncbi.nlm.nih.gov/27059806/): *"The Tn5 transposon was found to be inserted in the fdeE gene (Hsero_1007), which encodes a monooxygenase,"* establishing the *fde* gene names, and *"naringenin is first mono-oxygenated by the FdeE protein, to produce 5,7,8-trihydroxy-2-(4-hydroxyphenyl)-2,3-dihydro-4H-chromen-4-one, that is subsequently dioxygenated and cleaved at the A-ring by the FdeC dioxygenase."* These describe the upstream steps that generate the intermediates on which downstream hydrolases such as FdeB act.

**Interpretation:** Genomic clustering with a monooxygenase, dioxygenase, and cyclase is powerful contextual evidence that PP_3195/FdeB is a catabolic enzyme processing a flavonoid-derived intermediate — not a housekeeping peptidase.

### Finding 2 — FdeB is a serine hydrolase predicted to open a δ-lactone intermediate (KEGG reaction R13077)

KEGG links FdeB (K26184) to **reaction R13077**, classified as a **hydrolase**:

> 5-(4-hydroxyphenyl)-3-oxovalero-δ-lactone (C22570) + H₂O ⇌ 5-hydroxy-5-(4-hydroxyphenyl)-3-oxopentanoate (C22571)

This is a **lactone hydrolysis (lactonase/esterase) step** in the lower meta-cleavage branch, converting a cyclic ester into a linear 3-oxo-acid that is degraded onward toward TCA intermediates. KEGG flags R13077 as an "unclear reaction," reflecting that the pathway was reconstructed rather than experimentally validated at each step; the exact substrate/product should therefore be treated as a well-reasoned prediction.

Sequence analysis of Q88I07 (420 aa) locates the canonical α/β-hydrolase **GxSxG nucleophile-elbow motif "GVSLG"** with catalytic **Ser268**, together with the acidic and histidine residues that complete the Ser-Asp-His triad characteristic of clan SC / α/β-hydrolase serine hydrolases.

Supporting the hydrolase assignment for the broader family, [PMID: 30951551](https://pubmed.ncbi.nlm.nih.gov/30951551/) reports that a FrsA/esterase-family protein *"was able to catalyze the hydrolysis of esters, especially p-nitrophenyl acetate,"* confirming these proteins act as ester-hydrolyzing serine hydrolases and reinforcing an ester/lactone-hydrolase assignment for FdeB.

**Interpretation:** A lactone is simply a cyclic ester; a serine hydrolase with an intact catalytic triad is exactly the enzyme class expected to hydrolyze (open) such a ring. The predicted substrate is a flavonoid-derived δ-lactone, and the reaction is ring-opening hydrolysis to the corresponding hydroxy-keto-acid.

### Finding 3 — PP_3195 acts intracellularly (cytoplasm); its "peptidase S9" label is fold-based, not evidence of true peptidase activity

Q88I07 has **no recognizable N-terminal Sec signal peptide and no lipoprotein lipobox** (N-terminus: `MAPPCPACVPCLQTAPCLPV…`), consistent with a cytoplasmic localization. Bacterial flavonoid-catabolic enzymes and FrsA-family α/β-hydrolases are characteristically cytoplasmic.

The UniProt name "Peptidase S9 prolyl oligopeptidase catalytic domain-containing protein," together with GO terms GO:0008236 (serine-type peptidase activity) and GO:0006508 (proteolysis), are all **electronic (IEA) inferences** derived solely from Pfam PF00326. **MEROPS clan SC groups enzymes by their shared α/β-hydrolase Ser-Asp-His fold**, and this clan includes many esterases and lipases that are **not** peptidases. KEGG independently classifies the FdeB reaction (R13077) as a hydrolase acting on a **lactone**, not a peptide bond.

**Interpretation:** The "peptidase" designation is a well-known artifact of fold-based automated annotation. The catalytic machinery (Ser-His-Asp on an α/β-hydrolase scaffold) is shared across peptidases, esterases, and lactonases within clan SC. Substrate identity — supplied here by pathway context and KEGG reaction mapping — is what distinguishes them, and all pathway evidence points to a lactone/ester substrate, not a peptide.

### Finding 4 — AlphaFold model confirms an assembled Ser268–Asp359–His394 catalytic triad (high confidence)

The AlphaFold model **AF-Q88I07-F1** has a mean pLDDT of **91.6** (very high confidence), with the catalytic residues themselves modeled at even higher confidence (per-residue pLDDT: Ser268 = 96.7, His394 = 94.8). The model shows a canonical, spatially assembled serine-hydrolase catalytic triad with textbook hydrogen-bond geometry:

| Interaction | Distance |
|-------------|----------|
| Ser268 Oγ — His394 Nε2 | 2.74 Å |
| His394 Nδ1 — Asp359 Oδ2 | 2.72 Å |
| Asp359 Oδ1 — His394 Nδ1 | 3.19 Å |

Ser268 lies in the GxSxG nucleophile-elbow motif "GVSLG." The residue order — nucleophile Ser268 … acid Asp359 … His394 near the C-terminus (in a "VQHSS" motif) — is the canonical clan-SC / α/β-hydrolase arrangement.

This structural analysis **corrected an earlier sequence-only provisional guess** (which had proposed His405/Asp341–345). The true catalytic histidine is His394 and the acid is Asp359, as revealed by the 3D geometry — a clear example of structure providing information that primary sequence alone could not.

**Interpretation:** An intact, high-confidence catalytic triad is direct structural evidence that PP_3195 is a catalytically competent serine hydrolase. Combined with the pathway assignment, this strongly supports lactonase/esterase activity.

### Finding 5 — FdeB occupies a unique, non-redundant lactone-hydrolase step in the ordered naringenin meta-cleavage pathway

Mapping every *fde* KO onto the full KEGG naringenin-degradation reaction sequence (rn00946) shows that FdeB fills a specific and non-redundant slot:

```
naringenin
   │  R13074  (FdeE / K26180 monooxygenase + FdeD / K26179)
   ▼
5,7,8-trihydroxy-2-(4-hydroxyphenyl)-2,3-dihydro-4H-chromen-4-one
   │  R13075  (FdeC / K26181 dioxygenase + FdeH / K26182)   ← ring dioxygenation / meta-cleavage
   ▼
(ring-cleaved intermediate)
   │  R13076  (FdeJ / K26183 cyclase)
   ▼
5-(4-hydroxyphenyl)-3-oxovalero-δ-lactone
   │  ►►► R13077  (FdeB / K26184)  ◄◄◄  + H2O   ← THIS PROTEIN: δ-lactone hydrolysis
   ▼
5-hydroxy-5-(4-hydroxyphenyl)-3-oxopentanoate
   │  R13078 / R13079  (FdeI / K26185)
   ▼
downstream products → central metabolism
```

**FdeB (K26184) is the ONLY KEGG ortholog assigned to R13077**, making the lactone-hydrolase step assignment specific and non-redundant. The enzyme acts after ring cleavage (FdeC) and cyclization (FdeJ), and before FdeI. Its physiological **substrate is a pathway-derived six-membered δ-lactone (a cyclic ester)** and the product is a linear 5-hydroxy-3-oxo-pentanoate.

**Interpretation:** In an ordered catabolic pathway, each enzyme performs one committed transformation. FdeB's unique assignment to the δ-lactone-opening reaction gives it a defined mechanistic role: it hydrolyzes the cyclic ester to a linear hydroxy-keto-acid, priming the molecule for downstream β-oxidation-like processing that ultimately feeds flavonoid carbon into central metabolism.

### Finding 6 — FdeB is a *distinct* enzyme from authentic FrsA (important disambiguation)

Although InterPro places PP_3195 in the "FrsA/Cutinase/Hydrolase-like" family (IPR050261), it is **not** the enteric fermentation/respiration-switch protein FrsA:

- PP_3195 shares only **~28% identity** with *E. coli* FrsA (P04335) and *Vibrio vulnificus* FrsA (Needleman-Wunsch global alignment).
- Authentic *E. coli* FrsA **lacks any GxSxG motif** (consistent with its reported cofactor-independent, non-classical decarboxylase mechanism — [PMID: 21623357](https://pubmed.ncbi.nlm.nih.gov/21623357/): *"FrsA converts pyruvate to acetaldehyde and carbon dioxide in a cofactor-independent manner"*), whereas PP_3195 **retains** the nucleophilic serine — i.e., it is a bona fide serine hydrolase.
- FrsA's physiological switch role is restricted to facultative anaerobes ([PMID: 15169777](https://pubmed.ncbi.nlm.nih.gov/15169777/): *"Orthologs of FrsA have been found to exist only in facultative anaerobes belonging to the gamma-proteobacterial group"*); *P. putida* is a **strict aerobe**, so PP_3195 is a **catabolic hydrolase, not a metabolic-switch regulator**.

**Interpretation:** Family membership alone would be misleading. The combination of low sequence identity, the presence of a GxSxG nucleophile FrsA lacks, and the aerobic host physiology all argue that PP_3195 is a catabolic serine lactonase/esterase rather than a metabolic-flux-switch decarboxylase.

---

## Mechanistic Model / Interpretation

Putting the findings together yields a coherent mechanistic picture:

**PP_3195/FdeB is the δ-lactone hydrolase of the lower naringenin meta-cleavage pathway in *P. putida* KT2440.** *P. putida* is a soil bacterium that establishes positive interactions with the plant rhizosphere (PMID 29607620), an environment rich in plant secondary metabolites including the flavanone **naringenin**. The *fde* gene cluster equips the organism to catabolize this flavonoid as a carbon source.

The pathway proceeds by:
1. **Oxygenation and ring modification** of naringenin (FdeE monooxygenase, FdeD);
2. **A-ring dioxygenation and meta-cleavage** (FdeC dioxygenase, FdeH);
3. **Cyclization** to a δ-lactone (FdeJ);
4. **Lactone ring-opening hydrolysis** — the step catalyzed by **FdeB/PP_3195**;
5. **Downstream conversion** of the resulting 3-oxo-pentanoate (FdeI) toward central metabolism.

Mechanistically, FdeB is a **serine hydrolase** operating through the classic charge-relay system: His394, polarized by Asp359, deprotonates the Ser268 hydroxyl, which then nucleophilically attacks the carbonyl carbon of the δ-lactone. A tetrahedral intermediate collapses, cleaving the C–O ester bond and opening the ring; a water molecule (activated by the same His) hydrolyzes the resulting acyl-enzyme, releasing the linear 5-hydroxy-5-(4-hydroxyphenyl)-3-oxopentanoate product and regenerating the free enzyme.

| Property | Assignment | Confidence | Basis |
|----------|-----------|------------|-------|
| Primary function | δ-Lactone hydrolase (lactonase / serine ester hydrolase) | Moderate–High | KEGG R13077 + intact catalytic triad + pathway logic |
| Reaction | 5-(4-hydroxyphenyl)-3-oxovalero-δ-lactone + H₂O → 5-hydroxy-5-(4-hydroxyphenyl)-3-oxopentanoate | Moderate | KEGG orthology, unvalidated at protein level |
| Substrate specificity | Flavonoid-derived δ-lactone (naringenin catabolite) | Moderate | Pathway context; no direct assay |
| Catalytic mechanism | Ser268–His394–Asp359 charge-relay serine hydrolase | High | AlphaFold triad geometry (pLDDT >94, H-bonds ~2.7 Å) |
| Localization | Cytoplasm | High | No signal peptide/lipobox; intracellular pathway |
| Pathway | Naringenin/flavonoid degradation (KEGG ppu00946) | High | KEGG ortholog K26184, *fde* cluster |
| NOT a true peptidase | Correct | High | "Peptidase S9" is fold-based IEA; KEGG reaction acts on lactone |
| NOT FrsA-type switch protein | Correct | High | ~28% identity, retains GxSxG (FrsA lacks it), aerobe |

The single most important corrective insight from this investigation is that the **UniProt "Peptidase S9" name is misleading**. It arises because MEROPS clan SC groups proteins by their shared α/β-hydrolase Ser-His-Asp fold — a fold used by peptidases, esterases, lipases, and lactonases alike. Genomic context and KEGG reaction mapping resolve the ambiguity decisively in favor of a **lactone/ester hydrolase acting in flavonoid catabolism**.

---

## Supported and Refuted Hypotheses

| Hypothesis | Verdict | Basis |
|------------|---------|-------|
| PP_3195 is a serine α/β-hydrolase with a Ser-Asp-His triad | **Supported (structurally confirmed)** | AlphaFold triad Ser268–Asp359–His394 (2.7 Å H-bonds, pLDDT >94); GxSxG motif |
| PP_3195 is a catabolic enzyme of the naringenin/flavonoid degradation (*fde*) pathway | **Supported** | KEGG K26184/*fdeB*, genomic cluster, ppu00946 |
| Its reaction is hydrolysis of a δ-lactone (ester/lactonase), not proteolysis | **Supported (predicted)** | KEGG R13077, family = esterases; "peptidase" is fold-based only |
| PP_3195 is the fermentation/respiration-switch protein FrsA | **Refuted** | ~28% identity, has Ser nucleophile FrsA lacks, host is an obligate aerobe |
| PP_3195 is a genuine prolyl oligopeptidase / active peptidase | **Not supported** | Only IEA fold-based GO; no peptidase evidence; KEGG reaction is a hydrolase on a lactone |
| PP_3195 functions in the cytoplasm | **Supported** | No signal/lipobox; pathway analogy |

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports / relates to the findings |
|------|-----------------|-------------------------------------------|
| [27059806](https://pubmed.ncbi.nlm.nih.gov/27059806/) | *Genetic and functional characterization of a novel meta-pathway for degradation of naringenin in* Herbaspirillum seropedicae *SmR1* | Establishes the *fde* gene nomenclature and the naringenin meta-cleavage pathway; documents FdeE monooxygenation and FdeC A-ring dioxygenation/cleavage — the upstream steps producing intermediates on which FdeB acts. Primary source of the pathway model. |
| [30951551](https://pubmed.ncbi.nlm.nih.gov/30951551/) | *Purification and biochemical characterization of FrsA protein from* Vibrio vulnificus *as an esterase* | Demonstrates that FrsA/esterase-family proteins (InterPro IPR050261, which contains PP_3195) hydrolyze esters (notably p-nitrophenyl acetate), supporting the ester/lactone-hydrolase assignment for FdeB. |
| [15169777](https://pubmed.ncbi.nlm.nih.gov/15169777/) | *A novel fermentation/respiration switch protein regulated by enzyme IIAGlc in* E. coli | Shows authentic FrsA's metabolic-switch role is restricted to facultative anaerobes; since *P. putida* is a strict aerobe and PP_3195 is only ~28% identical to FrsA, PP_3195 is a catabolic hydrolase, not a switch regulator. |
| [21623357](https://pubmed.ncbi.nlm.nih.gov/21623357/) | *FrsA functions as a cofactor-independent decarboxylase to control metabolic flux* | Defines the distinct decarboxylase activity of authentic FrsA; contrast reinforces that PP_3195 (which retains the GxSxG serine FrsA lacks) belongs to a different functional class. |
| [29607620](https://pubmed.ncbi.nlm.nih.gov/29607620/) | *Regulation of carbohydrate degradation pathways in* Pseudomonas | Context for *P. putida* as a rhizosphere-associated soil bacterium with robust catabolism of aromatic compounds — the ecological rationale for flavonoid degradation. |
| [35294082](https://pubmed.ncbi.nlm.nih.gov/35294082/) | *Bacterial mandelic acid degradation pathway...* | Illustrates the broader theme of *P. putida* aromatic-compound catabolic pathways to which the *fde* cluster belongs. |

The AlphaFold structural model (AF-Q88I07-F1) and KEGG pathway/ortholog assignments (K26184, ppu00946, reactions R13074–R13079) constitute the primary database-derived evidence, complemented by the peer-reviewed literature above that validates the enzymology of the FrsA/esterase family and the naringenin pathway.

---

## Limitations and Knowledge Gaps

1. **No direct experimental data on PP_3195/Q88I07 itself.** All functional calls are by orthology (KEGG K26184, COG1506), genomic context, and domain/residue/structure analysis. The *Herbaspirillum* study directly characterized FdeE and FdeC by mutagenesis + LC-MS/MS but **not FdeB**, so FdeB's exact catalytic step is inferred. Targeted PubMed searches returned **no primary study of PP_3195 or of *P. putida* KT2440 growth on naringenin**; the KEGG *fde* KO assignments (K26179–K26185) appear to derive largely from the single *Herbaspirillum* characterization propagated by orthology.

2. **The pathway model derives from a different organism.** Orthology in *P. putida* is strongly supported but formally unproven at the biochemical level.

3. **KEGG flags R13077 as an "unclear reaction."** The specific δ-lactone substrate/product pair is a computational reconstruction; the exact chemical structure and regiochemistry of the physiological substrate have not been experimentally confirmed for FdeB.

4. **Catalytic triad is a model, not an experimental structure.** The Ser268–Asp359–His394 triad comes from a high-confidence AlphaFold model (pLDDT >90), not from an experimental X-ray/cryo-EM structure or site-directed mutagenesis. Confidence is high but not equivalent to experimental proof.

5. **Substrate specificity breadth is unknown.** Whether FdeB acts narrowly on the naringenin-derived δ-lactone or has broader esterase/lactonase promiscuity (as many α/β-hydrolases do) is untested.

6. **Regulation and expression are uncharacterized.** Whether the *fde* cluster is induced by naringenin, its transcriptional regulators, and growth conditions supporting flavonoid catabolism in *P. putida* KT2440 are not addressed by available data.

**Overall confidence:** High for "cytoplasmic serine α/β-hydrolase with a Ser268-Asp359-His394 triad" (structurally confirmed); moderate-to-high for the specific δ-lactone-hydrolase step and substrate (consistent orthology + unique KO→reaction mapping, but not enzymatically demonstrated).

---

## Proposed Follow-up Experiments / Actions

1. **Heterologous expression and enzyme assay.** Clone PP_3195, express and purify the recombinant protein, and test hydrolysis of the predicted δ-lactone substrate (or surrogates such as p-nitrophenyl esters and model lactones) to confirm lactonase/esterase activity and determine kinetic parameters (kcat, Km).

2. **Site-directed mutagenesis of the catalytic triad.** Generate Ser268Ala, His394Ala, and Asp359Ala/Asn mutants and confirm loss of activity, experimentally validating the AlphaFold-predicted triad and the identity of the catalytic nucleophile.

3. **Gene knockout / complementation in *P. putida* KT2440.** Delete PP_3195 and test growth on naringenin as sole carbon source; look for accumulation of the upstream δ-lactone intermediate (by LC-MS) and rescue by complementation.

4. **Metabolite identification.** Use LC-MS/MS and NMR to characterize the physiological substrate and product of FdeB in vivo, directly testing the KEGG R13077 assignment and its regiochemistry.

5. **Experimental structure determination.** Solve an X-ray or cryo-EM structure, ideally with substrate/product analog bound, to confirm the active-site architecture and define specificity determinants.

6. **Transcriptional analysis.** Perform RT-qPCR or RNA-seq of the *fde* cluster ± naringenin to establish inducibility and identify the regulator controlling flavonoid catabolism.

7. **Substrate-range profiling.** Screen a panel of lactones and esters to define the enzyme's specificity and assess biocatalytic potential (e.g., for flavonoid bioconversion or green-chemistry applications).

---

## Conclusion

PP_3195 (Q88I07) is **FdeB**, a **cytoplasmic α/β-hydrolase-fold serine hydrolase** of the **naringenin/flavonoid degradation (*fde*) gene cluster** of *Pseudomonas putida* KT2440 (KEGG ortholog K26184, pathway ppu00946). Its primary function is a **δ-lactone hydrolase (lactonase)** step in the lower naringenin meta-cleavage pathway (KEGG reaction R13077): it hydrolyzes 5-(4-hydroxyphenyl)-3-oxovalero-δ-lactone + H₂O to 5-hydroxy-5-(4-hydroxyphenyl)-3-oxopentanoate, acting after ring cleavage (FdeC) and cyclization (FdeJ) and before FdeI, thereby channeling flavonoid carbon toward central metabolism. It functions as an **ester/lactone hydrolase rather than a true peptidase** — the "Peptidase S9" UniProt name reflects only MEROPS clan-SC fold homology. The assignment is supported by a **structurally confirmed catalytic triad** (AlphaFold Ser268-Asp359-His394, ~2.7 Å H-bonds, pLDDT >94), **genomic clustering**, and **orthology**, but the protein itself has **not yet been directly characterized experimentally** and is distinct from (~28% identity to) the enteric fermentation/respiration-switch protein FrsA.

---

### Primary References

- Marin et al. (2016) *Environ. Microbiol.* Novel meta-pathway for naringenin degradation in *Herbaspirillum seropedicae* SmR1. **PMID 27059806** (defines *fde* pathway/genes).
- Koo et al. (2004) A novel fermentation/respiration switch protein (FrsA) regulated by enzyme IIA^Glc in *E. coli*. **PMID 15169777** (FrsA family context; restricted to facultative anaerobes).
- Lee et al. (2011) FrsA functions as a cofactor-independent decarboxylase. **PMID 21623357** (FrsA structure/mechanism; contrast to PP_3195).
- Wang et al. (2019) FrsA from *Vibrio vulnificus* is an esterase. **PMID 30951551** (family = ester hydrolases).
- Database records: UniProt Q88I07; InterPro IPR050261/IPR001375/IPR029058; KEGG K26184, ppu00946, R13077, COG1506; AlphaFold AF-Q88I07-F1.


## Artifacts

- [OpenScientist final report](PP_3195-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PP_3195-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:27059806
2. PMID:30951551
3. PMID:21623357
4. PMID:15169777