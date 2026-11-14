---
provider: claude_code
model: redacted
cached: false
start_time: '2026-11-13T21:51:20.431371'
end_time: '2026-11-13T21:53:20.910457'
duration_seconds: 120.48
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: TACR3
  gene_symbol: TACR3
  uniprot_accession: P29371
  protein_description: 'RecName: Full=Neuromedin-K receptor; Short=NKR; AltName: Full=NK-3
    receptor; Short=NK-3R; AltName: Full=Neurokinin B receptor; AltName: Full=Tachykinin
    receptor 3;'
  gene_info: Name=TACR3; Synonyms=NK3R, TAC3R;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the G protein-coupled receptor 1 family.
  protein_domains: GPCR_Rhodpsn. (IPR000276); GPCR_Rhodpsn_7TM. (IPR017452); Neurokn_rcpt.
    (IPR001681); NK3_rcpt. (IPR001013); 7tm_1 (PF00001)
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
  models_used: redacted
  web_search_requests: 6
  num_turns: 9
  total_cost_usd: 0.9258077
  session_id: ab863c20-b616-4f55-b119-c74ff95f808f
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 16
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P29371
- **Protein Description:** RecName: Full=Neuromedin-K receptor; Short=NKR; AltName: Full=NK-3 receptor; Short=NK-3R; AltName: Full=Neurokinin B receptor; AltName: Full=Tachykinin receptor 3;
- **Gene Information:** Name=TACR3; Synonyms=NK3R, TAC3R;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the G protein-coupled receptor 1 family.
- **Key Domains:** GPCR_Rhodpsn. (IPR000276); GPCR_Rhodpsn_7TM. (IPR017452); Neurokn_rcpt. (IPR001681); NK3_rcpt. (IPR001013); 7tm_1 (PF00001)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "TACR3" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'TACR3' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **TACR3** (gene ID: TACR3, UniProt: P29371) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# TACR3 (Neuromedin-K receptor / NK3R), human, UniProt P29371: functional annotation report

## 0. Identity check

The symbol, protein and organism all match the target, and none of the literature found points to a different gene with this name.

- **Symbol:** TACR3 (synonyms NK3R, TAC3R). It encodes the neuromedin-K receptor, also called the neurokinin-3 or neurokinin B receptor.
- **Protein:** 465 amino acids, 7-transmembrane (7TM), from rhodopsin-like class A of the G protein-coupled receptor 1 family. InterPro places it in the neurokinin receptor (IPR001681) and NK3 receptor (IPR001013) families. All of this agrees with the papers below.
- **Organism:** every human-specific claim below comes from studies of human TACR3 or human patients. Rodent and sheep findings are marked as such.

---

## 1. Primary function: a receptor for neurokinin B

### Ligands and how selective it is
NK3R is the high-affinity receptor for the tachykinin **neurokinin B (NKB, neuromedin-K)**. NKB is encoded by *TAC3*. UniProt's curated summary, based on the human cloning paper (Buell et al., *FEBS Lett* 1992, PMID:1312036) and the 2023 structure paper (PMID:37391393), says:

> "Receptor for the tachykinin neuromedin-K (neurokinin B), also able to bind and respond to tachynins substance K/neurokinin A and substance P … The rank order of affinity of this receptor to tachykinins is: neuromedin-K > substance K and substance P" (UniProt P29371, CC FUNCTION; ECO:0000269 PubMed:1312036, 37391393).

IntAct has a direct binary interaction between P29371 and the mature NKB peptide (PRO_0000033566, from TAC3 Q9UHF0). This is a receptor–ligand pair, not a scaffold interaction, so the informative molecular-function term is **tachykinin receptor activity / neuromedin-K receptor activity** rather than "protein binding".

