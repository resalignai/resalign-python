# Health

Types:

```python
from resalign.types import HealthCheckResponse
```

Methods:

- <code title="get /v1/health">client.health.<a href="./src/resalign/resources/health.py">check</a>() -> <a href="./src/resalign/types/health_check_response.py">HealthCheckResponse</a></code>

# Taxonomy

Types:

```python
from resalign.types import (
    TaxonomyListFunctionsResponse,
    TaxonomyListRolesResponse,
    TaxonomySearchSkillsResponse,
)
```

Methods:

- <code title="get /v1/taxonomy/functions">client.taxonomy.<a href="./src/resalign/resources/taxonomy.py">list_functions</a>() -> <a href="./src/resalign/types/taxonomy_list_functions_response.py">TaxonomyListFunctionsResponse</a></code>
- <code title="get /v1/taxonomy/roles">client.taxonomy.<a href="./src/resalign/resources/taxonomy.py">list_roles</a>(\*\*<a href="src/resalign/types/taxonomy_list_roles_params.py">params</a>) -> <a href="./src/resalign/types/taxonomy_list_roles_response.py">TaxonomyListRolesResponse</a></code>
- <code title="get /v1/taxonomy/skills">client.taxonomy.<a href="./src/resalign/resources/taxonomy.py">search_skills</a>(\*\*<a href="src/resalign/types/taxonomy_search_skills_params.py">params</a>) -> <a href="./src/resalign/types/taxonomy_search_skills_response.py">TaxonomySearchSkillsResponse</a></code>

# Alignments

Methods:

- <code title="get /v1/alignments/{alignment_id}">client.alignments.<a href="./src/resalign/resources/alignments/alignments.py">retrieve</a>(alignment_id) -> object</code>
- <code title="get /v1/alignments">client.alignments.<a href="./src/resalign/resources/alignments/alignments.py">list</a>() -> object</code>
- <code title="get /v1/alignments/{alignment_id}/resources">client.alignments.<a href="./src/resalign/resources/alignments/alignments.py">get_resources_status</a>(alignment_id) -> object</code>

## Start

Types:

```python
from resalign.types.alignments import StartAlignment
```

Methods:

- <code title="post /v1/alignments/start">client.alignments.start.<a href="./src/resalign/resources/alignments/start.py">create</a>(\*\*<a href="src/resalign/types/alignments/start_create_params.py">params</a>) -> object</code>
- <code title="post /v1/alignments/start/stream">client.alignments.start.<a href="./src/resalign/resources/alignments/start.py">create_with_streaming</a>(\*\*<a href="src/resalign/types/alignments/start_create_with_streaming_params.py">params</a>) -> object</code>

# Analysis

Types:

```python
from resalign.types import WeightFields, AnalysisGetQuotaResponse, AnalysisRunResponse
```

Methods:

- <code title="get /v1/analysis/fetch">client.analysis.<a href="./src/resalign/resources/analysis.py">list</a>() -> object</code>
- <code title="get /v1/analysis/quota">client.analysis.<a href="./src/resalign/resources/analysis.py">get_quota</a>() -> <a href="./src/resalign/types/analysis_get_quota_response.py">AnalysisGetQuotaResponse</a></code>
- <code title="post /v1/analysis/run">client.analysis.<a href="./src/resalign/resources/analysis.py">run</a>(\*\*<a href="src/resalign/types/analysis_run_params.py">params</a>) -> <a href="./src/resalign/types/analysis_run_response.py">AnalysisRunResponse</a></code>

# Roadmaps

Types:

```python
from resalign.types import RoadmapGenerateResponse
```

Methods:

- <code title="get /v1/roadmaps/fetch">client.roadmaps.<a href="./src/resalign/resources/roadmaps.py">list</a>() -> object</code>
- <code title="post /v1/roadmaps/generate">client.roadmaps.<a href="./src/resalign/resources/roadmaps.py">generate</a>(\*\*<a href="src/resalign/types/roadmap_generate_params.py">params</a>) -> <a href="./src/resalign/types/roadmap_generate_response.py">RoadmapGenerateResponse</a></code>

# LearningPaths

Methods:

- <code title="get /v1/learning-paths/{path_id}">client.learning_paths.<a href="./src/resalign/resources/learning_paths/learning_paths.py">retrieve</a>(path_id) -> object</code>
- <code title="get /v1/learning-paths">client.learning_paths.<a href="./src/resalign/resources/learning_paths/learning_paths.py">list</a>() -> object</code>
- <code title="post /v1/learning-paths/enroll">client.learning_paths.<a href="./src/resalign/resources/learning_paths/learning_paths.py">enroll</a>(\*\*<a href="src/resalign/types/learning_path_enroll_params.py">params</a>) -> object</code>

## Modules

