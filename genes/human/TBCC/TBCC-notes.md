# TBCC (human, Q15814) review notes

**Deep research status:** falcon (Edison) deep research failed with an authentication
error on 2026-10-24, and no other provider key was available. No `-deep-research-*.md`
file exists. The notes below come from manual literature research (cached publications,
PubMed E-utilities searches, WebSearch) and the UniProt record.

## Identity and domains

- Tubulin-specific chaperone C / tubulin folding cofactor C, 346 aa; UniProt Q15814.
- N-terminal spectrin-like three-helix bundle (TBCC_N, PF16752; NMR structure PDB 2L3L)
  and C-terminal C-CAP/cofactor C-like right-handed beta-helix domain (PF07986, PS51329,
  residues 171-323; PDB 2YUH). The C-terminal domain is shared with RP2 and TBCCD1.
- UniProt MUTAGEN: R262A "R->A: Inhibits stimulation of tubulin GTPase" activity
  (ECO:0000269, PMID:11847227).
- No P-loop, G-box or tubulin/FtsZ GTPase domain: TBCC cannot itself be a GTPase.

## Function

- Final step of the post-chaperonin tubulin folding/heterodimer assembly pathway.
  [PMID:8706133 "Cofactor E binds to the cofactor D-beta-tubulin complex; interaction with
  cofactor C then causes the release of beta-tubulin polypeptides that are committed to the
  native state."]
- Cofactors act as GAPs for beta-tubulin: [PMID:10446175 "the cofactors behave as
  GTPase-activating proteins, stimulating the GTP-binding protein beta-tubulin to hydrolyze
  its GTP"]; GTP hydrolysis by beta-tubulin in the supercomplex is the switch that releases
  the native heterodimer [PMID:10446175 "hydrolysis of GTP by beta-tubulin in the
  supercomplex acts as a switch for the release of native tubulin heterodimer"].
- [PMID:10831612 "stimulating it to hydrolyze GTP and thus acting together as a beta-tubulin
  GTPase activating protein (GAP)"]; ARL2 downregulates this GAP activity.
- [PMID:11847227 "Together with cofactors D and E, cofactor C stimulates the GTPase activity
  of native tubulin"]; the conserved arginine (R262 in TBCC) is an arginine finger
  [PMID:11847227 "this residue acts as an \"arginine finger\" to trigger the tubulin GTPase
  activity"]. Human TBCC partially complements yeast cofactor C deletion.
- Alternative/additional GAP target: ARL2. In reconstituted yeast proteins, TBCC binds the
  TBCD-TBCE-ARL2 cage with alpha/beta-tubulin and activates ARL2 GTP hydrolysis
  [PMID:26208336 "forming a ternary complex in which Arl2 GTP hydrolysis is activated to
  alter αβ-tubulin conformation"; "further supporting the idea that TBCC is a true GAP"].
  Fission yeast Tbc1 also acts as an Arl2 GAP [PMID:23576550 "Tbc1 acts as a GAP in
  regulating Alp41/Arl2, a highly conserved small GTPase"]. Either way, the GTP is
  hydrolysed by the GTPase (beta-tubulin or ARL2), and TBCC is the activator.

## Conclusion on GO:0003924 GTPase activity (IDA, PMID:11847227, assigned by UniProt)

Flagged by FRR:0010. The cited paper shows TBCC *stimulates* tubulin GTPase activity; it
does not show that TBCC hydrolyses GTP. GO:0003924 is "Catalysis of the reaction: GTP + H2O
= GDP + H+ + phosphate"; GO:0005096 GTPase activator activity is "Binds to and increases the
activity of a GTPase". MGI already annotates GO:0005096 from the same paper. Action: MODIFY
to GO:0005096, with a WRONG_TERM source_defect against UniProt.

## Localization

- Cytoplasm/cytosol; centrosome in HeLa cells [PMID:22028797 "TBCC is mostly a cytoplasmic
  protein but concentrates at the centrosomes of HeLa cells"]. TBCC depletion causes
  multipolar spindles and mitotic failure [PMID:22028797].
- Retina: [PMID:12417528 "cofactor C and Arl3 localized predominantly to the photoreceptor
  connecting cilium in rod and cone photoreceptors"; "Cofactor C was cytoplasmic in
  distribution"].
- No evidence for TBCC as a microtubule (polymer) component; it acts on soluble tubulin.

## Cellular phenotypes

- TBCC overexpression in breast cancer cells shifts tubulin to nonpolymerizable pools and
  dampens MT dynamics [PMID:20384997]; silencing does the reverse [PMID:21216936 "MC- cells
  displayed decreased content in nonpolymerizable tubulins and increased content of
  polymerizable/microtubule tubulins"].

## Protein-binding rows

PMID:32814053 is a large Y2H neurodegeneration interactome (GSN, FGFR3, CHAT isoform);
uninformative, removed per protein-binding policy.
