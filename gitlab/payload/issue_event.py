from typing import List, Optional
from pydantic import BaseModel

class User(BaseModel):
    id: Optional[int]
    name: Optional[str]
    username: Optional[str]
    avatar_url: Optional[str]
    email: Optional[str]

class Assignee(BaseModel):
    name: Optional[str]
    username: Optional[str]
    avatar_url: Optional[str]

class Project(BaseModel):
    id: Optional[int]
    name: Optional[str]
    description: Optional[str]
    web_url: Optional[str]
    avatar_url: Optional[str]
    git_ssh_url: Optional[str]
    git_http_url: Optional[str]
    namespace: Optional[str]
    visibility_level: Optional[int]
    path_with_namespace: Optional[str]
    default_branch: Optional[str]
    ci_config_path: Optional[str]
    homepage: Optional[str]
    url: Optional[str]
    ssh_url: Optional[str]
    http_url: Optional[str]

class Label(BaseModel):
    id: Optional[int]
    title: Optional[str]
    color: Optional[str]
    project_id: Optional[int]
    created_at: Optional[str]
    updated_at: Optional[str]
    template: Optional[bool]
    description: Optional[str]
    type: Optional[str]
    group_id: Optional[int]

class EscalationPolicy(BaseModel):
    id: Optional[int]
    name: Optional[str]

class ObjectAttributes(BaseModel):
    id: Optional[int]
    title: Optional[str]
    assignee_ids: Optional[List[int]]
    assignee_id: Optional[int]
    author_id: Optional[int]
    project_id: Optional[int]
    created_at: Optional[str]
    updated_at: Optional[str]
    updated_by_id: Optional[int]
    last_edited_at: Optional[str]
    last_edited_by_id: Optional[int]
    relative_position: Optional[int]
    description: Optional[str]
    milestone_id: Optional[int]
    state_id: Optional[int]
    confidential: Optional[bool]
    discussion_locked: Optional[bool]
    due_date: Optional[str]
    moved_to_id: Optional[int]
    duplicated_to_id: Optional[int]
    time_estimate: Optional[int]
    total_time_spent: Optional[int]
    time_change: Optional[int]
    human_total_time_spent: Optional[str]
    human_time_estimate: Optional[str]
    human_time_change: Optional[str]
    weight: Optional[int]
    iid: Optional[int]
    url: Optional[str]
    state: Optional[str]
    action: Optional[str]
    severity: Optional[str]
    escalation_status: Optional[str]
    escalation_policy: Optional[EscalationPolicy]
    labels: Optional[List[Label]]

class Repository(BaseModel):
    name: Optional[str]
    url: Optional[str]
    description: Optional[str]
    homepage: Optional[str]

class IssueEventPayload(BaseModel):
    object_kind: Optional[str]
    event_type: Optional[str]
    user: Optional[User]
    project: Optional[Project]
    object_attributes: Optional[ObjectAttributes]
    repository: Optional[Repository]
    assignees: Optional[List[Assignee]]
    assignee: Optional[Assignee]
    labels: Optional[List[Label]]
    changes: Optional[dict]
