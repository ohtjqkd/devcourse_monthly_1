# Monthly1 EDA project

- 열람할 수 있는 웹 사이트 주소 (endpoint) : 'http://ohtjqkd.pythonanywhere.com/'
- 작성한 코드 (github가 있다면 GitHub) : 'https://github.com/ohtjqkd/devcourse_monthly_1'
- 새로 공부한 것들
  - pythonanywhere, aws beanstalk 등 PaaS 서비스를 알게 됨

## _log_

- 2021-05-23 pythonanywhere를 통한 deploy (by. flask framework)
- 2021-05-24 kaggle 필사를 통한 EDA경험 (title. titanic)
- 2021-05-25 plotly + dash 활용 검토 예정
- 2021-05-26 과제 제출, VAERS EDA 진행 중

## 어려웠던 점과 해결 과정

1. 가장 먼저 시도했던 것은 DEPLOY 단계입니다. 새로운 tool을 사용할 때는 언제나 init..이 가장 어려운 과정인 거 같습니다. `wsgi.py`를 설정하는 과정에서 어려움을 가지게 됐습니다.
   - deploy과정을 쉽게 도와주는 다양한 platform을 알게 됐고, 그중에 pythonanywhere를 선택하여 진행하였습니다. wsgi설정에 관해서는 google 검색을 통해 많은 도움을 얻을 수 있었습니다.
2. EDA 과정이 어려웠습니다. 데이터를 분석하고 다루어 본 적이 없었기 때문에 어디서부터 어떻게 시작을 해야 할지 막막했습니다.
   - 먼저 함께 스터디를 하시는 분께서 kaggle필사에 대해서 언급을 해주셨고, 감이 잡히지 않을 때는 익숙해지는 것이 중요하다고 생각이 들어 필사를 먼저 진행해봤습니다. 전체적인 흐름을 한 번 더 경험하니, 조금은 길이 보이기 시작했고 현재 다른 dataset으로 eda를 다시 진행하는 중입니다. 속도가 많이 느리다 보니 과제 제출일인 오늘까지는 공유가 불가할 듯하지만, 계속해서 업데이트하도록 하겠습니다.
3. pandas 관련 method
   - pandas의 많의 기능들을 아직까지는 제대로 사용하지 못하고 있습니다. 이 부분은 계속해서 사용하며 익숙해지도록 하겠습니다.
