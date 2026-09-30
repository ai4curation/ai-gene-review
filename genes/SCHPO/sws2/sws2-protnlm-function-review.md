# sws2: ProtNLM2 function-description review

Source: **pre-release `post-processed-2026_02_28k.xml`**, accession `O59772`. The exact entry is preserved in [sws2-protnlm-source.xml](sws2-protnlm-source.xml); all original evidence elements and model scores are retained in [sws2-protnlm-source.json](sws2-protnlm-source.json). This record is currently Swiss-Prot and is absent from the published 26,856-record TrEMBL pilot list. The current public ProtNLM endpoint returns this record; API availability is distinct from membership in the published pilot list. No training-membership inference is made.

## Original paragraph 1

> Located at the top of the head of the 30S subunit, it contacts several helices of the 16S rRNA. In the 70S ribosome it contacts the 23S rRNA (bridge B1a) and protein L5 of the 50S subunit (bridge B1b), connecting the 2 subunits; these bridges are implicated in subunit movement. Contacts the tRNAs in the A and P-sites.

Original evidence key(s): `2`.

| Atomic claim | Assessment | Evidence and limit |
|---|---|---|
| Position at the small-subunit head and RNA binding | CNN for the conserved general role; UNC for the exact target contacts | Sws2 is a supported uS13m protein, whose family has an RNA-binding structural role. The exact target head orientation and contacted helices have not been verified in an S. pombe structure. |
| 16S and 23S rRNA designations | NPI for literal target rRNA identity | The direct S. pombe study PMID:21357609 identifies mitochondrial small and large rRNAs as 15S and 21S, respectively. Assigning literal bacterial 16S/23S rRNAs to Sws2’s native mitochondrial ribosome is incorrect. |
| 30S, 50S and 70S subunit/particle designations | UNC for exact sedimentation values | The target is mitochondrial uS13m. No target sedimentation measurement was inspected that validates these bacterial particle names; the S. cerevisiae 37S/54S/74S assignments are related-species observations. |
| Contacts with 23S rRNA and L5 through bridges B1a and B1b | UNC | The S. cerevisiae structure explicitly lacks bacterial B1a/b bridges (PMID:28154081), so universal uS13 family membership cannot validate the exact bridge assignments. A target or sufficiently conserved fission-yeast structure is missing. This is a concrete counterexample to unconditional transfer, not proof of a missing bridge in S. pombe. |
| Bridges connect subunits and participate in movement | UNC for these specified bridges | Intersubunit contacts and motions are general ribosome properties, but the paragraph specifically assigns this role to the unverified B1a/B1b contacts. Evidence for ribosome membership does not resolve that mechanism. |
| Contacts tRNAs in the A and P sites | UNC | The target’s exact tRNA contacts and conformational states have not been established from the available evidence. Conserved ribosomal function alone is insufficient to validate both specified contacts. |

## Primary evidence

- [PMID:21357609](https://pubmed.ncbi.nlm.nih.gov/21357609/) establishes the target organism’s mitochondrial rRNA identities.
- [PMID:28154081](https://pubmed.ncbi.nlm.nih.gov/28154081/) (cached as `publications/PMID_28154081.md`).
- [PMID:18245278](https://pubmed.ncbi.nlm.nih.gov/18245278/) (cached as `publications/PMID_18245278.md`).
- [PMID:16823372](https://pubmed.ncbi.nlm.nih.gov/16823372/) (cached as `publications/PMID_16823372.md`).

Family and feature provenance: [sws2-uniprot.txt](sws2-uniprot.txt).

Decisive counterexample to blanket bacterial transfer, PMID:28154081: “Most of the bridges present in the bacterial ribosome, with the exception of bridges B1a/b and B4, are also present in the yeast mitoribosome (fig. S9).” The yeast in this structural study is S. cerevisiae.

Target rRNA identity, PMID:21357609: “Transcripts were detected for the mitochondrial large (21S) and small (15S) ribosomal RNAs”. The paper studies S. pombe; this supports the rRNA-specific judgment independently of budding-yeast structure transfer.
