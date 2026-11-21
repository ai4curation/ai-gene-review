export const meta = {
  name: 'iba-tree-reread',
  description: 'Read-only re-read of overruled IBA rows against the PANTHER tree: one analyst per batch, then a verifier that tries to fault the analyst',
  whenToUse: 'Run on g... batches of projects/IBA_REVIEW/tree-rereview/plan.yaml; args.batches comes from tree_rereview.py inputs',
  phases: [
    { title: 'Read', detail: 'one analyst per batch reads every row against its tree extract' },
    { title: 'Verify', detail: 'a second agent tries to fault flagged rows, corrections and a sample of the rest' },
  ],
}

const READINGS = ['SUPPORTS', 'NOT_A_TREE_ARGUMENT', 'PAINT_ALREADY_REMOVED', 'REASON_CONTRADICTED', 'VERDICT_UNSUPPORTED', 'LOSS_APPLIES', 'LOSS_TOO_BROAD', 'CANNOT_TELL']
const ADDITIVE = ['SUPPORTS', 'NOT_A_TREE_ARGUMENT', 'PAINT_ALREADY_REMOVED']
const FAILURE_MODES = ['WRONG_ORTHOLOG_OR_PARALOG', 'FUNCTIONAL_DIVERGENCE', 'PSEUDO_OR_SUBACTIVITY_LOSS', 'CONTEXT_OR_TISSUE_MISMATCH', 'LINEAGE_OR_TAXON_MISMATCH', 'COMPARTMENT_OR_COMPLEX_MISMATCH', 'REGULATORY_SIGN_INVERSION', 'ROLE_CONFLATION', 'GRANULARITY_MISMATCH', 'SOURCE_MISCITATION', 'SOURCE_EVIDENCE_WEAK', 'CIRCULAR_PROPAGATION']

const ROW = {
  type: 'object',
  properties: {
    gene: { type: 'string' },
    term: { type: 'string' },
    negated: { type: 'boolean' },
    tree_reading: { type: 'string', enum: READINGS },
    quote_sentences: { type: 'array', items: { type: 'integer' } },
    tree_sentence: { type: 'string' },
    false_claims: { type: 'array', items: { type: 'string' } },
    false_claim_fields: { type: 'array', items: { type: 'string', enum: ['reason', 'summary', 'propagation_review'] } },
    reason_replacement: { type: 'string' },
    proposed_action: { type: 'string' },
    failure_modes_add: { type: 'array', items: { type: 'string', enum: FAILURE_MODES } },
    failure_modes_remove: { type: 'array', items: { type: 'string', enum: FAILURE_MODES } },
    note: { type: 'string' },
  },
  required: ['gene', 'term', 'negated', 'tree_reading', 'quote_sentences', 'tree_sentence'],
}
const ANALYSIS = { type: 'object', properties: { rows: { type: 'array', items: ROW } }, required: ['rows'] }
const CHECK = {
  type: 'object',
  properties: {
    rows: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          gene: { type: 'string' },
          term: { type: 'string' },
          negated: { type: 'boolean' },
          agrees: { type: 'boolean' },
          problem: { type: 'string' },
          fixed: {
            type: 'object',
            properties: {
              tree_reading: { type: 'string', enum: ADDITIVE },
              quote_sentences: { type: 'array', items: { type: 'integer' } },
              tree_sentence: { type: 'string' },
            },
            required: ['tree_reading', 'quote_sentences', 'tree_sentence'],
          },
        },
        required: ['gene', 'term', 'negated', 'agrees', 'problem'],
      },
    },
  },
  required: ['rows'],
}

