# wiki-basgrospoing

A conversion from mediawiki to HTML files using a scrapper and some voodoo magic.

## Required HTACCESS

Go from / to Accueil
```
RewriteEngine on
RewriteCond %{HTTP_HOST} ^wiki\.basgrospoing\.fr$ [OR]
RewriteCond %{HTTP_HOST} ^www\.wiki\.basgrospoing\.fr$
RewriteRule ^index\.php\/$ "https\:\/\/wiki\.basgrospoing\.fr\/index\.php\/Accueil" [R=302,L]
```

Prettyfy urls
```
RewriteCond %{REQUEST_FILENAME} !-d
RewriteCond %{REQUEST_FILENAME}\.html -f
RewriteRule ^(.*)$ $1.html
```