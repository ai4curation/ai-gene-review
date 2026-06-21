# Hand-review of the cazy2go TRUE_GAP safe rows

Manual adjudication of the **53 mono-specific TRUE_GAP families** in
[`cazy2go.safe.sssom.yaml`](cazy2go.safe.sssom.yaml) — families whose single specific GO MF term is,
under GO `is_a` closure, on a branch `interpro2go` is **silent** on (see
[GLYCOBIOLOGY-resource-reuse.md](GLYCOBIOLOGY-resource-reuse.md)). Worksheet evidence (member counts,
EC, and what `interpro2go` *does* give for each family) from
[`truegap_worksheet.py`](truegap_worksheet.py).

Verdicts: **ENDORSE** (clean, actionable `interpro2go`/GO gap — mono-specific catalytic family →
specific activity), **CAUTION** (real but needs a specific EC, subfamily split, or the term is
mid-level), **REJECT** (artifact — the activity is not the family's).

## Headline: hand-review caught systematic auto-selection artifacts

The automated safe set wrongly included two artifact classes that family→GO MF propagation must
exclude:

1. **CBM families are non-catalytic.** Carbohydrate-binding modules carry no EC of their own; the EC
   on a reviewed member belongs to its appended *catalytic* domain. So **CBM→catalytic-activity is
   always an artifact**: `CBM58`→α-amylase, `CBM61`→glucan 6-glucosyltransferase, `CBM67`→α-L-
   rhamnosidase, `CBM90`→polysaccharide lyase, `CBM101`→β-agarase. → **REJECT (5).**
2. **Multidomain EC bleed-through.** `GT44`→`GO:0004197` cysteine-type endopeptidase: GT44 are the
   large clostridial toxin glucosyltransferases (TcdA/TcdB); their cysteine-protease autoprocessing
   domain (EC 3.4.22.-) is what carries that EC, **not** the GT activity. A glycosyltransferase family
   mapping to a peptidase MF is wrong by construction. → **REJECT (1).**

Both are now filtered out of the safe set automatically (CBM-prefix skip; drop GO terms under
`GO:0008233 peptidase activity`), and the mid-level `GO:0016837` (carbon-oxygen lyase acting on
polysaccharides, reached only via partial `EC 4.2.2.-`) is treated as too generic.

## REJECT (6) — artifact, removed from safe set

| Family | proposed GO | why rejected |
|--------|-------------|--------------|
| CBM58 | α-amylase activity | CBM = non-catalytic binding module; EC from appended catalytic domain |
| CBM61 | 1,4-α-glucan 6-α-glucosyltransferase activity | CBM non-catalytic |
| CBM67 | α-L-rhamnosidase activity | CBM non-catalytic |
| CBM90 | carbon-oxygen lyase (polysaccharides) | CBM non-catalytic + generic lyase term |
| CBM101 | β-agarase activity | CBM non-catalytic |
| GT44 | cysteine-type endopeptidase activity | toxin autoprotease domain EC, not the GT44 glucosyltransferase |

## CAUTION (13) — real activity but not a clean family-level row

| Family | proposed GO | caveat |
|--------|-------------|--------|
| PL24 / PL25 / PL23 / PL14 / PL40 / PL28 | carbon-oxygen lyase activity, acting on polysaccharides | only the **partial** EC 4.2.2.- on members → mid-level term, not the specific lyase; needs specific EC |
| AA5 | galactose oxidase activity | AA5 has two subfamilies (galactose oxidase **and** glyoxal oxidase); not truly mono-specific — subfamily split |
| GT89 | pentosyltransferase activity | partial EC 2.4.2.- → broad transferase-class term |
| GH112 | 1,3-β-galactosyl-N-acetylhexosamine phosphorylase | InterPro gives a *sibling* phosphorylase; confirm specificity before propagating |
| GH100 | β-fructofuranosidase activity | family heterogeneous (InterPro flags endo-α-GalNAcase); verify |
| GH50 | β-agarase activity | InterPro gives β-galactosidase (sibling); confirm |
| GT56 | 4-acetamido-4,6-dideoxy-D-galactose transferase | InterPro gives fucosyltransferase (different); confirm |

## ENDORSE (34) — actionable mono-specific family → specific GO MF gap

These are well-characterised, (near-)mono-specific CAZy families whose specific catalytic MF
`interpro2go` does not supply (it gives nothing on the MF branch, or only binding/CC terms). Strong
candidates to propose to `interpro2go` / as confirmation of GO coverage:

- **GT27 → polypeptide N-acetylgalactosaminyltransferase activity** (GALNT family, mucin-type
  O-glycosylation initiators; 46 reviewed members; InterPro silent on MF) — the strongest case.
- Glycosidases: **GH110**→α-galactosidase, **GH109**→α-N-acetylgalactosaminidase (InterPro gives only
  nucleotide binding), **GH89**→α-N-acetylglucosaminidase, **GH106**→β-glucuronidase,
  **GH136**→lacto-N-biosidase, **GH127**→β-L-arabinofuranosidase, **GH98**→blood-group endo-1,4-β-
  galactosidase, **GH105**→unsaturated rhamnogalacturonyl hydrolase, **GH88**→unsaturated chondroitin
  disaccharide hydrolase, **GH66**→dextranase, **GH64**→glucan endo-1,3-β-D-glucosidase,
  **GH119**→α-amylase, **GH53**→arabinogalactan endo-1,4-β-galactosidase, **GH70**→dextransucrase.
- Marine polysaccharidases: **GH96**→α-agarase, **GH150**→λ-carrageenase, **GH82**→ι-carrageenase,
  **PL7**→poly(β-D-mannuronate) lyase (alginate), **PL11**→rhamnogalacturonan endolyase,
  **PL13**→heparin lyase.
- Transferases: **GT117/GT105**→dolichyl-P-mannose-protein mannosyltransferase (PMT),
  **GT74**→galactoside 2-α-L-fucosyltransferase, **GT60**→Skp1-hydroxyproline GlcNAc-transferase,
  **GT52**→α-2,3-sialyltransferase, **GT78**→mannosylglycerate synthase, **GT73**→Kdo transferase,
  **GT72**→DNA α-glucosyltransferase, **GT121**→O-antigen ligase, **GT119**→peptidoglycan
  glycosyltransferase, **GH102/GH103**→lytic exotransglycosylase, **GH91**→inulin fructotransferase.

## Outcome

| verdict | n | disposition |
|---------|--:|-------------|
| ENDORSE | 34 | actionable `interpro2go`/GO gap candidates (need a human GO/InterPro curator sign-off before submission) |
| CAUTION | 13 | retain but flag; need specific EC / subfamily resolution (→ dbCAN-sub step) |
| REJECT | 6 | artifacts; auto-filtered from the safe set |

So **34 / 53 true-gaps are genuine, specific contributions** `interpro2go` lacks; **13 await
subfamily/EC resolution**; **6 were artifacts** the review removed. The 6 rejects validate the value
of hand-review over the raw automated set, and the CAUTION set motivates the subfamily step next.

**Effect on the safe set:** after adding the CBM-skip, peptidase-branch drop, `GO:0016837`-generic,
and **CAUTION-family** exclusion filters to `select_cazy2go_safe.py`, `cazy2go.safe.sssom.yaml` shrank
89 → 66 (artifact filters) → **60 rows** (35 true-gap + 25 altitude-gain); the ENDORSE families are
retained, the CAUTION families (AA5 etc.) and artifact rows are now excluded from the safe set. The 34 ENDORSE rows still require a **human GO/InterPro2GO
curator sign-off** before any submission — they are AI-proposed candidates, not curated GO records.
