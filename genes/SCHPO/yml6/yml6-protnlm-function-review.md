# yml6: ProtNLM2 function-description review

Source: **pre-release `post-processed-2026_02_28k.xml`**, accession `O74801`. The exact entry is preserved in [yml6-protnlm-source.xml](yml6-protnlm-source.xml); all original evidence elements and model scores are retained in [yml6-protnlm-source.json](yml6-protnlm-source.json). This record is currently Swiss-Prot and is absent from the published 26,856-record TrEMBL pilot list. The current public ProtNLM endpoint returns this record; API availability is distinct from membership in the published pilot list. No training-membership inference is made.

## Original paragraph 1

> One of the primary rRNA binding proteins, this protein initially binds near the 5'-end of the 23S rRNA. It is important during the early stages of 50S assembly. It makes multiple contacts with different domains of the 23S rRNA in the assembled 50S subunit and ribosome.

Original evidence key(s): `2`.

| Atomic claim | Assessment | Evidence and limit |
|---|---|---|
| Primary rRNA-binding structural protein | CNN for RNA interaction; UNC for “primary” assembly class | The supported uL4m family placement and yeast mitoribosome structure establish a conserved RNA-associated ribosomal protein. Whether S. pombe Yml6 qualifies as a primary binder in an assembly hierarchy is not established. |
| Initial binding near the 5′ end of 23S rRNA | UNC | The literal 23S rRNA identity is NPI: the S. pombe mitochondrial LSU contains 21S rRNA (PMID:21357609). The homologous rRNA region and temporal order of Yml6 binding remain UNC. |
| Important during early 50S assembly | UNC | Mitochondrial LSU assembly uses lineage-specific protein clusters (PMID:29514071). The general requirement for ribosomal proteins does not establish Yml6’s exact early assembly stage, and the bacterial 50S designation should not be transplanted without target evidence. |
| Multiple contacts with domains of 23S rRNA in the assembled subunit | CNN for RNA-associated structural role; UNC for the exact stated geometry | The conserved mitochondrial uL4 role is established, but the number/domain identity of S. pombe rRNA contacts is unverified. The literal 23S identity is incorrect for its native mitochondrial 21S rRNA (PMID:21357609). |

## Original paragraph 2

> Forms part of the polypeptide exit tunnel.

Original evidence key(s): `3`.

| Atomic claim | Assessment | Evidence and limit |
|---|---|---|
| Forms part of the polypeptide exit tunnel | CNN | The characterized S. cerevisiae mitochondrial LSU retains the uL4/uL22 tunnel constriction (PMID:24675956). S. pombe Yml6 has the diagnostic uL4 family domain and is assigned to the mitochondrial LSU. Transfer of this deeply conserved uL4 structural feature is justified despite species-specific remodeling farther along the tunnel. This is a supported family inference, not a target structure, and the known conserved role is not a novel discovery. |

## Primary evidence

- [PMID:21357609](https://pubmed.ncbi.nlm.nih.gov/21357609/) establishes the target organism’s mitochondrial rRNA identities.
- [PMID:24675956](https://pubmed.ncbi.nlm.nih.gov/24675956/) (cached as `publications/PMID_24675956.md`).
- [PMID:28154081](https://pubmed.ncbi.nlm.nih.gov/28154081/) (cached as `publications/PMID_28154081.md`).
- [PMID:29514071](https://pubmed.ncbi.nlm.nih.gov/29514071/) (cached as `publications/PMID_29514071.md`).

Family and feature provenance: [yml6-uniprot.txt](yml6-uniprot.txt).

Decisive excerpt, PMID:24675956: “Beyond the entrance, the tunnel is lined by conserved elements (Fig. 6C), including the constriction site formed by uL22 and uL4.”

Target rRNA identity, PMID:21357609: “Transcripts were detected for the mitochondrial large (21S) and small (15S) ribosomal RNAs”. The paper studies S. pombe; this supports the rRNA-specific judgment independently of budding-yeast structure transfer.

Target-specific context: [PMID:34119521](https://pubmed.ncbi.nlm.nih.gov/34119521/) reports low-level Yml6 recovery among Ppr10-copurified mitoribosomal proteins (Figure 4A/Table S2). This supports mitochondrial translation-machinery association without determining Yml6’s rRNA contacts or assembly timing. The associated correction changes funding information only.
