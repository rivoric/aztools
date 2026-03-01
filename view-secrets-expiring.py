import global_config
import argparse
from datetime import datetime, timedelta, timezone

from azure.keyvault.secrets import SecretClient


def read_keyvault_secrets(vault_url: str, expiring_before: datetime):
    print(f"Reading secrets from {vault_url} expiring before {expiring_before}")
    client = SecretClient(vault_url=vault_url,credential=global_config.get_credential())
    secret_properties = client.list_properties_of_secrets()

    for secret_property in secret_properties:
        if secret_property.expires_on and secret_property.expires_on < expiring_before:
            print(secret_property.name, secret_property.expires_on)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="List Key Vault secrets expiring before a given date.")
    parser.add_argument("-d", "--days", type=int, default=30,
        help="Show secrets expired or expiring within this number of days."
    )
    parser.add_argument("-u", "--keyvault-url", type=str,
        default=global_config.get_env_var_default("AZURE_KEYVAULT_URL", None),
        help="The URL of the Key Vault to read secrets from. Will be read from the AZURE_KEYVAULT_URL environment variable if available. Can also use keyvault-name instead."
    )
    parser.add_argument("-v", "--keyvault-name", type=str,
        default=global_config.get_env_var_default("AZURE_KEYVAULT_NAME", None),
        help="The name of the Key Vault to read secrets from. Will be read from the AZURE_KEYVAULT_NAME environment variable if available. Ignored if keyvault-url instead."
    )
    args = parser.parse_args()

    expiring_before = datetime.now(timezone.utc) + timedelta(days=args.days)
    if args.keyvault_url:
        vault_url = args.keyvault_url
    elif args.keyvault_name:
        vault_url = f"https://{args.keyvault_name}.vault.azure.net"
    else:
        parser.print_help()
        exit(1)

    read_keyvault_secrets(vault_url, expiring_before)
