---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-17T12:56:46.290890'
end_time: '2026-07-17T13:22:53.007479'
duration_seconds: 1566.72
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: leuD
  gene_symbol: leuD
  uniprot_accession: Q88LE7
  protein_description: 'RecName: Full=3-isopropylmalate dehydratase small subunit
    {ECO:0000255|HAMAP-Rule:MF_01031}; EC=4.2.1.33 {ECO:0000255|HAMAP-Rule:MF_01031};
    AltName: Full=Alpha-IPM isomerase {ECO:0000255|HAMAP-Rule:MF_01031}; Short=IPMI
    {ECO:0000255|HAMAP-Rule:MF_01031}; AltName: Full=Isopropylmalate isomerase {ECO:0000255|HAMAP-Rule:MF_01031};'
  gene_info: Name=leuD {ECO:0000255|HAMAP-Rule:MF_01031}; OrderedLocusNames=PP_1986;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the LeuD family. LeuD type 1 subfamily.
  protein_domains: 3-IsopropMal_deHydase_ssu. (IPR004431); Aconitase/3IPM_dehydase_swvl.
    (IPR015928); AconitaseA/IPMdHydase_ssu_swvl. (IPR000573); IPMI_Swivel. (IPR033940);
    LeuD. (IPR050075)
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
  path: leuD-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: leuD-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88LE7
- **Protein Description:** RecName: Full=3-isopropylmalate dehydratase small subunit {ECO:0000255|HAMAP-Rule:MF_01031}; EC=4.2.1.33 {ECO:0000255|HAMAP-Rule:MF_01031}; AltName: Full=Alpha-IPM isomerase {ECO:0000255|HAMAP-Rule:MF_01031}; Short=IPMI {ECO:0000255|HAMAP-Rule:MF_01031}; AltName: Full=Isopropylmalate isomerase {ECO:0000255|HAMAP-Rule:MF_01031};
- **Gene Information:** Name=leuD {ECO:0000255|HAMAP-Rule:MF_01031}; OrderedLocusNames=PP_1986;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the LeuD family. LeuD type 1 subfamily.
- **Key Domains:** 3-IsopropMal_deHydase_ssu. (IPR004431); Aconitase/3IPM_dehydase_swvl. (IPR015928); AconitaseA/IPMdHydase_ssu_swvl. (IPR000573); IPMI_Swivel. (IPR033940); LeuD. (IPR050075)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "leuD" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'leuD' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **leuD** (gene ID: leuD, UniProt: Q88LE7) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *leuD* (Q88LE7, PP_1986) in *Pseudomonas putida* KT2440

## Gene/Protein Identity Verification

Before presenting the research, the target identity was verified against all mandatory checkpoints, and **no ambiguity was found**:

| Checkpoint | Result |
|---|---|
| Gene symbol vs. protein description | **Consistent.** "leuD" is the universal bacterial symbol for the 3‑isopropylmalate dehydratase **small subunit** / isopropylmalate isomerase (IPMI). |
| Organism | **Confirmed.** UniProt Q88LE7 and KEGG `ppu:PP_1986` both map to *Pseudomonas putida* KT2440 (ATCC 47054 / DSM 6125). |
| Family / domains | **Confirmed.** LeuD type‑1 subfamily; IPMI_Swivel (IPR033940), aconitase small‑subunit/swivel fold (IPR000573, IPR015928); Pfam Aconitase_C, LeuD, LeuD_C. |
| Literature vs. target | **Consistent.** All retrieved primary literature concerns the *leuC/leuD* isopropylmalate isomerase of leucine biosynthesis — the same protein. No conflicting "same‑symbol, different‑gene" literature was found. |
| Sequence orthology | **Confirmed.** 67.3 % amino‑acid identity to biochemically characterized *E. coli* LeuD (see §6). |

