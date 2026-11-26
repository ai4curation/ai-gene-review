# Published bacterial SepRS/SepCysS identity and assay trace

PMID:28487430 supplementary methods were recovered from the normal EuropePMC supplemental-file service. The original DOCX and its direct paragraph extraction are retained; `extract_sources.py` reproduces the download and extraction. The publisher URL returned 403 before this successful public repository recovery.

The methods identify codon-optimized recombinant Parcubacteria proteins KPJ56532 (SepRS) and KPJ56533 (SepCysS). UniParc maps them to UPI000726682A/A0A0S7X285 and UPI0007259301/A0A0S7X265, respectively. Literal UniSave versions 20 and 18 are the two gene raw records; their sequences match the UniParc sequences exactly, as recorded in the extension baseline. Current UniProt JSON records explain deletion as not being part of a reference proteome, not biological invalidation. Neither record supplies a primary gene name, so accession-based folders are retained.

The DG_74_2 bin contains multiple genomes. SepRS/SepCysS lie on a common contig, but that does not establish a cultured native isolate. The purified SepRS activity is directly measured; the coupled SepCysS assay uses Chloroflexi SepRS with Parcubacteria SepCysS. The matched Parcubacteria pair is therefore a genomic and mechanistic inference from separately demonstrated steps, not the exact pair reconstituted in the published assay. The engineered E. coli reporter uses tRNA(Sec), not native Parcubacteria translation.

Normal fetch-gene exited 0 for both inactive IDs but wrote empty UniProt text and no QuickGO rows. The acquisition script replaced those empty responses by automatically downloaded, byte-exact UniSave records before the extension baseline, using the existing taxon resolver and GOA seeder. The original 40-gene baseline was not changed. No GOA assertions are used as functional evidence.

Run `uv run python genes/9BACT/A0A0S7X285/A0A0S7X285-source-analysis/verify_identities.py` to check the preserved UniSave/UniParc mappings, raw hashes, sequence lengths and published clone identifiers without downloading or modifying sources.
