---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5, claude-opus-5-5
cached: false
start_time: '2026-11-08T08:08:09.087438'
end_time: '2026-11-08T08:10:00.404136'
duration_seconds: 111.32
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: mouse
  gene_id: G6pc2
  gene_symbol: G6pc2
  uniprot_accession: Q9Z186
  protein_description: 'RecName: Full=Glucose-6-phosphatase 2; Short=G-6-Pase 2; Short=G6Pase
    2; EC=3.1.3.9; AltName: Full=Islet-specific glucose-6-phosphatase catalytic subunit-related
    protein;'
  gene_info: Name=G6pc2; Synonyms=Igrp;
  organism_full: Mus musculus (Mouse).
  protein_family: Belongs to the glucose-6-phosphatase family. .
  protein_domains: Glucose-6-phosphatase. (IPR016275); PAP2/HPO. (IPR000326); PAP2/HPO_sf.
    (IPR036938); PAP2 (PF01569)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    claude_executable: claude
    skip_permissions: false
    allowed_tools:
    - WebSearch
    - WebFetch
    add_dirs: []
    timeout: 1800
    min_report_chars: 200
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-5-5
  - claude-opus-5
  - claude-opus-5-5
  web_search_requests: 2
  num_turns: 14
  total_cost_usd: 0.9674679
  session_id: b9b877d1-195c-4e7e-b6a9-8eb11efc0cb2
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  assistant_text_blocks: 3
citation_count: 12
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q9Z186
- **Protein Description:** RecName: Full=Glucose-6-phosphatase 2; Short=G-6-Pase 2; Short=G6Pase 2; EC=3.1.3.9; AltName: Full=Islet-specific glucose-6-phosphatase catalytic subunit-related protein;
- **Gene Information:** Name=G6pc2; Synonyms=Igrp;
- **Organism (full):** Mus musculus (Mouse).
- **Protein Family:** Belongs to the glucose-6-phosphatase family. .
- **Key Domains:** Glucose-6-phosphatase. (IPR016275); PAP2/HPO. (IPR000326); PAP2/HPO_sf. (IPR036938); PAP2 (PF01569)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "G6pc2" matches the protein description above**
2. **Verify the organism is correct:** Mus musculus (Mouse).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'G6pc2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **G6pc2** (gene ID: G6pc2, UniProt: Q9Z186) in mouse.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

Gathering key primary papers (enzymology, knockout physiology) before writing the report.

# G6pc2 (IGRP, glucose-6-phosphatase 2) in mouse: function, localization and pathways

**UniProt Q9Z186 · Mus musculus · glucose-6-phosphatase family (PAP2/HPO superfamily; IPR016275, PF01569)**

---

## 0. Identity check

The target is the right gene. The symbol *G6pc2* (synonym *Igrp*) matches UniProt Q9Z186, "Glucose-6-phosphatase 2 / Islet-specific glucose-6-phosphatase catalytic subunit-related protein", EC 3.1.3.9, in *Mus musculus*. The literature found describes the same protein:

- It was cloned from mouse insulinoma.
- It is 355 amino acids long, with a predicted mass of about 40.7 kDa.
- It shares about 50% identity with the liver enzyme G6PC1.
- It belongs to the glucose-6-phosphatase family, which matches the PAP2 domain annotation.

The 1999 cloning paper reports these properties: "The longer, 1901-bp full-length cDNA encoded a 355-amino acid protein (molecular weight 40,684) structurally related (50% overall identity) to the liver glucose-6-phosphatase and exhibited similar predicted transmembrane topology, conservation of catalytically important residues, and the presence of an endoplasmic reticulum retention signal" [PMID:10078553, Arden et al., *Diabetes* 1999]. I found no conflicting gene with the same symbol.

---

## 1. Summary

G6pc2 is the catalytic subunit of the pancreatic β-cell's glucose-6-phosphatase. It sits in the endoplasmic reticulum (ER) membrane, spans it multiple times, and is N-glycosylated. It hydrolyses D-glucose 6-phosphate (G6P) to D-glucose and inorganic phosphate, with a Km of about 0.3–0.45 mM [PMID:14722102].

Its main physiological role is not gluconeogenesis, as it is in liver. Instead it opposes glucokinase in the β-cell, creating a futile glucose ⇄ G6P cycle. This cycle reduces glycolytic flux and shifts the glucose dose–response of insulin secretion to the right. G6pc2 therefore acts as a negative regulator of basal glucose-stimulated insulin secretion (GSIS), and so helps set the fasting blood glucose level [PMID:23274894].

