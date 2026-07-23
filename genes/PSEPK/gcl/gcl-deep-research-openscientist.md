---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-15T17:08:39.802150'
end_time: '2026-07-15T17:22:27.980718'
duration_seconds: 828.18
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: gcl
  gene_symbol: gcl
  uniprot_accession: Q88F03
  protein_description: 'RecName: Full=Glyoxylate carboligase {ECO:0000256|ARBA:ARBA00069761};
    EC=4.1.1.47 {ECO:0000256|ARBA:ARBA00066435}; AltName: Full=Tartronate-semialdehyde
    synthase {ECO:0000256|ARBA:ARBA00077063};'
  gene_info: Name=gcl {ECO:0000313|EMBL:AAN69877.1}; OrderedLocusNames=PP_4297 {ECO:0000313|EMBL:AAN69877.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the TPP enzyme family.
  protein_domains: DHS-like_NAD/FAD-binding_dom. (IPR029035); Glyox_carbo_lig. (IPR006397);
    THDP-binding. (IPR029061); Thiamin_PyroP_enz_cen_dom. (IPR012000); Thiamin_PyroP_enz_TPP-bd_dom.
    (IPR012001)
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
citation_count: 4
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: gcl-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: gcl-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88F03
- **Protein Description:** RecName: Full=Glyoxylate carboligase {ECO:0000256|ARBA:ARBA00069761}; EC=4.1.1.47 {ECO:0000256|ARBA:ARBA00066435}; AltName: Full=Tartronate-semialdehyde synthase {ECO:0000256|ARBA:ARBA00077063};
- **Gene Information:** Name=gcl {ECO:0000313|EMBL:AAN69877.1}; OrderedLocusNames=PP_4297 {ECO:0000313|EMBL:AAN69877.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the TPP enzyme family.
- **Key Domains:** DHS-like_NAD/FAD-binding_dom. (IPR029035); Glyox_carbo_lig. (IPR006397); THDP-binding. (IPR029061); Thiamin_PyroP_enz_cen_dom. (IPR012000); Thiamin_PyroP_enz_TPP-bd_dom. (IPR012001)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "gcl" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'gcl' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **gcl** (gene ID: gcl, UniProt: Q88F03) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of *gcl* (Glyoxylate Carboligase, PP_4297, UniProt Q88F03) in *Pseudomonas putida* KT2440

**Gene:** gcl (OrderedLocusName PP_4297)
**Protein:** Glyoxylate carboligase (Gcl); AltName tartronate-semialdehyde synthase
**UniProt:** Q88F03 · **EC:** 4.1.1.47 · **Organism:** *Pseudomonas putida* KT2440 (PSEPK)

---

## Summary

The gene **gcl** (ordered locus **PP_4297**; UniProt accession **Q88F03**) of *Pseudomonas putida* KT2440 encodes **glyoxylate carboligase** (EC 4.1.1.47), also known as **tartronate-semialdehyde synthase**. The gene symbol, EC number, protein family (thiamine-pyrophosphate/TPP enzyme family), and domain architecture reported by UniProt are fully consistent with the primary literature. This report confirms — through direct biochemical precedent, comparative genomics, sequence analysis, and curated pathway databases — that Q88F03 is a genuine, catalytically intact glyoxylate carboligase. There is **no ambiguity in the gene identification**: the "gcl" symbol maps unambiguously to glyoxylate carboligase in bacteria, and the *P. putida* protein is a close ortholog (74.8% identity) of the biochemically characterized *Escherichia coli* enzyme.

The **primary function** of the Gcl gene product is to catalyze the decarboxylative condensation of **two molecules of glyoxylate** into **tartronate semialdehyde** (2-hydroxy-3-oxopropanoate) plus **CO₂**. This is a thiamine-pyrophosphate (TPP)- and FAD-dependent reaction, placing Gcl mechanistically in the acetohydroxyacid synthase (AHAS)/pyruvate oxidase family of ThDP enzymes. The reaction is the **committed, carbon–carbon-bond-forming entry step of the glycerate (tartronate-semialdehyde) pathway**, the metabolic route by which cells assimilate two-carbon (C2) units arriving as glyoxylate — for example, during the catabolism of glycolate and ethylene glycol.

In terms of **localization**, Gcl is a **soluble cytoplasmic enzyme**: it carries no signal peptide and no membrane-spanning segments, consistent with its role in central carbon metabolism. In terms of **pathway context**, *gcl* is the first gene of a five-gene operon (*gcl-hyi-glxR-ttuD-pykF*, PP_4297–PP_4301) encoding the complete downstream glycerate pathway, converting the tartronate semialdehyde product through D-glycerate and 2-phosphoglycerate into pyruvate/lower glycolysis. The operon is under negative transcriptional control by the regulator **GclR**, and its de-repression is the key adaptive event enabling *P. putida* KT2440 to grow on ethylene glycol as a sole carbon source. The functional assignment rests on multiple independent lines of evidence: *E. coli* biochemistry, *P. putida* proteomics and genetics, comparative sequence analysis with perfectly conserved cofactor-binding motifs, and curated KEGG pathway reconstruction.

---

## Key Findings

### Finding 1 — Gcl catalyzes the condensation of two glyoxylate molecules into tartronate semialdehyde + CO₂ (EC 4.1.1.47)

The defining catalytic activity of the Gcl protein is the condensation of **two molecules of glyoxylate** to yield **tartronic (tartronate) semialdehyde** and carbon dioxide. This reaction was established directly by the biochemical characterization of the cloned *E. coli* gcl gene product (Chang, Wang & Cronan, 1993; [PMID: 8440684](https://pubmed.ncbi.nlm.nih.gov/8440684/)), which states verbatim that "*Glyoxylate carboligase (Gcl) (EC 4.1.1.47) of Escherichia coli catalyzes the condensation of two molecules of glyoxylate to give tartronic semialdehyde, a key intermediate in glyoxylate catabolism.*"

The *P. putida* Q88F03 protein is annotated identically in UniProt: it carries the same recommended name (glyoxylate carboligase), the same EC number (4.1.1.47), and the same alternative name (tartronate-semialdehyde synthase). It belongs to the same TPP enzyme family and displays matching domain architecture: **Glyox_carbo_lig (IPR006397)**, **THDP-binding (IPR029061)**, and the TPP-binding central and C-terminal domains (**IPR012000 / IPR012001**). The tartronate semialdehyde product is described in the literature as "a key intermediate in glyoxylate catabolism," underscoring that this reaction is the entry point into a defined assimilatory pathway rather than an isolated transformation.

### Finding 2 — Gcl is a TPP- and FAD-dependent enzyme of the acetohydroxyacid synthase / pyruvate oxidase family

The Gcl enzyme is a thiamine-pyrophosphate (TPP)- and FAD-dependent enzyme. The *E. coli* enzyme is a 593-residue protein (~64.7 kDa) that displays **30% sequence similarity to the acetohydroxy acid synthases (AHAS)** of the branched-chain amino acid biosynthesis pathway and **26% identity to pyruvate oxidase**, and it contains binding sites for **thiamine pyrophosphate, FAD, and a quinone** ([PMID: 8440684](https://pubmed.ncbi.nlm.nih.gov/8440684/)). The paper states that "*Gcl contains a quinone binding site as well as binding site for thiamine pyrophosphate and FAD,*" and it notes the "*high level (30%) of sequence similarity to the acetohydroxy acid synthases (AHAS) of branched chain amino acid synthetic pathway.*"

These cofactor requirements are mechanistically important. TPP (thiamine diphosphate) is the catalytic cofactor that stabilizes the acyl-carbanion ("active aldehyde") intermediate needed to form the new C–C bond between the two glyoxylate-derived units, exactly as in other ThDP enzymes. The FAD in this family is structural rather than net-redox-active in the balanced overall reaction, a feature shared with AHAS. The UniProt domain architecture of Q88F03 — including the **DHS-like NAD/FAD-binding domain (IPR029035)**, the THDP-binding domain, and the TPP-binding domains — matches this enzyme family precisely, confirming that the *P. putida* protein shares the same cofactor-dependent mechanistic class.

### Finding 3 — Q88F03 is a true glyoxylate carboligase ortholog (74.8% identity to characterized *E. coli* Gcl) and is cytoplasmic

Comparative sequence analysis places Q88F03 unambiguously as an ortholog of the biochemically validated *E. coli* enzyme. A global Needleman–Wunsch alignment of *P. putida* KT2440 Gcl (Q88F03, 591 aa) against the characterized *E. coli* Gcl (P0AEP7 / GCL_ECOLI, 593 aa) yields **449/600 identical positions = 74.8% identity** over the full-length alignment (76.0% over the *P. putida* length). The two proteins are nearly identical in length (591 vs 593 aa), consistent with a one-to-one orthologous relationship rather than a distant paralog or a mis-annotated family member.

This level of identity — well above the ~40% threshold often used to transfer enzymatic function with confidence, and comfortably above the ~30% AHAS-family similarity that already implies a shared fold — provides strong evidence that Q88F03 catalyzes the same reaction as the *E. coli* enzyme.

Regarding **localization**, the protein has no N-terminal secretion signal. N-terminal Kyte–Doolittle hydropathy analysis (window 19) peaks at only **0.89** across the first 30 residues, well below the ~1.6 value characteristic of Sec-dependent signal peptides, and the mature N-terminus (MSKMRAIDAAVLVMRRE…) is hydrophilic and charged. Together with the absence of transmembrane segments, this indicates that Gcl is a **soluble cytoplasmic enzyme**, the expected compartment for an enzyme of central carbon/glyoxylate metabolism.

### Finding 4 — Catalytic and TPP/FAD cofactor-binding regions are perfectly conserved between the *P. putida* and *E. coli* orthologs

Beyond the high overall identity, the functionally critical regions of Gcl are perfectly conserved between *P. putida* and *E. coli*. The full-length pairwise alignment (74.8% overall identity) contains several long, 100%-identical blocks concentrated in the domains that build and bind the cofactors and substrate:

| Conserved block (P. putida position) | Sequence | Functional domain |
|---|---|---|
| ~res 87 (33 residues) | `LYSASADSIPILCITGQAPRARLHKEDFQAVDI` | N-terminal pyrimidine-binding (PYR) domain |
| ~res 410 (22 residues) | `RHWINCGQAGPLGWTIPAALGV` | Central transketolase-like domain |
| ~res 468 (14 residues) | `HVLVNNAYLGLIRQ` | C-terminal TPP-binding domain (contains conserved "NN" of the ThDP diphosphate-binding fingerprint) |

Nine non-overlapping 25-residue windows are 100% identical between the two orthologs. Critically, the C-terminal block containing the "**NN**" motif corresponds to the canonical thiamine-diphosphate diphosphate-binding fingerprint of the InterPro TPP-binding domain (IPR012001), and the N-terminal block sits within the pyrimidine-binding portion of the ThDP cofactor pocket. The fact that these substrate- and cofactor-contacting regions are perfectly (not just highly) conserved provides strong structural/evolutionary evidence that Q88F03 retains a fully functional active site and is a **catalytically intact** glyoxylate carboligase, not a degenerate pseudoenzyme.

### Finding 5 — KEGG confirms the reaction and a complete downstream glycerate-pathway operon at PP_4297–PP_4301

Curated pathway data corroborate the biochemical assignment and place *gcl* at the head of a complete metabolic module. KEGG assigns **PP_4297/gcl to KO K01608** (tartronate-semialdehyde synthase, EC 4.1.1.47) within pathway **ppu00630 (Glyoxylate and dicarboxylate metabolism)**, and annotates the protein with Pfam TPP_enzyme_N/M/C domains. The EC 4.1.1.47 reaction is formally written as "**2 glyoxylate = 2-hydroxy-3-oxopropanoate + CO₂**" (KEGG reaction R00013; systematic name *glyoxylate carboxy-lyase (dimerizing; 2-hydroxy-3-oxopropanoate-forming)*).

The genomic context is especially informative. Gene *gcl* (coordinates 4,886,942–4,888,717, + strand) is immediately followed on the same strand by a contiguous set of glycerate-pathway genes:

| Locus | Gene | KO | Enzyme | EC |
|---|---|---|---|---|
| PP_4297 | *gcl* | K01608 | Glyoxylate carboligase / tartronate-semialdehyde synthase | 4.1.1.47 |
| PP_4298 | *hyi* | K01816 | Hydroxypyruvate isomerase | 5.3.1.22 |
| PP_4299 | *glxR* | K00042 | 2-hydroxy-3-oxopropionate (tartronate semialdehyde) reductase | 1.1.1.60 |
| PP_4300 | *ttuD* | K11529 | Glycerate 2-kinase | 2.7.1.165 |
| PP_4301 | *pykF* | K00873 | Pyruvate kinase | 2.7.1.40 |

PP_4296 is divergently transcribed on the complementary strand. This arrangement encodes the enzymatic steps needed to convert tartronate semialdehyde all the way to pyruvate: reduction to D-glycerate (GlxR), phosphorylation to 2-phosphoglycerate (TtuD glycerate 2-kinase), and entry into lower glycolysis, with the isomerase Hyi handling hydroxypyruvate/tartronate-semialdehyde interconversions. The colocalization of the entire pathway in one operon is powerful genomic evidence that Gcl's biological role is to feed C2 (glyoxylate) carbon into central metabolism.

### Finding 6 — In *P. putida*, Gcl is the key glyoxylate-assimilation enzyme induced during glycolate/ethylene-glycol catabolism

Physiological, proteomic, and genetic studies in *P. putida* directly demonstrate that Gcl functions in glyoxylate assimilation. Comparative proteomics of *P. putida* JM37 showed that **tartronate semialdehyde synthase (Gcl), malate synthase (GlcB), and isocitrate lyase (AceA) are specifically induced when cells are grown on ethylene glycol or glyoxylic acid** (Mückschel et al., 2012; [PMID: 23023748](https://pubmed.ncbi.nlm.nih.gov/23023748/)). The paper states that "*tartronate semialdehyde synthase (Gcl), malate synthase (GlcB), and isocitrate lyase (AceA) were found to be induced in the presence of ethylene glycol or glyoxylic acid,*" defining the physiological trigger for Gcl expression.

In KT2440, **adaptive laboratory evolution for growth on ethylene glycol converged on de-repression of the glyoxylate carboligase pathway** (Li et al., 2019; [PMID: 31166064](https://pubmed.ncbi.nlm.nih.gov/31166064/)), which identifies "*a central role of the transcriptional regulator GclR, which represses the glyoxylate carboligase pathway.*" This establishes the Gcl (glyoxylate carboligase) pathway as the metabolic route that enables ethylene-glycol utilization once the block imposed by the regulator is lifted.

### Finding 7 — *gcl* (PP_4297) is an operonic gene repressed by GclR, acting with GlxR in the glycerate pathway

The regulation and functional partnership of *gcl* are well defined. In KT2440, *gcl* and its four neighboring genes (*hyi, glxR, ttuD, pykF*) are co-transcribed as a single operon: Franden et al. (2018; [PMID: 29885475](https://pubmed.ncbi.nlm.nih.gov/29885475/)) report that "*all of the four genes in genomic proximity to gcl (hyi, glxR, ttuD, and pykF) are transcribed as an operon.*" Functionally, expression of just two of these genes is the minimal requirement to unlock ethylene-glycol growth — "*the expression of only two genes (gcl and glxR) resulted in growth in ethylene glycol*" — showing that Gcl (glyoxylate carboligase) acts immediately upstream of GlxR (tartronate semialdehyde reductase) in the glycerate pathway, with full operon expression further improving growth.

Transcriptional control is provided by **GclR**, a repressor. Adaptive laboratory evolution independently and repeatedly selected loss-of-function mutations in GclR as the primary route to derepress the pathway (Li et al., 2019; [PMID: 31166064](https://pubmed.ncbi.nlm.nih.gov/31166064/)), which describes "*the transcriptional regulator GclR, which represses the glyoxylate carboligase pathway as part of a larger metabolic context of purine and allantoin metabolism.*" This ties the pathway not only to C2 (glycolate/ethylene glycol) catabolism but also to the broader glyoxylate flux generated by purine/allantoin degradation.

---

## Mechanistic Model / Interpretation

Integrating the seven findings yields a coherent mechanistic and physiological model of Gcl (PP_4297) in *P. putida* KT2440.

**The catalyzed reaction.** Gcl is a ThDP-dependent lyase/carboligase that performs a decarboxylative carboligation. Using its TPP cofactor to generate an active-aldehyde (thiamine-bound carbanion) intermediate from one glyoxylate, it forms a new carbon–carbon bond to a second glyoxylate and releases CO₂, producing the three-carbon product tartronate semialdehyde:

```
      Glyoxylate  +  Glyoxylate
        (C2)          (C2)
           \           /
            \         /   [ Gcl: TPP, FAD ]
             \       /
              v     v
     Tartronate semialdehyde (C3, 2-hydroxy-3-oxopropanoate)  +  CO2
```

**The glycerate (tartronate-semialdehyde) pathway.** Gcl is the first, committed, C–C-bond-forming step of a linear pathway encoded in one operon. The downstream steps, all encoded adjacent to *gcl*, convert the product to central-metabolic intermediates:

```
 Glycolate / Ethylene glycol
        |  (upstream oxidation)
        v
   2 x Glyoxylate
        |  gcl / PP_4297   (Glyoxylate carboligase, EC 4.1.1.47)   <-- committed step
        v
 Tartronate semialdehyde  (+ CO2)
        |  glxR / PP_4299  (Tartronate-semialdehyde reductase, EC 1.1.1.60; NAD(P)H)
        v
   D-Glycerate
        |  ttuD / PP_4300  (Glycerate 2-kinase, EC 2.7.1.165)
        v
   2-Phosphoglycerate
        |  (enolase; then pykF / PP_4301 pyruvate kinase, EC 2.7.1.40)
        v
   Pyruvate  ->  Lower glycolysis / TCA cycle
```

The isomerase *hyi* (PP_4298, hydroxypyruvate isomerase) participates in interconversion of tartronate semialdehyde/hydroxypyruvate species within this module. The net effect of the pathway is to assimilate two C2 glyoxylate units (four carbons in, one lost as CO₂) into a single three-carbon glycerate that can be phosphorylated and fed into gluconeogenesis/glycolysis and the TCA cycle. This is the classic "glycerate pathway" of glyoxylate assimilation, and Gcl is its gatekeeper.

**Physiological role and regulation.** Under standard conditions the operon is silenced by the repressor GclR. The pathway becomes physiologically relevant when the cell must metabolize substrates that funnel carbon through glyoxylate — most prominently **ethylene glycol** and **glycolate**, but also glyoxylate generated by **purine/allantoin** catabolism. Proteomics shows Gcl (with GlcB malate synthase and AceA isocitrate lyase) is induced on ethylene glycol/glyoxylate, and laboratory evolution shows that lifting GclR repression is the decisive adaptive event permitting growth on ethylene glycol. Notably, cells appear to have two possible fates for glyoxylate: (i) the **glyoxylate shunt** (isocitrate lyase/malate synthase) for anaplerosis, and (ii) the **glycerate pathway** (Gcl) for net C2 assimilation into glycolytic carbon. Co-induction of both routes on ethylene glycol suggests they operate together to balance anaplerotic and assimilatory demands.

**Localization.** All evidence — the absence of a signal peptide, low N-terminal hydropathy, lack of transmembrane segments, and the enzyme's role in central carbon metabolism — indicates that Gcl performs its function in the **cytoplasm** as a soluble enzyme.

---

## Evidence Base

| PMID | Study | Relevance to Gcl (Q88F03) |
|---|---|---|
| [8440684](https://pubmed.ncbi.nlm.nih.gov/8440684/) | *Molecular cloning, DNA sequencing, and biochemical analyses of E. coli glyoxylate carboligase* (Chang, Wang & Cronan, 1993) | **Primary biochemical reference.** Directly establishes the catalyzed reaction (2 glyoxylate → tartronic semialdehyde), the EC number (4.1.1.47), the cofactors (TPP, FAD, quinone site), and family membership (AHAS/pyruvate oxidase). Q88F03 is a 74.8%-identical ortholog of this enzyme. |
| [23023748](https://pubmed.ncbi.nlm.nih.gov/23023748/) | *Ethylene glycol metabolism by Pseudomonas putida* (Mückschel et al., 2012) | Proteomic evidence that Gcl (tartronate semialdehyde synthase) is specifically induced on ethylene glycol/glyoxylate in *P. putida*, defining its physiological role in C2/glyoxylate catabolism. |
| [29885475](https://pubmed.ncbi.nlm.nih.gov/29885475/) | *Engineering Pseudomonas putida KT2440 for efficient ethylene glycol utilization* (Franden et al., 2018) | Defines the *gcl-hyi-glxR-ttuD-pykF* operon; shows *gcl* + *glxR* are the minimal pair sufficient for ethylene-glycol growth, placing Gcl upstream of tartronate-semialdehyde reductase (GlxR). |
| [31166064](https://pubmed.ncbi.nlm.nih.gov/31166064/) | *Laboratory evolution reveals the metabolic and regulatory basis of ethylene glycol metabolism by P. putida KT2440* (Li et al., 2019) | Identifies GclR as the repressor of the glyoxylate carboligase pathway and links its de-repression to ethylene-glycol growth and to purine/allantoin metabolism. |
| [21751162](https://pubmed.ncbi.nlm.nih.gov/21751162/) | *Plasmid construction for a glycolate-oxidizing pathway in plants* (2011) | Uses glyoxylate carboligase and tartronic semialdehyde reductase as engineering tools, corroborating the pathway partnership and the functional annotation of Gcl. |
| [14342490](https://pubmed.ncbi.nlm.nih.gov/14342490/) | *The utilization of glycollate by Micrococcus denitrificans: the beta-hydroxyaspartate pathway* (1965) | Provides classical context: an organism that assimilates glyoxylate via an **alternative** (β-hydroxyaspartate) route with "negligible glyoxylate-carboligase activity," highlighting by contrast that Gcl defines the glycerate pathway. |

The convergence of these independent evidence types — direct enzymology, comparative proteomics, operon genetics, adaptive-evolution regulatory mapping, and curated KEGG pathway reconstruction — makes the functional assignment of Q88F03 as glyoxylate carboligase highly robust.

---

## Limitations and Knowledge Gaps

1. **No direct biochemistry on the *P. putida* protein.** The catalytic assignment for Q88F03 rests on strong homology (74.8% identity, perfectly conserved active-site motifs) to the *E. coli* enzyme and on proteomic/genetic association, but the purified *P. putida* KT2440 protein has not, to our knowledge, been kinetically characterized (kcat, Km for glyoxylate, cofactor stoichiometry). Substrate specificity is inferred, not directly measured, in this organism.

2. **Localization is predicted, not experimentally verified.** The cytoplasmic assignment is based on bioinformatic signal-peptide and hydropathy analysis plus the enzyme's metabolic role. No fractionation or microscopy data specific to *P. putida* Gcl were examined.

3. **Quaternary structure and cofactor loading unconfirmed.** Family members (AHAS, pyruvate oxidase) are typically oligomeric with tightly bound TPP/FAD/Mg²⁺; the oligomeric state and exact cofactor content of the *P. putida* enzyme are inferred from homology only. No experimental structure of Q88F03 was analyzed.

4. **Regulatory details in KT2440 are partly indirect.** GclR-mediated repression and operon structure are well supported, but the precise GclR operator sequence, inducer molecule, and quantitative regulatory logic in the native (non-evolved) strain remain incompletely defined.

5. **Relative flux between glyoxylate shunt and glycerate pathway.** The quantitative partitioning of glyoxylate between anaplerosis (glyoxylate shunt) and assimilation (Gcl/glycerate pathway) under different growth conditions has not been resolved here.

---

## Proposed Follow-up Experiments / Actions

1. **Enzymatic characterization of purified Q88F03.** Overexpress and purify the *P. putida* KT2440 Gcl, confirm TPP/FAD/Mg²⁺ dependence, and measure kinetic constants for glyoxylate and possible alternative 2-oxo-acid substrates to test substrate specificity directly.

2. **Structural determination.** Solve the crystal or cryo-EM structure (or generate/validate an AlphaFold model) to confirm the ThDP/FAD binding-pocket architecture and the oligomeric state, and to validate that the perfectly conserved motifs form the active site.

3. **Targeted gene deletion and complementation.** Construct a clean Δ*gcl* mutant in KT2440 and test growth on ethylene glycol, glycolate, and glyoxylate; complement with Q88F03 to demonstrate that this specific gene is necessary for the glycerate-pathway phenotype.

4. **Localization confirmation.** Use cell fractionation and/or a fluorescent fusion to verify cytoplasmic localization experimentally.

5. **Regulatory mapping of GclR.** Perform ChIP-seq/EMSA to define the GclR operator upstream of PP_4297 and identify the physiological inducer, clarifying the native regulatory circuit and its link to purine/allantoin metabolism.

6. **¹³C metabolic flux analysis.** Trace ¹³C-labeled ethylene glycol/glycolate to quantify flux partitioning between the Gcl/glycerate pathway and the glyoxylate shunt under different carbon regimes.

---

## Conclusion

The gene identity is confirmed and unambiguous: **gcl (PP_4297, UniProt Q88F03) of *Pseudomonas putida* KT2440 encodes glyoxylate carboligase / tartronate-semialdehyde synthase (EC 4.1.1.47)**, a soluble cytoplasmic, TPP- and FAD-dependent enzyme of the AHAS/pyruvate-oxidase (TPP enzyme) family. Its primary function is the decarboxylative condensation of two glyoxylate molecules into tartronate semialdehyde plus CO₂ — the committed first step of the glycerate pathway that assimilates C2 carbon (from glycolate, ethylene glycol, and purine/allantoin-derived glyoxylate) into lower glycolysis. This assignment is supported by direct *E. coli* biochemistry, 74.8% sequence identity with perfectly conserved active-site motifs, *P. putida* proteomics and genetics, operon structure (*gcl-hyi-glxR-ttuD-pykF*, PP_4297–PP_4301), GclR-mediated regulation, and curated KEGG pathway data.


## Artifacts

- [OpenScientist final report](gcl-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](gcl-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:8440684
2. PMID:23023748
3. PMID:31166064
4. PMID:29885475