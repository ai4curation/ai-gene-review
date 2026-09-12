---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-17T05:39:29.248621'
end_time: '2026-07-17T05:51:42.205579'
duration_seconds: 732.96
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: hisC
  gene_symbol: hisC
  uniprot_accession: Q88P86
  protein_description: 'RecName: Full=Histidinol-phosphate aminotransferase {ECO:0000255|HAMAP-Rule:MF_01023};
    EC=2.6.1.9 {ECO:0000255|HAMAP-Rule:MF_01023}; AltName: Full=Imidazole acetol-phosphate
    transaminase {ECO:0000255|HAMAP-Rule:MF_01023};'
  gene_info: Name=hisC {ECO:0000255|HAMAP-Rule:MF_01023}; OrderedLocusNames=PP_0967;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the class-II pyridoxal-phosphate-dependent
  protein_domains: Aminotrans_II_pyridoxalP_BS. (IPR001917); Aminotransferase_I/II_large.
    (IPR004839); HisP_aminotrans. (IPR005861); HistidinolP_aminotransfase. (IPR050106);
    PyrdxlP-dep_Trfase. (IPR015424)
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
  path: hisC-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: hisC-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88P86
- **Protein Description:** RecName: Full=Histidinol-phosphate aminotransferase {ECO:0000255|HAMAP-Rule:MF_01023}; EC=2.6.1.9 {ECO:0000255|HAMAP-Rule:MF_01023}; AltName: Full=Imidazole acetol-phosphate transaminase {ECO:0000255|HAMAP-Rule:MF_01023};
- **Gene Information:** Name=hisC {ECO:0000255|HAMAP-Rule:MF_01023}; OrderedLocusNames=PP_0967;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the class-II pyridoxal-phosphate-dependent
- **Key Domains:** Aminotrans_II_pyridoxalP_BS. (IPR001917); Aminotransferase_I/II_large. (IPR004839); HisP_aminotrans. (IPR005861); HistidinolP_aminotransfase. (IPR050106); PyrdxlP-dep_Trfase. (IPR015424)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "hisC" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'hisC' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **hisC** (gene ID: hisC, UniProt: Q88P86) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of *hisC* (Q88P86, PP_0967) in *Pseudomonas putida* KT2440

**Gene:** *hisC* (OrderedLocusName PP_0967)
**Protein:** Histidinol-phosphate aminotransferase (HisC); AltName: imidazole-acetol-phosphate transaminase
**UniProt:** Q88P86 · **EC:** 2.6.1.9 · **KEGG Ortholog:** K00817
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / NCIMB 11950 / **KT2440**)

---

## 1. Summary (Answer to the Research Question)

*hisC* encodes **histidinol-phosphate aminotransferase (HisC, EC 2.6.1.9)**, a soluble, cytoplasmic, pyridoxal-5′-phosphate (PLP)-dependent **class-II aminotransferase** that catalyzes the **seventh step of de novo L-histidine biosynthesis**. Working as a **homodimer**, it performs a reversible transamination that, in the biosynthetic direction, transfers the α-amino group of **L-glutamate onto imidazole-acetol phosphate (3-(imidazol-4-yl)-2-oxopropyl phosphate)** to yield **L-histidinol phosphate + 2-oxoglutarate**. Its substrate specificity is dominated by recognition of the substrate **phosphate group**; members of this subfamily can additionally act as aromatic-amino-acid aminotransferases. In *P. putida* the gene sits in a compact **hisG–hisD–hisC** cluster and is **conditionally essential** — its loss causes histidine auxotrophy on minimal medium.

The identity of the target was rigorously verified: gene symbol, organism, EC number, protein family, and catalytic residues are all mutually consistent across UniProt, KEGG, and the primary structural literature on close orthologs. **No gene-symbol ambiguity was encountered.**

---

## 2. Identity Verification

| Attribute | Provided target | Confirmed by this study |
|---|---|---|
| Gene symbol | *hisC* | UniProt Q88P86; KEGG ppu:PP_0967 (SYMBOL hisC) |
| Enzyme | Histidinol-phosphate aminotransferase, EC 2.6.1.9 | UniProt catalytic activity; KEGG KO K00817; EC 2.6.1.9 |
| Organism | *P. putida* KT2440 | KEGG ORGANISM ppu; UniProt organism |
| Family | Class-II PLP-dependent aminotransferase | UniProt SIMILARITY; KEGG BRITE "Aminotransferase Class II"; Pfam Aminotran_1_2 |
| Locus/position | PP_0967 | KEGG POSITION 1,106,849–1,107,895 |

