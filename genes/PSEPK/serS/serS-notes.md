# serS review notes

- Q88FT2 is a reviewed class II serine--tRNA ligase (EC 6.1.1.11) assigned to
  PTHR43697:SF1. [file:PSEPK/serS/serS-uniprot.txt
  "RecName: Full=Serine--tRNA ligase"] [file:interpro/panther/PTHR43697/PTHR43697-entries.csv
  "Q88FT2,Serine--tRNA ligase"]
- UniProt records two reactions: charging tRNA(Ser) for translation and
  charging tRNA(Sec) to form Ser-tRNA(Sec). [file:PSEPK/serS/serS-uniprot.txt
  "to aminoacylate tRNA(Sec) with serine"]
- Review boundary: SerS supplies the Ser-tRNA(Sec) precursor to SelA. It is not
  assigned the downstream SelA conversion or SelB-mediated Sec incorporation
  function, and no function of a downstream selenoprotein is attributed to it.
- Generic nucleotide-binding, ligase, and aminoacylation annotations were
  replaced with ATP binding, serine-tRNA ligase activity, and seryl-tRNA
  aminoacylation, respectively.


## 2026-10-26 complete annotation review

SerS is a cytoplasmic class II seryl-tRNA synthetase that charges tRNA(Ser) for translation and is predicted to charge tRNA(Sec), supplying the serine-bearing intermediate for selenocysteinyl-tRNA formation. HAMAP MF_00176 specifies both tRNA(Ser) and tRNA(Sec) reactions and a homodimer spanning the tRNA-binding surface. Current GO:0004828 explicitly includes the tRNA(Sec) reaction, so no extra MF proposal is required. Source: `serS-uniprot.txt`, curated HAMAP MF_00176, catalytic-activity, domain and subcellular-location sections. Exact-target kinetic and localization experiments were not located; the retained claims are explicitly conserved functional inferences. Integral ATP/tRNA/cofactor properties are not peripheral merely because support is computational.

All original rows and machine fields were preserved. Broad ligase/binding terms were refined to supported descendants; the verified obsolete amino-acid-specific process was replaced in review metadata by current GO:0006418. Original IDs and labels remain intact. No new annotation rows were proposed.

The actual Falcon attempt failed (HTTP 403), fallback Perplexity-lite failed (HTTP 401/quota), and the fitness retrieval failed; no provider or fitness report was fabricated. Normal publication caching completed. Per-target outcomes are recorded under `.cache/module-audit-logs/aminoacyl-root-acquisition/PSEPK-serS-results.json`. Manual review used the independently curated sequence record, domain assignments and live GO definitions.

Open question: Can purified KT2440 SerS charge both native tRNA(Ser) and tRNA(Sec), and which conditions support flux through the downstream Sec-tRNA route?
