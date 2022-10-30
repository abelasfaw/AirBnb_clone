#!/usr/bin/python3
"""intialization for models directory"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
