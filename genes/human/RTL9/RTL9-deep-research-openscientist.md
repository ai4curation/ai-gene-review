---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-24T13:59:01.646449'
end_time: '2026-10-24T14:24:57.143221'
duration_seconds: 1555.5
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: RTL9
  gene_symbol: RTL9
  uniprot_accession: Q8NET4
  protein_description: 'RecName: Full=Retrotransposon Gag-like protein 9 {ECO:0000312|HGNC:HGNC:29245};
    AltName: Full=Retrotransposon gag domain-containing protein 1; AltName: Full=Tumor
    antigen BJ-HCC-23;'
  gene_info: Name=RTL9 {ECO:0000312|HGNC:HGNC:29245}; Synonyms=KIAA1318, RGAG1;
  organism_full: Homo sapiens (Human).
  protein_family: Not specified in UniProt
  protein_domains: PEG10-RTL1_C-capsid. (IPR063300); RTL9. (IPR042919); PEG10-RTL1_C-capsid
    (PF30901)
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
citation_count: 10
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: RTL9-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: RTL9-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q8NET4
- **Protein Description:** RecName: Full=Retrotransposon Gag-like protein 9 {ECO:0000312|HGNC:HGNC:29245}; AltName: Full=Retrotransposon gag domain-containing protein 1; AltName: Full=Tumor antigen BJ-HCC-23;
- **Gene Information:** Name=RTL9 {ECO:0000312|HGNC:HGNC:29245}; Synonyms=KIAA1318, RGAG1;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** PEG10-RTL1_C-capsid. (IPR063300); RTL9. (IPR042919); PEG10-RTL1_C-capsid (PF30901)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "RTL9" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'RTL9' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **RTL9** (gene ID: RTL9, UniProt: Q8NET4) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# RTL9 (Q8NET4): A Domesticated Retroviral Gag Gene Functioning as a Microglial Lysosomal Antifungal Effector

**Gene:** RTL9 (Retrotransposon Gag-like protein 9)
**Synonyms:** RGAG1, KIAA1318, SIRH10, MART9, Tumor antigen BJ-HCC-23
**UniProt:** Q8NET4 · **NCBI Gene:** 57529 · **Locus:** Xq23 · **Organism:** *Homo sapiens*

---

## Gene Identity Verification

Before presenting the research findings, the mandatory identity check was performed. The target gene symbol **RTL9** and its synonyms (RGAG1, KIAA1318, SIRH10, Mart9) all map consistently to **UniProt Q8NET4**, a 1388-amino-acid human protein located on the X chromosome (Xq23). The UniProt protein description — "Retrotransposon Gag-like protein 9 / Retrotransposon gag domain-containing protein 1" — is fully concordant with the key domain annotation (**PEG10-RTL1_C-capsid**, PF30901 / IPR063300; and the RTL9-specific signature IPR042919). The scientific literature on RTL9/SIRH10 in the eutherian RTL/SIRH gene family (primarily from the Ishino/Kaneko-Ishino group) describes the same gene and the same retroviral-Gag-derived architecture. **Identity is confirmed; the research below pertains to the correct gene.**

One important caveat for readers mining databases: the symbol **RGAG1** also appears in several clinical/genomic papers (BCOR fusion sarcomas, Xq deletion syndromes, testicular cancer methylation studies, UK10K lipid GWAS). These describe the *genomic locus* RGAG1/RTL9 as a bystander or fusion partner and do **not** characterize the biochemical function of the protein. The functional annotation below is drawn from the RTL/SIRH functional literature, not these incidental genomic reports.

---

## Summary

**RTL9** (RGAG1/SIRH10/Mart9; UniProt **Q8NET4**) is a **domesticated retroviral Gag gene** — one of eleven eutherian-specific **Retrotransposon Gag-like (RTL) / sushi-ichi-related retrotransposon homolog (SIRH)** genes that arose when a Ty3/Gypsy ("sushi-ichi") LTR-retrotransposon was exapted into the mammalian genome. The human protein is 1388 residues (~144 kDa), encoded by a single-copy, X-linked gene at Xq23. Its only recognizable structured module is a **C-terminal retroviral Gag/capsid-like domain** (Pfam PF30901 / InterPro IPR063300), mapped to approximately residues 1239–1305; the large N-terminal region is poorly characterized and substantially disordered.

