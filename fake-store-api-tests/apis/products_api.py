from apis.api_client import APIClient


class ProductsClient(APIClient):
    
    def get_all_products(self):
        return self.get("/products")
    
    def get_product_by_id(self, product_id):
        return self.get(f"/products/{product_id}")
    
    def get_categories(self):
        return self.get("/products/categories")
    
    def get_products_with_limit(self, limit):
        return self.get(f"/products?limit={limit}")
    
    def get_products_sorted(self, order="asc"):
        return self.get(f"/products?sort={order}")
