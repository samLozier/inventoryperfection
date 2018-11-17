def dropboxGetfile(fullpath, url):
    from dropbox import dropbox
    print(url, fullpath)
    dbx = dropbox.Dropbox('nztpZkxMeAwAAAAAAAAGG8aaOjyOuO_3dnPuhPGIAIOFLem6axA7-_3NSs9zIYXc')

    dbx.files_download_to_file(fullpath, url)


