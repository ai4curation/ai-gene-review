# rps19 notes

- The GOA file is header-only, so there are no existing GOA annotations to review or convert into NEW rows.
- UniProt identifies the protein as small ribosomal subunit protein uS19c and states that protein S19 forms a complex with S13 that binds strongly to 16S rRNA [file:MISSI/rps19/rps19-uniprot.txt "Protein S19 forms a complex with S13 that binds strongly to the 16S ribosomal RNA"].
- Core curation uses structural constituent of ribosome, rRNA binding, translation, chloroplast, and small ribosomal subunit, matching the UniProt GO cross-references [file:MISSI/rps19/rps19-uniprot.txt "GO; GO:0003735; F:structural constituent of ribosome"] [file:MISSI/rps19/rps19-uniprot.txt "GO; GO:0019843; F:rRNA binding"] [file:MISSI/rps19/rps19-uniprot.txt "GO; GO:0006412; P:translation"].
- I did not propagate the TreeGrafter mitochondrial small ribosomal subunit annotation because this is a plastid/chloroplast rps19 entry [file:MISSI/rps19/rps19-uniprot.txt "SUBCELLULAR LOCATION: Plastid, chloroplast"].
- I did not make ribosomal small subunit assembly a core function because the direct UniProt functional support is a structural/rRNA-binding ribosomal subunit role rather than a dedicated assembly-factor role.
- PR review suggested a chloroplast-specific small ribosomal subunit term. I checked the local GO cache: GO:0009543 is labeled chloroplast thylakoid lumen here, and no chloroplast-specific small ribosomal subunit term is available in the cached terms. I therefore retained GO:0015935 small ribosomal subunit rather than using an incorrect GO ID.
