# Optional document engine

Run `cargo test --locked --workspace` here. The crate is intentionally empty;
this validates build plumbing, not parsing. Add deterministic processing and
fixtures in RUST-00, then optional PyO3 only after parity/benchmark evidence.
No database access. Python DocumentProcessor port retains a Python fallback;
neither adapter is implemented in ECO-00. Research installation never builds Rust.
