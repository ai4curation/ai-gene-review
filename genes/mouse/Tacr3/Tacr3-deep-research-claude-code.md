---
provider: claude_code
model: redacted
cached: false
start_time: '2026-11-13T23:01:49.192788'
end_time: '2026-11-13T23:03:26.047083'
duration_seconds: 96.85
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: mouse
  gene_id: Tacr3
  gene_symbol: Tacr3
  uniprot_accession: P47937
  protein_description: 'RecName: Full=Neuromedin-K receptor; Short=NKR; AltName: Full=NK-3
    receptor; Short=NK-3R; AltName: Full=Neurokinin B receptor; AltName: Full=Tachykinin
    receptor 3;'
  gene_info: Name=Tacr3; Synonyms=Tac3r;
  organism_full: Mus musculus (Mouse).
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
  web_search_requests: 5
  num_turns: 8
  total_cost_usd: 0.6686367
  session_id: fd2400e3-c447-49c2-9fae-a1d5592fe80e
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 12
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P47937
- **Protein Description:** RecName: Full=Neuromedin-K receptor; Short=NKR; AltName: Full=NK-3 receptor; Short=NK-3R; AltName: Full=Neurokinin B receptor; AltName: Full=Tachykinin receptor 3;
- **Gene Information:** Name=Tacr3; Synonyms=Tac3r;
- **Organism (full):** Mus musculus (Mouse).
- **Protein Family:** Belongs to the G protein-coupled receptor 1 family.
- **Key Domains:** GPCR_Rhodpsn. (IPR000276); GPCR_Rhodpsn_7TM. (IPR017452); Neurokn_rcpt. (IPR001681); NK3_rcpt. (IPR001013); 7tm_1 (PF00001)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Tacr3" matches the protein description above**
2. **Verify the organism is correct:** Mus musculus (Mouse).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Tacr3' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Tacr3** (gene ID: Tacr3, UniProt: P47937) in mouse.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Tacr3 (Neuromedin-K receptor / NK3R) in *Mus musculus*: research report

**UniProt:** P47937 (TACR3_MOUSE) · **MGI:** MGI:892968 · **Synonyms:** Tac3r, Nk3r, NK-3R, neurokinin B receptor

---

## 1. Identity check

The symbol, protein and organism all match. Mouse *Tacr3* encodes the NK3 tachykinin receptor, a class A (rhodopsin-like) GPCR. Its preferred endogenous ligand is neurokinin B (NKB, called neuromedin K), which is encoded by mouse *Tac2*, the orthologue of human *TAC3*.

The local UniProt record agrees:
- It carries the family signatures GPCR_Rhodpsn (IPR000276), GPCR_Rhodpsn_7TM (IPR017452), Neurokn_rcpt (IPR001681), NK3_rcpt (IPR001013) and 7tm_1 (PF00001).
- It predicts seven transmembrane helices: residues 72–94, 105–126, 147–168, 189–209, 233–257, 287–308 and 322–346 (`genes/mouse/Tacr3/Tacr3-uniprot.txt`).

