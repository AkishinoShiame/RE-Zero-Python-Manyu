# ゼロからパイソン
  
*此為中文版翻譯  
  
## パイソンのリリース / Python Release / Python釋出資訊
  
目前Python由官方提供了兩個基礎版本: Python 2 與 Python 3.    
介於 Python 2 與 Python 3 修改了部份了核心程式導致會有如以下的程式撰寫差異:  
  
```python
print "Hello World" # 於 Python 2 版撰寫此程式碼
print("Hello World") # 於 Python 3 版撰寫此程式碼
```
  
目前 Python 2 的最新版本為 2.7版, 同時官方已聲明在2020年後將終止支援。  
相關的官方發布資訊可 [由此](https://pythonclock.org/) 找到。  
  
至於 Python 3 則依然維持正常的更新與運作。  
對於新手,建議現階段開始以第 3 版進行學習與撰寫而非第 2版。  
  
所有的版本釋出資訊可由 [官網](https://www.python.org/)得知。  
而Linux平台也可由系統內建的套件管理程式以 `install python<version>` 或 `install python<version>-dev`指令進行安裝。  
  
## Enviorment / 使用環境 / ソフトウェアバージョン
  
介紹一些常用的編譯器(IDE)。  

#### [Pycharm]
>   
> 官方提供了兩個版本的PyCharm可使用, 通常建議選擇社群版本(Community Edition)。  
>   
> 社群版本以提供了許多基礎的便利功能而且是免費使用。  
>   
> 官方網頁與編譯器程式下載可由 [此處](https://www.jetbrains.com/pycharm/)取得。  
>   
> 同時他具備獨立的圖形化函式庫管理器，同時可在內部跑多個不同的版本與環境進行測試，對於第一次開發的人是個非常便利的工具。  
>   
> 同時此為一個跨作業系統的IDE，相關的學習與使用資訊也可由 [官網](https://www.jetbrains.com/pycharm/learning-center/) 取得。  
>   
> 目前最建議使用之編譯器(IDE)。  
  
#### [WinPython]
>   
> 此Python編譯器(IDE)為我接觸Python時所使用的編譯器包並是被當時的指導教授所建議使用。  
>  
> 其官方網頁可由[此處](https://winpython.github.io/)查詢，同時他只支援windows作業系統。  
>  
> 由於此編譯器包同時包含一些常用的函式庫，該內含函式庫清單可由[這邊](https://github.com/winpython/winpython/blob/master/changelogs/WinPython-64bit-3.7.4.0.md)取得，因次也是一個給新手使用挺建議的編譯器包。  
>  
> 個人也是使用此編譯器學習[深度學習網站](http://deeplearning.net/tutorial/index.html)的程式與進行開發撰寫。  
>  
> 這整包使用了**Spyder**編譯器作為其預設的程式編輯軟體。
>  
> 這個編譯器包包含了自帶的套件管理程式。  
  
#### [Anaconda]
>  
> 此編譯器包是由我的一位摯友所推薦。  
>  
> 由於WinPython無法提供支援給macOS作業系統進行使用，此編譯器包曾為一個不錯的選擇可推給macOS的使用者。  
>  
> 大體上他跟WinPython接近，同時包含自己的函式庫套件管理工具，但也可以使用官方提供的工具套件安裝。  
>  
> 此編譯器包也是使用**Spyter**編譯器作為其預設的程式編輯軟體。  
>  
> 關於官方網站與軟體下載可由[此處](https://www.anaconda.com/)取得。  
>  
> 在**Pycharm**變的更加知名與好用以前，此集成包仍提供Python開發者一個不錯的環境。  
>  
> 從該程式之官方網頁將此編輯器包定義為`The Enterprise Data Science Platform`(提供給企業的資料科學平台)但他也提供給一般使用者做為免費開發的選擇。  
  
#### [Spyder]
>  
> 這是基於python程式碼所建立出來的Python編譯器。  
>  
> 此編譯器當初也是以資料科學所使用為基礎進行開發。
>  
> `Spyter`所支援的作業系統橫跨所有平台。 可獨立由Python官方提供之`pip`工具進行安裝。  
>  
> 官網與相關資訊可由[此處](https://www.spyder-ide.org/)前往。  
>  
> 依據個人經驗，較不建議使用pip進行直接安裝。由於原始程式碼語系撰寫問題，將影響到程式對系統語系的錯誤判讀，導致程式無法開啟/運作。  
  
## Library Installation / ライブラリのインストール / 安裝函式庫
  
Python官方建議使用其附屬之套件管理程式進行任何函式庫安裝: `pip`.  
  
在Windows系統上，已經包裝在Python官方所提供的原生安裝檔，預設安裝下即會進行安裝。  
  
在其他平台上，需使用對應系統之套件管理程式進行安裝。 (如 apt install/yum install/easy_install...)  
  
根據現行Python官方仍提供兩個版本，pip工具仍根據python版本的不同，對應成`pip2`與`pip3`。  
  
一旦`pip`工具安裝完成後，Python函式庫可由類似以下指令進行安裝:  

```Bash
(Terminal) pip2 install <library/package name> # for python 2
(Terminal) pip3 install <library/package name> # for python 3
```
  
上述指令本身是直接連結至網路進行線上下載並同時安裝對應最新的函式庫/套件。  
  
關於可安裝的函式庫與清單，python官方網站已釋出一個專門的[網站](https://pypi.org/)提供確認與搜尋，甚至可自行提供自行開發的函式庫。  
  
此工具同時提供非官方與離線安裝套件/函式庫，由其他函式庫製作者之網站(非Python官方提供)或先下載後再進行離線安裝。  
  
針對非官方，不在上述網站清單之函式庫可由以下指令進行下載與安裝:  
  
```Bash
(Terminal) pip2 install <site address of .whl file> # for python 2
(Terminal) pip3 install <site address of .whl file> # for python 3
```
  
或是想進行離線安裝，可先下載對應的whl檔在執行以下指令進行安裝:  
  
```bash
(Terminal) wget <site address of .whl file> # or manually using browser to download
(Terminal) pip2 install <local .whl file> # for python 2
(Terminal) pip3 install <local .whl file> # for python 3
```
  
## {Jupyter Notebook}
  
關於Jupyter Notebook，其[官方網站](https://jupyter.org/)提供一個方案可以同時在同一個環境下執行python片段程式碼並加入markdown的註解對應python程式碼進行解說。  
  
此程式也是基於python開發並提供一個網頁介面進行存取與使用。  
  
任何檔案的副檔名由此程式建立出的使用".ipynb"為其父檔名，並建議初學者可安裝並下載與使用其他人所建好之'筆記'來學習Python語言。  
  
其安裝方式如下:  
  
```shell
(Terminal) pip2 install jupyter # for python 2
(Terminal) pip3 install jupyter # for python 3
```
  
完成安裝後，簡單的在終端機/命令行執行`jupyter notebook`來開啟與使用。  
  
---
  
Copyright (C) 2019  AkishinoShiame  