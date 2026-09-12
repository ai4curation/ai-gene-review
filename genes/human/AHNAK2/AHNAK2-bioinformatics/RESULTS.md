# AHNAK2: what the GO record is actually about

Every number below names the script that produces it. `audit_claims.py` re-derives
the load-bearing ones from the committed TSVs and fails if they drift.

## 1. Where the 13 GOA rows come from

`resolve_withfrom.py`, `gap_by_reference.py`

| basis | rows |
|---|---|
| human AHNAK2 imaged directly (HPA immunofluorescence IDA: cytosol, plasma membrane) | 2 |
| PMID:17185750, whose public abstract reports only AHNAK (2 IPI + 3 NAS) | 5 |
| IBA from periaxin/AHNAK donors (nucleus, cytoplasm, regulation of RNA splicing) | 3 |
| IEA: 1 UniProt SubCell mapping of a bare `ECO:0000250`, 2 ARBA rules | 3 |

Only the two HPA rows cite an experiment that is *reported for AHNAK2 in a
source anyone can read*. The five PMID:17185750 rows are not thereby wrong — the
paper is subscription-only and UniProt carries its DYSF interaction on the
AHNAK2 entry at `ECO:0000269`, which is a curator's attestation that AHNAK2 data
is in the full text — but nothing in the public record distinguishes them from
the identical rows the same paper gave human AHNAK.

## 2. The IBA donors are periaxin and AHNAK, not AHNAK2

`resolve_withfrom.py`, `check_multihit.py`

| token | resolves to | status | length |
|---|---|---|---|
| MGI:MGI:108176 | mouse Prx (O55103), periaxin | Swiss-Prot | 1391 aa |
| MGI:MGI:1316648 | mouse Ahnak (E9Q616) | TrEMBL (no Swiss-Prot entry exists) | 5656 aa |
| MGI:MGI:2144831 | mouse Ahnak2 (A0A7N9VR94) | TrEMBL (no Swiss-Prot entry exists) | 3501 aa |
| RGD:619960 | rat Prx (Q63425), periaxin | Swiss-Prot | 1383 aa |
| UniProtKB:Q09666 | human AHNAK | Swiss-Prot | 5890 aa |
| UniProtKB:Q9BXM0 | human PRX, periaxin | Swiss-Prot | 1461 aa |
| UniProtKB:Q8IVF2 | AHNAK2 itself (self-referential, valid) | Swiss-Prot | 5795 aa |
| PANTHER:PTN001156025 | a tree node, not a protein | - | - |

Multi-hit ambiguity is reported rather than collapsed: MGI:108176 has 5 UniProt
hits, MGI:1316648 has 5, MGI:2144831 has 3, RGD:619960 has 3. Neither mouse
Ahnak nor mouse Ahnak2 has a Swiss-Prot entry at all, so their *names* are
automatic even though their GO annotations are genuine IDAs.

**The AHNAK2 ortholog is absent from two of the three IBA donor sets.**
`GO:0005634 nucleus` draws on 3 periaxins + mouse Ahnak; `GO:0043484 regulation
of RNA splicing` draws on mouse Prx (which holds it only by IBA, i.e.
circularly) + mouse Ahnak. Only `GO:0005737 cytoplasm` includes mouse Ahnak2.

## 3. The paralogy is real but not functionally informative — and it points at periaxin

`paralogue_architecture.py`, output in `paralogue_architecture.md`

PANTHER puts AHNAK2, AHNAK and the periaxins in PTHR23348, in **three different
subfamilies** (SF37, SF41, SF42). The only structured domain any of them has is
an N-terminal PDZ.

| pair | PDZ-vs-PDZ identity | full-length local identity |
|---|---|---|
| AHNAK2 vs AHNAK | **28.4%** | 36.9% over 4838 aa |
| AHNAK2 vs human PRX | **56.8%** | 31.3% over 1342 aa |
| AHNAK2 vs mouse Prx | 58.0% | 36.2% over 1263 aa |
| AHNAK2 vs mouse Ahnak2 *(ortholog control)* | 89.7% | 66.2% |
| AHNAK vs mouse Ahnak *(control)* | 97.9% | 84.0% |
| human PRX vs mouse Prx *(control)* | 97.6% | 81.8% |

At its only domain, **AHNAK2 is twice as close to periaxin as to AHNAK.** That
is consistent with PDB 4CN0, which crystallised the PRX and AHNAK2 PDZ domains
together as homologues and did not involve AHNAK.

The 4838-residue AHNAK2-vs-AHNAK alignment is **71.9% repeat-on-repeat**, with
identity *higher* inside the repeat (39.9%) than outside it (29.3%): the big
alignment length is two low-complexity regions pairing up. The repeat units are
not even the same. Each protein's own most frequent 10-mer:

| protein | anchor | occurrences | occurrences of the AHNAK2 anchor |
|---|---|---|---|
| AHNAK2 | `KDSKFKMPKF` | 22 | 22 (spans residues 671-4468, 65.5% of the chain) |
| mouse Ahnak2 | `FKMPSFGVSA` | 12 | 11 |
| AHNAK | `KLKGPKFKMP` | 29 | **0** |
| mouse Ahnak | `KLKGPKFKMP` | 27 | **0** |
| human/mouse/rat PRX | — | 3-7 | **0** |

