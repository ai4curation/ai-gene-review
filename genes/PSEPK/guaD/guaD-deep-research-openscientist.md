---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-19T08:48:07.276102'
end_time: '2026-08-19T09:00:24.263919'
duration_seconds: 736.99
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: guaD
  gene_symbol: guaD
  uniprot_accession: Q88F18
  protein_description: 'RecName: Full=Guanine deaminase {ECO:0000256|ARBA:ARBA00012781,
    ECO:0000256|NCBIfam:TIGR02967}; Short=Guanase {ECO:0000256|RuleBase:RU366009};
    EC=3.5.4.3 {ECO:0000256|ARBA:ARBA00012781, ECO:0000256|NCBIfam:TIGR02967}; AltName:
    Full=Guanine aminohydrolase {ECO:0000256|RuleBase:RU366009};'
  gene_info: Name=guaD {ECO:0000313|EMBL:AAN69861.1}; OrderedLocusNames=PP_4281 {ECO:0000313|EMBL:AAN69861.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the metallo-dependent hydrolases superfamily.
  protein_domains: Amidohydro-rel. (IPR006680); Guanine_deaminase. (IPR014311); Metal-dep_hydrolase_composite.
    (IPR011059); Metal_Hydrolase. (IPR032466); Metallo-dep_hydrolases. (IPR051607)
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
citation_count: 8
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: guaD-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: guaD-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88F18
- **Protein Description:** RecName: Full=Guanine deaminase {ECO:0000256|ARBA:ARBA00012781, ECO:0000256|NCBIfam:TIGR02967}; Short=Guanase {ECO:0000256|RuleBase:RU366009}; EC=3.5.4.3 {ECO:0000256|ARBA:ARBA00012781, ECO:0000256|NCBIfam:TIGR02967}; AltName: Full=Guanine aminohydrolase {ECO:0000256|RuleBase:RU366009};
- **Gene Information:** Name=guaD {ECO:0000313|EMBL:AAN69861.1}; OrderedLocusNames=PP_4281 {ECO:0000313|EMBL:AAN69861.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the metallo-dependent hydrolases superfamily.
- **Key Domains:** Amidohydro-rel. (IPR006680); Guanine_deaminase. (IPR014311); Metal-dep_hydrolase_composite. (IPR011059); Metal_Hydrolase. (IPR032466); Metallo-dep_hydrolases. (IPR051607)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "guaD" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'guaD' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **guaD** (gene ID: guaD, UniProt: Q88F18) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of *guaD* (PP_4281 / UniProt Q88F18): Guanine Deaminase of *Pseudomonas putida* KT2440

**Gene:** guaD (ordered locus PP_4281) · **UniProt:** Q88F18 · **EC:** 3.5.4.3
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / NCIMB 11950 / KT2440)
**Protein length:** 434 aa · **Cofactor:** Zn²⁺ · **Family:** metallo-dependent hydrolases superfamily, ATZ/TRZ (amidohydrolase) family; Pfam PF01979

## Summary

The gene **guaD** (ordered locus **PP_4281**; UniProt **Q88F18**) of *Pseudomonas putida* strain KT2440 encodes **guanine deaminase** (guanase; EC 3.5.4.3), a **Zn²⁺-dependent metallo-hydrolase** that catalyzes the hydrolytic deamination of the free purine base **guanine to xanthine plus ammonia** (guanine + H₂O + H⁺ → xanthine + NH₄⁺; Rhea RHEA:14665). This is the enzyme's primary and committed physiological reaction, and it constitutes the single "guanine → xanthine" step (UniPathway UPA00603) that funnels guanine into the bacterial purine-catabolic pathway. The gene symbol *guaD* is **unambiguous and correct** for this protein: the annotated reaction, protein family, catalytic residues, organism, and genomic context all align consistently, so this report proceeds with confidence on the intended target.

At the molecular level, Q88F18 is a **~434-residue member of the amidohydrolase (ATZ/TRZ) superfamily** (Pfam PF01979 Amidohydro_1; InterPro IPR006680, IPR014311, IPR011059, IPR032466). It adopts the (β/α)₈ TIM-barrel fold characteristic of this superfamily and coordinates a single catalytic **zinc ion** through a conserved **His-His-His-Asp** ligand set (His78, His80, His233, Asp323 in the KT2440 numbering), which sequence-motif analysis mapped one-to-one onto the experimentally defined metal sites of orthologous guanine deaminases from *E. coli* and human. This places Q88F18 firmly in the "large" amidohydrolase-type guanine deaminase class, distinct from the smaller cytidine-deaminase-superfamily guanine deaminases (e.g., that of *Bacillus subtilis*).

Physiologically, guanine deaminase performs the **committed entry step of purine-base catabolism** in the cytoplasm. Its product, xanthine, is oxidized by an adjacent **xanthine dehydrogenase** and processed through urate and allantoin, allowing the cell to reclaim the purine ring's nitrogen for assimilation. Consistent with this role, *guaD* orthologs are transcriptionally controlled by **nitrogen availability** (via NtrC), and in KT2440 the gene sits in a dedicated chromosomal **purine-degradation island** immediately next to the xanthine dehydrogenase genes and downstream urate/allantoin-degrading enzymes. Notably, KT2440 guanine deaminase also exhibits a **promiscuous ammeline-deaminase activity**, linking this housekeeping purine enzyme to the environmentally important bacterial degradation of s-triazine compounds (melamine/atrazine metabolites).

---

## Key Findings

### Finding 1 — Primary function: guanine deaminase, guanine → xanthine + NH₃ (EC 3.5.4.3)

The primary and defining function of Q88F18 is the **hydrolytic deamination of guanine to xanthine**, releasing ammonia. UniProt annotates the reaction explicitly as guanine + H₂O + H⁺ = xanthine + NH₄⁺ (Rhea RHEA:14665; EC 3.5.4.3), assigned to the pathway "Purine metabolism; guanine degradation; xanthine from guanine, step 1/1" (UniPathway UPA00603). The protein is 434 amino acids, encoded by *guaD* / ordered locus PP_4281 (KEGG ppu:PP_4281, KO K01487).

This assignment is strongly supported by the biochemical literature, which uniformly defines guanine deaminase by exactly this reaction. As stated by Liaw and colleagues, *"Guanine deaminase, a key enzyme in the nucleotide metabolism, catalyzes the hydrolytic deamination of guanine into xanthine"* [PMID: 15180998](https://pubmed.ncbi.nlm.nih.gov/15180998/). The reaction's role in feeding downstream purine oxidation is likewise well documented: *"Guanine deaminase (GD) catalyzes the conversion of guanine to xanthine, providing substrate for downstream oxidation by XO"* [PMID: 42203193](https://pubmed.ncbi.nlm.nih.gov/42203193/). Because the deamination of guanine to xanthine is the universally conserved, class-defining activity of this enzyme, the functional annotation of Q88F18 as guanine deaminase can be made with very high confidence.

### Finding 2 — Q88F18 is a Zn²⁺-dependent amidohydrolase-superfamily enzyme (ATZ/TRZ family)

Q88F18 belongs to the **metallo-dependent hydrolases superfamily, ATZ/TRZ (amidohydrolase) family**. UniProt lists a **Zn(2+) cofactor**, and the domain architecture — Pfam PF01979 (Amidohydro_1); InterPro IPR006680 (Amidohydro-rel), IPR014311 (Guanine deaminase, TIGR02967), and IPR011059/IPR032466 (metal-dependent hydrolase) — is diagnostic of the (β/α)₈ TIM-barrel amidohydrolase fold. At 434 residues, Q88F18 is the **large, amidohydrolase-type guanine deaminase**, which is mechanistically and evolutionarily distinct from the small (~156-aa) cytidine-deaminase-superfamily guanine deaminases.

The closest biochemically characterized relative of this type is **NE0047 from *Nitrosomonas europaea***, a zinc-dependent guanine deaminase with a catalytic efficiency of kcat/KM = 1.2 × 10⁵ M⁻¹ s⁻¹. Bitra and colleagues confirmed that *"NE0047 from Nitrosomonas europaea has been annotated as a zinc-dependent deaminase"* and demonstrated that *"the extreme nine-amino acid C-terminal loop forms an active site flap"* that gates the active site during catalysis [PMID: 23557066](https://pubmed.ncbi.nlm.nih.gov/23557066/). These features — a mononuclear catalytic zinc and a C-terminal active-site flap — are hallmarks of the amidohydrolase-type guanine deaminase family to which Q88F18 belongs, supporting both its cofactor requirement and its catalytic architecture.

### Finding 3 — Q88F18 conserves the canonical mononuclear-Zn active site (His78/His80/His233/Asp323)

Direct sequence-motif analysis of the 434-residue Q88F18 sequence identified the **complete, canonical amidohydrolase metal-binding set**. The diagnostic β1 metal-binding motif **D-T-H-I-H** (residues 76–80) supplies the His-x-His zinc-ligand pair **His78/His80**; a second conserved **M-H-T-H** element (residues ~229–233) supplies the third histidine ligand (**His233**); and the β6 **G-T-D-V-G** motif (residues 321–325) supplies the zinc-ligating aspartate **Asp323**.

Critically, these four positions align one-to-one with the experimentally annotated Zn²⁺ ligands of characterized orthologs: *E. coli* GuaD (P76641) His82/His84/His237/Asp327, and human GDA/cypin (Q9Y2T3) His82/His84/His240/Asp330. Substrate-binding residues conserved in the orthologs (e.g., *E. coli* His209; human His213) are likewise present in the equivalent region of Q88F18. The perfect correspondence of the entire His/His/His/Asp catalytic constellation — not merely overall sequence similarity — provides strong structural-bioinformatic evidence that Q88F18 is a **catalytically competent guanine deaminase**, not a degenerate or misannotated family member. This finding is consistent with the demonstration that this enzyme family coordinates a catalytic zinc [PMID: 23557066](https://pubmed.ncbi.nlm.nih.gov/23557066/).

### Finding 4 — Pathway role: committed entry step of purine-ring catabolism for nitrogen assimilation

Guanine deaminase initiates the **catabolic degradation of the guanine purine ring**, enabling purines to serve as a nitrogen (and, in some organisms, carbon) source. In *Pseudomonas aeruginosa*, the purine-degradation pathway was genetically defined to comprise adenine deaminase (puuA), **guanine deaminase (puuB)**, xanthine dehydrogenase (puuC), uricase (puuD), allantoinase (puuE), and allantoicase (puuF). The classic mutant study established this ordered set: *"Mutants that are deficient in adenine deaminase (puuA), guanine deaminase (puuB), xanthine dehydrogenase (puuC), uricase (puuD), allantoinase (puuE), and/or allantoicase (puuF) were isolated"* [PMID: 104142](https://pubmed.ncbi.nlm.nih.gov/104142/). This places guanine deaminase as the **guanine-entry step** in *Pseudomonas* purine catabolism, and the *P. putida* KT2440 *guaD* is the direct ortholog occupying that position.

The pathway's physiological purpose — nitrogen assimilation — is reflected in its regulation. In *Klebsiella pneumoniae*, guanine deaminase activity is embedded in an allantoin/purine assimilation gene cluster, and its expression is controlled by the global nitrogen regulator NtrC: *"Expression of guaD is mainly regulated by nitrogen availability through the action of NtrC"* [PMID: 21357483](https://pubmed.ncbi.nlm.nih.gov/21357483/). This nitrogen-responsive control demonstrates that guaD functions physiologically in purine-nitrogen scavenging, consistent with KT2440 encoding the full downstream machinery (xanthine dehydrogenase, urate oxidation, allantoin degradation) needed to route xanthine onward toward assimilable nitrogen.

### Finding 5 — Genomic context in KT2440: guaD lies within a purine-catabolism gene island next to xanthine dehydrogenase

KEGG genomic-context analysis of ppu:PP_4281 (chromosomal position 4,871,626–4,872,930; KO K01487; EC 3.5.4.3; module M00959 "Guanine ribonucleotide degradation, GMP ⇒ Urate"; pathway ppu00230 Purine metabolism) shows that *guaD* sits within a **contiguous purine-degradation island**. Its immediate neighbors form a functionally coherent cluster:

| Locus | Product | Role relative to guaD |
|-------|---------|----------------------|
| PP_4277 | GntR-family regulator | Candidate transcriptional regulator |
| PP_4278 | Xanthine dehydrogenase subunit XdhA | Consumes guaD product (xanthine) |
| PP_4279 | Xanthine dehydrogenase subunit XdhB | Consumes guaD product |
| PP_4280 | Xanthine dehydrogenase accessory factor | Adjacent, directly upstream |
| **PP_4281** | **Guanine deaminase (guaD)** | **Guanine → xanthine (this study)** |
| PP_4283 | GntR-family regulator | Candidate transcriptional regulator |
| PP_4284 | Putative purine transporter | Substrate uptake |
| PP_4285 | 5-hydroxyisourate hydrolase | Downstream (urate branch) |
| PP_4286 | Allantoinase | Downstream (allantoin branch) |

The physical co-localization of guaD with the very enzyme (xanthine dehydrogenase) that consumes its product, together with downstream urate- and allantoin-degrading enzymes, a candidate purine transporter, and GntR-family regulators, strongly corroborates guaD's assigned pathway position. This mirrors the ordered *Pseudomonas* purine pathway (guanine deaminase → xanthine dehydrogenase → … → allantoinase) defined genetically in *P. aeruginosa* [PMID: 104142](https://pubmed.ncbi.nlm.nih.gov/104142/). Analogous multi-gene purine-utilization clusters, including guanine deaminase and homologs noted in *Pseudomonas*, have also been described in *Klebsiella oxytoca* [PMID: 19060149](https://pubmed.ncbi.nlm.nih.gov/19060149/).

### Finding 6 — Promiscuous ammeline-deaminase activity links KT2440 guanine deaminase to s-triazine metabolism

Beyond its canonical purine role, KT2440 guanine deaminase exhibits a documented **secondary (promiscuous) ammeline-deaminase activity**. Seffernick and colleagues demonstrated the ammeline-deamination phenotype directly in wild-type *P. putida* KT2440 (and *E. coli* K12) and identified guanine deaminase as the responsible enzyme — an *E. coli* guaD deletion abolished the activity. The authors report: *"The ammeline degradation phenotype was demonstrated in wild-type Escherichia coli and Pseudomonas strains, including E. coli K12 and Pseudomonas putida KT2440"* and that *"Bioinformatics analysis of these and other genomes led to the hypothesis that the ammeline deaminating enzyme was guanine deaminase"* [PMID: 20023034](https://pubmed.ncbi.nlm.nih.gov/20023034/).

This promiscuity is mechanistically sensible: ammeline (a hydroxy-s-triazine) docks in the guanine-deaminase active site much like guanine, and the amidohydrolase superfamily is evolutionarily related to the s-triazine (atrazine/melamine) hydrolases. Indeed, recent work traces the atrazine-degradation enzyme AtzB to an amidohydrolase progenitor with guanine deaminase (GuaD) activity, underscoring the deep functional overlap between guanine deaminases and s-triazine hydrolases [PMID: 41953217](https://pubmed.ncbi.nlm.nih.gov/41953217/). This link is biologically relevant because it connects a conserved housekeeping purine enzyme to the biodegradation of environmental s-triazine pollutants — a role of particular interest in the environmentally versatile *P. putida*.

---

## Mechanistic Model / Interpretation

Integrating the six findings yields a coherent mechanistic picture of Q88F18 as the **cytoplasmic, zinc-dependent gatekeeper of guanine catabolism** in *P. putida* KT2440.

**Catalytic mechanism.** Q88F18 adopts the (β/α)₈ TIM-barrel amidohydrolase fold and coordinates a single catalytic Zn²⁺ ion via His78, His80, His233, and Asp323. In the canonical amidohydrolase mechanism, the active-site zinc polarizes and deprotonates a water molecule to generate a zinc-bound hydroxide nucleophile; this hydroxide attacks C2 of the guanine ring, and the conserved aspartate acts as a general acid/base to shuttle protons, culminating in loss of ammonia and formation of xanthine. A mobile C-terminal loop (the "active-site flap," as characterized in the NE0047 ortholog) is expected to close over the bound substrate to sequester it from bulk solvent during catalysis.

**Pathway flux.** The reaction sits at a committed branch point of purine-base catabolism:

```
                 guanine
                    │  guaD / PP_4281 (Q88F18)   [Zn²⁺; His78/His80/His233/Asp323]
                    │  guanine + H2O + H+ → xanthine + NH4+
                    ▼
                 xanthine ──── (also produced from hypoxanthine / adenine branch)
                    │  xanthine dehydrogenase (PP_4278/4279/4280, XdhAB + accessory)
                    ▼
                  urate
                    │  urate oxidation (PP_4285 5-hydroxyisourate hydrolase, etc.)
                    ▼
                allantoin
                    │  allantoinase (PP_4286) → allantoate → …
                    ▼
        released NH3 / carbon skeletons → nitrogen (and carbon) assimilation
```

The genomic clustering (Finding 5) is the physical embodiment of this metabolic logic: guaD is transcribed within an island containing its immediate downstream consumer (xanthine dehydrogenase), further ring-opening enzymes, a putative purine importer, and local GntR regulators. The ammonia released by guaD, together with the nitrogen liberated during downstream ring cleavage, is the ultimate physiological payoff — which is why guaD expression is coupled to global nitrogen status through NtrC in related bacteria (Finding 4).

**Two faces of one active site.** The same active-site geometry that recognizes guanine also accommodates the structurally similar hydroxy-s-triazine ammeline (Finding 6). This is not a separate enzyme but a promiscuous side-activity of guanine deaminase, and it exemplifies how the amidohydrolase superfamily serves as an evolutionary reservoir from which novel xenobiotic-degrading activities (e.g., atrazine/melamine hydrolysis) can emerge.

**Localization.** All available evidence indicates guaD operates as a **soluble, cytoplasmic** enzyme. It has no signal peptide or transmembrane annotation, its substrate (free guanine) and partners (xanthine dehydrogenase, purine transporter) are cytoplasmic, and its family members are characterized as soluble proteins. This localization is inferred from family/domain architecture and genomic context rather than from direct KT2440 experimental data.

| Attribute | Assignment | Basis |
|-----------|-----------|-------|
| Reaction | guanine + H₂O + H⁺ → xanthine + NH₄⁺ | UniProt/Rhea; EC 3.5.4.3 |
| Substrate specificity | Guanine (primary); ammeline (promiscuous) | Family conservation; KT2440 phenotype |
| Cofactor | Mononuclear Zn²⁺ | His78/His80/His233/Asp323 conserved |
| Fold/family | (β/α)₈ TIM-barrel amidohydrolase (ATZ/TRZ) | Pfam PF01979; InterPro |
| Pathway | Purine catabolism, guanine-entry step | UniPathway UPA00603; KEGG M00959 |
| Localization | Cytoplasm (inferred) | No signal/TM; soluble family |
| Regulation | Nitrogen availability (NtrC in orthologs) | K. pneumoniae guaD |

---

## Evidence Base

| PMID | Study | How it supports the annotation |
|------|-------|-------------------------------|
| [15180998](https://pubmed.ncbi.nlm.nih.gov/15180998/) | *Crystal structure of B. subtilis guanine deaminase* | Defines the class reaction: hydrolytic deamination of guanine to xanthine (EC 3.5.4.3). Note: the B. subtilis enzyme is the small cytidine-deaminase-superfamily type, contrasting with Q88F18's amidohydrolase type. |
| [42203193](https://pubmed.ncbi.nlm.nih.gov/42203193/) | *Purine analog antivirals and serum uric acid* | Confirms guanine deaminase converts guanine to xanthine, feeding downstream oxidation. |
| [23557066](https://pubmed.ncbi.nlm.nih.gov/23557066/) | *Guanine deaminase from N. europaea (NE0047)* | Characterizes the amidohydrolase-type, zinc-dependent guanine deaminase most similar to Q88F18; defines the C-terminal active-site flap and catalytic zinc. |
| [21357483](https://pubmed.ncbi.nlm.nih.gov/21357483/) | *Regulation of allantoinase/guanine deaminase cluster in K. pneumoniae* | Shows guaD expression is nitrogen-regulated via NtrC, establishing the physiological purine-nitrogen-assimilation role. |
| [104142](https://pubmed.ncbi.nlm.nih.gov/104142/) | *Chromosomal location of genes for purine degradation in P. aeruginosa* | Genetically defines the ordered Pseudomonas purine pathway placing guanine deaminase (puuB) as the guanine-entry step. |
| [20023034](https://pubmed.ncbi.nlm.nih.gov/20023034/) | *Bacterial ammeline metabolism via guanine deaminase* | Directly demonstrates ammeline-deaminase activity in P. putida KT2440 and attributes it to guanine deaminase. |
| [41953217](https://pubmed.ncbi.nlm.nih.gov/41953217/) | *Discovery of AtzB evolving from a GuaD-like progenitor* | Documents the evolutionary link between guanine deaminase and s-triazine hydrolases, contextualizing the ammeline promiscuity. |
| [19060149](https://pubmed.ncbi.nlm.nih.gov/19060149/) | *Purine utilization by K. oxytoca* | Independent purine-catabolism gene cluster (including guanine deaminase) with homologs noted in Pseudomonas, supporting pathway conservation. |

**Consistency of the annotation.** Every independent line of evidence — the annotated reaction and pathway (UniProt/Rhea/KEGG), the domain architecture (Pfam/InterPro), the conserved His/His/His/Asp zinc site mapped onto experimentally validated orthologs, the genomic co-localization with xanthine dehydrogenase, the nitrogen-responsive regulation of guaD orthologs, and the experimentally observed ammeline activity in KT2440 itself — converges on the same conclusion. The gene symbol *guaD* is therefore **correct and unambiguous** for Q88F18; there is no evidence of a same-symbol conflict in a different organism, and all cited literature pertains to genuine guanine deaminases.

---

## Limitations and Knowledge Gaps

1. **No direct enzymology on the KT2440 protein.** There are, to our knowledge, no purified-enzyme kinetic parameters (kcat, KM, kcat/KM for guanine, metal-dependence assays) for Q88F18 specifically. The functional assignment rests on strong homology, conserved catalytic residues, and pathway/genomic context rather than direct biochemical characterization of this exact protein.

2. **Localization is inferred, not measured.** Cytoplasmic localization is deduced from the absence of signal/transmembrane features and from the soluble nature of characterized family members, not from experimental fractionation or imaging in KT2440.

3. **Catalytic residues assigned by sequence-motif alignment.** The His78/His80/His233/Asp323 zinc ligands were identified by motif analysis and cross-referenced to orthologs; no experimental crystal structure or site-directed mutagenesis of Q88F18 confirms these positions directly. An AlphaFold model or crystal structure would strengthen this.

4. **Substrate-specificity breadth untested for Q88F18.** While the ammeline promiscuity is documented for KT2440 as an organism, the quantitative substrate profile of the specific PP_4281 gene product (e.g., activity on 8-azaguanine, other purine analogs, or s-triazines) has not been directly measured.

5. **Regulatory model borrowed from orthologs.** NtrC/nitrogen control of guaD is established in *K. pneumoniae*; the specific regulators for PP_4281 (the neighboring GntR-family proteins PP_4277/PP_4283) and the actual transcriptional response in KT2440 remain to be experimentally verified.

6. **Downstream xanthine dehydrogenase is not the sole guanine sink.** Xanthine can also arise from hypoxanthine/adenine branches, so the quantitative contribution of guaD to purine-nitrogen assimilation under different conditions is not resolved.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant enzymology.** Clone, express, and purify Q88F18 (His-tagged) and determine steady-state kinetics for guanine (kcat, KM, kcat/KM), confirm Zn²⁺ dependence (metal-chelation and reconstitution), and test a substrate panel — 8-azaguanine, ammeline, ammelide, melamine, and other purine analogs — to quantify the primary vs. promiscuous activities.

2. **Structure determination / modeling.** Solve a crystal structure (ideally with bound substrate/product or a transition-state analog such as iso-azepinomycin, [PMID: 23891230](https://pubmed.ncbi.nlm.nih.gov/23891230/)) or, at minimum, build and analyze an AlphaFold model to validate the His78/His80/His233/Asp323 zinc site and the C-terminal active-site flap geometry.

3. **Site-directed mutagenesis.** Individually mutate His78, His80, His233, and Asp323 to confirm their roles as zinc ligands and their essentiality for catalysis.

4. **Genetic phenotyping in KT2440.** Construct a clean PP_4281 deletion and test growth on guanine as sole nitrogen source; complement to confirm; and assess loss of ammeline-deaminase activity to link PP_4281 directly to the KT2440 ammeline phenotype.

5. **Localization confirmation.** Perform cell fractionation and/or fluorescent-fusion imaging to confirm cytoplasmic localization.

6. **Regulatory dissection.** Use transcriptional reporters and knockouts of the neighboring GntR-family regulators (PP_4277, PP_4283) and nitrogen-regulatory genes to define how PP_4281 expression responds to nitrogen source and purine availability in KT2440.

7. **Pathway flux analysis.** Employ ¹⁵N-labeled guanine tracing to quantify guaD's contribution to nitrogen assimilation and confirm channeling of xanthine to the adjacent xanthine dehydrogenase.

---

*Report generated from 3 completed investigation iterations, 6 confirmed findings, and 26 reviewed papers. All functional claims are grounded in cited primary literature or database annotations as indicated.*


## Artifacts

- [OpenScientist final report](guaD-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](guaD-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:15180998
2. PMID:42203193
3. PMID:23557066
4. PMID:21357483
5. PMID:19060149
6. PMID:20023034
7. PMID:41953217
8. PMID:23891230