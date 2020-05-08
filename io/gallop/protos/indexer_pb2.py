# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: indexer.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import gallop.protos.common_pb2 as common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='indexer.proto',
  package='protos',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\rindexer.proto\x12\x06protos\x1a\x0c\x63ommon.proto\"P\n\x0b\x42indRequest\x12%\n\nsegment_id\x18\x01 \x01(\x0b\x32\x11.protos.SegmentId\x12\x0c\n\x04host\x18\x02 \x01(\t\x12\x0c\n\x04port\x18\x03 \x01(\x05\"6\n\rUnBindRequest\x12%\n\nsegment_id\x18\x01 \x01(\x0b\x32\x11.protos.SegmentId2i\n\x07Indexer\x12,\n\x04\x42ind\x12\x13.protos.BindRequest\x1a\r.protos.Error\"\x00\x12\x30\n\x06UnBind\x12\x15.protos.UnBindRequest\x1a\r.protos.Error\"\x00\x62\x06proto3'
  ,
  dependencies=[common__pb2.DESCRIPTOR,])




_BINDREQUEST = _descriptor.Descriptor(
  name='BindRequest',
  full_name='protos.BindRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='segment_id', full_name='protos.BindRequest.segment_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='host', full_name='protos.BindRequest.host', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port', full_name='protos.BindRequest.port', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=39,
  serialized_end=119,
)


_UNBINDREQUEST = _descriptor.Descriptor(
  name='UnBindRequest',
  full_name='protos.UnBindRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='segment_id', full_name='protos.UnBindRequest.segment_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=121,
  serialized_end=175,
)

_BINDREQUEST.fields_by_name['segment_id'].message_type = common__pb2._SEGMENTID
_UNBINDREQUEST.fields_by_name['segment_id'].message_type = common__pb2._SEGMENTID
DESCRIPTOR.message_types_by_name['BindRequest'] = _BINDREQUEST
DESCRIPTOR.message_types_by_name['UnBindRequest'] = _UNBINDREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BindRequest = _reflection.GeneratedProtocolMessageType('BindRequest', (_message.Message,), {
  'DESCRIPTOR' : _BINDREQUEST,
  '__module__' : 'indexer_pb2'
  # @@protoc_insertion_point(class_scope:protos.BindRequest)
  })
_sym_db.RegisterMessage(BindRequest)

UnBindRequest = _reflection.GeneratedProtocolMessageType('UnBindRequest', (_message.Message,), {
  'DESCRIPTOR' : _UNBINDREQUEST,
  '__module__' : 'indexer_pb2'
  # @@protoc_insertion_point(class_scope:protos.UnBindRequest)
  })
_sym_db.RegisterMessage(UnBindRequest)



_INDEXER = _descriptor.ServiceDescriptor(
  name='Indexer',
  full_name='protos.Indexer',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=177,
  serialized_end=282,
  methods=[
  _descriptor.MethodDescriptor(
    name='Bind',
    full_name='protos.Indexer.Bind',
    index=0,
    containing_service=None,
    input_type=_BINDREQUEST,
    output_type=common__pb2._ERROR,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UnBind',
    full_name='protos.Indexer.UnBind',
    index=1,
    containing_service=None,
    input_type=_UNBINDREQUEST,
    output_type=common__pb2._ERROR,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_INDEXER)

DESCRIPTOR.services_by_name['Indexer'] = _INDEXER

# @@protoc_insertion_point(module_scope)
