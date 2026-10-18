# Pax6 (mouse, P63015) curation notes

## Provenance / method

- Automated deep research was NOT available for this gene (falcon provider returned HTTP 402, OpenAI 401).
  No `-deep-research-<provider>.md` file was created. These notes were assembled manually from the cached
  publications in `publications/`, the UniProt record (`Pax6-uniprot.txt`) and the completed human
  ortholog review (`genes/human/PAX6/PAX6-ai-review.yaml`).
- Many cited MGI papers are abstract-only in the cache; for those, the "do not overrule curators" rule was
  applied (developmental IMP rows kept as non-core; UNDECIDED where the abstract does not mention Pax6).

## Molecular function

- Paired-box family TF; paired domain sufficient for sequence-specific DNA binding
  [PMID:10197584 "They share a common domain, the paired domain, that is sufficient to mediate sequence-specific DNA binding"].
- Direct target activation: Mitf RPE promoter [PMID:12756174 "both, Pax2 and Pax6 bind to and activate a MITF RPE-promoter element in vitro"];
  alpha-cell genes MafB, cMaf, NeuroD1 [PMID:20592023 "Pax6 directly binds and activates the promoter region of the three genes through specific binding sites"];
  Sox2 [PMID:18287938 "We confirmed that Pax6 could bind to the Sox2 promoter by chromatin immunoprecipitation assay and activate Sox2 expression by a luciferase reporter gene assay"];
  Six6 with Lhx2 [PMID:19146846 "Lhx2 and Pax6 associate with the chromatin at several regions of Six6 in vivo and cooperate for trans-activation of Six6 regulatory elements in vitro"].
- Genome-wide cortical targets [PMID:19521500 "finding that Pax6 positively and directly regulates cohorts of genes that promote neural stem cell self-renewal, basal progenitor cell genesis, and neurogenesis"];
  Pax6-Tbr2-Tbr1 cascade [PMID:30186101 "Pax6, Tbr2, and Tbr1 form a direct feedforward genetic cascade, with direct feedback repression"].
- Repressor activity: [PMID:23622063 "Biochemical assays indicated that Pax6 directly represses Cdk6 expression"];
  Trap/Acp5 in osteoclast lineage [PMID:23990468 "Pax6 binds endogenously to the proximal region of the tartrate acid phosphatase (TRAP) gene promoter and suppresses nuclear factor of activated T cells c1 (NFATc1)-induced TRAP gene expression"]
  with Grg6/Tle6 [PMID:23990468 "the Groucho family member co-repressor Grg6 contributes to Pax6-mediated suppression of the TRAP gene expression induced by NFATc1"].
- Regulation of Pax6 activity: HIPK2/p300 [PMID:16407227 "HIPK2 phosphorylates the activation domain of Pax6, which augments Pax6 transactivation by enhancing its interaction with p300"];
  Smad3 [PMID:17251190 "the MH1 domain of Smad3 was observed binding the RED sub-domain of the Pax6 paired domain"] -- NOTE the same paper
  invalidates Smad4 binding [PMID:17251190 "These data serve to validate the interaction of Smad3, and non-interaction of Smad2 with Pax6, while invalidating the Smad4 interaction that was observed only in vitro"]
  -> co-SMAD binding (GO:0070410) REMOVED (human review had accepted an IEA co-SMAD row; disagreement noted);
  Trim11 degradation [PMID:18628401 "Trim11, a member of the TRIM/RBCC protein family of E3 ubiquitin ligases, interacts with Pax6 and mediates Pax6 degradation via the ubiquitin-proteasome system"];
  SUMOylation of p32 isoform [PMID:21084637 "SUMO1-conjugated p32 Pax-6 exists in both the nucleus and cytoplasm"];
  lncRNA Paupar [PMID:24488179 "in part through physical association with PAX6 protein"].

## Isoforms

- Pax6(5a) vs canonical paired domain [PMID:15548580 "Retrovirally mediated overexpression of Pax6 containing exon 5a inhibited cell proliferation without affecting cell fate"];
  PD essential in brain [PMID:15548580 "the PD is necessary for the regulation of neurogenesis, cell proliferation and patterning effects of Pax6"].
- Paired-less isoform [PMID:16464444 "we identify, for the first time in mammals, an isoform of the Pax6 protein lacking the paired domain"].

## Biological roles (mostly non-core, KEEP_AS_NON_CORE)

- Eye: lens placode [PMID:11069887 "Pax6 activity was found to be essential in the specified ectoderm for lens placode formation"];
  cornea [PMID:16080917 "K12 expression was delayed and down-regulated in the Pax6+/- corneal epithelium, implying that differentiation of the Pax6+/- corneal epithelium was delayed and abnormal"];
  lacrimal gland [PMID:10821755 "the transcription factor Pax6 is required for normal development of the gland and is probably an important competence factor"].
- Telencephalon: [PMID:11050125 "Pax6 has an essential role for the modulation of the dorsoventral patterning of the embryonic telencephalon"];
  [PMID:15878992 "Pax6 delimits the appropriate proliferative zone for GABA INs and regulates their numbers and distributions by repressing the ventral fates of dTel progenitors and progeny"].
- Spinal cord/hindbrain: [PMID:9230312 "Pax6 establishes distinct ventral progenitor cell populations and controls the identity of motor neurons and ventral interneurons"].
- Pancreas: [PMID:20592023 "homozygous mutant mice for Pax6 are characterized by markedly decreased β and δ cells and absent α cells"].

## Problem annotations

- GO:0003682 chromatin binding IDA PMID:23637604: cached full text is a Candida albicans/Dectin-1 paper with no Pax6 mention -> UNDECIDED, reference flagged WRONG_IDENTIFIER.
- GO:0001933 (PMID:16497297, HSP27), GO:0023019 (PMID:18462699, ER71), GO:0007224 (PMID:18590716, FKBP8), GO:0045665 (PMID:16950124),
  GO:0042462 (PMID:12648492): abstracts do not support the specific Pax6 claim -> UNDECIDED.
- GO:0007601 visual perception: Pax6 Sey-Dey eyeless mice used only as blind controls -> over-annotation.
- GO:0030216 keratinocyte differentiation -> MODIFY to GO:0160122 corneal epithelial cell differentiation.
- protein binding rows -> REMOVE, except Tle6/Grg6 row -> MODIFY to GO:0001222 transcription corepressor binding.
