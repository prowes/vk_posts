import vk_api
import random
from bs4 import BeautifulSoup
from getpass import getpass

class Download():
    def login(self, login, password):
        vk_session = vk_api.VkApi(login, password)  # test it more
        try:
            vk_session.auth(reauth=True)
        except vk_api.AuthError as error_msg:
            print(error_msg)
            exit()
        return vk_session

    def get_posts(self, group_id):
        tools = vk_api.VkTools(vk_session)
        wall = tools.get_all('wall.get', 100, {'owner_id': f'-{group_id}'})

        print('Posts count:', wall['count'])
        if wall['count'] > 1:
            print('Last post:', wall['items'][-1])
        # todo: save to .txt file, remove special symbols (\n, etc)

    def main(self):
        login = input('Please enter e-mail:\n')
        password = getpass()

        vk_session = self.login(login, password)
        group_id = input('Please enter the ID of the group (ie 123456)')
        self.get_posts(group_id)

if __name__ == '__main__':
    Download().main()