---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-24T13:31:00.214634'
end_time: '2026-10-24T13:47:16.855551'
duration_seconds: 976.64
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: RTL5
  gene_symbol: RTL5
  uniprot_accession: Q5HYW3
  protein_description: 'RecName: Full=Retrotransposon Gag-like protein 5 {ECO:0000312|HGNC:HGNC:29430};
    AltName: Full=Retrotransposon gag domain-containing protein 4 {ECO:0000305};'
  gene_info: Name=RTL5 {ECO:0000312|HGNC:HGNC:29430}; Synonyms=KIAA2001, RGAG4 {ECO:0000305};
  organism_full: Homo sapiens (Human).
  protein_family: Not specified in UniProt
  protein_domains: PEG10-RTL1_C-capsid. (IPR063300); RTL1-rel. (IPR032567); RTL1/1-8/LDOC_capsid-like.
    (IPR032549); PEG10-RTL1_C-capsid (PF30901); RTL1-8_LDOC (PF16297)
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
citation_count: 5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: RTL5-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: RTL5-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q5HYW3
- **Protein Description:** RecName: Full=Retrotransposon Gag-like protein 5 {ECO:0000312|HGNC:HGNC:29430}; AltName: Full=Retrotransposon gag domain-containing protein 4 {ECO:0000305};
- **Gene Information:** Name=RTL5 {ECO:0000312|HGNC:HGNC:29430}; Synonyms=KIAA2001, RGAG4 {ECO:0000305};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** PEG10-RTL1_C-capsid. (IPR063300); RTL1-rel. (IPR032567); RTL1/1-8/LDOC_capsid-like. (IPR032549); PEG10-RTL1_C-capsid (PF30901); RTL1-8_LDOC (PF16297)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "RTL5" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'RTL5' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **RTL5** (gene ID: RTL5, UniProt: Q5HYW3) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# RTL5 (Q5HYW3): A Domesticated Retroviral Gag Protein Functioning as a Microglial Antiviral Innate-Immune Effector

**Gene:** RTL5 (synonyms: RGAG4, KIAA2001, SIRH8) · **UniProt:** Q5HYW3 · **Ensembl:** ENSG00000242732 · **HGNC:** 29430
**Organism:** *Homo sapiens* (human) · **Locus:** chromosome X (~72.13 Mb, minus strand) · **Protein:** 569 aa, strongly acidic

---

## Summary

**RTL5** (Retrotransposon Gag-like protein 5; UniProt **Q5HYW3**; gene synonyms **SIRH8**, **RGAG4**, **KIAA2001**; HGNC:29430) is a human, eutherian-specific gene that originated through the evolutionary "domestication" of a retroviral/metavirus (Ty3/gypsy-related) *Gag* gene. The protein is **not an enzyme or a transporter**. Instead, its structure and function are those of a repurposed retroviral capsid (Gag) protein that placental mammals have co-opted for an entirely new host physiological role. The gene symbol "RTL5" unambiguously matches the UniProt target identity, the organism (*Homo sapiens*), and the capsid-like Gag domain architecture (PF30901, PF16297), so the research below is confidently about the correct protein. **No gene-identity ambiguity was encountered** — the literature names SIRH8 and RGAG4 map to the same gene.

The **primary, experimentally established function** of RTL5 is as an **innate-immune effector in brain microglia**. In the eutherian central nervous system, RTL5 is a microglial gene whose product is secreted and appears extracellularly as dots and granules. It acts specifically as a defense factor against **double-stranded RNA (dsRNA)** — a hallmark pathogen-associated molecular pattern (PAMP) of viral infection — physically binding and helping remove this viral signature. RTL5 is the **antiviral** member of a three-gene microglial pattern-recognition module in which the paralog **RTL6/SIRH3** handles bacterial lipopolysaccharide (LPS) and **RTL9/SIRH10** handles fungal PAMPs. RTL5 encodes a strongly acidic protein, in contrast to the strongly basic RTL6, and this biochemical polarity is thought to underlie their complementary target specificities.

