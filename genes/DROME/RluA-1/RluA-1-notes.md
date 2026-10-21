# RluA-1 evidence notes

Q9VKV0 is the 739-residue PA/PB/PC protein of FBgn0051719. FlyBase reports all three sequences as identical; PD is a distinct 378-residue protein (M9PCT9) and is not the benchmark target. [FlyBase](https://flybase.org/reports/FBgn0051719).

[PMID:33028630](https://pmc.ncbi.nlm.nih.gov/articles/PMC7718762/) is cached with full text. Crucially, its sequence-analysis methods explicitly identify “RluA-1-PABC_Dm: Q9VKV0”, so the conservation analysis applies to this exact native protein. The reported conserved catalytic residues support pseudouridine-synthase function even without a purified-target assay. The same article explicitly leaves target RNAs unresolved. Thus general activity/process annotations are retained, whereas rRNA and tRNA-position-specific assignments remain uncertain; a conserved catalytic core is not a substrate-recognition map.

The protein GFP exon trap localized to nuclei; this is distinguished from membrane-tethered GFP driven by a regulatory reporter. The paper also reports null, neuron-specific RNAi and cDNA rescue experiments establishing hypersensitive thermal/mechanical nociception following RluA-1 loss. These justify proposed nucleus and negative-regulation-of-nociception annotations. GO:1904057 was verified through QuickGO as “negative regulation of sensory perception of pain”; its definition describes reducing the frequency, rate or extent of sensory perception of pain. The phenotype does not prove the RNA substrate mediating that role.

The original ProtNLM pseudouridine-synthesis prediction is CNN, not UNC from the absence of a target assay and not LSP based on unverified substrate-specific terms. The decisive source is the published target-resolved sequence comparison, not an automated activity label.

The Falcon report completed but missed the central 2020 Drosophila study (PMID:33028630). Its statements that no fly localization, phenotype or target-specific conservation study were found are therefore incomplete. The directly inspected full text supplies the nuclear, genetic-rescue and catalytic-conservation evidence used here. The report's caution about exact RNA substrates remains appropriate. The original provider artifact is preserved unchanged.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

Identity: Q9VKV0 is the 739-aa canonical RluA-1 product (FlyBase PA/PB/PC, identical sequences); not a fragment or alternative model. Pfam PF00849 domain 385-531; UniProt ACT_SITE Asp428 (verified D in sequence; the paper's model numbers it D426). The 378-aa PD product (M9PCT9) is a separate entry.

Evolutionary placement: PANTHER PTHR21600:SF40 (PSEUDOURIDYLATE SYNTHASE RPUSD2). Characterized SF40 members: yeast Rib2/Pus8 (Q12362, cytoplasmic tRNA Psi32) and Pus9 (Q12069, mitochondrial tRNA Psi32) [PMID:15466869 "two enzymes, Rib2/Pus8p and Pus9p, are required for Psi32 formation in cytoplasmic and mitochondrial tRNAs, respectively"]; human RPUSD2 (Q8IZ73) [PMID:41698914 "RPUSD2 pseudouridylates Ψ31 of mt-tRNALeu(CUN), Ψ32 of mt-tRNAPro and mt-tRNACys"; PMID:41136621 "Compared with bacterial RluA, eukaryotic RPUSD2 has lost its activity towards rRNAs, while its function on tRNA Ψ32 is well maintained."]. The fly paralog RluA-2 (Q9VKU8) is also in SF40, so fly has a lineage duplication; human RPUSD2 is the co-ortholog.

Changes vs prior review:
- GO:0000455 rRNA pseudouridine synthesis (IBA, deep node PTN002727951 seeded by bacterial and Pus5 rRNA enzymes): UNDECIDED -> MARK_AS_OVER_ANNOTATED (SF40 diverged to tRNA; RPUSD2 lost rRNA activity).
- GO:0160151 tRNA Psi32 synthase: UNDECIDED -> ACCEPT on subfamily-wide conservation (yeast both paralogs + human); now the core MF. Generic GO:0009982 rows and the general process/RNA binding rows -> MODIFY to GO:0160151 / GO:0031119.
- GO:0160152 tRNA Psi31: UNDECIDED -> KEEP_AS_NON_CORE (single human mt-tRNA site, consequence of first-unpaired-U specificity).
- Nucleus (IDA, GFSTF exon trap of the endogenous gene) kept as NEW.
- Dropped the previously proposed NEW GO:1904057 negative regulation of sensory perception of pain: hyperalgesia is an organismal phenotype of loss of an RNA-modifying enzyme with unknown target (and accompanied by dendrite hyperbranching); FlyBase curated this paper for expression/phenotype but not for this GO process. Moved to suggested_questions.
- Description rewritten; references added (PMID:15466869, 41136621, 41698914; 35051350 fetched but not cited).

Falcon deep research not used as support (it missed PMID:33028630, see above). PANTHER family review (interpro/panther/PTHR21600) places RluA-1 in SF40 as well; no placement disagreement, though its SF40 description does not mention the tRNA Psi32 specificity. Relative to review next: human RPUSD2 (Q8IZ73), no review in repo.
