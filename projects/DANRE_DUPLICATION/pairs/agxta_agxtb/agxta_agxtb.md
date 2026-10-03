---
title: "agxta / agxtb"
autolink_gene_symbols: false
---

# agxta / agxtb

[Back to pairs](../README.md)

**Bottom line:** PARTITION at the protein level, inferred from sequence only. The ancestral AGT carried two
organelle targeting signals: an N-terminal mitochondrial targeting sequence (MTS) and a C-terminal peroxisomal
signal (PTS1). Spotted gar, coelacanth and tetrapod orthologues all have both. Each zebrafish copy kept one. agxta has a
C-terminal PTS1-like end (SRV) and no MTS, and cannot make one because there is an in-frame stop upstream of its
start codon. agxtb has the gar-like MTS, but its C-terminus (SKA) no longer fits the PTS1 consensus. The catalytic
residues and the liver/kidney/intestine expression are shared. No localization, enzyme or mutant data exist for
either zebrafish protein.

**Sample record:** fate=PARTITION; level=protein; evidence=sequence_only; identity=62.4%

| | agxta | agxtb |
|---|---|---|
| UniProt | Q6DG86 (TrEMBL, 391 aa) | Q6PHK4 (TrEMBL, 423 aa) |
| Human ortholog | AGXT | AGXT |
| Chromosome | 6 | 2 |
| ZFIN | ZDB-GENE-040718-16 | ZDB-GENE-010302-3 |
| Ensembl | ENSDARG00000052099 | ENSDARG00000018478 |
| Predicted targeting | C-terminal PTS1-like (SRV); no MTS | N-terminal MTS (32 aa); no PTS1 (SKA) |
| Review | [genes/DANRE/agxta](../../../../genes/DANRE/agxta/agxta-ai-review.yaml) | [genes/DANRE/agxtb](../../../../genes/DANRE/agxtb/agxtb-ai-review.yaml) |

This pair was drawn at random (batch 4, draw 11, seed 20260928) from the PANTHER `TGD_tree` 1:1 pairs and accepted
because Ensembl Compara dates the duplication to a teleost node (`random_sample.tsv`).

## 1. Evidence the pair comes from the TGD

**PANTHER.** The row in `panther_tgd_pairs.tsv` is:

| tgd_call | branch | class | family | human orthologs (a / b) | gar co-orthologs | medaka co-orthologs | medaka parallel dup |
|---|---|---|---|---|---|---|---|
| TGD_tree | Neopterygii\|Teleostei | 1:1 | PTHR21152 (AMINOTRANSFERASE CLASS V) | AGXT(O) / AGXT(LDO) | 1 (same gar gene for both) | 2 | (blank) |

PANTHER places the duplication after the split from gar and before the zebrafish-medaka split, with a single gar
co-ortholog for both copies.

**Ensembl Compara.** The duplication node is Osteoglossocephalai (`random_sample.tsv`), and one gar gene
(ENSLOCG00000006520) is a one-to-many orthologue of both copies. Each teleost in my panel (the osteoglossomorph
arowana, herring, cavefish, pike, salmon, cod, medaka, stickleback, tilapia) has one one-to-one orthologue of each
zebrafish copy; fugu has only the b-type copy in Compara
([RESULTS.md](../../../../genes/DANRE/agxta/agxta-bioinformatics/RESULTS.md)).

**Synteny.** The two copies lie on chromosomes 6 and 2. Of the 7 genes within 1.5 Mb of agxta that have a
teleost-level zebrafish paralogue, 6 have that paralogue within 1.5 Mb of agxtb (hs2st1, stk25, espnl, amotl2,
sap130, myo7b, each an a/b pair), and the reverse search from agxtb recovers the same 6 pairs
([output.txt](../../../../genes/DANRE/agxta/agxta-bioinformatics/output.txt), section 10). This is a duplicated
chromosome block.

**Status.** TGD origin is well supported: PANTHER `TGD_tree`, a Compara teleost duplication node with one gar
orthologue, retention of both copies from arowana to tilapia, and a conserved paralogous block around both genes.
No published phylogenetic or synteny study of this pair was found.

## 2. Protein-level comparison

- **Identity.** 62.4% identity and 75.2% similarity over 423 columns
  ([annotation-comparison.md](annotation-comparison.md)). Against gar AGXT: agxta 61.5%, agxtb 71.8%.
- **Rates.** Relative to gar, agxta has more lineage-specific changes than agxtb (59 vs 32; chi2 8.01, P<0.05).
  agxta is the faster-evolving copy.
- **Catalytic core.** Both keep the PLP lysine (human K209) and the substrate arginine (human R360). Nothing
  suggests loss of activity in either copy. Fish liver AGT has the substrate range of mammalian AGT1:
  [PMID:6697688 "It was specific for L-alanine and L-serine with glyoxylate and for L-serine with pyruvate as amino acceptor."]
- **Targeting signals (the difference between the copies).**

