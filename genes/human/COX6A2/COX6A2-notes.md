# COX6A2 (Q02221) review notes

## Summary of biology

COX6A2 (cytochrome c oxidase subunit 6A2, mitochondrial; aka COX VIa-heart / COX VIa-muscle)
is the **heart/skeletal-muscle-specific** nuclear-encoded structural (supernumerary) subunit
of mitochondrial respiratory **Complex IV (cytochrome c oxidase, CIV)**. It is a
**non-catalytic** subunit; the catalytic core is the three mtDNA-encoded subunits MT-CO1,
MT-CO2, MT-CO3. COX6A2 is a single-pass inner-membrane protein located at the
monomer–monomer interface, contributing to complex assembly/stability and dimerisation.
COX6A1 is the ubiquitously expressed paralogous isoform.

## Key provenance

- Tissue specificity (heart/muscle-specific): UniProt Q02221 TISSUE SPECIFICITY, from
  PubMed:1327966 and PubMed:31155743. UniProt text:
  "Expressed specifically in heart and muscle (PubMed:31155743). Not detected in brain,
  colon, spleen, kidney, liver, lung and pancreas (PubMed:31155743)."
- Function / assembly-stabilization role and disease: UniProt Q02221 FUNCTION:
  "Plays a role in the assembly and stabilization of complex IV (PubMed:31155743)."
  DISEASE: "Mitochondrial complex IV deficiency, nuclear type 18 (MC4DN18) [MIM:619062]"
  autosomal recessive, muscle-specific; "Patient skeletal muscle shows decreased levels
  and activity of mitochondrial respiratory complex IV." From PubMed:31155743 (Inoue et
  al. 2019, Ann Neurol). NB: this paper is NOT in the publications/ cache.
- Complex IV membership / composition (14 subunits, 3 mtDNA catalytic + 11 nuclear
  supernumerary incl. COX6A1 or COX6A2): UniProt Q02221 SUBUNIT.
- Location — mitochondrial inner membrane, single-pass: UniProt Q02221 SUBCELLULAR
  LOCATION.
- Topology (transit peptide 1-12; TM 25-49; matrix and IMS topo domains): UniProt FT.

## Cached publications reviewed

- PMID:34800366 (Morgenstern et al., quantitative human mitochondrial proteome) — supports
  GO:0005739 mitochondrion (HTP). Verified header/title.
- PMID:9284905 (Hey et al., Cytogenet Cell Genet 1997) — abstract-only; title/abstract are
  entirely about **COX6A1** ("Assignment of COX6A1 to 6p21 and a pseudogene (COX6A1P) to
  1p31.1..."), the paralog, NOT COX6A2. It is cited (ProtInc/PINC, TAS) for the broad BP
  GO:0006091. This is a wrong-gene/uninformative citation for a very general term.

## Reactome entries reviewed

- R-HSA-163214 electron transfer from reduced cyt c to O2, R-HSA-9709406 CO binds COX,
  R-HSA-9865663 final CIV assembly (COX6A binds holo-MT-CO1,2). All localise COX6A2 to the
  mitochondrial inner membrane (TAS). R-HSA-9865663 directly places COX6A among the final
  assembly subunits, consistent with structural/assembly role.

## Annotation decisions (rationale)

- GO:0006123 mito electron transport cyt c to O2 (IBA, involved_in): ACCEPT. Core BP for a
  CIV subunit; matches UniProt FUNCTION.
- GO:0045277 respiratory chain complex IV (IBA part_of; also IEA part_of): ACCEPT both.
  Correct current CC for CIV membership (GO:0005751 is obsolete).
- GO:0030234 enzyme regulator activity (IBA, enables): MODIFY -> GO:0005198 structural
  molecule activity. COX6A2 is a non-catalytic structural/supernumerary subunit; UniProt
  frames its role as assembly/stabilization of the complex, not as an enzyme regulator per
  se. Structural molecule activity is the better-supported MF for a scaffolding subunit.
  (Note there is some literature that COX6A subunits modulate COX activity / H+/e- ratio,
  hence the IBA regulator call; but at the level of THIS human subunit the stronger,
  UniProt-supported characterization is structural. MODIFY, not REMOVE.)
- GO:0005743 mitochondrial inner membrane (IEA, ISS, 3x Reactome TAS, located_in): ACCEPT
  all. Correct anatomical location.
- GO:0006119 oxidative phosphorylation (IEA, involved_in): ACCEPT. UniProt PATHWAY: energy
  metabolism; oxidative phosphorylation. Broad but correct.
- GO:0005739 mitochondrion (HTP, located_in): ACCEPT. Supported by PMID:34800366; broad but
  correct (inner membrane is the specific location).
- GO:0006091 generation of precursor metabolites and energy (TAS, involved_in): the term is
  correct in essence (COX generates energy) but very general, and the cited reference
  PMID:9284905 is about the paralog COX6A1, not COX6A2. MARK_AS_OVER_ANNOTATED (general
  parent of the more specific GO:0006123 already annotated; wrong-gene ProtInc citation).

## core_functions

- MF: GO:0005198 structural molecule activity (contributes_to GO:0004129 cytochrome-c
  oxidase activity).
- BP: directly_involved_in GO:0006123 mitochondrial electron transport, cytochrome c to
  oxygen.
- CC: located_in GO:0005743 mitochondrial inner membrane; in_complex GO:0045277 respiratory
  chain complex IV.
</content>
