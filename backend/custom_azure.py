from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'bloomlearnstore' # Must be replaced by your <storage_account_name>
    account_key = 'mwcUaR0O80LVgkXncawkH1qn7mzOfjury323DDIl1aRGPW0BeBU89Y8JAVs+E1UjTifcZ+V1r0ZpsK4PES5qQg==' # Must be replaced by your <storage_account_key>
    azure_container = 'media'
    expiration_secs = None
    overwrite_files = True
'''
class AzureStaticStorage(AzureStorage):
    account_name = 'bloomlearnstore' # Must be replaced by your storage_account_name
    account_key = 'mwcUaR0O80LVgkXncawkH1qn7mzOfjury323DDIl1aRGPW0BeBU89Y8JAVs+E1UjTifcZ+V1r0ZpsK4PES5qQg==' # Must be replaced by your <storage_account_key>
    azure_container = 'static'
    expiration_secs = None
'''