const DEFINITIONS = `Readings (exactly one per row):
- SUPPORTS: the verdict's stated argument is about evolutionary placement (the gene is a paralog of the genes that have the function, sits in a divergent subfamily, lies outside the group the function belongs to, or the term was propagated from too deep a node) and the tree facts agree with it.
- NOT_A_TREE_ARGUMENT: the verdict rests on something the tree cannot settle: the scope or definition of the term, direct evidence on this gene, a missing domain or residue, a cell-type, compartment or taxon context, or the review's rejection of the seed annotations themselves. And nothing the review says about placement, relatedness, similarity or the seeds is contradicted by the tree facts. A gene that is itself a seed belongs here when the review also overrules or qualifies its own experimental row for the same term (see "other rows of this review on the same term"), or objects to the term and not to the transfer.
- PAINT_ALREADY_REMOVED: paint_losses_on_path lists a loss that is NOT re-asserted below. PAINT itself no longer makes this annotation for the gene, so the row in the cached GOA file is stale and an overruling verdict agrees with PAINT. Use this for kind "overruled" rows only.
- REASON_CONTRADICTED: the review states something about placement, orthology or paralogy, which genes the seeds are, how similar they are, or whether the gene's own annotation is among the evidence, and the tree facts contradict it; but the verdict still stands on other grounds that the review itself states.
- VERDICT_UNSUPPORTED: the tree contradicts the argument the verdict depends on and the review states no other ground. Also: the gene is itself a seed, the review keeps (ACCEPT or KEEP_AS_NON_CORE) its own experimental row for the same term, and it gives no term-scope or qualifier reason for treating the IBA row differently.
- LOSS_APPLIES / LOSS_TOO_BROAD: only for rows of kind "kept_under_loss", where the review keeps a term that PAINT has removed on the path. LOSS_APPLIES: PAINT's loss fits this gene, so the kept verdict rests on a stale row. LOSS_TOO_BROAD: the gene has its own evidence for the term (for example it is itself a seed), so PAINT's loss should not cover it.
- CANNOT_TELL: the dossier is not enough to decide; say in note what is missing.

How to read the tree facts:
- A review that says "paralog" is contradicted only when the seeds it means are ONE-TO-ONE ORTHOLOGs of the gene: joined at a speciation with no duplication and no horizontal-transfer node between them. A seed listed as ORTHOLOG across later duplications or across horizontal-transfer nodes does not contradict it. A review that says "distant" or "divergent" is contradicted by a one-to-one ortholog seed at high identity, not by a deep node alone.
- The tree's ortholog call is read from the family and subfamily PANTHER placed the gene in. When the review's argument is that this placement is itself the error (the gene lacks the domain that defines the family, the subfamily lumps proteins of different architecture, the alignment with the seeds covers a small part of the gene), the call cannot refute the review, because it is the thing disputed. Read such a row as NOT_A_TREE_ARGUMENT, say in the sentence that the tree places the seeds as orthologs and that the review disputes that placement on the grounds it gives, and do not treat the failure mode WRONG_ORTHOLOG_OR_PARALOG as contradicted (its definition includes a wrong family or subfamily).
- A line "MUST QUOTE AND ADDRESS" under a row names the summary sentences that stand against the verdict: the gene is itself a seed, it is inside the clade the seeds span, seeds share its own branch below the node, or every seed is an ortholog although the row claims a paralog. A verdict can hold in spite of any of them, but the reading has to face each one.
- The gene appearing among its own seeds (self_seed) is expected and is never circular: it means the gene's own experimental annotation is part of the evidence for the node.
- A short seed list is not weak support. A node far above the seeds (seed_mrca_steps_below_node > 0) means the curator placed the term above the evidence.
- The seed list of a cached GOA row can differ a little from current PAINT. A review naming a seed that is not in the dossier's list is not by itself a contradiction; put it in note.
- Judge the claim the review makes, not whether you would have reached the same verdict. A verdict you find weak, but that the tree does not contradict, is SUPPORTS or NOT_A_TREE_ARGUMENT with a note.`