All identifiers converge on a single, well-characterized enzyme family. The verification requirement is satisfied.

---

## 3. Primary Function: Reaction Catalyzed and Substrate Specificity

### 3.1 The reaction
HisC catalyzes the PLP-dependent, reversible transamination (UniProt Q88P86 catalytic activity):

> **L-histidinol phosphate + 2-oxoglutarate ⇌ 3-(imidazol-4-yl)-2-oxopropyl phosphate (imidazole-acetol phosphate) + L-glutamate**

Physiologically, the enzyme operates in the **biosynthetic (amination) direction**: "histidinol-phosphate aminotransferase catalyzes the transfer of the amino group from glutamate to imidazole acetol-phosphate producing 2-oxoglutarate and histidinol phosphate" (Fernández et al., 2004, PMID 15007066). This is the **seventh step in the synthesis of histidine within eubacteria** (Sivaraman et al., 2001, PMID 11518529), corresponding to **step 7 of 9** from 5-phospho-α-D-ribose-1-diphosphate (PRPP) in the UniProt/KEGG pathway map (KEGG module M00026).

### 3.2 Substrate specificity
- The **natural substrate pair** is L-histidinol phosphate / 2-oxoglutarate (amino donor L-glutamate in the biosynthetic direction).
- The **substrate phosphate group is the principal specificity determinant**. In *Corynebacterium glutamicum* HisC, "the hydrogen bond between the side chain of this residue [Tyr21] and the phosphate group of His-P is important for recognition of the natural substrate and discrimination against other potential amino donors such as phenylalanine and leucine" (Marienhagen et al., 2008, PMID 18560156).
- **Family-level substrate promiscuity / moonlighting:** In organisms lacking dedicated aromatic aminotransferases, HisC also transaminates aromatic amino acids. The *Thermotoga maritima* enzyme "accepts histidinol phosphate, tyrosine, tryptophan, and phenylalanine, but not histidine, as substrates" (Fernández et al., 2004, PMID 15007066). Consistent with this, **KEGG maps P. putida PP_0967 not only to histidine metabolism (ppu00340) but also to tyrosine (ppu00350), phenylalanine (ppu00360), and aromatic amino acid biosynthesis (ppu00400)** pathways. However, this mapping reflects **family-level catalytic capacity rather than a demonstrated dedicated role**: *P. putida* KT2440 encodes **two dedicated aromatic-amino-acid aminotransferases (PP_1972 and PP_3590; KEGG K00832, EC 2.6.1.57)**, whereas *T. maritima*—where HisC broadens to aromatic substrates—lacks such enzymes. Any aromatic-amino-acid transamination by *P. putida* HisC is therefore likely **biochemically possible but physiologically redundant/minor**, and has not been directly demonstrated.
- Genetic corroboration of the pathway step: *hisC* mutants (in *Micrococcus luteus*) "accumulated imidazoleacetol" (Kane-Falce & Kloos, 1975, PMID 1126626), confirming HisC acts at the imidazole-acetol(-phosphate) node.

---

## 4. Mechanism, Cofactor, and Quaternary Structure

