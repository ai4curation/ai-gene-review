---
provider: claude_code
cached: false
start_time: '2026-11-13T21:57:22.056516'
end_time: '2026-11-13T21:59:21.996066'
duration_seconds: 119.94
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: FSHR
  gene_symbol: FSHR
  uniprot_accession: P23945
  protein_description: 'RecName: Full=Follicle-stimulating hormone receptor; Short=FSH-R;
    AltName: Full=Follitropin receptor; Flags: Precursor;'
  gene_info: Name=FSHR; Synonyms=LGR1;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the G protein-coupled receptor 1 family.
  protein_domains: FSH_rcpt. (IPR002272); GnHR_TM. (IPR024635); GPCR_Rhodpsn. (IPR000276);
    GPCR_Rhodpsn_7TM. (IPR017452); Gphrmn_rcpt_fam. (IPR002131)
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
  web_search_requests: 7
  num_turns: 10
  total_cost_usd: 0.7668965000000001
  session_id: 110e7141-4734-46c5-8982-8e407cbbec7a
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 20
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P23945
- **Protein Description:** RecName: Full=Follicle-stimulating hormone receptor; Short=FSH-R; AltName: Full=Follitropin receptor; Flags: Precursor;
- **Gene Information:** Name=FSHR; Synonyms=LGR1;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the G protein-coupled receptor 1 family.
- **Key Domains:** FSH_rcpt. (IPR002272); GnHR_TM. (IPR024635); GPCR_Rhodpsn. (IPR000276); GPCR_Rhodpsn_7TM. (IPR017452); Gphrmn_rcpt_fam. (IPR002131)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "FSHR" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'FSHR' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **FSHR** (gene ID: FSHR, UniProt: P23945) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# FSHR (human follicle-stimulating hormone receptor, UniProt P23945): research report

## 0. Identity check

- The symbol FSHR (synonym LGR1) matches UniProt P23945, "Follicle-stimulating hormone receptor", in *Homo sapiens*. UniProt places it in the GPCR family 1 (rhodopsin-like), FSH/LSH/TSH subfamily. The InterPro domains fit: FSH_rcpt (IPR002272), Gphrmn_rcpt_fam (IPR002131), GnHR_TM (IPR024635) and GPCR_Rhodpsn_7TM (IPR017452).
- Every source used below concerns the glycoprotein-hormone receptor that FSH (CGA/FSHB) activates. None concerns an unrelated gene with a similar symbol.
- Some citations are taken from the local UniProt record (`genes/human/FSHR/FSHR-uniprot.txt`) and from the literature summaries returned by my searches. PMIDs written without a URL are noted as from the UniProt record or from memory and should be checked against PubMed before they are used as `VERIFIED`.

---

## 1. Summary

FSHR is a class A G protein-coupled receptor with a large leucine-rich-repeat ectodomain. It sits in the plasma membrane of ovarian granulosa cells and testicular Sertoli cells.

- **Primary function:** it is the high-affinity, ligand-selective receptor for the pituitary glycoprotein hormone follitropin (FSH), a heterodimer of CGA and FSHB.
- **Main signalling route:** hormone binding to the ectodomain activates the 7-transmembrane domain. This mainly couples to Gαs, which activates adenylyl cyclase and raises cAMP, which activates PKA and CREB.
- **Effects in the ovary:** follicle growth past the antral stage, aromatase (CYP19A1) induction and estradiol synthesis, and induction of the LH receptor in granulosa cells.
- **Effects in the testis:** Sertoli-cell support of spermatogenesis.
- **Secondary signalling:** PI3K/AKT/mTOR (partly through the adaptors APPL1 and 14-3-3τ), β-arrestin-dependent ERK1/2, and context-dependent Gαq or Gαi coupling.
- **Human genetics:** loss of function causes hypergonadotropic ovarian dysgenesis (ODG1). Gain of function or loss of selectivity causes spontaneous ovarian hyperstimulation syndrome (OHSS).
- **Extragonadal roles** (bone, fat, liver, β-cells, endothelium) have been reported but remain disputed.

---

## 2. Molecular function: receptor for a glycoprotein hormone

### 2.1 Ligand and its specificity

