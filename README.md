# 🛡️ SafeTalk

<div align="center">
  <h3>AI駆動型デジタルケア・対応プラットフォーム</h3>
  <p>サイバーいじめと憎悪表現をリアルタイムで検知し、被害者に感情的支援と行動ガイドを提供するサービス</p>
  
  <p>
    <a href="#features">✨ 主要機能</a> •
    <a href="#tech-stack">🏗️ 技術スタック</a> •
    <a href="#installation">🛠️ インストール</a> •
    <a href="#roadmap">🎯 ロードマップ</a>
  </p>
  
  <p>
    <a href="#japanese">🇯🇵 日本語</a> •
    <a href="#english">🇺🇸 English</a> •
    <a href="#korean">🇰🇷 한국어</a>
  </p>

  ![GitHub last commit](https://img.shields.io/github/last-commit/hyeon-marina/SafeTalk)
  ![GitHub issues](https://img.shields.io/github/issues/hyeon-marina/SafeTalk)
  ![GitHub stars](https://img.shields.io/github/stars/hyeon-marina/SafeTalk)
  ![License](https://img.shields.io/github/license/hyeon-marina/SafeTalk)
</div>

---

## 🇯🇵 日本語 {#japanese}

### ✨ 主要機能 {#features}

#### 🤖 リアルタイム感情分析
- 日本語特化BERTモデルを活用した高精度感情分析
- サイバーいじめ・憎悪表現のリアルタイム検知
- 感情状態の可視化と重要度分類

#### 💬 GPTベースのメンタルケアチャットボット
- 日本の文化的文脈を反映した共感型対話
- 個人化された感情的支援と対処法の提供
- 24時間365日の安全な匿名相談サービス

#### 🛡️ プライバシー優先設計
- ゼロトラストデータ処理方式
- クライアントサイド匿名化システム
- ユーザーデータ主権の保証

### 🏗️ 技術スタック {#tech-stack}

#### フロントエンド
- **React 18.2+** + **TypeScript 5.0+** - 型安全性の保証
- **Next.js 14.0+** - App Routerベースのモダンウェブフレームワーク
- **TailwindCSS 3.4+** + **shadcn/ui** - 一貫したデザインシステム
- **i18next** - 多言語対応（日本語、英語、韓国語）

#### バックエンド
- **FastAPI 0.104+** - 高性能Pythonウェブフレームワーク
- **PostgreSQL 15** - リレーショナルデータベース
- **Redis 7** - キャッシュとリアルタイム機能
- **Celery** - 非同期タスク処理

#### AI/ML
- **OpenAI GPT-4 API** - メンタルケアチャットボット
- **Transformers 4.35+** - 日本語感情分析モデル
- **MeCab** - 日本語形態素解析
- **scikit-learn** - 機械学習モデル

#### DevOps
- **Docker** + **Docker Compose** - コンテナ化
- **GitHub Actions** - CI/CDパイプライン
- **Vercel** - フロントエンド配信
- **Railway** - バックエンド配信

### 🛠️ インストールと実行 {#installation}

#### 前提条件 (macOS M4 基準)
- **Node.js 18.0+** - `brew install node`
- **Python 3.11+** - `brew install python@3.11`
- **Docker Desktop** - [Apple Silicon版ダウンロード](https://desktop.docker.com/mac/main/arm64/Docker.dmg)

#### 1. リポジトリクローン
```bash
git clone https://github.com/hyeon-marina/SafeTalk.git
cd SafeTalk
```

#### 2. 環境変数設定
```bash
cp .env.example .env
# .envファイルを編集して必要な環境変数を設定
```

必要な環境変数:
- `OPENAI_API_KEY`: OpenAI API キー
- `LINE_CHANNEL_ACCESS_TOKEN`: LINE チャンネルアクセストークン
- `LINE_CHANNEL_SECRET`: LINE チャンネルシークレット
- `DATABASE_URL`: PostgreSQL 接続 URL
- `REDIS_URL`: Redis 接続 URL

#### 3. Dockerによる開発環境構築
```bash
# データベースサービス起動
docker-compose up -d

# 依存関係確認
docker-compose ps
```

#### 4. バックエンド起動
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

#### 5. フロントエンド起動（新しいターミナル）
```bash
cd frontend
npm install
npm run dev
```

#### 6. 動作確認
- フロントエンド: http://localhost:3000
- バックエンドAPI: http://localhost:8000
- API文書: http://localhost:8000/docs

### 🎯 ロードマップ {#roadmap}

#### 📅 2025年8月 - フェーズ1（MVP開発）
- [x] プロジェクト企画・設計
- [x] 開発環境構築
- [ ] 基本感情分析機能実装
- [ ] GPTベースチャットボット開発
- [ ] ウェブインターフェース構築

#### 📅 2025年9月 - フェーズ2（機能拡張）
- [ ] LINE API連携
- [ ] リアルタイム通知システム
- [ ] 感情履歴・レポート機能
- [ ] セキュリティ強化

#### 📅 2025年10月 - フェーズ3（本格運用）
- [ ] パフォーマンス最適化
- [ ] 本格配信
- [ ] ドキュメント完成
- [ ] ポートフォリオ公開

### 📊 プロジェクト現況

#### 開発進捗度
- [x] プロジェクト企画・設計 (100%)
- [x] 技術スタック選定 (100%)
- [x] 開発環境構築 (90%)
- [ ] バックエンドAPI開発 (20%)
- [ ] フロントエンドUI開発 (10%)
- [ ] AI/ML モデル統合 (0%)

#### パフォーマンス目標
- **感情分析精度**: 目標95%以上
- **応答時間**: 目標100ms以内
- **可用性**: 目標99.9%

---

## 🇺🇸 English {#english}

### ✨ Key Features

#### 🤖 Real-time Emotion Analysis
- High-precision emotion analysis using Japanese-specialized BERT models
- Real-time detection of cyberbullying and hate speech
- Emotion state visualization and severity classification

#### 💬 GPT-based Mental Care Chatbot
- Empathetic conversations reflecting Japanese cultural context
- Personalized emotional support and coping strategies
- 24/7 safe anonymous counseling service

#### 🛡️ Privacy-First Design
- Zero-trust data processing approach
- Client-side anonymization system
- User data sovereignty guarantee

### 🏗️ Tech Stack

#### Frontend
- **React 18.2+** + **TypeScript 5.0+** - Type safety guarantee
- **Next.js 14.0+** - Modern web framework based on App Router
- **TailwindCSS 3.4+** + **shadcn/ui** - Consistent design system
- **i18next** - Multi-language support (Japanese, English, Korean)

#### Backend
- **FastAPI 0.104+** - High-performance Python web framework
- **PostgreSQL 15** - Relational database
- **Redis 7** - Caching and real-time features
- **Celery** - Asynchronous task processing

#### AI/ML
- **OpenAI GPT-4 API** - Mental care chatbot
- **Transformers 4.35+** - Japanese emotion analysis model
- **MeCab** - Japanese morphological analysis
- **scikit-learn** - Machine learning models

#### DevOps
- **Docker** + **Docker Compose** - Containerization
- **GitHub Actions** - CI/CD pipeline
- **Vercel** - Frontend deployment
- **Railway** - Backend deployment

### 🛠️ Installation & Setup

#### Prerequisites (macOS M4)
- **Node.js 18.0+** - `brew install node`
- **Python 3.11+** - `brew install python@3.11`
- **Docker Desktop** - [Download for Apple Silicon](https://desktop.docker.com/mac/main/arm64/Docker.dmg)

#### Quick Start
```bash
# Clone repository
git clone https://github.com/hyeon-marina/SafeTalk.git
cd SafeTalk

# Setup environment
cp .env.example .env
# Edit .env with your configuration

# Start services
docker-compose up -d

# Backend (Terminal 1)
cd backend && pip install -r requirements.txt
uvicorn app.main:app --reload

# Frontend (Terminal 2)
cd frontend && npm install && npm run dev
```

### 🎯 Roadmap

#### 📅 August 2025 - Phase 1 (MVP Development)
- [x] Project planning & design
- [x] Development environment setup
- [ ] Basic emotion analysis implementation
- [ ] GPT-based chatbot development
- [ ] Web interface construction

#### 📅 September 2025 - Phase 2 (Feature Enhancement)
- [ ] LINE API integration
- [ ] Real-time notification system
- [ ] Emotion history & reporting
- [ ] Security enhancement

#### 📅 October 2025 - Phase 3 (Production Ready)
- [ ] Performance optimization
- [ ] Production deployment
- [ ] Documentation completion
- [ ] Portfolio publication

---

## 🇰🇷 한국어 {#korean}

### ✨ 주요 기능

#### 🤖 실시간 감정 분석
- 일본어 특화 BERT 모델을 활용한 고정밀 감정 분석
- 사이버 괴롭힘 및 혐오 표현 실시간 탐지
- 감정 상태 시각화 및 심각도 분류

#### 💬 GPT 기반 멘탈 케어 챗봇
- 일본 문화적 맥락을 반영한 공감형 대화
- 개인화된 정서적 지지 및 대처 방안 제공
- 24/7 안전한 익명 상담 서비스

#### 🛡️ 개인정보 보호 우선 설계
- 제로 트러스트 데이터 처리 방식
- 클라이언트 사이드 익명화 시스템
- 사용자 데이터 주권 보장

### 🏗️ 기술 스택

#### 프론트엔드
- **React 18.2+** + **TypeScript 5.0+** - 타입 안정성 보장
- **Next.js 14.0+** - App Router 기반 모던 웹 프레임워크
- **TailwindCSS 3.4+** + **shadcn/ui** - 일관된 디자인 시스템
- **i18next** - 다국어 지원 (일본어, 영어, 한국어)

#### 백엔드
- **FastAPI 0.104+** - 고성능 Python 웹 프레임워크
- **PostgreSQL 15** - 관계형 데이터베이스
- **Redis 7** - 캐싱 및 실시간 기능
- **Celery** - 비동기 작업 처리

#### AI/ML
- **OpenAI GPT-4 API** - 멘탈 케어 챗봇
- **Transformers 4.35+** - 일본어 감정 분석 모델
- **MeCab** - 일본어 형태소 분석
- **scikit-learn** - 머신러닝 모델

#### DevOps
- **Docker** + **Docker Compose** - 컨테이너화
- **GitHub Actions** - CI/CD 파이프라인
- **Vercel** - 프론트엔드 배포
- **Railway** - 백엔드 배포

### 🛠️ 설치 및 실행

#### 사전 요구사항 (macOS M4 기준)
- **Node.js 18.0+** - `brew install node`
- **Python 3.11+** - `brew install python@3.11`
- **Docker Desktop** - [Apple Silicon용 다운로드](https://desktop.docker.com/mac/main/arm64/Docker.dmg)

#### 빠른 시작
```bash
# 저장소 클론
git clone https://github.com/hyeon-marina/SafeTalk.git
cd SafeTalk

# 환경 설정
cp .env.example .env
# .env 파일을 본인 설정에 맞게 편집

# 서비스 시작
docker-compose up -d

# 백엔드 (터미널 1)
cd backend && pip install -r requirements.txt
uvicorn app.main:app --reload

# 프론트엔드 (터미널 2)
cd frontend && npm install && npm run dev
```

#### 접속 확인
- **프론트엔드**: http://localhost:3000
- **백엔드 API**: http://localhost:8000
- **API 문서**: http://localhost:8000/docs

### 🎯 로드맵

#### 📅 2025년 8월 - 1단계 (MVP 개발)
- [x] 프로젝트 기획 및 설계
- [x] 개발 환경 구축
- [ ] 기본 감정 분석 기능 구현
- [ ] GPT 기반 챗봇 개발
- [ ] 웹 인터페이스 구축

#### 📅 2025년 9월 - 2단계 (기능 확장)
- [ ] LINE API 연동
- [ ] 실시간 알림 시스템
- [ ] 감정 히스토리 및 리포트 기능
- [ ] 보안 강화

#### 📅 2025년 10월 - 3단계 (운영 준비)
- [ ] 성능 최적화
- [ ] 프로덕션 배포
- [ ] 문서화 완성
- [ ] 포트폴리오 공개

## 🏗️ 프로젝트 구조

```
SafeTalk/
├── 📄 README.md                     # 프로젝트 개요
├── 📄 .gitignore                    # Git 무시 파일
├── 📄 LICENSE                       # MIT 라이선스
├── 📄 CONTRIBUTING.md               # 기여 가이드라인
├── 📄 docker-compose.yml            # 개발 환경 구성
├── 📄 .env.example                  # 환경변수 예시
├── 📄 package.json                  # 모노레포 루트 설정
├── 📁 .github/                      # GitHub 워크플로우
│   └── workflows/
│       └── ci.yml                   # CI/CD 파이프라인
├── 📁 docs/                         # 문서 모음
│   ├── 📄 architecture.md           # 시스템 아키텍처
│   ├── 📄 api-specification.md      # API 명세서
│   └── 📄 development-guide.md      # 개발 가이드
├── 📁 frontend/                     # Next.js 프론트엔드
│   ├── 📄 package.json
│   ├── 📄 next.config.js
│   ├── 📄 tailwind.config.js
│   ├── 📄 tsconfig.json
│   └── 📁 src/
│       ├── 📁 app/                  # Next.js 14 App Router
│       ├── 📁 components/           # React 컴포넌트
│       ├── 📁 hooks/                # 커스텀 훅
│       ├── 📁 lib/                  # 유틸리티 라이브러리
│       └── 📁 types/                # TypeScript 타입 정의
├── 📁 backend/                      # FastAPI 백엔드
│   ├── 📄 requirements.txt
│   ├── 📄 Dockerfile
│   └── 📁 app/
│       ├── 📄 main.py               # FastAPI 진입점
│       ├── 📁 api/                  # API 라우터
│       ├── 📁 core/                 # 핵심 비즈니스 로직
│       ├── 📁 models/               # 데이터 모델
│       └── 📁 services/             # 서비스 레이어
└── 📁 ml/                           # 머신러닝 모델
    ├── 📄 requirements.txt
    ├── 📁 notebooks/                # Jupyter 노트북
    ├── 📁 models/                   # 학습된 모델
    └── 📄 README.md
```

## 🤝 Contributing

이 프로젝트는 일본 AI 신졸 취업을 위한 포트폴리오 목적으로 개발되고 있습니다. 
기여를 원하시는 분은 [CONTRIBUTING.md](CONTRIBUTING.md)를 참고해주세요.

### 개발 워크플로우
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add some amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

## 📄 License

이 프로젝트는 MIT 라이선스 하에 있습니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.

## 👥 Developer

**개발자**: Hyeon
- 🐱 **GitHub**: [@hyeon-marina](https://github.com/hyeon-marina)
- 📧 **Email**: hyeon.marina@gmail.com
- 🌐 **Blog**: [Zenn](https://zenn.dev/hyeon_marina247) | [Qiita](https://qiita.com/hyeon)
- 💼 **LinkedIn**: [hyeon-marina](https://linkedin.com/in/hyeon-marina)

## 🙏 Acknowledgments

이 프로젝트는 다음 오픈소스 프로젝트들의 도움을 받았습니다:

- [OpenAI](https://openai.com/) - GPT API 제공
- [Hugging Face](https://huggingface.co/) - 일본어 BERT 모델
- [LINE Developers](https://developers.line.biz/) - LINE API 플랫폼
- [FastAPI](https://fastapi.tiangolo.com/) - 고성능 Python 웹 프레임워크
- [Next.js](https://nextjs.org/) - React 기반 웹 프레임워크

## 📈 프로젝트 상태

![GitHub commit activity](https://img.shields.io/github/commit-activity/m/hyeon-marina/SafeTalk)
![GitHub code size](https://img.shields.io/github/languages/code-size/hyeon-marina/SafeTalk)
![GitHub top language](https://img.shields.io/github/languages/top/hyeon-marina/SafeTalk)

---

<div align="center">
  <p>⭐ 이 프로젝트가 도움이 되었다면 스타를 눌러주세요! ⭐</p>
  <p><strong>🛡️ SafeTalk - 디지털 공간에서의 안전한 소통을 위하여</strong></p>
  <p><em>For Safe Communication in Digital Spaces</em></p>
</div>
