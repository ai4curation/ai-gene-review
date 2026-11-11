---
title: "RHEA -> GO completeness: candidate upstream issues"
---

# Candidate upstream issues

**Parent:** [RHEA-SWISSPROT-COMPLETENESS.md](../RHEA-SWISSPROT-COMPLETENESS.md)

Problems in GO, or in mappings that feed GO, found while completing the RHEA→GO mapping for
Swiss-Prot reactions.

**Filed (2026-11-05):**
- [geneontology/go-ontology#32884](https://github.com/geneontology/go-ontology/pull/32884): PR with
  batch 9 and items 1–4 below. **Closed unmerged** (too large, and not yet backed by
  gene reviews); to be resubmitted as small, review-backed PRs.
- [geneontology/go-ontology#32882](https://github.com/geneontology/go-ontology/issues/32882):
  MraY/MurG definitions (item 7b).
- [geneontology/go-ontology#32883](https://github.com/geneontology/go-ontology/issues/32883): NTR for
  preQ1 Tgt, EC 2.4.2.29 (item 8). E. coli Tgt's own IDA is on the queuine term, so this is a missing
  GO term first; the IPR004803 and UniRule fixes follow from it.
- [geneontology/go-annotation#6646](https://github.com/geneontology/go-annotation/issues/6646):
  ThiI InterPro2GO (item 9). Backed by the reviews genes/ECOLI/thiI, genes/BACSU/thiI and
  genes/SHESA/thiI, which record it as a `source_defects` entry on the GO:0004810 row.

The remaining items are drafts awaiting approval.
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

7b. **MraY and MurG terms have generic names but L-Lys-specific definitions.**
   GO:0008963 phospho-N-acetylmuramoyl-pentapeptide-transferase activity (RHEA:21920) and
   GO:0050511 undecaprenyldiphospho-muramoylpentapeptide beta-N-acetylglucosaminyltransferase
   activity (RHEA:23192) are defined with the L-Lys stem peptide (Gram-positive form). The
   meso-DAP forms GO:0051992 (RHEA:28386) and GO:0051991 (RHEA:31227) are siblings, not children.
   InterPro2GO and UniRule put the Lys terms on DAP-type enzymes (E. coli MraY/MurG and most
   Gram-negatives): 619 and 587 Swiss-Prot entries. Proposed fix: generalize the two definitions to
   any muramoyl-pentapeptide (keep the RHEA:21920/23192 xrefs as `narrowMatch`) and put the Lys
   and DAP forms underneath.

## InterPro2GO (via go-annotation / InterPro)

9. **IPR020536 "ThiI, AANH domain" → GO:0004810 CCA tRNA nucleotidyltransferase activity.** This
   is wrong. ThiI is tRNA 4-thiouridine synthase: RHEA:24176 → GO:0140741 tRNA-uracil-4
   sulfurtransferase activity. 267 Swiss-Prot ThiI entries get the CCA-adding activity from
   InterPro2GO alone. The mapping should move to GO:0140741.

8. **DONE (2026-11-09).** The preQ1 Tgt term requested in
   [geneontology/go-ontology#32883](https://github.com/geneontology/go-ontology/issues/32883)
   exists as **GO:7770158** tRNA-guanosine(34) preQ1 transglycosylase activity
   (go-ontology PR #32911), with `xref: RHEA:24104 {source="skos:exactMatch"}` and EC:2.4.2.29.
   RHEA:24104 (461 Swiss-Prot entries) is therefore mapped in GO, and its staged
   NoTermFound/broadMatch rows were removed from `rhea2go.sssom.yaml` (the term is not yet
   in a GO release, so the term validator cannot check a row pointing at it). The
   follow-on mapping fixes are tracked in
   [geneontology/go-annotation#6652](https://github.com/geneontology/go-annotation/issues/6652)
   (UniRule UR000079182, HAMAP MF_00168) and
   [geneontology/go-annotation#6653](https://github.com/geneontology/go-annotation/issues/6653)
   (InterPro). Original note:

   **IPR004803 "tRNA-guanine transglycosylase" → GO:0008479 tRNA-guanosine(34) queuine
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

## Reported during batch 10 (top 200 reactions); not yet independently verified

The subagents that curated batch 10 reported the items below. Each still needs to be checked
against go-edit.obo before it becomes an issue. The `NoTermFound` rows in batch 10 carry the
corresponding new-term proposals (77 reactions).

**Mis-predicated or misplaced xrefs**
- GO:0015385 sodium:proton antiporter has RHEA:29251 (1 Na+ : 2 H+) as `exactMatch`, but the
  definition is 1:1, which is RHEA:29419.
- GO:0140900 chloride:bicarbonate antiporter has RHEA:72203 (2 Cl- : 1 HCO3-) as `exactMatch`, but
  the definition is 1:1, which is RHEA:72363.
- GO:0033232 ABC-type D-methionine transporter has EC:7.4.2.11 as `exactMatch`, but that EC covers
  both L- and D-Met. No L- or generic ABC methionine transporter MF exists.
- Obsolete GO:0031679 NADH dehydrogenase (plastoquinone) has `replaced_by: GO:0008753`, which is
  NADPH-specific (donor mismatch).

**Definitions narrower than their name or EC xref**
- GO:0008478 pyridoxal kinase (EC 2.7.1.35 also covers pyridoxine and pyridoxamine).
- GO:0004731 purine-nucleoside phosphorylase (ribose-1P only).
- GO:0046922 (Ser only; EC 2.4.1.221 covers Ser and Thr).
- GO:0106251 (nucleoside only; it also lacks the EC:3.5.1.135 xref).
- GO:0004789 (no carboxylated thiazole).
- GO:0009383 rRNA (cytosine-C5-)-methyltransferase (small-subunit only).
- GO:0004674 and GO:0008531 (ATP-only, which excludes ADP- or CTP-dependent members).
- GO:0050290 sphingomyelin phosphodiesterase D (hydrolysis only; the Loxosceles enzymes cyclize).
- GO:0010333 terpene synthase (says "cyclic", but has acyclic children).

**Structure**
- GO:0015349 thyroid hormone transporter is `is_a` secondary active transporter, which is wrong for
  MCT8/MCT10.
- GO:0140292 and GO:0140293 ADP-ribosyl-Ser/Glu hydrolases are under N-glycosyl hydrolase; these
  bonds are O-glycosidic.
- GO:0140171 (generic acceptor) is `is_a` GO:0004457 (NAD-specific).
- There is no generic ferrochelatase parent.

**Large missing activities (by Swiss-Prot weight)**
- Proton-pumping NADH:quinone (generic and plastoquinone; 1,700–2,900 entries each).
- RuBisCO oxygenase (697).
- Acetyl-CoA carboxyltransferase EC 2.1.3.15 (980).
- QueC preQ0 synthase EC 6.3.4.20 (520).
- Bacterial preQ1 Tgt EC 2.4.2.29 (461).
- Photosystem I plastocyanin:ferredoxin oxidoreductase (457).
- Na+-NQR EC 7.2.1.1 (327).
- TtcA, TrhO, RsmG m7G527.
- DJ-1 nucleotide and nucleic-acid deglycase.
- Protein UMPylase.

**Native annotations that use the wrong chemistry**
- GO:0008137 (ubiquinone, H+-pumping) on plastoquinone NDH entries.
- GO:0008479 (queuine) on bacterial Tgt.
- GO:0004325 (protoporphyrin) on coproporphyrin ferrochelatase HemH.
- GO:0102067 on archaeal GGR.
- Phosphodiesterase terms on cyclizing SMase D.
- GO:0004126 (free cytidine) on APOBEC3.
