from be.api.v1.models.product import Product

products = [
    Product(
        id="1",
        name="Oversized Crew Neck Short Sleeve T-Shirt",
        price=22.90,
        images=[
            ("https://image.uniqlo.com/UQ/ST3/sg/imagesgoods/451406/item/"
             "sggoods_09_451406.jpg?width=1008&impolicy=quality_75")
        ],
        sizes=["xs", "s", "m", "l"],
        colorways=["Black", "White"],
        productCategory="t-shirt",
        sizeChart="https://cdn.ntuscse.com/merch/size-chart/trendlink.png",
        stock={
            "Black": {
                "xs": 5,
                "s": 10,
                "m": 7,
                "l": 12,
            },
            "White": {
                "xs": 5,
                "s": 10,
                "m": 7,
                "l": 12,
            },
        },
        isAvailable=True,
    ),
    # Product(
    #     id="2",
    #     name="AIRism Cotton UV Protection Crew Neck Long Sleeve T-Shirt",
    #     price=19.90,
    #     images=[
    #         ("https://image.uniqlo.com/UQ/ST3/sg/imagesgoods/433037/item/"
    #          "sggoods_67_433037.jpg?width=1008&impolicy=quality_75"
    # )],
    #     sizes=["xs", "s", "m", "l", "xl"],
    #     productCategory="t-shirt",
    # ),
    # Product(
    #     id="3",
    #     name="Square Neck Short Sleeve Cropped T-Shirt",
    #     price=14.90,
    #     images=[
    #         ("https://image.uniqlo.com/UQ/ST3/sg/imagesgoods/452928/item/"
    #          "sggoods_47_452928.jpg?width=1008&impolicy=quality_75")
    #     ],
    #     sizes=["xs", "s", "m", "l", "xl"],
    #     productCategory="t-shirt",
    # ),
    # Product(
    #     id="4",
    #     name="Uniqlo U Crew Neck Short Sleeve T-Shirt",
    #     price=14.90,
    #     images=[
    #         ("https://image.uniqlo.com/UQ/ST3/sg/imagesgoods/424873/item/"
    #          "sggoods_55_424873.jpg?width=1008&impolicy=quality_75")
    #     ],
    #     sizes=["xs", "s", "m", "l", "xl"],
    #     productCategory="t-shirt",
    # ),
    # Product(
    #     id="5",
    #     name="Art Icons UT (Short Sleeve Graphic T-Shirt)",
    #     price=18.90,
    #     images=[
    #         ("https://image.uniqlo.com/UQ/ST3/sg/imagesgoods/424873/item/"
    #          "sggoods_55_424873.jpg?width=1008&impolicy=quality_75")
    #     ],
    #     sizes=["xs", "s", "m", "l", "xl"],
    #     productCategory="t-shirt",
    # ),
    # Product(
    #     id="6",
    #     name="Middle Gauge Knitted Crew Neck Vest",
    #     price=29.90,
    #     images=[
    #         ("https://image.uniqlo.com/UQ/ST3/sg/imagesgoods/451613/item/"
    #          "sggoods_32_451613.jpg?width=1008&impolicy=quality_75")
    #     ],
    #     sizes=["xs", "s", "m", "l", "xl"],
    #     productCategory="sweater",
    # ),
    # Product(
    #     id="7",
    #     name="Peanuts Sunday Specials UT (Short Sleeve Graphic T-Shirt)",
    #     price=14.90,
    #     images=[
    #         ("https://image.uniqlo.com/UQ/ST3/sg/imagesgoods/447871/item/"
    #          "sggoods_40_447871.jpg?width=1600&impolicy=quality_75")
    #     ],
    #     sizes=["xs", "s", "m", "l", "xl"],
    #     productCategory="sweater",
    # ),
    # Product(
    #     id="8",
    #     name="Cotton Blend Parka",
    #     price=59.90,
    #     images=[
    #         ("https://image.uniqlo.com/UQ/ST3/sg/imagesgoods/445135/item/"
    #          "sggoods_30_445135.jpg?width=1008&impolicy=quality_75")
    #     ],
    #     sizes=["xs", "s", "m", "l", "xl"],
    #     productCategory="sweater",
    # ),
]
