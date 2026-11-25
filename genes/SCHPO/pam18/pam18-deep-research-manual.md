# pam18 manual deep research

`just deep-research-falcon SCHPO pam18 --fallback perplexity-lite` failed
because the Falcon and Perplexity providers were unavailable in this runtime.
`just mod-description-deep-research SCHPO pam18` skipped because no MOD
description provider is configured for `SCHPO`. `just paint-losses SCHPO pam18`
could not complete because the PANTHER tree API did not return `PTHR12763`
during the helper's retry loop; the local `PTHR12763-paint.tsv` extract has
only three positive IBD rows and no IRD or IKR loss rows.

## Summary

S. pombe pam18 (SPAC824.06; UniProt Q9UT37) encodes the fission-yeast
Tim14/Pam18 protein, the matrix-facing J-domain subunit of the
presequence translocase-associated motor. UniProt infers that S. pombe Pam18 is
a single-pass mitochondrial inner-membrane protein that heterodimerizes with
Pam16 in the PAM complex and stimulates Ssc1/mtHsp70 activity during
ATP-dependent import of transit-peptide-containing proteins from the inner
membrane into the mitochondrial matrix.

The PTHR12763 family extract places S. pombe pam18 and budding-yeast PAM18 in
the same Tim14/Pam18 subfamily, `PTHR12763:SF28`. Its PAINT extract places
`GO:0001405` PAM-complex membership, `GO:0001671` ATPase activator activity,
and `GO:0030150` matrix import at node `PTN000298641`, supported by
SGD:S000003998 and SGD:S000005272. The local PAINT extract has no loss rows for
this family.

The budding-yeast PAM18/TIM14 literature supports the transfer. D'Silva et al.
showed that Pam18 is an inner-membrane J-domain protein whose depletion
disrupts mitochondrial matrix import and whose purified protein stimulates the
Ssc1 ATPase (PMID:14605210). Truscott et al. independently identified
Pam18/Tim14 as an essential PAM subunit associated with TIM23, showed that its
J domain is matrix exposed, that pam18 mutants selectively impair
matrix-directed preprotein import, and that the purified J domain plus Mge1
stimulates mtHsp70 ATPase (PMID:14638855).

Pam18 acts in the import motor as a Pam18/Pam16 heterodimer rather than an
isolated J protein. Frazier et al. found that Pam16 interacts with Pam18 and is
needed to recruit Pam18 to the presequence translocase (PMID:14981507).
D'Silva et al. showed that stable Pam18-Pam16 heterodimerization through their
J/J-like domains is critical for matrix import (PMID:16105940), and later work
found that Pam18 association with the translocon is stabilized by the direct
Pam18-Pam16 J-domain interaction, Pam18's intermembrane-space contact with
Tim17, and the N-terminal Pam16 contact with the matrix side of the translocon
(PMID:18003975). Hutu et al. also showed that the Pam18/Pam16 J-complex is
recruited to the TIM23 presequence translocase in a Tim44-dependent way
(PMID:18400944).

Priesnitz et al. reported that disrupted Pam16-Pam18 coupling redistributes
budding-yeast Pam18 to respiratory-chain supercomplexes and stimulates
mtHsp70-dependent respiratory-chain-complex assembly (PMID:35385740). That is a
useful lead for Pam18 biology, but the current S. pombe record has no
respiratory-chain annotation to review and the matrix-import role remains the
only conserved core function to assert here.

## Annotation consequences

- Accept the `GO:0001405` PAM complex rows, the `GO:0001671` ATPase activator
  rows, and all `GO:0030150` matrix-import rows. These three assertions sit on
  the same PTHR12763 PAINT node and are supported by the conserved
  budding-yeast Pam18 mechanism.
- Accept the direct `GO:0005739` mitochondrion row from the Matsuyama et al.
  YFP screen under the root-organelle policy.
- Accept the UniProt SubCell `GO:0005743` mitochondrial inner-membrane row.
  The S. pombe protein is predicted to be a single-pass membrane protein with a
  matrix-exposed J domain, matching the topology of the active Tim14/Pam18
  subunit in the PAM import motor.

## GO-CAM 69729a3800007453 consistency

The model represents pam18 as enabling `GO:0001671` ATPase activator activity in
the mitochondrial matrix as part of `GO:0030150` protein import into the
mitochondrial matrix. The gene review agrees with that activity: the protein is
anchored in the mitochondrial inner membrane, but its J-domain ATPase activator
activity is matrix-facing and directed toward Ssc1/mtHsp70 in the PAM import
motor.
