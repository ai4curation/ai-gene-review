# ATG13 notes (human, O75143)

Deep research: not run (falcon times out after 600 s in this environment and perplexity-lite is not
installed). Review based on cached publications and the UniProt record.

## Key findings
- Subunit of ULK1-ATG13-FIP200 complex [PMID:19211835 "Atg13, which forms a stable approximately 3-MDa protein complex with ULK1 and FIP200"]; on isolation membrane and essential for autophagosome formation [PMID:19211835 "Atg13 localizes on the autophagic isolation membrane and is essential for autophagosome formation."].
- Activates ULK and bridges to FIP200 [PMID:19225151 "The binding of Atg13 stabilizes and activates ULK and facilitates the phosphorylation of FIP200 by ULK"].
- ATG101 binds via ATG13 HORMA [PMID:19597335; PMID:26299944].
- LIR binds LC3 isoforms [PMID:24290141].
- Mitophagy: recruited to damaged mitochondria after ULK1 phosphorylation [PMID:21855797].
- ULK1C:PI3KC3-C1 supercomplex; contacts mainly FIP200 with VPS15/ATG14/BECN1 [PMID:40442316].
- The lipidation paper itself says ATG13 "may not be essential for the lipidation of LC3" [PMID:19225151].

## Decisions
- Class III PI3K complex (IPI), autophagosome (IBA), regulation of protein lipidation, piecemeal microautophagy of nucleus (IBA, yeast route) and the obsolete parkin-screen term: MARK_AS_OVER_ANNOTATED.
- Obsolete PAS membrane -> MODIFY to phagophore assembly site.
- Core MF: protein kinase regulator activity (GO:0019887) in Atg1/ULK1 kinase complex, matching worm atg-13.
