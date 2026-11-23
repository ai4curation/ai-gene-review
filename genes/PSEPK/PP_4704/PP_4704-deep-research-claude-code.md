---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-30T21:34:01.500590'
end_time: '2026-10-30T21:37:00.361847'
duration_seconds: 178.86
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_4704
  gene_symbol: PP_4704
  uniprot_accession: Q88DW4
  protein_description: 'RecName: Full=DUF748 domain-containing protein {ECO:0008006|Google:ProtNLM};'
  gene_info: OrderedLocusNames=PP_4704 {ECO:0000313|EMBL:AAN70277.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: AsmA-related. (IPR052894); DUF748. (IPR008023); OmpA-like_sf. (IPR036737);
    DUF748 (PF05359)
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
  num_turns: 12
  total_cost_usd: 0.8284684800000002
  session_id: 3058e50b-5bf8-4565-a6ff-68a36d9623e1
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 12
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q88DW4
- **Protein Description:** RecName: Full=DUF748 domain-containing protein {ECO:0008006|Google:ProtNLM};
- **Gene Information:** OrderedLocusNames=PP_4704 {ECO:0000313|EMBL:AAN70277.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** AsmA-related. (IPR052894); DUF748. (IPR008023); OmpA-like_sf. (IPR036737); DUF748 (PF05359)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_4704" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_4704' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_4704** (gene ID: PP_4704, UniProt: Q88DW4) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

Brief update: PP_4704 sits in PANTHER subfamily PTHR30441:SF8 with *E. coli* YicH (AsmA family). Next I'll search the literature on AsmA-like lipid-transport proteins.

# PP_4704 (UniProt Q88DW4), *Pseudomonas putida* KT2440: research report

## 1. Identity check and limits of the evidence

| Item | Value | Source |
|---|---|---|
| Accession | Q88DW4 (TrEMBL, unreviewed), 978 aa, 107.3 kDa | local `PP_4704-uniprot.txt` |
| Locus | PP_4704 (EMBL AAN70277.1; RefSeq WP_010955353.1) | UniProt |
| Organism | *P. putida* KT2440 (taxon 160488) | UniProt |
| Name | "DUF748 domain-containing protein". This name comes from ProtNLM, a machine-learning model (ECO:0008006), and is not curated. | UniProt |
| Protein existence | PE 4, "Predicted" | UniProt |
| Families and domains | InterPro IPR052894 (AsmA-related); IPR008023 / Pfam PF05359 (DUF748); IPR036737 / SUPFAM SSF103088 / Gene3D 3.30.1330.60 (OmpA-like); PANTHER PTHR30441, subfamily **PTHR30441:SF8** | UniProt |
| eggNOG | COG2982 (AsmA) and COG2885 (OmpA family) | UniProt |

The locus tag "PP_4704" is unambiguous. It names one ORF in the KT2440 genome (Nelson et al. 2002, *Environ. Microbiol.* 4:799, PMID:12534463; re-annotation by Belda et al. 2016, PMID:26913973). **I found no publication that studies PP_4704 directly.** The genome papers only report its sequence. Everything below about function is inferred from:
- its domains and family membership;
- experimental work on homologs in *E. coli* and *P. aeruginosa*.

## 2. Family placement: an AsmA-like protein in the YicH subfamily

The local PANTHER family file (`genes/interpro/panther/PTHR30441/`) lists three Swiss-Prot *E. coli* K-12 members of PTHR30441:
- AsmA (P28249, SF4);
- **YicH (P31433, SF8, the same subfamily as PP_4704)**;
- YhjG (P37645, SF9).

A second *P. putida* paralog, PP_4572, is in SF4 ("Protein AsmA").

PTHR30441 is one branch of the bacterial **AsmA-like superfamily**. In *E. coli* this superfamily has six members: TamB, YhdP, YdbH, YhjG, YicH and AsmA. They are thought to be related to the eukaryotic repeating β-groove ("bridge-like") lipid-transfer proteins ([bioRxiv 2025, TamB groove](https://www.biorxiv.org/content/10.1101/2025.03.12.642747.full.pdf); [bioRxiv 2025, polar localization](https://www.biorxiv.org/content/10.1101/2025.04.17.649288.full.pdf)).

The InterPro/PANTHER family description says the family is "implicated in the process of outer membrane protein assembly". That text is LLM-generated and unchecked (`llm: true, checked: false` in the metadata). It reflects the original genetic finding about *E. coli* AsmA, not the current mechanistic model.

## 3. Domain architecture (from the sequence and the signatures above)

1. **N-terminus (about residues 1–35).** A hydrophobic stretch: `…AGAIVALVALYSLLGFLILPGVALRIA…`. This matches the N-terminal transmembrane helix that anchors AsmA-like proteins in the inner membrane. UniProt has no Phobius or TMHMM feature for this segment. This assignment is my reading of the sequence, not an annotated feature.
2. **Central region (about residues 40–800).** The DUF748 / AsmA-related region. In characterized family members this corresponds to the long periplasmic domain. AlphaFold predicts that domain as "extended, tube‑like structures consisting of stacked β‑strands, which create a continuous hydrophobic groove along the long axis" (Sposato et al. 2025, *Protein Sci.* 34:e70227, PMID:40970438). The region also has two disordered, low-complexity segments (333–362 and 556–578; MobiDB-lite).
3. **C-terminus (about residues 830–978).** An OmpA-like fold (SSF103088 / Gene3D 3.30.1330.60). In other proteins this fold usually binds peptidoglycan non-covalently. I have **not** checked whether the canonical peptidoglycan-binding residues are conserved here, so peptidoglycan binding by PP_4704 is not established.

This combination is unusual: an AsmA-like transmembrane anchor and β-groove fused to a C-terminal OmpA-like domain. *E. coli* YicH (569 aa) has no OmpA module. PP_4704 is therefore a longer, Pseudomonas-type variant of the YicH subfamily.

A comparison suggests one possible role for the OmpA-like domain. In *P. aeruginosa* YhdP, C-terminal hydrophobic helices are "crucial for its function" and are proposed to anchor the protein to the outer membrane and/or help insert phospholipids (Sposato et al. 2025). By analogy, the OmpA-like domain of PP_4704 could tether the far end of the bridge to the peptidoglycan/outer-membrane side. This is a **hypothesis only**.

## 4. What the family does: experimental evidence from homologs

**Phospholipid transport to the outer membrane (*E. coli*).**
- YhdP, TamB and YdbH are "redundant but essential". Losing all three is lethal, and any one of them is enough for growth. The authors propose they are the long-sought transporters that move phospholipids from the inner to the outer membrane (Ruiz et al., *mBio*, Dec 2021; [PMC8593681](https://pmc.ncbi.nlm.nih.gov/articles/PMC8593681)).
- Without YhdP, TamB and YdbH, glycerophospholipid transport and cell morphology are defective. Cells release excess outer-membrane vesicles rich in lipopolysaccharide (Douglass, McLean & Trent, *PLoS Genet.*, Feb 2022; [PMC8912898](https://pmc.ncbi.nlm.nih.gov/articles/PMC8912898)).
- YdbH pairs with the outer-membrane lipoprotein YnbE to form a bridge between the inner and outer membranes ([summary](https://academicnewsletter.sufe.edu.cn/info/261913); [CCNY seminar abstract](https://www.ccny.cuny.edu/calendar/biochemistry-seminar-natividad-ruiz-lipid-transporters-build-outer-membrane-gram-negative)).
- Lipids have been shown to traverse the hydrophobic groove of TamB. A preprint reports that all six *E. coli* AsmA-family proteins, including YicH, can hold lipids in their grooves; this is structural and simulation evidence and has not been peer reviewed ([bioRxiv 2025](https://www.biorxiv.org/content/10.1101/2025.03.12.642747.full.pdf)).
- Several of these proteins are mostly found at the cell poles (preprint, [bioRxiv 2025](https://www.biorxiv.org/content/10.1101/2025.04.17.649288.full.pdf)).

**YicH and YhjG specifically.** Neither has been shown to transport lipids in vivo. EcoliWiki lists YhjG as "function unknown" ([EcoliWiki](https://ecoliwiki.org/colipedia/index.php/yhjG:Gene_Product(s)); [PRO P31433](https://proconsortium.org/app/entry/PR:P31433)). The minor members appear to be accessory or redundant, not essential.

**Pseudomonas.**
- *P. aeruginosa* PAO1 encodes seven AsmA-like proteins. Four of them (YhdP, TamB, YdbH and PA4735/EpaF) are "essential yet redundant" for growth and outer-membrane integrity (Sposato et al., *mSphere* 2024, [PMC10900882](https://pmc.ncbi.nlm.nih.gov/articles/PMC10900882/), as cited in Sposato et al. 2025). I could not retrieve the 2024 full text. As a result, I could not confirm which PAO1 protein is the ortholog of PP_4704, or whether that protein is one of the essential four. Being in the YicH subfamily suggests it is probably one of the non-essential members.
- A ΔtamB ΔyhdP ΔydbH mutant shows "extreme sensitivity" to SDS/EDTA and vancomycin. YhdP has the strongest activity in maintaining outer-membrane integrity (Sposato et al. 2025, PMID:40970438, [PMC12447247](https://pmc.ncbi.nlm.nih.gov/articles/PMC12447247)).

**Historical role of AsmA.** *E. coli asmA* was first found as a suppressor of the assembly of defective OmpF (hence "assembly of outer membrane proteins"). asmA mutants also have less lipopolysaccharide ([ASU record](https://asu.elsevierpure.com/en/publications/examination-of-asma-and-its-effect-on-the-assembly-of-escherichia)). The current view is that these effects on outer-membrane proteins are indirect consequences of disturbed outer-membrane lipid homeostasis.

## 5. Synthesis: likely function of PP_4704

- **Molecular function.** Probably a lipid-binding protein with a hydrophobic β-groove that forms an intermembrane bridge for glycerophospholipids. No enzymatic activity is expected. The substrate (glycerophospholipids) is inferred from homologs and has not been tested for PP_4704.
- **Location.** Anchored in the inner (cytoplasmic) membrane by its N-terminal helix, with the large groove domain spanning the periplasm. The C-terminal OmpA-like domain may contact peptidoglycan or the outer membrane.
- **Process.** Probably contributes, likely redundantly with stronger paralogs, to moving phospholipids from the inner to the outer membrane and to outer-membrane biogenesis and integrity.
- **Confidence.** Moderate for family-level lipid transport. Low for any specific role or essentiality of PP_4704 itself.

## 6. Existing GO annotations (local `PP_4704-goa.tsv`, both IEA from TreeGrafter/PANTHER)

| Term | Assessment |
|---|---|
| GO:0005886 plasma membrane (located_in) | Plausible. It is consistent with the predicted N-terminal inner-membrane anchor in this family. |
| GO:0090313 regulation of protein targeting to membrane (involved_in) | Poorly supported. It probably comes from the old AsmA "outer-membrane protein assembly" phenotype. The current model is phospholipid transport, so a term such as "phospholipid transport" or "intermembrane lipid transfer" would describe the family better. Even that would be inferred only from homologs. |

## 7. Open questions and suggested experiments

1. Find the PAO1 ortholog of PP_4704 and check its essentiality and phenotype in the Sposato 2024 dataset. Check KT2440 RB-TnSeq fitness data (Fitness Browser) for PP_4704.
2. Delete PP_4704 alone, and together with the KT2440 orthologs of yhdP, tamB and ydbH. Test sensitivity to SDS/EDTA and vancomycin, NPN uptake, outer-membrane vesicle release and outer-membrane phospholipid content.
3. Predict the AlphaFold structure of the full-length protein to see whether the groove is continuous. Align the OmpA-like domain with OmpA and OprF to check the peptidoglycan-binding residues. Test peptidoglycan binding in vitro.
4. Fractionate membranes or use fluorescent fusions to confirm the inner-membrane anchor and to look for polar localization.

---

**Sources**
- [Ruiz et al. 2021, mBio (PMC8593681)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8593681)
- [Douglass et al. 2022, PLoS Genet (PMC8912898)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8912898)
- [Sposato et al. 2024, mSphere (PMC10900882)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10900882/)
- [Sposato et al. 2025, Protein Sci (PMC12447247; PMID:40970438)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12447247)
- [Bacterial lipids traverse the hydrophobic groove of TamB (bioRxiv 2025)](https://www.biorxiv.org/content/10.1101/2025.03.12.642747.full.pdf)
- [Polar localization of putative phospholipid transporters in *E. coli* (bioRxiv 2025)](https://www.biorxiv.org/content/10.1101/2025.04.17.649288.full.pdf)
- [YdbH and YnbE form an intermembrane bridge (summary)](https://academicnewsletter.sufe.edu.cn/info/261913)
- [Ruiz seminar abstract, CCNY](https://www.ccny.cuny.edu/calendar/biochemistry-seminar-natividad-ruiz-lipid-transporters-build-outer-membrane-gram-negative)
- [EcoliWiki yhjG](https://ecoliwiki.org/colipedia/index.php/yhjG:Gene_Product(s))
- [Protein Ontology PR:P31433 (YicH)](https://proconsortium.org/app/entry/PR:P31433)
- [Examination of AsmA (ASU)](https://asu.elsevierpure.com/en/publications/examination-of-asma-and-its-effect-on-the-assembly-of-escherichia)
- [Sposato et al. 2024 repository listing](https://iris.uniroma3.it/cris/rp/rp93551)
- Local files: `genes/PSEPK/PP_4704/PP_4704-uniprot.txt`, `PP_4704-goa.tsv`, `genes/interpro/panther/PTHR30441/`

## Citations

1. https://www.biorxiv.org/content/10.1101/2025.03.12.642747.full.pdf
2. https://www.biorxiv.org/content/10.1101/2025.04.17.649288.full.pdf
3. https://pmc.ncbi.nlm.nih.gov/articles/PMC8593681
4. https://pmc.ncbi.nlm.nih.gov/articles/PMC8912898
5. https://academicnewsletter.sufe.edu.cn/info/261913
6. https://www.ccny.cuny.edu/calendar/biochemistry-seminar-natividad-ruiz-lipid-transporters-build-outer-membrane-gram-negative
7. https://ecoliwiki.org/colipedia/index.php/yhjG:Gene_Product(s
8. https://proconsortium.org/app/entry/PR:P31433
9. https://pmc.ncbi.nlm.nih.gov/articles/PMC10900882/
10. https://pmc.ncbi.nlm.nih.gov/articles/PMC12447247
11. https://asu.elsevierpure.com/en/publications/examination-of-asma-and-its-effect-on-the-assembly-of-escherichia
12. https://iris.uniroma3.it/cris/rp/rp93551