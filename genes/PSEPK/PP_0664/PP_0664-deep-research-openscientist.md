---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-11T08:43:19.688022'
end_time: '2026-08-11T10:37:52.716856'
duration_seconds: 6873.03
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_0664
  gene_symbol: PP_0664
  uniprot_accession: Q88Q34
  protein_description: 'RecName: Full=homoserine dehydrogenase {ECO:0000256|ARBA:ARBA00013213};
    EC=1.1.1.3 {ECO:0000256|ARBA:ARBA00013213};'
  gene_info: OrderedLocusNames=PP_0664 {ECO:0000313|EMBL:AAN66289.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the homoserine dehydrogenase family.
  protein_domains: HDH_cat. (IPR001342); HDH_CS. (IPR019811); HDH_short. (IPR022697);
    NAD(P)-bd_dom_sf. (IPR036291); Homoserine_dh (PF00742)
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
  path: PP_0664-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PP_0664-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88Q34
- **Protein Description:** RecName: Full=homoserine dehydrogenase {ECO:0000256|ARBA:ARBA00013213}; EC=1.1.1.3 {ECO:0000256|ARBA:ARBA00013213};
- **Gene Information:** OrderedLocusNames=PP_0664 {ECO:0000313|EMBL:AAN66289.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the homoserine dehydrogenase family.
- **Key Domains:** HDH_cat. (IPR001342); HDH_CS. (IPR019811); HDH_short. (IPR022697); NAD(P)-bd_dom_sf. (IPR036291); Homoserine_dh (PF00742)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_0664" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_0664' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_0664** (gene ID: PP_0664, UniProt: Q88Q34) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: PP_0664 (Q88Q34), Homoserine Dehydrogenase of *Pseudomonas putida* KT2440

## 1. Summary (Answer to the Research Question)

**PP_0664** (UniProt **Q88Q34**; organism *Pseudomonas putida* strain KT2440) encodes **homoserine dehydrogenase (HSD; EC 1.1.1.3)**, a cytoplasmic NAD(P)H-dependent oxidoreductase of the aspartate-derived amino-acid biosynthetic pathway. Its primary function is to catalyze the reversible reduction of **L-aspartate-4-semialdehyde (ASA) to L-homoserine**, using **NADPH** as the preferred physiological reductant:

> L-aspartate-4-semialdehyde + NAD(P)H + H⁺ ⇌ **L-homoserine** + NAD(P)⁺

This is the **third and committed reductive step of the aspartate pathway** and the metabolic **branch point** that provides homoserine, the common precursor for **threonine (and isoleucine)** and **methionine** biosynthesis. The gene identity, organism, catalyzed reaction and protein family all match the UniProt record; there is no ambiguity in the identification.

---

## 2. Gene / Protein Identity Verification

| Attribute | Value | Source |
|---|---|---|
| UniProt accession | Q88Q34 | UniProt |
| Protein | Homoserine dehydrogenase, EC 1.1.1.3 | UniProt / KEGG K00003 |
| Ordered locus | PP_0664 (EMBL AAN66289.1) | UniProt / KEGG |
| Organism | *P. putida* KT2440 (ATCC 47054 / DSM 6125) | UniProt |
| Length | 347 aa | UniProt |
| Family | Homoserine dehydrogenase family | UniProt |
| Domains | PF00742 (Homoserine_dh); IPR001342 (HDH_cat); IPR022697 (HDH_short); IPR036291 (NAD(P)-binding Rossmann fold); PROSITE PS01042 | UniProt/InterPro |

All identifiers are mutually consistent (UniProt ↔ KEGG `ppu:PP_0664` ↔ KO `K00003` ↔ EC 1.1.1.3). **Verification passed.**

---

## 3. Primary Molecular Function — The Catalyzed Reaction

Homoserine dehydrogenase (HSD, EC 1.1.1.3) catalyzes the NAD(P)H-dependent reduction of the aldehyde group of L-aspartate-4-semialdehyde to the primary alcohol of L-homoserine (the reverse oxidation can also proceed in vitro). HSD is described as "an important regulatory enzyme in the aspartate pathway, which mediates synthesis of methionine, threonine and isoleucine from aspartate" (Ogata et al., 2018, PMID 29636528).

- **Cofactor:** UniProt annotates the enzyme with the keyword **NADP**, indicating NADPH is the physiological reductant; many bacterial HSDs are dual-specificity (NADH/NADPH), but biosynthetic flux uses NADPH.
- **Substrate specificity:** HSD is specific for the aspartate-pathway intermediate L-aspartate-4-semialdehyde/L-homoserine couple. Mechanistic studies of family members show an **ordered sequential mechanism in which the nicotinamide cofactor binds first, followed by the amino-acid substrate** ("StHSD first binds NAD and then homoserine through a sequentially ordered mechanism", Ogata et al., 2018, PMID 29636528).

---

## 4. Domain Architecture, Structure and Cofactor Binding

The 347-residue protein is a **short-form, monofunctional HSD**:

- **N-terminal NAD(P)-binding Rossmann-fold domain** (SUPFAM SSF51735; IPR036291) — binds the nicotinamide cofactor.
- **C-terminal catalytic / dimerization domain** (SUPFAM SSF55347; IPR001342 HDH_cat) — houses the homoserine-binding active site.
- The **HDH_short** signature (IPR022697) and the ~347 aa length indicate this is the **"short" HSD lacking a C-terminal ACT regulatory domain** and **not fused to aspartokinase**, in contrast to *E. coli*'s bifunctional aspartokinase-I–HSD-I (ThrA) and aspartokinase-II–HSD-II (MetL). PP_0664 is therefore a **standalone monofunctional enzyme**.
- HSDs of this family are typically **homodimers/homotetramers**; the active site lies at a domain/subunit interface. Structural work on family members shows the cofactor's nicotinamide ring is positioned adjacent to the substrate C4 atom (~1.9 Å) in the active site (Ogata et al., 2018, PMID 29636528), consistent with direct hydride transfer.

---

## 5. Pathway Context and Biological Process

PP_0664 is embedded in the **aspartate-derived amino-acid biosynthetic network**. KEGG assigns it to:

- **ppu_M00018 — Threonine biosynthesis** (aspartate ⇒ homoserine ⇒ threonine)
- **ppu_M00017 — Methionine biosynthesis** (aspartate ⇒ homoserine ⇒ methionine)
- Pathway maps ppu00260 (Glycine/Serine/Threonine metabolism), ppu00270 (Cysteine/Methionine metabolism), ppu01230 (Biosynthesis of amino acids).
- UniPathway UPA00050 / UPA00051; GO:0009088 (L-threonine biosynthetic process).

**Upstream:** aspartate → (aspartokinase) → aspartyl-4-phosphate → (aspartate-semialdehyde dehydrogenase) → **L-aspartate-4-semialdehyde** → **(PP_0664 / HSD) → L-homoserine**.

**Downstream branch point:** L-homoserine is partitioned between:
- the **threonine/isoleucine branch** (homoserine kinase → threonine synthase → threonine; then to isoleucine), and
- the **methionine branch** (homoserine O-acyltransferase → cystathionine → methionine).

L-aspartate-4-semialdehyde is also the substrate of dihydrodipicolinate synthase feeding **lysine/diaminopimelate** biosynthesis; thus HSD competes with the lysine branch for the shared ASA pool — a classic point of concerted regulation in the aspartate pathway (Shaul & Galili, 1993, PMID 8251629; Eikmanns et al., PMID 8092856). (KEGG lists PP_0664 under ppu00300 "Lysine biosynthesis" only by virtue of the shared ASA node, not because HSD catalyzes a lysine-pathway step.)

**Functional/genetic evidence in KT2440:** A genome-wide transposon-mutant screen of *P. putida* KT2440 recovered **threonine and methionine auxotrophs** ("we also found auxotrophs for proline, serine, threonine and methionine", Molina-Henares et al., 2010, PMID 20158506), consistent with the essential, homoserine-supplying role of this step for both downstream amino acids under minimal-medium (biosynthetic) conditions.

---

## 6. Regulation

Homoserine dehydrogenase is a well-established regulatory/control node of the aspartate pathway. In *E. coli*, control of threonine-pathway flux is shared among aspartate kinase, aspartate-semialdehyde dehydrogenase, and HSD, "with no single activity dominating the control" (Chassagnole et al., 2001, PMID 11368770). In classic *P. putida* biochemistry, the activities of aspartate kinase and homoserine dehydrogenase are modulated by aspartate-family amino acids: studies of ethionine-resistant *P. putida* mutants examined HSD activity "as affected by amino acids from the family of asparagine" and reported altered negative regulation in methionine-overproducing mutants (Polodienko et al., 1991, PMID 2067422; see also Robert-Gero, Poiret & Cohen, "Homoserine dehydrogenase of Pseudomonas putida. Properties and regulation", 1970, PMID 5441405). Because PP_0664 is a short-form enzyme lacking a fused ACT domain, feedback sensitivity may be comparatively modest and pathway control likely resides substantially at aspartokinase — but the enzyme's activity is nonetheless responsive to end-product amino acids.

---

## 6b. Genomic Context (Operon / Co-regulation)

In the KT2440 genome, PP_0664 (*hom*, 772338–773381) lies within a compact, same-strand gene cluster with aspartate-pathway relevance (KEGG neighborhood):

- **PP_0662** — putative **threonine synthase** (*thrC*-like; the terminal threonine-branch enzyme)
- **PP_0663** — **transcriptional regulator of the AsnC/Lrp family** (immediately upstream of *hom*, ~199 bp gap)
- **PP_0664** — **homoserine dehydrogenase** (this gene)
- **PP_0665** — putative glyceraldehyde-3-phosphate dehydrogenase (13 bp gap)

The proximity of *hom* to a threonine-branch enzyme and to an **AsnC/Lrp (leucine-responsive / feast–famine) family regulator** — a family that characteristically controls amino-acid biosynthetic genes — indicates that PP_0664 is likely **transcriptionally co-regulated with threonine-pathway genes in response to amino-acid availability**. This provides a genetic-level control layer complementary to the allosteric feedback of the enzyme itself.

## 7. Subcellular Localization

HSD is a **soluble cytoplasmic enzyme**. It carries no signal peptide, transmembrane segment, or membrane/secretion keyword in UniProt, and it acts on small soluble metabolites within the cytosol where aspartate-pathway metabolism occurs. Its function is therefore carried out **in the bacterial cytoplasm**.

---

## 8. Supported and Refuted Hypotheses

**Supported:**
- H1: PP_0664 encodes homoserine dehydrogenase (EC 1.1.1.3). *Supported* — UniProt, KEGG K00003, Pfam PF00742, PROSITE PS01042 all concordant.
- H2: It catalyzes ASA → L-homoserine using NAD(P)H (NADPH-preferring). *Supported* — enzyme-family reaction + UniProt NADP keyword.
- H3: It is a cytoplasmic, monofunctional, short-form HSD (no fused aspartokinase/ACT domain). *Supported* — 347 aa, IPR022697 HDH_short, no relevant multidomain/localization annotation.
- H4: It provides homoserine for both threonine and methionine branches and is genetically required for their biosynthesis. *Supported* — KEGG modules M00017/M00018; KT2440 Thr/Met auxotrophs (PMID 20158506).

**Refuted / Not supported:**
- That PP_0664 is a *bifunctional* aspartokinase-HSD like *E. coli* ThrA — *refuted* by short monofunctional architecture.
- That it acts in lysine biosynthesis directly — *refuted*; the ppu00300 map assignment reflects only the shared ASA precursor node, not a lysine-pathway catalytic step.

---

## 9. Limitations and Future Directions

- No PP_0664-specific crystal structure or purified-enzyme kinetic study exists; mechanistic/cofactor details are inferred from close family members (e.g., *S. tokodaii* StHSD) and from classic *P. putida* enzymology of the same activity (which predates modern locus assignments).
- The exact identity and strength of feedback effectors (threonine vs. methionine vs. concerted) for the KT2440 enzyme specifically have not been re-measured with recombinant PP_0664; this would be the most valuable experimental follow-up, alongside NADH/NADPH kinetic specificity constants.
- Direct localization (e.g., proteomics) is not reported but is inferred with high confidence from sequence features.

---

## 10. Key References

- Ogata et al. 2018, *inhibition of homoserine dehydrogenase by a cysteine-NAD covalent complex* — PMID 29636528 (HSD reaction, ordered mechanism, active-site geometry).
- Molina-Henares et al. 2010 — PMID 20158506 (KT2440 genome-wide auxotroph screen; Thr/Met auxotrophs).
- Polodienko et al. 1991 — PMID 2067422 (*P. putida* HSD regulation by aspartate-family amino acids).
- Robert-Gero, Poiret & Cohen 1970 — PMID 5441405 (*P. putida* homoserine dehydrogenase properties and regulation).
- Chassagnole et al. 2001 — PMID 11368770 / 11368768 (shared flux control of the threonine pathway including HSD).
- Shaul & Galili 1993 — PMID 8251629; Eikmanns et al. — PMID 8092856 (HSD as an aspartate-pathway branch-point control enzyme).
- Databases: UniProt Q88Q34; KEGG ppu:PP_0664 / K00003; InterPro IPR001342/IPR022697/IPR036291; Pfam PF00742.


## Artifacts

- [OpenScientist final report](PP_0664-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PP_0664-deep-research-openscientist_artifacts/final_report.pdf)