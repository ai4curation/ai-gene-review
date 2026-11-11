---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-30T21:31:14.593557'
end_time: '2026-10-30T21:36:55.730096'
duration_seconds: 341.14
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: VIBCH
  gene_id: VC_1370
  gene_symbol: VC_1370
  uniprot_accession: Q9KS89
  protein_description: 'SubName: Full=GGDEF family protein {ECO:0000313|EMBL:AAF94528.1};'
  gene_info: OrderedLocusNames=VC_1370 {ECO:0000313|EMBL:AAF94528.1};
  organism_full: Vibrio cholerae serotype O1 (strain ATCC 39315 / El Tor Inaba N16961).
  protein_family: Not specified in UniProt
  protein_domains: DGC-Regulatory_Protein. (IPR052163); GGDEF_dom. (IPR000160); HAMP_dom.
    (IPR003660); Nucleotide_cyclase. (IPR029787); Rev_trsase/Diguanyl_cyclase. (IPR043128)
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
  - claude-opus-5-5
  web_search_requests: 4
  num_turns: 16
  total_cost_usd: 1.08105941
  session_id: 9559002d-4e82-4bc0-b84e-7c0388ca3958
  stop_reason: end_turn
  assistant_text_blocks: 3
citation_count: 11
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q9KS89
- **Protein Description:** SubName: Full=GGDEF family protein {ECO:0000313|EMBL:AAF94528.1};
- **Gene Information:** OrderedLocusNames=VC_1370 {ECO:0000313|EMBL:AAF94528.1};
- **Organism (full):** Vibrio cholerae serotype O1 (strain ATCC 39315 / El Tor Inaba N16961).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** DGC-Regulatory_Protein. (IPR052163); GGDEF_dom. (IPR000160); HAMP_dom. (IPR003660); Nucleotide_cyclase. (IPR029787); Rev_trsase/Diguanyl_cyclase. (IPR043128)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "VC_1370" matches the protein description above**
2. **Verify the organism is correct:** Vibrio cholerae serotype O1 (strain ATCC 39315 / El Tor Inaba N16961).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'VC_1370' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **VC_1370** (gene ID: VC_1370, UniProt: Q9KS89) in VIBCH.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

Still researching: I'm pulling the full text of the c-di-GMP receptor screen through Europe PMC.

Several papers mention it. I'll pull the VC1370 passages from each one.

# VC_1370 (UniProt Q9KS89) in *Vibrio cholerae* O1 El Tor N16961: a GGDEF-domain diguanylate cyclase in the inner membrane

## Summary

VC_1370 is a predicted diguanylate cyclase (DGC) embedded in the inner membrane. A DGC makes the bacterial second messenger cyclic di-GMP (c-di-GMP) from two molecules of GTP. The protein's layout runs from a membrane sensor, through a HAMP domain and a coiled-coil linker, to a GGDEF output domain. That layout is typical of DGCs that switch on in response to signals outside the cell.

- **Activity:** there is no published enzyme assay on purified VC_1370. The case for DGC activity rests on four points:
  - an intact catalytic GGDEF site, which I checked residue by residue below;
  - a full set of the conserved residues that bind GTP and metal ions;
  - a report that expressing VC_1370 artificially in *V. cholerae* triggers biofilm formation, which is the usual readout of c-di-GMP production;
  - specific c-di-GMP binding in a genome-wide screen, which is expected from an intact c-di-GMP feedback site.
- **Pathway:** it is one of about 40 enzymes in *V. cholerae* that make or break down c-di-GMP. This network controls the switch between swimming and biofilm formation (Vibrio polysaccharide, VPS).
- **Regulation:** its gene is switched on by several signals. These include quorum sensing (cell-density sensing; strongly induced, but not by direct binding of the regulator HapR), the SOS DNA-damage response, the stress sigma factor RpoS (direct promoter binding), nitric oxide, and fragments of bacterial cell wall (peptidoglycan).

