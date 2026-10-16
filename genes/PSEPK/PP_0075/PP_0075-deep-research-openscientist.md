---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T04:59:54.775896'
end_time: '2026-08-31T05:15:29.922212'
duration_seconds: 935.15
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_0075
  gene_symbol: PP_0075
  uniprot_accession: Q88RQ4
  protein_description: 'SubName: Full=Choline sulfate transporter {ECO:0000313|EMBL:AAN65709.1};'
  gene_info: OrderedLocusNames=PP_0075 {ECO:0000313|EMBL:AAN65709.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: SLC26A/SulP_dom. (IPR011547); SLC26A/SulP_fam. (IPR001902); STAS_dom.
    (IPR002645); STAS_dom_sf. (IPR036513); STAS (PF01740)
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
citation_count: 9
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PP_0075-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PP_0075-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88RQ4
- **Protein Description:** SubName: Full=Choline sulfate transporter {ECO:0000313|EMBL:AAN65709.1};
- **Gene Information:** OrderedLocusNames=PP_0075 {ECO:0000313|EMBL:AAN65709.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** SLC26A/SulP_dom. (IPR011547); SLC26A/SulP_fam. (IPR001902); STAS_dom. (IPR002645); STAS_dom_sf. (IPR036513); STAS (PF01740)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_0075" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_0075' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_0075** (gene ID: PP_0075, UniProt: Q88RQ4) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: PP_0075 (Q88RQ4), *Pseudomonas putida* KT2440

**Gene:** PP_0075 (OrderedLocusNames PP_0075)
**UniProt:** Q88RQ4
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / NCIMB 11950 / KT2440), NCBI taxon PSEPK
**Automatic annotation under review:** "Choline sulfate transporter" (SubName, from EMBL AAN65709.1)

---

## Summary

PP_0075 encodes an integral inner-membrane secondary transporter belonging to the **SulP / SLC26 anion-permease superfamily**. The 521-residue protein has the canonical two-part architecture of this family: a hydrophobic transmembrane core of ~10 helices (residues ~42–416) that forms the anion-conducting pathway, followed by a C-terminal cytoplasmic **STAS domain** (residues ~434–521) that in this family serves regulatory and protein–protein interaction roles. This architecture is diagnostic and places PP_0075 firmly among bacterial sulfate/anion permeases (Pfam PF00916 Sulfate_transp + PF01740 STAS; InterPro IPR001902/IPR011547; KEGG orthology K03321 "sulfate permease, SulP family"; eggNOG COG0659).

Genomically, PP_0075 is the distal gene of a small **choline-O-sulfate (COS) catabolic operon** in *P. putida* KT2440. It is co-transcribed on the minus strand with an ABC-transporter substrate-binding protein (PP_0076, K02002) and the **betC choline-sulfatase** (PP_0077, EC 3.1.6.6, K01133), and is controlled by a divergently oriented LysR-type regulator (PP_0079). Choline-sulfatase cleaves the sulfate ester of intracellular choline-O-sulfate to release **free choline plus inorganic sulfate**; the choline then feeds the downstream betBA pathway (choline → betaine aldehyde → glycine betaine) as a carbon/nitrogen/energy source. This operonic context tightly links PP_0075 to sulfur and quaternary-ammonium-ester metabolism.

The literal database name — "choline sulfate transporter" — is an **unverified automatic annotation** and is most likely misleading with respect to the transported species. Comparative physiology and family biochemistry argue that the bulky zwitterionic COS molecule is imported by ABC binding-protein systems (as in *Bacillus subtilis* OpuC and rhizobial Cho/Prb systems), whereas SulP-family permeases characteristically move small inorganic anions (sulfate, bicarbonate). The most parsimonious functional assignment is therefore that **PP_0075 transports the inorganic sulfate liberated by choline-sulfatase across the cytoplasmic membrane**, coupling COS catabolism to cellular sulfur handling/assimilation. This substrate assignment is an inference from protein family, genome context, and comparative physiology; direct transport assays on PP_0075 have not been reported. This report lays out the evidence for each of these conclusions and identifies the experiments that would settle the remaining uncertainty.

---

## Key Findings

### F001 — PP_0075 is a SulP/SLC26-family anion permease with a TM core plus C-terminal STAS domain

UniProt Q88RQ4 describes a **521-amino-acid integral membrane protein**. Domain analysis is unambiguous and internally consistent across resources: Pfam assigns **PF00916 (Sulfate_transp)** for the membrane core and **PF01740 (STAS)** for the C-terminal cytoplasmic module; InterPro assigns **IPR001902/IPR011547 (SLC26A/SulP family and domain)** and **IPR002645/IPR036513 (STAS domain and its structural superfamily)**; eggNOG places it in **COG0659 (sulfate permease)**. The UniProt feature table predicts **9–10 helical transmembrane segments spanning residues ~42–416**, followed by a cytoplasmic STAS domain over residues ~434–521. Gene Ontology terms are consistent: C:membrane (GO:0016020) and P:transmembrane transport (GO:0055085).

This two-domain layout is the defining signature of the SLC26/SulP superfamily. As reviewed by Alper & Sharma, "*SLC26 polypeptides are characterized by N-terminal cytoplasmic domains, 10–14 hydrophobic transmembrane spans, and C-terminal cytoplasmic STAS domains*" ([PMID: 23506885](https://pubmed.ncbi.nlm.nih.gov/23506885/)). PP_0075 matches this template precisely (TM core + STAS). The same review notes the functional relevance of bacterial members: "*SulP genes present in antibiotic operons may provide sulfate for antibiotic biosynthetic pathways*" ([PMID: 23506885](https://pubmed.ncbi.nlm.nih.gov/23506885/)) — illustrating that bacterial SulP permeases characteristically transport sulfate/anions, which supports the inferred substrate class for PP_0075.

Structural work on bacterial homologs reinforces the architecture and its mechanistic implications. A *Yersinia enterocolitica* Slc26A protein forms a **transmembrane-stabilized dimer** in which "*the cytoplasmic STAS domain projects away from the transmembrane domain and is not involved in dimerization,*" and "*large movements of the STAS domain underlie the conformational changes that occur during transport*" ([PMID: 21659513](https://pubmed.ncbi.nlm.nih.gov/21659513/)). The *M. tuberculosis* Rv1739c protein is likewise "*a SulP anion permease, related in structure to the SLC26 gene family of metazoan anion exchangers and anion channels*" ([PMID: 19636956](https://pubmed.ncbi.nlm.nih.gov/19636956/)). These homologs establish the fold, oligomeric state, and STAS-driven conformational cycle expected for PP_0075.

### F002 — PP_0075 lies within the *P. putida* KT2440 choline-O-sulfate (COS) utilization gene cluster

The genomic neighborhood of PP_0075 defines its biological context. The adjacent genes are:

| Locus | UniProt | Product | KEGG orthology |
|-------|---------|---------|----------------|
| PP_0075 | Q88RQ4 | SulP-family anion permease | K03321 (sulfate permease) |
| PP_0076 | Q88RQ3 | choline/betaine ABC substrate-binding protein | K02002 |
| PP_0077 | Q88RQ2 | betC choline-sulfatase (EC 3.1.6.6) | K01133 |
| PP_0079 | Q88RQ0 | LysR-type transcriptional regulator | — |
| PP_0080 | Q88RP9 | NAD(P)-binding oxidoreductase | — |

This locus was experimentally described by Galvão and colleagues, who reported that "*the genomic context of the recognized bet genes for choline-O-sulphate (COS) utilization in Pseudomonas putida KT2440 is such that betC (choline sulphatase) lies adjacent to an ATP-binding cassette transporter and a LysR type regulator, but well away from betBA*" ([PMID: 17116241](https://pubmed.ncbi.nlm.nih.gov/17116241/)). PP_0075, PP_0076, and PP_0077 are precisely those "adjacent" genes.

The metabolic logic downstream of the sulfatase is set by the classical bet pathway. In the closely related *Sinorhizobium* system, the enzymes are "*betC (choline sulfatase), betB (betaine aldehyde dehydrogenase), and betA (choline dehydrogenase)*" ([PMID: 12906115](https://pubmed.ncbi.nlm.nih.gov/12906115/)). Thus betC desulfates COS to choline, and the choline is subsequently oxidized (via betA/betB) to glycine betaine, which serves as carbon/nitrogen/energy source. PP_0075 sits at the membrane-transport step of this catabolic module.

### F003 — The precise substrate of PP_0075 is inferred, not directly proven

Galvão et al. attributed **choline-O-sulfate uptake** in KT2440 to the co-encoded ABC transporter (a binding-protein-dependent system, i.e., PP_0076 plus its partners), and demonstrated that betC is required to metabolize **intracellular** COS as a carbon/nitrogen source. Critically, a betC mutant "*still accumulated intact COS but failed to use this compound as carbon or nitrogen source. Furthermore, betC expression was downregulated at high salt concentrations, showing that the principal role of this gene lied in COS metabolism, not in osmoprotection*" ([PMID: 17116241](https://pubmed.ncbi.nlm.nih.gov/17116241/)).

Two important conclusions follow. First, **COS uptake is separable from desulfation** — cells import intact COS even without betC — implying uptake is handled by the ABC binding-protein machinery rather than by PP_0075. Second, the locus functions in **catabolism/sulfur metabolism, not osmoprotection**. PP_0075 itself (a secondary SulP/SLC26 permease, PF00916) was **not individually assayed** in that study. Because SulP family members characteristically transport small inorganic anions (sulfate, bicarbonate) rather than bulky zwitterionic quaternary-ammonium esters, the most plausible role for PP_0075 is the movement of the **sulfate** released intracellularly by betC — a substrate assignment reached by inference rather than direct measurement.

### F004 — Operon structure and orthology: co-transcribed betC–bindingP–SulP under a divergent LysR regulator

KEGG genomic coordinates (organism ppu) place the three catabolic genes contiguously on the minus strand: PP_0077 (choline-sulfatase, complement 87800..89317), PP_0076 (betaine-binding protein, complement 86862..87785), and PP_0075 (SulP permease, complement 85152..86717). The intergenic gaps are only **15 bp (PP_0077→PP_0076)** and **145 bp (PP_0076→PP_0075)**, consistent with a **single operon transcribed betC → binding protein → SulP**. PP_0079 (89426..90325) lies on the **plus strand, divergently oriented** — the canonical arrangement of a LysR-type regulator controlling a divergent catabolic operon.

KEGG orthology assignments reinforce each gene's role: PP_0075 = **K03321** "sulfate permease, SulP family"; PP_0076 = **K02002** "glycine betaine/proline ABC transporter substrate-binding protein"; PP_0077 = **K01133** "choline-sulfatase [EC:3.1.6.6]." The co-localization of a sulfate permease with a sulfate-ester–hydrolyzing sulfatase within one operon is a strong contextual argument that PP_0075 handles the sulfate produced by the pathway.

### F005 — Comparative evidence: COS import is ABC-mediated in other bacteria, supporting a sulfate/anion role for PP_0075

Across bacteria that use COS, the **importer for the intact COS molecule is an ABC system, not a SulP permease.** In *Bacillus subtilis*, "*choline-O-sulfate was specifically acquired from the environment via OpuC*," and the authors "*identified a high-affinity ATP-binding cassette (ABC) transport system responsible for its uptake*" (Km ~4 µM) ([PMID: 9925583](https://pubmed.ncbi.nlm.nih.gov/9925583/)). In *P. putida* KT2440 the COS operon likewise encodes an ABC substrate-binding protein (PP_0076, K02002) that would capture the quaternary-ammonium substrate, while betC (PP_0077) desulfates intracellular COS to choline + sulfate.

This pattern generalizes to related quaternary-ammonium-compound (QAC) transporters in the Rhizobiaceae: *Sinorhizobium meliloti* Cho is "*a highly specific high-affinity choline transporter*" of the ABC class (ChoX binding protein, KD ~2.7 µM) ([PMID: 15342567](https://pubmed.ncbi.nlm.nih.gov/15342567/)), and the Opp-like ABC system Prb takes up proline betaine and "*other quaternary ammonium compounds such as choline*" ([PMID: 16923898](https://pubmed.ncbi.nlm.nih.gov/16923898/)). In every characterized case the QAC substrate is moved by a binding-protein-dependent ABC transporter — never by a SulP permease. Since PP_0075 is orthologous to SulP sulfate permeases (K03321), the comparative evidence points away from "choline sulfate transporter" and toward **inorganic sulfate/anion transport** as its true function.

---

## Mechanistic Model / Interpretation

The findings assemble into a coherent picture of a single catabolic module that lets *P. putida* KT2440 extract carbon, nitrogen, energy, and sulfur from environmental choline-O-sulfate, a common plant/soil osmolyte.

```
   ENVIRONMENT                 PERIPLASM / INNER MEMBRANE                 CYTOPLASM
 ─────────────────────────────────────────────────────────────────────────────────
   Choline-O-sulfate  ──►  ABC substrate-binding protein (PP_0076, K02002)
   (COS, zwitterion)            │  (+ ABC permease/ATPase partners)
                                ▼
                         COS imported intact ───────────────►  COS (cytoplasm)
                                                                     │
                                                       betC choline-sulfatase
                                                       (PP_0077, EC 3.1.6.6)
                                                                     │
                                            ┌────────────────────────┴───────────┐
                                            ▼                                     ▼
                                        CHOLINE                            INORGANIC SULFATE
                                            │                                     │
                                betA / betB (elsewhere on genome)         PP_0075 SulP permease
                                            ▼                              (K03321) moves sulfate
                                   glycine betaine ──► C/N/energy          across membrane → sulfur
                                                                            assimilation / homeostasis

   Regulation:  LysR-type regulator PP_0079 (divergent, plus strand) controls the
                betC–bindingP–SulP operon (minus strand, transcribed 0077→0076→0075).
```

**Why PP_0075 is best modeled as a sulfate/anion permease rather than a COS importer:**

1. **Family biochemistry.** SulP/SLC26 permeases transport small inorganic anions — sulfate, bicarbonate, and related species — and this is the diagnostic function of the fold ([PMID: 23506885](https://pubmed.ncbi.nlm.nih.gov/23506885/)). A bulky zwitterionic ester like COS is not a typical SulP substrate.
2. **Division of labor in the operon.** The operon already contains a dedicated ABC binding protein (PP_0076) whose family is the universal COS/QAC importer across bacteria ([PMID: 9925583](https://pubmed.ncbi.nlm.nih.gov/9925583/), [PMID: 15342567](https://pubmed.ncbi.nlm.nih.gov/15342567/), [PMID: 16923898](https://pubmed.ncbi.nlm.nih.gov/16923898/)). There is no need for a second COS importer, and PP_0075's fold is wrong for that job.
3. **Metabolic accounting.** Desulfation of COS liberates one sulfate per molecule inside the cell ([PMID: 17116241](https://pubmed.ncbi.nlm.nih.gov/17116241/), [PMID: 12906115](https://pubmed.ncbi.nlm.nih.gov/12906115/)). A co-transcribed sulfate permease provides an obvious route to manage that sulfate — feeding it into assimilation or exporting excess — closing the sulfur loop of the pathway.

**Localization.** PP_0075 is an integral protein of the **cytoplasmic (inner) membrane** (GO:0016020), with its transport pathway in the membrane and its STAS regulatory domain facing the cytoplasm. By analogy to the *Yersinia* homolog it likely functions as a homodimer stabilized through the transmembrane core, with STAS-domain motions driving the transport cycle ([PMID: 21659513](https://pubmed.ncbi.nlm.nih.gov/21659513/)). The STAS domain is also a documented protein-interaction hub in this family — e.g., *E. coli* YchM's STAS domain binds acyl carrier protein to link bicarbonate transport with fatty-acid metabolism ([PMID: 21070944](https://pubmed.ncbi.nlm.nih.gov/21070944/)) — leaving open the possibility of an analogous regulatory partnership for PP_0075, though none is documented.

**Pathway placement.** PP_0075 acts at the **membrane-transport / sulfur-handling step** of choline-O-sulfate catabolism. The upstream steps (COS import, desulfation) and the downstream carbon pathway (choline → glycine betaine via betA/betB) are established; PP_0075's specific contribution is to move the anionic product of desulfation. It is not implicated in osmoprotection, since the operon's catabolic character (betC downregulated by salt) argues explicitly against an osmotic-stress role ([PMID: 17116241](https://pubmed.ncbi.nlm.nih.gov/17116241/)).

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|------|-----------------|---------------------|
| [23506885](https://pubmed.ncbi.nlm.nih.gov/23506885/) | *The SLC26 gene family of anion transporters and channels* | Defines the SLC26/SulP architecture (TM core + STAS) that Q88RQ4 matches; documents sulfate/anion transport by bacterial SulP members |
| [21659513](https://pubmed.ncbi.nlm.nih.gov/21659513/) | *Low-resolution structure of a bacterial SLC26 transporter* | Bacterial SulP forms a TM-stabilized dimer; STAS domain projects into cytoplasm and drives conformational changes — the structural model for PP_0075 |
| [21070944](https://pubmed.ncbi.nlm.nih.gov/21070944/) | *STAS domain in complex with acyl carrier protein (E. coli YchM)* | Shows STAS domains mediate protein interactions linking anion transport to metabolism; template for possible PP_0075 STAS regulation |
| [19636956](https://pubmed.ncbi.nlm.nih.gov/19636956/) | *STAS domain of Rv1739c (M. tuberculosis)* | Confirms SulP anion-permease identity of bacterial family members related to SLC26 |
| [17116241](https://pubmed.ncbi.nlm.nih.gov/17116241/) | *Uncoupling of choline-O-sulphate utilization from osmoprotection in P. putida* | **Primary experimental study of this locus**: defines the KT2440 COS operon (betC + ABC transporter + LysR), shows COS uptake is separable from betC, and establishes a catabolic (not osmoprotective) role |
| [12906115](https://pubmed.ncbi.nlm.nih.gov/12906115/) | *S. meliloti glycine betaine biosynthetic genes (betICBA)* | Defines betC as choline sulfatase and the downstream betBA choline→betaine pathway that consumes the choline released after desulfation |
| [9925583](https://pubmed.ncbi.nlm.nih.gov/9925583/) | *High-affinity transport of choline-O-sulfate in B. subtilis* | Shows COS is imported by the ABC system OpuC, supporting that the ABC binding protein (not the SulP permease) captures COS |
| [15342567](https://pubmed.ncbi.nlm.nih.gov/15342567/) | *S. meliloti ABC transporter Cho specific for choline* | Comparative: high-affinity choline/QAC uptake is ABC-mediated, not SulP-mediated |
| [16923898](https://pubmed.ncbi.nlm.nih.gov/16923898/) | *Proline betaine uptake in S. meliloti (Prb, opp-like ABC)* | Comparative: QAC uptake is ABC-mediated; reinforces division of labor in the operon |
| [4855359](https://pubmed.ncbi.nlm.nih.gov/4855359/) | *Utilization of choline-O-sulphate as a sulphur source (Pseudomonas)* | Historical precedent that Pseudomonas uses COS as a sulfur source (abstract unavailable) |
| [30338300](https://pubmed.ncbi.nlm.nih.gov/30338300/) | *Choline sulfatase from …* | Enzymology of choline-sulfatase, the operon partner producing sulfate (abstract unavailable) |
| [21602374](https://pubmed.ncbi.nlm.nih.gov/21602374/) | *Small-molecule inhibition of choline catabolism in Pseudomonas* | Context: aerobic choline catabolism is widespread in Pseudomonas, including P. putida |

**Convergence of evidence.** Three independent lines all point to the same conclusion: (1) the **protein fold** (SulP/SLC26 anion permease), (2) the **operon context** (co-transcribed with a choline-sulfatase that produces sulfate, and with an ABC binding protein that handles the QAC substrate), and (3) **comparative physiology** (COS/QAC import is ABC-mediated in every characterized bacterium). Together they argue that PP_0075's substrate is the inorganic sulfate/anion product of the pathway, and that the "choline sulfate transporter" name is a misleading automatic annotation.

---

## Limitations and Knowledge Gaps

1. **No direct transport assay exists for PP_0075.** Its substrate (sulfate vs. bicarbonate vs. another anion), direction (import vs. export), and coupling ion have not been measured. The sulfate assignment is an inference from family, genome context, and comparative physiology, not an experimental determination.

2. **The "choline sulfate transporter" name is unverified.** It derives from an automatic annotation on EMBL AAN65709.1. No experimental evidence supports PP_0075 transporting intact choline-O-sulfate, and the family biochemistry argues against it.

3. **Operon transcription is inferred from gene spacing/orientation, not from transcript mapping.** While the 15-bp and 145-bp intergenic gaps and shared strand strongly suggest a single operon, RNA-seq/RT-PCR confirmation and mapping of the LysR-controlled promoter are lacking.

4. **No PP_0075-specific genetics.** The Galvão et al. study characterized betC; a clean PP_0075 deletion and its phenotype (growth on COS as sulfur source, intracellular sulfate accumulation) have not been reported.

5. **STAS-domain interactions are unexplored for PP_0075.** Whether its STAS domain binds a partner (as YchM's binds ACP) is unknown.

6. **Structure is homology-based only.** No experimental structure of PP_0075 exists; the dimeric, STAS-mobile model is transferred from *Yersinia*/*M. tuberculosis* homologs.

---

## Proposed Follow-up Experiments / Actions

1. **Direct transport assay.** Express and purify PP_0075, reconstitute into proteoliposomes, and test uptake/efflux of radiolabeled/ion-selective-electrode–monitored **sulfate**, bicarbonate, and — as a negative control — choline-O-sulfate, to define substrate specificity and directionality.

2. **Targeted genetics.** Construct an in-frame ΔPP_0075 deletion in KT2440 and assay growth on COS as sole **sulfur** source (vs. sole C/N source), and measure intracellular sulfate accumulation. Complement in trans to confirm.

3. **Operon/promoter mapping.** Use RT-PCR/RNA-seq to confirm co-transcription of PP_0077–PP_0076–PP_0075, and define the LysR (PP_0079)-dependent divergent promoter and its inducer (predicted: COS or choline).

4. **Regulator characterization.** Test whether PP_0079 binds the intergenic region and responds to COS; identify the effector molecule.

5. **STAS interactome.** Pull down the isolated PP_0075 STAS domain to test for metabolic partners analogous to the YchM STAS–ACP interaction.

6. **Structural determination.** Pursue cryo-EM or AlphaFold-guided crystallography of full-length PP_0075 to confirm the dimeric, STAS-mobile architecture and to model the anion-binding site.

7. **Annotation correction.** On the strength of the fold, orthology (K03321/COG0659), and comparative physiology, flag the UniProt "choline sulfate transporter" name as a likely automatic-annotation error and propose "SulP-family sulfate/anion permease (choline-O-sulfate catabolic operon)" pending assay.

---

## Conclusion

PP_0075 (Q88RQ4) is an inner-membrane **SulP/SLC26-family anion permease** — a 521-residue protein with a ~10-TM core and a cytoplasmic C-terminal STAS domain — encoded as the distal gene of a **choline-O-sulfate catabolic operon** in *P. putida* KT2440 (with betC choline-sulfatase PP_0077, ABC binding protein PP_0076, and divergent LysR regulator PP_0079). Its function is anion transport at the cytoplasmic membrane in service of COS utilization. Because COS is imported by ABC binding-protein systems and PP_0075 is orthologous to SulP sulfate permeases (KEGG K03321), it most plausibly transports the **inorganic sulfate** liberated by choline-sulfatase, coupling COS breakdown to sulfur assimilation. This substrate assignment is inferred from protein family, genome context, and comparative physiology; PP_0075 transport activity has not been directly assayed, so the literal "choline sulfate transporter" annotation remains unverified and probably inaccurate.


## Artifacts

- [OpenScientist final report](PP_0075-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PP_0075-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:23506885
2. PMID:21659513
3. PMID:19636956
4. PMID:17116241
5. PMID:12906115
6. PMID:9925583
7. PMID:15342567
8. PMID:16923898
9. PMID:21070944