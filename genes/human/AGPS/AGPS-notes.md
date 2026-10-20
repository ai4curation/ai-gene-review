# AGPS (alkylglycerone phosphate synthase) — review notes

UniProt: O00116 (ADAS_HUMAN). Gene: AGPS (a.k.a. AAG5, "aging-associated gene 5").
658 aa precursor; peroxisomal. EC 2.5.1.26.

The seed-era notes below are retained as history. Their donor-species descriptions and curation decisions are superseded by [the substantive re-review](#substantive-re-review-2026-09-26), including the correction of P97275 to guinea pig and the withdrawal of the mitochondrial-contamination assertion.

## Core biology (from local UniProt O00116 and cited primary literature)

- **Enzyme / reaction.** AGPS is alkyldihydroxyacetonephosphate synthase (alkyl-DHAP synthase / alkylglycerone-phosphate synthase). It catalyzes the committed **ether-bond-forming** step of ether-lipid (plasmalogen) biosynthesis: it exchanges the **acyl group of acyl-dihydroxyacetone phosphate (acyl-DHAP) for a long-chain fatty alcohol**, yielding **alkyl-DHAP** (the first O-alkyl ether intermediate) plus the released fatty acid.
  - UniProt FUNCTION: "Catalyzes the exchange of the acyl chain in acyl-dihydroxyacetonephosphate (acyl-DHAP) for a long chain fatty alcohol, yielding the first ether linked intermediate, i.e. alkyl-dihydroxyacetonephosphate (alkyl-DHAP), in the pathway of ether lipid biosynthesis" [file:human/AGPS/AGPS-uniprot.txt].
  - Reaction (Rhea:36171): "a long chain fatty alcohol + a 1-acylglycerone 3-phosphate = a 1-O-alkylglycerone 3-phosphate + a long-chain fatty acid + H(+)"; EC=2.5.1.26 [file:human/AGPS/AGPS-uniprot.txt].
  - [PMID:8399344 "the second enzyme involved in ether phospholipid biosynthesis from dihydroxyacetone phosphate and responsible for glycero-ether bond formation, has been purified from guinea-pig liver."] — original purification (guinea-pig liver ortholog); 65 kDa band, 13,000-fold purification. EC assigned in UniProt with ECO:0000269|PubMed:8399344.
  - [PMID:9553082] — human AGPS characterization; R419H patient mutation abolishes activity ("providing further proof that this substitution is responsible for the inactivity of the enzyme and the phenotype"). Enzyme activity is inhibited by the arginine-modifying agent phenylglyoxal and protected by saturating substrate palmitoyl-DHAP.

- **Cofactor.** FAD-dependent flavoprotein; belongs to the "FAD-binding oxidoreductase/transferase type 4 family" [file:human/AGPS/AGPS-uniprot.txt]. UniProt COFACTOR: Name=FAD (ISS from mouse ortholog P97275). Four FAD-binding regions annotated (residues 234-240, 303-309, 316-319, 368-374). KW: FAD; Flavoprotein.

- **Localization / import.** Peroxisomal enzyme. UniProt SUBCELLULAR LOCATION: "Peroxisome membrane" and "Peroxisome" (ISS from mouse P97275). Imported into peroxisome via a **PTS2** signal in a cleavable N-terminal presequence (TRANSIT 1..58), PEX7-dependent.
  - [PMID:9553082 "Alkyl-dihydroxyacetonephosphate synthase, a peroxisomal enzyme playing a key role in the biosynthesis of ether phospholipids, contains the peroxisomal targeting signal type 2 in a N-terminal cleavable presequence."] Reduced levels in Zellweger/RCDP fibroblasts (defective import → cytoplasmic instability); NALD PTS1-import-deficient patient retains precursor form intraperoxisomally ("in line with an intraperoxisomal localization").
  - [PMID:10415121 "a peroxisomal enzyme involved in the biosynthesis of ether phospholipids, is synthesized with a cleavable N-terminal presequence containing the peroxisomal targeting signal type 2."] The precursor is imported into purified peroxisomes and processed by a cysteine protease (matches Reactome "TYSND1 cleaves peroxisomal proteins"); processing does not change activity. GO CC peroxisome IDA supported here.

- **Quaternary structure / partners.** Homodimer (UniProt SUBUNIT, ISS from P97275). Works together with GNPAT (DHAPAT), which produces acyl-DHAP; GNPAT and AGPS are thought to form a complex on the inner peroxisomal membrane surface. UniProt lists a curated interaction with GORASP1 (Q9BQQ3, GRASP65) with NbExp=7.

- **Disease.** Biallelic AGPS loss-of-function causes **rhizomelic chondrodysplasia punctata type 3 (RCDP3; MIM:600121)** — rhizomelic limb shortening, chondrodysplasia punctata, cataract, severe intellectual disability. Characterized RCDP3 variants: R419H (loss of activity), T309I, L469P, R182Q, E471K, T568M [file:human/AGPS/AGPS-uniprot.txt; PMID:9553082; PMID:11152660; PMID:21990100].

- **Pathway.** UniProt PATHWAY: "Glycerolipid metabolism; ether lipid biosynthesis" (UniPathway UPA00781). Reactome: R-HSA-75896 Plasmalogen biosynthesis.

## GOA annotation review summary (33 annotations)

- **Core molecular function** — GO:0008609 alkylglycerone-phosphate synthase activity: present as IDA (PMID:8399344, PMID:9553082, PMID:10415121), IBA, and IEA. ACCEPT the experimental/IBA; ACCEPT the redundant IEA (own core function, not over-annotation).
- **FAD binding** (GO:0071949 ISS/IEA; GO:0050660 flavin adenine dinucleotide binding IEA): correct cofactor; ACCEPT ISS, KEEP redundant IEA. GO:0050660 is a valid synonym-branch term (parent of GO:0071949) — ACCEPT.
- **catalytic activity** GO:0003824 (IEA, InterPro): correct but uninformative parent of the specific MF → MARK_AS_OVER_ANNOTATED (generic root-ish IEA superseded by GO:0008609).
- **protein binding** GO:0005515 (three IPI, all vs GORASP1/Q9BQQ3, high-throughput Y2H interactome maps PMID:25416956/31515488/32296183): uninformative bare "protein binding"; MARK_AS_OVER_ANNOTATED (policy: never REMOVE an IPI protein-binding). The GORASP1 interaction is real per UniProt INTERACTION record but its biological meaning for AGPS is unclear.
- **Biological process** — GO:0008611 ether lipid biosynthetic process (ISS, IEA): core BP, ACCEPT. GO:0008610 lipid biosynthetic process (IBA, IEA InterPro, and IDA PMID:9553082 acts_upstream_of_or_within): correct but general parent of GO:0008611; the IDA/IBA reflect real data → KEEP but the plain "lipid biosynthetic process" is less informative than ether lipid biosynthesis → MARK_AS_OVER_ANNOTATED for the generic IEA, KEEP_AS_NON_CORE / MODIFY toward GO:0008611 for the experimental ones. Chose: IBA GO:0008610 → MODIFY to GO:0008611; IEA GO:0008610 → MARK_AS_OVER_ANNOTATED; IDA GO:0008610 (acts_upstream_of_or_within, PMID:9553082) → MODIFY to GO:0008611 (paper is about ether phospholipid biosynthesis specifically).
- **Cellular component** — peroxisome GO:0005777 (IDA PMID:10415121, IDA PMID:9553082, IDA HPA GO_REF:0000052, IBA, ISS, IEA), peroxisomal matrix GO:0005782 (Reactome TAS x3), peroxisomal membrane GO:0005778 (ISS, IEA, HDA PMID:21525035): all correct peroxisomal localization. ACCEPT experimental/IBA/matrix; KEEP redundant IEA. Peroxisomal matrix is the best (most specific, mature-enzyme) location; membrane association reflects the GNPAT/AGPS complex on the inner membrane surface.
- **cytosol** GO:0005829 (Reactome TAS R-HSA-9033232, R-HSA-9033514): reflects the transient PTS2/PEX7 cytosolic import stage before peroxisomal import, not the functional steady-state location → KEEP_AS_NON_CORE.
- **membrane** GO:0016020 (HDA PMID:19946888, NK-cell membrane proteome): generic; over-annotation from a proteomic membrane prep → MARK_AS_OVER_ANNOTATED.
- **mitochondrion** GO:0005739 (HDA PMID:20833797, muscle mitochondrial phosphoproteome): AGPS is peroxisomal; this is a common contaminant in mitochondrial fraction proteomics (co-purifying peroxisomes). Experimental HDA so not REMOVE → MARK_AS_OVER_ANNOTATED.

## Core functions chosen

1. MF GO:0008609 alkylglycerone-phosphate synthase activity (directly_involved_in GO:0008611 ether lipid biosynthetic process; location GO:0005782 peroxisomal matrix).
2. MF GO:0071949 FAD binding (cofactor required for catalysis).
</content>
</invoke>

## Substantive re-review, 2026-09-26

This section supersedes the curation judgments and donor-species descriptions above. The original notes remain as session history. All 33 original annotation objects, including evidence codes, references and qualifiers, are preserved. No new annotation is added. The final decisions are 27 ACCEPT, two KEEP_AS_NON_CORE (cytosolic import stages), three REMOVE (uninformative generic protein binding) and one UNDECIDED (mitochondrial detection). One integrated ether-bond-forming catalytic core replaces the two overlapping enzyme/cofactor cores.

### Identity and baseline

Human AGPS is HGNC:327, NCBI Gene 8540 and UniProt O00116. Primary identity records: [NCBI Gene](https://www.ncbi.nlm.nih.gov/gene/8540/) and [ClinGen](https://search.clinicalgenome.org/kb/genes/HGNC%3A327). Aliases checked include ADAS, ADPS, ADHAPS, ADAP-S, ALDHPSY and RCDP3, with historical ORF name AAG5. No competing human directory was found. The coordinator verified all five existing AGPS file blobs against main `a18dacfd84f4b1a18c864a145a88772e475091bd` and found no open canonical/alias PR overlap before authoring. The actual seed status was INITIALIZED, with 33 annotations and 20 references.

### Source audit and biological decisions

- **Donor identity:** P97275 is **guinea-pig (Cavia porcellus) AGPS**, not mouse. [NCBI Gene 100734021](https://www.ncbi.nlm.nih.gov/gene/100734021) and [RCSB 4BBY](https://www.rcsb.org/structure/4BBY) verify the identity. The latter maps the protein and bound FAD to PMID:23112191. Mouse Q8C0I1 occurs separately in the human UniProt record as the source of an additional acyl-exchange reaction; it is not substituted for the actual ISS donor. The historical donor GO rows were not independently reconstructed, but primary guinea-pig biochemical/structural evidence positively supports the transferred functions.
- **Catalysis and species scope:** PMID:8399344 is the original native guinea-pig liver purification, including extraction from a peroxisome-enriched membrane fraction. Its source IDA annotation remains intact, while the rationale identifies the ortholog scope. Human wild-type versus R419H recombinant assays in PMID:9553082 independently establish the human reaction. These are biochemical observations, not an inference solely from disease. PMID:10415121 directly imports human precursor into purified peroxisomes and measures activity before/after processing. Its cached statement, "Processing of alkyl-dihydroxyacetonephosphate synthase did not increase the activity of the enzyme", prevents treating targeting-sequence cleavage as obligatory activation. That paper characterizes a cysteine protease but does not itself identify TYSND1 by name.
- **FAD mechanism:** PMID:10692424, *Alkyl-dihydroxyacetonephosphate synthase. Presence and role of flavin adenine dinucleotide*, was checked through the [primary PubMed abstract](https://pubmed.ncbi.nlm.nih.gov/10692424/). It establishes the cofactor experimentally, but its historical reduction/reoxidation interpretation is not used as the final catalytic model. Later [primary full text, PMID:23112191](https://pmc.ncbi.nlm.nih.gov/articles/PMC3503197/) was read through the Results, Discussion and main Methods. The guinea-pig structure and flavin-analog experiments support covalent catalysis using oxidized FAD with no net substrate redox. Detailed supplementary methods were not read. FAD binding is incorporated into the enzyme core, without adding an oxidoreductase function. The live AmiGO definitions distinguish [GO:0050660](https://amigo.geneontology.org/amigo/term/GO:0050660), which includes different FAD oxidation states, from oxidized [GO:0071949](https://amigo.geneontology.org/amigo/term/GO:0071949); they are not exact synonyms. [GO:0008609](https://amigo.geneontology.org/amigo/term/GO:0008609) specifies the actual acyl/alkyl exchange.
- **Peroxisomal compartments:** Peroxisomal matrix access and luminal membrane association are compatible; matrix is not a universal specificity improvement over membrane. The [primary Wiley abstract, PMID:21990100](https://onlinelibrary.wiley.com/doi/10.1002/humu.21623), explicitly places the AGPS/GNPAT partnership at the luminal membrane surface. Its full Results were not read, and proposed substrate channeling is not promoted to an independently demonstrated molecular function. Native ortholog membrane extraction, direct human import, HPA curation and the source-specific Reactome events support the retained compartments. The 19946888 YTS-cell membrane HDA remains at the original broad membrane resolution; the individual supplemental AGPS hit was not recovered. The 21525035 PEX14-complex HDA is retained with independent localization support and curator deference; its AGPS mass-spectrometry entry was not recovered, and PEX14-specific tubulin/motility functions are not transferred.
- **Mitochondrial uncertainty:** PMID:20833797's local metadata says full text is available, but its extraction contains the abstract and Discussion and omits the AGPS result/supplement. Limited primary PMC Results text confirms functional respiration controls for the isolated human muscle mitochondria. It does not resolve the AGPS peptide identity or residence. Subsequent full/supplement retrieval returned CAPTCHA/internal errors. The localization is therefore UNDECIDED. Neither contamination nor absence of a mitochondrial pool is asserted; the older notes' contamination conclusion is withdrawn.
- **Import stages and reaction roles:** The four cached Reactome entries were read. R-HSA-9033232 and R-HSA-9033514 support cytosolic precursor recognition/translocation, retained as non-core localization. AGPS is cargo, so no protein-import process is newly assigned. R-HSA-390427 is AGPS catalysis; R-HSA-75879 is GNPAT catalysis in an AGPS-containing complex and does not give AGPS the GNPAT reaction.
- **Generic interactions:** The cached study frameworks for PMID:25416956, PMID:31515488 and PMID:32296183 were read, and the GOA/UniProt AGPS–GORASP1 partner was traced. Individual supplementary pair/variant records were not reconstructed. Remove generic GO:0005515 as uninformative without declaring the interaction false or inventing an adaptor function. The older notes' blanket rule against removing IPI terms is superseded.
- **Broad terms and propagation:** Lipid biosynthesis and catalytic activity remain accurate at their source breadth; their existing specific descendants do not make the parent assertions biologically false. PAINT PTHR46568 was read: all three relevant IBDs reside at PTN000922550. The lipid-biosynthesis IBD has human O00116 as its sole seed, which is legitimate experimental grounding, not circularity. Source reviews use that ancestral node. InterPro and ARBA identifiers were traced, but uninspected rule internals remain UNRESOLVED within otherwise biologically accepted assertions. Rhea/EC/UniPathway/subcellular mappings were compared with the cached human entry and the live reaction definition. The GO-CAM index had no matching human/queried donor activity; no process gap is inferred from that absence.
- **Disease scope:** The existing notes also cite cached PMID:11152660. Its abstract links deficient ether-lipid synthesis to altered membrane structure and trafficking. These downstream phenotypes do not establish an additional direct AGPS trafficking function. The AGPS-specific disease summary is grounded in the human enzyme/variant study, cached UniProt and the verified primary PMID:21990100 abstract; it does not conflate AGPS deficiency (RCDP3) with PEX7 deficiency (RCDP1).

### Research execution, source availability and publication gates

The required fresh Falcon command with `--fallback perplexity-lite` ran concurrently with publication caching, using task-specific writable UV directories. Both provider attempts failed during `uvx deep-research-client` dependency resolution because PyPI DNS could not resolve; no provider request or report was produced. Log: `/tmp/AGPS-fresh-research.log`. Manual research in these notes is not a provider artifact. All nine original GOA PMIDs were already cached (`/tmp/AGPS-fetch-pmids.log`). Normal fetches for PMID:21990100 and for PMID:10692424/PMID:23112191 each returned `nodename nor servname provided, or not known`, caching zero papers. No cached source was hand-written or edited.

The notes-inclusive citation census is **13 PMIDs, 10 cached, three missing**: **PMID:10692424, PMID:21990100 and PMID:23112191**. The two latter papers are added to the YAML reference list with explicit primary verification/access scope; the earlier cofactor paper remains a notes-level historical source. All three are publication draft gates until normal caching succeeds. Local `full_text_unavailable` flags follow actual cache metadata: false for the four original caches carrying full-text sections (20833797, 25416956, 31515488, 32296183), with partial extraction limits explicit; true for original abstract-only caches and the two uncached YAML papers even where full text was externally read.

The authored review is **DRAFT**, with all annotations adjudicated and no PENDING rows, because the required publication caches remain unavailable. Targeted validation passes with a reference-fetch warning for the two uncached YAML papers; the notes-only historical paper remains an additional publication gate. History validation and rendering pass. Source integrity checks preserve all 33 original assertion objects, all 20 original reference identities and the exact downloaded UniProt/GOA bytes. There are no new molecular/process annotations and no changes to publication or Reactome source objects. The final session receipt records the independent review and refreshed checks.

Independent annotation-reviewer audit by `annotation_a4galt` read all 33 decisions, the integrated core, all 23 reference assessments and these notes, and found no biological blocker. The reviewer independently checked the baseline/source preservation, RCSB donor/FAD identity, primary flavin chemistry and exact new quote, human active-precursor assays, and the Wiley luminal-membrane context. The mitochondrial gene-level supplement remained unrecovered in that audit as well; the reviewer agreed with the bounded UNDECIDED decision.


## 2026-09-27: PR 3209 source and precision follow-up

Compared canonical files byte-for-byte with published head `3b88baf9e391c4a6d698e88e14ffeaf5f239c809` before editing. All 33 source assertions and 23 reference identities remain preserved. The one action change refines root MF GO:0003824 to the already established GO:0008609 synthase reaction, using the human recombinant-enzyme evidence in PMID:9553082. The [live GO definition](https://amigo.geneontology.org/amigo/term/GO:0008609) specifies acyl-to-alkyl exchange with a long-chain alcohol. This is molecular-function precision, not a second activity. Final actions: **26 ACCEPT, 2 KEEP_AS_NON_CORE, 1 MODIFY, 3 REMOVE, 1 UNDECIDED**.

Broad lipid-biosynthesis assertions describe the actual ether-bond-forming step, and FAD binding is essential to that step. Their omission as separate entries from the integrated core does not make them secondary or excessive. No parent/child NEW annotations are added. The three uninformative protein-binding annotations remain REMOVE under the annotation-reviewer default; this does not deny the interactions. UNDECIDED is the adjudicated outcome for unresolved mitochondrial residence, not an unreviewed PENDING row.

The [original primary PMC3503197](https://pmc.ncbi.nlm.nih.gov/articles/PMC3503197/) abstract and Results were reopened. The core's chemical-trap quotation is verbatim. Results identify guinea-pig enzyme with 93% human sequence identity; human recombinant activity is supported separately by PMID:9553082. The [official PubMed21990100 abstract](https://pubmed.ncbi.nlm.nih.gov/21990100/) confirms citation identity and the patient-cell/PEX7/AGPS context. Neither external read substitutes for missing normal caches. VERIFIED records checked identity and bounded source content, rather than success of the local fetch.

The [official PubMed20833797 record](https://pubmed.ncbi.nlm.nih.gov/20833797/) confirms the title, DOI and human-muscle phosphoproteomics context; reference correctness is now VERIFIED. The AGPS supplemental identification and mitochondrial-residence evidence remain unresolved, so GO:0005739 stays UNDECIDED. True cache full-text-availability metadata is retained separately from incomplete body extraction.

PMID:10415121's abstract distinguishes the **human precursor**, **guinea-pig liver processing fraction**, and separately purified peroxisomes whose species is not given there. The localization rationale and reference assessment now state these boundaries. In-vitro targeting of the human protein is not described as human-cell imaging. Presequence processing still does not activate the enzyme.

Normal caches remain required for **PMID:10692424** (notes), **PMID:21990100**, and **PMID:23112191**. DRAFT and all citation gates remain. No source cache, provider output, published history, Git state or shared project file was manually edited.

Follow-up normal `fetch-pmid` attempt completed: **Cached 0/3**, with DNS resolution errors for every requested PMID. No publication file was generated. The execution log is `/tmp/AGPS-followup-fetch.log`.


## 2026-09-27 normal publication-cache recovery

The two YAML reference gaps (PMID:23112191 and PMID:21990100), plus the
notes-cited mechanistic predecessor PMID:10692424, now have normal fetched
publication records. All three are **abstract-only**. Local
`full_text_unavailable` flags therefore remain true; previously documented
external full-source reading of PMID:23112191 remains separate. Its cached
abstract directly contains the core's chemical-trap quotation. PMID:21990100
still describes substrate channeling as a proposal rather than a separately
established activity. The older PMID:10692424 abstract proposes a redox
intermediate; that historical model remains distinguished from the later
covalent-catalysis evidence and does not change the synthesized mechanism.

These exact records were recovered from standard fetch output in Actions run
36286975328, head 5946477c8ac79ade0709264c775ea1262b108438, artifact
10920674630. The transported ZIP SHA-256 is
`c0ffe4a66b80278af34b44aab6a3ae354ffd5699236b3a486ca95527be5e9713`;
`tmp/verified-reference-records/local-import-receipt.json` records the
per-file hashes. No record was rewritten. The publication manifest includes
only these three AGPS-required cache additions.

All 33 source assertions, all annotation decisions, the integrated core, 23
reference identifiers/titles, downloaded gene sources and prior history are
unchanged. Missing-source status in earlier dated notes is superseded by this
entry. Source availability does not itself establish biological support or
resolve the mitochondrial localization uncertainty. Targeted validation,
rendering and new history validation are recorded in the closure manifest;
COMPLETE requires zero gene validation warnings.
