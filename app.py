from pytube import Playlist


class Download:
    """
    Download your favourite playlists
    URL example >> url = 'https://www.youtube.com/playlist?list=PLbZIPy20-1pN7mqjckepWF78ndb6ci_qi'
    RES example >> res = '720'

    use download method to download all videos in the playlist
     def download(self):
        p = Playlist(self.url)
        res = '{res}p'

        for video in p.videos:
            video.streams.filter(res=res).first().download()
    """
    def __init__(self, url='', res=''):
        self.url = url 
        self.res = res 

    def download(self):
        p = Playlist(self.url)
        res = '{}p'.format(self.res)
        num = 1

        try:
            for video in p.videos:
                print(f'video {num}')
                video.streams.filter(res=res).first().download()
                print('Download complete')
                num += 1
        except:
            print('==============================================================================')
            print('ERROR: INVALID URL OR RESOLUTION')
            print('url: https://www.youtube.com/playlist?list=PLbZIPy20-1pN7mqjckepWF78ndb6ci_qi')
            print('resolution: 720')
            print('==============================================================================')


if __name__ == '__main__':
    url = input('url: ')
    res = input('resolution: ')

    d = Download(url, res)
    d.download()