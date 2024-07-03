# 라이브러리 상하관계

외부 라이브러리(pip install ~~ 등을 사용하는) 는 경우에는 링크를 걸어두었다. 예시 : [discord.py](<https://pypi.org/project/discord.py/>)

| 파일 | 참조하는 라이브러리 |
|-|-|
| **이 프로그램의 모든 파일들** | [discord.py](<https://pypi.org/project/discord.py/>) |

## 기본 라이브러리
| 라이브러리 이름 | 참조하는 라이브러리 |
|-|-|
| botsetup.py | **설치 시 기본제공** |
| file.py | - |
| MemoUI.py | *botsetup.py*, file.py |

## 추가 기능

| 추가 기능 이름 | 참조하는 라이브러리 | 참고사항 |
|-|-|-|
| ~~Admin.py~~ | **설치 시 기본제공** | - |
| Botplus.py | - | 랜덤 리스트 추첨 기능 제작 시 file 라이브러리 필요할 예정 |
| Memo.py | *botsetup.py*, file.py, MemoUI.py | - |
| Tts.py | [gTTS](<https://pypi.org/project/gTTS/>), discord.py[voice] *botsetup.py* | 사용 시 ffmpeg가 PATH에 포함되어 있어야 됨. voice는 ```pip install discord.py[voice]``` 를 이용하여 설치 가능 |