Methods:

- <code title="get /v1/learning-paths/{path_id}/modules/{module_id}">client.learning_paths.modules.<a href="./src/resalign/resources/learning_paths/modules.py">retrieve</a>(module_id, \*, path_id) -> object</code>
- <code title="get /v1/learning-paths/{path_id}/modules/{module_id}/content">client.learning_paths.modules.<a href="./src/resalign/resources/learning_paths/modules.py">get_content</a>(module_id, \*, path_id, \*\*<a href="src/resalign/types/learning_paths/module_get_content_params.py">params</a>) -> object</code>
- <code title="get /v1/learning-paths/{path_id}/modules/{module_id}/resources">client.learning_paths.modules.<a href="./src/resalign/resources/learning_paths/modules.py">get_resources</a>(module_id, \*, path_id, \*\*<a href="src/resalign/types/learning_paths/module_get_resources_params.py">params</a>) -> object</code>

## Topics

Methods:

- <code title="post /v1/learning-paths/{path_id}/topics/{topic_id}/complete">client.learning_paths.topics.<a href="./src/resalign/resources/learning_paths/topics.py">complete</a>(topic_id, \*, path_id) -> object</code>
- <code title="post /v1/learning-paths/{path_id}/topics/{topic_id}/uncomplete">client.learning_paths.topics.<a href="./src/resalign/resources/learning_paths/topics.py">uncomplete</a>(topic_id, \*, path_id) -> object</code>

# CompanyResearch

Types:

```python
from resalign.types import (
    CompanyResearchRetrieveResponse,
    CompanyResearchEnrichResponse,
    CompanyResearchResultResponse,
)
```

Methods:

- <code title="get /v1/company_research/retrieve/{identifier}">client.company_research.<a href="./src/resalign/resources/company_research.py">retrieve</a>(identifier) -> <a href="./src/resalign/types/company_research_retrieve_response.py">CompanyResearchRetrieveResponse</a></code>
- <code title="post /v1/company_research/enrich">client.company_research.<a href="./src/resalign/resources/company_research.py">enrich</a>(\*\*<a href="src/resalign/types/company_research_enrich_params.py">params</a>) -> <a href="./src/resalign/types/company_research_enrich_response.py">CompanyResearchEnrichResponse</a></code>
- <code title="get /v1/company_research/result/{identifier}">client.company_research.<a href="./src/resalign/resources/company_research.py">result</a>(identifier) -> <a href="./src/resalign/types/company_research_result_response.py">CompanyResearchResultResponse</a></code>
- <code title="post /v1/company_research/run">client.company_research.<a href="./src/resalign/resources/company_research.py">run</a>(\*\*<a href="src/resalign/types/company_research_run_params.py">params</a>) -> object</code>

# JobsBoard

Types:

```python
from resalign.types import JobsBoardRefreshResponse
```

Methods:

- <code title="post /v1/jobs_board/refresh_jobs">client.jobs_board.<a href="./src/resalign/resources/jobs_board/jobs_board.py">refresh</a>() -> <a href="./src/resalign/types/jobs_board_refresh_response.py">JobsBoardRefreshResponse</a></code>

## Fetch

Types:

```python
from resalign.types.jobs_board import JobPosting, FetchListResponse
```

Methods:

- <code title="get /v1/jobs_board/fetch/{job_id}">client.jobs_board.fetch.<a href="./src/resalign/resources/jobs_board/fetch.py">retrieve</a>(job_id) -> <a href="./src/resalign/types/jobs_board/job_posting.py">JobPosting</a></code>
- <code title="get /v1/jobs_board/fetch">client.jobs_board.fetch.<a href="./src/resalign/resources/jobs_board/fetch.py">list</a>(\*\*<a href="src/resalign/types/jobs_board/fetch_list_params.py">params</a>) -> <a href="./src/resalign/types/jobs_board/fetch_list_response.py">FetchListResponse</a></code>

# Favorites

Types:

```python
from resalign.types import FavoriteListResponse, FavoriteDeleteResponse, FavoriteAddResponse
```

Methods:

- <code title="get /v1/favorites/list">client.favorites.<a href="./src/resalign/resources/favorites.py">list</a>() -> <a href="./src/resalign/types/favorite_list_response.py">FavoriteListResponse</a></code>
- <code title="delete /v1/favorites/delete/{job_posting_id}">client.favorites.<a href="./src/resalign/resources/favorites.py">delete</a>(job_posting_id) -> <a href="./src/resalign/types/favorite_delete_response.py">FavoriteDeleteResponse</a></code>
- <code title="post /v1/favorites/add/{job_posting_id}">client.favorites.<a href="./src/resalign/resources/favorites.py">add</a>(job_posting_id) -> <a href="./src/resalign/types/favorite_add_response.py">FavoriteAddResponse</a></code>

