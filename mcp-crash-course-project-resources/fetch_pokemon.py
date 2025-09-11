import httpx
import asyncio
import json

async def get_pokemon(pokemon_id):
    async with httpx.AsyncClient(timeout=10.0) as client:
        response = await client.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")
        
        if response.status_code != 200:
            return {"error": f"Failed to fetch Pokémon with ID {pokemon_id}"}
                
        data = response.json()
        
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
            "api_url": f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
        }

async def main():
    result = await get_pokemon("25")
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    asyncio.run(main())
