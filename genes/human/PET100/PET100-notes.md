# PET100 (Protein PET100 homolog, mitochondrial) — curation notes

UniProt: P0DJ07 (PT100_HUMAN). HGNC:40038. Synonym C19orf79. 73 aa precursor,
single-pass membrane protein with an N-terminal mitochondrial transit peptide and a
predicted transmembrane helix (residues 7–24). Belongs to the PET100 family
(Pfam PF09803, InterPro IPR018625).

Note: no falcon deep-research file was generated (falcon out of credits, 402); these
notes are grounded in the cached UniProt record, the seeded GOA, and cached
publications PMID:22356826 and PMID:24462369 (PMID:25293719 not cached — abstract
content taken only from the UniProt reference block, not quoted as supporting_text).

## Function

PET100 is a small mitochondrial inner-membrane assembly chaperone specific to
Complex IV (cytochrome c oxidase, COX). It is non-catalytic and acts as a
COX-specific assembly factor.

- UniProt FUNCTION: "Plays an essential role in mitochondrial complex IV maturation and
  assembly." [ECO:0000269|PubMed:24462369, ECO:0000269|PubMed:25293719]
- PET100 was predicted as the human ortholog of S. cerevisiae Pet100p, a COX assembly
  factor, by Ortho-Profile [PMID:22356826]. In yeast Pet100p is a COX-specific chaperone
  that promotes incorporation of the early nuclear-encoded subunits (Cox7p/Cox7ap,
  Cox8p and related) into an early assembly intermediate; the human protein retains the
  conserved interaction with the COX subunit VIIa (COX7A2).
- PMID:22356826 (full text) TAP-MS: "The subunit VIIa of COX (encoded by the COX7A2
  gene) was specifically co-purified with PET100, corroborating the conserved
  interaction of fungal Pet100p-subunit VIIa that takes place in the inner mitochondrial
  membrane of yeast." → UniProt SUBUNIT: "Interacts with COX7A2."
- PMID:24462369 established the human disease role and showed PET100 "is located in the
  mitochondrial inner membrane and forms a ∼300 kDa subcomplex with complex IV subunits"
  — i.e. an early COX assembly intermediate.

Core BP = mitochondrial respiratory chain complex IV assembly (GO:0033617).
Location = mitochondrial inner membrane (GO:0005743).

## Molecular function

No informative catalytic MF. GOA carries only IBA "protein folding chaperone"
(GO:0044183) and the IEA-derived "protein folding" (GO:0006457). PET100 is a
scaffolding/assembly chaperone, not a bona fide protein-folding chaperone; there is no
experimental evidence it catalyses protein folding. UniProt DR lists the IBA MF as
GO:0051082 "unfolded protein binding" (i.e. the PAN-GO MF is binding, not folding). Per
policy, do NOT invent a catalytic MF; core_functions omits `molecular_function`
(analogous to COX14, COA3). The chaperone terms are marked as over-annotated rather than
removed (IBA, extensively reviewed; not obviously wrong, but over-interpreted as
protein-folding activity).

## Disease

Mitochondrial complex IV deficiency, nuclear type 12 (MC4DN12; MIM:619055), autosomal
recessive, onset in early infancy: poor growth, metabolic/lactic acidosis, profoundly
delayed psychomotor development, seizures, hypotonia, brain abnormalities (Leigh
syndrome), decreased COX levels/activity. Founder c.3G>C (p.Met1?) mutation in Lebanese
individuals [PMID:24462369]; truncating variant p.(48-73 del) causing fatal infantile
lactic acidosis [PMID:25293719, per UniProt].

## Annotation review summary

- GO:0005743 mitochondrial inner membrane (IBA is_active_in; IEA located_in; EXP
  located_in PMID:24462369): ACCEPT — core location, experimentally established.
- GO:0033617 complex IV assembly (IBA involved_in; IEA involved_in): ACCEPT — core BP.
- GO:0044183 protein folding chaperone (IBA enables): MARK_AS_OVER_ANNOTATED — assembly
  chaperone, not a folding chaperone; no folding-catalysis evidence.
- GO:0051131 chaperone-mediated protein complex assembly (IBA involved_in): ACCEPT /
  keep — reasonable characterization of assembly-chaperone activity, consistent with
  promoting subunit incorporation into COX. (Marked ACCEPT as non-core-adjacent BP that
  is a valid, more mechanism-flavored companion to GO:0033617.)
- GO:0006457 protein folding (IEA, inter-ontology link from GO:0044183): MARK_AS_OVER_
  ANNOTATED — inherits the over-interpretation of the folding-chaperone term.
- GO:0005739 mitochondrion (IEA; HTP PMID:34800366): ACCEPT — correct but general parent
  of the inner-membrane location.
- GO:0016020 membrane (IEA located_in, SubCell single-pass membrane): MARK_AS_OVER_
  ANNOTATED — uninformative root-level location; GO:0005743 is the specific term.
</content>