- **Ligand.** FSHR is the receptor for FSH. UniProt's function summary: "G protein-coupled receptor for follitropin, the follicle-stimulating hormone… Mediates FSH signaling through cAMP/protein kinase A (PKA) and phosphatidylinositol-3 kinase (PI3K)/protein kinase B (AKT) pathways to regulate ovarian follicular development and steroidogenesis" (UniProt P23945, citing PMID:11847099, PMID:24058690, PMID:24692546).
- **Specificity is in the ectodomain.**
  - FSH, LH/hCG and TSH share the same α subunit (CGA). Which receptor they bind is set by the hormone-specific β subunit, which contacts the concave LRR surface of the receptor ectodomain.
  - Fan & Hendrickson (2005, *Nature* 433:269; PDB 1XWD; PMID from memory, about 15662415) solved FSH bound to the FSHR hormone-binding domain. Both hormone subunits bind the concave face of the curved LRR domain in a "hand-clasp" arrangement.
- **Loss of specificity causes disease.** Mutations in the transmembrane domain that let hCG or TSH activate FSHR cause spontaneous OHSS during pregnancy (Smits et al. 2003, *NEJM*; Vassart et al. 2003, *NEJM*; PMID:12930927 and PMID:12930928 in the UniProt record).

### 2.2 How hormone binding activates the receptor

