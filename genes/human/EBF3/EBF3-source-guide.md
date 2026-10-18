# EBF3 source guide

The source keys below identify evidence, not independent new experiments. A00–A13 refer to the zero-based order of the 14 imported annotation rows. The [review](EBF3-ai-review.yaml) retains every original source assertion.

| Source key | Rows | Evidence used and limit |
| --- | --- | --- |
| TFCLASS | A00, A03 | Official EBF3 entry 6.1.5.0.3 and the manually evaluated 6.1.5 family; classification evidence, not a localization experiment. |
| PAINT | A01, A02, A06, A10 | Literal IBDs at PTN000844136 and verified target descent; limited current donor-record corroboration. |
| INTERPRO | A04, A05, A09 | Exact current domain/family matches and broad mappings, refined using independent target evidence. |
| SUBCELL | A08 | Official SL-0191 maps to nucleus; independently corroborated by human localization. |
| SLEVEN | A11 | Human EBF3, plasmacytoma Cd79a-linked readout, explicit dose dependence. |
| CHAO | A12 | Untagged human EBF3 in HEK293 reporter; separate tagged fly rescue. |
| HARMS | A07, A13; corroboration elsewhere | Human-cell nuclear/chromatin observations, promoter reporter and target binding/transcription. |
| SIPONEN | Integrated core | Direct EBF3 dimerization-fragment architecture, distinct from EBF1 DBD structural experiments. |

## Primary originals

**SLEVEN — [PMID:28017370](https://pmc.ncbi.nlm.nih.gov/articles/PMC5223060/).** The original Results and Figure 3 caption contain the graded-expression assay, clone IRCMp5012D0321D, tagging and flow-cytometry methods. Figure 4's caption and adjacent text contain the co-IP procedure and positive WT–mutant associations. Selected operative main-text and caption passages were read; no figure pixels or supplement were independently inspected. Surface IgM is the measured Cd79a-linked endpoint. The experiment supports transcriptional activation in its tested dosage range; it does not measure purified DNA affinity or establish native human neuronal target selection. Exact recovered HTML SHA256: `661139cf32cc04af6bdb75fb8e000d49971c7dd5d7194dbb8014f0ca986a25a6`.

**CHAO — [PMID:28017372](https://pmc.ncbi.nlm.nih.gov/articles/PMC5223093/).** Figure 2B's caption and adjacent Results specify untagged human constructs, a six-COE-site NanoLuc reporter in HEK293 cells, firefly normalization and deletion/empty/no-transfection controls. The following fly-rescue section and Figures 3–4 distinguish C-terminal HA constructs from the reporter proteins. Selected operative text/captions were read, without figure-pixel assessment. Exact recovered HTML SHA256: `b63e5cc680207e408f3087e6024c9d2d02b643efce1e1522cccfdd69b2eb900d`.

**HARMS — [PMID:28017373](https://pmc.ncbi.nlm.nih.gov/articles/PMC5223027/).** Operative main-text sections describing FLAG-tagged HEK293T localization, pGL2-p21/CDKN1A transactivation, in situ fractionation and stable SK-N-SH RNA-seq/ChIP-seq were independently read. WT was nuclear in that assay and tightly chromatin associated. Variant effects differed; P177L retained some binding and regulation. Detailed supplemental Methods and figure pixels were not independently assessed. The genuine HTML-derived cache used for this assessment has SHA256 `1b8e9cf0caf15c8bafa608e8f0c716112300ca3cd2ab8cbe2ef3b9af9e11aaf2`; the separate abstract-only version was not substituted for it.

**SIPONEN — [PMID:20592035](https://pmc.ncbi.nlm.nih.gov/articles/PMC2923972/).** Main-text cloning, bacterial protein production/crystallography and domain-results sections distinguish human EBF1 DBD/IPT constructs from EBF3 TIG-HLH/HLHLH constructs. Direct EBF3 fragment structures support a dimeric helical arrangement. EBF1's crystallized zinc-bearing DBD does not establish EBF3 metal occupancy, and suggested DNA docking or additional partner contacts remain models. Genuine XML-derived cache SHA256: `b91d229c6a6f8f0541f4f5cf78a571ac176c857b69176953d893bcaa3c8f37b1`.

Normal caches and actual access are separate facts. SLEVEN and CHAO caches retain `full_text_available: false`; the separately recovered operative originals justify `full_text_unavailable: false` in their authored reference assessments. No downloaded cache text or flag was manually rewritten. All findings here are paraphrases; no new supporting-text excerpt was introduced.

## Products and inference sources

The official products are [Long](https://www.uniprot.org/uniprotkb/Q9H4W6/entry) (596 residues) and Short (551). The recorded Short edits remove Long residues 252–260 and replace 521–558 with MK. The public ENA records [HQ258299](https://www.ebi.ac.uk/ena/browser/view/HQ258299) and [BC130479.1](https://www.ebi.ac.uk/ena/browser/view/BC130479.1), explicitly named in CHAO, both translate exactly to Short. These are deposited-template comparisons, not direct sequencing of the study's physical vials. No current natural-product identity was assigned to the other study constructs solely by name or residue count.

**PAINT.** [Official PANTHER gene information](https://www.pantherdb.org/services/oai/pantherdb/geneinfo?geneInputList=Q9H4W6&organism=9606) assigns EBF3 to PTHR10747:SF4. The current tree has 190 nodes and 98 leaves; its alignment includes 190 extant and ancestral sequences. Human EBF3 is PTN002473388, reached through 14 nodes from PTN000844136. Its ungapped alignment matches the official 596-residue sequence. The genuine IBD source carries GO:0000978, GO:0000981, GO:0005634 and GO:0006357 at that ancestor, with no additional loss event on the target path. The nuclear assertion includes human EBF3 among experimental descendants; this is expected rather than circular. [GO_REF:0000033](https://geneontology.org/GO_REF/0000033.html) describes the ancestral inference method. Current exact-term donor queries corroborated selected experimental records but did not exhaustively reconstruct all historical donor assertions or their original papers.

**INTERPRO.** The [current target response](https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q9H4W6/?page_size=100) verifies IPR003523 at residues 1–586, IPR032200 at 19–247, IPR038173 at 8–246 and IPR038006 at 263–347, together with their broad GO mappings. These mappings support the ancestral function; direct human evidence supplies the more specific Pol II terms. No isolated domain is thereby claimed to be a complete functional TF. [GO_REF:0000002](https://geneontology.org/GO_REF/0000002.html) describes the mapping method.

**TFCLASS and SUBCELL.** The [official TFClass table](https://genexplain.com/tfclass/huTF_classification_Genera.html) places EBF3 within the Early B-Cell Factor-related family at 6.1.5.0.3; [GO_REF:0000113](https://geneontology.org/GO_REF/0000113.html) explains the manually evaluated family assertions. The [UniProt SL-0191 record](https://rest.uniprot.org/locations/SL-0191.json) explicitly maps nucleus to GO:0005634 under [GO_REF:0000044](https://geneontology.org/GO_REF/0000044.html). These source scopes are preserved alongside independent human evidence.

The four refinements use current `is_a`/`part_of` ancestor responses: GO:0000978 contains GO:0003677, GO:0000981 contains GO:0003700, GO:0006357 contains GO:0006355, and GO:0045944 contains GO:0045893. The direction-neutral regulation term remains appropriate for the integrated core; positive reporter effects do not establish activation of all bound targets. The [portable evidence artifact](EBF3-evidence/README.md) records public raw-input URLs/hashes and reconstructs the family and template observations without bundling article bodies.
