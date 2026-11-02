# DNAJC19 (TIM14 / TIMM14) research notes

## Identity
- UniProt Q96DA6, TIM14_HUMAN, "Mitochondrial import inner membrane translocase subunit TIM14"; DnaJ homolog subfamily C member 19. 116 aa.
- HGNC:30528. Chromosome 3. Belongs to the TIM14 family.
- Topology: short intermembrane-space N-terminus (2-3), single transmembrane helix (4-24), then matrix-side J-domain (62-116). So a single-pass inner-membrane protein with its catalytic J-domain projecting into the matrix.

## Core function
- J-domain co-chaperone of the mitochondrial presequence translocase-associated import motor (PAM), the matrix-side motor of the TIM23 complex.
- Stimulates the ATPase activity of mitochondrial HSP70 (mortalin/HSPA9) to drive ATP-dependent import of presequence-bearing precursor proteins across the inner membrane into the matrix.
- [PMID:19564938 "J-domain containing proteins, DnaJs, usually enhance the ATPase activity of Hsp70 chaperones. Such enhancement of the ATPase activity is required for promoting the tight binding of unfolded substrate proteins to the peptide-binding pocket of mtHsp70. The latter role is played by the membrane-bound J-domain-containing protein named Tim14/Pam18"]
- Human DNAJC19 directly stimulates human mtHSP70 (Mortalin) ATPase activity; this is antagonized by Magmas/PAM16 [PMID:20053669 "we have observed upto 70% reduction in ATPase stimulating activity of human Mortalin by Magmas:DnaJC19 complex"].

## Partner / complex
- Forms a stable heterodimeric subcomplex with Magmas (PAM16/TIMM16) through their related J/J-like domains; this is the regulatory module of the import motor. Demonstrated in human mitochondria by reciprocal coIP.
- [PMID:20053669 "Magmas forms a stable subcomplex with J-protein Pam18 or DnaJC19 through its C-terminal region and is tethered to TIM23 complex of yeast and humans"]
- [PMID:20053669 "equivalent amounts of co-precipitation of Magmas with DnaJC19 (yPam18 ortholog) supports the existence of a similar subcomplex in humans"]
- Part of the human TIM23 translocon: co-IP with Tim17 pulls down hTim44, hTim23, DnaJC19, Magmas [PMID:20053669 "Pull down of Magmas along with other translocon components such as hTim44, hTim23, DnaJC19 provides direct evidence for the association of Magmas with the human translocon"].
- Human Tim14/Pam18 (DNAJC19) and human Tim16/Pam16 form hetero-oligomers and bind yeast mtHsp70 [PMID:19564938 "the soluble domains of the human Tim14/Pam18 and Tim16/Pam16 proteins interact with their yeast counterparts, forming heterodimeric complexes and that these complexes interact with yeast mtHsp70"].
- UniProt SUBUNIT: interacts with PHB2 (associates DNAJC19 with prohibitin complex) and with TIMM16/PAM16; may be component of PAM complex (mtHSP70, GRPEL1/2, TIMM44, TIMM16, TIMM14). (By similarity.)

## Localization
- Mitochondrion inner membrane, single-pass, matrix side [UniProt SUBCELLULAR LOCATION]. Confirmed in human heart mito proteome [PMID:12592411] and human mito proteome [PMID:34800366].

## Second function (cardiolipin)
- UniProt FUNCTION (by similarity): "forms a complex with prohibitins to regulate cardiolipin remodeling." Underlies the 3-methylglutaconic aciduria / DCMA phenotype (a cardiolipin/Barth-like syndrome). This is ISS/by-similarity, kept as non-core but plausible.

## Disease
- DCMA syndrome = dilated cardiomyopathy with ataxia = 3-methylglutaconic aciduria type 5 (MGCA5), autosomal recessive [PMID:16055927]. Also testicular dysgenesis (genitalia development), optic features. The IMP annotations to "genitalia development" and "visual perception" derive from the human disease phenotype description.

## Annotation review reasoning
- Core MF: GO:0001671 ATPase activator activity (stimulates mtHSP70) - ACCEPT, directly demonstrated for human protein.
- Core BP: GO:0030150 protein import into mitochondrial matrix - ACCEPT.
- Core CC: PAM complex (GO:0001405) and mitochondrial inner membrane / matrix side - ACCEPT.
- TIM23 translocase complex (GO:0005744) part_of - ACCEPT, human translocon coIP.
- Cardiolipin regulation (GO:1900208) ISS/IEA - KEEP_AS_NON_CORE (by similarity, disease-relevant but secondary).
- protein binding GO:0005515 IPI with Q9Y3D7 (=PAM16/Magmas) - KEEP_AS_NON_CORE (real interaction, uninformative term; informative is the J-domain/ATPase module).
- protein-containing complex GO:0032991 IDA - KEEP_AS_NON_CORE (generic, real but redundant with PAM/TIM23 complex).
- mitochondrion GO:0005739 IDA/HTP - ACCEPT (less specific than inner membrane but correct).
- membrane GO:0016020 NAS - KEEP_AS_NON_CORE (generic).
- intracellular protein transport GO:0006886 NAS - KEEP_AS_NON_CORE (generic parent of import into matrix).
- Note: genitalia development / visual perception IMP terms are in the DR/UniProt GO set but NOT in the GOA tsv stub, so not reviewed here.


## 2026-10-17 ClinGen augmentation — superseding evidence and source notes

This dated appendix preserves the earlier notes above as historical text. The current review has 23 rows (11 ACCEPT, 6 KEEP_AS_NON_CORE and 6 MODIFY), one integrated import core, two annotated sequence products and no authored NEW annotation. The [evidence guide](DNAJC19-evidence-guide.md) gives public original/supplement locators and access limits.

