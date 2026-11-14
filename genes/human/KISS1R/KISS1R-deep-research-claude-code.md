---
provider: claude_code
cached: false
start_time: '2026-11-13T21:57:45.730860'
end_time: '2026-11-13T21:59:37.829122'
duration_seconds: 112.1
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: KISS1R
  gene_symbol: KISS1R
  uniprot_accession: Q969F8
  protein_description: 'RecName: Full=KiSS-1 receptor; Short=KiSS-1R; AltName: Full=G
    protein-coupled receptor 54; AltName: Full=G protein-coupled receptor OT7T175;
    Short=hOT7T175; AltName: Full=Hypogonadotropin-1; AltName: Full=Kisspeptins receptor;
    AltName: Full=Metastin receptor;'
  gene_info: Name=KISS1R; Synonyms=AXOR12 {ECO:0000303|PubMed:11387329}, GPR54;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the G protein-coupled receptor 1 family.
  protein_domains: GPCR_Rhodpsn. (IPR000276); GPCR_Rhodpsn_7TM. (IPR017452); KiSS_1_rcpt.
    (IPR008103); 7tm_1 (PF00001)
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
  web_search_requests: 3
  num_turns: 10
  total_cost_usd: 0.7986541
  session_id: 2d977880-5813-4fd4-946d-fc5c03ad3d2c
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  assistant_text_blocks: 2
citation_count: 15
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q969F8
- **Protein Description:** RecName: Full=KiSS-1 receptor; Short=KiSS-1R; AltName: Full=G protein-coupled receptor 54; AltName: Full=G protein-coupled receptor OT7T175; Short=hOT7T175; AltName: Full=Hypogonadotropin-1; AltName: Full=Kisspeptins receptor; AltName: Full=Metastin receptor;
- **Gene Information:** Name=KISS1R; Synonyms=AXOR12 {ECO:0000303|PubMed:11387329}, GPR54;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the G protein-coupled receptor 1 family.
- **Key Domains:** GPCR_Rhodpsn. (IPR000276); GPCR_Rhodpsn_7TM. (IPR017452); KiSS_1_rcpt. (IPR008103); 7tm_1 (PF00001)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "KISS1R" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'KISS1R' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **KISS1R** (gene ID: KISS1R, UniProt: Q969F8) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

Local files are read; now checking recent literature (structures, β-arrestin signaling, cilia) by web search.

# KISS1R (GPR54) in human: a research report for functional annotation

**Target:** UniProtKB Q969F8, KISS1R (also called GPR54, AXOR12 or hOT7T175), *Homo sapiens*. It belongs to G protein-coupled receptor family 1, the rhodopsin-like class A, and carries the InterPro signatures IPR000276, IPR017452 and IPR008103 (the KiSS-1 receptor signature) and the Pfam domain PF00001 (7tm_1).

**Identity check:** The symbol is not ambiguous. The literature on "GPR54", "AXOR12" and "KISS1R" all describes this same receptor for the KISS1-derived peptides. The local cached publications match the UniProt identity: the receptor was cloned from human brain as AXOR12 with 81% homology to rat GPR54, and it responds to KiSS-1 peptides [PMID:11387329].

---

## 1. Summary

KISS1R is a class A, rhodopsin-like seven-transmembrane GPCR in the plasma membrane. Its endogenous ligands are the kisspeptins, peptides cleaved from the KISS1 precursor. The main forms are kisspeptin-54 (also called metastin), -14, -13 and -10. They share a C-terminal RF-amide motif, which is the part the receptor recognises.

- **Primary signalling:** Ligand binding couples the receptor to **Gαq/11**. This activates phospholipase C β (PLCβ), which hydrolyses PIP₂, releases Ca²⁺ and activates PKC and the ERK1/2 and p38 MAP kinases. The receptor also signals through a **β-arrestin-dependent** route that does not need G protein.
- **Physiological role:** Its core role is in the **hypothalamic–pituitary–gonadal (HPG) axis**. KISS1R on GnRH neurons is the receptor through which kisspeptin depolarises those neurons and triggers GnRH release. That GnRH release drives pituitary LH/FSH secretion, and so puberty and fertility.
- **Genetics:** In humans, loss-of-function mutations cause normosmic idiopathic hypogonadotropic hypogonadism (IHH), and a gain-of-function variant causes central precocious puberty.
- **Peripheral roles:** Placental, anti-metastatic and anti-proliferative signalling, and a recently described osteoclast and bone function, are real but secondary.

---

## 2. Molecular function: what the receptor does

### 2.1 Ligand specificity

