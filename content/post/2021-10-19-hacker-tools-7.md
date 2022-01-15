---
title: "Hacker Tools: CLI debugging and profiling"
date: 2021-10-19 21:00:00
author: Hao Wei
url: /2021/10/hacker-tools-7
summary: Come learn how to debug and profile various things on Linux, all from the command line.
---

This workshop has ended; here are links to the materials and recording:

- [Slides](https://nushackers.github.io/hackertools-slides/2110ht7/)
- [Recording](https://www.youtube.com/watch?v=maISKQl7rIo)

**Date/Time**: Wednesday, 27 Oct 2021, 19:00&ndash;21:00

Come learn how to debug and profile various things on Linux, all from the command line. We'll look at how to figure out what's going wrong with programs you write and the operating system itself.

Please ensure you have access to **real Linux**. If you are on a Linux distribution, you are set; if you use Windows or Mac, consider installing Ubuntu in a virtual machine like VirtualBox. If you are on Windows, you can also use Windows Subsystem for Linux 2. (**WSL 1 is not suitable.**)

- WSL: https://docs.microsoft.com/en-us/windows/wsl/install-win10

Please make sure you have the following programs installed in your Linux system:

- Git, Perl 5, Python 3, gdb, strace, ltrace, Valgrind, GCC, perf (Linux kernel), htop, dstat, iotop, df, du, free, lsof, ss, stress, s-tui
- On Ubuntu, the following packages: gdb strace ltrace valgrind linux-tools htop dstat iotop lsof iproute2 stress s-tui procps build-essential python3 perl git
- On Arch Linux, the following packages: gdb strace ltrace valgrind perf htop dstat iotop lsof iproute2 stress s-tui procps-ng base-devel python perl git

This workshop is largely based on the Missing Semester of Your CS Education lecture series conducted in MIT. This week's topic is based on https://missing.csail.mit.edu/2020/debugging-profiling/.

See you there!
