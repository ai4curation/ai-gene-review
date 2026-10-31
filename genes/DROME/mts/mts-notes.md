# mts (microtubule star, PP2A catalytic subunit, Drosophila melanogaster) curation notes

Accession: P23696 (FBgn0004177).

Deep research: `mts-deep-research-falcon.md` (falcon; completed after a wrapper timeout message). It confirms
Mts as the PP2A catalytic C subunit and adds recent substrate evidence: PP2A-Tws dephosphorylates Map205
pSer283 (immunoprecipitated Tws/Mts on a peptide) to recruit Polo at mitotic exit; Tws-dependent Otefin
Ser50/54 and Ankle2-PP2A-dependent BAF dephosphorylation for nuclear reassembly; Mts counteracts
Aurora-A-dependent Par-6 phosphorylation in neuroblasts; STRIPAK-PP2A restrains Tao-1 phosphorylation;
PP2A-Wrd can stabilize Expanded (context-dependent Hippo direction). None of these change the decisions below.

## Literature journal

- Catalytic activity/mitosis [PMID:9004035 "have reduced levels of PP2A mRNA and reduced PP2A catalytic activity against four different substrates compared to wild type"]
  [PMID:9004035 "exhibiting over-condensed chromatin and a block in mitosis between prophase and the initiation of anaphase"]
  [PMID:17306545 "knockdown of the catalytic or A subunits led to bipolar monoastral spindles"].
- Centrosomes/centrioles [PMID:18798690 "the three remaining proteins in this class encode the catalytic subunit (mts), a regulatory subunit (tws), and a structural subunit (PP2A-29B) of the protein phosphatase PP2A, thus providing compelling evidence that this enzyme is essential for efficient PCM recruitment in flies"]
  [PMID:21987638 "Consistent with a role in centriole duplication, Mts and PP2A-29B localize to mitotic centrioles in S2R+ cells"].
- Integrator/INTAC [PMID:32966759 "We find that Integrator-bound PP2A dephosphorylates the RNA Pol II C-terminal domain and Spt5, preventing the transition to productive elongation"].
- STRIPAK/Hippo [PMID:20797625 "dSTRIPAK depletion leads to increased Hpo activatory phosphorylation and repression of Yki target genes in vivo"].
- Hh: opposite-sign evidence [PMID:21730325 "Reduced PP2A activity by mts or CG17291 RNAi led to the accumulation of Smo"] vs [PMID:18245841 "We show that mts is necessary for full activation of Hh signaling"].

## Decisions

- PMID:34929720 (cited by GOA for cohesion and meiotic spindle NAS rows on mts and Pp2A-29B) resolves to a human NALCN channelosome structure paper: wrong identifier; rows UNDECIDED and reference flagged WRONG_IDENTIFIER.
- Phosphatase regulator activity (IDA, PMID:18256265) on the catalytic subunit modified to protein serine/threonine phosphatase activity; hydrolase activity likewise.
- General mitotic/spindle/segregation terms from S2 RNAi and embryo phenotypes modified to mitotic-specific terms.
- Tap42 protein binding rows removed (no informative term).
