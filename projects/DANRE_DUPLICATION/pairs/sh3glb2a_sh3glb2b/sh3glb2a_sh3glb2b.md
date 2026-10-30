---
title: "sh3glb2a / sh3glb2b"
autolink_gene_symbols: false
---

# sh3glb2a / sh3glb2b

[Back to pairs](../README.md)

**Bottom line:** UNRESOLVED. The two endophilin-B2 (SH3GLB2) co-orthologs keep the same domain architecture, evolve
at similar rates and are co-expressed in every adult tissue sampled, as the gar gene is. They differ mainly in level:
sh3glb2b dominates in the zygote and from segmentation onward. No functional data exist for either copy, so backup,
dosage and quantitative partition cannot be told apart.

**Sample record:** fate=UNRESOLVED; level=none; evidence=expression_only; identity=73.6%

| | sh3glb2a | sh3glb2b |
|---|---|---|
| UniProt | A0A8M1N8K5 (TrEMBL, 381 aa; RefSeq NP_001035087.2) | A0A8M9Q303 (TrEMBL, 421 aa; RefSeq XP_021331719.1, isoform X1) |
| Human ortholog | SH3GLB2 (endophilin-B2) | SH3GLB2 (endophilin-B2) |
| Chromosome | 8 | 5 |
| ZFIN | ZDB-GENE-061201-8 | ZDB-GENE-040426-833 |
| Ensembl | ENSDARG00000008983 | ENSDARG00000035470 |
| Review | [genes/DANRE/sh3glb2a](../../../../genes/DANRE/sh3glb2a/sh3glb2a-ai-review.yaml) | [genes/DANRE/sh3glb2b](../../../../genes/DANRE/sh3glb2b/sh3glb2b-ai-review.yaml) |

## 1. Evidence the pair comes from the TGD

**PANTHER.** The row in `panther_tgd_pairs.tsv` is:

| tgd_call | branch | class | family | human orthologs (a / b) | gar co-orthologs | medaka co-orthologs | medaka parallel dup |
|---|---|---|---|---|---|---|---|
| TGD_tree | Neopterygii\|Teleostei | 1:1 | PTHR14167 (SH3 DOMAIN-CONTAINING) | DBNL(O);SH3GLB2(LDO) / DBNL(O);SH3GLB2(O) | 1 (same gar gene for both) | 2 | (blank) |

The PANTHER table used A0A8M6Z0F0 for sh3glb2a, which no longer resolves in UniProtKB; the reviewed accession
A0A8M1N8K5 carries the RefSeq reference protein. The DBNL ortholog calls reflect the broad PTHR14167 family
(SH3-domain proteins), not a relationship specific to this pair.

**Ensembl Compara.** The duplication node is Osteoglossocephalai (`random_sample.tsv`). Both copies share one gar
orthologue (ENSLOCG00000006193) and human SH3GLB2, and each has its own one-to-one medaka orthologue
([RESULTS.md](../../../../genes/DANRE/sh3glb2b/sh3glb2b-bioinformatics/RESULTS.md)).

**Synteny.** The copies are on different chromosomes (sh3glb2a chr8, sh3glb2b chr5). Three neighbouring gene
pairs with teleost-level duplications flank both copies within about 200 kb: zdhhc12a/b, slc25a25a/b and eeig1a/b
([RESULTS.md](../../../../genes/DANRE/sh3glb2b/sh3glb2b-bioinformatics/RESULTS.md)). This is double-conserved
synteny at the zebrafish level; I did not check the gar region directly.

**Literature.** No paper discusses this pair.

**Status.** TGD origin is well supported: PANTHER `TGD_tree`, a Compara duplication at Osteoglossocephalai with a
single gar orthologue, medaka retaining both copies, and three co-duplicated neighbouring genes.

## 2. Protein-level comparison

