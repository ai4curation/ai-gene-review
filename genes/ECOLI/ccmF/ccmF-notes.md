# ccmF (P33927, b2196) notes

## Deep research status

2026-10-23: `just deep-research-falcon ECOLI ccmF` was attempted and failed with
`Exception: Failed to authenticate`; no other provider credentials were available.
This review is therefore based on the cached publications and the UniProt record.

## Biology

- CcmF forms a heme-lyase complex with CcmH and binds holo-CcmE [PMID:11744735 "We propose that CcmFH forms a bacterial heme lyase complex for the transfer of heme from CcmE to apocytochrome c."].
- CcmF is a cytochrome b with a stoichiometric b-heme, not derived from holo-CcmE [PMID:19629033 "Rather, the b -haem is a stable component of the CcmF protein in a 1:1 (molar) stoichiometry."]; His261 is an axial ligand, and His491 also contributes [PMID:22066495 "mutation of either of two conserved transmembrane histidines (His261 or His491) impairs stoichiometric b-heme binding in CcmF"].
- The b-heme is reduced by quinols in vitro [PMID:19629033 "The CcmF cytochrome b is reduced by ubiquinol 1"], but the proposed NPF quinone site is dispensable in vivo [PMID:24044352 "suggesting that interaction with quinols/quinones at this site is not essential for the function of CcmF"].
- CcmFH plus CcmG make holocytochrome c without CcmABCDE [PMID:24397552 "Our findings establish that CcmFH is the system I holocytochrome c synthetase."].
- ccmF deletion abolishes holocytochrome c but not apocytochrome [PMID:9237661 "The ccm mutants produce cytochrome c-550 polypeptide, but not holocytochrome c."].

## Curation decisions

- Holocytochrome-c synthase activity (GO:0004408) is complex-level; added as NEW with `contributes_to`. Core MF on CcmF itself is heme binding.
- Heme transmembrane transporter activity (IEA): REMOVE (no evidence of transport; heme arrives on holo-CcmE in the periplasm). Heme transport (IEA): MARK_AS_OVER_ANNOTATED.
- Quinol:heme oxidoreductase (GO:0016679, IDA): KEEP_AS_NON_CORE because the in vivo donor is unresolved; IBA GO:0016491 MODIFY to GO:0016679.
- Cytochrome complex assembly: MODIFY to GO:0018063; membrane: MODIFY to plasma membrane.
