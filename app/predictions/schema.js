/* Prediction records and emitted term claims share the generic faceted browser. */
(() => {
    const payload = window.predictionData;
    if (!payload || !Array.isArray(payload.sets) || !Array.isArray(payload.claims)) {
        throw new Error('Prediction browser data must contain sets and claims arrays');
    }
    const dataset = new URLSearchParams(window.location.search).get('dataset') === 'claims' ? 'claims' : 'sets';
    const claims = dataset === 'claims';
    const field = (name, label, type = 'string', extra = {}) => ({field: name, label, type, ...extra});
    const facet = (name, label, type = 'string', extra = {}) => field(name, label, type, {sortBy: 'count', ...extra});
    const link = (name, label, extra = {}) => field(name, label, 'url', extra);
    const sourceVersion = field('source_version', 'Source version', 'string', {emptyLabel: 'Not recorded'});
    const commonFacetFields = [
        'source_method', 'source_version', 'species', 'projects', 'cohorts',
        'output_type', 'output_state', 'review_state', 'default_visible', 'set_id'
    ];
    const facets = [
        facet('default_visible', 'Current representation', 'boolean', {
            valueLabels: {true: 'Current', false: 'Superseded'}
        }),
        facet('source_method', 'Method'),
        facet('source_version', 'Source version', 'string', {valueLabels: {'': 'Not recorded (empty field)'}}),
        facet('species', 'Species'),
        facet('projects', 'Project', 'array', {matchMode: 'any'}),
        facet('cohorts', 'Cohort', 'array', {matchMode: 'any'}),
        facet('output_type', 'Output type'),
        facet('output_state', 'Output state'),
        facet('review_state', 'Review state'),
        claims ? facet('assessment', 'Assessment')
            : facet('assessment_categories', 'Recorded assessment categories', 'array', {matchMode: 'any'}),
        ...(claims ? [facet('error_type', 'Error type')] : [
            facet('correctness', 'Narrative correctness', 'integer'),
            facet('completeness', 'Narrative completeness', 'integer'),
            facet('performance_included', 'Included in narrative performance', 'boolean'),
        ]),
    ];
    const commonFields = [
        field('gene_symbol', 'Gene'), field('protein_id', 'Protein accession'),
        field('species', 'Species'),
        field('source_method', 'Method'), sourceVersion,
        field('output_type', 'Output type'), field('output_state', 'Output state'),
        field('review_state', 'Review state'),
    ];
    const metadataFields = [
        field('taxon_label', 'Organism'),
        field('projects', 'Projects', 'array'), field('cohorts', 'Cohorts', 'array'),
        field('document_status', 'Document status'),
        field('representation', 'Representation'), field('assessment_scheme', 'Assessment scheme'),
        field('input_protein_id', 'Input protein accession'),
        field('reference_protein_id', 'Reference protein accession'),
        field('performance_included', 'Included in narrative performance'),
        field('metadata_status', 'Metadata status'),
    ];
    const sourceFields = [
        link('review_link', 'Gene review'), link('source_link', 'Prediction review'),
        link('raw_link', 'Model output'),
    ];
    const detailFields = claims ? [
        field('term_id', 'Term', 'curie'), field('term_label', 'Term label'), field('term_type', 'Term type'),
        field('assessment', 'Assessment'), field('review_score', 'Review score'),
        field('error_type', 'Error type'), field('summary', 'Rationale'), field('evidence', 'Evidence'),
        link('set_link', 'Prediction set', {target: '_self'}),
    ] : [
        field('prediction_summary', 'Model functional summary'), field('summary', 'Review evaluation'),
        field('claim_count', 'Emitted term claims'),
        field('assessment_categories', 'Recorded assessment categories', 'array'),
        field('correctness', 'Narrative correctness'), field('completeness', 'Narrative completeness'),
        field('input_quality', 'Narrative input quality'),
        link('claims_link', 'Browse emitted claims', {target: '_self'}),
    ];
    const geneColumn = {
        key: 'gene', label: 'Gene / protein', type: 'compound', parts: [
            link('review_link', 'Gene', {linkTextField: 'gene_symbol'}), field('protein_id', 'Protein')
        ]
    };
    const methodColumn = {
        key: 'method', label: 'Prediction source', type: 'compound', parts: [
            field('source_method', 'Method'), sourceVersion
        ]
    };
    const sourceColumn = {
        key: 'links', label: 'Links', type: 'compound', parts: [
            link('source_link', 'Review', {role: 'link'}),
            link('raw_link', 'Output', {role: 'link'}),
            claims ? link('set_link', 'Set', {target: '_self', role: 'link'})
                : link('claims_link', 'Claims', {target: '_self', role: 'link'}),
        ]
    };
    const tableFields = claims ? [
        geneColumn, field('species', 'Species'), methodColumn,
        {key: 'term', label: 'Emitted term', type: 'compound', parts: [
            field('term_id', 'Term', 'curie'), field('term_label', 'Label')
        ]},
        {key: 'assessment', label: 'Assessment / review state', type: 'compound', parts: [
            field('assessment', 'Assessment'), field('review_state', 'Review state')
        ]},
        field('review_score', 'Score'), field('error_type', 'Error'),
        field('summary', 'Rationale'), sourceColumn,
    ] : [
        geneColumn, field('species', 'Species'), methodColumn,
        field('output_type', 'Output type'), field('output_state', 'Output state'),
        field('review_state', 'Review state'), field('claim_count', 'Term claims'),
        field('summary', 'Review evaluation'), sourceColumn,
    ];
    const displayFields = [...commonFields, ...detailFields, ...metadataFields,
        field('quality_notes', 'Quality notes', 'array'), ...sourceFields];
    window.searchData = payload[dataset];
    window.searchSchema = {
        title: 'Prediction Review Browser',
        description: 'Browse computational prediction reviews by source, organism and assessment.',
        searchPlaceholder: claims ? 'Search genes, terms, rationale or evidence…' : 'Search genes, methods or review summaries…',
        itemLabel: claims ? 'claims' : 'prediction sets',
        exportFilenamePrefix: claims ? 'prediction-claims' : 'prediction-sets',
        dataset,
        syncUrl: true,
        defaultFilters: {default_visible: ['true']},
        defaultFilterBypassFields: ['set_id'],
        urlFilterFields: ['set_id'],
        urlFilterLabels: {set_id: 'Prediction set'},
        sharedFilterFields: commonFacetFields,
        keepFacetOptions: true,
        hideEmptyFields: true,
        quietMissingFields: true,
        collapseSidebarOnMobile: true,
        datasetTabs: [
            {value: 'sets', label: 'Prediction sets', count: payload.sets.length},
            {value: 'claims', label: 'Claims', count: payload.claims.length},
        ],
        navigationLinks: [
            {label: 'Gene annotations', href: '../index.html'},
            {label: 'Projects', href: '../../pages/projects/index.html'},
        ],
        scopeNote: claims
            ? 'Each row is an emitted GO/EC claim with its VDCL assessment and review state; scores apply to individual claims. Narrative reviews and empty outputs appear under Prediction sets.'
            : 'Prediction sets include emitted terms, narrative reviews and assessed empty output; a set has no single score. Current representations are selected by default; remove that filter to include superseded reviews.',
        searchableFields: [
            'gene_symbol', 'protein_id', 'species', 'taxon_label', 'source_method', 'source_version',
            'projects', 'cohorts', 'summary', 'output_state', 'review_state',
            ...(claims ? ['term_id', 'term_label', 'assessment', 'error_type', 'evidence'] : ['assessment_categories', 'prediction_summary', 'input_protein_id', 'reference_protein_id']),
        ],
        facets,
        tableFields,
        displayFields,
        exportFields: [field('set_id', 'Prediction set ID'), ...displayFields, field('source_file', 'Source file')],
        customCss: `
            .results-table { min-width: 1050px; }
            .results-table .cell-content { white-space: normal; }
            .table-cell-gene { width: 12%; }
            .table-cell-species { width: 6%; }
            .table-cell-method { width: 14%; }
            .table-cell-summary { width: 25%; }
            .table-cell-summary .cell-content { max-height: 8em; overflow: auto; }
            .compound-cell { flex-wrap: wrap; }
            .compound-primary, .compound-secondary { white-space: normal; }
            .result-card .field-value { overflow-wrap: anywhere; }
            .facet-item > span:not(.facet-count) { overflow-wrap: anywhere; min-width: 0; }
            .facet-checkbox, .facet-count { flex-shrink: 0; }
            @media (max-width: 768px) {
                .header { padding: 24px 20px; }
                .browser-navigation, .dataset-tabs, .scope-note, .active-filters { padding: 10px 16px; }
                .search-container, .results-area { padding: 16px; }
            }
        `,
    };
    document.title = window.searchSchema.title;
    window.dispatchEvent(new Event('searchDataReady'));
})();
