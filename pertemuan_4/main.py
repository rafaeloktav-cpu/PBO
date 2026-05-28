class Influencer:
    username = ''
    followers = 0
    postingan = 0

    def cek_profil(self):
        print(f'Halo {self.username}, Followers Anda: {self.followers}, Total Post: {self.postingan}')

    def __init__(self, username='', followers=0, postingan=0):
        if followers < 0:
            raise ValueError('Jumlah followers tidak mungkin negatif')
        self.username = username
        self.postingan = postingan
        self.followers = followers
        print('Akun telah terverifikasi!')

    def __str__(self):
        return f'Profil: @{self.username} - Post: {self.postingan}, Followers: {self.followers}'

    def __eq__(self, other):
        return self.username == other.username and self.followers == other.followers and self.postingan == other.postingan

    def __ge__(self, other):
        return self.followers >= other.followers
    
    def __le__(self, other):
        return self.followers <= other.followers

# Mengisi data Influencer
user1 = Influencer('TechReviewer', 500000, 120)
user1.cek_profil()

user2 = Influencer('DailyVlog', 150000, 450)
user2.cek_profil()

user3 = Influencer('FoodieGuide', 300000, 85)
user3.cek_profil()

# Output perbandingan berdasarkan jumlah Followers
print(user1)            # Menampilkan ringkasan profil user1
print(user3 <= user1)   # True (Followers FoodieGuide 300rb <= TechReviewer 500rb)
print(user1 == user2)   # False
print(user1 >= user2)   # True (Followers TechReviewer lebih banyak dari DailyVlog)