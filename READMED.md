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
- **React 18** + **TypeScript** - 型安全性の保証
- **Next.js 14** - App Routerベースのモダンウェブフレームワーク
- **TailwindCSS** + **shadcn/ui** - 一貫したデザインシステム
- **i18next** - 多言語対応（日本語、英語、韓国語）

#### バックエンド
- **FastAPI** - 高性能Pythonウェブフレームワーク
- **PostgreSQL** - リレーショナルデータベース
- **Redis** - キャッシュとリアルタイム機能
- **Celery** - 非同期タスク処理

#### AI/ML
- **OpenAI GPT-4 API** - メンタルケアチャットボット
- **Transformers** - 日本語感情分析モデル
- **MeCab** - 日本語形態素解析

#### DevOps
- **Docker** - コンテナ化
- **GitHub Actions** - CI/CDパイプライン
- **Vercel** - フロントエンド配信
- **Railway** - バックエンド配信

### 🛠️ インストールと実行 {#installation}

#### 前提条件
- Node.js 18以上
- Python 3.9以上
- Docker & Docker Compose

#### 1. 環境変数設定
```bash
cp .env.example .env
# .envファイルを編集して必要な環境変数を設定
```

#### 2. Dockerによる開発環境構築
```bash
docker-compose up -d
```

#### 3. 個別サービス実行
```bash
# フロントエンド
cd frontend && npm install && npm run dev

# バックエンド
cd backend && pip install -r requirements.txt && uvicorn app.main:app --reload
```

### 🎯 ロードマップ {#roadmap}

#### 📅 2024年7月 - フェーズ1（MVP）
- [ ] 基本感情分析機能
- [ ] GPTベースチャットボット
- [ ] ウェブインターフェース

#### 📅 2024年8月 - フェーズ2（拡張）
- [ ] LINE API連携
- [ ] リアルタイム通知システム
- [ ] 感情履歴機能

#### 📅 2024年9月 - フェーズ3（本格運用）
- [ ] パフォーマンス最適化
- [ ] セキュリティ強化
- [ ] 本格配信

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
- **React 18** + **TypeScript** - Type safety guarantee
- **Next.js 14** - Modern web framework based on App Router
- **TailwindCSS** + **shadcn/ui** - Consistent design system
- **i18next** - Multi-language support (Japanese, English, Korean)

#### Backend
- **FastAPI** - High-performance Python web framework
- **PostgreSQL** - Relational database
- **Redis** - Caching and real-time features
- **Celery** - Asynchronous task processing

#### AI/ML
- **OpenAI GPT-4 API** - Mental care chatbot
- **Transformers** - Japanese emotion analysis model
- **MeCab** - Japanese morphological analysis

#### DevOps
- **Docker** - Containerization
- **GitHub Actions** - CI/CD pipeline
- **Vercel** - Frontend deployment
- **Railway** - Backend deployment

### 🛠️ Installation & Setup

#### Prerequisites
- Node.js 18+
- Python 3.9+
- Docker & Docker Compose

#### 1. Environment Variables Setup
```bash
cp .env.example .env
# Edit .env file to set required environment variables
```

#### 2. Development Environment with Docker
```bash
docker-compose up -d
```

#### 3. Individual Service Execution
```bash
# Frontend
cd frontend && npm install && npm run dev

# Backend
cd backend && pip install -r requirements.txt && uvicorn app.main:app --reload
```

### 🎯 Roadmap

#### 📅 July 2024 - Phase 1 (MVP)
- [ ] Basic emotion analysis functionality
- [ ] GPT-based chatbot
- [ ] Web interface

#### 📅 August 2024 - Phase 2 (Enhancement)
- [ ] LINE API integration
- [ ] Real-time notification system
- [ ] Emotion history feature

#### 📅 September 2024 - Phase 3 (Production)
- [ ] Performance optimization
- [ ] Security enhancement
- [ ] Production deployment

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
- **React 18** + **TypeScript** - 타입 안정성 보장
- **Next.js 14** - App Router 기반 모던 웹 프레임워크
- **TailwindCSS** + **shadcn/ui** - 일관된 디자인 시스템
- **i18next** - 다국어 지원 (일본어, 영어, 한국어)

#### 백엔드
- **FastAPI** - 고성능 Python 웹 프레임워크
- **PostgreSQL** - 관계형 데이터베이스
- **Redis** - 캐싱 및 실시간 기능
- **Celery** - 비동기 작업 처리

#### AI/ML
- **OpenAI GPT-4 API** - 멘탈 케어 챗봇
- **Transformers** - 일본어 감정 분석 모델
- **MeCab** - 일본어 형태소 분석

