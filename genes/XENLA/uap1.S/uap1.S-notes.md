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

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

No ProtNLM files were opened for this re-review (the `*-protnlm-*` files, and the earlier `compare_sequences.py`, which reads its sequence from one of them). I worked from the UniProt flat file, the human UAP1 UniProt JSON, the PANTHER family/PAINT files, the cached publications and the falcon deep research.

### Identity
- Q6DCZ6 is the full-length uap1.S (S-homeolog) product, 507 aa. It is not a fragment or an alternative gene model. It aligns to human UAP1 Q16222 (522 aa, displayed isoform AGX2) over 505 residues with 382 identities (75.6%). The only gap is human 454-470, which is exactly the 17-residue segment missing from human isoform AGX1 (Q16222-2, 505 aa). The frog product therefore has the AGX1-type layout. Frog residues 506-507 are an extra C-terminal dipeptide. [file:XENLA/uap1.S/uap1.S-bioinformatics/RESULTS-rereview.md "| 454-470 | in isoform AGX1 | 0 |"]
- All 15 ligand-labelled human UDP-GlcNAc/UDP-GalNAc contact positions are conserved (human K472 maps to frog K455). [RESULTS-rereview.md "Binding-site positions conserved: 15 of 15."]
- New analysis files: `uap1.S-bioinformatics/compare_sequences_rereview.py` (PEP 723, `uv run --script`), `RESULTS-rereview.md` and `results-rereview.json`. The existing RESULTS.md, results.json, alignment.txt and compare_sequences.py were left untouched.

### Evolutionary grounding
- PANTHER: PTHR11952:SF4 (UDP-N-ACETYLHEXOSAMINE PYROPHOSPHORYLASE), the same subfamily as human UAP1. The family name PTHR11952 ("UDP- GLUCOSE PYROPHOSPHORYLASE") is broad and also covers the UGP branch, so subfamily placement is what decides the sugar substrate.
- PAINT (interpro/panther/PTHR11952/PTHR11952-paint.tsv): node PTN000237224 (taxon Eukaryota) carries IBDs for GO:0003977, GO:0006048 and GO:0005829. They are seeded by human Q16222 plus yeast, Candida, fly, rat and Arabidopsis members. The only recorded loss is an IKR NOT at PTN000237286 (Caenorhabditis). GO:0052630 (UDP-GalNAc diphosphorylase), which human UAP1 has by IDA (PMID:9765219), was **not** propagated. I treat that as a deliberate decision, so GO:0052630 is not proposed and is raised as a suggested question instead.

### Annotation decisions
- GO:0003977 (IEA TreeGrafter): ACCEPT (core).
- GO:0006048 (IEA TreeGrafter): ACCEPT. The enzyme catalyzes the terminal biosynthetic step, so this is participation and not just necessity.
- GO:0070569 uridylyltransferase (IEA ARBA/InterPro): MODIFY to GO:0003977. It is a true parent (OLS ancestors checked) but uninformative, because the IPR002618 signature also matches UGPs.
- NEW GO:0005829 cytosol, proposed on the basis of the PAINT IBD at PTN000237224. The frog product is missing it from its TreeGrafter set.
- No downstream glycosylation or O-GlcNAc processes were added; those consume the product.

### Substrate preference caveat
Human AGX1 (no insert) "was 2-3 times more active with GalNAc-1-P than with GlcNAc-1-P" [PMID:9765219]. Under assay conditions the two human isoforms behave similarly when monomeric [PMID:11707391]. The frog enzyme may therefore also make UDP-GalNAc, but this is not annotated without frog data or a PAINT propagation.

### Relative
Closest characterised relative by phylogeny: human UAP1 (Q16222), the same PANTHER subfamily SF4 and a seed of the PAINT node. The repo review genes/human/UAP1/UAP1-ai-review.yaml has every annotation actioned and has core_functions, and modules/hexosamine_biosynthesis.yaml cites it as the completed review. Its `status` field still reads INITIALIZED.

### Family / module notes
- interpro/panther/PTHR11952/PTHR11952-review.yaml lists Q6DCZ6 under SF4. That placement agrees with this review, so there is no conflict.
- modules/hexosamine_biosynthesis.yaml (uap1_activity) uses the whole family PANTHER:PTHR11952 as the participant. That family includes UDP-glucose pyrophosphorylases, so SF4 would be the more accurate grounding. This is recorded here only; the module was not edited.
