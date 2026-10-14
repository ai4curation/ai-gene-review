---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-14T23:14:32.675830'
end_time: '2026-10-14T23:15:10.163675'
duration_seconds: 37.49
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: SUCLA2
  gene_symbol: SUCLA2
  uniprot_accession: Q9P2R7
  protein_description: 'RecName: Full=Succinate--CoA ligase [ADP-forming] subunit
    beta, mitochondrial {ECO:0000255|HAMAP-Rule:MF_03220}; EC=6.2.1.5 {ECO:0000255|HAMAP-Rule:MF_03220,
    ECO:0000269|PubMed:15877282}; AltName: Full=ATP-specific succinyl-CoA synthetase
    subunit beta {ECO:0000255|HAMAP-Rule:MF_03220}; Short=A-SCS {ECO:0000255|HAMAP-Rule:MF_03220};
    AltName: Full=Itaconyl--CoA ligase [ADP-forming] subunit beta; EC=6.2.1.- {ECO:0000255|HAMAP-Rule:MF_03220,
    ECO:0000269|PubMed:40108300}; AltName: Full=Malyl--CoA ligase [ADP-forming] subunit
    beta; EC=6.2.1.9 {ECO:0000255|HAMAP-Rule:MF_03220, ECO:0000269|PubMed:40108300};
    AltName: Full=Succinyl-CoA synthetase beta-A chain {ECO:0000255|HAMAP-Rule:MF_03220};
    Short=SCS-betaA {ECO:0000255|HAMAP-Rule:MF_03220}; Flags: Precursor;'
  gene_info: Name=SUCLA2 {ECO:0000255|HAMAP-Rule:MF_03220, ECO:0000303|PubMed:34492704};
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the succinate/malate CoA ligase beta subunit
  protein_domains: ATP-grasp. (IPR011761); ATP-grasp_succ-CoA_synth-type. (IPR013650);
    ATP_grasp_subdomain_1. (IPR013815); Succ-CoA_synthase_bsu_CS. (IPR017866); SUCC_ACL_C.
    (IPR005811)
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
  - claude-sonnet-5-5
  web_search_requests: 3
  num_turns: 5
  total_cost_usd: 0.22000250000000002
  session_id: d59b2dca-3995-59ba-98f7-69e97fb62d6e
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 9
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q9P2R7
- **Protein Description:** RecName: Full=Succinate--CoA ligase [ADP-forming] subunit beta, mitochondrial {ECO:0000255|HAMAP-Rule:MF_03220}; EC=6.2.1.5 {ECO:0000255|HAMAP-Rule:MF_03220, ECO:0000269|PubMed:15877282}; AltName: Full=ATP-specific succinyl-CoA synthetase subunit beta {ECO:0000255|HAMAP-Rule:MF_03220}; Short=A-SCS {ECO:0000255|HAMAP-Rule:MF_03220}; AltName: Full=Itaconyl--CoA ligase [ADP-forming] subunit beta; EC=6.2.1.- {ECO:0000255|HAMAP-Rule:MF_03220, ECO:0000269|PubMed:40108300}; AltName: Full=Malyl--CoA ligase [ADP-forming] subunit beta; EC=6.2.1.9 {ECO:0000255|HAMAP-Rule:MF_03220, ECO:0000269|PubMed:40108300}; AltName: Full=Succinyl-CoA synthetase beta-A chain {ECO:0000255|HAMAP-Rule:MF_03220}; Short=SCS-betaA {ECO:0000255|HAMAP-Rule:MF_03220}; Flags: Precursor;
- **Gene Information:** Name=SUCLA2 {ECO:0000255|HAMAP-Rule:MF_03220, ECO:0000303|PubMed:34492704};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the succinate/malate CoA ligase beta subunit
- **Key Domains:** ATP-grasp. (IPR011761); ATP-grasp_succ-CoA_synth-type. (IPR013650); ATP_grasp_subdomain_1. (IPR013815); Succ-CoA_synthase_bsu_CS. (IPR017866); SUCC_ACL_C. (IPR005811)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "SUCLA2" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'SUCLA2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **SUCLA2** (gene ID: SUCLA2, UniProt: Q9P2R7) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# SUCLA2 (Q9P2R7), human: research report

