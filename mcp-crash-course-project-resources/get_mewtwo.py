import httpx
import asyncio
import json

async def get_pokemon(pokemon_name):
    """This function simulates an MCP resource call for pokemon/{name}"""
    # In a real MCP implementation, we would use the MCP client to make this call
    # Here we're directly implementing the logic of the MCP resource handler
    async with httpx.AsyncClient(timeout=10.0) as client:
        try:
            # This is the same logic as in the main.py MCP resource handler
            response = await client.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
            
            if response.status_code == 404:
                return {"error": f"Pokémon with name '{pokemon_name}' not found"}
            elif response.status_code != 200:
                return {"error": f"PokeAPI error: HTTP {response.status_code}"}
                    
            data = response.json()
            
            # This matches the structure in the main.py MCP resource handler
            return {
                "id": data["id"],
                "name": data["name"].capitalize(),
                "height": data["height"] / 10,  # Convert to meters
                "weight": data["weight"] / 10,  # Convert to kg
                "types": [t["type"]["name"] for t in data["types"]],
                "abilities": [a["ability"]["name"] for a in data["abilities"]],
                "base_stats": {
                    stat["stat"]["name"]: stat["base_stat"] 
                    for stat in data["stats"]
                },
                "sprite": data["sprites"]["front_default"],
                "api_url": f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
            }
            
        except httpx.RequestError as e:
            return {"error": f"Failed to fetch Pokémon data: {str(e)}"}
        except (KeyError, ValueError) as e:
            return {"error": f"Error processing Pokémon data: {str(e)}"}

async def main():
    # MCP URI would be: poke://pokemon/mewtwo
    result = await get_pokemon("mewtwo")
    print(json.dumps(result, indent=2))
    print("\nThis data was retrieved using the MCP resource handler logic from poke://pokemon/mewtwo")

if __name__ == "__main__":
    asyncio.run(main())
