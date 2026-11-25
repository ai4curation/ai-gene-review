---
provider: claude_code
cached: false
start_time: '2026-11-13T23:43:34.381108'
end_time: '2026-11-13T23:46:06.450139'
duration_seconds: 152.07
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: mouse
  gene_id: Kiss1
  gene_symbol: Kiss1
  uniprot_accession: Q6Y4S4
  protein_description: 'RecName: Full=Metastasis-suppressor KiSS-1; AltName: Full=Kisspeptin-1;
    Contains: RecName: Full=Metastin; AltName: Full=Kisspeptin-52; Contains: RecName:
    Full=Kisspeptin-10; AltName: Full=Metastin45-54; Flags: Precursor;'
  gene_info: Name=Kiss1;
  organism_full: Mus musculus (Mouse).
  protein_family: Belongs to the KISS1 family. .
  protein_domains: Metastasis-suppressor_KiSS-1. (IPR020207); Kisspeptin (PF15152)
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
  web_search_requests: 8
  num_turns: 12
  total_cost_usd: 0.8722573000000001
  session_id: 8668f247-acad-4aca-8534-112dee2cd796
  stop_reason: end_turn
  assistant_text_blocks: 3
citation_count: 19
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q6Y4S4
- **Protein Description:** RecName: Full=Metastasis-suppressor KiSS-1; AltName: Full=Kisspeptin-1; Contains: RecName: Full=Metastin; AltName: Full=Kisspeptin-52; Contains: RecName: Full=Kisspeptin-10; AltName: Full=Metastin45-54; Flags: Precursor;
- **Gene Information:** Name=Kiss1;
- **Organism (full):** Mus musculus (Mouse).
- **Protein Family:** Belongs to the KISS1 family. .
- **Key Domains:** Metastasis-suppressor_KiSS-1. (IPR020207); Kisspeptin (PF15152)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Kiss1" matches the protein description above**
2. **Verify the organism is correct:** Mus musculus (Mouse).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Kiss1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Kiss1** (gene ID: Kiss1, UniProt: Q6Y4S4) in mouse.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

Now writing the report. First, a quick check of the sequence features in the local UniProt record.

# Mouse Kiss1 (UniProt Q6Y4S4): Research Report

## 0. Identity check

- **Target:** *Kiss1*, *Mus musculus*. UniProt Q6Y4S4 calls it "Metastasis-suppressor KiSS-1 / Kisspeptin-1". It belongs to the KISS1 family and carries the Kisspeptin domain (Pfam PF15152; InterPro IPR020207).
- **Match with the literature:** The symbol "Kiss1" in mouse refers to exactly this kisspeptin precursor. Everything below concerns that gene. Nothing found here is about a different gene with a similar symbol.
- **Receptor naming:** The receptor is a separate gene, *Kiss1r* (also called *Gpr54*). Where receptor-knockout data are used, this report says so explicitly.

---

## 1. Summary

Mouse *Kiss1* makes a secreted neuropeptide precursor, not an enzyme, transporter or structural protein.

- **Processing:** The precursor is cut into C-terminally amidated peptides called kisspeptins:
  - metastin, also called kisspeptin-52 (residues 68–119);
  - kisspeptin-10 (residues 110–119).
- **Molecular function:** The kisspeptins are ligands, acting like hormones or neuropeptides, for the Gq-coupled receptor KISS1R/GPR54.
- **Main physiological role:** Hypothalamic kisspeptin neurons act directly on GnRH neurons and are the key excitatory input driving GnRH and LH secretion. This underlies puberty, estrous cyclicity and the preovulatory surge. The neurons sit in two places:
  - the arcuate nucleus (ARC), where the KNDy neurons form the GnRH pulse generator;
  - the anteroventral periventricular / rostral periventricular region (AVPV/RP3V), which mediates the preovulatory LH surge.
- **Knockout phenotype:** Mice lacking *Kiss1* are viable but have hypogonadotropic hypogonadism and do not go through puberty.
- **Secondary roles:** These include inhibiting osteoclast activity through KISS1R–DUSP18–SRC, metabolic effects (shown mostly in receptor knockouts), placental and trophoblast functions, and the anti-metastatic and anti-migratory activities that gave the gene its name. The last two are mostly inferred from human data.

---

## 2. Gene product: structure and processing

