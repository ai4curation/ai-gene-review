# ATP6V1E2 (V-type proton ATPase subunit E 2) — curation notes

UniProt: Q96A05 (VATE2_HUMAN). 226 aa. Gene HGNC:18125, chromosome 2.
Synonyms: ATP6E1, ATP6EL2, ATP6V1EL2.

## Identity and core function

ATP6V1E2 is one of two human paralogs encoding the "E" subunit of the V1 (peripheral,
cytoplasmic) sector of the vacuolar-type H(+)-ATPase (V-ATPase). The ubiquitously
expressed paralog is ATP6V1E1; ATP6V1E2 is the testis/sperm-restricted isoform
[PMID:12036578 "A human gene, ATP6E1, encoding a testis-specific isoform of H(+)-ATPase
subunit E"]. UniProt records TISSUE SPECIFICITY: "Testis specific"
[file:human/ATP6V1E2/ATP6V1E2-uniprot.txt "TISSUE SPECIFICITY: Testis specific. {ECO:0000269|PubMed:12036578}"].
Human Protein Atlas: "Tissue enriched (testis)"; Bgee: "Expressed in sperm and 140 other
cell types or tissues".

The V-ATPase is a rotary proton pump composed of a peripheral V1 complex that hydrolyzes
ATP and a membrane-integral V0 complex that translocates protons
[file:human/ATP6V1E2/ATP6V1E2-uniprot.txt "Subunit of the V1 complex of vacuolar(H+)-ATPase
(V-ATPase) ... a peripheral complex (V1) that hydrolyzes ATP and a membrane integral
complex (V0) that translocates protons"]. The V1 complex contains three catalytic AB
heterodimers forming a heterohexamer, three peripheral stalks each consisting of EG
heterodimers, one central rotor (subunits D and F), and regulatory subunits C and H
[file:human/ATP6V1E2/ATP6V1E2-uniprot.txt "The V1 complex consists of three catalytic AB
heterodimers ... three peripheral stalks each consisting of EG heterodimers, one central
rotor including subunits D and F, and the regulatory subunits C and H"].

Subunit E thus functions as part of the EG peripheral (stator) stalks that hold the (AB)3
catalytic head fixed against the torque produced when the central DF rotor turns during
ATP-hydrolysis-driven proton pumping. Its core molecular role is as a structural V1
peripheral-stalk component enabling rotary, ATP-driven proton transport. Family:
"Belongs to the V-ATPase E subunit family"
[file:human/ATP6V1E2/ATP6V1E2-uniprot.txt "SIMILARITY: Belongs to the V-ATPase E subunit family"].

## Localization

V-ATPase acidifies and maintains the pH of intracellular compartments and, in some cell
types, is targeted to the plasma membrane to acidify the extracellular environment
[file:human/ATP6V1E2/ATP6V1E2-uniprot.txt "responsible for acidifying and maintaining the
pH of intracellular compartments and ... targeted to the plasma membrane, where it is
responsible for acidifying the extracellular environment"]. For the testis-enriched E2
isoform the acrosome (a lysosome-related organelle in sperm) is a biologically plausible
site of action; GOA carries an Ensembl-orthology IEA "acrosomal vesicle" (GO:0001669)
annotation transferred from mouse Atp6v1e2 (UniProtKB:Q9D593).

## Interactions (GOA "protein binding" IPI annotations)

All GO:0005515 (protein binding) IPI annotations derive from high-throughput screens and
provide no specific functional information beyond confirming participation in PPIs:
- PMID:21516116 (Stitch-seq NGS interactome): with ATP6V1G1 (O75348).
- PMID:25416956 (Rolland et al., proteome-scale interactome): with ATP6V1G1 (O75348), BBLN (Q9BUW7).
- PMID:30021884 (histone crosslinking MS in nuclei): with ATP6V1G1 (O75348).
- PMID:32296183 (Luck et al. HuRI reference interactome): with RASSF10 (A6NK89), ATP6V1G1 (O75348), ATP6V1G2 (O95670), MESD (Q14696).
- PMID:40205054 (Schaffer et al. multimodal cell maps): with ATP6V1G2 (O95670).

Notably, UniProt INTERACTION lists curated interactions with ATP6V1G1 (NbExp=12) and
ATP6V1G2 (NbExp=7) [file:human/ATP6V1E2/ATP6V1E2-uniprot.txt "Q96A05; O75348: ATP6V1G1;
NbExp=12 ... Q96A05; O95670: ATP6V1G2; NbExp=7"]. These E–G interactions are biologically
meaningful: the V1 peripheral stalk is an E–G heterodimer, so the E2–G interactions
recapitulate the expected stator architecture. However, the bare GO:0005515 annotations
are uninformative as molecular-function statements and should be marked as over-annotated.

## regulation of macroautophagy (GO:0016241, NAS, PMID:22982048)

PMID:22982048 (Höhn et al., lipofuscin formation in senescent fibroblasts) is an NAS
(non-traceable author statement) annotation by ParkinsonsUK-UCL. The paper concerns
lipofuscin formation and macroautophagy/lysosomal activity in fibroblasts and does not
specifically study ATP6V1E2 (the testis-specific isoform). Any V-ATPase role in autophagy
is mediated by lysosomal acidification and is a downstream/indirect consequence, not a
core function of this testis-restricted subunit. NAS without a traceable experimental
link to this isoform — mark as over-annotated.

## Cytosol (GO:0005829, TAS Reactome x12)

Twelve identical TAS GO:0005829 (cytosol) annotations from Reactome reaction-level
records. The V1 sector is cytosolic/peripheral, so "cytosol" is defensible but is a coarse
location that does not capture the functional V-ATPase-complex / organelle-membrane
context. Keep as non-core.

## Summary of recommended actions

- ACCEPT: proton transmembrane transport (GO:1902600, IBA); proton-transporting ATPase
  activity, rotational mechanism (GO:0046961, IBA); V1 sector / two-sector ATPase
  catalytic-domain membership (GO:0033178, part_of).
- MARK_AS_OVER_ANNOTATED for redundant IEA duplicates of the IBA terms (GO:0046961,
  GO:1902600 IEA) — keep the IBA versions as the representative core annotations.
- MARK_AS_OVER_ANNOTATED: all GO:0005515 protein binding (high-throughput PPI).
- MARK_AS_OVER_ANNOTATED: GO:0016241 regulation of macroautophagy (NAS, not specific).
- KEEP_AS_NON_CORE: GO:0001669 acrosomal vesicle (ortholog IEA, plausible for testis
  isoform but unverified in human); GO:0005829 cytosol (TAS, coarse).
