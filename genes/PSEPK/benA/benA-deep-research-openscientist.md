---
provider: openscientist
model: openscientist-autonomous
cached: true
start_time: '2026-07-13T11:32:04.180863'
end_time: '2026-07-13T11:32:04.182312'
duration_seconds: 0.0
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: bena
  gene_symbol: benA
  uniprot_accession: Q88I40
  protein_description: 'SubName: Full=Benzoate 1,2-dioxygenase subunit alpha {ECO:0000313|EMBL:AAN68769.1};
    EC=1.14.12.10 {ECO:0000313|EMBL:AAN68769.1};'
  gene_info: Name=benA {ECO:0000313|EMBL:AAN68769.1}; OrderedLocusNames=PP_3161 {ECO:0000313|EMBL:AAN68769.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the bacterial ring-hydroxylating dioxygenase
  protein_domains: ARHD_Rieske_2Fe_2S. (IPR015881); Benzo_1-2-diOase_lsu. (IPR017639);
    Rieske_2Fe-2S. (IPR017941); Rieske_2Fe-2S_sf. (IPR036922); Ring_hydroxy_dOase_asu_C_dom.
    (IPR015879)
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
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: bena-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: bena-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88I40
- **Protein Description:** SubName: Full=Benzoate 1,2-dioxygenase subunit alpha {ECO:0000313|EMBL:AAN68769.1}; EC=1.14.12.10 {ECO:0000313|EMBL:AAN68769.1};
- **Gene Information:** Name=benA {ECO:0000313|EMBL:AAN68769.1}; OrderedLocusNames=PP_3161 {ECO:0000313|EMBL:AAN68769.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the bacterial ring-hydroxylating dioxygenase
- **Key Domains:** ARHD_Rieske_2Fe_2S. (IPR015881); Benzo_1-2-diOase_lsu. (IPR017639); Rieske_2Fe-2S. (IPR017941); Rieske_2Fe-2S_sf. (IPR036922); Ring_hydroxy_dOase_asu_C_dom. (IPR015879)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "benA" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'benA' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **benA** (gene ID: bena, UniProt: Q88I40) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: **benA** (Q88I40, PP_3161) — Benzoate 1,2-dioxygenase subunit alpha, *Pseudomonas putida* KT2440

## 0. Gene identity verification (PASSED)

The target was cross-checked against the literature before research:

- **Gene symbol `benA`** matches the protein description "Benzoate 1,2-dioxygenase subunit alpha" (EC 1.14.12.10). Multiple primary papers use exactly this symbol/enzyme in *Pseudomonas putida* KT2440 (PMIDs 18679676, 16470664, 21954182, 24588992).
- **Organism** *P. putida* KT2440 is confirmed (ordered locus PP_3161; benzoate/ben pathway mapped in the KT2440 genome, PMID 12534466).
- **Protein family / domains** align: the actual Q88I40 sequence (452 aa) contains the canonical Rieske [2Fe-2S] motif at residues 88–110, matching InterPro IPR017941/IPR015881/IPR015879 and the "bacterial ring-hydroxylating dioxygenase" family assignment (own sequence analysis, this study).

**Conclusion: the gene is unambiguously identified. No symbol ambiguity.** benA is a well-characterized enzyme, so the report rests primarily on experimental primary literature and authoritative reviews.

---

## 1. Summary (answer to the research question)

**benA** encodes the **catalytic α-subunit (large subunit) of benzoate 1,2-dioxygenase (BADO; the BenABC oxygenase system)**, a cytoplasmic, three-component **Rieske non-heme iron ring-hydroxylating dioxygenase** (EC 1.14.12.10). BenA catalyzes the **first, committed and rate-defining step of aerobic benzoate catabolism**: the **NADH- and O₂-dependent stereospecific *cis*-dihydroxylation of benzoate at the C1–C2 positions**, yielding **benzoate *cis*-dihydrodiol (1,2-dihydroxy-cyclohexa-3,5-diene-1-carboxylate, "DHCDC")**. Substrate specificity is comparatively **narrow, favoring unsubstituted benzoate**. The product is rearomatized/decarboxylated by BenD to **catechol**, which enters the **catechol (ortho-cleavage) branch of the β-ketoadipate pathway** for mineralization to TCA-cycle intermediates. Expression is **induced by benzoate through the BenR (AraC/XylS) activator** and **repressed by carbon-catabolite control via Crc**.

---

## 2. Primary function — the reaction catalyzed

BenA is the α-subunit of the terminal **oxygenase component (BenAB)** of benzoate 1,2-dioxygenase. The full three-component enzyme carries out:

> **benzoate + NADH + H⁺ + O₂ → benzoate *cis*-1,2-dihydrodiol (DHCDC) + NAD⁺**

- Recombinant *P. putida* overexpressing **benABC** (in a *benD*-deletion background that blocks downstream conversion) transforms benzoate stoichiometrically into **1,2-dihydroxy-cyclohexa-3,5-diene-1-carboxylate (benzoate *cis*-diol / DHCDC)**, reaching >17 g/L at ~73% yield — direct experimental proof that BenABC performs benzoate *cis*-dihydroxylation (PMID 18679676).
- As a member of the Rieske non-heme iron dioxygenase class, benzoate dioxygenase (BZDO; Wolfe & Lipscomb, 2002) **forms one *cis*-dihydrodiol per Rieske center oxidized, with the mononuclear iron ending in the ferric [Fe(III)] state** — establishing the dioxygenase (both O atoms of O₂ incorporated) stoichiometry (PMID 15835907).

This dearomatizing dihydroxylation is the **peripheral, upstream "activation" step** that converts an inert aromatic acid into a metabolizable diol.

---

## 3. Substrate specificity

- **Preferred substrate: benzoate (unsubstituted).** The chromosomal *ben*-encoded enzyme is comparatively **specific for benzoate**.
- Its closest paralog, the **TOL plasmid pWW0 toluate 1,2-dioxygenase (xylXYZ)**, whose α-subunit **XylX is 58% identical to BenA**, has **broad substrate specificity** and additionally oxidizes methylbenzoates (PMID 1938949). The comparison highlights that BenA occupies the narrow-specificity end of this closely related enzyme pair.
- In the RHO family, **substrate range is dictated by the size/shape of the hydrophobic active-site pocket and mobile loops** near the mononuclear iron; a few pocket residues determine which aromatics are accepted (PMID 17451434, 20652669, 16168954). BenR can also weakly respond to 3-methylbenzoate, and BADO shows modest activity toward some substituted benzoates, but benzoate is the physiological substrate.

---

## 4. Cofactors, structure, and catalytic mechanism (where/how it acts chemically)

- **Quaternary structure:** terminal oxygenases of this family are **α₃β₃ hexamers**; BenA is the α (large) subunit, BenB the β (small) subunit (PMID 17451434).
- **Cofactors in BenA:** a **Rieske [2Fe-2S] cluster** and a **mononuclear non-heme Fe(II) (2-His-1-carboxylate facial triad) catalytic center** (PMID 16168954, 20652669). **Direct sequence evidence:** Q88I40 (452 aa, ~51.5 kDa) contains the diagnostic Rieske ligand motif **C88-X-H90 … C-X-X-H110** (`CSHRGAMLCRHKRGNRSSYTCPFH`) in its N-terminal domain, plus the conserved mononuclear-iron **2-His motif His217/His222** ('HVSSVH') and candidate carboxylate ligand(s) among C-terminal Asp residues (e.g. Asp357/Asp368) in the catalytic domain — confirming both metal sites in the actual target protein (this study; consistent with IPR017941/IPR015879).
- **Reductase component (BenC):** an NADH:acceptor reductase carrying **FAD and a plant-type [2Fe-2S] center**, which feeds electrons from NADH into the oxygenase (inferred from the 52%-identical CbdC of 2-halobenzoate dioxygenase; PMID 7530709).
- **Electron transfer & O₂ activation:** electrons flow **NADH → reductase → Rieske center → the mononuclear iron of the *adjacent* α-subunit via a conserved gating aspartate**; **O₂ binds side-on** at the mononuclear iron and a **concerted mechanism of O₂ activation and ring *cis*-hydroxylation** occurs, with **substrate orientation controlling regio-/stereospecificity** (PMID 16168954). The inter-subunit relay rationalizes the obligate oligomeric assembly.

---

## 5. Localization

BenA functions in the **cytoplasm (soluble)**. Rieske ring-hydroxylating dioxygenase systems are soluble multicomponent cytoplasmic enzymes, and the benzoate degradation intermediates (notably **catechol**) accumulate **inside the cells** during benzoate metabolism, confirming that BenA's reaction and its downstream steps occur intracellularly (PMID 21954182). There is no signal peptide or membrane-targeting evidence; benzoate is imported and processed in the cytoplasm.

---

## 6. Pathway context (biological process)

BenA initiates the **peripheral benzoate ("ben") pathway** that funnels into central aromatic catabolism:

1. **benzoate → benzoate *cis*-dihydrodiol** — BenABC (BenA = catalytic α-subunit) *(this step)*
2. **benzoate *cis*-dihydrodiol → catechol + CO₂** — BenD (*cis*-diol/dihydrodiol dehydrogenase), with loss of CO₂ and rearomatization
3. **catechol → *cis,cis*-muconate** — CatA (catechol 1,2-dioxygenase, *ortho* ring cleavage)
4. ***cis,cis*-muconate → β-ketoadipate → succinyl-CoA + acetyl-CoA** — catechol branch of the **β-ketoadipate pathway** → TCA cycle

Supporting evidence:
- In KT2440, **benzoate specifically induces BenA, BenD and CatA**, and benzoate catabolism **converges with p-hydroxybenzoate/vanillin catabolism at the β-ketoadipate pathway** (PMID 16470664).
- Genome analysis maps the **ben peripheral pathway feeding the catechol (cat) branch of the β-ketoadipate pathway** in KT2440 (PMID 12534466).
- The **ben operon "encodes the conversion of benzoate to *cis,cis*-muconate"**; catechol accumulates intracellularly and **represses ben expression** (product feedback), and *catB*-blocked strains accumulate ~18.5 g/L muconate at ~100% molar yield (PMID 21954182). This makes BenA biotechnologically central to **microbial production of *cis,cis*-muconic acid / adipic acid from lignin-derived aromatics** (PMIDs 21954182, 32022244).

Its role is **specific and upstream** (substrate activation and channelling), not broadly pleiotropic.

---

## 7. Regulation of benA expression

- **Induction:** the chromosomal *ortho* pathway is **initiated by the Pben promoter and the BenR activator** (AraC/XylS family), which activates *PbenA*/*Pben* in response to **benzoate** (and, weakly, 3-methylbenzoate) (PMIDs 24588992, 22588473).
- **Catabolite repression:** the **translational repressor Crc** inhibits translation of **benR mRNA** (and of structural-gene mRNAs, including the first pathway enzyme), silencing benzoate assimilation when preferred carbon sources are present — a multi-tier control (PMID 22925411).
- **Specificity of regulation:** the Pben operator has **evolved to respond to BenR but resist cross-activation by the related XylS regulator**, preventing metabolic conflict during co-metabolism of benzoate and m-xylene/3-methylbenzoate (PMID 24588992). Cross-talk between chromosomal ben and TOL-plasmid pathways is documented at the promoter level (PMID 27046069).

---

## 8. Evolution

BenA belongs to a family of aromatic-acid dioxygenase α-subunits that diverged from a common ancestor: **XylX (toluate DO, TOL pWW0) is 58% identical**, **A. calcoaceticus BenA** is the chromosomal ortholog, and **CbdA (2-halobenzoate DO) is ~52% identical to BenA** (PMIDs 1938949, 7530709). Family-wide phylogenetics indicate all ring-hydroxylating oxygenases are related by divergent evolution, with structure–function studies showing that active-site divergence tunes substrate specificity and regiospecificity (PMID 20652669).

---

## 9. Supported and refuted hypotheses

**Supported:**
- H1: BenA is the catalytic α-subunit of benzoate 1,2-dioxygenase and catalyzes benzoate *cis*-dihydroxylation to DHCDC (PMIDs 18679676, 15835907). **Strongly supported.**
- H2: BenA carries a Rieske [2Fe-2S] + mononuclear Fe center and acts within an α₃β₃/three-component O₂- and NADH-dependent system (PMIDs 7530709, 16168954, 17451434; direct motif in Q88I40). **Supported.**
- H3: The enzyme is cytoplasmic and feeds catechol into the β-ketoadipate (ortho) pathway (PMIDs 16470664, 12534466, 21954182). **Supported.**
- H4: benA is benzoate-induced (BenR) and Crc-repressed (PMIDs 24588992, 22925411). **Supported.**
- H5: BenA is comparatively benzoate-specific relative to broad-specificity XylX (PMID 1938949). **Supported.**

**Refuted / not supported:** No evidence that benA is misannotated or belongs to a different gene family; no evidence of a broad, promiscuous substrate range comparable to toluate dioxygenase; no evidence of membrane localization.

---

## 10. Limitations and future directions

- Much mechanistic and structural detail is **inferred from close homologs** (naphthalene DO, CHY-1 RHD, 2-halobenzoate DO, and the Wolfe/Lipscomb benzoate DO biochemistry) rather than from a crystal structure of the KT2440 BenA itself; a KT2440-specific structure would confirm pocket residues governing specificity.
- Quantitative kinetic constants (kcat, Km) and the exact substituted-benzoate acceptance profile for the KT2440 enzyme specifically would refine the specificity statement.
- The identity of the dedicated benzoate transporter and precise BenA–BenC electron-transfer partners in KT2440 merit direct study.

---

### Key references (PMIDs)
18679676, 15835907, 7530709, 1938949, 12534466, 16470664, 21954182, 32022244, 24588992, 22925411, 22588473, 27046069, 16168954, 20652669, 17451434.


## Artifacts

- [OpenScientist final report](bena-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](bena-deep-research-openscientist_artifacts/final_report.pdf)