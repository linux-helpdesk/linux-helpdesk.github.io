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
	from /home/runner/work/linux-helpdesk.github.io/linux-helpdesk.github.io/vendor/bundle/ruby/3.1.0/gems/liquid-4.0.4/lib/liquid/block_body.rb:32:in `parse'
	from /home/runner/work/linux-helpdesk.github.io/linux-helpdesk.github.io/vendor/bundle/ruby/3.1.0/gems/liquid-4.0.4/lib/liquid/document.rb:10:in `parse'
	from /home/runner/work/linux-helpdesk.github.io/linux-helpdesk.github.io/vendor/bundle/ruby/3.1.0/gems/liquid-4.0.4/lib/liquid/document.rb:5:in `parse'
	from /home/runner/work/linux-helpdesk.github.io/linux-helpdesk.github.io/vendor/bundle/ruby/3.1.0/gems/liquid-4.0.4/lib/liquid/template.rb:130:in `parse'
	from /home/runner/work/linux-helpdesk.github.io/linux-helpdesk.github.io/vendor/bundle/ruby/3.1.0/gems/liquid-4.0.4/lib/liquid/template.rb:114:in `parse'
	from /home/runner/work/linux-helpdesk.github.io/linux-helpdesk.github.io/vendor/bundle/ruby/3.1.0/gems/jekyll-4.3.4/lib/jekyll/liquid_renderer/file.rb:13:in `block in parse'
	from /home/runner/work/linux-helpdesk.github.io/linux-helpdesk.github.io/vendor/bundle/ruby/3.1.0/gems/jekyll-4.3.4/lib/jekyll/liquid_renderer/file.rb:70:in `measure_time'
	from /home/runner/work/linux-helpdesk.github.io/linux-helpdesk.github.io/vendor/bundle/ruby/3.1.0/gems/jekyll-4.3.4/lib/jekyll/liquid_renderer/file.rb:12:in `parse'
	from /home/runner/work/linux-helpdesk.github.io/linux-helpdesk.github.io/vendor/bundle/ruby/3.1.0/gems/jekyll-4.3.4/lib/jekyll/renderer.rb:124:in `render_liquid'
	from /home/runner/work/linux-helpdesk.github.io/linux-helpdesk.github.io/vendor/bundle/ruby/3.1.0/gems/jekyll-4.3.4/lib/jekyll/renderer.rb:80:in `render_document'
	from /home/runner/work/linux-helpdesk.github.io/linux-helpdesk.github.io/vendor/bundle/ruby/3.1.0/gems/jekyll-4.3.4/lib/jekyll/renderer.rb:63:in `run'
	from /home/runner/work/linux-helpdesk.github.io/linux-helpdesk.github.io/vendor/bundle/ruby/3.1.0/gems/jekyll-4.3.4/lib/jekyll/site.rb:572:in `render_regenerated'
	from /home/runner/work/linux-helpdesk.github.io/linux-helpdesk.github.io/vendor/bundle/ruby/3.1.0/gems/jekyll-4.3.4/lib/jekyll/site.rb:557:in `block (2 levels) in render_docs'
	from /home/runner/work/linux-helpdesk.github.io/linux-helpdesk.github.io/vendor/bundle/ruby/3.1.0/gems/jekyll-4.3.4/lib/jekyll/site.rb:556:in `each'
	from /home/runner/work/linux-helpdesk.github.io/linux-helpdesk.github.io/vendor/bundle/ruby/3.1.0/gems/jekyll-4.3.4/lib/jekyll/site.rb:556:in `block in render_docs'
	from /home/runner/work/linux-helpdesk.github.io/linux-helpdesk.github.io/vendor/bundle/ruby/3.1.0/gems/jekyll-4.3.4/lib/jekyll/site.rb:555:in `each_value'
	from /home/runner/work/linux-helpdesk.github.io/linux-helpdesk.github.io/vendor/bundle/ruby/3.1.0/gems/jekyll-4.3.4/lib/jekyll/site.rb:555:in `render_docs'
	from /home/runner/work/linux-helpdesk.github.io/linux-helpdesk.github.io/vendor/bundle/ruby/3.1.0/gems/jekyll-4.3.4/lib/jekyll/site.rb:210:in `render'
	from /home/runner/work/linux-helpdesk.github.io/linux-helpdesk.github.io/vendor/bundle/ruby/3.1.0/gems/jekyll-4.3.4/lib/jekyll/site.rb:80:in `process'
	from /home/runner/work/linux-helpdesk.github.io/linux-helpdesk.github.io/vendor/bundle/ruby/3.1.0/gems/jekyll-4.3.4/lib/jekyll/command.rb:28:in `process_site'
	from /home/runner/work/linux-helpdesk.github.io/linux-helpdesk.github.io/vendor/bundle/ruby/3.1.0/gems/jekyll-4.3.4/lib/jekyll/commands/build.rb:65:in `build'
	from /home/runner/work/linux-helpdesk.github.io/linux-helpdesk.github.io/vendor/bundle/ruby/3.1.0/gems/jekyll-4.3.4/lib/jekyll/commands/build.rb:36:in `process'
	from /home/runner/work/linux-helpdesk.github.io/linux-helpdesk.github.io/vendor/bundle/ruby/3.1.0/gems/jekyll-4.3.4/lib/jekyll/command.rb:91:in `block in process_with_graceful_fail'
	from /home/runner/work/linux-helpdesk.github.io/linux-helpdesk.github.io/vendor/bundle/ruby/3.1.0/gems/jekyll-4.3.4/lib/jekyll/command.rb:91:in `each'
	from /home/runner/work/linux-helpdesk.github.io/linux-helpdesk.github.io/vendor/bundle/ruby/3.1.0/gems/jekyll-4.3.4/lib/jekyll/command.rb:91:in `process_with_graceful_fail'
	from /home/runner/work/linux-helpdesk.github.io/linux-helpdesk.github.io/vendor/bundle/ruby/3.1.0/gems/jekyll-4.3.4/lib/jekyll/commands/build.rb:18:in `block (2 levels) in init_with_program'
	from /home/runner/work/linux-helpdesk.github.io/linux-helpdesk.github.io/vendor/bundle/ruby/3.1.0/gems/mercenary-0.4.0/lib/mercenary/command.rb:221:in `block in execute'
	from /home/runner/work/linux-helpdesk.github.io/linux-helpdesk.github.io/vendor/bundle/ruby/3.1.0/gems/mercenary-0.4.0/lib/mercenary/command.rb:221:in `each'
	from /home/runner/work/linux-helpdesk.github.io/linux-helpdesk.github.io/vendor/bundle/ruby/3.1.0/gems/mercenary-0.4.0/lib/mercenary/command.rb:221:in `execute'
	from /home/runner/work/linux-helpdesk.github.io/linux-helpdesk.github.io/vendor/bundle/ruby/3.1.0/gems/mercenary-0.4.0/lib/mercenary/program.rb:44:in `go'
	from /home/runner/work/linux-helpdesk.github.io/linux-helpdesk.github.io/vendor/bundle/ruby/3.1.0/gems/mercenary-0.4.0/lib/mercenary.rb:21:in `program'
	from /home/runner/work/linux-helpdesk.github.io/linux-helpdesk.github.io/vendor/bundle/ruby/3.1.0/gems/jekyll-4.3.4/exe/jekyll:15:in `<top (required)>'
	from /home/runner/work/linux-helpdesk.github.io/linux-helpdesk.github.io/vendor/bundle/ruby/3.1.0/bin/jekyll:25:in `load'
	from /home/runner/work/linux-helpdesk.github.io/linux-helpdesk.github.io/vendor/bundle/ruby/3.1.0/bin/jekyll:25:in `<top (required)>'
	from /opt/hostedtoolcache/Ruby/3.1.4/x64/lib/ruby/3.1.0/bundler/cli/exec.rb:58:in `load'
	from /opt/hostedtoolcache/Ruby/3.1.4/x64/lib/ruby/3.1.0/bundler/cli/exec.rb:58:in `kernel_load'
	from /opt/hostedtoolcache/Ruby/3.1.4/x64/lib/ruby/3.1.0/bundler/cli/exec.rb:23:in `run'
	from /opt/hostedtoolcache/Ruby/3.1.4/x64/lib/ruby/3.1.0/bundler/cli.rb:486:in `exec'
	from /opt/hostedtoolcache/Ruby/3.1.4/x64/lib/ruby/3.1.0/bundler/vendor/thor/lib/thor/command.rb:27:in `run'
	from /opt/hostedtoolcache/Ruby/3.1.4/x64/lib/ruby/3.1.0/bundler/vendor/thor/lib/thor/invocation.rb:127:in `invoke_command'
	from /opt/hostedtoolcache/Ruby/3.1.4/x64/lib/ruby/3.1.0/bundler/vendor/thor/lib/thor.rb:392:in `dispatch'
	from /opt/hostedtoolcache/Ruby/3.1.4/x64/lib/ruby/3.1.0/bundler/cli.rb:31:in `dispatch'
	from /opt/hostedtoolcache/Ruby/3.1.4/x64/lib/ruby/3.1.0/bundler/vendor/thor/lib/thor/base.rb:485:in `start'
	from /opt/hostedtoolcache/Ruby/3.1.4/x64/lib/ruby/3.1.0/bundler/cli.rb:25:in `start'
	from /opt/hostedtoolcache/Ruby/3.1.4/x64/lib/ruby/gems/3.1.0/gems/bundler-2.3.26/libexec/bundle:48:in `block in <top (required)>'
	from /opt/hostedtoolcache/Ruby/3.1.4/x64/lib/ruby/3.1.0/bundler/friendly_errors.rb:120:in `with_friendly_errors'
	from /opt/hostedtoolcache/Ruby/3.1.4/x64/lib/ruby/gems/3.1.0/gems/bundler-2.3.26/libexec/bundle:36:in `<top (required)>'
	from /opt/hostedtoolcache/Ruby/3.1.4/x64/bin/bundle:25:in `load'
	from /opt/hostedtoolcache/Ruby/3.1.4/x64/bin/bundle:25:in `<main>'
Error: Process completed with exit code 1.
```
{% endraw %}

而报错原因其实是代码块中包含 Jeklly 语法的保留字，此时需要在代码块前后加入如下装饰以暂停使用 Liquid 语法进行渲染：

{% raw %}
````plaintext
\{% raw %\}
```plaintext
[Output texts]
```
\{% endraw %\}
````
{% endraw %}

实际文档中不用反斜杠，这里由于渲染问题加了反斜杠。
