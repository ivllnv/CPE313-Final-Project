import nest_asyncio
import asyncio
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport

def fetch_reviews(latitude, longitude):
    API_KEY = 'api_key'
    async def fetch_data():

        transport = AIOHTTPTransport(
            url="https://api.yelp.com/v3/graphql",
            headers={
                "Authorization": f"Bearer {API_KEY}"
            }
        )

        client = Client(transport=transport, fetch_schema_from_transport=True)

        query = gql(
            """
            query getBusinesses($latitude: Float!, $longitude: Float!) {
              search(latitude: $latitude, longitude: $longitude, radius: 100) {
                business {
                  name
                  reviews {
                    user {
                      name
                    }
                    rating
                    text
                  }
                }
              }
            }
            """
        )

        result = await client.execute_async(query, variable_values={"latitude": latitude, "longitude": longitude})
        return result

    response_data = asyncio.run(fetch_data())
    return response_data

fetch_reviews(37.7749, 122.4194)