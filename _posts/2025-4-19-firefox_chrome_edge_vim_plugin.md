---
title: Firefox Chrome Edge Vim 插件常用快捷键
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

Navigating the current page:

```text
?       show the help dialog for a list of all available keys
h       scroll left
j       scroll down
k       scroll up
l       scroll right
gg      scroll to top of the page
G       scroll to bottom of the page
d       scroll down half a page
u       scroll up half a page
f       open a link in the current tab
F       open a link in a new tab
r       reload
gs      view source
i       enter insert mode -- all commands will be ignored until you hit Esc to exit
yy      copy the current url to the clipboard
yf      copy a link url to the clipboard
```

Using find:

```text
/       enter find mode
          -- type your search query and hit enter to search, or Esc to cancel
n       cycle forward to the next find match
N       cycle backward to the previous find match
```

Navigating your history:

```text
H       go back in history
L       go forward in history
```

Manipulating tabs:

```text
J, gT   go one tab left
K, gt   go one tab right
g0      go to the first tab. Use ng0 to go to n-th tab
g$      go to the last tab
^       visit the previously-visited tab
t       create tab
x       close current tab
X       restore closed tab (i.e. unwind the 'x' command)
T       search through your open tabs
W       move current tab to new window
```

Additional advanced browsing commands:

```text
gi      focus the first (or n-th) text input box on the page. Use <tab> to cycle through options.
ge      edit the current URL
gE      edit the current URL and open in a new tab
v       enter visual mode; use p/P to paste-and-go, use y to yank
V       enter visual line mode
R       Hard reload the page (skip the cache)
```

```

```
