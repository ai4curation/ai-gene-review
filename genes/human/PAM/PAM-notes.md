# PAM (human, P19021) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: PAM is the closest experimentally characterised relative of quail
A0A8C2TBA7 (same PANTHER subfamily PTHR10680:SF14; human P19021 is one of the
descendant evidences of the PAINT IBD for GO:0004504 at PTN000073733,
Deuterostomia). This review treats PAM in its own right. No ProtNLM2 file was
opened or used.

### Deep research

`just deep-research-falcon human PAM --fallback perplexity-lite` failed: Edison
API returned `403 Forbidden` at `/auth/login`, and the perplexity-lite fallback
timed out after 600 s. No deep-research file exists. The review is based on the
UniProt record, the GOA-cited papers, and additional papers cached with
`just fetch-pmid` (30054598, 39137152, 34089560, 19604476, 35380039).

### Evidence summary (what is experimental in HUMAN vs inferred)

Experimental in human protein:
- Bifunctional PHM + PAL activity of recombinant human PAM (CHO-expressed,
  soluble truncation) [PMID:12699694 "The bifunctional PAM possesses two catalytic
  domains in a single polypeptide, peptidylglycine alpha-hydroxylating
  monooxygenase (PHM, EC 1.14.17.3) and peptidylamidoglycolate lyase (PAL, EC 4.3.2.5)"].
- Metal content: Zn and Cu [PMID:12699694 "Inductively coupled plasma detected
  0.62 mol of Zn(2+) and 1.25 mol of Cu(2+) per mol of bifunctional PAM"]; EDTA
  reduces PAL activity, restored by Zn.
- cDNA cloning and activity of truncated human PAM in COS cells [PMID:2357221].
- Amidating activity of recombinant human luminal PAM measured by glyoxylate
  release; T2D risk alleles (Ser539Trp, Asp563Gly) reduce activity; PAM amidates
  chromogranin A in the human beta-cell line EndoC-betaH1; endogenous PAM co-localises
  with insulin and glucagon vesicles in human islets; integral PAM in TGN
  [PMID:30054598].
- Human genetic LoF variants decrease plasma PAM amidating activity
  [PMID:39137152] (plasma activity = soluble secreted PAM).

Inferred (ortholog, rat/bovine, within SF14 / same enzyme):
- PAL is a six-bladed beta-propeller with Zn active site and a structural Ca
  (rat) [PMID:19604476].
- PHM dicopper ascorbate chemistry (rat) [PMID:19604476 intro; PMID:35380039].
- N-fatty-acylglycine -> primary fatty acid amide conversion (bovine P14925; ISS).
- Secretory granule membrane localisation (rat P10731; ISS), but human islet
  data corroborate granule localisation.

PAINT: only two IBDs reach PAM: GO:0004504 at PTN000073733 (Deuterostomia) and
GO:0005576 at PTN000840899. PAL activity (GO:0004598) was NOT propagated by
PAINT; the family review (interpro/panther/PTHR10680/PTHR10680-review.yaml)
leaves GO:0004598 UNRESOLVED because some family members are PHM-only. For human
PAM this does not matter: PAL activity is directly assayed (IDA).

### Decisions on problem rows

- GO:0034599 cellular response to oxidative stress (IC, PMID:39880951, UniProt):
  I read the full text via Europe PMC (PMC11821526). The paper shows that
  C-terminal amide-bearing proteins (CTAPs) formed under oxidative stress arise
  from non-enzymatic oxidative backbone cleavage, reconstituted in vitro without
  PAM ("Oxidative protein damage is sufficient to trigger CTAP formation in
  vitro"). PAM is mentioned only as the enzyme that amidates secreted peptide
  hormones, and the discussion speculates about "a to date unknown PAM-like
  lyase". The reader of CTAPs is FBXO31. No experiment implicates PAM. REMOVE,
  and recorded a PROBABLE source defect (WRONG_TERM / unsupported IC) for UniProt.
  The UniProt FUNCTION sentence on oxidative-stress amidation cites
  PubMed:2207077 (ECO:0000303, author statement) and does not describe PAM
  action either.
- GO:0010043 response to zinc ion (IDA, PMID:12699694): the experiment is in vitro
  metal stripping (EDTA) and Zn reconstitution of the purified enzyme, i.e.
  cofactor dependence, already captured by zinc ion binding. Not a cellular
  response. REMOVE.
- GO:0005515 protein binding (IPI, RASSF9/P-CIP1, PMID:9837933): generic binding;
  REMOVE per protein-binding policy. The cytosolic-domain interaction is about
  trafficking of rat PAM-1.
- Insulin secretion phenotypes after PAM knockdown (PMID:30054598) are
  downstream consequences of amidation of granule cargo (CgA) and are not
  annotated as process participation.
- NEW: trans-Golgi network (GO:0005802) from human EndoC-betaH1 data.
