# aroG (O53512, Rv2178c) - Mycobacterium tuberculosis H37Rv type II DAHP synthase - notes

## Provenance

Provider deep research (`just deep-research`) was unavailable for this review (no provider
key in the session), so no `aroG-deep-research-*.md` file exists. These notes are built from
the UniProt record (aroG-uniprot.txt), the cached publications under `publications/` (all
abstract-only, `full_text_available: false`), the Reactome entry R-MTU-964912, the PANTHER
family review `interpro/panther/PTHR21337/PTHR21337-review.yaml` and GO term definitions
read from the cached GO sqlite via runoak. The three synergistic-allostery papers
(PMID:20667835, PMID:22154807, PMID:23274137) were found by a PubMed title search and cached
for this review; UniProt lists them only as PDB references without PubMed ids.

## Identity and family

- 462-aa (UniProt; the 2009 papers quote 472 aa from an older start) type II
  3-deoxy-D-arabino-heptulosonate 7-phosphate synthase (DAH7PS, EC 2.5.1.54). UniProt:
  "Belongs to the class-II DAHP synthase family." Pfam PF01474 DAHP_synth_2, NCBIfam
  TIGR01358, PANTHER PTHR21337:SF0. It is the only DAH7PS of M. tuberculosis.
- Reference protein of the PTHR21337 family review. It is a seed of the family-root PAINT node
  PTN000481914 (GO:0003849), judged SOUND there. The chorismate-biosynthesis IBD
  (PTN008369313) and the chloroplast IBD sit on the plant/diatom node and do not reach aroG;
  the family review notes that placement is shallower than the biology.

## Activity

- UniProt CC FUNCTION (ECO:0000269|PubMed:16288916): "Catalyzes an aldol-like condensation
  reaction between phosphoenolpyruvate (PEP) and D-erythrose 4-phosphate (E4P) to generate
  3-deoxy-D-arabino-heptulosonate 7-phosphate (DAH7P) and inorganic phosphate."
  Km E4P 25 uM, Km PEP 37 uM, kcat 3.1 s-1.
