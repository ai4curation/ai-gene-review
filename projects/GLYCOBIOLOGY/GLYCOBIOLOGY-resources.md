# Glycoscience Resources Dossier

Supporting material for the [Glycobiology Project](../GLYCOBIOLOGY.md). A working
catalogue of external glycobiology databases, ontologies, and tools, with notes
on what each holds, its identifier scheme, and how it could feed or cross-check
GO-based curation of animal glycogenes.

## The GlySpace Alliance

The [GlySpace Alliance](https://pmc.ncbi.nlm.nih.gov/articles/PMC9875223/) is the
coordinating umbrella for the three major glycoinformatics integration projects.
Their shared goal is to provide trustable, quality information on biologically
relevant glycan structures, the glycoconjugates that carry them, their
biosynthesis/regulation, and their biological roles. They interoperate primarily
through the shared **GlyTouCan** glycan-structure identifier space.

| Project | Region | One-line scope |
|---------|--------|----------------|
| GlyGen | US | glycoprotein- and glycan-centric data integration + APIs |
| Glyco@Expasy | EU (SIB) | curated tools/databases incl. GlyConnect |
| GlyCosmos | JP | glycan-centric integration with omics; official JSCR portal |

## Core databases

### GlyGen — https://www.glygen.org/
- **Type:** integrating data portal for carbohydrate and glycoconjugate data.
- **Content:** harmonises glycoprotein-centric and glycan-centric data from
  GlyConnect, UniCarbKB, GlyTouCan, MatrixDB, UniProt, CAZy, and others.
- **Access:** machine-readable REST APIs **and** a SPARQL endpoint — the most
  programmatically convenient cross-reference hub for a curation pipeline.
- **Curation role:** one-stop lookup to pull, for a given UniProt accession, its
  known glycosylation sites, attached glycan structures (GlyTouCan IDs), and the
  biosynthetic enzymes — evidence to corroborate or challenge a GO annotation.

### GlyTouCan — https://glytoucan.org/
- **Type:** international glycan-structure **repository** (the structure-ID
  registry).
- **Content:** registered glycan structures, each issued a stable accession after
  validation; partner databases auto-link their data to these IDs.
- **Curation role:** the canonical identifier backbone — lets site/structure
  evidence from different resources be reconciled to one glycan.

### GlyCosmos — https://glycosmos.org/
- **Type:** web portal integrating glycoscience with the broader life sciences;
  official portal of the Japanese Society for Carbohydrate Research (JSCR).
- **Content:** glycans, glycogenes, glycoproteins, glycolipids, pathways,
  diseases; provides RDF/semantic-web representations.
- **Curation role:** gene→disease→pathway context and an alternative integrated
  view; RDF eases joining to GO.

### GlyConnect / Glyco@Expasy — https://www.expasy.org/glycomics
- **Type:** curated database of glycan structures, glycosylation **sites** on
  proteins, and the **enzymes** involved in glycan biosynthesis/modification
  (part of the SIB Glyco@Expasy suite).
- **Curation role:** the enzyme↔glycan↔site links are exactly the evidence needed
  to judge whether a glycosyltransferase/glycosidase MF (and its associated BP)
  annotation is supported, too generic, or missing.

### UniCarbKB — https://unicarbkb.org/
- **Type:** curated knowledge base of glycan structures and glycoprotein
  attachment sites, with literature provenance.
- **Curation role:** site-level glycosylation evidence with citations — directly
  usable to support `protein N-/O-linked glycosylation` annotations.

### CAZy — http://www.cazy.org/
- **Type:** expert sequence-family classification of **carbohydrate-active
  enzymes**: glycosyltransferases (GT), glycoside hydrolases (GH), polysaccharide
  lyases (PL), carbohydrate esterases (CE), and carbohydrate-binding modules
  (CBM). GTs alone span >90 families (~41% of CAZy).
- **Curation role:** an independent, sequence-grounded check on MF annotation —
  family membership predicts the broad activity class (GT → transferase, GH →
  hydrolase), useful for flagging wrong-class or wrong-specificity annotations in
  large paralogous families. (See also the repo's [INTERPRO](../INTERPRO.md) /
  [PFAM](../PFAM.md) family-audit projects for the analogous pattern.)

## Ontologies and standards

### GlycoCoO — GlycoConjugate Ontology — https://github.com/glycoinfo/GlycoCoO
- A standard semantic framework for describing glycoconjugate data
  (glycoprotein/glycolipid structures, biological source, experimental data, and
  provenance), published in *Glycobiology* (PMID:33677548).
- **Curation role:** the alignment/interoperability target — if GlycoCoO classes
  map cleanly to GO terms, specialist glyco annotations could be cross-validated
  against, or imported into, the GO framework.

### Other community standards
- **WURCS / GlycoCT** — glycan structure encoding formats (WURCS is the
  GlyTouCan-canonical line notation).
- **SNFG** — Symbol Nomenclature for Glycans (the standard pictorial vocabulary).

## How this feeds the GO-usage audit

1. **Enumerate** the animal glycogene set from GOA via closure under the anchor
   GO terms listed on the [project page](../GLYCOBIOLOGY.md).
2. **Cross-reference** each gene through GlyGen (API/SPARQL) to pull
   GlyConnect/UniCarbKB site+structure evidence and CAZy family.
3. **Compare** the GO annotation against (a) CAZy family (activity-class sanity
   check) and (b) GlyConnect enzyme records (specificity check), flagging
   over-/under-/mis-annotation.
4. **Gap-find** glyco facts present in the specialist resources but absent from
   GO → `proposed_new_terms` candidates (mirrors the [RHEA](../RHEA.md) reverse-gap
   method).

## Sources

- Worldwide Glycoscience Informatics Infrastructure: The GlySpace Alliance — https://pmc.ncbi.nlm.nih.gov/articles/PMC9875223/
- Databases and Bioinformatic Tools for Glycobiology and Glycoproteomics — https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7556027/
- Glycoinformatics — Essentials of Glycobiology (NCBI Bookshelf) — https://www.ncbi.nlm.nih.gov/books/NBK579995/
- The CAZy database: an expert resource for Glycogenomics — https://pmc.ncbi.nlm.nih.gov/articles/PMC2686590/
- The glycoconjugate ontology (GlycoCoO) — https://pmc.ncbi.nlm.nih.gov/articles/PMC8351504/ (PMID:33677548)
- Congenital Disorders of Glycosylation — Essentials of Glycobiology — https://www.ncbi.nlm.nih.gov/books/NBK579928/
