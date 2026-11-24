# SCL27 / AtHAM1 manual deep research

Automated deep research failed for both `falcon` and its `perplexity-lite`
fallback because the installed `deep-research-client` reported only
`claude_code` as an available provider. This file records the manual literature
synthesis used for the SCL27 review.

## Identity and family

`SCL27` is UniProtKB:Q7XJM8 and Arabidopsis locus `AT2G45160`. The current
UniProt record maps it to TAIR symbol `HAM1`; older and paper-specific names
include AtHAM1, LOM1 and SCL6-II. Ma et al. 2014 explicitly align the SCL6/HAM
aliases used in the miR171 literature with locus symbols in their primer table:
`SCL27 (At2G45160), SCL22 (At3G60630), SCL6 (At4G00150)` [PMID:25101599,
"SCL27 (At2G45160), SCL22 (At3G60630), SCL6 (At4G00150)"].
Schulze et al. 2010 likewise map the LOST MERISTEMS nomenclature to the same
first two loci: their methods identify `LOM1` insertions with `At2g45160`
primers and `LOM2` insertions with `At3g60630` primers.

SCL27 belongs to the plant-specific GRAS transcriptional-regulator family. The
protein has an N-terminal low-complexity/disordered region and a C-terminal GRAS
domain with LRI, VHIID, LRII, PFYRE and SAW subregions, matching the typical
GRAS architecture of transcriptional regulators.

## Nuclear transcriptional regulator

Lee et al. performed a large-scale reverse-genetics, expression, interaction and
subcellular-localization survey of Arabidopsis GRAS proteins and UniProt cites
that paper for SCL27 nuclear localization. The abstract-only cache does not
spell out SCL27 specifically, but Wang et al. 2010 report that SCL6-II/SCL27,
SCL6-III/SCL22 and SCL6-IV/SCL6 are nuclear and can activate transcription in a
reporter setting [PMID:20720155, "SCL6-II, SCL6-III, and SCL6-IV are located
to the nucleus, and show transcriptional activation activity."].

The best molecular-function evidence is Ma et al. 2014. They showed that SCL27
represses light-grown chlorophyll biosynthesis by directly controlling the
`PORC` promoter: promoter-luciferase assays in tobacco localized the responsive
region, Arabidopsis ChIP-qPCR enriched two `PORC` promoter fragments with
tagged SCL27, and purified His-SCL27 shifted the corresponding promoter DNA in
EMSA. Mutation and competitor experiments on a 62-bp fragment showed that the
GT elements in that promoter segment are required for SCL27 binding
[PMID:25101599, "GT elements are required for SCL27 to bind to the PORC
promoter"]. This supports both direct DNA binding and transcriptional
regulation.

Ma et al. also showed SCL27-DELLA coupling. SCL27 interacted with DELLA proteins
in yeast two-hybrid and co-immunoprecipitation assays, and RGA reduced SCL27
binding to the `PORC` promoter in EMSA/ChIP experiments [PMID:25101599, "SCL27
interacts with DELLA proteins in vitro and in vivo"]. Thus SCL27 is a direct
DNA-binding transcription factor whose promoter occupancy can be attenuated by
GA/DELLA signaling.

## miR171/HAM/LOM developmental functions

Wang et al. 2010 showed that miR171c targets the redundant SCL6-II/SCL27,
SCL6-III/SCL22 and SCL6-IV/SCL6 transcripts. MIR171c overexpression and the
triple mutant both reduced shoot branching, and a miR171c-resistant version of
any one SCL6 gene rescued that branching phenotype in the overexpression
background [PMID:20720155, "Expression of any one of the miR171c-resistant
versions of SCL6-II, SCL6-III, and SCL6-IV in 35Spro-MIR171c plants rescues the
reduced shoot branching phenotype."]. The abstract also reports pleiotropic
phenotypes: increased chlorophyll, decreased primary root elongation and
abnormal leaf and flower patterning.

Schulze et al. 2010 described the `LOST MERISTEMS` function of these GRAS
regulators in shoot apical meristems. In short photoperiods, higher-order
`lom` mutants had arrested meristems with over-proliferation of meristematic
cells, loss of polar organization, early arrest of axillary meristem
development and ectopic meristematic clusters in stems. The abstract concludes
that `LOM1` and `LOM2` promote cell differentiation at the shoot-meristem
periphery [PMID:21070418, "LOM1 and LOM2 promote cell differentiation at the
periphery of shoot meristems"].

Engstrom et al. 2011 independently analyzed Arabidopsis homologs of Petunia
`HAIRY MERISTEM`. The abstract reports that `Atham1,2,3` triple mutants lose
indeterminacy in both shoot and root and that their root meristems are smaller
because of reduced meristem cell division culminating in root-meristem arrest
[PMID:21173022, "reduced rates of meristem cell division that culminate in root
meristem arrest"]. The public full text additionally reports elevated branching
and transient swelling of Atham1,2,3 root hairs, supporting the root-hair
tip-growth annotations as peripheral HAM-clade phenotypes. The meristem and
root-hair phenotypes do not themselves identify a second molecular activity
beyond SCL27's nuclear transcriptional regulatory activity.

A QuickGO comparator check showed that TAIR currently annotates the upstream
Arabidopsis root-hair transcription factor RHD6 to `GO:0048768 root hair cell
tip growth`, whereas the downstream RHD6 target RSL4 has `GO:0048766 root hair
initiation` and lacks `GO:0048768`. That makes the standing SCL27 `GO:0048768`
rows a plausible but non-core TAIR/HAM-clade process convention, not evidence
that all root-hair transcription factors should carry the term.

## GO-CAM 67e5e74400000148 consistency

GO-CAM model `67e5e74400000148`, "Arabidopsis MRG domain proteins bridge two
histone modifications", uses `AT2G45160/SCL27` as the enabler for
`GO:0043995 histone H4K5 acetyltransferase activity`. The SCL27 literature
instead identifies `AT2G45160` as a HAM/LOM GRAS transcription factor; its
protein sequence lacks a MYST acetyltransferase domain and no paper reviewed
here supports any histone acetyltransferase activity. The most likely error is
a symbol collision with the unrelated Arabidopsis MYST histone acetyltransferase
`HAM1`, encoded by `AT5G64610`.
