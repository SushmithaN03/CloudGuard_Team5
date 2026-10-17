from pydantic import BaseModel


class Policy(BaseModel):
    id: int
    name: str
    policy_type: str
    severity: str
    auto_remediate: bool
