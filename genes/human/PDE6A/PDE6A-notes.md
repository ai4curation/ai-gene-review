# PDE6A notes

Session 2026-11-16, review of 22 GOA rows (vision-disorder alignment campaign).

## Function

- PDE6A is one of the two catalytic subunits of rod PDE6 (PDE6A/PDE6B heterodimer plus two
  PDE6G). UniProt: "Catalytic alpha subunit of the rod-specific cGMP phosphodiesterase (PDE6)
  complex, which hydrolyzes 3',5'-cyclic GMP in the phototransduction cascade"
  [file:human/PDE6A/PDE6A-uniprot.txt].
- Own catalytic site: the human PDE6A catalytic domain (aa 449-860), fused to PDE6C GAF domains
  and expressed as a homodimer in transgenic Xenopus rods, hydrolyses cGMP with Km 20-23 uM and
  kcat 4200-5100 s-1, like the PDE6B chimera [PMID:20940301 "Chimeric PDE6C-A and PDE6C-B catalyze
  hydrolysis of cGMP with equivalent K m and k cat values."]. The native AB dimer is "functionally
  inseparable" (same paper), and the bovine cryo-EM structure shows two catalytic sites, each
  blocked by one PDE6G C-terminus [PMID:33007200 "The C-terminus of each PDEγ subunit binds at the
  entrance of the active site of each catalytic domain"]. Decision: the activity is the subunit's
  own (molecular_function GO:0047555), exercised inside the heterotetramer (in_complex
  GO:7770030). The same reasoning is applied to PDE6B.
- GAF domains bind cGMP (non-catalytic, allosteric): shown on native bovine PDE6 [PMID:33007200
  "each GAFa domain that has an allosteric site occupied by a cGMP molecule"]; human residues are
  annotated by similarity to bovine P11541. GO term: GO:0030553 cGMP binding. Added as a NEW ISS row.
- Two transducins are needed for full activation (bovine) [PMID:30068566].
- Prenylation: PDE6 alpha is farnesylated, beta geranylgeranylated (rat retina, in vivo)
  [PMID:1309771]; PrBP/delta (PDE6D) needed for efficient outer segment delivery (mouse)
  [PMID:17496142]. Folding/assembly requires the chaperone AIPL1, which binds PDE6A (mouse)
  [PMID:19758987; PMID:27268253]. These are facts about PDE6A as a client; no GO row for PDE6A.
- Location: disc rims of rod outer segments (Xenopus, chimeric construct) [PMID:20940301].

## Species

Enzymology on bovine native PDE6 and human catalytic domains in Xenopus rods; trafficking in
mouse; prenylation in rat. Human evidence is genetic: recessive RP43 [PMID:7493036; PMID:10393062].

## Questionable rows

- Row 6 (visual perception IMP, PMID:8394174): the cached abstract is about PDE6B mutations only;
  the claim is true for PDE6A on PMID:7493036, so accepted; possible mis-keyed reference left to
  the curator (full text not available).
- cAMP PDE activity and negative regulation of cAMP/PKA signalling (IBA) are propagated from the
  cAMP-directed branch; PDE6A is cGMP-specific.
- Plasma membrane rows: PDE6 is on disc membranes; the Reactome row is from the WNT5A/Ca2+ pathway.
