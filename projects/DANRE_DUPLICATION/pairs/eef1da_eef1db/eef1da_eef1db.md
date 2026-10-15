---
title: "eef1da / eef1db"
autolink_gene_symbols: false
---

# eef1da / eef1db

[Back to pairs](../README.md)

**Bottom line:** UNRESOLVED. No zebrafish experiment on either copy exists. Both proteins keep
the eEF1B-delta core intact: the catalytic GEF regions are 89% identical to each other and about
80% identical to human EEF1D. Both genes are expressed strongly in every tissue Bgee records.
The only difference in expression is that eef1da is higher in oocytes and early embryos.
The 40.5% whole-protein identity is misleading, because the reviewed entries are long isoform
models with N-terminal extensions that have diverged. The evidence cannot tell backup, dosage and
partition apart.

**Sample record:** fate=UNRESOLVED; level=none; evidence=expression_only; identity=40.5%

| | eef1da | eef1db |
|---|---|---|
| UniProt | A0A8M6Z1P2 (TrEMBL; RefSeq model XP_017214236.2, long isoform, 463 aa) | A0A8M2B7W1 (TrEMBL; RefSeq models XP_005160975.1/XP_017207982.1, long isoform, 578 aa) |
| Short isoforms in UniProt | A0A0R4IA30 (245 aa), A0A8M2BAX4 (269 aa), A0A8M2BAS2 (291 aa) and others | Q5SPD1 (274 aa), Q5SPD0 (298 aa) and others |
| Human ortholog | EEF1D | EEF1D |
| Chromosome (UniProt proteome) | 2 | 20 |
| ZFIN | ZDB-GENE-040426-2740 | ZDB-GENE-030131-6544 |
| GOA rows | 6 (IEA/IBA only) | 6 (IEA/IBA only) |
| Review | [genes/DANRE/eef1da](../../../../genes/DANRE/eef1da/eef1da-ai-review.yaml) | [genes/DANRE/eef1db](../../../../genes/DANRE/eef1db/eef1db-ai-review.yaml) |

Drawn at random (draw 1, seed 20260928) from the 778 clean 1:1 `TGD_tree` pairs
(`batch3_sample.tsv`).

## 1. Evidence the pair comes from the TGD

**PANTHER.** The row in `panther_tgd_pairs.tsv` is:

| tgd_call | branch | class | family | human orthologs (a / b) | gar co-orthologs | medaka co-orthologs | medaka parallel dup |
|---|---|---|---|---|---|---|---|
| TGD_tree | Neopterygii\|Teleostei | 1:1 | PTHR11595 ("EF-HAND AND COILED-COIL DOMAIN-CONTAINING FAMILY MEMBER") | EEF1D(O) / EEF1D(LDO) | 1 (same gar gene for both) | 2 | (blank) |

**The PANTHER family label is wrong for these proteins and I do not use it.**
`interpro/panther/panther.obo` names PTHR11595 "EF-HAND AND COILED-COIL DOMAIN-CONTAINING FAMILY
MEMBER". Both zebrafish proteins instead carry the EF-1 beta/delta signatures:

- InterPro IPR014038 (EF1B beta/delta GEF domain), IPR049720 and IPR001326;
- UniProt family "EF-1-beta/EF-1-delta";
- no EF-hand.

The subfamily names are consistent with the gene: SF88 is "ELONGATION FACTOR-1, DELTA, A ISOFORM
X1" (eef1da), SF86 is "ELONGATION FACTOR 1-DELTA ISOFORM X1" (eef1db), and the obo also has SF19,
"ELONGATION FACTOR 1-BETA_1-DELTA 2-RELATED". The family placement is plausible and the label is
the anomaly. I did not trace where the label comes from.

**Literature.** I found no synteny or phylogeny paper on teleost EEF1D.

**Status.** TGD origin rests only on the PANTHER gene tree. It is a `TGD_tree` call with a single
gar co-ortholog and two medaka co-orthologs, the project's strictest criterion. No double-conserved
synteny check was done.

## 2. Protein-level comparison

Source: [eef1da-bioinformatics/RESULTS.md](../../../../genes/DANRE/eef1da/eef1da-bioinformatics/RESULTS.md).

