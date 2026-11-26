# pam16 manual deep research

`just deep-research-falcon SCHPO pam16 --fallback perplexity-lite` failed because
the Falcon provider was unavailable and the fallback Perplexity provider was also
unavailable. `just mod-description-deep-research SCHPO pam16` skipped because no
MOD description provider is configured for `SCHPO`.

## Summary

S. pombe pam16 (SPBC713.10; UniProt Q9C1W5) encodes the Tim16/Pam16 family
subunit of the presequence translocase-associated motor (PAM). The S. pombe
UniProt record infers from orthology that Pam16 is a peripheral mitochondrial
inner-membrane component of PAM, heterodimerizes with Pam18, and uses a
degenerate J-like region to position or regulate Pam18 rather than to stimulate
Ssc1/mtHsp70 ATPase directly.

The PAINT annotations in PTHR12388 place both `GO:0001405` PAM-complex
membership and `GO:0030150` protein import into the mitochondrial matrix at the
eukaryotic Tim16/Pam16 node PTN000273250, supported by S. cerevisiae PAM16,
human PAM16/MAGMAS, and mouse Pam16 evidence. `just paint-losses SCHPO pam16`
reported no IRD or IKR on the pam16 lineage.

The budding-yeast literature supports the conserved mechanism. Hutu et al.
describe Pam18/Pam16 as the J-complex in the PAM import motor, show that the
Pam18/Pam16 J-complex remains stable while a tim44 mutant strongly impairs
J-complex association with TIM23, and summarize the dual role in which Pam16
promotes Pam18 association with the presequence translocase but reduces
Pam18-stimulated mtHsp70 ATPase activity (PMID:18400944).

Elsner et al. found structural conservation between yeast and human
Tim14/Pam18-Tim16/Pam16 soluble-domain complexes, including heterologous
complexes with yeast counterparts (PMID:19564938). Sinha et al. showed that
human MAGMAS/PAM16 complements budding-yeast pam16 deletion, localizes to
mitochondria, behaves like a peripheral inner-membrane-associated protein, and
forms the Magmas-DNAJC19/Pam18 subcomplex of the human import motor
(PMID:20053669). These human studies strengthen the PTHR12388 eukaryotic
placement but are not needed to overturn the PomBase `GO:0140388` ISO row.

## Annotation consequences

- Accept the two `GO:0001405` PAM-complex rows and the three `GO:0030150`
  matrix-import rows as the core conserved role.
- Accept the root `GO:0005739` mitochondrial rows under the root-organelle
  policy and accept the by-similarity `GO:0005743` mitochondrial inner-membrane
  row.
- Modify the InterPro2GO `GO:0005744` TIM23-complex row to `GO:0001405`
  PAM complex. IPR005341 names Tim16/Pam16, a PAM motor family, not a TIM23
  core translocase subunit family.
- Remove the PomBase `GO:0140388` protein translocation chaperone activity ISO
  row. QuickGO defines that term as ATP-dependent binding/rebinding to the
  emerging unfolded polypeptide to drive vectorial transport. That is the
  activity of the Ssc1/mtHsp70 import motor, whereas Pam16 is the J-like
  Pam18 adaptor/regulator. The same row cites `SGD:S000005758`,
  which the SGD locus API resolves to MGE1/YOR232W; the budding-yeast PAM16
  donor is `SGD:S000003640`.
- Add `GO:0030674` protein-macromolecule adaptor activity as an inferred
  molecular function for the Pam18-binding Pam16 role that positions the
  J-complex at the import motor.
