# mitfa notes (Danio rerio, UniProt Q9PWC2, ZFIN:ZDB-GENE-990910-11; nacre)

## 2026-09-27 — review for DANRE_DUPLICATION (pair mitfa/mitfb)

Deep research: `just deep-research-falcon DANRE mitfa` (run by the coordinator) completed
during the review (`mitfa-deep-research-falcon.md`). It agrees with the cached-literature
picture: nuclear localization is family-level inference, mitfa;tfec double mutants lack
xanthophores, and mitfa/mitfb single and double mutants have a normal RPE. Its quotes are
used for the nucleus IBA and the NEW xanthophore term.

### Key findings with provenance

- nacre is mitfa: [PMID:10433906 "Homozygous nacre (nac(w2)) mutants lack melanophores
  throughout development but have increased numbers of iridophores."];
  [PMID:10433906 "The non-crest-derived retinal pigment epithelium is normal"];
  cell-autonomous, rescue and ectopic melanization: [PMID:10433906 "misexpression of nacre
  induced the formation of ectopic melanized cells"].
- Multiple stages of melanocyte differentiation (temperature-sensitive allele):
  [PMID:21146516 "mitfa is required at several stages of melanocyte differentiation"].
- Expression partition with mitfb: [PMID:11543618 "mitfb is coexpressed with mitfa in the RPE
  at an appropriate time to compensate for loss of mitfa function in the nacre mutant but is
  not expressed in neural crest melanoblasts"].
- RPE: mitfa and mitfb single and double mutants have a normal RPE
  [PMID:23139843 "the loss of Mitf activity in mitfa, mitfb, or double mitf mutant zebrafish
  had no effect on RPE pigmentation or development"]; mitfa is sufficient to induce retinal
  pigmentation when misexpressed [PMID:23139843 "the ability of mitfa to induce pigmentation in
  the zebrafish retina when misexpressed"]. tfec is the likely redundant factor
  [PMID:42663426 abstract, triple mutant].
- Tfec interplay: [PMID:33439865 "We show that Mitfa represses tfec expression"];
  choroid fissure: [PMID:32541011 "mitfa;tfec mutants possess severe colobomas"].
- Xanthophores: dominant-negative DNA-binding-domain allele [PMID:40123122 "Here we identify a
  new allele of the zebrafish Mitf gene, mitfa, that results in a complete absence of not only
  melanophores but also yellow-orange xanthophores."]; mitfa;mitfb double nulls show reduced
  xanthophores (PMID:37823232, PMID:40123122).
- Parallel regulators: TFAP2 (PMID:20862309, PMID:28249010), kit (PMID:15300437), ErbB/kitlga
  (PMID:23364329) — mitfa perturbations used as tools; melanocyte differentiation annotations
  are all consistent with the known requirement.

### Curation decisions (summary)

- Core: GO:0000981 (IBA, IDA), GO:0000978 (IBA), nucleus; melanocyte differentiation
  (all IMP/IGI/IBA ACCEPT).
- MODIFY GO:0006351 DNA-templated transcription (IDA) -> GO:0006357.
- REMOVE GO:0071228 cellular response to tumor cell (PMID:35929478; full text read): mitfa
  acts inside the melanoma cells as the conditional oncogenic driver, it is not a response of
  a cell to a stimulus from a tumor cell, which is what the term defines.
- UNDECIDED GO:0007623 circadian rhythm (PMID:26278158, abstract only; abstract never
  mentions mitfa).
- NEW GO:0050936 xanthophore differentiation (mirrored on mitfb).