**The gene symbol is unambiguous and the literature is directly relevant.** The annotation below rests on experimental biochemistry in *Salmonella*/*E. coli*, X‑ray crystallography in *Mycobacterium tuberculosis*, iron–sulfur biochemistry in yeast, and curated database records (UniProt/HAMAP, KEGG, Rhea), transferred to the *P. putida* protein through high‑confidence orthology.

---

## 1. Summary (Answer to the Research Question)

*leuD* (Q88LE7, locus PP_1986) encodes the **small subunit of isopropylmalate isomerase (IPMI; 3‑isopropylmalate dehydratase; EC 4.2.1.33)**, a 214‑residue polypeptide. It has **no independent catalytic activity**; instead it forms an **obligate 1:1 heterodimer with the large subunit LeuC (PP_1985)**. The LeuCD holoenzyme catalyzes the **reversible isomerization of (2S)‑2‑isopropylmalate to (2R,3S)‑3‑isopropylmalate**, proceeding through the dehydration intermediate **2‑isopropylmaleate**. This is the **second of four dedicated steps of L‑leucine biosynthesis** (from 2‑oxoisovalerate). The enzyme is a member of the **aconitase superfamily** of [4Fe‑4S] hydro‑lyases; the catalytic iron–sulfur cluster resides on LeuC, while **LeuD contributes the aconitase "swivel" domain and the substrate‑binding/substrate‑discriminating loops** that complete the active‑site cleft. The reaction occurs in the **cytoplasm**. LeuD's role is therefore that of a **structural/substrate‑specificity subunit essential for isomerase activity**, not a cofactor‑bearing catalytic subunit.

---

## 2. Primary Function: the Reaction Catalyzed and Substrate Specificity

**Reaction (LeuCD holoenzyme):**

> (2S)‑2‑isopropylmalate ⇌ (2R,3S)‑3‑isopropylmalate, via 2‑isopropylmaleate
> (EC 4.2.1.33; Rhea RHEA:32287; ChEBI 35121 ⇌ 1178) [UniProt Q88LE7 / HAMAP MF_01031; KEGG K01704].

Mechanistically this is a **dehydration followed by re‑hydration in the opposite orientation** — a net isomerization achieved by a hydro‑lyase, exactly analogous to aconitase's citrate ⇌ isocitrate interconversion via *cis*‑aconitate. UniProt annotates the function as *"Catalyzes the isomerization between 2‑isopropylmalate and 3‑isopropylmalate, via the formation of 2‑isopropylmaleate"* [Q88LE7, HAMAP‑Rule MF_01031].

**Experimental support for the reaction and complex** comes from classical work on the enterobacterial enzyme:
- IPMI *"is a complex enzyme composed of two subunits which are coded for by two genes of the leucine operon, leuC and leuD … The native isopropylmalate isomerase was shown to have a Km for its substrate alpha‑isopropylmalate of 3 × 10⁻⁴ M"* (Fultz & Kemper, *J. Bacteriol.* 1981, PMID 7026530).
- The functional complex *"catalyzes the stereospecific conversion reaction of α‑isopropylmalate to β‑isopropylmalate"* (Manikandan et al., 2011, PMID 20938981).

**Substrate specificity.** The primary physiological substrate is **2‑isopropylmalate** (the isopropyl‑substituted malate). KEGG maps ortholog K01704 to a **secondary activity, EC 4.2.1.35 ((R)‑2‑methylmalate/citramalate dehydratase**, C5‑branched dibasic acid metabolism, pathway ppu00660), reflecting the modest substrate promiscuity typical of aconitase‑superfamily [4Fe‑4S] hydro‑lyases toward the closely related 2‑methylmalate/citraconate. In *Leptospira interrogans*, the leucine‑pathway IPMI (EC 4.2.1.33) participates in a threonine‑independent isoleucine route acting on citraconate‑type substrates, directly illustrating this family flexibility (Xu et al., 2004, PMID 15292141). The **superfamily assignment is explicit**: *"In the aconitase superfamily, which includes the archetypical aconitase, homoaconitase, and isopropylmalate isomerase…"* (Watanabe et al., 2016, PMID 27929065).

---

## 3. Molecular Role of LeuD within the Enzyme

IPMI is an **obligate heterodimer**; LeuD alone is inert. Biochemical purification from *Salmonella typhimurium* resolved two copurifying polypeptides — **51 kDa (LeuC)** and **23.5 kDa (LeuD)** — and both are required, as shown by in‑vitro complementation of *leuC* and *leuD* mutant extracts (Fultz & Kemper 1981, PMID 7026530). Genetic work confirmed that *"the isopropylmalate isomerase of Salmonella typhimurium and Escherichia coli is a complex of the leuC and leuD gene products"* (Stover et al., 1988, PMID 2838459), and that a 22‑kDa LeuD functional analog (newD) can restore leucine prototrophy by pairing with LeuC (Kemper 1974, PMID 4612005).

**Division of labor:**
- **LeuC (large subunit)** harbors the catalytic **[4Fe‑4S] cluster** and most active‑site residues (aconitase domains 1–3).
- **LeuD (small subunit, this protein)** supplies **domain 4, the "swivel" domain** of the aconitase fold. In single‑chain aconitase this domain is part of one polypeptide; in bacterial IPMI the fold is **split across two genes**, and LeuD reconstitutes the active‑site cleft at the LeuC–LeuD interface.

Crystallography of *M. tuberculosis* LeuD (to 1.2 Å) localized LeuD's two most flexible, functionally critical regions: *"the regions of residues 30‑37, the substrate discriminating loop, and of residues 70‑74, the substrate binding loop"* (Manikandan et al., 2011, PMID 20938981). The same study found *"the presence of two LeuD subfamilies"* — consistent with the UniProt assignment of Q88LE7 to **LeuD type‑1** — and showed by solution scattering that the LeuC and LeuCD shapes differ radically from mitochondrial aconitase, underscoring the distinct two‑chain architecture. Thus LeuD acts as a **structural + substrate‑specificity subunit**: it completes the catalytic machinery and its loops discriminate the isopropylmalate substrate, but it does not itself carry the cofactor.

---

## 4. Cofactor and Catalytic Chemistry

IPMI is a **[4Fe‑4S] iron–sulfur enzyme**. The cluster (on LeuC) coordinates a substrate hydroxyl/carboxylate and activates it for dehydration, exactly as in aconitase. Evidence that catalytic competence depends on Fe–S assembly:
- Apo‑IPMI is activated by cluster transfer: *"The assembled Fe/S cluster could be transferred from SufU to the apo form of isopropylmalate isomerase Leu1, rapidly forming catalytically active [4Fe‑4S]‑containing holo‑enzyme"* (Albrecht et al., 2010, PMID 20097860).
- Impaired Fe–S biogenesis lowers IPMI activity, and IPMI is classed among *"cytosolic Fe‑S enzymes (sulfite reductase and isopropylmalate isomerase)"* (Patil et al., 2012, PMID 23192348).

LeuD itself does not bind the cluster but is required to build the catalytic site around it.

---

## 5. Localization

Leucine biosynthesis in bacteria is a **cytoplasmic** process, and IPMI is a soluble cytoplasmic enzyme. In eukaryotes the orthologous isopropylmalate isomerase (Leu1) is explicitly described as a **cytosolic Fe‑S enzyme** (Patil et al., 2012, PMID 23192348); in the prokaryote *P. putida*, which lacks such compartmentalization, the LeuCD complex operates in the cytoplasm. Consistent with this, UniProt Q88LE7 carries **no membrane, signal‑peptide, or secretion annotation** — the protein is a soluble cytoplasmic subunit.

---

## 6. Biological Pathway and Genomic Context in *P. putida*

**Pathway placement.** LeuCD catalyzes **step 2 of 4** of *"L‑leucine from 3‑methyl‑2‑oxobutanoate (2‑oxoisovalerate)"* (UniProt PATHWAY; KEGG module **M00432**, "Leucine biosynthesis, 2‑oxoisovalerate ⇒ 2‑oxoisocaproate"):

1. **LeuA** (2‑isopropylmalate synthase) — condenses 2‑oxoisovalerate + acetyl‑CoA → 2‑isopropylmalate
2. **LeuCD** (this enzyme) — 2‑isopropylmalate ⇌ 3‑isopropylmalate (via 2‑isopropylmaleate)
3. **LeuB** (3‑isopropylmalate dehydrogenase, EC 1.1.1.85) — oxidative decarboxylation → 2‑oxoisocaproate
4. **IlvE/aminotransferase** — transamination → **L‑leucine**

KEGG also maps PP_1986 to valine/leucine/isoleucine biosynthesis (ppu00290), 2‑oxocarboxylic‑acid metabolism (ppu01210), C5‑branched dibasic acid metabolism (ppu00660), and the biosynthesis‑of‑amino‑acids map (ppu01230). This branched‑chain‑amino‑acid pathway is **absent in humans**, which is why IPMI is of interest as an antibacterial/antifungal target (Manikandan et al., 2011, PMID 20938981).

**Genomic organization (KEGG genome coordinates).** In *P. putida* KT2440 the leucine genes are clustered:
- **leuC = PP_1985** (large subunit), 2,250,670–2,252,103
- **leuD = PP_1986** (this gene), 2,252,100–2,252,744
- **PP_1987**, UbiE/COQ5‑family methyltransferase, 2,252,863–2,253,627
- **leuB = PP_1988** (3‑isopropylmalate dehydrogenase), 2,253,682–2,254,764
- **PP_1984**, LysR‑family transcriptional regulator (opposite strand), upstream

Critically, **leuC and leuD overlap by 4 bp** (an ATGA‑type overlap), the hallmark of **translational coupling** that ensures the two subunits of the obligate heterodimer are produced in **matched stoichiometry**. The clustering of leuC–leuD with leuB mirrors the *leu* operon organization of enterobacteria and supports co‑regulated expression of the pathway.

**Regulation (family context).** In other bacteria the *leuCD* operon is under end‑product (branched‑chain amino acid) control — e.g., strong repression by leucine/isoleucine/valine in *Streptomyces coelicolor* (Craster et al., 1999, PMID 10517590) and dedicated transcriptional regulators in mycobacteria (Rv2989/IclR‑like; Angara et al., 2018, PMID 29523332). The LysR‑family regulator adjacent to the *P. putida* cluster (PP_1984) is a plausible local regulator, consistent with this general theme (inference from genomic context; not experimentally proven for *P. putida*).

---

## 7. Evidence That the Function Transfers to the *P. putida* Protein

- **Sequence orthology (bioinformatic).** Global Needleman–Wunsch alignment gives **67.3 % identity (134/199 aligned residues, 93 % coverage) between *P. putida* LeuD (Q88LE7) and experimentally characterized *E. coli* LeuD (P30126)** — far above the ~25–30 % "twilight zone," establishing unambiguous orthology. Alignment to the *M. tuberculosis* crystallographic LeuD fragment gave 43.5 % identity over its length.
- **Structural prediction (AlphaFold).** The AlphaFold DB model AF‑Q88LE7‑F1 is **highly confident (mean pLDDT 95.9; 93 % of residues >90, 0 % <50)**, describing a single compact swivel domain consistent with IPMI_Swivel (IPR033940). The only region of relatively reduced confidence is an N‑terminal loop (~res 30–37, homologous to the *M. tuberculosis* "substrate‑discriminating loop"; pLDDT ~84), independently echoing the crystallographic finding that this specificity loop is the most mobile element of LeuD, while the "substrate‑binding loop" region (~res 70–74) is highly ordered (pLDDT ~98).
- **Rule‑based annotation.** HAMAP family rule **MF_01031** (curated, expert‑derived) assigns the reaction, pathway, subunit composition, and family.
- **Experimental biochemistry** (Salmonella/E. coli): subunit composition, Km, complementation (PMIDs 7026530, 2838459, 374346, 4612005).
- **Structural biology** (M. tuberculosis): fold, substrate loops, two subfamilies (PMID 20938981).
- **Cofactor biochemistry** (yeast/*B. subtilis*): [4Fe‑4S] requirement, cytosolic localization (PMIDs 20097860, 23192348).

---

## 8. Supported and Refuted Hypotheses

**Supported:**
- H1 — *leuD encodes the small subunit of IPMI catalyzing step 2 of leucine biosynthesis.* ✅ (database + orthology + literature)
- H2 — *LeuD is catalytically inert alone and functions only as a LeuC–LeuD heterodimer.* ✅ (PMIDs 7026530, 2838459)
- H3 — *The enzyme is an aconitase‑family [4Fe‑4S] cytoplasmic hydro‑lyase; cluster on LeuC, specificity loops on LeuD.* ✅ (PMIDs 27929065, 20097860, 23192348, 20938981)
- H4 — *In P. putida, leuC/leuD are translationally coupled within a leucine gene cluster.* ✅ (KEGG coordinates)

**Refuted / not supported:**
- LeuD is **not** an independent catalytic enzyme, **not** the cofactor‑bearing subunit, and **not** membrane‑associated or secreted.
- No evidence for a distinct "same‑symbol, different‑gene" identity — the annotation is unambiguous.

---

## 9. Limitations and Future Directions

- **No *P. putida*‑specific enzymology.** Kinetic parameters (Km, kcat), the exact stereochemistry, and the physiological reversibility have been measured in *Salmonella*/*E. coli*, not in *P. putida* itself; transfer is by strong orthology (67 % identity), which is highly reliable for a conserved primary‑metabolic enzyme but remains an inference.
- **No experimental structure of the *P. putida* LeuCD complex.** Structural claims derive from the *M. tuberculosis* LeuD crystal structure and aconitase homology; an AlphaFold model of Q88LE7 could confirm the swivel fold and loop positions.
- **Regulation in *P. putida* is inferred** from genomic context (adjacent LysR regulator; family‑wide BCAA end‑product control), not directly demonstrated.
- **Secondary EC 4.2.1.35 activity** is a database (KEGG) inference for the orthology group; its physiological relevance in *P. putida* is untested.
- **Essentiality/fitness** under leucine‑replete vs. minimal conditions could be confirmed with existing *P. putida* RB‑TnSeq datasets.

