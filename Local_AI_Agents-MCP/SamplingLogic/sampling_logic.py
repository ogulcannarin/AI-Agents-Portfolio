from mcp.server.fastmcp import FastMCP
import mcp.types as types

mcp = FastMCP("DataAnalyst")

@mcp.tool()
async def analyze_data_with_ai(data_description: str, ctx: mcp.Context) -> str:
    """Sunucu, veriyi okur ve modelden profesyonel analiz talep eder."""
    
    # Modelden içerik isteme (Sampling)
    # Burada modelin 'yaratıcılığını' kontrol ediyoruz.
    response = await ctx.session.create_message(
        messages=[
            types.SamplingMessage(
                role="user",
                content=types.TextContent(
                    type="text",
                    text=f"Aşağıdaki veri setini analiz et ve bana en önemli 3 çıkarımı yaz: \n{data_description}"
                )
            )
        ],
        model_preferences=types.ModelPreferences(
            speed_priority=True, # Hızlı yanıt istiyoruz
            intelligence_priority=True # Ama zeki de olsun
        ),
        max_tokens=150
    )

    return f"ANALİZ SONUCU:\n{response.content.text}"

if __name__ == "__main__":
    mcp.run()