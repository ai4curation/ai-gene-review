# ey (eyeless) — curation notes

UniProt O18381 (PAX6_DROME), FlyBase FBgn0005558, Drosophila melanogaster.

## Provenance note

Automated deep research could not be run for this gene in this environment
(Falcon provider returned HTTP 402; OpenAI key rejected with HTTP 401). No
`ey-deep-research-*.md` file exists. The notes below were assembled manually from
the cached publications in `publications/`, the UniProt record, and PubMed
searches (E-utilities) used to locate and cache the classic papers on ey
(PMID:7914031, 7892602, 9584118, 10207149, 10198632, 16533912).

## Identity and domains

- Paired-box (Pax6 class) transcription factor with an N-terminal paired domain
  (PAI + RED subdomains, aa 56-182) and a paired-type homeodomain (aa 430-489);
  C-terminal P/S/T-rich transactivation region (UniProt O18381 features).
- Three isoforms (C/larval, A/embryonic, B lacking the N-terminal paired region).
- Cloned as the fly homolog of mouse Small eye / human Aniridia (PAX6)
  [PMID:7914031 "Two spontaneous mutations, ey2 and eyR, contain transposable
  element insertions into the cloned gene and affect gene expression, particularly
  in the eye primordia."]

## Eye specification (core)

- Ectopic expression is sufficient to induce eyes on wings, legs and antennae
  [PMID:7892602 "By targeted expression of the ey complementary DNA in various
  imaginal disc primordia of Drosophila, ectopic eye structures were induced on the
  wings, the legs, and on the antennae."] [PMID:7892602 "These results support the
  proposition that ey is the master control gene for eye morphogenesis."]
- Upstream regulator: toy (second fly Pax6) directly activates the eye enhancer of
  ey [PMID:10198632 "Toy functions upstream of ey by directly regulating the
  eye-specific enhancer of ey"].
- Downstream targets: so and eya [PMID:9584118 "During normal eye development,
  eyeless is expressed earlier than and is required for the expression of sine
  oculis and eyes absent, but not vice versa."]; direct binding to so intronic eye
  enhancer [PMID:10207149 "the EY protein activates transcription of sine oculis by
  direct interaction with an eye-specific enhancer in the long intron of the so
  gene"]; genome-wide direct targets incl. eya, shifted, Optix [PMID:16533912
  "Initial analysis reveals three genes, eyes absent, shifted, and Optix, as novel
  direct targets of Ey."]; dachshund regulation [PMID:16780828].
- Direct regulation of the proneural gene atonal via an eye-specific enhancer, with
  Sine oculis [PMID:17108002 "the RD factors Eyeless and Sine oculis function as
  direct regulators"] and in synergy with Daughterless homodimer [PMID:24886829
  "Experiments using antibodies against Ey and Da demonstrate the presence of Ey in
  the gel shift complex"].
- Ey is a transcriptional activator, unlike Eyg [PMID:15973436 "Most
  interestingly, Eyg acts exclusively as a repressor, whereas Ey is an
  activator."]; C-terminal activation domain stronger than Toy's [PMID:19406113 "We
  show that the transcriptional activation domains, located within the C-termini
  are of significantly different strengths with Ey acting as a more potent
  transcriptional activator than Toy."]
- Paired domain drives eye induction; homeodomain promotes growth and antagonizes
  PD function [PMID:25234589 "We showed that Ey can promote cell growth, which
  requires the HD but not the PD."]
- Intact protein (PD, HD and C-terminus) required for rescue [PMID:19666017 "Rescue
  of the eye and brain phenotypes was only observed when full-length Eyeless was
  expressed, while all deletion constructs failed to rescue."]

## Brain / neuroendocrine roles (non-core)

- Mushroom body: expressed in MB progenitors and neurons; hypomorph ey(R) loses
  medial lobe [PMID:10903173 "In the larval brains of the hypomorphic ey(R) strain,
  we find that beside an overall reduction of MB neurons, one MB pathway, the medial
  lobe, is malformed or missing."]
- Adult brain structure and locomotion [PMID:11153010 "Consistent with the
  morphological lesions, we observe defective walking behavior for these eyeless
  mutants."]; central complex [PMID:19666017].
- Insulin-producing cells: Ey directly activates dilp5 [PMID:18852455 "Eyeless
  controls IPC function by the direct transcriptional control of one of the major
  Dilps, dilp5"]; loss reduces body size and raises hemolymph sugar.
- Hyperglycaemia screen hit [PMID:25994086].
- Glial migration timing in eye disc [PMID:11804568].
- Physical interaction with Antp homeodomain, inhibitory to Ey [PMID:18755899].

## Curation thoughts

- Core: DNA-binding TF activity RNAPII-specific (GO:0000981) acting at
  cis-regulatory regions (GO:0000978) of so/eya/ato/dilp5; positive regulation of
  RNAPII transcription; compound eye development/morphogenesis; nucleus.
- GO:0010092 "specification of animal organ identity" would arguably describe the
  ectopic-eye selector function; not added as NEW (raised as a question).
- PMID:15790965 (DC5 enhancer) abstract says DC5 is regulated by D-Pax2, not Pax6 in
  vivo; the IDA rows to ey presumably come from full-text in-vitro assays. Deferred
  to curator.
- PMID:19901536 is a toy paper; MB/brain annotations to ey are biologically
  consistent, so kept as non-core rather than removed.
