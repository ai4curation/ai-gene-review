---
provider: claude_code
model: claude-fable-5-2, claude-haiku-5-5
cached: false
start_time: '2026-11-15T06:58:57.428924'
end_time: '2026-11-15T07:01:03.983514'
duration_seconds: 126.55
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: yeast
  gene_id: HIF1
  gene_symbol: HIF1
  uniprot_accession: Q12373
  protein_description: 'RecName: Full=HAT1-interacting factor 1;'
  gene_info: Name=HIF1; OrderedLocusNames=YLL022C; ORFNames=L1205;
  organism_full: Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
  protein_family: Belongs to the NASP family. .
  protein_domains: NASP-like. (IPR051730); TPR-like_helical_dom_sf. (IPR011990)
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
  - claude-fable-5-2
  - claude-haiku-5-5
  web_search_requests: 6
  num_turns: 21
  total_cost_usd: 2.0173331
  session_id: c42ab495-845b-4431-a84b-ac892d35dfd2
  stop_reason: end_turn
  permission_denials: 3
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
- **UniProt Accession:** Q12373
- **Protein Description:** RecName: Full=HAT1-interacting factor 1;
- **Gene Information:** Name=HIF1; OrderedLocusNames=YLL022C; ORFNames=L1205;
- **Organism (full):** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
- **Protein Family:** Belongs to the NASP family. .
- **Key Domains:** NASP-like. (IPR051730); TPR-like_helical_dom_sf. (IPR011990)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "HIF1" matches the protein description above**
2. **Verify the organism is correct:** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'HIF1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **HIF1** (gene ID: HIF1, UniProt: Q12373) in yeast.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

Still gathering sources — reading the last cached abstract (the 2016 Hif1–histone structure), then I'll write the report.

# HIF1 (YLL022C; UniProt Q12373) in *Saccharomyces cerevisiae*: research report for functional annotation

## 1. Identity verification

The symbol "HIF1" is ambiguous. Most literature under that name concerns mammalian hypoxia-inducible factor 1 (HIF1A/ARNT), which is unrelated and is excluded here.

The target is yeast **Hat1-interacting factor 1** (Hif1p; ORF YLL022C; 385 aa), a NASP-family protein. The literature below matches the UniProt record on all three checks:

- **Name and gene:** the protein was named for its interaction with Hat1, and YLL022C is the ORF named in the founding papers (Ai & Parthun 2004, PMID:15099519).
- **Organism:** all primary studies cited are in *S. cerevisiae*.
- **Family and domains:** Hif1 belongs to the Sim3–Hif1–NASP (SHNi-TPR) family of interrupted tetratricopeptide-repeat proteins, consistent with IPR051730 and IPR011990 (Zhang et al. 2016, PMID:27618665).

I read the abstracts of the 2004 and 2016 primary papers from the repository's publication cache (abstract-only). Other papers are cited from search-result summaries of their abstracts or PMC text, and I did not read their full text.

## 2. Summary

Hif1 is a non-enzymatic, nuclear histone chaperone with a preference for H3–H4. It is the third subunit of the nuclear type B histone acetyltransferase complex (HAT-B, also called NuB4), alongside the catalytic subunit Hat1 and the WD40 protein Hat2.

Its role is to hold newly synthesized H3–H4, acetylated on H4 by Hat1, and pass it toward deposition. It is not an acetyltransferase and does not regulate Hat1 catalysis. On its own it cannot deposit histones onto DNA.

Loss of HIF1 is viable. It causes defects in telomeric silencing and in chromatin reassembly after DNA double-strand break repair, both seen mainly in sensitized genetic backgrounds.

## 3. Molecular function

### 3.1 Histone H3–H4 chaperone

