# LCIA Architecture (MVP)

## High-level modules
- **frontend**: future React + TypeScript UI for repository ingestion, chat, and graph visualization.
- **backend**: FastAPI service exposing HTTP APIs and orchestrating analyzer/AI workflows.
- **ai-engine**: local model runtime abstractions (llama.cpp, embeddings, prompts).
- **code-analyzer**: parsing and metadata extraction from source code.
- **storage**: vector, metadata, and graph persistence adapters.

## Key architectural decisions
1. **Backend-first MVP**
   - The API service is bootstrapped first so all other components integrate through clear contracts.
2. **Strictly local inference boundary**
   - AI providers will be adapter-driven and local-only in this project to preserve privacy.
3. **Replaceable storage adapters**
   - Qdrant/SQLite/Neo4j are intended defaults, but access should be abstracted behind repository interfaces.
4. **Monorepo for coordination**
   - Keeps schema/contracts/docs co-located while features are evolving rapidly.

## Critical challenge to proposed architecture
Running SQLite, Qdrant, and Neo4j simultaneously in MVP can overcomplicate setup. For faster onboarding, keep interfaces ready but defer mandatory Neo4j dependency until graph features are implemented.