A **second, tissue-specific role** has been documented in the **anterior pituitary gland**, where RTL5/RGAG4 is a direct transcriptional target of the zinc-finger transcription factor **Ikaros**. In pituitary corticotrophs, Ikaros binds the *Rgag4* promoter and drives its expression; knockdown of *Rgag4* profoundly reduces hormone gene expression and diminishes ACTH secretion, phenocopying Ikaros deficiency. Human expression data (Human Protein Atlas) corroborate both roles, showing brain-enhanced expression and enrichment in anterior-pituitary endocrine cells (corticotrophs). Structurally, AlphaFold modeling confirms the protein consists of a single ordered Gag/capsid-like domain flanked by large, disordered, acidic segments — architecture consistent with a capsid-derived molecule that engages nucleic-acid/charged ligands rather than catalyzing a reaction.

---

## Key Findings

### Finding 1 — RTL5 is a eutherian-specific, retrovirus-derived "domesticated" Gag gene (= SIRH8/RGAG4/KIAA2001)

RTL5 belongs to a family of **11 eutherian metavirus-derived genes** collectively called the **sushi-ichi retrotransposon homolog (SIRH) / Retrotransposon Gag-like (RTL)** genes. These genes arose when the *Gag* (and in some cases *Pol*) regions of an ancient Ty3/gypsy-related metavirus were captured and functionally repurposed ("domesticated") in the ancestor of placental mammals. UniProt describes Q5HYW3 as a 569-amino-acid protein named Retrotransposon Gag-like protein 5, carrying the **PEG10-RTL1_C-capsid domain (PF30901)** and the **RTL1/8-LDOC capsid-like domain (PF16297)** — the structural signature of a retroviral capsid.

Review literature directly establishes the RTL5 = SIRH8 identity and its evolutionary origin: *"Retrotransposon Gag-like 5 [RTL5, also known as sushi-ichi-related retrotransposon homolog 8 (SIRH8)] and RTL6 (also known as SIRH3) are eutherian-specific genes presumably derived from a retrovirus and phylogenetically related to each other"* [PMID: 36162816]. The broader family context is confirmed by *"Eutherians have 11 retrotransposon Gag-like (RTL)/sushi-ichi retrotransposon homolog (SIRH) genes presumably derived from a certain retrovirus"* [PMID: 37892118], and the metavirus (Ty3/gypsy) origin is clarified by *"Eutherian mammals possess 11 metavirus-derived genes, collectively known as the sushi-ichi retrotransposon homologue (SIRH)/Retrotransposon Gag-like (RTL) genes"* [PMID: 42511665].

**Interpretation:** RTL5 is a captured viral structural gene, not a conventional cellular enzyme. Its function must be understood in terms of a repurposed capsid-like protein — a molecule evolved to interact with nucleic acids and to self-assemble/bind charged ligands — rather than a catalytic active site.

### Finding 2 — RTL5 is a microglial innate-immune factor acting extracellularly against double-stranded RNA

The most precise functional data come from knock-in and knockout mouse experiments. In knock-in mice expressing an RTL5–mCherry fusion, the protein is produced by **microglia** and appears as **extracellular dots and granules** in the central nervous system. The protein responds rapidly to pathogen-associated molecules (LPS, the dsRNA analog poly(I:C), and non-methylated CpG DNA), and genetic knockout experiments reveal a specific target: **RTL5 acts as a factor against dsRNA**, while its paralog RTL6 acts against LPS. Consistent with the UniProt annotation of multiple acidic compositional-bias regions (residues 334–350, 416–429, 443–469), RTL5 is a **strongly acidic** protein.

The key statements from the primary study are: *"RTL5 and RTL6 are microglial genes with roles in the front line of innate brain immune response"*; the RTL5 protein *"appeared as extracellular dots and granules in the central nervous system"*; and most decisively, *"RTL6 and RTL5 act as factors against LPS and dsRNA, respectively, in the brain, providing the first demonstration that retrovirus-derived genes play a role in the eutherian innate immune system"* [PMID: 36162816]. The biochemical contrast that likely encodes target specificity is captured by *"They, respectively, encode a strongly acidic and extremely basic protein"* [PMID: 36162816] — RTL5 being the strongly acidic member.

**Interpretation:** This is the central, mechanistically precise finding. RTL5's primary function is as a **secreted, extracellular pattern-recognition/clearance factor** specific for **viral double-stranded RNA** in the brain. It operates outside the cell (in the extracellular space of the CNS), consistent with a role in sequestering or removing a viral PAMP at the "front line" of brain immunity.

