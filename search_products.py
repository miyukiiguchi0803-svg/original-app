
import json
from pathlib import Path

# ==================================
# 1. 商品データを読み込む
# ==================================

data_path = Path("data/products.json")

with data_path.open("r", encoding="utf-8") as file:
    products = json.load(file)


# ==================================
# 2. 検索条件を設定する
# ==================================

search_conditions = {
    "season": "autumn",
    "occasion": "office",
    "style": "elegant",
    "budget": 20000
}


# ==================================
# 3. 条件に合う商品を検索する
# ==================================

matched_products = []

for product in products:

    # 季節が一致するか
    if search_conditions["season"] not in product["seasons"]:
        continue

    # シーンが一致するか
    if search_conditions["occasion"] not in product["occasions"]:
        continue

    # 好みのスタイルが一致するか
    if search_conditions["style"] not in product["style_tags"]:
        continue

    # 予算以内か
    if product["price"] > search_conditions["budget"]:
        continue

    # すべての条件に一致した商品を追加
    matched_products.append(product)


# ==================================
# 4. 検索結果を表示する
# ==================================

print("===== 商品検索結果 =====")
print(f"検索条件: {search_conditions}")
print(f"該当商品数: {len(matched_products)}件")

for product in matched_products:
    print("--------------------")
    print(f"商品名: {product['name']}")
    print(f"ブランド: {product['brand']}")
    print(f"価格: {product['price']:,}円")
    print(f"商品URL: {product['product_url']}")
