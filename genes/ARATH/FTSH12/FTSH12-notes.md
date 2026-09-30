# FTSH12 (A0A1P8ARD2): evidence and exact-input prediction review

The ATPase-domain name and plastid localization are supported. “Probable ATP-dependent zinc metallopeptidase” remains uncertain as an enzymatic-function prediction: a retained catalytic motif is not a measured protease activity, and the decisive experiment shows that the zinc-binding site is dispensable for the essential import role.

## Input identity and functional boundary

The benchmark input A0A1P8ARD2 and reference Q9SAJ3 both map to AT1G79560/FTSH12. Selected residues 1–987 match the reference at 983 positions; the small terminal difference leaves the chloroplast transit peptide, both annotated transmembrane segments, ATP-binding region and zinc-site residues intact. All 49 reference transit-peptide residues are identical. This is FTSH12, not one of the related FtsHi proteins that lack the canonical metalloprotease motif.

## Biological evidence

- [PMID:30309901 — A Ycf2-FtsHi Heteromeric AAA-ATPase Complex Is Required for Chloroplast Protein Import.](https://pubmed.ncbi.nlm.nih.gov/30309901/): Arabidopsis biochemistry identifies the Ycf2-FtsHi motor containing FtsH12 and its association with translocating preproteins.

> a 2-MD heteromeric AAA-ATPase complex associates with the TIC complex and functions as the import motor, directly interacting with various translocating preproteins


> even the FtsH12 zinc binding site is dispensable for its essential function

- [PMID:33216923 — Abundance of metalloprotease FtsH12 modulates chloroplast development in Arabidopsis thaliana.](https://pubmed.ncbi.nlm.nih.gov/33216923/): Fractionation and protease-protection experiments support inner-envelope localization with the ATPase/protease region facing the stroma.

> this unambiguously confirms the localization of FtsH12 in the inner chloroplast envelope


> N-terminome analyses further demonstrated normal proteolytic maturation of
> plastid-imported proteins irrespective of FTSH12 abundance.

## Exact non-GO claims

The complete emitted record is preserved in [FTSH12-protnlm-source.json](FTSH12-protnlm-source.json). Assessments below address the selected protein product; evidence on longer products is identified explicitly.

### Protein name

> AAA+ ATPase domain-containing protein

LSP (CS 2). The AAA+ ATPase domain is intact and supports the name, but the phrase omits the experimentally established FTSH12 identity and chloroplast-import-motor role. A correct ATPase-domain assignment does not imply a demonstrated protease substrate. [PMID:30309901](https://pubmed.ncbi.nlm.nih.gov/30309901/); [sequence mapping](FTSH12-bioinformatics/RESULTS.md).

### Function

> Probable ATP-dependent zinc metallopeptidase

UNC (CS 1). The word “probable” is appropriate to the current protease uncertainty. FTSH12 retains the zinc-binding motif, but H769Y complementation preserves essential function and import, and N-terminomics does not identify an endogenous FTSH12 cleavage substrate. Neither a robust physiological metallopeptidase assignment nor an absolute absence of proteolysis is established. [PMID:30309901](https://pubmed.ncbi.nlm.nih.gov/30309901/); [PMID:33216923](https://pubmed.ncbi.nlm.nih.gov/33216923/).

### Location

> Chloroplast membrane
> Plastid

LSP (CS 2) for “Chloroplast membrane”: fractionation/protease protection supports the more specific inner envelope, with the reference targeting sequence and membrane segments retained in the selected product. LSP (CS 2) for “Plastid”: correct but broader still. These two emitted locations are adjudicated independently; neither establishes thylakoid localization. [PMID:33216923](https://pubmed.ncbi.nlm.nih.gov/33216923/); [sequence mapping](FTSH12-bioinformatics/RESULTS.md).

No GO or EC term was emitted in this record; the name, function and location assessments above constitute its prediction review.

## Family integration

PTHR43655:SF19 is the FTSH12 branch. FtsH protease ancestry supplies a plausible catalytic fold, while the import-motor lineage illustrates functional divergence toward protein translocation. The exact selected sequence retains the zinc-site histidine, so it must not be called motif-deficient like an FtsHi paralog. H769Y is an experimental perturbation of the reference mechanism, not a residue present in the benchmark input.

## Evidence limits

The 2018 and 2021 primary papers have full text. The genuine Falcon report correctly emphasizes import and uncertainty about proteolysis, but it does not include the 2024 structural work. The primary 2024 citation and RCSB deposition are inspected separately; no atomic contact or subunit-specific ATP turnover is inferred from the title of an ATP-bound complex. The exact selected C-terminal variation has not been directly tested.

Exact sequence mapping: [FTSH12-bioinformatics/RESULTS.md](FTSH12-bioinformatics/RESULTS.md). Global alignments can place nonhomologous alternative tails opposite gaps or distant residues; only conserved segments and explicitly retained feature intervals support functional transfer.

## Additional primary evidence

[PMID:39197452 — Structural insights into the chloroplast protein import in land plants.](https://pubmed.ncbi.nlm.nih.gov/39197452/): The 2024 Arabidopsis structural work corroborates the heteromeric ATPase import-motor architecture; it does not establish a physiological FtsH12 protease substrate.

> The Ycf2-FtsHi structure reveals a
> heterohexameric AAA+ ATPase motor module with characteristic features.

The [8XKU deposition](https://www.rcsb.org/structure/8XKU) identifies FTSH12 in the Arabidopsis ATP-bound complex; [entry metadata](FTSH12-8XKU-entry.json) records the primary citation. Its sequence-to-reference comparison retains the ATP-binding and zinc-site regions. The resolved complex supports import architecture, while the independent H769Y complementation experiment defines the protease/function distinction.
