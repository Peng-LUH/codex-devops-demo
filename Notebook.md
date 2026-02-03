## Contexts
- needs -> outputs & results from dependent jobs
- steps -> prior step's outputs, outcome/conclusion
- secrets -> secret values incl. GITHUB_TOKEN (GitHub masks but be cautious)
- vars -> repo/org/environment-level config variables (great for cross-workflow settings)

- github -> run & event metadata (repo, ref, sha, event_name, etc.)
- env -> variables set at workflow/job/step scope (override rules: step > job > workflow)
- matrix: current matrix values (e.g., os, node)
- strategy -> matrix strategy info (job-index, job-total, fail-fast, max-parallel)
- job -> current job status; container/service info
- runner -> runner OS/arch/temp/tool_cache
- inputs -> parameters to reusable/workflow_dispatch workflows