- **Cofactor:** pyridoxal 5′-phosphate (PLP), covalently bound as an **internal aldimine (Schiff base) at Lys210** of *P. putida* HisC (UniProt "N6-(pyridoxal phosphate)lysine" at residue 210).
- **Catalytic cycle:** classic aminotransferase **ping-pong (two half-reaction)** mechanism cycling between the PLP and pyridoxamine-5′-phosphate (PMP) forms. In the *E. coli* ortholog, a covalent tetrahedral complex "consisting of PLP and l-histidinol phosphate attached to Lys214" was captured crystallographically, resembling the transient gem-diamine intermediate (Sivaraman et al., 2001, PMID 11518529). PMP-enzyme complexes have been trapped in both *E. coli* (PMID 11518529) and *C. glutamicum* (PMID 18560156).
- **Quaternary structure:** **homodimer**. "HisC is a dimeric enzyme with a mass of approximately 80 kDa" (Sivaraman et al., 2001, PMID 11518529); UniProt lists Q88P86 as a homodimer. Each monomer comprises a large α/β/α PLP-binding domain plus a small domain, with an N-terminal arm contributing to dimerization; the active site lies at the dimer interface.
- **Conserved catalytic apparatus in Q88P86 (direct sequence evidence):** A global alignment of Q88P86 against the crystallographically characterized *E. coli* HisC (P06986) shows the active-site residues are conserved — **Tyr55→Tyr57, Asp184→Asp181, Tyr187→Tyr184, Ser213→Ser209, Lys214→Lys210, Arg222→Arg218**. The reference set is described as: "Residues that interact with the PLP cofactor, including Tyr55, Asn157, Asp184, Tyr187, Ser213, Lys214 and Arg222, are conserved in the family of aspartate, tyrosine and histidinol phosphate aminotransferases" (Sivaraman et al., 2001, PMID 11518529). The mapped catalytic lysine (Lys214→**Lys210**) matches UniProt's independent PLP-attachment annotation exactly, validating the alignment. Asp181 stabilizes the protonated PLP pyridinium nitrogen (a fold-type-I/class-II hallmark), Arg218 binds the substrate α-carboxylate/2-oxoglutarate, and Tyr57 contributes to substrate/phosphate binding. This upgrades the annotation from database transfer to **residue-level evidence that Q88P86 is a catalytically competent HisC**.

---

## 5. Subcellular Localization

HisC acts in the **cytoplasm** as a soluble enzyme. UniProt Q88P86 shows **no signal peptide, transmembrane segment, or lipidation/anchor**; all characterized bacterial orthologs (*E. coli*, *Salmonella typhimurium*, *C. glutamicum*, *T. maritima*) are soluble proteins purified from soluble extracts and crystallized as such (e.g., "Crystalline L-histidinol phosphate aminotransferase from *Salmonella typhimurium*", Henderson & Snell, 1973, PMID 4632247). Its substrates are cytosolic phosphorylated intermediates and glutamate/2-oxoglutarate. The entire de novo histidine biosynthetic pathway is cytoplasmic, so HisC exerts its function there.

---

## 6. Pathway Context and Biological Role

- **Pathway:** de novo **L-histidine biosynthesis** (PRPP → histidine), an unbranched, ancient pathway. HisC provides the **transamination that installs the α-amino group of the histidine backbone**, converting imidazole-acetol phosphate to L-histidinol phosphate. The immediately downstream enzyme HisD (histidinol dehydrogenase) then oxidizes L-histidinol phosphate/L-histidinol to L-histidine. (Pathway architecture reviewed in Alifano et al., 1996, *Microbiol. Rev.*, PMID 8852895.)
- **Amino-donor coupling:** By consuming L-glutamate and releasing 2-oxoglutarate, HisC links histidine biosynthesis to the cell's central **glutamate/2-oxoglutarate nitrogen pool**.
- **Genomic organization / co-regulation:** In *P. putida* KT2440, *hisC* (PP_0967) lies immediately downstream of **hisG** (PP_0965, ATP phosphoribosyltransferase — the first, feedback-regulated step) and **hisD** (PP_0966, histidinol dehydrogenase — the terminal steps), all on the same strand. *hisD* and *hisC* are separated by only **2 bp**, indicating translational coupling and operon-like co-transcription of a **hisG–hisD–hisC** cluster. This physically and transcriptionally embeds HisC within the histidine biosynthetic program.
- **Physiological requirement (organism-specific):** A genome-wide mini-Tn5 transposon screen of *P. putida* KT2440 identified de novo amino-acid biosynthesis genes as **conditionally essential** on glucose minimal medium — "Auxotrophs for all amino acids predicted by the in silico models were found" (Molina-Henares et al., 2010, PMID 20158506). Because HisC catalyzes an obligatory, non-bypassable step of the single linear histidine pathway (no isozyme), *hisC* loss yields **histidine auxotrophy**: required for prototrophic growth but dispensable when histidine is supplied.

---

## 7. Evidence Summary