- **Why 40.5% is misleading.** EEF1D makes short isoforms: the eEF1B subunit, 281 aa in human.
  It also makes a long isoform with an N-terminal extension, eEF1BdeltaL, 647 aa in human:
  [PMID:36576126 "EEF1D is alternatively spliced giving rise to one long and three short isoforms."]
  Both reviewed zebrafish accessions are long-isoform RefSeq models of different lengths (463
  and 578 aa). The shortest isoforms of the two genes are 62.8% identical.
- **The core is conserved.** Mapped onto human coordinates, the paralogs are identical at 71.9% of
  core positions, 61.1% of the leucine zipper and **89.0% (97/109) of the catalytic GEF region**.
  Against human, the GEF region is 78.0% identical for eef1da, 80.7% for eef1db and 83.5% for
  gar. Every isoform of both genes has the complete GEF region.
- **Family function.** The GEF domain is the conserved part of the family:
  [PMID:10375624 "EF-1beta and EF-1delta are homologous in their C-terminal domain."]
  [PMID:8334168 "The human EF-1 delta sequence shows a strong conservation in its C-terminal domain."]
  [PMID:36576126 "the eEF1B complex acts as a guanine exchange factor (GEF) of GTP for GDP indirectly catalyzing the release of eEF1A from the ribosome."]
- **The long-isoform extension.** In mammals the long isoform works as a nuclear heat-shock
  cofactor:
  [PMID:21597468 "The long isoform of eEF1Bδ (eEF1BδL) is localized in the nucleus and induces heat-shock element (HSE)-containing genes in cooperation with heat-shock transcription factor 1 (HSF1)."]
  A review states that it is absent below reptiles:
  [PMID:25686034 "The orthologs of eEF1BδL are not found in reptiles or lower species."]
  My comparison uses a composition-matched shuffle control:
  - Gar EEF1D (W5MPR4, 676 aa) has an extension clearly similar to the human one (44.5% identity
    against a shuffled maximum of 36.9%).
  - eef1db's extension is modestly above background (34.7% against 31.8%).
  - eef1da's extension is not distinguishable from background (36.7% against 38.2%).
  - The two zebrafish extensions are only 22.8% identical where both align.

  So the gene models suggest that a long isoform existed before the TGD, which contradicts the
  review. They also suggest that its extension has diverged more in eef1da. All of these are
  computational gene models. Nobody has shown a fish long isoform protein or its function.
- **Comparator.** Allotetraploid *Xenopus laevis* keeps two EF-1 delta proteins, and both are in
  the same complex:
  [PMID:8647113 "Both EF-1 delta proteins are simultaneously present in oocytes extracts, at a molecular ratio around 1:10 for p34 versus p36 proteins."]

**Does each copy keep the ancestral molecular function?** Almost certainly, for the eEF1B GEF
function, judging from the intact and highly conserved catalytic region. For the long-isoform
nuclear function this is unknown, and it is the most likely place for protein-level divergence
between the copies.

## 3. Expression

- **Bgee** (RESULTS.md). Both genes are called expressed in the same 29 anatomical entities, with
  scores above 97 in their top tissues. eef1da is higher in 22 of 29 entities, mostly by a
  little. The large differences are maternal and early: cleaving embryo 91.6 vs 64.7, mature
  ovarian follicle 98.2 vs 73.0, early embryo 97.1 vs 74.5 and blastula 96.6 vs 76.1. eef1db is
  a little higher in retina, brain, eye and paraxial mesoderm.
- **ZFIN.** Only high-throughput whole-mount in situ rows exist: one for eef1da and two for eef1db,
  whole organism, 1-cell to pec-fin.
- **Tetrapod single-copy gene.** Human EEF1D short isoforms are ubiquitous:
  [PMID:30787422 "EEF1D encodes a ubiquitously expressed translational elongation factor functioning in the cytoplasm."]
  The long isoform is brain- and testis-enriched in mammals:
  [PMID:25686034 "Furthermore, eEF1BδL RNA and eEF1BδL protein are enriched in brain and testis [5]."]
  Whether the zebrafish long isoforms show tissue bias is unknown. Bgee calls are made per gene,
  not per isoform.

This is complete overlap at organ level, with a quantitative maternal bias toward eef1da.

## 4. Experimental evidence of function

