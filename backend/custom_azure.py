from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'bloomlearnstore'
    account_key = 'mwcUaR0O80LVgkXncawkH1qn7mzOfjury323DDIl1aRGPW0BeBU89Y8JAVs+E1UjTifcZ+V1r0ZpsK4PES5qQg=='
    azure_container = 'media'
    expiration_secs = None
    # overwrite_files = True

class AzureStaticStorage(AzureStorage):
    account_name = 'bloomlearnstore'
    account_key = 'mwcUaR0O80LVgkXncawkH1qn7mzOfjury323DDIl1aRGPW0BeBU89Y8JAVs+E1UjTifcZ+V1r0ZpsK4PES5qQg=='
    azure_container = 'static'
    expiration_secs = None