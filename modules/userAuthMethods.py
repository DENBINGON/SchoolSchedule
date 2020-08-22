import vk
from modules import const


class UserAuth:
    def __init__ ( self ):
        self.session = vk.Session( access_token=const.__TOKEN_USER__ )
        self.vk_api = vk.API( self.session )

    def getUserInformation ( self, user_id ):
        return self.vk_api.users.get( user_id=user_id, v='5.21' )
