def dropboxGetfile(fullpath, url):
    import config as cfg
    from dropbox import dropbox
    print(url, fullpath)
    dbx = dropbox.Dropbox(cfg.dropboxkey['dropboxkey'])

    dbx.files_download_to_file(fullpath, url)


