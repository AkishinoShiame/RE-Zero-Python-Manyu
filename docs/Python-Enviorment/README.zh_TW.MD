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
> This is the IDE base on python created application.  
>  
> It was also been created for the Data Science used.
>  
> The support OSs of the `Spyter` across all platform. Can be installed by official `pip` tool.  
>  
> The official site can be found in [this site](https://www.spyder-ide.org/).  
>  
> For the self experience, it is not suggest to install alone-side with pip. It will sometimes catch the bug of system ASCII/Unicode issue, makes the application can not opened/working.  
  
## Library Installation / ライブラリのインストール / 安裝函式庫
  
The official suggest to install the Python Libries by using their official tool: `pip`.  
  
For the Windows system, it packed with the Python official installation.  
  
For the other System, installed with their own Package Manager. (Ex. apt install/yum install/easy_install...)  
  
Due to the Python version, the pip tool also according to the python has `pip2` and `pip3`.  
  
After install the `pip` tool, the libraries can be install with below command:  

```Bash
(Terminal) pip2 install <library/package name> # for python 2
(Terminal) pip3 install <library/package name> # for python 3
```
  
The above command will goes online download & install for the latest library/package.  
  
For the list of of the packages/libraries which can be donload, the python official released a [site](https://pypi.org/) can check on.  
  
This tool also can install packages/libraries from other non-python-official sites or offline download.  
  
For the non-python-official packages can use below method to download and install:  
  
```Bash
(Terminal) pip2 install <site address of .whl file> # for python 2
(Terminal) pip3 install <site address of .whl file> # for python 3
```
  
Or for the offline installation, it can be download the whl file first and manually install as below:  
  
```bash
(Terminal) wget <site address of .whl file> # or manually using browser to download
(Terminal) pip2 install <local .whl file> # for python 2
(Terminal) pip3 install <local .whl file> # for python 3
```
  
## {Jupyter Notebook}
  
For the Jupyter Notebook, the [official page](https://jupyter.org/) tells for a solution to execute code and also with mark-down method to explane how the python code works in same enviorment.  
  
It is developed by python based and made out web page interface for access.  
  
The extension of notebook is called ".ipynb" and is suggest for the beginner to install and use for checking others 'notebook' to learn Python.  
  
The install method as below:  
  
```shell
(Terminal) pip2 install jupyter # for python 2
(Terminal) pip3 install jupyter # for python 3
```
  
After installation, simply execute `jupyter notebook` in the command-line to start using it.  
  
---
  
Copyright (C) 2019  AkishinoShiame  