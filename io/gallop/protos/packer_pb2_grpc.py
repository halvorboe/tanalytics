# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import common_pb2 as common__pb2
import packer_pb2 as packer__pb2


class PackerStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Insert = channel.unary_unary(
            "/protos.Packer/Insert",
            request_serializer=packer__pb2.InsertRequest.SerializeToString,
            response_deserializer=common__pb2.Error.FromString,
        )
        self.Segment = channel.unary_unary(
            "/protos.Packer/Segment",
            request_serializer=packer__pb2.SegmentRequest.SerializeToString,
            response_deserializer=packer__pb2.SegmentResponse.FromString,
        )
        self.Segments = channel.unary_unary(
            "/protos.Packer/Segments",
            request_serializer=packer__pb2.SegmentsRequest.SerializeToString,
            response_deserializer=packer__pb2.SegmentsResponse.FromString,
        )


class PackerServicer(object):
    """Missing associated documentation comment in .proto file"""

    def Insert(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Segment(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Segments(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_PackerServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "Insert": grpc.unary_unary_rpc_method_handler(
            servicer.Insert,
            request_deserializer=packer__pb2.InsertRequest.FromString,
            response_serializer=common__pb2.Error.SerializeToString,
        ),
        "Segment": grpc.unary_unary_rpc_method_handler(
            servicer.Segment,
            request_deserializer=packer__pb2.SegmentRequest.FromString,
            response_serializer=packer__pb2.SegmentResponse.SerializeToString,
        ),
        "Segments": grpc.unary_unary_rpc_method_handler(
            servicer.Segments,
            request_deserializer=packer__pb2.SegmentsRequest.FromString,
            response_serializer=packer__pb2.SegmentsResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "protos.Packer", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class Packer(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def Insert(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/protos.Packer/Insert",
            packer__pb2.InsertRequest.SerializeToString,
            common__pb2.Error.FromString,
            options,
            channel_credentials,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def Segment(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/protos.Packer/Segment",
            packer__pb2.SegmentRequest.SerializeToString,
            packer__pb2.SegmentResponse.FromString,
            options,
            channel_credentials,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def Segments(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/protos.Packer/Segments",
            packer__pb2.SegmentsRequest.SerializeToString,
            packer__pb2.SegmentsResponse.FromString,
            options,
            channel_credentials,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
