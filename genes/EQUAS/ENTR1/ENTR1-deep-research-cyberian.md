---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-25T23:27:18.471046'
end_time: '2026-10-25T23:36:37.952303'
duration_seconds: 559.48
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: EQUAS
  gene_id: ENTR1
  gene_symbol: ENTR1
  uniprot_accession: A0A8C4MKL2
  protein_description: 'RecName: Full=Endosome-associated-trafficking regulator 1
    {ECO:0000256|ARBA:ARBA00016007};'
  gene_info: Name=ENTR1 {ECO:0000313|Ensembl:ENSEASP00005027020.2};
  organism_full: Equus asinus (Donkey) (Equus africanus asinus).
  protein_family: Belongs to the ENTR1 family.
  protein_domains: ENTR1. (IPR026757); ENTR1_CC. (IPR063798); ENTR1 (PF29363)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3302
    skip_permissions: true
    manage_server: true
    workdir_base: /Users/cjm/.cache/drc-cyberian-work
citation_count: 52
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A8C4MKL2
- **Protein Description:** RecName: Full=Endosome-associated-trafficking regulator 1 {ECO:0000256|ARBA:ARBA00016007};
- **Gene Information:** Name=ENTR1 {ECO:0000313|Ensembl:ENSEASP00005027020.2};
- **Organism (full):** Equus asinus (Donkey) (Equus africanus asinus).
- **Protein Family:** Belongs to the ENTR1 family.
- **Key Domains:** ENTR1. (IPR026757); ENTR1_CC. (IPR063798); ENTR1 (PF29363)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ENTR1" matches the protein description above**
2. **Verify the organism is correct:** Equus asinus (Donkey) (Equus africanus asinus).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ENTR1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ENTR1** (gene ID: ENTR1, UniProt: A0A8C4MKL2) in EQUAS.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# ENTR1 (Endosome-associated trafficking regulator 1; SDCCAG3) in the donkey, *Equus asinus* (UniProt A0A8C4MKL2)

## 1. Introduction and summary

The target protein, UniProt A0A8C4MKL2, is an unreviewed (TrEMBL) 356-residue protein predicted from the donkey reference genome. Its Ensembl gene model is ENSEASG00005018403 on chromosome 10, and its sequence came from the donkey genome project [uniprot-A0A8C4MKL2]. It is named Endosome-associated-trafficking regulator 1 (gene symbol ENTR1) and is assigned to the ENTR1 family (PANTHER PTHR31259; InterPro IPR026757/IPR063798; Pfam PF29363). Its main feature is a C-terminal ENTR1 coiled-coil region (residues 178–347), preceded by a predicted disordered segment at residues 49–109 [uniprot-A0A8C4MKL2].

No experimental study of the donkey protein exists, so everything known about its function comes from its human and mouse orthologues. These were long known as SDCCAG3 (serologically defined colon cancer antigen 3, also called antigen NY-CO-3) before being renamed ENTR1 [uniprot-Q96C92; scanlan-1998-colon-cancer-serex-antigens-abstract; sharma-2019-fas-endosomal-sorting-fulltext]. The symbol is not ambiguous: in every paper retrieved, ENTR1 and SDCCAG3 name the same protein. The only false hits were unrelated papers on the prostate-cancer lncRNA PCA3, which happened to match the search terms and were excluded.

The literature agrees that ENTR1 is not an enzyme but a coiled-coil adaptor. It lives on early and recycling endosomes, where it decides what happens to particular transmembrane proteins after the cell has taken them in. Depending on the cargo, it helps send them either back to the plasma membrane, working with the retromer complex, or on to multivesicular bodies and lysosomes, working with dysbindin and the ESCRT-0 protein HRS [hagemann-2013-sdccag3-ptpn13-cytokinesis-abstract; mcgough-2014-snx27-retromer-heterogeneity-fulltext; sharma-2019-fas-endosomal-sorting-fulltext].

These sorting decisions underlie three cellular roles. First, ENTR1 sets how much of the glucose transporter GLUT1 and of the death receptors Fas/CD95 and TNFR1 sits on the cell surface, and therefore how sensitive cells are to apoptosis [mcgough-2014-snx27-retromer-heterogeneity-fulltext; sharma-2019-fas-endosomal-sorting-fulltext; neznanov-2005-sdccag3-tnfr1-surface-abstract]. Second, it takes part in cytokinesis: it collects at the midbody, the bridge between two dividing cells, and binds PTPN13, GIT1 and Arf6 [hagemann-2013-sdccag3-ptpn13-cytokinesis-abstract; sakagami-2016-sdccag3-arf6-testis-abstract]. Third, it supports primary cilia: it sits at the ciliary basal body, binds the intraflagellar transport proteins IFT88 and IFT20, and is needed to deliver the channel polycystin-2 into the cilium [yu-2016-sdccag3-ciliogenesis-fulltext; rezi-2024-dlg1-sdccag3-ift20-pc2-fulltext].

