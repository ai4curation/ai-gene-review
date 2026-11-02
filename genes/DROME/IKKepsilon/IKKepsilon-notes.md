# IKKepsilon / Q9V3Y8

Q9V3Y8 is the selected 720-residue IKKepsilon/Ik2 sequence with its kinase domain at residues 12–317. Primary fly studies independently establish Spn-F, Nuf and DIAP1 phosphorylation: [PMID:18796167](https://pubmed.ncbi.nlm.nih.gov/18796167/), [PMID:21316589](https://pubmed.ncbi.nlm.nih.gov/21316589/) and [PMID:16887178](https://pubmed.ncbi.nlm.nih.gov/16887178/). The broad ProtNLM reaction is CNN. Full texts inspected include the Spn-F kinase study, Rab interactome, bristle-localization study and SOP timing study.

[PMID:34965418](https://pubmed.ncbi.nlm.nih.gov/34965418/) full text directly depletes dTBK1/Ik2 in enterocytes and establishes STING-dependent antiviral signaling. The type-I-interferon IBA is nevertheless invalid: [PMID:30119996](https://pubmed.ncbi.nlm.nih.gov/30119996/) explicitly describes flies as devoid of interferons. This distinguishes conserved antiviral pathway activity from a taxon-incompatible downstream response.

The original apoptosis paper remains abstract-only and is not overruled from its nonapoptotic title; the apoptosis annotation is UNDECIDED. By contrast, [PMID:19822670](https://pubmed.ncbi.nlm.nih.gov/19822670/) full text explicitly places the observed Ik2 effect after division and finds no phase-I change, so its SOP-cell-division annotation is overannotated. All 36 GOA rows are retained and reviewed.

## Sequence and research provenance

The selected frozen UniProt record is retained in [IKKepsilon-uniprot-source.json](IKKepsilon-uniprot-source.json), with the complete original prediction metadata in [IKKepsilon-predictions-source.json](IKKepsilon-predictions-source.json). It maps the exact accession to this FlyBase gene; current sequence identity does not establish the historical predictor input. Gene-level experiments support conserved functions unless a relevant isoform difference is established. Falcon research was requested with perplexity-lite fallback alongside publication caching. Primary publications and sequence observations, rather than AI summaries or ARBA assertions, support the curated conclusions.

## Final research readback

The completed Falcon report was inspected. It correctly distinguishes Ik2 from Ird5, but its claim that DIAP1 direct phosphorylation is not established conflicts with the explicit primary PMID:16887178 abstract and later full-paper descriptions. The primary source is retained as the evidential basis. The report also misses the enterocyte-specific dTBK1/STING antiviral mechanism established by full PMID:34965418; the review includes that target-specific evidence.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 files and prediction-evidence folders were not opened or used for this pass.

### Identity of the benchmark accession

- Q9V3Y8 (TrEMBL, unreviewed, PE 1) is the 720-aa FlyBase product of FBgn0086657 shared by isoforms B and C. UniProt has no Swiss-Prot entry for this gene; the other entries are Q7KJQ4 (711 aa, "Protein kinase DIK2", an EMBL submission) and Q86PE7 (720 aa, SD10041p cDNA). Q9V3Y8 is therefore the canonical, full-length product, not a fragment or alternative model.
- Sequence check (scratchpad, regex over the UniProt SQ block): kinase domain 12-317 (PROSITE PS50011), ATP-binding Lys41 in the VAVK motif, catalytic HRD at 136 and DFG at 160 all present. Pfam TBK1_ULD (PF18396) and TBK1_CCD1 (PF18394) are present, i.e. the full TBK1-type architecture.

### Evolutionary placement

- PANTHER PTHR22969 (IKB KINASE), subfamily SF15 "FI05319P" (a fly subfamily). Human TBK1 is SF14 and IKBKE is SF10; fly IKKbeta/ird5 sits with the IKKalpha/beta clade.
- PAINT (interpro/panther/PTHR22969/PTHR22969-paint.tsv): PTN001491808 (taxon 6072, Eumetazoa) carries protein Ser/Thr kinase activity and cytoplasm; PTN000540338 (Bilateria, the TBK1/IKBKE clade) carries GO:0002218 (seeds include FB:FBgn0086657 itself) and GO:0032481 (seeds all vertebrate). PTN000540281 (IKKalpha/beta clade) carries IkappaB kinase activity, IKK complex, NF-kappaB activation; fly IKKbeta inherits those, IKKepsilon does not. So fly IKKepsilon is a co-ortholog of human TBK1 and IKBKE (the duplication is vertebrate-specific); human TBK1 is the closest well-characterised relative. TBK1-specific functions with no IBD (IRF3 phosphorylation, xenophagy) are not transferred.
- The PANTHER family review (interpro/panther/PTHR22969/PTHR22969-review.yaml) lists Q9V3Y8 as the SF15 representative; no disagreement with the UniProt placement.

### Changes made

- 6 GO:0005515 protein binding rows (Spn-F x5, DIAP1 x1): KEEP_AS_NON_CORE/UNDECIDED -> REMOVE under the protein-binding policy. The interactions are real (Spn-F, DIAP1 are substrates/adaptor), and the information is carried by the accepted kinase activity and cytoskeleton/endosome terms.
- GO:0045089 positive regulation of innate immune response (ARBA): ACCEPT -> MODIFY to GO:0002218 (child term, verified via OLS ancestors; already carried by IBA).
- GO:0009967 positive regulation of signal transduction (ARBA): -> MODIFY to GO:0140896 cGAS/STING signaling pathway (component, not generic regulator).
- GO:0010628 positive regulation of gene expression (ARBA): -> MARK_AS_OVER_ANNOTATED (indirect transcriptional output of dSTING signalling).
- GO:0001578 microtubule bundle formation: ACCEPT -> KEEP_AS_NON_CORE (Ik2 is a regulator at the bristle tip, not a bundling protein).
- GO:0035160 maintenance of epithelial integrity, open tracheal system: -> UNDECIDED. The abstract of PMID:16887350 reports branched terminal cells, not loss of integrity; full text not cached, so not overruled.
- GO:0032481 type I IFN production IBA: kept REMOVE; added propagation_review (vertebrate-only seeds, flies lack interferons per PMID:30119996).
- GO:0031267 small GTPase binding: kept non-core; added that the Rab30 interaction is GTP specific (PMID:25453831), and that Ik2/Spn-F puncta are Golgi (not proposed as a new annotation).
- Unchanged: kinase activity (all 4 rows), ATP binding, cytoplasm, cell tip, endocytic recycling, actin terms, antiviral innate immune response and cGAS/STING pathway (PMID:34965418), apoptosis UNDECIDED (abstract stresses nonapoptotic caspase function; full text unavailable), SOP cell division MARK_AS_OVER_ANNOTATED (full text of PMID:19822670 shows no phase-I effect).
- Rewrote description; added a DIAP1-regulation core function, reference_review on all PMIDs, suggested questions/experiment. Status set to COMPLETE.

### Modules

- modules/dmel_cgas_sting_signaling.yaml (IKKepsilon annoton, no activity asserted) and modules/cgas_sting_signaling.yaml (Q9V3Y8 as the fly representative of the TBK1-family kinase role). Both match this review: the shared process is activation of innate immune response / cGAS-STING signalling, with no interferon claim.
