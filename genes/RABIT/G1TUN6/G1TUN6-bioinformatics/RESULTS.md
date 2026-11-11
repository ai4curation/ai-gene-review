# G1TUN6 (rabbit UBE2L6) sequence and phylogenetic placement

Analysis date: 2026-10-20. Script: `compare_sequences.py` (raw output in
`compare_sequences_output.txt`).

## Pairwise comparison (global, BLOSUM62)

| Comparator | Length | Identity to G1TUN6 | G1TUN6 C86 aligns to |
|---|---|---|---|
| O14933 human UBE2L6 (UbcH8) | 153 | 79.7% over 153 aligned pairs | C86 |
| Q9QZU9 mouse Ube2l6 | 153 | 75.2% over 153 aligned pairs | C86 |
| P68036 human UBE2L3 (UbcH7) | 154 | 52.3% over 153 aligned pairs | C86 |
| P68037 mouse Ube2l3 | 154 | 52.3% over 153 aligned pairs | C86 |

G1TUN6 is 153 residues, the same length as human and mouse UBE2L6, with no
gaps against them, so it is a full-length product and not a fragment or
truncated gene model. The active-site cysteine (UniProt ACT_SITE 86, glycyl
thioester intermediate) is conserved and aligns to Cys86 of human UBE2L6, the
residue used as the catalytic cysteine in the UBE2L6 structural work.

Identity alone does not establish orthology. The orthology call rests on
independent evidence: the UniProt record cross-references CTD 9246 (the human
UBE2L6 gene) and Ensembl Compara projects the human O14933 annotations onto this
protein (GO_REF:0000107). The sequence result is consistent with that call:
G1TUN6 is much closer to UBE2L6 than to the UBE2L3 paralog.

## PANTHER placement

UniProt cross-references G1TUN6, O14933, Q9QZU9 and P68036 to PANTHER family
PTHR24067 with no subfamily. The PANTHER 19 web service (geneinfo for O14933)
places human UBE2L6 in PTHR24068:SF43 "UBIQUITIN_ISG15-CONJUGATING ENZYME E2
L6". This appears to be a renumbering of the family between releases, and
`interpro/panther/panther.obo` lists UBE2L3 separately in SF67 and SF116.
Repeated geneinfo queries for P68036, Q9QZU9 and G1TUN6 returned empty
responses, so their subfamilies could not be retrieved in this session. Rabbit
does not appear to be one of PANTHER's reference genomes: G1TUN6 has no IBA rows.

## PAINT nodes relevant to UBE2L6 (from PTHR24067-paint.tsv)

- PTN000631065 (taxon Mammalia, 40674): GO:0042296 ISG15 transferase activity and
  GO:0032020 ISG15-protein conjugation. Seeds: MGI:1914500 (mouse Ube2l6) and
  UniProtKB:O14933 (human UBE2L6).
- PTN002514495 (broad E2 node): GO:0061631 ubiquitin conjugating enzyme activity
  and GO:0000209 protein polyubiquitination. Seeds include UniProtKB:P68036
  (UBE2L3). Human O14933 inherits GO:0061631 by IBA from this node.
- PAINT did not propagate innate immune response at PTN000631065 or at any other
  node, although human O14933 carries an IDA for it (PMID:28724761).

Human O14933 receives IBA GO:0042296 and GO:0032020 with PTN000631065 in WITH/FROM
(QuickGO, queried 2026-10-20). A rabbit orthologue of human and mouse UBE2L6 sits
inside that Mammalia node, so the ISG15 functions placed there are expected to
apply to G1TUN6.