The donkey protein is about 83% identical to human ENTR1 across the region they share. Its interaction motifs, coiled-coil and C-terminus are almost invariant, so these functions very probably carry over to the donkey. Comparison with horse, cattle, dog and mouse orthologues (Section 7) points to two donkey-specific issues: the donkey gene model is missing its N-terminus, which is almost certainly a prediction error, and equids appear to lack the aspartate that caspases cleave in human ENTR1.

## 2. Identity, nomenclature and domain architecture

ENTR1 was first found by SEREX, a screen of colon tumour cDNA libraries with antibodies from the patients' own blood, and was catalogued as NY-CO-3 [scanlan-1998-colon-cancer-serex-antigens-abstract; uniprot-Q96C92]. The "colon cancer antigen" name therefore records how the protein was discovered, not what it does.

The protein has no catalytic domain; its defining feature is a long coiled-coil. Neznanov and colleagues noted that this region resembles the myosin tail and the coiled-coils of trafficking proteins such as golgin-160, kinesin and dynein, and on that basis first proposed a role in protein trafficking and secretion [neznanov-2005-sdccag3-tnfr1-surface-abstract].

The reviewed human entry (Q96C92) describes a 435-residue canonical isoform among four splice isoforms. It annotates the following features [uniprot-Q96C92]:

- a coiled-coil at residues 261–371;
- a region at residues 173–198 required for binding PTPN13, where the substitutions P190A and E194A each disrupt binding;
- several phosphoserines identified by large-scale phosphoproteomics.

Experimental mapping divides the protein into an N-terminal targeting and partner-binding region and a C-terminal coiled-coil and tail that bind effector proteins:

| Region | What it does | Source |
|---|---|---|
| N-terminal residues 1–100 | Necessary and sufficient for basal-body targeting and for binding IFT88 | [yu-2016-sdccag3-ciliogenesis-fulltext] |
| N-terminus | Binds the Arf GTPase-activating protein GIT1 directly | [hagemann-2013-sdccag3-ptpn13-cytokinesis-abstract; uniprot-Q96C92] |
| Central acidic, disordered segment | Contains the motif that binds the FERM domain of PTPN13 | [uniprot-Q96C92; sharma-2019-fas-endosomal-sorting-fulltext] |
| C-terminal 101 residues | Bind Arf6 | [sakagami-2016-sdccag3-arf6-testis-abstract] |
| Final 16 residues | Required for binding dysbindin | [sharma-2019-fas-endosomal-sorting-fulltext] |

## 3. Subcellular localization

Several independent studies place ENTR1 on endosomes:

- Hagemann et al. described it as a previously unknown endosomal protein, found mainly on early and recycling endosomes [hagemann-2013-sdccag3-ptpn13-cytokinesis-abstract].
- McGough et al. showed that endogenous SDCCAG3 sits on endosomes marked by the retromer subunit VPS35 in HeLa cells [mcgough-2014-snx27-retromer-heterogeneity-fulltext].
- Sharma et al. found ENTR1 on endosomes at all times. Its partner PTPN13, by contrast, appears on EEA1-positive early endosomes only after Fas is stimulated, and internalized Fas then co-localizes there with both proteins [sharma-2019-fas-endosomal-sorting-fulltext].

ENTR1 also moves during the cell cycle. It accumulates strongly at the midbody during cytokinesis [hagemann-2013-sdccag3-ptpn13-cytokinesis-abstract], and this recruitment depends on the C-terminal region that binds Arf6 [sakagami-2016-sdccag3-arf6-testis-abstract].

In ciliated cells, ENTR1 is found at the ciliary basal body. Yu et al. showed this both for the endogenous protein, seen in about 10% of ciliated RPE1 cells, 29% of IMCD3 cells and 22% of HEK cells, and for an EGFP-tagged version [yu-2016-sdccag3-ciliogenesis-fulltext]. Rezi et al. detected SDCCAG3 along the cilium and at its base in kidney epithelial cells and in mouse kidney tissue, and found that both signals depend on DLG1 [rezi-2024-dlg1-sdccag3-ift20-pc2-fulltext]. A proteome-wide proximity-labelling (BioID) map of centriolar satellites also detected SDCCAG3 among satellite neighbours. This high-throughput result fits a position near the centrosome but is weaker evidence than the targeted studies [gheiratmand-2019-centriolar-satellites-fulltext].