#### DevOps
- **Docker** - 컨테이너화
- **GitHub Actions** - CI/CD 파이프라인
- **Vercel** - 프론트엔드 배포
- **Railway** - 백엔드 배포

### 🛠️ 설치 및 실행

#### 사전 요구사항
- Node.js 18+
- Python 3.9+
- Docker & Docker Compose

#### 1. 환경 변수 설정
```bash
cp .env.example .env
# .env 파일을 편집하여 필요한 환경 변수 설정
```

#### 2. Docker로 개발 환경 구성
```bash
docker-compose up -d
```

#### 3. 개별 서비스 실행
```bash
# 프론트엔드
cd frontend && npm install && npm run dev

# 백엔드
cd backend && pip install -r requirements.txt && uvicorn app.main:app --reload
```

### 🎯 로드맵

#### 📅 2024년 7월 - 1단계 (MVP)
- [ ] 기본 감정 분석 기능
- [ ] GPT 기반 챗봇
- [ ] 웹 인터페이스

#### 📅 2024년 8월 - 2단계 (확장)
- [ ] LINE API 연동
- [ ] 실시간 알림 시스템
- [ ] 감정 히스토리 기능

#### 📅 2024년 9월 - 3단계 (운영)
- [ ] 성능 최적화
- [ ] 보안 강화
- [ ] 프로덕션 배포

---

## 📊 プロジェクト現況 / Project Status / 프로젝트 현황

### 開発進捗度 / Development Progress / 개발 진행도
- [x] プロジェクト企画・設計 / Project Planning & Design / 프로젝트 기획 및 설계
- [x] 技術スタック選定 / Tech Stack Selection / 기술 스택 선정
- [x] 開発環境構築 / Development Environment Setup / 개발 환경 구성
- [ ] バックエンドAPI開発 / Backend API Development / 백엔드 API 개발 (진행 중)
- [ ] フロントエンドUI開発 / Frontend UI Development / 프론트엔드 UI 개발 (진행 중)

### パフォーマンス目標 / Performance Goals / 성능 목표
- **感情分析精度 / Emotion Analysis Accuracy / 감정 분석 정확도**: 目標95% / Target 95% / 목표 95%
- **応答時間 / Response Time / 응답 시간**: 目標100ms以内 / Target <100ms / 목표 100ms 이내
- **可用性 / Availability / 가용성**: 目標99.9% / Target 99.9% / 목표 99.9%

---

## 🤝 Contributing

このプロジェクトへの貢献を歓迎します！イシューやPRを通じてご参加ください。

Contributions to this project are welcome! Please participate through issues or PRs.

프로젝트 기여를 환영합니다! 이슈나 PR을 통해 참여해주세요.

---

## 📄 License

このプロジェクトはMITライセンスの下にあります。詳細は[LICENSE](LICENSE)ファイルを参照してください。

This project is under the MIT License. See the [LICENSE](LICENSE) file for details.

이 프로젝트는 MIT 라이선스 하에 있습니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.

---

## 👥 Developer

**開発者 / Developer / 개발자**: [Hyeon]
- 🐱 GitHub: [@yhyeon-marina](https://github.com/hyeon-marina)
- 📧 Email: hyeon.marina@gmail.com
- 🌐 Blog: [Zenn](https://zenn.dev/hyeon_marina247) | [Qiita](https://qiita.com/hyeon)

---

## 🙏 謝辞 / Acknowledgments / 감사의 말

このプロジェクトは以下のオープンソースプロジェクトの支援を受けています：

This project is supported by the following open-source projects:

이 프로젝트는 다음 오픈소스 프로젝트들의 도움을 받았습니다:

- [OpenAI](https://openai.com/) - GPT APIの提供 / GPT API provision / GPT API 제공
- [Hugging Face](https://huggingface.co/) - 日本語BERTモデル / Japanese BERT model / 일본어 BERT 모델
- [LINE Developers](https://developers.line.biz/) - LINE APIプラットフォーム / LINE API platform / LINE API 플랫폼

---

<div align="center">
  <p>⭐ このプロジェクトが役に立ったら、スターを押してください！ ⭐</p>
  <p>⭐ If this project helped you, please give it a star! ⭐</p>
  <p>⭐ 이 프로젝트가 도움이 되었다면 스타를 눌러주세요! ⭐</p>
  
  <p><strong>🛡️ SafeTalk - デジタル空間での安全なコミュニケーションのために</strong></p>
  <p><strong>🛡️ SafeTalk - For Safe Communication in Digital Spaces</strong></p>
  <p><strong>🛡️ SafeTalk - 디지털 공간에서의 안전한 소통을 위하여</strong></p>
</div>