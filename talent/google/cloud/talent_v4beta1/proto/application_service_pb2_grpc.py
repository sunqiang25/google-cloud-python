# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.cloud.talent_v4beta1.proto import (
    application_pb2 as google_dot_cloud_dot_talent__v4beta1_dot_proto_dot_application__pb2,
)
from google.cloud.talent_v4beta1.proto import (
    application_service_pb2 as google_dot_cloud_dot_talent__v4beta1_dot_proto_dot_application__service__pb2,
)
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class ApplicationServiceStub(object):
    """A service that handles application management, including CRUD and
  enumeration.
  """

    def __init__(self, channel):
        """Constructor.

    Args:
      channel: A grpc.Channel.
    """
        self.CreateApplication = channel.unary_unary(
            "/google.cloud.talent.v4beta1.ApplicationService/CreateApplication",
            request_serializer=google_dot_cloud_dot_talent__v4beta1_dot_proto_dot_application__service__pb2.CreateApplicationRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_talent__v4beta1_dot_proto_dot_application__pb2.Application.FromString,
        )
        self.GetApplication = channel.unary_unary(
            "/google.cloud.talent.v4beta1.ApplicationService/GetApplication",
            request_serializer=google_dot_cloud_dot_talent__v4beta1_dot_proto_dot_application__service__pb2.GetApplicationRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_talent__v4beta1_dot_proto_dot_application__pb2.Application.FromString,
        )
        self.UpdateApplication = channel.unary_unary(
            "/google.cloud.talent.v4beta1.ApplicationService/UpdateApplication",
            request_serializer=google_dot_cloud_dot_talent__v4beta1_dot_proto_dot_application__service__pb2.UpdateApplicationRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_talent__v4beta1_dot_proto_dot_application__pb2.Application.FromString,
        )
        self.DeleteApplication = channel.unary_unary(
            "/google.cloud.talent.v4beta1.ApplicationService/DeleteApplication",
            request_serializer=google_dot_cloud_dot_talent__v4beta1_dot_proto_dot_application__service__pb2.DeleteApplicationRequest.SerializeToString,
            response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
        self.ListApplications = channel.unary_unary(
            "/google.cloud.talent.v4beta1.ApplicationService/ListApplications",
            request_serializer=google_dot_cloud_dot_talent__v4beta1_dot_proto_dot_application__service__pb2.ListApplicationsRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_talent__v4beta1_dot_proto_dot_application__service__pb2.ListApplicationsResponse.FromString,
        )


class ApplicationServiceServicer(object):
    """A service that handles application management, including CRUD and
  enumeration.
  """

    def CreateApplication(self, request, context):
        """Creates a new application entity.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetApplication(self, request, context):
        """Retrieves specified application.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def UpdateApplication(self, request, context):
        """Updates specified application.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DeleteApplication(self, request, context):
        """Deletes specified application.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ListApplications(self, request, context):
        """Lists all applications associated with the profile.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_ApplicationServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "CreateApplication": grpc.unary_unary_rpc_method_handler(
            servicer.CreateApplication,
            request_deserializer=google_dot_cloud_dot_talent__v4beta1_dot_proto_dot_application__service__pb2.CreateApplicationRequest.FromString,
            response_serializer=google_dot_cloud_dot_talent__v4beta1_dot_proto_dot_application__pb2.Application.SerializeToString,
        ),
        "GetApplication": grpc.unary_unary_rpc_method_handler(
            servicer.GetApplication,
            request_deserializer=google_dot_cloud_dot_talent__v4beta1_dot_proto_dot_application__service__pb2.GetApplicationRequest.FromString,
            response_serializer=google_dot_cloud_dot_talent__v4beta1_dot_proto_dot_application__pb2.Application.SerializeToString,
        ),
        "UpdateApplication": grpc.unary_unary_rpc_method_handler(
            servicer.UpdateApplication,
            request_deserializer=google_dot_cloud_dot_talent__v4beta1_dot_proto_dot_application__service__pb2.UpdateApplicationRequest.FromString,
            response_serializer=google_dot_cloud_dot_talent__v4beta1_dot_proto_dot_application__pb2.Application.SerializeToString,
        ),
        "DeleteApplication": grpc.unary_unary_rpc_method_handler(
            servicer.DeleteApplication,
            request_deserializer=google_dot_cloud_dot_talent__v4beta1_dot_proto_dot_application__service__pb2.DeleteApplicationRequest.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
        "ListApplications": grpc.unary_unary_rpc_method_handler(
            servicer.ListApplications,
            request_deserializer=google_dot_cloud_dot_talent__v4beta1_dot_proto_dot_application__service__pb2.ListApplicationsRequest.FromString,
            response_serializer=google_dot_cloud_dot_talent__v4beta1_dot_proto_dot_application__service__pb2.ListApplicationsResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "google.cloud.talent.v4beta1.ApplicationService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))