The electronic GO annotations on the donkey entry are early endosome, recycling endosome, midbody, centrosome and ciliary basal body (IEA via TreeGrafter) [uniprot-A0A8C4MKL2]. These match the experimental findings in human and mouse cells.

## 4. Role in endosomal cargo sorting: retromer recycling and lysosomal routing

### Recycling GLUT1 to the cell surface with retromer

The clearest molecular placement of ENTR1 comes from a SILAC proteomic survey of proteins bound to VPS35, the core retromer subunit. SDCCAG3 was enriched more than 100-fold in that dataset, alongside two other newly identified retromer partners, VARP and ANKRD50 [mcgough-2014-snx27-retromer-heterogeneity-abstract; mcgough-2014-snx27-retromer-heterogeneity-fulltext].

Knocking down SDCCAG3 lowered both the surface and total levels of GLUT1, a classic cargo that the SNX27–retromer pathway returns from endosomes to the plasma membrane. Unlike loss of VPS35, however, loss of SDCCAG3 did not make GLUT1 build up visibly in lysosomes, and its effect on another cargo, CD97, was small [mcgough-2014-snx27-retromer-heterogeneity-fulltext]. The authors concluded that retromer's accessory proteins each act on particular cargoes [mcgough-2014-snx27-retromer-heterogeneity-abstract]. On this evidence ENTR1 is best described as a cargo-selective modulator of retromer recycling to the plasma membrane, not a core retromer subunit.

Retromer itself works with the WASH actin-nucleating complex [mcgough-2014-vps35-d620n-wash-abstract], but there is no evidence yet that ENTR1 binds WASH directly.

### Routing Fas to lysosomes with dysbindin and ESCRT-0

The most detailed mechanistic study is by Sharma et al. [sharma-2019-fas-endosomal-sorting-abstract]. Removing ENTR1 raised the amount of the death receptor Fas/CD95 on the cell surface, and the effect was specific: transferrin receptor, EGF receptor and N-cadherin were unchanged. As a result, the cells became more sensitive to Fas-induced apoptosis. The paper's main findings were:

- **Fas is recycled instead of degraded.** Without ENTR1, internalized Fas failed to reach LAMP1-positive lysosomes efficiently and was not packed into the internal vesicles of multivesicular bodies. Instead it returned to the surface by a Rab11-dependent route. Blocking Rab11, with a dominant-negative mutant or with the Rab11-binding domain of RCP, fully reversed the rise in surface Fas, whereas blocking Rab4 had no effect [sharma-2019-fas-endosomal-sorting-fulltext].
- **ENTR1 binds dysbindin.** ENTR1 binds dysbindin (DTNBP1) through its last 16 residues, confirming earlier proteomic data. Pallidin did not co-purify, so ENTR1 apparently does not engage the canonical BLOC-1 complex.
- **Dysbindin and HRS act in the same pathway.** Knocking down dysbindin or the ESCRT-0 subunit HRS reproduced the Fas sorting defect, and removing dysbindin and ENTR1 together was no worse than removing either alone.
- **PTPN13 binding is required.** ENTR1 mutants that cannot bind the FERM domain of PTPN13 failed to restore normal Fas levels.

The proposed model is that ENTR1 acts as a scaffold on early endosomes. It brings PTPN13, a known negative regulator of surface Fas, together with the dysbindin–HRS sorting machinery, so that activated Fas is sent down the ESCRT-dependent degradation route and its signalling is switched off [sharma-2019-fas-endosomal-sorting-fulltext].

### TNFR1 and other death receptors

ENTR1 also supports surface display of the related death receptor TNFR1. In a functional suppressor screen, a dominant-negative fragment of mouse Sdccag3 containing the coiled-coil protected cells from TNF-induced death. The same fragment reduced the amount of TNFR1 on the cell surface and suppressed general protein secretion [neznanov-2005-sdccag3-tnfr1-surface-abstract]. A 2026 study in chondrocytes reported that ENTR1 lowers surface Fas by binding PTPN13, extending the Sharma mechanism to cartilage cells [gao-2026-entr1-osteoarthritis-ptpn13-abstract].

Taken together, these studies show ENTR1 acting at the endosome to decide each cargo's fate. Whether a cargo is recycled, as GLUT1 is, or degraded, as Fas is, depends on the cargo and on which partner proteins ENTR1 engages.

## 5. Cytokinesis and the Arf6, GIT1 and PTPN13 partners

Hagemann et al. first linked ENTR1 to cell division [hagemann-2013-sdccag3-ptpn13-cytokinesis-abstract]. They showed that SDCCAG3 forms a complex with PTPN13, a tyrosine phosphatase involved in cytokinesis, and accumulates at the midbody. Both overexpressing and depleting SDCCAG3 increased the number of cells with more than one nucleus, a hallmark of failed cytokinesis. SDCCAG3 also binds the Arf GTPase-activating protein GIT1 directly, and a GIT1 mutant lacking its GAP activity likewise caused multinucleation. This points to Arf-regulated vesicle traffic as the underlying mechanism.

