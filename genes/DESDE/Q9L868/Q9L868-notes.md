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
    Q9L868 is the 1999 sequence of the genome gene `Ddes_1038`, 15 residues shorter at
    the C terminus. Those 15 residues are most likely the maturation propeptide rather
    than an unsequenced remainder — see the discussion under "Relation to the CMMMech
    record", point 2.
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
cleaved is built entirely from large-subunit residues. The entry's `FT BINDING` features
annotate, exactly, **Ni(2+) at 72, 75 and 537**, **Fe cation at 75 and 540**, and
structural **Mg(2+) at 53, 489 and 543**
[UniProtKB:Q9L868 `FT BINDING 72 /ligand="Ni(2+)"`; `FT BINDING 75 /ligand="Fe cation"`;
`FT BINDING 537 /ligand="Ni(2+)"`; `FT BINDING 540 /ligand="Fe cation"`].
The four cysteines are 72 and 75 (the N-terminal CxxC) and 537 and 540 (the C-terminal
DPCxxC); in the canonical [NiFe] large-subunit architecture all four coordinate the
nickel, and 75 and 540 are the **bridging** pair shared between the nickel and the iron.
Note therefore that **540 is not annotated as a Ni(2+) ligand in this entry** even though
it is one on the biology: the reviewed Desulfovibrio-lineage homologues do annotate it,
and this entry's PIRSR-derived set is incomplete at that position (checks run live
against UniProt REST, 2026-10-28):

- `UniProtKB:P12944` (*Megalodesulfovibrio gigas* periplasmic [NiFe] hydrogenase large
  subunit) annotates `FT BINDING 65/68/530/533 /ligand="Ni(2+)"` — all four cysteines.
- `UniProtKB:P21852` (*Nitratidesulfovibrio vulgaris* Miyazaki F) annotates
  `FT BINDING 81/84/546/549 /ligand="Ni(2+)"` **and** `FT BINDING 84/549 /ligand="Fe cation"`
  — i.e. the same Fe pair as here, but with the fourth cysteine also typed as a Ni ligand.
  Its positions 81/84/546/549 correspond to 72/75/537/540 of Q9L868, so the position
  missing a `Ni(2+)` feature here is exactly the one P21852 annotates at 549.

A UniProt record defect follows from this (missing `FT BINDING 540 /ligand="Ni(2+)"`); it
is recorded here rather than as a `source_defects` entry because it is a missing sequence
feature rather than a defect in any GO annotation row under review.

The two `FT DISULFID` features pair the same four cysteines across the two motifs —
`DISULFID 72..537` and `DISULFID 75..540`, both `ECO:0007829|PDB:1E3D`, i.e. automatic
annotation derived from the deposited coordinates. They pair each N-terminal cysteine
with its C-terminal partner, which is the geometry imposed by both pairs clamping the
shared Ni–Fe centre; neither P12944 nor P21852 carries any `DISULFID` feature at the
equivalent positions, where the same cysteines are typed as metal ligands. The features
should therefore be read as the structure-derived proximity of the active-site cysteines,
not as disulfide bonds in the metallated holoenzyme.
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
2. The record does not note that Q9L868 is flagged a sequence **fragment** (543 aa against
   the 558 aa of `Ddes_1038` / GenBank `ACL48945.1`, which has no UniProtKB accession of
   its own). This is a record-keeping point, and probably one about **precursor versus
   mature chain** rather than about an incompletely known protein — so it does not weaken
   the record's use of Q9L868 as the catalytic subunit. [NiFe] hydrogenase large subunits
   are synthesised as precursors whose C-terminal propeptide is removed by a HycI/HybD-type
   endopeptidase that cuts immediately after the His of the conserved `DPCxxCxxH` motif,
   and four independent things line up with Q9L868 already being the mature chain (checks
   run live against UniProt REST and NCBI efetch, 2026-10-28):

   - Q9L868 ends `...IHSFDPCIACSTH` at position 543 — exactly at that motif His, with the
     Ni/Fe-ligating Cys537 and Cys540 inside the motif
     [UniProtKB:Q9L868 `SQ SEQUENCE   543 AA`].
   - **His543, the final residue, is an annotated `Mg(2+)` ligand with structure-derived
     evidence** [UniProtKB:Q9L868 `FT BINDING 543 /ligand="Mg(2+)" /evidence="ECO:0000256|PIRSR:PIRSR601501-1, ECO:0007829|PDB:1E3D"`].
     The structural Mg site of these subunits is ligated by the C-terminal His of the
     *mature* chain: `UniProtKB:P21852` annotates `CHAIN 1..552` with `FT BINDING 552
     /ligand="Mg(2+)"`, its last mature residue. A sequencing truncation would not stop at
     a structurally liganded C-terminus.
   - `1E3D` chains B/D cover residues 2–543, the whole of what UniProt has, with nothing
     unmodelled at either end.
   - The 15 residues by which `ACL48945.1` exceeds this entry are `VIDGESNEVHDYKVL`
     (positions 544–558), and they align to curated propeptides of the same length and
     position: `UniProtKB:P0ACE0` (*E. coli* hydrogenase-2 large chain) has
     `CHAIN 2..552` / `PROPEP 553..567 /note="Cleavage; by HybD"`, whose mature chain ends
     `...IHSFDPCMACAVH` and whose 15-residue propeptide is `VVDADGNEVVSVKVL`;
     `UniProtKB:P12944` has `CHAIN 2..536` / `PROPEP 537..551`, also 15 residues.

   So the likeliest reading is that `ACL48945.1` is the full-length precursor and Q9L868's
   543 residues are the mature subunit, the species actually crystallised. The entry's own
   `Flags: Fragment` and `FT NON_TER 543 /evidence="ECO:0000313|EMBL:AAF43138.1"` say only
   that the 1999 EMBL CDS `AAF43138.1` was submitted as non-terminal; they are not evidence
   that the protein continues past 543 *in the mature form*. This has not been confirmed
   experimentally for this enzyme (no `PROPEP` or `CHAIN` feature exists on either
   sequence), so it is recorded here and raised as a `suggested_question` rather than
   asserted in the review body.

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
