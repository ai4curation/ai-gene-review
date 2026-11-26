---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-30T21:32:44.237816'
end_time: '2026-10-30T21:36:38.809509'
duration_seconds: 234.57
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: yedI
  gene_symbol: yedI
  uniprot_accession: Q88F06
  protein_description: 'SubName: Full=Conserved inner membrane protein {ECO:0000313|EMBL:AAN69874.1};'
  gene_info: Name=yedI {ECO:0000313|EMBL:AAN69874.1}; OrderedLocusNames=PP_4294 {ECO:0000313|EMBL:AAN69874.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: YedI. (IPR008526); DUF808 (PF05661)
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
  num_turns: 13
  total_cost_usd: 0.7834791000000001
  session_id: a48ecb06-e029-49b2-b796-a1694a695d98
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 12
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q88F06
- **Protein Description:** SubName: Full=Conserved inner membrane protein {ECO:0000313|EMBL:AAN69874.1};
- **Gene Information:** Name=yedI {ECO:0000313|EMBL:AAN69874.1}; OrderedLocusNames=PP_4294 {ECO:0000313|EMBL:AAN69874.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** YedI. (IPR008526); DUF808 (PF05661)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "yedI" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'yedI' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **yedI** (gene ID: yedI, UniProt: Q88F06) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

Status: I've confirmed the protein's identity and pulled family and literature context. Now I'm checking the E. coli YedI record, the Daley topology data, and P. putida fitness data.

# yedI (PP_4294, UniProt Q88F06) of *Pseudomonas putida* KT2440: research report

## Summary

The target is correctly identified. The symbol yedI, the UniProt description ("Conserved inner membrane protein"), the organism (*P. putida* KT2440, taxon 160488) and the domain assignments (IPR008526 YedI; PF05661 DUF808; PIRSF016660) all point to one protein. It belongs to the YedI/DUF808 family, which is named after *Escherichia coli* YedI (P46125, gene b1958).

No experimental study of PP_4294 or any close homolog has been found. Its activity, substrate and pathway are unknown. The only well-supported statement is about location: it is very likely a multi-pass integral protein of the cytoplasmic (inner) membrane. Anything beyond that is speculation, and this report labels it as such.

---

## 1. Identity and basic properties

| Feature | Value | Source |
|---|---|---|
| Accession / locus | Q88F06 / PP_4294 (EMBL AAN69874.1; RefSeq WP_010955035.1) | UniProt Q88F06 (local copy `genes/PSEPK/yedI/yedI-uniprot.txt`) |
| Length / mass | 304 aa, 31.6 kDa | UniProt |
| Evidence level | PE 4, "Predicted"; TrEMBL (unreviewed) | UniProt |
| Name source | Automatic, imported from the genome submission (ECO:0000313) | UniProt |
| Family | InterPro IPR008526 "Inner membrane protein YedI"; Pfam PF05661 DUF808; PIRSF016660; PANTHER PTHR30503 / PTHR30503:SF3 "INNER MEMBRANE PROTEIN YEDI" | UniProt cross-references; InterPro API |
| Orthology | eggNOG COG2354; KEGG ppu:PP_4294 | UniProt |
| Genome papers | Nelson et al. 2002, *Environ Microbiol* 4:799–808 (PMID:12534463); Belda et al. 2016, *Environ Microbiol* 18:3403–3424 (PMID:26913973) | UniProt RN lines |

Neither genome paper describes what PP_4294 does. They only supply the gene model and its annotation.

## 2. Family: YedI / DUF808

- **InterPro and Pfam descriptions add no functional information.** InterPro IPR008526 says only "This family of proteins includes inner membrane protein YedI." Pfam PF05661 says "This family consists of several bacterial proteins of unknown function." Neither entry has GO mappings or literature (InterPro REST API, retrieved 2026-10-30, https://www.ebi.ac.uk/interpro/entry/InterPro/IPR008526/).
- **The family is large and widespread.** PANTHER PTHR30503 has about 6,500 member proteins from about 6,450 proteomes, and has only one subfamily (SF3). AlphaFold models exist for about 4,000 members, but no experimental structure exists for any of them (local InterPro metadata, `interpro/panther/PTHR30503/PTHR30503-metadata.yaml`). The only Swiss-Prot reviewed member listed is *E. coli* YedI, P46125.
- **The *E. coli* founding member is also uncharacterized.** Its reviewed entry, P46125 "Inner membrane protein YedI", says only "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein." Its topology features are predictions (ECO:0000255): an N-terminal cytoplasmic region of about 71 residues, then six transmembrane helices, with the C-terminus in the cytoplasm (UniProt P46125, https://rest.uniprot.org/uniprotkb/P46125.txt). EcoliWiki lists it as a "hypothetical protein; conserved inner membrane protein" with unknown function ([EcoliWiki yedI](https://ecoliwiki.org/colipedia/index.php/yedI:Gene_Product(s)); [Quickview](https://ecoliwiki.org/colipedia/index.php/yedI:Quickview)). P46125 cites Daley et al. 2005, *Science* (PMID:15919996), which tagged the C-termini of 601 *E. coli* inner-membrane proteins with alkaline phosphatase and GFP ([EcoliWiki PMID:15919996](https://ecoliwiki.org/colipedia/index.php/PMID:15919996)). I could not confirm YedI's own result in that dataset. The UniProt C-terminus assignment is marked as predicted.
- **Ribosome profiling suggests modest constitutive expression in *E. coli*:** about 267 molecules per cell per generation in rich MOPS medium (cited on EcoliWiki).

### The MutK link: a weak and indirect clue

EcoliWiki says *E. coli* YedI is homologous to *Vibrio cholerae* MutK. MutK (Q9ZAK8, 163 aa) does carry PF05661/DUF808, according to its UniProt record. Bera et al. 1999, "The mutK gene of *Vibrio cholerae*: a new gene involved in DNA mismatch repair", *J Bacteriol* (PMID:9922251; [PMC93454](https://pmc.ncbi.nlm.nih.gov/articles/PMC93454); [CORE](https://core.ac.uk/works/1304931)), reported the following:

- Cloned *mutK* lowered the spontaneous mutation frequency of several *E. coli* mismatch-repair mutants.
- A *mutK* knockout had a mutation rate close to wild type.
- The authors proposed a methyl-independent repair route.

This should not be transferred to PP_4294:

1. MutK is about half the length of YedI/PP_4294 (163 vs 304 aa). The two proteins therefore share at most part of the DUF808 region.
2. Its own UniProt record predicts three transmembrane helices for MutK. A membrane protein with a direct DNA-repair function is mechanistically implausible. The anti-mutator effect came from overexpression in a heterologous host, which can act indirectly.
3. No later work has confirmed a repair role for any DUF808 protein. Some automated databases list mismatch-repair GO terms for YedI-family entries. These appear to trace back to this one observation and should be treated as unreliable.

## 3. Localization: plasma (inner) membrane, multi-pass

**Sequence evidence for PP_4294:**

- **Five transmembrane helices** are predicted by Phobius, at residues 71–100, 151–168, 174–198, 231–251 and 271–294 (UniProt FT TRANSMEM, ECO:0000256|SAM:Phobius).
- **A soluble N-terminal region (about residues 1–70)** precedes the helices. It is rich in charged residues: "MAGSSLLVLIDDIATLLDDVSLMTKVAAKKTAGVLGDDLALNAQQVTGVRADREL…". There is no signal peptide annotation.
- **A charged loop of about 50 residues lies between TM1 and TM2** (…GFEKLAHKFLHSKEEDEAQHEARKEAVADASVDLVAFEKAKIK…). Its basic residues suggest it faces the cytoplasm, by the positive-inside rule.

**Comparison with *E. coli* YedI.** The architecture closely matches P46125: a cytoplasmic N-terminal region of about 70 residues, then a cluster of transmembrane helices, with the same helix positions to within a few residues. Where Phobius calls one long TM1 in PP_4294 (71–100), *E. coli* YedI is predicted to have two helices (72–92 and 93–113). PP_4294 therefore probably has six transmembrane helices as well. Its exact topology has not been determined experimentally.

**GO annotation.** The only existing annotation is GO:0005886 plasma membrane (IEA, TreeGrafter, from PANTHER node PTN000766748). This agrees with the sequence features and with the inner-membrane localization of the *E. coli* family member. Two independent lines support the inner (cytoplasmic) membrane: the predicted helices and the family-level localization. There is no sign of outer-membrane β-barrel character.

## 4. Molecular function and pathway: unknown

- **No catalytic motif, transporter signature or ligand-binding motif has been assigned to the DUF808 family.** Sequence searches found no characterized relative beyond the anecdotal MutK result.
- **The composition is notably Gly/Ala-rich within the helices.** Examples are "LVGGIVKLDDLG" and "AVVLAVVSVAGK". Glycine-rich helices are common in membrane proteins whose helices pack tightly together, such as transporters and channels. This fits the protein being a small integral membrane protein, but it does not identify any substrate (inference only).
- **Gene neighbourhood in KT2440 (KEGG):**

  | Locus | Annotation |
  |---|---|
  | PP_4290 | *uacT*, uric acid permease |
  | PP_4291 | conserved exported protein |
  | PP_4293 | conserved exported protein |
  | **PP_4294** | ***yedI*** |
  | PP_4295 | TetR-family transcriptional regulator |
  | PP_4296 | conserved exported protein |
  | PP_4297 | *gcl*, glyoxylate carboligase |
  | PP_4298 | *hyi*, hydroxypyruvate isomerase |

  The nearby purine/allantoin–glyoxylate catabolism genes (*uacT*, *gcl*, *hyi*) and the TetR regulator could hint at a regulated, membrane-associated role. Bacterial gene neighbourhoods are often uninformative, though, and this has not been tested (inference only).
- **Fitness data.** *P. putida* KT2440 has been profiled genome-wide by RB-TnSeq (e.g., Borchert et al., machine-learning analysis of KT2440 RB-TnSeq data; [PMC10949508](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10949508/)). I could not retrieve PP_4294's gene-level fitness values: the Fitness Browser blocked automated access, and the papers do not discuss the gene. Whether PP_4294 has a condition-specific phenotype is still open. Checking the Fitness Browser (orgId=Putida, locusId PP_4294) by hand is the most practical next step.

## 5. Implications for GO curation

| Aspect | Assessment |
|---|---|
| **CC: GO:0005886 plasma membrane (IEA, TreeGrafter)** | Supported by sequence and family evidence. Reasonable to keep as non-core but correct; it is the only defensible annotation. A more specific option, if desired, is "integral component of plasma membrane"-type wording, supported by the predicted 5–6 transmembrane helices. |
| **Molecular function** | No supported term. Do not transfer DNA mismatch repair (from MutK). Do not assign transporter activity without evidence. |
| **Biological process** | No supported term. |
| **Gene name** | "yedI" is an automatic name imported from the genome submission, based on homology to *E. coli* b1958. It describes family membership, not function. |

## 6. Open questions and suggested experiments

1. **Topology:** map the PP_4294 (or *E. coli* YedI) topology with PhoA/GFP fusions or cysteine accessibility. This would test the prediction of a cytoplasmic N-terminal region plus six helices.
2. **Phenotype:** retrieve or generate RB-TnSeq fitness data for PP_4294 across carbon/nitrogen sources (especially purines and allantoin, given the neighbourhood) and stress conditions. Co-fitness partners would be the strongest functional clue.
3. **The MutK claim:** test whether deleting or overexpressing PP_4294 or *yedI* changes spontaneous mutation rates in wild-type and *mutS*/*mutH* backgrounds. This would settle the inherited mismatch-repair claim.
4. **Regulation:** test whether the neighbouring TetR regulator (PP_4295) controls PP_4294 expression, and find its ligand.
5. **Structure:** analyse the AlphaFold model of Q88F06 for a cavity or pore. That could suggest transporter versus structural or scaffold roles.

---

## References

- UniProtKB Q88F06 (PP_4294, *P. putida* KT2440), entry version 87 (28-Jan-2026). https://www.uniprot.org/uniprotkb/Q88F06
- UniProtKB P46125, Inner membrane protein YedI, *E. coli* K-12. https://rest.uniprot.org/uniprotkb/P46125.txt
- UniProtKB Q9ZAK8, MutK, *V. cholerae*. https://www.uniprot.org/uniprotkb/Q9ZAK8
- InterPro IPR008526 and Pfam PF05661 entries (EBI InterPro API, accessed 2026-10-30). https://www.ebi.ac.uk/interpro/entry/InterPro/IPR008526/
- PANTHER PTHR30503 metadata (local InterPro export, `interpro/panther/PTHR30503/`).
- Nelson KE et al. (2002). Complete genome sequence and comparative analysis of the metabolically versatile *Pseudomonas putida* KT2440. *Environ Microbiol* 4:799–808. PMID:12534463.
- Belda E et al. (2016). The revisited genome of *Pseudomonas putida* KT2440 enlightens its value as a robust metabolic chassis. *Environ Microbiol* 18:3403–3424. PMID:26913973.
- Bera TK et al. (1999). The mutK gene of *Vibrio cholerae*: a new gene involved in DNA mismatch repair. *J Bacteriol*. PMID:9922251. [PMC93454](https://pmc.ncbi.nlm.nih.gov/articles/PMC93454); [CORE](https://core.ac.uk/works/1304931)
- Daley DO et al. (2005). Global topology analysis of the *Escherichia coli* inner membrane proteome. *Science*. PMID:15919996. [EcoliWiki summary](https://ecoliwiki.org/colipedia/index.php/PMID:15919996)
- EcoliWiki yedI pages: [Gene Product(s)](https://ecoliwiki.org/colipedia/index.php/yedI:Gene_Product(s)), [Quickview](https://ecoliwiki.org/colipedia/index.php/yedI:Quickview), [On One Page](https://ecoliwiki.org/colipedia/index.php/yedI:On_One_Page)
- KEGG genes ppu:PP_4290–PP_4298. https://www.kegg.jp/entry/ppu:PP_4294
- Machine-learning analysis of RB-TnSeq fitness data predicts functional gene modules in *Pseudomonas putida* KT2440 (2024). [PMC10949508](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10949508/)

## Citations

1. https://www.ebi.ac.uk/interpro/entry/InterPro/IPR008526/
2. https://rest.uniprot.org/uniprotkb/P46125.txt
3. https://ecoliwiki.org/colipedia/index.php/yedI:Gene_Product(s
4. https://ecoliwiki.org/colipedia/index.php/yedI:Quickview
5. https://ecoliwiki.org/colipedia/index.php/PMID:15919996
6. https://pmc.ncbi.nlm.nih.gov/articles/PMC93454
7. https://core.ac.uk/works/1304931
8. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10949508/
9. https://www.uniprot.org/uniprotkb/Q88F06
10. https://www.uniprot.org/uniprotkb/Q9ZAK8
11. https://ecoliwiki.org/colipedia/index.php/yedI:On_One_Page
12. https://www.kegg.jp/entry/ppu:PP_4294