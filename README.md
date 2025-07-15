SpaceFinderProject - Python Detection
캡스톤디자인 프로젝트 - 영진전문대
공공 주차장 또는 특정 영역에서 **빈 공간(주차 공간 등)**을 인식하는 프로젝트입니다.
영상 분석을 기반으로 Python과 OpenCV, Tesseract OCR을 사용하여 객체를 탐지합니다.

[관련영상](youtube.com/watch?v=xfp5TvkjUxA&list=PLDisgK6MxjFKBhqInjR0iObMXaK_3zJRi&index=10)

./
|- SpaceFinderModules
|   |- init.py                  # 패키지 구성파일
|   |- Caculaters.py            # 계산관련 함수 모음
|   |- Detecters.py             # OpenCV 를 이용한 사각형 탐지 함수
|   |- ImageConverters.py       # 전처리를 위한 이미지 함수 모음
|   |- SpaceFinderClasses.py    # 사각형의 좌표 및 기타 정보를 저장하는 Class
|- detectionCarInLine.py   # 추자공간 탐지를 인식 구현 코드
|- ExCam.py                # 캠의 동작 테스트
|- AccTest.py              # 정렬 테스트를 위해서 만든 테스트코드(중요하지않음 추후 정리필요)
|- pyTest.py               # 실제적으로 읽어낸 주차공간을 바탕으로 차가 대져 있는지 판단하는 코드
|- readText.py             # 주차장에 진입전 번호판을 읽기 위해 Tesseract OCR 을 이용하여 글자를 텍스트 정보를 읽는 코드
|- .pydevproject
|- .project
|- .gitignore
|- README.md

사용 기술
- Python
- OpenCV : 영상 처리 및 이미지 필터링
- Tesseract OCR : 이미지에서 문자 인식

2021년에 제작되었습니다.
