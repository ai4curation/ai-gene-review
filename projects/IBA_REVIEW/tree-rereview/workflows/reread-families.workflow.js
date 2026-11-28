export const meta = {
  name: 'iba-family-tree-reread',
  description: 'Read-only re-read of family-review node assessments that dispute a PAINT placement, against the family tree listing: one reader per batch, then a verifier',
  whenToUse: 'Run on f... batches of projects/IBA_REVIEW/tree-rereview/plan-families.yaml; args.batches comes from tree_rereview.py inputs',
  phases: [
    { title: 'Read', detail: 'one reader per batch reads every disputed node assessment against the tree listing' },
    { title: 'Verify', detail: 'a second agent tries to fault every reading' },
  ],
}

const READINGS = ['SUPPORTS', 'NOT_A_TREE_ARGUMENT', 'REASON_CONTRADICTED', 'VERDICT_UNSUPPORTED', 'CANNOT_TELL']
const ADDITIVE = ['SUPPORTS', 'NOT_A_TREE_ARGUMENT']

const ROW = {
  type: 'object',
  properties: {
    family: { type: 'string' },
    node: { type: 'string' },
    term: { type: 'string' },
    negated: { type: 'boolean' },
    tree_reading: { type: 'string', enum: READINGS },
    quote_sentences: { type: 'array', items: { type: 'integer' } },
    tree_sentence: { type: 'string' },
    false_claims: { type: 'array', items: { type: 'string' } },
    false_claim_fields: { type: 'array', items: { type: 'string', enum: ['reason', 'affected_subfamilies', 'seeds'] } },
    reason_replacement: { type: 'string' },
    proposed_action: { type: 'string' },
    note: { type: 'string' },
  },
  required: ['family', 'node', 'term', 'negated', 'tree_reading', 'quote_sentences', 'tree_sentence'],
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
          family: { type: 'string' },
          node: { type: 'string' },
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
        required: ['family', 'node', 'term', 'negated', 'agrees', 'problem'],
      },
    },
  },
  required: ['rows'],
}

const DEFINITIONS = `Each row is a family review's assessment of one PAINT assertion (a GO term placed on a node of the family tree, or a loss of one) that disputes where PAINT put it:
- TOO_DEEP: the term sits on a node above its evidence, so it descends to members that lack the function.
- WRONG_NODE: the term should not be on this node at all.
- NEEDS_PRUNING: the placement holds for most of the clade, but a clade below the node should be excluded.
- LOSS_CONTRADICTED: a PAINT loss (IRD or IKR) removes a term from members that have it.
- LOSS_TOO_BROAD: a PAINT loss covers more members than the evidence for the loss does.

Readings (exactly one per row):
- SUPPORTS: the assessment argues from where the node, its seeds or the named subfamilies sit, and the listing and the tree facts agree. Examples: TOO_DEEP where every seed sits in one branch several steps below the node; NEEDS_PRUNING where the named subfamilies lie below the node and hold none of the seeds; a loss assessment where the loss node covers seeds of the assertion it stops.
- NOT_A_TREE_ARGUMENT: the assessment rests on functional evidence about members, or on the scope of the term, which the tree cannot settle; and nothing it says about the node, what it covers, its seeds or the affected subfamilies is contradicted by the listing or the tree facts.
- REASON_CONTRADICTED: the assessment states something about the tree that the listing or the tree facts contradict (which node this is, its taxon, how many leaves or which subfamilies it covers, where the seeds sit, whether a named subfamily lies below the node), but the verdict still stands on other grounds the assessment states.
- VERDICT_UNSUPPORTED: the tree contradicts the argument the assessment depends on, and the assessment states no other ground.
- CANNOT_TELL: the dossier is not enough to decide. Use this when the row says the listing has no entry for the node or no assertion of the term.

How to read the tree facts:
- seed_mrca_steps_below_node above 0 means every seed sits in one branch and the term was placed that many steps above them; 0 means the seeds bracket the node.
- Under "from the PANTHER 19.0 tree", a line "affected subfamily X: 0 of the node's N leaves" means subfamily X does not descend from this node, so a term on this node cannot reach it. A seed line says which subfamily the seed is in and how far below the node it sits.
- A loss row's summary says which node's assertion it stops; "other terms PAINT places on this node" shows what else was asserted there.
- A short seed list is not weak support.
- A line "MUST QUOTE AND ADDRESS" under a row names a listing sentence that stands against the assessment: for a TOO_DEEP assessment, that the seeds bracket the node, which is then their common ancestor. The assessment can still hold (the term may be too broad for members no seed represents), but the reading has to quote that sentence and say why.
- Judge the claim the assessment makes, not whether you would have reached the same verdict. A verdict you find weak, but that the tree does not contradict, is SUPPORTS or NOT_A_TREE_ARGUMENT with a note.`

const SENTENCE_RULES = `one or two sentences, at most 60 words, to be added to the assessment's reason. Say what the tree shows for this node and term and how it bears on the assessment. Begin with "In the PANTHER 19.0 tree". Use only facts given in the row. A number or relation taken from the listing summary must be in a sentence you list in quote_sentences; facts from the lines under "from the PANTHER 19.0 tree" may be used as given. Write plain prose: no colon followed by a space, no "#" character, no quotation marks, no line breaks. Do not repeat the assessment's own non-tree argument.`

