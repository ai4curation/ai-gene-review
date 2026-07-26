# Where does the human ABRA GO record come from, and does its one plasma-membrane call have any support?

Reproduce with `uv run --no-project --with requests python audit_abra_record.py`.
Q1, Q2, Q4 and Q5 are fetched at run time from the UniProt, QuickGO and InterPro REST APIs,
plus this gene's own `ABRA-goa.tsv`. Q3 instead reads the repository's committed PANTHER
family export, `interpro/panther/PTHR22739/PTHR22739-entries.csv` (refresh it with
`just fetch-panther-family PTHR22739`); if that file is absent the script aborts rather
than dropping the section. Nothing is hardcoded, and a failed fetch is reported rather
than counted as an absence. Machine-readable output is written to `results.json`.

Run date: 2026-07-25.

## Q1. The human record is almost entirely rodent

The 16 GOA rows break down as IBA 3, IEA 6, ISS 5, IPI 1, IDA 1 — **two experimental rows
out of sixteen**, and neither of them is about what ABRA does. Resolving every WITH/FROM
accession to a species gives:

| WITH/FROM source | rows |
|---|---|
| Abra (*Mus musculus*, Q8BUZ1) | 8 |
| `ensembl:ENSMUSP00000051973` (the same mouse protein) | 4 |
| `PANTHER:PTN001100454` | 3 |
| `MGI:MGI:2444891` (the same mouse gene) | 2 |
| `InterPro:IPR026111` (the Abra family signature) | 2 |
| Abra (*Rattus norvegicus*, Q8K4K7) | 2 |
| `RGD:708493` (the same rat gene) | 1 |
| PPP1R18 (*Homo sapiens*, Q6NYC8) | 1 |
| UniProt SubCell / no WITH/FROM | 3 |

Every WITH/FROM protein accession is a genuine one-to-one ortholog of the gene under review
(mouse or rat *Abra*), not a paralog, so the transfers are legitimate in kind. The point is
the concentration: fourteen of the sixteen rows trace to two rodent proteins, and the mouse
entry supplies eight of them under four different identifier styles, which makes the record
look better-sourced than it is. No human experiment has established any molecular function,
process or native localisation for ABRA.

## Q2. The plasma-membrane annotation is unsupported, and it has already spread

`GO:0005886 plasma membrane` is the only cellular-component annotation on human ABRA not
derived from a rodent ortholog. It is an IDA under `GO_REF:0000054` — the LIFEdb survey of
GFP-tagged proteins expressed in cultured cells. Three independent checks:

- **UniProt does not place ABRA there.** Its subcellular location is
  `Cytoplasm, myofibril, sarcomere` and `Cytoplasm, cytoskeleton`. No plasma membrane.
- **Nothing in the sequence targets a membrane.** UniProt was queried for all four
  membrane-targeting feature classes — Transmembrane, Intramembrane, Signal, Lipidation —
  and ABRA carries none of them. A peripheral protein can of course reach a membrane through
  a partner, but no such anchor is reported for ABRA, whereas its F-actin binding gives a
  ready alternative reading of a GFP rim signal as cortical actin.
- **The call has been projected back into the mouse.** Mouse Abra now carries `GO:0005886`
  twice — an Ensembl Compara IEA (`GO_REF:0000107`) and an ISO (`GO_REF:0000119`) — and both
  cite `UniProtKB:Q8N0Z2`, i.e. the human protein. The single human GFP-overexpression image
  is the sole origin of a plasma-membrane annotation in two species.

## Q3. The PANTHER family carries no paralog hazard

All 4 reviewed members of `PTHR22739` are named ABRA (human, mouse, rat, pig) and all fall in
the single subfamily `PTHR22739:SF20`. There is no second subfamily and no paralog in the
reviewed set, so the IBA annotations from node `PTN001100454` and the ISS transfers are
operating inside a one-to-one ortholog group. Whatever else is wrong with this record, the
propagation topology is not.

## Q4. "Costars" is a domain shared with a different gene

Exactly two reviewed human proteins carry the Costars domain `PF14705`:

| accession | gene | length | UniProt FUNCTION |
|---|---|---|---|
| Q9P1F3 | ABRACL | 81 aa | associates with the actin cytoskeleton, may modulate actin dynamics in favour of F-actin |
| Q8N0Z2 | ABRA | 381 aa | activator of SRF-dependent transcription, possibly by inducing nuclear translocation of MKL1/MKL2 |

ABRACL is essentially the domain alone; ABRA is a 381-residue protein in which the domain
occupies the C-terminus. Work reported on "Costars" — the 82-residue *Dictyostelium* protein
of PMID:20940261 and its small mammalian counterpart — is therefore a statement about the
ABRACL-type protein, not about ABRA. Cytoskeletal phenotypes from that line of work should
not be carried over to ABRA on the strength of the shared domain.

## Q5. The mouse ortholog carries the import term, but not the regulation term

The review proposes `GO:0042307` *positive regulation of protein import into nucleus* as a
`NEW` annotation for human ABRA. That proposal previously rested on reasoning about the mouse
record and the MRTF literature without being checkable here, unlike the Q2 back-propagation
finding. Projecting both import terms onto mouse Q8BUZ1:

| term | on mouse Q8BUZ1 | evidence | reference | WITH/FROM |
|---|---|---|---|---|
| GO:0006606 protein import into nucleus | yes | IDA | PMID:15798203 | *(none)* |
| GO:0042307 positive regulation of protein import into nucleus | **no** | — | — | — |

Two things follow, and they point the same way.

The mouse annotation is a **direct assay with an empty WITH/FROM**, so it is not an ortholog
transfer from human — it is primary evidence, and PMID:15798203 is the same paper the review
already cites for the MRTF import mechanism. The `NEW` proposal is therefore anchored to a
real experiment rather than to an inference chain.

But the mouse record uses the **unqualified process term**, and that is very likely the less
accurate of the two. `GO:0006606` reads as the annotated protein being part of the import
event; ABRA is not the cargo. What PMID:15798203 shows is ABRA *promoting the import of
MRTF-A/B*, which is what `GO:0042307` says. So the human proposal is not merely a copy of the
mouse annotation at a different granularity — it is the term the mouse row arguably should
have used, and the gap in the mouse record is itself the reason no transfer supplied it to
human.
