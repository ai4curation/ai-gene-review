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

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

No ProtNLM2 file or prediction-evidence folder was opened in this pass, and none was used as evidence.

### Identity of the benchmark accession

- A0A1P8ARD2 (unreviewed, 991 aa) is an **alternative Araport11 gene model of AT1G79560/FTSH12**. It is not the canonical product. The canonical product is Swiss-Prot **Q9SAJ3** (FTSHC_ARATH, 1008 aa). UniProt lists a third model, A0A1P8ARE4 (963 aa).
- The independent re-analysis ([RESULTS-rereview.md](FTSH12-bioinformatics/RESULTS-rereview.md), from `compare_gene_models_rereview.py`, which fetches both sequences from UniProt REST) shows residues **1-983 identical**. Only the C-terminal tail differs: A0A1P8ARD2 984-991 `VVYILSSC` against Q9SAJ3 984-1008 `EELLPHKDRVSYQPVDLRAAPLHRS`.
- All functional regions lie in the shared prefix: transit peptide 1-49, TM 154-174 and 427-447, Walker A `GPPGTGKT` at 533, Walker B `FVFVDE` at 587, HEXXH `HEAGH` at 769-773, and the third zinc ligand Asp849. No domain or catalytic residue is missing. The divergent tail lies beyond the M41 domain and has not been tested experimentally.
- The experimental GO annotations (TAIR IDA/IMP/IPI from PMID:30309901 and others) sit on Q9SAJ3. This accession carries only IEA rows.

### Evidence re-checked (quotes grep-verified against cached full text)

- PMID:30309901 (Kikuchi 2018): FTSH12 is one of the six subunits of the 2-MD Ycf2/FtsHi import motor, and the only one that keeps the FtsH zinc site. Two points bear on the protease question and were missing from the earlier pass: [PMID:30309901 "Hydrophobic residues at the pore loop ... were well conserved in FtsHi1, FtsHi2, FtsHi3, FtsHi4, and FtsHi5, but not in FtsH12"] and [PMID:30309901 "We also detected trace amounts of FtsH12 in the pull-down fraction"]. The authors also write [PMID:30309901 "The role of FtsH12 in the complex remains unclear, but its zinc binding motif is not crucial for its essential function"].
- PMID:33216923 (Mielke 2021): inner-envelope localization with the AAA+ and catalytic domains facing the stroma, and normal N-terminal maturation of imported proteins whatever the FTSH12 level.
- PMID:39197452 (Liang 2024, Cell; abstract only): heterohexameric AAA+ motor structure.

### Evolutionary grounding

- PANTHER PTHR43655:SF19 ("ATP-DEPENDENT ZINC METALLOPROTEASE FTSH 12, CHLOROPLASTIC") is the FTSH12 subfamily. Kikuchi et al.'s own phylogeny places land-plant FtsH12 in the clade with the FtsHi proteins and Ycf2, derived from cyanobacterial FtsH.
- PAINT (interpro/panther/PTHR43655/PTHR43655-paint.tsv) has three IBD rows: PTN008683692 GO:0004222, and PTN000554085 GO:0005745 m-AAA complex and GO:0034982 mitochondrial protein processing. The seeds are all mitochondrial m-AAA proteases (human AFG3L2/SPG7, mouse, fly, yeast, worm). These propagate to canonical Q9SAJ3 as IBA. The two mitochondrial terms (m-AAA complex, mitochondrial protein processing) do not fit a chloroplast inner-envelope import-motor subunit. They should be challenged when Q9SAJ3 is reviewed (node placement or a missing NOT on the plastid branch). The metalloendopeptidase IBA is an ancestral-state claim that the H769Y result does not refute but does not support either.
- The family review interpro/panther/PTHR43655/PTHR43655-review.yaml lists A0A1P8ARD2 as the SF19 representative member and leaves GO:0004222 and GO:0045037 UNRESOLVED. I found no disagreement about subfamily placement. It would be better for the family review to name the canonical Q9SAJ3 as the representative.

### Decisions (changes from the earlier pass)

- The three protease rows (GO:0004176, GO:0004222, GO:0006508) stay MARK_AS_OVER_ANNOTATED. The reasons now add the missing pore-loop residues and the PAINT/TAIR-ISS context on the canonical entry.
- ATP binding and ATP hydrolysis activity: ACCEPT, re-grounded on the independently checked Walker A and Walker B motifs.
- cytoplasm: MODIFY to chloroplast inner membrane (GO:0009706).
- NEW part_of GO:0062091 Ycf2/FtsHi complex and NEW involved_in GO:0045037 protein import into chloroplast stroma (complex-subunit participation). Both are experimental on the same gene product (Q9SAJ3), and the sequence is identical over all functional regions.
- Core function rewritten: contributes_to GO:0016464 chloroplast protein-transporting ATPase activity, in complex GO:0062091. This is a complex-level activity, so it uses contributes_to, not enables. A second core function records ATP hydrolysis by the AAA+ module.
- The old RESULTS.md is kept but no longer cited as support, because its stated inputs include the frozen prediction-source JSON. RESULTS-rereview.md replaces it as the cited source.

### Relative to review next

The benchmark accession is an alternative gene model, and the canonical product Q9SAJ3 has no review in the repo. The next target is therefore **Q9SAJ3** (same_gene_canonical), in folder `genes/ARATH/FTSH12__Q9SAJ3`. That review should handle the TAIR IDA/IMP/IPI/HDA rows, the mitochondrial HDA (PMID:28887381), the plasma membrane ISM, the thylakoid SubCell row from PMID:14630971 (which conflicts with the inner-envelope data), and the m-AAA IBA rows.

### Modules

No module in modules/ covers chloroplast protein import or the Ycf2-FtsHi/TIC machinery (grep for FTSH12, Ycf2, FtsHi and chloroplast protein import found no relevant module).

## 2026-10-21 — NEW rows withdrawn: already annotated on another product of the same gene

The re-review proposed NEW rows (GO:0062091 Ycf2/FtsHi complex, GO:0045037 protein import into chloroplast
stroma) on this accession. GOA already carries both terms on the canonical FTSH12 product, reviewed in
`genes/ARATH/FTSH12__Q9SAJ3/`. GOA propagates gene-level annotations to one representative product per gene,
so adding them to a second product fills a convention, not a curation gap. The rows were withdrawn under the
rule applied across the ProtNLM2 re-review cohorts, first raised in the PR #5303 review. The gene-level
function is unchanged.