function readPrompt(b) {
  return `You are re-reading gene-review verdicts that overrule a PAINT IBA annotation, this time with the PANTHER family tree in view. This is a read-only task: do not create, edit or delete any file, and do not use the network.

Read the whole dossier at ${b.dossier} with the Read tool (one file of about 700 lines; read all of it before you answer). It holds ${b.rows} rows in ${b.units} genes. Each "### ROW" block gives the review's verdict on one IBA row (action, summary, reason, propagation_review, existing support, and the other rows of the same review on the same term) and, from the gene's tree extract, where the PAINT node sits, where the gene sits, every seed with its relation to the gene and its identity in the family alignment, any PAINT loss on the path, and the extract's summary split into numbered sentences. The project's CLAUDE.md section "What an IBA asserts: read the phylogeny, not the donor count" is the background.

For every row, decide how the tree bears on the verdict.

${DEFINITIONS}

For every row return:
- gene, term, negated: copied exactly from the ROW line.
- tree_reading: one of the readings above.
- quote_sentences: the numbers of the summary sentences that carry the facts you rely on. Sentence 1 is always quoted for you; add the one to three others that matter most (where the seeds sit, how they are related to the gene, a PAINT loss), and always every sentence named under MUST QUOTE AND ADDRESS. A row that quotes sentence 1 alone, or leaves out a sentence it must quote, is not applied.
- tree_sentence: one or two sentences, at most 60 words, to be added to the review's reason. Say what the tree shows for this row and how it bears on the verdict. Begin with "In the PANTHER 19.0 tree". Use only facts given in the dossier and give counts and relations exactly as given there (for example "all 19 seeds are paralogs of the gene", "one seed is a one-to-one ortholog", "the gene is itself a seed"). Every number and every relation in it must be in the summary sentences you list in quote_sentences, so quote the sentence that carries each one, and speak only of the seeds the dossier shows. Where the row has a MUST QUOTE AND ADDRESS line, the sentence states each of those facts and says why the verdict holds in spite of it, or that it does not. Write plain prose: no colon followed by a space, no "#" character, no quotation marks, no line breaks. Do not repeat the review's own non-tree argument.
- For REASON_CONTRADICTED and VERDICT_UNSUPPORTED also: false_claims (each contradicted claim, quoted or closely paraphrased from the review, followed by the tree fact that contradicts it), false_claim_fields (for every field of the review that holds one of those claims, its name: reason, summary, or propagation_review for a failure mode or a source note) and reason_replacement (the full corrected reason as one paragraph: keep every argument of the original that still holds, remove or correct only what the tree contradicts, add nothing the dossier does not support, and end with what the tree shows). The script rewrites review.reason and nothing else, so a row whose false claim is in the summary or the propagation_review, alone or as well, is left for a curator: name the fields exactly, and when the row has no reason at all say so in note. For VERDICT_UNSUPPORTED also proposed_action (ACCEPT, KEEP_AS_NON_CORE, MODIFY, TOO_GENERAL, MARK_AS_OVER_ANNOTATED or UNDECIDED). failure_modes_remove and failure_modes_add are proposals for a curator: the script never changes failure modes, and a row that carries a proposal is left for adjudication. Propose one only when the tree contradicts the mode itself (WRONG_ORTHOLOG_OR_PARALOG when every seed is a one-to-one ortholog, no duplication or transfer node lies on the path, and the review does not dispute the placement), never to tidy up.
- note: optional. Anything a curator should know that the other fields do not carry, for example that the reason argues the term is true but too broad (under CLAUDE.md that is TOO_GENERAL or MODIFY, not REMOVE), or that the action conflicts with another row on the same term.

Work from the dossier alone. It was built from the review files and the tree extracts and already holds everything this task needs, so do not open, search or list any other file, and do not run commands. Where the dossier is not enough to decide a row, the reading is CANNOT_TELL. Return exactly one entry for every ROW of the dossier, in dossier order.`
}

