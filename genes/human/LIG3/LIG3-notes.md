# LIG3 (human, P49916) review notes

## Literature search (manual; no deep-research provider available)

Sources checked:
- All GOA-cited PMIDs, cached with `just fetch-gene-pmids human LIG3` (13 papers).
- PubMed E-utilities searches (2026-11-04): "Gao Y[au] DNA ligase III essential
  mitochondrial Nature 2011" -> PMID:21390131, PMID:21390132; "Wang H[au] DNA ligase III
  backup pathways nonhomologous end joining 2005" -> PMID:15899791; "Della-Maria J[au]
  ligase III alternative end joining" -> PMID:21816818; "Simsek D[au] ligase III end
  joining 2011" -> PMID:21655080; "Lu G[au] ligase III alternative end joining 2016
  microhomology" -> PMID:26787905. All fetched into `publications/`.
- Reactome cached entries for LIG3 reactions (BER, MMEJ, NER ligation, mtDNA ligation).
- UniProt P49916 record.

## Key findings

- One gene, two compartments. Isoform 1 (P49916-1) carries an N-terminal mitochondrial
  transit peptide; isoform 3 (alpha, P49916-3) starts at the downstream ATG and is nuclear;
  isoforms 2/4 (beta, germ-cell splice form) lack the XRCC1-binding BRCT
  [PMID:10207110 "inactivation of the upstream ATG resulted in nuclear accumulation of the
  DNA ligase III protein, whereas inactivation of the downstream ATG abolished nuclear
  localization and led to accumulation within the mitochondrial compartment"].
- Activity: ATP-dependent nick sealing; the PARP-like ZnF senses nicks/ends
  [PMID:20518483 "The collective results support a \"jackknife model\" in which the ZnF loads
  ligase III onto nicked DNA and conformational changes deliver DNA into the active site."].
  LigIIIalpha/XRCC1 and LigIIIbeta join nicked and linear duplex substrates
  [PMID:19589734 "hLigIIIbeta and the hLigIIIalpha/XRCC1 and hLigIV/XRCC4 complexes are
  active on both nicked and linear duplex DNA substrates"].
- Essential role is mitochondrial: [PMID:21390132 "we find that the mitochondrial, but not
  nuclear, Lig3 is required for cellular viability"]; [PMID:21390131 "our data reveal that
  the critical biological role of Lig3 is to maintain mtDNA integrity and not
  Xrcc1-dependent DNA repair"]. Human biallelic variants cause MNGIE-like mtDNA depletion
  [PMID:33855352 "The LIG3 gene encodes the only mitochondrial DNA (mtDNA) ligase and
  therefore plays a pivotal role in mtDNA repair and replication."].
- mtDNA replication: Okazaki-fragment ligation [PMID:21878356 "These findings support the
  role of DNA ligase III as the replicative DNA ligase in human mtDNA replication"]. The
  GOA IMP row for this paper uses "negative regulation of mitochondrial DNA replication",
  which inverts the sign of the knockdown result (knockdown attenuated recovery of mtDNA
  copy number). Recorded as a source defect (CACAO).
- mtBER: [PMID:24674627 "Overexpression of DNA ligase III in mitochondria improved the rate
  of overall BER"].
- Nuclear BER/SSBR with XRCC1 (Reactome; PMID:33087283 review), redundant with LIG1 in
  mouse cells (PMID:21390131).
- Alt-NHEJ/MMEJ: [PMID:15899791 "These in vivo and in vitro observations identify DNA ligase
  III as a candidate component for B-NHEJ"]; [PMID:21816818 "MRN interacts with DNA ligase
  IIIalpha/XRCC1, stimulating intermolecular ligation, and together these proteins join
  incompatible DNA ends in a reaction that mimics alt-NHEJ."]; translocations reduced
  without nuclear Lig3 [PMID:21655080]; LIG1 can substitute for some A-EJ [PMID:26787905].
- Not in V(D)J recombination: LIG3 cannot complement LIG4-null pre-B cells (PMID:9809069),
  supporting the NOT annotation.
- Context: telomere end-joining pathway choice (module and GO-CAM review proposed in ai4curation/ai-gene-review#5904; not on this branch and not used as evidence). The placement of LIG3 (with PARP1)
  in the alternative-NHEJ route at telomeres lacking POT1-TPP1 rests on PMID:28216226 ("interaction of
  de-phosphorylated NBS1S432 with TRF2 promotes A-NHEJ mediated repair of telomeres lacking POT1-TPP1") and
  the LIG3 alt-NHEJ literature above.

## Curation decisions of note
- GO:0003909 rows MODIFY -> GO:0003910 DNA ligase (ATP) activity.
- Reactome "Homology Directed Repair" TAS for HR -> MODIFY to alt-NHEJ (MMEJ is grouped
  under HDR in Reactome but is not homologous recombination).
- ARBA "mitochondrion organization" -> MODIFY to mitochondrial DNA metabolic process
  (GO:0000002 mitochondrial genome maintenance is obsolete).
- ARBA "negative regulation of DNA metabolic process" REMOVE (no supporting evidence).
- Bare protein-binding IPI rows REMOVE per policy.
