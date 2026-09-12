# Blinded comparison — dGTPase NF002326 / Q92Q32 (a reviewed "-like" member)

Holdout (before run) vs `openscientist.md`. This run tested the over-annotation
CAUTION we raised on the dGTPase row (13 reviewed "-like" members, no EC).

## Verdict: our caution is SUBSTANTIATED and refined

| Question | Result |
|---|---|
| Active site intact, or degraded pseudo-enzyme? | **INTACT** — confident all-α HD-domain fold (AF-Q92Q32-F1 pLDDT 94.8); full H…HD…D metallocenter present, unsubstituted, converged in one pocket. So an MF **is** warranted. |
| Strict dGTP specificity (GO:0008832 / EC 3.1.5.1)? | **NOT supported** for this member. Closest to human **SAMHD1** (33.1% id, a *broad* dNTPase), more distant from strict *E. coli* Dgt (26.2%) and hexameric dGTPase (22.2%). Specificity is set by nucleobase-recognition residues unreadable from homology. |
| Correct altitude | General **dNTP triphosphohydrolase**, substrate (dGTP-specific vs broad) left open. |

Matches the holdout (intact HD fold; substrate the open question) and lands on the
UNDECIDED-substrate side — **vindicating the UniProt curator's "-like" caution**.

## Curation consequence for the seed (important)

The seed's dGTPase row was a **"refine"**: NCBI gave the broad parent GO:0016793
(triphosphoric monoester hydrolase); we refined it to the specific GO:0008832
(dGTPase). For the strict-dGTPase core of NF002326 (the ~59 reviewed members that
already carry GO:0008832) that refinement is fine. **But for the "-like" clade
(this member, the 13 reviewed we flagged, and its TrEMBL tail) the strict GO:0008832
is an over-refinement** — they are catalytically intact but SAMHD1-like broad
dNTPases.

GO structure note: **GO:0008832 (dGTPase) and GO:0106375 (deoxynucleoside
triphosphate hydrolase activity, the broad dNTPase term) are SIBLINGS**, both
children of GO:0016793 — the broad clade cannot take a parent-of-dGTPase, it needs
the sibling GO:0106375 or the common parent GO:0016793. So:

- strict-dGTPase members → **GO:0008832** (as in the seed) — OK;
- SAMHD1-like "-like" members → **GO:0106375** (broad dNTP hydrolase), NOT GO:0008832;
- a single family-level mapping to strict GO:0008832 therefore over-annotates the
  broad members. Safest family-level call is NCBI's original **GO:0016793** (the
  refine was partly an over-refinement), OR split the mapping by clade.

Net: keep GO:0008832 only for verified strict-dGTPase members; treat the "-like"
clade as GO:0106375 / substrate-UNDECIDED. This is the mirror of DUF1156 — there
OpenScientist showed we UNDER-specified; here it shows the seed can OVER-specify.

## Decisive experiment
In-vitro hydrolysis of all four dNTPs (dGTP/dATP/dCTP/dTTP) with metal + allosteric-
activator dependence → resolves strict-dGTPase vs broad-dNTPase and the exact EC.

## Literature note
Report cites no cached PMIDs for the specificity call — it rests on structure +
consistent-method global alignment to SAMHD1/Dgt, which is checkable and sound.
