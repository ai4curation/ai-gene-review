# coaT notes

## 2026-11-17 review

The first pipeline fetch returned a header-only GOA file for A. nidulans Q5BD33 even though the UniProt flat file carries AspGD direct annotations for `GO:0008775 acetate CoA-transferase activity`, `GO:0008410 CoA-transferase activity`, `GO:0016788 hydrolase activity, acting on ester bonds`, `GO:0019543 propionate catabolic process`, and mitochondrion. A direct QuickGO query against UniProtKB:Q5BD33 returned 17 rows, including those AspGD rows plus PAINT, InterPro2GO, EC2GO, UniProtKB-SubCell, and ARBA projections; the review now treats all 17 as existing GOA rows rather than as missing annotation candidates.

The key paper is Fleck and Brock 2008, which purified A. nidulans CoaT and found succinyl-, propionyl-, and acetyl-CoA donor activity with corresponding acids as acceptors. The same abstract states that acetyl-CoA hydrolase activity was hardly detectable despite sequence similarity to acetyl-CoA hydrolases, so the `GO:0003986 acetyl-CoA hydrolase activity` IEA and IBA rows are plausible minor side-activity annotations but not the core function.

Fleck and Brock 2009 re-characterized S. cerevisiae Ach1p as the same kind of succinyl-CoA:acetate CoA-transferase, showed only minor acetyl-CoA hydrolase activity, and rescued yeast ach1 growth on acetate with A. nidulans coaT. That supports the fungal Ach1/CoaT-family transferase call and the `GO:0006083 acetate metabolic process` rows.

The coaT single deletion had weak propionate phenotypes, while the double deletion with methylcitrate synthase blocked growth on acetate plus propionate as sole carbon sources. That supports a role as a propionyl-CoA detoxification backup rather than the primary methylcitrate-cycle enzyme.

`GO:0019543 propionate catabolic process` is direction-inverted for CoaT chemistry: the enzyme can transfer CoASH from propionyl-CoA to acetate, releasing free propionate, whereas propionate catabolism activates propionate and then runs the methylcitrate cycle to break it down. The AspGD rows are curated experimental rows, so the review marks them over-annotated rather than removing them.

UniProt still carries ARBA-derived hydrolase naming, hydrolase EC/catalytic activity, and cytoplasm location statements that are superseded by the CoaT biochemical papers and by AspGD mitochondrial localization. The review records these as a `UniProtKB:Q5BD33` source defect rather than treating the propagated EC2GO hydrolase row as the core activity.

I searched PubMed/web for `"ANIA_01547" CoaT`, `"Q5BD33" CoaT`, and `"Aspergillus nidulans" CoaT AtfA 2025` on 2026-11-17. The 2025 AtfA ChIP-seq/RNA-seq paper mentions `coaT` as an AtfA-bound gene in a regulatory survey; it did not add new direct CoaT biochemistry or change the GO decision.
