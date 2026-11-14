---
provider: claude_code
cached: false
start_time: '2026-11-13T22:24:16.207643'
end_time: '2026-11-13T22:26:09.124759'
duration_seconds: 112.92
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: TAC3
  gene_symbol: TAC3
  uniprot_accession: Q9UHF0
  protein_description: 'RecName: Full=Tachykinin-3; AltName: Full=ZNEUROK1; Contains:
    RecName: Full=Neurokinin-B; Short=NKB; AltName: Full=Neuromedin-K; Flags: Precursor;'
  gene_info: Name=TAC3; Synonyms=NKNB; ORFNames=UNQ585/PRO1155;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the tachykinin family. .
  protein_domains: Neurokinin-B/TAC3. (IPR003635); Tachy_Neuro_lke_CS. (IPR013055);
    Neurokinin_B (PF03823)
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
  num_turns: 11
  total_cost_usd: 0.7183510999999999
  session_id: bc175679-1437-4654-b4cd-b0e711d7f2ad
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  assistant_text_blocks: 2
citation_count: 14
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q9UHF0
- **Protein Description:** RecName: Full=Tachykinin-3; AltName: Full=ZNEUROK1; Contains: RecName: Full=Neurokinin-B; Short=NKB; AltName: Full=Neuromedin-K; Flags: Precursor;
- **Gene Information:** Name=TAC3; Synonyms=NKNB; ORFNames=UNQ585/PRO1155;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the tachykinin family. .
- **Key Domains:** Neurokinin-B/TAC3. (IPR003635); Tachy_Neuro_lke_CS. (IPR013055); Neurokinin_B (PF03823)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "TAC3" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'TAC3' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **TAC3** (gene ID: TAC3, UniProt: Q9UHF0) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

I'm checking a few more primary sources (placental NKB, receptor selectivity), then I'll write the report.

# TAC3 (Tachykinin‑3 / Neurokinin B), Human: Research Report

**Target:** TAC3, UniProtKB Q9UHF0, *Homo sapiens*. Synonyms are NKNB and ZNEUROK1. The mature product is the peptide neurokinin B (NKB, also called neuromedin K or neurokinin β).

**Identity check:** The symbol, the protein description ("Tachykinin‑3, contains Neurokinin‑B"), the family (tachykinin family; IPR003635 Neurokinin‑B/TAC3; PF03823) and the organism all match the literature below. There is no symbol ambiguity: "TAC3" consistently means the NKB precursor gene in human genetics and neuroendocrinology.

---

## 1. Summary

TAC3 encodes a 121‑residue secreted prepro‑peptide. Processing of this precursor releases the decapeptide **neurokinin B (NKB; Asp‑Met‑His‑Asp‑Phe‑Phe‑Val‑Gly‑Leu‑Met‑NH₂)**.

- **What it is:** NKB is a hormone and neurotransmitter, not an enzyme, transporter or structural protein. It is a ligand that preferentially activates the **neurokinin‑3 receptor (NK3R, encoded by TACR3)**. NK3R is a G protein‑coupled receptor (GPCR) that signals mainly through **Gq/11, phospholipase C (PLC), phosphoinositide hydrolysis and Ca²⁺**.
- **Main physiological role:** NKB is a central driver of reproduction. It is co‑expressed with kisspeptin and dynorphin in arcuate (infundibular) "KNDy" neurons, where it acts in an autocrine/paracrine way to synchronise the neurons and generate GnRH/LH pulses.
- **Human genetics:** Loss‑of‑function mutations in TAC3 or TACR3 cause normosmic congenital hypogonadotropic hypogonadism (HH10).
- **Other roles:** The same KNDy–NK3R circuit drives menopausal hot flushes, which NK3R antagonists such as fezolinetant now treat. NKB is also made by the placental syncytiotrophoblast.

---

## 2. Gene product structure and processing

### Precursor architecture (UniProt Q9UHF0)

| Feature | Residues | Evidence |
|---|---|---|
| Signal peptide | 1–16 | Predicted (ECO:0000255) |
| Propeptide | 17–78 | By similarity |
| **Neurokinin‑B** | **81–90** | Mature peptide |
| C‑terminal Met90 | 90 | **Methionine amide** (by similarity) |
| Propeptide | 94–121 | By similarity; disordered region |

