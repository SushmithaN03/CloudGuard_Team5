# CloudGuard_Team5
CloudGuard is a cloud infrastructure compliance and remediation platform that scans cloud resources, identifies policy violations, enables automated remediation for low-risk issues, and supports approval-based remediation for high-risk actions.

## Project structure

- `src/api/routes/` contains API route modules.
- `src/core/` contains configuration, database, and security modules.
- `src/models/`, `src/schemas/`, and `src/services/` contain application domain code.
- `src/workers/` contains background worker modules.
- `tests/`, `docs/`, `scripts/`, and `k8s/` hold tests and project resources.

Run the API locally with:

```bash
uvicorn src.main:app --reload
```

Copy `.env.example` to `.env` for local configuration. Keep secrets out of version control.
