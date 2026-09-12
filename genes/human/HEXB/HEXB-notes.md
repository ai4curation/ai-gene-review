# HEXB (P07686) review notes

Beta subunit of lysosomal beta-hexosaminidase. Shared subunit of two isozymes:
- **Hex A** = alpha-beta heterodimer (HEXA + HEXB)
- **Hex B** = beta-beta homodimer (HEXB only)
(A third labile isozyme, **Hex S**, is the alpha-alpha homodimer of HEXA.)

The beta subunit carries a catalytic active site (as in HexB, ββ). Enzyme hydrolyses
terminal non-reducing N-acetyl-D-hexosamine (β-GalNAc/GlcNAc) residues (EC 3.2.1.52)
from gangliosides (GM2/GA2), glycosaminoglycans (dermatan/keratan sulfate, hyaluronan
fragments), oligosaccharides and glycoproteins. Localises to lysosome/lysosomal lumen.
Deficiency (affecting BOTH HexA and HexB) causes Sandhoff disease = GM2 gangliosidosis
type 2 (GM2G2, MIM:268800).

## Key active-site / substrate-specificity facts
- Active-site proton donor = Glu-355 (ACT_SITE 355, PMID:11329289). Asp-354 and Asp-241
  also catalytically important; Glu-491 dispensable. pH optimum 4. [PMID:11329289]
- The **beta-active site** (present in both Hex A and Hex B) hydrolyses **neutral**
  substrates; the alpha-active site additionally hydrolyses **sulfated/negatively
  charged** substrates. Only Hex A + GM2 activator degrades GM2 ganglioside at
  physiological rates. [PMID:8672428, PMID:8663217, PMID:11707436]
- Hex B degrades sulfated GAG fragments (dermatan sulfate) and neutral N-glycan
  fragments; Reactome details HEXB cleaving terminal GalNAc/GlcNAc from DS, keratan
  sulfate and hyaluronan fragments (R-HSA-9638075/6/8).

## GOA MF term to use (verified current label via OLS)
- **GO:0004563 beta-N-acetylhexosaminidase activity** — this is the exact MF term carried
  by GOA (IBA/IEA/EXP/IDA/TAS) and confirmed current. Use as core MF.
- Complex: **GO:1905379 beta-N-acetylhexosaminidase complex** (ComplexPortal IPI,
  PMID:16698036). Use via in_complex.

## Core BP (verified)
- **GO:0006689 ganglioside catabolic process** — IDA (PMID:8123671, PMID:8672428) + IBA.
- **GO:0030203 glycosaminoglycan metabolic process** — IDA (ComplexPortal PMID:11707436,
  PMID:25645918) + IBA + Ensembl.

## Localization
- Lysosome (GO:0005764) EXP PMID:9694901; lysosomal lumen (GO:0043202) many Reactome TAS.

## Notes on over-annotations / peripheral
- Many IPI "protein binding" (GO:0005515) from high-throughput interactome screens
  (PMID:28514442, 32296183, 32814053, 33961781) — MARK_AS_OVER_ANNOTATED per policy
  (bare protein binding, uninformative). PMID:16698036 IPI is HEXA (P06865), the genuine
  biological partner (Hex A heterodimer) → informative, but term is still bare protein
  binding → MARK_AS_OVER_ANNOTATED but note the HEXA interaction is real.
- Ensembl-projected mouse (P20060) terms: single fertilization (GO:0007338), cortical
  granule (GO:0060473), regulation of cell shape (GO:0008360), astrocyte cell migration
  (GO:0043615), positive regulation of transcription by RNA pol II (GO:0045944). The
  fertilization/cortical-granule role is documented for mouse Hexb (zona block to
  polyspermy; UniProt FUNCTION By similarity from P20060) → KEEP_AS_NON_CORE. The others
  (cell shape, astrocyte migration, transcription) are weak mouse-projected phenotype
  associations, not molecular functions of the human enzyme → MARK_AS_OVER_ANNOTATED.
- GO:0008375 acetylglucosaminyltransferase activity (IDA PMID:25645918 + ARBA IEA):
  the neutrophil paper describes HEXA/HexB TRIMMING N-glycans (a hydrolase/glycosidase
  making paucimannose), not a transferase. Transferase MF is almost certainly wrong for a
  GH20 exo-glycosidase → MARK_AS_OVER_ANNOTATED (do not REMOVE experimental IDA per policy;
  it is a plausible mis-typing of the glycosidase activity).
- GO:0016020 membrane (HDA, NK cells) and GO:0070062 extracellular exosome (HDA) and
  GO:0042582 azurophil granule / GO:0035578 azurophil granule lumen / GO:0005576
  extracellular region: these reflect the secreted/granule pool of a mannose-6-phosphate
  lysosomal enzyme that traffics through secretory routes and is found in exosomes /
  neutrophil granules. Real observations but peripheral to core lysosomal catabolism →
  KEEP_AS_NON_CORE (granule/secreted) / MARK_AS_OVER_ANNOTATED (bulk-proteomics membrane).
