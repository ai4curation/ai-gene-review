# gtl-2 (F54D1.5, UniProt Q20766): manual literature review

No deep-research API was available for this review. This file was assembled by hand from the
cached publications (`publications/PMID_*.md`) and PubMed searches ("gtl-2 elegans", 11 hits,
searched 2026-10-28). Quotes are verbatim from the cached text.

## Identity and family

- gtl-2 (gon-2-like 2; ORF F54D1.5; WBGene00001796; GeneID 178036) encodes a 1406-aa protein
  (UniProt Q20766, unreviewed TrEMBL). UniProt/InterPro place it in the TRPM family
  (InterPro IPR050927 TRPM; Pfam PF18139 TRPM SLOG, PF25508 TRPM-like, PF00520 Ion_trans;
  PANTHER PTHR13800:SF1) with seven predicted transmembrane helices (Phobius, residues 780-1179).
- C. elegans has three TRPM paralogs: GON-2, GTL-1 and GTL-2. They are related to human TRPM6/7 but
  lack the C-terminal kinase domain [PMID:26606136 "encode cation channel proteins (GON-2, GTL-1 and GTL-2) that are similar to human TRPM6 and TRPM7, but lack the kinase domain"].
- gtl-1 and gtl-2 lie about 13 kb apart on chromosome IV [PMID:20221407 "the proximity of the gtl-1 and gtl-2 loci (13 kbp)"].

## Expression and localization

- Excretory cell, basal membrane: [PMID:20221407 "The GTL-2::GFP fusion protein is predominantly localized to the outer/basal surface of the excretory cell"].
  The authors note a small apical pool cannot be excluded [PMID:20221407 "we cannot rule out the possibility that a small fraction of GTL-2 is also expressed on the apical surface of the excretory cell"].
- Epidermis (hypodermis) and pharynx: [PMID:21549603 "We observed GTL-2::GFP on the epidermal cell surface (Figure 1D, E), as well as in the excretory cell and pharynx"].
- Not seen in locomotor neurons or muscles [PMID:21549603 "but not in neuronal and muscle cells associated with locomotion"].

## Channel activity (excretory cell electrophysiology)

- Whole-cell recordings of cultured excretory cells show a small outwardly rectifying current that
  depends on GTL-2 [PMID:20221407 "In gtl-2 mutant cells, we found that the outwardly-rectifying current was eliminated"];
  re-expression restores it [PMID:20221407 "When the GTL-2 cDNA was expressed in the excretory cell of the gtl-2 mutants, the outwardly-rectifying current was restored, suggesting that GTL-2 expression is responsible for current generation"].
- The current is blocked by La3+, as for TRPM channels [PMID:20221407 "The current was indeed suppressed nearly completely by 100"].
- Ion selectivity was not measured [PMID:20221407 "we were not able to determine the relative permeability of GTL-2 to different cations"];
  Ca2+/Mg2+ permeability is inferred from GON-2/GTL-1 [PMID:20221407 "it is likely that GTL-2 is also permeable to these cations"].
- No heterologous expression of GTL-2 has been published (none found in the PubMed search).

## Physiology: Mg2+ excretion

- gtl-2 loss causes hypermagnesemia [PMID:20221407 "we found that gtl-2(tm1463) animals contain approximately 1.5 times as much Mg2+ per unit mass as wild type animals"].
- Mg2+-specific hypersensitivity [PMID:20221407 "supplementation with Mg2+, but not other cations (Ca2+, Na+, and K+), greatly enhances the gtl-2 mutant phenotype"].
- Loss of the intestinal uptake channel gtl-1 suppresses gtl-2 [PMID:20221407 "inactivation of gtl-1 suppresses the hypermagnesemic phenotype of gtl-2 mutants"].
- Model [PMID:20221407 "The excretory cell expresses GTL-2 on its basal membrane, and this permits uptake of Mg2+ into the cytoplasm"].
- Independent confirmation of site of action [PMID:24564792 "GTL-2 acts in the excretory canal cell to regulate Mg(2+) homeostasis"] (abstract only).
- An antimorphic gon-2 allele also suppresses gtl-2 Mg2+ sensitivity [PMID:26606136].

## Epidermal Ca2+ signalling after wounding

- [PMID:22100061 "Of 11 TRP channels tested, only GTL-2 was required for normal epidermal Ca2+ responses"];
  cell-autonomous [PMID:22100061 "Epidermal expression of GTL-2 rescued gtl-2 Ca2+ defects"].
  gtl-2 mutants have impaired actin-ring wound closure and reduced post-wound survival; raising
  external Ca2+ restores closure. Gating mechanism unknown [PMID:22100061 "The mechanism of gating of GTL-2 remains an open question."].
  Caveat: gtl-2 gon-2 and gtl-2 gtl-1 doubles restore viability, so systemic ion imbalance may contribute.

## Indirect/organismal phenotypes (not used for GO terms)

- Suppression of acr-2(gf) convulsions; rescued by epidermal or excretory expression; the authors
  attribute it to extracellular ion homeostasis, not Mg2+ per se [PMID:21549603 "Thus, the increased Mg2+ levels in gtl-2(lf) mutants do not account for the effects on the locomotor circuit."].
- Suppression of gon-2(q388) gonadogenesis defect, slow growth, Egl [PMID:20221407].
- Required for learned avoidance of E. faecalis; rescued by excretory-cell expression; mechanism unclear [PMID:34032213 "Thus, it remains unclear how exactly GON-2 and GTL-2 function in pathogen avoidance."].
- Suppression of clozapine-induced larval arrest [PMID:24564792].
- Epidermal autophagy after structural damage (PMID:35311461; only a glossary mention in the abstract, not cached).
