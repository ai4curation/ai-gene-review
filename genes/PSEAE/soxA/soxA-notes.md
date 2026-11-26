# soxA (PA5418, Q9HTE6) — review notes

Tier-3 PseudoCAP review, done as part of the four-subunit sarcosine oxidase group
(`soxA`, `soxB`, `soxD`, `soxG`). Group-level evidence and the wrong-reference table are in
`soxB-notes.md`. `soxA` is the richest of the four and carries three separate problems.

## Wrong reference

The `GO:0008115` IMP row cites **PMID:17951384**, which PubMed shows to be
"Gene-specific regulation by a transcript cleavage factor: facilitating promoter escape"
(Hochschild, *J Bacteriol* 2007, DOI 10.1128/JB.01611-07) — a one-author commentary on
transcription, indexed as `Comment`, with no abstract. The intended paper is
**PMID:17951379**. Recorded as `WRONG_REFERENCE`, `CONFIRMED`.

It is worth noting that `soxA` is the **one** sox gene for which the correct paper reports
subunit-resolved data, which makes the misdirection here the costliest of the four:

`[PMID:17951379 "only sarcosine was detected at 9 h in extracts from soxA"]`

The ¹³C NMR flux experiment was done on a `soxA::TnM` mutant, and the paper's conclusion is
stated for `soxA` specifically:
`[PMID:17951379 "is required for conversion of sarcosine to glycine in P. aeruginosa"]`.

## What SoxA is

1005 residues, the large alpha subunit. The record carries no cofactor statement with usable
evidence (the FAD `COFACTOR` and the FAD/Flavoprotein keywords are all `ECO:0000256|ARBA`,
unvetted predictions, so they are not cited), but the domain complement is informative and
`DR` signature lines are valid support for membership:

- `[file:PSEAE/soxA/soxA-uniprot.txt "DR   InterPro; IPR006277; Sarcosine_oxidase_asu."]` —
  a signature specific to the **sarcosine oxidase alpha subunit**.
- `[file:PSEAE/soxA/soxA-uniprot.txt "DR   InterPro; IPR041117; SoxA_A3."]`
- `GCVT_N`, `GcvT_C`, `GcvT/YgfZ_C` (`PF01571`, `PF08669`) — glycine-cleavage-T-protein
  folate-binding domains. In the characterised tetrameric enzymes this is the half that
  handles the one-carbon unit, which is why the alpha subunit has the strongest claim of the
  four to `GO:0046653`.
- `FAD/NAD-binding_dom` (`IPR023753`, `PF07992 Pyr_redox_2`).
- `[file:PSEAE/soxA/soxA-uniprot.txt "DR   InterPro; IPR001041; 2Fe-2S_ferredoxin-type."]`
  plus `IPR042204` and `IPR041854`, and `PF13510 Fer2_4` — a genuine iron-sulfur domain.
- `DE   SubName` from EMBL (`ECO:0000313`), not cited.
- `PE   3: Inferred from homology`. No `FT TRANSMEM`, no membrane keyword — only five
  `DOMAIN` features.

## Problem 1: the L2HGDH node, and why two IBA rows are removed

Both of soxA's IBA rows come from nodes whose donors are **L-2-hydroxyglutarate
dehydrogenase** orthologs, not sarcosine oxidases. The accessions were resolved against the
UniProt REST API, not read from the identifiers:

| accession | entry | organism | location on record |
|---|---|---|---|
| P37339 | LHGD_ECOLI, L-2-hydroxyglutarate dehydrogenase | *E. coli* K12 | Cell inner membrane |
| Q9H9P8 | L2HDH_HUMAN, L-2-hydroxyglutarate dehydrogenase | human | Mitochondrion matrix |
| Q9LES4 | L2HDH_ARATH, L-2-hydroxyglutarate dehydrogenase | *Arabidopsis* | Mitochondrion |

plus `FB:FBgn0032729` and `MGI:MGI:2384968`.

This is not a broken link: PANTHER's own whole-protein HMM assignment for soxA is
`PTHR43104`, whose official name is `L-2-HYDROXYGLUTARATE DEHYDROGENASE, MITOCHONDRIAL`. So
PANTHER genuinely places this protein in the L2HGDH family, and the IBD was placed on that
clade.