| Claim | Evidence type | Source |
|---|---|---|
| EC 2.6.1.9; His-P aminotransferase; step 7 of His biosynthesis | Database annotation + primary structural lit. | UniProt Q88P86; KEGG K00817; PMID 11518529, 15007066 |
| PLP cofactor at Lys210; ping-pong (PLP↔PMP) mechanism | UniProt residue annotation + ortholog crystal structures | UniProt Q88P86; PMID 11518529, 18560156 |
| Homodimer, ~80 kDa | Ortholog biochemistry/crystallography | PMID 11518529; UniProt |
| Catalytic residues conserved in Q88P86 | Bioinformatic alignment (this study) | vs P06986; PMID 11518529 |
| Phosphate-group specificity; aromatic-AA moonlighting | Site-directed mutagenesis + substrate assays | PMID 18560156, 15007066; KEGG pathway mapping |
| Cytoplasmic, soluble | Sequence features + ortholog purification | UniProt Q88P86; PMID 4632247 |
| hisGDC cluster / co-regulation | Genome coordinates | KEGG ppu genome |
| Conditionally essential (His auxotrophy) | Genome-wide transposon screen | PMID 20158506 |

---

## 8. Supported and Refuted Hypotheses

**Supported:**
- H1 — *hisC* encodes a functional PLP-dependent histidinol-phosphate aminotransferase (EC 2.6.1.9). **Strongly supported** (database + conserved catalytic residues incl. Lys210-PLP).
- H2 — HisC operates in the cytoplasm as a soluble homodimer. **Supported.**
- H3 — HisC is embedded in a co-regulated histidine operon (hisG–hisD–hisC) and is required for de novo His synthesis. **Supported** (genomic + auxotrophy evidence).

**Partially supported / open:**
- H4 — *P. putida* HisC physiologically moonlights as an aromatic-amino-acid aminotransferase. **Plausible but unproven, and likely minor**: supported by family behavior (*T. maritima*) and KEGG pathway mapping, but no direct *P. putida* enzymology exists. *P. putida* encodes **two dedicated aromatic-amino-acid aminotransferases (PP_1972, PP_3590; K00832)**, making any HisC moonlighting role physiologically redundant/minor in this organism.

**Refuted / ruled out:**
- The protein is **not** a membrane transporter, structural protein, or signaling molecule; it is a soluble metabolic enzyme (no TM/signal features).
- HisC does **not** transaminate free histidine (orthologs do not accept histidine as substrate).

---

## 9. Limitations and Future Directions

- **No direct enzymology exists for the *P. putida* KT2440 protein itself.** All mechanistic and kinetic detail is transferred from orthologs (*E. coli*, *C. glutamicum*, *T. maritima*, *Salmonella*) plus bioinformatic residue mapping specific to Q88P86. This is standard and well-justified for a HAMAP-ruled housekeeping enzyme, but *P. putida*-specific kinetics (Km for His-P, imidazole-acetol phosphate, glutamate) and any aromatic-AA side activity remain to be measured.
- The **conditional-essentiality inference** for *hisC* rests on pathway logic plus a genome-wide screen that reports amino-acid auxotrophs collectively; a targeted *hisC* knockout with His-supplementation rescue would confirm it directly.
- **Future work:** solve/model the *P. putida* HisC structure (AlphaFold model is available), test aromatic-amino-acid transaminase activity, and define operon boundaries and HisG feedback regulation experimentally.

---

## References (PMIDs)
- Sivaraman J. et al. (2001) Crystal structure of histidinol phosphate aminotransferase (HisC) from *E. coli*. **PMID 11518529**
- Fernández F.J. et al. (2004) Structural studies of the catalytic reaction pathway of a hyperthermophilic HisC (*T. maritima*). **PMID 15007066**
- Marienhagen J. et al. (2008) Substrate recognition by HisC from *C. glutamicum*. **PMID 18560156**
- Kane-Falce & Kloos (1975) Histidine biosynthesis in *Micrococcus luteus*. **PMID 1126626**
- Henderson & Snell (1973) Crystalline His-P aminotransferase from *S. typhimurium*. **PMID 4632247**
- Alifano P. et al. (1996) Histidine biosynthetic pathway and genes. **PMID 8852895**
- Molina-Henares M.A. et al. (2010) Conditionally essential genes for growth of *P. putida* KT2440. **PMID 20158506**
- Rutkiewicz M. et al. (2023) Plant HISN6 substrate specificity/structure. **PMID 36842242**

*Database sources:* UniProt Q88P86; KEGG ppu:PP_0967 (K00817); Pfam Aminotran_1_2; InterPro IPR005861 (HisP_aminotrans), IPR050106.


## Artifacts

- [OpenScientist final report](hisC-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](hisC-deep-research-openscientist_artifacts/final_report.pdf)