# MK (At5g27450, P46086) notes

## Identity and nomenclature

- UniProt P46086 (KIME_ARATH) gives no primary gene name; the TAIR cross-reference on the
  record and NCBI Gene 832804 give the standard symbol **MK** ("mevalonate kinase"; alias
  MVK). The papers call it MK (Riou 1994) or MVK (Lluch 2000, Cho 2022). Folder: `genes/ARATH/MK`.
- 378 aa, GHMP kinase family, mevalonate kinase subfamily; PANTHER PTHR43290:SF2; single
  locus [PMID:7958957 "Southern analysis suggests that probably only one locus exists in the A. thaliana genome"].

## Literature search (2026-11-18)

PubMed E-utilities (Europe PMC returned HTTP 503 during this session):

1. `(arabidopsis[tiab] OR thaliana[tiab]) AND ("mevalonate kinase"[tiab] OR "phosphomevalonate kinase"[tiab] OR ... decarboxylase ...)` -> 10 hits. Relevant to MK: PMID:7958957, PMID:10794536, PMID:21655959, PMID:35064110, PMID:42298041 (and its preprint 41502558, not used).
2. `arabidopsis AND (MVK OR AtMVK OR AtMK OR ... At5g27450 ...)` -> 11 hits, same MK set plus PMID:32325804 (MVK gene-family evolution in angiosperms; not used).
3. `(plant OR arabidopsis) AND (mevalonate OR mevalonic) AND peroxisom*` -> 26 hits (localisation context; see the PMK and MVD1 notes).
4. `arabidopsis AND "mevalonate pathway" AND (mutant OR knockout OR lethal ...)` -> 35 hits; the only MK mutant papers are PMID:35064110 and PMID:42298041.

## Activity

- Cloned by complementation of yeast erg12-1 [PMID:7958957 "A 1.64-kb cDNA encoding an Arabidopsis thaliana mevalonate kinase (MK) was cloned by complementation of the erg 12-1 mutation affecting MK in the yeast Saccharomyces cerevisiae"].
- Direct biochemistry on the recombinant protein (Cho et al. 2022) [PMID:35064110 "In order to ascertain whether MVK (At5g27450) has enzymatic activity, we recombinantly expressed and affinity purified wild-type and mutated versions of MVK proteins from E. coli."] and [PMID:35064110 "These results indicate that Arabidopsis MVK has enzymatic activity."]. Catalytic mutants (S149D, D204A) gave very weak MVP production.
- No kinetic constants for the Arabidopsis enzyme in the papers I could read. UniProt's ACTIVITY REGULATION line (inhibition by GPP and FPP at the ATP site) carries no evidence tag and I could not trace it to an Arabidopsis paper; not used.
- No GOA row carries experimental MF evidence (only ISS, IBA, IEA). Cho 2022 is direct (IDA-quality) evidence for GO:0004496, cited on the existing rows rather than added as a NEW row for an already-present term.

## Pathway role (in vivo)

- mvk-1 (splice-site allele from a Ca2+-imaging screen) and CRISPR mvk-2 [PMID:35064110 "As expected, the mvk-1 mutant plants showed a marked reduction in MVP levels (Fig. 3b), while MVA, a precursor compound of MVP, was significantly higher in the mutant (Fig. 3a)."]; IPP also falls [PMID:35064110 "The levels of key downstream metabolites, such as Isopentenyl diphosphate (IPP), were also significantly reduced in the mvk-1 mutant plants (Fig. 3c)."]; growth partly rescued by MVP [PMID:35064110 "The growth of mvk-1 and mvk-2 mutant plants was partially rescued by exogenous application of MVP"].
- This is IMP-quality evidence for GO:0019287 on the gene itself; the term is already present (IBA, IEA).

## Localisation

- Cytosolic YFP in C. roseus cells for both periwinkle and Arabidopsis MVK [PMID:21655959 "while MVK was cytosolic. These compartmentalisation results were confirmed using the Arabidopsis thaliana MVK, PMK and MVD sequences fused to YFP."].
- Cytosolic YFP in Arabidopsis protoplasts [PMID:35064110 "we expressed a YFP fluorophore tagged version of MVK in Arabidopsis protoplasts, MVK was confined to the cytosol (Fig. 5c)."].
- Also in the crude leaf cytosolic fraction of Aryal et al. 2014 (HDA). That fraction also contains catalases, glycolate oxidase and hydroxypyruvate reductase (see `genes/ARATH/MVD1/MVD1-bioinformatics/RESULTS.md`), so by itself the HDA cannot tell cytosol from released peroxisomal matrix; for MK the two YFP studies settle it.
- MK has a PTS2-consensus match (KIILAGEHA, residues 10-18) in the conserved GHMP N-terminal glycine-rich region; human MVK has the equivalent KVILHGEHA (see `genes/ARATH/PMK/PMK-bioinformatics/RESULTS.md`). Human MVK was once proposed to be peroxisomal on this basis but is cytosolic; Arabidopsis MK is cytosolic by YFP. The motif match is not a targeting signal.
- BiFC with P2K1 at the plasma membrane (overexpressed partners) shows where the interaction happens, not a resident membrane pool. No CC term added.

## Regulation and signalling

- Interacts with and is phosphorylated by the eATP receptor P2K1 [PMID:35064110 "MVK interacts directly with the plant extracellular ATP (eATP) receptor P2K1 and is phosphorylated by P2K1 in response to eATP."]; phosphosites S329/T342 modulate activity [PMID:35064110 "Overall, these results suggest that MVK is a direct phosphorylation target of P2K1, and S329 and T342 are the critical MVK residues directly phosphorylated by P2K1 that modulate enzymatic activity."].
- mvk mutants lose the eATP-induced Ca2+ response and are more susceptible to P. syringae; Cho et al. attribute this to downstream MVA metabolites (MVP pre-treatment partly restores the Ca2+ response). MK supplies metabolites; it does not perform a signalling step, so no BP term for purinergic signalling or defence is proposed (participation test).
- Kang et al. 2026: mvk-1 increases sucrose-induced anthocyanin, via SUC1 and GA levels [PMID:42298041 "Loss-of-function mvk-1 mutants show increased anthocyanin levels compared to wild-type (WT) plants under high-sucrose conditions."]. Indirect, pleiotropic; not annotated.

## Expression

- Roots and inflorescences [PMID:10794536 "Northern blot analysis showed that the MVK mRNA accumulates preferentially in roots and influorescences."]; three transcription start sites.

## IBA / PAINT

- PTN000048555 (PTHR43290 root MK node) gives MK activity, GO:0019287 and cytosol (is_active_in). MK is in PTHR43290:SF2 with the human, yeast and archaeal MKs; `just paint-losses ARATH MK` reports no IRD/IKR on its lineage. All three IBAs are sound for this member.
- Family note: PTHR43290 paint.tsv also holds a glucuronokinase node (PTN008680403, seeded by AT3G01640) and an IRD (PTN002214956) of MK activity/GO:0019287, while current UniProt puts AT3G01640 (GLCAK1, Q93ZC9) in PTHR38710. The family is not a single-function family in PAINT's tree, whatever the current subfamily split.
