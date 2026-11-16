# PDE6B notes

Session 2026-11-16, review of 26 GOA rows (vision-disorder alignment campaign). Reviewed after
PDE6A with the same reasoning; see genes/human/PDE6A/PDE6A-notes.md.

## Function

- Catalytic beta subunit of rod PDE6 (PDE6A/PDE6B heterodimer plus two PDE6G) [file:human/PDE6B/PDE6B-uniprot.txt].
- Own catalytic site: the human PDE6B catalytic domain (aa 447-853) in a PDE6C-B chimera expressed in
  Xenopus rods hydrolyses cGMP like the PDE6A chimera [PMID:20940301 "Chimeric PDE6C-A and PDE6C-B
  catalyze hydrolysis of cGMP with equivalent K m and k cat values."]. Decision, as for PDE6A:
  molecular_function GO:0047555, in_complex GO:7770030.
- GAFa allosteric cGMP site: bovine cryo-EM [PMID:33007200]; NEW ISS row GO:0030553 cGMP binding.
- Geranylgeranylated (rat retina) [PMID:1309771]; PDE6D-assisted delivery to outer segments (mouse)
  [PMID:17496142].

## Disease

- Recessive RP40 (null alleles; PMID:8394174, human). Mouse rd1 and rd10 are Pde6b alleles; rat
  Pde6b knockout shows TUNEL-positive ONL degeneration from 3 weeks [PMID:31009522].
- Dominant CSNB (Rambusch pedigree): heterozygous His258 missense; the cached abstract reads
  "His258Asp" and lists an erratum (Nat Genet 1994 7:551) [PMID:8075643]; UniProt records H258N
  (VAR_009289, GAF 2 domain, aa 232-431) on this paper's evidence. No GO consequence.

## Questionable rows

- Row 5 (visual perception IMP, PMID:10393062): the paper screens PDE6A; its abstract mentions PDE6B
  only in a compilation. Mirror image of PDE6A row 6, which cites the PDE6B paper PMID:8394174. The
  two references look swapped between the genes, but full texts are not cached, so left to curators.
- Circadian entrainment rows (12, 13): source is mouse IMP PMID:30240620, which used rd1 mice as a
  tool to remove rods and cones; not a PDE6B-specific role.
- Retinal cell apoptotic process (24): rat knockout degeneration; PDE6B is not a participant.
