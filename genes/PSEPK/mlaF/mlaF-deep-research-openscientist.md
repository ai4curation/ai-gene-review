---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T02:37:33.866111'
end_time: '2026-09-01T03:42:08.150056'
duration_seconds: 3874.28
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: mlaF
  gene_symbol: mlaF
  uniprot_accession: Q88P94
  protein_description: 'RecName: Full=Intermembrane phospholipid transport system
    ATP-binding protein MlaF {ECO:0000256|ARBA:ARBA00070083};'
  gene_info: Name=mlaF {ECO:0000313|EMBL:AAN66583.1}; OrderedLocusNames=PP_0958 {ECO:0000313|EMBL:AAN66583.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the ABC transporter superfamily. MlaF family.
  protein_domains: AAA+_ATPase. (IPR003593); ABC_transporter-like_ATP-bd. (IPR003439);
    ABC_transporter-like_CS. (IPR017871); P-loop_NTPase. (IPR027417); ABC_tran (PF00005)
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
  path: mlaF-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: mlaF-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88P94
- **Protein Description:** RecName: Full=Intermembrane phospholipid transport system ATP-binding protein MlaF {ECO:0000256|ARBA:ARBA00070083};
- **Gene Information:** Name=mlaF {ECO:0000313|EMBL:AAN66583.1}; OrderedLocusNames=PP_0958 {ECO:0000313|EMBL:AAN66583.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the ABC transporter superfamily. MlaF family.
- **Key Domains:** AAA+_ATPase. (IPR003593); ABC_transporter-like_ATP-bd. (IPR003439); ABC_transporter-like_CS. (IPR017871); P-loop_NTPase. (IPR027417); ABC_tran (PF00005)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "mlaF" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'mlaF' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **mlaF** (gene ID: mlaF, UniProt: Q88P94) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: MlaF (Q88P94, PP_0958) — *Pseudomonas putida* KT2440

## 1. Summary (Answer to the Research Question)

**MlaF is the cytoplasmic ATP-binding/ATPase (nucleotide-binding domain, NBD) subunit of the inner-membrane ABC transporter MlaFEDB, the engine of the Mla (Maintenance of Lipid Asymmetry) system.** By binding and hydrolyzing ATP at the cytoplasmic face of the inner membrane, MlaF powers the transport of glycerophospholipids across the inner membrane as part of a cell-envelope-spanning pathway (MlaA–OmpC/F in the outer membrane → periplasmic shuttle MlaC → MlaFEDB in the inner membrane). The primary physiological role of this pathway is the **retrograde removal of mislocalized phospholipids from the outer leaflet of the outer membrane back to the inner membrane**, thereby maintaining outer-membrane (OM) lipid asymmetry and the permeability barrier that protects Gram-negative bacteria against antibiotics and other toxic compounds.

> **Identity verification.** The UniProt record (Q88P94; gene *mlaF*; ordered locus PP_0958; ABC-transporter superfamily / MlaF family; domains AAA+/P-loop NTPase and ABC transporter ATP-binding, PF00005) is fully consistent with the "MlaF" characterized experimentally in *E. coli*, *A. baumannii*, and *Pseudomonas aeruginosa*. No *P. putida* KT2440-specific biochemical study of MlaF was found; the functional annotation below is therefore established from well-characterized orthologs and from the conserved domain architecture, which are highly conserved across diderm (Gram-negative) bacteria. This is a confident annotation by orthology, not a case of gene-symbol ambiguity.

## 2. Molecular Function and Substrate

- **Enzymatic activity / role:** MlaF is a nucleotide-binding domain of the ABC transporter superfamily. Its Walker A (P-loop), Walker B, and ABC-signature motifs (reflected in InterPro IPR003439/IPR003593/IPR017871/IPR027417 and Pfam PF00005) bind and hydrolyze ATP. Two MlaF protomers form the NBD dimer of the MlaFEDB complex; ATP binding drives NBD dimerization and the conformational cycle that translocates lipid substrate through the transmembrane MlaE permease [PMID 33236984; PMID 33199922].
- **Substrate of the transporter it powers:** glycerophospholipids. The cryo-EM structure of MlaFEDB captured **two phospholipid molecules bound** along a continuous conduit running from the MlaE substrate-binding site through the MlaD pore, indicating phospholipids are the transported substrate [PMID 33236984].
- **Mechanistic caveat:** while MlaF is unambiguously the ATPase, precisely how ATP hydrolysis is coupled to the direction and steps of lipid movement is still debated and not fully resolved [PMID 39080293].
- **Organism-specific sequence evidence:** A motif scan of the actual 269-residue *P. putida* MlaF (Q88P94) confirms a complete, intact ABC nucleotide-binding active site: **Walker A / P-loop `GPSGCGKT` (res 41–48)**, **Q-loop Gln (res ~92)**, **ABC signature / C-loop `LSGGM` (res 145–149)**, **Walker B `ILMYDE` with the catalytic Asp/Glu (res 165–170)**, and the **H-loop switch histidine `VSHD` (res 201–204)**. The presence of all catalytic elements (P-loop for phosphate binding, Walker B Asp/Glu for Mg²⁺ coordination and hydrolysis, switch His for γ-phosphate sensing) indicates the *P. putida* protein itself is a catalytically competent ATPase, not merely inferred from orthologs.

## 3. Localization

- MlaF is a **peripheral cytoplasmic-membrane protein**: the NBDs sit on the **cytoplasmic (inner) face of the inner membrane**, coupled to the integral-membrane MlaE permease dimer, the periplasmic MCE domain hexamer MlaD, and the small regulatory subunit MlaB [PMID 33236984; PMID 33199922].
- The complex it belongs to (MlaFEDB) is one of three sub-cellular assemblies of the Mla pathway, which spans the entire Gram-negative cell envelope: **MlaA–OmpC/F (outer membrane)**, **MlaC (periplasm)**, **MlaFEDB (inner membrane)** [PMID 39080293; PMID 34753108].

## 4. Pathway and Biological Process

The Mla system maintains OM lipid asymmetry — lipopolysaccharide in the OM outer leaflet, glycerophospholipids in the inner leaflet. Glycerophospholipids that mislocalize to the OM outer leaflet compromise the barrier; the Mla pathway removes them:

1. **MlaA–OmpC/F** extracts mislocalized phospholipids from the OM outer leaflet.
2. **MlaC** shuttles the lipid across the periplasm (binding either MlaA or MlaD, one at a time) [PMID 37100290; PMID 39080293].
3. **MlaFEDB**, energized by **MlaF ATP hydrolysis**, receives the lipid at MlaD and moves it into the inner membrane.

Genetic and, more decisively, in vitro reconstitution/biochemical studies support **retrograde** (OM→IM) directionality, resolving an earlier anterograde-vs-retrograde debate [PMID 36459067; PMID 34753108]. Physiologically, loss of Mla function increases membrane permeability and antibiotic susceptibility, promotes outer-membrane vesicle blebbing, and reduces virulence [PMID 39080293]. In the closely related *Pseudomonas aeruginosa*, deleting the OM component *mlaA* increases fluoroquinolone susceptibility and reduces rhamnolipid secretion, motility, and biofilm formation — illustrating the pathway's envelope-integrity role in pseudomonads [PMID 37660742].

## 5. Structural/Family Classification and Regulation

- MlaFEDB is proposed to be the **founding member of a structurally distinct ABC superfamily**, with distant relationships to LPS, MacAB, and eukaryotic ABCA/ABCG transporters; MlaE has minimal sequence similarity to classical permeases [PMID 39080293; PMID 33236984; PMID 35981415].
- MlaF partners directly with **MlaB, a small cytoplasmic STAS-domain subunit** that assembles with and supports MlaF; the MlaB–MlaF interface and the non-canonical features distinguishing Mla proteins from classical ABC components are areas of active study [PMID 41047745].

## 6. Supported vs. Refuted Hypotheses

- **Supported:** MlaF is the ATP-binding/ATPase subunit of the MlaFEDB inner-membrane ABC transporter (domain + structural evidence). Substrate = glycerophospholipids. Localization = cytoplasmic face of the inner membrane. Pathway = Mla, retrograde phospholipid transport maintaining OM asymmetry.
- **Refuted/deprioritized:** Purely anterograde (IM→OM) transport as the primary function — recent biochemistry favors retrograde [PMID 36459067].
- **Open:** The exact coupling of MlaF ATP hydrolysis to individual lipid-transfer steps [PMID 39080293].

## 7. Limitations and Future Directions

- All mechanistic evidence derives from orthologs (*E. coli*, *A. baumannii*, *P. aeruginosa*); a direct *P. putida* KT2440 MlaF study was not identified. However, annotation transfer is well justified: a global alignment of *P. putida* MlaF (Q88P94, 269 aa) against experimentally/structurally characterized *E. coli* MlaF (P63386, 269 aa) gives **57.6% identity (155/269) over the full length with a 1:1 ungapped correspondence** — a clear one-to-one ortholog far above the ~30% threshold for confident functional transfer. Combined with the intact ABC-ATPase active site (Section 2) and near-universal conservation of Mla in diderms, the annotation transfers with high confidence.
- Future work specific to *P. putida* could test whether *mlaF* deletion affects the organism's notable solvent tolerance and envelope robustness, and could confirm ATP-hydrolysis-dependent retrograde phospholipid transport in the KT2440 complex directly.

---
*Key references: PMID 33236984 (Coudray 2020, MlaFEDB structure with substrate); PMID 33199922 (Tang 2021, nucleotide-bound structures + transport assays); PMID 39080293 (Wotherspoon 2024, MlaC–MlaD, ABC-superfamily statement); PMID 36459067 (Abellon-Ruiz 2023, transport direction); PMID 34753108 (Low & Chng 2021, pathway review); PMID 35981415 (Ekiert 2022, mechanism review); PMID 37100290 (MacRae 2023, interactions); PMID 41047745 (Dutta 2026, component analysis); PMID 37660742 (Kaur 2023, Pseudomonas mlaA phenotypes).*


## Artifacts

- [OpenScientist final report](mlaF-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](mlaF-deep-research-openscientist_artifacts/final_report.pdf)