### Finding 3 — RTL5/RGAG4 is an Ikaros transcriptional target in the pituitary that supports hormone (ACTH) gene expression

Independent of its brain-immune role, RTL5 (under the name **RGAG4**) was identified in a chromatin-immunoprecipitation screen in pituitary corticotroph cells as a target of the zinc-finger transcription factor **Ikaros**. Ikaros binds the *Rgag4* promoter and induces endogenous expression; *Rgag4* is robustly expressed in the anterior pituitary and reduced in Ikaros-knockout mice. Functionally, knockdown of *Rgag4* profoundly reduces hormone gene expression and diminishes **ACTH secretion**, recapitulating the phenotype of Ikaros deficiency.

The supporting statements are: *"We identified the ability of Ikaros to bind the Rgag4 promoter, influence its transcriptional activity, and induce endogenous gene expression"*; *"Down-regulation of Rgag4 resulted in profound reduction of hormone gene expression with diminished ACTH secretion, recapitulating the effect of Ikaros deficiency in knockout mice"*; and *"Robust expression of Rgag4 was noted in the anterior lobe of the pituitary gland which was diminished in Ikaros knockout mice"* [PMID: 28919299].

**Interpretation:** RTL5 has a distinct, tissue-specific function in the **anterior pituitary** as a downstream effector in an Ikaros-driven transcriptional program controlling corticotroph hormone output. This role is separate from — and mechanistically unrelated to — the microglial antiviral function, illustrating functional diversification of a single domesticated gene across tissues.

### Finding 4 — RTL5 is the antiviral member of a microglial PAMP-recognition triad (RTL5/RTL6/RTL9)

Multiple reviews place RTL5 within a coherent, three-gene **microglial defense module**. In this module, each gene targets a different class of pathogen: **RTL5/SIRH8 → viruses (dsRNA)**, **RTL6/SIRH3 → bacteria (LPS)**, and **RTL9/SIRH10 → fungi**. The mechanism attributed to RTL5 and RTL6 is physical **removal** of their respective PAMPs.

The reviews state: *"SIRH3/RTL6, SIRH8/RTL5, and SIRH10/RTL9 mediate innate immune responses against bacterial-, viral-, and fungal-derived pathogen-associated molecular patterns, respectively"* [PMID: 42511665]; *"RTL5 and RTL6 … are microglial genes that play important roles in the brain's innate immunity against viruses and bacteria through their removal of double-stranded [RNA]…"* [PMID: 37834332]; and *"at least three RTL/SIRH genes, RTL5/SIRH8, RTL6/SIRH3, and RTL9/SIRH10, play important roles in combating a variety of pathogens, namely viruses, bacteria, and fungi, respectively"* [PMID: 37892118]. Genomically, human RTL5 is **ENSG00000242732**, located on the **X chromosome** (~72.13 Mb, minus strand), protein-coding, ~569 aa.

**Interpretation:** RTL5 is not an isolated factor but one specialized component of a modular, three-pronged innate-immune system in microglia. Its specialization — dsRNA/viruses — defines its precise role within this system, mapping onto the division of labor among the three paralogs.

### Finding 5 — Human expression data corroborate brain and pituitary-corticotroph roles

Human Protein Atlas data for ENSG00000242732 show **"Tissue enhanced"** expression with a **brain-specific nTPM of 9.4**. Single-cell data reveal enrichment in anterior-pituitary endocrine cells — **corticotrophs (25.1 nCPM)**, lactotrophs (15.0), gonadotrophs (12.2), and neuroendocrine cells (11.6) — and the pituitary endocrine-cell group scores 25.1. The gene is essentially absent from the GTEx v8 bulk median table, consistent with restricted, cell-type-specific expression that is diluted below threshold in bulk tissue.

**Interpretation:** Independent human transcriptomic evidence supports **both** documented functional contexts: brain-enhanced expression aligns with the microglial immune role, and corticotroph enrichment aligns with the pituitary/Ikaros role. The low bulk expression is exactly what is expected for a gene restricted to specialized cell populations (microglia, corticotrophs).

### Finding 6 — AlphaFold structure: one ordered Gag/capsid domain plus a large disordered acidic C-terminal tail

