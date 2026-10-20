---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-12T23:10:09.475397'
end_time: '2026-08-12T23:23:56.643747'
duration_seconds: 827.17
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: iscS
  gene_symbol: iscS
  uniprot_accession: Q88PK8
  protein_description: 'RecName: Full=Cysteine desulfurase IscS {ECO:0000255|HAMAP-Rule:MF_00331};
    EC=2.8.1.7 {ECO:0000255|HAMAP-Rule:MF_00331};'
  gene_info: Name=iscS {ECO:0000255|HAMAP-Rule:MF_00331}; OrderedLocusNames=PP_0842;
    ORFNames=PP0842;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the class-V pyridoxal-phosphate-dependent
  protein_domains: Aminotrans_V_dom. (IPR000192); Aminotrans_V_PyrdxlP_BS. (IPR020578);
    Cys_deSase_IscS. (IPR010240); Cysteine_dSase. (IPR016454); PyrdxlP-dep_Trfase.
    (IPR015424)
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
  path: iscS-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: iscS-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88PK8
- **Protein Description:** RecName: Full=Cysteine desulfurase IscS {ECO:0000255|HAMAP-Rule:MF_00331}; EC=2.8.1.7 {ECO:0000255|HAMAP-Rule:MF_00331};
- **Gene Information:** Name=iscS {ECO:0000255|HAMAP-Rule:MF_00331}; OrderedLocusNames=PP_0842; ORFNames=PP0842;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the class-V pyridoxal-phosphate-dependent
- **Key Domains:** Aminotrans_V_dom. (IPR000192); Aminotrans_V_PyrdxlP_BS. (IPR020578); Cys_deSase_IscS. (IPR010240); Cysteine_dSase. (IPR016454); PyrdxlP-dep_Trfase. (IPR015424)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "iscS" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'iscS' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **iscS** (gene ID: iscS, UniProt: Q88PK8) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: IscS Cysteine Desulfurase (Q88PK8, PP_0842) in *Pseudomonas putida* KT2440

## Gene/Protein Identity Verification

The target is **iscS** (UniProt **Q88PK8**; OrderedLocusName **PP_0842**) from *Pseudomonas putida* strain KT2440, annotated as **Cysteine desulfurase IscS, EC 2.8.1.7**, a member of the **class-V pyridoxal-5'-phosphate (PLP)-dependent aminotransferase family** with the diagnostic domains Aminotrans_V (IPR000192/IPR020578), **Cys_deSase_IscS (IPR010240)**, and the PLP-dependent transferase fold (IPR015424).

**Verification outcome — unambiguous.** The gene symbol *iscS*, the EC number (2.8.1.7), the protein family, and the domain architecture are fully self-consistent and match the well-characterized bacterial ISC-type cysteine desulfurase. The *P. putida* protein is a close ortholog of the intensively studied *Escherichia coli* IscS (and ~60% identical to human NFS1), so mechanistic and structural conclusions from those orthologs transfer directly. No competing/ambiguous gene assignment was encountered. Where direct *P. putida* biochemical papers are scarce, function is inferred from highly conserved orthologs and from conserved sequence/structure features, and this is flagged below.

---

## 1. Summary (Answer to the Research Question)

IscS is a **homodimeric, PLP-dependent L-cysteine desulfurase (EC 2.8.1.7)** that catalyzes the desulfuration of **L-cysteine to L-alanine**, capturing the released sulfane sulfur as an **enzyme-bound cysteinyl persulfide** on its active-site cysteine. It is the **master sulfur-mobilizing enzyme** of the cell: it delivers this persulfide sulfur to the scaffold protein **IscU** for **iron–sulfur (Fe–S) cluster assembly** (the ISC pathway) and to additional acceptor proteins that channel sulfur into **thiolated tRNA nucleosides, thiamine, biotin, lipoic acid, and the molybdenum cofactor**. It performs these reactions in the **bacterial cytoplasm**.

## 2. Primary Function and Catalyzed Reaction

**Reaction:** L-cysteine + [acceptor/reductant] → L-alanine + [acceptor]-S (sulfane sulfur), EC 2.8.1.7.

