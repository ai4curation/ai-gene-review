# Results: LPA protease-domain sequence compatibility

## Question and scope

This analysis tests whether the human apo(a) reference sequence P08519 retains sequence features associated with a catalytically competent plasmin-like serine protease. It does **not** assay proteolysis. The direct outputs compare P08519 with its close paralog plasminogen P00747, the independently active trypsin-like protease precursor prothrombin P00734, and the protease-like pseudoenzyme control HGF P14210.

## Direct observations

1. UniProt defines one peptidase S1 domain at residues 1820–2038 of P08519. InterPro independently reports the integrated trypsin/peptidase S1 entries IPR001254 and IPR009003. The domain is therefore confidently homologous to trypsin-like serine proteases ([record_summary.tsv](outputs/record_summary.tsv)).
2. The P08519 and P00747 domains are very close paralogs: their pairwise alignment has 194 identical residues among 219 aligned reference-domain residues (88.58%). P00734 and HGF provide more distant positive and negative controls at 37.90% and 40.18% identity, respectively ([pairwise_identity.tsv](outputs/pairwise_identity.tsv)).
3. All three PLG charge-relay residues map without a gap to the same residue type in P08519: PLG H622/D665/S760 correspond to apo(a) H1861/D1904/S1990. UniProt itself annotates all three P08519 positions as charge-relay active sites. The active thrombin control likewise retains H/D/S, whereas the HGF pseudoenzyme control has Q/D/Y and no UniProt charge-relay annotations ([active_site_comparison.tsv](outputs/active_site_comparison.tsv)). Thus, apo(a) has **no catalytic-triad substitution** analogous to the disabling substitutions in the HGF control.
4. A separate, mechanistically critical difference occurs at the zymogen activation junction. UniProt annotates PLG R580|V581 cleavage by PLAU/PLAT and prothrombin R363|I364 cleavage by factor Xa. At the homologous apo(a) protease-domain boundary, the sequence is S1819|I1820 and UniProt provides no cleavage annotation. The P1 basic Arg is therefore replaced by Ser in P08519 ([activation_junction_comparison.tsv](outputs/activation_junction_comparison.tsv)). HGF retains R|V but, as expected for the pseudoenzyme control, lacks an annotated activating cleavage and has catalytic-residue substitutions.
5. The downloaded P08519 reference has 16 integrated InterPro kringle-domain fragments. This is a property of this reference sequence, not a universal LPA allele: apo(a) size varies because the kringle IV type-2 repeat has extensive copy-number polymorphism. The protease-domain comparison is downstream of that repeat array, but whole-protein length and kringle count must remain reference-allele-specific.

## Interpretation

P08519 retains an intact His–Asp–Ser catalytic triad and a highly conserved protease-like domain, so the catalytic center is more sequence-compatible with serine protease chemistry than a classic catalytic-residue-substituted pseudoenzyme such as HGF. However, it lacks the PLG-like basic activation cleavage junction: R|V is replaced by S|I. Canonical trypsin-family zymogen activation depends on proteolytic generation of the mature protease N terminus, so this substitution is strong sequence evidence for an activation-defective, pseudoenzyme-like protease domain despite the intact triad.

This sequence result cannot establish absolute inactivity. It neither reproduces nor refutes the older experimental report associated with UniProt's “serine proteinase activity” statement, and it cannot exclude noncanonical cleavage, context-dependent activity, or activity attributed to another component or contaminant in an Lp(a) preparation. Conversely, the presence of an H/D/S triad alone is not evidence of demonstrated serine endopeptidase activity.

## Annotation implications

- A serine-type endopeptidase activity annotation should not be accepted solely from domain membership, InterPro signatures, or retention of the catalytic triad.
- The S1819 substitution at the homologous PLG activation junction is a concrete reason to treat computationally propagated protease activity as suspect and pseudoenzyme over-annotation as biologically plausible.
- Any experimental activity annotation should be assessed against the primary assay, including substrate cleavage, inhibitors, purification controls, activation state, and exclusion of contaminating proteases. This sequence analysis alone warrants neither confident removal of curator-read experimental evidence nor elevation of protease activity to a core function.
- The most defensible sequence-level wording is: “protease-like domain with an intact catalytic triad but a noncanonical/activation-defective PLG-homologous junction.”

## Reproducibility checklist

- [x] Scripts use command-line parameters for accessions, inputs, outputs, and timeouts; no observed residues or conclusions are hardcoded.
- [x] The same pipeline was tested on three non-LPA inputs: PLG P00747, prothrombin P00734, and HGF P14210.
- [x] An active serine-protease control and a protease-like pseudoenzyme control behaved as expected at the charge-relay residues.
- [x] Official UniProt and InterPro API downloads completed for all four reviewed human proteins.
- [x] Direct source records, URLs, response metadata, byte counts, and SHA-256 checksums are retained under `raw/`.
- [x] Direct alignments and tabular results are retained under `outputs/`.
- [x] `just check` verifies source checksums, accession coverage, and three catalytic-site mappings per target.
- [x] The complete workflow was run twice, with identical tracked output checksums on the second run.
- [x] Conclusions distinguish sequence compatibility from experimental catalytic activity.
- [x] LPA kringle-copy-number polymorphism and reference-allele limitations are explicitly documented.

## Provenance

- UniProt REST API: `https://rest.uniprot.org/uniprotkb/{accession}.json` and `.fasta`, downloaded for P08519, P00747, P00734, and P14210.
- InterPro API: `https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/{accession}/?page_size=200`, downloaded for the same accessions.
- Pairwise alignment: Biopython 1.85 `PairwiseAligner`, global mode, BLOSUM62, gap-open −10.0, gap-extension −0.5.
- Dependency resolution is pinned in `uv.lock`; exact downloaded content is pinned by `raw/manifest.json` checksums.
