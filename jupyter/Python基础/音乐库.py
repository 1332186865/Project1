# 为了组织我们的数字音乐库，我们依靠Python的实现（实现）。
# (a) 一首歌是一个具有艺术家、标题和持续时间的音乐项目。建立一个类来表示一首歌曲，其构造函数要求将艺术家（字符串）、标题（将是一个字符串）和持续时间（将是一个数字，例如秒）作为参数。
# (b) 一张专辑是一连串的歌曲。该专辑也有一个标题。制作一个专辑类，其构造函数以标题为参数。添加一个方法 "addSong(song)"，以歌曲为参数，将其添加到专辑的末尾。
# (c) 增加一个方法来计算专辑的总时间。
# (d) 一个音乐库是一堆专辑。为音乐库制作一个类，并添加一个方法将专辑添加到其中。
# (e) 添加一个方法，检索库中给定艺术家的所有歌曲。这个方法应该返回一个tuples(元组)的列表。元组中的第一个元素(元素)将是歌曲，第二个元素是歌曲所属的专辑。这个方法应该在哪个类上实现？

class Song:
    def __init__(self, artist, theme, time):
        """艺术家，标题，时间"""
        self.artist = artist
        self.theme = theme
        self.time = int(time)
        # self.lst1 = [self.theme, self.artist, self.time]

    def __repr__(self):
        return '歌名：%s， 艺术家：%s， %ds' % (self.theme, self.artist, self.time)

    def get_time(self):
        return self.time

    def get_artist(self):
        return self.artist

    def get_theme(self):
        return self.theme


class Album:
    def __init__(self, theme):
        self.theme = theme
        self.lst = []

    def addsong(self, song):
        if song not in self.lst:
            self.lst.append(song)
        return self.lst

    def total_time(self):
        count = 0
        for song in self.lst:
            count += song.get_time()
        return count

    def __repr__(self):
        return '唱片名：%s, 包含的歌曲为：%s' % (self.theme, self.lst)

    def get_song(self):
        return self.lst

    def get_theme(self):
        return self.theme


class Library:
    def __init__(self, theme):
        self.theme = theme
        self.lst1 = []

    def getalbum(self, album):
        if album not in self.lst1:
            self.lst1.append(album)
        return self.lst1

    def show_all_songs(self, artist):
        ls = []
        for i in self.lst1:
            for j in i.lst:
                if j.get_artist() == artist:
                    ls.append((j.get_theme(), i.get_theme()))
        return ls

    def __repr__(self):
        return '音乐库名：%s, 包含的唱片为：%s' % (self.theme, self.lst1)


s1 = Song('a1', 'b1', '12')
s2 = Song('a2', 'b2', '15')
s3 = Song('a3', 'b3', '21')
s4 = Song('a3', 'b4', '30')
a1 = Album('aa1')
a2 = Album('aa2')
a1.addsong(s1)
a1.addsong(s2)
a2.addsong(s3)
a2.addsong(s4)
print(s1, s2, s3, s4)
print(a1, a2)
print(a1.total_time(), a2.total_time())
l1 = Library('lib1')
l1.getalbum(a1)
l1.getalbum(a2)
print(l1)
print(l1.show_all_songs('a3'))