- IscS is a **PLP-dependent enzyme** that catalyzes the **first committed step of sulfur mobilization** in cofactor biosynthesis (PMID 25447671).
- Mechanistically, L-cysteine forms an external aldimine with the PLP cofactor; **PLP-dependent cleavage of the C–S bond** yields a **cysteinyl persulfide intermediate** on the catalytic cysteine (Cys328 in *E. coli*), which is regarded as "the hallmark step in sulfur mobilization" (PMID 25447671). The carbon skeleton is released as **L-alanine** (PMID 15379559).
- **Substrate specificity:** the physiological substrate is **L-cysteine**, which serves as the universal sulfur donor; the "product" sulfur is transferred to a bound protein acceptor (or, in vitro, to chemical reductants such as DTT), while alanine is released.

## 3. Downstream Pathways and Molecular Partners

**(a) Iron–sulfur cluster biogenesis (primary output).** IscS is a **core component of the ISC assembly system**. It transfers persulfide sulfur to the **U-type scaffold protein IscU**, on which **[2Fe–2S] clusters are built before transfer to recipient apoproteins** (PMID 32131593, 36605734). The crystal structure of the **IscS–IscU complex** shows IscU docking at the IscS active site around **Cys328** (PMID 20404999). Native mass spectrometry has captured transient iron- and sulfur-based intermediates on IscU and supports a **concerted, sulfur-initiated** [2Fe–2S] assembly mechanism (PMID 32131593, 36605734).

**(b) Sulfur-trafficking hub for thio-cofactors.** IscS is a **highly conserved master enzyme** that initiates sulfur transfer to a range of acceptors involved in **Fe–S assembly, tRNA modifications, and sulfur-containing cofactor biosynthesis** — including **thiamine, biotin, lipoic acid, and the molybdenum cofactor (Moco)** (PMID 25447671, 20404999).

**(c) tRNA thiolation.** For **wobble 2-thiouridine (mnm5s2U)** formation, **IscS transfers persulfide sulfur to TusA**, whose desulfurase-stimulating binding launches a relay through **TusBCD → TusE → MnmA** onto tRNA (PMID 16387657, 20404999). IscS similarly supplies **ThiI** (4-thiouridine / thiamine) and interacts with rhodanese RhdA (PMID 20404999).

Distinct acceptors (IscU, TusA, ThiI) **bind one at a time** at overlapping surfaces centered on Cys328; the **conformational plasticity of the long Cys328 loop** is essential for servicing chemically diverse partners (PMID 20404999). Regulatory partners such as **CyaY/frataxin and IscX** also bind IscS but are not themselves sulfur acceptors (PMID 20404999, 27474202).

## 3b. Organism-Specific (P. putida KT2440) Evidence

Direct annotation of **UniProt Q88PK8 (ISCS_PSEPK)** confirms the ortholog-based conclusions at the level of the target protein itself:
- **404 amino acids, ~44.5 kDa**, functions as a **homodimer** that forms a **heterotetramer with IscU**.
- **Active site Cys328** forms the **"cysteine persulfide intermediate"** — the same catalytic cysteine position as experimentally validated *E. coli* IscS.
- **PLP cofactor** is covalently bound as **N6-(pyridoxal phosphate)lysine at Lys206** (internal Schiff base), with additional PLP-contacting residues at 75–76, 155, 183, 203–205, 243.
- **Cys328 additionally ligates a [2Fe–2S] cluster "via persulfide group" as a "ligand shared with IscU,"** directly encoding the sulfur-hand-off to the scaffold.
- **Pathway:** iron–sulfur cluster biosynthesis; **subcellular location: Cytoplasm** (HAMAP-Rule MF_00331).

**Genomic context.** PP_0842 (*iscS*) sits in the canonical, co-regulated **ISC operon**: **PP_0841 iscR** ([2Fe–2S] transcriptional regulator) – **PP_0842 iscS** – **PP_0843 iscU** (scaffold) – **PP_0844 iscA** (A-type carrier) – **PP_0845 hscB** (co-chaperone) – **PP_0846 hscA** (Hsp70 chaperone). This mirrors the *E. coli* *iscRSUA-hscBA-fdx* operon, in which **IscR provides [2Fe–2S]-responsive feedback regulation**. The divergent upstream gene **PP_0840 cysE** (serine O-acetyltransferase) ties the operon's neighborhood to cysteine (substrate) biosynthesis.

## 3c. Regulation of the Assembly Reaction