- **Deorphanisation (2001), by three groups in parallel:**
  - Kotani *et al.* purified 54-, 14- and 13-residue peptides from human placenta. These activated GPR54 and derive from the KiSS-1 metastasis-suppressor gene, so they were named **kisspeptins**. The authors reported "They bound with low nanomolar affinities to rat and human GPR54 expressed in Chinese hamster ovary K1 cells and stimulated PIP(2) hydrolysis, Ca(2+) mobilization, arachidonic acid release, ERK1/2 and p38 MAP kinase phosphorylation, and stress fiber formation but inhibited cell proliferation" [PMID:11457843, *J Biol Chem* 2001].
  - Muir *et al.* found high-potency agonism "indicative of a cognate ligand" from peptides derived from the KiSS-1 gene, all of which share a C-terminal amidated motif [PMID:11387329, *J Biol Chem* 2001].
  - Ohtaki *et al.* independently named the 54-residue peptide "metastin" and showed that it inhibits metastasis through OT7T175, the same receptor (*Nature* 2001;411:613–617).
- **Minimal agonist:** The C-terminal decapeptide, kisspeptin-10 (Kp-10, YNWNSFGLRF-NH₂), is the shortest fully active agonist. The amidated RF motif is required.
- **Classification:** By GO terms this is **neuropeptide receptor activity** (GO:0008188), and more precisely **G protein-coupled peptide receptor activity** for a kisspeptin ligand. The peptide-hormone character of the ligand also fits the more general GPCR activity term (GO:0004930).

### 2.2 G-protein coupling and proximal transduction

- **Gq/11–PLCβ:** This is the canonical axis. It is shown by PIP₂ hydrolysis and Ca²⁺ mobilisation in transfected cells [PMID:11457843].
  - **L148S mutation:** This IHH mutation lies in the second intracellular loop. Wacker *et al.* showed that it "does not affect the expression, ligand binding properties, or protein interaction network of GPR54", yet "diverse GPR54 functional responses are markedly inhibited". This identifies a conserved hydrophobic residue in intracellular loop 2 as critical for G-protein coupling in class A GPCRs [PMID:18772143, *J Biol Chem* 2008, full text available].
  - **Interaction data:** IntAct records direct GNAQ interaction, among others (UniProt Q969F8 INTERACTION section).
- **β-arrestin pathway:**
  - β-arrestins regulate KISS1R desensitisation and internalisation, and they also carry G protein-independent ERK1/2 signalling (Pampillo *et al.* 2009; Szereszewski *et al.* 2010).
  - Ahow *et al.* (Kaiser lab, *Endocrinology* 2014;155:4433) showed that the Gαq/11-uncoupled L148S mutant still activates ERK, and that this activation depends on β-arrestin. In mice lacking β-arrestin-1 or -2, kisspeptin-induced LH secretion was significantly reduced. So the arrestin arm contributes to GnRH and LH output in vivo [Endocrinology article; PMC4197989]. UniProt cites the arrestin–MAPK route as PubMed:25147978.
- **Gi/o coupling:** The PDB entry 8XGO notes that KISS1R can couple to Gi/o as well as Gq/11 [PDBj 8XGO]. This is secondary and context-dependent.
- **SRC/DUSP18 (2024):** In osteoclasts, Kp-10 activation of the receptor recruits the phosphatase DUSP18 and SRC to the KISS1R C-terminus through a Gq-dependent mechanism. DUSP18 then dephosphorylates SRC, which suppresses osteoclast differentiation and bone resorption [PMID:38346942, Li *et al.*, *Nat Commun* 2024, full text available]. Much of the in vivo work was done in mouse. UniProt annotates the human bone function "By similarity" to mouse Q91V45.

### 2.3 Structural evidence (2024)

Two independent cryo-EM studies solved KISS1R–Gq complexes:

- **Shen *et al.*, *Cell Reports* 2024:** Structures with kisspeptin-10 and with the synthetic agonist TAK-448 (PDB 8ZJD at about 3.06 Å; 8ZJE at 3.07 Å). Compared with other Gq-coupled receptors, the intracellular end of TM6 is displaced by about 40°, which gives a distinct interface with Gq [DOAJ record; RCSB 8ZJE].
- **Wu *et al.*, *Science Advances* 2024:** KISS1R–Gq structures with TAK-448 and with full-length KP54 at about 3 Å (PDB 8XGU, 8XGO). The authors propose that differences in the receptor's extracellular and intracellular loops, together with the Gα "wavy hook", determine which G protein it couples to [PDBj 8XGU, 8XGO].

