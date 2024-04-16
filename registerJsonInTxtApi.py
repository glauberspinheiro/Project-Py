import aiohttp
import asyncio
import json

# função assicrona para montar a url e headers e informando a quandidade paginas que irá percorrer
async def fetch_page(session, url, page_num, headers):
    async with session.get(f"{url}&pageNumber={page_num}", headers=headers) as response:
        
        print(page_num)
        return await response.json()
    
    
    
# função assicrona para percorrer todas as paginas até chegar na quantidade de paginas informada
async def fetch_all_pages(url, total_pages, headers):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for page_num in range(0, total_pages + 1):
            tasks.append(fetch_page(session, url, page_num, headers))
            

        responses = await asyncio.gather(*tasks)        
        return responses
        

async def main():
    url = 'https://api.bemoby.com/v1/callcenter/attendances;period=finalization;beginDate=2023-01-01;endDate=2023-01-30;tabulations=;fields=?pageSize=100'
    headers = {
        'Authorization': 'Basic YXBpLmF0aWJhaWFAYmVtb2J5LmNvbToyMlYyMU5AMng3dVg='
        # Adicionar mais cabeçalhos se fazer necessário
    }
    total_pages = 30  # <- Informar aqui a quantidade de paginas que irá percorrer
    responses = await fetch_all_pages(url, total_pages, headers)

    ##criar valiação de status##
    
    # Escrevendo cada response encontrado em uma linha no arquivo entitulado responses.txt
    with open('aquivostest.txt', 'w') as file:
        for response in responses:
            file.write(json.dumps(response))
            file.write('\n')


# Executando o main
if __name__ == "__main__":
    asyncio.run(main())