Two further facts complete the picture:

- **Autoantigen:** in NOD mice, G6pc2/IGRP is a major autoantigen, and pathogenic CD8⁺ T cells target it in autoimmune diabetes [PMID:12815107].
- **GWAS locus:** the human *G6PC2* locus is one of the strongest genome-wide association signals for fasting glucose.

---

## 2. Molecular function: the reaction and its substrate

### 2.1 Reaction

**D-glucose 6-phosphate + H₂O → D-glucose + phosphate** (EC 3.1.3.9; RHEA:16689). In GO terms this is glucose-6-phosphatase activity, GO:0004346.

UniProt records this activity with experimental evidence (ECO:0000269) from Petrolonis et al. 2004 [PMID:14722102]. That study states:

> "Here we present evidence that the previously identified islet-specific glucose-6-phosphatase-related protein (IGRP) is indeed the major islet glucose-6-phosphatase. IGRP overexpressed in insect cells possesses enzymatic activity comparable to the previously described G-6-Pase activity in islets. The K(m) and V(max) values determined using glucose-6-phosphate as the substrate were 0.45 mm and 32 nmol/mg/min by malachite green assay, and 0.29 mm and 77 nmol/mg/min by glucose oxidase/peroxidase coupling assay, respectively."

The same group found a small molecule that inhibits IGRP specifically. This supports the view that the activity belongs to IGRP and not to a contaminating phosphatase [PMID:14722102].

### 2.2 History and caveats

Earlier work could not detect catalytic activity for IGRP. Petrolonis et al. note that "the authors could not demonstrate enzymatic activity for this protein" [PMID:14722102]. Two points from the later work explain the discrepancy:

- G6PC2 turns over substrate much more slowly than hepatic G6PC1, which made it hard to detect.
- Deleting the gene in mice clearly reduces islet glucose-6-phosphatase activity. Pound et al. 2013 report: "Glucose-6-phosphatase activity was reduced … in islets isolated from G6pc2 KO mice" [PMID:23274894]. This loss-of-function result is the strongest support that the activity matters physiologically.

The mouse GOA file reflects these lines of evidence for GO:0004346:

- IDA, from PMID:14722102;
- IMP, from the knockout in PMID:23274894;
- IBA and ISO;
- a Reactome-based assertion.

### 2.3 Specificity

Only G6P was characterised as a substrate in the key enzymology study [PMID:14722102]. Broader phosphatase promiscuity, as reported for hepatic G6PC1 (for example pyrophosphate or carbamyl phosphate activity), has not been established for G6PC2. Within the PAP2 superfamily, G6PCs are the members specialised for sugar phosphates.

### 2.4 Catalytic mechanism, inferred from the family

G6pc2 has the PAP2 / acid phosphatase signature (PF01569). By analogy with G6PC1, catalysis is thought to go through a phosphohistidine intermediate. The UniProt features are:

| Residue | Role | Evidence |
|---|---|---|
| His174 | Nucleophile (phosphoryl acceptor) | By similarity (ECO:0000250) |
| His115 | Proton donor | Predicted (ECO:0000255) |
| Arg79, Arg168 | Phosphate-binding | Predicted (ECO:0000255) |

The cloning paper notes that a shorter splice variant lacking exon IV produces open reading frames, "neither of which possessed His174, a residue thought to be the phosphoryl acceptor" [PMID:10078553]. That isoform (Q9Z186-2) is therefore predicted to be inactive.

---

## 3. Where the protein acts

### 3.1 ER membrane, active site in the lumen

UniProt records the location as "Endoplasmic reticulum membrane; Multi-pass membrane protein". This is evidence by similarity (ECO:0000250) to G6PC1 and human G6PC2.

The mouse sequence carries **nine predicted transmembrane helices** (UniProt TRANSMEM 25–45 … 319–339). In the G6PC1 model, the conserved catalytic residues (Arg79, His115, Arg168, His174) lie on the luminal side of the ER membrane.

Further support for ER residence comes from three sources:

