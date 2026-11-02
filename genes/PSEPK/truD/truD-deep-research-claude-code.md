---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-30T21:11:43.716407'
end_time: '2026-10-30T21:13:10.567129'
duration_seconds: 86.85
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: truD
  gene_symbol: truD
  uniprot_accession: Q88MF2
  protein_description: 'RecName: Full=tRNA pseudouridine synthase D {ECO:0000255|HAMAP-Rule:MF_01082};
    EC=5.4.99.27 {ECO:0000255|HAMAP-Rule:MF_01082}; AltName: Full=tRNA pseudouridine(13)
    synthase {ECO:0000255|HAMAP-Rule:MF_01082}; AltName: Full=tRNA pseudouridylate
    synthase D {ECO:0000255|HAMAP-Rule:MF_01082}; AltName: Full=tRNA-uridine isomerase
    D {ECO:0000255|HAMAP-Rule:MF_01082};'
  gene_info: Name=truD {ECO:0000255|HAMAP-Rule:MF_01082}; OrderedLocusNames=PP_1619;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the pseudouridine synthase TruD family.
  protein_domains: PsdUridine_synth_cat_dom_sf. (IPR020103); PsdUridine_synth_TruD.
    (IPR001656); PsdUridine_synth_TruD_CS. (IPR020119); PsdUridine_synth_TruD_insert.
    (IPR011760); TruD_catalytic. (IPR042214)
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
  num_turns: 7
  total_cost_usd: 0.6129864
  session_id: da8e2811-ee10-4177-81a7-9363093522c9
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 13
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q88MF2
- **Protein Description:** RecName: Full=tRNA pseudouridine synthase D {ECO:0000255|HAMAP-Rule:MF_01082}; EC=5.4.99.27 {ECO:0000255|HAMAP-Rule:MF_01082}; AltName: Full=tRNA pseudouridine(13) synthase {ECO:0000255|HAMAP-Rule:MF_01082}; AltName: Full=tRNA pseudouridylate synthase D {ECO:0000255|HAMAP-Rule:MF_01082}; AltName: Full=tRNA-uridine isomerase D {ECO:0000255|HAMAP-Rule:MF_01082};
- **Gene Information:** Name=truD {ECO:0000255|HAMAP-Rule:MF_01082}; OrderedLocusNames=PP_1619;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the pseudouridine synthase TruD family.
- **Key Domains:** PsdUridine_synth_cat_dom_sf. (IPR020103); PsdUridine_synth_TruD. (IPR001656); PsdUridine_synth_TruD_CS. (IPR020119); PsdUridine_synth_TruD_insert. (IPR011760); TruD_catalytic. (IPR042214)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "truD" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'truD' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **truD** (gene ID: truD, UniProt: Q88MF2) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# truD (PP_1619; UniProt Q88MF2) from *Pseudomonas putida* KT2440: tRNA pseudouridine(13) synthase TruD

## 1. Identity check and scope

| Field | Value (source: UniProt Q88MF2 record, local copy `truD-uniprot.txt`) |
|---|---|
| Gene / locus | *truD* / PP_1619 |
| Organism | *Pseudomonas putida* KT2440 (ATCC 47054 / DSM 6125) |
| Protein | tRNA pseudouridine synthase D (EC 5.4.99.27). Also called tRNA pseudouridine(13) synthase. |
| Length | 352 aa (chain PRO_0000152516) |
| Family | Pseudouridine synthase TruD family (HAMAP MF_01082; Pfam PF01142; PANTHER PTHR47811:SF1) |
| Domains | Ψ-synthase catalytic domain superfamily (IPR020103); TruD (IPR001656); TruD signature (IPR020119); TruD insertion domain (IPR011760, IPR043165); TruD catalytic (IPR042214) |
| Key residue | Active-site nucleophile at Asp81 (`ACT_SITE 81 /note="Nucleophile"`, HAMAP-Rule evidence) |

**The identity checks pass.** The symbol *truD*, the protein name, the family and the InterPro signatures all agree. In bacteria the symbol *truD* refers only to the TruD-family tRNA Ψ13 synthase; no other gene in *P. putida* carries it. One unrelated name is worth noting: in eukaryotes "Pus7" is the TruD-family homolog. This report covers only the TruD-family Ψ synthase.

