# SnRK2.2 / SRK2D (Arabidopsis thaliana, At3g50500, UniProt Q39192) — review notes

## Provenance of this review
- No deep-research provider was available in this environment, so no
  `-deep-research-<provider>.md` file exists. Research was done from cached
  publications (`publications/PMID_*.md`), PubMed E-utilities searches, and the
  UniProt record. Several key papers are abstract-only in the cache
  (PMID:15292193, PMID:19805022, PMID:19880399, PMID:19420218, PMID:19541597,
  PMID:30962512, PMID:28481327); claims from those are limited to what the
  abstract states.
- Folder/gene_symbol: UniProt primary name is SRK2D; the review uses the
  community name SnRK2.2 (TAIR symbol SNRK2.2), following the OST1/SRK2E precedent.

## Identity and family
- 362 aa Ser/Thr protein kinase, EC 2.7.11.1; kinase domain 23–279, active-site
  Asp-142 (UniProt, PROSITE-ProRule). Subclass III SnRK2 together with
  SnRK2.3/SRK2I and SnRK2.6/OST1/SRK2E [PMID:17307925 "SnRK2.2 and SnRK2.3 are two
  protein kinases most closely related to SnRK2.6"].
- UniProt FUNCTION (ECO:0000269): "Together with SRK2I, key component and activator
  of the abscisic acid (ABA) signaling pathway that regulates numerous ABA
  responses, such as seed germination, Pro accumulation, root growth inhibition,
  dormancy and seedling growth, and, to a lesser extent, stomatal closure".

## Kinase activity / activation
- Activated by hyperosmotic and saline stress (as are 9/10 SnRK2s) and by ABA (one of
  five ABA-activated SnRK2s) [PMID:15292193 "Nine of the 10 SnRK2 were activated by
  hyperosmolarity induced by mannitol, as well as NaCl, indicating an important role
  of the SnRK2 family in osmotic signaling"; "abscisic acid only activated five of
  the nine SnRK2"]. Abstract only — the identity of SnRK2.2 among the five is from
  Fujii 2007 citing Boudsocq 2004 [PMID:17307925 "Of the Arabidopsis SnRK2s, SnRK2.2,
  SnRK2.3, SnRK2.6, SnRK2.7, and SnRK2.8 could be activated by ABA when expressed in
  Arabidopsis protoplasts ( Boudsocq et al., 2004 )"].
- In-gel kinase assays: the 42-kD ABA-induced activity phosphorylating ABF2, ABI5
  and ABF1 fragments is largely SnRK2.2 (+SnRK2.3) [PMID:17307925 "The stronger band
  of kinase activity was at 42 kD, and this activity was reduced in all three of the
  mutants. snrk2.2 had a greater reduction in the 42-kD activity than did snrk2.3"];
  [PMID:17307925 "these data demonstrate that SnRK2.2 and SnRK2.3 have ABA-inducible
  kinase activity and together are likely to play a major role in phosphorylating and
  activating ABF2, ABI5, ABF1, and possibly other ABFs."]
- Triple mutant snrk2.2/2.3/2.6 lacks all ABA-activated kinase activity [PMID:19420218
  "In-gel kinase assays showed that all ABA-activated protein kinase activities are
  eliminated in the triple mutant."].
- Regulation: clade A PP2Cs bind and dephosphorylate the activation loop; PYR/PYL
  receptors release this [PMID:19805022 "Group A PP2Cs interacted physically with
  SnRK2s in various combinations, and efficiently inactivated ABA-activated SnRK2s via
  dephosphorylation of multiple Ser/Thr residues in the activation loop."];
  [PMID:19924127 "the PP2C triple mutant abi1-2hab1-1pp2ca-1 shows a constitutive
  activation of 42 and 45 kD kinases, which correspond to SnRK2.2/2.3 and SnRK2.6,
  respectively"]. TOPP1/AtI-2 (PP1) also bind SnRK2.2 in Y2H [PMID:26943172 "TOPP2
  also interacts with SnRK2.2 and SnRK2.6, out of several SnRK2s tested"].
- Interaction partners (all upstream regulators or downstream substrates; none
  defines a new MF for SnRK2.2): ABI1 in vivo co-IP/affinity purification
  [PMID:19874541 "YFP–ABI1 constitutively interacted with HA–SnRK2.2, HA–SnRK2.3 and
  HA–OST1/SnRK2.6 both in the absence and presence of exogenously applied ABA"];
  PP2CA/AHG3 and AHG1 Y2H [PMID:19407142 "we observe interaction of SnRK2.2 with
  PP2CA/AHG3 and AHG1 using the Y2H assay"]; HAI1 and ABI1 [PMID:19880399]; AKS1
  substrate [PMID:28438792]; MAP4K1 (IP-MS) [PMID:41417897 "MAP4K1 preferentially
  interacts with subclass III SnRK2s (SRK2D/E/I)"]; RaptorB Y2H [PMID:29290610 "We
  found that RaptorB physically interacts with SnRK2.2, SnRK2.3, SnRK2.6, and
  SnRK2.8"]; FREE1 [PMID:30962512].

## Substrates
- ABF/AREB/ABI5 bZIPs (in-gel peptide assays, PMID:17307925; AREB1 in vitro,
  PMID:19880399).
- AKS1 bHLH [PMID:28438792 "Three ABA-responsive SnRK2s (SnRK2.2/SRK2D, SnRK2.3/SRK2I,
  and SnRK2.6/SRK2E/OST1) phosphorylated AKS1 in vitro"].
- FREE1 (ESCRT component), required for its nuclear import [PMID:30962512 "Following
  ABA treatment, SNF1-related protein kinase 2 (SnRK2) kinases phosphorylate FREE1, a
  step requisite for ABA-induced FREE1 nuclear import."].
- RaptorB (TOR complex) — phosphorylation shown for SnRK2.6, SnRK2.2 only Y2H
  [PMID:29290610 "We also found that SnRK2.6, but not a randomly selected protein
  kinase cyclin-dependent protein kinase CDKF, could phosphorylate a recombinant
  fragment of RaptorB"].

## Localisation
- Nucleus and cytoplasm; co-localises and interacts with AREB1 in nuclei
  [PMID:19880399 "SRK2D/E/I and AREB1 co-localize and interact in nuclei in planta"];
  mainly nuclear in seeds [PMID:19541597 "These SnRK2 proteins were mainly expressed in
  the nucleus during seed development and germination."]; ABI1–SnRK2 BiFC in nucleus
  and cytosol [PMID:19924127 "ABI1 interacts with the SnRK2s in the nucleus as well as
  the cytosol"]. Cytosol HDA from leaf fractionation proteomics (PMID:28887381).

## Biological roles
- Seed germination, dormancy, seedling/root growth responses to ABA (redundant with
  SnRK2.3) [PMID:17307925 "snrk2.2 snrk2.3 plants are insensitive to ABA in seed
  germination, indicating that SnRK2.2 and SnRK2.3 are the protein kinases that
  positively regulate ABA signaling in seed germination."].
- ABA-induced gene expression (RD29B, RAB18, NCED3, P5CS1) and proline accumulation
  (PMID:17307925).
- Minor role in stomatal control vs OST1 [PMID:17307925 "SnRK2.2 and SnRK2.3 have
  only minor roles in stomatal control and further distinguished their function from
  that of SnRK2.6."].
- Drought tolerance and water-stress gene expression (triple srk2d/e/i)
  [PMID:19880399 "srk2d srk2e srk2i (srk2d/e/i) triple mutants exhibit greatly reduced
  tolerance to drought stress and highly enhanced insensitivity to ABA"].
- Seed development/dormancy, triple mutant [PMID:19541597].
- Osmotic stress: decuple mutant [PMID:21220313 "SnRK2s are a merging point of
  ABA-dependent and -independent pathways for osmotic stress responses"].
- GA/ABA crosstalk at germination via ABI5 phosphorylation [PMID:18941053 "a recent
  report showed that two SnRK2-type kinases (SnRK2.2 and SnRK2.3) phosphorylate ABI5
  peptides and redundantly mediate ABA-dependent responses during seed germination in
  Arabidopsis"]. Cached text of PMID:18941053 lacks the Results section, so the
  specific IGI experiment behind the GO rows (snrk2.2/2.3 with GA-related treatment)
  could not be read; deferred to the TAIR curator.
- Root hydrotropism: SnRK2.2 acting in elongation-zone cortex [PMID:28481327
  "hydrotropism depends on the ABA signalling kinase SnRK2.2 and the
  hydrotropism-specific MIZ1, both acting specifically in elongation zone cortical
  cells"]. Abstract only; not added as an annotation (recorded as a question).
- Expression: broad, all tissues [PMID:17307925 "RT-PCR analysis showed the
  expression of SnRK2.2 in all tissues examined"].

## Curation decisions (summary)
- Protein binding (GO:0005515) rows: REMOVE per protein-binding policy; partners are
  PP2C regulators (ABI1, ABI2, HAB1, AHG1), substrate AKS1 and MAP4K1.
- kinase activity / protein kinase activity: MODIFY to protein serine/threonine kinase
  activity (GO:0004674), per the CLAUDE.md rule that correct-but-general terms are
  MODIFY. Note: OST1 review used MARK_AS_OVER_ANNOTATED (GO:0016301) and ACCEPT
  (GO:0004672) for the same terms.
- NEW: GO:0009738 abscisic acid-activated signaling pathway. Participation: SnRK2.2 is
  the kinase that performs the signal-transducing phosphorylation step (PP2C-released
  kinase phosphorylating ABFs). Comparator check: paralogs OST1 (Q940H6) and SnRK2.3
  (Q39193) both carry GO:0009738 (TAS) in GOA; SnRK2.2 does not — a gap, not a
  convention. Pathway reconstitution (PMID:19924127) shows the SnRK2s are core
  components.

## 2026-10-20: ported fixes from the parallel review branch

- TOPP1/AtI-2 regulation added to the description and core function 1 [PMID:26943172 "TOPP1 and AtI-2 negatively regulated the SnRK2.2/3/6-mediated activation of the ABA responsive reporter gene RD29B"]; core function 1 now cites the curated UniProt FREE1 statement (ECO:0000269, PMID:30962512).
- The ten GO:0005515 rows with clade A PP2C partners (ABI1, ABI2, HAB1, AHG1) changed from REMOVE to MODIFY to GO:0019903 protein phosphatase binding, matching the OST1 review, which ACCEPTs a curated GO:0019903 IPI row (PMID:19955427) in place of its generic phosphatase-binding rows. The bHLH122 and MAP4K rows stay REMOVE.
- GO:0009737 rows: reason now explains why the term is kept alongside GO:0009738.
- Source defect recorded on the PMID:19407142 IPI row: WITH/FROM is ABI1 (P49597) but the cached main text names only PP2CA/AHG3 (P49598) and AHG1 [PMID:19407142 "we observe interaction of SnRK2.2 with PP2CA/AHG3 and AHG1 using the Y2H assay (SOM Figure 3)"]. Confidence SUSPECTED because the supplementary figure was not checked.


## 2026-10-25 — ABA module member audit

Assessed all 37 existing annotation decisions and the core synthesis. Direct kinase assays, nuclear/cytoplasmic localization, seed-germination effects and redundant ABA/stress function continue to support this module exemplar. No additional GO assertions were introduced. The AKS1-binding row's reason accidentally described a PP2C interaction; corrected it to the kinase-substrate relationship. PP2C-binding refinements now rely on partner-specific function, not the absence of duplicate annotations; obsolete comparisons with older OST1 actions were removed.

PMID:33911084 full Results tests analog-sensitive SnRK2.2 and SnRK2.3 with RAF3/RAF10 rather than relying only on OST1. It states "transphosphorylation by RAFs is required for the reactivation of SnRK2.2/2.3/2.6." Description and core synthesis now distinguish RAF initiation from intermolecular SnRK2 amplification after PP2C inhibition. PMID:31896774 supplies complementary biochemical reconstitution and genetic evidence. Both papers are cached with full text.

Research used existing provider reports/manual notes and cached primary literature. All rows retain explicit decisions; unresolved findings are UNDECIDED rather than inferred from missing text. Record-section backfill and targeted validation were run for this session.
