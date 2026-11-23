# FBXL20 (donkey, A0A9L0IQA3) notes

## Sources
- Donkey UniProt A0A9L0IQA3 (unreviewed; names, subunit and location are ARBA predictions, ECO:0000256).
- Human ortholog Q96IG2 (genes/human/FBXL20/FBXL20-uniprot.txt) and human review genes/human/FBXL20/FBXL20-ai-review.yaml.
- Sequence comparison: FBXL20-bioinformatics/RESULTS.md.

## Biology
- FBXL20 is an F-box/LRR substrate receptor of SCF E3 ligases: [file:human/FBXL20/FBXL20-uniprot.txt "Substrate-recognition component of the SCF (SKP1-CUL1-F-box"]; [PMID:34731788 "an F-box protein that serves as a substrate recognition component of the SCF (Skp1_Cul1_F-box) E3 ubiquitin ligase complexes that promote proteasomal degradation"].
- Substrates: VPS34/PIK3C3 after DNA damage, leading to autophagy inhibition [PMID:33234069 "Removal of Vps34 by Fbxl20-mediated ubiquitination leads to inhibition of autophagy."]; PR55alpha/PPP2R2A, a PP2A regulatory subunit [PMID:34731788 "FBXL20 interacts with PR55α in vitro and in vivo"].
- FBXL20 is the paralogue of FBXL2 [PMID:33234069 "Fbxl20 is considered a paralogue for Fbxl2"].
- Mouse ortholog (Scrapper) acts at the presynapse (By similarity in human UniProt: "Role in neural transmission").

## Donkey sequence
- 97.25% identity over the full human length; 12-aa N-terminal insertion upstream of the F-box; C-terminal CAAX-type motif (…CCIIL) identical [file:EQUAS/FBXL20/FBXL20-bioinformatics/RESULTS.md].

## Decisions
- cytoplasm (SubCell mapping): ACCEPT.
- SCF ubiquitin ligase complex (TreeGrafter): ACCEPT.
- SCF-dependent proteasomal ubiquitin-dependent protein catabolic process (TreeGrafter): ACCEPT.
- NEW ubiquitin-like ligase-substrate adaptor activity (GO:1990756), matching the human review's MF.

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

### Deep research
- `just deep-research EQUAS FBXL20 --provider falcon --fallback perplexity-lite` failed: falcon "Exception: Failed to authenticate"; perplexity-lite HTTP 401 insufficient_quota. No deep-research file was created. Proceeded with cached literature (PMID:17803915 newly cached with full text, PMID:34731788, PMID:33234069) and the human FBXL20 review.

### Identity of A0A9L0IQA3
- 448 aa, unreviewed (PE 4). PANTHER PTHR13318:SF47 (F-BOX_LRR-REPEAT PROTEIN 20), the same subfamily as reviewed human Q96IG2, mouse Q9CZV8 and bovine Q58DG6 (interpro/panther/PTHR13318/PTHR13318-entries.csv).
- It is an alternative-first-exon gene model, not the canonical product: the first 26 residues (MRSVLVPQLPSMQAVIFKATAHLGIG) replace the canonical 14-residue start (MRRDVNGVTKSRFE); downstream of the conserved MFSNSDEAV motif it has the canonical 422-residue body with F-box, complete LRR domain and CAAX tail [file:EQUAS/FBXL20/FBXL20-bioinformatics/RESULTS-rereview.md "is an alternative first exon (alternative gene model), not an insertion."]. The earlier "12-residue insertion" wording in RESULTS.md is superseded (RESULTS.md left unchanged).
- Horse F6YIL4 starts with the same alternative segment; other donkey models use other first exons. No donkey model combines the canonical start with an intact F-box, and there is no reviewed donkey FBXL20, so the canonical reviewed product for the gene is human Q96IG2 (reviewed, COMPLETE in genes/human/FBXL20).

### Evolutionary grounding
- TreeGrafter node PTN002541195 gives SCF complex and SCF-dependent catabolism; mouse Fbxl20 gets the same two terms by IBA from PAINT node PTN002547163 (seeds include Arabidopsis, yeast, fly, mouse, human F-box/LRR proteins). PAINT placed GO:1990756 at other PTHR13318 nodes (PTN004419270, PTN009029653) but not on the FBXL20 lineage, whose members have no experimental MF annotation besides protein binding (mouse IPI with RIM1). I read that as missing descendant evidence, not a curated exclusion, so the NEW adaptor-activity MF is kept, supported by the mouse and human experiments.
- Mouse SCRAPPER [PMID:17803915 "Similarly, SCRAPPER formed an SCF complex with Skp1 and Cullin1 in mouse brain lysates"]; [PMID:17803915 "In neurons from Scrapper -knockout (SCR-KO) mice, RIM1 had a longer half-life with significant reduction in ubiquitination, indicating that SCRAPPER is the predominant ubiquitin ligase that mediates RIM1 degradation."].
- Mouse synaptic terms (presynapse, glutamatergic synapse, regulation of synaptic vesicle exocytosis) are neural-context roles of the ortholog and were not proposed for donkey.

### Decisions (re-review)
- cytoplasm: ACCEPT (unchanged; added CAAX/membrane context).
- SCF ubiquitin ligase complex: ACCEPT (now supported by mouse experimental SCF complex data).
- SCF-dependent proteasomal ubiquitin-dependent protein catabolic process: ACCEPT (mouse RIM1 KO data added).
- NEW GO:1990756 ubiquitin-like ligase-substrate adaptor activity: kept.
- Description rewritten to describe the alternative first exon and the mouse presynaptic role.

### Relative and family
- Next relative: mouse Fbxl20/SCRAPPER Q9CZV8 (ortholog, same PANTHER subfamily SF47; strongest experimental data). No review exists in the repo. Human Q96IG2 already has a complete review.
- Family placement note: rat Fbxl20 Q9QZH7 (276 aa, reviewed) is placed in PTHR13318:SF95 (F-BOX PROTEIN YLR352W) rather than SF47, unlike the human, mouse and bovine orthologs; likely a consequence of its truncated sequence. No PANTHER family review file (FamilyReview) exists under interpro/panther/PTHR13318/.
- Modules: no module includes FBXL20. modules/mitophagy.yaml cites PTHR13318 only through subfamily SF152 (a different F-box/LRR protein), so it is not an FBXL20 module.
