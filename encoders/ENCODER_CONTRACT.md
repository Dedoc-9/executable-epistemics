# Encoder Contract

An encoder family is an independent hypothesis about software structure.
Admission requirements:

1. **Deterministic**: identical inputs yield identical vectors; any internal
   randomness uses a declared constant seed. Live API calls (e.g., embedding
   services) are inadmissible — precompute to a cache; the cache hash enters
   provenance.
2. **Total**: every entity in the corpus receives a vector.
3. **Ground-truth independent**: no input may contain co-change pairs, commit
   history, churn statistics, or any function of the prediction target.
   Known soft channel (errata E-003): size-like features partially encode
   change frequency; families containing them carry a declared ambiguity.
4. **Family membership is measured**, not claimed: the runtime groups
   encoders by distance-structure correlation (Spearman >= 0.6). Two
   projections of the same features will be one family and confirm nothing.
5. **Forbidden as candidates**: the activity baseline (churn+size) and any
   co-change-derived view — these are controls, not hypotheses.