Sakagami et al. independently found SDCCAG3 in a yeast two-hybrid screen using constitutively active Arf6, a small GTPase that controls endosomal recycling at the cleavage furrow and midbody [sakagami-2016-sdccag3-arf6-testis-abstract]. Among the Arf family members tested, SDCCAG3 bound only Arf6. Binding required its C-terminal 101 residues, which were also needed for recruitment to the midbody.

The current model is that ENTR1 acts downstream of Arf6 as an effector or adaptor. It may help deliver recycling-endosome membrane to the bridge between the two daughter cells, with GIT1 and PTPN13 as regulatory partners. The exact step ENTR1 controls in the final separation of the cells (abscission) has not been defined. In mouse, SDCCAG3 is most abundant in the testis, in spermatocytes and spermatids [sakagami-2016-sdccag3-arf6-testis-abstract], which hints at a role in germ-cell division or sperm development.

## 6. Primary cilia: basal body localization, transport partners and polycystin-2 delivery

Yu et al. 2016 established a role for ENTR1 in primary cilia [yu-2016-sdccag3-ciliogenesis-abstract; yu-2016-sdccag3-ciliogenesis-fulltext]. Depleting SDCCAG3 lowered the fraction of cells that grew a cilium and shortened the cilia that did form; re-expressing EGFP-SDCCAG3 reversed both defects, and the rescue required the N-terminal residues 1–100. Using that N-terminal fragment as bait in a yeast two-hybrid screen, the authors found the intraflagellar transport protein IFT88. The binding site mapped to IFT88 residues 400–550, a stretch of tetratricopeptide repeats, and the interaction was confirmed by pull-downs in both directions. SDCCAG3 was needed to bring the cation channel polycystin-2 (PC2, encoded by PKD2) into the cilium, but not Rab8.

Rezi et al. 2024 extended this work to kidney tissue [rezi-2024-dlg1-sdccag3-ift20-pc2-abstract; rezi-2024-dlg1-sdccag3-ift20-pc2-fulltext]:

- **DLG1 is needed upstream.** Loss of DLG1, a member of the Scribble polarity complex, reduced the ciliary levels of SDCCAG3, IFT20 and PC2, both in cultured kidney epithelial cells and in the kidneys of conditional-knockout mice. Wild-type DLG1 restored them, but the T489R variant linked to CAKUT (congenital anomalies of the kidney and urinary tract) did not.
- **SDCCAG3 and IFT20 bind each other.** SDCCAG3, IFT20 and DLG1 co-immunoprecipitated. AlphaFold predicted a high-confidence direct SDCCAG3–IFT20 pair in which SDCCAG3 and IFT54 cannot bind IFT20 at the same time, suggesting that SDCCAG3 holds a pool of IFT20 outside the IFT-B complex.
- **Proposed route.** The authors suggest that SDCCAG3 and IFT20 move PC2 to the cilium through recycling endosomes and the cis-Golgi.

Two further studies fit with this. PC2 binds retromer through its cytoplasmic N-terminus [tilley-2018-retromer-polycystin2-abstract], and retromer subunits are needed for primary cilia to form [xie-2022-retromer-ciliogenesis-abstract]. Since ENTR1 is a retromer-associated protein, these findings suggest a single pathway in which ciliary membrane proteins such as PC2 travel from the endosome, via retromer and ENTR1, to IFT20 and IFT88 and into the cilium. This is an inference drawn across separate studies and has not been tested directly.

## 7. Conservation in the donkey and evidence for orthology

I aligned the donkey protein globally with human ENTR1 and with the UniProt ENTR1 entries for horse, cattle, dog and mouse, using Biopython's pairwise aligner with BLOSUM62 scoring. The scripts, sequences and output are in `analysis/`, and the sequences come from [uniprot-A0A8C4MKL2; uniprot-Q96C92; uniprot-A0A5F5Q1J2; uniprot-A2AIW0; uniprot-Q2KJD6].

**Overall identity.** The donkey protein shares 294 of its 356 residues with human ENTR1, about 83%.

**Conservation of mapped functional sites.** The residues needed to bind PTPN13 are conserved: human P190 and E194 correspond to donkey P114 and E118, within the motif GAYLPSA(I/V)EQ. The mapped phosphoserines are also conserved, with human Ser147, Ser243 and Ser247 corresponding to donkey Ser71, Ser164 and Ser168. The coiled-coil is nearly invariant. The C-terminal tail that binds dysbindin differs only slightly, reading KSIDRISEVKDEEEDS in human and KSIDRISEIKEEEESS in donkey. Conservation of these binding surfaces, together with the ENTR1 family assignment, supports one-to-one orthology and justifies transferring the human functions involving retromer, dysbindin, PTPN13 and Arf6 to the donkey protein.