function readPrompt(b) {
  return `You are re-reading PANTHER family reviews where the reviewer disputes a PAINT curator's placement of a GO term on a tree node, this time with the family tree in view. This is a read-only task: do not create, edit or delete any file, and do not use the network.

Read the whole dossier at ${b.dossier} with the Read tool (one file of about 700 lines; read all of it before you answer). It holds ${b.rows} rows in ${b.units} family reviews. Each "### ROW" block gives the review's assessment of one node and term (assessment, assessment_reason, the subfamilies it names as affected, its seeds, existing support, its other assessments of the same node) and, from the family's tree listing, what the node is, what lies below it, what else PAINT places on it, where the seeds of the assertion sit, and the listing's summary split into numbered sentences. Some rows add facts read straight off the PANTHER 19.0 tree.

For every row, decide how the tree bears on the assessment.

${DEFINITIONS}

For every row return:
- family, node, term, negated: copied exactly from the ROW line (node with its PANTHER: prefix).
- tree_reading: one of the readings above.
- quote_sentences: the numbers of the listing-summary sentences that carry the facts you rely on. Sentence 1 is always quoted for you; add the others that matter, and always every sentence named under MUST QUOTE AND ADDRESS. A row that quotes sentence 1 alone, or leaves out a sentence it must quote, is not applied. Leave it empty when the row has no listing summary.
- tree_sentence: ${SENTENCE_RULES} Leave it empty for CANNOT_TELL.
- For REASON_CONTRADICTED and VERDICT_UNSUPPORTED also: false_claims (each contradicted claim, quoted or closely paraphrased from the assessment, followed by the fact that contradicts it) and false_claim_fields (for every part of the assessment that holds one of those claims, its name: reason for the assessment_reason, affected_subfamilies when a listed subfamily does not descend from the node or holds seeds of the assertion, seeds when the review's seed list is wrong). For REASON_CONTRADICTED also reason_replacement: the full corrected assessment_reason as one paragraph that keeps every argument of the original that still holds, corrects only what the tree contradicts, adds nothing the row does not support, and ends with what the tree shows. The script rewrites the assessment_reason and nothing else, so a row whose false claim is in affected_subfamilies or seeds, alone or as well, is left for a curator, who has to correct the list: name the fields exactly. For VERDICT_UNSUPPORTED also proposed_action, the assessment you would give instead (SOUND, TOO_DEEP, WRONG_NODE, NEEDS_PRUNING, UNRESOLVED, LOSS_SUPPORTED, LOSS_CONTRADICTED or LOSS_TOO_BROAD).
- note: optional. Anything a curator should know that the other fields do not carry.

Work from the dossier alone. It was built from the review files, the tree listings and the PANTHER 19.0 tree and already holds everything this task needs, so do not open, search or list any other file, and do not run commands. Return exactly one entry for every ROW of the dossier, in dossier order.`
}

function checkPrompt(b, entries) {
  return `You are checking another agent's reading of PANTHER family-review node assessments against the family tree. This is a read-only task: do not create, edit or delete any file, and do not use the network.

The dossier is at ${b.dossier}; read it with the Read tool and work from it alone (do not open, search or list any other file, and do not run commands). Each "### ROW" block gives a family review's assessment of one node and term and what the family's tree listing, and the PANTHER 19.0 tree, say about the same node and term. The reader's entries for ${entries.length} of its rows are given below as JSON. For each entry, find its row in the dossier (same family, node, term and negated) and try to show that the entry is wrong. The reader used these definitions:

${DEFINITIONS}

Check each entry for:
1. The reading. Does tree_reading follow the definitions, given what the assessment argues and what the tree facts say? In particular, does a row read as SUPPORTS or NOT_A_TREE_ARGUMENT hide a contradiction: a statement in the assessment about the node, its taxon, its coverage, its seeds or the affected subfamilies that the listing or the tree facts contradict (for example an affected subfamily with 0 of the node's leaves)?
2. The sentence. Is every fact in tree_sentence present in that row, with the same numbers and relations? Is anything overstated? Is every number or relation taken from the listing summary carried by a sentence in quote_sentences?
3. Corrections. For REASON_CONTRADICTED and VERDICT_UNSUPPORTED: is each false claim really made by the assessment, and really contradicted by the row's facts? Does false_claim_fields name every part of the assessment the claims are in (affected_subfamilies when a listed subfamily has 0 of the node's leaves or holds seeds of the assertion)? Does reason_replacement keep every argument that still holds, change only what is contradicted, and add nothing the row does not support?
4. The quotes. Do they include every sentence named under MUST QUOTE AND ADDRESS, and does tree_sentence face that fact?

Return one result for every entry, with family, node, term and negated copied exactly: agrees is true only when you could not fault the entry; problem says specifically what is wrong and is empty when agrees is true. When a factual statement in tree_sentence cannot be found in the dossier row, agrees is false.

When you fault an entry and the right reading is SUPPORTS or NOT_A_TREE_ARGUMENT, so that the row can be put right by changing only the reading, the quoted sentences and the sentence, also give fixed with the corrected tree_reading, quote_sentences and tree_sentence. The corrected sentence follows the reader's rules: ${SENTENCE_RULES} Always give quote_sentences in fixed, including every MUST QUOTE AND ADDRESS sentence: the reader's list is not reused. Leave fixed out when the assessment's own reason or verdict needs correcting, or when the row needs a curator.

Entries to check:
${JSON.stringify(entries)}`
}

const batches = args.batches
log(`${batches.length} batch(es): ${batches.map(b => `${b.id} (${b.rows} rows)`).join(', ')}`)

const results = await pipeline(
  batches,
  b => agent(readPrompt(b), { label: `read:${b.id}`, phase: 'Read', schema: ANALYSIS, effort: 'medium', ...(args.readerModel ? { model: args.readerModel } : {}) }),
  async (analysis, b) => {
    if (!analysis) return { batch: b.id, analysis: null, verification: null }
    const entries = (analysis.rows || []).filter(r => r.tree_reading !== 'CANNOT_TELL')
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
