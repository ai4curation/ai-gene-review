# MCA1 manual review notes

## 2026-09-30

MCA1/YCA1 is the sole budding-yeast type I metacaspase. UniProt Q08601 places
the conserved catalytic residues at His220 and Cys276, and PMID:22761449
experimentally verified both residues: the H220A and C276A mutants failed
Ca(2+)-stimulated autoprocessing and Bir1p-fragment cleavage, while H277A did
not [PMID:22761449 Crystal structure of the yeast metacaspase Yca1., "Cys 276
and His 220 constitute the catalytic dyad residues"]. The same study showed that
Yca1 autoprocessing and substrate cleavage are specifically stimulated by
calcium rather than by Mg(2+), Zn(2+), Mn(2+), Ni(2+), Ba(2+), or Co(2+)
[PMID:22761449, "only Ca 2+ specifically enhanced the autocatalytic processing
of Yca1"].

The `GO:0004198 calcium-dependent cysteine-type endopeptidase activity` rows are
therefore well supported. `PMID:29363267` is abstract-only in the local cache,
but the abstract is direct enough for the Ddi1 row: Ddi1 is described as a
conserved metacaspase substrate in trypanosomes and yeasts, and yeast Ddi1
cleavage is reported to occur when calcium increases under specific metabolic
conditions [PMID:29363267 DNA-damage inducible protein 1 is a conserved
metacaspase substrate that is cleaved and further destabilized in yeast under
specific metabolic conditions., "Ddi1 cleavage is tightly regulated in vivo as
it only takes place in yeast when calcium increases but under specific metabolic
conditions"]. The broader PAINT, ARBA, and proteolysis rows are broad rather
than wrong.

Mca1 has a core protein-quality-control role that is independent of terminal
cell death. Lee et al. found Yca1 complexes enriched for aggregate-remodeling
chaperones, heat-induced Yca1-GFP colocalization with Hsp104-marked aggregates,
and increased aggregate/autophagic-body accumulation in deletion and catalytic
mutants [PMID:20624963 Metacaspase Yca1 is required for clearance of insoluble
protein aggregates., "deletion and inactivation mutants of Yca1 accrue protein
aggregates and autophagic bodies during log-phase growth"]. The N-terminal
Q/N-rich prodomain is the aggregate-targeting region in the same paper. Hill et
al. later localized Mca1 to IPOD/JUNQ during aging and proteostatic stress
[PMID:24855027 Life-span extension by a metacaspase in the yeast Saccharomyces
cerevisiae., "Mca1 is recruited to the insoluble protein deposit (IPOD) and
juxtanuclear quality-control compartment (JUNQ) during aging and proteostatic
stress"], which is enough to accept the broad cytosol row but not enough to add
new, narrower compartment terms from the abstract alone.

The fungal `GO:0006915 apoptotic process` rows should be accepted rather than
treated as the kind of assay-only over-annotation seen in mouse survival-kinase
papers. The founding Madeo et al. abstract ties peroxide treatment to
YCA1-dependent caspase-like activity and apoptosis, with the response abrogated
by YOR197W/YCA1 disruption and stimulated by overexpression [PMID:11983181 A
caspase-related protease regulates apoptosis in yeast., "This response is
completely abrogated after disruption and strongly stimulated after
overexpression of Yor197w"]. Mazzoni et al. places Yca1 downstream of
mRNA-stability perturbation: deleting YCA1 in the Kllsm4Delta1 background
suppressed rapid death, TUNEL-positive DNA fragmentation, ROS accumulation, and
mitochondrial fragmentation while mRNA levels remained high [PMID:16170310
Yeast caspase 1 links messenger RNA stability to apoptosis in yeast.,
"positioning the budding yeast caspase Yca1 as a downstream executor of cell
death induced by mRNA stability"]. Khan et al. independently compared H2O2
treated wild type and yca1 deletion cells, showing loss of phosphatidylserine
externalization and TUNEL-positive nuclei in the mutant [PMID:16301538 Knockout
of caspase-like gene, YCA1, abrogates apoptosis and elevates oxidized proteins
in Saccharomyces cerevisiae., "apoptosis was abrogated in the Delta yca1 strain,
whereas wild type underwent apoptosis as measured by externalization of
phosphatidylserine and the display of TUNEL-positive nuclei"].

I did not narrow the yeast `GO:0006915` rows to `GO:0097194 execution phase of
apoptosis`. That term was appropriate for metazoan effector caspases and DFFB,
but the local MCA1 sources do not identify a comparable execution-substrate set
or place Mca1 downstream of a conserved metazoan apoptosome.