**The donkey N-terminus is a gene-model error.** The donkey entry lacks the first 80 or so residues of human isoform 1 and does not begin with methionine; its first residues are QPPVHA. The three horse ENTR1 models (A0A5F5Q1J2, 459 aa; F6QT44, 448 aa; A0A3Q2H8N2, 360 aa), cattle Q2KJD6 and dog all start with the conserved sequence M(A/S)GYARRPG…, as human and mouse do. This strongly suggests that the donkey gene has the same N-terminus and that the Ensembl prediction simply missed the first exon or exons. The missing region overlaps residues 1–100, which in human are needed for basal-body targeting and for binding IFT88 and GIT1 [yu-2016-sdccag3-ciliogenesis-fulltext; hagemann-2013-sdccag3-ptpn13-cytokinesis-abstract]. The donkey protein should therefore still be annotated with ciliary and cytokinetic functions, and the sequence record should be flagged as fragmentary.

**Equids appear to lack the caspase cleavage site.** Sharma et al. mapped a single caspase cleavage site in ENTR1, at Asp236 of the longest human isoform (Asp213 in their shorter variant 2). Cleavage at this site inactivates ENTR1 during Fas-induced apoptosis and sets up a positive feedback loop [sharma-2019-fas-endosomal-sorting-fulltext]. The 23-residue offset between Sharma's PTPN13-binding mutants (P167/E171) and UniProt's P190/E194 is consistent with their longest isoform matching UniProt's canonical numbering. In human, Asp236 sits in the sequence LSDTD↓S. Mouse (LSDTD), cattle (LSDSD) and dog keep an aspartate at this position. All three horse models and the donkey instead read LSDSE, with glutamate in place of the aspartate. Because caspases strongly prefer aspartate at the cleavage position, equid ENTR1 may resist cleavage at this site. That would weaken or remove the apoptotic feedback loop described in human cells. This is a sequence-based inference and has not been tested experimentally.

## 8. Physiological and disease associations (lower-confidence findings)

Several recent studies link ENTR1 to wider physiology. Most come from one research group and in most cases only the abstract was available, so they carry less weight than the cell-biology work above:

- **Adipose tissue.** Deleting Sdccag3 in fat tissue made high-fat-diet obesity and insulin resistance worse, and overexpressing it protected against them. The proposed mechanism is that SDCCAG3 protects the transcription factor PPARγ from SMURF1-mediated ubiquitination and degradation [huo-2025-sdccag3-smurf1-ppar-abstract].
- **Periodontitis.** ENTR1 reduced pro-inflammatory (M1) macrophage polarization in a periodontitis model by enhancing AMPK phosphorylation [wang-2025-entr1-periodontitis-ampk-abstract].
- **Antiviral defence.** Loss of ENTR1 increased NIX-mediated mitophagy and the degradation of MAVS, weakening type I interferon responses to bovine parainfluenza virus 3 and vesicular stomatitis virus [yao-2026-entr1-mavs-mitophagy-abstract].
- **Cancer.** ENTR1 is overexpressed in several tumours, including colon cancer and glioblastoma, where it has been linked to proliferation, glycolytic gene expression and TNF-pathway transcription [ma-2025-entr1-colon-glycolysis-abstract; zhang-2024-entr1-glioblastoma-tnf-abstract; hagemann-2013-sdccag3-ptpn13-cytokinesis-abstract].
- **NOD2.** SDCCAG3 binds the innate immune sensor NOD2, shown by yeast two-hybrid, co-immunoprecipitation and BRET. NOD2 mutants associated with Crohn's disease lose this interaction, but variants in SDCCAG3 itself showed no genetic association with inflammatory bowel disease [thiebaut-2016-nod2-interacting-proteins-abstract].

Many of these effects may follow indirectly from ENTR1's control over which receptors, transporters and channels reach the cell surface, including death receptors, GLUT1 and possibly receptors upstream of AMPK or PPARγ. None yet has a direct mechanism as well defined as the Fas–dysbindin pathway.

## Open Questions

