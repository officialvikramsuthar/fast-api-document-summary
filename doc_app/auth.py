from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from doc_app.dependencies import get_settings

security = HTTPBasic()


def get_current_user(credentials: HTTPBasicCredentials = Depends(security)):
    settings = get_settings()
    correct_username = settings.username
    correct_password = settings.password

    if credentials.username != correct_username or credentials.password != correct_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username
