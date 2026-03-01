"""Shared Azure utilities used across aztools scripts."""

import argparse

from azure.identity import DefaultAzureCredential
from .osconfig import get_env_var_default

def get_credential() -> DefaultAzureCredential:
    """Return a DefaultAzureCredential instance."""
    return DefaultAzureCredential()
