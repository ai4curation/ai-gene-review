# Serinc isoform F (M9PFR2, DROME) notes

## 2026-10-21 — Full review, independent of the ProtNLM2 predictions

### Identity

- M9PFR2 is **Serinc isoform F** (Serinc-PF, FBpp0303601, 467 aa), one of six annotated
  polypeptides of FBgn0028399 / CG4672 (DmSERINC, TMS1, TMS1d)
  [file:genes/DROME/Serinc/Serinc-flybase.txt "Serinc-PF FBpp0303601 50.4 467 6.56 M9PFR2
  NP_001261947 AGB94640"]. It is the UniProt gene-centric canonical for the gene (AlphaFold
  entry, PANTHER HMM member) but is TrEMBL, PE 3, with no curated function.
- It gets its own folder rather than being an `isoform:` of the host because it has its own
  UniProt accession and its own GOA rows; it shares a symbol with the benchmark accession
  M9PCT1 (isoform C), so the folder follows the `<HOST>__<ACC>` convention.
- The fly has a single SERINC gene [PMID:31907454 "The fly possesses a single SERINC ortholog
  (referred to here as DmSERINC, and also known as TMS1)"].

### Which isoform was actually studied

The only primary study of the fly protein is the cryo-EM paper PMID:31907454. Its residue
numbering matches **isoform A (Q9VV58)** exactly: all 18 named residues (both disulphides,
the interface pocket, the inter-subdomain cleft) sit at the stated positions in isoform A and
in no other isoform. So the characterised protein is isoform A, not F.

`Serinc__M9PFR2-bioinformatics/RESULTS.md` quantifies what isoform F shares with it:

- identical over 1-365, then a 3-residue indel in the cytosolic TM8-TM9 loop, then identical
  again up to A419 = F416;
- completely different C-termini after that (A420-465 vs F417-467);
- 17 of the 18 named residues retained; the invariant **Lys438 is absent** from isoform F;
- Phobius: 9 helices for isoform A (last 439-459) versus 8 for isoform F (last 396-416), i.e.
  the isoform-F tail is not predicted to span the membrane, and the structure's final helix
  TM10 — part of subdomain B — is replaced.

The lipid-binding groove itself is "formed by TM5, 7, 8 and the C-terminal end of TM4"
[PMID:31907454], all inside the shared region, so the groove is intact in isoform F even
though subdomain B as a whole is not.

### Evolutionary grounding (why nothing is transferred from human or yeast)

- UniProt places M9PFR2 in **PANTHER PTHR10383:SF9**, whose official name is literally
  "SERINE INCORPORATOR, ISOFORM F" — the subfamily is named after this accession.
- SF9 is **not** a tight orthology group. `interpro/panther/PTHR10383/PTHR10383-entries.csv`
  puts yeast TMS1 (Q12116), *S. pombe* SPAPB1A10.07c (Q9HDY3), *Dictyostelium* (Q54UF8),
  *Monosiga* (A9UY97) and *Nematostella* (A7S4N4) in SF9, while the vertebrate paralogs each
  have their own subfamily (SERINC1 SF15, SERINC2 SF22, SERINC3 SF51, SERINC5 SF16). SF9 is
  effectively "the family minus the vertebrate expansions", so shared SF9 membership with
  yeast TMS1 says only that neither is a vertebrate paralog. It is not grounds for
  transferring the yeast endosome/vacuole localization or its putative scramblase role.
- PAINT: the only IBD for the family is `PTN000043695`, placed at **taxon:2759 (Eukaryota)**,
  and it propagates **only GO:0016020 membrane**
  (`interpro/panther/PTHR10383/PTHR10383-paint.tsv`). Its seeds include human SERINC2/3/5,
  two mouse genes, one rat gene and yeast TMS1 (SGD:S000002512). Curators who had the
  scramblase-capable members in hand propagated no molecular function and no process term
  from the root. Treated here as a deliberate decision, so scramblase activity
  (GO:0017128) and antiviral process terms are not proposed.
- Human SERINC3/5 do flip PS, PE and PC in proteoliposomes [PMID:37474505 "purified hSERINCs
  reconstituted into proteoliposomes induce the flipping of phosphatidylserine (PS),
  phosphatidylethanolamine (PE), and phosphatidylcholine (PC)"], but they are in SF51/SF16,
  so that is family context, not a transferable function.

### What is experimentally established in *Drosophila* (and on which isoform)

On isoform A, by direct assay:

- hexamer of ten-TM protomers in two subdomains [PMID:31907454 "Each of the six identical
  DmSERINC subunits consists of ten transmembrane helices (TM) arranged into two subdomains"];
- a groove in subdomain B with an acyl chain in the map ["the cryo-EM map revealed presence of
  an acyl chain bound at this site"];
- lipid-dependent stabilisation ["addition of phosphatidylserine, cholesterol or sulfatide
  increased DmSERINC and SERINC5 protein thermostability, while cardiolipin stabilised
  DmSERINC only"] and PS-sensitive HDX around that groove.

On the gene product generically: FlyBase records mass-spectrometric detection in an adult
head membrane fraction (Aradska et al. 2015, PMID:26201256) — gene-level and
high-throughput, not isoform-resolved.

Not established for any fly isoform: lipid transport/scrambling activity, native
compartment, loss-of-function phenotype, a physiological process. The HIV-1 restriction
result ["Ectopic expression of DmSERINC during production of Nef-deficient HIV-1 virions
strongly suppressed their infectivity"] is a heterologous assay in human cells and is not a
fly process. The authors themselves say "The conserved cellular functions of SERINCs remain
unclear".

### Decisions

- GO:0016020 membrane, IBA (PTN000043695) and IEA (InterPro IPR005016 +
  UniProtKB-SubCell SL-0162): **ACCEPT** both. GO:0016021 "integral component of membrane",
  which would have been the obvious refinement, is obsolete and replaced by GO:0016020
  (checked at OLS4), so membrane is already the most specific supported term; no fly
  experiment localises the protein to a named compartment.
- **NEW GO:0008289 lipid binding, evidence ISS**, not IDA: the direct lipid observations were
  made on isoform A, and this accession is a different protein entry. The groove is wholly
  inside the shared region, which is what justifies the inference; the C-terminal divergence
  is what keeps it from being IDA.
- Nothing proposed for scramblase activity, lipid transport, viral restriction or any
  biological process.

### Deep research

`just deep-research-falcon DROME Serinc__M9PFR2 --fallback perplexity-lite` was run twice on
2026-10-21 and failed both times (falcon 600 s timeout, then the perplexity-lite fallback
also timed out at 600 s). No deep-research file exists for this accession. The review was
built from the cached full text of PMID:31907454 and PMID:37474505, the UniProt and GOA
records, FlyBase, the PANTHER/PAINT files and the sequence analysis in
`Serinc__M9PFR2-bioinformatics/`. The falcon report for the same gene under the sibling
accession (`genes/DROME/Serinc/Serinc-deep-research-falcon.md`) was read as context; it
reaches the same conclusions (structure is the only direct fly evidence; scrambling is a
family-level hypothesis; no fly phenotype) but its citations are DOIs and internal chunk ids
rather than PMIDs, so nothing from it is cited as support here.

### Open items for other curators

- Isoform A (Q9VV58) is the accession the structural work actually describes and has no
  review in this repository. If one is written, the lipid-binding evidence is IDA there.
- `interpro/panther/PTHR10383/PTHR10383-review.yaml` lists M9PCT1 (isoform C) as the SF9
  representative member, whereas PANTHER 19.0's own classification carries M9PFR2. Same gene
  and same subfamily, so this is a representative-isoform difference, not a placement
  disagreement; left untouched.