---

### Key References
- Fultz & Kemper (1981) *J. Bacteriol.* PMID **7026530** — two‑subunit composition, Km.
- Stover, Kemper & Marsh (1988) PMID **2838459** — LeuC/LeuD complex; newD.
- Kemper (1974) PMID **4612005** / Fultz, Kwoh & Kemper (1979) PMID **374346** — leuC–leuD complementation, subunit substitution.
- Manikandan et al. (2011) *(structural studies on LeuCD, M. tuberculosis)* PMID **20938981** — crystal structure, substrate loops, subfamilies.
- Watanabe et al. (2016) PMID **27929065** — aconitase superfamily membership.
- Albrecht et al. (2010) PMID **20097860** — [4Fe‑4S] activation of IPMI.
- Patil et al. (2012) PMID **23192348** — cytosolic Fe‑S IPMI.
- Xu et al. (2004) PMID **15292141** — IPMI substrate flexibility (citraconate route).
- Angara et al. (2018) PMID **29523332**; Craster et al. (1999) PMID **10517590** — leuCD operon regulation (family context).
- Databases: UniProt **Q88LE7** (HAMAP **MF_01031**); KEGG **ppu:PP_1986** / **K01704** / module **M00432**; Rhea **RHEA:32287**.


## Artifacts

- [OpenScientist final report](leuD-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](leuD-deep-research-openscientist_artifacts/final_report.pdf)