Both studies show the RF-amide C-terminus of the peptide inserted into the orthosteric pocket, with extracellular-loop contacts. This is consistent with the C-terminal decapeptide being enough for full agonism. Because these analyses were seen only as abstracts and database summaries, residue-level claims should be checked against the full text before they are used in annotation.

---

## 3. Cellular localisation

| Location | Evidence |
|---|---|
| **Plasma membrane** (multi-pass) | Direct assay: wild-type and L148S receptors are at the cell surface [PMID:18772143]. UniProt: "Cell membrane {ECO:0000269\|PubMed:18772143}; Multi-pass membrane protein". Reactome lists plasma-membrane reactions (R-HSA-749448, R-HSA-388981). PAINT IBA supports it across the neuropeptide-receptor clade. |
| **Membrane / cell surface** | Antibody work in the original cloning paper [PMID:11387329]. Cell surface is also an electronic annotation. |
| **Primary cilium** | Kiss1r is concentrated in primary cilia of mouse GnRH neurons in vitro and in vivo. Adult GnRH neurons are often multiciliated, and the fraction with several Kiss1r-positive cilia rises over postnatal development. Removing cilia blunts the kisspeptin-induced increase in firing, though migration and puberty still occur (Koemeter-Cox *et al.*, *PNAS* 2014, PMID 24982149, PMC4104922). The human GOA cilium IDA row (PMID:28154160) records ciliary localisation in an experimental system. |
| **Endosomes (transient)** | After agonist exposure, β-arrestin-dependent internalisation moves the receptor into endosomes (Pampillo 2009). This is trafficking, not a site of residence. |

**Functional site:** The receptor acts at the plasma membrane of the GnRH neuron soma and dendrites, and in the cilium. Kisspeptin fibres from the arcuate (ARC/infundibular) and AVPV/preoptic populations contact these neurons. There is also evidence that the receptor acts at GnRH terminals in the median eminence.

---

## 4. Pathways and physiological roles

### 4.1 Core role: the GnRH neuron, the HPG axis and puberty

- **Human genetics:**
  - **Seminara *et al.* (*NEJM* 2003):** In a consanguineous family with IHH, affected members were homozygous for a loss-of-function GPR54 mutation. *Gpr54*-deficient mice had the same phenotype. Both patients and mice still responded to exogenous GnRH. This places the defect upstream of the GnRH receptor, in the control of GnRH secretion [PMID:14573733].
  - **de Roux *et al.* (*PNAS* 2003):** An independent report of GPR54 loss-of-function in IHH [PMID:12944565].
  - **Semple *et al.* (2005):** A compound heterozygous patient carried C223R in TM5, which had "profoundly impaired signaling", and R297L in extracellular loop 3, which showed a mild reduction in signalling [PMID:15598687].
  - **Teles *et al.* (*NEJM* 2008):** The **R386P** C-terminal variant causes central precocious puberty. The mechanism is prolonged signalling from reduced desensitisation and degradation, not constitutive activity [PMID:18272894].
- **Mechanism in the GnRH neuron:**
  - Kisspeptin depolarises GnRH neurons and causes sustained firing, partly by inhibiting inward-rectifier K⁺ channels and activating TRPC-like non-selective cation channels downstream of Gq–PLC. UniProt annotates this "By similarity", mainly from rodent electrophysiology.
  - Kisspeptin is among the most potent known stimulators of GnRH and LH release in rodents, primates and humans. Messager *et al.* (*PNAS* 2005) showed in *Gpr54*⁻/⁻ mice that it acts directly through the receptor on GnRH neurons.
- **GO view:** These data support "positive regulation of gonadotropin secretion" (GO:0032278; human IMP from PMID:14573733 and PMID:15598687). They also support regulation of membrane depolarisation and of cation transmembrane transport through the K⁺ and TRPC mechanisms. Strictly, the receptor's own function is the GPCR activity and the PLC-activating signalling pathway (GO:0007200, IDA PMID:11457843). Effects on gonadotropin secretion are downstream regulation.
- **Further roles:** KISS1R also mediates feedback by sex steroids on GnRH secretion, through steroid-sensitive kisspeptin neurons upstream of it. In the ARC KNDy neurons (kisspeptin/neurokinin B/dynorphin), it is part of the GnRH pulse generator, while the AVPV population drives the preovulatory surge. In these circuits KISS1R is the **output receptor** on GnRH neurons. It is not the pacemaker.

### 4.2 Secondary or peripheral roles

