import vk_api
from modules import const
from modules import db


class UserAuth:
    def __init__ ( self ):
        self.session = vk_api.VkApi( token=const.__TOKEN_USER__ )
        self.session._auth_token( )

    def getUserInformation ( self, user_id ):
        return self.session.method( 'account.getProfileInfo', { 'user_id': user_id } )
