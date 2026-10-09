# borr (Borealin-related, Drosophila melanogaster) curation notes

Accession: Q9VLD6 (FBgn0032105).

Deep research: `borr-deep-research-falcon.md` (falcon; the wrapper logged a 600 s timeout but the run completed and wrote the file). Important addition: Borr acts in acentrosomal female meiosis (oocytes): a Borr-INCENP fusion rescues bipolar and central spindle assembly after INCENP depletion, and borr RNAi increases homolog mono-orientation; 14-3-3 binding of phospho-Borr restrains CPC microtubule association. Borr is therefore absent only from male meiosis, so general spindle-midzone rows are kept general and only the male-meiosis-attributed and mitosis-specific rows are made specific.

## Literature journal

- Loss-of-function: CPC mislocalization, loss of H3S10ph, prometaphase delay, polyploidy
  [PMID:16224046 "Borr colocalises with the CPC components Aurora B kinase and Incenp in mitotic Drosophila cells, and is required for their localisation to the mitotic spindle"]
  [PMID:16224046 "a drastic reduction of histone H3 phosphorylation at serine 10"]
  [PMID:16224046 "producing large cells with giant nuclei and high ploidy"].
- Passenger localization in mitosis and absence from male meiosis
  [PMID:18268101 "During interphase, Borr was present in the nucleus"]
  [PMID:18268101 "By metaphase, the antibodies recognized specific dots that presumably correspond to the kinetochores"]
  [PMID:18268101 "Borr transferred onto the forming central spindle MTs, concentrating on the central spindle midzone by late anaphase and telophase"]
  [PMID:18268101 "Note that Borr is present in the nuclei of G2 spermatocytes but does not accumulate at the central spindle midzone of meiotic cells"].
- DNA binding [PMID:18268101 "MBP-Borr and MBP-Aust but not MBP alone were able to interact with DNA"].
- Binds Incenp directly and ESCRT-III Shrb [PMID:22724069 "Because Borr and INCENP interact directly"].

## Decisions

- Meiotic spindle midzone IDA (PMID:18268101) modified to mitotic spindle midzone: the paper states Borr is absent from the male meiotic midzone.
- Spindle (UniProt) modified to spindle midzone; spindle midzone IDA from the mitotic-cell paper (PMID:16224046) modified to mitotic spindle midzone; spindle midzone IBA accepted as-is because Borr also acts in oocyte meiosis.
- Protein binding (Shrb) removed: no informative ESCRT-III binding term exists.