- **Placenta and trophoblast:** The receptor is highly expressed in placenta [PMID:11457843; PMID:11387329]. Kisspeptin–KISS1R signalling limits trophoblast invasion. Expression is higher in early than in term placenta, and lower in choriocarcinoma cells (UniProt TISSUE SPECIFICITY).
- **Metastasis suppression, migration and proliferation:**
  - The receptor inhibits cell proliferation and induces stress fibres in CHO cells [PMID:11457843].
  - Ohtaki *et al.* 2001 showed that metastin suppresses metastasis.
  - In some carcinomas (breast) the effect is context-dependent and can even be pro-invasive.
- **Endocrine and other:**
  - Kisspeptin stimulates oxytocin secretion in rats [PMID:11457843].
  - KISS1R is expressed in pancreatic islets, where it may modulate insulin secretion, and in brain regions outside the hypothalamus, such as the amygdala and hippocampus.
- **Bone:** Kp-10 acting on the receptor in osteoclasts recruits DUSP18 and SRC, which suppresses osteoclastogenesis and bone resorption [PMID:38346942]. This is the source of the ISS rows for negative regulation of osteoclast differentiation and bone resorption. The underlying data are mainly from mouse.

---

## 5. Evolution and bioinformatics

- **Family:** KISS1R is in the rhodopsin-like (class A) GPCR family, PF00001 7tm_1. Its closest relatives are the RF-amide and galanin-like peptide receptors (the galanin/allatostatin-like branch). The PAINT IBA for plasma membrane draws on neuropeptide receptors from fly and nematode, which suggests that peptide-receptor activity and plasma-membrane location are ancestral to the clade. The IBA rows for neuropeptide receptor activity and the neuropeptide signalling pathway (GO:0008188, GO:0007218) fit this.
- **Conservation:** The receptor is conserved across vertebrates. Fish and amphibians have several paralogues (Kiss2r, Kiss3r), and some lineages, such as birds, have lost the kisspeptin system. In non-mammals its role in reproduction is less absolute than in mammals.
- **Features:** Seven transmembrane helices, the conserved DRY/NPxxY motifs typical of class A receptors, a hydrophobic residue in intracellular loop 2 needed for coupling (L148), and a long C-terminal tail with desensitisation and degradation determinants (R386).
- **Accessory proteins:** IntAct records interactions with RAMP1, RAMP2 and RAMP3, and with PPP2CA (UniProt INTERACTION). Their functional significance is unknown.

---

## 6. Implications for GO annotation

**Core molecular function**
- G protein-coupled (neuro)peptide receptor activity for kisspeptins (GO:0008188 / GO:0008528 / GO:0004930) [PMID:11457843; PMID:11387329; PMID:18772143].

**Core process**
- Phospholipase C-activating GPCR signalling pathway (GO:0007200) [PMID:11457843; PMID:18772143].
- Positive regulation of gonadotropin secretion (GO:0032278), from human genetics [PMID:14573733; PMID:15598687].
- The neuropeptide signalling pathway (GO:0007218) is appropriate.

**Core location**
- Plasma membrane [PMID:18772143].
- Primary cilium (GnRH neurons; PMID 24982149, and the GOA row from PMID:28154160).

**Secondary, non-core**
- Negative regulation of osteoclast differentiation and bone resorption [PMID:38346942; data mainly mouse].
- Regulation and positive regulation of membrane depolarisation, and of cation transmembrane transport (mechanism shown in rodent GnRH neurons).
- Placental and anti-metastatic effects.

**Likely uninformative or questionable**
- Bare "protein binding" (GO:0005515) IPI rows.
- "Molecular adaptor activity" (GO:0060090, IEA). The scaffolding of DUSP18 and SRC is an activation-dependent recruitment, not a dedicated adaptor function.
- "Regulation of transport" (GO:0051049, IEA). This is very general.

**Open questions**
1. How much do Gq/11 and β-arrestin each contribute to GnRH release in humans?
2. Is the Gi/o coupling seen structurally physiologically relevant?
3. What do the RAMP interactions do?
4. Does KISS1R act directly in human bone and islets?

---

## Sources

**Primary literature (cached locally under `publications/`)**
- Muir AI *et al.* (2001) AXOR12, a novel human G protein-coupled receptor, activated by the peptide KiSS-1. *J Biol Chem* 276:28969. PMID:11387329, doi:10.1074/jbc.M102743200
- Kotani M *et al.* (2001) The metastasis suppressor gene KiSS-1 encodes kisspeptins, the natural ligands of the orphan GPCR GPR54. *J Biol Chem* 276:34631. PMID:11457843, doi:10.1074/jbc.M104847200
- Seminara SB *et al.* (2003) The GPR54 gene as a regulator of puberty. *N Engl J Med* 349:1614. PMID:14573733
- Semple RK *et al.* (2005) Two novel missense mutations in GPR54 in a patient with hypogonadotropic hypogonadism. *J Clin Endocrinol Metab* 90:1849. PMID:15598687
- Wacker JL *et al.* (2008) Disease-causing mutation in GPR54 reveals the importance of the second intracellular loop for class A GPCR function. *J Biol Chem* 283:31068. PMID:18772143, PMC2576551
- Li Z *et al.* (2024) Kisspeptin-10 binding to Gpr54 in osteoclasts prevents bone loss by activating Dusp18-mediated dephosphorylation of Src. *Nat Commun* 15:1300. PMID:38346942, PMC10861593

