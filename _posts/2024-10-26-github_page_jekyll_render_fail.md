---
title: "Github Page 渲染 Jeklly 页面失败"
author: "Zhao Zilong"
date: 2024-10-26
category: Linux
layout: post
---

当使用 Github Page 发表 Jeklly 网站 post 时，有时会渲染失败并报如下错误：

{% raw %}

```plaintext
Run bundle exec jekyll build --baseurl ""
Configuration file: /home/runner/work/linux-helpdesk.github.io/linux-helpdesk.github.io/_config.yml
            Source: /home/runner/work/linux-helpdesk.github.io/linux-helpdesk.github.io
       Destination: /home/runner/work/linux-helpdesk.github.io/linux-helpdesk.github.io/_site
 Incremental build: disabled. Enable with --incremental
      Generating... 
       Jekyll Feed: Generating feed for posts
  Liquid Exception: Liquid syntax error (line 48): Unknown tag 'from' in /home/runner/work/linux-helpdesk.github.io/linux-helpdesk.github.io/_posts/2024-10-26-jupyter_to_html_state_error.md
                    ------------------------------------------------
      Jekyll 4.3.4   Please append `--trace` to the `build` command 
                     for any additional information or backtrace. 
                    ------------------------------------------------
/home/runner/work/linux-helpdesk.github.io/linux-helpdesk.github.io/vendor/bundle/ruby/3.1.0/gems/liquid-4.0.4/lib/liquid/document.rb:23:in `unknown_tag': Liquid syntax error (line 48): Unknown tag 'from' (Liquid::SyntaxError)
 from /home/runner/work/linux-helpdesk.github.io/linux-helpdesk.github.io/vendor/bundle/ruby/3.1.0/gems/liquid-4.0.4/lib/liquid/document.rb:11:in `block in parse'

...

 from /opt/hostedtoolcache/Ruby/3.1.4/x64/lib/ruby/gems/3.1.0/gems/bundler-2.3.26/libexec/bundle:48:in `block in <top (required)>'
 from /opt/hostedtoolcache/Ruby/3.1.4/x64/lib/ruby/3.1.0/bundler/friendly_errors.rb:120:in `with_friendly_errors'
 from /opt/hostedtoolcache/Ruby/3.1.4/x64/lib/ruby/gems/3.1.0/gems/bundler-2.3.26/libexec/bundle:36:in `<top (required)>'
 from /opt/hostedtoolcache/Ruby/3.1.4/x64/bin/bundle:25:in `load'
 from /opt/hostedtoolcache/Ruby/3.1.4/x64/bin/bundle:25:in `<main>'
Error: Process completed with exit code 1.
```

{% endraw %}

而报错原因其实是代码块中包含 Jeklly 语法的保留字，此时需要在代码块前后加入如下装饰以暂停使用 Liquid 语法进行渲染：

&#123;% raw %&#125;

```plaintext
[Output texts]
```

&#123;% endraw %&#125;

实际文档中不用反斜杠，这里由于渲染问题加了反斜杠。
