# MT-TL1 notes

## Identity

- HGNC:7490, "mitochondrially encoded tRNA-Leu (UUA/G) 1"; RNAcentral URS000061A10B
  (HGNC cross-reference, resolved via the HGNC REST API). Encoded on the mtDNA heavy strand
  between the 16S rRNA (MT-RNR2) and MT-ND1 genes; decodes the leucine UUR (UUA/UUG) codons.
- Gene product type: transfer RNA (no UniProt entry). Files fetched with
  `ai-gene-review fetch-ncrna human MT-TL1 -r URS000061A10B_9606`.

## GOA (RNAcentral id URS000061A10B_9606)

Two electronic annotations only:

- GO:0030533 triplet codon-amino acid adaptor activity, IEA, GO_REF:0000115 (Rfam2GO, Rfam RF00005 tRNA).
- GO:0006412 translation, IEA, GO_REF:0000108 (inferred from the GO:0030533 MF via part_of).

GO:0030533 definition (OLS): "The codon binding activity of a tRNA that positions an activated amino
acid, mediating its insertion at the correct point in the sequence of a nascent polypeptide chain
during protein synthesis." It is is_a molecular adaptor activity / mRNA binding and part_of
translation (GO:0006412). GO:0032543 mitochondrial translation is_a GO:0006412.

## Normal function (literature)

- Wild-type mt tRNA-Leu(UUR) decodes both UUA and UUG in an in vitro mitochondrial translation
  system and binds both codons at the ribosomal A site [PMID:15477592 "the WT mt tRNA Leu(UUR) was
  efficient in decoding both the UUA and UUG codons and showed no activity with the UUC noncognate
  codon."; "Native mt tRNA Leu(UUR) efficiently bound to both the UUA and UUG codons"].
- The wobble uridine (U34) carries 5-taurinomethyluridine (taum5U); the modification is installed by
  nuclear enzymes (MTO1/GTPBP3), and is required for UUG decoding [PMID:15477592; PMID:10660592].
- It is charged with leucine by mitochondrial leucyl-tRNA synthetase (LARS2) [PMID:12549915
  "mutant tRNA to be aminoacylated by the human mitochondrial leucyl-tRNA synthetase"].

## Disease (MELAS, MIDD)

- m.3243A>G in the D-loop region of tRNA-Leu(UUR) is the classic MELAS mutation [PMID:2102678].
- Mutant tRNAs (3243, 3271) show reduced steady-state levels and lack the wobble taurine
  modification [PMID:10660592]; A3243G native tRNA is ~25-fold less efficiently aminoacylated
  [PMID:12549915]; loss of taum5U causes a UUG-specific decoding defect [PMID:15477592;
  PMID:17132941]; the modification defect is seen in patient tissues [PMID:15893315].

## Curation decisions

- GO:0030533 ACCEPT; core MF. The tRNA itself performs the adaptor step (codon recognition with
  positioned aminoacyl group), so this is participation, not substrate status.
- GO:0006412 translation: the term is correct but general; for a mtDNA-encoded tRNA that only
  functions on the mitoribosome, MODIFY to GO:0032543 mitochondrial translation.
- No NEW process terms for tRNA aminoacylation (GO:0070127) or tRNA wobble uridine modification
  (GO:0002098): MT-TL1 is the substrate there; the work is done by LARS2 and MTO1/GTPBP3. Comparator
  logic per project guidance: substrate tRNAs are not annotated to their charging process.
- Location: mitochondrial matrix (GO:0005759) is where mitochondrial translation takes place; not
  added as an annotation (no direct localisation experiment curated here), used in core function
  only as context via the process.
- Module `mitochondrial_trna_charging_and_initiator_formylation`: MT-TL1 not added. In that module
  the mt-tRNAs are substrates (inputs) of the synthetases, the module's boundary excludes the
  mitoribosome where the tRNA's own adaptor activity happens, tRNA-Leu's synthetase (LARS2) is not
  in the module, and module parts are grounded on UniProt protein representatives.
