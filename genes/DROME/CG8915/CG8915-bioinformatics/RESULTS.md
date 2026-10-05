# CG8915 helicase-motif comparison

CG8915/Q9VX63 retains a canonical ATP-binding P-loop and DEAH catalytic motif. It differs from the inactive helicase-like protein Bgcn/Q9W1I2 at both diagnostic regions. This supports a catalytically competent RNA-helicase inference for CG8915, without implying methyladenosine recognition or a meiotic pathway.

Using human YTHDC2/Q9H6S0 as the reference, both MAFFT strategies give:

| Region | Human YTHDC2 | CG8915 | Bgcn control |
|---|---|---|---|
| Motif I | 216–224 GETGSGKTT | 232–240 GATGSGKST | 171–179 AALCWDKSV |
| Motif II | 316–319 DEVH | 333–336 DEAH | 269–272 NDVH |

The whole-protein alignment identities over paired nongap positions are approximately 32.6–32.8% for CG8915 versus human YTHDC2 and 27.0–27.7% for Bgcn versus human YTHDC2. These alignments verify motif conservation; they are not a phylogeny and do not independently settle orthology or all accessory-domain relationships.

## Biological grounding and limitations

Current [FlyBase FBgn0030833](https://flybase.org/reports/FBgn0030833) assigns YTHDC2 as the best bidirectional DIOPT human match (9/14 methods), and the target has an R3H domain, two helicase-core domains, HA2 and an OB fold. The target record does not contain a YTH-domain assignment. [PMID:29033321](https://pubmed.ncbi.nlm.nih.gov/29033321/) directly demonstrates RNA-stimulated ATPase and 3′–5′ RNA-helicase activity for mammalian YTHDC2; the manually transferred FlyBase ISS assertion cites human Q9H6S0. This is conserved-function inference for CG8915, not a target enzymology experiment.

[PMID:29360036](https://pmc.ncbi.nlm.nih.gov/articles/PMC5832417/), [DOI:10.7554/eLife.30919](https://doi.org/10.7554/eLife.30919), discusses divergence of Bgcn and states that Drosophila lacks a more YTHDC2-like version. Its main text does not name CG8915. That taxonomic conclusion cannot be used to equate CG8915 with Bgcn or to import Bgcn's altered motifs: the exact present sequences directly differ at those positions. Reconciling the historical family sampling with current CG8915 orthology would require a broader phylogeny; no such resolution is claimed here.

RNA binding is supported independently of the fine orthology question by the conserved RNA-helicase architecture and R3H domain. The broad ProtNLM nucleic-acid-binding claim remains supported even if future experiments revise the exact ATPase mechanism. No methyladenosine-binding, germline differentiation, nuclear localization or specific transcript is inferred from mammalian YTHDC2 studies.

## Reproduction and controls

Run `just` in this directory with uv and MAFFT 7.526. Python dependencies are locked (Biopython 1.85). `prepare.py` extracts exact benchmark Q9VX63 JSON plus downloaded human YTHDC2 and fly Bgcn Swiss-Prot records. G-INS-i and L-INS-i alignments use `--maxiterate 1000`. `analyze.py` receives reference coordinates explicitly and records site mappings, alignment hashes and paired identities in JSON.

- [x] Scripts accept all paths, identifiers and positions as arguments; conclusions are in this report only.
- [x] Different-gene positive (YTHDC2) and divergent (Bgcn) controls were analyzed with the same scripts.
- [x] Both alignments completed and independently agree on each displayed residue mapping.
- [x] Input FASTA, source records, output alignments, logs and numeric summaries are retained.
- [x] Sequence evidence is distinguished from unmeasured target activity and unresolved detailed phylogeny.

Sources: `../CG8915-uniprot-source.json` from the frozen cohort; [Q9H6S0](https://rest.uniprot.org/uniprotkb/Q9H6S0.txt) and [Q9W1I2](https://rest.uniprot.org/uniprotkb/Q9W1I2.txt), saved as adjacent `CG8915-reference-*-uniprot.txt` files. Human reference positions were taken from the fetched sequence/ATP-binding feature and its DEVH motif.
