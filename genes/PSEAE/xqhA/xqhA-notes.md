# xqhA (PA1868) — curation notes

## Identity

XqhA is an **orphan secretin** (GspD family) of *Pseudomonas aeruginosa* PAO1: a
GspD-family outer-membrane channel encoded away from both the *xcp* and *hxc* clusters,
which can functionally replace the main Xcp secretin XcpQ. Its partner is XphA, a GspC
(XcpP) homologue encoded next to it, and the two together form the "P(A)Q(A)" gatekeeper
pair of a **hybrid** T2SS that works with the rest of the Xcp machinery
[PMID:17351035 "Our results also revealed that complementation of an
xcpP/xcpQ mutant can be obtained with the gene couple xphA/xqhA."].

T2SS specificity in this organism rests mainly on the GspC/GspD pair
[PMID:17351035 "this specificity mainly
involves two proteins, XcpP (GspC family) and the secretin XcpQ (GspD family),
which are the gatekeepers of the system"], and swapping in XphA/XqhA changes what gets
exported: the hybrid machine secretes the major Xcp substrates but **not** the
aminopeptidase PaAP
[PMID:17351035 "A two-dimensional polyacrylamide gel electrophoresis
analysis showed that except for the aminopeptidase PaAP, for which secretion is
not restored by the P(A)Q(A) subunit in the xcpP/xcpQ deletion mutant, each
major Xcp-dependent exoprotein is secreted by the new hybrid machinery."]. The pair is
also expressed on a different schedule from XcpP/XcpQ
[PMID:17351035 "using a chromosomal xphA-lacZ fusion, we showed
that the xphA-xqhA genes are transcribed from an early stage of bacterial
growth"].

So *P. aeruginosa* has three GspD-family secretins — XcpQ, HxcQ and XqhA — and all three
share one PANTHER node (PTN000768388), each with its own experimental annotation.

## Domain architecture

776 aa. `SIGNAL 1..32`, then a canonical secretin: GspD-like N0 (48–114), three NolW-like
ring-building domains (141–201, 206–271, 276–352) and the secretin β-barrel (359–597),
with the GspD/PilQ family entry and the NCBIfam `TIGR02517` "type II secretion system
secretin GspD" covering 48–605.

Beyond residue ~605 there is a C-terminal extension of about 170 residues. Within it,
**684–769 matches CATH-Gene3D `G3DSA:3.30.70.1070` "Sporulation related repeat" and
nothing else** — no Pfam, no PROSITE, no NCBIfam, no family-level InterPro entry covers
that region. That single structural match is the whole basis of the `GO:0042834` row.

## The peptidoglycan-binding row

`GO:0042834` peptidoglycan binding is asserted by IEA from `IPR036680`. Two facts about
that entry decide the row:

1. **IPR036680 is a `homologous_superfamily`** — "Sporulation-like domain superfamily" —
   i.e. a structural grouping, not a domain or family entry. InterPro nonetheless maps it
   to a specific ligand-binding molecular function.
2. **InterPro's own justification for the term comes from other proteins.** Its
   description cites FtsN of *E. coli* and *C. crescentus*, plus CwlM and RlpA — cell
   division and cell wall proteins: "The SPOR domains in the FtsN cell division proteins
   from *Escherichia coli* and *Caulobacter crescentus* have been shown to bind
   peptidoglycan."

The comparator check is what makes this actionable, and it was run after confirming the
query can return a positive (`GO:0042834` has 42,400 annotations overall, and nine in
PAO1, so a negative result here would not be a malformed-query artifact):

| PAO1 protein | route to GO:0042834 |
|---|---|
| PA5052, PA5037, PA4278, PA3110, rlpA | `IPR007730` **and** `IPR036680` |
| PA0667 | `IPR007340` (LysM-like domain) |
| fimV | **IDA**, PMID:21097635 |
| **xqhA** | **`IPR036680` alone** |

`IPR007730` is "Sporulation-like domain" and its InterPro type is **domain**; InterPro maps
`GO:0042834` from both it and its superfamily. So every other protein in this organism that
reaches the term by the SPOR route matches the domain-level entry as well — including
*rlpA*, one of the proteins InterPro's description names. **xqhA is the sole outlier whose
assignment rests on fold similarity alone.**

**Action taken: `MARK_AS_OVER_ANNOTATED`, not `REMOVE`.** The claim is not demonstrably
false and there is a plausible reading: a secretin has to cross the peptidoglycan layer,
and C-terminal accessory domains that grip the sacculus are known in related
channel-forming families, so a genuine peptidoglycan-binding module at a secretin's
C-terminus would not be surprising. But nothing has been tested on XqhA or on any secretin
carrying this fold, the matched region has no domain-level signature, and the function was
transferred from proteins doing an unrelated job. That is an over-annotation of a structure
match rather than a wrong mapping, which is exactly what the action is for.

A `source_defects` entry asks InterPro to check whether a `homologous_superfamily` entry
should carry this molecular function at all when the domain-level entry exists and is what
the characterised members match. Confidence `SUSPECTED`, `requested_change: CHECK` — the
request is about the mapping's tier, which I can show, not about the biology of XqhA's
C-terminus, which I cannot.

## Other annotation decisions

- `GO:0015627` ×3 (IBA, IDA, InterPro IEA) and `GO:0015628` ×2: ACCEPT throughout.
- `GO:0009279` cell outer membrane (SubCell IEA): ACCEPT.
- `GO:0019867` outer membrane (InterPro IEA, IPR013356): MODIFY to `GO:0009279`.
- `GO:0009306` protein secretion (InterPro IEA, IPR004846): MODIFY to `GO:0015628`, with
  the same reasoning and the same corpus-consistency note as PA0685 — the signature spans
  T2SS and T3SS, and the disjunct is resolved by the gene's other evidence. All reviewed
  genes carrying this row MODIFY it to their system-specific term.
- `GO:0008320` proposed NEW (IC), as for xcpQ and PA0685, since GOA gives the secretin no
  molecular function.

The IDA row cites PMID:17351035, which is abstract-only in the cache. It names XqhA
throughout and reports the complementation and 2-D gel results directly, so the
complex-membership claim does not depend on unread text; nothing here second-guesses the
curator.

## Provider deep research

Not available. `--provider perplexity` is not configured in this environment and
`--provider asta` returned HTTP 429. Per project policy these notes stand in place of a
provider file rather than a hand-written file named as one.
