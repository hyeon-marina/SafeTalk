"""
SafeTalk 설정 관리 모듈

환경변수를 통한 애플리케이션 설정 관리
"""

import os
from typing import Optional
from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    """애플리케이션 설정 클래스"""
    
    # 기본 설정
    app_name: str = "SafeTalk API"
    debug: bool = Field(default=False, env="DEBUG")
    log_level: str = Field(default="info", env="LOG_LEVEL")
    
    # 데이터베이스 설정
    database_url: str = Field(env="DATABASE_URL")
    redis_url: str = Field(env="REDIS_URL")
    
    # OpenAI API 설정
    openai_api_key: str = Field(env="OPENAI_API_KEY")
    
    # LINE API 설정
    line_channel_access_token: Optional[str] = Field(default=None, env="LINE_CHANNEL_ACCESS_TOKEN")
    line_channel_secret: Optional[str] = Field(default=None, env="LINE_CHANNEL_SECRET")
    
    # 보안 설정
    secret_key: str = Field(env="SECRET_KEY")
    algorithm: str = Field(default="HS256", env="ALGORITHM")
    access_token_expire_minutes: int = Field(default=30, env="ACCESS_TOKEN_EXPIRE_MINUTES")
    
    # CORS 설정
    allowed_origins: list[str] = [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "https://safetalk.vercel.app"  # 프로덕션 도메인 (나중에)
    ]
    
    class Config:
        env_file = ".env"
        case_sensitive = False

# 전역 설정 인스턴스
settings = Settings()

# 개발/프로덕션 환경 확인
def is_development() -> bool:
    """개발 환경인지 확인"""
    return settings.debug

def is_production() -> bool:
    """프로덕션 환경인지 확인"""
    return not settings.debug

# 설정 검증
def validate_settings() -> dict:
    """필수 설정값들이 제대로 설정되었는지 검증"""
    issues = []
    
    # 필수 환경변수 체크
    required_vars = [
        ("DATABASE_URL", settings.database_url),
        ("REDIS_URL", settings.redis_url),
        ("OPENAI_API_KEY", settings.openai_api_key),
        ("SECRET_KEY", settings.secret_key)
    ]
    
    for var_name, var_value in required_vars:
        if not var_value or var_value.startswith("your_"):
            issues.append(f"{var_name}이 설정되지 않았거나 기본값입니다")
    
    # OpenAI API 키 형식 체크
    if settings.openai_api_key and not settings.openai_api_key.startswith("sk-"):
        issues.append("OPENAI_API_KEY 형식이 올바르지 않습니다 (sk-로 시작해야 함)")
    
    return {
        "valid": len(issues) == 0,
        "issues": issues,
        "environment": "development" if is_development() else "production"
    }