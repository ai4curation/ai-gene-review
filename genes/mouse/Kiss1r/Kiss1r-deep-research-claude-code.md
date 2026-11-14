---
provider: claude_code
model: redacted
cached: false
start_time: '2026-11-13T23:19:10.780462'
end_time: '2026-11-13T23:21:40.838514'
duration_seconds: 150.06
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: mouse
  gene_id: Kiss1r
  gene_symbol: Kiss1r
  uniprot_accession: Q91V45
  protein_description: 'RecName: Full=KiSS-1 receptor; Short=KiSS-1R; AltName: Full=G
    protein-coupled receptor 54; AltName: Full=G protein-coupled receptor OT7T175;
    Short=mOT7T175; AltName: Full=Kisspeptins receptor; AltName: Full=Metastin receptor;'
  gene_info: Name=Kiss1r; Synonyms=Gpr54;
  organism_full: Mus musculus (Mouse).
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
  models_used: redacted
  web_search_requests: 4
  num_turns: 18
  total_cost_usd: 0.9732409
  session_id: 7d940617-b60e-4d09-ac9f-638c215428a9
  stop_reason: end_turn
  permission_denials: 3
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
- **UniProt Accession:** Q91V45
- **Protein Description:** RecName: Full=KiSS-1 receptor; Short=KiSS-1R; AltName: Full=G protein-coupled receptor 54; AltName: Full=G protein-coupled receptor OT7T175; Short=mOT7T175; AltName: Full=Kisspeptins receptor; AltName: Full=Metastin receptor;
- **Gene Information:** Name=Kiss1r; Synonyms=Gpr54;
- **Organism (full):** Mus musculus (Mouse).
- **Protein Family:** Belongs to the G protein-coupled receptor 1 family.
- **Key Domains:** GPCR_Rhodpsn. (IPR000276); GPCR_Rhodpsn_7TM. (IPR017452); KiSS_1_rcpt. (IPR008103); 7tm_1 (PF00001)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Kiss1r" matches the protein description above**
2. **Verify the organism is correct:** Mus musculus (Mouse).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Kiss1r' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Kiss1r** (gene ID: Kiss1r, UniProt: Q91V45) in mouse.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

Checking the cached papers locally first, then a few targeted web searches.

I have what I need from the cached papers and searches; here is the report.

# Kiss1r (GPR54), the kisspeptin receptor, in mouse (*Mus musculus*): functional research report

**UniProt:** Q91V45 (KISSR_MOUSE) · **Gene:** *Kiss1r* (synonym *Gpr54*) · **Family:** rhodopsin-like class A G protein-coupled receptor (GPCR) family 1 (IPR000276, IPR017452, PF00001), with a KiSS-1 receptor family signature (IPR008103)

## 0. Identity check

