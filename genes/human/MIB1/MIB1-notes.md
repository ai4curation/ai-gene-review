# MIB1 (human, Q86YT6) review notes

## Identity
- E3 ubiquitin-protein ligase MIB1 (EC 2.3.2.27). PANTHER PTHR24202 (official name "E3 UBIQUITIN-PROTEIN LIGASE MIB2") / PTHR24202:SF53 (E3 UBIQUITIN-PROTEIN LIGASE MIB1).
- IBA nodes: ubiquitin protein ligase activity, protein ubiquitination, cytoplasm PTN001197468; Notch signaling pathway and endocytosis PTN008608909.

## Key findings
- MZM and REP domains bind JAG1 N-box and C-box; both needed for efficient ubiquitination and signaling; human MIB1 rescues fly mib1 [PMID:25747658].
- "The dominant E3 ligase responsible for ligand ubiquitination in mammals is Mib1" [PMID:25747658].
- Non-Notch substrates: SMN [PMID:23615451], GABARAP [PMID:28712572], TBK1 K63 [PMID:21903422], PCM1/AZI1/CEP131 at centriolar satellites [PMID:24121310].

## Decisions
- Core: GO:0061630 in GO:0016567, GO:0007219, GO:0006897; cytoplasm/plasma membrane.
- All protein-binding rows REMOVE (partners are substrates; interaction not disputed).
- Considered NEW GO:0045747 positive regulation of Notch; comparator check (QuickGO): mouse Mib1 carries GO:0007219 IMP but not GO:0045747; human MIB2 has neither -> did not add.

## Variant-relevant biology
- In mammals MIB1 is the main ligand E3; Neuralized (NEURL1/1B) is minor, in contrast to Drosophila where Neur is critical in neurogenesis.