The mouse cDNA came from mouse brain. One record is GenBank X87823 (Maroteaux, 1995) ([MGI X87823](https://www.informatics.jax.org/sequence/X87823)). The full-length clone was characterised pharmacologically by Sarau et al. 2001 (below). The current RefSeq transcript is NM_021382 ([MGI:892968](https://www.informatics.jax.org/marker/MGI:892968)).

I found no ambiguity with a different gene.

---

## 2. Primary molecular function: a G protein-coupled receptor for neurokinin B

### 2.1 Ligands and selectivity

NK3R binds the tachykinins through their shared C-terminal Phe-X-Gly-Leu-Met-NH₂ motif, with the rank order **NKB > NKA (substance K) > substance P**.

In the mouse record this function statement is propagated from the human orthologue P16177 (ECO:0000250): "Receptor for the tachykinin neuromedin-K (neurokinin B), also able to bind and respond to tachynins substance K/neurokinin A and substance P… Neuromedin-K binding to its receptor triggers G protein-coupled receptor signaling via activation of G(q) and phosphatidylinositol hydrolysis by phospholipase C … also … activation of adenylate cyclase activity which results in increased intracellular levels of cyclic AMP" (UniProt P47937, CC FUNCTION).

**Direct experimental evidence on the mouse receptor** comes from Sarau et al., 2001, *Eur J Pharmacol* 413(2–3):143–150, "Molecular and pharmacological characterization of the murine tachykinin NK3 receptor" (doi:10.1016/s0014-2999(01)00732-4; [record](https://ouci.dntb.gov.ua/works/4ENVdqOl); [MEDLINE mdl-11226387](https://pesquisa.bvsalud.org/portal/resource/pt/mdl-11226387)):
- The full-length cDNA was isolated from mouse brain by PCR. It encodes a **452-amino-acid** protein that is **96% identical to rat NK3R and 86% identical to human NK3R**.
- In HEK293 cells, agonist binding and potency were broadly similar for the mouse and human receptors.
- Substance P and NKA were more potent at the mouse receptor in calcium-mobilisation assays. This is consistent with Gq signalling.
- **NK3-selective non-peptide antagonists from two structural classes bound the mouse receptor with 10–100-fold lower affinity than the human receptor**, and were 5–10-fold less potent in functional assays. This species difference matters when antagonists such as osanetant, talnetant or fezolinetant are used in mouse models.
- The peptide agonist **senktide** is a selective NK3R agonist in mouse and is the standard tool for activating it in vivo (see §4).

### 2.2 Signal transduction

- **Gq/11 → PLCβ → IP₃/DAG → Ca²⁺ mobilisation and PKC.** This is the canonical pathway, behind GO:0007209 "phospholipase C-activating tachykinin receptor signaling pathway". In mouse it is supported by agonist-evoked Ca²⁺ responses in HEK293 cells expressing the mouse receptor (Sarau et al. 2001).
- **Gs → adenylyl cyclase → cAMP** (GO:0007189). This is reported for the human and rat receptors. The mouse annotation is ISS/ISO, so I found no mouse-specific evidence for it.
- **Membrane anchoring.** UniProt notes that a C-terminal cysteine is "probably" palmitoylated to anchor the receptor to the plasma membrane. This is inferred, not shown experimentally.
- **GO term.** Neuromedin K receptor activity (GO:0016498) is the most specific accurate molecular-function term. Tachykinin receptor activity (GO:0004995) and G protein-coupled receptor activity (GO:0004930) are its parents.

### 2.3 Classification of the function

NK3R is a **signalling receptor**, not an enzyme or transporter. It converts extracellular NKB, released mainly from hypothalamic neurons, into Gq-dependent depolarisation and excitation of the neurons that carry it.

---

## 3. Cellular and anatomical localisation

**Subcellular location.** NK3R is an integral **plasma membrane** protein with seven transmembrane helices (UniProt FT TRANSMEM; inferred from rat P29371). The mouse GO cellular-component rows add the following, all transferred by ISO from rat:
- neuronal cell body and cell body membrane
- dendrite membrane
- dendritic spine head and spine membrane
- axon terminus
- sperm midpiece

These fit a receptor on the somatodendritic surface of central neurons. The sperm-midpiece row comes from rat and human work on NK3R in spermatozoa.

**Anatomical expression (mouse):**
- **Arcuate nucleus (ARC) KNDy neurons.** These neurons co-express kisspeptin, NKB and dynorphin, and they also express NK3R. This sets up an autosynaptic or reciprocal NKB→NK3R loop within the KNDy network (Navarro et al., *J Neurosci* 2009, mouse; recalled from memory, not re-verified in this session).
- **Median preoptic nucleus (MnPO) and medial preoptic area (MPA).** In the mouse MnPO, **94% of NK3R neurons were glutamatergic**, whereas in the adjacent MPA **97% were GABAergic** (Krajewski-Hall et al., *Endocrinology* 2019; [PMC6424091](https://pmc.ncbi.nlm.nih.gov/articles/PMC6424091)). These experiments used *Tacr3*-EGFP reporter mice.
- **GnRH neuron terminals in the median eminence.** NK3R immunoreactivity has been reported here in rodents, which suggests NKB can also act directly on GnRH output (literature context from memory).
- **Elsewhere.** NK3R is also expressed in midbrain dopaminergic regions (consistent with the ISO rows "regulation of dopamine metabolic process" and "response to cocaine"), in the hippocampus and cortex, and at lower levels in some peripheral tissues such as the uterus and enteric neurons.

---

## 4. Pathways and physiological roles

### 4.1 Reproductive axis: the KNDy/GnRH pulse generator (best supported)

NKB acting on NK3R is a key **positive, excitatory component of the GnRH/LH pulse generator**:
- NKB released from KNDy neurons acts on NK3R on KNDy neurons themselves. Together with inhibitory dynorphin acting on κ-opioid receptors, this synchronises the population's bursts of activity.
- Each burst releases kisspeptin onto GnRH neuron terminals, and GnRH in turn drives pulsatile LH secretion.
- In mice, senktide acting on NK3R raises LH in a sex-steroid-dependent way. This matches the GO term "positive regulation of luteinizing hormone secretion" (GO:0033686).

**Genetic evidence in mice:**
- **First *Tacr3*⁻/⁻ line (Kung et al. 2004).** These mice were reported to be fertile ([review, LJMU](https://researchonline.ljmu.ac.uk/id/eprint/13122/1/509222.pdf)).
- **Later analysis (Yang et al., *Endocrinology* 2012;153(4):1578, "Uncovering novel reproductive defects in neurokinin B receptor null mice")** ([link](https://dbpia.nl.go.kr/endo/article/153/4/1578/2423671)). *Tacr3*-null **females were subfertile**, while males attained fertility. I could not open this paper this session; the summary of its findings comes from the LJMU review.
- **Mice versus humans.** The mouse phenotype is milder than in humans, where *TACR3* and *TAC3* loss-of-function mutations cause normosmic congenital hypogonadotropic hypogonadism ([review](https://researchonline.ljmu.ac.uk/id/eprint/13122/1/509222.pdf)).
- **Redundancy.** *Tac1/Tac2* double knockouts, lacking all tachykinins, show a much stronger female phenotype: no preovulatory LH surge, low-frequency LH pulses, and 80% of females infertile. This points to compensation by NKA/NK2R and substance P/NK1R in mice. Consistent with this, *Tacr2*⁻/⁻ females have altered LH pulsatility but remain fertile ([LJMU NKA study](https://researchonline.ljmu.ac.uk/11578/3/Characterization%20of%20the%20role%20of%20NKA%20in%20the%20control%20of%20puberty%20onset%20and%20gonadotropin%20release%20in%20the%20female%20mouse..pdf); [ORBi, Torres 2021](https://orbi.uliege.be/bitstream/2268/260389/1/Torres%202021.pdf)).

**Interpretation.** In mice, NK3R is a direct receptor component of pulse-generator signalling, but it is partly redundant with the other tachykinin receptors. GO process terms such as "positive regulation of LH secretion" describe this receptor-level role. Developmental terms such as "vagina development" (GO:0060068), "response to estradiol" (GO:0032355) and "positive regulation of uterine smooth muscle contraction" (GO:0070474) are ISO rows that reflect downstream or peripheral effects.

### 4.2 Thermoregulation: a hypothalamic heat-dissipation pathway

KNDy neurons project to the MnPO, where NK3R-expressing neurons promote heat loss:
- **Ablation.** Selectively removing MnPO NK3R neurons in *Tacr3*-EGFP mice with NK3-saporin raised core temperature during the light phase, with or without estradiol. The authors interpreted this as a regulated shift in the balance point ([PMC6424091](https://pmc.ncbi.nlm.nih.gov/articles/PMC6424091)).
- **Agonist effects.** Subcutaneous senktide in mice causes tail-skin vasodilatation, cold-seeking behaviour and hypothermia. Estradiol attenuates these effects (same source).
- **Not warm sensors.** MnPO NK3R neurons were not activated by warm signals from the skin or viscera. The authors conclude that KNDy neurons modulate heat-defence pathways indirectly through glutamatergic MnPO NK3R neurons (same source).
- **Rat data.** In rats, NK3R neurons in the MnPO are required for senktide-induced hypothermia (Dacks et al. 2011; Mittelman-Smith et al. 2015) ([PMC4475724](https://pmc.ncbi.nlm.nih.gov/articles/4475724)).
- **Clinical relevance.** This circuit underlies menopausal hot flushes and is the rationale for NK3R antagonists such as fezolinetant, approved by the FDA in 2023. Because mouse NK3R binds these antagonists less well (Sarau 2001), higher doses are needed in mouse studies.

### 4.3 Other central roles (moderate to weak support, pleiotropic)

- **Learning and memory.** *Tacr3*⁻/⁻ mice show deficits in passive avoidance, acquisition of conditioned avoidance responding and the Morris water maze. Locomotor activity, elevated plus maze, forced swim and hot-plate results were normal (Siuciak et al., *Psychopharmacology* 2007; [doi:10.1007/s00213-007-0828-6](https://dx.doi.org/10.1007/s00213-007-0828-6)).
- **Locomotion.** An independent knockout line showed mild hyperlocomotion and rotarod deficits (Nordquist et al.; [Utrecht thesis chapter](https://dspace.library.uu.nl/bitstream/handle/1874/32144/56.pdf?sequence=1)).
- **Dopamine and psychostimulants.** NK3R modulates midbrain dopamine neurons. The mouse rows "response to cocaine", "conditioned place preference" and "regulation of dopamine metabolic process" are ISO transfers, mainly from rat pharmacology.
- **Airway inflammation.** NK3R deficiency does not inhibit pulmonary eosinophilia in allergic mice (*Pharmacol Res* 2004, PMID 15501700). That is a negative result for an inflammatory role.
- **Cardiovascular, drinking and feeding.** "Positive regulation of blood pressure", "positive regulation of heart rate", "drinking behavior" and "regulation of feeding behavior" are rat-derived ISO rows from central senktide injection. I found no mouse genetic evidence for them.
- **Sperm motility.** "Positive regulation of flagellated sperm motility" and "sperm midpiece" (IBA/ISO) rest on human and rat sperm work showing NK3R on the midpiece and NKB-enhanced motility. I found no mouse-specific data, and *Tacr3*⁻/⁻ males are fertile.

---

## 5. Summary for curation

| Aspect | Best-supported statement | Evidence basis (mouse) |
|---|---|---|
| Molecular function | Neuromedin K (NKB) receptor activity, GO:0016498; rank order NKB > NKA > SP | Direct: Sarau et al. 2001 (cloned mouse receptor, binding and Ca²⁺ assays in HEK293) |
| Signalling | Gq → PLC tachykinin receptor pathway, GO:0007209; Gs/cAMP coupling less certain | Ca²⁺ mobilisation (mouse); cAMP by ISS from human/rat |
| Location | Plasma membrane, 7-TM; neuronal soma and dendrites | Sequence (7 TM); *Tacr3*-EGFP neurons; somatodendritic subcompartments by ISO from rat |
| Core process | Positive regulation of LH secretion via the KNDy pulse generator | Senktide/LH studies; *Tacr3*⁻/⁻ female subfertility (Yang 2012); redundancy with NK1R/NK2R |
| Core process | Heat dissipation via MnPO NK3R neurons | Ablation and senktide studies in mice (Krajewski-Hall 2019 and related work) |
| Non-core | Learning and memory, locomotion, dopamine modulation | Knockout behaviour (Siuciak 2007; Nordquist) |
| Weak / likely over-annotated in mouse | Blood pressure, heart rate, drinking, vagina development, sperm motility | ISO/IBA transfers from rat and human only |

### Key caveats
1. Most mouse GO rows are ISO, ISS or IBA transfers. The direct experimental record on mouse Tacr3 is mainly pharmacology (Sarau 2001), *Tacr3*-reporter neuroanatomy, and knockout phenotypes.
2. Mouse NK3R binds non-peptide antagonists 10–100-fold less well than human NK3R, so antagonist doses in mouse studies are not directly comparable to human ones.
3. Mouse knockouts show milder reproductive defects than humans, because other tachykinin receptors compensate. Receptor function should not be inferred from the severity of the mouse null phenotype alone.

---

### Sources
- UniProt P47937 record, local copy: `genes/mouse/Tacr3/Tacr3-uniprot.txt`
- Sarau et al. 2001, *Eur J Pharmacol* 413:143–150: https://ouci.dntb.gov.ua/works/4ENVdqOl ; https://pesquisa.bvsalud.org/portal/resource/pt/mdl-11226387
- MGI Tacr3: https://www.informatics.jax.org/marker/MGI:892968 ; X87823: https://www.informatics.jax.org/sequence/X87823
- Krajewski-Hall et al. 2019, *Endocrinology* (mouse MnPO NK3R neurons): https://pmc.ncbi.nlm.nih.gov/articles/PMC6424091
- Mittelman-Smith et al. 2015 (rat MnPO NK3R): https://pmc.ncbi.nlm.nih.gov/articles/4475724
- Review of tachykinin knockouts and reproduction (LJMU): https://researchonline.ljmu.ac.uk/id/eprint/13122/1/509222.pdf
- NKA and puberty in female mice (LJMU): https://researchonline.ljmu.ac.uk/11578/3/Characterization%20of%20the%20role%20of%20NKA%20in%20the%20control%20of%20puberty%20onset%20and%20gonadotropin%20release%20in%20the%20female%20mouse..pdf
- Torres et al. 2021 (ORBi): https://orbi.uliege.be/bitstream/2268/260389/1/Torres%202021.pdf
- Yang et al. 2012, *Endocrinology* 153:1578: https://dbpia.nl.go.kr/endo/article/153/4/1578/2423671
- Siuciak et al. 2007, *Psychopharmacology*: https://dx.doi.org/10.1007/s00213-007-0828-6
- Nordquist et al., NK3 knockout behaviour (Utrecht): https://dspace.library.uu.nl/bitstream/handle/1874/32144/56.pdf?sequence=1

*Verification note:* I recalled Navarro et al. 2009 (KNDy NK3R co-expression in mouse), Dacks et al. 2011, and Kung et al. 2004 (first knockout) from memory, or found them only cited in secondary sources. Check their PMIDs before using them as curation references.

## Citations

1. https://www.informatics.jax.org/sequence/X87823
2. https://www.informatics.jax.org/marker/MGI:892968
3. https://ouci.dntb.gov.ua/works/4ENVdqOl
4. https://pesquisa.bvsalud.org/portal/resource/pt/mdl-11226387
5. https://pmc.ncbi.nlm.nih.gov/articles/PMC6424091
6. https://researchonline.ljmu.ac.uk/id/eprint/13122/1/509222.pdf
7. https://dbpia.nl.go.kr/endo/article/153/4/1578/2423671
8. https://researchonline.ljmu.ac.uk/11578/3/Characterization%20of%20the%20role%20of%20NKA%20in%20the%20control%20of%20puberty%20onset%20and%20gonadotropin%20release%20in%20the%20female%20mouse..pdf
9. https://orbi.uliege.be/bitstream/2268/260389/1/Torres%202021.pdf
10. https://pmc.ncbi.nlm.nih.gov/articles/4475724
11. https://dx.doi.org/10.1007/s00213-007-0828-6
12. https://dspace.library.uu.nl/bitstream/handle/1874/32144/56.pdf?sequence=1