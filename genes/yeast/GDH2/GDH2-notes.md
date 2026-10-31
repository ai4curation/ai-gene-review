# GDH2 (YDL215C, P33327) notes

Evidence journal (no paid deep research run; built from UniProt and cached publications).

- NAD-specific glutamate dehydrogenase, EC 1.4.1.2, homotetramer; large (~1092 aa) fungal-type NAD-GDH (IPR016210 NAD-GDH_euk), distinct from the hexameric NADP-GDHs GDH1/GDH3 [UniProt:P33327].
- Function: "We cloned GDH2, the gene that encodes the NAD-linked glutamate dehydrogenase"; gdh2 deletion "grew very poorly with glutamate as a nitrogen source"; "NAD-linked glutamate dehydrogenase catalyzes the major, but not sole, pathway for generation of ammonia from glutamate"; "normally NAD-linked glutamate dehydrogenase is not involved in glutamate biosynthesis" [PMID:1975578].
- "The GDH2-encoded NAD(+)-dependent glutamate dehydrogenase degrades glutamate producing ammonium and alpha-ketoglutarate" [PMID:11562373].
- Location: cytosol (IDA, cytosol isolation method, PMID:6343120, abstract-only); detected in mitochondrial proteomes (PMID:14576278, PMID:16823961).
- Regulation: interacts with and is phosphorylated by an NNK1-containing complex (TORC1 effector kinase); gdh2 deletion confers rapamycin resistance on glutamate medium [UniProt:P33327; PMID:20489023].

## Curation decisions
- Core MF GO:0004352; BP GO:0006538; CC cytosol.
- Mitochondrion IBA (PTN000176229; animal/plant mitochondrial GDH seeds, no fungal seed): REMOVE.
- protein binding (NNK1) x2: REMOVE (uninformative; regulatory phosphorylation by Nnk1 noted in description).
