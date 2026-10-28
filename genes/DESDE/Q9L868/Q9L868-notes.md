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
DPCxxC). That all four coordinate the nickel, and that 75 and 540 are the **bridging**
pair shared between the nickel and the iron, is not merely the canonical architecture or
UniProt's own feature typing: the deposited coordinates of this enzyme show it. In the
current `1E3D` file each of the four cysteine sulfurs lies 2.17–2.62 Å from the cluster
nickel in both large-subunit chains, and only two of them — the counterparts of 75 and 540
— are also within bonding distance of the iron (2.28–2.32 Å, against 4.5–4.9 Å for the
other two) (see "The entry's two DISULFID features contradict its own metal assignment",
below, for the measurements, the numbering offset, and why the file's own `LINK` records
are an index to them rather than the evidence).
Note therefore that **540 is not annotated as a Ni(2+) ligand in this entry** even though
the structure UniProt already cites for this entry records a nickel–sulfur bond there, and
even though the reviewed Desulfovibrio-lineage homologues annotate the equivalent position:
this entry's PIRSR-derived set is incomplete at position 540 (checks run live
against UniProt REST, 2026-10-28):

- `UniProtKB:P12944` (*Megalodesulfovibrio gigas* periplasmic [NiFe] hydrogenase large
  subunit) annotates `FT BINDING 65/68/530/533 /ligand="Ni(2+)"` — all four cysteines.
- `UniProtKB:P21852` (*Nitratidesulfovibrio vulgaris* Miyazaki F) annotates
  `FT BINDING 81/84/546/549 /ligand="Ni(2+)"` **and** `FT BINDING 84/549 /ligand="Fe cation"`
  — i.e. the same Fe pair as here, but with the fourth cysteine also typed as a Ni ligand.
  Its positions 81/84/546/549 correspond to 72/75/537/540 of Q9L868, so the position
  missing a `Ni(2+)` feature here is exactly the one P21852 annotates at 549.

A UniProt record defect follows from this (missing `FT BINDING 540 /ligand="Ni(2+)"`). It is
recorded as a `source_defects` entry on the `GO:0016151 nickel cation binding` row, which is
the annotation whose claim the incomplete ligand set under-supports: `resource: UNIPROT`,
`record: UniProtKB:Q9L868`, `slot: FT BINDING`, `requested_change: ADD`,
`confidence: CONFIRMED`. The warrant is this entry's own cited structure, not the
comparative argument: the author-deposited `1E3D` coordinates put the sulfur of every one
of the four cysteines within 2.17–2.62 Å of the cluster nickel in both large-subunit
chains, position 540 (PDB 539) among them at 2.53 Å and 2.51 Å. So the structure UniProt
already cites records a nickel–sulfur bond at exactly the position that carries no `Ni(2+)`
feature, and the homologue annotations above corroborate that rather than carry it. Filing
it on that row is what gets it into `just export-source-defects`' report for UniProt. Two
further defects, one per contradicted `DISULFID` feature, are filed on the same row — see
"The entry's two DISULFID features contradict its own metal assignment", below.

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
     `UniProtKB:P12944` has `CHAIN 2..536` / `PROPEP 537..551`, also 15 residues;
     and `UniProtKB:P21852` has `CHAIN 1..552` / `PROPEP 553..567
     /id="PRO_0000013406"`, again 15 residues, on a 567-residue precursor. So all
     three reviewed orthologues of this subunit annotate a C-terminal propeptide
     of exactly this length.
   - **The P21852 correspondence holds for the full precursor, not only for the
     annotated features.** The P21852-to-Q9L868 offset of 9 that aligns all seven
     annotated metal positions (81/84/546/549 against 72/75/537/540, and
     62/498/552 against 53/489/543) also predicts the precursor length and the
     propeptide boundaries: 567 - 9 = 558, which is exactly the length of
     `ACL48945.1` [GenBank:ACL48945.1 `LOCUS       ACL48945                 558 aa`],
     and P21852's `PROPEP 553..567` maps onto 544-558, exactly the 15 residues by
     which `ACL48945.1` exceeds this entry. The offset was derived from the metal
     features alone, so the precursor length and the propeptide boundaries are
     predictions it makes rather than inputs to it.

   So the likeliest reading is that `ACL48945.1` is the full-length precursor and Q9L868's
   543 residues are the mature subunit, the species actually crystallised. The entry's own
   `Flags: Fragment` and `FT NON_TER 543 /evidence="ECO:0000313|EMBL:AAF43138.1"` say only
   that the 1999 EMBL CDS `AAF43138.1` was submitted as non-terminal; they are not evidence
   that the protein continues past 543 *in the mature form*. This has not been confirmed
   experimentally for this enzyme (no `PROPEP` or `CHAIN` feature exists on either
   sequence), so it is recorded here and raised as a `suggested_question` rather than
   asserted in the review body.

