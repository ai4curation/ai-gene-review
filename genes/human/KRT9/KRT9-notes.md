# KRT9 (human, P35527) review notes

Journal of the review session of 2026-11-26. Quotes are verbatim from the cached
`publications/PMID_*.md` files unless marked otherwise.

## Deep research provenance

- `just deep-research-falcon human KRT9 --fallback perplexity-lite` failed: neither
  `falcon` nor `perplexity` is configured in this environment (available providers
  were `asta`, `openscientist`, `claude_code`).
- `KRT9-deep-research-asta.md` was generated (retrieval-only). It returned 20 papers,
  the top hits being off-target proteomics and protocol papers that mention keratin 9
  only as an identified protein. It is preserved verbatim and not used as support.
- `just deep-research-openscientist human KRT9` was launched in the same session.
- Literature search of my own: PubMed queries
  `(KRT9 OR "keratin 9"[Title/Abstract]) AND (palmoplantar OR keratoderma OR knockout OR filament)`
  (134 hits, first 60 screened), `(Krt9 OR "keratin 9") AND (mouse OR mice) AND (knockout OR null OR knock-in OR siRNA)`
  (11 hits, all screened), `keratin 9 manchette perinuclear ring spermatids` (4 hits),
  plus every PubMed id cited by the UniProt record. About 80 papers were cached with
  `just fetch-pmid`; full text was available for a minority (noted below).

## What K9 is

