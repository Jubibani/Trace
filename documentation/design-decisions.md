# Design Decisions (MVP)

## Plan before coding
1. Establish monorepo skeleton and documentation.
2. Add minimal FastAPI service with environment-driven configuration.
3. Expose health endpoint for operational readiness checks.
4. Add development Docker setup for reproducible local runtime.

## Risks and mitigations
- **Model/runtime coupling risk**: avoid direct calls to llama.cpp from API handlers; route through service interfaces.
- **Indexing scale risk**: chunking and AST extraction can become CPU-intensive; design async job boundaries early.
- **Storage complexity risk**: supporting SQLite + Qdrant + Neo4j from day one increases dev friction; phase integrations.
- **Parser coverage risk**: language-specific edge cases may break extraction quality; establish parser contract tests later.
