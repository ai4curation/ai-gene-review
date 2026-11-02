# NCU04302 research notes

Review date: 2026-09-09T03:17:51.839101+00:00. Target: Q1K772, NEUCR, 157 residues. Identity is anchored to the frozen current UniProt accession and gene record. The accession-specific fetch seeded all 13 current GOA rows.

## Evidence basis

NCU04302 encodes a 157-residue Ubc9-family SUMO-conjugating E2 enzyme. Its conserved UBC catalytic domain and phylogenetic placement support transfer of activated SUMO to protein substrates, predominantly in the nucleus. SUMO modification provides a mechanism for regulating nuclear proteins; target-specific substrates and the distribution among nuclear subcompartments remain incompletely characterized.

- file:NEUCR/NCU04302/NCU04302-uniprot.txt: “DR   InterPro; IPR000608; UBC.”
- PMID:9435231: “Moreover, recombinant yeast and mammalian UBC9 enzymes were found to form thioester complexes with SMT3 and SUMO-1, respectively.”

## Source claim provenance

The full API prediction JSON is preserved without deleting any fields. Function and location reports retain original words, SL identifiers and entire evidence objects. GO sidecars preserve all emitted GO IDs and labels; main reviews assess the independent current GOA rows.

- GO:0016740: [{"evidenceCode": "ECO:0008006", "id": "ProtNLM2", "properties": [{"key": "model_score", "value": "0.91"}, {"key": "string_match_text", "value": "GO:0061656"}, {"key": "string_match_location", "value": "GO"}, {"key": "string_match_type", "value": "hydrated"}], "source": "Google"}]

## Research execution

The original Falcon attempt failed with HTTP 429 (rate limit), and the configured Perplexity-lite fallback failed with HTTP 401 (insufficient quota). No provider report was returned for this gene, and no duplicate provider request was submitted. The companion deep-research-manual.md is an explicitly manual synthesis of inspected sources, not provider output.

## Modifier specificity and donor

The PAINT SUMO-E2 node is PANTHER:PTN000629675. The UBC catalytic fold alone is insufficient to discriminate ubiquitin from SUMO. A direct comparative sequence analysis in NCU04302-bioinformatics therefore checks the target against reviewed human/fission-yeast Ubc9 and the recorded Arabidopsis ubiquitin-E2 donor P42745. PMID:9435231 demonstrates Ubc9 SUMO thioesters; PMID:16339806 reports Arabidopsis ubiquitin E2s and includes UBC1–6 activity. The donor’s reviewed function string exactly matches the paragraph. This records sequence/text provenance, not a claim about the model’s internal reasoning. QuickGO definitions cached in NCU04302-go-definitions.json distinguish isoenergetic SUMO and ubiquitin E2 transfer from the ATP-coupled ligase definition; E1 activation is a separate reaction step.

## Ubc9-specific evidence and complex definition

Exact sequence-classification excerpts: “DR   CDD; cd23798; UBCc_UBE2I; 1.” and “DR   FunFam; 3.10.110.10:FF:000035; SUMO-conjugating enzyme ubc9; 1.” The independent full-length reference comparison and all parameters are in NCU04302-bioinformatics/RESULTS.md. PMID:12597774 supplies direct SUMO-conjugation experiments on the 75%-identical fission-yeast Ubc9 reference. GO:0106068 was checked in QuickGO and includes a SUMO-protein transferase with specificity-associated proteins; stable residence is not required. PMID:17466333 describes the conserved SUMO E2 interactions with substrate and E3 ligase during conjugation, supporting broad SUMO ligase-complex membership.

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not consulted. Deep research: only the existing manual synthesis is present (earlier Falcon/Perplexity attempts failed, see above); no new provider run was made, and this re-review relied on the cached primary literature listed below.

### Identity
- Q1K772 is the complete, canonical NCU04302 product: 157 aa, UBC core 3-156 (PROSITE PS50127), catalytic glycyl-thioester Cys92 present (sequence position 92 = C, checked). Same length as fission-yeast Hus5 (P40984, 157 aa) and budding-yeast UBC9 (P50623, 157 aa). Not a fragment, isoform or alternative gene model.

