# pll (Pelle) notes

UniProt Q05652 (KPEL_DROME), 501 aa; N-terminal death domain (55-121), C-terminal Ser/Thr kinase domain (213-499), catalytic K240.

## Core biology (with provenance)
- Kinase: "pelle encodes a protein of 501 amino acids, the last 292 of which comprise a protein kinase catalytic domain" and "the kinase catalytic domain is required for biological activity" [PMID:8440018].
- Autophosphorylation and phosphorylation of Toll: "We then demonstrate that Pelle can be autophosphorylated, and that this prevents binding to Toll as well as Tube." [PMID:9806920]
- Cactus kinase (IKK counterpart): "We conclude that Pelle acts as a Cactus kinase and preferentially phosphorylates Cactus at the serines required for signal responsiveness." and "In Drosophila, Toll signaling directs Cactus degradation via a sequence motif that is highly similar to that in IκBα, but without involvement of IKK." [PMID:24086459]
- Slimb link: "Pelle phosphorylates Cactus, triggering recognition by the Slimb βTrCP and subsequent ubiquitination and proteasome mediated degradation." [PMID:24086459]
- Death domain complex: "The interaction of the serine/threonine kinase Pelle and adaptor protein Tube through their N-terminal death domains leads to the nuclear translocation of the transcription factor Dorsal" [PMID:10589682]; "we find a heterotrimeric association of the death domains of MyD88, Tube, and the protein kinase Pelle" [PMID:12351681].
- Membrane recruitment: "activated Toll induces a localized recruitment of Tube and Pelle to the plasma membrane" [PMID:9609827].
- Immunity: "a dominant-negative version of the kinase Pelle can block induction of drosomycin by the cytokine Spaetzle, but does not affect induction of the antibacterial peptide attacin by lipopolysaccharide" [PMID:10973475].
- Hippo link: "Cka was phosphorylated in vitro by wildtype Pll, but not the kinase-dead mutant Pll-K240R" [PMID:26824654].
- Other substrates in vitro: dTRAF2 "is phosphorylated by Pelle in vitro" [PMID:11447260].

## Curation decisions
- GO:0004674 rows all ACCEPT; NEW GO:0008384 IkappaB kinase activity (IDA, PMID:24086459). Participation: Pelle catalyses Cactus phosphorylation. Comparator: IKK catalytic subunits (CHUK, IKBKB, fly IKKbeta) carry GO:0008384; Pelle is in the same enzymatic role for Cactus. GO:0008384 is_a GO:0004674 (OLS).
- Protein binding with Tube (several papers) -> MODIFY to GO:0070513 death domain binding; Pellino row REMOVE; Tehao row MODIFY to GO:0005121 Toll binding.
- IBA GO:0031663 LPS-mediated signaling REMOVE (fly LPS/attacin response is Pelle-independent; PMID:10973475). IBA nucleus MARK_AS_OVER_ANNOTATED.
- GO:0019221 cytokine-mediated signaling IBA ACCEPT (Spaetzle is a cytokine); GO:0008063 is not an is_a child of GO:0019221 in current GO (OLS parents: GO:0007166 only).
- GO:0007352 zygotic specification of D/V axis (PMID:6434989, a paper about maternal mRNA) -> MODIFY to GO:0009950; pll is a maternal-effect gene. QuickGO: only pll and dpp carry GO:0007352 in fly.
- Apoptotic process NAS REMOVE (death domain homology only).
- Hemocyte proliferation TAS (review, abstract-only) UNDECIDED.
- No GO:0002224 (TLR signaling) or PRR terms reach pll; GO:0008063 is used consistently.

## Deep research
Falcon deep research had not finished (still queued in the batch job) when this review was completed; the review rests on the UniProt record and the cached GOA publications. Re-check against the deep research file when it appears.
