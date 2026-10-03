# KIF7 — curation notes

## Deep research status

- First run (`--fallback perplexity-lite`) was stopped (falcon default 600 s timeout; perplexity-lite
  unavailable). The 2400 s rerun was killed (exit 137); a second rerun SUCCEEDED
  (KIF7-deep-research-falcon.md). It added Haque et al. 2022 (PMID:35725768) and Yue et al. 2022
  (PMID:34705483), both cached and used below.

## Identity

- UniProt Q2M1P5, kinesin-like protein KIF7; kinesin-4 family; ortholog of Drosophila Costal2 (Cos2).
- Forms homodimers [PMID:24952464 "KIF7-GFP co-immunoprecipitated with KIF7-Flag, and vice versa (Supplementary Fig. 4b), indicating that KIF7 can form a homodimer."].

## Biochemistry: a non-motile, microtubule plus-end-tracking kinesin

- Purified KIF7 binds MTs but does not move:
  [PMID:24952464 "KIF7560-GFP molecules were stationary when bound to microtubules, exhibiting neither unidirectional movement nor significant diffusion along the microtubule lattice"].
- Tracks growing plus ends, slows growth, promotes catastrophe (ATP-hydrolysis dependent):
  [PMID:24952464 "the motor protein tracked the plus-ends of microtubules during the growth phase"];
  [PMID:24952464 "the plus-end-associated KIF7 promotes catastrophe and inhibits microtubule growth in an ATP-hydrolysis dependent manner."].
- Jiang et al. 2019: "The conserved non-motile kinesin Kif7 defines a "cilium-tip compartment" by
  localizing to the distal ends of axonemal microtubules"; prefers GTP-tubulin; ATPase not
  MT-stimulated: [PMID:31031197 "while the ATPase activity of Kif7 is not significantly regulated by microtubules"].
- Conclusion: kinesin-family IBA/IEA "microtubule motor activity", "microtubule-based movement"
  and "cytoskeleton-dependent intracellular transport" do not apply to KIF7 (lineage-specific
  loss of motility; the kinesin fold "has been repurposed" [PMID:31031197]). ATP hydrolysis and
  MT binding are retained.

## Cilium tip organization and length control

- Localizes to cilium tip; limits cilium length:
  [PMID:24952464 "Here we show that Kif7 localizes to the cilium tip, the site of microtubule plus ends, where it limits cilium length and controls cilium structure."].
- Mouse mutant cilia ~30% longer, unstable; human patient fibroblasts have longer cilia
  [PMID:21552264 "These findings suggest that, whereas KIF7 is not necessary for cilia formation, it might be involved in regulating cilia length."].
- Not required for IFT or Smo entry
  [PMID:24952464 "Kif7 is not required for normal intraflagellar transport or for trafficking of Hh pathway proteins into cilia."].

## GLI binding and ciliary delivery (from deep research, verified in cache)

- Direct binding by DNA mimicry: [PMID:35725768 "the coiled-coil dimerization domain of KIF7, characterized by its striking shape, size and charge similarity to DNA, forms a complex with the DNA-binding zinc fingers in GLI, thus revealing a mode of tethering a DNA-binding protein to the cytoskeleton"];
  [PMID:35725768 "showed that the Kif7-CC:Gli2-ZF complex has a Kd of 48 ± 5 nM"].
- KIF7 is carried by IFT kinesin-2; MT binding not required for induced GLI tip accumulation:
  [PMID:34705483 "we demonstrate that kinesin-2 KIF3A/KIF3B/KAP mediates the translocation of KIF7 to the cilium tip in response to Hedgehog pathway activation"];
  [PMID:34705483 "we show that the immotile behavior of KIF7 is required to prevent ciliary localization of Gli transcription factors in the absence of Hedgehog signaling"].
  This qualifies the He 2014 model: the length-control output plausibly needs plus-end binding,
  while GLI tip accumulation can occur without it.

## Hedgehog signaling

- Mouse Kif7 acts downstream of Smo, upstream of Gli2, both negative and positive roles
  [PMID:19666503 "mouse Kif7 acts downstream of Smo and upstream of Gli2 and has both negative and positive roles in Shh signal transduction."].
- Required for Gli3 ciliary localization and prevents Gli3 repressor processing with Hh
  [PMID:19592253 "We also demonstrate a requirement for Kif7 in the efficient localization of Gli3 to cilia in response to Hh and for the processing of Gli3 to its repressor form."].
- Interacts with Gli transcription factors and controls their stability
  [PMID:19549984 "Kif7 physically interacted with Gli transcription factors and controlled their proteolysis and stability, and acted both positively and negatively in Hh signaling."].
- Moves from base to tip on pathway activation
  [PMID:19666503 "Activation of the Shh pathway promotes trafficking of Kif7-eGFP from the base to the tip of the cilium"].
- Human disease: hydrolethalus, acrocallosal, Joubert (JBTS12) syndromes, with impaired GLI3
  processing [PMID:21552264 "we show deregulation of most GLI transcription factor targets and impaired GLI3 processing in tissues from individuals with KIF7 mutations."].
  Dafinger et al. (abstract only cached): KIF7 co-precipitates NPHP1; knockdown affects cilia,
  centrosomes, Golgi [PMID:21633164 "We found that KIF7 co-precipitated with nephrocystin-1."].

## Curation decisions summary

- MODIFY microtubule motor activity (IBA/IEA/IDA) -> microtubule plus-end binding (GO:0051010).
  Single-molecule TIRF data show KIF7 is stationary on MTs, and Jiang 2019 calls it non-motile.
- REMOVE microtubule-based movement and cytoskeleton-dependent intracellular transport (IBA/IEA):
  target-specific loss of motility; KIF7 is not required for IFT.
- ACCEPT MT binding, ATP hydrolysis activity, ATP binding, kinesin complex (homodimer), cilium,
  ciliary tip, basal body, and positive/negative regulation of smoothened signaling.
- NEW GO:0031115 negative regulation of microtubule polymerization (IDA, PMID:24952464). Purified
  KIF7 itself slows plus-end growth and raises catastrophe frequency, so KIF7 does the work.
- GLI co-IP rows (GLI3, mouse Gli1) MODIFIED to GO:0140297 DNA-binding transcription factor binding
  (direct binding shown by Haque 2022). Other protein binding rows removed (SMO, SUFU, NPHP1, P4HA2).

## HPA cilium atlas vs module role

- HPA v25 (member_evidence.md): Primary cilium (Supported); Primary cilium tip (Supported); main
  locations Primary cilium; Primary cilium tip. GOA has matching HPA rows (GO_REF:0000052) for
  cilium and ciliary tip. Only metadata for the HPA atlas paper (PMID:41005307) is cached.
- Module role (stage 6, length control: "ciliary tip length regulator") agrees with the HPA call
  and with the biochemistry (plus-end tracking, growth inhibition at axoneme tips). core_functions
  places the length-control function first, with the Hedgehog regulatory role (Gli/Sufu tip
  compartment) as a second core function. Length control and Hh regulation are mechanistically
  linked: the tip compartment KIF7 builds is where Gli-Sufu is regulated. KIF7 belongs in both the
  cilium life-cycle and Hedgehog modules. It is not a general ciliogenesis factor: cilia form
  without KIF7.
