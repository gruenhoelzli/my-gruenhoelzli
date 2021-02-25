-   Contains gruenhoelzli-specific translations / vocabulary

-   In principle these additional translation files are automatically discovered by Django and hence there would be
    no need to add "LOCALE_PATHS = ['path/to/locale/files]" in settingsy.py. BUT: these additional translation files
    need to have a *higher priority* than the translation files in juntagrico dependency. And this can be achieved
    with the LOCALE_PATHS setting.
    However, since there are no translations for German in the juntagrico dependency (only translation keys, which are
    used also as translation values), the translation files in this directy will always have the highest prio and will
    be applied. But this is not the case for other languages. E.g.: for English there are translation files in
    juntagrico and therefore the translation files in this directory need to have a higher priority.
    Long story short: the LOCALE_PATHS entry in settingsy.py is required.

-   If you change any of the *.po files, you need to recompile the files to create the *.mo files. For this run

        python manage.py compilemessages

    in the project root.

See also:
    https://docs.djangoproject.com/en/3.1/ref/settings/#locale-paths
    https://docs.djangoproject.com/en/3.1/topics/i18n/translation/#how-django-discovers-translations
    https://docs.djangoproject.com/en/3.1/topics/i18n/translation/#compiling-message-files
    https://stackoverflow.com/questions/21735576/how-to-set-locale-path-relative-to-project-path-in-django
