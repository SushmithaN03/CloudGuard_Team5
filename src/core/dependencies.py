from fastapi import Depends
from fastapi import HTTPException


def require_role(required_role):

    def checker(current_user=Depends(get_current_user)):

        if current_user.role != required_role:
            raise HTTPException(
                status_code=403,
                detail="Unauthorized"
            )

        return current_user

    return checker