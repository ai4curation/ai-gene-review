# A0BFB4: verified PAINT descent and differing sequence-family assignment

The independently checked PAINT target rows identify A0BFB4 as leaf PTN002805316 and propagate eight positive assertions. Four autophagy-specific process/location assertions originate at PTN000681272. The repository's PTHR24348 PAINT table places that ancestral node in the UNC-51-related kinase family, with eukaryotic taxon 2759 and experimental descendant sources including Atg1/ULK kinases. The separate PANTHER membership index and current UniProt record instead assign A0BFB4 to PTHR44167:SF18.

Root subsequently retrieved the actual nested PANTHER tree through a POST request to `https://www.pantherdb.org/services/oai/pantherdb/treeinfo` with form `family=PTHR24348`. The retained tree path was independently read for this review: PTN002805221 → PTN000681272 → PTN007795585 → PTN008401646 → PTN001218730 → PTN007795752 → PTN002805316. The leaf explicitly identifies A0BFB4/GSPATT00028266001 and inherits PTHR24348:SF22.

The actual tree therefore confirms that A0BFB4 descends from the autophagy-bearing ancestral node. The current sequence classifier assigns a different family, but that discrepancy does not establish a biological loss or overturn the inspected PAINT topology. Compact ciliate domain architecture and absence of a target assay likewise do not establish functional loss.

The four autophagy terms are accepted as inherited functions: GO:0000045 autophagosome assembly, GO:0010506 regulation of autophagy, GO:0000407 phagophore assembly site, and GO:0005776 autophagosome. Broad catalytic, nucleotide-binding, cytoplasmic and membrane annotations remain supported. The remaining question is why the current sequence classifier and this actual PAINT tree differ, not whether the target is absent from the inspected ancestral clade.

Exact target rows, ancestral rows, membership and live UniProt entry audit are preserved in [A0BFB4-placement-evidence.json](A0BFB4-placement-evidence.json). The actual tree lineage, response hash and independent live InterPro check are preserved in [root's detailed snapshot](../../../projects/TREEGRAFTER/rereview-2026-09-20/a0bfb4-paint-classification-check.json). Local sources are `.cache/panther/gene_association.paint_uniprot.gaf.gz`, `interpro/panther/PTHR24348/PTHR24348-paint.tsv`, and `interpro/panther/panther-members.tsv`. The current UniProt source is [A0BFB4 JSON](https://rest.uniprot.org/uniprotkb/A0BFB4.json). Initial tree GET requests returned HTTP403; the subsequent POST succeeded and supplied the inspected topology.

## 2026-10-10 addendum

The tree-lineage conclusion still holds: A0BFB4 is a descendant of the PTHR24348
Atg1/ULK-bearing ancestral node, so the autophagy rows are not explained by a
wrong target leaf or by donor-count weakness. A focused follow-up added
target-relevant ciliate evidence that was not incorporated above. Aslan et al.
(PMID:28123910) surveyed ciliate autophagy genes, explicitly including
Paramecium tetraurelia, and found that ciliates lack typical Atg1 proteins and
the corresponding Atg1-complex partners. The OpenScientist structural review also
found that A0BFB4 is a compact kinase-domain protein without the C-terminal
Atg1/ULK partner-binding module.

That evidence supersedes this note's earlier acceptance of the four
Atg1-complex BP/CC terms. Descent from the autophagy-bearing ancestor remains
verified and supports the kinase-domain inheritance, but GO:0000045, GO:0000407,
and GO:0005776 now look over-propagated for this ciliate target. GO:0010506 is
broader and remains unresolved pending Paramecium-specific evidence for or
against a noncanonical autophagy-regulatory role.