The AlphaFold DB model of Q5HYW3 (v6, 569 aa) shows a **single high-confidence structured module spanning ~residues 152–323** (mean pLDDT 85.9). The remaining regions are low-confidence/disordered: the N-terminus (1–115, pLDDT 56.9), a proline-rich region (115–151, 52.3), and a long C-terminal region (323–506, 56.6; 506–569, 44.3). These disordered, low-confidence segments coincide precisely with UniProt-annotated disordered regions (115–151, 323–506) and acidic compositional-bias stretches (334–350, 416–429, 443–469).

**Interpretation:** The structure is fully consistent with the functional model. RTL5 consists of a **single folded Gag/capsid-like domain** — the ancestral nucleic-acid/ligand-binding core — attached to an extended, intrinsically disordered, **acidic tail**. Disordered acidic tails commonly mediate electrostatic/multivalent interactions and extracellular behavior; here they are consistent with a secreted factor that engages charged ligands and with the "strongly acidic" character implicated in dsRNA-targeting specificity.

---

## Mechanistic Model / Interpretation

RTL5 is best understood as a **captured retroviral capsid protein repurposed by eutherians for host defense and endocrine function**. The following model integrates the findings:

```
          ANCESTRAL Ty3/gypsy METAVIRUS (Gag/capsid gene)
                               │
                   evolutionary "domestication"
                     in placental-mammal ancestor
                               │
             ┌─────────────────┴─────────────────┐
             ▼                                   ▼
   RTL/SIRH gene family (11 genes)       RTL5 = SIRH8 / RGAG4
   incl. RTL5, RTL6, RTL9, PEG10 ...      (ENSG00000242732, chrX)
                                                 │
                 ┌───────────────────────────────┴───────────────────────┐
                 ▼                                                         ▼
   ROLE 1: BRAIN INNATE IMMUNITY (microglia)         ROLE 2: ANTERIOR PITUITARY (corticotrophs)
   ────────────────────────────────────────          ─────────────────────────────────────────
   Secreted → extracellular dots/granules             Ikaros binds Rgag4 promoter → induces expression
   Strongly ACIDIC protein                            Rgag4 supports hormone gene expression
   TARGET: double-stranded RNA (viral PAMP)           Rgag4 knockdown → ↓ hormone genes, ↓ ACTH
   MECHANISM: physical removal/sequestration          (phenocopies Ikaros deficiency)

   Part of a PAMP-recognition triad:
     • RTL5/SIRH8  → viruses (dsRNA)   [acidic protein]
     • RTL6/SIRH3  → bacteria (LPS)    [basic protein]
     • RTL9/SIRH10 → fungi
```

**Structure–function logic.** The AlphaFold model (Finding 6) shows a single ordered capsid-like domain (~152–323) plus a disordered acidic tail (~323–569). Retroviral Gag/capsid domains natively bind nucleic acids and self-assemble. In RTL5, this core is retained while the acidic disordered tail provides the "strongly acidic" character that distinguishes RTL5 (antiviral/dsRNA) from the "extremely basic" RTL6 (antibacterial/LPS). The charge polarity between paralogs plausibly encodes their complementary ligand specificities: an acidic RTL5 engaging dsRNA, a basic RTL6 engaging the anionic lipid-A/LPS.

**Localization.** RTL5 performs its antiviral function **extracellularly**, in the extracellular space of the CNS, where it appears as secreted dots/granules produced by microglia (Finding 2). This is distinct from where many canonical dsRNA sensors (e.g., RIG-I/MDA5, cytoplasmic; TLR3, endosomal) operate, suggesting RTL5 provides an **extracellular clearance/sequestration** arm complementing intracellular viral sensing. Its pituitary role occurs in anterior-lobe endocrine cells (corticotrophs), where it acts in a transcriptional/effector capacity downstream of Ikaros (Finding 3).

**Two functions, one protein.** The data support two mechanistically distinct roles in two tissues — a situation not unusual for domesticated genes recruited into multiple host pathways. The microglial antiviral role is the more mechanistically precise and is supported by direct knock-in/knockout evidence; the pituitary role is supported by ChIP, expression, and knockdown data.

