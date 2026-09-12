# SPC24 / MUN (Q67XT3) — Arabidopsis thaliana — research notes

UniProt **Q67XT3** (`SPC24_ARATH`), reviewed/Swiss-Prot, PE=1, 201 aa.
Gene **SPC24** (synonym **MUN**, MERISTEM UNSTRUCTURED); locus **At3g08880**
(TAIR: AT3G08880 = MUN). Ortholog of the sorghum SORBI_3003G204000 (C5XPJ5)
reviewed in this project.

## Identity / family
- InterPro **IPR044951** "SPC24-like"; Gene3D 3.30.160.570 (Ncd80 complex, Spc24
  subunit); PANTHER **PTHR35730** (subfamily SF2). Q67XT3 is the single reviewed
  member of PTHR35730. Coiled-coil 78-133 (UniProt FT).
- SPC24 family (UniProt SIMILARITY). N-terminal coiled-coil + C-terminal RWD-like
  globular domain; pairs with SPC25 to anchor NDC80-NUF2 to the inner kinetochore.

## Defining experimental study
[PMID:29356153 Shin et al. 2018 Plant J, "MUN (MERISTEM UNSTRUCTURED), encoding a
SPC24 homolog of NDC80 kinetochore complex..."] — abstract-only in cache, but it
is the source of UniProt FUNCTION/SUBUNIT/LOCATION/TISSUE/DISRUPTION and of all
TAIR experimental (IDA/IMP/IPI) annotations.
- FUNCTION: component of the essential NDC80 complex, required for chromosome
  segregation and spindle-checkpoint activity; required for plant architecture.
- SUBUNIT: component of NDC80 complex (NDC80, NUF2, SPC24, SPC25).
- LOCATION: chromosome/centromere; colocalizes with CENH3 (HTR12).
- DISRUPTION: embryonic lethality (division arrest before globular stage); weak
  allele mun-1 (T-DNA in promoter) -> stunted growth, embryo arrest, DNA
  aneuploidy, chromosome-segregation defects, low cell-division rate, unstructured
  SAM with ectopic WUSCHEL.
- "Interactions among the components of the NDC80 complex were confirmed in a
  yeast two-hybrid assay and in planta co-immunoprecipitation."

## IPI partners (GO:0005515 protein binding, WITH/FROM AGI codes) -> NDC80 complex
- **AT3G54630 = AtNDC80**
- **AT1G61000 = AtNUF2**
- **AT3G48210 = AtSPC25**
[Identified via WebSearch of the Arabidopsis kinetochore literature; AtNUF2
(AT1G61000) is the subject of PMID:33993566, which states NUF2 binds SPC25.]
These three IPI rows (collapsed by the seeder into one GO:0005515 entry)
experimentally establish NDC80-complex assembly and corroborate the ISS
GO:0031262 annotation.

## Annotation review summary (12 GOA lines / 10 deduped entries)
- GO:0000776 kinetochore (IDA) — ACCEPT, core CC.
- GO:0031262 Ndc80 complex (ISS from human SPC24 Q8NBT2) — ACCEPT, core CC,
  experimentally confirmed in Arabidopsis.
- GO:0000775 chromosome, centromeric region (IEA/SubCell) — ACCEPT.
- GO:0005634 nucleus (IDA + ISM) — ACCEPT (correct but generic vs kinetochore).
- GO:0051983 regulation of chromosome segregation (IMP + IEA) — ACCEPT, core BP.
- GO:0051781 positive regulation of cell division (IMP) — ACCEPT (phenotype:
  reduced division rate / embryonic arrest).
- GO:0009933 meristem structural organization (IMP) — KEEP_AS_NON_CORE
  (downstream developmental consequence of impaired division; ectopic WUSCHEL).
- GO:0005515 protein binding (IPI x3) — ACCEPT but not core; meaning captured by
  Ndc80 complex CC. Per project guidance, bare "protein binding" is not promoted
  to a core molecular function.

## Other partner/context refs
- [PMID:33993566] AtNUF2 modulates spindle MT organization and chromosome
  segregation; NUF2 binds SPC25. Corroborating, MEDIUM relevance.