**How ENTR1 chooses between recycling and degradation.** It is not known how ENTR1 decides whether a cargo goes back to the surface, as GLUT1 does with retromer, or to lysosomes, as Fas does with dysbindin and HRS, or whether these involve separate ENTR1 complexes. It is also unclear whether ENTR1 binds VPS35 directly, because the evidence so far is co-purification in a proteomic screen and co-localization on endosomes [mcgough-2014-snx27-retromer-heterogeneity-fulltext]. Reconstitution with purified proteins, structural work on the coiled-coil, and AlphaFold-Multimer models of ENTR1 with VPS35, DTNBP1 and Arf6 (like the model already published with IFT20 [rezi-2024-dlg1-sdccag3-ift20-pc2-fulltext]) would all help.

**ENTR1's step in cytokinesis.** It is not known which part of cell separation ENTR1 controls: delivery of recycling endosomes to the midbody, recruitment of the ESCRT-III machinery that cuts the bridge, or Arf6 and GIT1 signalling. Nor is it known why both too much and too little ENTR1 leave cells with multiple nuclei [hagemann-2013-sdccag3-ptpn13-cytokinesis-abstract; sakagami-2016-sdccag3-arf6-testis-abstract].

**ENTR1 in cilia.** It is unclear whether ENTR1 itself enters the cilium and how its binding to IFT88 and to IFT20 is coordinated. It also remains to be shown whether loss of ENTR1 causes kidney cysts or other cilia-related defects in animals. The literature retrieved here describes no whole-body Entr1 knockout and no Entr1 disease variants [yu-2016-sdccag3-ciliogenesis-fulltext; rezi-2024-dlg1-sdccag3-ift20-pc2-fulltext].

**Donkey-specific checks.** Two follow-ups are needed for the donkey record. Transcript evidence, such as donkey RNA-seq or a re-annotation of the gene model, should confirm the predicted full-length N-terminus. Separately, a cleavage assay would show whether the glutamate at the human Asp236 position makes horse and donkey ENTR1 resistant to caspases during Fas-induced apoptosis.

**Replicating the newer findings.** The proposed links to AMPK, to PPARγ and SMURF1, and to NIX and MAVS come mainly from a single group and are described only in abstracts. They need independent replication and a mechanistic connection to ENTR1's endosomal role.

## References

