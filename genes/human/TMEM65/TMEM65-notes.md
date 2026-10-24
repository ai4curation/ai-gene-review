# TMEM65 (Q6PI78) — review notes

## 1. What the protein is

TMEM65 is a small (240 aa) polytopic protein of the mitochondrial inner membrane (IMM). It carries an
N-terminal mitochondrial targeting sequence that is cleaved on import, followed by a matrix-exposed
soluble segment and three transmembrane helices.

- Mitochondrial import and IMM integration:
  [PMID:24765583 "Alkali extraction analysis and digitonin extraction test using isolated mitochondria
  revealed that TMEM65 is an integral membrane protein that localizes to the inner-membrane of
  mitochondria."]
- Independent confirmation in human fibroblasts, plus a pathogenic splice variant:
  [PMID:28295037 "Subcellular fractionation confirmed that the TMEM65 protein was present in the inner
  mitochondrial membrane."]
- Both 2025 mitochondrial-calcium papers also place it in the IMM (GOA carries `is_active_in
  GO:0005743` IDA from each).

A separate, earlier line of work reported Tmem65 as a **cardiac intercalated-disc / plasma-membrane**
protein that stabilises connexin 43:
[PMID:26403541 "We identify Tmem65 as a cardiac-enriched, intercalated disc protein that increases
during development in both mouse and human hearts."]
This is the origin of the `plasma membrane`, `intercalated disc`, `cardiac conduction`,
`regulation of cardiac conduction` and `cardiac ventricle development` annotations (plus their
ISS/Ensembl-orthology projections). It sits uneasily with the IMM consensus — a protein with a
cleaved MTS that fractionates with the IMM is not obviously also a sarcolemmal protein — and none of
the mitochondrial studies reproduce it. Treated here as real but non-core and unreconciled, not
removed: the underlying data are experimental (IDA), and the two localisations are not formally
mutually exclusive.

## 2. The contested molecular function

Everything below concerns mitochondrial Na+/Ca2+ exchange (mito-NCX), the Na+-driven route by which
matrix Ca2+ is exported. Three groups independently found that TMEM65 is **required** for it. They
disagree about *what TMEM65 does*.

### Position A — TMEM65 *is* the exchanger (Zhang et al., Nat Cell Biol 2025)

[PMID:40691517 "Heterologous expression of TMEM65 induces Na+/Ca2+ exchange in cells lacking native
mito-NCX activity. Moreover, purified, liposome-reconstituted TMEM65 exhibits key mito-NCX features."]

The strongest arguments are the heterologous-reconstitution ones:
- [PMID:40691517 "Expression of human TMEM65 in these cells produced robust mito-NCX, which was
  inhibited by CGP-37157 (Fig. 3a-b)"] — in Sf9 mitochondria, which have a uniporter but no native
  mito-NCX.
- [PMID:40691517 "Lastly, we verified that no NCLX was co-purified or co-reconstituted with TMEM65
  (Extended Data Fig. 9b–c), ensuring that the observed activity is unrelated to NCLX."]
- Tissue distribution matches mito-NCX activity where NCLX's does not:
  [PMID:40691517 "TMEM65 is highly expressed in the heart and brain but absent in the liver,
  correlating with mito-NCX activity in these tissues."]
- Conclusion asserted flatly: [PMID:40691517 "These findings firmly establish TMEM65 as the protein
  mediating mito-NCX, offering a new therapeutic target for diseases associated with mitochondrial
  Ca2+ dysregulation."]

### Position B — TMEM65 is a required *regulator* of NCLX (Garbincius et al., Nat Metab 2025)

[PMID:40200126 "we identify the mitochondrial inner membrane protein TMEM65 as an NCLX binding
partner that enhances sodium (Na+)-dependent mCa2+ efflux. Mechanistically, acute pharmacological
NCLX inhibition or genetic deletion of NCLX ablates the TMEM65-dependent increase in mCa2+ efflux,
and loss-of-function studies show that TMEM65 is required for Na+-dependent mCa2+ efflux."]

The decisive experiment is epistatic: TMEM65 has no effect in cells lacking NCLX.
[PMID:40200126 "These findings suggest that TMEM65 limits net matrix Ca2+ accumulation upon increased
cytosolic Ca2+, but that this effect requires NCLX."]
[PMID:40200126 "Here we report the identification of TMEM65, an inner mitochondrial membrane protein,
as a genetically confirmed regulator of NCLX-dependent mCa2+ efflux and demonstrate its critical role
in preventing pathogenic mCa2+ overload in excitable tissues."]

### The field has not resolved it

A Cell Metab commentary (Garbincius & Elrod — note: same lab as Position B, so not a neutral referee,
but the methodological point is concrete) frames the dispute and identifies the specific gap:

[PMID:41061666 "In a recent study published in Nature Cell Biology, Zhang et al. challenge the
prevailing view that NCLX is the main mediator of mitochondrial sodium (Na+)/Ca2+ exchange (mito-NCX)
by proposing that transmembrane protein 65 (TMEM65) is responsible for this phenomenon."]

[PMID:41061666 "Unfortunately, this experiment cannot distinguish simple binding of Ca2+ to TMEM65
protein embedded in the proteoliposome membrane from actual transport of Ca2+ across the membrane."]

and, even-handedly:
[PMID:41061666 "Zhang et al. provide compelling evidence supporting a critical role for TMEM65 in
mCa2+ extrusion."]

So the 45Ca2+ proteoliposome accumulation assay — the one experiment that would make TMEM65 a
transporter rather than an accessory factor — is contested on the grounds that accumulation could
reflect binding rather than translocation. No electrophysiology on purified TMEM65 exists.

## 3. GOA carries both sides

Confirmed directly in `TMEM65-goa.tsv` (QUALIFIER column):

```
NOT|enables  GO:0005432 calcium:sodium antiporter activity  IDA  PMID:40200126  UniProt
enables      GO:0005432 calcium:sodium antiporter activity  IDA  PMID:40691517  UniProt
```

Two IDA annotations of the same term with opposite polarity, both from UniProt, both dated
2025-11-06. GO has deliberately annotated the disagreement rather than picking a winner. The stub
already carries `negated: true` on the PMID:40200126 row — verified, no fix needed.

**Decision:** `UNDECIDED` for both GO:0005432 rows. Accepting the positive IDA while a `NOT` IDA of
the same term co-exists would assert a resolution that does not exist; removing either would overrule
a curator who read a full text I have not. `UNDECIDED` is what the enum is for. The same reasoning
propagates to `GO:0035725 sodium ion transmembrane transport`, which GOA derives automatically from
GO:0005432 by inter-ontology inference (GO_REF:0000108) and which is therefore only as sound as the
contested MF.

**What is *not* contested:** that TMEM65 is required for mitochondrial Ca2+ export, and that it acts
at the IMM. `GO:0099093 calcium export from the mitochondrion` (IDA from *both* papers) and
`GO:0005743 mitochondrial inner membrane` are accepted as core.

## 4. Cross-reference: the counterion is contested for NCLX too

Both 2025/2026 cryo-EM structures of NCLX note it lacks the canonical Na+ sites — which is also
Position A's structural argument against NCLX:
[PMID:40691517 "However, it is unclear whether NCLX binds Na+, since it lacks multiple
Na+-coordinating residues found in canonical CaCA Na+/Ca2+ exchangers, such as cardiac NCX1"]
[PMID:40931067 "Structural comparison indeed reveals that NCLX lacks the Na+-binding sites identified
in MjNCX (Sext and Sint)."]

Note on provenance: PMID:40691517 (TMEM65 = mito-NCX) and PMID:40931067 (NCLX = H+/Ca2+ exchanger)
share senior authors (Feng L., Tsai M.-F.). They are one internally consistent model — TMEM65 does
mito-NCX, NCLX does something else — rather than two independent confirmations. That matters when
weighing how much of the field has actually moved. See `SLC8B1-notes.md`.

## 5. Other annotations

- `GO:0005515 protein binding` IPI (PMID:32296183, HuRI binary interactome, 37 partners collapsed
  into one stub row) — bare protein binding, uninformative as a molecular function.
- `GO:0005739 mitochondrion` (IBA, HTP PMID:34800366) — correct, less specific than the IMM
  annotations the gene already carries.
- Cardiac terms (`GO:0003231`, `GO:0061337`, `GO:1903779`) — organismal phenotypes arising from the
  Cx43/intercalated-disc work and its orthology projections; real but distal to the molecular
  function, and in any case downstream of whichever mitochondrial role turns out to be correct.

## 6. Open questions recorded in the review

1. Does purified TMEM65 translocate charge? (Electrophysiology on reconstituted protein, or
   simultaneous bilayer Ca2+/Na+ reporters, would settle Position A vs B.)
2. Why does TMEM65 require NCLX in fibroblasts (PMID:40200126) but suffice in Sf9 mitochondria and
   liposomes (PMID:40691517)?
3. Does CGP-37157 bind TMEM65, NCLX, or both?
4. Is the intercalated-disc/Cx43 localisation a genuine second pool, or an artefact?
