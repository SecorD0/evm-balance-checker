<h1><p align="center">evm-balance-checker</p></h1>

<p align="center"><img src="images/icons/app.ico" width="400"></p>



<h1><p align="center">Content</p></h1>

- [Description](#Description)
- [Useful links](#Useful-links)
- [File structure](#File-structure)
- [How to run](#How-to-run)
    - [Windows](#Windows)
    - [Docker (image)](#Docker-image)
    - [Docker (building)](#Docker-building)
    - [Source code](#Source-code)
- [Sample settings](#Sample-settings)
- [Updating](#Updating)
  - [Windows](#Windows-1)
  - [GitHub image](#GitHub-image)
  - [Self-built image](#Self-built-image)
  - [Source code](#Source-code-1)
- [Useful commands](#Useful-commands)
- [Report a bug or suggest an idea](#Report-a-bug-or-suggest-an-idea)
- [Express your gratitude](#Express-your-gratitude)



<h1><p align="center">Description</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀The program allows you to check balances in several EVM networks at once, 
for which it has flexible settings for each of them:
- Multiple RPCs to prevent the 429 error known as "too many requests".
- A list of token contract addresses whose balance needs to be parsed.
- A list of NFT contract addresses whose quantity on balance needs to be parsed.

⠀The program supports using proxies to access RPC from different IPs. Saving the state it also provided, so if the 
program suddenly terminates, the balances will be checked from the same place when the program is restarted. 
Importing addresses and uploading results is done via Excel spreadsheet (each network has its own sheet). 
In addition to parsing the balance in the token itself, the program counts the balance of each token in dollar 
equivalent and the total dollar balance.



<h1><p align="center">Useful links</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀[evm-balance-checker](https://github.com/SecorD0/evm-balance-checker)



<h1><p align="center">File structure</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀The program use the following files and directories:
- `files` — a user files directory:
  - `addresses.db` — a temporary database to save the state;
  - `addresses.xlsx` — a spreadsheet for importing and viewing results.
  - `errors.log` — a log file with errors that occurred during the work;
  - `proxies.txt` — a text file with HTTP/SOCKS5 IPv4 proxies;
  - `settings.json` — a JSON file for program setup.
- `evm-balance-checker.exe` / `app.py` — an executable file that runs the program.



<h1><p align="center">How to run</p></h1>
<p align="right"><a href="#Content">To the content</a></p>


<h2><p align="center">Windows</p></h2>

1. Download an EXE file from the [releases page](https://github.com/SecorD0/evm-balance-checker/releases).
2. Create a folder and put the EXE file in it.
3. Run the program the first time to create necessary files.
4. Insert addresses to be checked into the `addresses.xlsx` spreadsheet.
5. Optionally insert HTTP/SOCKS5 IPv4 proxies in one of the following formats into the `proxies.txt` file.
```
login:password@proxy:port
http://login:password@proxy:port
socks5://login:password@proxy:port
```
6. Configure the `settings.json`:
   - `general` — general settings:
     - `threads` — number of addresses to be checked simultaneously. It isn't desirable to specify a value greater than `20`.
     - `parse_token_price` — whether to add the dollar balance of each token and the total dollar balance to the results spreadsheet (`true` or `false`).
   - `networks` — list with fine-tune settings for each network:
     - `name` — network name, if not specified it will use the network ID (optional).
     - `rpcs` — list of RPCs from which a random one will be selected for each request.
     - `tokens` — list with token contract addresses, specify `""` to parse coin balance, if you don't specify anything, the coin balance will be parsed (optional).
     - `nfts` — list with information about NFTs whose quantity on balance needs to be parsed (optional):
       - `contract_address` — NFT contract addresses.
       - `token_id` — specific token ID (optional).
7. Run the program again, wait for it to finish and close it.
A total of 5 parsing attempts will be made to successfully complete all failed requests.
If the number of requests is large and the number of RPCs and proxies is small, an error may occur:
`Failed to parse the balances of all tokens and NFTs! Try adding RPC and/or proxies.`
8. Open the `addresses.xlsx` spreadsheet to view the results.
9. Delete the `addresses.xlsx` and `addresses.db` (if it exists) files.

<h2><p align="center">Docker (image)</p></h2>

1. Install Docker, in Ubuntu you can use the command:
```sh
. <(wget -qO- https://raw.githubusercontent.com/SecorD0/utils/main/installers/docker.sh)
```
2. Run the program the first time to create necessary files:
```sh
docker run -it --rm -v $HOME/evm-balance-checker/files:/app/files --name evm-balance-checker ghcr.io/secord0/evm-balance-checker:main
```
3. Insert addresses to be checked into the `addresses.xlsx` spreadsheet.
4. Optionally insert HTTP/SOCKS5 IPv4 proxies in one of the following formats into the `proxies.txt` file.
```
login:password@proxy:port
http://login:password@proxy:port
socks5://login:password@proxy:port
```
5. Configure the `settings.json`:
   - `general` — general settings:
     - `threads` — number of addresses to be checked simultaneously. It isn't desirable to specify a value greater than `20`.
     - `parse_token_price` — whether to add the dollar balance of each token and the total dollar balance to the results spreadsheet (`true` or `false`).
   - `networks` — list with fine-tune settings for each network:
     - `name` — network name, if not specified it will use the network ID (optional).
     - `rpcs` — list of RPCs from which a random one will be selected for each request.
     - `tokens` — list with token contract addresses, specify `""` to parse coin balance, if you don't specify anything, the coin balance will be parsed (optional).
     - `nfts` — list with information about NFTs whose quantity on balance needs to be parsed (optional):
       - `contract_address` — NFT contract addresses.
       - `token_id` — specific token ID (optional).
6. Run the program again, wait for it to finish and close it.
A total of 5 parsing attempts will be made to successfully complete all failed requests.
If the number of requests is large and the number of RPCs and proxies is small, an error may occur:
`Failed to parse the balances of all tokens and NFTs! Try adding RPC and/or proxies.`
```sh
docker run -it --rm -v $HOME/evm-balance-checker/files:/app/files --name evm-balance-checker ghcr.io/secord0/evm-balance-checker:main
```
7. Open the `addresses.xlsx` spreadsheet to view the results.
8. Delete the `addresses.xlsx` and `addresses.db` (if it exists) files.


<h2><p align="center">Docker (building)</p></h2>

1. Install Docker, in Ubuntu you can use the command:
```sh
. <(wget -qO- https://raw.githubusercontent.com/SecorD0/utils/main/installers/docker.sh)
```
2. Clone the repository:
```sh
cd; git clone https://github.com/SecorD0/evm-balance-checker
```
3. Go to the repository:
```sh
cd evm-balance-checker
```
4. Build an image:
```sh
docker build -t evm-balance-checker .
```
5. Run the program the first time to create necessary files:
```sh
docker run -it --rm -v $HOME/evm-balance-checker/:/app --name evm-balance-checker evm-balance-checker
```
6. Insert addresses to be checked into the `addresses.xlsx` spreadsheet.
7. Optionally insert HTTP/SOCKS5 IPv4 proxies in one of the following formats into the `proxies.txt` file.
```
login:password@proxy:port
http://login:password@proxy:port
socks5://login:password@proxy:port
```
8. Configure the `settings.json`:
   - `general` — general settings:
     - `threads` — number of addresses to be checked simultaneously. It isn't desirable to specify a value greater than `20`.
     - `parse_token_price` — whether to add the dollar balance of each token and the total dollar balance to the results spreadsheet (`true` or `false`).
   - `networks` — list with fine-tune settings for each network:
     - `name` — network name, if not specified it will use the network ID (optional).
     - `rpcs` — list of RPCs from which a random one will be selected for each request.
     - `tokens` — list with token contract addresses, specify `""` to parse coin balance, if you don't specify anything, the coin balance will be parsed (optional).
     - `nfts` — list with information about NFTs whose quantity on balance needs to be parsed (optional):
       - `contract_address` — NFT contract addresses.
       - `token_id` — specific token ID (optional).
9. Run the program again, wait for it to finish and close it.
A total of 5 parsing attempts will be made to successfully complete all failed requests.
If the number of requests is large and the number of RPCs and proxies is small, an error may occur:
`Failed to parse the balances of all tokens and NFTs! Try adding RPC and/or proxies.`
```sh
docker run -it --rm -v $HOME/evm-balance-checker/:/app --name evm-balance-checker evm-balance-checker
```
10. Open the `addresses.xlsx` spreadsheet to view the results.
11. Delete the `addresses.xlsx` and `addresses.db` (if it exists) files.


<h2><p align="center">Source code</p></h2>

1. Install [Python 3.8](https://www.python.org/downloads/).
2. Clone the repository:
```sh
git clone https://github.com/SecorD0/evm-balance-checker
```
3. Go to the repository:
```sh
cd evm-balance-checker
```
4. Set up an environment.
5. Install requirements:
```sh
pip install -r requirements.txt
```
6. Run the `app.py` the first time to create necessary files.
7. Insert addresses to be checked into the `addresses.xlsx` spreadsheet.
8. Optionally insert HTTP/SOCKS5 IPv4 proxies in one of the following formats into the `proxies.txt` file.
```
login:password@proxy:port
http://login:password@proxy:port
socks5://login:password@proxy:port
```
9. Configure the `settings.json`:
   - `general` — general settings:
     - `threads` — number of addresses to be checked simultaneously. It isn't desirable to specify a value greater than `20`.
     - `parse_token_price` — whether to add the dollar balance of each token and the total dollar balance to the results spreadsheet (`true` or `false`).
   - `networks` — list with fine-tune settings for each network:
     - `name` — network name, if not specified it will use the network ID (optional).
     - `rpcs` — list of RPCs from which a random one will be selected for each request.
     - `tokens` — list with token contract addresses, specify `""` to parse coin balance, if you don't specify anything, the coin balance will be parsed (optional).
     - `nfts` — list with information about NFTs whose quantity on balance needs to be parsed (optional):
       - `contract_address` — NFT contract addresses.
       - `token_id` — specific token ID (optional).
10. Run the `app.py` again, wait for it to finish and close it.
A total of 5 parsing attempts will be made to successfully complete all failed requests.
If the number of requests is large and the number of RPCs and proxies is small, an error may occur:
`Failed to parse the balances of all tokens and NFTs! Try adding RPC and/or proxies.`
11. Open the `addresses.xlsx` spreadsheet to view the results.
12. Delete the `addresses.xlsx` and `addresses.db` (if it exists) files.


⠀If you want to build the EXE file by yourself:
- Install `pyinstaller`:
```sh
pip install pyinstaller
```
- Build the EXE file:
```sh
pyinstaller app.py -Fn evm-balance-checker -i images/icons/app.ico --add-binary "images/icons;images/icons" --add-binary "venv/Lib/site-packages/fake_useragent/data;fake_useragent/data"
```



<h1><p align="center">Sample settings</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀Arbitrum ETH, USDC, USDT; Optimism ETH, Optimism quest NFTs.
```json
{
  "general": {
    "threads": 10,
    "parse_token_price": true
  },
  "networks": [
    {
      "name": "arbitrum",
      "rpcs": [
        "https://rpc.ankr.com/arbitrum/",
        "https://endpoints.omniatech.io/v1/arbitrum/one/public"
      ],
      "tokens": [
        "",
        "0xaf88d065e77c8cC2239327C5EDb3A432268e5831",
        "0xFd086bC7CD5C481DCC9C85ebE478A1C0b69FCbb9"
      ]
    },
    {
      "name": "optimism",
      "rpcs": [
        "https://rpc.ankr.com/optimism/",
        "https://endpoints.omniatech.io/v1/op/mainnet/public"
      ],
      "tokens": [],
      "nfts": [
        {
          "contract_address": "0xfA14e1157F35E1dAD95dC3F822A9d18c40e360E2"
        }
      ]
    }
  ]
}
```

⠀Arbitrum ETH, USDC, USDT.
```json
{
  "general": {
    "threads": 10,
    "parse_token_price": true
  },
  "networks": [
    {
      "name": "arbitrum",
      "rpcs": [
        "https://rpc.ankr.com/arbitrum/",
        "https://endpoints.omniatech.io/v1/arbitrum/one/public"
      ],
      "tokens": [
        "",
        "0xaf88d065e77c8cC2239327C5EDb3A432268e5831",
        "0xFd086bC7CD5C481DCC9C85ebE478A1C0b69FCbb9"
      ]
    }
  ]
}
```

⠀Optimism ETH, Optimism quest NFTs.
```json
{
  "general": {
    "threads": 10,
    "parse_token_price": true
  },
  "networks": [
    {
      "name": "optimism",
      "rpcs": [
        "https://rpc.ankr.com/optimism/",
        "https://endpoints.omniatech.io/v1/op/mainnet/public"
      ],
      "tokens": [],
      "nfts": [
        {
          "contract_address": "0xfA14e1157F35E1dAD95dC3F822A9d18c40e360E2"
        }
      ]
    }
  ]
}
```

⠀Polygon ETH
```json
{
  "general": {
    "threads": 10,
    "parse_token_price": true
  },
  "networks": [
    {
      "name": "polygon",
      "rpcs": [
        "https://rpc.ankr.com/polygon/",
        "https://endpoints.omniatech.io/v1/matic/mainnet/public"
      ]
    }
  ]
}
```



<h1><p align="center">Updating</p></h1>
<p align="right"><a href="#Content">To the content</a></p>


<h2><p align="center">Windows</p></h2>

1. Download an EXE file of the new version from the [releases page](https://github.com/SecorD0/evm-balance-checker/releases) and replace the old one with it.


<h2><p align="center">GitHub image</p></h2>

1. Stop the container:
```sh
docker stop evm-balance-checker
```
2. Remove the container:
```sh
docker rm evm-balance-checker
```
3. Update the image:
```sh
docker pull ghcr.io/secord0/evm-balance-checker:main
```


<h2><p align="center">Self-built image</p></h2>

1. Stop the container:
```sh
docker stop evm-balance-checker
```
2. Remove the container:
```sh
docker rm evm-balance-checker
```
3. Go to the repository:
```sh
cd evm-balance-checker
```
4. Update the local files:
```sh
git pull
```
5. Rebuild the image:
```sh
docker build -t evm-balance-checker .
```


<h2><p align="center">Source code</p></h2>

1. Go to the repository:
```sh
cd evm-balance-checker
```
2. Update the local files:
```sh
git pull
```



<h1><p align="center">Useful commands</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀To run the program (GitHub image):
```sh
docker run -it --rm -v $HOME/evm-balance-checker/files:/app/files --name evm-balance-checker ghcr.io/secord0/evm-balance-checker:main
```

⠀To run the program (self-built image):
```sh
docker run -it --rm -v $HOME/evm-balance-checker/:/app --name evm-balance-checker evm-balance-checker
```

⠀To remove the container:
```sh
docker stop evm-balance-checker; docker rm evm-balance-checker
```



<h1><p align="center">Report a bug or suggest an idea</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀If you found a bug or have an idea, go to [the link](https://github.com/SecorD0/evm-balance-checker/issues/new/choose), select the template, fill it out and submit it.



<h1><p align="center">Express your gratitude</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀You can express your gratitude to the developer by sending fund to crypto wallets!
- Address of EVM networks (Ethereum, Polygon, BSC, etc.): `0x900649087b8D7b9f799F880427DacCF2286D8F20`
- USDT TRC-20: `TNpBdjcmR5KzMVCBJTRYMJp16gCkQHu84K`
- SOL: `DoZpXzGj5rEZVhEVzYdtwpzbXR8ifk5bajHybAmZvR4H`
- BTC: `bc1qs4a0c3fntlhzn9j297qdsh3splcju54xscjstc`
