# uap1.S (Q6DCZ6): evidence and exact-input prediction review

The function paragraph assigns UDP-glucose production and glycogen precursor synthesis to a protein with the sequence and substrate-pocket architecture of UAP1. UDP-sugar pyrophosphorylases share related chemistry, but their sugar substrates cannot be interchanged.

## Input identity and functional boundary

Q6DCZ6 is the Xenbase-linked uap1.S product, not UGP2. Its 507-residue sequence aligns across the human UAP1 reference Q16222 with 382 identities among 505 aligned residues. All annotated reference nucleotide-sugar contact positions are conserved. A 17-residue human segment is absent from the alignment, similar in size to the known human UAP1 isoform insert; this does not identify the frog product as a particular human isoform or determine its substrate ratio. The model donor O35156 is UGP2.

## Biological evidence

- [PMID:9603950 — The eukaryotic UDP-N-acetylglucosamine pyrophosphorylases. Gene cloning, protein expression, and catalytic mechanism.](https://pubmed.ncbi.nlm.nih.gov/9603950/): Fungal and human UAP1 proteins have directly measured UDP-GlcNAc pyrophosphorylase activity and complement a yeast UAP1 deficiency.

> All the recombinant ScUap1p, 
> CaUap1p, and HsUap1p possessed UDP-N-acetylglucosamine pyrophosphorylase 
> activities in vitro.


> The yeast Uap1p utilized N-acetylglucosamine-1-phosphate as 
> the substrate

## Exact non-GO claims

The complete emitted record is preserved in [uap1.S-protnlm-source.json](uap1.S-protnlm-source.json). Assessments below address the selected protein product; evidence on longer products is identified explicitly.

### Protein name

> Uncharacterized protein

UNSCORED: the returned “Uncharacterized protein” name has no ProtNLM evidence tag and makes no substrate-specific assertion.

### Function

> UTP--glucose-1-phosphate uridylyltransferase catalyzing the conversion of glucose-1-phosphate into UDP-glucose, a crucial precursor for the production of glycogen

PLI (CS 0; PARALOG_OVERANNOTATION). The paragraph transfers UGP2 glucose-1-phosphate specificity and the resulting glycogen-precursor role to a UAP1-like enzyme. Conserved UAP1 nucleotide-sugar contacts and experimentally characterized ortholog chemistry support GlcNAc-1-phosphate utilization instead. The model’s shared uridylyltransfer chemistry is insufficient to establish the different phosphosugar substrate. [PMID:9603950](https://pubmed.ncbi.nlm.nih.gov/9603950/); [sequence mapping](uap1.S-bioinformatics/RESULTS.md); [donor](uap1.S-ugp-prediction-donor.json).

No GO or EC term was emitted in this record; the name, function and location assessments above constitute its prediction review.

## Family integration

PTHR11952 has the broad official name UDP- GLUCOSE PYROPHOSPHORYLASE, but the selected SF4 is UDP-N-ACETYLHEXOSAMINE PYROPHOSPHORYLASE. Family-level naming does not erase experimentally established UAP/UGP substrate distinctions. No exact GlcNAc-versus-GalNAc efficiency is inferred from the frog homeolog name or the missing human insert.

## Evidence limits

The founding primary study is abstract-only in the cache and directly reports the recombinant human/fungal activity. Human structural contact annotations are explicitly sequence-mapped, not treated as a structure of frog Uap1.S. The genuine Falcon report correctly identifies the UAP/UGP distinction; frog-specific kinetics, compartment and homeolog redundancy remain unmeasured.

Exact sequence mapping: [uap1.S-bioinformatics/RESULTS.md](uap1.S-bioinformatics/RESULTS.md). Global alignments can place nonhomologous alternative tails opposite gaps or distant residues; only conserved segments and explicitly retained feature intervals support functional transfer.

## Additional primary evidence

[PMID:11707391 — Crystal structures of two human pyrophosphorylase isoforms in complexes with UDPGlc(Gal)NAc: role of the alternatively spliced insert in the enzyme oligomeric assembly and active site architecture.](https://pubmed.ncbi.nlm.nih.gov/11707391/): Human UAP1 structures establish nucleotide-sugar contacts and isoform-dependent architecture; conservation is mapped explicitly to frog Uap1.S.

> we
> have solved the crystal structures of AGX1 and AGX2 in complexes with UDPGlcNAc

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

This entry was written during a re-review that deliberately ignored the ProtNLM2 predictions; the earlier sections above, including the ProtNLM2 claim assessments, are retained unchanged.

### 2026-10-20: full re-review

This review was carried out independently of any machine-learning function predictions. The earlier
version of these notes was organised around a prediction assessment; that material has been removed.
The earlier bioinformatics script read its sequence from a prediction-source file, so it was rewritten
to take the sequence from `uap1.S-uniprot.txt`.

#### Identity

- Q6DCZ6 is the Xenbase uap1.S (S-subgenome homeolog) product, 507 aa, from the full-length XGC mRNA
  BC077836. It is not a fragment or a truncated gene model.
- The protein aligns end to end with human UAP1 Q16222 (522 aa, canonical isoform AGX2): 382 identical
  out of 505 aligned pairs. The only gap is human 454-470, which is exactly the AGX2-specific insert
  (UniProt VSP "in isoform AGX1"). The frog product therefore has the shorter AGX1-like architecture
  [file:XENLA/uap1.S/uap1.S-bioinformatics/RESULTS.md "Human positions with no frog counterpart: 454-470."].
  Whether Xenopus also makes an insert-containing splice form is unknown.

#### Phylogenetic placement

- UniProt PANTHER: PTHR11952:SF4, UDP-N-ACETYLHEXOSAMINE PYROPHOSPHORYLASE. Human UAP1 (Q16222) and mouse
  Uap1 (Q91YN5) are in the same subfamily. The paralog UAP1L1 is in SF6, and the yeast QRI1 and S. pombe
  uap1 orthologs are in SF2 (`interpro/panther/PTHR11952/PTHR11952-entries.csv`).
- PAINT (`PTHR11952-paint.tsv`): the eukaryotic node PTN000237224 carries IBD GO:0003977 (seeds include
  Q16222, SGD QRI1, CGD, FB, RGD, AGI), GO:0006048 and GO:0005829 cytosol (seeds AT5G52560, Q16222). The
  frog TreeGrafter rows (PTN008986934) pass on the MF and BP but not cytosol; the cytosol IBD is dated
  2025-12-24, so the TreeGrafter release probably predates it. PAINT did not propagate
  UDP-GalNAc diphosphorylase activity (GO:0052630) or protein serine pyrophosphorylase / IRF3 terms. I
  treat these omissions as deliberate and do not add them.
- Closest experimentally characterised relative: human UAP1 (Q16222), an SF4 ortholog. Repo review:
  `genes/human/UAP1/UAP1-ai-review.yaml`. All annotations there have actions and there are core
  functions, but the header status is still INITIALIZED.

#### Sequence evidence (rewritten analysis)

- All 15 UniProt UDP-GlcNAc/UDP-GalNAc binding residues are conserved.
- The residues named in the human structures [PMID:11707391 "These extensive contacts suggest a specificity
  of the enzyme for acetylated hexosamine"] are conserved: N223, G290, E303, N327, H331, F381, F383, and
  the I-loop residue AGX1-K455 (frog K455).
- The human mutagenesis sites essential for catalysis are conserved: the signature motif 115-122
  (RLGVAYPK in human, RLGVSYPK in frog) and K407.
- Human R453, whose mutation reduces the IRF3 interaction and IRF3 pyrophosphorylation (PMID:36603579
  via UniProt), is L453 in the frog protein. This is a further reason not to transfer the human IRF3 or
  innate-immunity terms.

#### Literature

- No paper on Xenopus uap1 was found; the falcon deep research also found none
  [file:XENLA/uap1.S/uap1.S-deep-research-falcon.md "No retrieved paper mentioned **Q6DCZ6**"].
- Founding enzymology of eukaryotic UAP1 [PMID:9603950 "All the recombinant ScUap1p, CaUap1p, and HsUap1p
  possessed UDP-N-acetylglucosamine pyrophosphorylase activities in vitro."].
- Human isoforms [PMID:11707391 "AGX1 was 2- to 3-fold more active with GalNAc1P as a substrate while AGX2
  was 8-fold more active with GlcNAc1P"]. The insert also changes dimerisation.

#### Decisions

- GO:0003977 (IEA TreeGrafter): ACCEPT; this is the core function.
- GO:0006048 (IEA TreeGrafter): ACCEPT; the enzyme performs the last step of the process.
- GO:0070569 uridylyltransferase (IEA ARBA/InterPro): MODIFY to GO:0003977, because it is too general.
- NEW GO:0005829 cytosol (IBA-style, PAINT PTN000237224 descent): added.
- Not added: GO:0052630 UDP-GalNAc diphosphorylase (PAINT omission; the frog's AGX1-like architecture
  makes it plausible, so it is raised as a question), and IRF3 pyrophosphorylation or antiviral terms
  (mammal-only data, PAINT omission, R453 not conserved).

#### Family review and modules

- `interpro/panther/PTHR11952/PTHR11952-review.yaml` lists Q6DCZ6 as the SF4 representative. It agrees with
  the SF4 placement, and its GO:0003977 scope is UNRESOLVED. No disagreement. It cites this gene's RESULTS.md,
  which has now been regenerated (same alignment and conservation result, with richer labelling).
- Relevant module: `modules/hexosamine_biosynthesis.yaml` (UAP1 step, GlcNAc-1-P + UTP -> UDP-GlcNAc).
  `modules/sialic_acid_metabolism.yaml` uses UDP-GlcNAc downstream.