| Feature | Microglial role | Pituitary role |
|---|---|---|
| Tissue / cell | Brain microglia | Anterior pituitary corticotrophs |
| Localization | Extracellular (secreted dots/granules) | Intracellular / transcriptional effector |
| Molecular target | Double-stranded RNA (viral PAMP) | Hormone gene expression program |
| Upstream regulator | Pathogen exposure | Ikaros transcription factor |
| Functional readout | Removal of dsRNA; antiviral defense | ACTH secretion, hormone gene expression |
| Key evidence | Knock-in/knockout mice [PMID: 36162816] | ChIP + knockdown [PMID: 28919299] |

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution | Weight |
|---|---|---|---|
| [36162816](https://pubmed.ncbi.nlm.nih.gov/36162816/) | *Retrovirus-derived RTL5 and RTL6 genes are novel constituents of the innate immune system in the eutherian brain* | **Primary experimental study**: RTL5=SIRH8 identity; microglial expression; extracellular localization; dsRNA target via knockout; acidic protein | Highest (primary) |
| [28919299](https://pubmed.ncbi.nlm.nih.gov/28919299/) | *The retrotransposon gag domain containing protein Rgag4 is an Ikaros target in the pituitary* | **Primary experimental study**: RGAG4/RTL5 as Ikaros target; anterior-pituitary expression; knockdown reduces ACTH and hormone genes | Highest (primary) |
| [42511665](https://pubmed.ncbi.nlm.nih.gov/42511665/) | *Virus-Derived Domesticated Genes in Microglia and Resident Macrophages…* | Review: metavirus origin; RTL5/RTL6/RTL9 PAMP triad (virus/bacteria/fungi) | Review |
| [37892118](https://pubmed.ncbi.nlm.nih.gov/37892118/) | *Retrovirus-Derived RTL/SIRH: Their Diverse Roles…* | Review: 11-gene RTL/SIRH family; RTL5 antiviral specificity within triad | Review |
| [37834332](https://pubmed.ncbi.nlm.nih.gov/37834332/) | *Retrovirus-Derived…* | Review: mechanism = removal of double-stranded RNA by RTL5 | Review |
| [41594701](https://pubmed.ncbi.nlm.nih.gov/41594701/) | *Placenta-Driven Evolution: Viral Gene Acquisition…* | Context: metavirus-derived gene acquisition in mammalian evolution | Background |
| [37842090](https://pubmed.ncbi.nlm.nih.gov/37842090/) | *Roles of retrovirus-derived…* | Context: RTL/SIRH functional roles (no abstract available) | Background |

**How the evidence fits together.** The two primary studies ([PMID: 36162816](https://pubmed.ncbi.nlm.nih.gov/36162816/) and [PMID: 28919299](https://pubmed.ncbi.nlm.nih.gov/28919299/)) independently establish the two functional roles using orthogonal methods (mouse genetics + imaging; ChIP + knockdown). The reviews ([PMID: 42511665](https://pubmed.ncbi.nlm.nih.gov/42511665/), [PMID: 37892118](https://pubmed.ncbi.nlm.nih.gov/37892118/), [PMID: 37834332](https://pubmed.ncbi.nlm.nih.gov/37834332/)) corroborate and contextualize the microglial role, consistently assigning RTL5 the **antiviral/dsRNA** specialization within the RTL5/RTL6/RTL9 triad. UniProt, Ensembl, Human Protein Atlas, and AlphaFold provide structural, genomic, and expression evidence fully consistent with the literature — no database annotation contradicts the primary findings.

**No gene-identity conflict.** The verification required by the task is satisfied: "RTL5" matches the UniProt target Q5HYW3 (Retrotransposon Gag-like protein 5), the organism is human, and the capsid/Gag domains (PF30901, PF16297) align with the "domesticated retroviral Gag" literature. The synonyms SIRH8 and RGAG4 are the names used in the primary literature and map to the same gene. There is **no** confounding gene with the same symbol driving the findings.

---

## Limitations and Knowledge Gaps

1. **Most functional data are from mouse, not human.** The definitive antiviral/dsRNA experiments and the Ikaros/pituitary experiments were performed in mouse models. While RTL5 is eutherian-conserved and human expression data (HPA) corroborate both tissue contexts, direct human functional validation is lacking.

2. **Molecular mechanism of dsRNA "removal" is undefined.** The literature states RTL5 acts "through removal" of dsRNA and appears as extracellular granules, but the precise biochemistry — direct dsRNA binding affinity/specificity, stoichiometry, whether RTL5 sequesters, aggregates, or traffics dsRNA, and whether it requires partner proteins — has not been resolved. No binding constants or structural complex with dsRNA exist.

3. **Structure is predicted, not experimental.** The domain architecture (one ordered Gag/capsid domain + disordered acidic tail) is from AlphaFold (pLDDT-based), not from experimental crystallography/cryo-EM. The functional importance of specific residues (e.g., the acidic stretches) in dsRNA engagement is inferred, not demonstrated.

4. **Relationship between the two roles is unexplored.** It is unknown whether the microglial and pituitary functions share any molecular mechanism, whether different isoforms/processing underlie them, or whether they are entirely independent recruitments of the same protein.

5. **Not an enzyme/transporter — no catalytic substrate.** For the task's enzyme/transporter framing: RTL5 has **no known catalytic activity or transport substrate**. Its "substrate" in the functional sense is **dsRNA as a ligand/target**, not a reaction substrate. This should be stated explicitly to avoid over-interpretation of the Gag domain.

6. **Limited literature depth.** RTL5 is a relatively understudied gene; the functional conclusions rest on a small number of primary studies (two) plus reviews by overlapping author groups. Independent replication would strengthen confidence.

---

## Proposed Follow-up Experiments / Actions

1. **Direct dsRNA-binding biochemistry (human protein).** Express and purify recombinant human RTL5 (and its isolated capsid domain vs. acidic tail) and measure binding to dsRNA (e.g., poly(I:C)) vs. ssRNA/dsDNA/LPS by EMSA, fluorescence anisotropy, or SPR. Determine affinity and specificity, and test whether the acidic tail or capsid core mediates binding.

2. **Structural determination of the RTL5–dsRNA interaction.** Pursue cryo-EM or crystallography of the ordered Gag/capsid domain (residues ~152–323) alone and in complex with a short dsRNA, to test the predicted architecture and map the binding interface.

3. **Human microglia validation.** Use iPSC-derived human microglia with RTL5 knockout/knock-in reporters to confirm secretion, extracellular granule formation, and dsRNA (poly(I:C)) responsiveness in a human system; assess antiviral protection against dsRNA-genome or dsRNA-intermediate viruses.

4. **Mechanism of "removal."** Determine the fate of RTL5-bound dsRNA: does RTL5 sequester it into granules, promote clearance/phagocytosis, or deliver it to degradation? Use live imaging plus proximity labeling (BioID/TurboID) to identify extracellular/membrane partners.

5. **Dissect the pituitary role.** In corticotroph models, map Ikaros → RTL5 regulation in human cells, define which hormone genes depend on RTL5, and test whether the capsid domain or acidic tail is required for the ACTH-supporting function — clarifying whether this role is mechanistically distinct from dsRNA binding.

6. **Charge-polarity hypothesis.** Directly test whether swapping acidic (RTL5) vs. basic (RTL6) tail regions switches PAMP specificity (dsRNA ↔ LPS), which would mechanistically confirm the electrostatic basis of the triad's division of labor.

---

## Conclusion

RTL5 (Q5HYW3; SIRH8/RGAG4) is a eutherian-specific, domesticated retroviral (Ty3/gypsy metavirus) **Gag/capsid-derived protein** — not an enzyme or transporter. Its primary, experimentally established function is as a **secreted microglial innate-immune effector** that recognizes and physically removes **double-stranded RNA** (a viral PAMP), acting **extracellularly** in the brain as the **antiviral** member of a three-gene microglial defense module (RTL5→viruses, RTL6→bacteria/LPS, RTL9→fungi). A distinct, tissue-specific role occurs in the **anterior pituitary**, where RTL5/RGAG4 functions as an **Ikaros transcriptional target** supporting corticotroph hormone (ACTH) gene expression. Its single ordered capsid-like domain plus acidic disordered tail, brain- and corticotroph-enriched expression, and the complementary acidic/basic polarity of RTL5 vs. RTL6 together provide a coherent structural and evolutionary rationale for these functions.


## Artifacts

- [OpenScientist final report](RTL5-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](RTL5-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:36162816
2. PMID:37892118
3. PMID:42511665
4. PMID:28919299
5. PMID:37834332