# Java -> HTML parser for the UoPeople Forum

Got the motivation to make a small script that will parse the Java to HTML, using inline styles to get it a little bit of personality, given that the UoPeople forum lets you do that!

| Tag          | Description                                                           |
|--------------|-----------------------------------------------------------------------|
| /*comment:   | Marks the start of a text block                                       |
| endcomment*/ | Marks the end of a text block                                         |
| endcomment*/ | Marks the end of a text block                                         |
| //code:      | Marks the start of the Java code                                      |
| //endcode    | Marks the end of the Java code (</pre></code>)                        |
| \r           | Marks the place where two <br> will be inserted, for spacing          |
| //error      | Marks the place of an error, it will turn the number of the line red! |

I'll be updating this in my free time!

### How the current version looks like:

(From the provided example.java)
![current version image](https://cdn.discordapp.com/attachments/498759853670531075/1070405482231124109/image.png)
    