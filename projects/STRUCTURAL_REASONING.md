---
title: "Structural Reasoning in Annotation Review"
maturity: IN_PROGRESS
tags: [PIPELINE, BIOLOGY_DOMAIN]
species: [human]
genes: [SLC10A1, SLC10A2, SLC10A4, SLC10A6, SLC10A7]
manifest:
  artifacts:
    - href: https://claude.ai/artifact/VonifPVfZAE7t96cv4Jpaz
      title: SLC10 residue evidence
      description: Interactive NTCP structure and annotated alignment
---

# Structural Reasoning in Annotation Review

**Bottom line:** coordinates can settle a specific class of curation question —
*does this protein still have the residues its characterised relative uses?* — and
the first worked example refuted the hypothesis it was built to confirm. The method
is: define a functional site from ligand contacts in a deposited structure, record
whether each contact is made by a side chain or a backbone atom, map those positions
onto relatives by sequence alignment, and store the result as residue claims that a
validator can re-check against UniProt. The discipline that makes it worth doing is
knowing what the answer does **not** license: a retained site is not retained
activity, and a predicted model is not a predicted complex.

We want this because "lacks the catalytic residue" is one of the most consequential
claims a reviewer can make and one of the easiest to get wrong. Of 17 such claims
surveyed in this repository, [four were about proteins whose site was fully
intact](#why-this-exists). That is the error this project exists to make hard.

## The method

Five steps, each of which can fail loudly rather than quietly:

1. **Define the site from coordinates, not memory.** Take every residue of the
   reference protein with a heavy atom within a stated cutoff of a bound ligand in a
   named entry. Where UniProt curates no binding-site features — true for NTCP —
   there is no feature table to copy, and inventing one from recall is how a wrong
   position enters the record.
2. **Record the atom, not just the residue.** A contact made by a backbone atom is
   sequence-independent: any residue at that position makes it, so a substitution
   there is not loss of the site. Residue-level provenance cannot express this, and
   conflating the two is what turns a harmless substitution into a false claim of
   degeneration.
3. **Map positions by alignment, not by geometry.** Nearest-Cα pairing after
   superposition looks appealing and fails: in this project it frame-shifted the
   method control by four residues. The decisive mapping is the sequence alignment;
   the superposition is illustration.
4. **Calibrate with controls that have the function.** A low conservation score means
   nothing without relatives that are known to perform the activity and do retain the
   site. Without them, a mislabelled control makes every real enzyme look degenerate.
5. **Store it where it can be re-checked.** Sites live in a family review; gene
   reviews cite them by id; a validator confirms both sides against live UniProt
   sequences. Prose claims cannot be re-checked and drift silently.

## Worked example: the SLC10 family

The first application covers seven gene reviews across the bile acid:sodium symporter
family — SLC10A1, SLC10A2, SLC10A4, SLC10A6 and SLC10A7 in human, plus the rat and
mouse Slc10a1 orthologues — together with a family review for PANTHER PTHR10361 and
an [enterohepatic bile salt cycling module](../modules/enterohepatic_bile_salt_cycling.yaml).

The question was structural because two reviews had made it so. The SLC10A4 review
accepted the deliberately uninformative parent term `GO:0022857` partly on the ground
that "the fold and topology are demonstrably retained", and the SLC10A7 review
recorded an unidentified-substrate gap on similar footing. Neither claim had been
checked against coordinates.

**The hypothesis was that SLC10A4 had lost the sodium site, and that this explained
its orphan status. It was refuted.** All seven side-chain sodium ligands are
retained; the single substitution sits at a backbone-only contact and changes nothing
that touches the ion. SLC10A7 is the opposite case, and the two sodium-coupled
relatives that keep the site are what make its divergence readable rather than merely
a low number.

| Protein | Sodium-site side-chain ligands | Role in the comparison |
|---|---|---|
| SLC10A1 (NTCP) | reference | the characterised member, eleven cryo-EM entries |
| SLC10A2 (ASBT) | retained | positive control, transports bile salts |
| SLC10A6 (SOAT) | retained | positive control, sodium-coupled |
| SLC10A4 | retained | orphan — the hypothesis under test |
| SLC10A7 | lost | Golgi, no demonstrated transport |

Two of the project's own errors were caught by its checks rather than by judgement: a
Fab light chain from the experimental entry survived a buggy chain-pruning loop into
the published figure, and a bound bile salt was missed because the ligand list came
from an entry-summary field that reported only the sodium. Both are now structural
guarantees in the export rather than things to remember.

## What the method cannot do

This matters more than the result. A structural comparison of this kind supports a
negative:

> SLC10A4's orphan status should not be explained by loss of the sodium-coordinating
> residues.

and does not support the corresponding positive. A protein can keep the full ligand
set and still fail to transport, through the substrate pocket, substrate access,
gating, localization, regulation, oligomerization, or the coupling between ion and
substrate movement. Predicted models compound this: AlphaFold models are apo and
protein-only, so any ion or ligand shown beside one has been carried across by
superposition and is not a predicted interaction.

Three further limits are worth stating wherever this method is used:

- **A contact set depends on its cutoff and its conformational state.** Two entries of
  the same protein can disagree about which atom is closest. NTCP E257 coordinates
  sodium through its carboxylate in one entry while in another the nearest atom of the
  same residue is its backbone oxygen — so a distance is only interpretable with its
  source attached.
- **Some pockets are not diagnostic.** A small polar ion site has interpretable
  chemistry; a broad amphipathic substrate pocket, most of whose wall is hydrophobic
  and whose ligand is a model fitted into density, does not. Curate the polar anchors,
  not the shell.
- **A site is only worth curating when its residues decide the function.** A candidate
  site was drafted for the hepatitis B preS1 myristoyl pocket and rejected: rodent
  Ntcp retains all six positions and still restricts infection, so the pocket does not
  determine receptor competence. That observation became a scoping note on the term
  instead.

## Infrastructure this added

- `site_source: STRUCTURE` on family-review residue sites, for positions read from
  deposited coordinates rather than from a feature table or a paper's prose.
- `contact_atom`, `contact_via`, `contact_distance`, `contact_ligand` and
  `contact_structure` on a residue, so a site records which atom approaches the
  ligand, through side chain or backbone, how close, to what, and in which entry.
- A reproducible pipeline under
  `genes/human/SLC10A4/SLC10A4-bioinformatics/` that fetches the structures, defines
  the sites, runs the method control, and exports both the residue table and the
  viewer payload.

## Why this exists

The residue-site validator in this repository was written after a survey found that
four of 17 "lacks the catalytic residue" claims were made about proteins whose site
was intact. This project is the positive counterpart: rather than only catching false
claims of loss, it produces checkable claims of retention. The SLC10A4 review now
carries seven explicit `RETAINED` claims attached to the annotation that was
*removed*, so that a later reader cannot infer a degenerate site from a deleted
annotation.

## Related projects

- [PDB](PDB.md) — deposited structures as functional-insight evidence, the
  experimental-structure inventory this draws on.
- [AlphaFold](ALPHAFOLD.md) — predicted structures as computational evidence, scoped
  but not yet a pipeline.

## Next

- Apply the method to a family where the expected answer is loss, to test that it
  reports degeneration as readily as retention.
- Decide whether `ResidueClaim` should carry the same atom-level provenance as the
  family-level site, so a gene-level claim is self-describing.
- Bring the remaining SLC10 members (SLC10A3, SLC10A5) and the plant BASS and
  Acr3-related branches into the family review, or record explicitly why they are out
  of scope.