So "AHNAK2 is AHNAK's sibling" is a weaker premise than it looks, and it is not
the premise the IBA rows actually rest on.

## 4. AHNAK2's only UniProt location is an untraceable "by similarity" nucleus

`subcell_provenance.py`

```
AHNAK2 Q8IVF2  LOCATION: Nucleus            ECO:0000250          <- no source accession
AHNAK  Q09666  LOCATION: Nucleus            (no evidence tag at all)
PRX    Q9BXM0  LOCATION: Nucleus            ECO:0000269|PubMed:24633211
Prx    O55103  LOCATION: Nucleus            ECO:0000269|PubMed:10671475
```

The `GO_REF:0000044` nucleus row is a mechanical mapping of the first line. The
only *measured* nuclear localisation in this family belongs to periaxin. Human
Protein Atlas immunofluorescence for AHNAK2 (reliability **Enhanced**) calls
main location Cytosol, additional location Plasma membrane, and no nuclear
compartment — which is a measurement that declines to confirm, not a proof of
absence.

And in AHNAK and periaxin the nuclear pool is a **small N-terminal isoform**
(PMID:21940993), not the giant chain the annotation sits on. UniProt annotates
no such isoform for AHNAK2: its only short isoform, Q8IVF2-2, is residues
5003-5795 and lacks the PDZ domain entirely (`VSP_031550`, "Missing (in isoform 2)"
over 1..5002).

## 5. A 1.75 Å structure of AHNAK2's only domain produced zero GO annotations

`gap_homodimer.py`, `gap_by_reference.py`

PDB **4CN0** (1.75 Å, chains A/B, residues 108-203) is an intertwined
domain-swapped homodimer of the AHNAK2 PDZ domain, and is InterPro's
representative structure for the whole PTHR23348 family. UniProt curates it on
the AHNAK2 entry as `Homodimer (via PDZ domain) (PubMed:24675079)` with
`ECO:0000269`.

`PMID:24675079` has **0 GO annotations in all of GOA**, for any protein. Neither
AHNAK2 nor PRX nor AHNAK holds `GO:0042803`, `GO:0046982` or `GO:0051260`.

Per-paper coverage for the 11 papers this review uses:

| paper | annotations in GOA | on human AHNAK2 |
|---|---|---|
| PMID:17185750 (AHNAK/dysferlin) | 19 over 7 entities | 5 |
| PMID:20833135 (costamere) | 3 over 2 entities (mouse Ahnak, mouse Ahnak2) | **0** |
| PMID:15007166 (AHNAK2 discovery) | 2 over 1 entity (mouse Ahnak2) | **0** |
| PMID:21940993 (AHNAK splicing) | 17 over 2 entities (human AHNAK, mouse Ahnak) | **0** |
| PMID:24675079, 25560297, 31011849, 37349884, 38751848, 39849106, 33363388 | **0** | **0** |

The splicing paper is the sharp case: it produced 17 annotations, none on
AHNAK2 — yet AHNAK2 carries `GO:0043484` by IBA sourced from exactly those
annotations. The curator who read the paper did not annotate AHNAK2; the
phylogenetic pipeline did.

## 6. The two ARBA rows cannot be reproduced from the published rules

`arba_rules.py`

`ARBA00026971` (cytoplasm) has 2388 condition sets and `ARBA00027801` (plasma
membrane) has 686. Both rules condition only on InterPro, PANTHER, FunFam and
taxon. **Not one condition set in either rule mentions any of AHNAK2's six
signatures** (`IPR001478`, `IPR036034`, `IPR052082`, `PTHR23348`,
`PTHR23348:SF37`, Gene3D `2.30.42.10`).

The script self-tests first, constructing a true positive from the rule's own
conditions, so the zero is a result rather than a broken matcher. Either the
REST view of these rules is incomplete, or the annotations were applied from a
rule version whose conditions have since changed. Reported, not guessed at.

## 7. IntAct has 164 records over 118 partners; GOA imported none of them

`intact_partners.py`

18 distinct publication records (17 PMIDs plus one unassigned), 11 detection
methods (`anti tag coip` 55, `two hybrid array`
19, `two hybrid prey pooling approach` 19, `validated two hybrid` 18,
`holdup assay` 24, `proximity-dependent biotin identification` 11, ...). The
three two-hybrid sub-methods are the familiar one-screen-counted-three-ways
pattern, so UniProt's `NbExp=3` entries are not three experiments.

68 of the 164 records tested a short isoform (`Q8IVF2-3` 62, `Q8IVF2-2` 6)
rather than the 5795-aa chain.

GOA's only two `GO:0005515` rows name `O75923` (DYSF) and `Q9NZM1` (MYOF), and
**neither appears anywhere in IntAct's AHNAK2 record**. So the usual finding is
inverted here: this is not screen noise leaking into GO, it is a large
high-throughput interactome that GO has (defensibly) not imported, sitting
beside two rows from a targeted co-IP/pull-down paper.