| Sequence | N-terminal extension (before human Met1) | C-terminal tripeptide |
|---|---|---|
| agxta | none; in-frame stop 16 codons upstream, no upstream ATG | SRV |
| agxtb | 32 aa, Arg-rich (MMPRTVLSRCARLTQQVPLESAL...) | SKA |
| gar AGXT (unduplicated) | 38 aa, Arg-rich (MMQRTLFCRGAFLAQQVALESAL...) | SKV |
| coelacanth / Xenopus / chicken / mouse | 34 / 23 / 24 / 22 aa | NKM / NKM / SRL / NKL |
| human | none (MTS region present but no start codon) | KKL |

Source: [RESULTS.md](../../../../genes/DANRE/agxta/agxta-bioinformatics/RESULTS.md). The same split runs through
the teleost panel: all 10 agxtb orthologues keep an N-terminal extension and 7 of 10 end SKA, while the agxta
orthologues of cavefish, salmon, medaka and stickleback start without an extension. The arowana agxta orthologue
still has an Arg-rich extension, so the MTS may have been lost from the a-lineage after the osteoglossomorph split.

A published survey of the zebrafish peroxisome made the same prediction for the two genes:
[PMID:35295584 "Zebrafish also contains a putative peroxisomal alanine:glyoxylate aminotransferase (AGT) (Agxta, F1QY24 _DANRE) with a weak PTS1 (SRV), a key enzyme to prevent oxalate accumulation (Table 1 and Supplementary Table S3)."]
[PMID:35295584 "Interestingly, zebrafish encode another putative AGT (agxtb, Q6PHK4_DANRE) which lacks a PTS1 but possesses an N-terminal MTS."]
(F1QY24 is a deleted TrEMBL entry whose sequence differs from Q6DG86 at one residue.)

**How the ancestral single gene makes two forms (mammals).** One gene, two start sites:
[PMID:10723739 "AGT targeting is dependent on the variable use of two alternative transcription and translation initiation sites which determine whether or not the region encoding the N-terminal mitochondrial targeting sequence is contained within the open reading frame."]
[PMID:21558762 "Transcription from the upstream start site generates the 1900-nucleotide mRNA for a 45-kDa precursor for SPTm containing a cleavable N-terminal mitochondrial targeting signal of 22 amino acids."]
In zebrafish the two forms are encoded by two genes instead, each with a single start.

**Caveats on the signals.** Human AGT's KKL works only with an internal ancillary signal, which Xenopus AGT lacks:
[PMID:15911627 "The PTS1A is present in all mammalian AGTs studied (human, rat, guinea pig, rabbit, and cat), but not amphibian AGT (Xenopus)."]
Xenopus AGT, which has an MTS and ends NKM, is exclusively mitochondrial:
[PMID:41781394 "The human AGT protein lacks a functional MTS start codon and has been shown to exclusively target the peroxisome27,60, whereas the Xenopus protein exclusively targets the mitochondria61."]
So whether the fish tripeptides SRV and SKV work as PTS1 is uncertain; the peroxisomal prediction for agxta is weaker
than the mitochondrial prediction for agxtb.

**Does each copy keep the ancestral molecular function?** The enzyme activity, yes, by sequence (untested). The
ancestral targeting, no: each copy appears to keep one of the two signals.

## 3. Expression

- **Shared.** Both are liver-dominant with near-identical Bgee scores in liver, spleen, head kidney, intestine and
  bone; one-sided RNA-seq calls (agxta: embryo, integument, mesonephros; agxtb: male organism, gill) are
  moderate-scoring and do not look like a clean tissue split
  ([output.txt](../../../../genes/DANRE/agxta/agxta-bioinformatics/output.txt), section 8).
- **Development (E-ERAD-475).** Both nearly silent until hatching, then rise; agxtb is about three times higher than
  agxta in larvae (day 5: 175 vs 50 TPM).
- **ZFIN.** agxta: liver and pronephric duct by in situ (20-25 somites to day 5); agxtb: RT-PCR only.
- **Gar (pre-duplication).** Gar AGXT has Bgee calls in embryo, larva, liver, mesonephros and intestine, the same
  liver-kidney-gut pattern as both zebrafish copies (Bgee samples 14 gar tissues;
  [bgee_gar_coverage.txt](../../../../genes/DANRE/agxta/agxta-bioinformatics/bgee_gar_coverage.txt)).
- **Fish liver biochemistry.** In an unnamed freshwater fish, hepatic AGT is in both organelles, which is what one
  would expect if the two copies are co-expressed in hepatocytes and sent to different organelles:
  [PMID:8954944 "The present report describes that hepatic alanine:glyoxylate aminotransferase is located both in the peroxisomes and in the mitochondria in fresh water fish, showing that the intracellular localization of the enzyme differs between fresh water fish and marine fish."]
  Which gene products were measured, and in which species, is not stated in the abstract.

No expression partition is evident; the difference between the copies is where in the cell the protein goes, not
where in the body the gene is expressed.

