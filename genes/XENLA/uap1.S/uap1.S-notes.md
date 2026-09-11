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
