---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-17T06:44:37.959068'
end_time: '2026-07-17T07:04:56.365853'
duration_seconds: 1218.41
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: bioH
  gene_symbol: bioH
  uniprot_accession: Q88QX0
  protein_description: 'SubName: Full=Pimeloyl-[acp] methyl ester esterase {ECO:0000313|EMBL:AAN65995.1};
    EC=3.1.1.1 {ECO:0000313|EMBL:AAN65995.1}; EC=3.1.1.85 {ECO:0000313|EMBL:AAN65995.1};'
  gene_info: Name=bioH {ECO:0000313|EMBL:AAN65995.1}; OrderedLocusNames=PP_0364 {ECO:0000313|EMBL:AAN65995.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: AB_hydrolase_1. (IPR000073); AB_hydrolase_fold. (IPR029058); Carboxylesterase_BioH.
    (IPR050228); Abhydrolase_6 (PF12697)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 7
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: bioH-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: bioH-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88QX0
- **Protein Description:** SubName: Full=Pimeloyl-[acp] methyl ester esterase {ECO:0000313|EMBL:AAN65995.1}; EC=3.1.1.1 {ECO:0000313|EMBL:AAN65995.1}; EC=3.1.1.85 {ECO:0000313|EMBL:AAN65995.1};
- **Gene Information:** Name=bioH {ECO:0000313|EMBL:AAN65995.1}; OrderedLocusNames=PP_0364 {ECO:0000313|EMBL:AAN65995.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** AB_hydrolase_1. (IPR000073); AB_hydrolase_fold. (IPR029058); Carboxylesterase_BioH. (IPR050228); Abhydrolase_6 (PF12697)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "bioH" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'bioH' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **bioH** (gene ID: bioH, UniProt: Q88QX0) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of BioH (Q88QX0 / PP_0364) in *Pseudomonas putida* KT2440

## Summary

**BioH (UniProt Q88QX0; ordered locus PP_0364) of *Pseudomonas putida* KT2440 is a cytoplasmic α/β-hydrolase-fold serine esterase that catalyzes the terminal step in the biosynthesis of the pimelate moiety of biotin.** Its physiological reaction is the hydrolysis of pimeloyl-[acyl-carrier-protein] (ACP) methyl ester to pimeloyl-ACP plus methanol (EC 3.1.1.85). This activity, together with the *O*-methyltransferase BioC, constitutes the "early stage" of bacterial biotin biosynthesis — a route in which the intermediates of the pimelate precursor are chemically disguised as fatty-acid-synthesis substrates and processed by the host's type-II fatty-acid-synthase (FAS-II) machinery. BioH is the demethylation "gatekeeper" that reverses BioC's methyl esterification once the pimeloyl chain has reached the correct length, releasing free pimeloyl-ACP for entry into the conserved late-stage biotin pathway.

The protein is a small (~243 amino acid) soluble globular enzyme lacking any signal peptide or transmembrane segment, and therefore performs its catalysis in the **cytoplasm**, consistent with the cytosolic localization of its ACP-tethered substrate and of the FAS-II machinery that generates it. Mechanistically, BioH uses a classic **Ser–His–Asp catalytic triad** situated on a canonical α/β-hydrolase nucleophile elbow. In the paradigm *Escherichia coli* enzyme this triad is Ser82–His235–Asp207; sequence alignment shows that these residues are strictly conserved in the *P. putida* ortholog at positions **Ser68–Asp191–His219**, embedded within a conserved "GWSLGG" nucleophile-elbow motif, despite only ~30% overall sequence identity between the two orthologs.

BioH carries a dual EC annotation (EC 3.1.1.1 carboxylesterase and EC 3.1.1.85 pimeloyl-ACP methyl ester esterase). This reflects the history of the protein's characterization: BioH was first structurally and enzymologically described as a generic carboxylesterase with a preference for short acyl-chain esters, before its true physiological substrate — pimeloyl-ACP methyl ester — was identified. The carboxylesterase annotation therefore captures *in vitro* substrate promiscuity, whereas EC 3.1.1.85 captures the dedicated biological role. Importantly, the *P. putida* biotin operon (*bioBFHCD*, including *bioH*/PP_0364) has been shown to be genuinely functional: it reconstitutes biotin biosynthesis when engineered into *E. coli*, confirming that Q88QX0 is a bona fide, active BioH esterase and not merely a computational annotation.

---

## Key Findings

### Finding 1 — BioH catalyzes the last step of pimelate-moiety synthesis: hydrolysis of pimeloyl-ACP methyl ester

The defining function of BioH is the hydrolysis of **pimeloyl-ACP methyl ester → pimeloyl-ACP + methanol**, the reaction assigned to Q88QX0 as EC 3.1.1.85. This was established in the paradigm *E. coli* system through combined *in vivo* and *in vitro* reconstitution of the early biotin pathway (Lin, Hanson & Cronan, 2010, *Nature Chemical Biology*). In that work, the malonyl-thioester methyl ester produced by the BioC methyltransferase "enters fatty acid synthesis as the primer and undergoes two reiterations of the fatty acid elongation cycle to give pimeloyl-acyl carrier protein (ACP) methyl ester, which is hydrolyzed to pimeloyl-ACP and methanol by BioH" ([PMID: 20693992](https://pubmed.ncbi.nlm.nih.gov/20693992/)).

BioH therefore acts as the demethylating enzyme that terminates the FAS-II-based assembly of the seven-carbon pimelate chain. A later review reinforces BioH's status as the reference enzyme for this reaction: "The paradigm cleavage enzyme is *Escherichia coli* BioH which together with the BioC methyltransferase allows synthesis of the pimelate moiety by a modified fatty acid biosynthetic pathway" ([PMID: 26868423](https://pubmed.ncbi.nlm.nih.gov/26868423/)). Because Q88QX0 is annotated with exactly this EC number and belongs to the *bioH* gene, this reaction is the primary function attributable to the *P. putida* protein.

### Finding 2 — The *P. putida* biotin operon *bioBFHCD* (including bioH/PP_0364) is functional

A key concern in annotating a non-model-organism protein is whether the gene is genuinely functional or merely inferred by homology. This concern is directly resolved for *P. putida* BioH. Wei et al. (2021) engineered the *Pseudomonas putida* biotin operon — "which consisted of a *bioBFHCD* cluster and a *bioA* gene" — into *Escherichia coli* for heterologous biotin production ([PMID: 33666816](https://pubmed.ncbi.nlm.nih.gov/33666816/)). The resulting strain supported biotin synthesis, demonstrating that the *P. putida* BioH within the *bioBFHCD* cluster is a bona fide, catalytically active pimeloyl-ACP methyl ester esterase capable of functioning within an operon-encoded biotin pathway. This provides functional (not merely bioinformatic) validation that Q88QX0/PP_0364 performs the BioH reaction.

### Finding 3 — BioH is an α/β-hydrolase serine esterase using a Ser–His–Asp triad; its dual EC annotation reflects in vitro promiscuity with a specific physiological substrate

BioH belongs to the **α/β-hydrolase superfamily** (InterPro AB_hydrolase_1 / AB_hydrolase_fold; Pfam Abhydrolase_6 / PF12697; the Carboxylesterase_BioH family IPR050228). Enzymes of this class catalyze ester hydrolysis via a Ser–His–Asp catalytic triad. The mechanistic importance of this triad in pimeloyl-ACP methyl ester esterases is confirmed by studies of the analogous enzymes: for BioJ, "the BioJ catalytic triad consists of Ser151, Asp248 and His278, all of which are essential for activity" ([PMID: 24313380](https://pubmed.ncbi.nlm.nih.gov/24313380/)).

Notably, several evolutionarily distinct enzymes converge on this same chemical reaction. As Shapiro et al. (2012) observed, "Although the BioH, BioG and BioK esterases catalyze a common reaction, the proteins are evolutionarily distinct" ([PMID: 23152908](https://pubmed.ncbi.nlm.nih.gov/23152908/)). BioH is the paradigm, but bacteria variously use BioG, BioK, BioJ, or BioV to accomplish the same demethylation step — a striking example of non-orthologous gene displacement.

The dual EC annotation of Q88QX0 (EC 3.1.1.1 / EC 3.1.1.85) is a direct consequence of this enzyme's history. BioH was originally mis-annotated as a generic carboxylesterase (EC 3.1.1.1) based on its broad *in vitro* activity toward short-chain esters, before its physiological substrate — pimeloyl-ACP methyl ester (EC 3.1.1.85) — was identified. Both numbers are therefore "correct," but they describe different levels of specificity: EC 3.1.1.1 reflects promiscuous laboratory activity, and EC 3.1.1.85 reflects the dedicated biological role in biotin synthesis.

### Finding 4 — The E. coli BioH crystal structure defines the Ser82–His235–Asp207 triad and short-chain carboxylesterase activity

The structural basis for the α/β-hydrolase mechanism was established by Sanishvili et al. (2003), who solved the *E. coli* BioH crystal structure at **1.7 Å** resolution as part of a structural-genomics effort to assign function. Automated active-site template matching "identified a catalytic triad (Ser82, His235, and Asp207) with a configuration similar to that of the catalytic triad of hydrolases. Analysis of BioH with a panel of hydrolase assays revealed a carboxylesterase activity with a preference for short acyl chain substrates" ([PMID: 12732651](https://pubmed.ncbi.nlm.nih.gov/12732651/)).

This study is foundational for two reasons. First, it provides the experimentally determined geometry of the catalytic triad that all downstream annotations rely upon. Second, the observed preference for short acyl-chain substrates foreshadowed — but did not yet reveal — the true substrate, and it explains the historical EC 3.1.1.1 carboxylesterase assignment. This work exemplifies the "integrate structure, bioinformatics, and enzymology to discover function" approach, and it directly underpins the α/β-hydrolase serine-esterase mechanism assigned to Q88QX0, which shares the AB_hydrolase and Carboxylesterase_BioH domains.

### Finding 5 — BioH acts in the divergent "early stage" of biotin biosynthesis, feeding the conserved late-stage pathway

Bacterial biotin biosynthesis is naturally divided into two stages. A 2026 review states that "the late stage of biotin biosynthesis is a conserved pathway in which biotin is synthesized from a pimelate precursor using four conserved enzymes, whereas the early stage remained largely unknown until its discovery in *Escherichia coli* in 2010" ([PMID: 41943454](https://pubmed.ncbi.nlm.nih.gov/41943454/)).

BioH operates in the **early stage** — the assembly of the pimelate moiety. Together with BioC, it produces pimeloyl-ACP. This thioester precursor then enters the conserved **late stage**: it is condensed with L-alanine by BioF (KAPA synthase / 7-keto-8-aminopelargonic acid synthase), transaminated by BioA, cyclized by BioD (dethiobiotin synthetase), and finally sulfurated by BioB (biotin synthase) to give mature biotin. The early stage is remarkable for its evolutionary divergence: whereas the four late-stage enzymes are conserved, the demethylation step performed by BioH is accomplished by different, unrelated proteins (BioG, BioK, BioJ, BioV) in different taxa. BioH thus occupies a mechanistically pivotal but evolutionarily plastic node of the pathway.

### Finding 6 — Q88QX0 is a genuine BioH ortholog: it retains the complete catalytic triad and nucleophile elbow

To directly verify that the *P. putida* protein is a true BioH, a global pairwise (Needleman–Wunsch) alignment was computed between Q88QX0 (*P. putida* BioH, 243 aa) and P13001 (*E. coli* BioH, 256 aa). The two orthologs share only ~**30–32% amino-acid identity** (76/239 ungapped positions) — low enough that homology alone would leave residual uncertainty, but the functionally decisive residues are strictly conserved.

All three catalytic-triad residues map to identical Ser/Asp/His positions in the alignment: *E. coli* **Ser82, Asp207, and His235** each align to a conserved Ser/Asp/His in *P. putida*. Moreover, the α/β-hydrolase **nucleophile-elbow motif is perfectly conserved** — the *E. coli* "GWSLGG" sequence around the catalytic serine matches "GWSLGG" in *P. putida*. This conservation of the catalytic machinery, in the context of an otherwise divergent sequence, is exactly the signature expected of a true functional ortholog. It provides sequence-level confirmation that Q88QX0 retains the intact BioH active site and mechanism defined structurally in *E. coli* ([PMID: 12732651](https://pubmed.ncbi.nlm.nih.gov/12732651/)).

### Finding 7 — BioH is a soluble cytoplasmic enzyme; the P. putida triad is Ser68–Asp191–His219

Mapping the aligned catalytic residues onto the *P. putida* numbering places the Q88QX0 triad at **Ser68** (within the "GWSLGG" nucleophile elbow), **Asp191**, and **His219**, exactly corresponding to *E. coli* BioH Ser82/Asp207/His235.

Regarding localization, BioH is a small (~243 aa) soluble globular α/β-hydrolase with **no signal peptide and no transmembrane segment**; the *E. coli* ortholog was crystallized as a soluble cytosolic protein. Decisively, its physiological substrate — pimeloyl-ACP methyl ester — is generated by the cytoplasmic FAS-II machinery and remains tethered to acyl carrier protein, an obligately cytosolic component. Because BioH acts on an ACP-bound intermediate — "pimeloyl-acyl carrier protein (ACP) methyl ester, which is hydrolyzed to pimeloyl-ACP and methanol by BioH" ([PMID: 20693992](https://pubmed.ncbi.nlm.nih.gov/20693992/)) — its catalysis necessarily occurs in the **cytoplasm**.

---

## Mechanistic Model / Interpretation

### The "hijacked fatty-acid-synthesis" route to the pimelate moiety

Biotin's bicyclic ring is built onto a seven-carbon dicarboxylic acid (pimelate). Bacteria assemble this pimelate chain not by a dedicated pathway, but by temporarily disguising the growing chain as a fatty-acid intermediate so that the abundant FAS-II elongation machinery does the work. BioC and BioH are the enzymes that open and close this disguise:

```
                          EARLY STAGE (pimelate-moiety synthesis)
                          =======================================

   malonyl-ACP
       |
       |  BioC  (S-adenosyl-methionine-dependent O-methyltransferase)
       |  adds a methyl ester -> "disguises" the free carboxylate
       v
   malonyl-ACP methyl ester
       |
       |  FAS-II elongation cycle x2  (FabB/F, FabG, FabA/Z, FabI)
       |  chain grows from C3 -> C7
       v
   pimeloyl-ACP methyl ester
       |
       |  *** BioH ***   (EC 3.1.1.85; Ser68-Asp191-His219 triad)
       |  hydrolyzes the methyl ester -> removes the disguise
       v
   pimeloyl-ACP  +  methanol
       |
       |  ----------------------------------------------------------
       v
                          LATE STAGE (conserved, 4 enzymes)
                          ================================
   pimeloyl-ACP + L-alanine
       |  BioF (KAPA synthase)          -> 7-keto-8-aminopelargonate (KAPA)
       |  BioA (aminotransferase)       -> 7,8-diaminopelargonate (DAPA)
       |  BioD (dethiobiotin synthetase)-> dethiobiotin
       |  BioB (biotin synthase)        -> BIOTIN
       v
   BIOTIN
```

**Why methyl esterification, and why BioH?** The free ω-carboxylate of malonyl-ACP is chemically incompatible with the hydrophobic active sites of the FAS-II enzymes, which normally handle uncharged acyl chains. BioC's methyl ester neutralizes this charge, allowing the FAS-II enzymes to elongate the chain. But the methyl ester must be removed before the pimelate can serve as a biotin precursor, because the downstream late-stage enzymes and the final biotin structure require the free dicarboxylic acid. BioH is the esterase that performs this removal, and its timing is critical: it acts specifically once the chain has reached the pimeloyl (C7) stage. In this sense BioH functions as a **chain-length "gatekeeper"** whose substrate selectivity helps ensure that the correct seven-carbon precursor is released.

### Catalytic mechanism

BioH is a serine hydrolase of the α/β-hydrolase fold. Catalysis proceeds by the canonical two-step (acylation/deacylation) mechanism:

| Step | Event | Residue role |
|------|-------|--------------|
| 1 | His (general base) deprotonates the catalytic Ser | His219, Asp191 orient/polarize |
| 2 | Ser nucleophile attacks the ester carbonyl | Ser68 (nucleophile elbow) |
| 3 | Tetrahedral intermediate; oxyanion hole stabilizes | backbone amides |
| 4 | Methanol leaves; acyl-enzyme forms | — |
| 5 | Water (activated by His) hydrolyzes acyl-enzyme | releases pimeloyl-ACP |

The triad geometry is directly inherited from the structurally characterized *E. coli* enzyme (Ser82–His235–Asp207; [PMID: 12732651](https://pubmed.ncbi.nlm.nih.gov/12732651/)) and maps onto Ser68–Asp191–His219 in *P. putida*.

### Ortholog comparison table

| Property | *E. coli* BioH (P13001) | *P. putida* BioH (Q88QX0 / PP_0364) |
|---|---|---|
| Length | 256 aa | 243 aa |
| Fold | α/β-hydrolase | α/β-hydrolase (Pfam PF12697; IPR050228) |
| Catalytic Ser | Ser82 (GWSLGG elbow) | Ser68 (GWSLGG elbow) |
| Catalytic Asp | Asp207 | Asp191 |
| Catalytic His | His235 | His219 |
| Pairwise identity | — | ~30–32% vs. *E. coli* |
| Reaction | pimeloyl-ACP methyl ester → pimeloyl-ACP + MeOH | same (EC 3.1.1.85) |
| Localization | soluble cytosolic (crystallized) | soluble cytosolic (no signal peptide/TM) |
| Functional validation | reconstituted *in vivo*/*in vitro* | operon reconstitutes biotin synthesis in *E. coli* |

The low overall identity but perfect conservation of the catalytic apparatus is the hallmark of a genuine ortholog whose function is preserved under divergent evolution — reinforcing the annotation while explaining why databases carry both a specific (EC 3.1.1.85) and a generic (EC 3.1.1.1) descriptor.

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution to this report |
|------|-----------------|-----------------------------|
| [20693992](https://pubmed.ncbi.nlm.nih.gov/20693992/) | *Biotin synthesis begins by hijacking the fatty acid synthetic pathway* | **Primary functional evidence.** Defines the BioH reaction (pimeloyl-ACP methyl ester → pimeloyl-ACP + methanol) and its cytoplasmic, ACP-tethered substrate. Supports Findings 1 and 7. |
| [12732651](https://pubmed.ncbi.nlm.nih.gov/12732651/) | *Integrating structure, bioinformatics, and enzymology... BioH, a new carboxylesterase from E. coli* | **Structural/mechanistic anchor.** 1.7 Å crystal structure; defines Ser82–His235–Asp207 triad and short-chain carboxylesterase activity (explains EC 3.1.1.1). Supports Findings 3, 4, 6. |
| [26868423](https://pubmed.ncbi.nlm.nih.gov/26868423/) | *A Biotin Biosynthesis Gene Restricted to Helicobacter* | Establishes BioH as the paradigm cleavage enzyme acting with BioC. Supports Finding 1. |
| [33666816](https://pubmed.ncbi.nlm.nih.gov/33666816/) | *Engineering a heterologous synthetic pathway in E. coli for efficient production of biotin* | **Functional validation of the target ortholog.** *P. putida bioBFHCD* (incl. *bioH*) reconstitutes biotin synthesis. Supports Finding 2. |
| [24313380](https://pubmed.ncbi.nlm.nih.gov/24313380/) | *A Francisella virulence factor catalyses an essential reaction of biotin synthesis* | Documents the essential Ser–Asp–His triad in an analogous pimeloyl-ACP methyl ester esterase (BioJ). Supports Finding 3. |
| [23152908](https://pubmed.ncbi.nlm.nih.gov/23152908/) | *Remarkable diversity in the enzymes catalyzing the last step in synthesis of the pimelate moiety of biotin* | Establishes that BioH, BioG, BioK catalyze a common reaction but are evolutionarily distinct (non-orthologous displacement). Supports Findings 3, 5. |
| [41943454](https://pubmed.ncbi.nlm.nih.gov/41943454/) | *Early Stage of Biotin Biosynthesis Pathway: Non-Conserved Yet Unique* | Frames the early (BioC/BioH) vs. conserved late (BioF→BioA→BioD→BioB) stages. Supports Finding 5. |

Supporting bioinformatic evidence (Findings 6 and 7) was generated within this investigation by fetching the UniProt sequences of Q88QX0 and P13001 and computing a Needleman–Wunsch global alignment, which demonstrated strict conservation of the catalytic triad and the GWSLGG nucleophile elbow.

**Peripheral literature.** Several additional papers surfaced during literature search (e.g., on B-vitamin immunology, pyruvate carboxylase inhibitors, PII/BCCP regulation, sulfur incorporation into biomolecules) confirm the broader biological importance of biotin and biotin-dependent enzymes but do not bear directly on the specific catalytic function of BioH; they were reviewed and set aside as not directly supporting the mechanistic claims of this report.

---

## Limitations and Knowledge Gaps

1. **No direct biochemical characterization of the *P. putida* enzyme.** The functional assignment of Q88QX0 rests on (i) the paradigm *E. coli* BioH biochemistry, (ii) sequence-level conservation of the catalytic triad in *P. putida*, and (iii) operon-level functional reconstitution of the *P. putida bioBFHCD* cluster in *E. coli*. Purified *P. putida* BioH has not, to our knowledge, been kinetically characterized directly (no *k*cat/*K*m against pimeloyl-ACP methyl ester specifically for Q88QX0).

2. **No experimental structure of the *P. putida* protein.** The Ser68–Asp191–His219 triad and cytoplasmic localization are inferred from the *E. coli* crystal structure and from sequence/domain analysis, not from a *P. putida* crystal or cryo-EM structure. An AlphaFold model would strengthen (but not replace) this inference.

3. **Modest overall sequence identity (~30%).** While the catalytic residues and nucleophile elbow are conserved, the low global identity means substrate-specificity determinants (e.g., the acyl-chain-length selectivity pocket) could differ subtly between the *E. coli* and *P. putida* enzymes. Whether *P. putida* BioH has the same short-chain preference/promiscuity profile is untested.

4. **Substrate specificity is inferred, not measured, for this ortholog.** The dual EC annotation implies *in vitro* promiscuity, but the range of esters *P. putida* BioH can hydrolyze — and whether it, like the *E. coli* enzyme, prefers short acyl chains — has not been directly determined.

5. **Physiological essentiality in *P. putida* is not established here.** In *E. coli*, *bioH* deletion is complemented by exogenous biotin or by heterologous esterases. Whether PP_0364 is conditionally essential (biotin-free medium) in *P. putida* itself has not been directly tested in the evidence reviewed.

---

## Proposed Follow-up Experiments / Actions

1. **Direct enzymatic assay of purified Q88QX0.** Express and purify recombinant *P. putida* BioH and measure hydrolysis of pimeloyl-ACP methyl ester (and *p*-nitrophenyl short-chain esters as convenient surrogates) to obtain *k*cat/*K*m, directly confirming EC 3.1.1.85 activity for this specific protein.

2. **Active-site mutagenesis.** Generate S68A, D191N, and H219A variants and confirm loss of esterase activity, experimentally validating the inferred triad assignment.

3. **Genetic complementation / knockout.** Test whether PP_0364 complements an *E. coli* Δ*bioH* strain for biotin prototrophy, and whether a *P. putida* Δ*PP_0364* mutant is biotin auxotrophic (i.e., rescued by exogenous biotin), establishing physiological essentiality.

4. **Structure determination or AlphaFold analysis.** Solve or model the *P. putida* BioH structure to confirm triad geometry, the oxyanion hole, and the acyl-binding pocket; compare the pocket to *E. coli* BioH to predict substrate-length preference.

5. **Substrate-specificity profiling.** Screen a panel of acyl esters of varying chain length to determine whether *P. putida* BioH shares the short-chain carboxylesterase promiscuity of its *E. coli* counterpart, clarifying the basis of the dual EC annotation for this ortholog.

6. **Pathway context confirmation.** Verify co-transcription and genomic synteny of *bioBFHCD* in *P. putida* KT2440 and confirm that BioH functions with the native BioC, establishing that the "hijacked FAS-II" route operates in this organism as in *E. coli*.

---

## Conclusion

BioH (Q88QX0 / PP_0364) in *Pseudomonas putida* KT2440 is a soluble cytoplasmic α/β-hydrolase-fold serine esterase that performs the final step of pimelate-moiety synthesis in biotin biosynthesis: hydrolysis of pimeloyl-ACP methyl ester to pimeloyl-ACP and methanol (EC 3.1.1.85), using a Ser68–Asp191–His219 catalytic triad on a conserved GWSLGG nucleophile elbow. Working with BioC, it operates in the divergent early stage of biotin synthesis, converting a chemically disguised fatty-acid-synthesis intermediate back into a free pimelate precursor that feeds the conserved late-stage enzymes (BioF→BioA→BioD→BioB) to produce biotin. Its secondary carboxylesterase annotation (EC 3.1.1.1) is a historical artifact reflecting *in vitro* promiscuity toward short-chain esters rather than a distinct biological role. The assignment is supported by paradigm *E. coli* biochemistry and structure, by strict conservation of the catalytic apparatus in the *P. putida* ortholog, and by functional reconstitution of the *P. putida bioBFHCD* operon in *E. coli*.


## Artifacts

- [OpenScientist final report](bioH-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](bioH-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:20693992
2. PMID:26868423
3. PMID:33666816
4. PMID:24313380
5. PMID:23152908
6. PMID:12732651
7. PMID:41943454