- **Identity.** 73.6% identity and 81.9% similarity over 421 columns for the reviewed entries
  ([annotation-comparison.md](annotation-comparison.md)). The reviewed sh3glb2b entry is isoform X1, which carries two
  alternatively spliced insertions (about 15 residues in the BAR domain and a proline/serine-rich stretch in the
  linker) that lower the whole-length figure. sh3glb2a and sh3glb2b are 72.9% and 69.2% identical to human SH3GLB2,
  74.9% and 73.7% to gar SH3GLB2, and both are further from SH3GLB1 (58.2% and 55.3%).
- **Domains.** Against human SH3GLB2 the two copies are equally conserved: N-terminal amphipathic helix 85.2% in
  both; BAR domain 76.9% and 78.8%; SH3 domain 88.5% and 86.9%. All three end in the same SH3 sequence
  (...GKVPVTYLELLS). These are the parts that matter in mammals:
  [PMID:28455444 "The endophilin B family of proteins contains an N-terminal Bin/amphiphysin/Rvs (N-BAR) domain that induces membrane curvature to regulate intracellular membrane dynamics."]
  [PMID:28455444 "Interestingly, we found that the N-BAR domain of endophilin B2 is required to rescue EGFR degradation in endophilin B2-deficient cells, whereas the SH3 domain appears to be dispensable"]
- **Rate.** With gar as outgroup, 36 changes are unique to sh3glb2a and 23 to sh3glb2b (chi2 = 2.86, not
  significant at 0.05).
- **Biochemistry and cross-rescue.** None for either zebrafish protein.

**Does each copy keep the ancestral molecular function?** Probably yes for both, on sequence grounds only.

## 3. Expression

From my queries of public resources
([RESULTS.md](../../../../genes/DANRE/sh3glb2b/sh3glb2b-bioinformatics/RESULTS.md),
[output.txt](../../../../genes/DANRE/sh3glb2b/sh3glb2b-bioinformatics/output.txt)); no published expression study.

- **Development (E-ERAD-475, whole embryo).** sh3glb2b is strongly maternal (71 TPM in zygote) and stays at
  10-15 TPM from segmentation to day 5. sh3glb2a is low in the zygote (2 TPM), peaks at blastula (27-28 TPM, about
  equal to sh3glb2b then) and is 2-4 TPM from late gastrula onward.
- **Tissues (Bgee).** Every one of the 20 sh3glb2a calls also has a sh3glb2b call; both are called in brain, retina,
  heart, muscle, gill, intestine, liver, spleen, testis and ovarian follicle. The seven sh3glb2b-only calls come
  mostly from microarray data, and sh3glb2a has no microarray calls at all.
- **ZFIN (high-throughput in situ).** sh3glb2b in central nervous system and eye/lens from mid-segmentation to
  hatching; sh3glb2a recorded only as "whole organism".
- **Pre-duplication state.** Gar SH3GLB2 is called in 14 tissues, highest in eye and brain, and broad otherwise, like
  both zebrafish copies.
- **Tetrapod context.** Mouse endophilin-B2 is broadly expressed, with brain-enriched isoforms:
  [PMID:28455444 "Collectively, these results demonstrate that endophilin B2 is dispensable for murine embryonic development, shares a similar tissue distribution profile with endophilin B1, and exists as three predominant isoforms with isoform 1 ubiquitously expressed and isoforms 2 and 4 enriched in the brain."]

**Shared vs copy-specific.** Adult tissue expression is shared. The differences are quantitative and temporal:
maternal and post-gastrula embryonic expression is mostly sh3glb2b; the blastula peak is shared.

## 4. Experimental evidence of function

- **sh3glb2a, sh3glb2b:** none. Europe PMC returns no paper on either gene; there are no mutants, morphants, double
  mutants or rescue experiments.
- **Mammalian context.** The mouse knockout is viable, and cells lacking endophilin-B2 are slow to move endocytic
  cargo to lysosomes:
  [PMID:28455444 "In this study, we used genetic approaches that revealed that endophilin B2 is not required for embryonic development in vivo but that endophilin B2 deficiency impairs endosomal trafficking in vitro, as evidenced by suppressed endosome acidification, EGFR degradation, autophagic flux, and influenza A viral RNA nuclear entry and replication."]
  Endophilin-B2 also acts with endophilin-B1 in mitophagy:
  [PMID:27112121 "Here we report that EB2 plays an indispensable role in mitochondria sequestration and inner mitochondrial membrane (IMM) protein degradation during mitophagy."]

