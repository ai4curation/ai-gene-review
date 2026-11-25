# prom1b notes (Danio rerio, prominin 1 b; UniProt A0A8M2BI60)

## 2026-09-28 — session log (DANRE_DUPLICATION batch 4, random TGD_tree sample)

**Deep research:** not available (Edison 402 Payment Required; OpenAI key invalid). Not attempted, per
instructions. Shared literature in `../prom1a/prom1a-notes.md`; pair analysis in
`../prom1a/prom1a-bioinformatics/RESULTS.md`.

Accession A0A8M2BI60 (TrEMBL; RefSeq XP_005170970.1 isoform X8, 867 aa; alias proml2 in UniProt),
ZFIN:ZDB-GENE-031003-1, Ensembl ENSDARG00000034007, chr1. The PANTHER table lists UniProt A0A8M9QBM3 for this
gene; the review uses the accession with GOA rows. Jaszai et al. identify the originally cloned cDNA:
[PMID:21407811 "Dr prominin-1b (AF373869) therefore corresponds to splice variant s21 (Table S5)."]

### Expression
- More robust than prom1a in retina: [PMID:21407811 "Of the two prominin-1 paralogues, expression of prominin-1b appeared to be more robust in line with gene expression profiling reported earlier on embryonic retina [33]."]
- Adult brain, caudal: [PMID:23723983 "Note that major sites of expression of prominin-1a are mainly located in the prosencephalic (rostral) and dorsal mesencephalic (tectal) domain (A), whereas prominin-1b is predominantly found in the rhombencephalic brainstem (caudal) domain (B)."]
- Bulk: zygotic only, rising to 26-49 TPM at 3-5 dpf (E-ERAD-475); Bgee calls only retina, brain, larva,
  embryo, bone. Photoreceptor scRNA: rods 6.5 CP10K, cones 1.1-2.1 CP10K, 3-4x prom1a.

### Function
- Knockout: [PMID:31362982 "Loss of prom1b disrupted OS morphogenesis, with rods and cones exhibiting differences in impairment: cones degenerated at an early age, whereas rods remained viable but with an abnormal OS, even at 9 months postfertilization."]
- Prph2: [PMID:31362982 "Moreover, we found that Prom1b deletion causes mislocalization of Prph2 and disrupts its oligomerization."]
- Allele (full text on PMC, not cached): TALEN 4-bp deletion c.174_177delACCA, p.Pro59Valfs*62; prom1b mRNA reported decreased at 7 dpf in the mutant (the sentence is ambiguous about
  which genotype was compared, so I treat it as indicative only); the authors' antibody did
  not work for immunofluorescence, so Prom1b was not localized in photoreceptors.
- Apical marker: Prom1b-GFP transgene in retinal neuroepithelia (PMID:22492354).

### Annotation decisions
- All four rows ACCEPT; photoreceptor outer segment organization (IMP) is the core process.
