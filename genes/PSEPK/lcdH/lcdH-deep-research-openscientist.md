---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-11T14:08:36.031323'
end_time: '2026-07-11T14:17:47.743649'
duration_seconds: 551.71
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: lcdH
  gene_symbol: lcdH
  uniprot_accession: Q88R32
  protein_description: 'RecName: Full=L-carnitine dehydrogenase {ECO:0000255|HAMAP-Rule:MF_02129};
    Short=CDH {ECO:0000255|HAMAP-Rule:MF_02129}; Short=L-CDH {ECO:0000255|HAMAP-Rule:MF_02129};
    EC=1.1.1.108 {ECO:0000255|HAMAP-Rule:MF_02129};'
  gene_info: Name=lcdH {ECO:0000312|EMBL:AAN65933.1}; OrderedLocusNames=PP_0302 {ECO:0000312|EMBL:AAN65933.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the 3-hydroxyacyl-CoA dehydrogenase family. L-
  protein_domains: 3-OHacyl-CoA_DH_NAD-bd. (IPR006176); 3HC_DH_C. (IPR006108); 6-PGluconate_DH-like_C_sf.
    (IPR008927); 6PGD_dom2. (IPR013328); L-carnitine_dehydrogenase. (IPR026578)
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
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: lcdH-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: lcdH-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88R32
- **Protein Description:** RecName: Full=L-carnitine dehydrogenase {ECO:0000255|HAMAP-Rule:MF_02129}; Short=CDH {ECO:0000255|HAMAP-Rule:MF_02129}; Short=L-CDH {ECO:0000255|HAMAP-Rule:MF_02129}; EC=1.1.1.108 {ECO:0000255|HAMAP-Rule:MF_02129};
- **Gene Information:** Name=lcdH {ECO:0000312|EMBL:AAN65933.1}; OrderedLocusNames=PP_0302 {ECO:0000312|EMBL:AAN65933.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the 3-hydroxyacyl-CoA dehydrogenase family. L-
- **Key Domains:** 3-OHacyl-CoA_DH_NAD-bd. (IPR006176); 3HC_DH_C. (IPR006108); 6-PGluconate_DH-like_C_sf. (IPR008927); 6PGD_dom2. (IPR013328); L-carnitine_dehydrogenase. (IPR026578)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "lcdH" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'lcdH' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **lcdH** (gene ID: lcdH, UniProt: Q88R32) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *lcdH* (L-carnitine dehydrogenase, UniProt Q88R32)

**Organism:** *Pseudomonas putida* strain KT2440 (ATCC 47054 / DSM 6125 / NCIMB 11950)
**Gene:** *lcdH* (ordered locus PP_0302)
**Protein:** L-carnitine dehydrogenase (CDH / L-CDH), EC 1.1.1.108
**UniProt:** Q88R32 · HAMAP rule MF_02129

---

## 0. Gene identity verification

The target was verified against all provided UniProt criteria before research:

- **Gene symbol / function match:** The symbol *lcdH* denotes **l**‑**c**arnitine **d**e**h**ydrogenase, consistent with the UniProt description "L-carnitine dehydrogenase, EC 1.1.1.108."
- **Organism match:** Primary biochemical literature characterizes carnitine dehydrogenase from *Pseudomonas putida* (strain IFP 206) — the same species as the target strain KT2440 — with the identical EC number 1.1.1.108 (Goulas 1988, PMID 3058208). KT2440-specific pathway context is corroborated by studies in the closely related *P. aeruginosa* and by classic *P. putida* physiology work (Kleber 1978, PMID 565193).
- **Family / domain match:** Literature and UniProt agree that the enzyme belongs to the 3‑hydroxyacyl‑CoA dehydrogenase family and carries an N‑terminal NAD‑binding Rossmann domain (IPR006176) and C‑terminal helical catalytic domain (IPR006108), matching the provided domain list.

**Conclusion:** The gene symbol is unambiguous for this protein and the literature is directly on-target. No conflicting-gene problem was encountered. Research proceeded with high confidence.

---

## 1. Summary (answer to the research question)

*lcdH* encodes **L-carnitine dehydrogenase (EC 1.1.1.108)**, a soluble, cytoplasmic, NAD⁺-dependent oxidoreductase that catalyzes the **reversible oxidation of L-carnitine to 3-dehydrocarnitine**:

> **L-carnitine + NAD⁺ ⇌ 3-dehydrocarnitine + NADH + H⁺**

The enzyme is **strictly specific for the L-(−)-enantiomer of carnitine and for NAD⁺**. It performs the **committed first step of aerobic L-carnitine catabolism**, enabling *P. putida* to use L-carnitine as a sole source of carbon, nitrogen, and energy. Its product feeds a downstream pathway (3-dehydrocarnitine → glycine betaine → dimethylglycine → sarcosine → glycine). Structurally it is a homodimer of the 3-hydroxyacyl-CoA dehydrogenase (HAD) superfamily fold, acting in the cytoplasm.

---

## 2. Key findings with evidence

### 2.1 Catalyzed reaction and cofactor
Carnitine dehydrogenase (carnitine:NAD⁺ oxidoreductase, EC 1.1.1.108) purified from *P. putida* IFP 206 "catalyzes the oxidation of L-carnitine to 3-dehydrocarnitine" using NAD⁺ (Goulas 1988, PMID 3058208). The reaction is reversible; the enzyme has distinct pH optima for the two directions (pH 9.0 for oxidation, pH 7.0 for the reduction of 3-dehydrocarnitine back to L-carnitine), a hallmark of a thermodynamically balanced dehydrogenase.

Mechanistically, the enzyme oxidizes the **C3 secondary hydroxyl** of carnitine to a **C3 keto group**, exactly analogous to how 3-hydroxyacyl-CoA dehydrogenases oxidize the 3-hydroxyl of their substrates — consistent with its assignment to that structural family (UniProt Q88R32; IPR026578 L-carnitine_dehydrogenase signature).

### 2.2 Substrate and stereospecificity
The enzyme "is specific for L-carnitine and NAD⁺" (Goulas 1988, PMID 3058208): it does not oxidize D-carnitine and does not substitute NADP⁺ for NAD⁺. Km values for both substrates were determined. This stereospecificity is mirrored physiologically — *P. putida* and *Acinetobacter* grow on L-carnitine but not on D-carnitine as a sole carbon source unless L-carnitine is co-supplied (Kleber et al. 1977, PMID 849100; Kleber et al. 1978, PMID 565193).

### 2.3 Physical / biochemical properties
- Molecular mass ≈ **62 kDa**, a **homodimer of two identical subunits** (~31 kDa each) (Goulas 1988, PMID 3058208).
- Isoelectric point **4.7**; temperature optimum **30 °C**; purified **72-fold to homogeneity**.

### 2.4 Pathway role — committed first step of carnitine catabolism
"Some, especially *Pseudomonas* species, assimilate L-(−)-carnitine as sole source of carbon and nitrogen. **The first catabolic step is catalysed by the L-(−)-carnitine dehydrogenase**" (Kleber 1997 review, PMID 9037756). The product, 3-dehydrocarnitine, "is in turn metabolized to glycine betaine (GB), an intermediate metabolite in the catabolism of carnitine to glycine" (Wargo & Hogan 2009, PMID 19406895). Downstream, glycine betaine is demethylated stepwise to dimethylglycine → sarcosine → glycine by the GB-catabolic genes (gbcAB, dgcAB, soxBDAG) (Wargo et al. 2008, PMID 17951379). The deacetylation of 3-dehydrocarnitine to glycine betaine is proposed to involve a 3-ketoacid CoA-transferase (PA1999-PA2000 in *P. aeruginosa*) (Wargo & Hogan 2009, PMID 19406895).

**Full catabolic route initiated by lcdH:**
L-carnitine → **[lcdH]** → 3-dehydrocarnitine → glycine betaine → dimethylglycine → sarcosine → glycine.

### 2.5 Regulation
Expression is **substrate-inducible**: "L-Carnitine induced the carnitine dehydrogenase," and γ-butyrobetaine also induces it; synthesis "was repressed by glycinebetaine, glucose and long-chain fatty acids" (Kleber et al. 1978, PMID 565193). This links enzyme production to carnitine availability and to catabolite/pathway-product repression, so the cell makes the enzyme only when L-carnitine is present and preferred carbon sources are absent.

### 2.6 Localization
The enzyme was recovered from **soluble crude extract** and purified without membrane solubilization (Goulas 1988, PMID 3058208; activities measured in crude extract, Kleber 1978, PMID 565193), indicating a **cytoplasmic** location. This is where imported L-carnitine is oxidized. No signal/transmembrane features are indicated for this HAD-family soluble dehydrogenase.

### 2.7 Structural inference
UniProt Q88R32 places the protein in the **3-hydroxyacyl-CoA dehydrogenase family** with:
- **N-terminal NAD-binding Rossmann domain** (IPR006176, 3-OHacyl-CoA_DH_NAD-bd) — binds NAD⁺.
- **C-terminal α-helical catalytic/dimerization domain** (IPR006108, 3HC_DH_C; 6-phosphogluconate-dehydrogenase-like fold IPR008927/IPR013328) — forms the dimer interface and completes the active site.
- **L-carnitine dehydrogenase signature** (IPR026578).

The biochemically observed homodimer (Goulas 1988) matches this two-domain HAD fold, in which each subunit contributes a Rossmann NAD-binding module and a helical domain, and dimerization is required for a functional active site.

### 2.8 Sequence-level active-site evidence (bioinformatic)
Direct analysis of the 321-residue Q88R32 sequence (UniProt REST) confirms the diagnostic motifs of the family:
- **NAD-binding Rossmann fingerprint** `G-S-G-V-I-G` at residues **14–19** — exactly the UniProt-annotated NAD binding site (14–19). This glycine-rich βαβ loop is the classic dinucleotide-binding signature.
- **Substrate-binding motif** `SSTSG` at residues **117–121**, a conserved segment of the 3-hydroxyacyl-CoA dehydrogenase substrate pocket.
- **Family-diagnostic catalytic motif** `GHPFNP` at residues **140–145**, containing catalytic **His141** — the general-base histidine that deprotonates the C3-hydroxyl of L-carnitine, enabling hydride transfer to NAD⁺ to form the 3-keto product. This is the same catalytic logic used by 3-hydroxyacyl-CoA dehydrogenases.

UniProt/HAMAP (rule MF_02129) annotations independently confirm the manual findings: FUNCTION "Catalyzes the NAD(+)-dependent oxidation of L-carnitine to 3-dehydrocarnitine"; CATALYTIC "carnitine + NAD⁺ = 3-dehydrocarnitine + NADH + H⁺"; PATHWAY "Amine and polyamine metabolism; carnitine metabolism"; SUBUNIT "Homodimer"; SIMILARITY "3-hydroxyacyl-CoA dehydrogenase family, L-carnitine dehydrogenase subfamily." Database cross-references: KEGG `ppu:PP_0302`, BioCyc `PPUT160488:G1G01-334-MONOMER`, STRING `160488.PP_0302`.

### 2.9 Genomic context — a dedicated carnitine catabolic cluster (KT2440-specific)
KEGG genome annotation shows that *lcdH* (PP_0302) lies within a compact, co-oriented carnitine-catabolism gene cluster in KT2440, giving direct strain-specific support for the pathway model:

| Locus | Product | KO / EC | Role in pathway |
|---|---|---|---|
| **PP_0304** | Carnitine/glycine betaine ABC-transporter substrate-binding protein | K02002 | **Import** of L-carnitine into the cytoplasm |
| **PP_0302 (lcdH)** | L-carnitine (carnitine 3-)dehydrogenase | K17735 / EC 1.1.1.108 | **Step 1:** L-carnitine → 3-dehydrocarnitine (NAD⁺) |
| **PP_0303** | Dehydrocarnitine cleavage enzyme (3-dehydrocarnitine:acetyl-CoA trimethylamine transferase) | K27837 / EC 2.3.1.317 | **Step 2:** 3-dehydrocarnitine → glycine betaine (removes acetyl unit as acetyl-CoA) |
| **PP_0301** | Betainyl-CoA thioesterase | K27492 / EC 3.1.2.33 | Accessory CoA-ester hydrolysis |
| **PP_0305** | CdhR, AraC-family activator | K17736 | Carnitine-catabolism transcriptional **activator** |
| **PP_0298** | AraC-family, glycine betaine-responsive activator | K21826 | Downstream/betaine-responsive regulation |

This gene order (transporter → dehydrogenase → cleavage enzyme → regulator) confirms that L-carnitine is first **imported** by the PP_0304 ABC transporter, then oxidized **in the cytoplasm** by lcdH, after which the adjacent PP_0303 cleavage enzyme converts the 3-dehydrocarnitine product to **glycine betaine**. The clustered activator **CdhR (PP_0305)** provides the molecular basis for the substrate-inducibility of the enzyme observed biochemically (Kleber 1978, PMID 565193). Notably, this KT2440 cluster identifies the downstream betaine-forming step precisely (EC 2.3.1.317), refining the earlier "3-ketoacid CoA-transferase" inference drawn from *P. aeruginosa*.

---

## 3. Supported and refuted hypotheses

| Hypothesis | Verdict | Basis |
|---|---|---|
| *lcdH* encodes an NAD⁺-dependent L-carnitine dehydrogenase (EC 1.1.1.108) oxidizing L-carnitine → 3-dehydrocarnitine | **Supported** | Goulas 1988 (PMID 3058208); UniProt/HAMAP MF_02129 |
| Enzyme is stereospecific (L-carnitine only) and NAD⁺-specific (not NADP⁺) | **Supported** | Goulas 1988 (PMID 3058208) |
| It performs the committed first step of carnitine catabolism enabling growth on carnitine as C/N source | **Supported** | Kleber 1997 (PMID 9037756); Wargo & Hogan 2009 (PMID 19406895) |
| Product 3-dehydrocarnitine is routed to glycine betaine → glycine | **Supported** | Wargo & Hogan 2009 (PMID 19406895); Wargo 2008 (PMID 17951379) |
| Enzyme is cytoplasmic (soluble) | **Supported (strong inference)** | Soluble purification (PMID 3058208, 565193) |
| Homodimeric HAD-family fold with Rossmann NAD-binding domain | **Supported** | PMID 3058208 + UniProt domain architecture + sequence motifs (GSGVIG, His141) |
| lcdH sits in a dedicated carnitine catabolic cluster (importer + dehydrogenase + cleavage enzyme + CdhR activator) | **Supported (KT2440 genomics)** | KEGG PP_0298–PP_0305 |
| Enzyme uses NADP⁺ or acts on D-carnitine | **Refuted** | Goulas 1988 (PMID 3058208): specific for L-carnitine and NAD⁺ |

---

## 4. Limitations and future directions

- **Strain provenance:** The definitive biochemical characterization (Goulas 1988) used *P. putida* IFP 206, not KT2440 directly; genetic dissection of the pathway was done in *P. aeruginosa* PA14. KT2440 (PP_0302) function is assigned by sequence/HAMAP orthology, which is well supported but not yet KT2440-specific enzymology.
- **No experimental 3D structure** of this specific enzyme was located; the fold description rests on family/domain inference. AlphaFold modeling and superposition onto 3-hydroxyacyl-CoA dehydrogenase structures could confirm the active-site geometry and identify catalytic His/Asn residues.
- **Downstream deacetylation step** (3-dehydrocarnitine → glycine betaine) mechanism is inferred (3-ketoacid CoA-transferase) but not fully enzymatically characterized in *P. putida*.
- **Future work:** (i) KT2440 ΔPP_0302 knockout growth assays on L-carnitine; (ii) recombinant Q88R32 kinetics (Km, kcat for L-carnitine/NAD⁺); (iii) crystal/cryo-EM structure with NAD⁺/substrate to define catalytic residues; (iv) transcriptional mapping of the PP_0302 gene cluster and its regulator.

---

## References (PMID)
- **3058208** — Goulas P. (1988) Purification and properties of carnitine dehydrogenase from *Pseudomonas putida*. *Biochim Biophys Acta*.
- **9037756** — Kleber H-P. (1997) Bacterial carnitine metabolism. *FEMS Microbiol Lett*.
- **19406895** — Wargo MJ, Hogan DA. (2009) Identification of genes required for *Pseudomonas aeruginosa* carnitine catabolism. *Microbiology*.
- **17951379** — Wargo MJ, Szwergold BS, Hogan DA. (2008) Two gene clusters and a regulator required for *P. aeruginosa* glycine betaine catabolism. *J Bacteriol*.
- **565193** — Kleber H-P, Seim H, Aurich H, Strack E. (1978) Interrelationships between carnitine metabolism and fatty acid assimilation in *Pseudomonas putida*.
- **849100** — Kleber H-P, Seim H, Aurich H, Strack E. (1977) Utilization of trimethylammonium compounds by *Acinetobacter calcoaceticus*.
- **30670548** — Bazire P, et al. (2019) Characterization of L-carnitine metabolism in *Sinorhizobium meliloti*. *J Bacteriol*.


## Artifacts

- [OpenScientist final report](lcdH-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](lcdH-deep-research-openscientist_artifacts/final_report.pdf)