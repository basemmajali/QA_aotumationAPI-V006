from apis.api_client import APIClient


class CartsClient(APIClient):
    
    def get_all_carts(self):
        return self.get("/carts")
    
    def get_carts_by_user(self, user_id):
        return self.get(f"/carts/user/{user_id}")
    
    def get_carts_by_date(self, start_date, end_date):
        return self.get(f"/carts?startdate={start_date}&enddate={end_date}")
    
    def get_carts_sorted(self, order="asc"):
        return self.get(f"/carts?sort={order}")
    
    def get_carts_with_limit(self, limit):
        return self.get(f"/carts?limit={limit}")
