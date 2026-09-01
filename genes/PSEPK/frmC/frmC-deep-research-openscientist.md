---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T08:27:04.684924'
end_time: '2026-09-01T09:25:54.625491'
duration_seconds: 3529.94
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: frmC
  gene_symbol: frmC
  uniprot_accession: Q88MF4
  protein_description: 'RecName: Full=S-formylglutathione hydrolase {ECO:0000256|NCBIfam:TIGR02821,
    ECO:0000256|RuleBase:RU363068}; EC=3.1.2.12 {ECO:0000256|NCBIfam:TIGR02821, ECO:0000256|RuleBase:RU363068};'
  gene_info: Name=frmC {ECO:0000313|EMBL:AAN67238.1}; OrderedLocusNames=PP_1617 {ECO:0000313|EMBL:AAN67238.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the esterase D family.
  protein_domains: AB_hydrolase_fold. (IPR029058); Esterase-like. (IPR000801); S-formylglutathione_hydrol.
    (IPR014186); Esterase (PF00756)
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
citation_count: 21
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: frmC-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: frmC-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88MF4
- **Protein Description:** RecName: Full=S-formylglutathione hydrolase {ECO:0000256|NCBIfam:TIGR02821, ECO:0000256|RuleBase:RU363068}; EC=3.1.2.12 {ECO:0000256|NCBIfam:TIGR02821, ECO:0000256|RuleBase:RU363068};
- **Gene Information:** Name=frmC {ECO:0000313|EMBL:AAN67238.1}; OrderedLocusNames=PP_1617 {ECO:0000313|EMBL:AAN67238.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the esterase D family.
- **Key Domains:** AB_hydrolase_fold. (IPR029058); Esterase-like. (IPR000801); S-formylglutathione_hydrol. (IPR014186); Esterase (PF00756)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "frmC" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'frmC' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **frmC** (gene ID: frmC, UniProt: Q88MF4) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of *frmC* (PP_1617; UniProt Q88MF4) in *Pseudomonas putida* KT2440

## Summary

**frmC (locus tag PP_1617; UniProt Q88MF4) of *Pseudomonas putida* KT2440 encodes S-formylglutathione hydrolase (SFGH; EC 3.1.2.12), a cytosolic serine thioesterase/esterase of the esterase D (ESD) / α/β-hydrolase-fold family.** Its primary catalytic function is the hydrolysis of S-formylglutathione to formate and reduced glutathione (GSH): **S-formylglutathione + H₂O → formate + GSH**. This is the terminal, glutathione-regenerating step of the near-universal glutathione (GSH)-dependent formaldehyde-detoxification pathway. By releasing formate and returning GSH to the free thiol pool, FrmC completes a catalytic cycle in which GSH is used as a disposable C1-carrier cofactor rather than being consumed.

The gene's identity is unambiguous and well supported. The 284-residue protein carries the diagnostic hallmarks of this enzyme class: a GxSxG nucleophile-elbow motif (G-H-**S150**-M-G) housing the catalytic serine, a UniProt-annotated Ser150–His261–Asp228 charge-relay triad on an α/β-hydrolase fold, and InterPro/TIGRFAM signatures (IPR014186 S-formylglutathione hydrolase; IPR000801 esterase-D-like; Pfam PF00756). FrmC shares 57–62% sequence identity with the two biochemically characterized *E. coli* SFGHs (FrmB and YeiG), with its catalytic serine and histidine aligning exactly to residues that alanine-scanning mutagenesis proved to be essential. Genomically, *frmC* (PP_1617) lies immediately downstream of and co-oriented with *frmA* (PP_1616), the GSH-dependent formaldehyde dehydrogenase, separated by only 8 bp — a two-gene formaldehyde-detoxification operon that mirrors the conserved fghA/flhA arrangement in *Paracoccus denitrificans*.

Functionally, FrmC operates in the **cytoplasm** (no signal peptide or transmembrane segment; GO:0005829) and is the **sole SFGH** encoded in the KT2440 genome, making it non-redundant. Its physiological importance is heightened in this organism because *P. putida* KT2440 catabolizes lignin-derived methoxylated aromatics (e.g., vanillate), whose O-demethylation by Rieske monooxygenases liberates cytotoxic formaldehyde. FrmC clears this formaldehyde via the GSH pathway; consistent with this, adaptive laboratory evolution for improved vanillate utilization selected a mutation in the formaldehyde-detoxification (fghA/SFGH) step. The enzyme's substrate specificity — driven by a narrow acyl-binding pocket — favors S-formylglutathione and other small-acyl thioesters, with retained promiscuous short-chain carboxylesterase activity typical of the esterase D family, whose deeply conserved human ortholog is esterase D (ESD).

---

## Key Findings

### Finding 1 — frmC is S-formylglutathione hydrolase catalyzing the final step of GSH-dependent formaldehyde detoxification

UniProt Q88MF4 (frmC / PP_1617, *P. putida* KT2440, 284 aa) is annotated as **S-formylglutathione hydrolase, EC 3.1.2.12** (NCBIfam TIGR02821; RuleBase RU363068). The catalyzed reaction is:

> **S-formylglutathione + H₂O → glutathione (GSH) + formate**

Gene Ontology assignments consistently describe this activity: S-formylglutathione hydrolase activity (GO:0018738), carboxylic ester hydrolase activity (GO:0052689), and formaldehyde catabolic process (GO:0046294). InterPro (IPR014186, S-formylglutathione_hydrol; IPR000801, esterase-like/esterase D) and Pfam (PF00756) domain assignments corroborate the family placement.

This function is not merely a database inference: multiple orthologs have been biochemically characterized and shown to prefer S-formylglutathione as physiological substrate. In *E. coli*, the two SFGHs FrmB and YeiG "had the highest hydrolytic activity toward S-formylglutathione, an intermediate of the glutathione-dependent pathway of formaldehyde detoxification," with a similar affinity (Km = 0.41–0.43 mM) [PMID: 16567800]. The *Paracoccus denitrificans* ortholog FghA is part of "a formaldehyde detoxification pathway that is universal in nature" [PMID: 8892832]. The reaction and pathway position are stated directly for the plant ortholog: the enzyme "catalyses the final step of formaldehyde detoxification: the hydrolysis of S-formylglutathione to formate and glutathione" [PMID: 14646092]. Together these establish that FrmC performs the terminal, GSH-regenerating step of the pathway.

### Finding 2 — FrmC is a serine hydrolase with an α/β-hydrolase fold and a Ser150–His261–Asp228 catalytic triad

Sequence analysis of Q88MF4 identifies a **nucleophile-elbow motif G-H-S150-M-G** — the canonical GxSxG signature — placing **Ser150 as the catalytic nucleophile**. UniProt annotates a charge-relay system comprising **Ser150, Asp228, and His261**. The fold and family assignments are mutually consistent: SUPFAM SSF53474 (α/β-hydrolases), Pfam PF00756 (Esterase), InterPro IPR029058 (AB_hydrolase_fold) and IPR000801 (esterase-D-like); UniProt keyword "Serine esterase."

The catalytic mechanism is experimentally validated in orthologs. In *E. coli* YeiG, "Ser145, Asp233, and His256 are absolutely required for activity, indicating that these residues represent a serine hydrolase catalytic triad in this protein and in other S-formylglutathione hydrolases" [PMID: 16567800]. Structural and biochemical work on the Arabidopsis enzyme confirms that "AtSFGH from Arabidopsis thaliana has been shown to be a serine hydrolase rather than a cysteine hydrolase" [PMID: 16626737]. Notably, a conserved reactive cysteine near the active site (Cys57 in FrmC; cf. Cys59 in AtSFGH) "lies in close proximity to the serine hydrolase triad, serving a gate-keeping function" [PMID: 16626737], suggesting a possible redox-regulatory role for FrmC's activity. Yeast crystallography (PDB 1pv1; Ser161/His276/Asp241) further supports the conserved triad geometry.

### Finding 3 — FrmC has a narrow acyl-binding pocket giving specificity for S-formylglutathione and small acyl esters; it acts in the cytosol

Substrate specificity in this family is governed by the size of the acyl-binding pocket. The psychrophilic SFGH from *Pseudoalteromonas haloplanktis* (PhEst) "is able to efficiently hydrolyze several thioester substrates with very small acyl moieties. By contrast, the enzyme shows no activity toward substrates with bulky acyl groups… a very narrow acyl-binding pocket in a typical alpha/beta-hydrolase fold" [PMID: 20209484]. This explains the strong preference for the small **formyl** group of S-formylglutathione. Alongside the primary thioesterase activity, these enzymes retain promiscuous carboxylesterase activity: purified *E. coli* FrmB and YeiG "have high carboxylesterase activity against the model substrates, p-nitrophenyl esters of fatty acids (C2-C6) and alpha-naphthyl acetate" [PMID: 16567800], the classic esterase-D activity — but the highest activity is on S-formylglutathione.

**Localization:** Q88MF4 is a 284-aa soluble protein with no signal peptide and no transmembrane region; the GSH-dependent formaldehyde pathway operates in the bacterial cytoplasm, and the GO assignment is cytosol (GO:0005829). FrmC therefore carries out its function intracellularly, in the cytosol.

### Finding 4 — frmC (PP_1617) forms a two-gene formaldehyde-detoxification operon with frmA (PP_1616)

KEGG genome analysis of *P. putida* KT2440 places the two genes consecutively on the same strand:

| Locus | Gene | Function | KO / EC | Coordinates (strand) |
|-------|------|----------|---------|----------------------|
| PP_1616 | frmA | GSH-dependent formaldehyde dehydrogenase / S-(hydroxymethyl)glutathione dehydrogenase (class III ADH) | K00121; EC 1.1.1.284 / 1.1.1.1 | 1,812,522–1,813,637 (+) |
| PP_1617 | frmC | S-formylglutathione hydrolase | K01070; EC 3.1.2.12 | 1,813,646–1,814,500 (+) |

The **8 bp intergenic gap** and shared orientation indicate co-transcription as an operon encoding two consecutive steps of the same pathway. Immediately adjacent is PP_1615, a LysR-family transcriptional regulator (complementary strand) — a candidate regulator. Flanking genes PP_1618 (MEP-pathway IspF) and PP_1619 (tRNA pseudouridine synthase) are functionally unrelated, delimiting the operon.

This arrangement is evolutionarily conserved: in *Paracoccus denitrificans*, "Downstream of flhA, the… gene encoding glutathione-dependent formaldehyde dehydrogenase, an open reading frame was identified and called fghA" [PMID: 8892832] — exactly the frmA→frmC layout. The operon is expected to be formaldehyde-inducible, as "the expression of frmB was stimulated 45-75 times by the addition of formaldehyde to the growth medium" in *E. coli* [PMID: 16567800].

### Finding 5 — FrmC belongs to the deeply conserved esterase D family and completes a pathway whose upstream steps are spontaneous adduct formation followed by NAD⁺-dependent oxidation

SFGHs are ubiquitous across prokaryotes and eukaryotes; the human ortholog **esterase D (ESD)** is itself an S-formylglutathione hydrolase. Literature explicitly equates the two: "S-formylglutathione hydrolase (esterase D; ESD)" [PMID: 24682756], and "Esterase D (ESD) is a nonspecific esterase that detoxifies formaldehyde" [PMID: 34875997]. *Paracoccus* FghA is homologous to human esterase D [PMID: 8892832].

The complete pathway around FrmC has three steps:

1. **Spontaneous adduct formation** — "The first step in the reaction involves the nonenzymatic formation of the S-(hydroxymethyl)glutathione adduct from formaldehyde and glutathione" [PMID: 10978156].
2. **NAD⁺-dependent oxidation** — S-hydroxymethylglutathione (HMGSH) is oxidized by the GSH-dependent formaldehyde dehydrogenase / class III ADH (FrmA / PP_1616; EC 1.1.1.284) to S-formylglutathione.
3. **Hydrolysis by FrmC** — S-formylglutathione → formate + GSH.

This delineates FrmC's precise enzymatic scope: it acts only on the third step; the first step is non-enzymatic, and the second belongs to its operonic partner FrmA.

### Finding 6 — FrmC shares 57–62% identity with characterized E. coli SFGHs, with exact conservation of mutagenesis-validated catalytic residues

Global pairwise alignment of FrmC (Q88MF4, 284 aa) to characterized orthologs:

| Ortholog | UniProt | Length | % Identity | Aligned columns |
|----------|---------|--------|-----------|-----------------|
| *E. coli* YeiG (SFGH2) | P33018 | 278 aa | **61.7%** | 277 |
| *E. coli* FrmB (SFGH1) | P51025 | 277 aa | **56.7%** | 275 |

Critically, the catalytic residues map exactly: **FrmC Ser150 ↔ YeiG Ser145 / FrmB Ser145** (nucleophile); **FrmC His261 ↔ YeiG His256 / FrmB His254**; and FrmC Asp228 aligns to the conserved catalytic aspartate region. Because "Ser145, Asp233, and His256 are absolutely required for activity… in this protein and in other S-formylglutathione hydrolases" in YeiG by alanine-scanning mutagenesis [PMID: 16567800], the functional evidence transfers to FrmC by orthology. The catalytic serine sits in the GHS150MG (GxSxG) nucleophile elbow, the structural hallmark of the family.

### Finding 7 — In P. putida KT2440, frmC is the sole SFGH and clears formaldehyde released by aromatic O-demethylation

A UniProt taxonomy query (organism_id 160488) returns exactly **one** S-formylglutathione hydrolase — Q88MF4 = frmC / PP_1617 — with **no paralog**, in contrast to *E. coli*, which has two (FrmB and YeiG). FrmC is therefore non-redundant in KT2440.

The physiological relevance is amplified by this strain's lifestyle. *P. putida* KT2440 catabolizes lignin-derived methoxylated aromatics; O-demethylation of vanillate by the Rieske monooxygenase VanAB releases formaldehyde as a toxic byproduct. In adaptive laboratory evolution selecting improved vanillate utilization, one of three impactful mutations mapped to genes "including those in VanB, the reductase for vanillate O-demethylase, PP_3494, a global regulator of vanillate catabolism, and fghA, involved in formaldehyde detoxification" [PMID: 38936762]. This directly ties the SFGH step to the handling of formaldehyde generated during aromatic catabolism. In authoritative pathway terms, the GSH-dependent route is one of several cofactor-dependent linear formaldehyde-oxidation pathways involving "the spontaneous or enzyme-catalyzed condensation of formaldehyde and the respective C(1) carrier, the oxidation of the cofactor-bound C(1) unit and its conversion to formate, and the oxidation of formate to CO(2)" [PMID: 12209256].

### Finding 8 — Synthesis

Convergent evidence across all findings establishes frmC/PP_1617 as a **cytosolic serine S-formylglutathione hydrolase performing the terminal, GSH-regenerating step of glutathione-dependent formaldehyde detoxification** in *P. putida*: (1) UniProt/InterPro/TIGRFAM annotation as SFGH, EC 3.1.2.12; (2) Ser150 in a GxSxG elbow with an annotated Ser150–His261–Asp228 charge-relay triad; (3) 57–62% identity to *E. coli* SFGHs with exact catalytic-residue conservation; (4) a narrow acyl pocket conferring S-formylglutathione specificity plus secondary short-chain carboxylesterase activity; (5) cytosolic localization; (6) the frmA–frmC operon (8 bp gap); (7) sole-SFGH, non-redundant status clearing formaldehyde from aromatic O-demethylation; and (8) deep conservation to human esterase D.

---

## Mechanistic Model / Interpretation

### The glutathione-dependent formaldehyde-detoxification cycle

Formaldehyde is a reactive, cytotoxic electrophile generated endogenously (e.g., during demethylation reactions) and from environmental exposure. *P. putida* KT2440 neutralizes it through the conserved GSH-dependent pathway, in which glutathione acts as a **recyclable C1 carrier**:

```
   Formaldehyde (HCHO)
        │  + GSH   (spontaneous, non-enzymatic)
        ▼
   S-hydroxymethylglutathione (HMGSH)
        │  FrmA / PP_1616 (GSH-dependent formaldehyde dehydrogenase, class III ADH)
        │  NAD⁺ → NADH        [EC 1.1.1.284]
        ▼
   S-formylglutathione
        │  FrmC / PP_1617 (S-formylglutathione hydrolase)   ◄── THIS GENE
        │  + H₂O              [EC 3.1.2.12]
        ▼
   Formate (HCOOH)  +  GSH (regenerated → returns to pool)
        │  formate dehydrogenase (downstream, separate locus)
        ▼
   CO₂
```

FrmC catalyzes the **third and final** enzymatic step. Its output is twofold and both products matter: (i) **formate**, a far less toxic C1 species that can be further oxidized to CO₂ or assimilated, and (ii) **regenerated GSH**, which re-enters the cellular thiol pool. Because GSH is regenerated rather than consumed, the pathway is catalytic in GSH, allowing sustained detoxification of large formaldehyde fluxes with a limited GSH inventory. Failure at the FrmC step would trap glutathione as S-formylglutathione, depleting the free-GSH pool and stalling the entire pathway — explaining why the single, non-redundant SFGH is physiologically pivotal.

### Catalytic chemistry

FrmC is a classic α/β-hydrolase-fold serine hydrolase. The catalytic triad **Ser150–His261–Asp228** forms a charge-relay system: His261 (polarized by Asp228) deprotonates the Ser150 hydroxyl, which then performs nucleophilic attack on the thioester carbonyl of S-formylglutathione. A tetrahedral intermediate, stabilized by an oxyanion hole, collapses to release GSH (the thiol leaving group) and leaves a formyl-enzyme (acyl-enzyme) intermediate. A water molecule, activated by the same His, then hydrolyzes the acyl-enzyme to release formate and regenerate free enzyme.

```
   Ser150–OH  ── His261 ── Asp228     (charge-relay triad)
        │
        ▼ nucleophilic attack on C=O of  GS–C(=O)–H
   tetrahedral intermediate → GSH released + formyl–Ser150 (acyl-enzyme)
        │
        ▼ His-activated H2O
   formate released + Ser150–OH restored
```

### Substrate specificity

Specificity for the **small formyl group** arises from a **narrow acyl-binding pocket** [PMID: 20209484]. The pocket accommodates the formyl (and other very small acyl) moieties but excludes bulky acyl groups. The glutathione moiety of the substrate is recognized by a separate binding subsite. The retained ability to hydrolyze p-nitrophenyl esters of C2–C6 fatty acids and α-naphthyl acetate [PMID: 16567800] reflects the broad esterase-D ancestry of the enzyme, but S-formylglutathione is the physiological substrate. A conserved active-site cysteine (Cys57) adjacent to the triad may gate activity under oxidative conditions [PMID: 16626737], potentially coupling detoxification capacity to redox state.

### Comparison with characterized orthologs

| Property | FrmC (P. putida) | E. coli FrmB | E. coli YeiG | Arabidopsis AtSFGH | Human ESD |
|----------|------------------|--------------|--------------|--------------------|-----------|
| EC | 3.1.2.12 | 3.1.2.12 | 3.1.2.12 | 3.1.2.12 | 3.1.2.12 |
| Catalytic Ser | Ser150 | Ser145 | Ser145 | conserved | conserved |
| Catalytic His | His261 | His254 | His256 | conserved | conserved |
| Mechanism | serine hydrolase (inferred) | serine hydrolase (mutagenesis) | serine hydrolase (mutagenesis) | serine hydrolase (structure) | serine hydrolase |
| % identity to FrmC | — | 56.7% | 61.7% | family | family (ESD) |
| Km (S-formylglutathione) | not measured | 0.41–0.43 mM | 0.41–0.43 mM | — | — |
| Copies per genome | 1 (sole) | 2 (with YeiG) | 2 (with FrmB) | — | 1 |

---

## Evidence Base

| PMID | Title (abbrev.) | Relevance |
|------|-----------------|-----------|
| [16567800](https://pubmed.ncbi.nlm.nih.gov/16567800/) | *Molecular basis of formaldehyde detoxification: two SFGHs from E. coli, FrmB and YeiG* | **Cornerstone.** Establishes S-formylglutathione as preferred substrate (Km 0.41–0.43 mM); alanine-scanning proves Ser/Asp/His triad essential; shows short-chain carboxylesterase side-activity; documents 45–75× formaldehyde induction. FrmC aligns 57–62% with exact catalytic-residue conservation. |
| [8892832](https://pubmed.ncbi.nlm.nih.gov/8892832/) | *SFGH of P. denitrificans is homologous to human esterase D* | Defines the universal formaldehyde-detox pathway; documents the conserved fghA-downstream-of-dehydrogenase gene arrangement mirrored by frmA–frmC; links family to human ESD. |
| [16626737](https://pubmed.ncbi.nlm.nih.gov/16626737/) | *Unique regulation of the active site of the serine esterase SFGH* | Confirms serine-hydrolase (not cysteine) mechanism; identifies the conserved active-site cysteine as a gate-keeper (Cys57 in FrmC). |
| [14646092](https://pubmed.ncbi.nlm.nih.gov/14646092/) | *X-ray analysis of Arabidopsis SFGH* | States the reaction directly: hydrolysis of S-formylglutathione to formate and glutathione as the final detox step. |
| [20209484](https://pubmed.ncbi.nlm.nih.gov/20209484/) | *Crystal structure of SFGH from P. haloplanktis* | Documents the narrow acyl-binding pocket and small-acyl thioester specificity underlying formyl selectivity. |
| [10978156](https://pubmed.ncbi.nlm.nih.gov/10978156/) | *Kinetic mechanism of GSH-dependent formaldehyde dehydrogenase* | Establishes that the upstream HMGSH adduct forms spontaneously, delimiting FrmC's enzymatic scope. |
| [38936762](https://pubmed.ncbi.nlm.nih.gov/38936762/) | *Evolution and engineering of aromatic O-demethylation in P. putida KT2440* | Connects the KT2440 formaldehyde-detox (fghA/SFGH) step to formaldehyde produced during aromatic O-demethylation; ALE selected a mutation here. |
| [12209256](https://pubmed.ncbi.nlm.nih.gov/12209256/) | *Cofactor-dependent pathways of formaldehyde oxidation in methylotrophs (review)* | Authoritative placement of the GSH-dependent SFGH step within linear C1-carrier oxidation to formate/CO₂. |
| [24682756](https://pubmed.ncbi.nlm.nih.gov/24682756/) | *Bioactivating enzymes: laninamivir octanoate hydrolysis* | Explicitly equates SFGH with esterase D (ESD), confirming the human ortholog. |
| [34875997](https://pubmed.ncbi.nlm.nih.gov/34875997/) | *Esterase D stabilizes FKBP25 to suppress mTORC1* | Confirms ESD as a formaldehyde-detoxifying nonspecific esterase, the conserved eukaryotic ortholog. |

Supporting/context papers reviewed: yeast SFGH ([PMID: 10427036](https://pubmed.ncbi.nlm.nih.gov/10427036/)); class III ADH / FDH structure–function ([PMID: 12604204](https://pubmed.ncbi.nlm.nih.gov/12604204/), [PMID: 16605250](https://pubmed.ncbi.nlm.nih.gov/16605250/)); GSNO/HMGSH kinetics ([PMID: 18412547](https://pubmed.ncbi.nlm.nih.gov/18412547/), [PMID: 22335564](https://pubmed.ncbi.nlm.nih.gov/22335564/)); lignin/aromatic valorization and formaldehyde toxicity ([PMID: 41024182](https://pubmed.ncbi.nlm.nih.gov/41024182/), [PMID: 40741777](https://pubmed.ncbi.nlm.nih.gov/40741777/)); and ESD in mammalian physiology ([PMID: 33615471](https://pubmed.ncbi.nlm.nih.gov/33615471/), [PMID: 32247735](https://pubmed.ncbi.nlm.nih.gov/32247735/), [PMID: 27267271](https://pubmed.ncbi.nlm.nih.gov/27267271/), [PMID: 35627173](https://pubmed.ncbi.nlm.nih.gov/35627173/)).

No literature was found describing a *different* gene under the symbol "frmC" that would conflict with this assignment; the symbol, organism, protein family, and domain architecture all align consistently with S-formylglutathione hydrolase.

---

## Limitations and Knowledge Gaps

1. **No direct biochemical characterization of FrmC itself.** All kinetic parameters (Km, kcat, substrate range) and mechanistic conclusions are transferred by orthology from *E. coli* FrmB/YeiG, plant, yeast, and marine-bacterial enzymes. FrmC's own catalytic constants, pH/temperature optima, and precise substrate profile have not been measured experimentally.

2. **Catalytic triad is predicted, not experimentally validated in FrmC.** Ser150/His261/Asp228 are inferred from motif analysis, UniProt annotation, and exact alignment to mutagenesis-validated *E. coli* residues. No site-directed mutagenesis or structure of FrmC has confirmed the triad in this specific protein.

3. **No experimental structure.** No crystal structure or AlphaFold-validated model of FrmC was analyzed here; the α/β-hydrolase fold and narrow acyl pocket are inferred from homologs.

4. **Operon/regulation inferred from genomic context.** The frmA–frmC operon (8 bp gap) and the LysR regulator (PP_1615) are computational predictions; co-transcription, the transcription start site, and formaldehyde inducibility in KT2440 have not been directly demonstrated (the 45–75× induction figure is from *E. coli* frmB).

5. **Redox gate-keeping role of Cys57 is speculative.** Extrapolated from the Arabidopsis Cys59 finding; its functional relevance in FrmC is untested.

6. **Physiological knockout phenotype not directly established.** The ALE evidence linking the SFGH/fghA step to vanillate/formaldehyde handling is suggestive but does not equate to a clean *frmC* deletion phenotype in KT2440.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant enzymology.** Express and purify His-tagged FrmC and measure steady-state kinetics on S-formylglutathione (Km, kcat, kcat/Km) and on a panel of p-nitrophenyl esters (C2–C8) and α-naphthyl acetate to define the substrate spectrum and confirm the narrow-acyl-pocket prediction.

2. **Site-directed mutagenesis.** Generate S150A, H261A, and D228A variants and confirm loss of activity, directly validating the catalytic triad in FrmC. Test C57A/C57S to probe the proposed redox gate-keeping function and sensitivity to oxidants (e.g., H₂O₂, diamide).

3. **Structural determination.** Solve the crystal structure (or generate and validate an AlphaFold model with PAE/pLDDT analysis) of FrmC, ideally with a substrate analog or product (GSH) bound, to confirm the fold, triad geometry, and acyl-pocket dimensions.

4. **Genetic knockout and complementation.** Construct a clean ΔPP_1617 mutant and assay formaldehyde sensitivity and growth on vanillate/methoxylated aromatics; complement to confirm causality. Test whether S-formylglutathione accumulates and free GSH is depleted in the mutant.

5. **Operon and regulation.** Use RT-PCR / RNA-seq to demonstrate frmA–frmC co-transcription and formaldehyde inducibility, and test whether the adjacent LysR regulator (PP_1615) controls the operon (EMSA, reporter fusions).

6. **Metabolic-engineering relevance.** In strains engineered for lignin-aromatic valorization, quantify how frmC expression level affects formaldehyde tolerance, growth rate, and product yield during vanillate/syringate O-demethylation, informing whether FrmC is a bottleneck to be over-expressed.

---

*Report generated from an 8-finding, 26-paper, 5-iteration autonomous investigation. All functional claims are supported by verified citation snippets from the primary and review literature listed above; where evidence is by orthology rather than direct measurement, this is stated explicitly.*


## Artifacts

- [OpenScientist final report](frmC-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](frmC-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:16567800
2. PMID:8892832
3. PMID:14646092
4. PMID:16626737
5. PMID:20209484
6. PMID:24682756
7. PMID:34875997
8. PMID:10978156
9. PMID:38936762
10. PMID:12209256
11. PMID:10427036
12. PMID:12604204
13. PMID:16605250
14. PMID:18412547
15. PMID:22335564
16. PMID:41024182
17. PMID:40741777
18. PMID:33615471
19. PMID:32247735
20. PMID:27267271
21. PMID:35627173