## 4. Experimental evidence of function

None for either copy: no mutant, morphant, localization, or enzyme assay on the zebrafish proteins. The only
experimental GOA row is an estrogen-response IDA on agxtb from a whole-fish microarray, where an AGT probe was
down-regulated by estrogenic compounds:
[PMID:18618001 "Alanine-glyoxylate aminotransferase−1.47NS−0.80−0.85−1.82NSNS−1.014#"]
This shows transcriptional responsiveness, not function. Compensation between the copies has not been examined.

## 5. Fate classification

**PARTITION (subfunctionalization) at the protein level, of subcellular targeting. Confidence: moderate. The
evidence is sequence only, but the pattern is consistent across the teleost panel and matches an independent
published prediction.**

**Established (from sequence)**

- The unduplicated outgroup (gar) and the tetrapods have both an N-terminal MTS-like extension and a C-terminal
  tripeptide; the mammalian gene makes both targeted forms from one locus.
- agxta has lost the extension and has no upstream start; agxtb has kept the extension and has a C-terminus (SKA)
  that does not match the PTS1 consensus. Most agxtb orthologues across teleosts also end SKA.
- Both copies keep the catalytic residues, and their tissue expression overlaps extensively.

**Inferred, not shown**

- That Agxta is peroxisomal and Agxtb mitochondrial in zebrafish cells.
- That gar AGXT (ending SKV) is itself dual-targeted, i.e. that the ancestral C-terminus was a working PTS1 in fish.
  If gar AGXT were mitochondrial only, as Xenopus AGT is, agxta's peroxisomal targeting would be a gain
  (INNOVATION in one copy) rather than a partition.
- That both copies are active enzymes.

**Why not the other fates**

- *Backup or dosage:* the two proteins are predicted to act in different organelles on different glyoxylate pools
  (peroxisomal glyoxylate from glycolate and purine breakdown; mitochondrial glyoxylate from hydroxyproline), so
  they are not interchangeable copies of the same product.
- *Expression partition:* expression overlaps in liver, kidney and intestine.

**What would change the call**

- Localizing tagged Agxta and Agxtb in fish cells: if both went to mitochondria, the pair would move toward
  BACKUP/DOSAGE with a degenerate PTS1 in agxta.
- Localizing gar AGXT: mitochondrial-only gar AGXT would make agxta's peroxisomal form an innovation.

## 6. GO annotation consistency across the pair

Source: [annotation-comparison.md](annotation-comparison.md), after both reviews.

**Shared, and correctly so.** Both activities (L-alanine:glyoxylate and L-serine:pyruvate transaminase), glycine
biosynthetic process and glyoxylate catabolic process (IBA; the activities also IEA) are on both copies and were
accepted on both.

**Asymmetric, and correctly so.** Mitochondrion (ISS from rat Agxt) is on agxtb only, and was accepted; it matches
agxtb's MTS. Peroxisome (IBA) is on both copies: accepted for agxta, marked over-annotated for agxtb (IBA and a
second ISS row from human AGXT). This is the row where same-node IBA propagation cannot see the partition; I recorded
it with a propagation_review (root cause PROPAGATION_BAD, failure mode COMPARTMENT_OR_COMPLEX_MISMATCH). It was not
removed, because neither protein has been localized experimentally.

**Asymmetries that come from which copy was curated.** agxtb has extra ISS rows (glyoxylate metabolic process,
pyruvate biosynthetic process) because a ZFIN curator transferred annotations to it and not to agxta; the same
terms would apply to agxta. The estrogen-response IDA on agxtb was marked over-annotated (a transcript change).

**Should be copy-specific:** peroxisome (agxta), mitochondrion (agxtb). **Should be shared:** both activities,
glyoxylate catabolism and glycine biosynthesis.

## 7. Open questions

- Where do Agxta and Agxtb go in zebrafish cells, and is SRV sufficient for peroxisomal import?
- Is gar AGXT dual-targeted? This decides partition versus innovation.
- Did the a-copy lose its MTS once, or independently in several teleost lineages (arowana agxta keeps an
  Arg-rich extension)?
- Do agxta or agxtb mutants accumulate oxalate, and after which glyoxylate precursor (glycolate versus
  hydroxyproline)?

## References

PMID:6697688, PMID:8954944, PMID:10723739, PMID:15911627, PMID:18618001, PMID:21558762, PMID:35295584,
PMID:41781394. Also `panther_tgd_pairs.tsv`, `random_sample.tsv`, [annotation-comparison.md](annotation-comparison.md),
[agxta-bioinformatics/RESULTS.md](../../../../genes/DANRE/agxta/agxta-bioinformatics/RESULTS.md),
[output.txt](../../../../genes/DANRE/agxta/agxta-bioinformatics/output.txt) and
[bgee_gar_coverage.txt](../../../../genes/DANRE/agxta/agxta-bioinformatics/bgee_gar_coverage.txt).
