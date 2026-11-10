# UR000038407 / HAMAP MF_01501 (MtrH): what the rule asserts and how HAMAP treats complex subunits

Sources: `hamap_MF_01501.txt` (the MF_01501 block extracted verbatim from the
HAMAP rule flat file `hamap_rules.dat`), the cached UniRule JSON
(`UR000038407.json`), and live UniProtKB.

Commands (run from this folder):

    python summarize_complex_subunit_rules.py /path/to/hamap_rules.dat > summary.txt
    python classify_rule_matches.py > matches_summary.txt   # writes rule_matches.tsv

## What MF_01501 writes

- Name: RecName "Tetrahydromethanopterin S-methyltransferase subunit H" with EC=7.2.1.4.
- CATALYTIC ACTIVITY: RHEA:53492, the whole Na+-translocating reaction of the complex
  (methyl-H4MPT + CoM + 2 Na+(in) = H4MPT + methyl-CoM + 2 Na+(out)), EC 7.2.1.4.
- FUNCTION: complex-level text, followed by the MtrH-specific sentence (methyl transfer
  from methyl-H4MPT to the corrinoid of MtrA).
- SUBUNIT: the eight-subunit composition. No SUBCELLULAR LOCATION, no transmembrane
  trigger, no cellular-component GO term.
- Keywords: One-carbon metabolism, Transferase, Translocase, Methyltransferase;
  Methanogenesis only in methanogen classes.
- GO: GO:0030269 (F) and GO:0006730 (P) unconditionally; GO:0019386 (P) only in the
  four methanogen classes (a `case` block that the cached UniRule JSON does not show).

## The Mtr subunit rules (summary.txt)

All eight Mtr subunit rules (MtrA-MtrH) put EC 7.2.1.4 in the name and RHEA:53492 in
CATALYTIC ACTIVITY. Seven (MtrA-MtrG) state Cell membrane with a transmembrane trigger
and GO:0005886; MtrH alone has no location statement and no transmembrane trigger.
The MtrH rule is the only one whose FUNCTION adds a subunit-specific sentence.

## The HAMAP convention elsewhere (summary.txt)

The same whole-complex EC and Rhea reaction are copied onto every subunit in the
NDH-1 (11/11 rules, EC 7.1.1.-) and Na+-NQR (6/6, EC 7.2.1.1) rule sets; the Rnf
rules carry EC 7.-.-.- on all six subunits without a Rhea reaction. The bacterial
F-type ATP synthase is the exception: only the alpha and beta rules carry EC 7.1.2.2
and RHEA:57720, and the a, b, b', c, gamma, delta and epsilon rules carry neither.
So putting the complex reaction on every subunit is the usual HAMAP convention for
ion-translocating complexes, and the ATP synthase set shows HAMAP can restrict it.

## Matched proteins (matches_summary.txt)

UniProtKB entries with a HAMAP MF_01501 match all carry the MtrH-specific InterPro
family IPR028342; none is an MtxH-type paralog with only IPR023467. None has a
predicted transmembrane segment or a subcellular location statement. All are from
the four methanogen classes. Every entry carries EC 7.2.1.4 and RHEA:53492.
The live count differs from the rule statistics in the cached JSON (9 reviewed,
66 unreviewed), which come from an earlier release.