**Ectodomain and hinge (Jiang et al. 2012, *PNAS*; PDB 4AY9; [PMC/PMID 22802634](https://pmc.ncbi.nlm.nih.gov/articles/pmid/22802634)):**
- The 2.5 Å crystal structure of FSH bound to the entire FSHR extracellular domain shows that the hinge region "does not form a separate structural unit but is an integral part of FSHRED" ([RCSB 4AY9](https://www.rcsb.org/structure/4AY9); [Proteopedia](https://proteopedia.org/w/4ay9)).
- The authors propose a two-step mechanism:
  1. FSH binds the high-affinity hormone-binding subdomain, and this reshapes the hormone to form a pocket for a sulfotyrosine (sTyr).
  2. The receptor then inserts sulfated Tyr335 of the hinge into that pocket, which leads to activation.
- UniProt records tyrosine sulfation as a PTM (PMID:11847099). The crystal packs as a trimer, and UniProt lists the receptor as a homotrimer (PMID:24692546, PMID:36720854).

**Full-length receptor (Duan et al. 2023, *Nat Commun* 14:519; [DOI 10.1038/s41467-023-36170-3](https://www.nature.com/articles/s41467-023-36170-3.pdf); PDB [8I2G](https://www.rcsb.org/structure/8i2g)):**
- The team solved cryo-EM structures of inactive FSHR and of active FSHR bound to FSH, the allosteric agonist compound 21f and the Gs heterotrimer (2.8 Å).
- The authors conclude that FSHR's activation mechanism is conserved with the other glycoprotein hormone receptors (LHCGR, TSHR). The bound hormone pushes the ectodomain upright relative to the membrane, the conformational change passes through the hinge and extracellular loops to the 7TM bundle, and the bundle engages Gαs.
- Compound 21f binds inside the transmembrane domain and activates the receptor directly ([Nat Commun](https://www.nature.com/articles/s41467-023-36170-3.pdf); [DOAJ](https://doaj.org/article/856683e70c7b4674b3561a58992980ab)).
- This structure provides direct physical evidence that FSHR is a Gs-coupled receptor. UniProt lists an interaction with GNAS (PMID:36720854).

**Glycosylation.** The receptor's N-glycosylation is indirectly needed for high-affinity FSH binding (UniProt, by similarity to rat P20395).

### 2.3 Domain architecture (from UniProt and the structures)

| Region | Role |
|---|---|
| Signal peptide | ER targeting; the receptor is a plasma-membrane protein |
| LRR ectodomain (hormone-binding subdomain) | Binds the FSH αβ heterodimer and sets hormone specificity |
| Hinge (signal-specificity subdomain) with sulfo-Tyr335 | Senses the bound hormone and couples it to activation |
| 7TM (GPCR_Rhodpsn_7TM) | Engages Gαs (and Gαq, Gαi), GRKs and β-arrestins |
| Intracellular loops and C-tail | Bind the adaptors APPL1/APPL2 and 14-3-3τ; phosphorylation sites for desensitization |

There are four splice isoforms (UniProt). The long R1 form is canonical. Alternative forms such as E9Del (short) and E6Del lack transmembrane exons and are unlikely to signal.

---

## 3. Signalling pathways

### 3.1 Canonical Gαs, cAMP, PKA and CREB

- The dominant pathway in granulosa and Sertoli cells is Gαs activation, which stimulates adenylyl cyclase, raises cAMP and activates PKA (and EPAC).
- PKA phosphorylates CREB, which turns on FSH target genes. In granulosa cells these include CYP19A1 (aromatase), LHCGR, INHA, STAR and CCND2.
- Reviews state: "FSH/FSHR stimulates estrogen production in granulosa cells by inducing aromatase expression in a Gαs/cAMP/PKA-dependent manner" ([Casarini & Crépieux 2019, *Front Endocrinol*](https://www.frontiersin.org/articles/10.3389/fendo.2019.00305/full); [PMC6527893](https://pmc.ncbi.nlm.nih.gov/articles/PMC6527893)).

### 3.2 PI3K, AKT and mTOR

- FSH activates AKT and SGK in granulosa cells. PKA cross-talks with AKT to activate mTOR and p70S6K, which drives mRNA translation and granulosa-cell proliferation. ERK-mediated phosphorylation of tuberin is part of this route ([Casarini & Crépieux 2019](https://www.frontiersin.org/articles/10.3389/fendo.2019.00305/full); [Hunzicker-Dunn & Maizels-type review PMC2946492](https://pmc.ncbi.nlm.nih.gov/articles/PMC2946492)).
- A 2024 review of FSH–IGF cross-talk notes that AKT, with FOXO and HIF1α downstream, is a key intracellular target of FSHR in granulosa cells. It also argues that FSH needs IGF1R signalling to activate AKT fully ([PMC10988955](https://pmc.ncbi.nlm.nih.gov/articles/PMC10988955)).

### 3.3 Adaptor proteins that bind the receptor directly

- **APPL1.** A yeast two-hybrid screen of an ovarian cDNA library against FSHR intracellular loops 1 and 2 found APPL1. APPL1 co-immunoprecipitates with FSHR in HEK293 cells, which suggests it links FSHR to PI3K/AKT (Nechamen et al. 2004, *Biol Reprod* 71:629; [BioOne](https://bioone.org/journals/biology-of-reproduction/volume-71/issue-2/biolreprod.103.025833/Human-Follicle-Stimulating-Hormone-FSH-Receptor-Interacts-with-the-Adaptor/10.1095/biolreprod.103.025833.full); [BioGRID](https://thebiogrid.org/62967/publication/human-follicle-stimulating-hormone-fsh-receptor-interacts-with-the-adaptor-protein-appl1-in-hek-293-cells-potential-involvement-of-the-pi3k-pathway-in-fsh-signaling.html)).
- **APPL2.** UniProt also lists APPL2, which binds FSHR whether or not FSH is present (PMID:17030088).
- **Endosomal signalling.** APPL1 marks very early endosomes. The adaptor GIPC routes internalized FSHR to these compartments and so sustains MAPK signalling, which gives the signal a spatial dimension ([Casarini & Crépieux 2019](https://www.frontiersin.org/articles/10.3389/fendo.2019.00305/full)).
- **14-3-3τ (YWHAQ).** It binds FSHR at a site that overlaps the canonical G protein-binding site and promotes AKT activation ([Landomiel et al. 2019, *Front Endocrinol*](https://www.frontiersin.org/journals/endocrinology/articles/10.3389/fendo.2019.00148/full); [PMC6425863](https://pmc.ncbi.nlm.nih.gov/articles/PMC6425863)). IntAct records YWHAQ–FSHR in 4 experiments (UniProt).

### 3.4 β-arrestins, GRKs and biased signalling

- FSHR recruits β-arrestin 1 and 2 after phosphorylation by GRKs. UniProt lists ARRB2 by similarity to rat.
- ERK1/2 activated through G proteins is fast and transient. ERK1/2 activated through β-arrestins starts more slowly (about 5–10 min to peak) but lasts longer (half-life over 1 h).
- GRK5 and GRK6 favour β-arrestin-dependent ERK activation, while GRK2 and GRK3 inhibit it ([Landomiel et al. 2019](https://www.frontiersin.org/journals/endocrinology/articles/10.3389/fendo.2019.00148/full); [arXiv 1808.01965, "FSHR: Advances and remaining challenges"](https://arxiv.org/pdf/1808.01965)).
- **Biased ligands.** Different FSH glycoforms (hypoglycosylated FSH21/18 versus fully glycosylated FSH24) and small-molecule allosteric modulators push FSHR towards different pathways. This underlies efforts to design biased FSHR drugs ([Landomiel et al. 2019](https://www.frontiersin.org/journals/endocrinology/articles/10.3389/fendo.2019.00148/full)).

### 3.5 Non-canonical G proteins

- **Gαq/11:** this couples to PLC and Ca²⁺. Coupling is reported to be weaker for human than for rodent FSHR.
- **Gαi:** this has been reported mainly in Sertoli cells and osteoclasts. It leads to MEK/ERK, NF-κB and AKT activation ([Casarini & Crépieux 2019](https://www.frontiersin.org/articles/10.3389/fendo.2019.00305/full)).
- These couplings are much less well established than Gαs, and most of the evidence comes from heterologous or rodent systems.

---

## 4. Where FSHR acts

- **Inside the cell:** FSHR acts at the plasma membrane (UniProt CC: "Cell membrane… Multi-pass membrane protein", PMID:11847099, PMID:24692546). After agonist binding it is internalized and signals from very early (APPL1-positive) endosomes before it recycles or is degraded ([Casarini & Crépieux 2019](https://www.frontiersin.org/articles/10.3389/fendo.2019.00305/full)). The hormone binds on the extracellular face of the receptor. G proteins and adaptors engage the cytoplasmic face.
- **Cell types (well established):** granulosa cells of ovarian follicles and Sertoli cells of the testis (UniProt tissue specificity).
- **Extragonadal expression (disputed):**
  - FSHR has been reported on osteoclasts. Sun et al. (2006, *Cell* 125:247) showed that ovariectomized *Fshr*-null mice are protected from bone loss. They proposed direct, estrogen-independent stimulation of osteoclasts by FSH through Gαi, followed by MEK/ERK, NF-κB and AKT. UniProt includes this by similarity to mouse.
  - Expression has also been reported in adipocytes (suppressing UCP1 and thermogenesis), pancreatic β-cells (a bell-shaped effect on insulin secretion), hepatocytes (lowering LDLR and raising LDL-C; PMID:26583582) and tumour endothelium.
  - Chrusciel et al. (2019, [*Front Endocrinol* "Extragonadal FSHR Expression and Function—Is It Real?"](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6369633/)) review these claims critically. They point to reliance on poorly validated antibodies, protein signals that do not match the very low or absent transcript levels, and supraphysiological FSH doses in vitro. An Endocrinology mini-review likewise says the field is controversial ([*Endocrinology* 159:2](https://academic.oup.com/endo/article/159/1/2/4725019)).
  - **Conclusion:** treat the extragonadal roles as non-core and uncertain.

---

## 5. Physiological role, with genetic evidence

### Ovary
- FSHR is needed for follicles to grow beyond the preantral or early antral stage, and for granulosa-cell proliferation, aromatization and selection of the dominant follicle.
- **Human loss of function:** Aittomäki et al. (1995, *Cell* 82:959; PMID:7553856) mapped hypergonadotropic ovarian dysgenesis in Finnish families to 2p. They found the homozygous FSHR mutation A189V, which segregates with the disease. In transfected cells it greatly reduces binding capacity and signalling without changing ligand affinity, consistent with poor delivery of the receptor to the cell surface ([DrugBank record](https://drugbank.ca/articles/A54202)). This disease is ODG1 (MIM:233300).

### Testis
- **Human:** men homozygous for A189V have variable spermatogenic failure, but not uniform azoospermia or absolute infertility (Tapanainen et al. 1997, *Nat Genet* 15:205; [PDF](https://www.nature.com/articles/ng0297-205.pdf)). In males, FSHR supports Sertoli-cell number and spermatogenic efficiency, but intratesticular testosterone can partly make up for its loss.
- **Mouse:** *Fshr*-knockout mice (Dierich et al. 1998, *PNAS*; [PMC24867](https://pmc.ncbi.nlm.nih.gov/articles/PMC24867)) reproduce the picture.
  - Females: infertile, with small ovaries, follicles arrested before the antral stage, and low estrogen.
  - Males: fertile but with smaller testes and lower sperm output.
  - Together these establish a requirement that is conserved between species.

### Gain of function
- Activating or promiscuity-causing FSHR variants cause spontaneous OHSS (MIM:608115; Smits 2003, Vassart 2003; PMID:12930927, 12930928, 24058690).
- Common polymorphisms (N680S, and −29G>A in the promoter) change how women respond to exogenous FSH during IVF stimulation.

---

## 6. Evolution and structural inference

- FSHR is one of three vertebrate glycoprotein hormone receptors (with LHCGR and TSHR). They form LGR subfamily A of the rhodopsin-like GPCRs: an N-terminal LRR ectodomain, a hinge (signal-specificity subdomain) and a 7TM domain.
- The conserved architecture and the shared Gs-coupling interface explain why the cryo-EM work points to an activation mechanism common to the whole subfamily ([Duan et al. 2023](https://www.nature.com/articles/s41467-023-36170-3.pdf)).
- Orthologs across vertebrates (fish to mammals) keep the hormone-binding LRR and the hinge sulfotyrosine motif. This argues that FSHR's role as the FSH receptor, coupled to cAMP, is an ancestral vertebrate function.

---

## 7. Applications and recent developments

- **Therapeutic target:** recombinant FSH and long-acting FSH analogues for controlled ovarian stimulation. The orthosteric site is the target.
- **Small-molecule allosteric agonists:** thienopyrimidines, dihydropyrazoles and the "compound 21f" class. These are potential oral IVF drugs, and the 2023 cryo-EM structure now defines how they bind ([Duan 2023](https://www.nature.com/articles/s41467-023-36170-3.pdf)).
- **Negative allosteric modulators and FSH-blocking antibodies:** under exploration as contraceptives and, more speculatively, for postmenopausal bone loss and obesity. That second use depends on the disputed extragonadal biology.

---

## 8. Implications for GO annotation

| Aspect | Well-supported core terms | Non-core or caution |
|---|---|---|
| MF | follicle-stimulating hormone receptor activity (GO:0004963); hormone binding / FSH binding; G protein-coupled peptide receptor activity (parent) | Bare protein binding (RAMP1-3, YWHAQ IntAct hits) is uninformative. "Coreceptor" or "transmembrane signaling" terms are too general. |
| BP | follicle-stimulating hormone signaling pathway (GO:0042699); adenylate cyclase-activating GPCR signaling pathway; ovarian follicle development; Sertoli-cell-mediated spermatogenesis | Bone resorption, osteoclast differentiation, insulin-secretion regulation, adipose thermogenesis, cholesterol metabolism (extragonadal claims that are disputed or rest on rodent data). Downstream pleiotropic processes such as "female gonad development". |
| CC | plasma membrane (GO:0005886, IDA); endosome (early or very early, signalling) | ER or Golgi rows would reflect biosynthetic transit only. |
| Complex | homotrimeric receptor (structural), FSHR–Gs complex | — |

---

## 9. Open questions

1. Is the FSHR trimer seen in the ectodomain crystal needed for signalling in vivo, and how does trimerization shape bias towards Gαs or β-arrestin?
2. How much does endosomal FSHR signalling (APPL1/GIPC compartments) contribute, relative to signalling at the plasma membrane, in native human granulosa cells?
3. Is FSHR expressed physiologically outside the gonads (osteoclasts, adipocytes, hepatocytes)? This needs validated, antibody-independent methods such as single-cell RNA-seq, knock-in reporters and cell-type-specific knockouts.
4. Does Gαi or Gαq coupling happen at physiological FSH levels in human cells?

---

## Sources

- UniProt P23945 (local copy: `genes/human/FSHR/FSHR-uniprot.txt`), FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, PTM and DISEASE sections.
- Duan J. et al. 2023, *Nat Commun* 14:519: [nature.com PDF](https://www.nature.com/articles/s41467-023-36170-3.pdf); [DOAJ](https://doaj.org/article/856683e70c7b4674b3561a58992980ab); [PDB 8I2G](https://www.rcsb.org/structure/8i2g)
- Jiang X. et al. 2012, *PNAS*, FSH–FSHR ectodomain structure: [PMC (PMID 22802634)](https://pmc.ncbi.nlm.nih.gov/articles/pmid/22802634); [PDB 4AY9](https://www.rcsb.org/structure/4AY9); [Proteopedia 4ay9](https://proteopedia.org/w/4ay9)
- Fan Q.R. & Hendrickson W.A. 2005, *Nature* 433:269 (PDB 1XWD), cited from memory; not retrieved in this search.
- Casarini L. & Crépieux P. 2019, *Front Endocrinol* 10:305: [frontiersin.org](https://www.frontiersin.org/articles/10.3389/fendo.2019.00305/full); [PMC6527893](https://pmc.ncbi.nlm.nih.gov/articles/PMC6527893)
- Landomiel F. et al. 2019, "Biased Signaling and Allosteric Modulation at the FSHR", *Front Endocrinol* 10:148: [frontiersin.org](https://www.frontiersin.org/journals/endocrinology/articles/10.3389/fendo.2019.00148/full); [PMC6425863](https://pmc.ncbi.nlm.nih.gov/articles/PMC6425863)
- "Follicle-stimulating hormone receptor: Advances and remaining challenges": [arXiv 1808.01965](https://arxiv.org/pdf/1808.01965)
- Nechamen C.A. et al. 2004, *Biol Reprod* 71:629 (APPL1): [BioOne](https://bioone.org/journals/biology-of-reproduction/volume-71/issue-2/biolreprod.103.025833/Human-Follicle-Stimulating-Hormone-FSH-Receptor-Interacts-with-the-Adaptor/10.1095/biolreprod.103.025833.full); [BioGRID](https://thebiogrid.org/62967/publication/human-follicle-stimulating-hormone-fsh-receptor-interacts-with-the-adaptor-protein-appl1-in-hek-293-cells-potential-involvement-of-the-pi3k-pathway-in-fsh-signaling.html)
- FSH signalling in granulosa cells review: [PMC2946492](https://pmc.ncbi.nlm.nih.gov/articles/PMC2946492)
- 2024 review of FSH–IGF cross-talk in granulosa cells: [PMC10988955](https://pmc.ncbi.nlm.nih.gov/articles/PMC10988955)
- Aittomäki K. et al. 1995, *Cell* 82:959 (PMID 7553856): [DrugBank record](https://drugbank.ca/articles/A54202)
- Tapanainen J.S. et al. 1997, *Nat Genet* 15:205: [nature.com PDF](https://www.nature.com/articles/ng0297-205.pdf)
- Dierich A. et al. 1998, *PNAS* (Fshr knockout): [PMC24867](https://pmc.ncbi.nlm.nih.gov/articles/PMC24867)
- Chrusciel M. et al. 2019, "Extragonadal FSHR Expression and Function—Is It Real?", *Front Endocrinol* 10:32: [PMC6369633](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6369633/)
- *Endocrinology* mini-review on nongonadal FSH actions: [academic.oup.com](https://academic.oup.com/endo/article/159/1/2/4725019)
- Sun L. et al. 2006, *Cell* 125:247 (FSH and bone), as summarized in the review above.
- Smits G. et al. 2003 and Vassart G. et al. 2003, *NEJM* (OHSS; PMID 12930927 and 12930928, from the UniProt record).

## Citations

1. https://pmc.ncbi.nlm.nih.gov/articles/pmid/22802634
2. https://www.rcsb.org/structure/4AY9
3. https://proteopedia.org/w/4ay9
4. https://www.nature.com/articles/s41467-023-36170-3.pdf
5. https://www.rcsb.org/structure/8i2g
6. https://doaj.org/article/856683e70c7b4674b3561a58992980ab
7. https://www.frontiersin.org/articles/10.3389/fendo.2019.00305/full
8. https://pmc.ncbi.nlm.nih.gov/articles/PMC6527893
9. https://pmc.ncbi.nlm.nih.gov/articles/PMC2946492
10. https://pmc.ncbi.nlm.nih.gov/articles/PMC10988955
11. https://bioone.org/journals/biology-of-reproduction/volume-71/issue-2/biolreprod.103.025833/Human-Follicle-Stimulating-Hormone-FSH-Receptor-Interacts-with-the-Adaptor/10.1095/biolreprod.103.025833.full
12. https://thebiogrid.org/62967/publication/human-follicle-stimulating-hormone-fsh-receptor-interacts-with-the-adaptor-protein-appl1-in-hek-293-cells-potential-involvement-of-the-pi3k-pathway-in-fsh-signaling.html
13. https://www.frontiersin.org/journals/endocrinology/articles/10.3389/fendo.2019.00148/full
14. https://pmc.ncbi.nlm.nih.gov/articles/PMC6425863
15. https://arxiv.org/pdf/1808.01965
16. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6369633/
17. https://academic.oup.com/endo/article/159/1/2/4725019
18. https://drugbank.ca/articles/A54202
19. https://www.nature.com/articles/ng0297-205.pdf
20. https://pmc.ncbi.nlm.nih.gov/articles/PMC24867