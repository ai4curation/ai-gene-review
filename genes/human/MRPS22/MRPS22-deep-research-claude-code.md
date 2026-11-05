---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-24T04:30:04.358032'
end_time: '2026-10-24T04:30:37.232393'
duration_seconds: 32.87
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: MRPS22
  gene_symbol: MRPS22
  uniprot_accession: P82650
  protein_description: 'RecName: Full=Small ribosomal subunit protein mS22 {ECO:0000303|PubMed:25838379};
    AltName: Full=28S ribosomal protein S22, mitochondrial; Short=MRP-S22; Short=S22mt;'
  gene_info: Name=MRPS22; Synonyms=C3orf5, RPMS22; ORFNames=GK002;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the mitochondrion-specific ribosomal protein
  protein_domains: Ribosomal_mS22. (IPR019374); MRP-S22 (PF10245)
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
  web_search_requests: 2
  num_turns: 6
  total_cost_usd: 0.22100039999999999
  session_id: d59b2dca-3995-59ba-98f7-69e97fb62d6e
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 7
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P82650
- **Protein Description:** RecName: Full=Small ribosomal subunit protein mS22 {ECO:0000303|PubMed:25838379}; AltName: Full=28S ribosomal protein S22, mitochondrial; Short=MRP-S22; Short=S22mt;
- **Gene Information:** Name=MRPS22; Synonyms=C3orf5, RPMS22; ORFNames=GK002;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the mitochondrion-specific ribosomal protein
- **Key Domains:** Ribosomal_mS22. (IPR019374); MRP-S22 (PF10245)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "MRPS22" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'MRPS22' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **MRPS22** (gene ID: MRPS22, UniProt: P82650) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# MRPS22 (mS22, human, UniProt P82650): research report

## Identity check
The symbol, protein and organism match. MRPS22 (synonyms C3orf5, RPMS22, GK002) encodes the 360-aa "Small ribosomal subunit protein mS22" (28S ribosomal protein S22, mitochondrial). It is *Homo sapiens* (taxon 9606), in the mitochondrion-specific ribosomal protein mS22 family, with the InterPro domain IPR019374 (Ribosomal_mS22) and the Pfam family PF10245 (MRP-S22). I found no ambiguity with another gene. The following come from the local UniProt record (`MRPS22-uniprot.txt`, entry version 194). The first two cite PMID:25838379 and PMID:17873122 as given there. The disease entries (COXPD5, ODG7) are quoted from the record.

**Scope of this report.** I ran two web searches, one on disease and one on mitoribosome structure. The structure search did not return anything specific to mS22. Some statements below come from my background knowledge and are flagged as not verified in this session.

## Primary function
MRPS22 is a structural protein, not an enzyme or signalling protein. It is a component of the mitochondrial small ribosomal subunit (mt-SSU, 28S).

