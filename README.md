##Summary: Summarize your Text in Sublime Text

This plugin summarizes selected text in Sublime Text and replaces the original text with the Summarized Text. It uses the [summary_tool.py](https://gist.github.com/shlomibabluki/5473521) code by shlomibabluki.
This should be used in Markdown Documents or TXT files with large text. Do not use with Code.


###Installtion

Search for Summary on Package Control and Press enter to install.

Alternatively, you can `git clone` this repo or download the zip file and extract the contents of this repository onto your Sublime Packages folder (Preferences - Browse Packages..)

###Usage

Select the text that you want to summarize and then right click, and click "Summarize Text"

You can use the Command Pallete too if you want.

You can set a keybinding to the summarize command as well. Just click on `Prefernces - Key Bindings - User` and enter the following data into the JSON file.

```
{ "keys": ["ctrl+shift+s"], "command": "summary"}
```

You can change the keybinding to your choice by modifying the `keys` key-value pair.

###About

Created By Pradipta (geekpradd). Copyright 2015. MIT Licensed.