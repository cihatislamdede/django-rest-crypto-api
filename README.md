# Django Rest Framework - Crypto Assets API

<h3><b>GET</b> <i>/assets.json</i> </h3>

```json
[
    {
        "id": "bitcoin",
        "symbol": "BTC",
        "name": "Bitcoin",
        "explorer": "https://blockchain.info/"
    },
    {
        "id": "ethereum",
        "symbol": "ETH",
        "name": "Ethereum",
        "explorer": "https://etherscan.io/"
    },
    {
        "id": "algorand",
        "symbol": "ALGO",
        "name": "Algorand",
        "explorer": "https://algoexplorer.io/"
    }
    ...
]
```

<h3><b>POST</b> <i>/assets</i> </h3>
Example body: 

```json
{
    "id": "algorand",
    "symbol": "ALGO",
    "name": "Algorand",
    "explorer": "https://algoexplorer.io/"
} 
```


<h3><b>GET</b> <i>/assets/{id}</i> </h3>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Get the asset with id = ALGO

```json
{
    "id": "algorand",
    "symbol": "ALGO",
    "name": "Algorand",
    "explorer": "https://algoexplorer.io/"
}
```

<h3><b>PUT</b> <i>/assets/{id}</i> </h3>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Update the asset with id = ALGO

```json
{
    "id": "algorand",
    "symbol": "ALGO",
    "name": "Algorand",
    "explorer": "https://goalseeker.purestake.io/algorand/mainnet"
}
```

<h3><b>DELETE</b> <i>/assets/{id}</i> </h3>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Delete the asset with id

<br>

##
<h2>

Source: [https://www.django-rest-framework.org/tutorial/quickstart/](https://www.django-rest-framework.org/tutorial/quickstart/)
</h2>
