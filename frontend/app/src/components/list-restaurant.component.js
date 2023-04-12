import React, { Component } from "react";
import RestaurantDataService from "../services/restaurant.service";
import { Link } from "react-router-dom";

class RestaurantList extends Component {
    constructor(props){
        super(props);
        this.state = {
            restaurants: []
        };
    }
    

    componentDidMount() {
        RestaurantDataService.getAll()
        .then(response => {
            this.setState({ restaurants: response.data });
          })
          .catch(error => {
            console.log(error);
          });
    }
    render() {
        return (
          <div>
            <h1>Restaurant List</h1>
            <Link to={"/restaurants/add"} className="btn btn-primary">Agregar Restaurant</Link>
            <table className="table">
                <thead>
                    <tr>
                        <th scope="col">Id</th>
                        <th scope="col">Name</th>
                        <th scope="col">Logo</th>
                        <th scope="col">Options</th>
                    </tr>
                </thead>
                <tbody>
                    {
                        this.state.restaurants.map((restaurant) => (
                            <tr key={restaurant.id}>
                                <td>{restaurant.id}</td>
                                <td>{restaurant.name}</td>
                                <td>{restaurant.logo}</td>
                                <td><Link to={`/restaurants/${restaurant.id}`} className="btn btn-warning">Ver</Link></td>
                            </tr>
                        ))
                    }
                </tbody>
            </table>
          </div>
        );
      }
}

export default RestaurantList;