**Identity check.** The symbol, protein name, organism, family and domains all describe the same protein. SUCLA2 is the ATP-specific beta subunit of succinate–CoA ligase [ADP-forming]. It belongs to the succinate/malate CoA ligase beta family and has an ATP-grasp domain. The gene symbol is not ambiguous.

**How this report was built.** I ran three web searches, which returned mostly secondary sources. Those searches did not retrieve the primary papers for PMID:15877282 or PMID:40108300, or the Lambeth 2004 abstract. Claims that rest only on the UniProt annotation supplied in the task, or on my background knowledge, are marked as such.

## 1. Primary function

**Reaction.** SUCLA2 is the beta subunit of ATP-specific succinyl-CoA synthetase (A-SCS), EC 6.2.1.5:

succinyl-CoA + ADP + Pi ⇌ succinate + CoA + ATP

This is the only substrate-level phosphorylation step of the TCA cycle. DrugBank describes the enzyme this way, and it cites PMID:15877282, PMID:34492704 and PMID:40108300 for the TCA-cycle role ([DrugBank Q9P2R7](https://go.drugbank.com/polypeptides/Q9P2R7)). The UniProt record in the task cites PMID:15877282 as experimental support for EC 6.2.1.5.

**Subunit composition.** SUCLA2 forms a heterodimer with the shared alpha subunit SUCLG1.
- The beta subunit supplies nucleotide specificity (ATP) and helps bind succinate (as relayed by [Wikipedia](https://en.wikipedia.org/wiki/Succinyl_coenzyme_A_synthetase) and the search summaries).
- The alternative beta subunit SUCLG2 pairs with SUCLG1 to form the GTP-specific enzyme (G-SCS). The two beta subunits are about 50% identical ([Lambeth et al. 2004, J Biol Chem 279:36621, "Expression of two succinyl-CoA synthetases with different nucleotide specificities in mammalian tissues"](https://medlineplus.gov/genetics/gene/sucla2); full text not retrieved).
- A human SUCLG1–SUCLA2 structure has been deposited at 2.59 Å ([PDB 6G4Q](https://rcsb.org/structure/6G4Q)). Its entry is listed as "To be published".

**Substrate specificity and secondary activities.** The UniProt entry lists two further ADP-forming ligase activities, both attributed to PMID:40108300:
- itaconyl-CoA ligase, EC 6.2.1.-
- malyl-CoA ligase, EC 6.2.1.9

These are mirrored in the mouse UniProt record ([Glycosmos](https://glycosmos.org/genes/20916)) and as malate-CoA ligase GO terms on [DrugBank](https://go.drugbank.com/polypeptides/Q9P2R7). I could not retrieve the 2025 paper, so I cannot say how efficient these side activities are or whether they matter in vivo. They fit a role in itaconate and malate/CoA-ester metabolism, but treat them as secondary to succinyl-CoA synthesis.

## 2. Localization

- SUCLA2 is a mitochondrial matrix enzyme. The UniProt record flags it as a precursor, which implies cleavage of an N-terminal mitochondrial targeting peptide.
- The complex also associates with mitochondrial nucleoside diphosphate kinase (NME4) and with mtDNA maintenance. This is a background-knowledge claim that I could not verify from the searches.

## 3. Pathways

- **TCA cycle.** The enzyme converts succinyl-CoA to succinate with ATP production. Succinyl-CoA comes from 2-oxoglutarate dehydrogenase, and from the catabolism of odd-chain fatty acids, branched-chain amino acids and propionate.
- **Tissue expression.** Per secondary sources, SUCLA2 is predominantly expressed in catabolic, ATP-reliant tissues: brain, heart and skeletal muscle. SUCLG2 is more prominent in liver and kidney ([Abcam summary of UniProt](https://www.abcam.com/en-us/targets/suclg2/8764); [MedlinePlus](https://medlineplus.gov/genetics/gene/sucla2)).
- **Nucleotide pools and mtDNA.** The complex is thought to support mitochondrial dNTP supply through its interaction with NME4. Loss of SUCLA2 causes mtDNA depletion, which is the likely mechanism behind the disease (see section 4). The exact molecular link is not fully resolved in the sources I retrieved.

## 4. Disease and genetic evidence

Biallelic SUCLA2 variants cause mitochondrial DNA depletion syndrome 5 (MTDPS5), an autosomal recessive encephalomyopathic form with mild methylmalonic aciduria ([MedlinePlus condition page](https://medlineplus.gov/genetics/condition/sucla2-related-mitochondrial-dna-depletion-syndrome)).
- **Clinical picture.** Patients have progressive, childhood-onset Leigh-like encephalomyopathy with dystonia, hypotonia, sensorineural hearing loss, basal ganglia lesions, mtDNA depletion and methylmalonic aciduria. Expression is highest in brain, which may explain the neurological predominance ([PMC review](https://pmc.ncbi.nlm.nih.gov/articles/PMC4864773)).
- **Key primary study.** [Carrozzo et al. 2007, Brain, PMID:17301081](https://pubmed.ncbi.nlm.nih.gov/17301081/) studied 14 patients from 11 families with mild methylmalonic aciduria. It found three novel mutations and confirmed the mtDNA depletion and the protein-level defect.
- **Related gene.** SUCLG1 variants, in the shared alpha subunit, give a similar phenotype.

Proposed explanation for the methylmalonic aciduria: succinyl-CoA accumulation or imbalance, which is likely to affect methylmalonyl-CoA metabolism. This is my inference and I did not verify it against a primary source.

## 5. Evidence summary and caveats

| Claim | Evidence | Strength |
|---|---|---|
| ATP-forming succinyl-CoA synthetase, EC 6.2.1.5 | UniProt, citing PMID:15877282 (experimental); DrugBank | Strong, but the primary paper was not retrieved |
| Itaconyl-CoA and malyl-CoA ligase activity | UniProt, citing PMID:40108300 | Recent; paper not read, so treat as secondary |
| Heterodimer with SUCLG1 | Structure (PDB 6G4Q), reviews | Good |
| MTDPS5 / methylmalonic aciduria | Carrozzo 2007 (PMID:17301081); MedlinePlus; PMC review | Strong |
| Tissue bias (brain, heart, muscle) | Lambeth 2004 via secondary summaries | Moderate |

**Unresolved:**
- The kinetics and relative efficiency of the itaconyl-CoA and malyl-CoA activities in vivo.
- The molecular mechanism linking loss of SUCLA2 to mtDNA depletion.
- The Johnson 2005 and PMID:40108300 primary papers, which should be read before the review file cites them.

## Sources

- [MedlinePlus: SUCLA2 gene](https://medlineplus.gov/genetics/gene/sucla2)
- [MedlinePlus: SUCLA2-related mitochondrial DNA depletion syndrome](https://medlineplus.gov/genetics/condition/sucla2-related-mitochondrial-dna-depletion-syndrome)
- [Carrozzo et al. 2007, PMID:17301081](https://pubmed.ncbi.nlm.nih.gov/17301081/)
- [PMC4864773](https://pmc.ncbi.nlm.nih.gov/articles/PMC4864773)
- [DrugBank Q9P2R7](https://go.drugbank.com/polypeptides/Q9P2R7)
- [Glycosmos: mouse Sucla2 (UniProt-derived)](https://glycosmos.org/genes/20916)
- [RCSB PDB 6G4Q](https://rcsb.org/structure/6G4Q)
- [Wikipedia: Succinyl coenzyme A synthetase](https://en.wikipedia.org/wiki/Succinyl_coenzyme_A_synthetase)
- [Abcam SUCLG2 summary](https://www.abcam.com/en-us/targets/suclg2/8764)

## Citations

1. https://go.drugbank.com/polypeptides/Q9P2R7
2. https://en.wikipedia.org/wiki/Succinyl_coenzyme_A_synthetase
3. https://medlineplus.gov/genetics/gene/sucla2
4. https://rcsb.org/structure/6G4Q
5. https://glycosmos.org/genes/20916
6. https://www.abcam.com/en-us/targets/suclg2/8764
7. https://medlineplus.gov/genetics/condition/sucla2-related-mitochondrial-dna-depletion-syndrome
8. https://pmc.ncbi.nlm.nih.gov/articles/PMC4864773
9. https://pubmed.ncbi.nlm.nih.gov/17301081/