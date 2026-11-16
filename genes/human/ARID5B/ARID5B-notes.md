# Curation Notes for Human `ARID5B` (`UniProtKB:Q14865`)

## 1. Gene Identity & Phylogenetic Context (`PANTHER:PTHR13964:SF37`)
- **Organism**: *Homo sapiens* (`NCBITaxon:9606`)
- **HGNC / Gene Symbol**: `HGNC:17362` / `ARID5B` (*AT-rich interactive domain 5B*; aliases `MRF2`, `MRF-2`, `DESRT`).
- **UniProtKB**: `Q14865` (1188 aa, sequence version 3; isoforms `Q14865-1`, `Q14865-2`, `Q14865-3`).
- **PANTHER Family / Subfamily**: `PANTHER:PTHR13964` (`RBP-RELATED`) / `PANTHER:PTHR13964:SF37` (`AT-RICH INTERACTIVE DOMAIN-CONTAINING PROTEIN 5B`).
- **Pivotal PAINT Role**: `UniProtKB:Q14865` is the **sole experimental seed** for `GO:0000976` (`transcription cis-regulatory region binding`) on the Opisthokont root node `PANTHER:PTN000359478`, where it is genuinely valid for the vertebrate ARID5 clade (`SF37` `ARID5B` and `SF25` `ARID5A`) but over-propagated to `SF24`/`SF26`/`SF27` (`PTHR13964-review.yaml` recommends `MOVE_IBD` to `PANTHER:PTN009015192`).

## 2. Structural & Mechanistic Synthesis (`Q14865`, 1188 aa)
1. **Sequence-Specific AT-Rich Cis-Regulatory DNA Recognition (`AATA(C/T)`)**:
   - Whitson et al. 1999 (`PMID:10329386`), Zhu et al. 2001 (`PMID:11478881`), Patsialou et al. 2005 (`PMID:15640446`), and Cai et al. 2007 (`PMID:17407261`, `PDB:2OEH` paramagnetic spin-label NMR complex) established `ARID5B` (`MRF2`) as the archetypal sequence-specific AT-rich DNA-binding ARID protein (`GO:0000976`), recognizing the 5-bp core motif `5'-AATA(C/T)-3'` via Loop L1 phosphate contacts and insertion of Loop L2 / Helix 5 (`386-GSTSAATCTRRHYERL-401`: `Ser387`, `Thr388`, `Ser389`, `Cys393`, `Arg396`, `His397`; `Trp374` anchors Helix 4) into the DNA major groove.
2. **PKA-Activated `PHF2-ARID5B` H3K9me2 Demethylase Coactivator Complex (`Lys336` Switch)**:
   - Baba et al. 2011 (`PMID:21532585`, *Nat Cell Biol*) discovered that JmjC protein `PHF2` (`UniProtKB:O75151`) is catalytically inactive alone until PKA phosphorylation induces its association with `ARID5B`, triggering demethylation of methylated `ARID5B` (`Lys336` in `335-RKTPI-339`) and targeting the `PHF2-ARID5B` holoenzyme to gluconeogenic/fasting hepatic promoters (`Pepck`, `G6pc`) and `FXR` targets to erase repressive `H3K9me2` marks (`GO:0003713`, `GO:0045815`).
   - Hata et al. 2013 (`PMID:24276541`, *Nat Commun*) showed that `ARID5B` physically partners with `SOX9` and recruits `PHF2` to `Col2a1` and `Agc1` promoters to demethylate `H3K9me2` during chondrogenesis and endochondral ossification.
3. **Bimodal Transcriptional Repression & Metabolic / Developmental Functions**:
   - Huang et al. 1996 (`PMID:8649988`) originally identified `MRF` (`ARID5B`/`ARID5A`) in undifferentiated Tera-2 and THP-1 nuclear extracts as an AT-stretch-binding transcriptional repressor of the human cytomegalovirus (`CMV`) major immediate-early enhancer modulator (`GO:0000122`), and high-throughput HDAC interactome proteomics (`PMID:23752268`, `PMID:26496610`, `PMID:28514442`, `PMID:33961781`, `PMID:35271311`, `PMID:40205054`) repeatedly recover `ARID5B` with `HDAC1` (`Q13547`).
   - Whitson et al. 2003 (`PMID:14651970`) and Claussnitzer/Whitson/conditional KO studies (`PMID:33757861`) demonstrated that `Mrf2`/`Arid5b` knockout mice display neonatal mortality, reduced brown/white adipose lipid accumulation, and resistance to diet-induced obesity and hepatic steatosis (`GO:0060612`, `GO:0001889`).

## 3. Audit of `ARID5B-deep-research-affinage.md`
- Frontmatter: `uniprot_accession: Q14865` (matches), `self_evaluation_pairwise: win`, `faith_pct: 100.0`, `citation_count: 23`.
- **Verdict**: `relevance: HIGH`, `correctness: LOW_QUALITY` (2 structured `source_defects` recorded):
  1. **`WRONG_STATEMENT` (`slot: citations`, `requested_change: CHECK`)**: Emits malformed non-PubMed identifier `- PMID:bio_10.1101_2025.10.17.683040` for an unpeer-reviewed bioRxiv preprint and elevates its `ARID5B-MIER1-C16ORF87-HDAC1/2` claim into the headline mechanistic model alongside peer-reviewed discoveries.
  2. **`MISSING_STATEMENT` (`slot: molecular_activity`, `requested_change: ADD`)**: Constrained by `goslim_generic`, emits only coarse `GO:0003677 DNA binding, GO:0140110 transcription regulator activity, GO:0060090 molecular adaptor activity`, omitting both specific `GO:0000976` (`transcription cis-regulatory region binding`) and `GO:0003713` (`transcription coactivator activity`), and omits the foundational discovery of CMV enhancer transcriptional repression (`PMID:8649988`).

## 4. Existing Annotation Decisions
- **`GO:0000976` (`IBA` from `PTN000359478` & `IDA` from `PMID:21532585`), `GO:0003713` (`IDA` from `PMID:21532585`), `GO:0000122` (`IDA` from `PMID:8649988`), `GO:0006357` (`IBA` from `PTN000359478`), `GO:0045815` (`IDA` from `PMID:21532585`), `GO:0005654` (`TAS` x2) -> `ACCEPT`**.
- **`GO:0003677` (`EXP`, `IDA`, `IEA`), `GO:0045892` (`TAS`), `GO:0045893` (`IEA`), `GO:1902494` (`catalytic complex`, `IPI`) -> `TOO_GENERAL`** (subsumed by specific `GO:0000976`, `GO:0000122`, and `GO:0003713`/`GO:0045815`, or `KEEP_AS_NON_CORE` on `GO:1902494` since `PHF2-ARID5B` lacks its own specific GO complex term — YES! `KEEP_AS_NON_CORE` on `GO:1902494` because no more specific `PHF2-ARID5B` complex term is asserted in the review, whereas `TOO_GENERAL` requires a more specific asserted descendant in the same ontology!).
- **7 bare `GO:0005515` (`protein binding`, `IPI`) rows (`PMID:21532585`, `PMID:23752268`, `PMID:26496610`, `PMID:28514442`, `PMID:33961781`, `PMID:35271311`, `PMID:40205054`) -> `REMOVE`** per `protein_binding_policy.py` (uninformative generic protein binding).
- **`GO:0005634` (`IBA`, `IEA`), `GO:0001889` (`liver development`, `TAS`), `GO:0060612` (`adipose tissue development`, `IEA`, `ISS`) -> `KEEP_AS_NON_CORE`**.