### Processing
- Processing is the standard neuropeptide route. After signal‑peptide removal in the endoplasmic reticulum (ER), prohormone convertases cleave at the dibasic sites flanking NKB (Arg79‑Arg80 before it; the Gly91‑Lys92‑Arg93 motif after it).
- Peptidylglycine α‑amidating monooxygenase then converts Gly91 into the C‑terminal Met‑NH₂ amide.
- The amidated C‑terminal motif **Phe‑X‑Gly‑Leu‑Met‑NH₂** is the tachykinin family signature (PROSITE/InterPro Tachy_Neuro_lke_CS, IPR013055) and is needed for receptor activation.

### Isoforms
UniProt records three splice isoforms:
- **β** (canonical).
- **α**, which has a different C‑terminal propeptide but keeps NKB.
- **γ** (VSP_013186). This isoform replaces residues 80–98 with a single His, which deletes the NKB sequence. It is therefore unlikely to produce NKB; this is an inference from the sequence.

### Receptor selectivity: the "message–address" model
- The shared C‑terminal "message" (FxGLM‑NH₂) activates all three NK receptors.
- The divergent N‑terminal "address" sets subtype preference: NKB prefers NK3R, substance P (from TAC1) prefers NK1R, and neurokinin A prefers NK2R.
- Sun et al. (2023) solved cryo‑EM structures of **NK3R–Gq bound to NKB**, substance P and senktide. They state that *"the endogenous peptide agonist neurokinin B (NKB) preferentially activates NK3R, while substance P (SP) binds preferentially"* to NK1R. The structures show how the peptides engage the receptor and how Gq is coupled [PMID:37391393; Cell Discovery 2023].

---

## 3. Molecular function and signalling pathway

**Molecular function:** NKB is a receptor ligand, specifically a neuropeptide hormone (GO:0048018 receptor ligand activity; GO:0005184 neuropeptide hormone activity). Its main receptor is NK3R (TACR3). At higher concentrations it can also act on NK1R and NK2R.

**Pathway:**
1. NKB binds NK3R.
2. Gαq/11 activates PLCβ.
3. PLCβ hydrolyses PIP₂ into IP₃ and DAG.
4. Ca²⁺ is released from stores and PKC is activated.
5. The neuron depolarises and its excitability increases.

UniProt records Gq‑coupled phosphatidylinositol hydrolysis as experimental evidence for the human peptide (PubMed:37391393). It records NK3R‑mediated adenylate cyclase/cAMP signalling as "by similarity" from rodent data. In GO terms this corresponds to:
- GO:0007189: adenylate cyclase‑activating GPCR signalling.
- GO:0007217: tachykinin receptor signalling pathway.
- GO:0007209: phospholipase C‑activating tachykinin receptor signalling pathway.

**Functional validation from disease variants:**
- **HH10 variant p.Met90Thr** (in NKB, Met10Thr). This substitution changes the C‑terminal Met‑NH₂, which every tachykinin needs. In Topaloglu et al. (2009) it **markedly reduced the peptide's ability to activate NK3R**. This is direct evidence that the conserved amidated C‑terminus is required for function [PMID:19079066; Nat Genet 2009;41:354–358; doi:10.1038/ng.306].
- **Variant p.Arg80Ser** sits at the processing site just before NKB. It was found in a patient with normosmic IHH who also carried an HS6ST1 mutation (oligogenic) [PMID:23643382; Miraoui et al., Am J Hum Genet 2013].

---

## 4. Where it acts (localisation)

### Subcellular
- NKB is a **secreted / extracellular** peptide (GO:0005576 extracellular region). It is stored in dense‑core vesicles and released from axon terminals and dendrites.
- In the arcuate nucleus, NKB released by one KNDy neuron acts on NK3R on neighbouring KNDy neurons (recurrent collaterals) and on the neuron itself. This is a local paracrine/autocrine action at synapses within the neuron network, not long‑range endocrine signalling.