**Literature on this exact protein is limited.** I found no primary experimental study of *P. putida* PP_1619 itself. Its functional annotation comes from:
- the UniProt HAMAP rule;
- the biochemistry and genetics of *E. coli* TruD, the founding member;
- crystal structures of *E. coli* TruD;
- recent substrate mapping of *Thermus thermophilus* TruD;
- studies of eukaryotic TruD-family Pus7 homologs.

Every functional statement below about PP_1619 is therefore an inference by homology. The family is conserved and carries strong signatures, so the inference is robust for the core catalytic activity. It is less certain for the exact set of tRNA substrates in *Pseudomonas*.

---

## 2. Primary function: reaction and substrate

### 2.1 Reaction catalysed
TruD is an RNA-modifying isomerase. It converts uridine at position 13 of the tRNA D-stem into pseudouridine (Ψ):

> uridine(13) in tRNA = pseudouridine(13) in tRNA (Rhea:RHEA:42540; EC 5.4.99.27)

UniProt Q88MF2 states: "Responsible for synthesis of pseudouridine from uracil-13 in transfer RNAs" (CC FUNCTION, ECO:0000255 | HAMAP-Rule:MF_01082). The reaction is the standard Ψ-synthase isomerization. The uracil base is detached from C1′ of the ribose, rotated 180°, and reattached through its C5, which forms a C–C glycosidic bond. No cofactor or guide RNA is needed, and the enzyme acts alone on the RNA substrate ([Rhea 42540](https://www.rhea-db.org/rhea/42540)).

### 2.2 Discovery of the activity: *E. coli* TruD (YgbO)
- **Kaya & Ofengand (2003, *RNA* 9:711–721; PMID 12756329).** Ten known *E. coli* Ψ synthases accounted for every Ψ in tRNA and rRNA except Ψ13 in tRNA^Glu. Kaya and Ofengand purified the Ψ13-forming activity and identified it as the uncharacterised protein YgbO, which they renamed TruD ([PMC article](https://pmc.ncbi.nlm.nih.gov/articles/pmid/12756329); [EcoliWiki](https://ecoliwiki.org/colipedia/index.php/PMID:12756329)).
- **Genetic test.** Deleting *ygbO* removed Ψ13 from tRNA^Glu, and a plasmid carrying the gene restored it. This establishes TruD as both necessary and sufficient for the modification.
- **A new family.** The authors found 58 TruD homologs across all three domains of life. They concluded that TruD forms a new, widespread class of Ψ synthase with no sequence homology to the four previously known families (TruA, TruB, RluA, RsuA).

### 2.3 Substrate specificity: updated by work in *Thermus*, 2025
- **The *E. coli* paradigm.** Only tRNA^Glu Ψ13 was clearly assigned to TruD.
- **Yamagami et al., 2025 (*RNA* 31(6):850–867).** The authors used PRAISE, a bisulfite-based Ψ mapping method, on wild-type and *truD*-disrupted *T. thermophilus* ([RNA journal](https://rnajournal.cshlp.org/content/31/6/850.full); [abstract](https://rnajournal.cshlp.org/content/31/6/850.short)). They found that:
  - TruD modifies U13 in tRNA^Asp, tRNA^Glu and tRNA^Gln;
  - TruD also modifies **U35 in tRNA^Tyr**, a site previously attributed to RluF in *E. coli*;
  - TruD prefers the sequence **UNUAR**, where the underlined U is the target, N is any nucleotide and R is a purine;
  - in vitro, recombinant TruD modified an mRNA fragment (CDC8), and the authors noted more than 600 ORF fragments carrying this motif. This suggests possible non-tRNA substrates, which have not been confirmed in vivo.
- **Eukaryotic homologs (Pus7).** *S. cerevisiae* Pus7 is a TruD-family enzyme. It makes Ψ13 in cytoplasmic tRNAs, Ψ35 in U2 snRNA and Ψ35 in pre-tRNA^Tyr, and it also acts on mRNA. Its substrate range is therefore broader, but U13 remains the conserved family target (Behm-Ansmant et al. 2003, *RNA*; reviewed in [PMC8794802](https://pmc.ncbi.nlm.nih.gov/articles/PMC8794802) and [NAR 2021, 49:11810](https://academic.oup.com/nar/article/49/20/11810/6413612)). I took the Pus7 details from these later reviews and the Rhea entry, not from the 2003 paper itself.

**Inference for PP_1619.** Its most likely biological substrates are the U13 positions of *P. putida* tRNAs whose D-stem fits the UNUAR-type context, which in *E. coli* means at least tRNA^Glu. Which specific *P. putida* tRNAs are modified is untested. Whether *Pseudomonas* TruD also modifies U35 of tRNA^Tyr or any mRNAs is also unknown.

---

## 3. Structure and catalytic mechanism (from *E. coli* TruD)

Three crystal structures of *E. coli* TruD were published in 2004:

1. **Hoang & Ferré-D'Amaré (2004, *RNA* 10:1026; PMID 15208439)**, at 2.2 Å, PDB 1SB7 ([full text](https://rnajournal.cshlp.org/content/10/7/1026.full); [RCSB 1SB7](https://www.rcsb.org/structure/1SB7)).
   - The molecule is U-shaped, and its catalytic domain superimposes closely on those of other Ψ synthases.
   - The domain's connectivity is a **circular permutation** of the conserved Ψ-synthase fold.
   - The catalytic aspartate sits in the β3–β4 loops. It forms the conserved active-site triad with an aromatic and a basic residue: D80, F131 and K21.
   - The two lobes can flex by about 18°.
2. **Kaya et al. (2004, *J Biol Chem*; PMID 15135053)**, an independent crystal form. It describes a catalytic domain that differs in sequence from other Ψ synthases but is structurally very similar to them. It also has a second large domain with a novel α/β fold, the "TruD insertion domain" ([PubMed 15135053](https://pubmed.ncbi.nlm.nih.gov/15135053); [PDB 1SI7](https://www.rcsb.org/structure/1SI7)).
3. **Ericsson et al. (2004, *FEBS Lett*)**, at 2.0 Å. The protein is V-shaped, with an RNA-binding cleft between the catalytic domain and the insertion domain. The U-shaped versus V-shaped descriptions appear to reflect different crystal forms and the flexibility between domains.

**Mapping to PP_1619.**
- UniProt places the nucleophile of Q88MF2 at **Asp81**, the counterpart of *E. coli* Asp80.
- The TRUD insertion domain spans residues 157–303.
- The domain architecture matches *E. coli* TruD (IPR011760/IPR043165 insertion domain; IPR042214 catalytic domain).

This conservation supports the view that PP_1619 is an active enzyme rather than a catalytically dead paralog. I did not directly check that the conserved Lys and Phe/Tyr residues are present in the *P. putida* sequence; an alignment would be needed to confirm it.

---

## 4. Biological process and pathway context

- **Process.** tRNA pseudouridine synthesis, which falls under tRNA modification and tRNA processing. The specific GO process is "tRNA pseudouridine synthesis" (GO:0031119). The broader "pseudouridine synthesis" (GO:0001522) is less precise.
- **Role of Ψ13.** Ψ13 lies in the D-stem (the 13–22 base pair). Ψ in this region is thought to stiffen the stem through an extra N1-H hydrogen bond, which helps tertiary folding of tRNA. In bacteria TruD is not essential, and *E. coli* Δ*truD* strains grow normally under standard conditions (Kaya & Ofengand 2003). Ψ13 is therefore a fine-tuning modification, not one required for viability.
- **Pathway.** TruD acts on its own; it is not part of a multi-enzyme pathway or complex. It is one of about ten site-specific bacterial Ψ synthases, alongside TruA, TruB, TruC, RluA–F and RsuA.

---

## 5. Cellular localization

TruD has no signal peptide, transmembrane segment or secretion signals. Like all bacterial tRNA-modifying enzymes it is expected to act in the **cytoplasm (cytosol)**, where tRNA maturation takes place. The existing cytosol annotation (GO:0005829, from ECO:0007826) agrees with this. I found no localization experiment specific to *P. putida*.

---

## 6. Existing GO annotations (from `truD-goa.tsv`), with comments

| GO term | Aspect | Evidence | Comment |
|---|---|---|---|
| GO:0160150 tRNA pseudouridine(13) synthase activity | MF | IEA/rule (ECO:0000501) | **Core function.** Supported by HAMAP, family membership and the conserved Asp81 nucleophile. |
| GO:0009982 pseudouridine synthase activity | MF | IEA | Correct but a parent of GO:0160150. |
| GO:0140098 catalytic activity, acting on RNA | MF | IEA (ECO:0000256) | Correct but very general. |
| GO:0003723 RNA binding | MF | IEA (ECO:0000256) | True in that the enzyme binds its substrate; uninformative. |
| GO:0031119 tRNA pseudouridine synthesis | BP | IEA | **Core process.** |
| GO:0001522 pseudouridine synthesis | BP | IEA | Correct; a parent of GO:0031119. |
| GO:0009451 RNA modification | BP | IEA | Correct but general. |
| GO:0006396 RNA processing | BP | IEA | Correct but general. |
| GO:0005829 cytosol | CC | ECO:0007826 | Consistent with what is expected for a tRNA-modifying enzyme. |

No annotation looks wrong. The general terms are all implied by GO:0160150 and GO:0031119.

---

## 7. Summary of core function

PP_1619 (TruD) from *P. putida* KT2440 is a stand-alone, cytoplasmic **tRNA pseudouridine(13) synthase** (EC 5.4.99.27). It converts U13 in the D-stem of a subset of tRNAs into Ψ, using a catalytic Asp nucleophile (Asp81, the counterpart of *E. coli* Asp80). The protein has a circularly permuted Ψ-synthase catalytic domain and a TruD-specific α/β insertion domain that together form the RNA-binding cleft.

| Evidence for this conclusion | Status |
|---|---|
| Family assignment (HAMAP MF_01082, Pfam PF01142, PROSITE TruD signature) | Applies directly to PP_1619 |
| Genetic and biochemical proof of function for the *E. coli* ortholog | Ortholog only |
| Structural conservation of the active site | Ortholog structures; PP_1619 residues mapped by UniProt |
| Substrate mapping in *T. thermophilus*: tRNA^Asp/Glu/Gln U13, tRNA^Tyr U35, UNUAR motif | Ortholog only |
| Direct experiments on the *P. putida* protein | None found |

## 8. Open questions and suggested experiments

1. **Which *P. putida* tRNAs carry Ψ13?** Apply PRAISE or a similar Ψ-mapping method to wild type and a PP_1619 deletion.
2. **Does *P. putida* TruD also modify U35 of tRNA^Tyr?** In *T. thermophilus* TruD does, while in *E. coli* the site is attributed to RluF. *P. putida* has its own Rlu complement, so this is an open question.
3. **Are any mRNA sites modified?** The UNUAR motif suggests possible mRNA targets.
4. **Does loss of TruD have a phenotype under stress?** For example, a growth defect at temperature extremes.

---

### Sources
- UniProt Q88MF2 record (local copy `genes/PSEPK/truD/truD-uniprot.txt`); HAMAP MF_01082
- Kaya Y, Ofengand J. 2003. *RNA* 9:711–721 (PMID 12756329): https://pmc.ncbi.nlm.nih.gov/articles/pmid/12756329 ; https://ecoliwiki.org/colipedia/index.php/PMID:12756329
- Hoang C, Ferré-D'Amaré AR. 2004. *RNA* 10:1026 (PMID 15208439): https://rnajournal.cshlp.org/content/10/7/1026.full ; PDB 1SB7: https://www.rcsb.org/structure/1SB7
- Kaya Y et al. 2004. *J Biol Chem* (PMID 15135053): https://pubmed.ncbi.nlm.nih.gov/15135053 ; PDB 1SI7: https://www.rcsb.org/structure/1SI7
- Ericsson UB et al. 2004. *FEBS Lett* (TruD 2.0 Å structure); via Modomics: https://iimcb.genesilico.pl/modomics/publications/278/
- Yamagami R et al. 2025. *RNA* 31(6):850–867: https://rnajournal.cshlp.org/content/31/6/850.full
- Rhea 42540: https://www.rhea-db.org/rhea/42540
- Pus7/TruD-family reviews: https://pmc.ncbi.nlm.nih.gov/articles/PMC8794802 ; https://academic.oup.com/nar/article/49/20/11810/6413612
- PROSITE TruD domain: https://prosite.expasy.org/PDOC50984

## Citations

1. https://www.rhea-db.org/rhea/42540
2. https://pmc.ncbi.nlm.nih.gov/articles/pmid/12756329
3. https://ecoliwiki.org/colipedia/index.php/PMID:12756329
4. https://rnajournal.cshlp.org/content/31/6/850.full
5. https://rnajournal.cshlp.org/content/31/6/850.short
6. https://pmc.ncbi.nlm.nih.gov/articles/PMC8794802
7. https://academic.oup.com/nar/article/49/20/11810/6413612
8. https://rnajournal.cshlp.org/content/10/7/1026.full
9. https://www.rcsb.org/structure/1SB7
10. https://pubmed.ncbi.nlm.nih.gov/15135053
11. https://www.rcsb.org/structure/1SI7
12. https://iimcb.genesilico.pl/modomics/publications/278/
13. https://prosite.expasy.org/PDOC50984