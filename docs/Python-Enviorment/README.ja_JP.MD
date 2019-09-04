# ゼロからパイソン
  
*日本語で原稿として書いてます。  
  
## パイソンのリリース / Python Release / Python釋出資訊
  
現時点のパイソンは二つ公式リリースである: Python 2 と Python 3.    
パイソン2とパイソン3は部分なプログラミングの違い、それはパイソンコーアの部分が変わったから。例文は:  
  
```python
print "Hello World" # パイソン2しか使う
print("Hello World") # パイソン3しか使う
```
  
現在のパイソン2は最新なリリースが2.7、そうして公式はEoM(End of Maintenance)が表明し、2020は最終期限。  
そのアナウンスは[この文章](https://pythonclock.org/)に書いてある。  
  
パイソン3は今も絶賛運転中。  
初めてから使いの方々はパイソン3がおすすめです。パイソン2は辞めた方がよい。  
  
全部なリリースはパイソンの公式[サイト](https://www.python.org/)に公開された。  
そうしてlinuxシステムで開発や使いの方々はシステム内蔵のパッケージマネージャーに`install python<version>`や`install python<version>-dev`でインストールする。  
  
## Enviorment / 使用環境 / ソフトウェアバージョン
  
様々なIDEを紹介します.  

#### [Pycharm]
>   
> There are two version of PyCharm can use, usually it`s suggest to use Community Edition.  
>   
> The communication version already has a lot of useful function and it`s free.  
>   
> Official site and download can found from [here](https://www.jetbrains.com/pycharm/).  
>   
> This has a dependent library management GUI tool, which very friendly for the first time developer.  
>   
> Also this is a cross-OS IDE, the usage learning can also find in [here](https://www.jetbrains.com/pycharm/learning-center/)  
>   
> The best suggest IDE.  
  
#### [WinPython]
>   
> This Python IDE was the first one I`ve used and suggest by an Instructor.  
>  
> The Official website can be found from [Here](https://winpython.github.io/), and only support in windows OS.  
>  
> It`s also a good starter-used IDE, due to its build-in library. Which can found the list from [Here](https://github.com/winpython/winpython/blob/master/changelogs/WinPython-64bit-3.7.4.0.md).  
>  
> I was also use this for learning the stuffs in [Deep Learning Site](http://deeplearning.net/tutorial/index.html) also try some coding.  
>  
> This package uses **Spyder** editor as their default IDE.
>  
> This package also has it`s own Package Management Tool.  
  
#### [Anaconda]
>  
> This IDE was suggest by one of my best friend.  
>  
> As the WinPython can not supported for mac system, this was a suggestion for mac user previously.  
>  
> It also like WinPython, has its own library management tool, but still can usin official install method.  
>  
> This Package also uses **Spyter** as it`s default editor.  
>  
> The official website and download can be found from [Here](https://www.anaconda.com/).  
>  
> Before **Pycharm** became famous, this is another choice on Python development.
>  
> From officials description said its `The Enterprise Data Science Platform` also free for download and used.  
  
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