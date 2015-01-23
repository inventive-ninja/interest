from .dispatcher import (Dispatcher, Resource,
                         Binding, get, post, put, delete, patch, head, options,
                         Match, ExistentMatch, NonExistentMatch)
from .formatter import Formatter, JSONFormatter
from .logger import Logger, SystemLogger
from .protocol import Protocol, Interaction
from .responder import Responder, Middleware
from .service import Service
version = '0.1.0'  # REPLACE: version = '{{ version }}'
