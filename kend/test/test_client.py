import kend.client
import logging

logging.basicConfig(level=logging.DEBUG)

def test_client():
    service = kend.client.Service()
    client = service.client()

    client.annotations(document='http://utopia.cs.manchester.ac.uk/documents/850')

if __name__ == '__main__':
    test_client()