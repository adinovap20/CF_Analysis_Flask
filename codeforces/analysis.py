import codeforces
import requests
import json

class CodeforcesData:
    handle = None
    email = None
    vkId = None
    openId = None
    firstName = None
    lastName = None
    country = None
    city = None
    organization = None
    contribution = None
    rank = None
    rating = None
    maxRank = None
    maxRating = None
    lastOnlineTimeSeconds = None
    registrationTimeSeconds = None
    friendOfCount = None
    avatar = None
    titlePhoto = None
    

class CodeforcesAnalyzer:
    def __init__(self, username):
        self.__username = username
        self.__data = self.create_data_block()
        self.update_block_with_user_info()

    def get_datablock(self):
        return self.__data

    def get_username(self):
        return self.__username

    def create_data_block(self):
        block = CodeforcesData()
        block.handle = self.__username
        return block
    
    def update_block_with_user_info(self):
        response = requests.get(f"https://codeforces.com/api/user.info?handles={self.__username}")
        response_dict = json.loads(response.content)
        info_dict = response_dict['result'][0]
        self.__data.handle = info_dict['handle']
        
        try:
            self.__data.email = info_dict['email']
        except Exception as e:
            self.__data.email = "$$NONE$$"
        
        try:
            self.__data.vkId = info_dict['vkId']
        except Exception as e:
            self.__data.vkId = "$$NONE$$"
        
        try:
            self.__data.openId = info_dict['openId']
        except Exception as e:
            self.__data.openId = "$$NONE$$"
        
        try:
            self.__data.firstName = info_dict['firstName']
        except Exception as e:
            self.__data.firstName = "$$NONE$$"
        
        try:
            self.__data.lastName = info_dict['lastName']
        except Exception as e:
            self.__data.lastName = "$$NONE$$"
        
        try:
            self.__data.country = info_dict['country']
        except Exception as e:
            self.__data.country = "$$NONE$$"
        
        try:
            self.__data.city = info_dict['city']
        except Exception as e:
            self.__data.city = "$$NONE$$"
        
        try:
            self.__data.organization = info_dict['organization']
        except Exception as e:
            self.__data.organization = "$$NONE$$"
        
        self.__data.contribution = info_dict['contribution']
        self.__data.rank = info_dict['rank']
        self.__data.rating = info_dict['rating']
        self.__data.maxRank = info_dict['maxRank']
        self.__data.maxRating = info_dict['maxRating']
        self.__data.lastOnlineTimeSeconds = info_dict['lastOnlineTimeSeconds']
        self.__data.registrationTimeSeconds = info_dict['registrationTimeSeconds']
        self.__data.friendOfCount = info_dict['friendOfCount']
        self.__data.avatar = info_dict['avatar']
        self.__data.titlePhoto = info_dict['titlePhoto']

        return True