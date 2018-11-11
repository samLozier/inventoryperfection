
def getfile(url, destination):
    import urllib.request
    if url is None:
        print('badurl')
    else:
        print('Beginning file download with urllib2...')
        urllib.request.urlretrieve(str(url), destination)
        print('gotfile')
