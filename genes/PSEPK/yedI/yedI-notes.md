# yedI (PP_4294, Q88F06): notes

Dashboard protein: [NZ_CP015876.1_1546](https://gene-annotate-dashboard.kbase.us/review/NZ_CP015876.1_1546)
(*P. putida*, tier B, "Prior-annotated"). The exact-match UniProt entries are deleted, so the
review is filed on KT2440 Q88F06. The two are 97.0% identical over 304/304 residues (BERIL run
`20261030T213540Z-yedi-seq-topology`).

## Conclusion

The protein is a YedI/DUF808 (PF05661, PIRSF016660, PTHR30503) integral inner-membrane protein,
and its molecular function is **unknown**.

- **Topology.** DeepTMHMM predicts six TM helices (66-83, 87-107, 147-165, 174-195, 231-251,
  273-293). They form three tight hairpins after a soluble N-terminal region of about 65 residues,
  with N- and C-termini in the cytoplasm. Phobius (UniProt) merges the first hairpin into one long
  71-100 segment. The helices map onto the predicted helices of E. coli YedI (P46125, 65.8% identity
  over 298 aligned residues).
- **Literature.** Nothing is known about the function of any family member. E. coli YedI is
  annotated only as a multi-pass inner-membrane protein; it is among the proteins of the global
  topology study (PMID:15919996), but only the abstract was read.
- **The DNA-repair label.** COG2354's "may be involved in DNA repair" comes from *V. cholerae*
  MutK (Q9ZAK8, a 163-aa DUF808 protein). MutK overexpression reduced mutation frequency in
  *E. coli* repair mutants, while the knockout had no phenotype (PMID:9922251). That is not
  transferable evidence.
- **KT2440 fitness.** The data come from BERDL `kescience.fitnessbrowser` (run
  `20261030T213338Z-yedi-pp4294-fitness`). PP_4294 has no phenotype in 300 experiments: fitness
  ranges from -0.56 to +0.41, and nothing passes |fit| ≥ 1 with |t| ≥ 4. The top cofitness partner
  is PP_2787 at r = 0.31, so the cofitness gives no clue either.
- **Neighbourhood.** PP_4294 (minus strand) is divergent from the TetR-family regulator PP_4295,
  and a TetR/RutR regulator sits next to the orthologue in *P. simiae* and *P. fluorescens*.
  Nearby genes are uacT (PP_4290), several "conserved exported" proteins, and gcl/hyi/glxR
  (PP_4297-PP_4299, glyoxylate/allantoin pathway). None of these genes has fitness or cofitness
  links to PP_4294, and the regulatory pairing is the only conserved feature.

## Dashboard verdict

**Supported.** "YedI-family integral inner membrane protein of unknown molecular function" is
correct and appropriately hedged. The annotator rightly discarded the ABC-transporter, GGDEF and
DNA-repair labels, which came from distant-homolog PaperBLAST text and the COG description.

- GO:0005886 plasma membrane: **CNN**, score 2. It is correct, but GOA already has it as an IEA
  from TreeGrafter.
- Suggested wording: "YedI/DUF808 family integral inner membrane protein (6 TM), molecular
  function unknown".
- The annotator did not see KT2440's own fitness data; the dashboard's fitness block held only
  distant cofitness from Pedobacter and Sphingomonas. Those data would not have changed the call.

## Caveats

- Topology is predicted, not measured, for PP_4294. The YedI-specific result in the Daley et al.
  2005 supplementary data was not checked.
- "No fitness phenotype" refers only to the 300 conditions tested; the gene may matter under
  conditions not tested.

## Tooling

- `just fetch-fitness` failed: there is no local FEBA DB and the Fitness Browser is unreachable
  (403). Fitness was pulled from BERDL with `yedI-bioinformatics/fb_fitness.py`, adapted from
  PP_2389's script (curl User-Agent, limit 1000).
- No PMIDs were found by `fetch-gene-pmids`. PMIDs 15919996, 2527357 and 9922251 were fetched by
  hand.
- The `claude-code` deep-research provider worked.