- **Discovery (two-hybrid):** Hif1 was identified as a Hat1- and histone H4-interacting protein, and both interactions required HAT2 (Poveda et al. 2004, J Biol Chem 279:16033, PMID:14761951, https://doi.org/10.1074/jbc.M314228200).
- **Discovery (purification):** the nuclear Hat1p/Hat2p complex copurified with the YLL022C product. The authors reported that "Hif1p is a histone chaperone that selectively interacts with histones H3 and H4" (Ai & Parthun 2004, Mol Cell 14:195, PMID:15099519, https://doi.org/10.1016/s1097-2765(04)00184-4).
- **In vivo cargo:** the nuclear Hat1p/Hat2p/Hif1p complex is bound to acetylated H4 and to H3. Hif1's association with acetylated H4 requires Hat1 and Hat2 (PMID:15099519).
- **Not a catalytic regulator:** "In contrast to Hat2, this novel subunit does not appear to regulate Hat1 enzymatic activity" (PMID:14761951). Hat1 itself acetylates free H4 at K12 and, to a lesser extent, K5.

### 3.2 Chromatin assembly activity

- Hif1 promotes histone deposition only "in the presence of a yeast cytosolic extract" (PMID:15099519).
- A follow-up study confirmed that Hif1 cannot deposit histones by itself. It found that the cooperating factor in the extract was RNA rather than protein, and that sNASP mutations disrupting H3/H4 binding blocked the activity (Knapp et al. 2014, PLoS One, https://pmc.ncbi.nlm.nih.gov/articles/PMC4114455).
- The RNA dependence rests on this single in vitro study; I found no independent replication, and its physiological meaning is unresolved.

### 3.3 Structural basis

- **Hif1 alone (PDB 4NQ0, 2.1 Å):** a superhelical TPR domain with an extended acidic loop covering its rear face. The authors described Hif1 as a scaffold recruiting protein complexes to core histones (Liu et al. 2014, Biochem J, PMID:24946827, https://rcsb.org/structure/4NQ0).
- **Hif1 with H2A–H2B (PDB 5BT1, 2.6 Å):** Hif1 binds the H2A–H2B dimer and the H3–H4 tetramer "via distinct mechanisms", and the authors propose alternate binding of the two (Zhang et al. 2016, Structure 24:1810, PMID:27618665, https://doi.org/10.1016/j.str.2016.08.001).
- **Curated details from UniProt (Q12373), citing those two papers:**
  - Hif1 is a homodimer.
  - An acidic patch in the N-terminal TPR region is important for histone binding.
  - A polar C-terminal region mediates H2A–H2B binding but not H3–H4 binding.
  - H3–H4 tetramer binding precludes H2A–H2B binding.
- **Caveat on H2A–H2B:** this binding is shown in vitro with recombinant proteins. In vivo evidence points to H3–H4 as the physiological cargo, so H2A–H2B chaperoning should be treated as unproven in cells.

### 3.4 Interactions within and beyond HAT-B

- **Hat2 is the bridge.** Hif1 does not bind Hat1 without Hat2 (PMID:14761951), and Hif1 binds Hat2 directly. Asf1 joins HAT-B only through contacts with H3–H4 (Haigney et al. 2015, J Biol Chem, https://pmc.ncbi.nlm.nih.gov/articles/PMC4683284).
- **The TPR2 acidic patch is multifunctional.** It is required for Hif1's interactions with Hat1/Hat2, Asf1 and H3/H4 (Dannah et al. 2018, G3 8:1993, https://pmc.ncbi.nlm.nih.gov/articles/PMC5982827).
- **Nuclear targeting.** A basic patch at the extreme C-terminus is indispensable for proper nuclear localization (Dannah et al. 2018).
- **Spt2.** The same study reports a physical interaction with the transcription-linked chromatin protein Spt2, possibly connecting NuB4 to transcription-associated chromatin reassembly. This is a single report.
- **Hat1-independent pool.** Hif1 also exists in complexes independent of Hat1 and Hat2 and influences an H3-specific acetyltransferase activity (Ge et al. 2011, J Biol Chem, https://pmc.ncbi.nlm.nih.gov/articles/PMC3089522).
- **Handoff model.** A 3.3 Å structure of yeast Hat1–Hat2 with Asf1–H3–H4 led the authors to propose that H3–H4 passes from Hif1/NASP to Asf1 via Hat2 (Yue et al. 2022, Genes Dev 36:408, PMID:35393344, https://genesdev.cshlp.org/content/36/7-8/408.full). That structure lacks Hif1, so the handoff is inferred. I found no structure of an intact Hif1-containing NuB4 complex.

## 4. Localization

- **Nucleus.** Immunofluorescence of tagged Hat1, Hat2 and Hif1 showed that "all three HAT-B proteins are mainly localized in the nucleus" (PMID:14761951).
- **Nuclear form of the complex.** Hat1/Hat2 is found in both cytoplasm and nucleus, and Hif1 copurifies with the nuclear form (PMID:15099519).
- **High-throughput support.** The genome-wide GFP localization study also places Hif1 in the nucleus (Huh et al. 2003, PMID:14562095).
- **Sites of DNA damage.** Hif1 is recruited to an HO-induced double-strand break with a distribution similar to Hat1 (Qin & Parthun 2006, Mol Cell Biol, PMID:16612003, https://pmc.ncbi.nlm.nih.gov/articles/PMC1447429).
- **Telomeres.** The existing "chromosome, telomeric region" annotation is electronic (IEA). It appears to follow from the silencing phenotype, and I found no direct evidence that Hif1 resides at telomeres.
- **Abundance.** About 4,550 molecules per cell in log phase (Ghaemmaghami et al. 2003, PMID:14562106, as cited in UniProt).

## 5. Biological processes

### 5.1 Replication-coupled handling of new H3–H4 (core role)

Hif1's core role is as the H3–H4-binding subunit of nuclear HAT-B, linking type B histone acetylation to chromatin assembly (PMID:15099519). The working model is:

1. Hat1–Hat2 acetylates new H4 on K5/K12.
2. The complex enters the nucleus and associates with Hif1.
3. H3–H4 is passed to Asf1 and onward to deposition factors.

Steps 2–3 rest on interaction data and structural inference (Haigney et al. 2015; Yue et al. 2022), not on direct reconstitution.

### 5.2 Telomeric silencing

- hif1Δ and hat1Δ strains "display similar defects in telomeric silencing and DNA double-strand break repair" (PMID:15099519); Poveda et al. independently found that Hif1 influences telomeric silencing (PMID:14761951).
- The GO annotation to subtelomeric heterochromatin formation is largely by genetic interaction (IGI), which points to a sensitized background. For Hat1 the known sensitizer is H3 N-terminal lysine mutation, but I did not confirm from full text that the Hif1 experiments used the same design.
- The silencing role is best read as a downstream consequence of defective histone supply or assembly. Hif1 is not known to be a structural component of silent chromatin.

### 5.3 Chromatin reassembly after double-strand break repair

- After a break, acetylation rises on all four H4 tail lysines, but only H4K12 acetylation depends on Hat1. Hat1 arrives after H2A S129 phosphorylation and together with Rad52 (Qin & Parthun 2006, PMID:16612003).
- Loss of Hif1 combined with H3 K14/K23 mutation strongly impaired reassembly, resembling asf1Δ. The Hat1/Hif1 role is at least partly redundant with Asf1 (Ge et al. 2011, https://pmc.ncbi.nlm.nih.gov/articles/PMC3089522).
- Summaries of Ge et al. differ on whether Hif1 or Hat1 has the stronger reassembly role. I could not resolve this without the full text.

### 5.4 Buffering soluble histones

Cells lacking HIF1 are sensitive to histone H3 overexpression and are synthetic lethal with deletion of the histone mRNA regulator LSM1 (Dannah et al. 2018, https://pmc.ncbi.nlm.nih.gov/articles/PMC5982827). This fits a role in managing the soluble H3–H4 pool, as proposed for mammalian NASP.

## 6. Evolutionary and comparative context

- Hif1 is the budding yeast NASP homolog. Family members include *S. pombe* Sim3, *Xenopus* N1/N2 and human sNASP/tNASP (PMID:27618665; Dannah et al. 2018).
- Human sNASP has more than one H3–H4 binding mode:
  - With ASF1 present, it mainly recognizes a partially unfolded N-terminal α-helix region of H3.
  - Without ASF1, an additional site in the H3–H4 core becomes available (Liu et al. 2021, Genes Dev 35:1610, https://genesdev.cshlp.org/cgi/content/full/35/23-24/1610).
  - An H3 core-derived peptide binds the groove of the stacked TPR motifs (https://pmc.ncbi.nlm.nih.gov/articles/PMC4838342).
- These human data support, by homology only, the idea that Hif1 and Asf1 can co-chaperone one H3–H4 unit. This has not been shown directly for yeast Hif1.
- Functional transfer from NASP to Hif1 should be made cautiously. NASP's best-characterized role is protecting a soluble H3–H4 reservoir, whereas Hif1's strongest evidence is as a nuclear HAT-B subunit.

## 7. Assessment of existing annotations

| Annotation | Evidence | Assessment |
|---|---|---|
| Histone binding (GO:0042393) | IDA, PMID:15099519, PMID:27618665 | Well supported; H3–H4 is the physiological cargo |
| Histone acetyltransferase complex (GO:0000123) | IDA/IPI/IMP, PMID:14761951, PMID:15099519 | Well supported; Hif1 is a non-catalytic subunit |
| Nucleus (GO:0005634) | IDA and HDA | Well supported |
| Nucleosome assembly (GO:0006334) | IDA, PMID:15099519 | Supported in vitro, but only with extract (RNA-dependent in one study) |
| Subtelomeric heterochromatin formation (GO:0031509) | IDA/IGI | Real phenotype, probably indirect |
| Protein homodimerization (GO:0042803) | IPI, PMID:27618665 | Structural observation; in vivo relevance unclear |
| Chromosome, telomeric region (GO:0000781) | IEA | No direct localization evidence found |
| Protein binding (GO:0005515) | IPI, mostly interactome screens | Uninformative; partners are Hat2 and histone H4 per IntAct |

No catalytic activity has been reported for Hif1, and none is expected from its TPR-only architecture.

## 8. Open questions

- What is the structure of intact NuB4 (Hat1–Hat2–Hif1) with H3–H4, and how is the cargo handed to Asf1?
- Is the RNA dependence of Hif1-mediated assembly physiological?
- What is the Hat1-independent Hif1 complex, and which H3 acetyltransferase does it influence?
- Does Hif1 bind H2A–H2B in vivo?
- Does the Spt2 interaction reflect a role in transcription-coupled histone recycling?

## 9. Sources

Primary literature (PMIDs taken from the UniProt record and the repository's cached publications):

- Poveda A et al. (2004) J Biol Chem 279:16033–43. PMID:14761951. https://doi.org/10.1074/jbc.M314228200
- Ai X, Parthun MR (2004) Mol Cell 14:195–205. PMID:15099519. https://doi.org/10.1016/s1097-2765(04)00184-4
- Qin S, Parthun MR (2006) Mol Cell Biol. PMID:16612003. https://pmc.ncbi.nlm.nih.gov/articles/PMC1447429
- Ge Z et al. (2011) J Biol Chem, "Nuclear Hat1p complex (NuB4) components participate in DNA repair-linked chromatin reassembly". https://pmc.ncbi.nlm.nih.gov/articles/PMC3089522
- Liu H et al. (2014) Biochem J. PMID:24946827. https://doi.org/10.1042/bj20131640 ; PDB https://rcsb.org/structure/4NQ0
- Knapp AR et al. (2014) PLoS One, "The yeast histone chaperone Hif1p functions with RNA in nucleosome assembly". https://pmc.ncbi.nlm.nih.gov/articles/PMC4114455
- Haigney A et al. (2015) J Biol Chem, HAT-B histone chaperone dissection. https://pmc.ncbi.nlm.nih.gov/articles/PMC4683284
- Zhang M et al. (2016) Structure 24:1810–20. PMID:27618665. https://doi.org/10.1016/j.str.2016.08.001
- Dannah NS et al. (2018) G3 8:1993–2006. https://pmc.ncbi.nlm.nih.gov/articles/PMC5982827 (doi:10.1534/g3.118.200229)
- Liu CP et al. (2021) Genes Dev 35:1610. https://genesdev.cshlp.org/cgi/content/full/35/23-24/1610
- Yue Y et al. (2022) Genes Dev 36:408. PMID:35393344. https://genesdev.cshlp.org/content/36/7-8/408.full
- sNASP TPR–H3 peptide study. https://pmc.ncbi.nlm.nih.gov/articles/PMC4838342
- Huh WK et al. (2003) Nature. PMID:14562095. Ghaemmaghami S et al. (2003) Nature. PMID:14562106.

Databases:

- UniProt Q12373 (function, subunit, domain and localization comments).
- SGD locus page: https://www.yeastgenome.org/locus/HIF1

Author names for Knapp, Haigney, Yue and Liu CP, and the first initials for Ge and Dannah, are from memory rather than from the retrieved pages; check them before reuse. I found no Hif1-specific primary papers from 2023–2024 beyond interactome datasets (e.g. Michaelis et al. 2023, Nature, PMID:37968396, which supplies protein-binding rows only).

## Citations

1. https://doi.org/10.1074/jbc.M314228200
2. https://doi.org/10.1016/s1097-2765(04
3. https://pmc.ncbi.nlm.nih.gov/articles/PMC4114455
4. https://rcsb.org/structure/4NQ0
5. https://doi.org/10.1016/j.str.2016.08.001
6. https://pmc.ncbi.nlm.nih.gov/articles/PMC4683284
7. https://pmc.ncbi.nlm.nih.gov/articles/PMC5982827
8. https://pmc.ncbi.nlm.nih.gov/articles/PMC3089522
9. https://genesdev.cshlp.org/content/36/7-8/408.full
10. https://pmc.ncbi.nlm.nih.gov/articles/PMC1447429
11. https://genesdev.cshlp.org/cgi/content/full/35/23-24/1610
12. https://pmc.ncbi.nlm.nih.gov/articles/PMC4838342
13. https://doi.org/10.1042/bj20131640
14. https://www.yeastgenome.org/locus/HIF1