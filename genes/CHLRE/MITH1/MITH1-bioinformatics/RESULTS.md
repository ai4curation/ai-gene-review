# Does MITH1 carry a membrane-binding element above its coiled-coil background?

Run `python3 membrane_element_scan.py` from this directory. Stdlib only, no network;
it reads `../MITH1-uniprot.txt` and hardcodes no results.

Written because the OpenScientist run intended for this gap (`kgap-mith1-membrane-element`)
could not be obtained: the service returned nothing for any submission after
2026-11-26 19:52 (see `genes/BACSU/plsY/plsY-notes.md`). It covers only what a
sequence scan can reach. **These are scores, not binding measurements.**

## Why a control was necessary

The protein is 1304 residues, of which **624 (47.9%) are annotated coiled-coil**
(`COILED` 208–313, 396–633, 683–710, 739–990), with low-complexity/disordered
`REGION`s at 60–180, 1194–1222 and 1258–1304. The record has **no** `TRANSMEM`
feature, consistent with the published detergent-sensitive co-pelleting that
indicates peripheral association.

Coiled coils have periodic hydrophobic faces, so they score as "amphipathic helices"
by construction. Every window below is therefore reported with whether it sits inside
an annotated coiled coil, and each score distribution is compared between coiled and
non-coiled positions. **A hit that is not separable from the coiled-coil background is
not evidence of anything.**

## Results

| Candidate mechanism | Best window | Score | Separable from coiled-coil background? |
|---|---|---|---|
| Amphipathic helix (Eisenberg µH) | 753–770, inside a coiled coil | +0.572 | **No** — best non-coiled window is +0.519, below the best coiled window; means +0.255 inside vs +0.214 outside |
| Basic patch (net charge, 18-mer) | **71–88** | **+8** | **Yes** — beats every coiled window (best inside +4); means +0.560 outside vs +0.051 inside |
| Hydrophobic loop (mean KD, 18-mer) | **179–196** | **+1.789** | **Yes** — beats every coiled window (best inside +0.506) |

## What follows

**No amphipathic helix.** All five top-scoring µH windows lie inside annotated coiled
coils, and nothing outside them exceeds the best coiled-coil window. This is exactly
the false positive the scan was designed to catch, and the control catches it. An
amphipathic-helix mechanism is **not** supported.

**Two candidate elements, both in or beside the disordered N-terminal region.** The
strongly basic window 71–88 (net +8) and the most hydrophobic window 179–196
(KD +1.789) both sit in or at the edge of the annotated low-complexity region 60–180,
and both are separable from the coiled-coil background. A basic patch binding anionic
lipid headgroups is a recognised peripheral mechanism, and this is where to look.

**Why these are candidates and not findings.** Low-complexity and disordered regions
commonly have skewed amino-acid composition, so a charge extreme inside one may be
composition bias rather than a functional patch; the scan cannot distinguish those.
With 1287 windows, some extreme is expected by chance, and no multiple-testing
correction was applied. The 179–196 hydrophobicity is in the range a transmembrane
helix would reach, yet the record annotates no TM segment and the published
detergent-sensitive co-pelleting argues against one, so that window should not be read
as a membrane-spanning element.

**What is out of scope.** Nothing here identifies a lipid, a leaflet, or a mechanism,
and nothing here tests binding. The gap asks what molecular activity MITH1 performs;
this narrows where to look for a membrane-interaction element and rules out one
mechanism, but it does not establish an activity. The gap stays OPEN.