- The cloning paper reports an ER-retention signal [PMID:10078553].
- Pound et al. call it an "islet-specific, endoplasmic reticulum-resident glucose-6-phosphatase catalytic subunit" [PMID:23274894].
- Topology studies of human IGRP (PubMed 15044018, retrieved as a title only in this search) and secondary summaries describe it as an ER-embedded glycoprotein [Wikipedia: G6PC2](https://en.wikipedia.org/wiki/G6PC2).

### 3.2 Glycosylation

The protein has one N-glycosylation site, Asn92, which lies in a predicted luminal loop (TOPO_DOM 78–115). UniProt states that the non-glycosylated form is less stable and is degraded by the proteasome (by similarity). This fits with ER-associated quality control.

### 3.3 Substrate delivery by the G6P transporter

Because the active site faces the lumen, cytosolic G6P has to cross the ER membrane first. In liver the G6P translocase SLC37A4 (G6PT) does this. Hutton's group showed that murine islets express both components: "Evidence for the expression of both the hydrolase and translocase components of hepatic glucose-6-phosphatase in murine pancreatic islets" [PMID:12878201, title]. The working model is therefore SLC37A4 → G6PC2 in β-cell ER, a two-component system like the one in liver [PMC8800118](https://pmc.ncbi.nlm.nih.gov/articles/PMC8800118).

### 3.4 Tissue and developmental expression

G6pc2 is restricted to pancreatic islets, mainly β-cells. UniProt summarises it as "Not detected in testis, kidney, muscle, liver, lung, spleen, brain, pituitary, gastric fundus or heart" [PMID:10078553, PMID:12878201, PMID:14722102].

- **Development:** expression in the pancreas begins around E12 and is prominent by E14 [PMID:10078553].
- **Regulation by glucose:** islets cultured in high glucose up-regulate it [PMID:14722102].
- **Splicing:** islets express two transcripts that differ by exon IV; the shorter one is likely non-catalytic [PMID:10078553].
- **Promoter:** Ebert et al. 1999 characterised the islet-specific promoter [PMID:10078554].

---

## 4. Pathway role: the glucokinase–G6PC2 futile cycle in β-cell glucose sensing

### 4.1 Mechanism

In β-cells, glucokinase (GCK) is the glucose sensor that phosphorylates glucose to G6P and sets the rate of glycolysis. G6PC2 reverses that step in the ER lumen, producing a substrate (futile) cycle:

```
glucose --GCK (cytosol)--> G6P --SLC37A4--> ER lumen --G6PC2--> glucose + Pi
                             |
                             v
       glycolysis -> TCA -> ↑ATP/ADP -> K_ATP closure -> Ca2+ influx -> insulin secretion
```

The Vanderbilt group sums this up: "G6PC2 represents a novel, negative regulator of basal GSIS that acts by hydrolyzing glucose-6-phosphate, thereby reducing glycol

The report was interrupted mid-section. Rather than regenerate the same text, here is the remaining content in condensed form, covering the pathway role, knockout evidence, autoantigen function, and annotation implications.

## Pathway role (continued)

G6PC2 does not serve gluconeogenesis in the β-cell — islets lack the full gluconeogenic pathway, and UniProt's "PATHWAY: Carbohydrate biosynthesis; gluconeogenesis" line is a family-level inference carried over from G6PC1, not an experimental claim for this paralog. The documented role is the glucokinase–G6PC2 substrate cycle: by returning G6P to glucose, G6PC2 lowers net glycolytic flux at a given extracellular glucose concentration, raising the threshold at which the ATP/ADP ratio rises enough to close K_ATP channels and trigger Ca²⁺-dependent insulin release. The consequence is a rightward shift of the GSIS dose–response curve.

## Knockout evidence

- **Pound et al. 2013** [PMID:23274894]: *G6pc2* deletion produced "a leftward shift in the dose-response curve for glucose-stimulated insulin secretion (GSIS)." As a result, "under fasting conditions in which plasma insulin levels were identical, blood glucose levels were reduced in G6pc2 KO mice." Islet glucose-6-phosphatase activity was reduced and basal cytoplasmic Ca²⁺ was elevated. Insulin sensitivity and glucose tolerance were largely unaffected; body fat was reduced in female KO mice. These effects mirror human *G6PC2* GWAS associations with fasting glucose and body fat but not insulin sensitivity.
- **Wang et al. 2007** [PMID:17265032]: the original KO showed "no overt anatomical or behavioral phenotype but display a mild metabolic phenotype," with significantly lower fasting blood glucose and triacylglycerol (UniProt DISRUPTION PHENOTYPE).
- **Flux studies** from the same groups report increased glycolytic and TCA-cycle flux in KO islets, supporting a quantitatively meaningful cycle ([Wall et al. 2015](https://www.vanderbilt.edu/younglab/pdf/wall15.pdf); [PMC4439557](https://pmc.ncbi.nlm.nih.gov/articles/PMC4439557); [PMC4041587](https://pmc.ncbi.nlm.nih.gov/articles/PMC4041587)). Caveat: most of this work comes from one or two laboratories, and the magnitude of glucose cycling in islets has been contested since the radioisotope era.

GOA reflects this as *glucose homeostasis* (GO:0042593) and *regulation of insulin secretion* (GO:0050796), both IMP/ISO from the knockout work.

## Second, non-enzymatic role: β-cell autoantigen

IGRP is a dominant autoantigen in NOD mouse autoimmune diabetes — "the β-cell antigen targeted by a prevalent population of pathogenic CD8+ T cells in autoimmune diabetes" [PMID:12815107], with CD4⁺ epitopes also mapped [PMID:15843527]. This is a property of the protein as a peptide source, not an activity it carries out, so it does not correspond to a molecular function term.

## Annotation implications

| Claim | Support | Confidence |
|---|---|---|
| GO:0004346 glucose-6-phosphatase activity | IDA kinetics [PMID:14722102] + KO loss of islet activity [PMID:23274894] | High — core function |
| GO:0005789 ER membrane, multi-pass | 9 TM helices; ER retention signal [PMID:10078553]; ER-resident [PMID:23274894] | High, though direct mouse localization evidence is by similarity |
| Active site luminal; needs SLC37A4 for substrate | Family topology; both components in islets [PMID:12878201] | Moderate-high (inference) |
| GO:0050796 regulation of insulin secretion (negative) | KO GSIS shift [PMID:23274894] | High |
| GO:0042593 glucose homeostasis | reduced fasting glucose in KO [PMID:17265032, PMID:23274894] | High |
| GO:0006094 gluconeogenesis | IBA/Reactome only; islets are not gluconeogenic | **Likely over-annotation** by propagation from G6PC1 |

Open questions worth flagging: whether G6PC2 has substrates beyond G6P; whether the exon-IV-skipping isoform (Q9Z186-2, lacking His174) has any role; and direct structural confirmation of the nine-TM topology and luminal active site in mouse.

**Sources:** [PMID:10078553](https://pubmed.ncbi.nlm.nih.gov/10078553/), [PMID:14722102](https://pubmed.ncbi.nlm.nih.gov/14722102/), [PMID:23274894](https://pubmed.ncbi.nlm.nih.gov/23274894/), [PMID:12878201](https://pubmed.ncbi.nlm.nih.gov/12878201/), [PMID:12815107](https://pubmed.ncbi.nlm.nih.gov/12815107/), [PMID:17265032](https://pubmed.ncbi.nlm.nih.gov/17265032/), [Wikipedia G6PC2](https://en.wikipedia.org/wiki/G6PC2), [PMC8800118](https://pmc.ncbi.nlm.nih.gov/articles/PMC8800118), [PMC3636628](https://pmc.ncbi.nlm.nih.gov/articles/PMC3636628)

I couldn't retrieve cached full text for PMID:17265032 or PMID:12815107 — those two rest on UniProt's curated statements and the paper titles rather than on text I read directly.

## Citations

1. https://en.wikipedia.org/wiki/G6PC2
2. https://pmc.ncbi.nlm.nih.gov/articles/PMC8800118
3. https://www.vanderbilt.edu/younglab/pdf/wall15.pdf
4. https://pmc.ncbi.nlm.nih.gov/articles/PMC4439557
5. https://pmc.ncbi.nlm.nih.gov/articles/PMC4041587
6. https://pubmed.ncbi.nlm.nih.gov/10078553/
7. https://pubmed.ncbi.nlm.nih.gov/14722102/
8. https://pubmed.ncbi.nlm.nih.gov/23274894/
9. https://pubmed.ncbi.nlm.nih.gov/12878201/
10. https://pubmed.ncbi.nlm.nih.gov/12815107/
11. https://pubmed.ncbi.nlm.nih.gov/17265032/
12. https://pmc.ncbi.nlm.nih.gov/articles/PMC3636628