# Resume

Types:

```python
from resalign.types import (
    ResumeListResponse,
    ResumeDeleteResponse,
    ResumeRetryExtractionResponse,
    ResumeUploadResponse,
)
```

Methods:

- <code title="get /v1/resume/list">client.resume.<a href="./src/resalign/resources/resume.py">list</a>() -> <a href="./src/resalign/types/resume_list_response.py">ResumeListResponse</a></code>
- <code title="delete /v1/resume/delete/{resume_id}">client.resume.<a href="./src/resalign/resources/resume.py">delete</a>(resume_id) -> <a href="./src/resalign/types/resume_delete_response.py">ResumeDeleteResponse</a></code>
- <code title="get /v1/resume/download/{resume_id}">client.resume.<a href="./src/resalign/resources/resume.py">download</a>(resume_id) -> object</code>
- <code title="post /v1/resume/retry-extraction/{resume_id}">client.resume.<a href="./src/resalign/resources/resume.py">retry_extraction</a>(resume_id) -> <a href="./src/resalign/types/resume_retry_extraction_response.py">ResumeRetryExtractionResponse</a></code>
- <code title="post /v1/resume/upload">client.resume.<a href="./src/resalign/resources/resume.py">upload</a>(\*\*<a href="src/resalign/types/resume_upload_params.py">params</a>) -> <a href="./src/resalign/types/resume_upload_response.py">ResumeUploadResponse</a></code>

# Profile

Methods:

- <code title="get /v1/profile">client.profile.<a href="./src/resalign/resources/profile.py">retrieve</a>() -> object</code>
- <code title="post /v1/profile/complete-onboarding">client.profile.<a href="./src/resalign/resources/profile.py">complete_onboarding</a>() -> object</code>
- <code title="post /v1/profile/merge-resume">client.profile.<a href="./src/resalign/resources/profile.py">merge_resume</a>() -> object</code>
- <code title="patch /v1/profile/step/{step}">client.profile.<a href="./src/resalign/resources/profile.py">save_onboarding_step</a>(step, \*\*<a href="src/resalign/types/profile_save_onboarding_step_params.py">params</a>) -> object</code>
- <code title="patch /v1/profile">client.profile.<a href="./src/resalign/resources/profile.py">update_preferences</a>(\*\*<a href="src/resalign/types/profile_update_preferences_params.py">params</a>) -> object</code>

# Recommendations

Types:

```python
from resalign.types import RecommendationRefreshBatchResponse
```

Methods:

- <code title="get /v1/recommendations">client.recommendations.<a href="./src/resalign/resources/recommendations.py">list</a>() -> object</code>
- <code title="post /v1/recommendations/refresh">client.recommendations.<a href="./src/resalign/resources/recommendations.py">refresh</a>() -> object</code>
- <code title="post /v1/recommendations/refresh-batch">client.recommendations.<a href="./src/resalign/resources/recommendations.py">refresh_batch</a>(\*\*<a href="src/resalign/types/recommendation_refresh_batch_params.py">params</a>) -> <a href="./src/resalign/types/recommendation_refresh_batch_response.py">RecommendationRefreshBatchResponse</a></code>

# Assessments

Types:

```python
from resalign.types import AssessmentAutoAssessResponse
```

Methods:

- <code title="post /v1/assessments/auto-assess">client.assessments.<a href="./src/resalign/resources/assessments.py">auto_assess</a>(\*\*<a href="src/resalign/types/assessment_auto_assess_params.py">params</a>) -> <a href="./src/resalign/types/assessment_auto_assess_response.py">AssessmentAutoAssessResponse</a></code>

# Notifications

Types:

```python
from resalign.types import NotificationDeliverResponse
```

Methods:

- <code title="post /v1/notifications/deliver">client.notifications.<a href="./src/resalign/resources/notifications/notifications.py">deliver</a>() -> <a href="./src/resalign/types/notification_deliver_response.py">NotificationDeliverResponse</a></code>

## Preferences

Types:

```python
from resalign.types.notifications import PreferenceRetrieveResponse, PreferenceUpdateResponse
```

Methods:

- <code title="get /v1/notifications/preferences">client.notifications.preferences.<a href="./src/resalign/resources/notifications/preferences.py">retrieve</a>() -> <a href="./src/resalign/types/notifications/preference_retrieve_response.py">PreferenceRetrieveResponse</a></code>
- <code title="put /v1/notifications/preferences">client.notifications.preferences.<a href="./src/resalign/resources/notifications/preferences.py">update</a>(\*\*<a href="src/resalign/types/notifications/preference_update_params.py">params</a>) -> <a href="./src/resalign/types/notifications/preference_update_response.py">PreferenceUpdateResponse</a></code>