function checkPrompt(b, entries) {
  return `You are checking another agent's reading of gene-review verdicts against the PANTHER family tree. This is a read-only task: do not create, edit or delete any file, and do not use the network.

The dossier is at ${b.dossier}; read it with the Read tool and work from it alone (do not open, search or list any other file, and do not run commands). Each "### ROW" block gives a review's verdict on one IBA row and what the gene's tree extract says about the same row. The reader's entries for ${entries.length} of its rows are given below as JSON. For each entry, find its row in the dossier (same gene, term and negated) and try to show that the entry is wrong. The reader used these definitions:

${DEFINITIONS}

Check each entry for:
1. The reading. Does tree_reading follow the definitions, given what the review argues and what the tree facts say? In particular, does a row read as SUPPORTS or NOT_A_TREE_ARGUMENT hide a contradiction: a statement in the review's summary, reason or propagation_review about placement, orthology or paralogy, seed identity, similarity, or the gene's own annotation that the tree facts contradict? And the other way: is a row read as REASON_CONTRADICTED only because the tree calls the seeds orthologs, when the review's argument is with the family or subfamily placement itself, or when a transfer node lies between the gene and the seeds?
2. The sentence. Is every fact in tree_sentence present in that row's tree facts, seed list or summary sentences, with the same numbers and relations? Is anything overstated (for example "all seeds" when it is some, "one-to-one ortholog" when duplications lie between)? Does it say how the tree bears on the verdict without claiming more than the tree shows?
3. Corrections. For REASON_CONTRADICTED and VERDICT_UNSUPPORTED: is each false claim really made by the review, and really contradicted by the tree facts? Does false_claim_fields name every field the claims are in (a claim that is also in the summary, a failure mode or a source note must be named there, because the script rewrites the reason only)? Does reason_replacement keep every argument of the original that still holds, change only what is contradicted, and add nothing the dossier does not support? Does the proposed action follow?
4. The quotes. Do the chosen quote_sentences carry the facts the sentence relies on? Do they include every sentence named under MUST QUOTE AND ADDRESS, and does tree_sentence face each of those facts instead of stepping around it?

Return one result for every entry, with gene, term and negated copied exactly: agrees is true only when you could not fault the entry; problem says specifically what is wrong and is empty when agrees is true. When a factual statement in tree_sentence cannot be found in the dossier row, agrees is false.

When you fault an entry and the right reading is SUPPORTS, NOT_A_TREE_ARGUMENT or PAINT_ALREADY_REMOVED, so that the row can be put right by changing only the reading, the quoted sentences and the sentence, also give fixed with the corrected tree_reading, quote_sentences and tree_sentence. The corrected sentence follows the reader's rules: one or two sentences of at most 60 words beginning "In the PANTHER 19.0 tree", only facts in the dossier row, every number and relation carried by a quoted summary sentence, every MUST QUOTE AND ADDRESS sentence quoted and addressed, plain prose with no colon followed by a space, no "#", no quotation marks. Always give quote_sentences in fixed: the reader's list is not reused. Leave fixed out when the review's own reason or verdict needs correcting, or when the row needs a curator.

Entries to check:
${JSON.stringify(entries)}`
}

const key = r => `${r.gene}|${r.term}|${String(Boolean(r.negated))}`

function toVerify(b, rows) {
  const flagged = new Set(b.flagged || [])
  let plain = 0
  return rows.filter(r => {
    const additive = ADDITIVE.includes(r.tree_reading)
    if (!additive || flagged.has(key(r)) || r.proposed_action || (r.false_claims || []).length) return true
    plain += 1
    return plain % 4 === 1
  })
}

const batches = args.batches
log(`${batches.length} batch(es): ${batches.map(b => `${b.id} (${b.rows} rows)`).join(', ')}`)

const results = await pipeline(
  batches,
  b => agent(readPrompt(b), { label: `read:${b.id}`, phase: 'Read', schema: ANALYSIS, effort: 'medium', ...(args.readerModel ? { model: args.readerModel } : {}) }),
  async (analysis, b) => {
    if (!analysis) return { batch: b.id, analysis: null, verification: null }
    const entries = toVerify(b, analysis.rows || [])
    log(`${b.id}: ${analysis.rows.length} rows read, ${entries.length} sent to the verifier`)
    if (!entries.length) return { batch: b.id, analysis, verification: { rows: [] } }
    const verification = await agent(checkPrompt(b, entries), { label: `verify:${b.id}`, phase: 'Verify', schema: CHECK, effort: 'high', ...(args.verifierModel ? { model: args.verifierModel } : {}) })
    return { batch: b.id, analysis, verification }
  },
)

// The full readings are in the run's journal, one result line per agent; return only counts.
const out = results.map((r, i) => r || { batch: batches[i].id, analysis: null, verification: null })
const summary = out.map(r => {
  const rows = (r.analysis && r.analysis.rows) || []
  const counts = {}
  for (const row of rows) counts[row.tree_reading] = (counts[row.tree_reading] || 0) + 1
  const checks = (r.verification && r.verification.rows) || []
  return { batch: r.batch, read: rows.length, readings: counts, checked: checks.length, faulted: checks.filter(c => !c.agrees).length, verified: Boolean(r.verification) }
})
for (const s of summary) log(`${s.batch}: ${JSON.stringify(s.readings)}; verifier faulted ${s.faulted} of ${s.checked}`)
return { summary }
