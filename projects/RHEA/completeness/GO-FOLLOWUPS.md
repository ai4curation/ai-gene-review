---
title: "RHEA -> GO completeness: candidate upstream issues"
---

# Candidate upstream issues

**Parent:** [RHEA-SWISSPROT-COMPLETENESS.md](../RHEA-SWISSPROT-COMPLETENESS.md)

Problems in GO, or in mappings that feed GO, found while completing the RHEA→GO mapping for
Swiss-Prot reactions. **Nothing here has been filed yet.** Each item is a draft awaiting approval.
The GO edits themselves are staged as rows in [`../rhea2go.sssom.yaml`](../rhea2go.sssom.yaml).

## go-ontology: RHEA xref predicates

1. **Inverted predicates.** Each of these is the case where the GO term is broader than the reaction
   but the xref says `broadMatch` (GO narrower), or the GO term equals the reaction:
   - GO:0003953 NAD+ nucleosidase activity: `RHEA:16301 {broadMatch}`. The GO definition *is* this
     reaction, so this should be `exactMatch`.
   - GO:0046592 polyamine oxidase activity: `RHEA:25808 {broadMatch}`. The spermidine reaction is a
     polyamine oxidation, so this should be `narrowMatch`.
   - GO:0140326 ATPase-coupled intramembrane lipid transporter activity: `RHEA:66132 {broadMatch}`.
     Generic ATP-driven lipid translocation is broader than the PE reaction, so this should be
     `narrowMatch`.
2. **RHEA:66132 carries `broadMatch` on 20 GO terms**, including ceramide, LPS, lipid III,
   sphingolipid and glycolipid floppases, and lysoPC, lysoPS and glycosylceramide flippases. Those
   are not narrower than a PE-translocation reaction, so those xrefs should be removed.
3. **Five RHEA xrefs have no predicate**; all are `exactMatch`: GO:0052868/RHEA:83435,
   GO:0047473/RHEA:55132, GO:0004435/RHEA:33179, GO:0036393/RHEA:69416, GO:0035755/RHEA:44884.
4. **RHEA:30783 `narrowMatch` on GO:0043795 glyceraldehyde oxidoreductase** (EC 1.2.99.8, generic
   acceptor, the Mo/W enzyme). RHEA:30783 is NAD+-dependent, and every carrying Swiss-Prot entry is
   ALDH1A1 (an NAD-dependent aldehyde dehydrogenase). Move it to GO:0004029 aldehyde dehydrogenase (NAD+)
   activity.

## go-ontology: structure

5. **GO:0106310 protein serine kinase activity is not `is_a` GO:0004674 protein serine/threonine
   kinase activity.** Its only parent is GO:0004672. The Ser/Thr term reads as covering both, so
   1,409 Swiss-Prot Ser/Thr kinases carry RHEA:17989 → GO:0106310 while their GO annotation sits
   on a non-ancestor.
6. **There is no protein-threonine kinase term.** RHEA:46608 (L-threonyl-[protein] phosphorylation)
   is on 3,735 Swiss-Prot entries, so it is staged as `narrowMatch` to GO:0004674. Alternatively,
   GO:0004674 could be given a sibling GO:0106310-style threonine term.
7. **Histone-only terms with no protein-level parent:** benzoyl-, isonicotinyl- and methacryl-lysine
   transferases and removers (GO:0140228, GO:0140229, GO:0140230, GO:0140218), and the H3R2/H4R3
   arginine demethylases (GO:0033746, GO:0033749). RHEA's reactions are on generic
   L-lysyl/arginyl-[protein], so the staged calls fall back to class terms.

## InterPro2GO (via go-annotation / InterPro)

8. **IPR004803 "tRNA-guanine transglycosylase" → GO:0008479 tRNA-guanosine(34) queuine
   transglycosylase activity.** The family spans bacterial preQ1-dependent Tgt (RHEA:24104,
   EC 2.4.2.29), eukaryotic queuine QTRT1 (EC 2.4.2.64), non-catalytic QTRT2, and archaeal ArcTGT
   (guanine15, RHEA:43164 → GO:0043867). All 35 Swiss-Prot ArcTGTs receive the queuine term from
   InterPro2GO alone. The mapping should move to subfamily entries or to a generic TGT term (none
   exists yet).

## Notes (not issues)

- **GMP synthase GuaA:** RHEA records the glutamine-dependent reaction (GO:0003922), while
  InterPro2GO IPR025777 (ATP-pyrophosphatase domain), TreeGrafter and IBA give the
  ammonia-dependent GO:0003921. Both are catalysed: the synthetase domain uses NH3. This is a
  `has_part` relationship GO does not state (GO:0003922 `has_part` GO:0003921?), not a wrong
  annotation.
