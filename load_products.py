
import json
from pathlib import Path

# JSONファイルを読み込む
data_path = Path("data/products.json")

with data_path.open("r", encoding="utf-8") as file:
    products = json.load(file)

# 必須項目
required_fields = [
    "id",
    "name",
    "brand",
    "category",
    "price",
    "colors",
    "seasons",
    "occasions",
    "style_tags",
    "product_url",
    "image_url"
]

errors = []
product_ids = []

# 商品データを1件ずつ検証
for product in products:

    # 必須項目の確認
    for field in required_fields:
        if field not in product:
            errors.append(
                f"{product.get('id', '不明')}: {field} がありません"
            )

    # IDの重複確認
    product_id = product.get("id")

    if product_id in product_ids:
        errors.append(f"IDが重複しています: {product_id}")
    else:
        product_ids.append(product_id)

    # 商品名の確認
    if not product.get("name"):
        errors.append(f"{product_id}: 商品名が空欄です")

    # 価格の確認（boolは数値として扱わない）
    price = product.get("price")

    if isinstance(price, bool) or not isinstance(price, (int, float)) or price < 0:
        errors.append(f"{product_id}: 価格が正しくありません")

    # 商品URLの確認
    if not product.get("product_url"):
        errors.append(f"{product_id}: 商品URLがありません")

# 検証結果
print(f"検証商品数: {len(products)}")

if errors:
    print("検証結果: エラーあり")
    for error in errors:
        print(error)
else:
    print("検証結果: すべて正常です！")
