# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import authentication_pb2 as authentication__pb2
import miscellaneous_pb2 as miscellaneous__pb2


class AuthenticationStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.StartPhoneAuth = channel.unary_unary(
        '/dialog.Authentication/StartPhoneAuth',
        request_serializer=authentication__pb2.RequestStartPhoneAuth.SerializeToString,
        response_deserializer=authentication__pb2.ResponseStartPhoneAuth.FromString,
        )
    self.SendCodeByPhoneCall = channel.unary_unary(
        '/dialog.Authentication/SendCodeByPhoneCall',
        request_serializer=authentication__pb2.RequestSendCodeByPhoneCall.SerializeToString,
        response_deserializer=miscellaneous__pb2.ResponseVoid.FromString,
        )
    self.StartEmailAuth = channel.unary_unary(
        '/dialog.Authentication/StartEmailAuth',
        request_serializer=authentication__pb2.RequestStartEmailAuth.SerializeToString,
        response_deserializer=authentication__pb2.ResponseStartEmailAuth.FromString,
        )
    self.StartAnonymousAuth = channel.unary_unary(
        '/dialog.Authentication/StartAnonymousAuth',
        request_serializer=authentication__pb2.RequestStartAnonymousAuth.SerializeToString,
        response_deserializer=authentication__pb2.ResponseAuth.FromString,
        )
    self.StartTokenAuth = channel.unary_unary(
        '/dialog.Authentication/StartTokenAuth',
        request_serializer=authentication__pb2.RequestStartTokenAuth.SerializeToString,
        response_deserializer=authentication__pb2.ResponseAuth.FromString,
        )
    self.StartUsernameAuth = channel.unary_unary(
        '/dialog.Authentication/StartUsernameAuth',
        request_serializer=authentication__pb2.RequestStartUsernameAuth.SerializeToString,
        response_deserializer=authentication__pb2.ResponseStartUsernameAuth.FromString,
        )
    self.ValidateCode = channel.unary_unary(
        '/dialog.Authentication/ValidateCode',
        request_serializer=authentication__pb2.RequestValidateCode.SerializeToString,
        response_deserializer=authentication__pb2.ResponseAuth.FromString,
        )
    self.ResendCode = channel.unary_unary(
        '/dialog.Authentication/ResendCode',
        request_serializer=authentication__pb2.RequestResendCode.SerializeToString,
        response_deserializer=miscellaneous__pb2.ResponseVoid.FromString,
        )
    self.ValidatePassword = channel.unary_unary(
        '/dialog.Authentication/ValidatePassword',
        request_serializer=authentication__pb2.RequestValidatePassword.SerializeToString,
        response_deserializer=authentication__pb2.ResponseAuth.FromString,
        )
    self.GetOAuth2Params = channel.unary_unary(
        '/dialog.Authentication/GetOAuth2Params',
        request_serializer=authentication__pb2.RequestGetOAuth2Params.SerializeToString,
        response_deserializer=authentication__pb2.ResponseGetOAuth2Params.FromString,
        )
    self.CompleteOAuth2 = channel.unary_unary(
        '/dialog.Authentication/CompleteOAuth2',
        request_serializer=authentication__pb2.RequestCompleteOAuth2.SerializeToString,
        response_deserializer=authentication__pb2.ResponseAuth.FromString,
        )
    self.SignUp = channel.unary_unary(
        '/dialog.Authentication/SignUp',
        request_serializer=authentication__pb2.RequestSignUp.SerializeToString,
        response_deserializer=authentication__pb2.ResponseAuth.FromString,
        )
    self.GetAuthSessions = channel.unary_unary(
        '/dialog.Authentication/GetAuthSessions',
        request_serializer=authentication__pb2.RequestGetAuthSessions.SerializeToString,
        response_deserializer=authentication__pb2.ResponseGetAuthSessions.FromString,
        )
    self.TerminateSession = channel.unary_unary(
        '/dialog.Authentication/TerminateSession',
        request_serializer=authentication__pb2.RequestTerminateSession.SerializeToString,
        response_deserializer=miscellaneous__pb2.ResponseVoid.FromString,
        )
    self.TerminateAllSessions = channel.unary_unary(
        '/dialog.Authentication/TerminateAllSessions',
        request_serializer=authentication__pb2.RequestTerminateAllSessions.SerializeToString,
        response_deserializer=miscellaneous__pb2.ResponseVoid.FromString,
        )
    self.SignOut = channel.unary_unary(
        '/dialog.Authentication/SignOut',
        request_serializer=authentication__pb2.RequestSignOut.SerializeToString,
        response_deserializer=miscellaneous__pb2.ResponseVoid.FromString,
        )
    self.SignInObsolete = channel.unary_unary(
        '/dialog.Authentication/SignInObsolete',
        request_serializer=authentication__pb2.RequestSignInObsolete.SerializeToString,
        response_deserializer=authentication__pb2.ResponseAuth.FromString,
        )
    self.SignUpObsolete = channel.unary_unary(
        '/dialog.Authentication/SignUpObsolete',
        request_serializer=authentication__pb2.RequestSignUpObsolete.SerializeToString,
        response_deserializer=authentication__pb2.ResponseAuth.FromString,
        )
    self.SendAuthCodeObsolete = channel.unary_unary(
        '/dialog.Authentication/SendAuthCodeObsolete',
        request_serializer=authentication__pb2.RequestSendAuthCodeObsolete.SerializeToString,
        response_deserializer=authentication__pb2.ResponseSendAuthCodeObsolete.FromString,
        )
    self.SendAuthCallObsolete = channel.unary_unary(
        '/dialog.Authentication/SendAuthCallObsolete',
        request_serializer=authentication__pb2.RequestSendAuthCallObsolete.SerializeToString,
        response_deserializer=miscellaneous__pb2.ResponseVoid.FromString,
        )


class AuthenticationServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def StartPhoneAuth(self, request, context):
    """/ Start authorization by phone
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SendCodeByPhoneCall(self, request, context):
    """/ Resend code by transaction hash
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StartEmailAuth(self, request, context):
    """/ Start email authorization process
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StartAnonymousAuth(self, request, context):
    """/ Deprecated
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StartTokenAuth(self, request, context):
    """/ Start token auth authorization (actual for bots)
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StartUsernameAuth(self, request, context):
    """/ Start login/password authorization process
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ValidateCode(self, request, context):
    """* Validate code received by phone or email
    Returns error if user does not exist
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ResendCode(self, request, context):
    """/ Resend code if you don't receive it with first attempt
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ValidatePassword(self, request, context):
    """/ Validate your passwword
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetOAuth2Params(self, request, context):
    """/ Deprecated
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CompleteOAuth2(self, request, context):
    """/ Deprecated
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SignUp(self, request, context):
    """/ Sign up existed user
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetAuthSessions(self, request, context):
    """/ Returns all authorized user's sessions
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def TerminateSession(self, request, context):
    """/ Deprecated. Does not produce any effect.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def TerminateAllSessions(self, request, context):
    """/ Log out user
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SignOut(self, request, context):
    """/ Log out current session
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SignInObsolete(self, request, context):
    """/ Deprecated
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SignUpObsolete(self, request, context):
    """/ Deprecated
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SendAuthCodeObsolete(self, request, context):
    """/ Deprecated
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SendAuthCallObsolete(self, request, context):
    """/ Deprecated
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_AuthenticationServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'StartPhoneAuth': grpc.unary_unary_rpc_method_handler(
          servicer.StartPhoneAuth,
          request_deserializer=authentication__pb2.RequestStartPhoneAuth.FromString,
          response_serializer=authentication__pb2.ResponseStartPhoneAuth.SerializeToString,
      ),
      'SendCodeByPhoneCall': grpc.unary_unary_rpc_method_handler(
          servicer.SendCodeByPhoneCall,
          request_deserializer=authentication__pb2.RequestSendCodeByPhoneCall.FromString,
          response_serializer=miscellaneous__pb2.ResponseVoid.SerializeToString,
      ),
      'StartEmailAuth': grpc.unary_unary_rpc_method_handler(
          servicer.StartEmailAuth,
          request_deserializer=authentication__pb2.RequestStartEmailAuth.FromString,
          response_serializer=authentication__pb2.ResponseStartEmailAuth.SerializeToString,
      ),
      'StartAnonymousAuth': grpc.unary_unary_rpc_method_handler(
          servicer.StartAnonymousAuth,
          request_deserializer=authentication__pb2.RequestStartAnonymousAuth.FromString,
          response_serializer=authentication__pb2.ResponseAuth.SerializeToString,
      ),
      'StartTokenAuth': grpc.unary_unary_rpc_method_handler(
          servicer.StartTokenAuth,
          request_deserializer=authentication__pb2.RequestStartTokenAuth.FromString,
          response_serializer=authentication__pb2.ResponseAuth.SerializeToString,
      ),
      'StartUsernameAuth': grpc.unary_unary_rpc_method_handler(
          servicer.StartUsernameAuth,
          request_deserializer=authentication__pb2.RequestStartUsernameAuth.FromString,
          response_serializer=authentication__pb2.ResponseStartUsernameAuth.SerializeToString,
      ),
      'ValidateCode': grpc.unary_unary_rpc_method_handler(
          servicer.ValidateCode,
          request_deserializer=authentication__pb2.RequestValidateCode.FromString,
          response_serializer=authentication__pb2.ResponseAuth.SerializeToString,
      ),
      'ResendCode': grpc.unary_unary_rpc_method_handler(
          servicer.ResendCode,
          request_deserializer=authentication__pb2.RequestResendCode.FromString,
          response_serializer=miscellaneous__pb2.ResponseVoid.SerializeToString,
      ),
      'ValidatePassword': grpc.unary_unary_rpc_method_handler(
          servicer.ValidatePassword,
          request_deserializer=authentication__pb2.RequestValidatePassword.FromString,
          response_serializer=authentication__pb2.ResponseAuth.SerializeToString,
      ),
      'GetOAuth2Params': grpc.unary_unary_rpc_method_handler(
          servicer.GetOAuth2Params,
          request_deserializer=authentication__pb2.RequestGetOAuth2Params.FromString,
          response_serializer=authentication__pb2.ResponseGetOAuth2Params.SerializeToString,
      ),
      'CompleteOAuth2': grpc.unary_unary_rpc_method_handler(
          servicer.CompleteOAuth2,
          request_deserializer=authentication__pb2.RequestCompleteOAuth2.FromString,
          response_serializer=authentication__pb2.ResponseAuth.SerializeToString,
      ),
      'SignUp': grpc.unary_unary_rpc_method_handler(
          servicer.SignUp,
          request_deserializer=authentication__pb2.RequestSignUp.FromString,
          response_serializer=authentication__pb2.ResponseAuth.SerializeToString,
      ),
      'GetAuthSessions': grpc.unary_unary_rpc_method_handler(
          servicer.GetAuthSessions,
          request_deserializer=authentication__pb2.RequestGetAuthSessions.FromString,
          response_serializer=authentication__pb2.ResponseGetAuthSessions.SerializeToString,
      ),
      'TerminateSession': grpc.unary_unary_rpc_method_handler(
          servicer.TerminateSession,
          request_deserializer=authentication__pb2.RequestTerminateSession.FromString,
          response_serializer=miscellaneous__pb2.ResponseVoid.SerializeToString,
      ),
      'TerminateAllSessions': grpc.unary_unary_rpc_method_handler(
          servicer.TerminateAllSessions,
          request_deserializer=authentication__pb2.RequestTerminateAllSessions.FromString,
          response_serializer=miscellaneous__pb2.ResponseVoid.SerializeToString,
      ),
      'SignOut': grpc.unary_unary_rpc_method_handler(
          servicer.SignOut,
          request_deserializer=authentication__pb2.RequestSignOut.FromString,
          response_serializer=miscellaneous__pb2.ResponseVoid.SerializeToString,
      ),
      'SignInObsolete': grpc.unary_unary_rpc_method_handler(
          servicer.SignInObsolete,
          request_deserializer=authentication__pb2.RequestSignInObsolete.FromString,
          response_serializer=authentication__pb2.ResponseAuth.SerializeToString,
      ),
      'SignUpObsolete': grpc.unary_unary_rpc_method_handler(
          servicer.SignUpObsolete,
          request_deserializer=authentication__pb2.RequestSignUpObsolete.FromString,
          response_serializer=authentication__pb2.ResponseAuth.SerializeToString,
      ),
      'SendAuthCodeObsolete': grpc.unary_unary_rpc_method_handler(
          servicer.SendAuthCodeObsolete,
          request_deserializer=authentication__pb2.RequestSendAuthCodeObsolete.FromString,
          response_serializer=authentication__pb2.ResponseSendAuthCodeObsolete.SerializeToString,
      ),
      'SendAuthCallObsolete': grpc.unary_unary_rpc_method_handler(
          servicer.SendAuthCallObsolete,
          request_deserializer=authentication__pb2.RequestSendAuthCallObsolete.FromString,
          response_serializer=miscellaneous__pb2.ResponseVoid.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'dialog.Authentication', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))