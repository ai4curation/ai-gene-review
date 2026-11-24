# tmc2b notes (Danio rerio, transmembrane channel-like 2b; UniProt F1QZE9)

## 2026-09-28 — session log (DANRE_DUPLICATION batch 3, random TGD_tree sample)

**Deep research:** not available (Edison/Falcon 402 Payment Required; OpenAI key invalid). Not attempted, per
instructions; literature searched by hand via Europe PMC. Most shared pair literature and the pair analysis are
recorded in `../tmc2a/tmc2a-notes.md` and `../tmc2a/tmc2a-bioinformatics/RESULTS.md`.

Accession F1QZE9 (Swiss-Prot TMC2B_DANRE, 892 aa), ZFIN:ZDB-GENE-060526-262, Ensembl ENSDARG00000030311,
chr5:25.62 Mb, adjacent to tmc1: [PMID:32371604 "High-frequency homologous recombination of tmc2a and tight linkage of the tmc1 and tmc2b genes (5 kb apart) allowed us to produce the double-mutant combination tmc1 Ex3 , + 1bp(1) / tmc2b sa8817 from the tmc1 Ex3 , + 1bp(1) / tmc2a Ex4 , − 23bp / tmc2b sa8817 triple-mutant line."]

### Expression
- Neuromasts: [PMID:25114259 "In the lateral-line neuromasts, only tmc2b was robustly detected by in situ hybridization"]
- Inner ear: peripheral/extrastriolar with tmc1 [PMID:38035267 "In the larval saccule and crista, tmc2b is predominantly expressed in peripheral hair cells, either outlining the entire saccule or at both ends of the cristae (Figures 3E,F)."]
- Not regulated by prdm1a (ear/lateral-line fate switch): [PMID:40825768 "On the other hand, the paralog tmc2b is highly expressed in the sibling and prdm1a mutant lateral line hair cells, suggesting that it is not regulated by prdm1a (Supplementary Fig. 2l)."]
- Adult: ear only among adult tissues tested by RT-PCR [PMID:25114259 "RT-PCR from RNA isolated from various adult tissues revealed that tmc1 , tmc2a , and tmc2b transcripts were detectable only in adult ear tissue ( Fig."]
- Bgee (my expression_compare.py) reports tmc2b in neuromast hair cells (in situ) plus low bulk RNA-seq calls in
  muscle and tail; tmc2a has no Bgee calls. Bulk calls are not hair-cell resolved and are not used for fate calls.

### Protein / localization
- [PMID:29269857 "First, by transgenesis, we showed that full-length Tmc2b fused to GFP localizes to the tips of neuromast stereocilia (Fig. 2a, b), fulfilling a key requirement of being a component of the mechanotransduction apparatus in zebrafish hair cells."]
- Needs Tomt and Tmie for bundle targeting (PMID:28534737, PMID:30726219); does not need Lhfpl5 (PMID:32009898).

### Function
- Alleles: TALEN PTC allele (Chou 2017; truncated 148 aa), cwr2 (5-bp del exon 7, in the double), cwr8, sa8817 (ENU nonsense).
- Lateral line: [PMID:29269857 "94 ± 1.2% (n = 55) of control hair cells loaded fluorophore; in contrast, 35 ± 1.8% (n = 48) of tmc2b −/− hair cells loaded (Fig. 3d), confirming Tmc2b is absolutely required for a subpopulation of hair cells within a single neuromast."]
- Hearing unaffected in single mutant: [PMID:29269857 "In mutants, no defects in hair bundle morphology (Supplementary Fig. 2a–d) or hearing (Supplementary Fig. 2f, g) were observed."]
- No paralog upregulation: [PMID:29269857 "These findings indicate that these genes are not upregulated in response to genetic inactivation of tmc2b."]
- Vestibular: [PMID:32371604 "The two double-mutant combinations that gave rise to a deficit included the tmc2b sa8817 allele, suggesting that Tmc2b is the primary contributor to vestibular end organ function."]
- Rescue of triple mutant by Tmc2b transgene (PMID:32371604) and of tmc2b sa8817 by Tmc2b-GFP (PMID:28534737).

### Annotation decisions
- GO:0050910 IMP/IGI from Chou 2017 → MODIFY to GO:0050974 (lateral-line data; the single mutant hears normally).
- IEP development terms (inner ear morphogenesis, inner ear development, neuromast development) → REMOVE.
- NEW: stereocilium tip (IDA, PMID:29269857).