### Tissue and cellular expression
- **Hypothalamic arcuate/infundibular nucleus (KNDy neurons):** NKB is co‑expressed with kisspeptin (KISS1) and dynorphin A (PDYN). It was characterised in sheep, rodents, monkeys and humans [Lehman, Coolen & Goodman, *Endocrinology* 2010 (KNDy minireview); Moore, Novak & Lehman, *Endocrinology* 2023/24;165(2), PMID:38170643].
- **Postmenopausal women:** infundibular NKB neurons become larger and express more NKB mRNA. This is a classic human post‑mortem finding (Rance & Young, *Endocrinology* 1991) and reflects loss of oestrogen negative feedback.
- **Placenta:** the outer syncytiotrophoblast secretes NKB, which is detectable in maternal plasma from about week 9 of pregnancy. Plasma levels are raised in pre‑eclampsia and pregnancy‑induced hypertension [Page et al., *Nature* 2000;405:797–800, doi:10.1038/35015579]. Placental TAC3 expression is about 1.7‑fold higher in pre‑eclamptic placentas [Kingston eprints 1558].
- **Elsewhere:** NKB is also present in other brain regions, spinal cord and some peripheral tissues (uterus, gut), where it is generally less studied.

---

## 5. Biological processes

### 5.1 Core role: GnRH pulse generation and control of reproduction
- **Pulse‑generator model:** NKB released within the KNDy network acts on NK3R to start and synchronise burst firing. Kisspeptin is the output to GnRH neurons, and dynorphin (via κ‑opioid receptors) ends each burst.
- Moore et al. (2023) review the model: *"NKB drives synchronized firing, kisspeptin is the output, and dynorphin ends each burst."* KNDy neurons are both necessary and sufficient for pulsatility. Glutamate also contributes to network synchronisation, and the role of dynorphin differs between species [PMID:38170643].
- Other reviews (Uenoyama et al., *Front Endocrinol* 2021) call KNDy neurons the "GnRH pulse generator" [PMC8458932].
- **Human genetic proof (the strongest evidence for core function):** Topaloglu et al. (2009) found homozygous TAC3 (M90T) and TACR3 loss‑of‑function mutations in consanguineous families with normosmic hypogonadotropic hypogonadism. Patients had absent puberty and low LH and testosterone. This *"reveal[s] a key role for Neurokinin B in the central control of reproduction"* [PMID:19079066].
- **Later cohorts** (Gianetti et al., *JCEM* 2010; Young et al., *JCEM* 2010) confirmed that the TAC3/TACR3 phenotype is hypothalamic (GnRH deficiency). They also described a high rate of **reversal** of hypogonadism in adulthood, which suggests redundancy develops in the mature axis.
- **Disease entry:** HH10 [MIM:614839].
- **Mechanistic placement:** NKB acts **upstream of kisspeptin**. Pharmacological studies show that senktide (an NK3R agonist) stimulates LH secretion through kisspeptin/KISS1R, and that NK3R antagonists lower LH pulse frequency in humans and animals.

### 5.2 Thermoregulation and menopausal vasomotor symptoms
- KNDy neurons project to the median preoptic nucleus, a thermoregulatory centre. After oestrogen withdrawal, increased NKB/NK3R signalling there triggers heat‑dissipation responses (hot flushes).
- In rats, ablating KNDy neurons changes tail‑skin vasodilation (Mittelman‑Smith et al., *PNAS* 2012).
- In humans, intravenous NKB induces hot flushes in women (Jayasena et al., *Sci Rep* 2015).
- **Translation:** Fezolinetant, a selective NK3R antagonist, reduced the frequency and severity of moderate‑to‑severe vasomotor symptoms in the phase 3 SKYLIGHT 1 and 2 trials (12 weeks placebo‑controlled, 40‑week extension; SKYLIGHT 4 was a 52‑week safety study). Its effect over placebo was about 2.5–3 fewer episodes per day [PMC10348473; JCEM 2023;108(8):1981].
- Fezolinetant was approved by the FDA in 2023. The dual NK1/NK3 antagonist elinzanetant followed in 2025.
- These trials are pharmacological validation that endogenous NKB→NK3R signalling causes vasomotor symptoms.

### 5.3 Pregnancy and the placenta
- Page et al. (2000) proposed that excessive NKB secretion by the placenta in the third trimester contributes to hypertension in pre‑eclampsia [doi:10.1038/35015579].
- This is supported by elevated plasma and placental expression. The causal model is still debated, so it is best treated as a secondary or peripheral role.

