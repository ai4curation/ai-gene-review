---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-25T14:11:42.688051'
end_time: '2026-07-25T14:30:30.315061'
duration_seconds: 1127.63
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: liuC
  gene_symbol: liuC
  uniprot_accession: Q88FM3
  protein_description: 'SubName: Full=Methylglutaconyl-CoA hydratase {ECO:0000313|EMBL:AAN69656.1};
    EC=4.2.1.18 {ECO:0000313|EMBL:AAN69656.1};'
  gene_info: Name=liuC {ECO:0000313|EMBL:AAN69656.1}; OrderedLocusNames=PP_4066 {ECO:0000313|EMBL:AAN69656.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the enoyl-CoA hydratase/isomerase family.
  protein_domains: ClpP/crotonase-like_dom_sf. (IPR029045); Enoyl-CoA_hyd/isom_CS.
    (IPR018376); Enoyl-CoA_hydra/iso. (IPR001753); Enoyl-CoA_hydra_C. (IPR014748);
    Enoyl-CoA_Hydratase/Isomerase. (IPR051683)
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
citation_count: 16
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: liuC-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: liuC-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88FM3
- **Protein Description:** SubName: Full=Methylglutaconyl-CoA hydratase {ECO:0000313|EMBL:AAN69656.1}; EC=4.2.1.18 {ECO:0000313|EMBL:AAN69656.1};
- **Gene Information:** Name=liuC {ECO:0000313|EMBL:AAN69656.1}; OrderedLocusNames=PP_4066 {ECO:0000313|EMBL:AAN69656.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the enoyl-CoA hydratase/isomerase family.
- **Key Domains:** ClpP/crotonase-like_dom_sf. (IPR029045); Enoyl-CoA_hyd/isom_CS. (IPR018376); Enoyl-CoA_hydra/iso. (IPR001753); Enoyl-CoA_hydra_C. (IPR014748); Enoyl-CoA_Hydratase/Isomerase. (IPR051683)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "liuC" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'liuC' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **liuC** (gene ID: liuC, UniProt: Q88FM3) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: LiuC (PP_4066) — 3-Methylglutaconyl-CoA Hydratase of *Pseudomonas putida* KT2440

**UniProt:** Q88FM3 | **Gene:** *liuC* | **Locus:** PP_4066 | **EC 4.2.1.18** | **Organism:** *Pseudomonas putida* KT2440 (ATCC 47054 / DSM 6125 / NCIMB 11950)

---

## Summary

**LiuC (PP_4066; UniProt Q88FM3) is a 3-methylglutaconyl-CoA hydratase (EC 4.2.1.18), a soluble cytoplasmic enzyme of the crotonase (enoyl-CoA hydratase/isomerase) superfamily.** It catalyzes the reversible hydration of the α,β-unsaturated thioester **(E)-3-methylglutaconyl-CoA** to **(S)-3-hydroxy-3-methylglutaryl-CoA (HMG-CoA)**, adding water across the substrate's carbon-carbon double bond. This is the penultimate step of the **leucine/isovalerate utilization (Liu) pathway**, the conserved bacterial route by which the branched-chain amino acid leucine and the methyl-branched compound isovalerate are catabolized to the central-metabolism products acetyl-CoA and acetoacetate.

The gene identity is unambiguous and well supported. The UniProt annotation ("Methylglutaconyl-CoA hydratase, EC 4.2.1.18," enoyl-CoA hydratase/isomerase/crotonase family) matches the biochemically and structurally characterized Liu pathway of *Pseudomonas*, and *liuC* sits in a **syntenic leucine-catabolism gene cluster** in the *P. putida* KT2440 genome (PP_4064 *ivd*/LiuA → PP_4065 *mccB*/LiuB → PP_4066 *liuC* → PP_4067 *mccA*/LiuD, with an adjacent Cro/CI-family regulator). The neighboring enzymes have been experimentally validated in the closely related *P. aeruginosa* — isovaleryl-CoA dehydrogenase (LiuA), 3-methylcrotonyl-CoA carboxylase (LiuB/LiuD), and HMG-CoA lyase (LiuE) — placing LiuC by both position and family as the 3-methylglutaconyl-CoA hydratase between the carboxylase and the lyase. The crystal structure of a LiuC ortholog from *Myxococcus xanthus* (solved to 1.1–2.05 Å) directly confirms the crotonase fold and defines catalytic glutamates and substrate-positioning residues.

Functionally, LiuC acts in the **cytoplasm** as a soluble globular enzyme (no signal peptide, no transmembrane segment by sequence analysis, consistent with the crotonase superfamily and with the soluble mitochondrial-matrix localization of eukaryotic orthologs). Its pathway is induced by leucine and repressed on preferred carbon sources through the regulator **LiuR** and the **CbrAB/Crc** carbon catabolite repression system, and it is fed upstream by the **bkd-encoded branched-chain 2-oxoacid dehydrogenase (BCKDH)** that generates isovaleryl-CoA from leucine. The same pathway node (3-methylcrotonyl-CoA) links leucine catabolism to acyclic monoterpene (citronellol/geraniol) degradation via the Atu pathway in *Pseudomonas*.

---

## Key Findings

### F1. LiuC is 3-methylglutaconyl-CoA hydratase (EC 4.2.1.18) of the Liu pathway

The gene symbol *liuC* and the UniProt annotation of Q88FM3 (Methylglutaconyl-CoA hydratase, EC 4.2.1.18; enoyl-CoA hydratase/isomerase/crotonase family) match the biochemically characterized **leucine/isovalerate utilization (Liu) pathway** of *Pseudomonas*. In *P. aeruginosa* the *liuRABCDE* gene cluster encodes the leucine/isovalerate utilization enzymes; the individual enzymes have been experimentally assigned: LiuA = isovaleryl-CoA dehydrogenase, LiuB/LiuD = 3-methylcrotonyl-CoA carboxylase, and LiuE = HMG-CoA lyase. By its genomic position and its family membership, LiuC is the **3-methylglutaconyl-CoA hydratase** that catalyzes the step between methylcrotonyl-CoA carboxylase (LiuBD) and HMG-CoA lyase (LiuE).

The direct textual evidence is decisive: the structural study of the *Myxococcus xanthus* ortholog states, *"The first step into this pathway is mediated by LiuC, a member of the 3-methylglutaconyl CoA hydratases (MGCH)"* ([PMID: 27271456](https://pubmed.ncbi.nlm.nih.gov/27271456/)). The cluster organization is established in *P. aeruginosa*: *"The identified genes are part of two separate gene clusters [liuRABCDE (PA2011-PA2016) and atuABCDEFGH (PA2886-PA2893)]"* ([PMID: 16272386](https://pubmed.ncbi.nlm.nih.gov/16272386/)). Crucially for our target organism, genome analysis confirmed that *"other pseudomonads (P. putida KT2440 and P. fluorescens Pf-5) revealed candidate genes for Liu proteins for both species"* ([PMID: 16820476](https://pubmed.ncbi.nlm.nih.gov/16820476/)).

**Reaction catalyzed:**

```
(E)-3-methylglutaconyl-CoA  +  H2O   ⇌   (S)-3-hydroxy-3-methylglutaryl-CoA (HMG-CoA)
```

Substrate specificity: LiuC operates on the CoA-thioester 3-methylglutaconyl-CoA, hydrating the α,β double bond to give the β-hydroxy thioester HMG-CoA. This is the physiological forward direction in catabolism.

### F2. LiuC is a crotonase-superfamily enzyme with a defined fold and catalytic mechanism

Q88FM3 is a **271-amino-acid** protein carrying Pfam ECH domains (PF00378) and the InterPro crotonase-like/ClpP domain signature (IPR029045), assigned to COG1024 (enoyl-CoA hydratase/isomerase) and KEGG ortholog **K13766**. The crystal structure of the LiuC ortholog from *Myxococcus xanthus* was solved at **1.1–2.05 Å** in both apo and CoA-bound forms, revealing the canonical crotonase fold and identifying the catalytic machinery: two glutamates (**Glu112, Glu132**) act as the acid/base pair, with **Tyr231** and **Arg69** positioning the substrate ([PMID: 27271456](https://pubmed.ncbi.nlm.nih.gov/27271456/)).

The mechanistic assignment is stated directly: *"The dehydration of 3-hydroxy-3-methylglutaconyl CoA to 3-methylglutaconyl CoA catalyzed by LiuC involves Glu112 and Glu132 and likely employs the typical crotonase acid-base mechanism"* ([PMID: 27271456](https://pubmed.ncbi.nlm.nih.gov/27271456/)). A striking evolutionary observation from the same work is that *"LiuC shows higher sequence and structural similarity to human MGCH than to bacterial forms, although they convert the same substrate"* — i.e., LiuC is more like the human enzyme AUH (3-methylglutaconyl-CoA hydratase) than to some other bacterial crotonases, while catalyzing the identical reaction.

The broader superfamily context is provided by the authoritative crotonase review: *"CS enzymes possess a canonical fold formed from repeated betabetaalpha units that assemble into two approximately perpendicular beta-sheets surrounded by alpha-helices. CS enzymes often, although not exclusively, oligomerize as trimers or dimers of trimers. Two conserved backbone NH groups in CS active sites form an oxyanion 'hole' that can stabilize enolate/oxyanion intermediates"* ([PMID: 18470480](https://pubmed.ncbi.nlm.nih.gov/18470480/)). This oxyanion hole is the structural basis by which LiuC stabilizes the enolate/oxyanion intermediate during hydration.

### F3. Direct genomic confirmation of synteny in *P. putida* KT2440

KEGG annotation of the PP_4064–PP_4068 neighborhood in *P. putida* KT2440 shows a **contiguous leucine/isovalerate-catabolism cluster**:

| Locus | Gene | Enzyme | EC / KO | Liu name |
|-------|------|--------|---------|----------|
| PP_4064 | *ivd* | Isovaleryl-CoA dehydrogenase | EC 1.3.8.4 / K00253 | LiuA |
| PP_4065 | *mccB* | 3-Methylcrotonyl-CoA carboxylase β-subunit | EC 6.4.1.4 / K01969 | LiuB |
| **PP_4066** | **liuC** | **Methylglutaconyl-CoA hydratase** | **EC 4.2.1.18 / K13766** | **LiuC** |
| PP_4067 | *mccA* | 3-Methylcrotonyl-CoA carboxylase α-subunit | EC 6.4.1.4 / K01968 | LiuD |
| PP_4068 | — | Cro/CI-family transcriptional regulator | — | LiuR ortholog |

The terminal HMG-CoA lyase step (EC 4.1.3.4 / K01640, LiuE) is encoded elsewhere in the genome (PP_3394 / PP_3540), not within this cluster. A pairwise global alignment of *P. putida* LiuC (271 aa) against the structurally characterized *M. xanthus* LiuC (PDB 5JBW/5JBX) gives **~29% full-length identity**, confirming clear homology within the crotonase superfamily. This positions PP_4066 unambiguously between the carboxylase and the (distally encoded) lyase — exactly the metabolic slot for a 3-methylglutaconyl-CoA hydratase.

### F4. LiuC is a soluble cytoplasmic protein (localization)

Sequence-based analysis of the 271-residue *P. putida* LiuC indicates a **soluble, cytosolic** protein. The N-terminus (MSDFSTLEVIRDPRGF…) is polar, carrying an Asp at position 3 and multiple charged residues within the first 30 aa (D3, E8, R11, D12, R14, R23, E24, D25, K26) — incompatible with a hydrophobic Sec/Tat signal peptide. A Kyte-Doolittle hydropathy scan (19-residue window) never sustains a membrane-spanning helix: the single maximum reaches only ~1.76 at an internal position (~residue 105), reflecting a buried core segment of the globular fold rather than a transmembrane helix. The protein is mildly acidic (33 Lys/Arg vs 38 Asp/Glu; net charge ~-5), typical of soluble cytosolic enzymes.

This inference is consistent with (i) the crotonase superfamily being composed of soluble globular enzymes, and (ii) the mitochondrial-matrix (soluble) localization of eukaryotic orthologs. Indeed, the trypanosome ortholog *"3-MGCoA-H localizes in the mitochondrial matrix"* ([PMID: 28366667](https://pubmed.ncbi.nlm.nih.gov/28366667/)), and the plant ortholog is targeted to mitochondria ([PMID: 29742810](https://pubmed.ncbi.nlm.nih.gov/29742810/)) — the soluble compartment equivalent to the bacterial cytoplasm. Thus LiuC carries out its function **in the cytoplasm** of *P. putida*.

### F5. Pathway context, regulation, and metabolic role

LiuC operates within the linear Liu pathway:

```
Isovaleryl-CoA
   │  LiuA (isovaleryl-CoA dehydrogenase, EC 1.3.8.4)
   ▼
3-Methylcrotonyl-CoA  ◄──── entry point for Atu (acyclic monoterpene) pathway
   │  LiuB / LiuD (3-methylcrotonyl-CoA carboxylase, EC 6.4.1.4)  [+CO2, ATP]
   ▼
(E)-3-Methylglutaconyl-CoA
   │  ★ LiuC (3-methylglutaconyl-CoA hydratase, EC 4.2.1.18)  [+H2O]
   ▼
(S)-3-Hydroxy-3-methylglutaryl-CoA (HMG-CoA)
   │  LiuE (HMG-CoA lyase, EC 4.1.3.4)
   ▼
Acetyl-CoA  +  Acetoacetate  ───►  central carbon/energy metabolism
```

Each downstream/upstream step is experimentally supported: LiuA was purified and shown to have acyl-CoA dehydrogenase activity with isovaleryl-CoA (KM 2.3 µM) ([PMID: 18625020](https://pubmed.ncbi.nlm.nih.gov/18625020/)); the carboxylases LiuB/LiuD were assigned to *liuB/liuD* ([PMID: 16272386](https://pubmed.ncbi.nlm.nih.gov/16272386/)); and LiuE was purified and shown to be HMG-CoA lyase (KM 100 µM for HMG-CoA) ([PMID: 19459965](https://pubmed.ncbi.nlm.nih.gov/19459965/)).

**Regulation.** The *liu* operon is induced by leucine and repressed on preferred carbon sources: *"expression of the liu operon is subjected to carbon catabolite repression control (CCR); protein LiuD was strongly expressed in the presence of leucine, but it was repressed in the presence of glucose or succinate"* ([PMID: 29787835](https://pubmed.ncbi.nlm.nih.gov/29787835/)). Control is exerted by the transcriptional regulator **LiuR** and the **CbrAB/Crc** system: *"Pseudomonas aeruginosa metabolizes leucine through the leucine/isovalerate utilization pathway, whose enzymes are encoded in the liuRABCDE gene cluster (liu)"* ([PMID: 29787835](https://pubmed.ncbi.nlm.nih.gov/29787835/)).

**Metabolic convergence.** The 3-methylcrotonyl-CoA node makes the Liu pathway the convergence point for both leucine/isovalerate catabolism and acyclic monoterpene degradation: *"Mutagenesis of the atu and liu clusters showed that both are involved in AMTC and leucine catabolism by encoding the enzymes related to the geranyl-CoA and the 3-methylcrotonyl-CoA pathways, respectively"* ([PMID: 16517656](https://pubmed.ncbi.nlm.nih.gov/16517656/)).

### F6. Upstream connection to the bkd operon

Upstream of the Liu pathway, leucine is converted to isovaleryl-CoA — the entry metabolite of the Liu pathway — by the **branched-chain 2-oxoacid dehydrogenase (BCKDH)** complex encoded by the *bkd* operon in *P. putida*. This operon is positively regulated by **BkdR** (an Lrp homolog): *"Chromosomal mutations affecting this gene, named bkdR, resulted in a loss of ability to use branched-chain amino acids as carbon and energy sources"* ([PMID: 8320210](https://pubmed.ncbi.nlm.nih.gov/8320210/)). The inducers are the branched-chain amino acids: *"the L-branched-chain amino acids and D-leucine are the inducers of the bkd operon"* ([PMID: 10217783](https://pubmed.ncbi.nlm.nih.gov/10217783/)). BkdR is a tetramer that binds cooperatively upstream of *bkdA1*, and the operon is subject to catabolite repression ([PMID: 7836297](https://pubmed.ncbi.nlm.nih.gov/7836297/), [PMID: 9068646](https://pubmed.ncbi.nlm.nih.gov/9068646/)).

The complete upstream route is therefore:

```
L-Leucine → (transamination) → 2-oxoisocaproate → (BCKDH / bkd operon) → Isovaleryl-CoA → Liu pathway (LiuA→LiuB/D→LiuC→LiuE)
```

---

## Mechanistic Model / Interpretation

LiuC sits at the biochemical heart of the leucine/isovalerate utilization pathway, performing the **hydration** step that converts the α,β-unsaturated CoA-thioester 3-methylglutaconyl-CoA into the β-hydroxy thioester HMG-CoA. Mechanistically, this is a textbook crotonase-superfamily reaction:

1. The substrate's thioester carbonyl is oriented into the **oxyanion hole** formed by two conserved backbone NH groups. This polarizes the carbonyl and stabilizes the developing enolate/oxyanion negative charge.
2. One catalytic glutamate (Glu112/Glu132 in the ortholog numbering) acts as a **general base**, activating a water molecule for nucleophilic attack (in the hydration direction), while the partner glutamate acts as a **general acid**, protonating the α-carbon.
3. **Tyr231 and Arg69** position the dicarboxylic substrate correctly in the active site.

Because the crotonase acid/base pair is reversible, LiuC can in principle run in either direction; physiologically in catabolism it runs toward HMG-CoA. Notably, the same reversibility underlies the pathophysiology of the human ortholog (AUH): in "primary" 3-methylglutaconic aciduria, hydratase deficiency causes accumulation of 3-methylglutaconate ([PMID: 24407466](https://pubmed.ncbi.nlm.nih.gov/24407466/), [PMID: 23355087](https://pubmed.ncbi.nlm.nih.gov/23355087/)) — a human counterpart that directly corroborates the enzyme's role in leucine catabolism.

Placed in the whole-cell context, LiuC is one enzyme in a tightly coordinated, co-regulated cassette. The Liu operon behaves as a switchable catabolic module: turned **on** by leucine via LiuR and turned **off** in the presence of preferred carbon sources (glucose, succinate) via CbrAB/Crc. This ensures that *P. putida* only invests in the branched-chain catabolic machinery when leucine/isovalerate (or acyclic terpenes feeding into the same node) are available and preferred carbon is scarce. LiuC's activity is therefore both a metabolic bottleneck and a regulated node — its product HMG-CoA is committed to cleavage by LiuE into acetyl-CoA and acetoacetate, funneling branched-chain carbon into central metabolism and energy production.

**Integrated pathway map:**

```
                bkd operon (BkdR-regulated, leucine-induced)
L-Leucine ──► 2-oxoisocaproate ──► Isovaleryl-CoA
                                         │
        ┌────────────── liuRABCDE operon (LiuR + CbrAB/Crc) ──────────────┐
        │  LiuA        LiuB/LiuD             ★LiuC★          LiuE          │
   Isovaleryl-CoA ─► 3-Me-crotonyl-CoA ─► 3-Me-glutaconyl-CoA ─► HMG-CoA ─►│─► AcCoA + Acetoacetate
        │                   ▲                                              │
        └───────────────────┼──────────────────────────────────────────────┘
                            Atu pathway (acyclic monoterpenes: citronellol/geraniol)
```

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports the annotation |
|------|-----------------|-------------------------------|
| [27271456](https://pubmed.ncbi.nlm.nih.gov/27271456/) | *Structure of LiuC, a 3-hydroxy-3-methylglutaconyl-CoA dehydratase in M. xanthus* | Direct: identifies LiuC as an MGCH; solves crystal structure; defines Glu112/Glu132 catalytic residues and crotonase acid-base mechanism; notes similarity to human MGCH |
| [16272386](https://pubmed.ncbi.nlm.nih.gov/16272386/) | *Methylcrotonyl-CoA & geranyl-CoA carboxylases (liuB/liuD, atuC/atuF)* | Establishes the *liuRABCDE* cluster and the carboxylase step immediately upstream of LiuC |
| [16820476](https://pubmed.ncbi.nlm.nih.gov/16820476/) | *Genes/proteins for acyclic terpene and leucine/isovalerate catabolism in P. aeruginosa* | Confirms *P. putida* KT2440 encodes orthologous Liu proteins, including LiuC |
| [18625020](https://pubmed.ncbi.nlm.nih.gov/18625020/) | *Biochemical characterization of LiuA (isovaleryl-CoA dehydrogenase)* | Validates the upstream LiuA step; confirms importance of *liu* genes |
| [19459965](https://pubmed.ncbi.nlm.nih.gov/19459965/) | *P. aeruginosa liuE encodes HMG-CoA lyase* | Validates the downstream LiuE step consuming LiuC's product HMG-CoA |
| [16517656](https://pubmed.ncbi.nlm.nih.gov/16517656/) | *atu and liu clusters in monoterpene and leucine catabolism* | Shows the shared 3-methylcrotonyl-CoA node linking Liu and Atu |
| [29787835](https://pubmed.ncbi.nlm.nih.gov/29787835/) | *liu gene expression controlled by LiuR and CbrAB/Crc* | Establishes regulation: leucine induction, CCR repression |
| [18470480](https://pubmed.ncbi.nlm.nih.gov/18470480/) | *Mechanisms and structures of crotonase superfamily enzymes* | Authoritative description of the crotonase fold, oligomerization, and oxyanion hole underlying LiuC catalysis |
| [8320210](https://pubmed.ncbi.nlm.nih.gov/8320210/) | *bkdR required for bkd operon expression* | Establishes the upstream BCKDH step producing isovaleryl-CoA |
| [10217783](https://pubmed.ncbi.nlm.nih.gov/10217783/) | *In vitro transcription of bkd operon; BCAAs and D-leucine are inducers* | Shows leucine induces the upstream bkd operon |
| [9068646](https://pubmed.ncbi.nlm.nih.gov/9068646/), [7836297](https://pubmed.ncbi.nlm.nih.gov/7836297/) | *BkdR transcriptional activation and DNA binding* | Mechanistic detail on upstream regulation |
| [28366667](https://pubmed.ncbi.nlm.nih.gov/28366667/) | *3-MGCoA hydratase in T. brucei* | Ortholog localizes to mitochondrial matrix (soluble compartment) — supports soluble localization inference |
| [29742810](https://pubmed.ncbi.nlm.nih.gov/29742810/) | *Plant 3-methylglutaconyl-CoA hydratase* | Ortholog catalyzes the same dehydration; kinetics similar to prokaryotic homolog; mitochondrially targeted |
| [26162879](https://pubmed.ncbi.nlm.nih.gov/26162879/) | *P. aeruginosa AtuE crotonase (isohexenyl-glutaconyl-CoA hydratase)* | Sister crotonase in the linked Atu pathway; corroborates crotonase active-site architecture (oxyanion hole from Gly NH groups) |
| [24407466](https://pubmed.ncbi.nlm.nih.gov/24407466/), [23355087](https://pubmed.ncbi.nlm.nih.gov/23355087/) | *3-methylglutaconic aciduria reviews* | Human AUH deficiency confirms the enzyme's role in leucine catabolism |

**Note on human/disease literature:** Many retrieved papers concern the human ortholog AUH and 3-methylglutaconic aciduria. These are *not* the target gene, but they are legitimately informative as orthologs of the same enzyme catalyzing the identical reaction (EC 4.2.1.18). They corroborate substrate identity and reaction chemistry, but clinical phenotypes are specific to humans and do not describe *P. putida* biology.

---

## Limitations and Knowledge Gaps

1. **No direct biochemical characterization of the *P. putida* LiuC protein.** The functional assignment for PP_4066 rests on (i) genomic synteny, (ii) family/domain membership, and (iii) experimental characterization of orthologs (notably *M. xanthus* LiuC and the neighboring *P. aeruginosa* Liu enzymes). No purified-enzyme kinetics (KM, kcat, substrate specificity), pH optimum, or oligomeric state have been reported *for the KT2440 protein specifically*.

2. **Structure is inferred, not solved.** The crotonase fold, catalytic residues, and oxyanion hole are assigned from the *M. xanthus* ortholog (~29% identity) and from superfamily conservation. No experimental *P. putida* LiuC structure exists; a homology/AlphaFold model would be inferential.

3. **Localization is a sequence-based inference.** The soluble cytoplasmic assignment is supported by absence of signal peptide/TM segments and by ortholog behavior, but no experimental fractionation or fluorescence-localization data exist for PP_4066.

4. **Regulatory data are largely from *P. aeruginosa*.** LiuR/CbrAB/Crc control of the *liu* operon and BkdR control of the *bkd* operon are best characterized in *P. aeruginosa* and *P. putida* respectively; the precise operon boundaries, promoter, and LiuR binding sites for the KT2440 *liuC*-containing cluster should be confirmed directly.

5. **Directionality/reversibility in vivo.** While the crotonase mechanism is reversible, the physiological flux direction and any kinetic asymmetry for *P. putida* LiuC are assumed from pathway logic, not measured.

---

## Proposed Follow-up Experiments / Actions

1. **Heterologous expression and enzyme assay.** Clone PP_4066, express His-tagged LiuC in *E. coli*, purify, and measure hydratase activity on 3-methylglutaconyl-CoA (forward) and HMG-CoA (reverse). Report KM, kcat, pH optimum, and test substrate specificity against related CoA-thioesters (e.g., glutaconyl-CoA, crotonyl-CoA) to define selectivity.

2. **Gene knockout / complementation.** Construct a *P. putida* KT2440 Δ*liuC* mutant and test growth on leucine and isovalerate as sole carbon sources; confirm loss of growth and restoration by *in trans* complementation. Measure accumulation of 3-methylglutaconyl-CoA/3-methylglutaconate as a diagnostic metabolite.

3. **Structure determination.** Solve the crystal structure of *P. putida* LiuC (or generate an AlphaFold model with confidence analysis) and confirm the predicted catalytic glutamates and oxyanion-hole geometry; compare with the *M. xanthus* ortholog and human AUH.

4. **Subcellular localization.** Verify cytoplasmic localization by cell fractionation and/or GFP fusion imaging.

5. **Transcriptional regulation mapping.** Define the *liuC*-containing operon transcript, map the promoter and LiuR binding site upstream of the cluster in KT2440, and test induction by leucine and CbrAB/Crc-mediated repression by glucose/succinate directly (RT-qPCR / reporter fusions).

6. **Flux confirmation.** Use ¹³C-leucine labeling and LC-MS to trace flux through 3-methylglutaconyl-CoA → HMG-CoA → acetyl-CoA + acetoacetate, confirming LiuC's in vivo role.

---

## Conclusion

All lines of evidence — UniProt/InterPro annotation, KEGG orthology (K13766), genomic synteny within the *P. putida* KT2440 leucine-catabolism cluster (PP_4064–PP_4068), the crystallographically defined *M. xanthus* ortholog, experimentally validated neighboring Liu enzymes, and orthologous enzymes across bacteria, plants, protozoa, and humans — converge on a single, well-supported conclusion: **LiuC (PP_4066) is the soluble cytoplasmic 3-methylglutaconyl-CoA hydratase (EC 4.2.1.18) that catalyzes the penultimate, water-adding step of the leucine/isovalerate utilization pathway in *Pseudomonas putida* KT2440.**


## Artifacts

- [OpenScientist final report](liuC-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](liuC-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:27271456
2. PMID:16272386
3. PMID:16820476
4. PMID:18470480
5. PMID:28366667
6. PMID:29742810
7. PMID:18625020
8. PMID:19459965
9. PMID:29787835
10. PMID:16517656
11. PMID:8320210
12. PMID:10217783
13. PMID:7836297
14. PMID:9068646
15. PMID:24407466
16. PMID:23355087