The **primary function of RTL9 is innate antifungal immunity in the brain**. Experimental evidence from RTL9-mCherry knock-in mice shows that the RTL9 protein localizes to **microglial lysosomes**, where it degrades **zymosan** — a fungal cell-wall β-glucan/mannan preparation that serves as a model fungal pathogen-associated molecular pattern (PAMP). Critically, in knockout mice engineered to express an **RTL9ΔC** protein lacking the C-terminal retroviral Gag-like region, this zymosan-degrading activity was abolished, demonstrating that the **Gag domain is essential** for function ([PMID: 37834332](https://pubmed.ncbi.nlm.nih.gov/37834332/)).

RTL9 is therefore not a classical enzyme, transporter, or signaling receptor. Instead, it is the **antifungal arm of a three-member microglial innate-immune module** unique to the eutherian brain: **RTL5/SIRH8 → viruses (double-stranded RNA), RTL6/SIRH3 → bacteria (lipopolysaccharide), and RTL9/SIRH10 → fungi (zymosan)**. Whereas RTL5 and RTL6 act extracellularly as secreted PAMP-binding granules, RTL9 is distinctive in acting **intracellularly within the lysosome** to clear phagocytosed fungal material. The human–mouse orthologs are strongly conserved across the functional Gag module (~78% amino-acid identity), supporting conservation of this antifungal role in humans.

---

## Key Findings

### Finding 1 — Primary function: lysosomal antifungal defense in brain microglia

The single most informative study of RTL9 function is **Shiura et al., 2023** (*Retrovirus-Derived RTL9 Gene...*, *Int. J. Mol. Sci.*; [PMID: 37834332](https://pubmed.ncbi.nlm.nih.gov/37834332/)). Using **RTL9-mCherry knock-in mice**, the authors demonstrated that the RTL9 protein is expressed in **microglia** — the brain's resident macrophages — and that it **localizes specifically to lysosomes**. When fungal **zymosan** (a particulate β-1,3-glucan/mannan preparation derived from the *Saccharomyces cerevisiae* cell wall and a canonical fungal PAMP) was introduced into the brain, it was phagocytosed by microglia and trafficked to lysosomes, where RTL9 mediated its **degradation**. In the authors' own words: *"Here, we demonstrate that RTL9 plays an important role, degrading zymosan in the brain. The RTL9 protein is localized in the microglial lysosomes where incorporated zymosan is digested."*

The functional requirement of the retroviral Gag domain was established by a **structure–function loss-of-function experiment**: in *Rtl9* knockout mice engineered to express a truncated **RTL9ΔC** protein lacking the C-terminal retroviral GAG-like region, *"the zymosan degrading activity was lost."* This directly links the antifungal activity to the inherited retroviral capsid-like module rather than to the poorly characterized N-terminus.

An independent 2026 review (**Irie et al.**, *Virus-Derived Domesticated Genes in Microglia and Resident Macrophages*; [PMID: 42511665](https://pubmed.ncbi.nlm.nih.gov/42511665/)) corroborates this, stating that *"SIRH3/RTL6, SIRH8/RTL5, and SIRH10/RTL9 mediate innate immune responses against bacterial-, viral-, and fungal-derived pathogen-associated molecular patterns, respectively."* RTL9 (= SIRH10) is thus consistently assigned the **antifungal** role.

**Localization:** microglial **lysosomes** (intracellular). **Substrate/target:** fungal cell-wall PAMP (zymosan / β-glucan). **Essential module:** C-terminal retroviral Gag/capsid-like domain.

### Finding 2 — RTL9 is a domesticated Ty3/Gypsy (sushi-ichi) retrotransposon Gag-derived gene

RTL9 belongs to a family of **eleven** eutherian **RTL/SIRH** genes that were created by the **domestication (exaptation)** of a retroviral/retrotransposon Gag gene. As Kaneko-Ishino & Ishino, 2023 (*Retrovirus-Derived RTL/SIRH...*, *Biomolecules*; [PMID: 37892118](https://pubmed.ncbi.nlm.nih.gov/37892118/)) state: *"Eutherians have 11 retrotransposon Gag-like (RTL)/sushi-ichi retrotransposon homolog (SIRH) genes presumably derived from a certain retrovirus."* The ancestral element is the **sushi-ichi LTR-retrotransposon**, a member of the **Metaviridae (Ty3/Gypsy)** superfamily first described in pufferfish. RTL9 is equivalently named **SIRH10** and **Mart9** in the Mart (Mammalian retrotransposon transcript) nomenclature.

The molecular signature of this retroviral ancestry is retained in UniProt Q8NET4 as the **PEG10-RTL1_C-capsid domain** (Pfam **PF30901** / InterPro **IPR063300**) — a Gag/capsid-like fold shared with the better-known domesticated genes **PEG10** and **RTL1/PEG11**. The persistence of this domain over the ~160 million years of eutherian evolution, together with the functional data above, indicates that RTL9 was **repurposed** from a mobile-element gene into a host gene with a defined physiological role.

### Finding 3 — RTL9 is the antifungal member of a three-gene microglial innate-immune module

A central organizing concept is that domesticated retroviral Gag genes built a **novel innate-immune system in the eutherian brain**. Kaneko-Ishino & Ishino, 2023 ([PMID: 37892118](https://pubmed.ncbi.nlm.nih.gov/37892118/)) describe that *"at least three RTL/SIRH genes, RTL5/SIRH8, RTL6/SIRH3, and RTL9/SIRH10, play important roles in combating a variety of pathogens, namely viruses, bacteria, and fungi, respectively."* Each family member recognizes a **distinct class of PAMP**:

| RTL / SIRH gene | Pathogen class | PAMP target | Site of action |
|---|---|---|---|
| RTL5 / SIRH8 | Viruses | Double-stranded RNA | Extracellular (secreted granules) |
| RTL6 / SIRH3 | Bacteria | Lipopolysaccharide (LPS) | Extracellular (secreted granules) |
| **RTL9 / SIRH10** | **Fungi** | **Zymosan / β-glucan** | **Intracellular (microglial lysosome)** |

This division of labor means RTL9 occupies the **antifungal arm** of a dedicated, eutherian-specific defense system in the central nervous system. The module is paralogous — the three genes derive from the same ancestral Gag gene but have sub-functionalized to cover different microbial threats.

### Finding 4 — Human gene/protein architecture: X-linked, 1388 aa, single C-terminal Gag domain, testis-enriched expression

According to NCBI Gene (ID **57529**), human RTL9 is a **single-copy gene on the X chromosome at Xq23** (GRCh38 chrX:110,358,847–110,456,333), with aliases **MART9 / RGAG1 / SIRH10**. UniProt **Q8NET4** describes a **1388-residue (~144 kDa)** protein. Domain mapping by InterPro/Pfam places the **only recognizable structured module** — the PEG10/RTL1 C-terminal capsid-like (Gag) domain (**IPR063300 / PF30901**) — at approximately **residues 1239–1305**. The large **N-terminal region (residues 1–1238)** contains multiple predicted intrinsically disordered segments and **no other recognized domains**, and UniProt provides **no curated function or subcellular-location annotation** for the human protein.

Expression data from the **Human Protein Atlas** indicate the RTL9 transcript is **"tissue enriched" in testis** (~7.5 nTPM) and **"cell-type enriched,"** with no experimentally determined subcellular localization in that resource. The testis enrichment in humans contrasts with the functionally characterized microglial/brain role in mice, a point revisited under Limitations. Consistent with low somatic expression in some tissues, an earlier mouse study (Kaneko-Ishino lab placentogenesis survey; [PMID: 25888968](https://pubmed.ncbi.nlm.nih.gov/25888968/)) found **Rgag1/Mart9 expression undetectable in the placenta**, indicating RTL9 has no placental role and is spatially restricted — compatible with a specialized, tissue-specific (brain microglia / testis) function rather than a housekeeping one.

### Finding 5 — Mechanistic model: RTL/SIRH Gag proteins are PAMP-binding/clearance effectors; RTL9 acts intracellularly at the lysosome

The mechanistic framework for the whole family comes from **Irie et al., 2022** (*Retrovirus-derived RTL5 and RTL6 genes are novel constituents of the innate immune system in the eutherian brain*, *Development*; [PMID: 36162816](https://pubmed.ncbi.nlm.nih.gov/36162816/)). This study showed that **RTL5 and RTL6 are microglial proteins** that appear as **extracellular dots/granules** in the CNS and *"display a rapid response to pathogens such as lipopolysaccharide (LPS), double-stranded (ds) RNA analog and non-methylated CpG DNA, acting both cooperatively and/or independently."* Knockout experiments confirmed RTL6 acts against LPS (bacteria) and RTL5 against dsRNA (viruses). The paper explicitly provides *"the first demonstration that retrovirus-derived genes play a role in the eutherian innate immune system."*

The unifying mechanism is therefore that **domesticated retroviral Gag proteins directly bind and neutralize or clear microbial molecular patterns**. RTL9 fits this framework but is mechanistically **distinctive**: rather than acting extracellularly, it operates **intracellularly within the microglial lysosome**, where it degrades phagocytosed fungal zymosan, with its C-terminal Gag domain being indispensable ([PMID: 37834332](https://pubmed.ncbi.nlm.nih.gov/37834332/)). The retroviral capsid-like fold — evolutionarily built to package and interact with nucleic acids and to oligomerize — is plausibly repurposed here to **bind fungal cell-wall polysaccharide and promote its lysosomal breakdown**, although the precise biochemistry (direct β-glucan binding vs. recruitment of hydrolases) remains to be resolved.

### Finding 6 — Human and mouse RTL9 are conserved orthologs with a highly conserved Gag domain

To assess whether the mouse-derived functional conclusions transfer to humans, the orthologs were compared directly. Human RTL9 (**Q8NET4**, 1388 aa) and mouse Rtl9 (**Q32KG4**, 1339 aa) are **single orthologs of comparable length**, and both retain the Pfam **PEG10/RTL1 C-terminal capsid-like Gag domain (PF30901)** — presence in the mouse protein was confirmed via InterPro. A **Needleman–Wunsch global alignment** of the C-terminal Gag-domain region yielded **~78% amino-acid identity (112/143 aligned positions)**. For a retroelement-derived protein, this level of conservation is high and indicates **strong purifying (negative) selection** acting specifically on the functional Gag module. This evolutionary signature strengthens the inference that the **antifungal function demonstrated in mouse microglia is conserved in the human protein**.

---

## Mechanistic Model / Interpretation

The findings integrate into a coherent evolutionary-and-functional narrative:

```
   Ancestral Ty3/Gypsy "sushi-ichi" LTR-retrotransposon (retroviral Gag/capsid gene)
                                   │
                        Domestication in early eutherians
                                   │
          ┌────────────────────────┴────────────────────────┐
     11 RTL/SIRH genes (PEG10, RTL1/PEG11, RTL5, RTL6, RTL9/SIRH10, ...)
                                   │
            Sub-functionalization of a brain microglial innate-immune trio
                                   │
   ┌───────────────┬───────────────────────────┬──────────────────────────┐
  RTL5/SIRH8      RTL6/SIRH3                   RTL9/SIRH10 (this gene)
  antiVIRAL       antiBACTERIAL                antiFUNGAL
  (dsRNA)         (LPS)                        (zymosan / β-glucan)
  extracellular   extracellular                INTRACELLULAR — lysosome
  secreted dots   secreted dots                degrades phagocytosed fungi
                                                   │
                                   Requires C-terminal Gag domain (PF30901)
                                   (RTL9ΔC abolishes zymosan degradation)
```

**What RTL9 does (primary function):** It is an **innate-immune effector** that mediates the **lysosomal degradation of fungal cell-wall material (zymosan/β-glucan)** inside brain microglia. It is best classified as a **domesticated retroviral Gag-derived clearance/effector protein**, not an enzyme with a defined EC reaction, a transporter, or a signaling receptor.

**Where it acts (localization):** Intracellularly, in the **lysosomes of microglia** (brain-resident macrophages). This contrasts with its sister genes RTL5/RTL6, which act extracellularly as secreted granules — RTL9 is the **intracellular** member of the trio.

**Pathway context:** RTL9 functions within **innate antifungal immunity / phagocytic clearance** in the CNS. The phagocytosis → lysosomal trafficking → degradation axis is the operative pathway. It is specifically the **fungal-PAMP-handling** component, complementing (but distinct from) classical fungal-sensing pathways such as Dectin-1/β-glucan signaling. The evidence places RTL9 at the **effector/degradation** step rather than the receptor/signaling step.

**Why the Gag domain matters:** The retroviral capsid-like fold is the **essential functional unit** (RTL9ΔC loses activity). Evolutionarily, capsid proteins oligomerize and bind macromolecules; this biochemical capacity appears to have been exapted for engaging fungal polysaccharide and/or organizing its lysosomal degradation.

---

## Evidence Base

| PMID | Study (short) | Relevance to RTL9 function | Strength |
|---|---|---|---|
| [37834332](https://pubmed.ncbi.nlm.nih.gov/37834332/) | Shiura et al. 2023, *IJMS* — RTL9 gene | **Primary functional evidence.** RTL9-mCherry knock-in: lysosomal localization in microglia; degrades zymosan; RTL9ΔC loses activity → Gag domain essential | **High** (direct, in vivo, loss-of-function) |
| [37892118](https://pubmed.ncbi.nlm.nih.gov/37892118/) | Kaneko-Ishino & Ishino 2023, *Biomolecules* — RTL/SIRH review | Establishes RTL9 = SIRH10 = 1 of 11 domesticated retroviral Gag genes; antifungal member of microglial trio | High (authoritative review) |
| [42511665](https://pubmed.ncbi.nlm.nih.gov/42511665/) | Irie et al. 2026 review — virus-derived genes in microglia | Independent confirmation: SIRH10/RTL9 mediates innate immunity against fungal PAMPs | High (independent review) |
| [36162816](https://pubmed.ncbi.nlm.nih.gov/36162816/) | Irie et al. 2022, *Development* — RTL5 & RTL6 | **Mechanistic framework** for the family: microglial Gag proteins directly respond to PAMPs; first demonstration of retrovirus-derived innate immunity in eutherian brain | High (direct, in vivo) |
| [25888968](https://pubmed.ncbi.nlm.nih.gov/25888968/) | Mart-gene placentogenesis survey | Rgag1/Mart9 undetectable in placenta → RTL9 is spatially restricted, no placental role | Moderate (expression) |

**Incidental / non-functional literature (RGAG1 as a genomic locus — not function):** RGAG1-BCOR gene fusions in sarcomas ([PMID: 34331570](https://pubmed.ncbi.nlm.nih.gov/34331570/), [PMID: 32156473](https://pubmed.ncbi.nlm.nih.gov/32156473/)); Xq22.3-q23 deletion syndromes including RGAG1 as a bystander ([PMID: 23520119](https://pubmed.ncbi.nlm.nih.gov/23520119/)); testicular germ-cell-tumor DNA-methylation dysregulation of RGAG1 ([PMID: 20051947](https://pubmed.ncbi.nlm.nih.gov/20051947/)); and an RGAG1 association signal with LDL cholesterol in UK10K ([PMID: 26367797](https://pubmed.ncbi.nlm.nih.gov/26367797/)). These report the locus but **do not characterize the protein's biochemical function** and should not be over-interpreted as functional evidence.

---

## Limitations and Knowledge Gaps

1. **Species gap between function and human expression.** The direct functional evidence (lysosomal antifungal activity in microglia) comes from **mouse** models ([PMID: 37834332](https://pubmed.ncbi.nlm.nih.gov/37834332/)). In humans, the transcript is reported as **testis-enriched** (Human Protein Atlas), and no human in-brain functional study exists. The strong Gag-domain conservation (~78% identity) supports — but does not prove — transfer of function to humans. Human microglial expression and activity need direct confirmation.

2. **No defined enzymatic mechanism.** It remains unresolved whether RTL9 itself catalyzes degradation, directly binds β-glucan via its capsid fold, or acts as a scaffold/adapter that recruits lysosomal hydrolases. The term "degrades zymosan" describes the phenotype, not a proven catalytic reaction; no EC number or substrate kinetics are available.

3. **The N-terminus (res 1–1238) is uncharacterized.** The vast majority of the protein lies outside the Gag domain and has no annotated function or structure. Whether it contributes to targeting, oligomerization, or substrate engagement is unknown.

4. **No experimental human subcellular localization.** Lysosomal localization is established in mouse microglia; the human protein's localization has not been experimentally determined.

5. **Sparse primary literature.** Functional understanding rests heavily on a small number of papers from a single research group. Independent replication would strengthen confidence.

6. **Clinical significance unclear.** Genomic associations (BCOR fusions, Xq deletions, TGCT methylation, LDL GWAS) are not mechanistically linked to the antifungal function and may be incidental to the locus.

---

## Proposed Follow-up Experiments / Actions

1. **Confirm human microglial expression and localization.** Immunostain human brain microglia (and iPSC-derived microglia) for RTL9; use fractionation/confocal co-localization with lysosomal markers (LAMP1/2) to test whether the mouse lysosomal localization is conserved.

2. **Reconstitute the antifungal activity in human cells.** Express human RTL9 and RTL9ΔC in human macrophage/microglial lines, challenge with fluorescent zymosan/β-glucan, and quantify lysosomal degradation to confirm the Gag domain requirement in the human ortholog.

3. **Define the biochemical mechanism.** Test direct binding of purified RTL9 Gag domain to β-1,3-glucan/zymosan (pulldown, ITC, SPR); determine whether RTL9 possesses intrinsic hydrolytic activity or acts as a scaffold recruiting glucanases/cathepsins (proximity proteomics / BioID in lysosomes).

4. **Structural characterization.** Solve or predict (AlphaFold) the structure of the RTL9 C-terminal Gag domain and compare to PEG10/RTL1 capsids; probe whether it oligomerizes and whether a putative polysaccharide-binding surface exists.

5. **Dissect the N-terminal region.** Use truncation/domain-swap constructs and disorder-aware analysis to assign any role (trafficking, oligomerization) to residues 1–1238.

6. **In vivo infection models.** Challenge Rtl9-knockout vs. wild-type mice with live neurotropic fungi (e.g., *Candida*, *Cryptococcus*) to test whether RTL9 confers resistance to genuine CNS fungal infection, beyond model zymosan.

7. **Reconcile testis expression.** Investigate whether RTL9 has a second, germline-specific role in testis (e.g., in spermatogenesis or control of endogenous retroelements), which could explain the human expression pattern.

---

## Conclusion

RTL9/RGAG1/SIRH10 (Q8NET4) is a **domesticated Ty3/Gypsy sushi-ichi retrotransposon Gag-derived gene**, X-linked (Xq23), encoding a 1388-aa protein whose sole functional module is a **C-terminal retroviral Gag/capsid-like domain** (PF30901). Its **primary function is innate antifungal immunity**: in brain **microglia** it localizes to **lysosomes** and mediates the **degradation of phagocytosed fungal cell-wall material (zymosan/β-glucan)**, an activity that **requires the Gag domain** (demonstrated by RTL9-mCherry knock-in and RTL9ΔC loss-of-function in mice). It is the **antifungal member of a eutherian-specific microglial innate-immune trio** (RTL5→viruses, RTL6→bacteria, RTL9→fungi) and is distinctive in acting **intracellularly at the lysosome** rather than as an extracellular granule, an enzyme with a defined EC reaction, a transporter, or a signaling receptor. Strong human–mouse Gag-domain conservation (~78% identity) supports conservation of this function in humans, though direct human functional validation remains an important gap.


## Artifacts

- [OpenScientist final report](RTL9-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](RTL9-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:37834332
2. PMID:42511665
3. PMID:37892118
4. PMID:25888968
5. PMID:36162816
6. PMID:34331570
7. PMID:32156473
8. PMID:23520119
9. PMID:20051947
10. PMID:26367797