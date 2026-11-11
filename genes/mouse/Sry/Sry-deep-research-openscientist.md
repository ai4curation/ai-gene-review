---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-24T04:14:57.297910'
end_time: '2026-10-24T04:45:30.054449'
duration_seconds: 1832.76
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: mouse
  gene_id: Sry
  gene_symbol: Sry
  uniprot_accession: Q05738
  protein_description: 'RecName: Full=Sex-determining region Y protein {ECO:0000303|PubMed:1518820};
    AltName: Full=Testis-determining factor {ECO:0000250|UniProtKB:Q05066};'
  gene_info: Name=Sry {ECO:0000303|PubMed:1518820, ECO:0000312|MGI:MGI:98660}; Synonyms=Tdf
    {ECO:0000250|UniProtKB:Q05066}, Tdy {ECO:0000312|MGI:MGI:98660};
  organism_full: Mus musculus (Mouse).
  protein_family: Belongs to the SRY family. .
  protein_domains: HMG_box_dom. (IPR009071); HMG_box_dom_sf. (IPR036910); SRY-related_HMG-box_TF-like.
    (IPR050140); HMG_box (PF00505)
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
citation_count: 22
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Sry-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Sry-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q05738
- **Protein Description:** RecName: Full=Sex-determining region Y protein {ECO:0000303|PubMed:1518820}; AltName: Full=Testis-determining factor {ECO:0000250|UniProtKB:Q05066};
- **Gene Information:** Name=Sry {ECO:0000303|PubMed:1518820, ECO:0000312|MGI:MGI:98660}; Synonyms=Tdf {ECO:0000250|UniProtKB:Q05066}, Tdy {ECO:0000312|MGI:MGI:98660};
- **Organism (full):** Mus musculus (Mouse).
- **Protein Family:** Belongs to the SRY family. .
- **Key Domains:** HMG_box_dom. (IPR009071); HMG_box_dom_sf. (IPR036910); SRY-related_HMG-box_TF-like. (IPR050140); HMG_box (PF00505)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Sry" matches the protein description above**
2. **Verify the organism is correct:** Mus musculus (Mouse).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Sry' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Sry** (gene ID: Sry, UniProt: Q05738) in mouse.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: Mouse *Sry* (Q05738)

**Gene:** *Sry* (Sex-determining region Y; synonyms *Tdf*, *Tdy*)
**Protein:** Sex-determining region Y protein / Testis-determining factor
**UniProt:** Q05738 | **Organism:** *Mus musculus* (mouse)
**Protein family:** SRY family (HMG-box superfamily)
**Key domains:** HMG box (PF00505; IPR009071, IPR036910); SRY-related HMG-box TF-like (IPR050140)

---

## Identity Verification

Before research, gene identity was confirmed. The gene symbol **"Sry"** matches the UniProt protein description ("Sex-determining region Y protein; Testis-determining factor"), the organism is **Mus musculus**, and the literature retrieved describes a **Y-chromosome-encoded HMG-box transcription factor that triggers testis development** — fully consistent with the PF00505 HMG box domain and the SRY protein family annotation. No conflicting literature for a different gene bearing the same symbol was encountered. The research target is unambiguous and well-characterized; mouse *Sry* is in fact one of the most intensively studied developmental switch genes in mammalian biology. This report proceeds with high confidence in gene identity.

---

## Summary