### Evolutionary placement
- PANTHER 19 geneinfo API: Q1K772 and P40984 are both PTHR24067:SF248 (official name "DORSAL INTERACTING PROTEIN 4", a member-dominated label). The local PANTHER 19 classification files place S. cerevisiae UBC9 P50623, S. pombe hus5 P40984, Candida UBC9, Dictyostelium ubc9, Drosophila lwr and C. elegans ubc-9 in SF248; vertebrate UBE2I orthologs (human P63279 etc.) are in SF280 "SUMO-CONJUGATING ENZYME UBC9". Both subfamilies descend from the PAINT Ubc9 node PTN000629675 (taxon Eukaryota), which carries IBD nucleus, SUMO conjugating enzyme activity and protein sumoylation, with seeds from both subfamilies. So the core SUMO-E2 function is inherited eukaryote-wide, and NCU04302 is in the same subfamily as both yeast Ubc9s.
- PAINT did NOT propagate heterochromatin, DNA repair or SUMO ligase complex at PTN000629675. Those rows here come only from Ensembl Compara transfer from PomBase hus5; treated as non-core.
- interpro/panther/PTHR24067/PTHR24067-review.yaml makes no subfamily claim for NCU04302 (family-level coherence note only), so there is no placement disagreement.

### Literature checked
- PMID:11600706 (full text): Hus5 is the conjugator required for in vitro Pmt3 modification ["The Pmt3 modification that we detect requires the presence of added Pmt3-GG (the mature form of Pmt3), the activator (Rad31 + Fub2) and the conjugator, Hus5."]; hus5 mutants are sensitive to DNA damage, and Rad22/Rhp51 are sumoylated in vitro.
- PMID:16168376 (abstract): Hus5 is ChIP-enriched at heterochromatin in a heterochromatin-dependent manner, binding Swi6/Chp2/Clr4 ["chromatin immunoprecipitation (ChIP) revealed that Hus5 was highly enriched in heterochromatic regions in a heterochromatin-dependent manner"].
- Europe PMC search for Neurospora Ubc9/SUMO studies found no gene-specific experimental work on NCU04302.

### Changes made
- GO:0000792 heterochromatin: UNDECIDED -> KEEP_AS_NON_CORE (same-subfamily ortholog ChIP; HP1 and DIM-5/Clr4 are conserved in Neurospora).
- GO:0005694 chromosome: UNDECIDED -> KEEP_AS_NON_CORE.
- GO:0019789 SUMO transferase activity: ACCEPT -> MODIFY to GO:0061656 (is_a ancestor checked in QuickGO; the gene already carries the child term).
- GO:0106068 SUMO ligase complex: ACCEPT -> KEEP_AS_NON_CORE (transient, E3-defined; not propagated by PAINT).
- GO:0006281 DNA repair: kept as KEEP_AS_NON_CORE, now with PMID:11600706 support.
- Unchanged: nucleus (ACCEPT x2), protein sumoylation (ACCEPT x2), SUMO conjugating enzyme activity (ACCEPT x2), ligase activity (MODIFY to GO:0061656; not an ancestor of the E2 term), ubiquitin conjugating enzyme activity (MODIFY to GO:0061656; wrong modifier from EC 2.3.2.23).
- Rewrote the description; added PMID:11600706 and PMID:16168376 to references.

### Relative to review next
- Saccharomyces cerevisiae UBC9 (P50623, SGD:S000002222): same PANTHER subfamily SF248, a PAINT seed at PTN000629675, the best-characterised SF248 member (PMID:9435231 shows SUMO thioester formation by yeast UBC9), and Saccharomycotina is the sister group of the Pezizomycotina. No review exists in the repo (no genes/yeast/UBC9). Fission-yeast hus5 (P40984) is an equally valid same-subfamily alternative and is also unreviewed.

### Modules
- No SUMO-pathway module exists. modules/dmel_smc5_6_complex.yaml mentions SUMO (Nse2 SUMO E3) but is Drosophila-specific; modules/ubiquitin_transfer_relay.yaml covers ubiquitin E1-E2-E3 relay, not SUMO. Neither is a direct fit.
