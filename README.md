# DSschool

## IPython 및 주피터 설정

IPython 및 주피터 설정 디렉토리
IPython, 또는 주피터 QtConsole, 주피터 노트북이 설치되면 사용자 홈 디렉토리 아래에 .ipython 이라는 디렉토리가 생기는데 이 디렉토리가 설정 디렉토리이다. 주피터라는 이름으로 바뀌기 전에는 ipython이라는 이름이 공통으로 사용되었기 때문에 이름이 바뀐 현재에도 이 이름으로 설정 디렉토리를 사용할 수 있다.


.ipython 디렉토리가 보이지 않는 경우

윈도우즈에서는 탐색기에서 보기 > 옵션 > "폴더 및 검색 옵션 변경"을 눌러 다이얼로그를 띄운 뒤 "보기" 탭에서 "숨긴 파일, 폴더 및 드라이브 표시"에 체크한다.


맥 OS에서는 Finder에서 홈 디렉토리로 이동한 뒤 shift + command + .를 누른다.


### 프로필 작성

모든 IPython 또는 주피터 관련 설정은 프로필(profile)에 따라서 다르게 할 수 있다. 프로필은 .ipython 설정 디렉토리 아래에 디렉토리 형태로 저장되는데 기본으로 만들어지는 프로필 디렉토리는 `profile_default` 디렉토리이다.

만약 디폴트 프로필 디렉토리가 없다면 터미널에서 다음 명령으로 만들 수 있다.
```
$ ipython profile create

```

### 설정 파일
설정은 다음 파일을 이용하며 설정 내용은 모든 IPython 과 주피터 QtConsole, Notebook에 공통으로 적용된다.

- 스타트업 파일
- `ipython_config.py` 파일



### 스타트업 파일

스타트업(startup) 파일은 IPython 과 주피터 QtConsole, Notebook 을 이용한 콘솔이 시작되기 전에 실행되는 파일이다. 스타트업 파일은 따로 정해진 이름이 있는 것이 아니라 프로필 디렉토리 아래의 startup 폴더 아래의.py 확장자를 가진 모든 파이썬 스크립트가 스타트업 파일이 되며 파일 이름의 알파벳 순서로 실행된다.

datascienceschool/rpython 도커 이미지의 경우에는 프로필 디렉토리가 /home/dockeruser/.ipython/profile_default/ 이므로 스타트업 파일은 /home/dockeruser/.ipython/profile_default/startup/00.py 이다.

datascienceschool/rpython 도커 이미지에는 파이썬 사용을 쉽게 하기 위해 자주 사용하는 패키지를 미리 00.py라는 이름의 스타트업 파일에서 다음과 같이 임포트하고 있다. 따라서 IPython 과 주피터 QtConsole, Notebook을 사용하는 경우 이 패키지들은 별도의 import 명령 없이 바로 사용할 수 있다.

```
import numpy as np
import scipy as sp
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import statsmodels.stats.api as sms
import sklearn as sk

import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pylab as plt
from mpl_toolkits.mplot3d import Axes3D

import seaborn as sns
sns.set()
sns.set_style("whitegrid")
sns.set_color_codes()
```

단 위의 스타트업 파일이 정상적으로 실행되려면 임포트하고자 하는 패키지가 미리 설치되어 있어야 한다. 위에서 사용하고 있는 패키지들은 다음과 같다. 만약 Anaconda 4.4.0 이상을 설치하였다면 이 패키지들은 모두 자동으로 설치된다.

- NumPy
- SciPy
- Pandas
- Statsmodels
- Scikit-Learn
- Matplotlib
- Seaborn

### ipython_config.py 설정 파일

일부 파이썬 명령은 하나의 스크립트 안에서만 실행되기 때문에 스타트업 파일에 적어 놓아도 실제 IPython 콘솔에는 적용되지 않는다. 예를 들어 from __future__ import 계열의 임포트 명령은 하나의 스크립트 안에서만 영향을 미친다.

이런 경우에는 ipython_config.py 설정 파일안에서 InteractiveShellApp.exec_lines 설정 항목을 다음과 같이 지정하면 된다. InteractiveShellApp.exec_lines 설정 항목은 실행할 명령어 문자열로 이루어진 리스트이다.

다음은 datascienceschool/rpython 도커 이미지에 설정한 ipython_config.py 설정 파일의 예다. 도커 이미지에서는 /home/dockeruser/.ipython/profile_default/ipython_config.py 위치에 저장되어 있다.

```
c = get_config()

c.InteractiveShellApp.exec_lines = [
    "from __future__ import division",  # use python 3 division operator in python 2
    "from __future__ import print_function",  # use python 3's print function, not python 2's print keyword
    "mpl.rc('font', family='nanumgothic')",  # font name
    "mpl.rc('axes', unicode_minus=False)", # for unicode
    "mpl.rc('figure', figsize=(11, 8))",  # figure size (unit: inch)
    "mpl.rc('figure', dpi=300)",  # figure resolution
]

 ```

### 파이썬 스크립트의 경우
위에서 적용한 내용은 모두 IPython, 주피터 QtConsole, 주피터 노트북과 같은 상호작용 콘솔에서만 적용되는 것이고 파이썬 인터프리터를 직접 실행하여 파이썬 스크립트를 가동하는 배치(batch) 실행에는 적용되지 않는다.

### 권장 사항
이제부터 나오는 모든 파이썬 예제 코드는 스타트업 파일과 ipython_config.py 설정 파일이 위에서 적은 대로 설정되어 있다는 가정하에 만들어진 코드들이다. 따라서 각자 사용하는 파이썬 환경에 대해 미리 설정 파일을 적용해 두기를 권장한다.




#### 출처: https://datascienceschool.net/



