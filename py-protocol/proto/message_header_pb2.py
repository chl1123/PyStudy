# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: message_header.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor.FileDescriptor(
    name='message_header.proto',
    package='rbk4.protocol',
    syntax='proto3',
    serialized_options=None,
    serialized_pb=_b(
        '\n\x14message_header.proto\x12\rrbk4.protocol\"F\n\x0eMessage_Header\x12\x0f\n\x07\x63hannel\x18\x01 \x01(\t\x12\x10\n\x08sequence\x18\x02 \x01(\x04\x12\x11\n\ttimestamp\x18\x03 \x01(\x04\x62\x06proto3')
)

_MESSAGE_HEADER = _descriptor.Descriptor(
    name='Message_Header',
    full_name='rbk4.protocol.Message_Header',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='channel', full_name='rbk4.protocol.Message_Header.channel', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='sequence', full_name='rbk4.protocol.Message_Header.sequence', index=1,
            number=2, type=4, cpp_type=4, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='timestamp', full_name='rbk4.protocol.Message_Header.timestamp', index=2,
            number=3, type=4, cpp_type=4, label=1,
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
    serialized_end=109,
)

DESCRIPTOR.message_types_by_name['Message_Header'] = _MESSAGE_HEADER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Message_Header = _reflection.GeneratedProtocolMessageType('Message_Header', (_message.Message,), dict(
    DESCRIPTOR=_MESSAGE_HEADER,
    __module__='message_header_pb2'
    # @@protoc_insertion_point(class_scope:rbk4.protocol.Message_Header)
))
_sym_db.RegisterMessage(Message_Header)

# @@protoc_insertion_point(module_scope)
