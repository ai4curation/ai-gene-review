---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-30T19:33:11.412976'
end_time: '2026-09-30T19:45:23.398744'
duration_seconds: 731.99
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: SEC23A
  gene_symbol: SEC23A
  uniprot_accession: Q15436
  protein_description: 'RecName: Full=Protein transport protein Sec23A {ECO:0000305};
    Short=hSec23A {ECO:0000303|PubMed:8898360}; AltName: Full=SEC23-related protein
    A;'
  gene_info: Name=SEC23A {ECO:0000312|HGNC:HGNC:10701};
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the SEC23/SEC24 family. SEC23 subfamily.
  protein_domains: ADF-H/Gelsolin-like_dom_sf. (IPR029006); Beta-sandwich_Sec23_24.
    (IPR012990); Gelsolin-like_dom. (IPR007123); Gelsolin-like_dom_sf. (IPR036180);
    Sec23. (IPR037364)
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
citation_count: 19
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: SEC23A-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: SEC23A-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q15436
- **Protein Description:** RecName: Full=Protein transport protein Sec23A {ECO:0000305}; Short=hSec23A {ECO:0000303|PubMed:8898360}; AltName: Full=SEC23-related protein A;
- **Gene Information:** Name=SEC23A {ECO:0000312|HGNC:HGNC:10701};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the SEC23/SEC24 family. SEC23 subfamily.
- **Key Domains:** ADF-H/Gelsolin-like_dom_sf. (IPR029006); Beta-sandwich_Sec23_24. (IPR012990); Gelsolin-like_dom. (IPR007123); Gelsolin-like_dom_sf. (IPR036180); Sec23. (IPR037364)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "SEC23A" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'SEC23A' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **SEC23A** (gene ID: SEC23A, UniProt: Q15436) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# SEC23A (Q15436): The COPII Inner-Coat Cargo Adaptor and Sar1 GAP That Drives ER Export

**Gene:** SEC23A | **Protein:** Protein transport protein Sec23A (hSec23A) | **UniProt:** Q15436
**Organism:** *Homo sapiens* | **Family:** SEC23/SEC24 family, SEC23 subfamily | **HGNC:** 10701

## Summary