### 5.4 Other tachykinin actions
- The general tachykinin activities recorded in UniProt (neuronal excitation, smooth‑muscle contraction, vasodilation, secretagogue action) apply to the family as a whole.
- For NKB, central actions on vasopressin release, fluid balance and reward circuits are mostly described in rodents. They are peripheral to its core reproductive role.

---

## 6. Evolution and bioinformatic inference

- TAC3 is a member of the vertebrate tachykinin family; its paralog TAC1 encodes substance P and NKA.
- The amidated FxGLM‑NH₂ motif is conserved, and the NKB decapeptide sequence is essentially identical across mammals. The fish orthologues (tac3a/tac3b) encode NKB and an "NKF" peptide that also regulate gonadotropins, which supports an ancient reproductive role.
- The Pfam Neurokinin_B (PF03823) domain covers the precursor.
- The C‑terminal propeptide (94–121) is predicted to be intrinsically disordered (MobiDB‑lite) and has no known function.
- No catalytic or transmembrane features are present, which is consistent with a soluble secreted ligand.

---

## 7. Annotation‑relevant synthesis

| Aspect | Best‑supported description | Key evidence |
|---|---|---|
| MF | Neuropeptide hormone / receptor ligand activity; tachykinin receptor (NK3R) binding | Sun 2023 cryo‑EM and signalling [PMID:37391393]; Topaloglu 2009 functional assay [PMID:19079066] |
| BP (core) | Tachykinin receptor signalling pathway (PLC‑activating, Gq); regulation of GnRH/LH pulsatile secretion; reproductive (puberty/gonadotropin) control | Human genetics [PMID:19079066]; KNDy reviews [PMID:38170643] |
| BP (secondary) | Thermoregulation (vasomotor), placental/pregnancy roles | Fezolinetant trials; Page 2000 |
| CC | Extracellular region / extracellular space (secreted); neuronal dense‑core vesicles/axon terminals of arcuate KNDy neurons | UniProt; neuroanatomy reviews |

**Notes on the existing GOA set:**
- GO:0048018 receptor ligand activity (IDA), GO:0007209 PLC‑activating tachykinin receptor signalling (IDA) and GO:0005576 extracellular region are well supported.
- The cAMP pathway term GO:0007189 rests on "by similarity" (rodent) evidence.
- GO:0045777 (positive regulation of blood pressure, IBA) is consistent with the placenta/pre‑eclampsia hypothesis and with tachykinin vasoactivity, but it is peripheral.
- GO:0005515 (protein binding, IPI; JPH3, PRB1, high‑throughput) is uninformative. The informative interaction is with TACR3.

---

## 8. Open questions and suggested experiments

1. **Processing:** Which prohormone convertase(s) (PC1/3 vs PC2) process proNKB in human KNDy neurons and in placenta? Do the α and β isoforms differ in how efficiently NKB is released? Test with convertase knockdown in TAC3‑expressing cells and mass spectrometry peptidomics.
2. **γ isoform:** Is the γ isoform, which lacks NKB, translated? Does it have any function?
3. **Reversal:** Why does hypogonadism reverse in adults with TAC3/TACR3 mutations? Candidate explanations are compensation by NK1R/NK2R signalling (substance P, NKA) or kisspeptin network plasticity. Test with combined receptor antagonism in adult animal models.
4. **Placenta:** Is placental NKB a cause of pre‑eclampsia or only a marker? Test with trophoblast‑specific Tac3 deletion in rodent pre‑eclampsia models.

---

## Sources

**Local cached papers and records (repository `publications/`):**
- Topaloglu AK et al. *TAC3 and TACR3 mutations in familial hypogonadotropic hypogonadism reveal a key role for Neurokinin B in the central control of reproduction.* Nat Genet 2009;41:354–358. PMID:19079066; doi:10.1038/ng.306; PMC4312696.
- Sun W et al. *Structural insights into neurokinin 3 receptor activation by endogenous and analogue peptide agonists.* Cell Discov 2023. PMID:37391393.
- Miraoui H et al. *Mutations in FGF17, IL17RD, DUSP6, SPRY4, and FLRT3 are identified in individuals with congenital hypogonadotropic hypogonadism.* Am J Hum Genet 2013. PMID:23643382.
- UniProtKB Q9UHF0 (TAC3_HUMAN), local copy `genes/human/TAC3/TAC3-uniprot.txt`.