**Cited from the UniProt Q969F8 record, not read here**
- de Roux N *et al.* (2003) *PNAS*. PMID:12944565
- Teles MG *et al.* (2008) *NEJM*, R386P activating variant. PMID:18272894
- β-arrestin–MAPK signalling. PubMed:25147978

**Web sources**
- Ahow M *et al.* (2014) KISS1R signals independently of Gαq/11 and triggers LH secretion via the β-arrestin pathway in the male mouse. *Endocrinology* 155:4433. [PMC4197989](https://pmc.ncbi.nlm.nih.gov/articles/PMC4197989), [journal page](https://dbpia.nl.go.kr/endo/article/155/11/4433/2422694), [OUCI](https://ouci.dntb.gov.ua/works/4YPPNeQ7), [ICN 2014 abstract](https://icn-2014.p.asnevents.com.au/days/2014-08-18/abstract/13614)
- Koemeter-Cox AI *et al.* (2014) Primary cilia enhance kisspeptin receptor signaling on GnRH neurons. *PNAS*. [PubMed 24982149](https://www.pubmed.gov/24982149/), [PMC4104922](https://pmc.ncbi.nlm.nih.gov/articles/PMC4104922), [IU ScholarWorks](https://scholarworks.indianapolis.iu.edu/items/60987791-e324-437c-be64-d8d5045904c8)
- Shen *et al.* (2024) KISS1R–Gq cryo-EM structures, *Cell Reports*. [DOAJ](https://doaj.org/article/9c255df8d34046729b6af43aebba673c), [RCSB 8ZJE](https://rcsb.org/structure/8ZJE), [PDBj 8ZJD](https://pdbj.org/mine/summary/8zjd)
- Wu *et al.* (2024) KISS1R–Gq structures with KP54 and TAK-448, *Science Advances*. [PDBj 8XGU](https://pdbj.org/mine/summary/8xgu), [PDBj 8XGS](https://pdbj.org/mine/summary/8xgs), [8XGO summary](https://ibdc.dbtindia.gov.in/isda/summary/8XGO), [EMDB 38332](https://pdbj.org/emnavi/emnavi_detail.php?id=38332)
- [BU OpenBU thesis: KISS1R signalling and gain/loss-of-function mutations](https://open.bu.edu/items/62194549-cc34-4122-914b-e0334136273b)

**Cited from memory, not re-checked in this session**
- Ohtaki T *et al.* (2001) *Nature* 411:613–617
- Messager S *et al.* (2005) *PNAS*
- Pampillo M *et al.* (2009) β-arrestin regulation of KISS1R
- Szereszewski JM *et al.* (2010)

**Databases**
- UniProtKB Q969F8 (local copy `genes/human/KISS1R/KISS1R-uniprot.txt`)
- QuickGO GOA annotations (`genes/human/KISS1R/KISS1R-goa.tsv`)
- Reactome R-HSA-749448, R-HSA-388981

## Citations

1. https://pmc.ncbi.nlm.nih.gov/articles/PMC4197989
2. https://dbpia.nl.go.kr/endo/article/155/11/4433/2422694
3. https://ouci.dntb.gov.ua/works/4YPPNeQ7
4. https://icn-2014.p.asnevents.com.au/days/2014-08-18/abstract/13614
5. https://www.pubmed.gov/24982149/
6. https://pmc.ncbi.nlm.nih.gov/articles/PMC4104922
7. https://scholarworks.indianapolis.iu.edu/items/60987791-e324-437c-be64-d8d5045904c8
8. https://doaj.org/article/9c255df8d34046729b6af43aebba673c
9. https://rcsb.org/structure/8ZJE
10. https://pdbj.org/mine/summary/8zjd
11. https://pdbj.org/mine/summary/8xgu
12. https://pdbj.org/mine/summary/8xgs
13. https://ibdc.dbtindia.gov.in/isda/summary/8XGO
14. https://pdbj.org/emnavi/emnavi_detail.php?id=38332
15. https://open.bu.edu/items/62194549-cc34-4122-914b-e0334136273b