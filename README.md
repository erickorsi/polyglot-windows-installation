# polyglot-windows-installation

Manual steps, explanation and automatic installation of the package "Polyglot" in any version of Python 3 on Windows.

---
Polyglot is a natural language pipeline that supports various languages, built for Linux and very useful for natural language processing of texts in non-english languages. The <a href="http://polyglot.readthedocs.org" title="http://polyglot.readthedocs.org">Polyglot Documentation</a> explains how to install it on Linux, by installing its dependencies and running `pip install polyglot` in the terminal. However, as of September 2022, the package is still not stable for Windows OS, requiring either the use of a Windows Subsystem for Linux (WSL) or through various installations of dependencies and setup through the Command Prompt.

---
* ## **Using WSL**

With the use of a virtual Linux environment in Windows, it is possible to run the regular installation of polyglot in a WSL virtual machine platform. Installation of the WSL can be done following the <a href="https://docs.microsoft.com/en-us/windows/wsl/install" title="https://docs.microsoft.com/en-us/windows/wsl/install">Microsoft Documentation</a>.

This is a good solution, but may result in slower performance or conflict with running virtual environments in some cases.

* ## **On base Windows**

If trying to install and use polyglot in Windows without the use of a virtual Linux machine, the process is more complex. This repo was created to offer an easy way to do this, by running the **`setup.bat`** file. The steps taken in this installation are as follows:

1. **Download** of depencencies *PyICU*, *pycld2*, *futures* and *Morfessor*. *Morfessor* and *futures* wheels may be unnecessary in some cases. These two are already present in the **wheels/** folder, and are built for all versions of Python 3. *PyICU* and *pycld2* are version-specific according to which minor version of Python 3 you are using and can be accordingly downloaded from this <a href="https://www.lfd.uci.edu/~gohlke/pythonlibs/" title="https://www.lfd.uci.edu/~gohlke/pythonlibs/">Archive of Python Extension Packages</a>.
   
    Within the **`get_dependencies.py`** file, which is called by **`setup.bat`** after installing the *requests* package, these wheels are automatically downloaded according to the detected Python version of the interpreter. By manually running this python script, you can input a specific version of each of these wheels for download, instead of downloading the default versions.

2. **Installaion** of dependencies using

   ```
   python -m pip install [path/to/downloaded/wheel.whl]
   ```
   In some cases, it is possible to simply run `pip install [wheel.whl]` or `pip3 install [wheel.whl]`, though these may not work in all cases.
   
   This is also automated within the **`get_dependencies.py`** script for each of the four wheels required.

3. **Setup** of the polyglot package itself directly from the <a href="https://github.com/aboSamoor/polyglot.git" title="https://github.com/aboSamoor/polyglot.git">GitHub Repo</a>.
   
   ```
   git clone https://github.com/aboSamoor/polyglot.git
   cd polyglot
   python setup.py install
   ```
   This is done automatically within the **`setup.bat`** file. After the setup is finished, the created folder is also removed, because it is no longer necessary.

With this the package is installed on Windows and can be tested by running in Python:

```python
from polyglot.text import Text
```

Errors may be the result of failed installation of dependencies or unsupported versions of packages.

---
* ## **Installing specific language models**

When using polyglot for parts-of-speech tagging in languages other than english, it is necessary to install the respective **embeddings2** and **pos2** models. For example, to use portuguese (pt) parts-of-speech tagging, you need to run in the Command Prompt or Terminal:

```
polyglot download embedding2.pt pos2.pt
```
More information on languages and parts-of-speech tagging can be found in the <a href="https://polyglot.readthedocs.io/en/latest/POS.html" title="https://polyglot.readthedocs.io/en/latest/POS.html">POS Documentation</a>, <a href="https://polyglot.readthedocs.io/en/latest/Download.html" title="https://polyglot.readthedocs.io/en/latest/Download.html">Model Download Documentation</a> and in the <a href="https://universaldependencies.org/docs/tagset-conversion/index.html" title="https://universaldependencies.org/docs/tagset-conversion/index.html">Universal POS Tables</a>.