**Web sources:**
- [Moore AM, Novak AG, Lehman MN. KNDy Neurons of the Hypothalamus and Their Role in GnRH Pulse Generation: an Update. Endocrinology 2023/2024;165(2) (PMID:38170643)](https://www.endocrine.org/journals/endocrinology/kndy-neurons-of-the-hypothalamus-and-their-role-in-gnrh-pulse-generation)
- [Same review, bibliographic record](https://pesquisa.bvsalud.org/mtci/resource/es/mdl-38170643)
- [Uenoyama et al., Front Endocrinol 2021 (KNDy neurons as GnRH pulse generator)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8458932)
- [Front Endocrinol 2021 PDF](https://frontiersin.org/articles/10.3389/fendo.2021.724632/pdf)
- [Front Endocrinol 2022 review on ARC kisspeptin neurons](https://www.frontiersin.org/journals/endocrinology/articles/10.3389/fendo.2022.951938/epub)
- [KNDy review, PMC6098225](https://pmc.ncbi.nlm.nih.gov/articles/PMC6098225)
- [Fezolinetant SKYLIGHT trial (PMC10348473)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10348473/)
- [JCEM 2023;108(8):1981 fezolinetant](https://academic.oup.com/jcem/article/108/8/1981/7025342)
- [Fezolinetant review, PMC10583986](https://pmc.ncbi.nlm.nih.gov/articles/PMC10583986)
- [IMS Menopause Live, fezolinetant efficacy and safety](https://menopause.org.au/members/ims-menopause-live/efficacy-and-safety-of-fezolinetant-for-the-treatment-of-moderate-to-severe-menopausal-related-vasomotor-symptoms)
- [Relias Media commentary on SKYLIGHT effect sizes](https://www.reliasmedia.com/articles/nonhormonal-treatment-for-menopausal-vasomotor-symptoms-a-phase-iii-study-of-fezolinetant)
- [Page N et al. Excessive placental secretion of neurokinin B during the third trimester causes pre‑eclampsia. Nature 2000;405:797–800](https://www.nature.com/articles/35015579)
- [Gene regulation of NKB and NK3 in late pregnancy and pre‑eclampsia (Kingston eprints)](https://eprints.kingston.ac.uk/1558)
- [PMC2290535 (NKB/NK3 placenta context)](https://pmc.ncbi.nlm.nih.gov/articles/PMC2290535)

**Cited from background knowledge, not re‑fetched this session (no PMIDs given):** Rance & Young 1991 (*Endocrinology*); Lehman, Coolen & Goodman 2010 (*Endocrinology*); Gianetti et al. 2010 and Young et al. 2010 (*JCEM*); Mittelman‑Smith et al. 2012 (*PNAS*); Jayasena et al. 2015 (*Sci Rep*); the 2025 approval of elinzanetant. Check these against PubMed before using them as formal citations in a review file.

## Citations

1. https://www.endocrine.org/journals/endocrinology/kndy-neurons-of-the-hypothalamus-and-their-role-in-gnrh-pulse-generation
2. https://pesquisa.bvsalud.org/mtci/resource/es/mdl-38170643
3. https://pmc.ncbi.nlm.nih.gov/articles/PMC8458932
4. https://frontiersin.org/articles/10.3389/fendo.2021.724632/pdf
5. https://www.frontiersin.org/journals/endocrinology/articles/10.3389/fendo.2022.951938/epub
6. https://pmc.ncbi.nlm.nih.gov/articles/PMC6098225
7. https://pmc.ncbi.nlm.nih.gov/articles/PMC10348473/
8. https://academic.oup.com/jcem/article/108/8/1981/7025342
9. https://pmc.ncbi.nlm.nih.gov/articles/PMC10583986
10. https://menopause.org.au/members/ims-menopause-live/efficacy-and-safety-of-fezolinetant-for-the-treatment-of-moderate-to-severe-menopausal-related-vasomotor-symptoms
11. https://www.reliasmedia.com/articles/nonhormonal-treatment-for-menopausal-vasomotor-symptoms-a-phase-iii-study-of-fezolinetant
12. https://www.nature.com/articles/35015579
13. https://eprints.kingston.ac.uk/1558
14. https://pmc.ncbi.nlm.nih.gov/articles/PMC2290535