**Identity check:** the locus tag VC1370 / VC_1370 is used consistently in the papers below for this N16961 protein, described as a "GGDEF family protein" or a "putative … GGDEF family protein". The protein has no assigned gene name such as *cdgX*. I found no literature on any other gene with this symbol.

---

## 1. Identity and domain architecture

| Feature | Positions (443 aa, 50.4 kDa) | Basis |
|---|---|---|
| N-terminal hydrophobic segment (likely transmembrane helix 1) | ~9–30 | My Kyte–Doolittle hydropathy scan: windows ≥2.4, e.g. `TLLFIASLLLVGFIAFSLL`. Positive residues just before it (R7, K8) suggest the N-terminus sits inside the cell. |
| Extracellular (periplasmic) region | ~31–164 | About 134 residues lying between the two hydrophobic segments. InterPro detects no domain here. |
| Transmembrane helix 2 | 165–189 | UniProt, predicted by the Phobius tool (ECO:0000256\|SAM:Phobius) |
| HAMP domain | 190–243 | PROSITE PS50885; CDD cd06225 |
| Coiled coil (signalling helix) | 245–272 | UniProt, predicted by the Coils tool |
| GGDEF domain | 300–433 | PROSITE PS50887; Pfam PF00990; SMART SM00267; CDD cd01949 |
| Families | – | InterPro IPR052163 (DGC-regulatory protein), IPR029787 (nucleotide cyclase), IPR043128; PANTHER PTHR46663 (DIGUANYLATE CYCLASE DGCT-RELATED), subfamily SF2 |

UniProt predicts only one transmembrane helix, at 165–189. My hydropathy scan finds a second, equally hydrophobic segment at the N-terminus. Taken together, the likely topology is:

- N-terminus inside the cell, then two membrane-crossing helices around a periplasmic sensor of about 134 residues;
- HAMP domain, linker and GGDEF domain all in the cytoplasm.

That is the standard layout of membrane DGCs with a sensor outside, a HAMP domain and a GGDEF output. In those proteins, a signal sensed in the periplasm is passed through the HAMP domain and coiled-coil linker to the GGDEF domain, which then pairs up into the active two-subunit form. One transcriptome annotation (MAGE) describes VC1370 as a "putative Signal transduction histidine kinase domain, Methyl-accepting chemotaxis domain and GGDEF family protein" in the inner membrane [Krin et al. 2018, BMC Genomics, PMID:29783948]. "Methyl-accepting chemotaxis domain" probably refers to the HAMP/periplasmic sensor region. Current InterPro annotations do not support a chemotaxis-receptor or histidine-kinase activity.

**What the periplasmic domain senses is unknown.**

## 2. Molecular function: c-di-GMP synthesis (diguanylate cyclase, EC 2.7.7.65)

**Reaction:** 2 GTP → cyclic di-3′,5′-GMP + 2 diphosphate, with Mg²⁺ as cofactor. UniProt's Mg²⁺ cofactor line comes only from an automated ARBA rule, so it restates the family-level expectation rather than evidence for this protein.

**Catalytic residues.** I checked the Q9KS89 sequence against the conserved features of active GGDEF domains:

- **Active site (A-site) motif:** `GGDEF` at 349–353, preceded by R347/L348 (`RLGGDEF`). This is the canonical catalytic motif. In inactive "degenerate" GGDEF proteins it is commonly mutated. For comparison, VCA0965 has `AGDEF` and still retains activity [Hunter et al. 2014, BMC Microbiol, PMID:24490592, PMC3974145].
- **Metal- and substrate-binding residues:**
  - `D308-L-D310` (in `FFDLDKFKEIND`), the conserved acidic pair that coordinates metal ions;
  - N316 and D317, plus the `GH…GD` stretch (`NDTKGHEVGD`, 316–325), which bind the guanine base and ribose of GTP;
  - the downstream `RIADEAMY` (411–418) region typical of the end of the domain.