## 5. Fate classification

**UNRESOLVED; no difference established at either the protein or the expression level (level: none); expression
data only. Confidence in any specific fate: low.**

**Established**

- Both proteins keep the full endophilin-B2 architecture and evolve at statistically similar rates.
- Adult expression is broad and overlapping in both copies, as in gar.
- sh3glb2b is the more highly expressed copy in the zygote and after gastrulation.

**Inferred, not shown**

- Equivalent molecular function (no assay or cross-rescue).
- Whether the level difference matters. Overlapping broad expression with one dominant copy fits dosage retention,
  redundancy (backup), or quantitative subfunctionalization; the data here cannot separate them.

**Why not the other fates**

- *Innovation:* no protein change and no new expression domain.
- *Partition:* no domain has been shown to belong to only one copy; the differences are in level.
- *Backup or dosage:* plausible, but untested; there are no single or double mutant data, and the mouse knockout
  shows the ancestral gene is itself dispensable for development, which would make a phenotype-based test hard.

**What would change the call**

- Double mutants with a phenotype (e.g. in endosome maturation or autophagic flux) and no phenotype in either single
  mutant (RNA-less alleles) would support BACKUP.
- A phenotype in one single mutant only, in a tissue where only that copy is expressed, would support PARTITION.
- Cell-resolved expression showing distinct cell types for each copy.

## 6. GO annotation consistency across the pair

Source: [annotation-comparison.md](annotation-comparison.md), after both reviews.

- **The asymmetry is an artefact of classification, not of biology.** sh3glb2b has four IBA rows (membrane,
  membrane organization, endocytosis, protein-macromolecule adaptor activity); sh3glb2a has none. All UniProt entries
  for sh3glb2a are placed in PANTHER subfamily PTHR14167:SF68 "DREBRIN-LIKE PROTEIN-RELATED", while sh3glb2b is in
  SF106 "ENDOPHILIN-B2 ISOFORM X1", so the endophilin-node IBAs never reach sh3glb2a. Every sh3glb2a UniProt entry has
  only one GOA row, so choosing another accession would not help.
- **Correction proposed.** I added membrane (NEW, ISS, from the pair analysis) to sh3glb2a. I did not add process
  terms; they should come back through a corrected PANTHER placement, which I raise as a suggested question.
- **sh3glb2b decisions.** membrane and membrane organization accepted; endocytosis modified to endosome to lysosome
  transport (GO:0008333), because loss of endophilin-B2 affects trafficking to lysosomes but not internalization;
  protein-macromolecule adaptor activity kept as non-core (deep SH3-superfamily node seeded by SORBS1; the SH3
  domain is dispensable for the best-characterized endophilin-B2 role).
- **Shared:** cytoplasm (IEA) accepted on both.
- **Should be shared:** membrane, membrane organization, endosome to lysosome transport. Nothing here should be
  copy-specific.

## 7. Open questions

- Is the PANTHER subfamily placement of sh3glb2a an error?
- Where are the two copies expressed at cellular resolution, and is sh3glb2a enriched anywhere?
- Is gar SH3GLB2 maternally loaded?
- Do single or double mutants affect endosome maturation or autophagy in zebrafish?

## References

PMID:27112121, PMID:28455444. Also `panther_tgd_pairs.tsv`, `random_sample.tsv`,
[annotation-comparison.md](annotation-comparison.md),
[sh3glb2b-bioinformatics/RESULTS.md](../../../../genes/DANRE/sh3glb2b/sh3glb2b-bioinformatics/RESULTS.md) and
[output.txt](../../../../genes/DANRE/sh3glb2b/sh3glb2b-bioinformatics/output.txt).