None in zebrafish. No mutant, morphant, rescue or biochemical study of either copy was found in
Europe PMC. The GO annotations are all IEA or IBA. Human data (GEF role, intellectual-disability
variants in both the long-isoform exon and the GEF domain, ER anchoring of the short isoforms)
describe the single-copy gene only:
[PMID:36576126 "Pathogenic variants localized in both the alternatively spliced domain or the GEF domain of EEF1D cause a severe neurodevelopmental disorder with microcephaly and spasticity."]
[PMID:42230146 "In this study, we show that short EEF1D isoforms containing exon 5 interact with the ER-resident scaffold protein KTN1 and RRBP1, thereby anchoring the EEF1B complex to the ER."]

## 5. Fate classification

**UNRESOLVED. Confidence in any specific fate: none.**

**Established**

- A TGD-branch duplication (PANTHER tree only).
- Both copies keep an intact, highly conserved eEF1B-delta GEF core.
- Both genes are broadly co-expressed, and eef1da has more maternal and early-embryo signal.

**Suggestive, not shown**

- The long-isoform N-terminal extensions have diverged between the copies, and eef1da's is not
  recognizably homologous to the mammalian one. If fish make long isoforms, this is where a
  partition or loss at the protein level would sit.
- The maternal bias hints at a quantitative expression split for early translation. It is not a
  partition: eef1db is also expressed at those stages.

**Why no fate can be called**

- *Backup and dosage.* These fit the conserved core and the co-expression. The two cannot be told
  apart, and neither can be told from a hidden partition, without loss-of-function data.
  Duplicated translation-machinery genes are often kept for dose, but that is a prior, not
  evidence for this pair.
- *Partition and innovation.* There is no functional evidence either way.

**What data would resolve it**

- Single and double mutants, including RNA-less alleles to avoid transcriptional adaptation,
  scored for viability, growth and global translation. Lethality or reduced translation only in
  the double mutant would mean BACKUP or DOSAGE. Double heterozygotes would separate the two.
- Paralog-resolved proteomics of eEF1B complexes in oocytes, embryos and adult tissues, to show
  whether both proteins assemble and in what ratio.
- Isoform-resolved long-read RNA-seq, to show whether either gene makes the long isoform and in
  which tissues. Gar expression would give the ancestral state.

## 6. GO annotation consistency across the pair

Source: [annotation-comparison.md](annotation-comparison.md), after both reviews.

- The annotation sets are identical: six rows each, same terms, same evidence codes (InterPro2GO
  IEA and the same PAINT node PTN000174394), all accepted. The terms are guanyl-nucleotide
  exchange factor activity, translation elongation factor activity, translational elongation,
  cytosol and the eukaryotic translation elongation factor 1 complex.
- Same-node IBA propagation suits the conserved GEF core, which is what those terms describe.
- **Missing from both.** Neither copy has any zebrafish experimental annotation. Neither has a term
  for the long-isoform nuclear or heat-shock function. I added none: the fish long isoform is
  unverified, and its extension is not clearly conserved in eef1da.
- **Should be copy-specific:** nothing is known.
- The PANTHER family label (section 1) does not affect GO propagation, which runs through the PTN
  node, but it could mislead anyone reading family names.

## 7. Open questions

- Are the long isoforms translated in zebrafish? Does either copy's extension carry the nuclear
  localization and HSF1-cooperating activity described for mammalian eEF1BdeltaL?
- Does the maternal bias toward eef1da show up at the protein level in the oocyte eEF1B complex?
- Are eef1da and eef1db mutants viable alone? Is the double mutant lethal?
- Why does PANTHER label PTHR11595 "EF-hand and coiled-coil domain-containing"? Does the
  family include non-EF1B members?

## References

PMID:8334168, PMID:8647113, PMID:10375624, PMID:21597468, PMID:25686034, PMID:30787422,
PMID:36576126, PMID:42230146. Also the files `panther_tgd_pairs.tsv`, `batch3_sample.tsv`,
`interpro/panther/panther.obo`, [annotation-comparison.md](annotation-comparison.md) and
[eef1da-bioinformatics/RESULTS.md](../../../../genes/DANRE/eef1da/eef1da-bioinformatics/RESULTS.md).