- **Inhibitory feedback site (I-site):** `R340-E-S-D343` (RxxD), five residues before GGDEF, which is the canonical spacing. In active DGCs this site binds c-di-GMP and switches the enzyme off when product builds up.

**Experimental evidence:**

- **c-di-GMP binding.** A screen of the *V. cholerae* ORFeome used DRaCALA, a radioactive filter-binding assay. VC1370 was found in both the His-tagged and His-MBP-tagged libraries:
  - fraction of labelled c-di-GMP bound was 0.45 and 0.30, against 0.03 and 0.02 when unlabelled c-di-GMP competed it off;
  - unlabelled cGMP and GTP did not compete it off (0.51/0.47 and 0.34/0.37), so the binding is specific to c-di-GMP.
  
  The authors classify it as one of three GGDEF-only proteins carrying "the RxxD motif required for c-di-GMP binding (VC1370, VC2370, VCA0965 (CdgF))", a motif present in only 11 of the 37 GGDEF-domain ORFs [Roelofs et al. 2015, PLoS Pathog 11:e1005232, PMID:26506097, https://journals.plos.org/plospathogens/article?id=10.1371/journal.ppat.1005232]. The assay used crude *E. coli* lysates expressing the protein, not purified VC1370. What it shows is binding at the I-site, not catalysis. It still fits with a working, feedback-regulated DGC.
- **Biofilm phenotype when expressed artificially.** A 2025 study states that "a previous study has shown that ectopic expression of vc1370 or vca0848 causes biofilm formation", citing Massie et al. 2012 [PMC11726461, PMID:39753671]. Massie et al. measured c-di-GMP made by seven DGCs, each expressed at eight levels, and correlated it with biofilm formation. They concluded that *V. cholerae* uses "high-specificity" c-di-GMP signalling, meaning individual DGCs are tied to particular outputs rather than to one shared c-di-GMP pool [Massie et al. 2012, PNAS 109:12746–51, PMID:22802636]. I could read only the abstract, which does not list the seven DGCs. I could not confirm whether VC1370's c-di-GMP output was quantified directly.
- **No direct enzyme assay.** I found no assay of purified VC1370 and no published active-site mutants.

**Conclusion:** diguanylate cyclase activity (GO:0052621) is strongly supported by an intact catalytic site, family membership, specific c-di-GMP binding and the biofilm phenotype. Direct biochemical proof is still missing. The PANTHER-based IBA assignment of DGC activity fits this evidence.

## 3. Biological process: c-di-GMP signalling and biofilm control

The *V. cholerae* genome encodes many enzymes that turn c-di-GMP over: about 31 GGDEF, 12 EAL and 10 GGDEF–EAL proteins, plus HD-GYP proteins [review, Diguanylate Cyclases in *V. cholerae*, PMC7642852]. High c-di-GMP does three things:

- it activates the transcription factors VpsR and VpsT, which switch on VPS and matrix genes;
- it represses motility;
- it promotes surface attachment, including through the MSHA pilus.

VC_1370 feeds into this network as a c-di-GMP source that promotes biofilm. Its GO annotations to "c-di-GMP signaling" (GO:0061939) and the broader "signal transduction" (GO:0007165) are appropriate.

### Regulation of *vc1370* transcription

| Signal / regulator | Effect on *vc1370* | Evidence |
|---|---|---|
| Quorum sensing (high cell density) | Strongly induced: "VC1370 is strongly induced by QS (30.1- and 11.9-fold at the late-exponential phase and stationary phase, respectively) but shows no HapR binding." Induction is therefore indirect. | GFP reporter fusions compared between a high-cell-density mutant (ΔluxO) and a low-cell-density mutant (luxO D47E), plus HapR gel-shift assays [Waters et al. 2008, J Bacteriol 190:2527, PMID:18223081, PMC2293178] |
| Autoinducers (CAI-1, AI-2, DPO) | Induced, "in accordance with elevated expression of these genes in luxO deficient V. cholerae" | RNA-seq [Herzog et al. 2019, PMID:30649554, PMC6451090] |
| SOS / DNA damage | Co-expressed with the SOS regulon. Δ*vc1369* and Δ*vc1370* mutants "were less resistant to UV irradiation" | Transcriptomics plus UV survival assays [Krin et al. 2018, PMID:29783948, PMC5963079] |
| RpoS (stress sigma factor) | RpoS binds the *vc1370* promoter directly; it is described as the "SOS-induced VC1370" | ChIP / promoter binding [2025, PMID:40953128, PMC12456836] |
| Nitric oxide | Up more than 2-fold; one of 6 GGDEF genes induced | RNA-seq [2025, PMID:41329732, PMC12704800] |
| Exogenous peptidoglycan (a "danger signal" from lysed cells) | Up within 10 min, alongside *hnoX* and *vca0848*, together with a rise in c-di-GMP and matrix production | RNA-seq [2025, PMID:39753671, PMC11726461] |

**Gene neighbourhood.** The neighbouring gene *vc1369* is annotated as the periplasmic component of an ABC transport system for nitrate, sulfonate or bicarbonate. It is also SOS co-expressed, and its mutant shows the same UV sensitivity [Krin et al. 2018]. The two genes may form a functional unit. No one has tested whether the VC1370 periplasmic sensor responds to that transporter's substrate class.

**Interpretation.** VC_1370 looks like a stress- and density-responsive DGC. It is expressed at high cell density and under DNA-damage, nitrosative and envelope-damage stress, which links those conditions to more c-di-GMP and more matrix production. The UV-sensitivity phenotype is a pleiotropic, high-throughput-level observation. It does not point to a direct role in DNA repair.

## 4. Cellular location

- **Inner (cytoplasmic) membrane:** an integral protein with two membrane-crossing helices and its catalytic domain in the cytoplasm. This rests on:
  - the Phobius-predicted helix at 165–189 and my N-terminal hydropathy result;
  - the HAMP domain, which in this kind of protein only works next to the membrane;
  - the MAGE annotation "Inner membrane protein" [Krin et al. 2018].
- The existing IEA annotation "membrane" (GO:0016020) is correct but general. "Plasma membrane" (GO:0005886) would be the more specific term. No experiment has localised the protein, for example by fractionation or a GFP fusion.

## 5. Existing GO annotations, as background for curation

| GO term | Evidence | Assessment |
|---|---|---|
| GO:0052621 diguanylate cyclase activity | IBA | Supported: intact GGDEF and GTP-binding residues; biofilm on artificial expression |
| GO:0061939 c-di-GMP signaling | IBA | Supported |
| GO:0007165 signal transduction | IEA (InterPro HAMP) | True but general. c-di-GMP signaling is the informative term |
| GO:0016020 membrane | IEA (InterPro HAMP) | True but general. Plasma membrane is better supported |

Possible additional function: specific c-di-GMP binding, from the DRaCALA screen. In active DGCs this binding reflects I-site feedback inhibition rather than a separate receptor role.

## 6. Open questions and suggested experiments

1. **Direct catalysis:** purify the cytoplasmic part of the protein (HAMP–GGDEF, about residues 190–443) and measure c-di-GMP made from GTP by HPLC or LC-MS. Compare with a GGDEF→GGAAF mutant, and test I-site inhibition with an R340A/D343A mutant.
2. **Measured output in cells:** quantify c-di-GMP by LC-MS/MS in the Δ*vc1370* mutant and with inducible expression. Check VPS and biofilm phenotypes, and *vpsL* reporter output, in a background lacking several other DGCs.
3. **Sensor ligand:** identify what the periplasmic sensor (about residues 31–164) binds, using thermal-shift ligand screens. Candidates include the nitrate/sulfonate/bicarbonate substrates suggested by the neighbouring *vc1369* transporter gene, and cell-wall fragments.
4. **Stress coupling:** find out whether the reduced UV survival of Δ*vc1370* depends on c-di-GMP, for example by complementing with the catalytic mutant.

---

## References

- Waters CM, Lu W, Rabinowitz JD, Bassler BL (2008). Quorum sensing controls biofilm formation in *Vibrio cholerae* through modulation of cyclic di-GMP levels and repression of *vpsT*. *J Bacteriol* 190:2527–2536. PMID:18223081. https://pmc.ncbi.nlm.nih.gov/articles/PMC2293178/
- Massie JP, et al. (2012). Quantification of high-specificity cyclic diguanylate signaling. *PNAS* 109:12746–12751. PMID:22802636. https://pmc.ncbi.nlm.nih.gov/articles/PMC3411991 (abstract only read)
- Hunter JL, et al. (2014). The *Vibrio cholerae* diguanylate cyclase VCA0965 has an AGDEF active site and synthesizes cyclic di-GMP. *BMC Microbiol* 14:22. PMID:24490592. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3974145/
- Roelofs KG, et al. (2015). Systematic identification of cyclic-di-GMP binding proteins in *Vibrio cholerae* reveals a novel class of cyclic-di-GMP-binding ATPases associated with type II secretion systems. *PLoS Pathog* 11:e1005232. PMID:26506097. https://journals.plos.org/plospathogens/article?id=10.1371/journal.ppat.1005232
- Krin E, et al. (2018). Expansion of the SOS regulon of *Vibrio cholerae* through extensive transcriptome analysis and experimental validation. *BMC Genomics* 19:373. PMID:29783948. https://pmc.ncbi.nlm.nih.gov/articles/PMC5963079/
- Herzog R, et al. (2019). Three autoinducer molecules act in concert to control virulence gene expression in *Vibrio cholerae*. *Nucleic Acids Res*. PMID:30649554. https://pmc.ncbi.nlm.nih.gov/articles/PMC6451090/
- (2025) Bacteria use exogenous peptidoglycan as a danger signal to trigger biofilm formation. PMID:39753671. https://pmc.ncbi.nlm.nih.gov/articles/PMC11726461/
- (2025) Parallel regulatory circuits orchestrate biofilm formation in response to c-di-GMP levels and growth phase. PMID:40953128. https://pmc.ncbi.nlm.nih.gov/articles/PMC12456836/
- (2025) Nitric oxide promotes rapid development of motility to accelerate biofilm dispersal in *Vibrio cholerae*. PMID:41329732. https://pmc.ncbi.nlm.nih.gov/articles/PMC12704800/
- Review: Diguanylate cyclases in *Vibrio cholerae*: essential regulators of lifestyle switching (2020). https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7642852/
- UniProt Q9KS89 (local file `genes/VIBCH/VC_1370/VC_1370-uniprot.txt`); InterPro, PROSITE and Pfam cross-references as listed. Wikidata Q23435779: https://www.wikidata.org/wiki/Q23435779

**Method notes:**
- I read full texts through the Europe PMC open-access API and searched them for VC1370. The Massie 2012 full text was not accessible, and PMC pages blocked automated fetching with a reCAPTCHA check.
- The motif positions and the N-terminal transmembrane prediction come from my own analysis of the UniProt sequence. They were not taken from published studies.

## Citations

1. https://journals.plos.org/plospathogens/article?id=10.1371/journal.ppat.1005232
2. https://pmc.ncbi.nlm.nih.gov/articles/PMC2293178/
3. https://pmc.ncbi.nlm.nih.gov/articles/PMC3411991
4. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3974145/
5. https://pmc.ncbi.nlm.nih.gov/articles/PMC5963079/
6. https://pmc.ncbi.nlm.nih.gov/articles/PMC6451090/
7. https://pmc.ncbi.nlm.nih.gov/articles/PMC11726461/
8. https://pmc.ncbi.nlm.nih.gov/articles/PMC12456836/
9. https://pmc.ncbi.nlm.nih.gov/articles/PMC12704800/
10. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7642852/
11. https://www.wikidata.org/wiki/Q23435779