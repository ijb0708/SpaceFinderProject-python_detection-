# SpaceFinderProject - Python Detection
> **영진전문대 캡스톤디자인 프로젝트**
> 공공 주차장 또는 특정 영역에서 **빈 공간(주차 공간 등)**을 인식하는 프로젝트입니다.
> 영상 분석을 기반으로 Python과 OpenCV, Tesseract OCR을 사용하여 객체를 탐지합니다.

[관련영상](youtube.com/watch?v=xfp5TvkjUxA&list=PLDisgK6MxjFKBhqInjR0iObMXaK_3zJRi&index=10)

---
 ## 프로젝트 구조
 ```
./
├── SpaceFinderModules/              # 주요 기능 모듈 폴더
│   ├── __init__.py                  # 패키지 초기화 파일
│   ├── Caculaters.py                # 계산 관련 함수 모음
│   ├── Detecters.py                 # OpenCV 기반 사각형 탐지 함수
│   ├── ImageConverters.py           # 이미지 전처리 함수 모음
│   └── SpaceFinderClasses.py        # 사각형 좌표 및 상태 저장 클래스 정의
│
├── detectionCarInLine.py            # 주차 공간 인식 및 위치 추적 핵심 코드
├── pyTest.py                        # 실제 주차 여부 판단 구현 코드
├── readText.py                      # 번호판 인식을 위한 Tesseract OCR 모듈
│
├── ExCam.py                         # 카메라 동작 테스트용 코드
├── AccTest.py                       # 정렬 알고리즘 테스트용 (임시, 추후 정리 필요)
│
├── .gitignore                       # Git 버전관리 제외 설정
├── .pydevproject                    # PyDev 프로젝트 설정 파일
├── .project                         # Eclipse 프로젝트 설정 파일
└── README.md                        # 현재 문서
```

---

사용 기술
- **Python 3**
- **OpenCV** : 이미지 및 사각형 탐지
- **Tesseract OCR** : 번호판 문자 인식
- **NumPy** : 수치 연산


> The program was created in 2021 as part of a Capstone Design Project at Yeungjin College.
