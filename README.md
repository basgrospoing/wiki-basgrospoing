# wiki-basgrospoing
An old mediawiki I painfully have to convert to something else.

## Solution 1

Curl every page for the main tag, then convert HTML to MD:

`pandoc -f html -t markdown-raw_html-native_divs-native_spans-fenced_divs-bracketed_spans test.html -o test2.md && pandoc test.md > final.html`

Remove :
```
<p><br>
</p>

</ul>
      <ul>
```

## Solution 2

Use the database as JSON files.