## The entry's two DISULFID features contradict its own metal assignment

Q9L868 carries `FT DISULFID 72..537` and `FT DISULFID 75..540`, both with evidence
`ECO:0007829|PDB:1E3D` — automatic annotation derived from the deposited coordinates — over
the same four cysteines the entry types as Ni-Fe cluster ligands. Each feature pairs an
N-terminal cysteine with its C-terminal partner, which is the geometry imposed by both pairs
clamping the shared Ni–Fe centre, not the geometry of a disulfide bond. The metal assignment
and the disulfides cannot both hold in one conformer. Checks run live on 2026-10-28:

- **The author-deposited coordinates are what settle it, and they are measurements, not
  annotations.** Taken straight from the `ATOM`/`HETATM` records of the current `1E3D` file
  (files.rcsb.org, revision 2.4 of 2026-09-02), each of the four cysteine sulfurs lies
  2.17–2.62 Å from the cluster nickel in both large-subunit chains (chain B: 71 at 2.17 Å,
  74 at 2.58 Å, 536 major rotamer at 2.20 Å, 539 at 2.53 Å; chain D: 2.20, 2.62, 2.19,
  2.51 Å), with 74 and 539 additionally 2.28–2.32 Å from the iron, while 71 and 536 are
  4.5–4.9 Å from it. The two pairs the entry calls disulfides are 2.87 Å and 2.95 Å apart in
  chain B (72/537 at the major rotamer of 537) and 2.96 Å and 2.95 Å in chain D — short,
  because the sulfurs clamp a single metal centre, but well above the roughly 2.05 Å of a
  real disulfide. PDB numbering here is one lower than UniProt's, so these are Q9L868's 72,
  75, 537 and 540. Every sulfur is at bonding distance from the nickel and no pair is at
  bonding distance from its partner.
- The file's derived records agree, and are a convenient index to the measurements rather
  than the evidence for them: there is **no `SSBOND` record** at all, and the `LINK` records
  bond every one of the four SG atoms to the nickel. They are not independent of the
  problem, though — `REVDAT 7` records revision 2.4 as changing `REMARK`, `SSBOND` **and**
  `LINK` together, and the RCSB revision history classes that revision under "Derived
  calculations", so `LINK` is the same class of automatic output whose earlier generation
  most likely produced the stale `DISULFID` features. That is why the argument above is
  made from the coordinates. The provenance reading is an inference, not something either
  resource states.
- The entry's own reference block corroborates that provenance reading. The `RP` scope for
  PMID:11191224 reads `X-RAY CRYSTALLOGRAPHY (1.80 ANGSTROMS) OF 2-543 IN COMPLEX WITH
  MG(2+), AND DISULFIDE BONDS.` — it names the Mg(2+) and the disulfides and **does not
  mention the Ni-Fe cluster at all**, although that is the structure's defining feature.
  Those are exactly the features carrying `ECO:0007829|PDB:1E3D` (the three Mg(2+) sites at
  53/489/543 and the two disulfides); every Ni and Fe feature is PIRSR-only
  (`ECO:0000256|PIRSR:PIRSR601501-1`). So the scope line appears to have been generated from
  the PDB-derived feature set, and inherits its error. If both `DISULFID` features go, that
  scope goes stale with them. For contrast, the reviewed `UniProtKB:P21852` describes its own
  1.8 Å structure as `X-RAY CRYSTALLOGRAPHY (1.8 ANGSTROMS) OF 19-552, AND COFACTOR.`
- None of the three reviewed orthologues carries any `DISULFID` feature at the equivalent
  positions, where the same cysteines are typed as metal ligands instead: `UniProtKB:P21852`,
  `UniProtKB:P12944` and `UniProtKB:P0ACE0` have no `DISULFID` feature between them, and no
  occurrence of "DISULFIDE BOND" in any `RP` scope either.

Q9L868 is `Unreviewed`, so it has had no curator pass over the automatic features. Three
defects are filed as `source_defects` on the `GO:0016151` row: the missing
`BINDING 540 /ligand="Ni(2+)"` (`requested_change: ADD`) and one `DELETE_VALUE` per
contradicted feature, `DISULFID 72..537` and `DISULFID 75..540` separately. They are split
because `report_status` is per entry and `just export-source-defects` keys rows on
`asserted_value`, so a bundled pair could not record UniProt removing one feature and
keeping the other; the two entries share their reasoning and differ only in the value asked
to be removed. The request is removal, not reinterpretation: the features assert bonds the
cited structure does not contain.

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