Not all IscS partners are sulfur acceptors. **CyaY (bacterial frataxin)** and **IscX** bind IscS and act as **regulators of assembly rate** rather than sulfur recipients. Molecular-dynamics/NMR studies of the IscS–IscU and ternary IscS–IscU–CyaY complexes show IscU is firmly anchored yet retains pivotal interfacial motion, and that **CyaY hampers the specific IscU–IscS movements and catalytic-loop flipping required for [2Fe–2S] formation**, giving it an inhibitory role (PMID 27474202). In other systems frataxin can conversely **stimulate** desulfurase activity in an **iron-dependent** manner (PMID 26032732), so frataxin functions as an iron-responsive rheostat coordinating iron and sulfur supply on the scaffold. Downstream, the **HscA/HscB (Hsp70/J-protein) chaperones and ferredoxin (Fdx)** drive ATP-dependent, redox-assisted transfer of the assembled cluster from IscU to recipient apoproteins.

## 4. Structure and Catalytic Residue

IscS is a **homodimer** adopting the **class-V (fold-type I) PLP aminotransferase fold**. The essential **active-site cysteine on a mobile loop** (Cys328 in *E. coli*) shuttles the persulfide from the PLP-bound substrate to protein acceptors; its loop flexibility underlies the multi-partner relay (PMID 20404999). Crystal structures of IscS–IscU and IscS–TusA complexes, and of *M. tuberculosis* IscS, define this architecture (PMID 20404999, 24548275).

## 5. Localization

Bacterial IscS functions in the **cytoplasm**, where the *isc* operon and Fe–S/cofactor assembly machinery reside; this is explicitly annotated for Q88PK8 (**Subcellular location: Cytoplasm**, HAMAP-Rule MF_00331). Conservation is strong: the human ortholog **NFS1 is ~60% identical** to *E. coli* IscS and localizes to mitochondria (with a cytosolic pool), consistent with IscS acting in the bacterial cytosolic compartment (PMID 28766335).

## 6. Supported vs. Refuted Hypotheses

- **Supported:** IscS = PLP-dependent L-cysteine desulfurase producing alanine + enzyme persulfide (EC 2.8.1.7). *Strong, direct biochemical/structural evidence in orthologs.*
- **Supported:** Persulfide sulfur is delivered to IscU for [2Fe–2S] assembly and to TusA/ThiI for tRNA/cofactor thiolation. *Strong; complex crystal structures and reconstituted relays.*
- **Supported:** Homodimeric class-V PLP fold with catalytic Cys on a flexible loop; cytoplasmic. *Strong structural/homology evidence.*
- **Not refuted, but organism-specific caveat:** Direct *P. putida* KT2440 IscS enzymology was not located; conclusions rest on close orthologs (*E. coli*, and the conserved domain signature Cys_deSase_IscS in Q88PK8).

## 7. Limitations and Future Directions

- Evidence is largely from *E. coli*/*Synechocystis*/*M. tuberculosis*/human orthologs; a *P. putida*-specific kinetic and knockout characterization would confirm partner usage in this organism.
- The exact *P. putida* isc operon composition (iscR, iscU, iscA, hscBA, fdx) and IscR-mediated regulation were not experimentally examined here.
- Quantitative substrate/partner specificity (e.g., selenocysteine handling, relative flux to Fe–S vs. tRNA thiolation) in *P. putida* remains to be measured.

## Key References
- Black & Dos Santos 2015, *Biochim Biophys Acta* (PMID 25447671) — mechanism, hub role.
- Shi et al. 2010, *PLoS Biol* (PMID 20404999) — IscS–IscU and IscS–TusA structures, Cys328 loop.
- Lin et al. 2020, *J Am Chem Soc* (PMID 32131593); Bennett et al. 2022 (PMID 36605734) — Fe–S assembly mechanism on IscU.
- Ikeuchi et al. 2006, *Mol Cell* (PMID 16387657) — TusABCDE tRNA 2-thiouridine relay.
- Tirupati et al. 2004 (PMID 15379559) — products (alanine + cysteinyl persulfide).
- Bühning et al. 2017 (PMID 28766335) — IscS vs. NFS1 conservation/localization.
- Rybniker et al. 2014 (PMID 24548275) — IscS structure and Fe–S/oxidative-stress role.


## Artifacts

- [OpenScientist final report](iscS-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](iscS-deep-research-openscientist_artifacts/final_report.pdf)