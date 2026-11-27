# Fbxo42 (Q9W281): evidence and ProtNLM claim review

Fbxo42 is the substrate-recognizing F-box subunit of an SCF ubiquitin ligase. In Drosophila oocytes, SCF-Fbxo42 downregulates the PP2A-B56 phosphatase subunit and promotes assembly and maintenance of the synaptonemal complex. Its F-box and kelch-like architecture support substrate recognition and complex assembly rather than intrinsic ubiquitin transfer.

Exact input: [Q9W281](https://www.uniprot.org/uniprotkb/Q9W281/entry), 667 residues. The accession was fetched explicitly with the gene-directory alias; no canonical-sequence substitution is made.

Raw emitted predictions: [Fbxo42-predictions-source.json](Fbxo42-predictions-source.json). Source features: [Fbxo42-uniprot.txt](Fbxo42-uniprot.txt), with an exact extraction in [Fbxo42-sequence-evidence.json](Fbxo42-sequence-evidence.json).

## Sequence and domain evidence

These are sequence/domain observations or explicitly named feature predictions, not measurements of biological function. ARBA assertions and ProtNLM-derived UniProt names are not counted as validation.

```text
DR   InterPro; IPR036047; F-box-like_dom_sf.
DR   InterPro; IPR001810; F-box_dom.
DR   InterPro; IPR052821; F-box_only_SRC.
DR   InterPro; IPR015915; Kelch-typ_b-propeller.
FT   DOMAIN          21..70
FT                   /note="F-box"
FT                   /evidence="ECO:0000259|PROSITE:PS50181"
```

## ProtNLM claims

The snapshot emits names and location/keyword statements, with no GO or EC prediction for this target. Each actual statement is assessed below; no GO term has been substituted for it. Categories follow the function-prediction rubric, with nonspecific “uncharacterized” names marked UNC because they contain no testable function. CNN records an independently supported existing annotation; it does not assert a particular training-set composition.

| Kind | Verbatim emitted statement | Assessment | Evidence and limitation |
|---|---|---|---|
| Name | F-box domain-containing protein | CNN | The F-box at residues 21-70 is independently supported by IPR001810, and PMID:33382409 directly establishes an SCF-Fbxo42 complex. The architecture name is correct but less informative than the known substrate-adaptor function. |
| Location | Nucleus (SL-0191) | UNC | A role in nuclear meiotic chromosome organization does not by itself establish nuclear localization of the adaptor. The inspected experiments establish SCF association and a PP2A-B56-dependent phenotype; direct localization of Fbxo42 to nuclei is needed to resolve this claim. |

## Literature evidence

- [PMID:33382409](https://pubmed.ncbi.nlm.nih.gov/33382409/): “Our biochemical and genetic evidence suggests that Fbxo42 promotes synaptonemal complex assembly by negatively controlling the level of the protein phosphatase PP2A-B56.”

## Annotation decisions

- GO:0019005 SCF ubiquitin ligase complex (IBA): **ACCEPT**. PMID:33382409 identifies Fbxo42 as an SCF substrate-recognition subunit; the IBA is concordant with direct target evidence and is not circular.
- GO:0019005 SCF ubiquitin ligase complex (IDA): **ACCEPT**. Biochemical interaction and genetic analyses in PMID:33382409 establish the Fbxo42 SCF complex in Drosophila ovaries.
- GO:0019005 SCF ubiquitin ligase complex (ISM): **ACCEPT**. The independent F-box domain at residues 21-70 and direct complex evidence in PMID:33382409 support the computational annotation.
- GO:0031146 SCF-dependent proteasomal ubiquitin-dependent protein catabolic process (ISM): **ACCEPT**. PMID:33382409 shows that SCF-Fbxo42 downregulates PP2A-B56 in the pathway promoting synaptonemal-complex assembly. The protein is the substrate adaptor rather than the catalytic ubiquitin-transfer enzyme.
- GO:1905088 positive regulation of synaptonemal complex assembly (IMP): **ACCEPT**. The full text of PMID:33382409 documents impaired assembly and maintenance after Fbxo42 depletion and connects this phenotype to PP2A-B56 regulation.
- GO:1990756 ubiquitin-like ligase-substrate adaptor activity (IBA): **ACCEPT**. F-box-mediated SCF incorporation and substrate-recognition evidence support the IBA; they do not establish intrinsic ubiquitin ligase catalysis by Fbxo42 alone.
- GO:1990756 ubiquitin-like ligase-substrate adaptor activity (IPI): **ACCEPT**. PMID:33382409 identifies Fbxo42 as a substrate-recognizing SCF subunit and PP2A-B56 as the regulated target. This is more informative than generic protein binding.

## Research provenance

Genuine external literature research is requested through the repository Falcon wrapper, with perplexity-lite configured as fallback. Provider output is retained separately as `Fbxo42-deep-research-<provider>.md`; its source leads are checked against the underlying publications and exact sequence record.

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not consulted for this re-review.

**Identity.** Q9W281 is the sole UniProt entry (unreviewed TrEMBL, 667 aa, 74.4 kDa) for FlyBase FBgn0034704/CG6758. It is the full-length canonical product, not a fragment, isoform or alternative gene model. Its architecture is an N-terminal F-box (21-70, PS50181) followed by a kelch-type beta-propeller (PF13415 Beta-prop_FBX42, IPR015915). PMID:40804044 reports the expected 74.4 kDa band, which is absent in Su226 mutants [PMID:40804044 "The expected size for Fbxo42 is 74,4 kDa."].

**Evolutionary placement.** PANTHER PTHR46432 (F-BOX ONLY PROTEIN 42), subfamily SF1. SF1 also contains human FBXO42 (Q6P3S6), mouse Fbxo42 (Q6PDJ6) and Pongo FBXO42 (interpro/panther/PTHR46432/PTHR46432-entries.csv), so these are 1:1 orthologs [PMID:33382409 "CG6758 is conserved and the orthologue of human Fbxo42"]. Both IBA rows come from PTN002924600, and their WITH/FROM is the fly gene itself, so the clade-level PAINT call was seeded by the fly IDA. The family review interpro/panther/PTHR46432/PTHR46432-review.yaml places Q9W281 in SF1, in agreement with UniProt, so there is no placement disagreement. It does not yet cite PMID:40804044.

**New literature.** The falcon deep-research report built its Ataxin-2/Xbp1 account from an unpublished dissertation and missed PMID:33382409. I found and cached the peer-reviewed version, Santos et al. 2025 Nat Commun (PMID:40804044, full text). Its findings:
- SkpA binds Fbxo42 in a way that depends on the F-box [PMID:40804044 "SkpA co-immunoprecipitates with FLAG-HA-Fbxo42, but not with a deletion of the F-box domain (FLAG-HA-ΔFbxo42)"].
- Ataxin-2 binds Fbxo42 and is ubiquitylated and degraded by the proteasome in a way that depends on Fbxo42 [PMID:40804044 "We conclude that Fbxo42 promotes the degradation of Ataxin-2 by mediating the ubiquitylation of the C244 residue."].
- Under stress, Fbxo42 is recruited to Ataxin-2 granules [PMID:40804044 "Ataxin-2 forms granules that are decorated with Fbxo42 foci"].
- Degrading Ataxin-2 frees Xbp1 mRNA for translation [PMID:40804044 "degradation of Ataxin-2 granules by Fbxo42 is required for the accumulation of Xbp1spliced protein"].

**Decisions.** All 7 GOA rows are ACCEPTed (3 SCF complex, 2 adaptor activity, 1 SCF-dependent proteasomal catabolism, 1 positive regulation of synaptonemal complex assembly). The changes from the earlier review are:
- GO:0031146 is now supported by direct Ataxin-2 evidence, not only by the F-box sequence model.
- Supporting text that was copied identically into every row has been replaced with row-specific quotes.
- The IPI row notes that the Fbxo42 IPs contained the PP2A A and C subunits. Wrd (FBgn0042693) is the curator-recorded partner; I deferred to the curators, who saw the full figures.
- The description now covers both characterised roles (Ataxin-2/UPR in somatic tissues, PP2A-B56/synaptonemal complex in the germline) and expression.
- There are two core functions: the generic SCF adaptor function, and the germline synaptonemal-complex regulation.

**No NEW annotations.** A stress-granule CC and a UPR-regulation BP are raised as suggested_questions instead. The localization is recruitment to the granule surface, not shown constituency. The retinal-degeneration and cell-death readouts are downstream phenotypes in an Xbp1s overexpression model, and the paper itself places Fbxo42 upstream of the apoptotic machinery.

**Relative to review next.** Human FBXO42 (Q6P3S6) is the 1:1 ortholog in the same PANTHER subfamily SF1, and it has no review in the repo (no genes/human/FBXO42). Human literature mentioned in PMID:40804044: "loss of Fbxo42 leads to cell cycle progression delays and aberrant mitosis". Web search also turns up reports of human FBXO42 regulating p53 and PP4; these have not been verified here.

**Modules.** No module includes Fbxo42. Related modules: modules/dmel_scf_slimb_ubiquitin_ligase.yaml (shares the SkpA-Cul1-Roc1a core; SCF-Slimb acts alongside SCF-Fbxo42 in synaptonemal-complex regulation per PMID:33382409) and modules/er_unfolded_protein_response.yaml (pathway context for the Ataxin-2/Xbp1 role).
