import http from "../http-common"

class RestaurantDataService {
  getAll() {
    return http.get("/restaurant");
  }

  get(id) {
    return http.get(`/restaurant/${id}`);
  }

  create(data) {
    return http.post("/restaurant", data);
  }

  update(id, data) {
    return http.put(`/restaurant/${id}`, data);
  }

  delete(id) {
    return http.delete(`/restaurant/${id}`);
  }
}

export default new RestaurantDataService();