
def getfile(url, fullpath):
    import urllib.request


    if url is None:
        print('no link')
    else:
        print('Beginning file download with urllib2...')
        urllib.request.urlretrieve(str(url), fullpath)

        print(fullpath)
        print('gotfile')