- UniProt describes the mammalian 55S mitoribosome as a 28S small subunit and a 39S large subunit. The 28S subunit contains the 12S mt-rRNA and 30 different proteins. The 39S subunit contains 16S mt-rRNA, mt-tRNA(Val) and 52 proteins. UniProt cites PMID:25838379 (Greber & Ban, structure of the human mitoribosome) for this. The UniProt record gives the protein's location as "Mitochondrion", also citing PMID:25838379.
- The mitoribosome translates the 13 mtDNA-encoded OXPHOS subunits. Amunts et al. 2015 (Science, cryo-EM at 3.5 Å, PDB 3J9M) reported 80 proteins and three rRNAs. They also described extensive remodelling of the small-subunit head around the mRNA channel ([PMC4501431](https://pmc.ncbi.nlm.nih.gov/articles/PMC4501431); [RCSB 3J9M](https://www.rcsb.org/structure/3J9M)). That search result did not mention mS22 specifically.
- From background knowledge, not verified here: mS22 is a mitochondria-specific small-subunit protein. It sits in the body of the 28S subunit and contributes to rRNA scaffolding and assembly, and it has no bacterial orthologue.
- UniProt lists one IntAct interaction, with MRPS18B (Q9Y676), which is another mt-SSU protein. That is consistent with co-assembly in the same particle and does not indicate an independent function.

**For GO curation.**
- The appropriate molecular function is `structural constituent of ribosome` (GO:0003735).
- The component terms are `mitochondrial small ribosomal subunit` (GO:0005763) and the mitochondrion.
- The process is `mitochondrial translation` (GO:0032543). It is supported indirectly, as the ribosome's function. No catalytic step is attributed to mS22 itself.
- The GOA file also contains `protein binding` (GO:0005515, two rows with an experimental ECO code). This is uninformative and should be replaced by, or subsumed under, the structural constituent annotation.
- GOA has many `mitochondrial inner membrane` rows (GO:0005743, ECO:0000304, TAS-type, apparently from Reactome). The mitoribosome is membrane-associated in vivo, but this is a weak annotation for an individual protein and is better treated as non-core. I did not check this against the primary literature.

## Localisation
The protein is in the mitochondrial matrix side of the inner membrane, as part of the mitoribosome. UniProt lists the location as mitochondrion, and GOA has an HPA IDA mitochondrion annotation. The exact sub-mitochondrial location comes from the structural context and was not examined in this session.

## Pathway
The relevant pathway is mitochondrial translation. The ribosome synthesises the 13 mtDNA-encoded subunits of OXPHOS complexes I, III, IV and V, so mS22 deficiency causes combined OXPHOS defects.

## Disease evidence (loss-of-function)
These studies show the protein is necessary for mitochondrial translation. They are not evidence of a catalytic role.

- **COXPD5 (MIM 611719).** UniProt describes it as severe metabolic acidosis, edema, hypertrophic cardiomyopathy, tubulopathy and hypotonia. Smits et al. 2010 reported a patient with Cornelia de Lange-like features, brain abnormalities, hypertrophic cardiomyopathy and combined complex I, III and IV deficiency. The patient was homozygous for a variant predicted to give Leu215Pro. Re-expressing wild-type MRPS22 in patient fibroblasts restored complex IV amount and activity and 12S rRNA levels ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/pmid/21189481); [EJHG 2010](https://www.nature.com/articles/ejhg2010214)). The 12S rRNA result is consistent with a role in small-subunit stability or assembly.
- **Severe neonatal case.** Baertling et al. 2015 reported a neonate with fatal lactic acidosis and combined OXPHOS deficiency, a homozygous MRPS22 mutation, agenesis of the corpus callosum, and atrial and ventricular septal defects with a coronary artery fistula ([Springer](https://link.springer.com/article/10.1007/s10048-015-0440-6)).
- **Ovarian dysgenesis 7 (MIM 618117).** UniProt cites PMID:29566152 for an autosomal recessive form with streak gonads and primary amenorrhea. GeneCards also lists 46,XX gonadal dysgenesis ([GeneCards](https://www.genecards.org/card/MRPS22)). I did not read the primary paper.
- The UniProt record cites PMID:17873122 for the COXPD5 entry. I did not check that paper, and it may be an earlier MRPS22 mutation report.

## Evidence summary
| Claim | Evidence |
|---|---|
| Part of the 28S mt-SSU | Cryo-EM structures (PMID:25838379; Amunts et al. 2015), cited in UniProt |
| Mitochondrial localisation | UniProt; HPA |
| Needed for mitochondrial translation | Patient fibroblasts with MRPS22 variants, rescued by wild-type cDNA (Smits 2010) |
| Family and domain | InterPro IPR019374; Pfam PF10245; mitochondria-specific mS22 family |

## Gaps and caveats
- I did not retrieve PMID:25838379, PMID:17873122 or PMID:29566152 to confirm what they show for MRPS22. Check the cached `publications/PMID_*.md` files before using them as evidence in the review.
- The precise position of mS22 within the 28S subunit (which rRNA helices and neighbouring proteins it contacts) needs the structure papers or PDB 3J9M, which this session did not cover.
- There is no evidence of any non-ribosomal function. The unexplained pleiotropy (cardiomyopathy, brain malformations, ovarian dysgenesis) is best attributed to tissue-specific dependence on mitochondrial translation.

Sources:
- [Smits et al. 2010, PMC](https://pmc.ncbi.nlm.nih.gov/articles/pmid/21189481)
- [Smits et al. 2010, EJHG](https://www.nature.com/articles/ejhg2010214)
- [Baertling et al. 2015](https://link.springer.com/article/10.1007/s10048-015-0440-6)
- [GlyCosmos COXPD5](https://glycosmos.org/diseases/DOID:0111473)
- [GeneCards MRPS22](https://www.genecards.org/card/MRPS22)
- [Amunts et al. 2015, PMC4501431](https://pmc.ncbi.nlm.nih.gov/articles/PMC4501431)
- [RCSB PDB 3J9M](https://www.rcsb.org/structure/3J9M)
- Local files: `genes/human/MRPS22/MRPS22-uniprot.txt`, `MRPS22-goa.tsv`

## Citations

1. https://pmc.ncbi.nlm.nih.gov/articles/PMC4501431
2. https://www.rcsb.org/structure/3J9M
3. https://pmc.ncbi.nlm.nih.gov/articles/pmid/21189481
4. https://www.nature.com/articles/ejhg2010214
5. https://link.springer.com/article/10.1007/s10048-015-0440-6
6. https://www.genecards.org/card/MRPS22
7. https://glycosmos.org/diseases/DOID:0111473