- [uniprot-A0A8C4MKL2] UniProtKB/TrEMBL entry A0A8C4MKL2 (A0A8C4MKL2_EQUAS), Endosome-associated-trafficking regulator 1, *Equus asinus*; entry version 21 (02-SEP-2026). https://rest.uniprot.org/uniprotkb/A0A8C4MKL2.txt . Sequence source: Wang C. et al. "Donkey genomes provide new insights into domestication and selection for coat color." Nat Commun 11:6014 (2020), PMID 33293529.
- [uniprot-Q96C92] UniProtKB/Swiss-Prot entry Q96C92 (ENTR1_HUMAN), Endosome-associated-trafficking regulator 1, *Homo sapiens*. https://rest.uniprot.org/uniprotkb/Q96C92.txt
- [uniprot-A0A5F5Q1J2] UniProtKB/TrEMBL entry A0A5F5Q1J2, ENTR1, *Equus caballus* (horse); Ensembl ENSECAG00000010463. https://rest.uniprot.org/uniprotkb/A0A5F5Q1J2.txt (other horse models F6QT44 and A0A3Q2H8N2, and dog A0A8I3MXN3, were retrieved for the comparison and are stored in analysis/orth.fa)
- [uniprot-A2AIW0] UniProtKB/Swiss-Prot entry A2AIW0 (ENTR1_MOUSE). https://rest.uniprot.org/uniprotkb/A2AIW0.txt
- [uniprot-Q2KJD6] UniProtKB/Swiss-Prot entry Q2KJD6 (ENTR1_BOVIN). https://rest.uniprot.org/uniprotkb/Q2KJD6.txt
- [scanlan-1998-colon-cancer-serex-antigens] Scanlan MJ, Chen YT, Williamson B, Gure AO, Stockert E, Gordan JD, Türeci O, Sahin U, Pfreundschuh M, Old LJ. "Characterization of human colon cancer antigens recognized by autologous antibodies." Int J Cancer 1998. PMID 9610721. DOI 10.1002/(sici)1097-0215(19980529)76:5<652::aid-ijc7>3.0.co;2-p
- [neznanov-2005-sdccag3-tnfr1-surface] Neznanov N, Neznanova L, Angres B, Gudkov AV. "Serologically defined colon cancer antigen 3 is necessary for the presentation of TNF receptor 1 on cell surface." DNA Cell Biol 2005. PMID 16332174. DOI 10.1089/dna.2005.24.777
- [hagemann-2013-sdccag3-ptpn13-cytokinesis] Hagemann N, Ackermann N, Christmann J, Brier S, Yu F, Erdmann KS. "The serologically defined colon cancer antigen-3 interacts with the protein tyrosine phosphatase PTPN13 and is involved in the regulation of cytokinesis." Oncogene 2013. PMID 23108400. DOI 10.1038/onc.2012.485
- [mcgough-2014-snx27-retromer-heterogeneity] McGough IJ, Steinberg F, Gallon M, Yatsu A, Ohbayashi N, Heesom KJ, Fukuda M, Cullen PJ. "Identification of molecular heterogeneity in SNX27-retromer-mediated endosome-to-plasma-membrane recycling." J Cell Sci 2014. PMID 25278552. PMCID PMC4231307. DOI 10.1242/jcs.156299
- [mcgough-2014-vps35-d620n-wash] McGough IJ, Steinberg F, Jia D, et al. "Retromer binding to FAM21 and the WASH complex is perturbed by the Parkinson disease-linked VPS35(D620N) mutation." Curr Biol 2014. PMID 24980502. PMCID PMC4110399. DOI 10.1016/j.cub.2014.06.024
- [yu-2016-sdccag3-ciliogenesis] Yu F, Sharma S, Skowronek A, Erdmann KS. "The serologically defined colon cancer antigen-3 (SDCCAG3) is involved in the regulation of ciliogenesis." Sci Rep 2016. PMID 27767179. PMCID PMC5073310. DOI 10.1038/srep35399
- [sakagami-2016-sdccag3-arf6-testis] Sakagami H, Hara Y, Fukaya M. "Interaction of serologically defined colon cancer antigen-3 with Arf6 and its predominant expression in the mouse testis." Biochem Biophys Res Commun 2016. PMID 27373827. DOI 10.1016/j.bbrc.2016.06.150
- [thiebaut-2016-nod2-interacting-proteins] Thiébaut R, Esmiol S, Lecine P, et al. "Characterization and Genetic Analyses of New Genes Coding for NOD2 Interacting Proteins." PLoS One 2016. PMID 27812135. PMCID PMC5094585. DOI 10.1371/journal.pone.0165420
- [tilley-2018-retromer-polycystin2] Tilley FC, Gallon M, Luo C, Danson CM, Zhou J, Cullen PJ. "Retromer associates with the cytoplasmic amino-terminus of polycystin-2." J Cell Sci 2018. PMID 29724910. PMCID PMC6031323. DOI 10.1242/jcs.211342
- [gheiratmand-2019-centriolar-satellites] Gheiratmand L, Coyaud E, Gupta GD, et al. "Spatial and proteomic profiling reveals centrosome-independent features of centriolar satellites." EMBO J 2019. PMID 31304627. PMCID PMC6627244. DOI 10.15252/embj.2018101109
- [sharma-2019-fas-endosomal-sorting] Sharma S, Carmona A, Skowronek A, Yu F, Collins MO, Naik S, Murzeau CM, Tseng PL, Erdmann KS. "Apoptotic signalling targets the post-endocytic sorting machinery of the death receptor Fas/CD95." Nat Commun 2019. PMID 31308371. PMCID PMC6629679. DOI 10.1038/s41467-019-11025-y
- [xie-2022-retromer-ciliogenesis] Xie S, Dierlam C, Smith E, et al. "The retromer complex regulates C. elegans development and mammalian ciliogenesis." J Cell Sci 2022. PMID 35510502. PMCID PMC9189432. DOI 10.1242/jcs.259396
- [zhang-2024-entr1-glioblastoma-tnf] Zhang Q, Dai Z, Chen Y, et al. "Endosome associated trafficking regulator 1 promotes tumor growth and invasion of glioblastoma multiforme via inhibiting TNF signaling pathway." J Neurooncol 2024. PMID 38191954. DOI 10.1007/s11060-023-04527-9
- [rezi-2024-dlg1-sdccag3-ift20-pc2] Rezi CK, Aslanyan MG, Diwan GD, et al. "DLG1 functions upstream of SDCCAG3 and IFT20 to control ciliary targeting of polycystin-2." EMBO Rep 2024. PMID 38849673. PMCID PMC11239879. DOI 10.1038/s44319-024-00170-1
- [huo-2025-sdccag3-smurf1-ppar] Huo F, Liu C, Wang X, et al. "SDCCAG3 inhibits adipocyte hypertrophy and improves obesity-related metabolic disorders via SDCCAG3/SMURF1/PPARγ axis." J Lipid Res 2025. PMID 40058593. PMCID PMC12002885. DOI 10.1016/j.jlr.2025.100772
- [ma-2025-entr1-colon-glycolysis] Ma A, Zhai C, He Q, et al. "ENTR1 affects the progression of colon cancer by regulating energy metabolism under the influence of glycolysis." BMC Cancer 2025. PMID 40462015. PMCID PMC12135303. DOI 10.1186/s12885-025-14412-5
- [wang-2025-entr1-periodontitis-ampk] Wang X, Gui H, Liu C, et al. "ENTR1 regulates periodontitis by modulating macrophage M1 polarization via AMPK activation." Life Sci 2025. PMID 40054733. DOI 10.1016/j.lfs.2025.123525
- [yao-2026-entr1-mavs-mitophagy] Yao X, Li X, Shi L, Wang H, He H. "ENTR1 stabilizes MAVS by inhibiting NIX-mediated mitophagy to restrict BPIV3 and VSV replication." Vet Microbiol 2026. PMID 41494271. DOI 10.1016/j.vetmic.2025.110865
- [gao-2026-entr1-osteoarthritis-ptpn13] Gao N, Guo Q, Zhao S, Ren H, Lan J. "ENTR1 ameliorates osteoarthritis through decreasing FAS expression by binding PTPN13." Tissue Cell 2026. PMID 42863186. DOI 10.1016/j.tice.2026.103996