- [PMID:16288916 "The type II DAH7PS from M.tuberculosis has been expressed in Escherichia
  coli, purified, functionally characterized and crystallized. It is found to be metal
  ion-dependent and subject to feedback inhibition by phenylalanine, tryptophan, tyrosine and
  chorismate, with a significant synergistic effect when tryptophan is used in combination
  with phenylalanine."]
- Structure with PEP and Mn2+: [PMID:16288916 "The crystal structure of M.tuberculosis DAH7PS
  has been determined by single-wavelength anomalous diffraction and refined at 2.3A in
  complex with substrate phosphoenolpyruvate and Mn(2+)."] Common catalytic scaffold with
  type I: [PMID:16288916 "The monomer fold, the arrangement of key residues in the active
  site, and the binding modes of PEP and Mn(2+), all match those of the type I enzymes, and
  indicate a common ancestry for the type I and type II DAH7PSs, despite their minimal
  sequence identity."]
- Independent purification with activity: [PMID:15721768 "An approximately threefold
  purification protocol yielded homogeneous enzyme with a specific activity value of 0.47U
  mg(-1) under the experimental conditions used."] and first committed step [PMID:15721768
  "The M. tuberculosis aroG-encoded 3-deoxy-d-arabino-heptulosonate 7-phosphate synthase
  (mtDAHPS) catalyzes the first committed step in this pathway."]

## Metal

- UniProt COFACTOR (ECO:0000269|PubMed:16288916): "Binds 1 divalent cation per subunit. The
  enzyme is active with manganese, cobalt or cadmium ions." Mn2+ ligands at residues 87,
  369, 411, 441 (FT BINDING, ECO:0000269 and PDB 2B7O). Mn2+ is the metal seen in the
  structure; the physiological metal in M. tuberculosis is not established.

## Oligomeric state

- [PMID:15721768 "Gel filtration chromatography results demonstrate that recombinant mtDAHPS
  is a pentamer in solution."] The crystal structures disagree with a pentamer:
  [PMID:16288916 "The structure reveals a tightly associated dimer of (beta/alpha)(8) TIM
  barrels."] and the inhibitor complexes are tetramers [PMID:20667835 "The MtuDAH7PS/Trp/Phe
  homotetramer binds four Trp and six Phe molecules."] UniProt SUBUNIT: "Homodimer."
  Homo-oligomerisation is real (dimer/tetramer); the pentamer stoichiometry is superseded.

## Synergistic feedback inhibition

- [PMID:20667835 "Whereas Mycobacterium tuberculosis DAH7PS (MtuDAH7PS) is not inhibited by
  the addition of Phe, Tyr, or Trp alone, combinations cause significant loss of enzyme
  activity."] Trp and Phe bind separate allosteric sites on accessory elements unique to type
  II DAH7PS: [PMID:20667835 "Binding sites for both aromatic amino acids are formed by
  accessory elements to the core DAH7PS (β/α)(8) barrel that are unique to the type II DAH7PS
  family and contribute to the tight dimer and tetramer interfaces."]
- Mechanism is dynamic rather than conformational: [PMID:22154807 "Isothermal titration
  calorimetry experiments demonstrate that the inhibitor binding sites are in direct
  communication."]
- A third, Tyr-selective site: [PMID:23274137 "DAH7PS from M. tuberculosis possesses a
  Tyr-selective site in addition to the Trp and Phe sites, revealing an unusual and highly
  sophisticated network of three synergistic allosteric sites on one enzyme."]

## Chorismate mutase partnership

- AroG (MtDS, Rv2178c) forms a noncovalent complex with the intracellular AroQ-delta
  chorismate mutase MtCM (Rv0948c) and activates it: [PMID:19556970 "However, its catalytic
  efficiency increases >100-fold on addition of DAHP synthase (MtDS; Rv2178c), another
  shikimate-pathway enzyme."] Complex architecture: [PMID:19556970 "The 2.35 A crystal
  structure of the MtCM-MtDS complex bound to a transition-state analogue shows a central core
  formed by four MtDS subunits sandwiched between two MtCM dimers."] Activation mechanism:
  [PMID:19556970 "Structural comparisons imply catalytic activation to be a consequence of the
  repositioning of MtCM active-site residues on binding to MtDS."] The complex makes CM
  activity sensitive to Phe/Tyr: [PMID:19556970 "The chorismate-mutase activity of the
  complex, but not of MtCM alone, is inhibited synergistically by phenylalanine and
  tyrosine."]
- Crystallisation report of the same complex: [PMID:19851019 "The MtCM-MtDS complex represents
  the first noncovalent enzyme complex from the common shikimate pathway to be structurally
  characterized."]
- GO MF reading: AroG binds MtCM and increases its catalytic activity, which fits GO:0008047
  enzyme activator activity ("A molecular function regulator that increases a catalytic
  activity."). This is a second, non-catalytic activity of AroG.

## Location

- Soluble cytosolic enzyme, no TM segment or signal peptide in the record. Reactome places the
  reaction in the cytosol: [Reactome:R-MTU-964912 "The first committed step in the
  biosynthesis of chorismate is the fusion of D-erythrose-4-phosphate with
  phosphoenolpyruvate, catalyzed by AroG (Rizzi et al, 2005; Webby et al, 2005)."]
- The plasma-membrane HDA row comes from membrane-fraction proteomics of H37Rv
  [PMID:14532352 "we have profiled the membrane protein fraction of the M. tuberculosis H37Rv
  strain using an analytical platform that couples one-dimensional SDS gels to a
  microcapillary liquid chromatography-nanospray-tandem mass spectrometer."] Detection of an
  abundant soluble enzyme in a membrane fraction is not evidence of membrane residence.

## GO term checks (cached GO via runoak)

- GO:0009423 chorismate biosynthetic process is not a descendant of GO:0009073 aromatic amino
  acid biosynthetic process; they are separate pathway claims.
- GO:0051260 protein homooligomerization: "The process of creating protein oligomers,
  compounds composed of a small number, usually between three and ten, of identical component
  monomers."
