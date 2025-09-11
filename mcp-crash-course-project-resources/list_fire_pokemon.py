import asyncio
import json
from fastmcp import FastMCP
from main import app

async def get_fire_pokemon():
    # Access the poke://types/fire resource from the main.py MCP app
    result = await app.resource_handlers['poke://types/{type_name}']('fire')
    return result

if __name__ == "__main__":
    try:
        result = asyncio.run(get_fire_pokemon())
        print(json.dumps(result, indent=2))
    except Exception as e:
        print(f"Error: {e}")
        # Fallback to direct API call if MCP access fails
        print("Falling back to direct API call...")
        import httpx
        
        async def get_fire_pokemon_direct():
            async with httpx.AsyncClient(timeout=10.0) as client:
                response = await client.get("https://pokeapi.co/api/v2/type/fire")
                data = response.json()
                
                # Return first 10 Pokémon of this type
                pokemon_list = data["pokemon"][:10]
                
                return {
                    "type": "Fire",
                    "type_id": data["id"],
                    "pokemon_count": len(data["pokemon"]),
                    "showing": len(pokemon_list),
                    "pokemon": [
                        {
                            "name": p["pokemon"]["name"].capitalize(),
                            "uri": f"poke://pokemon/{p['pokemon']['name']}"
                        }
                        for p in pokemon_list
                    ]
                }
        
        result = asyncio.run(get_fire_pokemon_direct())
        print(json.dumps(result, indent=2))