## Citations

1. gao-2026-entr1-osteoarthritis-ptpn13-abstract.md
2. gao-2026-entr1-osteoarthritis-ptpn13-summary.md
3. gheiratmand-2019-centriolar-satellites-abstract.md
4. gheiratmand-2019-centriolar-satellites-fulltext.txt
5. gheiratmand-2019-centriolar-satellites-summary.md
6. hagemann-2013-sdccag3-ptpn13-cytokinesis-abstract.md
7. hagemann-2013-sdccag3-ptpn13-cytokinesis-summary.md
8. huo-2025-sdccag3-smurf1-ppar-abstract.md
9. huo-2025-sdccag3-smurf1-ppar-fulltext.txt
10. huo-2025-sdccag3-smurf1-ppar-summary.md
11. ma-2025-entr1-colon-glycolysis-abstract.md
12. ma-2025-entr1-colon-glycolysis-fulltext.txt
13. ma-2025-entr1-colon-glycolysis-summary.md
14. mcgough-2014-snx27-retromer-heterogeneity-abstract.md
15. mcgough-2014-snx27-retromer-heterogeneity-fulltext.txt
16. mcgough-2014-snx27-retromer-heterogeneity-summary.md
17. mcgough-2014-vps35-d620n-wash-abstract.md
18. mcgough-2014-vps35-d620n-wash-fulltext.txt
19. mcgough-2014-vps35-d620n-wash-summary.md
20. neznanov-2005-sdccag3-tnfr1-surface-abstract.md
21. neznanov-2005-sdccag3-tnfr1-surface-summary.md
22. rezi-2024-dlg1-sdccag3-ift20-pc2-abstract.md
23. rezi-2024-dlg1-sdccag3-ift20-pc2-fulltext.txt
24. rezi-2024-dlg1-sdccag3-ift20-pc2-summary.md
25. sakagami-2016-sdccag3-arf6-testis-abstract.md
26. sakagami-2016-sdccag3-arf6-testis-summary.md
27. scanlan-1998-colon-cancer-serex-antigens-abstract.md
28. scanlan-1998-colon-cancer-serex-antigens-summary.md
29. sharma-2019-fas-endosomal-sorting-abstract.md
30. sharma-2019-fas-endosomal-sorting-fulltext.txt
31. sharma-2019-fas-endosomal-sorting-summary.md
32. thiebaut-2016-nod2-interacting-proteins-abstract.md
33. thiebaut-2016-nod2-interacting-proteins-fulltext.txt
34. thiebaut-2016-nod2-interacting-proteins-summary.md
35. tilley-2018-retromer-polycystin2-abstract.md
36. tilley-2018-retromer-polycystin2-summary.md
37. uniprot-A0A5F5Q1J2-entry.txt
38. uniprot-A0A8C4MKL2-entry.txt
39. uniprot-A2AIW0-entry.txt
40. uniprot-Q2KJD6-entry.txt
41. uniprot-Q96C92-entry.txt
42. wang-2025-entr1-periodontitis-ampk-abstract.md
43. wang-2025-entr1-periodontitis-ampk-summary.md
44. xie-2022-retromer-ciliogenesis-abstract.md
45. xie-2022-retromer-ciliogenesis-summary.md
46. yao-2026-entr1-mavs-mitophagy-abstract.md
47. yao-2026-entr1-mavs-mitophagy-summary.md
48. yu-2016-sdccag3-ciliogenesis-abstract.md
49. yu-2016-sdccag3-ciliogenesis-fulltext.txt
50. yu-2016-sdccag3-ciliogenesis-summary.md
51. zhang-2024-entr1-glioblastoma-tnf-abstract.md
52. zhang-2024-entr1-glioblastoma-tnf-summary.md