# Actl7a (rat, UniProt Q641W9) - manual literature synthesis

No deep-research provider was available for this session, so this synthesis was written by the
reviewer from cached publications (`publications/PMID_*.md`) and the UniProt record. Quotes are
verbatim from the cached text. The companion human review (`genes/human/ACTL7A/`) was consulted for
the structural audit and PAINT reading; facts reused from it are re-anchored here to primary papers.

## Identity

- Rat Actl7a, Actin-like protein 7A (Arp7A, T-actin 2), 440 aa, RGD:1304697, GeneID 298017.
  Swiss-Prot reviewed, PE 1. Belongs to the actin family; carries the actin fold (Pfam PF00022) plus
  a unique N-terminal extension (Pfam PF16840, ACTL7A_N).
- The only experimental work on the rat protein itself is the co-immunoprecipitation from rat testis
  extracts in Boeda et al. 2011 [PMID:21278383 "immunoblot analysis of Tes immunoprecipitations (IP)
  with the indicated antibodies reveals that Arp7A, Tes, and Mena are complexed to each other in rat
  testes extracts"]. All other functional knowledge comes from mouse knock-outs and human patients.

## Molecular function

- The N-terminal extension binds the tandem LIM2-3 domains of testin (TES) [PMID:21278383 "The
  N-terminal 65-residue extension to the actin-like fold of Arp7A interacts directly with Tes.";
  "Two alanine residues from Arp7A that occupy equivalent apolar pockets in both LIM domains as well
  as an intervening GPAK linker that binds the LIM2-3 junction are critical for the Arp7A-Tes
  interaction."]. The binding assays and crystal structure used human Arp7A residues 1-65.
- Rat conservation (reviewer sequence check of the UniProt records): human residues 28-45
  (LQTASLRDGPAKRAVWVR) are identical in rat at residues 33-50, so the two apolar-pocket alanines
  (human A31/A41, rat A36/A46) and the GPAK linker (human 36-39, rat 41-44) are retained; the rat
  protein has a 5-residue longer N-terminus. The paper itself notes the extension is conserved
  [PMID:21278383 "The sequence of the first 65 residues of Arp7A is highly conserved among placental
  mammals"].
- Actin fold: no filament formation in cells [PMID:21278383 "In contrast, when expressed in HeLa
  cells, GFP-Arp7A is cytoplasmic and does not assemble into filaments or co-localize with and/or
  affect the localization of Tes and Mena at focal adhesions (data not shown)."]. Nucleotide binding
  and ATPase activity have never been measured. PAINT places GO:0005198 structural molecule activity
  on the ACTL7 node (PTN008986528) rather than the actin-specific structural constituent of
  cytoskeleton (see the human ACTL7A review notes for the PAINT table reading).
- Whether ACTL7A forms, nucleates or anchors subacrosomal F-actin is open [PMID:36734600 "it is not
  yet clear whether ACTL7A may be the filament-forming actin in the acroplaxome, or whether its role
  is to nucleate, stabilize formation, and/or anchor F-actin formed by conventional ARPs to the
  nuclear surface"].

## Location

- Subacrosomal layer (acroplaxome) of the perinuclear theca [PMID:21278383 "We have now extended
  these earlier studies and shown that Arp7A is actually localized in the subacrosomal layer, which
  is also known as the acroplaxome"]. Immunofluorescence in this paper was on mouse testis sections
  ("Adult mouse testes were fixed in 4% paraformaldehyde"), not rat.
- Golgi apparatus during acrosome biogenesis [PMID:21278383 "Arp7A is associated with the Golgi
  apparatus prior to and throughout the biogenesis of the acrosome"].
- Nucleus of germ cells (mouse) [PMID:12672658 "T-ACTIN-1 was found in the cytoplasm and T-ACTIN-2
  was located in the nucleus"]; [PMID:36734600 "Our intracellular localization data show ACTL7A to be
  dynamically present within the nucleus and subacrosomal space and later associated with
  postacrosomal regions of developing spermatids."].
- Sperm tail: reported only in the 2003 abstract [PMID:12672658 "In contrast, only T-ACTIN-2 was
  present in sperm heads and tails."]. The 2023 mouse study instead describes a connecting-piece
  pool, which GO does not place inside the flagellum (GO:0120212 sperm head-tail coupling apparatus
  has no part_of link to sperm flagellum).

## Process (mouse genetics, human disease)

- Acrosome biogenesis and attachment [PMID:36734600 "Through the generation of an Actl7a knock-out
  mouse model, we consistently observed disruption of acrosomal biogenesis with abnormal migration of
  the acrosomal granule and peeling acrosomes during spermatid elongation."]; subacrosomal F-actin is
  lost specifically [PMID:36734600 "Significantly, we found a complete loss of subacrosomal
  filamentous actin (F-actin) structures in knock-out spermatids suggesting a regulatory role for
  subacrosomal F-actin."].
- Sperm head shaping [PMID:37667331 "Immunofluorescence and TEM analyses revealed that the deletion of
  ACTL7A damaged the formation of acrosome-acroplaxome-manchette complex, leading to abnormalities in
  the shaping of sperm heads."].
- Fertilization [PMID:35921706 "Actl7a deficiency led to malformed formation of sperm acrosomes, male
  infertility, fertilization failure during in vitro fertilization (IVF) and intracytoplasmic sperm
  injection (ICSI), and reduced sperm-zona pellucida (ZP) binding ability."]; PLCzeta mislocalisation
  [PMID:32923619 "Furthermore, the sperm from ACTL7A/Actl7a-mutated men and mice showed reduced
  expression and abnormal localization of PLCζ as a potential cause of embryonic arrest and failure
  of fertilization."].
- Partners in the perinuclear theca: CYLC1 [PMID:38573307], FNDC8 [PMID:41169243 "ACTL7A, another
  essential PT protein, is required for acrosome biogenesis and mediates the tethering of the
  acrosomal outer membrane to the nucleus."].

## Gaps

- No rat-specific localisation, mutant or biochemical study exists.
- Nucleotide binding/hydrolysis and polymerisation behaviour of the actin fold are unmeasured.
