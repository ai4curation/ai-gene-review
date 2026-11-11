# hydA (P13061, PHNS_DESDA) — periplasmic [NiFe] hydrogenase small subunit

## Identity and partner subunit

- P13061 (`PHNS_DESDA`, Swiss-Prot) is the small (beta) subunit of the periplasmic
  [NiFe] hydrogenase of *Desulfovibrio desulfuricans* ATCC 27774 / DSM 6949 / MB
  (NCBITaxon:525146), locus `Ddes_1039`, 315 aa precursor with a Tat signal peptide
  (1–49) and mature chain 50–315 [UniProtKB:P13061 `FT SIGNAL 1..49 /note="Tat-type signal"`].
- The large (alpha) catalytic subunit reviewed alongside it is
  UniProtKB:Q9L868 (`Q9L868_DESDE`, TrEMBL, `genes/DESDE/Q9L868/`).

**Are they genuine partners?** Yes, despite carrying different UniProt taxon ids.
Checks performed in this review (live UniProt/NCBI queries, 2026-10-28):

- Q9L868 derives from EMBL `AF216303` (Saraiva, 1999), whose UniProt reference
  block records `STRAIN=ATCC 27774`, although the entry's `OX` line is the
  species-level NCBITaxon:876 rather than the strain taxon 525146. The apparent
  "two strains" split is a record-level artifact, not a biological one.
- `AF216303` also encodes Q9L869 (266 aa, "cytochrome-c3 hydrogenase", fragment).
  Its sequence is identical to the P13061 mature chain (residues 50–315) at
  265/266 positions (single difference R→S at mature position 5). So Q9L869 and
  P13061 are the same gene product from the same strain, sequenced twice.
- Q9L868 (543 aa, Flags: Fragment) is identical at 542/543 positions to
  GenBank `ACL48945.1` ("nickel-dependent hydrogenase large subunit",
  `locus_tag="Ddes_1038"`, 558 aa) from the ATCC 27774 genome `CP001358`.
  `Ddes_1038` is immediately adjacent to `Ddes_1039` (= hydA), i.e. the two
  reviewed accessions are the large and small subunits of one operon in one strain.
- PDB `1E3D` is the heterodimeric enzyme from this strain; Q9L868 maps to chains
  B/D (residues 2–543) [UniProtKB:Q9L868 `DR PDB; 1E3D; X-ray; 1.80 A; B/D=2-543.`].
  The structure paper is [PMID:11191224 "The primary and three-dimensional structures of a [NiFe] hydrogenase isolated from D. desulfitricans ATCC 27774 were determined, by nucleotide analysis and single-crystal X-ray crystallography."]
  (the species is misspelled in the published abstract).

## Function

The division of labour in [NiFe] hydrogenases is well established and is visible
in the two records themselves: the bimetallic Ni–Fe catalytic centre is carried
by the **large** subunit (Q9L868 `FT BINDING` residues for Ni(2+) and Fe cation),
while the **small** subunit carries the iron–sulfur relay — two [4Fe-4S] clusters
and one [3Fe-4S] cluster — that conducts electrons between the active site and
the external redox partner
[UniProtKB:P13061 `COFACTOR: Name=[4Fe-4S] cluster ... Note=Binds 2 [4Fe-4S] clusters.`;
`COFACTOR: Name=[3Fe-4S] cluster ... Note=Binds 1 [3Fe-4S] cluster.`].
The structural work on this very enzyme shows the cluster chain running up to the
[NiFe] centre [PMID:11191224 "the [4Fe-4S] cluster nearest the [NiFe] centre has been modified [4Fe-3S-3O] by loss of one sulfur atom and inclusion of three oxygen atoms"]
and identifies the physiological acceptor as the tetrahaem cytochrome c3, docking
at the **distal [4Fe-4S] cluster of the small subunit**
[PMID:11191224 "The lowest energy docking solutions were found to correspond to an interaction between the haem IV region in tetrahaem cytochrome c3 with the distal [4Fe-4S] cluster in [NiFe] hydrogenase."].

Therefore, for the small subunit:

- `GO:0009055 electron transfer activity` is its own molecular function, not a
  merely structural role; it is accepted here as the core MF.
