# PP_2800 curation notes

PP_2800 (`Q88J49`) is an unreviewed class III PLP-dependent aminotransferase.
UniProt supplies the submitted product name `Diaminobutyrate-2-oxoglutarate
transaminase`, but no experimental reference, gene name, or EC number
[file:PSEPK/PP_2800/PP_2800-uniprot.txt, "SubName:
Full=Diaminobutyrate-2-oxoglutarate transaminase"]. Its two GOA rows are broad
family-derived annotations for transaminase activity and PLP binding.

The pyoverdine-cluster enzyme PvdH is a distinct paralog at PP_4223. UniProt
places PP_2800 in `PTHR43552:SF2` and PvdH in `PTHR43552:SF1`; PP_2800 is also
located in a separate locus containing several predicted aminotransferase,
redox, transport, and catabolic proteins. KEGG membership in `ppu00975` is
therefore a candidate EC/family mapping, not evidence that PP_2800 supplies the
pyoverdine precursor.

## Curation boundary

- Retain only activities supported by the class III PLP-aminotransferase
  architecture.
- Do not assign pyoverdine biosynthesis or the exact PvdH reaction without
  target-specific substrate, genetic, or strong orthology evidence.
- Treat the physiological substrate and pathway as unresolved.
