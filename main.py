from src import application_gui as ag

# run in console if new translations are includes:
# msgfmt -o i18n/de/LC_MESSAGES/messages.mo i18n/de/LC_MESSAGES/messages.po
# msgfmt -o i18n/en/LC_MESSAGES/messages.mo i18n/en/LC_MESSAGES/messages.po

if __name__ == '__main__':
    app = ag.App()
    app.mainloop()
    print(app.streamerName)
    print(app.language)