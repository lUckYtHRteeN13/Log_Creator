<!-- Italic "_", "*" -->
<!-- Strong "_ _", "* *"-->
<!-- Strikethrough "~~" -->
<!-- Horizontal Rule "--", "_ _" -->
<!-- Block Quote ">" -->
<!-- Links "[Text](Link "Title")" -->
<!-- UL "*"-->
<!-- OL "1."-->
<!-- Inline Code Block "'" -->
<!-- Images "![Text](Location)"-->

<!-- GitHub -->
<!-- Code Block " ```syntax \nContent \n``` "-->
<!-- Table Jhon Doe-->
<!-- Task List "* []"-->
<!-- Heading "#" -->
# __Log_Creator__
Under construction! Not ready for use yet! Currently experimenting and planning!

Developed by Nethan Quinn Jael (c) 2022

# __How To Use__
``` python
from log_creator import Log

#Create an Instance
x = Log(file_name="optional.txt", file_directory="../<optional>")

#Create a Log File and Directory to the Current Working Directory
x.create_log()

#Write a Log
x.write_log("Hello World")
```