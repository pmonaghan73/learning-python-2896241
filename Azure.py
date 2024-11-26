from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient


def get_blob_service_client_sas():
    # TODO: Replace <storage-account-name> with your actual storage account name
    account_url = "https://data0001.blob.core.windows.net/logging?sp=r&st=2024-11-19T18:56:31Z&se=2025-05-01T01:56:31Z&spr=https&sv=2022-11-02&sr=c&sig=An90PFtCRzzAq4G160LUN156LB8GrXzQQLn6hTEO1XI%3D"
    # The SAS token string can be assigned to credential here or appended to the account URL
    #credential = sas_token

    # Create the BlobServiceClient object
    blob_service_client = BlobServiceClient(account_url)

    return blob_service_client

def list_blobs_flat(self, blob_service_client: BlobServiceClient, container_name):
    container_client = blob_service_client.get_container_client(container=container_name)

    blob_list = container_client.list_blobs()

    for blob in blob_list:
        print(f"Name: {blob.name}")
        
blob = get_blob_service_client_sas()