The symbol *Kiss1r*/*Gpr54*, the protein name (KiSS-1 receptor, also called the metastin or kisspeptin receptor), the organism (*Mus musculus*) and the family (seven-transmembrane class A GPCR) all match the mouse literature below. The symbol is not ambiguous. Every primary study cited here works on this receptor, either in mice or in cells carrying the mouse receptor. Where an inference comes from human KISS1R, the report says so.

## 1. Summary

Kiss1r is a cell-surface class A GPCR. Its ligands are the kisspeptins, the C-terminally amidated RF-amide peptides cut from the *Kiss1* precursor: kisspeptin-54/metastin, -14, -13 and -10.

- **Core role:** it is the receptor on hypothalamic gonadotropin-releasing hormone (GnRH) neurons that lets kisspeptin drive GnRH secretion. That makes it the main gate of the hypothalamic–pituitary–gonadal (HPG) axis, needed for puberty and fertility.
- **Main signalling route:** the receptor couples to Gαq/11. This activates phospholipase C-β (PLCβ), which hydrolyses PIP2 to IP3 and DAG. IP3 receptors then release Ca²⁺.
- **Effect on the neuron:** downstream, TRPC-like non-selective cation channels open and inward-rectifier K⁺ (Kir) channels close. The GnRH neuron depolarises and fires for a prolonged period.
- **Second route:** a Gαq/11-independent, β-arrestin-dependent route activates ERK1/2.
- **Location within the cell:** on GnRH neurons the receptor is enriched in primary cilia, which boost signalling.
- **Bone:** a newer, non-neuronal role has been described in osteoclasts. Ligand-bound Kiss1r uses its C-terminus as a scaffold to recruit SRC and the phosphatase DUSP18. DUSP18 then dephosphorylates SRC at Tyr416, which restrains osteoclast activity and bone loss.

## 2. Molecular function

### 2.1 Ligand recognition and receptor activity

- **Cloning and first characterisation.** Mouse Kiss1r was identified together with mouse *Kiss1*. Mouse and human kisspeptins are only 52% identical overall, but the active C-terminal decapeptide (Kp-10) is highly conserved. The two differ by one conservative residue: "[Tyr (Y) to Phe (F)]" [PMID:12359743, Mol Cell Biol / BBRC 2002, "Identification and characterization of mouse metastasis-suppressor KiSS1 and its G-protein-coupled receptor"].
  - The same study found that "Activation of the receptor by KiSS1 peptide leads to the activation of G-protein-activated phospholipase C (PLC-beta), which suggests direct coupling of the KiSS1 peptide to the Galphaq-mediate PLC-Ca2+ signaling pathway" [PMID:12359743].
  - This is the main experimental basis for **G protein-coupled peptide receptor activity (GO:0008528)** and **neuropeptide receptor activity (GO:0008188)**.
- **Kisspeptin works only through this receptor in vivo.** Peripheral kisspeptin raises gonadotropins in wild-type mice and has no effect in *Gpr54⁻/⁻* mice. The authors conclude that "kisspeptin acts directly and uniquely by means of GPR54" and that the effect on the HPG axis "occurs directly at the level of GnRH neurons" [PMID:15665093, Messager et al., PNAS 2005, "Kisspeptin directly stimulates gonadotropin-releasing hormone release via G protein-coupled receptor 54"].
- **Same ligand–receptor pair, confirmed by genetics.** *Kiss1*-null and *Gpr54*-null mice have almost the same hypogonadotropic phenotype. This "provides direct proof that kisspeptins are the true physiological ligand for the GPR54 receptor in vivo" (d'Anglemont de Tassigny et al., PNAS 2007; Lapatto et al., Endocrinology 2007, where *Kiss1⁻/⁻* mice were somewhat less severely affected) [PMID:17563351; Lapatto 2007, https://healthandenvironment.org/docs/Lapatto2007.pdf].

### 2.2 Transducer coupling: Gαq/11 and β-arrestin

**Gαq/11 route (canonical)**
- Human patients carrying loss-of-function mutations produce less inositol phosphate in transfected COS-7 cells. Examples are L148S, R331X and X399R, which "demonstrated a significantly decreased accumulation of inositol phosphate" [PMID:14573733, Seminara et al., NEJM 2003, "The GPR54 gene as a regulator of puberty"].
- In mouse GnRH neurons, blocking PLC or IP3 receptors almost abolishes the kisspeptin response: responders fell "from 80 to 15 and 7%, respectively" [PMID:18483150, Liu et al., Endocrinology 2008].

**β-arrestin route (Gαq/11-independent)**
- In mice lacking β-arrestin-1 or β-arrestin-2, kisspeptin-induced LH secretion "was significantly diminished relative to wild-type mice (P < .001)" [PMID:25147978, Ahow et al., Endocrinology 2014, "KISS1R signals independently of Gαq/11 and triggers LH secretion via the β-arrestin pathway in the male mouse"].
- The L148S mutant is "strongly uncoupled from Gαq/11" yet still triggers ERK1/2 phosphorylation. That phosphorylation depends on β-arrestin, shown in mouse embryonic fibroblasts lacking β-arrestin-1/2 [PMID:25147978].
- The authors conclude: "KISS1R signals via Gαq/11 and β-arrestin to regulate GnRH secretion" [PMID:25147978].
- This supports annotations for ERK1/2 / MAPK cascade activation, namely positive regulation of ERK1/ERK2 cascade and MAPK cascade. It is a second transducer route, not a separate function.

### 2.3 Scaffold (adaptor) activity in osteoclasts

Li et al. (Nat Commun 2024; erratum 2024) report a non-canonical scaffolding function [PMID:38346942, "Kisspeptin-10 binding to Gpr54 in osteoclasts prevents bone loss by activating Dusp18-mediated dephosphorylation of Src"]:

- "Gpr54 recruits both active Src and the Dusp18 phosphatase at its proline/arginine-rich motif in its C terminus."
- Kp-10 binding also "leads to the up-regulation of Dusp18," and DUSP18 dephosphorylates Src at Tyr416.
- UniProt records that this recruitment depends on receptor activation and proceeds "through a G(q)-dependent signaling pathway." The UniProt SUBUNIT line records the interactions with SRC and DUSP18.

This is the basis for the IDA row for **molecular adaptor activity (GO:0060090)**. The finding comes from one 2024 study and has not been replicated independently. It is best treated as a secondary, tissue-specific function, not the receptor's core activity.

## 3. Cellular location

- **Plasma membrane / cell surface.** The receptor is a seven-transmembrane protein that works at the plasma membrane, and it binds its peptide ligand from outside the cell.
  - In UniProt, the plasma-membrane location of mouse Q91V45 is transferred by similarity from human Q969F8 (ECO:0000250). The multi-pass topology rests on sequence analysis (ECO:0000255).
  - MGI has a direct IDA row for **cell surface (GO:0009986)** (PMID:11414709 or 12359743).
- **Primary cilia of GnRH neurons.** Koemeter-Cox et al. (PNAS 2014;111:10335–10340; PMID:24982149) found that "Kiss1r is enriched in primary cilia on GnRH neurons in the mouse" [https://pmc.ncbi.nlm.nih.gov/articles/PMC4104922; https://www.pubmed.gov/24982149/]. Their other findings:
  - GnRH neurons often carry several Kiss1r-positive cilia, and the share of multiciliated neurons rises with sexual maturation.
  - Removing the cilia did not change GnRH neuron migration or pubertal timing.
  - Without cilia, kisspeptin produced a smaller increase in GnRH neuron firing. The authors conclude that cilia enhance Kiss1r signalling.
  - This is direct mouse evidence for the **cilium (GO:0005929)** location. In GOA that location currently appears only as ISO/ISS rows.
- **Where it is expressed.** In the cloning studies, mouse *Kiss1r* mRNA was highest in heart and in embryos at days 15 and 17, and low elsewhere [PMID:12359743; PMID:11414709]. In the hypothalamus it colocalises with GnRH neurons [PMID:15665093]. Osteoclasts also express it [PMID:38346942].

## 4. Pathways and biological processes

### 4.1 How kisspeptin signals in the GnRH neuron (core pathway)

```
Kisspeptin (from ARC/AVPV Kiss1 neurons)
   ↓ binds
Kiss1r (plasma membrane, enriched on primary cilia of GnRH neurons)
   ├── Gαq/11 → PLCβ → PIP2 → IP3 + DAG
   │       └── IP3R → ↑[Ca²⁺]i
   │              ├── TRPC-like NSCC opening (major)
   │              └── Kir K⁺ channel closure (minor)
   │                     → depolarisation, sustained firing → GnRH release
   └── β-arrestin-1/2 → ERK1/2 phosphorylation → contributes to GnRH/LH secretion
```

- **Electrophysiology.** In acute brain slices, 100 nM kisspeptin depolarised "75% of adult GnRH neurons", raised firing rate by 87%, and raised intracellular Ca²⁺ by about 10%. The authors conclude that kisspeptin "activates G protein-coupled receptor 54 (GPR54) to initiate a PLC-IP3R-calcium cascade that modulates both potassium and NSC channels to initiate depolarization in GnRH neurons" [PMID:18483150].
- **Ion channels.** Zhang et al. (J Neurosci 2008) found that the kisspeptin inward current is blocked by TRPC channel blockers. GnRH neurons express TRPC1 and TRPC3–7. They conclude that "kisspeptin depolarizes GnRH neurons through activating TRPC-like channels and, to a lesser extent, inhibition of Kir channels" [PMID:18434521, "Kisspeptin depolarizes gonadotropin-releasing hormone neurons through activation of TRPC-like cationic channels"].
- **GO terms this supports:** G protein-coupled receptor signalling pathway (GO:0007186); phospholipase C-activating GPCR signalling (GO:0007200); calcium-mediated signalling (GO:0019722); neuropeptide signalling pathway (GO:0007218); and, as a downstream physiological outcome, positive regulation of gonadotropin secretion (GO:0032278).

### 4.2 Physiological role: puberty and fertility

- **Whole-body knockouts.** Two *Gpr54*-null lines were reported in 2003:
  - Seminara et al. described one in NEJM [PMID:14573733]: "The Gpr54-deficient mice had isolated hypogonadotropic hypogonadism." These mice still responded to exogenous GnRH, which places the defect above the pituitary.
  - Funes et al. described the other in BBRC (PMID:14652023, not in the local cache).
  - A later review says the Seminara line was made by Paradigm Therapeutics and the Funes line by Schering-Plough [https://pmc.ncbi.nlm.nih.gov/articles/PMC3473196]. I could not confirm this from the primary papers.
  - Both lines lack sexual maturation and have low gonadotropins, much like human patients with *KISS1R* loss-of-function mutations [PMID:14573733].
- **GnRH-neuron-specific knockouts.**
  - Novaira et al. (Mol Endocrinol 2014;28:225) made a GnRH-neuron-specific deletion ("GKirKO") by crossing floxed *Kiss1r* with *Gnrh-Cre*. Females had delayed puberty and abnormal cycles. Both sexes were infertile, with low LH and FSH [https://academic.oup.com/mend/article/28/2/225/2556171; https://pmc.ncbi.nlm.nih.gov/articles/PMC3896637].
  - An earlier GnRH-specific inactivation by Kirilov et al. (2013) is cited as reproducing hypogonadotropic hypogonadism [https://pmc.ncbi.nlm.nih.gov/articles/PMC4197989]. I could not retrieve the primary Kirilov paper, so its details (including any rescue experiment) are unconfirmed here.
  - Together these show that the HPG-axis function is cell-autonomous to the GnRH neuron.
- **Gonadotroph receptor.** Deleting Kiss1r only in pituitary gonadotrophs lowers FSH in males but leaves fertility normal [Frontiers in Physiology 2022, https://www.frontiersin.org/journals/physiology/articles/10.3389/fphys.2022.868593/epub]. Any pituitary role is therefore minor.

### 4.3 Bone remodelling (non-neuronal)

- Li et al. report that *Kiss1*, *Gpr54* and *Dusp18* knockout mice "all exhibit osteoclast hyperactivation and bone loss." Kp-10 given in vivo "abrogated bone loss by suppressing osteoclast activity" [PMID:38346942].
- This supports **negative regulation of bone resorption (GO:0045779, IMP)**, with the Kiss1r–DUSP18–SRC scaffold as the proposed mechanism. The receptor's actions in other contexts, by contrast, are mostly mediated by Gq/PLC/Ca²⁺.

### 4.4 Other and pleiotropic roles (lower priority)

- **Cell proliferation and migration.** In the original cell-line study, receptor activation "inhibits cell proliferation and cell migration," in keeping with KiSS1's history as a metastasis suppressor [PMID:12359743]. This underlies the ISO row for negative regulation of cell population proliferation. In mouse it is a cell-culture observation, not an established in vivo function.
- **Arachidonic acid release.** Rows for arachidonate secretion (GO:0050482) and positive regulation of hormone secretion are carried over (ISO) from human/rat studies of kisspeptin-stimulated arachidonic acid release in transfected cells. They are downstream readouts of PLC/PLA2 activation.
- **Metabolism.** Female *Kiss1r⁻/⁻* mice become obese in early adulthood even though they eat less. They have lower energy expenditure, hyperleptinemia and impaired glucose tolerance. Ovariectomised knockouts still become obese, so the effect is not just a lack of estrogen [Tolson et al., JCI 2014, https://www.jci.org/articles/view/71075; Tolson et al. 2020, https://pmc.ncbi.nlm.nih.gov/articles/PMC6814569]. This is a systemic phenotype, and which cells mediate it is still under study.

## 5. Evolution and structure

- **Structural family.** Kiss1r is a class A (rhodopsin-like) GPCR. It carries the 7TM_1 domain (PF00001), PROSITE PRU00521, and a KiSS-1 receptor family signature (IPR008103).
- **Relatives.** It is related to the galanin receptors and other neuropeptide/RF-amide peptide receptors. These relatives explain the IBA rows for neuropeptide receptor activity (GO:0008188), neuropeptide signalling (GO:0007218) and plasma membrane.
- **Ligand conservation.** The ligand-binding determinants are conserved, since the active Kp-10 is almost identical between mouse and human [PMID:12359743].
- **C-terminal motif.** The proline/arginine-rich motif in the C-terminal tail, which recruits SRC and DUSP18, has been mapped by mutagenesis [PMID:38346942].
- **Human disease and mutations.** Human disease mutations are informative because their mouse equivalents recapitulate the phenotype:
  - L148S, in intracellular loop 2, uncouples the receptor from Gq but keeps β-arrestin signalling [PMID:14573733; PMID:25147978].
  - R331X and X399R are truncation and extension mutations of the C-terminus [PMID:14573733].

## 6. How the current GO annotations line up with the evidence

| Aspect | Best-supported terms | Evidence |
|---|---|---|
| Molecular function (core) | Kisspeptin receptor activity as a neuropeptide / G protein-coupled peptide receptor (GO:0008188 / GO:0008528) | Direct experimental evidence [PMID:12359743, 15665093]; IBA |
| Molecular function (secondary) | Molecular adaptor activity (GO:0060090), scaffolding SRC and DUSP18 | One study [PMID:38346942] |
| Location | Plasma membrane / cell surface; primary cilium (on GnRH neurons) | Similarity to human plus IDA; cilium shown directly in mouse (PMID:24982149) |
| Process (core) | PLC-activating GPCR signalling → Ca²⁺ → GnRH neuron depolarisation; positive regulation of gonadotropin secretion | [PMID:18483150, 18434521, 14573733, 15665093] |
| Process (secondary) | β-arrestin-mediated ERK1/2 activation; negative regulation of bone resorption | [PMID:25147978]; [PMID:38346942] |
| Process (peripheral) | Arachidonate secretion; negative regulation of cell proliferation | Cell culture / transferred from other species |

The bare protein-binding IPI (GO:0005515) row comes from the SRC/DUSP18 interaction study [PMID:38346942]. It is better captured by the adaptor-activity term.

## 7. Open questions

1. **What cilia add.** It is not known what ciliary localisation contributes beyond amplifying the signal, for example local cAMP/Ca²⁺ microdomains or particular β-arrestin pools (PMID:24982149).
2. **How the two routes div

The last part of the report was withheld, so it stops partway through section 7 (open questions). Sections 0 to 6 above are complete.

The main conclusions:
- **Core function:** Kiss1r is the kisspeptin receptor on the surface of GnRH neurons, a G protein-coupled peptide receptor. Kisspeptin binding starts PLC and Ca²⁺ signalling and opens TRPC-like channels, which depolarises the neuron and drives GnRH and gonadotropin release.
- **Secondary findings:** a β-arrestin route to ERK1/2, and a scaffolding role in osteoclasts that limits bone resorption.
- **Location in the cell:** the receptor is concentrated in the primary cilia of GnRH neurons.

Two primary papers could not be checked: Funes et al. 2003 (PMID:14652023) is not in the local publication cache, and Kirilov et al. 2013 did not come up in searches.

## Sources

**Local cached publications (`publications/`)**
- PMID:12359743, cloning of mouse KiSS1 and its receptor
- PMID:14573733, Seminara et al., NEJM 2003
- PMID:15665093, Messager et al., PNAS 2005
- PMID:18434521, Zhang et al., J Neurosci 2008
- PMID:18483150, Liu et al., Endocrinology 2008
- PMID:25147978, Ahow et al., Endocrinology 2014
- PMID:38346942, Li et al., Nat Commun 2024
- UniProt Q91V45 record (`genes/mouse/Kiss1r/Kiss1r-uniprot.txt`)

**Web**
- [Koemeter-Cox et al. 2014, PNAS (PMC4104922)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4104922)
- [PubMed 24982149](https://www.pubmed.gov/24982149/)
- [Primary cilia enhance kisspeptin receptor signaling (IU ScholarWorks)](https://scholarworks.indianapolis.iu.edu/items/60987791-e324-437c-be64-d8d5045904c8)
- [Novaira et al. 2014, Mol Endocrinol](https://academic.oup.com/mend/article/28/2/225/2556171)
- [Novaira et al. 2014 (PMC3896637)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3896637)
- [Review citing Kirilov 2013 (PMC4197989)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4197989)
- [Gonadotroph Kiss1r knockout, Frontiers in Physiology 2022](https://www.frontiersin.org/journals/physiology/articles/10.3389/fphys.2022.868593/epub)
- [Kiss1-null mice, PubMed 17563351](https://pubmed.ncbi.nlm.nih.gov/17563351/)
- [Lapatto et al. 2007](https://healthandenvironment.org/docs/Lapatto2007.pdf)
- [Review of Gpr54 knockout lines (PMC3473196)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3473196)
- [Tolson et al. 2014, JCI](https://www.jci.org/articles/view/71075)
- [Tolson et al. 2020 (PMC6814569)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6814569)

## Citations

1. https://healthandenvironment.org/docs/Lapatto2007.pdf
2. https://pmc.ncbi.nlm.nih.gov/articles/PMC4104922
3. https://www.pubmed.gov/24982149/
4. https://pmc.ncbi.nlm.nih.gov/articles/PMC3473196
5. https://academic.oup.com/mend/article/28/2/225/2556171
6. https://pmc.ncbi.nlm.nih.gov/articles/PMC3896637
7. https://pmc.ncbi.nlm.nih.gov/articles/PMC4197989
8. https://www.frontiersin.org/journals/physiology/articles/10.3389/fphys.2022.868593/epub
9. https://www.jci.org/articles/view/71075
10. https://pmc.ncbi.nlm.nih.gov/articles/PMC6814569
11. https://scholarworks.indianapolis.iu.edu/items/60987791-e324-437c-be64-d8d5045904c8
12. https://pubmed.ncbi.nlm.nih.gov/17563351/