---
author: Viet Le
categories:
- Uncategorized
comments: true
date: 2010-06-16T00:00:00Z
title: Intro to Nokia Qt C++ Framework
url: /2010/06/16/intro-to-nokia-qt-c-framework/
---

![Qt Logo](/res/2010/06/qt_image_thumb.png "Qt Logo")

Developing a portable application has never been an easy task, be it a browser-based service or a fanciful desktop application. With emergence of many frameworks for developing cross-platform applications, choosing the right one has become a challenge. One can name a bunch of frameworks for desktop development, such as GTK+, Gtkmm, FLTK, VCF C++, etc. Adobe fans would pronounce Adobe Air as the best choice. Well, so what do I have in my hat? Voilà! I'd like to present Nokia Qt C++ framework - one of the leading frameworks for desktop &amp; mobile development.

### GUI in a while

There are many reasons why I love Qt Designer and would like to share some with you:

* If you love Delphi &amp; M$.NET GUI designers, you will find a new romance with Qt Designer.
* Dozens of widgets are available to serve you and what you need to do is just to drag &amp; drop.
* Adding menu, submenus, toolboxes &amp; docked widgets can be done with a few clicks.
* Qt Designer loves diversity and accepts your custom widgets.
* Feel free to load and change GUI dynamically with UiLoader.

You may want read more on [Qt Designer][].

![World Time Clock Plugin Example](/res/2010/06/worldtimeclockplugin-example.png "World Time Clock Plugin Example")

### Write once &amp; run everywhere

You can target different architectures such as x86, x86-64, ARM, ... and run on Windows, Linux, Mac OS X, S60, Maemo, etc with no or little modification to your code. The broader audience you reach, the more popularity you gain.

### Network boldly

Qt has a wealth of network libraries. The clients to the standard services such as HTTP(S) &amp; FTP are already there for you. XML parsing, XQuery &amp; XPath libraries will enable you to interface with web services. Writing own TCP/UDP-based protocols with Qt is easy. Feel free to read more on [Qt Network][].

![Google Suggest Example](/res/2010/06/googlesuggest-example.png "Google Suggest Example")

### Browser &amp; scripting integration

Along with high quality modules for GUI, networking and XML, Nokia Qt C++ framework has other 2 killer modules: QtWebkit &amp; QtScript. QtWebkit provides browser integration based on the Webkit engine used by Apple Safari &amp; Google Chrome. Adding a browser to your application to render web pages or custom help/manual files in HTML has never been easier. QtScript exposes Qt objects to scripting with JS-like language. With QtScript you are empowered to do cross-platform scripting on your applications to increase productivity and encourage users to write their own extensions. Please refer to the official [Qt Script][] and [Qt Webkit][] documents and examples to explore more.

![Webkit Examples](/res/2010/06/webkit-examples.png "Webkit Examples")

### Installation

1. Please find suitable installation package for your OS &amp; architecture from [http://qt.nokia.com/downloads/](http://qt.nokia.com/downloads/ "Qt Nokia C++ Downloads"). Please pay close attention to whether your OS is 32-bit or 64-bit and make sure you download the version of Qt SDK that suits your OS.

2. Proceed to the installation with the default settings. It is recommended that you stick with the default installation settings. There are very few things to tweak.

3. Set up paths and links for the Qt library. If you are using Mac, you may skip this step. This step is only advisable for Windows and Linux developers.

    *     Windows: You need to add paths to the Qt bin &amp; MinGW bin folders. If you installed Qt 4.6.3 then the path of Qt is `C:\Qt\2010.3`. You need to add the following paths: `C:\Qt\2010.3\qt\bin` and `C:\Qt\2010.3\mingw\bin`.

    *     Linux/Unix: You have 2 options: Either to create soft links or add to the environment variables `PATH` &amp; `LD_LIBRARY_PATH`. To add soft links, you need to run the following commands:

        `sudo ln -s /opt/qtsdk-2010.3/qt/bin/* /usr/bin/`

        `sudo ln -s /opt/qtsdk-2010.3/qt/lib/lib* /usr/lib/`

        To manipulate environment variables, edit the file `~/.bash_profile` and add these 2 lines:

        `export PATH=$PATH:/opt/qtsdk-2010.3/qt/bin`

        `export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/qtsdk-2010.3/qt/lib`

    For the changes to the environment variables to take effect, you need to log out and log in again. Soft links don't need that extra step.

Now you are ready to run Qt demos &amp; examples. Enjoy!

![Qt Demonstrations](/res/2010/06/qtdemo.png "Qt Demonstrations")

### Conclusion

Nokia might not suit all your needs but it's one of the best options to keep an eye on. Among large users of Nokia Qt C++ framework, there are companies such as [Google, Adobe and Skype](http://qt.nokia.com/qt-in-use/target/desktop/ "[Google, Adobe and Skype"). Qt has found its application in a [breadth of industries](http://qt.nokia.com/qt-in-use/). Your next killer application may be written in Nokia C++ too! Stay tuned with our series of Qt tutorials!

***

\* The screenshots are provided at the official Nokia Qt C++ documentation website.

[Qt Nokia C++ Downloads]: http://qt.nokia.com/downloads/ "Qt Nokia C++ Downloads"

[Qt Designer]: http://doc.qt.nokia.com/4.6/examples-designer.html "Qt Designer Examples"

[Qt Network]: http://doc.qt.nokia.com/4.6/examples-network.html "QtNetwork Examples"

[Qt Script]: http://doc.qt.nokia.com/4.6/examples-script.html "QtScript Examples"

[Qt Webkit]: http://doc.qt.nokia.com/4.6/examples-webkit.html "QtWebkit Examples"