**SEC23A** encodes the human **Protein transport protein Sec23A** (UniProt **Q15436**, HGNC:10701), a core subunit of the **coat protein complex II (COPII)** machinery that mediates the first step of the secretory pathway: export of newly synthesized proteins from the endoplasmic reticulum (ER). SEC23A is not an enzyme in the classical metabolic sense and not a transporter of small molecules; rather, it is a **structural coat/adaptor protein with a built-in regulatory enzymatic activity**. It performs two tightly coupled jobs. First, together with a SEC24 partner it forms the **inner-layer "pre-budding" cargo adaptor** that physically selects, concentrates, and packages secretory and membrane cargo at specialized ER subdomains called **ER exit sites (ERES)**. Second, SEC23A is the **GTPase-activating protein (GAP)** for the small GTPase **Sar1**, inserting a catalytic arginine finger into the Sar1 active site to trigger GTP hydrolysis, thereby timing coat polymerization, recruitment of the outer SEC13/SEC31 layer, and ultimately vesicle budding ([PMID: 12239560](https://pubmed.ncbi.nlm.nih.gov/12239560/)).

SEC23A therefore carries out its function on the **cytosolic face of the ER membrane** at ER exit sites, where it drives the obligatory COPII route of anterograde ER-to-Golgi transport. Because the vast majority of proteins destined for secretion or for other compartments require COPII to leave the ER ([PMID: 24076263](https://pubmed.ncbi.nlm.nih.gov/24076263/)), SEC23A sits at a rate-limiting gateway of the secretory pathway. It is especially critical for the export of **bulky, non-canonical cargo such as procollagen**, which it packages into enlarged tubular carriers with the help of the TANGO1/cTAGE5 receptor system ([PMID: 27551091](https://pubmed.ncbi.nlm.nih.gov/27551091/)). Consistent with this, loss-of-function mutations in human SEC23A cause **cranio-lenticulo-sutural dysplasia (CLSD)**, a skeletal/craniofacial disease, and the zebrafish *sec23a* mutant *crusher* shows chondrocytes stuffed with undischarged collagen in a distended ER ([PMID: 17981132](https://pubmed.ncbi.nlm.nih.gov/17981132/); [PMID: 16980978](https://pubmed.ncbi.nlm.nih.gov/16980978/); [PMID: 18713835](https://pubmed.ncbi.nlm.nih.gov/18713835/)).

Beyond its housekeeping coat role, SEC23A functions as a **regulated secretome gate**: it is a direct post-transcriptional target of the miR-200 microRNA family, and SEC23A output controls the secretion of specific metastasis-suppressive factors (Igfbp4, Tinagl1), linking ER-export capacity to cancer cell behavior ([PMID: 21822286](https://pubmed.ncbi.nlm.nih.gov/21822286/)). Finally, SEC23A is **biochemically interchangeable with its paralog SEC23B**; the two cause distinct human diseases (CLSD vs. congenital dyserythropoietic anemia type II) chiefly because of tissue-specific expression and gene dosage rather than divergent molecular function ([PMID: 35441598](https://pubmed.ncbi.nlm.nih.gov/35441598/); [PMID: 34818036](https://pubmed.ncbi.nlm.nih.gov/34818036/)).

**Gene identity confirmed.** The gene symbol SEC23A, the human organism assignment, the SEC23/SEC24 family / SEC23 subfamily classification, and the InterPro domain architecture (gelsolin-like, β-sandwich Sec23/24, and Sec23-specific folds) are all fully consistent across UniProt annotation, structural biology, and the primary literature reviewed here. There is no ambiguity in this identification.

---

## Key Findings

### Finding 1 — SEC23A is the inner-coat COPII cargo adaptor AND the Sar1 GTPase-activating protein (GAP)

The defining mechanistic insight into SEC23A comes from the crystal structure of the yeast Sec23/24–Sar1 "pre-budding" complex ([PMID: 12239560](https://pubmed.ncbi.nlm.nih.gov/12239560/)). This structure shows that Sec23 forms a continuous surface with the small GTPase Sar1 and that the Sec23/24 heterodimer acts "to select SNARE and cargo molecules." Critically, **Sec23 supplies the GAP activity that accelerates GTP hydrolysis on Sar1**: "The GTPase-activating protein (GAP) activity of Sec23 involves an arginine side chain inserted into the Sar1 active site." This arginine-finger mechanism is the same catalytic strategy used by RasGAP and other GAPs, and it establishes SEC23A's dual identity — it is simultaneously the **cargo-selecting adaptor** and the **enzymatic timer** of the coat.

SEC23A (Q15436) belongs to the **SEC23/SEC24 family, SEC23 subfamily**, placing it firmly in the Sec23 branch that contributes GAP activity (as opposed to the Sec24 branch, which is dedicated to cargo-signal recognition). This is the single most important functional annotation for the protein: SEC23A is not a metabolic enzyme or small-molecule transporter but a **coat adaptor whose "catalysis" is the regulated hydrolysis of GTP on Sar1** to control vesicle coat dynamics.

### Finding 2 — SEC23A operates at ER exit sites and recruits the outer SEC13/SEC31 coat

COPII coats assemble through a defined, ordered sequence of recruitment events on the ER membrane: **Sar1-GTP → Sec23/Sec24 (inner coat) → Sec13/Sec31 (outer coat)** ([PMID: 12239560](https://pubmed.ncbi.nlm.nih.gov/12239560/); [PMID: 20679433](https://pubmed.ncbi.nlm.nih.gov/20679433/)). SEC23A sits at the center of this cascade. Studies of the CLSD-causing SEC23A missense mutant showed that "the mutant form of SEC23A poorly recruits the Sec13-Sec31 complex, inhibiting vesicle formation," and that patient cells "accumulate numerous tubular cargo-containing ER exit sites devoid of observable membrane coat" ([PMID: 17981132](https://pubmed.ncbi.nlm.nih.gov/17981132/)).

These two observations pin down both **where** SEC23A works (ER exit sites, on the cytosolic membrane surface) and **what** it does there (bridges the inner cargo-adaptor layer to the outer cage-forming Sec13/Sec31 layer). When that bridging fails, cargo still reaches ERES and the membrane still deforms into tubules, but a functional coat cannot be completed and transport carriers cannot bud — a precise, mechanistically interpretable phenotype rather than a diffuse secretory collapse.

### Finding 3 — SEC23A-dependent COPII transport is essential for secretion of large cargo (collagen) and for craniofacial development

A recurring theme across model systems is that SEC23A is **especially rate-limiting for the export of large/bulky cargo**, most notably procollagen, which is too large to fit into a canonical ~60–90 nm COPII vesicle. Townley et al. demonstrated that "efficient coupling of Sec23-Sec24 to Sec13-Sec31" is required for COPII-dependent collagen secretion and normal craniofacial development, and that when this coupling fails "secretion of collagen from primary fibroblasts is strongly inhibited" ([PMID: 18713835](https://pubmed.ncbi.nlm.nih.gov/18713835/)).

The in vivo requirement was shown dramatically in the zebrafish *crusher* mutant, which carries a *sec23a* nonsense mutation (L402X). In these animals, "crusher chondrocytes accumulate proteins in a distended endoplasmic reticulum, resulting in severe reduction of cartilage extracellular matrix (ECM) deposits, including type II collagen," producing a malformed craniofacial skeleton ([PMID: 16980978](https://pubmed.ncbi.nlm.nih.gov/16980978/)). In humans, loss-of-function SEC23A mutations cause **cranio-lenticulo-sutural dysplasia (CLSD)** ([PMID: 17981132](https://pubmed.ncbi.nlm.nih.gov/17981132/)), with subsequent case reports extending the allelic and inheritance spectrum, including a dominant de novo variant ([PMID: 38275611](https://pubmed.ncbi.nlm.nih.gov/38275611/)). The disease phenotype — late-closing fontanels, skeletal defects, and cataracts — directly reflects the impaired export of collagen and other large ECM cargo from cells that build the craniofacial skeleton.

### Finding 4 — Sec23A is a polyvalent template for TANGO1/cTAGE5-mediated assembly of large (procollagen) COPII coats

How does a coat built from standard subunits accommodate cargo as large as a 300-nm procollagen fiber? The answer involves SEC23A acting as a **repeating structural template**. Ma & Goldberg showed that procollagen is loaded at ER exit sites by the TANGO1/cTAGE5 receptor system, which molds a tubular carrier via "a distinctive helical array of the COPII inner coat protein Sec23/24" ([PMID: 27551091](https://pubmed.ncbi.nlm.nih.gov/27551091/)). The proline-rich domains of TANGO1 and cTAGE5 bind Sec23 through **PPP (proline-proline-proline) motifs**, and because these receptors contain multiple PPP motifs, "a single TANGO1/cTAGE5 receptor can bind multiple copies of coat protein in a close-packed array."

This explains at a molecular level how SEC23A enables bulky-cargo export: multivalent PPP-motif docking onto the Sec23 surface nucleates and stabilizes an extended helical inner-coat lattice capable of shaping an enlarged tubular carrier. Importantly, the **outer-coat subunit Sec31 also contains PPP motifs that bind the same Sec23 surface**, which provides a built-in handoff: as the coat matures, Sec31 can compete for and displace TANGO1/cTAGE5, coupling cargo loading to coat completion. SEC23A is thus the shared binding platform onto which both the cargo receptor and the outer coat converge.

### Finding 5 — The Sec23A/Sec24 adaptor captures cargo via sequence-specific ER-exit codes and is tuned by Sar1 paralog identity

Cargo capture by the inner coat is **sequence-specific**, mediated by short "ER-exit codes" in the cytosolic tails of cargo proteins that dock onto the Sec23/Sec24 adaptor. Two well-defined examples illustrate the substrate logic:

- **CFTR** uses a **di-acidic (DxE) exit code**; "mutation of the code disrupts interaction with the COPII coat selection complex Sec23/Sec24" ([PMID: 15479737](https://pubmed.ncbi.nlm.nih.gov/15479737/)).
- **Human classical MHC class I molecules (HLA-A/-B/-C)** use a **C-terminal single amino acid (valine or alanine)** signal that binds the Sec23/24 complex to drive their ER export ([PMID: 20946353](https://pubmed.ncbi.nlm.nih.gov/20946353/)).

In addition to recognizing cargo codes, SEC23A-dependent coat assembly is **tuned by which Sar1 paralog is engaged**. In the CLSD mutant analysis, the defect "is modulated by the Sar1 GTPase paralog used in the reaction, indicating distinct affinities of the two human Sar1 paralogs for the Sec13-Sec31 complex" ([PMID: 17981132](https://pubmed.ncbi.nlm.nih.gov/17981132/)). This places SEC23A at a combinatorial node where cargo identity (via Sec24-bound exit codes) and GTPase identity (via Sar1 paralog) jointly determine coat output.

### Finding 6 — SEC23A is a regulated secretome gate: miR-200 represses it, controlling secretion of metastasis-suppressive proteins

SEC23A is not a constitutive housekeeping component expressed at fixed levels; its abundance is **post-transcriptionally controlled**, with functional consequences for which proteins a cell secretes. Korpal et al. showed that "miR-200s promote metastatic colonization partly through direct targeting of Sec23a, which mediates secretion of metastasis-suppressive proteins, including Igfbp4 and Tinagl1" ([PMID: 21822286](https://pubmed.ncbi.nlm.nih.gov/21822286/)). Lowering SEC23A via miR-200 therefore selectively curtails export of specific anti-metastatic secreted factors, promoting metastatic colonization.

This finding is mechanistically important for two reasons. First, it demonstrates that **SEC23A output is rate-limiting for the export of specific cargo**, such that modest changes in SEC23A level reshape the secretome rather than simply scaling it uniformly. Second, it shows that SEC23A is embedded in a **regulatory circuit (miR-200 → SEC23A → secretome)** that links epithelial–mesenchymal plasticity to ER-export capacity. A related study in hepatocellular carcinoma with bile-duct tumor thrombus similarly connected miR-200c/miR-141 loss, a Sec23a-mediated secretome, and reduced IGFBP4 ([PMID: 24135722](https://pubmed.ncbi.nlm.nih.gov/24135722/)), reinforcing the SEC23A–secretome axis in cancer.

### Finding 7 — SEC23A multidomain architecture matches its mechanistic roles

The domain organization annotated for Q15436 maps cleanly onto the functional roles established structurally. The Sec23/24–Sar1 crystal structure describes "a bow-tie-shaped structure, 15 nm long, with a membrane-proximal surface that is concave and positively charged to conform to the size and acidic-phospholipid composition of the COPII vesicle" ([PMID: 12239560](https://pubmed.ncbi.nlm.nih.gov/12239560/)), and an independent perspective confirmed that this "prebudding complex of COPII now provides a molecular view of this GTPase-directed coat assembly mechanism" ([PMID: 12408798](https://pubmed.ncbi.nlm.nih.gov/12408798/)).

The InterPro/UniProt domains for SEC23A correspond directly to this fold:

| Domain / region (InterPro) | Structural role in SEC23A |
|---|---|
| ADF-H / Gelsolin-like domain (IPR007123, IPR029006, IPR036180) | N-terminal and C-terminal gelsolin-like regions forming part of the bow-tie body |
| Beta-sandwich Sec23/24 (IPR012990) | Central β-sandwich forming the rigid core of the adaptor |
| Sec23 (IPR037364) | Sec23-specific zinc-finger/trunk region that contacts Sar1 and provides the GAP arginine finger |

The concave, positively charged membrane-proximal surface explains how the adaptor conforms to the curved, acidic-phospholipid-rich COPII membrane, while the Sec23-specific trunk/zinc-finger region provides the Sar1-contacting GAP surface. Thus the structure-to-function mapping is internally consistent: domain architecture → bow-tie fold → membrane-proximal cargo/membrane surface + Sar1 GAP surface.

### Finding 8 — SEC23A and SEC23B are functionally interchangeable paralogs; distinct diseases reflect tissue-specific expression

Vertebrates have two SEC23 paralogs, SEC23A and SEC23B, which are **biochemically interchangeable**. A 2022 review states that "SEC23B was found to functionally overlap with its paralogous protein, SEC23A, likely explaining the absence of CDAII in SEC23B-deficient mice," and that "increased SEC23A expression rescued the CDAII erythroid defect, suggesting a novel therapeutic strategy for the disease" ([PMID: 35441598](https://pubmed.ncbi.nlm.nih.gov/35441598/)). Direct experimental rescue was demonstrated by King et al., titled *SEC23A rescues SEC23B-deficient congenital dyserythropoietic anemia type II* ([PMID: 34818036](https://pubmed.ncbi.nlm.nih.gov/34818036/)).

The striking implication is that the **distinct human diseases** caused by the two paralogs — SEC23A mutation → cranio-lenticulo-sutural dysplasia (skeletal/craniofacial); SEC23B mutation → congenital dyserythropoietic anemia type II (erythroid) — arise not from divergent molecular function but from **tissue-specific expression patterns and gene dosage**. Each cell type relies predominantly on whichever paralog it expresses most; depleting that paralog produces a tissue-restricted phenotype even though the two proteins can substitute for one another biochemically.

### Finding 9 — COPII (and thus SEC23A) is the obligatory machinery for ER export of essentially all secreted/membrane proteins

Finally, SEC23A's functional annotation must be understood in the context of COPII's near-universal role. The authoritative review by Venditti, Wilson & De Matteis states that "the vast majority of proteins that are transported to different cellular compartments and secreted from the cell require coat protein complex II (COPII) for export from the endoplasmic reticulum (ER)," and notes that genetic diseases of the early secretory pathway (including SEC23A/CLSD) "added fundamental insights into the regulation of ER-derived carrier formation" ([PMID: 24076263](https://pubmed.ncbi.nlm.nih.gov/24076263/)). As the Sec23 inner-coat subunit of this machinery, SEC23A is a **core component of the obligatory ER-export route**, which is why its loss has such broad yet cargo-sensitive (especially collagen) consequences.

---

## Mechanistic Model / Interpretation

SEC23A can be understood as the **engine control unit of the COPII inner coat**: it simultaneously selects cargo, deforms the membrane, and times the reaction through GTP hydrolysis on Sar1. The full sequence of events on the ER membrane is:

```
   Cytosol
   ────────────────────────────────────────────────────────────────
                     Sar1-GDP  --(Sec12 GEF)-->  Sar1-GTP
                                                    |
                                      membrane insertion of Sar1
                                                    |
                                                    v
        ┌───────────────────────────────────────────────────────┐
        │   INNER COAT (pre-budding complex)                     │
        │        SEC23A  +  SEC24  :  Sar1-GTP                    │
        │   • SEC24 binds cargo ER-exit codes                    │
        │       - DxE di-acidic (e.g., CFTR)                     │
        │       - C-terminal Val/Ala (e.g., MHC-I)              │
        │   • SEC23A = Sar1 GAP (arginine finger)               │
        │   • SEC23A PPP-binding surface docks:                  │
        │       - TANGO1 / cTAGE5 (large cargo, procollagen)    │
        │       - SEC31 (outer coat)                             │
        └───────────────────────────────────────────────────────┘
                                                    |
                              SEC23A recruits SEC13/SEC31 outer cage
                                                    |
                                                    v
        ┌───────────────────────────────────────────────────────┐
        │   OUTER COAT: SEC13 / SEC31 polymerizes the cage       │
        │   • Completes curvature; drives budding                │
        │   • SEC31 stimulates SEC23A GAP activity               │
        └───────────────────────────────────────────────────────┘
                                                    |
                              GTP hydrolysis on Sar1 (timed by SEC23A)
                                                    |
                                                    v
             COPII vesicle / tubular carrier buds from ER exit site
                          ──> anterograde transport to Golgi
   ────────────────────────────────────────────────────────────────
   ER membrane (cytosolic face, at ER exit sites / transitional ER)
```

Three features of this model deserve emphasis:

1. **Dual function in one protein.** SEC23A is both a *structural adaptor* (cargo selection, membrane shaping, scaffold for the outer coat) and a *regulatory enzyme* (Sar1 GAP). The GAP activity is the molecular timer that couples cargo loading and coat maturation to vesicle release. Because SEC31 stimulates the GAP activity, coat completion and GTP hydrolysis are self-coordinated.

2. **A shared PPP-binding surface is the hub.** The same Sec23 surface that binds TANGO1/cTAGE5 PPP motifs also binds SEC31 PPP motifs. This creates an elegant handoff mechanism: large-cargo receptors first use SEC23A as a multivalent template to build an extended helical inner coat, and the outer coat subsequently competes for the same surface to seal and bud the carrier.

3. **Tunability.** SEC23A output is tuned at multiple levels — by the cargo exit codes it recognizes (via SEC24), by the Sar1 paralog engaged, and by its own abundance (via miR-200). This makes SEC23A a *regulated gate* rather than a constitutive pipe, which is why its modulation reshapes the secretome (e.g., selective loss of Igfbp4/Tinagl1 secretion in cancer).

### Comparative summary of SEC23A functional attributes

| Attribute | SEC23A (Q15436) |
|---|---|
| Molecular class | COPII inner-coat cargo adaptor + Sar1 GAP (not a metabolic enzyme or small-molecule transporter) |
| Primary "catalysis" | GTPase-activating protein for Sar1 via arginine-finger insertion |
| Binding partners | SEC24 (obligate heterodimer), Sar1-GTP, SEC13/SEC31, TANGO1/cTAGE5, p125A/Sec16 |
| Subcellular location | Cytosolic face of the ER at ER exit sites (transitional ER) |
| Pathway | COPII-mediated anterograde ER-to-Golgi transport (first step of secretory pathway) |
| Signature cargo | Procollagen (via TANGO1/cTAGE5); general secretory/membrane proteins with ER-exit codes |
| Regulation | miR-200 (post-transcriptional); Sar1 paralog identity; cargo exit-code affinity |
| Paralog | SEC23B — biochemically interchangeable; distinct disease by tissue expression |
| Disease (loss-of-function) | Cranio-lenticulo-sutural dysplasia (CLSD) |

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports the findings |
|---|---|---|
| [12239560](https://pubmed.ncbi.nlm.nih.gov/12239560/) | *Structure of the Sec23/24-Sar1 pre-budding complex of the COPII vesicle coat* | Foundational structure: Sec23 is the Sar1 GAP (arginine finger) and the cargo/SNARE-selecting inner adaptor; defines the bow-tie fold and membrane-proximal surface (F001, F007) |
| [12408798](https://pubmed.ncbi.nlm.nih.gov/12408798/) | *Three-dimensional structure of a COPII prebudding complex* | Independent perspective confirming the GTPase-directed coat-assembly mechanism (F007) |
| [17981132](https://pubmed.ncbi.nlm.nih.gov/17981132/) | *The genetic basis of a craniofacial disease provides insight into COPII coat assembly* | CLSD SEC23A mutant poorly recruits Sec13/31; patient cells accumulate coatless tubular ERES; Sar1 paralog modulation (F002, F005) |
| [18713835](https://pubmed.ncbi.nlm.nih.gov/18713835/) | *Efficient coupling of Sec23-Sec24 to Sec13-Sec31 drives COPII-dependent collagen secretion…* | Collagen export requires efficient inner-to-outer coat coupling; essential for craniofacial development (F003) |
| [16980978](https://pubmed.ncbi.nlm.nih.gov/16980978/) | *Secretory COPII coat component Sec23a is essential for craniofacial chondrocyte maturation* | Zebrafish *crusher* sec23a mutant: distended ER, loss of type II collagen/ECM (F003) |
| [38275611](https://pubmed.ncbi.nlm.nih.gov/38275611/) | *First Case of a Dominant De Novo … (CLSD)* | Extends human SEC23A disease/inheritance spectrum (F003) |
| [27551091](https://pubmed.ncbi.nlm.nih.gov/27551091/) | *TANGO1/cTAGE5 receptor as a polyvalent template for assembly of large COPII coats* | Sec23/24 helical array molds large carriers; PPP-motif multivalent binding; Sec31 handoff (F004) |
| [15479737](https://pubmed.ncbi.nlm.nih.gov/15479737/) | *COPII-dependent export of CFTR… di-acidic exit code* | DxE exit code binds Sec23/Sec24 (F005) |
| [20946353](https://pubmed.ncbi.nlm.nih.gov/20946353/) | *Receptor-mediated ER export of human MHC class I… C-terminal single amino acid* | C-terminal Val/Ala signal binds Sec23/24 (F005) |
| [21822286](https://pubmed.ncbi.nlm.nih.gov/21822286/) | *Direct targeting of Sec23a by miR-200s influences cancer cell secretome…* | miR-200 directly represses Sec23a; controls secretion of Igfbp4/Tinagl1 (F006) |
| [24135722](https://pubmed.ncbi.nlm.nih.gov/24135722/) | *miR-200 family in HCC with bile duct tumor thrombus* | Independent support for miR-200 → Sec23a-mediated secretome → IGFBP4 axis (F006) |
| [35441598](https://pubmed.ncbi.nlm.nih.gov/35441598/) | *The congenital dyserythropoietic anemias: genetics and pathophysiology* | SEC23A/SEC23B functional overlap; SEC23A overexpression rescues CDAII (F008) |
| [34818036](https://pubmed.ncbi.nlm.nih.gov/34818036/) | *SEC23A rescues SEC23B-deficient congenital dyserythropoietic anemia type II* | Direct experimental interchangeability of paralogs (F008) |
| [24076263](https://pubmed.ncbi.nlm.nih.gov/24076263/) | *Exiting the ER: what we know and what we don't* | COPII is the obligatory ER-export machinery for most secreted/membrane proteins (F009) |
| [20679433](https://pubmed.ncbi.nlm.nih.gov/20679433/) | *p125A … mammalian Sec13/Sec31 COPII subcomplex* | Sec23A-interacting p125A; sequential COPII recruitment; ERES organization (F002) |
| [17428803](https://pubmed.ncbi.nlm.nih.gov/17428803/) | *Mammalian Sec16/p250 plays a role in membrane traffic from the ER* | Sec23-binding Sec16 builds ER exit sites (context for F002) |
| [15580264](https://pubmed.ncbi.nlm.nih.gov/15580264/) | *Coupling of ER exit to microtubules through direct interaction of COPII with dynactin* | Sec23 binds p150Glued/dynactin, linking carriers to microtubule transport (context) |
| [23349870](https://pubmed.ncbi.nlm.nih.gov/23349870/) | *CK2 phosphorylates Sec31 and regulates ER-to-Golgi trafficking* | Sec31 phosphorylation modulates its Sec23 affinity and coat duration (context) |

Supporting SEC23B-focused studies ([PMID: 34954140](https://pubmed.ncbi.nlm.nih.gov/34954140/), [PMID: 35163229](https://pubmed.ncbi.nlm.nih.gov/35163229/), [PMID: 41880517](https://pubmed.ncbi.nlm.nih.gov/41880517/)) further characterize the paralog and reinforce the tissue-specificity interpretation underlying Finding 8.

---

## Limitations and Knowledge Gaps

1. **Reliance on yeast and orthologous structures.** The definitive atomic-level mechanism (arginine-finger GAP activity, bow-tie fold, membrane-proximal surface) derives from the *yeast* Sec23/24–Sar1 structure ([PMID: 12239560](https://pubmed.ncbi.nlm.nih.gov/12239560/)). While the family/subfamily assignment and domain architecture of human SEC23A (Q15436) are strongly conserved, a high-resolution human SEC23A–Sar1 structure with human-specific GAP kinetics is not detailed in the evidence reviewed here.

2. **SEC24 paralog pairing is underspecified.** Humans have multiple SEC24 paralogs (SEC24A–D), each with distinct cargo-signal preferences. Which SEC24 partner(s) SEC23A preferentially pairs with for specific cargo (e.g., procollagen vs. CFTR vs. MHC-I) was not resolved in this investigation and is an important determinant of substrate specificity.

3. **Cargo breadth is sampled, not comprehensive.** Exit-code evidence covers CFTR (DxE) and MHC-I (C-terminal Val/Ala), but the complete repertoire of human cargo that strictly depends on SEC23A (versus SEC23B) is not enumerated. The collagen dependence is well established; dependence of other bulky cargoes (e.g., chylomicrons / pre-chylomicron transport) was not directly examined here.

4. **Regulation beyond miR-200.** Post-translational regulation of SEC23A itself (phosphorylation, ubiquitination) was not characterized here, although Sec31 phosphorylation by CK2 ([PMID: 23349870](https://pubmed.ncbi.nlm.nih.gov/23349870/)) hints that the broader coat is kinase-regulated. Whether SEC23A is directly phosphoregulated remains open.

5. **Quantitative GAP kinetics and SEC31 stimulation.** The degree to which outer-coat SEC31 stimulates human SEC23A GAP activity, and how CLSD mutations quantitatively alter this, were inferred from coupling/recruitment phenotypes rather than from direct enzymatic rate measurements in the human system.

6. **Analysis was literature-based.** No primary experimental dataset was supplied for this target; all findings rest on published structural, genetic, and cell-biological studies. The strength of the conclusions therefore reflects convergent prior literature rather than new primary data generated in this investigation.

---

## Proposed Follow-up Experiments / Actions

1. **Human SEC23A–Sar1–SEC24 structure and GAP kinetics.** Determine a cryo-EM/crystal structure of the human pre-budding complex and measure Sar1 GTP-hydrolysis rates with and without SEC31, comparing wild-type SEC23A to CLSD mutants to quantify the catalytic defect directly.

2. **Map SEC23A–SEC24 paralog pairing by cargo.** Use co-immunoprecipitation and reconstituted budding assays to establish which SEC24 paralog partners with SEC23A for procollagen, CFTR, and MHC-I export, clarifying the combinatorial basis of substrate specificity.

3. **Define the SEC23A-dependent secretome.** Perform quantitative secretomics (mass spectrometry) in isogenic SEC23A knockout vs. rescue cells to build a comprehensive list of cargo whose export is rate-limited by SEC23A, testing whether Igfbp4/Tinagl1 generalize to a broader "SEC23A-sensitive" cargo class.

4. **Dissect the PPP-binding hub.** Mutate the Sec23 PPP-binding surface and measure the competitive handoff between TANGO1/cTAGE5 and SEC31 in real time (e.g., FRET or single-molecule assays) to test the proposed sequential template-to-cage handoff model for large-cargo carriers.

5. **Test SEC23A as a therapeutic lever.** Building on the demonstration that increased SEC23A rescues CDAII ([PMID: 34818036](https://pubmed.ncbi.nlm.nih.gov/34818036/)), evaluate whether pharmacologic or genetic upregulation of SEC23A can compensate for SEC23B deficiency in human erythroid models, and conversely whether SEC23B upregulation mitigates CLSD.

6. **Probe miR-200 → SEC23A in metastasis.** Test whether restoring SEC23A in miR-200-high tumor cells reinstates Igfbp4/Tinagl1 secretion and suppresses metastatic colonization in vivo, validating the SEC23A secretome gate as a candidate anti-metastatic target.

---

## Conclusion

SEC23A (Q15436) is unambiguously the **human Sec23 inner-coat subunit of the COPII vesicle machinery**. Its primary function is dual and tightly coupled: it is the **cargo-selecting inner-coat adaptor** (with SEC24) that concentrates secretory and membrane proteins at ER exit sites, and it is the **Sar1 GTPase-activating protein** that, through an arginine finger, times GTP hydrolysis to coordinate coat assembly, outer-coat (SEC13/SEC31) recruitment, and vesicle budding. It acts on the cytosolic face of the ER, functions within the obligatory COPII anterograde ER-to-Golgi pathway, is especially required for export of bulky cargo such as procollagen (via TANGO1/cTAGE5), and is a regulated secretome gate (miR-200 target) biochemically interchangeable with SEC23B. Loss of function causes cranio-lenticulo-sutural dysplasia. The evidence base — anchored by a definitive pre-budding structure, zebrafish and human genetics, cargo exit-code biochemistry, and paralog-rescue experiments — provides a coherent, mechanistically precise functional annotation.


## Artifacts

- [OpenScientist final report](SEC23A-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](SEC23A-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:12239560
2. PMID:24076263
3. PMID:27551091
4. PMID:17981132
5. PMID:16980978
6. PMID:18713835
7. PMID:21822286
8. PMID:35441598
9. PMID:34818036
10. PMID:20679433
11. PMID:38275611
12. PMID:15479737
13. PMID:20946353
14. PMID:24135722
15. PMID:12408798
16. PMID:34954140
17. PMID:35163229
18. PMID:41880517
19. PMID:23349870