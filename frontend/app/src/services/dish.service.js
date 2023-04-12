import http from "../http-common"

class DishDataService {
  getAll() {
    return http.get("/dish");
  }

  get(id) {
    return http.get(`/dish${id}`);
  }

  create(data) {
    return http.post("/dish", data);
  }

  update(id, data) {
    return http.put(`/dish/${id}`, data);
  }

  delete(id) {
    return http.delete(`/dish/${id}`);
  }
}

export default new DishDataService();