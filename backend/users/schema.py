import strawberry
from gqlauth.user.queries import UserQueries
from gqlauth.user import arg_mutations as mutations

from typing import List
from .types import CustomUserType
from .models import CustomUser

@strawberry.type
class Query(UserQueries):
    @strawberry.field
    def users(self) -> List[CustomUserType]:
        return CustomUser.objects.all()
    
    @strawberry.field
    def user(self, id: int) -> CustomUserType:
        if id == id:
            user = CustomUser.objects.get(id=id)
            return user
        



@strawberry.type
class Mutation:
    verify_token = mutations.VerifyToken.field
    update_account = mutations.UpdateAccount.field
    archive_account = mutations.ArchiveAccount.field
    delete_account = mutations.DeleteAccount.field
    password_change = mutations.PasswordChange.field
    # swap_emails = mutations.SwapEmails.field

    # these are mutation that does not require authentication.
    # captcha = Captcha.field
    token_auth = mutations.ObtainJSONWebToken.field
    register = mutations.Register.field
    verify_account = mutations.VerifyAccount.field
    resend_activation_email = mutations.ResendActivationEmail.field
    send_password_reset_email = mutations.SendPasswordResetEmail.field
    password_reset = mutations.PasswordReset.field
    password_set = mutations.PasswordSet.field
    refresh_token = mutations.RefreshToken.field
    revoke_token = mutations.RevokeToken.field
    # verify_secondary_email = mutations.VerifySecondaryEmail.field





    # @strawberry.field
    # def delete_users(self, id: int) -> bool:
    #     user = CustomUser.objects.get(id=id)
    #     user.delete
    #     return True


# schema = strawberry.Schema(query=Query, mutation=Mutation)