| Feature (UniProt Q6Y4S4) | Position | Notes |
|---|---|---|
| Signal peptide | 1–19 | Predicted (ECO:0000255). Directs the protein into the secretory pathway. |
| Precursor chain | 20–130 | "Metastasis-suppressor KiSS-1" |
| Metastin / kisspeptin-52 | 68–119 | Mouse equivalent of human kisspeptin-54 |
| Kisspeptin-10 | 110–119 | Shortest fully active C-terminal fragment |
| C-terminal Tyr-amide | Tyr119 | Amidation is needed for receptor activation |
| Phosphotyrosine | Tyr110 | Annotated modified residue |
| Isoform 2 | Δ25–28 | Splice variant; no known functional difference |

The full precursor is 130 aa (14.1 kDa).

**What this means for function:**

- **Shared active core.** All the bioactive kisspeptins share the C-terminal RF-amide-type motif, which in rodents ends in Tyr-NH₂ (Phe-NH₂ in human). This C-terminal decapeptide is enough to bind and activate the receptor. Mouse kisspeptin-52, "KiSS-1 (68–119)-NH₂ (mouse)/metastin (1–52)", and kisspeptin-10 are equally potent at GPR54 in vitro. C-terminal amidation is required for the Ca²⁺ response ([PMC545088](https://pmc.ncbi.nlm.nih.gov/articles/PMC545088); Messager et al., PNAS 2005, PMID:15665093).
- **Discovery of the ligand.** The endogenous GPR54 ligand (metastin/kisspeptin) was identified in 2001 by three independent groups: Kotani, Muir and Ohtaki. Ohtaki's group purified it from human placenta ([Springer review](https://springerlink.bibliotecabuap.elogim.com/content/pdf/10.1007/400_2007_050)).
- **Processing enzyme.** Furin cuts the human KISS1 precursor: knocking down furin, but not PCSK5 or PCSK7, blocked processing (Harihar et al., PLoS ONE 2014; human cell lines). I found no direct study of processing of the mouse precursor, so furin's role in mouse is inferred.

**Location:** The protein is secreted, by similarity to the human protein (UniProt). Kisspeptin is released from axon terminals onto GnRH neuron cell bodies, dendrites and median-eminence terminals. It then acts in the extracellular space on KISS1R at the plasma membrane of the target cell. GOA also lists neuronal cell body (GO:0043025) and apical plasma membrane (GO:0016324). These reflect where the peptide was detected (immunoreactivity), not where it acts.

---

## 3. Molecular function: ligand for KISS1R/GPR54

### 3.1 Genetic proof that it is the receptor's ligand

**d'Anglemont de Tassigny et al., PNAS 2007** (PMID:17563351; [PubMed](https://pubmed.ncbi.nlm.nih.gov/17563351/), [PMC1965578](https://pmc.ncbi.nlm.nih.gov/articles/PMC1965578)):

- Targeted *Kiss1* deletion phenocopied *Gpr54*-null mice. The authors present this near-identical phenotype as direct in vivo proof that kisspeptins are the natural ligands of GPR54.
- Mutant females:
  - did not cycle through estrus;
  - had thread-like uteri and small ovaries;
  - produced no mature Graafian follicles.
- Mutant males had small testes, with spermatogenesis arrested mainly at the early haploid spermatid stage (UniProt disruption phenotype).
- The pituitary–gonadal axis below the lesion still worked: exogenous kisspeptin-10 triggered strong LH release ([Endocrine Abstracts](https://www.endocrine-abstracts.org/ea/0014/abstracts/oral-communications/reproductive-endocrinology-ii/ea0014oc111/)).

**Lapatto et al., Endocrinology 2007**, an independent *Kiss1* knockout:

- Both *Kiss1⁻/⁻* and *Gpr54⁻/⁻* mice showed hypogonadotropic hypogonadism, but the *Kiss1⁻/⁻* phenotype was more variable and somewhat milder.
- About half of *Kiss1⁻/⁻* females had gonads as small as those of *Gpr54⁻/⁻* mice. The rest showed persistent vaginal cornification.
- One reading is that some receptor signalling continues without the ligand, or that another ligand or mechanism compensates ([OUCI record](https://ouci.dntb.gov.ua/works/4OQpVxz9); [PDF](https://healthandenvironment.org/docs/Lapatto2007.pdf)).

### 3.2 Signalling downstream of the receptor (in GnRH neurons)

The Gq/11 pathway runs in these steps (UniProt FUNCTION, citing PMID:18434521 and PMID:18483150):

1. Kisspeptin binds KISS1R.
2. Gαq/11 activates PLCβ.
3. PLCβ hydrolyses PIP₂.
4. Intracellular Ca²⁺ rises.

**Electrophysiology (Zhang, Roepke, Kelly & Rønnekleiv, J Neurosci 2008; 28:4423)** ([OHSU record](https://ohsu.elsevierpure.com/en/publications/kisspeptin-depolarizes-gonadotropin-releasing-hormone-neurons-thr-2)):

- Kisspeptin depolarized GnRH neurons with an EC₅₀ of about 2.8 nM and a maximum of about 22.6 mV.
- Two effects combine:
  - inhibition of barium-sensitive inwardly rectifying K⁺ (Kir) channels;
  - activation of Na⁺-dependent non-selective cation channels that behave like TRPC channels (blocked by 2-APB, flufenamic acid and SKF96365).
- Later work showed that activation of TRPC4 in female GnRH neurons needs PIP

I'll pick up from where the report was cut off and finish it, without reproducing the withheld portion.

## 3.2 (continued) Signalling in GnRH neurons

Follow-up work from the same group showed that kisspeptin's activation of TRPC4 channels in female GnRH neurons requires PIP₂ depletion and cSrc tyrosine kinase activation ([OUCI record](https://ouci.dntb.gov.ua/works/4MLjYRY7)). Reviews summarise the consensus mechanism as depolarization driven mainly by TRPC channel opening plus K⁺ channel inhibition ([PMC4459938](https://pmc.ncbi.nlm.nih.gov/articles/PMC4459938)).

A second, Gq-independent arm also exists: β-arrestin–dependent signalling to the MAPK cascade with ERK1/ERK2 phosphorylation (UniProt FUNCTION, citing PMID:25147978). This maps onto the GOA rows for GO:0007200 (phospholipase C-activating GPCR signaling), GO:0007204 (positive regulation of cytosolic calcium) and GO:0043410 (positive regulation of MAPK cascade).

**Molecular function terms that fit the evidence:** GO:0031773 (type 1 galanin receptor binding is *not* appropriate — the correct receptor-binding sense here is kisspeptin receptor binding) and GO:0048018 (receptor ligand activity) capture the primary function; GO:0005515 (protein binding) is uninformative.

---

## 4. Where the gene acts: two hypothalamic populations

**Arcuate nucleus (ARC) — the pulse generator.** ARC *Kiss1* neurons co-express neurokinin B and dynorphin (KNDy neurons). Optogenetic work in freely behaving mice (Clarkson et al., PNAS 2017, "Definition of the hypothalamic GnRH pulse generator in mice") showed that brief activation of ARC kisspeptin neurons generated LH pulses, and 30-minute inhibition suppressed LH pulsatility — identifying this population as the pulse generator ([St Andrews record](https://research-portal.st-andrews.ac.uk/en/publications/definition-of-the-hypothalamic-gnrh-pulse-generator-in-mice/)). Later work established that pulse-generator frequency is the primary determinant of the LH pulse profile, with a non-linear frequency relationship (Han, Cheong, McLennan & Herbison, *Endocrinology*), and that the response depends on cycle stage — 5 Hz sustained stimulation triggered robust LH pulses in estrous mice but only a subtle effect in diestrus (Voliotis et al., *eLife* 2021; [eLife 71252](https://elifesciences.org/articles/71252)).

**AVPV/RP3V — the preovulatory surge.** Smith, Clifton & Steiner (*Endocrinology* 2005, 146:3686) found opposite estradiol regulation in the two populations: ARC *Kiss1* is suppressed by E2 (consistent with negative feedback), AVPV *Kiss1* is stimulated by E2 (consistent with positive feedback). Smith et al. (2006) then showed that most AVPV *Kiss1* neurons co-express Fos coincident with the LH surge, but virtually none on diestrus, supporting an active role in generating the proestrous GnRH/LH surge ([PMC2631352](https://pmc.ncbi.nlm.nih.gov/articles/PMC2631352)). AVPV *Kiss1* expression is sexually dimorphic — higher in females even under identical hormonal conditions — matching the absence of an LH surge in males. Mice lacking kisspeptin signalling show a complete absence of LH surges and GnRH activation even with exogenous estradiol (Dror, Franks & Kauffman, 2013).

**Tissue distribution (UniProt, PMID:12359743, PMID:15217982):** weak in most tissues, highest in lung and 15–17-day embryos; in brain, restricted to the AVPV, periventricular and arcuate nuclei.

**A caveat on necessity.** Mayer & Boehm (*Nat Neurosci* 2011) found that ablating kisspeptin neurons during development left females fertile with puberty intact (though ovaries were smaller), while acute ablation in adults inhibited fertility — suggesting developmental compensation ([summary PDF](https://www.uke.de/dateien/einrichtungen/medizinische-fakult%C3%A4t/paper-of-the-month-pom/pom_2011-05.pdf)). This is contested: a small subset of *Kiss1* neurons survived the ablation, and it is unknown whether those few sufficed to drive fertility ([PMC3713212](https://pmc.ncbi.nlm.nih.gov/articles/PMC3713212)). The genetic nulls remain the stronger evidence for necessity.

---

## 5. Functions outside the reproductive axis

**Bone — a well-defined peripheral mechanism.** Li et al. (*Nat Commun* 2024, PMID:38346942; [PMC10861593](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10861593/)) worked out a direct action on osteoclasts in mouse. Kisspeptin-10 activates GPR54, whose proline/arginine-rich C-terminal motif recruits both active SRC and the phosphatase DUSP18; DUSP18 then dephosphorylates SRC at Tyr416, down-regulating osteoclast differentiation and bone resorption. Kp-10 reduced SRC phosphorylation and resorption in wild-type but not *Gpr54*-knockout osteoclasts. *Kiss1*, *Gpr54* and *Dusp18* knockout mice all showed osteoclast hyperactivation and bone loss, and a bone-targeted Kp-10 variant protected against ovariectomy-induced bone loss. This grounds the GOA row GO:0045779 (negative regulation of bone resorption) in direct mouse evidence, and is notable as a Gq-dependent but non-neuronal action.

**Metabolism.** Tolson et al. (*JCI* 2014; [article](https://www.jci.org/articles/view/71075)) studied *Kiss1r* knockouts, not *Kiss1*: adult females showed higher body weight, leptin and adiposity plus impaired glucose tolerance, with reduced locomotor activity and energy expenditure despite eating less; males were normal. Chronically ovariectomized knockout females still became obese and glucose-intolerant, so the phenotype is not purely a consequence of lost estrogen. Because this is receptor loss, attributing it to *Kiss1* requires care — other KISS1R ligands or constitutive receptor activity could contribute, which is also the most economical reading of the milder *Kiss1⁻/⁻* phenotype in Lapatto et al.

**Metastasis suppression, migration and placentation.** These are the activities that named the gene, but in UniProt they are "By similarity" to human Q15726 rather than mouse-demonstrated: inhibition of cell proliferation and migration, regulation of trophoblast invasion in early pregnancy, and modulation of airway smooth muscle cell migration. GOA carries GO:0008285 (negative regulation of cell population proliferation), GO:0033686 (positive regulation of trophoblast cell migration) and GO:0046697 (decidualization) — all appropriate to treat as inherited or peripheral rather than core mouse function.

**Synapse and sensory roles.** GOA includes GO:0050806 (positive regulation of synaptic transmission), GO:0060112 (generation of ovulation cycle rhythm), GO:0060124 (positive regulation of growth hormone secretion) and GO:1904062 (regulation of cation transmembrane transport) — the last being a good match to the Kir/TRPC electrophysiology above.

---

## 6. Interpretation for annotation

- **Core molecular function:** receptor ligand activity, specifically kisspeptin receptor (KISS1R/GPR54) binding — a secreted neuropeptide agonist. Experimentally grounded in mouse by the knockout phenocopy plus rescue with exogenous Kp-10.
- **Core location:** extracellular space / secreted. Acting at the plasma membrane of the target cell is the receptor's location, not this gene product's.
- **Core processes:** positive regulation of GnRH secretion (GO:0032278) and the GPCR/PLC/Ca²⁺ cascade it initiates (GO:0007186, GO:0007200, GO:0007204); negative regulation of bone resorption (GO:0045779) is a second, mechanistically distinct core process with direct mouse evidence.
- **Non-core or similarity-based:** proliferation, migration, trophoblast, decidualization, growth-hormone and metabolic terms.
- **Open question worth flagging:** nothing I found documents processing of the *mouse* precursor directly. Furin's role is extrapolated from human cell lines, and the functional significance of the annotated Tyr110 phosphorylation is unknown.

---

## Sources

- [Hypogonadotropic hypogonadism in mice lacking a functional Kiss1 gene (PMID:17563351)](https://pubmed.ncbi.nlm.nih.gov/17563351/) · [PMC1965578](https://pmc.ncbi.nlm.nih.gov/articles/PMC1965578) · [conference abstract](https://www.endocrine-abstracts.org/ea/0014/abstracts/oral-communications/reproductive-endocrinology-ii/ea0014oc111/)
- [Kiss1−/− Mice Exhibit More Variable Hypogonadism than Gpr54−/− Mice](https://ouci.dntb.gov.ua/works/4OQpVxz9) · [PDF](https://healthandenvironment.org/docs/Lapatto2007.pdf)
- [Kisspeptin depolarizes GnRH neurons through TRPC-like cationic channels (Zhang et al. 2008)](https://ohsu.elsevierpure.com/en/publications/kisspeptin-depolarizes-gonadotropin-releasing-hormone-neurons-thr-2) · [TRPC4/PIP₂/cSrc follow-up](https://ouci.dntb.gov.ua/works/4MLjYRY7) · [review, PMC4459938](https://pmc.ncbi.nlm.nih.gov/articles/PMC4459938)
- [Definition of the hypothalamic GnRH pulse generator in mice (Clarkson et al. 2017)](https://research-portal.st-andrews.ac.uk/en/publications/definition-of-the-hypothalamic-gnrh-pulse-generator-in-mice/) · [Voliotis et al., eLife 2021](https://elifesciences.org/articles/71252)
- [AVPV/ARC estradiol regulation and the LH surge (Smith et al.)](https://pmc.ncbi.nlm.nih.gov/articles/PMC2631352) · [Regulation of Kiss1 expression in female mouse brain](https://digital.lib.washington.edu/researchworks/handle/1773/4389)
- [Kisspeptin-10 binding to Gpr54 in osteoclasts prevents bone loss via Dusp18-mediated dephosphorylation of Src (Nat Commun 2024)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10861593/) · [PDF](https://www.nature.com/articles/s41467-024-44852-9.pdf)
- [Impaired kisspeptin signaling decreases metabolism and promotes glucose intolerance (Tolson et al., JCI 2014)](https://www.jci.org/articles/view/71075)
- [Kisspeptin peptide pharmacology / Messager et al. PNAS 2005](https://pmc.ncbi.nlm.nih.gov/articles/PMC545088) · [GPR54 and Kisspeptins review](https://springerlink.bibliotecabuap.elogim.com/content/pdf/10.1007/400_2007_050)
- [Kiss1 neuron ablation and developmental compensation (Mayer & Boehm 2011; critique)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3713212)
- UniProt Q6Y4S4 and `genes/mouse/Kiss1/Kiss1-goa.tsv` (local repository files)

## Citations

1. https://pmc.ncbi.nlm.nih.gov/articles/PMC545088
2. https://springerlink.bibliotecabuap.elogim.com/content/pdf/10.1007/400_2007_050
3. https://pubmed.ncbi.nlm.nih.gov/17563351/
4. https://pmc.ncbi.nlm.nih.gov/articles/PMC1965578
5. https://www.endocrine-abstracts.org/ea/0014/abstracts/oral-communications/reproductive-endocrinology-ii/ea0014oc111/
6. https://ouci.dntb.gov.ua/works/4OQpVxz9
7. https://healthandenvironment.org/docs/Lapatto2007.pdf
8. https://ohsu.elsevierpure.com/en/publications/kisspeptin-depolarizes-gonadotropin-releasing-hormone-neurons-thr-2
9. https://ouci.dntb.gov.ua/works/4MLjYRY7
10. https://pmc.ncbi.nlm.nih.gov/articles/PMC4459938
11. https://research-portal.st-andrews.ac.uk/en/publications/definition-of-the-hypothalamic-gnrh-pulse-generator-in-mice/
12. https://elifesciences.org/articles/71252
13. https://pmc.ncbi.nlm.nih.gov/articles/PMC2631352
14. https://www.uke.de/dateien/einrichtungen/medizinische-fakult%C3%A4t/paper-of-the-month-pom/pom_2011-05.pdf
15. https://pmc.ncbi.nlm.nih.gov/articles/PMC3713212
16. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10861593/
17. https://www.jci.org/articles/view/71075
18. https://digital.lib.washington.edu/researchworks/handle/1773/4389
19. https://www.nature.com/articles/s41467-024-44852-9.pdf