- `GO:0047806 cytochrome-c3 hydrogenase activity` (EC 1.12.2.1, the whole-enzyme
  reaction) is retained but marked as an over-annotation of an individual chain,
  following the repository's subunit precedent (`genes/PSEPK/ureA`): the small
  subunit contributes to, rather than independently enables, the holoenzyme
  activity. It is recorded as `contributes_to_molecular_function` in `core_functions`.
- The protein is a soluble, Tat-exported periplasmic protein
  [UniProtKB:P13061 "SUBCELLULAR LOCATION: Periplasm."; `PTM: Predicted to be exported by the Tat system.`];
  it has no transmembrane segment and the holoenzyme was crystallised as a soluble
  heterodimer. The TreeGrafter `GO:0016020 membrane` row is over-propagation from
  membrane-anchored relatives (e.g. *E. coli* Hyd-1/Hyd-2 small subunits, which
  carry a C-terminal membrane anchor this protein lacks) and is removed.

## InterPro2GO defects (recorded as `source_defects`)

The live `interpro2go` file maps the two [NiFe] hydrogenase signatures onto
ferredoxin-specific terms:

```
InterPro:IPR001821 [NiFe]-hydrogenase, small subunit > GO:ferredoxin hydrogenase activity ; GO:0008901
InterPro:IPR001821 [NiFe]-hydrogenase, small subunit > GO:ferredoxin hydrogenase complex ; GO:0009375
InterPro:IPR018194 Nickel-dependent hydrogenase, large subunit, nickel binding site > GO:ferredoxin hydrogenase activity ; GO:0008901
```

`GO:0008901` is defined as "Catalysis of the reaction: 2 reduced ferredoxin + 2 H+
= 2 oxidized ferredoxin + H2" (the [FeFe]/ferredoxin reaction, EC 1.12.7.2), and
`GO:0009375 ferredoxin hydrogenase complex` is an intracellular complex term.
Neither fits a periplasmic cytochrome-c3-linked [NiFe] enzyme (EC 1.12.2.1).
Suggested repointing: `GO:0033748 hydrogenase (acceptor) activity` (acceptor-agnostic,
suitable for a family-level signature) and `GO:0044569 [Ni-Fe] hydrogenase complex`.

## Relation to the CMMMech record (`data/records/palladium.yaml`)

CMMMech grounds the palladium mechanism in *D. desulfuricans* to this pair of
accessions. Two points where the CMMMech text is stronger or looser than the
evidence supports (noted here only; CMMMech is not edited by this review):

1. The `functional_role` for P13061 reads "…small iron-sulfur subunit (EC 1.12.2.1;
   HydA / Ddes_1039) **mediating H2 oxidation** and periplasmic electron transfer".
   H2 oxidation chemistry happens at the Ni–Fe site of the **large** subunit; the
   small subunit mediates the electron transfer half of that sentence. The EC number
   properly belongs to the holoenzyme.
2. The Q9L868 entry is given `target_organism: NCBITaxon:876` (species level), which
   mirrors UniProt but obscures that the sequence is from ATCC 27774 — the same
   strain as P13061. The two protein examples are operon partners (`Ddes_1038`/
   `Ddes_1039`), which is stronger support for the "periplasmic [NiFe] hydrogenase
   system" claim than the record currently states.

The Pd(II)-reduction evidence itself remains indirect for either subunit:
Lloyd et al. used *D. desulfuricans* ATCC 29577 (a different strain) and inferred
hydrogenase involvement from H2 dependence and Cu2+ pretreatment, explicitly noting
that no deletion mutants were available
[PMID:9797331 "the lack of molecular genetic studies on D. desulfuricans makes confirmation with specific deletion mutants difficult, but the involvement of hydrogenase activity is strongly implicated"],
and Mikheenko et al. worked in *D. fructosivorans*
[PMID:18689514 "Wild-type Desulfovibrio fructosivorans and three hydrogenase-negative mutants reduced Pd(II) to Pd(0)."].
No GO annotation of metal (Pd/U/Tc) reduction is proposed for either subunit here:
no experiment localises Pd(II) reduction to this enzyme, and a hydrogenase reducing
a soluble metal ion non-specifically is not evidence that it executes a
characterised biological process.
