# Q9L868 (Q9L868_DESDE) — periplasmic [NiFe] hydrogenase large subunit

## Identity: which protein is this, and whose partner is it?

- Q9L868 is a TrEMBL entry, 543 aa, flagged `Fragment`, derived from EMBL
  `AF216303` (Saraiva, direct submission 1999, "Nucleotide sequence of the gene
  encoding the [NiFe] hydrogenase from Desulfovibrio desulfuricans ATCC 27774").
  The UniProt `OX` line gives the species-level NCBITaxon:876, but the reference
  block of the entry records `STRAIN=ATCC 27774`.
- Checks run during this review (live UniProt/NCBI queries, 2026-10-28):
  - Q9L868 is identical at 542/543 positions (one difference, position 542 T vs V)
    to GenBank `ACL48945.1`, "nickel-dependent hydrogenase large subunit",
    `locus_tag="Ddes_1038"`, 558 aa, from the ATCC 27774 genome `CP001358`. So
    Q9L868 is the truncated 1999 sequence of the genome gene `Ddes_1038`.
  - The same EMBL entry `AF216303` also encodes Q9L869 (266 aa, fragment), which is
    identical at 265/266 positions to the mature chain (50–315) of
    UniProtKB:P13061 (`hydA`, `Ddes_1039`), the Swiss-Prot small subunit reviewed
    in `genes/DESDA/hydA/`.
  - `Ddes_1038` and `Ddes_1039` are adjacent loci.
- Conclusion: **Q9L868 and P13061 are genuine partner subunits of one periplasmic
  [NiFe] hydrogenase from one strain** (ATCC 27774). The two different UniProt taxon
  ids (876 vs 525146) are a record-level artifact of the TrEMBL entry keeping the
  species-level taxon, not evidence of two organisms.
- PDB `1E3D` is the heterodimer of this enzyme at 1.8 Å; Q9L868 maps to chains
  B/D (residues 2–543) [UniProtKB:Q9L868 `DR PDB; 1E3D; X-ray; 1.80 A; B/D=2-543.`].
  The structure paper is PMID:11191224 (its abstract misspells the species as
  "D. desulfitricans"; the strain stated is ATCC 27774).

## Function

This is the catalytic chain. The bimetallic Ni–Fe centre at which H2 is heterolytically
cleaved is built entirely from large-subunit residues, annotated in the entry as Ni(2+)
and Fe-cation ligands at positions 72/75/537/540 plus structural Mg(2+)
[UniProtKB:Q9L868 `FT BINDING 72 /ligand="Ni(2+)"`; `FT BINDING 75 /ligand="Fe cation"`].
The structural work on this enzyme resolves the nickel ligand Cys536 in three rotamers
and reports a partially occupied bridging sulfur, i.e. a partly activated active site
[PMID:11191224 "a three-fold disorder was observed for Cys536 which binds to the nickel atom"].
The electrons released are passed through the iron–sulfur relay of the small subunit to
the tetrahaem cytochrome c3
[PMID:11191224 "its physiological partner, the tetrahaem cytochrome c3 from the same organism"],
which is the reaction GO:0047806 / EC 1.12.2.1 describes.

Localisation: the entry's `SUBCELLULAR LOCATION: Periplasm` is ARBA-derived (an
unvetted prediction, so it is not quoted as support here). The periplasmic location
is instead argued from the partner subunit, whose Tat signal peptide cleavage site was
determined by direct protein sequencing of the purified mature protein
[UniProtKB:P13061 `PTM: Predicted to be exported by the Tat system. The position of the signal peptide cleavage has been experimentally proven.`],
and from the fact that the Tat system exports the folded heterodimer, the large subunit
riding along with the signal-bearing small subunit.

## Annotation calls of note

- `GO:0008901 ferredoxin hydrogenase activity` (InterPro2GO from IPR018194) is removed:
  the live `interpro2go` file maps the [NiFe] large-subunit nickel-binding-site signature
  onto the ferredoxin-linked reaction (EC 1.12.7.2), which is not this enzyme's
  chemistry. Recorded as a `source_defect` against InterPro, with
  `GO:0033748 hydrogenase (acceptor) activity` proposed as the acceptor-agnostic
  replacement for a family-level signature.
- Three `NEW` rows are added, all IC and all narrowly evidenced:
  `GO:0044569 [Ni-Fe] hydrogenase complex` (the heterodimer, crystallised from this
  strain, with this entry mapped to PDB chains B/D), `GO:0005506 iron ion binding`
  (the Fe of the bimetallic centre, with curated ligand-binding positions in the entry)
  and `GO:0000287 magnesium ion binding` (the structural Mg(2+), whose ligand
  positions 53/489/543 carry structure-derived evidence from PDB 1E3D as well as the
  PIRSR rule).
  No new biological-process term (e.g. `GO:0009061 anaerobic respiration`) is
  proposed for this chain. The reason is evidential, not that the partner subunit
  already carries it (annotations are per gene product): the available evidence
  for this enzyme is structural and docking-based, and there is no chain-specific
  experimental evidence (mutant, physiological or in vivo electron-flow data) for
  this subunit's role in the respiratory process, so a `NEW` process row is withheld
  under the conservative policy for process terms.

## Relation to the CMMMech record (`data/records/palladium.yaml`)

CMMMech cites Q9L868 as "Catalytic Ni-Fe active-site large subunit of periplasmic
[NiFe] cytochrome-c3 hydrogenase (EC 1.12.2.1) in Desulfovibrio desulfuricans", which
this review supports. Two notes (CMMMech is not edited here):

1. The record's `target_organism` for Q9L868 is the species-level NCBITaxon:876, mirroring
   UniProt, which obscures that this sequence is from ATCC 27774 — the same strain as the
   P13061 small subunit. The two protein examples are operon partners (`Ddes_1038`/
   `Ddes_1039`), which strengthens the record's "periplasmic [NiFe] hydrogenase system"
   framing beyond what it currently claims.
2. The record does not note that Q9L868 is a sequence **fragment** (543 of 558 aa);
   the complete large subunit is `Ddes_1038` / GenBank `ACL48945.1`, which has no
   UniProtKB accession of its own.

The Pd(II)-reduction evidence remains indirect for this subunit: Lloyd et al. used strain
ATCC 29577 and inferred hydrogenase involvement from H2 dependence and Cu2+ pretreatment
[PMID:9797331 "the lack of molecular genetic studies on D. desulfuricans makes confirmation with specific deletion mutants difficult, but the involvement of hydrogenase activity is strongly implicated"],
and the mutant work is in a different species
[PMID:18689514 "Wild-type Desulfovibrio fructosivorans and three hydrogenase-negative mutants reduced Pd(II) to Pd(0)."].
No metal-reduction GO annotation is proposed on that basis.

## Tooling note

The reference validator strips some square-bracketed strings from quotations as
editorial notes: a `supporting_text` containing `[NiFe]` fails to match the cached
publication, although `[4Fe-4S]` and `[cytochrome c3]` match. Quotes here were chosen
to avoid `[NiFe]`.