The project's IBA rule says a challenge has to argue with the **node placement**, not with a
similarity score, so that is the argument made here:

1. **Architecture.** The L2HGDH donors are single-chain FAD oxidoreductases. SoxA is a
   1005-residue multidomain protein and one subunit of a four-subunit complex. What it shares
   with the donors is one region, the FAD/NAD-binding domain (`IPR023753`); the GcvT
   folate-binding domains and the 2Fe-2S domain have no counterpart in the donors' function.
2. **Target-specific signature.** SoxA carries `IPR006277`, a signature for the sarcosine
   oxidase alpha subunit specifically. A protein assigned to its own subunit family within
   the characterised sarcosine oxidase systems is not inside the L2HGDH functional clade,
   whatever the family name says.
3. **Target-specific evidence.** `soxA` sits in the `soxBDAG` operon, and a `soxA` mutant
   accumulates sarcosine under ¹³C-choline feeding (quoted above). Its function in this
   organism is established and it is not 2-hydroxyglutarate dehydrogenation.

PANTHER family names are frequently dominated by one member — the project rules warn about
exactly this — and `PTHR43104` looks like a case where a broad FAD-oxidoreductase family took
its name and its seeds from the eukaryotic L2HGDH clade.

So:

- **`GO:0047545` (S)-2-hydroxyglutarate dehydrogenase activity → `REMOVE`.** A specific
  catalytic activity on a specific substrate, asserted on a protein with a competing specific
  family signature and an established different function, with no evidence for it on this
  protein or any sarcosine oxidase subunit.
- **`GO:0005886` plasma membrane → `REMOVE`.** The single donor behind this node, P37339, is
  inner-membrane-associated because E. coli LhgD feeds electrons to the respiratory chain.
  SoxA has no transmembrane segment and no membrane keyword on its record, and the sarcosine
  oxidase is a soluble cytoplasmic enzyme — `soxB` carries cytoplasm rows from a different
  node, and the pathway runs on cytoplasmic substrates
  (`[PMID:17951379 "Once in the cytoplasm, choline binds to BetI"]`).

Note on the donor count: the project rule is explicit that a short `WITH/FROM` list is **not**
weak support, so the fact that the plasma-membrane node has one donor is not used as an
argument. The argument is that the donor's membrane association is a property of its own
respiratory role and does not transfer.

## Problem 2: a wrong oxidoreductase branch

`GO:0016614 oxidoreductase activity, acting on CH-OH group of donors` (IEA,
`GO_REF:0000117`, `ARBA:ARBA00028437`) asserts the wrong chemistry. Sarcosine oxidation
attacks a **C–N** bond, not a C–OH. Checked in OLS: the ancestors of `GO:0008115` are

```
GO:0003824 catalytic activity
GO:0016491 oxidoreductase activity
GO:0016645 oxidoreductase activity, acting on the CH-NH group of donors
GO:0016647 oxidoreductase activity, acting on the CH-NH group of donors, oxygen as acceptor
```

`GO:0016614` is **not** among them — the CH-NH branch (`GO:0016645`) is the correct one. The
row's only evidence is an ARBA machine-learning association rule, which the project rules
class as an unvetted prediction. `REMOVE`, with a `WRONG_TERM` defect against UniProt naming
`GO:0016645` as the corrected value.

By contrast `GO:0016491 oxidoreductase activity` **is** a genuine ancestor, so that row is
`TOO_GENERAL` rather than wrong.

## Problem 3: the qualifier

As for `soxD` and `soxG`: `enables GO:0008115` over-reaches on a subunit that does not carry
the catalytic site. The flavin and the D-amino-acid-oxidase-family domain are on SoxB. SoxA's
own contribution is the folate-handling half, so it gets `contributes_to_molecular_function`
for the activity and keeps `GO:0046653` as a process it directly participates in.

`enables` → `contributes_to` recorded once, on the IMP row, against PseudoCAP.

## Iron-sulfur cluster binding is kept

`GO:0051536` (IEA, from `IPR001041`) is accepted: the 2Fe-2S ferredoxin-type domain is a real
domain assignment on this protein, supported by three independent InterPro signatures and a
Pfam match, and domain classification is valid support for a binding claim. The 2Fe-2S cluster
of the alpha subunit is the one part of soxA's cofactor complement that does not rest on ARBA
text.
