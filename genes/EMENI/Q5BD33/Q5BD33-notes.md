# coaT notes

## 2026-11-17 review

QuickGO returned no rows for A. nidulans Q5BD33 even though the UniProt flat file carries AspGD direct annotations for `GO:0008775 acetate CoA-transferase activity`, `GO:0008410 CoA-transferase activity`, `GO:0019543 propionate catabolic process`, and mitochondrion. I therefore treated the direct CoaT paper and the PANTHER PAINT rows as missing annotation candidates rather than existing GOA rows to review.

The key paper is Fleck and Brock 2008, which purified A. nidulans CoaT and found succinyl-, propionyl-, and acetyl-CoA donor activity with corresponding acids as acceptors. The same abstract states that acetyl-CoA hydrolase activity was hardly detectable despite sequence similarity to acetyl-CoA hydrolases, so the root PAINT `GO:0003986 acetyl-CoA hydrolase activity` assertion looks like the legacy family name rather than the best core function.

The coaT single deletion had weak propionate phenotypes, while the double deletion with methylcitrate synthase blocked growth on acetate plus propionate as sole carbon sources. That supports a role as a propionyl-CoA detoxification backup rather than the primary methylcitrate-cycle enzyme.

I searched PubMed/web for `"ANIA_01547" CoaT`, `"Q5BD33" CoaT`, and `"Aspergillus nidulans" CoaT AtfA 2025` on 2026-11-17. The 2025 AtfA ChIP-seq/RNA-seq paper mentions `coaT` as an AtfA-bound gene in a regulatory survey; it did not add new direct CoaT biochemistry or change the GO decision.
