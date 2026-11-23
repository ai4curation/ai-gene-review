# motI curation notes

## 2026-11-05

Manual literature review completed after `just deep-research-falcon BACSU motI` returned HTTP 403 (Edison authentication failure). No provider report was fabricated. Full texts of the cited primary studies were read; the original UniProt/GOA records and all seeded annotation payloads were preserved.

### Evidence and decisions

- [PMID:23893111 Functional characterization of core components of the Bacillus subtilis cyclic-di-GMP signaling pathway.](https://pubmed.ncbi.nlm.nih.gov/23893111/): DgrA/YpfA, now MotI, binds c-di-GMP directly. Supporting text: “Thus, YpfA directly interacts with c-di-GMP”
- [PMID:29196522 MotI (DgrA) acts as a molecular clutch on the flagellar stator protein MotA in Bacillus subtilis.](https://pubmed.ncbi.nlm.nih.gov/29196522/): MotI inhibits the motor through a MotA-dependent clutch mechanism. Supporting text: “MotI acts like a molecular clutch on the flagellar motor by interacting with MotA and preventing contact with FliG.” Functional fusions show both cytoplasmic and peripheral membrane pools. Supporting text: “cell membrane-associated puncta stood out over the cytoplasmic haze”
- [PMID:32156823 Cyclic di-GMP Signaling in Bacillus subtilis Is Governed by Direct Interactions of Diguanylate Cyclases and Cognate Receptors.](https://pubmed.ncbi.nlm.nih.gov/32156823/): DgcK and DgcP directly interact with the MotI/DgrA receptor. Supporting text: “Both, DgcK and DgcP interact with DgrA in vitro”

### Strain identity and evidence coding

The reviews identify the UniProt strain-168 protein. The c-di-GMP studies use NCIB 3610 or its derivatives; they are not represented as tests of strain-168 biofilm behavior. To establish protein identity, the full local UniProt sequence was compared by exact equality against every translated CDS from the experimentally relevant strain reference chromosome CP020102.1 (NCIB 3610 comI-Q12L reference; Nye et al., 2017, DOI:10.1128/genomeA.00364-17). The resulting full-length sequence match supports transfer of molecular activity; it does not establish equivalent whole-cell physiology.

- Reviewed accession: P38491
- Length: 217 amino acids
- Sequence SHA-256: `383ccd832e5703f732752282241784e3b97125dd59636033d4d5da0f8d216ab0`
- Exact matched source header: `lcl|CP020102.1_prot_AQZ91192.1_2398 [gene=dgrA] [locus_tag=B4U62_12435] [protein=flagellar brake protein] [protein_id=AQZ91192.1] [location=complement(2397052..2397705)] [gbkey=CDS]`
- Source URL: https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=CP020102.1&db=nuccore&report=fasta_cds_aa&retmode=text
- Retrieval and comparison date: 2026-11-05. Strip whitespace from the local UniProt sequence after `SQ   SEQUENCE` and before `//`; parse each FASTA record from the source URL, concatenate its sequence lines, compare whole strings and compute SHA-256 over UTF-8 sequence text.

Existing machine-supplied evidence codes remain unchanged. Newly proposed receptor/regulator annotations use ISS for the explicit strain transfer, despite complete sequence identity.

### PAINT check

```text
uv run python -m ai_gene_review.validation.gene_paint_losses BACSU motI
# PAINT losses on the motI (P38491) lineage

- No PANTHER family in motI-uniprot.txt; losses not checked.
```

The name MotI is used because PMID:29196522 renames DgrA to reflect motility inhibition. The mechanism is a MotA clutch; it is not assumed to be identical to the enterobacterial YcgR brake. QuickGO was queried on 2026-11-05: GO:0098772 molecular function regulator activity describes non-covalent regulation of a target; GO:0140659 is explicitly cytoskeletal and is not appropriate for the bacterial flagellar motor. The regulator MF adds the experimentally established output not captured by ligand binding alone. The MotI-delta4 crystallographic construct is an engineered truncation, not a native isoform.


## PR #6062 review follow-up — 2026-11-06

Refined the authored NEW regulatory activity and matching core to GO:0140678 molecular function inhibitor activity. PMID:29196522 directly supports non-covalent MotA inhibition; the sequence-identical NCIB 3610-to-168 transfer remains explicit. Original GOA rows and raw sources are unchanged.