### Structure (2023)
Sun et al. (*Cell Discovery*, June 2023; PMID:37391393; [PMC10313662](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10313662/); [DOI 10.1038/s41421-023-00564-w](https://link.springer.com/article/10.1038/s41421-023-00564-w)) solved cryo-EM structures of human NK3R bound to Gq.

- **Ligands and resolutions:** NKB at 2.8 Å (PDB [8JBG](https://www.rcsb.org/structure/8JBG)), substance P at 2.9 Å (8JBH) and the synthetic agonist senktide at 3.0 Å (8JBF).
- **How peptides bind:** the C-terminal tachykinin motif (FxGLM-NH₂), which all three peptides share, binds NK3R in the same way. The differing N-termini decide which peptide the receptor prefers. This explains the NKB > NKA ≈ SP order at the structural level.
- **Activation:** all three complexes use what the authors call a "noncanonical" activation mechanism. It differs from the textbook class A rearrangements of the conserved receptor motifs.

The structure gives atomic-level direct evidence for two things: peptide-hormone binding in the extracellular/7TM pocket, and direct coupling to the heterotrimeric G protein Gq on the cytoplasmic face.

---

## 2. Signalling pathway

| Step | Evidence | Source |
|---|---|---|
| NKB binds NK3R at the cell surface | Binding assays, cryo-EM | PMID:1312036; PMID:37391393 |
| NK3R couples to **Gαq/11** | Cryo-EM of the NK3R–Gq complex; functional assays | PMID:37391393 |
| Gq activates **phospholipase C-β**, which hydrolyses PIP₂ into IP₃ and DAG | Inositol phosphate accumulation | UniProt FUNCTION (PubMed:37391393) |
| IP₃ releases Ca²⁺ from intracellular stores; DAG activates PKC | Ca²⁺ mobilisation assays used to test patient variants | Patient-variant studies (below) |
| Possible **Gs/adenylate cyclase**, raising cAMP | Inferred by similarity to rat Nk3r (P16177), not shown for the human protein | UniProt FUNCTION, "By similarity" |

**Main pathway:** G protein-coupled receptor signalling through Gq, then phospholipase C activation, then a rise in cytosolic Ca²⁺. The GOA terms for this are GO:0007186, GO:0007217 (tachykinin receptor signalling pathway), GO:0007200/GO:0007218 (neuropeptide signalling) and the PLC-activating GPCR terms.

**cAMP is uncertain.** Coupling to adenylate cyclase (GO:0007189) is only inferred by similarity for the human receptor and should be treated as secondary.

**Regulation:** as with other tachykinin receptors, agonist binding is followed by phosphorylation, β-arrestin recruitment and internalisation. UniProt says membrane anchoring is "probably mediated by the palmitoylation of a cysteine residue", which is an inference.

---

## 3. Where it acts

- **Within the cell:** the plasma membrane, as an integral multi-pass protein. UniProt lists "Cell membrane {ECO:0000269|PubMed:37968728}; Multi-pass membrane protein". The membrane topology is predicted (ECO:0000255): an extracellular N-terminus (residues 1–84) and seven helices starting at residues 85–107.
  - The membrane location fits its function, since it senses an extracellular peptide.
  - Cell-surface trafficking matters clinically: some patient missense variants reduce how much receptor reaches the plasma membrane (Section 4).
  - I could not confirm from abstracts exactly what PMID:37968728 shows about location ([SciCrunch record](https://scicrunch.org/scicrunch/37968728?rpKey=on)). Check it before relying on it.
- **Neuronal compartments** in GOA include neuronal cell body, dendrite, axon terminus and sperm midpiece (GO:0097225). These come from rodent work or human sperm studies. They are plausible for a neuropeptide receptor but secondary to the plasma-membrane claim.
- **Tissues:** mainly the central nervous system.
  - Hypothalamus: the arcuate nucleus, where KNDy neurons express NK3R themselves; the median preoptic nucleus; and GnRH-neuron terminal fields.
  - Also cortex, substantia nigra and other basal-ganglia and limbic regions.
  - Lower expression outside the CNS: enteric neurons, placenta/uterus and spermatozoa.

---

## 4. Core biological role: controlling reproduction through the GnRH pulse generator

### Human genetics
Topaloglu et al. (*Nat Genet* 2009; 41:354–358; PMID:19079066) found that affected members of consanguineous families with severe congenital gonadotropin deficiency and failed puberty were homozygous for loss-of-function mutations in *TAC3* or *TACR3*. This established that NKB–NK3R signalling is required for human sexual maturation ([summary of the 2009 work](https://pmc.ncbi.nlm.nih.gov/articles/PMC4306717)).

Later cohorts confirmed autosomal recessive normosmic congenital hypogonadotropic hypogonadism. That condition is OMIM **HH11** (MIM:614840; UniProt DISEASE, PubMed:19079066, 23643382, 25077900).

- **Gagliardi/Young et al.** ([JCEM, PMC3198730](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3198730/)) described the neuroendocrine phenotype. Patients have low LH pulse frequency, and LH responds to exogenous pulsatile GnRH. This puts the defect **upstream of GnRH neurons**, not in the pituitary.
- **Disease mechanism:** studies of patient variants show NK3R function is disrupted in distinct ways ([TACR3 mutations disrupt NK3R function through distinct mechanisms](https://www.peeref.com/works/9635028)):
  - impaired ligand binding;
  - impaired Gq/Ca²⁺ signalling;
  - reduced trafficking to the plasma membrane.
- **Oligogenic cases:** UniProt notes "Oligogenic inheritance has been reported in some patients carrying mutations in TACR3 as well as in other HH-associated genes including FGFR1, SPRY4 and KAL1 (PubMed:23643382)".
- **Partial recovery:** "reversal" of hypogonadism in adulthood is often reported in TACR3 patients. This suggests NK3R matters most for setting off the pubertal GnRH rhythm.

### Cellular mechanism: the KNDy model
NK3R is the receptor through which NKB acts on **KNDy neurons** in the arcuate nucleus. These neurons co-express kisspeptin, neurokinin B and dynorphin, and they are thought to be the hypothalamic GnRH pulse generator. Reviews: [PMC6098225](https://pmc.ncbi.nlm.nih.gov/articles/PMC6098225); [Frontiers Endocrinol 2021](https://frontiersin.org/articles/10.3389/fendo.2021.724632/pdf); [Fergani & Navarro](https://researchonline.ljmu.ac.uk/id/eprint/8795/1/Fergani%20Navarro%20Tachykinin%20review.pdf).

The current model:
1. NKB released by KNDy neurons acts on NK3R on neighbouring KNDy neurons, and on the releasing neuron itself, to start a synchronised burst.
2. The burst releases kisspeptin onto GnRH neuron terminals through KISS1R, which drives a GnRH/LH pulse.
3. Dynorphin acting on κ-opioid receptors ends the pulse.

Supporting evidence:
- In mice, the NK3R agonist senktide makes KNDy neurons fire more action potentials, and the effect is stronger after castration.
- In mice, rats and goats, senktide stimulates LH.
- The LH effect is not consistent: in some steroid states (for example oestradiol-treated ovariectomised rats) senktide suppresses LH. NK3R output therefore depends on the steroid environment ([PMC6098225](https://pmc.ncbi.nlm.nih.gov/articles/PMC6098225)).
- Kisspeptin-independent routes to GnRH release exist but are poorly defined.

**Who does the work:** NK3R itself performs the step that turns a neuropeptide signal into Ca²⁺ signalling and neuronal excitation. It is the signal-transducing component of the GnRH pulse-generator circuit. Annotating it to neuropeptide signalling, and to regulation of gonadotropin secretion and reproductive processes, is well supported. Downstream events such as GnRH secretion and gonad development are carried out by other cells, so those terms are indirect.

---

## 5. Second well-supported role: thermoregulation and menopausal hot flushes

**Rodent evidence:**
- KNDy neurons project to the median preoptic nucleus (MnPO) and medial preoptic area, which belong to the heat-defence pathway and express NK3R.
- Rats in which MnPO NK3R neurons were ablated with NK3-saporin had lower tail-skin temperature. This implies those neurons help drive cutaneous vasodilation.
- Mice lacking MnPO NK3R neurons had higher core temperature during the light phase.
- These neurons are glutamatergic, and they are neither warm-sensitive nor activated by skin or visceral warm sensors. KNDy neurons therefore seem to adjust heat-defence pathways indirectly through MnPO NK3R neurons (Krajewski-Hall, Rance et al. 2019; [PMC6424091](https://pmc.ncbi.nlm.nih.gov/articles/PMC6424091), [PMC4475724](https://pmc.ncbi.nlm.nih.gov/articles/4475724)).
- After menopause, oestrogen withdrawal causes KNDy neurons to grow larger and express more NKB. This is proposed to over-drive NK3R signalling in the MnPO.

**Human pharmacology (strong translational evidence):**
- **Fezolinetant (Veozah, Astellas)** is a selective NK3R antagonist. The FDA approved it on 12 May 2023 for moderate-to-severe menopausal vasomotor symptoms, based on the SKYLIGHT phase 3 trials. A boxed warning for hepatotoxicity was added in December 2024 ([Pharmacy Times](https://www.pharmacytimes.com/view/fda-approves-elinzanetant-as-first-nonhormonal-therapy-for-menopause-vasomotor-symptoms); [Cleveland Clinic](https://consultqd.clevelandclinic.org/a-new-family-of-nk3-receptor-antagonists-offer-menopausal-symptom-relief); [pharmaphorum](https://pharmaphorum.com/news/astellas-breaks-new-ground-menopause-veozah)).
- **Elinzanetant (Lynkuet, Bayer)** blocks both NK1R and NK3R. The FDA approved it on 24 October 2025, based on the OASIS 1–3 trials ([Pharmacy Times, Oct 2025](https://www.pharmacytimes.com/view/fda-approves-elinzanetant-as-first-nonhormonal-therapy-for-menopause-vasomotor-symptoms); [clinician.com](https://www.clinician.com/articles/elinzanetant-capsules-lynkuet)).
- Earlier, NK3R antagonists such as MLE4901 (pavinetant) reduced hot flushes in a proof-of-concept trial. Infusing NKB into healthy premenopausal women caused hot-flush-like episodes (Jayasena et al. 2015, from memory; my search did not retrieve it).

Together these make human NK3R a validated regulator of central heat-dissipation responses. For GO, this supports a thermoregulation or body-temperature process term as a well-evidenced but non-core role.

---

## 6. Other, less central roles

Annotations such as regulation of dopamine metabolism, feeding, blood pressure, uterine contraction and sperm motility rest mostly on rodent pharmacology or descriptive studies. They are best treated as non-core.

- **Dopamine and the basal ganglia / mood:** NK3R in the substantia nigra, ventral tegmental area and cortex modulates dopamine release in rodents. NK3R antagonists (osanetant, talnetant) were tested for schizophrenia and did not succeed, so there is no strong human functional evidence.
- **Cardiovascular and feeding:** central injection of senktide in rodents raises blood pressure and changes drinking and feeding. These are the basis for GO:0045777 and GO:0060259.
- **Uterus/placenta and sperm:** NKB and NK3R are expressed in placenta and myometrium (pre-eclampsia hypothesis) and on human spermatozoa, where NK3R agonists modulate motility. This is the basis for GO:1902093 and the sperm midpiece term.
- **Enteric nervous system:** NK3R mediates slow excitatory transmission in myenteric neurons (mostly guinea pig and rodent data).

---

## 7. Evolution and bioinformatics

- **Family:** NK3R is one of three mammalian tachykinin receptors (TACR1/NK1R, TACR2/NK2R, TACR3/NK3R). The three are close paralogues in the rhodopsin-like GPCR family (Pfam PF00001 7tm_1; InterPro IPR000276, IPR017452) and share the peptide-binding pocket that recognises the FxGLM-NH₂ motif. The NK3-specific signature IPR001013 separates it from NK1R and NK2R.
- **Paralogue-transfer risk:** each paralogue prefers a different ligand (NK1R: SP; NK2R: NKA; NK3R: NKB). Annotations carried over between them by similarity may be imprecise about the ligand.
- **Conservation:** orthologues exist throughout vertebrates. The NKB/NK3R pair has a conserved role in controlling gonadotropins, including in teleost fish.
- **Domain layout (UniProt FT, predicted):** extracellular N-terminus (1–84) carrying N-glycosylation sites, seven TM helices, and a cytoplasmic C-terminal tail with a predicted palmitoylation site and Ser/Thr residues for receptor desensitisation.

---

## 8. Summary for annotation

| Aspect | Core assertion | Strength |
|---|---|---|
| **Molecular function** | Neuromedin-K (NKB) receptor activity / tachykinin receptor activity (GO:0016498 / GO:0004995); a GPCR coupled to Gq | Strong: human cloning, binding, cryo-EM (PMID:1312036, 37391393) |
| **Cellular component** | Plasma membrane, integral 7TM (GO:0005886) | Strong (UniProt ECO:0000269; topology) |
| **Biological process, core** | Tachykinin receptor signalling pathway (GO:0007217); Gq/PLC-coupled GPCR signalling, leading to intracellular Ca²⁺ | Strong |
| **Biological process, physiological** | Regulation of GnRH/LH pulsatile secretion and onset of puberty, via KNDy neurons | Strong: human genetics (PMID:19079066) and animal physiology |
| **Biological process, secondary** | Regulation of body temperature / heat-dissipation responses | Strong translational evidence (fezolinetant, elinzanetant) plus rodent circuit studies |
| **Peripheral** | Dopamine metabolism, blood pressure, feeding, uterine contraction, sperm motility | Mostly rodent or pharmacological; non-core |
| **Uncertain** | Gs/adenylate cyclase–cAMP coupling (GO:0007189) | Inferred by similarity only for the human receptor |

Bare "protein binding" (GO:0005515) adds nothing here. The interaction behind it is NK3R binding its peptide ligand NKB, which the receptor-activity terms already capture.

---

## Key references
1. Buell G et al. (1992) Molecular characterisation, expression and localisation of human neurokinin-3 receptor. *FEBS Lett*. PMID:1312036.
2. Sun W et al. (2023) Structural insights into neurokinin 3 receptor activation by endogenous and analogue peptide agonists. *Cell Discov* 9:66. PMID:37391393. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10313662/
3. Topaloglu AK et al. (2009) TAC3 and TACR3 mutations in familial hypogonadotropic hypogonadism reveal a key role for Neurokinin B in the central control of reproduction. *Nat Genet* 41:354–358. PMID:19079066.
4. Gagliardi/Young et al. Normosmic congenital hypogonadotropic hypogonadism due to TAC3/TACR3 mutations: neuroendocrine phenotypes and novel mutations. *JCEM*. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3198730/
5. UniProt P29371, curated FUNCTION, DISEASE (PubMed:23643382, 25077900) and SUBCELLULAR LOCATION (PubMed:37968728) sections.
6. KNDy / GnRH pulse-generator reviews: https://pmc.ncbi.nlm.nih.gov/articles/PMC6098225 ; https://frontiersin.org/articles/10.3389/fendo.2021.724632/pdf ; https://pmc.ncbi.nlm.nih.gov/articles/PMC4306717
7. Krajewski-Hall SJ, Rance NE et al. (2019) Glutamatergic NK3R neurons in the median preoptic nucleus modulate heat-defense pathways. https://pmc.ncbi.nlm.nih.gov/articles/PMC6424091 ; Mittelman-Smith/Rance rat studies, https://pmc.ncbi.nlm.nih.gov/articles/4475724
8. FDA approvals of fezolinetant (May 2023) and elinzanetant (Oct 2025): https://www.pharmacytimes.com/view/fda-approves-elinzanetant-as-first-nonhormonal-therapy-for-menopause-vasomotor-symptoms ; https://consultqd.clevelandclinic.org/a-new-family-of-nk3-receptor-antagonists-offer-menopausal-symptom-relief

**Not verified:** I read most sources only as abstracts or search excerpts. Check these against full text before using them in `supported_by` quotes:
- the exact membrane-localisation result in PMID:37968728;
- residue-level details of the cryo-EM binding pocket;
- the Jayasena NKB-infusion study, cited from memory without a PMID.

## Citations

1. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10313662/
2. https://link.springer.com/article/10.1038/s41421-023-00564-w
3. https://www.rcsb.org/structure/8JBG
4. https://scicrunch.org/scicrunch/37968728?rpKey=on
5. https://pmc.ncbi.nlm.nih.gov/articles/PMC4306717
6. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3198730/
7. https://www.peeref.com/works/9635028
8. https://pmc.ncbi.nlm.nih.gov/articles/PMC6098225
9. https://frontiersin.org/articles/10.3389/fendo.2021.724632/pdf
10. https://researchonline.ljmu.ac.uk/id/eprint/8795/1/Fergani%20Navarro%20Tachykinin%20review.pdf
11. https://pmc.ncbi.nlm.nih.gov/articles/PMC6424091
12. https://pmc.ncbi.nlm.nih.gov/articles/4475724
13. https://www.pharmacytimes.com/view/fda-approves-elinzanetant-as-first-nonhormonal-therapy-for-menopause-vasomotor-symptoms
14. https://consultqd.clevelandclinic.org/a-new-family-of-nk3-receptor-antagonists-offer-menopausal-symptom-relief
15. https://pharmaphorum.com/news/astellas-breaks-new-ground-menopause-veozah
16. https://www.clinician.com/articles/elinzanetant-capsules-lynkuet