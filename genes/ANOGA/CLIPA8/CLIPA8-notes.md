# CLIPA8 (Anopheles gambiae, A0A1S4H5S2, AGAP010731) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: CLIPA8 was reviewed as the nearest experimentally characterised noncatalytic
CLIP-domain relative of DROME/scaf at the shared PAINT node PANTHER:PTN000667087. No
ProtNLM2 file or prediction-evidence folder was opened. This review stands on its own.

### Deep research
- `just deep-research-falcon ANOGA CLIPA8 --fallback perplexity-lite` failed: the
  Edison (falcon) API returned `403 Forbidden` at `/auth/login`, and the perplexity-lite
  fallback also failed. No deep-research file exists. The literature below was found with
  PubMed E-utilities (`CLIPA8 AND Anopheles` returns 6 records, plus searches for
  SPCLIP1, CLIPA28 and non-catalytic CLIP homologs) and cached with `just fetch-pmid`.

### Sequence and family
- 363 aa, signal peptide 1-25, clip domain 33-82, S1 peptidase domain 114-360; predicted
  activation cleavage after IMLR(66) (UniProt FT, by similarity to Q9GRW0).
- Catalytic triad scan (`CLIPA8-bioinformatics/RESULTS.md`): His163 and Asp212 kept;
  the catalytic Ser position (311, in CDGDGGSG) is Gly. Agrees with the UniProt curated
  caution [file:ANOGA/CLIPA8/CLIPA8-uniprot.txt "lacks the conserved Ser residue within
  the catalytic triad (Asp-His-Ser) which is replaced by a Gly residue"]. CLIPA8 is a
  serine protease homolog (cSPH), not a protease.
- UniProt PANTHER cross-reference: PTHR24258:SF129 (LP15124P-RELATED). GOA IBA rows
  for innate immune response and extracellular region trace to PTN000667087 (Ecdysozoa).
  CLIPA8 is itself among the descendant evidence for both IBD calls (appears in
  WITH/FROM), which marks its own experimental grounding. The IBD there did not include a
  catalytic or regulatory MF. Treat that as a deliberate PAINT decision.
- Scaf (Q7K5M0) carries the same two IBA rows from the same node, but UniProt places it in
  PTHR24250:SF27, a different family/subfamily cross-reference. The tree inside
  PTN000667087 was not resolved here, so CLIPA8-specific functions (melanization cascade
  hierarchy) should not be transferred to Scaf; only the node-level claims (extracellular,
  innate immunity) are shared by descent.

### Experimental findings in A. gambiae (all RNAi knockdown + biochemistry in hemolymph)
- Plasmodium: in refractory L3-5 mosquitoes CLIPA8 is needed for melanization of
  P. berghei ookinetes [PMID:16922859 "CLIPA8 is essential for parasite melanization"];
  in susceptible G3 it is needed for melanization caused by CTL4 knockdown, and co-
  silencing rescues viable oocysts [PMID:33045027 "CLIPA8/CTL4 co-silencing potently
  inhibited ookinete melanization and rescued viable oocysts"]. Single knockdown in G3
  changes nothing.
- Bacteria: needed for PPO activation and melanization of bacteria in hemolymph, not for
  wound melanization or melanotic pseudotumours, and not for survival after infection
  [PMID:17537726 abstract].
- Fungus (B. bassiana): needed for melanization of hyphae (not conidia/germ tubes), for
  PPO recruitment to hyphae, and for late PO activity; knockdown mosquitoes are more
  susceptible [PMID:23166497].
- Secreted into hemolymph as full-length protein and cleaved after infection into two
  disulfide-linked chains [PMID:17537726, UniProt PTM]. Cleavage depends on TEP1 and
  SPCLIP1 [PMID:24039584 "silencing SPCLIP1 inhibited completely CLIPA8 cleavage"];
  SRPN2 knockdown increases cleavage [PMID:31765430].
- Hierarchy of the noncatalytic module SPCLIP1 > CLIPA8 > CLIPA28 (> CLIPA14):
  [PMID:31765430 "the positive regulatory cSPHs are activated in a hierarchical manner,
  with SPCLIP1 being upstream followed by CLIPA8 then CLIPA28"].
- Downstream protease processing: CLIPA8 knockdown blocks cleavage of CLIPA28 and
  CLIPC9 and CLIPC9 localisation to E. coli [PMID:33045027], and abolishes CLIPB10
  cleavage [PMID:37918462 "silencing either CLIPA8 or CLIPA28 abolished CLIPB10
  cleavage"].
- In vitro: recombinant CLIPA8 is cleaved by activated CLIPB4, CLIPB9 and CLIPB10,
  probably after IMLR [PMID:37918462]. This shows CLIPA8 is a substrate of catalytic
  CLIPBs; it does not by itself show a cofactor activity.

### What is not established
- No biochemical evidence that CLIPA8 directly acts as a cofactor for a PPO-activating
  protease (as Manduca SPH1/SPH2 do) or binds PPO, PO or microbial surfaces. Osta's group
  wrote [PMID:23166497 "there is no evidence yet for the direct involvement of CLIPA8 in
  the processing of PPO"]. So no molecular function term is asserted; the core function is
  recorded at process level (positive regulation of melanization / protein processing).
- The protease that cleaves CLIPA8 in vivo is unknown; CLIPB4/B9/B10 are candidates.

### Decisions
- GO:0004252 serine-type endopeptidase activity (IEA InterPro) and GO:0006508 proteolysis
  (IEA InterPro): REMOVE. Catalytic Ser is Gly; being cleaved is not performing proteolysis.
- Extracellular region (IBA, 3x IDA, IEA): ACCEPT.
- Positive regulation of melanization defense response (2x IMP): ACCEPT, core.
- Positive regulation of melanin biosynthetic process (IMP): ACCEPT.
- Positive regulation of protein processing (IMP, CLIPA28/CLIPC9 cleavage): ACCEPT.
- Defense response to bacterium (2x IMP): ACCEPT; melanization of bacteria is a defense
  response even though survival is not affected.
- Antifungal innate immune response (IMP): ACCEPT.
- Defense response to symbiont (IMP, Plasmodium): ACCEPT.
- Innate immune response (IBA): ACCEPT; node-level claim, CLIPA8 is a donor.
- No NEW terms.