The two prior ATPase-activator core blocks describe the same mechanism and are consolidated. PMID:20053669 Figure 9B and the purified-protein Methods directly demonstrate human DNAJC19 stimulation of human Mortalin. Magmas attenuates that stimulation; the older generated PN note's approximately 70% stimulation wording reverses the reported effect of the Magmas:DNAJC19 complex. PMID:19564938 Results 2.1–2.2 establishes human soluble heterodimer biophysics, but its ATPase experiment uses yeast Pam18 and yeast mtHsp70. Import-kinetics experiments in PMID:20053669 concern Magmas mutants in yeast. These assay boundaries supersede broader wording in the historical notes without changing the positive import-associated conclusion.

The two literal PAM16-binding annotations remain positive and non-core under the explicit [project binding instruction](https://github.com/ai4curation/ai-gene-review/blob/864cafe6233e8f9ba6edf74a76c053bc31f6c4cf/projects/CLINGEN_MENDELIAN.md#curation-instructions). Their partner is not Mortalin; no ATPase activity or substrate-binding chaperone class is assigned to PAM16 from this interaction alone. Six broad location, complex and transport assertions receive supported specific replacements, with the original assay resolution kept explicit.

PMID:24856930 has positive primary abstract evidence for a prohibitin-associated DNAJC19 pool and cardiolipin regulation, with direct experimental mouse donor annotations. This is more than a similarity-only biological conjecture. Its full Methods remain inaccessible, so the retained non-core assertions do not specify unverified source constructs, stable stoichiometry, lipid catalysis or a second settled human core. The broad prohibitin-context complex assertions are not exchanged for the separate PAM complex claim.

PMID:16055927 is now verified against the separately recovered full PMC original, although its protected cache stays abstract-only. The disease-associated predicted 47-residue truncation differs from the natural 91-residue splice product. Official products reconstruct to 116 and 91 residues; the latter deletes residues 1–25, including the predicted membrane anchor, without establishing inactivity. The engineered 24–116 protein is distinct again. The 2003 proteome's GI 16307227 maps exactly to human AAH09702.1/DNAJC19. The 2021 MitoCoP Table S1 group 9092 verifies the target but groups Q96DA6 and Q96DA6-2 and does not establish isoform-specific topology.

The genuine current GOA replaces the historical GO_REF:0000120 source with GO_REF:0000044 for the same inner-membrane IEA assertion. The [old GOA snapshot](source-snapshots/DNAJC19-goa-before-5157.tsv) and [provenance record](source-snapshots/DNAJC19-goa-refresh-20261017.yaml) preserve the exact original bytes and fetch origin. Historical row index 3 retains ACCEPT and all original source fields, adding only `retired: true`; a genuine current row is appended with ACCEPT. The other 21 historical dictionaries stay unchanged. This records a replaced source assertion without rejecting its biology or manufacturing NEW coverage.

The previous review's remote path history identifies #1434 creation and #1492 update; #3214 was only a shallow local history boundary. The configured Falcon research attempt and perplexity-lite fallback failed authentication/quota, respectively. No provider content was fabricated. The original notes prefix, generated PN notes, existing publication caches and downloaded UniProt record remain intact. No new verbatim quotations are added; exact public article sections provide source provenance.


## 2026-10-17: primary evidence anchors and source support

The review now includes short primary-source anchors for the human Mortalin/DNAJC19 single-turnover ATPase assay ([PMID:20053669, Figure 9B and accompanying Results](https://pmc.ncbi.nlm.nih.gov/articles/PMC2838536/)), human translocon co-immunoprecipitation (the same paper, Figure 8B), and the reconstituted human co-chaperone heterodimer ([PMID:19564938, Results 2.1](https://pmc.ncbi.nlm.nih.gov/articles/PMC2695266/)). Each new excerpt appears once in the YAML. The purified fragments and the separate yeast ATPase experiments retain their stated scope; these anchors do not establish natural isoform 2 activity or a human membrane-face measurement.

Annotation support now cites the primary publications and original database records directly. The [evidence guide](DNAJC19-evidence-guide.md) remains a locator for Methods, figures, independently recovered supplements and source provenance; it is not an independent experimental source. The accepted historical inner-membrane row now leads with its positive biological support before explaining the source-reference transition. All annotation actions, source dictionaries, products and the single import-associated core are unchanged.

The historical notes above are retained verbatim, including their older excerpts and the preceding qualifications. The new excerpts are budgeted separately from that inherited text and are not repeated here. The exact historical GOA snapshot and its generated provenance record remain in their existing locations; retirement records a source-reference transition rather than loss of the biological localization.

## 2026-10-17 — source-snapshot layout and portable provenance links

The unchanged [historical GOA snapshot](source-snapshots/DNAJC19-goa-before-5157.tsv) and the [YAML source-refresh provenance](source-snapshots/DNAJC19-goa-refresh-20261017.yaml) now reside in `source-snapshots/`, outside the bioinformatics folder, following the CYP7B1 source-refresh layout. The raw snapshot retains its exact bytes and mode. The provenance conversion preserves the original source identifiers, hashes, retrieval timestamps, command, URL caveat and single source-reference transition; only its archive destination changes, with an additive relocation record.

The two earlier snapshot/provenance link destinations have been corrected; all other original notes text remains unchanged. The prior statement that the artifacts remained in their existing locations describes the previous layout and is superseded by this appendix. The original absolute command paths remain a historical execution receipt, while the live paths in the YAML are portable relative links. Only the standard [DNAJC19-goa.tsv](DNAJC19-goa.tsv) is the input regenerated by normal fetches. No scientific review field, product, quotation, raw source byte stream, PN note, publication cache or previous history is changed or lost.
