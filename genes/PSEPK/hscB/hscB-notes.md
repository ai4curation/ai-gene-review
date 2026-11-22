# hscB curation notes

- Q88PK5 is the HscB-family co-chaperone encoded in the KT2440 isc locus. UniProt/HAMAP supports its dedicated Isc-system role.
- HscB recognizes IscU and stimulates the HscA ATP-dependent chaperone cycle; this role is represented as ATPase activator activity within Fe-S cluster assembly.
- No direct KT2440 interaction or kinetic study was found in this pass, so the mechanistic assignment rests on the conserved HscB family and locus architecture.


## Isc comparative-evidence audit (2026-11-07)

HscB (PP_0845) is the J-domain cochaperone of the Pseudomonas putida KT2440 Isc system. It binds the Hsp70-family partner HscA and stimulates ATP hydrolysis. Its conserved specialized family supports recognition of the IscU scaffold and coupling to cluster transfer, with the detailed interaction and conformational cycle established in bacterial homologs.

The target remains KT2440; no purified target assay is claimed. Specific curated HAMAP/RuleBase statements or independent NCBIfam/InterPro signatures ground the target inference. ARBA names are not used as proof. All original ordered source payloads are retained. The rows are IEA or historical NEW, not IBA; no donor-count argument, PAINT loss or new evolutionary node placement is asserted.

A genuine Falcon request failed with HTTP 403 authentication/access failure. Existing OpenScientist reports, where present, were preserved; no provider-branded replacement was fabricated. The log is `.cache/module-audit-logs/isc-20261107/psepk-consultation/falcon-hscB.log`.

### Evidence and biological limits

- [PMID:18986169] ATP-dependent HscA/HscB cluster-transfer reconstitution supports the cochaperone role and transient complex participation. Quoted support: “HscA-mediated acceleration of [2Fe2S] cluster transfer exhibited an absolute requirement for both HscB and ATP.”.
- [PMID:22782893] E. coli HscB preferentially binds structured IscU whereas HscA stabilizes its disordered form.

### Decisions

- GO:0001671 ATPase activator activity: ACCEPT. The target HAMAP SUBUNIT statement directly assigns stimulation of HscA ATPase; homolog biochemical studies explain this conserved role. HscB is the activator, not an independently assigned ATPase.
- GO:0006457 protein folding: UNDECIDED. Client specificity alone is not grounds to reject protein folding. E. coli HscB stabilizes structured IscU and participates in an ATP-dependent cluster-transfer cycle, but that endpoint is not itself a test of assisting formation of the correct tertiary structure in KT2440. Retain uncertainty rather than claiming that specialization excludes folding or that a generic J-domain proves it.
- GO:0044571 [2Fe-2S] cluster assembly: ACCEPT. Curated target HscB function and ATPase stimulation, together with homolog cluster-transfer reconstitution, support involvement in this assembly process. This does not assign sulfur mobilization, cluster synthesis catalysis or direct cluster binding to HscB.
- GO:0051087 protein-folding chaperone binding: MODIFY. Use the supported Hsp70 partner identity to specify the binding claim. This replacement describes the known target partner and does not infer that HscA is a general refolding enzyme. The dedicated interaction is independently curated by HAMAP; its detailed target affinity has not been measured.
- GO:0051259 protein complex oligomerization: UNDECIDED. GO0051259 includes oligomers of different subunits. HscB participation in an IscU-HscA transfer complex is compatible with that definition, and isolated monomeric HscB would not refute it. However, complex membership and an oligomerization-domain name do not by themselves demonstrate that KT2440 HscB promotes oligomer creation. Without a resolved target assembly mechanism, retain uncertainty rather than REMOVE.
- GO:1990230 iron-sulfur cluster transfer complex: ACCEPT. Specific HscB identity, curated HscA binding and activation, and homolog ternary-complex reconstitution support transfer-complex membership. The published stoichiometry is experimental context for homologs, not a measured native KT2440 stoichiometry.


## 2026-11-07 PR6175 evidence-specific follow-up

Reviewed the disputed folding, oligomerization and sulfur-transport interpretations against fresh official GO definitions and primary assay context. See `analysis/module_audits/bacterial_isc_iron_sulfur_cluster_assembly/round1/ecoli-psepk-consultation/evidence.md` and source-provenance.json for exact access limits and the newly read full9852006 negative luciferase assay. Original ordered source payloads, all historical NEW rows and immutable sources are preserved. E. coli negative folding assays are not relabeled as KT2440 experiments; HscB structured-state stabilization remains distinct from HscA holdase behavior. The PSEPK HscA retired proposal lifecycle is deliberately untouched pending parent adjudication. No new annotation is added.