- Type I (acidic) keratin, 623 aa, head 1-152 / rod 153-465 / tail 462-623 in the UniProt
  numbering. Cloned from human foot sole epidermis.
  [PMID:7507869 "Differentiation of human plantar and palmar epidermis is characterized by the
  suprabasal synthesis of a major special intermediate-sized filament (IF) protein, the type I
  (acidic) cytokeratin 9 (CK 9)"]
- Closest paralog is K10. [PMID:7507869 "The protein displayed the highest homology to human CK 10"]
- Expression is restricted to suprabasal keratinocytes of palm and sole.
  [PMID:10201533 "keratin 9 is exclusively expressed in the palmoplantar suprabasal keratinocyte layers"]
  [PMID:19675559 "it is expressed exclusively in suprabasal layers of palmoplantar epidermis and is only
  sparsely detected in acrosyringia"]
- Expression is induced by palmoplantar dermal fibroblasts (site identity is
  mesenchyme-instructed). [PMID:10201533 "Our report indicates extrinsic keratin 9 regulation by
  signals from dermal fibroblasts"] DKK1 from palmoplantar fibroblasts raises keratin 9.
  [PMID:19675559 "Treatment of keratinocytes with DKK1 increased the expression of αKLEIP and keratin 9"]
- In mouse footpad, Krt9 is the most highly expressed gene of differentiating volar
  keratinocytes and depends on K16. [PMID:31220272 "Keratin 9 (Krt9/K9), the most robustly expressed
  gene in differentiating volar keratinocytes, is markedly downregulated in Krt16-null paw skin"]

## Function: structural keratin filament subunit

- Wild-type K9 integrates into the endogenous keratin network; a rod 1A mutant disrupts it.
  [PMID:8647270 "the vector with a G to A point mutated keratin 9 cDNA showed disrupted keratin
  filaments with droplet formation in the cells"]
  [PMID:10218578 "Double staining of K9 and the endogenous keratin revealed the incorporation of de
  novo synthesized K9 into the keratin network"]
- Krt9-null mouse (full text read, PMC3923277): calluses confined to stress-bearing footpads,
  suprabasal cytolysis, fewer keratin filaments, impaired terminal differentiation, K6/K16 induced.
  [PMID:23962810 "ultrastructural analyses of the localized phenotype showed cytolysis-associated
  suprabasal splits with a significant reduction of keratin filaments"]
  [PMID:23962810 "K9 is required for terminal differentiation and maintaining the mechanical
  integrity of palmoplantar epidermis"]
- Heterozygous null mice are normal, so half dosage is tolerated.
  [PMID:23962810 "mice heterozygous for the K9-null allele (Krt9(+/-)) show neither an overt nor
  histological phenotype"]
- Desmosomes look normal in the knockout.
  [PMID:23962810 "no morphological differences were observed between the desmosomes of Krt9+/+ and
  Krt9−/− mice"]

## Open question: the type II partner

The partner is not settled and three candidates are in the literature:

- K1: assumed from co-expression with K1/K10 in footpad
  [PMID:26603179 "the footpads where K1, K9 and K10 predominate"], but the knockout authors saw no
  change in K1. [PMID:23962810 "As no change in the quantity or distribution of K1 was observed in
  Krt9−/− footpads, K9 may not interact with K1 here."]
- K5: [PMID:23962810 "K5 protein levels decreased in Krt9−/− tissues suggesting that K5 may be the
  type II keratin-binding partner of K9 in the palmoplantar/footpad epidermis."] K5 is a basal
  keratin, K9 is suprabasal, so this is inference from co-regulation only.
- K6C: [PMID:37467889 "keratin 6C (KRT6C) is a probable hereterodimer partner for KRT9"] (abstract
  only; in silico model plus proteomics).

An OpenScientist hypothesis job on this question was launched (see `KRT9-hypotheses/`).

## Disease mechanism (EPPK1, MIM 144200; MONDO:0007758)

- Dominant, fully penetrant, almost all variants are missense or small in-frame changes in the rod.
  First reports: [PMID:7512862 "Three KRT9 mutations, N160K, R162Q, and R162W, were identified. All the
  mutations are in the highly conserved coil 1A of the rod domain"].
- **Numbering.** The 1994-2005 papers follow the original cDNA sequence, which is one residue
  shorter upstream of the rod (UniProt sequence conflict at 12-13, canonical SR against a single
  T); their R162 is Arg163 of P35527, N160 is Asn161, M156 is Met157, L159 is Leu160, Q171 is
  Gln172, L457 is Leu458. The later literature uses the UniProt numbering
  [PMID:22262370 "The most common mutation of KRT9, c.C487T (p.R163W)"]. Checked in
  `KRT9-bioinformatics/` (findings N1-N3): all 22 UniProt, 211 ClinVar and 1,496 gnomAD
  protein-level variants match the canonical sequence at their reference residue.
- Dominant-negative, shown three ways:
  1. Mutant K9 collapses the network of cells that also make wild-type keratins.
     [PMID:8647270 "These results indicate that the point mutation seen in our patients had a
     dominant-negative effect on keratin network formation."]
  2. In vivo in mouse skin. [PMID:10218578 "the keratin 9 mutation disrupts the keratin network
     formation in the suprabasal cells in vivo"]
  3. Knock-in mouse of a human indel at the 1A helix initiation motif is affected when
     heterozygous, while the heterozygous null is not (full text read, PMC5014458).
     [PMID:27003758 "The phenotype confirmed that EPPK is a dominant-negative condition, such that
     mice heterozygotic for the K9-mutant allele (Krt9(+/mut)) showed a clear EPPK-like phenotype."]
     [PMID:27003758 "Ultrastructural examination showed cytolysis of keratinocytes and abnormal
     aggregation of tonofilaments in the suprabasal layers of the epidermis"]
- Mutant-allele-specific knockdown rescues the knock-in phenotype
  [PMID:27003758 "shRNA-mediated knockdown of mutant protein resulted in almost normal morphology and
  functions of the skin"], and allele-specific siRNAs exist for the four hotspot alleles
  [PMID:22402445 "generic KRT9 siRNAs and allele-specific siRNAs for four prevalent mutations"].
- Loss of function is also pathogenic, but only when complete: the null mouse is recessive.
  So the human disease is not haploinsufficiency.
- Unusual variant classes worth structural attention:
  - a head-domain "missense" that is really a splice defect
    [PMID:23397986 "the mutation was shown to be pathogenic through activation of a cryptic donor
    splice site, resulting in the deletion of 162 amino acids"];
  - an in-frame 18 bp deletion in linker L1 (PMID:37401035, title only);
  - coil 2B helix termination motif variants (L458F in PMID:16911293, L458P in PMID:21715251
    [PMID:21715251 "a novel c.T1373C (p.L458P) mutation within the sixth exon of KRT9"]).

## New: K9 and YAP1 mechanosignalling (2025-2026)

- [PMID:42918816 "K9 interacts with the YAP1 binding protein 14-3-3σ and sequesters YAP1 in the
  cytoplasm, inhibiting its transcriptional activity; these functions are disrupted by
  KRT9-pEDD-causing variants in K9."] Abstract only; PMC returned no full text for either the
  journal version or the preprint (PMID:41000774) on 2026-11-26, so the assay details
  (which K9 region binds, direct or via the filament) were not read. Treated as a lead:
  recorded in `suggested_questions` and a knowledge gap, not as a NEW annotation.
- [PMID:42918816 "genetic or pharmacological inhibition of YAP1 ameliorates palmoplantar
  keratoderma in Krt9 null mice"].
- A second OpenScientist hypothesis job (head-domain 14-3-3 motif) was launched.

## Rodent testis observations (basis of the spermatogenesis IEA)

- [PMID:11071770 "this protein is a component the perinuclear ring of the manchette of rat
  spermatids"]
- Mouse allele with a neo cassette in intron 6 (makes wild-type plus a truncated K9):
  sperm tail anomalies, but [PMID:16015579 "All mutant mice were fertile."]. The later clean
  null was [PMID:23962810 "born at approximate Mendelian ratios"]; fertility is not discussed there.
- No human testis data found.

## Proteomics (HDA) rows

K9 is a palm/sole keratin and one of the classic handling contaminants of mass spectrometry
(fingertip skin). The HDA rows place it in tears, parotid and prostatic exosomes, NK-cell
membranes and sperm nuclei. None of the cached texts for those papers (three are full text)
names keratin 9 in the body text; identifications will be in supplementary tables.
[PMID:39761842 "identifying keratins using mass spectrometry analysis is challenging due to
potential contamination from skin cells and hair during sample handling"]
A dissenting view exists for CSF/plasma [PMID:26973255 "the possibility of contamination causing
these baselines levels of expression cannot be disregarded"]. Decision: the detections are not
disputed as detections, but they are not evidence of where K9 acts; marked over-annotated,
not removed, because the supplementary data were not read.

## Curation-gap notes (not knowledge gaps)

- No GO-CAM contains KRT9 (`gocams/index.tsv` has no P35527 row on 2026-11-26).
- The UniProt record's two phosphoserines (Ser14, Ser57) are by similarity to K10 only.

## Bioinformatics (KRT9-bioinformatics/RESULTS.md), summary of what it adds

- 28 disease missense variants at 11 positions; 24 in the first 20 residues of coil 1A
  (Fisher odds ratio 433 against gnomAD missense), 3 in the last 20 residues of coil 2, none
  outside the rod coils.
- Fifteen sit at heptad a/d core positions (M157, L160, Y167, V171, Y454, L458), eleven at
  core-flanking e/g positions of the initiation segment (N161, R163, L168); Q172 is a surface b
  position hit only by proline.
- KRT9 is loss-of-function tolerant in gnomAD v4 (pLI 5.5e-8, LOEUF 0.88, 84 high-confidence
  pLoF variants, cumulative allele frequency 2.3e-4). With the normal heterozygous null mouse,
  this argues against haploinsufficiency and for a dominant-negative mechanism.
- p.Cys406Arg (UniProt VAR, EPPK1) has 835 gnomAD alleles and 5 homozygotes, conflicting ClinVar
  classifications, low conservation and an exposed position: not credible as a penetrant
  dominant allele. This is a variant-level disagreement with the UniProt record, noted here; it
  does not touch a GO annotation, so no `source_defects` entry is recorded.
- No experimental K9 structure; no keratin heterodimer structure covers coil 1A, so the
  structural reading of the hotspot rests on lamin A and vimentin homodimers.
- The agent's first `uv add` briefly modified the root `pyproject.toml`/`uv.lock`; both were
  restored and are clean in git. Scripts now carry inline pinned dependencies.

## Not done

- The gene-review checklist (`lcv`) could not be filled: the validator's repository is outside
  this session's GitHub scope and is not on PyPI.