Mouse **Sry (Q05738) is the master genetic switch that initiates male sex determination.** It encodes a Y-chromosome-linked, sequence-specific DNA-binding protein of the **High-Mobility-Group (HMG) box** family whose singular developmental job is to divert the bipotential (sexually indifferent) embryonic gonad away from the default ovarian fate and toward testis formation. It accomplishes this by committing the supporting-cell precursor lineage of the genital ridge to become **Sertoli cells** rather than ovarian follicle (granulosa) cells. The landmark demonstration of its sufficiency was the generation of phenotypically male XX mice carrying only a 14-kb *Sry*-containing transgene ([PMID: 2030730](https://pubmed.ncbi.nlm.nih.gov/2030730/)).

At the molecular level, SRY is an **architectural transcription factor**. Its HMG box binds the **minor groove** of DNA in a sequence-specific manner and sharply **bends the double helix (~54° in the human complex)**, remodeling local chromatin architecture. Its primary, direct, physiologically validated target is a gonad-specific enhancer of *Sox9* (**TESCO / Enh13**), which it binds cooperatively with the orphan nuclear receptor **SF1 (NR5A1)** to up-regulate *Sox9* transcription ([PMID: 18454134](https://pubmed.ncbi.nlm.nih.gov/18454134/)). SRY acts **transiently in the nuclei** of internal pre-Sertoli cells during a narrow developmental window (~10.5–12.5 dpc in mouse), after which SOX9 sustains its own expression through a feed-forward loop, and SRY is no longer required. SRY therefore sits at the **apex of the testis-determining gene-regulatory network (SRY → SOX9 → FGF9)**, which is mutually antagonistic to the ovary-determining network (RSPO1–WNT4–β-catenin–FOXL2).

Three features make the **mouse** protein distinctive relative to other mammals: (1) it carries a **glutamine-rich (CAG-repeat) C-terminal trans-activation domain** essential for function in vivo; (2) the genuine testis-determining molecule is a recently evolved, stabilized **two-exon isoform (SRY-T)** that escapes a C-terminal degron present in the canonical single-exon form; and (3) its activity depends on regulated **nuclear import** (calmodulin- and importin-β-mediated) and on timely, threshold-level expression driven by upstream **GADD45γ–MAP3K4–p38 MAPK–GATA4** signaling. SRY evolved by truncation of the X-linked neural gene *SOX3*, which explains its shared HMG box and its otherwise rapid, lineage-specific divergence.

---

## Key Findings

### 1. Sry is the master trigger of testis determination via Sertoli cell induction

Genetic and transgenic data firmly establish *Sry* on the Y chromosome as the dominant male determinant. Its defined role in sex determination is to **initiate testis rather than ovary development** from the early bipotential gonad. Mechanistically, it does so by **triggering the differentiation of Sertoli cells from supporting-cell precursors** — the precursor pool that, in the absence of *Sry*, would instead give rise to ovarian follicle (granulosa) cells ([PMID: 18454134](https://pubmed.ncbi.nlm.nih.gov/18454134/)). *Sry* is described as a newly evolved gene on the Y chromosome that acts as the **primary trigger for mammalian sex determination** ([PMID: 25725066](https://pubmed.ncbi.nlm.nih.gov/25725066/)).

> *"...whose role in sex determination is to initiate testis rather than ovary development from early bipotential gonads. It does so by triggering the differentiation of Sertoli cells from supporting cell precursors, which would otherwise give follicle cells"* — Sekido & Lovell-Badge ([PMID: 18454134](https://pubmed.ncbi.nlm.nih.gov/18454134/))

The Sertoli cell is the key organizing cell of the testis: once specified, it directs the morphogenesis of testis cords, recruits and organizes other testicular cell types, and secretes anti-Müllerian hormone (AMH). Thus SRY's role is not to build the whole testis directly but to flip a single cell-fate switch in one lineage, which then cascades into the entire male developmental program.

### 2. Sry directly binds a gonad-specific Sox9 enhancer with SF1 to up-regulate Sox9

SRY is a **transcription factor** whose critical, directly validated target is *Sox9*. In mouse gonads, SRY binds **multiple elements within a Sox9 gonad-specific enhancer** (TES/TESCO, overlapping the Enh13 element) together with **steroidogenic factor 1 (SF1 / NR5A1)**, an orphan nuclear receptor, and the two cooperatively up-regulate *Sox9* ([PMID: 18454134](https://pubmed.ncbi.nlm.nih.gov/18454134/)). This was independently confirmed across mouse and human: *"SRY proteins bind to the testis-specific enhancer of SOX9 (TES) with SF1 to upregulate SOX9 expression in undifferentiated gonads of XY embryos of humans and mice"* ([PMID: 25265165](https://pubmed.ncbi.nlm.nih.gov/25265165/)). Loss of the SRY/SF1 binding sites abolishes enhancer activity.

Critically, once SOX9 reaches a threshold, **SOX9 itself binds the same enhancer** (together with SF1), establishing a **feed-forward, self-reinforcing loop** that maintains *Sox9* expression after *Sry* expression has ceased:

> *"...a feedforward, self-reinforcing pathway in which SF1 and SRY cooperatively upregulate Sox9 and then, together with SF1, SOX9 also binds to the enhancer to help maintain its own expression after that of SRY has ceased"* — ([PMID: 18454134](https://pubmed.ncbi.nlm.nih.gov/18454134/))

This explains how a transiently expressed protein can irreversibly commit a cell lineage: SRY is the match that lights the fire, and SOX9 is the fuel that keeps it burning.

### 3. Sry is an HMG-box architectural factor that bends DNA in the minor groove

The sole conserved functional module of SRY is the **HMG box**, an alpha-helical DNA-binding domain that binds within an **expanded minor groove** and induces substantial **DNA bending** ([PMID: 16504207](https://pubmed.ncbi.nlm.nih.gov/16504207/)). The human SRY–DNA complex bends DNA by **~54°**. Raman spectroscopy of the SRY-HMG:DNA complex independently confirmed the structural signature of HMG-box binding: **minor-groove expansion, sharp bending toward the major groove, and local unwinding** of the double helix ([PMID: 10642178](https://pubmed.ncbi.nlm.nih.gov/10642178/)).

The functional importance of this DNA-bending activity is proven by human disease genetics: *"...binds DNA sequence-specifically in the minor groove, resulting in substantial DNA bending. The majority of point mutations resulting in 46X,Y sex reversal are located within this domain"* ([PMID: 11563911](https://pubmed.ncbi.nlm.nih.gov/11563911/)). A clinically characterized point mutation (M64I) that **reduces the bend angle by ~13°** causes XY sex reversal, directly linking the biophysical property (bending) to the biological outcome (male development). A **basic C-terminal tail** flanking the HMG box acts both as a **kinetic clamp that augments DNA bending** and as a **nuclear localization signal** ([PMID: 16504207](https://pubmed.ncbi.nlm.nih.gov/16504207/)). SRY therefore functions less like a classical activator that merely recruits polymerase and more like an **architectural remodeler** that reshapes the enhancer to nucleate an active transcriptional complex.

### 4. Mouse Sry uniquely requires a glutamine-rich (CAG-repeat) trans-activation domain

Whereas in most mammals only the HMG box is conserved, **Mus musculus Sry** carries a large **CAG trinucleotide-repeat region** encoding a **C-terminal glutamine-rich domain** that functions as a transcriptional **trans-activator** in vitro ([PMID: 10431249](https://pubmed.ncbi.nlm.nih.gov/10431249/)). Transgenic truncation experiments proved this domain is **essential in vivo**: *Sry* constructs lacking the glutamine-rich region **failed to induce male sex determination** in XX embryos, whereas wild-type constructs succeeded.

> *"Sry constructs that encode proteins lacking the glutamine-rich region were unable to effect male sex determination, in contrast to their wild-type counterparts"* — Bowles et al. ([PMID: 10431249](https://pubmed.ncbi.nlm.nih.gov/10431249/))

This makes the mouse protein a **genuine transcriptional activator**, not merely an architectural/DNA-bending factor — a mechanistically important distinction from human SRY, where the activation function is thought to be supplied largely by partner proteins such as SF1.

### 5. The bona fide mouse determinant is the stabilized two-exon isoform SRY-T

A major recent revision (2020) to the mouse story: *Sry* was long assumed to be a **single-exon** gene, but it in fact possesses a **cryptic second exon** generating a two-exon transcript, **Sry-T**. Functional proof is definitive: *"XY mice lacking Sry-T were sex-reversed, and ectopic expression of Sry-T in XX mice induced male development"* ([PMID: 33004521](https://pubmed.ncbi.nlm.nih.gov/33004521/)). Although the *Sry-T* and canonical single-exon *Sry-S* mRNAs are expressed at similar levels, the **SRY-T protein predominates** because SRY-S carries a **C-terminal degron** that targets it for degradation; exon 2 arose recently in mice from a **retrotransposon-derived coding sequence** that replaced the degron, stabilizing the protein.

> *"Our findings suggest that in nature, SRY-T, not SRY-S, is the bona fide testis-determining factor"* — Miyawaki et al. ([PMID: 33004521](https://pubmed.ncbi.nlm.nih.gov/33004521/))

This finding refines the molecular identity of the functional protein and highlights **post-translational stability** as a decisive layer of regulation in mouse sex determination. (Note: the citation snippets for this finding were flagged as sequence-"mismatch" against the stored abstract record, likely because the full abstract text was not indexed; the *Science* paper PMID 33004521 is nonetheless the correct and authoritative source.)

### 6. SRY requires regulated nuclear import (calmodulin / importin-β)

To function, SRY must enter the nucleus. Its HMG domain is flanked by **two independent nuclear localization signals (NLSs)**: an N-terminal **CaM-NLS** recognized by **calmodulin (CaM)**, and a C-terminal **β-NLS** recognized by **importin-β1** ([PMID: 21558314](https://pubmed.ncbi.nlm.nih.gov/21558314/), [PMID: 21051653](https://pubmed.ncbi.nlm.nih.gov/21051653/)). The two import pathways are mutually exclusive and switched by **intracellular Ca²⁺**. The physiological relevance was demonstrated directly in mouse gonad culture: treating sexually indifferent XY mouse fetal gonads with a CaM antagonist **reduced Sox9 expression, caused defects in testicular cord formation, and induced ectopic ovarian markers (Rspo1, Foxl2)**:

> *"CaM antagonist treatment of cultured, sexually indifferent XY mouse fetal gonads led to reduced expression of the Sry target gene Sox9, defects in testicular cord formation, and ectopic expression of the ovarian markers Rspondin1 and forkhead box L2"* — Sim et al. ([PMID: 21558314](https://pubmed.ncbi.nlm.nih.gov/21558314/))

NLS mutations found in XY sex-reversed human females impair SRY nuclear import ([PMID: 15746192](https://pubmed.ncbi.nlm.nih.gov/15746192/)), confirming that **subcellular localization is itself a point of functional control and of disease**.

### 7. Timely, threshold-level Sry expression is set by GADD45γ–MAP3K4–p38 MAPK–GATA4

SRY's function is exquisitely sensitive to **timing and dose**. Upstream control is provided by a kinase cascade: loss of **MAP3K4** causes mouse XY gonadal sex reversal due to **reduced Sry expression**, and mice lacking **Gadd45γ** show the identical phenotype. *Gadd45γ* is expressed in gonadal somatic cells from 10.5–12.5 dpc, genetically interacts with *Map3k4* (MAP3K4 overexpression rescues *Gadd45γ*-null gonads), and sex reversal in both mutants is associated with **reduced phosphorylation of p38 MAPK and of the transcription factor GATA4**; embryos lacking both p38α and p38β also undergo XY sex reversal ([PMID: 23102580](https://pubmed.ncbi.nlm.nih.gov/23102580/)).

> *"...our data suggest a requirement for GADD45γ in promoting MAP3K4-mediated activation of p38 MAPK signaling in embryonic gonadal somatic cells for testis determination in the mouse"* — Warr et al. ([PMID: 23102580](https://pubmed.ncbi.nlm.nih.gov/23102580/))

GATA4 (with its partner FOG2) is a key activator that drives *Sry* transcription; the GADD45γ–MAP3K4–p38 cascade converges on GATA4 to ensure *Sry* is switched on at the right place, time, and level.

### 8. Sry evolved by truncation of SOX3

SRY arose evolutionarily by **truncation of SOX3**, an X-linked gene expressed in brain development ([PMID: 12438793](https://pubmed.ncbi.nlm.nih.gov/12438793/)). Outside the HMG box, SRY is poorly conserved, and its mode of action has demonstrably changed in the mouse lineage; in some rodents SRY has even been inactivated or superseded by other mechanisms. This evolutionary origin elegantly explains the shared HMG box between SRY and the SOX family, as well as the rapid divergence of the flanking sequence — including the mouse-specific glutamine-rich domain and the retrotransposon-derived exon 2.

> *"The mammalian testis-determining gene, SRY, is a typical Y-borne gene. It arose by truncation of a gene (SOX3) on the X that is expressed in brain development"* — Marshall Graves ([PMID: 12438793](https://pubmed.ncbi.nlm.nih.gov/12438793/))

### 9. Spatiotemporal expression: transient, cell-autonomous action in internal pre-Sertoli cells

In the mouse genital ridge, *Sry* is transcribed in a **dynamic centre-to-pole wave**, emanating from central/anterior regions, spreading to both poles, and ending caudally ([PMID: 11376487](https://pubmed.ncbi.nlm.nih.gov/11376487/)). It is expressed in **internal (supporting-cell precursor) cells but NOT in the coelomic surface epithelium**, indicating that its effect on surface-cell proliferation is non-cell-autonomous while its Sertoli-specifying role is cell-autonomous. Its direct target *Sox9* is expressed male-specifically, localized to the developing sex cords and **specific to the Sertoli cell lineage** (absent from germ cells) ([PMID: 8787755](https://pubmed.ncbi.nlm.nih.gov/8787755/)). The tight temporal window and cell-type specificity are consistent with direct regulation of *Sox9* by SRY.

> *"Sry is expressed in internal cells but not in coelomic surface epithelial cells, indicating that its effect on proliferation of surface cells is achieved non-cell-autonomously"* — Bullejos & Koopman ([PMID: 11376487](https://pubmed.ncbi.nlm.nih.gov/11376487/))

### 10. A single Sry gene is sufficient to switch female to male development

The foundational genetic proof: introduction of mouse *Sry* on a **14-kb genomic DNA fragment** into chromosomally female (XX) mouse embryos was **sufficient to induce testis differentiation and subsequent male development** ([PMID: 2030730](https://pubmed.ncbi.nlm.nih.gov/2030730/); reviewed [PMID: 27190031](https://pubmed.ncbi.nlm.nih.gov/27190031/)). This single experiment ("Randy," the sex-reversed mouse) is the definitive demonstration that *Sry* is the mammalian testis-determining gene.

> *"It is now shown that Sry on a 14-kilobase genomic DNA fragment is sufficient to induce testis differentiation and subsequent male development when introduced into chromosomally female mouse embryos"* — Koopman et al. ([PMID: 2030730](https://pubmed.ncbi.nlm.nih.gov/2030730/))

---

## Mechanistic Model

The findings assemble into a coherent, well-supported model of SRY action, spanning upstream regulation, molecular function, and downstream network output:

```
  UPSTREAM SIGNALING (sets timing & dose of Sry)
  ┌─────────────────────────────────────────────────────────┐
  │  GADD45γ ─► MAP3K4 ─► p38α/β MAPK ─► GATA4 (+FOG2)        │
  └───────────────────────────────┬─────────────────────────┘
                                   │ activates transcription
                                   ▼
                          ┌──────────────────┐
                          │   Sry (Sry-T)    │  Y chromosome
                          │  two-exon, stable│  (escapes degron)
                          └────────┬─────────┘
                                   │ translation
                                   ▼
             Cytoplasm  ──  SRY protein  ── regulated nuclear import
                            (CaM-NLS / importin-β-NLS; Ca²⁺ switch)
                                   │
                                   ▼  NUCLEUS of internal pre-Sertoli cell
                          ┌─────────────────────────────────┐
             SF1/NR5A1 ──►│  Sox9 enhancer (TESCO / Enh13)  │
                          │  SRY HMG box bends DNA ~54°      │
                          │  minor-groove binding + Q-rich   │
                          │  trans-activation domain (mouse) │
                          └────────────────┬────────────────┘
                                           │ up-regulates
                                           ▼
                                    ┌────────────┐
                                    │   Sox9     │◄──┐ feed-forward
                                    └─────┬──────┘   │ (SOX9+SF1 bind
                                          │          │  enhancer; SRY
                                          │──────────┘  no longer needed)
                                          ▼
                     TESTIS NETWORK:  SOX9 ─► FGF9/FGFR2, PGD2, AMH, DMRT1
                                          │
                                          │  mutual antagonism
                                          ▼
                     OVARY NETWORK (repressed): RSPO1–WNT4–β-catenin–FOXL2

  OUTCOME: Supporting-cell precursor ──► SERTOLI CELL ──► testis cords ──► TESTIS
```

**Narrative:** In the bipotential gonad, upstream GADD45γ–MAP3K4–p38–GATA4 signaling ensures *Sry* is expressed at a sufficient threshold in a tight ~10.5–12.5 dpc window within internal supporting-cell precursors. The stabilized SRY-T protein is imported into the nucleus via CaM/importin-β pathways, where its HMG box binds and sharply bends the minor groove of the *Sox9* TESCO/Enh13 enhancer. Acting cooperatively with SF1 — and, in mouse, supplying its own activation function through the glutamine-rich domain — SRY up-regulates *Sox9*. Once SOX9 crosses a threshold it, together with SF1, binds the same enhancer in a feed-forward loop, locking in *Sox9* expression independently of SRY. SOX9 then drives the testis gene-regulatory network (FGF9, PGD2, AMH, DMRT1), which mutually antagonizes the ovary-determining RSPO1–WNT4–β-catenin–FOXL2 network ([PMID: 24643063](https://pubmed.ncbi.nlm.nih.gov/24643063/), [PMID: 32099981](https://pubmed.ncbi.nlm.nih.gov/32099981/)). The precursor cell is thereby committed to the Sertoli fate, and the entire male developmental program follows.

### Functional annotation at a glance

| Attribute | Annotation | Evidence |
|---|---|---|
| **Molecular function** | Sequence-specific DNA-binding transcription factor; architectural DNA-bending (HMG box) | [PMID: 16504207](https://pubmed.ncbi.nlm.nih.gov/16504207/), [PMID: 11563911](https://pubmed.ncbi.nlm.nih.gov/11563911/) |
| **Primary direct target** | *Sox9* gonad-specific enhancer (TESCO/Enh13), with SF1 | [PMID: 18454134](https://pubmed.ncbi.nlm.nih.gov/18454134/), [PMID: 25265165](https://pubmed.ncbi.nlm.nih.gov/25265165/) |
| **Reaction/activity** | Not an enzyme; activates transcription (mouse requires Q-rich trans-activation domain) | [PMID: 10431249](https://pubmed.ncbi.nlm.nih.gov/10431249/) |
| **Subcellular localization** | Nucleus (regulated import via CaM-NLS / importin-β-NLS) | [PMID: 21558314](https://pubmed.ncbi.nlm.nih.gov/21558314/), [PMID: 21051653](https://pubmed.ncbi.nlm.nih.gov/21051653/) |
| **Cell type / tissue** | Internal pre-Sertoli supporting-cell precursors, embryonic genital ridge | [PMID: 11376487](https://pubmed.ncbi.nlm.nih.gov/11376487/) |
| **Timing** | Transient, ~10.5–12.5 dpc; centre-to-pole wave | [PMID: 11376487](https://pubmed.ncbi.nlm.nih.gov/11376487/) |
| **Biological process** | Male sex determination; Sertoli cell differentiation; testis development | [PMID: 18454134](https://pubmed.ncbi.nlm.nih.gov/18454134/), [PMID: 2030730](https://pubmed.ncbi.nlm.nih.gov/2030730/) |
| **Pathway position** | Apex of SRY→SOX9→FGF9 testis network; antagonizes ovarian network | [PMID: 24643063](https://pubmed.ncbi.nlm.nih.gov/24643063/) |
| **Upstream regulation** | GADD45γ–MAP3K4–p38 MAPK–GATA4 | [PMID: 23102580](https://pubmed.ncbi.nlm.nih.gov/23102580/) |
| **Functional isoform (mouse)** | SRY-T (two-exon, degron-free, stabilized) | [PMID: 33004521](https://pubmed.ncbi.nlm.nih.gov/33004521/) |
| **Evolutionary origin** | Truncation of X-linked SOX3 | [PMID: 12438793](https://pubmed.ncbi.nlm.nih.gov/12438793/) |

---

## Evidence Base

| PMID | Study | Contribution | Weight |
|---|---|---|---|
| [2030730](https://pubmed.ncbi.nlm.nih.gov/2030730/) | Koopman et al. 1991, *Nature* | 14-kb *Sry* transgene masculinizes XX mice — proof of **sufficiency** | Definitive primary |
| [18454134](https://pubmed.ncbi.nlm.nih.gov/18454134/) | Sekido & Lovell-Badge 2008, *Nature* | SRY+SF1 bind *Sox9* enhancer; feed-forward loop — **direct target** | Definitive primary |
| [33004521](https://pubmed.ncbi.nlm.nih.gov/33004521/) | Miyawaki et al. 2020, *Science* | SRY-T two-exon isoform is the true determinant; degron biology | Definitive primary |
| [16504207](https://pubmed.ncbi.nlm.nih.gov/16504207/) | Phillips et al. 2006 | HMG box minor-groove binding, DNA bending, basic tail clamp/NLS | Strong structural |
| [11563911](https://pubmed.ncbi.nlm.nih.gov/11563911/) | Murphy et al. 2001 | Bend-angle reduction (M64I) causes XY sex reversal | Strong structure–function |
| [10642178](https://pubmed.ncbi.nlm.nih.gov/10642178/) | Benevides et al. 2000 | Raman spectroscopy: minor-groove expansion, bending, unwinding | Independent biophysical |
| [10431249](https://pubmed.ncbi.nlm.nih.gov/10431249/) | Bowles et al. 1999 | Mouse-specific Q-rich domain required in vivo | Strong primary |
| [21558314](https://pubmed.ncbi.nlm.nih.gov/21558314/) | Sim et al. 2011 | CaM-dependent nuclear import required for testis differentiation | Strong functional |
| [21051653](https://pubmed.ncbi.nlm.nih.gov/21051653/) | Kaur & Jans 2010/11 | Dual NLS mechanism; Ca²⁺ as import switch | Strong mechanistic |
| [15746192](https://pubmed.ncbi.nlm.nih.gov/15746192/) | Sim et al. 2005 | NLS mutations impair import in XY sex reversal | Supporting (human) |
| [23102580](https://pubmed.ncbi.nlm.nih.gov/23102580/) | Warr et al. 2012 | GADD45γ–MAP3K4–p38–GATA4 controls *Sry* | Strong genetic |
| [11376487](https://pubmed.ncbi.nlm.nih.gov/11376487/) | Bullejos & Koopman 2001 | Dynamic expression wave; cell-autonomy | Strong primary |
| [8787755](https://pubmed.ncbi.nlm.nih.gov/8787755/) | Kent et al. 1996 | *Sox9* is Sertoli-lineage-specific | Supporting |
| [24643063](https://pubmed.ncbi.nlm.nih.gov/24643063/) | Carré & Greenfield 2014 | Antagonistic testis vs. ovary networks | Review |
| [32099981](https://pubmed.ncbi.nlm.nih.gov/32099981/) | Cen et al. 2020 | Downstream testis/ovary factor inventory | Review |
| [25265165](https://pubmed.ncbi.nlm.nih.gov/25265165/) | Kimura et al. 2014 | SRY+SF1 at TES conserved mouse/human | Comparative |
| [12438793](https://pubmed.ncbi.nlm.nih.gov/12438793/) | Marshall Graves 2002 | SRY evolved by SOX3 truncation | Review/evolution |
| [25725066](https://pubmed.ncbi.nlm.nih.gov/25725066/) | Zhao et al. 2015 | *Sry* as primary trigger; Dmrt1 context | Supporting primary |
| [27190031](https://pubmed.ncbi.nlm.nih.gov/27190031/) | Koopman et al. 2016 | Retrospective review of the sex-reversed mouse | Review |

The evidence base is unusually strong and multi-layered: **genetic sufficiency** (transgenic XX→male mice), **direct biochemical target identification** (enhancer binding, ChIP), **structural/biophysical mechanism** (crystallography, Raman spectroscopy, bend-angle quantification), **clinical validation** (human sex-reversal point mutations map to the HMG box and NLSs), and **in vivo gonad-culture perturbation** (CaM antagonists). Importantly, the primary molecular function is established by **precise, low-throughput studies**, exactly the class of evidence prioritized in this annotation.

---

## Limitations and Knowledge Gaps

1. **Direct activation vs. architectural facilitation.** Mouse SRY has a glutamine-rich trans-activation domain and behaves as a bona fide activator, but the precise contribution of DNA bending versus direct transcriptional activation at the *Sox9* enhancer in vivo has not been fully dissected. Some human SRY activity depends on partner proteins (SF1), raising a mouse–human mechanistic distinction that remains incompletely quantified.

2. **Full target repertoire.** *Sox9* is the one rigorously validated, physiologically essential direct target. Other candidate targets have been proposed (e.g., *CATSPER1* promoter regulation by SRY, [PMID: 30379860](https://pubmed.ncbi.nlm.nih.gov/30379860/)), but a genome-wide, developmentally timed, in vivo SRY binding map (ChIP-seq from sorted pre-Sertoli cells) is still lacking given the very small number of SRY-expressing cells and the brief window.

3. **cis-regulation of *Sry* itself.** The 5′ regulatory sequences driving correct *Sry* expression remain unmapped; single-copy transgenes within 8 kb of the TSS failed to recapitulate expression ([PMID: 24743337](https://pubmed.ncbi.nlm.nih.gov/24743337/)), indicating essential elements lie elsewhere or require native chromatin context.

4. **SRY-T biology is new.** The two-exon SRY-T isoform ([PMID: 33004521](https://pubmed.ncbi.nlm.nih.gov/33004521/)) reframes the functional protein, but the biochemistry of the exon-2-encoded C-terminus (beyond degron removal) — whether it adds new interaction surfaces or activity — is not yet characterized. (The citation snippets for this finding were flagged as a text "mismatch" during validation, warranting a careful re-read of the primary paper.)

5. **Threshold and timing quantification.** While GADD45γ–MAP3K4–p38–GATA4 clearly sets *Sry* dose/timing, the exact molecular threshold of SRY/SOX9 needed to tip the bistable switch, and how developmental noise is buffered, remains quantitatively underdefined.

6. **Species-specificity of structural data.** Many structural and NLS data derive from **human** SRY; while the HMG box is highly conserved, the mouse-specific Q-rich domain and SRY-T mean some mechanistic details should be confirmed directly in mouse.

---

## Proposed Follow-up Experiments

1. **In vivo SRY-T ChIP-seq / CUT&RUN** from FACS-purified E11.5 XY pre-Sertoli cells (using a tagged SRY-T knock-in) to define the complete, developmentally relevant direct target set and confirm *Sox9*/TESCO occupancy genome-wide.

2. **Separation-of-function mutants** of mouse *Sry*: knock-in alleles that (a) abolish the Q-rich activation domain while preserving DNA bending, and (b) reduce bend angle while preserving activation, to dissect architectural vs. activator contributions at the endogenous *Sox9* enhancer.

3. **Quantitative single-cell dynamics**: live imaging of SRY-T and SOX9 reporter thresholds in gonad explants to measure the bistable switch point and the handoff from SRY to the SOX9 feed-forward loop.

4. **Exon-2 structure–function**: biochemical and structural characterization of the SRY-T C-terminus — identify interaction partners and test whether it contributes activity beyond degron removal.

5. **cis-regulatory mapping of *Sry***: ATAC-seq / enhancer-trap screens across the Y *Sry* locus in E10.5–11.5 gonads to locate the elements integrating GATA4 and p38 signaling.

6. **Reconstitute the upstream cascade** (GADD45γ/MAP3K4/p38/GATA4) in gonadal organ culture ([PMID: 32092744](https://pubmed.ncbi.nlm.nih.gov/32092744/)) with graded perturbation to establish the dose–response relationship that sets the *Sry* expression threshold.

---

## Conclusion

Mouse *Sry* (Q05738) is the archetypal developmental master switch: a Y-linked, HMG-box, DNA-bending transcription factor that acts transiently in the nuclei of embryonic pre-Sertoli cells to directly up-regulate *Sox9* via a gonad-specific enhancer in cooperation with SF1. This single transcriptional event commits the bipotential supporting-cell lineage to the Sertoli (testis) fate, initiating the SOX9–FGF9 network that antagonizes the ovarian program — and a single *Sry* transgene is sufficient to make an XX mouse male. Mouse-specific refinements (the glutamine-rich activation domain, the stabilized SRY-T isoform, CaM/importin-β nuclear import, and GADD45γ–MAP3K4–p38–GATA4 upstream control) tune where, when, how much, and in what form this switch is thrown.


## Artifacts

- [OpenScientist final report](Sry-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Sry-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:2030730
2. PMID:18454134
3. PMID:25725066
4. PMID:25265165
5. PMID:16504207
6. PMID:10642178
7. PMID:11563911
8. PMID:10431249
9. PMID:33004521
10. PMID:21558314
11. PMID:21051653
12. PMID:15746192
13. PMID:23102580
14. PMID:12438793
15. PMID:11376487
16. PMID:8787755
17. PMID:27190031
18. PMID:24643063
19. PMID:32099981
20. PMID:30379860
21. PMID:24743337
22. PMID:32092744